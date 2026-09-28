# S108 Part A - section 1 - variants computed

*Computing agent for section 1 (rule 5 of `S108 Part A - how the replies will be read, written before sending.md`), Opus 5.5, 28 September 2026. Fresh. Works only in `S108 Part A - computation/section 1 model/` (a copy of `S107 Round 4 - maths after the reading/model after round 4/`). Nothing here changes the theory (rule 11). "Candidate" or "explanation" for what the theory judges; "model" only for the program or a small structure it builds (S43).*

Status: in progress. Filled as it goes.

## 0. Setup

| item | state |
|---|---|
| copy | `S108 Part A - computation/section 1 model/` = program after round 4, every file md5-identical at the copy |
| switches | `model/core.py`: `S108_S1` ("none" default; V1.1, V1.2, V1.3, V1.4, V1.5, V1.8), from env `S108_S1_VARIANT`; `S108_S1_GEN` ("follow" default, "fixed") for the generator's encodings; `claims_r3a1.ident` ('bot') and FC28's R4 part route Ident's contract clause through `core.ident_contract`; `gen._E_from_lam` reads D1.4 through `_gen_variant()` |
| default unchanged | under "none" the three case scripts print byte for byte the committed printouts (md5 86a67664…, d473944e…, 043aeb36…, as the rule gives) |
| scripts (in the copy) | `s108_s1_suite.py` (whole suite → JSON), `s108_s1_cases.py` (worked cases, provenance, the reply's small cases), `s108_s1_worlds.py` (generated worlds) |
| runs | PYTHONHASHSEED=0, `timeout` on every run; suite at scale 4, time cap 45 (the printout's settings) |

## 1. Which variants are implemented (the tabulation, §1 and §6)

| id | item | kind | implemented | why |
|---|---|---|---|---|
| V1.1 | D1.4 (Sol_N) | swap | yes | in scope |
| V1.2 | D2.1 (k ≠ j clause) | delete | yes | in scope |
| V1.3 | D2.4 (R-i) | weaken | yes | in scope |
| V1.4 | D3.3 (Ident's contract clause) | swap | yes | in scope |
| V1.5 | D3.4 (ρ_p) | delete | yes (nearest reading, S108-1-I5) | in scope; the program carries no ρ_p |
| V1.6 | D3.6 + a new sentence | strengthen | **no** | flagged by the tabulation (§6): out of scope in effect (D6.7, S2) and adds prose (S40); rule 4: not implemented while flagged |
| V1.7 | D0.2 (Excl defined) | other | **no** | flagged (§6): in effect rewrites D3.5 (FROZEN); rule 4. Only the baseline side of its case is run (§4) |
| V1.8 | D2.6 (Slc_j := Alt_j) | weaken | yes | in scope |

## 2. How each is implemented, and the inventions it forced (S36)

| id | code (the copy) | as written? | inventions recorded here |
|---|---|---|---|
| V1.1 | `Org.sol_sub`: Sol_N(a,b) := proj of Sol_D(a,b) on V_N (V_N, I138 unchanged) | yes | S108-1-I2: the generator's encodings (`gen._E_from_lam`, I81/I32) build E from Sol_N; whole suite: they follow the variant (`S108_S1_GEN=follow`); generated-worlds comparison: built as after round 4 (`fixed`) so the same candidate is judged off and on |
| V1.2 | `sets_through`: the ∀k ≠ j loop skipped | yes | none |
| V1.3 | `core.OBS_READING = "R-i"` | yes | none (claims that compute both readings by name keep doing so; only the default reading moves) |
| V1.4 | `core.ident_contract`: ∃(a,b) ∈ C: a ≠ 1 ∧ obs(a,b) ≠ obs(1,b0) | yes | S108-1-I4: where a claim's helper has no b0 (`claims_r3a1.ident`), b0 := the one b with (1,b) ∈ C, else the first in sorted order (on every call site C holds one such b, or none with a ≠ 1) |
| V1.5 | `Question.rho`; under V1.5 `account` adds the conjunct "p is a question" := ρ_p ∈ {selected, constructed} | nearest statable | S108-1-I5: the program records no contract history; a question built without one has ρ_p = declared (I127 applied: neither selected nor constructed). "No candidate of a non-question meets (E)" is read as Acc false with the detail `question F`. Other choice: ρ_p unknown, the case left out (then V1.5 computes nothing) |
| V1.8 | `Roles.slc = Alt` | yes | none |
| V1.1 small case | ℰ_bv | reply gives L_bv at 1 only | S108-1-I1: L_bv at a ≠ 1: (i) "follows" := the one solution of D at (a,b); (ii) "baseline" := L_bv(1,b). Both run |

## 3. The worked cases (rule 5.1): Acc and Account ∧ ¬Dec(t), off and on

Run: `s108_s1_cases.py` (output: `S108 Part A - computation/section 1 runs/cases.txt`). The 27 candidate cases of the written-in step's script, rebuilt, plus E6 (FC63) and the student's copy (FC30.new1 (d)). Dec(t): no worked case carries a history; t's history is set by hand three ways (Θ by hand, I90; `claims_s41.provenance_of`): Dec-history (Expl = F always), Con-history (Expl = Acc), Sel-history on H = {(1,b0)} (Sel reads Faithful_H, D12.1 → D5.7 → (F1) → D1.4).

| variant | worked cases whose Acc moves | direction | Account ∧ ¬Dec(t) moves | Dec(t) (Sel-history) moves |
|---|---|---|---|---|
| V1.1 | 15 of 27: E1 forward on C1, C2, C3; E_rev τ′ on C_H; **E_rev on C_id**; M2; M5; **M13 the weathervane**; E5 both encodings; E8 p_δ; E9 both; **S44 sign, two parts**; the sign with a day port | all T → F (conjunct F1) | the same 15 (Con- and Sel-histories) | 14 cases F → T (Sel fails with (F1) on H), among them E_rev production C1 (Acc F both); M2, M13: Dec stays F; E_rev τ′ on C1: (F1) T → F, Acc F both |
| V1.1 | unchanged: E_tab C1, C2 (F both); E_enc C1, C2; "p because p"; M1; M3; R3-Q1 vane; S44 sign, one part; L257 relabelings; E_rev C1 (F); E_rev τ′ C1 (F) | – | – | – |
| V1.2 | 0 | – | 0 | 0 |
| V1.3 | 0 | – | 0 | 0 |
| V1.4 | 0 | – | 0 | 0 |
| V1.5 | every case with Acc T under none: 22 | T → F (conjunct "p is a question") | the same 22 | 0 |
| V1.5, ρ_p set to constructed (or selected) by hand | 0 | – | 0 | 0 |
| V1.8 | 0 | – | 0 | 0 |

- Unchanged-under-V1.1 pattern (computed, not argued): every case that stays has each commitment's counterpart = J_D (E_enc, E_tab, the lookups, M1, M3, the one-part sign, the hand-turned vane), where V1.1 and I14 agree (I138); every case that moves has a commitment whose counterpart is a proper subnetwork whose own relation is wider than the projection of Sol_D.
- E6 (FC63): (c-i) not as claimed under every reading; (c-ii) as claimed under none, V1.2, V1.3, V1.4, V1.5, V1.8, **not as claimed under V1.1**.
- The student's declared copy (FC30.new1 (d)): Acc(ℰ_fwd) T → F under V1.1 and under V1.5; Dec(t) at the student's holding T under every reading (the copy has no trace; under V1.1 held and Sel's conditions also go F); Account ∧ ¬Dec(t) F under every reading. The student's case never counts as an explanation, off or on.
- The bridge (FC84.new1): no candidate and no (E) is built; Con, Episode, Build are computed from hand-set labels that read no section-1 item. Unchanged under every variant (suite, §8). Under V1.5 the brief's own ρ_p is not recorded, so whether the bridge's question is a question is **not computed** (S108-1-I5 would make it declared).
- E2, E3, E4, E7, the route examples (FC57–FC61, FC64–FC66, FC37–FC40): no candidate's (E) computed; their claims are in the suite (§8).

## 4. The reply's small cases, run (every "after" was marked not run by the reply)

| variant | case | reply's claim | computed | standing |
|---|---|---|---|---|
| V1.1 | E_fwd on C1, C2 | (F1) fails at every pair; out | (F1) fails at 7 of 7 (C1), 15 of 15 (C2); at (1,b1_45) proj Sol_{c_L} = {(1,45°,1)} vs L_cL 9 tuples; Acc T → F | computed |
| V1.1 | ℰ_bv (reading i, "follows") on C1, C2 | out as it stands, in under V1.1 | Acc F → T; under none only (F1) fails (7, 15 pairs); F2, A, Dep, NonVacuous T | computed (on S108-1-I1 (i)) |
| V1.1 | ℰ_bv (reading ii, "baseline") | – | Acc F both (F1, F2, A fail) | the reply's case needs reading (i) |
| V1.1 | E_enc | still meets (F1) | Acc T both | computed |
| V1.1 | E_tab | still fails (F1) where the projection moves | Acc F both | computed |
| V1.1 | E_rev on C_id | not named | Acc T → F: r_H (λ = {c_L}) fails (F1) at 3 of 3 boundaries | **added** |
| V1.2 | a = set(H=2,T=60) | a ∉ Set_H, Set_T before; ∈ both after | F,F → T,T; \|Set_H\| 3 → 143, \|Set_T\| 3 → 143, \|Set_L\| 8 → 128; asg unchanged | computed |
| V1.2 | p* = (D_pole, {(1,b1_45),(a,b1_45)}, Q_L) | Prod F → T; E_fwd meets (E) both | Prod F → T; Acc T, T | computed |
| V1.2 | families on C2* (the reply's unsettled edge) | "whether Slc_j must grow with Set_v" open | R-ii (the reading after round 4): C2 and C2* unchanged (causal c_H, c_L, c_T; no meas, no rule); Slc unchanged (108, 108, 128). R-i: meas (c_L,H), (c_L,T) → none, on C2 and C2* | computed: on the pole D2.6 need not co-vary under R-ii |
| V1.3 | families on C2 | c_L no longer causal; meas (c_L,H), (c_L,T) | causal {c_H,c_L,c_T} → {c_H,c_T}; meas ∅ → {(c_L,H),(c_L,T)}; C1 unchanged; Acc(E_fwd, C2) T both | computed |
| V1.4 | Ident(p_id) on C_id | fails | contract clause T → F on C_id; settings of H, of L, C1: T both | computed |
| V1.4 | E_rev on C_id | still meets (E) | Acc T both | computed |
| V1.5 | E_fwd on C1 | out (declared contract) | ρ_p not recorded: Acc T → F (p no question); ρ_p constructed or selected: T both | computed (on S108-1-I5) |
| V1.8 | families on the pole | Obs = ∅; meas, rule empty; causal list does not move | Slc_j = Alt_j **already** on the pole (every edit altering a pole component replaces it by a slice): V1.8 is idle there; Obs(R-ii) = ∅ both; families unchanged | computed; "happens not to move" holds because nothing moves |
| V1.7 (flagged) | FC34's witness, baseline side only | before: Acc on C ✗, on C′ ✓ (default scope); Σ′ with Excl = ∅: Stated ✗, NonVacuous ✗, Acc ✗ | C: Acc F (F1, F2, A fail); C′ with I85's default scope: Acc T; C′ with Excl(Σ′) = ∅: Acc F (NonVacuous F only) | baseline computed; the "after" is I85's default, which already equals V1.7's formula on every question built without a stated Σ (not implemented, rule 4) |
| V1.6 (flagged) | p′ with Desc′ | – | no Desc is built (I76; FC106 "not tested") | not run: flagged, and no Desc in the program |

## 5. The generated worlds at scale 4 (rule 5.4)

Run: `s108_s1_worlds.py` (and `s108_s1_v11_in.py` for V1.1's moves). `claims_a.gen_p_cand` (gen_org, gen_question, any_candidate: E_enc-built 60%, random 20%, lookup 20%; G-surg and G-free targets), 40 × 4 = 160 models per size, one seeded stream, sizes ascending; candidates built with D1.4 as after round 4 (`S108_S1_GEN=fixed`) and judged off and on. Dec(t): t's history set by hand as a selection on {(1,b0)} (Θ by hand, I90). No part hit a cap (these runs have none).

| world set | models | Acc T under none |
|---|---|---|
| SMALL (108 sizes: ports ≤ 3, dom ≤ 2, comps ≤ 3, \|B\| ≤ 2, edits ≤ 2), seed 108001 | 17,280 | 961 |
| SMALL with value maps, seed 108002 | 17,280 | 886 |
| SMALL, proper targets only (I101), seed 108003 | 1,434 | 221 |
| MID (dom ≤ 3; 162 sizes), seed 108004 | 25,920 | 1,674 |

**Acc and Account ∧ ¬Dec(t)** (candidates whose result differs; the two counts are equal in every run):

| variant | SMALL: in / out | SMALL vm | proper | MID | conjunct that moved | Dec(t) moves (Acc ∧ ¬Dec unchanged there) |
|---|---|---|---|---|---|---|
| V1.1 | 16 / 199 | 13 / 203 | 1 / 30 | 19 / 358 | F1 only | 1,360 / 1,211 / 106 / 2,212 (Sel fails or holds with (F1) on H) |
| V1.2 | 0 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | – | 0 |
| V1.3 | 0 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | – | 0 |
| V1.4 | 0 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | – | 0 |
| V1.5 (ρ_p not recorded ⇒ declared) | 0 / 961 | 0 / 886 | 0 / 221 | 0 / 1,674 | "p is a question" | 0 |
| V1.5, ρ_p constructed by hand | 0 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | – | 0 |
| V1.8 | 0 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | – | 0 |

**Of each kind, SMALL (candidate generator | target family | direction: count, smallest witness's size)**:

| variant | kind | count | smallest |
|---|---|---|---|
| V1.1 | E_enc \| G-free \| out | 100 | ports 1, dom 1, comps 2, \|B\| 2, edits 0 |
| V1.1 | E_enc \| G-surg \| out | 98 | ports 1, dom 1, comps 2, \|B\| 2, edits 0 |
| V1.1 | E_enc \| G-free \| in | 7 | ports 1, dom 1, comps 2, \|B\| 2, edits 2 |
| V1.1 | E_enc \| G-surg \| in | 6 | ports 1, dom 1, comps 3, \|B\| 2, edits 0 |
| V1.1 | random \| G-free \| in | 2 | ports 1, dom 1, comps 3, \|B\| 2, edits 2 |
| V1.1 | random \| G-free \| out | 1 | ports 2, dom 1, comps 3, \|B\| 1, edits 1 |
| V1.1 | random \| G-surg \| in | 1 | ports 1, dom 1, comps 3, \|B\| 2, edits 1 |
| V1.1 | lookup | 0 | (λ = J_D: V1.1 and I14 agree) |
| V1.5 | E_enc \| G-free / G-surg \| out | 439 / 399 | ports 1, dom 1, comps 1, \|B\| 1, edits 1 |
| V1.5 | lookup \| G-free / G-surg \| out | 61 / 53 | ports 1, dom 2, comps 1, \|B\| 1, edits 1 |
| V1.5 | random \| G-free / G-surg \| out | 7 / 2 | ports 1, dom 2, comps 1, \|B\| 2, edits 0 |

Witnesses written out in full: `section 1 runs/worlds.*.json` (field `witness`).

**What V1.1's generated moves are** (`s108_s1_v11_in.py`: the pairs of C where (F1) differs between I14 and V1.1, and whether Sol_D is empty there):

| world set | in: all differing pairs have Sol_D = ∅ | in: none has | out: all have | out: none has | out: some have |
|---|---|---|---|---|---|
| SMALL | 14 | 2 | 124 | 36 | 39 |
| SMALL vm | 12 | 1 | 170 | 17 | 16 |
| proper | 0 | 1 | 1 | 19 | 10 |
| MID | 16 | 3 | 184 | 91 | 83 |

- Where Sol_D(a,b) = ∅, V1.1 makes Sol_N = ∅ for every N, so (F1) asks every active component to be empty there: most generated moves, in and out, are at such pairs.
- The "in" moves at non-empty solutions (2, 1, 1, 3) are the reply's ℰ_bv pattern: a component whose relation is the value D's other components fix (the smallest, SMALL model 104: λ(k0) = {c1}, L_c1 full, k0 = {(0)} at (1,b1) where c0, c2 fix p0 = 0). Printed in `v11_in.*.txt`.
- The "out" moves at non-empty solutions are the pole's pattern: a commitment whose counterpart is a proper subnetwork and whose relation is its counterpart's own, wider than the projection of Sol_D.

**The other items each variant moves, of (D, C, Q) alone** (SMALL; the other sets in the JSONs):

| variant | item | (D, C, Q) where it differs from none (of 17,280) |
|---|---|---|
| V1.1 | D4.4 (FROZEN): sig_C({j}) ≠ sig_C(j) at some pair of C for some j | 7,552 (under I14: 0, by D1.4) |
| V1.2 | Set_v (some port) | 3,284 |
| V1.2 | asg | 1,758 |
| V1.2 | families on C (R-ii) | 1,924 |
| V1.2 | Prod(p) | 549 |
| V1.2 | new (port, setting edit) pairs; of them Sol_D empty at some b | 5,954; 4,129 (old setting edits with Sol_D empty at some b: 1,182) |
| V1.3 | families on C | 57 |
| V1.4 | Ident's contract clause (the designated port as the observed one; Ident itself holds nowhere: the generated queries read a port, not a fibre) | 1,113 |
| V1.8 | families on C | 2,419 |
| V1.8 | a rule family nonempty: under none / under V1.8 | 2,413 / 0 |
| V1.8 | a measurement family nonempty (R-ii): under none / under V1.8 | 169 / 0 |
| V1.5 | none of these (V1.5 reads nothing of D, C, Q but ρ_p) | 0 |

## 6. The external examples FC-E1–FC-E5, the creative transport case CT1–CT8, and the written-in step's case script (rules 5.1–5.3)

Run: each script under `S108_S1_VARIANT=<v>`, output compared line by line with its output under none (= the committed printout). Outputs and diffs: `section 1 runs/scripts/`.

| variant | FC-E1–FC-E5 (`s104_external.py`) | CT1–CT8 (`s104_creative_transport.py`) | written-in step's cases (`s106_cases.py`) |
|---|---|---|---|
| V1.1 | **FC-E1**: the full candidate (Γ = {k, d}) (E) yes → no ((F1) fails); routes {{d,k}} → ∅; d no longer critical or contributory; variants (a), (b) (E) yes → no; "reproduced: no". **FC-E4**: E_readout (E) yes → no on C1 for both Γ ({c_M, c_N, c_Yp} and {c_Yp}): proj Sol_{c_N,c_Y} on (N,Y) at set(N=0,X=1) [(0,0),(0,1)] → [(0,1)] (c_M's M = X now reaches it); "reproduced: no". FC-E2, FC-E3, FC-E5 unchanged | **CT1**: (E) yes → no ((F1)). **CT2**: pairs meeting (E) ['0110/0110','1001/1001'] → []; faithful on H 2 → 0. **CT5**: fidelity survivors 2 → 0; the direct pair on the non-inverting target (E) yes → no. **CT8**: under T′ (Held computed at the output from t's fidelity) R1, R3, R5: constructed → **declared** (Con no): Dec(t) moves; "faithful on H" yes → no. CT3, CT4, CT6, CT7 unchanged | 12 rows move, all (E) after S106 T → F, conjunct F1: E1 forward C1, C2, C3; E_rev τ′ H only; E_rev C_id; M2; M5; M13 weathervane; E5 both; E8; E9 both; S44 two-part sign; the day-port sign; E6 (c-ii) as claimed → not; MOVED count 10 → 7 |
| V1.2 | **FC-E3** (a response and a reading of one port share their families): under R-i every "measurement of X" → none; "both invariant under the settings of X" yes → **no** on every row; with recal(c_N): under R-i they no longer differ; "reproduced: no". Others unchanged | unchanged | unchanged |
| V1.3 | unchanged (FC-E3 computes both readings by name) | unchanged | unchanged |
| V1.4 | unchanged | unchanged | unchanged |
| V1.5 | **FC-E1**: (E) yes → no (p no question), routes → ∅, "reproduced: no"; **FC-E4**: (E) yes → no on C1 for both Γ; conjuncts F1–NonVacuous unchanged | **CT1** (E) yes → no; **CT2** pairs meeting (E) → [] (faithful pairs still 2: fidelity reads no ρ_p); **CT5** the direct pair (E) yes → no; CT8 unchanged (Dec(t) is the transport's, not the contract's) | every row with (E) T → F (no NC1 conjunct moves); E6 (c-ii) → not as claimed; MOVED 10 → 0 |
| V1.8 | **FC-E3** with recal(c_N): c_N's rule family yes → no (R-i, R-ii); under R-ii c_N causal no → yes; "they no longer share their families" yes → **no** under both; "reproduced" stays yes (FC-E3's checks on D_ro unchanged) | unchanged | unchanged |

## 7. The whole suite with each variant on (rule 5, last clause)

Run: `s108_s1_suite.py` under `S108_S1_VARIANT=<v>` (scale 4, cap 45, PYTHONHASHSEED=0; for V1.1 the generator's encodings follow the variant, S108-1-I2), compared with the same run under none by `s108_s1_compare.py` (status per claim; per part the status and the counterexample/witness/result text; model counts and timings not compared). The baseline under none: 133 hold, 2 counterexamples (FC23, FC63), 7 not tested of 142, every claim's status as the committed printout. Other sections' agents ran suites on the same machine at the same time: parts that reached the 45 s cap in any run are listed and re-run alone (§7.1). Comparisons in full: `section 1 runs/suite/compare.<v>.txt`.

| variant | claims whose status moves | parts that move (status or text) | statuses under the variant |
|---|---|---|---|
| V1.1 | 21 | 60 | 112 / 23 / 7 |
| V1.2 | 5 | 10 | 128 / 7 / 7 |

**V1.1** (every move is HOLDS → COUNTEREXAMPLE; claim, its text lines, what moved):

| claim | lines | moved under V1.1 |
|---|---|---|
| FC26 | L325 | the pole's forward candidate on C1, C2: (E) not met |
| FC28 | L325 | E_rev on C_id (both encodings): (F1) fails |
| FC27.new1 | L151, L271 | (d) E_rev under τ′ on C_H: no longer meets every conjunct |
| FC99 | L606 (Argument 7) | the account on C fails already on C ((F1)) |
| FC101 | L616 (Argument 9) | (b) the parallel-route candidate no longer meets (E) on either question |
| FC22 | L141, L255 | (b) S41 Q15's weathervane M13: (E) not met ((F1)) |
| FC23.new1, FC23.new2, FC23.new3, FC23.new5 | written-in step | the pole, the round-2 models, E5, **S44's two-part sign** ((a): "an explanation under (E)" → not met), (f) S41 Q2's declared-link case, the one-part target's sign |
| FC62 | L339 | the eliminative explanation (E5): (F1) fails |
| FC72.new2 | L317 | (a) the axial tilt ℰ_tilt (E) T → F, ℰ_myth2 T → F, **ℰ_myth1 (the myth with a written-in "bargain" slot) stays T**; (d) the finer question's test |
| FC30.new1 | L17, L536 | (a), (d), (e), (g), (h): Acc(ℰ_fwd) F, so the defeat-set parts built on it change |
| FC85 | L413, L416 | **(a) c ≡ c: the identity transport c → c is not faithful** (smallest: two components on one port, one empty); D13.4's reflexivity fails |
| FC95 | L211 | a system can represent a theory in error: no faithful transport o → c |
| FC12.new2, FC12.new3 | D12.1, D12.2 | provenance with Held and Sel's conditions computed from fidelity: Sel, Con → Dec |
| FC42.new1 | D7.4 | Boundary: every E_v fails (E); \|Boundary\| → 0 |
| FC90.new1 | D13.3, (EX) | Acc(ℰ_fwd), Acc(ℰ_rev) F; the "claim must hold" readings lose Build/(EX) |
| FC102.new1 | E9 | (c) t1 no longer meets (F1), (F2) on the extended contract |
| FC104.new1 | L220 | (a), (b): (F1) fails at every pair of the pole's H |
| also moved, status kept | | FC12.new1, FC83 (witness parts: no witness), FC19, FC23 (c), (d), FC23.new4, FC27, FC42.new1 (c), FC63 (c-ii) → not as claimed, FC78, FC81, FC82, FC97.new1, FC103.new1, FC107, FC18 (only its I94 look) |
| **not moved** (among those the reply names or the worked cases use) | | FC17, FC18 (Argument 1: sig(λ(k)) reads Sol_{λ(k)} and follows the variant), FC21, FC25, FC25.new2, FC30, FC34, FC106 |

**V1.2**:

| claim | lines | moved under V1.2 |
|---|---|---|
| FC06 | L119 (L119.n8), L124 | HOLDS → CEX: "a setting edit leaves every reader's relation as it was": [alt:k0] sets p0 through h_p0 and alters k0 |
| FC09 | L121, **L347** | HOLDS → CEX: L347's rule relation c_r loses Rule_C (and its measurement) under both readings: families {causal h_z, meas (c_r,z), rule c_r} → {causal h_z} |
| FC2.new1 | L109, L123 | HOLDS → CEX: under R-i a reader of an assigned port is causal (c0 on (p0,p1)) |
| FC4.new1 | L127 | HOLDS → CEX, both readings |
| FC07 | L123 | HOLDS → CEX: the pole's C2 under R-i: c_L's measurements lost; C2* text changes |
| FC08 | L127 | the witness (a measurement whose reading does not follow) no longer found |
| FC23.new2 | S44 | (a) text only: the slot reading "some-exempt-set" (reads D2.1) drops u; (E) unchanged |

