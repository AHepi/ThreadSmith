"""Strip the setup labels, shuffle, number. Writes marking/to_mark.md and marking/marks.csv for the marker,
and marking/secret_mapping.json, which the marker does not open."""
import os, json, random, csv
HERE = os.path.dirname(os.path.abspath(__file__))
passages = {c["id"]: c for c in json.load(open(os.path.join(HERE, "passages.json"), encoding="utf-8"))}
for c in json.load(open(os.path.join(HERE, "reworded.json"), encoding="utf-8")): passages[c["id"]] = c
recs = []
for fn in sorted(os.listdir(os.path.join(HERE, "replies"))):
    if fn.endswith(".json"): recs.append(json.load(open(os.path.join(HERE, "replies", fn), encoding="utf-8")))
random.Random().shuffle(recs)        # a fresh, unrecorded seed: the order tells the marker nothing
os.makedirs(os.path.join(HERE, "marking"), exist_ok=True)
mapping, md = {}, ["# Replies to mark\n\nLabels hidden. Mark each against keys.json for its case.\n"]
with open(os.path.join(HERE, "marking", "marks.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f); w.writerow(["number", "case", "mark", "reason_as_change", "note"])
    for i, r in enumerate(recs, 1):
        n = f"{i:03d}"
        mapping[n] = {"run_id": r["run_id"], "setup": r["setup"], "repeat": r["repeat"], "case": r["case"]}
        md.append(f"\n---\n\n## Reply {n} - case {r['case']} ({passages[r['case']]['name']})\n\n{r['reply'].strip()}\n")
        w.writerow([n, r["case"], "", "", ""])
open(os.path.join(HERE, "marking", "to_mark.md"), "w", encoding="utf-8").write("\n".join(md))
json.dump(mapping, open(os.path.join(HERE, "marking", "secret_mapping.json"), "w"), indent=1)
print(len(recs), "replies hidden and numbered")
