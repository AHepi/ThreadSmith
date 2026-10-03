# 05b Mimo's reply in three parts - how it will be read, written before sending

*Written by a Claude subagent for the orchestrator on 23 September 2026, before any part was sent. It is committed with the three parts and their job list, and it applies only if Mimo's single call fails. When it was written, no reply from Mimo existed to be read, no file of the single call had been opened for it, and the folder `results/S87 Cross-examination - the S81 determination - returns/Mimo in three parts/` did not exist.*

## When this note applies

- **Mimo's single call, `s87_xexam_mimo`, sends the whole brief under 05.** The brief is `tests/S87 Cross-examination - the S81 determination, file 11 against file 10.md`.
- **What is known of it so far.** Two of its attempts ran to the 131,072-token limit and wrote no reply. The call may still be in its last attempt: its job allows at most 3 answers that come back and fail (`max_rejects` 3, `max_pass` 1). This comes from the orchestrator's report only. No file of the call was opened for this note.
- **If the call is accepted,** the parts are not sent, and this note lapses. Its reply is read under 05 alone.
- **If the call fails,** rule 5 of 05 applies to it:
  - it supports nothing, counts neither for nor against the determination, and no ruling cites it;
  - its attempt files are kept and not read for arguments.

  The three parts are then sent, and each reply is read as below.

## Why three parts

- **S88 failed the same way, and the split worked there.**
  - Mimo's single S88 call ran out of room before writing any reply (48236c7): its reasoning either used up the 131,072-token ceiling or stopped first.
  - Split finding by finding, all three S88 parts came back with an accepted reply (68ab4da).
- **Splitting is no guarantee.** The supplementary audit of Mimo on tester A was split in four, and two of the four parts failed.
- **Each part carries a smaller task.**
  - It has two or three pressed rows, where the brief has seven.
  - Only part P3 is asked about the standing clause.
  - No part is asked to hunt for other away-rows, and none gets the "anything else" task.
  - Each has a limit of about 3,000 words, where the brief allowed about 6,000.

## The three texts

| part | tag | brief, in `tests/` | rows | words (`wc -w`) | sha256 (first 12) |
|---|---|---|---|---|---|
| P1 | `s87_xexam_mimo_P1` | `S87 Cross-examination - part P1, O5 O30 O17.md` | O5, O30, O17 (the rows test (b) turned on) | 16,687 | dc84398705b6 |
| P2 | `s87_xexam_mimo_P2` | `S87 Cross-examination - part P2, O35 O40.md` | O35, O40 | 16,285 | acdcc3db259c |
| P3 | `s87_xexam_mimo_P3` | `S87 Cross-examination - part P3, O48 O45 and the standing clause.md` | O48, O45, and the standing clause | 16,359 | 17885e20f729 |

- **Runner's counts.** The runner counts 16,731, 16,327 and 16,407 words.
- **File 11's share.** Most of each part is file 11, which every part carries in full.
- **Part labels and prediction names.** The labels P1 to P3 appear only in the file names, the tags and this note. The texts never use them, because in the texts P1 to P4 are the plan's predictions. In this note, "part P2" is a part and "prediction P2" is the plan's prediction.

## How each part differs from the brief

A program built the three parts from the committed brief. That brief has md5 6acd78f5217acf2ce4e95acdbc1454f3, sha256 8e70216af88f…, and 25,477 words by `wc -w`. It is the text that `tools/s87_jobs - S81 determination cross-examination.json` sends in both S87 calls.

**Kept byte for byte in all three parts:**
- **Section 2,** the rules, word for word.
- **Section 3,** file 11 in full.
  - The embedded block has md5 5e494c1095d920d128b9a79de378f923 in every part, the md5 of `authority/11 … revision 1.md`.
  - So file 11's line numbers are unchanged.
- **Section 4's opening paragraph and every excerpt kept.** The build checked each excerpt against its line of file 10.
- **Section 5's opening paragraph and each of the part's rows, whole.** The build checked each row's situation and fixed verdict against the case book.
- **Section 6,** except one sub-bullet (listed under "Dropped").
- **Section 7's opening paragraph** ("Work from the texts: …").
- **The title, the notes for the record and section 1,** except the changes listed below.

**Dropped:**
- **The reference section.** This is the unnumbered section "For reference: the forty-five cases not pressed": 45 cases, 3,810 words. It served task 2.
- **The list of CLAIM places.** In section 6, the sub-bullet under P3 lists every place step 4 ruled CLAIM, by line: 49 places, M1 to M59. It served task 2. The P3 line above it is kept whole.
- **The other parts' rows** in section 5.
- **The test (b) paragraph, in parts P2 and P3.** It opens "The first three rows (O5, O30, O17) decide test (b). …" and is about part P1's rows.
- **Unneeded section 4 material.** The excerpts and counterpart notes that the part's rows do not need are dropped. Which lines each part keeps is set out in the next section.

**Changed in the notes for the record:**
- **"Written".** The brief says "This file is sent whole, as the one message, to each of two auditors, separately. Neither sees the other's reply." Each part says instead "This file is one of three parts cut from a brief of that date, and it is sent, as the one message, to one auditor. No other reply, to that brief or to another part, is shown with it."
- **The case book as a source.** "all 52 cases word for word, in the reference section after section 4 and in section 5" becomes "whose cases for the pressed rows in this text are given word for word in section 5". The md5 is unchanged.
- **Step 4 as a source.** "whose CLAIM places are listed in section 6" becomes "whose CLAIM places are cited by number in sections 4 to 6".
- **The reading rule.** The notes quote 05's rule. After its item 6 comes one new sentence: "The reply to each of the three parts of this brief is read by this rule on its own, independently of the replies to the other parts and of the other auditor's reply."
- **"Length"** gives the part's own count by `wc -w`.
- **The source md5s** were checked again when the parts were built. File 10, the case book, the plan (second version), `s81_1C_A.txt`, 03 and 04 all match the brief's notes.

**Changed in section 1:**
- **A sentence naming the part's rows** now follows "**Your job is to try to overturn that determination.**". It says three things:
  - which pressed rows the text carries;
  - that in this text "the pressed rows" means those rows;
  - that the other rows are examined in separate texts. In parts P1 and P2 it adds that the standing clause is too.
- **The contents list** changes in three places:
  - it drops "After section 4, for reference: the forty-five cases not pressed, word for word.";
  - it says "the three pressed rows" or "the two pressed rows", where the brief says "the seven";
  - it says section 6 comes "without its list of the CLAIM places by line".
- **In section 5 of part P1,** the test (b) paragraph opens "The three rows" instead of "The first three rows".

**Replaced in section 7, the tasks:**
- **Task 1, the pressed rows.** This is the brief's task 1 word for word, cut to the part's rows and the brief's questions on them:
  - part P1: O5, O30 and O17, with the one question the brief asks on all three, so its lead-in reads "The question these rows raise:" where the brief has "The questions each row raises:";
  - part P2: O35 and O40, with the brief's two questions;
  - part P3: O48 and O45, with the brief's two questions.
- **Task 2, the standing clause, in part P3 only.** This is the brief's task 3 word for word, including the scoring choice for prediction P2 and its frozen reading.
- **Not asked:** the brief's task 2 (other rows that move away) and task 4 (anything else).
- **The form of the report:**
  - one part per row, in the brief's order, with the points numbered most serious first;
  - each part closed with "O<n>: RULING STANDS" or "O<n>: RULING FALLS — <mark>", under the brief's definition of a ruling that falls.
- **The example closing line.** Each part's example uses its own first row and the contrary the determination names for that row:
  - part P1: "O5: RULING FALLS — file 11 SILENT", as in the brief;
  - part P2: "O35: RULING FALLS — file 10 AGREE";
  - part P3: "O48: RULING FALLS — file 10 SPLIT".
- **Part P3 only.** It adds a section on the standing clause, then the line "STANDING VERDICT: UPHELD" or "STANDING VERDICT: FALLS", with the brief's definition.
- **Every part.** The report stays under about 3,000 words and ends with END OF REPORT.

**Names.**
- Outside the file-11 block, no part names any model or provider. A program checked this.
- The block's title line is file 11's own, as in the brief.
- The brief's substitutions are kept: "the determiner", "auditor 1" and "auditor 2".

## Section 4 in each part

**When a part keeps an excerpt.** It keeps an excerpt only when its rows need it, in one of three ways:
- section 5 cites it on the row;
- the determination cites it on the row (04, 04b, 04c or 04d);
- it is the file-10 counterpart of a file-11 sentence the row rests on, as the counterpart notes in section 4 name it.

**What goes with it.**
- A heading is kept when at least one line under it is kept.
- The counterpart notes and the "Shared word for word" line are cut to the same rows.
- Every file-10 line that a kept note names is excerpted in that part.

| part | file-10 lines kept | the rows that need them |
|---|---|---|
| P1 | L40–L41, L138, L140, L176, L272, L414, L476, and Part XIV (L516, L518, L519, L521, L523) | O5: L140 and L272, and L41 and L176, the counterparts of f11 L161. O30: L414 and L476. O17: L476, with L414 from the counterpart note on f11 L419. All three rest on f11 L514, whose counterpart is Part XIV. O30 and O17 also rest on f11 L465, whose counterpart is L523. |
| P2 | L25, L122, L164, L176, L414, L432, L438, L440–L442, L444, L476, and Part XIV | O35: L25, L122, L164, L438–L444, L176 (04b's word search) and Part XIV (f11 L514). O40: L25 (f11 L27), L414, L432, L438–L444 (f11 L433 s4) and L523 (04b), with L476 from the counterpart note on f11 L419. |
| P3 | L23, L37–L38, L74, L210, L246, L248, L280, L304, L324, L326, L384, L482, L539, L541, L569, L571, L573, L613 | O48: L38, L74, L210, L482, L539, L541 and L569–L573, the Derivation 3 cluster and the counterpart of f11 L473. O45: L23, L246, L248, L280, L304, L324, L326, L384 and L613. |

- **Coverage.** Together the three parts carry every excerpt in the brief's section 4, and no other file-10 text.
- **Two lines in part P2 stand on the thinnest grounds.**
  - **f10 L476** is there only because of a counterpart note. O40's file-11 route runs through f11 L419 s2, and the note on f11 L419 names f10 L414 and L476. The determination does not cite L476 on O40.
  - **f10 L176** is there only because 04b's search for "during" on O35 names it.

## How each part's reply will be read

Each part's reply is read by 05, part by part, as follows.

1. **The receipt comes first.** A part is read only if it is accepted within its one pass: finish "stop", and END OF REPORT on the last line of its reply (rule 5 of 05). **A failed part supports nothing.**
   - Its rows are recorded as not examined by Mimo. For part P3, so is the standing clause.
   - Its attempt files are kept and not read for arguments.
   - It counts neither for nor against the determination.
2. **The reply is evidence, not a result** (rule 1).
3. **Some rows go to a fresh determiner** who did not write the determination (rule 2). This covers two kinds of row:
   - every row the reply says FALLS;
   - every new away-row it names, although no part asks for one.

   The determiner reads file 10, file 11, the case book, the determination (04 and its raw readings) and the part's reply. It first states the determination's ruling, then the reply's argument, and then rules.
4. **A change of ruling is recorded** with its reason, and with the fact that it came after the cross-examination (rule 3).
5. **A changed row that is a theory change away** from the thoughtful person fails test (b). The standing verdict is then applied again under the plan's three clauses (rule 4).
6. **Part P3's standing-clause points and its STANDING VERDICT line are evidence** of the kind 05 names under "Beside the rule". S81 Results answers, with its reason, each point that would change a test, a prediction's score or the clause applied.
7. **Each part is read on its own.** Rule 6 is extended to the parts.
   - A part is read independently of Atria's reply and of its reading, 06, and independently of the other two parts.
   - The reader of a part does not open Atria's reply, 06, or the other parts' replies or their readings.
   - The readings are set side by side only after all of them are written. Where two readings rule differently on one row, both rulings are recorded, and the difference is resolved in writing from the texts.
8. **The tasks not asked.**
   - **The brief's task 2,** the hunt for other rows that move away, is recorded as not examined by Mimo. Atria's reply examined it and found none (06, section 4).
   - **The brief's task 4,** anything else, is recorded the same way. Atria's points under it were answered in 06, section 5.
   - **If a part raises either anyway,** the point is read as in items 3 and 6.

## Confounds, stated before the data

- **Each part is a different call from the single call.**
  - It sees all of file 11, but only its own rows, the file-10 lines they need and the summary.
  - It cannot draw on work done on the other rows.
- **Cases cited but not given.** The rows' reasons cite other cases as contrasts, and those cases' texts are no longer in the part.
  - Part P1: O1, O35, O41 and O51. O17 and O30 cite each other, and both are there.
  - Part P2: O21, O27, O38 and O50.
  - Part P3: none in its rows. Section 6 names many.

  The reasons quote the words they rely on. A reply that argues from a case the part does not give is checked against the case book.
- **Section 6 in parts P1 and P2.** Both carry the whole of section 6, including the standing clause and the scoring choice for prediction P2, but they are not asked about either.
- **Word limits.** Each part allows about 3,000 words for two or three rows. The brief allowed about 6,000 for seven rows and three further tasks.
- **Selection by the ceiling.** A part is accepted only if its reasoning fits within 131,072 tokens. The accepted parts are the runs that happened to fit.
- **Timing and order.** The parts would go out after Atria's reply, after its reading (06), and after the single call fails. Mimo sees neither Atria's reply nor 06.
- **Two formats for the two auditors.** Atria answered the whole brief, and Mimo would answer the parts. When the readings are set side by side, the comparison must say so.

## Settings

- **The call.**
  - Thinking is on, with `reasoning_effort` medium, from `s80_common.effort_for("audit", "mimo")` under decision S17.
  - max_tokens is 131,072 on both rungs ([131072, 131072], Mimo's ceiling).
  - The temperature is 0.7.
  - There is no system message: the part's text is the one user message.
- **Attempts.** Each part may make up to 6 attempts, and at most 3 of them may come back and fail. Each part goes one pass only (`max_pass` 1), so a part that fails is never sent again.
- **Acceptance.** A part is accepted only if it finishes with "stop" and the last line of its reply is END OF REPORT.
- **Runner.**
  - The parts are sent by `tools/s87_run.py` with `tools/s87_jobs - Mimo in three parts.json` (sha256 079ebcd6f483…).
  - At most three Mimo calls are in flight across every process, through the shared slot lock.
  - The returns go to `results/S87 Cross-examination - the S81 determination - returns/Mimo in three parts/`.
- **Dry run.** The runner's dry run on this job list passes. It shows all three parts to go as pass 1 of at most 1, with no files already in place.

## Who decided, and when

- **Who.** Claude decided this under decision S18 on 23 September 2026.
- **When.** Before any part was sent, while Mimo's single call may still have been in its last attempt.
- **What was known.** No reply text from Mimo existed to be read. No file of the single call was opened.
- **Status.** The parts are prepared, not sent. They are to be sent only if the single call fails.

## Files

- `tests/S87 Cross-examination - part P1, O5 O30 O17.md`, `… part P2, O35 O40.md` and `… part P3, O48 O45 and the standing clause.md`: the three texts, exactly as they would be sent.
- `tools/s87_jobs - Mimo in three parts.json`: the job list. For each part it gives provider mimo, effort medium, ladder [131072, 131072], 6 attempts, at most 3 that come back and fail, and `max_pass` 1.
- `results/S87 Cross-examination - the S81 determination - returns/Mimo in three parts/`: written by the runner, if the parts are sent.
