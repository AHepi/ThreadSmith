# Glossary

The words used for the repository itself. Each project keeps its own words in its README ("Words used in this project"); the authority for a project's words is the project's own files.

- **Project.** One folder at the root, with the standard shape (see [START-HERE.md](START-HERE.md)). Three exist; each is separate, with its own authority, record and next step.
- **Authority.** The thing actually under test at a research state. Once used in a recorded test it is preserved, never silently changed; a new version is a new numbered file. Lives in a project's `authority/`.
- **Research state.** One row of a project's INDEX: a story (what was wanted and expected), a test, a raw result, an interpretation, and the lessons that followed.
- **Story.** Intent before evidence: what was wanted, expected and uncertain at a stage. Written into each frozen test plan and into the log entry that opens a stage.
- **Test.** A frozen plan: the cases and the predictions, written before the run and not edited after. Lives in `tests/`.
- **Raw result.** The untouched record of what happened: a raw log, an output file as written, a return kept as it came. Lives in `results/` or `rigs/`.
- **Interpretation.** What the result appears to show, with its uncertainty. Sits in the results file and in the log entry for that run, never inside the raw result.
- **Not tested.** The lines in every results file that name what the run did not exercise. A clean report without them is not a result.
- **Lesson.** Something that failed while being made or tested, and how it was fixed. Only failures. Lives in a project's `records/`.
- **Decision.** The owner's instruction, in the owner's words as written. Lives in a project's `records/`.
- **Record.** The four files that are the running account of a project: project story (the log), Decisions, Lessons, Status. Appended to, never rewritten. Lives in `records/`.
- **Log entry.** One numbered paragraph in the project story: what was asked, what was done, what came out, what was not tested, and the output files, which take the entry's number.
- **Relation.** A claim about a connection between this project and another, with its status and evidence. Lives in the project's RELATIONS.md.
- **Rig.** The working apparatus of a project: programs, rules, the runs they produced, and the raw log of every question and answer. Lives in `rigs/`.
- **Frozen / patched.** The apparatus as it stood when a test was run, kept with fingerprints / the working copy with every change logged. A **patch** is any change after a freeze, and each patch records what it gives up.
- **Seen / claimed / worked out / recalled.** How a thing is known. Seen: watched it happen. Claimed: a source says so. Worked out: follows from tagged things. Recalled: memory only. "Seen" is further marked "on my own cases" or "on someone else's".
- **The owner, Claude, the other model, a reader under test.** The four roles; see [START-HERE.md](START-HERE.md).
- **Bundle.** A zip in which a set of files arrived. Their contents are here unpacked; the imports are commits in git history.
