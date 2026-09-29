# S109 Part B round 1 - section B1 (organizations, kinds, questions and contracts) - variants computed

*Rule 5 of `S109 Part B round 1 - how the replies will be read, written before sending.md`. The one Opus 5.5 agent of decision S56 (effort high). Works only in `S109 Part B round 1 - computation/section B1 model/` (a copy of `S107 Round 4 - maths after the reading/model after round 4/`, 26 files md5-identical at the copy; the original and Part A's copies never written). Read with the reply (`returns/s109_glm_section1.response.txt`) and the tabulation (`S109 Part B round 1 - tabulation of the replies, before any ruling.md`). Built by `computation/map/s109b_map_build.py` from the hand record `computation/map/s109b_data.py`, the scope runs and the whole-suite results. Nothing here changes the theory (rule 13). "Candidate" or "explanation" for what the theory judges; "model" only for the program or a small structure it builds (S43).*

Status: complete, 29 September 2026.

## 0. Setup

| item | state |
|---|---|
| copy | `model after round 4/`, 26 files identical at the copy (md5 list compared) |
| switches | `S109B_VARIANT` in the environment (a case script sets `core.S109B`); readings: `S109B_THETA` (all, strict); every change is guarded by the switch, the patch is `computation/patches/patch_B1.py` |
| default unchanged | the whole suite in the B3 copy with every switch off equals the record after round 4 (142 of 142 claims, `whole suite/B3/none.json`); the scope script's 'none' values equal Part A's section 2 copy's on all 17,329 cases (`comparisons with Part A/`) |
| scope | `computation/scripts/s109b_scope.py` → `section B1 runs/scope.json`, `scope.txt`, `scope tables.md` / `.json`: the 27 worked cases and 22 encodings of the owner's sign and vane (edit, boundary, mixed; E_enc on each question), the student's copy (FC30.new1 (d)), the generated worlds (SMALL, 160 per size, seed 109001: 17,280 candidates, 999 meeting (E)),  FC-E1-E5 (`s104_external.py`) and CT1-CT8 (`s104_creative_transport.py`) against their output under 'none' |
| the replies' small cases | `computation/scripts/s109b_small_cases.py` → `section B1 runs/small cases.txt` (B1, B2) |
| whole suite | `tools/sonnet_harness/run_claims.py` per variant and reading, scale 4, time cap 45, PYTHONHASHSEED=0, from the copy's parent, under `timeout`, output in the scratchpad, results copied to `whole suite/B1/` and summarized in `whole suite/summary.md` / `.json` (the moved claims' printouts kept there) |

## 1. What is implemented, and the inventions it forced (S36)

| id | free item(s) | kind | carry-over | implemented | switch | inventions (other choices) |
|---|---|---|---|---|---|---|
| PB1.1 | D3.5 | replace | V1.7 (a) | yes | S109B_VARIANT=PB1.1 (core.nonvacuous) | none new: drops I27 (Excl a primitive); other choice: I27 kept |
| PB1.2 | D3.1 | strengthen | R2V1.9 (b) | nearest reading | S109B_VARIANT=PB1.2, S109B_THETA=all or strict (core.is_question) | S109-B1-I1: Θ_admits of a bare edit, which the program never computes: 'all' (Θ admits every edit: the program's worlds) or 'strict' (Θ admits the identity only: the reading on which no edit of a mathematical target is admitted); others: Θ_admits of an edit of an attributed organization at a grain (the text's words at L159.s3); of the pair (a,b) |
| PB1.3 | D3.2 | replace | R2V1.8 (b) | yes | S109B_VARIANT=PB1.3 (core.is_question) | S109-B1-I2: Y_p ⊆ X_δD checked at the pairs of C (others: at every pair of A×B); a designation that is not one port (the fibre query's (H,T,L)) names no question |
| PB1.4 | D4.2 | replace | R2V1.7 (b) | yes | S109B_VARIANT=PB1.4 (core.footprint_bijections) | none new: drops I10 (β); other choices: β as now; β keeping an order |
| PB1.5 | L155.s6 | replace | R2V1.4 (b) | yes (read by no claim) | core.found() | which values count as found (other: all three, which makes Found vacuous) |
| PB1.6 | L103.s1, D1.3 | replace | – | yes | S109B_VARIANT=PB1.6 (core.Org.L) | the empty-relation deletion; the absent-port clause not implemented (the program adds no absent port); others: the full relation (as now); removal from J (needs I03 moved) |
| PB1.7 | L141.s2, D3.1 | strengthen | – | yes | S109B_VARIANT=PB1.7 (core.is_question) | 'some edit other than 1' (others: some edit no relabeling; two pairs with different answers) |
| PB1.8 | L115.s1, D4.1 | strengthen | – (lifts e1.00) | yes | S109B_VARIANT=PB1.8 (core.sig_fn, one_kind) | Sol_D(a,b)↾V_j as the fourth component (others: Sol of {j} alone; the baseline only) |
| PB1.9 | L113.s1, D4.1, D4.2, D4.3, D4.4 | replace | – | yes | S109B_VARIANT=PB1.9 (core.one_kind) | S109-B1-I3: A×B read as every pair both readings reach (others: C, as now; C ⊆ C′ ⊆ A×B) |

## 2. Meaning: the changed formal statement, old beside new, of each part of the explanation definition that moves

| id | part | old | new |
|---|---|---|---|
| PB1.1 | (E): NonVacuous | Sol_D(1,b0) ≠ ∅ ∧ (A×B)∖C ⊆ Excl(Σ), Excl(Σ) a declared input (I27) | Sol_D(1,b0) ≠ ∅ (Excl(Σ) := (A×B)∖C, so Stated holds of every question) |
| PB1.2 | domain of (E), Expl, (Suff), (Nec) | p a question: C ⊆ A×B, (1,b0) ∈ C | … ∧ ∀(a,b) ∈ C: Θ_admits(a); a contract holding an edit Θ does not admit names no question |
| PB1.3 | domain of (E); what (A) and Contrast compare | Q(O,a,b;δ) ∈ Y_p ∪ {⊥}, Y_p free (I21) | Y_p := X_δD: a query with an answer outside X_δD ∪ {⊥} names no question |
| PB1.4 | none of the five parts | j ~_C j′ :⟺ ∃β … | j ~_C j′ :⟺ V_j = V_j′ (ordered) ∧ sig_C(j) = sig_C(j′) |
| PB1.5 | none of the five parts | Found(p) requires ρ_p = constructed | Found(p) :⟺ ρ_p ∈ {selected, constructed} |
| PB1.6 | (E): Dependence (NC2's Lost, through D6.1's E−G) | E−G: every component of G imposes the full relation | E−G: every component of G imposes the empty relation; so Sol_{E−G} = ∅ and Ans_{E−G} = ⊥ wherever G's footprints are nonempty |
| PB1.7 | domain of (E) | (1,b0) ∈ C | (1,b0) ∈ C ∧ ∃(a,b) ∈ C: a ≠ 1 |
| PB1.8 | none of the five parts | sig_C(j) = {(a,b,L_j(a,b))} | sig⁺_C(j) = {(a,b,L_j(a,b),Sol_D(a,b)↾V_j)} |
| PB1.9 | none of the five parts | kinds: classes of ~_C | kinds: classes of ~_{A×B} |

## 3. Scope: computed, the variant off against on

### PB1.1

On every question the program builds Excl(Σ) already equals (A×B)∖C (I85), so no worked, owner's or generated case moves; the hand case with Excl(Σ) = ∅ (the pole's forward candidate on C1) enters: Acc F → T (small cases).

| reading | cases moved (Acc in / out / Expl only) | the owner's sign and vane (off → on; Expl on Dec/Con/Sel histories) | the student's copy | generated | FC-E, CT |
|---|---|---|---|---|---|
| PB1.1 | 0 (0 / 0 / 0) | all stay | stays (Acc True, Dec at o2 [True]) | Acc in 0, out 0; Expl (Sel history) in 0, out 0 | same |

Claims that move (whole suite): none.

### PB1.2

Θ 'all': nothing moves (the code path is the default's). Θ 'strict': every contract holding an edit other than 1 names no question: 36 of 49 cases leave (0 enter), among them the owner's two-part sign and weathervane with the change read as an edit or mixed; with the change read as a boundary both stay (their contracts hold the identity edit only); 813 of 999 generated accounts leave; 18 claims move.

| reading | cases moved (Acc in / out / Expl only) | the owner's sign and vane (off → on; Expl on Dec/Con/Sel histories) | the student's copy | generated | FC-E, CT |
|---|---|---|---|---|---|
| PB1.2 Θ all | 0 (0 / 0 / 0) | all stay | stays (Acc True, Dec at o2 [True]) | Acc in 0, out 0; Expl (Sel history) in 0, out 0 | same |
| PB1.2 Θ strict | 41 (0 / 36 / 5) | sign two parts (edit): Acc T, Expl F/T/T → Acc F, Expl F/F/F; sign two parts (mixed): Acc T, Expl F/T/T → Acc F, Expl F/F/F; vane M13 (edit): Acc T, Expl F/T/T → Acc F, Expl F/F/F; vane ℰ_mix (mixed): Acc T, Expl F/T/T → Acc F, Expl F/F/F | moves: H={(1,b1_45)}: Dec [True] → [True]; H=∅: Dec [True] → [True] | Acc in 0, out 813; Expl (Sel history) in 0, out 813 | s104_external.py, s104_creative_transport.py |

PB1.2 Θ strict: enter: none. Leave: E1 pole, forward organization, C1; E1 pole, forward organization, C2; E1 pole, forward organization, C3; E1 pole, reversed calculation under Mimo's τ', H only; L269 encoding table E_enc, pole C1; L269 encoding table E_enc, pole C2; L273 'p because p': the pole's L written in, C1; M1 decorated lookup; M2 lookup under I83; M3 one component on two ports; M5: the answer fixed at each pair by another part; M13: the owner's weathervane (S41 Q15); R3-Q1: the hand-turned vane ('north when turned'); E5 eliminative (L339), FC62's encoding; E5 eliminative (L339), the second encoding; E8 p_δ, the identity candidate (K1's criticism question); E9 two-layer episode, S1 with t1 (L626); E9 two-layer episode, S1 with t1∘ψ (L630); S44 the shop sign, two parts (red on Mon, blue on Tue); S44 the shop sign, one part (red on Mon, blue on Tue); the sign with a day port and a palette rule; owner's vane, change as edit: M13 (Γ = {cy}); owner's vane, change as edit: E_enc on p; owner's vane, change as edit: M13 Γ = {cx} (the wind's commitment); owner's vane, change as mixed: D_vane^mix Γ = {cW} (the reply's ℰ_mix); owner's vane, change as mixed: E_enc on p_mix; owner's vane, change as mixed: D_vane^mix Γ = {cP}; owner's vane, change as mixed: D_vane^mix Γ = {cW,cP}; owner's sign, change as edit: two parts (ℰ_two, S44); owner's sign, change as edit: E_enc on p_sign; owner's sign, change as edit: one part (ℰ_one); owner's sign, change as edit: day port (ℰ_day); owner's sign, change as edit: E_enc on p_sign_day; owner's sign, change as mixed: two parts; owner's sign, change as mixed: E_enc on p_sign_mix; owner's sign, change as mixed: one part.

Claims that move (whole suite): FC101 H→CEX; FC22 H→CEX; FC23 parts: (c) area 2: restating lookups / (d) area 2: the slot quantifier (A2-02; R3-Q1, a; FC23.new1 H→CEX; FC23.new2 H→CEX; FC23.new3 H→CEX; FC23.new5 H→CEX; FC25.new2 H→CEX; FC26 H→CEX; FC27.new1 H→CEX; FC30.new1 H→CEX; FC34 parts: wide reading: a candidate meeting (E) on both; FC42.new1 H→CEX; FC62 H→CEX; FC63 parts: (c-ii) the Leibniz candidate, sum restricted to ; FC72.new2 H→CEX; FC90.new1 H→CEX; FC99 H→CEX.

### PB1.3

The pole's identification question C_id (fibre query) leaves (Acc T → F); nothing else, no generated case (every generated query reads a port), no claim.

| reading | cases moved (Acc in / out / Expl only) | the owner's sign and vane (off → on; Expl on Dec/Con/Sel histories) | the student's copy | generated | FC-E, CT |
|---|---|---|---|---|---|
| PB1.3 | 1 (0 / 1 / 0) | all stay | stays (Acc True, Dec at o2 [True]) | Acc in 0, out 0; Expl (Sel history) in 0, out 0 | same |

PB1.3: enter: none. Leave: E1 pole, reversed calculation, identification C_id.

Claims that move (whole suite): none.

### PB1.4

No case moves (no conjunct reads a kind). FC05 (ii) and FC103.new1 (b) (Argument 2's 'one kind' for E9's exchanged pair) move.

| reading | cases moved (Acc in / out / Expl only) | the owner's sign and vane (off → on; Expl on Dec/Con/Sel histories) | the student's copy | generated | FC-E, CT |
|---|---|---|---|---|---|
| PB1.4 | 0 (0 / 0 / 0) | all stay | stays (Acc True, Dec at o2 [True]) | Acc in 0, out 0; Expl (Sel history) in 0, out 0 | same |

Claims that move (whole suite): FC05 parts: (ii) reading (ii), no longer a reading of L119; FC103.new1 H→CEX.

### PB1.5

Nothing moves: no conjunct of (E), Dec or the defeat sets reads Found (FC30), and no claim calls it; the whole suite was not run (its code path is the default's).

| reading | cases moved (Acc in / out / Expl only) | the owner's sign and vane (off → on; Expl on Dec/Con/Sel histories) | the student's copy | generated | FC-E, CT |
|---|---|---|---|---|---|
| PB1.5 | 0 (0 / 0 / 0) | all stay | stays (Acc True, Dec at o2 [True]) | Acc in 0, out 0; Expl (Sel history) in 0, out 0 | same |

Claims that move (whole suite): the whole suite was not run: no claim reads the changed code.

### PB1.6

61 generated candidates enter (Dep F → T; all E_enc-family with a commitment empty somewhere), the reply's idle-commitment case enters (Acc F → T); no worked or owner's case moves; FC-E's restriction line changes (E|{k} gives ⊥); FC01 (a) (deletion keeps solutions) fails.

| reading | cases moved (Acc in / out / Expl only) | the owner's sign and vane (off → on; Expl on Dec/Con/Sel histories) | the student's copy | generated | FC-E, CT |
|---|---|---|---|---|---|
| PB1.6 | 0 (0 / 0 / 0) | all stay | stays (Acc True, Dec at o2 [True]) | Acc in 61, out 0; Expl (Sel history) in 61, out 0 | s104_external.py |

Claims that move (whole suite): FC01 H→CEX.

### PB1.7

8 cases leave: C_id and every encoding of the owner's sign and vane with the change read as a boundary (contracts {1}×B); with the change as an edit or mixed both stay; 186 generated leave; FC25.new2 (a) fails. Its drops are a subset of Part A's C5's: equal on every worked and owner's case, C5 drops 80 generated more (comparisons with Part A).

| reading | cases moved (Acc in / out / Expl only) | the owner's sign and vane (off → on; Expl on Dec/Con/Sel histories) | the student's copy | generated | FC-E, CT |
|---|---|---|---|---|---|
| PB1.7 | 8 (0 / 8 / 0) | sign two parts (boundary): Acc T, Expl F/T/T → Acc F, Expl F/F/F; vane Γ={cW} (boundary): Acc T, Expl F/T/T → Acc F, Expl F/F/F | stays (Acc True, Dec at o2 [True]) | Acc in 0, out 186; Expl (Sel history) in 0, out 186 | same |

PB1.7: enter: none. Leave: E1 pole, reversed calculation, identification C_id; owner's vane, change as boundary: D_vane Γ = {cW} (the wind's commitment); owner's vane, change as boundary: E_enc on p_vane_b; owner's vane, change as boundary: D_vane Γ = {cP}; owner's vane, change as boundary: D_vane Γ = {cW,cP}; owner's sign, change as boundary: two parts; owner's sign, change as boundary: E_enc on p_sign_b; owner's sign, change as boundary: one part.

Claims that move (whole suite): FC25.new2 H→CEX.

### PB1.8

No case moves; FC05 fails ((i) signatures use relations only; (ii) reading (i)); FC17, FC18 hold (the reply's 'FC18 at risk' does not happen).

| reading | cases moved (Acc in / out / Expl only) | the owner's sign and vane (off → on; Expl on Dec/Con/Sel histories) | the student's copy | generated | FC-E, CT |
|---|---|---|---|---|---|
| PB1.8 | 0 (0 / 0 / 0) | all stay | stays (Acc True, Dec at o2 [True]) | Acc in 0, out 0; Expl (Sel history) in 0, out 0 | same |

Claims that move (whole suite): FC05 H→CEX.

### PB1.9

No case moves; FC04 (b) (a finer contract can separate) finds no witness, FC05 and FC16 fail.

| reading | cases moved (Acc in / out / Expl only) | the owner's sign and vane (off → on; Expl on Dec/Con/Sel histories) | the student's copy | generated | FC-E, CT |
|---|---|---|---|---|---|
| PB1.9 | 0 (0 / 0 / 0) | all stay | stays (Acc True, Dec at o2 [True]) | Acc in 0, out 0; Expl (Sel history) in 0, out 0 | same |

Claims that move (whole suite): FC04 parts: (b) a finer contract can separate; FC05 H→CEX; FC16 H→CEX.

## 4. Edges

| id | kind | item | standing | Part A id | why |
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
| PB1.9 | blocks | L119 (FROZEN): kinds relative to the contract | computed | – | FC04 (b), FC16 |
| PB1.9 | constrains | L11.s2 (FROZEN) | claimed only | – | reads more nearly this way |

Nothing here is a change to the theory (rule 13). Written by one Opus 5.5 agent under rule 5 and decision S56, 29 September 2026.
