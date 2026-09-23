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
