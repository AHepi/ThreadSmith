# S109 Part B round 1 - section B2 (transports, fidelity, the account, routes and the exact constructions) - variants computed

*Rule 5 of `S109 Part B round 1 - how the replies will be read, written before sending.md`. The one Opus 5.5 agent of decision S56 (effort high). Works only in `S109 Part B round 1 - computation/section B2 model/` (a copy of `S107 Round 4 - maths after the reading/model after round 4/`, 26 files md5-identical at the copy; the original and Part A's copies never written). Read with the reply (`returns/s109_glm_section2.response.txt`) and the tabulation (`S109 Part B round 1 - tabulation of the replies, before any ruling.md`). Built by `computation/map/s109b_map_build.py` from the hand record `computation/map/s109b_data.py`, the scope runs and the whole-suite results. Nothing here changes the theory (rule 13). "Candidate" or "explanation" for what the theory judges; "model" only for the program or a small structure it builds (S43).*

Status: complete, 29 September 2026.

## 0. Setup

| item | state |
|---|---|
| copy | `model after round 4/`, 26 files identical at the copy (md5 list compared) |
| switches | `S109B_VARIANT` in the environment (a case script sets `core.S109B`); readings: `S109B_NC0` (bg, bg-input), `S105_SLOT_QUANTIFIER` (the program's); every change is guarded by the switch, the patch is `computation/patches/patch_B2.py` |
| default unchanged | the whole suite in the B3 copy with every switch off equals the record after round 4 (142 of 142 claims, `whole suite/B3/none.json`); the scope script's 'none' values equal Part A's section 2 copy's on all 17,329 cases (`comparisons with Part A/`) |
| scope | `computation/scripts/s109b_scope.py` → `section B2 runs/scope.json`, `scope.txt`, `scope tables.md` / `.json`: the 27 worked cases and 22 encodings of the owner's sign and vane (edit, boundary, mixed; E_enc on each question), the student's copy (FC30.new1 (d)), the generated worlds (SMALL, 160 per size, seed 109001: 17,280 candidates, 999 meeting (E)),  FC-E1-E5 (`s104_external.py`) and CT1-CT8 (`s104_creative_transport.py`) against their output under 'none' |
| the replies' small cases | `computation/scripts/s109b_small_cases.py` → `section B2 runs/small cases.txt` (B1, B2) |
| whole suite | `tools/sonnet_harness/run_claims.py` per variant and reading, scale 4, time cap 45, PYTHONHASHSEED=0, from the copy's parent, under `timeout`, output in the scratchpad, results copied to `whole suite/B2/` and summarized in `whole suite/summary.md` / `.json` (the moved claims' printouts kept there) |

## 1. What is implemented, and the inventions it forced (S36)

| id | free item(s) | kind | carry-over | implemented | switch | inventions (other choices) |
|---|---|---|---|---|---|---|
| PB2.1 | L189.s2 | replace | R2V2.7 (a) | yes | S109B_VARIANT=PB2.1 (core.faithful; claims_b.faithful_on, viol_at) | none new: I49's wide extent (others: narrow; wide at L220 only) |
| PB2.2 | D5.5, L241.s1 | weaken | – | yes | S109B_VARIANT=PB2.2 (core.F2; faithful_on) | none new: I18's dropped choice |
| PB2.3 | D5.4 | strengthen | – | nearest reading | S109B_VARIANT=PB2.3 (core.F1_at) | S109-B2-I1: a component of E with no counterpart in λ fails (F1) (others: exempt; (F1) over J_E minus input assigners) |
| PB2.4 | D5.6, L249.s1 | weaken | – | yes | S109B_VARIANT=PB2.4 (core.A_at) | S109-B2-I2 (the reply's PB2-In2): (A) over Det_C (others: C, as now; Det_C ∪ both ⊥) |
| PB2.5 | D6.2 | strengthen | – | nearest reading | S109B_VARIANT=PB2.5, S109B_NC0=bg or bg-input (core.NC0, dep) | S109-B2-I3: 'carries Ans_p' read as Pin (D6.3's clause at one pair) by a background component (k ∉ Γ): 'bg' any, 'bg-input' one that assigns an input port of E (Roles(E)); other: I23's gloss (NC0 always true) |
| PB2.6 | D6.6 | weaken | – | yes | S109B_VARIANT=PB2.6 (core.nonvacuous) | I27 'no conjunct' (others: as now; V1.7) |
| PB2.7 | D5.6 | re-order a dependence | – | yes | S109B_VARIANT=PB2.7, S105_SLOT_QUANTIFIER (core.A) | none new: D6.3's quantifier (I136) computed under each reading |
| PB2.8 | L311.s2, D7.3 | weaken | – | no code change | none (every block of a finite Γ is finite) | PB2-In3: B finite (other: unrestricted) |
| PB2.9 | D5.1 | replace | – | no code change | none (π is total in the program, I81) | none: I16 (partial on solutions) was never the program's; I81 builds π total |

## 2. Meaning: the changed formal statement, old beside new, of each part of the explanation definition that moves

| id | part | old | new |
|---|---|---|---|
| PB2.1 | Dec (Sel's Faithful_H, Held, Rep, T′) and Expl | Faithful_C := F1 ∧ F2; Faithful_H without (A); Viol narrow | Faithful_C := F1 ∧ F2 ∧ A; Faithful_H with (A) at H; Viol := Viol⁺ |
| PB2.2 | (E): (F2); Dec through Faithful_H | F2_C := F2eq_C ∧ Hom(τ) | F2_C := F2eq_C |
| PB2.3 | (E): (F1) | ∀k ∈ Γ: proj^λ Sol_λ(k) = L_k | ∀k ∈ J_E: … |
| PB2.4 | (E): (A) | ∀(a,b) ∈ C: Ans_E = Ans_p (⊥ = ⊥) | ∀(a,b) ∈ Det_C: Ans_E = Ans_p |
| PB2.5 | (E): Dependence | NC0 (true) ∧ NC2 | NC0′ ∧ NC2, NC0′ :⟺ no background component pins δ_E to Ans_p at a pair of C |
| PB2.6 | (E): NonVacuous | Sol_D(1,b0) ≠ ∅ ∧ Stated(C,Σ) | Sol_D(1,b0) ≠ ∅ |
| PB2.7 | (E): (A) | A_C(ℰ) | A_C(ℰ) ∧ NC1(ℰ) (no answer slot, D6.3) |
| PB2.8 | none of the five parts | CB(B;W) :⟺ ∅ ≠ B ⊆ W ∧ W ∈ S ∧ W∖B ∉ S | … ∧ B finite |
| PB2.9 | (E): what (F1), (F2) read (the transport) | π: X_D ⇀ X_E on Sol_D (I16) | π: X_D → X_E total |

## 3. Scope: computed, the variant off against on

### PB2.1

No worked, owner's or generated case moves on the hand-set histories (their selection pair is answered right); FC104.new1 (b)'s selected transport, wrong in its answer at its own H, is no longer selected (Sel F): declared, so no explanation there; FC67 (invertible recodings keep fidelity) fails. The bridge's chain reads Held by hand: stays.

| reading | cases moved (Acc in / out / Expl only) | the owner's sign and vane (off → on; Expl on Dec/Con/Sel histories) | the student's copy | generated | FC-E, CT |
|---|---|---|---|---|---|
| PB2.1 | 0 (0 / 0 / 0) | all stay | stays (Acc True, Dec at o2 [True]) | Acc in 0, out 0; Expl (Sel history) in 0, out 0 | same |

Claims that move (whole suite): FC104.new1 H→CEX; FC67 H→CEX.

### PB2.2

The reversed calculation under τ′ on C1 enters (Acc F → T: identification presented as production); the relabeling candidate (τ(1) ≠ 1) moves on the Sel history only (Faithful_H loses Hom); 11 generated enter; FC27.new1 (c) and FC77 move.

| reading | cases moved (Acc in / out / Expl only) | the owner's sign and vane (off → on; Expl on Dec/Con/Sel histories) | the student's copy | generated | FC-E, CT |
|---|---|---|---|---|---|
| PB2.2 | 2 (1 / 0 / 1) | all stay | stays (Acc True, Dec at o2 [True]) | Acc in 11, out 0; Expl (Sel history) in 11, out 0 | same |

PB2.2: enter: E1 pole, reversed calculation under Mimo's τ', C1. Leave: none.

Claims that move (whole suite): FC27.new1 H→CEX; FC77 H→CEX.

### PB2.3

214 generated leave (mostly E_enc candidates whose background component has no counterpart: I1 decides it); no worked or owner's case moves; the reply's small case (an added k1 with no counterpart) leaves.

| reading | cases moved (Acc in / out / Expl only) | the owner's sign and vane (off → on; Expl on Dec/Con/Sel histories) | the student's copy | generated | FC-E, CT |
|---|---|---|---|---|---|
| PB2.3 | 0 (0 / 0 / 0) | all stay | stays (Acc True, Dec at o2 [True]) | Acc in 0, out 214; Expl (Sel history) in 0, out 214 | s104_external.py |

Claims that move (whole suite): FC42.new1 parts: (d) the other choice: δ_v quantified; FC80.new1 parts: (a) W6: fidelity on H is required, not all the e.

### PB2.4

Meaning moves, scope unchanged on every case computed (49 cases, 17,280 generated, FC-E, CT); the reply's small cases fail (F1) and (F2) on and off; FC21 (a2), FC96 (i) and FC109 fail (two candidates both meeting (A) with different answers at ⊥ pairs).

| reading | cases moved (Acc in / out / Expl only) | the owner's sign and vane (off → on; Expl on Dec/Con/Sel histories) | the student's copy | generated | FC-E, CT |
|---|---|---|---|---|---|
| PB2.4 | 0 (0 / 0 / 0) | all stay | stays (Acc True, Dec at o2 [True]) | Acc in 0, out 0; Expl (Sel history) in 0, out 0 | same |

Claims that move (whole suite): FC109 H→CEX; FC21 H→CEX; FC96 H→CEX.

### PB2.5

'bg': E5's eliminative candidate (FC62's encoding) leaves, 149 generated leave, FC23.new1 and FC62 fail; 'bg-input': 12 generated leave, no claim moves. The owner's four cases stay. The reply's small case fails (F2) and (A) with and without the variant.

| reading | cases moved (Acc in / out / Expl only) | the owner's sign and vane (off → on; Expl on Dec/Con/Sel histories) | the student's copy | generated | FC-E, CT |
|---|---|---|---|---|---|
| PB2.5 bg | 1 (0 / 1 / 0) | all stay | stays (Acc True, Dec at o2 [True]) | Acc in 0, out 149; Expl (Sel history) in 0, out 149 | same |
| PB2.5 bg-input | 0 (0 / 0 / 0) | all stay | stays (Acc True, Dec at o2 [True]) | Acc in 0, out 12; Expl (Sel history) in 0, out 12 | same |

PB2.5 bg: enter: none. Leave: E5 eliminative (L339), FC62's encoding.

Claims that move (whole suite): FC23.new1 H→CEX (PB2.5-bg); FC62 H→CEX (PB2.5-bg).

### PB2.6

As PB1.1 on every case computed: nothing moves on the program's questions; the hand case with Excl(Σ) = ∅ enters (the same code path's value).

| reading | cases moved (Acc in / out / Expl only) | the owner's sign and vane (off → on; Expl on Dec/Con/Sel histories) | the student's copy | generated | FC-E, CT |
|---|---|---|---|---|---|
| PB2.6 | 0 (0 / 0 / 0) | all stay | stays (Acc True, Dec at o2 [True]) | Acc in 0, out 0; Expl (Sel history) in 0, out 0 | same |

Claims that move (whole suite): none.

### PB2.7

'every': 20 cases leave (the one-part sign in every encoding, E_enc on every question, the lookups), the two-part sign and the vane stay; 'some', 'some-exempt', 'some-exempt-set': the two-part sign leaves too (every encoding); 935 / 946 / 855 / 858 generated leave. Equal to Part A's C6 (V2.4) on all 17,329 cases under each quantifier (comparisons with Part A).

| reading | cases moved (Acc in / out / Expl only) | the owner's sign and vane (off → on; Expl on Dec/Con/Sel histories) | the student's copy | generated | FC-E, CT |
|---|---|---|---|---|---|
| PB2.7 every | 21 (0 / 20 / 1) | all stay | stays (Acc True, Dec at o2 [True]) | Acc in 0, out 935; Expl (Sel history) in 0, out 935 | same |
| PB2.7 some | 29 (0 / 28 / 1) | sign two parts (edit): Acc T, Expl F/T/T → Acc F, Expl F/F/F; sign two parts (boundary): Acc T, Expl F/T/T → Acc F, Expl F/F/F; sign two parts (mixed): Acc T, Expl F/T/T → Acc F, Expl F/F/F | stays (Acc True, Dec at o2 [True]) | Acc in 0, out 946; Expl (Sel history) in 0, out 946 | same |
| PB2.7 some-exempt | 25 (0 / 24 / 1) | sign two parts (edit): Acc T, Expl F/T/T → Acc F, Expl F/F/F; sign two parts (boundary): Acc T, Expl F/T/T → Acc F, Expl F/F/F; sign two parts (mixed): Acc T, Expl F/T/T → Acc F, Expl F/F/F | stays (Acc True, Dec at o2 [True]) | Acc in 0, out 855; Expl (Sel history) in 0, out 855 | same |
| PB2.7 some-exempt-set | 26 (0 / 25 / 1) | sign two parts (edit): Acc T, Expl F/T/T → Acc F, Expl F/F/F; sign two parts (boundary): Acc T, Expl F/T/T → Acc F, Expl F/F/F; sign two parts (mixed): Acc T, Expl F/T/T → Acc F, Expl F/F/F | stays (Acc True, Dec at o2 [True]) | Acc in 0, out 858; Expl (Sel history) in 0, out 858 | same |

PB2.7 every: enter: none. Leave: E1 pole, reversed calculation under Mimo's τ', H only; L269 encoding table E_enc, pole C1; L269 encoding table E_enc, pole C2; L273 'p because p': the pole's L written in, C1; M1 decorated lookup; M2 lookup under I83; M3 one component on two ports; R3-Q1: the hand-turned vane ('north when turned'); E8 p_δ, the identity candidate (K1's criticism question); S44 the shop sign, one part (red on Mon, blue on Tue); owner's vane, change as edit: E_enc on p; owner's vane, change as boundary: E_enc on p_vane_b; owner's vane, change as mixed: E_enc on p_mix; owner's sign, change as edit: E_enc on p_sign; owner's sign, change as edit: one part (ℰ_one); owner's sign, change as edit: E_enc on p_sign_day; owner's sign, change as boundary: E_enc on p_sign_b; owner's sign, change as boundary: one part; owner's sign, change as mixed: E_enc on p_sign_mix; owner's sign, change as mixed: one part.

PB2.7 some: enter: none. Leave: E1 pole, forward organization, C2; E1 pole, forward organization, C3; E1 pole, reversed calculation under Mimo's τ', H only; L269 encoding table E_enc, pole C1; L269 encoding table E_enc, pole C2; L273 'p because p': the pole's L written in, C1; M1 decorated lookup; M2 lookup under I83; M3 one component on two ports; M5: the answer fixed at each pair by another part; R3-Q1: the hand-turned vane ('north when turned'); E5 eliminative (L339), FC62's encoding; E8 p_δ, the identity candidate (K1's criticism question); S44 the shop sign, two parts (red on Mon, blue on Tue); S44 the shop sign, one part (red on Mon, blue on Tue); owner's vane, change as edit: E_enc on p; owner's vane, change as boundary: E_enc on p_vane_b; owner's vane, change as mixed: E_enc on p_mix; owner's sign, change as edit: two parts (ℰ_two, S44); owner's sign, change as edit: E_enc on p_sign; owner's sign, change as edit: one part (ℰ_one); owner's sign, change as edit: E_enc on p_sign_day; owner's sign, change as boundary: two parts; owner's sign, change as boundary: E_enc on p_sign_b; owner's sign, change as boundary: one part; owner's sign, change as mixed: two parts; owner's sign, change as mixed: E_enc on p_sign_mix; owner's sign, change as mixed: one part.

PB2.7 some-exempt: enter: none. Leave: E1 pole, reversed calculation under Mimo's τ', H only; L269 encoding table E_enc, pole C1; L269 encoding table E_enc, pole C2; L273 'p because p': the pole's L written in, C1; M1 decorated lookup; M2 lookup under I83; M3 one component on two ports; M5: the answer fixed at each pair by another part; E5 eliminative (L339), FC62's encoding; E8 p_δ, the identity candidate (K1's criticism question); S44 the shop sign, two parts (red on Mon, blue on Tue); S44 the shop sign, one part (red on Mon, blue on Tue); owner's vane, change as boundary: E_enc on p_vane_b; owner's vane, change as mixed: E_enc on p_mix; owner's sign, change as edit: two parts (ℰ_two, S44); owner's sign, change as edit: E_enc on p_sign; owner's sign, change as edit: one part (ℰ_one); owner's sign, change as edit: E_enc on p_sign_day; owner's sign, change as boundary: two parts; owner's sign, change as boundary: E_enc on p_sign_b; owner's sign, change as boundary: one part; owner's sign, change as mixed: two parts; owner's sign, change as mixed: E_enc on p_sign_mix; owner's sign, change as mixed: one part.

PB2.7 some-exempt-set: enter: none. Leave: E1 pole, reversed calculation under Mimo's τ', H only; L269 encoding table E_enc, pole C1; L269 encoding table E_enc, pole C2; L273 'p because p': the pole's L written in, C1; M1 decorated lookup; M2 lookup under I83; M3 one component on two ports; M5: the answer fixed at each pair by another part; E5 eliminative (L339), FC62's encoding; E8 p_δ, the identity candidate (K1's criticism question); S44 the shop sign, two parts (red on Mon, blue on Tue); S44 the shop sign, one part (red on Mon, blue on Tue); owner's vane, change as edit: E_enc on p; owner's vane, change as boundary: E_enc on p_vane_b; owner's vane, change as mixed: E_enc on p_mix; owner's sign, change as edit: two parts (ℰ_two, S44); owner's sign, change as edit: E_enc on p_sign; owner's sign, change as edit: one part (ℰ_one); owner's sign, change as edit: E_enc on p_sign_day; owner's sign, change as boundary: two parts; owner's sign, change as boundary: E_enc on p_sign_b; owner's sign, change as boundary: one part; owner's sign, change as mixed: two parts; owner's sign, change as mixed: E_enc on p_sign_mix; owner's sign, change as mixed: one part.

Claims that move (whole suite): FC23 parts: (c) area 2: restating lookups / (e) S106: a lookup E_lk meets (E); FC23.new1 H→CEX; FC23.new2 H→CEX; FC23.new5 H→CEX; FC25.new2 H→CEX; FC27.new1 H→CEX; FC72.new2 H→CEX.

### PB2.8

No part reads (S), (B), (D); on finite Γ nothing can move. On L311's infinitary example FC40 found no finite critical block in 20,000 samples, so under PB2.8 that example has no critical block at all (by argument from FC40's computed result); FC40's check is unchanged and holds.

| reading | cases moved (Acc in / out / Expl only) | the owner's sign and vane (off → on; Expl on Dec/Con/Sel histories) | the student's copy | generated | FC-E, CT |
|---|---|---|---|---|---|
| PB2.8 | 0 (0 / 0 / 0) | all stay | stays (Acc True, Dec at o2 [True]) | Acc in 0, out 0; Expl (Sel history) in 0, out 0 | same |

Claims that move (whole suite): the whole suite was not run: no code changes.

### PB2.9

Meaning moves, scope unchanged on every case computed: the program's π is total already.

| reading | cases moved (Acc in / out / Expl only) | the owner's sign and vane (off → on; Expl on Dec/Con/Sel histories) | the student's copy | generated | FC-E, CT |
|---|---|---|---|---|---|
| PB2.9 | 0 (0 / 0 / 0) | all stay | stays (Acc True, Dec at o2 [True]) | Acc in 0, out 0; Expl (Sel history) in 0, out 0 | same |

Claims that move (whole suite): the whole suite was not run: no code changes.

## 4. Edges

| id | kind | item | standing | Part A id | why |
|---|---|---|---|---|---|
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

Nothing here is a change to the theory (rule 13). Written by one Opus 5.5 agent under rule 5 and decision S56, 29 September 2026.
