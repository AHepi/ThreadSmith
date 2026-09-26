# S81 Results - file 11 against file 10, determined

*Written by Claude on 23 September 2026, and completed on 24 September 2026 when the last reading was written, under log S87, from Claude's determination in `S81 File 11 against every case - outputs/determination/` (files 01 to 05 and their raw readings), which stays there unchanged. The round keeps its name, S81; its write-up's log entry is S87 (plan, third version, change j). "The plan" is the S81 plan in `tests/`: its second version, which governs, read with `S81 Plan - third version, the changes made after the second version was frozen.md`, which records what changed after the second was frozen. Decision S13: "you are the authority, not Mimo or Atria. You make the big decisions." This file carries the determination (04) and what the later readings did to it: Atria's cross-examination (06), Mimo's cross-examination in three parts, of which one came back (08), Mimo's retry of the failed part's rows one per call (09 for O17; 10 for O5 and O30, with every reading set side by side), the supplementary audit of Mimo on tester A (07), and the effort controls, each read under a rule written and committed before it was opened, except the controls' rule, which is recorded below as late. None of them changed a ruling. Every reading is now written, and this file is final.*

## The question the round froze

Whether file 11 (revision 1, log S76), read bare, gives on all 52 outside cases the verdicts file 10 gives, except on O48, where it was written to give the thoughtful person's; and whether it differs from file 10 in claim only where its note says (Derivation 3 and the three sentences that restated it). The prediction was frozen in the plan and kept out of every call:

- **P1, the one change.** O48 is DISAGREE under file 10 and AGREE under file 11, on the qualified claim of Derivation 3 or one of the three sentences restated with it: CHANGED toward the thoughtful person, in verdict and in passage.
- **P2, nothing else.** Every other case keeps its baseline mark under file 11: forty-three AGREE, the same eight SILENT, and no DISAGREE, SPLIT or CASE DISPUTED that file 10 does not also give.
- **P3, the claim count.** The places Claude rules CLAIM are Derivation 3 and its three sentences; every other place is WORDING or ORDER. Named against it before the run: the Part XI occasions clause and the Part XIV Declared inputs paragraph.
- **P4, the instrument** (a claim about the readers). Within each tester, the 1K and 1C marks differ on O48 and on no other case.
- **E1**, at least one tester marks the occasions clause CLAIM in 1D; **E2**, a reader's blind reading differs from its own 1C more than its 1K and 1C differ.

The baseline, S75's determination from the S72 table as audited: DISAGREE on O48; SILENT on O1, O12, O20, O21, O27, O35, O40 and O50; AGREE on the other forty-three. File 11 stands, on Claude's determination, when (a) O48 is AGREE under file 11; (b) no case shows a theory change away from the thoughtful person; (c) no sentence of file 11 is ruled to give a wrong verdict where file 10's corresponding sentence gave the thoughtful person's; (d) no cross-reference in file 11 points wrong in a way that changes what a sentence claims.

## How it was run

- **Stage 1, testing.** Six fresh Claude subagents, each alone in a fresh folder holding one brief: testers A and B, each with 1C (file 11 against every case), 1K (the same brief on file 10, a control arm the tester cannot tell apart) and 1D (every difference between the two files). These are the rerun of decision S16 (log S83 (a)); the first six returns are kept as a comparison and are not evidence here.
- **Stage 2, audit.** Atria and Mimo, one prompt in and one answer out, thinking on, temperature 0.7, each at its output ceiling (Mimo 131,072 tokens, Atria 65,536). 2a, a blind reading of all 52 cases with the fixed verdicts withheld, by both, at high effort. 2D, a difference audit by each (Atria with tester A's list under audit, Mimo with B's). 2b, an open audit of each tester's 1C by each auditor, fully crossed: Atria on A at high; Atria on B and Mimo on B at medium (decision S17, pass 2); Mimo on A failed on both allowed passes and is missing.
- **The samples.** The mandatory rules M1 to M6 left three rows for tester A and two for tester B, so the residual draw R took those rows and not ten. Each sample covers all 52 rows (plan, third version, change i).
- **The determination.** Two independent Claude readers ruled every case and every difference from the texts alone, and a Claude reconciler merged them (01, 02), before any return was opened. Step 4 ruled every difference after reading the 1D lists and 2D audits (03). The table was built by program. Four Claude determiners ruled the 33 rows the plan's step 3 names, each starting from 01; two Claude verifiers tried to overturn them, one from the texts and one on the plan's rules; Claude assembled the result (04).

## What came back, and whether it did as instructed

- **1C and 1K, both testers.** Each is complete: a record with a MARK for every case O1 to O52 and the closing line. Each counts "CASE DISPUTED: 0 - none". Every transcript is clean; each return's only void hits were the word "prediction", which the theory and the case book use themselves, read and cleared by the orchestrator with the reason in the receipt. Every 1C quotation was found in file 11 by program: tester A 92 verbatim, 0 loose, 0 absent; tester B 86, 0, 0.
- **1D.** Tester A 68 records (55 CLAIM, 13 WORDING); tester B 72 (52 CLAIM, 20 WORDING). Both report "Cross-references in Text B: WRONG 0".
- **2a.** Both accepted, Atria at the plan's 48,000 and Mimo on its second pass at 131,072 after three empty attempts at 64,000 (lesson S11).
- **2D.** Atria 107 records and none added; Mimo 107 records and one added (ruled ORDER).
- **2b.** Three accepted: each audits all 52 rows in Part 1, leaves Part 2 empty, and counts "Cases to rule on" at 0. The fourth, Mimo on A, is MISSING (below).

Did they do as instructed: yes, on every check the plan names, for every accepted return. The one call that did not return is Mimo on tester A.

## The order of work

| when (UTC) | what | commit |
|---|---|---|
| 11:34 | the plan's third version, written at 11:33 before any pass-2 return | 24d2d75 |
| 12:21 | **01 and 02**: Claude's rulings on every case, and Claude's reading of the differences, from the texts alone | **2788a77** |
| 13:22 | **03**: step 4, every difference ruled, after the 1D lists and 2D audits and before any 1C, 1K, 2a or 2b return was opened | **0aedc9c** |
| 13:43 | the pass-2 2b returns and the effort controls, collected | 6106e7d |
| 14:07 | `table.md`, built by program | **69e8b1a** |
| 15:09 | **04**: step 3, the verifications and the determination | b54556e |
| 15:27 | the cross-examination brief, with its reading rule (05) committed before sending | a2c5e36 |
| 15:29 | the cross-examination requests, as sent | 4c891ce |
| 15:37 | the supplementary audit's part 3, as returned (unopened) | 57ce308 |
| 16:09 | the supplementary audit's part 4, as returned (unopened) | 0af82ef |
| 16:17 | the effort controls read, by their rule | 941b207 |
| 16:41 | Atria's cross-examination, as returned | 396a321 |
| 16:48 | **06**: the reading of Atria's cross-examination | a0db21c |
| 16:55 | the supplementary audit's parts 1 and 2, failed | 392fe2d |
| 17:08 | **07**: the reading of the supplementary audit, after 04 and 06 were committed | 1ef2ce4 |
| 19:17 | **05b** and the three part texts for Mimo, before sending, in case the single call failed | 6a9f75c |
| 19:26 | Mimo's single cross-examination call, failed | e123397 |
| 19:28 | the three part requests, as sent | 8bfefc1 |
| 22:19 | the three parts as returned: P2 accepted, P1 and P3 failed | e373275 |
| 22:23 | **08**: the reading of Mimo's cross-examination in three parts | 76cceac |
| 22:32 | **05c** and the three one-row retry texts, before sending | ff36cd4 |
| 22:35 | the retry launched, its requests as written | 2155d0f |
| 23:32 | the O17 retry as returned (it came back at 23:26, before the container restarted at about 23:30) | c137e86 |
| 23:41 | the O5 and O30 retries, failed on the dead proxy after the restart, as recorded | 1feb425 |
| 23:45 | the rerun note and job list, written before sending: O5 and O30 go again as pass 2 | 57482a5 |
| 23:46 | pass 2 launched, its requests byte-identical to pass 1's | faf91f6 |
| 23:59 | **09**: the reading of Mimo's retry of O17 | 8263ff9 |
| 01:58 (24 September) | the O5 and O30 pass-2 replies, as returned | 286d69c |
| 03:15 (24 September) | **10**: the reading of Mimo's retry of O5 and O30, and every reading set side by side | 3deee3e |

What the history proves: the pre-return rulings (2788a77) and the step-4 rulings (0aedc9c) are older than the table (69e8b1a) and than the pass-2 returns (6106e7d); every reading after the determination (06, 07, 08, 09, 10) is younger than the rule it follows (05, the supplementary READ ME, 05b, 05c and, for O5 and O30, the rerun note). What it does not prove by itself: the Stage 1, 2a, 2D and first 2b returns were already in the repository when 2788a77 was written, having been committed on the earlier session's branch; that no reader opened them rests on each file's own record of what its writer opened and saw by name only.

## The result

> **THE STANDING VERDICT: File 11 stands as the authority under the plan's second clause, with P3's 41 undeclared CLAIM places inside the theory (none shown harmful by any case), P2's failure at O45 (a theory change toward the thoughtful person), the three S75 corrections and the seven errata recorded against its frozen note in S81 Results.**

This is the determination's verdict (04). Atria's cross-examination upheld it; Mimo's accepted part upheld its two rows, and its retry left O5, O30 and O17 standing, O5 after a fresh determiner re-read it on Mimo's RULING FALLS; the supplementary audit changed no ruling (below). So it is also the verdict after every reading. In the plan's words, the clause that applies: "With (a) to (d), and P2 or P3 failing only by a theory change toward the thoughtful person or by an undeclared CLAIM that no case shows harmful, file 11 stands with those findings recorded against its note; the note is frozen, so the correction lives in S81 Results, and in a revision 2 if the owner asks for one." This file is that record.

- **Tests:** (a) HOLDS, (b) HOLDS, (c) HOLDS, (d) HOLDS.
- **Ruled marks over all 52 cases.** File 10: AGREE 44, SILENT 6, SPLIT 1, DISAGREE 1. File 11: AGREE 46, SILENT 6, no SPLIT, DISAGREE or CASE DISPUTED.
- **Verdicts CHANGED: 2,** O45 and O48, both toward the thoughtful person, both theory changes. None away. Reader variation: none.
- **S75 corrections: 3** (O20, O40, O45); one declined (O15). **CASE DISPUTED: none.**

## Predictions and expectations

| | result | count and rows |
|---|---|---|
| **P1**, the one change | **HOLDS** | O48: file 10 DISAGREE on the unqualified claim (f10 L569, with L38's "*always*" and L539's "This refutes Derivation 3."); file 11 AGREE on the qualified claim, f11 L562 s2–s3 ("The presence of an unseen pair alone does not establish that such a \(t'\) exists; it must be admitted, realizable, a member of \(\mathcal T\), and a survivor of \(H\)."), restated at L534 and L43. Verdict CHANGED, passage CHANGED (alteration), toward, theory change. All five file-11 readings AGREE. Every file-11 reader also cites the undeclared population sentence f11 L473; it applies the change to the case's words and cannot carry it alone. Neither 1K return marks AGREE (A DISAGREE, B SPLIT), so the plan's clause on a file-10 AGREE is not triggered. |
| **P2**, nothing else | **FAILS**, only by a theory change toward the thoughtful person | On the reading adopted after the data (below): one exception, O45, SPLIT under file 10 (corrected) and AGREE under file 11, through f11 L309 s3's first clause, "A route already present in the candidate is a route whether or not anyone has described its work" (step 4's M28, an undeclared CLAIM no case shows harmful). On the frozen reading: two exceptions, O20 and O40, each an error in S75's baseline and not a change between the files. Either way, none is away and none is reader variation. File 11 gives no DISAGREE, SPLIT or CASE DISPUTED on any case. |
| **P3**, the claim count | **FAILS**, only by undeclared CLAIMs no case shows harmful | Derivation 3 (M53 to M56), the answer to grievance 3 (M8) and attack point (D) with the Part XV entry (M52) are CLAIM, as expected. Both named places are CLAIM: the occasions clause (M38, f11 L433 s1) and the Declared inputs paragraph (M48, f11 L514). In all, 43 CLAIM places lie beyond Derivation 3 and its three sentences: 41 inside the theory (40 distinct changes) and 2 meta (the note, M1; the front-matter reading rule, M7). The note's "Nothing else changes in what is claimed" (f11 L5) is false against the 41. None is shown harmful by any case (the one conditional harm, M38 with M48 on O35, fell away when O35's file-10 mark was ruled SILENT). |
| **P4**, the instrument | **FAILS** for both testers | Tester A's 1K and 1C marks differ on 10 cases (O4, O5, O17, O18, O30, O31, O32, O41, O45, O48); tester B's on 12 (O1, O5, O15, O18, O31, O32, O38, O39, O45, O46, O48, O50). O48 is in both; neither set is O48 alone. On Claude's ruled marks only O45 and O48 differ between the files, so the rest are differences between two readings by one tester. |
| **E1** | **HOLDS** | 2 of 2 testers mark the occasions clause CLAIM in 1D (A's D47, B's D47); neither marks it WORDING, and both 2D audits agree. |
| **E2** | **Not scorable as written** | No reader now writes both a 2a and a 1C. The substitute the plan fixed before any return is below, marked "not E2". |

**Not E2.** Each auditor's BLIND MARK (its 2a reading as marked in its own 2b) against the audited tester's 1C mark, row by row over all 52 rows, beside the count of rows where that tester's 1K and 1C differ. It mixes seeing the fixed verdict with a change of family, carries the effort confound, and scores no expectation.

| auditor on tester | effort | blind mark differs from the tester's 1C | rows | the tester's 1K differs from its 1C |
|---|---|---|---|---|
| Atria on A | high | 7 | O8, O10, O13, O15, O30, O32, O33 | 10 |
| Atria on B | medium | 8 | O5, O13, O21, O27, O30, O33, O40, O50 | 12 |
| Mimo on B | medium | 6 | O1, O4, O10, O19, O35, O50 | 12 |
| Mimo on A | — | MISSING (failed twice) | — | 10 |

On all three counted pairs the blind-against-1C count is the lower (7 < 10, 8 < 12, 6 < 12). Atria's blind marks from one 2a text differ between its two audits on O5, O10, O17, O27 and O40.

## The ruled table

**The 33 rows of step 3.** A is AGREE, S SILENT, P SPLIT, D DISAGREE. 2b Mimo on A is MISSING on every row. "Base" is S75's baseline. "f10 L438" is a line of file 10 and "f11 L433 s1" the first sentence of a line of file 11. Each ruling is argued in full, with its evidence and strongest contrary, in `determination/raw readings/04b rulings - O1 group.md` to `- O4 group.md`.

| case | readings: 1K A, 1K B · 1C A, 1C B · 2b Atria on A (high), Atria on B (medium), Mimo on B (medium) | file-10 mark | file-11 mark | verdict | passage the file-11 verdict rests on | direction | kind |
|---|---|---|---|---|---|---|---|
| O1 The forecaster who keeps finding honest limits | S D · S S · S S S | SILENT (base) | SILENT | SAME (same point: "the series as a whole is a retreat") | CHANGED (additive): f11 L161 s3, L514 | — | no change |
| O2 The tide table with a real bell attached | A A · A A · A A A | AGREE (base) | AGREE | SAME | SAME: f11 L257, L255 = f10 L270, L268; L275 s2 *application* | — | no change |
| O3 Nadia and the cards she has never seen | A A · A A · A A A | AGREE (base) | AGREE | SAME | SAME: Build, f11 L401 s1, s3, and the construction response, L227 (= f10 L414, L240); L401 s4 *application* | — | no change |
| O4 Dormitive power, with a meter | P A · A A · A A A | AGREE (base) | AGREE | SAME | SAME: shared f11 L126, L111, L153 s4, L257, L259; L129 s4–s5 and L153 last *application* | — | no change |
| O5 Greta's dough | A A · S S · S A S | AGREE (base) | AGREE | SAME | CHANGED (additive): f11 L161 s3, L514 | — | no change |
| O8 Petra's own ovens | A A · A A · A A A | AGREE (base) | AGREE | SAME | SAME: f11 L161 s1–s2 (ORDER of f10 L41, L272 s2) | — | no change |
| O10 Two thermostats | A S · A S · A S S | AGREE (base) | AGREE | SAME | SAME: f11 L93, L105, L111, L121 (= f10 L108, L120, L126; L136 in other words) | — | no change |
| O12 The rota | S S · S S · S S S | SILENT (base) | SILENT | SAME (same point: "a better question, and its merit is real") | SAME: the merit disclaimer, f10 L25 / f11 L27 s1; L582 last *application* | — | no change |
| O13 Two plumbers | A A · A A · A A A | AGREE (base) | AGREE | SAME | SAME: f11 L433 s5, *application* of f10 (P) and (EK) | — | no change |
| O14 The phrasebook | A A · A A · A A A | AGREE (base) | AGREE | SAME | SAME: f11 L399 s4, *application* of f10 L412, L476, L496 | — | no change |
| O15 Sam's inherited marks | P P · P A · A A A | AGREE (base; correction declined) | AGREE | SAME | SAME: f11 L401 s2–s3, L393, L371 s2 (= f10 L414, L406, L384) | — | no change |
| O16 The worn key and the diary | A A · A A · A A A | AGREE (base) | AGREE | SAME | CHANGED (additive): f11 L213 last, L393 last | — | no change |
| O17 The robot's log and the maker's manual | A A · S A · S A A | AGREE (base) | AGREE | SAME | CHANGED (additive): f11 L467 last, L419 s1 | — | no change |
| O18 The one tooth | P D · A A · A A A | AGREE (base, by rule; Claude's reading SPLIT) | AGREE | SAME | CHANGED (additive): f11 L401 s5 | — | no change |
| O19 The diagram in his hand | A A · A A · A A A | AGREE (base) | AGREE | SAME | SAME: f11 L371 s2 (= f10 L384); L371 s3 applies it | — | no change |
| O20 Two valves in one second | A A · A A · A A A | **AGREE (S75 corrected from SILENT)** | AGREE | SAME | CHANGED (additive): f11 L433 s4 | — | no change |
| O21 The expert's question | S S · S S · S A S | SILENT (base) | SILENT | SAME (same point: "mostly the expert's") | SAME: the disclaimer, f10 L25 / f11 L27 | — | no change |
| O24 The unused joint setting | A A · A A · A A A | AGREE (base) | AGREE | SAME | SAME: f11 L558, L259 s2 (= f10 L565, L272 s2) | — | no change |
| O27 The test that fitted neither | S S · S S · S A S | SILENT (base) | SILENT | SAME (same point: "mostly the robot's") | SAME: the disclaimer, f10 L25 / f11 L27 | — | no change |
| O30 The routine uploaded that morning | A A · S A · S P A | AGREE (base) | AGREE | SAME | CHANGED (additive): f11 L419 s2, L465 | — | no change |
| O31 The wrong valve | P D · A A · A A A | AGREE (base) | AGREE | SAME | CHANGED (additive): f11 L401 s5 | — | no change |
| O32 Found aloud, drawn later | A S · D A · A A A | AGREE (base) | AGREE | SAME | SAME: f11 L393 s1, L512 (= f10 L406 s1, L521) | — | no change |
| O33 The table with empty columns | A A · A A · A A A | AGREE (base) | AGREE | SAME | SAME: f11 L153 s1 (= f10 L168 s1) | — | no change |
| O35 Four seconds | S S · S S · S S S | SILENT (base) | SILENT | SAME (same point: whether the protected condition held, and whether the stop is a loss) | CHANGED (additive): f11 L433 s1, L514 | — | no change |
| O37 The uncited textbook | A A · A A · A A A | AGREE (base) | AGREE | SAME | CHANGED (additive): f11 L518 last | — | no change |
| O38 Written on the job sheet | A P · A A · A A A | AGREE (base) | AGREE | SAME | CHANGED (additive): f11 L433 s1 | — | no change |
| O39 Two routes, both running | A P · A A · A A A | AGREE (base) | AGREE | SAME | CHANGED (additive): f11 L433 s4 | — | no change |
| O40 Two hands on the test | A A · A A · A A A | **AGREE (S75 corrected from SILENT)** | AGREE | SAME | CHANGED (additive): f11 L419 s2, L433 s4 for "theirs together"; the "mostly" point on the shared disclaimer | — | no change |
| O41 The technician's whisper | P A · A A · A A A | AGREE (base, by rule; Claude's reading SPLIT) | AGREE | SAME | CHANGED (additive): f11 L419 s2, L465 last | — | no change |
| O45 The spring nobody mentioned | P P · A A · A A A | **SPLIT (S75 corrected from AGREE)** | AGREE | **CHANGED** | CHANGED: f11 L309 s3, first clause (step 4 M28, undeclared CLAIM) | **toward** | **theory change** |
| O46 The cable that used to be a spring | A S · A A · A A A | AGREE (base) | AGREE | SAME | SAME: f11 L309 s3, second clause, applies f10 L246, L204, L304 | — | no change |
| O48 The forbidden wire | D P · A A · A A A | DISAGREE (base) | AGREE | **CHANGED** | CHANGED (alteration): f11 L562 s2–s3 against f10 L569; L534 and L43 restate it | **toward** | **theory change** |
| O50 The same afternoon, three achievements | S S · S D · S A S | SILENT (base) | SILENT | SAME (same point: "The inquiry was mostly the expert's") | SAME: the disclaimer, f10 L25 / f11 L27 | — | no change |

**The other 19 rows** (O6, O7, O9, O11, O22, O23, O25, O26, O28, O29, O34, O36, O42, O43, O44, O47, O49, O51, O52): AGREE (base) under file 10, AGREE under file 11, verdict SAME, no change. On each, every reading in `table.md` is AGREE (both 1K, both 1C, every audit mark and every blind mark), and Claude's pre-ruling (01) is AGREE in both files. The passage is 01's: CHANGED (additive) on O26, O42, O49 and O51, SAME on the other fifteen.

**Counts over all 52 cases.**

| | AGREE | SILENT | SPLIT | DISAGREE | CASE DISPUTED |
|---|---|---|---|---|---|
| file 10, ruled | 44 | 6: O1, O12, O21, O27, O35, O50 | 1: O45 | 1: O48 | 0 |
| file 11, ruled | 46 | 6: O1, O12, O21, O27, O35, O50 | 0 | 0 | 0 |

Verdicts: 50 SAME, 2 CHANGED (O45, O48), both toward, both theory changes; 0 away; 0 reader variation. Passages: 20 CHANGED (O48's an alteration, the rest additive) and 32 SAME. The six SILENT rows are SILENT in both files on the same point.

## Rulings on the disputed rows

Every row where the readings split, where a reading departs from the baseline, or where Claude's ruling departs from its own pre-ruling.

*Of the seven rows pressed in the cross-examination, Atria's reply leaves every ruling standing; Mimo's accepted part leaves O35 and O40 standing, and its retry leaves O17 and O30 standing and says O5 falls, which a fresh determiner re-read from the texts and upheld; O48 and O45 were in Mimo's failed part P3 and have Atria's reading only (below).*

- **O48, the forbidden wire.** P1, above. Upheld by both verifications.
- **O45, the spring nobody mentioned.** File 10 SPLIT, corrected from S75's AGREE: file 10 gives a candidate "an identified set \(\Gamma\) of active commitments" (f10 L246) and separates commitments from "named background" (f10 L304), and never says how \(\Gamma\) is identified, so whether an undescribed, connected spring "was already a route" is open. Both 1K returns mark SPLIT at that point, and step 4 (written before any 1K return was opened) had found it open. File 11 closes it (f11 L309 s3). A theory change toward. It holds if "active" in f10 L246 is not a matter of fact, which the cross-examination was asked to press.
- **O35, four seconds.** SILENT under both files, on the same point: whether the protected condition held, and so whether the stop is a loss. File 10's mark is set by the plan's rule (both 1K returns SILENT, which is the baseline) and is SILENT on the text as well: (P) evaluates protected obligations "fixed for the comparison" (f10 L438), and the case states no condition. File 11 is SILENT on the occasions clause and the Declared inputs paragraph (f11 L433 s1, L514). Claude's pre-ruling had file 10 AGREE, on an endpoint reading of (P) that file 10 does not state; that reading was given up after the 1K returns were opened, and is recorded as such. The counted mark does not depend on it. On the pre-ruling, O35 would have been a theory change away and test (b) would have failed. The supplementary audit's blind DISAGREE under file 11 was re-read from the texts and fails (07): it needs a stated condition and stated occasions that the case does not give, and f11 L514 forbids supplying a missing input either way.
- **O5, Greta's dough; O30, the routine uploaded that morning; O17, the robot's log and the maker's manual.** File-11 AGREE on each, against part of the readers. A file-11 SILENT on any of them would have been a change away through new sentences, and test (b) would have failed. O5: four of five file-11 readings SILENT on f11 L161 s3 ("the semantics records the restriction and supplies no rule that certifies it"); ruled AGREE because Greta's account states the ground of her limit and f11 L514 makes "what makes a restriction appropriate" a stated input on which the verdict is given. O30: two SILENT and one SPLIT of five, for want of a boundary declared in words; ruled AGREE because the situation names the system ("The robot compares the pressures itself") and f11 L419 s2 gives "a process that runs inside the boundary is the system's own today whoever wrote it". O17: two of five SILENT on the same ground; ruled AGREE on f11 L467 ("Ownership is grounded in the processes and resources the boundary includes, never in the capability being attributed"). Upheld by both verifications, O5 and O30 at medium confidence. After the cross-examination: Atria said RULING STANDS on all three; Mimo's retry said RULING STANDS on O17 and O30, and "RULING FALLS — file 11 SILENT" on O5, which a fresh determiner re-read from the texts and upheld at medium confidence (10a; below). No ruling changed.
- **O40, two hands on the test.** File 10 AGREE, corrected from S75's SILENT; file 11 AGREE; no change. The one conflict between the verifications (text lens UNCERTAIN, rule lens UPHELD), ruled by Claude from the texts: "Neither can say 'mostly'" is about what either party can assert; file 10 counts "a ranking of thinkers" among what it does not supply and "marks those places as empty" (f10 L25), so neither party has a ground for "mostly"; file 11 reaches the same point by the same route (f11 L27 s2–s3). A verdict that denies a claim is reached when the input that would warrant it is absent; a verdict that asserts what the input would decide (O21, O27, O50) is not. Every reading of O40 gives no change or a change toward, so no test turns on it. A note for revision 2: its entry W6.1 rewrites f11 L27 s2, so in the drafts that sentence no longer says what this ruling cites it for; the ruling's other grounds carry O40 without it (the change list's "Findings carried forward"). The ruling on file 11 as it stands is unaffected.
- **O20, two valves in one second.** File 10 AGREE, corrected from S75's SILENT: every point of the verdict is reached without a definition of ProducedBy ("each is contributory, neither indispensable", f10 L324; "missing evidence stays missing", f10 L406); S72's SILENT was on a further allocation the verdict does not claim. File 11 AGREE on f11 L433 s4.
- **O21, the expert's question; O27, the test that fitted neither; O50, the same afternoon, three achievements.** SILENT in both files on "mostly": the step from "the only construction is X's" to "mostly X's" needs a premise that credit goes with the originative part, and neither file states it (f10 L25; f11 L27 s3, "It does not supply a division of credit among contributors beyond what a history establishes"). Claude's pre-ruling had both files AGREE on O21 and O27; it changed on reading, and the rule gives SILENT in any case. On O50, tester B's 1C DISAGREE on the discovery (through f11 L419 s2, L433 s4) fails: credit is per achievement, and the discovery point is reached. After the supplementary audit (07), O50's same point reads: the weighting that "The inquiry was mostly the expert's" needs, which also carries the verdict's last sentence, "One word for all three would be wrong for at least two of them". A clarification; no mark, verdict, passage or count changes.
- **O1, the forecaster who keeps finding honest limits.** SILENT in both files on the same point ("the series as a whole is a retreat"); tester B's 1K DISAGREE is not followed. File 11's L514 now names the input the case lacks ("what makes a restriction appropriate").
- **O12, the rota.** SILENT in both files on "its merit is real"; the standard of worth is the normative relation, primitive 2, which L514 leaves out by design.
- **O15, Sam's inherited marks.** AGREE in both. Both 1K returns mark SPLIT, but on different points of the verdict ("his account of his own work" and "his account"), so Claude's reading does not confirm them and the correction is declined. Tester A's 1C SPLIT through f11 L213 fails: both readings put the hole in the record.
- **O18, the one tooth; O41, the technician's whisper.** AGREE in both by the plan's rule. Claude's reading of file 10 is SPLIT on each, but the 1K returns do not agree on a different mark (O18: SPLIT and DISAGREE; O41: SPLIT and AGREE), so the baseline stands. Each would otherwise be a theory change toward (through f11 L401 s5, and f11 L419 s2 with L465). The rule withholds a count in file 11's favour; recorded as findings about S75.
- **O37, the uncited textbook.** AGREE in both. Claude's pre-ruling had file 10 SPLIT; on reading, file 10's receipts are indexed to their user (\(P_j\), f10 L406), so an uncited proof is not among the account's receipts.
- **O10, two thermostats.** AGREE in both. Every blind reading and three of five file-11 marks are not AGREE, on sentences both files carry; tester B is SILENT in both arms. A reading hazard in shared text, not a change.
- **O4, O31, O32, O38, O39, O46.** AGREE in both, with 1K marks that differ from S72 (O4 A SPLIT; O31 A SPLIT, B DISAGREE; O32 B SILENT; O38 B SPLIT; O39 B SPLIT; O46 B SILENT) and, on O32, tester A's 1C DISAGREE, which rests chiefly on a sentence the two files share (f11 L606 = f10 L613). None is confirmed on the text.
- **O8, O13, O19, O33.** AGREE in both. Blind departures that fail on the text: O13, Atria's blind DISAGREE through f11 L433 s4, answered by f11 L371 and the case's "Before she can replace it"; O19, Mimo's blind SPLIT through f11 L309 s3, which says nothing about whether a route did work; O33, Atria's blind DISAGREE on f11 L259, which file 10 carries word for word; O8, Atria's blind SILENT, against a verdict both files reach (f11 L161 s1–s2 restates f10 L41 and L272).

## Tests (a) to (d)

- **(a) HOLDS.** O48 is AGREE under file 11 (P1).
- **(b) HOLDS.** No ruled file-11 mark lies further from AGREE than its ruled file-10 mark. The rows it turned on are O35 (SILENT in both) and O5, O30 and O17 (AGREE in both, against part of the readers); the readings that would have given a change away (O13, O19, O50, and O15 under file 11) fail on the text. After the cross-examination all four rows have both outside readings: RULING STANDS from both on O30, O17 and O35, and on O5 STANDS from Atria and FALLS from Mimo, resolved from the texts by a fresh determiner's re-reading, which upholds the ruling (10a). No reply names a new away-row.
- **(c) HOLDS.** No ruled file-11 mark is DISAGREE, and each file-11 SILENT stands against a file-10 SILENT on the same point.
- **(d) HOLDS.** 18 pointers ruled: 11 CORRECT, 7 SLIP, 0 CLAIM-CHANGING. The seven slips are errata (below).

## S75 corrections, each with its row

The plan's rule: both 1K returns agree on a different mark, and Claude's own reading of file 10 confirms it.

| row | S75 | 1K A / 1K B | Claude's reading of file 10 | corrected to |
|---|---|---|---|---|
| O20 Two valves in one second | SILENT | AGREE / AGREE | AGREE (01, before any return was opened) | **AGREE** |
| O40 Two hands on the test | SILENT | AGREE / AGREE | AGREE (01, before any return was opened) | **AGREE** |
| O45 The spring nobody mentioned | AGREE | SPLIT / SPLIT, at "It was already a route." | SPLIT (step 4's M28, written before any 1K return was opened, had found the point open) | **SPLIT** |

Declined: O15 (both 1K SPLIT, not confirmed). Findings about S75 that the rule does not turn into corrections: O18 and O41 (Claude's reading SPLIT; the 1K returns do not agree).

## 1K rows that differ from S72

None is a verdict on file 10 for the record; the baseline is S75's.
- **1K A differs on 8 rows:** O4 (SPLIT against AGREE), O15 (SPLIT/AGREE), O18 (SPLIT/AGREE), O20 (AGREE/SILENT), O31 (SPLIT/AGREE), O40 (AGREE/SILENT), O41 (SPLIT/AGREE), O45 (SPLIT/AGREE).
- **1K B differs on 13 rows:** O1 (DISAGREE/SILENT), O10 (SILENT/AGREE), O15 (SPLIT/AGREE), O18 (DISAGREE/AGREE), O20 (AGREE/SILENT), O31 (DISAGREE/AGREE), O32 (SILENT/AGREE), O38 (SPLIT/AGREE), O39 (SPLIT/AGREE), O40 (AGREE/SILENT), O45 (SPLIT/AGREE), O46 (SILENT/AGREE), O48 (SPLIT/DISAGREE).
- **The union is 15 rows.** Both returns agree on the same non-baseline mark on four: O15 SPLIT, O20 AGREE, O40 AGREE, O45 SPLIT. Three become corrections; O15 is declined. The other eleven keep the baseline by the rule.

## CASE DISPUTED

None. No reader marks any case CASE DISPUTED: each Stage 1 return counts 0, the three accepted audits count YOUR MARK CASE DISPUTED 0 and every "Cases to rule on" section counts 0, and no step-3 ruling raises one. Step 6 of the plan has nothing to set aside, no count omits a case, and no new numbered case file is needed. The case book's provenance file was not opened.

## The stopping rule

**It did not fire.** No auditor marked DISAGREE, on verdict or on mark, on any R row (tester A: O24, O11, O22; tester B: O22, O11). Mimo on A's R rows cannot be scored, since its audit is missing. **Nothing to widen:** each sample covers all 52 rows, so a widening would have had no rows had the rule fired. No 2W exists.

## Errata: seven cross-reference slips in file 11

Each is recorded for a later revision; none changes what a sentence claims.

| id | f11 line | pointer | the slip |
|---|---|---|---|
| XR1 | L5 | "(the answer to grievance 3, attack point (D), the Part XV entry)" | Follows file 10's layout; in file 11 attack point (D) and the Part XV entry are one passage (L534). The note also omits L197, L225, L473 and L616, which carry the declared change. |
| XR2 | L5 | "the audit's case O48", "(Semantics results S75)" | Points outside the document. |
| XR3 | L27 | "(Parts XI, XIV)" | Those Parts carry worth and aesthetics through \(\mathcal N\); a probability of truth is marked nowhere. |
| XR4 | L275 | "(the bell does not explain the tide)" | Case O2's content inside the theory, with no referent in the document. |
| XR5 | L447 | "(Part XIV)" | Lands on L510, but L514 excludes \(\mathcal N\) from the declared inputs. |
| XR6 | L588 | "By the dependence order of Part XIV" | The order at L518 lists no declared input and none of the definitions that rest on one. |
| XR7 | L616 | "Derivation 3's qualification seen from the other side" | Misdescribes the qualification: it concerns a *differing* survivor, not any survivor at all. |

Also for a later revision: twelve unclear wordings and tensions inside file 11 (03, section 8), and three reading hazards the readers fell into: f11 L161 s3 read as withholding a verdict even where a claim states its own ground (O5); f11 L419 with L514 read as leaving ownership open for want of a boundary declared in words (O30, O17); and shared text read against the fixed verdict on O10.

## Rulings adopted after the data

Recorded as adopted then (lesson S2).
1. **How P2 is scored: adopted after the data.** P2 is scored against the baseline as the plan's own rule corrects it (the plan's words for the file-10 mark end "then the baseline is corrected"), because P1 to P3 are claims about the theory and compare the two files' ruled marks. The plan's numbers in P2 describe the baseline when P2 was written. The frozen reading is reported beside the adopted one (P2, above), and both give FAILS; on the frozen reading the failure is by errors in the baseline, a kind the standing clauses do not name.
2. **The passage label.** A file-11 sentence that step 4 grades *application* (derivable from file 10, first stated in file 11) or ORDER gives passage SAME. This departs from step 4, which counts *application* as CLAIM for P3; the two answer different questions, and no count depends on it (every such row has verdict SAME).
3. **Two fallback labels corrected**, neither affecting a mark or a count (O10, O32).
4. **O40**, ruled from the texts where the verifications conflicted.
5. **O50's same point, clarified after the supplementary audit** (07): the missing weighting also carries the verdict's "at least two". A clarification; no mark, verdict, passage or count changes.

Where Claude's pre-rulings (01) changed after the returns were opened, each with its reason: file 10 on O35 (AGREE to SILENT), O21 and O27 (AGREE to SILENT), O37 (SPLIT to AGREE), O18 and O41 (SPLIT to AGREE by the rule only) and O45 (AGREE to SPLIT, a correction); file 11 on O21 and O27 (AGREE to SILENT). So 01's five changed verdicts (O18, O37, O41 and O48 toward; O35 away) became two (O45 and O48, both toward). No step-4 ruling changed.

## The missing audit: Mimo on tester A

Mimo's 2b audit of tester A's 1C failed on both allowed passes: pass 1 at high effort (three attempts, two ending at the 131,072-token limit after 3,189 s and 2,809 s, one with no finish after 695 s, none with any answer) and pass 2 at medium (three attempts, each at the limit after 2,817 to 3,052 s, each with 540,000 to 554,382 bytes of reasoning and no answer). It is MISSING from the table. What is lost:
- **The crossing on tester A.** On A's return only Atria audits, so a row Atria disputes on A cannot be told apart as auditor or run.
- **Mimo's blind marks on A's return,** one of the two checks the plan added for rows where both testers mark AGREE. Atria's blind marks from one 2a text differ between its two audits, so Mimo's might have differed on A as well.
- **A second outside audit of every tester-A row.** Each had one (Atria at high), not two.
- Mimo's Part 3 lists on A, its R-row judgments for the stopping rule on A (O24, O11, O22), and the fourth pair of the E2 substitute.

Not lost: Mimo's 2a reading of all 52 rows, which stands, and the rows Claude reads, which include every row where any accepted reading departs from the baseline. A supplementary audit in four parts was sent after the failure; it is outside the table, two of its four parts came back, and it restores a Mimo audit of tester A on O27 to O52 only (below).

## The effort confound

The plan sent Stage 2 at high effort. Decision S17 ("Use Atria and Mimo on medium thinking effort for cross examination") moved the three pending 2b calls to medium for their pass 2; the accepted returns at high stand (plan, third version, change c). So Atria on A is at high; Atria on B and Mimo on B at medium; Mimo on A would have been at medium; both 2a readings, from which every blind mark comes, are at high. Atria on A and Atria on B differ in effort as well as in the return audited, and on each return the auditors differ in effort as well as in family. Atria's unstable blind marks may reflect this. No ruled mark rests on an auditor's mark alone: every mark is Claude's, from the texts. The table heads each 2b column with its effort and names the confound under it.

## The effort controls

Sent by Claude as an audit of its own process under decision S18, outside the plan and never in its table, each resending the exact text of an accepted high-effort call at a stated effort, in the same process and provider slots as the last allowed pass of the real calls. Their reading rule is in `returns/effort controls/READ ME - effort controls, outside the S81 table.md`, R1 to R8. They were read by a Claude subagent by that rule, as written, in `returns/effort controls/Reading of the effort controls, by the rule written before they were opened.md` (941b207). Nothing in the reading bears on any ruling, and none is changed.

- **Atria on text A, at medium and at high: both failed.** The medium control ran to the 65,536-token limit on all three attempts. The high control made five attempts: two disconnected after about 1,803 s and three ran to the limit. Neither receipt records a token count. Under R4, "A control that fails supports no inference about effort beyond the fact that it failed and any token usage recorded for it." No inference is drawn. R2 (three readings of text A) and R3 (the replay check) cannot be run, and the secondary all-medium table that R7 allowed cannot be built, since it needed the Atria medium control. For the record only, as R8 foresaw: the accepted original at high had fitted on its fourth attempt, using 64,037 of its 65,536 tokens.
- **Mimo's 2a blind reading at medium: accepted** (returned 11:27:49 UTC). The two request bodies differ in `reasoning_effort` only; same text, limit, temperature and thinking.
  - **R1, reasoning.** The medium run reasoned more than the accepted high run, not less: 54,236 reasoning tokens against 42,679 (1.27 times), 244,044 characters of reasoning against 193,318 (1.26). Its response was shorter (55,129 characters against 63,224), and its FINDINGS shorter in 51 of the 52 rows.
  - **R5, the two readings row by row, descriptive only.** 16 rows show no difference in substance in FINDINGS, OPEN or SPLIT; 36 of 52 differ in at least one. FINDINGS: 32 the same, 13 overlapping, 7 different (O2, O10, O28, O29, O30, O33, O35). OPEN differs on 27 rows; SPLIT on 10. On four rows (O24, O30, O35, O40) a matter the high reading left OPEN is the medium reading's SPLIT, and on O35 the high reading's FINDINGS decide what the medium reading leaves as a SPLIT.
  - **R6 and R8.** One run at each effort, with no repeat at high: agreement does not show the efforts equivalent, and a difference is not read as an effect of effort. At high this same text has run from 193,318 characters of reasoning to at least 288,727 (three earlier attempts at high ran out before any reply), and the medium run's 244,044 lies inside that range. The two calls were 3 hours 37 minutes apart and shared slots differently. So the pair does not settle whether Mimo honours the effort setting, and no inference about effort is drawn.
  - What it does show, as a fact about the reader and not about effort: two readings of one text by one model at one temperature can differ on most rows (36 of 52). Decision D11 of the revision 2 drafts cites this for repeats in the next round.

## The reading rule for the controls came late

The controls were launched at 11:11 UTC with a statement of purpose and no rule for reading them; the process audit found the gap at about 11:25. The rule was written at 11:28 to 11:29 UTC (the READ ME lists the folder as it stood at 11:28:44 and 11:29:04; the file was saved at 11:29:19 and committed at 11:29:32 as 10464ba). The Mimo control had returned at 11:27:49, before the rule existed, and the first attempt of the Atria medium control had ended at the token limit (11:28:27). No one writing the rule opened any control's response, reasoning, truncated answer or receipt, and the READ ME says all of this itself. The commit message of 10464ba, "reading rule written before their data", overstates it: the rule was written before the data was opened, not before it existed. The READ ME's own text is the accurate account. The same fault recurred with the S88 cross-examination (log S88; lesson S12). The reading of the controls (941b207) followed the rule as written and states the timing again.

## The Stage 1 receipts' reader label

The six Stage 1 receipts in `returns/` (`s81_1C_A.receipt.json` to `s81_1K_B.receipt.json`, and their `.pass2.cleared.receipt.json` copies) carry the collector's fixed reader label, which names the tester model that decision S16 set aside. The returns are the S16 rerun by Claude subagents: each receipt's own record of the model as served says so, and its check against the set-aside model reads false. The receipts are kept as they came; the reader is named correctly here (plan, third version, change k). The label bears on no mark.

## The plan's third version

The second version said it was "Frozen once the first agent or call of this version is started; a change after that is a third version." Changes were made after its first agent started, and the third version was written only when the process audit found none had been (11:33 UTC, commit 24d2d75; lesson S15). For each change it quotes the second version, says what was done instead, on whose authority, and whether before or after the data it could bear on:
- **a.** Stage 1 by Claude subagents (decision S16); after the first six returns.
- **b.** Output limits at each provider's ceiling, Mimo 131,072 and Atria 65,536 (lessons S7, S11); after the failures that prompted it.
- **c.** Medium effort for the three pending 2b calls (decision S17), the accepted returns at high standing; after those returns.
- **d.** A pass cut off by the session's end does not use the one further run: Atria on B and Mimo on B had pass 1 cut off with no receipt, so pass 2 was their first completed attempt; Mimo on A's pass 1 failed with a receipt, so pass 2 was its one further run (Claude's ruling); before any pass-2 return.
- **e.** The effort controls, outside the table (decision S18); after the returns they repeat.
- **f.** Claude rules every case and difference from the texts before opening any return (lesson S2); after the data existed, before Claude opened it.
- **g.** Atria and Mimo cross-examine the determination (decisions S15, S17); before it is finished.
- **h.** The table shows each 2b column's effort, the confound and MISSING; before the table was built.
- **i.** 2W cannot be built, since each sample covers all 52 rows; before Claude read any 2b audit.
- **j.** The determination's log entry is S87 (LEGEND; lesson S5).
- **k.** The Stage 1 receipts' reader label is corrected here.
- **l.** The harness's hand-back tool passes the transcript check; after the first Stage 1 transcripts.

## Findings beyond the round: three defects in both files, the subject of S88

While the round was being determined, Claude subagents checked the holes Mimo found in its blind reading (log S83) and the one qualification S78 listed as untested, against file 10, file 11 and the predecessor (file 00). Three defects stood, and each is in both files word for word, so none bears on tests (a) to (d), which compare the two files; they bear on whether either file is right. They were put to Atria and Mimo as round S88 (`tests/S88 Cross-examination - three defects in the theory's own defeat list.md`), and none is ruled here.

1. **Derivation 2, "Indistinguishable is identical" (f10 L559–L565; f11 L552–L556).** Its component half, that two faithful candidates' "components are pairwise of one kind on \(C\)", is false under its stated assumptions: (F1), (F2) and (A) constrain each candidate against the target separately, so nothing pairs the components of two candidates, and "Immediate from Derivation 1 and (A)" passes over the step that fails. Two counter-instances are given. Part XV's own defeat entry, "A mathematical error. A counterexample to ... Derivations 1–3 under their stated assumptions", is therefore triggered, in both files. The repair proposed is a change of claim: answer profiles coincide, and components are of one kind only where a bijection pairs their anchors. Its only use, in Derivation 10, is restated with it.
2. **(T2), the accumulated-error bound (f10 L376; f11 L361).** It omits three hypotheses its predecessor stated: matching starts (\(e_0=0\)), that \(L\) is the Lipschitz constant of the represented map, and that \(\varepsilon\) bounds the discrepancy at every state of the stated scope. On a literal reading it has counterexamples; on the reading its placement suggests it is true. A drafting omission, for an erratum. This is the R2 J Part VIII qualification the S78 readers and this round's plan listed as touched by no case.
3. **Non-circular dependence (f10 L270; f11 L257).** The set \(\Gamma\) of active commitments whose block the third sentence has an admitted pair "remove or replace" is never typed: it may hold components, boundary values, or only the mechanism the candidate offers, and the text pulls three ways (a smaller slip, which the text's own conventions fill, is that the sentence names no translation from the target's edits to the explanation's). On the reading Part VI's wording invites, verdicts the theory needs flip: O33, O5 and Part VII's production case. The repair preferred is a change of claim that keeps the witnessing contrast inside the contract and places the dependence on \(\Gamma\) through Part VI's restriction.

S88 was sent at 14:07 UTC; Atria's reply arrived at 14:24, and its reading rule was written after the reply arrived and before it was opened (lesson S12). S88 is now settled (log S88; `results/S88 Reading of Mimo's reply in three parts, and the settled positions.md`): the first defect UPHELD, so Part XV's defeat entry stands triggered in both files and the repair is a change of claim; the second NARROWED to an undefined \(e_n\) and two omitted hypotheses, an erratum; the third NARROWED (its O33 flip withdrawn), repaired by a change of claim. Atria added a fourth: Derivation 3 of file 10 is false as stated, which file 11's qualified Derivation 3 already repairs, and which is P1's change seen from the defeat list. None of this bears on tests (a) to (d). The repairs are entries in the revision 2 drafts (log S90), not in file 11; S90's cross-examination carried all seven of those entries to both outside readers, and its rulings are applied in draft 3 (log S90).

## The cross-examination by Atria and Mimo

**What was sent.** At 15:28 UTC (requests committed as 4c891ce): the brief `tests/S87 Cross-examination - the S81 determination, file 11 against file 10.md` (25,477 words; md5 6acd78f5217acf2ce4e95acdbc1454f3), once to Atria and once to Mimo, each at medium effort and one pass, naming no model. It pressed seven rows (O5, O30, O17, O35, O40, O48, O45) and asked three more things: other rows that move away, the standing clause with the P2 scoring choice, and anything else. The rule it is read by is `determination/05 How the cross-examination will be read - written before sending.md`, committed before sending (a2c5e36): the replies are evidence, not results; every row either reply says FALLS, and every new away-row either names, is re-read from the texts by a fresh Claude determiner, who states the ruling, then the reply's argument, then rules; a change is recorded with its reason and with the fact that it came after the cross-examination; a changed row that is a theory change away fails test (b), and the standing verdict is then re-applied under the plan's three clauses; a call not accepted within its one pass supports nothing; the two replies are read independently. 05 was extended, each time before the texts it governs were sent, by `05b Mimo's reply in three parts - how it will be read, written before sending.md` (6a9f75c) and `05c Mimo's retry of part P1, one row per call - how it will be read, written before sending.md` (ff36cd4).

### Atria: accepted, every ruling stands (06)

- **The receipt.** Accepted at 16:40 UTC on the third attempt of its one pass (the first two returned no status, after 1,802 s and 1,637 s): finish "stop", last line END OF REPORT, 4,951 words, the brief as sent. Read on its own in `06 Reading of Atria's cross-examination.md` (a0db21c), while Mimo's single call was still running and nothing from it had been opened; Atria's reasoning file was not opened.
- **The pressed rows.** Seven closing lines, each "RULING STANDS". No row went to a fresh determiner, no re-rule file was written, and no ruling changed.
- **Other away-rows.** "None found", after seven families of cases (the occasions pair, the boundary pair, the credit pair, the route sentence, the receipts sentences, the construction sentences, the Derivation 3 cluster).
- **The standing clause.** "STANDING VERDICT: UPHELD".
- **Its other points, each answered in 06 section 5; none changes a test, a score or the clause applied.**
  - The reply's point on the P2 scoring choice is accepted on the outcome: the adopted scoring is a fair reading of the plan's words, and on either scoring the verdict cannot move to the first or third clause (06, 5.10). Not accepted: its description of O20 and O40 as theory changes toward the thoughtful person on the frozen reading. On either reading both rows are verdict SAME between the files, since the ruled file-10 mark is AGREE by the plan's own correction rule; they are S75 corrections, and are already recorded against the note as such. The gap 04 named stays open: on the frozen reading a P2 failure caused by an error in the baseline is a kind the clauses do not name.
  - M38 and M48 are cleared by O35, and O38 is AGREE in both files; the withheld corrections on O18 and O41; the credit rows O13, O20, O32 and O50; O15 under file 11; the Derivation 3 cluster outside O48 (M19, M21, M59); the caveat that "no case shows it harmful" is weak evidence; tests (a) to (d); the counts. All accepted, each as 04 already has it.
  - O10 as "reader variation": not accepted. f11 L121 and L41 are not word for word f10 L136 and L35, so a file-11 SILENT there would have been a verdict CHANGED with passage SAME. The ruled marks are AGREE in both files, so nothing turns on it.
  - The four rulings the verdict rests on (O5, O30 and O17, each upheld at medium confidence, and O35's file-10 SILENT) are accepted as the places where the verdict is fragile. Atria tried each and could not overturn it. That support weighs less than it seems: its reasons on O5, O30 and O17 are largely the determination's own, which the brief quoted, and on O5, O13, O17 and O30 it gave up contrary marks it had made as an auditor.
- **Findings about the reply**, counting neither for nor against file 11: on O30 it quotes the fixed verdict's words ("running inside the robot") as the situation's; on O40 it says the text lens upheld the SILENT reading, where the text lens marked it UNCERTAIN; the O10 label; the citation f11 L149 at O5 and O10, which is the obligations line; its account of why O15's correction was declined (the outcome is the same); O20 and O40 as theory changes. On O40 it names the file-11 route as f11 L27 s3 and L433 s4 where 04 names L419 s2 and L433 s4; the passage is CHANGED (additive) either way, and the count of 20 CHANGED passages stands.

### Mimo's single call: failed

`s87_xexam_mimo` waited for a Mimo slot and ended at 19:24:58 UTC as failed after six attempts: three ran to the 131,072-token limit with no reply (attempts 2, 3 and 6) and three returned no status (1, 4 and 5). Committed as the runner wrote it (e123397). Under rule 5 it supports nothing; its attempt files are kept and were not read for arguments.

### Mimo in three parts: one accepted, two failed (08)

- **The parts.** Prepared under 05b while the single call was still running, in case it failed (6a9f75c, 19:17 UTC), and sent at 19:27 UTC when it did (8bfefc1). Each carries the brief's rules and file 11 whole, only its own rows and the file-10 lines they need, a limit of about 3,000 words, and neither the hunt for other away-rows nor "anything else": part P1, O5, O30 and O17 (16,687 words); part P2, O35 and O40 (16,285); part P3, O48, O45 and the standing clause (16,359). Read by a Claude subagent in `08 Reading of Mimo's cross-examination in three parts.md` (76cceac), which opened neither Atria's reply nor 06, and no reasoning file.
- **Part P2: accepted.** On its fourth attempt (one empty, two with no status), after 2,756 s, with 106,392 reasoning tokens against its 131,072-token ceiling. "O35: RULING STANDS" and "O40: RULING STANDS".
  - On O35 it argues that file 10 is SILENT on the text as well as by the rule: (P) fixes when the condition is evaluated, not what it says (f10 L438); file 10 lets values be histories (f10 L122); "in every way that mattered" needs a standard f10 L25 marks as empty. File 11 is SILENT on the same point, through f11 L433 s1 and L514. It rejects its own blind DISAGREE as choosing the input from the verdict wanted.
  - On O40 it reads "Neither can say 'mostly'" as a point about what either party can claim, reached by file 10 through f10 L414 and L25 and by file 11 through f11 L27 s3 and L433 s4; the two files reach it by different routes where 04 says the same route, which changes no element. Its residual request, for any credit-division text in file 10 that file 11 replaces, was answered by searching file 10: there is none, so file 11's sentences add and replace nothing, which is 04's "CHANGED (additive)".
  - Every quotation it relies on is word for word in the files and the case book. No row went to a fresh determiner; no ruling changed.
- **Parts P1 and P3: failed.** P1 made six attempts: four with no status, one empty, and one that ran to the limit after 4,458 s, having written 6,910 characters that are not read. P3 made six: five with no status and one empty. Under rule 5 neither supports anything. So O5, O30, O17, O48, O45 and the standing clause are not examined by Mimo in these parts, and the hunt for other away-rows and "anything else" were not asked of Mimo (Atria's reply examined the hunt and found none).
- **P3 is not sent again** (05c section 2): O48 and O45 moved toward the thoughtful person, and Atria upheld both. For those two rows and for the standing clause there is one outside reading, Atria's, not two.
- **P1's rows are sent again, one per call** (05c): `tests/S87 Cross-examination - retry, O5 alone.md`, `… O30 alone.md` and `… O17 alone.md` (15,342, 15,134 and 14,868 words; replies of about 2,000 words), one pass each, each read on its own and independently of every other reply. Launched at 22:33 UTC (2155d0f); the three calls queued behind the S90 runner, which then held all three Mimo slots.

### Mimo one row per call: all three accepted (09, 10)

- **O17 went in its one pass and was accepted on its first attempt** (`s87_xexam_mimo_O17`): status 200, finish "stop", END OF REPORT, 1,392 words, after 2,482 s (it waited 710 s for a slot first), using 121,326 reasoning tokens of the 131,072 allowed. It came back at 23:26 UTC, before the container restarted at about 23:30, and was committed after the restart (c137e86); its sha256 matches the receipt, so nothing was lost.
- **O5 and O30 were cut by the container restart.** Their pass 1 was in flight when the restart moved the agent proxy: the attempt in flight lost its connection at about 23:31, every attempt after it was refused at once by a proxy address that no longer existed, and both calls ended as failed at 23:37:33 (1feb425). Neither failure was anything the model did. Under a note written before sending, `results/S90 and S87 - seven calls rerun after the container restart - written before sending.md` (57482a5), Claude ruled under decision S18 that a failure caused by the session's own network is not a reply and does not use up the call; both went again as pass 2, with the same text and settings and requests byte-identical to pass 1's, launched from a shell started after the restart (faf91f6), with no pass 3 allowed (lesson S24). Each reply is read by 05, 05b and 05c, as pass 1's would have been.
  - **O5, pass 2: accepted on attempt 4** of 4, after one attempt that ran to the limit with no content and two that returned no status; 1,237 words, 106,892 reasoning tokens.
  - **O30, pass 2: accepted on attempt 2** of 2, after one empty attempt; 1,335 words, 61,285 reasoning tokens.
  - Both were committed as returned at 286d69c (01:58 UTC on 24 September), each response's sha256 matching its receipt.
- **The closing lines.** `O17: RULING STANDS`; `O30: RULING STANDS`; `O5: RULING FALLS — file 11 SILENT`. None names a new away-row.
- **O17, read in `09 Reading of Mimo's retry - O17.md`** (8263ff9). Mimo puts the SILENT reading at full strength ("The pressure is real") and rejects it on the case's own words: "The case's first sentence states whose processes the work is: 'A repair robot keeps a log of every comparison it runs.' … The input is therefore stated, not missing". It rejects DISAGREE and SPLIT as well, and finds the other elements of the ruling hold. Rule 2 sends nothing to a determiner. A fresh determiner re-read the row all the same, because the orchestrator's task said the reply said FALLS, which it does not; that re-reading (`raw readings/09a re-read O17.md`) is recorded as beyond rule 2, and it comes to the determination's ruling on every column, at medium confidence. The boundary hazard of 04 section 7.10 stays as recorded.
- **O30, read in `10 Reading of Mimo's retry - O5 and O30.md`** (3deee3e). Mimo calls the declared-boundary attack "the strongest attack on the ruling; it fails, but on a single hinge": the situation's "The robot compares the pressures itself" states whose act the comparison is, so the input is given and not missing. It rejects SPLIT from f11 L419 s2's two clauses, since "whoever wrote it" would cover no case if a process written outside and handed in were outside work, and a reading of the verdict's last point through the defined term "Origin". It calls 04's word "places" loose, with the situation's "itself" as the ruling's real ground. Rule 2 sends nothing to a determiner, and every quotation the reply relies on was checked word for word against file 10, file 11, the case book and the retry text.
- **O5, read in 10.** Mimo reads f11 L161 s3 and L514 as withholding a verdict on whether a restriction is appropriate even where the claim states its ground ("On this point they record the claim's ground and abstain"), by analogy with Part XI, whose obligations are recorded and not judged; SILENT then comes before AGREE, and O5 is a theory change away through M17 and M48. Every quotation it relies on is word for word. Under rule 2 a fresh determiner, who had not opened 06, 07, 08 or 09, re-read the row from the texts (`raw readings/10a re-read O5.md`) and upheld the ruling on every column, at medium confidence: neither route to SILENT that the mark rules name fits, since the case states the input ("her account says why: the yeast that makes the gas works slowly in the cold") and L514 sets "a verdict given the input" against "where the input is missing, the verdict is unsettled", which is O1's case and not O5's; the Part XI analogy fits the ruling, since inputs are recorded and not judged and the verdicts that depend on them are given with them. Its record line (05 rule 3), exact:

> After the cross-examination (s87_xexam_mimo_O5, pass 2, attempt 4, accepted; "O5: RULING FALLS — file 11 SILENT"): re-read by a fresh determiner; RULING STANDS. File 10 AGREE (baseline, both 1K AGREE); file 11 AGREE; verdict SAME; passage CHANGED (additive), f11 L161 s3 and L514; no change; not away; test (b) unaffected. The reply reads L161 s3 and L514 as withholding a verdict on appropriateness even where the claim states its ground. L514 contrasts "a verdict given the input" with "where the input is missing, the verdict is unsettled", and the mark rules make SILENT on an input turn on an input "the case leaves unstated"; Greta's case states it ("her account says why"). The reply's Part XI analogy fits the ruling: inputs are recorded and not judged, and verdicts that depend on them are given with them. Worth is a different input (N; L27, L447). Confidence medium; the L161 s3 reading hazard stands as recorded.

- **The hazard on O5 remains.** Four of five earlier file-11 readings and this reply took L161 s3 to withhold the verdict. The repair is for revision 2: its entry at f11 L161 (W57.1 + W32(b).1, R10) expects "O5 stays AGREE, and the hazard is closed", and both S90 replies to its part let it stand. The boundary hazard on O30 and O17 has its repair drafted in revision 2's entry at f11 L465 (W12.1, R40), which both S90 replies let stand too.
- **What the recorders disclose.** 09's recorder opened 08 before writing, and 10's recorder opened 06 to 09 for its side-by-side section; 05c item 7 asks a retry's reader not to open them until its own reading is written. The re-readings of O17 and O5 were made without them, and neither recorder adds a ruling of its own.
- **Changes of ruling: none.** No mark, verdict, passage, direction or kind changes on O5, O30 or O17. All three stay AGREE in both files, so none is a theory change away; test (b) keeps its footing, rule 4 of 05 is not engaged, and 04's counts stand.

### Every reading side by side (10, section 11)

05b item 7 and 05c item 7 held the comparison until every reading was written; it is made in 10, section 11.

| row | what it decides | the determination (04) | Atria (06) | Mimo, cross-examination (08, 09, 10) | ruling after every reading |
|---|---|---|---|---|---|
| O5 | test (b) | f10 AGREE, f11 AGREE, SAME | RULING STANDS | P1 failed; retry: RULING FALLS — file 11 SILENT; re-read by a fresh determiner (10a): stands | **stands** |
| O30 | test (b) | f10 AGREE, f11 AGREE, SAME | RULING STANDS | P1 failed; retry: RULING STANDS | **stands** |
| O17 | test (b) | f10 AGREE, f11 AGREE, SAME | RULING STANDS | P1 failed; retry: RULING STANDS | **stands** |
| O35 | test (b) | f10 SILENT, f11 SILENT, SAME on the same point | RULING STANDS | P2: RULING STANDS | **stands** |
| O40 | an S75 correction | f10 AGREE (corrected), f11 AGREE, SAME | RULING STANDS | P2: RULING STANDS | **stands** |
| O48 | test (a) and P1 | f10 DISAGREE, f11 AGREE, CHANGED, toward | RULING STANDS | P3 failed, not sent again: **not examined by Mimo** | **stands** |
| O45 | P2 | f10 SPLIT (corrected), f11 AGREE, CHANGED, toward | RULING STANDS | P3 failed, not sent again: **not examined by Mimo** | **stands** |

- **Where two readings rule differently on one row: none.** 06 and 08 re-read no row; 07 re-read O35 and O50; 09 re-read O17 beyond rule 2; 10 re-read O5. Every reading leaves every ruling standing. (The supplementary audit, 07, audits tester A's marks and stands outside this comparison; its agreements count as no confirmation.)
- **Where the two outside models' replies differ: O5 alone.** Atria says RULING STANDS and Mimo RULING FALLS. Both are recorded, and the difference is resolved in writing from the texts by 10a's re-reading, made without 06, on two grounds: L514's contrast between a verdict given the input and a missing input, and O1 as the case where the input is missing. 06 records that Atria rejected the SILENT reading on the same two grounds after trying it as "the strongest challenge on the row"; the two reached them independently. 10a also answers what Atria did not raise: the Part XI analogy, the point that reading L161 s3 as a criterion contradicts it, and "can never find a narrowing illegitimate", which is recorded as a limit of the theory and not a failure to reach "legitimate" where a ground is stated.
- **Differences of route or citation**, none of which changes a ruling: on O30, Atria gave the verdict's "running inside the robot" as the situation's words, where Mimo quotes the situation correctly; on O40, Atria and Mimo each cite a file-11 route different from 04's listing; on O5, Atria cited f11 L149 where the causal-assignment clause is f11 L125.
- **Coverage of the pressed rows.** Atria examined all seven, the standing clause and the P2 scoring choice, and the hunt for other away-rows, in one reply. Mimo examined five of the seven: O35 and O40 in part P2, and O17, O5 and O30 one per call (O5 and O30 on a second pass after the restart). Its single call on the whole brief failed, part P3 (O48, O45 and the standing clause) failed and was not sent again, and no Mimo call was asked the hunt for other away-rows or "anything else". So the four rows test (b) turned on have both outside readings; O40 has both; O48 (test (a), P1), O45 (P2) and the standing clause have Atria's alone.

### The standing verdict after every reading

No ruling changed. Tests (a) to (d) hold. P1 holds. P2 fails at O45 alone on the adopted scoring, a theory change toward the thoughtful person, and at O20 and O40 on the frozen scoring, which are errors in the baseline. P3 fails only by undeclared CLAIM places, none shown harmful. The first and third clauses do not apply; the second does.

> **THE STANDING VERDICT AFTER EVERY READING OF THE CROSS-EXAMINATION (06, 07, 08, 09, 10): File 11 stands as the authority under the plan's second clause, with P3's 41 undeclared CLAIM places inside the theory (none shown harmful by any case), P2's failure at O45 (a theory change toward the thoughtful person), the three S75 corrections and the seven errata recorded against its frozen note in S81 Results.** It does not differ from the determination's verdict.

Its limits: each reply is evidence, not a result (05 rule 1); O48, O45 and the standing clause rest on one outside reading; on O5 the two outside replies disagree, and the ruling rests on the re-reading from the texts at medium confidence, with the L161 s3 hazard recorded; the ruling side is one model family (below).

## The supplementary audit, Mimo on tester A in four parts

**What was sent.** At 14:07 UTC (commit 4b41c28), under `supplementary - Mimo on tester A in four parts/READ ME - written before sending.md` (written at 14:02 UTC, before any part was sent; committed in f5f9dcb): the plan's own text for Mimo on tester A, byte for byte (36,671 words each), with its rows split into four parts of thirteen (O1–O13, O14–O26, O27–O39, O40–O52) and Part 2 left empty by one added sentence; Mimo at medium effort and its ceiling, one pass each. It is outside the table and does not replace the missing audit. Its reading rule: no part is opened until the step-3 rulings are committed; each row is taken only from the part that lists it; YOUR MARK, ON VERDICT, ON MARK and BLIND MARK are compared with Claude's ruled file-11 mark; every row where any of the four differs is re-read by Claude from the texts; agreement is reported as agreement and not counted as a confirmation (lesson 35); a failed part supports nothing and its rows are "not audited by the supplement".

**What came back.** Read in `07 Reading of the supplementary audit, Mimo on tester A in four parts.md` (1ef2ce4), after 04 and 06 were committed.

| part | rows | outcome |
|---|---|---|
| 1 | O1–O13 | **Failed.** First attempt ended on the provider's content filter after 2,066 s (60 characters, reported as the provider's refusal notice); the other two ran to the 131,072-token limit with no answer. |
| 2 | O14–O26 | **Failed.** Three attempts ran to the limit with no answer. |
| 3 | O27–O39 | **Accepted** on its second attempt (the first ran to the limit), after 1,524 s. |
| 4 | O40–O52 | **Accepted** on its first attempt, after 2,223 s, using 127,600 of its 131,072 tokens. |

**The rows, O27 to O52.** 24 of the 26 rows agree on all four fields; of the 104 field comparisons, 102 match. Both differences are BLIND MARK: O35 (blind DISAGREE) and O50 (blind SPLIT). A check by program showed each blind mark is Mimo marking its own 2a text a second time, and each equals Mimo on B's blind mark, already in the E2 table. On both rows Mimo's own YOUR MARK is the ruled SILENT. Both were re-read by Claude from the texts (`raw readings/07a re-read O35.md`, which covers both):
- **O35 stays SILENT in both files.** The blind DISAGREE needs a stated condition and occasions that include the four seconds; the case names only "the protected tap", neither file sets a default occasion, and f11 L514 says that "where the input is missing, the verdict is unsettled and the semantics says so rather than choosing the input from the verdict wanted". Mimo's own blind reading lists the occasions as open. Had the DISAGREE held under file 11, O35 would have been a theory change away and test (b) would have failed.
- **O50 stays SILENT in both files.** The two sentences the SPLIT cites (f11 L419 s2 and L465 s2) are complementary clauses of one rule, each classifying a different contribution; credit is per achievement; and even on a strict boundary reading the discovery point would be unsettled, which is SILENT, not SPLIT. A SILENT to SPLIT would not have been away. The same-point wording is clarified (see O50 above).

**Changes of ruling: none.** No mark, verdict, passage, direction or kind changed; 04's counts stand; test (b) needs no re-application; the second clause applies as before. The 24 agreeing rows count as no confirmation, including O30 and O32, where the audit sides with the ruling against tester A.

**Rows not audited by the supplement:** O1 to O26. **Not restored:** a second outside audit of tester A on those rows, the crossing there, the fourth pair of the E2 substitute, and Mimo's Part 3 lists over tester A's whole return. **Findings about the reader:** on O35 and O50, Mimo's blind mark from one 2a text is the same in both of its audits, where Atria's differed between its two; and in both audits Mimo moved from its blind mark to the ruled SILENT once it had read the tester's row.

## Not tested

Carried from the plan:
- Whether the fixed verdicts are right. They are Claude's; CASE DISPUTED was the only channel against them, and no reader used it. Cases by an agent that has never read file 10 (S78 group C) were not applied.
- R2 J's Part VIII qualification: no case touches it (and see the second finding above).
- D3-T, the case aimed at the qualified Derivation 3's weakest sentence: not entered in this round. Its verdict has since been fixed by two pairs of fresh Claude authors who never read the theory (No, high confidence), as the candidate O76 for the next round (log S89).
- The parts of file 11 no case reaches. Coverage of the recovered Stage B rows stands at 55 of 80 (log S74), and the first 32 rows are unrecovered. Some undeclared CLAIM places are touched by no case (M7, M24, M43 and M59 among them) and most by one to three, so "no case shows it harmful" is weak evidence that a place is harmless.
- Any reader armed with the audit workflow (file 24).
- Whether the pattern can catch a known error: S79's question.
- File 12 (the causality version) and the richness question (FW5).
- Stage 1 by testers of the family that wrote the theory, the revision, the case book and the fixed verdicts, and that determines the result: shared training can mean shared readings.
- Reader variation between families at Stage 1: seen only at Stage 2.
- The Stage 1 settings (thinking and temperature are the harness's), and what the harness shows a subagent beyond its prompt.
- E2, as written.
- Whether a tester working from a file with tools reads as it would from one prompt.

Added by this determination:
- **One model family throughout the Claude side.** The testers, the builder of the texts and tools, the case and difference readers, the step-3 determiners, the verifiers and the determiner are all Claude subagents or Claude, of the family that wrote the theory, file 11, the case book and the fixed verdicts. Only Atria and Mimo read from outside it, and their readings are evidence.
- **One outside audit of tester A on O1 to O26,** not two. The supplementary audit restores a Mimo audit of O27 to O52 only, outside the table.
- **Mixed effort** across the accepted audits; the effort controls say nothing about it (Atria's failed; Mimo's is descriptive, one run at each effort, on a different task).
- **The cross-examination is uneven between the two outside readers.** Atria answered the whole brief in one reply. Mimo's whole brief failed; of its three parts only one came back, and its retry of the failed part's rows, one per call, came back on all three, two of them on a second pass after the container restart cut the first. Of the pressed rows, Mimo's reading covers five of seven (O35, O40, O17, O5, O30); O48, O45 and the standing clause, with the P2 scoring choice, have Atria's reading only, and P3 is not sent again. Mimo was not asked to hunt for other away-rows. On O5 the two outside readers disagree, and the ruling rests on a fresh determiner's re-reading from the texts, at medium confidence. Each accepted outside reading is the run that happened to fit under its ceiling (the O17 retry used 121,326 reasoning tokens of 131,072), and each was told the determination's reasons, so agreement with them weighs less than an independent reading would.

## Next step

None for this round: every reading of the cross-examination is written, no ruling changed, and this file is final. Its findings are carried by the revision 2 drafts (log S90): the seven errata, the three reading hazards (O5 at f11 L161 s3; O30 and O17 at L419 with L514; O10), the twelve unclear wordings, a declaration of the 41 undeclared CLAIM places (and M7) in the second layer of the revision's record, and S88's settled repairs to Derivation 2, (T2) and non-circular dependence. Revision 2's own cross-examination (S90) is read, and its rulings are applied in draft 3 (99e9cd0). Whether draft 3 is frozen as file 13 and its test round run is the owner's decision (log S90, and the project story's Next step).
