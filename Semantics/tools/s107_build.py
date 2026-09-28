#!/usr/bin/env python3
"""s107_build.py: build round 4 of the review rounds (decision S35; log S107): four GLM jobs at once (decision S39),
each a slightly different attack, in maths and code (decisions S36, S40), on the state after step S106 (the written-in
test taken out of what makes something an explanation, decisions S44 and S45; "and criticism" put back into the
opening and the bridge re-encoded, decision S47). Written 28 September 2026 by a Claude subagent (Opus 5.5) for the
orchestrator, on the model of tools/s105_build.py (round 3's build), whose parts it keeps.

  python3 Semantics/tools/s107_build.py --printouts   run the program three times (the whole suite, the external
                                                      examples, the creative transport case) on the model after S106
                                                      and write the printouts; about ten minutes
  python3 Semantics/tools/s107_build.py               build the reading copy of the text, the four briefs, the sandbox
                                                      manifest and the job list; refuses to write over a file whose
                                                      content differs; prints the table for the reading rule
  python3 Semantics/tools/s107_build.py --check       rebuild in memory and compare with the files; writes nothing

What differs from round 3's build:
- the material: the text after S106 (tests/106), the maths after S106, the records of S106 (report, critical review,
  the orchestrator's decisions, the second checker) and of round 3 (moves, integration, areas 1 and 3, critical review,
  the orchestrator's decisions, the second checker, the text changes); the text as round 3 left it (tests/105) and as
  round 3 found it (tests/104 with the owner's answers), for comparison;
- two files of round 3 are left out of the sandbox because they use the word "model" for a candidate explanation
  (decision S43; lesson S42): `S105 Round 3 - area 2 - verdicts and formal fixes.md` (its L72) and `owner questions
  after round 3.md` (its L7). Area 2 made no move; its one finding that held became the owner question R3-Q1, which
  decisions S44 and S45 answered. Every file of the sandbox is scanned for that use (MODEL_FOR_CANDIDATE) and the build
  refuses on a hit;
- the reading copy marks the lines round 3 changed (*) and the lines S106 changed (+);
- the owner's words add S43, S44, S45 and S47; the connecting words of S43, S44 and S47 that quote Claude's question
  with the word "model", or name an internal file, are replaced by plain descriptions, checked against the record;
- each brief says what "model" means in it (only a small structure the program builds, or the program's folder), and
  the frame is scanned for "model" used for a candidate as well as for the words decision S23 scrubs;
- the jobs point at what changed since round 3 (the orchestrator's brief for log S107).
Checks before anything is written: every source committed and unchanged from HEAD, with the md5s pinned below; the
owner's words against the record; the frame of each brief (everything but the owner's words); each brief at most CAP
words; round 3's 9 changed lines; the counts of S106's changed lines against its record.
"""
import hashlib, json, os, re, subprocess, sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
SEM = os.path.dirname(HERE)
REPO = os.path.dirname(SEM)
STEP = "results/S106 The written-in test taken out"
R3 = "results/S105 Round 3 - maths after the reading"
R3R = "results/S105 Round 3 - "
R2 = "results/S104 Round 2 - maths after the reading"
R2M = "results/S104 Round 2 - maths"
MODEL_DIR = STEP + "/model after S106"
MAT = "results/S107 Round 4 - material for the readers"
READING_RULE = "results/S107 Round 4 - how the replies will be read, written before sending.md"
OUT = "results/S107 Round 4 - returns"
JOBS_FILE = "tools/s107_jobs - round 4, GLM.json"
MANIFEST = MAT + "/sandbox manifest.json"
BYLINE = MAT + "/the text under review, by line.md"
CAP = 7000
# The text under review: the text after S106, rebuilt by S106's second checker (b73d9bf); its md5 is the one that
# file gives. The text as round 3 left it, and as round 3 found it, are given for comparison.
TEXT = ("tests/106 The semantics, standing alone, without the written-in test.md", "c7af964c329ab7959243405d394e6574")
TEXT_R3 = ("tests/105 The semantics, standing alone, after round 3.md", "da9a30cd052d46f2a5ead259cea97d3c")
TEXT_R2A = ("tests/104 The semantics, standing alone, after round 2, with the owner's answers.md",
            "bc14045aae3139df710d8339a9c1c81b")
DECISIONS = ("records/Semantics - Decisions.md", None)
R3_LINES = [13, 49, 61, 69, 201, 220, 375, 397, 405]                    # round 3's 13 changes on 9 lines
STEP_LINES = [13, 255, 257, 262, 273, 275, 317, 343, 397, 520, 536]     # S106's 13 and S47's 1, on 11 lines

# (path in the sandbox, source under Semantics/, md5). The md5s are those the second checker of S106 gives for its
# files (b73d9bf), and those of round 3's second checker and the earlier records for theirs.
SOURCES = [
    ("text/the text under review.md", TEXT[0], TEXT[1]),
    ("text/the text after round 3, before the step.md", TEXT_R3[0], TEXT_R3[1]),
    ("text/the text before round 3.md", TEXT_R2A[0], TEXT_R2A[1]),
    ("maths/formal core, now.md", STEP + "/formal core, after S106.md", "40d7c80ec78574794962fece34a4cb51"),
    ("maths/formal claims, now.md", STEP + "/formal claims, after S106.md", "c0884083daae9b95be0c36d111d71019"),
    ("maths/formal claims, now.json", STEP + "/formal claims, after S106.json", "e02291ba44e78e56a44a23cb626a703b"),
    ("maths/inventions I184 onwards, added in the step.md", STEP + "/inventions register - addendum after S106.md",
     "4c19472b4f097fc5698e8e4722017100"),
    ("maths/owner questions, now.md", STEP + "/owner questions after S106.md", "6658823bd9d055b25af4412eb4bf1197"),
    ("maths/parked, now.md", STEP + "/parked after S106.md", "d42327cbe4b3c25b8f923ef2447ef4ba"),
    ("maths/parked P1-P7, after round 3.md", R3 + "/parked after round 3.md", "6a50b6b2c96281cbeb4d7ffab33ea79c"),
    ("maths/formal core, after round 3, before the step.md", R3 + "/formal core, after round 3.md",
     "9202ad317a5987481d4374cf5d718d8b"),
    ("maths/formal claims, after round 3, before the step.md", R3 + "/formal claims, after round 3.md",
     "1daa09d01fd00ec406034dc0fc69a8c9"),
    ("maths/inventions I165-I183, added in round 3.md", R3 + "/inventions register - addendum after round 3.md",
     "ce8f00ae62d5b6933e899d93d7402e29"),
    ("maths/inventions I122-I164, added in round 2.md", R2 + "/inventions register - addendum after round 2.md",
     "507a0d56a4596f93a1118eaf3677c00a"),
    ("maths/inventions I01-I102.md", R2M + "/inventions register.md", "397c8381ceb56a231afe154466696bb6"),
    ("maths/inventions I103-I108, external examples.md",
     R2M + "/inventions register - addendum for the external examples.md", "1f7beaf9420340e773e76e6987b7fa06"),
    ("maths/inventions I109-I121, creative transport case.md",
     R2M + "/inventions register - addendum for the creative transport case.md", "52e1400f03634ed0908ff451f0939ca4"),
    ("maths/formal claims FC-E1 to FC-E5, external examples.md",
     R2M + "/formal claims - addendum for the external examples.md", "be4000fa00e47e190865c6ea52d4a2ab"),
    ("the step/report.md", STEP + "/S106 report.md", None),
    ("the step/critical review.md", STEP + "/S106 critical review.md", None),
    ("the step/the orchestrator's decisions on the critical review.md",
     STEP + "/S106 the orchestrator's decisions on the critical review.md", None),
    ("the step/the second checker on the critical review.md",
     STEP + "/S106 the second checker on the critical review.md", None),
    ("the step/text changes for the written-in test.json", STEP + "/text changes for S106.json",
     "cc978532cb8abed4ad0506a95649ddd8"),
    ("the step/text changes for the bridge.json", STEP + "/text changes for S47.json", "431206c572803507df09e60af273b616"),
    ("round 3/text changes applied in round 3.json", R3 + "/text changes after the review.json",
     "2d24131a45029c62c9f9bd2f3f2b5294"),
    ("round 3/moves after round 3.md", R3 + "/moves after round 3.md", "778be185632b10796ca498e9206f6fbd"),
    ("round 3/integration report.md", R3 + "/integration report.md", "3ffc18bcdd239dad581854981a821d68"),
    ("round 3/area 1 - verdicts and formal fixes.md", R3R + "area 1 - verdicts and formal fixes.md",
     "f690ce669b59d1c0d7801c67c26b8b09"),
    ("round 3/area 3 - verdicts and formal fixes.md", R3R + "area 3 - verdicts and formal fixes.md",
     "545c81842c2336bb2380536bd122892e"),
    ("round 3/critical review.md", R3R + "critical review of the round.md", "e720f198ee14fa2493e7c5b868439604"),
    ("round 3/the orchestrator's decisions on the critical review.md",
     R3R + "the orchestrator's decisions on the critical review.md", "66b5ec99f428b6da8389c57bfc82fa58"),
    ("round 3/the second checker on the critical review.md", R3R + "the second checker on the critical review.md",
     "f2f778e7f8674095bb01b6e4701e7727"),
    ("cases/creative transport case card.md", "results/S104 Round 2 - case card, the creative transport experiment.md",
     "3bdd2fab9ed63777cca1868d57c178aa"),
    ("cases/code of the external examples (read only).py", MODEL_DIR + "/s104_external.py", None),
    ("cases/code of the creative transport case (read only).py", MODEL_DIR + "/s104_creative_transport.py",
     "dd49e2b0bc0c72fde6c1b93977f73c8e"),
    ("cases/code of the cases the step moved (read only).py", MODEL_DIR + "/s106_cases.py",
     "5b153417c62c3b17ab275c81d52adcf5"),
]
MODEL_FILES = ["__init__.py", "args.py", "cases.py", "claims_a.py", "claims_area1.py", "claims_b.py", "claims_r3a1.py",
               "claims_r3a2.py", "claims_r3a3.py", "claims_s106.py", "claims_s41.py", "core.py", "e9.py", "gen.py",
               "harness.py", "inventions_model.py", "phys.py", "register.py", "report.py", "run.py"]
MODEL_MD5 = {"core.py": "80a1f3200320d35606787c6438fb4012", "claims_s106.py": "0a07401b7f1b84e3be05a46b82ff2afc",
             "claims_a.py": "c1e323dd533dd60babccfcec20c9b269", "claims_b.py": "4d69c86f37e36a78b8222f9e5efcfe7e",
             "claims_s41.py": "f0611d34990664a342390068b427f57b", "claims_r3a3.py": "6a49482b69cb49598a0a03aa6ba021a8"}
# Left out on purpose (decision S43; lesson S42): they use "model" for a candidate explanation.
LEFT_OUT = [(R3R + "area 2 - verdicts and formal fixes.md", 72), (R3 + "/owner questions after round 3.md", 7)]
# The printouts: (path in the sandbox, file, arguments, time limit, what the S106 records give for the output)
PRINTOUTS = [
    ("program printouts/whole suite now, scale 4, time cap 45.txt", MAT + "/printout - whole suite now.txt",
     ["-B", "-m", "model.run", "--scale", "4", "--time-cap", "45", "--no-write"], 2400, {"H": 128, "CEX": 2, "NT": 7}),
    ("program printouts/external examples FC-E1 to FC-E5 now.txt", MAT + "/printout - external examples now.txt",
     ["-B", "s104_external.py"], 900, "86a67664a9a3584351fd4836a4140b69"),
    ("program printouts/creative transport case CT1 to CT8 now.txt", MAT + "/printout - creative transport case now.txt",
     ["-B", "s104_creative_transport.py"], 900, "d473944e74d2f349b1fdfb83277843cf"),
    ("program printouts/the cases the step moved, now.txt", MAT + "/printout - the cases the step moved now.txt",
     ["-B", "s106_cases.py"], 900, "043aeb3647a9004ae43009a7fed50b4e"),
]
STATUS = {"HOLDS ON ALL MODELS TRIED": "H", "COUNTEREXAMPLE FOUND": "CEX", "NOT TESTED": "NT"}


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


def committed(rel):
    """Tracked by git and unchanged from HEAD (lesson S12: the material is fixed before anything is sent)."""
    rel = os.path.relpath(path(rel), REPO)
    git = ["git", "-C", REPO]
    tracked = subprocess.run(git + ["ls-files", "--error-unmatch", "--", rel], capture_output=True,
                             stdin=subprocess.DEVNULL).returncode == 0
    same = subprocess.run(git + ["diff", "--quiet", "HEAD", "--", rel], capture_output=True,
                          stdin=subprocess.DEVNULL).returncode == 0
    return tracked and same


def need(ok, msg):
    if not ok:
        raise SystemExit("refused: " + msg)


def words(s):
    return len(s.split())


def counts_of(printout):
    c = {"H": 0, "CEX": 0, "NT": 0}
    for m in re.finditer(r"(?m)^FC\S+\s{2}(HOLDS ON ALL MODELS TRIED|COUNTEREXAMPLE FOUND|NOT TESTED)\s{2}\(", printout):
        c[STATUS[m.group(1)]] += 1
    return c


# ------------------------------------------------------------------ the printouts (--printouts)
def printouts():
    check_sources(printouts_too=False)
    before = {f: md5_file(MODEL_DIR + "/model/" + f) for f in MODEL_FILES}
    for _, rel, args, limit, want in PRINTOUTS:
        print("running", " ".join(args), flush=True)
        env = {"PATH": "/usr/local/bin:/usr/bin:/bin", "LANG": "C.UTF-8", "PYTHONHASHSEED": "0",
               "PYTHONDONTWRITEBYTECODE": "1"}
        r = subprocess.run([sys.executable] + args, cwd=path(MODEL_DIR), env=env, capture_output=True, text=True,
                           timeout=limit)
        need(r.returncode == 0, "%s ended with exit %d: %s" % (args, r.returncode, r.stderr[-500:]))
        if isinstance(want, dict):
            got = counts_of(r.stdout)
            need(got == want, "%s: %s, the second checker of S106 gives %s" % (args, got, want))
        else:
            need(md5(r.stdout) == want, "%s: output md5 %s, the S106 records give %s" % (args, md5(r.stdout), want))
        text = ("# command, from `%s`: PYTHONHASHSEED=0 python3 %s\n# exit 0\n\n" % (MODEL_DIR, " ".join(args))
                + r.stdout)
        write_checked(rel, text)
    after = {f: md5_file(MODEL_DIR + "/model/" + f) for f in MODEL_FILES}
    need(before == after and not os.path.exists(path(MODEL_DIR + "/model/__pycache__")),
         "the program's folder changed during the printouts")


# ------------------------------------------------------------------ the text by line
def lines_of(text):
    lines = text.split("\n")
    return lines[:-1] if lines and lines[-1] == "" else lines


def changed_lines(a, b):
    la, lb = lines_of(a), lines_of(b)
    need(len(la) == len(lb), "the two texts have %d and %d lines: not one line to one line" % (len(la), len(lb)))
    return {n for n, (x, y) in enumerate(zip(la, lb), 1) if x != y}


def by_line(text, text_md5, r3, step):
    lines = lines_of(text)
    out = ["# The text under review, by line",
           "",
           "A reading copy of `text/the text under review.md` (md5 %s), made so that no line is longer than 1,500 "
           "characters. Each line of the text is given as `L<n> | <line>`; a line longer than 1,500 characters is cut "
           "at a space into pieces, the second and later written `L<n> (cont.) | <piece>`. A star, `L<n>* |`, marks "
           "the %d lines the third review round changed; a plus, `L<n>+ |`, the %d lines the step after it changed "
           "(both, `L<n>*+ |`). Empty lines are given as `L<n> |`. Nothing else differs from the text."
           % (text_md5, len(r3), len(step)), ""]
    for n, l in enumerate(lines, 1):
        star = ("*" if n in r3 else "") + ("+" if n in step else "")
        pieces, rest = [], l
        while len(rest) > 1500:
            cut = rest.rfind(" ", 0, 1500)
            cut = cut if cut > 0 else 1500
            pieces.append(rest[:cut])
            rest = rest[cut:].lstrip(" ")
        pieces.append(rest)
        out.append(("L%d%s | %s" % (n, star, pieces[0])).rstrip())
        out += ["L%d (cont.) | %s" % (n, p) for p in pieces[1:]]
    return "\n".join(out) + "\n"


# ------------------------------------------------------------------ the sources
def all_sources():
    return ([src for _, src, _ in SOURCES] + [MODEL_DIR + "/model/" + f for f in MODEL_FILES]
            + [DECISIONS[0], MODEL_DIR + "/s104_external.py", MODEL_DIR + "/s104_creative_transport.py",
               MODEL_DIR + "/s106_cases.py"])


def check_sources(printouts_too=True):
    for dst, src, want in SOURCES:
        need(os.path.isfile(path(src)), "%s is not there" % src)
        if want:
            need(md5_file(src) == want, "%s has md5 %s, expected %s" % (src, md5_file(src), want))
    for f, want in MODEL_MD5.items():
        rel = MODEL_DIR + "/model/" + f
        need(md5_file(rel) == want, "%s has md5 %s, expected %s" % (rel, md5_file(rel), want))
    got = sorted(f for f in os.listdir(path(MODEL_DIR + "/model")) if f.endswith(".py"))
    need(got == sorted(MODEL_FILES), "the program's files are %s, the build names %s" % (got, sorted(MODEL_FILES)))
    for rel in all_sources():
        need(os.path.isfile(path(rel)), "%s is not there" % rel)
        need(committed(rel), "%s is not committed, or differs from HEAD: the material must be fixed first" % rel)
    if printouts_too:
        for _, rel, _, _, _ in PRINTOUTS:
            need(os.path.isfile(path(rel)), "%s is not there: run --printouts first" % rel)
            need(committed(rel), "%s is not committed: commit the printouts first" % rel)


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


# ------------------------------------------------------------------ the owner's words
KEEP = [20, 21, 23, 25, 26, 27, 28, 33, 34, 36, 40, 41, 43, 44, 45, 47]
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
    # S43: Claude's question used the word "model" for a candidate explanation (lesson S42); it is described, not quoted
    (43, "Answering Claude's question \"When should a model count as \\\"cheating\\\", meaning it just has the answer "
         "written into it instead of explaining it? …\": ",
     "Answering Claude's question on when a candidate explanation counts as cheating, meaning it just has the "
     "answer written into it instead of explaining it: "),
    (44, "Answering Claude's question asked again without the word \"model\" (", "Answering Claude's question ("),
    (47, "Quoting from the plain file 105 ",
     "Quoting a passage Claude wrote in a plain-words summary of the third review round, "),
]
# Spans that may hold quotation marks: Claude's words, not the owner's (checked: every other span holds none)
REPLACE_WITH_QUOTES = {43, 44}
DATES = {20: "24 and 25 September 2026", 21: "25 September 2026", 23: "25 September 2026", 25: "26 September 2026",
         26: "26 September 2026", 27: "26 September 2026", 28: "26 September 2026", 33: "27 September 2026",
         34: "27 September 2026", 36: "27 September 2026", 40: "28 September 2026", 41: "28 September 2026",
         43: "28 September 2026", 44: "28 September 2026", 45: "28 September 2026", 47: "28 September 2026"}
# The owner's own words that each brief must carry (the first quotation, or for S43-S47 the owner's answer)
OWNER_CHECK = {43: "LLMs are not part of the semantics", 44: "Neither. It's an explanation when the agent",
               45: "Yes, take the test out", 47: "I think I misunderstood this question. The math doesn't ask for "
                                                 "anything."}


def owner_words(dec):
    own = {}
    for n in KEEP:
        m = re.search(r"(?m)^S%d\. \[Claude's reading[^:\]]*: .*?\] (.*)$" % n, dec)
        need(m, "decision S%d not found" % n)
        own[n] = m.group(1)
    text = dict(own)
    for n, old, new in REPLACE:
        s = text[n]
        need(s.count(old) == 1, "S%d: %r occurs %d times" % (n, old, s.count(old)))
        i = s.index(old)
        need(s[:i].count('"') % 2 == 0 and s[i + len(old):].count('"') % 2 == 0,
             "S%d: %r lies inside a quotation" % (n, old))
        need(n in REPLACE_WITH_QUOTES or '"' not in old, "S%d: the span replaced holds a quotation" % n)
        text[n] = s.replace(old, new)
    for n in own:
        b = text[n]
        for _, old, new in [r for r in REPLACE if r[0] == n]:
            b = b.replace(new, old, 1)
        need(own[n] == b, "S%d: the owner's words changed" % n)
        need(not re.search(r"\blog S\d|\bfile \d{2,3}\b|\bdraft \d|round-2|round 1\b", text[n]),
             "S%d still names an internal record" % n)
        need(not re.search(r"\bmodel", text[n], re.I) or n not in (43, 44), "S%d still says \"model\"" % n)
    need("if implementation forces invention, that needs to be recorded." in own[36], "S36 is not whole")
    need("more prose is self defeating" in own[40] and "This only needs maybe 3 checkers." in own[40], "S40 is not whole")
    body = ["## 2. The owner's words",
            "The theory's owner took the decisions below, in this order; they bind every finding and every proposal. "
            "Each is quoted from the project's record of decisions. Words inside quotation marks are the owner's, "
            "word for word, typos included, except where the connecting words say that a quoted passage is Claude's "
            "(in S26, S28, S41, S44, S45 and S47). The few connecting words outside the quotation marks are the "
            "recorder's; where the record names internal files or logs there, a plain description stands in their "
            "place, and in S43 Claude's question is described, not quoted. Where this brief is worded differently from "
            "the owner's words, the owner's words decide, and you should say so. In these words \"Claude\" is the "
            "drafters of the text and of the maths; \"your agents\" and \"your explanation\" in S27 are addressed to "
            "them."]
    for n in KEEP:
        body.append("**S%d** (%s). %s" % (n, DATES[n], text[n]))
        if n == 26:
            body.append("*What S27 answers.* Between S26 and S27 the drafters gave the owner the five examples asked "
                        "for: holding an explanation in a carrier (ink, a brain, a file); copying or teaching it; "
                        "testing between two rival explanations, where the test changes the thing explained; building "
                        "from an explanation (a perpetual-motion machine, a bridge); and performing music. The examples "
                        "are the drafters' words, not the owner's, and are not a decision. S27 is the owner's reply to "
                        "them.")
        if n == 41:
            body.append("*What S41 is.* The four questions in S41 are the drafters' words; the owner's words are the "
                        "four answers. Each answer is the owner's choice between two sides the drafters offered. S47 "
                        "says how the answer on the bridge was meant. Do not argue the answers: take them as given, "
                        "with S47, and attack how they were written into the maths, the program and the text "
                        "(section 4).")
        if n == 45:
            body.append("*What S44 and S45 are.* The question in S44 and the proposal in S45 are the drafters' words; "
                        "the owner's words are the answers, and in S45 the owner chose the proposal with its "
                        "description. Do not argue them: a written-in answer never stops a candidate being an "
                        "explanation; it makes it a bad one. Attack how this was written into the maths, the program "
                        "and the text (section 4).")
        if n == 47:
            body.append("*What S47 is.* The passage the owner quotes is the drafters' own words; the owner's words "
                        "follow it. Do not argue them: attack how they were written (section 4).")
    return "\n\n".join(body), own


# ------------------------------------------------------------------ the briefs
JOBS = [
    (1, "breaker", "the breaker", "s107_glm_breaker"),
    (2, "maths_words", "the maths against the words", "s107_glm_maths_words"),
    (3, "structure", "the structure of the formal core", "s107_glm_structure"),
    (4, "cases", "the cases", "s107_glm_cases"),
]
BRIEF_PATH = {n: "tests/S107 Round 4 - GLM job %d, %s.md" % (n, title) for n, _, title, _ in JOBS}

INTRO = """# Round 4 of the review of a semantics: job {n} of 4, {title}

## 1. What this is

You are one of four readers working at the same time on the same material, each with a slightly different job. Yours is section 5. You work in a folder, the sandbox, that holds copies of the material; section 3 maps it and says what your tools can do.

A theory, called here the semantics, is stated in a prose text (`text/the text under review.md`, {nlines} lines, cited as L1 to L{nlines}). A formal core writes its sentences as definitions (D§.n, with the sentence each formalizes quoted above it) and as encodings of the text's worked cases (E1 to E9). Formal claims (FCnn) state consequences, and a program in `model/` searches small models for counterexamples to them: a claim either holds on every model tried, has a counterexample, or was not tested. In this brief a "model" is only such a small structure built to test a claim, or the program's folder; what the theory judges is always called a candidate or an explanation.

Three review rounds have been read. Each changed the maths and changed lines of the text by three kinds of change only: a span deleted, a span replaced by its formal statement, or a span replaced by a pointer to a definition or claim. The third round changed {n_r3} lines. Then one step, after the owner's decisions S44, S45 and S47 (section 2), took out of what makes something an explanation the test that a candidate with its answer simply written in is not one, everywhere the theory used it, and put " and criticism" back into the opening at L13 (a revert of the third round's deletion there); it changed {n_step} lines. Your job is to attack this state, in maths and code, and find where it fails. The maths is a conjecture, and so is the text.

Where the maths had to choose something the text leaves open, the choice is recorded as an invention (Inn), with the other choices it could have made. Nothing invented is the text's own content. A counterexample that rests on an invention tells against the text only where the text fixes what the invention fills in; otherwise it tells against that way of writing the text, and you should say which.

Who is who: "the owner" is the person whose theory this is; "Claude" is the drafters of the text and of the maths, and the checkers who ruled on the earlier rounds and on the step. The records of the third round and of the step name the outside readers and the reviewers; who made a point decides nothing, only its reasons do."""

SANDBOX = """## 3. The sandbox and your tools

| file or folder | what it is |
|---|---|
| `text/the text under review.md` | the text under review, exactly as it stands |
| `text/the text under review, by line.md` | the same text, one line per text line as `L<n> \\| ...`, long lines cut into pieces of at most 1,500 characters; a star marks the lines the third round changed, a plus the lines the step changed. Read the text here: the Read tool cuts lines longer than 2,000 characters |
| `text/the text after round 3, before the step.md`; `text/the text before round 3.md` | the text as the third round left it, and as it found it, for comparison |
| `maths/formal core, now.md` | the definitions D0.1 to D18.x and the encodings E1 to E9, each with the sentences it formalizes; a mark in square brackets names the round, step or ruling that made a change |
| `maths/formal claims, now.md` and `.json` | the claims and their results now: 128 hold on every model tried, 2 have a counterexample (FC23, FC63), 7 were not tested, of 137 |
| `maths/inventions I184 onwards, added in the step.md` | the step's inventions (I184 Pin; I185, I186 withdrawn; I187 to I191) and the earlier inventions whose standing it changed |
| `maths/inventions I165-I183, added in round 3.md`; `... I122-I164, added in round 2.md`; `maths/inventions I01-I102.md`, `... I103-I108, external examples.md`, `... I109-I121, creative transport case.md` | the earlier inventions |
| `maths/formal core, after round 3, before the step.md`; `maths/formal claims, after round 3, before the step.md` | the maths before the step, for comparison |
| `maths/formal claims FC-E1 to FC-E5, external examples.md` | five claims from an outside cross-examination, with the models the program built for them |
| `maths/owner questions, now.md` | the questions to the owner and their status: none new; the third round's one question answered by S44 and S45 |
| `maths/parked, now.md`; `maths/parked P1-P7, after round 3.md` | points parked (section 4): P1 to P7, and P8, new |
| `the step/report.md` | what the step did and why: every use of the written-in test, kept or removed (its section 1), the changes old and new, the runs, the cases that moved, the text changes, the bridge (its section 15) |
| `the step/critical review.md`, `the step/the orchestrator's decisions on the critical review.md`, `the step/the second checker on the critical review.md` | the objections to the step, what was done with them, and the last rulings, which changed the maths after the report (D6.11 withdrawn; the pin kept as a clause of D6.3; L273 a pointer) |
| `the step/text changes for the written-in test.json`; `the step/text changes for the bridge.json` | the step's 13 changes on 10 lines and the revert at L13: line, kind, old span, new span, why, what each settles |
| `round 3/text changes applied in round 3.json` | the third round's 13 changes on 9 lines (the one at L13 is reverted by the step) |
| `round 3/moves after round 3.md`, `round 3/integration report.md`, `round 3/area 1 - ...`, `round 3/area 3 - ...`, `round 3/critical review.md`, `round 3/the orchestrator's decisions ...`, `round 3/the second checker ...` | how the third round ruled, each fix in maths and code, and what it changed at the end |
| `cases/creative transport case card.md`; `cases/code of ... (read only).py` | a worked case supplied by the owner; the code that reads it, the external examples, and the cases the step moved (you can read it; it does not run here) |
| `program printouts/` | the program's printouts on the model as it now stands: the whole suite at scale 4 (every claim, in full), the external examples FC-E1 to FC-E5, the creative transport case CT1 to CT8, and the 28 cases of the step's case script, each with its result before and after the step |
| `model/` | the program, standard-library Python: `core.py` (organizations, questions, candidates, the account), `claims_a.py`, `claims_b.py`, `claims_area1.py`, `claims_s41.py`, `claims_r3a1.py` to `claims_r3a3.py`, `claims_s106.py` (one function per claim), `args.py`, `phys.py`, `gen.py` (the model generators), `cases.py`, `e9.py`, `inventions_model.py` |
| `BRIEF.md` | this brief |

Your tools. **Read** (read a long file in pieces with offset and limit), **Glob** and **Grep**, inside this folder only. **Bash** runs one command only, typed plainly from this folder: `python3 -m model.run` with `--claim FCnn` (repeatable, for example `--claim FC23.new2 --claim FC84.new1`), `--scale N` (at most 4), `--time-cap N` (at most 60), `--brief`, `--help`. Anything else is refused, and nothing can be written. One claim at the default scale takes seconds; the whole suite takes several minutes (give the Bash tool a timeout of 600000 for it), and its printout at scale 4 is already in `program printouts/`. You cannot change the program or run new code: a new definition, a changed claim or a new small model goes into your report as Python in the program's own notation (as in `model/core.py` and `model/claims_s106.py`), with the output you expect, marked "not run"; the next step of the round will run it. Work economically: read what your job needs, search with Grep, run a claim where its result bears on your point.

**Only your final message is kept.** Write the whole report in your last message, after your last tool call."""

HELD = """## 4. What changed since round 3, the owner's decisions as written, parked matters, values

**The third round** (`round 3/moves after round 3.md`; `round 3/text changes applied in round 3.json`): 18 formal changes and 13 text changes on 9 lines (L13, L49, L61, L69, L201, L220, L375, L397, L405): 4 deletions, 7 spans replaced by their formula, 2 pointers. The deletion at L13 (" and criticism") is reverted by the step.

**The step after it, as written** (`the step/report.md`, with the second checker's rulings; `maths/formal core, now.md` §6, D12.2, D13.8). Do not argue the owner's decisions: attack how they were written. A proposal that would put the written-in test back, or reverse or weaken an owner's answer, is not taken.

| decision | the owner's words | written as | text | tested by |
|---|---|---|---|---|
| S44, S45 | "In either case, it is an explanation. Just not a good one"; "Yes, take the test out" | D6.5: Dependence :⟺ NC0 ∧ NC2 (was NonCircular :⟺ NC0 ∧ NC1 ∧ NC2); D6.7: Acc :⟺ F1 ∧ F2 ∧ A ∧ Dependence ∧ NonVacuous, no grain ℓ among its arguments; D6.3: Slot and NC1 stay defined, read by no conjunct of (E); Pin(ℰ,k;a,b), Slot's clause at one pair (I184); I187, I188 | L255 (heading, "independent", two sentences deleted), L257, L262, L273 (a pointer), L275, L317, L343, L397, L520, L536 | FC23 (e), FC23.new1 (h), FC23.new2, FC23.new3, FC25.new2; the case script (10 cases move under the reading 'every', 5 more under another reading only) |
| S47 | "The math doesn't ask for anything. The agent does when a question occurs as potentially important and worth investigating." | L13's " and criticism" restored (a revert); the bridge as FC84.new1 (a1), with no criticism in the history, and (a2), with a criticism of an earlier design, and in both no question about the brief occurred to the agent (NoBriefQuestion, I191); I190: L13's phrase names D13.8's episode; Con, CT and Episode read no criticism event | L13 | FC84.new1 (a1), (a2); FC32.new1 (f) |

What the step kept, by its own account (`the step/report.md` §1): NC2, as Dependence; the table of observed answers fails (F1) (L269, D6.10), while the encoding table E_enc now meets (E); the reversed calculation fails (F2) (L271, L325; FC27); L331's "circular" and L397's block on a premise that is the claim's denial speak of arguments (D9.7; FC60 (a), FC72). What its second checker withdrew: D6.11 (b), (c) ("the further questions it leaves open") and the node Open, now parked (P8).

**The owner's four answers (S41), as they now stand.** No line is held.

| answer | the owner's words | written as | text | tested by |
|---|---|---|---|---|
| Q2 | "No, not if just declared" | D16.XV: Acc(ℰ) ∧ Dec(t) ⇒ ¬Expl(ℰ); L49, L61 (Suff), L69 write Account(ℰ) ∧ ¬Dec(t) | L17, L49, L61, L69 | FC30.new1; FC23.new2 (f) |
| Q6 | "Yes, it can", as S47 says it was meant | D13.8: an episode need hold no change of contract, and each change it holds is recorded (I165); the bridge as above | L55, L13 | FC84.new1 |
| Q15 | "Yes, it can be explained" | D6.4: Contrast symmetric in Y_p ∪ {⊥}, ⊥ ≠ y; now (E)'s Dependence | L255 | FC22 (b) |
| Q23 | "Yes, it's an argument" | D9.2: a premise alone is an argument; D9.6: usable when accepted (I166); two sentences at L397 deleted in the third round | L397 | FC72 (d) to (f), FC72.new1 |

**Points the records note and do not rule on.** For each, propose a fix from your job's angle, in one of the forms of section 6, or say in one line why none is needed.

| point | where | what |
|---|---|---|
| N1 | D7.4 | Acc(E_v, p), with v declaring (E_v, t_v, Γ_v): no designation δ_v, while D16.4 and D14.7 quantify δ |
| N2 | FC31, L61 | FC31 (not tested) still names "the four conditions" at L61, which the third round replaced by Account(ℰ) ∧ ¬Dec(t) |
| N3 | D9.10 (K1), FC107 | a criticism whose connection writes its defect in now has bearing where it meets the rest of (E) |
| N4 | D16.XV (Suff), L536 | candidates with a slot now fall in (Suff)'s range |
| N5 | L255, I188 | the heading is now the formula Dependence, the kinds of change allowed giving no plain-word name |
| N6 | FC84.new1, I191 | "a question about the brief occurred to the agent" is encoded as a criticism aimed at the brief; which occurrences are criticisms, and of what, is read through Θ (I90) |

- **Parked.** What hard to vary covers is parked (S33, S34; `maths/parked, now.md`, P1 to P8). P8 is the owner's "bad … through the questions it leaves open" (S44, S45): what makes an explanation a bad one, and which questions it leaves open, are parked with it. Do not argue them, and build nothing on them.
- **Values.** Where values are placed is the owner's question. Propose nothing that moves them."""

FORM = """## 6. The form of every proposal (decision S40)

Every proposal is exactly one of:
1. **maths**: a changed or new definition or claim, in the formal core's notation, written beside the one it replaces, with its id;
2. **code**: a change to the program or a new small model, as Python in the program's notation, with the output you expect, and "run" (with the command and the program's result line) or "not run";
3. **a text change of one of three kinds**: delete a span; replace a span by its formal statement; replace a span by a pointer to a definition or claim. Give the line, the exact old span and the exact new span.

Never new prose: no added sentence, no reworded sentence, no gloss. A proposal that adds prose is not taken.

The owner's words bind every proposal and every name in it. Do not list, count, grade or rank rivals, and do not argue from how many (S20). Nothing about what must happen to a candidate (S21). Every word S23 forbids stays out of every name, gloss and proposal; "argument" is reasons why this and not that, and every accepting is tentative (S23). Physical possibility only where information or knowledge is instantiated or transformed, and as the content of claims a candidate can conflict with (S25 to S27). Nothing is settled, and a ruling out by a claim taken as given is a choice (S28). Nothing about what hard to vary covers, or about what makes an explanation a bad one (S33, S34; P8). Every choice you make that the text leaves open is named as an invention, with the other choices (S36). The four answers stand (S41), with S47 for the bridge. AI programs are not part of the semantics (S43). A written-in answer never stops a candidate being an explanation (S44, S45): no proposal puts the written-in test back into what makes something an explanation, by that name or another; a finding that (E) without it admits a candidate the text or the owner's words exclude is ruled like any other, and its fix keeps S44 and S45. The maths asks for nothing; an agent asks, when a question occurs to it as worth investigating (S47): no proposal has the maths demand a criticism event, or reads the bridge as having had no criticism where only no question about the brief occurred to the agent."""

REPORT = """## 7. The report

Terse: tables, formulas, small models in the program's format, one-line reasons. No summary of the material. For each finding: an id (B1, B2, ... for job 1; W1, ... for job 2; S1, ... for job 3; K1, ... for job 4), the item or items and the line or lines, what fails in one line, the model or computation (and whether you ran it: the command and the program's result line), the proposal in one of the forms of section 6, and the inventions it rests on, if any. Items you examined and found nothing against are named together in one line at the end of each section. At most about 3,000 words.

Sections, in this order:
{sections}

Write the whole report as your final message. Its last line must be exactly:

END OF REPORT"""

JOB_TEXT = {
    1: ("the breaker", """## 5. Your job: the breaker

Try to break the step's changes (section 4). For each, look for a small model where the definition or claim fails; where it contradicts another definition of the core; where it changes the result of a worked case the text fixes; or where it clashes with the owner's words (S41 with S47, S44, S45). Most pressure on these five:

1. **(E) without the written-in test** (D6.7: Acc :⟺ F1 ∧ F2 ∧ A ∧ Dependence ∧ NonVacuous). Build a candidate that should not count as meeting (E), and see whether it now does. Take it from what the text excludes (a table of observed answers, L269; a reversed calculation, L271, L325; a bare denial, L339; a contract of relabelings only, L257; a contrast no admitted edit realizes, L275), or from what the owner's words exclude (a link only declared, Q2). If it now meets (E), is that S44's and S45's point (a written-in answer is an explanation, a bad one), or a clash with a line of the text or with the owner's words? A candidate whose answer is written in and which now meets (E) is S45's, not a clash: say what else in it fails, if anything.
2. **Dependence = NC0 ∧ NC2, kept** (D6.2, D6.4, D6.5). Is it the written-in test by another name (a candidate that fails it only because its answer is written in), or empty (a candidate that meets it for no reason the text gives)? NC0 is said to hold of every candidate: is it then idle in D6.5? Does Lost's second disjunct let through what L255's sentence would not?
3. **The kept exclusions**: tables (D6.10: E_tab fails (F1); E_enc now meets (E), FC25.new2); reversed calculations (FC27; (F2)'s composition clause; the case the step's second checker added, the transport restricted to a contract of H settings, which now meets (E)); circular arguments (L331; L397's block on a premise that is the claim's denial, D9.7; FC60 (a), FC72). Does each still hold for the reason the text gives, and not only through the written-in test?
4. **The pin** (D6.3: Pin(ℰ,k;a,b), Slot's clause at one pair, I184; FC23.new3 (a): Slot ⟺ Pin at every pair of Det_C). Is it well defined where t does not translate (a,b), where Det_C is empty, where δ_E lies in several V_k? Does anything in the core or the program (`core.account`, `core.slot`, `core.NC1`, `SLOT_QUANTIFIER`) still read Slot or NC1 as a condition of (E)?
5. **The bridge re-encoded** (S47; FC84.new1 (a1), (a2); NoBriefQuestion, I191; I190; the [S47] notes at D12.2 and D13.8; FC32.new1 (f)). Does the encoding say "no question about the brief occurred to the agent", no more (not "no criticism") and no less? Build the nearest history on which NoBriefQuestion and "no question occurred to the agent" part ways: a question that occurred and was not pursued; a criticism of a design that also bears on the brief; a brief changed with no criticism in the history. Does anything in the maths now ask for a criticism event?

For each: (i) what exactly the definition says, in one line; (ii) the smallest model that breaks it, or makes it disagree with a line of the text, another definition or the owner's words, in the program's format; (iii) the program's check where one exists (run the claim); (iv) a fix, in one of the forms of section 6.""",
     """(a) (E) without the written-in test; (b) Dependence; (c) the kept exclusions; (d) the pin; (e) the bridge; (f) the third round's other changes, where the step bears on them; (g) what held under attack, one line each."""),
    2: ("the maths against the words", """## 5. Your job: the maths against the words

Where a formula or a pointer replaced words in the text, and wherever a definition formalizes a sentence, does the maths say what the sentence needs, no more and no less?

1. **Every text change since round 2's text**: the third round's 13 (`round 3/text changes applied in round 3.json`; the lines starred in the reading copy) and the step's 14 (`the step/text changes for the written-in test.json`, `the step/text changes for the bridge.json`; the lines marked with a plus). For each change of kind "formal" or "pointer": compare the old span with the new span, and with the definition or claim the new span points to. Verdict: **same** (the formula says what the words said), **more** (what it adds), **less** (what it drops), or **other** (where it differs). For every verdict but "same", give a witness: the smallest case on which the words and the formula give different answers. For each "delete" (the step's: L255's heading words, "independent" and two sentences, L317's and L397's "that it assumes its own answer, or ", L536's clause): does anything the rest of the text or the maths uses go with it?
2. **The revert at L13** (" and criticism" restored; I190). Does L13 now say what S47 says (the maths asks for nothing; an episode of conjecture and criticism includes one in which no question occurred to the agent as worth investigating), no more and no less? Compare it with I190, D12.2, D13.8, FC84.new1 (a1), (a2), and with L201's pointer and L411, which the step kept.
3. **The definitions the step changed** (D6.2's note, D6.3 with Pin, D6.5, D6.7, D6.8, D6.10's note, D18.1) and the renamed conjunct (the formula Dependence at L255, L257, L262, L275, L343, L520), each against the sentences quoted above it: same, more, less, or other, with a witness.
4. **The owner's answers as they now stand** (section 4): for each written line and each definition, does it say the answer, with S47 for Q6 and S44, S45 for the written-in test? The answer is given: the question is only whether the maths and the text now say it.
5. **Any other definition** you meet where the formula and its quoted sentence part ways in a way that changes a claim's result.

Say for each gap which should stand, the maths or the words, and why, in one line; where the words should stand, the fix is to the maths; where the maths should stand, the fix is a text change of one of the three kinds. Where the gap rests on an invention the text leaves open, name it: the text need not settle it.""",
     """(a) the text changes of the third round and of the step, one table: change id, line, kind, verdict, witness, proposal; (b) the revert at L13; (c) the definitions the step changed; (d) the owner's answers as they stand; (e) other definitions; (f) the proposals, each in its form."""),
    3: ("the structure of the formal core", """## 5. Your job: the structure of the formal core

Read the formal core as it now stands (`maths/formal core, now.md`) as one system of definitions, and look for:
1. **Dangling uses of removed notions.** Every place in the core, the claims, the program and the text that still uses a notion the step took out of (E) or withdrew: NC1 as a condition of (E) (it was in D6.5 and D6.7); the old slot test ("non-circular", NonCircular, "assumes its own answer", "restates", "unanalysed", "at the declared grain", the grain ℓ as an argument of Acc); D6.11 (b), (c) and the node Open (withdrawn, parked as P8); the quantifier of D6.3 as bearing on (E). For each: is it still read as a condition, or only named? Is a claim, a note or a node of D18.1's graph left pointing at nothing?
2. **Circular definitions.** The dependence of the definitions after the step (D18.1; the program's DEP in `model/claims_b.py`; FC32, FC32.new1): every cycle; whether the step's edges (Dependence → (O), (Q), C, δ; the node Slot) are the edges the definitions actually have.
3. **Primitives left undefined.** Every symbol used and never defined, the step's new ones among them (Pin, Det_C, NoBriefQuestion, a criticism aimed at a brief). For each, whether D0.2 lists it, or it is read through Θ or a declared input.
4. **Definitions no claim uses.** For each definition, whether any claim's statement or the program uses it (search `maths/formal claims, now.md` and `model/`). An unused definition is not thereby idle: say whether the text needs it.
5. **Two definitions that conflict.** A model on which one definition says something the other says cannot hold, or two definitions of one term.
6. **Notation used two ways.** For example: Dependence as (E)'s conjunct and "dependence" in D18.1's dependence order and §18; Slot, Pin and NC1; Dep in the program; ⊥; δ as a designation and as a defect; C as a contract and as a set of pairs; primes on changed definitions.

For each finding, the smallest witness (a chain of definitions, a model, or two quoted uses) and a fix in one of the forms of section 6.""",
     """(a) dangling uses of removed notions, one table: place, notion, read as a condition or named only, fix; (b) cycles, with the dependence table; (c) undefined primitives, one table: symbol, where used, listed by the text or not; (d) definitions no claim uses; (e) conflicts; (f) notation used two ways; (g) the proposals, each in its form."""),
    4: ("the cases", """## 5. Your job: the cases

Run the cases through the maths as it now stands, by hand or by the program, and say whether their results move.

1. **The text's worked cases**: the encodings E1 to E9 of the formal core, and the cases the text works through in its lines (among them the pole and its shadow, the table of observed answers at L269, the reversed calculation at L271 and L325, "p because p" at L273, the bare denial at L339, the skew-symmetric matrices at L343, the swap, and the occlusion case at L626 to L630). For each: what the text says the result is, what the maths gives now, and whether the third round or the step moved it.
2. **The external examples FC-E1 to FC-E5** (`maths/formal claims FC-E1 to FC-E5, external examples.md`; now: `program printouts/external examples ...`): the result after round 2, now, moved or not, and which change moved it.
3. **The creative transport case, CT1 to CT8, CT8 above all** (`cases/creative transport case card.md`; now: `program printouts/creative transport case ...`). Did the step or the revert at L13 move any reading? Does CT8's result still match what the text says of such a history (L193 to L211, L405, L411)?
4. **The cases the step moved** (`cases/code of the cases the step moved (read only).py`; its printout: 28 cases, 10 move under the reading 'every', 5 more under another reading only). List every case whose result moved, and check each move against the owner's words: S44 ("In either case, it is an explanation. Just not a good one"), S45 ("A written-in answer never stops something being an explanation. It only makes it a bad one"), S47 ("The math doesn't ask for anything"). Does every case those words make an explanation now meet (E) where it meets the rest? Does any case move that those words leave where it was? For each moved case, does a line of the text still state the old result?
5. **The owner's examples as encoded**: the student's declared pendulum formula (Q2; FC30.new1), the bridge (Q6 with S47; FC84.new1 (a1), (a2)), the weathervane (Q15; FC22 (b)), "perpetual motion is impossible" used alone (Q23; FC72 (d)), the shop sign with one part and with two (S44; FC23.new2 (a), (b)). Is each encoding faithful to its example? Does the maths give the owner's answer? Build, for each, the nearest variant the encoding would judge otherwise than the owner's words do.
6. **New small cases, at most six**, each built to probe one change of the step: a candidate that should not count and may now meet (E); Dependence on a contract where only the written-in part carries the contrast; a pin at a pair the transport does not translate; the bridge with a question about the brief that occurred and was not pursued; a criticism whose connection writes its defect in (K1, FC107). Each as a small model in the program's format, with the result you expect under the maths now and under the text's words, and whether the two agree.

Where a result moves, say which change moved it and whether the move matches the text and the owner's words; where the maths and the text part ways, the fix goes in one of the forms of section 6.""",
     """(a) the worked cases, one table: case, lines, the text's result, the result now, moved or not, why; (b) FC-E1 to FC-E5, one table; (c) CT1 to CT8, one table, then CT8 in full; (d) the cases the step moved, one table: case, before, now, the owner's words it meets or not, a line of the text that still states the old result; (e) the owner's examples; (f) the new cases; (g) the proposals, each in its form."""),
}

SCRUB = [r"\bfits?\b", r"\bfitt\w*", r"\bsupport\w*", r"\bverif\w*", r"\bcorroborat\w*", r"\bprov(e|es|ed|en|ing)\b",
         r"\bdisprov\w*", r"\bbelie\w*", r"better than", r"worse than", r"\btrue\b", r"\btruth\w*", r"\bfalse\b",
         r"\bestablish\w*", r"\bauthorit\w*", r"\bfoundation\w*", r"\bderiv\w*", r"\bjustif\w*", r"\brank\w*",
         r"\bvalid\w*", r"\bcorrect(ly|ness)?\b", r"\bevidence\b", r"\bconfirm\w*", r"\bcertain\w*",
         r"\bgrade[sd]?\b", r"\bwrong\b", r"\bprefer\w*",
         r"\bAtria\b", r"\bMimo\b", r"\bGLM\b", r"\bFable\b", r"\bOpus\b", r"\bSonnet\b", r"\bDeutsch\b",
         r"\bMarletto\b", r"\bPinker\b", r"\blog S\d", r"\bS(?:9\d|1\d\d)\b", r"\bCONFIRMED\b"]
# "model" used for a candidate explanation (decision S43; lesson S42). In the frame, also "modelled"/"modelling".
MODEL_FOR_CANDIDATE = [r"\bmodels? counts? as (cheat|simply|just|an? explanation|explain)", r"\bwhen does a model\b", r"\b(candidate|explanatory) models?\b",
                       r"\bmodels? (that|which) explains?\b", r"\ba model (is|as) an explanation\b"]
FRAME_MODEL = MODEL_FOR_CANDIDATE + [r"\bmodell?(ed|ing)\b"]
ALLOWED_IN_FRAME = ["Do not list, count, grade or rank rivals"]
DECISIONS_NAMED = set(KEEP)


def frame_of(text):
    f = re.sub(r"(?s)## 2\. The owner's words.*?(?=## 3\. The sandbox)", "", text)
    for s in ALLOWED_IN_FRAME:
        f = f.replace(s, "")
    return f


def scan(text):
    f = frame_of(text)
    hits = sorted({m.group(0) for pat in SCRUB + FRAME_MODEL for m in re.finditer(pat, f, re.I)})
    for m in re.finditer(r"\bS(\d\d)\b", f):
        if int(m.group(1)) not in DECISIONS_NAMED:
            hits.append(m.group(0))
    return hits


def model_for_candidate(text):
    return sorted({m.group(0) for pat in MODEL_FOR_CANDIDATE for m in re.finditer(pat, text, re.I)})


def build_brief(n, title, owner, counts):
    job_title, job, sections = JOB_TEXT[n]
    sections = sections.rstrip(".") + ("; (n) the points N1 to N6 (section 4): for each, a fix in one of the forms of "
                                       "section 6, or one line on why none is needed.")
    parts = [INTRO.format(n=n, title=title, **counts), owner, SANDBOX, HELD, job, FORM,
             REPORT.format(sections=sections)]
    return "\n\n".join(parts) + "\n"


# ------------------------------------------------------------------ the build
def build():
    check_sources()
    files = {}
    text = read(TEXT[0])
    r3 = changed_lines(read(TEXT_R2A[0]), read(TEXT_R3[0]))
    step = changed_lines(read(TEXT_R3[0]), text)
    need(sorted(r3) == R3_LINES, "round 3 changed lines %s, the record gives %s" % (sorted(r3), R3_LINES))
    need(sorted(step) == STEP_LINES, "the step changed lines %s, its record gives %s" % (sorted(step), STEP_LINES))
    bl = by_line(text, md5_file(TEXT[0]), r3, step)
    files[BYLINE] = bl
    counts = {"nlines": len(lines_of(text)), "n_r3": len(r3), "n_step": len(step)}
    # the left-out files are caught by the scan that keeps them out, and are not in the sandbox (lesson 26)
    for rel, ln in LEFT_OUT:
        need(model_for_candidate(lines_of(read(rel))[ln - 1]), "%s L%d is not caught by the scan" % (rel, ln))
        need(rel not in [s for _, s, _ in SOURCES], "%s is in the sandbox" % rel)
    owner, own = owner_words(read(DECISIONS[0]))
    rows = []
    for n, name, title, tag in JOBS:
        b = build_brief(n, title, owner, counts)
        hits = scan(b)
        need(not hits, "brief %d: the frame holds %s" % (n, hits))
        need(words(b) <= CAP, "brief %d has %d words, above %d" % (n, words(b), CAP))
        for k in KEEP:
            need(OWNER_CHECK.get(k, own[k].split('"')[1]) in b, "brief %d lacks the owner's words of S%d" % (n, k))
        files[BRIEF_PATH[n]] = b
        rows.append((n, name, title, tag, BRIEF_PATH[n], words(b), md5(b)))
    entries = [{"path": dst, "src": src, "md5": md5_file(src)} for dst, src, _ in SOURCES]
    entries.append({"path": "text/the text under review, by line.md", "src": BYLINE, "md5": md5(bl)})
    entries += [{"path": dst, "src": rel, "md5": md5_file(rel)} for dst, rel, _, _, _ in PRINTOUTS]
    entries += [{"path": "model/" + f, "src": MODEL_DIR + "/model/" + f, "md5": md5_file(MODEL_DIR + "/model/" + f)}
                for f in MODEL_FILES]
    for e in entries:
        need(not re.search(r"(\.env$|key)", e["path"], re.I), "a sandbox path looks like a key file: %s" % e["path"])
        if not e["path"].endswith(".py"):
            body = bl if e["src"] == BYLINE else read(e["src"])
            hit = model_for_candidate(body)
            need(not hit, "%s uses \"model\" for a candidate: %s (decision S43)" % (e["src"], hit))
    manifest = {"note": "round 4 (log S107): the files copied into each GLM call's sandbox, each checked by md5 at the "
                        "copy; the brief is added as BRIEF.md. Written by tools/s107_build.py.",
                "text_under_review": {"path": TEXT[0], "md5": md5_file(TEXT[0]), "lines": counts["nlines"],
                                      "lines_changed_by_round_3": sorted(r3),
                                      "lines_changed_by_the_step": sorted(step)},
                "decisions_record": {"path": DECISIONS[0], "md5": md5_file(DECISIONS[0])},
                "left_out": [{"path": rel, "why": "uses \"model\" for a candidate explanation at L%d (decision S43; "
                                                  "lesson S42)" % ln} for rel, ln in LEFT_OUT],
                "printout_commands": {dst: "PYTHONHASHSEED=0 python3 " + " ".join(a) + "  (from " + MODEL_DIR + ")"
                                      for dst, _, a, _, _ in PRINTOUTS},
                "files": entries}
    files[MANIFEST] = json.dumps(manifest, indent=1, ensure_ascii=False) + "\n"
    jobs = {"round": "round 4 of the review rounds (log S107)", "rule": READING_RULE, "out": OUT, "max_pass": 3,
            "effort": "medium", "context_1m": True, "attempts": 6, "max_rejects": 3, "deadline": 7200,
            "manifest": MANIFEST, "manifest_md5": md5(files[MANIFEST]),
            "sandbox_root": "s107_sandboxes", "home_root": "s107_homes",
            "helper": "tools/glm_via_claude_code_sandboxed.py",
            "jobs": [{"job": n, "name": name, "tag": tag, "brief": BRIEF_PATH[n], "brief_md5": h}
                     for n, name, title, tag, _, w, h in rows]}
    files[JOBS_FILE] = json.dumps(jobs, indent=1, ensure_ascii=False) + "\n"
    return files, rows, manifest


def main():
    a = sys.argv[1:]
    need(set(a) <= {"--check", "--printouts"}, "usage: s107_build.py [--printouts | --check]")
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
    print("\n| job | name | tag | brief | words (build) | md5 |\n|---|---|---|---|---|---|")
    for n, name, title, tag, rel, w, h in rows:
        print("| %d | %s | %s | `%s` | %d | %s |" % (n, title, tag, rel, w, h))
    print("\nsandbox: %d files from the manifest + BRIEF.md; manifest md5 %s" % (len(manifest["files"]),
                                                                            md5(files[MANIFEST])))


if __name__ == "__main__":
    main()
