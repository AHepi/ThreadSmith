#!/usr/bin/env python3
"""L86_strip.py REPORT: prints the report with the third driver's two headed blocks removed (plan L86, "What is built",
last paragraph): every line matching the block headings and every line that follows one of them indented deeper than
the heading, until the indentation returns. With no such block the report is printed unchanged. Written 23 September 2026."""
import re, sys
HEAD = re.compile(r"^(\s*)(General lines that could (produce|reach) .*|Reached without the reason:.*)$")
out, depth = [], None
for line in open(sys.argv[1]).read().split("\n"):
    m = HEAD.match(line)
    if m: depth = len(m.group(1)); continue
    if depth is not None and line.strip() and (len(line) - len(line.lstrip(" "))) > depth: continue
    depth = None; out.append(line)
sys.stdout.write("\n".join(out))
