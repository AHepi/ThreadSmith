#!/usr/bin/env python3
"""s80_call.py: one streamed call to an outside model, with a receipt. Written for round S80 (does the hard-to-vary
skill add anything), 23 September 2026, from the pattern of Language/tools/ask_model_2.py (read, not copied across
projects' records: this file is the Semantics project's own).

Providers (keys from the environment only, never from a file in the repository):
  atria     https://api.atria-asi.ai/v1/chat/completions             Atria-Dawn-Preview  ATRIA_API_KEY
  mimo      https://token-plan-sgp.xiaomimimo.com/v1/chat/completions mimo-v2.6-pro       MIMO_API_KEY
  deepseek  https://api.deepseek.com/chat/completions                 deepseek-v4-pro     DEEPSEEK_API_KEY
Thinking is switched with the body field `thinking: {"type": "enabled"|"disabled"}`, which all three accept
(probe of 23 September: reasoning tokens 0 with it disabled on each).

call(provider, system, user, out_dir, tag, thinking, max_tokens) writes <tag>.response.txt, <tag>.reasoning.txt,
<tag>.request.json and <tag>.receipt.json in out_dir; on failure <tag>.error.txt and a receipt with "failed": true.
Retries on 429, 5xx, disconnects, silence and empty answers, at most 5 attempts; 400/401/403/404/413/422 not retried.
"""
import hashlib, json, os, time
import requests

PROVIDERS = {
    "atria": ("https://api.atria-asi.ai/v1/chat/completions", "Atria-Dawn-Preview", "ATRIA_API_KEY"),
    "mimo": ("https://token-plan-sgp.xiaomimimo.com/v1/chat/completions", "mimo-v2.6-pro", "MIMO_API_KEY"),
    "deepseek": ("https://api.deepseek.com/chat/completions", "deepseek-v4-pro", "DEEPSEEK_API_KEY"),
}
FINAL = {400, 401, 403, 404, 413, 422}


def _stream(url, key, body, idle):
    content, reasoning, finish, last, chunks = "", "", None, None, 0
    with requests.post(url, json=body, stream=True, timeout=(30, idle),
                       headers={"Authorization": "Bearer " + key, "Accept": "text/event-stream"}) as r:
        if r.status_code != 200:
            return r.status_code, r.text[:4000], None
        for line in r.iter_lines(decode_unicode=True):
            if not line or not line.startswith("data:"):
                continue
            data = line[5:].strip()
            if data == "[DONE]":
                break
            try:
                d = json.loads(data)
            except Exception:
                continue
            chunks += 1; last = d
            for ch in d.get("choices") or []:
                delta = ch.get("delta") or {}
                content += delta.get("content") or ""
                reasoning += delta.get("reasoning_content") or ""
                if ch.get("finish_reason"):
                    finish = ch["finish_reason"]
    return 200, "", dict(content=content, reasoning=reasoning, finish=finish, last=last, chunks=chunks)


def call(provider, system, user, out_dir, tag, thinking, max_tokens=48000, idle=900, attempts=5):
    url, model, keyname = PROVIDERS[provider]
    key = os.environ[keyname]
    os.makedirs(out_dir, exist_ok=True)
    p = lambda ext: os.path.join(out_dir, tag + ext)
    if os.path.exists(p(".response.txt")):
        return "skipped"
    messages = ([{"role": "system", "content": system}] if system else []) + [{"role": "user", "content": user}]
    body = {"model": model, "messages": messages, "max_tokens": max_tokens, "stream": True,
            "stream_options": {"include_usage": True},
            "thinking": {"type": "enabled" if thinking else "disabled"}}
    if thinking:
        body["reasoning_effort"] = "high"
    raw = json.dumps(body, ensure_ascii=False, sort_keys=True)
    open(p(".request.json"), "w").write(raw)
    started, history = time.time(), []
    for n in range(1, attempts + 1):
        t0 = time.time()
        try:
            status, text, res = _stream(url, key, body, idle)
        except Exception as e:
            status, text, res = 0, repr(e), None
        if status == 200 and not (res["content"] or "").strip():
            status, text = (-4 if res["finish"] == "length" else -2), "empty content, finish %s" % res["finish"]
        history.append({"attempt": n, "status": status, "seconds": round(time.time() - t0, 1),
                        "finish": res and res["finish"]})
        if status == 200:
            break
        if status in FINAL or n == attempts:
            open(p(".error.txt"), "w").write("status %s after %d attempts\n%s" % (status, n, text))
            open(p(".receipt.json"), "w").write(json.dumps({"provider": provider, "model": model, "tag": tag,
                "failed": True, "attempt_history": history, "thinking": thinking}, indent=1))
            return "failed"
        time.sleep(min(120, 10 * 2 ** n))
    open(p(".reasoning.txt"), "w").write(res["reasoning"])
    open(p(".response.txt"), "w").write(res["content"])
    last = res["last"] or {}
    open(p(".receipt.json"), "w").write(json.dumps({
        "provider": provider, "model": last.get("model", model), "tag": tag, "thinking": thinking,
        "response_id": last.get("id"), "finish_reason": res["finish"], "chunks": res["chunks"],
        "usage": last.get("usage"), "request_sha256": hashlib.sha256(raw.encode()).hexdigest(),
        "response_sha256": hashlib.sha256(res["content"].encode()).hexdigest(),
        "reasoning_chars": len(res["reasoning"]), "attempt_history": history,
        "total_seconds": round(time.time() - started, 1), "asked_at_unix": int(started)}, indent=1))
    return "ok"
