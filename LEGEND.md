# Legend - how to read the names

Filenames here are the owner's and Claude's, kept exactly as they were made. This page decodes them. A reader should never have to remember it: every index uses the descriptive name beside the number.

## The numbered files
```
38 The ledger language - complete definition.md
^^ ^^^^^^^^^^^^^^^^^^^   ^^^^^^^^^^^^^^^^^^^  ^^
|  |                     |                    file type
|  kind of artifact      what it is about
log entry number
```
- **The number** is the entry in the project story's log under which the file was made. It is a sequence, not a version. Two files with the same number were made in the same entry: `21 Test plan` and `21 Test results` belong to the Markus paragraph; `24 Workflow` and `24 Owner's guide` are the audit pair; `38 The ledger language` and `38 Checker rigs` were produced together.
- **A higher number supersedes a lower one of the same kind.** The language file 38 supersedes 36, which superseded rulebooks 34, 33, 23 and 20. The skill file 30 supersedes 29, 22, 21, 17, 14, 11, 10, 08 and 05. Superseded files were left out of the bundles on purpose; the log entries describe them.
- **Numbers 37, 38 and 39 were used twice** for a while: a later chat, starting without the files, reused them. Its three documents were renumbered 41, 42 and 43 before import, and the numbers inside them corrected (Lesson 37). **Numbers 45 to 52 were used twice** the same way by the chat that ran the skill test; its files are here as 47 to 54, decisions 37 to 43, with every reference rewritten (Lesson 48).
- **The kinds** that appear: Test plan (frozen before a run), Test results and Results (what happened), Plan and Addendum (a design and what was fixed before running it), Marking plan (how replies are marked, frozen before reading), Pilot results and Corpus run (a run as it happened, before any reading), Next instruction for the other model (an audit round), Workflow and Owner's guide (the audit pair), Skill, Prompt (a translator's task), Corpus (cases with answer keys), Checker rigs. Kinds named in the log but not in the bundles: Theory, Research plan, Research, Reference, Rulebook.

## The record files
`Checked reasoning language - project story.md`, `- Decisions.md`, `- Lessons.md`, `- Status.md` carry no number. They are overwritten in place and only ever appended to. The **log** in the project story is the record; Status is the summary; Decisions holds the owner's words; Lessons holds only failures.

## Inside the rigs (`Language/rigs/`)
- `rig 1 - arguments/`, `rig 2 - causes/`: the two checker set-ups. `frozen/` is untouched since the freeze, with `fingerprints.txt` (SHA-256 of the frozen files and the time). `patched/` is the working copy. `joined/` runs rig 1's driver with rig 2's laws and `bridge.pl` added.
- `run_check.py` (rig 1) and `check2.py` (rig 2) are the drivers; `checker_rules.pl` and `laws.pl` the fixed rules s(CASP) uses.
- `..._before_pile2.py`, `..._before_F.txt` and the like: a copy of a file as it stood before a named change, kept so reports can be compared.
- **Ledgers** come in pairs: `ledger_X.json` is the ledger as data (paragraph, sentences, lines with their marks, the bin, what-ifs); `ledger_X.pl` is the same ledger as s(CASP) facts, one `line(N).` per line so a line can be taken out.
- **Ledger letters.** Each ledger's `"paragraph"` field names its text, and rig 2's `"whose"` field says whose it was. The letters are per rig and do not line up across the two.
  - Rig 1: `A` tomato, `A2` tomato with "always" softened to "usually", `B` buses, `C` henhouse, `D` lateness, `E` letter, `F` ball and coin (the owner's), `G` Markus (the owner's), `H` abolish Mondays (the owner's), `J` the owner's ball sentences with both rigs joined. `K..` the other model's audit cases, numbered after its findings (K04 is finding F04; `b` marks a second form; KX and K22b are hostile cases added after the clean sweep). `T..` its literary texts by family and text: T05B is family 5, base text; T05D its contrasting text.
  - Rig 2: `A` ball and coin (the owner's, second form), `B` rope and cart, `C1` to `C4` four one-sentence pushes and drops, `D` people and rules, `E` the ball bounced back faster, `F` the owner's paragraph with three what-ifs added by Claude, `G` Markus (the happening only), `K01` the audit's F01 box case, `X1` and `X2` cases Claude added after the plan, chosen to break the rig.
- `raw_log.txt`: every question put to the checker and its full answer, in order. Leave out the GAUGE line when comparing runs; it carries timings.

## Inside the skill rigs (`HV Skill/rigs/`)
- `runs/<source>-m<mode>.json`: one DeepSeek return; `source` is the id in `sources.json` (S1 to S18 science, E economics, P philosophy, C computability, F fiction, D design, R rules, I instructions; `b` a paired critique), `mode` 0 no skill, 1 skill pasted whole, 2 router live. `conv/<source>-conv.json`: a conversation dialogue with its report.
- `marking/to_mark.md` is what the marker saw (labels hidden); `secret_mapping.json` restores them; `close_marks_restored.json` is the marks with the labels back. See `HV Skill/rigs/README.md`.

## File types
`.md` plain text. `.html` a results page written for reading in a browser. `.skill` a zip archive in the format Claude skills are uploaded in; it is also unpacked beside itself. `.pl` s(CASP) / Prolog. `.json` data. `.py` Python.

## Three examples, decoded
- `22 Test plan - your Mondays paragraph.md`: made under log 22; a frozen plan; for the owner's Mondays paragraph. Its pair is `22 Test results - your Mondays paragraph.html`.
- `41 Next instruction for the other model - finish Stage B and near cases.md`: log 41 (the later chat); an audit round to hand to the other model; asks it to finish its Stage B table and hold each pair against a near case. Returned (log 55); 57 is the live one; 27, 28, 30, 41 and 55 are rounds already run.
- `Language/rigs/rig 1 - arguments/ledger_T07B.json`: rig 1; the other model's literary text, family 7, base text; the ledger as data. Its run is in `raw_log.txt`; its reading is in `37 Test results`.
