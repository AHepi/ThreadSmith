# S108 Part A - section 2 - variants computed

*Computing agent for section 2 (rule 5 of `results/S108 Part A - how the replies will be read, written before sending.md`), Opus 5.5, fresh, 28 September 2026. An experiment on a copy (rule 11): nothing in the theory's text, formal core, claims or the program after round 4 is changed. "Candidate" or "explanation" for what the theory judges, never "model" (S43); "model" means only the program's folder or a small structure it builds.*

Status: complete, 28 September 2026. Nothing ruled; nothing applied to the theory.

## Findings in brief

| variant | (E) (Acc) | Account ∧ ¬Dec(t) | worked cases / FC-E / CT | suite: claims whose result moves | what the computation adds or corrects |
|---|---|---|---|---|---|
| V2.1 D6.4 without Lost | F→T on 57 / 74 / 8 generated; none T→F | the same movers (Con, Sel histories) | none / none (a printed witness block) / none | none (six print witness block []) | admits candidates whose contrast no block of Γ carries (background or ⊥); 8 of 57 keep a commitment doing work for (F1)/(F2); ∅ becomes a route (63); routes with no critical block appear (120; off 0) |
| V2.2 singleton block | T→F on 23 / 20 / 4; none F→T | the same | none / none / none; the built L307 candidate T→F | **none** | under V2.2 every route has a critical singleton: L307's S realized by no candidate (17 → 0); L311's candidate has S = ∅ (argument); L299.s1 still realized (1), its Γ meeting (E) |
| V2.3 witness edit ≠ 1 | T→F on 253 / 213 / 65 | the same | E_rev, E_fwd on C_id T→F / none / none | FC25.new2, FC23 (b) | every account on a {1}×B contract goes (168 → 0), and 85 more whose contrasts sit only at boundary pairs; identification itself (L329.s3, FC57, FC58, Ident on C_id) untouched |
| V2.4 NC1 back in (E) | T→F on 972 / 776 / 301 (of 1,027 / 847 / 310) | the same | 11 T→F (the 10 of S106 and ℰ_myth1) / none / none | FC23.new1, FC23.new2, FC23.new5, FC25.new2, FC27.new1, FC72.new2; FC23, FC107 | the largest move; FC107: K1's criticism candidate loses (E), so Bearing; **(E) depends on D6.3's quantifier again** (FC23.new1 (h)), against the reply's "quantifier-independent" |
| V2.5 H = ∅ in Sel | unchanged | F→T for **every** account on a holding with nothing tried and no earlier representation (28 of 28 worked; 1,027 / 847 / 310) | none in the three scripts | FC77, FC30.new1 | Acc ⇒ (F2) ⇒ Hom(τ) ⇒ Sel(t;{t},id,∅): ¬Dec adds only Θ's admission there; the student's copy of a worked-out formula (FC30.new1 (d)) stays Dec under U, T, T′ |
| V2.6 Conf only in C | unchanged | unchanged | none / none / none; tilt–myth (Greeks' C) not rivals | FC72.new2 | 310 of 310 kind-ii pairs lose rivalry; 492 kind-i pairs lose outside-C conflicts |
| V2.7 ConfCl by answer only | unchanged | unchanged | none / none / none | FC52 | 410 of 1,822 ConfCl lost (23 on accounts); where the answer itself is the excluded motion (FC53 (b)) the conflict stays |
| V2.8 | not implemented (out of scope as written, tabulation §6) | | | | its reading is in the program already (FC30.new1 (h)); section 4's V4.4 |

Discovered changes to which candidates meet (E): V2.1, V2.2, V2.3, V2.4. To which count as explanations with (E) unchanged: V2.5. Neither: V2.6, V2.7. Edges: named 23 (computed 14, contradicted 3, not settled 6), added 17 (§8). Gaps for the map: no worked case and no claim of the suite separates D6.4 from V2.1 or V2.2 (only generated worlds and the built Part VI cases do); the (Nec) attack through easy to vary and any argument from ConfCl are not computed by the program.

## 0. Set-up

| item | state |
|---|---|
| reply read whole | `results/S108 Part A - returns/s108_glm_section2.response.txt` (md5 1d602e0f…, as the tabulation gives) |
| copy | `results/S108 Part A - computation/section 2 model/` from `results/S107 Round 4 - maths after the reading/model after round 4/` (26 files, each md5-checked identical at the copy) |
| in scope (tabulation §6) | V2.1 to V2.7 |
| not implemented | V2.8: flagged out of scope as written (tabulation §6: names FROZEN L315.s7; its trace is D16.XV's "not using (E)" at the instance, S4's V4.4). The program already carries that reading (`claims_s41.USES_READING = "instance"`; FC30.new1 (h) prints it) |
| switch | `core.S2_VARIANT`, from `S108_S2_VARIANT` (default `off` = every definition after round 4); `off` reproduces the three committed case printouts byte for byte (§2–§4) and the whole suite claim by claim (§6) |
| runs | PYTHONHASHSEED=0, `python3 -B`, every run under `timeout`; suite at scale 4, time cap 45 s, as the printouts |

## 1. The variants as implemented

| id | item | as implemented (file: place) | as written? |
|---|---|---|---|
| V2.1 | D6.4 | `core.NC2`: return at the first pair of C with Contrast(E;x); no block, no Lost | yes |
| V2.2 | D6.4 | `core.NC2`: blocks = the singletons {d}, d ∈ Γ | yes |
| V2.3 | D6.4 | `core.NC2`: pairs (a,b) of C with a = 1 skipped | yes |
| V2.4 | D6.7 | `core.account`: under the reading "S106" (the current (E)) the conjuncts are F1, F2, A, Dep, NC1, NonVacuous; NC1 under D6.3 as it stands (quantifier 'every', I136) | yes; = round 3's (E) (the program's reading "r3") |
| V2.5 | D12.1 | `claims_b.sel`: the test 'H ≠ ∅' skipped whatever reading the caller asks; the two hand-written 'H nonempty' tests (`claims_s41.py` FC30.new1 (d); `s104_creative_transport.py` CT8) skipped too | yes |
| V2.6 | D8.2 | `core.conflict`: no conflict at a pair outside the question's C | yes |
| V2.7 | D8.5 | `core.conf_claim`: the second disjunct reads False (with `parts=True` it is returned as False) | yes; program's choice: a caller asking for the two disjuncts gets the deleted one as False |

Where the program computes the current definition under a name (`account(reading="S106")`, `sel(h_nonempty=True)`), the variant replaces it; readings kept only for comparison (`"r3"`, `h_nonempty=False`, `round2`) are left as they were, except that V2.1–V2.3 vary D6.4 wherever NC2 is computed (round 3's (E) reads NC2 too). Program choices of this agent, not the theory's (S36): **P-S2-1** that mapping; **P-S2-2** V2.7's deleted disjunct reads False; **P-S2-3** the four histories of §2, Θ by hand (I90) as `claims_s41.provenance_of` has them, plus FC77's history with nothing tried.

md5 of the copy's changed files (originals after round 4 in brackets): `model/core.py` 82fe831b… (6922c3bf…); `model/claims_b.py` 65964915… (931262d3…); `model/claims_s41.py` c7eee707… (fcacbcae…); `s104_creative_transport.py` 1a85277f… (dd49e2b0…). New: `s108_s2_cases.py`, `s108_s2_gen.py`, `s108_s2_routes.py`, `s108_s2_suite.py`; the edges builder and its input are in `results/S108 Part A - computation/section 2 runs/` (`s108_s2_edges.py`, `suite edges.json`).

## 2. The worked cases (rule 5.1)

Runs: `s106_cases.py` (the case script of the written-in step) under off and each variant, diffed; `s108_s2_cases.py` (the same 27 candidates, collected, plus 8: E_fwd on C_id, the student's declared formula, the tilt and both myths on the Greeks' and the finer contract), Acc and conjuncts per variant; E6 (the Leibniz candidate) through `claims_b.e6_parts`. Outputs in `results/S108 Part A - computation/section 2 runs/`. `off` = the printout, byte for byte (checked by diff).

**Acc (E), off → on; only the cases that move** (35 cases; T = meets (E)):

| variant | cases whose Acc moves | conjunct that moves |
|---|---|---|
| V2.1 | none | — (every case with a contrast already has a block losing it; FC-E1's witness block becomes [] with (E) unchanged) |
| V2.2 | none | — (every worked case that meets (E) has a single commitment whose deletion loses its contrast) |
| V2.3 | E_rev on C_id T→F; E_fwd on C_id T→F | Dep (witness off: ((1,b2_45), {r_L}) and ((1,b2_45), {c_H}): a boundary-only contrast) |
| V2.4 | 11, all T→F: E_enc C1, E_enc C2, L273 'p because p', M1, M2, M3, ℰ_one (sign, one part), ℰ_myth1 (Greeks' C), R3-Q1 hand-turned vane, E8 p_δ identity candidate, E_rev under τ′ (H only) | NC1 (a slot); = round 3's (E) under 'every', the 10 MOVED of the S106 printout plus ℰ_myth1 |
| V2.5 | none | — (Acc reads no provenance, FC30) |
| V2.6 | none | — |
| V2.7 | none | — |

Unchanged under every variant: E_fwd C1, C2, C3; E_rev C1 (F); E_rev τ′ C1 (F); E_tab C1, C2 (F); L257 relabelings (F); M5; M13 weathervane; E5 both encodings; E9 t1 and t1∘ψ; ℰ_two (sign, two parts); the sign with a day port; the student's formula; the tilt (both contracts); ℰ_myth2 (Greeks'); both myths on the finer C (F). E6: (c-i) "not as claimed", (c-ii) "as claimed" under off and all seven.

**Account ∧ ¬Dec(t)**, histories set by hand (Θ, I90; P-S2-3): *Con* (a trace prepares t, cod t held); *Sel* (selection history on H = {(1,b0)}, admitted); *nothing tried* (H = ∅, no trace, admitted; FC77, FC30.new1 (e)); *Dec* (Θ admits no selection).

| variant | (case, history) whose Account ∧ ¬Dec(t) moves |
|---|---|
| V2.1, V2.2, V2.6, V2.7 | none |
| V2.3 | 4: E_rev and E_fwd on C_id, histories Con and Sel, T→F |
| V2.4 | 22: the 11 cases above, histories Con and Sel, T→F |
| V2.5 | 28: every case that meets (E) (28 of 35), history *nothing tried*, F→T; no other history moves |

Why V2.5 moves exactly the accounts: Acc ⇒ (F2) ⇒ Hom(τ) (D5.5, I18), and with H = ∅ allowed Sel(t;{t},id,∅) ⟺ Hom(τ) where Θ admits t (FC77 part 3, "the other choice"); so every account on such a history is Sel, not Dec.

**The owner's declared link (S41 Q2)**, the program's two encodings: (e) a link written from nothing, no earlier holding, nothing tried (FC30.new1 (e)): off Sel F, Con F, Dec T, Acc T, Account ∧ ¬Dec(t) F; V2.5 Sel T (also when the caller asks 'H ≠ ∅' explicitly), Dec F, Account ∧ ¬Dec(t) **T**. (d) the student's copy of a formula its author worked out (FC30.new1 (d), provenance computed on the chain source ≺ copy): under V2.5 still **Dec** under the cuts U, T and T′ (the source's earlier representation excludes Sel at the copy, D12.1), with H = ∅ as with H = {(1,b1_45)}; only under K (the reading rejected in round 2) is the copy Sel (as it is off with H nonempty). So V2.5 reaches a declared link whose history holds no earlier representation of t or cod t, not a copy of a worked-out one (§6). **The bridge (S41 Q6; FC84.new1)** computes provenance only (no candidate's (E)); its Sel's conditions are all 0, so no variant reaches it (suite, §6).

## 3. The external examples FC-E1 to FC-E5 (rule 5.2)

`s104_external.py` under off and each variant, diffed. `off` = the printout.

| variant | what moves |
|---|---|
| V2.1 | FC-E1's printed NC2 witness block: ['k'] → [] (the variant has no block); every (E), route, CriticalBlock, Indisp, NoWork line unchanged; "reproduced: yes" ×5 |
| V2.2–V2.7 | nothing (output identical to off) |

## 4. The creative transport case CT1 to CT8 (rule 5.3)

`s104_creative_transport.py` under off and each variant: output identical to off under all seven (CT1–CT7's (E) values; CT8's Sel/Con/Dec under R1–R5 and T′: its H is the eight settings, nonempty, so V2.5 does not reach it).

## 5. The generated worlds at scale 4 (rule 5.4)

`s108_s2_gen.py --scale 4` (≈80 s): the program's own generators, sizes ascending, seeded; every candidate's Acc computed under off and all seven, and Account ∧ ¬Dec(t) under the four histories of §2. `s108_s2_routes.py` (same seed, same candidates): S, (B), NoWork. Kinds: the target's generator family (G-surg, G-free) × the candidate's (E_enc = `gen_candidate`, random, lookup = `gen_lookup`, the written-in one).

**Populations**

| name | generator | sizes | drawn | meet (E) off |
|---|---|---|---|---|
| single | `gen_p_cand` (FC30.new1 (b)'s) | SMALL, 108 sizes, 160 each | 17,280 | 1,027 |
| single, value maps | `gen_p_cand(valuemaps=True)` | SMALL, 160 each | 17,280 | 847 |
| single, MID, proper targets | `gen_p_cand_proper` | MID, 162 sizes, 80 each | 1,914 | 310 |
| pairs | `gen_pair` (FC43's) | CONF, 48 sizes, 80 each | 3,835 pairs | kinds off: i 1,892, ii 310, none 1,633 |
| claims | FC52's generator (candidate, random χ) | CONF, 40 each | 1,914 (4,307 translated pairs) | ConfCl holds at 1,822 pairs |

**Acc: candidates whose result differs, off → on** (single / value maps / MID proper)

| variant | differ | direction | by kind (single) | conjunct |
|---|---|---|---|---|
| V2.1 | 57 / 74 / 8 | all F→T | G-free E_enc 36, G-surg E_enc 21 | Dep F→T |
| V2.2 | 23 / 20 / 4 | all T→F | G-free E_enc 12, G-surg E_enc 10, G-free random 1 | Dep T→F |
| V2.3 | 253 / 213 / 65 | all T→F | E_enc 227, lookup 24, random 2 | Dep T→F |
| V2.4 | 972 / 776 / 301 | all T→F | E_enc 864, lookup 102, random 6 | NC1 (slot); 55 / 71 / 9 accounts left |
| V2.5, V2.6, V2.7 | 0 | — | — | — |

**Account ∧ ¬Dec(t): (candidate, history) that differ.** V2.1–V2.4: exactly the Acc movers, on the histories Con and Sel (2 each), none on *nothing tried* or *Dec* (Dec there off and on). V2.5: 1,027 / 847 / 310, all F→T, all on *nothing tried*: **every** candidate meeting (E), none other. V2.6, V2.7: 0.

**Smallest witnesses** (first found; sizes ascend). Degenerate ones (a one-value port, an empty relation giving ⊥) come first in SMALL; the MID proper population gives targets with every domain ≥ 2 and Sol_D(1,b) ≠ ∅ (I101).

| variant | smallest (SMALL) | smallest on a proper target (MID) |
|---|---|---|
| V2.1 F→T | p0 ∈ {0}; C = {(1,b0),(1,b1)}; Γ = {k0}, background k1; both empty at b1 → answer 0 vs ⊥; deleting k0 leaves k1 empty: contrast not lost | p0 ∈ {0,1}; C = {(1,b0), (both alts,b0)}; Γ = {k1}; the contrast (0 vs ⊥) carried by background k0; deleting k1 loses nothing |
| V2.2 T→F | p0 ∈ {0}; Γ = {k0,k1}, two copies (L307's redundancy) | p0 ∈ {0,1}; C = {1}×{b0,b1}; Γ = {k0,k1}, both p0 = 0 at b0, full at b1 (baseline b1: ⊥): only the pair deletes the contrast |
| V2.3 T→F | p0 ∈ {0}; C = {(1,b0),(1,b1)}; one component, 0 at b0, empty at b1 | p0 ∈ {0,1}; C = {1}×{b0,b1}; one component, p0 = 1 at b0, 0 at b1: a boundary-only contrast |
| V2.4 T→F | p0 ∈ {0}; C = {(1,b0),(e1,b0)}; one component, {(0)} at 1, empty at e1 (0 vs ⊥): a slot at the one determined pair | p0 ∈ {0,1}; C = {(1,b0),(alt,b0)}; the identity copy of a one-component target, {(1)} at 1, empty at alt: the same slot |
| V2.5 (Account ∧ ¬Dec) F→T | the first account drawn (ports 1, dom 1, comps 1, B 1, edits 1), nothing tried | the V2.4 candidate beside it, nothing tried: Hom(τ) T, so Sel(t;{t},id,∅) |

Full descriptions: `results/S108 Part A - computation/section 2 runs/generated worlds - s108_s2_gen.py witnesses.json`.

**Routes and blocks** (`s108_s2_routes.py`, population single):

| measure | off | V2.1 | V2.2 | V2.3 | V2.4 |
|---|---|---|---|---|---|
| routes W ∈ S (all candidates) | 1,322 | 1,450 | 1,297 | 980 | 60 |
| routes with no critical block | **0** | 120 | 0 | 0 | 0 |
| routes with no critical singleton | 21 | 141 | **0** | 13 | 0 |
| candidates with ∅ ∈ S | 0 | 63 | 0 | 0 | 0 |
| candidates realizing L307's S = {{a},{b},{a,b}} | 17 | 17 | **0** (all 17 → {{a},{b}}) | 9 | 0 |
| candidates realizing L299.s1 (a block critical in a route, no singleton of it critical) | 20 | 20 | 1 | 12 | 0 |
| candidates on a contract {1}×B′ (1,953): meeting (E) | 168 | 177 | 161 | **0** | 7 |
| V2.1's 57 new accounts: every commitment NoWork (D7.6) under V2.1's S | — | 49 of 57 | — | — | — |

Two facts the counts show, each also a two-line argument:
- **Off: every route has a critical block.** W ∈ S has Dependence witnessed by a block G with Lost(E|W, G; x); Lost changes an answer of E|W at x or x0 = (1,σ(b0)), both images of pairs of C, where E|W meets (A); E|W − G = E|(W∖G) (D7.1) then fails (A), so W∖G ∉ S: G is critical in W. (0 of 1,322.)
- **V2.2: every route has a critical singleton**, by the same step with G = {d}. So S = {{a},{b},{a,b}} (L307.s1) is realized by no candidate (in {a,b} neither singleton is critical), and an infinitary Γ in which no singleton is critical in any route (L311) has S = ∅. (0 of 1,297; L307: 17 → 0.)
- **V2.1**: the witness block is gone, and routes with no critical block appear (120, of which 63 are ∅); 8 of the 57 new accounts keep a commitment that does work for (F1)/(F2) while none carries the contrast (smallest: Γ = {k0} on p0, the answer on p1 set by background k1).

**Pairs (V2.6)**: 802 of 3,835 pairs differ: 310 kind ii → no conflict, not rivals, no problem (all 310); 492 kind i keep kind i and lose their conflict pairs outside C. V2.1–V2.4 move no pair's conflict pairs, rivals or kind (0 of 3,835 each: Conf reads no Dependence and no slot).

**Claims (V2.7)**: 410 of the 1,822 (candidate, pair) with ConfCl lose it; in all 410 the first disjunct fails and the second holds; 23 of them are candidates that meet (E) (20 at a pair of C, 3 outside); by kind E_enc 263, random 110, lookup 37.

## 6. The whole suite with each variant on

`s108_s2_suite.py`: `python3 -B -m model.run --scale 4 --time-cap 45 --no-write`, one run per variant (≈500–620 s each), compared claim by claim and part by part with the off run (status, and the written result, counterexample, witness or reason; the lines that depend on the time a search had are left out). **The off run equals the committed printout in every claim's status and every part's status and written result (0 differences), 133 / 2 / 7 of 142.** Counterexamples off: FC23, FC63.

| variant | holds / counterexample / not tested | claims whose result moves |
|---|---|---|
| V2.1 | 133 / 2 / 7 | **none**. Six claims print a different NC2 witness (block [] in place of a commitment: FC21 (b), (d); FC22 (b); FC23.new2 (a); FC26's look; FC62; FC63 (c-i), (c-ii)); every status and every value the same. FC29 (L275.n1's unrealizable contrast) unchanged |
| V2.2 | 133 / 2 / 7 | **none**; every written result identical. No claim of the suite builds a candidate whose Dependence needs a block of two or more (FC37–FC40 test set systems, not candidates) |
| V2.3 | 132 / 3 / 7 | FC25.new2 (a) "E_enc meets (E) where its answer varies": counterexample (an E_enc whose answer varies only across boundaries); FC23 (b) "with satisfiable background: Ans_p not constant on C ⇒ NC2(E_lk)": counterexample (a lookup, C = {1}×{b0,b1}, 1 at b0, 0 at b1); witnesses differ in FC21 (d), FC23.new1 (b), FC34, FC74. FC28 (E_rev on C_id meets (F1), (F2), (A); Ident holds on C_id), FC57, FC58, FC28.new2 unchanged |
| V2.4 | 127 / 8 / 7 | holds → counterexample: **FC23.new1** ((h) "the quantifier does not change (E)": counterexample, one component, ⊥ at 1 and 1 at e1: (E) (F,F,T,T) under (every, some, some-exempt, some-exempt-set); (h)'s computation not as claimed), **FC23.new2** ((a), (b), (f): the one-part sign fails (E), so it is in no defeat set of (Suff) under any provenance), **FC23.new5** (b), **FC25.new2** ((a), (c): E_enc on C1, C2 fails (E)), **FC27.new1** (d) (E_rev under τ′ on C_H fails (E)), **FC72.new2** ((a) ℰ_myth1 fails (E); (c) j1's taken-as-given ground now coincides with (E); j0's problem stands). FC23 (c) not as claimed; (e) "a lookup E_lk meets (E)": no witness found. **FC107** "(E) assesses a candidate for p_δ": Acc T → F for the identity candidate (NC1 F: 'base' a slot), so a criticism whose connection is that candidate loses Bearing (D9.10). FC34, FC74: witnesses differ |
| V2.5 | 131 / 4 / 7 | **FC77** part 1 "no transport has Sel(t;{t},id,∅)": counterexample; **FC30.new1** (e) not as claimed (both of its rows Sel T, Dec F, in Def(L17, S41) T); (d) same status, its K rows move (with H = ∅, K: fixed point {o2: Sel}, Dec F); under U, T, T′ the copy stays Dec |
| V2.6 | 132 / 3 / 7 | **FC72.new2** (b) not as claimed (Greeks' C: conflict pairs none, not rivals, no kind), (c) not as claimed (no problem for j0). FC43–FC47, FC54 unchanged |
| V2.7 | 132 / 3 / 7 | **FC52** (2) "first disjunct ∧ ∃R Meets_ab(ℰ,R) ⇒ second": counterexample (the second disjunct reads False, P-S2-2); (3)'s witness differs. **FC53 (b)** (the pendulum with friction deleted: ConfCl by its answer) unchanged; FC54 (ConfG_χ excludes Conf) unchanged |

## 7. The reply's small cases, built and run

| case (reply) | reply's claim | computed |
|---|---|---|
| V2.1: D x,y,z; cx, cy, dz; A = {1,e}; Γ = {dz}; δ_E = y | before: F1, F2, A, NonVacuous ✓; Ans(1,b0) = ⊥, Ans(e,b0) = 1; ¬Lost → ¬NC2 → ¬Acc; after: Acc | as claimed: off conjuncts F1T F2T AT DepF NonVacuousT, (E) F; V2.1 Dep T, (E) T, witness ((e,b0), []). Account ∧ ¬Dec(t) under V2.1: T with a Con or Sel history, F with nothing tried or Dec (the reply's "declared": its trace assumes the Dec history) |
| V2.2: L311's infinitary Γ | before meets (E); after stops | **not buildable** (Γ infinite; `core.routes` enumerates a finite powerset). Nearest statable: L307's finite redundancy (below) and §5's fact that under V2.2 every route has a critical singleton, which gives S = ∅ for L311 by argument |
| V2.2: L307's redundant Γ = {a,b} | before meets (E) via G = {a,b}; after stops | built (x input, y = x; a, b both y = x): off (E) T, S = {{a},{b},{a,b}}, witness ((e,b0), {a,b}); V2.2 (E) F, S = {{a},{b}} |
| V2.3: E_rev on C_id | before: witness at (1,b), b ≠ b0, {1} vs {2}, G = {r_L}; after: fails | as claimed: witness ((1,b2_45), {r_L}); V2.3 Dep F. E_fwd on C_id the same (witness {c_H}) |
| V2.3: M13 | unaffected | as claimed (witness at (e,b0), a ≠ 1) |
| V2.4: the listed cases | E_enc, ℰ_one, ℰ_myth1, M1–M3, lookups stop; E_fwd, ℰ_two, ℰ_myth2 stay | as claimed; **also stop, not named**: R3-Q1's hand-turned vane, E8 p_δ's identity candidate, E_rev under τ′ (H only) |
| V2.5: FC30.new1 (e) | Dec → Sel: the student's copy counts as an explanation; "every declared transport for which a population and survival condition are merely stipulated becomes Sel" | as claimed for (e), the link with no earlier holding; **not** for (d), the copy of a worked-out formula: Dec under U, T, T′ with H = ∅ (the source's earlier representation excludes Sel). The general claim holds of holdings with no earlier representation of t or cod t (§2, §6) |
| V2.6: FC72.new2 (b), (d) | Greeks' C: no conflict, not rivals, no kind ii; finer C unaffected | as claimed: Greeks' C conflict pairs [(1,S),(dec,S)] → [], rivals T → F, kind ii → none; finer C kind i both |
| V2.7: D w,y; c:(w,y); L_c = {(1,0)}; χ allows only R_c = {(0,0)} | before: ConfCl by the second disjunct; after: none | as claimed: (first F, second T) → (F, F). The candidate does not meet (E) either way (C = {(1,b0)}: no contrast, Dep F) |
| (the reply's unsettled edge) L309 under V2.1 | needs S recomputed | built (a: y = x, b: y = 0): off S = {{a}}, full (E) F (F1, F2, A fail); V2.1 the same. L309.s1 stays realized |

## 8. The edges

The reply's edges (tabulation §4, V2.1–V2.8, and its prose edge on L309), each marked **computed** (the computation shows it), **contradicted** (it shows otherwise) or **not settled by computation** (with what would settle it); then the edges the computation shows that the reply did not name. Also in `results/S108 Part A - section 2 - variants computed.json`. Counts: named 23 (computed 14, contradicted 3, not settled 6); added 17 (computed 15, not settled 2). Where one row joins a computed part and a contradicted or unsettled part, the standing is that of the part the reply asserted beyond the formula (R5, R7, R17, R20 say which).

**Named by the reply**

| id | variant | kind | item [mark] | standing | what shows it | what would settle it |
|---|---|---|---|---|---|---|
| R1 | V2.1 | moves | Dependence (D6.5), a conjunct of (E) [S2] | computed | Dep F→T on 57 / 74 / 8 generated candidates (single / value maps / MID proper), none T→F; the reply's case ¬Acc → Acc — note: the reply's gloss 'commitments that do no work (L313) become accounts' holds of 49 of the 57; 8 keep a commitment doing work for (F1)/(F2) while no block carries the contrast (§5) | — |
| R2 | V2.1 | changes with | D7.2 routes (S), L289 [FROZEN] | computed | ∅ ∈ S for 63 generated candidates under V2.1, 0 off; L299.s1 realized by 20 off and 20 under V2.1; L307's S by 17 and 17; L309's finite realization S = {{a}} under both | — |
| R3 | V2.1 | constrains | L275.n1 [S2] | computed | FC29 unchanged under V2.1 (§6): a contrast no admitted edit realizes sits at no pair of C, and V2.1 still asks a pair of C | — |
| R4 | V2.2 | blocks | L311.s2 ('(B) records the collective contribution') [FROZEN] | not settled by computation | finite part computed: under V2.2 every route has a critical singleton (0 of 1,297 routes without one); so an infinitary Γ in which no singleton is critical in any route has S = ∅ and (B) records nothing (argument, two lines, §5) | a computation of S over an infinite Γ (the program enumerates a finite powerset); or the owner reading L311 as a claim about its finite truncations |
| R5 | V2.2 | constrains | L299.s1 ('a block may be critical while no singleton in it is') [FROZEN] | contradicted | 'constrains' computed (realizations 20 → 1); 'such a candidate now fails (E)' contradicted: under V2.2 one generated candidate has S = {{k0,k1},{k0,k2},{k0,k1,k2}}, Γ meets (E), block {k1,k2} critical in Γ, no singleton of it critical (the critical singleton k0 lies outside the block) | — |
| R6 | V2.2 | changes with | D10.4 / D10.6 (problems; easy to vary; solved) [FROZEN / S2] | contradicted | V2.2 moves no pair's conflict pairs, rivals or kind (0 of 3,835); Prob_j (D10.1) reads Riv and NotOut, not the value of Acc; so no problem is added or removed | — |
| R7 | V2.3 | blocks | L329.s3 (identification, (I1)) and E2; L331.s2 [FROZEN (L329.s3); S2 (E2, L331.s2)] | contradicted | 'no candidate meets (E) on a contract {1}×B' computed: 168 → 0 of 1,953 generated; E_rev and E_fwd on C_id T→F; contradicted as to L329.s3: identification (Z_y ≠ ∅ ∧ |f[Z_y]| = 1) reads no (E); FC57, FC58, FC28's Ident part and FC28.new2 unchanged under V2.3 (§6); FC28's (F1), (F2), (A) on C_id unchanged (L325.n6 'faithful' stays). What V2.3 blocks is any account on a {1}×B contract (computed), not L329.s3 | for L331.s2: the two balances built as a question on {1}×B with a candidate (the program computes their kernel, FC59, FC60, not (E)), or a reading of 'account' there |
| R8 | V2.3 | changes with | D3.3 (S1: Ident, identification contracts) [S1] | not settled by computation | V2.3 leaves Ident(p) as it was (D3.3 reads no Dependence; FC28's Ident part under V2.3, §6); the reply's 'would need contracts that vary only the boundary re-read' is a proposal for D3.3 | section 1's computation of V1.4 (Ident with a ≠ 1) read together with V2.3 (tabulation §7, same axis) |
| R9 | V2.3 | constrains | L253.s1 (the query held fixed) [FROZEN] | computed | the switch reads only the pair's edit in NC2's pair loop; no query changes in any run | — |
| R10 | V2.4 | blocks | — (the owner's decision S45, with S44) | not settled by computation | an owner's decision, not an item; V2.4 = round 3's (E) exactly (§2: the S106 printout's 10 MOVED cases move back) | the owner's yes or no in the later step (S52) |
| R11 | V2.4 | moves | (E) itself; what Bearing reads (D9.10, S3) [S2 / S3] | computed | (E): 11 worked cases, 972 / 776 / 301 generated accounts T→F; FC107 under V2.4: the identity candidate for p_δ (K1's criticism question) Acc T → F (its part 'base' a slot), so a criticism with that connection has no Bearing (D9.10); FC72.new2 (a), (c) not as claimed | — |
| R12 | V2.4 | changes with | D16.XV (S4), (Suff) / (Nec) at L536 / L538 [S4] | computed | Expl shrinks: 22 (case, history) T→F; 1,944 generated; FC23.new2 (f) under V2.4: ℰ_one in no defeat set of (Suff) under any provenance (it fails (E)); the (Nec) attack list is not computed by any claim that moves | — |
| R13 | V2.5 | constrains | L195.s1 ('a finite history H ⊆ C of edit–boundary pairs actually encountered') [FROZEN] | computed | under V2.5 Sel accepts H = ∅: 'its pairs having occurred' vacuous, fidelity on ∅ is Hom(τ) (I18); FC77 part 3's 'other choice' is the variant's reading | — |
| R14 | V2.5 | blocks (in effect) | L211.s3 ('A declared transport does not make an occurrence represent anything') [S2] | computed | FC30.new1 (e) under V2.5: the link nobody tried and nobody worked out is Sel, its fixed point {o1: Sel}, so its holding represents (D12.5); as an effect: the transport is no longer declared, so L211.s3 still holds formally | — |
| R15 | V2.5 | moves | Dec (D12.3), hence Expl := Acc ∧ ¬Dec and (Suff) L536 [S2 / S4] | computed | Account ∧ ¬Dec(t) F→T on the history 'nothing tried' for every account: 28 of 28 worked cases, 1,027 / 847 / 310 generated; no other history moves | — |
| R16 | V2.6 | blocks | L315.s1 (rivals: conflict 'in C or outside it'), L317.s6 (kind ii) [FROZEN] | computed | 310 of 310 kind-ii pairs lose every conflict pair, rivalry and kind; FC72.new2 (b): tilt and myth on the Greeks' C not rivals (§7) | — |
| R17 | V2.6 | moves | nothing in (E); problems, ETV (D10.4) and the (Nec) attack route through easy-to-vary change | computed | 0 Acc changes in every population; no kind ii remains, so ETV_j holds of no candidate; no claim computes an attack on (Nec) through easy to vary; that part is not settled | — |
| R18 | V2.7 | blocks (in effect) | L315.s12 ('the bare claim that perpetual motion is impossible is enough for a conflict with a candidate whose organization gives perpetual motion') [S2] | computed | the reply's case: ConfCl T→F; 410 of 1,822 generated (candidate, pair) lose ConfCl, all by the second disjunct alone — note: where the candidate's answer is itself the motion χ excludes (FC53 (b), L315.s16's pendulum) the conflict stays under V2.7 (suite, §6); S27's words are about what the explanation describes, not only its answer | — |
| R19 | V2.7 | constrains | D8.4 (Allow_χ, Applies) [FROZEN] | computed | the switch touches only D8.5's second disjunct; Allow_χ and Applies are read as before in every run | — |
| R20 | V2.7 | changes with | D8.6 (ConfG_χ) [FROZEN] | not settled by computation | 'no longer feeds any ruling out of a single candidate': the program builds no argument from ConfCl or ConfG_χ; computed: ConfG_χ unchanged in form (core.conf_given untouched; FC54 unchanged under V2.7, §6) | an encoding of L315.s13–s14's argument whose premise is a computed ConfCl |
| R21 | V2.8 | constrains | D16.XV (S4): 'Acc ∉ Uses(α)' [S4] | not settled by computation | V2.8 not implemented: out of scope as written (tabulation §6). The committed printout's FC30.new1 (h) already computes both readings on one case: 'symbol False, instance True' | section 4's computation of V4.4 (the same reading) |
| R22 | V2.8 | moves | (Suff)'s defeat set (L536) [S4] | not settled by computation | as R21 | section 4's computation of V4.4 |
| P1 | V2.1 | keeps | L309.s1 (interference: the full candidate fails (E) although a subset meets it) [FROZEN] | computed | built (Γ = {a,b}, a: y = x, b: y = 0): S = {{a}}, full candidate (E) F under off and V2.1 (F1, F2, A fail); the reply left it unsettled | — |

**Added by the computation**

| id | variant | kind | item [mark] | standing | what shows it | what would settle it |
|---|---|---|---|---|---|---|
| N1 | V2.1 | changes with | D7.3 (B) critical block; L293 (B)'s definition [FROZEN (D7.3)] | computed | off: every route has a critical block (0 of 1,322 without; argument §5: the Lost witness is critical); V2.1: 120 of 1,450 routes have none (63 of them ∅) | — |
| N2 | V2.1 | changes with | L313.s2 (NoWork) [S2] | computed | V2.1 admits more than L313's case: 8 of 57 new accounts have a commitment that does work for (F1)/(F2) while none carries the contrast (smallest: Γ = {k0} on p0, the answer on p1 set by the background) | — |
| N3 | V2.2 | blocks | L307.s1 (redundant routes S = {{a},{b},{a,b}}) [FROZEN] | computed | no candidate realizes that S under V2.2 (17 → 0; all 17 become {{a},{b}}); argument: every route has a critical singleton, and in {a,b} neither is | — |
| N4 | V2.2 | blocks | L313.n3 ('When Γ is infinite, a block of such commitments can still be critical') [S2] | not settled by computation | by the argument of R4: L311's candidate has S = ∅ under V2.2, so its example goes | as R4 |
| N5 | V2.2 | changes with | D7.3 (B): every route has a critical singleton [FROZEN (D7.3)] | computed | 0 of 1,297 routes under V2.2 without a critical singleton (21 of 1,322 off) | — |
| N6 | V2.3 | moves | (E) on every contract whose contrasts all sit at pairs (1,b), not only on {1}×B [S2 (D6.4)] | computed | 253 generated accounts T→F, of which 168 on contracts {1}×B′; the other 85 on contracts that hold an edit but carry their contrast only at boundary pairs | — |
| N7 | V2.4 | moves | E8 p_δ's identity candidate (K1's criticism question, FC107); R3-Q1's hand-turned vane; E_rev under τ′ (H only) [S2 / S3] | computed | all three T→F under V2.4 (§2); the reply named the myth's bearing, not these | — |
| N8 | V2.4 | changes with | D6.10 (tables) and the generators' E_enc [S2] | computed | 972 of 1,027 generated accounts fail (E) under V2.4 (E_enc 864, lookup 102, random 6), each by a slot: after S106 most generated accounts have a component that pins the answer | — |
| N9 | V2.5 | changes with | D5.5 Hom(τ) (I18) and D6.7 (F2) [S2] | computed | Acc ⇒ (F2) ⇒ Hom(τ); with H = ∅ allowed, Hom(τ) ∧ Θ admits t ⇒ Sel(t;{t},id,∅); so on a holding with nothing tried Account ∧ ¬Dec(t) ⟺ Acc ∧ Θ admits t: ¬Dec(t) adds only Θ's admission (1,027 of 1,027) | — |
| N10 | V2.6 | changes with | D8.3 Riv (its ∃ over A_D × B_D) [S2] | computed | 492 kind-i pairs keep kind i and lose their conflict pairs outside C; rivals then need a conflict in C | — |
| N11 | V2.7 | changes with | L317 'solved with no test' by an argument from a claim (D10.6) [S2] | not settled by computation | 23 generated (candidate, pair) where the candidate meets (E) lose ConfCl (20 at a pair of C): the ground for that route to solving goes there | an encoding of the argument from ConfCl (as R20); the program computes ConfCl, not the solving |
| N12 | V2.1–V2.4 | independent of | D8.2 Conf, D8.3 Riv, D10.2 kinds [S2 / FROZEN] | computed | 0 of 3,835 pairs change conflict pairs, rivals or kind under each of V2.1–V2.4 | — |
| N13 | V2.5, V2.6, V2.7 | independent of | (E) (D6.7) [S2] | computed | 0 Acc changes in every population and case | — |
| N14 | V2.4 | changes with | D6.3's quantifier (I136) and exemption (I176) [S2] | computed | FC23.new1 (h) under V2.4: counterexample: (E) (F,F,T,T) under (every, some, some-exempt, some-exempt-set) for one component, ⊥ at 1, 1 at e1; with NC1 back in (E), (E) depends on the quantifier again — note: contradicts the reply's (e): 'V2.4's effect is quantifier-independent' (it cited FC23.new1 (h), which holds of (E) after S106, not of V2.4) | — |
| N15 | V2.5 | constrains | L195.n4 / D12.1's exclusion ¬∃o ≺ o_t: Rep(o, x) [S2] | computed | FC30.new1 (d) under V2.5: the student's copy of a worked-out formula stays Dec under U, T, T′ with H = ∅ (the source's earlier representation excludes Sel); only (e), the link with no earlier holding, becomes Sel — note: so V2.5 reaches the owner's S41 Q2 example only where the declared link has no earlier representation in its history; the copied formula of Q2, as the program encodes it, stays declared | — |
| N16 | V2.2 | no claim separates | the suite (FC21–FC40) and D6.4's block quantifier | computed | no claim's result moves under V2.2 (§6); only the generated worlds (23 / 20 / 4) and the built L307 candidate separate V2.2 from D6.4 as it stands — note: a gap for the map: the text's cases and the suite do not test a Dependence that needs a block of two or more | — |
| N17 | V2.1 | no claim separates | the suite and D6.4's Lost clause | computed | no claim's result moves under V2.1 (§6); no worked case moves (§2); only the generated worlds (57 / 74 / 8) separate it — note: a gap for the map: every worked case with a contrast has a block that loses it | — |

## 9. Inventions and program choices (S36)

Every variant was implementable as written; none needed a nearest reading. What this agent chose, not the theory (each recorded here, none applied to the theory):

| id | choice | other choices |
|---|---|---|
| P-S2-1 | under a variant the varied definition replaces the current one wherever the program computes it by name (`account(reading="S106")`, `sel(h_nonempty=True)`, the two hand-written 'H nonempty' tests); comparison readings (`"r3"`, `h_nonempty=False`, `round2`) kept; D6.4 varied wherever NC2 is computed, round 3's (E) included | vary only the default; then the claims that name "S106" or "H ≠ ∅" would not move |
| P-S2-2 | V2.7: a caller asking for D8.5's two disjuncts gets the deleted second as False | raise an error; return the second as computed and ignore it in the whole |
| P-S2-3 | Account ∧ ¬Dec(t) on four histories set by hand (Θ, I90): Con, Sel on {(1,b0)}, nothing tried (H = ∅, admitted, no trace), Dec (not admitted), as `claims_s41.provenance_of` and FC77 build them | other histories; provenance computed from a chain (`prov_fixed_points`), as FC30.new1 (d) |
| P-S2-4 | V2.2's L311 case (infinite Γ) is not built; nearest statable: L307's finite redundancy, and the argument that under V2.2 every route has a critical singleton | a finite truncation d_1..d_N (not the case: it has a route of one commitment, d_N, which L311 excludes) |
| P-S2-5 | the finite realizations of L307 (a, b both y = x) and L309 (a: y = x, b: y = 0) on a target x → y with one edit setting x = 1 | any other organization with the same S |
| P-S2-6 | "kind" of a generated difference = the target's generator family × the candidate's generator (E_enc, random, lookup) × direction × the conjuncts that move | kinds by size, by contract shape |

The reply's own new inventions are the variants V2.2 ("a nonempty block" read as "a singleton") and V2.3 ("a pair of C" read as "a pair with a ≠ 1"); both implemented as the reply states them.

## 10. Unsure

- **Who ran the suite.** The rule gives the whole suite on each computing copy to Sonnet through the harness (`run_claims.py`); this agent has no way to start a harness worker, so the runs are its own scripts'. The check a harness job makes was made: the off run equals the committed printout in every claim's status and every part's status and written result. The orchestrator may give the reruns to the harness.
- **Load.** Every run was made while the other sections' agents ran (load 5–8 on 4 cores); the suite's searches stop at a wall-clock cap (45 s). The off run still matched the printout exactly; every difference reported in §6 is in a claim whose code reads the varied definition, and none in a claim that reads none. The generated-world scripts have no time cap.
- **Dec on the worked cases** is Θ by hand (I90, P-S2-3): the program builds histories only for the student's formula (FC30.new1 (d), (e)), the bridge (FC84.new1) and CT8. The four histories are the program's own, not the text's.
- **Kinds** of generated differences are the generators' families (P-S2-6); smallest witnesses in SMALL are degenerate (a one-value port, an empty relation giving ⊥); the MID proper population gives witnesses on targets with every domain ≥ 2 and Sol_D(1,b) ≠ ∅.
- **L311** (infinite Γ) is not built; its standing under V2.2 rests on the two-line argument of §5 (every route has a critical singleton).
- **V2.8** was not implemented (tabulation §6's flag, rule 4); whether it is taken up is the orchestrator's.
- **Quotations** (rule 14): the reply's quotation of L195.s1 is not verbatim (tabulation §9); the edges above read the text's L195.s1 ("of edit–boundary pairs actually encountered"). The reply's "before" values that this computation reran (V2.1's case, E_rev's witness on C_id, FC72.new2 (b), FC30.new1 (e)) are as the reply gives them.
- **Words.** "True"/"False" appear only as program values and identifiers; no statement or gloss here uses a word S23 lists; "model" names only the program's folder.

Computed by one Opus 5.5 agent under rule 5, 28 September 2026. Nothing ruled.
