# S109 Part B round 1 - section B4 (rivals, problems, criticism, the class, what would rule it out, and the Arguments) - variants computed

*Rule 5 of `S109 Part B round 1 - how the replies will be read, written before sending.md`. The one Opus 5.5 agent of decision S56 (effort high). Works only in `S109 Part B round 1 - computation/section B4 model/` (a copy of `S107 Round 4 - maths after the reading/model after round 4/`, 26 files md5-identical at the copy; the original and Part A's copies never written). Read with the reply (`returns/s109_glm_section4.response.txt`) and the tabulation (`S109 Part B round 1 - tabulation of the replies, before any ruling.md`). Built by `computation/map/s109b_map_build.py` from the hand record `computation/map/s109b_data.py`, the scope runs and the whole-suite results. Nothing here changes the theory (rule 13). "Candidate" or "explanation" for what the theory judges; "model" only for the program or a small structure it builds (S43).*

Status: complete, 29 September 2026.

## 0. Setup

| item | state |
|---|---|
| copy | `model after round 4/`, 26 files identical at the copy (md5 list compared) |
| switches | `S109B_VARIANT` in the environment (a case script sets `core.S109B`); readings: `S109B_HELD` (all, no-records); every change is guarded by the switch, the patch is `computation/patches/patch_B4.py` |
| default unchanged | the whole suite in the B3 copy with every switch off equals the record after round 4 (142 of 142 claims, `whole suite/B3/none.json`); the scope script's 'none' values equal Part A's section 2 copy's on all 17,329 cases (`comparisons with Part A/`) |
| scope | `computation/scripts/s109b_scope.py` → `section B4 runs/scope.json`, `scope.txt`, `scope tables.md` / `.json`: the 27 worked cases and 22 encodings of the owner's sign and vane (edit, boundary, mixed; E_enc on each question), the student's copy (FC30.new1 (d)),  FC-E1-E5 (`s104_external.py`) and CT1-CT8 (`s104_creative_transport.py`) against their output under 'none' |
| the replies' small cases | `computation/scripts/s109b_small_cases.py` → `section B4 runs/small cases.txt` (B1, B2) |
| whole suite | `tools/sonnet_harness/run_claims.py` per variant and reading, scale 4, time cap 45, PYTHONHASHSEED=0, from the copy's parent, under `timeout`, output in the scratchpad, results copied to `whole suite/B4/` and summarized in `whole suite/summary.md` / `.json` (the moved claims' printouts kept there) |

## 1. What is implemented, and the inventions it forced (S36)

| id | free item(s) | kind | carry-over | implemented | switch | inventions (other choices) |
|---|---|---|---|---|---|---|
| PB4.1 | L315.s7 | replace | V2.8's part (a) | nearest reading | S109B_VARIANT=PB4.1 (args.X) | S109-B4-I1: 'uses its meeting (E)' read as every atom of φ among α's leaves' atoms; the defeat sets' φ (Expl_ atoms) keep D16.XV's reading (others: the instance reading everywhere; RO asking φ among α's symbols) |
| PB4.2 | D9.5 | weaken | – | yes | S109B_VARIANT=PB4.2 (args.Assessor.scope_ok) | which indices j declares (I42) |
| PB4.3 | D9.3 | weaken | – | no code change | none (every form's pattern uses all its children) | what a form uses (I89's other side) |
| PB4.4 | L397.s13 | strengthen | – | flagged out as written; computed as PB4.4′ on D9.8 | S109B_VARIANT=PB4.4', S109B_HELD=all or no-records (args.X) | S109-B4-I2: the variant restated on D9.8 (the tabulation's flag); no one in the program holds a represented explanation of a premise; 'all' every accepted leaf, 'no-records' record leaves exempt (the two give the same) |
| PB4.5 | L383.s1 | strengthen | – | yes | S109B_VARIANT=PB4.5 (claims_b FC74, FC76) | occurrence typed with its allegation (other: retyped, not excluded) |
| PB4.6 | L385.s1, D9.11 | weaken | – | yes | S109B_VARIANT=PB4.6 (claims_b FC76) | route readings as Part A's e3.34b |
| PB4.7 | L546.s1 | strengthen | – | yes | S109B_VARIANT=PB4.7 (claims_b FC109) | none |
| PB4.8 | D10.1, L317.s1 | weaken | – | yes | S109B_VARIANT=PB4.8 (claims_r3a2 FC47.new1, claims_r4a3 FC72.new2) | whether Prob keeps ξ (other: an assessor-free core beside per-assessor problems) |

## 2. Meaning: the changed formal statement, old beside new, of each part of the explanation definition that moves

| id | part | old | new |
|---|---|---|---|
| PB4.1 | none of the five parts (Out_j) | ℰ ruled out for j :⟺ X_j('Acc(ℰ)') ≠ ∅ | … ∃α ∈ X_j with Acc(ℰ) ∈ Uses(α) |
| PB4.2 | (Suff), (Nec): X_j through Usable | Scope_j(u) :⟺ C_u ⊆ C_j(u) ∧ ℓ_u = ℓ_j(u) ∧ β_u = β_j(u) | Scope_j(u) :⟺ C_u ⊆ C_j(u) |
| PB4.3 | (Suff), (Nec): X_j through Prem | Prem(u) := children(u) | Prem(u) := the premises Form(u) uses |
| PB4.4 | (Suff), (Nec): X_j | X_j(φ) := {α: Usable_j(α) ∧ RO(α,φ)} | … ∧ every premise of α taken as given has a held explanation |
| PB4.5 | none of the five parts | a criticism occurrence may lack Bearing | Occ_criticism(c) ⇒ Bearing(c,z,p) |
| PB4.6 | none of the five parts | UsesReason asks an image port on an active route | that clause dropped |
| PB4.7 | none of the five parts | list with Arguments 1-3 | list with Arguments 1-10 |
| PB4.8 | none of the five parts | Prob_j :⟺ Riv ∧ NotOut_j ∧ NotOut_j | Prob :⟺ Riv |

## 3. Scope: computed, the variant off against on

### PB4.1

No case of (E) or Expl moves; a premise alone (¬PM) no longer rules out the design (FC72 (d), FC72.new1 (c)); FC56 (c′) moves.

| reading | cases moved (Acc in / out / Expl only) | the owner's sign and vane (off → on; Expl on Dec/Con/Sel histories) | the student's copy | generated | FC-E, CT |
|---|---|---|---|---|---|
| PB4.1 | 0 (0 / 0 / 0) | all stay (B4 reads neither (E) nor Dec) | stays | not run (B4 code reads neither Acc nor Dec) | same |

Claims that move (whole suite): FC56 H→CEX; FC72 H→CEX; FC72.new1 H→CEX.

### PB4.2

No case of (E) or Expl moves; FC56 (a″): the coarse-grain assessor's argument becomes usable.

| reading | cases moved (Acc in / out / Expl only) | the owner's sign and vane (off → on; Expl on Dec/Con/Sel histories) | the student's copy | generated | FC-E, CT |
|---|---|---|---|---|---|
| PB4.2 | 0 (0 / 0 / 0) | all stay (B4 reads neither (E) nor Dec) | stays | not run (B4 code reads neither Acc nor Dec) | same |

Claims that move (whole suite): FC56 H→CEX.

### PB4.3

Meaning moves, scope unchanged: form_ok's patterns use every child.

| reading | cases moved (Acc in / out / Expl only) | the owner's sign and vane (off → on; Expl on Dec/Con/Sel histories) | the student's copy | generated | FC-E, CT |
|---|---|---|---|---|---|
| PB4.3 | 0 (0 / 0 / 0) | all stay (B4 reads neither (E) nor Dec) | stays | not run (B4 code reads neither Acc nor Dec) | same |

Claims that move (whole suite): the whole suite was not run: no code changes.

### PB4.4

No case of (E) or Expl moves; every argument of the program has a premise taken as given, so X_j is empty everywhere: nothing is ruled out and the defeat sets are empty; FC23.new2 (f), FC30.new1 (a), (d), (e), (g), (h), FC47.new1, FC56, FC72, FC72.new1, FC72.new2 move.

| reading | cases moved (Acc in / out / Expl only) | the owner's sign and vane (off → on; Expl on Dec/Con/Sel histories) | the student's copy | generated | FC-E, CT |
|---|---|---|---|---|---|
| PB4.4' all | 0 (0 / 0 / 0) | all stay (B4 reads neither (E) nor Dec) | stays | not run (B4 code reads neither Acc nor Dec) | same |
| PB4.4' no-records | 0 (0 / 0 / 0) | all stay (B4 reads neither (E) nor Dec) | stays | not run (B4 code reads neither Acc nor Dec) | same |

Claims that move (whole suite): FC23.new2 H→CEX (PB4.4p-all), H→CEX (PB4.4p-no-records); FC30.new1 H→CEX (PB4.4p-all), H→CEX (PB4.4p-no-records); FC47.new1 H→CEX (PB4.4p-all), H→CEX (PB4.4p-no-records); FC56 H→CEX (PB4.4p-all), H→CEX (PB4.4p-no-records); FC72 H→CEX (PB4.4p-all), H→CEX (PB4.4p-no-records); FC72.new1 H→CEX (PB4.4p-all), H→CEX (PB4.4p-no-records); FC72.new2 H→CEX (PB4.4p-all), H→CEX (PB4.4p-no-records).

### PB4.5

No case of (E) or Expl moves; FC74 (a criticism without bearing) finds no witness; FC76 fails.

| reading | cases moved (Acc in / out / Expl only) | the owner's sign and vane (off → on; Expl on Dec/Con/Sel histories) | the student's copy | generated | FC-E, CT |
|---|---|---|---|---|---|
| PB4.5 | 0 (0 / 0 / 0) | all stay (B4 reads neither (E) nor Dec) | stays | not run (B4 code reads neither Acc nor Dec) | same |

Claims that move (whole suite): FC74 parts: a criticism without bearing; FC76 H→CEX.

### PB4.6

Nothing moves (FC76's route is active anyway); Part A's e3.34b computed the neighbouring reading.

| reading | cases moved (Acc in / out / Expl only) | the owner's sign and vane (off → on; Expl on Dec/Con/Sel histories) | the student's copy | generated | FC-E, CT |
|---|---|---|---|---|---|
| PB4.6 | 0 (0 / 0 / 0) | all stay (B4 reads neither (E) nor Dec) | stays | not run (B4 code reads neither Acc nor Dec) | same |

Claims that move (whole suite): none.

### PB4.7

Nothing moves; FC109 holds with FC81, FC95, FC97-FC103 added.

| reading | cases moved (Acc in / out / Expl only) | the owner's sign and vane (off → on; Expl on Dec/Con/Sel histories) | the student's copy | generated | FC-E, CT |
|---|---|---|---|---|---|
| PB4.7 | 0 (0 / 0 / 0) | all stay (B4 reads neither (E) nor Dec) | stays | not run (B4 code reads neither Acc nor Dec) | same |

Claims that move (whole suite): none.

### PB4.8

No case of (E) or Expl moves; FC47.new1 (solved, posed again) and FC72.new2 (c) (no problem for j1) fail.

| reading | cases moved (Acc in / out / Expl only) | the owner's sign and vane (off → on; Expl on Dec/Con/Sel histories) | the student's copy | generated | FC-E, CT |
|---|---|---|---|---|---|
| PB4.8 | 0 (0 / 0 / 0) | all stay (B4 reads neither (E) nor Dec) | stays | not run (B4 code reads neither Acc nor Dec) | same |

Claims that move (whole suite): FC47.new1 H→CEX; FC72.new2 H→CEX.

## 4. Edges

| id | kind | item | standing | Part A id | why |
|---|---|---|---|---|---|
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

Nothing here is a change to the theory (rule 13). Written by one Opus 5.5 agent under rule 5 and decision S56, 29 September 2026.
