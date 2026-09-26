#!/usr/bin/env python3
"""s96_build.py: build the S96 cross-examination of the repaired copy (the scrubbed copy of draft 5, repaired under
decisions S25 to S27), in two halves for Atria and four quarters for Mimo, and its job list for tools/s87_run.py.
Written 26 September 2026 by a Claude subagent (agent 14 of the owner's 15 for this task) for the orchestrator (log
S96), on the model of tools/s93_build.py.

  python3 Semantics/tools/s96_build.py           build the six briefs and the job list; refuses to overwrite a file
                                                 whose content differs
  python3 Semantics/tools/s96_build.py --check   rebuild in memory and compare with the files; writes nothing

What is cross-examined: the whole repaired copy, 632 lines, md5 8bb4d19d5aad53de2492b2193fd23ff1.
  - Atria, two halves (each at most 15,000 words; Atria failed on briefs over about 18,000, lesson S20):
      A  lines 1-372, the title, the two opening notes (l. 2 and l. 8) and Parts 0 to VIII;
      B  lines 373-632, Parts IX to XVI, the last being the numbered Arguments.
  - Mimo, four quarters of the same text (smaller, since Mimo ran away on large tasks, lesson S20):
      1  lines 1-164, the title, the opening notes and Parts 0 to III;
      2  lines 165-320, Parts IV to VI;
      3  lines 321-484, Parts VII to XII;
      4  lines 485-632, Parts XIII to XVI.
  Each part also carries, for their definitions, lines examined in a companion part (the CONTEXT ranges below).
Each part carries: the owner's words of decisions S20 to S27, quoted from records/Semantics - Decisions.md with every
quoted word unchanged (S27 whole), and the connecting words outside the quotation marks the recorder's, with internal
record labels replaced by plain descriptions (REPLACE below); a sentence saying what the owner's footnotes of S27
answered; the six questions Q1 to Q6; the lines, each with its line number; and a report form ending in one verdict
line per question, "OVERALL: SOUND" or "OVERALL: NEEDS REPAIR", and "END OF REPORT".
Withheld: the record's readings of the decisions (the owner's words decide), the S95 and S96 results and checks, the
change lists and scripts, the case book, and every model name.

Sources are compared by md5 before anything is built; the build refuses on any mismatch. The frame of every brief
(everything but the owner's words and the lines of the text) is scanned for the words decision S23 forbids and for
words near them, and the build refuses on any hit outside the one sentence of Q1 that names the forbidden ideas.
"""
import hashlib, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SEM = os.path.dirname(HERE)
TESTS = os.path.join(SEM, "tests")
OUT_DIR = os.path.join(SEM, "results", "S96 Cross-examination - repaired copy - returns")
JOBS = os.path.join(HERE, "s96_jobs - repaired copy.json")
READING_RULE = "results/S96 How the cross-examination of the repaired copy will be read - written before sending.md"

SRC = {
    "text": ("tests/Revision 2 - scrubbed copy, repaired (S96), theory text.md", "8bb4d19d5aad53de2492b2193fd23ff1"),
    "decisions": ("records/Semantics - Decisions.md", "89a661c3bc46ac986d2110a6c492df3a"),
}
CAP = {"atria": 15000, "mimo": 9000}   # words, by the runner's count and by wc -w; Mimo's parts about half of Atria's


def read(rel):
    with open(os.path.join(SEM, rel), encoding="utf-8") as f:
        return f.read()


def md5(s):
    return hashlib.md5(s.encode("utf-8")).hexdigest()


def need(ok, msg):
    if not ok:
        raise SystemExit("s96_build: " + msg)


def wc_words(s):
    """wc -w in the C locale: runs of bytes that are not ASCII whitespace."""
    return len(re.findall(rb"[^ \t\n\r\v\f]+", s.encode("utf-8")))


# ------------------------------------------------------------------ sources
T = {}
for k, (rel, want) in SRC.items():
    T[k] = read(rel)
    need(md5(T[k]) == want, "%s: md5 %s, expected %s" % (rel, md5(T[k]), want))
TX = T["text"].split("\n")
if TX and TX[-1] == "":
    TX = TX[:-1]
N = len(TX)
need(N == 632, "the repaired copy has %d lines, expected 632" % N)

# ------------------------------------------------------------------ the owner's words, S20 to S27
dec = T["decisions"]
OWN = {}
for n in range(20, 28):
    m = re.search(r"(?m)^S%d\. \[Claude's reading: .*?\] (.*)$" % n, dec)
    need(m, "decision S%d not found" % n)
    OWN[n] = m.group(1)

# The recorder's connecting words that name internal records, replaced by plain descriptions. Each must occur once in
# its decision, outside every quotation: the text before it and after it must each hold an even number of straight
# double quotation marks.
REPLACE = [
    (21, "Answering file 93's choices (log S93): ", "Answering choices the drafters had put to the owner: "),
    (22, "Said while the S94 workflow was running (log S94): ", "Said while a workflow of Claude agents was running: "),
    (23, "Next step after log S94, in three paragraphs: ", "Next step, in three paragraphs: "),
    (24, "Said while the S95 workflow was running (log S95): ",
     "Said while the workflow of Claude agents for the scrub was running: "),
    (25, " (log S95): ", ": "),
    (26, " (log S95): ", ": "),
]
OWNER_TEXT = dict(OWN)
for n, old, new in REPLACE:
    s = OWNER_TEXT[n]
    need(s.count(old) == 1, "S%d: %r occurs %d times" % (n, old, s.count(old)))
    i = s.index(old)
    need(s[:i].count('"') % 2 == 0 and s[i + len(old):].count('"') % 2 == 0, "S%d: %r lies inside a quotation" % (n, old))
    OWNER_TEXT[n] = s.replace(old, new)
# every quotation of the owner is unchanged: the texts differ only at the replaced connecting words
for n in OWN:
    a, b = OWN[n], OWNER_TEXT[n]
    for _, old, new in [r for r in REPLACE if r[0] == n]:
        b = b.replace(new, old, 1)
    need(a == b, "S%d: the owner's words changed" % n)
need('"Two important footnotes so your agents aren\'t led astray"' in OWN[27] or
     "Two important footnotes so your agents aren't led astray" in OWN[27], "S27 is not the full decision")
need(OWN[27].rstrip().endswith("(26 September 2026)") and "It's also a detail that exists outside the process." in
     OWN[27], "S27 is not whole")

DATES = {20: "24 and 25 September 2026", 21: "25 September 2026", 22: "25 September 2026", 23: "25 September 2026",
         24: "25 September 2026", 25: "26 September 2026", 26: "26 September 2026", 27: "26 September 2026"}

OWNER = "\n\n".join(
    ["## 2. The owner's words",
     "The theory's owner took the decisions below, S20 to S27, in this order; the questions in section 4 are asked "
     "against them. Each is quoted from the project's record of decisions. Everything inside quotation marks is the "
     "owner's, word for word, typos included. The few connecting words outside the quotation marks are the recorder's; "
     "where the record names internal files or logs there, a plain description stands in their place. The record's "
     "own reading of each decision is not given here: the owner's words decide, and where a question in section 4 is "
     "worded differently from them, the owner's words decide there too, and you should say so. In these words "
     "\"Claude\" is the drafters of the text; \"your agents\" and \"your explanation\" in S27 are addressed to them."] +
    ["**S%d** (%s). %s" % (n, DATES[n], OWNER_TEXT[n]) +
     ("\n\n*What S27 answers.* Between S26 and S27 the drafters gave the owner the five examples asked for: holding "
      "an explanation in a carrier (ink, a brain, a file); copying or teaching it; testing between two rival "
      "explanations, where the test changes the thing explained; building from an explanation (a perpetual-motion "
      "machine, a bridge); and performing music. The examples are the drafters' words, not the owner's, and are not "
      "a decision. S27 is the owner's reply to them." if n == 26 else "")
     for n in range(20, 28)])

# ------------------------------------------------------------------ the parts
HEADS = [(i + 1, TX[i]) for i in range(N) if TX[i].startswith("#")]

# context ranges (first line, last line), given for their definitions
C_OPEN = [(1, 8)]                    # title, the experiment note (l. 2), Part 0's heading and its "Two words" (l. 8)
C_WORDS = [(7, 8)]                   # Part 0's heading and its "Two words" (l. 8): argument, and accepting
C_ATTR = [(75, 75)]                  # Part I: substrate independence with physical conditions
C_QUEST = [(133, 147), (159, 159)]   # Part III: a question and its contract; scope and the range of changes
C_ACC = [(229, 233), (255, 257)]     # Part V: the candidate, component fidelity; non-circular dependence, non-vacuity
C_275 = [(275, 275)]                 # Part V: a contrast no edit of the target realizes
C_RIV = [(313, 317)]                 # Part VI: commitments that do no work, rivals and conflict, problems
C_ARG = [(385, 397)]                 # Part IX: reason use, usability (K2), Form, what a test rules out, arguments
C_PHYS = [(459, 461), (497, 497)]    # Part XII: tasks; Part XIII: universality

PARTS = [
    dict(key="A", model="atria", title="Parts 0 to VIII, with the opening notes", own=(1, 372),
         ctx=C_ARG + C_PHYS),
    dict(key="B", model="atria", title="Parts IX to XVI, with the Arguments", own=(373, 632),
         ctx=C_OPEN + C_ATTR + C_QUEST + C_ACC + C_275 + C_RIV),
    dict(key="1", model="mimo", title="the opening notes, and Parts 0 to III", own=(1, 164),
         ctx=[(257, 257), (315, 315), (393, 397)]),
    dict(key="2", model="mimo", title="Parts IV to VI", own=(165, 320),
         ctx=C_WORDS + C_ATTR + [(159, 159), (393, 397), (461, 461)]),
    dict(key="3", model="mimo", title="Parts VII to XII", own=(321, 484),
         ctx=C_WORDS + [(159, 159), (229, 231), (257, 257), (315, 315)]),
    dict(key="4", model="mimo", title="Parts XIII to XVI, with the Arguments", own=(485, 632),
         ctx=C_WORDS + [(159, 159), (229, 231), (257, 257), (315, 315), (393, 397), (461, 461)]),
]
# the parts of each model tile lines 1-632 exactly once
for model in ("atria", "mimo"):
    rs = sorted(p["own"] for p in PARTS if p["model"] == model)
    need(rs[0][0] == 1 and rs[-1][1] == N and all(rs[i][1] + 1 == rs[i + 1][0] for i in range(len(rs) - 1)),
         "%s's parts do not tile lines 1-%d" % (model, N))


def heads_in(a, b, level=1):
    return [h.lstrip("#").strip() for i, h in HEADS if a <= i <= b and len(h) - len(h.lstrip("#")) == level]


def lines(a, b):
    return ["L%d| %s" % (i, TX[i - 1]) if TX[i - 1].strip() else "" for i in range(a, b + 1)]


def excerpt(ranges, own):
    """The lines of the ranges, in text order, less the part's own lines, which stand in section 3a and are named here
    by one bracketed line; each other run not given is named by one bracketed line with the headings it holds."""
    keep = set()
    for a, b in ranges:
        keep |= set(range(a, b + 1))
    keep -= set(range(own[0], own[1] + 1))
    kind = lambda i: "keep" if i in keep else "own" if own[0] <= i <= own[1] else "gap"
    out, i = [], 1
    while i <= N:
        j = i
        while j + 1 <= N and kind(j + 1) == kind(i):
            j += 1
        if kind(i) == "keep":
            out += lines(i, j) + [""]
        elif kind(i) == "own":
            out += ["[L%d–L%d: the lines this part examines, given in section 3a]" % (i, j), ""]
        else:
            hs = "; ".join(h.lstrip("#").strip() for k, h in HEADS if i <= k <= j)
            out += ["[L%d–L%d not given here: %s]" % (i, j, hs or "no heading"), ""]
        i = j + 1
    while out and out[-1] == "":
        out.pop()
    return "\n".join(out)


# ------------------------------------------------------------------ fixed texts
Q1_NAMES = ("verification or falsification in an absolute sense, justification, belief, authority, foundation, or a "
            "ranking of candidates")   # the one span of the frame that names the forbidden ideas (decision S23)

QUESTIONS = """**Q1. What the scrub left.** Decision S23 forbids the words it lists and the ideas behind them. In the lines this part examines, is any word or idea left that implies %s? Is any "accept" or "accepted" not tentative? Is any "argument" used as reasons for this, rather than as reasons why this and not that? Look for disguised synonyms as well as the listed words. A listed word inside a quotation of the owner, or where the text names a word in order to set it aside, is not a fault.

**Q2. Physical possibility.** Does physical possibility, or an adopted physics, still define explanation anywhere in these lines: a question's range of changes, non-vacuity, conflict, fidelity, or the requirements a candidate has to meet? Or does it enter only where information or knowledge is instantiated or transformed (in the drafters' examples: held in a carrier, copied, taught, tested, built, performed), or as the content of a claim about what is possible or impossible, such as "perpetual motion is impossible"? And, as the text stands, can a piece of mathematics, a melody or a philosophical claim be the target of a question?

**Q3. Conflict by argument.** Does the text say that explanations can conflict with no test against the world; that a bare claim, tentatively accepted (such as "perpetual motion is impossible"), is enough to trigger a conflict and, in the owner's words, "not enough for a creative agent to do anything about it"; and that what is done about a conflict is the choice of the person choosing? Where these lines rely on the text's definitions of conflict and of an argument, those definitions are among the lines given in section 3.

**Q4. Premises taken as given.** May an argument use a claim whose explanation the person using it does not contain, even a claim accepted as a given without any thought? Does the text avoid requiring that anyone contain the whole of such an explanation before using the claim to find errors?

**Q5. What breaks.** Does anything break: a definition; a symbol used before it is defined, or defined two ways; a cross-reference to a Part, line, label or tag that does not say what it is cited for; or a step of an argument (the numbered Arguments of Part XVI included) that no longer goes through after the repairs?

**Q6. Faithfulness.** Does any sentence say more than the owner's words in section 2 say, or less than they require? In particular: does a sentence present the drafters' reading as the owner's words; bring back a list or set of rivals or versions, a count, a grade, a ranking, or a record doing work that the explanation's own content should do (decision S20); or state what must happen to candidates, where the owner speaks only of what the person choosing does and "sees no option" (decision S21)?""" % Q1_NAMES

VERDICTS = [
    "`Q1: NOTHING LEFT` or `Q1: LEFT — <the places>`",
    "`Q2: KEPT OUT OF WHAT DEFINES EXPLANATION` or `Q2: STILL DEFINES — <the places>`",
    "`Q2 targets: ALL THREE CAN BE TARGETS` or `Q2 targets: NOT ALL — <which, and the words that stop it>`",
    "`Q3: SAID` or `Q3: SAID IN PART — <what is missing or at fault>` or `Q3: NOT SAID`",
    "`Q4: ALLOWED, AND NOT REQUIRED` or `Q4: FAULT — <the place>`",
    "`Q5: NOTHING BREAKS` or `Q5: BREAKS — <the places>`",
    "`Q6: FAITHFUL`, `Q6: SAYS MORE — <the places>`, `Q6: SAYS LESS — <the places>` or `Q6: SAYS MORE AND LESS — "
    "<the places>`",
]


def build_part(p):
    a, b = p["own"]
    parts = heads_in(a, b)
    if a == 1:
        need(parts[0] == "Claude Fable Semantics", "line 1 is not the title")
        parts[0] = "the title, with the editorial note on line 2"
    title = "# Cross-examination of the repaired copy, part %s: %s" % (p["key"], p["title"])
    s1 = ["## 1. What you are asked to do",
          "Section 3 gives lines of a theory of explanation: a formal semantics of what an explanation is and of "
          "explanatory creativity, 632 lines in all. Its owner took the decisions quoted in section 2. Under decision "
          "S23 the text was scrubbed of the words and ideas that decision forbids. Under decisions S25 to S27 it was "
          "then repaired, in two stages, so that physical possibility no longer defines what an explanation is, and "
          "so that it says what the owner said about conflict found by argument and about premises taken as given. No "
          "outside reader has seen the repaired text.",
          "The cross-examination is split into parts, each read on its own. **This part examines lines %d to %d: %s.** "
          "Section 3 gives those lines whole, and then, for their definitions, some lines that a companion part "
          "examines; raise a finding on those only where the lines this part examines depend on them or pull against "
          "them." % (a, b, "; ".join(parts)),
          "**Your stance.** Those who repaired the text put it forward as obeying the owner's decisions and as holding "
          "together. Your job is to attack that as hard as you can, against the texts alone. An answer that finds no "
          "fault tells us something only when it shows the attacks you made and why each one failed.",
          "**Who is who.** In the text, \"the owner\" is the theory's owner, whose words are in section 2, and "
          "\"Claude\" is the drafters. A sentence the text marks \"[Claude's reading ...]\" is one the drafters marked "
          "as their reading, not the owner's words.",
          "**Citing the text.** Line numbers are those of the whole text, with its title as line 1; section 3 prints "
          "each line's number before it. Quote the text whenever you rely on it, with its line number.",
          "Section 2 quotes the owner's words, section 3 gives the text, section 4 asks the questions, and section 5 "
          "sets out the form of the report."]
    s3 = ["## 3. The text",
          "Each line below is a line of the repaired text, given as `L<number>| ` followed by the line exactly as it "
          "stands; the prefix is not part of the text. Blank lines are kept blank.%s" % (
              " Line 2 is an editorial note on how the copy was made; it names files and records you do not have, "
              "and you need not follow them." if a <= 2 <= b or any(x <= 2 <= y for x, y in p["ctx"]) else ""),
          "### 3a. The lines this part examines: lines %d to %d" % (a, b),
          "=============== BEGIN LINES %d TO %d ===============" % (a, b),
          "\n".join(lines(a, b)).rstrip("\n"),
          "=============== END LINES %d TO %d ===============" % (a, b),
          "### 3b. Lines given for their definitions (a companion part examines them)",
          "Where lines are not given, one bracketed line names them and the headings they hold.",
          "=============== BEGIN LINES GIVEN FOR THEIR DEFINITIONS ===============",
          excerpt(p["ctx"], p["own"]),
          "=============== END LINES GIVEN FOR THEIR DEFINITIONS ==============="]
    s5 = ["## 4. The questions",
          "Ask each question of the lines this part examines (section 3a), using the lines of section 3b where these "
          "lines rely on them.",
          QUESTIONS,
          "**For every finding** give the place (line numbers), what is at fault, shown from the text with quotations, "
          "and the exact wording you propose in its place. Keep apart what the text forces and what a reader might take "
          "it to mean."]
    s6 = ["## 5. The report", "\n".join([
        "- Number your findings in one list, most serious first. Head each with the question it falls under and the "
        "lines, for example `Q2 · L<n>` or `Q3 · L<n>–L<m>`.",
        "- For every finding, give the exact wording you propose, between fence lines, whole (the sentence or "
        "paragraph as it should stand), so that it could be put in place as written; where the repair is to delete "
        "words, say which.",
        "- Then answer each question, Q1 to Q6, in one short paragraph each, headed by the question, and end the "
        "paragraph with its verdict line, exactly as follows (Q2 has two lines):"] +
        ["  - " + v for v in VERDICTS] + [
        "- Then one line reading exactly `OVERALL: SOUND` or `OVERALL: NEEDS REPAIR`. NEEDS REPAIR means that at least "
        "one finding asks for the text to change.",
        "- Keep the report under about 3,000 words. Depth on the findings that matter counts for more than coverage of "
        "small ones.",
        "- End the report with a line that reads exactly END OF REPORT."])]
    text = "\n\n".join([title] + s1 + [OWNER] + s3 + s5 + s6) + "\n"
    return text


# ------------------------------------------------------------------ the scan of the frame (decision S23)
SCRUB = [r"\bfits?\b", r"\bfitt\w*", r"\bsupport\w*", r"\bverif\w*", r"\bcorroborat\w*", r"\bprov(e|es|ed|en|ing)\b",
         r"\bdisprov\w*", r"\bbelie\w*", r"better than", r"worse than", r"\btrue\b", r"\btruth\w*", r"\bestablish\w*",
         r"\bauthorit\w*", r"\bfoundation\w*", r"\bderiv\w*", r"\bjustif\w*", r"\brank\w*", r"\bvalid\w*",
         r"\bcorrect(ly|ness)?\b", r"\bevidence\b", r"\bconfirm\w*", r"\bcertain\w*", r"\bgrade[sd]?\b", r"\bwrong\b",
         r"\bAtria\b", r"\bMimo\b", r"\bDeutsch\b", r"\bMarletto\b", r"\bPinker\b"]
ALLOWED_IN_FRAME = [Q1_NAMES, "a grade, a ranking"]   # Q1 names the forbidden ideas; Q6 names what S20 rules out


def frame_of(text):
    f = re.sub(r"(?s)=============== BEGIN LINES.*?=============== END LINES[^\n]*===============", "", text)
    f = re.sub(r"(?s)## 2\. The owner's words.*?(?=## 3\. The text)", "", f)
    for s in ALLOWED_IN_FRAME:
        f = f.replace(s, "")
    return f


def scan(text):
    f = frame_of(text)
    return sorted({m.group(0) for pat in SCRUB for m in re.finditer(pat, f, re.I)})


def build():
    out, rows = {}, []
    for p in PARTS:
        text = build_part(p)
        hits = scan(text)
        need(not hits, "part %s: forbidden or withheld words in the frame: %s" % (p["key"], hits))
        for pat in (r"\bAtria\b", r"\bMimo\b", r"\bDeutsch\b", r"\bMarletto\b", r"\bPinker\b"):
            need(not re.search(pat, text), "part %s names %s" % (p["key"], pat))
        # every line given equals its line of the text
        for m in re.finditer(r"(?m)^L(\d+)\| (.*)$", text):
            need(TX[int(m.group(1)) - 1] == m.group(2), "part %s: line %s differs from the text" % (p["key"],
                                                                                                  m.group(1)))
        cap = CAP[p["model"]]
        need(len(text.split()) <= cap and wc_words(text) <= cap, "part %s is over %d words" % (p["key"], cap))
        fname = "S96 Cross-examination - repaired copy - part %s, %s.md" % (p["key"], p["title"])
        out[os.path.join(TESTS, fname)] = text
        rows.append((p, fname, text))
    names = [os.path.basename(k) for k in out]
    need(len(set(names)) == len(names), "two parts share a file name")
    jobs = []
    for p, fname, text in rows:
        ladder = [65536, 65536] if p["model"] == "atria" else [131072, 131072]
        jobs.append({
            "tag": "s96_xexam_%s_%s" % (p["model"], p["key"]),
            "provider": p["model"],
            "brief": os.path.join(TESTS, fname),
            "out": OUT_DIR,
            "effort": "medium",
            "ladder": ladder,
            "attempts": 6,
            "max_rejects": 3,
            "max_pass": 3,
            "note": "S96 cross-examination of the repaired copy, part %s (%s): lines %d-%d; read under '%s', "
                    "independently of every other reply" % (p["key"], p["title"], p["own"][0], p["own"][1],
                                                           READING_RULE)})
    tags = [j["tag"] for j in jobs]
    need(len(set(tags)) == len(tags), "two jobs share a tag")
    about = ("S96 cross-examination of the repaired copy (tests/Revision 2 - scrubbed copy, repaired (S96), theory "
             "text.md, md5 %s), 26 September 2026: the whole text in two halves to Atria (A, lines 1-372; B, lines "
             "373-632) and in four quarters to Mimo (1, lines 1-164; 2, 165-320; 3, 321-484; 4, 485-632), each part "
             "sent whole as the one user message at medium effort (decision S17), built by tools/s96_build.py. Up to "
             "three passes (max_pass 3), a later pass only for calls with no reply returned. Read under '%s'."
             % (SRC["text"][1], READING_RULE))
    out[JOBS] = json.dumps({"purpose": "audit", "about": about, "jobs": jobs}, indent=1, ensure_ascii=False) + "\n"
    return out, rows


def main():
    check = "--check" in sys.argv[1:]
    out, rows = build()
    bad = []
    for path, text in out.items():
        if os.path.exists(path):
            with open(path, encoding="utf-8") as f:
                if f.read() != text:
                    bad.append(path)
        elif check:
            bad.append(path)
    if check:
        print("check: %d files, %d differ or are missing%s" % (len(out), len(bad), (": " + "; ".join(
            os.path.basename(b) for b in bad)) if bad else ""))
        sys.exit(1 if bad else 0)
    need(not [b for b in bad if os.path.exists(b)], "refusing to overwrite files whose content differs: %s" % bad)
    for path, text in out.items():
        if not os.path.exists(path):
            with open(path, "w", encoding="utf-8") as f:
                f.write(text)
    print("| part | model | lines examined | file in `tests/` | words (runner / `wc -w`) | md5 |")
    print("|---|---|---|---|---|---|")
    for p, fname, text in rows:
        print("| %s | %s | %d–%d | `%s` | %d / %d | %s |" % (p["key"], p["model"], p["own"][0], p["own"][1], fname,
                                                          len(text.split()), wc_words(text), md5(text)))
    print("job list %s, sha256 %s" % (os.path.relpath(JOBS, SEM), hashlib.sha256(out[JOBS].encode()).hexdigest()))


if __name__ == "__main__":
    main()
