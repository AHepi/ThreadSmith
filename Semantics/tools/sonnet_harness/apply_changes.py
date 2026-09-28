#!/usr/bin/env python3
"""Apply a list of text changes to a text by program, and check each one byte for byte.

  python3 -B apply_changes.py --src TEXT --src-md5 MD5 --changes CHANGES.json --out NEW [--expect-md5 MD5]
         [--held ID ...] [--allow-new-in-sem]

The rules are those of round 2's two appliers ("apply text changes.py" and "apply text changes for the owner's
answers.py", results/S104 Round 2 - maths after the reading/), made general:
  - the source's md5 must be the one given, or nothing is written;
  - kinds allowed: delete, formal, pointer (decision S40); any other kind is refused;
  - each change's old span must occur exactly once in its line (overlapping occurrences counted), else refused;
  - a delete must have an empty new span;
  - two changes whose spans overlap on one line are both refused;
  - a change marked waiting (keys waiting, owner_question, held, blocked_by, hold) or named by --held is held;
  - every applied change is compared with its JSON entry byte for byte, and undoing the applied changes must give the
    source line back; the line count must not change;
  - the output is a NEW file: never over an existing file, never over the source (hcommon.guard_write).
Then the scans of text_scan.py (S95 residue, S96 physical words, headings/terms/tags kept, words outside formulas).
ok = the md5 is right, nothing refused, and, when --expect-md5 is given, the output's md5 equals it. The scans are
reported, not judged: a spec's checks say which of them must be zero.
"""
import argparse
import collections
import json
import os
import re
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hcommon as H  # noqa: E402
import text_scan  # noqa: E402

KINDS = {"delete", "formal", "pointer"}
HOLD_KEYS = ("waiting", "owner_question", "held", "blocked_by", "hold")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", required=True)
    ap.add_argument("--src-md5", required=True)
    ap.add_argument("--changes", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--expect-md5")
    ap.add_argument("--held", action="append", default=[])
    ap.add_argument("--allow-new-in-sem", action="store_true")
    a = ap.parse_args()

    raw = open(H.guard_read(a.src), "rb").read()
    got_md5 = H.md5_bytes(raw)
    if got_md5 != a.src_md5:
        H.refuse("source md5 is %s, not %s; nothing written" % (got_md5, a.src_md5))
    if H.real(a.out) == H.real(a.src):
        H.refuse("the output would be the source")
    H.guard_write(a.out, a.allow_new_in_sem)
    if os.path.exists(a.out):
        H.refuse("the output exists; the applier never writes over a file: %s" % a.out)
    old = raw.decode("utf-8").split("\n")
    ch = [dict(e) for e in H.load_json(a.changes)]
    ids = collections.Counter(e.get("id") for e in ch)
    if any(v > 1 for v in ids.values()):
        H.refuse("duplicate ids: %s" % [k for k, v in ids.items() if v > 1])

    refused, held, ok_list = [], [], []
    for e in ch:
        if any(e.get(k) for k in HOLD_KEYS) or e.get("id") in a.held:
            held.append(dict(id=e.get("id"), line=e.get("line"), why="marked waiting, or named by --held"))
            continue
        if e.get("kind") not in KINDS:
            refused.append(dict(id=e.get("id"), line=e.get("line"), why="kind %r not delete/formal/pointer" % e.get("kind")))
            continue
        if not isinstance(e.get("line"), int) or not (1 <= e["line"] <= len(old)):
            refused.append(dict(id=e.get("id"), line=e.get("line"), why="no such line"))
            continue
        k = len(re.findall("(?=%s)" % re.escape(e["old"]), old[e["line"] - 1])) if e.get("old") else 0
        if k != 1:
            refused.append(dict(id=e["id"], line=e["line"], why="old span occurs %d times in the line" % k))
            continue
        if e["kind"] == "delete" and e.get("new", "") != "":
            refused.append(dict(id=e["id"], line=e["line"], why="delete with a nonempty new span"))
            continue
        s = old[e["line"] - 1].index(e["old"])
        e["span"] = (s, s + len(e["old"]))
        ok_list.append(e)

    byline = collections.defaultdict(list)
    for e in ok_list:
        byline[e["line"]].append(e)
    applied = []
    for ln, es in byline.items():
        bad = set()
        for i in range(len(es)):
            for j in range(i + 1, len(es)):
                x, y = es[i]["span"], es[j]["span"]
                if x[0] < y[1] and y[0] < x[1]:
                    bad |= {i, j}
        for i in sorted(bad):
            refused.append(dict(id=es[i]["id"], line=ln, why="overlaps another change on the line; neither applied"))
        applied += [e for i, e in enumerate(es) if i not in bad]

    new = list(old)
    for ln in sorted({e["line"] for e in applied}):
        es = sorted((e for e in applied if e["line"] == ln), key=lambda e: e["span"][0])
        line, out, pos = old[ln - 1], [], 0
        for e in es:
            out.append(line[pos:e["span"][0]])
            e["out_at"] = sum(len(x) for x in out)
            out.append(e["new"])
            pos = e["span"][1]
        out.append(line[pos:])
        new[ln - 1] = "".join(out)
    byte_checks = []
    for ln in sorted({e["line"] for e in applied}):
        es = sorted((e for e in applied if e["line"] == ln), key=lambda e: e["span"][0])
        got, back, pos = new[ln - 1], [], 0
        for e in es:
            seg = got[e["out_at"]:e["out_at"] + len(e["new"])]
            byte_checks.append(dict(id=e["id"], line=ln, written_equals_entry=seg.encode("utf-8") == e["new"].encode("utf-8")))
            back.append(got[pos:e["out_at"]])
            back.append(e["old"])
            pos = e["out_at"] + len(e["new"])
        back.append(got[pos:])
        byte_checks.append(dict(id="undo L%d" % ln, line=ln, written_equals_entry="".join(back).encode("utf-8") == old[ln - 1].encode("utf-8")))
    if not all(b["written_equals_entry"] for b in byte_checks):
        H.refuse("a written span differs from its entry, or undoing does not give the line back; nothing written",
                 byte_checks=[b for b in byte_checks if not b["written_equals_entry"]])
    if len(new) != len(old):
        H.refuse("line count changed; nothing written")
    text = "\n".join(new)
    H.write_text(a.out, text, a.allow_new_in_sem)
    out_md5 = H.md5_bytes(text.encode("utf-8"))

    deleted = {(e["line"], m.group(1)) for e in applied if e["kind"] == "delete" for m in H.BOLD.finditer(e["old"])}
    scans = text_scan.compare(old, new, deleted)
    res = dict(job="apply_text_changes", src=H.rel(a.src), src_md5=got_md5, changes=H.rel(a.changes),
               changes_md5=H.md5_file(a.changes), out=H.rel(a.out), out_md5=out_md5,
               changes_read=len(ch), applied_count=len(applied), applied_lines=len({e["line"] for e in applied}),
               refused_count=len(refused), held_count=len(held),
               applied=[dict(id=e["id"], line=e["line"], kind=e["kind"],
                             prose_words_delta=len(H.prose(e["new"])) - len(H.prose(e["old"])))
                        for e in sorted(applied, key=lambda e: (e["line"], e["span"][0]))],
               refused=refused, held=held, byte_checks_passed=len(byte_checks), **scans)
    ok = not refused
    if a.expect_md5:
        res["expect_md5"] = a.expect_md5
        res["md5_match"] = out_md5 == a.expect_md5
        ok = ok and res["md5_match"]
    res["ok"] = ok
    H.emit(res)


if __name__ == "__main__":
    main()
