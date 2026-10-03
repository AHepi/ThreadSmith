# S93: how the cross-examination of draft 4 will be read

*Written by a Claude subagent for the orchestrator on 25 September 2026, from about 09:15 UTC, before anything was sent, and committed in the same commit as the eleven part briefs, the job list and the tool that builds them. When it was written, the folder `results/S93 Cross-examination - draft 4 - returns/` did not exist, no call of this round had been sent, and no runner was going. Nothing was written into `authority/`.*

## The number

S93, by LEGEND's rule (lessons S5 and S19): the next number after the highest entry in the three projects' logs, read at 09:05 UTC on 25 September 2026 in each project's story on this branch and on every remote branch (`git branch -a` after `git fetch`). This branch: Semantics S92, Language L86, Checked reasoning language 59, HV Skill 54. Other branches: HV Skill H69 (`origin/claude/hv-skill-scope-kl0oyr` and `-oz6b4c`), nothing higher elsewhere. No file, commit message or log on any branch uses S93, L87 or above, or H70 or above.

## What is cross-examined

Eighteen items, X01 to X18 in the order of the text. No outside reader has seen any of them in its present form.

- **The draft-4 entries.** Found by program: the change list at 99e9cd0 (draft 3) and as it stands (draft 4, md5 b6b2ea95ea9e21ebea3316d8e9fa4b40) were split at their `##` and `###` headings and compared. The entries that differ are W38.1, W36.1, W34.1 (renamed, "the job-counting lemma and Pres are dropped, and reach with them"), W33.1, and the new W59.1 and W60.1. The frame sections that differ (What this is, Counts, What the checks changed, the held items, Findings carried forward, Carried forward after S90) describe these and change no entry. W59.1 inserts two paragraphs and is examined as two items, "Rivals" (X09) and "Problems" (X10).
- **The ten S90 fixes.** The entries the S90 checkers fixed after the S90 cross-examination, as `results/S90 Verification of draft 3.md` (check 1) and the change list's table "After the cross-examination (S90)" list them: W37.1, W19.1, W35.1, W35.2, W20.1, W40.1, W24.1, W22.1, W6.3 and W7.5. They were verified in draft 3 and never re-sent to Atria or Mimo. Draft 4 left all ten as draft 3 has them.
- **One proposed WORDING entry (X11), not yet made.** At draft 4 L325 (file 11 L323, file 10 L338; Part VII, "Production and direction") the text says "intervening on \(H\) changes the target's \(L\) but not the calculation's \(H\)". Part V at L271 says of the same reversed calculation that it "changes the target's downstream value but not the calculation's", which is \(L\); under the reversed calculation an intervention on \(H\) sets the calculation's \(H\) too. Proposed: OLD "The reversed calculation \(H=L\tan\theta\) is not: intervening on \(H\) changes the target's \(L\) but not the calculation's \(H\)." (once in file 11 and once in draft 4), NEW the same with the last \(H\) replaced by \(L\); KIND WORDING, REASON WORD erratum, no declaration. It is put to the readers here and is not applied to the change list or the theory text (log S92 recorded the slip).

| id | entry | place in draft 4 | kind | part | what an earlier outside reading saw |
|---|---|---|---|---|---|
| X01 | W37.1 | Part 0, L13 | ORDER | F | S90 R01, with "blind" |
| X02 | W36.1 | Part I, L69 | CLAIM | D | S90 R06, "how hard an account is to vary" |
| X03 | W19.1 | Part II, L119 | CLAIM | F | S90 R08, without the typing sentence |
| X04 | W35.1 | Part IV, L217–221 | CLAIM | G | S90 R12, "a transport" |
| X05 | W35.2 | Part IV, L223 | CLAIM | G | S90 R13, "every transport" |
| X06 | W20.1 | Part V, L231 | CLAIM | H | S90 R15, without "whether or not anyone has described their work" |
| X07 | W34.1 | Part VI, L313 | CLAIM | D | S90 R23, Pres kept and reach defined |
| X08 | W33.1 | Part VI, L313 | CLAIM | D | S90 R24, with the reach sentence and Pres |
| X09 | W59.1, "Rivals" | Part VI, L315 | CLAIM | A | nothing |
| X10 | W59.1, "Problems" | Part VI, L317 | CLAIM | B | nothing |
| X11 | proposed | Part VII, L325 | WORDING | I | nothing |
| X12 | W40.1 | Part VII, L339 | CLAIM | I | S90 R25, the shorter declaration |
| X13 | W24.1 | Part VIII, L353 | WORDING | J | S90 R26, "every generator" |
| X14 | W60.1 | Part VIII, L369 | CLAIM | C | nothing |
| X15 | W22.1 | Part IX, L377 | CLAIM | J | S90 R28, "the explanatory candidate … that the criticism offers" |
| X16 | W6.3 | Part XI, L455 | CLAIM | K | S90 R39, as WORDING |
| X17 | W7.5 | Part XIV, L526 | CLAIM | K | S90 R48, without "(EK) also on (P)" |
| X18 | W38.1 | the note of sources and departures, before Part 0 | META | E | nothing (S90 withheld the meta entries) |

The earlier wordings are taken byte for byte from the S90 part briefs that carried them, and the build checks that each differs from the present form where the item says so.

## What is sent

- **Eleven part briefs**, in `tests/`, built by `tools/s93_build.py` (md5 fc46268b2049f38e28ef8c684e692317). The tool refuses on any source md5 mismatch, checks that every excerpt line equals its draft-4 line, and with `--check` rebuilds in memory and compares; run at commit time, it reported "12 files, 0 differ".
- **Each part goes to both Atria and Mimo**, whole, as the one user message with no system text: 22 calls. The job list is `tools/s93_jobs - draft 4 in eleven parts.json` (sha256 10ba67a36ad125f45f856a001fe2ac5291399c1a21ad2b8978c73652a6887b7c), run by `tools/s87_run.py`. Every job: effort medium (the map's "audit" for both providers, decision S17), ladder 65,536 and 65,536 for Atria and 131,072 and 131,072 for Mimo (each provider's ceiling), 6 attempts, `max_rejects` 3, `max_pass` 3. Tags are `s93_xexam_<atria|mimo>_<part>`, so every file name is unique per model and part (lesson S25). The returns go to `results/S93 Cross-examination - draft 4 - returns/`.
- **The dry run** (`s87_run.py … --dry-run`, before the commit): 22 jobs, 11 to each provider, every one pass 1 of at most 3, reasoning_effort medium, the ladders above, temperature 0.7, system none, no file already in the way, at most 3 in flight per provider across every process.
- **Sizes.** Atria failed on a brief of 25,790 words and came back on briefs of 18,000 words or fewer (lesson S20); the owner's cap here is 15,000 for Atria. Mimo ran away on large tasks, so each part holds one entry or one small group, and the same parts go to Atria. Cases were added while a part stayed within 14,000 words by both counts.

| part | file in `tests/` | items | words (runner / `wc -w`) | md5 | cases given / offered |
|---|---|---|---|---|---|
| A | `S93 Cross-examination - draft 4 - part A, rivals.md` | X09 | 13,658 / 13,658 | 852342f348dac7baa52b87b2deab333f | 11 / 11: N1, N2, N3, N25, O24, O36, D3-T, N7, O48, O46, N5 |
| B | `S93 Cross-examination - draft 4 - part B, problems.md` | X10 | 13,853 / 13,853 | 712ae2d47e35ad96083ef208d808f8f3 | 10 / 10: N2, N3, N5, O24, N4, O1, D3-T, O27, N1, O48 |
| C | `S93 Cross-examination - draft 4 - part C, a failed answer stays failed.md` | X14 | 12,913 / 12,913 | 902c9ea16de250837e05a607aaf6179d | 7 / 7: O1, D3-T, O27, O8, N7, N2, O24 |
| D | `S93 Cross-examination - draft 4 - part D, commitments that do no work, and Part I's companion edit.md` | X02, X07, X08 | 13,749 / 13,749 | 3acf25ca82b9873888287528b4ca3c15 | 10 / 10: N1, O36, N25, N3, O45, N7, O2, N4, N2, O47 |
| E | `S93 Cross-examination - draft 4 - part E, the note of sources and departures.md` | X18 | 13,746 / 13,746 | d91a2a693b5e69e3a43b44e9a245f5cb | 6 / 6: N2, N3, N4, N1, N22, N5 |
| F | `S93 Cross-examination - draft 4 - part F, selection in Part 0, and kinds across two candidates.md` | X01, X03 | 13,074 / 13,074 | 9331bd89299b5dc76f29144a26cbf431 | 7 / 7: O11, O10, O22, O9, N25, N9, N11 |
| G | `S93 Cross-examination - draft 4 - part G, expectation, violation and surprise.md` | X04, X05 | 12,964 / 12,964 | 116b65985d098eb606855954fa34bc71 | 8 / 8: N18, O23, O24, O11, O48, O3, O13, O5 |
| H | `S93 Cross-examination - draft 4 - part H, the commitments of a candidate.md` | X06 | 12,078 / 12,078 | 4be1172e57216bd67a9a9dce66ba2040 | 8 / 8: O45, O46, O36, N1, O47, O2, O5, O7 |
| I | `S93 Cross-examination - draft 4 - part I, Part VII, the pole sentence and the absent structure.md` | X11, X12 | 12,581 / 12,581 | 2be35c1ec040d791e348acacaae6a79c | 6 / 6: O6, O4, N22, O34, N8, N25 |
| J | `S93 Cross-examination - draft 4 - part J, functional transport, and the terms of (K1).md` | X13, X15 | 12,628 / 12,628 | 48c0e74429d7be0b3de79b1382199e37 | 5 / 5: O27, N20, N11, O40, O50 |
| K | `S93 Cross-examination - draft 4 - part K, the normative relation, and the dependence order.md` | X16, X17 | 13,124 / 13,124 | 0c3bb649152a55104195e908f38ec498 | 4 / 4: O35, O38, O37, O49 |

## What each part carries, and what it withholds

- **Section 1**: what the reader is asked to do; the kinds CLAIM, WORDING, ORDER and META; the stance ("attack that, as hard as you can"; each item UPHELD or CHALLENGED, with the reason and, if challenged, the exact wording proposed).
- **Section 2, verbatim**: the owner's words of decision S20; the drafters' reading of them (S20's bracket); lesson S26's sentence on what the owner corrected; and lesson S26's rule.
- **Section 3**: excerpts of the draft-4 theory text (md5 fc55b470c63cd4b3c27d6aa64d8d8c17), each line prefixed with its line number, omitted runs named by their headings. Every part carries Part 0's first three sections, Parts I–VI, VIII and IX, and Derivations 1–3, 8 and 9, and the Parts its items need besides (the build's `PARTS` table); part E carries a list of its own, chosen for the Parts the note names.
- **Section 4**: the items, in the S90 form (id; place; kind and reason word; declaration, "none" for WORDING and ORDER; old and new wording, byte for byte from the change list), with what an earlier outside reading saw where the item has changed since, and the cases the entry's CASES AT RISK names, as ids only. For X09 and X10 the new wording is pointed to in section 3 and not printed twice.
- **Section 5**: four standard tests for every item (T1 true, T2 kind and declaration, T3 coherence, T4 verdicts), and the orchestrator's questions for the items they concern: (a) faithfulness to S20 and S26 (A, B, C, D, E; J for X15); (b) whether a failed answer stays failed and how a corrected mistake could creep back (C); (c1) the symmetry on the Greeks' question (B, E); (c2) whether a failure found by examining a candidate counts as established (A, B, C); (d) the conflict condition for rivals, idle parts and redescriptions (A; D for X08; F for X03; H for X06). The parts with no assigned question ask for (a) wherever an item bears on rivals, variation, criticism or correction.
- **Section 6**: the report form. Points numbered, most serious first; for each challenge the exact wording; for each assigned question a paragraph ending in a verdict line (`(a) Xnn: FAITHFUL` / `NOT FAITHFUL — …`; `(b) Xnn: HOLDS AS STATED` / `HOLDS WITH CONDITIONS — …` / `FAILS — …`; `(c1) Xnn: DEFECT` / `HARMLESS` / `SAY DIFFERENTLY`; `(c2) Xnn: ESTABLISHED` / `NOT ESTABLISHED` / `UNSETTLED BY THE TEXT`; `(d) Xnn: RIGHT` / `WRONG` / `RIGHT, WITH A LOSS — …`); one line per item, `Xnn: UPHELD` or `Xnn: CHALLENGED — …`; `OVERALL: SOUND` or `OVERALL: NEEDS REPAIR`; about 3,000 words at most; last line END OF REPORT.
- **Section 7**: the described situations. O-cases are the S81 book's entries byte for byte (md5 4f488d149e44669240d5db546c8e946a), taken from the S90 part briefs, and O34 and O38 from the book itself; N-cases are as the S90 parts gave them from the S89 candidate book, with the same […] cuts; D3-T is its final text (md5 6b211dea40d735abf50426e56344f161), situation, question, and verdict with its reason.
- **Withheld, as in S90**: every W-number; REASON, CHECK, GAIN and LOSS; the drafters' expected direction on each case; the draft-4 pass record, its models and attacks; the two analyses of 24 September; the S90 readings and rulings and their reasons.
- **Words.** The build checks every part's frame (everything outside the excerpts, the fenced wordings and the case texts) for "Revision 2", "revision record", "file 13", W-numbers, "R2-", model names, record labels and "round", and finds none; the only model name in any part is the theory's own title inside the excerpt. Outside part E no part names either book's author. **Part E is the exception**: its item is the note of sources and departures, which names the two books and their authors and cites pages; it quotes no book passage, and the brief asks the reader to quote no more than a few words of either book, never more than twenty-five in all. No brief names where any book file came from.
- **Case numbers.** W34.1's and W59.1's CASES AT RISK write "N7 (O59)"; under D8 N7 is O58 and O59 is N8. The build reads that O-number as N7's, which is what those entries mean; the slip itself is left for the orchestrator.

## How the replies will be read

This rule was written and committed before any call was sent.

1. **Nothing is opened before the run is over.** No reply, receipt, reasoning file or attempt file is opened until every one of the 22 calls has ended its last allowed pass (accepted, or failed with no pass left), or until 21:00 UTC on 26 September 2026, whichever comes first. If the time limit passes first, the replies then accepted are read under these rules, the calls still going are left to finish, and a reply accepted later is read under these same rules and recorded as late. The progress log (the runner's `start`, `ok` and `failed` lines, and its closing `done:` line) may be watched; it holds no reply text.
2. **A reply is evidence, not a result.** No item is kept, fixed or dropped on a model's say-so, and no verdict line settles anything by itself. Silence is not support: an item a reply does not attack is not thereby confirmed.
3. **What counts as a challenge.** A reply challenges an item when its closing line for the item says CHALLENGED; or when any of its points shows, on that item, a false statement, a wrong kind or declaration, an incoherence, a verdict moved away from the fixed verdict, or wording that brings back a list, a count of versions, a grade or a record (question (a)), whatever its closing line says; or when it proposes exact new wording for the item. A verdict line on a question that reads NOT FAITHFUL, FAILS, DEFECT, SAY DIFFERENTLY or WRONG is a challenge to the item it names.
4. **Every challenged item goes to one fresh Claude checker**, who did not draft, assemble or check the change list, did not write these briefs, and has read no S93 reply other than those it is given. One checker per item: it receives every point that either reply makes on the item (and any point raised on it in another part, marked as such), the item's entry from the change list, the draft-4 text and the part brief. It works in this order: first, it states the entry (OLD, NEW, KIND, DECLARATION and its CHECK field); then each reply's argument, separately; then it rules **KEEP** (the challenge is not upheld), **FIX** (the challenge is upheld: the exact new OLD, NEW, KIND or DECLARATION, with the reason) or **DROP** (the challenge is upheld and the entry leaves the list; for X11, the proposal is not entered). **A challenge counts as upheld only when that checker rules FIX or DROP.**
5. **Disagreements between the two models go to that checker, and are ruled, not counted.** A disagreement is: one reply UPHELD and the other CHALLENGED on the same item; two challenges with different proposed wordings or incompatible reasons; or different verdict words from the two replies on the same question and item. The checker states each side's argument and rules between them or writes a third wording; the number of replies on a side decides nothing. An item that neither reply challenges and on which their verdict words agree goes to no checker, and is recorded as "upheld by both readers; not thereby confirmed". An item one model upheld and the other could not examine (rule 8) is recorded the same way, with that model named.
6. **The questions.** Each verdict word on (a), (b), (c1), (c2) and (d) is recorded by model and item. A finding that asks for a change of the theory text goes to the item's checker as a challenge (rule 4). A finding that is a choice for the owner and not a defect of the wording (for example, whether "easy to vary" should point at one side, question (c1), or whether the text should settle (c2)) is recorded with both replies' reasons for the owner's word, and the checker says only whether the present wording states the matter truly.
7. **File names** (lesson S25). Each checker writes `results/S93 reading rulings/ruling S93 <item id> <entry>.md` (X11 as "proposed"), and never writes over a file that exists. The reading that records all rulings is `results/S93 Reading of the replies.md`.
8. **A failed call supports nothing, and failed calls are sent again up to pass 3.** A reply is accepted only when it finishes "stop" with END OF REPORT on its last line (`s80_call.accept_reader`). A call that failed counts neither for nor against any item; its attempt files are kept and are not read for arguments. The job list allows three passes (`max_pass` 3), and this rule is the note written before sending for all three: when a pass ends, every call without an accepted reply is sent again as the next pass, with a byte-identical request, until pass 3. A call that failed only on the connection (every attempt ended with no HTTP status, a cut stream or a proxy refusal) is not an answer from the model and is not counted against it (lessons S21 and S24); if such a call is still failed after pass 3, it may be sent again only under a new note written before sending. A call that is still failed after pass 3 on answers the model did give (length at the ceiling, or no END OF REPORT) is final: its items are reported as **not examined by that model**. After any container restart, the runner is checked and relaunched from a shell started after the restart, and a proxy failure is not a reply (lesson S24).
9. **Quotations are checked.** Each quotation a reply relies on is checked against the draft-4 text or the brief; where one is not found, that is recorded and the point is ruled on what the texts say. A reply's quotation of a book longer than twenty-five words is not copied into any ruling or reading.
10. **Fixed verdicts are not in question.** A point that disputes a fixed verdict is noted and not ruled.
11. **A point on an item outside the reply's part** goes to that item's checker, marked as raised outside its part; it does not count that item as examined by that model.
12. **Edits come after all rulings.** No ruling is applied until every checker has ruled. Each FIX is then made in its entry, marked as after the S93 cross-examination, with a line beginning "S93 cross-examination:" in its CHECK field; a KEEP is recorded there too. X11, if not dropped, is entered as a new WORDING entry. The draft is rebuilt by `tools/s89_apply_changes.py --self-test`, and nothing is written into `authority/`.

## How the run is launched

From the repository root, after this commit is pushed, with the keys loaded into the runner's environment from the session's key file and never printed:

```
setsid nohup bash -c 'set -a; . <scratchpad>/cross_examiner_keys.env; set +a; for pass in 1 2 3; do <scratchpad>/venv/bin/python Semantics/tools/s87_run.py "Semantics/tools/s93_jobs - draft 4 in eleven parts.json" || break; done' > <scratchpad>/s93_run.log 2>&1 &
```

Each turn of the loop is one pass: a job whose reply is accepted is skipped, a failed job goes as the next pass (its earlier files kept under their pass numbers), and the runner refuses a pass above `max_pass`. The loop runs pass 2 only after every call of pass 1 has ended. The run is over when the log's last `done:` line is followed by no further `start` line and the process has exited, or when every tag has a `.response.txt` in the returns folder, or a `.error.txt` and a receipt with `"failed": true` from its third pass.

Decided by Claude under decisions S17 and S18. 25 September 2026.
