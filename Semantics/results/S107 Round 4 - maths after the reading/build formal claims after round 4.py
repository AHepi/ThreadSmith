#!/usr/bin/env python3
"""S107 round 4, integration (rule 7): build `formal claims, after round 4.json` and `.md` from
`results/S106 The written-in test taken out/formal claims, after S106.json` (read only) and the three area checkers'
records (`area N - expected claims.json`, read only). Every claim keeps its S106 fields; round 4 adds `r4`
({areas, findings, restated, note}; restated: the statement changed, `formal_after_s106` keeps S106's) and
`after_round4`, the result expected on `model after round 4/` (the merged program): the area record that changed the claim
(no claim is changed by two areas; checked), else the S106 record (equal in all three areas; checked). The claims the
merge touches were run singly on the merged program by the integration (`integration notes.md` §9) and agree.
Five new test claims. Writes only the two files named above, beside this program; refuses to write over one.
Run: python3 -B "build formal claims after round 4.py"   (standard library only)
"""
import collections
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
S106 = os.path.join(HERE, "..", "S106 The written-in test taken out", "formal claims, after S106.json")
AREAS = [("A1", os.path.join(HERE, "area 1 - expected claims.json"), "area1_r4", "after_s106"),
         ("A2", os.path.join(HERE, "area 2 - expected claims.json"), "after_r4a2", "baseline_after_S106"),
         ("A3", os.path.join(HERE, "area 3 - expected claims.json"), "area3_r4", "after_s106")]
OUT_JSON = os.path.join(HERE, "formal claims, after round 4.json")
OUT_MD = os.path.join(HERE, "formal claims, after round 4.md")
REPRO = ('cd "/home/user/ThreadSmith/Semantics/results/S107 Round 4 - maths after the reading/model after round 4" && '
         'PYTHONHASHSEED=0 python3 -B -m model.run --claim %s --scale 4 --time-cap 45')
H, CEX, NT = "HOLDS ON ALL MODELS TRIED", "COUNTEREXAMPLE FOUND", "NOT TESTED"
SHORT = {H: "H", CEX: "CEX", NT: "NT"}

# round 4 per existing claim: (areas, findings, restated, new statement or None, note, inventions to add)
R4 = {
    "FC31": ("A1", "B-N2, W-N2, S-N2, C-N2 (N2)", True,
             "(E) has five conjuncts (D6.7); Part V has four headed conditions (D6.8): Component fidelity = (F1) ∧ (F2), Question fidelity = (A), "
             "Dependence, Non-vacuity. 'The four conditions' at L231 and L536 are the four headings. L520 writes (E)'s five conjuncts, (A) among "
             "them; the extent of 'fidelity' is open at L630 alone (FC104; L220 narrow, R3A1-T5, D5.7).",
             "re-based (area 1 F1): L61's phrase was replaced in round 3 (R3A1-T1); L520 writes the five conjuncts; NT unchanged", []),
    "FC84.new1": ("A1", "B11, W-N6, S-N6, C-N6 (N6)", True, None,
                  "test part (a3) added (area 1): the readings of 'no question about the brief occurred' (I191; I192 (d), (e)); Con and Build the same under all three", ["I192"]),
    "FC30.new1": ("A3", "W5", True, None,
                  "test part (h) added (area 3 F7): 'not using (E)' read at the symbol (I196); (a), (b), (g) through not_using_E, default 'symbol'", ["I196"]),
    "FC98": ("A3", "S2", True,
             "(a) With 'represented' (L195's Rep, L197) read through (R) the dependence graph has a cycle (E03); Build reads Held (L405 since "
             "R3A3-T4); (a') with (R) inside Sel and Con staged (K), replaced by Held (T), or Held in Con and staged in Sel (T′), Build reading Held "
             "under each, none; (b) the sinks outside L522's list (a look; each read through Θ or a declared input, D0.2); (c) Rep as a fixed point "
             "on a two-occurrence history: as worded two / none, K, T and T′ one each; (d) K gives a first construction no representation, T and T′ "
             "one; (e) an earlier holder by a declared transport blocks a later selection under T, not under K or T′ (L195 with L211): the cut T′ (I162).",
             "re-based (area 3 F2: DEP['Build'] staged (R) → Held); (a), (a′) statements; results unchanged; (b)'s look lists D16.XV's five terms (F4)", []),
    "FC32.new1": ("A3", "B14, W6, S1; S4, S6", False, None,
                  "note (area 3 F1, F3, F4): (a) reads the formal core through model/corefile.py, after round 4 `formal core, after round 4.md`; "
                  "(c) classes D0_2_R4A3 beside D0_2_R3A3; 'subhistory' no longer a sink", []),
    "FC14": ("A3", "B14, W6, S1", False, None,
             "note (area 3 F1): reads the formal core through model/corefile.py (one list; name and md5 printed; no older core read)", []),
    "FC23.new3": ("A2", "B8, S3", False, None, "note (area 2 F1): (a) now holds of D6.3 as written (t translates (a,b) inside the ∀)", []),
    "FC23.new2": ("A3", "W5", False, None, "note: (f) through expl_ruled_out's symbol reading (area 3 F7); unchanged", []),
    "FC27": ("A2", "B4, C-K1", False, None,
             "note: L271 reads 'the production contract \\(C_1\\) (E1, FC27)' (R4A2-T1), L536 'under \\(C_1\\)' (R4INT-T1), settling I193; FC27.new1", ["I193"]),
    "FC83": ("integration", "pair 5", False, None,
             "note: build_at unchanged: round 2's reading under U and K (named alternatives), Held under T and T′, as DEP reads under every cut", []),
}

NEW = [
    dict(id="FC27.new1", after="FC27", areas="A2", findings="B4, C-K1",
         title="L271's 'the production contract': C1 (E1), not every production contract",
         source=[{"line": 271, "quote": "fails (F2) under the production contract:"}, {"line": 151, "quote": "a \\(C\\) containing interventions on upstream ports"}],
         formal="(a) C1 and C_H := {1} ∪ settings of H are production contracts (L151; D3.3 Prod). (b) Under τ (each edit to itself) E_rev fails (F2) "
                "on C1 and on C_H. (c) Under τ′ on C1, E_rev meets F2eq at every pair and fails Hom: (F2) fails. (d) Under τ′ on C_H, E_rev meets (F1), "
                "(F2), (A), Dependence and non-vacuity under every reading of D6.3's quantifier (r_L a slot: an explanation, S44, S45): L271 read of every "
                "production contract states an (F2) failure the computation does not give; read of C1 (I193) it is (b), (c).",
         inventions=["I65", "I193"], sections=["§17", "§5"]),
    dict(id="FC23.new4", after="FC23.new3", areas="A2", findings="B8, S3, B9",
         title="D6.3 with 't translates (a,b)' inside the ∀: Slot is Pin at every pair of Det_C",
         source=[],
         formal="(a) τ undefined at a determined pair: D6.3's displayed clause (after S106) has no value there; with the clause Slot is False, as Pin is. "
                "(b) π partial exactly off Sol_D at a determined pair: the displayed clause holds and Pin fails; D6.3 with the clause gives Slot ⟺ "
                "Det_C ≠ ∅ ∧ Pin at every pair. (c) On generated models, τ and π partial: Slot_C(ℰ,k) ⟺ Det_C ≠ ∅ ∧ ∀(a,b) ∈ Det_C Pin(ℰ,k;a,b). "
                "(d) Look: every pin of c_L on the pole's C2 is at a setting of L, whose own edit alters c_L; I184 counts it (I194); I136's exempt "
                "reading would exempt each; (E) reads none.",
         inventions=["I16", "I184", "I194"], sections=["§6"]),
    dict(id="FC23.new5", after="FC23.new4", areas="A2", findings="C-K3",
         title="The owner's sign on a target with one part: the two-part candidate fails (F1), not for a slot",
         source=[{"line": 245, "quote": "(F1) prevents an assembled match from hiding a decomposition in error"}],
         formal="(a) On D_beh (one component c, red on Mondays, blue on Tuesdays) no λ in D5.1's range and no τ(tue) lets ℰ_two meet (F1): a "
                "decomposition the target lacks (L245). (b) There ℰ_one (one part k, λ(k) = {c}) meets (E) and Slot_C(ℰ_one, k). (c) On I189's target, "
                "whose parts are the target's, ℰ_two meets (E) (FC23.new2 (a)): which candidate meets (F1) turns on the target's components at the "
                "declared grain (L31).",
         inventions=["I189"], sections=["§5", "§6"]),
    dict(id="FC42.new1", after="FC42", areas="A2", findings="B-N1, W-N1, S-N1, C-N1 (N1)",
         title="D7.4's Boundary with the designation carried (δ_v)",
         source=[],
         formal="(a) With δ_v carried by the operation, each v declaring (E_v, t_v, Γ_v, δ_v), Boundary is the set of pairs whose computed Acc differs. "
                "(b) Without δ_v, the designations E_v allows give Acc(E_v, p) both values for some v, and a pair is in Boundary under one choice and "
                "not another. (c) A renaming leaves δ_E no port of E_v; δ_v = the port the renaming carries δ_E to gives Acc(E_v) = Acc(E). (d) Look, "
                "the other choice ∃δ_v (as D14.7, D16.4): an edit moving the answer onto another port keeps Acc under ∃δ_v and loses it with δ "
                "carried (L253: the query held fixed).",
         inventions=["I20", "I195"], sections=["§7"]),
    dict(id="FC72.new2", after="FC72.new1", areas="A3", findings="K1 (addendum)",
         title="K1: the myth about winter after S106",
         source=[{"line": 317, "quote": "one that finds, by examining it, that at a pair of \\(C\\) it gives what a claim the assessor tentatively accepts excludes"}],
         formal="(a) On the Greeks' contract C_G = {(June, N), (Dec, N)} the tilt meets (E) with no slot; the myth with its answer written in (one part) "
                "is a slot under 'every' and meets (E) after S106 (round 3's (E): no, under every reading); the myth as told (two parts) has no slot "
                "under 'every' and meets (E). (b) Offered one in place of the other: conflict pairs {(June, S), (Dec, S)}, outside C_G: rivals; for an "
                "assessor who rules out neither, a problem of kind ii, each easy to vary against the other (D10.2, D10.4), for either encoding. (c) j0 "
                "takes up the finding Slot(myth): no argument usable by j0 rules out Acc(myth); j1 also takes 'Slot → ¬Acc' as given ((E) does not "
                "give it): MP rules the myth out for j1, not blocked, j1's choice (L397, S28); j2 holds Slot ∧ ¬Acc as one premise: blocked (D9.7). "
                "(d) With the south in the contract the myth fails (E) and the tilt meets it: kind i; a record of June in the south with (A)'s premise "
                "rules out the myth, not the tilt, for whoever takes them up (L317, K2, K3).",
         inventions=["I197"], sections=["§9", "§10"]),
]
APPEND = {  # statement parts appended to an existing claim's formal statement
    "FC84.new1": " (a3) Which occurrences are a question about the brief is read through Θ (I90): as criticisms (D9.10) aimed at the brief (I191); as "
                 "question-occurrences, with or without an alleged defect (I192 (d)); or as a question found (L15, L155, L161), operative at its "
                 "occurrence (I192 (e)). The readings part ways and agree on (a1)'s chain; under D13.8 as S41 has it, Con and Build at the output are "
                 "the same in every case, one fixed point each (T′): no computed value reads the labels; under L55 as text 104 words it, only a "
                 "recorded change of contract moves Con, as in (b).",
    "FC30.new1": " (h) An argument usable by j whose only use of (E) is Acc(ℰ′) for another candidate rules out Expl(ℰ): read as D16.XV writes it "
                 "((E), Acc ∉ Uses(α); I196) it does not put ℰ in (Suff)'s defeat set; read at the instance (no use of Acc(ℰ) itself) it does; the "
                 "argument from a record (r, r → ¬Expl(ℰ)) is in it under both.",
}


def load_area(path, key, base_key):
    d = json.load(open(path, encoding="utf-8"))
    return {c["id"]: (c.get(key), c.get(base_key)) for c in d["claims"]}


def same(a, b):
    return a is not None and b is not None and a["status"] == b["status"] and \
        [(p["label"], p["kind"], p["status"]) for p in a["parts"]] == [(p["label"], p["kind"], p["status"]) for p in b["parts"]]


def main():
    for p in (OUT_JSON, OUT_MD):
        if os.path.exists(p):
            sys.exit("REFUSED: %s exists; never written over" % os.path.basename(p))
    d = json.load(open(S106, encoding="utf-8"))
    base = {c["id"]: c["after_s106"] for c in d["claims"]}
    areas = [(n, load_area(p, k, bk)) for n, p, k, bk in AREAS]
    ids = sorted(set().union(*[set(a) for _, a in areas]))
    expected, changed_by = {}, collections.defaultdict(list)
    for cid in ids:
        for n, a in areas:
            new, old = a.get(cid, (None, None))
            if new is None:
                continue
            if cid in base and not same(old if old is not None else base[cid], base[cid]):
                sys.exit("REFUSED: %s: area %s's baseline differs from the S106 record" % (cid, n))
            if cid not in base or not same(new, base[cid]):
                changed_by[cid].append(n)
                expected[cid] = new
        if cid not in expected:
            if cid not in base:
                sys.exit("REFUSED: %s in no record" % cid)
            expected[cid] = base[cid]
        for n, a in areas:
            if cid in base and cid not in a:
                sys.exit("REFUSED: %s missing from area %s" % (cid, n))
    two = {k: v for k, v in changed_by.items() if len(v) > 1}
    if two:
        sys.exit("REFUSED: claims changed by two areas: %s" % two)
    for c in d["claims"]:
        e = expected[c["id"]]
        c["after_round4"] = {"status": e["status"], "parts": [{"label": p["label"], "kind": p["kind"], "status": p["status"]} for p in e["parts"]],
                             "reproduce": REPRO % c["id"], "from": ("area %s" % changed_by[c["id"]][0][1]) if c["id"] in changed_by else "S106 record"}
        if c["id"] in R4:
            ar, fi, restated, formal, note, inv = R4[c["id"]]
            c["r4"] = {"areas": ar, "findings": fi, "restated": restated, "note": note}
            if restated:
                c["formal_after_s106"] = c["formal"]
                c["formal"] = formal if formal else c["formal"] + APPEND[c["id"]]
            for i in inv:
                if i not in c["inventions"]:
                    c["inventions"].append(i)
        else:
            c["r4"] = None
    for n in NEW:
        e = expected[n["id"]]
        c = dict(id=n["id"], title=n["title"], source=n["source"], formal=n["formal"], type=["test (round 4)"], s100_units=[], round1=[],
                 inventions=n["inventions"], formal_core_sections=n["sections"], look="", round2_result=None, r2=None, r3=None,
                 after_round3=None, s106=None, after_s106=None,
                 r4={"areas": n["areas"], "findings": n["findings"], "restated": False, "note": "new (round 4)"},
                 after_round4={"status": e["status"], "parts": [{"label": p["label"], "kind": p["kind"], "status": p["status"]} for p in e["parts"]],
                               "reproduce": REPRO % n["id"], "from": "area %s" % n["areas"][1]})
        at = [i for i, x in enumerate(d["claims"]) if x["id"] == n["after"]][0]
        d["claims"].insert(at + 1, c)
    missing = sorted(set(expected) - set(c["id"] for c in d["claims"]))
    if missing:
        sys.exit("REFUSED: expected results with no claim: %s" % missing)
    unchanged_moved = [cid for cid in changed_by if cid not in R4 and cid not in [n["id"] for n in NEW]]
    if unchanged_moved:
        sys.exit("REFUSED: claims whose result moved with no round-4 entry: %s" % unchanged_moved)
    cnt = collections.Counter(c["after_round4"]["status"] for c in d["claims"])
    d["about"]["r4"] = ("S107 round 4 (log S107), integration, 28 September 2026: r4 = {areas, findings, restated, note} (restated: the statement "
                        "changed, formal_after_s106 keeps S106's); after_round4 = the result expected on results/S107 Round 4 - maths after the "
                        "reading/model after round 4/ (the merged program; scale 4, time cap 45 s, PYTHONHASHSEED=0, --no-write), from the area "
                        "record that changed the claim, else the S106 record; the claims the merge touches were run singly by the integration; the "
                        "whole suite is the harness job 'r4 claim suite, merged'. New claims: type 'test (round 4)'. Inventions I192–I197. "
                        "Record: integration notes.md")
    d["about"]["text_under_review_round4"] = ("tests/106 The semantics, standing alone, without the written-in test.md (md5 c7af964c329ab7959243405d394e6574); "
                                              "text changes: text changes after round 4.json → tests/107 The semantics, standing alone, after round 4.md")
    d["about"]["model_round4"] = "results/S107 Round 4 - maths after the reading/model after round 4/"
    d["about"]["counts_after_round4"] = {k: cnt.get(k, 0) for k in (H, CEX, NT)}
    d["about"]["claims"] = len(d["claims"])
    with open(OUT_JSON, "x", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=1)

    M = ["# S107 Round 4 — formal claims, after round 4", "",
         "*Integration of round 4 (log S107), 28 September 2026: `results/S106 The written-in test taken out/formal claims, after S106.md` and "
         "`.json` (not written) with each claim's statement as it now stands, five new test claims, and the result expected on `model after round 4/` "
         "(the merged program; scale 4, time cap 45 s, PYTHONHASHSEED=0, --no-write): the area record that changed the claim, else the S106 record. "
         "The claims the merge touches were run singly on the merged program (`integration notes.md` §9); the whole suite is the harness job "
         "`r4 claim suite, merged` (key after_round4 of the json). Sources, quotations, parts: `formal claims, after round 4.json`. Column r4: "
         "'restated' = the statement changed (S106's kept in the json as formal_after_s106); 'note' = the code or its print changed, the statement "
         "kept; 'new' = a test claim of round 4 (not a move). H holds on all models tried; CEX counterexample found; NT not tested. Built by "
         "`build formal claims after round 4.py`.*", "",
         "**Counts.** After S106: 128 H, 2 CEX, 7 NT of 137. **After round 4 (expected): %d H, %d CEX, %d NT of %d** (137 + 5 new, each H; no "
         "status of an earlier claim changed; test parts FC84.new1 (a3), FC30.new1 (h) added, each as claimed). CEX: %s. NT: %s." % (
             cnt[H], cnt[CEX], cnt[NT], len(d["claims"]),
             ", ".join(c["id"] for c in d["claims"] if c["after_round4"]["status"] == CEX),
             ", ".join(c["id"] for c in d["claims"] if c["after_round4"]["status"] == NT)), "",
         "| id | claim | statement as it now stands | r4 | after S106 | after round 4 |", "|---|---|---|---|---|---|"]
    for c in d["claims"]:
        r4 = c.get("r4")
        mark = "" if not r4 else ("new (%s; %s)" % (r4["areas"], r4["findings"]) if r4["note"] == "new (round 4)"
                                  else ("restated: " if r4["restated"] else "") + r4["note"])
        s6 = SHORT[c["after_s106"]["status"]] if c.get("after_s106") else "—"
        M.append("| %s | %s | %s | %s | %s | %s |" % (c["id"], c["title"].replace("|", "∣"), c["formal"].replace("|", "∣"),
                                                     mark.replace("|", "∣"), s6, SHORT[c["after_round4"]["status"]]))
    M += ["", "**Not formalized.** NF01–NF19, NF.new1, NF.new2 as after S106; none added in round 4.", ""]
    with open(OUT_MD, "x", encoding="utf-8") as f:
        f.write("\n".join(M))
    print("claims %d; after round 4: %s; changed by one area: %s" % (len(d["claims"]), {SHORT[k]: v for k, v in cnt.items()},
                                                                    dict(changed_by)))


if __name__ == "__main__":
    main()
