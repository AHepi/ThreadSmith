# S110 - the GLM cross-examination: dry test before sending

*Run 29 September 2026 by the second Opus 5.5 agent that finished the setup after the outage, on the four jobs as built by `tools/s110x_build.py` at the rule's commit 3a9f35d (`--check`: all 9 built files identical to the build). A dummy key only; the real key was not used, opened or read. Nothing was sent.*

## 1. The sandboxes and the shell guard (`sandbox check.py`)

Each sandbox built by the helper's own `build_sandbox`; the manifest's and the brief's md5s checked against the job list and against `BRIEF.md` in the sandbox; the guard handed a write, `touch`, two `python3 -c`, `cat`, `env`, a redirect and the one program command. Every command was refused (exit 126; there is no program in any sandbox), no output held the dummy token, and every sandbox came back unchanged. The three book probes are printed as md5s only.

```
book probes (md5 only): ['7306eaa2', '7ed7ae08', '0e9a14b9']
job 1 manifest md5: dba5a2cab94bb9f7d32170099eb3f3f2 job list gives dba5a2cab94bb9f7d32170099eb3f3f2
job 1 (s110x_glm_a): brief md5 2ec8f2a83681bc4083a8afdf9d2aa6e1, job list 2ec8f2a83681bc4083a8afdf9d2aa6e1, in sandbox 2ec8f2a83681bc4083a8afdf9d2aa6e1; files 15, links 0, key-like paths none; sources from the scratchpad none; book probes found none
   --- echo probe > probe.txt -> exit 126 | refused by the sandbox …| dummy token in output: False
   --- touch probe.txt -> exit 126 | refused by the sandbox …| dummy token in output: False
   --- python3 -c 'print(1)' -> exit 126 | refused by the sandbox …| dummy token in output: False
   --- python3 -c "open('p','w')" -> exit 126 | refused by the sandbox …| dummy token in output: False
   --- cat BRIEF.md -> exit 126 | refused by the sandbox …| dummy token in output: False
   --- env -> exit 126 | refused by the sandbox …| dummy token in output: False
   --- python3 -m model.run --claim FC23 > out.txt -> exit 126 | refused by the sandbox …| dummy token in output: False
   --- python3 -m model.run --claim FC23 -> exit 126 | refused by the sandbox …| dummy token in output: False
   sandbox unchanged: True ; __pycache__: False ; probe files: none
   guard log: ['refused', 'refused', 'refused', 'refused', 'refused', 'refused', 'refused', 'refused']
job 2 manifest md5: 7c1744cac2a8c12b675c3cd7e0213d8c job list gives 7c1744cac2a8c12b675c3cd7e0213d8c
job 2 (s110x_glm_b): brief md5 faaaa9140a6600405c5bc1b73e0a608f, job list faaaa9140a6600405c5bc1b73e0a608f, in sandbox faaaa9140a6600405c5bc1b73e0a608f; files 15, links 0, key-like paths none; sources from the scratchpad none; book probes found none
   --- echo probe > probe.txt -> exit 126 | refused by the sandbox …| dummy token in output: False
   --- touch probe.txt -> exit 126 | refused by the sandbox …| dummy token in output: False
   --- python3 -c 'print(1)' -> exit 126 | refused by the sandbox …| dummy token in output: False
   --- python3 -c "open('p','w')" -> exit 126 | refused by the sandbox …| dummy token in output: False
   --- cat BRIEF.md -> exit 126 | refused by the sandbox …| dummy token in output: False
   --- env -> exit 126 | refused by the sandbox …| dummy token in output: False
   --- python3 -m model.run --claim FC23 > out.txt -> exit 126 | refused by the sandbox …| dummy token in output: False
   --- python3 -m model.run --claim FC23 -> exit 126 | refused by the sandbox …| dummy token in output: False
   sandbox unchanged: True ; __pycache__: False ; probe files: none
   guard log: ['refused', 'refused', 'refused', 'refused', 'refused', 'refused', 'refused', 'refused']
job 3 manifest md5: 4d46471e6925bafd13bcdb6a30d9102f job list gives 4d46471e6925bafd13bcdb6a30d9102f
job 3 (s110x_glm_c): brief md5 7511f2a2b4a23ed248b35c196c151472, job list 7511f2a2b4a23ed248b35c196c151472, in sandbox 7511f2a2b4a23ed248b35c196c151472; files 21, links 0, key-like paths none; sources from the scratchpad none; book probes found none
   --- echo probe > probe.txt -> exit 126 | refused by the sandbox …| dummy token in output: False
   --- touch probe.txt -> exit 126 | refused by the sandbox …| dummy token in output: False
   --- python3 -c 'print(1)' -> exit 126 | refused by the sandbox …| dummy token in output: False
   --- python3 -c "open('p','w')" -> exit 126 | refused by the sandbox …| dummy token in output: False
   --- cat BRIEF.md -> exit 126 | refused by the sandbox …| dummy token in output: False
   --- env -> exit 126 | refused by the sandbox …| dummy token in output: False
   --- python3 -m model.run --claim FC23 > out.txt -> exit 126 | refused by the sandbox …| dummy token in output: False
   --- python3 -m model.run --claim FC23 -> exit 126 | refused by the sandbox …| dummy token in output: False
   sandbox unchanged: True ; __pycache__: False ; probe files: none
   guard log: ['refused', 'refused', 'refused', 'refused', 'refused', 'refused', 'refused', 'refused']
job 4 manifest md5: da348503a3ccc057726d44f5c6f70a70 job list gives da348503a3ccc057726d44f5c6f70a70
job 4 (s110x_glm_d): brief md5 e26cf9410abc0132ab446b149b6d663b, job list e26cf9410abc0132ab446b149b6d663b, in sandbox e26cf9410abc0132ab446b149b6d663b; files 16, links 0, key-like paths none; sources from the scratchpad none; book probes found none
   --- echo probe > probe.txt -> exit 126 | refused by the sandbox …| dummy token in output: False
   --- touch probe.txt -> exit 126 | refused by the sandbox …| dummy token in output: False
   --- python3 -c 'print(1)' -> exit 126 | refused by the sandbox …| dummy token in output: False
   --- python3 -c "open('p','w')" -> exit 126 | refused by the sandbox …| dummy token in output: False
   --- cat BRIEF.md -> exit 126 | refused by the sandbox …| dummy token in output: False
   --- env -> exit 126 | refused by the sandbox …| dummy token in output: False
   --- python3 -m model.run --claim FC23 > out.txt -> exit 126 | refused by the sandbox …| dummy token in output: False
   --- python3 -m model.run --claim FC23 -> exit 126 | refused by the sandbox …| dummy token in output: False
   sandbox unchanged: True ; __pycache__: False ; probe files: none
   guard log: ['refused', 'refused', 'refused', 'refused', 'refused', 'refused', 'refused', 'refused']
```

## 2. Book text and keys, by searching the sandboxes

Every file of every sandbox searched against all 8-word runs of both books' extracted text (253,847 runs), for the longest stretch of words matching the books; and for file names and content shaped like a key (the helper's own key shapes).

```
book 8-word shingles: 253847
job1 : longest run of words matching the books 26 in S110/3 When something in a creative agent is knowledge.md ; key-named files none ; key-shaped content none
job2 : longest run of words matching the books 26 in S110/3 When something in a creative agent is knowledge.md ; key-named files none ; key-shaped content none
job3 : longest run of words matching the books 26 in S110/3 When something in a creative agent is knowledge.md ; key-named files none ; key-shaped content none
job4 : longest run of words matching the books 26 in S110/3 When something in a creative agent is knowledge.md ; key-named files none ; key-shaped content none
```

No sandbox holds a book file or a stretch of book text beyond single quotations. The longest match, 26 words, is in file 3 (section on Marletto's ch. 5): a checked quotation of 22 words ("it is exactly the thing one would ultimately have to eliminate …") preceded, outside the quotation marks, by the book's own words "of information is that", so the book's words run on for 26. The next longest is 24 words, also in file 3. This is recorded for the agent that reads the cross-examination (S19: at most 25 words); the file is sent as it was committed.

## 3. The runner, dry (`s110x_glm_loop.py --dry-run`, no key in the environment)

```
2026-09-29T09:59:36Z note: not committed, or differing from HEAD (a real run refuses): Semantics/tools/s110x_jobs - S110, GLM cross-examination.json
2026-09-29T09:59:36Z s110x_glm_loop: 4 jobs at once, up to 3 passes, effort medium, 1M context, rule Semantics/results/S110 - how the GLM cross-examination will be read, written before sending.md, returns Semantics/results/S110 - GLM cross-examination returns, sandboxes /tmp/claude-0/-home-user-ThreadSmith/8d9323da-c0ec-57ec-91fd-8f99ca99320a/scratchpad/s110x_sandboxes, GLM slots 4 [dry run: nothing sent; round 1 only]
2026-09-29T09:59:36Z round 1
2026-09-29T09:59:36Z s110x_glm_a: job 1 (map-FW0-I2), pass 1 of at most 3, as tag s110x_glm_a [dry run: not sent]
2026-09-29T09:59:36Z s110x_glm_b: job 2 (map-FW2-FW4), pass 1 of at most 3, as tag s110x_glm_b [dry run: not sent]
2026-09-29T09:59:36Z s110x_glm_c: job 3 (map-FW5-theory), pass 1 of at most 3, as tag s110x_glm_c [dry run: not sent]
2026-09-29T09:59:36Z s110x_glm_d: job 4 (files-1-3), pass 1 of at most 3, as tag s110x_glm_d [dry run: not sent]
2026-09-29T09:59:36Z s110x_glm_loop: every pass ended; accepted 0 of 4 jobs; not accepted: s110x_glm_a, s110x_glm_b, s110x_glm_c, s110x_glm_d
```

The one note (the job list not yet committed) is cleared by the commit that holds this file; the real run refuses otherwise.
