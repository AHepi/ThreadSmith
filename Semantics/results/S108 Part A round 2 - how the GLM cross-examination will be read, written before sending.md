# S108 Part A round 2 - how the GLM cross-examination will be read, written before sending

*Written 29 September 2026 by the one Opus 5.5 agent that, under decision S56, did the whole reading of Part A's round 2 (the computation of sections 2 to 4, the dependency map and the candidate list after round 2), before anything of this cross-examination was sent. When this file was committed, the returns folder `results/S108 Part A round 2 - GLM cross-examination returns/` did not exist, no call had been sent, and no runner of it was going. It follows round 2's rule (`results/S108 Part A round 2 - how the replies will be read, written before sending.md`) where it says nothing else. It obeys decision S23 except where it quotes the owner. For what the theory judges it says "candidate" or "explanation", never "model" (S43).*

## The instruction

- **S56**, the owner's words: "I see. You're using Opus 5.5 on Xhigh. That's a waste of tokens. It's capable of doing the whole thing on its own. Use GLM for cross examination. No need to Opus to do single sections". So one Opus agent did the whole job of round 2's reading, and **GLM cross-examines it in place of rule 8's fresh Opus critical reviewer** (and of rule 9's second checker, which reviewed a reviewer). Rules 5, 6 and 7 of round 2's rule were done by that one agent (recorded in the map's §0).
- **S55**: Sonnet 5.5 for routine jobs only. The whole-suite runs of round 2, which the round's rule gave to Sonnet harness workers, were run by the Opus agent itself by script (`tools/sonnet_harness/run_claims.py`), as cheaper than a Sonnet agent: recorded in the map's §0.
- **S39, S29, S17**: up to four GLM calls at once, each through Claude Code, at medium effort. **S52**: the review is of Part A; Part B follows it. **S20 to S56**: the owner's words bind every finding as content.
- **The restart.** The Opus agent first given this job was cut off by a session restart at about 00:24 UTC on 29 September 2026; its partial work (committed in f601771) was continued, not redone, by the agent that writes this rule (the map's §0 says what was continued and how).

## What is sent

Four jobs, built by `tools/s108r2x_build.py` on the pattern of round 2's build (round 1's build imported for its checks and the owner's words; the sandboxed helper `tools/glm_via_claude_code_sandboxed.py` and the shell guard `tools/glm_sandbox_shell_guard.py` used unchanged), run by `tools/s108r2x_glm_loop.py` (round 2's runner with its names changed and one change: each job names its own sandbox manifest, because each sandbox holds a different program copy at its root). Each job cross-examines the round-2 work from one angle:

| job | tag | angle | the program at the sandbox's root |
|---|---|---|---|
| 1 | `s108r2x_glm_a` | the computations of sections 1 and 2 | section 2's round-2 copy (section 1's copy to read) |
| 2 | `s108r2x_glm_b` | the computations of sections 3 and 4 | section 3's round-2 copy (section 4's copy to read) |
| 3 | `s108r2x_glm_c` | the dependency map's edges and gaps | the program after round 4 |
| 4 | `s108r2x_glm_d` | the candidate list against the owner's decisions S20 to S56 | the program after round 4 |

Each sandbox holds copies only: the text, formal core, claims, frozen template and set after round 4 (round 1's material); round 2's rule, the record of who computes, this rule, the tabulation, the four "variants computed" files and their `.json`, the map and the list after round 2, the four round-2 replies; round 1's corrected map and list and the review of the Sonnet 5.5 trial; and, per job, the program copies, runs and whole-suite results of its sections, the map's builder and `.json`, or the decisions record. GLM may Read, Glob and Grep and run only `python3 -m model.run …` (claim ids, `--scale` at most 4, `--time-cap` at most 60) with `--no-write` and a clean environment, so every reading switch of a copy is off in its runs; it writes nothing. Each brief asks for objections, each with **the exact fix**, terse, with a last line `END OF REPORT`. The briefs, manifests and job list are named, with their md5s, in the job list `tools/s108r2x_jobs - Part A round 2, GLM cross-examination.json`, written by the build before the launch and committed with it.

- **The call**: glm-5.3 through Claude Code (S29), `--effort medium` (S17), the 1,000,000-token window, 6 attempts, at most 3 answers without END OF REPORT, 7,200 seconds per attempt, `--rule` (this file, committed and unchanged from HEAD), `--brief-md5`, `--manifest-md5`. Up to 3 passes per job. Sandboxes in `<scratchpad>/s108r2x_sandboxes/`, homes in `<scratchpad>/s108r2x_homes/`. Returns in `results/S108 Part A round 2 - GLM cross-examination returns/`.

## How the replies will be read

1. **Nothing is opened until all four calls end.** No reply, receipt, reasoning file, attempt file, stream file or guard log of this cross-examination is opened until every job has ended its last allowed pass: the run log holds `s108r2x_glm_loop: every pass ended; …` and `loop ended <UTC time>`, and the process in the pid file has exited. The progress lines may be watched; they hold no reply text. If a call is still running 24 hours after the launch, the runner may be stopped by its PID and the calls not ended recorded as not returned.
2. **What counts as a reply**: only `<tag>.response.txt` (or `<tag>_pass<k>.response.txt`); failed calls count neither way; connection failures are not answers; a key in the output or a sandbox not unchanged is reported before anything else is read.
3. **One Opus agent reads every objection and settles each**, by argument (from the text, the formal core, the owner's words, the files) or by a run (in the round-2 copies, with the switch the objection names, under `timeout`), and records for each: the objection, its settlement (stands, stands in part, does not stand), the reason or the run, and what it changes. An objection is a claim until settled; a count repeated by several jobs decides nothing (arguments, not numbers); silence is not agreement. The agent writes `results/S108 Part A round 2 - the GLM cross-examination, settled.md`, created at once and filled as it goes.
4. **Findings that stand amend the map and the list**: each amendment is made in the after-round-2 files (or in a corrected copy, if they are to be kept as they were sent), marked, with the objection's id; nothing in the theory's text, formal core, claims or program after round 4, round 1's files or round 1's program copies is written (rule 11 of round 2's rule).
5. **A third round of Part A only if gaps that bear on the explanation definition remain** after the settled findings (items still untouched that are upstream of (E), Dec, Expl, (Suff) or (Nec), or edges on them the computation could not settle and that a variant inside Part A's rule could reach), under its own rule, written and committed before sending. Otherwise Part A ends, and **Part B** follows (S52), then the flags for the owner's yes or no.
6. **The owner's words bind every finding as content** (S20 to S56). The readings the owner's own cases turn on (the change as an edit or a boundary; D6.3's quantifier; a question's recorded history; Desc's grain) are the owner's to settle: an objection that would settle one of them for the owner is recorded, not applied.
7. **Records and a plain-words file** (S48) follow the settlement, by one Opus agent: `plain words/108 Part A round 2 - what the variations found, in plain words.md`, saying "candidate" or "explanation", never "model" (S43).

## How the run is launched

From the repository root, after this file's commit is pushed, one process, detached so that it outlives the agent that starts it, with the key loaded only into its own environment from the session's key file and never printed, and the other keys unset:

```
setsid nohup bash -c 'cd /home/user/ThreadSmith || exit 1; echo "launched $(date -u +%Y-%m-%dT%H:%M:%SZ)"; R="Semantics/results/S108 Part A round 2 - how the GLM cross-examination will be read, written before sending.md"; { git ls-files --error-unmatch -- "$R" >/dev/null && git diff --quiet HEAD -- "$R"; } || { echo "the reading rule is not committed or differs from HEAD; nothing sent"; exit 1; }; set -a; . <key file>; set +a; unset ATRIA_API_KEY MIMO_API_KEY OPENAI_API_KEY; python3 -B Semantics/tools/s108r2x_glm_loop.py "Semantics/tools/s108r2x_jobs - Part A round 2, GLM cross-examination.json"; echo "loop ended $(date -u +%Y-%m-%dT%H:%M:%SZ)"' > <scratchpad>/s108r2x_glm_run.log 2>&1 < /dev/null &
```

The process id of the session leader goes in `<scratchpad>/s108r2x_glm_run.pid`. The launching agent hands back once the log shows all four calls sent.

## Unsure

- The guard passes a clean environment, so GLM cannot run a copy with a variant switched on; its runs check "off" values and the claims' printouts. Where an objection needs a run with a switch, it names the run, and the reading agent makes it (rule 3 above).
- One GLM job per angle is not a second computation: it reads the computation, and may rerun what the guard allows.
- The whole-suite runs were made once per setting by the Opus agent's script, without a second run by a verifier; the cross-examination of sections 1 to 4 may weigh that.

Decided by Claude under decisions S13, S17, S39, S52, S55 and S56. 29 September 2026.
