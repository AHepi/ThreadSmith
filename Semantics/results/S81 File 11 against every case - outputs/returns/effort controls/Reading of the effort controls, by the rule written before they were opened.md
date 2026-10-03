# Reading of the effort controls, by the rule written before they were opened

23 September 2026. Written by a Claude subagent for the orchestrator. This reading applies the rule in `READ ME - effort controls, outside the S81 table.md`, section "How the controls will be read", as written. It uses R1, R5, R6 and R8 for the Mimo control and R4 for the two Atria controls.

## In short

- **R1, Mimo.** On the same 2a text, the medium control used 54,236 reasoning tokens and 244,044 characters of reasoning. The accepted high reading used 42,679 tokens and 193,318 characters. Medium over high is 1.27 for tokens and 1.26 for characters.
- **R5, Mimo.** The FINDINGS wording differs in all 52 rows. In substance, 16 rows show no difference in FINDINGS, OPEN or SPLIT, and 36 rows differ in at least one of them. By field: FINDINGS are the same in 32 rows, overlap in 13 and differ in 7. OPEN differs in 27 rows. SPLIT differs in 10.
- **R6 and R8.** This is one run at each effort, with no repeat at high. Where the two runs agree, that does not show the two efforts are equivalent. Where they differ, that is not read as an effect of the effort. Runs at high on this same text have varied widely: three earlier attempts at high hit their output limits before writing any reply.
- **R4, Atria.** Both Atria controls failed. Every attempt that returned stopped with finish "length" at the 65,536-token limit. Neither receipt records a token count. No inference about effort is drawn.

## What was read, and when the rule was written

- The rule was committed at 11:29:32 UTC (commit 10464ba). The Mimo control had already returned: its four files were in this folder, listed by name only, at 11:28:44 UTC. Nobody had opened them. The READ ME records this, and the fact goes with this reading.
- This reading used:
  - the receipts and request bodies of `returns/s81_2a_mimo` (accepted at high, pass 2) and `s81_2a_mimo.control-medium`;
  - the length of each call's reasoning file and response;
  - the FINDINGS, OPEN and SPLIT of both 2a responses;
  - the receipts and error files of the two Atria controls. The Atria attempt files were measured for length and not read.
- The 2a readings are blind readings of the cases. The brief gives the theory and the 52 situations and withholds the cases' verdicts. Reading these texts has no bearing on the S81 determination, which was already written.
- The controls stay outside the S81 table (R7). Because the Atria `control-medium` failed, there is no second table.

## Mimo: what was sent

| | accepted `s81_2a_mimo` | `s81_2a_mimo.control-medium` |
| --- | --- | --- |
| `reasoning_effort` in the request body | high | medium |
| Pass, attempts | pass 2, 1 attempt | pass 1, 1 attempt |
| Asked (UTC) | 07:33:23 | 11:11:03 |
| `max_tokens` | 131,072 | 131,072 |
| Temperature, thinking | 0.7, on | 0.7, on |
| User text sha256 | a2cef715… | a2cef715… |
| Request body sha256 | 312e8d37… | 9c763dd9… |
| Finish | stop | stop |
| Seconds | 835.9 | 1,006.3 |

The two request bodies differ in one field only: `reasoning_effort`. The accepted call's receipt has no `reasoning_effort` field; the control's receipt has one. The effort "high" of the accepted call comes from that call's `request.json`, whose sha256 equals the receipt's `request_sha256`.

## R1. Reasoning at medium against reasoning at high

| | high (accepted) | medium (control) | medium / high |
| --- | --- | --- | --- |
| Reasoning tokens (receipt) | 42,679 | 54,236 | 1.27 |
| Reasoning text, characters (receipt; the reasoning file gives the same count) | 193,318 | 244,044 | 1.26 |
| Completion tokens | 56,306 | 66,351 | 1.18 |
| Completion tokens other than reasoning | 13,627 | 12,115 | 0.89 |
| Response, characters | 63,224 | 55,129 | 0.87 |
| Prompt tokens (of which cached) | 19,367 (19,328) | 19,367 (19,328) | 1.00 |

In this pair, the medium run reasoned more than the high run: 11,557 more reasoning tokens and 50,726 more characters of reasoning. There is one run at each effort, and runs at high on this text have varied widely (R8, below). So this pair does not settle whether Mimo honours the effort setting.

## R5. The two 2a readings compared row by row

This comparison only describes. There is no repeat at high, so every difference below mixes the effect of the effort with run-to-run variation. None of them is read as an effect of the effort.

**How the rows were compared.**
- FINDINGS were compared by what they say, in three classes:
  - **same**: the same findings in other words, possibly with a different amount of detail;
  - **overlap**: one side states a finding the other does not, and nothing is at odds;
  - **differ**: the two classify some element of the case differently, or one decides what the other leaves open.
- For OPEN and SPLIT, the comparison records whether each reading names a matter or says NONE. Where both name matters, it records whether the matters are the same, overlapping or different.
- The classification is this reader's judgement. The table gives the ground for each call.

**Form.** Both replies are complete: all 52 records are in the required form, and `END OF REPORT` is on the last line. Both give `COUNT: 8` under "Noticed beyond the cases". R5 does not cover that section, and it is not compared here.

**Wording.** The FINDINGS wording differs in all 52 rows. The OPEN text is identical in 17 rows, all of them NONE in both readings. The SPLIT text is identical in 40 rows, all of them NONE in both. No row is identical in all three fields.

**Substance.**
- 16 rows show no difference in FINDINGS, OPEN or SPLIT: O9, O17, O21, O23, O25, O26, O34, O36, O37, O39, O43, O46, O47, O48, O49, O52. The other 36 rows differ in at least one of the three fields.
- **FINDINGS:** 32 same, 13 overlap, 7 differ. The 7 that differ are O2, O10, O28, O29, O30, O33 and O35.
  - The medium FINDINGS are shorter in 51 of the 52 rows: 2,914 words against 3,951 (0.74), and 180 sentences against 208.
  - In 7 of the 13 overlap rows, only the high reading has the extra finding. In the other 6, each side has a finding the other lacks.
- **OPEN:** 27 rows differ.
  - 17 rows are NONE in both.
  - 11 rows name a matter at high only: O2, O5, O13, O20, O24, O31, O33, O42, O44, O45, O51.
  - 1 row names a matter at medium only: O32.
  - 23 rows name matters in both readings: 8 the same matter, 5 overlapping, 10 different.
  - Rows with any OPEN matter: 34 at high, 24 at medium. Matters named: 39 at high, 27 at medium.
- **SPLIT:** 10 rows differ.
  - 40 rows are NONE in both.
  - 3 rows have a SPLIT at high only: O4, O10, O19.
  - 5 rows have a SPLIT at medium only: O15, O24, O30, O35, O40.
  - 4 rows have a SPLIT in both readings: 2 on the same matter (O2, O50) and 2 on different matters (O1, O28).
  - Rows with a SPLIT: 7 at high, 9 at medium.
- **Matters that change field.**
  - In O24, O30, O35 and O40, a matter the high reading lists as OPEN is the medium reading's SPLIT.
  - In O4, the ground of the high reading's SPLIT (which question was asked) appears in the medium reading's OPEN.
  - In O2, the high reading names the bell matter under both OPEN and SPLIT. The medium reading names it under SPLIT only.
  - In O35, the high FINDINGS decide the matter (the protected condition was lost), while the medium reading leaves it as a SPLIT.

**Row by row.** Words are the FINDINGS word counts, high / medium. In the notes, "high" is the accepted `s81_2a_mimo` and "medium" is the control.

| Row | Words | FINDINGS | OPEN | SPLIT |
| --- | --- | --- | --- | --- |
| O1 | 119 / 94 | same | overlapping: both: the rule's organization; high also: whether each limit is appropriate; medium also: the provenance of each restated contract | different: high: account or table of successes. medium: stated scope or a contract that excludes every relevant change |
| O2 | 108 / 66 | differ: high gives the bell a measurement's signature (it reads and reports the float); medium calls it a genuine mechanism that answers a different question | high only | same: whether removing the bell meets non-circular dependence |
| O3 | 99 / 67 | overlap: high adds that the construction witness is incomplete; medium adds that the tally is a new organization she built | different: high: construction witness; New under (N). medium: organization or contract; retained capability under a use task | NONE in both |
| O4 | 119 / 66 | same | different: high: which kind of edit recalibration is; "restates". medium: whether the contract is production or identification (high's SPLIT ground) | high only: naming that answers the wrong question, or a permitted coarse account |
| O5 | 94 / 72 | same | high only | NONE in both |
| O6 | 83 / 56 | overlap: high adds that the first statement answers the identification question only, and names (F2) | NONE in both | NONE in both |
| O7 | 79 / 62 | overlap: high leaves open whether the rule is an account (no component decomposition given); medium does not raise it | overlapping: both: components or organization behind the rule; medium also: grain and contract | NONE in both |
| O8 | 75 / 44 | overlap: high adds that the combined-draw commitment meets non-circular dependence | different: high: whether the restriction is appropriate. medium: the contract's provenance | NONE in both |
| O9 | 85 / 63 | same | NONE in both | NONE in both |
| O10 | 86 / 62 | differ: high lets the held temperatures separate the two on a contract with no setting change, so Emil's finding stands there; medium says the room outcome is a state, not a signature feature | same: the contract of the comparison | high only: Rosa's one kind or Emil's two |
| O11 | 79 / 57 | overlap: high leaves Wednesday's pick open (her prior repertoire); medium says the pick is not relay and uses Tuesday's construction | overlapping: both: Wednesday's pick and New; high also: Monday's selected provenance | NONE in both |
| O12 | 99 / 68 | overlap: high says the situation gives no witness in the required form and adds the new obligation as a declared input; medium states (G) conditionally | overlapping: both: the construction witness; medium also: New | NONE in both |
| O13 | 69 / 54 | same | high only | NONE in both |
| O14 | 82 / 47 | overlap: high adds relay from the book, the declared use task, and the open question of his own bindings | different: high: a nontrivial binding construction. medium: the declared use task | NONE in both |
| O15 | 80 / 55 | overlap: high adds that Sam's following of the arrows is deployment of received content | same: the arrow's provenance | medium only: whether the arrow represents content with no recorded witness |
| O16 | 67 / 56 | overlap: high adds that Sam's cutting stays deployable | NONE in both | NONE in both |
| O17 | 67 / 53 | same | same: the declared boundary (high also: continuity) | NONE in both |
| O18 | 54 / 35 | same | different: high: New under (N). medium: whether the one binding is "nontrivial" | NONE in both |
| O19 | 74 / 38 | same | NONE in both | high only: whether the open diagram is a route in the candidate |
| O20 | 58 / 37 | same | high only | NONE in both |
| O21 | 83 / 53 | same | same: the declared boundary | NONE in both |
| O22 | 82 / 54 | overlap: high derives the lead's direction from the admitted edits; medium places the lead at the output port as a port value | different: high: single-knob edits in the contract. medium: the declared grain | NONE in both |
| O23 | 64 / 48 | same | NONE in both | NONE in both |
| O24 | 80 / 76 | same | high only | medium only: one account at the tested contract or two at a finer one (high has this ground as OPEN) |
| O25 | 60 / 42 | same | NONE in both | NONE in both |
| O26 | 71 / 46 | same | NONE in both | NONE in both |
| O27 | 89 / 54 | overlap: high gives the candidates and the test to the expert; medium calls the episode a complete critical episode and the third fault the robot's new content | overlapping: both: New for the third fault; high also: the declared boundary | NONE in both |
| O28 | 72 / 59 | differ: high holds that the card's representation does not lapse with the reader; medium leaves that as its SPLIT | different: high: whether the touch method was selected or constructed. medium: whether the convention counts as declared | different: high: whether the fresh copy is a second witness. medium: whether the marks still represent content without a reader |
| O29 | 83 / 77 | differ: high holds that the quoted line is still an evidence leaf; medium lists that question as OPEN | different: high: whether the line carries an interpreted claim. medium: evidence leaf or derived record | NONE in both |
| O30 | 65 / 48 | differ: high keeps the remote person's authoring an outside contribution; medium says the authorship does not by itself make the routine one | same: the uploaded routine and the boundary | medium only: which clause of one Part X sentence governs the uploaded routine (high has this as OPEN) |
| O31 | 54 / 47 | same | high only | NONE in both |
| O32 | 66 / 47 | same | medium only | NONE in both |
| O33 | 78 / 66 | differ: high: the table answers only the joint question, which was Lea's; medium: the single-knob edits are silently excluded, which non-vacuity forbids, and the rewrite is a different question from Lea's | high only | NONE in both |
| O34 | 72 / 57 | same | NONE in both | NONE in both |
| O35 | 85 / 56 | differ: high: the protected condition was lost; medium: that depends on the stated occasions, which the theory leaves as a declared input | same: which occasions the protection covers | medium only: loss or preserved condition, by the stated occasions (high has this as OPEN, and decides it in FINDINGS) |
| O36 | 56 / 40 | same | NONE in both | NONE in both |
| O37 | 77 / 52 | same | NONE in both | NONE in both |
| O38 | 73 / 59 | same | different: high: whether an unexercised interruption is a loss. medium: whether "exposed" applies inside P | NONE in both |
| O39 | 67 / 50 | same | NONE in both | NONE in both |
| O40 | 73 / 58 | same | same: (G) when the decisive question came from outside | medium only: Origin for the robot, or shared with the expert (high has this as OPEN) |
| O41 | 83 / 56 | overlap: high treats the recorded change as a new claim at a new index; medium says the log makes the mixed provenance visible | same: whether the robot-only claim survives the outside instruction (read in different Parts) | NONE in both |
| O42 | 54 / 46 | same | high only | NONE in both |
| O43 | 56 / 42 | same | NONE in both | NONE in both |
| O44 | 57 / 44 | same | high only | NONE in both |
| O45 | 78 / 47 | same | high only | NONE in both |
| O46 | 78 / 54 | same | NONE in both | NONE in both |
| O47 | 63 / 49 | same | NONE in both | NONE in both |
| O48 | 61 / 59 | same | NONE in both | NONE in both |
| O49 | 66 / 56 | same | NONE in both | NONE in both |
| O50 | 90 / 81 | overlap: high makes the reinterpretation creative only if it is new and built by an owned subhistory; medium calls it the robot's own construction | different: high: which achievement is the content c and which the Δ. medium: each achievement against (G)'s conjuncts | same: to whom the discovery of the fault is attributed |
| O51 | 74 / 67 | same | high only | NONE in both |
| O52 | 65 / 72 | same | NONE in both | NONE in both |

## R6. Agreement is not equivalence

One medium reading that agrees with one high reading does not show that the two efforts are equivalent. The 16 rows with no difference in substance, and the 32 rows whose FINDINGS agree in substance, show that two runs agreed. They do not show that the two efforts are equivalent. Likewise, the 36 rows that differ do not show an effect of the effort (R5).

## R8. Confounds

- **The accepted high reading is the attempt that fitted.** Pass 1 of `s81_2a_mimo` also ran at high, on the same user text. Its request bodies are in the history of `returns/s81_2a_mimo.request.json`, at commits 1f37750 and 2b81a6f.
  - Pass 1 made three attempts, with `max_tokens` of 48,000, 64,000 and 64,000. Each stopped with finish "length" before any reply text, after 217,711, 283,872 and 288,727 characters of reasoning.
  - The accepted reading came on pass 2, with a limit of 131,072 tokens, after 42,679 reasoning tokens and 193,318 characters of reasoning.
  - At high, then, this text has run from 193,318 characters of reasoning to at least 288,727. The three cut-off attempts give lower bounds only. The medium control's 244,044 characters fall inside that range.
  - These are facts about the runs. They are not a measure of the effort.
- **Time.** The two calls were asked 3 hours 37 minutes apart, at 07:33:23 and 11:11:03 UTC. Both receipts name the model `mimo-v2.6-pro`. The provider's model or serving may still have changed in between.
- **Shared slots.** The control ran in the same process as pass 2 of `s81_2b_mimo_A` and `s81_2b_mimo_B`, with at most three Mimo calls in flight. The high reading ran in Stage 2a, and its receipt records nothing about slots.
- **Pass.** The high reading is the second pass of its call, after a failed first pass. The control had one pass. The output limit, temperature, thinking setting and user text were the same for both.
- **Timing of the rule.** The Mimo control had returned before the rule was written, though it had not been opened (see above).

## R4. The two Atria controls

Both Atria controls failed. Under R4, no inference about effort is drawn beyond the failures and the token usage recorded for them.

| | `s81_2b_atria_A.control-medium` | `s81_2b_atria_A.control-high` |
| --- | --- | --- |
| Effort | medium | high |
| Asked (UTC) | 11:11:03 | 11:11:03 |
| Attempts | 3, all returned (status 200), none accepted | 5: 3 returned (status 200) and none was accepted; 2 (attempts 1 and 4) ended with status 0 after 1,802.7 s and 1,802.6 s, with no finish recorded |
| Finish of the returned attempts | length, length, length | length, length, length |
| `max_tokens` of each attempt | 65,536 | 65,536 |
| Reply characters, by returned attempt | 0; 47,371; 0 | 0; 33,899; 0 |
| Reasoning characters, by returned attempt (attempt files) | 281,744; 236,415; 278,965 | 281,803; 251,721; 289,689 |
| Seconds, by attempt | 1,044.0; 1,102.4; 1,114.4 | 1,802.7; 1,067.6; 1,119.1; 1,802.6; 1,310.1 |
| Error file | status 200 after 3 attempts (3 came back but were not accepted); finish length | status 200 after 5 attempts (3 came back but were not accepted); finish length |

- **Token usage.** Neither receipt has a usage field or any token count. What they record is that every returned attempt stopped with finish "length" at its limit of 65,536 tokens.
- **Request body.** The `control-high` request body has the same sha256 as the original `s81_2b_atria_A`'s (8ad07e15…), as R3 requires.
- **What cannot be applied.** Neither control has an accepted reply. So R2 (the three-way comparison) and the replay check in R3 have nothing to read, and R7's second table is not made.
- **R8's first confound still applies.** The original was accepted on its 4th attempt, after using 64,037 of its 65,536 tokens.
