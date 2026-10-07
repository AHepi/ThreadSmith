# S110 - GLM cross-examination, launch record

*Written 29 September 2026 by the second Opus 5.5 agent, which finished the setup after a system outage stopped the first agent before anything was sent (decision S56; decisions S57, S58). Nothing of the replies has been opened; the progress lines of the run log hold no reply text.*

## What the first agent left, and what was finished

- Left at 15f5b4e: the reading rule, `tools/s110x_build.py`, `tools/s110x_glm_loop.py` (Part A round 2's cross-examination runner with its names changed), and `sandbox check.py`. Nothing built, nothing sent.
- Checked: the rule's four jobs, briefs, sandbox contents and reading steps (nothing opened until all calls end; one Opus agent settles each objection by argument, amends the S110 files in corrected copies, updates plain file 110) match the build and the runner.
- Corrected: job 3's sandbox lacked two records that the change map's "recorded" edges cite: the S96 record (e110, e125) and the note `tests/Revision 2 - hard to vary restated through rivals and problems, 25 September.md` (e119, e123). Both added to the build and to the rule, and the rule records that a second agent finished the setup. Commit 3a9f35d (rule and build).
- Built, dry-tested and committed before sending: commit 42ef7a4 (four briefs in `tests/S110 - GLM cross-examination, job 1..4, …`, four sandbox manifests, the job list `tools/s110x_jobs - S110, GLM cross-examination.json`, and `results/S110 - material for the GLM cross-examination/dry test before sending.md`). Both commits pushed.

| job | tag | angle | brief md5 | sandbox files |
|---|---|---|---|---|
| 1 | s110x_glm_a | the change map against FW0 and I2 | 2ec8f2a83681bc4083a8afdf9d2aa6e1 | 14 + BRIEF.md |
| 2 | s110x_glm_b | the change map against FW2, FW3 and FW4 | faaaa9140a6600405c5bc1b73e0a608f | 14 + BRIEF.md |
| 3 | s110x_glm_c | the change map against FW5, the present theory and the S89 audit | 7511f2a2b4a23ed248b35c196c151472 | 20 + BRIEF.md |
| 4 | s110x_glm_d | files 1 and 3: consistency, readings passed off as the book's, the owner's decisions | e26cf9410abc0132ab446b149b6d663b | 15 + BRIEF.md |

## The dry test

Every sandbox built by the helper's `build_sandbox` with a dummy key: md5s match; the guard refused all eight commands in each (a write, `touch`, two `python3 -c`, `cat`, `env`, a redirect, the program command; there is no program in the sandbox); every sandbox came back unchanged; no key-named file and no key-shaped content. A search of every sandbox file against all 8-word runs of both books' extracted text found no book file; the longest run of the books' words is 26, in file 3, where a checked 22-word quotation of Marletto ch. 5 is preceded outside the quotation marks by the book's words "of information is that". That is one word over S19's 25; recorded for the reading agent, and the file sent as committed.

## The launch

- Launched 2026-09-29T10:00:31Z, detached (`setsid nohup bash -c …` as the rule sets out), after the check that the rule is committed and equal to HEAD; the key loaded only into the process's environment from the session's key file, never opened or printed; the other keys unset.
- Session leader PID **6632**, in `<scratchpad>/s110x_glm_run.pid`; log `<scratchpad>/s110x_glm_run.log`.
- glm-5.3 with the 1,000,000-token window, through Claude Code 2.1.284, effort medium, four at once; all four calls logged "attempt 1: sent" at 10:00:31Z.
- Part B's GLM run (PID 5784) had ended (`loop ended 2026-09-29T06:08:08Z`); no other GLM call was running.
- Returns go to `results/S110 - GLM cross-examination returns/`, which is not opened until the log holds `every pass ended` and `loop ended`, and PID 6632 has exited.

## Unsure

- The shell guard's command format was observed with Claude Code 2.1.283; the run uses 2.1.284. The dry test used the 2.1.283 format; since the S110 sandboxes hold no program, any other format is refused as well, so GLM can still only read.
