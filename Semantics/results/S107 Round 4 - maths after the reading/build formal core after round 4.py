#!/usr/bin/env python3
"""S107 round 4, integration (rule 7): build `formal core, after round 4.md` from
`results/S106 The written-in test taken out/formal core, after S106.md` (read only; md5 checked) by exact replacements,
each span found exactly once, and write it as a NEW file beside this program (never over a file).
The fixes are the three areas' (`results/S107 Round 4 - area N - verdicts and formal fixes.md` §2) and the
integration's marks (pairs 5, 7, 9, 13, 14 of `integration notes.md` §4). Standard library only.
Run: python3 -B "build formal core after round 4.py"
"""
import hashlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "S106 The written-in test taken out", "formal core, after S106.md")
SRC_MD5 = "40d7c80ec78574794962fece34a4cb51"
OUT = os.path.join(HERE, "formal core, after round 4.md")

PRE = ("*Integration of round 4 (log S107), 28 September 2026: `results/S106 The written-in test taken out/formal core, after S106.md` "
       "(md5 40d7c80ec78574794962fece34a4cb51, not written) with every formal fix of the three areas "
       "(`results/S107 Round 4 - area N - verdicts and formal fixes.md` §2) put in place. A changed definition carries its new form and, "
       "in the mark, what it was; ids are kept; no paragraph added or removed (118). Each change is marked [r4: area; finding] "
       "(A1, A2, A3; the finding ids of the tabulation); the integration's own marks [r4: integration; pair n] (`integration notes.md` §4). "
       "Inventions I192–I197 (R4A1-01 → I192, R4A2-01 → I193, R4A2-02 → I194, R4A2-03 → I195, R4A3-01 → I196, R4A3-02 → I197): "
       "`inventions register - addendum after round 4.md`. Program: `model after round 4/` (its `model/corefile.py` reads this file). "
       "Text changes: `text changes after round 4.json` → `tests/107 The semantics, standing alone, after round 4.md` (R4A2-T1 at L271, "
       "R4INT-T1 at L536). Quotations `> Lnnn` stay those of the round-2 file (text 103); an [r4] mark names the text-107 change of a line "
       "where there is one (pair 14: D6.9 marked here; D9.7's [S106] mark already names S106-T11). The letter δ (pair 9): δ alone is "
       "D9.10's alleged defect; a subscripted δ is the designation of the organization it names (δ_D, δ_E, δ_c of a content in D14.7, "
       "δ_v of E_v in D7.4, δ_Conn in D9.10); D7.4 checked. Nothing is settled (S28).*")

R = [
    # title and preamble
    ("# S106 — formal core, after S106 (the written-in test taken out)\n",
     "# S107 Round 4 — formal core, after round 4\n\n" + PRE + "\n"),
    # D0.2 (A3 F3, F4)
    ("AtRest [I149]; Org_ℓ(h) and subhistory [I151]; q(o)", "AtRest [I149]; Org_ℓ(h) [I151]; q(o)"),
    ("Below (D9.2) is defined.", "Below (D9.2) and subhistory (D11.3, I151) are defined."),
    ("D18.1's nodes and folds are I181.",
     "D18.1's nodes and folds are I181. Used by D16.XV's shapes and defined nowhere (D16.XV says so of each): Work(kl) [(Elim), L540]; "
     "'without loss', 'operates on' [(Prov) (ii), (iii), L542]; 'fails to capture', 'not creative' [(QF), L544]. "
     "[r4: A3; S4 (F3): 'subhistory' was among the primitives 'stated, not defined'; D11.3 defines it (I151); the program's "
     "DEP['Episode'] loses the sink 'subhistory'] [r4: A3; S6 (F4): D16.XV's five undefined terms were in no list; the program's "
     "DEP['DefeatConds'] gains Work, WithoutLoss, OperatesOn, FailsToCapture, NotCreative, classed in D0_2_R4A3 (FC32.new1 (c))]"),
    # D6.3 (A2 F1; B9 I194)
    ("Slot_C(ℰ, k) :⟺ δ_E ∈ V_k ∧ Det_C ≠ ∅ ∧ ∀(a,b) ∈ Det_C: {w_δE : w ∈ L^E_k(τ(a),σ(b))} = {Ans_p(a,b)} **[I135; quantifier I136]**; "
     "likewise for a boundary coordinate of E whose value at σ(b) is Ans_p(a,b) [I79].",
     "Slot_C(ℰ, k) :⟺ δ_E ∈ V_k ∧ Det_C ≠ ∅ ∧ ∀(a,b) ∈ Det_C [t translates (a,b) ∧ {w_δE : w ∈ L^E_k(τ(a),σ(b))} = {Ans_p(a,b)}] "
     "**[I135; quantifier I136; I184]**; likewise for a boundary coordinate of E whose value at σ(b) is Ans_p(a,b), t translating (a,b) [I79]."),
    ("S106-T6 was the formula Slot_C(ℰ,k) ⇏ ¬Account(ℰ) (objection 2)]",
     "S106-T6 was the formula Slot_C(ℰ,k) ⇏ ¬Account(ℰ) (objection 2)] [r4: A2; B8, S3 (F1): was '∀(a,b) ∈ Det_C: "
     "{w_δE : …} = {Ans_p(a,b)} [I135; quantifier I136]', with no 't translates (a,b)' (D5.1): where τ(a) or σ(b) is undefined at a "
     "determined pair the clause had no value (FC23.new4 (a)); with π undefined on Sol_D(a,b) there it held while Pin failed "
     "(FC23.new4 (b)); now inside the ∀, as Pin and core.slot have it, and the [S106b] equivalence Slot ⟺ Det_C ≠ ∅ ∧ Pin at every "
     "pair of Det_C holds of D6.3 as written (FC23.new3 (a), FC23.new4 (c)). B9: Pin at a pair whose own edit alters k counts as a pin, "
     "I184 as registered **[I194]** (FC23.new4 (d)); (E) reads neither]"),
    # D6.9 (A2 F3, a mark)
    ("[r2: A2; D6.9, I26 ('≠ ⊥' dropped); A2-T2, A2-T3]",
     "[r2: A2; D6.9, I26 ('≠ ⊥' dropped); A2-T2, A2-T3] [r4: A2; W4: the quote is text 103's (preamble); L257 now reads "
     "'admits no candidate that meets (F2), (A) and \\(\\operatorname{Dependence}\\) (FC21)' (A2-T3, S106-T4)]"),
    # D7.4 (A2 F2; I195)
    ("Boundary := {(v,w) ∈ 𝒱² : Acc(E_v, p) ≠ Acc(E_w, p)}, each v ∈ 𝒱 declaring (E_v, t_v, Γ_v), t_v the transport the operation "
     "carries t to and Γ_v the commitments it leaves (L231). [r2: A2; D7.4]",
     "Boundary := {(v,w) ∈ 𝒱² : Acc((E_v, p, t_v, Γ_v, δ_v)) ≠ Acc((E_w, p, t_w, Γ_w, δ_w))}, each v ∈ 𝒱 declaring (E_v, t_v, Γ_v, δ_v), "
     "t_v the transport the operation carries t to, Γ_v the commitments it leaves and δ_v the designation it carries δ_E to "
     "(L231; D5.3, I20) **[I195]**. [r2: A2; D7.4] [r4: A2; N1 (B-N1, W-N1, S-N1, C-N1) (F2): was 'Acc(E_v, p) ≠ Acc(E_w, p)', each v "
     "declaring (E_v, t_v, Γ_v): Acc takes δ (D6.7); without δ_v Boundary is no function of the declared data (FC42.new1 (b); "
     "FC90.new1 (c)); δ_v carried, not quantified: L253 holds the query fixed (FC42.new1 (d)); core.boundary; L302 unchanged (the text's "
     "candidate carries no designation, I20)]"),
    # D9.7 (A3 K1, a pointer to the test claim; no change)
    ("it is about ruling out, not about what makes an explanation]",
     "it is about ruling out, not about what makes an explanation] [r4: A3; K1 (addendum): no change; the finding that a candidate "
     "assumes its own answer rules nothing out by itself, and taking 'Slot → ¬Acc' as given is the person's choice (L397, S28): "
     "computed on the myth about winter (FC72.new2 **[I197]**)]"),
    # D9.10 (A3 F5, notation)
    ("ℰ_c := (Conn, Qf(z,δ,p), t_c, Γ_c, δ_c), with t_c, Γ_c, δ_c supplied with c **[I147]**.",
     "ℰ_c := (Conn, Qf(z,δ,p), t_c, Γ_c, δ_Conn), with t_c, Γ_c and δ_Conn, the designation of Qf(z,δ,p)'s query in Conn (D5.3, I20), "
     "supplied with c **[I147]**; δ alone is the alleged defect (L377)."),
    ("(FC107: E8's p_δ, its identity candidate a slot, meets (E) now; round 3's (E) excluded it)]",
     "(FC107: E8's p_δ, its identity candidate a slot, meets (E) now; round 3's (E) excluded it)] [r4: A3; S-δ (F5): was "
     "'(Conn, Qf(z,δ,p), t_c, Γ_c, δ_c), with t_c, Γ_c, δ_c supplied with c': δ_c named ℰ_c's designation with c a criticism, where a "
     "subscript elsewhere names the organization (D3.1 δ_D, D5.3 δ_E, D14.7 δ_c with c a content); notation, content unchanged]"),
    # D12.2 (A1 N6; I192)
    ("which neither D12.2 nor D12.1 carries (R1 below; S47)]",
     "which neither D12.2 nor D12.1 carries (R1 below; S47)] [r4: A1; N6 (B11, W-N6, S-N6, C-N6): I191's reading of 'no question about "
     "the brief occurred to the agent' is recorded, not chosen anew, beside two others **[I192]**: (d) a question-occurrence its own Θ "
     "label, with or without an alleged defect; (e) a question found (L15, L155, L161), operative at its occurrence; they part ways on "
     "B11's cases and agree on (a1)'s chain; Con and Build at the output are the same under all three (FC84.new1 (a3)): no computed "
     "value reads the labels (S47)]"),
    # D13.8 (pair 13)
    ("hold a criticism (D9.10) because the agent asked, not because Con does]",
     "hold a criticism (D9.10) because the agent asked, not because Con does] [r4: A1; N6; integration, pair 13: the note kept as "
     "written; 'because the agent asked' is I191's reading; I192 records (d), under which a criticism can be used with no question "
     "occurring (a claim taken as given, S27), and (e); no value of (EX), Con or Build turns on it (FC84.new1 (a3)); A3's B12 not "
     "taken: (EX) needs a critical episode (L429, L447–L449), computed as FC32.new1 (f)]"),
    # D16.XV (A3 F7: the program's reading of Uses; I196)
    ("S41 (Q2) kept: Acc(ℰ) ∧ Dec(t) ⇒ ¬Expl(ℰ) for them as for any (FC23.new2 (f))]",
     "S41 (Q2) kept: Acc(ℰ) ∧ Dec(t) ⇒ ¬Expl(ℰ) for them as for any (FC23.new2 (f))] [r4: A3; W5 (F7): 'Acc ∉ Uses(α)' read as "
     "written, at the symbol: no leaf or form of α uses Acc of any candidate **[I196]**; the program read the instance before round 4 "
     "(no use of Acc(ℰ) for the candidate at issue), kept for comparison (claims_s41.USES_READINGS); the two part only on an argument "
     "whose only use of (E) is Acc(ℰ′) (FC30.new1 (h)); the program's reading of a definition]"),
    # D16.XV (Elim) (A3 F6, notation)
    ("a kind-label κ(ℰ) ≠ κ(ℰ') ∧ Work(κ); Work has no definition.",
     "a kind-label kl(ℰ) ≠ kl(ℰ′) ∧ Work(kl); Work has no definition; κ stays D5.1's value maps (I14) [r4: A3; S-κ (F6): was "
     "'κ(ℰ) ≠ κ(ℰ') ∧ Work(κ)'; notation, content unchanged]."),
    # D18.1 (A3 F2; integration pair 5)
    ("- T′: Con's 'available as a represented target' (D12.2) and Build's 'represented organization' (D13.3) := Held at o' ⪯ o in the "
     "episode; Sel's exclusion (D12.1)",
     "- T′: Con's 'available as a represented target' (D12.2, L197) := Held at o' ⪯ o_t in the episode; Build reads Held_ℓ(o, c) "
     "outright (D13.3; L405 since R3A3-T4), under every reading; Sel's exclusion (D12.1)"),
    ("FC98.new1 (a), FC98.new2 (a)].",
     "FC98.new1 (a), FC98.new2 (a)]. [r4: A3; S2 (F2): was 'Con's … (D12.2) and Build's 'represented organization' (D13.3) := Held at "
     "o' ⪯ o in the episode'; the program's DEP['Build']: staged (R) → Held, under every reading; the r3 mark's 'Build → ExplUse → (E)' "
     "now reads Build → Held, ExplUse; ExplUse → (E); FC98 (a), (a′) re-based, results unchanged] [r4: integration; pair 5: FC83's "
     "build_at keeps round 2's reading of L405's old wording under the rejected cuts U and K (Build through (R), staged under K), "
     "named alternatives FC83 names; under T and T′ it reads Held, as DEP does; read as Held under K, FC83 (a) gives K's own defect "
     "(FC98 (d); area 3 runs §3.6); not changed]"),
    # E1 (A2 B4, C-K1; integration pair 7; I193)
    ("Claims: FC02, FC07, FC26–FC28, FC99.",
     "Claims: FC02, FC07, FC26–FC28, FC27.new1, FC99. [r4: A2; B4, C-K1: 'the production contract' of L271 is C1 (R4A2-T1: "
     "'\\(C_1\\) (E1, FC27)'), and that of L536 (R4INT-T1; integration, pair 7) **[I193]**; C_H := {1} ∪ settings of H is a production "
     "contract too (L151, D3.3 Prod), and under τ′ on C_H E_rev meets (F2) and every conjunct of (E) (FC27.new1 (d))]"),
    # counts and date
    ("FC23.new2 (f) computed, (g) a look.\n",
     "FC23.new2 (f) computed, (g) a look. Round 4 (S107): 118 definition paragraphs (none added or removed); changed in form: D0.2 "
     "(twice: A3 F3, F4), D6.3 (A2 F1), D7.4 (A2 F2), D18.1 (A3 F2: the T′ item and the program's graph); notation: D9.10 (A3 F5), "
     "D16.XV (Elim) (A3 F6); the program's reading: D16.XV's Uses (A3 F7, I196); marks without a formal change: D6.9 (A2 F3), D9.7 (K1), "
     "D12.2, D13.8 (A1; I192), D18.1 (pair 5), E1 (I193); inventions I192–I197 (`inventions register - addendum after round 4.md`); "
     "142 claims (`formal claims, after round 4.md`: FC27.new1, FC23.new4, FC23.new5, FC42.new1, FC72.new2 new; test parts "
     "FC84.new1 (a3), FC30.new1 (h) new; FC31, FC98, FC32.new1 re-based).\n"),
    ("S106 (the written-in test taken out) on 28 September 2026.*",
     "S106 (the written-in test taken out) on 28 September 2026; after round 4 (S107) on 28 September 2026.*"),
]


def main():
    raw = open(SRC, "rb").read()
    md5 = hashlib.md5(raw).hexdigest()
    if md5 != SRC_MD5:
        sys.exit("REFUSED: source md5 %s, not %s" % (md5, SRC_MD5))
    if os.path.exists(OUT):
        sys.exit("REFUSED: %s exists; never written over" % os.path.basename(OUT))
    s = raw.decode("utf-8")
    for i, (old, new) in enumerate(R, 1):
        k = s.count(old)
        if k != 1:
            sys.exit("REFUSED: replacement %d: the old span occurs %d times: %r" % (i, k, old[:80]))
        s = s.replace(old, new)
    ids_src = [l.split("**")[1].split(" ")[0] for l in raw.decode("utf-8").split("\n") if l.startswith("**D")]
    ids_out = [l.split("**")[1].split(" ")[0] for l in s.split("\n") if l.startswith("**D")]
    if ids_src != ids_out:
        sys.exit("REFUSED: definition paragraphs changed")
    with open(OUT, "x", encoding="utf-8") as f:
        f.write(s)
    print("wrote %s: %d replacements; %d definition lines, as the source; md5 %s" % (
        os.path.basename(OUT), len(R), len(ids_out), hashlib.md5(s.encode("utf-8")).hexdigest()))


if __name__ == "__main__":
    main()
