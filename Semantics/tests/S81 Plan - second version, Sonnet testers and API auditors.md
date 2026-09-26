# S81 Plan - second version, Sonnet testers and API auditors

*Written by Claude (an Opus 5.5 subagent doing the analysis and building for the orchestrator) on 23 September 2026, before any call of this round, under decision S15. It replaces the first version (`S81 Plan - file 11 against every case, rebuilt with the S78 repairs, for two API models.md`), which is kept as it was: no call had been sent under it, so this is a new numbered file and not an edit. Frozen once the first agent or call of this version is started; a change after that is a third version. Nothing in this plan travels in any call or to any agent: the prediction, the baseline, the sampling rule and the standing rule live here and in `tools/s81_build.py` only.*

## What changed, and why

Decision S15 sets the roles: "start with Opus 5.5 subagents. Use the others for cross examination.", "And use sonnet for running tests on." Read by Claude as: Sonnet subagents run the tests, Atria and Mimo cross-examine, Opus 5.5 subagents analyse and build, and Claude (the orchestrator) remains the authority that determines the result (decision S13). The first version gave both Stage 1 and Stage 2 to Atria and Mimo. This version moves Stage 1 to Sonnet and keeps everything else, changing as little of the frozen design as it can.

| | First version | This version | Why |
| --- | --- | --- | --- |
| Stage 1 (1C, 1K, 1D) | Atria and Mimo, one API call each per brief | Two independent Sonnet subagent testers, A and B; each call a separate fresh agent (six agents) | Decision S15: Sonnet runs the tests |
| How a Stage 1 call reaches its reader | `s80_call.py`, one prompt in, one answer out | A fresh folder outside the repository holding only `brief.md`, the exact user text the API call would have sent; the agent writes `return.md` | A subagent reads files; the folder is its whole world, and the text it reads is byte for byte the first version's |
| Contamination check | Not needed (no files, no tools) | Return scanned for void strings; tool-call extract scanned for paths outside the folder; a void run is rerun once | A subagent has tools and a working directory inside the repository, which holds the plan and the answer |
| Stage 2 (2a, 2b, 2D, 2W) | Atria and Mimo, each auditing the other | Atria and Mimo; 2a as before; 2b fully crossed (each auditor audits both testers' 1C); 2D one per auditor, Atria's list under audit A's, Mimo's B's | Below, "Who does which stage" |
| Calls | 12 API calls (+ 2W) | 6 Sonnet agents (+ reruns) and 8 API calls (+ 2W) | 2b is crossed: two calls more |
| Briefs | Frozen | Unchanged word for word | The briefs name no reader, and each still reads true: 2b's reading under audit is "another reader's", 2D's second list is "made by a reader working alone" |

The notes for the orchestrator in the two instruction files (outside their BEGIN and END markers) name Atria and Mimo for Stage 1 and the pairing "Atria audits Mimo"; where they differ from this plan, this plan governs. The instruction files are not edited.

## What this round is

Round S76 as planned (log S76): file 11, the candidate revision, tested against every case, testing then audit (decision S7), with Claude reading both and determining the result (decision S13: "you are the authority, not Mimo or Atria. You make the big decisions"). It carries the S78 repairs of group A (`results/S78 Results - the two-stage pattern reviewed by five readers, ...md`), which the five readers said must be made before S76 runs. The S76 packs as sent at log S76 are superseded unsent and kept. Stage 1 is run by Sonnet subagents (decision S15); Stage 2 by the two outside API models of decision S12, Atria (`Atria-Dawn-Preview`) and Mimo (`mimo-v2.6-pro`), each reached by one prompt in and one answer out, with no files and no tools, through `tools/s80_call.py`.

The owner's word on group A is not in Decisions as words of its own; the rebuild is made on the orchestrator's instruction under decision S13. **Confirmed by Claude, 23 September 2026, under decision S13** (first version, carried unchanged): group A is applied as mapped below; group C stays out; the three calls added beyond the brief (1K, 1D, 2a on all 52) are kept; D3-T stays out of the case book until Claude fixes its verdict; file 11's revision note is withheld from every call as a presentation choice (the frozen file is unchanged). The number S81 is kept although LEGEND's rule would give S88 (the shared sequence stands at L86): S80 was named the same way before the rule was checked, and renaming a round mid-run costs more than the gap; log S80 records the deviation.

## The texts

Unchanged. `s81_build.py build` makes the same texts as the first version (the same sha256 for each call text: 1C 7ff4bb69e4d3, 1K d27b26b004d6, 1D f03e993111bf, 2a a2cef715fcb8), once per tester for Stage 1.

| Text | File | As sent |
| --- | --- | --- |
| File 11, the candidate | `authority/11 Claude Fable Semantics - standalone theory, revision 1.md` (md5 5e494c1095d920d128b9a79de378f923) | Whole, except line 5, the revision note, and the blank line after it. The note names O48 and S75 and states the claim count, which is the answer; the frozen file is untouched and the build checks its md5 before cutting. 9,487 words as sent. |
| File 10, the authority | `authority/10 Claude Fable Semantics - standalone theory.md` (md5 3a8cd7c8ca6f3ad3b8a85ab9984d850e) | Whole. 7,937 words. |
| The case book | `tests/S81 Case book - the 52 cases, situations and fixed verdicts, as the tested agent sees them.md` (md5 4f488d149e44669240d5db546c8e946a) | Whole for 1C, 1K and 2b (4,344 words); for 2a, the verdict lines cut and the opening paragraph replaced by one that mentions no verdict (2,840 words). Provenance, kept out of every call: `tests/S81 Case book - provenance.md`. |
| The briefs | `tests/S81 Stage 1 testing - file 11 against every case.md` (briefs 1-cases, 1-texts); `tests/S81 Stage 2 audit - check the Stage 1 return.md` (briefs 2a, 2b, 2D) | Lifted between their markers, word for word. |

## What is run

**Stage 1: six Sonnet agents.** Each is a fresh subagent started by the orchestrator on the Sonnet model, with one prompt, working in its own folder. Thinking and temperature are the harness's and cannot be set; the model as served is read from each agent's transcript and recorded.

| Agent | Tester | Call | Its folder's `brief.md` | Words | Return named |
| --- | --- | --- | --- | --- | --- |
| A1 | A | 1C, the test | brief 1-cases + file 11 (note withheld) + the case book | 14,803 | `s81_1C_A` |
| A2 | A | 1K, the control | brief 1-cases + file 10 + the case book | 13,253 | `s81_1K_A` |
| A3 | A | 1D, the differences | brief 1-texts + file 10 as Text A + file 11 (note withheld) as Text B | 18,024 | `s81_1D_A` |
| B1 | B | 1C | as A1 | 14,803 | `s81_1C_B` |
| B2 | B | 1K | as A2 | 13,253 | `s81_1K_B` |
| B3 | B | 1D | as A3 | 18,024 | `s81_1D_B` |

The 1C and 1K arms are separate agents, so neither knows the other arm exists, as in the first version. "Tester A" and "tester B" are bookkeeping: the three agents of a tester share nothing but a letter, and each of the six is as independent of its two siblings as of the other three. What makes A and B two testers is that each has its own 1C, 1K and 1D, so each tester's 1K and 1C can be compared within the tester, as each model's were.

**Stage 2: eight API calls,** each a fresh single-turn call, thinking on (`reasoning_effort: high`), temperature pinned at 0.7 by `s80_common`, max_tokens on the reader ladder (48,000, then 64,000), accepted only when the reply ends with `END OF REPORT`, at most three in flight per provider.

| Call | What the model sees | Words | Tag |
| --- | --- | --- | --- |
| 2a, the blind reading | brief 2a + file 11 (note withheld) + the 52 situations, verdicts withheld | 12,740 | `s81_2a_atria`, `s81_2a_mimo` |
| 2b, the open audit | brief 2b with its rows + file 11 + the case book + one tester's 1C return + the auditor's own 2a return | about 15,000 + the two returns (about 30,000 to 35,000 in all) | `s81_2b_atria_A`, `s81_2b_atria_B`, `s81_2b_mimo_A`, `s81_2b_mimo_B` (`s81_2b_<auditor>_<tester audited>`) |
| 2D, the difference audit | brief 2D + file 10 + file 11 + one tester's 1D list (under audit) + the other tester's 1D list (the second list) | about 17,500 + the two lists (about 25,000 to 30,000) | `s81_2D_atria` (under audit: A's list; second: B's), `s81_2D_mimo` (under audit: B's; second: A's) |
| 2W, widening, only if the stopping rule fires | as 2b, with the widened rows | as 2b | `s81_2W_<auditor>_<tester>` |

Every call and every brief is under the ~60,000-word ceiling, so nothing splits its cases into batches; each 1C, 1K and 2a text carries all 52 cases and its theory whole.

**Why the control arm (1K).** SAME and CHANGED compare file 11 with file 10. S76 took file 10's side from S72's table, thirty-three of whose rows no auditor opened (S78 item 9), written under a different instrument. 1K runs the identical brief on file 10, by the same tester, on the same cases, so each tester's two arms differ in the theory alone; neither arm can tell which it is in. This is S78 repair A1's "worked from file 10" for all 52 rows, in a form the tested agent cannot read as a hint that two versions exist.

**Why the difference call (1D) is in Stage 1.** S76 Stage 1 Part 2 tested file 11's note that one claim changes; S78 (item 6 and its correction to S75 point 2) says that count is under test and names one sentence against it. The cases cannot test it alone, since a claim change that no case touches changes no verdict.

## Stage 1 by Sonnet: the folders, the prompt, and the contamination rule

**The folders.** `tools/s81_sonnet_prep.py` (after `s81_build.py build`) makes one folder per agent, outside the repository, at `<scratchpad>/s81runs/<agent>/`, holding only `brief.md`. The prep rebuilds each call text from the frozen sources (md5-checked) and refuses to go on unless it equals, byte for byte, the text in `briefs/`. The prompts go to `s81runs/_prompts/<agent>.txt`, and the map from agent to folder, call and hashes to `s81runs/_prompts/MAP.json`; neither is inside any agent's folder. The agent names are a letter and a number (A1 to B3) so that the path the agent sees names no arm, version, case or expectation; the parent folder's name, `s81runs`, carries the round number in lower case, which is the orchestrator's layout and names nothing else.

**The prompt,** the same for all six but for the folder's path, and checked by the prep to carry no round or case identifier and none of the words prediction, control, arm, version, revision, tester, Sonnet or round:

> Your working folder is {F}. It holds one file, {F}/brief.md: a task, followed by the texts the task works on.
>
> Read {F}/brief.md from its first line to its last, and carry out its task exactly as it says. The file is long: read it with the Read tool in parts, about 300 lines at a time, using offset and limit, until you have read every line.
>
> Work from brief.md alone. Use absolute paths inside {F} only, and open no other file or folder. The Read, Write and Edit tools are all the task needs.
>
> Write your whole answer, in exactly the form brief.md asks for, to {F}/return.md. A long answer may be written in parts: the first part with the Write tool, and each later part added at the end of return.md. The last line of return.md is the brief's closing line, on its own:
> END OF REPORT
>
> When return.md is complete, reply with the single word DONE.

The brief reads "Below this instruction are ..." and names its sections by heading; in a file those words still point where they did in a prompt.

**Collecting.** `tools/s81_sonnet_collect.py --transcripts DIR`, with DIR holding each agent's transcript as `<agent>.jsonl` (the orchestrator supplies them). For each agent's latest attempt:

- **Void, from the return:** it contains "S81", "S76", "S75" or "R2 J" (as written), or "prediction" or "O48 change" (in any case). A double-quoted span of the return that stands word for word in that agent's own `brief.md` is left out of the scan. The reason: the texts the testers are given carry the word "prediction" themselves (four times in each theory file, twice in the case book; file 11's simulation layer is one "whose queries are predictions", and a fixed verdict reads "a reliable prediction"), and a sentence copied from the given text is no sign of contamination. A remaining hit whose only word is "prediction", in a run whose transcript is clean and whose return is complete, may be read by Claude and cleared with a recorded reason (`--clear <agent> "<reason>"`), since a tester paraphrasing a verdict that uses the word is to be expected; nothing else is clearable.
- **Void, from the transcript:** its tool-call extract, made with `tools/s80_transcript_extract.py` and kept as `stage1/<agent>.tools.txt`, touches any path outside the agent's folder. Read, Write and Edit must name a file inside the folder; Glob and Grep must name a path inside it (a missing path is the working directory, which is the repository); a Bash command must name the folder, every absolute path in it must lie inside the folder, and `~` or `..` as a path voids (the body of a heredoc is text being written and is not scanned); TodoWrite and ToolSearch pass; any other tool voids.
- **Void:** `brief.md` changed. **Incomplete:** the last non-blank line of `return.md` lacks `END OF REPORT`, or a 1C or 1K return lacks a record with a MARK line for any of O1 to O52, or a 1D return lacks its Counts section. The form check is new with the file route: a second Write that overwrites the first part would leave the closing line and lose records, which a single API reply cannot do.
- **Rerun once.** A void or incomplete attempt is kept (`returns/<s81 tag>.pass<k>.void.txt` or `.truncated.txt`, with a receipt) and rerun once in a fresh folder (`s81_sonnet_prep.py --attempt 2 <agent>`, folder `<agent>-2`). A second failure is recorded as failed twice, and Claude decides whether that tester's call is missing from the round.
- **Collected:** a clean, complete return is copied to `returns/<s81 tag>.response.txt`, the name every later step of `s81_build.py` reads; the prompt to `.request.md`; a receipt to `.receipt.json` (folder, prompt and brief hashes, response hash, the hits, the transcript path, the model as served, and whether it is a Sonnet model). Every run of the collector rewrites `stage1/contamination.md`, one row per attempt judged.

The orchestrator may run the six agents at once: none depends on another.

## Who does which stage, and why

Sonnet testers A and B each run all of Stage 1 independently (1C, 1K, 1D). Atria and Mimo each run the blind reading 2a. Then **each auditor audits both testers' 1C returns** (2b, fully crossed), and **each auditor audits one 1D list with the other tester's list beside it** (2D: Atria has A's under audit, Mimo B's).

- **Two independent testers.** Two readings of file 11 on every case, in two fresh runs, measure how much of a mark is the theory and how much the reading (S78 reader 4's first repair), before any audit. In this version the two readings are two runs of one model, not two families: they measure run-to-run variation within Sonnet, which the first version did not measure at all, and no longer measure variation between families at Stage 1 (below, "Not tested").
- **Cross-audit, never self-audit.** Every auditor is of a different family from every tester, so no model audits its own reasoning, whatever the pairing.
- **Why crossed, and not Atria on A with Mimo on B.** Testers A and B are the same model under the same prompt, so they are exchangeable: "Atria audits A, Mimo audits B" and its swap are the same design, and neither pairing buys independence the other lacks. The first version's argument for crossing was "role and model are crossed, so a lenient model and a lenient role can be told apart in the table". With one auditor per tester, an auditor's disagreement rate is confounded with the particular run it audits. With both auditors on both returns, on the same rows (the sample is drawn from the tested return alone, so both auditors of a return get the same rows), the table separates auditor from run: a row one auditor disputes and the other passes on the same return is a difference between auditors; a row both dispute on one return and neither on the other is a difference between runs. And since the two testers now share a family (and a maker with the author of the cases and the theory), two outside families reading each Sonnet return is the independence Stage 1 no longer has. The cost is two 2b calls.
- **Why 2D is not crossed.** Brief 2D audits every CLAIM record on either list and asks for the differences both lists missed; an auditor given A's list under audit and B's as second has already read both lists in full. Crossing would give each auditor the same two lists in swapped places. One 2D per auditor, the list under audit alternating, keeps the brief's two roles for the lists and costs nothing.
- **Blind first, by call.** In a single-call API a column cannot be withheld inside one prompt. 2a is written from the theory and the situations alone, before the auditor sees any fixed verdict or any Stage 1 reading; 2b opens both and starts each row from 2a. 2a covers all 52 cases: the cost is small, and a verdict-blind reading of every row is what puts the forty-odd agreeing rows under pressure (S78 reader 5), which a sample would cover thinly. In this version 2a is also the only reading of every row by a family other than the author's, which weighs more now.
- **Claude decides** (decision S13). The testers' and auditors' marks are evidence; Claude reads the theory's text on every row the rules below name, and rules.

## The frozen prediction

Carried from the first version word for word. Kept here and out of every brief; `s81_build.py` asserts that no brief carries "O48 change", "S75", "prediction", "R2", "S76" or any round number, file number, "Revision", "Derivation 3" or "amendment", and that no Stage 1 or 2a brief carries "O48" or "O24" at all.

The baseline is S75's determination on file 10 (from the S72 table as audited): **DISAGREE** on O48; **SILENT** on O1, O12, O20, O21, O27, O35, O40 and O50; **AGREE** on the other forty-three, O24 among them.

- **P1, the one change.** Under file 11, Claude's ruled mark on O48 is AGREE, and it rests on the qualified claim of Derivation 3 or on one of the three sentences restated with it (the answer to grievance 3, attack point (D), the Part XV entry). Under file 10 it is DISAGREE, resting on the unqualified claim. O48 is CHANGED toward the thoughtful person, in its verdict and in the passage it rests on.
- **P2, nothing else.** Every other case keeps its baseline mark under file 11 on Claude's ruling: forty-three AGREE, the same eight SILENT, and no DISAGREE, SPLIT or CASE DISPUTED that file 10 does not also give.
- **P3, the claim count.** Of the places where file 10 and file 11 differ, the ones Claude rules CLAIM after reading both 1D lists and both 2D audits are Derivation 3 and the three sentences restated with it. Every other place is WORDING or ORDER. Recorded before the run, against P3: S78 item 6 found one sentence file 10 does not carry, in Part XI's Repair paragraph, "each as a stated condition over stated occasions, and a protected condition is lost exactly when it fails on an occasion it covers" (file 11, the paragraph opening at line 427, the sentence at line 433; file 10's Repair paragraph, line 438, has no such clause); the "Declared inputs" paragraph of Part XIV (log S76) is a second candidate. P3 stands only if Claude rules both WORDING.
- **P4, the instrument (a claim about the readers, not the theory).** Within each model, the 1K and 1C marks differ on O48 and on no other case.

Two expectations, written first and not predictions of file 11: **E1**, at least one model marks the occasions clause CLAIM in 1D; **E2**, a model's 2a reading, marked in 2b, differs from its own 1C mark on more rows than its 1K and 1C marks differ from each other (seeing the fixed verdict moves a reading more than the change between the two files does). Both are reported with their counts.

**How the carried words are read in this version,** fixed before any return:
- In **P4** and **E1**, "model" reads "tester": P4 is scored within tester A and within tester B, E1 on the 1D lists of A and B. Both remain claims about the readers; P1 to P3 are about the theory and are untouched.
- **E2 cannot be scored as written**: no model now writes both a 2a and a 1C. It is not re-worded into a new expectation after the fact. Reported instead, and marked as not E2: each auditor's 2a reading, as marked by that auditor in its 2b BLIND MARK, against each tester's 1C mark, row by row, beside the count of rows where that tester's 1K and 1C differ. That comparison mixes seeing the verdict with a change of family, and is recorded as such.

## The words Claude rules with, fixed before the data

- **The file-11 mark** of a case: Claude's ruling, from file 11's text, informed by both 1C returns and all four 2b audits.
- **The file-10 mark**: S75's baseline, unless both 1K returns agree on a different mark and Claude's own reading of file 10 confirms it; then the baseline is corrected, and the correction to S75 is recorded in S81 Results with the row.
- **Verdict SAME or CHANGED**: whether the two ruled marks differ, and, where both are DISAGREE, SPLIT or SILENT, whether they concern the same point. The rule "a clarification is not a changed verdict" is the brief's "Same finding", fixed in advance.
- **Passage SAME or CHANGED**: whether the sentence of file 11 the verdict rests on claims something different from its counterpart in file 10. The program marks every quoted sentence found in file 11 and absent from file 10; Claude decides whether its claim differs, with the 1D and 2D returns beside it.
- **Direction**: toward the thoughtful person when the file-11 mark is nearer AGREE than the file-10 mark, away when it is further (AGREE, then SILENT or SPLIT, then DISAGREE).
- **A theory change** is a case CHANGED in its verdict where the change traces to a passage CHANGED. **Reader variation** is a difference of marks where both verdicts rest on sentences the two files share word for word; it is recorded as a finding about the readers, or about S75, and counts neither for nor against file 11.

## The 2b sample, fixed here and applied after the returns

The rows the auditors of tester X's 1C return audit in full, drawn by `s81_build.py build2` once both 1C and both 1K returns are in, and written only into the 2b briefs for X. The rule reads only the returns, so both auditors of X's return get the same rows.

- **M1**, every row X's 1C marks other than AGREE;
- **M2**, every row where X's 1C mark differs from the other tester's 1C mark, or from X's own 1K mark;
- **M3**, every row whose quotations include a sentence found in file 11 and absent from file 10 (the S81 form of S78 A3's "names a sentence of file 11 that differs from file 10");
- **M4**, every row with a quotation the program cannot find in file 11, or with none;
- **M5**, every row whose strongest contrary reading X itself says HOLDS;
- **M6**, every row the baseline marks other than AGREE (O1, O12, O20, O21, O27, O35, O40, O48, O50);
- **R**, from the rows left, the ten whose `sha256("S81-2b-residual|" + sha256(X's 1C return) + "|" + case)` sort first. The key is the return's own hash, so the draw is fixed by rule and unknowable before the return exists.

Every other row gets the one-line comparison of 2b Part 2. **Stopping rule:** if an auditor marks DISAGREE (ON VERDICT or ON MARK) on any R row of tester X's return, Claude builds `widen <auditor> <X> <rows>` with every row outside the sample whose 1C quotations cite the same Part of file 11 as that row, and runs 2W for that auditor and tester. The rule's draw is saved as `sample - tester <X>.json` beside the returns.

## How Claude determines the result

1. **Receipts.** Stage 1: every agent's return collected by `s81_sonnet_collect.py` (complete, clean on the return and on the transcript), its folder, prompt and brief hashes, the model as served, and `stage1/contamination.md`; a void or incomplete return is kept and run once more, recorded as a second attempt. Stage 2: every call accepted by `s80_call.py` (finish "stop", the last line `END OF REPORT`), its model as served, its request and response hashes; an empty or failed return is kept and run once more, recorded as a second attempt.
2. **By program** (`s81_build.py table`): each case's marks in 1K and 1C for each tester and in each of the four 2b audits (a 2W record in place of the 2b record where there is one); every 1C quotation marked VERBATIM, LOOSE (letters and digits match) or ABSENT against file 11; the count of quotations absent from file 10.
3. **By Claude, against the two files directly, row by row:** O48 in full; every row where any reading of file 11 (either 1C, any 2b) differs from the baseline; every row where either 1K differs from the baseline; every CASE DISPUTED; every row named under "Disagreements the reading under audit left unmarked" or "Wrong, and uncorrected anywhere in the theory"; every row with an ABSENT quotation; and, new in this version, every row where both testers' 1C marks are AGREE and either auditor's 2a-based BLIND MARK is not (the rows a shared blind spot of the testers would hide). For each: the file-11 mark, the file-10 mark, verdict and passage SAME or CHANGED, direction, theory change or reader variation.
4. **The differences:** every CLAIM place on either 1D list, and every place in either 2D's "Surviving differences in claim" or "Differences in claim that both lists missed", read against both files and ruled CLAIM or WORDING.
5. **The eight SILENT cases:** from their SEARCH records in both arms, whether file 11's Declared inputs paragraph (Part XIV) now names the input each case lacks, which S76 Stage 1 asked the tester and which is asked here of the determiner, because the question names the earlier finding.
6. **CASE DISPUTED rulings:** a case Claude rules wrongly fixed is set aside from every count, named, and corrected only in a new numbered case file.
7. **Written up** as `results/S81 Results - ...md`: P1 to P4 and E1 ticked, E2 reported as not scorable with the substitute comparison, the ruled table, every ruling on a disputed row, the standing verdict, and "Not tested"; and the log entry S81.

## What counts as file 11 standing as the authority

Unchanged. File 11 stands, on Claude's determination, when all four hold:

- **(a)** O48 is AGREE under file 11: the change it was written for is delivered, whatever the control arm shows.
- **(b)** No case shows a theory change away from the thoughtful person.
- **(c)** No sentence of file 11 is ruled to give a wrong verdict on a case where file 10's corresponding sentence gave the thoughtful person's.
- **(d)** No cross-reference in file 11 is ruled to point wrong in a way that changes what a sentence claims. A pointer that is only a slip is recorded as an erratum for a later revision.

With (a) to (d), and P2 and P3 holding, file 11 stands as written and its note is confirmed. With (a) to (d), and P2 or P3 failing only by a theory change toward the thoughtful person or by an undeclared CLAIM that no case shows harmful, file 11 stands with those findings recorded against its note; the note is frozen, so the correction lives in S81 Results, and in a revision 2 if the owner asks for one. Where (a), (b), (c) or (d) fails, file 10 remains the authority and S81 Results lists what a revision 2 would have to repair. If 1K shows O48 AGREE under file 10 (a fresh reader supplying the qualification the proof already assumes, as S75 said the proof does), P1's file-10 half fails under this instrument, rests on S72 and S75 as audited, and is reported so; it bears on P4 and leaves (a) untouched.

## The S78 repairs, and where each is applied

As in the first version, with the rows this version touches marked **(changed)**.

| Repair (S78) | Where, or why not |
| --- | --- |
| A1: strip the answer from the tested agent's brief; S75 and the S72 Stage 2 return out of the tester's pack; column 3 from file 10 | Applied. The prediction is in this plan only. No call or folder carries any earlier return, S75, R2, a file number or a round number in its text (asserted by the build; the prompt is checked by the prep). File 11's revision note, which carries the answer, is withheld from every call. Column 3 becomes the 1K control arm, file 10 read under the same brief on all 52 rows. The case book drops each case's header annotation, which for O24 and O48 quotes R2 J (provenance file). **(changed)** A Sonnet tester has tools and a working directory in the repository, where the plan lies: its folder holds only its brief, it is told to open nothing else, and its transcript is checked by program (above). |
| A2: two-pass audit, Stage 1's columns withheld; sample chosen after the return; every-fifth dropped | Applied, by call: 2a blind (every case, verdicts withheld too), then 2b open. The sample is drawn by the rule above after the returns, keyed to the return's hash; there is no fixed sequence to print. |
| A3: mandatory set widened; stopping rule | Applied: M1 to M6, and 2W, per auditor and tester. |
| A4: SAME and CHANGED as two columns fixed in the instruction; SILENT with a recorded search | Applied. The tester's marks and "Same finding" are defined in brief 1-cases before the data. SAME and CHANGED, verdict and passage, are the determiner's columns, fixed above and computed from the two arms; the tester is asked for neither, since it sees one version. SILENT carries SEARCH. |
| A5: "Changes Stage 1 did not mark"; "Wrong, with no amendment that fixes it"; CASE DISPUTED | Applied, in the S81 forms: "Disagreements the reading under audit left unmarked", "Wrong, and uncorrected anywhere in the theory" (2b), "Differences in claim that both lists missed" (2D), each counted at zero; CASE DISPUTED is a mark in 1C and 2b with its required field, and "Cases to rule on" carries it to Claude. |
| A6: quotation counts in two, source-checked and chained | Applied in form: every quotation in S81 is of a text inside its own call or folder, so all are source-checkable and none is chained; the program counts VERBATIM, LOOSE and ABSENT for every one. |
| A7: manifest line (model, date, fresh chat) | **(changed)** Stage 2: the `s80_call.py` receipt (model as served, time, request and response hashes; fresh and single-turn by construction). Stage 1: the collector's receipt (model as served from the transcript, folder, prompt, brief and response hashes); every agent is fresh by construction and has a fresh folder. |
| A7: negative-wording search at build time | Applied: `s81_build.py` prints every negative word in every brief; zero at freeze, apart from the values NONE and NO. The Sonnet prompt is positive except "open no other file or folder", the orchestrator's own condition. |
| A7: the read-me sentence made conditional | Not applicable: no pack, no read-me travels. The folder holds one file. |
| A7: D3-T entered as O53 with its verdict frozen | **Not applied.** D3-T's situation and verdict were written by the S72 auditor ("Written by: me" in its fix card), so its verdict is not yet fixed by the determiner; entering it needs Claude to fix the verdict first. It is the one case aimed at the qualified Derivation 3's weakest sentence, so it is the first case to add; held for the orchestrator. |
| A7: Part 4's fix card conditional on Part 1 | Not applicable: S81 commissions no fix card. A repair, if one is needed, is Claude's after the determination. |
| B: the seeded-error round | Run separately as S79 (log S79). S81's "nothing else changes" is read with S79's result on what the pattern can catch. |
| C: cases by an agent that has never read file 10 | Not applied; the owner's call. CASE DISPUTED is the only channel against a Claude-written verdict in this round. |
| Item 8: R2 copy-checked | R2 is absent from S81 altogether. |
| Item 9: S76 imports an unaudited baseline | The 1K arm reads file 10 afresh on all 52 rows, by both testers. |
| Item 10: R2 J's Part VIII qualification has no case | Not tested (below). |
| Reader 1, finding 5: expectation first, the best case against each agreeing row | Applied: EXPECT, AGAINST and HOLDS in every 1C record; HOLDS YES puts a row in the sample (M5). |
| Reader 4: Stage 1 twice, by two agents | Applied: two testers, each also in the control arm. **(changed)** The two are two runs of one model, not two families. |
| Reader 5: the fixed verdict withheld from the auditor on some rows | Applied on every row (2a). |
| Smaller items: the coverage file unaudited; the five zero gauges; `build.py`'s single cut | S81 prints no coverage file (Claude updates coverage in results only where a verdict changes); every heading states its count and the "Wrong, and uncorrected" heading names the Parts read; briefs are lifted between explicit markers, so the orchestrator's notes and the brief never share a cut. |

S76 parts not carried: its Part 1 column 3 (S72's verdicts quoted; A1), its Part 3 coverage reprint, its Part 4 quotations file (the quotations are checked in place by program), and its closing question on the eight SILENT cases, which named the earlier finding and moves to the determiner (step 5).

## Run order

1. `python Semantics/tools/s81_build.py build`: the six Stage 1 texts (1C, 1K, 1D for testers A and B) and the two 2a texts, word counts, hashes, the checks. The texts are frozen from here.
2. `python Semantics/tools/s81_sonnet_prep.py`: the six folders and prompts. The orchestrator starts six fresh Sonnet subagents, one per prompt in `s81runs/_prompts/`, and keeps each one's transcript as `<agent>.jsonl`. Beside it, `python Semantics/tools/s81_build.py run 2a` (it shares nothing with Stage 1).
3. `python Semantics/tools/s81_sonnet_collect.py --transcripts DIR`. For each void or incomplete agent, `s81_sonnet_prep.py --attempt 2 <agent>`, a fresh agent on the new prompt, and collect again. A "prediction"-only void is read by Claude first and cleared or rerun.
4. `python Semantics/tools/s81_build.py build2`: the two samples drawn and saved; the four 2b and two 2D texts built and checked. Then `run 2` (three calls in flight per provider).
5. If the stopping rule fires: `widen <auditor> <tester> <rows>`, then `run 2W`.
6. `table`; Claude's reading; S81 Results; log entry S81 and Status.

Outputs go to `results/S81 File 11 against every case - outputs/` (`briefs/` the exact texts, `returns/` every return with its receipt, `stage1/` the tool-call extracts and `contamination.md`, the sample files, `table.md`), kept as they came. The agents' folders stay in the scratchpad; the returns and receipts are the record.

## Not tested

Carried from the first version:
- Whether the fixed verdicts are right. They are Claude's (cases O15 to O52 by Claude with the verdict fixed first; O1 to O14 by Claude as "a different author"); CASE DISPUTED is the only channel, and group C is not applied.
- R2 J's Part VIII qualification (the accumulated-error bound with unmatched initial states): no case touches it.
- D3-T, the case aimed at the qualified Derivation 3's weakest sentence: not entered (above).
- The parts of file 11 no case reaches: the coverage of the recovered Stage B rows stands at 55 of 80 (log S74), and the first 32 rows are still unrecovered.
- Any reader armed with the audit workflow (file 24): the briefs are self-contained and carry none of it.
- Whether the pattern can catch a known error: that is S79's question, not this round's.
- File 12 (the causality version) and the richness question (FW5).

Changed or new with the testers:
- **Stage 1 by a model of the author's maker.** Sonnet is made by the maker of the model that wrote the theory, file 11's revision, the case book and the fixed verdicts, and of the model that determines the result. Shared training can mean shared readings: a Sonnet tester may supply the qualification the author meant, or read a sentence of file 11 the way it was written to be read, more readily than an outside reader would. That bears on how much a tester's agreement with a fixed verdict is worth as evidence (less than the same agreement from Atria or Mimo), on which rows reach the 2b sample through M1 and M2 (a blind spot the two testers share leaves a row AGREE in both returns and out of M1 and M2), and on P4 to the extent the shared reading is stronger for one file than the other (file 11 was written by the same maker's model in answer to O48). It does not bear on the texts sent (unchanged and checked by program), on the quotation checks, on M3 to M6 and the residual draw (fixed by rule), on 2a (written by the two outside families on every row, blind to the verdicts), on the 2b and 2D audits (outside families), or on the rows Claude reads, which include every row where either auditor's blind mark departs from both testers' AGREE (step 3). It adds nothing that was not already there in the determiner, who was always Claude.
- **Reader variation between families at Stage 1.** The first version's two testers were two families; these are two runs of one model. Between-family variation is now seen only at Stage 2, in 2a and the audits. Within-model repetition is now measured (two runs per arm), where the first version had one call per arm per model.
- **The Stage 1 settings.** Thinking and temperature are the harness's and are not set or known beyond what the transcript records; Stage 2 runs with thinking on (high) and temperature 0.7. The Sonnet version served is recorded from the transcript and not chosen by this plan.
- **What the harness shows a subagent beyond its prompt.** A subagent may be given context by the harness (for example, the repository's status and recent commit subjects, which name the round, though not the prediction, a case, or which text is which arm). The collector checks what the agent did and wrote, not what it was shown; a return that uses such context is caught only if it writes a void string.
- **E2**, as written: not scorable (above).
- **Whether a Sonnet tester in a file-and-tool setting reads as it would in one prompt.** Reading `brief.md` in parts may lose or repeat text at the seams; the form check catches a return that lost records, not a reading that skimmed.
