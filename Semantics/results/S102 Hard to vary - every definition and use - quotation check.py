#!/usr/bin/env python3
"""S102 quotation check (log S102, 27 September 2026).

Checks the quotations of two files:
  results/S102 Hard to vary - every definition and use, from the start to now.md
  plain words/102 Hard to vary - every way it has been defined and used, in plain words.md

1. Every stretch of text between straight double quotes, or between curly
   double quotes, of 15 characters or more, is looked for in the repository's
   own files (every .md file in Semantics/, HV Skill/ and Language/records/,
   the two checked files excepted), after white space is collapsed and a
   backslash before a double quote is dropped. A stretch not found is printed.
   On lines where a quotation holds inner double quotes, a stretch can be the
   words between two quotations; those are listed in BETWEEN below, each read
   by hand, and skipped.
2. Each quotation of a book (listed in BOOK below) is counted: at most 25
   words, and it must be found in the repository's source reading or audit.
3. Each attribution listed in PLACED is looked for in the named file.

It reads only and writes nothing. Run from the repository root:
  python3 "Semantics/results/S102 Hard to vary - every definition and use - quotation check.py"
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CHECKED = [
    "Semantics/results/S102 Hard to vary - every definition and use, from the start to now.md",
    "Semantics/plain words/102 Hard to vary - every way it has been defined and used, in plain words.md",
]


def norm(s):
    s = s.replace('\\"', '"')
    return re.sub(r"\s+", " ", s).strip()


def corpus():
    texts = {}
    for top in ("Semantics", "HV Skill", os.path.join("Language", "records")):
        for d, _, fs in os.walk(os.path.join(ROOT, top)):
            for f in fs:
                if not f.endswith(".md"):
                    continue
                rel = os.path.relpath(os.path.join(d, f), ROOT)
                if rel in CHECKED:
                    continue
                with open(os.path.join(d, f), encoding="utf-8") as h:
                    texts[rel] = norm(h.read())
    return texts


# Stretches between two quotations on one line (read by hand; not quotations).
BETWEEN = {
    " (the heading that replaced ",
    " (listed among the words the paths pass through that the text leaves undefined) ",
}

# Book quotations: (quotation, page), each taken from the source reading of
# 24 September or the S89 audit.
BOOK = [
    ("An explanation that is hard/easy to vary while still accounting for what it purports to account for.", "D p.31"),
    ("That is a good explanation – hard to vary, because all its details play a functional role.", "D p.24"),
    ("when theories are easily variable … experimental testing is almost useless for correcting their errors. I call such theories bad explanations.", "D p.22"),
    ("we should choose between them not on the basis of their origin, but according to how good they are as explanations: how hard to vary.", "D p.209"),
    ("advocating a particular one in preference to the others is irrational.", "D p.21"),
    ("because it is a good explanation – hard to vary – it is not yours to modify.", "D p.28"),
    ("good adaptations, like good explanations, are distinguished by being hard to vary while still fulfilling their functions.", "D p.78"),
    ("is hard to change further, while still meeting the criteria, because it has been obtained by tentatively removing flaws in previous versions", "M p.15"),
    ("hard to change further", "M p.15"),
]
BOOK_SOURCES = [
    "Semantics/tests/Revision 2 - error correction and grading, analysis of 24 September.md",
    "Semantics/results/S89 The theory against its sources - Deutsch and Marletto.md",
]

F00 = "Semantics/authority/00 FW5 JUMP from FW2+FW3+FW4 - Explanatory construction (predecessor, 8 September 2026).md"
F10 = "Semantics/authority/10 Claude Fable Semantics - standalone theory.md"
F11 = "Semantics/authority/11 Claude Fable Semantics - standalone theory, revision 1.md"
F12 = "Semantics/authority/12 Claude Fable Semantics - causality, standalone theory.md"
D1 = "Semantics/tests/Revision 2 - file 13 draft, theory text, as sent for cross-examination.md"
D3 = "Semantics/tests/Revision 2 - file 13 draft 3, theory text.md"
D4 = "Semantics/tests/Revision 2 - file 13 draft 4, theory text.md"
D5 = "Semantics/tests/Revision 2 - file 13 draft 5, theory text.md"
SC = "Semantics/tests/Revision 2 - file 13 draft 5, scrubbed of verificationist words, theory text.md"
LT = "Semantics/tests/Revision 2 - scrubbed copy, repaired (S96), after cross-examination, theory text.md"
SA = "Semantics/tests/99 The semantics, standing alone.md"
CL = "Semantics/tests/Revision 2 - change list, draft of 23 September.md"
DEC = "Semantics/records/Semantics - Decisions.md"
LES = "Semantics/records/Semantics - Lessons.md"
SK = "HV Skill/authority/hard-to-vary/SKILL.md"

# Attributions: (file, quotation).
PLACED = [
    (F00, "The FW3 statement that an explanation reaching more is thereby harder to vary is not a valid comparison between arbitrary contents."),
    (F00, "FW5 also withdraws the special permission for a count of conjecturally independent features to order explanations for preference."),
    (F00, "Fix an organization, interpretation, variation family \\(\\mathcal V\\), and a family \\(F\\) of explanatory jobs."),
    (F00, "“Hard to vary” is therefore an articulated pattern of constrained changes, relative to an explanatory job."),
    (F00, "Reach occurs when an unchanged organizational core participates in an account of another question through a stated anchor and additional background."),
    (F00, "There is no further generic predicate defined as “withstanding criticism well enough to merit preference.”"),
    (F00, "no special count of “independent reach” is licensed to choose explanations by itself."),
    (F10, "For a declared family \\(\\mathcal V\\) of organization edits,"),
    (F10, "More reach constrains variation; the containment need not be strict; counting jobs is not a warrant."),
    (F10, "A correspondence can be *selected* — produced by blind variation and survival on a history of predictions —"),
    (F10, "a physically admitted variation operator, and a survival condition enacted by the environment."),
    (F11, "More reach constrains variation; the containment need not be strict; counting jobs is not a warrant."),
    (F11, "The population \\(\\mathcal T\\) is part of the claim: what \\(H\\) leaves open about \\(t\\) is what \\(\\mathcal T\\) leaves open (Derivation 3)."),
    (F12, "**Hard-to-vary.** For causal jobs"),
    (F12, "A tested model is underdetermined where an admitted rival agrees on the tests"),
    (SK, "A good explanation is hard to vary: you cannot change its parts and still have it explain what it is meant to explain."),
    (SK, "This skill is a way of criticising, not a truth-meter."),
    (D1, "How hard an account is to vary is a separate matter, shown by \\(\\operatorname{Pres}\\), and it grades nothing."),
    (D3, "how hard an account is to vary is a separate matter (Part VI)."),
    (D4, "**Commitments that do no work.**"),
    (D4, "A candidate is **easy to vary**, in the sense used here, when it and a rival pose a problem of the second kind; the rival is then easy to vary too, and the term says nothing about which of them is right."),
    (D4, "whether an account is easy to vary is a separate matter (Part VI)."),
    (D4, "from the candidate's own answer there, with no record of which candidates failed before or of how any was changed."),
    (D5, "and easy to vary on a problem for \\(p\\)."),
    (SC, "the term says nothing about which of them, and not the other, is an account on a finer contract."),
    (LT, "Nothing here counts rivals or orders candidates: of one candidate, what is said is whether it meets (E) on a contract and whether it is ruled out for an assessor; of two, whether they conflict; of a candidate and a claim, whether they conflict."),
    (LT, "whether anyone asks it is that person's choice (Part 0)."),
    (LT, "which one the person goes on with is the person's choice (Part 0)"),
    (LT, "no argument makes the choice."),
    (LT, "Nor are rivals a selection population"),
    (LT, "Construction is not selection. A selected transport has no represented target in its history; a constructed one does."),
    (LT, "For a declared family \\(\\mathcal V\\) of organization edits,"),
    (SA, "the term says nothing about which of them, and not the other, is an account on a finer contract."),
    (CL, "Here hard-to-vary is stated through rivals and problems, with no measure or count of variants (Part VI)."),
    (CL, "here it is shown only by offering the rival, which is the criticism."),
    (CL, "Here being easy to vary is relative to the question and symmetric between two rivals, and prefers neither"),
    (CL, "Deutsch calls criticism and experiment a selection (chapter 4, p.78). Here selection is blind: its history holds no represented target (Parts 0 and IV)."),
    (DEC, "A record is redundant. Once the explanation is rescued, the mistake shouldn't be able to creep back in. Good explanations make bad ones harder to fit by definition."),
    (DEC, "A variation is a competitor. Whether anyone can list all variations that still fit is beside the point. If two discovered variations fit, that constitutes a problem."),
    (DEC, "The skill isn't worth it."),
    (LES, "Rule: state hard to vary through discovered rivals and the problems they make, never through a listed set, an enumeration or a count of versions, and never as a grade;"),
]


def stretches(line):
    line = line.replace('\\"', "\x00")
    out = []
    for m in re.finditer(r'"([^"]*)"', line):
        out.append(m.group(1))
    for m in re.finditer(r"“([^”]*)”", line):
        out.append(m.group(1))
    return [x.replace("\x00", '"') for x in out]


def main():
    texts = corpus()
    whole = " \n ".join(texts.values())
    bad = 0
    for rel in CHECKED:
        with open(os.path.join(ROOT, rel), encoding="utf-8") as h:
            lines = h.read().split("\n")
        n = 0
        for i, line in enumerate(lines, 1):
            for s in stretches(line):
                if len(s) < 15 or s in BETWEEN:
                    continue
                n += 1
                if norm(s) not in whole:
                    bad += 1
                    print(f"NOT FOUND  {os.path.basename(rel)} L{i}: {s[:120]}")
        print(f"{os.path.basename(rel)}: {n} quoted stretches of 15 characters or more checked")
    src = " \n ".join(texts[p] for p in BOOK_SOURCES)
    for q, page in BOOK:
        w = len(q.replace("–", " ").replace("…", " ").split())
        found = norm(q) in src
        if w > 25 or not found:
            bad += 1
        print(f"BOOK {page}: {w} words, {'found' if found else 'NOT FOUND'}")
    for p, q in PLACED:
        if norm(q) not in texts.get(p, ""):
            bad += 1
            print(f"NOT IN FILE  {p}: {q[:100]}")
    print(f"PLACED: {len(PLACED)} attributions checked")
    print("ALL FOUND" if bad == 0 else f"{bad} PROBLEMS")
    return 0 if bad == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
