"""c2: which reports count as "read" for W10.16, as the harness finds them and as the independent does.

  /home/user/.venvs/threadsmith/bin/python c2_read_sets.py

Explanation under test: the two programs' W10.16 numbers differ because they read W14 section 3's
"the record files named anywhere in criteria.json and marking-plan.md ... mapped to run ids by set"
two ways (the harness: folder-qualified names ending in .json; the independent's primary: those
plus the adapted run ids that marking-plan section 14.1 names directly), and because they divide
by different bases. It forbids any difference in the agreement counts on the same read set.
Rival: the two programs pair or compare the marks differently on the read reports. Separating
check: c1's cause rows (the harness's split equals the independent's reading A exactly, on the
readable basis). This file adds what the harness's own pattern catches, and what it leaves out.
Writes nothing.
"""
import os, re, sys, json
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
RIG = os.path.normpath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(RIG, "code"))
import stage_b as SB  # the harness's read_reports(), read only; importing it runs nothing

IND = json.load(open(os.path.join(HERE, "..", "output.json")))
harness = SB.read_reports()
text = "".join(open(os.path.join(RIG, "instrument", fn), encoding="utf-8").read()
               for fn in ("criteria.json", "marking-plan.md"))
A = set(IND["read_reports"]["A_record_file_names_only"])
Bp = set(IND["read_reports"]["B_record_file_names_and_run_ids (primary)"])
D = set(IND["read_reports"]["D_W13_marking_plan_sections_13_to_15_only"])
print(f"harness read_reports(): {len(harness)}; independent A {len(A)}, B {len(Bp)}, D {len(D)}")
print(f"  harness == A: {harness == A};  harness == D: {harness == D}")
print(f"  in B and not in the harness's set ({len(Bp - harness)}): {sorted(Bp - harness)}")

# 1. The harness's pattern needs '.json'. Does any folder-qualified name appear only without it?
with_json = set(re.findall(r"(runs[a-z0-9_]*)/([A-Za-z0-9_-]+)\.json", text))
without = set(re.findall(r"(runs[a-z0-9_]*)/([A-Za-z0-9_-]+)(?![A-Za-z0-9_.-])", text))
only_without = sorted(x for x in without - with_json if x[0] in SB.FOLDER_TAG and x[1] != "X")
print(f"\nfolder-qualified names written only without '.json' (the harness's pattern would miss them): {only_without}")

# 2. Adapted run ids written directly in the two files (the independent's B adds these)
ids = sorted(set(re.findall(r"\b((?:p52|rep31|rep|son31|son)_[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*)", text)))
print(f"adapted run ids written directly in the two files ({len(ids)}): {ids}")
for rid in ids:
    where = [m.start() for m in re.finditer(re.escape(rid), text)]
    print(f"    {rid}: {len(where)} occurrence(s); among the harness's read set: {rid in harness}")

# 3. How the two texts word the rule
for fn, pat in (("Workflow/tests/W14 Plan - stage B, the instrument certified on the 96 reports by two blind Sonnet 5 markers.md", r"The reports any maker[^\n]*"),
                ("Workflow/tests/W13 Addendum to W10 - the fix loop runs until no fault is found, every round a saved version (decision W11).md", r"over the reports no maker[^)]*\)")):
    t = open(os.path.join(RIG, "..", "..", "..", fn), encoding="utf-8").read()
    m = re.search(pat, t)
    print(f"\n{fn.split('/')[-1][:4]}: {m.group(0)[:330] if m else 'NOT FOUND'}")
