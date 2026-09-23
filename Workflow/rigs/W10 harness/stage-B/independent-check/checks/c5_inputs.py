"""c5: are the harness's numbers from the scratch-copy run the numbers of the marks the markers made?

  /home/user/.venvs/threadsmith/bin/python c5_inputs.py

The scratch-copy run used run records that record_adapter.py rebuilt from the record, because the
ones the prompts were made from were gitignored and are not in this checkout. The marks themselves
are the saved files, unchanged. What the rebuilt records feed into stage_b.py: the document of each
run (marks_per_part's document gate) and the four run-record fields (first marks only).
Explanation under test: the rebuilt records are the records the prompts were made from. It forbids
any saved prompt differing from one rebuilt from them. Rival: the records changed, so the document
grouping could differ from what the markers saw. Separating check: rebuild all 192 prompts in
memory with the harness's own prompt_for from the adapter's in-memory records, and compare bytes.
Also: whether any prompt hands in a question (the independent's E1, on P3.3). Writes nothing.
"""
import os, re, sys, json
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
RIG = os.path.normpath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(RIG, "code"))
import record_adapter as RA, first_marker as FM, marks as M  # read only; collect() writes nothing

crit = M.load(os.path.join(RIG, "instrument", "criteria.json"))
recs = {r["run_id"]: r for r in RA.collect(RA.RECORD)}
B = os.path.join(RIG, "stage-B", "w10")
idx = json.load(open(os.path.join(B, "marking1", "index.json")))["reports"]
mp = json.load(open(os.path.join(RIG, "marking", "secret_mapping_record96.json")))["mapping"]
same = differ = 0; doc_mismatch = []; headings = {}
for folder, table in (("marking1", idx), ("marking2", mp)):
    for num, meta in table.items():
        saved = open(os.path.join(B, folder, "prompts", f"{num}.txt"), encoding="utf-8").read()
        out_path = re.search(r"Output path \(use Write, once, the JSON only\): (.*)\n", saved).group(1)
        r = recs[meta["run"]]
        if r["document"] != meta["document"]:
            doc_mismatch.append(num)
        rebuilt = FM.prompt_for(num, r["document"], r.get("report", ""), crit, out_path)
        if rebuilt == saved:
            same += 1
        else:
            differ += 1
        for h in re.findall(r"^=== (.*?) ===$", saved, flags=re.M):
            headings[h] = headings.get(h, 0) + 1
print(f"adapter records rebuilt in memory: {len(recs)}; prompts byte-identical {same}, differing {differ}; "
      f"document mismatches {doc_mismatch}")
print(f"section headings across all 192 prompts: {headings}")
print(f"prompt_for has a question slot: {'question' in FM.prompt_for.__code__.co_varnames}")
print(f"'Question' or 'question handed' as a heading in any prompt: "
      f"{any('QUESTION' in h.upper() for h in headings)}")
