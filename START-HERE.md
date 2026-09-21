# Start here

You do not need to know Git, or any of the history, to read this repository. This page says what it is, who is in it, and where to go next.

## The story in one paragraph
The owner wants a way to check reasoning. You write a few sentences in ordinary prose. A translator (a language model) turns them into short, fixed-form lines called a ledger. A checker (a program with fixed rules, never guessing) reads the ledger and finds where the lines clash, where a step is a jump, where a thing is treated as the wrong kind of thing. A read-back turns the findings into plain words that point at your own sentences. Anything that could not be written as lines goes into a leftover bin, and the bin is always listed. That is the **Language** project. The theory of meaning that says what counts as an explanation, and what a "kind" is, is the **Semantics** project: it is the authority document everything else quotes. The method used to build and criticise all of this, "is every part of this explanation doing work?", is a Claude skill, the **HV Skill** ("hard to vary", from David Deutsch).

## Who is who
- **The owner.** Sets the questions, supplies the paragraphs, makes the decisions. The Decisions file holds their words as written.
- **Claude.** Did the building, translating, testing and record-keeping. Almost every case so far is Claude's own; the record says so where it matters ("seen, on my own cases" / "on someone else's").
- **The other model.** A second language model, given the theory and a workflow, asked to audit it and try to break it. Its outputs are quoted in the log; its audit of 38 and 39 is in `Language/results/`.
- **The reader.** DeepSeek V4.1 Flash, given the skill and one document at a time and never the answer key, in the HV Skill test. Its 147 reports and twelve dialogues are in `HV Skill/rigs/`.

## The three projects, one sentence each
- **Semantics/** - the audit of "Claude Fable Semantics - standalone theory": rounds of described situations where the theory's verdict and a thoughtful person's verdict might come apart.
- **Language/** - the ledger language, defined in one clean file (38), with two checker rigs built on s(CASP), tests frozen before each run, and results kept as they came.
- **HV Skill/** - the hard-to-vary skill (file 30), improved seven times from what each stage taught, and tested on 49 outside documents read by DeepSeek V4.1 Flash: its words do work in a reader that is not Claude, and file 54 says where they break.

## Three ways to read
**New reader.** This page -> [GLOSSARY.md](GLOSSARY.md) -> [tutorials/](tutorials/) -> a project `README.md`.

**Research review.** A project's `INDEX.md` -> its authority -> a test plan -> the result -> the log entry and lesson that followed. The whole log is in [records/](records/).

**Agent or checker.** A project's `INDEX.md` -> the exact files it names -> raw evidence in `Language/rigs/` (`raw_log.txt`, the ledgers) and `HV Skill/rigs/` (the runs and the marks) -> [RESEARCH-CONVENTIONS.md](RESEARCH-CONVENTIONS.md).

## Two things to know before reading any result
1. **A test plan is frozen before its run.** Files called "Test plan" say what was expected, written first and not edited after. Files called "Test results" say what happened. Read them as a pair.
2. **Every result names what it did not test.** A clean report is not a pass mark. Read the "Not tested" lines.

## Traps
The bundle read-me and the project story each keep a Traps list. Two matter most on first reading:
- "Stage" and "Where things stand" in the project story and in Status still describe the project as it was around log 17. The log is the record.
- The rig bundle holds the checkers as they are **now**. An older test write-up says what the checkers said on that day.
