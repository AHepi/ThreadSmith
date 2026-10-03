# S109 Part B round 1 - launch record

*Written 29 September 2026 by the one Opus 5.5 agent of decision S56 that built and launched Part B round 1, after the launch. No reply, receipt or stream file of the round has been opened (its rule, rule 1). Kept apart from the files the sandboxes copy, whose md5s the runner checks at every attempt.*

| item | value |
|---|---|
| rule, committed and pushed before sending | `S109 Part B round 1 - how the replies will be read, written before sending.md` (commit c28d832) |
| free set and frozen template, build, runner, briefs, manifest, job list, dry test | commit 1bcd127; `tools/s109_build.py --check`: all 8 files identical to the build, rerun after the rule's commit; the runner's dry run after it: nothing uncommitted |
| the four sections | B1 organizations, kinds, questions and contracts (57: 41 sentences + 16 definitions); B2 transports, fidelity, the account, routes and the exact constructions (57: 37 + 20); B3 provenance, histories, representation, construction, repair and the physical module (57: 37 + 20); B4 rivals, problems, criticism, the class, what would rule it out, and the Arguments (67: 54 + 13) |
| dry test (before launch) | each of the four sandboxes built by the helper's own `build_sandbox` with a dummy key: 55 files, no link, no key-shaped path, `BRIEF.md` at the job list's md5; the guard ran FC23.new2, FC84.new1, FC22, FC14 in job 1's (all hold) and refused, in all four, a write (`echo … > probe.txt`, `touch`, a redirect of a program run), `python3 -c` (twice), `cat BRIEF.md` and `env`; each sandbox unchanged, no `__pycache__`; output `S109 Part B round 1 - material for the readers/sandbox check - output.txt` |
| launched | 2026-09-29T03:23:53Z, detached (`setsid nohup`), the key loaded only inside the launch command from the session's key file (the other keys unset); never opened or printed |
| calls sent | all four at 03:23:53Z, pass 1, attempt 1: `s109_glm_section1` to `s109_glm_section4`, glm-5.3 through Claude Code 2.1.283, effort medium, 1M window, 55 sandbox files each |
| session leader | PID 1524 (the `bash -c` that `setsid` started, which echoed its own PID into the log; `$!` gave 1523, setsid's own); the runner python3 is PID 1543 |
| log, pid | `<scratchpad>/s109_glm_run.log`, `<scratchpad>/s109_glm_run.pid` (1524) |
| returns | `S109 Part B round 1 - returns/` (written by the helper; not committed while the run goes, and not opened) |

Next, under the rule: nothing opened until the log shows `every pass ended` and `loop ended`, and PID 1524 has exited; then one Opus 5.5 agent (effort high) does the whole reading (rules 4 to 7: tabulation; computation of every section in program copies, for meaning and scope; the map of how explanation changes; the candidate list); then the GLM cross-examination under its own rule; then one Opus agent settles it and writes the records and the plain-words file; then Part B ends, or a round 2 under its own rule (rule 10); then Part C, the owner's yes or no on the flags, and stop (rule 11).
