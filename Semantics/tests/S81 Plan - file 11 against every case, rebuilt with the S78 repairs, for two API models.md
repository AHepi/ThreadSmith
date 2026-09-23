# S81 Plan - file 11 against every case, rebuilt with the S78 repairs, for two API models

*Written by Claude (an Opus 5.5 subagent doing the analysis and integration for the orchestrator) on 23 September 2026, before any call of this round. Frozen once the first call is sent; a change after that is a new numbered file. Nothing in this plan travels in any call: the prediction, the baseline, the sampling rule and the standing rule live here and in `tools/s81_build.py` only.*

## What this round is

Round S76 as planned (log S76): file 11, the candidate revision, tested against every case, testing then audit (decision S7), with Claude reading both and determining the result (decision S13: "you are the authority, not Mimo or Atria. You make the big decisions"). It is rebuilt for the two outside API models of decision S12, Atria (`Atria-Dawn-Preview`) and Mimo (`mimo-v2.6-pro`), each reached by one prompt in and one answer out, with no files and no tools, through `tools/s80_call.py`; and it carries the S78 repairs of group A (`results/S78 Results - the two-stage pattern reviewed by five readers, ...md`), which the five readers said must be made before S76 runs. The S76 packs as sent at log S76 are superseded unsent and kept.

The owner's word on group A is not in Decisions as words of its own; the rebuild is made on the orchestrator's instruction under decision S13. The orchestrator confirms that reading before the first call. **Confirmed by Claude, 23 September 2026, under decision S13** ("you are the authority ... You make the big decisions"): group A is applied as mapped below; group C stays out; the three calls added beyond the brief (1K, 1D, 2a on all 52) are kept; D3-T stays out of the case book until Claude fixes its verdict; file 11's revision note is withheld from every call as a presentation choice (the frozen file is unchanged). The number S81 is kept although LEGEND's rule would give S88 (the shared sequence stands at L86): S80 was named the same way before the rule was checked, and renaming a round mid-run costs more than the gap; log S80 records the deviation.

## The texts

| Text | File | As sent |
| --- | --- | --- |
| File 11, the candidate | `authority/11 Claude Fable Semantics - standalone theory, revision 1.md` (md5 5e494c1095d920d128b9a79de378f923) | Whole, except line 5, the revision note, and the blank line after it. The note names O48 and S75 and states the claim count, which is the answer; the frozen file is untouched and the build checks its md5 before cutting. 9,487 words as sent. |
| File 10, the authority | `authority/10 Claude Fable Semantics - standalone theory.md` (md5 3a8cd7c8ca6f3ad3b8a85ab9984d850e) | Whole. 7,937 words. |
| The case book | `tests/S81 Case book - the 52 cases, situations and fixed verdicts, as the tested agent sees them.md` (md5 4f488d149e44669240d5db546c8e946a) | Whole for 1C, 1K and 2b (4,344 words); for 2a, the verdict lines cut and the opening paragraph replaced by one that mentions no verdict (2,840 words). Provenance, kept out of every call: `tests/S81 Case book - provenance.md`. |
| The briefs | `tests/S81 Stage 1 testing - file 11 against every case.md` (briefs 1-cases, 1-texts); `tests/S81 Stage 2 audit - check the Stage 1 return.md` (briefs 2a, 2b, 2D) | Lifted between their markers, word for word. |

## What is run

Twelve calls, each a fresh single-turn call, thinking on (`reasoning_effort: high`), temperature pinned at 0.7 by `s80_common`, max_tokens on the reader ladder (48,000, then 64,000), accepted only when the reply ends with `END OF REPORT`. Word counts are from `s81_build.py build` at freeze; the two Stage 2 calls that carry returns are estimated.

| Stage | Call | What the model sees | Words | Tag |
| --- | --- | --- | --- | --- |
| 1 | 1C, the test | brief 1-cases + file 11 (note withheld) + the case book | 14,803 | `s81_1C_atria`, `s81_1C_mimo` |
| 1 | 1K, the control | brief 1-cases + file 10 + the case book | 13,253 | `s81_1K_atria`, `s81_1K_mimo` |
| 1 | 1D, the differences | brief 1-texts + file 10 as Text A + file 11 (note withheld) as Text B | 18,024 | `s81_1D_atria`, `s81_1D_mimo` |
| 2 | 2a, the blind reading | brief 2a + file 11 (note withheld) + the 52 situations, verdicts withheld | 12,740 | `s81_2a_atria`, `s81_2a_mimo` |
| 2 | 2b, the open audit | brief 2b with its rows + file 11 + the case book + the other model's 1C return + the auditor's own 2a return | about 15,000 + the two returns (about 30,000 to 35,000 in all) | `s81_2b_atria` (audits Mimo), `s81_2b_mimo` (audits Atria) |
| 2 | 2D, the difference audit | brief 2D + file 10 + file 11 + the other model's 1D list + the auditor's own 1D list, unlabelled | about 17,500 + the two lists (about 25,000 to 30,000) | `s81_2D_atria`, `s81_2D_mimo` |
| 2 | 2W, widening, only if the stopping rule fires | as 2b, with the widened rows | as 2b | `s81_2W_<auditor>` |

Every call is under the ~60,000-word ceiling, so no call splits its cases into batches; each 1C, 1K and 2a call carries all 52 cases and its theory whole. At roughly two tokens per word for these texts (the theory is dense with notation) the largest call is near 70,000 tokens of input.

**Why the control arm (1K).** SAME and CHANGED compare file 11 with file 10. S76 took file 10's side from S72's table, thirty-three of whose rows no auditor opened (S78 item 9), written under a different instrument. 1K runs the identical brief on file 10, by the same models, on the same cases, so each model's two arms differ in the theory alone; neither arm can tell which it is in. This is S78 repair A1's "worked from file 10" for all 52 rows, in a form the tested agent cannot read as a hint that two versions exist.

**Why the difference call (1D) is in Stage 1.** S76 Stage 1 Part 2 tested file 11's note that one claim changes; S78 (item 6 and its correction to S75 point 2) says that count is under test and names one sentence against it. The cases cannot test it alone, since a claim change that no case touches changes no verdict.

## Who does which stage, and why

Atria and Mimo each run all of Stage 1 independently (1C, 1K, 1D) and the blind reading 2a. Then each audits the other's Stage 1: Atria's 2b and 2D check Mimo's 1C and 1D, and Mimo's check Atria's.

- **Two independent testers.** Two blind readings of file 11 on every case, by two model families, measure how much of a mark is the theory and how much the reader (S78 reader 4's first repair), before any audit.
- **Cross-audit, never self-audit.** A model auditing its own return reads its own reasoning twice. A different family shares fewer blind spots with the tester, and the auditor has never seen the tested return when it writes its blind reading.
- **Both roles for both models.** Role and model are crossed, so a lenient model and a lenient role can be told apart in the table.
- **Blind first, by call.** In a single-call API a column cannot be withheld inside one prompt. 2a is written from the theory and the situations alone, before the auditor sees any fixed verdict or any Stage 1 reading; 2b opens both and starts each row from 2a. 2a covers all 52 cases: the cost is small, and a verdict-blind reading of every row is what puts the forty-odd agreeing rows under pressure (S78 reader 5), which a sample would cover thinly. Set beside the same model's 1C, it also measures how far seeing the fixed verdict moved that model's reading.
- **Claude decides** (decision S13). The models' marks are evidence; Claude reads the theory's text on every row the rules below name, and rules.

## The frozen prediction

Kept here and out of every brief; `s81_build.py` asserts that no brief carries "O48 change", "S75", "prediction", "R2", "S76" or any round number, file number, "Revision", "Derivation 3" or "amendment", and that no Stage 1 or 2a brief carries "O48" or "O24" at all.

The baseline is S75's determination on file 10 (from the S72 table as audited): **DISAGREE** on O48; **SILENT** on O1, O12, O20, O21, O27, O35, O40 and O50; **AGREE** on the other forty-three, O24 among them.

- **P1, the one change.** Under file 11, Claude's ruled mark on O48 is AGREE, and it rests on the qualified claim of Derivation 3 or on one of the three sentences restated with it (the answer to grievance 3, attack point (D), the Part XV entry). Under file 10 it is DISAGREE, resting on the unqualified claim. O48 is CHANGED toward the thoughtful person, in its verdict and in the passage it rests on.
- **P2, nothing else.** Every other case keeps its baseline mark under file 11 on Claude's ruling: forty-three AGREE, the same eight SILENT, and no DISAGREE, SPLIT or CASE DISPUTED that file 10 does not also give.
- **P3, the claim count.** Of the places where file 10 and file 11 differ, the ones Claude rules CLAIM after reading both 1D lists and both 2D audits are Derivation 3 and the three sentences restated with it. Every other place is WORDING or ORDER. Recorded before the run, against P3: S78 item 6 found one sentence file 10 does not carry, in Part XI's Repair paragraph, "each as a stated condition over stated occasions, and a protected condition is lost exactly when it fails on an occasion it covers" (file 11, the paragraph opening at line 427, the sentence at line 433; file 10's Repair paragraph, line 438, has no such clause); the "Declared inputs" paragraph of Part XIV (log S76) is a second candidate. P3 stands only if Claude rules both WORDING.
- **P4, the instrument (a claim about the readers, not the theory).** Within each model, the 1K and 1C marks differ on O48 and on no other case.

Two expectations, written first and not predictions of file 11: **E1**, at least one model marks the occasions clause CLAIM in 1D; **E2**, a model's 2a reading, marked in 2b, differs from its own 1C mark on more rows than its 1K and 1C marks differ from each other (seeing the fixed verdict moves a reading more than the change between the two files does). Both are reported with their counts.

## The words Claude rules with, fixed before the data

- **The file-11 mark** of a case: Claude's ruling, from file 11's text, informed by both 1C returns and both 2b audits.
- **The file-10 mark**: S75's baseline, unless both 1K returns agree on a different mark and Claude's own reading of file 10 confirms it; then the baseline is corrected, and the correction to S75 is recorded in S81 Results with the row.
- **Verdict SAME or CHANGED**: whether the two ruled marks differ, and, where both are DISAGREE, SPLIT or SILENT, whether they concern the same point. The rule "a clarification is not a changed verdict" is the brief's "Same finding", fixed in advance.
- **Passage SAME or CHANGED**: whether the sentence of file 11 the verdict rests on claims something different from its counterpart in file 10. The program marks every quoted sentence found in file 11 and absent from file 10; Claude decides whether its claim differs, with the 1D and 2D returns beside it.
- **Direction**: toward the thoughtful person when the file-11 mark is nearer AGREE than the file-10 mark, away when it is further (AGREE, then SILENT or SPLIT, then DISAGREE).
- **A theory change** is a case CHANGED in its verdict where the change traces to a passage CHANGED. **Reader variation** is a difference of marks where both verdicts rest on sentences the two files share word for word; it is recorded as a finding about the readers, or about S75, and counts neither for nor against file 11.

## The 2b sample, fixed here and applied after the returns

The rows the auditor of model X's 1C return audits in full, drawn by `s81_build.py build2` once both 1C and both 1K returns are in, and written only into that auditor's 2b brief:

- **M1**, every row X's 1C marks other than AGREE;
- **M2**, every row where X's 1C mark differs from the other model's 1C mark, or from X's own 1K mark;
- **M3**, every row whose quotations include a sentence found in file 11 and absent from file 10 (the S81 form of S78 A3's "names a sentence of file 11 that differs from file 10");
- **M4**, every row with a quotation the program cannot find in file 11, or with none;
- **M5**, every row whose strongest contrary reading X itself says HOLDS;
- **M6**, every row the baseline marks other than AGREE (O1, O12, O20, O21, O27, O35, O40, O48, O50);
- **R**, from the rows left, the ten whose `sha256("S81-2b-residual|" + sha256(X's 1C return) + "|" + case)` sort first. The key is the return's own hash, so the draw is fixed by rule and unknowable before the return exists.

Every other row gets the one-line comparison of 2b Part 2. **Stopping rule:** if an auditor marks DISAGREE (ON VERDICT or ON MARK) on any R row, Claude builds `widen` for that auditor with every row outside the sample whose 1C quotations cite the same Part of file 11 as that row, and runs 2W. The rule and its sample are saved as `sample - <auditor> audits <tested>.json` beside the returns.

## How Claude determines the result

1. **Receipts.** Every call accepted by `s80_call.py` (finish "stop", the last line `END OF REPORT`), its model as served, its request and response hashes. An empty or failed return is kept and run once more, recorded as a second attempt.
2. **By program** (`s81_build.py table`): each case's marks in 1K and 1C for each model and in each 2b; every 1C quotation marked VERBATIM, LOOSE (letters and digits match) or ABSENT against file 11; the count of quotations absent from file 10.
3. **By Claude, against the two files directly, row by row:** O48 in full; every row where any reading of file 11 (either 1C, either 2b) differs from the baseline; every row where either 1K differs from the baseline; every CASE DISPUTED; every row named under "Disagreements the reading under audit left unmarked" or "Wrong, and uncorrected anywhere in the theory"; every row with an ABSENT quotation. For each: the file-11 mark, the file-10 mark, verdict and passage SAME or CHANGED, direction, theory change or reader variation.
4. **The differences:** every CLAIM place on either 1D list, and every place in either 2D's "Surviving differences in claim" or "Differences in claim that both lists missed", read against both files and ruled CLAIM or WORDING.
5. **The eight SILENT cases:** from their SEARCH records in both arms, whether file 11's Declared inputs paragraph (Part XIV) now names the input each case lacks, which S76 Stage 1 asked the tester and which is asked here of the determiner, because the question names the earlier finding.
6. **CASE DISPUTED rulings:** a case Claude rules wrongly fixed is set aside from every count, named, and corrected only in a new numbered case file.
7. **Written up** as `results/S81 Results - ...md`: P1 to P4 and E1, E2 ticked, the ruled table, every ruling on a disputed row, the standing verdict, and "Not tested"; and the log entry S81.

## What counts as file 11 standing as the authority

File 11 stands, on Claude's determination, when all four hold:

- **(a)** O48 is AGREE under file 11: the change it was written for is delivered, whatever the control arm shows.
- **(b)** No case shows a theory change away from the thoughtful person.
- **(c)** No sentence of file 11 is ruled to give a wrong verdict on a case where file 10's corresponding sentence gave the thoughtful person's.
- **(d)** No cross-reference in file 11 is ruled to point wrong in a way that changes what a sentence claims. A pointer that is only a slip is recorded as an erratum for a later revision.

With (a) to (d), and P2 and P3 holding, file 11 stands as written and its note is confirmed. With (a) to (d), and P2 or P3 failing only by a theory change toward the thoughtful person or by an undeclared CLAIM that no case shows harmful, file 11 stands with those findings recorded against its note; the note is frozen, so the correction lives in S81 Results, and in a revision 2 if the owner asks for one. Where (a), (b), (c) or (d) fails, file 10 remains the authority and S81 Results lists what a revision 2 would have to repair. If 1K shows O48 AGREE under file 10 (a fresh reader supplying the qualification the proof already assumes, as S75 said the proof does), P1's file-10 half fails under this instrument, rests on S72 and S75 as audited, and is reported so; it bears on P4 and leaves (a) untouched.

## The S78 repairs, and where each is applied

| Repair (S78) | Where, or why not |
| --- | --- |
| A1: strip the answer from the tested agent's brief; S75 and the S72 Stage 2 return out of the tester's pack; column 3 from file 10 | Applied. The prediction is in this plan only. No call carries any earlier return, S75, R2, a file number or a round number (asserted by the build). File 11's revision note, which carries the answer, is withheld from every call. Column 3 becomes the 1K control arm, file 10 read under the same brief on all 52 rows. The case book drops each case's header annotation, which for O24 and O48 quotes R2 J (provenance file). |
| A2: two-pass audit, Stage 1's columns withheld; sample chosen after the return; every-fifth dropped | Applied, by call: 2a blind (every case, verdicts withheld too), then 2b open. The sample is drawn by the rule above after the returns, keyed to the return's hash; there is no fixed sequence to print. |
| A3: mandatory set widened; stopping rule | Applied: M1 to M6, and 2W. |
| A4: SAME and CHANGED as two columns fixed in the instruction; SILENT with a recorded search | Applied. The tester's marks and "Same finding" are defined in brief 1-cases before the data. SAME and CHANGED, verdict and passage, are the determiner's columns, fixed above and computed from the two arms; the tester is asked for neither, since it sees one version. SILENT carries SEARCH. |
| A5: "Changes Stage 1 did not mark"; "Wrong, with no amendment that fixes it"; CASE DISPUTED | Applied, in the S81 forms: "Disagreements the reading under audit left unmarked", "Wrong, and uncorrected anywhere in the theory" (2b), "Differences in claim that both lists missed" (2D), each counted at zero; CASE DISPUTED is a mark in 1C and 2b with its required field, and "Cases to rule on" carries it to Claude. |
| A6: quotation counts in two, source-checked and chained | Applied in form: every quotation in S81 is of a text inside its own call, so all are source-checkable and none is chained; the program counts VERBATIM, LOOSE and ABSENT for every one. |
| A7: manifest line (model, date, fresh chat) | Replaced by the `s80_call.py` receipt: model as served, time, request and response hashes; every call is fresh and single-turn by construction. |
| A7: negative-wording search at build time | Applied: `s81_build.py` prints every negative word in every brief; zero at freeze, apart from the values NONE and NO. |
| A7: the read-me sentence made conditional | Not applicable: no pack, no read-me travels. |
| A7: D3-T entered as O53 with its verdict frozen | **Not applied.** D3-T's situation and verdict were written by the S72 auditor ("Written by: me" in its fix card), so its verdict is not yet fixed by the determiner; entering it needs Claude to fix the verdict first. It is the one case aimed at the qualified Derivation 3's weakest sentence, so it is the first case to add; held for the orchestrator. |
| A7: Part 4's fix card conditional on Part 1 | Not applicable: S81 commissions no fix card. A repair, if one is needed, is Claude's after the determination. |
| B: the seeded-error round | Run separately as S79 (log S79). S81's "nothing else changes" is read with S79's result on what the pattern can catch. |
| C: cases by an agent that has never read file 10 | Not applied; the owner's call. CASE DISPUTED is the only channel against a Claude-written verdict in this round. |
| Item 8: R2 copy-checked | R2 is absent from S81 altogether. |
| Item 9: S76 imports an unaudited baseline | The 1K arm reads file 10 afresh on all 52 rows, by both models. |
| Item 10: R2 J's Part VIII qualification has no case | Not tested (below). |
| Reader 1, finding 5: expectation first, the best case against each agreeing row | Applied: EXPECT, AGAINST and HOLDS in every 1C record; HOLDS YES puts a row in the sample (M5). |
| Reader 4: Stage 1 twice, by two agents | Applied: two models, and each also in the control arm. |
| Reader 5: the fixed verdict withheld from the auditor on some rows | Applied on every row (2a). |
| Smaller items: the coverage file unaudited; the five zero gauges; `build.py`'s single cut | S81 prints no coverage file (Claude updates coverage in results only where a verdict changes); every heading states its count and the "Wrong, and uncorrected" heading names the Parts read; briefs are lifted between explicit markers, so the orchestrator's notes and the brief never share a cut. |

S76 parts not carried: its Part 1 column 3 (S72's verdicts quoted; A1), its Part 3 coverage reprint, its Part 4 quotations file (the quotations are checked in place by program), and its closing question on the eight SILENT cases, which named the earlier finding and moves to the determiner (step 5).

## Run order

1. `python Semantics/tools/s81_build.py build`: the eight Stage 1 and 2a texts, word counts, hashes, the checks. The texts are frozen from here.
2. `python Semantics/tools/s81_build.py run 1`, then `run 2a` (three calls at a time per model, decision S12).
3. `python Semantics/tools/s81_build.py build2`: the sample drawn and saved; the four 2b and 2D texts built and checked. Then `run 2`.
4. If the stopping rule fires: `widen <auditor> <rows>`, then `run 2W`.
5. `table`; Claude's reading; S81 Results; log entry S81 and Status.

Outputs go to `results/S81 File 11 against every case - outputs/` (`briefs/` the exact texts sent, `returns/` every return with its receipt, the sample files, `table.md`), kept as they came.

## Not tested

- Whether the fixed verdicts are right. They are Claude's (cases O15 to O52 by Claude with the verdict fixed first; O1 to O14 by Claude as "a different author"); CASE DISPUTED is the only channel, and group C is not applied.
- R2 J's Part VIII qualification (the accumulated-error bound with unmatched initial states): no case touches it.
- D3-T, the case aimed at the qualified Derivation 3's weakest sentence: not entered (above).
- The parts of file 11 no case reaches: the coverage of the recovered Stage B rows stands at 55 of 80 (log S74), and the first 32 rows are still unrecovered.
- Repetition: one call per arm per model. Reader variation is measured between the two models and the two arms, not within a model across runs; temperature 0.7.
- Other model families, and any reader armed with the audit workflow (file 24): the briefs are self-contained and carry none of it.
- Whether the pattern can catch a known error: that is S79's question, not this round's.
- File 12 (the causality version) and the richness question (FW5).
