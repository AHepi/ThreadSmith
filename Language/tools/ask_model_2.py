#!/usr/bin/env python3
"""ask_model_2.py: one streamed call to an outside model, with a receipt. Second version of ask_model.py (6736ac6793471387),
kept beside it. Give-up line: ask_model.py's non-streaming request died at 301 s on every Atria attempt of the first Arm B
run (22 September 2026, 16:33; RemoteDisconnected after 301 s, six times per text), while its pilot calls under 300 s had
succeeded; Mimo's reasoning ran past the 2400 s socket timeout on hard texts. This version streams (`stream: true`), so the
connection carries bytes throughout, and times out on silence (no chunk for --idle seconds), not on the whole call.

Providers (keys from the environment, never from a file in the repository):
  atria  POST https://api.atria-asi.ai/v1/chat/completions      model Atria-Dawn-Preview   30 requests/minute   ATRIA_API_KEY
  mimo   POST https://token-plan-sgp.xiaomimimo.com/v1/chat/completions  model mimo-v2.6-pro  100 requests/minute  MIMO_API_KEY
Both are OpenAI-shaped; streamed chunks carry `delta.content` and `delta.reasoning_content`; the receipt keeps both.

Usage:
  ask_model_2.py PROVIDER --system FILE --user FILE --out DIR [--tag NAME] [--max-tokens N] [--temperature T] [--idle S] [--effort low|medium|high] [--attempts N] [--extra JSON]
(--effort is sent as `reasoning_effort`, which both providers accept; the request body records it)
Writes DIR/<tag>.response.txt (the content), DIR/<tag>.reasoning.txt, DIR/<tag>.receipt.json (provider, model, request
SHA-256, response id, token counts when the stream's last chunk carries usage, finish reason, chunk count, the last attempt's
seconds, the whole call's total_seconds, attempt count and the labelled status and seconds of every attempt, "stream": true),
and DIR/<tag>.request.json (the exact request body). Exit 0 on success. Retries on 429/5xx/disconnects/silence with backoff,
at most 6 attempts; a 400/401/403/404/413/422 is not retried; an empty answer whose finish reason is `length` is not retried
(the same cap gives the same answer) and is recorded as status -4; an empty answer with no finish reason (a stream that
carried chunks and then closed cleanly, Atria's cut) or with any finish reason other than `length` is retried (-2); a 200
whose stream yields no parsable chunk (-3; a chunk that does not parse is skipped, so an unparsable body arrives as no
chunks); a raised exception (0): a connection closed without any response, a reset, or silence for --idle seconds. A failed call leaves DIR/<tag>.error.txt and a
receipt with "failed": true. Rate limit kept per provider by a lock file in DIR, or in $ASK_MODEL_LOCKDIR when set.
Written under decision L11, 22 September 2026.
"""
import argparse, hashlib, json, os, socket, sys, time, urllib.request, urllib.error, fcntl

PROVIDERS = {
    "atria": dict(url="https://api.atria-asi.ai/v1/chat/completions", model="Atria-Dawn-Preview", key="ATRIA_API_KEY", rpm=30),
    "mimo":  dict(url="https://token-plan-sgp.xiaomimimo.com/v1/chat/completions", model="mimo-v2.6-pro", key="MIMO_API_KEY", rpm=100),
}

def wait_for_slot(lockdir, provider, rpm):
    """One call per (60/rpm × 1.1) seconds per provider, serialised by a lock file."""
    lockdir = os.environ.get("ASK_MODEL_LOCKDIR") or lockdir
    path = os.path.join(lockdir, ".rate_%s" % provider)
    with open(path, "a+") as f:
        fcntl.flock(f, fcntl.LOCK_EX)
        f.seek(0); last = float(f.read().strip() or 0)
        gap = 60.0 / rpm * 1.1
        now = time.time()
        if now - last < gap: time.sleep(gap - (now - last))
        f.seek(0); f.truncate(); f.write(str(time.time())); f.flush()
        fcntl.flock(f, fcntl.LOCK_UN)

def stream(url, key, raw, idle):
    """One streamed request. Returns (content, reasoning, finish, last_chunk, chunks, response_id); raises on an HTTP error, on silence for `idle` seconds, or on a closed connection."""
    req = urllib.request.Request(url, data=raw, method="POST",
          headers={"Authorization": "Bearer " + key, "Content-Type": "application/json", "Accept": "text/event-stream"})
    content, reasoning, finish, last, chunks, rid = "", "", None, None, 0, None
    with urllib.request.urlopen(req, timeout=idle) as r:   # the timeout is per read: silence for `idle` seconds raises
        for line in r:
            line = line.decode(errors="replace").strip()
            if not line.startswith("data:"): continue
            data = line[5:].strip()
            if data == "[DONE]": break
            try: d = json.loads(data)
            except Exception: continue
            chunks += 1; last = d; rid = d.get("id", rid)
            for ch in d.get("choices") or []:
                delta = ch.get("delta") or {}
                content += delta.get("content") or ""; reasoning += delta.get("reasoning_content") or ""
                if ch.get("finish_reason"): finish = ch["finish_reason"]
    return content, reasoning, finish, last, chunks, rid

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("provider", choices=PROVIDERS)
    ap.add_argument("--system"); ap.add_argument("--user", required=True); ap.add_argument("--out", required=True)
    ap.add_argument("--tag", default="call"); ap.add_argument("--max-tokens", type=int, default=16000)
    ap.add_argument("--temperature", type=float, default=0.2); ap.add_argument("--idle", type=float, default=600.0)
    ap.add_argument("--effort", choices=["low", "medium", "high"], help="sent as reasoning_effort; omitted means the provider's default")
    ap.add_argument("--attempts", type=int, default=6, help="at most this many HTTP attempts (default 6)")
    ap.add_argument("--extra", help="a JSON object merged into the request body (for provider-specific fields such as a reasoning budget); recorded in the request file")
    a = ap.parse_args()
    p = PROVIDERS[a.provider]
    key = os.environ.get(p["key"])
    if not key: print("no %s in the environment" % p["key"], file=sys.stderr); return 2
    os.makedirs(a.out, exist_ok=True)
    messages = []
    if a.system: messages.append({"role": "system", "content": open(a.system).read()})
    messages.append({"role": "user", "content": open(a.user).read()})
    body = {"model": p["model"], "messages": messages, "max_tokens": a.max_tokens, "temperature": a.temperature, "stream": True}
    if a.effort: body["reasoning_effort"] = a.effort
    if a.extra: body.update(json.loads(a.extra))
    raw = json.dumps(body, ensure_ascii=False, sort_keys=True).encode()
    req_hash = hashlib.sha256(raw).hexdigest()
    open(os.path.join(a.out, a.tag + ".request.json"), "wb").write(raw)
    attempts, started, history = 0, time.time(), []
    content = reasoning = ""; finish = last = rid = None; chunks = 0; text = ""
    while True:
        attempts += 1
        content = reasoning = ""; finish = last = rid = None; chunks = 0; text = ""   # each attempt starts clean
        wait_for_slot(a.out, a.provider, p["rpm"])
        t0 = time.time()
        try:
            content, reasoning, finish, last, chunks, rid = stream(p["url"], key, raw, a.idle); status = 200; text = ""
        except urllib.error.HTTPError as e:
            status, text = e.code, e.read().decode(errors="replace")
        except (socket.timeout, TimeoutError) as e:
            status, text = 0, "silence for %.0f s: %r" % (a.idle, e)
        except Exception as e:
            status, text = 0, repr(e)
        seconds = time.time() - t0
        if status == 200 and not chunks: status = -3
        elif status == 200 and not content.strip(): status = -4 if finish == "length" else -2
        history.append({"attempt": attempts, "status": status, "seconds": round(seconds, 1), "finish": finish, "chunks": chunks})   # this attempt's own, reset at the top of the loop
        if status == 200: break
        final = status in (400, 401, 403, 404, 413, 422, -4)
        if final or attempts >= a.attempts:
            open(os.path.join(a.out, a.tag + ".error.txt"), "w").write("status %s after %d attempt(s)%s\nfinish %s, %d chunks, %d reasoning chars, %d content chars\n%s" % (
                status, attempts, " (not retried)" if final else "", finish, chunks, len(reasoning), len(content), text[:4000]))
            open(os.path.join(a.out, a.tag + ".reasoning.txt"), "w").write(reasoning)
            open(os.path.join(a.out, a.tag + ".receipt.json"), "w").write(json.dumps({"provider": a.provider, "url": p["url"], "model": p["model"], "request_sha256": req_hash,
                "failed": True, "status": status, "finish_reason": finish, "chunks": chunks, "attempts": attempts, "attempt_history": history, "seconds": round(seconds, 1),
                "total_seconds": round(time.time() - started, 1), "usage": (last or {}).get("usage"), "stream": True, "tag": a.tag, "user_file": a.user, "asked_at_unix": int(started)}, indent=1))
            print("failed after %d attempt(s): status %s%s" % (attempts, status, " (not retried)" if final else ""), file=sys.stderr); return 1
        time.sleep(min(120, 5 * 2 ** attempts))
    open(os.path.join(a.out, a.tag + ".response.txt"), "w").write(content)
    open(os.path.join(a.out, a.tag + ".reasoning.txt"), "w").write(reasoning)
    receipt = {"provider": a.provider, "url": p["url"], "model": (last or {}).get("model", p["model"]), "request_sha256": req_hash,
               "response_id": rid, "created": (last or {}).get("created"), "finish_reason": finish, "chunks": chunks,
               "usage": (last or {}).get("usage"), "seconds": round(seconds, 1), "total_seconds": round(time.time() - started, 1), "attempts": attempts, "attempt_history": history, "effort": a.effort,
               "response_sha256": hashlib.sha256(content.encode()).hexdigest(), "stream": True, "tag": a.tag,
               "system_file": a.system, "user_file": a.user, "asked_at_unix": int(started)}
    open(os.path.join(a.out, a.tag + ".receipt.json"), "w").write(json.dumps(receipt, indent=1))
    print("%s %s: %d chars, %s, %.0fs, %d chunks" % (a.provider, a.tag, len(content), (receipt["usage"] or {}).get("total_tokens"), seconds, chunks))
    return 0

if __name__ == "__main__": sys.exit(main())
