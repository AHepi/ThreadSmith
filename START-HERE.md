# Start here

You do not need to know Git, or any of the history, to read this repository. This page says how any project here is laid out, who is in it, and how to read it. What each project is about is on its own README, linked from [README.md](README.md).

## Who is who
- **The owner.** Sets the questions, supplies the material, makes the decisions. A project's Decisions file holds their words as written.
- **Claude.** Does the building, translating, testing and record-keeping. Where a case is Claude's own, the record says so ("seen, on my own cases" / "on someone else's").
- **The other model.** A second language model used from outside: to audit, to translate, to try to break what Claude built. Its returns are kept as they came, in a project's `results/`, and read in the project's log.
- **A reader under test.** A model given an artifact and a task and never the answer key. Its runs are kept as they came in a project's `rigs/`.

## The shape of a project
```
README.md      front door: what it is, where it stands, its rules, its words, its traps
ORIGIN.md      where it began, in the owner's words
INDEX.md       the timeline: each research state with its story, test, raw result, interpretation, lessons
RELATIONS.md   the project's claims about its connections to the other projects, with status and evidence
records/       the project's own log, Decisions, Lessons, Status, and a read-me
authority/     the thing under test, frozen once used; a new version is a new numbered file
tests/         frozen plans, written before a run and not edited after
results/       what happened, kept as it came, with predictions ticked and "not tested" named
rigs/          (optional) the working apparatus and the raw evidence of every run
tutorials/     (optional) worked examples on the project's own files
```

## Three ways to read
**New reader.** This page -> [GLOSSARY.md](GLOSSARY.md) -> [tutorials/](tutorials/) -> a project's `README.md`.

**Research review.** A project's `INDEX.md` -> its authority -> a test plan -> the result -> the log entry and lesson that followed, in the project's `records/`.

**Agent or checker.** A project's `INDEX.md` -> the exact files it names -> the raw evidence in its `rigs/` or `results/` -> [RESEARCH-CONVENTIONS.md](RESEARCH-CONVENTIONS.md).

## Two things to know before reading any result
1. **A test plan is frozen before its run.** Files called "Test plan" or "Plan" say what was expected, written first and not edited after. Files called "Test results" or "Results" say what happened. Read them as a pair.
2. **Every result names what it did not test.** A clean report is not a pass mark. Read the "Not tested" lines.

## Traps
- **Reading a project's apparatus as matching an older result.** A `rigs/` folder holds the apparatus as it is now; an older results file says what it said on the day.
- **Reading the shared history as a project's current record.** The record the projects began with is kept, complete to its last shared entry, in the project it began with; each project's own `records/` is where its record continues.
- **Numbering a new file by a number seen in another project.** Each project counts on its own from its own log's highest number; the numbers below 60 interleave only because the projects once shared one record. The rule is in [LEGEND.md](LEGEND.md).
- **Editing a file in another project's folder while working in one.** Read it and link it; change nothing there. The root is the only shared surface.
