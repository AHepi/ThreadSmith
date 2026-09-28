# S108 Part A - tabulation of the replies, before any ruling

*Written by the tabulating agent (Opus 5.5, rule 4 of `results/S108 Part A - how the replies will be read, written before sending.md`), 28 September 2026. Fresh: built nothing of Part A; had read no reply before this file was created. Rules on nothing; implements nothing; changes no theory text, formal core, claim or program (rule 11). "Candidate" or "explanation" for what the theory judges, never "model" (S43); "model" below means only a small structure the program builds.*

Status: complete, 28 September 2026. Nothing ruled.

## 0. Before reading (rules 1, 2)

| check | state |
|---|---|
| rule 1: every call ended | run log: `s108_glm_loop: every pass ended; accepted 4 of 4 jobs`, `loop ended 2026-09-28T18:19:20Z`; the pid (3947) has exited |
| rule 2: key in output | receipts, field `key_found_in_output_and_replaced`: 0, 0, 0, 0 (only this field and the next were read from the receipts) |
| rule 2: sandbox unchanged | receipts, `sandbox_unchanged`: True ×4, 50 files each |
| replies read (rule 2: `.response.txt` only) | section 1 `2079837edc80f619c5a9d9eff8f78e09` (2,636 words); section 2 `1d602e0f4b756a75773ae3d4d95ff5d1` (2,507); section 3 `7a7bda1cd8365bd8d85c2eb2cf72d931` (2,409); section 4 `2cd6484ae5ec8feb11bdc5fcf553e63a` (2,390); each pass 1, each ends END OF REPORT |
| not opened | reasoning files, stream files, guard logs, requests |
| marks used | the frozen template, §3 and §4 (815 items: 238 FROZEN; S1 154, S2 153, S3 137, S4 133, as the rule gives); claims' sections from its §5 |

Every "after" in every reply is marked **not run** by the reply; a "before" is either run (the reply cites a claim of the suite) or worked by hand, as §3 marks. Everything below is the replies' claims (rule 3), with the template's marks and the owner's words beside them.

## 1. Counts per section

| | S1 | S2 | S3 | S4 | all |
|---|---|---|---|---|---|
| variants | 8 | 8 | 8 | 8 | 32 |
| kind: delete / weaken / strengthen / swap / other | 2 / 2 / 1 / 2 / 1 | 0 / 4 / 3 / 1 / 0 | 7 / 0 / 1 / 0 / 0 | 3 / 2 / 1 / 2 / 0 | 12 / 8 / 6 / 5 / 1 |
| by the reply's trace: which candidates meet (E) moves (so being an explanation moves with it) | 4 (V1.1, V1.5, V1.6 by its formula, V1.7) | 4 (V2.1–V2.4) | 0 | 0 | 8 |
| by the reply's trace: being an explanation (Account ∧ ¬Dec(t)) moves, (E) does not | 0 (V1.6 by its trace: see §6) | 1 (V2.5) | 3 (V3.4, V3.5, V3.6) | 3 (V4.1, V4.2, V4.3) | 7 |
| by the reply's trace: neither moves; something else does | 4 (V1.2, V1.3, V1.4, V1.8) | 3 (V2.6, V2.7, V2.8) | 5 (V3.1, V3.2, V3.3, V3.7, V3.8) | 5 (V4.4–V4.8) | 17 |
| edge rows: blocks / constrains / changes with / moves | 5 / 8 / 8 / 8 | 6 / 6 / 5 / 5 | 4 / 6 / 4 / 8 | 2 / 6 / 5 / 7 | 17 / 26 / 22 / 28 = 93 |
| of the blocks rows, naming a FROZEN item | 4 (V1.1, V1.2, V1.7, V1.8) | 3 (V2.2, V2.3, V2.6) | 2 (V3.4, V3.7) | 1 (V4.7) | 10 |
| edges the reply leaves unsettled or partly | 1 | 1 + 1 in prose | 1 | 5 + 1 in prose | 10 |
| departs from an owner's decision (reply's own row) | 1 (V1.6: S21) | 4 (V2.4: S45, S44; V2.5: S41 Q2; V2.6: S20; V2.7: S27) | 3 (V3.1: S23; V3.3: S28, S41 Q23; V3.8: S47) | 3 (V4.1: S45; V4.2: S41 Q2; V4.4: S23) | 11 |
| **flag: out of scope** (FROZEN or another section's item) | 2, in effect (V1.6, V1.7) | 1, as written (V2.8) | 0 | 0 | 3 |
| **flag: adds prose (S40)** | 1 (V1.6) | 0 | 0 | 0 | 1 |
| **flag: moves where values are placed** | 0 | 0 | 0 | 0 | 0 |
| new inventions the reply names | 0 | 2 (V2.2, V2.3) | 0 | 2 (V4.5, V4.8) | 4 |
| small cases after the variant, run | 0 | 0 | 0 | 0 | 0 |

## 2. The variants

Old = the template's current statement of the clause varied (checked against the reply's "old"; they agree unless a note says otherwise). New = the reply's. Marks in brackets are the template's.

### Section 1 (Part 0 to Part III)

| id | item varied | kind | old | new | why (reply) |
|---|---|---|---|---|---|
| V1.1 | D1.4 [S1] | swap | Sol_N(a,b) := {z ∈ ∏_{v∈V_N} X_v : ∀j ∈ N, z\|V_j ∈ L_j(a,b)} (the constraints of N alone, I14) | Sol_N(a,b) := {y\|V_N : y ∈ Sol_D(a,b)}; V_N, I138 unchanged | (F1) is built on Sol_{N_k} |
| V1.2 | D2.1 [S1] | delete | a sets v through j at b :⟺ L_j(a,b) = {w ∈ ∏_{V_j} X : w_v = x} for some x ∈ X_v ∧ ∀k ≠ j: L_k(a,b) = L_k(1,b) (I04) | a sets v through j at b :⟺ L_j(a,b) = {w ∈ ∏_{V_j} X : w_v = x} for some x ∈ X_v; Set_v, asg as before | grows Set_v, hence Prod(p) and Input |
| V1.3 | D2.4 [S1] | weaken | Obs(o,m) := {a ∈ Alt_j ∖ Slc_j : L_asg(m)(a,b) = L_asg(m)(1,b) ∀b} (I06, reading R-ii) | Obs(o,m) := {a ∈ Alt_j : L_asg(m)(a,b) = L_asg(m)(1,b) ∀b} (reading R-i) | does the reading of observation reach (E) |
| V1.4 | D3.3 [S1], Ident clause | swap | Ident(p) :⟺ Q returns a fibre g⁻¹(obs(a,b)) ∧ ∃(a,b),(a′,b′) ∈ C: obs(a,b) ≠ obs(a′,b′) (I163) | Ident(p) :⟺ Q returns a fibre ∧ ∃(a,b) ∈ C: a ≠ 1 ∧ obs(a,b) ≠ obs(1,b0) | decides whether C_id asks an identification question |
| V1.5 | D3.4 [S1]; L155.s2, L155.s5 [S1] varied with it, new form not given | delete | ρ_p ∈ {declared, selected, constructed}; declared :⟺ neither (I127) | ρ_p ∈ {selected, constructed}; a contract with neither history is no question's contract | is ρ_p, unlike Dec(t), read anywhere in being an explanation |
| V1.6 | D3.6 [S1] + a new sentence in Part III | strengthen | D3.6 defines BadTarget, BadBaseline, BadReq (with Desc, I76); only BadBaseline is read (through NonVacuous) | D3.6 unchanged, and: BadTarget(p) ∨ BadReq(p) ⇒ ∀ℰ ¬Acc(ℰ,p). The trace writes instead: being an explanation := Account(ℰ) ∧ ¬Dec(t) ∧ ¬BadTarget(p) ∧ ¬BadReq(p) | the two defects are read by nothing |
| V1.7 | D0.2 [S1] | other | Excl(Σ) a primitive (I27); D3.5 [FROZEN]: Σ is a declared input naming Excl(Σ) ⊆ A×B; Stated(C,Σ) :⟺ (A×B)∖C ⊆ Excl(Σ) | Excl(Σ) := (A×B) ∖ C, defined; so Stated(C,Σ) always holds | the silent narrowing L43.s4 says is caught |
| V1.8 | D2.6 [S1] | weaken | Slc_j := {a ∈ Alt_j : ∀b [L_j(a,b) ≠ L_j(1,b) ⇒ ∃v ∈ V_j, asg(v) = j, ∃x: L_j(a,b) = {w : w_v = x}]} (I125) | Slc_j := Alt_j | D2.6's distance from (E) |

### Section 2 (Part IV to Part VII)

| id | item varied | kind | old | new | why (reply) |
|---|---|---|---|---|---|
| V2.1 | D6.4 [S2]; L255.n2 [S2] | weaken | NC2(ℰ) :⟺ ∃(a,b) ∈ C, G ⊆ Γ, G ≠ ∅: Contrast(E;x) ∧ Lost(E,G;x) | NC2(ℰ) :⟺ ∃(a,b) ∈ C: Contrast(E;x) | cuts the one conjunct of (E) that ties the answer to Γ |
| V2.2 | D6.4 [S2] | strengthen | as V2.1 | NC2(ℰ) :⟺ ∃(a,b) ∈ C, d ∈ Γ: Contrast(E;x) ∧ Lost(E,{d};x) | Dependence tied to one commitment |
| V2.3 | D6.4 [S2] | strengthen | as V2.1 | NC2(ℰ) :⟺ ∃(a,b) ∈ C with a ≠ 1, G ⊆ Γ, G ≠ ∅: Contrast(E;x) ∧ Lost(E,G;x) | boundary-only contrasts stop counting |
| V2.4 | D6.7 [S2]; L261.n1 [S2] | strengthen | Acc(ℰ) :⟺ F1_C ∧ F2_C ∧ A_C ∧ Dependence ∧ NonVacuous (Dependence := NC0 ∧ NC2) | Acc(ℰ) :⟺ F1 ∧ F2 ∧ A ∧ NC0 ∧ NC1 ∧ NC2 ∧ NonVacuous (round 3's (E)) | puts the written-in test back in (E) |
| V2.5 | D12.1 [S2]; "L195" (no sentence id; L195.s1, .s5 FROZEN, .s2, .s3, .n4, .s6 S2) | weaken | Sel(t;𝒯,μ,H) :⟺ … H ⊆ C finite and nonempty, its pairs having occurred in h(t) … (the core marks "nonempty" as I52's registered other choice, added in round 3) | the same with "H ⊆ C finite" (H = ∅ allowed) | a stipulated population makes a transport Sel |
| V2.6 | D8.2 [S2]; L315.n2 [S2] | weaken | For (a,b) ∈ A_D × B_D that both transports translate, in C or outside it: Conf(ℰ,ℰ′;a,b) :⟺ [answers differ in Y_p ∪ {⊥}] ∨ [∃R Meets_ab(ℰ,R) ∧ ∃R′ Meets_ab(ℰ′,R′) ∧ ¬∃R″ BothMeet_ab(R″)] | the same, for (a,b) ∈ C only | confines conflict to the contract |
| V2.7 | D8.5 [S2]; L315.n11 [S2] | weaken | ConfCl(ℰ,χ;a,b) :⟺ [∃R Ans^R_p(a,b) = y ∧ ∀R (Ans^R_p(a,b) = y ⇒ R ∉ Allow_χ(a,b))] ∨ [∃R Meets_ab(ℰ,R) ∧ ∀R (Meets_ab(ℰ,R) ⇒ R ∉ Allow_χ(a,b))] (I137) | the first disjunct alone | conflict with a claim only through the answer |
| V2.8 | D9.8 [S2]; L315.s6 [S2]; L315.s7 [FROZEN] | swap | X_j(φ) := {α : Usable_j(α) ∧ RO(α,φ)}; Out_j(φ) :⟺ X_j(φ) ≠ ∅; ℰ ruled out for j :⟺ Out_j('Acc(ℰ)') (old not given by the reply) | Out_j('Acc(ℰ)') :⟺ ∃α ∈ X_j('Acc(ℰ)') with Acc(ℰ) ∈ Uses(α) ("I196's instance reading") | changes which arguments rule a candidate out |

### Section 3 (Part VIII to Part XII)

| id | item varied | kind | old | new | why (reply) |
|---|---|---|---|---|---|
| V3.1 | D9.7 [S3]; L397.n14, L397.s16 [S3] varied with it, new form not given | delete | RO(α,φ) :⟺ Incons(φ, concl(α)) ∧ no leaf of α has ¬φ as a conjunct (flattened, up to renaming and order; I39) ∧ no record leaf of α is made from a claim whose denial is φ | RO(α,φ) :⟺ Incons(φ, concl(α)) | what else, if anything, blocks "p because p" |
| V3.2 | D9.4 [S3] | delete | Live_j(d;u) :⟺ ∃u′ ∈ Below(u) [d = concl(u′) ∧ Usable_j(u′)] ∨ d ∈ Accepted_j(ξ) (I40) | Live_j(d;u) :⟺ d ∈ Accepted_j(ξ) | how much ruling out rests on the tree |
| V3.3 | D9.6 [S3] | delete | Usable_j(α) :⟺ ∀u ∈ steps(α) Usable_j(u) ∧ [steps(α) = ∅ ⇒ concl(α) ∈ Accepted_j(ξ)] (I166) | Usable_j(α) :⟺ ∀u ∈ steps(α) Usable_j(u) | a bare claim would rule out with no one taking it up |
| V3.4 | D13.3 [S3], ExplUse | strengthen | ExplUse(o,c) :⟺ UsesClaim(o,'Acc(ℰ)') for some ℰ = (E,p,t,Γ,δ_E) with c ∈ {E,t,C_p}; the claim need not hold (I178) | ExplUse(o,c) :⟺ UsesClaim(o,'Acc(ℰ)') ∧ Acc(ℰ) for some such ℰ | may construction feed on an account in error |
| V3.5 | D13.8 [S3], Episode | delete | Episode(h′) :⟺ h′ ⊆ h a subhistory ∧ for every o ≺_h′ o′, o′ immediately after o, with q(o) ≠ q(o′): Rec_h′(ρ_q(o′)) (I165, I173, I174) | Episode(h′) :⟺ h′ ⊆ h is a subhistory | how much of Con, hence of ¬Dec, rests on records |
| V3.6 | D15.8 [S3]; L481.s3 [S3] varied with it, new form not given | delete | 𝒯 := {t : Θ admits t ∧ parts(t) ⊆ the parts of the stated construction} (I158) | 𝒯 := {t : Θ admits t} | how much of Sel is fixed by the stated construction |
| V3.7 | D11.4 [S3] | delete | ActRoute_h(R;i,r,K) :⟺ i,r ∈ R ⊆ O_h ∧ ∀n ∈ R: n ⇝_R r ∧ ∀n ∈ R: n meets Org_ℓ(h)'s relation ∧ ∃(x,x′) ∈ K: val_r(Org_ℓ(h)\|_R[i:=x]) ≠ val_r(Org_ℓ(h)\|_R[i:=x′]) ∧ ¬AtRest_h(R,r) | the same without the ∃(x,x′) ∈ K conjunct | is the "did work" clause read by the definition |
| V3.8 | D14.7 [S3] (L445.s1's formal statement) | delete | CreateEx(s,Δ,h,e) :⟺ CreativeCriticalEpisode(s,Δ,h,e) ∧ ∃ξ,ξ′[Repair_{O,P}(ξ,ξ′;Δ) ∧ ∃o ∈ O_ex ∃c,p_c,e_c,t_c,Γ_c,δ_c (e_c ⪯_h e ∧ ¬o(ξ) ∧ o(ξ′) ∧ Origin(s,c,p_c,h,e_c) ∧ Acc((c,p_c,t_c,Γ_c,δ_c)) ∧ c ∈ Result(Δ) ∧ Deploy(s,c,ξ′;U_c) ∧ ProducesVia(Δ,c,o;ξ,ξ′))] | the same without CreativeCriticalEpisode(s,Δ,h,e) | does the critical episode do work in (EX) |

### Section 4 (Part XIII to Part XVI)

| id | item varied | kind | old | new | why (reply) |
|---|---|---|---|---|---|
| V4.1 | D16.XV [S4], the rule on Expl | strengthen | Acc(ℰ) ∧ Dec(t) ⇒ ¬Expl(ℰ) (being an explanation: Account(ℰ) ∧ ¬Dec(t)) | beside it, Acc(ℰ) ∧ Slot_C(ℰ) ⇒ ¬Expl(ℰ) (Slot as D6.3, reading "every"); i.e. Expl :⟺ Acc ∧ ¬Dec ∧ ¬Slot | the written-in test at the level of being an explanation |
| V4.2 | D16.XV [S4], the rule on Expl | delete | as V4.1 | rule deleted: Expl(ℰ) :⟺ Acc(ℰ) | does provenance matter at all |
| V4.3 | D16.XV [S4], (Suff) shape and being an explanation | swap | (Suff): defeated for j ⟺ ∃ℰ [Acc(ℰ) ∧ ¬Dec(t) ∧ ∃α ∈ X_j(Expl(ℰ)): Acc ∉ Uses(α)]; being an explanation: Acc ∧ ¬Dec(t) | ¬Dec(t) → ¬Dec(t) ∧ (Sel(t) ∨ CT(t)), in both | must provenance be positive |
| V4.4 | D16.XV [S4], Uses(α) | swap | 'an argument not using (E)' := Acc ∉ Uses(α), at the symbol (I196) | Acc(ℰ) ∉ Uses(α), at the instance | the readings part on arguments citing a rival's Acc |
| V4.5 | D16.XV [S4], (Nec) shape; L538 [S4] | weaken | (Nec): defeated for j ⟺ ∃ℰ [∃α ∈ X_j(¬Expl(ℰ)): Acc ∉ Uses(α) ∧ ∀C′ on D ∀t′: ¬Faithful_{C′}(t′: D → E)] | … ∧ ∀t′: ¬Faithful_C(t′: D → E) | (Nec)'s exposure restricted to C |
| V4.6 | D16.4 [S4] | delete | 𝔈_Θ := {c : Acc((c,p,t,Γ,δ)) for some p,t,Γ,δ, δ the designation of Q in c, and Θ admits a carrier instantiating c} (I75, I183) | the same without "δ the designation of Q in c" | must explanatory content answer the question it designates |
| V4.7 | D16.3 [S4] | delete | Enable(s,T,χ) :⟺ Θ admits χ ∧ NQB ∧ χ an enabling condition in (CT1)'s sense (I154) | Enable(s,T,χ) :⟺ Θ admits χ ∧ χ an enabling condition in (CT1)'s sense | the weight of NQB in the class |
| V4.8 | D12.9 [S4] + (Prov)(i) in D16.XV [S4] | weaken | Underdet(t;a,b;𝒯,H) :⟺ some t′ ∈ 𝒯 with surv(t′,H) has value_t′(a,b) ≠ value_t(a,b); (Prov)(i): ∃t [Sel(t;𝒯,μ,H) ∧ (a,b) ∈ C∖H ∧ ∃t′ ∈ 𝒯 surviving on H with value_t′(a,b) ≠ value_t(a,b) ∧ value_t(a,b) a function of (𝒯,H)] | Underdet :⟺ ∃t′ ∈ 𝒯: value_t′(a,b) ≠ value_t(a,b); (Prov)(i)'s middle conjunct → Underdet(t;a,b;𝒯,H) | makes (Prov)(i) satisfiable |

## 3. The traces (each reply's claim; every "after" not run)

"In" / "out": candidates that newly meet, or stop meeting. "Run" = the reply cites the claim's output; "by hand" = the reply works it out without a run. Explanation = Account(ℰ) ∧ ¬Dec(t).

### Section 1

| id | meets (E): in / out | explanation: in / out | what else moves | cases: before | after |
|---|---|---|---|---|---|
| V1.1 | in: ℰ_bv (E_bv = D_pole with c_L replaced by c_bv, L_bv(1,b) := {(u_H,u_θ,u_H·cot u_θ)}, Γ = {c_bv}, identity τ,σ,π, λ(c_bv) = {c_L}); out: E_fwd on C1 and C2 ((F1) fails at every pair); E_enc stays in, E_tab stays out | E_fwd out; ℰ_bv "becomes an account" | (F1) reads Sol_D's projection, not the counterpart's own constraints | E_fwd on C1: run (FC26); ℰ_bv: not run | not run |
| V1.2 | none | none | Prod(p*) holds for p* = (D_pole, {(1,b1_45), (set(H=2,T=60), b1_45)}, Q_L): p* becomes a production question | a ∉ Set_H, Set_T: by hand; FC07's round-2 precedent: run | not run |
| V1.3 | none (`core.account` reads no Roles; FC30 run) | none | on C2, c_L no longer a causal assignment; meas = {(c_L,H),(c_L,T)} | C2 under R-i and R-ii: run (FC07, FC2.new1) | not run ("the program already computes it") |
| V1.4 | none | none | Ident(p_id) fails on C_id = {1}×B; E_rev meets (E) on a question whose respect is unnamed; L271.s2 no longer points at C_id | E_rev on C_id: run (FC28) | not run |
| V1.5 | out: every candidate of a question whose contract is declared (no such question); E1–E6 need a selected or constructed contract | same | which questions exist; ρ_p unread, Dec(t) read ("the finding") | E_fwd on C1: run (FC26) | not run |
| V1.6 | out (by the formula): every candidate of a BadTarget or BadReq question, e.g. E_fwd on p′ (target D_pole, Desc′ := "an organization with ports H, T, L and a component on all three", met by D_pole and E_rev) | out: E_fwd on p′ | being an explanation gains ¬BadTarget(p) ∧ ¬BadReq(p) | FC106: run (the two defects "not tested"); p′: not run | not run |
| V1.7 | in: silently narrowed contracts, e.g. D with one port p0, edits {1,[alt]}, B = {b0,b1}, C′ = {(1,b0),(1,b1)}, Σ′ with Excl(Σ′) = ∅: Acc ✗ → ✓ | not stated | NonVacuous's second conjunct reads nothing | FC34's witness: run; Stated(C′,Σ′) ✗: by hand | not run |
| V1.8 | none (FC30 run) | none | measurement and rule families empty everywhere; no rule relation variable under edits to itself | C2 under R-ii: run (FC07) | not run |

### Section 2

| id | meets (E): in / out | explanation: in / out | what else moves | cases: before | after |
|---|---|---|---|---|---|
| V2.1 | in: every candidate whose commitments do no work (L313) and whose answers vary over C; e.g. D ports x,y,z ∈ {0,1}; cx:(x), cy:(x,y), dz:(z); A = {1,e}; L_cx(e,b0) = {(1)}; L_cy = {(0,0),(1,1)}; Γ = {dz}; δ_E = y; C = {(1,b0),(e,b0)}: ¬Acc → Acc; out: none | not stated (the case's transport is declared: "still not an explanation") | Dependence no longer reads Γ | by hand, not run | not run |
| V2.2 | out: L311's infinitary Γ = {d_n : \|x\| ≤ 1/n}; L307's redundant Γ = {a,b}; in: none | the same out | fewer problems (D10.4, D10.6) | FC40 run (routes); NC2: by hand, not run | not run |
| V2.3 | out: E_rev and E_fwd on C_id; every candidate on a contract {1}×B (identification questions admit no accounts); the weathervane M13 stays in | not stated | — | E_rev on C_id: run (FC28), NC2 not run; M13: run (FC22) | not run |
| V2.4 | out: E_enc, ℰ_one, ℰ_myth1, M1–M3, every lookup E_lk (FC23 (e)); stay: E_fwd, ℰ_two, ℰ_myth2; in: none | the same out | Bearing (D9.10): the myth's slot connection loses bearing | run (FC26, FC25.new2 (c), FC23 (c), FC23.new2 (a), (b), FC72.new2 (a)) | "= round 3's (E), computed in those same printouts" (reply); not run under the variant |
| V2.5 | none | in: the student's declared copy (Dec → Sel), and every declared transport whose population and survival condition are only stipulated | Dec shrinks to "no population and no trace" | FC30.new1 (e), (a): run; the printout also gives the round-2 reading (H = ∅): Sel True, Dec False | not run |
| V2.6 | none | none | no conflict outside C; the tilt and the myth (Greeks' contract) are no longer rivals; no problem of the second kind; ETV_j (D10.4) false of every candidate | FC72.new2 (b), (d): run | not run |
| V2.7 | none | none | conflicts that run through the relations a candidate needs, not its answer, disappear; e.g. D ports w,y; comp c:(w,y); L_c(1,b0) = {(1,0)}; χ = "perpetual motion is impossible", Allow_χ(1,b0) = {R : R_c = {(0,0)}}: ConfCl ✓ → ✗ | by hand, not run | not run |
| V2.8 | none | none | (Suff)'s defeat set grows by arguments reaching ℰ only through another candidate's Acc | FC30.new1 (h): run ("symbol False, instance True") | not run |

### Section 3

| id | meets (E): in / out | explanation: in / out | what else moves | cases: before | after |
|---|---|---|---|---|---|
| V3.1 | none | none | ¬PM alone rules out PM for j who accepts ¬PM; a record made from ψ rules out ¬ψ; accepting 'Ans_p(a,b) = y' rules out every candidate answering y at (a,b) with no test; (Suff), (Nec) defeat sets reachable by acceptance alone | FC72 (e), (b): run | not run |
| V3.2 | none | none | multi-step arguments unusable unless each intermediate conclusion is in Accepted_j; X_j shrinks; fewer ruled out, fewer problems and solved; defeat sets shrink | FC70: run | not run |
| V3.3 | none | none | "perpetual motion is impossible" alone rules out the design for every assessor, taken up or not; defeat sets and Prob_j assessor-independent | FC72 (f), (d): run | not run |
| V3.4 | none | out: a candidate whose transport's construction uses an account failing (E) on its contract of use; e.g. E_rev meeting (F1), (F2), (A) on the identification contract but claimed on the production contract: Build ✗ → CT ✗ → Dec(t) | Dec grows via CT | FC90.new1, FC28, FC27: run; the case: not run | not run |
| V3.5 | none | in: candidates whose transport was Dec for want of an episode after an unrecorded change of contract (CT gains witnesses, Con grows) | Episode, Con | FC84.new1 (c), (iv-u): run | not run |
| V3.6 | none | in: holdings Dec for want of a Sel witness become Sel; the student's copy stays Dec (its defect is the absent trace) | Sel; Argument 3's underdetermination (FC80) reaches more pairs; e.g. pole forward organization, t with parts {set H, set T}, t′ = t plus a setting of L, H = {(1,b1_45)} | no claim computes the parts clause (I158); the case: not run; FC30.new1 (d): run | not run |
| V3.7 | none | none | both routes of FC75 (a′) active; ProducedBy (D14.3), ProducesVia (D14.6), UsesReason (D9.11) reach idle routes; (P) and (EX) attribution widens | FC75 (a′), (a): run | not run |
| V3.8 | none | none | the class of created explanations widens: the bridge (a1) counts whenever repair, origin, Account, Deploy and ProducesVia hold, under both labellings of "no question occurred" | FC84.new1 (a4): run ([False, True] under I191; [False] under I192 (d)) | not run ([True] under both, claimed) |

### Section 4

| id | meets (E): in / out | explanation: in / out | what else moves | cases: before | after |
|---|---|---|---|---|---|
| V4.1 | none | out: ℰ_one, E_enc, E_rev under τ′ (slot ['r_L']), the pole on C2 (8 pins by c_L); stay: ℰ_two, the pole on C1 | a written-in answer moves from "bad explanation" to "no explanation"; Slot becomes an ancestor of Expl in D18.1's graph | FC23.new2, FC23.new3, FC25.new2: run; FC27.new1 (d): cited | not run |
| V4.2 | none | in: the student's declared copy and every Dec candidate meeting (E) | FC30.new1 (b)'s Def_j(L17, S41) = Def_j(L536) fails unless L536's "whose provenance is not declared" goes with it | FC30.new1 (a), (c): run | not run |
| V4.3 | none | out: every candidate with no provenance record: E_enc, E_rev under τ′ ("exactly the formal core's own worked cases"); stay: E9's t1 (Con), a selected t0; the student's copy out under both | explanation asks for positive provenance | FC25.new2 (a), FC27.new1 (d): run | not run |
| V4.4 | none | none | (Suff)'s defeat set grows: an argument citing Acc(ℰ_rev) to rule out Expl(ℰ_fwd) now counts | FC30.new1 (h), FC103.new1: run | not run |
| V4.5 | none | none | an argument not using (E) for Expl(E_rev) defeats (Nec); likewise E5's eliminative candidates | FC27.new1 (b), (d), FC99: run | not run |
| V4.6 | none | none | 𝔈_Θ unchanged on E1–E9 (expected); bites only where every Acc-witness mis-designates; reach needs a generated search | FC90.new1 (c): run | not run |
| V4.7 | none | none | UU, UC met more easily; UECS grows; RC untouched | none (FC110 not tested); formal trace only | not run |
| V4.8 | none | none | (Prov)(i) becomes satisfiable: a differing non-survivor counts toward Underdet | FC80 (a), (d): run | not run |

## 4. The edges, as each reply names them

The reply's words for the item (cut at 90 characters), then the template's mark of every id named. Rows a reply lists as "—" or "none" are kept.

| variant | kind | item named (reply) | template mark of each id named | why (reply, cut) | settled (reply) | note |
|---|---|---|---|---|---|---|
| V1.1 | blocks | D4.4 (FROZEN, §4 in S1's stretch) | D4.4 FROZEN | for N = {j}, sig becomes the full-solution projection, not L_j, so "extends (K)" (L115 FROZEN) fails wherever a sibling… | yes, by wording |  |
| V1.1 | constrains | D5.2 (FROZEN, S2) | D5.2 FROZEN | proj^λ stays readable, but "hidden ports projected away" stops matching: siblings' constraints now reach the projection… | yes |  |
| V1.1 | changes with | L233.s1 (S2), L556.n2 (S4), FC17/FC18 | L233.s1 S2; L556.n2 S4; FC17 claim S2, S4; FC18 claim S2, S4 | L233's "imposing the constraints of λ(k)" words the old reading; Argument 1's two signatures and its claims must be rec… | yes |  |
| V1.1 | moves | (F1): what it reads (Sol_{N_k}) | — | E_fwd out, ℰ_bv in; component fidelity stops isolating the counterpart's own constraints | yes |  |
| V1.2 | blocks | L103.s2 (FROZEN, S1) | L103.s2 FROZEN | an edit that sets v through j while altering k does "add an equation beside" | yes, by wording |  |
| V1.2 | constrains | D2.2, D2.5 (FROZEN, S1) | D2.2 FROZEN; D2.5 FROZEN | Input and dir stay readable; their extensions grow with Set_v | yes |  |
| V1.2 | changes with | D2.6, D2.4 (S1, mine), E1's setting-edit meta I04 (S2), FC27.new1 (S2) | D2.6 S1; D2.4 S1; E1 S2; FC27.new1 claim S1, S2 | Slc_j and Obs read Set_v; E1's "each setting replacing its component" and "the production contract" re-read | partly — whether Slc_j must grow with Set_v to keep L57's s… |  |
| V1.2 | moves | no conjunct of (E); the respect "production" | — | what meeting (E) says on composite-only contracts | yes |  |
| V1.3 | constrains | L124.s1, L125.s1 (FROZEN, S1) | L124.s1 FROZEN; L125.s1 FROZEN | the families stay definable; their extensions shift (FC07 computes both) | yes |  |
| V1.3 | changes with | L123.n1 (S1), D4.6 (S1) | L123.n1 S1; D4.6 S1 | the causal-assignment gloss excludes readers of assigned ports (FC2.new1) | yes |  |
| V1.3 | moves | nothing in (E) | — | D2.4 → families → not (E): the reading choice never reaches the account | yes (FC30 run) |  |
| V1.4 | constrains | L151.s1 (S1), L151.s2 (FROZEN, S1) | L151.s1 S1; L151.s2 FROZEN | "fixed by the type of Q and the shape of C" and the Prod clause are untouched | yes |  |
| V1.4 | changes with | E1's C_id (S2), L271.s2 (S2), L325.n6 (S2), FC28/FC28.new2 | E1 S2; L271.s2 S2; L325.n6 S2; FC28 claim S2; FC28.new2 claim — | the identification reading of C_id and the reversed calculation's home question move with it | yes |  |
| V1.4 | moves | what meeting (E) says on C_id | — | the respect is unnamed; Acc's extension unchanged | yes |  |
| V1.5 | blocks | L155.s2, L155.s5 (S1, varied with it) | L155.s2 S1; L155.s5 S1 | declared contracts and "any assessment may use any of the three" are negated | yes | names middle items only |
| V1.5 | constrains | L155.s6 (FROZEN, S1), D3.1 (FROZEN, S1) | L155.s6 FROZEN; D3.1 FROZEN | found ⇒ constructed stays readable; ρ_p's slot stays in the tuple | yes |  |
| V1.5 | changes with | D13.8 q(o)/Rec (S3), D16.4 𝔓^adv (S4), (QF) L544 (S4), E8 (S2) | D13.8 S3; D16.4 S4; L544 line: S4; E8 FROZEN | episode records and question-finding quantify over contracts that must now be non-declared | yes | reply marks E8 S2; template FROZEN; names a FROZEN item as changing with it |
| V1.5 | moves | which questions exist | — | candidates on declared-contract questions stop meeting (E), with (E) and Expl unchanged in form | yes |  |
| V1.6 | constrains | L161.s1–s3 (FROZEN, S1), D6.6 (FROZEN, S2) | L161.s1 FROZEN; D6.6 FROZEN | defective questions stay questions; NonVacuous keeps BadBaseline, the variant adds the other two beside it | yes |  |
| V1.6 | changes with | D16.XV (Suff)/(Nec) (S4), FC106 (S1) | D16.XV S4; FC106 claim S1 | the defeat sets would quantify over non-defective p; FC106's untested parts become testable | yes |  |
| V1.6 | moves | being an explanation | — | gains the question's non-defect beside Account ∧ ¬Dec(t) | yes |  |
| V1.7 | blocks | D3.5 (FROZEN, §3 in S1's stretch), L43.s4, L159.s1 (S1) | D3.5 FROZEN; L43.s4 S1; L159.s1 S1 | "Σ is a declared input naming Excl(Σ)"; the stated-scope requirement and grievance 4's answer fall | yes | L43.s4, L159.s1 middle |
| V1.7 | constrains | D6.6 (FROZEN, S2) | D6.6 FROZEN | NonVacuous keeps its form; its second conjunct becomes vacuous | yes |  |
| V1.7 | changes with | none required | — | the theory hangs together; L317.s15 (FROZEN, S2) is safe (narrowing still makes a new question) | yes |  |
| V1.7 | moves | NonVacuous: what its second conjunct reads (nothing) | — | silently narrowed contracts newly meet (E) | yes |  |
| V1.8 | blocks | L347.s2 (FROZEN, S2's stretch) | L347.s2 FROZEN | Changes_C(j, Alt_j∖Slc_j) = Changes_C(j,∅) is false by D4.5, so no rule relation's signature is variable under edits to… | yes |  |
| V1.8 | constrains | L57.s1 (FROZEN, S1) | L57.s1 FROZEN | the rule/cause difference stays definable; the rule side is empty | yes |  |
| V1.8 | changes with | D4.6, L123.n1 (S1) | D4.6 S1; L123.n1 S1 | the families' form is unchanged; their extensions empty | yes |  |
| V1.8 | moves | nothing in (E) | — | Slc_j → families → not (E) | yes (FC30 run) |  |
| V2.1 | moves | Dependence (D6.5), a conjunct of (E) | D6.5 S2 | Dependence stops reading Γ; "commitments that do no work" (L313, S2) become accounts | yes |  |
| V2.1 | changes with | D7.2 routes (S), L289 FROZEN | D7.2 FROZEN; L289 line: FROZEN | ∅ can enter S (contrast with no commitments); frozen L293.s1, L299.s1 still readable, but the frozen examples L307/L309… | partly — computing S under V2.1 on L307/L309's set systems… | names a FROZEN item as changing with it |
| V2.1 | constrains | L275.n1 (S2) | L275.n1 S2 | the unrealizable-contrast case still fails (contrast must sit at a pair of C, FC29) | yes |  |
| V2.2 | blocks | L311.s2 FROZEN ("(B) records the collective contribution") | L311.s2 FROZEN | under V2.2 no collective block witnesses Dependence, so (B)'s collective case and (E) come apart at the infinitary cand… | yes |  |
| V2.2 | constrains | L299.s1 FROZEN (a block critical while no singleton is) | L299.s1 FROZEN | readable (about S), but such a candidate now fails (E) | yes |  |
| V2.2 | changes with | D10.4/D10.6 (S4's claims read problems) | D10.4 FROZEN; D10.6 S2 | fewer problems posed, none of the second kind from collective candidates | yes | names a FROZEN item as changing with it |
| V2.3 | blocks | L329.s3 FROZEN (identification, (I1)) + E2 | L329.s3 FROZEN; E2 S2 | under V2.3 no candidate meets (E) on any {1}×B contract, so the text's identification accounts (L331.s2 "This is an acc… | yes | E2 middle (S2) |
| V2.3 | changes with | D3.3 (S1, identification contracts) | D3.3 S1 | S1's contract classification would need contracts that vary only the boundary re-read | yes |  |
| V2.3 | constrains | L253.s1 FROZEN (query fixed) | L253.s1 FROZEN | untouched; only the witnessing pairs move | yes |  |
| V2.4 | blocks | — (owner decision, not a frozen item) | — | S45 removed NC1; no frozen sentence contradicts it (S106 changed them) | yes |  |
| V2.4 | moves | (E) itself; what Bearing reads | — | D9.10 (S3): Bearing(c,z,p) :⟺ Acc(ℰ_c) — the myth's slot connection (FC107, FC72.new2 (c)) stops having bearing | yes |  |
| V2.4 | changes with | D16.XV (S4), (Suff)/(Nec) L536/L538 | D16.XV S4; L536 line: S4; L538 line: S4 | Expl shrinks; both defeat sets and the (Nec) attack list change | yes |  |
| V2.5 | constrains | L195.s1 FROZEN ("a finite history H ⊆ C of pairs actually encountered") | L195.s1 FROZEN | ∅ is finite and vacuously encountered: constrains, does not block | yes | quote not verbatim: L195.s1 reads "edit–boundary pairs" |
| V2.5 | blocks | L211.s3 (S2) in effect | L211.s3 S2 | a transport declared by its author, with a stipulated population, makes the occurrence represent — against "a declared… | yes (as an effect, not a formal clash) | names a middle item |
| V2.5 | moves | Dec (D12.3), hence Expl := Acc ∧ ¬Dec and (Suff) L536 | D12.3 S2; L536 line: S4 | declared candidates with a stipulated population become explanations | yes |  |
| V2.6 | blocks | L315.s1 FROZEN (rivals: conflict "in C or outside it"), L317.s6 FROZEN (kind ii) | L315.s1 FROZEN; L317.s6 FROZEN | the kind-ii problem these define cannot exist | yes |  |
| V2.6 | moves | nothing in (E); what meeting (E) says | — | no candidate's Acc changes; problems, ETV and the (Nec) attack route through easy-to-vary change | yes |  |
| V2.7 | blocks | L315.s12 (S2) in effect | L315.s12 S2 | the bare perpetual-motion claim no longer conflicts with a candidate whose answer it allows — against S27's own example | yes | names a middle item |
| V2.7 | constrains | D8.4 (frozen): Allow_χ, Applies | D8.4 FROZEN | unchanged; only the route through Meets_ab is cut | yes |  |
| V2.7 | changes with | D8.6 (frozen, ConfG_χ) | D8.6 FROZEN | formally unchanged, but its antecedent ("every such R lies outside Allow") no longer feeds any ruling out of a single c… | yes | D8.6 FROZEN; reply: formally unchanged |
| V2.8 | constrains | D16.XV (S4): "Acc ∉ Uses(α)" | D16.XV S4 | the variant is the other reading of that phrase (I196) | yes |  |
| V2.8 | moves | (Suff)'s defeat set (L536) | L536 line: S4 | grows by arguments reaching a candidate only through another's Acc | yes |  |
| V3.1 | constrains | L397.s5 (FROZEN, S3 stretch) | L397.s5 FROZEN | X_j(ψ) = usable ∧ RO must stay a reading of the frozen words; the variant lives inside RO | yes |  |
| V3.1 | changes with | L8.s3 (S1) | L8.s3 S1 | "the claim's denial is not among its premises" states the block in Part 0; must change with the variant | yes |  |
| V3.1 | moves | (Suff) and (Nec) defeat sets (D16.XV, S4) | D16.XV S4 | ruling out by bare acceptance enters them; being an explanation (Acc ∧ ¬Dec) unmoved | yes |  |
| V3.2 | constrains | L389.s1 (FROZEN, K2 display) | L389.s1 FROZEN | Live must remain a predicate of (d;u) read by K2's ∀d | yes |  |
| V3.2 | moves | X_j and everything downstream (D9.8, S2; D10.1, FROZEN) | D9.8 S2; D10.1 FROZEN | fewer usable arguments; no conjunct of (E) moves | yes |  |
| V3.3 | constrains | L397.s5 (FROZEN) | L397.s5 FROZEN | as V3.1 | yes |  |
| V3.3 | changes with | L393.n2 (S3, same section; "a claim j has never taken up is not live for j") | L393.n2 S3 | the varied D9.6 contradicts it | yes |  |
| V3.3 | moves | (Suff)/(Nec) defeat sets; Prob_j becomes assessor-independent | — | bare claims rule out with no chooser, against S28 | yes |  |
| V3.4 | blocks | L403.s3 (FROZEN, Part X) | L403.s3 FROZEN | "A system may understand a theory in error": a use in error can no longer prepare explanatory use | yes |  |
| V3.4 | moves | Dec(t), via CT (D12.2, S2) and Build | D12.2 S2 | transports constructed only through uses-in-error become Dec; Expl = Acc ∧ ¬Dec shrinks on that class | yes |  |
| V3.4 | constrains | L526 (S4) "Build depends on … (E)" | L526 line: FROZEN/S4 | ExplUse must keep reading the claim 'Acc(ℰ)' — it does, conjoined with Acc | yes |  |
| V3.5 | changes with | L55.n3 (S1) | L55.n3 S1 | "An episode is a history in which every change C→C′ carries a provenance record (D13.8)" points at D13.8 and would be f… | yes |  |
| V3.5 | moves | Dec(t) via Episode → CT (D12.2, S2) | D12.2 S2 | more episodes → more Con → fewer Dec → more explanations | yes |  |
| V3.6 | blocks | — none found: no frozen sentence states the parts bound (L481.s3 is S3, varied with it) | L481.s3 S3 | — | yes (checked by search) |  |
| V3.6 | constrains | D12.1 (S2) writes 𝒯 = D15.8's population | D12.1 S2; D15.8 S3 | the variant must still define a set 𝒯; it does | yes |  |
| V3.6 | moves | Sel (D12.1, S2), hence Dec and Expl; Argument 3's extent (FC80, S4) | D12.1 S2; FC80 claim S4 | wider population: more Sel, fewer Dec, wider underdetermination | yes |  |
| V3.7 | blocks | L375.s2 (FROZEN) | L375.s2 FROZEN | "nonconstant dependence on the represented distinction under the declared contrasts" is part of the frozen definition t… | yes |  |
| V3.7 | moves | (P) via ProducedBy (D14.3), (EX) via ProducesVia (D14.6), reason use (D9.11 FROZEN) | D14.3 FROZEN; D14.6 FROZEN; D9.11 FROZEN | idle routes become active; no part of (E) moves | yes |  |
| V3.8 | blocks | — none: L443.s3 (FROZEN) constrains only O_ex ⊆ O; L445.s1 and L429.s1–s3 are S3 | L443.s3 FROZEN; L445.s1 S3; L429.s1 S3 | — | yes |  |
| V3.8 | constrains | L443.n1 (S3) "an explanatory aim requires a deployable account" | L443.n1 S3 | Deploy conjunct kept | yes |  |
| V3.8 | changes with | L628 (S4) and D18.1's DEP (S4) | L628 line: S4; D18.1 S4 | FC90: CreativeCriticalEpisode is "left unstated by L628", so no sentence change is forced; DEP's (EX) node loses its Cr… | unsettled whether the owner wants the Crit edge kept (S47's… | reply: settled by the owner's yes/no |
| V3.8 | moves | the class of created explanations; not (E), not Expl, not (Suff)/(Nec) | — | (EX) is a defined relation of an episode (L31.s4, S1) | yes |  |
| V4.1 | moves | Expl gains `¬Slot`; D18.1's graph: Slot becomes an ancestor of Expl/(Suff) | D18.1 S4 | the written-in test re-enters through the explainer, not the account | not settled (needs the graph recomputed) |  |
| V4.1 | changes with | L17, L49, L61, L69 (S1); the L267–L277 table (S2); FC23.new2/.new3, FC25.new2, FC30.new1… | L17 line: S1; L49 line: S1; L61 line: S1; L69 line: S1; L267 ?; L277 line: S2; FC23.new2 claim —; FC25.new2 claim S2; FC30.new1 claim S1, S4 | every sentence writing `Account(ℰ) ∧ ¬Dec(t)` and the row "a written-in answer never stops…" reverse | yes (runs above show the slot/pin facts) |  |
| V4.1 | blocks | none FROZEN | — | the rule strengthened is S4's own; the exclusion is the owner's, not a frozen line | yes |  |
| V4.2 | moves | Expl := Acc; being an explanation loses ¬Dec | — | provenance leaves explanation entirely | yes |  |
| V4.2 | changes with | L17/L49/L61/L69 (S1); D16.XV (Suff) shape; FC30.new1 | L17 line: S1; L49 line: S1; L61 line: S1; L69 line: S1; D16.XV S4; FC30.new1 claim S1, S4 | the one-defeat-set identity FC30.new1 (b) is what breaks | yes |  |
| V4.2 | constrains | FC30 ((E) takes no provenance) | FC30 claim S1, S2 | still true — Acc unchanged; only Expl moves | yes |  |
| V4.3 | constrains | D12.3/D12.4 (S2), provenance per holding | D12.3 S2; D12.4 FROZEN | whether "no record at all" is possible decides if V4.3 is vacuous or not | not settled (needs a provenance-less case computed; I90 cur… | reply marks D12.4 S2; template FROZEN |
| V4.3 | moves | Expl and (Suff)'s range | — | explanation demands positive provenance | yes |  |
| V4.3 | changes with | L17 etc. (S1); FC25.new2's reading | L17 line: S1; FC25.new2 claim S2 | the encoding table stops being an explanation, so the worked cases change role | yes |  |
| V4.4 | constrains | X_j / Out_j, D9.x (S2) | — | the widened defeat set is still assessor-relative; nothing overrides j's choice (S21) | yes |  |
| V4.4 | moves | (Suff) and (Nec) defeat sets only | — | "not using (E)" shrinks from symbol to instance; being-an-explanation unchanged | yes (FC30.new1 (h) computed both) |  |
| V4.5 | constrains | L606.s4 (S4, Argument 7), FC99 | L606.s4 S4; FC99 claim S4 | "ℰ can meet (E) on C and fail on C′" is the resource the variant trades on | yes (FC99 run) |  |
| V4.5 | changes with | L538.s1 (S4, co-varied); FC30.new1 (g); Part VII's exposure (E5 stays FROZEN, only its us… | L538.s1 S4; FC30.new1 claim S1, S4; E5 FROZEN | (Nec)'s exposed case widens from eliminative to every unpreservable-on-C candidate | not settled (needs FC62 under the varied shape) | E5 FROZEN; reply: E5 unchanged, its use changes |
| V4.6 | constrains | D5.3/I20 (S1, designation) | D5.3 FROZEN | δ's role is fixed upstream; the variant only stops reading it | yes | reply marks D5.3 S1; template FROZEN |
| V4.6 | moves | 𝔈_Θ, UU, UECS; nothing in (E) | — | universality's domain loosens from designation | not settled (reach unknown without a search) |  |
| V4.7 | blocks | L495.s1 FROZEN (barriers: "every admitted, non-question-begging enabling condition leaves… | L495.s1 FROZEN | with NQB out of Enable, the barrier sentence can no longer be read through Enable: the two "non-question-begging" condi… | yes |  |
| V4.7 | moves | UECS only | — | no conjunct of (E), no defeat set, no Expl reads Enable | yes |  |
| V4.8 | constrains | D12.1 surv (S2); L574.s2 FROZEN | D12.1 S2; L574.s2 FROZEN | surv supplies the dropped conjunct; L574.s2 (relations independent per pair) supports the alteration step and does not… | yes |  |
| V4.8 | moves | (Prov)(i) from closed-by-definition to open | — | "what would rule the class out" changes content | not settled (needs FC80 re-run with the co-varied (Prov)(i)) |  |
| V4.8 | changes with | L572.s2, L574.n4, L576.s1/.s4 (S4, co-varied); FC80 (S4) | L572.s2 S4; L574.n4 S4; L576.s1 S4; FC80 claim S4 | Argument 3's wording and consequence shift together | yes |  |

Edges a reply names in prose, unsettled: V2.1 — whether FROZEN L309.s1 (interference: the full candidate fails (E) although a subset meets it) still holds under contrast-only Dependence (needs S recomputed on its set system). V4.4 — whether any FROZEN item blocks it; nearest L556.s3 [FROZEN]; "an owner ruling on whether citing a rival's being an account is 'using (E)'" would settle it.

## 5. The owner's decisions each variant names, and the inventions it rests on

As the reply gives them ((a)'s last column, (b), (c), (e)). "New" = not a registered invention; the reply makes it here.

| id | decisions named (reply) | inventions (reply) |
|---|---|---|
| V1.1 | none | I14 (other choice: the projection of Sol_D, the variant); I138 kept |
| V1.2 | none | I04 (the k ≠ j clause); I122 kept |
| V1.3 | none | I06 (R-i, the registered other choice, made the one reading) |
| V1.4 | none | I163 (other choices: the pre-round-4 reading, the variant; "C holds edits to the observed value"; an exists-pair reading with no a ≠ 1) |
| V1.5 | none | I127 (other choices: two values, the variant; declared defined by a stipulation event) |
| V1.6 | S21, in tension ("Notice I never once claimed what must happen … the problem may be ill posed") | I76 (other choices: no Desc, as now; Desc replaced by conditions on (D, C, Q)) |
| V1.7 | none | I27 (other choice: the complement, the variant); I85 (the program's default scope) made a definition |
| V1.8 | none | I125 (other choices: Alt_j, the variant; Alt_j ∖ ⋃_{asg(v)≠j} Set_v) |
| V2.1 | none | I21; I22/I25 |
| V2.2 | none | I21; I22/I25; new: "a nonempty block" read as "a singleton" (other choices: nonempty, as now; a block critical in some route W ∈ S) |
| V2.3 | none | I21; I22/I25; I26 kept; new: "a pair of C" read as "a pair with a ≠ 1" (other choices: any pair of C, as now; pairs other than (1,b0)) |
| V2.4 | rejected by S45 ("Yes, take the test out"), with S44 | I136/I184 (slot quantifier 'every'; FC23.new1 (h): the same under all four) |
| V2.5 | departs in effect from S41 Q2 ("No, not if just declared") | I52 (a third choice named: H nonempty and proper in C) |
| V2.6 | departs in effect from S20 ("If two discovered variations fit, that constitutes a problem") | I21 (read by Conf) |
| V2.7 | rejected by S27 (perpetual motion enough to trigger a conflict) | I137 (other choice: no existence clause, FC52's first part) |
| V2.8 | none | I196 (instance reading; the symbol reading is the default) |
| V3.1 | rejected by S23 (an argument is reasons why this and not that) | I39 (other choice: logical equivalence, excluded by L397.n14) |
| V3.2 | none | I40 (other choice: any step of the argument, FC69) |
| V3.3 | rejected by S28, with S41 Q23; S27's split named in the trace | I166 (the variant is its registered other choice, FC72.new1 (a)) |
| V3.4 | none (blocked by L403.s3 [FROZEN]) | I178 (the variant is its registered third choice) |
| V3.5 | none (S41 Q6 named: it dropped "in which contracts change", not the record) | I165/I174 (both keys deleted) |
| V3.6 | none | I158 (the variant is its registered other choice) |
| V3.7 | none | I46 (I149, I150 kept) |
| V3.8 | in tension with S47 read strongly ("the maths asks for nothing"); "flag for the owner's yes/no" | I59, I180 kept; I152, I190/I192 |
| V4.1 | rejected by S45 | the four readings of Slot (D6.3; FC23.new2); trace the same under all four |
| V4.2 | rejected by S41 Q2 ("No, not if just declared") | none named |
| V4.3 | none ("no owner decision covers a transport with no provenance record") | D12.3/D12.4, I90 (other choice: provenance total, then V4.3 changes nothing) |
| V4.4 | none as a decision; tension with S23's gloss of argument | I196 |
| V4.5 | none directly | new: preservability read at contracts C′ other than the question's own (other choice: only declared contracts of the question) |
| V4.6 | none | I75/I183 (other choice: δ the designation for every Acc-witness) |
| V4.7 | none as a decision | I154 (idle here: both readings deleted) |
| V4.8 | none | new: (Prov)(i)'s middle conjunct read through D12.9 (other choice: kept inline; then only Argument 3's wording changes) |

## 6. Flags (rule 4)

Scope: "as written" = the variant names, among the items it varies, an item marked FROZEN or of another section; "in effect" = its statement is on its own item but its formula rewrites what an item of another mark states. Not implemented while flagged (rule 4); for the orchestrator to decide.

| id | out of scope | adds prose (S40) | moves where values are placed | why, in one line |
|---|---|---|---|---|
| V1.6 | in effect: D6.7 [S2] (the formula "⇒ ∀ℰ ¬Acc(ℰ,p)" adds a condition on Acc); its trace instead changes being an explanation (L17, L49, L69 [S1]; D16.XV [S4], named "changes with") | **yes**: "a new sentence in Part III", given as a formula; S40 allows deletions and a sentence replaced by its formal statement, not a new sentence | no | formula and trace are two different variants |
| V1.7 | in effect: D3.5 [FROZEN] ("Σ is a declared input naming Excl(Σ)"); the reply's own edge: blocks | no | no (turns a declared input, the scope, into a definition; not the appraisal relation, the aims or a weighting) | defines a symbol a FROZEN definition makes an input |
| V2.8 | as written: names L315.s7 [FROZEN] among the items varied; its trace is D16.XV's "not using (E)" read at the instance (I196, S4), which is V4.4's variant | no | no | the formula on D9.8 (ruling out needs Acc(ℰ) ∈ Uses(α)) and the trace (arguments using only Acc(ℰ′) enter (Suff)'s defeat set) describe different changes |

No other variant names or rewrites a FROZEN item or another section's item; none adds prose; none varies the appraisal relation 𝒩 (L31, L455, L518), the aims O and P (L441, D14.1) or a weighting, or makes (E) or being an explanation read one of them (V3.8 keeps Repair_{O,P} as it is).

Further notes, not flags:

- **Blocks a FROZEN item, by the reply's own edge** (in scope, but by the brief "cannot stand beside" it; the template: "a variant of the definition must still be a reading of the frozen words"): V1.1 (D4.4), V1.2 (L103.s2), V1.7 (D3.5), V1.8 (L347.s2), V2.2 (L311.s2), V2.3 (L329.s3), V2.6 (L315.s1, L317.s6), V3.4 (L403.s3), V3.7 (L375.s2), V4.7 (L495.s1).
- **Names a FROZEN item as "changes with"**: V1.5 (E8, which the reply marks S2), V2.1 (D7.2, L289), V2.2 (D10.4); V2.7 (D8.6) and V4.5 (E5) say the frozen item stays as it is.
- **Sentences varied with it, new form not given** (S40 wants a deletion or the formal statement): V1.5 (L155.s2, L155.s5), V2.1 (L255.n2), V2.6 (L315.n2), V2.7 (L315.n11), V2.8 (L315.s6), V3.1 (L397.n14, L397.s16), V3.6 (L481.s3), V4.5 (L538.s1), V4.6 (L497.s1), V4.8 (L572.s2, L574.n4, L576.s1, L576.s4); all middle, each of its own section. (V2.4's L261.n1 is the display (E), and V3.8's L445.s1 is (EX)'s display: their new form is the variant's formula.)
- **Changes with, another section, named by the reply**: V1.1 (L233.s1 S2; L556.n2 S4), V1.2 (E1 S2), V1.4 (E1, L271.s2, L325.n6: S2), V1.5 (D13.8 S3; D16.4, L544 S4), V1.6 (D16.XV S4), V2.3 (D3.3 S1), V2.4 (D16.XV, L536, L538: S4), V3.1 (L8.s3 S1), V3.5 (L55.n3 S1), V3.8 (L628, D18.1: S4), V4.1–V4.3 (L17, L49, L61, L69: S1; V4.1 also the L267–L277 table, S2).

## 7. Same axis, across sections (cross-reference; nothing ruled)

| axis | variants |
|---|---|
| the written-in test | V2.4 (NC1 back in (E), D6.7) · V4.1 (¬Slot in being an explanation, D16.XV); both named against S45 |
| "not using (E)" at the symbol or the instance (I196) | V2.8 (by its trace) · V4.4 |
| how far Dec(t) reaches (the ¬Dec(t) of being an explanation) | V2.5 (Sel with H = ∅) · V3.4 (ExplUse needs Acc) · V3.5 (episode without records) · V3.6 (population without the parts clause) · V4.2 (¬Dec dropped) · V4.3 (Sel ∨ CT required) |
| provenance of a contract, beside that of a transport | V1.5 (ρ_p) · V4.3 |
| ruling out by a claim taken as given | V3.1 (RO's block) · V3.2 (Live) · V3.3 (premise alone) · V2.7 (ConfCl) · V2.8, V4.4 (defeat sets) |
| Dependence (D6.4) | V2.1 · V2.2 · V2.3 |
| the identification contract C_id = {1}×B | V1.4 (Ident) · V2.3 (a ≠ 1) |
| (F1)'s component side | V1.1 (Sol_N) |
| inputs made conditions of (E) | V1.6 (Desc's defects) · V1.7 (Excl(Σ)) |
| the families of signatures (no reach into (E), by the replies) | V1.2 · V1.3 · V1.8 |
| the class, universality, genesis | V4.5 (Nec) · V4.6 · V4.7 · V4.8 · V3.8 ((EX)) · V3.7 (active route) |

## 8. Items each reply names as not varied, and why (its (d)), with the template's marks

| section | items |
|---|---|
| S1 | L17.s1–L17.n2 [S1] (the target; left to S4's D16.XV); L11.s1 [S1] (a prose variant is what S40 refuses); L49.n3, L69.n3 [S1] (one definition of Expl; Q2 not the reply's to move); L119.s3–L119.n5 [S1] (kinds; D4.2–D4.4 [FROZEN] carry them); L159.s3 [S1] (the owner's words, S25–S27); D4.6 [S1] (read by nothing in (E)); L141.n3, L151.n6 [S1] and "L151.n7" (the template's id is L151.s7 [S1]) (D3.2, D3.7 [FROZEN] carry them) |
| S2 | D5.7 (fidelity's extent is "section 3's" L630; the template marks L630.s1 S4); D6.8, D6.9; D7.4 (settled in round 4); D8.new1 (I36, FC44); D8.3 (Offered: varying it would invent content S20 forbids); D10.3, D10.6 (K3 fixes it); D11.2; D12.2, D12.7, D12.8 (S47 settled what Con asks); E1, E2 |
| S3 | D9.2 (V3.3 covers it; reversing Q23 was round 2's rejected reading, I88); D9.9 (K3: moving it moves a frozen pair's reading, L369.s1–s2); D11.3 (uniqueness of the T′ fixed point, hence "exactly one of three"); D13.7 (fixed by L427.s3 [FROZEN]); D14.1 (blocked by L441.s2 [FROZEN]); D15.1, D15.2 (pointing them at (E) would move physical possibility into explanation, against S25) |
| S4 | D16.5 (pure extensions); E9 (the owner's worked case; its natural variant "left to Part B"); D18.1 (the map itself); D18.2 (a constraint every variant must respect; V4.3 "not obviously φ-invariant"); (Elim) and (QF) in D16.XV (their terms are undefined; formalizing them is new content) |

Marks: every definition named in S2's row is S2, in S3's row S3, in S4's row S4 (the template's lists); the frozen items named are as marked above; L427.s3, L441.s2, L369.s1, L369.s2 are FROZEN.

Middle definitions no variant varies (from §2 against the template's lists): S1 D4.6 (1 of 9); S2 D5.7, D6.3, D6.5, D6.8, D6.9, D7.4, D8.new1, D8.3, D10.3, D10.6, D11.2, D12.2, D12.3, D12.7, D12.8, E1, E2 (17 of 23; D6.3, D6.5, D12.2, D12.3 are read or moved by traces, not varied); S3 D9.1, D9.2, D9.9, D9.10, D11.3, D13.7, D14.1, D15.1, D15.2, D15.5 (10 of 18); S4 D16.5, E9, D18.1, D18.2 (4 of 8). Of the 519 middle sentences, the variants name 17 as varied with them (§2: L155.s2, L155.s5, L255.n2, L261.n1, L315.n2, L315.n11, L315.s6, L397.n14, L397.s16, L481.s3, L445.s1, L538.s1, L497.s1, L572.s2, L574.n4, L576.s1, L576.s4), and V2.5 names line L195 with no sentence id.

## 9. Quotations compared (rule 14)

Every quotation in double quotes was searched for in the template (text and core), the text by line, the committed printouts and the decisions. Found verbatim, or with only spacing, LaTeX or True/✓ differences, unless listed:

| reply | quotation | attributed to | found |
|---|---|---|---|
| 1 (V1.2 edge) | "each setting replacing its component" | E1 | not verbatim: E1 reads "(each replacing its component, D2.1)" |
| 2 (V2.5 edge) | "a finite history H ⊆ C of pairs actually encountered" | L195.s1 | not verbatim: L195.s1 reads "of edit–boundary pairs actually encountered" |
| 2 (V2.6 trace) | "conflict only in the south, outside the Greeks' contract: rivals True; kind ii" | FC72.new2 (b) | condensed: the printout reads "they conflict only in the south, outside the Greeks' contract: rivals, and for an assessor who rules out neither a problem of the second kind (D10.2); …" |
| 3 (V3.3 row) | "that ruling out is a choice that was made, not something the claim does by itself" | S28 | mixed: S28's words are "That "ruling out" is a choice that was made."; "not something the claim does by itself" is the text's (L8.n9, L397), not the owner's |
| 3 (V3.8 row) | "the maths asks for nothing" | S47 | the brief's gloss; the owner's words: "The math doesn't ask for anything." |
| 4 (V4.2 trace) | "L536 False; L17 (S41) False" | FC30.new1 (a) | a middle clause dropped with no ellipsis: "L536 False; L17 as text 104 words it True; L17 (S41) False" |
| 4 (V4.7 edge) | "every admitted, non-question-begging enabling condition leaves the capability unavailable" | L495.s1 | not verbatim: "leaves the relevant capability unavailable" |
| 4 (V4.8 row) | "what would rule the class out" | Part XV's title | the title is "What would rule this class out" |

Quotation marks around the replies' own phrases ("no population and no trace", "a singleton", "did work", "only at ξ′", "no record at all", "answers the question it designates", Desc′'s wording) are not quotations of the text and were not compared.

## 10. Words of S23, and "model", in the replies' own glosses (rule 13)

No variant's statement holds a word S23 lists. In the replies' glosses: "derivable" (reply 1, V1.7 trace), "derivation" (reply 2, V2.2 and V2.3 traces), "true" as a gloss (reply 2, unsettled edge; reply 3, V3.4 trace, "Con true"; reply 4, V4.2 edge, "still true"), "establishing Expl(E_rev)" (reply 4, V4.5 trace, twice), "supports the alteration step" (reply 4, V4.8 edge). "Model" never names a candidate: reply 1 quotes the printout's "which the model does not build" and says "the modeller" of the person who narrows a contract; reply 4's "models" are the program's small structures. True/False as program output is not counted.

## 11. Unsure

- The scope flags follow the template's marks and the variant's own statement; "in effect" (V1.6, V1.7) is this agent's reading of what the formula rewrites, left to the orchestrator.
- V1.6's formula (on Acc) and trace (on being an explanation), and V2.8's formula (on D9.8) and trace (on D16.XV), are tabulated as the replies give them; which of each pair is the variant is not settled here.
- "Old" statements are the template's clause, not always its whole definition: the rest of each definition (change marks, notes, other clauses) is unchanged by the variant, as the replies state.
- Counts of "moves" follow each trace's own words; where a trace names (E) and not being an explanation, the latter is recorded "not stated".
- Whether the replies ran what they say they ran was not checked against their stream or guard files (not opened, rule 2); their quoted outputs were compared with the committed printouts (§9), which were made at scale 4 with cap 45 — the replies ran at default settings (reply 2) or scale 4, cap 40 (reply 4).

Tabulated by one Opus 5.5 agent under rule 4, 28 September 2026. Nothing ruled.
