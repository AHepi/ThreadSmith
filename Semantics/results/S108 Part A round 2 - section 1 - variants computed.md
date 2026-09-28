# S108 Part A round 2 - section 1 - variants computed

*Computing agent for section 1 (rule 5 of `S108 Part A round 2 - how the replies will be read, written before sending.md`; Opus 5.5 per `S108 Part A round 2 - who computes, recorded before any reply is opened.md`), 28 September 2026. Fresh. Works only in `S108 Part A round 2 - computation/section 1 model/` (a copy of round 1's `S108 Part A - computation/section 1 model/`, all 31 files md5-identical at the copy; round 1's copy never written). Runs in `S108 Part A round 2 - computation/section 1 runs/`. Nothing here changes the theory (rule 11). "Candidate" or "explanation" for what the theory judges; "model" only for the program or a small structure it builds (S43). Read with the reply (`s108r2_glm_section1.response.txt`, a3bd9ffd…) and the tabulation (§2–§8).*

Status: complete, 28 September 2026. Filled as it went; nothing ruled. The whole-suite runs are the harness's (§6): spec written and validated, brief returned, not run here.

## 0. Setup

| item | state |
|---|---|
| copy | round 1's section 1 copy, 31 files identical (md5 list compared) |
| round 1's switches kept | `S108_S1_VARIANT` (V1.1, V1.2, V1.3, V1.4, V1.5, V1.8), `S108_S1_GEN` |
| round 2's switches (`model/core.py`) | `S108R2_S1_VARIANT` ∈ {none, R2V1.1, R2V1.6, R2V1.6s}; `S108R2_S1_RHO` ∈ {declared, selected, constructed}; `S108R2_S1_I1` ∈ {follows, baseline, iii}. Hooks: `rho_of`, `is_question`, `adn`, `expl_base`, `defeat_base`; routed in `claims_s106` (FC23.new2 (f)) and `claims_s41` (FC30.new1 (a)–(h)) |
| default unchanged | under every switch off: `s104_external.py`, `s104_creative_transport.py`, `s106_cases.py` print the committed md5s (86a67664…, d473944e…, 043aeb36…); round 1's `s108_s1_cases.py` prints round 1's `cases.txt` byte for byte |
| scripts (in the copy) | `s108r2_s1_cases.py` (§3, §4, §7), `s108r2_s1_worlds.py` (§5), `s108r2_s1_suite_check.py` (the harness's check step, §6); in `section 1 runs/`: `s108r2_s1_specs.py` (writes the specs), `suite - expected moves.json` |
| runs | PYTHONHASHSEED=0, `timeout` on every run; outputs in `section 1 runs/` (cases, worlds, scripts, single) |

## 1. Which variants are implemented (tabulation §2, §7)

| id | item or reading | tabulation flag | implemented | why |
|---|---|---|---|---|
| R2V1.1 | S108-1-I5: ρ_p a recorded field; V1.5's conjunct kept | none | **yes** | in scope; a reading C2 rests on (rule 5.i) |
| R2V1.2 | D3.4.v2: Found(p′) :⟺ ρ = constructed | possible, in effect L155.s6 [FROZEN] | no | rule 4; its case is computed as e1.37's settlement with D3.4 as written (⇒), §7 |
| R2V1.3 | the bridge's brief, ρ read by Episode | in effect D13.8 [S3] | no | rule 4; e1.38 computed with D13.8 as written, and C2's S41 Q6 flag through D14.7's Acc (R2V1.1), §3, §7 |
| R2V1.4 | Found at selected | in effect L155.s6 [FROZEN] | no | rule 4 |
| R2V1.5 | L17.s1 without (iii) | in effect D16.XV [S4] | no | rule 4 |
| R2V1.6 | L11.s1: Expl := (A) ∧ Dependence ∧ NonVacuous ∧ ¬Dec(t) | none | **yes** (+ R2V1.6s) | in scope |
| R2V1.7 | L119.s1: ~_C without β | in effect D4.2 [FROZEN] | no | rule 4 |
| R2V1.8 | L141.n3: Y_p := X_δD | possible, in effect D3.2, E4 [FROZEN] | no | rule 4 |
| R2V1.9 | L159.s3 / D3.1: Question ⇒ Θ admits C | as written D3.1 [FROZEN] | no | rule 4 |
| R2V1.10 | S108-1-I1, reading (iii) | none | **yes** | in scope; a reading C1 rests on (rule 5.i) |

Rule 5.iii (V1.6's formula with a Desc) is section 2's (R2V2.8); nothing of it here.

## 2. How each is implemented; the inventions it forced (S36)

| id | code | as written? | inventions (other choices) |
|---|---|---|---|
| R2V1.1 | `account` adds `question` := ρ_p ∈ {selected, constructed} (as V1.5); `rho_of(p)` = the question's own ρ if set, else the run's recorded value `S108R2_S1_RHO` | yes, with the values set per case | **S108r2-1-I1**: in the suite, every question the claims build carries one recorded value per run (they record none); in the scripts, per case. Others: unrecorded ⇒ declared (S108-1-I5); unrecorded ⇒ left out |
| R2V1.1, the bridge | CreateEx (D14.7) over FC84.new1's 1,024 Θ-values, its conjunct Acc((c, p_c, …)) := the Θ label ∧ p_c a question | nearest statable | **S108r2-1-I3**: p_c := the brief's question (FC84.new1 builds no (D, C, Q); only ρ is read). Other: p_c a question found in the episode |
| ρ from a history | D3.4's constructed :⟺ Con (D12.2) with the contract as the content (E8's arrangement): a trace preparing it in an episode; selected: Sel's conditions by hand (none given); declared: neither | nearest statable | **S108r2-1-I4**. Other: ρ by hand only. Used for the bridge's brief (FC84.new1's chain: declared) and e1.37's found question |
| R2V1.6 | `expl_base(ℰ)` := adn(ℰ) = translates C ∧ A ∧ Dep ∧ NonVacuous; Expl := expl_base ∧ ¬Dec(t) where the program forms Expl (FC23.new2 (f), FC30.new1 (c)) | yes | (A) and Dependence read t's translation of C, as `account` does (no new choice). The defeat sets as written (Account ∧ ¬Dec) |
| R2V1.6s | `defeat_base(ℰ)` := adn(ℰ) in (Suff)'s and (Nec)'s defeat sets (FC30.new1 (a), (b), (d), (e), (g), (h); FC23.new2 (f)) | the reply names no form | **S108r2-1-I2**: the defeat sets' antecedent co-varied to (A) ∧ Dep ∧ NonVacuous ∧ ¬Dec(t). Other: as written (R2V1.6) |
| R2V1.10 | ℰ_bv (round 1's case) with L_bv(a,b) := ∪_{b′∈B} proj_{V_cbv} Sol_D(a,b′) for a ≠ 1; L_bv(1,b) the reply's | yes | none new (S108-1-I1's family: (i), (ii), (iii)) |
| R2V1.10, generated | the ℰ_bv pattern on each generated target: component j's relation replaced by proj_{V_j} Sol_D(1,b) at 1 and by I1's reading at a ≠ 1; Γ = {j}, λ(j) = {j} | nearest statable | **S108r2-1-I5** (the pattern itself) |
| e1.14 | "an equation beside an incompatible one", read two ways (§7) | reading | **S108r2-1-I6**: loose reading := some component k ≠ j altered by the edit whose relation alone admits no tuple with v = x |

## 3. The readings the round-1 candidates rest on (rule 5.i)

### 3.1 C2 (V1.5) under each choice of S108-1-I5 (R2V1.1)

Run: `s108r2_s1_cases.py`, part A (`section 1 runs/cases/cases.txt`). Expl with t's history set by hand (I90): Con-history (a trace), Sel-history (H = {(1, b0)}).

| choice | worked cases with Acc T (of 27) | the owner's cases (two-part sign / one-part / E_enc on the sign's q / M13 / E_enc on M13's q) | the student's copy (S41 Q2) | the bridge (S41 Q6): Con, Build at the output | CreateEx on (a2) (a first design criticized), valuations of 1,024 |
|---|---|---|---|---|---|
| none | 22 | T / T / T / T / T | Acc T, Dec, Expl F | T, T | 1 |
| I5: unrecorded ⇒ declared (round 1) | 0 | F / F / F / F / F | Acc F, Dec, Expl F | T, T | 0 (brief unrecorded or declared); 1 (brief selected or constructed) |
| unrecorded ⇒ left out | nothing computed on any worked case (none records ρ) | not computed | not computed | T, T | 0 where ρ(brief) is computed from FC84.new1's chain (declared, S108r2-1-I4); else not computed |
| R2V1.1, recorded declared | 0 (the same 22 move) | F / F / F / F / F | Acc F, Dec, Expl F | T, T | 0 |
| R2V1.1, recorded selected | 22 (0 move) | T / T / T / T / T | Acc T, Dec, Expl F | T, T | 1, except 0 where the brief's own ρ is declared |
| R2V1.1, recorded constructed | 22 (0 move) | as selected | as selected | T, T | as selected |

- ρ(C_brief) by D3.4 on FC84.new1's own chain: no trace prepares the brief (the trace prepares t), no population of contracts: **declared** (Con with the brief as content F).
- (a1) (no criticism, the owner's case as S47 writes it): CreateEx 0 of 1,024 under every choice, none included ((EX) asks a critical episode, FC32.new1 (f)); (a4) (I191's labelling): as (a2).
- FC-E1–E5, CT1–CT8, the written-in step's cases (`section 1 runs/scripts/`): under R2V1.1 declared, byte-identical to round 1's V1.5 outputs (c47d5828…, ef236836…, 3a2b4de8…); under selected and constructed, byte-identical to none.

**C2 under each choice** (admits / drops / flags):

| choice | admits | drops | S44 | S41 Q15 | S41 Q6 | S41 Q2 |
|---|---|---|---|---|---|---|
| I5 (round 1) | none | every candidate on every question built: 22 worked, FC-E1, FC-E4, CT1, CT2, CT5, generated 961 / 886 / 221 / 1,674 | stands | stands | **comes**, on (EX)'s reading of "created": CreateEx 1 → 0 on (a2); Con and Build do not move | appears to agree (the copy stays no explanation) |
| left out | none | none computed | goes (not computed) | goes (not computed) | comes only where the brief's ρ is computed from its chain (declared) | – |
| recorded declared | as I5 | as I5 | stands | stands | comes (as I5) | as I5 |
| recorded selected / constructed | none | none (0 moves: worked, scripts, 61,914 generated) | goes | goes | goes (CreateEx 1 of 1,024, as off) | – |
| recorded per case | none | exactly the candidates on questions recorded declared | stands iff the sign's question is recorded declared | stands iff the vane's question is | stands iff the brief is | – |

- The reply's R2V1.1 trace (C2's flags "stand only where ρ_p is unrecorded or declared; go where recorded selected or constructed"): **computed**, for S44 and S41 Q15; and S41 Q6 now computed (round 1: "not computed").
- S47 ("The math doesn't ask for anything"): under C2 on a declared brief the created explanation needs the brief's history (selected or constructed); named as the reply names it, with S41 Q6.

### 3.2 C1 (V1.1) under each choice of S108-1-I1 (R2V1.10)

Run: part C. ℰ_bv = the pole with c_L replaced by c_bv on (H, T, L); Γ = {c_bv}, λ(c_bv) = {c_L}.

| I1 reading | ℰ_bv on C1: none / V1.1 | on C2: none / V1.1 | (F1) under V1.1 fails at | C1 admits ℰ_bv |
|---|---|---|---|---|
| (i) follows (round 1) | F / **T** | F / **T** | 0 of 7; 0 of 15 | yes |
| (ii) baseline (round 1) | F / F | F / F | 4 of 7; 11 of 15 | no |
| (iii) ∪_{b′} proj Sol_D(a, b′) (the reply's) | F / **F** | F / **F** | 6 of 7; 14 of 15 (at set(H=1): proj^λ Sol_{c_L} 1 tuple, L_bv 3) | **no** |

- The reply's "under V1.1 + (iii), proj^λ = L_bv at every pair as under (i) ⇒ ℰ_bv stays admitted": **contradicted**. The union over boundaries holds every T the boundaries give; the projection of the one solution at b1_45 holds one.
- C1's drops and flags do not read I1 (computed): under V1.1 the owner's two-part sign F, M13 F; the one-part sign T, E_enc on the sign's q T, E_enc on M13's q T, under every I1 reading. **S44 stands** under (i), (ii), (iii); S41 Q15 appears to agree under all three.
- The ℰ_bv pattern on generated targets (S108r2-1-I5; §5): under V1.1 it is admitted, by reading, follows / baseline / iii: SMALL 2,899 / 870 / 1,841 of 34,560 built (in, against none: 822 / 162 / 445; out: 0 / 113 / 64). So (iii) is admitted on generated targets whose boundary does not reach V_j, not on the pole.
- The reply's quotation "r and u fail (F1) under V1.1 at ('tue', b0), proj Sol_{λ(r)} = {blue} vs L_r = full" is in no file of round 1 (rule 14). Computed here: r fails at ('tue', b0) as quoted; u fails at (1, b0) (proj {red}, L_u full), not at ('tue', b0).

## 4. The worked cases, FC-E1–FC-E5, CT1–CT8 (rules 5.1–5.3)

| variant | worked cases (27): Acc moves | being an explanation moves | FC-E1–E5 | CT1–CT8 | the written-in step's cases |
|---|---|---|---|---|---|
| R2V1.1 declared | 22 T → F (all that met (E)) | the same 22 (Con-, Sel-history) | = round 1's V1.5 (FC-E1, FC-E4 (E) yes → no) | = V1.5 (CT1, CT2, CT5) | = V1.5 (every (E) T → F) |
| R2V1.1 selected, constructed | 0 | 0 | unchanged | unchanged | unchanged |
| R2V1.6 | 0 | **in 2**, Con-history only: E_rev under τ′ on C1 (F1 T, F2 F: Hom); the relabeling candidate with τ(1) ≠ 1 (F1 F, F2 F). Out 0 | Acc unchanged; being an explanation (captured candidates, 12): in 1, ℰ\|{k} on p_E1 (FC-E1; F1 T, F2 F), Con-history | Acc unchanged; captured 775: in 3, on p_nosender (F1 F, F2 F), Con-history | printouts unchanged (they print Acc) |
| R2V1.10 | ℰ_bv only (§3.2); every worked case as V1.1 | as V1.1 | as V1.1 | as V1.1 | as V1.1 |

R2V1.6 in detail (part B):

| item | computed |
|---|---|
| (Suff) as written, Account ∧ ¬Dec ⇒ Expl, worked × 3 histories | 0 failures |
| (Nec) as written, Expl ⇒ Account ∧ ¬Dec | 2 failures (the two entering cases, Con-history): the variant contradicts it by its own definition |
| Sel-history | neither entering case enters: Sel reads Faithful_H (D12.1 → D5.7); both fail Hom, a condition on τ as a whole (I18); the relabeling also fails (F1) at (1, b0) (computed) |
| defeat sets, R2V1.6 (as written) | the entering cases stay in (Nec)'s defeat set (L61's 'their'), out of (Suff)'s |
| defeat sets, R2V1.6s | with a Con-history and an argument not using (E) that rules out Expl(ℰ): the entering cases move into (Suff)'s defeat set and out of (Nec)'s; E_fwd (meets (E)) as before |
| the student's copy (S41 Q2) | Acc T, ADN T, Dec: Expl F under none and R2V1.6 |
| (A) ∧ NonVacuous without Dependence (prediction alone) | stays out under R2V1.6: worked 0, FC-E 0, CT 0 of the captured; generated 6,621 / 6,190 / 653 / 10,230 (SMALL, vm, proper, MID) |
| the reply's small cases | FC27's τ′ look (F1 T, F2 F, A, Dep, NonVacuous T) and FC21 (d)'s relabeling (A T, F2 F): both enter with a Con-history, **computed**; the reply's "nothing drops … the two-part sign, the vane, E_enc, 'p because p' all stay": computed |

## 5. The generated worlds at scale 4 (rule 5.4)

Run: `s108r2_s1_worlds.py`, round 1's seeds (108001–108004), 160 models per size; candidates built with D1.4 as after round 4; the base counts equal round 1's (Acc T under none: 961 / 886 / 221 / 1,674).

| state | SMALL: Acc moves; Expl moves (Con / Sel) | SMALL vm | proper | MID |
|---|---|---|---|---|
| I5 (round 1's V1.5, for comparison) | 961 out; 961 / 961 | 886; 886 / 886 | 221; 221 / 221 | 1,674; 1,674 / 1,674 |
| R2V1.1 declared | 961 out; 961 / 961 | 886; 886 / 886 | 221; 221 / 221 | 1,674; 1,674 / 1,674 |
| R2V1.1 selected | 0; 0 / 0 | 0 | 0 | 0 |
| R2V1.1 constructed | 0; 0 / 0 | 0 | 0 | 0 |
| R2V1.6 | 0; **in 201 / 141** | 0; 149 / 99 | 0; 59 / 35 | 0; 415 / 236 |

R2V1.6, SMALL, of each kind (candidate generator | target family | the conjuncts failing under none: count, smallest):

| kind | count | smallest |
|---|---|---|
| E_enc \| G-free \| F1 / F1,F2 / F2 | 14 / 12 / 5 | ports 1, dom 1, comps 2, \|B\| 2, edits 2 / ports 2, dom 2, comps 2, \|B\| 1, edits 1 / ports 2, dom 2, comps 1, \|B\| 1, edits 1 |
| E_enc \| G-surg \| F1 / F1,F2 / F2 | 22 / 11 / 12 | ports 1, dom 1, comps 3, \|B\| 2, edits 0 / ports 1, dom 2, comps 2, \|B\| 2, edits 0 / ports 1, dom 1, comps 1, \|B\| 2, edits 2 |
| lookup \| G-free \| F1,F2 / F2 | 40 / 9 | ports 1, dom 2, comps 1, \|B\| 2, edits 1 / ports 2, dom 2, comps 1, \|B\| 2, edits 1 |
| lookup \| G-surg \| F1,F2 / F2 | 44 / 12 | ports 1, dom 2, comps 2, \|B\| 1, edits 1 / ports 2, dom 2, comps 1, \|B\| 2, edits 1 |
| random \| G-free \| F1 / F1,F2 | 4 / 3 | ports 1, dom 1, comps 3, \|B\| 2, edits 2 / ports 1, dom 2, comps 1, \|B\| 1, edits 2 |
| random \| G-surg \| F1 / F1,F2 | 6 / 7 | ports 1, dom 1, comps 3, \|B\| 2, edits 0 / ports 1, dom 2, comps 2, \|B\| 2, edits 0 |

- Every R2V1.6 move is "in" (0 out); every one fails (F1) or (F2) under none and meets (A), Dependence, NonVacuous; with a Sel-history fewer enter (Sel reads Faithful_H).
- (A) ∧ NonVacuous without Dependence (agreement of answers alone): 6,621 / 6,190 / 653 / 10,230, out under R2V1.6 as under none; (A) ∧ Dependence ∧ NonVacuous with (F1) and (F2) both failing: 117 / 88 / 34 / 243 (in under R2V1.6 with a constructed t).
- R2V1.1 declared = I5 candidate for candidate (the same kinds and smallest witnesses as round 1's V1.5 table).
- R2V1.10: no generated candidate reads I1 (0 moves); the ℰ_bv pattern: §3.2 (SMALL), and vm, proper, MID in `worlds.*.txt`.
- Witnesses written out in full: `section 1 runs/worlds/worlds.*.json` (field `witness`).

## 6. The whole suite: a harness job (rule 5; "Who does what")

- **Spec** (the one to run): `tools/sonnet_harness/specs/s108r2 claim suites, section 1.json`: seven runs of `run_claims.py` on this copy (scale 4, cap 45), each compared with the round-4 record (`formal claims, after round 4.json`, key after_round4): off; R2V1.1 declared, selected, constructed; R2V1.6; R2V1.6s; R2V1.10. A variant is switched on only by the environment (`/usr/bin/env NAME=value … run_claims.py`); nothing in the program is edited. Check steps: `s108r2_s1_suite_check.py` lists the claims whose status or parts move against the record, compares them with `section 1 runs/suite - expected moves.json`, and lists the claims whose printed text moves against the off run.
- **Per-variant specs** (the rule's naming, the same commands, one variant each, for a re-run; no off run and no text comparison): `s108r2 suite, section 1, R2V1.1.json`, `…, R2V1.6.json`, `…, R2V1.10.json`. All four written by `section 1 runs/s108r2_s1_specs.py`, which takes every input's md5 (the copy's `model/*.py`, the check script, the expected moves, the record); `run_task.py --phase validate`: ok for all four.
- **The switch reaches the program through the harness** (checked, two claims only): `/usr/bin/env S108R2_S1_VARIANT=R2V1.1 S108R2_S1_RHO=declared … run_claims.py --claim FC26 --claim FC22`: both HOLDS → COUNTEREXAMPLE, as under round 1's V1.5; the program's folder unchanged, no `__pycache__`.
- **Expected** (what goes back to Opus if it differs):

| run | claims expected to move (status or parts) | why |
|---|---|---|
| off | 0 (133 / 2 / 7 of 142, every part as the record) | the program after round 4 |
| R2V1.1 declared | 19: FC22, FC23, FC23.new1, FC23.new2, FC23.new3, FC23.new5, FC25.new2, FC26, FC27.new1, FC30.new1, FC34, FC42.new1, FC62, FC63, FC72.new2, FC74, FC90.new1, FC99, FC101 | the conjunct and value of round 1's V1.5 (its suite moved these: 15 in status, 4 in parts only) |
| R2V1.1 selected, constructed | 0 | the conjunct holds everywhere; only printed conjunct lists gain 'question': True |
| R2V1.6, R2V1.6s | 0 | the suite forms Expl only on candidates meeting (E) |
| R2V1.10 | 25: round 1's V1.1 moves (21 in status, 4 in parts only) | I1 is read by no claim |

- **Single claims run here** (allowed; `section 1 runs/single/`): FC22, FC23.new2, FC23.new5, FC26, FC30.new1 under R2V1.1 selected and constructed, R2V1.6, R2V1.6s: every status and part as none; text moves only under R2V1.1 ('question': True). FC17, FC18 under V1.1: hold (e1.03).
- The suite's blind spot for R2V1.6: no claim forms Expl on a candidate failing (F1) or (F2), so the suite cannot see R2V1.6's moves (§4, §5 do).
- **Brief** (`run_task.py … --phase brief --run s108r2`): returned to the orchestrator as suite_brief_json.

## 7. Round 1's claimed-only edges of section 1's share (rule 5.ii)

Run: part D (`cases.txt`).

| edge | the reply's settlement | computed (the nearest the program computes) | standing |
|---|---|---|---|
| e1.02 (V1.1: D1.4 changes with L233.s1) | a reading: "imposing the constraints of λ(k)" on D, then projecting; contradicted | the two readings of the words: W1 (λ(k)'s constraints alone) = I14's Sol_N at 138,487 of 138,487 (k, pair) of the worked candidates; W2 (imposed within D, restricted to V_N) = V1.1's at 138,487 of 138,487; W1 = W2 at 14,004 | **not settled by computation**: each reading states one definition exactly; which the words carry is a reading. On the reply's reading (W2), L233.s1 needs no change (contradicted there) |
| e1.03 (V1.1: D1.4 changes with L556.n2) | contradicted | under V1.1, L556.n2's statement ((F1) at (a,b) ⟺ D4.4's sig_C(λ(k)) and (K)'s sig_τ[C](k) agree) at 7,042 of 7,042 translated pairs; FC17, FC18 hold (single runs). D4.4's gloss 'extends (K)' fails (sig_C({j}) = sig_C(j) at 14,064 of 166,251 (j, pair); round 1's e1.00), but L556.n2 uses D4.4's formula and (K)'s component clause | **contradicted** |
| e1.14 (V1.2: D2.1 blocks L103.s2) | a reading: nothing is added; contradicted | round 1's SMALL targets (seed 108001, 160 per size) and the pole: 6,354 new setting pairs (pole 400). Reply's reading (the assigning component's old relation left beside the slice): 0 of 6,354. Loose reading (S108r2-1-I6): 2,709 of 5,954 generated (0 of 400 on the pole) have an altered k ≠ j whose relation alone excludes the set value; Sol_D empty at some b: 4,129, of which 1,420 with no single such k | **not settled by computation**: contradicted on the reply's reading; stands on the loose one (2,709 cases) |
| e1.36 (V1.5 blocks L155.s2, L155.s5) | stands by derivation | value side: under V1.5 (I5, R2V1.1 declared) every assessment of (E) on a declared contract admits nothing (22 worked, all generated) | **not settled by computation**: V1.5 removes the value L155.s2 defines (wording); whether "may use" in L155.s5 is negated is a reading; would settle: the owner's yes or no on C2 |
| e1.37 (V1.5 constrains L155.s6, D3.1) | R2V1.2's encoding | a chain o1 ≺ o2, C1 → C2 (E8's arrangement, S108r2-1-I4): a trace preparing C2, change recorded: Con(C2) T (S41 and L55) ⇒ ρ = constructed; unrecorded: T under S41, F under L55 ⇒ constructed; no trace: declared. D3.1's slot holds the computed value; L155.s6's Found claim allowed exactly where constructed; E_fwd on the found question: Acc T under none, V1.5, R2V1.1; on the declared one: T, F, F | **computed** (stands) |
| e1.38 (V1.5 changes with D13.8 q(o)/Rec) | R2V1.3 (Episode reading ρ; S3's change) | D13.8 as written: Episode, Con and Build at the bridge's output identical under every state and every ρ(brief) (a1, a2, a4; S41 and L55). What moves is D14.7's CreateEx, through Acc(c, p_c, …): 1 → 0 of 1,024 on (a2) where the brief is declared | **contradicted** for D13.8; the move is in D14.7 (added edge, §8); a D13.8 reading ρ (R2V1.3) is flagged, not computed |
| e1.39 (V1.5 changes with D16.4 𝔓^adv) | R2V1.1: a finite 𝔈_Θ over the case scripts | 𝔈_Θ over the 27 worked (p, t, Γ, δ), Θ admitting every carrier (by hand): 13 organizations under none, recorded selected, recorded constructed; 0 under I5 and recorded declared | **computed** for 𝔈_Θ (D16.4); 𝔓^adv itself is undefined (NF12): not settled for it |
| e1.40 (V1.5 changes with (QF) L544) | not settled | – ('fails to capture', 'not creative' undefined, D16.XV's list) | **not settled by computation**; would settle: definitions of the two terms (S4) |

## 8. The edges (rule 5): the reply's, marked; and those the computation adds

Marks are the template's. Every row is in the `.json` beside this file.

### R2V1.1

| kind | item [mark] | the reply's why (cut) | standing | evidence |
|---|---|---|---|---|
| constrains | D3.1 [FROZEN], D3.4 [S1] | ρ_p's slot is D3.1's own | computed | the slot holds a recorded or computed value; D3.4 computes it from a chain (e1.37: constructed; the bridge's brief: declared) |
| moves | (E) as C2 has it; flags S44, S41 Q15 | conditional on the recording | computed | recorded declared: 22 worked, all generated out (= I5); selected or constructed: 0 moves (27 worked, scripts, 61,914 generated); S44, S41 Q15 stand under declared, go under selected or constructed |
| changes with | D16.4 𝔈_Θ [S4] | a finite 𝔈_Θ separates the two sides | computed | 13 organizations vs 0 (e1.39) |
| changes with | D14.7 CreateEx [S3], through Acc(c, p_c, …) | – | **added** | the bridge (a2): 1 → 0 of 1,024 valuations where ρ(brief) is declared (as its chain computes it); C2's S41 Q6 flag comes on that reading |
| independent of | D13.8 Episode, D12.2 Con, D13.3 Build [S3; D12.2 S2] on the bridge | – | **added** | identical under every state and ρ(brief) (e1.38) |

### R2V1.6

| kind | item [mark] | the reply's why (cut) | standing | evidence |
|---|---|---|---|---|
| blocks | L23.s1 [S1] | prediction plus a carried contrast becomes explanation | not settled by computation | computed: candidates whose components match no counterpart (F1 and F2 fail) and whose answers agree become explanations with a constructed t (the relabeling candidate; CT's three; generated 117 / 88 / 34 / 243 with (F1) and (F2) both failing, of them 84 lookups on SMALL); (A) ∧ NonVacuous without Dependence stays out (generated 6,621 / 6,190 / 653 / 10,230). Whether (A) ∧ Dependence ∧ NonVacuous ∧ ¬Dec(t) is "prediction" is a reading |
| moves | Expl | E_rev under τ′ and the relabeling candidate in; nothing out | computed | worked 2 in, 0 out (Con-history only); FC-E 1; CT 3; generated 201 / 149 / 59 / 415 (Con), 141 / 99 / 35 / 236 (Sel); Acc 0 moves |
| changes with | L49.n3 [S1] | the pointer sentences write Account ∧ ¬Dec | **contradicted** | L49.n3 states sufficiency ("explains … when"); Account ∧ ¬Dec ⇒ Expl holds under R2V1.6 (0 failures) |
| changes with | L69.n3 [S1] | as above | computed | L69.n3's "means" (Account ∧ ¬Dec) and R2V1.6's Expl differ on the 2 worked entering cases |
| changes with | D16.XV [S4], X:(Nec) | the defeat sets re-quantify | computed | (Nec) as written fails on the 2 entering cases (Expl without Account); under R2V1.6s they leave (Nec)'s defeat set |
| changes with | X:(Suff) | as above | contradicted as written; computed under R2V1.6s | (Suff) as written: 0 failures; its defeat set moves only when its antecedent is co-varied (R2V1.6s: the entering cases join it) |
| blocks | L69.s2 [S1] ("What cannot count as explanation is an error in the very dependence alleged to do the work") | – | **added**, computed on the reading that such an error is (F1) or (F2) failing on C | the relabeling candidate (F1, F2 fail) and E_rev under τ′ (F2 fails) count as explanations with a constructed t |
| constrains | X:(F1), X:(F2) through ¬Dec(t), D12.1 [S2] (Sel reads Faithful_H) | – | **added** | with a selected t they still bind on H: neither worked entering case enters under a Sel-history; generated 141 of 201 |
| independent of | X:(E) (Acc), FC-E and CT printouts, the suite's claims | – | **added** | 0 Acc moves anywhere; single claims unchanged; suite expected unchanged (§6) |

### R2V1.10

| kind | item [mark] | the reply's why (cut) | standing | evidence |
|---|---|---|---|---|
| constrains | S108-1-I1's family | (iii) a third choice | computed | (iii) built and run (§3.2) |
| moves (the reply's trace) | ℰ_bv admitted under V1.1 + (iii), "as under (i)" | – | **contradicted** | (F1) fails at 6 of 7 (C1), 14 of 15 (C2): Acc F |
| independent of | C1's flag S44 | the flag rests on the two-part sign | computed | the two-part sign F under V1.1 under every I1 reading (it reads no I1) |
| changes with | what C1 admits of the ℰ_bv pattern (generated) | – | **added** | under V1.1: follows 2,899, baseline 870, iii 1,841 of 34,560 (SMALL) |

### Edge counts

In the `.json`: 43 rows. Round 1's claimed-only edges 8 (§7): computed 2, contradicted 2, not settled by computation 4. The in-scope variants 18: computed 8, contradicted 3, not settled 1, added 6. The flagged variants' own edges 17: not settled by computation (rule 4). All: computed 10, contradicted 5, not settled 22, added 6.

## 9. What the computation says (for the map; nothing ruled)

| variant | which candidates meet (E) | being an explanation | round-1 candidates it bears on | decisions the computed effect sits against (named, not ruled; rule 13) |
|---|---|---|---|---|
| R2V1.1 | moves exactly where a question is recorded declared (then as I5); nothing where selected or constructed | as (E); and CreateEx on a declared brief | **C2**: its whole effect is the recording; flags S44, S41 Q15 stand iff the case's question is declared (or unrecorded under I5); S41 Q6 comes on (EX)'s reading where the brief is declared | S44, S41 Q15, S41 Q6 (and S47 as the reply names it), only "on that reading" of the question's history (the owner's to settle) |
| R2V1.6 | unchanged | **moves in** (never out): candidates meeting (A), Dependence, NonVacuous but not (F1) or (F2), with a constructed t (with a selected t fewer) | a new candidate definition (the reply's "C-new"): (A) ∧ Dependence ∧ NonVacuous ∧ ¬Dec(t) | none by the reply; computed: it counts as explanations candidates whose parts match nothing of the target (L23.s1, L69.s2 are the text's, not the owner's); S41 Q2 appears to agree (the student's copy stays out) |
| R2V1.10 | ℰ_bv only: (iii) not admitted on the pole | as (E) | **C1**: admits ℰ_bv under (i) only; drops and S44 flag the same under all three | S44 (C1's flag stands under every I1 reading) |

## 10. Items of the share still untouched

- D4.6 (the one middle definition of S1 no variant of either round has varied); L13.s1–s7, L151, L141.s1, L159.s4–s7, L155.s1–s5 as varied items: no in-scope variant (the flagged R2V1.2, R2V1.4, R2V1.8, R2V1.9 touch L155, L151, L159 and await the orchestrator).
- The flagged variants' own computations (R2V1.2–R2V1.5, R2V1.7–R2V1.9): not made (rule 4).

## 11. Unsure

- C2's flags turn on each question's history, which no case records; the bridge's brief is declared only on the reading that FC84.new1's chain is its whole history (S108r2-1-I4). Which the owner meant is the owner's (rule 13).
- S41 Q6's "created" is read two ways: Con and Build (no move) or CreateEx (moves); the owner's case (a1), with no criticism, has CreateEx F under every choice, none included; the move is on (a2), a criticized first design.
- p_c = the brief (S108r2-1-I3) decides the bridge's CreateEx; with p_c a question found in the episode (constructed), nothing moves.
- R2V1.6's entering candidates enter only with t constructed (Con-history) in the worked cases; histories are set by hand (I90).
- R2V1.6s's co-variation is my choice (S108r2-1-I2); the reply gives no form.
- The whole suite is not run here (the harness's job); its expectations rest on round 1's suite runs and on single claims.
- Silence is not agreement (rule 3): items untouched here are not shown free of dependencies.

Computed by one Opus 5.5 agent under rule 5 of round 2, 28 September 2026. Nothing here changes the theory's text, formal core, claims or program after round 4, or round 1's files and copies (rule 11).
