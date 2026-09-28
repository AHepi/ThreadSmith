#!/usr/bin/env python3
"""s105_build.py: build round 3 of the review rounds (decision S35; log S105): four GLM jobs at once (decision S39),
each a slightly different attack, in maths and code (decisions S36, S40), on the state after round 2. Written 28
September 2026 by a Claude subagent for the orchestrator, on the model of tools/s104_build.py.

  python3 Semantics/tools/s105_build.py --printouts   run the program three times (the whole suite, the external
                                                      examples, the creative transport case) on the merged model after
                                                      round 2 and write the printouts; about seven minutes
  python3 Semantics/tools/s105_build.py               build the reading copy of the text, the four briefs, the sandbox
                                                      manifest and the job list; refuses to write over a file whose
                                                      content differs; prints the table for the reading rule
  python3 Semantics/tools/s105_build.py --check       rebuild in memory and compare with the files; writes nothing

Each GLM call runs in a sandbox (tools/glm_via_claude_code_sandboxed.py) holding copies of the files the manifest names
(every source checked by md5 here and again at the copy) and its brief. The brief carries: what the round is; the
owner's words of decisions S20, S21, S23, S25 to S28, S33, S34, S36 and S40 (every quoted word unchanged; connecting
words that name internal records replaced by plain descriptions, REPLACE below; checked against the record); the map
of the sandbox and the tools; the held lines and the parked matters; the job; the form of every proposal (maths, code,
or one of the three permitted text changes: never new prose); the report form, ending END OF REPORT.
Checks before anything is written: every source's md5; the owner's words against the record; the frame of each brief
(everything but the owner's words) for the words decision S23 scrubs and words near them, the outside readers' and the
books' authors' names and internal record labels; each brief at most CAP words.
"""
import hashlib, json, os, re, subprocess, sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
SEM = os.path.dirname(HERE)
R2 = "results/S104 Round 2 - maths after the reading"
R2M = "results/S104 Round 2 - maths"
MODEL_DIR = R2 + "/model after round 2"
MAT = "results/S105 Round 3 - material for the readers"
READING_RULE = "results/S105 Round 3 - how the replies will be read, written before sending.md"
OUT = "results/S105 Round 3 - returns"
JOBS_FILE = "tools/s105_jobs - round 3, GLM.json"
MANIFEST = MAT + "/sandbox manifest.json"
BYLINE = MAT + "/the text after round 2, by line.md"
CAP = 7000
TEXT = ("tests/104 The semantics, standing alone, after round 2.md", "735ec1e8256cc6a251715a031944ea65")
DECISIONS = ("records/Semantics - Decisions.md", "55d30682530ac8e6fdc403ecf89ef92e")

# (path in the sandbox, source under Semantics/, md5): the round-3 material, as the orchestrator listed it, and the
# records it rests on (the earlier inventions, the external examples and the creative transport case).
SOURCES = [
    ("text/the text after round 2.md", TEXT[0], TEXT[1]),
    ("maths/formal core, after round 2.md", R2 + "/formal core, after round 2.md", "d8011c669603725937dc4cb36ff28177"),
    ("maths/formal claims, after round 2.md", R2 + "/formal claims, after round 2.md", "bbebe5497dbf3f98eb9a69eb4dc93699"),
    ("maths/formal claims, after round 2.json", R2 + "/formal claims, after round 2.json", "4638ded3c46b7c08f170f0d601f0b979"),
    ("maths/inventions I122-I164, added in round 2.md", R2 + "/inventions register - addendum after round 2.md",
     "00404849ca9b88cdd09934849445c724"),
    ("maths/owner questions after round 2.md", R2 + "/owner questions after round 2.md", "684cb7c378110a3a32723d17297807c3"),
    ("maths/parked after round 2.md", R2 + "/parked after round 2.md", "a62db83b8420c7e948ceaade2fadef98"),
    ("maths/inventions I01-I102.md", R2M + "/inventions register.md", None),
    ("maths/inventions I103-I108, external examples.md", R2M + "/inventions register - addendum for the external examples.md", None),
    ("maths/inventions I109-I121, creative transport case.md",
     R2M + "/inventions register - addendum for the creative transport case.md", None),
    ("maths/formal claims FC-E1 to FC-E5, external examples.md",
     R2M + "/formal claims - addendum for the external examples.md", None),
    ("round 2/the second checker on the critical review.md",
     "results/S104 Round 2 - the second checker on the critical review.md", None),
    ("round 2/critical review.md", "results/S104 Round 2 - critical review of the round.md", None),
    ("round 2/the orchestrator's decisions on the critical review.md",
     "results/S104 Round 2 - the orchestrator's decisions on the critical review.md", None),
    ("round 2/integration report.md", R2 + "/integration report.md", "29c8cd6018e397a21bc1f183a7b62730"),
    ("round 2/area 1 - verdicts and formal fixes.md", R2 + "/area 1 - verdicts and formal fixes.md",
     "8e46209f78c7e0930d3e2ca965173c35"),
    ("round 2/area 2 - verdicts and formal fixes.md", R2 + "/area 2 - verdicts and formal fixes.md",
     "207ec5996c6b7bc0bddbf54e38aaf014"),
    ("round 2/area 3 - verdicts and formal fixes.md", R2 + "/area 3 - verdicts and formal fixes.md",
     "ad63a42c6ab67684b4eae6d6261fac11"),
    ("round 2/text changes applied in round 2.json", R2 + "/text changes after the review.json",
     "3f43745f9da7680eb85f60cef8b38172"),
    ("cases/creative transport case card.md", "results/S104 Round 2 - case card, the creative transport experiment.md", None),
    ("cases/code of the external examples (read only).py", MODEL_DIR + "/s104_external.py", None),
    ("cases/code of the creative transport case (read only).py", MODEL_DIR + "/s104_creative_transport.py",
     "cdde2bf3c1270d185463a12a673d36e5"),
]
MODEL_FILES = ["__init__.py", "args.py", "cases.py", "claims_a.py", "claims_area1.py", "claims_b.py", "core.py", "gen.py",
               "harness.py", "inventions_model.py", "phys.py", "register.py", "report.py", "run.py"]
MODEL_MD5 = {"claims_a.py": "62bb05be912fafed7b66659006c6f971", "claims_b.py": "f788408a75b40553fe83d839ee371efe",
             "claims_area1.py": "c02c209514787cae74eadf08377be3e0", "args.py": "10fff81e8bb77a114566275d7a95deda",
             "inventions_model.py": "dba0c346a84ed4f1996f17026d288f5a"}
PRINTOUTS = [
    ("program printouts/whole suite after round 2, scale 4, time cap 45.txt", MAT + "/printout - whole suite after round 2.txt",
     ["-B", "-m", "model.run", "--scale", "4", "--time-cap", "45", "--no-write"], 2400),
    ("program printouts/external examples FC-E1 to FC-E5 after round 2.txt",
     MAT + "/printout - external examples after round 2.txt", ["-B", "s104_external.py"], 900),
    ("program printouts/creative transport case CT1 to CT8 after round 2.txt",
     MAT + "/printout - creative transport case after round 2.txt", ["-B", "s104_creative_transport.py"], 900),
]


def path(rel):
    return os.path.join(SEM, rel)


def read(rel):
    with open(path(rel), encoding="utf-8") as f:
        return f.read()


def md5_file(rel):
    with open(path(rel), "rb") as f:
        return hashlib.md5(f.read()).hexdigest()


def md5(s):
    return hashlib.md5(s.encode("utf-8")).hexdigest()


def need(ok, msg):
    if not ok:
        raise SystemExit("refused: " + msg)


def words(s):
    return len(s.split())


# ------------------------------------------------------------------ the printouts (--printouts)
def printouts():
    for _, rel, args, limit in PRINTOUTS:
        print("running", " ".join(args), flush=True)
        env = {"PATH": "/usr/local/bin:/usr/bin:/bin", "LANG": "C.UTF-8", "PYTHONHASHSEED": "0",
               "PYTHONDONTWRITEBYTECODE": "1"}
        r = subprocess.run([sys.executable] + args, cwd=path(MODEL_DIR), env=env, capture_output=True, text=True,
                           timeout=limit)
        need(r.returncode == 0, "%s ended with exit %d: %s" % (args, r.returncode, r.stderr[-500:]))
        text = ("# command, from `%s`: PYTHONHASHSEED=0 python3 %s\n# exit 0\n\n" % (MODEL_DIR, " ".join(args))
                + r.stdout)
        write_checked(rel, text)


# ------------------------------------------------------------------ the text by line
CHANGED = {109, 119, 127, 141, 151, 195, 199, 257, 265, 269, 273, 313, 315, 317, 325, 375, 393, 395, 441, 453, 471,
           520, 526, 528, 556, 558, 574, 584, 590, 626, 628, 630}


def by_line(text):
    lines = text.split("\n")
    if lines and lines[-1] == "":
        lines = lines[:-1]
    out = ["# The text after round 2, by line",
           "",
           "A reading copy of text/the text after round 2.md (md5 %s), made so that no line is longer than 1,500 "
           "characters. Each line of the text is given as `L<n> | <line>`; a line longer than 1,500 characters is cut "
           "at a space into pieces, the second and later written `L<n> (cont.) | <piece>`. A star, `L<n>* |`, marks "
           "the 32 lines round 2 changed. Empty lines are given as `L<n> |`. Nothing else differs from the text."
           % TEXT[1], ""]
    for n, l in enumerate(lines, 1):
        star = "*" if n in CHANGED else ""
        pieces, rest = [], l
        while len(rest) > 1500:
            cut = rest.rfind(" ", 0, 1500)
            cut = cut if cut > 0 else 1500
            pieces.append(rest[:cut])
            rest = rest[cut:].lstrip(" ")
        pieces.append(rest)
        out.append(("L%d%s | %s" % (n, star, pieces[0])).rstrip())
        out += ["L%d (cont.) | %s" % (n, p) for p in pieces[1:]]
    return "\n".join(out) + "\n", len(lines)


# ------------------------------------------------------------------ the owner's words
KEEP = [20, 21, 23, 25, 26, 27, 28, 33, 34, 36, 40]
REPLACE = [
    (21, "Answering file 93's choices (log S93): ", "Answering choices the drafters had put to the owner: "),
    (23, "Next step after log S94, in three paragraphs: ", "Next step, in three paragraphs: "),
    (25, "Claude's report that draft 5 ties", "Claude's report that an earlier draft ties"),
    (25, " (log S95): ", ": "),
    (26, " (log S95): ", ": "),
    (33, "After reading log S101 (file 101, what the tested strong candidates depend on), in three paragraphs: ",
     "After reading a study of what seven sentences of the text depend on, in three paragraphs: "),
    (34, "Then, after log S102 (file 102, every way hard to vary has been defined and used), in two paragraphs: ",
     "Then, after reading a summary of every way hard to vary had been defined and used, in two paragraphs: "),
    (36, "During the reading of round 1 (log S103): ", "During the reading of the first review round: "),
    (40, "During the round-2 checking (log S104), ", "During the checking of the second review round, "),
]
DATES = {20: "24 and 25 September 2026", 21: "25 September 2026", 23: "25 September 2026", 25: "26 September 2026",
         26: "26 September 2026", 27: "26 September 2026", 28: "26 September 2026", 33: "27 September 2026",
         34: "27 September 2026", 36: "27 September 2026", 40: "28 September 2026"}


def owner_words(dec):
    own = {}
    for n in KEEP:
        m = re.search(r"(?m)^S%d\. \[Claude's reading: .*?\] (.*)$" % n, dec)
        need(m, "decision S%d not found" % n)
        own[n] = m.group(1)
    text = dict(own)
    for n, old, new in REPLACE:
        s = text[n]
        need(s.count(old) == 1, "S%d: %r occurs %d times" % (n, old, s.count(old)))
        i = s.index(old)
        need(s[:i].count('"') % 2 == 0 and s[i + len(old):].count('"') % 2 == 0,
             "S%d: %r lies inside a quotation" % (n, old))
        text[n] = s.replace(old, new)
    for n in own:
        b = text[n]
        for _, old, new in [r for r in REPLACE if r[0] == n]:
            b = b.replace(new, old, 1)
        need(own[n] == b, "S%d: the owner's words changed" % n)
        need(not re.search(r"\blog S\d|\bfile \d{2,3}\b|\bdraft \d|round-2|round 1\b", text[n]),
             "S%d still names an internal record" % n)
    need("if implementation forces invention, that needs to be recorded." in own[36], "S36 is not whole")
    need("more prose is self defeating" in own[40] and "This only needs maybe 3 checkers." in own[40], "S40 is not whole")
    body = ["## 2. The owner's words",
            "The theory's owner took the decisions below, in this order; they bind every finding and every proposal. "
            "Each is quoted from the project's record of decisions. Words inside quotation marks are the owner's, "
            "word for word, typos included, except where the connecting words say that a quoted phrase is Claude's (in "
            "S26 and S28). The few connecting words outside the quotation marks are the recorder's; where the record "
            "names internal files or logs there, a plain description stands in their place. Where this brief is "
            "worded differently from the owner's words, the owner's words decide, and you should say so. In these "
            "words \"Claude\" is the drafters of the text and of the maths; \"your agents\" and \"your explanation\" in "
            "S27 are addressed to them."]
    for n in KEEP:
        body.append("**S%d** (%s). %s" % (n, DATES[n], text[n]))
        if n == 26:
            body.append("*What S27 answers.* Between S26 and S27 the drafters gave the owner the five examples asked "
                        "for: holding an explanation in a carrier (ink, a brain, a file); copying or teaching it; "
                        "testing between two rival explanations, where the test changes the thing explained; building "
                        "from an explanation (a perpetual-motion machine, a bridge); and performing music. The examples "
                        "are the drafters' words, not the owner's, and are not a decision. S27 is the owner's reply to "
                        "them.")
    return "\n\n".join(body), own


# ------------------------------------------------------------------ the briefs
JOBS = [
    (1, "breaker", "the breaker", "s105_glm_breaker"),
    (2, "maths_words", "the maths against the words", "s105_glm_maths_words"),
    (3, "structure", "the structure of the formal core", "s105_glm_structure"),
    (4, "cases", "the cases", "s105_glm_cases"),
]
BRIEF_PATH = {n: "tests/S105 Round 3 - GLM job %d, %s.md" % (n, title) for n, _, title, _ in JOBS}

INTRO = """# Round 3 of the review of a semantics: job {n} of 4, {title}

## 1. What this is

You are one of four readers working at the same time on the same material, each with a slightly different job. Yours is section 5. You work in a folder, the sandbox, that holds copies of the material; section 3 maps it and says what your tools can do.

A theory, called here the semantics, is stated in a prose text (`text/the text after round 2.md`, 632 lines, cited as L1 to L632). A formal core writes its sentences as definitions (D§.n, with the sentence each formalizes quoted above it) and as encodings of the text's worked cases (E1 to E9). Formal claims (FCnn) state consequences, and a program in `model/` searches small models for counterexamples to them: a claim either holds on every model tried, has a counterexample, or was not tested. Two review rounds have been read. The second one changed the maths (new and changed definitions and claims) and changed 32 lines of the text, each change of one of three kinds only: a span deleted, a span replaced by its formal statement, or a span replaced by a pointer to a definition or claim. Your job is to attack the state after that round, in maths and code, and find where it fails. The maths is a conjecture, and so is the text.

Where the maths had to choose something the text leaves open, the choice is recorded as an invention (Inn), with the other choices it could have made. Nothing invented is the text's own content. A counterexample that rests on an invention tells against the text only where the text fixes what the invention fills in; otherwise it tells against that way of writing the text, and you should say which.

Who is who: "the owner" is the person whose theory this is; "Claude" is the drafters of the text and of the maths, and the checkers who ruled on the earlier rounds. The records of the second round name the outside readers and the reviewers of that round; who made a point decides nothing, only its reasons do."""

SANDBOX = """## 3. The sandbox and your tools

| file or folder | what it is |
|---|---|
| `text/the text after round 2.md` | the text, exactly as it stands |
| `text/the text after round 2, by line.md` | the same text, one line per text line as `L<n> \\| ...`, long lines cut into pieces of at most 1,500 characters; a star marks the 32 lines round 2 changed. Read the text here: the Read tool cuts lines longer than 2,000 characters |
| `maths/formal core, after round 2.md` | the definitions D0.1 to D18.x and the encodings E1 to E9, each with the sentences it formalizes |
| `maths/formal claims, after round 2.md` and `.json` | the claims and their results after round 2: 103 hold on every model tried, 3 have a counterexample (FC18, FC23, FC63), 7 were not tested, of 113 |
| `maths/inventions I122-I164, added in round 2.md` | the inventions round 2 added, among them I161, I162, I163, I164; and the earlier inventions it fixed or amended |
| `maths/inventions I01-I102.md`, `... I103-I108, external examples.md`, `... I109-I121, creative transport case.md` | the earlier inventions |
| `maths/formal claims FC-E1 to FC-E5, external examples.md` | five claims from an outside cross-examination, with the models the program built for them |
| `maths/owner questions after round 2.md` | the questions left to the owner (section A) and those ruled on argument (section B) |
| `maths/parked after round 2.md` | points parked (section 4) |
| `round 2/the second checker on the critical review.md` | the last ruling of round 2: what was changed at the end and why, with the strict count of its changes (its section 5 lists every definition and claim round 2 changed) |
| `round 2/critical review.md`, `round 2/the orchestrator's decisions on the critical review.md` | the objections of the review of round 2 and what was done with them |
| `round 2/integration report.md`, `round 2/area 1 - verdicts and formal fixes.md` (and areas 2, 3) | how the three checkers of round 2 ruled, each fix in maths and code, and how the fixes were merged |
| `round 2/text changes applied in round 2.json` | the 43 changes applied to the text on its 32 lines: for each, the line, the kind, the old span, the new span, what it settles and the items behind it |
| `cases/creative transport case card.md`; `cases/code of ... (read only).py` | a worked case supplied by the owner, and the code that reads it and the external examples on the model (you can read it; it does not run here) |
| `program printouts/` | the program's printouts after round 2: the whole suite at scale 4 (every claim, in full), the external examples FC-E1 to FC-E5, and the creative transport case CT1 to CT8 |
| `model/` | the program, standard-library Python: `core.py` (organizations, questions, candidates, the account), `claims_a.py`, `claims_b.py`, `claims_area1.py` (one function per claim), `args.py`, `phys.py`, `gen.py` (the model generators), `inventions_model.py` |
| `BRIEF.md` | this brief |

Your tools. **Read** (read a long file in pieces with offset and limit), **Glob** and **Grep**, inside this folder only. **Bash** runs one command only, typed plainly from this folder: `python3 -m model.run` with `--claim FCnn` (repeatable, for example `--claim FC12.new1 --claim FC83`), `--scale N` (at most 4), `--time-cap N` (at most 60), `--brief`, `--help`. Anything else is refused, and nothing can be written. One claim at the default scale takes seconds; the whole suite takes several minutes (give the Bash tool a timeout of 600000 for it), and its printout at scale 4 is already in `program printouts/`. You cannot change the program or run new code: a new definition, a changed claim or a new small model goes into your report as Python in the program's own notation (as in `model/core.py` and `model/claims_b.py`), with the output you expect, marked "not run"; the next step of the round will run it. Work economically: read what your job needs, search with Grep, run a claim where its result bears on your point.

**Only your final message is kept.** Write the whole report in your last message, after your last tool call."""

HELD = """## 4. Held lines, parked matters, values

- **Held lines: the owner's four open questions.** Q2, Q6 and Q15 are the owner's (`maths/owner questions after round 2.md`, section A); Q23 (is a bare premise an argument) was ruled in section B of that file and now goes back to the owner. The lines they concern are held: **L17 and L536** (Q2: is meeting (E) enough to count as an explanation, or only with a transport whose provenance is not declared); **L55, and "episode" at L197, L405 and L429** (Q6: an episode as any delimited subhistory, or as a history in which contracts change); **L255's non-circular dependence clause, with D6.4 and I22** (Q15: a contrast when the baseline answer is not determined); **L397, with I88** (Q23). You may comment on them and show what the maths does there; a proposal on a held line, or on the matter of its question in the maths, is recorded for the owner and not applied. Say which side of the question each such finding bears on.
- **Parked.** What hard to vary covers is parked (S33, S34; `maths/parked after round 2.md`, P1 to P7). Do not argue it.
- **Values.** Where values are placed is the owner's question. Propose nothing that moves them."""

FORM = """## 6. The form of every proposal (decision S40)

Every proposal is exactly one of:
1. **maths**: a changed or new definition or claim, in the formal core's notation, written beside the one it replaces, with its id;
2. **code**: a change to the program or a new small model, as Python in the program's notation, with the output you expect, and "run" (with the command and the program's result line) or "not run";
3. **a text change of one of three kinds**: delete a span; replace a span by its formal statement; replace a span by a pointer to a definition or claim. Give the line, the exact old span and the exact new span.

Never new prose: no added sentence, no reworded sentence, no gloss. A proposal that adds prose is not taken.

The owner's words bind every proposal and every name in it. Do not list, count, grade or rank rivals, and do not argue from how many (S20). Nothing about what must happen to a candidate (S21). Every word S23 forbids stays out of every name, gloss and proposal; "argument" is reasons why this and not that, and every accepting is tentative (S23). Physical possibility only where information or knowledge is instantiated or transformed, and as the content of claims a candidate can conflict with (S25 to S27). Nothing is settled, and a ruling out by a claim taken as given is a choice (S28). Nothing about what hard to vary covers (S33, S34). Every choice you make that the text leaves open is named as an invention, with the other choices (S36)."""

REPORT = """## 7. The report

Terse: tables, formulas, small models in the program's format, one-line reasons. No summary of the material. For each finding: an id (B1, B2, ... for job 1; W1, ... for job 2; S1, ... for job 3; K1, ... for job 4), the item or items and the line or lines, what fails in one line, the model or computation (and whether you ran it: the command and the program's result line), the proposal in one of the forms of section 6, and the inventions it rests on, if any. Items you examined and found nothing against are named together in one line at the end of each section. At most about 3,000 words.

Sections, in this order:
{sections}

Write the whole report as your final message. Its last line must be exactly:

END OF REPORT"""

JOB_TEXT = {
    1: ("the breaker", """## 5. Your job: the breaker

Try to break round 2's changes. For each definition and claim round 2 changed or added (the list is section 5 of `round 2/the second checker on the critical review.md`, "Moves (strict)"; the definitions are in `maths/formal core, after round 2.md`), look for a small model:
- where the definition or claim fails;
- where it contradicts another definition of the core;
- where it changes the result of a worked case the text fixes (E1 to E9; the cases the text works through, among them the pole and its shadow, the table of observed answers, the occlusion case at L626 to L630).

Put the most pressure on the three inventions the last ruling of round 2 added:
- **I161**: Sel(t) excludes a construction trace in t's history that prepares t (D12.1, D12.3; the change T9 at L195; claims FC12.new1 and FC83). Is Sel ∧ Con now excluded under every cut, as claimed? Does I161 exclude a selection the text counts as one (L195, L201, L211, L411)? Does "a construction trace prepares t" have one reading, or several that give different answers?
- **I162**: the cut T′ of the loop in "represented" (Held in Con, D12.2, and in Build, D13.3; Sel's exclusion by Rep at o ≺_h o_t, a recursion along ≺_h; D18.1; FC98 (a′) to (e)). Is the recursion well founded on every history the core admits (a history with no least occurrence below o_t, occurrences not ordered by ≺_h, a first construction)? Does T′ give exactly one of the three provenances (L193) on every history? Build the smallest history on which T′ and the text part ways.
- **I163**: identification by a varying observed value (D3.3: Ident :⟺ the query returns a fibre ∧ ∃(a,b),(a′,b′) ∈ C: obs(a,b) ≠ obs(a′,b′); FC28 (R4); L151 and L325). Does it now admit a question the text would not call an identification question, or exclude one it would (the pole at L325, E1, E2)? What if obs varies only across boundaries, or only through an edit that also alters what is identified?

For each: (i) what exactly the definition says, in one line; (ii) the smallest model that breaks it, or makes it disagree with a line of the text or another definition, in the program's format; (iii) the program's check where one exists (run the claim); (iv) a fix, in one of the forms of section 6.""",
     """(a) I161; (b) I162; (c) I163; (d) the other definitions and claims round 2 changed or added; (e) what held under attack, one line each."""),
    2: ("the maths against the words", """## 5. Your job: the maths against the words

Where a formula or a pointer replaced words in the text, and wherever a definition formalizes a sentence, does the maths say what the sentence needs, no more and no less?

1. **The 43 text changes of round 2** (`round 2/text changes applied in round 2.json`; the lines are starred in the reading copy of the text). For each change of kind "formal" or "pointer": compare the old span with the new span, and with the definition or claim the new span points to. Verdict: **same** (the formula says what the words said), **more** (what it adds), **less** (what it drops), or **other** (where it differs). For every verdict but "same", give a witness: the smallest case on which the words and the formula give different answers. For each change of kind "delete": does anything the rest of the text or the maths uses go with it?
2. **The definitions round 2 changed or added** (section 5 of `round 2/the second checker on the critical review.md`), each against the sentences quoted above it in the formal core: same, more, less, or other, with a witness.
3. **Any other definition** you meet where the formula and its quoted sentence part ways in a way that changes a claim's result.

Say for each gap which should stand, the maths or the words, and why, in one line; where the words should stand, the fix is to the maths; where the maths should stand, the fix is a text change of one of the three kinds. Where the gap rests on an invention the text leaves open, name it: the text need not settle it.""",
     """(a) the 43 text changes, one table: change id, line, kind, verdict, witness, proposal; (b) the definitions round 2 changed or added, one table; (c) other definitions; (d) the proposals, each in its form."""),
    3: ("the structure of the formal core", """## 5. Your job: the structure of the formal core

Read the formal core after round 2 as one system of definitions and look for:
1. **Circular definitions.** Draw the dependence of the definitions (which definition uses which) and give every cycle. For the loop in "represented" as now cut (I162: Held in Con, D12.2, and in Build, D13.3; Sel's exclusion by Rep at o ≺_h o_t, a recursion along ≺_h; D18.1 and L526): is it a cycle, a well-founded recursion, or neither, on every history the core admits? Is D18.1's one dependence order (L526) the order the definitions actually have?
2. **Primitives left undefined.** Every symbol used and never defined. For each, whether the text lists it among what is "stated, not defined" (L526; D0.2 classes the primitives), or reads it through Θ or a declared input.
3. **Definitions no claim uses.** For each definition, whether any claim's statement or the program uses it (search `maths/formal claims, after round 2.md` and `model/`). An unused definition is not thereby idle: say whether the text needs it.
4. **Two definitions that conflict.** A model on which one definition says something the other says cannot hold, or two definitions of one term.
5. **Notation used two ways.** A symbol, letter or name with two meanings (for example δ as a designation and as a defect; C as a contract and as a set of pairs; Rep, Held and "represented"; Pred and Ans; primes on changed definitions).

For each finding, the smallest witness (a chain of definitions, a model, or two quoted uses) and a fix in one of the forms of section 6.""",
     """(a) cycles and the cut loop, with the dependence table; (b) undefined primitives, one table: symbol, where used, listed by the text or not; (c) definitions no claim uses; (d) conflicts; (e) notation used two ways; (f) the proposals, each in its form."""),
    4: ("the cases", """## 5. Your job: the cases

Run the cases through the maths after round 2, by hand or by the program, and say whether their results move.

1. **The text's worked cases**: the encodings E1 to E9 of the formal core (the pole and its shadow, identification, the two balances, obstruction, explanation that removes structure, odd-order skew-symmetric matrices, the transport results, a contract as an organization, the two-layer episode) and the cases the text works through in its lines (among them the table of observed answers, the reversed calculation, the swap and the occlusion case at L626 to L630). For each: what the text says the result is, what the maths after round 2 gives, and whether round 2's changes moved it.
2. **The external examples FC-E1 to FC-E5** (`maths/formal claims FC-E1 to FC-E5, external examples.md`; after round 2: `program printouts/external examples ...`). For each: the result before round 2, after round 2, and whether it moved; if it moved, which change moved it.
3. **The creative transport case, CT1 to CT8, CT8 above all** (`cases/creative transport case card.md`; after round 2: `program printouts/creative transport case ...`). Round 2 moved one reading of CT8 from "selected" to "neither". Does the move follow from the maths as changed (I161, I162), and does it match what the text says of such a history (L193 to L211, L405, L411)? Under the cut T′, would a pair in CT8 count as constructed?
4. **New small cases, at most six**, each built to probe one of round 2's new cuts and inventions: I161, I162, I163, the one edge set of D18.1, D15.2 per execution, Forms_cl in D9.1 and D9.7. Each as a small model in the program's format, with the result you expect under the maths after round 2 and under the text's words, and whether the two agree.

Where a result moves, say which change moved it and whether the move matches the text; where the maths and the text part ways, the fix goes in one of the forms of section 6.""",
     """(a) the worked cases, one table: case, lines, the text's result, the result after round 2, moved or not, why; (b) FC-E1 to FC-E5, one table; (c) CT1 to CT8, one table, then CT8 in full; (d) the new cases; (e) the proposals, each in its form."""),
}

SCRUB = [r"\bfits?\b", r"\bfitt\w*", r"\bsupport\w*", r"\bverif\w*", r"\bcorroborat\w*", r"\bprov(e|es|ed|en|ing)\b",
         r"\bdisprov\w*", r"\bbelie\w*", r"better than", r"worse than", r"\btrue\b", r"\btruth\w*", r"\bfalse\b",
         r"\bestablish\w*", r"\bauthorit\w*", r"\bfoundation\w*", r"\bderiv\w*", r"\bjustif\w*", r"\brank\w*",
         r"\bvalid\w*", r"\bcorrect(ly|ness)?\b", r"\bevidence\b", r"\bconfirm\w*", r"\bcertain\w*",
         r"\bgrade[sd]?\b", r"\bwrong\b", r"\bprefer\w*",
         r"\bAtria\b", r"\bMimo\b", r"\bGLM\b", r"\bFable\b", r"\bOpus\b", r"\bDeutsch\b", r"\bMarletto\b",
         r"\bPinker\b", r"\blog S\d", r"\bS(?:9\d|1\d\d)\b", r"\bCONFIRMED\b"]
ALLOWED_IN_FRAME = ["Do not list, count, grade or rank rivals"]
DECISIONS_NAMED = set(KEEP)


def frame_of(text):
    f = re.sub(r"(?s)## 2\. The owner's words.*?(?=## 3\. The sandbox)", "", text)
    for s in ALLOWED_IN_FRAME:
        f = f.replace(s, "")
    return f


def scan(text):
    f = frame_of(text)
    hits = sorted({m.group(0) for pat in SCRUB for m in re.finditer(pat, f, re.I)})
    for m in re.finditer(r"\bS(\d\d)\b", f):
        if int(m.group(1)) not in DECISIONS_NAMED:
            hits.append(m.group(0))
    return hits


def build_brief(n, title, owner):
    job_title, job, sections = JOB_TEXT[n]
    parts = [INTRO.format(n=n, title=title), owner, SANDBOX, HELD, job, FORM, REPORT.format(sections=sections)]
    return "\n\n".join(parts) + "\n"


# ------------------------------------------------------------------ the build
def check_sources():
    for dst, src, want in SOURCES:
        need(os.path.isfile(path(src)), "%s is not there" % src)
        if want:
            need(md5_file(src) == want, "%s has md5 %s, expected %s" % (src, md5_file(src), want))
    for f in MODEL_FILES:
        rel = MODEL_DIR + "/model/" + f
        need(os.path.isfile(path(rel)), "%s is not there" % rel)
        if f in MODEL_MD5:
            need(md5_file(rel) == MODEL_MD5[f], "%s has md5 %s, expected %s" % (rel, md5_file(rel), MODEL_MD5[f]))
    need(md5_file(TEXT[0]) == TEXT[1], "the text has md5 %s, expected %s" % (md5_file(TEXT[0]), TEXT[1]))
    need(md5_file(DECISIONS[0]) == DECISIONS[1], "the decisions record has md5 %s, expected %s"
         % (md5_file(DECISIONS[0]), DECISIONS[1]))
    for _, rel, _, _ in PRINTOUTS:
        need(os.path.isfile(path(rel)), "%s is not there: run --printouts first" % rel)


def build():
    check_sources()
    files = {}
    bl, nlines = by_line(read(TEXT[0]))
    need(nlines == 632, "the text has %d lines, expected 632" % nlines)
    files[BYLINE] = bl
    owner, own = owner_words(read(DECISIONS[0]))
    rows = []
    for n, name, title, tag in JOBS:
        b = build_brief(n, title, owner)
        hits = scan(b)
        need(not hits, "brief %d: the frame holds %s" % (n, hits))
        need(words(b) <= CAP, "brief %d has %d words, above %d" % (n, words(b), CAP))
        for k in KEEP:
            need(own[k].split('"')[1] in b, "brief %d lacks the owner's words of S%d" % (n, k))
        files[BRIEF_PATH[n]] = b
        rows.append((n, name, title, tag, BRIEF_PATH[n], words(b), md5(b)))
    entries = [{"path": dst, "src": src, "md5": md5_file(src)} for dst, src, _ in SOURCES]
    entries.append({"path": "text/the text after round 2, by line.md", "src": BYLINE, "md5": md5(bl)})
    entries += [{"path": dst, "src": rel, "md5": md5_file(rel)} for dst, rel, _, _ in PRINTOUTS]
    entries += [{"path": "model/" + f, "src": MODEL_DIR + "/model/" + f, "md5": md5_file(MODEL_DIR + "/model/" + f)}
                for f in MODEL_FILES]
    manifest = {"note": "round 3 (log S105): the files copied into each GLM call's sandbox, each checked by md5 at the "
                        "copy; the brief is added as BRIEF.md. Written by tools/s105_build.py.",
                "printout_commands": {dst: "PYTHONHASHSEED=0 python3 " + " ".join(a) + "  (from " + MODEL_DIR + ")"
                                      for dst, _, a, _ in PRINTOUTS},
                "files": entries}
    files[MANIFEST] = json.dumps(manifest, indent=1, ensure_ascii=False) + "\n"
    jobs = {"round": "round 3 of the review rounds (log S105)", "rule": READING_RULE, "out": OUT, "max_pass": 3,
            "effort": "medium", "context_1m": True, "attempts": 6, "max_rejects": 3, "deadline": 7200,
            "manifest": MANIFEST, "manifest_md5": md5(files[MANIFEST]),
            "sandbox_root": "s105_sandboxes", "home_root": "s105_homes",
            "helper": "tools/glm_via_claude_code_sandboxed.py",
            "jobs": [{"job": n, "name": name, "tag": tag, "brief": BRIEF_PATH[n], "brief_md5": h}
                     for n, name, title, tag, _, w, h in rows]}
    files[JOBS_FILE] = json.dumps(jobs, indent=1, ensure_ascii=False) + "\n"
    return files, rows, manifest


def write_checked(rel, text):
    p = path(rel)
    if os.path.exists(p):
        with open(p, encoding="utf-8") as f:
            old = f.read()
        need(old == text, "%s exists with other content; nothing overwritten" % rel)
        return False
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "x", encoding="utf-8") as f:
        f.write(text)
    return True


def main():
    a = sys.argv[1:]
    need(set(a) <= {"--check", "--printouts"}, "usage: s105_build.py [--printouts | --check]")
    if "--printouts" in a:
        printouts()
        return
    files, rows, manifest = build()
    if "--check" in a:
        for rel, text in files.items():
            need(os.path.exists(path(rel)) and read(rel) == text, "%s differs from the build" % rel)
        print("check: all %d files identical to the build" % len(files))
    else:
        for rel, text in files.items():
            print(("wrote   " if write_checked(rel, text) else "same    ") + rel)
    print("\n| job | name | tag | brief | words (wc) | md5 |\n|---|---|---|---|---|---|")
    for n, name, title, tag, rel, w, h in rows:
        print("| %d | %s | %s | `%s` | %d | %s |" % (n, title, tag, rel, w, h))
    print("\nsandbox: %d files from the manifest + BRIEF.md; manifest md5 %s" % (len(manifest["files"]),
                                                                            md5(files[MANIFEST])))


if __name__ == "__main__":
    main()
