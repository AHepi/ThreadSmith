# S112 What the evolved sums are: GLM cross-examination, launch record

*Written 30 September 2026 by the one Opus 5.5 agent of log S112 (decisions S56, S60, S61), in the owner's Avida terms. Nothing of the replies has been opened; the progress lines of the run log hold no reply text.*

## Before sending

- The reading rule, `results/S112 What the evolved sums are - how the GLM cross-examination will be read, written before sending.md`, committed before anything was built or sent (bb63fb2) and pushed; unchanged since.
- The results and the plain file, as sent: `results/S112 What the evolved sums are - what had to be removed and what it is.md` and `.json` (f4e2f37), `plain words/112 What the evolved sums actually are, in plain words.md` (8031e5e).
- The build, the runner and the dry-test script: `tools/s112x_build.py` (log S111's build with its names, files and briefs changed; round 1's build imported for its helpers only), `tools/s112x_glm_loop.py` (log S111's runner with its names changed), `results/S112 What the evolved sums are - material for the GLM cross-examination/sandbox check.py` (9c0b0aa); the helper `tools/glm_via_claude_code_sandboxed.py` and the guard `tools/glm_sandbox_shell_guard.py` unchanged.
- Built and committed before sending: d4a1481 (four briefs in `tests/S112 - GLM cross-examination, job 1..4, …`, four sandbox manifests, the job list `tools/s112x_jobs - S112, GLM cross-examination.json`); dry test 7dc85bc (`results/S112 What the evolved sums are - material for the GLM cross-examination/dry test before sending.md`). Pushed.

| job | tag | angle | brief md5 | sandbox files |
|---|---|---|---|---|
| 1 | s112x_glm_a | whether the answer answers the owner's two questions exactly | e848d5d631ffb6e905a7cbb28ac891c3 | 19 + BRIEF.md |
| 2 | s112x_glm_b | the minimal-removal search (instruction ablation) and its limits | 573858be2002b5e41a7afe86656162f4 | 17 + BRIEF.md |
| 3 | s112x_glm_c | the circuits and their canonical forms against the traces | aa704a8d0503ea738d263f84eb832487 | 17 + BRIEF.md |
| 4 | s112x_glm_d | the plain-words file against the results | c757274dfe6aaf0867661c6d07e7176d | 19 + BRIEF.md |

## The dry test

Every sandbox built by the helper's `build_sandbox` with a dummy key: md5s match the job list; no link, no key-like path, no source from outside `Semantics/`, no Avida binary, no `.spop`, `.dat`, `.trace` or `.jsonl` file, no file over 400,000 bytes, no `model/` folder. The guard refused all nine command lines in each sandbox; every sandbox came back unchanged. The runner's dry run sent nothing; `tools/s112x_build.py --check`: all 9 files identical to the build.

## The launch

- S111's GLM run (PID 3581) had exited; no other GLM call of this project was running.
- Launched 2026-09-30T03:30:54Z, detached (`setsid nohup bash -c …` as the rule sets out), after the check that the rule is committed and equal to HEAD; the key loaded only into the process's environment from the session's key file, never opened or printed; the other keys unset.
- Session leader PID **23023**, in `<scratchpad>/s112x_glm_run.pid` (the `$!` of the launching shell was 23021, `setsid`'s own parent, which exited at once; the pid file was corrected to the leader, 23023, within a minute); log `<scratchpad>/s112x_glm_run.log`.
- glm-5.3 with the 1,000,000-token window, through Claude Code 2.1.285, effort medium, four at once; all four calls logged "attempt 1: sent" at 03:30:54Z.
- Returns go to `results/S112 What the evolved sums are - GLM cross-examination returns/`, which is not opened until the log holds `every pass ended` and `loop ended`, and PID 23023 has exited.

## Unsure

- The briefs quote the owner's decisions S20, S21, S23, S28, S43, S56, S60 and S61.
- GLM sees Avida's rules only as S111's build notes and the S112 scripts' citations give them, and none of the raw output; it judges the numbers by their agreement with the scripts, the worked examples and each other.
