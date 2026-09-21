"""Light marking by program (plan 52): shape, length, marks used, modules opened, for every run on disk."""
import os, re, json
HERE=os.path.dirname(os.path.abspath(__file__))
HEAD=[r"question,? frozen|frozen question|the question\b.*frozen", r"explanation in parts|the parts\b", r"part by part",
      r"whole[- ]explanation checks|flip|reverse|starting points", r"harder to vary|tighten", r"does not show|not the same as true", r"next step"]
MARKS=["held if","two routes","held","loose","idle","borrowed","fixed","unknown"]
TESTS=["remove","swap","flip","poke","reverse","starting point","add a job","rival","pull","patch","look inside"]
rows=[]
for fn in sorted(os.listdir(f"{HERE}/runs")):
    if not fn.endswith(".json"): continue
    r=json.load(open(f"{HERE}/runs/{fn}",encoding="utf-8")); rep=r["reply"]; low=rep.lower()
    heads=sum(1 for h in HEAD if re.search(h,low))
    marks=[m for m in MARKS if re.search(r"\b"+m+r"\b",low)]
    tests=[t for t in TESTS if t in low]
    shape="FULL" if heads>=6 and len(marks)>=3 else ("PART" if heads>=3 or marks else "NONE")
    rows.append(dict(run=fn[:-5], source=r["source"], mode=r["mode"], words=len(rep.split()), shape=shape,
                     headings=heads, marks=len(marks), tests_named=len(tests), modules=r.get("modules_opened",[]),
                     tool_calls=r.get("tool_calls",0), seconds=r["seconds"], thinking_words=len(r["reasoning"].split())))
json.dump(rows,open(f"{HERE}/marking/shape_by_program.json","w"),indent=1)
from collections import defaultdict
agg=defaultdict(list)
for x in rows: agg[x["mode"]].append(x)
print(f"{len(rows)} runs on disk")
for m in sorted(agg):
    xs=agg[m]; sh={s:sum(1 for x in xs if x['shape']==s) for s in ('FULL','PART','NONE')}
    print(f"mode {m}: n={len(xs)} shape {sh} | words avg {sum(x['words'] for x in xs)//len(xs)} | marks avg {sum(x['marks'] for x in xs)/len(xs):.1f} | tests named avg {sum(x['tests_named'] for x in xs)/len(xs):.1f}")
if agg.get(2):
    from collections import Counter
    c=Counter(mod for x in agg[2] for mod in x["modules"]); print("modules opened in mode 2:", dict(c))
    print("mode 2 runs with no module opened:", sum(1 for x in agg[2] if not x['modules']))
