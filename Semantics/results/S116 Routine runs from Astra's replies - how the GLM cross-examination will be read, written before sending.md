# S116 Routine runs from Astra's replies: how the GLM cross-examination will be read, written before sending

*Written 30 September 2026 by the one Opus 5.5 agent that does the whole S116 job under decisions S56 and S68 (the plan, batches 2 and 3 of S115's plan of runs, the continuation of FIXED LARGE LIST seed 2, the results and the plain-words file), before anything of this cross-examination was built or sent. When this file was committed, the returns folder `results/S116 Routine runs from Astra's replies - GLM cross-examination returns/` did not exist, no brief or manifest had been built, no call had been sent and no runner of it was going (the runner `tools/s116x_glm_loop.py`, log S113's runner with its names changed, was written, not run; the build `tools/s116x_build.py` was not yet written). It follows log S113's cross-examination rule (`results/S113 Which execution environments learn - how the GLM cross-examination will be read, written before sending.md`) where it says nothing else. It is written in the owner's Avida terms (decision S61, `records/Semantics - Avida terms, given by the owner.md`). It obeys decision S23 except where it quotes the owner; for what the theory judges it says "candidate" or "explanation", never "model" (S43).*

## The instruction

- **S56**, the owner's words: "It's capable of doing the whole thing on its own. Use GLM for cross examination." So one Opus agent does the whole S116 job, and GLM cross-examines it.
- **S63**, the question the runs serve: "The execution environment is an important clue. Looking inside the machines is the wrong direction. The question is, what kind of execution environment can use these machines to progressively learn how to do new things..." **S66 to S68**: GPT 6 Astra's replies, S115's check of them and its plan of runs; "Noo too many agents" (S68): one agent per job, never more than two agents at once. **S61**: the owner's Avida terms.
- **S39, S29, S17**: up to four GLM calls at once, each through Claude Code, at medium effort. **S20, S21, S23, S28, S43**: the owner's words bind every finding as content.

## What is sent

Four jobs, built by `tools/s116x_build.py` (log S113's build with its names, files and briefs changed; Part A round 1's build imported for its helpers only; the sandboxed helper `tools/glm_via_claude_code_sandboxed.py` and the shell guard `tools/glm_sandbox_shell_guard.py` used unchanged), run by `tools/s116x_glm_loop.py`:

| job | tag | angle |
|---|---|---|
| 1 | `s116x_glm_a` | (a) whether the runs answer what the plan says they test, and whether the comparisons with S113 are fair |
| 2 | `s116x_glm_b` | (b) the measures and the scripts |
| 3 | `s116x_glm_c` | (c) the results against the plan |
| 4 | `s116x_glm_d` | (d) the plain-words file against the results |

Each sandbox holds copies only, all committed under `Semantics/`: the S116 plan written before running; the results (`.md`, `.json`); the plain-words file 116; this rule; the owner's Avida terms; the exact commands; S115's plan of runs and its checks of replies 01, 02 and 05; S113's corrected results and its settlement; the S114 restart audit's results; the S116 scripts, the S113 scripts they import, and the reply scripts they run (reply 01's probe and summariser, reply 02's generator); S111's Avida configuration and build notes. Job 1 adds the decisions record; job 4 adds the decisions record and plain file 113 (for style). **No sandbox holds Avida's source or binary, or any raw output** (Avida's data files, saved program populations, probe results): those stay in the scratch space, and the build refuses any source outside `Semantics/`. There is no program in any sandbox, so the guard refuses every command: GLM may Read, Glob and Grep, and writes nothing, executes nothing of its own. Each brief quotes the owner's words and asks for objections, each with **the exact fix**, terse, at most about 3,000 words, last line `END OF REPORT`. The briefs, manifests and job list are named, with their md5s, in `tools/s116x_jobs - S116, GLM cross-examination.json`, written by the build and committed before the launch.

- **The call**: glm-5.3 through Claude Code (S29), `--effort medium` (S17), the 1,000,000-token window, 6 attempts, at most 3 answers without END OF REPORT, 7,200 seconds per attempt, `--rule` (this file, committed and unchanged from HEAD), `--brief-md5`, `--manifest-md5`. Up to 3 passes per job. Sandboxes in `<scratchpad>/s116x_sandboxes/`, homes in `<scratchpad>/s116x_homes/`. Returns in `results/S116 Routine runs from Astra's replies - GLM cross-examination returns/`.
- **Before the launch**: a dry test of the four sandboxes with a dummy key (built by the helper's own `build_sandbox`; the guard handed a write, `touch`, two `python3 -c`, `cat`, `env`, a redirect and a run of one of the S116 scripts, each to be refused; every sandbox to come back unchanged; no Avida binary, no `.spop`, `.dat`, `.trace`, `.tsv` or `.jsonl` file, no file larger than 400,000 bytes), recorded and committed; no other GLM run of this project going.

## How the replies will be read

1. **Nothing is opened until all four calls end.** No reply, receipt, reasoning file, attempt file, stream file or guard log of this cross-examination is opened until every job has ended its last allowed pass: the run log holds `s116x_glm_loop: every pass ended; …` and `loop ended <UTC time>`, and the process in the pid file has exited. The progress lines may be watched; they hold no reply text. If a call is still running 24 hours after the launch, the runner may be stopped by its PID and the calls not ended recorded as not returned.
2. **What counts as a reply**: only `<tag>.response.txt` (or `<tag>_pass<k>.response.txt`); failed calls count neither way; a key in the output or a sandbox not unchanged is reported before anything else is read.
3. **One Opus agent settles each objection** (S56, S68: one agent, no subagent or workflow), by argument from the plan, the results, the scripts, the configuration and Avida's source, or **by rerunning** (Avida in analysis mode or short runs under `timeout` and `nice -n 19`, the scripts, or a new check) in the scratch space (`/tmp/claude-0/-home-user-ThreadSmith/8d9323da-c0ec-57ec-91fd-8f99ca99320a/scratchpad`), never in the repository; and records for each: the objection, its settlement (stands, stands in part, does not stand), the reason (or the rerun and its numbers), and what it changes. An objection is a claim until settled; an objection repeated by several jobs counts once; silence is not agreement. The agent writes `results/S116 Routine runs from Astra's replies - the GLM cross-examination, settled.md`, created at once and filled as it goes.
4. **Findings that stand amend the S116 files in corrected copies**: `… results, after the cross-examination.md` (and `.json`) beside the results file, and corrected copies of any script that changes (with its own plain name and note); the files as sent are kept as they were. The plain-words file 116 is corrected to match, and its note says it now follows the check. Nothing in the theory's text, formal core, claims or program, any Part A, Part B, S110 to S115 file, the decisions record, the S61 terms file or `authority/` is written.
5. **The owner's words bind every finding as content.** An objection that would settle for the owner something left open (what knowledge is; how "causes itself" is read; S111's open question on resisting change; S112's two readings; which execution environment to pursue; which of S115's batches 4 to 9 to run) is recorded, not applied (S28, S21). No finding ranks anything (S20).
6. **Records** follow the settlement, by the same agent: an addition to log S116 in the project story and the plain story, and Status, INDEX and README as earlier entries did.

## How the run is launched

From the repository root, after this file's commit is pushed and the build and dry test are committed, one process, detached so that it outlives the agent that starts it, with the key loaded only into its own environment from the session's key file and never opened, printed or copied by the agent, and the other keys unset:

```
setsid nohup bash -c 'cd /home/user/ThreadSmith || exit 1; echo "launched $(date -u +%Y-%m-%dT%H:%M:%SZ)"; R="Semantics/results/S116 Routine runs from Astra'"'"'s replies - how the GLM cross-examination will be read, written before sending.md"; { git ls-files --error-unmatch -- "$R" >/dev/null && git diff --quiet HEAD -- "$R"; } || { echo "the reading rule is not committed or differs from HEAD; nothing sent"; exit 1; }; set -a; . <key file>; set +a; unset ATRIA_API_KEY MIMO_API_KEY OPENAI_API_KEY; python3 -B Semantics/tools/s116x_glm_loop.py "Semantics/tools/s116x_jobs - S116, GLM cross-examination.json"; echo "loop ended $(date -u +%Y-%m-%dT%H:%M:%SZ)"' > <scratchpad>/s116x_glm_run.log 2>&1 < /dev/null &
```

The process id of the session leader goes in `<scratchpad>/s116x_glm_run.pid`. The launching agent writes `results/S116 Routine runs from Astra's replies - GLM cross-examination, launch record.md`, commits it, pushes, and hands back once the log shows all four calls sent.

## Unsure

- GLM cannot run Avida or see the raw output (the probe results, the saved program populations, the competition's saves); it judges the numbers by their consistency with the scripts, the configuration and each other. A claim it cannot check is to be listed as not reached, not as an objection.
- The reply scripts are long (reply 01's probe about 300 lines); a fault there that S115's check and this job both missed could pass.
- One GLM job per angle may miss what the work also missed.

Decided by Claude under decisions S17, S29, S39, S56, S61 and S68. 30 September 2026.
