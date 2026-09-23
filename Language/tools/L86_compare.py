#!/usr/bin/env python3
"""L86_compare.py OLD NEW: compares a second-version report (OLD) with a third-version report (NEW) as plan L86's E3 and
E4 ask: the third version's two headed blocks are removed from NEW (the rule of L86_strip.py), the wall-clock field
`Slowest question: N.NN seconds.` is replaced by `Slowest question: (seconds).` in both, and the results are compared byte
for byte. Prints `SAME` or `DIFFERENT at line <n>:` with the two lines, and exits 0 or 1. Written 23 September 2026."""
import re, sys
HEAD = re.compile(r"^(\s*)(General lines that could (produce|reach) .*|Reached without the reason:.*)$")
def strip(text):
    out, depth = [], None
    for line in text.split("\n"):
        m = HEAD.match(line)
        if m: depth = len(m.group(1)); continue
        if depth is not None and line.strip() and (len(line) - len(line.lstrip(" "))) > depth: continue
        depth = None; out.append(line)
    return "\n".join(out)
norm = lambda t: re.sub(r"Slowest question: \d+\.\d+ seconds\.", "Slowest question: (seconds).", t)
old = norm(open(sys.argv[1]).read()); new = norm(strip(open(sys.argv[2]).read()))
if old == new: print("SAME"); sys.exit(0)
a, b = old.split("\n"), new.split("\n")
for i in range(max(len(a), len(b))):
    x = a[i] if i < len(a) else "<end>"; y = b[i] if i < len(b) else "<end>"
    if x != y: print("DIFFERENT at line %d:\n  old: %s\n  new: %s" % (i + 1, x, y)); break
sys.exit(1)
