# S110 - how the GLM cross-examination will be read, written before sending

*Written 29 September 2026 by the one Opus 5.5 agent that did the whole S110 job under decision S56 (files 1 to 4 and the change map's data), before anything of this cross-examination was built or sent. When this file was committed, the returns folder `results/S110 - GLM cross-examination returns/` did not exist, no brief or manifest had been built, no call had been sent and no runner of it was going. It follows Part A round 2's cross-examination rule (`results/S108 Part A round 2 - how the GLM cross-examination will be read, written before sending.md`) where it says nothing else. It obeys decision S23 except where it quotes the owner; for what the theory judges it says "candidate" or "explanation", never "model" (S43).*

## The instruction

- **S56**, the owner's words: "It's capable of doing the whole thing on its own. Use GLM for cross examination." So one Opus agent did the whole S110 job, and GLM cross-examines it in place of a fresh Opus critical reviewer.
- **S57, S58**: the job itself (error correction from constructor theory's perspective; a change map of the owner's six earlier frameworks and the present theory; the owner's question how to tell when something in a creative agent is knowledge). Part B stays held before its settlement (S57); nothing of Part B is sent, opened or written.
- **S39, S29, S17**: up to four GLM calls at once, each through Claude Code, at medium effort. **S19** with lesson S29: book quotations at most 25 words, never chained. **S20 to S58**: the owner's words bind every finding as content.

## What is sent

Four jobs, built by `tools/s110x_build.py` (Part A round 1's build imported for its helpers only; the sandboxed helper `tools/glm_via_claude_code_sandboxed.py` and the shell guard `tools/glm_sandbox_shell_guard.py` used unchanged), run by `tools/s110x_glm_loop.py` (Part A round 2's cross-examination runner with its names changed):

| job | tag | angle |
|---|---|---|
| 1 | `s110x_glm_a` | (a) the change map against FW0 and I2 |
| 2 | `s110x_glm_b` | (b) the change map against FW2, FW3 and FW4 |
| 3 | `s110x_glm_c` | (c) the change map against FW5, the present theory and the S89 audit |
| 4 | `s110x_glm_d` | (d) files 1 and 3 for internal consistency, for Claude's readings passed off as the book's, and against the owner's decisions S20 to S58 |

Each sandbox holds copies only: the six frameworks as supplied; the present theory (`tests/107`); the S89 audit; the four S110 files (file 1, the change map and its `.json`, file 3, plain file 110) and this rule. Job 3 adds the records its "recorded" edges cite (the S95 record, `authority/NOT-IN-BUNDLE.md`, the S108 round 2 record, the decisions record); job 4 adds the decisions record. **No sandbox holds either book or any text extracted from them**: the quotations are checked by `tools/s110_quote_check.py` instead, and the build refuses any source from the scratchpad. There is no program in any sandbox, so the guard refuses every command: GLM may Read, Glob and Grep, and writes nothing. Each brief quotes the owner's words (S19, S20, S21, S23, S25, S27, S28, S31, S34, S43, S56, S57, S58) and asks for objections, each with **the exact fix**, terse, at most about 3,000 words, last line `END OF REPORT`. The briefs, manifests and job list are named, with their md5s, in `tools/s110x_jobs - S110, GLM cross-examination.json`, written by the build and committed before the launch.

- **The call**: glm-5.3 through Claude Code (S29), `--effort medium` (S17), the 1,000,000-token window, 6 attempts, at most 3 answers without END OF REPORT, 7,200 seconds per attempt, `--rule` (this file, committed and unchanged from HEAD), `--brief-md5`, `--manifest-md5`. Up to 3 passes per job. Sandboxes in `<scratchpad>/s110x_sandboxes/`, homes in `<scratchpad>/s110x_homes/`. Returns in `results/S110 - GLM cross-examination returns/`.
- **Before the launch**: a dry test of the four sandboxes with a dummy key (built by the helper's own `build_sandbox`; the guard handed a write, `python3 -c`, `cat`, `env` and a redirect, each to be refused; every sandbox to come back unchanged), recorded and committed; Part B's GLM run (session leader PID 5784) must have exited, so that no more than four GLM calls run at once.

## How the replies will be read

1. **Nothing is opened until all four calls end.** No reply, receipt, reasoning file, attempt file, stream file or guard log of this cross-examination is opened until every job has ended its last allowed pass: the run log holds `s110x_glm_loop: every pass ended; …` and `loop ended <UTC time>`, and the process in the pid file has exited. The progress lines may be watched; they hold no reply text. If a call is still running 24 hours after the launch, the runner may be stopped by its PID and the calls not ended recorded as not returned.
2. **What counts as a reply**: only `<tag>.response.txt` (or `<tag>_pass<k>.response.txt`); failed calls count neither way; connection failures are not answers; a key in the output or a sandbox not unchanged is reported before anything else is read.
3. **One Opus agent reads every objection and settles each by argument**, from the frameworks, the present theory, the S89 audit, the records, the owner's words and, for a book quotation or a statement marked as the book's, the book's extracted text in the scratchpad (checked by script; never copied into the repository beyond checked quotations), and records for each: the objection, its settlement (stands, stands in part, does not stand), the reason, and what it changes. An objection is a claim until settled; an objection repeated by several jobs decides nothing (arguments, not numbers); silence is not agreement. The agent writes `results/S110 - the GLM cross-examination, settled.md`, created at once and filled as it goes.
4. **Findings that stand amend the S110 files in corrected copies**: `… , after the cross-examination.md` beside each of files 1 to 3 (and the change map's `.json`, regenerated by `tools/s110_change_map.py` from corrected data), each amendment marked with the objection's id; the files as sent are kept as they were. Plain file 110 is updated to match, and its note says it now follows the check. Nothing in the theory's text, formal core, claims or program, any Part A or Part B file, the decisions record, `authority/` or the six frameworks is written.
5. **The owner's words bind every finding as content** (S20 to S58). An objection that would settle for the owner something the S110 files leave open (which question to take forward; the readings of "capable" and of what a spreading idea is knowledge of; whether the two-types result holds) is recorded, not applied (S28, S21). No finding ranks the options (S20).
6. **Records** follow the settlement, by the same agent: an addition to log S110 in the project story and the plain story, and Status, INDEX and README as earlier entries did. Then the owner chooses which question to take forward (S57).

## How the run is launched

From the repository root, after this file's commit is pushed and the build and dry test are committed, one process, detached so that it outlives the agent that starts it, with the key loaded only into its own environment from the session's key file and never printed, and the other keys unset:

```
setsid nohup bash -c 'cd /home/user/ThreadSmith || exit 1; echo "launched $(date -u +%Y-%m-%dT%H:%M:%SZ)"; R="Semantics/results/S110 - how the GLM cross-examination will be read, written before sending.md"; { git ls-files --error-unmatch -- "$R" >/dev/null && git diff --quiet HEAD -- "$R"; } || { echo "the reading rule is not committed or differs from HEAD; nothing sent"; exit 1; }; set -a; . <key file>; set +a; unset ATRIA_API_KEY MIMO_API_KEY OPENAI_API_KEY; python3 -B Semantics/tools/s110x_glm_loop.py "Semantics/tools/s110x_jobs - S110, GLM cross-examination.json"; echo "loop ended $(date -u +%Y-%m-%dT%H:%M:%SZ)"' > <scratchpad>/s110x_glm_run.log 2>&1 < /dev/null &
```

The process id of the session leader (not `setsid`'s own) goes in `<scratchpad>/s110x_glm_run.pid`. The launching agent writes `results/S110 - GLM cross-examination, launch record.md`, commits it, and hands back once the log shows all four calls sent.

## Unsure

- GLM cannot see the books, so it judges statements marked as the book's only from the quotations and the S89 audit; a statement it cannot check is to be listed as not reached, not as an objection.
- One GLM job per angle is not a second reading of the frameworks: it reads the map against them, and may miss what the map also missed.
- 71 of the map's 132 edges are Claude's reading across missing documents; the cross-examination can test their faithfulness to what is supplied, not to what is missing.

Decided by Claude under decisions S17, S29, S39, S56, S57 and S58. 29 September 2026.
