# S105: Round 3 — critical review of the round

*Fable 5.1 (decision S35, used sparingly on the owner's word; rule 8 of `results/S105 Round 3 - how the replies will be read, written before sending.md`, read whole first), 28 September 2026. Read: decisions S20–S42; the tabulation; the four `.response.txt` (nothing else of the returns folder); the three area files with their runs and text-change JSON; the integration report, the formal core and claims after round 3, the inventions addendum, the owner questions, the parked file, the moves list, the apply program; `tests/105` diffed against `tests/104 … with the owner's answers` (8 lines differ, 632 lines both). Reran the program where a result carried weight (§1). Wrote this file only; nothing else written, no earlier file touched. Obeys S23 except where it quotes.*

## 0. In one line

Nothing of substance to contest: every verdict I checked holds on its reason, every fix is maths, code or one of the three text changes, no owner answer is reversed or weakened, the one owner question is the owner's, and the count of 29 moves stands. Four minor objections, each with its fix (§3).

## 1. Reruns (`model after round 3/`, PYTHONHASHSEED=0, `-B`, scale 4, cap 45, `--no-write`, under `timeout`)

| run | result | agrees with |
|---|---|---|
| whole suite | 125 H, 2 CEX (FC23 (b), FC63 (c-i)), 7 NT (FC31, FC35, FC89, FC94, FC104, FC105, FC110) of 134; no traceback; 495 s | integration §2 (125 H, 2 CEX, 7 NT of 134) |
| FC30.new1 (a)–(f), FC77, FC12.new2, FC98.new1 | all H; (d) Dec at o2 under U, T, T′, Sel under K only; (e) H = ∅ Sel after round 2, Dec with I171 | area 1 rows 8, 1, 10, 3, 4 |
| FC98.new2, FC72.new1, FC84.new2, FC28.new2, FC32.new1, FC90.new1, FC80.new1 | all H; FC98.new2 (a): no fixed point on the infinite chain (B3 right, S1's two fixed points wrong) | area 3 rows 19, 1–4, 20–24, 27, 14; area 1 rows 9, 6 |
| FC22, FC26, FC62, FC23.new1 under `S105_SLOT_QUANTIFIER=some-exempt` | FC22 H (Q15 untouched), FC26 H, FC62 CEX, FC23.new1 H | area 2 §3; owner question R3-Q1 |
| `s104_external.py` | body byte-identical to the round's printout (md5 86a67664a9a3584351fd4836a4140b69): FC-E1–FC-E5 unchanged | integration §3 |
| `s104_creative_transport.py` | CT1–CT7 identical to the printout; CT8 differs only by the five T′ lines | integration §3; CT8's five T′ lines: R1, R3, R5 constructed; R2, R4 neither |
| CT8 with `held_out` printed (scratch copy) | `held_out` (faithful(cq)) True in all five readings; the constant `held_trees` decides nothing | §3, objection 4 |

## 2. Checks against the rule and the owner's words

| check | result |
|---|---|
| rule 2: replies | four `.response.txt`, each ending END OF REPORT; no `_pass2`/`_pass3` file; receipts not opened by me (as instructed) |
| rule 4: tabulation | 81 findings (41/6/34), job counts 18/29/21/13, quotations compared, S40 flags 6, S41 flags 0: checked against the four replies, nothing missing or misread |
| rule 5: verdicts | one line each, code M/W/I/N; every "not run" model run before its row (B1 sketch, B7, W3, W8, S1 witness, P7, P8, C-P1, C-P5, N1–N3) |
| rule 5.3: computed inputs | provenance always by fixed point from held/trace/Sel-condition flags (I90, Θ by hand), never a tag; FC30.new1 (d) computes the student's copy from its history, the round-2 `admitted=False` witness kept only as (a)'s record; one idle constant in CT8 (objection 4) |
| rule 5.4 / 14: text | 11 changes: 3 deletes, 7 formulas, 1 pointer; refused 0; words outside formulas 15,388 → 15,324; no new word outside pointers; each span found once, undone byte for byte |
| rule 6: inventions in the text | four, each named in so many words with its formal statement: I166 (L397, T1), I162 for Build (L405, T4), I169 (L375, T5), I50 narrow at L220 (T5 of area 1); I167–I182 recorded, 17 provisional ids → 16 numbers, no collision with the replies' own "I167"–"I172" |
| rule 7: integration | three-way merge, one textual conflict (`sel`'s signature) conjoined; every claim equals the start or the one area that changed it; X1–X17 pairs listed; no two fixes conflict |
| rule 11 / S41 | Q2: L17 unchanged, D16.XV's Acc ∧ Dec ⇒ ¬Expl unchanged, I171 widens Dec's reach (FC30.new1 (e)); Q6: FC84.new1 (a) still Con, I173 defines "immediately after"; Q15: FC22 (b) H under all four D6.3 readings, I172 keeps still/north an identification; Q23: T1 writes I166 (a premise alone usable iff accepted), T2/T3 delete what contradicted it. Nothing reversed or weakened |
| rule 11: O1–O6 | O1–O3 formulas at L61, L49, L69 (no added prose; the four replies' O2 spans rightly refused, S40); O4, O5 deletes; O6 no clash (FC72.new1 (c), (d)); the orchestrator's reading corrected as area 3 §6 records ("not a repair"), S27/S28 untouched |
| rule 12 | one owner question, R3-Q1 (§4); nothing parked, none on values |
| rule 13: forbidden words | none of S23's list in `tests/105`, the formal core, the addendum, the questions, the moves, the integration report (own scan; the apply program's S23 scan 0); "Accepted_j", "Held_ℓ" are symbols |
| S20, S21, S25–S28, S33, S34 | I171 (H ≠ ∅) is no count, grade or list; I177 (Env) is physical and sits in D15.8's module, read through Θ; nothing on what hard to vary covers; P1–P7 untouched |
| rule 15 | replies' quotations not in text 104 (B3's L199, B7's "edits to the observed value", T6, A2-T3/T5/T13, A3-L375/393/626) ruled on the text, as each area file records |
| rule 16 | §5 |
| book quotations | none in the round's files |

## 3. Objections (all minor; none stops a fix)

| # | weight | what | reason (texts or computation) | proposed fix |
|---|---|---|---|---|
| 1 | minor | D16.4 keeps `Acc(c, p, t, Γ)`, four data, after F4 changed D14.7 to five | S-e-Acc's defect (Acc is not a function of the four: FC90.new1 (c)) stands in D16.4; integration §8 flags it, no area ruled it | D16.4: `𝔈_Θ := {c : ∃p, t, Γ, δ  Acc((c, p, t, Γ, δ)) ∧ Θ admits a carrier instantiating c}`; re-based on F4, not counted |
| 2 | minor | L13 still says a constructed correspondence is "produced by an episode of conjecture and criticism" | D12.2 asks no criticism (round 2 R1); FC84.new1 (a), the owner's bridge, is Con with none; L201 lost the same words (R3A1-T6, K2); L35: the front matter "states nothing the body does not state more exactly"; area 1 §10 saw it and left it | L13, delete: " and criticism" (kind delete). Other choice: leave, record as I168-style words-more-than-maths |
| 3 | minor | L61 "(Nec) their necessity" now ranges over `Account ∧ ¬Dec`, but L538's (Nec) exhibits the necessity of (E)'s conditions only | after R3A1-T1 "their" has the formula's two conjuncts as antecedent; L538 names no Dec | L61, delete: "their " (kind delete), so (Nec) names L538's condition; W-O1's "its" rightly refused (S40) |
| 4 | minor | CT8's T′ line: `held_trees = "o_trees" in occ` is a constant True (occ is the fixed list) and `k_t = prep and (held_out or held_trees)` | lesson S39; rerun shows `held_out` True in every reading, so the line rests on the computed Held already; the header still says "Sel as D12.1 has it after round 2" | `k_t = bool(prep) and held_out`; delete `held_trees`; header: "after round 3". Output unchanged; not a move |

Not objected, noted: FC30.new1 (a) keeps its `admitted=False` witness as a record beside (d), (e); the code keeps the checkers' provisional ids and B6's "I168" in comments (the addendum maps them); R3A3-T4's `o` at L405 is bound only by D13.3 (a pointer carries it; no prose may); I171 (H ≠ ∅) says more than L195's "a finite history" and stays in the register, not the text (rule 6 allows it; a next round may write it as a formula).

## 4. The owner question R3-Q1 (D6.3's quantifier, L255): fair

- The owner's words say nothing on it; L255 has no quantifier over the question's cases (checked).
- The text excludes W3 as written ('some' without the exemption): E1's own contract C2 fails NC1 under it (FC26 CEX, area 2 §3), against L325. The remaining choice, 'every' against 'some-exempt', is separated by no case the text states: the pole, the weathervane (Q15), M1–M3, FC-E1–E5, CT1–CT8 agree; M5, FC23.new1 (b), (d) and one encoding of E5 (FC62) differ, a second encoding of E5 does not (FC23.new1 (g)). So neither the texts nor a computation settles it.
- Both sides, each with an everyday example (shop sign; hand-turned vane), in plain words; L255 held (the apply program refuses changes there); the maths keeps side 1 meanwhile; Q15 untouched under both (FC22 rerun under some-exempt).
- Nothing else raised in round 3 is the owner's: H ≠ ∅ rests on Q2 as asked and L13; O6 has no clash; CT8's R4 residue is I90's reading of the run, not the theory's.

## 5. Moves (rule 16)

29 = 18 formal + 11 text, as the integrator counts. Checked: A1 F1 = A3 F1 counted once; FC77, FC104 re-based, not counted; 19 test claims, I167–I182, R3-Q1 not counted. Two borderline items, both counted: D0.2 (A3 F7), which round 2's second checker also counted ("D0.2 primitives classed", its table row of 9); D5.7's scope clause (A1 F11), the maths side of T5. Under any reading 27 ≤ moves ≤ 29 and rule 17 gives the same: the series continues.

## 6. Where I found nothing to object to

The tabulation; every N verdict I read against its reply (B4, B7, T5, T6, T8, T9, S-c, C-CT8a, K3, K5, N3, A2-T3, A2-T5, A2-T13, W4, W5, A3-L375.1–L626.1, W9, S-e-letters, O6 ×4); F1 (well founded, both areas, B3's witness right); F2/F3 (per holding; records carry provenance, L211); F4 (CT exact, L405); F5 (H ≠ ∅, Q2 and L13); F6/F7 (H, surv typed; Held with D12.5's extent, Rep ⇒ Held); F8 (obs ⊥, Q15's convention); F9 (covering relation); F10 (O_j as I124); F11/T5 (narrow Viol at L220); A3 F2 (Env), F3 (ExplUse through the claim, L403 and L526 both kept), F4 (δ_c), F5 (FC18 H under L554's reading), F6 (82-node graph, no cycle under K, T, T′), F7 (D0.2's list); area 2's four readings and its refusal of W3; the 11 text changes; the O-point rulings; the integration's merge and its 17 pairs.

## 7. For the orchestrator (rule 9)

The four objections are small enough to decide without a second checker: 1 and 4 are code and a re-based definition; 2 and 3 are one delete each, or a record if the words are preferred. Nothing here reopens a line, an answer, or the count.
