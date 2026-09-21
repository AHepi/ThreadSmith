# HV Skill - index

The skill's lineage, as the log records it. Each improvement is a research state: what prompted it, what was added, and what tested it. Numbers are log entries; the skill's entries are in this project's own [project story](<records/HV Skill - project story.md>) (copied from the shared record, where they also remain), and new ones are H-numbered there. Skill files before 30 are **not in bundle** (superseded, left out on purpose).

| Log | Skill file | Prompted by | What changed | Tested by |
| --- | --- | --- | --- | --- |
| 01 | (unnumbered, prior) | Decision 2 | Used, not changed: worked out twelve properties for the language | The properties themselves, untested |
| 02 | (no file named) | What page 01 taught | A way to build; a source for each job (given / fixed / added); naming what a swap shares; a "pull" test; a gauge for every catch-all; three more marks (held if, two routes, fixed); a reference file on building, researching and compiling | Skill validator passes (Lesson 4: description trimmed) |
| 05 | `05 Skill - improved after research test.skill` | Entries 03 and 04 | Tested each addition by "what would have gone differently without it?"; three gaps fixed: the tag "claimed", a rule for when to stop, a list for findings that fit no part | Log 05 itself |
| 08 | `08 Skill - improved after the checker run.skill` (named in log) | The s(CASP) run, log 07 | A section on running a home-made test: freeze cases first, keep a "nothing" case, develop on one then freeze, keep first outputs, log every patch by layer, tick predictions, say whose cases | Logs 09, 10 |
| 10, 11 | `10`, `11 Skill ...` | The owner's paragraph; the second theory | (named as superseded in the read-me; details in logs 10 and 11) | |
| 14 | `14 Skill - improved before the build.skill` | Before building rig 2 | Name a borrowed idea's best rival before searching; build from one page only; for every one-case law add a quiet neighbour; label your own added sentences | Log 17 build |
| 17 | `17 Skill - improved after the build test.skill` | Rig 2 build and hostile cases | (log 17) | |
| 21 | `21 Skill - improved after the Markus paragraph.skill` | Log 21 | (log 21) | |
| 22 | `22 Skill - improved after the Mondays paragraph.skill` | Log 22 | (log 22) | |
| 29 | `29 ...` | Round 4 | Never run; content sits inside instruction 30 | |
| 30 | **[30 Skill - hard-to-vary - modular, with router and map.skill](<authority/30 Skill - hard-to-vary - modular, with router and map.skill>)** - current | Log 30: rebuilt as modules with a router table and a flowchart map | One main file, seven references: the idea in depth, question bank, by domain, building, testing against cases, reporting, word list | Used as the test for the other model's workflow update (log 30, 31); opened and counted at log 43 |
| 42 | (no change) | The owner asked whether anything needs adding | One line proposed for the poke test (two changes close together) plus a trap; **held out until tested**. Found: the skill already asks for a "near neighbour" in swaps, says nothing about closeness in pokes | Plan 42, never sent; the line stayed out of the skill through the outside-papers test (log 54) |

## Research state: the DeepSeek test (logs 42, 43, 47) - designed, rigged, not sent
| | |
| --- | --- |
| Story | Decision 31: "Design a test for hard to vary using Deepseek V4.1 flash. Don't run it just yet though." Decision 32: compile a corpus of about twenty contested theories first. Decision 33: restart without the research add-ons. |
| Authority under test | Skill file 30. Reader: DeepSeek V4.1 Flash. |
| Test | [42 Test plan](<tests/42 Test plan - hard-to-vary skill read by DeepSeek.md>) - two questions frozen: do the skill's words do work in another reader; does the proposed line do work. Four setups, three repeats each, a program hides and shuffles the labels, Claude marks blind. [47 Addendum](<tests/47 Addendum to test plan 42 - the corpus run, settings and expectations.md>) - the settings and expectations frozen for running it on corpus 43 (effort "high" as the middle of three; rewording in place of renaming; a seventh way to fail, that recall does the work). |
| Cases | [43 Corpus](<tests/43 Corpus - contested theories for the DeepSeek test.md>) - 20 contested theories in a supporter's voice (the passage), what critics name as the weak point (the answer key, never shown), and 5 controls. Source-checked on the day: seven keys changed. |
| Rig | [rigs/plan 42 rig](<rigs/plan 42 rig - DeepSeek, unrun/>) - runner, hider, table-maker; dry-run on a stub. |
| Raw result | None. Never sent: the owner redirected the test to outside papers (decision 39) before a key was used on it. |
| Lessons | [Lesson 36](<../Language/records/Checked reasoning language - Lessons.md>) (add-ons stalled), [37](<../Language/records/Checked reasoning language - Lessons.md>) (numbering), [38](<../Language/records/Checked reasoning language - Lessons.md>) (renaming does not transfer to real theories), [39](<../Language/records/Checked reasoning language - Lessons.md>) (the record disagreed with itself about the source check). |

## Research state: Claude readers on well-built contested explanations (log 48) - stopped
| | |
| --- | --- |
| Story | Decision 37: continue the skill test, not the language test, on well-constructed explanations widely known to be contested. Decision 38: "No stop". |
| Test | [48 Test plan](<tests/48 Test plan - the skill on well-constructed contested explanations (stopped).md>) - twelve contested theories rebuilt in their supporters' strongest form plus four controls; three setups (report shape; the skill; the skill with the semantics); reader a fresh Claude agent. |
| Raw result | [rigs/plan 48](<rigs/plan 48 - Claude readers, stopped/>) - 31 of 48 replies, written before the owner stopped the run. Unmarked; nothing read. |
| Lessons | [Lesson 40](<../Language/records/Checked reasoning language - Lessons.md>) (thirty readers launched before the owner had seen the plan), [41](<../Language/records/Checked reasoning language - Lessons.md>) (a Claude reader was never what the owner wanted). |

## Research state: the skill on outside papers, read by DeepSeek V4.1 Flash (logs 49 to 54) - run and marked
| | |
| --- | --- |
| Story | Decision 39: DeepSeek as reader; no Claude subagents; the semantics not as test content; papers from science, fiction, philosophy, computability and elsewhere, chosen to test all of the skill, "to see where it breaks"; ten concurrent; plan first, start only on the owner's word. Decisions 40 to 43: each phase started on the owner's word ("Compile corpus first", "Go", "Great. Do it", "Ok go!"). |
| Authority under test | Skill file 30, unchanged throughout (checked by difference before every run). Reader: `deepseek-flash` (V4.1 Flash), thinking on, effort high. |
| Test | [49 Plan](<tests/49 Plan - the skill on outside papers, read by DeepSeek V4.1 Flash.md>) - the rule for choosing a source, the channels, a coverage map from every part of the skill to at least two sources, three ways of handing over the skill (pasted whole; the router live through a tool; a conversation with a second session playing the author), the framing text word for word, settings, phases each waiting on the owner. [52 Marking plan](<tests/52 Marking plan - frozen before the corpus is read.md>) - marks the skill, not the truth of the documents; four meanings of "broke", each its own mark; three layers kept apart (document, skill, reader); a close-marking sample drawn by program before anything was read. |
| Cases | [50 Corpus](<tests/50 Corpus - outside sources for the skill test.md>) - 49 sources, 429,268 words: 18 science, 7 computability, 6 economics, 6 philosophy, 6 fiction, 2 designs, 2 rules, 2 instructions; five pairs (a claim beside its critique); eight controls; every substitution recorded with its reason. The texts are rebuilt by `fetch.py` and are not in the repository. |
| Raw result | [rigs/plan 49 rig](<rigs/plan 49 rig - DeepSeek on outside papers/>) - 147 single-shot runs (`runs/`), two first attempts that came back empty, twelve conversation dialogues (`conv/`), the hidden reports and the marks (`marking/`). |
| Interpretation | [51 Pilot results](<results/51 Pilot results - nine runs on three outside sources.md>) - the introduction works: none of the six things watched for happened; the router opened modules unprompted. [53 Corpus run](<results/53 Corpus run - what happened, before any report was marked.md>) - the run as a program sees it: the method's form in 40 of 49 (pasted) and 49 of 49 (router) reports, none without the skill; two empty replies re-run once. [54 Results](<results/54 Results - where the skill breaks, on outside papers read by DeepSeek.md>) - the answer: two breaks in the skill's wording (the flip test fires on a derived conclusion; two vocabularies let a free design choice be marked "fixed"), one gap (look inside has almost no purchase on a single document), no CANNOT mark anywhere, three misreads all in the pasted-whole mode, controls standing, six same-explanation-at-this-level verdicts from the skill modes and none from the bare reader; conversation mode works and the author concedes under the skill's questions. Three changes to the skill proposed and held. |
| Lessons | [Lessons 42 to 48](<../Language/records/Checked reasoning language - Lessons.md>): fetch failures a status code does not show; trimming by marker; the crashed pilot; empty replies with no error; the marker judging from the first search hit (ten marks wrong, corrected); readers asking several questions a turn; the third numbering clash. |
| Not tested | Repeatability (one run per box; two runs on one paper disagreed on the flip); 33 of the 49 sources beyond their shape; a second marker; the semantics as content. |
| Next | On the owner's word: P3 and F4 three more runs each under both skill modes, skill unchanged; if the breaks recur, the three changes in file 54, then the same six runs again. |

## Files in this project, by folder
- `authority/`: `hard-to-vary/SKILL.md` and `references/` (8 files); the `.skill` archive.
- `tests/`: 42, 43, 47, 48, 49, 50, 52.
- `results/`: 51, 53, 54.
- `rigs/`: `plan 42 rig - DeepSeek, unrun/`; `plan 48 - Claude readers, stopped/`; `plan 49 rig - DeepSeek on outside papers/` (147 runs, 12 dialogues, the marks). See [rigs/README.md](rigs/README.md).

## Numbering note
The chat that ran the outside-papers test numbered its files 45 to 52 while the repository had gone on to 45 and 46 in the Language project. On import they were renumbered 47 to 54 (decisions 37 to 43), with every reference inside them rewritten (Lesson 48).
