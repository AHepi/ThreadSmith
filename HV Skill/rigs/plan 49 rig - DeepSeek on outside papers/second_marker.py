"""Plan H63: blind second marking by Sonnet 5 subagents.
  python3 second_marker.py prep <scratch>                 # builds <scratch>/marking2/: rules, texts, skill, hidden reports (set 1 from
                                                          #   marking/to_mark.md; set 2 the 48 repeat reports, shuffled, mapping saved)
  python3 second_marker.py compare <scratch> <journal>    # reads the workflow journal, aligns with the first marker's marks, prints agreement
Sends nothing itself."""
import os, sys, json, re, random, shutil
HERE = os.path.dirname(os.path.abspath(__file__))
TESTS = ["remove", "swap", "flip", "poke", "reverse", "hunt", "addjob", "rival", "pull", "patches", "inside"]

def joined(text):
    return "\n\n".join(re.sub(r"\s*\n\s*", " ", p).strip() for p in re.split(r"\n\s*\n", text) if p.strip())

def prep(scratch):
    base = f"{scratch}/marking2"
    for d in ("rules", "texts", "p49", "rep"): os.makedirs(f"{base}/{d}", exist_ok=True)
    proj = os.path.normpath(f"{HERE}/../..")
    shutil.copy(f"{proj}/tests/52 Marking plan - frozen before the corpus is read.md", f"{base}/rules/plan52.md")
    h56 = open(f"{proj}/tests/H56 Plan - repeatability of the two breaks, P3 and F4 three runs each.md", encoding="utf-8").read()
    q = h56.split("## The question", 1)[1].split("## What is fixed", 1)[0]
    c = h56.split("## What counts as a recurrence, decided before reading", 1)[1].split("## Predictions", 1)[0]
    open(f"{base}/rules/h56_criteria.md", "w", encoding="utf-8").write(
        "# Marking criteria for the repeat reports (from plan H56, frozen before any run)\n\n## The two breaks being looked for\n" + q +
        "\n## What counts as a recurrence, decided before reading\n" + c)
    if os.path.isdir(f"{base}/skill30"): shutil.rmtree(f"{base}/skill30")
    shutil.copytree(f"{proj}/authority/hard-to-vary", f"{base}/skill30/hard-to-vary")
    sample = json.load(open(f"{HERE}/close_marking_sample.json"))["sample"]
    for s in sample:
        t = open(f"{HERE}/corpus/{s}.txt", encoding="utf-8").read().split("\n\n", 1)[1]
        open(f"{base}/texts/{s}.txt", "w", encoding="utf-8").write(joined(t))
    # set 1: split to_mark.md
    md = open(f"{HERE}/marking/to_mark.md", encoding="utf-8").read()
    parts = re.split(r"\n---\n\n## Report (\d{3}) - source (\S+)\n", md)
    n1 = 0
    for i in range(1, len(parts), 3):
        num, src, body = parts[i], parts[i+1], parts[i+2]
        open(f"{base}/p49/{num}.md", "w", encoding="utf-8").write(f"## Report {num} - source {src}\n{body.strip()}\n"); n1 += 1
    # set 2: the 48 repeat reports, hidden
    recs = []
    for folder in ("runs_repeat", "runs_repeat_31", "runs_sonnet5", "runs_sonnet5_31"):
        for fn in sorted(os.listdir(f"{HERE}/{folder}")):
            if fn.endswith(".json") and not fn.startswith("shape"):
                r = json.load(open(f"{HERE}/{folder}/{fn}", encoding="utf-8"))
                recs.append({"run": f"{folder}/{fn[:-5]}", "source": r["source"], "reply": r["reply"]})
    random.Random().shuffle(recs)
    mapping = {}
    for i, r in enumerate(recs, 1):
        num = f"R{i:02d}"; mapping[num] = r["run"]
        open(f"{base}/rep/{num}.md", "w", encoding="utf-8").write(f"## Report {num} - source {r['source']}\n\n{r['reply'].strip()}\n")
    json.dump(mapping, open(f"{HERE}/marking/secret_mapping_repeat.json", "w"), indent=1)
    print(f"set 1: {n1} reports; set 2: {len(recs)} reports hidden as R01..R{len(recs):02d}; texts: {len(sample)}")

def compare(scratch, journal):
    labels, results = {}, {}
    for line in open(journal):
        d = json.loads(line)
        if d.get("type") == "started": labels[d["agentId"]] = d["label"]
        if d.get("type") == "result": results[labels.get(d["agentId"], d["agentId"])] = d["result"]
    first = {r["number"]: r for r in json.load(open(f"{HERE}/marking/close_marks_restored.json"))}
    mapping1 = json.load(open(f"{HERE}/marking/secret_mapping.json"))
    out = {"set1": {}, "set2": {}}
    # set 1
    shape = yn1 = yn2 = ctrl = 0; cells = ran = 0; cannot = []; breaks = {}
    for num, f in sorted(first.items()):
        s = results.get(f"p49:{num}")
        if not s: continue
        row = {"run": f["run"], "first": f, "second": s}
        out["set1"][num] = row
        shape += f["shape"] == s.get("shape")
        yn1 += (f["by_testing"] == "Y") == bool(s.get("by_testing") == "Y")
        yn2 += (f["turned_own_test"] == "Y") == bool(s.get("turned_own_test") == "Y")
        ctrl += (f.get("control_mark") or "") == (s.get("control_mark") or "")
        for t in TESTS:
            a, b = f["tests"].get(t), (s.get("tests") or {}).get(t)
            cells += 1; ran += (a == "RAN") == (b == "RAN")
            if b == "CANNOT": cannot.append((num, f["run"], t))
        if f["breaks"] or s.get("breaks"):
            breaks[num] = {"run": f["run"], "first": f["breaks"], "second": s.get("breaks")}
    n = len(out["set1"])
    print(f"SET 1: {n} reports compared")
    print(f"  shape agree {shape}/{n}; by_testing agree {yn1}/{n}; turned_own_test agree {yn2}/{n}; control mark agree {ctrl}/{n}")
    print(f"  tests RAN-vs-not agree {ran}/{cells} ({100*ran/max(cells,1):.0f}%)")
    print(f"  second marker CANNOT cells: {len(cannot)} {cannot}")
    print(f"  reports with a break from either marker: {len(breaks)}")
    for num, b in breaks.items():
        print(f"    {num} {b['run']}: first={len(b['first'])} second={len(b['second'] or [])}")
    # set 2
    mapping2 = json.load(open(f"{HERE}/marking/secret_mapping_repeat.json"))
    fm = json.load(open(f"{HERE}/marking/first_marker_repeat_marks.json"))
    b1 = b2 = same = shp = 0; rows = []
    for num, run in sorted(mapping2.items()):
        s = results.get(f"rep:{num}"); f = fm.get(run)
        if not s or not f: continue
        src = run.split("/")[1][:2]
        r = {"num": num, "run": run, "first": f, "second": s}
        out["set2"][num] = r; rows.append(r)
        shp += s.get("shape") == "FULL"
        if src == "P3": b1 += bool(s.get("break1_recurs")) == bool(f["break1_recurs"])
        if src == "F4": b2 += bool(s.get("break2_recurs")) == bool(f["break2_recurs"])
        same += bool(s.get("same_explanation")) == bool(f["same_explanation"])
    print(f"SET 2: {len(rows)} reports compared; second marker FULL {shp}/{len(rows)}; break1 agree {b1}/24; break2 agree {b2}/24; same-explanation agree {same}/{len(rows)}")
    for r in rows:
        s, f = r["second"], r["first"]
        flag = ""
        if bool(s.get("break1_recurs")) != bool(f["break1_recurs"]) and r["run"].split("/")[1].startswith("P3"): flag += " BREAK1-DISAGREE"
        if bool(s.get("break2_recurs")) != bool(f["break2_recurs"]) and r["run"].split("/")[1].startswith("F4"): flag += " BREAK2-DISAGREE"
        if s.get("break1_recurs") or s.get("break2_recurs"): flag += " second-flags"
        if flag: print(f"    {r['num']} {r['run']}: second b1={s.get('break1_recurs')} b2={s.get('break2_recurs')} flip={s.get('flip_status')} |{flag}")
    json.dump(out, open(f"{HERE}/marking/second_marker_comparison.json", "w"), indent=1, ensure_ascii=False)
    print("written marking/second_marker_comparison.json")

if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "prep": prep(sys.argv[2])
    else: compare(sys.argv[2], sys.argv[3])
