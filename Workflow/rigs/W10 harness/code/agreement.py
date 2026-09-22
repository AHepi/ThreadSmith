"""DRIVER and RULE. Agreement by field and document, and the counts the predictions are made of.

  python3 agreement.py runs    --marks <marks file> [--criteria F]     # run to run, by field and arm
  python3 agreement.py markers --first <f> --second <f> [--criteria F] # marker to marker
  python3 agreement.py records --reader deepseek                       # PA.1 and P4.9, from the run records
  python3 agreement.py --dry                                           # a worked example, reading nothing

No program in the record computes run-to-run agreement; W3 section 5 names it as one of phase
4's outputs ("a comparison program that computes run-to-run agreement by field, which no program
in the rig does"). This is it.

The baseline rule, as W3 section 5 fixes it in P4.1 and W10 section 5 numbers it:
  "the baseline is the number of documents on which any two of the three repeats of arm (a)
   disagree; the comparison is the number of documents on which any repeat of arm (a) disagrees
   with any repeat of arm (b)."
So: all three (a)-to-(a) pairs are taken, and a document counts as disagreeing when any pair
disagrees. Tolerance: two documents. k, for a loss: the arm's own (a)-to-(a) baseline on that
field plus three (W10 section 5).

Three things this program will not do. It never sums across fields, or across arms, or across
readers (W10 section 12: "Summing readers or arms"). It never turns a count into a verdict on a
part: a count falsifies a prediction and nothing else (W3 section 5). A document where either
side has no value is counted as unreadable and named, never as agreement
(testing-against-cases.md: "'Found nowhere' means unknown").
"""
import os, sys, json, argparse, itertools
import rig, marks as M
from rig import RUNS, MARKING, read_json, write_json, stamp

TOLERANCE = 2
K_ADD = 3


def parse_rid(rid):
    return rig.parse_run_id(rid)


def index(mrks):
    """{(document, arm, repeat): {field: value}}"""
    out = {}
    for rid, row in mrks.items():
        out[parse_rid(rid)] = row
    return out


def _pairs_disagree(field, ix, doc, arm1, arm2):
    """(disagreed, readable) for one document: any pair of repeats that disagrees."""
    r1 = [(k, v) for (d, a, k), v in ix.items() if d == doc and a == arm1]
    r2 = [(k, v) for (d, a, k), v in ix.items() if d == doc and a == arm2]
    pairs = (itertools.combinations(sorted(r1), 2) if arm1 == arm2
             else itertools.product(sorted(r1), sorted(r2)))
    readable, disagreed = False, False
    for (k1, v1), (k2, v2) in pairs:
        s = M.same(field, v1.get(field["name"]), v2.get(field["name"]))
        if s is None:
            continue
        readable = True
        if not s:
            disagreed = True
    return disagreed, readable


def field_counts(field, ix, docs, arm1, arm2):
    dis, unread = [], []
    for d in docs:
        disagreed, readable = _pairs_disagree(field, ix, d, arm1, arm2)
        if not readable:
            unread.append(d)
        elif disagreed:
            dis.append(d)
    return {"documents": len(docs), "unreadable": unread,
            "readable": len(docs) - len(unread), "disagreeing": dis, "count": len(dis)}


def run_agreement(crit, data):
    ix = index(data["marks"])
    docs = sorted({d for d, _, _ in ix})
    armsp = sorted({a for _, a, _ in ix})
    n = len(docs)
    out = {"documents": docs, "arms": armsp, "tolerance_documents": TOLERANCE,
           "k_rule": f"baseline + {K_ADD}", "fields": {}}
    for f in M.fields(crit, comparable_only=True):
        base = field_counts(f, ix, docs, "a", "a")
        row = {"sort": f["sort"], "baseline": base,
               "uninformative": base["count"] > n / 2 if n else True, "against_a": {}}
        for a in armsp:
            if a == "a":
                continue
            c = field_counts(f, ix, docs, "a", a)
            k = base["count"] + K_ADD
            unreadable = c["readable"] == 0 or base["readable"] == 0
            c["within_tolerance"] = None if unreadable else c["count"] <= base["count"] + TOLERANCE
            c["loses_field"] = None if unreadable else c["count"] >= k
            c["k"] = k
            c["nothing_readable"] = unreadable
            if a == "x":
                moved = []
                for d in docs:
                    dx, rx = _pairs_disagree(f, ix, d, "a", "x")
                    da, ra = _pairs_disagree(f, ix, d, "a", "a")
                    if rx and dx and ra and not da:
                        moved.append(d)
                c["moved_beyond_the_a_to_a_spread"] = moved
            row["against_a"][a] = c
        out["fields"][f["name"]] = row
    out["predictions"] = verdicts(crit, out)
    return out


def verdicts(crit, out):
    """Each prediction as the count that could fail it, never as a verdict on a part."""
    n = len(out["documents"])
    by = {f["name"]: f for f in crit["fields"]}
    v = {}
    win = [k for k, r in out["fields"].items() if r["sort"] == "within-step"]
    cross = [k for k, r in out["fields"].items() if r["sort"] == "cross-step"]

    def got(arm, field):
        return out["fields"][field]["against_a"].get(arm)

    v["PA.2"] = {"rule": "the (a)-to-(a) baseline is above zero on at least one certified field",
                 "baselines": {k: out["fields"][k]["baseline"]["count"] for k in out["fields"]},
                 "holds": any(out["fields"][k]["baseline"]["count"] > 0 for k in out["fields"])}
    v["P4.1"] = {"rule": f"arm (b) exceeds the baseline by more than {TOLERANCE} documents on no certified field",
                 "over": [k for k in out["fields"] if got("b", k) and got("b", k)["within_tolerance"] is False],
                 "nothing_readable": [k for k in out["fields"] if got("b", k) and got("b", k)["nothing_readable"]],
                 "uninformative_fields": [k for k, r in out["fields"].items() if r["uninformative"]]}
    v["P4.1"]["holds"] = not v["P4.1"]["over"]
    for arm, name in (("c", "P4.2"), ("d", "P4.3")):
        lost = [k for k in cross if got(arm, k) and got(arm, k)["loses_field"] is True]
        kept = [k for k in win if got(arm, k) and got(arm, k)["within_tolerance"] is False]
        v[name] = {"rule": f"arm ({arm}) loses at least one certified cross-step field by k = baseline + {K_ADD}, "
                           f"and its within-step fields stay within {TOLERANCE}",
                   "cross_step_fields_lost": lost, "within_step_fields_also_lost": kept,
                   "holds": bool(lost) and not kept}
    if "cctl" in out["arms"]:
        v["P4.2 control"] = {"rule": "arm (c)'s equal-length control, which omits the parts list "
                                     "(W8 section 4): what it loses that arm (c) does not",
                             "cross_step_fields_lost": [k for k in cross if got("cctl", k) and got("cctl", k)["loses_field"] is True],
                             "reads": "a control that loses the same fields says the loss was length, not the parts list"}
    ev = {k: (got("e", k), got("b", k)) for k in win}
    v["P4.4"] = {"rule": f"arm (e) disagrees with arm (a) on the within-step fields on at least {K_ADD} more "
                         f"documents than arm (b) does, while arms (b) and (c) stay within {TOLERANCE}",
                 "by_field": {k: {"e": e["count"], "b": b["count"], "e_minus_b": e["count"] - b["count"],
                                  "holds": e["count"] - b["count"] >= K_ADD}
                              for k, (e, b) in ev.items() if e and b},
                 "read_only_harness_lost_a_within_step_field":
                     [k for k in win for a in ("b", "c") if got(a, k) and got(a, k)["within_tolerance"] is False]}
    v["P4.4"]["holds"] = any(d["holds"] for d in v["P4.4"]["by_field"].values()) and \
                         not v["P4.4"]["read_only_harness_lost_a_within_step_field"]
    v["P4.5 (f)"] = {"rule": "arm (f) moves at least one within-step field on at least k of n documents",
                     "moved": {k: got("f", k)["count"] for k in win if got("f", k)},
                     "k": {k: got("f", k)["k"] for k in win if got("f", k)},
                     "holds": any(got("f", k) and got("f", k)["loses_field"] is True for k in win)}
    cc = {k: (got("cprime", k), got("c", k)) for k in cross}
    v["P4.5 (c')"] = {"rule": "arm (c') loses fewer cross-step fields than arm (c) on at least three more documents",
                      "by_field": {k: {"cprime": a["count"], "c": b["count"], "c_minus_cprime": b["count"] - a["count"]}
                                   for k, (a, b) in cc.items() if a and b},
                      "holds": any(b["count"] - a["count"] >= 3 for a, b in cc.values() if a and b)}
    half = (n + 1) // 2
    v["PA.3 (x)"] = {"rule": f"the emission moves on at least one certified field on at least "
                             f"{max(4, half)} of {n} documents (W10 section 5 fixes four of eight)",
                     "moved": {k: got("x", k)["count"] for k in out["fields"] if got("x", k)},
                     "moved_beyond_the_spread": {k: len(got("x", k).get("moved_beyond_the_a_to_a_spread", []))
                                                 for k in out["fields"] if got("x", k)},
                     "holds": any(got("x", k) and got("x", k)["count"] >= max(4, half) for k in out["fields"])}
    return v


def marker_agreement(crit, first, second):
    rows = []
    shared = sorted(set(first["marks"]) & set(second["marks"]))
    for f in M.fields(crit, comparable_only=True):
        agree, dis, unread = [], [], []
        for rid in shared:
            s = M.same(f, first["marks"][rid].get(f["name"]), second["marks"][rid].get(f["name"]))
            (unread if s is None else agree if s else dis).append(rid)
        rows.append({"field": f["name"], "sort": f["sort"], "reports": len(shared),
                     "agree": len(agree), "disagree": len(dis), "unreadable": len(unread),
                     "disagreeing_reports": dis})
    return rows


def print_marker_table(rows, n):
    print(f"marker to marker, {n} report(s) in both sets. No field is summed with another.")
    print(f"  {'field':34} {'sort':12} {'agree':>7} {'disagree':>9} {'unreadable':>11}")
    for r in rows:
        print(f"  {r['field']:34} {r['sort']:12} {r['agree']:>7} {r['disagree']:>9} {r['unreadable']:>11}")


def print_run_table(out):
    n = len(out["documents"])
    print(f"run to run, {n} document(s): {', '.join(out['documents'])}")
    for name, row in out["fields"].items():
        b = row["baseline"]
        flag = "  [baseline over half the documents: this field says nothing]" if row["uninformative"] else ""
        print(f"\n  {name}  ({row['sort']})  baseline (a)-to-(a): {b['count']}/{b['readable']} readable{flag}")
        for arm, c in row["against_a"].items():
            bits = [f"{c['count']}/{c['readable']}"]
            bits.append("nothing readable" if c["within_tolerance"] is None
                        else ("within tolerance" if c["within_tolerance"] else "OVER tolerance"))
            if c["loses_field"] is True:
                bits.append(f"loses the field (k={c['k']})")
            if c["unreadable"]:
                bits.append(f"unreadable on {len(c['unreadable'])}")
            print(f"     vs arm ({arm}): " + "; ".join(bits))
    print("\n  predictions, as counts that could fail:")
    for k, v in out["predictions"].items():
        print(f"     {k}: holds={v.get('holds')}  {v['rule']}")


def records_counts(reader):
    d = os.path.join(RUNS, reader)
    rows = []
    for fn in sorted(os.listdir(d)):
        if not fn.endswith(".json"):
            continue
        r = read_json(os.path.join(d, fn))
        served = sorted(set(r.get("modules_served") or []))
        said = sorted(set(r.get("modules_self_reported") or []))
        rows.append({"run": r["run_id"], "arm": r["arm"], "requests": r.get("requests"),
                     "tool_loop_requests": r.get("tool_loop_requests"), "steps": r.get("steps"),
                     "one_request_per_step": (None if r.get("tool_loop_requests") is None else
                                              (r["requests"] - r["tool_loop_requests"]) == r.get("steps")),
                     "modules_served": served, "modules_self_reported": said,
                     "traces_differ": served != said})
    pa1 = [x for x in rows if x["arm"] in ("b", "c", "cctl", "cprime", "d")
           and x["one_request_per_step"] is False]
    p49 = [x for x in rows if x["traces_differ"] and (x["modules_served"] or x["modules_self_reported"])]
    return {"rows": rows,
            "PA.1": {"rule": "one request per step in arms (b), (c), (c') and (d), and more than one "
                             "in arm (a); the tool-loop requests the rig served are counted apart",
                     "arms_with_more_than_one_request_per_step": [x["run"] for x in pa1],
                     "holds": not pa1},
            "P4.9": {"rule": "on every run that opens a module, the transport's record and the "
                             "reader's own list name the same modules; more than one difference "
                             "and the self-reported field carries no arm difference",
                     "runs_where_they_differ": [x["run"] for x in p49],
                     "holds": len(p49) <= 1}}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("cmd", nargs="?", default="runs", choices=["runs", "markers", "records"])
    p.add_argument("--marks", default="")
    p.add_argument("--first", default="")
    p.add_argument("--second", default="")
    p.add_argument("--criteria", default=None)
    p.add_argument("--reader", default="deepseek")
    p.add_argument("--out", default="")
    p.add_argument("--dry", action="store_true")
    o = p.parse_args()
    if o.dry:
        crit = M.load(os.path.join(rig.FIXTURES, "criteria.example.json"))
        data = read_json(os.path.join(rig.FIXTURES, "marks.example.json"), "the example marks")
        out = run_agreement(crit, data)
        print_run_table(out)
        print("\ndry run: read only the example marks in fixtures/, wrote nothing, sent nothing.")
        return
    crit = M.load(o.criteria)
    if o.cmd == "runs":
        data = read_json(o.marks or os.path.join(MARKING, f"marks_first_{o.reader}.json"), "a marks file")
        out = run_agreement(crit, data)
        print_run_table(out)
        write_json(o.out or os.path.join(MARKING, f"agreement_runs_{o.reader}.json"),
                   {"made_at": stamp(), "reader": o.reader,
                    "criteria_version": crit.get("version"), **out})
        return
    if o.cmd == "markers":
        first = read_json(o.first or os.path.join(MARKING, f"marks_first_{o.reader}.json"), "the first marks")
        second = read_json(o.second or os.path.join(MARKING, f"marks_second_{o.reader}.json"), "the second marks")
        rows = marker_agreement(crit, first, second)
        print_marker_table(rows, len(set(first["marks"]) & set(second["marks"])))
        write_json(o.out or os.path.join(MARKING, f"agreement_markers_{o.reader}.json"),
                   {"made_at": stamp(), "reader": o.reader, "rows": rows})
        return
    out = records_counts(o.reader)
    for k in ("PA.1", "P4.9"):
        print(f"{k}: holds={out[k]['holds']}  {out[k]['rule']}")
        for kk, vv in out[k].items():
            if kk.startswith(("arms_", "runs_")) and vv:
                print(f"   {kk}: {vv}")
    write_json(o.out or os.path.join(MARKING, f"records_counts_{o.reader}.json"),
               {"made_at": stamp(), "reader": o.reader, **out})


if __name__ == "__main__":
    main()
