# S109 Part B round 1 - how explanation changes in meaning and scope

*Rule 6 of `S109 Part B round 1 - how the replies will be read, written before sending.md`. The one Opus 5.5 agent of decision S56 (effort high), 29 September 2026. Built by `computation/map/s109b_map_build.py` from the four "section Bn - variants computed" files (and their hand record `computation/map/s109b_data.py`, the scope runs and the whole-suite results). Part A's map (`S108 Part A round 2 - the dependency map, after the cross-examination.md` / `.json`) is never written; edges that join it cite its ids. Nothing here is applied; nothing is ruled. "Candidate" or "explanation" for what the theory judges; "model" only for the program (S43).*

## 0. What is mapped

Being an explanation = Account(ℰ) ∧ ¬Dec(t), Account = (E) = (F1) ∧ (F2) ∧ (A) ∧ Dependence ∧ NonVacuous; (Suff) and (Nec) are the claims about it, read through their defeat sets X_j (D16.XV). **Meaning** = the changed formal statement, old beside new, of each part that moves. **Scope** = which things count, computed off against on: the text's worked cases (27), the owner's four cases (the two-part sign and the weathervane under the three readings of the owner's change, the student's copy FC30.new1 (d), the bridge FC84.new1 (a1), (a2)), the made-up candidates (17,280 generated at scale 4, FC-E1-E5, CT1-CT8; chains of up to three holdings for Dec), and the whole claim suite (142 claims) per variant and reading. 34 variants: 31 implemented as switches (PB2.8, PB2.9, PB4.3 with no code change, PB1.5 with no reader), PB3.8 flagged out (no formal statement), PB4.4 flagged out as written and computed as PB4.4′ restated on D9.8. The three class-a carry-overs are computed (V1.7 as PB1.1, R2V2.7 as PB2.1, V2.8's L315.s7 part as PB4.1); of class b, R2V1.4, R2V1.7, R2V1.8, R2V1.9, R2V2.4 (as PB1.5, PB1.4, PB1.3, PB1.2, PB3.1); R2V1.2 was not taken up.

## 1. Per variant

| id | free item(s) | kind | meaning: part (old → new) | scope (computed) | claims that move | edges (computed / contradicted / claimed only) |
|---|---|---|---|---|---|---|
| PB1.1 | D3.5 | replace | (E): NonVacuous: Sol_D(1,b0) ≠ ∅ ∧ (A×B)∖C ⊆ Excl(Σ), Excl(Σ) a declared input (I27) → Sol_D(1,b0) ≠ ∅ (Excl(Σ) := (A×B)∖C, so Stated holds of every question) | the hand case with Excl(Σ) = ∅ enters | none | 2 / 0 / 2 |
| PB1.2 | D3.1 | strengthen | domain of (E), Expl, (Suff), (Nec): p a question: C ⊆ A×B, (1,b0) ∈ C → … ∧ ∀(a,b) ∈ C: Θ_admits(a); a contract holding an edit Θ does not admit names no question | Θ strict: 36 cases and 813 generated leave (the sign and vane as edits or mixed) | FC101, FC22, FC23, FC23.new1, FC23.new2, FC23.new3, FC23.new5, FC25.new2, FC26, FC27.new1, FC30.new1, FC34, FC42.new1, FC62, FC63, FC72.new2, FC90.new1, FC99 | 1 / 0 / 2 |
| PB1.3 | D3.2 | replace | domain of (E); what (A) and Contrast compare: Q(O,a,b;δ) ∈ Y_p ∪ {⊥}, Y_p free (I21) → Y_p := X_δD: a query with an answer outside X_δD ∪ {⊥} names no question | C_id leaves | none | 1 / 0 / 2 |
| PB1.4 | D4.2 | replace | none of the five parts: j ~_C j′ :⟺ ∃β … → j ~_C j′ :⟺ V_j = V_j′ (ordered) ∧ sig_C(j) = sig_C(j′) | no candidate moves (nothing in the definition reads it) | FC05, FC103.new1 | 2 / 0 / 0 |
| PB1.5 | L155.s6 | replace | none of the five parts: Found(p) requires ρ_p = constructed → Found(p) :⟺ ρ_p ∈ {selected, constructed} | no candidate moves (nothing in the definition reads it) | not run | 0 / 0 / 2 |
| PB1.6 | L103.s1, D1.3 | replace | (E): Dependence (NC2's Lost, through D6.1's E−G): E−G: every component of G imposes the full relation → E−G: every component of G imposes the empty relation; so Sol_{E−G} = ∅ and Ans_{E−G} = ⊥ wherever G's footprints are nonempty | 61 generated enter | FC01 | 2 / 0 / 1 |
| PB1.7 | L141.s2, D3.1 | strengthen | domain of (E): (1,b0) ∈ C → (1,b0) ∈ C ∧ ∃(a,b) ∈ C: a ≠ 1 | 8 cases (the sign and vane as boundaries, C_id) and 186 generated leave | FC25.new2 | 1 / 0 / 1 |
| PB1.8 | L115.s1, D4.1 | strengthen | none of the five parts: sig_C(j) = {(a,b,L_j(a,b))} → sig⁺_C(j) = {(a,b,L_j(a,b),Sol_D(a,b)↾V_j)} | no candidate moves (nothing in the definition reads it) | FC05 | 2 / 1 / 0 |
| PB1.9 | L113.s1, D4.1, D4.2, D4.3, D4.4 | replace | none of the five parts: kinds: classes of ~_C → kinds: classes of ~_{A×B} | no candidate moves (nothing in the definition reads it) | FC04, FC05, FC16 | 1 / 0 / 1 |
| PB2.1 | L189.s2 | replace | Dec (Sel's Faithful_H, Held, Rep, T′) and Expl: Faithful_C := F1 ∧ F2; Faithful_H without (A); Viol narrow → Faithful_C := F1 ∧ F2 ∧ A; Faithful_H with (A) at H; Viol := Viol⁺ | FC104.new1 (b)'s selection becomes declared | FC104.new1, FC67 | 4 / 0 / 0 |
| PB2.2 | D5.5, L241.s1 | weaken | (E): (F2); Dec through Faithful_H: F2_C := F2eq_C ∧ Hom(τ) → F2_C := F2eq_C | 1 worked case and 11 generated enter; the relabeling candidate on a Sel history | FC27.new1, FC77 | 2 / 0 / 1 |
| PB2.3 | D5.4 | strengthen | (E): (F1): ∀k ∈ Γ: proj^λ Sol_λ(k) = L_k → ∀k ∈ J_E: … | 214 generated leave | FC42.new1, FC80.new1 | 1 / 0 / 1 |
| PB2.4 | D5.6, L249.s1 | weaken | (E): (A): ∀(a,b) ∈ C: Ans_E = Ans_p (⊥ = ⊥) → ∀(a,b) ∈ Det_C: Ans_E = Ans_p | meaning moves, scope unchanged on every case computed | FC109, FC21, FC96 | 2 / 1 / 1 |
| PB2.5 | D6.2 | strengthen | (E): Dependence: NC0 (true) ∧ NC2 → NC0′ ∧ NC2, NC0′ :⟺ no background component pins δ_E to Ans_p at a pair of C | bg: 1 case, 149 generated leave; bg-input: 12 generated leave | FC23.new1, FC62 | 1 / 0 / 1 |
| PB2.6 | D6.6 | weaken | (E): NonVacuous: Sol_D(1,b0) ≠ ∅ ∧ Stated(C,Σ) → Sol_D(1,b0) ≠ ∅ | the hand case enters (as PB1.1) | none | 2 / 0 / 0 |
| PB2.7 | D5.6 | re-order a dependence | (E): (A): A_C(ℰ) → A_C(ℰ) ∧ NC1(ℰ) (no answer slot, D6.3) | 20 to 28 cases, 855 to 946 generated leave (as C6) | FC23, FC23.new1, FC23.new2, FC23.new5, FC25.new2, FC27.new1, FC72.new2 | 3 / 0 / 0 |
| PB2.8 | L311.s2, D7.3 | weaken | none of the five parts: CB(B;W) :⟺ ∅ ≠ B ⊆ W ∧ W ∈ S ∧ W∖B ∉ S → … ∧ B finite | no candidate moves (nothing in the definition reads it) | not run | 0 / 0 / 1 |
| PB2.9 | D5.1 | replace | (E): what (F1), (F2) read (the transport): π: X_D ⇀ X_E on Sol_D (I16) → π: X_D → X_E total | meaning moves, scope unchanged on every case computed | not run | 0 / 0 / 1 |
| PB3.1 | D12.4 | replace | Dec (inheritance, D12.4): provenance per part; a binding newly built by the copier gets its own value → a holding reached by a copy of a carrier's whole content inherits prov(t,o) whole | the student's copy stops being declared | FC30.new1 | 1 / 0 / 1 |
| PB3.2 | D12.5, L207.s1 | weaken | Dec (Sel's exclusion): Rep_ℓ(o,c) :⟺ ∃t [Faithful ∧ (Sel ∨ Con)]; Sel's exclusion reads Rep at o′ ≺ o (T′) → Rep := Held; Sel's exclusion reads Held at o′ ≺ o (T) | 10 chain outputs become declared | FC98 | 2 / 0 / 0 |
| PB3.3 | L195.s1, L195.s5 | strengthen | Dec (Sel): Sel(t;𝒯,μ,H) as D12.1 → … ∧ C ∩ Occ(h) ⊆ H | every Sel-history case (44 cases, 999 generated) becomes declared | FC102.new1, FC12.new1, FC12.new2, FC30.new1, FC83 | 2 / 0 / 1 |
| PB3.4 | L199.s1, L199.s3 | re-order a dependence | Dec (the history): Dec(t,o_t) read on h(t,o_t) → read on h∪(t) = ∪{h(t,o): t held at o} | the student's copy and 82 chain outputs stop being declared | FC12.new1, FC12.new2, FC30.new1, FC83, FC84.new1, FC98, FC98.new1 | 2 / 0 / 0 |
| PB3.5 | D11.5, L217.s2 | weaken | Dec (Sel's H-clause): H ⊆ Occ(h) (Occurs a primitive through Θ) → H admitted (Occurs := admitted ∧ actual) | meaning moves, scope unchanged on every case computed | none | 1 / 0 / 0 |
| PB3.6 | D11.1, L169.s1 | strengthen | Dec (what histories are built from): Occ: physically located carriers → Occ: those inside the declared boundary β | the student's copy stops being declared (on that reading) | FC30.new1 | 1 / 0 / 1 |
| PB3.7 | D13.4, L169.s3 | replace | none of the five parts (New, Origin): d ≡_ℓ c :⟺ faithful transports both ways → d ≡_ℓ c :⟺ Ans_d = Ans_c on C_c | no candidate moves (nothing in the definition reads it) | none | 0 / 0 / 1 |
| PB3.8 | L225.s4 | drop | none: — → — | flagged out, not computed | not run | 0 / 0 / 0 |
| PB4.1 | L315.s7 | replace | none of the five parts (Out_j): ℰ ruled out for j :⟺ X_j('Acc(ℰ)') ≠ ∅ → … ∃α ∈ X_j with Acc(ℰ) ∈ Uses(α) | meaning moves, scope unchanged on every case computed | FC56, FC72, FC72.new1 | 1 / 0 / 1 |
| PB4.2 | D9.5 | weaken | (Suff), (Nec): X_j through Usable: Scope_j(u) :⟺ C_u ⊆ C_j(u) ∧ ℓ_u = ℓ_j(u) ∧ β_u = β_j(u) → Scope_j(u) :⟺ C_u ⊆ C_j(u) | FC56 (a″)'s coarse-grain assessor's argument becomes usable | FC56 | 1 / 0 / 0 |
| PB4.3 | D9.3 | weaken | (Suff), (Nec): X_j through Prem: Prem(u) := children(u) → Prem(u) := the premises Form(u) uses | meaning moves, scope unchanged on every case computed | not run | 0 / 0 / 1 |
| PB4.4 | L397.s13 | strengthen | (Suff), (Nec): X_j: X_j(φ) := {α: Usable_j(α) ∧ RO(α,φ)} → … ∧ every premise of α taken as given has a held explanation | X_j empty everywhere: nothing ruled out, the defeat sets empty | FC23.new2, FC30.new1, FC47.new1, FC56, FC72, FC72.new1, FC72.new2 | 2 / 0 / 0 |
| PB4.5 | L383.s1 | strengthen | none of the five parts: a criticism occurrence may lack Bearing → Occ_criticism(c) ⇒ Bearing(c,z,p) | no candidate moves (nothing in the definition reads it) | FC74, FC76 | 1 / 0 / 0 |
| PB4.6 | L385.s1, D9.11 | weaken | none of the five parts: UsesReason asks an image port on an active route → that clause dropped | no candidate moves (nothing in the definition reads it) | none | 1 / 0 / 0 |
| PB4.7 | L546.s1 | strengthen | none of the five parts: list with Arguments 1-3 → list with Arguments 1-10 | no candidate moves (nothing in the definition reads it) | none | 1 / 0 / 0 |
| PB4.8 | D10.1, L317.s1 | weaken | none of the five parts: Prob_j :⟺ Riv ∧ NotOut_j ∧ NotOut_j → Prob :⟺ Riv | no candidate moves (nothing in the definition reads it) | FC47.new1, FC72.new2 | 1 / 0 / 0 |

## 2. Per part of the definition

| part | free items its meaning was found to turn on (variants) | free items its scope was found to turn on (computed moves) |
|---|---|---|
| (E) | D3.5 (PB1.1); D3.1 (PB1.2); D3.2 (PB1.3); L103.s1, D1.3 (PB1.6); L141.s2, D3.1 (PB1.7); D5.5, L241.s1 (PB2.2); D5.4 (PB2.3); D5.6, L249.s1 (PB2.4); D6.2 (PB2.5); D6.6 (PB2.6); D5.6 (PB2.7); D5.1 (PB2.9) | D3.5 (PB1.1: the hand case with Excl(Σ) = ∅ enters); D3.1 (PB1.2: Θ strict: 36 cases and 813 generated leave (the sign and vane as edits or mixed)); D3.2 (PB1.3: C_id leaves); L103.s1, D1.3 (PB1.6: 61 generated enter); L141.s2, D3.1 (PB1.7: 8 cases (the sign and vane as boundaries, C_id) and 186 generated leave); D5.5, L241.s1 (PB2.2: 1 worked case and 11 generated enter); D5.4 (PB2.3: 214 generated leave); D6.2 (PB2.5: bg: 1 case, 149 generated leave; bg-input: 12 generated leave); D6.6 (PB2.6: the hand case enters (as PB1.1)); D5.6 (PB2.7: 20 to 28 cases, 855 to 946 generated leave (as C6)) |
| Dec | L189.s2 (PB2.1); D5.5, L241.s1 (PB2.2); D12.4 (PB3.1); D12.5, L207.s1 (PB3.2); L195.s1, L195.s5 (PB3.3); L199.s1, L199.s3 (PB3.4); D11.5, L217.s2 (PB3.5); D11.1, L169.s1 (PB3.6) | L189.s2 (PB2.1: FC104.new1 (b)'s selection becomes declared); D5.5, L241.s1 (PB2.2: the relabeling candidate on a Sel history); D12.4 (PB3.1: the student's copy stops being declared); D12.5, L207.s1 (PB3.2: 10 chain outputs become declared); L195.s1, L195.s5 (PB3.3: every Sel-history case (44 cases, 999 generated) becomes declared); L199.s1, L199.s3 (PB3.4: the student's copy and 82 chain outputs stop being declared); D11.1, L169.s1 (PB3.6: the student's copy stops being declared (on that reading)) |
| X_j (the defeat sets of (Suff), (Nec) only) | D9.5 (PB4.2); D9.3 (PB4.3); L397.s13 (PB4.4) | D9.5 (PB4.2: FC56 (a″)'s coarse-grain assessor's argument becomes usable); L397.s13 (PB4.4: X_j empty everywhere: nothing ruled out, the defeat sets empty) |
| Expl | everything under (E) and Dec (Expl := Account ∧ ¬Dec(t)) | everything under (E) and Dec |
| (Suff), (Nec) | everything under (E) and Dec (their antecedent), and X_j's items | everything under (E) and Dec (FC30.new1's defeat-set parts move with PB1.2, PB3.1, PB3.3, PB3.4, PB3.6), and X_j's (PB4.2, PB4.4′) |

Varied, meaning of a part moved, scope unchanged on every case computed: PB2.4 (D5.6, L249.s1); PB2.9 (D5.1); PB3.5 (D11.5, L217.s2); PB4.3 (D9.3); PB4.1 (L315.s7).

Varied, moving neither the meaning nor the scope of any of the five parts (what moves is kinds, Found, routes, New, criticism, problems or the class's list; claims move as §1 says): PB1.4 (D4.2); PB1.5 (L155.s6); PB1.8 (L115.s1, D4.1); PB1.9 (L113.s1, D4.1, D4.2, D4.3, D4.4); PB2.8 (L311.s2, D7.3); PB3.7 (D13.4, L169.s3); PB4.5 (L383.s1); PB4.6 (L385.s1, D9.11); PB4.7 (L546.s1); PB4.8 (D10.1, L317.s1).

Not varied: see §5.

## 3. Edges

| variant | kind | item | standing | Part A id | why |
|---|---|---|---|---|---|
| PB1.1 | moves | X:NonVacuous, X:(E) | computed | e1.51 | the hand case: NonVacuous F → T, Acc F → T |
| PB1.1 | constrains | D6.6 | computed | e1.49 | NonVacuous's second conjunct holds of every candidate under PB1.1 |
| PB1.1 | blocks | L43.s4, L159.s1 (FROZEN) | claimed only | e1.48 | the requirement that the exclusion be stated has nothing to read |
| PB1.1 | changes with | D0.2 (FROZEN; I27) | claimed only | – | Excl leaves the primitives |
| PB1.2 | blocks | L159.s3, L49.s4 (FROZEN) | claimed only | – | admitting a change is not a claim that it can be carried out |
| PB1.2 | constrains | Θ (D0.1) | claimed only | – | Θ_admits must be read of a bare edit |
| PB1.2 | moves | X:(E) (its domain), X:Expl | computed | – | Θ strict: 36 cases, 813 generated leave |
| PB1.3 | constrains | D3.3 (FROZEN) | claimed only | – | Ident and Obst have no question |
| PB1.3 | moves | X:(E) (its domain) | computed | – | C_id leaves |
| PB1.3 | changes with | E2, E4, E9 (FROZEN) | claimed only | – | their non-port queries name no question |
| PB1.4 | changes with | D4.3 | computed | r2e1.34 | FC103.new1 (b): k1 and k2 no longer of one kind |
| PB1.4 | moves | nothing in the definition; Arguments 1-2's claims | computed | – | FC05, FC103.new1 |
| PB1.5 | changes with | D3.4 (FROZEN) | claimed only | r2e1.30 | Found's clause |
| PB1.5 | constrains | (QF) (L544) | claimed only | – | Found is (QF)'s subject |
| PB1.6 | moves | X:Dependence, X:(E) | computed | – | 61 generated enter |
| PB1.6 | changes with | D6.1, D7.1 (restriction) | computed | – | FC-E1's restriction to {k} answers ⊥ |
| PB1.6 | constrains | D3.6 (FROZEN) | claimed only | – | an absent port |
| PB1.7 | moves | X:(E) (its domain) | computed | – | 8 cases, 186 generated leave |
| PB1.7 | constrains | L257, D6.9 (FROZEN) | claimed only | – | the relabeling exclusion vacuous on baseline-only contracts |
| PB1.8 | changes with | D4.4 | computed | e1.00 | FC17, FC18 unchanged |
| PB1.8 | blocks | L119 (FROZEN): kinds 'not from the values its ports take in a solution' | computed | – | FC05 (i) |
| PB1.8 | changes with | FC18 (Argument 1: a same-kind condition adds nothing), the reply's 'at risk' | contradicted | – | FC18 holds under PB1.8 |
| PB1.9 | blocks | L119 (FROZEN): kinds relative to the contract | computed | – | FC04 (b), FC16 |
| PB1.9 | constrains | L11.s2 (FROZEN) | claimed only | – | reads more nearly this way |
| PB2.1 | changes with | D5.7, D12.7 (FROZEN) | computed | r2e2.14 | FC104.new1 (b) |
| PB2.1 | blocks | L221.n1, L223.s3 (FROZEN) | computed | r2e2.14 | FC104.new1 (b): no Sel with Viol⁺ inside H |
| PB2.1 | moves | X:Dec, X:Expl | computed | – | FC104.new1 (b) |
| PB2.1 | blocks | invariance of fidelity under recoding (FC67) | computed | – | FC67 |
| PB2.2 | moves | X:(F2), X:(E) | computed | – | 1 worked, 11 generated enter |
| PB2.2 | blocks | L271.s1 (FROZEN): the reversed calculation fails (F2) on the production contract | computed | – | FC27.new1 (c) |
| PB2.2 | blocks | L257.n3 (FROZEN) | claimed only | – | not run as the reply's FC21 (d) |
| PB2.3 | moves | X:(F1), X:(E) | computed | – | 214 generated leave |
| PB2.3 | constrains | L231.s2, L245.s4 (FROZEN) | claimed only | – | background as named background |
| PB2.4 | blocks | L369.s2 (B2) | claimed only | – | not computed |
| PB2.4 | changes with | D6.4, D8.2 (FROZEN) | computed | – | FC96 (i): (A) for both no longer gives equal answers |
| PB2.4 | moves | X:(A) | computed | – | meaning only: no candidate enters |
| PB2.4 | moves | X:(E): 'enter: candidates that determine an answer where the target gives ⊥' (the reply) | contradicted | – | none enters on any case computed; the reply's own case fails (F1), (F2) |
| PB2.5 | moves | X:Dependence, X:(E) | computed | – | 149 / 12 generated leave |
| PB2.5 | constrains | D6.5 (FROZEN) | claimed only | – | NC0 stays a conjunct |
| PB2.6 | moves | X:NonVacuous | computed | e1.51 | as PB1.1 |
| PB2.6 | changes with | PB1.1 (V1.7) | computed | – | the same (E) on every case |
| PB2.7 | changes with | D6.3 (FROZEN) | computed | – | the quantifier readings move (E) again |
| PB2.7 | blocks | L269.s2 (FROZEN) with S45 | computed | – | FC25.new2 |
| PB2.7 | moves | X:(A), X:(E) | computed | – | as C6 |
| PB2.8 | blocks | L313.n3 (FROZEN) | claimed only | – | by argument from FC40 |
| PB2.9 | changes with | D8.2, D8.3, D12.5 | claimed only | – | not computed |
| PB3.1 | moves | X:Dec, X:Expl | computed | – | the student's copy |
| PB3.1 | blocks | L405 (FROZEN): 'the rest of the content keeps its inherited provenance' | claimed only | – |  |
| PB3.2 | moves | X:Dec, X:Expl | computed | – | 10 chains |
| PB3.2 | blocks | L211.s3, L211.s1 (FROZEN) | computed | – | FC98 (e) |
| PB3.3 | changes with | D12.1 (FROZEN) | computed | – | the hand-set Sel history |
| PB3.3 | moves | X:Dec, X:Expl | computed | – | 44 cases, 999 generated on a Sel history |
| PB3.3 | constrains | L223.s3 (FROZEN) | claimed only | – |  |
| PB3.4 | moves | X:Dec, X:Expl | computed | – | student's copy; 82 chains |
| PB3.4 | blocks | L193.s1 (FROZEN): exactly one of three | computed | – | FC12.new1: Sel ∧ Con at a fixed point |
| PB3.5 | changes with | D12.1 (FROZEN) | computed | – | no case moves |
| PB3.6 | moves | X:Dec, X:Expl | computed | – | student's copy, on that reading |
| PB3.6 | constrains | D16.3 (FROZEN) | claimed only | – |  |
| PB3.7 | blocks | L413.s1, L413.s2 (FROZEN) | claimed only | – |  |
| PB4.1 | changes with | D9.8 (FROZEN) | computed | e2.20 | FC72 (d), FC72.new1 (c) |
| PB4.1 | moves | X:(Suff) | claimed only | e2.21 | under S109-B4-I1 the defeat sets do not move; the other choice not computed |
| PB4.2 | changes with | D9.6 (FROZEN) | computed | – | FC56 (a″) |
| PB4.3 | changes with | D9.6 (FROZEN) | claimed only | – |  |
| PB4.4 | blocks | L397.s10 (FROZEN) | computed | – | X_j empty |
| PB4.4 | moves | X:(Suff), X:(Nec) | computed | – | the defeat sets empty |
| PB4.5 | changes with | D9.10 (FROZEN) | computed | – | FC74, FC76 |
| PB4.6 | changes with | D11.4 (FROZEN) | computed | e3.34b | no claim moves |
| PB4.7 | changes with | FC109 | computed | – | holds |
| PB4.8 | blocks | D10.6 (FROZEN) as written | computed | – | FC47.new1 |

Edges joining Part A's map: e1.48, e1.49, e1.51 (V1.7, now computed as PB1.1: e1.51 and e1.49 computed, e1.48 still claimed only); e2.20 (computed), e2.21 (still claimed only: under S109-B4-I1 the defeat sets do not move); r2e2.14 (R2V2.7, computed as PB2.1); r2e1.30 (R2V1.4: no reader, claimed only); r2e1.34 (R2V1.7, computed as PB1.4); e1.00 (V1.1's block on D4.4: PB1.8 lifts it and FC17, FC18 hold); e3.34b (the neighbour of PB4.6).

## 4. Totals

**69 edges**: claimed only 23, computed 44, contradicted 2.

| kind | computed | contradicted | claimed only |
|---|---|---|---|
| blocks | 10 | 0 | 7 |
| changes with | 14 | 1 | 5 |
| constrains | 1 | 0 | 10 |
| moves | 19 | 1 | 1 |

Variants: 33 implemented and computed (18 moving scope, 5 meaning only, 10 neither), 1 flagged out (PB3.8; PB4.4 computed as PB4.4′).

## 5. Gaps under rule 10 (a proposal; the settlement after the cross-examination decides)

Rule 10: Part B ends when no gap bearing on the explanation definition remains that another round of Part B could reach: every free item upstream of (E), Dec, Expl, (Suff) or (Nec) varied and computed, or recorded with why no variant inside Part B's rule can reach it; every class-a carry-over computed; no edge on the definition's parts left claimed only that a variant inside the rule could settle.

- **Class-a carry-overs**: all three computed (PB1.1, PB2.1, PB4.1). No gap. (e2.21 stays claimed only under S109-B4-I1's reading, which keeps the defeat sets as D16.XV has them; the other choice, the instance reading inside the defeat sets, was Part A's V4.4, computed there.)
- **Free items bearing on the definition that no variant reached** (the tabulation's §8), with the reply's reason and this reading of it:

| section | items | the reply's reason | can a variant inside the rule reach it? |
|---|---|---|---|
| B1 | D1.1 and its sentences L87.s1, L91.s1–s6, L93.s1 | varying the organization tuple changes every structure at once | **yes**: a clause of D1.1 can be varied alone and computed (X_v ≠ ∅; composition partial or total; I02's no-law clause; the identity law), as PB1.6 varied D1.3 alone; "changes everything" is a prediction, not a reason no variant exists |
| B1 | D1.2 ((O)), L99.s1 | (O) is the vocabulary every conjunct is written in | **yes**, the same way (e.g., Sol read over V_J only, or with a declared tolerance); the reason given is that the change would be large, which the rule does not exclude |
| B1 | L105.s2, L105.s3, L137.s1, L143.s1 | no conjunct reads them; displays of D3.1, D3.2 | recorded: displays and glosses whose formal content is D3.1 and D3.2, varied by PB1.2, PB1.3, PB1.7 — no separate variant |
| B1 | L147.s1 (O_p), L147.s2 (ρ_p) | O_p read only by repair; ρ_p is B3's | **open**: the template marks both as bearing on (E) and Dec (through D3.1); O_p reaches the definition only through the static graph; ρ_p is read by no conjunct (FC30) but by Found (PB1.5) and Part A's V1.5 / R2V1.1 (C2). A variant of ρ_p's values inside B1 is statable (R2V1.2, not taken up) |
| B1 | D3.7 | FC34 already computes both readings | recorded: both readings computed (FC34) |
| B2 | L245.s1–s3 | glosses of (F1), (F2) | recorded: their content moved with PB2.2, PB2.3 |
| B2 | D5.2 (projection), D5.3 (candidate shape) | notation; the tuple D6.7 reads | D5.2: **yes**, a variant is statable (the projection read through a value map other than λ's, or the counterpart's solutions read before projecting, which is Part A's V1.1 on D1.4 from the other side); D5.3: recorded (varying the candidate's shape changes D6.7, FROZEN) |
| B2 | D6.1 | reads D1.3 (B1's) | recorded: moved with PB1.6 (FC-E1's restriction); a variant of D6.1 itself (Lost read on δ_E's value set rather than on answers) is statable — **open** |
| B2 | D6.10 | E_tab and E_enc anchor FC25 | recorded: an encoding, not a definition of a part |
| B3 | L169.s2 (a content) | not named by the reply | **open**: a content read as an organization with its contract-relative commitments is what New and Rep read; a variant is statable |
| B4 | L315.s10, L315.s17 | FROZEN formalizations; S21 | recorded: L315.s17 cannot be varied without saying what must happen (S21); L315.s10's formalizations (D8.1–D8.6) are FROZEN beyond D8.4, D8.6, whose variants move the claim-conflict layer only |
| B4 | L389.s1 (K2), L397.s5 (X_j) | each conjunct varied at its own definitions | recorded: K2's conjuncts varied at D9.5 (PB4.2), D9.3 (PB4.3); X_j at D9.8 (PB4.1, PB4.4′); L397.s5 formalized by D9.7, whose variants Part A computed |

- **Edges on the definition's parts left claimed only that a variant could settle**: e1.48 (the stated-scope requirement at L43.s4, L159.s1: a text block, no run decides it); PB2.4's block of L369.s2 (a run could: a candidate with a determined answer at a ⊥ pair that also meets (F1), (F2) — none exists on the cases computed); PB2.9's changes with D8.2 (the program's π is total; a partial-π copy would be needed); PB2.2's block of L257.n3 (FC21 (d)'s relabeling case under PB2.2: runnable).
- **Readings the owner's cases turn on** (not gaps; the owner's): the change as an edit, a boundary or mixed (PB1.2, PB1.7); D6.3's quantifier (PB2.7); Θ's reading of a bare edit (PB1.2); whether the textbook's carrier is inside the student's boundary (PB3.6); a selection history for the sign and the vane (PB3.3).

**Proposal**: gaps remain that a round 2 of Part B could reach: D1.1's and D1.2's clauses (B1), L147.s1–s2 (B1), D5.2 and D6.1 (B2), L169.s2 (B3), and the four edges above. So a round 2 of Part B, aimed at those items only, under its own rule written and committed before sending — unless the settlement after the GLM cross-examination finds the reasons for leaving them sufficient.

## 6. Unsure

- The free set is Claude's working reading of "the parts that are hard to vary", not approved by the owner; everything here is a result on this free set.
- The owner's cases are the program's encodings (Part A's for the edit, boundary and mixed readings); the bridge's history is (a1) or (a2) as FC84.new1 builds them; the student's copy is FC30.new1 (d)'s chain.
- Dec on the worked and generated cases is read on three hand-set histories (I90); only the chains, the student's copy and the bridge compute provenance from a history. PB3.3 and PB3.5 turn on the hand-set history's occurrences (every pair of C occurs there).
- Where the program has no counterpart for the variant's object (Θ of a bare edit, β, an input-assigning background, a held explanation of a premise), the nearest reading was implemented and recorded as an invention with its other choices (S36); PB2.3's drops rest mostly on S109-B2-I1.
- Each whole-suite run was made once, by this agent's script, without a second run by a verifier.
- FC84.new1 (d) under PB3.4 prints a TypeError: the claim's own failure message formats a tuple with %, a defect of the claim's code on a failure path (the program after round 4 never reaches it); recorded, not repaired (rule 13).

Written by one Opus 5.5 agent under rule 6 and decision S56, 29 September 2026. Nothing applied; nothing ruled.
