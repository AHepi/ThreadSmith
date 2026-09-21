# Language - the ledger language

A formal language that everyday reasoning prose can be turned into, so that an external checker with fixed rules can find the faults (contradictions, jumps, kind mistakes, parts that do no work) and its findings can be turned back into plain prose that points at your sentences. "The external checker is the one essential thing" (Decision 5).

## Current state
- **Authority:** [38 The ledger language - complete definition](<authority/38 The ledger language - complete definition.md>): purpose, what a line means, the five parts of a line, fourteen kinds of content, the fixed lists, strength, the laws, how arguments and what-ifs are tested, everything the checker can say, sixteen translator rules, what is outside the language, traps. Supersedes 36, and the rulebooks 34, 33, 23, 20 before it. Handed to a translator together with [39 Prompt - translate a text into the ledger language](<authority/39 Prompt - translate a text into the ledger language.md>), never alone.
- **Built:** two checker rigs on s(CASP), joined by a bridge, in [rigs/](rigs/). Rig 1 checks arguments; rig 2 checks causes written as pressing patterns in five slots. Sixteen logged patches on rig 1 and three on rig 2, each with what it gives up ([project story](<records/Checked reasoning language - project story.md>), "What each patch gave up").
- **Tested on:** five of Claude's paragraphs, three of the owner's (ball and coin, Markus, Mondays), 21 of the other model's audit cases, and a blind sample of eight of its literary texts (seven matched its keys). Every run had its plan frozen first.
- **Strength of evidence:** the translating has always been Claude's. "Not tested: a translator other than Claude" appears in every results file.
- **Audited from outside (log 45):** the other model's audit of 38 and 39 is in [results/](results/), unchanged: fifteen findings on the wording, twelve repairs, sixty new texts, six of its own translations, nothing run. Four findings hold up against the text (F01, F02, F04, F15). [Plan 45](<tests/45 Test plan - the 38 and 39 audit package, ledgers compared and findings sorted.md>) is frozen and not yet run: compare its six ledgers with Claude's, and sort the fifteen findings by running their cases.
- **Live instruction:** [46](<tests/46 Next instruction for the other model - translate the eight texts of plan 37.md>) - the eight texts of plan 37 for the other model to translate under 38 and 39, so the comparison runs both ways. Not yet sent.
- **Execution attempt (log 58):** the other model tried plan 45 and was blocked by the missing runtime; its attempt is kept in [results/](results/). The runtime now runs here and reproduces the recorded T05-B run.
- **Handoff (L60):** a new agent runs plan 45 from [the brief](<tests/L60 Handoff - a new agent runs plan 45.md>); the tools it needs are in `tools/`.
- **Next step (from the log):** the new agent's return; or run plan 45 here; paste 46.

## Where to start
This thread keeps its own record in [records/](records/) from 21 September 2026 (log, Decisions, Lessons, Status); its [READ ME FIRST](<records/READ ME FIRST.md>) says how it relates to the shared record the three projects began with, which is kept unchanged in the same folder. Its claims about the other projects are in [RELATIONS.md](RELATIONS.md); worked examples on its files are in [tutorials/](tutorials/).

[INDEX.md](INDEX.md) for the timeline. [ORIGIN.md](ORIGIN.md) for the goal in the owner's words and the twelve properties. For the language itself, file 38. For what the checkers actually do, `rigs/READ ME FIRST.md`.

## What is in this folder
```
ORIGIN.md      the goal, the twelve properties, how the pieces fit
records/       this thread's own log, Decisions, Lessons and Status, from 21 September 2026; beside them the shared record the three projects began with, unchanged
RELATIONS.md   this project's claims about its connections to the other two, with status and evidence
tutorials/     three worked examples on this project's files: reading an authority, following a test, reading a result
INDEX.md       every research state from the first theory to file 39, with what is and is not here
authority/     38 (the language), 39 (the translator's task)
tests/         frozen plans: 21 Markus, 22 Mondays, 35 the third pile, 37 the blind sample, 45 the audit of 38 and 39; 46 the next instruction for the other model
results/       21 and 22 (html pages), 37 (md): what happened, with predictions ticked; 45: the other model's package, as received
rigs/          the working checkers, frozen and patched, every ledger, the bridge, and raw_log.txt
tools/         sameness.py (the sameness test as a program), install_scasp.sh and the expected smoke report
```
`rigs/` is this project's own addition to the shared layout: the rig is at once the build of the theory, the apparatus for every test, and (in `raw_log.txt` and the ledgers) the raw evidence.

## Rules of this project
- **To write a ledger:** follow the language definition (38). If something will not fit, put it in the bin with the reason, and log it as a candidate new kind of line.
- **To change the checker:** never edit the frozen copy. For every patch, record what it gives up as well as what it fixes. Change the patched copy, log the patch with the paragraph that forced it and the layer it changed, then rerun every ledger.
- **Before any build:** merge the theory into one page and freeze it. The build tests that page only.
- **After a clean sweep:** add cases chosen to break the rig, run them against the frozen copy, label them as added after the plan.
- **Handing things to the other model:** give it file 39 with file 38, never 38 alone.
- **Whose cases:** say whether a result is seen on Claude's own cases or on someone else's.

## Words used in this project
Short form. The authority for these is the word list in the shared project story in `records/`.
- **Prose.** What you write in everyday language.
- **Translator.** The language model that turns prose into a ledger. The only step that guesses; every guess is marked.
- **Ledger, line.** Your text in the formal language; one line per thing you committed yourself to. Every line has five fixed parts: number, standing, content, source mark, sentence.
- **Standing.** Whether a line is the point of its sentence (CLAIMED), taken for granted (GIVEN), only supposed for a what-if (SUPPOSED), or told inside a named story-world (TOLD).
- **Source mark.** Who put the line there: said / filled in / usual case.
- **Checker.** A program with fixed rules that reads a ledger. Never guesses.
- **Finding.** What the checker returns: a contradiction, a jump, a kind mistake, a part that does no work, a counter-case, "cannot tell", "not checked".
- **Read-back, report.** Fixed rules that turn findings into prose; the findings after read-back.
- **Leftover bin.** Prose that could not be written as lines. Not checked, always listed.
- **Rig.** The driver (a small program that decides what to ask, takes lines out, writes the report) and the checker rules together, on s(CASP). **Rig 1** is for arguments; **rig 2** for causes written as pressing patterns; the **bridge** joins them.
- **Frozen / patched.** The rig as it stood when frozen, with fingerprints kept / the working copy with every change logged. A **patch** is any change after the freeze, and each patch records what it gives up.
- **MAKES / SHOWS.** A line that says what produces a thing / a line that says how we can tell.
- **MAKES / LETS / STOPS / DESPITE.** The basic causal words of rig 2, each defined by how five slots are filled.
- **BECAUSE / SINCE.** What produced it / a reason to expect or believe it. Different tests run on each.
- **What-if.** Asking whether the result would still have happened with a cause taken away, or a line changed.

## Traps
- **The rig bundle matches no older results file.** It holds the checkers as they are now. The results files say what the checkers said on the day.
- **A clean report means the lines fit together**, not that the reasoning is right. On a story it may only mean "not the kind of text the checker was built for".
- **Patches 4 and 5 are not general.** Each was forced by one paragraph.
- **Both drivers point at the machine the rigs were built on.** `run_check.py` and `check2.py` call `/home/claude/sCASP/scasp`, and the joined script reads `/home/claude/rig2/patched/laws.pl`. To run elsewhere, put s(CASP) at that path (a symlink does) or change the one line; this is what blocked the other model's execution attempt (log 58).
- **Compare reports without the GAUGE line.** It carries timings that change run to run.
