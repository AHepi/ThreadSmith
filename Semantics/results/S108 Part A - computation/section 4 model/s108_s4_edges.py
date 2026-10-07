# S108 Part A, section 4: the edges (rule 5): every edge the reply names, marked computed / contradicted / not settled by
# computation (with what would settle it), and the edges the computation adds. Writes
# "results/S108 Part A - section 4 - variants computed.json" and prints the tables of §8 of the results file.
#   python3 -B s108_s4_edges.py > edges_tables.md
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.normpath(os.path.join(HERE, "..", "..", "S108 Part A - section 4 - variants computed.json"))

R, A = "reply", "computation (not named by the reply)"
C, X, N = "computed", "contradicted", "not settled by computation"

EDGES = [
    # ---- V4.1 ------------------------------------------------------------------------------------------------------
    dict(id="E4.1a", variant="V4.1", kind="moves", item="Expl gains ¬Slot; D18.1's graph: Slot an ancestor of Expl/(Suff)", mark="D18.1 S4; D16.XV S4", named_by=R, standing=C,
         reply_why="the written-in test re-enters through the explainer, not the account (reply: not settled, needs the graph recomputed)",
         evidence="graph recomputed: DefeatConds (D16.XV) gains Slot and through it ℓ, Cand, Transport; Expl stays an atom (a sink); Slot is reached by DefeatConds only; (E)'s ancestors unchanged. Being an explanation T → F on 10 of 29 worked cases, 941 of 1,019 generated Acc-T candidates (each ¬Dec history)"),
    dict(id="E4.1b", variant="V4.1", kind="changes with", item="L17, L49, L61, L69 (Account(ℰ) ∧ ¬Dec(t) as being an explanation)", mark="S1", named_by=R, standing=C,
         reply_why="every sentence writing Account(ℰ) ∧ ¬Dec(t) reverses",
         evidence="the formula they write parts from V4.1's being an explanation on 10 worked cases (ℰ_one, E_enc C1 and C2, E_rev τ′ on C_H, 'p because p', M1–M3, the hand-turned vane, E8's identity candidate) under Con, Sel and relay histories; L61's (Suff) fails by definition of ℰ_one (FC30.new1 (c), (Suff) kept)"),
    dict(id="E4.1c", variant="V4.1", kind="changes with", item="the L267–L277 table ('a written-in answer never stops…')", mark="L269–L277 S2 (L267 a heading)", named_by=R, standing=X,
         reply_why="the row 'a written-in answer never stops…' reverses",
         evidence="L269–L277 speak of (E), which V4.1 does not move (E_enc still meets (E): Acc unchanged on every case); the quoted row is the brief's summary of S44, S45 (brief line 90), not a line of the text; what it summarizes (S44, S45) is reversed on 10 worked cases (§9)"),
    dict(id="E4.1d", variant="V4.1", kind="changes with", item="FC30.new1", mark="claim S1, S4", named_by=R, standing=C,
         reply_why="runs show the slot/pin facts",
         evidence="(Suff) kept (as written): FC30.new1 (c) holds → fails by construction at (Acc T, Dec F, Slot T); (Suff) co-varied: (c) holds, (b)'s second identity (Def(L17 as text 104) = Def(L536) ∪ declared) fails on slot candidates (suite, §7)"),
    dict(id="E4.1e", variant="V4.1", kind="changes with", item="FC23.new2", mark="claim (S44)", named_by=R, standing=C,
         reply_why="runs show the slot/pin facts",
         evidence="(Suff) kept: no result moves ((f) checks the owner's condition, which V4.1 keeps); (Suff) co-varied: (f) moves (ℰ_one constructed leaves (Suff)'s defeat set) (§7)"),
    dict(id="E4.1f", variant="V4.1", kind="changes with", item="FC23.new3, FC25.new2", mark="claims S2", named_by=R, standing=X,
         reply_why="runs show the slot/pin facts",
         evidence="no result of either moves under V4.1 (suite, both sub-choices): they compute the Pin, Slot and Acc facts V4.1 reads, which V4.1 does not change"),
    dict(id="E4.1g", variant="V4.1", kind="blocks", item="none FROZEN", mark="-", named_by=R, standing=C,
         reply_why="the rule strengthened is S4's own; the exclusion is the owner's, not a frozen line",
         evidence="in D18.1 the only node gaining an edge is DefeatConds (D16.XV, S4); the claims that move (FC30.new1, FC23.new2) test S1/S4 lines and S44; no FROZEN definition reaches Slot. Frozen sentences are not read by the program (not searched beyond the graph)"),
    dict(id="E4.1h", variant="V4.1", kind="changes with", item="ℓ, 'at the declared grain' (D6.3's NC1 words; I28)", mark="D6.3 S2", named_by=A, standing=C,
         evidence="under V4.1 ℓ becomes an ancestor of D16.XV's defeat conditions (graph); after S106 ℓ was an ancestor of no conjunct of (E) and of no defeat condition"),
    dict(id="E4.1i", variant="V4.1", kind="changes with", item="D6.3's quantifier over Det_C (I136)", mark="D6.3 S2", named_by=A, standing=C,
         evidence="the owner's two-part sign stays an explanation under V4.1 only with 'every' (T, F, F, F under every / some / some-exempt / some-exempt-set); under 'some' the pole's forward candidate on C2 and C3, M5 and E5 (FC62's encoding) also stop; generated Acc-T with a slot: 941 / 952 / 849 / 854"),
    dict(id="E4.1j", variant="V4.1", kind="constrains", item="(Suff)'s shape (D16.XV; L61, L536)", mark="D16.XV S4; L61 S1; L536 S4", named_by=A, standing=C,
         evidence="with (Suff)'s antecedent kept, V4.1 makes (Suff) as conjectured fail by definition of every constructed or selected candidate with a slot (FC30.new1 (c) fails by construction; ℰ_one: 'holds of ℰ_one' F); only with the antecedent co-varied (Acc ∧ ¬Dec ∧ ¬Slot) do the two have a common model"),
    dict(id="E4.1k", variant="V4.1", kind="moves", item="the pole's forward candidate on C2 ('8 pins by c_L')", mark="E1 S2", named_by=A, standing=C,
         evidence="the reply's trace has it stop being an explanation: under 'every' it has no slot (pins only at the settings of L) and stays (T → T); it stops only under 'some' (a correction of the reply's trace, recorded as an edge of the quantifier, E4.1i)"),
    dict(id="E4.1l", variant="V4.1", kind="constrains", item="D18.2 (structure-preserving bijections; Argument 8)", mark="D18.2 S4", named_by=A, standing=C,
         evidence="the reply's (d) says V4.1 is safe: FC100's generator and bijections at scale 4 (12,960 port-query models, seed 108404): Slot under all four readings, the pins and Acc are kept by every bijection tried (0 exceptions), so V4.1's being an explanation is kept"),
    # ---- V4.2 ------------------------------------------------------------------------------------------------------
    dict(id="E4.2a", variant="V4.2", kind="moves", item="Expl := Acc; being an explanation loses ¬Dec", mark="D16.XV S4", named_by=R, standing=C,
         reply_why="provenance leaves explanation entirely",
         evidence="F → T on 24 of 29 worked cases under a declared or unrecorded history (every Acc-T case), the student's copy (FC30.new1 (d)), a link no pair tried (FC30.new1 (e)), CT8's R2 and R4, FC-E 7, CT 4, 1,019 of 1,019 generated Acc-T candidates"),
    dict(id="E4.2b", variant="V4.2", kind="changes with", item="L17/L49/L61/L69; D16.XV (Suff) shape; FC30.new1 (the one-defeat-set identity (b))", mark="S1; D16.XV S4", named_by=R, standing=C,
         reply_why="the one-defeat-set identity FC30.new1 (b) is what breaks",
         evidence="(b) breaks under the reply's trace reading (S108-4-I2 'L17': Def(L17) T, Def(L536) F for the declared copy; with (a), (c), (d), (e) of FC30.new1 and FC23.new2 (f)); as written ('rule') (b) holds and FC30.new1 (c) (the owner's condition) and FC23.new2 (f) fail instead; with 'both', (b) holds and (a), (c), (d), (e) fail: the declared copy is in both defeat sets (suite, §7)"),
    dict(id="E4.2c", variant="V4.2", kind="constrains", item="FC30 ((E) takes no provenance)", mark="claim S1, S2", named_by=R, standing=C,
         reply_why="still holds: Acc unchanged; only Expl moves",
         evidence="FC30 unchanged in the suite under V4.2 (every sub-choice); Acc unchanged on every case, script and generated candidate"),
    dict(id="E4.2d", variant="V4.2", kind="blocks", item="the owner's condition Acc ∧ Dec ⇒ ¬Expl (S41 Q2), as FC30.new1 (c) and FC23.new2 (f) compute it", mark="D16.XV S4 (owner S41)", named_by=A, standing=C,
         evidence="FC30.new1 (c) fails by construction at (Acc T, Dec T); FC23.new2 (f) not as claimed (ℰ_two, ℰ_one declared are explanations)"),
    dict(id="E4.2e", variant="V4.2", kind="moves", item="CT8's readings R2, R4 (Build's primitives not met)", mark="CT8 (case)", named_by=A, standing=C,
         evidence="the chosen pair's transport is declared under R2, R4 (T′): not an explanation now, an explanation under V4.2 only"),
    # ---- V4.3 ------------------------------------------------------------------------------------------------------
    dict(id="E4.3a", variant="V4.3", kind="constrains", item="D12.3/D12.4, provenance per holding", mark="D12.3 S2; D12.4 FROZEN", named_by=R, standing=C,
         reply_why="whether 'no record at all' is possible decides whether V4.3 is vacuous (reply: not settled)",
         evidence="a holding with no record is Dec (D12.3: no parameters give Sel, none give Con; H0: Dec on 29 of 29); at every holding not reached by a transfer ¬Dec(t) ⇔ Sel ∨ Con ⇒ Sel ∨ CT (chains: 0 exceptions in 39,926 holdings), so V4.3 is vacuous there; it bites only at transferred holdings, whose provenance D12.3's first clause and D12.4 [FROZEN] inherit"),
    dict(id="E4.3b", variant="V4.3", kind="moves", item="Expl and (Suff)'s range", mark="D16.XV S4", named_by=R, standing=C,
         reply_why="explanation demands positive provenance",
         evidence="only relayed or recorded copies move, T → F: (a) of constructed and selected holdings (worked cases 24 + 24; chains 2,692 holdings; generated 1,019 + 1,019), (b) of selected holdings only (24; 1,126; 1,019); no case with no record moves"),
    dict(id="E4.3c", variant="V4.3", kind="changes with", item="L17 etc.; FC25.new2's reading ('the encoding table stops being an explanation')", mark="S1; claim S2", named_by=R, standing=X,
         reply_why="the encoding table stops being an explanation, so the worked cases change role",
         evidence="E_enc with no record is Dec now and under V4.3 (not an explanation either way); with Con or Sel it is one either way; it moves only as a relayed copy; FC25.new2 does not move (suite)"),
    dict(id="E4.3d", variant="V4.3", kind="changes with", item="D12.4 (a transfer gives each part at o′ the value it had at o)", mark="FROZEN", named_by=A, standing=C,
         evidence="under V4.3 (a) an inherited Con or Sel no longer makes a transferred holding an explanation: FC30.new1 (f)'s K3 reading (the student's component transferred, Con inherited) T → F; E9's t1 relayed T → F; (b) keeps relays of constructed holdings"),
    dict(id="E4.3e", variant="V4.3", kind="changes with", item="which holding CT(t) is read at (S108-4-I3)", mark="D12.2 S2", named_by=A, standing=C,
         evidence="(a) the holding itself: relays of constructed holdings move; (b) the holding or one it was transferred from: they do not; (c) through inherited provenance: V4.3 is now's reading (0 moves)"),
    dict(id="E4.3f", variant="V4.3", kind="constrains", item="D18.2 (bijections carry occurrences; Argument 8)", mark="D18.2 S4", named_by=A, standing=N,
         evidence="the reply's (d): 'V4.3 is not obviously φ-invariant'; in the program's chains Sel, CT and transfers are fixed by ≺ and the transfer relation, which a structure-preserving bijection keeps, so V4.3 is kept there trivially; the program's histories are hand-set labels (I90)",
         what_would_settle="histories built by the program (Θ realized), with D18.2's bijections acting on occurrences, and V4.3 computed before and after"),
    # ---- V4.4 ------------------------------------------------------------------------------------------------------
    dict(id="E4.4a", variant="V4.4", kind="constrains", item="X_j / Out_j (D9.x), assessor-relative", mark="D9.6, D9.7 S3", named_by=R, standing=C,
         reply_why="the widened defeat set is still assessor-relative; nothing overrides j's choice (S21)",
         evidence="the defeat set grows only through X_j: for a j that takes Acc(ℰ′) and Acc(ℰ′) → ¬Expl(ℰ) as given (usable by modus ponens); the record argument (r, r → ¬Expl) is in it under both readings"),
    dict(id="E4.4b", variant="V4.4", kind="moves", item="(Suff) and (Nec) defeat sets only", mark="D16.XV S4", named_by=R, standing=C,
         reply_why="'not using (E)' shrinks from symbol to instance; being an explanation unchanged",
         evidence="(Suff): FC30.new1 (h)'s ℰ_fwd and E9's t1∘ψ enter (instance T, symbol F), declared ones do not; generated: 1,019 (Con), 1,019 (Sel); (Nec): 3,979 generated candidates exposed now enter; the full pole's E_rev on C1 only with V4.5 too (not exposed now); Acc and being an explanation: 0 moves; suite: 0 claims move"),
    dict(id="E4.4c", variant="V4.4", kind="blocks", item="any FROZEN item (the reply's unsettled edge)", mark="-", named_by=R, standing=N,
         reply_why="nothing frozen defines Uses(α); the nearest, L556.s3, is about Argument 1's proof",
         evidence="a search of the template: no FROZEN sentence or definition holds 'not using' or Uses (the three that hold it, L17.n2, L536.s1, L538.s1, are middle: S1, S4, S4); the program has no node for Uses",
         what_would_settle="a reading, not a run: whether citing a rival's being an account is 'using (E)' (the owner's gloss of argument, S23), as the reply says"),
    dict(id="E4.4d", variant="V4.4", kind="changes with", item="V4.5 ((Nec)'s exposure)", mark="D16.XV S4", named_by=A, standing=C,
         evidence="for E_rev on the full pole's C1 both are needed: the rival-citing argument counts only at the instance (V4.4) and E_rev is exposed only on C alone (V4.5); on FC30.new1's pole (θ at 45) it is exposed under neither; generated: 2,138 candidates enter (Nec)'s defeat set with both on and not with V4.4 alone"),
    # ---- V4.5 ------------------------------------------------------------------------------------------------------
    dict(id="E4.5a", variant="V4.5", kind="constrains", item="L606.s4 (Argument 7), FC99", mark="L606.s4 S4; claim S4", named_by=R, standing=C,
         reply_why="'ℰ can meet (E) on C and fail on C′' is the resource the variant trades on",
         evidence="FC99 unchanged (suite); now's exposure fails for 28 of 29 worked cases, each having a transport faithful at a single baseline pair (C′ = {(1,b)}; for 24 their own t is faithful on C), and for 3,979 of 17,280 generated candidates it holds: fidelity on some contract is cheap, the transport-level form of Argument 7's point"),
    dict(id="E4.5b", variant="V4.5", kind="changes with", item="L538.s1 (co-varied); FC30.new1 (g); Part VII's exposure (E5)", mark="L538.s1 S4; claim S1, S4; E5 FROZEN", named_by=R, standing=X,
         reply_why="(Nec)'s exposed case widens from eliminative to every unpreservable-on-C candidate (reply: not settled, needs FC62 under the varied shape)",
         evidence="E5's two encodings meet (E), so their own t is faithful on C: exposed under neither shape (contradicted for E5); FC30.new1 (g) unchanged (t faithful); the widening is real elsewhere: E_rev under τ and τ′ on C1, E_tab on C1 and C2, 2,138 generated, all Acc F"),
    dict(id="E4.5c", variant="V4.5", kind="moves", item="L538.s2 'Eliminative explanation (Part VII) is the exposed case'", mark="L538.s2 S4", named_by=A, standing=C,
         evidence="neither of E5's encodings [FROZEN] is exposed under now's shape or V4.5's; the one worked case exposed now is L257's contract of relabelings (no injective θ_k exists: exact in D5.1's class)"),
    dict(id="E4.5d", variant="V4.5", kind="moves", item="(Nec)'s defeat set on the worked cases", mark="D16.XV S4", named_by=A, standing=C,
         evidence="exposed now: 1 of 29 (the relabelings); under V4.5: 5 (+ E_rev τ and τ′ on C1, E_tab C1 and C2); no candidate meeting (E) is exposed under either"),
    # ---- V4.6 ------------------------------------------------------------------------------------------------------
    dict(id="E4.6a", variant="V4.6", kind="constrains", item="D5.3/I20 (designation)", mark="D5.3 FROZEN", named_by=R, standing=C,
         reply_why="δ's role is fixed upstream; the variant only stops reading it",
         evidence="(E) reads δ through (A) and Dependence: the pole on C1 meets (E) with δ = L only; FC90.new1 (c) unchanged"),
    dict(id="E4.6b", variant="V4.6", kind="moves", item="𝔈_Θ, UU, UECS; nothing in (E)", mark="D16.4 S4", named_by=R, standing=C,
         reply_why="universality's domain loosens from designation (reply: not settled, reach unknown without a search)",
         evidence="on the searched witnesses: 1 of 17,280 generated candidates (SMALL) and 2 of 25,920 (MID) meet (E) only with a non-designated δ (so enter 𝔈_Θ through it under V4.6); 334 and 355 meet it with the designated δ and another; worked cases: none (on the pole with θ at 45, δ = H also meets (E), δ = L too); (E) unchanged; 𝔈's graph unchanged. Membership over every (p, t, Γ) not computed"),
    dict(id="E4.6c", variant="V4.6", kind="changes with", item="the pole with θ at 45 (FC30.new1's target): L = H at every pair", mark="E1 S2", named_by=A, standing=C,
         evidence="the forward candidate meets (E) with δ_E = L and with δ_E = H: the designation clause separates witnesses there, not contents"),
    # ---- V4.7 ------------------------------------------------------------------------------------------------------
    dict(id="E4.7a", variant="V4.7", kind="blocks", item="L495.s1 (barriers: 'every admitted, non-question-begging enabling condition leaves the relevant capability unavailable')", mark="L495.s1 FROZEN", named_by=R, standing=C,
         reply_why="with NQB out of Enable the barrier sentence can no longer be read through Enable",
         evidence="on the toy (S108-4-I7, the only reading computable): with the barrier read as L495.s1's words have it, 'barrier ∧ UU' holds on 0 of 484 assignments now and on 217 under V4.7: the frozen barrier no longer excludes universality over the same content. The program computes no barrier, Enable or UU: on the program itself not settled",
         what_would_settle="a (CT1)/Can model of tasks and realizations in the program; then Enable, UU and a barrier computed on it"),
    dict(id="E4.7b", variant="V4.7", kind="moves", item="UECS only", mark="D16.4 S4", named_by=R, standing=C,
         reply_why="no conjunct of (E), no defeat set, no Expl reads Enable",
         evidence="graph: Enable is reached by UU, UC, UECS and Classes only, now and under V4.7; (E), Dec, DefeatConds do not reach it; toy: UU moves F → T on 217 of 484; all 24 script runs and the suite: nothing moves"),
    dict(id="E4.7c", variant="V4.7", kind="changes with", item="Part IV's provenance (Sel, Con, CT, Held, (R), surv, 𝒯pop)", mark="D12.1–D12.5 S2/FROZEN", named_by=A, standing=C,
         evidence="graph: under V4.7 Enable loses (R) and β, and UU, UC, UECS no longer reach any provenance node: universality stops reading provenance"),
    dict(id="E4.7d", variant="V4.7", kind="changes with", item="the universal class (L528's membership sentences; D16.5's Universal)", mark="L528.s1–s4 FROZEN; D16.5 S4", named_by=A, standing=C,
         evidence="graph: Classes (D16.5) reaches Enable through UECS; the class's words are unchanged and its extension grows with UU (toy: UU F → T on 217 of 484)"),
    # ---- V4.8 ------------------------------------------------------------------------------------------------------
    dict(id="E4.8a", variant="V4.8", kind="constrains", item="D12.1 surv; L574.s2", mark="D12.1 S2; L574.s2 FROZEN", named_by=R, standing=C,
         reply_why="surv supplies the dropped conjunct; the alteration step rests on L574.s2, which does not block (the reply's gloss, reworded: S23)",
         evidence="FC80 (d), (d′) (L574's step) and FC80.new1 unchanged under V4.8 (suite); surv still reaches the defeat conditions through Sel (graph)"),
    dict(id="E4.8b", variant="V4.8", kind="moves", item="(Prov)(i) from closed by definition to open", mark="D16.XV S4", named_by=R, standing=C,
         reply_why="what would rule the class out changes content (reply: not settled, needs FC80 re-run)",
         evidence="built on the pole: (Prov)(i) F now, T under V4.8; generated: 0 of FC80's own 9,930 populations, 1,647 of 9,768 wide ones (a member altered at an unseen pair's image and at H's, or τ×σ not one-to-one); now: 0 anywhere (FC80 (a))"),
    dict(id="E4.8c", variant="V4.8", kind="changes with", item="L572.s2, L574.n4, L576.s1, L576.s4 (co-varied)", mark="S4", named_by=R, standing=N,
         reply_why="Argument 3's wording and consequence shift together",
         evidence="the sentences are not read by the program",
         what_would_settle="a reading of the four sentences against Underdet without surv"),
    dict(id="E4.8d", variant="V4.8", kind="changes with", item="FC80", mark="claim S4", named_by=R, standing=C,
         reply_why="Argument 3's wording and consequence shift together",
         evidence="FC80's underdetermination witness is read through D12.9 under V4.8 (every member); its status holds; its text moves (suite, §7)"),
    dict(id="E4.8e", variant="V4.8", kind="blocks", item="D16.XV's note '(Prov)(i) unsatisfiable by definition (FC80 (a))'", mark="D16.XV S4", named_by=A, standing=C,
         evidence="satisfiable under V4.8 (the pole case; 1,647 generated models)"),
    dict(id="E4.8f", variant="V4.8", kind="changes with", item="FC80's population generator (one alteration per member, τ one-to-one)", mark="claim S4", named_by=A, standing=C,
         evidence="on FC80's own populations V4.8 moves nothing: a differing member there differs at an unseen pair only, so it survives and now's conjunct already holds"),
]

VARIANTS = [
    dict(id="V4.1", item="D16.XV (the rule on Expl)", implemented="as written", inventions=["S108-4-I1", "S108-4-I9"]),
    dict(id="V4.2", item="D16.XV (the rule on Expl)", implemented="as written", inventions=["S108-4-I2", "S108-4-I9"]),
    dict(id="V4.3", item="D16.XV ((Suff) and being an explanation)", implemented="nearest statable (read at the holding)", inventions=["S108-4-I3", "S108-4-I9"]),
    dict(id="V4.4", item="D16.XV (Uses)", implemented="as written", inventions=["S108-4-I4"]),
    dict(id="V4.5", item="D16.XV ((Nec)); L538", implemented="nearest statable (a searched class of transports)", inventions=["S108-4-I5"]),
    dict(id="V4.6", item="D16.4 (𝔈_Θ)", implemented="nearest statable (on the witnesses built)", inventions=["S108-4-I6"]),
    dict(id="V4.7", item="D16.3 (Enable)", implemented="not as written: the program has no Enable; a toy", inventions=["S108-4-I7"]),
    dict(id="V4.8", item="D12.9 (Underdet); (Prov)(i)", implemented="as written", inventions=["S108-4-I8"]),
]


def main():
    counts = {}
    for e in EDGES:
        k = ("reply / " if e["named_by"] == R else "added / ") + e["standing"]
        counts[k] = counts.get(k, 0) + 1
    out = dict(about="S108 Part A, section 4: the edges each variant of the reply for section 4 shows, marked computed / contradicted / "
                     "not settled by computation, and the edges the computation adds (rule 5). Nothing here changes the theory (rule 11).",
               file="results/S108 Part A - section 4 - variants computed.md", variants=VARIANTS, counts=counts, edges=EDGES)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    for v in ("V4.1", "V4.2", "V4.3", "V4.4", "V4.5", "V4.6", "V4.7", "V4.8"):
        print("\n### %s\n" % v)
        print("| id | kind | item [mark] | named by | standing | evidence / what would settle it |")
        print("|---|---|---|---|---|---|")
        for e in EDGES:
            if e["variant"] != v:
                continue
            ev = e["evidence"] + (("; to settle: " + e["what_would_settle"]) if e.get("what_would_settle") else "")
            st = e["standing"] if e["named_by"] == R else "**added** (" + e["standing"] + ")"
            print("| %s | %s | %s [%s] | %s | %s | %s |" % (e["id"], e["kind"], e["item"], e["mark"], "reply" if e["named_by"] == R else "computation", st, ev))
    print("\nCounts: %s; %d rows." % ("; ".join("%s %d" % kv for kv in sorted(counts.items())), len(EDGES)))


if __name__ == "__main__":
    main()
