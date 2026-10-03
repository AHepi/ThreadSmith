# S112 What the evolved sums are: how the GLM cross-examination will be read, written before sending

*Written 30 September 2026 by the one Opus 5.5 agent that does the whole S112 job under decision S56 (the plan, the instruction ablations, the traces, the execution-environment tests, the results and the plain-words file), before anything of this cross-examination was built or sent. When this file was committed, the returns folder `results/S112 What the evolved sums are - GLM cross-examination returns/` did not exist, no brief or manifest had been built, no call had been sent and no runner of it was going. It follows log S111's cross-examination rule (`results/S111 Avida - how the GLM cross-examination will be read, written before sending.md`) where it says nothing else. It is written in the owner's Avida terms (decision S61, `records/Semantics - Avida terms, given by the owner.md`). It obeys decision S23 except where it quotes the owner; for what the theory judges it says "candidate" or "explanation", never "model" (S43).*

## The instruction

- **S56**, the owner's words: "It's capable of doing the whole thing on its own. Use GLM for cross examination." So one Opus agent does the whole S112 job, and GLM cross-examines it in place of a fresh Opus critical reviewer.
- **S60**: the job itself, in the owner's words: "Of the of machines that could do rudimentary math, what needed to be removed in order for them to stop doing that math. Ignore the fact that they were evolved to solve a problem, I want to know what that evolved information actually is, given the environment it was instantiated in." **S61**: the owner's Avida terms, used in every file, brief and reply of this log.
- **S39, S29, S17**: up to four GLM calls at once, each through Claude Code, at medium effort. **S20, S21, S23, S28, S43**: the owner's words bind every finding as content. Part B stays held before its settlement (S57); nothing of Part B, S110 or S111 is written.

## What is sent

Four jobs, built by `tools/s112x_build.py` (log S111's build with its names, files and briefs changed; Part A round 1's build imported for its helpers only; the sandboxed helper `tools/glm_via_claude_code_sandboxed.py` and the shell guard `tools/glm_sandbox_shell_guard.py` used unchanged), run by `tools/s112x_glm_loop.py` (log S111's runner with its names changed):

| job | tag | angle |
|---|---|---|
| 1 | `s112x_glm_a` | (a) whether the answer answers the owner's two questions exactly |
| 2 | `s112x_glm_b` | (b) the minimal-removal search (instruction ablation) and its limits |
| 3 | `s112x_glm_c` | (c) the circuits and their canonical forms against the traces |
| 4 | `s112x_glm_d` | (d) the plain-words file against the results |

Each sandbox holds copies only: the plan written before running (with its dated note on the terms); the results (`.md`, `.json`); the plain-words file 112; this rule; the owner's Avida terms; the exact commands; log S111's Avida configuration files and its build notes (Avida's rules as read from its source); the five S112 scripts (the test-processor helper, the trace reader, the minimal-removal search, the execution-environment tests, the summariser). Job 1 adds the decisions record and S111's results after its cross-examination; job 4 adds the decisions record and plain file 111 (for style). **No sandbox holds Avida's source or binary, or any raw output** (traces, ablation lists, saved program populations): those stay in the scratch space, and the build refuses any source outside `Semantics/`. There is no program in any sandbox (no `model/` folder), so the guard refuses every command: GLM may Read, Glob and Grep, and writes nothing. Each brief quotes the owner's words (S20, S21, S23, S28, S43, S56, S60, S61) and asks for objections, each with **the exact fix**, terse, at most about 3,000 words, last line `END OF REPORT`. The briefs, manifests and job list are named, with their md5s, in `tools/s112x_jobs - S112, GLM cross-examination.json`, written by the build and committed before the launch.

- **The call**: glm-5.3 through Claude Code (S29), `--effort medium` (S17), the 1,000,000-token window, 6 attempts, at most 3 answers without END OF REPORT, 7,200 seconds per attempt, `--rule` (this file, committed and unchanged from HEAD), `--brief-md5`, `--manifest-md5`. Up to 3 passes per job. Sandboxes in `<scratchpad>/s112x_sandboxes/`, homes in `<scratchpad>/s112x_homes/`. Returns in `results/S112 What the evolved sums are - GLM cross-examination returns/`.
- **Before the launch**: a dry test of the four sandboxes with a dummy key (built by the helper's own `build_sandbox`; the guard handed a write, `touch`, two `python3 -c`, `cat`, `env`, a redirect and a run of one of the S112 scripts, each to be refused; every sandbox to come back unchanged; no Avida binary, no `.spop`, `.dat`, `.trace` or `.jsonl` file, no file larger than 400,000 bytes), recorded and committed; no other GLM run of this project going, so that no more than four GLM calls run at once.

## How the replies will be read

1. **Nothing is opened until all four calls end.** No reply, receipt, reasoning file, attempt file, stream file or guard log of this cross-examination is opened until every job has ended its last allowed pass: the run log holds `s112x_glm_loop: every pass ended; …` and `loop ended <UTC time>`, and the process in the pid file has exited. The progress lines may be watched; they hold no reply text. If a call is still running 24 hours after the launch, the runner may be stopped by its PID and the calls not ended recorded as not returned.
2. **What counts as a reply**: only `<tag>.response.txt` (or `<tag>_pass<k>.response.txt`); failed calls count neither way; connection failures are not answers; a key in the output or a sandbox not unchanged is reported before anything else is read.
3. **One Opus agent reads every objection and settles each**, by argument from the plan, the results, the scripts, the configuration and Avida's source, or **by rerunning** (Avida in analysis mode, the scripts, or a new check) in the scratch space (`/tmp/claude-0/-home-user-ThreadSmith/8d9323da-c0ec-57ec-91fd-8f99ca99320a/scratchpad`), never in the repository; and records for each: the objection, its settlement (stands, stands in part, does not stand), the reason (or the rerun and its numbers), and what it changes. An objection is a claim until settled; an objection repeated by several jobs decides nothing (arguments, not numbers); silence is not agreement. The agent writes `results/S112 What the evolved sums are - the GLM cross-examination, settled.md`, created at once and filled as it goes.
4. **Findings that stand amend the S112 files in corrected copies**: `… , after the cross-examination.md` (and `.json`) beside the results file, and corrected copies of any script that changes (with its own plain name and note); the files as sent are kept as they were. The plain-words file 112 is updated to match, and its note says it now follows the check. Nothing in the theory's text, formal core, claims or program, any Part A, Part B, S110 or S111 file, the decisions record, the S61 terms file or `authority/` is written.
5. **The owner's words bind every finding as content** (S20 to S61). An objection that would settle for the owner something the S112 files leave open (whether what was found is knowledge; how the owner's question should be read beyond what S60 says) is recorded, not applied (S28, S21). No finding ranks anything (S20).
6. **Records** follow the settlement, by the same agent: an addition to log S112 in the project story and the plain story, and Status, INDEX and README as earlier entries did. Then the owner chooses the next step.

## How the run is launched

From the repository root, after this file's commit is pushed and the build and dry test are committed, one process, detached so that it outlives the agent that starts it, with the key loaded only into its own environment from the session's key file and never opened or printed by the agent, and the other keys unset:

```
setsid nohup bash -c 'cd /home/user/ThreadSmith || exit 1; echo "launched $(date -u +%Y-%m-%dT%H:%M:%SZ)"; R="Semantics/results/S112 What the evolved sums are - how the GLM cross-examination will be read, written before sending.md"; { git ls-files --error-unmatch -- "$R" >/dev/null && git diff --quiet HEAD -- "$R"; } || { echo "the reading rule is not committed or differs from HEAD; nothing sent"; exit 1; }; set -a; . <key file>; set +a; unset ATRIA_API_KEY MIMO_API_KEY OPENAI_API_KEY; python3 -B Semantics/tools/s112x_glm_loop.py "Semantics/tools/s112x_jobs - S112, GLM cross-examination.json"; echo "loop ended $(date -u +%Y-%m-%dT%H:%M:%SZ)"' > <scratchpad>/s112x_glm_run.log 2>&1 < /dev/null &
```

The process id of the session leader goes in `<scratchpad>/s112x_glm_run.pid`. The launching agent writes `results/S112 What the evolved sums are - GLM cross-examination, launch record.md`, commits it, and hands back once the log shows all four calls sent.

## Unsure

- GLM cannot run Avida or see the traces or the ablation lists; it judges the numbers by their consistency with the scripts, the configuration, the worked examples and each other. A claim it cannot check is to be listed as not reached, not as an objection.
- GLM sees Avida's rules only as S111's build notes and the S112 scripts' citations give them; a rule misread there could pass unnoticed.
- One GLM job per angle may miss what the work also missed.

Decided by Claude under decisions S17, S29, S39, S56, S60 and S61. 30 September 2026.
