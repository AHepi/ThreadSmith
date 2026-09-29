# S109 Part B round 1 - section B3 (provenance, histories, representation, construction, repair and the physical module) - variants computed

*Rule 5 of `S109 Part B round 1 - how the replies will be read, written before sending.md`. The one Opus 5.5 agent of decision S56 (effort high). Works only in `S109 Part B round 1 - computation/section B3 model/` (a copy of `S107 Round 4 - maths after the reading/model after round 4/`, 26 files md5-identical at the copy; the original and Part A's copies never written). Read with the reply (`returns/s109_glm_section3.response.txt`) and the tabulation (`S109 Part B round 1 - tabulation of the replies, before any ruling.md`). Built by `computation/map/s109b_map_build.py` from the hand record `computation/map/s109b_data.py`, the scope runs and the whole-suite results. Nothing here changes the theory (rule 13). "Candidate" or "explanation" for what the theory judges; "model" only for the program or a small structure it builds (S43).*

Status: complete, 29 September 2026.

## 0. Setup

| item | state |
|---|---|
| copy | `model after round 4/`, 26 files identical at the copy (md5 list compared) |
| switches | `S109B_VARIANT` in the environment (a case script sets `core.S109B`); readings: none beyond the variant; every change is guarded by the switch, the patch is `computation/patches/patch_B3.py` |
| default unchanged | the whole suite in the B3 copy with every switch off equals the record after round 4 (142 of 142 claims, `whole suite/B3/none.json`); the scope script's 'none' values equal Part A's section 2 copy's on all 17,329 cases (`comparisons with Part A/`) |
| scope | `computation/scripts/s109b_scope.py` → `section B3 runs/scope.json`, `scope.txt`, `scope tables.md` / `.json`: the 27 worked cases and 22 encodings of the owner's sign and vane (edit, boundary, mixed; E_enc on each question), the student's copy (FC30.new1 (d)), the generated worlds (SMALL, 160 per size, seed 109001: 17,280 candidates, 999 meeting (E)),  FC-E1-E5 (`s104_external.py`) and CT1-CT8 (`s104_creative_transport.py`) against their output under 'none'; every chain of 1 to 3 holdings (584) and the bridge's chains (FC84.new1 (a1), (a2)) |
| the replies' small cases | `computation/scripts/s109b_small_cases.py` → `section B3 runs/small cases.txt` (B1, B2) |
| whole suite | `tools/sonnet_harness/run_claims.py` per variant and reading, scale 4, time cap 45, PYTHONHASHSEED=0, from the copy's parent, under `timeout`, output in the scratchpad, results copied to `whole suite/B3/` and summarized in `whole suite/summary.md` / `.json` (the moved claims' printouts kept there) |

## 1. What is implemented, and the inventions it forced (S36)

| id | free item(s) | kind | carry-over | implemented | switch | inventions (other choices) |
|---|---|---|---|---|---|---|
| PB3.1 | D12.4 | replace | R2V2.4 (b) | nearest reading | S109B_VARIANT=PB3.1 (claims_s41 FC30.new1 (d), (f): rec_of) | S109-B3-I1: only holdings a case names as whole-content copies inherit (the student's); the program's other chains name none |
| PB3.2 | D12.5, L207.s1 | weaken | – | yes | S109B_VARIANT=PB3.2 (claims_b._prov_step) | none new: the reading T in Sel's exclusion (I162's other choice) |
| PB3.3 | L195.s1, L195.s5 | strengthen | – | yes | S109B_VARIANT=PB3.3 (claims_b.sel) | occurrence read on h's occurs set (the hand-set Sel history lets every pair of C occur, I90) (others: up to o_t; up to e) |
| PB3.4 | L199.s1, L199.s3 | re-order a dependence | – | nearest reading | S109B_VARIANT=PB3.4 (claims_b._prov_step) | S109-B3-I2: every held holding of a chain holds the one transport t; Sel and Con on h∪ read as 'some holding has it' (others: the last holding's, as now; the earliest's); no precedence rule (Sel and Con may both hold) |
| PB3.5 | D11.5, L217.s2 | weaken | – | yes | S109B_VARIANT=PB3.5 (claims_b.sel) | S109-B3-I3: every boundary of H actual (others: Θ by hand, as now; the edit enacted) |
| PB3.6 | D11.1, L169.s1 | strengthen | – | nearest reading (a case reading) | S109B_VARIANT=PB3.6 (claims_s41 FC30.new1 (d)) | the textbook's carrier outside the student's declared boundary (the reading); others: anywhere (as now); β plus carriers relayed in |
| PB3.7 | D13.4, L169.s3 | replace | – | yes | S109B_VARIANT=PB3.7 (claims_b FC85 equiv) | output equality of the port query on the first port at the pairs of C_c (others: on C_d; on C_c ∪ C_d) |
| PB3.8 | L225.s4 | drop | – | flagged out (no formal statement) | none | none |

## 2. Meaning: the changed formal statement, old beside new, of each part of the explanation definition that moves

| id | part | old | new |
|---|---|---|---|
| PB3.1 | Dec (inheritance, D12.4) | provenance per part; a binding newly built by the copier gets its own value | a holding reached by a copy of a carrier's whole content inherits prov(t,o) whole |
| PB3.2 | Dec (Sel's exclusion) | Rep_ℓ(o,c) :⟺ ∃t [Faithful ∧ (Sel ∨ Con)]; Sel's exclusion reads Rep at o′ ≺ o (T′) | Rep := Held; Sel's exclusion reads Held at o′ ≺ o (T) |
| PB3.3 | Dec (Sel) | Sel(t;𝒯,μ,H) as D12.1 | … ∧ C ∩ Occ(h) ⊆ H |
| PB3.4 | Dec (the history) | Dec(t,o_t) read on h(t,o_t) | read on h∪(t) = ∪{h(t,o): t held at o} |
| PB3.5 | Dec (Sel's H-clause) | H ⊆ Occ(h) (Occurs a primitive through Θ) | H admitted (Occurs := admitted ∧ actual) |
| PB3.6 | Dec (what histories are built from) | Occ: physically located carriers | Occ: those inside the declared boundary β |
| PB3.7 | none of the five parts (New, Origin) | d ≡_ℓ c :⟺ faithful transports both ways | d ≡_ℓ c :⟺ Ans_d = Ans_c on C_c |
| PB3.8 | none | — | — |

## 3. Scope: computed, the variant off against on

### PB3.1

The student's copy enters: Dec at o2 T → F under both H, Expl F → T; nothing else (worked cases, generated, chains, bridge, CT); FC30.new1 (d), (f) fail.

| reading | cases moved (Acc in / out / Expl only) | the owner's sign and vane (off → on; Expl on Dec/Con/Sel histories) | the student's copy | generated | FC-E, CT |
|---|---|---|---|---|---|
| PB3.1 | 0 (0 / 0 / 0) | all stay | moves: H={(1,b1_45)}: Dec [True] → [False]; H=∅: Dec [True] → [False] | Acc in 0, out 0; Expl (Sel history) in 0, out 0 | same |

PB3.1, chains: 0 of 584 differ; at the output Dec → not Dec 0, not Dec → Dec 0; number of fixed points changed 0. The bridge: stays (Con and Build at the output under (a1) and (a2)).

Claims that move (whole suite): FC30.new1 H→CEX.

### PB3.2

10 chain outputs of 584 become declared (18 chains differ), no hand-set case, no generated case; the student's copy and the bridge stay; FC98 (e) fails (the earlier declared holder now blocks the selection).

| reading | cases moved (Acc in / out / Expl only) | the owner's sign and vane (off → on; Expl on Dec/Con/Sel histories) | the student's copy | generated | FC-E, CT |
|---|---|---|---|---|---|
| PB3.2 | 0 (0 / 0 / 0) | all stay | stays (Acc True, Dec at o2 [True]) | Acc in 0, out 0; Expl (Sel history) in 0, out 0 | same |

PB3.2, chains: 18 of 584 differ; at the output Dec → not Dec 0, not Dec → Dec 10; number of fixed points changed 0. The bridge: stays (Con and Build at the output under (a1) and (a2)).

Claims that move (whole suite): FC98 H→CEX.

### PB3.3

On the hand-set selection history (every pair of C occurred, H = {(1,b0)}) no candidate is selected: 44 of 49 cases lose Expl on that history, the owner's sign and vane among them (every encoding), 999 of 999 generated; Acc unchanged; chains unchanged; FC102.new1, FC12.new2, FC30.new1 (e) move.

| reading | cases moved (Acc in / out / Expl only) | the owner's sign and vane (off → on; Expl on Dec/Con/Sel histories) | the student's copy | generated | FC-E, CT |
|---|---|---|---|---|---|
| PB3.3 | 44 (0 / 0 / 44) | sign two parts (edit): Acc T, Expl F/T/T → Acc T, Expl F/T/F; sign two parts (boundary): Acc T, Expl F/T/T → Acc T, Expl F/T/F; sign two parts (mixed): Acc T, Expl F/T/T → Acc T, Expl F/T/F; vane M13 (edit): Acc T, Expl F/T/T → Acc T, Expl F/T/F; vane Γ={cW} (boundary): Acc T, Expl F/T/T → Acc T, Expl F/T/F; vane ℰ_mix (mixed): Acc T, Expl F/T/T → Acc T, Expl F/T/F | stays (Acc True, Dec at o2 [True]) | Acc in 0, out 0; Expl (Sel history) in 0, out 999 | same |

PB3.3, chains: 0 of 584 differ; at the output Dec → not Dec 0, not Dec → Dec 0; number of fixed points changed 0. The bridge: stays (Con and Build at the output under (a1) and (a2)).

Claims that move (whole suite): FC102.new1 H→CEX; FC12.new1 parts: round 2's D12.1 (no cod t exclusion), tags; FC12.new2 H→CEX; FC30.new1 H→CEX; FC83 parts: U and K with Build read as Held (D13.3 as it now / without I161 (the review's R1).

### PB3.4

The student's copy enters (Dec F); 82 chain outputs of 584 enter (198 differ; 16 change their number of fixed points); the bridge stays; FC12.new1, FC12.new2, FC30.new1, FC83, FC98, FC98.new1 fail; FC84.new1 (d) finds a chain with more than one fixed point (printed as an error: the claim's own message formats a tuple with %).

| reading | cases moved (Acc in / out / Expl only) | the owner's sign and vane (off → on; Expl on Dec/Con/Sel histories) | the student's copy | generated | FC-E, CT |
|---|---|---|---|---|---|
| PB3.4 | 0 (0 / 0 / 0) | all stay | moves: H={(1,b1_45)}: Dec [True] → [False]; H=∅: Dec [True] → [False] | Acc in 0, out 0; Expl (Sel history) in 0, out 0 | same |

PB3.4, chains: 198 of 584 differ; at the output Dec → not Dec 82, not Dec → Dec 0; number of fixed points changed 16. The bridge: stays (Con and Build at the output under (a1) and (a2)).

Claims that move (whole suite): FC12.new1 H→CEX; FC12.new2 H→CEX; FC30.new1 H→CEX; FC83 H→CEX; FC84.new1 H→NT; FC98 H→CEX; FC98.new1 H→CEX.

### PB3.5

Meaning moves, scope unchanged on every case computed: every hand-set history of the program lets every pair of C occur, and FC30.new1 (e)'s link has H = ∅.

| reading | cases moved (Acc in / out / Expl only) | the owner's sign and vane (off → on; Expl on Dec/Con/Sel histories) | the student's copy | generated | FC-E, CT |
|---|---|---|---|---|---|
| PB3.5 | 0 (0 / 0 / 0) | all stay | stays (Acc True, Dec at o2 [True]) | Acc in 0, out 0; Expl (Sel history) in 0, out 0 | same |

PB3.5, chains: 0 of 584 differ; at the output Dec → not Dec 0, not Dec → Dec 0; number of fixed points changed 0. The bridge: stays (Con and Build at the output under (a1) and (a2)).

Claims that move (whole suite): none.

### PB3.6

On that reading the student's copy with one pair tried enters (Dec F: Sel at its own holding); with H = ∅ it stays declared; FC30.new1 (d) fails; nothing else (no other case names β).

| reading | cases moved (Acc in / out / Expl only) | the owner's sign and vane (off → on; Expl on Dec/Con/Sel histories) | the student's copy | generated | FC-E, CT |
|---|---|---|---|---|---|
| PB3.6 | 0 (0 / 0 / 0) | all stay | moves: H={(1,b1_45)}: Dec [True] → [False]; H=∅: Dec [True] → [True] | Acc in 0, out 0; Expl (Sel history) in 0, out 0 | same |

PB3.6, chains: 0 of 584 differ; at the output Dec → not Dec 0, not Dec → Dec 0; number of fixed points changed 0. The bridge: stays (Con and Build at the output under (a1) and (a2)).

Claims that move (whole suite): FC30.new1 H→CEX.

### PB3.7

No case moves; FC85 holds (its witness of a one-way match survives output equality).

| reading | cases moved (Acc in / out / Expl only) | the owner's sign and vane (off → on; Expl on Dec/Con/Sel histories) | the student's copy | generated | FC-E, CT |
|---|---|---|---|---|---|
| PB3.7 | 0 (0 / 0 / 0) | all stay | stays (Acc True, Dec at o2 [True]) | Acc in 0, out 0; Expl (Sel history) in 0, out 0 | same |

PB3.7, chains: 0 of 584 differ; at the output Dec → not Dec 0, not Dec → Dec 0; number of fixed points changed 0. The bridge: stays (Con and Build at the output under (a1) and (a2)).

Claims that move (whole suite): none.

### PB3.8

Not implemented (tabulation §6).


Claims that move (whole suite): the whole suite was not run: flagged out.

## 4. Edges

| id | kind | item | standing | Part A id | why |
|---|---|---|---|---|---|
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

Nothing here is a change to the theory (rule 13). Written by one Opus 5.5 agent under rule 5 and decision S56, 29 September 2026.
