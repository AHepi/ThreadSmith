import os, json, csv
from collections import defaultdict
HERE=os.path.dirname(os.path.abspath(__file__))
cases=json.load(open(f"{HERE}/cases.json")); order=[c["id"] for c in cases]
mapping=json.load(open(f"{HERE}/marking/secret_mapping.json"))
rows=list(csv.DictReader(open(f"{HERE}/marking/marks.csv",encoding="utf-8")))
miss=[r["number"] for r in rows if not r["mark"].strip()]
if miss: raise SystemExit(f"{len(miss)} unmarked: {miss[:6]}")
box={}
for r in rows:
    run=mapping[r["number"]]; case,setup=run[1:].rsplit("-",1)
    box[(case,setup)]=(r["mark"].strip(), r["change_YN"].strip().upper(), r["recall_or_test_RT"].strip().upper(), r["note"].strip())
def cell(c,s):
    v=box.get((c,s)); return f"{v[0]} ({v[1]}/{v[2]})" if v else "-"
print("| Case | Exercises | A: shape only | B: skill | C: skill + semantics |\n|---|---|---|---|---|")
for c in cases:
    print(f"| {c['id']} {c['name']} | {c['exercises']} | {cell(c['id'],'A')} | {cell(c['id'],'B')} | {cell(c['id'],'C')} |")
print("\nMark (change Y/N / recall R or test T)\n\nNotes:")
for c in cases:
    for s in "ABC":
        v=box.get((c["id"],s))
        if v and v[3]: print(f"- {c['id']}-{s}: {v[3]}")
json.dump({f"{k[0]}-{k[1]}":v for k,v in box.items()}, open(f"{HERE}/marking/marks_restored.json","w"), indent=1)
