"""Splice the drafted entries into a scratch copy of the change list (never the repository copy)."""
import pathlib, re
REPO = pathlib.Path("/home/user/ThreadSmith")
S = pathlib.Path("/tmp/claude-0/-home-user-ThreadSmith/8d9323da-c0ec-57ec-91fd-8f99ca99320a/scratchpad/rivals")
cl = (REPO / "Semantics/tests/Revision 2 - change list, draft of 23 September.md").read_text(encoding="utf-8")
head, sec = cl.split("\n## The entries\n", 1)
# the entries section runs to the next '## ' heading
m = re.search(r"(?m)^## (?!#)", sec)
entries_part, tail = sec[:m.start()], sec[m.start():]
blocks = re.split(r"(?m)^(?=### )", entries_part)
pre, blocks = blocks[0], blocks[1:]
def bid(b): return b.split(" — ", 1)[0][4:]
new = {}
theory = (S / "blocks_theory.md").read_text(encoding="utf-8")
for b in re.split(r"(?m)^(?=### )", theory):
    if b.startswith("### "):
        new[bid(b)] = b.rstrip("\n") + "\n\n"
new["W38.1"] = (S / "block_W38.1.md").read_text(encoding="utf-8").rstrip("\n") + "\n\n"
out = []
for b in blocks:
    i = bid(b)
    if i in ("W34.1", "W33.1", "W38.1"):
        # keep the original trailing blank-line layout
        out.append(new[i])
    else:
        out.append(b)
    if i == "W33.1":
        out.append(new["W59.1"])
    if i == "W31.1":
        out.append(new["W60.1"])
spliced = head + "\n## The entries\n" + pre + "".join(out) + tail
# normalise: exactly one blank line before each ### and before the next ## heading
spliced = re.sub(r"\n{3,}(?=### )", "\n\n", spliced)
(S / "cl_spliced.md").write_text(spliced, encoding="utf-8")
print("blocks before", len(blocks), "after", len(re.findall(r"(?m)^### ", spliced.split("\n## The entries\n",1)[1].split("\n## Layer 1")[0])))
