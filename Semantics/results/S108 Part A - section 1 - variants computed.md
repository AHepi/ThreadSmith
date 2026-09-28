# S108 Part A - section 1 - variants computed

*Computing agent for section 1 (rule 5 of `S108 Part A - how the replies will be read, written before sending.md`), Opus 5.5, 28 September 2026. Fresh. Works only in `S108 Part A - computation/section 1 model/` (a copy of `S107 Round 4 - maths after the reading/model after round 4/`). Nothing here changes the theory (rule 11). "Candidate" or "explanation" for what the theory judges; "model" only for the program or a small structure it builds (S43).*

Status: complete, 28 September 2026. Filled as it went; nothing ruled.

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
- Other candidates on the same questions (computed, `s108_s1_cases.py`, §B): on M13's (the weathervane's) question E_enc meets (E) under none and V1.1, not under V1.5; on S44's sign question the one-part sign and E_enc meet (E) under none and V1.1, none of the three under V1.5; the two-part sign under none only.
- E6 (FC63): (c-i) not as claimed under every reading; (c-ii) as claimed under none, V1.2, V1.3, V1.4, V1.5, V1.8, **not as claimed under V1.1**.
- The student's declared copy (FC30.new1 (d)): Acc(ℰ_fwd) T → F under V1.1 and under V1.5; Dec(t) at the student's holding T under every reading (the copy has no trace; under V1.1 held and Sel's conditions also go F); Account ∧ ¬Dec(t) F under every reading. The student's case never counts as an explanation, off or on.
- The bridge (FC84.new1): no candidate and no (E) is built; Con, Episode, Build are computed from hand-set labels that read no section-1 item. Unchanged under every variant (FC84.new1 moves in no suite run, §7). Under V1.5 the brief's own ρ_p is not recorded, so whether the bridge's question is a question is **not computed** (S108-1-I5 would make it declared).
- E2, E3, E4, E7, the route examples (FC57–FC61, FC64–FC66, FC37–FC40): no candidate's (E) computed; none of their claims moves under any variant (§7).

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

Witnesses written out in full: `section 1 runs/worlds/worlds.*.json` (field `witness`).

**What V1.1's generated moves are** (`s108_s1_v11_in.py`: the pairs of C where (F1) differs between I14 and V1.1, and whether Sol_D is empty there):

| world set | in: all differing pairs have Sol_D = ∅ | in: none has | out: all have | out: none has | out: some have |
|---|---|---|---|---|---|
| SMALL | 14 | 2 | 124 | 36 | 39 |
| SMALL vm | 12 | 1 | 170 | 17 | 16 |
| proper | 0 | 1 | 1 | 19 | 10 |
| MID | 16 | 3 | 184 | 91 | 83 |

- Where Sol_D(a,b) = ∅, V1.1 makes Sol_N = ∅ for every N, so (F1) asks every active component to be empty there: most generated moves, in and out, are at such pairs.
- The "in" moves at non-empty solutions (2, 1, 1, 3) are the reply's ℰ_bv pattern: a component whose relation is the value D's other components fix (the smaller of SMALL's two, at ports 1, dom 2, comps 2, |B| 1, edits 2, index 89: λ(k1) = {c1}, L_c1(e1,b0) full, L_k1(e1,b0) = {(0)}, the value c0 fixes at e1). Printed in `section 1 runs/worlds/v11_in.*.txt`.
- The "out" moves at non-empty solutions are the pole's pattern: a commitment whose counterpart is a proper subnetwork and whose relation is its counterpart's own, wider than the projection of Sol_D.

**The other items each variant moves, of (D, C, Q) alone** (SMALL; the other sets in the JSONs):

| variant | item | (D, C, Q) where it differs from none (of 17,280) |
|---|---|---|
| V1.1 | D4.4 (FROZEN): sig_C({j}) ≠ sig_C(j) at some pair of C for some j | 7,552 (under I14: 0, by D1.4) |
| V1.2 | Set_v (some port) | 3,284 |
| V1.2 | asg | 1,758 |
| V1.2 | families on C (R-ii) | 1,924 |
| V1.2 | Prod(p) | 549 |
| V1.2 | Input (some port) | 2,107 |
| V1.2 | Slc_j (some j) | 881 |
| V1.2 | Obs (R-ii) | 18 |
| V1.2 | new (port, setting edit) pairs; of them Sol_D empty at some b | 5,954; 4,129 (69%). On the same targets the old pairs: 3,571; 1,182 (33%) |
| V1.3 | families on C | 57 |
| V1.4 | Ident's contract clause (the designated port as the observed one; Ident itself holds nowhere: the generated queries read a port, not a fibre) | 1,113 |
| V1.8 | families on C | 2,419 |
| V1.8 | Slc_j (some j) | 4,593 |
| V1.8 | Obs (R-ii) nonempty: under none / under V1.8 | 17 / 0 |
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
| V1.3 | 0 | 2 (text only) | 133 / 2 / 7 |
| V1.4 | 3 | 3 | 130 / 5 / 7 |
| V1.5 | 15 | 53 | 118 / 17 / 7 |
| V1.8 | 1 | 1 | 132 / 3 / 7 |

**V1.1** (every move is HOLDS → COUNTEREXAMPLE; claim, its text lines, what moved):

| claim | lines | moved under V1.1 |
|---|---|---|
| FC26 | L325 | the pole's forward candidate on C1, C2: (E) not met |
| FC28 | L325 | E_rev on C_id (both encodings): (F1) fails |
| FC27.new1 | L151, L271 | (d) E_rev under τ′ on C_H: no longer meets every conjunct |
| FC99 | L606 (Argument 7) | the account on C fails already on C ((F1)) |
| FC101 | L616 (Argument 9) | (b) the parallel-route candidate no longer meets (E) on either question |
| FC22 | L141, L255 | (b) S41 Q15's weathervane M13: (E) not met ((F1)) |
| FC23.new1, FC23.new2, FC23.new3, FC23.new5 | written-in step | the pole, the round-2 cases M1–M5, E5, **S44's two-part sign** ((a): "an explanation under (E)" → not met), (f) S41 Q2's declared-link case, the one-part target's sign |
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

**V1.3**: no status moves. Text only: FC2.new1 (the pole's c_L) and FC4.new1 (the pole's C1) print the default reading's name (R-ii → R-i); their values are the same (both claims compute both readings by name).

**V1.4**:

| claim | lines | moved under V1.4 |
|---|---|---|
| FC28 | L325 | HOLDS → CEX: "second check (R4): C_id is an identification contract under D3.3": the contract clause on C_id T → F (the printout's word "varies" now prints the clause's value) |
| FC28.new1 | L151 | HOLDS → CEX: (a) Ident on the pole: C_id T → F; settings of H, of L T both; (b) N3 unchanged (obs equal at both pairs under either clause) |
| FC28.new2 | – | HOLDS → CEX: B6's vane, still/north: Ident ('bot') T → F (no edit a ≠ 1 in a contract of boundaries only); "the three readings agree on the pole's C_id" T → F |

**V1.5** (every question the claims build has no recorded contract history, so is declared, S108-1-I5): every claim that asks (E) of a candidate moves where (E) was met: FC22 (b) (S41 Q15's M13), FC23 (c)–(e), FC23.new1 (a)–(d), (f)–(h), FC23.new2 (a), (b), (f), FC23.new3 (d), FC23.new5 (b), (c), FC25.new2 (a), (c) (E_enc), FC26, FC27.new1 (d), FC30.new1 (a), (d), (e), (g), (h), FC42.new1, FC62, FC63 (c-ii), FC72.new2 (a), (c), (d), FC90.new1 (a), (c), FC99, FC101 (b); witness parts lost: FC34 (all four: Acc is F on every question), FC74 (bearing is relative to p). Not moved: every claim that reads fidelity, provenance or families without (E) (FC85, FC95, FC12.*, FC06–FC09, FC17–FC19, FC27's status).

**V1.8**: FC09 (L121, L347) HOLDS → CEX: L347's rule relation c_r: under R-i rule lost (measurement kept); under R-ii c_r becomes causal, measurement and rule lost. Nothing else moves (V1.8 is idle on the pole; FC07, FC2.new1, FC4.new1 unchanged).

### 7.1 Parts that reached the 45 s cap

Under contention (other sections' suites on the same four CPUs) these parts reached the cap in some run: FC70 (none, V1.1, V1.2, V1.3, V1.4, V1.5, V1.8), FC56 (a), (c) (V1.1–V1.5), FC66 (a) (V1.1), FC23.new1 (c), (d), (f) (V1.5). None changed status. FC23.new1's three parts under V1.5 search for a candidate meeting round 3's (E), which asks Acc, false on every question under V1.5: no witness can exist, so the cap hides nothing. FC56, FC66, FC70 re-run under every reading, two runs at a time, cap 300 (`section 1 runs/suite/capped300.<v>.json`): no part reached the cap (FC56 67–71 s, FC66 15–16 s, FC70 13–15 s, as the printout's 69, 16, 13 s); under every variant every part's status, counterexample/result text and number of models tried equals none's. So the caps hid nothing.

## 8. The edges (rule 5): the reply's, marked; and those the computation adds

Standing: **computed** (the computation shows it), **contradicted** (it shows otherwise), **not settled by computation** (with what would settle it); **added**: shown by the computation, not named by the reply. Marks are the template's. The `.json` beside this file holds every row.

### V1.1 (D1.4: Sol_N := the projection of Sol_D)

| kind | item [mark] | the reply's why (cut) | standing | evidence |
|---|---|---|---|---|
| blocks | D4.4 [FROZEN] ("extends (K)") | for N = {j}, sig becomes the full-solution projection, not L_j | computed | sig_C({c_L}) ≠ sig_C(c_L) at 7 of 7 pairs of C1, 15 of 15 of C2; generated SMALL: 7,552 of 17,280 (D, C) have sig_C({j}) ≠ sig_C(j) for some j (I14: none) |
| constrains | D5.2 [FROZEN] | proj^λ readable; siblings' constraints reach it | computed | FC-E4 at set(N=0,X=1): proj Sol_{c_N,c_Y} on (N,Y) [(0,0),(0,1)] → [(0,1)]: c_M's M = X enters; D5.2's formula unchanged |
| changes with | L233.s1 [S2] | "imposing the constraints of λ(k)" words the old reading | not settled by computation | a wording point: whether "imposing the constraints of λ(k)" still describes proj Sol_D|V_N; settled by reading L233.s1 against the variant, not by a run |
| changes with | L556.n2 [S4] | Argument 1's signatures recomputed | not settled by computation | its formula reads Sol_{λ(k)} and follows the variant with no change of form; whether the sentence still says what Argument 1 needs is a reading |
| changes with | FC17, FC18 | Argument 1's claims must be recomputed | **contradicted** | recomputed: FC17 and FC18 hold under V1.1 (sig(λ(k)) reads Sol_{λ(k)}, so (F1) still makes k's signature its counterpart's); only FC18's I94 look changes its witness |
| moves | (F1): what it reads | E_fwd out, ℰ_bv in | computed | E_fwd Acc T → F on C1, C2, C3; ℰ_bv F → T on C1, C2 under S108-1-I1 (i); under (ii) F both |
| moves | Acc and being an explanation on 15 of 27 worked cases | – | **added** | §3: E_rev on C_id (L325.n6, L271.s2), M2, M5, M13 (S41 Q15), E5 ×2 (L339), E8 (FC107), E9 ×2 (L626, L630), S44's two-part sign, the day-port sign, E_rev τ′ on C_H; E6 (c-ii); FC-E1, FC-E4; CT1, CT2, CT5 |
| changes with | D12.1 Sel [S2] → D12.3 Dec(t) [S2] (through Faithful_H, D5.7) | – | **added** | Dec(t) under a hand-set selection history moves in 14 worked cases and 1,360 / 1,211 / 106 / 2,212 generated; CT8 under T′: constructed → declared; FC12.new2, FC12.new3, FC104.new1 move. Account ∧ ¬Dec(t) moves only where Acc moves (Acc ⇒ Faithful_C ⇒ Faithful_H, so where Acc holds under a reading Sel's fidelity clause holds too): equal counts in every run |
| blocks | D13.4 [FROZEN] (≡ reflexive: "a content matches itself") | – | **added** | FC85 (a) HOLDS → counterexample: the identity transport c → c is not faithful (two components on one port, one empty); so D13.5 (N) [FROZEN] reads a content as not matching itself |
| constrains | D12.5 Rep [FROZEN] | – | **added** | FC95 (a system represents a theory in error, L211): no faithful transport o → c under V1.1 |
| changes with | D7.2 routes, D7.3 (B) [FROZEN]; D7.4 Boundary [S2] | – | **added** | FC-E1: routes {{d,k}} → ∅, d no longer critical; FC42.new1: \|Boundary\| → 0 |
| moves | which of rival candidates meet (E) on K1 (L317; D8.3, D10.1) | – | **added** | FC72.new2 (a): ℰ_tilt T → F, ℰ_myth2 T → F, ℰ_myth1 (a written-in slot, "bargain") stays T; (d) the finer question's test moves |
| moves | Arguments 7, 9 (L606, L616) | – | **added** | FC99 (the account fails already on C), FC101 (b) |
| moves | which generated candidates meet (E) | – | **added** | §5: out 199, in 16 (SMALL); most at pairs where Sol_D = ∅; the ins at non-empty solutions write in a value D's other components fix (ℰ_bv's pattern) |

### V1.2 (D2.1: the k ≠ j clause deleted)

| kind | item [mark] | the reply's why (cut) | standing | evidence |
|---|---|---|---|---|
| blocks | L103.s2 [FROZEN] | a setting that alters k "adds an equation beside" | not settled by computation | computed both ways: every setting edit under V1.2 still replaces its assigning component (L_j(a,b) is the slice, by D2.1), so none leaves j's old equation beside the slice; but of 5,954 new (port, setting edit) pairs (SMALL), 4,129 (69%) leave Sol_D empty at some b; on the same targets the old pairs 3,571, of which 1,182 (33%). Settled by a reading: does "beside an incompatible one" cover an alteration of another component that leaves no solution? |
| constrains | D2.2 [FROZEN] | Input stays readable; its extension grows | computed | Input differs on 2,107 of 17,280 generated targets (it can only grow); on the pole all three ports are inputs both ways |
| constrains | D2.5 [FROZEN] | dir readable; grows with Set_v | computed | asg (dir's second part) differs on 1,758 of 17,280; the pole's asg unchanged |
| changes with | D2.6 [S1] | Slc_j reads Set_v | computed, in part | Slc_j reads asg, not Set_v: it moves only where asg moves (asg 1,758, Slc 881 of 17,280); pole: unchanged (108, 108, 128) |
| changes with | D2.4 [S1] | Obs reads Set_v | computed | Obs (R-ii) excludes Set_o (and Slc): it moves on 18 of 17,280; pole: 0 both ways |
| changes with | E1's I04 [S2]: "each replacing its component", "the production contract" | re-read | computed | E1's edits still replace their components; composites now set each port they set (\|Set_H\| 3 → 143); Prod(p*) F → T; C1's Prod unchanged |
| changes with | FC27.new1 [claims S1, S2] | – | **contradicted** | FC27.new1 unchanged under V1.2 (every part, status and text) |
| changes with (open in the reply) | whether D2.6 must co-vary to keep L57's split | "a computation of families under the grown Set on C2* would settle" | computed | on the pole's C2*, R-ii: families unchanged (causal c_H, c_L, c_T; no meas, no rule) with Slc unchanged: no co-variation needed there. But on L347's own case (FC09) the rule family is lost under V1.2 with Slc as it stands (next row): there L57's split is not kept |
| moves | no conjunct of (E); the respect "production" | – | computed | Acc: 0 moves (worked cases, scripts, 61,914 generated candidates); Prod moves on 549 of 17,280 |
| blocks | L347.s2 [FROZEN] | – | **added** | FC09 HOLDS → counterexample: c_r (L347's rule relation) loses Rule_C under both readings (World_{c_r} now holds edits that alter c_r) |
| blocks | L119.n8 [S1] ("replaces only the component that assigns the port, … not the relations of the components that read it") | – | **added** | FC06 HOLDS → counterexample: [alt:k0] sets p0 through h_p0 and alters k0 |
| changes with | L109, L123, L127 (FC2.new1, FC4.new1, FC07, FC08) [S1] | – | **added** | FC2.new1 (R-i part), FC4.new1 (both readings), FC07 (C2 under R-i) → counterexample; FC08's witness lost |
| changes with | FC-E3 (external 2.3) | – | **added** | every row "both invariant under the settings of X" yes → no; "reproduced: no" |

### V1.3 (D2.4: R-i the one reading)

| kind | item [mark] | the reply's why (cut) | standing | evidence |
|---|---|---|---|---|
| constrains | L124.s1 [FROZEN], L125.s1 [FROZEN] | families stay definable; extensions shift | computed | the pole's C2: causal {c_H,c_L,c_T} → {c_H,c_T}, meas ∅ → {(c_L,H),(c_L,T)}; generated: families differ on 57 of 17,280 (SMALL), 143 of 25,920 (MID) |
| changes with | L123.n1 [S1], D4.6 [S1] | the causal gloss excludes readers of assigned ports | computed | FC2.new1's for-all part (R-i: no reader of an assigned port is causal) holds and is now the default reading's; §4 |
| moves | nothing in (E) | the reading never reaches the account | computed | Acc: 0 moves on the worked cases, the three scripts, 61,914 generated candidates; the whole suite: no status moves |

### V1.4 (D3.3: Ident's contract clause ∃(a,b) ∈ C: a ≠ 1 ∧ obs(a,b) ≠ obs(1,b0))

| kind | item [mark] | the reply's why (cut) | standing | evidence |
|---|---|---|---|---|
| constrains | L151.s1 [S1], L151.s2 [FROZEN] | "fixed by the type of Q and the shape of C" and Prod untouched | computed | Prod moves on 0 generated questions under V1.4; the clause still reads only (Q, C, b0) |
| changes with | E1's C_id [S2], L271.s2 [S2], L325.n6 [S2] | the identification reading of C_id moves | computed | C_id's clause T → F (§4; FC28's R4 part, FC28.new1 (a)); E_rev's faithfulness on C_id unchanged (Acc T both), so L325.n6's "faithful under the identification contract" names a contract D3.3 no longer calls one |
| changes with | FC28, FC28.new2 | – | computed | both HOLDS → counterexample; FC28.new1 too (not named) |
| moves | what meeting (E) says on C_id; Acc unchanged | – | computed | Acc: 0 moves anywhere; the contract clause moves on 1,113 of 17,280 generated (C, b0) |
| changes with | D3.3's obs with ⊥ (I172, B6; Q15's convention) [S1] | – | **added** | FC28.new2's still/north (boundaries only; obs ⊥ then n) is an identification contract under I163 and not under V1.4 (no a ≠ 1): I172's ⊥-reading of obs then decides nothing on a contract with no edit; the 'three readings agree on C_id' check flips |

### V1.5 (D3.4: ρ_p ∈ {selected, constructed})

| kind | item [mark] | the reply's why (cut) | standing | evidence / what would settle |
|---|---|---|---|---|
| blocks | L155.s2 [S1], L155.s5 [S1] | declared contracts and "any assessment may use any of the three" negated | not settled by computation | holds by the variant's own wording (it removes the value L155.s2 defines); there is nothing to run |
| constrains | L155.s6 [FROZEN], D3.1 [FROZEN] | found ⇒ constructed stays readable; ρ_p's slot stays | not settled by computation | the program builds no Found and records no ρ_p (only S108-1-I5's default); settled by encoding a found question with its trace |
| changes with | D13.8 q(o)/Rec [S3] | episode records quantify over non-declared contracts | not settled by computation | the program's Episode reads q(o) and records as hand-set labels with no ρ_p; the bridge's brief (FC84.new1) is unchanged. Settled by giving q(o) a ρ_p and computing Episode and Con under V1.5 |
| changes with | D16.4 𝔓^adv [S4] | – | not settled by computation | 𝔈_Θ quantifies Acc over questions; no claim computes 𝔈_Θ itself: FC94 (recursion does not entail universality) does not move, FC110 is not tested (FC42.new1, FC90.new1, which cite D16.4, move through Acc). Settled by a finite 𝔈_Θ over the program's questions with ρ_p recorded |
| changes with | (QF) L544 [S4] | – | not settled by computation | 'fails to capture', 'not creative' have no definition (D16.XV) |
| changes with | E8 [FROZEN] | – | computed | E8's p_δ candidate: Acc T → F (§3); FC107's text moves |
| moves | which questions exist | candidates on declared-contract questions stop meeting (E) | computed | every Acc-T worked case (22), FC-E1, FC-E4, CT1, CT2, CT5, all generated (961 / 886 / 221 / 1,674) → F; with ρ_p set to selected or constructed by hand: 0 moves; the asymmetry the reply names (ρ_p unread by (E), Dec(t) read by being an explanation) is computed: (E) reads ρ_p only through V1.5's added conjunct |
| moves | the owner's own examples | – | **added** | S44's sign (two-part, one-part, E_enc on its question) and S41 Q15's weathervane (M13, E_enc) all F: nothing on those questions meets (E) unless their contracts' history is recorded (§9) |
| changes with | FC34 (L151's "an answer to one is not an answer to the other", D3.7), FC74 (bearing relative to p, D9.10) | – | **added** | their witnesses are no longer found: no candidate meets (E) on any question the searches build |

### V1.8 (D2.6: Slc_j := Alt_j)

| kind | item [mark] | the reply's why (cut) | standing | evidence |
|---|---|---|---|---|
| blocks | L347.s2 [FROZEN] | Changes_C(j, Alt_j ∖ Slc_j) = Changes_C(j, ∅) is false, so no rule relation is variable under edits to itself | computed | FC09 HOLDS → counterexample: L347's c_r loses Rule_C under both readings; generated: a rule family nonempty on 2,413 of 17,280 under none, on 0 under V1.8 |
| constrains | L57.s1 [FROZEN] | the rule/cause difference stays definable; the rule side is empty | computed | rule and (R-ii) measurement families empty on every generated (D, C) (2,413 and 169 → 0); causal families stand |
| changes with | D4.6 [S1], L123.n1 [S1] | families' form unchanged, extensions empty | computed | families differ on 2,419 of 17,280; Obs (R-ii) nonempty 17 → 0 |
| moves | nothing in (E) | – | computed | Acc: 0 moves anywhere |
| moves (the reply's trace) | "on the pole the causal list happens not to move" | – | computed, for another reason | on the pole Slc_j = Alt_j already (every edit that alters a pole component replaces it by a slice): V1.8 changes nothing there |
| changes with | FC-E3 (external 2.3, the recalibration case) | – | **added** | with recal(c_N) in the contract: c_N's rule family yes → no; under R-ii c_N causal no → yes; "they no longer share their families" yes → no under both readings |

### V1.6 and V1.7 (flagged by the tabulation, §6; not implemented, rule 4)

| variant | kind | item [mark] | standing | what would settle it |
|---|---|---|---|---|
| V1.6 | constrains | L161.s1–s3 [FROZEN], D6.6 [FROZEN] | not settled by computation | the orchestrator's ruling on scope and on S40 (a new sentence); then a Desc (I76) built for the worked cases, and BadTarget/BadReq computed on them |
| V1.6 | changes with | D16.XV (Suff)/(Nec) [S4], FC106 [S1] | not settled by computation | as above; FC106's two untested defects need Desc |
| V1.6 | moves | being an explanation (gains ¬BadTarget ∧ ¬BadReq) | not settled by computation | as above; the reply's formula (on Acc) and trace (on being an explanation) are two variants (tabulation §11) |
| V1.7 | blocks | D3.5 [FROZEN], L43.s4 [S1], L159.s1 [S1] | not settled by computation (flagged) | the orchestrator's ruling (V1.7 turns D3.5's declared input into a definition). Baseline computed: the reply's case under none gives Acc F with Excl(Σ′) = ∅ (NonVacuous F alone), Acc T with I85's default scope |
| V1.7 | constrains | D6.6 [FROZEN] | not settled by computation (flagged) | as above. Observation, no implementation: every question the program builds has Excl(Σ) = (A×B)∖C: I85's default everywhere, E6's stated Excl = ∅ with C = A×B (the same set), and claims_b's renamed copies carry theirs (grep of the copy); I85 already is V1.7's formula there, so V1.7 would move no case the program builds; only a question stating an Excl smaller than (A×B)∖C, like the reply's Σ′ run here, moves |
| V1.7 | changes with | none required; L317.s15 [FROZEN] safe | not settled by computation (flagged) | as above |
| V1.7 | moves | NonVacuous's second conjunct (reads nothing) | not settled by computation (flagged) | as above; the baseline side (the narrowing caught, Acc F) is computed |

### Edge counts

58 rows in the JSON: computed 25, contradicted 2 (V1.1's FC17/FC18; V1.2's FC27.new1), not settled by computation 15 (7 of them V1.6's and V1.7's, flagged), added 16.

## 9. What the computation says of each variant and the explanation definition (for the map; nothing ruled)

| variant | which candidates meet (E) | being an explanation (Account ∧ ¬Dec(t)) | what else moves | owner's decisions the computed effect sits against (named, not ruled; rule 13) |
|---|---|---|---|---|
| V1.1 | **moves**: out 15 of 27 worked cases (mechanisms whose counterpart is a proper subnetwork), FC-E1, FC-E4, CT1, CT2's two pairs; in: ℰ_bv (a component carrying the value D's other components fix), and generated candidates at pairs with no solution; unchanged: every candidate whose counterparts are J_D (E_enc, lookups, "p because p", the one-part sign) | moves exactly where Acc moves; Dec(t) moves on its own through Sel's fidelity, never alone moving Account ∧ ¬Dec(t) | D4.4 (FROZEN), D13.4's reflexivity (FROZEN), Rep, routes, Boundary, provenance claims, Arguments 7 and 9 | S44 ("In either case, it is an explanation"): the two-part sign stops meeting (E), so is no explanation, while the one-part (written-in) sign and E_enc on the sign's question stay; S41 Q15 ("Yes, it can be explained"): the weathervane's mechanism M13 stops meeting (E) (FC22 (b)), but E_enc on the same question still meets it (computed), so something still counts; on K1 the written-in myth keeps (E) and the tilt loses it (FC72.new2), which S44/S45 do not decide either way |
| V1.2 | unchanged everywhere | unchanged | Set_v, asg, Input, Slc, Obs, families, Prod; FC06, FC09 (L347.s2 FROZEN), FC2.new1, FC4.new1, FC07, FC08, FC-E3 | none computed |
| V1.3 | unchanged everywhere | unchanged | families (the pole's C2: c_L causal → measurement); (suite: §7) | none computed |
| V1.4 | unchanged everywhere | unchanged | Ident's contract clause (C_id no longer an identification contract; 1,113 of 17,280 generated contracts); (suite: §7) | none computed |
| V1.5 | **moves**: every candidate of a question whose contract has no recorded selected or constructed history: all 22 worked cases that met (E), FC-E1, FC-E4, CT1, CT2, CT5, every generated one (961 / 886 / 221 / 1,674); with ρ_p set by hand to selected or constructed nothing moves ((E) reads no ρ_p) | moves exactly where Acc moves | nothing of (D, C, Q) | S44: under S108-1-I5 no candidate on the sign's question meets (E) (two-part, one-part, E_enc: all F, computed), so none is an explanation; S41 Q15: on the weathervane's question neither M13 nor E_enc meets (E) (computed), so nothing counts as explaining "north" unless the contract's history is recorded; S41 Q6 (the bridge's fixed brief): not computed, the brief's ρ_p is not recorded |
| V1.8 | unchanged everywhere | unchanged | rule and measurement families empty everywhere (2,413 and 169 of 17,280 → 0); idle on the pole (Slc_j = Alt_j there already); FC-E3's recal case | none computed |

## 10. Unsure

- S108-1-I5 (a question with no recorded contract history is declared) decides V1.5's whole effect; under its other choice (ρ_p unknown, left out) V1.5 computes nothing on any case the program builds. The program records no contract history anywhere (ρ_p is in D3.1 and nowhere in the code).
- S108-1-I1 (ℰ_bv's relation at a ≠ 1) decides whether the reply's ℰ_bv becomes an account: yes under (i), no under (ii).
- S108-1-I2: in the whole suite under V1.1 the generator's encodings follow the variant; the generated-worlds comparison holds them fixed. A suite run with them fixed was not made.
- Dec(t) on the worked cases and the generated worlds is computed on histories set by hand (Θ by hand, I90), as the program's own claims do; no worked case carries a history of its own except the student's copy, the bridge and CT8.
- The suites ran beside other sections' suites on four CPUs; parts that reached the 45 s cap are listed and re-run alone (§7.1). A counterexample found is not a timing effect; a "holds" under a cap is fewer models tried.
- "Smallest witness" is the first found in ascending size order, as the harness takes it, not a minimum over all models.
- V1.4 on the generated worlds reads Ident's contract clause on the designated port; the generated queries read a port, so Ident itself (a fibre query) holds under no reading there.
- Silence is not agreement (rule 3): items no variant of section 1 touched are not shown free of dependencies.

Computed by one Opus 5.5 agent under rule 5, 28 September 2026. Nothing here changes the theory's text, formal core, claims or program after round 4 (rule 11).
