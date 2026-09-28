#!/usr/bin/env python3
"""Collect the results of the round-2 tests of the harness for one run label, as JSON and as table rows for the note.

  python3 -B report_tests.py --run <label> [--out report.json]

Reads only the folders under sonnet_harness_tests/<label>/ and, for the tabulation, the round 2 tabulation (the known
answer) through tabulation.py compare. For the sheets it also compares each agent's FIRST attempt (the .attempt1
copy), and the sheet as Opus's check would correct it (opus_check.json: each row_to_change applied to the marks).
"""
import argparse
import json
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hcommon as H  # noqa: E402
import tabulation as TB  # noqa: E402

RET = os.path.join(H.SEM, "results", "S104 Round 2 - returns")
TAB = os.path.join(H.SEM, "results", "S104 Round 2 - tabulation of the replies, before any ruling.md")
REPLIES = [os.path.join(RET, "s104_maths_mimo_12.response.txt") + ":M12:Mimo",
           os.path.join(RET, "s104_maths_glm_12.response.txt") + ":G12:GLM"]


def jload(p):
    try:
        return H.load_json(p)
    except SystemExit:
        return None


def latest(d, stem):
    for name in (stem + ".json",):
        p = os.path.join(d, name)
        if os.path.exists(p):
            return jload(p)
    return None


def summarize_compare(c):
    return dict(pairs=c["pairs"], opus_found=c["found"] + len(c["missed"]), found=c["found"], missed=len(c["missed"]),
                extra=len(c["extra"]), marks_equal=c["said_equal"], to_checker_equal="%d/%d" % (c["goes_to_checker_equal"], c["items"]),
                blocks_equal=c["blocks_equal"], lines_equal=c["lines_equal"], passages_covered=c["passages_covered"],
                wordings_exact="%s/%s" % (c["wordings_sheet_exact"], c["wordings_sheet_given"]),
                missed_rows=c["missed"], extra_rows=c["extra"], mark_diffs=c["said_diff"], block_diffs=c["blocks_diff"],
                line_diffs=c["lines_diff"], to_checker_diffs=c["goes_to_checker_diff"])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    ap.add_argument("--out")
    a = ap.parse_args()
    root = os.path.join(H.TEST_ROOT, a.run)
    if not os.path.isdir(root):
        H.refuse("no folder %s" % root)
    rep = dict(run=a.run, folder=root)
    replies = TB.parse_replies(REPLIES)

    d = os.path.join(root, "r2-claim-suite")
    w, v = latest(d, "result.all"), latest(d, "result.check.verifier")
    s = jload(os.path.join(d, "suite.json")) if os.path.exists(os.path.join(d, "suite.json")) else None
    rep["claims"] = dict(worker_ok=w and w.get("ok"), verifier_ok=v and v.get("ok"),
                         digests_equal=bool(w and v and w.get("digest") == v.get("digest")),
                         counts=s and s.get("counts"), differences=s and len(s.get("differences", [])),
                         seconds=s and s.get("seconds"), model_folder_changed=s and s.get("model_folder_changed"))

    d = os.path.join(root, "r2-text-changes")
    w, v = latest(d, "result.all"), latest(d, "result.check.verifier")
    s1, s2 = [jload(os.path.join(d, f)) if os.path.exists(os.path.join(d, f)) else None for f in ("step1.json", "step2.json")]
    rep["text"] = dict(worker_ok=w and w.get("ok"), verifier_ok=v and v.get("ok"),
                       digests_equal=bool(w and v and w.get("digest") == v.get("digest")),
                       md5_1=s1 and s1.get("out_md5"), md5_2=s2 and s2.get("out_md5"),
                       applied=[s1 and s1.get("applied_count"), s2 and s2.get("applied_count")],
                       words_outside_formulas=[s1 and s1["before"]["words_outside_formulas"], s1 and s1["after"]["words_outside_formulas"],
                                               s2 and s2["after"]["words_outside_formulas"]] if s1 and s2 else None)

    for var in ("harnessed", "bare"):
        d = os.path.join(root, "r2-tabulation-part12-%s" % var)
        ext = os.path.join(d, "extraction.json")
        row = dict(present=os.path.exists(ext))
        if row["present"]:
            w, v = latest(d, "result.check"), latest(d, "result.check.verifier")
            row.update(worker_ok=w and w.get("ok"), verifier_ok=v and v.get("ok"), attempts=(w or {}).get("agent_attempt"))
            tries = [("final", ext)]
            if os.path.exists(ext + ".attempt1"):
                tries.insert(0, ("first attempt", ext + ".attempt1"))
            for label, path in tries:
                e = jload(path)
                if var == "harnessed":
                    e = TB.fill(e, replies, None)
                row[label] = summarize_compare(TB.compare(e, TAB, 12, replies))
            oc = os.path.join(d, "opus_check.json")
            if os.path.exists(oc):
                o = jload(oc)
                e = jload(ext)
                if var == "harnessed":
                    e = TB.fill(e, replies, None)
                fix = {(r["item"], r["reader"]): r["said_should_be"] for r in o.get("rows_to_change", [])}
                for r in e.get("rows", []):
                    if (r.get("item"), r.get("reader")) in fix:
                        r["said"] = fix[(r["item"], r["reader"])]
                row["after the Opus check"] = summarize_compare(TB.compare(e, TAB, 12, replies))
                row["opus_check"] = dict(rows_checked=o.get("rows_checked"), rows_to_change=len(o.get("rows_to_change", [])),
                                         passages_missing=len(o.get("passages_missing", [])))
        rep["tabulation_" + var] = row

    d = os.path.join(root, "r2-merge-area-models")
    m = jload(os.path.join(d, "merge.json")) if os.path.exists(os.path.join(d, "merge.json")) else None
    w, v = latest(d, "result.all"), latest(d, "result.check.verifier")
    rep["merge"] = dict(worker_ok=w and w.get("ok"), verifier_ok=v and v.get("ok"),
                        conflicts=m and [(c["file"], c["conflicts"]) for c in m["conflicts"]])

    d = os.path.join(root, "r2-log-entry-draft")
    c = jload(os.path.join(d, "check.json")) if os.path.exists(os.path.join(d, "check.json")) else None
    w = latest(d, "result.check")
    rep["records"] = dict(worker_ok=w and w.get("ok"), words=c and c.get("words"), unsupported=c and c.get("unsupported"),
                          s23_hits=c and len(c.get("s23_list_hits", [])))
    if a.out:
        H.write_json(a.out, rep)
    H.emit(dict(ok=True, **rep))


if __name__ == "__main__":
    main()
