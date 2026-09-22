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

LEAK = [
    (r"(?i)\bpull(s|ing)?\b.*\bagainst\b", "a pulling pair"),
    (r"(?i)\bpairs? that pull\b", "a pulling pair"),
    (r"(?i)\brival\b", "a rival built"),
    (r"(?i)\bsame explanation\b", "the same-explanation verdict"),
    (r"(?i)\bmark[:s]?\b.*\b(held|loose|idle|borrowed|unknown|two routes)\b", "a mark"),
    (r"(?i)^\s*\|?\s*(held if|held|two routes|loose|idle|borrowed|fixed|unknown)\b", "a mark"),
    (r"(?i)\bremove (them |the parts )?in groups\b", "remove in groups"),
]
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
    """The gauge on the parts pass. Returns a list of (what, line)."""
    found = []
    for raw in (reply or "").split("\n"):
        s = raw.strip()
        if not s:
            continue
        for pat, what in LEAK:
            if re.search(pat, s):
                found.append((what, s[:160]))
                break
    return found


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
