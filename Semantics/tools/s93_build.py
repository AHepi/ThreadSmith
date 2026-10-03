#!/usr/bin/env python3
"""s93_build.py: build the S93 cross-examination of draft 4 of revision 2, in eleven parts, and its job list for
tools/s87_run.py. Written 25 September 2026 by a Claude subagent for the orchestrator (log S93).

  python3 Semantics/tools/s93_build.py           build the eleven briefs and the job list; refuses to overwrite a
                                                 file whose content differs
  python3 Semantics/tools/s93_build.py --check   rebuild in memory and compare with the files; writes nothing

What is cross-examined (eighteen items, X01 to X18 in the order of the text):
  - every change-list entry that draft 4 added or edited: W59.1 (as two items, its paragraphs "Rivals" and
    "Problems"), W60.1, W34.1, W33.1, W36.1 and W38.1 (found by comparing the change list at 99e9cd0, draft 3, with
    draft 4, section by section);
  - the ten entries the S90 checkers fixed after the S90 cross-examination (S90 Verification of draft 3, check 1):
    W37.1, W19.1, W35.1, W35.2, W20.1, W40.1, W24.1, W22.1, W6.3 and W7.5;
  - one proposed WORDING entry, not yet made: draft 4 L325's "not the calculation's \\(H\\)" to "... \\(L\\)", as Part V
    L271 says of the same reversed calculation.
Each part carries: the owner's position (decision S20) verbatim, with the drafters' reading beside it, and lesson
S26's rule verbatim; excerpts of the draft-4 theory text, each line with its line number; the part's items in the S90
form (id, place, kind, reason word, declaration, old and new wording byte for byte), with the wording an earlier outside
reading saw where it has since changed; the tasks and the report form; and the described situations the items name,
added while the part stays within WORD_CAP words. Withheld, as in S90: every W-number; REASON, CHECK, GAIN, LOSS and
the drafters' expected direction on each case; the draft-4 pass record, the analyses and the S90 rulings.

Sources are checked by md5 before anything is built; the build refuses on any mismatch.
"""
import hashlib, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SEM = os.path.dirname(HERE)
TESTS = os.path.join(SEM, "tests")
OUT_DIR = os.path.join(SEM, "results", "S93 Cross-examination - draft 4 - returns")
JOBS = os.path.join(HERE, "s93_jobs - draft 4 in eleven parts.json")
READING_RULE = "results/S93 How the cross-examination of draft 4 will be read - written before sending.md"

SRC = {
    "draft4": ("tests/Revision 2 - file 13 draft 4, theory text.md", "fc55b470c63cd4b3c27d6aa64d8d8c17"),
    "cl": ("tests/Revision 2 - change list, draft of 23 September.md", "b6b2ea95ea9e21ebea3316d8e9fa4b40"),
    "file11": ("authority/11 Claude Fable Semantics - standalone theory, revision 1.md",
               "5e494c1095d920d128b9a79de378f923"),
    "s81book": ("tests/S81 Case book - the 52 cases, situations and fixed verdicts, as the tested agent sees them.md",
                "4f488d149e44669240d5db546c8e946a"),
    "d3t": ("tests/S89 Case book - candidate case D3-T, the controller that failed the test/final.md",
            "6b211dea40d735abf50426e56344f161"),
    "decisions": ("records/Semantics - Decisions.md", "84ee721cd0398b25f4869f8b960f9481"),
    "lessons": ("records/Semantics - Lessons.md", "bb7d37ac64841b81113d5f6aced09b24"),
    "s90A1": ("tests/S90 Cross-examination - part A1, errata and pointers, Parts 0 to VI.md",
              "1364c50fdc388e091552bbf41b538d76"),
    "s90A2": ("tests/S90 Cross-examination - part A2, errata and pointers, Parts VIII to XVI.md",
              "234bf749788fc3ab3ddcb1e06e249f98"),
    "s90B1": ("tests/S90 Cross-examination - part B1, declared inputs.md", "130a5eace514ebb02b736d12a311ade2"),
    "s90B2": ("tests/S90 Cross-examination - part B2, ownership, repair, selection, newness.md",
              "d214f495e0b9fcac4f423d522bee0d37"),
    "s90C": ("tests/S90 Cross-examination - part C, source-derived clarifications.md",
             "2183faa5005b112347f484b6c8ace196"),
}
WORD_CAP = 14000          # cases are added while the part stays within this, by the runner's count and by wc -w
HARD_CAP = 15000          # Atria failed at 26,000 words and succeeded at 18,000 or fewer; the owner's cap here is 15,000


def read(rel):
    with open(os.path.join(SEM, rel), encoding="utf-8") as f:
        return f.read()


def md5(s):
    return hashlib.md5(s.encode("utf-8")).hexdigest()


def need(ok, msg):
    if not ok:
        raise SystemExit("s93_build: " + msg)


def wc_words(s):
    """wc -w in the C locale: runs of bytes that are not ASCII whitespace."""
    return len(re.findall(rb"[^ \t\n\r\v\f]+", s.encode("utf-8")))


# ------------------------------------------------------------------ sources
T = {}
for k, (rel, want) in SRC.items():
    T[k] = read(rel)
    need(md5(T[k]) == want, "%s: md5 %s, expected %s" % (rel, md5(T[k]), want))
D4 = T["draft4"].split("\n")
if D4 and D4[-1] == "":
    D4 = D4[:-1]
need(len(D4) == 632, "draft 4 has %d lines, expected 632" % len(D4))


def entries(text):
    body = text[text.index("## The entries"):]
    parts = re.split(r"(?m)^(### W.*)$", body)
    out = {}
    for k in range(1, len(parts), 2):
        wid = parts[k][4:].split(" — ")[0]
        b = parts[k + 1]
        d = {}
        for fld in ("OLD", "NEW"):
            m = re.search(r"(?m)^- \*\*" + fld + r":\*\*\n````text\n(.*?)\n````\n", b, re.S)
            d[fld] = m.group(1) if m else None
        for fld in ("KIND", "REASON WORD", "DECLARATION", "FILE-11 LINE"):
            m = re.search(r"(?m)^- \*\*" + re.escape(fld) + r":\*\* (.*)$", b)
            d[fld] = m.group(1) if m else None
        out[wid] = d
    return out


E = entries(T["cl"])


def s90_changes():
    """Each S90 part's section 3, parsed: R-id -> kind, reason, declaration, old, new, as the S90 readers saw them."""
    R = {}
    for k in ("s90A1", "s90A2", "s90B1", "s90B2", "s90C"):
        t = T[k]
        sec = t[t.index("## 3. "):t.index("## 4. Your tasks")]
        parts = re.split(r"(?m)^(### R\d\d .*)$", sec)
        for i in range(1, len(parts), 2):
            rid, body = parts[i].split()[1], parts[i + 1]
            m = re.search(r"\*\*Kind:\*\* (\w+)\. \*\*Reason given:\*\* ([^\n]*?)\.\n", body)
            d = re.search(r"\*\*Declaration:\*\* (.*?)\n\n\*\*Old", body, re.S)
            o = re.search(r"\*\*Old:\*\*\n\n````text\n(.*?)\n````", body, re.S)
            n = re.search(r"\*\*New:\*\*\n\n````text\n(.*?)\n````", body, re.S)
            R[rid] = dict(kind=m.group(1), reason=m.group(2), decl=d.group(1), old=o.group(1), new=n.group(1))
    return R


R90 = s90_changes()


def s90_cases():
    C = {}
    for k in ("s90A1", "s90A2", "s90B1", "s90B2", "s90C"):
        t = T[k]
        sec = t[t.index("## 5. Described situations"):]
        parts = re.split(r"(?m)^(### [ON]\d+ - .*)$", sec)
        for i in range(1, len(parts), 2):
            cid = parts[i].split()[1]
            txt = (parts[i] + parts[i + 1]).rstrip() + "\n"
            need(cid not in C or C[cid] == txt, "case %s differs between S90 parts" % cid)
            C[cid] = txt
    # O34 and O38 were given in no S90 part: the S81 book's entries byte for byte, headed as S90 headed its cases.
    book = T["s81book"]
    for cid in ("O34", "O38"):
        m = re.search(r"(?ms)^## (%s - .*?)(?=^## O\d+ - |\Z)" % cid, book)
        need(m, "case %s not found in the S81 book" % cid)
        C[cid] = ("### " + m.group(1)).rstrip() + "\n"
    # D3-T (candidate O76): its final text, the situation, the question, and the verdict with its reason.
    d = T["d3t"]
    sit = re.search(r"(?ms)^## Situation\n\n(.*?)\n\n## Question", d).group(1)
    q = re.search(r"(?ms)^## Question\n\n(.*?)\n\n## Verdict", d).group(1)
    v = re.search(r"(?ms)^## Verdict\n\n(.*?)\n\n## Reason", d).group(1)
    r = re.search(r"(?ms)^## Reason\n\n(.*?)\n\n## Confidence", d).group(1)
    C["D3-T"] = ("### D3-T - The discarded lamp controller\n\n**Situation.** %s\n\n**Question.** %s\n\n"
                 "**Thoughtful person's verdict.** %s %s\n" % (sit, q, v, r))
    return C


CASES = s90_cases()

# ------------------------------------------------------------------ the owner's position and the drafters' rule
dec = T["decisions"]
s20 = re.search(r"(?m)^S20\. \[Claude's reading: (.*?)\] (.*)$", dec)
need(s20, "decision S20 not found")
S20_READING, S20_WORDS = s20.group(1), s20.group(2)
les = T["lessons"]
s26 = re.search(r"(?m)^S26\. (.*)$", les).group(1)
S26_CORRECTED = re.search(r"(The analyses of 24 September proposed .*?\(𝒱 is not among Part XIV's declared inputs\)\.)",
                          s26).group(1)
S26_RULE = re.search(r"(Rule: state hard to vary .*)$", s26).group(1)

# ------------------------------------------------------------------ the items
PROPOSED_OLD = ("The reversed calculation \\(H=L\\tan\\theta\\) is not: intervening on \\(H\\) changes the target's "
                "\\(L\\) but not the calculation's \\(H\\).")
PROPOSED_NEW = ("The reversed calculation \\(H=L\\tan\\theta\\) is not: intervening on \\(H\\) changes the target's "
                "\\(L\\) but not the calculation's \\(L\\).")
need(T["draft4"].count(PROPOSED_OLD) == 1 and T["file11"].count(PROPOSED_OLD) == 1,
     "the proposed entry's OLD must occur once in draft 4 and once in file 11")
need(PROPOSED_NEW not in T["draft4"], "the proposed entry's NEW is already in draft 4")

# id, entry, place, earlier S90 id (the wording an earlier outside reading saw), or None
ITEMS = [
    ("X01", "W37.1", "Part 0, What this document claims", "R01"),
    ("X02", "W36.1", "Part I, Fallibility without falsehood-as-work", "R06"),
    ("X03", "W19.1", "Part II, Kinds are edit-signatures", "R08"),
    ("X04", "W35.1", "Part IV, Expectation, surprise, violation", "R12"),
    ("X05", "W35.2", "Part IV, Expectation, surprise, violation", "R13"),
    ("X06", "W20.1", "Part V, Account", "R15"),
    ("X07", "W34.1", "Part VI, Commitments that do no work", "R23"),
    ("X08", "W33.1", "Part VI, Commitments that do no work", "R24"),
    ("X09", "W59.1", "Part VI, Rivals", None),
    ("X10", "W59.1", "Part VI, Problems", None),
    ("X11", "proposed", "Part VII, Production and direction", None),
    ("X12", "W40.1", "Part VII, Explanations that remove structure", "R25"),
    ("X13", "W24.1", "Part VIII, Functional transport", "R26"),
    ("X14", "W60.1", "Part VIII, A failed answer stays failed", None),
    ("X15", "W22.1", "Part IX, Bearing", "R28"),
    ("X16", "W6.3", "Part XI, Worth, and the normative relation", "R39"),
    ("X17", "W7.5", "Part XIV, Dependence order", "R48"),
    ("X18", "W38.1", "The note of sources and departures, placed before Part 0", None),
]
ITEM = {i[0]: i for i in ITEMS}

# Cases named by the entries' CASES AT RISK, as N-ids (O53-O75 are N1-N5, N7-N13, N15-N25; O76 is D3-T), in the order
# they are offered to a part; a part takes them in this order while it stays within WORD_CAP.
PARTS = [
    dict(key="A", title="rivals", items=["X09"],
         q={"X09": ["a", "c2", "d"]},
         extra=["PXIV", "PXV", "D7"],
         cases=["N1", "N2", "N3", "N25", "O24", "O36", "D3-T", "N7", "O48", "O46", "N5"]),
    dict(key="B", title="problems", items=["X10"],
         q={"X10": ["a", "c1", "c2"]},
         extra=["PX", "PXI", "D7"],
         cases=["N2", "N3", "N5", "O24", "N4", "O1", "D3-T", "O27", "N1", "O48"]),
    dict(key="C", title="a failed answer stays failed", items=["X14"],
         q={"X14": ["a", "b", "c2"]},
         extra=["PXI", "PXIV", "PXV", "D7"],
         cases=["O1", "D3-T", "O27", "O8", "N7", "N2", "O24"]),
    dict(key="D", title="commitments that do no work, and Part I's companion edit", items=["X02", "X07", "X08"],
         q={"X02": ["a"], "X07": ["a"], "X08": ["a", "d"]},
         extra=["PXIV", "PXV"],
         cases=["N1", "O36", "N25", "N3", "O45", "N7", "O2", "N4", "N2", "O47"]),
    dict(key="E", title="the note of sources and departures", items=["X18"],
         q={"X18": ["a", "c1"]},
         excerpt=["P0", "PI", "PIII", "PIV", "PV", "PVI", "PVIIrm", "PIX", "PX", "PXI", "PXIII", "PXIV", "D2", "D3",
                  "D8", "D9"],
         note="**For X18, the standard tests read as follows.** T1: does each sentence of the note that begins "
              "\"Here\" say truly what the revised text says, at the Parts it names; and does what the note says of the "
              "two books agree with them, so far as you know them? Quote no more than a few words of either book, and "
              "never more than twenty-five words in all. T2: the note is declared no part of the theory; does any line "
              "of it state a claim that the revised text does not make? T3 as written. T4 only where the note describes "
              "the theory in a way that would change a careful reader's verdict on a case.",
         cases=["N2", "N3", "N4", "N1", "N22", "N5"]),
    dict(key="F", title="selection in Part 0, and kinds across two candidates", items=["X01", "X03"],
         q={"X03": ["d"]},
         extra=["PX", "PXII", "D10"],
         cases=["O11", "O10", "O22", "O9", "N25", "N9", "N11"]),
    dict(key="G", title="expectation, violation and surprise", items=["X04", "X05"],
         q={},
         extra=["PX", "PXII", "D4", "D10"],
         cases=["N18", "O23", "O24", "O11", "O48", "O3", "O13", "O5"]),
    dict(key="H", title="the commitments of a candidate", items=["X06"],
         q={"X06": ["d"]},
         extra=["PVII", "PXI", "PXV"],
         cases=["O45", "O46", "O36", "N1", "O47", "O2", "O5", "O7"]),
    dict(key="I", title="Part VII, the pole sentence and the absent structure", items=["X11", "X12"],
         q={},
         extra=["PVII", "PXIV", "PXV"],
         cases=["O6", "O4", "N22", "O34", "N8", "N25"]),
    dict(key="J", title="functional transport, and the terms of (K1)", items=["X13", "X15"],
         q={"X15": ["a"]},
         note="**Why (a) is asked of X15.** Part VI's paragraph \"Problems\" (line 317) says that a criticism that a "
              "candidate is easy to vary must supply a rival, and points to Part IX, where X15 defines the terms of "
              "(K1).",
         extra=["PX", "PXIV", "PXV"],
         cases=["O27", "N20", "N11", "O40", "O50"]),
    dict(key="K", title="the normative relation, and the dependence order", items=["X16", "X17"],
         q={},
         extra=["PX", "PXI", "PXII", "PXIII", "PXIV", "D5", "D6"],
         note="**For X17, T3 includes this.** Part VI of the revised text now defines rivals, conflict, what is "
              "established, what fits and a problem for a question (lines 315 and 317). Say whether the dependence "
              "order, as X17 leaves it, stays true of the revised text with those terms in it.",
         cases=["O35", "O38", "O37", "O49"]),
]

# ------------------------------------------------------------------ the excerpt blocks (draft-4 line ranges)
BLOCKS = [  # key, first line, last line: the draft-4 theory text cut at its headings
    ("P0c", 1, 18), ("P0n", 19, 28), ("P0p", 29, 32), ("P0g", 33, 58), ("P0w", 59, 64),
    ("PI", 65, 80), ("PII", 81, 130), ("PIII", 131, 164), ("PIV", 165, 228), ("PV", 229, 284), ("PVI", 285, 320),
    ("PVIIpd", 321, 326), ("PVIIid", 327, 332), ("PVIIob", 333, 336), ("PVIIrm", 337, 340), ("PVIIsk", 341, 344),
    ("PVIIcr", 345, 350), ("PVIII", 351, 372), ("PIX", 373, 400), ("PX", 401, 432), ("PXI", 433, 458),
    ("PXII", 459, 484), ("PXIII", 485, 512), ("PXIV", 513, 531), ("PXV", 532, 549),
    ("D1", 550, 559), ("D2", 560, 569), ("D3", 570, 577), ("D4", 578, 585), ("D5", 586, 593), ("D6", 594, 601),
    ("D7", 602, 609), ("D8", 610, 613), ("D9", 614, 617), ("D10", 618, 632),
]
ALIAS = {"P0": ["P0c", "P0n", "P0p"], "PVII": ["PVIIpd", "PVIIid", "PVIIob", "PVIIrm", "PVIIsk", "PVIIcr"]}
# The core every part carries, unless a part gives its own list ("excerpt" in PARTS).
CORE = ["P0", "PI", "PII", "PIII", "PIV", "PV", "PVI", "PVIII", "PIX", "D1", "D2", "D3", "D8", "D9"]
need([b[1] for b in BLOCKS] == [1] + [b[2] + 1 for b in BLOCKS[:-1]] and BLOCKS[-1][2] == 632,
     "the blocks must tile lines 1-632")


def expand(keys):
    out = set()
    for k in keys:
        out |= set(ALIAS.get(k, [k]))
    need(out <= {b[0] for b in BLOCKS}, "unknown blocks %s" % sorted(out - {b[0] for b in BLOCKS}))
    return out


def headings(a, b):
    return [D4[i - 1].lstrip("#").strip() for i in range(a, b + 1) if D4[i - 1].startswith("#")]


def excerpt(keys):
    keys = expand(keys)
    out, gap = [], []

    def flush():
        if gap:
            a, b = gap[0][1], gap[-1][2]
            hs = [h for g in gap for h in headings(g[1], g[2])]
            out.append("[L%d–L%d not given here: %s]" % (a, b, "; ".join(hs)))
            out.append("")
            del gap[:]
    for blk in BLOCKS:
        if blk[0] in keys:
            flush()
            for i in range(blk[1], blk[2] + 1):
                line = D4[i - 1]
                out.append("L%d| %s" % (i, line) if line.strip() else "")
        else:
            gap.append(blk)
    flush()
    while out and out[-1] == "":
        out.pop()
    return "\n".join(out)


def line_of(text):
    """The draft-4 line(s) holding the first line of text (which must be found exactly once)."""
    first = text.split("\n")[0]
    hits = [i + 1 for i, l in enumerate(D4) if first in l]
    need(len(hits) == 1, "%r found on %d lines of draft 4" % (first[:60], len(hits)))
    return hits[0]


# ------------------------------------------------------------------ fixed texts
KIND_TEXT = """Each item is listed with its old wording and its new wording, the reason given for it (erratum, clarification or change of claim) and a declared kind:

- **CLAIM**: a reader can conclude from the new wording something the current text left unconcluded, or can no longer conclude something the current text allowed. Every CLAIM item carries a **declaration**, which is meant to say exactly what changes in what is claimed.
- **WORDING**: the new wording says what the old wording said, in other words.
- **ORDER**: the new wording states, in its place, only what the text already states elsewhere.
- **META**: the note of sources and departures, which stands before the theory, is declared to be no part of the theory and to add nothing to it.

WORDING and ORDER items carry no declaration, because they are meant to change no claim."""

STANCE = """**Your stance.** Those who drafted and checked these items hold that each is true, that each declaration says exactly what changes, that the WORDING and ORDER items change no claim, and that the revised text is coherent. Your job is to attack that, as hard as you can, against the texts alone. For each listed item, give one of two findings: **UPHELD**, when your strongest attack fails, with the reason it fails; or **CHALLENGED**, when an attack succeeds, with the reason and the exact wording you propose in its place. An UPHELD with no attack behind it tells us nothing; show the attacks you made."""

OWNER = """## 2. The owner's position, and the drafters' rule

The theory's owner has stated a position on what makes an explanation hard to vary, on rivals, and on error correction. The drafters restated part of the theory to follow it. The owner's words, the drafters' reading of them, and the rule the drafters bound themselves by are quoted here verbatim. Question (a) in section 5 asks whether the listed wording is faithful to them.

**The owner's words** (24 and 25 September 2026):

> %s

**The drafters' reading of those words**, as recorded beside them:

> %s

**What the owner corrected.** In the drafters' own words: "%s"

**The drafters' rule**, written after that correction:

> %s""" % (S20_WORDS, S20_READING, S26_CORRECTED, S26_RULE)

STD_TESTS = """**The standard tests**, for every listed item.

- **T1. Is it true?** Does the new wording state anything false in the theory's own terms, or anything that its stated hypotheses and the definitions it relies on do not support? Build a counterexample where you can; a small organization, a contract and two candidates are often enough.
- **T2. Are the kind and the declaration right?** For a CLAIM item: is every part of the declaration true of the new wording, and does the new wording claim more than the declaration says, or less? For a WORDING or ORDER item: can a reader now conclude something the current text left unconcluded, or no longer conclude something it allowed? For an ORDER item, name the place that already states what it adds. Say which kind the item should have: CLAIM, WORDING or ORDER.
- **T3. Is it coherent with the rest of the revised text?** Look for a term or symbol used before it is defined, or defined two ways; a clash of notation; a pointer to a Part, derivation, condition, label or tag that does not say what the item says it says; a new sentence that contradicts an unchanged one; an unchanged sentence that the item makes false, stale or idle; and two items that pull against each other.
- **T4. Does it move a verdict?** The theory's verdict on a situation is what a careful reader of the text would say the theory concludes on the situation's question: it agrees with the fixed verdict, disagrees with it, is silent (the text does not settle it), or is split. Report any move between the current text and the revised text, in either direction, and say which. A move away from the fixed verdict is a defect. A move toward it that the declaration does not account for is an undeclared change of claim. Use the situations in section 7, or describe one of your own."""

QUESTIONS = {
    "a": """- **(a) Faithfulness to the owner's position and the drafters' rule (section 2).** Is the wording faithful to them? In particular, does any of it bring back, openly or in effect, a listed set of rivals or versions, an enumeration, a count of versions, a grade or ranking of candidates, or a record or log of failures or rescues doing work that the explanation's own content should do? Quote the words that do it. Where the wording is faithful, say what in it keeps it so.""",
    "b": """- **(b) Does a correction stick?** Does "A failed answer stays failed" hold exactly as stated? Under what conditions could a corrected mistake come back in: on the same question; on a narrowed contract or a changed query; through the background and instruments of the test (K3), or a premise that ceases to be live (K2); through a candidate that changes its answer at the failed pair only slightly, or makes the same mistake at a neighbouring pair not yet tested; through a change of grain or of target; or in some other way? For each, say whether the text lets it happen, and whether it should.""",
    "c1": """- **(c1) Symmetry.** Take the question why the seasons come as they do in the lands the Greeks knew, and no others. The axis-tilt explanation and the myth of Demeter's grief both fit everything established on that question, and on the text's definitions they conflict only at pairs outside it (for example, in lands the Greeks never saw). By the paragraph "Problems" each is then easy to vary relative to the other, and the tilt stays so until the question is widened. Check that this is what the text says. Is it a defect, a harmless consequence, or something the theory should say differently? If differently, give the words, and say whether your words bring back a grade.""",
    "c2": """- **(c2) What counts as established.** The text says that a result is established for an assessor who holds a usable receipt for it (Part IX). Does a failure found by examining a candidate itself, and not by looking at the world, count as established, so that the candidate no longer fits? Examples: a failure of non-circular dependence, a component anchored to nothing, or a contradiction inside the candidate. Does the text settle this? Should it, and how? Say what turns on it for the problems two rivals pose.""",
    "d": """- **(d) Rivals must conflict at an admitted change.** Is the condition right that two candidates are rivals only if they conflict at some admitted edit–boundary pair, in the contract or outside it? Do two candidates that differ only by a part that does no work, or only in how they are written, correctly fall outside "rivals"? Is anything lost that the theory should keep?""",
}
VERDICT_LINES = {
    "a": "`(a) X..: FAITHFUL` or `(a) X..: NOT FAITHFUL — <the words at fault>`",
    "b": "`(b) X..: HOLDS AS STATED`, `(b) X..: HOLDS WITH CONDITIONS — <the condition>` or `(b) X..: FAILS — <the case>`",
    "c1": "`(c1) X..: DEFECT`, `(c1) X..: HARMLESS` or `(c1) X..: SAY DIFFERENTLY`",
    "c2": "`(c2) X..: ESTABLISHED`, `(c2) X..: NOT ESTABLISHED` or `(c2) X..: UNSETTLED BY THE TEXT`",
    "d": "`(d) X..: RIGHT`, `(d) X..: WRONG` or `(d) X..: RIGHT, WITH A LOSS — <the loss>`",
}
Q_ORDER = ["a", "b", "c1", "c2", "d"]

CASES_INTRO = """Each case is a described situation with a thoughtful person's verdict on it, fixed in advance. Where a case states a question, its verdict answers that question. The verdicts stay exactly as written. A verdict is not in question here, only whether an item moves what the theory says about the case. The labels O1 to O52, N1 to N25 and D3-T name cases only; they are not the text's tags, such as (O1). Where a verdict's wording reported only how it was agreed, those words are left out and the place is marked […].

These are the cases named as at risk from the items in section 4; where space ran out, those named later were left out. An item may still move the verdict on a case not given here, and you may describe such a case yourself."""


def fence(s):
    return "````text\n%s\n````" % s


def item_block(xid):
    _, wid, place, rid = ITEM[xid]
    if wid == "proposed":
        ln = line_of(PROPOSED_OLD)
        return "\n\n".join([
            "### %s · %s, line %d (proposed, not yet made)" % (xid, place, ln),
            "**Kind:** WORDING. **Reason given:** erratum.",
            "**Declaration:** none.",
            "**Proposed, not yet made.** The old wording below is one sentence of line %d, which the excerpt in "
            "section 3 shows as it now stands; the current text has the same sentence. Line 271 (Part V) says of the "
            "same reversed calculation: \"intervening on the upstream port changes the target's downstream value but "
            "not the calculation's.\" The proposal changes the last symbol of the sentence, \\(H\\), to \\(L\\), so "
            "that the two places agree. Examine it as you would a change already made: is it right, is WORDING its "
            "right kind, and is there a better repair?" % ln,
            "**Old:**", fence(PROPOSED_OLD), "**New:**", fence(PROPOSED_NEW),
            "**Situations:** O6, O4."])
    e = E[wid]
    new, old = e["NEW"], e["OLD"]
    if xid == "X18":
        head = "### X18 · %s" % place
    elif xid in ("X09", "X10"):
        ln = line_of("**Rivals.**" if xid == "X09" else "**Problems.**")
        head = "### %s · %s, line %d (inserted)" % (xid, place, ln)
    elif wid == "W60.1":
        ln = line_of("**A failed answer stays failed.**")
        head = "### %s · %s, line %d (inserted)" % (xid, place, ln)
    elif wid == "W34.1":
        head = "### %s · %s, line %d" % (xid, place, line_of("**Commitments that do no work.**"))
    else:
        # the line of the first new sentence that is not in the old wording
        probe = [l for l in new.split("\n") if l.strip() and l not in old.split("\n")] or [new]
        cand = [p for p in probe if T["draft4"].count(p) == 1]
        if cand:
            ln = line_of(cand[0])
        else:
            ln = line_of(new.split("\n")[0])
        n_lines = len([l for l in new.split("\n")])
        head = "### %s · %s, line%s %s" % (xid, place, "s" if n_lines > 1 and wid == "W35.1" else "",
                                             "%d–%d" % (ln, ln + 4) if wid == "W35.1" else "%d" % ln)
    kind = e["KIND"]
    decl = e["DECLARATION"] if kind in ("CLAIM",) else ("none." if kind in ("WORDING", "ORDER") else None)
    parts = [head]
    if xid == "X18":
        parts.append("**Kind:** META. **Reason given:** none; the note is new, and the current text has no note of "
                     "sources.")
        parts.append("**Declaration:** none. The note says of itself that it is not part of the theory and adds "
                     "nothing to it. Its lines *Explanation*, *Idle parts*, *Hard to vary*, *Reach* and *Surprise and "
                     "problems* were written or rewritten with the paragraphs \"Rivals\" and \"Problems\"; no outside "
                     "reader has seen any of the note. The note is not in the revised text's line numbering: it stands "
                     "before Part 0, after a short editorial note that says what the revision changed.")
        parts += ["**Old** (the place where the note is inserted, the rule and heading that open Part 0):", fence(old),
                  "**New:**", fence(new)]
    else:
        parts.append("**Kind:** %s. **Reason given:** %s." % (kind, e["REASON WORD"]))
        parts.append("**Declaration:** %s" % decl)
        if xid in ("X09", "X10"):
            parts.append("**One change, two items.** One change inserts both paragraphs, \"Rivals\" (line 315, item "
                         "X09) and \"Problems\" (line 317, item X10), before the rule that opens Part VII, and the one "
                         "declaration above covers both. This part examines %s; the other paragraph is examined in a "
                         "companion part. Read it as part of the revised text, and leave it out of your report except "
                         "where %s depends on it or pulls against it." % (
                             "X09, the paragraph \"Rivals\"" if xid == "X09" else "X10, the paragraph \"Problems\"",
                             xid))
        if xid == "X07":
            parts.append("**One paragraph, two items.** In the current text the old wordings of X07 and X08 are one "
                         "paragraph, in that order, separated by one space; in the revised text the new wordings are "
                         "line 313, in the same order.")
        if xid in ("X09", "X10"):
            need("\n".join(D4[314:321]) == new, "W59.1's NEW is not draft 4's lines 315-321")
            parts += ["**Old:**", fence(old), "**New:** exactly this: the paragraph \"Rivals\" (line 315 of "
                      "section 3), a blank line, the paragraph \"Problems\" (line 317), a blank line, and then the old "
                      "wording above, from line 319. The two paragraphs are printed in full in section 3 and are not "
                      "repeated here."]
        else:
            parts += ["**Old:**", fence(old), "**New:**", fence(new)]
    if rid:
        r = R90[rid]
        diff = []
        if r["new"] != new:
            diff.append("new wording")
        if r["old"] != old:
            diff.append("old wording")
        if r["kind"] != kind:
            diff.append("kind")
        rdecl = r["decl"]
        if kind == "CLAIM" and rdecl != decl:
            diff.append("declaration")
        need(diff, "%s: the earlier reading saw the same text" % xid)
        what = [d for d in ("kind", "declaration", "old wording", "new wording") if d in diff]
        what = what[0] if len(what) == 1 else ", ".join(what[:-1]) + " and " + what[-1]
        parts.append("**What an earlier reading saw.** An earlier outside cross-examination read this change with the "
                     "%s below. After it, the change was revised to the form above. No outside reader has seen the "
                     "form above." % what)
        if "kind" in diff:
            parts.append("*Earlier kind:* %s. *Earlier declaration:* %s" % (r["kind"], rdecl))
        elif "declaration" in diff:
            parts.append("*Earlier declaration:* %s" % rdecl)
        if "old wording" in diff:
            parts += ["*Earlier old wording:*", fence(r["old"])]
        if "new wording" in diff:
            parts += ["*Earlier new wording:*", fence(r["new"])]
    return "\n\n".join(parts)


def build_part(p):
    ids = p["items"]
    n = len(ids)
    word = {1: "one", 2: "two", 3: "three"}[n]
    has_prop = "X11" in ids
    title = "# Cross-examination, part %s of eleven: %s" % (p["key"], p["title"])
    s1 = ["## 1. What you are asked to do",
          "Section 3 gives excerpts of a theory of explanation: a formal semantics of what an explanation is and of "
          "explanatory creativity. It exists in a current version, called **the current text** here. A revised version "
          "has been drafted, called **the revised text**. The revised text is the current text with fifty-seven "
          "changes made to it, and no others, and section 3 quotes it. This cross-examination covers eighteen items, "
          "X01 to X18 in the order of the text: fifteen of those changes, one of them split into two items (X09 and "
          "X10); the note of sources and departures that the revision places before the theory (X18); and one further "
          "change that is proposed and not yet made (X11). No outside reader has checked any of them in its present "
          "form. The cross-examination is split into eleven parts. **This part covers %s item%s: %s.** The other items are examined in companion parts. Read them as "
          "part of the revised text as it stands, and leave them out of your report, except where a listed item "
          "depends on one of them or pulls against it." % (word, "" if n == 1 else "s", ", ".join(ids)),
          KIND_TEXT, STANCE,
          "Section 2 quotes the owner's position that the revision follows. Section 4 lists the items. Section 5 sets "
          "out the tests and questions, and section 6 the form of the report. Section 7 gives described situations, "
          "each with a verdict fixed in advance, which you may use to test whether an item moves what the theory says "
          "about a case.",
          "**Citing the texts.** Line numbers are those of the full revised text, with its title line as line 1; "
          "section 3 prints each line's number before it. Cite an item by its id. Quote the text whenever you rely on "
          "it."]
    s3 = ["## 3. The revised text, in excerpts",
          "Each line below is a line of the revised text, given as `L<number>| ` followed by the line exactly as it "
          "stands; the prefix is not part of the text. Blank lines are kept blank. Where lines are not given, one "
          "bracketed line names them and the headings they hold. The whole revised text has 632 lines. The excerpts "
          "include the new wording of every item of this cross-examination that falls inside them%s." % (
              "; line 325 is shown as it stands, before the proposed change X11" if has_prop else ""),
          "=============== BEGIN EXCERPTS OF THE REVISED TEXT ===============",
          excerpt(p.get("excerpt", CORE + p.get("extra", []))),
          "=============== END EXCERPTS OF THE REVISED TEXT ==============="]
    s4 = ["## 4. The item%s" % ("" if n == 1 else "s"),
          "Each item gives its id; its place, as the Part and heading and the line or lines of the revised text where "
          "the new wording stands; its declared kind and the reason given for it; its declaration, for a CLAIM item; "
          "the old wording, from the current text; and the new wording. The wordings are exact, between fence lines "
          "that are not part of them. Where a change inserts text, the old wording is the passage it is inserted into "
          "or before, and the new wording is that passage with the insertion. Where the change was revised after an "
          "earlier outside reading, the item also gives what that reading saw.",
          "Under **Situations** each item lists the cases in section 7 that the drafters named as possibly affected by "
          "it. The list is a pointer, not a limit."]
    for xid in ids:
        blk = item_block(xid)
        cs = [c for c in p["cases"] if c in ITEM_CASES.get(xid, p["cases"])]
        s4.append(blk if xid == "X11" else blk + "\n\n**Situations:** %s." % (", ".join(cs) if cs else "none named"))
    qs = [(x, q) for x in ids for q in p["q"].get(x, [])]
    s5 = ["## 5. Your tasks",
          "Read each listed item in its place in the revised text. Make the four standard tests on each, and answer "
          "the questions this part asks.",
          STD_TESTS]
    if qs:
        asked = {}
        for x, q in qs:
            asked.setdefault(q, []).append(x)
        s5.append("**The questions this part asks**: %s." % "; ".join(
            "(%s) of %s" % (q, " and ".join(asked[q])) for q in Q_ORDER if q in asked))
        s5 += [QUESTIONS[q] for q in Q_ORDER if q in asked]
    else:
        s5.append("**The questions.** This part asks the four standard tests only. Where a listed item bears on how "
                  "the theory treats rivals, the variation of a candidate, criticism or the correction of a mistake, "
                  "say so in a point, under the heading (a): whether it is faithful to the owner's position and the "
                  "drafters' rule in section 2.")
    if p.get("note"):
        s5.append(p["note"])
    s5.append("**How to argue.** Show every point from the texts. Quote the revised text with line numbers, and quote "
              "the old wording where the comparison matters. Keep apart what the text forces and what a reader might "
              "reasonably take it to mean. Where you find a defect, give the repair in exact words.")
    s6 = ["## 6. The report", "\n".join([
        "- Number your points in one list, most serious first. Head each point with the item id and the test or "
        "question it falls under, for example `%s · T1`%s." % (ids[0], " or `%s · (%s)`" % qs[0] if qs else ""),
        "- For every item you challenge, give the exact wording you propose in its place, between fence lines, whole "
        "(the new wording, the declaration or the kind, as the challenge needs), so that it could be put in place as "
        "written.",
        ] + (["- Then answer each question this part asks, in one short paragraph each, headed by the question and the "
              "item, and end the paragraph with one verdict line, exactly as follows:"] +
             ["  - " + VERDICT_LINES[q].replace("X..", x) for x, q in sorted(qs, key=lambda t: (Q_ORDER.index(t[1]), t[0]))]
             if qs else []) + [
        "- Then one line for every listed item, in the order of the ids, reading exactly `%s: UPHELD` or `%s: "
        "CHALLENGED — <the reason in a phrase>`, with nothing else on the line. An item is CHALLENGED when your points "
        "show it should not stand as it is: it states something false, its kind or declaration is wrong, it makes the "
        "text incoherent, it moves a verdict away from the fixed verdict%s. Otherwise it is UPHELD, and your points say "
        "which attacks you made and why each failed." % (ids[0], ids[0], ", or one of your verdict lines on it above "
                                                         "reads NOT FAITHFUL, FAILS, DEFECT or WRONG" if qs else ""),
        "- Then one line reading exactly `OVERALL: SOUND` or `OVERALL: NEEDS REPAIR`. NEEDS REPAIR means that at least "
        "one item is CHALLENGED.",
        "- Keep the report under about 3,000 words. Depth on the points that matter counts for more than coverage of "
        "small ones.",
        "- End the report with a line that reads exactly END OF REPORT."])]
    head = "\n\n".join([title] + s1 + [OWNER] + s3 + s4 + s5 + s6)
    s7 = ["## 7. Described situations", CASES_INTRO]
    given, left = [], []
    text = head + "\n\n" + "\n\n".join(s7) + "\n"
    stop = False
    for c in p["cases"]:
        need(c in CASES, "case %s has no text" % c)
        trial = text + "\n" + CASES[c]
        if not stop and len(trial.split()) <= WORD_CAP and wc_words(trial) <= WORD_CAP:
            text = trial
            given.append(c)
        else:
            stop = True
            left.append(c)
    need(len(text.split()) <= HARD_CAP and wc_words(text) <= HARD_CAP, "part %s is over %d words" % (p["key"],
                                                                                                    HARD_CAP))
    return text, given, left


# Which of a part's offered cases each item names in its CASES AT RISK (N-ids; O53-O75 and O76 mapped).
OMAP = {"O53": "N1", "O54": "N2", "O55": "N3", "O56": "N4", "O57": "N5", "O58": "N7", "O59": "N8", "O60": "N9",
        "O61": "N10", "O62": "N11", "O63": "N12", "O64": "N13", "O65": "N15", "O66": "N16", "O67": "N17", "O68": "N18",
        "O69": "N19", "O70": "N20", "O71": "N21", "O72": "N22", "O73": "N23", "O74": "N24", "O75": "N25",
        "O76": "D3-T"}


def named_cases(wid):
    t = T["cl"]
    body = t[t.index("### " + wid + " — "):]
    body = body[:body.index("\n### ", 5)] if "\n### " in body[5:] else body
    m = re.search(r"(?ms)^- \*\*CASES AT RISK:\*\*(.*?)(?=^- \*\*[A-Z]|\Z)", body)
    # W34.1 and W59.1 write "N7 (O59)"; under D8 N7 is O58 and O59 is N8, so the O-number there is read as N7's.
    ids = re.findall(r"\b(O\d+|N\d+|D3-T)\b", (m.group(1) if m else "").replace("N7 (O59", "N7 (O58"))
    return {OMAP.get(i, i) for i in ids}


ITEM_CASES = {}
for xid, wid, _, _ in ITEMS:
    if wid == "proposed":
        ITEM_CASES[xid] = {"O6", "O4"}
    else:
        ITEM_CASES[xid] = named_cases(wid)
# W38.1 names cases in its fallback table; the part's cases for X18 are those the Hard to vary line and the departures
# bear on, which W59.1 names.
ITEM_CASES["X18"] = ITEM_CASES["X18"] | named_cases("W59.1")


def build():
    out, rows = {}, []
    for p in PARTS:
        text, given, left = build_part(p)
        # the Situations lines must name only cases given in the part
        for xid in p["items"]:
            if xid == "X11":
                continue
            m = re.search(r"### %s · .*?\*\*Situations:\*\* ([^\n]*)\." % xid, text, re.S)
            named = [c.strip() for c in m.group(1).split(",")] if m and m.group(1) != "none named" else []
            keep = [c for c in named if c in given]
            text = text.replace("**Situations:** %s." % m.group(1),
                                "**Situations:** %s." % (", ".join(keep) if keep else
                                                         "none given here" if named else "none named"), 1)
        fname = "S93 Cross-examination - draft 4 - part %s, %s.md" % (p["key"], p["title"])
        out[os.path.join(TESTS, fname)] = text
        rows.append((p, fname, text, given, left))
    jobs = []
    for p, fname, text, given, left in rows:
        for prov, ladder in (("atria", [65536, 65536]), ("mimo", [131072, 131072])):
            jobs.append({
                "tag": "s93_xexam_%s_%s" % (prov, p["key"]),
                "provider": prov,
                "brief": os.path.join(TESTS, fname),
                "out": OUT_DIR,
                "effort": "medium",
                "ladder": ladder,
                "attempts": 6,
                "max_rejects": 3,
                "max_pass": 3,
                "note": "S93 cross-examination of draft 4, part %s (%s): items %s; read under '%s', independently of "
                        "every other reply" % (p["key"], p["title"], ", ".join(p["items"]), READING_RULE)})
    about = ("S93 cross-examination of draft 4 of revision 2, 25 September 2026: eighteen items (the draft-4 entries "
             "W59.1 as two items, W60.1, W34.1, W33.1, W36.1 and W38.1; the ten entries fixed after S90; one proposed "
             "WORDING entry for draft 4 L325), in eleven parts built by tools/s93_build.py, each part sent whole as the "
             "one user message to both Atria and Mimo at medium effort. Up to three passes (max_pass 3): a later pass "
             "is sent only as the reading rule allows. Read under '%s'." % READING_RULE)
    out[JOBS] = json.dumps({"purpose": "audit", "about": about, "jobs": jobs}, indent=1, ensure_ascii=False) + "\n"
    return out, rows


FORBIDDEN = [r"Revision 2", r"revision record", r"file 13", r"\bW\d+(\.\d+|\(|\b)", r"R2-", r"\bAtria\b", r"\bMimo\b",
             r"\bS\d\d\b", r"\bL\d\d\b(?!\|)", r"\bround\b"]


def check_words(path, text):
    """The frame (everything outside the excerpts, the fenced wordings and the case texts) names no W-number, record,
    model or round; outside part E it names neither book author."""
    frame = re.sub(r"(?s)=============== BEGIN EXCERPTS.*?=============== END EXCERPTS OF THE REVISED TEXT "
                   r"===============", "", text)
    frame = re.sub(r"(?s)````text\n.*?\n````", "", frame)
    frame = frame[:frame.index("## 7. Described situations")]
    hits = []
    for pat in FORBIDDEN:
        for m in re.finditer(pat, frame):
            hits.append(m.group(0))
    if "part E," not in os.path.basename(path):
        for pat in (r"Deutsch", r"Marletto", r"Pinker"):
            if re.search(pat, text):
                hits.append(pat)
    return hits


def main():
    check = "--check" in sys.argv[1:]
    out, rows = build()
    bad = []
    for path, text in out.items():
        if path.endswith(".md"):
            hits = check_words(path, text)
            need(not hits, "%s: withheld words in the frame: %s" % (os.path.basename(path), hits))
        if os.path.exists(path):
            with open(path, encoding="utf-8") as f:
                cur = f.read()
            if cur != text:
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
    print("| part | file in `tests/` | items | words (runner / `wc -w`) | md5 | cases given / offered | left out |")
    print("|---|---|---|---|---|---|---|")
    for p, fname, text, given, left in rows:
        print("| %s | `%s` | %s | %d / %d | %s | %d / %d: %s | %s |" % (
            p["key"], fname, ", ".join("%s (%s)" % (x, ITEM[x][1]) for x in p["items"]), len(text.split()),
            wc_words(text), md5(text), len(given), len(p["cases"]), ", ".join(given), ", ".join(left) or "none"))
    print("job list %s, sha256 %s" % (os.path.relpath(JOBS, SEM), hashlib.sha256(out[JOBS].encode()).hexdigest()))


if __name__ == "__main__":
    main()
