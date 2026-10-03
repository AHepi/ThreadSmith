# S104 Round 2 — the owner's answers written into the maths

*Opus 5.5, 28 September 2026. Decision S41 (Q2, Q6, Q15, Q23), written as maths and code (decision S40), then into a new copy of the text by permitted changes only. Terse by S40. The answers are the owner's; they are written, not weighed.*

Files: `S104 Round 2 - maths after the reading/` (formal core, formal claims .md/.json, inventions addendum, owner questions, the program `model after round 2/`); the new text `tests/104 The semantics, standing alone, after round 2, with the owner's answers.md`. tests/104 and every earlier text untouched.

## 1. The four answers

### Q2 — "No, not if just declared"

| where | old | new |
|---|---|---|
| D16.XV | Expl(ℰ): an atom, no definition uses it | the same, and Acc(ℰ) ∧ Dec(t) ⇒ ¬Expl(ℰ) |
| D16.XV (Suff) | L536: Acc ∧ ¬Dec(t) ∧ ∃α ∈ X_j(Expl(ℰ)), Acc ∉ Uses(α); L17 has no ¬Dec(t): Def(L536) ⊊ Def(L17) | L536 and L17: the same condition; Def(L17) = Def(L536) |
| (E), FC30 | takes no provenance | unchanged: ¬Dec(t) stands beside (E), not in it (note on FC30) |
| FC30.new1 | — | new: (a) the student's formula (pole's forward candidate, meets (E), declared transport, an argument not using (E) rules out Expl): in Def(L17 as text 104 words it), in neither Def(L536) nor Def(L17, S41); constructed or selected: in all three; (b) random candidates: Def(L17, S41) = Def(L536); (c) Expl := Acc ∧ ¬Dec meets (Suff) and the owner's condition |

Code: `model/claims_s41.py` (new): `suff_defeats` (three readings), `expl_ok` (the owner's condition), `expl_ruled_out` (an MP argument whose leaves do not mention Acc), provenance computed by `sel`, `con` on hand-made histories (I90). Run: FC30.new1 H (3 parts; (b) 17,280 models); FC30 H.

### Q6 — "Yes, it can"

| where | old | new |
|---|---|---|
| D13.8 | An episode is a subhistory (I131, "not applied either way") | Episode(h') :⟺ subhistory ∧ each change of contract in it (o ≺ o' immediately, q(o) ≠ q(o')) has a record of ρ_{q(o')} with its trace; no change need occur (I165); CompleteCritical(h') asks Episode(h') |
| D12.2 | Con: some episode h' of h up to e has CT(h', t) … | the same; the episode need hold no change of contract |
| D0.2 | — | q(o) and Rec_h' added to the primitives, read through Θ |
| FC84 | — | note |
| FC84.new1 | — | new: (a) the bridge to a fixed brief: one contract throughout, trace, cod t held: Con at o2 (one fixed point, T′), Build; under L55 as text 104 words it Con fails, Build holds; (b) a recorded change: episode, Con, both readings; (c) an unrecorded change: no episode across it; Con through {o2} under S41 only; (d) every chain ≤ 3 occurrences (8,456): Con(S41) ⊇ Con(L55's wording), differing exactly where no episode ending at the output holds a change and the target; Sel ∧ Con nowhere; one fixed point each |

Code: `model/claims_b.py`: `Hist` takes contracts and records; `episode` (readings "S41", "L55"), `chain_eps`; `_con_at` (Con over the episodes ending at o), used by `_prov_step` and `prov_fixed_points(…, eps)`; `con` checks an episode of h. With no contract data every sub-chain is an episode, so Con is as before. Runs: FC84.new1 H (4 parts); FC12.new1, FC78, FC81, FC82, FC83, FC84, FC98 unchanged.

### Q15 — "Yes, it can be explained"

| where | old | new |
|---|---|---|
| D6.4 Contrast | [both ≠ ⊥ ∧ differ] ∨ [Ans_E(x) = ⊥ ∧ Ans_E(x0) ≠ ⊥] (I21, I22) | Ans_E(x) ≠ Ans_E(x0) in Y_p ∪ {⊥}, ⊥ ≠ y, ⊥ = ⊥ (as D8.2): adds [Ans_E(x) ≠ ⊥ ∧ Ans_E(x0) = ⊥] |
| §6 Vague | "in the claimed way" not fixed [I22] | I22 settled; the phrase leaves L255 |
| FC22 | (a) the baseline alone gives no contrast | (a) kept, reworded for the one ≠; (b) new: M13 (the weathervane): ⊥ at the baseline, a value at the edit; NC2 under D6.4 as now, not under round 2's; E = D meets (E) |

Code: `model/core.py`: `contrast(…, reading)` symmetric (`CONTRAST_READING = "S41"`, "round2" kept); `NC2(…, reading)`. Runs: FC22 H (2 parts); FC21, FC23, FC29, FC34, FC37, FC62, FC63: status and parts unchanged (details in §2; FC23 (b): the same counterexample, ⊥ at both pairs).

### Q23 — "Yes, it's an argument"

| where | old | new |
|---|---|---|
| D9.2 | a finite tree of steps; (I88: an argument has a step) | α may be one leaf, a premise alone; concl(α) := the leaf's claim then |
| D9.6 | Usable_j(α) :⟺ every step usable | … and, for a premise alone d, d ∈ Accepted_j(ξ) (I166) |
| D9.7 | Incons(φ, concl(root of α)) | Incons(φ, concl(α)) |
| FC72 | (a)–(c) | (d) ¬PM ("perpetual motion is impossible") alone, accepted, rules out design ∧ PM; not an argument under round 2's I88; (e) the block holds: ¬PM alone does not rule out PM; (f) a premise alone not taken up is not usable |
| FC53, FC56, FC71 | — | notes: X_j now ranges over the premises alone too |

Code: `model/args.py`: `Leaf.concl`; `usable(j, Leaf)` = accepted (I166; `ARG_READING = "S41"`, "I88" kept); `enumerate_args` adds the premises alone after round 2's stepped arguments (those unchanged). `inventions_model.py`: I88's entry amended. Runs: FC72 H (4 parts); FC47, FC53, FC56, FC70, FC71, FC73 H, parts unchanged.

## 2. Result before and after

Whole suite, `PYTHONHASHSEED=0 python3 -B -m model.run --scale 4 --time-cap 45 --no-write --brief`, from `model after round 2/`:

| | H | CEX | NT | of | time |
|---|---|---|---|---|---|
| before (reproduced) | 103 | 3 | 7 | 113 | 378.4 s |
| after | **105** | 3 | 7 | **115** | 404.4 s |

CEX: FC18, FC23, FC63 (unchanged). NT: FC31, FC35, FC89, FC94, FC104, FC105, FC110 (unchanged). Every change, compared part by part (label, kind, status), then line by line:

| claim | status | parts | why |
|---|---|---|---|
| FC30.new1 | new: H | 3 | Q2 |
| FC84.new1 | new: H | 4 | Q6 |
| FC22 | H → H | 1 → 2 | Q15: (b) M13 |
| FC72 | H → H | 1 → 4 | Q23: (d)–(f) |

No other status, part label or part status changed. Details that changed, status kept:
- Q15 (more candidates meet NC2): FC21 (b) finds a different, smaller witness (model 236, was 241); FC34 (Acc not antitone) a different witness (5,559, was 5,737); FC29 hypothesis met 1,722 → 3,238; FC37 116 → 120.
- Q23 (the premises alone join the arguments): FC53 (b), FC56 (b) (6 → 8 arguments), FC71 (iii) (6 → 9): none rules out more; FC70 models tried 1,186 → 1,200 (no argument set is empty now); FC71 (i), (ii) hypothesis met 276 → 300 (premises alone in X_j(O) now also tested as α).

`s104_external.py` and `s104_creative_transport.py`: output byte-identical before and after.

## 3. The text

`text changes for the owner's answers.json` (5), applied by `apply text changes for the owner's answers.py` (new; input md5 checked, spans exact and unique, kinds delete/formal/pointer, overlaps refused, byte comparison and undo check, S95 and S96 scans, headings/terms/tags kept, prose must not grow; writes only the new file). Applied 5 on 4 lines, refused 0.

| id | line | kind | old → new | prose |
|---|---|---|---|---|
| S41-Q2 | L17 | formal | "that meets (E) on its question and contract" → "that meets \(\operatorname{Account}(\mathcal E)\land\neg\operatorname{Dec}(t)\) on its question and contract" | −1 |
| S41-Q6 | L55 | formal | "An episode is a history in which contracts change, and every change carries a provenance record." → "An episode is a history in which every change \(C\to C'\) carries a provenance record (D13.8)." | −2 |
| S41-Q15 | L255 | formal | "the answer of \(E\) at \((\tau(a),\sigma(b))\) differs from its answer at \((1,\sigma(b_0))\), or is not determined at \((\tau(a),\sigma(b))\) in the claimed way," → "\(\operatorname{Ans}_E(\tau(a),\sigma(b))\neq\operatorname{Ans}_E(1,\sigma(b_0))\) (D6.4)," | −18 |
| S41-Q23a | L397 | pointer | "An argument is an argument tree: argument steps whose leaves are premises," → "An argument is an argument tree (D9.2) whose leaves are premises," | −1 |
| S41-Q23b | L397 | pointer | "… when each of its steps is (K2)," → "… when each of its steps is (K2) (D9.6)," | +1 |

Words outside formulas: **15,409 → 15,388** (−21); all words 16,284 → 16,265. S95 scan: 0 new hits; S96: 0 new; headings 55, defined terms 154, labelled formulas 23: none missing.

## 4. md5, before → after

| file | before | after |
|---|---|---|
| formal core, after round 2.md | d8011c669603725937dc4cb36ff28177 | 96798d3bf3b60da8d67175c39462ef4a |
| formal claims, after round 2.md | bbebe5497dbf3f98eb9a69eb4dc93699 | 0306ff0a8d4727823864bb853e8dfde6 |
| formal claims, after round 2.json | 4638ded3c46b7c08f170f0d601f0b979 | 745cc40c12ff3ff0b4e48d7dafafee08 |
| inventions register - addendum after round 2.md | 00404849ca9b88cdd09934849445c724 | 507a0d56a4596f93a1118eaf3677c00a |
| owner questions after round 2.md | 684cb7c378110a3a32723d17297807c3 | 59fd4bd63a434bf90ae233dd67b93483 |
| text changes for the owner's answers.json | (new) | 8836b844ef122be01a6dc4a8bfb60c6a |
| apply text changes for the owner's answers.py | (new) | f833cb92e43ffbe98c31d311cfe990d7 |
| model after round 2/model/core.py | 6ea15cc0d6781700a528e17d244dab9b | 68c9a65a202c2f85365c5d7c4ef9bd47 |
| model after round 2/model/args.py | 10fff81e8bb77a114566275d7a95deda | 81ae45be0a7c5870c71bd5814448fd79 |
| model after round 2/model/claims_a.py | 62bb05be912fafed7b66659006c6f971 | cba30de265f14fd9f7ca726aabea53ff |
| model after round 2/model/claims_b.py | f788408a75b40553fe83d839ee371efe | 449920633217e8f497935e61cbfeadc3 |
| model after round 2/model/claims_s41.py | (new) | 1f07a6a2b7fd82f361e25057aa2f1a8c |
| model after round 2/model/run.py | b7c53ae0b24283666106899e83c476b0 | f3d491e3706d84d5488efb0bf9ea76a6 |
| model after round 2/model/inventions_model.py | dba0c346a84ed4f1996f17026d288f5a | eb410a1316b0b09da791ee2294cc7680 |
| tests/104 The semantics, standing alone, after round 2, with the owner's answers.md | (new) | bc14045aae3139df710d8339a9c1c81b |
| results/S104 Round 2 - the owner's answers written into the maths.md | (new; this file) | (not listed: it holds this table) |
| tests/104 The semantics, standing alone, after round 2.md (unchanged) | 735ec1e8256cc6a251715a031944ea65 | 735ec1e8256cc6a251715a031944ea65 |
| apply text changes.py (unchanged) | 6865929abb5487c11f85515d21a930a7 | 6865929abb5487c11f85515d21a930a7 |
| text changes after the review.json (unchanged) | 3f43745f9da7680eb85f60cef8b38172 | 3f43745f9da7680eb85f60cef8b38172 |

## 5. New inventions

- **I165** (Q6): the episode's record clause kept from L55: each change of contract, q(o) ≠ q(o') for o' immediately after o, has a record of ρ_{q(o')} with its trace; q(o) read through Θ; no change needed. Other: drop the clause too (I131 as registered).
- **I166** (Q23): a premise alone is usable by j exactly when j tentatively accepts it (Live with no step); no Form_j or Scope_j. Other: vacuous (everyone can use any premise alone).

Settled: I22 (Q15), I131 (Q6); I88's "an argument has a step" reversed (Q23). Q2 and Q15 needed no invention. Register: `inventions register - addendum after round 2.md`.

## 6. Conflicts found — questions for the orchestrator (nothing applied on these points)

Q2:
- L61: "(Suff) sufficiency of the four conditions of Account".
- S41 Q2: the four conditions are not enough where the link is only declared.

- L49: "A piece of mathematics explains, relative to a question, when its components respond to those edits as the target structure does".
- S41 Q2: not an explanation if its link was only declared.

- L69: "'Explanation' in this commitment means an account, an explanatory candidate meeting Account on its contract".
- S41 Q2: a candidate meeting (E) whose link was only declared is not an explanation.

Q23:
- L397: "What a stated premise cannot do is stand in for the steps."
- S41 Q23: a single claim used alone to decide this and not that is an argument.

- L397: "A premise taken as given differs from such a premise in that the argument has steps from it to what it rules out".
- S41 Q23: an argument may be a premise alone, with no step.

- S27: the bare claim "is not enough for a creative agent to do anything about it".
- S41 Q23: a single claim used alone to decide this and not that is an argument. (S28 says a ruling out by a claim taken as given "is a choice that was made".)

Q6, Q15: none found (L155, L197, L429, L544, L604–L608; L257, L273, L275, L315 checked).

## 7. Moves (strict)

As the second check counts: formal changes that write an answer, plus text changes applied; not counted: register entries (I165, I166), re-based statements (D9.7's concl(α), D12.2's note, D0.2's list, §6's Vague, the notes on FC30, FC53, FC56, FC71, FC84), new test claims and parts (FC30.new1, FC84.new1, FC22 (b), FC72 (d)–(f)).

| | | n |
|---|---|---|
| formal | D16.XV (Q2); D13.8 (Q6); D6.4 (Q15); D9.2, D9.6 (Q23) | 5 |
| text | S41-Q2, S41-Q6, S41-Q15, S41-Q23a, S41-Q23b | 5 |
| **moves** | | **10** |
