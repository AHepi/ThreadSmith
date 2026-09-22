"""Arm (d), the partition harness: the parts pass, the split, the assembler, and the leak gauge.

A RULE with a checking driver (`python3 partition.py --demo`).

W3 section 5's arm (d): "fresh calls, one per test of Step 5, each handed only the document,
the frozen question and the one test, and a final call handed the pile of answers to write the
report". W8 part B12 amends it: the arm "must split the parts under test across calls, as the
sketch's own sentence says ('A call handed one test and one part'), not only the tests."

So the arm needs a numbered parts list before the test calls, and no test call may hold all of
it. This rig makes it in one **parts pass** (steps 1 to 4, no test, no report), splits it into
groups, and hands each test call one test and one group. The parts pass is an addition of this
rig, not of W3, and it can absorb the arm's whole result if the reader writes its report there,
so it comes with a gauge: leak_check() reads the parts pass and reports every line that carries
cross-step material (a pulling pair, a rival, the same-explanation verdict, a mark). A run whose
parts pass leaks is reported, not silently counted.

The default split is `cross`: every test meets every group, so 11 tests x G groups calls.
The alternative, `rotate`, is 11 calls with the groups rotating; it is cheaper and each test
then meets only one group. `cross` with G=2 is a free choice of this rig and is marked loose in
the read-me: what would settle it is the phase plan's budget, which is not mine to fix.
"""
import re, sys


class Leak(Exception):
    """Raised by gate(): this run's parts pass carries cross-step material and is not counted."""


# The gauge, widened (fault 10 of the stage-A review) and made a gate.
#
# The first version keyed on the skill's own vocabulary, which is exactly the vocabulary
# SKILL.md tells the reader not to lean on ("Plain words, concrete verbs"): seven of ten
# realistic leaks the reviewer put to it passed. The plain-word forms of every cross-step
# verdict are named below beside the skill's own.
#
# What this patch gives up: a false alarm is read by a person, while a gauge that reports "no
# leak" on a leaking pass is read as evidence, so the gate is set the strict way round. Every
# flagged line is written into the stopped run's record, so a person can see which it was.
#
# *fixed* is deliberately not a mark word here: Step 2 of the procedure asks the reader to tag
# each job "given, fixed or added", so a parts pass says "fixed" as a matter of course.
#
# --------------------------------------------------------------------------------------------
# Three plain-word patterns, narrowed (fault 27 of the fix round's review).
#
# Fault 24's bill, arriving on the next case, which is what a patch does. Three of the
# plain-word patterns fired on the words a physical or narrative document puts in a reader's
# mouth, and a flagged parts pass stops the run, writes no record and is not counted, so a
# false alarm costs P4.3 a run from its denominator for a reason that is the rig's — fault 24's
# own ground. The four lines, all innocent, all flagged by the unnarrowed patterns:
#   "1. The paper sets Fresnel's account of aberration against the rival hypothesis of Stokes."
#   "2. The two rival hypotheses differ over whether the ether at the surface is carried along."
#   "10. The Crocodile pulls and the Elephant's Child pulls against him."
#   "6. A stronger drift would give a larger displacement; a weaker one, a smaller."
# W1 is the Michelson-Morley paper, whose whole argument sets Fresnel's account against
# Stokes's; W9's own text is a tug of war ("he pulled, and pulled, and pulled"). A Step 3 parts
# list and a Step 4 change list on those two arms documents are where such lines come from.
#
# Each word now counts only where it stands as the CROSS-STEP VERDICT, not where it is the
# document's own noun or the mechanism's own description:
#   rivals?          — the line opens with the word as a heading ("Rival:", "- **Rivals.**"),
#                      or "best|strongest|nearest|obvious" stands just before it, or the line
#                      also says the rival is ruled out / told apart / separated, or a build
#                      word stands within forty characters of it ("Build the best rival").
#   pull … against   — a part reference WRITTEN OUT ("part 2", "parts 3 and 4") stands in the
#   stronger/weaker    line. The line's own leading number does not count: that is what fault
#                      24 tripped on, and "10. The Crocodile pulls …" is numbered, not a part
#                      reference.
# The other patterns and the gate are unchanged. "Pairs that pull: 1 against 4" is caught by
# the unnarrowed first pattern, so the narrowed pull rule may let it through.
#
# What this gives up, and it is said in the read-me too: a rival built in a sentence that
# neither opens with the word nor uses one of those verbs ("Stokes's account is a rival to
# Fresnel's, and the fringe count would tell them apart" — caught, by *tell apart*; but
# "Stokes's account is a rival to Fresnel's" alone) is now caught by nothing; a pulling pair
# named without writing out a part number ("making the first stronger makes the second
# weaker") is caught by nothing; and a part written in words ("part two") is not a part
# reference to this rule. Against that: the separation clause still fires on a parts pass whose
# own document rules a rival out in its own words ("2. The rival hypothesis of Stokes is ruled
# out by the fringe count"), which is a false alarm this narrowing does not remove. The gate is
# set the strict way round on purpose and every flagged line is written into the stopped run's
# record, so a person can see which it was.
_PART_REF_WRITTEN = re.compile(r"(?i)\bparts?\s+\d{1,2}\b")
_PULL_AGAINST = re.compile(r"(?i)\bpull(s|ing)?\b[^.]{0,80}\bagainst\b")
_STRONGER_WEAKER = re.compile(
    r"(?i)\b(stronger|strengthen(s|ing|ed)?)\b[^.]{0,80}\b(weaker|weaken(s|ing|ed)?)\b"
    r"|\b(weaker|weaken(s|ing|ed)?)\b[^.]{0,80}\b(stronger|strengthen(s|ing|ed)?)\b")
# "Rival:", "- **Rivals.**", "1. Rival - the harbour works": the word, at the head of the line,
# with a heading's separator after it.
_RIVAL_HEADING = re.compile(
    r"(?i)^[\s>*_`#\-]*(?:\d{1,2}[.)\]][ \t]*)?[\s*_`]*rivals?\b[\s*_`]*[:.–—\-]")
_RIVAL_SUPERLATIVE = re.compile(r"(?i)\b(best|strongest|nearest|obvious)\b[^.]{0,20}\brivals?\b")
_RIVAL_WORD = re.compile(r"(?i)\brivals?\b")
# The verbs of the test itself: the rival is told from the thing under test.
_TOLD_APART = re.compile(r"(?i)\bruled? out\b|\brules out\b|\bruling out\b"
                         r"|\btells? (them|the two|us) apart\b|\btold apart\b"
                         r"|\bseparates?\b|\bseparated\b|\bsets? (them|the two) apart\b")
_BUILD_NEAR_RIVAL = re.compile(
    r"(?i)\b(buil[dt]s?|building|construct(s|ed|ing)?)\b[^.]{0,40}\brivals?\b"
    r"|\brivals?\b[^.]{0,40}\b(buil[dt]s?|building|construct(s|ed|ing)?)\b")


def _pull_against(s):
    """"pull … against" as a cross-step verdict: a part reference written out in the line."""
    return bool(_PULL_AGAINST.search(s) and _PART_REF_WRITTEN.search(s))


def _stronger_weaker(s):
    """Stronger/weaker as a cross-step verdict: a part reference written out in the line."""
    return bool(_STRONGER_WEAKER.search(s) and _PART_REF_WRITTEN.search(s))


def _rival_built(s):
    """"rival" where it is the test's own verdict, not the document's own noun."""
    if not _RIVAL_WORD.search(s):
        return False
    return bool(_RIVAL_HEADING.match(s) or _RIVAL_SUPERLATIVE.search(s)
                or _TOLD_APART.search(s) or _BUILD_NEAR_RIVAL.search(s))


#
# Three of the plain-word patterns below are narrowed the way fault 24's last rule was
# narrowed (fault 27 of the fix round's review); the predicates are defined just above the
# list and the reason is written there.
LEAK = [
    (r"(?i)\bpairs? that pull\b", "a pulling pair"),
    (_pull_against, "a pulling pair"),
    (_stronger_weaker, "a pulling pair, in plain words"),
    (r"(?i)\b(which|that)\s+gives\s+way\b|\bthe line is drawn\b|\bwhere the line is\b"
     r"|\bdrawn in the wrong place\b", "a pulling pair: which gives way, or where the line is"),
    (_rival_built, "a rival built"),
    (r"(?i)\bsame explanation\b|\bone explanation at (this|that) level\b"
     r"|\bthe same at (this|that) level\b", "the same-explanation verdict"),
    (r"(?i)\bnothing\b[^.]{0,80}\bseparates?\b|\bno (change|edit)\b[^.]{0,80}\bseparates?\b"
     r"|\bnothing\b[^.]{0,80}\btells the two apart\b|\bcannot be told apart\b",
     "the same-explanation verdict, in plain words"),
    (r"(?i)\btwo routes\b", "two routes to one job"),
    (r"(?i)\beither\b[^.]{0,80}\bdoes the job\b|\bcut either\b[^.]{0,80}\bsurvives\b"
     r"|\beach helps\b[^.]{0,40}\bneither is needed\b", "two routes to one job, in plain words"),
    (r"(?i)\bremove (them |the parts )?in groups\b|\bin pairs and groups\b",
     "remove in groups"),
    (r"(?i)\b(both|together)\b[^.]{0,60}\bthe job (goes|fails|is lost)\b"
     r"|\bremov\w+ both\b[^.]{0,60}\b(goes|fails|flat)\b", "remove in groups, in plain words"),
    (r"(?i)\bmark[:s]?\b[^.]{0,80}\b(held|loose|idle|borrowed|unknown|two routes)\b", "a mark"),
    (r"(?i)^\s*\|?\s*(held if|held|two routes|loose|idle|borrowed|unknown)\b", "a mark"),
]
# The last rule, narrowed (fault 24 of the fix round's review). Its first version flagged any
# mark word standing in a line that also named a numbered part. "held", "loose", "idle" and
# "unknown" are ordinary English about apparatus and evidence, and a numbered part's own line
# matches a part reference by its leading digit, so "1. The ether is held stationary while the
# earth moves through it." stopped an arm (d) run for a reason that was the rig's -- the same
# shape as the fault the gate was built to remove, and one that costs P4.3 a run from its
# denominator. A mark word now counts only where it stands as a VERDICT ON A PART, in one of
# two forms and nothing else:
#   (i)  it is the first word after a part reference and its separator -- "Part 1: held by
#        job 2. Part 2: loose.", "2. loose - any near neighbour would do", "Part 3 - unknown,
#        and this would settle it", "| 1 | held | ... |";
#   (ii) it is the whole content of a table cell -- "| A | held | ... |", the row-and-mark shape
#        a part-by-part table writes, which the first version missed altogether.
# Every other LEAK pattern above is unchanged, and so is the gate.
#
# What the narrowing gives up, both ways. A mark written as a sentence about a part ("Part 4 is
# idle", "I would mark part 2 loose") is caught by no rule here now: the wording that would catch
# it is the wording that fires on "the mirror is loose in its mounting". And (ii) still fires on
# an innocent cell: a Step 4 change-list table with an outcome column reading "unknown" is
# stopped, though nothing in it is a mark. Both are named in the read-me.
_MARKS = r"(held if|held|two routes|loose|idle|borrowed|unknown)"
# A part reference and its separator: "part 7" anywhere, or a number opening the line or the
# line's first table cell, then one of the separators a report puts between a part and its
# verdict (: . ) ] | = - en dash em dash).
VERDICT_ON_PART = re.compile(
    r"(?i)(?:\bparts?\s*\d{1,2}\b|^[ \t]*\|?[ \t]*\d{1,2}\b)"
    r"[ \t]*[:.)\]|=\u2013\u2014-][ \t]*" + _MARKS + r"(?![\w-])")
# A mark word that is the whole of a table cell, bare or emphasised.
CELL_MARK = re.compile(r"(?i)^[\s*`_]*" + _MARKS + r"[\s*`_.]*$")


def verdict_on_part(line):
    """The mark word where it stands as a verdict on a part, or None. Fault 24's rule."""
    m = VERDICT_ON_PART.search(line)
    if m:
        return m.group(1), "standing as the verdict on a part"
    if "|" in line:
        for cell in line.split("|"):
            c = CELL_MARK.match(cell)
            if c:
                return c.group(1), "alone in a table cell"
    return None


PART_LINE = re.compile(r"^\s*(?:part\s*)?(\d{1,2})\s*[.)\]:-]\s+(.{3,})$", re.I)


def parse_parts(reply):
    """The numbered parts the parts pass wrote. Deterministic: the longest run of lines
    numbered 1, 2, 3 ... in order. Fewer than two and the arm cannot be partitioned."""
    runs, cur, want = [], [], 1
    for raw in (reply or "").split("\n"):
        m = PART_LINE.match(raw.strip())
        if m and int(m.group(1)) == want:
            cur.append(re.sub(r"\s+", " ", m.group(2)).strip()); want += 1
        elif m and int(m.group(1)) == 1:
            if len(cur) > 1: runs.append(cur)
            cur, want = [re.sub(r"\s+", " ", m.group(2)).strip()], 2
        elif cur and not raw.strip():
            continue
    if len(cur) > 1:
        runs.append(cur)
    runs.sort(key=len)
    return runs[-1] if runs else []


def groups(parts, g=2):
    """Contiguous, near-equal groups, each a strict subset. Numbering is 1-based and kept."""
    n = len(parts)
    if n < 2:
        raise SystemExit(f"arm (d): the parts pass gave {n} part(s); nothing to partition. Nothing sent.")
    g = max(2, min(int(g), n))
    size = (n + g - 1) // g
    out = []
    for i in range(0, n, size):
        out.append([(j + 1, parts[j]) for j in range(i, min(i + size, n))])
    return [x for x in out if x]


def calls(parts, tests, g=2, mode="cross"):
    """(test_id, group_index, group) for every test call of arm (d)."""
    gs = groups(parts, g)
    if mode == "rotate":
        return [(t, i % len(gs), gs[i % len(gs)]) for i, t in enumerate(tests)]
    return [(t, gi, grp) for t in tests for gi, grp in enumerate(gs)]


def render_group(grp):
    return "\n".join(f"{n}. {text}" for n, text in grp)


def leak_check(reply):
    """The gauge on the parts pass. Returns a list of (what, line).

    A LEAK entry is a regular expression, or (fault 27) a predicate over the line where the
    plain word alone is not the verdict.
    """
    found = []
    for raw in (reply or "").split("\n"):
        s = raw.strip()
        if not s:
            continue
        hit = None
        for pat, what in LEAK:
            if pat(s) if callable(pat) else re.search(pat, s):
                hit = what
                break
        if hit is None:
            v = verdict_on_part(s)
            if v:
                hit = f"a mark ({v[0].lower()}) {v[1]}"
        if hit:
            found.append((hit, s[:160]))
    return found


def gate(leaks, rid=""):
    """The gate (fault 10). A parts pass that carries cross-step material has done in one
    context the work arm (d) exists to split, so the run is stopped and not counted. The
    flagged lines go into the stopped run's record for a person to read."""
    if leaks:
        raise Leak(f"{rid}: arm (d)'s parts pass carries cross-step material on "
                   f"{len(leaks)} line(s); the run is stopped and not counted. First: "
                   f"{leaks[0][0]} — {leaks[0][1][:100]!r}")
    return True


def pile(answers):
    """The pile the assembler is handed: every test call's answer, labelled, in a fixed order."""
    out = []
    for (test_id, gi, grp, text) in answers:
        out.append(f"--- answer: test {test_id}, parts {', '.join(str(n) for n, _ in grp)} ---\n{(text or '').strip()}")
    return "\n\n".join(out)


if __name__ == "__main__":
    demo = ("Step 3, the parts\n1. The yeast was alive.\n2. The dough was warm.\n3. There was sugar.\n"
            "4. The oven was hot enough.\nStep 4, the change list\n- cool the kitchen\n")
    ps = parse_parts(demo)
    print("parts:", ps)
    for t, gi, grp in calls(ps, ["remove", "swap"], g=2)[:4]:
        print(f"  call test={t} group={gi}: {[n for n, _ in grp]}")
    print("leak on a clean parts pass:", leak_check(demo))
    print("leak on a dirty parts pass:", leak_check(demo + "Part 2 and part 3 pull against each other. Mark: held"))
    print("\nthe ten lines the stage-A reviewer put to the first gauge:")
    for line in [
        "The best rival: the harbour works were the cause",
        "Pairs that pull: 1 against 4",
        "Remove them in groups: 2 and 3 together and the job goes",
        "Parts 2 and 3 are two routes to one job: cut either and the job survives",
        "Strengthening part 2 weakens part 3, and part 3 is where the line is drawn",
        "Nothing on the change list separates part 1 from a plainer account of the same closure",
        "Part 1: held by job 2. Part 2: loose.",
        "At this level the two accounts are the same explanation",
        "Either part 1 or part 4 does the job, so neither is needed alone",
        "Remove 2 and 3 together and the job fails",
    ]:
        got = leak_check(line)
        print(f"  {'CAUGHT ' + got[0][0] if got else 'MISSED':52} {line[:70]}")

    # Fault 24: the last rule fires on a verdict on a part and not on a part's own description.
    print("\nthe four verdict forms the fix-round reviewer put to the narrowed rule "
          "(all four must fire):")
    for line in [
        "Part 1: held by job 2. Part 2: loose.",
        "| A | held | job 2 holds it |",
        "2. loose \u2014 any near neighbour would do",
        "Part 3 - unknown, and this would settle it",
    ]:
        got = leak_check(line)
        print(f"  {'CAUGHT ' + got[0][0] if got else 'MISSED':52} {line[:70]}")
    print("\nthe five innocent lines of fault 24, a parts pass on a physical document "
          "(none may fire):")
    for line in [
        "1. The ether is held stationary while the earth moves through it.",
        "2. The two arms are held at the same length by the same slab of sandstone.",
        "1. The mirror is loose in its mounting, which the authors say they corrected.",
        "3. Whether the residual is real or idle noise is not settled by this run.",
        "3. The apparatus is sensitive enough; below one hundredth of a fringe the drift "
        "is unknown.",
    ]:
        got = leak_check(line)
        print(f"  {'FLAGGED ' + got[0][0] if got else 'clean':52} {line[:70]}")

    # Fault 27: the three plain-word patterns fire on the verdict and not on the document's own
    # noun or the mechanism's own description.
    print("\nthe seven cross-step verdicts of fault 27's three patterns (all must fire):")
    for line in [
        "Rival: the ether is dragged at the surface, which would give the same null result",
        "- **Rivals.** Stokes's drag, and a shortening of the arm itself.",
        "The strongest rival is a contraction of the stone in the direction of motion",
        "I built a rival account from the same two facts and it does every job",
        "The rival can be ruled out by turning the instrument through ninety degrees",
        "Part 2 and part 5 pull against each other, and part 5 gives way",
        "Making part 1 stronger makes part 4 weaker",
    ]:
        got = leak_check(line)
        print(f"  {'CAUGHT ' + got[0][0] if got else 'MISSED':52} {line[:70]}")
    print("\nthe seven innocent lines of fault 27, the document's own words "
          "(none may fire; the first four are the fault's own evidence):")
    for line in [
        "1. The paper sets Fresnel's account of aberration against the rival hypothesis "
        "of Stokes.",
        "2. The two rival hypotheses differ over whether the ether at the surface is "
        "carried along.",
        "10. The Crocodile pulls and the Elephant's Child pulls against him.",
        "6. A stronger drift would give a larger displacement; a weaker one, a smaller.",
        "4. The rival accounts of aberration were both current in 1887.",
        "5. The screw pulls the mirror against the casting until the fringes settle.",
        "7. A stronger source gives a brighter fringe and a weaker one a fainter.",
    ]:
        got = leak_check(line)
        print(f"  {'FLAGGED ' + got[0][0] if got else 'clean':52} {line[:70]}")
