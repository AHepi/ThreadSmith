# S81 step 3: verification of the rulings, rule-application lens

*Written by a Claude subagent acting as an adversarial verifier, 23 September 2026. It checks whether the four step-3 rulings files apply the plan's definitions exactly. It does not re-rule the texts, except where a rule turns on a reading.*

## What was read

- The four rulings files in this folder: `rulings - O1 group.md`, `rulings - O2 group.md`, `rulings - O3 group.md` and `rulings - O4 group.md`, all in full.
- `build_packets.py`, `run.log` and `selection.json` in this folder, for the selection.
- The plan, second version: "The frozen prediction", "The words Claude rules with", "How Claude determines the result" and "What counts as file 11 standing as the authority" (lines 107–166). The plan's third version, in full.
- `determination/03`: the header, sections 3 to 7, and the M28 ruling in `raw readings/03c rulings R2.md`. `determination/READ ME.md`, and the git log of `determination/`.
- `table.md`, in full.
- The returns, for the selection check only: Part 3 of the three accepted 2b returns; every ON VERDICT, ON MARK and ON QUOTES line of those returns that is not AGREE or SUPPORTS; a search of all nine accepted returns for CASE DISPUTED; the closing "Sentences … that give a verdict different" lists of both 1C returns; the 1K A and 1K B records for O20, O40 and O45.
- The mark rules at the head of `briefs/s81_1K_A.txt`, including "Same finding" and SPLIT.
- The S72 Stage 1 return, `01 The bare earlier version against every case.md`: the rows for O1, O5, O12, O15, O18, O20, O21, O27, O35, O39, O40, O45 and O50. These rows were read to check the "same point" rulings and the corrections.
- File 11, lines 159–163, 417–421, 463–467 and 508–516.

**Not opened.** The effort-controls folder. The supplementary audit of Mimo on tester A and its returns. The folders set aside by decision S16. The provenance file, because no row carries a CASE DISPUTED ruling.

## Result

- **Rows verified: 11.** 11 UPHELD, 0 OVERTURNED, 0 UNCERTAIN.
- **Classes with no row.** No row is ruled a theory change away from the thoughtful person. No reader marks CASE DISPUTED in any accepted return, and no determiner raises it, so there is no CASE DISPUTED ruling to check.
- **The file-10 mark rule** was checked on 19 rows: every row where a 1K mark differs from the baseline, and every row where Claude's pre-ruling (01) differs from it. It is applied exactly on all 19 (section 3).
- **Missing rows: none.** The 33 selected rows are every row that the plan's step-3 criteria name in the accepted returns (section 5).
- **Findings on rule application: four.** None of them changes a row verdict, a count, test (b) or the standing verdict (section 4). Finding 1 needs action before S81 Results: a post-data rule that is not yet marked as adopted now.

## 1. The rows verified

| row | why decisive | file-10 | file-11 | verdict / passage / direction / kind | verdict |
|---|---|---|---|---|---|
| O35 | test (b); flagged decisive in 03 section 6 | SILENT (baseline) | SILENT | SAME (same point) / CHANGED (additive) / none / no change | UPHELD |
| O48 | test (a) and P1 | DISAGREE (baseline) | AGREE | CHANGED / CHANGED (alteration) / toward / theory change | UPHELD |
| O20 | S75 correction | AGREE (corrected from SILENT) | AGREE | SAME / CHANGED (additive) / none / no change | UPHELD |
| O40 | S75 correction | AGREE (corrected from SILENT) | AGREE | SAME / CHANGED (additive) / none / no change | UPHELD |
| O45 | S75 correction; theory change | SPLIT (corrected from AGREE) | AGREE | CHANGED / CHANGED / toward / theory change | UPHELD |
| O15 | both 1K agree on a different mark, and the correction is declined | AGREE (baseline) | AGREE | SAME / SAME / none / no change | UPHELD |
| O18 | Claude's reading of file 10 (SPLIT) differs from the mark the rule gives | AGREE (baseline, by rule) | AGREE | SAME / CHANGED (additive) / none / no change | UPHELD |
| O41 | as O18 | AGREE (baseline, by rule) | AGREE | SAME / CHANGED (additive) / none / no change | UPHELD |
| O5 | departs from the majority (4 of 5 file-11 readings SILENT); test (b) turns on it | AGREE (baseline) | AGREE | SAME / CHANGED (additive) / none / no change | UPHELD |
| O10 | departs from the majority (3 of 5 SILENT) | AGREE (baseline) | AGREE | SAME / SAME / none / no change | UPHELD |
| O30 | departs from the majority (3 of 5 not AGREE); named in a Part 3 list; test (b) turns on it | AGREE (baseline) | AGREE | SAME / CHANGED (additive) / none / no change | UPHELD |

The "file-11 readings" of a row are the two 1C marks and the three accepted 2b YOUR MARKs. The majority check covers every row where these five are not unanimous: O5, O10, O15, O17, O21, O27, O30, O32 and O50. Only O5, O10 and O30 are ruled against the majority. O17 (AGREE) and O50 (SILENT) are ruled with 3 of 5, and O15, O21, O27 and O32 with 4 of 5.

## 2. Row by row

**O35 (test (b)). UPHELD.**
- The file-10 mark is correct by rule. Both 1K returns mark SILENT, which is the baseline, so the rule gives SILENT whatever Claude's reading is. 01's AGREE could never have become the file-10 mark, because that needs both 1K returns to mark AGREE.
- 03 section 6 fixed the consequence before any 1K return was opened: "If the file-10 mark is SILENT, O35 is SILENT→SILENT on the same point … and no case shows M38 or M48 harmful." The ruling follows that condition. It does not choose the outcome after the data.
- "Same point" was checked against the source of the baseline. S72 reads O35 as SILENT because "the protected predicate and its time range are unstated", and the bare formula needs protected obligations "fixed for the comparison". The file-11 SILENT rests on the unstated condition and its occasions (f11 L433 s1, L514). This is the same point.
- Direction is none (SILENT to SILENT). A change at the same rank could not fail test (b) in any case.
- Claude's own reading of file 10 moved from AGREE to SILENT after the returns were opened. The change is recorded with its reason (lesson S2). S72 made the same reading before this round, and the O38 ruling uses the same formula. The change does not set the mark.
- Note, not a defect. The record addresses test (b) and does not state test (c). Test (c) is not engaged, because the ruled file-11 mark is SILENT, not a wrong verdict, and Claude's reading of file 10 is now SILENT as well. S81 Results should say so.

**O48 (test (a), P1). UPHELD.**
- File-10 mark: 1K A marks DISAGREE and 1K B marks SPLIT, so no correction is possible. The baseline DISAGREE stands. 1K B's SPLIT is correctly recorded as differing from S72 and as not triggering the plan's clause "If 1K shows O48 AGREE under file 10".
- File-11 mark: AGREE. It rests on L562 s2–s3, the qualified Claim, which is one of the places P1 names, with L534 and L43 restating it.
- The ruling meets 03's check that no reading rests on L473 alone. It gives a counterfactual reason: under file 10's unqualified claim, t′ need not be a member of 𝒯, so L473 by itself could not change the verdict. No reader cites L63.
- The verdict is CHANGED, the passage CHANGED (L562 against f10 L569), the direction toward and the kind a theory change. Each is by the definitions.

**O20 and O40 (S75 corrections). Both UPHELD.**
- Both 1K returns mark AGREE on each row, which is a different mark from the baseline SILENT. Claude's reading confirms AGREE. The confirmation predates the data: 01, committed in 2788a77 before any return was opened, already has file 10 AGREE on both rows.
- The S72 rows bear the reasons out. On O20, S72 says "the record warrants neither exclusive claim" and is SILENT only "on a further allocation", which the fixed verdict does not claim. On O40, S72 is SILENT on "a comparative rule", and the ruling reads the verdict as a claim about what either party can say.
- Each correction is recorded with the row, as the rule requires.
- The fallbacks are ruled correctly. If the baseline stood, each row would be SILENT→AGREE, a theory change toward the thoughtful person. On O40's alternative reading, the row is SILENT in both files with no change. Neither route gives a change away.
- The P2 consequence is Finding 1.

**O45 (S75 correction, theory change toward). UPHELD.**
- Both 1K returns mark SPLIT at the same point ("It was already a route.") on f10 L246. The 1K records were checked in the raw returns.
- Claude's confirmation came after the 1K returns were opened, and it reverses 01's AGREE. It is recorded with its reason (lesson S2). It also has a text basis that predates the 1K returns: 03's M28 ruling (raw reading 03c), written before any 1K return was opened, says f10 L246 "leaves open whether a part nobody described belongs to Γ".
- The plan puts Claude's confirmation after the 1K returns by design, so a confirmation made then is within the rule.
- SPLIT→AGREE is toward under the plan's order. The file-11 AGREE rests on the first clause of L309 s3 (M28, CLAIM new), not on sentences shared word for word. It is therefore a theory change, not reader variation.

**O15 (correction declined). UPHELD.**
- Both 1K returns mark SPLIT, so the rule turns on Claude's reading. Claude does not confirm.
- The reason uses the brief's own definition of SPLIT: "on at least one point, the theory's sentences support two readings that reach different findings". The two 1K readings answer different points of the verdict ("his account of his own work" and "his account"), not one point.
- S72 read file 10 the same way before this round: "No disagreement when the two scopes in the fixed verdict are kept distinct."
- The fallback is ruled correctly. If the correction were made, the row would be reader variation or a change toward the thoughtful person, never away.

**O18 and O41 (Claude's reading of file 10 differs from the ruled mark). Both UPHELD.**
- O18: 1K A marks SPLIT and 1K B DISAGREE. They do not "agree on a different mark", so the baseline AGREE stands, although Claude's own reading is SPLIT. The ruling states the contrary reading of the rule (both 1K returns are non-AGREE) and rejects it on the rule's words.
- O41: 1K A marks SPLIT and 1K B AGREE, so the baseline stands.
- Both rows are recorded as findings about S75, not as corrections. Each would otherwise be a theory change toward the thoughtful person, so the rule withholds a count in file 11's favour, not against it.

**O5 (departure; test (b) turns on it). UPHELD.**
- The plan makes the file-11 mark Claude's ruling from the text, informed by the returns, so it is not a count of readers.
- The ruling uses only the brief's "Same finding" rule, which was fixed in advance. That rule says a verdict that "reaches the fixed verdict's finding and adds a qualification" reaches the same finding.
- The text check agrees with the ruling. f11 L161 s3 makes what makes a restriction appropriate "a substantive, criticizable part of the claim". L514 lists it among the inputs on which "a verdict … is a verdict given the input". Greta's claim states its ground, so the input is present.
- The consequence is stated exactly. If the SILENT contrary held, the row would be AGREE→SILENT, tracing to M17 and M48, a theory change away, and test (b) would fail. The row is named for the plan v3 (g) cross-examination.
- Recorded: the row's substance is exposed, not its rule application. Four of five readings go the other way, and test (b) turns on this one textual ruling.

**O10 (departure). UPHELD.**
- The ruling follows the rules, and no count depends on it.
- The fallback is misnamed. The record says a file-11 SILENT "would then be reader variation". Under the plan, reader variation needs verdicts that rest on sentences the two files share word for word. The SILENT readings rest on f11 L121 and L41. 02 rules both of them WORDING against f10 L136 and L35 (C24, C12), so they are not word-for-word. The correct fallback is "verdict CHANGED with passage SAME". That is not a theory change, so test (b) is still not engaged, but it is also not reader variation as the plan defines it (Finding 3).

**O30 (departure; Part 3 row; test (b) turns on it). UPHELD.**
- The file-10 mark is correct by rule: both 1K returns mark AGREE, which is the baseline.
- The file-11 AGREE rests on f11 L419 s2 ("a process that runs inside the boundary is the system's own today whoever wrote it") and L465. The ruling reads the situation's "the robot compares the pressures itself … a routine … uploaded to it" as supplying the boundary input. It also answers the Part 3 SPLIT entry in 2b Atria on B on the sentence's own words.
- The consequence is stated exactly. If the SILENT or SPLIT contrary held, the row would be AGREE→SILENT, a theory change away tracing to M37, M44 and M48, and test (b) would fail.
- Unlike O5, the record does not name O30 for the cross-examination. O17 rests on the same boundary reading, with 2 of 5 readings SILENT, and is not named either. Both should be named beside O5 (Finding 4).

## 3. The file-10 mark rule, row by row

The rule: the baseline, unless both 1K returns agree on a different mark and Claude's reading of file 10 confirms it.

| row | baseline | 1K A | 1K B | both 1K agree on a different mark? | Claude's reading (step 3) | ruled file-10 mark | exact? |
|---|---|---|---|---|---|---|---|
| O1 | SILENT | SILENT | DISAGREE | no | SILENT | SILENT | yes |
| O4 | AGREE | SPLIT | AGREE | no | AGREE | AGREE | yes |
| O10 | AGREE | AGREE | SILENT | no | AGREE | AGREE | yes |
| O15 | AGREE | SPLIT | SPLIT | yes | AGREE (does not confirm) | AGREE | yes |
| O18 | AGREE | SPLIT | DISAGREE | no (two different marks) | SPLIT | AGREE | yes |
| O20 | SILENT | AGREE | AGREE | yes | AGREE (confirms; 01 AGREE before the data) | AGREE, corrected | yes |
| O31 | AGREE | SPLIT | DISAGREE | no | AGREE | AGREE | yes |
| O32 | AGREE | AGREE | SILENT | no | AGREE | AGREE | yes |
| O38 | AGREE | AGREE | SPLIT | no | AGREE | AGREE | yes |
| O39 | AGREE | AGREE | SPLIT | no | AGREE | AGREE | yes |
| O40 | SILENT | AGREE | AGREE | yes | AGREE (confirms; 01 AGREE before the data) | AGREE, corrected | yes |
| O41 | AGREE | SPLIT | AGREE | no | SPLIT | AGREE | yes |
| O45 | AGREE | SPLIT | SPLIT | yes | SPLIT (confirms; 01 AGREE; 03 M28 before the 1K returns found the point open) | SPLIT, corrected | yes |
| O46 | AGREE | AGREE | SILENT | no | AGREE | AGREE | yes |
| O48 | DISAGREE | DISAGREE | SPLIT | no | DISAGREE | DISAGREE | yes |
| O21 | SILENT | SILENT | SILENT | (baseline) | SILENT (01 AGREE) | SILENT | yes |
| O27 | SILENT | SILENT | SILENT | (baseline) | SILENT (01 AGREE) | SILENT | yes |
| O35 | SILENT | SILENT | SILENT | (baseline) | SILENT (01 AGREE) | SILENT | yes |
| O37 | AGREE | AGREE | AGREE | (baseline) | AGREE (01 SPLIT) | AGREE | yes |

- **Every 1K mark that differs from S72 is said to differ, and none is read as a verdict on file 10 for the record.** Tester A: O4, O15, O18, O20, O31, O40, O41 and O45. Tester B: O1, O10, O15, O18, O20, O31, O32, O38, O39, O40, O45, O46 and O48.
- **"Same point" on the six SILENT→SILENT rows.** O1, O12, O21, O27, O35 and O50 were each checked against the S72 row behind the baseline. On every row, S72's silence and the file-11 silence concern the same point:
  - O1: "the retreat verdict";
  - O12: merit;
  - O21, O27 and O50: "mostly";
  - O35: the unstated protected condition.
- **Direction.** Every ruled direction follows the plan's order (AGREE, then SILENT or SPLIT, then DISAGREE): O48 DISAGREE→AGREE and O45 SPLIT→AGREE are toward. No ruled file-11 mark lies further from AGREE than its ruled file-10 mark, so test (b) holds on the ruled marks. No file-11 mark is DISAGREE, so no sentence of file 11 is ruled to give a wrong verdict, and test (c) is not engaged.
- **Theory change against reader variation.** The only two CHANGED verdicts, O45 and O48, each rest on a passage CHANGED (M28; L562 against L569). Both are theory changes, both toward. No difference between ruled marks rests on shared sentences, so the reader-variation count of 0 is correct.

## 4. Findings on rule application

1. **P2 is scored against the frozen baseline, and the consequence is a post-data rule that is not yet marked as adopted now (O20, O40, O45).**
   - The O4 group scores P2 against the frozen baseline: "P2 as frozen fails at O20 and O40, but by S75, not by file 11 … This failure is of neither kind. It is a finding about S75."
   - The O2 group scores O45 the same way: "As frozen, P2 is untouched."
   - The standing clause names only two ways in which P2 may fail and file 11 still stand: a theory change toward the thoughtful person, and an undeclared CLAIM that no case shows harmful. A P2 failure caused by S75 is a third kind, which the plan does not provide for. The phrase "counts neither for nor against file 11" is borrowed from the plan's reader-variation clause. O20 and O40 are not reader variation, because their file-11 AGREE rests on the new L433 s4 and L27 s3. The step-3 files therefore rule on a gap in the plan after the data, without marking the ruling as adopted now (lesson S2).
   - There is a second reading. The rule's own words are "then the baseline is corrected". If P2 is scored against the corrected baseline, P2 holds at O20 and O40 and fails only at O45, by a theory change toward the thoughtful person. That is a kind the saving clause names, and no new rule is needed.
   - Either reading leaves test (b) and the standing verdict unchanged. S81 Results must pick one reading, state it, and mark it as adopted after the data.

2. **The passage-label policy is a step-3 rule, and it conflicts with step 4's policy.**
   - All four groups label a passage SAME where it rests on a file-11 sentence that step 4 grades *application*. 03 counts *application* as CLAIM "under the pre-reading's policy, kept here".
   - So the same sentence counts as CLAIM for P3 and as "claims nothing different" for the passage label. Examples: O13 on L433 s5 (M41), O2 on L275 s2 (M23), O3 on L401 s4 (M34), O14 on L399 s4 (M33).
   - O46 goes further and grades the two clauses of M28 separately, where step 4 grades the sentence whole.
   - The policy is presented as the plan's rule, not as one adopted at step 3. It changes no count, because every row that rests on an *application* sentence has verdict SAME. It should still be marked as adopted at step 3, with a note that it departs from 03.

3. **Two fallback labels are looser than the plan's definition of reader variation.**
   - O10: see section 2.
   - O32 in the O2 group: tester A's 1K AGREE and 1C DISAGREE are called reader variation. The 1C DISAGREE also quotes the new L417 s3, and the 1K AGREE rests partly on f10 L521, which differs from f11 L512 by one word. The operative sentence, L606 = f10 L613, is shared, so the finding stands. The label should say "rests chiefly on".
   - Neither affects a ruled mark or a count.

4. **Exposure is flagged for one decisive row and not for two others.**
   - The rulings keep test (b) holding on three textual rulings against part of the readers. On each, a file-11 SILENT would be a theory change away:
     - O5 (4 of 5 readings SILENT, through M17 and M48);
     - O30 (3 of 5 not AGREE, through M37, M44 and M48);
     - O17 (2 of 5 SILENT, through the same places).
   - Only O5 is named for the plan v3 (g) cross-examination. O30 and O17 should be named with it. Each ruling applies the rules exactly, so this is a gap in coverage, not an error.

## 5. The selection: no missing row

The plan's step-3 criteria were checked against the table and the returns, independently of `build_packets.py`.

- **O48 in full.** Selected.
- **Any 1C mark or 2b YOUR MARK that differs from the baseline.** O5, O10, O15, O17, O20, O21, O27, O30, O32, O40, O48 and O50. All are selected.
- **Any 1K mark that differs from the baseline.** O1, O4, O10, O15, O18, O20, O31, O32, O38, O39, O40, O41, O45, O46 and O48. All are selected.
- **CASE DISPUTED.** None in any mark or count line of the nine accepted returns. 2b "Cases to rule on" is COUNT 0 in all three accepted 2b returns.
- **Part 3 lists.**
  - "Disagreements the reading under audit left unmarked": O30, in Atria on B (COUNT 1). Atria on A and Mimo on B have COUNT 0.
  - "Wrong, and uncorrected anywhere in the theory": COUNT 0 in all three. Atria on A's entry names O32 while reporting none.
  - Both O30 and O32 are selected.
- **ABSENT quotations.** None: the table's absent count is 0 on every row for both testers.
- **Both 1C marks AGREE and a BLIND MARK not AGREE.** O4, O8, O13, O19, O33 and O40, matching the table's last column. All are selected.
- **Auditor disagreement lines.** Every row where a 2b ON VERDICT or ON MARK is DISAGREE, or ON QUOTES is PARTLY or FAILS, is selected: O5, O8, O10, O13, O15, O21, O27, O30, O32, O33 and O50. So is every row on either 1C list of "Sentences … that give a verdict different": O32 and O50.
- **03's step-4 flags and the eight baseline-SILENT rows (step 5).** All are selected.
- **One limit, recorded and not a gap.** 2b Mimo on A is missing. A row that only that audit would have raised cannot be selected from the accepted returns. Atria's blind marks differ between its two audits of one 2a text (O5, O10, O17, O27, O40), so Mimo's might differ too. The supplementary audit of Mimo on tester A is read after step 3, under its own reading rule, and may add rows then.
