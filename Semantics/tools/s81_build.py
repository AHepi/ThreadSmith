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
  python Semantics/tools/s81_build.py table            marks per case from every return present, and quote checks;
                                                       each 2b column's effort, MISSING for an expected 2b with no
                                                       accepted return, the effort confound under the table
  python Semantics/tools/s81_build.py run 2a|2|2W      send the built Stage 2 texts with tools/s80_call.py (thinking on,
                                                       at s80_common.effort_for("audit", auditor): Atria and Mimo
                                                       medium, decision S17); refuses while s81_run2.pid is alive
  python Semantics/tools/s81_build.py run 2 --dry-run  what `run 2` would send, and the files each pass may write;
                                                       sends nothing, writes nothing, needs no keys
  python Semantics/tools/s81_build.py run 2 --effort-controls [--dry-run]
                                                       `run 2` plus the effort controls (EFFORT_CONTROLS below) in
                                                       the same process and the same pool of 3 per provider

Texts go to <OUT>/briefs/<tag>.txt, returns to <OUT>/returns/ (the s80_call layout). OUT defaults to
results/S81 File 11 against every case - outputs; set S81_OUT to build elsewhere (a dry run).
Nothing is sent except by `run`. Every guard is a check that raises SystemExit (never an assert, which `python -O`
drops).
"""
import collections, hashlib, json, os, re, sys

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
# The plan (second version, step 1): an empty or failed return is kept and run once more, recorded as a second attempt.
# `run` refuses to start, and sends nothing, if any call it would send is numbered above this pass.
MAX_PASS = 2
# The plan's Stage 2 ladder (second version, line 52: 48,000, then 64,000). Each provider goes at its probed ceiling on
# every rung, from s80_common.MAX_TOKENS_CEILING (Atria 65,536, Mimo 131,072; third version, change b).
STAGE2_LADDER = [48000, 64000]
# Effort controls: Claude's own process audit, decided after the data under decision S18; outside the plan, and never
# in the S81 table (table() opens named files directly in RET, never this subfolder). Each sends the exact text of an
# accepted high-effort call again at a stated effort, to measure what the switch from high to medium (decision S17)
# changes; the repeat at high separates run-to-run variation from the effect of the effort. One pass each, with the
# same ladders, acceptance rule and deadlines as the real calls. (source tag, effort); the tag is <source>.control-<effort>.
CONTROL_DIR = os.path.join(RET, "effort controls")
EFFORT_CONTROLS = [("s81_2b_atria_A", "medium"), ("s81_2b_atria_A", "high"), ("s81_2a_mimo", "medium")]


def need(ok, msg):
    """A guard that holds under `python -O` too."""
    if not ok:
        raise SystemExit(msg)


def read(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


def write(p, s):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(s)


def md5_ok(p):
    got = hashlib.md5(open(p, "rb").read()).hexdigest()
    need(got == MD5[p], "%s: md5 %s, expected %s (a frozen file changed)" % (os.path.basename(p), got, MD5[p]))


def brief(path, name):
    s = read(path)
    m = re.search(r"<!-- BRIEF %s BEGIN -->\n(.*?)\n<!-- BRIEF %s END -->" % (re.escape(name), re.escape(name)), s, re.S)
    need(m, "brief %s missing from %s" % (name, path))
    return m.group(1).strip() + "\n"


def theory11():
    md5_ok(F11)
    lines = read(F11).split("\n")
    i = [k for k, l in enumerate(lines) if l.startswith(NOTE_START)]
    need(len(i) == 1 and lines[i[0] + 1] == "", "file 11's revision note not found where expected")
    out = "\n".join(lines[:i[0]] + lines[i[0] + 2:])
    need("O48" not in out and "S75" not in out and "file 10" not in out, "file 11 as sent names O48, S75 or file 10")
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
    need(len(intro) == 1, "the case book's opening line was not found once")
    s = s.replace(intro[0], "Fifty-two cases, O1 to O52. Each has a title and a situation. "
                            "The identifiers O1 to O52 name cases only.")
    s = "\n".join(l for l in s.split("\n") if not l.startswith("**Thoughtful person's verdict.**"))
    s = re.sub(r"\n{3,}", "\n\n", s)
    need("verdict" not in s.lower(), "a verdict survived in the blind case book")
    return s


def section(title, body):
    return "%s %s %s\n%s\n%s END OF %s %s\n" % (BAR, title, BAR, body.strip(), BAR, title, BAR)


def check(tag, brief_text, whole, stage1):
    """Check the forbidden strings (raising); return the negative words in the brief and the count of 'prediction'
    outside it."""
    def has(text, w):
        return re.search(r"\bR2\b", text) if w == "R2" else (w.lower() in text.lower())
    for w in BRIEF_FORBID + (STAGE1_FORBID if stage1 else []):
        need(not has(brief_text, w), "%s: the brief carries %r" % (tag, w))
    for w in WHOLE_FORBID:
        need(not has(whole, w), "%s: the call text carries %r" % (tag, w))
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
    need(os.path.exists(p), "return missing: " + p)
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
    need("{{ROWS}}" in b2b, "the 2b brief has no {{ROWS}} place")
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
    need(a in AUDITORS and x in TESTERS, "widen AUDITOR TESTER ROWS, e.g. widen atria A O7,O9")
    rows = [r.strip() for r in rows.split(",") if r.strip()]
    need(rows and all(r in CASES for r in rows), "widen: rows must be case names O1 to O52")
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


def _ret(name):
    """A file directly in returns/, by its exact name. The table opens nothing else there, and never a subfolder, so it
    never reads the effort controls or the folders set aside by decision S16."""
    need(name and os.sep not in name and not (os.altsep and os.altsep in name) and not name.startswith("."),
         "the table reads files directly in returns/ only, not %r" % name)
    return os.path.join(RET, name)


def _json(p):
    try:
        return json.loads(read(p))
    except (OSError, ValueError):
        return None


def audit_state(a, x):
    """The expected 2b audit of tester x's 1C return by auditor a, from names and structural fields only: whether an
    accepted response is there, the effort its request.json records (that of the last attempt sent, which for an
    accepted return is the accepted one), and how many of its passes left a failed receipt."""
    tag = "s81_2b_%s_%s" % (a, x)
    kept = re.compile(re.escape(tag) + r"(\.pass\d+)?\.receipt\.json$")
    receipts = [n for n in sorted(os.listdir(RET)) if kept.match(n)]
    return dict(tag=tag, accepted=os.path.exists(_ret(tag + ".response.txt")),
                effort=(_json(_ret(tag + ".request.json")) or {}).get("reasoning_effort") or "effort not recorded",
                failed=sum(1 for n in receipts if (_json(_ret(n)) or {}).get("failed")))


def missing_text(failed):
    return {0: "MISSING (no return)", 1: "MISSING (failed once)", 2: "MISSING (failed twice)"}.get(
        failed, "MISSING (failed %d times)" % failed)


def effort_line(states):
    """One line naming the effort of the four expected 2b audits, and the confound when they differ (plan, third
    version, change c); an expected audit with no accepted return is named as missing."""
    name = lambda ax: "2b %s on %s" % (ax[0].capitalize(), ax[1])
    eff = {ax: s["effort"] for ax, s in states.items()}
    counts = collections.Counter(eff.values())
    words = {1: "one", 2: "two", 3: "three"}
    if len(counts) == 1:
        parts = ["all four 2b audits sent at %s" % next(iter(counts))]
    else:
        major = counts.most_common(1)[0][0]
        parts = ["%s at %s" % (name(ax), e) for ax, e in eff.items() if e != major]
        parts.append("the other %s at %s" % (words.get(counts[major], counts[major]), major))
    parts += ["%s missing" % name(ax) for ax, s in states.items() if not s["accepted"]]
    return ("Effort confound (plan, third version, change c): " if len(counts) > 1 else "Effort: ") + \
        "; ".join(parts) + "."


def table():
    """One row per case: S75's mark, each tester's 1K and 1C marks, each auditor's YOUR MARK on each tester's 1C
    (a 2W record, where there is one, in place of the 2b record), and quote standing. Every expected 2b audit has its
    column, headed with the effort its request.json records; one with no accepted return shows MISSING in every row. A
    blind mark missing from an accepted 2b return is never taken as AGREE: it shows as — and is counted under the
    table, beside one line naming the effort confound. Only named files directly in returns/ are opened."""
    t10, t11 = theory10(), theory11()
    got = {}
    for x in TESTERS:
        for k in ("1K", "1C"):
            p = _ret("s81_%s_%s.response.txt" % (k, x))
            if os.path.exists(p):
                got[(k, x)] = records(read(p))
        for a in AUDITORS:
            for k in ("2b", "2W"):
                p = _ret("s81_%s_%s_%s.response.txt" % (k, a, x))
                if os.path.exists(p):
                    got[(k, a, x)] = records(read(p))
                    if k == "2b":
                        got[("blind", a, x)] = blind_marks(read(p))
    cols = [(k, x) for k in ("1K", "1C") for x in TESTERS if (k, x) in got]
    expected = [(a, x) for x in TESTERS for a in AUDITORS]
    states = {ax: audit_state(*ax) for ax in expected}
    aud = [ax for ax in expected if ("2b",) + ax in got]
    head = ["Case", "S75"] + ["%s %s" % km for km in cols] + \
           ["2b %s on %s (%s)" % (a, x, states[(a, x)]["effort"]) for a, x in expected] + \
           ["1C quotes: verbatim/loose/absent; count absent from file 10",
            "both 1C AGREE, a blind mark not AGREE or missing (plan v2, step 3)"]
    out = ["| " + " | ".join(head) + " |", "|" + " --- |" * len(head)]
    no_blind = {ax: [] for ax in aud}
    for c in CASES:
        base = "DISAGREE" if c == "O48" else ("SILENT" if c in BASELINE_NOT_AGREE else "AGREE")
        ms = [mark((got[km].get(c, {}).get("MARK") or [""])[0]) for km in cols]
        au = []
        for a, x in expected:
            if (a, x) not in aud:
                au.append(missing_text(states[(a, x)]["failed"]))
                continue
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
        bl = []
        for a, x in aud:
            b = got[("blind", a, x)].get(c)
            if b is None:                      # missing: shown as —, counted apart, never taken as AGREE
                no_blind[(a, x)].append(c)
                bl.append("%s on %s —" % (a, x))
            elif b != "AGREE":
                bl.append("%s on %s %s" % (a, x, b))
        flag = "READ: " + ", ".join(sorted(bl)) if len(c1) == 2 and set(c1) == {"AGREE"} and bl else ""
        out.append("| " + " | ".join([c, base] + ms + au + ["; ".join(qs), flag]) + " |")
    n_no = sum(len(v) for v in no_blind.values())
    out += ["", effort_line(states),
            "Blind marks missing from an accepted 2b return (shown as —, never counted as AGREE): %d%s" % (
                n_no, "".join("; %s on %s: %s" % (a, x, ", ".join(v)) for (a, x), v in no_blind.items() if v))]
    write(os.path.join(OUT, "table.md"), "\n".join(out) + "\n")
    print("\n".join(out))


def run(stage, dry=False, controls=False):
    sys.path.insert(0, HERE)
    import s80_common as C
    from s80_call import call, pass_plan, PROVIDERS
    from s80_run import run_pool
    if stage == "1":
        raise SystemExit("Stage 1 is run by Sonnet subagents (second version, decision S15): "
                         "tools/s81_sonnet_prep.py, then tools/s81_sonnet_collect.py")
    need(stage in ("2a", "2", "2W"), "run 2a|2|2W, not %r" % stage)
    # The runner of pass 2 and the effort controls ran from the code before the slot lock and takes no slot.
    if not dry:
        C.refuse_if_runner_alive()
    pre = {"2a": ("s81_2a_",), "2": ("s81_2b_", "s81_2D_"), "2W": ("s81_2W_",)}[stage]
    jobs = []
    for f in sorted(os.listdir(BRIEFS)):
        tag = f[:-4]
        if f.endswith(".txt") and tag.startswith(pre):
            model = tag.split("_")[2]          # s81_2a_atria, s81_2b_atria_A, s81_2D_mimo, s81_2W_mimo_B
            need(model in AUDITORS, "%s: %r is not an auditor; nothing sent" % (tag, model))
            # Thinking effort from the one map: Stage 2 is an audit (decision S17: Atria and Mimo at medium).
            jobs.append(dict(tag=tag, model=model, out=RET, user=read(os.path.join(BRIEFS, f)),
                             effort=C.effort_for("audit", model), control_of=None))
    if controls:
        need(stage == "2", "--effort-controls goes with `run 2` only")
        for src, eff in EFFORT_CONTROLS:
            user = read(os.path.join(BRIEFS, src + ".txt"))
            rec = json.loads(read(os.path.join(RET, src + ".receipt.json")))
            need(not rec.get("failed") and os.path.exists(os.path.join(RET, src + ".response.txt"))
                 and C.sha256(user) == rec["user_sha256"],
                 "%s: the brief is not the text of an accepted call; nothing sent" % src)
            jobs.append(dict(tag="%s.control-%s" % (src, eff), model=src.split("_")[2], out=CONTROL_DIR, user=user,
                             effort=eff, control_of=src))
    # Before anything is sent: a real call goes as pass MAX_PASS at most; a control goes once, into an empty slot.
    for j in jobs:
        if not os.path.exists(os.path.join(j["out"], j["tag"] + ".response.txt")):
            k, limit = pass_plan(j["out"], j["tag"])[1], (1 if j["control_of"] else MAX_PASS)
            need(k <= limit, "%s would go as pass %d, above %d; nothing sent" % (j["tag"], k, limit))
    # max_tokens: the plan's ladder with each provider's probed ceiling on every rung (s80_common.ladder_for): Mimo
    # 131,072 (its reasoning at high outgrew 64,000 on 2a, three attempts with no content; lesson S7), Atria 65,536
    # (it refuses more; its first 2b call ran out at 48,000).
    ladder = lambda m: C.ladder_for(m, STAGE2_LADDER)
    if dry:
        dry_run(jobs, ladder, C, pass_plan, PROVIDERS)
        return

    def one(j):
        extra = {"round": "S81", "stage": stage, "effort_from": "s80_common.effort_for('audit', provider)"}
        if j["control_of"]:
            extra.update(effort_control=True, control_of=j["control_of"], effort_from="EFFORT_CONTROLS",
                         note="Claude's process audit, decided after the data under decision S18; "
                              "outside the S81 plan and never in its table")
        if not os.path.exists(os.path.join(j["out"], j["tag"] + ".response.txt")):
            C.log("start", j["model"], j["tag"], "effort", j["effort"])
        return call(j["model"], None, j["user"], j["out"], j["tag"], True, ladder(j["model"]), extra=extra,
                    effort=j["effort"])
    run_pool(jobs, one)


def dry_run(jobs, ladder, C, pass_plan, providers, attempts=6, max_rejects=3):
    """Print what `run` would send, with s80_call.call's own defaults, and every file each pass may write; list any
    such file that is already there (none should be). Reads the folders only."""
    pid = C.live_pid(C.S81_RUN_PIDFILE)
    if pid:
        print("NOTE: %s names live pid %d; a real run refuses to start until it ends" % (C.S81_RUN_PIDFILE, pid))
    send = []
    for j in jobs:
        t, m, d = j["tag"], j["model"], j["out"]
        names = set(os.listdir(d)) if os.path.isdir(d) else set()
        if t + ".response.txt" in names:
            print("%-16s skip: %s.response.txt is there" % (t, t))
            continue
        send.append(j)
        renames, k = pass_plan(d, t)
        freed = {old for old, _ in renames}
        may = [t + e for e in (".request.json", ".response.txt", ".reasoning.txt", ".receipt.json", ".error.txt")]
        may += ["%s.pass%d.a%d.%s.txt" % (t, k, n, w) for n in range(1, attempts + 1)
                for w in ("truncated", "reasoning")]
        clash = sorted(f for f in may if f in names and f not in freed)
        kind = ("CONTROL of %s, into returns/%s/" % (j["control_of"], os.path.relpath(d, RET)) if j["control_of"]
                else "real, into returns/")
        print("%-16s SEND (%s) to %s (%s): pass %d; max_tokens %s; thinking on, reasoning_effort %s; temperature %s; "
              "text sha256 %s, %d words" % (t, kind, m, providers[m][1], k, ladder(m), j["effort"],
                                            C.TEMPERATURE, C.sha256(j["user"])[:12], len(j["user"].split())))
        print("%16s renamed first: %s" % ("", ", ".join("%s -> %s" % r for r in renames) or "none"))
        print("%16s may write: %s.pass%d.a<1..%d>.truncated.txt / .reasoning.txt (attempts that come back and fail), "
              "then %s.request.json, and on success .reasoning.txt, .receipt.json and last .response.txt, or on "
              "failure .error.txt and .receipt.json; already there: %s" % ("", t, k, attempts, t,
                                                                          ", ".join(clash) or "none"))
    per = {m: sum(j["model"] == m for j in send) for m in AUDITORS}
    real = [j for j in send if not j["control_of"]]
    print("to send: %d calls (%s), %d real and %d controls; at most %d in flight per provider across every process "
          "(slot locks in %s)%s; up to %d attempts per call, at most %d that come back and fail" % (
              len(send), ", ".join("%s %d" % kv for kv in per.items()), len(real), len(send) - len(real),
              C.SLOTS_PER_PROVIDER, C.LOCK_DIR,
              ", so all start at once if no other process holds a slot" if max(per.values() or [0]) <= 3
              else ", so some wait for a free slot", attempts, max_rejects))
    for j in send:
        print("   %-32s %-5s effort %-6s %s" % (j["tag"], j["model"], j["effort"],
                                              "control" if j["control_of"] else "real"))


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "build"
    {"build": build, "build2": build2, "table": table}.get(cmd, lambda: None)()
    if cmd == "widen":
        if len(sys.argv) != 5:
            raise SystemExit("widen AUDITOR TESTER ROWS, e.g. widen atria A O7,O9")
        widen(sys.argv[2], sys.argv[3], sys.argv[4])
    if cmd == "run":
        need(len(sys.argv) > 2, "run 2a|2|2W [--dry-run] [--effort-controls]")
        need(set(sys.argv[3:]) <= {"--dry-run", "--effort-controls"}, "unknown option in %s" % sys.argv[3:])
        run(sys.argv[2], dry="--dry-run" in sys.argv[3:], controls="--effort-controls" in sys.argv[3:])
