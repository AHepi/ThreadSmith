# HV Skill - hard to vary

A Claude skill for testing whether an explanation is **hard to vary**: whether every part does real work, so that changing any part would break its power to explain. The idea is David Deutsch's (*The Beginning of Infinity*); the skill sharpens it with the semantics (see [Semantics/](../Semantics/)) and maps the theory's terms to plain words.

The skill is also the method the whole project was built with: the language's twelve properties were worked out with it (log 01), and it was improved from what each stage taught.

## Current state
- **Draft file 32** (`authority/32/`, log H67): file 31 with one change answering every fault H62 and H64 left open; not the authority until plan H67 runs and the skill is frozen.
- **Authority:** [file 31](<authority/31/hard-to-vary/SKILL.md>), made under log H58 after the repeatability run (H57) forced it: file 30 with two changes (the flip is not for a derived conclusion; *fixed* is only for what the owner put outside the test). Unpacked in `authority/31/hard-to-vary/`, the archive `31 Skill - ... .skill` beside it. Tested in plan H58 (H59): neither break recurred in twelve runs, no new fault. [File 30](<authority/hard-to-vary/SKILL.md>), "modular, with router and map" (8 files, 13,614 words; log 43), stays in `authority/hard-to-vary/` with its archive: it is the version every test up to H57 ran on.
- **Improved eight times** (02, 05, 08, 14, 21, 22, 30, 31 as the log counts them, with 10, 11, 17 and 29 as further named files). Earlier skill files are not in the bundles; each improvement is logged with the case that prompted it.
- **One line proposed, held out** (log 42): for the poke test, pick the two changes close together, because far-apart changes can be found for any label. Kept out of the skill until tested.
- **Tested on outside papers, read by DeepSeek V4.1 Flash (logs 49 to 54):** 49 documents from science, computability, economics, philosophy, fiction, design, rules and instructions ([50 Corpus](<tests/50 Corpus - outside sources for the skill test.md>)), three ways of handing over the skill ([49 Plan](<tests/49 Plan - the skill on outside papers, read by DeepSeek V4.1 Flash.md>)), 147 runs and twelve conversations, marked under a plan frozen before reading ([52](<tests/52 Marking plan - frozen before the corpus is read.md>)). The answer is in [54 Results](<results/54 Results - where the skill breaks, on outside papers read by DeepSeek.md>): the skill's words do work in a reader that never saw them; it breaks in two small places in its wording (the flip test on a derived conclusion; a free design choice marked "fixed"); *look inside* has almost no purchase on a single document; no test was ever reported as impossible to run; controls stood; the skill modes reached six "same explanation at this level" verdicts the bare reader never reached. Three changes proposed, held until tested.
- **The two breaks on repeat (H56 to H62):** under file 30, DeepSeek reproduced break 2 once in six and break 1 not at all; Sonnet 5 reproduced neither. File 31 (the flip not for a derived conclusion; *fixed* only for what the owner put outside the test) was forced and then tested: neither break in twelve DeepSeek runs or twelve Sonnet 5 runs; Sonnet 5 showed two new faults tied to the new wording, one run each ([H62](<results/H62 Results - the Sonnet 5 arm of plans H56 and H58, as Claude Code subagents.md>)).
- **Blind second marking (H63, H64):** ninety-six Sonnet 5 markers re-marked every close-marked report without the labels or the first marker's marks. Both breaks of file 54 were found again; recurrence on the repeat set agreed 48 of 48; RAN-versus-not 84 percent; controls 6 of 6; no CANNOT. Shape's PART boundary, the "turned own test" mark and the same-explanation count do not agree between markers and are struck as marked. Four further kinds of break in the skill's wording, quoted, held as change candidates ([H64](<results/H64 Results - blind second marking by Sonnet 5, agreement with the first marker.md>)).
- **Two earlier designs, not run to a result:** [42 Test plan](<tests/42 Test plan - hard-to-vary skill read by DeepSeek.md>) with [43 Corpus](<tests/43 Corpus - contested theories for the DeepSeek test.md>) and [47 Addendum](<tests/47 Addendum to test plan 42 - the corpus run, settings and expectations.md>), rigged and dry-run but never sent; [48](<tests/48 Test plan - the skill on well-constructed contested explanations (stopped).md>), Claude readers on rebuilt contested theories, stopped by the owner part-way and unmarked.

## Where to start
This project keeps its own record in [records/](records/) from 21 September 2026 (log, Decisions, Lessons, Status); its [READ ME FIRST](<records/READ ME FIRST.md>) says how it relates to the shared record the projects began with. Its claims about the other projects are in [RELATIONS.md](RELATIONS.md).

Read [SKILL.md](<authority/hard-to-vary/SKILL.md>): the idea in one example (seasons: a grieving goddess against the tilt of the earth), the three things that can change, and the router table saying which module to open when. [INDEX.md](INDEX.md) has the timeline. [ORIGIN.md](ORIGIN.md) says where the skill came from.

## What is in this folder
```
ORIGIN.md      Deutsch's idea; the skill's relation to the semantics; how it entered the project
records/       this thread's own log, Decisions, Lessons and Status, from 21 September 2026
RELATIONS.md   this project's claims about its connections to the other two, with status and evidence
INDEX.md       every improvement, what prompted it, and the unrun test
authority/     hard-to-vary/ (SKILL.md + references/), and the .skill archive as uploaded
tests/         42, 43, 47 (the first design and its corpus); 48 (stopped); 49, 50, 52 (the outside-papers plan, corpus and marking plan)
results/       51 (pilot), 53 (the run as a program sees it), 54 (where the skill breaks)
rigs/          the programs and raw returns: 147 runs, 12 dialogues, the hidden reports and the marks
```

## Rules of this project
- **Never show a reader under test the answer key or a source's standing** (files 42, 43, 49, 50, 52; `keys.json` and `cases.json` in the rigs).
- **Running a reader under test:** every run saved as it came, with its finish reason; a run that returns empty is kept and run once more, recorded as a second attempt; the key is read from the environment and written to no file.
- **A change to the skill is a new numbered skill file**, made only after a test has forced it; proposed changes are held in the results file that proposes them.
- **Third-party texts fetched for a test are not kept;** the manifest and fetcher that rebuild them are.
- **The skill judges; it does not choose** (decision H5, RELATIONS R6). Its report ends with one next step offered, never taken. Which test to run, how often, when to stop, what a result forces and what is held out are planning decisions, made in a plan file under the shared conventions and not by the skill.
- **Never a Fable 5.1 reader under test, and never a Fable 5.1 subagent** (decisions H4, H7). Opus 5 subagents are permitted from decision H7, geared with this skill, at effort "extra" (xhigh), not max. Readers so far: DeepSeek V4.1 Flash; Claude Sonnet 5 from plan H56 (decision H3), run as Claude Code subagents under addendum H61.

## Words used in this project
Short form; the skill's own word list, mapping the theory's terms to plain words, is `authority/hard-to-vary/references/word-list.md`.
- **The eight marks.** Held / held if / two routes / loose / idle / borrowed / fixed / unknown: how firmly a part of an explanation is held in place.
- **Seen / claimed / worked out / recalled.** How a thing about a tool is known. Seen: watched it happen. Claimed: a source says so. Worked out: follows from tagged things. Recalled: memory only. "Seen" is further marked "on my own cases" or "on someone else's".
- **Passage, answer key, setup, control (DeepSeek test).** What the reader under test is sent; what its reply is marked against, which it never sees; what it is given alongside the case; a sound case there to catch a reader that criticises everything.

## Traps
- **Showing file 42, 43, 49, 50 or 52 to a reader under test.** They hold the answer keys and the sources' standing.
- **Handing the skill to the other model.** Its wording is full of "never" and "may not". File 24 in Semantics/ is the version written for that model.
- **Reading the corpus as looked up.** File 43 was compiled from Claude's own knowledge and source-checked afterwards; file 50's sources are other people's papers, fetched, and the texts are not in the repository.
- **Reading file 54 as a pass mark.** It marks the skill, not the truth of any document; one run per box; the marker wrote the skill and chose the corpus, and got ten marks wrong on a first pass before correcting them.
- **Reading a fuller report as a better one.** Length is not a finding; the marks in file 54 are never added up.
