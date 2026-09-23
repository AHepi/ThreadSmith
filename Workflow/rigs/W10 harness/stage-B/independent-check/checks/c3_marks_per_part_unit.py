"""c3: marks_per_part's gate, counted by document (the harness) and by report (the independent).

  /home/user/.venvs/threadsmith/bin/python c3_marks_per_part_unit.py

Explanation under test: the two programs agree report by report on marks_per_part (37 of 48 in
p52, 44 of 48 in the repeat set; c1 shows the same reports named) and differ only in the unit of
the gate. stage_b.py counts documents all of whose reports agree, against ceil(40/48 x documents);
the independent counts reports against 40 of 48. It forbids any report-level difference.
Rival: the programs differ on some report, and the document counts reflect that. Separating
check: aggregate the independent's own per-report outcomes by document; if the rival held, the
result would differ from stage_b.py's 6 of 16 and 0 of 2.

Second question: is the document gate the same test as "40 of 48" at a coarser grain, or a
different test? Computed: for the document sizes in each set, the fewest agreeing reports that can
pass the document gate (disagreements packed into the fewest documents) and the most that can
still fail it (disagreements spread one per document). Writes nothing.
"""
import os, re, sys, json, math
from collections import defaultdict
HERE = os.path.dirname(os.path.abspath(__file__))
RIG = os.path.normpath(os.path.join(HERE, "..", "..", ".."))
IND = json.load(open(os.path.join(HERE, "..", "output.json")))
HB = json.load(open(os.path.join(HERE, "harness-programs-on-a-scratch-copy", "stage_b_record96.json")))
idx = json.load(open(os.path.join(RIG, "stage-B", "w10", "marking1", "index.json")))["reports"]
doc = {m["run"]: m["document"] for m in idx.values()}

f = IND["per_field"]["marks_per_part"]
for s, hs in (("p52", "close"), ("repeat", "repeat")):
    bad = set(f[s]["disagree_runs"]) | set(f[s]["unreadable_runs"])
    runs = [r for r in doc if (r.startswith("p52_") if s == "p52" else not r.startswith("p52_"))]
    per_doc = defaultdict(list)
    for r in runs:
        per_doc[doc[r]].append(r)
    all_agree = sorted(d for d, rr in per_doc.items() if not (set(rr) & bad))
    h = HB["fields"]["marks_per_part"]["per_set"][hs]
    sizes = sorted(len(v) for v in per_doc.values())
    thr_docs = math.ceil(40 / 48 * len(per_doc))
    may_fail_docs = len(per_doc) - thr_docs          # documents that may hold a disagreement and still pass
    fewest_to_pass = len(runs) - sum(sorted(sizes, reverse=True)[:may_fail_docs])
    most_that_fail = len(runs) - (may_fail_docs + 1)  # one disagreement in each of one document too many
    print(f"{s}: {len(runs)} reports on {len(per_doc)} documents, sizes {sorted(set(sizes))}")
    print(f"  independent, reports agreeing: {f[s]['agree']} of {len(runs)} (disagree {len(f[s]['disagree_runs'])}, unreadable {len(f[s]['unreadable_runs'])})")
    print(f"  independent's per-report outcomes aggregated by document: {len(all_agree)} of {len(per_doc)} documents all agree")
    print(f"  stage_b.py: {h['agree_documents']} of {h['documents']} documents, threshold {h['threshold']}; same: "
          f"{(len(all_agree), len(per_doc)) == (h['agree_documents'], h['documents'])}")
    print(f"  documents with a disagreeing or unreadable report: "
          + ", ".join(f"{d} ({len(set(rr) & bad)} of {len(rr)})" for d, rr in sorted(per_doc.items()) if set(rr) & bad))
    print(f"  the document gate, said in reports: passes with as few as {fewest_to_pass} of {len(runs)} agreeing; "
          f"fails with as many as {most_that_fail} of {len(runs)}. The texts' gate: 40 of 48.")
    print(f"  per-set verdict: by report {'reaches' if f[s]['agree'] >= 40 else 'misses'} 40; "
          f"by document {'reaches' if h['agree_documents'] >= h['threshold'] else 'misses'} {h['threshold']}")

# the harness's own split for the same field counts reports, not documents
sp = HB["fields"]["marks_per_part"]["split"]
print(f"\nstage_b.py's W10.16 split for marks_per_part: read n {sp['read']['n']}, unread n {sp['unread']['n']} "
      f"(sum {sp['read']['n'] + sp['unread']['n']}: reports, not documents)")

# the words, quoted from the frozen texts
T = {"W14": "Workflow/tests/W14 Plan - stage B, the instrument certified on the 96 reports by two blind Sonnet 5 markers.md",
     "marking plan": "Workflow/rigs/W10 harness/instrument/marking-plan.md"}
for k, fn in T.items():
    t = open(os.path.join(RIG, "..", "..", "..", fn), encoding="utf-8").read()
    for pat in (r"[^.\n]*read by document[^.\n]*\.", r"[^.\n]*of 48 separately[^.\n]*"):
        for m in re.finditer(pat, t):
            print(f"\n{k}: ...{m.group(0).strip()[:300]}")
c = json.load(open(os.path.join(RIG, "instrument", "criteria.json")))
print(f"\ncriteria.json agreement.marker_to_marker_rule: {c['agreement']['marker_to_marker_rule']}")
print(f"stage_b.py's docstring claims the scaling was 'fixed in W14': "
      f"{'ceil(40/48 x the documents' in open(os.path.join(RIG, 'code', 'stage_b.py')).read()}; "
      f"W14 contains 'ceil' or 'scaled': {any(w in open(os.path.join(RIG, '..', '..', '..', T['W14'])).read() for w in ('ceil', 'scaled', 'proportion'))}")
