# Check every double-quoted string in Mimo's F3 reply against the theory text (file 10)
# and, failing that, against the F3 brief (the finding's own words).
import re
S = "/tmp/claude-0/-home-user-ThreadSmith/8d9323da-c0ec-57ec-91fd-8f99ca99320a/scratchpad/s88m/"
R = "/home/user/ThreadSmith/Semantics/results/S88 Cross-examination - three defects - returns/Mimo in three parts/s88_xexam_mimo_F3.response.txt"
B = "/home/user/ThreadSmith/Semantics/tests/S88 Cross-examination - part F3, non-circular dependence.md"
theory = open(S + "f3_theory.txt").read().split("\n")
brief = open(B).read()
reply = open(R).read()
def norm(s):
    s = s.replace("…", "...")
    s = re.sub(r"\s+", " ", s)
    return s.strip()
tl = [norm(l) for l in theory]
bn = norm(brief)
quotes = re.findall(r'"([^"]{6,})"', reply)
for q in quotes:
    parts = [norm(p) for p in re.split(r"\.\.\.|…|\\\[[^\]]*\\\]|\[[^\]]*\]", q) if len(norm(p)) > 3]
    hits = []
    for p in parts:
        ln = [i + 1 for i, l in enumerate(tl) if p in l]
        hits.append((p[:50], ln if ln else ("BRIEF" if p in bn else "NOT FOUND")))
    print("Q:", q[:90].replace("\n", " "))
    for h in hits:
        print("    ", h)
