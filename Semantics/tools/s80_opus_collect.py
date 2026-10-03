#!/usr/bin/env python3
"""s80_opus_collect.py: bring the Opus 5.5 reader reports of round S80 into the results, with the frozen contamination
rule of plan S80, second version.

  python Semantics/tools/s80_opus_collect.py --transcripts DIR     # DIR/<tag>.a<k>.txt: each agent's transcript
  python Semantics/tools/s80_opus_collect.py --no-transcripts      # records that no transcript was checked

For each Opus tag, the latest prepared attempt (s80_opus_prep.py) is read from its folder:
- report.md missing: nothing is done (not yet run).
- Contamination (any hit voids the repetition; it is rerun once, with s80_opus_prep.py --attempt 2 TAG):
  the report contains one of: S80, S70, S75 (as written), or seeded, planted, "Derivation 3 was", "file 10" (in any
  case);
  the transcript shows any tool call touching /home/user/ThreadSmith, the answer key, the keys, another agent's
  folder, or any path outside the agent's own folder (every absolute path in the transcript is checked).
- The report's last non-blank line must carry END OF REPORT; otherwise it is kept as <tag>.pass<k>.truncated.txt and
  the repetition counts as failed on that attempt.
- A clean, complete report is copied to results/.../readers/<tag>.response.txt, the prompt to <tag>.request.md, and a
  receipt to <tag>.receipt.json. A void or incomplete attempt leaves <tag>.pass<k>.receipt.json with "failed": true.
Refuses to run once anything exists in marks/.
"""
import json, os, re, shutil, sys, time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import s80_common as C
from s80_opus_prep import ADMIN, WORK

READERS_DIR = os.path.join(C.OUT, "readers")
REPORT_WORDS = ["S80", "seeded", "planted", "Derivation 3 was", "S70", "S75", "file 10"]
TRANSCRIPT_WORDS = ["/home/user/ThreadSmith", "sealed list", "Seeded errors", "plant.py", "api.env", "opus_admin",
                    "scratchpad/keys", "/pilot/"]
PATH_RE = re.compile(r"(/(?:tmp|home|root|etc|usr|var|opt|proc|mnt|srv)(?:/[^\s\"'`<>|;,)\]}]*)?)")


CASE_SENSITIVE = {"S80", "S70", "S75"}   # record ids; the default folder path holds a lowercase "s80"


def report_hits(text):
    low = text.lower()
    return [w for w in REPORT_WORDS if (w in text if w in CASE_SENSITIVE else w.lower() in low)]


def transcript_hits(text, folder):
    hits = [w for w in TRANSCRIPT_WORDS if w in text]
    own = os.path.abspath(folder)
    for m in PATH_RE.finditer(text):
        p = m.group(1).rstrip(".:")
        if p == own or p.startswith(own + "/"):
            continue
        hits.append("path outside the folder: " + p[:200])
    return sorted(set(hits))


def main(a):
    if "--transcripts" not in a and "--no-transcripts" not in a:
        raise SystemExit(__doc__)
    tdir = a[a.index("--transcripts") + 1] if "--transcripts" in a else None
    marks = os.path.join(C.OUT, "marks")
    if os.path.isdir(marks) and any(os.scandir(marks)):
        raise SystemExit("marks/ is not empty; the Opus arm is closed")
    mp = json.loads(C.read(os.path.join(ADMIN, "MAP.json")))
    os.makedirs(READERS_DIR, exist_ok=True)
    summary = {}
    for tag in C.opus_tags():
        p = lambda ext: os.path.join(READERS_DIR, tag + ext)
        if os.path.exists(p(".response.txt")):
            summary[tag] = "already collected"
            continue
        attempts = mp.get(tag, {})
        if not attempts:
            summary[tag] = "not prepared"
            continue
        k = max(int(x) for x in attempts)
        at = attempts[str(k)]
        rpath = os.path.join(at["folder"], "report.md")
        if not os.path.exists(rpath):
            summary[tag] = "attempt %d not yet run" % k
            continue
        if os.path.exists(p(".pass%d.receipt.json" % k)):
            summary[tag] = "attempt %d already judged failed" % k
            continue
        report = C.read(rpath)
        prompt = C.read(at["prompt"])
        rh = report_hits(report)
        th, tchecked = [], False
        if tdir:
            tp = os.path.join(tdir, "%s.a%d.txt" % (tag, k))
            if not os.path.exists(tp):
                summary[tag] = "attempt %d: transcript %s missing; not collected" % (k, tp)
                continue
            th, tchecked = transcript_hits(C.read(tp), at["folder"]), True
        complete = C.report_complete(report)
        receipt = {"reader": "opus 5.5 subagent", "tag": tag, "attempt": k, "folder": at["folder"],
                   "prompt_sha256": C.sha256(prompt), "document_md5": at["document_md5"],
                   "method_text_sha256": at["method_text_sha256"], "response_sha256": C.sha256(report),
                   "response_chars": len(report), "sentinel_present": complete,
                   "contamination": {"report_hits": rh, "transcript_checked": tchecked, "transcript_hits": th},
                   "thinking": "as the agent runs (not switchable)", "temperature": "not settable",
                   "collected_at_unix": int(time.time())}
        if rh or th or not complete:
            receipt["failed"] = True
            receipt["void"] = bool(rh or th)
            C.write(p(".pass%d.truncated.txt" % k) if not (rh or th) else p(".pass%d.void.txt" % k), report)
            C.write(p(".pass%d.receipt.json" % k), json.dumps(receipt, indent=1))
            why = "void (contamination: %s)" % (rh + th) if (rh or th) else "incomplete (no END OF REPORT)"
            summary[tag] = "attempt %d %s%s" % (k, why, "; rerun once with --attempt 2" if k == 1 else "; failed twice")
            continue
        receipt["failed"] = False
        C.write(p(".request.md"), prompt)
        shutil.copyfile(rpath, p(".response.txt"))
        C.write(p(".receipt.json"), json.dumps(receipt, indent=1))
        summary[tag] = "collected (attempt %d)%s" % (k, "" if tchecked else ", transcript NOT checked")
    for t, s in summary.items():
        print(t, s)


if __name__ == "__main__":
    main(sys.argv[1:])
