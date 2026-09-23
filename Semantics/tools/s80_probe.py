#!/usr/bin/env python3
"""s80_probe.py: before the counted run of round S80, one tiny call per provider per thinking setting in the exact
request shape of the reader calls (stream, stream_options include_usage, thinking enabled/disabled, reasoning_effort
when on at the shared s80_common.REASONING_EFFORT, temperature pinned, max_tokens at the top rung of the reader
ladder), and one marker-shaped call per marker provider (thinking on, max_tokens at the top rung of the marker
ladder, a JSON answer checked by parsing).
Prints status, finish reason, reasoning and content sizes, usage, bad chunks, and the model the provider names.
Exit status 1, and the line "STOP: ..." , if any call returns 400 (or any other non-200): the run does not start.

The prompts are tiny ("Say OK."); no document, method or key is sent. Nothing is written to the repository; with
--save DIR the printed lines are also written there. Keys come from the environment only.
"""
import json, os, sys, time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import s80_common as C
from s80_call import build_body, stream, PROVIDERS


def one(provider, thinking, max_tokens, system, user, want_json=False):
    body = build_body(provider, system, user, thinking, max_tokens)
    t0 = time.time()
    try:
        status, text, res = stream(provider, body, idle=120, deadline=300)
    except Exception as e:
        status, text, res = 0, repr(e), None
    row = {"provider": provider, "shape": "marker" if want_json else "reader",
           "thinking": thinking, "max_tokens": max_tokens, "temperature": body["temperature"],
           "reasoning_effort": body.get("reasoning_effort"), "status": status,
           "seconds": round(time.time() - t0, 1)}
    if status != 200:
        row["error"] = text[:600]
        return row
    last = res["last"] or {}
    row.update(finish=res["finish"], model=last.get("model"), content=res["content"][:80],
               reasoning_chars=len(res["reasoning"]), chunks=res["chunks"], bad_chunks=res["bad_chunks"],
               saw_done=res["saw_done"], usage=res["usage"])
    if want_json:
        try:
            json.loads(C.strip_fences(res["content"]))
            row["json_parses"] = True
        except Exception:
            row["json_parses"] = False
    return row


def main(a):
    rows, out = [], []

    def show(r):
        rows.append(r)
        line = json.dumps(r, ensure_ascii=False)
        out.append(line)
        print(line, flush=True)
    for p in C.MODELS:
        for th in (True, False):
            show(one(p, th, C.READER_LADDER[-1], "You are reviewing a document.", "Say OK."))
    for p in C.API_MARKERS:
        show(one(p, True, C.MARKER_LADDER[-1], None,
                 'Answer with a single JSON object and nothing else, in this form: {"ok": true}', True))
    bad = [r for r in rows if r["status"] != 200]
    warn = [r for r in rows if r["status"] == 200 and (r.get("finish") != "stop" or (not r["thinking"] and
            r.get("reasoning_chars")) or r.get("usage") is None or r.get("json_parses") is False)]
    for r in warn:
        msg = "WARN: %s %s thinking=%s: finish %s, reasoning chars %s, usage %s%s" % (
            r["provider"], r["shape"], r["thinking"], r.get("finish"), r.get("reasoning_chars"),
            "present" if r.get("usage") else "MISSING", ", JSON does not parse" if r.get("json_parses") is False else "")
        out.append(msg)
        print(msg)
    if bad:
        msg = "STOP: %d probe calls did not return 200: %s" % (len(bad), [(r["provider"], r["shape"], r["thinking"],
                                                                          r["status"]) for r in bad])
    else:
        msg = "PROBE OK: every provider accepted the exact request shape at both thinking settings"
    out.append(msg)
    print(msg)
    if "--save" in a:
        d = a[a.index("--save") + 1]
        C.write(os.path.join(d, "s80_probe_%d.txt" % int(time.time())), "\n".join(out) + "\n")
    raise SystemExit(1 if bad else 0)


if __name__ == "__main__":
    main(sys.argv[1:])
