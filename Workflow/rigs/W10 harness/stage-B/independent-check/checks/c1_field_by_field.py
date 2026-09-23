"""c1: every number of stage B, the harness's programs against the independent program, field by field.

  /home/user/.venvs/threadsmith/bin/python c1_field_by_field.py

Reads (writes nothing but c1_field_by_field.json beside this file):
  ../output.json                                               the independent program's counts
  harness-programs-on-a-scratch-copy/stage_b_record96.json     stage_b.py's counts (scratch-copy run)
  harness-programs-on-a-scratch-copy/agreement_markers_record96.json   second_marker.py compare's rows
  the raw marks, paired through index.json and the closed mapping, compared with the harness's own
  rule (code/marks.py `same`), only to name which reports are unreadable under the harness's rule
  (the harness's files name disagreeing reports but not unreadable ones).

What this check could show and would forbid: if the two programs apply the same per-kind rule to
the same pairing, every per-report count agrees and so does every named report. A count that
matches while the named reports differ would mean two different rules happening to give one total.
"""
import os, sys, json
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
RIG = os.path.normpath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(RIG, "code"))
import marks as M  # the harness's rule, read only

IND = json.load(open(os.path.join(HERE, "..", "output.json")))
H = os.path.join(HERE, "harness-programs-on-a-scratch-copy")
HB = json.load(open(os.path.join(H, "stage_b_record96.json")))
HA = {r["field"]: r for r in json.load(open(os.path.join(H, "agreement_markers_record96.json")))["rows"]}
crit = M.load(os.path.join(RIG, "instrument", "criteria.json"))
by = {f["name"]: f for f in crit["fields"]}

# pair the raw marks exactly as first_marker.py collect and second_marker.py collect do
B = os.path.join(RIG, "stage-B", "w10")
idx = json.load(open(os.path.join(B, "marking1", "index.json")))["reports"]
mp = json.load(open(os.path.join(RIG, "marking", "secret_mapping_record96.json")))["mapping"]
first = {m["run"]: json.load(open(os.path.join(B, "marking1", "marks", f"{n}.json"))) for n, m in idx.items()}
second = {m["run"]: json.load(open(os.path.join(B, "marking2", "marks", f"{n}.json"))) for n, m in mp.items()}
runs = sorted(set(first) & set(second))
SETS = {"p52": [r for r in runs if r.startswith("p52_")], "repeat": [r for r in runs if not r.startswith("p52_")]}
HSET = {"p52": "close", "repeat": "repeat"}


def harness_rule(name, rids):
    f = by[name]; a, d, u = [], [], []
    for r in rids:
        s = M.same(f, first[r].get(name), second[r].get(name))
        (u if s is None else a if s else d).append(r)
    return a, d, u


rows = []
SECTION = ["primary"]  # "primary": the harness's output against the independent's primary output.
                       # "cause": a check of what a difference comes from; never counted with the first.


def kind_of(item, h, i):
    """number: a count, threshold or percentage (with its unit where the units differ);
    verdict: a certified flag or a prediction's holds; list: named reports or fields."""
    if isinstance(h, list) or isinstance(i, list):
        return "list"
    if item.endswith(" certified") or item.endswith(" holds"):
        return "verdict"
    return "number"


def cmp(item, h, i, note=""):
    ok = (h == i)
    rows.append({"section": SECTION[0], "kind": kind_of(item, h, i), "item": item, "harness": h,
                 "independent": i, "match": ok, "note": note})
    return ok


shared = [f for f in IND["per_field"]]
for name in shared:
    fi = IND["per_field"][name]; fh = HB["fields"][name]
    for s in ("p52", "repeat"):
        hs = fh["per_set"][HSET[s]]; is_ = fi[s]
        if name == "marks_per_part":
            cmp(f"{name} {s} agreeing reports", hs["agree_reports"], is_["agree"])
            cmp(f"{name} {s} the gate count (harness: documents all agreeing; independent: reports)",
                f"{hs['agree_documents']} of {hs['documents']} documents", f"{is_['agree']} of {is_['n']} reports")
            cmp(f"{name} {s} threshold", f"{hs['threshold']} of {hs['documents']} documents", f"{fi['threshold_of_48']} of 48 reports")
        else:
            cmp(f"{name} {s} agree", hs["agree"], is_["agree"])
            cmp(f"{name} {s} disagree", hs["disagree"], is_["disagree"])
            cmp(f"{name} {s} unreadable", hs["unreadable"], is_["unreadable"])
            cmp(f"{name} {s} threshold", hs["threshold"] if fh["certified_candidate"] else f"{hs['threshold']} (printed; not a candidate)",
                fi["threshold_of_48"])
        # the named reports, by the harness's own rule on the raw marks, against the independent's lists
        a, d, u = harness_rule(name, SETS[s])
        cmp(f"{name} {s} disagreeing reports named", sorted(d), sorted(is_["disagree_runs"]))
        cmp(f"{name} {s} unreadable reports named", sorted(u), sorted(is_["unreadable_runs"]))
    hp = fh["pooled"]; ip = fi["pooled_96"]
    cmp(f"{name} pooled agree", hp["agree"], ip["agree"])
    cmp(f"{name} pooled disagree", hp["disagree"], ip["disagree"])
    cmp(f"{name} pooled unreadable", hp["unreadable"], ip["unreadable"])
    # the harness's compare file names its disagreeing reports; the raw-marks route must give the same
    a, d, u = harness_rule(name, runs)
    assert sorted(d) == sorted(HA[name]["disagreeing_reports"]), f"raw-marks route differs from compare on {name}"
    assert (len(a), len(d), len(u)) == (HA[name]["agree"], HA[name]["disagree"], HA[name]["unreadable"])
    cmp(f"{name} certified", fh["certified"] if fh["certified_candidate"] else f"{fh['certified']} (not a candidate)",
        fi["certified"])

# the field only one side counted
mh = HB["fields"].get("modules_served")
rows.append({"section": "not compared", "item": "modules_served (harness only)", "harness": {"p52": mh["per_set"]["close"], "repeat": mh["per_set"]["repeat"], "pooled": mh["pooled"]},
             "independent": "not counted (filled by program on one side only; not a candidate)", "match": None, "note": "not compared"})

# W10.17, per enum field per marker
w17 = IND["predictions"]["W10.17"]["per_field"]
for name, f in by.items():
    if f["kind"] != "enum":
        continue
    hl = HB["fields"][name]["in_list"]
    cmp(f"W10.17 {name} first marker in-list", hl["first"], w17[name]["first"]["closed_list"])
    cmp(f"W10.17 {name} second marker in-list", hl["second"], w17[name]["second"]["closed_list"])
cmp("W10.17 fields named unreadable", sorted(HB["W10.17"]["unreadable"]),
    sorted(k for k, v in w17.items() if v.get("holds_on_this_field") is False and by[k]["kind"] == "enum"))

# the split (W10.16). Primary: the harness's numbers against the independent's primary (reading B, of n).
spA = IND["split"]["A_record_file_names_only"]; spB = IND["split"]["B_record_file_names_and_run_ids (primary)"]
for name in ("marks_per_part", "pairs_that_pull", "rivals_built"):
    hs = HB["fields"][name]["split"]; x = spB[name]
    cmp(f"W10.16 {name} read n", hs["read"]["n"], x["read"]["n"])
    cmp(f"W10.16 {name} read agree", hs["read"]["agree"], x["read"]["agree"])
    cmp(f"W10.16 {name} unread n", hs["unread"]["n"], x["unread"]["n"])
    cmp(f"W10.16 {name} unread agree", hs["unread"]["agree"], x["unread"]["agree"])
    cmp(f"W10.16 {name} read %", hs["read_pct"], round(x["read"]["pct_of_n"], 1))
    cmp(f"W10.16 {name} unread %", hs["unread_pct"], round(x["unread"]["pct_of_n"], 1))
    cmp(f"W10.16 {name} gap, points", round(hs["read_pct"] - hs["unread_pct"], 1), round(IND["predictions"]["W10.16"]["primary"]["of_n"]["gaps_pp"][name], 1))
cmp("W10.16 the read reports (the set)", sorted(HB["read_reports"]), sorted(IND["read_reports"]["B_record_file_names_and_run_ids (primary)"]))
cmp("W10.16 falsified on", HB["W10.16"]["falsified_on"], IND["predictions"]["W10.16"]["primary"]["of_n"]["falsified_on"])
# the certified list and the predictions
cmp("certified list", sorted(HB["certified"]), sorted(IND["consequences"]["certified_fields"]))
P = IND["predictions"]
cmp("P3.1 holds", HB["P3.1"]["held"], P["P3.1"]["holds (primary: each field in both sets, then two of three)"])
cmp("P3.1 fields reaching 44 in both sets", sorted(HB["P3.1"]["reached"]), sorted(P["P3.1"]["fields_reaching_44_in_both_sets (primary)"]))
cmp("P3.2 holds", HB["P3.2"]["held"], P["P3.2"]["holds"])
cmp("P3.3 holds", HB["P3.3"]["held"], P["P3.3"]["holds"])
cmp("P3.4 holds", HB["P3.4"]["held"], P["P3.4"]["holds"])
cmp("P3.5 holds", HB["P3.5"]["held"], P["P3.5"]["holds"])
h39 = [n for n, r in HB["fields"].items() if r["certified_candidate"] and r["threshold_of_48"] == 39 and not r["certified"]]
cmp("other fields at 39: the fields failing (harness: implied by its certified list)", sorted(h39), sorted(P["other_fields_at_39"]["failing"]))
cmp("W10.16 holds", not HB["W10.16"]["falsified_on"], P["W10.16"]["primary"]["of_n"]["holds"])
cmp("W10.17 holds", not HB["W10.17"]["unreadable"], all(v.get("holds_on_this_field") is not False for v in w17.values()))

# ---- cause checks: what the differences come from (not counted with the primary comparison) ----
SECTION[0] = "cause"
for name in ("marks_per_part", "pairs_that_pull", "rivals_built"):
    hs = HB["fields"][name]["split"]; x = spA[name]
    cmp(f"cause: W10.16 {name} read n, harness = independent's reading A", hs["read"]["n"], x["read"]["n"])
    cmp(f"cause: W10.16 {name} read agree, reading A", hs["read"]["agree"], x["read"]["agree"])
    cmp(f"cause: W10.16 {name} unread n, reading A", hs["unread"]["n"], x["unread"]["n"])
    cmp(f"cause: W10.16 {name} unread agree, reading A", hs["unread"]["agree"], x["unread"]["agree"])
    cmp(f"cause: W10.16 {name} read %, reading A over readable", hs["read_pct"], round(x["read"]["pct_of_readable"], 1))
    cmp(f"cause: W10.16 {name} unread %, reading A over readable", hs["unread_pct"], round(x["unread"]["pct_of_readable"], 1))
    cmp(f"cause: W10.16 {name} gap, reading A over readable", round(hs["read_pct"] - hs["unread_pct"], 1),
        round(x["read"]["pct_of_readable"] - x["unread"]["pct_of_readable"], 1))
cmp("cause: W10.16 the read reports = the independent's reading A", sorted(HB["read_reports"]), sorted(IND["read_reports"]["A_record_file_names_only"]))
AR = IND["predictions"]["W10.16"]["all_readings"]
cmp("cause: W10.16 falsified on, harness = independent's reading A over readable",
    HB["W10.16"]["falsified_on"], AR["A_record_file_names_only"]["of_readable"]["falsified_on"])
cmp("cause: W10.16 pairs_that_pull (the one certified field of the three) falsified under any of the independent's ten reading-and-basis pairs",
    False, any("pairs_that_pull" in AR[r][b]["falsified_on"] for r in AR for b in ("of_n", "of_readable")))
dA = IND["other_readings"]["count_of_source_documents"]["marks_per_part"]
for s_ in ("p52", "repeat"):
    hs = HB["fields"]["marks_per_part"]["per_set"][HSET[s_]]
    cmp(f"cause: marks_per_part {s_} documents all agreeing, harness = independent's other reading (source documents)",
        (hs["agree_documents"], hs["documents"]), (dA[s_]["documents_all_reports_agree"], dA[s_]["documents"]))

prim = [r for r in rows if r["section"] == "primary"]; cause = [r for r in rows if r["section"] == "cause"]
out = {"primary": {"items_compared": len(prim), "items_matching": sum(r["match"] for r in prim),
                   "differing": [r["item"] for r in prim if not r["match"]]},
       "cause_checks": {"compared": len(cause), "matching": sum(r["match"] for r in cause),
                        "differing": [r["item"] for r in cause if not r["match"]]},
       "rows": rows}
json.dump(out, open(os.path.join(HERE, "c1_field_by_field.json"), "w"), indent=1, ensure_ascii=False)
print(f"primary: compared {len(prim)}, matching {out['primary']['items_matching']}, differing {len(out['primary']['differing'])}")
print(f"cause checks: compared {len(cause)}, matching {out['cause_checks']['matching']}")
for k in ("number", "verdict", "list"):
    rr = [r for r in prim if r["kind"] == k]
    out["primary"][f"{k}s_compared"] = len(rr); out["primary"][f"{k}s_matching"] = sum(r["match"] for r in rr)
    print(f"  primary {k}s: compared {len(rr)}, matching {sum(r['match'] for r in rr)}")
json.dump(out, open(os.path.join(HERE, "c1_field_by_field.json"), "w"), indent=1, ensure_ascii=False)
for r in rows:
    if r["match"] is False:
        print(f"  DIFFERS [{r['section']}] {r['item']}\n           harness: {json.dumps(r['harness'])[:150]}\n           independent: {json.dumps(r['independent'])[:150]}")
