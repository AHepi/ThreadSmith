#!/usr/bin/env python3
# ---------------------------------------------------------------------------
# sameness_2.py - the sameness test, second version.
#
# Made from: Language/tools/sameness.py, SHA-256 begins 9bb0534553397401.
# Built to: "L79 Test plan - Arm A, the ledgers in hand on the old rig and the
#   new, third version" (SHA-256 begins 2e97300690dc39f7), the `tools/
#   sameness_2.py` paragraph under "What is built", which reads in full:
#
#     **`tools/sameness_2.py`** from sameness.py (9bb0534553397401): a NOT on
#     one side only breaks a near pair and prints the pair under `OPPOSITE`;
#     exact match on token multisets; the buckets partition the lines; a near
#     partner is consumed. *Gives up:* the old counts, which overlapped.
#
# The plan numbers changes D1 to D8 and gives those numbers to the driver's
# changes only (`rigs/rig 1 - arguments/patched/run_check_2.py`). The
# sameness_2 paragraph carries no D-numbers, so its four changes are listed
# here in the plan's own order and wording, each with the paragraph's give-up
# line, which is one line and covers all four; it is copied whole under each.
#
#   Change 1 (the plan gives this file's changes no D-number):
#     "a NOT on one side only breaks a near pair and prints the pair under
#     `OPPOSITE`"
#     Gives up: the old counts, which overlapped.
#
#   Change 2 (the plan gives this file's changes no D-number):
#     "exact match on token multisets"
#     Gives up: the old counts, which overlapped.
#
#   Change 3 (the plan gives this file's changes no D-number):
#     "the buckets partition the lines"
#     Gives up: the old counts, which overlapped.
#
#   Change 4 (the plan gives this file's changes no D-number):
#     "a near partner is consumed"
#     Gives up: the old counts, which overlapped.
#
# Nothing else changes. sameness.py is untouched and stays runnable.
#
# Where the paragraph leaves a choice, the reading taken is the one that keeps
# every old finding's text byte-identical:
#
#   - A NOT counts when the word NOT stands alone in upper case in the line's
#     content, after the standing bracket is stripped. File 38 writes the
#     denial marker in upper case ("Put NOT on exactly what is denied, in
#     square brackets"); a lower-case "not" is ordinary prose, as in "response
#     to a press not stated", and does not break a pair.
#   - A pair broken by NOT is not re-paired against the next-best candidate:
#     the pair is what goes under OPPOSITE, and both of its lines are consumed,
#     as a near pair's two lines are.
#   - The NOT rule is not applied to an exact match, whose two sides carry the
#     same tokens by construction. It applies to near pairs, as the plan says.
#   - OPPOSITE is printed after NEAR and before BIN ENTRIES, so that every old
#     section keeps its old place, its old heading and its old rows. A pair
#     under OPPOSITE is printed in the full `line id [standing; mark; sentence
#     N] content` form on both sides, because those two lines no longer appear
#     under ONLY THE FIRST SAYS or ONLY THE SECOND SAYS and their ids would
#     otherwise be lost. NEAR keeps its old two-line form unchanged.
#   - SAME CONTENT, DIFFERENT STANDING keeps the meaning it has in the old
#     file: it re-lists matched pairs whose standing differs, and it is not one
#     of the buckets that partition the lines. The buckets that partition are
#     BOTH SAY, ONLY THE FIRST SAYS, ONLY THE SECOND SAYS, NEAR and OPPOSITE;
#     every line of either ledger falls in exactly one of them, and the program
#     stops with a message rather than print a report where it does not.
#   - The counts in the headings are the sizes of those buckets. They no longer
#     overlap, which is what the paragraph gives up.
# ---------------------------------------------------------------------------
"""The sameness test, written down as a program (Lesson 52).

What it does: reads two ledgers in the rig's .json form and lists
  - what both say         (same content, standing set aside)
  - what only the first says
  - what only the second says
  - where the same content carries a different standing
  - near matches, for the reader to judge by hand
  - opposite pairs: a near match with NOT on one side only
It compares the wording of lines, not their meaning. Two translators can
write one fact in two wordings; those land in "near" or in "only", and a
person decides. Say so whenever this output is quoted.

Every line of either ledger falls in exactly one of BOTH SAY, ONLY THE FIRST
SAYS, ONLY THE SECOND SAYS, NEAR and OPPOSITE; the counts do not overlap.

Usage: sameness_2.py A.json B.json [--near 0.5]
"""
import json, re, sys

STANDING = re.compile(r'^\s*\[(CLAIMED|GIVEN|SUPPOSED|TOLD)[^\]]*\]\s*', re.I)
# The ledger language's denial marker, upper case and standing alone (file 38:
# "Put NOT on exactly what is denied, in square brackets").
NOT_MARK = re.compile(r'(?<![A-Za-z0-9_])NOT(?![A-Za-z0-9_])')

def load(path):
    meta = json.load(open(path, encoding="utf-8"))
    rows = []
    for lid, info in meta["lines"].items():
        text = info.get("text", "")
        m = STANDING.match(text)
        standing = m.group(0).strip() if m else (info.get("standing") or "(none written)")
        content = STANDING.sub("", text)
        rows.append({"id": lid, "standing": standing, "content": content.strip(),
                     "mark": info.get("mark", "?"), "sentence": info.get("sentence", "?"),
                     "key": norm(content), "tokens": multiset(norm(content)),
                     "denies": bool(NOT_MARK.search(content))})
    return meta.get("paragraph", path), rows

def norm(s):
    s = s.lower()
    s = re.sub(r"[^a-z0-9 ]+", " ", s)
    s = re.sub(r"\b(the|a|an|is|are|was|were|of|to|its|it|that|this)\b", " ", s)
    return " ".join(s.split())

def multiset(key):
    """The tokens of a normalised content, with their multiplicity, order gone.
    Exact match compares these, not the normalised string."""
    return tuple(sorted(key.split()))

def jaccard(a, b):
    A, B = set(a.split()), set(b.split())
    return len(A & B) / len(A | B) if A | B else 0.0

def take(rows, row):
    """Consume a row from a bucket, by identity: two lines can carry the same
    fields and must still count as two lines."""
    for i, r in enumerate(rows):
        if r is row:
            del rows[i]
            return

def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    near_at = 0.5
    if "--near" in sys.argv: near_at = float(sys.argv[sys.argv.index("--near") + 1])
    if len(args) != 2: sys.exit(__doc__)
    (na, A), (nb, B) = load(args[0]), load(args[1])
    both, only_a, only_b, standing_diff, near, opposite = [], [], list(B), [], [], []
    for ra in A:
        hit = next((rb for rb in only_b if rb["tokens"] == ra["tokens"]), None)
        if hit:
            take(only_b, hit); both.append((ra, hit))
            if ra["standing"].split(",")[0].upper() != hit["standing"].split(",")[0].upper():
                standing_diff.append((ra, hit))
        else:
            only_a.append(ra)
    for ra in list(only_a):
        best = max(only_b, key=lambda rb: jaccard(ra["key"], rb["key"]), default=None)
        if best is None: break
        j = jaccard(ra["key"], best["key"])
        if j < near_at: continue
        take(only_a, ra); take(only_b, best)
        # A NOT on one side only breaks the pair: it goes under OPPOSITE, and
        # is not offered to the next-best candidate.
        (opposite if ra["denies"] != best["denies"] else near).append((ra, best, j))
    partition_or_stop(A, B, both, only_a, only_b, near, opposite)
    def show(r): return 'line %s [%s; %s; sentence %s] %s' % (r["id"], r["standing"], r["mark"], r["sentence"], r["content"])
    print("SAMENESS TEST: %s  against  %s" % (na, nb))
    print("(wording compared, not meaning; near matches and only-lines need a reader)\n")
    print("BOTH SAY (%d):" % len(both));            [print("  A " + show(a) + "\n  B " + show(b)) for a, b in both]
    print("\nONLY THE FIRST SAYS (%d):" % len(only_a)); [print("  " + show(r)) for r in only_a]
    print("\nONLY THE SECOND SAYS (%d):" % len(only_b)); [print("  " + show(r)) for r in only_b]
    print("\nSAME CONTENT, DIFFERENT STANDING (%d):" % len(standing_diff)); [print("  A %s  |  B %s  ::  %s" % (a["standing"], b["standing"], a["content"])) for a, b in standing_diff]
    print("\nNEAR, JUDGE BY HAND (%d, overlap >= %.2f):" % (len(near), near_at)); [print("  %.2f  A: %s\n        B: %s" % (j, a["content"], b["content"])) for a, b, j in near]
    print("\nOPPOSITE (%d, a near pair with NOT on one side only):" % len(opposite)); [print("  %.2f  A: %s\n        B: %s" % (j, show(a), show(b))) for a, b, j in opposite]
    la, lb = json.load(open(args[0]))["leftover"], json.load(open(args[1]))["leftover"]
    print("\nBIN ENTRIES: first %d, second %d (compare by reading)" % (len(la), len(lb)))

def partition_or_stop(A, B, both, only_a, only_b, near, opposite):
    """The buckets partition the lines: each line of either ledger is in one
    bucket and in one only. SAME CONTENT, DIFFERENT STANDING re-lists pairs
    already counted under BOTH SAY and is not one of the buckets."""
    placed = {"first":  [a for a, _ in both] + only_a + [p[0] for p in near] + [p[0] for p in opposite],
              "second": [b for _, b in both] + only_b + [p[1] for p in near] + [p[1] for p in opposite]}
    for side, rows in (("first", A), ("second", B)):
        got = [id(r) for r in placed[side]]
        if len(got) != len(set(got)) or set(got) != set(id(r) for r in rows):
            sys.exit("sameness_2: the buckets do not partition the %s ledger's lines "
                     "(%d line(s), %d placed); no report printed." % (side, len(rows), len(got)))

if __name__ == "__main__":
    main()
