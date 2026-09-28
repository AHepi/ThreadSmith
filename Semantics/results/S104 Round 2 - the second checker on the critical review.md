# S104 Round 2 — the second checker on the critical review

*Opus 5.5, second checker (orchestrator's decisions 1–7), 28 September 2026. Terse by decision S40. (a) keep the first checker's fix as merged; (b) the review's proposal; (c) a third fix. Reasons weigh arguments, not sources.*

Baseline (merged model as committed, scale 4, cap 45 s, `--no-write`): 101 H, 3 CEX (FC18, FC23, FC63), 9 NT (FC31, FC32, FC35, FC89, FC94, FC104, FC105, FC107, FC110) of 113; 366 s. Reproduces the integration.

## 1. Rulings (R1 and R3 first)

R1/R3, every chain history of 1–4 occurrences (4,680; held, trace, Sel's conditions per occurrence), Rep as every fixed point of (R): a scratch run of the logic now in the model as `prov_fixed_points` (claims_b.py). Timeout 120 s.

| reading | Sel+Con at some fixed point, without / with I161 | fixed points per history |
|---|---|---|
| U (as worded) | 0 / 0 | 0–5 (selection: none) |
| K (staged) | 0 / 0 | 1 |
| T (Held in Sel, Con, Build) | 1,085 / 0 | 1 |
| T′ (Held in Con, Build; Sel's exclusion by Rep at o ≺ o_t) | 1,300 / 0 | 1 |

| case | U | K | T | T′ |
|---|---|---|---|---|
| R1 mixed (o2 held, trace, selection; o1 unheld), no I161 | Con | Sel | Sel+Con | Sel+Con |
| same, with I161 | {} or Con | none | Con | Con |
| first construction (L405) | {} or Con | none | Con | Con |
| selection | no fixed point | Sel | Sel | Sel |
| built on a selected representation (L201) | no fixed point | Sel, Con | Sel, Con | Sel, Con |
| earlier holder by a declared transport, later selection (L195 with L211) | no fixed point | Sel | **none** | Sel |

T′ is a third cut, found here: it reads "represented" as Held only where L405 forces it (Con's target, Build's output), and keeps (R), staged along ≺_h, in Sel's exclusion (L195, L201, L411 with L211).

| id | ruling | reason (one line) | program |
|---|---|---|---|
| R1 | (b), corrected | Adding ¬∃h' ⊆ h(t): CT(h', t) (I161) excludes Sel ∧ Con by definition under U, K, T and T′. Two corrections: it is not L201's "no criticism" (D12.2 asks no criticism, so that clause gives no exclusivity); it writes L193's "exactly one" and L411's "the traces differ". And the mixed case gives Con only under T, T′ (U: {} or Con; K: none). FC12.new1 and FC83' did rest on tags (`sel` banned a hand-set 'cod'); both now compute Rep. | FC12.new1: 146 chains (pole, t's holding and Sel's conditions computed) + 8,640 random transports: no Sel ∧ Con under U, K, T, T′; without I161: witness under T. FC83: 146 chains, holds under all four; without I161: witness under T. |
| R3 | (c): Q1 is not the owner's; cut T′ (I162) | U breaks L526 (a cycle) and L193 (0–5 fixed points; a selection has none). K breaks L405 (a first construction represents nothing). T meets L405, L526 and, with I161, L193, but a declared earlier holder then blocks a selection, against L195 with L211. T′ meets all four. Other side, one line: T needs no recursion along ≺_h, and K keeps (R) everywhere, but each fails one computed case above. | FC98 (a′) no cycle under K, T, T′; (c) one fixed point each; (d), (e) as in the table above. |
| R2 | (c): the formula, with the cut | With Q1 ruled, the reason for a pointer is gone. T9 now writes D12.1 as ruled: ¬[∃o ≺_{h(t)} o_t, x ∈ {t, H, surv, cod t}: Rep(o,x)] ∧ ¬[∃h' ⊆ h(t): CT(h',t)]. It settles H05, I52 (part), I53, I128, I161 and I162 (rule 6). | L195: −11 prose words. |
| R4 | (b) | C_id = {1} × B holds no edit ≠ 1, so D3.3 as written ("C holds edits to the observed value") makes the pole's identification question no identification question. An L-setting breaks E_rev (FC28 look). New: Ident :⟺ fibre ∧ ∃(a,b),(a′,b′) ∈ C: obs(a,b) ≠ obs(a′,b′) (I163). L151 gets it in symbols (R4-L151, new, −6). | FC28 (R4): the observed L takes 8 values over C_id; no edit ≠ 1 alters it. |
| R5 | (c) | One edge set. D18.1 = DEP: NC → (O), (Q), C, ℓ, δ, with no (K) (NC0–NC2 read no signature) and no t (an argument, as for (F1), (F2), (A)); NV → (O), C, Σ. L526 becomes the pointer "(D18.1)", because the formula would write I20's δ (the designation) where the text's δ is a defect (L377). | FC32 computed: NT → H (the code reads exactly DEP's classes). |
| R6 | (b) | L584: Sel(t;𝒯_t,μ_t,H_t) ∧ (a,b) ∉ H_t ∧ Viol(t;a,b) (D12.7′, one history). | — |
| R7 | (b), with w ≤ L_occ inside the formula | No prose added: −5 (A3's version added 17). | FC102 (b″) unchanged. |
| R8 | (c) | L395 is now all symbols with D9.9 (i)'s MadeFrom clause; the pointer (D9.9) covers u⁺ and α⁺. −15 (A3's version: +10). | FC71 (i′): a leaf made from ¬(T∧B∧I) blocks α⁺. |
| R9 | (b) | Pointer "(D9.4, D9.8, FC70, FC56)"; X^ξ_j and Usable^ξ_j defined in D9.8. | — |
| R10 | (c) | "an account" → \(\mathcal E\) (D5.3): the symbol, kind formal, so no word is substituted; −1. | — |
| R11 | (b), confirmed | S31's values are the appraisal's (𝒩, D14.8); port values are an organization's data. The tag is dropped, and Q9 is then ruled (§2). | — |
| R12 | (b), confirmed | Q3 does not block; nor is it the owner's (I51 kept). | FC35 stays NT. |
| R13 | (b), confirmed | L590 with E8 and L161 settle Q13. | FC107 tested on E8: NT → H. |
| R14 | (b) | Recounted strictly in §5. | — |
| R15 | (b) | "classically sound" → Forms_cl := the forms whose every instance has Incons(Prem ∪ {¬concl}) (D9.1). Changed in D9.7, D9.9 (iii) and the code's labels (S23). | FC71 (iii), (iv) relabelled; results unchanged. |
| R16 | (b) | Recorded as I164; A3-L528.1 settles I164. | — |

Counts: R1–R4: (b) 2 (R1, R4), (c) 2 (R2, R3). The other twelve: (a) 0, (b) 9 (R6, R7, R9, R11–R16), (c) 3 (R5, R8, R10).

New inventions: I161 (Sel's ¬CT), I162 (cut T′), I163 (Ident's varying observed value), I164 (Universal) (`inventions register - addendum after round 2.md`).

## 2. Owner questions, re-sorted

The orchestrator's three proposed changes are confirmed on the texts: Q9 is not S31's values question; Q3 does not block; Q13 is settled by L590 with E8 (and FC107 now holds on E8).

Re-sorted: 25 → **3 the owner's** (Q2, Q6, Q15). The other 22 are ruled on argument, each with its other side in one line, in `owner questions after round 2.md` §B:
- Q1, Q3, Q4, Q5, Q7, Q8, Q9, Q10, Q11, Q13, Q14, Q16, Q17, Q19, Q20, Q21, Q22, Q23, Q24, Q25 are settled by the texts or the computations.
- Q12 and Q18 are ruled on the text; their S20 sides go to parked P6 and P7.

Only Q1 and Q5 change the maths: Q1 by the cut T′; Q5 by D15.2, per execution (I153).

| # | stays the owner's because | in plain words |
|---|---|---|
| Q2 | L17 and L536 disagree on what counts as an explanation (whether meeting (E) needs a link that is not declared); no owner's word settles it | If something passes all four of the theory's tests for an explanation, does it count as an explanation even when its link to what it explains was simply declared, not found by trial or worked out? Example: a student copies a correct pendulum formula and writes "this stands for the pendulum": if it passes every test, is it an explanation? |
| Q6 | L55's definition and the body's uses disagree on what counts as an episode of construction (creativity) | Can something be created in a stretch of work where the question itself never changes, or only where the question gets reworked along the way? Example: an engineer designs a new bridge to a fixed brief: is that an episode in which something can be built, or must the brief itself change during the work? |
| Q15 | whether a question with no definite answer at the baseline can have an account (what counts as an explanation); L255's "differs" and its second disjunct pull opposite ways | If in the normal case a question has no single answer, and a change gives it one, can anything explain that change? Example: in still air a weathervane may point anywhere; a north wind makes it point north. Can a model count as explaining "north", or only a change from one definite answer to another? |

## 3. Runs

Whole suite, `PYTHONHASHSEED=0 python3 -B -m model.run --scale 4 --time-cap 45 --no-write --brief` (timeout 1800 s), from `model after round 2/`:

| | H | CEX | NT | of |
|---|---|---|---|---|
| integration (reproduced here, 366 s) | 101 | 3 | 9 | 113 |
| after the second check (385.8 s) | 103 | 3 | 7 | 113 |

CEX: FC18, FC23, FC63 (unchanged: I94, U3, I99). NT: FC31, FC35, FC89, FC94, FC104, FC105, FC110. Every claim whose status or parts changed (parts compared label by label):

| claim | status | parts | why |
|---|---|---|---|
| FC12.new1 | HOLDS → HOLDS | 2 → 4 | R1: Rep computed from t (fixed points of (R)), under U, K, T, T′, with and without I161 |
| FC28 | HOLDS → HOLDS | 4 → 5 | R4: Ident on C_id under D3.3 (I163) |
| FC32 | NOT → HOLDS | 1 → 2 | R5: computed on D18.1 = DEP; NT → H |
| FC71 | HOLDS → HOLDS | 4 → 5 | R15 labels (Forms_cl); R8: (i′) MadeFrom |
| FC83 | HOLDS → HOLDS | 1 → 2 | R1: Rep computed, U, K, T, T′; without I161 a witness |
| FC98 | HOLDS → HOLDS | 5 → 6 | R3: (a′) K, T, T′; (e) the L211 case |
| FC102 | HOLDS → HOLDS | 5 → 6 | Q25: (b3) end rule 'stop' |
| FC107 | NOT → HOLDS | 1 → 2 | R13/Q13: tested on E8; NT → H |

No other claim changed in status or in any part's label or status.

`s104_external.py`: output byte-identical to the integration's (FC-E1–FC-E5 reproduced). `s104_creative_transport.py`: 2 lines differ, both CT8:
- the stale label is now "Sel as D12.1 has it after round 2 (… I161 …)";
- R5 (nothing represents, Build met): "selected" → "neither". I161 makes a trace preparing t exclude Sel; with tags, Con needs a tagged target; under T′ (Held) the pair would be constructed.
CT1–CT7 unchanged.

Text: `apply text changes.py`, adapted to read `text changes after the review.json`, all checks kept. Results:
- 43 applied on 32 lines; 0 refused; 0 held;
- S95 scan: 3 new hits ('Accepted', allowed), 0 forbidden (S23);
- S96 scan: 0 new;
- headings, defined terms and labelled formulas: none missing;
- words 16,394 → 16,284; **outside formulas 15,611 → 15,409** (the integration's version: 15,463).

## 4. md5 before → after

| file (in `S104 Round 2 - maths after the reading/` unless named) | before | after |
|---|---|---|
| tests/104 The semantics, standing alone, after round 2.md | d0b3987cb89626585a1f6d68c2abc270 | 735ec1e8256cc6a251715a031944ea65 |
| tests/103 (input, unchanged) | f31ebb1f050783f1a84f6136cec20fcd | f31ebb1f050783f1a84f6136cec20fcd |
| apply text changes.py | 43720c2a4effe04dec12c0bc65fec90d | 6865929abb5487c11f85515d21a930a7 |
| text changes after the review.json | (new) | 3f43745f9da7680eb85f60cef8b38172 |
| formal core, after round 2.md | 04ac592210d628a3a79f681dfed281b7 | d8011c669603725937dc4cb36ff28177 |
| formal claims, after round 2.md | e94171ead4cda982fc1559ca97ef3006 | bbebe5497dbf3f98eb9a69eb4dc93699 |
| formal claims, after round 2.json | 293de8bf4f74d25817ac0a8a3aa51ca1 | 4638ded3c46b7c08f170f0d601f0b979 |
| inventions register - addendum after round 2.md | c94396e5fc03d5f07b9ae002bd31f44f | 00404849ca9b88cdd09934849445c724 |
| owner questions after round 2.md | fa48546d99a943ee1523df6f43a2b046 | 684cb7c378110a3a32723d17297807c3 |
| parked after round 2.md | c74058bac84a0ed56caa080ad470751f | a62db83b8420c7e948ceaade2fadef98 |
| model after round 2/model/claims_a.py | a891df77a1dd86296e010696018867db | 62bb05be912fafed7b66659006c6f971 |
| model after round 2/model/claims_b.py | bea41c1743350995a76a10973d4a7189 | f788408a75b40553fe83d839ee371efe |
| model after round 2/model/claims_area1.py | 2f013c02b66f71d48054838f673d1004 | c02c209514787cae74eadf08377be3e0 |
| model after round 2/model/args.py | 55a5452bcd6387fe1da3fb04407de57f | 10fff81e8bb77a114566275d7a95deda |
| model after round 2/model/inventions_model.py | 317f593d410dff824ad082a222bb0ccb | dba0c346a84ed4f1996f17026d288f5a |
| model after round 2/s104_creative_transport.py | a2e64545ac54764362f5eb8647c9fc07 | cdde2bf3c1270d185463a12a673d36e5 |

Unchanged: the three area files, the integration report, `model/core.py` and every other model file, `s104_external.py`, tests/103. The integration's versions are in git at 84c4969.

## 5. Moves (strict)

The governing note's definition: formal changes that answer a challenge that holds (M, W, I; HM, HW, INV), plus the text changes applied. Not counted:
- register entries: I83/I84 (U6), I161–I164 as records, I164 (R16);
- re-based claims, whose statement follows a counted change with the result unchanged: FC21 (a2), FC44, FC52, FC104 (= D5.7), D14.7 (= D13.8), FC75 (= D11.4);
- new test claims or test parts: FC2.new1, FC4.new1, FC12.new1 (and its rewrite), FC21 (d), FC23 (c)(d), FC80 (d), FC90, FC92 (e), and this check's FC28 (R4), FC32, FC71 (i′), FC83 rewrite, FC98 (a′)–(e), FC102 (b3), FC107;
- Part XV (NF02, NF03, NF05 do not hold; E06 → Q2).

| group | formal changes | n |
|---|---|---|
| A1 | D2.1′, D2.4′, D2.6, D3.3′, D3.4′, D3.6′, D4.6′, D12.1′, D12.7′, D12.8′, FC02′, FC06′, FC20′, FC30′, FC77′, FC83′, FC101 (code, H18) | 17 |
| A2 | D6.3, D6.9, D8.2, D8.3, D8.5, D8.new1, D10.3, D10.6, D5.7, D7.4, E1, D1.4, E2/FC58, FC25, FC33, FC48, FC50, FC51, FC53, FC63, FC64, FC65, FC67, FC68 | 24 |
| A3 | D0.2, D9.2/D9.4, D9.9, D9.10, D11.3, D11.4, D12.1 (H09), D13.3, D13.7, D13.8, D14.1, D15.1, D15.2, D15.5, D16.3, D16.5, D18.1, FC56, FC70, FC74, FC94, FC102 | 22 |
| second check | D12.1 ¬CT (I161; R1); the cut T′ in D12.2, D13.3, D18.1 (I162; R3, E03); D18.1's one edge set (R5); D3.3 Ident (I163; R4); Forms_cl in D9.1, D9.7, D9.9 (R15); D9.8 X^ξ (R9); D15.2 per execution (Q5, E17); D16.4 𝔓^adv through Θ (Q8, NF12); D0.2 primitives classed (Q4, FC98 (b)) | 9 |
| **formal** | | **72** |
| **text changes applied** | the integration's 42 (8 amended: T9, A2-T6 (now kind formal), A3-L393.2, A3-L395.1, A3-L526.1, A3-L528.1, A3-L584.1, A3-L626.1) + R4-L151 (new) | **43** |
| **moves** | | **115** |

The integration's formal changes, recounted: 63. The review gave 71–73; the difference is FC21, FC23, FC52, FC75, FC80, FC90, FC92 and FC104, excluded here as re-based or as tests. 63 + 9 = 72 formal; 72 + 43 = 115 moves. The series continues.

## 6. Unsure

- T′ is a cut this check introduced; it is not the review's or area 3's. It rests on FC98 (e) (L195 with L211) and on ≺_h being well founded below o_t.
- FC12.new1 and FC83 compute only the output's holding and Sel's conditions from t. Earlier occurrences and traces are still Θ by hand (I90).
- Q23 was ruled, although it concerns what counts as an argument, because L397, S23 and S27 point the same way. If the owner reads S23 otherwise, it goes back to §A.
