# Language - the ledger language

A formal language that everyday reasoning prose can be turned into, so that an external checker with fixed rules can find the faults (contradictions, jumps, kind mistakes, parts that do no work) and its findings can be turned back into plain prose that points at your sentences. "The external checker is the one essential thing" (Decision 5).

## Current state
- **Authority:** [38 The ledger language - complete definition](<authority/38 The ledger language - complete definition.md>): purpose, what a line means, the five parts of a line, fourteen kinds of content, the fixed lists, strength, the laws, how arguments and what-ifs are tested, everything the checker can say, sixteen translator rules, what is outside the language, traps. Supersedes 36, and the rulebooks 34, 33, 23, 20 before it. Handed to a translator together with [39 Prompt - translate a text into the ledger language](<authority/39 Prompt - translate a text into the ledger language.md>), never alone.
- **Built:** two checker rigs on s(CASP), joined by a bridge, in [rigs/](rigs/). Rig 1 checks arguments; rig 2 checks causes written as pressing patterns in five slots. Sixteen logged patches on rig 1 and three on rig 2, each with what it gives up ([project story](<../records/Checked reasoning language - project story.md>), "What each patch gave up").
- **Tested on:** five of Claude's paragraphs, three of the owner's (ball and coin, Markus, Mondays), 21 of the other model's audit cases, and a blind sample of eight of its literary texts (seven matched its keys). Every run had its plan frozen first.
- **Strength of evidence:** the translating has always been Claude's. "Not tested: a translator other than Claude" appears in every results file.
- **Audited from outside (log 45):** the other model's audit of 38 and 39 is in [results/](results/), unchanged: fifteen findings on the wording, twelve repairs, sixty new texts, six of its own translations, nothing run. Four findings hold up against the text (F01, F02, F04, F15). [Plan 45](<tests/45 Test plan - the 38 and 39 audit package, ledgers compared and findings sorted.md>) is frozen and not yet run: compare its six ledgers with Claude's, and sort the fifteen findings by running their cases.
- **Next step (from the log):** run plan 45; then hand the other model the eight texts of plan 37 so the comparison runs both ways.

## Where to start
[INDEX.md](INDEX.md) for the timeline. [ORIGIN.md](ORIGIN.md) for the goal in the owner's words and the twelve properties. For the language itself, file 38. For what the checkers actually do, `rigs/READ ME FIRST.md`.

## What is in this folder
```
ORIGIN.md      the goal, the twelve properties, how the pieces fit
INDEX.md       every research state from the first theory to file 39, with what is and is not here
authority/     38 (the language), 39 (the translator's task)
tests/         frozen plans: 21 Markus, 22 Mondays, 35 the third pile, 37 the blind sample, 45 the audit of 38 and 39
results/       21 and 22 (html pages), 37 (md): what happened, with predictions ticked; 45: the other model's package, as received
rigs/          the working checkers, frozen and patched, every ledger, the bridge, and raw_log.txt
```
`rigs/` is this project's own addition to the shared layout: the rig is at once the build of the theory, the apparatus for every test, and (in `raw_log.txt` and the ledgers) the raw evidence.

## Traps
- **The rig bundle matches no older results file.** It holds the checkers as they are now. The results files say what the checkers said on the day.
- **A clean report means the lines fit together**, not that the reasoning is right. On a story it may only mean "not the kind of text the checker was built for".
- **Patches 4 and 5 are not general.** Each was forced by one paragraph.
- **The joined script points at the folder the rigs were built in.** Change that one path (`/home/claude/rig2/...` in `rigs/rig 1 - arguments/joined/run_joined.py`) to run it elsewhere.
- **Compare reports without the GAUGE line.** It carries timings that change run to run.
