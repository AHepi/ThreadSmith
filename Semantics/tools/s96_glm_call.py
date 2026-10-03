#!/usr/bin/env python3
"""s96_glm_call.py: one streamed call to GLM 5.3 (Z.ai), with a receipt, for the S96 pilot of a third outside reader
(26 September 2026). Standalone: it changes nothing in the shared tools and imports from s80_common only the pieces
that have no side effect on import (the sentinel test, the provider slot lock, the tag lock, the pinned temperature,
hashing and the log line). The shared caller s80_call.py is not imported; its acceptance rule is restated here
word for word (accept_reader below).

The call: the brief, whole, as the single user message, no system text; model glm-5.3; thinking enabled (GLM 5.3 cannot
switch it off); reasoning_effort "high" by default (Z.ai's model page gives GLM 5.3 only low, high and max, "any other
input will result in an error"; tested 26 September 2026 on the endpoint below, a made-up value is refused with code
1210, "reasoning_effort must be one of: none, minimal, low, medium, high, xhigh, max", and "medium" is taken, but
whether GLM 5.3 acts on "medium" or maps it to another level is not known, so this tool offers only the documented
three); max_tokens 65,536 by default (the API's range is 1 to 131,072); temperature s80_common.TEMPERATURE (0.7, as
every Atria and Mimo call); streamed, with usage asked for.
Endpoint: the GLM Coding Plan's OpenAI-compatible URL (below). The key the owner sent is a Coding Plan key: on the
general URL, https://api.z.ai/api/paas/v4/chat/completions, it is refused with HTTP 429, code 1113, "Insufficient
balance or no resource package". Z.ai's usage policy for the Coding Plan says it "may only be used within officially
supported tools and products".
The key is read from the environment variable GLM_API_KEY only, sent only in the Authorization header, and never
written, printed or logged.

Files, in --out, all under --tag, none ever overwritten (the call refuses to start if any file of the tag exists, and
every file is written whole to a temporary name and then linked into place, which fails if the name is taken):
  <tag>.request.json    the request body as sent (identical on every attempt; no key), written before the first attempt
  <tag>.aN.truncated.txt / <tag>.aN.reasoning.txt   an attempt that came back but was not accepted
  on acceptance: <tag>.reasoning.txt, then <tag>.receipt.json, then <tag>.response.txt last (so a response file on
  disk always has its receipt);
  on failure: <tag>.error.txt, then <tag>.receipt.json with "accepted": false.
Acceptance (s80_call.accept_reader): finish "stop" and END OF REPORT on the last non-blank line.
Retries: up to --attempts (6). Connection failures, timeouts, a stream cut before its finish, a finish of
"network_error", an error sent inside the stream, HTTP 429 and 5xx -> the same request again after a back-off of
min(120, 10 * 2**n) seconds. HTTP 429 with Z.ai code 1113 (no balance) or 1309 (package expired), and any other
4xx (400, 401, 403, 404, 413, 422 ...), are final. An answer that comes back and is not accepted (length, sensitive, no sentinel) is
sent again at the same max_tokens, at most --max-rejects (3) such answers in all, as in the S96 job list.
Lesson S12: with --rule, nothing is sent unless that file is tracked by git and unchanged from HEAD; with --brief-md5,
nothing is sent unless the brief has that md5. Every attempt holds one of the "glm" provider slots
(s80_common.provider_slot). Progress goes to stdout as counts and times only, never reply text.
"""
import argparse, datetime, json, os, subprocess, sys, time

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import requests  # noqa: E402
import s80_common as C  # noqa: E402

URL = "https://api.z.ai/api/coding/paas/v4/chat/completions"   # GLM Coding Plan
MODEL = "glm-5.3"
KEYNAME = "GLM_API_KEY"
EFFORT_LEVELS = ("low", "high", "max")      # GLM 5.3's documented values (docs.z.ai, thinking guide)
API_MAX_TOKENS = 131072                     # the API's range for max_tokens is 1 to 131,072
FINAL_429_CODES = {"1113", "1309"}          # no balance; package expired
PROGRESS_EVERY = 300                        # seconds between progress lines while a stream runs


def now():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def accept_reader(res):
    """s80_call.accept_reader, restated: finish "stop" and the sentinel on the last non-blank line."""
    if res["finish"] != "stop":
        return False, "finish %s" % res["finish"]
    if not C.report_complete(res["content"]):
        return False, "finish stop but the last line does not carry %s" % C.SENTINEL
    return True, ""


def write_new(path, text):
    """Write `text` whole to `path`, which must not exist: temporary file, fsync, then a hard link (which fails if
    the name is taken), so an existing file is never overwritten."""
    tmp = "%s.tmp.%d" % (path, os.getpid())
    with open(tmp, "x", encoding="utf-8") as f:
        f.write(text)
        f.flush()
        os.fsync(f.fileno())
    try:
        os.link(tmp, path)
    finally:
        os.unlink(tmp)


def build_body(user, effort, max_tokens):
    return {"model": MODEL, "messages": [{"role": "user", "content": user}], "max_tokens": max_tokens,
            "stream": True, "stream_options": {"include_usage": True}, "temperature": C.TEMPERATURE,
            "thinking": {"type": "enabled"}, "reasoning_effort": effort}


def business_code(text):
    try:
        err = json.loads(text).get("error") or {}
        return str(err.get("code", "")) or None
    except Exception:
        return None


def stream(url, body, key, idle, deadline, label):
    """One attempt. Returns (status, error_text, result); result holds whatever arrived, also when the stream is cut
    (then result["cut"] names the exception class)."""
    t0 = time.time()
    res = dict(content="", reasoning="", finish=None, last=None, model=None, id=None, chunks=0, bad_chunks=0,
               usage=None, saw_done=False, stream_error=None, cut=None, cut_detail=None)
    content, reasoning = [], []
    try:
        with requests.post(url, json=body, stream=True, timeout=(30, idle),
                           headers={"Authorization": "Bearer " + key, "Accept": "text/event-stream"}) as r:
            if r.status_code != 200:
                return r.status_code, r.text[:4000], None
            C.log("%s: HTTP 200, streaming" % label)
            r.encoding = "utf-8"
            next_note = t0 + PROGRESS_EVERY
            for line in r.iter_lines(decode_unicode=True):
                if time.time() - t0 > deadline:
                    raise TimeoutError("stream passed its deadline of %s s" % deadline)
                if time.time() > next_note:
                    C.log("%s: still streaming, %d s, reasoning %d chars, answer %d chars"
                          % (label, time.time() - t0, sum(map(len, reasoning)), sum(map(len, content))))
                    next_note += PROGRESS_EVERY
                if not line or not line.startswith("data:"):
                    continue
                data = line[5:].strip()
                if data == "[DONE]":
                    res["saw_done"] = True
                    break
                try:
                    d = json.loads(data)
                except Exception:
                    res["bad_chunks"] += 1
                    continue
                res["chunks"] += 1
                res["last"] = d
                if d.get("error"):
                    res["stream_error"] = json.dumps(d["error"], ensure_ascii=False)[:2000]
                res["model"] = d.get("model") or res["model"]
                res["id"] = d.get("id") or res["id"]
                if d.get("usage"):
                    res["usage"] = d["usage"]
                for ch in d.get("choices") or []:
                    delta = ch.get("delta") or {}
                    content.append(delta.get("content") or "")
                    reasoning.append(delta.get("reasoning_content") or "")
                    if ch.get("finish_reason"):
                        res["finish"] = ch["finish_reason"]
    except Exception as e:   # connection failures, timeouts, cut streams, the deadline
        res["cut"], res["cut_detail"] = type(e).__name__, repr(e)[:1000]
    res["content"], res["reasoning"] = "".join(content), "".join(reasoning)
    if res["cut"] and res["chunks"] == 0 and not res["content"] and not res["reasoning"]:
        return 0, res["cut_detail"], res
    return 200, "", res


def classify(status, text, res):
    """(error class or None, final?) for one attempt that was not accepted."""
    if status == 0:
        cut = (res or {}).get("cut") or ""
        return ("timeout" if "Timeout" in cut else "connection"), False
    if status == 429:
        code = business_code(text)
        return "http_429" + ("_code_%s" % code if code else ""), code in FINAL_429_CODES
    if status >= 500:
        return "http_%d" % status, False
    if status != 200:   # any other 4xx is final
        return "http_%d" % status, True
    if res["cut"]:
        return ("timeout" if "Timeout" in res["cut"] else "cut_stream"), False
    if res["stream_error"]:
        return "stream_error", False
    if res["finish"] is None:
        return "cut_stream", False
    if res["finish"] == "network_error":
        return "provider_network_error", False
    return "rejected_answer", False


def check_rule(rule):
    """Lesson S12: the reading rule must be tracked and unchanged from HEAD; returns (relative path, HEAD commit)."""
    rel = os.path.relpath(os.path.abspath(rule), C.REPO)
    git = ["git", "-C", C.REPO]
    if subprocess.run(git + ["ls-files", "--error-unmatch", "--", rel], capture_output=True).returncode != 0:
        raise SystemExit("the reading rule %s is not committed; nothing sent" % rel)
    if subprocess.run(git + ["diff", "--quiet", "HEAD", "--", rel], capture_output=True).returncode != 0:
        raise SystemExit("the reading rule %s differs from HEAD; nothing sent" % rel)
    head = subprocess.run(git + ["rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    return rel, head


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--brief", required=True, help="the file sent, whole, as the one user message")
    ap.add_argument("--tag", required=True)
    ap.add_argument("--out", required=True, help="the folder the files go to")
    ap.add_argument("--effort", default="high", choices=EFFORT_LEVELS)
    ap.add_argument("--max-tokens", type=int, default=65536)
    ap.add_argument("--attempts", type=int, default=6)
    ap.add_argument("--max-rejects", type=int, default=3)
    ap.add_argument("--idle", type=int, default=900, help="seconds of silence before an attempt is given up")
    ap.add_argument("--deadline", type=int, default=7200, help="seconds of wall clock per attempt")
    ap.add_argument("--url", default=URL)
    ap.add_argument("--rule", help="the note written before sending; must be committed and unchanged")
    ap.add_argument("--brief-md5", help="refuse unless the brief has this md5")
    a = ap.parse_args()

    if not 1 <= a.max_tokens <= API_MAX_TOKENS:
        raise SystemExit("max_tokens %d is outside the API's 1 to %d" % (a.max_tokens, API_MAX_TOKENS))
    if not os.environ.get(KEYNAME):
        raise SystemExit("%s is not set in the environment; nothing sent" % KEYNAME)
    brief_md5 = C.md5_file(a.brief)
    if a.brief_md5 and brief_md5 != a.brief_md5:
        raise SystemExit("the brief has md5 %s, expected %s; nothing sent" % (brief_md5, a.brief_md5))
    rule = check_rule(a.rule) if a.rule else None
    user = C.read(a.brief)
    os.makedirs(a.out, exist_ok=True)
    taken = sorted(n for n in os.listdir(a.out) if n.startswith(a.tag + "."))
    if taken:
        raise SystemExit("%d file(s) of tag %s already in %s; nothing sent, nothing overwritten"
                         % (len(taken), a.tag, a.out))

    with C.tag_lock(a.out, a.tag) as mine:
        if not mine:
            raise SystemExit("another sender holds %s in this folder now; nothing sent" % a.tag)
        return run(a, user, brief_md5, rule)


def run(a, user, brief_md5, rule):
    p = lambda ext: os.path.join(a.out, a.tag + ext)
    key = os.environ[KEYNAME]
    body = build_body(user, a.effort, a.max_tokens)
    raw = json.dumps(body, ensure_ascii=False, sort_keys=True)
    write_new(p(".request.json"), raw)
    started, started_utc = time.time(), now()
    C.log("start %s: %s, effort %s, max_tokens %d, brief md5 %s, %d words, %s"
          % (a.tag, MODEL, a.effort, a.max_tokens, brief_md5, C.words(user), a.url))
    history, rejects, res, why, status, text = [], 0, None, "", None, ""
    accepted = False
    for n in range(1, a.attempts + 1):
        label = "%s attempt %d" % (a.tag, n)
        t0, t0_utc, slot = time.time(), now(), {}
        with C.provider_slot("glm", label=a.tag) as slot:
            t1 = time.time()
            C.log("%s: sent" % label)
            status, text, res = stream(a.url, body, key, a.idle, a.deadline, label)
        h = {"attempt": n, "started_utc": t0_utc, "ended_utc": now(), "seconds": round(time.time() - t1, 1),
             "slot": slot.get("slot"), "slot_wait_seconds": slot.get("waited_seconds"), "status": status,
             "finish": res and res["finish"], "content_chars": res and len(res["content"]),
             "reasoning_chars": res and len(res["reasoning"]), "chunks": res and res["chunks"],
             "bad_chunks": res and res["bad_chunks"], "usage": res and res["usage"], "request_sha256": C.sha256(raw)}
        if status == 200 and not res["cut"] and not res["stream_error"] and res["finish"] not in (None, "network_error"):
            accepted, why = accept_reader(res)
        else:
            accepted, why = False, ""
        if accepted:
            h.update(accepted=True, error_class=None)
            history.append(h)
            C.log("%s: accepted (finish %s, %d s)" % (label, res["finish"], h["seconds"]))
            break
        cls, final = classify(status, text, res)
        h.update(accepted=False, error_class=cls)
        if cls == "rejected_answer":
            rejects += 1
            h["rejected_because"] = why
            write_new(p(".a%d.truncated.txt" % n), res["content"])
            if res["reasoning"]:
                write_new(p(".a%d.reasoning.txt" % n), res["reasoning"])
        else:
            h["error"] = (res and (res["cut_detail"] or res["stream_error"])) or text[:1000] or None
            if status == 200:
                why = cls
        history.append(h)
        C.log("%s: not accepted, %s%s (%s s)" % (label, cls, (": " + why) if why and why != cls else "",
                                                  h["seconds"]))
        if final or n == a.attempts or rejects >= a.max_rejects:
            break
        wait = min(120, 10 * 2 ** n)
        C.log("%s: next attempt in %d s" % (label, wait))
        time.sleep(wait)

    conn = sum(1 for h in history if h["error_class"] in ("connection", "timeout", "cut_stream",
                                                            "provider_network_error"))
    receipt = {
        "tool": "Semantics/tools/s96_glm_call.py", "provider": "glm (Z.ai)", "url": a.url, "model": MODEL,
        "model_returned": res and res["model"], "tag": a.tag, "accepted": accepted, "thinking": True,
        "reasoning_effort": a.effort, "temperature": C.TEMPERATURE, "top_p": "provider default (unset)",
        "max_tokens": a.max_tokens, "stream": True, "system": None,
        "brief": os.path.relpath(os.path.abspath(a.brief), C.REPO), "brief_md5": brief_md5,
        "user_sha256": C.sha256(user), "request_sha256": C.sha256(raw),
        "rule": rule and {"path": rule[0], "head_at_send": rule[1]},
        "response_id": res and res["id"], "finish_reason": res and res["finish"], "saw_done": res and res["saw_done"],
        "chunks": res and res["chunks"], "bad_chunks": res and res["bad_chunks"], "usage": res and res["usage"],
        "usage_missing": not (res and res["usage"]),
        "response_sha256": C.sha256(res["content"]) if res else None,
        "response_chars": len(res["content"]) if res else 0, "reasoning_chars": len(res["reasoning"]) if res else 0,
        "attempts": len(history), "connection_failures": conn, "rejected_answers": rejects,
        "attempt_history": history, "started_utc": started_utc, "ended_utc": now(),
        "total_seconds": round(time.time() - started, 1)}
    if accepted:
        write_new(p(".reasoning.txt"), res["reasoning"])
        write_new(p(".receipt.json"), json.dumps(receipt, indent=1, ensure_ascii=False))
        write_new(p(".response.txt"), res["content"])
        C.log("done: ok %s after %d attempt(s), %d connection failure(s), %s s"
              % (a.tag, len(history), conn, receipt["total_seconds"]))
        return 0
    write_new(p(".error.txt"), "status %s after %d attempts (%d came back but were not accepted; %d connection "
              "failures)\n%s\n%s" % (status, len(history), rejects, conn, why, text or (res and res["cut_detail"]) or ""))
    write_new(p(".receipt.json"), json.dumps(receipt, indent=1, ensure_ascii=False))
    C.log("done: failed %s after %d attempt(s), %d connection failure(s), %d rejected answer(s), %s s"
          % (a.tag, len(history), conn, rejects, receipt["total_seconds"]))
    return 1


if __name__ == "__main__":
    sys.exit(main())
