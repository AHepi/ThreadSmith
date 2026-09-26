# The three pending 2b calls: pass 1 at high effort, pass 2 at medium

Written on 23 September 2026, in the day's second session, before any pass 2 call was sent. Claude subagents wrote it while preparing the tools for the orchestrator.

**The calls.** `s81_2b_atria_B` (Atria audits tester B's 1C), `s81_2b_mimo_A` (Mimo audits tester A's 1C) and `s81_2b_mimo_B` (Mimo audits tester B's 1C). The other 2b call, `s81_2b_atria_A`, and both 2D calls have accepted replies and are not sent again.

**What changed between the passes.** The owner's instruction of 23 September 2026 (decision S17) is that Atria and Mimo run at medium thinking effort for cross-examination. Pass 1 of each call was sent with `"reasoning_effort": "high"`, as its `pass1.request.json` records. Pass 2 goes with `"medium"`, the one shared setting `REASONING_EFFORT` in `tools/s80_common.py`, and records it in its `request.json` and its receipt (`"reasoning_effort"`). Everything else is as in pass 1:
- the same text, byte for byte;
- the same output limits (Mimo 131,072 tokens, Atria 65,536);
- temperature 0.7;
- thinking on.

The plan's line "thinking on (`reasoning_effort: high`)" (second version, "What is run") describes pass 1.

**The texts are unchanged.** `s81_build.py build2` was rebuilt into a scratch folder outside the repository. It gives the same bytes as `briefs/` for all four 2b texts and both 2D texts, and the same two sample files. Each pass 1 request carries its brief as its user message, byte for byte:

| Call | md5 of the brief |
| --- | --- |
| `s81_2b_atria_B` | 01e41090c468d6f0c7ee03a26ce2ef61 |
| `s81_2b_mimo_A` | f592d5e3c39bae1824e93fdeba521aaf |
| `s81_2b_mimo_B` | 3a0281aa4377e4b3ea09ee9a6f7941a6 |

Each text is the one Atria received for `s81_2b_atria_A` (md5 6f58a95c8515baae9eba2d0e706c1804), except for the sections the design changes: the reading under audit (tester B's 1C in place of A's) for `s81_2b_atria_B`, the blind readings (Mimo's 2a in place of Atria's) for `s81_2b_mimo_A`, and both for `s81_2b_mimo_B`. The brief, the theory and the cases are the same in all four.

## Renamed, content unchanged

`git mv`, before the run, so that no pass 2 file can land on a pass 1 file and the run itself renames nothing. The md5 of each file was checked before and after.

| Was | Now | What it is |
| --- | --- | --- |
| `s81_2b_atria_B.request.json` | `s81_2b_atria_B.pass1.request.json` | Pass 1's request (high, max_tokens 65,536). Pass 1 left no other file: no attempt came back with an answer that was kept, and no receipt was written before the session ended. |
| `s81_2b_mimo_A.receipt.json` | `s81_2b_mimo_A.pass1.receipt.json` | Pass 1's failed receipt. There were three attempts at 131,072, which ended in finish "length" (3,189 s), "length" (2,809 s) and none (695 s), and none of them gave any content. |
| `s81_2b_mimo_A.error.txt` | `s81_2b_mimo_A.pass1.error.txt` | Pass 1's error line. |
| `s81_2b_mimo_A.request.json` | `s81_2b_mimo_A.pass1.request.json` | Pass 1's request (high, max_tokens 131,072). |
| `s81_2b_mimo_B.request.json` | `s81_2b_mimo_B.pass1.request.json` | Pass 1's request (high, max_tokens 131,072). Pass 1 was cut off after two attempts that came back with no content, when the session ended. No receipt was written. |

These files already carried their pass number and stay where they are, unchanged:
- `s81_2b_mimo_A.pass1.a1`, `.a2` and `.a3`, each as `.truncated.txt` (empty) and `.reasoning.txt` (569,691, 557,260 and 249,327 bytes);
- `s81_2b_mimo_B.pass1.a1` and `.a2`, each as `.truncated.txt` (empty) and `.reasoning.txt` (552,843 and 559,420 bytes).

The renaming is what `tools/s80_call.py` does itself at the start of a new pass, as `s81_2a_mimo.pass1.*` shows. Two changes were made to it on the same day:
- It now keeps the earlier pass's request as well as its receipt and error.
- It numbers a new pass above every pass that left any file. Before, a pass that was cut off before its receipt would have been numbered 1 again, and `s81_2b_mimo_B`'s pass 1 attempt files would have been overwritten.

## Pass 2 and the plan's rule

The plan (second version, "How Claude determines the result", step 1) says: "Stage 2: every call accepted by `s80_call.py` (finish "stop", the last line `END OF REPORT`), its model as served, its request and response hashes; an empty or failed return is kept and run once more, recorded as a second attempt." Pass 2 is that second attempt for each of the three calls.

Inside a pass, `s80_call.py` makes up to six attempts. It stops after three replies that come back and fail acceptance. It retries disconnects and 429 or 5xx answers after a back-off, and it stops at once on 400, 401, 403, 404, 413 or 422. If pass 2 of a call fails, that call has failed twice, and Claude decides whether it is missing from the round.

`python Semantics/tools/s81_build.py run 2 --dry-run` prints, without sending anything, the calls, their pass numbers and every file each pass may write.
