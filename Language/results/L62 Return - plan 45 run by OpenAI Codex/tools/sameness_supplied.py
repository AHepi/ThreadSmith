#!/usr/bin/env python3
"""The sameness test, written down as a program (Lesson 52).

What it does: reads two ledgers in the rig's .json form and lists
  - what both say         (same content, standing set aside)
  - what only the first says
  - what only the second says
  - where the same content carries a different standing
  - near matches, for the reader to judge by hand
It compares the wording of lines, not their meaning. Two translators can
write one fact in two wordings; those land in "near" or in "only", and a
person decides. Say so whenever this output is quoted.

Usage: sameness.py A.json B.json [--near 0.5]
"""
import json, re, sys

STANDING = re.compile(r'^\s*\[(CLAIMED|GIVEN|SUPPOSED|TOLD)[^\]]*\]\s*', re.I)

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
                     "key": norm(content)})
    return meta.get("paragraph", path), rows

def norm(s):
    s = s.lower()
    s = re.sub(r"[^a-z0-9 ]+", " ", s)
    s = re.sub(r"\b(the|a|an|is|are|was|were|of|to|its|it|that|this)\b", " ", s)
    return " ".join(s.split())

def jaccard(a, b):
    A, B = set(a.split()), set(b.split())
    return len(A & B) / len(A | B) if A | B else 0.0

def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    near_at = 0.5
    if "--near" in sys.argv: near_at = float(sys.argv[sys.argv.index("--near") + 1])
    if len(args) != 2: sys.exit(__doc__)
    (na, A), (nb, B) = load(args[0]), load(args[1])
    both, only_a, only_b, standing_diff, near = [], [], list(B), [], []
    for ra in A:
        hit = next((rb for rb in only_b if rb["key"] == ra["key"]), None)
        if hit:
            only_b.remove(hit); both.append((ra, hit))
            if ra["standing"].split(",")[0].upper() != hit["standing"].split(",")[0].upper():
                standing_diff.append((ra, hit))
        else:
            only_a.append(ra)
    for ra in list(only_a):
        best = max(only_b, key=lambda rb: jaccard(ra["key"], rb["key"]), default=None)
        if best and jaccard(ra["key"], best["key"]) >= near_at:
            near.append((ra, best, jaccard(ra["key"], best["key"])))
    def show(r): return 'line %s [%s; %s; sentence %s] %s' % (r["id"], r["standing"], r["mark"], r["sentence"], r["content"])
    print("SAMENESS TEST: %s  against  %s" % (na, nb))
    print("(wording compared, not meaning; near matches and only-lines need a reader)\n")
    print("BOTH SAY (%d):" % len(both));            [print("  A " + show(a) + "\n  B " + show(b)) for a, b in both]
    print("\nONLY THE FIRST SAYS (%d):" % len(only_a)); [print("  " + show(r)) for r in only_a]
    print("\nONLY THE SECOND SAYS (%d):" % len(only_b)); [print("  " + show(r)) for r in only_b]
    print("\nSAME CONTENT, DIFFERENT STANDING (%d):" % len(standing_diff)); [print("  A %s  |  B %s  ::  %s" % (a["standing"], b["standing"], a["content"])) for a, b in standing_diff]
    print("\nNEAR, JUDGE BY HAND (%d, overlap >= %.2f):" % (len(near), near_at)); [print("  %.2f  A: %s\n        B: %s" % (j, a["content"], b["content"])) for a, b, j in near]
    la, lb = json.load(open(args[0]))["leftover"], json.load(open(args[1]))["leftover"]
    print("\nBIN ENTRIES: first %d, second %d (compare by reading)" % (len(la), len(lb)))

if __name__ == "__main__":
    main()
