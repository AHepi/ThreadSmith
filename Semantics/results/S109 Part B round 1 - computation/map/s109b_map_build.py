# S109 Part B round 1 (rules 5 and 6): builds the four "section Bn - variants computed" files (.md, .json) and the map of how
# explanation changes in meaning and scope (.md, .json) from the hand record (s109b_data.py), the scope runs (section Bn
# runs/scope tables.json) and the whole-suite results (whole suite/summary.json).
#   python3 -B s109b_map_build.py
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
COMP = os.path.dirname(HERE)
RES = os.path.dirname(COMP)
sys.path.insert(0, HERE)
from s109b_data import V, PARTS  # noqa: E402

PB = "S109 Part B round 1 - "
suite = json.load(open(os.path.join(COMP, "whole suite", "summary.json"), encoding="utf-8"))
scope = {}
for s in ("B1", "B2", "B3"):
    scope[s] = json.load(open(os.path.join(COMP, "section %s runs" % s, "scope tables.json"), encoding="utf-8"))
b4 = json.load(open(os.path.join(COMP, "section B4 runs", "scope.json"), encoding="utf-8"))
TITLES = {"B1": "organizations, kinds, questions and contracts", "B2": "transports, fidelity, the account, routes and the exact constructions",
          "B3": "provenance, histories, representation, construction, repair and the physical module",
          "B4": "rivals, problems, criticism, the class, what would rule it out, and the Arguments"}


def moved_claims(v):
    out = {}
    for key in v["suite"]:
        for c, m in suite[key]["moved"].items():
            out.setdefault(c, []).append("%s%s" % (m["status"] or "parts: " + " / ".join(m["parts"][:2]), "" if len(v["suite"]) == 1 else " (%s)" % key.split(" ", 1)[1]))
    return out


def scope_rows(v):
    rows = []
    for lab in v["readings"]:
        if v["section"] == "B4":
            r = b4["variants"][lab]
            mv = [m for m in r["moved"] if m["off"].replace(" question T", "") != m["on"].replace(" question T", "")]
            rows.append(dict(reading=lab, moved=len(mv), acc_in=[], acc_out=[], expl_only=[m["label"] for m in mv], owner="all stay (B4 reads neither (E) nor Dec)",
                             student="stays" if not r["student_moves"] else "moves", worlds="not run (B4 code reads neither Acc nor Dec)",
                             scripts=[s for s, x in r["scripts"].items() if not x["same"]], chains=None, bridge=None))
            continue
        r = scope[v["section"]]["readings"][lab]
        w = r["worlds"]
        own = "; ".join("%s: %s" % kv for kv in r["owner"].items() if not kv[1].startswith("stays")) or "all stay"
        rows.append(dict(reading=lab, moved=len(r["ain"]) + len(r["aout"]) + len(r["eonly"]), acc_in=r["ain"], acc_out=r["aout"], expl_only=r["eonly"],
                         owner=own, student=r["student"],
                         worlds=("Acc in %d, out %d; Expl (Sel history) in %d, out %d" % (w["acc_in"], w["acc_out"], w["expl_in"], w["expl_out"])) if w else "not run",
                         scripts=list(r["scripts"].keys()), chains=r["chains"], bridge=r["bridge"]))
    return rows


def md_section(sec):
    vs = [v for v in V.values() if v["section"] == sec]
    L = ["# S109 Part B round 1 - section %s (%s) - variants computed" % (sec, TITLES[sec]), "",
         "*Rule 5 of `S109 Part B round 1 - how the replies will be read, written before sending.md`. The one Opus 5.5 agent of decision S56 (effort high). "
         "Works only in `S109 Part B round 1 - computation/section %s model/` (a copy of `S107 Round 4 - maths after the reading/model after round 4/`, 26 files md5-identical at the copy; "
         "the original and Part A's copies never written). Read with the reply (`returns/s109_glm_section%s.response.txt`) and the tabulation (`S109 Part B round 1 - tabulation of the replies, before any ruling.md`). "
         "Built by `computation/map/s109b_map_build.py` from the hand record `computation/map/s109b_data.py`, the scope runs and the whole-suite results. "
         "Nothing here changes the theory (rule 13). \"Candidate\" or \"explanation\" for what the theory judges; \"model\" only for the program or a small structure it builds (S43).*" % (sec, sec[1]), "",
         "Status: complete, 29 September 2026.", "",
         "## 0. Setup", "",
         "| item | state |", "|---|---|",
         "| copy | `model after round 4/`, 26 files identical at the copy (md5 list compared) |",
         "| switches | `S109B_VARIANT` in the environment (a case script sets `core.S109B`); readings: %s; every change is guarded by the switch, the patch is `computation/patches/patch_%s.py` |" % (
             {"B1": "`S109B_THETA` (all, strict)", "B2": "`S109B_NC0` (bg, bg-input), `S105_SLOT_QUANTIFIER` (the program's)", "B3": "none beyond the variant", "B4": "`S109B_HELD` (all, no-records)"}[sec], sec),
         "| default unchanged | the whole suite in the B3 copy with every switch off equals the record after round 4 (142 of 142 claims, `whole suite/B3/none.json`); the scope script's 'none' values equal Part A's section 2 copy's on all 17,329 cases (`comparisons with Part A/`) |",
         "| scope | `computation/scripts/s109b_scope.py` → `section %s runs/scope.json`, `scope.txt`, `scope tables.md` / `.json`: the 27 worked cases and 22 encodings of the owner's sign and vane (edit, boundary, mixed; E_enc on each question), the student's copy (FC30.new1 (d)), %s FC-E1-E5 (`s104_external.py`) and CT1-CT8 (`s104_creative_transport.py`) against their output under 'none'%s |" % (
             sec, "the generated worlds (SMALL, 160 per size, seed 109001: 17,280 candidates, 999 meeting (E)), " if sec != "B4" else "", "; every chain of 1 to 3 holdings (584) and the bridge's chains (FC84.new1 (a1), (a2))" if sec == "B3" else ""),
         "| the replies' small cases | `computation/scripts/s109b_small_cases.py` → `section %s runs/small cases.txt` (B1, B2) |" % sec,
         "| whole suite | `tools/sonnet_harness/run_claims.py` per variant and reading, scale 4, time cap 45, PYTHONHASHSEED=0, from the copy's parent, under `timeout`, output in the scratchpad, results copied to `whole suite/%s/` and summarized in `whole suite/summary.md` / `.json` (the moved claims' printouts kept there) |" % sec,
         "", "## 1. What is implemented, and the inventions it forced (S36)", "",
         "| id | free item(s) | kind | carry-over | implemented | switch | inventions (other choices) |", "|---|---|---|---|---|---|---|"]
    for v in vs:
        L.append("| %s | %s | %s | %s | %s | %s | %s |" % (v["id"], ", ".join(v["free"]), v["kind"], v["carry"], v["impl"], v["switch"], "; ".join(v["inventions"]) or "none"))
    L += ["", "## 2. Meaning: the changed formal statement, old beside new, of each part of the explanation definition that moves", "",
          "| id | part | old | new |", "|---|---|---|---|"]
    for v in vs:
        for part, old, new in v["meaning"]:
            L.append("| %s | %s | %s | %s |" % (v["id"], part, old, new))
    L += ["", "## 3. Scope: computed, the variant off against on", ""]
    for v in vs:
        L.append("### %s" % v["id"])
        L.append("")
        L.append(v["scope_note"])
        L.append("")
        rows = scope_rows(v)
        if rows:
            L.append("| reading | cases moved (Acc in / out / Expl only) | the owner's sign and vane (off → on; Expl on Dec/Con/Sel histories) | the student's copy | generated | FC-E, CT |")
            L.append("|---|---|---|---|---|---|")
            for r in rows:
                L.append("| %s | %d (%d / %d / %d) | %s | %s | %s | %s |" % (r["reading"], r["moved"], len(r["acc_in"]), len(r["acc_out"]), len(r["expl_only"]), r["owner"], r["student"], r["worlds"], ", ".join(r["scripts"]) or "same"))
            for r in rows:
                if r["acc_in"] or r["acc_out"]:
                    L.append("")
                    L.append("%s: enter: %s. Leave: %s." % (r["reading"], "; ".join(r["acc_in"]) or "none", "; ".join(r["acc_out"]) or "none"))
                if r["chains"]:
                    L.append("")
                    L.append("%s, chains: %d of %d differ; at the output Dec → not Dec %d, not Dec → Dec %d; number of fixed points changed %d. The bridge: %s." % (
                        r["reading"], r["chains"]["differ"], r["chains"]["total"], r["chains"]["output_dec_to_not"], r["chains"]["output_not_to_dec"], r["chains"]["fixed_point_count_changed"],
                        "stays (Con and Build at the output under (a1) and (a2))" if r["bridge"] and r["bridge"]["on"] == r["bridge"]["off"] else r["bridge"]))
        mc = moved_claims(v)
        L.append("")
        L.append("Claims that move (whole suite): %s." % ("; ".join("%s %s" % (c, ", ".join(x)) for c, x in sorted(mc.items())) if v["suite"] and mc else ("none" if v["suite"] else "the whole suite was not run: " + ("no code changes" if "no code" in v["impl"] else "no claim reads the changed code" if v["id"] == "PB1.5" else "flagged out"))))
        L.append("")
    L += ["## 4. Edges", "", "| id | kind | item | standing | Part A id | why |", "|---|---|---|---|---|---|"]
    for v in vs:
        for e in v["edges"]:
            L.append("| %s | %s | %s | %s | %s | %s |" % (v["id"], e[0], e[1], e[2], e[3] or "–", e[4]))
    L += ["", "Nothing here is a change to the theory (rule 13). Written by one Opus 5.5 agent under rule 5 and decision S56, 29 September 2026."]
    return "\n".join(L) + "\n"


def rec_json(v):
    return dict(id=v["id"], section=v["section"], free=v["free"], kind=v["kind"], carry=v["carry"], implemented=v["impl"], switch=v["switch"],
                inventions=v["inventions"], meaning=[dict(part=p, old=o, new=n) for p, o, n in v["meaning"]], scope_note=v["scope_note"],
                scope=scope_rows(v), claims_moved=moved_claims(v), suite_runs=v["suite"],
                edges=[dict(kind=e[0], item=e[1], standing=e[2], part_A=e[3], why=e[4]) for e in v["edges"]])


for sec in ("B1", "B2", "B3", "B4"):
    open(os.path.join(RES, PB + "section %s - variants computed.md" % sec), "w", encoding="utf-8").write(md_section(sec))
    json.dump(dict(section=sec, status="complete", variants=[rec_json(v) for v in V.values() if v["section"] == sec]),
              open(os.path.join(RES, PB + "section %s - variants computed.json" % sec), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("four section files written")


# ---------------------------------------------------------------- the map (rule 6)
LEVEL = {  # which part of the definition each variant's meaning moves first; Expl, (Suff), (Nec) contain (E) and Dec
    "(E)": ["PB1.1", "PB1.2", "PB1.3", "PB1.6", "PB1.7", "PB2.2", "PB2.3", "PB2.4", "PB2.5", "PB2.6", "PB2.7", "PB2.9"],
    "Dec": ["PB2.1", "PB2.2", "PB3.1", "PB3.2", "PB3.3", "PB3.4", "PB3.5", "PB3.6"],
    "X_j (the defeat sets of (Suff), (Nec) only)": ["PB4.2", "PB4.3", "PB4.4"],
}
SCOPE_MOVES = {  # computed: which candidates meet (E), or count as explanations, or fall in a defeat set, changes
    "(E)": {"PB1.1": "the hand case with Excl(Σ) = ∅ enters", "PB1.2": "Θ strict: 36 cases and 813 generated leave (the sign and vane as edits or mixed)",
            "PB1.3": "C_id leaves", "PB1.6": "61 generated enter", "PB1.7": "8 cases (the sign and vane as boundaries, C_id) and 186 generated leave",
            "PB2.2": "1 worked case and 11 generated enter", "PB2.3": "214 generated leave", "PB2.5": "bg: 1 case, 149 generated leave; bg-input: 12 generated leave",
            "PB2.6": "the hand case enters (as PB1.1)", "PB2.7": "20 to 28 cases, 855 to 946 generated leave (as C6)"},
    "Dec": {"PB2.1": "FC104.new1 (b)'s selection becomes declared", "PB2.2": "the relabeling candidate on a Sel history", "PB3.1": "the student's copy stops being declared",
            "PB3.2": "10 chain outputs become declared", "PB3.3": "every Sel-history case (44 cases, 999 generated) becomes declared", "PB3.4": "the student's copy and 82 chain outputs stop being declared",
            "PB3.6": "the student's copy stops being declared (on that reading)"},
    "X_j": {"PB4.2": "FC56 (a″)'s coarse-grain assessor's argument becomes usable", "PB4.4": "X_j empty everywhere: nothing ruled out, the defeat sets empty"},
}
MEANING_ONLY = ["PB2.4", "PB2.9", "PB3.5", "PB4.3", "PB4.1"]
NEITHER = ["PB1.4", "PB1.5", "PB1.8", "PB1.9", "PB2.8", "PB3.7", "PB4.5", "PB4.6", "PB4.7", "PB4.8"]
FLAGGED_OUT = ["PB3.8"]

allv = list(V.values())
edges = [dict(variant=v["id"], kind=e[0], item=e[1], standing=e[2], part_A=e[3], why=e[4]) for v in allv for e in v["edges"]]
tot = {}
for e in edges:
    tot[e["standing"]] = tot.get(e["standing"], 0) + 1
kinds = {}
for e in edges:
    kinds.setdefault(e["kind"], {}).setdefault(e["standing"], 0)
    kinds[e["kind"]][e["standing"]] += 1

M = ["# S109 Part B round 1 - how explanation changes in meaning and scope", "",
     "*Rule 6 of `S109 Part B round 1 - how the replies will be read, written before sending.md`. The one Opus 5.5 agent of decision S56 (effort high), 29 September 2026. "
     "Built by `computation/map/s109b_map_build.py` from the four \"section Bn - variants computed\" files (and their hand record `computation/map/s109b_data.py`, the scope runs and the whole-suite results). "
     "Part A's map (`S108 Part A round 2 - the dependency map, after the cross-examination.md` / `.json`) is never written; edges that join it cite its ids. Nothing here is applied; nothing is ruled. "
     "\"Candidate\" or \"explanation\" for what the theory judges; \"model\" only for the program (S43).*", "",
     "## 0. What is mapped", "",
     "Being an explanation = Account(ℰ) ∧ ¬Dec(t), Account = (E) = (F1) ∧ (F2) ∧ (A) ∧ Dependence ∧ NonVacuous; (Suff) and (Nec) are the claims about it, read through their defeat sets X_j (D16.XV). "
     "**Meaning** = the changed formal statement, old beside new, of each part that moves. **Scope** = which things count, computed off against on: the text's worked cases (27), the owner's four cases (the two-part sign and the weathervane under the three readings of the owner's change, the student's copy FC30.new1 (d), the bridge FC84.new1 (a1), (a2)), the made-up candidates (17,280 generated at scale 4, FC-E1-E5, CT1-CT8; chains of up to three holdings for Dec), and the whole claim suite (142 claims) per variant and reading. "
     "34 variants: 31 implemented as switches (PB2.8, PB2.9, PB4.3 with no code change, PB1.5 with no reader), PB3.8 flagged out (no formal statement), PB4.4 flagged out as written and computed as PB4.4′ restated on D9.8. The three class-a carry-overs are computed (V1.7 as PB1.1, R2V2.7 as PB2.1, V2.8's L315.s7 part as PB4.1); of class b, R2V1.4, R2V1.7, R2V1.8, R2V1.9, R2V2.4 (as PB1.5, PB1.4, PB1.3, PB1.2, PB3.1); R2V1.2 was not taken up.", "",
     "## 1. Per variant", "",
     "| id | free item(s) | kind | meaning: part (old → new) | scope (computed) | claims that move | edges (computed / contradicted / claimed only) |", "|---|---|---|---|---|---|---|"]
for v in allv:
    sc = "; ".join(x[v["id"]] for x in SCOPE_MOVES.values() if v["id"] in x) or ("meaning moves, scope unchanged on every case computed" if v["id"] in MEANING_ONLY else ("flagged out, not computed" if v["id"] in FLAGGED_OUT else "no candidate moves (nothing in the definition reads it)"))
    mc = moved_claims(v)
    st = [sum(1 for e in v["edges"] if e[2] == s) for s in ("computed", "contradicted", "claimed only")]
    mean = "; ".join("%s: %s → %s" % m for m in v["meaning"])
    M.append("| %s | %s | %s | %s | %s | %s | %d / %d / %d |" % (v["id"], ", ".join(v["free"]), v["kind"], mean.replace("|", "∣"), sc, ", ".join(sorted(mc)) or ("none" if v["suite"] else "not run"), *st))
M += ["", "## 2. Per part of the definition", "",
      "| part | free items its meaning was found to turn on (variants) | free items its scope was found to turn on (computed moves) |", "|---|---|---|"]
for lvl, ids in LEVEL.items():
    key = "X_j" if lvl.startswith("X_j") else lvl
    mi = "; ".join("%s (%s)" % (", ".join(V[i]["free"]), i) for i in ids)
    si = "; ".join("%s (%s: %s)" % (", ".join(V[i]["free"]), i, SCOPE_MOVES[key][i]) for i in ids if i in SCOPE_MOVES[key])
    M.append("| %s | %s | %s |" % (lvl, mi, si))
M.append("| Expl | everything under (E) and Dec (Expl := Account ∧ ¬Dec(t)) | everything under (E) and Dec |")
M.append("| (Suff), (Nec) | everything under (E) and Dec (their antecedent), and X_j's items | everything under (E) and Dec (FC30.new1's defeat-set parts move with PB1.2, PB3.1, PB3.3, PB3.4, PB3.6), and X_j's (PB4.2, PB4.4′) |")
M += ["", "Varied, meaning of a part moved, scope unchanged on every case computed: %s." % "; ".join("%s (%s)" % (i, ", ".join(V[i]["free"])) for i in MEANING_ONLY),
      "", "Varied, moving neither the meaning nor the scope of any of the five parts (what moves is kinds, Found, routes, New, criticism, problems or the class's list; claims move as §1 says): %s." % "; ".join("%s (%s)" % (i, ", ".join(V[i]["free"])) for i in NEITHER),
      "", "Not varied: see §5.", "",
      "## 3. Edges", "", "| variant | kind | item | standing | Part A id | why |", "|---|---|---|---|---|---|"]
for e in edges:
    M.append("| %s | %s | %s | %s | %s | %s |" % (e["variant"], e["kind"], e["item"], e["standing"], e["part_A"] or "–", e["why"]))
M += ["", "Edges joining Part A's map: e1.48, e1.49, e1.51 (V1.7, now computed as PB1.1: e1.51 and e1.49 computed, e1.48 still claimed only); e2.20 (computed), e2.21 (still claimed only: under S109-B4-I1 the defeat sets do not move); r2e2.14 (R2V2.7, computed as PB2.1); r2e1.30 (R2V1.4: no reader, claimed only); r2e1.34 (R2V1.7, computed as PB1.4); e1.00 (V1.1's block on D4.4: PB1.8 lifts it and FC17, FC18 hold); e3.34b (the neighbour of PB4.6).", "",
      "## 4. Totals", "",
      "**%d edges**: %s." % (len(edges), ", ".join("%s %d" % kv for kv in sorted(tot.items()))), "",
      "| kind | computed | contradicted | claimed only |", "|---|---|---|---|"]
for k, d in sorted(kinds.items()):
    M.append("| %s | %d | %d | %d |" % (k, d.get("computed", 0), d.get("contradicted", 0), d.get("claimed only", 0)))
M += ["", "Variants: %d implemented and computed (%d moving scope, %d meaning only, %d neither), %d flagged out (PB3.8; PB4.4 computed as PB4.4′)." % (
    len(allv) - 1, sum(1 for v in allv if any(v["id"] in x for x in SCOPE_MOVES.values())), len(MEANING_ONLY), len(NEITHER), 1)]
tail = open(os.path.join(HERE, "s109b_map_tail.md"), encoding="utf-8").read()
open(os.path.join(RES, PB + "how explanation changes in meaning and scope.md"), "w", encoding="utf-8").write("\n".join(M) + "\n\n" + tail)
json.dump(dict(about="S109 Part B round 1, rule 6: how explanation changes in meaning and scope, per variant and per part; built by computation/map/s109b_map_build.py",
               variants=[rec_json(v) for v in allv], levels=LEVEL, scope_moves=SCOPE_MOVES, meaning_only=MEANING_ONLY, neither=NEITHER, flagged_out=FLAGGED_OUT,
               edges=edges, totals=dict(edges=len(edges), by_standing=tot, by_kind=kinds)),
          open(os.path.join(RES, PB + "how explanation changes in meaning and scope.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("map written (§5, §6 from s109b_map_tail.md)")
