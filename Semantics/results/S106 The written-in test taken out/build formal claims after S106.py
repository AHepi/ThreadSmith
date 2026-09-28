#!/usr/bin/env python3
"""S106 (decisions S44, S45): build `formal claims, after S106.json` and `.md` from round 3's
`formal claims, after round 3.json` (read only) and the whole-suite printout of `model after S106/`
(`S106 - whole suite, printout.txt`, scale 4, time cap 45 s, PYTHONHASHSEED=0, --no-write).
Every claim keeps its round-3 fields; S106 adds `s106` (restated or not, note), `formal_after_round3` where the
statement is restated, and `after_s106` (status and parts, parsed from the printout). Three new test claims.
Writes only the two files named above, beside this program; refuses to write over an existing one.
Run: python3 -B "build formal claims after S106.py"   (standard library only)
"""
import collections
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
R3 = os.path.join(HERE, "..", "S105 Round 3 - maths after the reading", "formal claims, after round 3.json")
PRINTOUT = os.path.join(HERE, "S106 - whole suite, printout.txt")
OUT_JSON = os.path.join(HERE, "formal claims, after S106.json")
OUT_MD = os.path.join(HERE, "formal claims, after S106.md")
# S47 (28 September 2026): --rebuild writes over this program's own earlier outputs, only if their md5s are these
# (S106's first build; after S47; the second checker on the critical review writes over the second)
REBUILD_OVER = {OUT_JSON: ("3d225297a9ea6179365debab0eab9b44", "d02562b63a3f2c2366d30d17aad1f0a8"),
                OUT_MD: ("72a9806787ff47128eeeed8868a833e5", "e7707ebfd711ebe485793bdc66bce7a2")}
REPRO = 'cd "/home/user/ThreadSmith/Semantics/results/S106 The written-in test taken out/model after S106" && PYTHONHASHSEED=0 python3 -B -m model.run --claim %s --scale 4 --time-cap 45'
H, CEX, NT = "HOLDS ON ALL MODELS TRIED", "COUNTEREXAMPLE FOUND", "NOT TESTED"
SHORT = {H: "H", CEX: "CEX", NT: "NT"}

# S106 per claim: (restated, new statement or None, new title or None, note)
S106 = {
    "FC21": (True, "(a) If every edit of C is a relabeling for p (I26), then for every ℰ with A_C(ℰ) and τ(1) = 1: ¬NC2(ℰ). (a2) The same with relabelings Ans_p(a,b) = Ans_p(1,b0), ⊥ = ⊥ (D6.9). (b) Without (A) the implication can fail. (c) 'Excluding every change under which the active commitments could matter to Q' is ¬NC2 for every candidate. (d) ∃ℰ: A ∧ Dependence ∧ τ(1) ≠ 1 on a contract of relabelings: L257 needs (F2) as well as (A) (A2-T3).",
             "A contract of relabelings admits no candidate meeting (A) and Dependence",
             "re-based on D6.5 (Dependence = NC2): (d) no longer asks NC1; L257 writes Dependence (S106-T4)"),
    "FC23": (True, "Let E_lk have Γ = {k}, L_k(τ(a),σ(b)) the answer slot for Ans_p(a,b) (I24), and no other component constraining the answer ports. (a) NC1 fails for E_lk (a slot, D6.3). (b) If Ans_p is not constant on C, NC2 holds for E_lk with G = {k}: after deleting k the answer is ⊥ at both points, so an answer E_lk determined is no longer determined. So E_lk meets Dependence (D6.5), and after S106 (E) does not exclude it for its slot (I24's alternative (a), taken by S45). (c) M1, M2, M3 fail NC1 under D6.3 (slots) and meet (E) after S106; round 3's (E) excluded them. (d) M5 meets (E) under I135; the quantifier (I136) no longer changes (E): a look. (e) Some E_lk meets (E) after S106.",
             "'p because p' meets Dependence where its answer varies; its slot is content, not a failure of (E)",
             "restated: the conclusion about (E) reverses (S44, S45); L273 replaced by the pointer (D6.3, FC23, FC24) (S106-T6); (e) added; CEX stays for (b) as stated (the claim's own wording, U3)"),
    "FC23.new1": (True, "Acc ∧ NC1_q ('meets (E) with no slot under q', round 3's (E)) under every / some / some-exempt / some-exempt-set (I136, I176): (a) pole C1 (T,T,T,T), C2, C3 (T,F,T,T), M5 (T,F,F,F), M13 (T,T,T,T), M1–M3 none; (b) W3's partial lookup meets it under 'every'; (c) 'some' alone excludes; (d) 'some-exempt' keeps what 'every' excludes; (e) 'some' implies the other three; (f) the two exempt extents differ; (g) L339's eliminative construction: FC62's encoding (T,F,F,F), a second encoding (T,T,T,T). (h) S106: (E) after S106 is the same under the four readings, on the cases of (a) and (g) (all T) and on generated models.",
                   "D6.3's quantifier: four readings of Slot; (E) the same under all four",
                   "restated: parts (a)-(g) read Acc ∧ NC1_q (round 3's (E)), content; (h) added; R3-Q1 answered (S44, S45)"),
    "FC24": (True, "No ℰ has Acc(ℰ) ∧ ¬Dependence(ℰ), by (E). Adding to Γ a component answering another question leaves the answer slot in place, so NC1 still fails (I24); after S106 the slot is content a criticism can point at (D6.3), not a failure of (E). L273 is replaced by a pointer to D6.3, FC23 and this claim (S106-T6).",
             "L273's second sentence used 'account' for a candidate; packaging leaves the slot (content)",
             "re-based on D6.5, D6.3; its line replaced by a pointer (S106-T6)"),
    "FC26": (False, None, None, "note: (E) after S106 is (F1), (F2), (A), Dependence (NC2) and non-vacuity; NC1 holds too, as the statement says"),
    "FC27": (False, None, None, "note: the look's text: (F2)'s homomorphism clause alone excludes the reversed calculation under τ'; NC1 fails too and is no longer a conjunct"),
    "FC30": (True, "Acc(ℰ) is a function of (D, C, b0, Q, δ, E, t, Γ, Σ) only (Σ the stated scope, I27; S106: not of the grain ℓ, which only NC1 read, I28); it takes no assessor, no Accepted_j, no history and no provenance. Faithful_C(t) is a function of (D, E, t, C). Candidates alike in these arguments have the same Acc value, whatever else differs.",
             None, "re-based on D6.7 (no grain)"),
    "FC31": (True, "(E) has five conjuncts; Part V has four headed conditions: Component fidelity = (F1) ∧ (F2), Question fidelity = (A), Dependence, Non-vacuity. 'The four conditions' at L61, L231 and L536 are the four headings. L520's three sources cover the four headings exactly when 'fidelity under change' has the wide extent Fid⁺ (I49); with the narrow extent L189 defines, L520 names no source for (A).",
             None, "re-based: the heading is Dependence (S106-T1)"),
    "FC32": (True, "(1) Every argument of Acc other than the candidate's own t and Γ ((O), (Q), C, δ, Σ) is an ancestor of (E) in D18.1's graph, to which L526 points (A3-L526.1, a pointer). (2) D18.1's edges for Dependence ({(O), (Q), C, δ}) and NonVacuous ({(O), C, Σ}) are the classes of symbols the program's NC2, dep and nonvacuous read (S106: ℓ no longer, I28; NC1's Slot is a node of its own, not an ancestor of (E)).",
             None, "re-based on D6.5, D6.7, D18.1 (the program's DEP: 'NC' renamed 'Dep', no ℓ; 'Slot' added)"),
    "FC33": (False, None, None, "note: (b)'s not-tested reason: after S106 no conjunct reads the grain; the scope clause is the one exception L265 names"),
    "FC34": (True, "Narrow reading (I73): there are p, p' with the same D, (C,Q) ≠ (C',Q'), and ℰ with Acc on p and not on p'. Wide reading: no ℰ has Acc on both. Test the wide reading with C' ⊊ C and the same Q: if NC2's witness pair lies in C' and Σ' states the scope of C', a candidate meeting (E) on C meets it on C' (S106: the hypothesis 'NC1 holds on C'' is gone with NC1). (NC1 can fail on C' while holding on C: a component can coincide with the answer slot on the fewer pairs of C'; content, D6.3.) Also: Acc is neither monotone nor antitone in C.",
             None, "re-based on D6.7; its witnesses change (Acc changed), not its parts' statuses"),
    "FC37": (False, None, None, "note: more random candidates meet (E) after S106, so more route systems are tested (hypothesis met 120 → 1661 in the printout)"),
    "FC46": (False, None, None, "note: more pairs of accounts tested (hypothesis met 66 → 962 in the printout)"),
    "FC51": (False, None, None, "note: the hypothesis met on more models (15 → 265 in the printout)"),
    "FC60": (False, None, None, "note: after S106 NC1 is not a conjunct of (E) either; the circularity is registered only by Part IX's block (D9.7)"),
    "FC74": (False, None, None, "note: another first witness (bearing relative to p), since Acc changed"),
    "FC100": (False, None, None, "note: Acc after S106; NC1's answer slot still carried along (content)"),
    "FC107": (False, None, None, "note: Acc of E8's identity candidate for p_δ is True after S106 (a slot; round 3's (E): False); the claim asks only that (E) assesses it"),
    "FC84.new1": (True, "Episode(h') :⟺ h' a subhistory whose changes of contract, if any, each carry a provenance record (D13.8, I165). (a) The bridge to a fixed brief (S47): an episode in which no question about the brief occurred to the agent as worth investigating (NoBriefQuestion: one contract throughout, no criticism aimed at it, I191), a construction trace preparing t, cod t held at the output: Con(t) at the output (one fixed point of (R), cut T′), and Build; under L55 as text 104 words it (an episode holds a change of contract) Con fails and Build holds; (a1) with no criticism in the history (o1 ≺ o2); (a2) with a criticism of an earlier design in it (o1 ≺ o2 ≺ o3, o2 criticizing the design at o1): Con either way, since Con reads no criticism event (I190); with that criticism aimed at the brief instead, NoBriefQuestion fails. (b) A recorded change of contract C → C′ at o2: o1 ≺ o2 is an episode under both readings, and Con. (c) The change unrecorded: o1 ≺ o2 is no episode; Con at o2 through {o2} under S41, none under L55's wording. (d) Every chain of ≤ 3 occurrences with contracts and records: Con(S41) ⊇ Con(L55's wording), differing exactly where no episode ending at the output holds a change of contract and the target; Sel ∧ Con at no fixed point; one fixed point each (T′).",
                  None, "restated (S47): (a) re-encoded as an episode in which no question about the brief occurred to the agent, not a history with no criticism; two parts, (a1) without and (a2) with criticism of designs, Con in both"),
    "FC32.new1": (True, "(a) every definition paragraph of §§1–16 a node of DEP or folded into one (I181); (b) U: a cycle through (R); K, T, T′: none; (c) the sinks D0.2 (after round 2) does not list are classed; (d) every dependence L526 states is a path (grouped subjects together, I179); Build ⇝ (E) only with ExplUse defined (I178); (e) only D16.XV reaches the atom Expl; (f) under U, K, T, T′, Con, CT and Episode reach no Crit (D9.10), (EX) does through CCE: the maths asks construction for no criticism event, and an episode of conjecture and criticism (L13) includes one in which no question occurred to the agent (S47, I190).",
                  None, "restated (S47): (f)'s reading; its computation unchanged; round 3 drew from it the deletion of L13's ' and criticism', which S47 reverts (S47-T1)"),
    "FC108": (True, "Under I23, NC0 holds of every candidate: every answer is computed by evaluating E at (τ(a),σ(b)), with σ(b) a function of b. A reading on which it adds a condition needs a notion of how an answer is computed (propagation against lookup) that (O) and (Q) do not give; I23's other reading (a) was the written-in test on a boundary, closed by S45 (I187: L255's 'independent' deleted, S106-T2).",
              "The first sentence of Dependence adds no condition", "re-based on D6.5, I187"),
}

# S106, second checker on the critical review (S106b): the change to each claim it touched, statuses unchanged
S106B = {
    "FC23": "S106-T6 is the pointer (D6.3, FC23, FC24), not the formula (objection 2)",
    "FC24": "D6.11 withdrawn (objection 1): the slot is content by D6.3; S106-T6 is a pointer (objection 2)",
    "FC32": "the node Open (D6.11) deleted with D6.11 (objection 1)",
    "FC23.new2": "(c), (d), (e) deleted: D6.11 (b), (c) parked, P8 (objection 1); (f) computed, (g) a look (objection 3); letters kept",
    "FC23.new3": "(b), (c) and (d)'s LeavesOpen clause deleted: D6.11 (b), (c) parked, P8 (objection 1); letters kept",
}

NEW = [
    dict(id="FC23.new2", title="The owner's shop sign (S44): an explanation under (E) after S106",
         source=[], formal="(a) ℰ_two (a red part pinning red on Mondays, a blue part pinning blue on Tuesdays; no slot under 'every') meets (E) under every reading of D6.3's quantifier; round 3's (E): (T,F,F,F). (b) ℰ_one (one part: red on Mondays, blue on Tuesdays) is a slot under every reading and meets (E) after S106; round 3's (E) excluded it under every reading. (f) S41 (Q2) kept, computed as FC30.new1 (a): with a declared transport (Dec) and an argument not using (E) that rules out Expl(ℰ), ℰ_two and ℰ_one are outside (Suff)'s defeat set as S41 and L536 write it (Acc ∧ Dec ⇒ ¬Expl), inside it as text 104's L17 words it; with a constructed transport, inside all three. (g) Look: slot, NC1, pin and pins each take one candidate; none orders candidates.",
         inventions=["I184", "I189", "I90"], formal_core_sections=["§6"]),
    dict(id="FC23.new3", title="Pin (D6.3's clause at one pair) on generated models and on the pole",
         source=[], formal="(a) Slot_C(ℰ,k) ⟺ Det_C ≠ ∅ ∧ Pin(ℰ,k;a,b) at every (a,b) ∈ Det_C. (d) The pole's forward candidate: on C1 no pin; on C2 c_L pins exactly at the settings of L (the pair's own edit puts the slice there).",
         inventions=["I184"], formal_core_sections=["§6"]),
    dict(id="FC25.new2", title="L269's encoding table meets (E) where its answer varies; its one component a slot",
         source=[{"line": 269, "quote": "it meets (F1) as a decomposition does, and it is an account when it meets the other conjuncts of (E)"}],
         formal="(a) Ans_p not constant on C ∧ Sol_D(1,b0) ≠ ∅ ∧ every port of D in a footprint ⇒ Acc(E_enc). (b) Det_C ≠ ∅ ⇒ Slot_C(E_enc, tab) (D6.3, 'every'). (c) The pole: E_enc (δ = L) meets (E) after S106 on C1 and C2; round 3's (E) excluded it (NC1).",
         inventions=["I32", "I184"], formal_core_sections=["§6"]),
]


def parse(path):
    out, cur = collections.OrderedDict(), None
    for line in open(path, encoding="utf-8"):
        m = re.match(r"^(FC[0-9A-Za-z.]+)  (%s|%s|%s)" % (H, CEX, NT), line)
        if m:
            cur = m.group(1)
            out[cur] = {"status": m.group(2), "parts": []}
            continue
        m = re.match(r"^-- (.*) \[([^\]]+)\] (.*)$", line.rstrip("\n"))
        if m and cur:
            out[cur]["parts"].append({"label": m.group(1), "kind": m.group(2), "status": m.group(3)})
    return out


def main():
    import hashlib
    for p in (OUT_JSON, OUT_MD):
        if os.path.exists(p):
            md5 = hashlib.md5(open(p, "rb").read()).hexdigest()
            if "--rebuild" not in sys.argv[1:] or md5 not in REBUILD_OVER[p]:
                sys.exit("REFUSED: %s exists (md5 %s); --rebuild writes over this program's own earlier output only" % (os.path.basename(p), md5))
    d = json.load(open(R3, encoding="utf-8"))
    res = parse(PRINTOUT)
    ids = [c["id"] for c in d["claims"]]
    for c in d["claims"]:
        r = res[c["id"]]
        c["after_s106"] = {"status": r["status"], "parts": r["parts"], "reproduce": REPRO % c["id"]}
        if c["id"] in S106:
            restated, formal, title, note = S106[c["id"]]
            c["s106"] = {"restated": restated, "note": note}
            if restated:
                c["formal_after_round3"] = c["formal"]
                c["formal"] = formal
                if title:
                    c["title_after_round3"] = c["title"]
                    c["title"] = title
        else:
            c["s106"] = None
        for inv in {"FC84.new1": ["I190", "I191"], "FC32.new1": ["I190"]}.get(c["id"], []):  # S47
            if inv not in c["inventions"]:
                c["inventions"].append(inv)
    for n in NEW:
        r = res[n["id"]]
        c = dict(id=n["id"], title=n["title"], source=n["source"], formal=n["formal"], type=["test (S106)"], s100_units=[], round1=[],
                 inventions=n["inventions"], formal_core_sections=n["formal_core_sections"], look="", round2_result=None, r2=None, r3=None,
                 after_round3=None, s106={"restated": False, "note": "new (S106)"},
                 after_s106={"status": r["status"], "parts": r["parts"], "reproduce": REPRO % n["id"]})
        base = n["id"].split(".")[0]
        at = max(i for i, x in enumerate(d["claims"]) if x["id"].split(".")[0] == base)
        d["claims"].insert(at + 1, c)
    for c in d["claims"]:
        if c["id"] in S106B:
            c["s106b"] = S106B[c["id"]]
    missing = sorted(set(res) - set(c["id"] for c in d["claims"]))
    if missing:
        sys.exit("REFUSED: claims in the printout and not in the json: %s" % missing)
    cnt = collections.Counter(c["after_s106"]["status"] for c in d["claims"])
    for u in d["strong_candidates"]:
        if u["unit"] == "L273.s1":
            u["s106"] = "L273 replaced by the pointer (D6.3, FC23, FC24) (S106-T6); FC23 restated: the lookup meets (E) where its answer varies"
    d["about"]["s106"] = ("S106 (decisions S44, S45), 28 September 2026: the written-in test (NC1, D6.3) taken out of (E). s106: {restated, note} "
                          "(restated: the statement changed; formal_after_round3 keeps round 3's); after_s106: the whole suite on "
                          "results/S106 The written-in test taken out/model after S106/ (scale 4, time cap 45 s, PYTHONHASHSEED=0, --no-write). "
                          "New claims: type 'test (S106)'. Record: results/S106 The written-in test taken out/S106 report.md")
    d["about"]["counts_after_s106"] = {k: cnt.get(k, 0) for k in (H, CEX, NT)}
    d["about"]["second_check_s106"] = ("second checker on the critical review of S106, 28 September 2026 (results/S106 The written-in test taken out/S106 the second checker on the critical review.md): "
                                       "s106b notes on FC23, FC24, FC32, FC23.new2, FC23.new3; D6.11 withdrawn; whole suite rerun (scale 4, cap 45 s, PYTHONHASHSEED=0, --no-write); statuses unchanged")
    d["about"]["claims"] = len(d["claims"])
    json.dump(d, open(OUT_JSON, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

    M = ["# S106 — formal claims, after S106", "",
         "*S106 (decisions S44, S45), 28 September 2026; S47 applied inside S106 (FC84.new1, FC32.new1 restated): `results/S105 Round 3 - maths after the reading/formal claims, after round 3.md` and `.json` (not written) with each claim's statement as it now stands, three new test claims, and the result on `model after S106/` (scale 4, time cap 45 s, PYTHONHASHSEED=0; whole suite with --no-write; printout `S106 - whole suite, printout.txt`). Sources, quotations, parts: `formal claims, after S106.json`. The S106 column: 'restated' = the statement changed (round 3's kept in the json); 'note' = the code or its print changed, the statement kept; 'new' = a test claim of S106 (not a move). H holds on all models tried; CEX counterexample found; NT not tested. Built by `build formal claims after S106.py`.*", "",
         "**Counts.** After round 3: 125 H, 2 CEX, 7 NT of 134. **After S106: %d H, %d CEX, %d NT of %d** (134 + 3 new, each H; no status of an earlier claim changed; FC23.new1 would have gone H → CEX had its parts kept reading (E), and is restated to read round 3's (E) as Acc ∧ NC1_q, with (h) added). Second checker on the critical review: D6.11 withdrawn, FC23.new2 (c)–(e) and FC23.new3 (b), (c) deleted (parked, P8), FC23.new2 (f) computed and (g) a look; no status changed; column S106 marks its changes 'second checker'. CEX: %s. NT: %s." % (
             cnt[H], cnt[CEX], cnt[NT], len(d["claims"]),
             ", ".join(c["id"] for c in d["claims"] if c["after_s106"]["status"] == CEX),
             ", ".join(c["id"] for c in d["claims"] if c["after_s106"]["status"] == NT)), "",
         "| id | claim | statement as it now stands | S106 | after round 3 | after S106 |", "|---|---|---|---|---|---|"]
    for c in d["claims"]:
        s6 = c.get("s106")
        mark = "" if not s6 else ("new" if s6["note"] == "new (S106)" else ("restated: " if s6["restated"] else "note: ") + s6["note"].replace("note: ", ""))
        if c.get("s106b"):
            mark += "; second checker: " + c["s106b"]
        r3 = SHORT[c["after_round3"]["status"]] if c.get("after_round3") else "—"
        M.append("| %s | %s | %s | %s | %s | %s |" % (c["id"], c["title"].replace("|", "∣"), c["formal"].replace("|", "∣"), mark.replace("|", "∣"), r3, SHORT[c["after_s106"]["status"]]))
    M += ["", "**Not formalized.** NF01–NF19, NF.new1, NF.new2 as after round 3; none added in S106.", ""]
    open(OUT_MD, "w", encoding="utf-8").write("\n".join(M))
    print("claims %d; after S106: %s" % (len(d["claims"]), dict(cnt)))


if __name__ == "__main__":
    main()
