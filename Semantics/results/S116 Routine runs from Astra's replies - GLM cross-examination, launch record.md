# S116 Routine runs from Astra's replies: GLM cross-examination, launch record

*Written 30 September 2026 by the one Opus 5.5 agent of log S116 (decisions S56, S61, S68), in the owner's Avida terms. Nothing of the replies has been opened; the progress lines of the run log hold no reply text.*

## Before sending

- The reading rule, `results/S116 Routine runs from Astra's replies - how the GLM cross-examination will be read, written before sending.md`, committed before anything was built or sent (1f41d20), pushed, and unchanged since.
- The plan (732cf7f), the results `results/S116 Routine runs from Astra's replies - results.md` and `.json` (38b41e5), and `plain words/116 What the routine runs from Astra's replies found, in plain words.md` (36789ba), as sent.
- The build, the runner and the dry-test script: `tools/s116x_build.py` (log S113's build with its names, files and briefs changed; round 1's build imported for its helpers only), `tools/s116x_glm_loop.py` (log S113's runner with its names changed; the body identical apart from names), `results/S116 Routine runs from Astra's replies - material for the GLM cross-examination/sandbox check.py`; the helper `tools/glm_via_claude_code_sandboxed.py` and the guard `tools/glm_sandbox_shell_guard.py` unchanged.
- Built and committed before sending (509863e): four briefs in `tests/S116 - GLM cross-examination, job 1..4, …`, four sandbox manifests, the job list `tools/s116x_jobs - S116, GLM cross-examination.json`, and the dry test, `results/S116 Routine runs from Astra's replies - material for the GLM cross-examination/dry test before sending.md`. Pushed.

| job | tag | angle | brief md5 | sandbox files |
|---|---|---|---|---|
| 1 | s116x_glm_a | whether the runs answer what the plan says they test, and whether the comparisons with S113 are fair | 8c21f40e710925d33c792fd11c45cf55 | 32 + BRIEF.md |
| 2 | s116x_glm_b | the measures and the scripts | 48715b6c3e3b41cbf707f0244c5f5b29 | 31 + BRIEF.md |
| 3 | s116x_glm_c | the results against the plan | 58d215a72298ad7dc34bbd20143642a4 | 31 + BRIEF.md |
| 4 | s116x_glm_d | the plain-words file against the results | 900a2d4e298130b9169110796a497e89 | 33 + BRIEF.md |

## The dry test

Every sandbox built by the helper's `build_sandbox` with a dummy key: md5s match the job list; no link, no key-like path, no source from outside `Semantics/`, no Avida binary, no `.spop`, `.dat`, `.trace`, `.jsonl` or `.tsv` file, no file over 400,000 bytes, no `model/` folder. The guard refused all nine command lines in each sandbox (36 of 36); every sandbox came back unchanged. The runner's dry run sent nothing; `tools/s116x_build.py --check`: all 9 files identical to the build.

## The launch

- No other GLM call of this project was running (no `glm_loop` or `glm_via_claude` process on the machine).
- Launched 2026-09-30T18:35:44Z, detached (`setsid nohup bash -c …` as the rule sets out), after the check that the rule is committed and equal to HEAD; the key loaded only into the process's environment from the session's key file, never opened, printed or copied; the other keys unset.
- Session leader PID **2881**, in `<scratchpad>/s116x_glm_run.pid` (the `$!` of the launching shell was 2879, `setsid`'s own parent, which exited at once); the runner is PID 2902; log `<scratchpad>/s116x_glm_run.log`.
- glm-5.3 with the 1,000,000-token window, through Claude Code 2.1.285, effort medium, four at once; all four calls logged "attempt 1: sent" at 18:35:45Z.
- Returns go to `results/S116 Routine runs from Astra's replies - GLM cross-examination returns/`, which is not opened until the log holds `every pass ended` and `loop ended`, and PID 2881 has exited.

## Unsure

- The briefs quote the owner's decisions S20, S21, S23, S28, S43, S56, S61, S62, S63, S64, S66 and S68.
- GLM sees none of the raw output (probe results, saved program populations, the competition's saves); it judges the numbers by their agreement with the scripts and each other. The input-order finding of the results was made by Claude after the first results; GLM cannot rerun anything to test it.
