"""S108 Part A round 2: the dependency map after the GLM cross-examination (rule 4 of the cross-examination's reading rule).
Reads the map after round 2 (.json, never written; md5 asserted) and writes a corrected copy with every amendment marked by
the objection id that caused it (the settlement: `results/S108 Part A round 2 - the GLM cross-examination, settled.md`).
  python3 -B s108r2x_map_amend.py        writes the corrected .json and prints the new counts
Standard library only. The touched-count logic is the round-2 builder's (map after round 2/s108r2_map_build.py), unchanged.
"""
import copy, hashlib, json, re
from collections import Counter, OrderedDict

RES = "/home/user/ThreadSmith/Semantics/results/"
INJ = RES + "S108 Part A round 2 - the dependency map, after round 2.json"
OUTJ = RES + "S108 Part A round 2 - the dependency map, after the cross-examination.json"
XA1 = "S108 Part A round 2 - computation/cross-examination runs/Xa1 section 2 worked cases, rerun/"


def md5(p):
    return hashlib.md5(open(p, "rb").read()).hexdigest()


IN_MD5 = md5(INJ)
M = json.load(open(INJ, encoding="utf-8"))
M0 = copy.deepcopy(M)
edges = OrderedDict((e["id"], e) for e in M["edges"])
nodes = OrderedDict((n["id"], n) for n in M["nodes"])
amend = []   # (objection, edge or place, what)


def note(e, obj, text):
    e.setdefault("cross_examination", []).append({"objection": obj, "amendment": text})
    amend.append(OrderedDict(objection=obj, where=e["id"], amendment=text))


def split(eid, keep_to, part_to, part_label, part_standing, why, obj, part_id=None, keep_standing=None):
    """Keep the edge with keep_to (standing unchanged unless keep_standing); add <eid>b with part_to and part_standing."""
    e = edges[eid]
    b = copy.deepcopy(e)
    b.pop("cross_examination", None)
    if keep_to is not None:
        e["to"] = keep_to
    if keep_standing:
        e["standing"] = keep_standing
    note(e, obj, "split: the part(s) %s moved to %s (%s)" % (part_label, part_id or eid + "b", part_standing))
    b.update(id=part_id or eid + "b", to=part_to, to_label=part_label, standing=part_standing, what_shows_it=why,
             source=e["source"] + " (split after the cross-examination, %s)" % obj)
    if part_standing != "computed":
        b["what_would_settle"] = b.get("what_would_settle") or ""
    note(b, obj, "the part of %s whose standing differs from its row's headline: %s" % (eid, why))
    # insert b right after e
    items = list(edges.items())
    i = [k for k, _ in items].index(eid)
    items.insert(i + 1, (b["id"], b))
    edges.clear()
    edges.update(items)


# ---- Xc1: rows whose parts differ in standing are split (round 1's convention; correction O2's lesson)
split("r2e3.18", ["X:(Suff)"], ["X:(Nec)", "D10.1"], "X:(Nec), D10.1 [FROZEN]", "claimed only",
      "section 3 §8 (R3E18): D10.1 and (Nec) not computed", "Xc1")
split("r2e3.22", ["D13.1", "D14.7"], ["D13.2", "D16.1"], "D13.2 [FROZEN], D16.1 [FROZEN]", "claimed only",
      "section 3 (R3E22): D13.2, D16.1 not computed", "Xc1")
split("r2e3.17", ["D9.6", "D9.7"], ["L397.s16"], "L397.s16 [S3]", "claimed only",
      "section 3 (R3E17): L397.s16 a sentence the program does not read", "Xc1")
split("r2e3.03", [t for t in edges["r2e3.03"]["to"] if t != "L55.n3"], ["L55.n3"], "L55.n3 [S1]", "claimed only",
      "section 3 (R3E04): L55.n3 a sentence the program does not read", "Xc1")
split("r2e2.18", [t for t in edges["r2e2.18"]["to"] if t != "L231.s3"], ["L231.s3"], "L231.s3 [S2]", "claimed only",
      "section 2 (R2E23): L231.s3's word not computed", "Xc1")
split("r2e2.20", None, [], "Surp at a pair of H (the reply's claim under R2V2.10)", "contradicted",
      "section 2 §10 (R2E25): Surp F at the pair of H (D12.7 asks (a,b) ∉ H); Viol T there (rerun: cross-examination runs/Xa1…/section 4)", "Xc1")
split("r2e2.21", ["D12.8"], ["D12.1"], "D12.1 [S2]", "contradicted",
      "section 2 (R2E26): D12.1 unchanged under R2V2.10 (a 'changes with' the computation does not show)", "Xc1")
split("r2e2.16", [t for t in edges["r2e2.16"]["to"] if t != "X:(Nec)"], ["X:(Nec)"], "X:(Nec) (as L538 states it)", "contradicted",
      "section 2 §8 (R2E21): (Nec) as L538 states it independent of R2V2.8", "Xc1")
split("r2e4.09", ["FC103.new1", "L630.n3", "L630.s4"], ["L630.s5"], "L630.s5 [S4]", "claimed only",
      "section 4 (R4E10): L630.s5 not computed", "Xc1")
split("r2e2.13", None, ["X:Dec", "X:Expl"], "X:Dec, X:Expl (R2V2.6 at the reply's reach: the whole exclusion dropped)", "computed",
      "section 2 §4, §10 (R2E16): with the whole exclusion of D12.1 dropped the student's copy becomes Sel (51 of 51 accounts where an "
      "earlier occurrence represents cod t); C21's ground (rerun: cross-examination runs/Xa1…/section 4)", "Xc1")
# the same shape in a round-1 edge settled in round 2 (found while applying Xc1)
split("e1.46", ["X:(Suff)", "FC106"], ["X:(Nec)"], "X:(Nec) (as L538 states it)", "contradicted",
      "section 2 §8: (Nec) as L538 states it independent of V1.6's formula (R2V2.8)", "Xc1")

# ---- Xb1: R2V4.3 (e) turns on reading "Sel at o" (run: cross-examination runs/xb1_e_readings.py)
XB1 = ("(e) as computed (S108r2-4-I3: a holding of t with Sel's conditions staged there, or a trace): 25 held outputs of 3,208 move; "
       "a holding of t with Sel read as the fixed point's value (inherited): 4; any holding with Sel as the fixed point's value, or a trace "
       "(the objection's reading): 0")
e = edges["r2e4.06"]
e["what_shows_it"] = "under S108r2-4-I3: 25 held outputs move (§3); " + XB1
note(e, "Xb1", "qualified: contradicted under S108r2-4-I3's reading (and under the inherited value at a holding of t: 4), not under the objection's")
split("r2e4.06", None, ["X:Expl"], "X:Expl on chains (the reply's lemma), 'Sel at o' read as the fixed point's value at any holding",
      "computed", "0 moves of 3,208 chains: the reply's lemma holds on this reading. " + XB1, "Xb1")
e = edges["r2e4.05"]
note(e, "Xb1", "qualified: (e) departs from D12.4 on 25 held relays under S108r2-4-I3 only")
split("r2e4.05", None, ["D12.4"], "D12.4 [FROZEN], 'Sel at o' read as the fixed point's value at any holding", "contradicted",
      "0 departures: on this reading (e) returns D12.4's inherited value everywhere. " + XB1, "Xb1")

# ---- Xb3, Xc4: R2V4.8's claim parts: the evidence re-pointed; no suite run under U (a parameter, not a switch)
e = edges["r2e4.17"]
e["what_shows_it"] = ("FC98 (c) and FC32.new1 (b) compute cut U beside K, T, T′ in every off run (U: two fixed points for a first construction, "
                      "none for a selection; the cycle Live → (K2) → Live): cross-examination runs/'Xb3 Xc4 - FC98 and FC32.new1 off…'; "
                      "section 4 §2 R2V4.8 row and worlds (U: 2 or 0 fixed points on every account). No whole-suite run under U: the cut "
                      "is a function parameter the claims already enumerate, not a switch (a departure recorded after the cross-examination)")
e["standing_as_written"] = "computed (section 4 §2; FC98 (c), FC32.new1 (b) off)"
note(e, "Xb3/Xc4", "evidence re-pointed from '§8' (no R2V4.8 suite run exists) to the claims' own parts and section 4 §2")
e = edges["r2e4.04"]
e["what_shows_it"] = "round 1's whole-suite run under V4.2 (the three shapes); section 4 §2 (R2V4.2's small case). No round-2 suite run of R2V4.2"
note(e, "Xb3", "evidence re-pointed from 'the whole suite §8' (no R2V4.2 run there) to round 1's suite and section 4 §2")

# ---- Xc3: e2.38 and e2.39 carry the round-2 closure the builder dropped (a trailing comma in section 2's .json)
changes = M["round2"]["changes"]
for rid in ("e2.38", "e2.39"):
    e = edges[rid]
    e["round2_note"] = ("the gap it names is closed in round 2 (R2V2.11): FC21.v2 holds off, counterexample under V2.2; FC21.v1 holds off, "
                        "counterexample under V2.1; with them the suite separates D6.4 from both (section 2 §8)")
    note(e, "Xc3", "round-2 closure recorded on the edge (section 2's .json row 'settles e2.38,' was skipped by the builder)")
    changes.append(OrderedDict(edge=rid, round1_standing=e["standing"], after_round2=e["standing"],
                               what_changed_it="section 2, R2V2.11 (FC21.v1, FC21.v2) [Xc3]",
                               why="the suite's blind spot is closed: " + e["round2_note"]))

# ---- Xa1: the section-2 worked-case numbers now rest on a surviving run
for rid in ("r2e2.02", "r2e2.05", "r2e2.06", "e2.06c", "e2.07"):
    e = edges[rid]
    note(e, "Xa1", "the numbers are reproduced by the rerun after the cross-examination (%s); the earlier runs ended at the timeout" % XA1)

# ---- assemble, recompute touched (the round-2 builder's logic)
all_edges = list(edges.values())
for n in nodes.values():
    n["edges_in"] = []
for e in all_edges:
    for t in e.get("to", []):
        if t in nodes:
            nodes[t]["edges_in"].append({"edge": e["id"], "kind": e["kind"], "standing": e["standing"], "variants": e.get("variants", [])})
DEF_OF = {"X:(E)": ["D6.7"], "X:(F1)": ["D5.4"], "X:(F2)": ["D5.5"], "X:(A)": ["D5.6"], "X:Dependence": ["D6.5", "D6.4", "D6.2", "D6.1"],
          "X:NonVacuous": ["D6.6"], "X:Dec": ["D12.3"], "X:Expl": ["D16.XV"], "X:(Suff)": ["D16.XV"], "X:(Nec)": ["D16.XV"]}
before = {i: n["touched"] for i, n in nodes.items()}
for n in nodes.values():
    st = [x["standing"] for x in n["edges_in"]]
    if n.get("varied_by") or n.get("varied_by_round2") or "computed" in st or "contradicted" in st:
        n["touched"] = "computed"
    elif "claimed only" in st or "not settled by computation" in st:
        n["touched"] = "claimed only"
    else:
        n["touched"] = "untouched"
for x, ds in DEF_OF.items():
    if nodes[x]["touched"] == "computed":
        for d in ds:
            if nodes[d]["touched"] != "computed":
                nodes[d]["touched"] = "computed"
touch_changed = {i: (before[i], n["touched"]) for i, n in nodes.items() if before[i] != n["touched"]}
tmpl = [n for n in nodes.values() if n["kind"] in ("sentence", "definition")]
mid = [n for n in tmpl if n["mark"] not in ("FROZEN", "–")]
by_stretch = {}
for n in tmpl:
    k = (n.get("stretch", "?"), "FROZEN" if n["mark"] == "FROZEN" else "middle")
    by_stretch.setdefault(k, Counter())[n["touched"]] += 1
r2 = [e for e in all_edges if e["id"].startswith("r2e")]
M["edges"] = all_edges
M["nodes"] = list(nodes.values())
M["counts"] = OrderedDict(nodes=len(nodes), edges=len(all_edges), edges_round1=M0["counts"]["edges_round1"], edges_round2=len(r2),
                          edges_by_standing=dict(Counter(e["standing"] for e in all_edges)),
                          edges_by_kind=dict(Counter(e["kind"] for e in all_edges)),
                          round2_edges_by_standing=dict(Counter(e["standing"] for e in r2)),
                          template_items_touched=dict(Counter(n["touched"] for n in tmpl)),
                          template_items_touched_round1=M0["counts"]["template_items_touched_round1"],
                          middle_items_untouched=sum(1 for n in mid if n["touched"] == "untouched"),
                          before_the_cross_examination=M0["counts"])
M["gaps"]["edges_claimed_only"] = sorted(e["id"] for e in all_edges if e["standing"] == "claimed only")
M["gaps"]["touched_by_stretch"] = {"%s %s" % k: dict(v) for k, v in sorted(by_stretch.items())}
M["gaps"]["untouched_middle_definitions"] = sorted(n["id"] for n in tmpl if n["kind"] == "definition" and n["mark"] != "FROZEN" and n["touched"] == "untouched")
M["gaps"]["readings_computed_one_way_only_added"] = [
    {"objection": "Xc5", "reading": "S108-4-I7: round 1's V4.7 (D16.3, Enable) computed on a toy only; D16.3 not varied again in round 2",
     "bears_on_the_explanation_definition": "no: by D18.1's graph Enable is reached by UU, UC, UECS and Classes only; (E), Dec and the defeat conditions do not reach it (round 1's map, e4.35)"},
    {"objection": "Xb1", "reading": "R2V4.3 (e): 'Sel at o' read at the holding's staged conditions (S108r2-4-I3), at the holding's fixed-point value, or at any holding",
     "bears_on_the_explanation_definition": "yes, as C13's fifth reading: 25 / 4 / 0 held outputs of 3,208 chains"},
]
M["gaps"]["middle_definitions_never_varied_note"] = (
    "[Xc2] D6.5, D12.3, D18.1 are upstream of (E) or Dec and never varied themselves: D6.5 is NC0 ∧ NC2 with NC0 true of every candidate "
    "(D6.2), so it varies only through D6.4 (V2.1, V2.2, V2.3, V2.3b) and through the conjunct V2.4 restores (its pre-S106 form); D12.3 is "
    "D12.4's inheritance [FROZEN] and the complement of Sel ∨ Con, whose parts were varied by fourteen variants over two rounds, and whose "
    "Boolean form, varied, gives only the limits the list already carries (every Con history declared: C8's, C20's direction at its widest; "
    "every Sel history declared: C16's; the rule dropped: C12); D18.1 is the order, varied through L526.s18 (R2V4.8: no value) and "
    "computed in FC32.new1 and FC98 under every cut. See the map's §7 after the cross-examination.")
M["round2"]["changes"] = changes
M["cross_examination"] = OrderedDict(
    rule="results/S108 Part A round 2 - how the GLM cross-examination will be read, written before sending.md",
    settled="results/S108 Part A round 2 - the GLM cross-examination, settled.md",
    input_map={"path": INJ[len(RES) - len("results/"):], "md5": IN_MD5},
    amendments=amend, touched_changed={k: list(v) for k, v in touch_changed.items()})
FL = {c["id"]: c for c in M["candidates"]}
FL["C2"]["decisions_after_round2"] = ["S44 (on that reading)", "S41 Q15 (on that reading)",
                                      "S41 Q6 (on that reading: the question's history; the bridge's history with a first design criticized (a2); 'created' read as CreateEx; p_c the brief) [Xd1]"]
FL["C16"]["decisions"] = ["S41 Q2 ('No, not if just declared'; the question it answered was Claude's) [Xd2]", "S44 (on a selection history)", "S41 Q15 (on a selection history)"]
FL["C13"]["note_after_the_cross_examination"] = "[Xb1] reading (e)'s 25 drops hold under S108r2-4-I3 only; 4 with the inherited value at a holding of t; 0 at any holding"
M["third_round_needed"] = ("no [Xc2 settled]: no gap bearing on the explanation definition remains that a variant inside Part A's rule could reach "
                           "and that the computation has not already given; D5.7 belongs to Part B; the readings the owner's cases turn on are the owner's. "
                           "Part A ends; Part B follows (S52). See the settled file's §4.")
M["about"] = M0["about"] + " AFTER THE GLM CROSS-EXAMINATION: a corrected copy of the map after round 2 (which is kept as it was sent); every amendment carries its objection id (cross_examination)."
json.dump(M, open(OUTJ, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
assert md5(INJ) == IN_MD5
print("COUNTS", json.dumps({k: v for k, v in M["counts"].items() if k != "before_the_cross_examination"}, ensure_ascii=False))
print("TOUCHED CHANGED", touch_changed)
print("STRETCH", M["gaps"]["touched_by_stretch"])
print("UNTOUCHED MID DEFS", M["gaps"]["untouched_middle_definitions"])
print("CLAIMED ONLY", len(M["gaps"]["edges_claimed_only"]))
print("AMENDMENTS", len(amend))
