#!/usr/bin/env python3
"""s80_call.py: one streamed call to an outside model, with a receipt. Written for round S80 (does the hard-to-vary
skill add anything), 23 September 2026, from the pattern of Language/tools/ask_model_2.py (read, not copied across
projects' records: this file is the Semantics project's own). Second version, after the cross-examination by Atria and
Mimo (plan S80, second version): acceptance test, max_tokens ladder, pinned temperature, text hashes, bad-chunk count,
UTF-8 everywhere, earlier receipts kept.

Providers (keys from the environment only, never from a file in the repository):
  atria     https://api.atria-asi.ai/v1/chat/completions             Atria-Dawn-Preview  ATRIA_API_KEY
  mimo      https://token-plan-sgp.xiaomimimo.com/v1/chat/completions mimo-v2.6-pro       MIMO_API_KEY
  deepseek  https://api.deepseek.com/chat/completions                 deepseek-v4-pro     DEEPSEEK_API_KEY
Thinking is switched with `thinking: {"type": "enabled"|"disabled"}`; with it on, `reasoning_effort` is
s80_common.REASONING_EFFORT (the one shared setting: "medium" from 23 September 2026, decision S17; "high" before), or
an explicit `effort` argument; the effort sent is recorded in the request and the receipt.
Temperature is pinned (s80_common.TEMPERATURE) and recorded; top_p is left to the provider and recorded as unset.

call(provider, system, user, out_dir, tag, thinking, ladder, accept, ...) writes, in out_dir:
  <tag>.response.txt, <tag>.reasoning.txt, <tag>.request.json, <tag>.receipt.json   only when `accept` passes;
  <tag>.pass<k>.a<n>.truncated.txt (+ .reasoning.txt) for every attempt that came back but failed `accept`;
  <tag>.error.txt and a receipt with "failed": true when every attempt is spent.
An earlier pass's receipt, error and request for the same tag are renamed <tag>.pass<k>.receipt.json / .error.txt /
.request.json, never overwritten, and a new pass is numbered above every earlier pass that left any file (a pass cut
off before its receipt included), so no earlier attempt file is overwritten. A tag whose .response.txt exists is
skipped.
Retries: 429, 5xx, disconnects, silence -> same max_tokens, back-off. finish "length" -> next rung of the ladder.
Any other failed acceptance (finish "stop" without the sentinel, no finish, invalid marker JSON) -> same max_tokens,
at most `max_rejects` such answers. 400/401/403/404/413/422 are final and not retried.
"""
import hashlib, json, os, re, time
import requests

import s80_common as C

PROVIDERS = {
    "atria": ("https://api.atria-asi.ai/v1/chat/completions", "Atria-Dawn-Preview", "ATRIA_API_KEY"),
    "mimo": ("https://token-plan-sgp.xiaomimimo.com/v1/chat/completions", "mimo-v2.6-pro", "MIMO_API_KEY"),
    "deepseek": ("https://api.deepseek.com/chat/completions", "deepseek-v4-pro", "DEEPSEEK_API_KEY"),
}
FINAL = {400, 401, 403, 404, 413, 422}


def build_body(provider, system, user, thinking, max_tokens, temperature=C.TEMPERATURE, effort=None):
    """The exact request shape of every S80 call (the probe uses this too). effort: None reads the shared setting,
    s80_common.REASONING_EFFORT, at call time; a value given here overrides it for this call."""
    model = PROVIDERS[provider][1]
    messages = ([{"role": "system", "content": system}] if system else []) + [{"role": "user", "content": user}]
    body = {"model": model, "messages": messages, "max_tokens": max_tokens, "stream": True,
            "stream_options": {"include_usage": True}, "temperature": temperature,
            "thinking": {"type": "enabled" if thinking else "disabled"}}
    if thinking:
        body["reasoning_effort"] = effort or C.REASONING_EFFORT
    return body


def stream(provider, body, idle=900, deadline=None):
    """deadline: seconds of wall clock for the whole stream; past it the call raises (and is retried as a disconnect)."""
    url, _, keyname = PROVIDERS[provider]
    t_end = time.time() + deadline if deadline else None
    key = os.environ[keyname]
    content, reasoning, finish, last, chunks, bad, usage = [], [], None, None, 0, 0, None
    with requests.post(url, json=body, stream=True, timeout=(30, idle),
                       headers={"Authorization": "Bearer " + key, "Accept": "text/event-stream"}) as r:
        if r.status_code != 200:
            return r.status_code, r.text[:4000], None
        r.encoding = "utf-8"
        done = False
        for line in r.iter_lines(decode_unicode=True):
            if t_end and time.time() > t_end:
                raise TimeoutError("stream passed its deadline of %s s" % deadline)
            if not line or not line.startswith("data:"):
                continue
            data = line[5:].strip()
            if data == "[DONE]":
                done = True
                break
            try:
                d = json.loads(data)
            except Exception:
                bad += 1
                continue
            chunks += 1
            last = d
            if d.get("usage"):
                usage = d["usage"]
            for ch in d.get("choices") or []:
                delta = ch.get("delta") or {}
                content.append(delta.get("content") or "")
                reasoning.append(delta.get("reasoning_content") or "")
                if ch.get("finish_reason"):
                    finish = ch["finish_reason"]
    return 200, "", dict(content="".join(content), reasoning="".join(reasoning), finish=finish, last=last,
                         chunks=chunks, bad_chunks=bad, usage=usage, saw_done=done)


KEPT = (".receipt.json", ".error.txt", ".request.json")   # an earlier pass's own files, renamed .pass<k><ext>


def pass_plan(out_dir, tag):
    """([(old name, new name)], this pass's number), touching nothing. An earlier pass's loose receipt, error and
    request belong to the highest pass that left a <tag>.pass<k>.* file, or to the one after it when that pass's own
    receipt, error or request is already kept under its number. This pass is numbered one above every earlier pass,
    so no file of an earlier pass is overwritten, the attempt files of a pass cut off before its receipt included
    (the earlier rule counted only kept receipts and errors, and would have reused such a pass's number)."""
    names = set(os.listdir(out_dir)) if os.path.isdir(out_dir) else set()
    pat = re.compile(re.escape(tag) + r"\.pass(\d+)\.")
    hi = max([int(m.group(1)) for m in map(pat.match, names) if m] or [0])
    loose = [e for e in KEPT if tag + e in names]
    if not loose:
        return [], hi + 1
    k = hi if hi and not any("%s.pass%d%s" % (tag, hi, e) in names for e in KEPT) else hi + 1
    return [(tag + e, "%s.pass%d%s" % (tag, k, e)) for e in loose], k + 1


def _keep_earlier(out_dir, tag):
    """Rename an earlier pass's receipt, error and request so a rerun never overwrites them; return this pass's
    number, or None (and rename nothing) if a new name is already taken, which pass_plan's numbering rules out."""
    renames, k = pass_plan(out_dir, tag)
    if any(os.path.exists(os.path.join(out_dir, new)) for _, new in renames):
        return None
    for old, new in renames:
        os.replace(os.path.join(out_dir, old), os.path.join(out_dir, new))
    return k


def accept_reader(res):
    if res["finish"] != "stop":
        return False, "finish %s" % res["finish"]
    if not C.report_complete(res["content"]):
        return False, "finish stop but the last line does not carry %s" % C.SENTINEL
    return True, ""


def call(provider, system, user, out_dir, tag, thinking, ladder, accept=accept_reader, extra=None,
         idle=900, attempts=6, max_rejects=3, deadline=7200, effort=None):
    _, model, _ = PROVIDERS[provider]
    os.makedirs(out_dir, exist_ok=True)
    p = lambda ext: os.path.join(out_dir, tag + ext)
    if os.path.exists(p(".response.txt")):
        return "skipped"
    pas = _keep_earlier(out_dir, tag)
    if pas is None:
        return "refused: an earlier pass's file would be renamed over another; nothing sent"
    effort = (effort or C.REASONING_EFFORT) if thinking else None   # read once: every attempt of a pass sends the same
    rung = 0
    started, history, rejects, res, why = time.time(), [], 0, None, ""
    for n in range(1, attempts + 1):
        max_tokens = ladder[min(rung, len(ladder) - 1)]
        body = build_body(provider, system, user, thinking, max_tokens, effort=effort)
        raw = json.dumps(body, ensure_ascii=False, sort_keys=True)
        C.write(p(".request.json"), raw)   # the last attempt's request; every attempt's hash is in the history
        t0 = time.time()
        try:
            status, text, res = stream(provider, body, idle, deadline)
        except Exception as e:
            status, text, res = 0, repr(e), None
        h = {"attempt": n, "status": status, "max_tokens": max_tokens, "seconds": round(time.time() - t0, 1),
             "finish": res and res["finish"], "bad_chunks": res and res["bad_chunks"],
             "content_chars": res and len(res["content"]), "request_sha256": C.sha256(raw)}
        ok = False
        if status == 200:
            ok, why = accept(res)
            h["accepted"] = ok
            if not ok:
                h["rejected_because"] = why
                rejects += 1
                C.write(p(".pass%d.a%d.truncated.txt" % (pas, n)), res["content"])
                if res["reasoning"]:
                    C.write(p(".pass%d.a%d.reasoning.txt" % (pas, n)), res["reasoning"])
                if res["finish"] == "length":
                    rung += 1
        history.append(h)
        if ok:
            break
        final = status in FINAL or n == attempts or rejects >= max_rejects
        if final:
            C.write(p(".error.txt"), "status %s after %d attempts (%d came back but were not accepted)\n%s\n%s"
                    % (status, n, rejects, why if status == 200 else "", text))
            C.write(p(".receipt.json"), json.dumps({
                "provider": provider, "model": model, "tag": tag, "failed": True, "pass": pas, "thinking": thinking,
                "reasoning_effort": effort, "temperature": C.TEMPERATURE, "top_p": "provider default (unset)",
                "system_sha256": C.sha256(system) if system else None, "user_sha256": C.sha256(user),
                "attempt_history": history, "extra": extra or {}, "asked_at_unix": int(started)}, indent=1))
            return "failed"
        if status != 200:
            time.sleep(min(120, 10 * 2 ** n))
    C.write(p(".reasoning.txt"), res["reasoning"])
    C.write(p(".response.txt"), res["content"])
    last = res["last"] or {}
    C.write(p(".receipt.json"), json.dumps({
        "provider": provider, "model": last.get("model", model), "tag": tag, "pass": pas, "thinking": thinking,
        "reasoning_effort": effort, "temperature": C.TEMPERATURE, "top_p": "provider default (unset)",
        "max_tokens_used": history[-1]["max_tokens"],
        "response_id": last.get("id"), "finish_reason": res["finish"], "saw_done": res["saw_done"],
        "chunks": res["chunks"], "bad_chunks": res["bad_chunks"],
        "usage": res["usage"], "usage_missing": res["usage"] is None,
        "system_sha256": C.sha256(system) if system else None, "user_sha256": C.sha256(user),
        "request_sha256": history[-1]["request_sha256"],
        "response_sha256": C.sha256(res["content"]), "response_chars": len(res["content"]),
        "reasoning_chars": len(res["reasoning"]), "attempt_history": history, "extra": extra or {},
        "total_seconds": round(time.time() - started, 1), "asked_at_unix": int(started)}, indent=1))
    return "ok"
