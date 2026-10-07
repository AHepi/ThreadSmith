# S108: Part A round 2 - tabulation of the replies, before any ruling

*By a fresh Opus 5.5 agent (rule 4 of `results/S108 Part A round 2 - how the replies will be read, written before sending.md`), which built nothing of Part A and read no reply of round 2 before this. Created at once and filled as it goes (lesson S28). Rules on nothing. "Candidate" or "explanation" for what the theory judges; "model" only for the program's folder (S43).*

## 0. Status

Complete, 28 September 2026. Nothing ruled; nothing implemented; no theory text, formal core, claim, program, round-1 file or program copy written (rule 11). Four replies, 41 variants (S1 10, S2 11, S3 10, S4 10); flags in §7, the parts of each share no variant answers in §8.

## 1. Before reading (rules 1, 2)

| check | state |
|---|---|
| rule 1: every call ended | run log: `s108r2_glm_loop: every pass ended; accepted 4 of 4 jobs`, `loop ended 2026-09-28T22:40:55Z`; the pid in `s108r2_glm_run.pid` (27908) has exited |
| rule 2: key in output | receipts, field `key_found_in_output_and_replaced`: 0, 0, 0, 0 (only this field and the next were read from the receipts) |
| rule 2: sandbox unchanged | receipts, `sandbox_unchanged`: True ×4 (run log: 64 sandbox files each) |
| replies read (`.response.txt` only) | S1 `a3bd9ffd5e52e095878219b79344882a` (3,127 words); S2 `01c99d710fe76ecde5d8952b6a76ec00` (3,410); S3 `34a8e69fa03c3bd49e4df8326181ac8b` (2,658); S4 `3ffec2d215a91889337ced3e0577e918` (3,880); each pass 1, attempt 1, each ends END OF REPORT |
| not opened | reasoning files, stream files, guard logs, requests |
| marks used | the frozen set `.json` (30ca39e3…; the template's marks), sections by line (S1 L1–L164, S2 L165–L350, S3 L351–L484, S4 L485–L632) and the rule's list of middle definitions per section; the shares from the four briefs' §5 (md5s as the rule gives) |

Every "after" in every reply is marked **not run** by the reply. A "before" marked run cites a claim of the suite (`python3 -m model.run --claim …`); nothing below checks that the cited result line is what the program prints (rule 5's work). Everything below is the replies' claims (rule 3).

## 2. The variants (rule 4: section, id, item or reading varied, old and new, kind, share part)

Marks in brackets are the template's (frozen set `.json`). Old = the formal core after round 4 (d6e6ec62…) or the text, or round 1's reading as its files state it; checked against each reply's "old" (they agree unless a note says otherwise). New = the reply's, as written. "Share" = which part of the section's share (the brief's §5) the reply says it answers. "Departs" = the owner's decision the reply's own row names.

### Section 1 (Part 0 to Part III): 10 variants

| id | item or reading varied [mark] | kind | share | old | new | departs (reply) |
|---|---|---|---|---|---|---|
| R2V1.1 | S108-1-I5 (C2's reading), on D3.4 [S1] under V1.5's conjunct | other choice of a reading | 1 (I5) | a question built with no recorded contract history has ρ_p = declared; V1.5: Acc ∧ ρ_p ∈ {selected, constructed} | ρ_p a recorded field of each question (D3.1 [FROZEN] already has the slot); V1.5's conjunct kept (D3.4.v1); values set per case: selected, constructed, declared | none |
| R2V1.2 | D3.4 [S1] with L155.s6 [FROZEN]: a found question with its trace | other (an encoding) | 3 (e1.37) | D3.4: constructed :⟺ C results from an episode with a construction trace; Found(p) requires ρ_p = constructed | constructed :⟺ ∃h′ [Rec_h′(C→C′) = constructed ∧ Prepares(h′, C′ as a content)]; Found(p′) :⟺ ρ_p′ = constructed (D3.4.v2) | none |
| R2V1.3 | the bridge's brief (S41 Q6, FC84.new1 (a1)), ρ_p recorded | other choice of a reading (a case only) | 1, 3 (e1.38; C2's Q6 flag) | FC84.new1 (a1): no ρ_p for C_brief; D13.8's Episode asks a record at each change and reads no value of it | ρ(C_brief) = declared (second case: constructed); Episode and Con read the value: "a change in D13.8 (S3's) … not made here" | S41 Q6, S47 (under declared) |
| R2V1.4 | L15.s2 [S1] (a question can be found), through D3.4's Found | weaken | 2 (L15) | Found(p) requires ρ_p = constructed (D3.4; L155.s6 [FROZEN]) | Found(p) :⟺ ρ_p ∈ {selected, constructed} | none |
| R2V1.5 | L17.s1 [S1] (the conjecture's four) | delete | 2 (L17) | (i) organizations and admitted changes, (ii) transports tested by change-fidelity alone, (iii) provenance of transports and questions, (iv) physical realization; L17.n2: "an argument not using these four" | the four without (iii), read as D16.XV's "not using" set U := {(O), (Q), transports ∧ change-fidelity, Θ} | none |
| R2V1.6 | L11.s1 [S1] (the opening statement), read as naming (F1) ∧ (F2) | weaken | 2 (L11) | being an explanation: Account(ℰ) ∧ ¬Dec(t) (L17, L49, L61, L69 [S1]; D16.XV [S4]) | Expl(ℰ) :⟺ (A) ∧ Dependence ∧ NonVacuous ∧ ¬Dec(t) | none (blocks L23.s1) |
| R2V1.7 | L119.s1 [S1] (one kind on C); its formal statement is D4.2 [FROZEN] | swap | 2 (L119) | D4.2: j ~_C j′ :⟺ a bijection β: V_j → V_j′ with X_v = X_β(v) and L_j′(a,b) = β_*(L_j(a,b)) ∀(a,b) ∈ C (I10) | j ~_C j′ :⟺ V_j = V_j′ ∧ sig_C(j) = sig_C(j′) (footprints as ordered tuples; β dropped) | none (blocks D4.2) |
| R2V1.8 | L141.n3 [S1] (the query's codomain); D3.2 [FROZEN] states it | strengthen | 2 (L141) | Q(O,a,b;δ_O) ∈ Y_p ∪ {⊥}, Y_p free (D3.2) | Y_p := X_δD (⊥ as D3.2) | none |
| R2V1.9 | L159.s3 [S1] with D3.1 [FROZEN] (what a contract may hold) | strengthen | 2 (L159) | L159.s3: admitting a change is not a claim that it can be carried out; whether it can "does not by itself put a change in a contract or keep it out"; D3.1: C ⊆ A×B, (1,b0) ∈ C | Question(p) ⇒ ∀(a,b) ∈ C: Θ_admits(a); a C holding an unadmitted pair names no question | S25, S26–S27 |
| R2V1.10 | S108-1-I1 (C1's reading: ℰ_bv's relation at a ≠ 1) | other choice of a reading | 1 (I1) | (i) the one solution of D at (a,b); (ii) L_bv(1,b); both run in round 1 | (iii) L_bv(a,b) := ∪_{b′∈B} proj_{V_cbv} Sol_D(a,b′) | none |

### Section 2 (Part IV to Part VII): 11 variants

| id | item or reading varied [mark] | kind | share | old | new | departs (reply) |
|---|---|---|---|---|---|---|
| R2V2.1 | edit or boundary (C5's reading; the owner's change in the vane) | other choice of a reading | 1 (edit or boundary) | edit only (M13, I189) or boundary only (FC28.new2's D_vane) | a mixed encoding D_vane^mix: V = {W,P}, J = {cW, cP}, B = {b_still, b_north}, A = {1, setW1}; the wind a boundary of cW and an edit setW1; p_mix: Q_w on P, C = {(1,b_still),(1,b_north),(setW1,b_still)}; ℰ_mix = D with identity maps, Γ = {cW} (Inv-R2-1; in full in the reply) | none |
| R2V2.2 | D6.3's quantifier (I136) [S2], with (E) as it is and with V2.4 on | other choice of a reading | 1 (quantifier) | 'every' (the program's) | each of 'every', 'some', 'some-exempt', 'some-exempt-set'; (E) as it is / round 3's (E) | S44 (with V2.4 on, under the three non-'every' readings) |
| R2V2.3 | the hand-set histories (I90; P-S2-3), C7's | other choice of a reading | 1 (histories) | four histories set by hand | (a) provenance computed on chains (prov_fixed_points, as FC30.new1 (d)); (b) H = {(e,b0)} with a survival condition the transport fails | none |
| R2V2.4 | D12.3 [S2] with D12.4 [FROZEN] (the student's copy, inherited) | strengthen | 1 (histories: the student's copy) | D12.3: a holding reached by content-preserving transfers has prov(t,o′) := prov(t,o), part by part (D12.4: parts = each component with its counterpart binding; a binding newly built gets Con) | D12.3.v1: a holding reached by a copy of the carrier's whole content (relay or record of t as one content, D11.2) has prov(t,o′) := prov(t,o); D12.4's rule with parts := {t} (Inv-R2-3) | S41 Q2 |
| R2V2.5 | D6.9 [S2] (Relabeling) | strengthen | 2 (upstream) | Ans_p(a,b) = Ans_p(1,b0) at every b with (a,b) ∈ C, ⊥ = ⊥ (I26) | the same with Ans_p(1,b0) ≠ ⊥ (I26's registered other choice) | none |
| R2V2.6 | D11.2 [S2] (Content), second sentence | delete | 2 (upstream) | "A transport or a contract (D13.6, L590), a finite H ⊆ A × B, and the survival condition surv over 𝒯 (D12.1) are contents by L590's construction …; so Rep(o,x) and Held(o,x) for x ∈ {t, H, surv, cod t} are typed as D12.5 types Rep" (I170) | deleted | S41 Q2 |
| R2V2.7 | D5.7 [S2] (Faithful) | swap | 2 (upstream) | Faithful_C(t) := F1_C ∧ F2_C (L189, L245); QFid_C := A_C; Viol narrow (D12.7) | Faithful_C(t) := F1_C ∧ F2_C ∧ A_C; Viol := Viol⁺ | none named ("blocks a FROZEN item") |
| R2V2.8 | D6.7 [S2]: round 1's V1.6 formula, no added sentence (share part 4) | strengthen | 4 (V1.6's formula) | Acc(ℰ) :⟺ F1_C ∧ F2_C ∧ A_C ∧ Dependence ∧ NonVacuous | … ∧ ¬BadTarget(p) ∧ ¬BadReq(p), from D3.6 [S1] with a Desc per case (Inv-R2-2: phenomenon grain or target grain) | S44, S41 Q15 (phenomenon-grain Desc only) |
| R2V2.9 | D6.8 [S2] (the four conditions) | re-order (naming) | 2 (upstream) | four headings: Component fidelity = F1 ∧ F2; Question fidelity = A; Dependence; Non-vacuity | five: Component fidelity := (F1); Assembly := (F2); Question fidelity; Dependence; Non-vacuity; (E) unchanged | none |
| R2V2.10 | D12.7 [S2] (violation) | strengthen | 2 (other untouched) | Viol(t;a,b) :⟺ ¬(F1 ∧ F2eq) at (a,b); Viol⁺ adds (A) (I50) | Viol :⟺ ¬(F1 ∧ F2eq ∧ A) at (a,b) | none |
| R2V2.11 | new claims beside FC21 | other (claims) | 4 (e2.38, e2.39) | no claim separates D6.4 from V2.1 or V2.2 | FC21.v1: ∃ℰ: F1 ∧ F2 ∧ A ∧ NonVacuous ∧ Contrast(E;x) at some (a,b) ∈ C ∧ no ∅ ≠ G ⊆ Γ with Lost(E,G;x); FC21.v2: ∃ℰ meeting (E) with S_E,p = {{a},{b},{a,b}} on Γ = {a,b} | none |

### Section 3 (Part VIII to Part XII): 10 variants

| id | item or reading varied [mark] | kind | share | old | new | departs (reply) |
|---|---|---|---|---|---|---|
| R2V3.1 | S108-3-I2 and S108-3-I5 (C8's readings): CT (D12.2 [S2]) and ExplUse (D13.3 [S3]) | other choice of a reading | 1 (C8) | D12.2: CT(h′,t) :⟺ t held at an output of a construction trace; V3.4: ExplUse(o,c) :⟺ UsesClaim(o,'Acc(ℰ)') ∧ Acc(ℰ), ℰ on the candidate's own question or the widest contract | CT(h′,t) := some Build subhistory of h′ ∧ ExplUse(o,c) :⟺ UsesClaim(o,'Acc(ℰ′)') ∧ Acc(ℰ′), ℰ′ = (E, p′, t, Γ, δ′) on another question sharing t (R2-3-I1: p′ = p, δ′ = H) | none (C8's flag: see §3) |
| R2V3.2 | D13.8 [S3], the record's key (I174, "recorded, not chosen") | swap | 1 (C9) | Rec_h′(ρ_q(o′)) keyed by the new contract | keyed by the change q(o) → q(o′) | none |
| R2V3.3 | the trace's extent and the tag encoding against D13.3's tuple (I56, I162), record clause kept | other choice of a reading (two) | 1 (C9) | Held at o_t (the program's); round 1's tag counts were made with the record clause deleted (V3.5) | (a) Held read as a Θ tag at o1 before an unrecorded change, clause kept; (b) the extent := the whole subhistory, Held at o_t | none |
| R2V3.4 | D15.8 [S3], parts (I158; S108-3-I4) | swap | 1 (C10) | parts(t) := E_t's components with their bindings | parts(t) := the ports of E_t's codomain with their bindings; the stated construction's parts likewise; the clause kept | none |
| R2V3.5 | D15.8 [S3] / S108-3-I3 | strengthen | 1 (C10) | a history stating no construction: 𝒯 = {t : Θ admits t} (the program's) | no construction stated ⇒ 𝒯 = ∅ | none |
| R2V3.6 | I90 (Θ by hand) | other choice of a reading | 1 (histories) | hand-set histories | Dec(t) on every worked case from a chain history (prov_fixed_points, Rep computed, cut T′, H one occurring pair, a trace per occurrence) | none |
| R2V3.7 | D11.3 [S3] (History) | weaken | 2 (upstream) | ⪯_h := ≺_h* (I44 (b)) | ⪯_h := the reflexive closure of ≺_h (not transitive) | none |
| R2V3.8 | D9.2 [S3] (Argument) | strengthen | 2 (upstream) | "α may be one leaf, a premise alone, with no step" (S41 Q23) | every argument has at least one step (I88's reading) | S41 Q23 |
| R2V3.9 | D9.1 [S3] (Claims) | delete | 2 (upstream) | "The claims used here include 'Acc(ℰ)', 'Ans_p(a,b) = y', records of a test, and conditionals" | 'Ans_p(a,b) = y' dropped | none |
| R2V3.10 | D15.5 [S3] (Owned capability) | delete | 2 (other untouched) | Can :⟺ owned RetReal, or an owned, physically admitted, finite construction of such (I157) | the construction disjunct deleted | none |

### Section 4 (Part XIII to Part XVI): 10 variants

| id | item or reading varied [mark] | kind | share | old | new | departs (reply) |
|---|---|---|---|---|---|---|
| R2V4.1 | D16.XV [S4] with S108-4-I1, the pair jointly (Slot's quantifier is D6.3's, I136 [S2]) | other choice of a reading (two together) | 1 (I1) | C11 = V4.1: Expl :⟺ Acc ∧ ¬Dec ∧ ¬Slot_C, Slot under 'every', (Suff)'s antecedent kept | Slot under 'some' and (Suff), L536/L17: defeated for j ⟺ ∃ℰ [Acc ∧ ¬Dec ∧ ¬Slot_some(ℰ) ∧ ∃α ∈ X_j(Expl(ℰ)): Acc ∉ Uses(α)] | S45, S44 |
| R2V4.2 | D16.XV [S4] with S108-4-I2 | other choice of a reading | 1 (I2) | C12 = V4.2: Expl :⟺ Acc, (Suff) shape 'rule' | shape 'both': L17 and L536: defeated for j ⟺ ∃ℰ [Acc(ℰ) ∧ ∃α ∈ X_j(Expl(ℰ)): Acc ∉ Uses(α)]; L536's "with a transport whose provenance is not declared" deleted | S41 Q2 |
| R2V4.3 | D16.XV [S4] with S108-4-I3, a fifth reading | other choice of a reading | 1 (I3) | C13 = V4.3: ¬Dec ∧ (Sel ∨ CT), read (a) at the holding, (b) at a holding transferred from, (c) inherited | (e) at the content: (Sel ∨ CT)(t) :⟺ ∃o holding t's content (D11.2): Sel at o or a construction trace prepares t at o | none |
| R2V4.4 | I90 (the hand-set histories), C12's and C13's | code | 1 (histories) | hand-set histories | per worked case: o1 a source holding with Sel from the case's own named trial history (the pole's grids, E9's H0), else Dec; o2 a transfer of o1; fixed points under T′ (prov_fixed_points) | none |
| R2V4.5 | E9 [S4], the question's query | swap | 2 (E9) | occupancy reading per cell; ψ ∈ Aut(P), ψ[C] = C, Ans_p∘ψ = Ans_p | Q := Q_id, the set query reading (x1_3, x2_3); C, t1, S0, t0 unchanged (R2-4-I5) | none |
| R2V4.6 | L524.s2 [S4] | swap | 2 (Part XIV) | "Every claim is relative to them; none is a predicate that a case meets or fails" (them: ℓ, β, Ω, C, L524.s1) | a claim is a predicate of the case alone: P(ℰ) or P(M), the indices internal to P's content | none named (blocks L604.s1) |
| R2V4.7 | L522.s1 [S4], the declared inputs | delete | 2 (Part XIV) | the clause "for an assessor j, the inference forms j admits, the scope j declares and the premises j tentatively accepts and has not withdrawn (K2, Part IX)" | the clause struck; K2's premises no longer declared inputs | S28 |
| R2V4.8 | L526.s18 [S4], with D18.1 [S4] | delete | 2 (Part XIV) | "A representation defined only by its own construction, or an ownership and a capability each defined only by the other, has not supplied its place in the order; …" | deleted: D18.1 counts a definition as having supplied its place when its right-hand side cites itself or a cycle-mate | none named (contradicts L526.s17) |
| R2V4.9 | D12.9 [S4] and (Prov)(i) in D16.XV [S4], with L572.s2, L574.n4, L576.s1, L576.s4 [S4] | swap (co-variation) | 3 (e4.40) | Underdet :⟺ some t′ ∈ 𝒯 surviving on H has value_t′(a,b) ≠ value_t(a,b); the four sentences as written | round 1's V4.8 (surviving dropped) with the four sentences reworded (§7) | none |
| R2V4.10 | D18.2 [S4] | strengthen | 2, 3 (e4.22) | "… with Q, δ, Σ and every declared input carried along" | "… with Q, δ, Σ, every declared input, the transfer relation, the provenance records Rec_h′ and the construction traces carried along" (R2-4-I8: φ(Trace_h(o)) = Trace_φ(h)(φ(o)), likewise Rec_h′) | none |

Notes on the "old" column: R2V1.2 and R2V1.3 say records carry no provenance value "as now" ((f): "I165 (Rec_h′) extended to carry a provenance value"); the core's I165 reads "Rec_h′(ρ) is a record in h′ of ρ with its trace (D3.4)" (D13.8), and the program's records are booleans (the reply's case: `records = [False, 'constructed']`). R2V1.5's old is not D16.XV's: the core's "not using (E)" is Acc ∉ Uses(α), at the symbol (I196), with no set of four. R2V4.5's trace says the variant "states a second question, it does not replace the first", its row says Q := Q_id (a swap).

## 3. The traces (each reply's claim; every "after" not run)

"Run" = a claim of the suite the reply cites for the "before"; "hand" = worked by hand or taken from round 1's files. (E) = which candidates meet (E); Expl = which count as explanations (Account ∧ ¬Dec(t)).

### Section 1

| id | (E) | Expl | round 1's candidates and flags (the reply's claim) | cases: before / after |
|---|---|---|---|---|
| R2V1.1 | moves only through V1.5's conjunct: T with ρ_p selected or constructed, F with declared | as (E) | **C2**: its whole effect "an artifact of the missing field"; flags S44, S41 Q15 stand only where ρ_p is unrecorded or declared, go where recorded selected or constructed | M13 (FC22 (b)), the two-part sign (FC23.new2 (a)), p_δ's identity candidate (FC107): run / not run |
| R2V1.2 | no move | no move | – (settles e1.37) | FC84.new1 (b)'s chain, `records = [False, 'constructed']`, p′ with rho = 'constructed': not run |
| R2V1.3 | – (no candidate built) | with the brief declared and Episode reading ρ: Con at o2 T → F, CreateEx 1024 → 0 valuations; with constructed: unchanged | **C2**: its S41 Q6 flag stands exactly where the brief's ρ_p is declared | FC84.new1 (a1): run / not run |
| R2V1.4 | no move (Found read by no conjunct) | no move | – ((QF)'s cases and D16.4's 𝔓^adv grow) | FC84.new1 (a3) case (e), record `selected`: not run |
| R2V1.5 | no move | no move; (Suff)'s defeat set takes in every declared candidate with Acc (the student's copy, CT8's R2/R4, "FC-E 7"): "the conjecture is ruled out outright" | – ; "a constraint on (Suff)" | FC23.new2 (f): run / "derivable", not run |
| R2V1.6 | no move (Acc as it is) | grows by the candidates failing only (F1)/(F2): E_rev under τ′ on the production contract; the relabeling candidate with τ(1) ≠ 1; nothing drops | new candidate named **"C-new"**: question-relevant dependence with a non-declared link, no fidelity | FC27 (τ′), FC21 (d): run (conjuncts) / not run |
| R2V1.7 | no move (account reads no ~_C, FC30) | no move | – (FC05's antecedent rarer; Argument 2's exchange case loses its premise) | `one_kind` on a two-component D: not run |
| R2V1.8 | C_id "ceases to be a question": its candidates meet (E) of no question; port questions untouched | as (E) | – | FC28: run / not run |
| R2V1.9 | p_del names no question: the identity candidate on it (E) of no question; idle where Θ admits every edit | as (E) | – | the pole with c_L deleted (L315.s16), Θ by hand: not run (before also not run) |
| R2V1.10 | ℰ_bv under V1.1 + (iii) admitted, as under (i) | – | **C1**: no third reading changes its S44 flag (it rests on the two-part sign's drop under V1.1, computed in round 1); I1 decides only what C1 admits (ℰ_bv) | ℰ_bv on C1: not run |

### Section 2

| id | (E) | Expl | round 1's candidates and flags (the reply's claim) | cases: before / after |
|---|---|---|---|---|
| R2V2.1 | off: ℰ_mix meets every conjunct; under V2.3 on D_vane^mix: Acc stays T (witness at the edit pair) | as (E) | **C5**: its drop of the vane and the two-part sign is "an artifact of the pure boundary encoding"; flags S41 Q15, S44 on the boundary reading only; **C1** drops the sign under all three encodings | FC28.new2 (boundary), FC22 (b) (edit): run / D_vane^mix under V2.3: not run |
| R2V2.2 | (E) as it is: no move under any reading (FC23.new1 (h)); with V2.4 on: the two-part sign drops under the three non-'every' readings, ℰ_one under all four, M13 stays, pole C2/C3 drop under the three | as (E) | **C6, C11**: S45 flag under 'every', S44 added under the other three; "no other candidate of C1–C13 reads the quantifier" | FC23.new2: run; "all values already computed by the cited claims" |
| R2V2.3 | no move | (a) on chains C7's 28 of 28 shrinks to holdings with no earlier representation of t or cod t; the student's copy stays Dec; (b) every account survives its own H; a non-account stays Dec | **C7**: flag S41 Q2 stands, narrowed | FC30.new1 (d): run / ℰ_bad (M13 with L_cy(e,b0) altered): not run |
| R2V2.4 | no move | the student's declared formula becomes an explanation (prov inherited Con → Dec F); enters Def(L536) | **C13** reading (c) no longer idle; C12's, C7's flags unchanged | FC30.new1 (d): run / not run |
| R2V2.5 | no move ("no conjunct of Acc reads D6.9") | no move | – (FC21 (a2)'s coverage; L257.n3's antecedent) | a two-pair contract answering ⊥: not run |
| R2V2.6 | no move | on a history with one tried pair every account becomes Sel → an explanation, the student's copy included | – | FC77, FC97.new1: run / not run |
| R2V2.7 | no move | (i) a selected transport wrong in its answers on its own H is not Sel → Dec → stops (FC104.new1 (a)'s case Sel T → F); (ii) Rep harder → Sel easier where earlier representations exist | – | FC104.new1 (a), (b): run / not run |
| R2V2.8 | phenomenon-grain Desc: ℰ_two, ℰ_one, E_enc (the sign) and M13, E_enc (the vane) stop; the pole, the balances, the student's formula: no move; the bridge: not computable; target-grain Desc: 0 moves | as (E) | – ; departs S44, S41 Q15 at phenomenon grain | the Desc table, per case: not run |
| R2V2.9 | no move | no move | – (FC31 now five headings) | none |
| R2V2.10 | no move | no move (Dec unmoved) | – (Surp at a pair of H; SelResp there; FC104.new1 (b) "not as claimed") | FC104.new1 (b): run / not run |
| R2V2.11 | – | – | – (two suite claims; v1 holds under D6.4's negation and fails under D6.4; v2 holds under D6.4 and fails under V2.2) | witnesses from round 1's runs (MID; the L307 case): not run as claims |

### Section 3

| id | (E) | Expl | round 1's candidates and flags (the reply's claim) | cases: before / after |
|---|---|---|---|---|
| R2V3.1 | no move | a trace whose output uses Acc(ℰ′) on another question sharing t, with Acc(ℰ′) F: Con F, Dec T, stops; the pole's forward candidate (δ_E = L) drops when the claim reads δ′ = H | **C8**: its flag S41 Q2 "rests wholly on S108-3-I5's choice": none under the candidate's own question; stands under the widest contract or another question | FC90.new1 (a), (c): run / not run |
| R2V3.2 | no move | on re-entry chains (q = [C′, C, C], one record of ρ_C): episode lost → Con F, Dec T, stops | **C9**: gains re-entry chains; no flag either way | FC84.new1 (c): run / the three-occurrence chain: not run |
| R2V3.3 | no move | (a) tag at o1 before an unrecorded change, clause kept: Con F, Dec T, every Acc-T candidate on such a history stops; (b) Con F only where the trace spans o_s..o_t and the episode must hold an occurrence outside it | **C9**: round 1's tag row "an artefact of the deletion, not of the encoding"; new candidate **"C9′"**; no flag (the bridge keeps one contract) | FC84.new1 (c): run / `Hist(occ=["o1","o2"], …)`: not run |
| R2V3.4 | no move | t′ with an extra component on a stated port enters 𝒯: Sel T, Dec F, becomes an explanation; underdetermined pairs 0 → 1 | **C10**: its reach "does not need the deletion" | FC80 (a) format, the pole with k_x on port L: not run |
| R2V3.5 | no move | every candidate meeting (E) on a history stating no construction stops (expected 22 of 27 worked; 1,013 / 881 / 232 / 1,670 generated; CT8's R1–R5) | new candidate **"C10′"**, opposite to C10; no flag ("it declares more, which Q2 permits") | FC30.new1 (d): run / not run |
| R2V3.6 | no move | on chain histories C7's and C10's counts reproduce (0 moves); C9's tag counts do not (tag before an unrecorded change: Con F) | **C9**'s tag counts rest wholly on I90 | none built: expected, not run |
| R2V3.7 | no move | where the Held witness is ≥ 2 steps before the output: Con F, Dec T, stops; (EX) loses origin episodes ending ≥ 2 steps before e | – | o1 ≺ o2 ≺ o3, tag at o1: FC84.new1 (a1) (2-chain analogue): run / not run |
| R2V3.8 | no move | no move | – ; X_j loses every premise-only member; (Suff)/(Nec) defeat sets lose bare-acceptance entries; problems grow | FC72 (d): run / not run |
| R2V3.9 | no move | no move | – ; X_j('Ans_p(a,b) = y') = ∅; problems and defeat sets shrink | none; not run |
| R2V3.10 | no move | no move | – ; Deploy harder, (EX) smaller; (G) unmoved | none; not run |

### Section 4

| id | (E) | Expl | round 1's candidates and flags (the reply's claim) | cases: before / after |
|---|---|---|---|---|
| R2V4.1 | no move | under 'some': round 1's 'every' drops plus the two-part sign, the pole's forward candidate on C2 and C3, M5, E5's FC62 encoding; with (Suff) co-varied FC30.new1 (c) holds; (Suff) "as conjectured" fails of the owner's two-part sign | **C11**: S45 stands under all four quantifiers and both (Suff) shapes; S44 on exactly when the quantifier is not 'every'; the (Suff) shape moves no flag | ℰ_two, constructed, j = Assessor(["MP"], ["r", Imp("r", Not("Expl_two"))]): FC23.new2 (a), FC30.new1 (a): run / not run |
| R2V4.2 | no move | C12's admits unchanged (Expl := Acc); new under 'both': (Suff) itself is defeated by the owner's Q2 answer read as an argument | **C12**: flag S41 Q2 under 'rule', 'L17', 'both' | ℰ_dec with α = MP on r := "the link was declared, not found by trial or worked out" (R2-4-I2): FC30.new1 (a): run / not run |
| R2V4.3 | no move | 0 moves (a lemma: every chain-wide reading returns the inherited value) on 29 worked cases and 13,509 chain fixed points | **C13** a candidate only under (a) and (b); no flag under any of five readings | a two-holding chain, the pole's forward candidate: (a) run in round 1 / (e) not run |
| R2V4.4 | no move | changes the baseline: on chain-built histories the cases with a named trial history (the pole's forward, E9's t0, the lookups' tables) become explanations under the theory as it stands; the rest stay Dec | **C12** admits ℰ as before; **C13**(a) drops what now admits; "the separation … no longer rests on a history built to produce it" | the pole's production question, H = {(1,b1_45)}: FC30.new1 (d): run / not run |
| R2V4.5 | t1 still meets (E) (A at every pair) | unchanged for t1 and t1∘ψ on the occupancy question | – ; FC103.new1 (a), (c) fail; L630.n3's last clause and L630.s4 false of this contract | FC102.new1 (c), FC103.new1: run / not run |
| R2V4.6 | no move | no move | – ; (Suff)/(Nec) get one unindexed defeat set each; L604.s1 blocked | ℰ_fwd on C1 and C2 (FC102/FC26 "line of record"): run / not run |
| R2V4.7 | no move | "not statable" (the defeat conditions read X_j, whose inputs are struck) | – | j = Assessor(["MP"], ["r", Imp("r", Not("Expl_fwd"))]), FC30.new1 (a): run / not run |
| R2V4.8 | no move | no move | – ; DEP gains a cycle; FC32.new1 (b) fails as claimed; cut U usable again | FC32.new1 (b): run / not run |
| R2V4.9 | no move | no move ((Prov)(i) is a defeat condition) | – (e4.40) | the pole at θ = 45, 𝒯 = {t, t_ab,H}: FC80 (d): run; round 1's V4.8 values / the sentence checks: not run |
| R2V4.10 | no move | no move; V4.3 φ-invariant under D18.2.v1 | – (e4.22) | two histories differing only in a trace: not run; FC100: run (12,960/12,960) |

No reply marks any "after" as run. S1's baselines ran at `--scale 4 --time-cap 45`, S3's at `--scale 3`, S2's and S4's with `--brief` and no scale stated.

## 4. Settlements proposed for round 1's claimed-only edges (each a proposal until computed, rule 3)

| edge (round 1's map) | section | proposed by | proposal | outcome the reply expects | run |
|---|---|---|---|---|---|
| e1.02 (V1.1: D1.4 changes with L233.s1) | S1 | a reading | "imposing the constraints of λ(k)" read as imposing them on D, then projecting; the words cover I14 and V1.1 | contradicted; reclassify as constrains | no (a reading) |
| e1.03 (V1.1: D1.4 changes with L556.n2) | S1 | a reading on a computed base | the sentence's two signatures change value, not form; Argument 1's conclusion computed by FC17/FC18 (round 1, e1.04) | contradicted | no |
| e1.14 (V1.2: D2.1 blocks L103.s2) | S1 | a reading on a computed base | L103.s2 says a setting edit does not "add" an equation; V1.2 adds nothing; Sol_D's emptiness comes from altered components | contradicted (the other reading, "any juxtaposition with no solution", would keep it) | no |
| e1.36 (V1.5 blocks L155.s2, L155.s5) | S1 | "derivation" | V1.5's domain {selected, constructed} with L155.s2's "declared := neither" and L155.s5 jointly inconsistent | "stands by derivation"; nothing computable; would settle: the owner's yes or no on C2 | no |
| e1.37 (V1.5 constrains L155.s6, D3.1) | S1 | R2V1.2 | a found question with its trace encoded, ρ_p recorded | computed (stands) | no |
| e1.38 (V1.5 changes with D13.8 q(o)/Rec) | S1 | R2V1.3 | q(o) given ρ_p; Episode and Con under V1.5 (needs D13.8 to read the value, S3's) | computed (stands): with declared, Con at the output F, CreateEx 0 of 1024 | no |
| e1.39 (V1.5 changes with D16.4 𝔓^adv) | S1 | R2V1.1 | the questions with ρ_p recorded read as a finite 𝔈_Θ over the case scripts' (p, t, Γ) | computed (stands): declared-contract candidates out, selected and constructed kept | no |
| e1.40 (V1.5 changes with (QF) L544) | S1 | – | 'fails to capture', 'not creative' undefined (D16.XV's list) | not settled; would settle: definitions of the two terms (S4); R2V1.4 moves (QF)'s cases through Found | no |
| e1.45–e1.47 (V1.6: constrains L161.s1–s3 and D6.6; changes with (Suff), (Nec), FC106; moves being an explanation) | S2 | R2V2.8 | Acc with ¬BadTarget ∧ ¬BadReq, Desc per case | the reply marks all three "not" settled; its trace: e1.45 constrains (the variant adds, it does not replace), e1.46 changes with (defeat sets lose every ℰ on a defective p), e1.47 moves (E) and Expl at phenomenon-grain Desc and nothing at target grain | no |
| e2.03 (V2.2 blocks L311.s2) | S2 | a symbolic case (Inv-R2-7) | Γ = {d_n : n ∈ ℕ}, d_n := \|x\| ≤ 1/n, S := {W : W unbounded}: under V2.2 S = ∅, no route | computed (blocks) | no |
| e2.26 (V2.2 blocks L313.n3) | S2 | the same case | with S = ∅ no block is critical in any route | computed (blocks) | no |
| e2.06c (V2.3 blocks L329.s3, E2; L331.s2) | S2 | the balances as a question with a candidate (Inv-R2-5) | D_bal over a small finite field, C = {1}×B, Q_w on d, ℰ_bal = D, Γ = {cd}: Acc T off, F under V2.3 | computed under the strict reading of "account" (meets (E)); no block under the loose reading; E2 itself reads no (E) | no |
| e2.07 (V2.3 changes with D3.3) | S2 | composition | section 1's V1.4 run with V2.3 on C_id | computed (changes with stands): L325.n6's "faithful under the identification contract" loses its referent | no |
| e2.09 (V2.4 blocks — S45) | S2 | – | the owner's yes or no (S52) | noted only | – |
| e2.11b (V2.4 changes with (Nec)) | S2 | a computation | (Nec)'s defeat set with ℰ = E_enc on C1: exposure reads faithfulness of t, not (E) | contradicted | no |
| e2.16c (V2.6 moves the (Nec) attack route through ETV) | S2 | an argument encoded | premise ETV_j(ℰ;p), conclusion ¬Expl(ℰ): can serve (Suff)'s defeat set, never (Nec)'s | contradicted; keep as "independent of" for (Nec) | no |
| e2.19 (V2.7 changes with D8.6) | S2 | an argument encoded | α := one MP step on {record ConfCl(ℰ,χ;a,b), (ConfCl ∧ (a,b) ∈ C ∧ χ) ⇒ ¬Acc(ℰ)}; round 1's V2.7 case | computed (changes with): under V2.7 ConfCl F, α not constructible | no |
| e2.33 (V2.7 changes with L317.n8 / D10.6) | S2 | the same α | on round 1's 23 generated (candidate, pair) losing ConfCl under V2.7 (20 at a pair of C) | computed (changes with) | no |
| e2.38, e2.39 (the suite's blind spots) | S2 | R2V2.11 | FC21.v1, FC21.v2 as suite claims | separate D6.4 from V2.1 (v1) and V2.2 (v2) | no |
| e3.30b (V3.6 → Sel → Dec → FC80) | S3 | FC80's generator extended | a stated construction per population; (a), (a′), (d′) recomputed under none and under R2V3.4 | computed (stands) | no |
| e3.34b (V3.7 → UsesReason, D9.11) | S3 | circuits with objections | circuits of ≤ 4 occurrences each given a represented objection with role bindings onto an active route; UsesReason on the 1,436 routes that did no work (FC75 (a)) | computed (stands): UsesReason T under V3.7, F under none | no |
| e3.37b (V3.8 changes with L628, D18.1's DEP) | S3 | – | the owner's yes or no (S47 with S41 Q6) | noted only | – |
| e4.22 (V4.3: D16.XV constrains D18.2) | S4 | R2V4.10 | two histories differing only in a trace, φ allowed by D18.2 as written; V4.3(a) on both; then D18.2.v1 on all chains | computed "in the strong direction": V4.3 not φ-invariant under D18.2 as written; invariant under D18.2.v1; FC100 unchanged | no |
| e4.40 (V4.8 changes with L572.s2, L574.n4, L576.s1, L576.s4) | S4 | R2V4.9 | the four sentences checked against the pole case beside Underdet and (Prov)(i) | computed, refined: changes with for L572.s2 and L576.s4; for L574.n4 "the derivation, not the sentence"; L576.s1 unchanged (under R2-4-I7) | no (the case's values are round 1's) |

Of the 22 claimed-only edges the shares name (S1 8, S2 9, S3 3, S4 2), every one has a proposal or a note: expected computed 13 (e1.37, e1.38, e1.39, e2.03, e2.26, e2.06c (strict reading only), e2.07, e2.19, e2.33, e3.30b, e3.34b, e4.22, e4.40), expected contradicted 5 (e1.02, e1.03, e1.14, e2.11b, e2.16c), "stands by derivation" 1 (e1.36), not settled 1 (e1.40), the owner's 2 (e2.09, e3.37b). Of the 13, three rest on a change another section would make or a reading the reply chooses: e1.38 (D13.8 [S3] reading ρ's value), e2.06c (Inv-R2-5), e4.40 (R2-4-I7). The share of section 2 also gives it e1.45–e1.47 (proposed, the reply says not settled) and e2.38, e2.39 (claims proposed).

## 5. The edges, as each reply names them (its (d); marks are the template's; a reply's mark that differs is noted)

Rows per reply (blocks / constrains / changes with / moves / "independent of", a kind the replies add): S1 5 / 5 / 9 / 4 / 2 = 25; S2 2 / 6 / 11 / 5 / 3 = 27; S3 1 / 5 / 10 / 6 / 0 = 22; S4 4 / 9 / 6 / 2 / 2 = 23; all 12 / 25 / 36 / 17 / 7 = 97. "Settled" is the reply's own word: almost every row is "not run", "not" or "–"; the exceptions are named.

| id | blocks | constrains | changes with | moves | independent of |
|---|---|---|---|---|---|
| R2V1.1 | – | D3.1 [FROZEN], D3.4 [S1] | e1.39's 𝔈_Θ (D16.4 [S4]) | (E) as C2 has it; flags S44, S41 Q15 go under recorded ρ_p | – |
| R2V1.2 | – | L155.s6, D3.1 [FROZEN] | E8 [FROZEN] | – | – |
| R2V1.3 | – | – | D13.8 Rec [S3] | Expl on the bridge's episode (Con, Build, CreateEx; the reply's "D13.6/D14.7, S3": D13.6 is [FROZEN], D14.7 [S3]) | – |
| R2V1.4 | L155.s6 [FROZEN] ("by wording") | – | (QF) L544 [S4], D16.4 𝔓^adv [S4], D13.8 [S3] | – | – |
| R2V1.5 | – | L17.n2 [S1] ("by wording") | D16.XV [S4], (Suff), (Nec) | – | – |
| R2V1.6 | L23.s1 [S1] ("by wording") | – | L49.n3, L69.n3 [S1], D16.XV [S4], (Suff), (Nec) | Expl (E_rev under τ′ on C1 and the relabeling candidate in) | – |
| R2V1.7 | D4.2 [FROZEN] ("by wording") | – | L119.n4, L119.n5 [S1], Argument 2's claim [S4], L317.s13 [S2], FC03–FC05 | – | (E), Expl ("computed (round 1, FC30)") |
| R2V1.8 | L151.n3, L151.s4 [S1] ("by wording") | D3.2 [FROZEN] ("by wording") | D3.3 [S1], E2 [S2], E4 (the reply: "S2"; the template: [FROZEN]), C_id's reading (E1 [S2]) | – | – |
| R2V1.9 | L75.s3, L75.s7 [S1] ("by wording") | – | L275.s2, L315.s16 [S2] | which questions exist (p_del names nothing) | – |
| R2V1.10 | – | S108-1-I1's family | – | – | C1's flag S44 ("computed (round 1)" + the (iii) case not run) |
| R2V2.1 | – | FC28.new2 ("computed (run)") | D3.3 [S1] | C5's flags ("computed (cited runs)") | – |
| R2V2.2 | – | – | C6's and C11's flags ("computed (run)") | – | (E) ("computed (run)", FC23.new1 (h)) |
| R2V2.3 | – | L195.n4 [S2] / D12.1's exclusion clause ("computed (run)") | Dec, Expl ("computed (run)") | – | – |
| R2V2.4 | – | L211.s4 [S2], D12.4 [FROZEN] | D13.3 [S3], FC30.new1 (d), (f) | Dec, Expl, (Suff) | – |
| R2V2.5 | – | L257.n3 [S2] | FC21 (a2) | – | (E), Expl ("computed": no conjunct reads D6.9) |
| R2V2.6 | FC97.new1 (a claim) | – | E8 [FROZEN], L590.s1–s2 [S4] ("the construction sentence is deleted with the typing") | Dec, Expl (flag S41 Q2) | – |
| R2V2.7 | L189.s2 [FROZEN] | – | D12.1, D12.7, L220.n1 [S2]; FC104.new1 (b), FC104 ("partly (run before)") | Dec | – |
| R2V2.8 | – | L161.s1–s3 [FROZEN], D6.6 [FROZEN], D3.6 [S1] (e1.45) | (Suff), (Nec), FC106, D3.6 [S1] (e1.46) | (E), Expl (e1.47) | – |
| R2V2.9 | – | – | L231.s3 [S2], FC31 | – | (E), Expl ("computed (by construction)") |
| R2V2.10 | – | L220.n1, L221.n1, L223.s2–s3 [S2] | D12.8, D12.1 [S2] | – | – |
| R2V2.11 | – | – | e2.38, e2.39 | – | – |
| R2V3.1 | L403.s3 [FROZEN] ("computed (round 1)", inherited from V3.4, e3.19) | – | D12.2 [S2], D13.3 [S3] | Dec, Expl | – |
| R2V3.2 | – | – | L55.n3 [S1], FC84.new2 | Dec, Expl | – |
| R2V3.3 | – | – | D12.2 [S2] (Held's reading), D13.3's tuple [S3] | Dec, Expl | – |
| R2V3.4 | – | D12.1 [S2] | L481.s3 [S3] | Dec, Expl, D12.9 (the reply: "[S2]"; the template: [S4]) | – |
| R2V3.5 | – | L195.s1 [FROZEN] ("claimed only") | L481.s3 [S3] | – | – |
| R2V3.6 | – | FC30 | I90 and C7/C9/C10's counts | – | – |
| R2V3.7 | – | – | D14.7 [S3], D12.2 [S2] | Dec, Expl | – |
| R2V3.8 | – | – | D9.6, D9.7, L397.s16 [S3] | (Suff), (Nec), D10.1 [FROZEN] | – |
| R2V3.9 | – | L397.s5 [FROZEN] | D9.8, D10.3 [S2] | – | – |
| R2V3.10 | – | D15.7 [FROZEN] | D13.1, D13.2 [FROZEN], D14.7 [S3], D16.1 (the reply: "[S4]"; the template: [FROZEN]) | – | – |
| R2V4.1 | – | (Suff)'s shape (D16.XV [S4]; L61 [S1], L536 [S4]) | D6.3's quantifier I136 [S2] ("computed", FC23.new2 and round 1); L17.n2, L49.n3, L61.n2, L69.n3 [S1] | – | – |
| R2V4.2 | (Suff) as L536 states it [S4] | FC30.new1, FC23.new2 ("computed (round 1)") | – | – | – |
| R2V4.3 | – | D12.4 [FROZEN] ("computed (round 1 chains)") | – | – | – |
| R2V4.4 | – | I90 | – | – | – |
| R2V4.5 | – | Argument 2, L562.s3 [S4] | – | FC103.new1; L630.n3, L630.s4, L630.s5 [S4] | (E), Expl (expected) |
| R2V4.6 | L604.s1 [FROZEN] | – | L606.s2–s4, L608.s1–s2 [S4] | (Suff), (Nec) | – |
| R2V4.7 | D16.XV's shapes and note [S4] | L522.s2 [S4] | – | – | – |
| R2V4.8 | L526.s17 [S4] | FC32.new1 (b), FC98 (c) | L598.s2, L596.s1 [S4] | – | – |
| R2V4.9 | – | L574.n4, L574.s5 [S4] | L572.s2, L576.s4 [S4] | – | (E), Expl ("computed (round 1)") |
| R2V4.10 | – | D18.2 [S4], FC100 ("FC100 run (holds)") | D0.2's Rec_h′ (I165) [S1] | – | – |

Blocks naming a FROZEN item: 5 (R2V1.4 L155.s6; R2V1.7 D4.2; R2V2.7 L189.s2; R2V3.1 L403.s3, inherited; R2V4.6 L604.s1). The S4 reply's closing line says "No FROZEN item is blocked by R2V4.1–R2V4.5, R2V4.8–R2V4.10 except as listed (L604.s1 by R2V4.6)"; its R2V4.7 row blocks D16.XV [S4], not FROZEN. The S3 reply: "No blocks of a FROZEN item computed this round".

## 6. The owner's decisions each variant names, and the inventions it rests on

| id | decisions named (the reply's row or trace) | inventions (the reply's (f); "other" = the other choices it names) |
|---|---|---|
| R2V1.1 | flags of C2: S44, S41 Q15 (go under recorded ρ_p) | I127 with ρ_p supplied per question; other: unrecorded ⇒ declared (S108-1-I5); unrecorded ⇒ unknown, case left out |
| R2V1.2 | – | I165 "extended to carry a provenance value" (see §2's note); other: records carry none; the trace's extent |
| R2V1.3 | departs S41 Q6, S47 (under declared) | as R2V1.2; I90; I191/I192 (the bridge's labels) |
| R2V1.4 | – | I127 as R2V1.1 |
| R2V1.5 | – | "not using these four" read as one set U; other: U fixed per defeat shape "as D16.XV has it" |
| R2V1.6 | – | L11.s1's "held to a target by a transport that is tested…" read as naming (F1) ∧ (F2); other: Faithful_C alone; change-fidelity's extent only |
| R2V1.7 | – | I10 dropped; other: kept (D4.2); a bijection up to port-translation |
| R2V1.8 | – | I20, I21 kept, Y_p fixed; other: Y_p free (D3.2); Y_p free, ⊥ excluded |
| R2V1.9 | departs S25 ("a pretty big hole"), S26–S27 | I90; "admitted" read as Θ-admitted; other: unadmitted pairs dropped from C; Θ read at a grain |
| R2V1.10 | C1's flag S44 | S108-1-I1's family (i)–(iii); a fourth (the answer port's value alone) "excluded by S45's keeping of Slot as defined content" |
| R2V2.1 | C5's flags S41 Q15, S44 | Inv-R2-1 (the mixed encoding); other: edit only (M13, I189); boundary only (FC28.new2) |
| R2V2.2 | with V2.4 on: S44 (three readings); C6, C11: S45 | – (I136's four readings) |
| R2V2.3 | C7: S41 Q2 (stands, narrowed) | Inv-R2-4 (prov_fixed_points chains for the worked cases); other: hand-set (P-S2-3); no history |
| R2V2.4 | departs S41 Q2 ("No, not if just declared") | Inv-R2-3 (D12.4's parts := {t}); other: component with binding (as now, FC30.new1 (f)); the component alone (K3) |
| R2V2.5 | – | Inv-R2-6 (I26's '≠ ⊥' re-taken); other: ⊥ = ⊥ |
| R2V2.6 | departs S41 Q2 | – |
| R2V2.7 | none named | – |
| R2V2.8 | departs S44, S41 Q15 (phenomenon grain only) | Inv-R2-2 (Desc per case at phenomenon or target grain, I76); other: any grain between |
| R2V2.9, R2V2.10, R2V2.11 | – | – |
| e2.03, e2.26, e2.06c (proposals) | – | Inv-R2-7 (L311's set system given symbolically); Inv-R2-5 (L331.s2's "account" read strictly) |
| R2V3.1 | C8: S41 Q2 (rests on S108-3-I5) | R2-3-I1 (p′ := p, δ′ = H); other: another Γ; another query port; the widest contract |
| R2V3.2 | – | R2-3-I2 (one record, of ρ_C); other: keyed both ways; a record per change |
| R2V3.3 | "none found" (S41 Q6's bridge unaffected) | R2-3-I3 (one tag, at o1, of cod t); other: a tag at every occurrence before the change; Held at o_t |
| R2V3.4 | – | R2-3-I4 (parts := codomain ports with bindings); other: parts as edits; components with bindings (I158) |
| R2V3.5 | "no flag (it declares more, which Q2 permits)" | R2-3-I5 (no construction ⇒ 𝒯 = ∅); other: admitted alone (S108-3-I3); the case left out |
| R2V3.6 | – | R2-3-I6 (H one occurring pair; a trace per occurrence; least fixed point under T′); other: H = ∅; all pairs; every fixed point must agree |
| R2V3.7 | – | R2-3-I7 (⪯ := reflexive closure); other: ≺* (now) |
| R2V3.8 | departs S41 Q23 ("Yes, it's an argument") | – (I88) |
| R2V3.9 | – | R2-3-I8 (records of a test kept as claims); other: dropped too; answers kept, tests dropped |
| R2V3.10 | S25–S27 "respected" | – |
| R2V4.1 | departs S45, S44 | R2-4-I1 (the pair as one variant); other: each alone; 'some-exempt', 'some-exempt-set' in the pair ("same expected pattern") |
| R2V4.2 | departs S41 Q2; S23 (r as "reasons why this and not that") | R2-4-I2 (the owner's Q2 answer as an argument r); other: r a bare record (round 1's α); shapes 'rule', 'L17' |
| R2V4.3 | – | R2-4-I3 (content of a holding := D11.2's Content); other: (a)–(d) |
| R2V4.4 | – | R2-4-I4 (o1's Sel from the case's own trial history); other: o1 always Con; three holdings; the source inside β or outside |
| R2V4.5 | – | R2-4-I5 (Q_id := the set query); other: a fibre query on identity; the swap excluded from C |
| R2V4.6 | none named | R2-4-I6 (P unindexed); other: the index internalized as a conjunct ("blocks nothing") |
| R2V4.7 | departs S28 ("That 'ruling out' is a choice that was made.") | – |
| R2V4.8 | none named | – |
| R2V4.9 | "none (V4.8's own departures: none computed)" | R2-4-I7 (the sentences read at their own wording); other: L576.s1's "alternative" as "surviving alternative" |
| R2V4.10 | – | R2-4-I8 ("carried along" := φ(Trace_h(o)) = Trace_φ(h)(φ(o)); likewise Rec_h′, the transfer relation); other: the transfer relation only; all of Θ's interpretation |

Departures named in the replies' own rows: S1 2 (R2V1.3, R2V1.9), S2 4 (R2V2.2 with V2.4 on, R2V2.4, R2V2.6, R2V2.8), S3 1 (R2V3.8), S4 3 (R2V4.1, R2V4.2, R2V4.7): 10. New inventions with an id: S2 7 (Inv-R2-1 to 7), S3 8 (R2-3-I1 to I8), S4 8 (R2-4-I1 to I8); S1 names its choices by the existing I-numbers and round 1's S108-1-In, with no new ids.

## 7. Flags (rule 4)

As in round 1's tabulation: "as written" = the variant names, among the items it varies, an item marked FROZEN or of another section; "in effect" = its statement is on its own item but its formula rewrites what an item of another mark states, or its computed effect needs such an item changed. Rule 4: recorded, not implemented; for the orchestrator to decide. "Possible" marks a case this agent could not place on either side.

| id | out of scope | repeats a round-1 variant | adds prose (S40) | moves where values are placed | why, one line |
|---|---|---|---|---|---|
| R2V1.2 | possible, in effect: L155.s6 [FROZEN] | no | no | no | Found(p′) :⟺ ρ_p′ = constructed where D3.4 [S1] and L155.s6 write "requires" (⇒); the reply calls it an encoding |
| R2V1.3 | in effect: D13.8 [S3] | no | no | no | its trace (Con T → F, CreateEx 1024 → 0) needs Episode and Con to read ρ's value, "a change in D13.8 (S3's) … not made here" |
| R2V1.4 | in effect: L155.s6 [FROZEN] | no | no | no | its formula rewrites what L155.s6 states (found requires constructed); the reply's own edge: blocks |
| R2V1.5 | in effect: D16.XV [S4] | no | no | no | its formula is a set U read as D16.XV's; the reply's own edge: changes with D16.XV |
| R2V1.7 | in effect: D4.2 [FROZEN] | no | no | no | the new ~_C replaces D4.2's definition (I10 dropped); the reply's own edge: blocks D4.2 |
| R2V1.8 | possible, in effect: D3.2 [FROZEN]; E4 [FROZEN] | no | no | no | fixes Y_p, which D3.2 leaves free (the reply: "constrains", "inside what D3.2 allows"); E4 would carry no question (the reply marks E4 "S2") |
| R2V1.9 | as written: D3.1 [FROZEN] | no | no | no | the row names "L159.s3 / D3.1"; the formula adds a condition to Question(p) |
| R2V2.4 | possible, in effect: D12.4 [FROZEN] | no | no | no | parts := {t} for a whole-content copy, where D12.4 fixes parts as components with their bindings; the reply: "constrains … D12.4's parts rule is its lever" |
| R2V2.7 | in effect: L189.s2 [FROZEN] | no | no | no | Faithful := F1 ∧ F2 ∧ A where L189.s2 names component and global fidelity only; the reply: "by the template's rule it is not a reading of the frozen words" |
| R2V4.1 | no (the share gives S4 the pair with D6.3's quantifier) | **in part**: being an explanation under V4.1 with 'some' was computed by round 1 on every case (its section 4 file §3–§5); new: the pair with (Suff) co-varied under 'some' (round 1 co-varied the suite under 'every') | no | no | the reply's own (f): "round 1 computed 'every' co-varied; 'some' with (Suff) kept on cases only" |
| R2V4.2 | no | **in part**: V4.2 under 'both' was computed on the suite by round 1 (its §7: FC30.new1 (a), (d), (e) not as claimed, (b) holds, (c) fails by construction); new: the case with Q2's answer as an argument (R2-4-I2) | no | no | the reply cites "round 1, suite" for the shapes |
| R2V4.9 | no | **yes, its formula**: round 1's V4.8 (Underdet without surv; (Prov)(i)'s middle conjunct); new: the four sentences read against it (e4.40) | **yes**: the four co-varied sentences are given as reworded prose ("…at which some t′ ∈ 𝒯 has a different value…", "…wherever its population admits an alternative member…", …), not as formal statements (the brief: "a variant of a sentence is its formal statement, not a rewording") | no | the share asks only e4.40's settlement |

No other variant names or rewrites a FROZEN item or another section's item; none other repeats a round-1 variant or adds prose; none varies the appraisal relation 𝒩 (L518), the aims O and P or a weighting (L522.s1's other clauses; R2V4.7 strikes only K2's clause), or makes (E) or being an explanation read one of them. R2V4.6's indices are ℓ, β, Ω and C (L524.s1), not values.

Not flags (given by the shares, or already round 1's): R2V1.1 is V1.5's conjunct under S108-1-I5's other choice; R2V2.8 is V1.6's formula as the orchestrator's decision 3 sends it; R2V3.1 is V3.4's formula under S108-3-I2 and I5's other choices, and reads D12.2 [S2]'s CT, which the share hands to S3; R2V2.2's values are, by the reply's own words, "already computed by the cited claims" (FC23.new2; round 1's C6); R2V1.10 and R2V4.3 take a further reading of round 1's own inventions.

Further notes, not flags:

- **Blocks a FROZEN item, by the reply's own edge** (the template: "a variant of the definition must still be a reading of the frozen words"): R2V3.1 (L403.s3, inherited from V3.4), R2V4.6 (L604.s1); and the flagged R2V1.4, R2V1.7, R2V2.7.
- **Names a FROZEN item as "changes with" or "moves"**: R2V1.2 (E8), R2V2.6 (E8), R2V3.10 (D13.1, D13.2; and D16.1, marked "[S4]" by the reply), R2V3.8 (D10.1, moves), R2V1.8 (E4, marked "S2").
- **Sentences co-varied, new form not given** (S40 wants a deletion or the formal statement): R2V1.5 (L17.n2), R2V1.6 (L49.n3, L69.n3), R2V1.7 (L119.n4, L119.n5), R2V2.9 (L231.s3's "four"), R2V2.10 (L220.n1, L221.n1, L223.s2–s3), R2V3.4 and R2V3.5 (L481.s3), R2V4.5 (L630.n3, L630.s4, L630.s5), R2V4.6 (L606.s2–s4, L608.s1–s2), R2V4.8 (L526.s17, L598.s2, L596.s1); all middle, each of its own section except R2V1.6's D16.XV [S4]. R2V2.9 names a new heading, "Assembly", for (F2).
- **Another section's item as "changes with"** (edges, not flags): R2V1.1, R2V1.4 (D16.4, L544 [S4]; D13.8 [S3]), R2V1.6 (D16.XV [S4]), R2V1.7 (L317.s13 [S2]; Argument 2 [S4]), R2V1.8 (E1, E2 [S2]), R2V1.9 (L275.s2, L315.s16 [S2]), R2V2.1 (D3.3 [S1]), R2V2.4 (D13.3 [S3]), R2V2.6 (L590.s1–s2 [S4], "deleted with the typing"), R2V3.2 (L55.n3 [S1]), R2V3.1, R2V3.3, R2V3.7 (D12.2 [S2]), R2V3.9 (D9.8, D10.3 [S2]), R2V3.10 (D16.1, the reply's "[S4]"), R2V4.1 (L17.n2, L49.n3, L61.n2, L69.n3 [S1]; I136 [S2]), R2V4.10 (D0.2's Rec_h′ [S1]).
- **Marks that differ from the template's**: E4 (the S1 reply "S2"; [FROZEN]); D13.6 (the S1 reply "S3"; [FROZEN]); D12.9 (the S3 reply "[S2]"; [S4]); D16.1 (the S3 reply "[S4]"; [FROZEN]).

## 8. The parts of each share no variant answers (rule 4), with the reply's own reason (its (e)) where it gives one

"Answered" = a variant or a proposal addresses it (§2, §4); nothing here says the answer holds.

| section | share part | answered by | not answered | the reply's reason |
|---|---|---|---|---|
| S1 | 1: S108-1-I5 under selected or constructed on the owner's cases; a found question with its trace; the bridge's brief; C2's flags | R2V1.1, R2V1.2, R2V1.3 | – | – |
| S1 | 1: S108-1-I1, a third reading | R2V1.10 | – | – |
| S1 | 2: untouched middle sentences, "above all" L11, L13, L15, L17, L119, L141, L151, L155, L159 | L11.s1 (R2V1.6), L15.s2 (R2V1.4), L17.s1 (R2V1.5), L119.s1 (R2V1.7), L141.n3 (R2V1.8), L159.s3 (R2V1.9); L155 only through D3.4 and the FROZEN L155.s6 (R2V1.2, R2V1.4) | **L13** (s1–s7); **L151** (none varied; L151.n3, L151.s4 only as blocked by R2V1.8); L141.s1; L159.s4–s7; L155's middle sentences (s1–s5) as varied items; the other ~120 middle sentences of S1 | L13: "their maths is D12.1–D12.3 (S2)"; L141.s1: "no maths of its own"; L151.s1/.s5/.s7: reached by V1.4 or living in Parts VII/XI; L159.s4–s7: D3.5, D3.7 FROZEN and V1.7 ruled to Part B; the rest: "their formal statements are the negations the named claims already test" |
| S1 | 2: D4.6 (the one middle definition round 1 did not vary; the share says "none untouched") | – | D4.6 | "a direct D4.6 variant would move only the families" |
| S1 | 3: e1.02, e1.03, e1.14, e1.36–e1.40 | all eight (§4) | – (e1.36 and e1.40 left not computable) | – |
| S2 | 1: edit or boundary, with a mixed reading | R2V2.1 | – | – |
| S2 | 1: D6.3's quantifier alone, with (E) as it is and with V2.4 on | R2V2.2 | – | – |
| S2 | 1: the hand-set histories (chains; pairs tried nothing survives; the student's copy inheriting) | R2V2.3 (a), (b); R2V2.4 | – | – |
| S2 | 2: D6.9, D11.2, D6.8, D5.7 | R2V2.5, R2V2.6, R2V2.9, R2V2.7 | – | – |
| S2 | 2: D8.new1, D10.3, D12.7, D12.8 | D12.7 (R2V2.10) | **D8.new1, D10.3, D12.8** | "upstream of no part of the explanation definition"; D12.7 "taken as their representative" |
| S2 | 2: untouched middle sentences of S2 | – (those the edges name reached through §4) | all | "none is upstream of the explanation definition" |
| S2 | 3: nine edges | all nine (§4; e2.09 noted) | – | – |
| S2 | 4: V1.6's formula with a Desc per case; e1.45–e1.47; e2.38, e2.39 | R2V2.8; R2V2.11 | e1.45–e1.47 proposed but marked "not" settled by the reply | – |
| S3 | 1: S108-3-I2 and I5 (CT as written, as Build; the claim on the own question, the widest contract, another question) | R2V3.1 (another question; the rest cited from round 1) | – | – |
| S3 | 1: the trace's extent, the tag encoding, **the cut K** | R2V3.3 (a), (b); R2V3.2 (the record's key) | **the cut K**; the whole-subhistory extent crossed with R2V3.2's key | cut K: none given; the crossing: named as not reached |
| S3 | 1: S108-3-I4 and I3 (parts as ports, as edits; the stated construction as t's own parts; a history stating no construction left out) | R2V3.4 (ports; stated := t's own parts in its case); R2V3.5 (a third choice, 𝒯 = ∅) | **parts as edits**; **the history stating no construction left out** (both only as "other choices" in (f)) | none given |
| S3 | 1: the hand-set histories | R2V3.6 | – | – |
| S3 | 2: D11.3, D9.1, D9.2 | R2V3.7, R2V3.9, R2V3.8 | – | – |
| S3 | 2: D13.7, D14.1, D15.1, D15.2, D15.5 | D15.5 (R2V3.10); D13.7 only as a note in R2V3.1's row | **D13.7, D14.1, D15.1, D15.2** | D14.1, D15.1, D15.2: "left out for budget"; D13.7: "recorded in R2V3.1's row rather than run" |
| S3 | 2: untouched middle sentences of S3 | – (L405.s2–s5, L481.s3 as co-varied readings) | all | "a sentence-by-sentence pass needs a round of its own" |
| S3 | 3: e3.30b, e3.34b, e3.37b | all three (§4; e3.37b noted) | – | – |
| S4 | 1: S108-4-I1, the pair ('some', 'some-exempt', 'some-exempt-set' with (Suff) co-varied) | R2V4.1 ('some') | **'some-exempt' and 'some-exempt-set' in the pair** | "same expected pattern" (R2-4-I1) |
| S4 | 1: S108-4-I2 ('rule', 'L17', 'both') | R2V4.2 ('both'; 'rule' and 'L17' stated from round 1) | – | – |
| S4 | 1: S108-4-I3 ((a), (b), (c)) | R2V4.3 (a fifth reading (e), and a lemma covering (c) and (d)) | – | – |
| S4 | 1: the hand-set histories | R2V4.4 | – | – |
| S4 | 2: E9 | R2V4.5 | – | – |
| S4 | 2: Part XIV's declared inputs and dependence order (L520, L522, L524, L526) | L522.s1 (R2V4.7), L524.s2 (R2V4.6), L526.s18 (R2V4.8) | **L520** | "L520.s2/s6/n7/s8 … reached only through R2V4.7/R2V4.9" |
| S4 | 2: Part XV's defeat conditions (L534 to L544) | – (L536 and L538 appear only in edges and in R2V4.1, R2V4.2's (Suff) shapes) | **L534, L536, L538, L540, L542, L544** as varied items | (Elim) L540, (QF) L544, (Prov)(ii)–(iii) L542: terms undefined; L534.s3, L536.n2/s3: "their own variation would need V4.4-style readings already computed" |
| S4 | 2: D16.5 (round 1's other untouched middle definition of S4; the share names only E9) | – | D16.5 | "a variant needs a (G)/(EX)/RC model the program lacks (FC110 not tested)" |
| S4 | 3: e4.22, e4.40 | R2V4.10, R2V4.9 | – | – |

Middle definitions still varied by no variant of either round, from the template's lists: S1 D4.6; S2 D6.5, D7.4, D8.new1, D8.3, D10.3, D10.6, D12.2 (read as CT by R2V3.1, not varied), D12.8, E1, E2 (E2 reached by e2.06c's case); S3 D9.9, D9.10, D13.7, D14.1, D15.1, D15.2; S4 D16.5 (D18.1 read by R2V4.8 through L526.s18). Middle sentences varied in round 2: S1 6 (L11.s1, L15.s2, L17.s1, L119.s1, L141.n3, L159.s3), S2 0, S3 0, S4 7 (L522.s1, L524.s2, L526.s18; L572.s2, L574.n4, L576.s1, L576.s4 by R2V4.9's rewording).

## 9. Counts per section, and the same axis across sections (nothing ruled)

| | S1 | S2 | S3 | S4 | all |
|---|---|---|---|---|---|
| variants | 10 | 11 | 10 | 10 | 41 |
| kind: other choice of a reading / strengthen / weaken / delete / swap / re-order / other | 3 / 2 / 2 / 1 / 1 / 0 / 1 (an encoding) | 3 / 4 / 0 / 1 / 1 / 1 / 1 (claims) | 3 / 2 / 1 / 2 / 2 / 0 / 0 | 3 / 1 / 0 / 2 / 3 / 0 / 1 (code) | 12 / 9 / 3 / 6 / 7 / 1 / 3 |
| share part: readings / untouched items / claimed-only edges / V1.6's formula and the blind spots | 3 (R2V1.1, .3, .10; .3 also e1.38) / 6 (L11, L15, L17, L119, L141, L159) / 1 (R2V1.2; plus e1.39 by R2V1.1, e1.38 by R2V1.3) / – | 4 (R2V2.1–.4) / 5 (R2V2.5, .6, .7, .9, .10) / 0 (edges settled by cases, §4) / 2 (R2V2.8, .11) | 6 (R2V3.1–.6) / 4 (R2V3.7–.10) / 0 (edges by cases, §4) / – | 4 (R2V4.1–.4) / 5 (R2V4.5–.8, .10) / 2 (R2V4.9, .10; .10 counted twice) / – | – |
| by the reply's trace: which candidates meet (E) moves | 1 (R2V1.1, under V1.5's conjunct) | 2 (R2V2.1 under V2.3 on its new case; R2V2.8 at phenomenon grain) | 0 | 0 | 3 |
| by the reply's trace: which questions exist moves (so (E) on them) | 2 (R2V1.8, R2V1.9) | 0 | 0 | 0 | 2 |
| by the reply's trace: being an explanation moves, (E) not | 2 (R2V1.3 via D13.8's change; R2V1.6) | 4 (R2V2.3, .4, .6, .7) | 6 (R2V3.1, .2, .3, .4, .5, .7) | 3 (R2V4.1; R2V4.4 on the baseline; R2V4.7 "not statable") | 15 |
| by the reply's trace: neither moves | 5 | 5 (R2V2.2 with (E) as it is, .5, .9, .10, .11) | 4 (R2V3.6 but C9's counts, .8, .9, .10) | 7 | 21 |
| new candidates the reply names | 1 ("C-new", R2V1.6) | 0 | 2 ("C9′", R2V3.3; "C10′", R2V3.5) | 0 | 3 |
| edge rows (§5) | 25 | 27 | 22 | 23 | 97 |
| departs from an owner's decision (reply's own row) | 2 | 4 | 1 | 3 | 10 |
| flag: out of scope (§7; "possible" included) | 7 (R2V1.2, .3, .4, .5, .7, .8, .9) | 2 (R2V2.4, .7) | 0 | 0 | 9 |
| flag: repeats a round-1 variant (in part included) | 0 | 0 | 0 | 3 (R2V4.1, .2 in part; R2V4.9's formula) | 3 |
| flag: adds prose (S40) | 0 | 0 | 0 | 1 (R2V4.9) | 1 |
| flag: moves where values are placed | 0 | 0 | 0 | 0 | 0 |
| small cases after the variant, run | 0 | 0 | 0 | 0 | 0 |

| axis | variants (both rounds where round 2 continues one) |
|---|---|
| provenance of a contract (ρ_p) and question-finding | R2V1.1, R2V1.2, R2V1.3, R2V1.4 · round 1's V1.5 |
| how a record of a contract change is keyed and what it carries (D13.8, I165, I174) | R2V1.2 (Rec_h′(C→C′) with a value), R2V1.3 (Episode reads the value) · R2V3.2 (keyed by the change) · R2V4.10 (records carried by φ) |
| the trace's extent, Held and the tag | R2V3.3 (a), (b) · R2V3.7 (⪯ not transitive: Held's witness) · round 1's V3.5 |
| Sel and the population | R2V2.3 · R2V2.6 (D11.2) · R2V2.7 (surv on the wide extent) · R2V3.4, R2V3.5 (D15.8) · round 1's V2.5, V3.6 |
| inheritance along transfers (D12.3, D12.4) | R2V2.4 (whole-content copy) · R2V4.3 (reading (e); the lemma) · round 1's V4.3 |
| the hand-set histories (I90) | R2V2.3 · R2V3.6 · R2V4.4: three proposals; R2V3.6 expects C7's and C10's counts to reproduce on chains and C9's not; R2V4.4 expects C13's separation to survive and the baseline itself to move |
| the written-in test (Slot, I136) | R2V2.2 · R2V4.1 · round 1's V2.4, V4.1 |
| (Suff)'s shape, and the owner's Q2 answer | R2V1.5 (the four without provenance) · R2V4.2 ('both'; Q2 as an argument) · R2V2.4, R2V2.6 (the student's copy becomes an explanation) |
| fidelity's extent ((A) inside "faithful", D5.7, D12.7) | R2V2.7 · R2V2.10 · R2V1.6 (being an explanation without (F1), (F2)) |
| what counts as a question | R2V1.8 (Y_p fixed) · R2V1.9 (Θ-admitted pairs only) · R2V2.8 (Desc's defects) |
| ruling out, arguments and claims | R2V3.8 (D9.2) · R2V3.9 (D9.1) · R2V4.7 (K2's inputs) · R2V4.6 (unindexed claims) |
| the dependence order and invariance | R2V4.8 (a cycle admitted) · R2V4.10 (D18.2) |
| the owner's vane and sign under encodings | R2V2.1 (mixed) · R2V1.10 (C1's flag) · R2V2.8 (Desc grain) |

## 10. Quotations compared (rule 14)

Every quotation in double quotes was searched for (whitespace, LaTeX and quote marks ignored) in the text by line, the frozen template, the formal core and claims after round 4, the committed printouts of round 1's material, the decisions, and round 1's files. Found verbatim, or with only such differences, unless listed. Program output given in backticks was not checked line by line (rule 5's work), except where a double-quoted line cites it.

| reply | quotation | attributed to | found |
|---|---|---|---|
| 1 (R2V1.9) | "'Physically possible or impossible' … has nothing to do with explanation" | S25 | spliced across two sentences: the owner's "\"Physically possible or impossible\" has to do with instantiation and transformation of information and knowledge. It has nothing to do with explanation." |
| 1 (R2V1.3, before) | `S41: Con at o2 [True]; Build True; no question about the brief occurred: True` (backticks) | FC84.new1 (a1) | two printout lines reordered and joined: "…; no question about the brief occurred: True; cut T′ …" then "S41: 1 fixed point(s) [{'o2': 'Con'}]; Con at o2 [True]; Build True" |
| 1 (R2V1.8, before) | `Ident(p) holds on C_id (I163)` (backticks) | FC28 | condensed: the printout's statement is "Ident(p) :⟺ Q returns a fibre ∧ … (I163) holds on C_id" |
| 2 (R2V2.1) | "(E): True … witness (('e','b0'),['cy'])" | FC22 (b) | order reversed across the ellipsis: the printout gives the witness first, then "(E): True" |
| 2 (R2V2.3) | "(d) … H = ∅, U: fixed points [{'o1':'Con'}]; Dec(t) at o2 [True, True]" | FC30.new1 (d) | one fixed point dropped: the printout reads "H = ∅, U: fixed points [{}, {'o1': 'Con'}]; Dec(t) at o2 [True, True]" |
| 2 (R2V2.5) | "only relabelings" | L257.n3 | not verbatim: "A contract consisting only of relabelings (D6.9)" |
| 3 (R2V3.1) | "δ_E = L: (True, …); δ_E = H: (False, {'A': False})" | FC90.new1 (c) | condensed with no ellipsis inside the second dict: the printout lists every conjunct, 'A': False among them |
| 4 (R2V4.2, R2-4-I2) | "the link was declared, not found by trial or worked out", called "the owner's Q2 answer" | S41 Q2 | the words are Claude's question in S41 ("its link to the pendulum was simply declared, not found by trial or worked out"); the owner's answer is "No, not if just declared" |
| 4 (R2V4.6) | "defeated for j at ξ" | D16.XV | not verbatim: D16.XV writes "defeated for j ⟺ …" |
| 4 (R2V4.7) | "for an assessor j, … (K2)" | L522.s1 | the text ends "(K2, Part IX)" |
| 4 (R2V4.9) | "gives up the claim of a differing survivor" | L576.s4 | not verbatim: "What the qualification gives up is the claim of a differing survivor at every unseen pair" |

Quotation marks around the replies' own phrases (the Desc strings of R2V2.8 other than "red on Mondays, blue on Tuesdays"; "any juxtaposition with no solution"; "meets on C, fails on C′"; "Argument 3's proof changes"; "a predicate of the case alone"; "surviving alternative"; "traces carried along"; R2V4.9's and R2V4.10's new wordings) are not quotations of the text and were not compared.

## 11. Words of S23, and "model", in the replies' own glosses (rule 13)

No variant's statement holds a word S23 lists. In the replies' glosses: "true" (reply 1: R2V1.2 "readable and true", R2V1.4 "true under the variant", R2V1.7 "true (β = swap)"); "derivable", "derivation", "stands by derivation" (reply 1, R2V1.5, e1.36); "keeps its truth", "the derivation" (reply 4, R2V4.9 and e4.40); "false" of sentences (reply 4, R2V4.5, R2V4.9; not a listed word). True/False as program output is not counted. "Model" never names a candidate: every "model" is `model.run` or the program's folder, and reply 4's "a (G)/(EX)/RC model the program lacks" is a small structure the program would build.

## 12. Unsure

- The out-of-scope flags marked "possible" (R2V1.2, R2V1.8, R2V2.4) turn on whether a formula is a reading of the FROZEN words or a change of them: "requires" read as ⟺; Y_p fixed where D3.2 leaves it free; D12.4's "part" taken as the whole transport for one kind of copy. This agent rules on none of them.
- R2V1.6 (being an explanation without (F1), (F2)) and R2V1.5 (the four without provenance) change what S1's own sentences (L17, L49, L69) and S4's D16.XV state together; round 1 did not flag the like for V4.1–V4.3 (S4 changing what S1's sentences say). R2V1.5 is flagged here because its formula is written on D16.XV's set; R2V1.6 is not, because its formula is written on Expl, which S1's sentences state.
- "Repeats a round-1 variant" is flagged only where the reply's own words or round 1's files show the computation done (R2V4.1, R2V4.2 in part; R2V4.9's formula). R2V2.2's values are round 1's and the suite's by the reply's own words; it is listed under "not flags" because the share asks for it as a reading.
- Several expected outcomes rest on a change another section would make (R2V1.3 and e1.38 on D13.8 reading ρ's value) or on the reply's own reading (e2.06c on Inv-R2-5; e4.40 on R2-4-I7); §4 lists them as proposals, not results.
- The section's shares and the templates' marks were read from the frozen set `.json` and the briefs; a sentence id the template does not hold (none met here beyond FC-claims and I-numbers) would have been listed.
