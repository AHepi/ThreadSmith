# Start here

You do not need to know Git, or any of the history, to read this repository. This page says what it is, who is in it, and where to go next.

## Three projects, not one
This repository is three separate research projects, each in its own folder. They quote one another, and one shared record logs all three, but each has its own question, its own authority, its own tests and its own next step.

- **Semantics/** - a theory of meaning, "Claude Fable Semantics - standalone theory", which says what it takes for something to count as an explanation and what a "kind" is. The project is the audit of that theory: rounds of described situations, handed to the other model, where the theory's verdict and a thoughtful person's verdict might come apart. The theory is the authority the other two projects quote.
- **Language/** - a way to check reasoning. You write a few sentences in ordinary prose. A translator (a language model) turns them into short, fixed-form lines called a ledger. A checker (a program with fixed rules, never guessing) reads the ledger and finds where the lines clash, where a step is a jump, where a thing is treated as the wrong kind of thing. A read-back turns the findings into plain words that point at your own sentences. Anything that could not be written as lines goes into a leftover bin, and the bin is always listed.
- **HV Skill/** - a Claude skill for asking "is every part of this explanation doing work?" ("hard to vary", from David Deutsch), sharpened with the semantics. It was the method the other two projects were built with, and it is now a project of its own: tested on 49 outside documents read by DeepSeek V4.1 Flash, with file 54 saying where its words break.

## Who is who
- **The owner.** Sets the questions, supplies the paragraphs, makes the decisions. The Decisions file holds their words as written.
- **Claude.** Did the building, translating, testing and record-keeping. Almost every case so far is Claude's own; the record says so where it matters ("seen, on my own cases" / "on someone else's").
- **The other model.** A second language model, given the theory and a workflow, asked to audit it and try to break it. Its outputs are quoted in the log; its audit of 38 and 39 is in `Language/results/`.
- **The reader.** DeepSeek V4.1 Flash, given the skill and one document at a time and never the answer key, in the HV Skill test. Its 147 reports and twelve dialogues are in `HV Skill/rigs/`.

## Where each project stands, one line each
- **Semantics/** - Stage C of the second audit pass is returned (file 57); the live instruction is Stage D's fix cards and the report. The authority (file 10) is in the repository; the revised version the other model audits (file 20) is not.
- **Language/** - the language is one clean file (38) with a translator prompt (39); two checker rigs on s(CASP); the other model's audit of 38 and 39 is in hand and plan 45 to sort it is frozen, unrun.
- **HV Skill/** - the skill (file 30) tested on outside papers; file 54 names two breaks, one gap and three held changes; the repeatability run is the next step, on the owner's word.

## Three ways to read
**New reader.** This page -> [GLOSSARY.md](GLOSSARY.md) -> [tutorials/](tutorials/) -> a project `README.md`.

**Research review.** A project's `INDEX.md` -> its authority -> a test plan -> the result -> the log entry and lesson that followed. The whole log is in [records/](records/).

**Agent or checker.** A project's `INDEX.md` -> the exact files it names -> raw evidence in `Language/rigs/` (`raw_log.txt`, the ledgers) and `HV Skill/rigs/` (the runs and the marks) -> [RESEARCH-CONVENTIONS.md](RESEARCH-CONVENTIONS.md).

## Two things to know before reading any result
1. **A test plan is frozen before its run.** Files called "Test plan" say what was expected, written first and not edited after. Files called "Test results" say what happened. Read them as a pair.
2. **Every result names what it did not test.** A clean report is not a pass mark. Read the "Not tested" lines.

## Traps
The bundle read-me and the project story each keep a Traps list. Two matter most on first reading:
- The record files in `records/` are named "Checked reasoning language" but they record all three projects; the name is the first project's, kept. "The goal" and "Where things stand" in the project story are the Language project's and still describe it as it was around log 17. The log is the record.
- The rig bundle holds the checkers as they are **now**. An older test write-up says what the checkers said on that day.
