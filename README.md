# Checked reasoning language - research repository

One repository for three related, evolving research programs, run by the owner with Claude, and audited from outside by a second language model ("the other model").

| Folder | What it holds | One line |
| --- | --- | --- |
| [Semantics/](Semantics/) | The audit of the authority document, "Claude Fable Semantics - standalone theory" | A theory of what it takes for something to count as an explanation, and the rounds of outside audit that try to break it |
| [Language/](Language/) | The ledger language, its checker rigs, tests and results | A formal language that everyday reasoning prose can be turned into, so that a fixed-rule checker can find the faults |
| [HV Skill/](<HV Skill/>) | The hard-to-vary skill and its unrun test | A Claude skill for testing whether an explanation is hard to vary (Deutsch), sharpened with the semantics |

The three sit beside one another. How they relate is itself a research question; see [RELATIONS.md](RELATIONS.md).

## Where to start
- New to all of it: [START-HERE.md](START-HERE.md), then [GLOSSARY.md](GLOSSARY.md), then [tutorials/](tutorials/).
- Reviewing the research: [records/](records/) holds the record of the whole project. Its [READ ME FIRST](<records/READ ME FIRST.md>) says what to read in what order; the [project story](<records/Checked reasoning language - project story.md>) is the log; [Status](<records/Checked reasoning language - Status.md>) is the summary.
- Decoding a filename: [LEGEND.md](LEGEND.md).
- The rules the work is done under: [RESEARCH-CONVENTIONS.md](RESEARCH-CONVENTIONS.md).

## The tree
```
README.md, START-HERE.md, GLOSSARY.md, LEGEND.md, RELATIONS.md, RESEARCH-CONVENTIONS.md
records/       the four record files (project story, Decisions, Lessons, Status) and the bundle read-me
tutorials/     four short worked demonstrations on real files
Semantics/     README, ORIGIN, INDEX; authority/ (note: not in bundle); tests/ (the audit workflow and rounds); results/ (not in bundle)
Language/      README, ORIGIN, INDEX; authority/ (the language, the translator prompt); tests/; results/; rigs/ (the working checkers)
HV Skill/      README, ORIGIN, INDEX; authority/ (the skill, unpacked and as .skill); tests/ (plan 42, corpus 43); results/ (not yet run)
```
Each project has the same shape: `README.md` (front door), `ORIGIN.md` (where it began), `INDEX.md` (its ledger of research states, with links), and shallow folders named by artifact kind, never by version. Folder names describe what a thing is; the files and indexes say which version and state it belongs to.

## How this repository came to be
The earlier contents of `main` (a Rust workspace, ThreadSmith) were removed on 21 September 2026 at the owner's request; they remain in git history before commit `06aef52`.

The research files arrived as two zip bundles, both made on 20 September 2026:
- `Language.zip` (12:28): twenty files plus a read-me.
- `Semantics.zip` (12:35): the same twenty, byte for byte, plus three later documents (41, 42, 43), with the four record files and the read-me brought up to date.

The first was imported as one commit and the second on top of it, so the earlier state of the record files is in history. Despite their names, neither bundle was specific to one project: both held the whole set. The files were sorted into the three folders here by what each is about; the [project INDEX](Language/INDEX.md) files say where every file went and why.

Not in either bundle, and so not here: the authority document itself (file 10, and its revised version 20), most of the other model's outputs (its amendments, audit package, Stage A and Stage B tables, rulebook audit V3), and the earlier numbered files the read-me lists as superseded and left out on purpose. Each project's INDEX marks these. Added after the bundles, on 21 September: the other model's audit of files 38 and 39 (`Language/results/45 ...`), which also carries the 324-input literary corpus of log 37.

The structure follows a written proposal for a human-first research repository (research lineage: authority -> story -> test -> raw result -> interpretation -> lessons). Naming, numbering and conventions remain the owner's; see LEGEND.md and RESEARCH-CONVENTIONS.md.
