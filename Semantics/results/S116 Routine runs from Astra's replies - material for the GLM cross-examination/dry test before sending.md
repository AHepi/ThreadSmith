# S116 Routine runs from Astra's replies: dry test of the four GLM sandboxes, before sending

*Written 30 September 2026 by the one Opus 5.5 agent of log S116, after the build and before anything was sent. Run: `python3 -B "Semantics/results/S116 Routine runs from Astra's replies - material for the GLM cross-examination/sandbox check.py" "tools/s116x_jobs - S116, GLM cross-examination.json"` (log S113's check with its names changed, and `.tsv` files added to the raw output looked for). A dummy key only; the real key was not used, opened or read.*

- Every sandbox built by the helper's own `build_sandbox`: manifest and brief md5s equal to the job list's, and the brief in the sandbox equal too; 33, 32, 32 and 34 files (with BRIEF.md); no link, no key-like path, no source from outside `Semantics/`, no Avida binary, no `.spop`, `.dat`, `.trace`, `.jsonl` or `.tsv` file, no file over 400,000 bytes, no `model/` folder.
- The guard refused all nine command lines in each sandbox (36 of 36, exit 126): a write, `touch`, two `python3 -c`, `cat`, `env`, a redirect, a run of `scripts/s116_gather_the_results.py`, and the program command of earlier rounds. The dummy key appeared in no output.
- Every sandbox came back unchanged. (The check's "probe files" line lists files whose names contain "probe": here the three probe scripts copied in by the manifest, not files made by the refused commands.)
- `tools/s116x_build.py --check`: all 9 files identical to the build. The runner's dry run sent nothing (round 1 only, four jobs listed).
- No other GLM run of this project was going.

The check's full output follows.

```
job 1 manifest md5: 36cfcab2eb3f73e30682dd443cdf6ddb job list gives 36cfcab2eb3f73e30682dd443cdf6ddb
job 1 (s116x_glm_a): brief md5 8c21f40e710925d33c792fd11c45cf55, job list 8c21f40e710925d33c792fd11c45cf55, in sandbox 8c21f40e710925d33c792fd11c45cf55; files 33, links 0, key-like paths none; sources from outside Semantics/ none; binaries, raw output or large files none; a model/ folder False
   --- echo probe > probe.txt -> exit 126 | refused by the sandbox: here only `python3 -m model.run` runs, with --claim FCnn (repeatable), --scale N (at most 4), -- | dummy token in output: False
   --- touch probe.txt -> exit 126 | refused by the sandbox: here only `python3 -m model.run` runs, with --claim FCnn (repeatable), --scale N (at most 4), -- | dummy token in output: False
   --- python3 -c 'print(1)' -> exit 126 | refused by the sandbox: here only `python3 -m model.run` runs, with --claim FCnn (repeatable), --scale N (at most 4), -- | dummy token in output: False
   --- python3 -c "open('p','w')" -> exit 126 | refused by the sandbox: here only `python3 -m model.run` runs, with --claim FCnn (repeatable), --scale N (at most 4), -- | dummy token in output: False
   --- cat BRIEF.md -> exit 126 | refused by the sandbox: here only `python3 -m model.run` runs, with --claim FCnn (repeatable), --scale N (at most 4), -- | dummy token in output: False
   --- env -> exit 126 | refused by the sandbox: here only `python3 -m model.run` runs, with --claim FCnn (repeatable), --scale N (at most 4), -- | dummy token in output: False
   --- python3 scripts/s116_gather_the_results.py > out.txt -> exit 126 | refused by the sandbox: here only `python3 -m model.run` runs, with --claim FCnn (repeatable), --scale N (at most 4), -- | dummy token in output: False
   --- python3 scripts/s116_gather_the_results.py -> exit 126 | refused by the sandbox: here only `python3 -m model.run` runs, with --claim FCnn (repeatable), --scale N (at most 4), -- | dummy token in output: False
   --- python3 -m model.run --claim FC23 -> exit 126 | refused by the sandbox: here only `python3 -m model.run` runs, with --claim FCnn (repeatable), --scale N (at most 4), -- | dummy token in output: False
   sandbox unchanged: True ; __pycache__: False ; probe files: ['scripts/s116_probe_the_saved_program_populations.py', 'scripts/reply 01, summarize_probes.py', 'scripts/reply 01, probe_task_audit.py']
   guard log: ['refused', 'refused', 'refused', 'refused', 'refused', 'refused', 'refused', 'refused', 'refused']
job 2 manifest md5: 6c77854f76d4d6c19271e7d06e1d0d97 job list gives 6c77854f76d4d6c19271e7d06e1d0d97
job 2 (s116x_glm_b): brief md5 48715b6c3e3b41cbf707f0244c5f5b29, job list 48715b6c3e3b41cbf707f0244c5f5b29, in sandbox 48715b6c3e3b41cbf707f0244c5f5b29; files 32, links 0, key-like paths none; sources from outside Semantics/ none; binaries, raw output or large files none; a model/ folder False
   --- echo probe > probe.txt -> exit 126 | refused by the sandbox: here only `python3 -m model.run` runs, with --claim FCnn (repeatable), --scale N (at most 4), -- | dummy token in output: False
   --- touch probe.txt -> exit 126 | refused by the sandbox: here only `python3 -m model.run` runs, with --claim FCnn (repeatable), --scale N (at most 4), -- | dummy token in output: False
   --- python3 -c 'print(1)' -> exit 126 | refused by the sandbox: here only `python3 -m model.run` runs, with --claim FCnn (repeatable), --scale N (at most 4), -- | dummy token in output: False
   --- python3 -c "open('p','w')" -> exit 126 | refused by the sandbox: here only `python3 -m model.run` runs, with --claim FCnn (repeatable), --scale N (at most 4), -- | dummy token in output: False
   --- cat BRIEF.md -> exit 126 | refused by the sandbox: here only `python3 -m model.run` runs, with --claim FCnn (repeatable), --scale N (at most 4), -- | dummy token in output: False
   --- env -> exit 126 | refused by the sandbox: here only `python3 -m model.run` runs, with --claim FCnn (repeatable), --scale N (at most 4), -- | dummy token in output: False
   --- python3 scripts/s116_gather_the_results.py > out.txt -> exit 126 | refused by the sandbox: here only `python3 -m model.run` runs, with --claim FCnn (repeatable), --scale N (at most 4), -- | dummy token in output: False
   --- python3 scripts/s116_gather_the_results.py -> exit 126 | refused by the sandbox: here only `python3 -m model.run` runs, with --claim FCnn (repeatable), --scale N (at most 4), -- | dummy token in output: False
   --- python3 -m model.run --claim FC23 -> exit 126 | refused by the sandbox: here only `python3 -m model.run` runs, with --claim FCnn (repeatable), --scale N (at most 4), -- | dummy token in output: False
   sandbox unchanged: True ; __pycache__: False ; probe files: ['scripts/s116_probe_the_saved_program_populations.py', 'scripts/reply 01, summarize_probes.py', 'scripts/reply 01, probe_task_audit.py']
   guard log: ['refused', 'refused', 'refused', 'refused', 'refused', 'refused', 'refused', 'refused', 'refused']
job 3 manifest md5: 6249f07b1ef399d98d54dbdfee19ad33 job list gives 6249f07b1ef399d98d54dbdfee19ad33
job 3 (s116x_glm_c): brief md5 58d215a72298ad7dc34bbd20143642a4, job list 58d215a72298ad7dc34bbd20143642a4, in sandbox 58d215a72298ad7dc34bbd20143642a4; files 32, links 0, key-like paths none; sources from outside Semantics/ none; binaries, raw output or large files none; a model/ folder False
   --- echo probe > probe.txt -> exit 126 | refused by the sandbox: here only `python3 -m model.run` runs, with --claim FCnn (repeatable), --scale N (at most 4), -- | dummy token in output: False
   --- touch probe.txt -> exit 126 | refused by the sandbox: here only `python3 -m model.run` runs, with --claim FCnn (repeatable), --scale N (at most 4), -- | dummy token in output: False
   --- python3 -c 'print(1)' -> exit 126 | refused by the sandbox: here only `python3 -m model.run` runs, with --claim FCnn (repeatable), --scale N (at most 4), -- | dummy token in output: False
   --- python3 -c "open('p','w')" -> exit 126 | refused by the sandbox: here only `python3 -m model.run` runs, with --claim FCnn (repeatable), --scale N (at most 4), -- | dummy token in output: False
   --- cat BRIEF.md -> exit 126 | refused by the sandbox: here only `python3 -m model.run` runs, with --claim FCnn (repeatable), --scale N (at most 4), -- | dummy token in output: False
   --- env -> exit 126 | refused by the sandbox: here only `python3 -m model.run` runs, with --claim FCnn (repeatable), --scale N (at most 4), -- | dummy token in output: False
   --- python3 scripts/s116_gather_the_results.py > out.txt -> exit 126 | refused by the sandbox: here only `python3 -m model.run` runs, with --claim FCnn (repeatable), --scale N (at most 4), -- | dummy token in output: False
   --- python3 scripts/s116_gather_the_results.py -> exit 126 | refused by the sandbox: here only `python3 -m model.run` runs, with --claim FCnn (repeatable), --scale N (at most 4), -- | dummy token in output: False
   --- python3 -m model.run --claim FC23 -> exit 126 | refused by the sandbox: here only `python3 -m model.run` runs, with --claim FCnn (repeatable), --scale N (at most 4), -- | dummy token in output: False
   sandbox unchanged: True ; __pycache__: False ; probe files: ['scripts/s116_probe_the_saved_program_populations.py', 'scripts/reply 01, summarize_probes.py', 'scripts/reply 01, probe_task_audit.py']
   guard log: ['refused', 'refused', 'refused', 'refused', 'refused', 'refused', 'refused', 'refused', 'refused']
job 4 manifest md5: 92c13f194013cd6a010ca157ea61a27c job list gives 92c13f194013cd6a010ca157ea61a27c
job 4 (s116x_glm_d): brief md5 900a2d4e298130b9169110796a497e89, job list 900a2d4e298130b9169110796a497e89, in sandbox 900a2d4e298130b9169110796a497e89; files 34, links 0, key-like paths none; sources from outside Semantics/ none; binaries, raw output or large files none; a model/ folder False
   --- echo probe > probe.txt -> exit 126 | refused by the sandbox: here only `python3 -m model.run` runs, with --claim FCnn (repeatable), --scale N (at most 4), -- | dummy token in output: False
   --- touch probe.txt -> exit 126 | refused by the sandbox: here only `python3 -m model.run` runs, with --claim FCnn (repeatable), --scale N (at most 4), -- | dummy token in output: False
   --- python3 -c 'print(1)' -> exit 126 | refused by the sandbox: here only `python3 -m model.run` runs, with --claim FCnn (repeatable), --scale N (at most 4), -- | dummy token in output: False
   --- python3 -c "open('p','w')" -> exit 126 | refused by the sandbox: here only `python3 -m model.run` runs, with --claim FCnn (repeatable), --scale N (at most 4), -- | dummy token in output: False
   --- cat BRIEF.md -> exit 126 | refused by the sandbox: here only `python3 -m model.run` runs, with --claim FCnn (repeatable), --scale N (at most 4), -- | dummy token in output: False
   --- env -> exit 126 | refused by the sandbox: here only `python3 -m model.run` runs, with --claim FCnn (repeatable), --scale N (at most 4), -- | dummy token in output: False
   --- python3 scripts/s116_gather_the_results.py > out.txt -> exit 126 | refused by the sandbox: here only `python3 -m model.run` runs, with --claim FCnn (repeatable), --scale N (at most 4), -- | dummy token in output: False
   --- python3 scripts/s116_gather_the_results.py -> exit 126 | refused by the sandbox: here only `python3 -m model.run` runs, with --claim FCnn (repeatable), --scale N (at most 4), -- | dummy token in output: False
   --- python3 -m model.run --claim FC23 -> exit 126 | refused by the sandbox: here only `python3 -m model.run` runs, with --claim FCnn (repeatable), --scale N (at most 4), -- | dummy token in output: False
   sandbox unchanged: True ; __pycache__: False ; probe files: ['scripts/s116_probe_the_saved_program_populations.py', 'scripts/reply 01, summarize_probes.py', 'scripts/reply 01, probe_task_audit.py']
   guard log: ['refused', 'refused', 'refused', 'refused', 'refused', 'refused', 'refused', 'refused', 'refused']
```
