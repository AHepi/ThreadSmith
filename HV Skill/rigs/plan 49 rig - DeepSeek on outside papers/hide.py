"""Close marking (plan 52): for the drawn sample, strip mode labels and module lists from modes 1 and 2,
shuffle with an unrecorded seed, number. Mode 0 reports are listed too but cannot be hidden (plan 52 says so)."""
import os, json, random, csv
HERE=os.path.dirname(os.path.abspath(__file__))
sample=json.load(open(f"{HERE}/close_marking_sample.json"))["sample"]
recs=[]
for s in sample:
    for m in (0,1,2):
        p=f"{HERE}/runs/{s}-m{m}.json"
        if os.path.exists(p):
            r=json.load(open(p,encoding="utf-8")); recs.append({"run":f"{s}-m{m}","source":s,"mode":m,"reply":r["reply"]})
random.Random().shuffle(recs)
md=["# Close-marking sample, labels hidden (plan 52)\n"]; mapping={}
with open(f"{HERE}/marking/marks.csv","w",newline="",encoding="utf-8") as f:
    w=csv.writer(f); w.writerow(["number","source","shape","tests_RAN","tests_NAME_ONLY","tests_ABSENT","tests_CANNOT",
                                 "claims_SUPPORTED","claims_MISREAD","claims_OUTSIDE","verdict","breaks","by_testing_YN","turned_own_test_YN","control_mark","note"])
    for i,r in enumerate(recs,1):
        n=f"{i:03d}"; mapping[n]=r["run"]
        md.append(f"\n---\n\n## Report {n} - source {r['source']}\n\n{r['reply'].strip()}\n")
        w.writerow([n,r["source"]]+[""]*14)
open(f"{HERE}/marking/to_mark.md","w",encoding="utf-8").write("\n".join(md))
json.dump(mapping,open(f"{HERE}/marking/secret_mapping.json","w"),indent=1)
print(len(recs),"reports hidden and numbered")
