# 07 Reading of the supplementary audit, Mimo on tester A in four parts

*Written by Claude on 23 September 2026, after 17:05 UTC.*

- **The rule followed.** "The reading rule, fixed before sending" in `supplementary - Mimo on tester A in four parts/READ ME - written before sending.md`. It was written at 14:02 UTC, before any part was sent, and committed in f5f9dcb. This file follows it exactly.
- **When it was read.** Rule 1 holds no part closed until Claude's step-3 rulings are written and committed. They were: 04 in b54556e (15:09 UTC), and 06, the reading of Atria's cross-examination, in a0db21c (16:48 UTC). 06 changed no ruling, so the ruled marks compared here are 04's.
- **Parts 1 and 2 failed and support nothing (rule 5).** Rows O1 to O26 have no supplementary reading. Each is "not audited by the supplement".
- **Parts 3 and 4 were accepted.** They cover O27 to O52, one Part 1 record per row.
- **Outside the plan's table.** The table's column "2b mimo on A" stays "MISSING (failed twice)". These records are reported beside the plan's evidence and do not replace it.

**Read for this file.**
- The reading rule, in full.
- The four receipts and the two error files.
- The Part 1 records of parts 3 and 4: all 26, in full for O27, O30, O32, O35 and O50, and by their five mark fields for the rest.
- From 04: the header, sections 1 to 6, 7.6, 7.8 to 7.12, 8 and 9.
- 06, in full.
- 01's reconciled rows for the 11 rows 04 section 2.3 keeps: O28, O29, O34, O36, O42, O43, O44, O47, O49, O51 and O52.
- Tester A's 1C column of `table.md`, O27 to O52.
- The re-read of O35 and O50 (07a), in full. Spot checks of its texts: f11 L27, L419, L433 and L514, and f10 L25, with whole-file searches for "occasion" and "mostly".

**Not opened.**
- The reasoning files and truncated attempt files of every part. For parts 1 and 2 these are 12 of the 16 files committed in 392fe2d. The other four, the two receipts and the two error files, were read.
- The Part 2 lines and the Part 3 of parts 3 and 4. They are kept and not used (rule 6).
- The S87 and S88 returns folders, and Mimo's reply to the cross-examination. Mimo's reply is still to be read under 05.

---

## 1. The four parts

| part | rows | attempts (finish, seconds) | outcome | committed |
|---|---|---|---|---|
| 1 | O1–O13 | 1: content_filter, 2,066 s. 60 characters came back. The check made when the files were collected reports them as the provider's refusal notice ("The request was rejected because it was considered high risk"), with no record in it. The file was not opened here. 2: length, 2,760 s, no answer. 3: length, 2,699 s, no answer. | **FAILED.** Three answers were rejected, which is the job's `max_rejects`. | 392fe2d |
| 2 | O14–O26 | 1: length, 2,686 s. 2: length, 2,700 s. 3: length, 3,074 s. No answer in any. | **FAILED**, on the same limit. | 392fe2d |
| 3 | O27–O39 | 1: length, 2,693 s, no answer. 2: stop, 1,524 s. | **ACCEPTED** on attempt 2. It ends END OF REPORT and has 13 readable records. Its response sha256 is 21089fa2b711…, and its user sha256 is f028c1cbe704…, which matches the brief. | 57ce308 |
| 4 | O40–O52 | 1: stop, 2,223 s. It used 127,600 completion tokens, 122,728 of them reasoning, against the 131,072 ceiling. | **ACCEPTED** on attempt 1. It ends END OF REPORT and has 13 readable records. Its response sha256 is 3de8d8ae3033…, and its user sha256 is e25b7743190f…, which matches the brief. | 0af82ef |

Every part ran at medium effort, with thinking on and max_tokens 131,072. Part 4 fitted under the ceiling by 3,472 tokens. The READ ME's confound, "selection by the ceiling", applies to both accepted parts.

---

## 2. How each row was compared (rule 2)

- Each row comes from the Part 1 record of the part that lists it. Four fields are compared with Claude's ruled file-11 mark.
  - **YOUR MARK and BLIND MARK** differ when they are not the ruled mark.
  - **ON VERDICT and ON MARK** differ when the audit says AGREE with tester A where the ruled mark is not tester A's mark, or DISAGREE where it is.
- **Where the ruled file-11 marks come from.**
  - 04's ruled table gives O27, O30, O31, O32, O33, O35, O37, O38, O39, O40, O41, O45, O46, O48 and O50.
  - For O28, O29, O34, O36, O42, O43, O44, O47, O49, O51 and O52, 04 section 2.3 keeps 01's mark. It is AGREE on every one.
- Tester A's mark is its 1C mark. It matches the TESTER MARK field of every record.

---

## 3. The rows, O27 to O52

A is AGREE, S is SILENT, P is SPLIT and D is DISAGREE. ON VERDICT and ON MARK are the audit's side on tester A's mark.

| case | part | BLIND MARK | tester A (1C) | ON VERDICT | ON MARK | YOUR MARK | ruled file-11 mark (source) | fields that differ | result |
|---|---|---|---|---|---|---|---|---|---|
| O1–O26 | 1, 2 | — | — | — | — | — | — | — | **not audited by the supplement** (parts 1 and 2 failed) |
| O27 | 3 | S | S | AGREE | AGREE | S | SILENT (04) | none | agreement |
| O28 | 3 | A | A | AGREE | AGREE | A | AGREE (01; 04 §2.3) | none | agreement |
| O29 | 3 | A | A | AGREE | AGREE | A | AGREE (01; 04 §2.3) | none | agreement |
| O30 | 3 | A | S | DISAGREE | DISAGREE | A | AGREE (04) | none. Tester A differs from the ruling, and the audit takes the ruling's side. | agreement |
| O31 | 3 | A | A | AGREE | AGREE | A | AGREE (04) | none | agreement |
| O32 | 3 | A | D | DISAGREE | DISAGREE | A | AGREE (04) | none. Tester A differs from the ruling, and the audit takes the ruling's side. | agreement |
| O33 | 3 | A | A | AGREE | AGREE | A | AGREE (04) | none | agreement |
| O34 | 3 | A | A | AGREE | AGREE | A | AGREE (01; 04 §2.3) | none | agreement |
| **O35** | 3 | **D** | S | AGREE | AGREE | S | SILENT (04) | **BLIND MARK** | **re-read: the ruling stands** (section 4) |
| O36 | 3 | A | A | AGREE | AGREE | A | AGREE (01; 04 §2.3) | none | agreement |
| O37 | 3 | A | A | AGREE | AGREE | A | AGREE (04) | none | agreement |
| O38 | 3 | A | A | AGREE | AGREE | A | AGREE (04) | none | agreement |
| O39 | 3 | A | A | AGREE | AGREE | A | AGREE (04) | none | agreement |
| O40 | 4 | A | A | AGREE | AGREE | A | AGREE (04) | none | agreement |
| O41 | 4 | A | A | AGREE | AGREE | A | AGREE (04) | none | agreement |
| O42 | 4 | A | A | AGREE | AGREE | A | AGREE (01; 04 §2.3) | none | agreement |
| O43 | 4 | A | A | AGREE | AGREE | A | AGREE (01; 04 §2.3) | none | agreement |
| O44 | 4 | A | A | AGREE | AGREE | A | AGREE (01; 04 §2.3) | none | agreement |
| O45 | 4 | A | A | AGREE | AGREE | A | AGREE (04) | none | agreement |
| O46 | 4 | A | A | AGREE | AGREE | A | AGREE (04) | none | agreement |
| O47 | 4 | A | A | AGREE | AGREE | A | AGREE (01; 04 §2.3) | none | agreement |
| O48 | 4 | A | A | AGREE | AGREE | A | AGREE (04) | none | agreement |
| O49 | 4 | A | A | AGREE | AGREE | A | AGREE (01; 04 §2.3) | none | agreement |
| **O50** | 4 | **P** | S | AGREE | AGREE | S | SILENT (04) | **BLIND MARK** | **re-read: the ruling stands**, with the same-point wording clarified (section 4) |
| O51 | 4 | A | A | AGREE | AGREE | A | AGREE (01; 04 §2.3) | none | agreement |
| O52 | 4 | A | A | AGREE | AGREE | A | AGREE (01; 04 §2.3) | none | agreement |

**Counts.**
- 26 rows audited: 24 agree on all four fields, and 2 differ (O35 and O50).
- Of the 104 field comparisons, 102 match and 2 differ. Both are BLIND MARK.
- 26 rows (O1–O26) are not audited by the supplement.

**Agreement is reported as agreement (rule 4).** The 24 matching rows count as no confirmation and as no test passed. That holds on O30 and O32 too, where the audit sides with the ruling against tester A. For the record, the audit's reasons there are these:
- O30: "the case states in ordinary terms that "The robot compares the pressures itself", so the input is supplied".
- O32: "Derivation 9 bars inferring account claims from identical output projections, while the minutes here are a contemporaneous record of an event".

---

## 4. The two re-read rows (rule 3)

Both rows were re-read by Claude from the texts: file 10, file 11, the case, tester A's row and the audit's record. The re-read is kept as written in `raw readings/07a re-read O35.md`, which covers O35 and O50. It records what was read, and it checked by program that each brief's blind block for these rows is, byte for byte, Mimo's 2a return, and that the reading under audit is tester A's 1C return. So each BLIND MARK is Mimo marking the same 2a text a second time. It is not a new reading. On both rows that mark equals Mimo on B's blind mark, already listed in 04's E2 table.

### O35, "Four seconds": ruled SILENT, stays SILENT. Change: no. Away: no.

**What the audit says.** The BLIND field reads: "The tap is a protected condition and the four-second stop is a failure on an occasion the condition covers, so the protection was lost … The tap's later running does not restore the condition on the covered occasion." BLIND MARK DISAGREE. The audit's own YOUR MARK is SILENT: "The condition's wording and its occasions are declared inputs the case never states".

**What was at stake.** Suppose the blind DISAGREE held under file 11. Then O35 would be SILENT→DISAGREE, a theory change away through f11 L433 s1 (M38). Test (b) would fail, and so would the second clause. So the row was ruled on the text, not on the three agreeing fields.

**Why the ruling stands.**
1. **The DISAGREE needs two inputs the case never states.** One is the condition ("the tap runs"). The other is occasions that include the four seconds. f11 L433 s1 requires "a stated condition over stated occasions". The case names only "the protected tap".
2. **Mimo's own blind reading lists the occasions as open.** Its OPEN line asks "which occasions the protection covers and whether seconds in which nobody draws are among them".
3. **Neither file sets a default occasion.** "occasion" appears only at f11 L433 and L514. "At all times", "interrupt" and "draw" appear in neither file. O38 is AGREE because its case states "the kitchen tap runs at all times during the work".
4. **f11 L514 forbids supplying a missing input in either direction.** It reads: "where the input is missing, the verdict is unsettled and the semantics says so rather than choosing the input from the verdict wanted". Mark rule 4 then gives SILENT.
5. **The blind reading misapplies L433 s3.** "Losses outside \(P\) must be exposed" does not make the absence of a draw a loss. The interruption "is on the record" whichever way the input falls.

**The ruling after the re-read.**
- File 10 SILENT, file 11 SILENT.
- Verdict SAME on the same point: whether the protected condition held, and whether the stop is a loss.
- Passage CHANGED (additive), f11 L433 s1 and L514. Direction none. Kind: no change.

**File 10 is untouched.** It is SILENT by the plan's rule, because both 1K returns match the baseline. It is SILENT on the text as well: f10 L438, L441, L122 and L164.

### O50, "The same afternoon, three achievements": ruled SILENT, stays SILENT. Change: no. Away: no.

**What the audit says.** The BLIND field reads: "… the blind reading found the discovery attribution split between the robot's inner processes and the expert's outside contribution." BLIND MARK SPLIT. The audit's own YOUR MARK is SILENT. Its reason is that "mostly the expert's" and the "one word wrong for at least two" claim "both turn on a weighting the theory does not supply".

**What was at stake.** Suppose the discovery point were SPLIT under file 11. Then the row would be SILENT→SPLIT, a verdict CHANGED through f11 L419 s2 (M37) and L465 s2.
- The plan ranks SILENT and SPLIT level, so the change would not be away, and test (b) would not turn on it.
- It would add a P2 exception, by an undeclared CLAIM that no case shows harmful. The second clause names that kind of failure.

**Why the ruling stands.** 04b recorded this blind SPLIT as evidence but did not argue it as a contrary. The re-read argues it.
1. **The two sentences the SPLIT cites are not two readings.** They are complementary clauses of one rule. f11 L419 s2 keeps the expert's proposal "an outside contribution however it is executed inside". It makes the robot's rerun and finding "the system's own today whoever wrote it". L465 s2 repeats the second clause. Each clause classifies a different contribution, and no choice between them is left open.
2. **The point names the processes.** The verdict says "The discovery was the robot's: it ran the test and found the fault". The situation says "the robot does it and finds the third fault".
3. **The proposal keeps its provenance, and the new work is the robot's.** The witness "identifies … the incoming carriers" (f11 L401 s2), and "the rest of the content keeps its inherited provenance" (L401 s5). The theory's finding is the fixed finding with a qualification: the swap it ran remains the expert's.
4. **Credit is per achievement.** Origin is indexed to the content (f11 L417 = f10 L430), and L433 s5 keeps "three different attributions" apart. The verdict already credits the proposal to the reinterpretation and to the inquiry.
5. **The 2a's doubt is not a doubt about the theory.** Its doubt is about which content the case's word "discovery" names, and mark rule 3 does not cover that: rule 3 needs the theory's sentences to support two readings. The verdict itself settles the content.
6. **On a strict boundary reading the mark would still be SILENT.** With the system boundary taken as undeclared (f11 L514), the discovery point would be unsettled, which is SILENT, not SPLIT.

**The ruling after the re-read.**
- File 10 SILENT, file 11 SILENT.
- Verdict SAME on the same point: the weighting behind "The inquiry was mostly the expert's".
- Passage SAME: the shared disclaimer, f10 L25 / f11 L27. Direction none. Kind: no change.

**One clarification, recorded after the audit.** The same missing weighting also carries the verdict's last sentence: "One word for all three would be wrong for at least two of them".
- The reinterpretation is joint and the discovery is the robot's. So any one word is wrong for at least one achievement.
- "At least two" also needs the inquiry not to be simply joint, and that is the weighting "mostly" needs.
- This narrows 01's "Every other point is reached". The same-point label now reads: the weighting that "The inquiry was mostly the expert's" needs, which also carries the last sentence's "at least two".
- It changes no mark, verdict, passage label or count. Under 04's words, "a clarification is not a changed verdict".

---

## 5. Changes of ruling

- **None.** No mark, verdict, passage, direction or kind changed on any row.
- **One clarification.** O50's same-point wording now also names the "at least two" of the verdict's last sentence (section 4). It is not a change of ruling.
- **04's counts stand.**
  - File 10: AGREE 44, SILENT 6, SPLIT 1, DISAGREE 1.
  - File 11: AGREE 46, SILENT 6.
  - Verdicts: 50 SAME, 2 CHANGED (O45 and O48, both toward).
  - Passages: 20 CHANGED.

---

## 6. Theory change away, test (b) and the clauses

- **No change was made, so none is a theory change away.** Test (b) needs no re-application. It holds as 04 section 5(b) and 06 section 6 state it: no ruled file-11 mark lies further from AGREE than its ruled file-10 mark. O35, the row test (b) turned on, stays SILENT→SILENT on the same point.
- **What the re-reads settle.**
  - The only reading in the supplement that would have been away is O35's blind DISAGREE, and it fails on the text.
  - O50's blind SPLIT would not have been away even if it had held.
- **Tests.** (a), (b), (c) and (d) HOLD.
- **Predictions.** P1 HOLDS. P2 FAILS, at O45 alone, by a theory change toward. P3 FAILS, only by undeclared CLAIM places, none shown harmful.
- **Clauses.** The first does not apply, and the third does not apply. The second applies, as in 04 and 06.

> **THE STANDING VERDICT AFTER THE SUPPLEMENTARY AUDIT:** File 11 stands as the authority under the plan's second clause, with the same findings recorded against its frozen note as 04 and 06 list (P3's 41 undeclared CLAIM places inside the theory, none shown harmful; P2's failure at O45, a theory change toward the thoughtful person; the three S75 corrections; the seven errata), and the supplementary audit changes no ruling.

---

## 7. What the supplement does not restore, and findings about the reader

**Not restored (04 section 7.6).**
- A second outside audit of tester A on O1 to O26.
- The crossed design on those rows.
- The fourth pair of the E2 substitute. The supplement covers 26 of 52 rows, stands outside the table, and the rule does not use it for E2.
- Mimo's Part 3 lists on tester A's whole return. Each part's Part 3 covers only what that part noticed, and the rule does not use them.

**Findings about the reader.** These count neither for nor against file 11.
- **Mimo's blind marks are stable where Atria's were not (04 section 7.10).** On O35 and O50, Mimo's BLIND MARK on the same 2a text is the same in both of its audits: DISAGREE and SPLIT. Only these two rows were compared.
- **Mimo moves to the ruled mark after reading the tester.** In both audits, on both rows, Mimo went from its blind mark to the ruled SILENT once it had read the tester's row.
- **Parts 1 and 2 both failed at medium effort**, as the plan's single call had failed on both of its passes. Part 1's first attempt ended on a content filter, and the other five failed attempts ran to the 131,072-token ceiling. On the rows O1 to O26, Mimo's audit of tester A did not finish at this ceiling in any form tried.

**Still open.**
- Mimo's reply to the cross-examination. It is read on its own under 05, and nothing from it was opened for this file.
- S81 Results, which carries the determination as it stands after both cross-examination replies and this reading.

---

## 8. Files

- This file.
- `raw readings/07a re-read O35.md`: the re-read of O35 and O50, copied unchanged from the working file. It was written at about 17:05 UTC with the branch head at 392fe2d, before this file.
