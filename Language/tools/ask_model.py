#!/usr/bin/env python3
"""ask_model.py: one call to an outside model, with a receipt.

Providers (keys from the environment, never from a file in the repository):
  atria  POST https://api.atria-asi.ai/v1/chat/completions      model Atria-Dawn-Preview   30 requests/minute   ATRIA_API_KEY
  mimo   POST https://token-plan-sgp.xiaomimimo.com/v1/chat/completions  model mimo-v2.6-pro  100 requests/minute  MIMO_API_KEY
Both are OpenAI-shaped and return `reasoning_content` beside `content`; the receipt keeps both.

Usage:
  ask_model.py PROVIDER --system FILE --user FILE --out DIR [--tag NAME] [--max-tokens N] [--temperature T]
Writes DIR/<tag>.response.txt (the content), DIR/<tag>.reasoning.txt, DIR/<tag>.receipt.json
(provider, model, request SHA-256, response id from the provider, token counts, timings, attempt count),
and DIR/<tag>.request.json (the exact request body). Exit 0 on success. Retries on 429/5xx/timeouts
with backoff, at most 6 attempts; a 400/401/403/404/413/422 is not retried; an answer with empty content is retried. A failed call leaves DIR/<tag>.error.txt and a receipt with "failed": true. Rate limit kept per provider by a
lock file in DIR, or in $ASK_MODEL_LOCKDIR when set (so every step of one run shares one lock).
Written under decision L11, 22 September 2026. A new version is a new file beside this one.
"""
import argparse, hashlib, json, os, sys, time, urllib.request, urllib.error, fcntl

PROVIDERS = {
    "atria": dict(url="https://api.atria-asi.ai/v1/chat/completions", model="Atria-Dawn-Preview", key="ATRIA_API_KEY", rpm=30),
    "mimo":  dict(url="https://token-plan-sgp.xiaomimimo.com/v1/chat/completions", model="mimo-v2.6-pro", key="MIMO_API_KEY", rpm=100),
}

def wait_for_slot(lockdir, provider, rpm):
    """Crude but safe: one call per (60/rpm) seconds per provider, serialised by a lock file."""
    lockdir = os.environ.get("ASK_MODEL_LOCKDIR") or lockdir   # a shared lock dir for a whole run
    path = os.path.join(lockdir, ".rate_%s" % provider)
    with open(path, "a+") as f:
        fcntl.flock(f, fcntl.LOCK_EX)
        f.seek(0); last = float(f.read().strip() or 0)
        gap = 60.0 / rpm * 1.1   # a tenth over the minimum gap, so a fixed-window count never reaches rpm + 1
        now = time.time()
        if now - last < gap: time.sleep(gap - (now - last))
        f.seek(0); f.truncate(); f.write(str(time.time())); f.flush()
        fcntl.flock(f, fcntl.LOCK_UN)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("provider", choices=PROVIDERS)
    ap.add_argument("--system"); ap.add_argument("--user", required=True); ap.add_argument("--out", required=True)
    ap.add_argument("--tag", default="call"); ap.add_argument("--max-tokens", type=int, default=16000)
    ap.add_argument("--temperature", type=float, default=0.2)
    a = ap.parse_args()
    p = PROVIDERS[a.provider]
    key = os.environ.get(p["key"])
    if not key: print("no %s in the environment" % p["key"], file=sys.stderr); return 2
    os.makedirs(a.out, exist_ok=True)
    messages = []
    if a.system: messages.append({"role": "system", "content": open(a.system).read()})
    messages.append({"role": "user", "content": open(a.user).read()})
    body = {"model": p["model"], "messages": messages, "max_tokens": a.max_tokens, "temperature": a.temperature}
    raw = json.dumps(body, ensure_ascii=False, sort_keys=True).encode()
    req_hash = hashlib.sha256(raw).hexdigest()
    open(os.path.join(a.out, a.tag + ".request.json"), "wb").write(raw)
    attempts, started = 0, time.time()
    while True:
        attempts += 1
        wait_for_slot(a.out, a.provider, p["rpm"])
        req = urllib.request.Request(p["url"], data=raw, method="POST",
              headers={"Authorization": "Bearer " + key, "Content-Type": "application/json"})
        t0 = time.time()
        try:
            with urllib.request.urlopen(req, timeout=2400) as r: text = r.read().decode()
            status = 200
        except urllib.error.HTTPError as e:
            status, text = e.code, e.read().decode(errors="replace")
        except Exception as e:
            status, text = 0, repr(e)
        seconds = time.time() - t0
        if status == 200:
            try: data = json.loads(text)
            except Exception: status = -1
        if status == 200 and data.get("choices") and ((data["choices"][0].get("message") or {}).get("content") or "").strip(): break
        if status == 200: status = -2   # a well-formed answer with no content: retried like a failure
        final = status in (400, 401, 403, 404, 413, 422)   # a request the provider rejects outright: no retry
        if final or attempts >= 6:
            open(os.path.join(a.out, a.tag + ".error.txt"), "w").write("status %s after %d attempt(s)%s\n%s" % (status, attempts, " (not retried)" if final else "", text[:4000]))
            open(os.path.join(a.out, a.tag + ".receipt.json"), "w").write(json.dumps({"provider": a.provider, "url": p["url"], "model": p["model"], "request_sha256": req_hash,
                "failed": True, "status": status, "attempts": attempts, "seconds": round(time.time() - started, 1), "tag": a.tag, "user_file": a.user, "asked_at_unix": int(started)}, indent=1))
            print("failed after %d attempt(s): status %s%s" % (attempts, status, " (not retried)" if final else ""), file=sys.stderr); return 1
        time.sleep(min(120, 5 * 2 ** attempts))
    msg = data["choices"][0]["message"]
    content = msg.get("content") or ""
    reasoning = msg.get("reasoning_content") or ""
    open(os.path.join(a.out, a.tag + ".response.txt"), "w").write(content)
    open(os.path.join(a.out, a.tag + ".reasoning.txt"), "w").write(reasoning)
    receipt = {"provider": a.provider, "url": p["url"], "model": data.get("model", p["model"]), "request_sha256": req_hash,
               "response_id": data.get("id"), "created": data.get("created"), "finish_reason": data["choices"][0].get("finish_reason"),
               "usage": data.get("usage"), "seconds": round(seconds, 1), "attempts": attempts,
               "response_sha256": hashlib.sha256(content.encode()).hexdigest(), "tag": a.tag,
               "system_file": a.system, "user_file": a.user, "asked_at_unix": int(started)}
    open(os.path.join(a.out, a.tag + ".receipt.json"), "w").write(json.dumps(receipt, indent=1))
    print("%s %s: %d chars, %s, %.0fs" % (a.provider, a.tag, len(content), receipt["usage"] and receipt["usage"].get("total_tokens"), seconds))
    return 0

if __name__ == "__main__": sys.exit(main())
