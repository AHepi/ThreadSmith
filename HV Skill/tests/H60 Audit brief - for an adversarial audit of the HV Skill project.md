# H60 Audit brief - for an adversarial audit of the HV Skill project

Written 21 September 2026 for whoever audits this project from outside: a person or a model, given this bundle and nothing else. It says what the project claims, where each claim's evidence sits, what to attack first, and how to rerun anything. Everything in it is a pointer into files that were written before the audit was thought of; nothing was made for the audit. The bundle was built by `rigs/make_audit_bundle.py`, which is included, so the auditor can check what was left out.

## What is under audit
A Claude skill, "hard-to-vary": a method for asking of any explanation whether every part does work. The current version is **file 31** (`authority/31/hard-to-vary/`, eight files); the version every test up to H57 ran on is **file 30** (`authority/hard-to-vary/`). The two differ in five passages; `diff -r` between the folders is the whole change. The project's own account of itself is `README.md`, its timeline `INDEX.md`, its log `records/HV Skill - project story.md`.

The project is one of three in a repository. The other two (a semantics and a formal language) are not in this bundle. The skill's front matter says it "sharpens" Deutsch's idea "using a formal theory supplied by the user" and maps that theory's terms in `references/word-list.md`; the project's own ledger (`RELATIONS.md`, entry R2) rates that claim **stated, not tested**. Treat it as an unsupported claim inside the artefact. The theory can be supplied on request.

## The claims, and where each one's evidence is
Each claim is made in the file named, from the raw evidence named. The auditor's job is to break the step from evidence to claim.

1. **The skill's words do work in a reader that never saw them.** Made in `results/54 Results ...`. Evidence: 147 single-shot runs in `rigs/plan 49 rig - DeepSeek on outside papers/runs/` (49 sources, three modes: 0 bare, 1 skill pasted, 2 router live), shape by program in `marking/shape_by_program.json`, close marks on 48 hidden reports in `marking/close_marks_restored.json`, the reports as the marker saw them in `marking/to_mark.md` with the labels in `marking/secret_mapping.json`. The plan that fixed the marking before any report was read: `tests/52 Marking plan ...`.
2. **The skill broke in two places in its wording** (the flip test fired on a derived conclusion; a free design choice was marked *fixed*), **and has one gap** (look inside has no purchase on a single document). Made in file 54 from two runs, `runs/P3-m1.json` and `runs/F4-m1.json`, one each.
3. **Break 1 did not recur in six repeats; break 2 recurred once in six** (skill unchanged). Made in `results/H57 ...` from `runs_repeat/` (twelve files), under criteria frozen in `tests/H56 Plan ...` before the runs. One P3 run is called borderline and quoted; the auditor should re-decide it.
4. **Under file 31, neither break recurred in twelve runs, and the new wording caused no new fault.** Made in `results/H59 ...` from `runs_repeat_31/`, under `tests/H58 Plan ...`.
5. **Controls stood; no test was ever reported impossible to run; the skill modes reached "same explanation at this level" verdicts the bare reader never did.** File 54, from the same 147 runs and the marks.
6. **Conversation mode works.** File 54, read but not marked, from `conv/` (twelve dialogues).

## Where to attack, in the order the project itself would
1. **The marker.** One marker (Claude) wrote the skill, chose the corpus, wrote the marking plan, marked every report, wrote both changes in file 31, and marked the runs that tested them. Every results file says so. The strongest single audit is a **blind re-mark**: take `marking/to_mark.md` (48 reports, labels stripped, as the marker saw them), mark under plan 52's rules without opening `secret_mapping.json`, then compare with `close_marks_restored.json`. Where the marks differ, the project's claims 1, 2 and 5 are in question. For H57 and H59 no hidden version was made (the marker saw file names); `hide.py` shows how one is made, and the twenty-four runs are small enough to shuffle by hand.
2. **The recurrence criteria** (`tests/H56 Plan`, section "What counts as a recurrence"). They were frozen before the runs, but they were written by the marker, and the P3 borderline run (H57, "Break 1, run by run", m1-r2) shows the line matters. Read the six P3 file 30 runs and decide where you would draw it. If you count the borderline as a recurrence, claim 3 changes and claim 4's premise ("both breaks seen under 30, neither under 31") strengthens; if you would count none of the F4 file 30 runs as break 2 (the recurrence's rationale differed from the original), file 31 was not forced and claim 4 rests on a change made without a forcing test.
3. **Three runs per box.** H57 and H59 rest on n = 3 per mode per paper per version. "0 of 6" is compatible with a break that fires one time in ten. The project says this in every "What this does not show". The auditor can add runs: `run.py` takes any repeat index (`P3:1:4`), costs about a cent a run.
4. **The framing text.** `run.py` `FRAMING` (mode 1 and 2) and `BARE` (mode 0) are the words every reader saw. Mode 0's instruction is shorter and asks for less; a reader told "say which parts do the work, which are loose" is not a fair rival to one handed a 13,000-word method. Claim 5's "the bare reader never did" is a comparison against that instruction. Read both and decide whether the comparison is fair, and what a fairer mode 0 would be.
5. **Shape by program.** `shape.py` and `repeat_check.py` decide FULL/PART/NONE by regular expressions on headings and mark words. A report can be FULL by the regexes and empty of method. H57 flags one such (F4-m1-r3, "FULL by program, thin by eye"). Read the twelve `runs_repeat/` replies and count how many you would call FULL.
6. **Claim-checking.** Each close-marked report had up to five claims (plan 52) or three (plans H56, H58) checked against the text. The claims were chosen by the marker. Lesson 46 records ten wrong marks on a first pass, corrected. Re-check any claim; the texts are rebuilt by `fetch.py` (they are third parties' papers and are not in the bundle).
7. **The corpus.** `tests/50 Corpus ...` says how 49 sources were chosen and why ten were replaced. Nine are truncated (listed there). The coverage map from every part of the skill to at least two sources is the marker's. Ask whether the sources that exercised each test were the ones most likely to break it.
8. **The change to file 31.** Plan H56 froze, before the run, the observation that file 54's change 2 was aimed at a line already present in `by-domain.md`; the reworded change went to where *fixed* is defined. H59 records a side effect: four P3 runs now mark a premise the author "takes as a given" *fixed* where file 30 runs said *borrowed*. Decide whether that is a better or a worse mark, and whether the new clause could produce a break on a paper not in this set. Change 1 was applied although break 1 did not recur (plan H56's rule said both; H57 says why it went in).
9. **The Sonnet 5 arm is not run.** Plan H56 names Claude Sonnet 5 as a second reader (decision H3); no Anthropic key was available in the session that ran the DeepSeek arm. Claims 3 and 4 are one reader's. `run_sonnet.py` is written and dry-run; it has never sent a request.
10. **Numbering and cross-references.** Lesson 48 records a renumbering by script (45 to 52 became 47 to 54). Every internal reference was rewritten; check a sample. Since the record split, this project counts on its own (H55 onward); the rule is in the root conventions.
11. **The rig's own checks.** The runner diffs its skill copy against the authority before any call (Lesson 44), retries once on an empty reply (Lesson 45), and records finish reasons. The 147-run phase ran on an earlier unstreamed runner (`run_v1_unstreamed.py`), the repeats on the streamed one; `runs_verify/` is the one run that verified the patch. Decide whether the two runners are the same instrument.
12. **The skill's own claims about itself.** `SKILL.md` says it is "a way of criticising, not a truth-meter". Read a report that reached a verdict and ask whether the reader treated the marks as a score despite "never add the marks up".

## How to rerun anything
- Packages: `requests`, `pymupdf` (for fetching), `anthropic` (Sonnet runner). Python 3.
- Rebuild the texts: `python3 fetch.py` (all 49) or `python3 fetch.py P3 F4`; writes `corpus/<id>.txt`. Sources and licences in `sources.json`; every substitution in file 50.
- Copy the skill in: `cp -r ../../authority/hard-to-vary skill/` (file 30) or `cp -r ../../authority/31/hard-to-vary skill_31/` (file 31). The runner refuses to send if the copy differs from the authority.
- Dry run (sends nothing): `python3 run.py --dry P3:1:1`; `SKILL_FILE=31 python3 run.py --dry P3:1:1`.
- Run: `DEEPSEEK_API_KEY=... python3 run.py P3:1:4 F4:2:4` (a new repeat index; existing files are skipped, never overwritten). Sonnet: `ANTHROPIC_API_KEY=... python3 run_sonnet.py P3:1:1 ...`. Settings are constants at the top of each runner.
- Shape check: `python3 repeat_check.py runs_repeat runs_repeat_31`.
- Keys are read from the environment and written to no file; the project's rule.

## What is in the bundle, and what is not
In: this brief; the root conventions and tutorials of the repository (`conventions/`); the whole `HV Skill/` folder as committed (authority, tests, results, records, rigs with every raw return, the marks, the conversation dialogues); the shared record the three projects began with (`shared-history/`, complete to log 59, unchanged), because this project's INDEX links into it.
Out: the fetched texts (rebuilt by `fetch.py`); the two other projects (on request); the `skill/` copies inside the rig (identical to the authority by the runner's check); any key.

## Reading order for the auditor
1. This brief. 2. `HV Skill/README.md`, then `records/READ ME FIRST.md` and `records/HV Skill - Status.md`. 3. `tests/52 Marking plan` (the rules the marks were given under), then `results/54`. 4. `tests/H56 Plan`, `results/H57`, `tests/H58 Plan`, `results/H59`. 5. The raw returns for whatever you doubt. The conventions in `conventions/RESEARCH-CONVENTIONS.md` say what "frozen", "kept as it came" and "not tested" mean here.

## Traps
- Reading the marks as scores. The project never adds them; neither should the audit.
- Reading a FULL shape as a good report.
- Reading file 54 or H57 as saying anything about the truth of any document. They mark the skill.
- Trusting this brief's summary over the files it points to. Where they disagree, the files are the record.
