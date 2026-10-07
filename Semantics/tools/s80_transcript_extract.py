#!/usr/bin/env python3
"""s80_transcript_extract.py: from a subagent's JSONL transcript, write only its tool calls and their inputs, one per
line, for the Opus arm's contamination scan (plan S80, second version, "Points settled by the orchestrator"). The
preamble, the prompt and the tool results are left out, so the scan reads what the agent did, not what it was told.
  python Semantics/tools/s80_transcript_extract.py TRANSCRIPT.jsonl OUT.txt
"""
import json, sys

out = []
for line in open(sys.argv[1], encoding="utf-8"):
    try:
        d = json.loads(line)
    except Exception:
        continue
    if d.get("type") != "assistant":
        continue
    c = (d.get("message") or {}).get("content")
    if not isinstance(c, list):
        continue
    for b in c:
        if b.get("type") == "tool_use":
            out.append("%s %s" % (b.get("name"), json.dumps(b.get("input"), ensure_ascii=False)))
open(sys.argv[2], "w", encoding="utf-8").write("\n".join(out) + "\n")
print(len(out), "tool calls")
