# HV Skill - hard to vary

A Claude skill for testing whether an explanation is **hard to vary**: whether every part does real work, so that changing any part would break its power to explain. The idea is David Deutsch's (*The Beginning of Infinity*); the skill sharpens it with the semantics (see [Semantics/](../Semantics/)) and maps the theory's terms to plain words.

The skill is also the method the whole project was built with: the language's twelve properties were worked out with it (log 01), and it was improved from what each stage taught.

## Current state
- **Authority:** [file 30](<authority/hard-to-vary/SKILL.md>), "modular, with router and map": one main file and seven reference modules (8 files, 13,614 words; log 43). Unpacked in `authority/hard-to-vary/`; the uploadable archive `30 Skill - ... .skill` sits beside it.
- **Improved seven times** (02, 05, 08, 14, 21, 22, 30 as the log counts them, with 10, 11, 17 and 29 as further named files). Earlier skill files are not in the bundles; each improvement is logged with the case that prompted it.
- **One line proposed, held out** (log 42): for the poke test, pick the two changes close together, because far-apart changes can be found for any label. Kept out of the skill until tested.
- **Tested on outside papers, read by DeepSeek V4.1 Flash (logs 49 to 54):** 49 documents from science, computability, economics, philosophy, fiction, design, rules and instructions ([50 Corpus](<tests/50 Corpus - outside sources for the skill test.md>)), three ways of handing over the skill ([49 Plan](<tests/49 Plan - the skill on outside papers, read by DeepSeek V4.1 Flash.md>)), 147 runs and twelve conversations, marked under a plan frozen before reading ([52](<tests/52 Marking plan - frozen before the corpus is read.md>)). The answer is in [54 Results](<results/54 Results - where the skill breaks, on outside papers read by DeepSeek.md>): the skill's words do work in a reader that never saw them; it breaks in two small places in its wording (the flip test on a derived conclusion; a free design choice marked "fixed"); *look inside* has almost no purchase on a single document; no test was ever reported as impossible to run; controls stood; the skill modes reached six "same explanation at this level" verdicts the bare reader never reached. Three changes proposed, held until tested.
- **Two earlier designs, not run to a result:** [42 Test plan](<tests/42 Test plan - hard-to-vary skill read by DeepSeek.md>) with [43 Corpus](<tests/43 Corpus - contested theories for the DeepSeek test.md>) and [47 Addendum](<tests/47 Addendum to test plan 42 - the corpus run, settings and expectations.md>), rigged and dry-run but never sent; [48](<tests/48 Test plan - the skill on well-constructed contested explanations (stopped).md>), Claude readers on rebuilt contested theories, stopped by the owner part-way and unmarked.

## Where to start
Read [SKILL.md](<authority/hard-to-vary/SKILL.md>): the idea in one example (seasons: a grieving goddess against the tilt of the earth), the three things that can change, and the router table saying which module to open when. [INDEX.md](INDEX.md) has the timeline. [ORIGIN.md](ORIGIN.md) says where the skill came from.

## What is in this folder
```
ORIGIN.md      Deutsch's idea; the skill's relation to the semantics; how it entered the project
INDEX.md       every improvement, what prompted it, and the unrun test
authority/     hard-to-vary/ (SKILL.md + references/), and the .skill archive as uploaded
tests/         42, 43, 47 (the first design and its corpus); 48 (stopped); 49, 50, 52 (the outside-papers plan, corpus and marking plan)
results/       51 (pilot), 53 (the run as a program sees it), 54 (where the skill breaks)
rigs/          the programs and raw returns: 147 runs, 12 dialogues, the hidden reports and the marks
```

## Traps
- **Showing file 42, 43, 49, 50 or 52 to a reader under test.** They hold the answer keys and the sources' standing.
- **Handing the skill to the other model.** Its wording is full of "never" and "may not". File 24 in Semantics/ is the version written for that model.
- **Reading the corpus as looked up.** File 43 was compiled from Claude's own knowledge and source-checked afterwards; file 50's sources are other people's papers, fetched, and the texts are not in the repository.
- **Reading file 54 as a pass mark.** It marks the skill, not the truth of any document; one run per box; the marker wrote the skill and chose the corpus, and got ten marks wrong on a first pass before correcting them.
- **Reading a fuller report as a better one.** Length is not a finding; the marks in file 54 are never added up.
