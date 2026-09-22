"""The DeepSeek transport: one request, saved as sent, and the reply, saved as returned.

A RULE (run_deepseek.py is the driver). Nothing here runs on import and nothing here is sent
unless a driver calls send().

The service, as its documentation has it (CLAIMED, read 22 September 2026):
  https://api-docs.deepseek.com/api/create-chat-completion/ - the models listed are
    "deepseek-flash" and "deepseek-v4-pro"; "reasoning_effort" "Controls the thinking mode
    toggle and the thinking effort. `none` disables thinking mode; `low` / `high` / `max`
    enable thinking mode."; max_tokens' "maximum allowable value is 384K (393,216 tokens)";
    the prefix field: "(Beta) Set this to `true` to force the model to start its answer by the
    content of the supplied prefix in this `assistant` message."
  https://api-docs.deepseek.com/guides/chat_prefix_completion/ - "set base_url=
    "https://api.deepseek.com/beta" to enable the Beta feature", and the last message must have
    role assistant with prefix true.
The model, the effort and the endpoint the old rig used are seen, not claimed: plan 49 rig,
run.py, `URL = "https://api.deepseek.com/chat/completions"`, `MODEL = "deepseek-flash"`,
`EFFORT = "high"`.

Not settled here, and the first live call settles it: whether the beta prefix endpoint accepts
thinking mode on deepseek-flash. The documentation at the address above does not say. If the
service refuses it, the driver stops that run and writes the service's own words into
<run>.failed.json; it does not quietly drop thinking and carry on, because a run made under a
different thinking setting is a different arm.

The client seam. A6 of stage A writes clients/deepseek_client.py. If that file is on the path
this module uses it and records `"client": "clients.deepseek_client"` in every call record;
otherwise it uses the poster below and records `"client": "deepseek_transport"`. The record is
the gauge: no run can be read without knowing which client sent it.
"""
import os, sys, json, time, threading
try:
    import requests
except ImportError:
    requests = None

URL = "https://api.deepseek.com/chat/completions"
URL_BETA = "https://api.deepseek.com/beta/chat/completions"
MODEL = "deepseek-flash"
EFFORT = "high"
# W10 section 2: "token spend not limited". The documented maximum is 384K (393,216 tokens) and
# A6's clients/deepseek_client.py defaults to it; this constant is the value actually sent, so a
# lower number here was the ceiling whatever the client's default said (fault 14 of the stage-A
# review). The ceiling costs nothing unused and a truncated report is a lost run: arm (e)'s
# prefixed report and arm (d)'s 24-answer assembler are the long calls. finish_reason is saved
# per call in the reply record, so a truncation shows.
MAX_TOKENS = 393216       # the documented maximum. Lower it for one run with --max-tokens.
_lock = threading.Lock()

CLIENT = "deepseek_transport"
_ext = None
try:
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from clients.deepseek_client import send as _ext          # A6 writes this; absent today
    CLIENT = "clients.deepseek_client"
except Exception:
    _ext = None


def body_for(messages, tools=None, prefix=False, max_tokens=MAX_TOKENS,
             effort=EFFORT, model=MODEL, stream=True):
    b = {"model": model, "messages": messages, "max_tokens": max_tokens,
         "thinking": {"type": "enabled"}, "reasoning_effort": effort, "stream": stream}
    if stream:
        b["stream_options"] = {"include_usage": True}
    if tools:
        b["tools"] = tools
    b["_endpoint"] = URL_BETA if prefix else URL      # stripped before sending; kept in the record
    return b


def _strip(body):
    b = dict(body)
    b.pop("_endpoint", None)
    return b


def send(body, key, tag="", stream_path=None, tries=7):
    """Send one request. Returns (message, finish_reason, usage, http). Saves nothing:
    the driver saves the body before this is called and the reply after it returns."""
    if _ext is not None:
        return _ext(body, key, tag=tag, stream_path=stream_path, tries=tries)
    if requests is None:
        raise SystemExit("the requests package is not installed. Nothing sent.")
    url = body.get("_endpoint", URL)
    payload = _strip(body)
    stream = bool(payload.get("stream"))
    delay, err = 4, ""
    for _ in range(tries):
        try:
            r = requests.post(url, json=payload, timeout=(30, 900), stream=stream,
                              headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"})
            if r.status_code in (400, 401, 402, 422):
                raise SystemExit(f"{tag}: stopped, HTTP {r.status_code} {r.text[:400]}")
            if r.status_code != 200:
                raise RuntimeError(f"HTTP {r.status_code} {r.text[:200]}")
            if not stream:
                d = r.json()
                ch = (d.get("choices") or [{}])[0]
                return ch.get("message", {}), ch.get("finish_reason"), d.get("usage", {}), d
            content, reasoning, finish, usage, tcs, raw = [], [], None, {}, {}, []
            for line in r.iter_lines():
                if not line:
                    continue
                s = line.decode("utf-8", "ignore")
                raw.append(s)
                if not s.startswith("data:"):
                    continue
                data = s[5:].strip()
                if data == "[DONE]":
                    break
                ch = json.loads(data)
                if ch.get("usage"):
                    usage = ch["usage"]
                for c in ch.get("choices", []):
                    d = c.get("delta", {}) or {}
                    if d.get("content"):
                        content.append(d["content"])
                    if d.get("reasoning_content"):
                        reasoning.append(d["reasoning_content"])
                    for tc in d.get("tool_calls") or []:
                        i = tc.get("index", 0)
                        slot = tcs.setdefault(i, {"id": "", "type": "function",
                                                  "function": {"name": "", "arguments": ""}})
                        if tc.get("id"):
                            slot["id"] = tc["id"]
                        f = tc.get("function") or {}
                        if f.get("name"):
                            slot["function"]["name"] += f["name"]
                        if f.get("arguments"):
                            slot["function"]["arguments"] += f["arguments"]
                    if c.get("finish_reason"):
                        finish = c["finish_reason"]
            if stream_path:
                os.makedirs(os.path.dirname(stream_path), exist_ok=True)
                with open(stream_path, "w", encoding="utf-8") as f:
                    f.write("\n".join(raw))
            msg = {"content": "".join(content), "reasoning_content": "".join(reasoning),
                   "tool_calls": [tcs[i] for i in sorted(tcs)] or None}
            return msg, finish, usage, {"stream_lines": len(raw), "saved": stream_path}
        except SystemExit:
            raise
        except Exception as e:
            err = repr(e)[:200]
        with _lock:
            print(f"  {tag}: retry after {err}", file=sys.stderr, flush=True)
        time.sleep(delay)
        delay = min(delay * 2, 90)
    raise RuntimeError(f"{tag}: gave up, {err}")


def cost(usages):
    """The old rig's off-peak arithmetic, kept so two rounds can be compared:
    cache-hit 0.003, cache-miss 0.15, out 0.6 per million (plan 49 rig, run.py, cost_so_far)."""
    hit = sum(u.get("prompt_cache_hit_tokens", 0) for u in usages)
    miss = sum(u.get("prompt_cache_miss_tokens", 0) or
               (u.get("prompt_tokens", 0) - u.get("prompt_cache_hit_tokens", 0)) for u in usages)
    out = sum(u.get("completion_tokens", 0) for u in usages)
    return hit, miss, out, hit / 1e6 * 0.003 + miss / 1e6 * 0.15 + out / 1e6 * 0.6
