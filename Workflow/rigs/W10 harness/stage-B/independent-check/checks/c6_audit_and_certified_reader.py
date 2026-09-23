"""c6: W10.18 from the audit, as both workers read it; and agreement.py's --certified reader on the
file stage_b.py actually wrote.

  /home/user/.venvs/threadsmith/bin/python c6_audit_and_certified_reader.py

W10.18: no harness program computes it (stage_b.py has no W10.18 block, and no harness program
reads tool_audit.json or strikes a mark). Both workers read tool_audit.json. Explanation under test:
both read the same file and report the same numbers. It forbids any difference between the file
and either report. Rival: one worker read a different audit or miscounted. Check: read the file.

--certified: the harness worker found, on synthetic files, that agreement.py's reader
`c if isinstance(c, list) else (c.get("certified") or c.get("fields"))` takes every field when
stage B certifies none. Check here on the real file's shape, in memory: the real list, and the
same file with an empty list. Writes nothing.
"""
import os, re, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
RIG = os.path.normpath(os.path.join(HERE, "..", "..", ".."))
a = json.load(open(os.path.join(RIG, "stage-B", "tool_audit.json")))
IND = json.load(open(os.path.join(HERE, "..", "output.json")))["audit"]
pm = a["per_marker"]
odd = {k: v for k, v in pm.items() if (v.get("reads"), v.get("skill_files"), v.get("writes"), v.get("other")) != (8, 7, 1, 0)}
seen = {"markers": a["markers"], "strikes": len(a["strikes"]), "key_hits": a["key_hits"], "tools": a["tools"],
        "per_marker_rows": len(pm), "rows_not_8_7_1_0": odd, "M085_rerun": a["M085_rerun"]}
print("tool_audit.json, seen:", json.dumps(seen))
# the harness worker's return, as the orchestrator relayed it (claimed): markers 192, strikes [], key_hits 0,
# Read 1536, Write 191, StructuredOutput 191, M085 writes 0, rerun reads 8, reads_outside [], one write
claimed = {"markers": 192, "strikes": 0, "key_hits": 0, "tools": {"Read": 1536, "Write": 191, "StructuredOutput": 191},
           "M085_writes": 0, "rerun_reads": 8, "rerun_outside": 0, "rerun_writes": 1}
got = {"markers": a["markers"], "strikes": len(a["strikes"]), "key_hits": a["key_hits"], "tools": a["tools"],
       "M085_writes": pm["M085"]["writes"], "rerun_reads": a["M085_rerun"]["reads"],
       "rerun_outside": len(a["M085_rerun"]["reads_outside"]), "rerun_writes": len(a["M085_rerun"]["writes"])}
print("harness worker's return (claimed) equals the file:", claimed == got)
ind = {"markers": IND["markers_in_audit"], "strikes": len(IND["audit_strikes_list"]), "key_hits": IND["key_hits"],
       "tools": IND["tools"], "M085_writes": IND["rows_not_8_reads_7_skill_1_write_0_other"]["M085"]["writes"],
       "rerun_reads": IND["M085_rerun"]["reads"], "rerun_outside": len(IND["M085_rerun"]["reads_outside"]),
       "rerun_writes": len(IND["M085_rerun"]["writes"])}
print("independent output.json equals the file:", ind == got)
code = "".join(open(os.path.join(RIG, "code", f)).read() for f in os.listdir(os.path.join(RIG, "code")) if f.endswith(".py"))
print("any harness program reads tool_audit.json or strikes a mark:",
      bool(re.search(r"tool_audit|strike|struck", code, flags=re.I)))

sb = json.load(open(os.path.join(HERE, "harness-programs-on-a-scratch-copy", "stage_b_record96.json")))
reader = lambda c: c if isinstance(c, list) else (c.get("certified") or c.get("fields"))
got = reader(sb)
print(f"\nagreement.py's reader on the real file: {type(got).__name__} of {len(got)}; equals the certified list: {got == sb['certified']}")
empty = dict(sb, certified=[])
got0 = reader(empty)
print(f"the same file with an empty certified list: {type(got0).__name__} of {len(got0)} names "
      f"(the {len(sb['fields'])} comparable fields of stage_b.py's 'fields' map), not an empty list")
