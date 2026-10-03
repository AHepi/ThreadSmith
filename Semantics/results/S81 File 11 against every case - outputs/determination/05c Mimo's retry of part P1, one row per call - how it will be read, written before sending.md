# 05c Mimo's retry of part P1, one row per call - how it will be read, written before sending

*Written by a Claude subagent for the orchestrator on 23 September 2026, before any of the three calls was sent. It is committed with the three texts and their job list. When it was written, no reply to any of the three texts existed, and the folder `results/S87 Cross-examination - the S81 determination - returns/Mimo retry one row per call/` did not exist. Mimo is "auditor 2" in the briefs.*

*What the writer opened and did not open.*
- **Opened:**
  - part P1's text, with its receipt and error file;
  - 05, 05b and 08;
  - the runner `tools/s87_run.py` and the job list of the three parts;
  - file 10, file 11 and the case book, to check the texts.
- **Searched only, for the file-10 lines each row cites:** 04, 04b (O1 and O4 groups), 04c and 04d.
- **Opened in part:** 06, at its table lines for O48 and O45, to confirm Atria's closing lines on those two rows. The lines around them in that table also show Atria's closing lines on O5 and O30. Nothing in the three texts turns on them: the texts are part P1, changed only as set out below.
- **Not opened:**
  - any attempt file of part P1, P2 or P3, including P1's partial text from attempt 6;
  - Atria's reply;
  - the rest of 06, and 07.
- **Part P2's reply** was not opened. 08, which reads it, was.

---

## 1. Why part P1 is sent again

**Part P1 failed.** P1 was `s87_xexam_mimo_P1`, sending `tests/S87 Cross-examination - part P1, O5 O30 O17.md` (committed in 6a9f75c; sha256 dc84398705b6…, the `user_sha256` of its receipt). Its receipt and error file were committed in e373275. The receipt shows six attempts, 8,634.6 s in all, at max_tokens 131,072:

| attempt | status | what came back | result |
|---|---|---|---|
| 1–4 | 0 | nothing | no answer |
| 5 | 200 | finish None, 0 characters | rejected ("finish None") |
| 6 | 200 | finish "length" after 4,457.9 s, 6,910 characters | rejected ("finish length"): the reply ran into the 131,072-token limit before END OF REPORT |

- **The error file** reads "status 200 after 6 attempts (2 came back but were not accepted) / finish length".
- **Under rule 5 of 05 and item 1 of 05b, P1 supports nothing.**
  - Its rows are recorded as not examined by Mimo (08, section 2).
  - Its attempt files are kept and not read for arguments.
  - It counts neither for nor against the determination.

**Why these three rows.**
- O5, O30 and O17 are the rows test (b) turned on, with O35 (04, section 5).
- On each, the determination rules file 11 AGREE, against part of the readers.
- **A SILENT ruling on any of them would be a theory change away.** It would make the row AGREE→SILENT through new sentences of file 11, and test (b) would fail.
- Mimo's P2 reply examined O35 (08). In the cross-examination, only Atria has examined these three rows.

**Why one row per call.**
- P1 carried three rows and a limit of about 3,000 words. Its one answer that ran to the end used up the 131,072-token limit before END OF REPORT.
- Each retry text carries one row, with a limit of about 2,000 words.
- Part P2, with two rows, was accepted, using 106,392 reasoning tokens of the 131,072 (08, section 1).
- **Splitting is no guarantee.** Two of the four parts of the supplementary audit failed, and so did parts P1 and P3.

## 2. Part P3 is not sent again

- **Its rows moved toward the thoughtful person.** O48 is DISAGREE under file 10 and AGREE under file 11. O45 is SPLIT under file 10 and AGREE under file 11.
- **Atria upheld both rulings** (06, its table: "O48: RULING STANDS", "O45: RULING STANDS").
- **So they are recorded as not examined by Mimo,** with the standing clause and the scoring choice for prediction P2, as 08 section 6 records them.
- **The limit, stated.** A ruling that fell on O48 would bear on test (a) and prediction P1, and one on O45 on prediction P2. For those rows there is one outside reading, Atria's, not two.

## 3. The three texts

| tag | text, in `tests/` | row | words (`wc -w`) | runner's count | sha256 (first 12) |
|---|---|---|---|---|---|
| `s87_xexam_mimo_O5` | `S87 Cross-examination - retry, O5 alone.md` | O5, Greta's dough | 15,342 | 15,382 | 97297d856d51 |
| `s87_xexam_mimo_O30` | `S87 Cross-examination - retry, O30 alone.md` | O30, the routine uploaded that morning | 15,134 | 15,173 | a6db38cc09e2 |
| `s87_xexam_mimo_O17` | `S87 Cross-examination - retry, O17 alone.md` | O17, the robot's log and the maker's manual | 14,868 | 14,905 | e1adbdde463b |

- **File 11 is embedded verbatim in each.** The block between the BEGIN and END markers has md5 5e494c1095d920d128b9a79de378f923 in all three, the md5 of `authority/11 … revision 1.md`. So file 11's line numbers are unchanged.
- **The source md5s were checked again when the texts were built.** File 10, file 11, the case book, the plan (second version), `s81_1C_A.txt`, 03 and 04 all match the notes for the record, unchanged from P1.
- **Most of each text is file 11,** as in P1 (16,687 words by `wc -w`).

## 4. How each text differs from part P1

A program built the three texts from P1's committed text, after checking its sha256 against the receipt. The program is not committed. It changed only the places below, each checked to occur exactly once, and it checked the result.

**Kept byte for byte:**
- the title;
- section 2, the rules;
- section 3, file 11 in full;
- section 6, the determination's summary, including the standing clause and the scoring choice for prediction P2;
- the text's one row in section 5, whole. Its situation and fixed verdict were checked against the case book;
- each file-10 excerpt kept. Each was checked against its line of file 10.

**Changed in the notes for the record:**
- **"Written"** now says the file is "one of three texts cut from one of three parts of a brief of that date, one for each of that part's pressed rows". No other reply, "to that brief, to another part or to another of these texts", is shown with it.
- **The case book as a source:** "whose case for the pressed row in this text is given word for word in section 5".
- **The reading rule.** The sentence after item 6 now reads: "The reply to this text is read by this rule on its own, independently of every other reply: the replies to the brief, to its parts and to the two other texts cut with this one, and the other auditor's reply."
- **"Length"** gives the text's own count by `wc -w`.

**Changed in section 1:**
- **The row sentence** says the text carries one of the seven pressed rows, one of the three test (b) turned on, and that in it "the pressed row" means that row. It says "The other six rows and the standing clause are examined in separate texts" and "Test its ruling on O<n>".
- **Two contents bullets** say "the pressed row" for sections 4 and 5.

**Changed in section 4:**
- **The opening paragraph** speaks of one row, and adds: "The excerpts that only other pressed rows need have been cut."
- **The counterpart notes, and the line on lines shared or extended,** are cut to the row.
- **The excerpts** are cut to the row (section 5 of this note).

**Changed in section 5:**
- **The heading** is "The pressed row", and the opening paragraph starts "For the row".
- **The test (b) paragraph** opens "This row is one of the three (O5, O30, O17) that decide test (b)." The rest of it is unchanged.
- **The other two rows** are dropped.

**Changed in section 7, the task:**
- **The opening paragraph** says "and the case" where P1 says "and the cases".
- **Task 1** is P1's, cut to the one row. For that row it asks the auditor:
  - to try to show from the texts that the ruling is wrong;
  - to quote file 11 with line numbers, and file 10 where it is excerpted.

  Its question is P1's question, on that row alone.
- **The form of the report:**
  - points numbered most serious first;
  - after them, one line reading exactly "O<n>: RULING STANDS" or "O<n>: RULING FALLS — <mark>";
  - under about 2,000 words (P1: about 3,000);
  - the last line END OF REPORT.
- **The example closing line** is "O<n>: RULING FALLS — file 11 SILENT" in each text, as P1's was for O5. SILENT is the contrary the determination names on each row. On O30 it names "SILENT or SPLIT".

**Names.** Outside the file-11 block, no text names any model or provider. A program checked this. The briefs' substitutions are kept: "the determiner", "auditor 1" and "auditor 2".

## 5. Section 4 in each text

A text keeps a file-10 excerpt only when its row needs it, by the rule of 05b ("Section 4 in each part"): section 5 cites it on the row; or the determination cites it on the row (04, 04b, 04c or 04d); or it is the file-10 counterpart of a file-11 sentence the row rests on, as the counterpart notes name it. Every file-10 line that a kept note names is excerpted. A heading is kept when a line under it is kept.

| row | file-10 lines kept | why | no-counterpart notes kept |
|---|---|---|---|
| O5 | L40–L41, L138, L140, L176, L272, and Part XIV (L516, L518, L519, L521, L523) | 04b cites L41, L140 and L272. L41 and L176 are the counterparts of f11 L161, and Part XIV of f11 L514. L40 and L138 are the lines that introduce L41 and L140. | f11 L161 s3 (M17); f11 L514 (M48); and "Shared word for word … f10 L272 = f11 L259. Nearly so: f10 L41 = f11 L45 …" |
| O30 | L414, L476, and Part XIV | 04b cites L414 and L476. Part XIV is the counterpart of f11 L514, and L523 of f11 L465. | f11 L419 (M37); f11 L465 (M44); f11 L514 (M48); and "Extended in file 11: f10 L414 = f11 L401 s1–s3 …" |
| O17 | L414, L476, and Part XIV | 04b cites L476. L414 comes from the counterpart note on f11 L419. Part XIV is the counterpart of f11 L514, and L523 of f11 L465. | f11 L419 (M37); f11 L465 (M44); f11 L467 last sentence (M45); f11 L514 (M48); and the "Extended" line as for O30 |

- **Coverage.** Together the three texts carry every excerpt in P1's section 4, and no other file-10 text.
- **The thinnest grounds.** O17's L414 is there only through the counterpart note on f11 L419. It carries the "Extended" line with it.

## 6. How each reply will be read

Each reply is read by 05 as extended by 05b, as follows.

1. **The receipt comes first.** A call is read only if it is accepted within its one pass: finish "stop", and END OF REPORT on the last line of its reply (rule 5 of 05).
2. **A failed call supports nothing.**
   - Its row is recorded as not examined by Mimo.
   - Its attempt files are kept and not read for arguments.
   - It counts neither for nor against the determination, and no ruling cites it.
   - Each call goes one pass only, so a call that fails is not sent again under this job list.
3. **The reply is evidence, not a result** (rule 1).
4. **Some rows go to a fresh determiner** who did not write the determination (rule 2):
   - the row, if the reply says RULING FALLS;
   - any new away-row the reply names, although none is asked for.

   The determiner reads file 10, file 11, the case book, the determination (04 and its raw readings) and the reply. It first states the determination's ruling, then the reply's argument, and then rules.
5. **A change of ruling is recorded** with its reason, and with the fact that it came after the cross-examination (rule 3).
6. **A changed row that is a theory change away** from the thoughtful person fails test (b). The standing verdict is then applied again under the plan's three clauses (rule 4).
7. **Each reply is read independently of all other replies.** Rule 6 and 05b item 7 extend to the three calls.
   - Until its own reading is written, the reader of a reply opens none of these:
     - the other two retry replies, or their readings;
     - Atria's reply, or 06;
     - part P2's reply, or 08;
     - any attempt file of part P1.
   - The readings are set side by side only after all of them are written, and with 06 and 08 only then. Where two readings rule differently on one row, both rulings are recorded, and the difference is resolved in writing from the texts.
8. **Points beyond the row** are evidence of the kind 05 names under "Beside the rule". This covers the standing clause, the scoring choice for prediction P2, and other rows. S81 Results answers each point that would change a test, a prediction's score or the clause applied, with its reason.

## 7. Confounds, stated before the data

- **Each call sees one row.** It sees all of file 11, its own row, the file-10 lines that row needs and the summary. It cannot draw on work done on the other two rows.
- **Cases cited but not given.** The rows' reasons cite other cases as contrasts, and those cases' texts are not in the text:
  - O5 cites O1;
  - O30 cites O17, O35, O41 and O51;
  - O17 cites O30 and O41.

  The reasons quote the words they rely on. A reply that argues from a case not given is checked against the case book.
- **The same auditor has seen this material before.** It was sent P1, and before that the whole brief, and both calls failed. Each call is new and carries no earlier attempt.
- **Section 6 is carried whole.** It names the other rows and the standing clause, which are not asked about.
- **Word limits.** About 2,000 words for one row, where P1 allowed about 3,000 for three.
- **Selection by the ceiling.** A call is accepted only if its reasoning fits within 131,072 tokens. The accepted calls are the runs that happened to fit.
- **Timing and order.** The calls go out after Atria's reply and 06, after part P2's reply and 08, and after P1 failed. Mimo sees none of them.
- **Three formats.** Atria answered the whole brief. Mimo answered part P2 as a part of two rows, and would answer P1's rows one per call. The side-by-side comparison must say so.
- **One model family on the ruling side** (04, section 8). The readers of the replies will be Claude subagents, like the determiner.

## 8. Settings

- **The job list:** `tools/s87_jobs - Mimo retry, one row per call.json` (sha256 2e2e61c841f8…), run by `tools/s87_run.py`.
- **The call.**
  - Provider mimo.
  - Thinking is on, with `reasoning_effort` medium, from `s80_common.effort_for("audit", "mimo")` under decision S17.
  - max_tokens is 131,072 on both rungs ([131072, 131072], Mimo's ceiling).
  - The temperature is 0.7.
  - There is no system message: the text is the one user message.
- **Attempts.** Each call may make up to 6 attempts, and at most 3 of them may come back and fail. Each goes one pass only (`max_pass` 1).
- **Acceptance.** A call is accepted only if it finishes with "stop" and the last line of its reply is END OF REPORT.
- **Slots.** At most three Mimo calls are in flight across every process, through the shared slot lock. Other processes that send to Mimo share those slots, so a call may wait for one.
- **The returns go to** `results/S87 Cross-examination - the S81 determination - returns/Mimo retry one row per call/`.
- **Dry run.** The runner's dry run on this job list passes with no keys set. It shows all three calls to go as pass 1 of at most 1, with no files already in place. The returns folder does not yet exist.

## 9. Who decided, and when

- **Who.** Claude decided this under decision S18 on 23 September 2026.
- **What was weighed.** An independent second reading of the rows that decided test (b), against about three more Mimo calls.
- **When.** After P1 failed and before any of the three calls was sent.
- **What was known.** No reply to any of the three texts existed. No attempt file of P1 was opened.
- **Status.** The texts are prepared, not sent.

## 10. Files

- `tests/S87 Cross-examination - retry, O5 alone.md`, `… retry, O30 alone.md` and `… retry, O17 alone.md`: the three texts, exactly as they would be sent.
- `tools/s87_jobs - Mimo retry, one row per call.json`: the job list, with tags `s87_xexam_mimo_O5`, `s87_xexam_mimo_O30` and `s87_xexam_mimo_O17`. For each it gives:
  - provider mimo;
  - effort medium;
  - ladder [131072, 131072];
  - 6 attempts, at most 3 that come back and fail;
  - `max_pass` 1.
- `results/S87 Cross-examination - the S81 determination - returns/Mimo retry one row per call/`: written by the runner, once the calls are sent.
- **The rules this note extends:** 05 and 05b in this folder.
