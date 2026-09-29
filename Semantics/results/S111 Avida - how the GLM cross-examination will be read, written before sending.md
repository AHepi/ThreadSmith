# S111 Avida: how the GLM cross-examination will be read, written before sending

*Written 29 September 2026 by the one Opus 5.5 agent that did the whole S111 job under decision S56 (the plan, the runs, the measures, the results and the plain-words file), before anything of this cross-examination was built or sent. When this file was committed, the returns folder `results/S111 Avida - GLM cross-examination returns/` did not exist, no brief or manifest had been built, no call had been sent and no runner of it was going. It follows log S110's cross-examination rule (`results/S110 - how the GLM cross-examination will be read, written before sending.md`) where it says nothing else. It obeys decision S23 except where it quotes the owner; for what the theory judges it says "candidate" or "explanation", never "model" (S43).*

## The instruction

- **S56**, the owner's words: "It's capable of doing the whole thing on its own. Use GLM for cross examination." So one Opus agent did the whole S111 job, and GLM cross-examines it in place of a fresh Opus critical reviewer.
- **S59**: the job itself: the owner's three properties of knowledge (information that can cause itself to be copied, to resist change, to remain), measured on Avida's digital organisms, a working case of knowledge without explanation; the explanation kind comes next. Part B stays held before its settlement (S57); nothing of Part B, and nothing of S110, is sent, opened or written.
- **S39, S29, S17**: up to four GLM calls at once, each through Claude Code, at medium effort. **S20, S21, S23, S28, S43**: the owner's words bind every finding as content.

## What is sent

Four jobs, built by `tools/s111x_build.py` (Part A round 1's build imported for its helpers only; the sandboxed helper `tools/glm_via_claude_code_sandboxed.py` and the shell guard `tools/glm_sandbox_shell_guard.py` used unchanged), run by `tools/s111x_glm_loop.py` (log S110's cross-examination runner with its names changed):

| job | tag | angle |
|---|---|---|
| 1 | `s111x_glm_a` | (a) whether the measures measure the three properties as the owner stated them |
| 2 | `s111x_glm_b` | (b) the scripts and the numbers |
| 3 | `s111x_glm_c` | (c) what the program causes and what the simulated world does |
| 4 | `s111x_glm_d` | (d) the plain-words file against the results |

Each sandbox holds copies only: the plan written before running; the results (`.md`, `.json`); the plain-words file 111; this rule; Avida's configuration files as used; the build notes with Avida's rules as read from its source; the exact commands; the four summary tables (`.md`, `.json`); the six S111 scripts. Job 1 adds the decisions record and the two S110 records that give Marletto's test; job 4 adds the decisions record and plain file 110 (for style). **No sandbox holds Avida's source or binary, or any raw run output**: those stay in the scratch space, and the build refuses any source outside `Semantics/`. There is no program in any sandbox (no `model/` folder), so the guard refuses every command: GLM may Read, Glob and Grep, and writes nothing. Each brief quotes the owner's words (S19, S20, S21, S23, S28, S43, S56, S57, S59) and asks for objections, each with **the exact fix**, terse, at most about 3,000 words, last line `END OF REPORT`. The briefs, manifests and job list are named, with their md5s, in `tools/s111x_jobs - S111, GLM cross-examination.json`, written by the build and committed before the launch.

- **The call**: glm-5.3 through Claude Code (S29), `--effort medium` (S17), the 1,000,000-token window, 6 attempts, at most 3 answers without END OF REPORT, 7,200 seconds per attempt, `--rule` (this file, committed and unchanged from HEAD), `--brief-md5`, `--manifest-md5`. Up to 3 passes per job. Sandboxes in `<scratchpad>/s111x_sandboxes/`, homes in `<scratchpad>/s111x_homes/`. Returns in `results/S111 Avida - GLM cross-examination returns/`.
- **Before the launch**: a dry test of the four sandboxes with a dummy key (built by the helper's own `build_sandbox`; the guard handed a write, `touch`, two `python3 -c`, `cat`, `env`, a redirect and a run of one of the S111 scripts, each to be refused; every sandbox to come back unchanged; no Avida binary, no `.spop` or `.dat` file, no file larger than the summaries), recorded and committed; S110's GLM run (session leader PID 6632) must have exited (`kill -0 6632` fails), so that no more than four GLM calls run at once.

## How the replies will be read

1. **Nothing is opened until all four calls end.** No reply, receipt, reasoning file, attempt file, stream file or guard log of this cross-examination is opened until every job has ended its last allowed pass: the run log holds `s111x_glm_loop: every pass ended; …` and `loop ended <UTC time>`, and the process in the pid file has exited. The progress lines may be watched; they hold no reply text. If a call is still running 24 hours after the launch, the runner may be stopped by its PID and the calls not ended recorded as not returned.
2. **What counts as a reply**: only `<tag>.response.txt` (or `<tag>_pass<k>.response.txt`); failed calls count neither way; connection failures are not answers; a key in the output or a sandbox not unchanged is reported before anything else is read.
3. **One Opus agent reads every objection and settles each**, by argument from the plan, the results, the scripts, the configuration and Avida's source, or **by rerunning** (Avida, the scripts, or a new check) in the scratch space, never in the repository; and records for each: the objection, its settlement (stands, stands in part, does not stand), the reason (or the rerun and its numbers), and what it changes. An objection is a claim until settled; an objection repeated by several jobs decides nothing (arguments, not numbers); silence is not agreement. The agent writes `results/S111 Avida - the GLM cross-examination, settled.md`, created at once and filled as it goes.
4. **Findings that stand amend the S111 files in corrected copies**: `… , after the cross-examination.md` (and `.json`) beside the results file, and corrected copies of any summary table or script that changes (a script's corrected copy gets its own plain name and note); the files as sent are kept as they were. The plain-words file 111 is updated to match, and its note says it now follows the check. Nothing in the theory's text, formal core, claims or program, any Part A, Part B or S110 file, the decisions record or `authority/` is written.
5. **The owner's words bind every finding as content** (S20 to S59). An objection that would settle for the owner something the S111 files leave open (whether these organisms hold knowledge; how the three properties should be read; what the explanation kind needs) is recorded, not applied (S28, S21). No finding ranks anything (S20).
6. **Records** follow the settlement, by the same agent: an addition to log S111 in the project story and the plain story, and Status, INDEX and README as earlier entries did. Then the owner chooses the next step.

## How the run is launched

From the repository root, after this file's commit is pushed and the build and dry test are committed, once `kill -0 6632` fails, one process, detached so that it outlives the agent that starts it, with the key loaded only into its own environment from the session's key file and never opened or printed by the agent, and the other keys unset:

```
setsid nohup bash -c 'cd /home/user/ThreadSmith || exit 1; echo "launched $(date -u +%Y-%m-%dT%H:%M:%SZ)"; R="Semantics/results/S111 Avida - how the GLM cross-examination will be read, written before sending.md"; { git ls-files --error-unmatch -- "$R" >/dev/null && git diff --quiet HEAD -- "$R"; } || { echo "the reading rule is not committed or differs from HEAD; nothing sent"; exit 1; }; set -a; . <key file>; set +a; unset ATRIA_API_KEY MIMO_API_KEY OPENAI_API_KEY; python3 -B Semantics/tools/s111x_glm_loop.py "Semantics/tools/s111x_jobs - S111, GLM cross-examination.json"; echo "loop ended $(date -u +%Y-%m-%dT%H:%M:%SZ)"' > <scratchpad>/s111x_glm_run.log 2>&1 < /dev/null &
```

The process id of the session leader goes in `<scratchpad>/s111x_glm_run.pid`. The launching agent writes `results/S111 Avida - GLM cross-examination, launch record.md`, commits it, and hands back once the log shows all four calls sent.

## Unsure

- GLM cannot run Avida or see the raw output; it judges the numbers by their consistency with the scripts, the configuration and each other. A claim it cannot check is to be listed as not reached, not as an objection.
- GLM sees Avida's rules only as the build notes give them, with source lines; a rule misread there could pass unnoticed.
- One GLM job per angle may miss what the work also missed.

Decided by Claude under decisions S17, S29, S39, S56 and S59. 29 September 2026.
