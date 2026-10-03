# S104 Round 2 — what the readers found and what changed

*Written on 28 September 2026 by a Claude subagent (Opus 5.5), the records step of round 2 (log S104), from the files named below; it ruled on nothing and read no reply, reasoning file or request file. The text under review was `tests/103 The semantics, standing alone, after round 1.md` (md5 f31ebb1f050783f1a84f6136cec20fcd, unchanged). The new text is `tests/104 The semantics, standing alone, after round 2.md` (md5 735ec1e8256cc6a251715a031944ea65, 632 lines; checked). Terse by decision S40. This file obeys decision S23 except where it quotes the owner. Nothing here is settled (S28).*

## In brief

- **Asked.** Round 2 of the review rounds (S35), the maths round (S36): the text written as mathematics (definitions, 110 claims, a program that searches small models for counterexamples, every forced choice recorded as an invention), sent beside the words to Mimo and GLM in 17 parts, each asked where the maths and the words part.
- **Back.** All 34 replies, each accepted on pass 1 (Mimo 17 of 17, GLM 17 of 17).
- **Tabulated.** 399 items from the parts; 349 items to checkers (328 of them from the parts, plus 13 findings of the external reader and 8 items of the creative transport case); 70 not challenged by either reader.
- **Stopped.** A run of 78 checkers, one per group of lines, writing prose rulings, was stopped on the owner's words (S40: "more prose is self defeating"; "This only needs maybe 3 checkers."). Four rulings finished, four begun; all eight kept as a record, none applied.
- **Ruled in maths and code.** Three area checkers, one integration agent, one critical review (Fable 5.1, 16 objections), one second checker.
- **Claims.** 87 hold / 12 counterexample / 11 not tested (of 110) → **103 / 3 / 7 (of 113)**. The three left rest on inventions or on a claim's own wording, not on the words.
- **Text.** 43 changes on 32 lines, each a formula, a pointer or a deletion; no prose added. Words outside formulas **15,611 → 15,409**.
- **Owner questions left:** three (on what counts as an explanation, an episode of construction, a question with no definite answer at the baseline), and a fourth returned because it turns on the owner's reading of "argument" (S23).
- **Moves: 115** (strict count). So round 3 follows: GLM alone, up to four calls at once, each with a slightly different job (S38, S39).

## Before the replies

- **The maths** (c764266, 19:33 UTC on 27 September), in `results/S104 Round 2 - maths/`: formal core (115 definitions, 9 encodings of the worked cases), claims FC01–FC110 and NF01–NF19, inventions I01–I102, the search (87 hold on every model tried, 12 counterexample, 11 not tested), and two fresh checks: of the program and its twelve counterexamples, and of the formalization against the text.
- **Briefs and reading rule** (a3f7b46, 21:00 UTC): seventeen parts, the same to both readers, built by `tools/s104_build.py` (491 quoted lines compared with the text); the reading rule, 15 rules, committed before sending.
- **Two addenda to the reading rule**, each written before any reply was opened: the external cross-examination the owner supplied (ddd718e; read as a third reader's reply, findings E01–E22; its examples reproduced as FC-E1 to FC-E5, all reproduced; inventions I103–I108), and the owner's creative transport experiment (f15e1e4; rerun byte for byte, read as a case card with items C01–C14; inventions I109–I121). Decision S37 records the owner's words on both.
- **The open expression workspace** (d1d17fc): one agent reran it (35 tests pass) and found nothing the maths, the case card or the external items had not already tested; kept as a record, not a case.
- **Four GLM calls at once** (e4e20ce), for round 3 (S39): two bursts of four through `tools/glm_via_claude_code.py`, all eight accepted on attempt 1; in the second, all four streamed together for at least 15 s. GLM's slot limit set to 4 in `tools/s80_common.py`; Mimo's left at 1 and kept out by not sending (S38).

## Receipts

Both runs launched at about 21:00 UTC on 27 September; request files committed in flight (a201bd1), returns saved unread while the runs went on and all in at 76f14b8 (01:31 UTC, 28 September). Each receipt was read before its reply, and only the `.response.txt` files were read for arguments (the tabulation, section 1).

| reader | parts | back (UTC) | attempts | reply words (`wc -w`) |
| --- | --- | --- | --- | --- |
| GLM (glm-5.3 via Claude Code, effort medium) | 1–17, one after another | 21:05 to 22:00, 27 September; 144 to 362 s a part | 1 each; no connection failure, no answer rejected | 1,773 to 2,772 |
| Mimo (mimo-v2.6-pro, effort medium) | 1–17, one at a time | 21:08, 27 September, to 00:55, 28 September; 435 to 1,197 s a call | 1 each, except part 14: attempt 1 a connection failure (no HTTP status; not counted against the reader, rule 2), attempt 2 accepted | 1,373 to 2,779 |

Every reply ends with END OF REPORT; no part needed a second pass, so no item is "not examined".

## The tabulation

`results/S104 Round 2 - tabulation of the replies, before any ruling.md` (594f9a1): one fresh Opus 5.5 agent; 399 items from the parts (definitions, encodings, claims, inventions, U- and H-entries, NF entries, round-1 matters and changes); 255 distinct proposals copied byte for byte; every quotation compared with the text. To checkers: **349** (313 challenged by Mimo or GLM, among them the twelve counterexamples; 15 challenged only by the external reader or the card; 13 external findings; 8 card items). Rule 7: **70** "not challenged by either reader; not thereby final". 16 context items. Marked PARKED on 4 rows and OWNER QUESTION on the rest of section 7; marked, not weighed.

## The stopped run

- **Grouping** (562f52b, before any ruling): items sharing a line, grouped transitively, gave 55 groups, two of them of 92 items over 23 lines and 109 items over 38 lines. Those two were split by the section each line stands in, keeping one checker per line: 78 checkers over 140 lines. A recorded departure from the letter of rule 5.
- **Stopped** at about 02:40 UTC on 28 September, on decision S40. Finished (END OF RULING): L113-L127, L13-L201, L255-L257, L315-L568 (committed 02:46 to 02:53). Begun: L109, L217-L225, L231-L253, L375-L385. All eight in `results/S104 Round 2 - rulings/`, unchanged; the finished four were given to the area checkers as analysis, their prose wordings not used.
- **What replaced rules 5 and 12 to 14** (437efd6): `results/S104 Round 2 - the owner's change to the reading - three checkers, in maths and code.md`. Three checkers, one per area; each verdict in one line; each fix as maths beside the old, put into a copy of the program and run; the text changed only by deleting a span, replacing it by its formula, or replacing it by a pointer.

## The three areas

Verdicts: holds against the maths (M), against the words (W), rests only on an invention the text leaves open (I), does not hold (N).

| area | lines | items | M | W | I | N | text changes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 (a2a78c1) | L1–L228 | 117 | 26 | 37 | 31 | 23 | 10 (9 formal, 1 deletion) |
| 2 (24b9029) | L229–L372 | 104 | 21 | 22 | 17 | 44 | 13 (5 formal, 8 pointers); 7 rows split, counted by first verdict |
| 3 (cd077b0) | L373–L632 | 128 | 21 | 43 | 37 | 27 | 19 on 17 lines (17 formal, 2 pointers) |

The fixes that matter most:

- **Area 1.** The identity edit no longer sets a port (D2.1′). An intervention on a component is any edit that replaces it by a slice on a port it assigns, single or composite (D2.6); observation and the three families rest on it (D2.4′, D4.6′). Selection bars any occurrence of t's own history from representing t, the record, the survival condition or the codomain (D12.1′). Surprise and a selection response are read in t's one history, and a response needs a violation (D12.7′, D12.8′). Seven counterexamples resolved (FC05, FC20, FC77, FC78, FC81, FC82, FC83). The one deletion: L199's "The transport is entered into the model by its author.", which made a transport found by a coded search declared by whoever wrote it in (card item C01).
- **Area 2.** The slot test of non-circular dependence (D6.3), read with L255, L273 and L397: three models met (E) under the old test and fail it under the new. Conflict with a claim needs something the claim excludes (D8.5); a claim allowing everything conflicted before. Rivals need both candidates offered (D8.3). Counterparts are compared through one port bijection (D8.new1). A test is a record at one pair (D10.3). FC25 resolved (I14's bookkeeping).
- **Area 3.** (K3)'s added step (D9.9). The history order is acyclic, not a partial order (D11.3). Active routes rewritten: members reach the result inside the route, side inputs admitted, "already at rest" kept (D11.4). Build keeps "a represented organization for explanatory use" (D13.3), which exposed a loop in the words: represented → constructed → built → represented (external item E03). Which defeat conditions of Part XV can be written in maths, and which cannot ("is an explanation", "does explanatory work", "capture", "without loss"). FC90 and FC98 computed; FC102 resolved.

## Integration

One agent (84c4969) merged the three model copies into `model after round 2/` (one textual conflict, in FC14, combined; none in substance), numbered the inventions I122–I160, wrote the formal core and claims after round 2 beside the old files, and applied 42 text changes by program to file 104 (0 refused). Claims 87/12/11 of 110 → 98/3/9 of 110; with three new claims, **101 / 3 / 9 of 113**. Words outside formulas 15,611 → 15,463. It left one interaction open (X2: area 1 used "represented" unstaged; area 3 left its staging to the owner) and counted 120 moves.

## The critical review and the second checker

The review (Fable 5.1, 8d2d62b) raised **16 objections**, three of which matter; it reproduced the whole suite (101/3/9) and the prose count. The orchestrator sent all 16 to one fresh second checker (ec18198), R1 and R3 first; it took R2 at once (the L195 change as a pointer until R1 and R3 were ruled). The second checker (bfac1c4) chose between the first fix (a), the review's (b), or a third (c):

| | objection | ruling |
| --- | --- | --- |
| R1 | Under one staging of "represented" (cut T), a transport could be both selected and constructed, against L193's "exactly one"; FC12.new1 and FC83′ held only because the program read hand-set tags. Computed by the review with the program's own function. | (b), corrected: selection also requires that no construction trace in t's history prepares t (**I161**). Selected and constructed are then exclusive under every cut; FC12.new1 and FC83 now compute "represented". Over 4,680 short histories: without I161, 1,085 and 1,300 cases both under cuts T and T′; with it, none. |
| R2 | The L195 change wrote an unstaged "represented" into the text before the loop was ruled. | (c): with R3 ruled, L195 carries the formula, cut included. |
| R3 | The loop's question (owner question 1) was stated unfairly and may not be the owner's. | (c): not the owner's; a new cut **T′** (**I162**): "held" where L405 forces it (a construction's target, a build's output), "represented", staged along the history order, in selection's exclusion. The words as they stand break L526 and L193; cut K breaks L405; cut T breaks L195 with L211; T′ meets all four. |
| R4 | Area 2's pole fix (the identification contract with no edit) made the pole's identification question fail D3.3. | (b): an identification question needs the observed value to vary over the contract (**I163**); L151 gets the formula. |

Of the other twelve: (b) on R6, R7, R9, R11–R16 (R16 recorded as **I164**); (c) on R5 (one edge set, L526 a pointer), R8, R10; none kept as first written. R15 replaced "classically sound" by the classical forms (S23).

## Claim results

| | hold | counterexample | not tested | of |
| --- | --- | --- | --- | --- |
| before round 2 (c764266) | 87 | 12 | 11 | 110 |
| integration (84c4969) | 101 | 3 | 9 | 113 |
| after the second check (bfac1c4) | 103 | 3 | 7 | 113 |

Counterexamples left: FC18 (rests on I94, which L556 excludes), FC23 (b) (the claim's own wording), FC63 (c-i) (I99). Not tested: FC31, FC35, FC89, FC94, FC104, FC105, FC110. Scale 4, time cap 45 s, `PYTHONHASHSEED=0`; the whole suite about 386 s.

## The text changes

File 104 from file 103 by `apply text changes.py` reading `text changes after the review.json`: **43 changes on 32 lines**, 0 refused, 0 held.

| kind | changes |
| --- | --- |
| a span replaced by its formula | 32 |
| a pointer to a definition or claim added | 10 |
| a sentence deleted (L199) | 1 |

All words 16,394 → 16,284; **words outside formulas 15,611 → 15,409**. The S95 scan finds 3 new hits, all the symbol Accepted_j (allowed as tentative, S23), none forbidden; the S96 physical scan none new; headings, defined terms and labelled formulas all kept. Changes that write an invention in say "settles" (rule 6).

## Inventions added

**43 numbers, I122–I164**: I122–I160 from the areas (13, 10 and 16), I161–I164 from the second check. I132 and I139 are one choice (κ(⊥) := ⊥), so 42 choices; I131 and I134 recorded, not adopted; I146 fixed by I162; I153 fixed (tolerance per execution); I149's reading of "already at rest" open, not the owner's. Earlier in the round, before any reply: I103–I108 (the external examples) and I109–I121 (the creative transport case). None of these is a move.

## Owner questions left

25 were raised by the areas; the second checker ruled 22 on argument, each with the other side in one line (`owner questions after round 2.md`, §B). Left with the owner:

- **Q2.** L17 against L536: is meeting (E) enough to count as an explanation, or only for a transport whose provenance is not declared?
- **Q6.** "Episode": any delimited stretch of a history (the body's uses), or L55's history in which contracts change, each change recorded?
- **Q15.** NC2's contrast when the baseline answer is not determined: only a determined baseline counts, or a value against no value either way?
- **Q23, returned.** Is a bare premise an argument? Ruled "no" by the second checker (L397's argument steps; S23's "strung together into a coherent structure"; S27). It turns on the owner's reading of "argument" (S23), and the second checker itself says it goes back if the owner reads S23 otherwise; listed here as the owner's.

## Parked

Seven points, recorded and not applied (S33, S34; `parked after round 2.md`): P1–P3 (S20 cited on survival conditions, competitors in a population, and time-indexed survival), P4 (FC43, "easy to vary" read as "has a variation that still meets"), P5 (a population's restriction and "value"), P6 and P7 (the S20 sides of Q12 and Q18). No value was moved.

## Moves

Counted strictly (decision 5 of the orchestrator): 72 formal changes answering a challenge that holds (area 1: 17; area 2: 24; area 3: 22; second check: 9) plus 43 text changes applied = **115**. Not counted: register entries, re-based claims, new test claims, Part XV. The integration's 120 counted some of these. Moves > 0, so the series goes on (rule 15).

## Departures from the reading rule

- The two large groups split by section (rule 5), recorded before any ruling.
- Rules 5 and 12 to 14 replaced on the owner's word (S40): no KEEP, FIX or DROP per line; fixes in maths and code; the text applied by the integration before the review and rebuilt after it (84c4969, then bfac1c4).
- Rule 14's re-reading of the cases on the new copy was not done.
- The review file is `critical review of the round.md`, not rule 13's `critical review of the rulings.md`; its 16 objections went to one second checker, not to one per group.

## Agents and outside calls

- **Agents:** the maths' builders (how many is not recorded in the maths files) and its two fresh checks; one agent for the briefs and the reading rule; one for each addendum (external cross-examination; creative transport case); one for the open expression workspace; one for the four-GLM test; one tabulator; eight checkers of the stopped run; three area checkers; one integration agent; one critical review by Fable 5.1; one second checker; this recorder. All but the review Opus 5.5.
- **Outside calls:** the 34 round-2 calls (35 attempts); the eight four-at-once GLM test calls; Z.ai's documentation pages, read by the four-GLM agent.

## Not tested, and unsure

- No outside reader has seen file 104, the formal core after round 2, or the new claims.
- Each area was ruled by one checker, and the review's objections by one second checker; cut T′ is that checker's own and read by no one else. It needs the history order well founded (no endless run of earlier occurrences) below the transport's occurrence.
- In FC12.new1 and FC83, earlier occurrences and traces are still set by hand (I90); only the output's holding and selection's conditions are computed.
- The simulation layer is not encoded (E9's is not built); FC35 stays not tested.
- Seven claims are not tested; a claim that holds on every model tried holds on nothing beyond them (rule 3).
- Not done (the areas' own lists): FC51 (b) for (F2) and (A), stated and not coded; the slot's quantifier readings (I136) not run on the worked cases; the external-examples and case-card addenda not rewritten for their changed output lines (FC-E3, CT8).
- The project's everyday cases were not read again on file 104.

## Files

- This file; `plain words/104 Round 2 - what the readers found and what changed, in plain words.md` for the owner.
- The reading: the reading rule and its two addenda; the tabulation (.md, .json); the grouping (.md, .json); the owner's change to the reading (with the three areas' .json); `S104 Round 2 - rulings/` (the stopped run).
- `S104 Round 2 - maths after the reading/`: the three areas (verdicts, runs, text changes, model copies); the integration report; `model after round 2/`; the formal core, claims and inventions after round 2; owner questions; parked; `apply text changes.py` and `text changes after the review.json`.
- The critical review, the orchestrator's decisions on it, and the second checker's file.
- `tests/104 The semantics, standing alone, after round 2.md`.
