"""03a: put the proposed fixes into a copy of rivals/cl_spliced.md (never the repository copy)."""
import pathlib, re
S = pathlib.Path(__file__).resolve().parent
cl = (S.parent / "cl_spliced.md").read_text(encoding="utf-8")

def replace_new(text, entry_id, new_body):
    i = text.index("### %s — " % entry_id)
    j = text.index("- **NEW:**\n````text\n", i) + len("- **NEW:**\n````text\n")
    k = text.index("\n````\n", j)
    return text[:j] + new_body.rstrip("\n") + text[k:]

cl = replace_new(cl, "W59.1", (S / "fixed_W59.txt").read_text(encoding="utf-8"))
cl = replace_new(cl, "W60.1", (S / "fixed_W60.txt").read_text(encoding="utf-8"))
# W36.1 companion: 'how hard an account is to vary' -> 'whether an account is easy to vary', in its NEW only
i = cl.index("### W36.1 — ")
j = cl.index("- **NEW:**\n````text\n", i); k = cl.index("\n````\n", j)
seg = cl[j:k]
assert seg.count("how hard an account is to vary") == 1
cl = cl[:j] + seg.replace("how hard an account is to vary", "whether an account is easy to vary") + cl[k:]
# W38.1: the four lines
i = cl.index("### W38.1 — ")
j = cl.index("- **NEW:**\n````text\n", i); k = cl.index("\n````\n", j)
seg = cl[j:k]
for line in (S / "fixed_W38_lines.txt").read_text(encoding="utf-8").splitlines():
    tag = line.split(".*", 1)[0] if False else line[:line.index("*", 3) + 1]  # '- *Explanation*' etc
    old = [l for l in seg.splitlines() if l.startswith(tag)]
    assert len(old) == 1, (tag, len(old))
    seg = seg.replace(old[0], line)
cl = cl[:j] + seg + cl[k:]
(S / "cl_fixed.md").write_text(cl, encoding="utf-8")
print("written", S / "cl_fixed.md")
