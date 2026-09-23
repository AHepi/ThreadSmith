#!/usr/bin/env python3
"""s81_build.py: assemble every call of round S81 (file 11 against every case, rebuilt with the S78 repairs), print
word counts, and check each call's text by program before it goes. Written 23 September 2026 for the plan
`tests/S81 Plan - file 11 against every case, rebuilt with the S78 repairs, for two API models.md`; re-roled the same
day for `tests/S81 Plan - second version, Sonnet testers and API auditors.md` (decision S15): Stage 1 (1C, 1K, 1D) is
run by two Sonnet subagent testers, A and B, from folders made by tools/s81_sonnet_prep.py and collected by
tools/s81_sonnet_collect.py; Stage 2 (2a, 2b, 2D, 2W) stays with Atria and Mimo, and each auditor's 2b audits both
testers' 1C returns (fully crossed); each auditor's 2D audits one tester's 1D list with the other's as the second list.

  python Semantics/tools/s81_build.py build            Stage 1 texts (1C, 1K, 1D per tester) and the blind 2a texts
  python Semantics/tools/s81_build.py build2           2b and 2D texts; needs 1C, 1K, 1D and 2a returns
  python Semantics/tools/s81_build.py widen AUDITOR TESTER O7,O9   a 2W text for the stopping rule
  python Semantics/tools/s81_build.py table            marks per case from every return present, and quote checks
  python Semantics/tools/s81_build.py run 2a|2|2W      send the built Stage 2 texts with tools/s80_call.py (thinking on)

Texts go to <OUT>/briefs/<tag>.txt, returns to <OUT>/returns/ (the s80_call layout). OUT defaults to
results/S81 File 11 against every case - outputs; set S81_OUT to build elsewhere (a dry run).
Nothing is sent except by `run`.
"""
import hashlib, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
S = os.path.dirname(HERE)
T, A = os.path.join(S, "tests"), os.path.join(S, "authority")
OUT = os.environ.get("S81_OUT", os.path.join(S, "results", "S81 File 11 against every case - outputs"))
BRIEFS, RET = os.path.join(OUT, "briefs"), os.path.join(OUT, "returns")
F10 = os.path.join(A, "10 Claude Fable Semantics - standalone theory.md")
F11 = os.path.join(A, "11 Claude Fable Semantics - standalone theory, revision 1.md")
BOOK = os.path.join(T, "S81 Case book - the 52 cases, situations and fixed verdicts, as the tested agent sees them.md")
ST1 = os.path.join(T, "S81 Stage 1 testing - file 11 against every case.md")
ST2 = os.path.join(T, "S81 Stage 2 audit - check the Stage 1 return.md")
MD5 = {F10: "3a8cd7c8ca6f3ad3b8a85ab9984d850e", F11: "5e494c1095d920d128b9a79de378f923",
       BOOK: "4f488d149e44669240d5db546c8e946a"}
NOTE_START = "*Revision 1 (file 11)"        # file 11's revision note, withheld from every call
TESTERS, OTHER = ["A", "B"], {"A": "B", "B": "A"}          # Stage 1: two Sonnet subagent testers (decision S15)
AUDITORS = ["atria", "mimo"]                                   # Stage 2: the two API models (decision S12)
D_UNDER_AUDIT = {"atria": "A", "mimo": "B"}                    # 2D: the list under audit; the other tester's is second
CASES = ["O%d" % i for i in range(1, 53)]
# The sampling rule of the plan (section "The 2b sample"). Written here and in the plan only.
BASELINE_NOT_AGREE = ["O1", "O12", "O20", "O21", "O27", "O35", "O40", "O48", "O50"]   # S75: eight SILENT, O48 DISAGREE
RESIDUAL, SALT = 10, "S81-2b-residual"
# Checks. BRIEF_FORBID: none of these in any brief (the instruction part). WHOLE_FORBID: none in any whole call text.
BRIEF_FORBID = ["O48 change", "S75", "prediction", "R2", "S76", "S72", "S78", "S79", "S80", "S81", "file 10", "file 11",
                "Revision", "revision note", "Derivation 3", "amendment"]
STAGE1_FORBID = ["O48", "O24", "{{ROWS}}"]          # also barred from 1-cases, 1-texts and 2a: no row list reaches a tester
WHOLE_FORBID = ["O48 change", "S75", "S76", "Revision 1", "file 10", "file 11", "Semantics results", "R2"]
NEG = re.compile(r"\b(not|never|don't|do not|avoid|nothing|without|neither|nor|cannot|can't|won't|no|none)\b", re.I)
BAR = "=" * 20


def read(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


def write(p, s):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(s)


def md5_ok(p):
    got = hashlib.md5(open(p, "rb").read()).hexdigest()
    assert got == MD5[p], "%s: md5 %s, expected %s (a frozen file changed)" % (os.path.basename(p), got, MD5[p])


def brief(path, name):
    s = read(path)
    m = re.search(r"<!-- BRIEF %s BEGIN -->\n(.*?)\n<!-- BRIEF %s END -->" % (re.escape(name), re.escape(name)), s, re.S)
    assert m, "brief %s missing from %s" % (name, path)
    return m.group(1).strip() + "\n"


def theory11():
    md5_ok(F11)
    lines = read(F11).split("\n")
    i = [k for k, l in enumerate(lines) if l.startswith(NOTE_START)]
    assert len(i) == 1 and lines[i[0] + 1] == "", "file 11's revision note not found where expected"
    out = "\n".join(lines[:i[0]] + lines[i[0] + 2:])
    assert "O48" not in out and "S75" not in out and "file 10" not in out
    return out


def theory10():
    md5_ok(F10)
    return read(F10)


def book(verdicts=True):
    md5_ok(BOOK)
    s = read(BOOK)
    if verdicts:
        return s
    intro = [l for l in s.split("\n") if l.startswith("Fifty-two cases")]
    assert len(intro) == 1
    s = s.replace(intro[0], "Fifty-two cases, O1 to O52. Each has a title and a situation. "
                            "The identifiers O1 to O52 name cases only.")
    s = "\n".join(l for l in s.split("\n") if not l.startswith("**Thoughtful person's verdict.**"))
    s = re.sub(r"\n{3,}", "\n\n", s)
    assert "verdict" not in s.lower(), "a verdict survived in the blind case book"
    return s


def section(title, body):
    return "%s %s %s\n%s\n%s END OF %s %s\n" % (BAR, title, BAR, body.strip(), BAR, title, BAR)


def check(tag, brief_text, whole, stage1):
    """Assert the forbidden strings; print negative words in the brief and every 'prediction' outside it."""
    def has(text, w):
        return re.search(r"\bR2\b", text) if w == "R2" else (w.lower() in text.lower())
    for w in BRIEF_FORBID + (STAGE1_FORBID if stage1 else []):
        assert not has(brief_text, w), "%s: the brief carries %r" % (tag, w)
    for w in WHOLE_FORBID:
        assert not has(whole, w), "%s: the call text carries %r" % (tag, w)
    negs = [brief_text[max(0, m.start() - 30):m.end() + 30].replace("\n", " ") for m in NEG.finditer(brief_text)
            if m.group(0) not in ("NO", "NONE")]
    rest = whole.replace(brief_text, "", 1)
    return negs, len(re.findall("prediction", rest, re.I))


def emit(tag, brief_text, sections, stage1):
    whole = joined(brief_text, sections)
    negs, pred = check(tag, brief_text, whole, stage1)
    write(os.path.join(BRIEFS, tag + ".txt"), whole)
    parts = " + ".join("%s %d" % (t.split()[-1].lower(), len(b.split())) for t, b in sections)
    print("%-16s %6d words  (brief %d + %s)  sha256 %s" % (tag, len(whole.split()), len(brief_text.split()), parts,
                                                           hashlib.sha256(whole.encode()).hexdigest()[:12]))
    print("%16s negative words in the brief: %d%s; 'prediction' in the joined texts: %d"
          % ("", len(negs), (" -> " + " | ".join(negs)) if negs else "", pred))


def calls1():
    """{tag: (brief, sections)} for the Stage 1 and 2a calls; s81_sonnet_prep.py rebuilds from this and compares."""
    b1, bt, b2a = brief(ST1, "1-cases"), brief(ST1, "1-texts"), brief(ST2, "2a")
    t10, t11, bk, bk0 = theory10(), theory11(), book(True), book(False)
    out = {}
    for x in TESTERS:
        out["s81_1C_" + x] = (b1, [("THE THEORY", t11), ("THE CASES", bk)])
        out["s81_1K_" + x] = (b1, [("THE THEORY", t10), ("THE CASES", bk)])
        out["s81_1D_" + x] = (bt, [("TEXT A", t10), ("TEXT B", t11)])
    for a in AUDITORS:
        out["s81_2a_" + a] = (b2a, [("THE THEORY", t11), ("THE CASES", bk0)])
    return out


def joined(brief_text, sections):
    return brief_text + "\n" + "\n".join(section(t, b) for t, b in sections)


def build():
    for tag, (b, secs) in calls1().items():
        emit(tag, b, secs, True)


# ---------------------------------------------------------------- reading returns

def ret(tag):
    p = os.path.join(RET, tag + ".response.txt")
    assert os.path.exists(p), "return missing: " + p
    return read(p)


def records(text):
    """{case: {label: [values]}} from '### O12' records; labels are the upper-case words before a colon."""
    out, cur = {}, None
    for line in text.split("\n"):
        h = re.match(r"^#{2,4}\s*\**\s*(O\d{1,2})\b", line.strip())
        if h and h.group(1) in CASES:
            cur = out.setdefault(h.group(1), {})
            continue
        if line.startswith("## "):
            cur = None
        k = re.match(r"^\**([A-Z][A-Z ]+?)\**:\s*(.*)$", line.strip())
        if cur is not None and k:
            cur.setdefault(k.group(1).strip(), []).append(k.group(2).strip())
    return out


def mark(v):
    v = (v or "").upper()
    for m in ("CASE DISPUTED", "DISAGREE", "SPLIT", "SILENT", "AGREE"):
        if m in v:
            return m
    return "?"


def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = s.replace("—", "-").replace("–", "-").replace("**", "").replace("*", "")
    return re.sub(r"\s+", " ", s).strip()


def loose(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())


def quote_text(v):
    m = re.match(r'^["“](.*)["”]\s*\(', v) or re.match(r'^["“](.*)["”]\s*$', v)
    return m.group(1) if m else v


def where(q, text):
    """VERBATIM, LOOSE (letters and digits match, every piece around an ellipsis) or ABSENT."""
    if norm(q) and norm(q) in norm(text):
        return "VERBATIM"
    pieces = [loose(p) for p in re.split(r"\.\.\.|…", q) if len(loose(p)) >= 12]
    lt = loose(text)
    return "LOOSE" if pieces and all(p in lt for p in pieces) else "ABSENT"


def quote_flags(rec, t_own, t10):
    """For each quote: its standing in the theory the reader was given, and whether file 10 carries it."""
    flags = []
    for v in rec.get("QUOTE", []):
        q = quote_text(v)
        flags.append((where(q, t_own), where(q, t10) != "ABSENT"))
    return flags


def sample(x):
    """The plan's rule for the rows the auditors of tester x's 1C return audit in full, drawn after the returns. The
    rule reads only the returns, so both auditors of x's return get the same rows (second version: fully crossed)."""
    t10, t11 = theory10(), theory11()
    cx, ca, kx = records(ret("s81_1C_" + x)), records(ret("s81_1C_" + OTHER[x])), records(ret("s81_1K_" + x))
    why = {}
    for c in CASES:
        r = cx.get(c, {})
        mx = mark((r.get("MARK") or [""])[0])
        fl = quote_flags(r, t11, t10)
        rs = []
        if mx != "AGREE": rs.append("M1 marked " + mx)
        if mx != mark((ca.get(c, {}).get("MARK") or [""])[0]): rs.append("M2 the other tester's 1C differs")
        if mx != mark((kx.get(c, {}).get("MARK") or [""])[0]): rs.append("M2 own 1K differs")
        if any(s != "ABSENT" and not in10 for s, in10 in fl): rs.append("M3 rests on a sentence absent from file 10")
        if any(s == "ABSENT" for s, _ in fl) or not fl: rs.append("M4 a quotation fails or is missing")
        if (r.get("HOLDS") or [""])[0].upper().startswith("YES"): rs.append("M5 HOLDS YES")
        if c in BASELINE_NOT_AGREE: rs.append("M6 not AGREE at S75")
        if rs: why[c] = rs
    h = hashlib.sha256(ret("s81_1C_" + x).encode()).hexdigest()
    rest = sorted((c for c in CASES if c not in why),
                  key=lambda c: hashlib.sha256(("%s|%s|%s" % (SALT, h, c)).encode()).hexdigest())
    for c in rest[:RESIDUAL]:
        why[c] = ["R residual draw"]
    return [c for c in CASES if c in why], why


def build2():
    b2b, b2d = brief(ST2, "2b"), brief(ST2, "2D")
    assert "{{ROWS}}" in b2b
    t10, t11, bk = theory10(), theory11(), book(True)
    for x in TESTERS:
        rows, why = sample(x)
        write(os.path.join(OUT, "sample - tester %s.json" % x), json.dumps(why, indent=1))
        print("sample, tester %s (audited by %s): %d rows: %s" % (x, " and ".join(AUDITORS), len(rows), ", ".join(rows)))
        filled = b2b.replace("{{ROWS}}", ", ".join(rows) + ".")
        for a in AUDITORS:
            emit("s81_2b_%s_%s" % (a, x), filled, [("THE THEORY", t11), ("THE CASES", bk),
                                                   ("THE READING UNDER AUDIT", ret("s81_1C_" + x)),
                                                   ("YOUR BLIND READINGS", ret("s81_2a_" + a))], False)
    for a in AUDITORS:
        x = D_UNDER_AUDIT[a]
        emit("s81_2D_" + a, b2d, [("TEXT A", t10), ("TEXT B", t11), ("THE LIST UNDER AUDIT", ret("s81_1D_" + x)),
                                  ("THE SECOND LIST", ret("s81_1D_" + OTHER[x]))], False)


def widen(a, x, rows):
    assert a in AUDITORS and x in TESTERS, "widen AUDITOR TESTER ROWS, e.g. widen atria A O7,O9"
    rows = [r.strip() for r in rows.split(",") if r.strip()]
    assert rows and all(r in CASES for r in rows)
    filled = brief(ST2, "2b").replace("{{ROWS}}", ", ".join(rows) + ".")
    emit("s81_2W_%s_%s" % (a, x), filled, [("THE THEORY", theory11()), ("THE CASES", book(True)),
                                           ("THE READING UNDER AUDIT", ret("s81_1C_" + x)),
                                           ("YOUR BLIND READINGS", ret("s81_2a_" + a))], False)


def blind_marks(text):
    """{case: BLIND MARK} from a 2b return: Part 1 records ('BLIND MARK:' lines) and Part 2 one-liners."""
    out = {c: mark((r.get("BLIND MARK") or [""])[0]) for c, r in records(text).items() if r.get("BLIND MARK")}
    for m in re.finditer(r"^\W*(O\d{1,2})\W*:\s*BLIND MARK\s+([A-Z ]+?)\s*;", text, re.M):
        out.setdefault(m.group(1), mark(m.group(2)))
    return out


def table():
    """One row per case: S75's mark, each tester's 1K and 1C marks, each auditor's YOUR MARK on each tester's 1C
    (a 2W record, where there is one, in place of the 2b record), and quote standing."""
    t10, t11 = theory10(), theory11()
    got = {}
    for x in TESTERS:
        for k in ("1K", "1C"):
            p = os.path.join(RET, "s81_%s_%s.response.txt" % (k, x))
            if os.path.exists(p):
                got[(k, x)] = records(read(p))
        for a in AUDITORS:
            for k in ("2b", "2W"):
                p = os.path.join(RET, "s81_%s_%s_%s.response.txt" % (k, a, x))
                if os.path.exists(p):
                    got[(k, a, x)] = records(read(p))
                    if k == "2b":
                        got[("blind", a, x)] = blind_marks(read(p))
    cols = [(k, x) for k in ("1K", "1C") for x in TESTERS if (k, x) in got]
    aud = [(a, x) for x in TESTERS for a in AUDITORS if ("2b", a, x) in got]
    head = ["Case", "S75"] + ["%s %s" % km for km in cols] + ["2b %s on %s" % ax for ax in aud] + \
           ["1C quotes: verbatim/loose/absent; count absent from file 10",
            "both 1C AGREE, a blind mark not (plan v2, step 3)"]
    out = ["| " + " | ".join(head) + " |", "|" + " --- |" * len(head)]
    for c in CASES:
        base = "DISAGREE" if c == "O48" else ("SILENT" if c in BASELINE_NOT_AGREE else "AGREE")
        ms = [mark((got[km].get(c, {}).get("MARK") or [""])[0]) for km in cols]
        au = []
        for a, x in aud:
            w = got.get(("2W", a, x), {})
            r = w.get(c) if c in w else got[("2b", a, x)].get(c, {})
            au.append(mark((r.get("YOUR MARK") or [""])[0]) if r else "-")
        qs = []
        for m in TESTERS:
            if ("1C", m) in got:
                fl = quote_flags(got[("1C", m)].get(c, {}), t11, t10)
                qs.append("%s %d/%d/%d; %d" % (m, sum(s == "VERBATIM" for s, _ in fl), sum(s == "LOOSE" for s, _ in fl),
                                               sum(s == "ABSENT" for s, _ in fl),
                                               sum(s != "ABSENT" and not i for s, i in fl)))
        c1 = [mark((got[("1C", x)].get(c, {}).get("MARK") or [""])[0]) for x in TESTERS if ("1C", x) in got]
        bl = sorted({"%s %s" % (a, got[("blind", a, x)][c]) for a, x in aud
                     if got[("blind", a, x)].get(c, "AGREE") != "AGREE"})
        flag = "READ: " + ", ".join(bl) if len(c1) == 2 and set(c1) == {"AGREE"} and bl else ""
        out.append("| " + " | ".join([c, base] + ms + au + ["; ".join(qs), flag]) + " |")
    write(os.path.join(OUT, "table.md"), "\n".join(out) + "\n")
    print("\n".join(out))


def run(stage):
    sys.path.insert(0, HERE)
    import s80_common as C
    from s80_call import call
    from s80_run import run_pool
    if stage == "1":
        raise SystemExit("Stage 1 is run by Sonnet subagents (second version, decision S15): "
                         "tools/s81_sonnet_prep.py, then tools/s81_sonnet_collect.py")
    pre = {"2a": ("s81_2a_",), "2": ("s81_2b_", "s81_2D_"), "2W": ("s81_2W_",)}[stage]
    jobs = []
    for f in sorted(os.listdir(BRIEFS)):
        tag = f[:-4]
        if f.endswith(".txt") and tag.startswith(pre):
            model = tag.split("_")[2]          # s81_2a_atria, s81_2b_atria_A, s81_2D_mimo, s81_2W_mimo_B
            assert model in AUDITORS, tag
            jobs.append(dict(tag=tag, model=model, out=RET, user=read(os.path.join(BRIEFS, f))))
    run_pool(jobs, lambda j: call(j["model"], None, j["user"], RET, j["tag"], True, C.READER_LADDER,
                                  extra={"round": "S81", "stage": stage}))


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "build"
    {"build": build, "build2": build2, "table": table}.get(cmd, lambda: None)()
    if cmd == "widen":
        if len(sys.argv) != 5:
            raise SystemExit("widen AUDITOR TESTER ROWS, e.g. widen atria A O7,O9")
        widen(sys.argv[2], sys.argv[3], sys.argv[4])
    if cmd == "run":
        run(sys.argv[2])
