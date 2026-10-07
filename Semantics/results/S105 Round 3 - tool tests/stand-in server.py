#!/usr/bin/env python3
"""A local stand-in for an Anthropic-format endpoint that plays a scripted model: on each main-loop request it answers
with the next tool call of the script (one per turn), and after the last one with a text ending END OF REPORT. Every
request is recorded (auth headers redacted), with the tool results that came back, so what Claude Code allowed and what
it refused can be read afterwards. No key is involved: the caller runs Claude Code with a dummy token.
Usage: standin_tools.py PORT LOG.jsonl SCRIPT.json   (runs until killed by its starter, by exact PID)."""
import json, sys, time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

PORT, OUT, SCRIPT = int(sys.argv[1]), sys.argv[2], json.load(open(sys.argv[3]))


def record(entry):
    with open(OUT, "a") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


class H(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def log_message(self, *a):
        pass

    def _body(self):
        n = int(self.headers.get("content-length") or 0)
        raw = self.rfile.read(n) if n else b""
        if self.headers.get("content-encoding") == "gzip":
            import gzip
            raw = gzip.decompress(raw)
        return raw

    def _plain(self, code, obj=None):
        out = json.dumps(obj or {}).encode()
        self.send_response(code)
        self.send_header("content-type", "application/json")
        self.send_header("content-length", str(len(out)))
        self.end_headers()
        self.wfile.write(out)

    def do_HEAD(self):
        record({"t": time.time(), "method": "HEAD", "path": self.path})
        self.send_response(200)
        self.send_header("content-length", "0")
        self.end_headers()

    def do_GET(self):
        record({"t": time.time(), "method": "GET", "path": self.path})
        self._plain(404)

    def do_POST(self):
        raw = self._body()
        try:
            req = json.loads(raw) if raw else {}
        except Exception:
            req = {}
        path = self.path.split("?")[0]
        if "count_tokens" in path:
            record({"t": time.time(), "method": "POST", "path": self.path, "kind": "count_tokens"})
            return self._plain(200, {"input_tokens": 10})
        if not path.endswith("/v1/messages"):
            record({"t": time.time(), "method": "POST", "path": self.path, "kind": "other"})
            return self._plain(404)
        tools = [t.get("name") for t in req.get("tools") or []]
        msgs = req.get("messages") or []
        n_assist = sum(1 for m in msgs if m.get("role") == "assistant")
        results = []
        if msgs and msgs[-1].get("role") == "user" and isinstance(msgs[-1].get("content"), list):
            for b in msgs[-1]["content"]:
                if b.get("type") == "tool_result":
                    c = b.get("content")
                    if isinstance(c, list):
                        c = " ".join(x.get("text", "") for x in c if isinstance(x, dict))
                    results.append({"id": b.get("tool_use_id"), "is_error": b.get("is_error"), "content": str(c)[:3000]})
        system = req.get("system")
        sys_text = json.dumps(system)[:400] if system else ""
        main = bool(tools)
        record({"t": time.time(), "method": "POST", "path": self.path, "kind": "main" if main else "side",
                "model": req.get("model"), "tools": tools, "n_messages": len(msgs), "n_assistant": n_assist,
                "tool_results": results, "system_head": sys_text,
                "last_user_head": (json.dumps(msgs[-1])[:600] if msgs and not main else None)})
        if main and n_assist == 0:
            with open(OUT + ".first.json", "w") as f:
                json.dump({"headers": {k: ("[redacted]" if k.lower() in ("authorization", "x-api-key") else v)
                                       for k, v in self.headers.items()}, "body": req}, f, ensure_ascii=False, indent=1)
        if main and n_assist < len(SCRIPT):
            step = SCRIPT[n_assist]
            block = {"type": "tool_use", "id": "toolu_%02d" % n_assist, "name": step["name"], "input": {}}
            delta = {"type": "input_json_delta", "partial_json": json.dumps(step["input"])}
            stop = "tool_use"
        else:
            block = {"type": "text", "text": ""}
            delta = {"type": "text_delta", "text": "stand-in: script done.\nEND OF REPORT" if main else "none"}
            stop = "end_turn"
        msg = {"id": "msg_standin_%d" % n_assist, "type": "message", "role": "assistant",
               "model": (req.get("model") or "?"), "content": [], "stop_reason": None, "stop_sequence": None,
               "usage": {"input_tokens": 10, "output_tokens": 1}}
        if not req.get("stream"):
            b = dict(block)
            if b["type"] == "tool_use":
                b["input"] = step["input"]
            else:
                b["text"] = delta["text"]
            msg.update(content=[b], stop_reason=stop)
            return self._plain(200, msg)
        self.send_response(200)
        self.send_header("content-type", "text/event-stream")
        self.send_header("cache-control", "no-cache")
        self.send_header("connection", "close")
        self.end_headers()

        def ev(name, data):
            self.wfile.write(("event: %s\ndata: %s\n\n" % (name, json.dumps(data))).encode())
            self.wfile.flush()
        ev("message_start", {"type": "message_start", "message": msg})
        ev("content_block_start", {"type": "content_block_start", "index": 0, "content_block": block})
        ev("content_block_delta", {"type": "content_block_delta", "index": 0, "delta": delta})
        ev("content_block_stop", {"type": "content_block_stop", "index": 0})
        ev("message_delta", {"type": "message_delta", "delta": {"stop_reason": stop, "stop_sequence": None},
                             "usage": {"output_tokens": 5}})
        ev("message_stop", {"type": "message_stop"})
        self.close_connection = True


ThreadingHTTPServer(("127.0.0.1", PORT), H).serve_forever()
