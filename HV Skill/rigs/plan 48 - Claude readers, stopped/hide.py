"""Strip setup labels, shuffle with an unrecorded seed, number. Marker reads marking/to_mark.md and fills marking/marks.csv."""
import os, json, random, csv, re
HERE=os.path.dirname(os.path.abspath(__file__))
cases={c["id"]:c for c in json.load(open(f"{HERE}/cases.json"))}
recs=[]
for fn in sorted(os.listdir(f"{HERE}/replies")):
    m=re.match(r"c(.+)-([ABC])\.md$", fn)
    if m: recs.append({"run":fn[:-3],"case":m.group(1),"setup":m.group(2),"reply":open(f"{HERE}/replies/{fn}",encoding="utf-8").read()})
random.Random().shuffle(recs)
os.makedirs(f"{HERE}/marking",exist_ok=True)
mapping={}; md=["# Replies to mark (labels hidden)\n"]
with open(f"{HERE}/marking/marks.csv","w",newline="",encoding="utf-8") as f:
    w=csv.writer(f); w.writerow(["number","case","mark","change_YN","recall_or_test_RT","note"])
    for i,r in enumerate(recs,1):
        n=f"{i:03d}"; mapping[n]=r["run"]
        md.append(f"\n---\n\n## Reply {n} - case {r['case']} ({cases[r['case']]['name']})\n\n{r['reply'].strip()}\n")
        w.writerow([n,r["case"],"","","",""])
open(f"{HERE}/marking/to_mark.md","w",encoding="utf-8").write("\n".join(md))
json.dump(mapping,open(f"{HERE}/marking/secret_mapping.json","w"),indent=1)
print(len(recs),"replies hidden")
