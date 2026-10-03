# S81 Plan - third version, the changes made after the second version was frozen

*Written by Claude subagents for the orchestrator on 23 September 2026, at 11:33 UTC. At that time the last allowed pass of the three pending 2b calls and the effort controls were still running. The second version (`S81 Plan - second version, Sonnet testers and API auditors.md`) says at line 3: "Frozen once the first agent or call of this version is started; a change after that is a third version." Changes were made after its first agent started, and no third version was written. This file is that third version. It does not restate the plan: the second version governs wherever this file is silent. For each change it gives (i) what the second version said, quoted with its line; (ii) what is done instead; (iii) when, and on whose authority; (iv) whether the change was made before or after the data it could bear on, with that data named.*

## The changes at a glance

| | Change | Authority | Before or after the data it could bear on |
| --- | --- | --- | --- |
| a | Stage 1 run by Claude subagents | Decision S16 | After the first six Stage 1 returns |
| b | Output limits: Mimo 131,072, Atria 65,536 | Claude (lessons S7, S11; log S83) | After Mimo's failed 2a pass 1 and Atria's 2b attempt that ran out at 48,000 |
| c | Medium effort for the three pending 2b calls | Decision S17; Claude's ruling that the accepted returns stand | After the five accepted Stage 2 returns at high |
| d | A pass cut off by the session's end does not use the one further run | Claude's ruling | After pass 1 of the three pending calls; before any pass-2 return |
| e | Effort controls, outside the table | Claude, under decision S18 | After the accepted high-effort returns they repeat |
| f | Claude rules every case and difference from the texts before opening any return | Claude, for lesson S2 | After the Stage 1 and Stage 2 data existed; before Claude opened any of it |
| g | Atria and Mimo cross-examine the determination | Decisions S15, S17 | Before the determination is finished |
| h | The table shows each 2b column's effort, the confound, and MISSING | Claude | After the effort switch; before the table is built |
| i | 2W cannot be built | Claude's reading of the rule | After the samples were drawn; before Claude read any 2b audit |
| j | The determination's log entry is S87 | LEGEND; lesson S5 | Bears on no data |
| k | The Stage 1 receipts' reader label is corrected in S81 Results | Claude | After the Stage 1 returns were collected; bears on no mark |
| l | The hand-back tool passes the transcript check | Claude's ruling | After the first Stage 1 transcripts |

## a. Stage 1 by Claude subagents

- **(i) The second version.** Line 39: "**Stage 1: six Sonnet agents.** Each is a fresh subagent started by the orchestrator on the Sonnet model, with one prompt, working in its own folder." Line 11 gives the same.
- **(ii) Instead.** Stage 1 was run again by six fresh Claude subagents of the model named in decision S16. Each had a fresh folder, the same briefs and the same prompt, and was collected by the same collector. The six earlier returns are kept as a comparison in `returns/Sonnet testers - set aside by decision S16/`. The Stage 2 audits of them were stopped and are kept in `returns/Stage 2 on the Sonnet testers - stopped by decision S16/`. The 2b and 2D texts were rebuilt on the new returns, and the blind readings (2a) stand. The concern of the second version's line 220, that the testers share a maker with the author of the theory, the cases and the verdicts, now applies with more force: the testers, the author and the determiner are all Claude.
- **(iii) When and on whose authority.** The owner's instruction of 23 September 2026, decision S16. Log S83 (a).
- **(iv) Before or after the data.** After. The first six Stage 1 returns had been collected (commit 1f37750, 06:34 UTC), and Stage 2 audits of them were running. The rerun's returns did not yet exist.

## b. The output limits

- **(i) The second version.** Line 52: "max_tokens on the reader ladder (48,000, then 64,000)".
- **(ii) Instead.** Each provider starts at its ceiling and stays there: Mimo 131,072 tokens on every attempt, Atria 65,536. Both ceilings were found by probe on 23 September: Mimo refuses 200,000, and Atria refuses more than 65,536. The limits are set in `tools/s81_build.py`. `s81_2a_atria` had already been accepted at the plan's 48,000, as its `request.json` records.
- **(iii) When and on whose authority.** Claude, on 23 September 2026, under lessons S7 and S11. Log S83 (b).
- **(iv) Before or after the data.** After the failures that prompted it. Mimo's 2a pass 1 at 64,000 gave three attempts with no content (`s81_2a_mimo.pass1.*`; lesson S11). Atria's first 2b call ran out at 48,000 (the comment in `s81_build.py`). The change came before the returns accepted under the new limits: `s81_2a_mimo` (pass 2), `s81_2D_atria`, `s81_2D_mimo` and `s81_2b_atria_A`.

## c. Medium effort for the three pending 2b calls

- **(i) The second version.** Line 52: "thinking on (`reasoning_effort: high`)". Line 222: "Stage 2 runs with thinking on (high) and temperature 0.7."
- **(ii) Instead.** The three calls still pending, `s81_2b_atria_B`, `s81_2b_mimo_A` and `s81_2b_mimo_B`, go at `"medium"` on pass 2. Pass 1 of each went at high, as its `pass1.request.json` records. Everything else is unchanged: the texts byte for byte, the limits, temperature 0.7, thinking on (`returns/READ ME - the three pending 2b calls, pass 1 at high effort, pass 2 at medium.md`). The five accepted returns at high stand and are not sent again: `s81_2a_atria`, `s81_2a_mimo`, `s81_2D_atria`, `s81_2D_mimo` and `s81_2b_atria_A`. The returns READ ME's reading, that line 52 "describes pass 1", is replaced by this entry.
- **The confound this makes.** The four 2b audits are at mixed effort: Atria on A at high, and Atria on B, Mimo on A and Mimo on B at medium. The reason for crossing (line 102: the table "separates auditor from run") is mixed with effort in two places. Atria on A and Atria on B differ in effort as well as in the return audited. On return A, Atria and Mimo differ in effort as well as in auditor. Mimo's two 2b audits at medium also start each row from Mimo's 2a reading, made at high. The confound is recorded here, shown in the table (h), and measured in part by the effort controls (e).
- **(iii) When and on whose authority.** The owner's instruction of 23 September 2026, decision S17: "Use Atria and Mimo on medium thinking effort for cross examination." Applying it to the pending S81 calls, and keeping the accepted returns at high, is Claude's ruling.
- **(iv) Before or after the data.** After the five accepted Stage 2 returns at high, and after pass 1 of the three pending calls at high. Before any pass-2 return.

## d. How a pass cut off by the end of the session counts

- **(i) The second version.** Line 149 (step 1): "an empty or failed return is kept and run once more, recorded as a second attempt."
- **(ii) Instead: Claude's ruling.** A pass cut off by the end of the session is not "an empty or failed return" in the sense of step 1, and it does not use the one further run. Such a pass is one that left no receipt and no failure recorded by the caller, `tools/s80_call.py`.
  - `s81_2b_atria_B` and `s81_2b_mimo_B`: pass 1 was cut off, with no receipt (returns READ ME, lines 31 and 35). Pass 2 is their first completed attempt. If pass 2 fails, each may be run once more, as pass 3.
  - `s81_2b_mimo_A`: pass 1 failed, with three attempts rejected and a failed receipt (`s81_2b_mimo_A.pass1.receipt.json`, `s81_2b_mimo_A.pass1.error.txt`). Pass 2 is its one further run. If pass 2 fails, the call has failed twice, and Claude decides whether it is missing from the round.
  - The returns READ ME's sentence "Pass 2 is that second attempt for each of the three calls" (line 47) holds for `s81_2b_mimo_A` only.
  - The code does not yet follow the ruling. `tools/s81_build.py` sets `MAX_PASS = 2` and refuses any pass 3. It will be changed after the run, and not while the run is live, to allow a pass 3 only for a call whose pass 1 left no receipt.
- **(iii) When and on whose authority.** Claude's ruling, 23 September 2026, written down here at 11:33 UTC.
- **(iv) Before or after the data.** After pass 1 of the three calls. Before any pass-2 return: at 11:33:36 UTC none of the three calls had a pass-2 response, receipt, error or attempt file. At that time `returns/` held these files, by name only:
  - `READ ME - the three pending 2b calls, pass 1 at high effort, pass 2 at medium.md`, and the folders `Sonnet testers - set aside by decision S16`, `Stage 2 on the Sonnet testers - stopped by decision S16` and `effort controls`;
  - `s81_1C_A`, `s81_1C_B`, `s81_1D_A`, `s81_1D_B`, `s81_1K_A`, `s81_1K_B`, each with `.pass2.cleared.receipt.json`, `.pass2.void.txt`, `.receipt.json`, `.request.md`, `.response.txt`;
  - `s81_2D_atria`, `s81_2D_mimo`, `s81_2a_atria`, each with `.reasoning.txt`, `.receipt.json`, `.request.json`, `.response.txt`;
  - `s81_2a_mimo`: `.pass1.a1.reasoning.txt`, `.pass1.a1.truncated.txt`, `.pass1.a2.reasoning.txt`, `.pass1.a2.truncated.txt`, `.pass1.a3.reasoning.txt`, `.pass1.a3.truncated.txt`, `.pass1.error.txt`, `.pass1.receipt.json`, `.reasoning.txt`, `.receipt.json`, `.request.json`, `.response.txt`;
  - `s81_2b_atria_A`: `.pass1.a2.reasoning.txt`, `.pass1.a2.truncated.txt`, `.reasoning.txt`, `.receipt.json`, `.request.json`, `.response.txt`;
  - `s81_2b_atria_B`: `.pass1.request.json`, `.request.json`;
  - `s81_2b_mimo_A`: `.pass1.a1.reasoning.txt`, `.pass1.a1.truncated.txt`, `.pass1.a2.reasoning.txt`, `.pass1.a2.truncated.txt`, `.pass1.a3.reasoning.txt`, `.pass1.a3.truncated.txt`, `.pass1.error.txt`, `.pass1.receipt.json`, `.pass1.request.json`, `.request.json`;
  - `s81_2b_mimo_B`: `.pass1.a1.reasoning.txt`, `.pass1.a1.truncated.txt`, `.pass1.a2.reasoning.txt`, `.pass1.a2.truncated.txt`, `.pass1.request.json`, `.request.json`.

## e. The effort controls

- **(i) The second version.** It has no such calls. Line 15: "6 Sonnet agents (+ reruns) and 8 API calls (+ 2W)". Line 202: "Then `run 2` (three calls in flight per provider)."
- **(ii) Instead.** Three effort controls were sent in the same process as pass 2 of the pending calls (`s81_build.py run 2 --effort-controls`, started 11:11 UTC): `s81_2b_atria_A.control-medium`, `s81_2b_atria_A.control-high` and `s81_2a_mimo.control-medium`. Each sends again the exact text of an accepted high-effort call, at a stated effort. They share the providers' slots with the real calls: two of Atria's three, one of Mimo's three. They stay outside the S81 table; `table` reads nothing in their folder. Their design, and the rule for reading them, is in `returns/effort controls/READ ME - effort controls, outside the S81 table.md`. That rule allows one secondary table, clearly labelled, beside the plan's table and never in its place (R7).
- **(iii) When and on whose authority.** Claude, on 23 September 2026, as an audit of its own process under decision S18.
- **(iv) Before or after the data.** After the accepted high-effort returns they repeat, `s81_2b_atria_A` and `s81_2a_mimo`. Their reading rule was written at 11:29 UTC. By then the Mimo control had returned and the first attempt of the Atria medium control had been cut off, but no one had opened either.

## f. Claude's rulings from the texts, before any return is opened

- **(i) The second version.** Line 151 (step 3): "**By Claude, against the two files directly, row by row:** O48 in full; every row where any reading of file 11 (either 1C, any 2b) differs from the baseline; ...". Line 204 (run order): "6. `table`; Claude's reading; S81 Results; log entry S81 and Status." Claude's reading came after the table, and on the rows the returns name.
- **(ii) Instead.** Before the table is built, two independent Claude readers each rule every one of the 52 cases, and every place where file 10 and file 11 differ, from the texts alone, with no return open. A Claude reconciler sets the two readings side by side and rules where they differ. The rulings are committed, in the folder `determination/`, before the table is built. Steps 3 and 4 then read the returns beside them.
- **(iii) When and on whose authority.** Claude, on 23 September 2026, to satisfy lesson S2: "a second reader writes its reading before it opens the first reader's".
- **(iv) Before or after the data.** Adopted after the Stage 1 and Stage 2 data existed, and before Claude opened any of it.

## g. Atria and Mimo cross-examine the determination

- **(i) The second version.** Line 105: "**Claude decides** (decision S13). The testers' and auditors' marks are evidence; Claude reads the theory's text on every row the rules below name, and rules." Steps 3 to 7 (lines 151 to 155) go from Claude's reading to the write-up, with no outside reading of the determination.
- **(ii) Instead.** Before S81 Results is final, Atria and Mimo, at medium effort, cross-examine Claude's determination. Their points are evidence, and Claude rules on each. No call to either provider is sent while the S81 run's process is alive, so that at most three calls are in flight to each.
- **(iii) When and on whose authority.** Adopted on 23 September 2026, under decision S15 ("Use the others for cross examination.") and decision S17 ("Use Atria and Mimo on medium thinking effort for cross examination.").
- **(iv) Before or after the data.** After the Stage 1 and Stage 2 data existed. Before the determination is finished and before any of it is sent.

## h. What the table shows

- **(i) The second version.** Line 150 (step 2): "each case's marks in 1K and 1C for each tester and in each of the four 2b audits (a 2W record in place of the 2b record where there is one)".
- **(ii) Instead.** The table produced by `s81_build.py table` also shows:
  - the effort of each 2b column in its heading, read from that call's `request.json` (for example "2b atria on A (high)");
  - a line under the table that names the effort confound of (c);
  - MISSING for an expected 2b audit with no accepted response. The present code drops such a column.

  This is coded after the run and before the table is built.
- **(iii) When and on whose authority.** Claude, on 23 September 2026.
- **(iv) Before or after the data.** After the effort switch and the accepted returns at high. Before any pass-2 return (at 11:33 UTC), and before the table is built.

## i. 2W cannot be built

- **(i) The second version.** Line 143: "**R**, from the rows left, the ten whose `sha256("S81-2b-residual|" + sha256(X's 1C return) + "|" + case)` sort first." Line 145: "**Stopping rule:** if an auditor marks DISAGREE (ON VERDICT or ON MARK) on any R row of tester X's return, Claude builds `widen <auditor> <X> <rows>` with every row outside the sample whose 1C quotations cite the same Part of file 11 as that row, and runs 2W for that auditor and tester."
- **(ii) Instead.** Rules M1 to M6 left 3 rows for tester A and 2 for tester B, so R drew those rows, not ten. Each sample (`sample - tester A.json`, `sample - tester B.json`) covers all 52 rows. No row lies outside either sample, so a `widen` has no rows and 2W cannot be built. S81 Results still records whether the stopping rule fired, that is, whether an auditor marked DISAGREE on an R row. The rule itself is unchanged.
- **(iii) When and on whose authority.** Claude's reading of the rule, 23 September 2026.
- **(iv) Before or after the data.** Found after the samples were drawn from the Stage 1 returns (`build2`). Recorded before Claude has read any 2b audit.

## j. The log entry

- **(i) The second version.** Line 155 (step 7): "and the log entry S81." Line 204 (run order 6): "log entry S81 and Status."
- **(ii) Instead.** The determination's log entry is S87. Log S81 already exists: it is the entry under which the round was built. By LEGEND's rule, a new entry takes the next number in the shared sequence at the time of writing. By lesson S5, that number is read from all three projects' logs. The highest number in any project's log is 86 (Language, L86), so the entry is S87. The round keeps its name, S81 (line 24).
- **(iii) When and on whose authority.** LEGEND's rule and lesson S5, applied by Claude on 23 September 2026.
- **(iv) Before or after the data.** It bears on no data.

## k. The Stage 1 receipts' reader label

- **(i) The second version.** Line 92: "a receipt to `.receipt.json` (folder, prompt and brief hashes, response hash, the hits, the transcript path, the model as served, and whether it is a Sonnet model)".
- **(ii) Instead.** The six Stage 1 receipts in `returns/` (`s81_1C_A.receipt.json` to `s81_1K_B.receipt.json`, and their `.pass2.cleared.receipt.json` copies) carry `"reader": "sonnet subagent"`. That is the collector's fixed label (`tools/s81_sonnet_collect.py`). The returns are in fact the S16 rerun by Claude subagents, and each receipt's `served_model_is_sonnet` is false. The returns and receipts are kept as they came. S81 Results names the reader correctly.
- **(iii) When and on whose authority.** Claude, on 23 September 2026.
- **(iv) Before or after the data.** Found after the Stage 1 returns were collected. It bears on no mark.

## l. The hand-back tool in the transcript check

- **(i) The second version.** Line 89: "TodoWrite and ToolSearch pass; any other tool voids."
- **(ii) Instead.** The harness's hand-back tool (`SubagentHandback`) passes too. A subagent returns its final report through it, and it opens no file. It is set in `tools/s81_sonnet_collect.py` (`PASS_TOOLS`).
- **(iii) When and on whose authority.** Claude's ruling, 23 September 2026 (the collector's comment; commit 1f37750).
- **(iv) Before or after the data.** After the first Stage 1 transcripts existed (the first collection, commit 1f37750, 06:34 UTC). It was applied to the rerun as well (log S83 (a)).

## Beside the plan, and changing none of its steps

The DeepSeek trial (log S83 (c); `results/S81 Trial - DeepSeek as a third auditor, three blind readings compared.md`) ran a third blind reading beside the plan. DeepSeek was not added as an auditor, and its reading is not part of the S81 table.
