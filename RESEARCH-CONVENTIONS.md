# Research conventions

The rules the work is done under. The first part is copied from the project story's "How to work on this project" and the bundle read-me, which remain the authority; the second part is what this repository adds so that the tree stays readable.

## The project's own rules (from the record)
- **To read:** start with the project story, then the newest numbered file in the log.
- **To change a project file:** check Decisions first; make the change as a new numbered file; never overwrite an old numbered file.
- **To write a ledger:** follow the language definition (38). If something will not fit, put it in the bin with the reason, and log it as a candidate new kind of line.
- **To change the checker:** never edit the frozen copy. For every patch, record what it gives up as well as what it fixes. Change the patched copy, log the patch with the paragraph that forced it and the layer it changed, then rerun every ledger.
- **Before any test or research:** freeze the predictions as their own numbered file first.
- **Before any build:** merge the theory into one page and freeze it. The build tests that page only.
- **After a clean sweep:** add cases chosen to break the rig, run them against the frozen copy, label them as added after the plan.
- **To edit the documentation:** add a log entry to the project story, update Status, add to Decisions or Lessons if one applies. The log is added to, never rewritten. Decisions holds the owner's words. Lessons holds only things that failed while being built or tested.
- **Every result names what it did not test.** A clean report is not a pass mark.
- **Whose cases:** say whether a result is seen on Claude's own cases or on someone else's.
- **Handing things to the other model:** it reinterprets negative instructions and follows positive ones. Give it file 24 in place of the skill; give it file 39 with file 38, never 38 alone. Never show a reader under test the answer key (files 42, 43).
- **Starting a new chat:** upload the current set first. That is how the numbering clashed (Lesson 37).

## What this repository adds
- **Folders name kinds, not versions.** A new authority version is a new numbered file in `authority/`, beside the old one. Never a `v2/` folder.
- **Raw evidence is never edited.** Files under `results/` and `rigs/` are kept as they came. Reinterpret in a new file or a log entry.
- **A numbered file lives in exactly one place**, chosen by what it is about: Semantics (the authority document and its audit), Language (the ledger language, rigs, translations, their tests), HV Skill (the skill and tests of the skill). If a file belongs to two, put it where its number was made and link from the other project's INDEX.
- **The records stay together** in `records/`, as one set. They span all three projects. Each project's `INDEX.md` cites log entries by number.
- **Each INDEX marks what is missing.** A research state whose files are not in the repository is still listed, with "not in bundle" and the log entry that describes it.
- **Add a story/ folder only when intent starts being written separately** from the frozen test plans. Add `synthesis/` at the root only when the same pattern has been seen across several research states.
- **RELATIONS.md is a ledger, not a diagram.** Entries are added, updated or marked rejected; never removed.
- **The two zip bundles are not kept as files.** Their contents are here unpacked, and their import is two commits in git history. The `.skill` archive is the one exception, kept beside its unpacked copy because that is the form it is uploaded in.
