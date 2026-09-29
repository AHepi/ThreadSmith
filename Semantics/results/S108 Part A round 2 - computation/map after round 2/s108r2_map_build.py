"""S108 Part A round 2, rule 6: the dependency map after round 2 (.json; the .md's generated tables).
Built by the one Opus 5.5 agent of S56 on round 1's corrected map (results/S108 Part A - the dependency map.json,
7ce9b1c65b55487d79f0c1a427adc2d9, read, never written), the four round-2 "variants computed" .json files, the whole-suite
runs of round 2, and the corrections from the Opus review of the Sonnet 5.5 trial (O1-O4 of round 1's section-2 work).
  python3 -B s108r2_map_build.py      writes the map's .json and prints the generated tables (markdown) to stdout
"""
import copy, hashlib, json, os, re, sys
from collections import Counter, OrderedDict

SEM = "/home/user/ThreadSmith/Semantics/"
RES = SEM + "results/"
R1MAP = RES + "S108 Part A - the dependency map.json"
R1MD5 = "7ce9b1c65b55487d79f0c1a427adc2d9"
SECJ = [RES + "S108 Part A round 2 - section %d - variants computed.json" % n for n in (1, 2, 3, 4)]
SUITE = RES + "S108 Part A round 2 - computation/whole suite/"
OUTJ = RES + "S108 Part A round 2 - the dependency map, after round 2.json"
REVIEW = RES + "S108 Part A - Sonnet 5.5 trial/Opus review of the Sonnet 5.5 trial.md"


def md5(p):
    return hashlib.md5(open(p, "rb").read()).hexdigest()


assert md5(R1MAP) == R1MD5, "round 1's map is not at its md5"
r1 = json.load(open(R1MAP, encoding="utf-8"))
M = copy.deepcopy(r1)
nodes = OrderedDict((n["id"], n) for n in M["nodes"])
for n in nodes.values():
    n["round1_touched"] = n["touched"]

# ------------------------------------------------------------------ round-2 variants: implemented, and what each varies
VARIED = {
    "R2V1.1": ["D3.4"], "R2V1.6": ["L11.s1"], "R2V1.10": ["D1.4"],
    "R2V2.1": [], "R2V2.2": ["D6.3"], "R2V2.3": [], "R2V2.5": ["D6.9"], "R2V2.6": ["D11.2"], "R2V2.8": ["D6.7", "D3.6"],
    "R2V2.9": ["D6.8"], "R2V2.10": ["D12.7"], "R2V2.11": [],
    "R2V3.1": ["D12.2", "D13.3"], "R2V3.2": ["D13.8"], "R2V3.3": ["D13.3"], "R2V3.4": ["D15.8"], "R2V3.5": ["D15.8"],
    "R2V3.6": [], "R2V3.7": ["D11.3"], "R2V3.8": ["D9.2"], "R2V3.9": ["D9.1"], "R2V3.10": ["D15.5"],
    "R2V4.1": ["D16.XV"], "R2V4.2": ["D16.XV"], "R2V4.3": ["D16.XV"], "R2V4.4": [], "R2V4.5": ["E9"], "R2V4.6": ["L524.s2"],
    "R2V4.7": ["L522.s1"], "R2V4.8": ["L526.s18"], "R2V4.10": ["D18.2"],
}
NOT_IMPLEMENTED = {"R2V1.2": "L155.s6 [FROZEN] in effect", "R2V1.3": "D13.8 [S3] in effect", "R2V1.4": "L155.s6 [FROZEN] in effect",
                   "R2V1.5": "D16.XV [S4] in effect", "R2V1.7": "D4.2 [FROZEN] in effect", "R2V1.8": "D3.2, E4 [FROZEN] possibly",
                   "R2V1.9": "D3.1 [FROZEN] as written", "R2V2.4": "D12.4 [FROZEN] possibly", "R2V2.7": "L189.s2 [FROZEN] in effect",
                   "R2V4.9": "repeats round 1's V4.8 and adds prose"}

ID = re.compile(r"X:\((?:E|F1|F2|A|Suff|Nec)\)|X:(?:Dec|Expl|Dependence|NonVacuous)|\bL\d+\.[sn]\d+(?:[–-][sn]?\d+)?|"
                r"\bD\d+\.(?:\d+|new\d+|XV)\b|\bE\d\b|\bFC\d+(?:\.new\d|\.v\d)?\b|\bFC-E\d\b")


def ids_in(text):
    out = []
    t = re.sub(r"(?<!X:)\((Suff|Nec)\)", r"X:(\1)", text)
    for m in ID.finditer(t):
        s = m.group(0)
        r = re.match(r"(L\d+)\.([sn])(\d+)[–-][sn]?(\d+)$", s)
        if r:
            for k in range(int(r.group(3)), int(r.group(4)) + 1):
                for kind in "sn":
                    i = "%s.%s%d" % (r.group(1), kind, k)
                    if i in nodes:
                        out.append(i)
            continue
        out.append(s)
    return list(OrderedDict.fromkeys(out))


def ensure_node(i):
    if i not in nodes:
        kind = "claim" if i.startswith("FC") else ("definition" if re.match(r"D\d|E\d", i) else "other")
        nodes[i] = {"id": i, "kind": kind, "mark": "–", "title": "named first in round 2", "varied_by": [], "edges_in": [],
                    "touched": "untouched", "round1_touched": "absent"}
    return nodes[i]


# ------------------------------------------------------------------ round-2 edges from the four section files
secs = [json.load(open(p, encoding="utf-8")) for p in SECJ]
new_edges, settles = [], {}
for n, sj in zip((1, 2, 3, 4), secs):
    for k, e in enumerate(sj["edges"]):
        v = e["variant"]
        m = re.match(r"(V\d\.\d+) \(round 1; (e\d\.\d+\w?)\)", v)
        rid = e.get("round1_edge") or (m.group(2) if m else "")
        if rid:
            settles.setdefault(rid, []).append(dict(section=n, standing=e["standing"], evidence=e["evidence"],
                                                    as_written=e.get("standing_as_written", e["standing"]),
                                                    settlement=e.get("settlement", e.get("item", ""))))
            continue
        to = ids_in(e["item"])
        st0 = e["standing"]
        st = {"added": "computed", "not settled by computation": "claimed only"}.get(st0, st0)
        kind = re.split(r" \(| /", e["kind"])[0]
        new_edges.append(OrderedDict(id="r2e%d.%02d" % (n, k), source="section %d .json, edge %d (%s)" % (n, k, e.get("id", "")),
                                     variants=[re.split(r"[ ,–]", v)[0]], from_=VARIED.get(re.split(r"[ ,–]", v)[0], []),
                                     kind=kind, kind_as_written=e["kind"], to=to, to_label=e["item"], standing=st,
                                     standing_as_written=e.get("standing_as_written", st0),
                                     named_by=e.get("named_by", "") or ("the computing agent (added)" if st0 == "added" else ""),
                                     implemented=re.split(r"[ ,–]", v)[0] not in NOT_IMPLEMENTED,
                                     what_shows_it=e["evidence"],
                                     what_would_settle=e.get("what_would_settle", "") if st != "computed" else ""))

# ------------------------------------------------------------------ changes to round-1 edges (recorded, round-1 standing kept beside)
edges = OrderedDict((e["id"], e) for e in M["edges"])
changes = []


def change(eid, new, why, by):
    e = edges[eid]
    changes.append(OrderedDict(edge=eid, round1_standing=e["standing"], after_round2=new, what_changed_it=by, why=why))
    e["round1_standing"] = e["standing"]
    e["standing"] = new
    e["changed_in_round2"] = {"by": by, "why": why}


RULE = {  # round-1 edge -> (new standing, why, by) where the section's settlement needs a reading beyond its standing
    "e2.09": ("claimed only", "the owner's yes or no (S45, S52); no computation settles it", "section 2 §8 (noted)"),
    "e3.37b": ("claimed only", "the owner's yes or no (S47 with S41 Q6)", "section 3 §7 (noted)"),
}
OVERRIDE = {  # a settlement whose parts differ: the round-1 edge's own claim decides its standing
    "e2.19": "contradicted",     # the edge claims V2.7 changes with D8.6: contradicted as to D8.6 (computed for the argument from ConfCl)
}
for rid, ss in sorted(settles.items()):
    if rid not in edges:
        continue
    s = ss[0]
    if rid in RULE:
        st, why, by = RULE[rid]
        edges[rid]["round2_note"] = why
        continue
    if rid == "e4.40":
        continue      # split below
    if rid in ("e2.38", "e2.39"):
        edges[rid]["round2_note"] = "the gap it names is closed in round 2: " + s["evidence"]
        changes.append(OrderedDict(edge=rid, round1_standing=edges[rid]["standing"], after_round2=edges[rid]["standing"],
                                   what_changed_it="section 2, R2V2.11 (FC21.v1, FC21.v2)",
                                   why="the suite's blind spot is closed: " + s["evidence"]))
        continue
    new = OVERRIDE.get(rid) or {"computed": "computed", "contradicted": "contradicted", "not settled by computation": "claimed only"}[s["standing"]]
    if new == edges[rid]["standing"] and new == "claimed only":
        edges[rid]["round2_note"] = "round 2 proposed a settlement and could not compute it: " + s["evidence"]
        changes.append(OrderedDict(edge=rid, round1_standing="claimed only", after_round2="claimed only",
                                   what_changed_it="section %d (not settled)" % s["section"], why=s["evidence"]))
        continue
    change(rid, new, "%s: %s" % (s["as_written"], s["evidence"]), "section %d, round 2" % s["section"])

# e4.40: split by part (section 4 §6)
e = edges["e4.40"]
base = dict(e)
parts = [("e4.40a", ["L572.s2", "L574.s5"], "changes with", "computed",
          "the pole, 𝒯 = {t, t_ab,H}: L572.s2's condition (a surviving differer) at 0 of 2 unseen pairs, V4.8's Underdet at 2; survivors agree at 2 (L574.s5)"),
         ("e4.40b", ["L574.n4"], "changes with", "contradicted",
          "L574.n4's route (t_ab survives on H at every unseen pair, t_ab,H at none) is the same under V4.8"),
         ("e4.40c", ["L576.s1", "L576.s4"], "changes with", "claimed only",
          "turns on reading 'admits an alternative' (L576.s1); not computed")]
del edges["e4.40"]
for pid, to, kind, st, why in parts:
    x = dict(base)
    x.update(id=pid, to=to, kind=kind, standing=st, round1_standing="claimed only", what_shows_it=why,
             changed_in_round2={"by": "section 4, round 2 (§6)", "why": why}, source=base["source"] + " (split in round 2)")
    edges[pid] = x
    changes.append(OrderedDict(edge=pid, round1_standing="claimed only (e4.40)", after_round2=st,
                               what_changed_it="section 4, round 2 (§6)", why=why))

# the orchestrator's rulings on round 1's nine claimed-only edges no share named
for rid, why in (("e1.45", None), ("e1.46", None), ("e1.47", None)):
    pass   # settled by section 2 (R2V2.8) above
for rid in ("e1.48", "e1.49", "e1.50", "e1.51"):
    edges[rid]["round2_note"] = "V1.7: to Part B (the orchestrator's decision 3 on round 1's review); not computed in round 2"
for rid in ("e2.20", "e2.21"):
    edges[rid]["round2_note"] = "V2.8's D16.XV part is V4.4's reading, computed in round 1; its L315.s7 part to Part B (decision 3)"

# ------------------------------------------------------------------ corrections from the review of the Sonnet 5.5 trial (O1-O4)
CORR = [
    ("O1", "e2.O1", ["V2.6"], ["D8.2"], "moves", ["FC50"], "computed",
     "V2.6 empties FC50 (a)'s hypothesis (572 → 0): FC50 (a) holds vacuously under V2.6 (the Sonnet 5.5 trial's count, "
     "rerun by the Opus review); round 1's section 2 left the claim counts out as 'timed', but these searches are seeded and "
     "run to the end"),
    ("O2", None, None, None, None, None, None,
     "round 1's section 2 marked R12, R15, R17 computed with a part unsettled: R12 and R17 were already split by the map "
     "(e2.11a/b, e2.16a/b/c); R15 is split here: e2.14 keeps X:Dec, X:Expl computed; its X:(Suff) part is claimed only (e2.14b)"),
    ("O3", "e2.O3", ["V2.2"], ["D6.4"], "changes with", ["FC46", "FC29", "FC37", "FC51"], "computed",
     "under V2.2 FC46's accounts drop 962 → 927 and the counts of FC29, FC37, FC51 move (no status moves): round 1's N16 "
     "(e2.38) wording 'no claim builds a candidate whose Dependence needs a block of two or more' is withdrawn; its gap (no "
     "claim's result separates V2.2) held after round 1 and is closed in round 2 by FC21.v2"),
    ("O4", "e2.O4", ["V2.3b"], ["D6.4"], "moves", ["X:(E)"], "computed",
     "V2.3's second reading, the witness pair read through τ (τ(a) ≠ 1): 6 accounts on τ[C] ⊆ {1}×B that survive V2.3 drop "
     "under V2.3b (the Sonnet 5.5 trial; rerun by the Opus review); C5 rests on this reading too"),
]
corrections = []
for oid, eid, var, frm, kind, to, st, why in CORR:
    corrections.append(OrderedDict(id=oid, edge=eid or "e2.14", correction=why))
    if eid:
        for t in to:
            ensure_node(t)
        edges[eid] = OrderedDict(id=eid, source="correction %s (Opus review of the Sonnet 5.5 trial)" % oid, variants=var,
                                 **{"from": frm}, kind=kind, to=to, to_label=", ".join(to), standing=st, condition="",
                                 named_by="the review of the Sonnet 5.5 trial", claimed_by="", what_shows_it=why,
                                 what_would_settle="", note="a recorded correction to round 1's map", reply_why="")
e14 = edges["e2.14"]
e14b = dict(e14)
e14["to"] = [t for t in e14["to"] if t != "X:(Suff)"]
e14["correction"] = "O2: split; the X:(Suff) part is e2.14b"
e14b.update(id="e2.14b", to=["X:(Suff)"], standing="claimed only", round1_standing="computed (as part of e2.14)",
            what_would_settle="(Suff)'s defeat set under V2.5 on the 'nothing tried' history (claims_s41.suff_defeats), not computed in either round",
            correction="O2: the part of R15 its own row left uncomputed")
edges["e2.14b"] = e14b
changes.append(OrderedDict(edge="e2.14b", round1_standing="computed (in e2.14)", after_round2="claimed only",
                           what_changed_it="correction O2", why="the (Suff) part of R15 was not computed"))
edges["e2.38"]["correction"] = "O3: " + CORR[2][7]

# ------------------------------------------------------------------ assemble; touched
all_edges = list(edges.values())
for e in new_edges:
    e = OrderedDict((("from" if k == "from_" else k), v) for k, v in e.items())
    all_edges.append(e)
for n in nodes.values():
    n["edges_in"] = []
    n["varied_by_round2"] = []
for v, items in VARIED.items():
    for i in items:
        ensure_node(i)["varied_by_round2"].append(v)
for e in all_edges:
    for t in e.get("to", []):
        ensure_node(t)["edges_in"].append({"edge": e["id"], "kind": e["kind"], "standing": e["standing"], "variants": e.get("variants", [])})
DEF_OF = {"X:(E)": ["D6.7"], "X:(F1)": ["D5.4"], "X:(F2)": ["D5.5"], "X:(A)": ["D5.6"], "X:Dependence": ["D6.5", "D6.4", "D6.2", "D6.1"],
          "X:NonVacuous": ["D6.6"], "X:Dec": ["D12.3"], "X:Expl": ["D16.XV"], "X:(Suff)": ["D16.XV"], "X:(Nec)": ["D16.XV"]}
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
tmpl = [n for n in nodes.values() if n["kind"] in ("sentence", "definition")]
touched = Counter(n["touched"] for n in tmpl)
mid = [n for n in tmpl if n["mark"] not in ("FROZEN", "–")]
by_stretch = {}
for n in tmpl:
    k = (n.get("stretch", "?"), "FROZEN" if n["mark"] == "FROZEN" else "middle")
    by_stretch.setdefault(k, Counter())[n["touched"]] += 1
untouched_mid_defs = sorted(n["id"] for n in tmpl if n["kind"] == "definition" and n["mark"] != "FROZEN" and n["touched"] == "untouched")
never_varied_mid_defs = sorted(n["id"] for n in tmpl if n["kind"] == "definition" and n["mark"] != "FROZEN"
                               and not n.get("varied_by") and not n.get("varied_by_round2"))
st_counts = Counter(e["standing"] for e in all_edges)
kind_counts = Counter(e["kind"] for e in all_edges)
r2_counts = Counter(e["standing"] for e in new_edges)
claimed = sorted(e["id"] for e in all_edges if e["standing"] in ("claimed only", "not settled by computation"))

# ------------------------------------------------------------------ the whole-suite runs of round 2
suite = OrderedDict()
for sec in sorted(os.listdir(SUITE)):
    d = os.path.join(SUITE, sec)
    if not os.path.isdir(d) or not sec.startswith("section"):
        continue
    for f in sorted(os.listdir(d)):
        if not f.endswith(".json"):
            continue
        try:
            r = json.load(open(os.path.join(d, f), encoding="utf-8"))
        except Exception:
            continue
        if "counts" not in r:
            suite["%s/%s" % (sec, f[:-5])] = {"ok": False, "note": r.get("refused", "no result")}
            continue
        moved = sorted({x["id"] for x in r.get("differences", [])})
        parts_only = sorted({x["id"] for x in r.get("differences", []) if x["what"] == "parts"} -
                            {x["id"] for x in r.get("differences", []) if x["what"] == "status"})
        suite["%s/%s" % (sec, f[:-5])] = OrderedDict(counts=r["counts"], timed_out=r["timed_out"], seconds=r["seconds"],
                                                     folder_changed=r["model_folder_changed"], moved=moved, parts_only=parts_only,
                                                     not_in_record=r.get("claims_not_in_record", []), claims_with_error=r.get("claims_with_error", []))

M["about"] = ("S108 Part A round 2, rule 6: the dependency map after round 2, built on round 1's corrected map (never written), "
              "by the one Opus 5.5 agent of decision S56. Round-1 edges keep their standing unless a round-2 computation or a "
              "recorded correction changes it (each change in 'changes', with the round-1 standing); round-2 edges are r2e<section>.<k>.")
M["inputs"] = OrderedDict([("round 1 map .json", {"path": R1MAP[len(SEM):], "md5": R1MD5})] +
                          [("section %d .json" % n, {"path": p[len(SEM):], "md5": md5(p)}) for n, p in zip((1, 2, 3, 4), SECJ)] +
                          [("review of the Sonnet 5.5 trial", {"path": REVIEW[len(SEM):], "md5": md5(REVIEW)})])
M["nodes"] = list(nodes.values())
M["edges"] = all_edges
M["round2"] = OrderedDict(variants_implemented=VARIED, variants_not_implemented=NOT_IMPLEMENTED, changes=changes,
                          corrections=corrections, suite=suite)
M["counts"] = OrderedDict(nodes=len(nodes), edges=len(all_edges), edges_round1=len(r1["edges"]), edges_round2=len(new_edges),
                          edges_by_standing=dict(st_counts), edges_by_kind=dict(kind_counts), round2_edges_by_standing=dict(r2_counts),
                          template_items_touched=dict(touched), template_items_touched_round1=r1["counts"]["template items touched"],
                          middle_items_untouched=sum(1 for n in mid if n["touched"] == "untouched"))
M["gaps"] = OrderedDict(untouched_middle_definitions=untouched_mid_defs, middle_definitions_never_varied=never_varied_mid_defs,
                        edges_claimed_only=claimed,
                        touched_by_stretch={"%s %s" % k: dict(v) for k, v in sorted(by_stretch.items())})
M.pop("second_round_needed", None)
FLAGS = {"C1": ["S44"], "C2": ["S44 (on that reading)", "S41 Q15 (on that reading)", "S41 Q6 (on that reading)"],
         "C3": [], "C4": [], "C5": ["S41 Q15 (on that reading)", "S44 (on that reading)"], "C6": ["S45", "S44 (on that reading)"],
         "C7": ["S41 Q2 (in part)"], "C8": ["S41 Q2 (on that reading)"], "C9": [], "C10": [], "C11": ["S45", "S44 (on that reading)"],
         "C12": ["S41 Q2"], "C13": [], "C14": [], "C15": ["S44 (at that grain)", "S41 Q15 (at that grain)"],
         "C16": ["S41 Q2", "S44 (on a selection history)", "S41 Q15 (on a selection history)"], "C17": [], "C18": [], "C19": [],
         "C20": [], "C21": ["S41 Q2 (on the reply's reading)"]}
VAR = {"C14": "R2V1.6", "C15": "R2V2.8", "C16": "R2V3.5", "C17": "R2V3.2", "C18": "R2V3.3 (b)", "C19": "R2V3.4", "C20": "R2V3.7",
       "C21": "R2V2.6 (the reply's reach)"}
cands = [dict(c, decisions_after_round2=FLAGS[c["id"]], flagged_after_round2=bool(FLAGS[c["id"]])) for c in r1["candidates"]]
cands += [{"id": k, "variant": v, "round": 2, "decisions": FLAGS[k], "flagged": bool(FLAGS[k])} for k, v in VAR.items()]
M["candidates"] = cands
M["third_round_needed"] = ("not for gaps bearing on the explanation definition that Part A's rule can reach (the map's §7), "
                           "pending the GLM cross-examination; D5.7 belongs to Part B")
json.dump(M, open(OUTJ, "w", encoding="utf-8"), indent=1, ensure_ascii=False)

# ------------------------------------------------------------------ printed tables for the .md
P = print
P("COUNTS", json.dumps(M["counts"], ensure_ascii=False))
P("\nCHANGES")
for c in changes:
    P("| %s | %s | %s | %s | %s |" % (c["edge"], c["round1_standing"], c["after_round2"], c["what_changed_it"], c["why"][:300].replace("|", "/")))
P("\nSTRETCH")
for k, v in sorted(by_stretch.items()):
    P(k, dict(v))
P("\nUNTOUCHED MID DEFS", untouched_mid_defs)
P("NEVER VARIED MID DEFS", never_varied_mid_defs)
P("\nCLAIMED ONLY", len(claimed), claimed)
P("\nSUITE")
for k, v in suite.items():
    P(k, json.dumps(v, ensure_ascii=False))
P("\nR2 EDGES by section and standing", Counter((e["id"].split(".")[0], e["standing"]) for e in new_edges))
