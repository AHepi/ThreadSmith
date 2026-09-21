# HV Skill - hard to vary

A Claude skill for testing whether an explanation is **hard to vary**: whether every part does real work, so that changing any part would break its power to explain. The idea is David Deutsch's (*The Beginning of Infinity*); the skill sharpens it with the semantics (see [Semantics/](../Semantics/)) and maps the theory's terms to plain words.

The skill is also the method the whole project was built with: the language's twelve properties were worked out with it (log 01), and it was improved from what each stage taught.

## Current state
- **Authority:** [file 30](<authority/hard-to-vary/SKILL.md>), "modular, with router and map": one main file and seven reference modules (8 files, 13,614 words; log 43). Unpacked in `authority/hard-to-vary/`; the uploadable archive `30 Skill - ... .skill` sits beside it.
- **Improved seven times** (02, 05, 08, 14, 21, 22, 30 as the log counts them, with 10, 11, 17 and 29 as further named files). Earlier skill files are not in the bundles; each improvement is logged with the case that prompted it.
- **One line proposed, held out** (log 42): for the poke test, pick the two changes close together, because far-apart changes can be found for any label. Kept out of the skill until tested.
- **A test designed and frozen, unrun:** [42 Test plan - hard-to-vary skill read by DeepSeek](<tests/42 Test plan - hard-to-vary skill read by DeepSeek.md>). Does the skill's wording do work in a reader that has never seen the theory? Four setups, each adding one thing; replies marked blind against an answer key. [43 Corpus](<tests/43 Corpus - contested theories for the DeepSeek test.md>) supplies 20 contested theories and 5 controls, replacing the plan's ten invented cases. Waiting on the owner's go-signal and a source check of the answer keys.

## Where to start
Read [SKILL.md](<authority/hard-to-vary/SKILL.md>): the idea in one example (seasons: a grieving goddess against the tilt of the earth), the three things that can change, and the router table saying which module to open when. [INDEX.md](INDEX.md) has the timeline. [ORIGIN.md](ORIGIN.md) says where the skill came from.

## What is in this folder
```
ORIGIN.md      Deutsch's idea; the skill's relation to the semantics; how it entered the project
INDEX.md       every improvement, what prompted it, and the unrun test
authority/     hard-to-vary/ (SKILL.md + references/), and the .skill archive as uploaded
tests/         42 (the plan, frozen), 43 (the corpus with answer keys)
results/       NOT-YET-RUN.md - nothing until the DeepSeek test runs
```

## Traps
- **Showing file 42 or 43 to a reader under test.** Both hold the answer key.
- **Handing the skill to the other model.** Its wording is full of "never" and "may not". File 24 in Semantics/ is the version written for that model.
- **Reading the corpus as looked up.** File 43 was compiled from Claude's own knowledge and says so; a source check is a named step before the run (Lesson 36).
- **Counting a good result as the skill's.** Until plan 42 runs, results may come from Claude having read the theory, not from the words of the skill.
