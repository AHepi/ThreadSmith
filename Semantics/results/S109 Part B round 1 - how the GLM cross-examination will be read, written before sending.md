# S109 Part B round 1 - how the GLM cross-examination will be read, written before sending

*Written 29 September 2026 by the one Opus 5.5 agent that, under decision S56, did the whole reading of Part B round 1 (the tabulation, the computation of sections B1 to B4, the map of how explanation changes in meaning and scope, and the candidate list), before anything of this cross-examination was sent. When this file was committed, the returns folder `results/S109 Part B round 1 - GLM cross-examination returns/` did not exist, no call had been sent, and no runner of it was going. It follows the round's rule (`results/S109 Part B round 1 - how the replies will be read, written before sending.md`, rule 8) and, where that says nothing else, Part A round 2's cross-examination rule (`results/S108 Part A round 2 - how the GLM cross-examination will be read, written before sending.md`). It obeys decision S23 except where it quotes the owner. For what the theory judges it says "candidate" or "explanation", never "model" (S43).*

## The instruction

- **S56**, the owner's words: "It's capable of doing the whole thing on its own. Use GLM for cross examination. No need to Opus to do single sections". One Opus agent did rules 4 to 7 of the round's rule; **GLM cross-examines that work** (rule 8, in place of a fresh Opus critical reviewer).
- **S55**: Sonnet 5.5 for routine jobs only. The whole-suite runs (32, one per variant and reading) were made by the Opus agent itself by script (`tools/sonnet_harness/run_claims.py` through `computation/whole suite/run_queue.py`), as cheaper than a Sonnet agent.
- **S39, S29, S17**: up to four GLM calls at once, each through Claude Code, at medium effort. **S52**: Part B, then Part C, then stop. **S20 to S56**: the owner's words bind every finding as content.

## What is sent

Four jobs, built by `tools/s109x_build.py` on the pattern of Part A round 2's cross-examination build (`tools/s108r2x_build.py`; Part A round 1's build `tools/s108_build.py` imported for its checks and the owner's words, never changed; the sandboxed helper `tools/glm_via_claude_code_sandboxed.py` and the shell guard `tools/glm_sandbox_shell_guard.py` used unchanged), run by `tools/s109x_glm_loop.py` (Part A round 2's cross-examination runner with its names changed; each job names its own sandbox manifest). Each job cross-examines the round's work from one angle:

| job | tag | angle | the program at the sandbox's root |
|---|---|---|---|
| 1 | `s109x_glm_a` | (a) the tabulation and computation of sections B1 and B2 | section B2's copy (B1's copy to read) |
| 2 | `s109x_glm_b` | (b) the tabulation and computation of sections B3 and B4 | section B3's copy (B4's copy to read) |
| 3 | `s109x_glm_c` | (c) the map of how explanation changes in meaning and scope | the program after round 4 |
| 4 | `s109x_glm_d` | (d) the candidate list against the owner's decisions S20 to S56 and against Part A's list | the program after round 4 |

Each sandbox holds copies only: the text, formal core and claims after round 4; the round's rule, this rule, the free set and frozen template, the tabulation, the four "variants computed" files and their `.json`, the map (`.md`), the candidate list, the four replies; Part A's map, candidate list and settled cross-examination; and, per job, the program copies, patches, scripts, runs and whole-suite results of its sections, the map's builder and `.json`, or the decisions record. GLM may Read, Glob and Grep and run only `python3 -m model.run …` (claim ids, `--scale` at most 4, `--time-cap` at most 60) with `--no-write` and a clean environment, so every reading switch (`S109B_VARIANT` and its readings) is off in its runs; it writes nothing and runs no code of its own. Each brief asks for objections, each with **the exact fix**, terse, with a last line `END OF REPORT`. The briefs, manifests and job list are named, with their md5s, in `tools/s109x_jobs - Part B round 1, GLM cross-examination.json`, written by the build before the launch and committed with it.

- **The call**: glm-5.3 through Claude Code (S29), `--effort medium` (S17), the 1,000,000-token window, 6 attempts, at most 3 answers without END OF REPORT, 7,200 seconds per attempt, `--rule` (this file, committed and unchanged from HEAD), `--brief-md5`, `--manifest-md5`. Up to 3 passes per job. Sandboxes in `<scratchpad>/s109x_sandboxes/`, homes in `<scratchpad>/s109x_homes/`. Returns in `results/S109 Part B round 1 - GLM cross-examination returns/`.
- **The dry test, before sending**: for each job a sandbox built from its manifest by the helper's own `build_sandbox`, with a dummy key (the real one never used); the guard runs one `python3 -m model.run --claim …` and refuses a write (`echo probe > probe.txt`, `touch`), `python3 -c`, `cat`, `env` and a redirect; the dummy key in no output; each sandbox unchanged. Recorded in `results/S109 Part B round 1 - material for the GLM cross-examination/sandbox check - output.txt`.

## How the replies will be read

1. **Nothing is opened until all four calls end.** No reply, receipt, reasoning file, attempt file, stream file or guard log of this cross-examination is opened until every job has ended its last allowed pass: the run log holds `s109x_glm_loop: every pass ended; …` and `loop ended <UTC time>`, and the process in the pid file has exited. The progress lines may be watched; they hold no reply text. If a call is still running 24 hours after the launch, the runner may be stopped by its exact PID and the calls not ended recorded as not returned.
2. **What counts as a reply**: only `<tag>.response.txt` (or `<tag>_pass<k>.response.txt`); failed calls count neither way; connection failures are not answers; a key in the output or a sandbox not unchanged is reported before anything else is read.
3. **One Opus 5.5 agent (effort high) reads every objection and settles each**, by argument (from the text, the formal core, the owner's words, the files) or by a run (in the Part B copies, with the switch the objection names, under `timeout`), and records for each: the objection, its settlement (stands, stands in part, does not stand), the reason or the run, and what it changes. An objection is a claim until settled; a point repeated by several jobs decides nothing (arguments, not numbers); silence is not agreement. It writes `results/S109 Part B round 1 - the GLM cross-examination, settled.md`, created at once and filled as it goes.
4. **Findings that stand amend the map and the list in corrected copies** (`… how explanation changes in meaning and scope, after the cross-examination.md` / `.json`, `… candidate definitions of explanation, after the cross-examination.md`), each amendment marked with its objection's id; the versions sent are kept as they were. Nothing in the theory's text, formal core, claims or program after round 4, no Part A file, no decision and nothing in `authority/` is written (rule 13 of the round's rule).
5. **Round 2 of Part B, or Part C, by rule 10.** After the settlement the agent decides, by rule 10 of the round's rule, whether a gap remains that bears on the explanation definition and that another round of Part B could reach (a free item upstream of (E), Dec, Expl, (Suff) or (Nec) neither varied nor recorded with why no variant inside the rule can reach it; a class-a carry-over not computed; an edge on the definition's parts left claimed only that a variant could settle). If one does, a round 2 of Part B follows, under its own rule, written and committed before sending. If none does, Part B ends and **Part C** follows (rule 11): the flagged candidates of Parts A and B put to the owner as yes-or-no questions in plain words; then stop (S52). The readings the owner's own cases turn on are not gaps: they are the owner's.
6. **The owner's words bind every finding as content** (S20 to S56). An objection that would settle for the owner a reading the owner's cases turn on (the change as an edit or a boundary; D6.3's quantifier; Θ's reading of a bare edit; a question's recorded history; which history the bridge has; whether the textbook's carrier lies inside the student's boundary) is recorded, not applied.
7. **Records and a plain-words file** (S48), by the same agent: the story log S109, the status, the index; and `plain words/109 Part B round 1 - what the variations found, in plain words.md`, saying "candidate" or "explanation", never "model" (S43), the owner's S44 case being the two-part sign.

## How the run is launched

From the repository root, after this file's commit is pushed, one process, detached so that it outlives the agent that starts it, with the key loaded only into its own environment from the session's key file and never printed, and the other keys unset:

```
setsid nohup bash -c 'cd /home/user/ThreadSmith || exit 1; echo "launched $(date -u +%Y-%m-%dT%H:%M:%SZ)"; R="Semantics/results/S109 Part B round 1 - how the GLM cross-examination will be read, written before sending.md"; { git ls-files --error-unmatch -- "$R" >/dev/null && git diff --quiet HEAD -- "$R"; } || { echo "the reading rule is not committed or differs from HEAD; nothing sent"; exit 1; }; set -a; . <key file>; set +a; unset ATRIA_API_KEY MIMO_API_KEY OPENAI_API_KEY; python3 -B Semantics/tools/s109x_glm_loop.py "Semantics/tools/s109x_jobs - Part B round 1, GLM cross-examination.json"; echo "loop ended $(date -u +%Y-%m-%dT%H:%M:%SZ)"' > <scratchpad>/s109x_glm_run.log 2>&1 < /dev/null &
```

The process id of the session leader (the `bash -c` that `setsid` starts, not `setsid`'s own) goes in `<scratchpad>/s109x_glm_run.pid`. The launching agent writes `results/S109 Part B round 1 - GLM cross-examination, launch record.md` and hands back once the log shows all four calls sent.

## Unsure

- The guard passes a clean environment, so GLM cannot run a copy with a variant switched on; its runs check "off" values and the claims' printouts. Where an objection needs a run with a switch, it names the run, and the settling agent makes it (rule 3).
- One GLM job per angle reads the computation; it is not a second computation.
- The whole-suite runs were made once per setting, without a second run by a verifier.
- The map and the list were written by the same agent that computed; the cross-examination is the first reading by anyone else.

Decided by Claude under decisions S13, S17, S39, S52, S55 and S56. 29 September 2026.
