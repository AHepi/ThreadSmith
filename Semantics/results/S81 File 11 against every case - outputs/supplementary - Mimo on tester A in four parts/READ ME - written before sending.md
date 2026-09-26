# Supplementary: Mimo's audit of tester A, sent in four parts

*Written by a Claude subagent for the orchestrator on 23 September 2026 at 14:02 UTC, before any part was sent. At that time this folder held only `briefs/` (the four texts) and `jobs for s87_run.json`. There was no `returns/` folder.*

## What this is

This folder holds four calls to Mimo. Each call sends the exact text of the plan's call `s81_2b_mimo_A`, which is Mimo's audit of tester A's 1C return, with two small changes. The rows it audits in full are one quarter of the 52 cases, not all 52. One sentence is added, which says that Part 2 is to be left empty.

| Part | Tag | Rows audited in full | Text sha256 (first 12) |
| --- | --- | --- | --- |
| 1 | `s81_2b_mimo_A_part1` | O1 to O13 | 130145ff0d56 |
| 2 | `s81_2b_mimo_A_part2` | O14 to O26 | 4cbe44c94b55 |
| 3 | `s81_2b_mimo_A_part3` | O27 to O39 | f028c1cbe704 |
| 4 | `s81_2b_mimo_A_part4` | O40 to O52 | e25b7743190f |

The four texts were built by `tools/s87_split.py` from `briefs/s81_2b_mimo_A.txt` (sha256 b1e5f0a991e2). That source is byte for byte the text the plan sent: its sha256 equals the `user_sha256` in both of the plan's failed receipts. The program checks that each part differs from the source in exactly two places, the rows line and the added sentence. It also runs the plan's checks for forbidden words on each part.

## Why

The plan's call failed twice.

- **Pass 1**, at high effort with a 131,072-token limit. Attempts 1 and 2 each ran to the limit ("length") after 3,189 s and 2,809 s, and wrote no answer. Attempt 3 stopped with no finish reason after 695 s, also with no answer.
- **Pass 2**, at medium effort with the same limit. All three attempts ran to the limit after 2,817 s, 3,047 s and 3,052 s, and wrote no answer. Each left between 540,000 and 554,382 bytes of reasoning.

At both efforts, Mimo's reasoning on the full 52-row audit used up the whole 131,072-token ceiling before any answer was written. The plan allows one further run after a failed return (second version, step 1; third version, change d). That run was pass 2, so `s81_2b_mimo_A` is missing from the plan's table. The table shows it as "MISSING (failed twice)".

Splitting the rows is the smallest change that might let the audit finish. Each part asks for 13 full records instead of 52.

## What these calls are not

- **They are outside the plan's table.** `s81_build.py table` reads only named files directly in `returns/`, and never this folder. The column "2b mimo on A" stays "MISSING (failed twice)".
- **They do not replace the missing audit.** They are not a third pass of the plan's call, because the text is different. The S81 findings rest on the plan's evidence. These returns are reported beside that evidence, as supplementary.

## The change to the text, and why it is the smaller one

The text differs from the source in two places, and nowhere else.

1. **The rows line of Part 1.** "These rows: O1, O2, …, O52." becomes the part's quarter, for example "These rows: O1, O2, O3, O4, O5, O6, O7, O8, O9, O10, O11, O12, O13."
2. **One sentence at the end of the Part 2 section**, after Part 2's one-line form and before the Part 3 heading. It is the same in all four parts:

   > In this call the rows outside the Part 1 list are audited in companion calls, so leave Part 2 empty.

**Why add the sentence rather than change the rows line alone.** Changing only the rows line would be one line fewer. But Part 2 says "For each case outside the Part 1 list, in order, one line", so each part would then have to write one-line comparisons (BLIND MARK, TESTER MARK, SAME or DIFFERENT) for the other 39 rows.

- The plan's call never asked for these lines. Its Part 1 held all 52 rows, so its Part 2 was empty.
- They would add to the reasoning that ran out.
- They would give up to four readings of each row, one full record and three one-liners, from calls that saw the row in different roles.

With the sentence, each part asks for a strict subset of what the plan's call asked for: 13 of its 52 full records, and its Part 3. So the change to the task is smaller, at the cost of 20 words.

The sentence sits at the end of the Part 2 section, so that it reads as the exception to the form just above it. It contains no negative word (lesson 27).

## Settings

- **Model and output:** Mimo (`mimo-v2.6-pro`), thinking on, `reasoning_effort` medium, max_tokens 131,072 on both rungs (Mimo's ceiling), temperature 0.7. There is no system message; the text is the one user message.
  - The effort comes from `s80_common.effort_for("audit", "mimo")`, decision S17. It is the same as the effort of the plan's pass 2 and of the other two medium 2b audits.
- **Attempts:** up to 6 attempts per part, and at most 3 answers that come back and fail the acceptance test.
  - A part is accepted only when it finishes with "stop" and its last line is END OF REPORT.
- **One pass each (`max_pass` 1).** A part that fails is never sent again.
- **Runner:** sent by `tools/s87_run.py` with `jobs for s87_run.json`.
  - At most three calls are in flight to Mimo across every process, through the shared slot lock. Three parts start at once and the fourth waits for a free slot.
  - Returns go to `returns/` in this folder. The file names follow `tools/s80_call.py`, and the response file is written last.

## The reading rule, fixed before sending

1. **When the parts are read.** No return in this folder is opened until Claude's step-3 rulings have been written and committed on the three accepted 2b audits: Atria on A, Atria on B and Mimo on B.
2. **What counts, per row.** Each row is taken from the part whose Part 1 list holds it, and only from that part's Part 1 record for the row. Four fields are compared with Claude's ruled file-11 mark for that row: YOUR MARK, ON VERDICT, ON MARK and BLIND MARK.
   - **YOUR MARK and BLIND MARK** differ when they are not the mark Claude ruled.
   - **ON VERDICT and ON MARK** say whether the audit agrees with tester A. They differ from Claude when they take the other side from Claude's ruling:
     - AGREE where Claude's ruled mark is not tester A's mark;
     - DISAGREE where Claude's ruled mark is tester A's mark.
3. **Every row where any of the four differs is re-read by Claude from the texts:** file 11, the case, tester A's row, and this audit's record. Any change of ruling is recorded with its reason. A ruling that stands is recorded as standing, with the reason.
4. **Agreement is reported as agreement.** A row where all four fields match Claude's ruling is reported as that and nothing more. It is not counted as a confirmation or as a test passed (lesson 35).
5. **A failed part supports nothing.** Its 13 rows are reported as "not audited by the supplement". Its attempt files (truncated answers and reasoning) are kept and not read for marks. A row whose record is missing or unreadable in an accepted part is treated the same way.
6. **What this rule does not use.** Any Part 2 lines a part writes despite the sentence, and each part's Part 3, are kept but not used. Each part's Part 3 covers only what that part noticed.

## Confounds, stated before the data

- **Each part audits only 13 rows in full.** Each part sees the whole theory, all 52 cases, the whole of tester A's reading and the whole of Mimo's blind readings, but writes full records for only its 13 rows.
- **This is a different call from the plan's single call.** That call audited all 52 rows in one reply, so each row's audit could draw on the work done on the others, and its Part 3 covered the whole return. Four parts give four separate Part 3s and no cross-row work.
- **Effort.** These parts are at medium, like the plan's pass 2 and the other two medium audits. Atria on A was at high. The blind readings embedded in the text (Mimo's 2a return) were made at high.
- **Selection by the ceiling.** A part is accepted only if its reasoning fits within 131,072 tokens. The accepted parts are therefore the runs that happened to fit, as with every accepted return in this round.
- **Timing.** The parts are sent later than the plan's calls, on the same text apart from the two changed lines.

## Who decided, and when

Claude decided this under decision S18 ("Keep going autonomously with auditing and improving the semantics"). The decision came after the data it responds to and before any part is sent. That data is the two failures, known only from their receipts: finish reasons, token limits, times and file sizes. No answer text existed to be read.

## Files

- `briefs/s81_2b_mimo_A_part1.txt` to `_part4.txt`: the four texts, as they will be sent.
- `jobs for s87_run.json`: the job list, with provider mimo, effort medium, ladder [131072, 131072], 6 attempts, at most 3 rejected, and `max_pass` 1.
- `returns/`: written by `tools/s87_run.py` when the parts are sent.

Rebuild check: `python Semantics/tools/s87_split.py --check`. It rebuilds the four texts and the job list in memory and compares them with these files.
