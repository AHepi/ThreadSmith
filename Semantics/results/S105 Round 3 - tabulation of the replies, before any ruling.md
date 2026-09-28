# S105: Round 3 — tabulation of the replies, before any ruling

*Written by the tabulating agent of rule 4 (a fresh Opus 5.5 agent that built nothing of this round and had read no reply when this file was created), 28 September 2026. Created at once, filled as it goes (lesson S28). Rules on nothing: "fails" says what a reply claims, not whether it holds. No theory text, rule, reply, decision or committed file of an earlier round was written. Obeys S23 except where it quotes.*

## 0. Counts per area (rule 5, lesson S36)

Counted by program from the tables of §3 before any checker starts.

| area | lines | findings | O-points among them | with a proposed change | S40 flags | S41 flags | ties decided by the tie rule (§1) |
|---|---|---|---|---|---|---|---|
| 1 | L1–L228 (Parts 0–IV) | **41** | 12 (O1–O3 ×4) | 29 | 5 | 0 | B7, B8, R4-L151, K2 |
| 2 | L229–L372 (Parts V–VIII) | **6** | 0 | 1 | 0 | 0 | — |
| 3 | L373–L632 (Parts IX–XVI) | **34** | 12 (O4–O6 ×4) | 19 | 1 | 0 | W7, S1, S-b |
| all | | **81** | 24 | 49 | 6 | 0 | 7 |

| job | findings | area 1 | area 2 | area 3 |
|---|---|---|---|---|
| 1 breaker | 18 | 14 | 0 | 4 |
| 2 maths_words | 29 | 9 | 6 | 14 |
| 3 structure | 21 | 9 | 0 | 12 |
| 4 cases | 13 | 9 | 0 | 4 |

No proposal would reverse or weaken an owner's answer (S41). Six text proposals add words outside formulas (S40): all four for O2, W-O1, W-O5. One point lies across areas: B3 [1] and S1 [3] (same fix, D11.3; §6).

## 1. How made

- Read first, whole: the rule (`results/S105 Round 3 - how the replies will be read, written before sending.md`); decisions S20–S41.
- Replies: the four `.response.txt` only (no receipt, reasoning, request, attempt, stream or guard file opened). All four end with END OF REPORT. Reply lines cited as r*n*.
- Text under review: `tests/104 The semantics, standing alone, after round 2, with the owner's answers.md`, md5 bc14045aae3139df710d8339a9c1c81b (checked), 632 lines.
- **Finding** = a point a reply says fails, departs (maths says more / less / other than the words), or proposes a change for; each O1–O6 answer is a finding. Points a reply marks held, same or clean are listed in §5, not counted.
- **Ids**: the reply's own (B*n*, W*n*, P*n*, K*n*, N*n*, table-row ids), prefixed where needed: B- breaker, W- maths_words, S- structure, C- cases.
- **Lines it bears on** (rule 5): the text lines the finding names (header, body or proposal); an owner's answer counts as its line in the briefs' table (Q2 L17, Q6 L55, Q15 L255, Q23 L397). **Maths alone** (no line named): the lines its definition formalizes, from the formal core's own citations or the Part: D3.3 L151; D4.6 L127; D6.3, D6.4 L255; D8.3 L315; D10.6 L317; D11.2 L169; D11.3 L375; D12.1 L195; D12.2 L197; D12.3 L199; D12.4 L211; D12.5 L205; D12.7 L217–L220; D13.3 L405; D13.8 L55; D14.7 L449; D16.XV L17, L536; D18.1 L526; D0.2 L31, L520–L522, L596. **Tie**: the area of the line of the definition the proposal changes (else the one attacked); every tie is marked. O1–O3 → area 1, O4–O6 → area 3 (rule 5). Area 1 L1–L228, area 2 L229–L372, area 3 L373–L632.
- **Form**: maths; code; or text: delete / formula (span replaced by its formal statement) / pointer; none.
- **S40 flag**: a text proposal whose new span has words outside formulas and pointers that the old span lacks (counted by program, §2). **S41 flag**: a proposal that would reverse or weaken Q2, Q6, Q15 or Q23.
- **Inventions**: I-numbers the finding rests on; "new I*nnn*" is the reader's own number (not assigned: rule 6 numbers them at integration; see §7).

## 2. Quotations and text proposals compared (rule 15)

**Text proposals** (old span searched in the cited line of the text under review; words outside `\(…\)` formulas and pointers counted, old → new; "new words" = words of the new span the old span lacks). By program (scratchpad `s105tab/prose.py`).

| id | line | kind | old span | words old → new | new words | S40 |
|---|---|---|---|---|---|---|
| B4 | L195 | pointer | found once | 14 → 14 (inside a formula) | — | — |
| B-O1, S-O1, C-O1 | L61 | formula | found once | 7 → 2 | — | — |
| W-O1 | L61 | formula | found once | 9 → 4 | its | FLAG |
| B-O2 | L49 | formula | found once | 12 → 8 | it meets on question and contract | FLAG |
| W-O2 | L49 | formula | found once | 21 → 17 | it meets on and contract | FLAG |
| S-O2 | L49 | formula | found once | 12 → 4 | holds of it | FLAG |
| C-O2 | L49 | formula | found once | 12 → 8 | it meets on question and contract | FLAG |
| B-O3, W-O3, C-O3 | L69 | formula | found once | 7 → 7 | — | — |
| S-O3 | L69 | formula | found once | 7 → 7 | — | — |
| B-O4, W-O4, S-O4, C-O4 | L397 | delete | found once | 12 → 0 | — | — |
| B-O5 | L397 | delete | found once | 13 → 0 | — | — |
| W-O5 | L397 | formula | found once | 33 → 28 | is not conjunct of | FLAG |
| S-O5 | L397 | pointer | found once | 23 → 0 | — | — |
| C-O5 | L397 | delete | found once | 33 → 0 | — | — |
| W2 | L220 | formula | found once | 7 → 4 | — | — |
| W9 | L556 | pointer | found once | 1 → 1 | — | — |
| S-P10 | L405 | formula | found (the text has `\(c\)`, the reply `c`) | 9 → 6 | — | — |
| S-P6 | L449 | formula | found (`\operatorname{Account}\big((c,p_c,t_c,\Gamma_c)\big)`); new span not given | — | — | not counted |
| C-P2 | L411 | delete | found once | 4 → 0 | — | — |
| C-P3 | L201 | pointer | found once | 25 → 0 | — | — |

**Quotations the findings rest on**

| quotation (as the reply gives it) | by | line cited | result |
|---|---|---|---|
| "exactly one"; "determined by its history" | B1, B3, C-CT8a | L193 | found L193 |
| "a carrier keeps its provenance" | B1 | L211 | found L211 ("A carrier …") |
| "a binding newly prepared is construction of that binding" | B1 | L405 | found L405 with words between ("A small binding newly prepared inside received content is …") |
| "Selection may continue to operate beneath construction" | B2 | L201 | found L201 |
| "entered into the model by its author" | B3 | L199 | **not in the text under review**; round-1 text (tests/103) L199, removed in round 2 (T10) |
| "a C containing edits to the observed value" ("the text's own words") | B7 | L151 | **not in the text under review**; "edits to the observed value" in tests/103 L151 |
| "several solutions several" | B6 | L105 | L105 reads "Several solutions remain several" |
| "a selected transport has no represented target in its history" | breaker r21 | L411 | found L411 ("A selected …") |
| "which does not say where the rival is in error" | B-O6 | L317 | found L317 |
| "no endless descent"; "Build depends on histories, Ownership and (E)"; "(K3) on (K2)" | S1, S2(iii), S3 | L526 | found L526 |
| "ruling the candidate out by χ is already doing something about it… a response that changes the candidate, the claim or the question is construction and repair" | S-O6 | L315 | found L315 (two fragments) |
| "the target's answer does not appear … as a component" | W3 | L255 | found L255 (fragments) |
| "offered as an answer to p in place of the other" | W4 | L315 | found L315 (fragments) |
| "while the argument stays usable" | W5 | L317 | found L317 |
| "enacted by the environment" | W6 | L481 | found L481 |
| "change the part and the reading follows"; "whose edits alter the observed L"; "reflexive closure"; "a step of the same argument"; "predict from occupancy" | T6, A2-T13, A3-L375.1, A3-L393.1, A3-L626.1 | L127, L325, L375, L393, L626 | cited as words round 2 dropped: not in the text under review; in tests/103 at L127, L325, L375, L393, L626 (L624 now has "predicting from occupancy") |
| "usable by j when each of its steps is (K2)" | B-Q23n | L397 | found L397 |
| "a transport whose provenance is not declared" | maths_words Q2 | L536 | found L536 |
| "specified independently" | maths_words D16.4 | L497 | found L497 |
| "a constructed one does"; "a constructed one has both" | K2 | L411; L201 | found |
| "so far as (F1), (F2) and (A) reach, the two candidates are one account" | K4 | L630 | found L630 |
| L161's "frozen-contract rule" | cases r50 | L161 | L161 "an event with a frozen contract" |
| "not enough to do anything about it" | C-O6 | S27 | S27 (decisions): "It is not enough for a creative agent to do anything about it though." |

## 3. Findings

### 3.1 Job 1, the breaker (`s105_glm_breaker`), 18 findings

Runs the reply reports (r1): `FC12.new1 FC83 FC98`, `FC84.new1 FC30.new1 FC22 FC72 FC28`, `FC77 FC84`, scale 4, cap 45: all "HOLDS ON ALL MODELS TRIED".

| id (r) | items | lines [area] | what fails, as claimed | model / computation; run? | proposal (§4) | form | inventions | S40 | S41 | area |
|---|---|---|---|---|---|---|---|---|---|---|
| B1 (r5–17) | D12.1–D12.3, I161, h(t) | L193, L211 [1]; L405 [3] | L193 "exactly one": t Sel at o1, re-prepared by a trace at o2 ≻ o1 → Sel (I128 reading) or Con (I53 reading) | `b1_two_readings` sketch, **not run**; FC12.new1, FC83 run, hold (case outside their space) | D12.2 beside the old: Con excludes an earlier Sel holding | maths | I161, I128, I53; new "I170" | — | — | 1 |
| B2 (r19) | D12.1/D12.2 CT, I56 | L201 [1] | "a construction trace prepares t": exact vs transitive; transitive blocks Sel beneath construction, against L201 | none (reading) | CT(h′,t) := a trace whose output is t | maths | I56, I161 | — | — | 1 |
| B3 (r25) | D11.3, D18.1, T′ | L193, L199 [1] | ≺_h acyclic only; an infinite chain below o_t: T′'s equations have **no** fixed point; no provenance; Dec wrong | proof by hand; not runnable (infinite) | D11.3: acyclic and well founded below every occurrence | maths | I162; new "I167" | — | — | 1 |
| B4 (r27) | L195 (T9), (R) L208, D18.1 | L195, L208 [1]; L526 [3] | L195 + L208 read alone = reading U: no fixed point for a selection; the staging is only in D18.1 | FC98 (c) printout, run: "none for a selection" | L195: add `\ (D18.1)` inside the formula | pointer | I162 | — | — | 1 |
| B5 (r29) | L195 (T9), D12.5, D11.2 | L195 [1] | Rep typed on contents; H and the survival condition are not contents | none (typing) | D11.2: a content may be H or a survival condition | maths | I52; new "I171" | — | — | 1 |
| B6 (r35) | D3.3, I163 | L151, L105 [1] | obs(a,b) undefined where g is not constant on Sol; image vs singleton readings differ; singleton excludes Q15-like questions | M13 / FC22 (b) run (g[Sol] = {0,1}); fix not run | obs := g[Sol]; Ident: ∃ pairs with obs ≠ obs′ | maths | I163; new "I168" | — | — (fix keeps the weathervane in) | 1 |
| B7 (r37–48) | D3.3, I163, FC28 | L151 [1]; L325 [2] | I163 unties Ident from the observed value's side: set(H=2), or any obs difference, makes Ident true | FC28 R4 part run; `FC28.new1` code **not run** (expect `True True True`) | FC28.new1 + register note (source of variation unconstrained) | code | I163 | — | — | 1 (tie 1:1 → D3.3, L151) |
| B8 (r52) | D16.XV, D12.1, D12.3, FC77, FC30.new1, Q2 | L17 [1]; L481 [3] | Dec hollow: FC77, any admitted Hom(τ) transport is Sel with H = ∅, so Acc ∧ Dec ⇒ ¬Expl misses the student's copy; FC30.new1's Dec witness is `admitted=False`; D16.XV says less than Q2 (no positive condition on Expl) | FC77 run 8,640/8,640; FC30.new1 run; fix not run | D12.1: add "survival condition enacted by the environment, a declared input" | maths | I158 ("the stated construction"); new "I169" | — | — (aims to make Q2 reach its own case) | 1 (tie 1:1 → D12.1, L195) |
| B9 (r54) | D13.8, I165, D11.3, D0.2, Q6 | L55 (Q6) [1] | "o′ immediately after o in h′" and q(o) undefined; benign for records | FC84.new1 run, holds | D13.8: covering relation; q(o) a function read through Θ | maths | I165; new "I172" | — | — (Chg = ∅ still allowed) | 1 |
| B-Q23n (r58) | D9.2, D9.6, I166, Q23 | L397 [3] | L397's "usable by j when each of its steps is (K2)" vacuous for a premise alone; premise-alone usability asks no Form_j, Scope_j | FC72 (d)–(f) run | none ("nothing to change") | none | I166 | — | — | 3 |
| B-e6 (r67) | D12.4 vs D12.1–D12.3 | maths alone: D12.4 L211 [1] | a record of a selected carrier: Dec on its own history, Sel by inheritance (predates round 2) | none | none | none | I54 | — | — | 1 |
| B-e7 (r68) | T9, I161, FC12.new1 | L195 [1] | T9 wrote I161's conjunct into L195: an invention made text (rule 6) | FC12.new1 part 3 witness (run) | none (see B1) | none | I161 | — | — | 1 |
| B-O1 (r76) | O1, Q2 | L61 | — | none | formula at L61 (rests on B8's fix) | formula | (I169, via B8) | — | — | 1 |
| B-O2 (r77) | O2, Q2 | L49 | — | none | formula at L49 | formula | — | **FLAG**: adds "it meets", "on … question and contract" | — | 1 |
| B-O3 (r78) | O3, Q2 | L69 | — | none | formula at L69 | formula | — | — | — | 1 |
| B-O4 (r79) | O4, Q23 | L397 | — | FC72 (e) cited | delete span | delete | — | — | — | 3 |
| B-O5 (r80) | O5, Q23 | L397 | — | FC72 (e) cited | delete span | delete | — | — | — | 3 |
| B-O6 (r81) | O6, S27, S28 | L317 cited | none: the orchestrator's reading holds; L317's clause ("which does not say where the rival is in error") carries S27's line; Out_j vs Repair/ProducedBy | none (reading) | no change | none | — | — | — | 3 |

### 3.2 Job 2, the maths against the words (`s105_glm_maths_words`), 29 findings

Runs the reply reports (r3): `FC30.new1 FC84.new1 FC22 FC72`, scale 4, cap 45: all "HOLDS ON ALL MODELS TRIED". Every other witness is cited from the build's printouts, not re-run by the reader. Rows of its tables with verdict "more", "less" or "other" are findings; the proposal cell is copied whole.

| id (r) | items | lines [area] | what fails, as claimed | model / computation; run? | proposal (whole, or §4) | form | inventions | S40 | S41 | area |
|---|---|---|---|---|---|---|---|---|---|---|
| T5 (r12) | T5, FC13 | L127 [1] | more: two components, identical sig on C, one Causal, one not (Set_v/Obs read A beyond C) | FC13 printout | "maths stands (already written); I04, I06, I08" | none | I04, I06, I08 | — | — | 1 |
| T6 (r13) | T6, FC08 | L127, L124 [1] | less: drops "change the part and the reading follows" (round-1 words) | FC08 printout, H | "maths stands ((K) cannot record it); I07" | none | I07 | — | — | 1 |
| T8 (r15) | T8 | L151 [1] | other: words categorical about answers, formula existential about accounts; Q′ extensionally equal to Q | none | "none; I73 records both readings; the text need not settle it" | none | I73 | — | — | 1 |
| R4-L151 (r16) | R4, D3.3, C_id | L151 [1]; L325 [2] | more: C_id = {1}×B, no edit alters observed L, yet pairs with obs ≠ obs′ | FC28 printout | "maths stands (E1/L325 needs C_id; already written); I163" | none | I163 | — | — | 1 (tie 1:1 → D3.3, L151) |
| T9 (r17) | T9, D12.1 | L195, L193 [1] | more: (i) adds cod t; (ii) adds ¬CT | none | "maths stands (R1–R3); I161, I162" | none | I161, I162 | — | — | 1 |
| A2-T3 (r21) | NC, D6.9, FC21 | L257 [2] | less: NC weakened to (F2)∧(A)∧NC; old words false in the maths | FC21 (b)/(d) printout, H | "maths stands (FC21 H); I26" | none | I26 | — | — | 2 |
| A2-T5 (r23) | D6.10, FC25 | L269 [2] | less: conditionalized; an intervention disjoint from λ(k) changes no projection | FC25 (a*) printout, H | "maths stands; I32" | none | I32 | — | — | 2 |
| A2-T13 (r31) | E1, C_id | L325 [2] | less: drops "whose edits alter the observed L", false of C_id | none | "maths stands; I65" | none | I65 | — | — | 2 |
| A3-L375.1 (r32, r87) | D11.3 | L375 [3] | other: reflexive closure → ≺_h*: o1 ≺ o2 ≺ o3, ¬o1 ≺ o3: words o1 ⋠ o3, formula o1 ⪯ o3 | none | "maths stands (I44 (b)); already written" | none | I44 | — | — | 3 |
| A3-L393.1 (r33) | D9.4 Below | L393 [3] | other: sibling step; words two fixed points of (K2), formula one | FC69 printout | "maths stands; I40" | none | I40 | — | — | 3 |
| A3-L393.2 (r34) | monotonicity X^{ξ′} ⊆ X^ξ | L393 [3] | more: adds monotonicity; no case separates | FC70, FC56 (c) printouts, H | "none" | none | — | — | — | 3 |
| A3-L395.1 (r35) | test ruling out | L395 [3] | less: α with ¬(T∧B∧I) among a leaf's conjuncts: words rule out, formula blocks | FC71 (i′) printout, H | "maths stands; I43" | none | I43 | — | — | 3 |
| W9 = A3-L556.1 (r42, r108, r134) | (K), D4.1, D4.4 | L556 [3] | other: the pointer lets "(K)" name D4.4 | none | pointer at L556 | pointer | — | — | — | 3 |
| W8 = A3-L558.1 (r43, r108, r132) | FC18, D4.4, I94 | L558 [3] | other: L558 cites FC18, whose status is CEX (I94 reading); L558's statement holds on 17,280 models | printout; restated claim **not run** | FC18 restated; I94 reading to a remark | maths | I94, I10 | — | — | 3 |
| A3-L574.1 (r44) | FC80 | L574 [3] | other: τ×σ non-injective on H: old proof over-claims | FC80 (d) printout, H | "maths stands (FC80 (d), H)" | none | — | — | — | 3 |
| A3-L590.1 (r46) | E8, FC97 | L590 [3] | more: adds the query port | FC97 printout, H | "maths stands (FC97 H); I67" | none | I67 | — | — | 3 |
| A3-L626.1 (r47) | E9, FC102 (b″) | L626 [3] | more: adds w ≤ L_occ | FC102 (b″) printout | "maths stands; I68, I100 — the text leaves "predict from occupancy" open" | none | I68, I100 | — | — | 3 |
| W1/W2 (r106, r126) | D12.7, D5.7, FC104 | L220, L189 [1] | Viol narrow vs wide extent of "faithful": t meeting F1, F2eq at (a,b) but failing (A) | witness described, not run | formula at L220 (settles FC104's open extent) | formula | FC104 extent (rule 6: settles it) | — | — | 1 |
| W3 (r76, r128) | D6.3, I136 | L255 [2] | other: ∀ lets a partial lookup (pins the answer at one pair of Det_C only) pass NC1; L255 condemns it | FC23, FC26, FC63 re-run proposed, **not run** | D6.3 ∀ → ∃ | maths (+ code re-run) | I136, taken the other way | — | — (not shown; FC22 (b), Q15's case, not in its re-run list) | 2 |
| W4 (r79, r130) | D8.3, I33 | L315 [2] | more: Off(ℰ,p) ∧ Off(ℰ′,p): ℰ′ offered only for p″, words rivals, maths not | none | none ("the text need not settle it") | none | I33 | — | — | 2 |
| W5 (r86, r136) | D10.6, I141 | L317 [2] | less: "while the argument stays usable" is time outside the model | none | none (record only) | none | I141 | — | — | 2 |
| W6 (r89, r136) | D12.1 (survival condition) | L481 [3] | other: condition fixed to fidelity alone; "fidelity on H and length < 5": words not survived, maths Sel | none | none (record only) | none | survival condition (unnumbered) | — | — | 3 |
| W7 (r93, r136) | D13.3, I146, I162 | L205 [1]; L405 [3] | other: "represented organization" read as Held, not Rep; the Rep reading fails Build at a first construction | FC98 (d) printout | "the maths stands" | none | I146, I162 | — | — | 3 (tie 1:1 → D13.3, L405) |
| W-O1 (r114) | O1, Q2 | L61 | — | none | formula at L61 | formula | — | **FLAG**: "(Nec) their" → "(Nec) its" (a word outside formulas) | — | 1 |
| W-O2 (r116) | O2, Q2 | L49 | — | none | formula at L49; "(Part VII)" → "(Part V)" | formula | — | **FLAG**: adds "it meets", "on … and contract" | — | 1 |
| W-O3 (r118) | O3, Q2 | L69 | — | none | formula at L69 | formula | — | — | — | 1 |
| W-O4 (r120) | O4, Q23 | L397 | — | none | delete span | delete | — | — | — | 3 |
| W-O5 (r122) | O5, Q23 | L397 | — | none | "the argument has steps from it to what it rules out" → "\(\neg\varphi\) is not a conjunct of it (D9.7)" | formula | — | **FLAG**: adds "is not a conjunct of" | — | 3 |
| W-O6 (r124) | O6, S27, S28 | L315 cited | none; but against the orchestrator's reading: S28's "yes" says plainly that ruling out is already doing something; no reading denying it should be written | FC72 (f) run | no change | none | — | — | — | 3 |

### 3.3 Job 3, the structure of the formal core (`s105_glm_structure`), 21 findings

Runs the reply reports (r24): `--claim FC98 --claim FC32`, both hold. Everything else by reading (code lines cited: claims_b.py:2485, :1638; core.py:312–320; args.py:62–91, 266–276).

| id (r) | items | lines [area] | what fails, as claimed | model / computation; run? | proposal (§4) | form | inventions | S40 | S41 | area |
|---|---|---|---|---|---|---|---|---|---|---|
| S1 (r24, r92) | D11.3, D18.1, T′, Dec, Q2 | L17 [1]; L526 [3] | cut loop well founded only on well-founded histories; infinite descending chain: **two** incomparable fixed points ({o_1}, {o_2}), no least; Rep, Sel, Con, Dec and L17's Def vary; L526's "no endless descent" fails | FC98, FC32 run, hold; witness not run (infinite) | P1: D11.3 acyclic and well founded | maths | I162; new "I167" | — | — | 3 (tie 1:1 → D11.3, L375) |
| S-fQ2 (r85) | D16.XV, Dec, Q2 | L17 (Q2) [1] | Q2's defeat condition sits inside S1's non-uniqueness: Dec(t) fixed-point dependent on an infinite history | FC30.new1 (H) cited | none (P1) | none | I162 | — | — (Q2 untouched) | 1 |
| S2(i) (r26) | D18.1, DEP, FC98 (b) | L526 [3] | DEP has 28 nodes of the 118 announced; (S), (B), (D), (K3), Result, Episode, Scr, RC, UU, UC absent; FC98 (b)'s sink check sees a subgraph | reading | P7 | code, **not run** | — | — | — | 3 |
| S2(ii) (r26) | DEP["Sel"], D12.1 | L526 [3] | DEP["Sel"] omits Faithful_H (→ (F1), (F2)) and ¬CT (→ Build); no cycle hidden | reading | P7 | code, **not run** | I161 | — | — | 3 |
| S2(iii) (r26) | DEP["Build"], D13.3, ExplUse (D0.2) | L526 [3] | L526 "Build depends on … (E)" has no definition behind it: ExplUse is a primitive | reading | P5: define ExplUse via Acc; remove from D0.2 | maths | I148; new "Inn" | — | — | 3 |
| S3 (r28) | D18.1, D9.9 | L526 [3] | L526 "(K3) on (K2)": no (K3) node | reading | P7 (same subgraph point as S2(i)) | code, **not run** | — | — | — | 3 |
| S-b (r30–49) | D0.2; 12 symbols (𝒱, parts(t), surv, h(t)/o_t, cod t, val_r…, trans/ρ·ob/γ·ob, Exec…, Desc, "immediately after", "output of h′", 𝔓^adv_Θ) | L31 [1]; L522 [3] | used, never defined, not listed | reading | P7 makes the sinks visible; rows "should be added to D0.2 or defined" (P3, P4 for surv, cod t, "immediately after") | code / maths | I158, I165, NF12 | — | — | 3 (tie 1:1 → D0.2: L520–L522, L596) |
| S-c (r53) | D2.5, Found(p), D7.4, D10.3, D10.6, D12.6, D14.8, D15.4, D15.6, D16.1 | L109, L155, L175, L177, L179 [1]; L302, L317 [2]; L455, L473, L487, L495 [3] | no claim and no model code uses them; "none is idle" | reading | "No proposal; note only that D10.3 and FC47 should point at each other" | none | — | — | — | 1 (5:2:4) |
| S-D1 (r57) | D4.6, D2.1, I124, core.py:312–320 | maths alone: D4.6 L127 [1] | D4.6 "the port j assigns" singular; I124 and the program take a union: V_k = {v,w} → D4.6's o_k has no value, the program computes Causal(k) | witness **not run**; P8 code **not run** | P2 (D4.6 as a set O_j), P8 (the case) | maths + code | I124 | — | — | 1 |
| S-D2 (r59) | D12.5, D12.1, D18.1 Held, D12.2 | maths alone: D12.1 L195, D12.2 L197 [1] | Rep and Held applied outside their type (t, H, surv; Held names no contract) | reading | P3: Held on x ∈ {t, cod t}; H, surv via record leaves | maths | I162 (Held); cf. I52 | — | — | 1 |
| S-e-letters (r63–76) | δ, B, G, K, κ, O, S/P, T, q, CT, π/C, Pred/Ans | L395 [3] | one letter, two or three uses; K collides inside DEP | reading | "I propose only the δ and K renamings, as inventions of notation": **not given in (g)** | none given | notation (unnumbered) | — | — | 3 |
| S-e-represented (r77, r110) | Rep (D12.5, D13.1), Held (D18.1, D12.2, D13.3), D11.4, D13.8 | L405 [3] | "represented" names Rep, Held, or neither | reading | P10: formula at L405 (Held) | formula | I162 (writes T′'s Held into L405: rule 6) | — | — | 3 |
| S-e-primed (r78, r108) | FC07, FC36, FC77, FC81–FC83; D2.4′, D3.3′, D4.6′, D12.1′, D12.7′, D12.8′ | maths alone: L109, L127, L151, L195, L217–L220 [1] | claims cite primed ids that no longer exist | reading | P9 (the reply's (e) calls it "P11") | maths (editorial) | — | — | — | 1 |
| S-e-Acc (r79, r102) | D6.7, D14.7, D9.10 | L449 [3] | Acc arity: D6.7 eleven arguments, D14.7 four, no δ_c: (EX) evaluates a query with no designation | reading | P6: D14.7 with δ_c; "Same change at L449 by its formal statement" (new span not given) | maths + formula | — | — | — | 3 |
| S-fQ6 (r86, r98) | D13.8, I165, Q6 | L55 (Q6) [1] | "o′ immediately after o in h′" undefined; the program does adjacency on chains only | reading | P4: every o, o′ ∈ h′ with q(o) ≠ q(o′) | maths | I165 (amended) | — | — (Chg = ∅ still allowed) | 1 |
| S-O1 (r114) | O1, Q2 | L61 | — | none | formula at L61 | formula | — | — | — | 1 |
| S-O2 (r115) | O2, Q2 | L49 | — | none | formula at L49 | formula | — | **FLAG**: adds "holds of it" | — | 1 |
| S-O3 (r116) | O3, Q2 | L69 | — | none | formula at L69 | formula | — | — | — | 1 |
| S-O4 (r117) | O4, Q23 | L397 | — | none | delete span | delete | — | — | — | 3 |
| S-O5 (r118) | O5, Q23 | L397 | — | none | span → "(D9.2)" | pointer | — | — | — | 3 |
| S-O6 (r119) | O6, S27 | L315 cited | none: ruling out (D9.6–D9.8) and response (D12.8, D14.2) share no definition; L315 writes the separation | reading | no change | none | — | — | — | 3 |

### 3.4 Job 4, the cases (`s105_glm_cases`), 13 findings

Runs the reply reports (r3): `FC30.new1 FC84.new1 FC22 FC72`, scale 3, cap 30: all hold. CT and FC-E results from the printouts. New cases N1–N6 all **not run**.

| id (r) | items | lines [area] | what fails, as claimed | model / computation; run? | proposal (§4) | form | inventions | S40 | S41 | area |
|---|---|---|---|---|---|---|---|---|---|---|
| C-CT8a (r40–43) | CT8 R3–R5, D12.1, I161 | L193, L195, L199, L13 [1] | the brief's "one reading moved" is two (R4 by D12.1's represented-codomain ban, R5 by I161); residue: "neither" = Dec by exclusion over a history that computed the pair (C01, "known, left") | CT8 printout | none | none | I161; C01 | — | — | 1 |
| K1 (r44, r113–119) | CT8 R5, D12.2, T′, I90 | maths alone: D12.2 L197 [1] | CT8 computes Con from (R)-tags (`con(h)` reads `h.rep`); under T′ (Held) R5 is constructed; the printed "neither" is an artefact | printout; P1 code **not run** (expect R5 "constructed") | P1: a T′ line in the CT8 block | code | I162, I90 | — | — | 1 |
| K2 (r45, N2 r68–75, r121, r123) | D12.2, T′, CT8 R1/R3/R5 | L197, L201 [1]; L405, L411 [3] | constructed histories with no criticism and (under T′) no represented target: L411 "a constructed one does", L201 "has both" say otherwise | N2 code **not run** (expect `[{'o2': 'Con'}]`) | P2: delete at L411; P3: L201 sentence → pointer | delete + pointer | I161, I162; C02, NF07 | — | — | 1 (tie 2:2 → D12.2, L197) |
| K3 (r49, r125) | Q2, D16.XV, D12.4, I118 | L17 (Q2), L211 [1] | the student's example is a copy: per part (D12.4, L211) the content parts are Con, Dec(t) fails and Expl is not blocked, against the answer; the reading D16.XV needs is not registered | FC30.new1 (a) run; per-part variant not run | P4: Dec read on t as one transport | maths | I118; new "I167" | — | — (chooses the reading under which Q2's answer stands) | 1 |
| K4 (r22, r127) | E9, FC102 (a),(c), FC103 (a)–(c), FC33, FC96 (ii), FC51 (b) | L620–L630 (L626, L628, L630) [3] | E9's simulation layer S0, S1 not built; five parts NOT TESTED; the swap conclusion and t0's surprise carried only by other claims | P5 code **not run** | P5: build S0, S1 | code | — | — | — | 3 |
| K5 (N1 r57–66) | I161, Sel | L193, L195 [1] | Dec now covers a history meeting every other condition of Selected; rests wholly on I161; the owner's words nowhere ask for ¬CT | N1 code **not run** (expect `False False` / `True`) | none | none | I161 | — | — | 1 |
| N3 (r77–88) | I163, D3.3 | L151 [1] | none claimed ("maths and text agree"); a contract setting the observed value but leaving it constant: Ident False under I163, True under the round-1 wording | code **not run** | none | none | I163 | — | — | 1 |
| C-O1 (r131) | O1, Q2 | L61 | — | none | formula at L61 | formula | — | — | — | 1 |
| C-O2 (r132) | O2, Q2 | L49 | — | none | formula at L49; old span stops before "(Part VII)", which would stay after the new "(D16.XV)" | formula | — | **FLAG**: adds "it meets", "on … question and contract" | — | 1 |
| C-O3 (r133) | O3, Q2 | L69 | — | none | formula at L69 | formula | — | — | — | 1 |
| C-O4 (r134) | O4, Q23 | L397 | — | none | delete span | delete | — | — | — | 3 |
| C-O5 (r135) | O5, Q23 | L397 | — | none | delete the whole sentence | delete | — | — | — | 3 |
| C-O6 (r136) | O6, S27, S28 | — | none: ruling out stays a choice via Accepted_j (S28); no definition of §§12–14 lets a bare premise build, respond or repair | FC72 (d)–(f) run | no change | none | I166 | — | — | 3 |

## 4. Proposals whole

Copied by program from the `.response.txt` files, byte for byte (a breaker line is cut to start at its "**Fix"). Heading: finding id, reply lines.

### `s105_glm_breaker`

**B1** (r17)
~~~~
**Fix (maths)**: D12.2, beside the old — `Con(t;h,e) :⟺ some episode h′ of h up to e has CT(h′,t) ∧ Held_ℓ(o′,x) for some o′ ⪯ o_t of h′, x ∈ {t, cod t} ∧ ¬∃o″ ≺_h o_t holding t with Sel(t;·) [I170; other choice: provenance re-read on the whole history at each holding (L193 read whole)]`. Restores "exactly one" under both readings of h(t).
~~~~

**B2** (r19)
~~~~
**Fix (maths)**: D12.2, `CT(h′,t) :⟺ h′ has a construction trace (D13.3) whose output is t [I56 read exactly; other choice: transitively through contents built from the trace's output — contradicts L201]`.
~~~~

**B3** (r25)
~~~~
**Fix (maths)**: D11.3, beside the old — `≺_h acyclic and well founded below every occurrence [I167; other choices: acyclic only (round 2 — B3), well founded on all of O_h]`.
~~~~

**B4** (r27)
~~~~
**Fix (text, pointer)**: L195, old `x\in\{t,\ H,\ \text{survival condition},\ \operatorname{cod}t\}:\ \operatorname{Rep}(o,x)]` → new `x\in\{t,\ H,\ \text{survival condition},\ \operatorname{cod}t\}:\ \operatorname{Rep}(o,x)\ (D18.1)]`.
~~~~

**B5** (r29)
~~~~
**Fix (maths)**: D11.2, add `a content may also be a finite H ⊆ C or a survival condition, each read through Θ as an organization (E8's construction) [I171; other choice: D12.1's exclusion ranges over t and cod t only]`.
~~~~

**B6** (r35)
~~~~
**Fix (maths)**: D3.3, beside the old — `obs(a,b) := g[\operatorname{Sol}_D(a,b)]; Ident(p) :⟺ Q returns a fibre ∧ ∃(a,b),(a′,b′) ∈ C: obs(a,b) ≠ obs(a′,b′) [I168; other choice: |g[Sol]| = 1 asked at both pairs]`. On the pole (singletons throughout) Ident is unchanged; FC28 (R4) stays H.
~~~~

**B7** (r37–r48)
~~~~
**Fix (code, not run)**:

```python
# FC28.new1 (not run), in cases.py notation: Ident under D3.3 on the pole's contracts
D = pole(); b0 = "b1_45"
for C, why in [({(ONE,b0)} | {(ONE,b) for b in D.B}, "C_id: boundaries only"),
               (frozenset([(ONE,b0)] + [(a,b0) for a in single_settings(D,["H"])]), "settings of H"),
               (frozenset([(ONE,b0)] + [(a,b0) for a in single_settings(D,["L"])]), "settings of L")]:
    print(why, ident_question(D, C))   # expect: True, True, True under I163;
    # under L151's words ("edits to the observed value"): no / yes-by-reading / yes
```
Expected output: `True True True`. Register with I163: the source of variation is unconstrained (other choices: only boundaries; only edits altering obs).
~~~~

**B8** (r52)
~~~~
**Fix (maths)**: D12.1, add a conjunct — `and the survival condition is one the environment enacts (D15.8, L481), a declared input [I169; other choices: keep FC77's trivial witness (Dec then nearly empty, B8); require H ≠ ∅]`. FC77's verdict flips to the intended "nothing is selected by empty parameters"; FC30.new1 (a) then reaches the student's case. D16.XV also says less than the answer (no positive condition on Expl) — carried by the O3 fix below.
~~~~

**B9** (r54)
~~~~
**Fix (maths)**: D13.8, add `o′ immediately after o in h′ :⟺ o ≺_{h′} o′ ∧ ¬∃o″ ∈ h′: o ≺ o″ ≺ o′; q(o) a function read through Θ [I172; other choices as above]`.
~~~~

**B-O1** (r76)
~~~~
- **O1 (L61)**: text, formal — old `(Suff) sufficiency of the four conditions of Account` → new `(Suff) sufficiency of \(\operatorname{Account}(\mathcal E)\land\neg\operatorname{Dec}(t)\) (D16.XV)`. (Rests on B8's fix for Dec to carry weight.)
~~~~

**B-O2** (r77)
~~~~
- **O2 (L49)**: text, formal — old `when its components respond to those edits as the target structure does (Part VII)` → new `when it meets \(\operatorname{Account}(\mathcal E)\land\neg\operatorname{Dec}(t)\) on its question and contract (Part VII, D16.XV)`.
~~~~

**B-O3** (r78)
~~~~
- **O3 (L69)**: text, formal — old `an explanatory candidate meeting \(\operatorname{Account}\) on its contract` → new `an explanatory candidate meeting \(\operatorname{Account}(\mathcal E)\land\neg\operatorname{Dec}(t)\) on its contract (D16.XV)`.
~~~~

**B-O4** (r79)
~~~~
- **O4 (L397)**: text, delete — old `What a stated premise cannot do is stand in for the steps. ` (delete the span). A premise alone is an argument (D9.2, S41-Q23); the circularity block that follows is unaffected (FC72 (e)).
~~~~

**B-O5** (r80)
~~~~
- **O5 (L397)**: text, delete — old ` in that the argument has steps from it to what it rules out` (delete the span), leaving `A premise taken as given differs from such a premise: it finds that the candidate gives what the premise excludes.` The residual difference is the structural block, which holds of premises alone (FC72 (e)).
~~~~

**B-O6** (r81)
~~~~
- **O6**: no change needed. The orchestrator's reading holds and the material already carries it: L317's own clause — the ruling out "is already something done about the conflict with the claim, **which does not say where the rival is in error**" — is the distinction S27 draws (enough to trigger and to rule out, not enough to repair); the maths keeps them apart (Out_j, D9.8, vs Repair/ProducedBy, D14.2–D14.3), the choice shows as Accepted_j (S28), and D10.6's "solved" claims no repair. S27 and S28 are the owner's words and are not touched.
~~~~

### `s105_glm_maths_words`

**W-O1** (r114)
~~~~
**W-O1 (text, formal, L61).** old: `(Suff) sufficiency of the four conditions of Account; (Nec) their necessity;` → new: `(Suff) sufficiency of \(\operatorname{Account}(\mathcal E)\land\neg\operatorname{Dec}(t)\) (D16.XV); (Nec) its necessity;`
~~~~

**W-O2** (r116)
~~~~
**W-O2 (text, formal, L49).** old: `A piece of mathematics explains, relative to a question, when its components respond to those edits as the target structure does (Part VII).` → new: `A piece of mathematics explains, relative to a question, when it meets \(\operatorname{Account}(\mathcal E)\land\neg\operatorname{Dec}(t)\) on its question and contract (Part V).`
~~~~

**W-O3** (r118)
~~~~
**W-O3 (text, formal, L69).** old: `an explanatory candidate meeting \(\operatorname{Account}\) on its contract` → new: `an explanatory candidate meeting \(\operatorname{Account}(\mathcal E)\land\neg\operatorname{Dec}(t)\) on its contract`
~~~~

**W-O4** (r120)
~~~~
**W-O4 (text, delete, L397).** delete: `What a stated premise cannot do is stand in for the steps. ` (the block it introduced is D9.7's, stated in the next sentence).
~~~~

**W-O5** (r122)
~~~~
**W-O5 (text, formal, L397).** old: `A premise taken as given differs from such a premise in that the argument has steps from it to what it rules out: it finds that the candidate gives what the premise excludes.` → new: `A premise taken as given differs from such a premise in that \(\neg\varphi\) is not a conjunct of it (D9.7): it finds that the candidate gives what the premise excludes.`
~~~~

**W-O6** (r124)
~~~~
**W-O6.** No change. The maths already keeps the two apart: the claim alone (not taken up) rules nothing out and does nothing (FC72 (f), run), the conflict is ConfCl (D8.5), and the ruling out is Out_j, which turns on Accepted_j, a declared input no definition sets — the person's choice (S28). L315 says the same. Against the orchestrator's reading as recorded: S28's "yes" answers "is ruling out … already doing something about it" plainly, so no reading that denies it should be written in; none is needed.
~~~~

**W1/W2** (r126)
~~~~
**W2 (text, formal, L220).** old: `a **violation** occurs when fidelity fails at \((a,b)\);` → new: `a **violation** occurs when \(\neg(\text{F1 at }(a,b)\land\text{F2eq at }(a,b))\) (D12.7);` — settles FC104's open extent in the reading L189 defines.
~~~~

**W3** (r128)
~~~~
**W3 (maths, D6.3; invention I136 taken the other way).** Beside the current form, replace `∀(a,b) ∈ Det_C: {w_δE : w ∈ L^E_k(τ(a),σ(b))} = {Ans_p(a,b)}` by `∃(a,b) ∈ Det_C: {w_δE : w ∈ L^E_k(τ(a),σ(b))} = {Ans_p(a,b)}`. Companion code: re-run FC23, FC26, FC63. Expected: FC23 (d) — M5's partial slot fails NC1 (computed, no longer "a look"); FC26, FC63 unchanged (the pole's c_L projects onto the full domain X_L, never a slot; the Leibniz candidate likewise). Not run. The words should stand: L255 condemns the answer appearing as a component anywhere on C; the ∀ reading lets a partial lookup through. Other choice: keep ∀ and record that the words over-reach.
~~~~

**W4** (r130)
~~~~
**W4 (no proposal).** D8.3's Off-clauses rest on I33; the words' "offered as an answer to p in place of the other" can be read either way; the text need not settle it.
~~~~

**W8** (r132)
~~~~
**W8 (maths, FC18 restated).** FC18: `SameKind_C(ℰ) := … coincide under a footprint bijection (I10, D4.4's reading). Claim: F1_C(ℰ) ⇒ SameKind_C(ℰ)…` — move the I94 untranslated reading to a remark ("a look"), so the claim's status (H) matches what L558 asserts. Not run (status unchanged for the part L558 uses).
~~~~

**W9** (r134)
~~~~
**W9 (text, pointer, L556).** old: `By (K) (D4.4),` → new: `By (K) (D4.1, D4.4),`
~~~~

**W5, W6, W7** (r136)
~~~~
**W5, W6, W7 (no proposal).** W5 (I141) and W6 (the survival condition) are inventions the text leaves open — record only. W7 is the ruled cut T′ (Q1, I146/I162); the alternative was computed and rejected (FC98 (d)); the maths stands.
~~~~

### `s105_glm_structure`

**S1: P1** (r92)
~~~~
**P1 (maths).** D11.3, beside: "≺_h acyclic" → "≺_h acyclic **and well founded** [I167; other choices: the least fixed point of the staged recursion — none exists in general, see S1's witness; the greatest — admits Rep everywhere]. L526's 'no endless descent' asks for this." No text change; invention registered.
~~~~

**S-D1: P2** (r94)
~~~~
**P2 (maths).** D4.6: "o_j is the port j assigns (asg(o_j) = j)" → "O_j := {v : asg(v) = j} [I124], Set_{O_j} := ∪_{v∈O_j} Set_v; Causal_C(j) :⟺ Changes_C(j, Set_{O_j}) ∧ Inv_C(j, Obs)". Matches the program as it stands.
~~~~

**S-D2: P3** (r96)
~~~~
**P3 (maths).** D18.1/D12.1: "Held_ℓ(o, x) :⟺ ∃t′ Faithful(t′: Org_ℓ(o) → cod x) on the preimage of C_{cod x} (D12.5's extent), for x ∈ {t, cod t}, with (C_{cod x}, Γ_{cod x}) declared with t; D12.1's exclusion ranges over x ∈ {t, cod t}, and 'no member of the history represents H or the survival condition' := no record leaf of h(t) is MadeFrom H or surv (D9.2)."
~~~~

**S-fQ6: P4** (r98)
~~~~
**P4 (maths).** D13.8: "for every o ≺_{h′} o′, o′ immediately after o in h′, with q(o) ≠ q(o′)" → "for every o, o′ ∈ h′ with q(o) ≠ q(o′)" (extensionally equal wherever immediacy is defined; removes the undefined symbol). No new invention: an amendment to I165.
~~~~

**S2(iii): P5** (r100)
~~~~
**P5 (maths).** D0.2/D13.3: remove ExplUse from D0.2 and add to D13.3: "ExplUse(o, c) :⟺ the occurrence's use is of a claim Acc((E_c, p_c, t_c, Γ_c, δ_c)) [Inn; other choices: keep ExplUse a primitive and drop (E) from Build's edges and from L526 by a text change]". This is what makes L526's "Build depends on … (E)" true.
~~~~

**S-e-Acc: P6** (r102)
~~~~
**P6 (maths).** D14.7: "Acc(c, p_c, t_c, Γ_c)" → "Acc((E_c, p_c, t_c, Γ_c, δ_c)), δ_c supplied with c (as D9.10 supplies δ_c)". Same change at L449 by its formal statement.
~~~~

**S2(i), S2(ii), S3, S-b: P7** (r104)
~~~~
**P7 (code, not run).** Extend `DEP` (claims_b.py:2485) with the missing nodes — (S),(B),(D),(K3),Result,Episode(+q,Rec),Scr,RC,UU,UC — and the missing edges "Sel": […, "(F1)", "(F2)", "Build"]. Expected: `dep_cycle(False)` still returns a cycle, `dep_cycle(True,"T'")` none; FC98 (b)'s sink list grows by 𝒱, parts(t), surv, Desc, h(t) — the rows of table (b). Command: `python3 -m model.run --claim FC98 --claim FC32 --scale 4`.
~~~~

**S-D1: P8** (r106)
~~~~
**P8 (code, not run).** For D1: `Org("Dcoll", ["v","w"], {"v":(0,1),"w":(0,1)}, ["k"], {"k":("v","w")}, ["b"], [ONE,"sv","sw"], compose, Lf)` with Lf slicing v under sv and w under sw through k; `Roles(...).asg == {"v":"k","w":"k"}`; `set_oj("k") == {"sv","sw"}`. Expected: D4.6's o_k has no value; the program's Causal(k) is computed — the conflict of D1 made runnable.
~~~~

**S-e-primed: P9** (r108)
~~~~
**P9 (maths, editorial).** Re-base the dangling primed ids in the claims file to the current ids (D2.4, D3.3, D4.6, D12.1, D12.7, D12.8).
~~~~

**S-e-represented: P10** (r110)
~~~~
**P10 (text).** L405: old "prepares a represented organization for explanatory use of c" → new "prepares \(\operatorname{Held}_\ell(o,c)\) (D18.1) for explanatory use of c" (replacement by formal statement; fixes the text side of the "represented" double use).
~~~~

**S-O1** (r114)
~~~~
- **O1 (L61).** Text change: old "(Suff) sufficiency of the four conditions of Account" → new "(Suff) sufficiency of \(\operatorname{Account}(\mathcal E)\land\neg\operatorname{Dec}(t)\) (D16.XV)" — the same form as L17's change.
~~~~

**S-O2** (r115)
~~~~
- **O2 (L49).** Text change: old "when its components respond to those edits as the target structure does (Part VII)" → new "when \(\operatorname{Account}(\mathcal E)\land\neg\operatorname{Dec}(t)\) holds of it (Part VII, D16.XV)".
~~~~

**S-O3** (r116)
~~~~
- **O3 (L69).** Text change: old "an explanatory candidate meeting \(\operatorname{Account}\) on its contract (Part V)" → new "an explanatory candidate meeting \(\operatorname{Account}(\mathcal E)\land\neg\operatorname{Dec}(t)\) on its contract (Part V, D16.XV)".
~~~~

**S-O4** (r117)
~~~~
- **O4 (L397).** Delete the span "What a stated premise cannot do is stand in for the steps. " (contradicts D9.2 as written by Q23).
~~~~

**S-O5** (r118)
~~~~
- **O5 (L397).** Text change: old "in that the argument has steps from it to what it rules out: it finds that the candidate gives what the premise excludes" → new "(D9.2)".
~~~~

**S-O6** (r119)
~~~~
- **O6 (S27).** None needed: the ruling out (D9.6–D9.8) and the response (D12.8, D14.2) share no definition, and L315 already writes the separation ("ruling the candidate out by χ is already doing something about it… a response that changes the candidate, the claim or the question is construction and repair").
~~~~

### `s105_glm_cases`

**K1: P1** (r113–r119)
~~~~
**P1 (code, K1)** — in the CT8 block of the case script, beside `k = con(h)`:
```python
HELD = True if any(o == "o_trees" for o in occ) else False   # Θ by hand (I90): the trees hold cod t (D18.1)
k_tprime = prep and HELD                                      # Con under T′ (I162), not the tag reading
P("         D12.2 (T′): Sel %s, Con %s => %s" % (yn(s1 and not prep and not any(x in ("t","H","surv","cod") for (_,x) in h.rep)), yn(k_tprime), cls(s1 and not prep, k_tprime)))
```
not run; expected: R5 "D12.2 (T′): Sel no (I161), Con yes => constructed"; R1–R4 unchanged.
~~~~

**K2: P2** (r121)
~~~~
**P2 (text, K2, L411)** — delete the span "; a constructed one does".
~~~~

**K2: P3** (r123)
~~~~
**P3 (text, K2, L201)** — old span "Neither provenance is reducible to the other: a selected transport has no represented target and no criticism in its history; a constructed one has both." → new span "(D12.1, D12.2)" (pointer).
~~~~

**K3: P4** (r125)
~~~~
**P4 (maths, K3)** — beside D16.XV: "Dec(t) in the Q2 condition is Dec read on t as one transport: CT(h′, t) prepares every part of t, the bindings of E's ports to the target included, so a content whose source was constructed, carried to a new target by a declared binding, is Dec; other choice: Dec per part (D12.4, I118), under which such a copy is not Dec and Expl is not blocked. [I167]" (invention to register).
~~~~

**K4: P5** (r127)
~~~~
**P5 (code, K4)** — build E9's S0 (window-w occupancy predictor) and S1 on the encoded object layer, in the program's notation; not run; expected: "(a) t0: Viol at the re-emergence pair yes; Surp yes given Sel(t0) (b3's end rule aside); (c) t1 and ψ∘t1: F1, F2, A yes, no admitted pair separates the two pairings" — turning FC102 (a),(c) and FC103 (a)–(c) from NOT TESTED to computed.
~~~~

**C-O1** (r131)
~~~~
- **O1 (L61)**: text, formal — old "(Suff) sufficiency of the four conditions of Account" → "(Suff) sufficiency of \(\operatorname{Account}(\mathcal E)\land\neg\operatorname{Dec}(t)\) (D16.XV)".
~~~~

**C-O2** (r132)
~~~~
- **O2 (L49)**: text, formal — old "when its components respond to those edits as the target structure does" → "when it meets \(\operatorname{Account}(\mathcal E)\land\neg\operatorname{Dec}(t)\) on its question and contract (D16.XV)".
~~~~

**C-O3** (r133)
~~~~
- **O3 (L69)**: text, formal — old "an explanatory candidate meeting \(\operatorname{Account}\) on its contract" → "an explanatory candidate meeting \(\operatorname{Account}(\mathcal E)\land\neg\operatorname{Dec}(t)\) on its contract (D16.XV)".
~~~~

**C-O4** (r134)
~~~~
- **O4 (L397)**: text, delete — "What a stated premise cannot do is stand in for the steps."
~~~~

**C-O5** (r135)
~~~~
- **O5 (L397)**: text, delete — "A premise taken as given differs from such a premise in that the argument has steps from it to what it rules out: it finds that the candidate gives what the premise excludes." (the next sentence already carries what remains of the difference, the denial block).
~~~~

**C-O6** (r136)
~~~~
- **O6 (S27)**: none needed. FC72 (d)–(f) (run, above) keep the ruling out a choice made through Accepted_j (I166, S28); no definition in §§12–14 lets a bare premise build, respond or repair (D12.8 asks a violation and a new transport, D14 an active route), so "not enough to do anything about it" and "an argument" never meet.
~~~~

## 5. Examined and held by the replies (not findings, not counted; silence is not agreement, rule 3)

| reply | held, same, clean or "nothing against" (r) |
|---|---|
| breaker | r21: ¬CT = ¬Con for traces at or before o_t; L411 met under T′; records keep Sel by D12.4 (FC12.new1, FC83 run). r31: T′ vs K and T on FC98 (c)–(e); L405, L201, L211, L13 met; FC84.new1 (d) one fixed point on 8,456 chains. r56: Q15, D6.4/Lost match L255 (FC22 (b) run). r62–r66: D6.3 (harmless), D18.1 one edge set (FC32), D15.2 per execution, Forms_cl (FC71), D16.4 ("admittedly undefined, not broken", NF12). r72: the list of claims held |
| maths_words | (a) "same": T1–T4, T7, T10, A2-T1, A2-T2, A2-T4, A2-T6 to A2-T12, A3-L441.1, L453.1, L471.1, L520.1, L526.1, L528.1, L584.1, L628.1–2, L630.1. (b) Q2 (L17, L536), Q6, Q15, Q23a, Q23b "same"; note r57: "Residual: Expl stays an atom; FC30.new1 (c) shows Expl := Acc∧¬Dec is available if a definition is wanted", proposal "none" (cf. B8). (c) "same": D2.1, D2.4, D2.6, D3.3, D3.4, D3.6, D4.6, D5.7 (see W2), D6.9, D8.2, D8.5, D8.new1, D9.1, D9.2, D9.4, D9.6, D9.7, D9.9, D9.10 ("more, unused"), D10.3, D11.4, D12.2, D12.3, D12.7, D12.8, D13.7, D13.8, D14.1, D15.1, D15.2, D15.5, D16.1–D16.3, D16.4 (note: "less than L497's 'specified independently'"), D16.5, D16.XV, D18.1, D1.4, D7.4, E1, E2. (d) r110: the clean list |
| structure | (f) Q15 clean; Q23 clean (I166 recorded). r121: D6.4/D8.2 under Q15; D9.2–D9.7; the K2 → Live staging; D15.2–D15.3; E1–E9; D18.2; the Q23 block against reworded denials |
| cases | (a) E1 forward (C3 printed "look: not as expected", "no conflict"), E1 reversed, E1 identification (moved by R4, matches the amended text), table L269, E2–E5, E6 (FC63 CEX "by design": "the counterexample is the encoding's (I14 vs I81), not the text's"), E7, E8 (moved by R13/Q13, matches), E9 where computed (see K4). (b) FC-E1–FC-E5 reproduced. (c) CT1–CT7 byte-identical. (d) the four examples faithful; note r50: an unrecorded change of contract gives Con through {o2} under S41 only, "which L161's frozen-contract rule does not forbid"; r53 witness and count changes, none in status. (e) N4, N5, N6 "Nothing against". r138 the clean list |

## 6. One point, several findings (for the orchestrator; no ruling)

| point | findings [area] |
|---|---|
| ≺_h well founded / the cut loop | B3 [1], S1 [3], S-fQ2 [1]; same fix (D11.3). **The replies differ on the witness**: B3 "no fixed point", S1 "two incomparable fixed points" |
| D13.8 "immediately after", q(o) (Q6) | B9 [1], S-fQ6 [1] |
| Rep / Held typed on contents vs H, surv | B5 [1], S-D2 [1] |
| "represented": Held vs Rep (L405, D13.3, CT8) | W7 [3], S-e-represented [3], K1 [1], K2 [1] |
| the survival condition | B8 [1], W6 [3] |
| Ident (I163) | B6 [1], B7 [1], R4-L151 [1], N3 [1]; A2-T13 [2] (C_id at L325) |
| I161 (¬CT in Sel) | B1 [1], B2 [1], B-e7 [1], T9 [1], C-CT8a [1], K5 [1], S2(ii) [3] |
| Dec and the Q2 write-in | B8 [1], K3 [1], S-fQ2 [1]; maths_words r57 (§5) |
| DEP a subgraph | S2(i) [3], S3 [3], S-b [3] |
| O1 (L61) | B-O1, S-O1, C-O1 identical; W-O1 also changes "(Nec) their" |
| O2 (L49) | four different new spans; **all four flagged S40** |
| O3 (L69) | four: same formula, pointers differ |
| O4 (L397) | four: the same deletion (C-O4 without the trailing space) |
| O5 (L397) | B-O5 delete clause; W-O5 formula (flagged); S-O5 pointer; C-O5 delete sentence |
| O6 | four: no change; W-O6 argues against part of the orchestrator's reading |
| L201 / L411 against T′ | K2 (P2, P3); B2 (L201 fixes the exact reading of "prepares") |

## 7. Notes for the orchestrator

1. **Reader invention numbers collide**: "I167" is B3's and S1's well-foundedness and K3's Dec-on-whole-t (different content); the breaker also uses "I168"–"I172"; S2(iii) "Inn". The register ends at I166; rule 6 numbers at integration.
2. **Structure reply, internal mismatch**: (e) names "P6, P10, P11"; (g) has no P11 (the primed ids are P9); "the δ and K renamings" announced, not given.
3. **Rule 6** (inventions into the text): S-P10 writes Held (T′, I162) into L405; W2 settles FC104's extent at L220; B4 points L195 at D18.1's staging (I162); C-P2, C-P3 delete L411, L201 wording that disagrees with T′ (I161, I162); B-e7 says T9 already wrote I161 into L195.
4. **Rule 3, not run** (run by the checker before ruling): B1 sketch; B7 FC28.new1; W3 re-runs (FC23, FC26, FC63); W8 restated FC18; B3 / S1 witness (infinite; outcomes differ); S-D1 witness and P8; S-P7; C-P1; C-P5; N1–N3. N4–N6 not run, "nothing against".
5. **S41**: no proposal found that would reverse or weaken Q2, Q6, Q15 or Q23. Findings on how an answer is written: Q2 B8, K3, S-fQ2; Q6 B9, S-fQ6; Q15 B6; Q23 B-Q23n. W3 changes NC1 and does not list FC22 (b) (Q15's case) among its re-runs.
6. **S40**: 6 flagged, of the 26 text proposals whose new span is given (B-O2, W-O1, W-O2, W-O5, S-O2, C-O2); no text proposal adds prose outside O1, O2, O5. S-P6's new span at L449 is not given. C-O2 leaves "(Part VII)" after its "(D16.XV)".
7. **Rule 12**: no finding is about what hard to vary covers or where values are placed; none is parked.
8. Receipts not opened (this agent's task: `.response.txt` only); the returns folder holds no `_pass2` or `_pass3` file.
