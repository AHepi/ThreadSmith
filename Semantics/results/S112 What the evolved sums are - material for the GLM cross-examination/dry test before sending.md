# S112 What the evolved sums are: the dry test of the GLM sandboxes, before sending

*Log S112, 30 September 2026, by the one Opus 5.5 agent of log S112. Run with `sandbox check.py` in this folder, after the build (`tools/s112x_build.py`, d4a1481) and before anything was sent. The real key was never used, opened or read; a dummy stood in for it.*

For each of the four jobs, the helper's own `build_sandbox` built the sandbox from the job's manifest and brief:

| job | tag | files in the sandbox (with BRIEF.md) | manifest and brief md5 as the job list gives | links | key-like paths | sources from outside Semantics/ | Avida binaries, `.spop`, `.dat`, `.trace` or `.jsonl` files, files over 400,000 bytes | a `model/` folder |
|---|---|---|---|---|---|---|---|---|
| 1 | s112x_glm_a | 20 | yes | 0 | none | none | none | no |
| 2 | s112x_glm_b | 18 | yes | 0 | none | none | none | no |
| 3 | s112x_glm_c | 18 | yes | 0 | none | none | none | no |
| 4 | s112x_glm_d | 20 | yes | 0 | none | none | none | no |

The shell guard (`tools/glm_sandbox_shell_guard.py`, unchanged) was handed nine command lines per sandbox, in the form Claude Code builds: `echo probe > probe.txt`, `touch probe.txt`, `python3 -c 'print(1)'`, `python3 -c "open('p','w')"`, `cat BRIEF.md`, `env`, `python3 scripts/s112_find_minimal_removals.py > out.txt`, `python3 scripts/s112_find_minimal_removals.py`, and `python3 -m model.run --claim FC23`. **All 36 were refused** (exit 126; the guard's log: nine "refused" per sandbox); the dummy key appeared in no output; **every sandbox came back unchanged**, with no probe file and no `__pycache__`. There is no program in any sandbox, so GLM can only Read, Glob and Grep.

The runner's dry run (`tools/s112x_glm_loop.py … --dry-run`) listed the four jobs, 4 GLM slots, effort medium, the 1,000,000-token window, and sent nothing. `tools/s112x_build.py --check`: all 9 built files identical to the build. S111's GLM run (session leader PID 3581) has exited; no other GLM call of this project is running.
