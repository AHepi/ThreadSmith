# Research conventions

The rules every project in this repository follows. A project may add rules of its own; those are in its README under "Rules of this project", never here.

## The shape of a project
- **Folders name kinds, not versions.** `authority/`, `tests/`, `results/`, `records/`, and optionally `rigs/` and `tutorials/`. A new authority version is a new numbered file beside the old one, never a `v2/` folder.
- **Every project has** a README (front door), ORIGIN (where it began), INDEX (the timeline of research states), RELATIONS (its claims about the other projects), and `records/` (its log, Decisions, Lessons, Status, and a read-me).
- **A numbered file lives in exactly one place,** chosen by what it is about. If it belongs to two projects, it lives where its number was made and the other project's INDEX links to it.
- **Nothing project-specific lives at the root.** The root holds navigation and these conventions only.
- **Work on one project edits only that project's folder.** Nothing in another project's folder is changed, however small, and nothing at the root unless the owner is changing the conventions themselves. What a project needs from another it reads and links; what it claims about another goes in its own RELATIONS.md. The root is the one shared surface, conventions and navigation, for when the projects come together later.

## The record
- **The log is the record.** Every piece of work is a numbered entry in the project story: what was asked, what was done, what came out, what was not tested, and the output files, which take the entry's number. The log is added to, never rewritten.
- **Decisions holds the owner's words** as written, and nothing else. **Lessons holds only things that failed** while being built or tested, and how each was fixed. **Status is the summary** and drifts from the log at its peril.
- **To edit the documentation:** add a log entry, update Status, add to Decisions or Lessons if one applies.
- **Numbering is each project's own.** A new entry takes the project's letter and one more than the highest number that project's log has used, whatever the other projects have done since; check that log's highest number before the first new file, not only at the start of a chat. A number seen in another project means nothing here (see [LEGEND.md](LEGEND.md)).
- **Starting a new chat:** read the project's `records/` read-me and its Status first, then the newest numbered file in its log.

## Tests and results
- **Before any test or research:** freeze the predictions as their own numbered file first. A test plan is written before the run and not edited after.
- **Every result names what it did not test.** A clean report is not a pass mark.
- **Raw evidence is never edited.** Files under `results/` and `rigs/` are kept as they came. Reinterpret in a new file or a log entry. A return from another model or a reader is kept unchanged, named by the log entry that received it, with the reading kept outside it.
- **Whose cases:** say whether a result is seen on Claude's own cases or on someone else's.
- **Every patch records what it gives up** as well as what it fixes. A frozen copy is never edited.
- **Third-party texts fetched for a test are not kept;** what rebuilds them (a manifest and a fetcher) is.

## Working with other models
- **The other model** is handed positive instructions with a closing line, and its return is brought back whole. Each project's README says what it may and may not be given.
- **A reader under test** is never shown an answer key or a source's standing. Every run is saved as it came, with its finish reason; an empty return is kept and run once more, recorded as a second attempt. Keys and credentials are read from the environment and written to no file.
- **Start only after the owner's word.** Work is planned, the plan is shown, and the run waits for the go-signal for each phase.

## Changing things
- **To change a project file:** check Decisions first; make the change as a new numbered file; never overwrite an old numbered file.
- **RELATIONS.md is a ledger, not a diagram.** Entries are added, updated or marked rejected; never removed. A claim lives in the project that makes it.
- **Each INDEX marks what is missing.** A research state whose files are not in the repository is still listed, with "not in bundle" and the log entry that describes it.
- **Bundles are not kept as files.** Their contents are here unpacked, and their import is a commit in git history. An archive is kept beside its unpacked copy only when that archive is the form the thing is used in.
