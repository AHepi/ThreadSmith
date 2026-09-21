# Legend - how to read the names

Filenames are the owner's and Claude's, kept exactly as they were made. This page decodes them. A reader should never have to remember it: every INDEX uses the descriptive name beside the number.

## The numbered files
```
NN Kind of artifact - what it is about.ext
^^ ^^^^^^^^^^^^^^^^   ^^^^^^^^^^^^^^^^^^  ^^^
|  |                  |                   file type
|  kind of artifact   subject
log entry number
```
- **The number** is the entry in a project story's log under which the file was made. It is a sequence, not a version. Two files with the same number were made in the same entry (a test plan and its results; an instruction and the guide to it).
- **Each project counts on its own.** The numbers were one sequence across the projects while they shared one record (to 59), so a project's numbers below 60 have gaps where another project's entries fall. Since the split, a new entry carries the project's letter and one more than the highest number that project's log has used, and a file made under it is named the same way ("H55 ..."). Nothing another project has numbered is looked at. (The first entries after the split, S60 to S64 and L60 to L65, were numbered against the shared sequence under an earlier rule; they stand as they are.) New decisions and lessons in a project's own record start at 1 with the letter. The letter says the project; the number says where in that project's log.
- **A higher number supersedes a lower one of the same kind.** Superseded files are named in the log entries that replaced them and may be left out of a folder on purpose; each INDEX marks what is missing with "not in bundle" and the entry that describes it.
- **The kinds** that appear: Test plan (frozen before a run), Test results and Results (what happened), Plan and Addendum (a design and what was fixed before running it), Marking plan (how replies are marked, frozen before reading), Pilot results and Corpus run (a run as it happened, before any reading), Next instruction for the other model (a round handed to the outside model), Workflow and Owner's guide (an instruction pair), Skill, Prompt, Theory, Rulebook, Reference, Corpus, Return (something received, kept unchanged).
- **Two files with the same number and kind** are the same artifact in two forms (a text and its archive, a plan and its rig).

## The record files
A project's `records/` holds four files with no number: `<Project> - project story.md` (the log), `- Decisions.md` (the owner's words), `- Lessons.md` (only failures), `- Status.md` (the summary), and a read-me saying how the record relates to the shared history. They are overwritten in place and only ever appended to. The shared history the projects began with is four files of the same shape named "Checked reasoning language - ...", kept complete and unchanged in the project it began with.

## Inside a rigs folder
Each project with a `rigs/` folder keeps a read-me there that decodes its own names: which programs are drivers and which are rules, how runs and ledgers are named, what a frozen copy and a patched copy are, and which lines of a raw log to leave out when comparing runs.

## File types
`.md` plain text. `.html` a results page written for reading in a browser. `.skill` a zip archive in the format Claude skills are uploaded in; also unpacked beside itself. `.pl` s(CASP) / Prolog. `.json` data. `.jsonl` one record per line. `.py` Python. `.zip` a received bundle, kept only when it is the form something was received in.

## An example, decoded
`NN Test plan - the owner's paragraph.md`: made under log entry NN; a frozen plan; about that paragraph. Its pair is `NN Test results - the owner's paragraph.html`, what happened. The log entry NN in the project's story is the short account; the project's INDEX row for that state links both.
