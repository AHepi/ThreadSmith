"""After marks.csv is filled in: restore the labels and print the table, case by setup, three marks a box."""
import os, json, csv
from collections import defaultdict
HERE = os.path.dirname(os.path.abspath(__file__))
mapping = json.load(open(os.path.join(HERE, "marking", "secret_mapping.json")))
keys = {k["id"]: k for k in json.load(open(os.path.join(HERE, "keys.json"), encoding="utf-8"))}
rew = {c["id"]: c for c in json.load(open(os.path.join(HERE, "reworded.json"), encoding="utf-8"))}
rows = list(csv.DictReader(open(os.path.join(HERE, "marking", "marks.csv"), encoding="utf-8")))
missing = [r["number"] for r in rows if not r["mark"].strip()]
if missing: raise SystemExit(f"{len(missing)} replies still unmarked, e.g. {missing[:5]}. Table not printed.")
box = defaultdict(list); change = defaultdict(lambda: [0, 0])
for r in rows:
    m = mapping[r["number"]]
    box[(m["case"], m["setup"])].append((m["repeat"], r["mark"].strip().upper()))
    c = r["reason_as_change"].strip().upper()
    if c in ("Y", "N"): change[m["setup"]][c == "Y"] += 1
def cell(case, s):
    return " / ".join(mk for _, mk in sorted(box.get((case, s), []))) or "-"
order = [k for k in keys if k[0] != "C"] + [k for k in keys if k[0] == "C"]
print("| Case | Role | Setup 0 | Setup 1 | Setup 2 | Setup 3 |\n|---|---|---|---|---|---|")
for cid in order:
    k = keys[cid]
    print(f"| {cid} {k['name']} | {k['role']} | " + " | ".join(cell(cid, s) for s in range(4)) + " |")
print("\nReworded cases (one run each; should match the marks of the case they reword)\n")
print("| Case | Rewords | Setup 0 | Setup 1 | Setup 2 | Setup 3 |\n|---|---|---|---|---|---|")
for cid, c in rew.items():
    print(f"| {cid} | {c['of']} | " + " | ".join(cell(cid, s) for s in range(4)) + " |")
print("\nReason given as a change someone could make (Y) rather than a story (N), per setup:")
for s in range(4):
    n, y = change[s]; print(f"  setup {s}: Y {y}, N {n}")
dis = [(c, s) for (c, s), v in box.items() if len(v) == 3 and len({mk for _, mk in v}) > 1]
print(f"\nBoxes where the three repeats disagree: {len(dis)} of {sum(1 for v in box.values() if len(v)==3)}")
for c, s in sorted(dis): print(f"  case {c}, setup {s}: {cell(c, s)}")
