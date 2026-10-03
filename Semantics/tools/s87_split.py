#!/usr/bin/env python3
"""s87_split.py: the supplementary split of one S81 2b audit (log S87). The plan's s81_2b_mimo_A (Mimo auditing tester
A's 1C return, all 52 rows in Part 1) failed on both allowed passes: every attempt that ran to its end reached the
131,072-token ceiling with no answer written. As supplementary evidence outside the plan's table, the same text is sent
in four calls, one per quarter of the rows.

  python Semantics/tools/s87_split.py           build the four briefs and the job list for tools/s87_run.py
  python Semantics/tools/s87_split.py --check   rebuild in memory and compare with the files; writes nothing

Source: briefs/s81_2b_mimo_A.txt, byte for byte the text sent (its SHA-256 must equal the user_sha256 of both of the
plan's failed receipts). Each part differs from it in two places, and only there:
  - Part 1's rows line names the quarter (O1-O13, O14-O26, O27-O39, O40-O52) in place of all 52 rows;
  - one sentence, NOTE below, closes the Part 2 section (after its one-line form, before the Part 3 heading), so that
    Part 2 stays empty as it was in the plan's call (where every row was in Part 1) and the part is asked for no
    one-line comparisons the plan's call never asked for. It comes last in the section so that it reads as the
    exception to the form just above it.
Everything else (the instruction, the theory, the cases, tester A's reading, Mimo's blind readings) is unchanged. The
program checks this line by line, runs s81_build's forbidden-string checks on each part, and prints no part of the
embedded returns. It refuses to overwrite a file whose content differs.
"""
import difflib, hashlib, json, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import s81_build as B

SOURCE_TAG = "s81_2b_mimo_A"
SRC = os.path.join(B.BRIEFS, SOURCE_TAG + ".txt")
RECEIPTS = [os.path.join(B.RET, SOURCE_TAG + ".pass1.receipt.json"), os.path.join(B.RET, SOURCE_TAG + ".receipt.json")]
SUP = os.path.join(B.OUT, "supplementary - Mimo on tester A in four parts")
JOBS = os.path.join(SUP, "jobs for s87_run.json")
QUARTERS = [B.CASES[i:i + 13] for i in range(0, 52, 13)]
ROWS_ALL = "These rows: " + ", ".join(B.CASES) + "."
PART2_HEAD = "## Part 2 - Every other row, in one line each\n\n"
PART3_HEAD = "## Part 3 - What the reading under audit has left unmarked\n"
NOTE = "In this call the rows outside the Part 1 list are audited in companion calls, so leave Part 2 empty."
FIRST_SECTION = "%s THE THEORY %s" % (B.BAR, B.BAR)


def sha(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def tag(q):
    return "%s_part%d" % (SOURCE_TAG, q)


def parts():
    src = B.read(SRC)
    for p in RECEIPTS:
        rec = json.loads(B.read(p))
        B.need(rec.get("failed") and rec.get("user_sha256") == sha(src),
               "%s: not a failed receipt of this exact text; nothing built" % os.path.basename(p))
    cut = src.index(FIRST_SECTION)
    for s in (ROWS_ALL, PART2_HEAD, PART3_HEAD):
        B.need(src.count(s) == 1 and src.index(s) < cut, "%r is not in the instruction part exactly once" % s[:40])
    out = {}
    for q, rows in enumerate(QUARTERS, 1):
        t = src.replace(ROWS_ALL, "These rows: " + ", ".join(rows) + ".", 1)
        t = t.replace(PART3_HEAD, NOTE + "\n\n" + PART3_HEAD, 1)
        B.need(t.index(PART2_HEAD) < t.index(NOTE) < t.index(PART3_HEAD), "%s: the note is not in Part 2" % tag(q))
        new_rows = "These rows: " + ", ".join(rows) + "."
        a, b = src.split("\n"), t.split("\n")
        ops = [(o, a[i1:i2], b[j1:j2]) for o, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False)
               .get_opcodes() if o != "equal"]
        # Line by line: the rows line replaced, and one inserted paragraph (the note and a blank line), nothing else;
        # and taking the note out and putting the rows line back gives the source byte for byte.
        B.need(len(ops) == 2 and ops[0] == ("replace", [ROWS_ALL], [new_rows])
               and ops[1][0] == "insert" and sorted(ops[1][2]) == sorted([NOTE, ""])
               and t.count(NOTE) == 1 and t.count(new_rows) == 1
               and t.replace(NOTE + "\n\n", "", 1).replace(new_rows, ROWS_ALL, 1) == src,
               "%s: the part differs from the source other than by its rows line and the note: %s" % (tag(q), ops))
        brief_part = t[:t.index(FIRST_SECTION)]
        negs, pred = B.check(tag(q), brief_part, t, False)
        out[tag(q)] = dict(text=t, rows=rows, negs=len(negs), pred=pred)
    negs0, pred0 = B.check(SOURCE_TAG, src[:cut], src, False)
    return src, out, (len(negs0), pred0)


def jobs_json(out):
    return json.dumps({
        "purpose": "audit",
        "about": "Supplementary to S81, outside the plan's table: the plan's s81_2b_mimo_A in four parts, one quarter "
                 "of the rows each; see READ ME - written before sending.md in this folder.",
        "jobs": [{"tag": t, "provider": "mimo", "brief": "briefs/%s.txt" % t, "out": "returns", "effort": "medium",
                  "ladder": [131072, 131072], "attempts": 6, "max_rejects": 3, "max_pass": 1,
                  "note": "rows %s-%s of s81_2b_mimo_A; supplementary, outside the S81 table"
                          % (v["rows"][0], v["rows"][-1])} for t, v in out.items()]}, indent=1) + "\n"


def main(check_only):
    src, out, (n0, p0) = parts()
    print("source %s: sha256 %s, %d words; negative words in its instruction part %d; 'prediction' outside it %d"
          % (os.path.relpath(SRC, B.S), sha(src)[:12], len(src.split()), n0, p0))
    files = {os.path.join(SUP, "briefs", t + ".txt"): v["text"] for t, v in out.items()}
    files[JOBS] = jobs_json(out)
    for t, v in out.items():
        B.need(v["negs"] == n0 and v["pred"] == p0, "%s: its checks differ from the source's" % t)
        print("%-22s rows %s-%s: sha256 %s, %d words (source %+d); negative words %d; 'prediction' outside %d"
              % (t, v["rows"][0], v["rows"][-1], sha(v["text"])[:12], len(v["text"].split()),
                 len(v["text"].split()) - len(src.split()), v["negs"], v["pred"]))
    for p, s in files.items():
        have = B.read(p) if os.path.exists(p) else None
        if have == s:
            print("unchanged:", os.path.relpath(p, B.S))
            continue
        B.need(have is None, "%s is there with other content; nothing written" % os.path.relpath(p, B.S))
        B.need(not check_only, "missing: %s" % os.path.relpath(p, B.S))
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "x", encoding="utf-8") as f:
            f.write(s)
        print("written:", os.path.relpath(p, B.S))


if __name__ == "__main__":
    B.need(set(sys.argv[1:]) <= {"--check"}, __doc__)
    main("--check" in sys.argv[1:])
