# Effort controls: outside the S81 plan and its table

Written on 23 September 2026, before any control was sent, by Claude subagents preparing the run for the orchestrator.

**What they are for.** Decision S17 moved the cross-examination calls from `reasoning_effort` "high" to "medium". The three 2b calls still pending go at medium on their pass 2; the calls already accepted went at high. That change was made after data (lesson S2). These controls measure what the switch itself changes, so that a difference between the accepted high-effort returns and the medium-effort ones can be read against it. Each control sends again the exact text of a call that was accepted at high effort, at a stated effort. The repeat at high separates run-to-run variation from the effect of the effort.

**Who decided, and when.** Claude decided them after the data, as an audit of its own process under decision S18 ("always audit your own processes"). They are extra evidence about the method. The owner did not ask for them, and the plan does not include them.

**They stay out of the S81 table.** The table is built by `tools/s81_build.py table`, which opens named files directly in `returns/` and reads nothing in this folder. That was checked before the run: a trace on a scratch copy of the outputs, with decoy files in this folder under the real calls' names, recorded no read here. Each control's tag also differs from every real tag (`.control-<effort>`).

| Control | Text sent (the accepted call's brief, byte for byte) | Provider | Effort | The accepted call's own effort |
| --- | --- | --- | --- | --- |
| `s81_2b_atria_A.control-medium` | `briefs/s81_2b_atria_A.txt`, md5 6f58a95c8515baae9eba2d0e706c1804 | Atria | medium | high (pass 1) |
| `s81_2b_atria_A.control-high` | the same | Atria | high | high (pass 1) |
| `s81_2a_mimo.control-medium` | `briefs/s81_2a_mimo.txt`, md5 895fa740266b9161081f1b31c72f1b3c | Mimo | medium | high (pass 2) |

Before sending, `s81_build.py` checks that each brief's SHA-256 equals the `user_sha256` in the accepted call's receipt. Mimo has no repeat at high, because its three slots are taken by the two real calls and this control. So Mimo's comparison cannot separate run-to-run variation from the effect of the effort.

**Run as the real calls are.** All six calls go in one process, `s81_build.py run 2 --effort-controls`, with at most three in flight per provider (decision S17): on Atria, `s81_2b_atria_B` and the two Atria controls; on Mimo, `s81_2b_mimo_A`, `s81_2b_mimo_B` and the Mimo control. Everything else is the same as for the real calls:
- the same `tools/s80_call.py`;
- the same output limits (Atria 65,536 tokens, Mimo 131,072);
- the same acceptance rule: finish "stop", and `END OF REPORT` on the last line;
- up to six attempts, stopping after three replies that come back and fail;
- the same deadlines: 900 s of silence, 7,200 s for a whole stream;
- temperature 0.7, thinking on.

The effort sent is recorded in each control's `request.json` and in its receipt (`"reasoning_effort"`). The receipt's `extra` names the call it controls.

**One pass each.** `s81_build.py` refuses to send a control if any file of it is already in this folder. A failed control stays failed and is recorded as it is.

## How the controls will be read (written before any control's data was opened)

Written by Claude at 11:29 UTC on 23 September 2026, while the run was still going (lessons S2 and 35: the reading rule is fixed before the data it reads). This rule was due before any control returned. It was not ready in time. At 11:28:44 and again at 11:29:04 UTC this folder held these files, listed by name only:
- `READ ME - effort controls, outside the S81 table.md`
- `s81_2a_mimo.control-medium.reasoning.txt`
- `s81_2a_mimo.control-medium.receipt.json`
- `s81_2a_mimo.control-medium.request.json`
- `s81_2a_mimo.control-medium.response.txt`
- `s81_2b_atria_A.control-high.request.json`
- `s81_2b_atria_A.control-medium.pass1.a1.reasoning.txt`
- `s81_2b_atria_A.control-medium.pass1.a1.truncated.txt`
- `s81_2b_atria_A.control-medium.request.json`

So the Mimo control had already returned, and the first attempt of the Atria medium control had been cut off. The Atria high control had not returned. No one writing this rule opened any response, reasoning, truncated or receipt file of a control. The rule below applies to all three controls in the same way. The fact that the Mimo control came back before the rule existed is recorded here and goes with any reading of it.

**R1. Whether each provider honours the effort setting.** For each provider, the reasoning tokens (and the characters of reasoning text) at medium are set against those at high on the same text: Atria, `control-medium` against the original `s81_2b_atria_A` and `control-high`; Mimo, `control-medium` against the accepted `s81_2a_mimo`. They are reported as counts and as a ratio, medium over high. The counts come from the receipts and the reasoning files.

**R2. Atria, text A: three readings.** The three readings are the original accepted `s81_2b_atria_A` (high), `control-high` and `control-medium`. For each row, the four fields YOUR MARK, BLIND MARK, ON VERDICT and ON MARK are compared across the three. The report gives:
- the number of rows where all three readings agree;
- the number of rows where exactly one reading differs from the other two, split by which one it is (the original high, `control-high`, or `control-medium`);
- the number of rows where all three differ.

If the effort made no difference, `control-medium` would be the odd one out on about one third of the rows with exactly one odd reading. The counts are reported as they are. With one reading for each condition, no claim of significance is made.

**R3. Replay check.** The request body of `control-high` is byte for byte the same as the original's; this is checked by comparing the sha256 of the two request bodies. If the response sha256 or the response id of `control-high` equals the original's, the provider replayed its earlier answer. In that case `control-high` says nothing about run-to-run variation, and the report says so.

**R4. A failed control.** A control that fails supports no inference about effort beyond the fact that it failed and any token usage recorded for it.

**R5. Mimo.** `control-medium` is set against the accepted `s81_2a_mimo` (high) on the 2a text. For each row, FINDINGS, OPEN and SPLIT are compared, and the differences are reported. The comparison is descriptive only. There is no repeat at high, so a difference mixes the effect of the effort with run-to-run variation.

**R6. Agreement is not equivalence.** One medium reading that agrees with one high reading does not show that the two efforts are equivalent.

**R7. Outside the table.** The controls stay outside the S81 table. A second table may be shown beside the plan's table, clearly labelled, never in its place: the four 2b audits with the Atria `control-medium` in place of the high-effort `s81_2b_atria_A`, so that all four are at medium.

**R8. Confounds, stated in advance.**
- The high-effort originals are the attempts that happened to fit the output limit. `s81_2b_atria_A` used 64,037 of its 65,536 tokens, on its 4th attempt. A control at high may fail where the original, by chance, did not.
- About 2.7 hours separate the originals from the controls. The provider's model or serving may have changed in between.
- The controls ran in the same process as the last allowed pass of the real calls, and shared their Atria and Mimo slots (at most three in flight per provider).
