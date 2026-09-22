"""DRIVER and RULE. Agreement by field and document, and the counts the predictions are made of.

  python3 agreement.py runs    --marks <marks file> [--criteria F] [--certified F]
  python3 agreement.py markers --first <f> --second <f> [--criteria F] # marker to marker
  python3 agreement.py records --reader deepseek [--marks F]           # the counts from the records
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

Four things the stage-A review and W11 forced, each named where it bites:

 - **Certified fields only** (fault 1). P4.1, P4.2, P4.3, P4.4, P4.5 and PA.3 are read over
   fields with `certified_candidate` true, and over stage B's own certified list where one is
   supplied with --certified. The read-outs and the gauges (`modules_served`,
   `marks_outside_closed_list`, `layer_at_fault`) are printed beside every count and are never
   inside one: criteria.json's own words, "false fields are read-outs and gauges and carry no
   arm difference".
 - **"never varies"** (W11 D4, fault 18). A field that takes one value on every run of every arm
   cannot show a loss, so it is flagged beside "uninformative" and carries no arm difference.
 - **The corpus affordance** (W11 D4, fault 18). P4.2 and P4.3 are read over the certified
   cross-step fields that at least one of the eight arms documents affords, by A4's table.
   Where no table is found, every certified cross-step field is read and the counts file names
   every place that was looked at.
 - **PA.1 by halves** (W11 D2, fault 15). The plain count and the count with the tool-loop
   requests taken out are both printed, so a later reader can take the other reading. The arm
   (a) half of PA.1 is reported "not reached" on both transports and never as held or falsified:
   on DeepSeek arm (a) is five turns of one conversation, five requests for five steps, so the
   clause is falsified by the rig's own design and not by anything about the reader; on the
   Sonnet subagent transport a request inside one call is not observable from outside it.
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


def never_varies(field, ix):
    """W11 D4: does this field take one value on every run of every arm? A field that never
    varies anywhere cannot show a loss, so it carries no arm difference.
    Returns (never_varies, distinct_readable_values)."""
    vals = set()
    for row in ix.values():
        v = M.normalise(field, row.get(field["name"]))
        if v is not None:
            vals.add(v)
    return (len(vals) == 1), len(vals)


def run_agreement(crit, data, certified=None):
    ix = index(data["marks"])
    docs = sorted({d for d, _, _ in ix})
    armsp = sorted({a for _, a, _ in ix})
    n = len(docs)
    aff, aff_where = M.affordance(crit)
    cert_names = {f["name"] for f in M.fields(crit, comparable_only=True,
                                              certified_only=True, certified=certified)}
    out = {"documents": docs, "arms": armsp, "tolerance_documents": TOLERANCE,
           "k_rule": f"baseline + {K_ADD}",
           "certified_fields": sorted(cert_names),
           "certified_from": ("certified_candidate true, and stage B's certified list"
                              if certified is not None else
                              "certified_candidate true; no stage-B certified list was supplied, "
                              "so no field has yet agreed anywhere and every count below is "
                              "provisional on stage B (W10 stage B)"),
           "read_outs_and_gauges": sorted(f["name"] for f in M.read_outs(crit)),
           "read_outs_are": ("printed beside every count and never inside one: criteria.json, "
                             "'false fields are read-outs and gauges and carry no arm difference'"),
           "corpus_affordance_from": aff_where,
           "fields": {}}
    for f in M.fields(crit, comparable_only=True):
        base = field_counts(f, ix, docs, "a", "a")
        nv, distinct = never_varies(f, ix)
        # A field the table does not name is read, not excluded: A4's own rule, "'Found nowhere
        # means unknown': a gap in the corpus's record is not a finding that the documents
        # afford nothing." Only a field the table names with no arms document is excluded.
        afforded = (None if (aff is None or f["sort"] != "cross-step" or f["name"] not in aff)
                    else bool(aff[f["name"]]))
        row = {"sort": f["sort"], "baseline": base,
               "certified": f["name"] in cert_names,
               "certified_candidate": f.get("certified_candidate") is True,
               "never_varies": nv, "distinct_values_anywhere": distinct,
               "afforded_by_the_arms_documents": (None if aff is None else aff.get(f["name"])),
               "afforded": afforded,
               "in_the_affordance_table": (None if aff is None else f["name"] in aff),
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
    """Each prediction as the count that could fail it, never as a verdict on a part.

    Every count below is read over the certified fields alone (fault 1), and a field flagged
    "never varies" is left out of the cross-step counts (W11 D4). The read-outs and gauges are
    printed beside, under "read_outs_beside"."""
    n = len(out["documents"])
    v = {}

    def usable(k, sort):
        r = out["fields"][k]
        return r["sort"] == sort and r["certified"]

    win = [k for k in out["fields"] if usable(k, "within-step")]
    cross_all = [k for k in out["fields"] if usable(k, "cross-step")]
    # W11 D4: read over the cross-step fields at least one arms document affords, and never over
    # one that takes the same value on every run of every arm.
    cross = [k for k in cross_all
             if out["fields"][k]["afforded"] is not False and not out["fields"][k]["never_varies"]]
    cross_left_out = {k: ("no arms document affords it" if out["fields"][k]["afforded"] is False
                          else "never varies across every run of every arm")
                      for k in cross_all if k not in cross}

    def got(arm, field):
        return out["fields"][field]["against_a"].get(arm)

    v["read_outs_beside"] = {
        "rule": "printed beside the counts, never inside one (criteria.json: read-outs and "
                "gauges carry no arm difference)",
        "fields": {k: {"baseline": out["fields"][k]["baseline"]["count"],
                       "against_a": {a: c["count"] for a, c in out["fields"][k]["against_a"].items()},
                       "never_varies": out["fields"][k]["never_varies"]}
                   for k in out["fields"] if not out["fields"][k]["certified"]}}
    v["PA.2"] = {"rule": "the (a)-to-(a) baseline is above zero on at least one certified field",
                 "baselines": {k: out["fields"][k]["baseline"]["count"] for k in win + cross_all},
                 "holds": any(out["fields"][k]["baseline"]["count"] > 0 for k in win + cross_all)}
    v["P4.1"] = {"rule": f"arm (b) exceeds the baseline by more than {TOLERANCE} documents on no certified field",
                 "read_over": sorted(win + cross_all),
                 "over": [k for k in win + cross_all if got("b", k) and got("b", k)["within_tolerance"] is False],
                 "nothing_readable": [k for k in win + cross_all if got("b", k) and got("b", k)["nothing_readable"]],
                 "uninformative_fields": [k for k in win + cross_all if out["fields"][k]["uninformative"]],
                 "never_varies_fields": [k for k in win + cross_all if out["fields"][k]["never_varies"]]}
    v["P4.1"]["holds"] = not v["P4.1"]["over"]
    for arm, name in (("c", "P4.2"), ("d", "P4.3")):
        lost = [k for k in cross if got(arm, k) and got(arm, k)["loses_field"] is True]
        kept = [k for k in win if got(arm, k) and got(arm, k)["within_tolerance"] is False]
        v[name] = {"rule": f"arm ({arm}) loses at least one certified cross-step field by k = baseline + {K_ADD}, "
                           f"and its within-step fields stay within {TOLERANCE}",
                   "cross_step_fields_read": sorted(cross),
                   "cross_step_fields_left_out": cross_left_out,
                   "corpus_affordance_from": out["corpus_affordance_from"],
                   "cross_step_fields_lost": lost, "within_step_fields_also_lost": kept,
                   "holds": (None if not cross else bool(lost) and not kept),
                   "unreadable_because": (None if cross else
                                          "no certified cross-step field is both afforded by an "
                                          "arms document and varies anywhere; the round did not "
                                          "reach this prediction rather than falsifying it")}
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
                 "read_over": sorted(win),
                 "read_only_harness_lost_a_within_step_field":
                     [k for k in win for a in ("b", "c") if got(a, k) and got(a, k)["within_tolerance"] is False]}
    v["P4.4"]["holds"] = any(d["holds"] for d in v["P4.4"]["by_field"].values()) and \
                         not v["P4.4"]["read_only_harness_lost_a_within_step_field"]
    v["P4.5 (f)"] = {"rule": "arm (f) moves at least one within-step field on at least k of n documents",
                     "read_over": sorted(win),
                     "moved": {k: got("f", k)["count"] for k in win if got("f", k)},
                     "k": {k: got("f", k)["k"] for k in win if got("f", k)},
                     "holds": any(got("f", k) and got("f", k)["loses_field"] is True for k in win)}
    cc = {k: (got("cprime", k), got("c", k)) for k in cross}
    v["P4.5 (c')"] = {"rule": "arm (c') loses fewer cross-step fields than arm (c) on at least three more documents",
                      "by_field": {k: {"cprime": a["count"], "c": b["count"], "c_minus_cprime": b["count"] - a["count"]}
                                   for k, (a, b) in cc.items() if a and b},
                      "holds": any(b["count"] - a["count"] >= 3 for a, b in cc.values() if a and b)}
    half = (n + 1) // 2
    certified_all = sorted(set(win) | set(cross_all))
    v["PA.3 (x)"] = {"rule": f"the emission moves on at least one certified field on at least "
                             f"{max(4, half)} of {n} documents (W10 section 5 fixes four of eight)",
                     "read_over": certified_all,
                     "moved": {k: got("x", k)["count"] for k in certified_all if got("x", k)},
                     "moved_beyond_the_spread": {k: len(got("x", k).get("moved_beyond_the_a_to_a_spread", []))
                                                 for k in certified_all if got("x", k)},
                     "holds": any(got("x", k) and got("x", k)["count"] >= max(4, half)
                                  for k in certified_all)}
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
    print(f"  certified fields ({len(out['certified_fields'])}): {out['certified_from']}")
    print(f"  read-outs and gauges, beside and never inside a count: {out['read_outs_and_gauges']}")
    print(f"  the corpus-affordance table (W11 D4): {out['corpus_affordance_from']}")
    for name, row in out["fields"].items():
        b = row["baseline"]
        flags = []
        if not row["certified"]:
            flags.append("READ-OUT: carries no arm difference")
        if row["uninformative"]:
            flags.append("baseline over half the documents: this field says nothing")
        if row["never_varies"]:
            flags.append("never varies across every run of every arm")
        if row["afforded"] is False:
            flags.append("no arms document affords it")
        flag = ("  [" + "; ".join(flags) + "]") if flags else ""
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


def records_counts(reader, marks=None, crit=None):
    """The counts read from the run records, and the two that need the marks beside them.

    `marks` is a marks file's "marks" object: {run_id: {field: value}}. P4.9 is read over A4's
    marked modules_self_reported, never over any substring sweep of the report text (fault 11);
    P4.7 is read over the eleven test fields' CANNOT values (fault 12). Without a marks file
    both say so and hold nothing."""
    d = os.path.join(RUNS, reader)
    rows = []
    marks = marks or {}
    for fn in sorted(os.listdir(d)):
        if not fn.endswith(".json"):
            continue
        r = read_json(os.path.join(d, fn))
        served = sorted(set(r.get("modules_served") or []))
        mk = marks.get(r["run_id"]) or {}
        said = sorted(set(mk.get("modules_self_reported") or [])) if "modules_self_reported" in mk else None
        tl = r.get("tool_loop_requests")
        rows.append({"run": r["run_id"], "arm": r["arm"], "document": r.get("document"),
                     "requests": r.get("requests"), "tool_loop_requests": tl,
                     "steps": r.get("steps"),
                     "requests_equal_steps": (None if r.get("requests") is None or r.get("steps") is None
                                              else r["requests"] == r["steps"]),
                     "requests_minus_tool_loop_equal_steps":
                         (None if tl is None or r.get("requests") is None or r.get("steps") is None
                          else (r["requests"] - tl) == r["steps"]),
                     "modules_served": served,
                     "modules_self_reported_marked": said,
                     "modules_named_in_report": sorted(set(r.get("modules_named_in_report") or [])),
                     "traces_differ": (None if said is None else served != said)})

    # --- PA.1, by halves (W11 decision D2) ---------------------------------------------------
    plain = [x for x in rows if x["arm"] in ("b", "c", "cctl", "cprime", "d")
             and x["requests_equal_steps"] is False]
    adjusted = [x for x in rows if x["arm"] in ("b", "c", "cctl", "cprime", "d")
                and x["requests_minus_tool_loop_equal_steps"] is False]
    unreadable = [x["run"] for x in rows if x["arm"] in ("b", "c", "cctl", "cprime", "d")
                  and x["requests_minus_tool_loop_equal_steps"] is None]
    pa1 = {"rule": "W8 A1: exactly one request per step in arms (b), (c), (c') and (d), and more "
                   "than one in arm (a).",
           "first_half_read_as": "requests minus the tool-loop requests the rig served equals "
                                 "steps (W11 D2; the router is live in every arm and the record "
                                 "carries both numbers)",
           "runs_over_on_the_adjusted_count": [x["run"] for x in adjusted],
           "runs_over_on_the_plain_count": [x["run"] for x in plain],
           "both_counts_printed_so_a_later_reader_can_take_the_other_reading": True,
           "unreadable_runs": unreadable,
           "holds": (None if not [x for x in rows if x["arm"] in ("b", "c", "cctl", "cprime", "d")
                                  and x["requests_minus_tool_loop_equal_steps"] is not None]
                     else not adjusted)}
    pa1["arm_a_half"] = {
        "verdict": "NOT REACHED",
        "why": ("On DeepSeek arm (a) is five turns of one conversation: five requests for five "
                "steps, so the clause is falsified by this rig's own design and not by anything "
                "about the reader. On the Sonnet subagent transport a request inside one call is "
                "not observable from outside it. The half is therefore not reached on either "
                "transport and is reported as such, never as held or falsified (W11 decision D2)."),
        "arm_a_runs": [{"run": x["run"], "requests": x["requests"], "steps": x["steps"],
                        "tool_loop_requests": x["tool_loop_requests"]}
                       for x in rows if x["arm"] == "a"]}

    # --- P4.9 (fault 11) ----------------------------------------------------------------------
    have_marks = any(x["modules_self_reported_marked"] is not None for x in rows)
    opened = [x for x in rows if x["modules_served"]]          # "every run that opens a module"
    p49 = [x for x in opened if x["traces_differ"] is True]
    v = {"rows": rows,
         "PA.1": pa1,
         "P4.9": {"rule": "on every run that opens a module, the transport's record and the "
                          "reader's own list name the same modules; more than one difference "
                          "and the self-reported field carries no arm difference",
                  "read_over": "A4's marked modules_self_reported against the run record's "
                               "modules_served, on runs whose modules_served is not empty",
                  "runs_that_opened_a_module": len(opened),
                  "runs_where_they_differ": [x["run"] for x in p49],
                  "holds": (len(p49) <= 1) if have_marks else None,
                  "not_computed_because": (None if have_marks else
                                           "no marks file: A4's modules_self_reported is a "
                                           "marker's field and no substring sweep stands in for "
                                           "it")}}

    # --- P4.6, P-B7 and P4.8, from modules_served by arm and document (fault 12) --------------
    docs = sorted({x["document"] for x in rows if x["document"]})
    by = {}
    for x in rows:
        by.setdefault((x["arm"], x["document"]), []).append(x)

    def served_sets(arm, doc):
        return [frozenset(x["modules_served"]) for x in by.get((arm, doc), [])]

    half = (len(docs) + 1) // 2
    r_ran = any(by.get(("r", d)) for d in docs)
    moved = [d for d in docs
             if served_sets("r", d) and served_sets("a", d)
             and any(s not in served_sets("a", d) for s in served_sets("r", d))]
    v["P4.6"] = {"rule": "W3 P4.6: arm (r) shows a change in the modules-opened trace against arm "
                         "(a) in at least one of its three runs per document, on at least half "
                         f"the documents ({half} of {len(docs)})",
                 "read_over": "modules_served alone (criteria.json: 'P4.6 is read over "
                              "modules_served alone')",
                 "documents_where_the_trace_moved": moved,
                 "documents": docs,
                 "holds": (len(moved) >= half) if r_ran else None}
    v["P-B7"] = {"rule": "W8 B7: in every arm whose router is live, at least one read the reader "
                         f"itself chose on at least half the documents ({half} of {len(docs)})",
                 "read_over": "modules_served, per arm, per document",
                 "by_arm": {}, "holds": None}
    live = sorted({x["arm"] for x in rows})
    for a in live:
        got = [d for d in docs if any(s for s in served_sets(a, d))]
        v["P-B7"]["by_arm"][a] = {"documents_with_a_read_the_reader_chose": got,
                                  "holds": len(got) >= half if docs else None}
    v["P-B7"]["holds"] = (None if not docs else
                          all(r["holds"] for r in v["P-B7"]["by_arm"].values()))
    kruns = [x for x in rows if x["arm"] == "k"]

    def sizes(arm, d):
        return sorted(len(s) for s in served_sets(arm, d))

    every = [d for d in docs if sizes("k", d) and sizes("a", d)
             and max(sizes("k", d)) < min(sizes("a", d))]
    any_run = [d for d in docs if sizes("k", d) and sizes("a", d)
               and min(sizes("k", d)) < max(sizes("a", d))]
    v["P4.8"] = {"rule": "W8 C1: arm (a) under a copy of file 33 with the router table's rows "
                         "removed opens fewer modules than arm (a). W10 section 5 fixes no k for "
                         "this count, so the falsifier used is W8 C1's own: zero difference on "
                         "every document falsifies C1's claim that the table is the aspect doing "
                         "the work. Both readings are printed, as with PA.1",
                 "documents_where_every_k_run_opened_fewer_than_every_a_run": every,
                 "documents_where_some_k_run_opened_fewer_than_some_a_run": any_run,
                 "arm_k_ran": bool(kruns),
                 "modules_by_document": {d: {"a": [sorted(s) for s in served_sets("a", d)],
                                             "k": [sorted(s) for s in served_sets("k", d)]}
                                         for d in docs if by.get(("k", d))},
                 "holds": (None if not kruns else len(every) > 0)}

    # --- P4.7, the CANNOT count, from the marks (fault 12) -------------------------------------
    test_fields = [f["name"] for f in (crit or {}).get("fields", [])
                   if f["name"].startswith("test_")] or [
        "test_remove", "test_swap", "test_poke", "test_flip", "test_reverse", "test_hunt",
        "test_addjob", "test_rival", "test_pull", "test_patches", "test_inside"]
    cannot = {}
    for rid, mk in (marks or {}).items():
        got = [f for f in test_fields if str(mk.get(f)) == "CANNOT"]
        if got:
            cannot[rid] = got
    v["P4.7"] = {"rule": "W3 P4.7: under file 33 the reader is instructed to name a test that "
                         "cannot bite and leave its part unknown; the count of such "
                         "named-and-unknown verdicts is above zero. The record's CANNOT count "
                         "has been zero wherever it was applied",
                 "read_over": test_fields,
                 "runs_with_a_CANNOT": cannot,
                 "count": sum(len(x) for x in cannot.values()),
                 "holds": (None if not marks else sum(len(x) for x in cannot.values()) > 0),
                 "not_computed_because": (None if marks else "no marks file")}
    return v


def main():
    p = argparse.ArgumentParser()
    p.add_argument("cmd", nargs="?", default="runs", choices=["runs", "markers", "records"])
    p.add_argument("--marks", default="")
    p.add_argument("--first", default="")
    p.add_argument("--second", default="")
    p.add_argument("--criteria", default=None)
    p.add_argument("--certified", default="",
                   help="stage B's list of the fields that agreed there: a JSON file holding a "
                        "list of field names, or an object with a 'certified' list")
    p.add_argument("--reader", default="deepseek")
    p.add_argument("--out", default="")
    p.add_argument("--dry", action="store_true")
    o = p.parse_args()
    cert = None
    if o.certified:
        c = read_json(o.certified, "stage B's certified fields")
        cert = c if isinstance(c, list) else (c.get("certified") or c.get("fields"))
    if o.dry:
        crit = M.load(os.path.join(rig.FIXTURES, "criteria.example.json"))
        data = read_json(os.path.join(rig.FIXTURES, "marks.example.json"), "the example marks")
        out = run_agreement(crit, data, cert)
        print_run_table(out)
        print("\ndry run: read only the example marks in fixtures/, wrote nothing, sent nothing.")
        return
    crit = M.load(o.criteria)
    if o.cmd == "runs":
        data = read_json(o.marks or os.path.join(MARKING, f"marks_first_{o.reader}.json"), "a marks file")
        out = run_agreement(crit, data, cert)
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
    mp = o.marks or os.path.join(MARKING, f"marks_first_{o.reader}.json")
    marks = read_json(mp)["marks"] if os.path.exists(mp) else None
    out = records_counts(o.reader, marks, crit)
    if marks is None:
        print(f"no marks file at {mp}: P4.7 and P4.9 are not computed and say so.")
    for k in ("PA.1", "P4.6", "P4.7", "P4.8", "P4.9", "P-B7"):
        print(f"{k}: holds={out[k]['holds']}  {out[k]['rule']}")
        for kk, vv in out[k].items():
            if kk.startswith(("arms_", "runs_", "documents_")) and vv:
                print(f"   {kk}: {vv}")
    a = out["PA.1"]["arm_a_half"]
    print(f"PA.1, the arm (a) half: {a['verdict']}. {a['why']}")
    write_json(o.out or os.path.join(MARKING, f"records_counts_{o.reader}.json"),
               {"made_at": stamp(), "reader": o.reader, "marks_file": mp if marks else None, **out})


if __name__ == "__main__":
    main()
