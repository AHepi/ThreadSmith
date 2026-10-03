# S108 Part A round 2 - what the variations found

*Written on 29 September 2026 by the one Opus 5.5 agent that settled the GLM cross-examination (decision S56), the records step of Part A's round 2 (rule 7 of `S108 Part A round 2 - how the GLM cross-examination will be read, written before sending.md`; decision S48), from the files named below. Nothing in the theory is changed: Part A is an experiment on copies (rule 11); the text (`tests/107`), the formal core after round 4, its claims and the program after round 4 are as round 4 left them. Terse by decision S40. Obeys decision S23 except where it quotes the owner; "candidate" or "explanation" for what the theory judges, never "model" (S43). Where the files after the cross-examination differ from the files after round 2, the former govern. Nothing here is settled (S28); no owner decision is added.*

## In brief

- **Asked (S52).** As round 1: keep the frozen parts (238 of 815 items, Claude's reading), vary the middle, see how the definition of explanation changes, map the dependencies. Round 2 aimed at what round 1 left open: the readings the owner's cases turn on, the claimed-only edges, and the middle definitions round 1 had not varied.
- **Run.** Four GLM 5.3 calls through Claude Code, one per section, round 1's frozen set and template; each accepted on attempt 1; loop ended 22:40:55 UTC on 28 September; no key in any output; every sandbox unchanged (64 files).
- **Tabulated** by a fresh Opus 5.5 agent: **41 variants** (S1 10, S2 11, S3 10, S4 10); **10 flagged** out of scope (rule 4) and not implemented; **31 implemented and computed**.
- **Staffing changed mid-round** by the owner's decisions S54, S55 and S56 (§2): the per-section agents were stopped; after a session restart one Opus 5.5 agent did the rest of the whole reading; the whole suite was run by script (42 runs); GLM, four jobs at once, cross-examined the result in place of an Opus reviewer.
- **Effect on explanation** (computed): (E) moved only where a variant rewrites what (E) reads (R2V1.1 on a declared question, R2V2.8's condition on the question's target, R2V2.2 with the written-in test back, R2V4.5's query). Being an explanation moved far more with **readings of Dec** (the record key, the trace's extent, the parts, a history with no stated construction, "worked out", chain histories, the cut) than with the definitions varied for the first time; of those, only D11.3 moved Dec.
- **The owner's cases stay where round 1 left them**, on the same readings (the change as an edit or a boundary; D6.3's quantifier; a question's recorded history), plus one new: a condition on the question's target at the program's grain (R2V2.8) empties the sign's and the weathervane's questions.
- **Map after the cross-examination**: 876 nodes, **351 edges: 268 computed, 51 claimed only, 32 contradicted**; 591 of 815 template items still untouched (426 of 577 middle).
- **Candidates**: **21** (13 from round 1, 8 new), **11 flagged** (no flag added or removed by the cross-examination).
- **Cross-examination**: 16 objections; **7 stand, 7 stand in part, 2 do not**. The one that mattered most: section 2's worked-case numbers rested on no kept run (two runs cut by a timeout); rerun, **every number reproduced**.
- **Decision (rule 5)**: **no third round; Part A ends; Part B follows** (S52).

## 1. The rule and the run

Round 2's reading rule (`S108 Part A round 2 - how the replies will be read, written before sending.md`, 882f23c) was committed before sending; the four briefs used round 1's frozen set and template, each section with its share of round 1's open edges and readings. Sent about 22:28 UTC on 28 September; `loop ended 2026-09-28T22:40:55Z`; replies 3,127, 3,410, 2,658 and 3,880 words, each ending END OF REPORT; returns saved before any was opened (f603ae5). Who computes was recorded before any reply was opened (7472b02).

## 2. Who did the work, and the owner's decisions during the round

- **S54** (2bbdfc5): after the Sonnet 5.5 trial, Part B's sections to be computed by Opus with Sonnet 5.5 as a second opinion. **S55** (aa6efbb) changed it: "Sonnet 5.5 for routine tasks only", because for these tasks it costs more than twice Opus 5.5. **S56** (855552e), the owner's words: "I see. You're using Opus 5.5 on Xhigh. That's a waste of tokens. It's capable of doing the whole thing on its own. Use GLM for cross examination. No need to Opus to do single sections".
- The tabulation (fd22ea5) and section 1 (917acee) were done by fresh per-section agents before S56. Sections 2 and 3 were in progress; S56 stopped them and their partial work was saved (855552e, 8020be9).
- **The restart.** The Opus agent first given the whole remaining job was cut off by a session restart at about 00:24 UTC on 29 September; its partial work was saved (f601771). One Opus 5.5 agent continued it, not redone (7ac7145). Its queue's whole-suite jobs had all ended at once with exit 2 (the harness refuses an output folder outside the scratchpad); they were rerun with the folders in the scratchpad. Two section-3 "failures" (exit 1) were results: the harness exits 1 when claims move.
- **The whole suite**, given by the round's rule to Sonnet harness workers with a verifier, was run by that agent's script, once per setting: 42 runs, the off runs 133 / 2 / 7 of 142 with no difference from the record; every run whose moves a section file listed moved exactly those (7dc907e). No second run by a verifier.
- **The map and the list** (7ec7725) by the same agent; **the GLM cross-examination** (2a7e188, 278db5e) in place of the Opus critical reviewer and second checker; its rule written before sending.

## 3. What was computed

31 variants, each a switch in a copy of the program whose default reproduces the printouts: worked cases (section 2: 60), FC-E1–E5, CT1–CT8, generated candidates at scale 4, chain histories (up to 3 or 4 holdings), and the whole suite. The 10 flagged and not implemented: R2V1.2–R2V1.5, R2V1.7–R2V1.9, R2V2.4, R2V2.7, R2V4.9 (each in effect rewrites a FROZEN item, adds prose, or repeats a round-1 variant; the orchestrator's to rule).

## 4. What moves the explanation definition (the map's §2)

| kind of variant | examples | effect |
|---|---|---|
| rewrites what (E) reads | R2V1.1 (a question recorded as declared), R2V2.8 (a condition on the question's target), R2V2.2 with V2.4 (the written-in test back, under each reading of D6.3's quantifier), R2V4.5 (E9's query) | (E) moves: R2V1.1 declared, as round 1's I5 (22 worked, every generated); R2V2.8 at the program's grain, every candidate on the sign's and the vane's questions (26 worked); V2.4 21 / 29 / 25 / 26 of 51 worked by quantifier |
| a reading of Dec | R2V3.2 (record key), R2V3.3 (trace's extent), R2V3.4 (parts), R2V3.5 (no stated construction), R2V3.1 (CT reading "worked out" through the account used), R2V4.4 (chain histories), R2V4.8 (cut U), R2V4.1–R2V4.3 and R2V1.6 (D16.XV's rule) | being an explanation moves with (E) unchanged; R2V3.5 drops every selected account whose history states no construction (1,013 / 881 / 232 / 1,670 generated); R2V4.4 makes every account an explanation; R2V4.8 leaves Dec without a value wherever t is held |
| an upstream definition varied for the first time | D6.9, D11.2, D11.3, D6.8, D9.1, D9.2, D12.7, D15.5 | none moves any candidate's Acc; only D11.3 (R2V3.7) moves Dec, on histories whose witness lies two steps back |

Also found: **the core and the program part on D13.8's record key** (R2V3.2: the program keys a record by the change, I174; the formal core's words by the new contract); every account on a re-entry history is an explanation under one and not the other. A result about the state after round 4, for the records, not for change in Part A.

## 5. The map

After round 1: 859 nodes, 221 edges (179 / 31 / 11). After round 2 (as sent): 876 nodes, 337 edges (265 computed, 46 claimed only, 26 contradicted), 110 of them new (70 / 32 / 8); template items touched 191 computed, 33 claimed only, 591 untouched; middle untouched 426 of 577 (after round 1, 473). **After the cross-examination** (`S108 Part A round 2 - the dependency map, after the cross-examination.md` / `.json`): **351 edges: 268 computed, 51 claimed only, 32 contradicted** (14 parts split off rows whose parts differ in standing; e2.14b computed); items touched 187 / 37 / 591; middle untouched 426. Middle definitions still untouched: D5.7 (upstream; its one variant rewrites a FROZEN sentence, so Part B's), D8.new1, D13.7, D14.1, D15.1, D15.2. Corrections O1–O4 from the review of the Sonnet 5.5 trial are carried as edges e2.O1, e2.O3, e2.O4 and the split e2.14 / e2.14b.

## 6. The candidates (after the cross-examination)

21: round 1's C1–C13, each with what round 2 computed of the readings it rests on, and C14–C21 (R2V1.6, R2V2.8, R2V3.5, R2V3.2, R2V3.3 (b), R2V3.4, R2V3.7, R2V2.6 at the reply's reach). **11 flagged** (S52: they do not appear to agree with a past decision of the owner's; "on that reading" where the owner's own case turns on a reading the owner has not settled):

| # | may clash with | in one plain sentence | everyday example |
|---|---|---|---|
| C1 | S44 | each part must match what its piece does inside the whole thing | a gear part may say only "the wheel turns at this speed with this rider" |
| C2 | S44, S41 Q15, S41 Q6, on that reading | a question simply laid down, not found or worked out, has no answer | a customer's bare "why is the sign red on Mondays?" |
| C5 | S41 Q15, S44, on that reading | a difference counts only when it comes with a change made to the thing | "someone flipped the switch" explains the lamp; "it is night" does not |
| C6 | S45; S44 on that reading | something with its answer written into one part is no explanation | a table that just lists the answers |
| C7 | S41 Q2 (in part) | a link counts as found by trial even with nothing tried, if nothing earlier stood for the answer | a formula on a napkin by someone who never saw a pendulum |
| C8 | S41 Q2, S41 Q15, on that reading | a worked-out link counts only if what it leaned on passes the tests | a navigator's course worked out with a method that fails at sea |
| C11 | S45; S44 on that reading | an answer written into one part passes the tests but is no explanation | "it is red because it is red" |
| C12 | S41 Q2 | anything that passes the tests is an explanation, even with a declared link | the student who copies the pendulum formula |
| C15 | S44, S41 Q15, at that grain | a question counts only if what it describes could be built in one way | "why is this lamp on at night?" when many circuits do that |
| C16 | S41 Q2; S44, S41 Q15 on a selection history | a link found by trying counts as declared unless the trying says what it was built from | a gardener who keeps the watering schedule that works but never writes down what it is |
| C21 | S41 Q2, on the reply's reading | a link counts as found by trial even when the answer was already in front of the chooser | a student who copies the formula, checks it on one swing, and keeps it |

S44's case is always the two-part sign (a red part on Mondays, a blue part on Tuesdays). Unflagged: C3, C4, C9, C10, C13, C14, C17–C20.

## 7. The GLM cross-examination and its settlement

Four GLM 5.3 jobs, one angle each (sections 1–2; sections 3–4; the map; the list against S20–S56), sent 02:16 UTC on 29 September; all four accepted on pass 1 by 02:41; receipts clean. Settled one by one in `S108 Part A round 2 - the GLM cross-examination, settled.md`:

| job | objections | stand | in part | not |
|---|---|---|---|---|
| a (sections 1–2) | 4 | 3 | 0 | 1 |
| b (sections 3–4) | 5 | 1 | 3 | 1 |
| c (the map) | 5 | 2 | 3 | 0 |
| d (the list) | 2 | 1 | 1 | 0 |

What changed: **Xa1** (section 2's worked-case numbers unbacked) rerun in 12 minutes, every number reproduced; **Xb1** R2V4.3's "contradicted" holds on one reading of "Sel at o" (25 of 3,208 chains), on a second gives 4, on a third 0: qualified and split; **Xc1** eleven map rows whose parts differ in standing split into twelve parts (six claimed only, five contradicted, one computed; R2V3.8's effect on (Nec) computed in the settlement); **Xc2** the verdict on a third round now names D6.5, D12.3 and D18.1 and argues them; **Xc3** a trailing comma had dropped R2V2.11's closure of e2.38 and e2.39 from the map's `.json`; **Xd1** C2's bridge flag needs three more readings (a criticized first design in its history, "created" as CreateEx, the brief as the question), recorded "on that reading"; which history the owner's bridge is stays the owner's (rule 6); **Xd2** C16 now quotes the owner's answer to S41 Q2, not Claude's question. Not standing: **Xa4** (the S44 quotation is verbatim) and **Xb5** (the glosses are right). The rest are record pointers and errata of the section files (kept as sent).

## 8. The Sonnet 5.5 trial (S53)

Sonnet 5.5 redid round 1's section 2 blind; an Opus review compared it (`S108 Part A - Sonnet 5.5 trial/Opus review of the Sonnet 5.5 trial.md`). On what can be counted it matched Opus; it did three things the Opus computation had not (FC50's count, a finite analogue of L311, V2.3's reading through τ); it fell short where the job is analysis. Its four findings (O1–O4) are carried into the map. The owner's S54 and S55 followed.

## 9. Departures and failures

- The staffing of rules 5 to 9 (§2), under S55 and S56; no verifier's second run of the suite.
- **Section 2's worked-case script was cut twice by a timeout** before round 2 was written, and the file did not say so; found by the cross-examination (Xa1); rerun, nothing wrong.
- **The map's builder took one standing per row** (Xc1) and **skipped a row with a trailing comma** (Xc3); both repaired in the corrected copy.
- Wrong pointers in sections 3 and 4 (a suite run "§8" that does not exist; a file named in section 3 that lives in section 1's folder); recorded as errata.
- The first continuing agent's queue failed at once (exit 2) and was lost to the restart; the work was continued, not redone.
- No suite run with cut U in place of T′ (R2V4.8 is a parameter, not a switch); recorded.

## 10. Not tested, and unsure

- Every reading the owner's cases turn on remains the owner's: edit or boundary; D6.3's quantifier; a question's recorded history; Desc's grain; now also which history the bridge is.
- Section 4's program code was not in any cross-examiner's sandbox; the md5 checks of the copies were taken on trust by the cross-examiners.
- 426 of 577 middle sentences are untouched; the section agents judged most not upstream of the definition; no job contested it.
- The whole suite was run once per setting, not twice.
- The everyday examples are the agents' own, written to show each sentence; the owner's cases (the sign, the vane, the pendulum formula, the bridge) are the computed ones.

## 11. What follows

**Part B** (S52): freeze all but the parts that are hard to vary, vary those, and see how explanation changes in meaning and scope; under its own rule, written and committed before sending; staffed under S55 and S56 (one Opus agent per whole job; GLM for cross-examination; Sonnet 5.5 for routine jobs only). Then the flagged candidates go to the owner for a yes or a no.

## Files

- `results/S108 Part A round 2 - how the replies will be read, written before sending.md`; `… - who computes, recorded before any reply is opened.md`; `… - tabulation of the replies, before any ruling.md`; `… - section 1 … 4 - variants computed.md` / `.json`; `… - computation/`.
- `results/S108 Part A round 2 - the dependency map, after round 2.md` / `.json`; `… - candidate definitions of explanation, after round 2.md` (as sent to the cross-examination).
- `results/S108 Part A round 2 - how the GLM cross-examination will be read, written before sending.md`; `… - GLM cross-examination returns/`; `… - the GLM cross-examination, settled.md`; `… - computation/cross-examination runs/`.
- `results/S108 Part A round 2 - the dependency map, after the cross-examination.md` / `.json`; `… - candidate definitions of explanation, after the cross-examination.md` (these govern).
- `plain words/108 Part A round 2 - what the variations found, in plain words.md`.
