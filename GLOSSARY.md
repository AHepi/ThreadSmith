# Glossary

Short definitions, in two parts: words for the repository, then the project's own words. For the full project word list see the [project story](<records/Checked reasoning language - project story.md>), section "Word list", which is the authority for the second part. The hard-to-vary skill keeps its own list mapping the semantics' terms to plain words: [word-list.md](<HV Skill/authority/hard-to-vary/references/word-list.md>).

## Words for the repository
- **Authority.** The thing actually under test at a research state: the theory page, the language definition, the skill file. Once used in a recorded test it is preserved, never silently changed. Lives in a project's `authority/`.
- **Story.** Intent before evidence: what was wanted, expected, and uncertain at a stage. In this project the intent is written into each frozen test plan and into the log entry that opens a stage, so the projects have no separate `story/` folder yet.
- **Test.** A frozen plan: the cases and the predictions, written before the run and not edited after. Lives in `tests/`.
- **Raw result.** The untouched record of what happened: `raw_log.txt` in a rig, a ledger as written, a results page kept as it came. Lives in `results/` or `rigs/`.
- **Interpretation.** What the result appears to show, with its uncertainty. Here it sits in the "Test results" files and in the log entry for that run.
- **Lesson.** Something that failed while being made or tested, and how it was fixed. Only failures. Lives in [Lessons](<records/Checked reasoning language - Lessons.md>).
- **Decision.** The owner's instruction, in the owner's words as written. Lives in [Decisions](<records/Checked reasoning language - Decisions.md>).
- **Record.** The four files that are the running account of the whole project: project story (the log), Decisions, Lessons, Status. Appended to, never rewritten. Lives in `records/`.
- **Relation.** A suspected connection between two of the three projects, with its status and evidence. Lives in [RELATIONS.md](RELATIONS.md).
- **Bundle.** One of the two zip files the repository was built from. See README.
- **The other model.** The second language model used as an outside auditor and, later, as a second translator.

## The project's own words (short form)
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
- **The eight marks.** Held / held if / two routes / loose / idle / borrowed / fixed / unknown: how firmly a part of an explanation is held in place.
- **Seen / claimed / worked out / recalled.** How a thing about a tool is known. Seen: watched it happen. Claimed: a source says so. Worked out: follows from tagged things. Recalled: memory only. "Seen" is further marked "on my own cases" or "on someone else's".
- **Case (audit).** A short described situation about ordinary things, with a thoughtful person's verdict and the theory's verdict, condition by condition. A **break** is where the two differ and the difference survives the best reply on the theory's behalf.
- **Pair, near case, gauge (audit).** For a phrase that asks the reader to judge: two picturable changes, one showing it met and one unmet; a case that sits close to the line between them; the list of phrases still marked BORROWED: JUDGEMENT.
- **Passage, answer key, setup, control (DeepSeek test).** What the reader under test is sent; what its reply is marked against, which it never sees; what it is given alongside the case; a sound case there to catch a reader that criticises everything.
