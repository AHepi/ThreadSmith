# S98 — Proposal: the records lumped by place in the latest text

*Log S98, 26 September 2026, under the owner's instruction of that day (decision S30). One of the proposals for how to lump the ledger's records together; this one groups by **where in the text** their sentences sit. Made by program from `anchored.jsonl` (md5 41752268722000a376a15e7de2bde76e) and `sentence index of the latest text.jsonl` (md5 fdaf069a0c1d71be4e17b38d2f6bce82), both read only. Programs and their outputs are in `proposal by place - scripts/`: `place.py` makes the groups and the measures (`assignment.jsonl`, `sections.json`, `measures.json`), `page.py` writes this page and `groups.json` (each group with its rule and its change ids). A rerun (`PYTHONDONTWRITEBYTECODE=1 python3 place.py v2 > /dev/null && PYTHONDONTWRITEBYTECODE=1 python3 page.py`) gives the same bytes. Nothing is committed.*

## The metric

A change belongs to the stretch of the latest text its sentences sit in: the Part, then the section inside the Part (a `##` heading, or where a Part has none, a paragraph with a bold run-in label, with the unlabelled paragraphs after it), then the sentence. A change whose sentences sit in several sections goes to the section holding most of them, and a vocabulary change spread over three or more Parts goes to one group for the whole text. A change with no sentence in the latest text goes to the section its source names, or else to the section whose wording it shares most (only at a share of 0.5 or more), or else to its Part's group of wording not in the latest text.

The unit placed is the **change** (`change_id`, 1275 of them), so the records that are one change seen in several sources stay together; each record goes with its change. Sections holding fewer than four changes are joined to the section before them in the same Part.

## How it was measured, and the one adjustment

The first cut (v1) used the sections as the text draws them: headings, run-in labels, unlabelled paragraphs joined to the label before them, every change with no sentence put in its Part's residue, and vocabulary changes treated like any other. The adjusted cut (v2) made these changes, all at once, after reading the v1 figures:

1. **Grievances split.** "Grievances, anticipated" held 81 changes in one group with no shared term above a tenth of them; each of the eleven numbered grievances is now its own section.
2. **Unlabelled paragraphs that start a new matter** get their own section instead of riding with the label before them: Part V line 259 (the conjunction (E)), Part X lines 407–411 (representation in use; construction is not selection) and 425 (what a new content may be), Part XI lines 441 (the aims of a repair) and 453 (Result, and the index of (EX)), Part XIV line 520 (what everything else is defined from).
3. **Term-wide changes.** A change of scope term (or whole text) whose sentences sit in three or more Parts has no one place; it goes to the group *Vocabulary across the text* (46 changes). With one or two Parts it follows the majority rule.
4. **Changes with no sentence.** First the section its source names (`target_part` after " / ", or a quoted paragraph name), if that heading or label still stands in the same Part; then the *section lead*: the section of the Part(s) named whose words the change's old and new wording share most, weighted by how rare each word is among sections, taken only at a share of 0.5 or more; otherwise the Part's residue. Notes with no Part join the front matter.
5. **Small sections joined.** v1 had 7 groups of one change and 25 of three or fewer; a section with fewer than four changes now joins the section before it in its Part (the first ones join the next).

| measure | v1 | v2 |
| --- | --- | --- |
| groups | 116 | 109 |
| changes per group: median / largest | 8 / 81 | 9 / 46 |
| groups of 3 or fewer changes | 25 | 5 |
| groups of more than 40 changes | 3 | 2 |
| changes in no group | 0 | 0 |
| changes whose sentences sit in more than one section (records: 89) | 94 | 94 |
| changes with no sentence (181) placed in a section | 0 | 45 |
| changes with no sentence left in a Part residue | 164 | 119 |
| term overlap inside groups (mean Jaccard of the changes' terms) against the same group sizes drawn at random | 0.156 against 0.026 | 0.145 against 0.026 |

Reading the figures:

- **Term overlap.** Changes in one group share their theory terms 6.0 times as much as changes drawn at random in v1 and 5.6 times in v2. The table below leaves out each adjustment in turn: splitting the grievances and giving new matters their own sections raise the overlap; the vocabulary group and the joining of small sections lower it, the first because it gathers renames of different terms, the second because joined neighbours share fewer terms. The joining was kept because 26 groups of one to three changes line up little; the step that joins the proposals can switch it off (`min_changes` 0 in `place.py`) and have 130 groups on the text's own sections.

| cut | groups | term overlap, all groups | term overlap, section groups only | groups of 3 or fewer | largest |
| --- | --- | --- | --- | --- | --- |
| v2 as made | 109 | 0.145 | 0.155 | 5 | 46 |
| without the grievance split | 99 | 0.137 | 0.145 | 5 | 85 |
| without the own sections | 105 | 0.144 | 0.153 | 5 | 46 |
| without the vocabulary group | 110 | 0.153 | 0.158 | 5 | 50 |
| without named section and lead | 109 | 0.145 | 0.158 | 5 | 47 |
| without joining small sections | 130 | 0.158 | 0.170 | 26 | 46 |

- **The section lead** was tried on the 958 placed records whose new wording is not word for word in the latest text: at a share of 0.5 or more it named the section they are placed in for 656 of 722 (91%); under 0.5 for 127 of 236 (54%). Hence the cut at 0.5. For the changes it placed that also carry the anchoring step's lead sentence (`latest_nearest`), the two leads name the same section in 11 of 15.
- **Several places.** 94 changes touch more than one section. 39 of them are vocabulary changes that went to the whole-text group; the other 55 are placed by the majority rule, and on average 55% of their sentences sit in the group they are placed in. The table gives the other groups each one touches.
- **Does each group read as one part of the semantics?** The section groups do: each is a heading or a labelled paragraph the theory itself draws, so someone following the theory finds the group where they are reading. Three kinds of group read less well and are marked below: the joined groups (two to five short sections side by side), the Part residues (proposals the text never took, one bucket per Part; Part V's holds 36 changes from three R2 amendments written against file 20: A on scope, B on dependence, C "Anchor the relevant parts"), and the vocabulary group (one matter, the renaming of terms, but no one place).

## How a change that touches several places is placed

Count the change's sentences (over all its records) by section; it goes to the section holding most of them, and a tie goes to the one that comes first in the text. If the change is a vocabulary change (scope term or whole text) and its sentences sit in three or more Parts, it goes to *Vocabulary across the text* instead. Every other section it touches is listed in the column *also touches* of the assignment table, so reading by place can still find it there; the change itself is counted once.

## The groups

Ids run in text order: `V.3` is the third group of Part V, `V.x` Part V's residue, `FM` the front matter, `ALL` the vocabulary group. *No sentence* counts the changes in the group that have no sentence in the latest text. *Most shared term* is the theory term found in most of the group's changes, with the share of changes carrying it; old names are the ones the S95 vocabulary replaced.

| id | group | lines | rule | changes | records | no sentence | most shared term |
| --- | --- | --- | --- | --- | --- | --- | --- |
| FM | Front matter and notes before Part 0 | 1–3 | The title, the note under it, and the notes that stood before Part 0 in earlier texts (file 11's revision note, the note of sources and departures, the change list's fallback table). | 16 | 16 | 10 | “Repair” (0.31) |
| 0.1 | opening of Part 0 · Two words, as used here | 7–8 | Changes whose sentences sit wholly or mostly in lines 7–8 (2 sections of the text; those holding fewer than four changes are joined to a neighbour). | 6 | 9 | 0 | “argument” (0.67) |
| 0.2 | What this document claims | 9–17 | Changes whose sentences sit wholly or mostly in lines 9–17; with them, changes with no sentence that name this section or share most words with it. | 30 | 50 | 1 | “argument” (0.23) |
| 0.3 | What this document does not claim | 19–27 | Changes whose sentences sit wholly or mostly in lines 19–27; with them, changes with no sentence that name this section or share most words with it. | 22 | 26 | 1 | “worth” (old name) (0.27) |
| 0.4 | What is imported, what is an index, and what is defined | 29–31 | Changes whose sentences sit wholly or mostly in lines 29–31. | 22 | 30 | 0 | “primitive” (old name) (0.50) |
| 0.5 | Grievances, anticipated / introduction | 33–35 | Changes whose sentences sit wholly or mostly in lines 33–35; with them, changes with no sentence that name this section or share most words with it. | 5 | 17 | 3 | “Repair” (0.20) |
| 0.6 | Grievances, anticipated / 1. "Without declared kinds you cannot tell a cause from a correlation." · 2. "So this is operationalism: a thing is what you can do to it." | 37–39 | Changes whose sentences sit wholly or mostly in lines 37–39 (2 sections of the text; those holding fewer than four changes are joined to a neighbour). | 7 | 7 | 0 | “checks” (old name) (0.43) |
| 0.7 | Grievances, anticipated / 3. "If correspondences are selected, you have made fidelity a matter of survival." | 41 | Changes whose sentences sit wholly or mostly in line 41. | 9 | 9 | 0 | “transport” (0.44) |
| 0.8 | Grievances, anticipated / 4. "Then everything is relative to a contract of admitted changes, and nothing is independent of the modeller." | 43 | Changes whose sentences sit wholly or mostly in line 43. | 15 | 18 | 0 | “fact” (old name) (0.33) |
| 0.9 | Grievances, anticipated / 5. "This is teleosemantics, structural realism or functionalism with new words." | 45 | Changes whose sentences sit wholly or mostly in line 45. | 4 | 4 | 0 | “obligation” (old name) (0.50) |
| 0.10 | Grievances, anticipated / 6. "You have replaced explanation with evolution." | 47 | Changes whose sentences sit wholly or mostly in line 47. | 8 | 11 | 0 | “object layer” (0.25) |
| 0.11 | Grievances, anticipated / 7. "Mathematics has no interventions." | 49 | Changes whose sentences sit wholly or mostly in line 49. | 11 | 16 | 0 | “axiom” (old name) (0.36) |
| 0.12 | Grievances, anticipated / 8. "Where is aesthetics?" | 51 | Changes whose sentences sit wholly or mostly in line 51. | 10 | 10 | 0 | “true” (old name) (0.30) |
| 0.13 | Grievances, anticipated / 9. "'Selected' is as much a stipulation as 'is a cause'." | 53 | Changes whose sentences sit wholly or mostly in line 53. | 5 | 6 | 0 | “argument” (0.20) |
| 0.14 | Grievances, anticipated / 10. "Freezing the question for assessment while letting questions change across episodes is having it both ways." | 55 | Changes whose sentences sit wholly or mostly in line 55. | 4 | 5 | 0 | “argument” (0.50) |
| 0.15 | Grievances, anticipated / 11. "Kinds exist. A rule is not a cause." | 57 | Changes whose sentences sit wholly or mostly in line 57. | 4 | 4 | 0 | “obviously” (old name) (0.50) |
| 0.16 | Where to attack this | 59–61 | Changes whose sentences sit wholly or mostly in lines 59–61; with them, changes with no sentence that name this section or share most words with it. | 13 | 15 | 2 | “selected” (0.38) |
| 0.x | Part 0, not in the latest text |  | Changes to Part 0 with no sentence in the latest text that name no section still standing and share too few words with any section of the Part (section lead under 0.5). | 9 | 20 | 9 | “declared” (0.56) |
| I.1 | opening of Part I · Faithfulness without assessors | 65–67 | Changes whose sentences sit wholly or mostly in lines 65–67 (2 sections of the text; those holding fewer than four changes are joined to a neighbour). | 6 | 6 | 0 | “tentatively accept” (0.17) |
| I.2 | Fallibility without error-as-work | 69 | Changes whose sentences sit wholly or mostly in line 69. | 6 | 7 | 0 | “false theory” (old name) (0.50) |
| I.3 | Conjecture, criticism, action · Recursive scrutiny with operative return | 71–73 | Changes whose sentences sit wholly or mostly in lines 71–73 (2 sections of the text; those holding fewer than four changes are joined to a neighbour). | 5 | 5 | 0 | “argument” (0.80) |
| I.4 | Substrate independence with physical conditions · Two provenances, not one | 75–77 | Changes whose sentences sit wholly or mostly in lines 75–77 (2 sections of the text; those holding fewer than four changes are joined to a neighbour). | 12 | 16 | 0 | “adopted” (old name) (0.50) |
| II.1 | opening of Part II · Organizations · Roles are defined, not supplied · Kinds are edit-signatures | 81–127 | Changes whose sentences sit wholly or mostly in lines 81–127 (4 sections of the text; those holding fewer than four changes are joined to a neighbour). | 28 | 36 | 0 | “signature” (0.43) |
| II.x | Part II, not in the latest text |  | Changes to Part II with no sentence in the latest text that name no section still standing and share too few words with any section of the Part (section lead under 0.5). | 6 | 7 | 6 | “declared” (0.17) |
| III.1 | opening of Part III · Contracts | 131–147 | Changes whose sentences sit wholly or mostly in lines 131–147 (2 sections of the text; those holding fewer than four changes are joined to a neighbour). | 4 | 4 | 0 | “contract” (0.25) |
| III.2 | The respect is the query | 149–151 | Changes whose sentences sit wholly or mostly in lines 149–151; with them, changes with no sentence that name this section or share most words with it. | 12 | 32 | 4 | “prediction” (0.33) |
| III.3 | Contracts have provenance | 153–155 | Changes whose sentences sit wholly or mostly in lines 153–155. | 4 | 4 | 0 | “witness” (old name) (0.75) |
| III.4 | Scope, and a question that can be in error | 157–161 | Changes whose sentences sit wholly or mostly in lines 157–161; with them, changes with no sentence that name this section or share most words with it. | 23 | 33 | 1 | “contract” (0.39) |
| III.x | Part III, not in the latest text |  | Changes to Part III with no sentence in the latest text that name no section still standing and share too few words with any section of the Part (section lead under 0.5). | 2 | 2 | 2 | “derive” (old name) (0.50) |
| IV.1 | opening of Part IV · Occurrences and contents · The object layer and the simulation layer · Transports | 165–189 | Changes whose sentences sit wholly or mostly in lines 165–189 (4 sections of the text; those holding fewer than four changes are joined to a neighbour); with them, changes with no sentence that name this section or share most words with it. | 8 | 8 | 1 | “expectation” (old name) (0.25) |
| IV.2 | Three provenances | 191–201 | Changes whose sentences sit wholly or mostly in lines 191–201; with them, changes with no sentence that name this section or share most words with it. | 16 | 25 | 3 | “transport” (0.25) |
| IV.3 | Representation is defined, not supplied | 203–213 | Changes whose sentences sit wholly or mostly in lines 203–213; with them, changes with no sentence that name this section or share most words with it. | 12 | 16 | 2 | “derive” (old name) (0.42) |
| IV.4 | Prediction, surprise, violation | 215–225 | Changes whose sentences sit wholly or mostly in lines 215–225; with them, changes with no sentence that name this section or share most words with it. | 27 | 45 | 2 | “surprise” (0.56) |
| IV.x | Part IV, not in the latest text |  | Changes to Part IV with no sentence in the latest text that name no section still standing and share too few words with any section of the Part (section lead under 0.5). | 10 | 23 | 10 | “surprise” (0.30) |
| V.1 | opening of Part V | 229–231 | Changes whose sentences sit wholly or mostly in lines 229–231; with them, changes with no sentence that name this section or share most words with it. | 14 | 23 | 3 | “input” (0.43) |
| V.2 | Component fidelity · Question fidelity | 233–253 | Changes whose sentences sit wholly or mostly in lines 233–253 (2 sections of the text; those holding fewer than four changes are joined to a neighbour). | 11 | 18 | 0 | “(F1)” (0.64) |
| V.3 | Non-circular dependence | 255 | Changes whose sentences sit wholly or mostly in line 255; with them, changes with no sentence that name this section or share most words with it. | 12 | 17 | 1 | “declared” (0.33) |
| V.4 | Non-vacuity · The conjunction (E) | 257–265 | Changes whose sentences sit wholly or mostly in lines 257–265 (2 sections of the text; those holding fewer than four changes are joined to a neighbour). | 4 | 10 | 0 | “contract” (0.50) |
| V.5 | What (E) excludes, and what it does not | 267–277 | Changes whose sentences sit wholly or mostly in lines 267–277; with them, changes with no sentence that name this section or share most words with it. | 40 | 44 | 2 | “contract” (0.17) |
| V.6 | Why there is no counterpart-kind condition | 279–281 | Changes whose sentences sit wholly or mostly in lines 279–281. | 5 | 5 | 0 | “(F1)” (0.40) |
| V.x | Part V, not in the latest text |  | Changes to Part V with no sentence in the latest text that name no section still standing and share too few words with any section of the Part (section lead under 0.5). | 36 | 36 | 36 | “legitimate” (old name) (0.11) |
| VI.1 | opening of Part VI | 285–303 | Changes whose sentences sit wholly or mostly in lines 285–303; with them, changes with no sentence that name this section or share most words with it. | 17 | 26 | 1 | “declared” (0.24) |
| VI.2 | Finite monotone claim | 305 | Changes whose sentences sit wholly or mostly in line 305. | 8 | 10 | 0 | “route” (0.50) |
| VI.3 | Redundant routes · Interference | 307–309 | Changes whose sentences sit wholly or mostly in lines 307–309 (2 sections of the text; those holding fewer than four changes are joined to a neighbour); with them, changes with no sentence that name this section or share most words with it. | 11 | 15 | 1 | “route” (0.55) |
| VI.4 | Infinitary routes | 311 | Changes whose sentences sit wholly or mostly in line 311. | 4 | 6 | 0 | “route” (1.00) |
| VI.5 | Commitments that do no work | 313 | Changes whose sentences sit wholly or mostly in line 313. | 17 | 19 | 0 | “contract” (0.18) |
| VI.6 | Rivals | 315 | Changes whose sentences sit wholly or mostly in line 315; with them, changes with no sentence that name this section or share most words with it. | 32 | 48 | 2 | “argument” (0.41) |
| VI.7 | Problems | 317 | Changes whose sentences sit wholly or mostly in line 317; with them, changes with no sentence that name this section or share most words with it. | 46 | 59 | 1 | “argument” (0.35) |
| VI.x | Part VI, not in the latest text |  | Changes to Part VI with no sentence in the latest text that name no section still standing and share too few words with any section of the Part (section lead under 0.5). | 8 | 15 | 8 | “Reason use” (0.25) |
| VII.1 | opening of Part VII · Production and direction | 321–325 | Changes whose sentences sit wholly or mostly in lines 321–325 (2 sections of the text; those holding fewer than four changes are joined to a neighbour); with them, changes with no sentence that name this section or share most words with it. | 7 | 9 | 1 | “(F1)” (0.29) |
| VII.2 | Identification · Obstruction | 327–335 | Changes whose sentences sit wholly or mostly in lines 327–335 (2 sections of the text; those holding fewer than four changes are joined to a neighbour); with them, changes with no sentence that name this section or share most words with it. | 8 | 16 | 1 | “content” (0.38) |
| VII.3 | Explanations that remove structure | 337–339 | Changes whose sentences sit wholly or mostly in lines 337–339. | 7 | 11 | 0 | “adequate” (old name) (0.29) |
| VII.4 | Odd-order skew-symmetric matrices · Constitutive rules | 341–347 | Changes whose sentences sit wholly or mostly in lines 341–347 (2 sections of the text; those holding fewer than four changes are joined to a neighbour). | 9 | 9 | 0 | “witness” (old name) (0.33) |
| VIII.1 | opening of Part VIII · Functional transport · Relational transport | 351–361 | Changes whose sentences sit wholly or mostly in lines 351–361 (3 sections of the text; those holding fewer than four changes are joined to a neighbour). | 4 | 5 | 0 | “Functional transport” (0.50) |
| VIII.2 | Approximate transport | 363 | Changes whose sentences sit wholly or mostly in line 363. | 5 | 11 | 0 | “satisfies” (old name) (0.40) |
| VIII.3 | Recoding | 365 | Changes whose sentences sit wholly or mostly in line 365; with them, changes with no sentence that name this section or share most words with it. | 7 | 7 | 1 | “Recoding” (0.57) |
| VIII.4 | Historical index | 367 | Changes whose sentences sit wholly or mostly in line 367. | 5 | 5 | 0 | “contract” (0.80) |
| VIII.5 | A failed answer stays failed | 369 | Changes whose sentences sit wholly or mostly in line 369. | 11 | 14 | 0 | “argument” (0.36) |
| VIII.x | Part VIII, not in the latest text |  | Changes to Part VIII with no sentence in the latest text that name no section still standing and share too few words with any section of the Part (section lead under 0.5). | 1 | 3 | 1 |  (0.00) |
| IX.1 | opening of Part IX · Histories · Bearing · Reason use | 373–385 | Changes whose sentences sit wholly or mostly in lines 373–385 (4 sections of the text; those holding fewer than four changes are joined to a neighbour). | 20 | 40 | 0 | “argument” (0.35) |
| IX.2 | Usability · What a test rules out | 387–395 | Changes whose sentences sit wholly or mostly in lines 387–395 (2 sections of the text; those holding fewer than four changes are joined to a neighbour). | 13 | 19 | 0 | “argument” (0.38) |
| IX.3 | Arguments | 397 | Changes whose sentences sit wholly or mostly in line 397. | 21 | 34 | 0 | “argument” (0.57) |
| IX.x | Part IX, not in the latest text |  | Changes to Part IX with no sentence in the latest text that name no section still standing and share too few words with any section of the Part (section lead under 0.5). | 1 | 1 | 1 | “derive” (old name) (1.00) |
| X.1 | opening of Part X · Deployment | 401–403 | Changes whose sentences sit wholly or mostly in lines 401–403 (2 sections of the text; those holding fewer than four changes are joined to a neighbour); with them, changes with no sentence that name this section or share most words with it. | 9 | 10 | 1 | “declared” (0.33) |
| X.2 | Construction | 405 | Changes whose sentences sit wholly or mostly in line 405. | 11 | 20 | 0 | “content” (0.45) |
| X.3 | Representation in use; construction is not selection | 407–411 | Changes whose sentences sit wholly or mostly in lines 407–411. | 4 | 4 | 0 | “witness” (old name) (0.50) |
| X.4 | Newness · Origin · What a new content may be | 413–425 | Changes whose sentences sit wholly or mostly in lines 413–425 (3 sections of the text; those holding fewer than four changes are joined to a neighbour). | 7 | 8 | 0 | “contract” (0.71) |
| X.5 | Ownership | 427 | Changes whose sentences sit wholly or mostly in line 427; with them, changes with no sentence that name this section or share most words with it. | 12 | 17 | 1 | “Ownership” (0.58) |
| X.6 | Episodes | 429 | Changes whose sentences sit wholly or mostly in line 429. | 10 | 13 | 0 | “argument” (0.50) |
| X.x | Part X, not in the latest text |  | Changes to Part X with no sentence in the latest text that name no section still standing and share too few words with any section of the Part (section lead under 0.5). | 9 | 18 | 9 | “Repair” (0.56) |
| XI.1 | opening of Part XI · Repair | 433–439 | Changes whose sentences sit wholly or mostly in lines 433–439 (2 sections of the text; those holding fewer than four changes are joined to a neighbour); with them, changes with no sentence that name this section or share most words with it. | 7 | 11 | 1 | “Repair” (0.57) |
| XI.2 | The aims of a repair | 441 | Changes whose sentences sit wholly or mostly in line 441. | 20 | 25 | 0 | “Repair” (0.50) |
| XI.3 | Created explanation | 443–451 | Changes whose sentences sit wholly or mostly in lines 443–451. | 7 | 7 | 0 | “Created explanation” (0.29) |
| XI.4 | Result, and the index of (EX) | 453 | Changes whose sentences sit wholly or mostly in line 453. | 5 | 7 | 0 | “contract” (0.60) |
| XI.5 | Appraisal | 455 | Changes whose sentences sit wholly or mostly in line 455. | 18 | 27 | 0 | “declared” (0.39) |
| XI.x | Part XI, not in the latest text |  | Changes to Part XI with no sentence in the latest text that name no section still standing and share too few words with any section of the Part (section lead under 0.5). | 10 | 24 | 10 | “Repair” (0.60) |
| XII.1 | opening of Part XII · Tasks · Retained realization · Retention fixed point | 459–471 | Changes whose sentences sit wholly or mostly in lines 459–471 (4 sections of the text; those holding fewer than four changes are joined to a neighbour). | 6 | 9 | 0 | “conflict” (0.33) |
| XII.2 | System boundary and continuity | 473 | Changes whose sentences sit wholly or mostly in line 473. | 6 | 7 | 0 | “declared” (0.83) |
| XII.3 | Owned capability · Achievement | 475–477 | Changes whose sentences sit wholly or mostly in lines 475–477 (2 sections of the text; those holding fewer than four changes are joined to a neighbour); with them, changes with no sentence that name this section or share most words with it. | 6 | 7 | 1 | “Ownership” (0.83) |
| XII.4 | Tolerances | 479 | Changes whose sentences sit wholly or mostly in line 479. | 9 | 11 | 0 | “Tolerances” (0.67) |
| XII.5 | Selection in the physical module | 481 | Changes whose sentences sit wholly or mostly in line 481. | 5 | 7 | 0 | “transport” (0.60) |
| XII.x | Part XII, not in the latest text |  | Changes to Part XII with no sentence in the latest text that name no section still standing and share too few words with any section of the Part (section lead under 0.5). | 6 | 10 | 6 | “Ownership” (0.33) |
| XIII.1 | opening of Part XIII · Scrutinizability · Recursive capacity · Barriers | 485–495 | Changes whose sentences sit wholly or mostly in lines 485–495 (4 sections of the text; those holding fewer than four changes are joined to a neighbour). | 5 | 7 | 0 | “argument” (0.60) |
| XIII.2 | Universality | 497–509 | Changes whose sentences sit wholly or mostly in lines 497–509; with them, changes with no sentence that name this section or share most words with it. | 7 | 13 | 1 | “advanceable challenges” (old name) (0.43) |
| XIII.x | Part XIII, not in the latest text |  | Changes to Part XIII with no sentence in the latest text that name no section still standing and share too few words with any section of the Part (section lead under 0.5). | 9 | 20 | 9 | “credit” (old name) (0.22) |
| XIV.1 | opening of Part XIV · Imports | 513–518 | Changes whose sentences sit wholly or mostly in lines 513–518 (2 sections of the text; those holding fewer than four changes are joined to a neighbour). | 9 | 11 | 0 | “input” (0.44) |
| XIV.2 | What everything else is defined from | 520 | Changes whose sentences sit wholly or mostly in line 520. | 6 | 11 | 0 | “Imports” (0.33) |
| XIV.3 | Declared inputs · Indices, not imports | 522–524 | Changes whose sentences sit wholly or mostly in lines 522–524 (2 sections of the text; those holding fewer than four changes are joined to a neighbour). | 21 | 24 | 0 | “input” (0.33) |
| XIV.4 | Dependence order · Membership | 526–528 | Changes whose sentences sit wholly or mostly in lines 526–528 (2 sections of the text; those holding fewer than four changes are joined to a neighbour). | 34 | 49 | 0 | “declared” (0.32) |
| XIV.x | Part XIV, not in the latest text |  | Changes to Part XIV with no sentence in the latest text that name no section still standing and share too few words with any section of the Part (section lead under 0.5). | 8 | 18 | 8 | “ground” (old name) (0.38) |
| XV.1 | opening of Part XV | 532–534 | Changes whose sentences sit wholly or mostly in lines 532–534. | 8 | 11 | 0 | “refutation” (old name) (0.38) |
| XV.2 | (Suff) Sufficiency | 536 | Changes whose sentences sit wholly or mostly in line 536. | 20 | 26 | 0 | “transport” (0.30) |
| XV.3 | (Nec) Necessity | 538 | Changes whose sentences sit wholly or mostly in line 538. | 12 | 14 | 0 | “genuine” (old name) (0.33) |
| XV.4 | (Elim) Reinstatement of kinds | 540 | Changes whose sentences sit wholly or mostly in line 540. | 10 | 14 | 0 | “derivation” (old name) (0.50) |
| XV.5 | (Prov) Genesis | 542 | Changes whose sentences sit wholly or mostly in line 542. | 9 | 11 | 0 | “argument” (0.56) |
| XV.6 | (QF) Question-finding | 544 | Changes whose sentences sit wholly or mostly in line 544. | 11 | 13 | 0 | “genuine” (old name) (0.45) |
| XV.7 | A mathematical error | 546 | Changes whose sentences sit wholly or mostly in line 546. | 5 | 6 | 0 | “derivation” (old name) (0.80) |
| XV.x | Part XV, not in the latest text |  | Changes to Part XV with no sentence in the latest text that name no section still standing and share too few words with any section of the Part (section lead under 0.5). | 1 | 1 | 1 |  (0.00) |
| XVI.1 | opening of Part XVI · 1. Kind preservation needs no condition of its own | 550–558 | Changes whose sentences sit wholly or mostly in lines 550–558 (2 sections of the text; those holding fewer than four changes are joined to a neighbour). | 8 | 9 | 0 | “anchor” (old name) (0.38) |
| XVI.2 | 2. Same counterparts, one account | 560–568 | Changes whose sentences sit wholly or mostly in lines 560–568. | 17 | 25 | 0 | “anchor” (old name) (0.47) |
| XVI.3 | 3. Selected transports are underdetermined on unseen changes their population leaves open | 570–576 | Changes whose sentences sit wholly or mostly in lines 570–576. | 11 | 36 | 0 | “transport” (0.36) |
| XVI.4 | 4. Surprise requires an incomplete history | 578–584 | Changes whose sentences sit wholly or mostly in lines 578–584. | 8 | 10 | 0 | “transport” (0.50) |
| XVI.5 | 5. Question-finding is representable | 586–592 | Changes whose sentences sit wholly or mostly in lines 586–592; with them, changes with no sentence that name this section or share most words with it. | 17 | 30 | 5 | “worth” (old name) (0.24) |
| XVI.6 | 6. There are two imports | 594–600 | Changes whose sentences sit wholly or mostly in lines 594–600; with them, changes with no sentence that name this section or share most words with it. | 16 | 24 | 1 | “declared” (0.44) |
| XVI.7 | 7. The frozen assessment and the moving question are consistent | 602–608 | Changes whose sentences sit wholly or mostly in lines 602–608. | 10 | 11 | 0 | “license” (old name) (0.30) |
| XVI.8 | 8. Equivariance under structure-preserving recoding · 9. Output descriptions do not determine accounts | 610–616 | Changes whose sentences sit wholly or mostly in lines 610–616 (2 sections of the text; those holding fewer than four changes are joined to a neighbour). | 6 | 7 | 0 | “(EX)” (0.33) |
| XVI.9 | 10. A two-layer episode, in exact form | 618–632 | Changes whose sentences sit wholly or mostly in lines 618–632. | 26 | 36 | 0 | “derivation” (old name) (0.38) |
| XVI.x | Part XVI, not in the latest text |  | Changes to Part XVI with no sentence in the latest text that name no section still standing and share too few words with any section of the Part (section lead under 0.5). | 3 | 5 | 3 | “Dependence order” (0.33) |
| ALL | Vocabulary across the text |  | Vocabulary changes (scope term or whole text) whose sentences in the latest text sit in three or more Parts, or that name no line at all. | 46 | 89 | 7 | “argument” (0.20) |

Part totals (changes): FM 16; Part 0 184; Part I 29; Part II 34; Part III 45; Part IV 73; Part V 122; Part VI 143; Part VII 31; Part VIII 33; Part IX 55; Part X 62; Part XI 67; Part XII 38; Part XIII 21; Part XIV 78; Part XV 76; Part XVI 122; ALL 46.

## Strengths and weaknesses

**Strengths.**

- The groups are the theory's own divisions, so a reader can lay each group beside the paragraph it concerns and read the old and new sentences in place; nothing depends on a judgment about what a change is about.
- Every change has exactly one group, found by a stated rule from the anchors; 1000 of the 1275 changes sit in one section only, and the rule for the rest is mechanical.
- The Part numbers are the same in every version, so even the proposals written against file 20 or file 10 find their Part.
- Term overlap inside groups is 5.6 times that of random groups of the same sizes, so place and matter largely coincide.

**Weaknesses.**

- A change is only as well placed as its anchor: the anchoring summary counts 582 records placed by similarity, 91 of them with a ratio under 0.4, and a wrong anchor puts its change in the wrong group.
- 119 changes (203 records) have no place in the latest text and sit in Part residues; the residue of Part V mixes several matters. The section lead places 24 more, and about one in ten of those may belong in another section of the same Part.
- The same matter written in several places is split by place: counterparts are treated in Part V (why there is no counterpart-kind condition) and in Part XVI (arguments 1 and 2), the frozen question in grievance 10 and argument 7; each change goes to its own place, and only the *also touches* column and the vocabulary group gather such a matter.
- The vocabulary group gathers the renames by kind of change, not by place; its 46 changes reach 17 of the 18 divisions of the text (front matter and Parts 0 to XVI).
- Joining small sections gives groups whose sections are neighbours rather than one matter; 7 groups join three or more sections (II.1, IV.1, VIII.1, IX.1, X.4, XII.1, XIII.1), and Part II is a single group.
- Group sizes stay uneven (from 1 to 46 changes), because the text's sections are uneven and the changes gather where the rounds worked hardest (the rivals and problems of Part VI, (E)'s exclusions in Part V, Part XIV's dependence order).

## The full assignment: change → group

One row per change, in the order of the text: by group, then by the position of its home sentence (changes with no sentence last in their group, then by change id). *Home sentence* is the first sentence of the change in its group (for a change with no sentence, empty). *Also touches* lists the other groups (and sections) its sentences reach. The records of each change are in `anchored.jsonl` under the same `change_id`; `proposal by place - scripts/assignment.jsonl` gives the same table with the record ids.

| change | group | placed by | records | home sentence | also touches |
| --- | --- | --- | --- | --- | --- |
| CH-0984 | FM | its sentences, one section | 1 | L2.s1 |  |
| CH-0880 | FM | its sentences, one section | 1 | L2.s2 |  |
| CH-0956 | FM | its sentences, one section | 1 | L2.s2 |  |
| CH-0985 | FM | its sentences, one section | 1 | L2.s2 |  |
| CH-0955 | FM | its sentences, one section | 1 | L2.s3 |  |
| CH-0986 | FM | its sentences, one section | 1 | L2.s4 |  |
| CH-0175 | FM | note before Part 0 (removed) | 1 |  |  |
| CH-0176 | FM | note before Part 0 (removed) | 1 |  |  |
| CH-0177 | FM | note before Part 0 (removed) | 1 |  |  |
| CH-0178 | FM | note before Part 0 (removed) | 1 |  |  |
| CH-0179 | FM | note before Part 0 (removed) | 1 |  |  |
| CH-0438 | FM | note before Part 0 (never applied) | 1 |  |  |
| CH-1251 | FM | note before Part 0 (not locatable) | 1 |  |  |
| CH-1252 | FM | note before Part 0 (not locatable) | 1 |  |  |
| CH-1253 | FM | note before Part 0 (not locatable) | 1 |  |  |
| CH-1255 | FM | note before Part 0 (not locatable) | 1 |  |  |
| CH-0909 | 0.1 | its sentences, one section | 3 | L8.s2 |  |
| CH-0957 | 0.1 | its sentences, one section | 2 | L8.s3 |  |
| CH-0881 | 0.1 | its sentences, one section | 1 | L8.s6 |  |
| CH-0906 | 0.1 | its sentences, one section | 1 | L8.s6 |  |
| CH-1036 | 0.1 | most of its sentences (2 sections) | 1 | L8.s6 | I.1 (Faithfulness without assessors) |
| CH-0987 | 0.1 | its sentences, one section | 1 | L8.s7 |  |
| CH-0582 | 0.2 | its sentences, one section | 1 | L11.s1 |  |
| CH-0180 | 0.2 | its sentences, one section | 1 | L11.s2 |  |
| CH-0181 | 0.2 | its sentences, one section | 1 | L11.s4 |  |
| CH-0583 | 0.2 | its sentences, one section | 1 | L11.s4 |  |
| CH-1219 | 0.2 | its sentences, one section | 1 | L11.s4 |  |
| CH-0182 | 0.2 | its sentences, one section | 1 | L13.s1 |  |
| CH-0584 | 0.2 | its sentences, one section | 1 | L13.s1 |  |
| CH-0183 | 0.2 | its sentences, one section | 1 | L13.s3 |  |
| CH-0434 | 0.2 | its sentences, one section | 5 | L13.s3 |  |
| CH-0465 | 0.2 | its sentences, one section | 1 | L13.s3 |  |
| CH-0184 | 0.2 | its sentences, one section | 1 | L13.s4 |  |
| CH-0585 | 0.2 | its sentences, one section | 1 | L13.s7 |  |
| CH-1088 | 0.2 | its sentences, one section | 1 | L13.s7 |  |
| CH-1161 | 0.2 | its sentences, one section | 1 | L13.s7 |  |
| CH-1177 | 0.2 | most of its sentences (2 sections) | 1 | L13.s7 | XVI.6 (6. There are two imports) |
| CH-0185 | 0.2 | its sentences, one section | 1 | L15.s2 |  |
| CH-0586 | 0.2 | its sentences, one section | 1 | L15.s2 |  |
| CH-1220 | 0.2 | its sentences, one section | 1 | L15.s2 |  |
| CH-0186 | 0.2 | its sentences, one section | 1 | L15.s3 |  |
| CH-0996 | 0.2 | its sentences, one section | 2 | L15.s3 |  |
| CH-0587 | 0.2 | its sentences, one section | 1 | L17.s1 |  |
| CH-0997 | 0.2 | most of its sentences (8 sections) | 13 | L17.s1 | 0.16 (Where to attack this); VII.3 (Explanations that remove structure); XV.2 ((Suff) Sufficiency); XV.3 ((Nec) Necessity); XV.4 ((Elim) Reinstatement of kinds); XV.5 ((Prov) Genesis); XV.6 ((QF) Question-finding) |
| CH-1133 | 0.2 | most of its sentences (2 sections) | 3 | L17.s1 | I.1 (Faithfulness without assessors) |
| CH-0910 | 0.2 | its sentences, one section | 2 | L17.s2 |  |
| CH-0588 | 0.2 | its sentences, one section | 1 | L17.s3 |  |
| CH-1207 | 0.2 | its sentences, one section | 1 | L17.s3 |  |
| CH-0187 | 0.2 | its sentences, one section | 1 | L17.s4 |  |
| CH-1087 | 0.2 | most of its sentences (3 sections) | 1 | L17.s4 | 0.15 (Grievances, anticipated / 11. "Kinds exist. A rule is not a cause."); XV.2 ((Suff) Sufficiency) |
| CH-1159 | 0.2 | most of its sentences (2 sections) | 1 | L17.s4 | XV.2 ((Suff) Sufficiency) |
| CH-0518 | 0.2 | section lead 0.59 (not locatable) | 1 |  |  |
| CH-0279 | 0.3 | its sentences, one section | 1 | L19.s1 |  |
| CH-0589 | 0.3 | its sentences, one section | 1 | L21.s1 |  |
| CH-0190 | 0.3 | its sentences, one section | 1 | L23.s2 |  |
| CH-0191 | 0.3 | its sentences, one section | 1 | L23.s3 |  |
| CH-0590 | 0.3 | its sentences, one section | 1 | L23.s3 |  |
| CH-0192 | 0.3 | its sentences, one section | 1 | L25.s1 |  |
| CH-0346 | 0.3 | its sentences, one section | 3 | L25.s1 |  |
| CH-0367 | 0.3 | its sentences, one section | 1 | L25.s1 |  |
| CH-0591 | 0.3 | its sentences, one section | 1 | L25.s1 |  |
| CH-1096 | 0.3 | its sentences, one section | 1 | L25.s1 |  |
| CH-0188 | 0.3 | its sentences, one section | 1 | L25.s2 |  |
| CH-0592 | 0.3 | its sentences, one section | 1 | L25.s2 |  |
| CH-0189 | 0.3 | its sentences, one section | 1 | L25.s3 |  |
| CH-0193 | 0.3 | its sentences, one section | 1 | L25.s3 |  |
| CH-0368 | 0.3 | its sentences, one section | 1 | L25.s3 |  |
| CH-0593 | 0.3 | its sentences, one section | 1 | L25.s3 |  |
| CH-0911 | 0.3 | its sentences, one section | 3 | L25.s3 |  |
| CH-1141 | 0.3 | most of its sentences (2 sections) | 1 | L25.s3 | VII.2 (Obstruction) |
| CH-1245 | 0.3 | its sentences, one section | 1 | L25.s3 |  |
| CH-0194 | 0.3 | its sentences, one section | 1 | L27.s1 |  |
| CH-0594 | 0.3 | its sentences, one section | 1 | L27.s1 |  |
| CH-0547 | 0.3 | section lead 1.00 (not locatable) | 1 |  |  |
| CH-0195 | 0.4 | its sentences, one section | 1 | L29.s1 |  |
| CH-0595 | 0.4 | its sentences, one section | 1 | L29.s1 |  |
| CH-0196 | 0.4 | its sentences, one section | 1 | L31.s1 |  |
| CH-0363 | 0.4 | its sentences, one section | 2 | L31.s1 |  |
| CH-0369 | 0.4 | its sentences, one section | 1 | L31.s1 |  |
| CH-0596 | 0.4 | its sentences, one section | 1 | L31.s1 |  |
| CH-0597 | 0.4 | its sentences, one section | 1 | L31.s1 |  |
| CH-0601 | 0.4 | its sentences, one section | 1 | L31.s1 |  |
| CH-0197 | 0.4 | its sentences, one section | 1 | L31.s2 |  |
| CH-0353 | 0.4 | most of its sentences (3 sections) | 8 | L31.s2 | XIV.3 (Declared inputs); XIV.3 (Indices, not imports) |
| CH-0598 | 0.4 | its sentences, one section | 1 | L31.s2 |  |
| CH-1074 | 0.4 | most of its sentences (2 sections) | 1 | L31.s2 | XIV.3 (Indices, not imports) |
| CH-1215 | 0.4 | its sentences, one section | 1 | L31.s2 |  |
| CH-0198 | 0.4 | its sentences, one section | 1 | L31.s3 |  |
| CH-0501 | 0.4 | its sentences, one section | 1 | L31.s3 |  |
| CH-0599 | 0.4 | its sentences, one section | 1 | L31.s3 |  |
| CH-0199 | 0.4 | its sentences, one section | 1 | L31.s4 |  |
| CH-0497 | 0.4 | its sentences, one section | 1 | L31.s4 |  |
| CH-0498 | 0.4 | its sentences, one section | 1 | L31.s4 |  |
| CH-0600 | 0.4 | its sentences, one section | 1 | L31.s4 |  |
| CH-0602 | 0.4 | its sentences, one section | 1 | L31.s4 |  |
| CH-1222 | 0.4 | its sentences, one section | 1 | L31.s4 |  |
| CH-0200 | 0.5 | its sentences, one section | 1 | L35.s1 |  |
| CH-0370 | 0.5 | its sentences, one section | 1 | L35.s1 |  |
| CH-0148 | 0.5 | section its source names (never applied) | 13 |  |  |
| CH-0213 | 0.5 | section its source names (removed) | 1 |  |  |
| CH-0224 | 0.5 | section its source names (removed) | 1 |  |  |
| CH-0201 | 0.6 | its sentences, one section | 1 | L37.s3 |  |
| CH-0603 | 0.6 | its sentences, one section | 1 | L37.s3 |  |
| CH-1086 | 0.6 | its sentences, one section | 1 | L37.s3 |  |
| CH-0202 | 0.6 | its sentences, one section | 1 | L37.s4 |  |
| CH-0203 | 0.6 | its sentences, one section | 1 | L39.s2 |  |
| CH-0604 | 0.6 | its sentences, one section | 1 | L39.s2 |  |
| CH-0204 | 0.6 | its sentences, one section | 1 | L39.s4 |  |
| CH-0605 | 0.7 | its sentences, one section | 1 | L41.s1 |  |
| CH-1078 | 0.7 | its sentences, one section | 1 | L41.s1 |  |
| CH-1142 | 0.7 | its sentences, one section | 1 | L41.s1 |  |
| CH-0206 | 0.7 | its sentences, one section | 1 | L41.s2 |  |
| CH-0606 | 0.7 | its sentences, one section | 1 | L41.s2 |  |
| CH-0887 | 0.7 | its sentences, one section | 1 | L41.s2 |  |
| CH-0205 | 0.7 | its sentences, one section | 1 | L41.s3 |  |
| CH-0207 | 0.7 | its sentences, one section | 1 | L41.s3 |  |
| CH-0607 | 0.7 | its sentences, one section | 1 | L41.s3 |  |
| CH-0608 | 0.8 | its sentences, one section | 1 | L43.s1 |  |
| CH-0884 | 0.8 | its sentences, one section | 1 | L43.s1 |  |
| CH-1080 | 0.8 | its sentences, one section | 1 | L43.s1 |  |
| CH-1203 | 0.8 | its sentences, one section | 2 | L43.s2 |  |
| CH-0209 | 0.8 | its sentences, one section | 1 | L43.s3 |  |
| CH-0609 | 0.8 | its sentences, one section | 1 | L43.s3 |  |
| CH-1079 | 0.8 | its sentences, one section | 1 | L43.s3 |  |
| CH-1130 | 0.8 | most of its sentences (3 sections) | 2 | L43.s3 | IV.3 (Representation is defined, not supplied); IV.4 (Prediction, surprise, violation) |
| CH-1223 | 0.8 | its sentences, one section | 1 | L43.s3 |  |
| CH-0001 | 0.8 | its sentences, one section | 1 | L43.s4 |  |
| CH-0208 | 0.8 | its sentences, one section | 1 | L43.s4 |  |
| CH-0885 | 0.8 | its sentences, one section | 1 | L43.s4 |  |
| CH-0610 | 0.8 | its sentences, one section | 1 | L43.s5 |  |
| CH-0886 | 0.8 | its sentences, one section | 1 | L43.s5 |  |
| CH-1204 | 0.8 | its sentences, one section | 2 | L43.s5 |  |
| CH-0210 | 0.9 | its sentences, one section | 1 | L45.s1 |  |
| CH-0611 | 0.9 | its sentences, one section | 1 | L45.s4 |  |
| CH-1092 | 0.9 | most of its sentences (2 sections) | 1 | L45.s4 | I.4 (Substrate independence with physical conditions) |
| CH-0211 | 0.9 | its sentences, one section | 1 | L45.s5 |  |
| CH-0212 | 0.10 | its sentences, one section | 1 | L47.s1 |  |
| CH-0214 | 0.10 | its sentences, one section | 1 | L47.s1 |  |
| CH-0614 | 0.10 | its sentences, one section | 1 | L47.s1 |  |
| CH-1000 | 0.10 | its sentences, one section | 2 | L47.s1 |  |
| CH-0612 | 0.10 | its sentences, one section | 1 | L47.s2 |  |
| CH-0215 | 0.10 | its sentences, one section | 1 | L47.s3 |  |
| CH-0613 | 0.10 | its sentences, one section | 1 | L47.s3 |  |
| CH-0913 | 0.10 | its sentences, one section | 3 | L47.s3 |  |
| CH-0216 | 0.11 | its sentences, one section | 1 | L49.s1 |  |
| CH-0220 | 0.11 | its sentences, one section | 1 | L49.s1 |  |
| CH-0218 | 0.11 | its sentences, one section | 1 | L49.s2 |  |
| CH-0615 | 0.11 | its sentences, one section | 1 | L49.s2 |  |
| CH-1072 | 0.11 | its sentences, one section | 1 | L49.s2 |  |
| CH-1143 | 0.11 | its sentences, one section | 1 | L49.s2 |  |
| CH-0219 | 0.11 | its sentences, one section | 1 | L49.s3 |  |
| CH-0616 | 0.11 | its sentences, one section | 1 | L49.s3 |  |
| CH-1001 | 0.11 | most of its sentences (3 sections) | 5 | L49.s3 | II.1 (Organizations); VII.4 (Odd-order skew-symmetric matrices) |
| CH-0888 | 0.11 | its sentences, one section | 1 | L49.s4 |  |
| CH-0958 | 0.11 | its sentences, one section | 2 | L49.s5 |  |
| CH-0516 | 0.12 | its sentences, one section | 1 | L51.s1 |  |
| CH-0618 | 0.12 | its sentences, one section | 1 | L51.s1 |  |
| CH-0221 | 0.12 | its sentences, one section | 1 | L51.s2 |  |
| CH-0889 | 0.12 | its sentences, one section | 1 | L51.s2 |  |
| CH-0217 | 0.12 | its sentences, one section | 1 | L51.s3 |  |
| CH-0222 | 0.12 | its sentences, one section | 1 | L51.s3 |  |
| CH-0227 | 0.12 | its sentences, one section | 1 | L51.s3 |  |
| CH-0617 | 0.12 | its sentences, one section | 1 | L51.s3 |  |
| CH-1094 | 0.12 | its sentences, one section | 1 | L51.s3 |  |
| CH-1192 | 0.12 | its sentences, one section | 1 | L51.s3 |  |
| CH-0223 | 0.13 | its sentences, one section | 1 | L53.s1 |  |
| CH-0225 | 0.13 | its sentences, one section | 1 | L53.s1 |  |
| CH-0619 | 0.13 | its sentences, one section | 1 | L53.s2 |  |
| CH-1002 | 0.13 | its sentences, one section | 2 | L53.s2 |  |
| CH-0226 | 0.13 | its sentences, one section | 1 | L53.s3 |  |
| CH-0228 | 0.14 | its sentences, one section | 1 | L55.s1 |  |
| CH-0229 | 0.14 | its sentences, one section | 1 | L55.s3 |  |
| CH-0620 | 0.14 | its sentences, one section | 1 | L55.s4 |  |
| CH-0959 | 0.14 | its sentences, one section | 2 | L55.s4 |  |
| CH-0621 | 0.15 | its sentences, one section | 1 | L57.s1 |  |
| CH-1160 | 0.15 | its sentences, one section | 1 | L57.s1 |  |
| CH-0230 | 0.15 | its sentences, one section | 1 | L57.s2 |  |
| CH-0231 | 0.15 | its sentences, one section | 1 | L57.s3 |  |
| CH-0233 | 0.16 | its sentences, one section | 1 | L61.s1 |  |
| CH-0622 | 0.16 | its sentences, one section | 1 | L61.s1 |  |
| CH-0623 | 0.16 | its sentences, one section | 1 | L61.s1 |  |
| CH-0914 | 0.16 | its sentences, one section | 3 | L61.s1 |  |
| CH-1107 | 0.16 | most of its sentences (2 sections) | 1 | L61.s1 | XV.1 (opening of Part XV) |
| CH-1155 | 0.16 | most of its sentences (2 sections) | 1 | L61.s1 | XV.1 (opening of Part XV) |
| CH-0232 | 0.16 | its sentences, one section | 1 | L61.s2 |  |
| CH-0360 | 0.16 | its sentences, one section | 1 | L61.s2 |  |
| CH-0443 | 0.16 | its sentences, one section | 1 | L61.s2 |  |
| CH-0565 | 0.16 | its sentences, one section | 1 | L61.s2 |  |
| CH-1216 | 0.16 | its sentences, one section | 1 | L61.s2 |  |
| CH-0012 | 0.16 | section its source names (removed) | 1 |  |  |
| CH-0245 | 0.16 | section its source names (removed) | 1 |  |  |
| CH-0172 | 0.x | Part only (not locatable) | 1 |  |  |
| CH-0345 | 0.x | Part only (not locatable) | 7 |  |  |
| CH-0427 | 0.x | Part only (not locatable) | 6 |  |  |
| CH-0463 | 0.x | Part only (not locatable) | 1 |  |  |
| CH-0464 | 0.x | Part only (not locatable) | 1 |  |  |
| CH-0545 | 0.x | Part only (not locatable) | 1 |  |  |
| CH-0546 | 0.x | Part only (not locatable) | 1 |  |  |
| CH-0548 | 0.x | Part only (not locatable) | 1 |  |  |
| CH-1273 | 0.x | Part only (not locatable) | 1 |  |  |
| CH-0624 | I.1 | its sentences, one section | 1 | L67.s1 |  |
| CH-0625 | I.1 | its sentences, one section | 1 | L67.s1 |  |
| CH-1081 | I.1 | its sentences, one section | 1 | L67.s1 |  |
| CH-1162 | I.1 | its sentences, one section | 1 | L67.s1 |  |
| CH-0248 | I.1 | its sentences, one section | 1 | L67.s2 |  |
| CH-0626 | I.1 | its sentences, one section | 1 | L67.s2 |  |
| CH-0627 | I.2 | its sentences, one section | 1 | L69.s1 |  |
| CH-1186 | I.2 | its sentences, one section | 1 | L69.s1 |  |
| CH-0429 | I.2 | its sentences, one section | 2 | L69.s2 |  |
| CH-0466 | I.2 | its sentences, one section | 1 | L69.s2 |  |
| CH-0628 | I.2 | its sentences, one section | 1 | L69.s3 |  |
| CH-0629 | I.2 | its sentences, one section | 1 | L69.s3 |  |
| CH-0630 | I.3 | its sentences, one section | 1 | L71.s1 |  |
| CH-1057 | I.3 | its sentences, one section | 1 | L71.s1 |  |
| CH-1173 | I.3 | its sentences, one section | 1 | L71.s1 |  |
| CH-0631 | I.3 | its sentences, one section | 1 | L71.s3 |  |
| CH-0249 | I.3 | its sentences, one section | 1 | L73.s1 |  |
| CH-0442 | I.4 | its sentences, one section | 2 | L75.s1 |  |
| CH-0632 | I.4 | its sentences, one section | 1 | L75.s1 |  |
| CH-0633 | I.4 | its sentences, one section | 1 | L75.s2 |  |
| CH-0882 | I.4 | its sentences, one section | 1 | L75.s2 |  |
| CH-0960 | I.4 | its sentences, one section | 2 | L75.s2 |  |
| CH-1037 | I.4 | its sentences, one section | 1 | L75.s2 |  |
| CH-1152 | I.4 | most of its sentences (2 sections) | 1 | L75.s2 | XVI.9 (10. A two-layer episode, in exact form) |
| CH-1193 | I.4 | its sentences, one section | 1 | L75.s2 |  |
| CH-0510 | I.4 | its sentences, one section | 1 | L75.s4 |  |
| CH-0634 | I.4 | its sentences, one section | 1 | L75.s4 |  |
| CH-0883 | I.4 | its sentences, one section | 1 | L75.s5 |  |
| CH-0961 | I.4 | its sentences, one section | 3 | L75.s6 |  |
| CH-0250 | II.1 | its sentences, one section | 1 | L105.s1 |  |
| CH-0635 | II.1 | its sentences, one section | 1 | L105.s1 |  |
| CH-0636 | II.1 | its sentences, one section | 1 | L107.s1 |  |
| CH-1003 | II.1 | its sentences, one section | 2 | L109.s4 |  |
| CH-0480 | II.1 | its sentences, one section | 1 | L119.s1 |  |
| CH-0486 | II.1 | its sentences, one section | 1 | L119.s1 |  |
| CH-1254 | II.1 | its sentences, one section | 1 | L119.s1 |  |
| CH-0411 | II.1 | its sentences, one section | 5 | L119.s2 |  |
| CH-0467 | II.1 | its sentences, one section | 2 | L119.s2 |  |
| CH-0487 | II.1 | its sentences, one section | 1 | L119.s3 |  |
| CH-0519 | II.1 | its sentences, one section | 1 | L119.s3 |  |
| CH-0560 | II.1 | its sentences, one section | 1 | L119.s3 |  |
| CH-0637 | II.1 | its sentences, one section | 1 | L119.s3 |  |
| CH-1004 | II.1 | its sentences, one section | 2 | L119.s3 |  |
| CH-0520 | II.1 | its sentences, one section | 1 | L119.s4 |  |
| CH-0638 | II.1 | its sentences, one section | 1 | L119.s4 |  |
| CH-0639 | II.1 | its sentences, one section | 1 | L119.s4 |  |
| CH-0640 | II.1 | its sentences, one section | 1 | L119.s4 |  |
| CH-0251 | II.1 | its sentences, one section | 1 | L119.s6 |  |
| CH-0366 | II.1 | its sentences, one section | 2 | L119.s6 |  |
| CH-0252 | II.1 | its sentences, one section | 1 | L121.s1 |  |
| CH-0580 | II.1 | its sentences, one section | 1 | L121.s1 |  |
| CH-0253 | II.1 | its sentences, one section | 1 | L127.s4 |  |
| CH-0371 | II.1 | its sentences, one section | 1 | L127.s4 |  |
| CH-0254 | II.1 | its sentences, one section | 1 | L127.s5 |  |
| CH-0641 | II.1 | its sentences, one section | 1 | L127.s5 |  |
| CH-1046 | II.1 | its sentences, one section | 1 | L127.s5 |  |
| CH-1163 | II.1 | most of its sentences (2 sections) | 1 | L127.s5 | VI.7 (Problems) |
| CH-0067 | II.x | Part only (never applied) | 1 |  |  |
| CH-0068 | II.x | Part only (never applied) | 2 |  |  |
| CH-0069 | II.x | Part only (never applied) | 1 |  |  |
| CH-0070 | II.x | Part only (never applied) | 1 |  |  |
| CH-0071 | II.x | Part only (never applied) | 1 |  |  |
| CH-0072 | II.x | Part only (never applied) | 1 |  |  |
| CH-0255 | III.1 | its sentences, one section | 1 | L141.s3 |  |
| CH-1218 | III.1 | its sentences, one section | 1 | L141.s3 |  |
| CH-0642 | III.1 | its sentences, one section | 1 | L147.s1 |  |
| CH-1213 | III.1 | its sentences, one section | 1 | L147.s2 |  |
| CH-0256 | III.2 | its sentences, one section | 1 | L151.s1 |  |
| CH-1005 | III.2 | its sentences, one section | 2 | L151.s1 |  |
| CH-0579 | III.2 | its sentences, one section | 1 | L151.s2 |  |
| CH-0643 | III.2 | its sentences, one section | 1 | L151.s4 |  |
| CH-0257 | III.2 | its sentences, one section | 1 | L151.s7 |  |
| CH-0372 | III.2 | its sentences, one section | 1 | L151.s7 |  |
| CH-0644 | III.2 | its sentences, one section | 1 | L151.s7 |  |
| CH-0915 | III.2 | its sentences, one section | 3 | L151.s7 |  |
| CH-0149 | III.2 | section its source names (never applied) | 1 |  |  |
| CH-0150 | III.2 | section its source names (never applied) | 1 |  |  |
| CH-0151 | III.2 | section its source names (never applied) | 1 |  |  |
| CH-0152 | III.2 | section its source names (never applied) | 18 |  |  |
| CH-0645 | III.3 | its sentences, one section | 1 | L155.s1 |  |
| CH-0647 | III.3 | its sentences, one section | 1 | L155.s4 |  |
| CH-0646 | III.3 | its sentences, one section | 1 | L155.s6 |  |
| CH-1214 | III.3 | its sentences, one section | 1 | L155.s6 |  |
| CH-0261 | III.4 | its sentences, one section | 1 | L157.s1 |  |
| CH-0648 | III.4 | its sentences, one section | 1 | L157.s1 |  |
| CH-0258 | III.4 | its sentences, one section | 1 | L159.s1 |  |
| CH-0890 | III.4 | its sentences, one section | 1 | L159.s3 |  |
| CH-0962 | III.4 | its sentences, one section | 2 | L159.s3 |  |
| CH-0259 | III.4 | its sentences, one section | 1 | L159.s4 |  |
| CH-1257 | III.4 | its sentences, one section | 2 | L159.s4 |  |
| CH-0260 | III.4 | its sentences, one section | 1 | L159.s5 |  |
| CH-0364 | III.4 | its sentences, one section | 3 | L159.s5 |  |
| CH-0373 | III.4 | its sentences, one section | 1 | L159.s5 |  |
| CH-0649 | III.4 | its sentences, one section | 1 | L159.s5 |  |
| CH-1085 | III.4 | its sentences, one section | 1 | L159.s5 |  |
| CH-0916 | III.4 | its sentences, one section | 3 | L159.s6 |  |
| CH-1043 | III.4 | its sentences, one section | 1 | L159.s6 |  |
| CH-1242 | III.4 | its sentences, one section | 2 | L159.s6 |  |
| CH-0500 | III.4 | its sentences, one section | 1 | L159.s7 |  |
| CH-0650 | III.4 | its sentences, one section | 1 | L159.s7 |  |
| CH-1144 | III.4 | its sentences, one section | 1 | L159.s7 |  |
| CH-0917 | III.4 | its sentences, one section | 3 | L161.s4 |  |
| CH-0167 | III.4 | its sentences, one section | 1 | L161.s5 |  |
| CH-0262 | III.4 | its sentences, one section | 1 | L161.s5 |  |
| CH-0374 | III.4 | its sentences, one section | 1 | L161.s5 |  |
| CH-0110 | III.4 | section lead 0.63 (never applied) | 2 |  |  |
| CH-0166 | III.x | Part only (never applied) | 1 |  |  |
| CH-0435 | III.x | Part only (never applied) | 1 |  |  |
| CH-0651 | IV.1 | its sentences, one section | 1 | L171.s1 |  |
| CH-0263 | IV.1 | its sentences, one section | 1 | L175.s1 |  |
| CH-0652 | IV.1 | its sentences, one section | 1 | L175.s1 |  |
| CH-1190 | IV.1 | most of its sentences (4 sections) | 1 | L177.s1 | IV.4 (Prediction, surprise, violation); XVI.4 (4. Surprise requires an incomplete history); XVI.9 (10. A two-layer episode, in exact form) |
| CH-0653 | IV.1 | its sentences, one section | 1 | L177.s2 |  |
| CH-0552 | IV.1 | its sentences, one section | 1 | L189.s1 |  |
| CH-0654 | IV.1 | its sentences, one section | 1 | L189.s2 |  |
| CH-0084 | IV.1 | section lead 0.54 (never applied) | 1 |  |  |
| CH-1006 | IV.2 | most of its sentences (2 sections) | 4 | L193.s1 | IV.3 (Representation is defined, not supplied) |
| CH-0441 | IV.2 | its sentences, one section | 1 | L195.s1 |  |
| CH-0489 | IV.2 | its sentences, one section | 1 | L195.s1 |  |
| CH-0444 | IV.2 | its sentences, one section | 1 | L195.s2 |  |
| CH-0264 | IV.2 | its sentences, one section | 1 | L195.s6 |  |
| CH-0375 | IV.2 | its sentences, one section | 1 | L195.s6 |  |
| CH-0655 | IV.2 | its sentences, one section | 1 | L195.s6 |  |
| CH-0656 | IV.2 | its sentences, one section | 1 | L197.s1 |  |
| CH-1007 | IV.2 | most of its sentences (2 sections) | 4 | L197.s1 | IV.3 (Representation is defined, not supplied) |
| CH-0657 | IV.2 | its sentences, one section | 1 | L201.s1 |  |
| CH-0658 | IV.2 | its sentences, one section | 1 | L201.s1 |  |
| CH-0918 | IV.2 | its sentences, one section | 3 | L201.s1 |  |
| CH-1191 | IV.2 | its sentences, one section | 1 | L201.s1 |  |
| CH-0083 | IV.2 | section lead 0.64 (never applied) | 1 |  |  |
| CH-0160 | IV.2 | section its source names (never applied) | 2 |  |  |
| CH-0162 | IV.2 | section its source names (never applied) | 1 |  |  |
| CH-0659 | IV.3 | its sentences, one section | 1 | L203.s1 |  |
| CH-0504 | IV.3 | its sentences, one section | 1 | L205.s1 |  |
| CH-0660 | IV.3 | its sentences, one section | 1 | L211.s1 |  |
| CH-1184 | IV.3 | its sentences, one section | 1 | L211.s1 |  |
| CH-0902 | IV.3 | its sentences, one section | 1 | L211.s2 |  |
| CH-0265 | IV.3 | its sentences, one section | 1 | L211.s4 |  |
| CH-0376 | IV.3 | its sentences, one section | 1 | L211.s4 |  |
| CH-0661 | IV.3 | its sentences, one section | 1 | L211.s4 |  |
| CH-0919 | IV.3 | its sentences, one section | 3 | L211.s4 |  |
| CH-1068 | IV.3 | most of its sentences (2 sections) | 1 | L211.s4 | VII.1 (Production and direction) |
| CH-0076 | IV.3 | section lead 0.51 (never applied) | 3 |  |  |
| CH-0077 | IV.3 | section lead 0.52 (never applied) | 1 |  |  |
| CH-0662 | IV.4 | its sentences, one section | 1 | L215.s1 |  |
| CH-1093 | IV.4 | most of its sentences (5 sections) | 1 | L215.s1 | IV.1 (The object layer and the simulation layer); IV.2 (Three provenances); XVI.4 (4. Surprise requires an incomplete history); XVI.9 (10. A two-layer episode, in exact form) |
| CH-1201 | IV.4 | its sentences, one section | 2 | L215.s1 |  |
| CH-0437 | IV.4 | most of its sentences (3 sections) | 10 | L217.s1 | X.6 (Episodes); XVI.4 (4. Surprise requires an incomplete history) |
| CH-0468 | IV.4 | its sentences, one section | 1 | L217.s1 |  |
| CH-0508 | IV.4 | its sentences, one section | 1 | L219.s1 |  |
| CH-0663 | IV.4 | its sentences, one section | 1 | L219.s1 |  |
| CH-0506 | IV.4 | its sentences, one section | 1 | L221.s1 |  |
| CH-0920 | IV.4 | most of its sentences (2 sections) | 7 | L221.s1 | XI.3 (Created explanation) |
| CH-1199 | IV.4 | its sentences, one section | 2 | L221.s1 |  |
| CH-0268 | IV.4 | its sentences, one section | 1 | L223.s2 |  |
| CH-0267 | IV.4 | its sentences, one section | 1 | L223.s3 |  |
| CH-0665 | IV.4 | its sentences, one section | 1 | L223.s3 |  |
| CH-0891 | IV.4 | its sentences, one section | 1 | L223.s3 |  |
| CH-0266 | IV.4 | its sentences, one section | 1 | L223.s4 |  |
| CH-0377 | IV.4 | its sentences, one section | 1 | L223.s4 |  |
| CH-0469 | IV.4 | its sentences, one section | 1 | L223.s4 |  |
| CH-0470 | IV.4 | its sentences, one section | 2 | L223.s4 |  |
| CH-0664 | IV.4 | its sentences, one section | 1 | L223.s4 |  |
| CH-0485 | IV.4 | its sentences, one section | 1 | L223.s5 |  |
| CH-0509 | IV.4 | its sentences, one section | 1 | L223.s5 |  |
| CH-0514 | IV.4 | its sentences, one section | 1 | L223.s5 |  |
| CH-0521 | IV.4 | its sentences, one section | 1 | L223.s5 |  |
| CH-0522 | IV.4 | its sentences, one section | 1 | L223.s5 |  |
| CH-0666 | IV.4 | its sentences, one section | 1 | L225.s3 |  |
| CH-0075 | IV.4 | section lead 1.00 (never applied) | 1 |  |  |
| CH-0087 | IV.4 | section lead 0.79 (never applied) | 1 |  |  |
| CH-0073 | IV.x | Part only (never applied) | 1 |  |  |
| CH-0074 | IV.x | Part only (never applied) | 5 |  |  |
| CH-0078 | IV.x | Part only (never applied) | 3 |  |  |
| CH-0079 | IV.x | Part only (never applied) | 2 |  |  |
| CH-0080 | IV.x | Part only (never applied) | 1 |  |  |
| CH-0081 | IV.x | Part only (never applied) | 1 |  |  |
| CH-0082 | IV.x | Part only (never applied) | 3 |  |  |
| CH-0086 | IV.x | Part only (never applied) | 3 |  |  |
| CH-0088 | IV.x | Part only (never applied) | 3 |  |  |
| CH-0507 | IV.x | Part only (never applied) | 1 |  |  |
| CH-0414 | V.1 | its sentences, one section | 1 | L231.s1 |  |
| CH-0419 | V.1 | its sentences, one section | 4 | L231.s1 |  |
| CH-0471 | V.1 | its sentences, one section | 1 | L231.s1 |  |
| CH-0472 | V.1 | its sentences, one section | 2 | L231.s1 |  |
| CH-0481 | V.1 | its sentences, one section | 1 | L231.s1 |  |
| CH-0488 | V.1 | its sentences, one section | 1 | L231.s2 |  |
| CH-0523 | V.1 | its sentences, one section | 1 | L231.s2 |  |
| CH-0524 | V.1 | its sentences, one section | 1 | L231.s2 |  |
| CH-0528 | V.1 | its sentences, one section | 1 | L231.s2 |  |
| CH-0667 | V.1 | its sentences, one section | 1 | L231.s3 |  |
| CH-1008 | V.1 | most of its sentences (3 sections) | 6 | L231.s3 | V.4 (Non-vacuity); VI.1 (opening of Part VI) |
| CH-0027 | V.1 | section lead 0.55 (never applied) | 1 |  |  |
| CH-0046 | V.1 | section lead 0.60 (never applied) | 1 |  |  |
| CH-0060 | V.1 | section lead 1.00 (never applied) | 1 |  |  |
| CH-0668 | V.2 | its sentences, one section | 1 | L233.s1 |  |
| CH-1009 | V.2 | most of its sentences (2 sections) | 5 | L233.s1 | XVI.1 (1. Kind preservation needs no condition of its own) |
| CH-0551 | V.2 | its sentences, one section | 1 | L245.s1 |  |
| CH-0669 | V.2 | its sentences, one section | 1 | L245.s1 |  |
| CH-1042 | V.2 | its sentences, one section | 1 | L245.s1 |  |
| CH-1137 | V.2 | most of its sentences (2 sections) | 3 | L245.s1 | 0.14 (Grievances, anticipated / 10. "Freezing the question for assessment while letting questions change across episodes is having it both ways.") |
| CH-0269 | V.2 | its sentences, one section | 1 | L245.s4 |  |
| CH-0525 | V.2 | its sentences, one section | 1 | L245.s4 |  |
| CH-0670 | V.2 | its sentences, one section | 1 | L245.s4 |  |
| CH-0671 | V.2 | its sentences, one section | 1 | L245.s4 |  |
| CH-1010 | V.2 | its sentences, one section | 2 | L245.s4 |  |
| CH-0417 | V.3 | its sentences, one section | 1 | L255.s1 |  |
| CH-0415 | V.3 | its sentences, one section | 1 | L255.s2 |  |
| CH-0436 | V.3 | its sentences, one section | 2 | L255.s2 |  |
| CH-0573 | V.3 | its sentences, one section | 1 | L255.s3 |  |
| CH-0577 | V.3 | its sentences, one section | 1 | L255.s3 |  |
| CH-0672 | V.3 | its sentences, one section | 1 | L255.s3 |  |
| CH-0413 | V.3 | its sentences, one section | 1 | L255.s4 |  |
| CH-0416 | V.3 | its sentences, one section | 4 | L255.s4 |  |
| CH-0423 | V.3 | its sentences, one section | 1 | L255.s4 |  |
| CH-0490 | V.3 | its sentences, one section | 1 | L255.s4 |  |
| CH-1011 | V.3 | its sentences, one section | 2 | L255.s4 |  |
| CH-0041 | V.3 | section lead 0.59 (never applied) | 1 |  |  |
| CH-0999 | V.4 | most of its sentences (4 sections) | 7 | L257.s1 | 0.8 (Grievances, anticipated / 4. "Then everything is relative to a contract of admitted changes, and nothing is independent of the modeller."); III.3 (Contracts have provenance); III.4 (Scope, and a question that can be in error) |
| CH-0892 | V.4 | its sentences, one section | 1 | L257.s2 |  |
| CH-0673 | V.4 | its sentences, one section | 1 | L257.s3 |  |
| CH-1224 | V.4 | its sentences, one section | 1 | L257.s3 |  |
| CH-0272 | V.5 | its sentences, one section | 1 | L267.s1 |  |
| CH-0273 | V.5 | its sentences, one section | 1 | L269.s1 |  |
| CH-0006 | V.5 | its sentences, one section | 1 | L269.s2 |  |
| CH-0274 | V.5 | its sentences, one section | 1 | L269.s2 |  |
| CH-0378 | V.5 | its sentences, one section | 1 | L269.s2 |  |
| CH-0445 | V.5 | its sentences, one section | 1 | L269.s2 |  |
| CH-0566 | V.5 | its sentences, one section | 1 | L269.s2 |  |
| CH-0674 | V.5 | its sentences, one section | 1 | L269.s2 |  |
| CH-0676 | V.5 | its sentences, one section | 1 | L269.s2 |  |
| CH-0270 | V.5 | its sentences, one section | 1 | L269.s3 |  |
| CH-0675 | V.5 | its sentences, one section | 1 | L269.s3 |  |
| CH-1045 | V.5 | its sentences, one section | 1 | L269.s3 |  |
| CH-0275 | V.5 | its sentences, one section | 1 | L271.s1 |  |
| CH-0007 | V.5 | its sentences, one section | 1 | L271.s2 |  |
| CH-0271 | V.5 | its sentences, one section | 1 | L271.s2 |  |
| CH-0276 | V.5 | its sentences, one section | 1 | L273.s2 |  |
| CH-0347 | V.5 | its sentences, one section | 2 | L273.s2 |  |
| CH-0379 | V.5 | its sentences, one section | 1 | L273.s2 |  |
| CH-0677 | V.5 | its sentences, one section | 1 | L273.s2 |  |
| CH-0963 | V.5 | its sentences, one section | 2 | L275.s1 |  |
| CH-0893 | V.5 | its sentences, one section | 1 | L275.s2 |  |
| CH-0380 | V.5 | its sentences, one section | 1 | L277.s1 |  |
| CH-0678 | V.5 | its sentences, one section | 1 | L277.s1 |  |
| CH-0921 | V.5 | its sentences, one section | 3 | L277.s1 |  |
| CH-1259 | V.5 | its sentences, one section | 1 | L277.s1 |  |
| CH-0277 | V.5 | its sentences, one section | 1 | L277.s2 |  |
| CH-0679 | V.5 | its sentences, one section | 1 | L277.s2 |  |
| CH-1099 | V.5 | its sentences, one section | 1 | L277.s2 |  |
| CH-0278 | V.5 | its sentences, one section | 1 | L277.s3 |  |
| CH-0280 | V.5 | its sentences, one section | 1 | L277.s3 |  |
| CH-0381 | V.5 | its sentences, one section | 1 | L277.s3 |  |
| CH-0680 | V.5 | its sentences, one section | 1 | L277.s3 |  |
| CH-0681 | V.5 | its sentences, one section | 1 | L277.s3 |  |
| CH-1101 | V.5 | its sentences, one section | 1 | L277.s3 |  |
| CH-1158 | V.5 | its sentences, one section | 1 | L277.s3 |  |
| CH-0281 | V.5 | its sentences, one section | 1 | L277.s4 |  |
| CH-0682 | V.5 | its sentences, one section | 1 | L277.s4 |  |
| CH-0683 | V.5 | its sentences, one section | 1 | L277.s4 |  |
| CH-0058 | V.5 | section lead 1.00 (never applied) | 1 |  |  |
| CH-0159 | V.5 | section lead 0.58 (never applied) | 1 |  |  |
| CH-0684 | V.6 | its sentences, one section | 1 | L279.s1 |  |
| CH-0282 | V.6 | its sentences, one section | 1 | L281.s1 |  |
| CH-0685 | V.6 | its sentences, one section | 1 | L281.s2 |  |
| CH-0026 | V.6 | its sentences, one section | 1 | L281.s3 |  |
| CH-0686 | V.6 | its sentences, one section | 1 | L281.s5 |  |
| CH-0028 | V.x | Part only (never applied) | 1 |  |  |
| CH-0029 | V.x | Part only (never applied) | 1 |  |  |
| CH-0030 | V.x | Part only (never applied) | 1 |  |  |
| CH-0031 | V.x | Part only (never applied) | 1 |  |  |
| CH-0032 | V.x | Part only (never applied) | 1 |  |  |
| CH-0033 | V.x | Part only (never applied) | 1 |  |  |
| CH-0034 | V.x | Part only (never applied) | 1 |  |  |
| CH-0035 | V.x | Part only (never applied) | 1 |  |  |
| CH-0036 | V.x | Part only (never applied) | 1 |  |  |
| CH-0037 | V.x | Part only (never applied) | 1 |  |  |
| CH-0038 | V.x | Part only (never applied) | 1 |  |  |
| CH-0039 | V.x | Part only (never applied) | 1 |  |  |
| CH-0040 | V.x | Part only (never applied) | 1 |  |  |
| CH-0042 | V.x | Part only (never applied) | 1 |  |  |
| CH-0043 | V.x | Part only (never applied) | 1 |  |  |
| CH-0044 | V.x | Part only (never applied) | 1 |  |  |
| CH-0045 | V.x | Part only (never applied) | 1 |  |  |
| CH-0047 | V.x | Part only (never applied) | 1 |  |  |
| CH-0048 | V.x | Part only (never applied) | 1 |  |  |
| CH-0049 | V.x | Part only (never applied) | 1 |  |  |
| CH-0050 | V.x | Part only (never applied) | 1 |  |  |
| CH-0051 | V.x | Part only (never applied) | 1 |  |  |
| CH-0052 | V.x | Part only (never applied) | 1 |  |  |
| CH-0053 | V.x | Part only (never applied) | 1 |  |  |
| CH-0054 | V.x | Part only (never applied) | 1 |  |  |
| CH-0055 | V.x | Part only (never applied) | 1 |  |  |
| CH-0056 | V.x | Part only (never applied) | 1 |  |  |
| CH-0057 | V.x | Part only (never applied) | 1 |  |  |
| CH-0059 | V.x | Part only (never applied) | 1 |  |  |
| CH-0061 | V.x | Part only (never applied) | 1 |  |  |
| CH-0062 | V.x | Part only (never applied) | 1 |  |  |
| CH-0063 | V.x | Part only (never applied) | 1 |  |  |
| CH-0064 | V.x | Part only (never applied) | 1 |  |  |
| CH-0065 | V.x | Part only (never applied) | 1 |  |  |
| CH-0066 | V.x | Part only (never applied) | 1 |  |  |
| CH-0147 | V.x | Part only (never applied) | 1 |  |  |
| CH-0687 | VI.1 | its sentences, one section | 1 | L285.s1 |  |
| CH-0422 | VI.1 | its sentences, one section | 2 | L287.s2 |  |
| CH-0425 | VI.1 | its sentences, one section | 1 | L287.s2 |  |
| CH-1266 | VI.1 | its sentences, one section | 1 | L293.s2 |  |
| CH-0557 | VI.1 | its sentences, one section | 1 | L299.s1 |  |
| CH-0141 | VI.1 | its sentences, one section | 3 | L299.s2 |  |
| CH-0283 | VI.1 | its sentences, one section | 1 | L299.s2 |  |
| CH-0362 | VI.1 | its sentences, one section | 2 | L299.s2 |  |
| CH-0382 | VI.1 | its sentences, one section | 1 | L299.s2 |  |
| CH-0526 | VI.1 | its sentences, one section | 1 | L299.s2 |  |
| CH-0688 | VI.1 | its sentences, one section | 1 | L299.s2 |  |
| CH-0922 | VI.1 | its sentences, one section | 3 | L299.s2 |  |
| CH-1230 | VI.1 | its sentences, one section | 2 | L299.s3 |  |
| CH-1212 | VI.1 | its sentences, one section | 1 | L301.s1 |  |
| CH-1231 | VI.1 | its sentences, one section | 2 | L301.s1 |  |
| CH-1233 | VI.1 | its sentences, one section | 1 | L301.s1 |  |
| CH-0165 | VI.1 | section lead 0.52 (never applied) | 2 |  |  |
| CH-0689 | VI.2 | its sentences, one section | 1 | L305.s1 |  |
| CH-1012 | VI.2 | its sentences, one section | 2 | L305.s1 |  |
| CH-1174 | VI.2 | most of its sentences (2 sections) | 1 | L305.s1 | XV.5 ((Prov) Genesis) |
| CH-0692 | VI.2 | its sentences, one section | 1 | L305.s2 |  |
| CH-0690 | VI.2 | its sentences, one section | 1 | L305.s3 |  |
| CH-0284 | VI.2 | its sentences, one section | 1 | L305.s5 |  |
| CH-0691 | VI.2 | its sentences, one section | 1 | L305.s5 |  |
| CH-0923 | VI.2 | its sentences, one section | 2 | L305.s5 |  |
| CH-0286 | VI.3 | its sentences, one section | 1 | L307.s2 |  |
| CH-0696 | VI.3 | its sentences, one section | 1 | L307.s2 |  |
| CH-0446 | VI.3 | its sentences, one section | 1 | L307.s3 |  |
| CH-0693 | VI.3 | its sentences, one section | 1 | L307.s3 |  |
| CH-0924 | VI.3 | its sentences, one section | 3 | L307.s3 |  |
| CH-0694 | VI.3 | its sentences, one section | 1 | L307.s4 |  |
| CH-0285 | VI.3 | its sentences, one section | 1 | L307.s5 |  |
| CH-0383 | VI.3 | its sentences, one section | 2 | L307.s5 |  |
| CH-0695 | VI.3 | its sentences, one section | 1 | L307.s5 |  |
| CH-0697 | VI.3 | its sentences, one section | 1 | L309.s1 |  |
| CH-0098 | VI.3 | section lead 0.73 (never applied) | 2 |  |  |
| CH-0698 | VI.4 | its sentences, one section | 1 | L311.s1 |  |
| CH-0699 | VI.4 | its sentences, one section | 1 | L311.s1 |  |
| CH-0925 | VI.4 | its sentences, one section | 2 | L311.s1 |  |
| CH-1013 | VI.4 | its sentences, one section | 2 | L311.s1 |  |
| CH-0430 | VI.5 | its sentences, one section | 2 | L313.s1 |  |
| CH-1260 | VI.5 | its sentences, one section | 1 | L313.s1 |  |
| CH-1264 | VI.5 | its sentences, one section | 1 | L313.s1 |  |
| CH-1268 | VI.5 | its sentences, one section | 1 | L313.s1 |  |
| CH-0428 | VI.5 | its sentences, one section | 2 | L313.s2 |  |
| CH-0473 | VI.5 | its sentences, one section | 1 | L313.s2 |  |
| CH-0474 | VI.5 | its sentences, one section | 1 | L313.s2 |  |
| CH-0700 | VI.5 | its sentences, one section | 1 | L313.s2 |  |
| CH-0701 | VI.5 | its sentences, one section | 1 | L313.s2 |  |
| CH-1258 | VI.5 | its sentences, one section | 1 | L313.s2 |  |
| CH-1262 | VI.5 | its sentences, one section | 1 | L313.s2 |  |
| CH-1270 | VI.5 | its sentences, one section | 1 | L313.s2 |  |
| CH-0431 | VI.5 | its sentences, one section | 1 | L313.s3 |  |
| CH-0575 | VI.5 | its sentences, one section | 1 | L313.s3 |  |
| CH-0702 | VI.5 | its sentences, one section | 1 | L313.s3 |  |
| CH-1263 | VI.5 | its sentences, one section | 1 | L313.s3 |  |
| CH-1267 | VI.5 | its sentences, one section | 1 | L313.s3 |  |
| CH-0533 | VI.6 | its sentences, one section | 1 | L315.s1 |  |
| CH-0555 | VI.6 | its sentences, one section | 1 | L315.s1 |  |
| CH-1113 | VI.6 | most of its sentences (2 sections) | 3 | L315.s1 | VIII.5 (A failed answer stays failed) |
| CH-1239 | VI.6 | its sentences, one section | 2 | L315.s1 |  |
| CH-0447 | VI.6 | most of its sentences (2 sections) | 2 | L315.s2 | VII.1 (opening of Part VII) |
| CH-0703 | VI.6 | its sentences, one section | 1 | L315.s2 |  |
| CH-0894 | VI.6 | its sentences, one section | 1 | L315.s2 |  |
| CH-0988 | VI.6 | its sentences, one section | 1 | L315.s3 |  |
| CH-0536 | VI.6 | its sentences, one section | 1 | L315.s5 |  |
| CH-0705 | VI.6 | its sentences, one section | 1 | L315.s5 |  |
| CH-1221 | VI.6 | its sentences, one section | 1 | L315.s5 |  |
| CH-0704 | VI.6 | its sentences, one section | 1 | L315.s6 |  |
| CH-0926 | VI.6 | its sentences, one section | 3 | L315.s6 |  |
| CH-1240 | VI.6 | its sentences, one section | 2 | L315.s7 |  |
| CH-0706 | VI.6 | its sentences, one section | 1 | L315.s9 |  |
| CH-0903 | VI.6 | its sentences, one section | 1 | L315.s9 |  |
| CH-0576 | VI.6 | its sentences, one section | 1 | L315.s11 |  |
| CH-1209 | VI.6 | its sentences, one section | 1 | L315.s11 |  |
| CH-1237 | VI.6 | its sentences, one section | 2 | L315.s11 |  |
| CH-0966 | VI.6 | its sentences, one section | 3 | L315.s12 |  |
| CH-0529 | VI.6 | its sentences, one section | 1 | L315.s13 |  |
| CH-0964 | VI.6 | its sentences, one section | 2 | L315.s13 |  |
| CH-0532 | VI.6 | its sentences, one section | 1 | L315.s14 |  |
| CH-0965 | VI.6 | its sentences, one section | 2 | L315.s14 |  |
| CH-1238 | VI.6 | its sentences, one section | 2 | L315.s14 |  |
| CH-0967 | VI.6 | its sentences, one section | 2 | L315.s18 |  |
| CH-0989 | VI.6 | its sentences, one section | 1 | L315.s18 |  |
| CH-0968 | VI.6 | its sentences, one section | 3 | L315.s20 |  |
| CH-0530 | VI.6 | its sentences, one section | 1 | L315.s21 |  |
| CH-0531 | VI.6 | its sentences, one section | 1 | L315.s21 |  |
| CH-1274 | VI.6 | section its source names (never applied) | 1 |  |  |
| CH-1275 | VI.6 | section its source names (never applied) | 1 |  |  |
| CH-0540 | VI.7 | its sentences, one section | 1 | L317.s1 |  |
| CH-0707 | VI.7 | its sentences, one section | 1 | L317.s1 |  |
| CH-1049 | VI.7 | its sentences, one section | 1 | L317.s1 |  |
| CH-1050 | VI.7 | its sentences, one section | 1 | L317.s1 |  |
| CH-1210 | VI.7 | its sentences, one section | 1 | L317.s1 |  |
| CH-1211 | VI.7 | its sentences, one section | 1 | L317.s1 |  |
| CH-1225 | VI.7 | its sentences, one section | 1 | L317.s1 |  |
| CH-0708 | VI.7 | its sentences, one section | 1 | L317.s4 |  |
| CH-0991 | VI.7 | its sentences, one section | 2 | L317.s4 |  |
| CH-1035 | VI.7 | most of its sentences (3 sections) | 1 | L317.s4 | VI.6 (Rivals); XIV.4 (Dependence order) |
| CH-1051 | VI.7 | its sentences, one section | 1 | L317.s4 |  |
| CH-1082 | VI.7 | most of its sentences (2 sections) | 1 | L317.s4 | XVI.9 (10. A two-layer episode, in exact form) |
| CH-1112 | VI.7 | most of its sentences (3 sections) | 2 | L317.s4 | VI.6 (Rivals); XIV.4 (Dependence order) |
| CH-1115 | VI.7 | its sentences, one section | 2 | L317.s4 |  |
| CH-1164 | VI.7 | its sentences, one section | 1 | L317.s4 |  |
| CH-1234 | VI.7 | its sentences, one section | 1 | L317.s4 |  |
| CH-1247 | VI.7 | its sentences, one section | 1 | L317.s4 |  |
| CH-0927 | VI.7 | its sentences, one section | 3 | L317.s5 |  |
| CH-0709 | VI.7 | its sentences, one section | 1 | L317.s7 |  |
| CH-0905 | VI.7 | its sentences, one section | 1 | L317.s7 |  |
| CH-0928 | VI.7 | its sentences, one section | 3 | L317.s7 |  |
| CH-1145 | VI.7 | its sentences, one section | 1 | L317.s7 |  |
| CH-0969 | VI.7 | its sentences, one section | 2 | L317.s8 |  |
| CH-0990 | VI.7 | its sentences, one section | 1 | L317.s9 |  |
| CH-1052 | VI.7 | its sentences, one section | 1 | L317.s9 |  |
| CH-1116 | VI.7 | its sentences, one section | 2 | L317.s9 |  |
| CH-0710 | VI.7 | its sentences, one section | 1 | L317.s11 |  |
| CH-1167 | VI.7 | its sentences, one section | 1 | L317.s11 |  |
| CH-1244 | VI.7 | its sentences, one section | 1 | L317.s11 |  |
| CH-1250 | VI.7 | its sentences, one section | 1 | L317.s11 |  |
| CH-0535 | VI.7 | its sentences, one section | 1 | L317.s13 |  |
| CH-0711 | VI.7 | its sentences, one section | 1 | L317.s13 |  |
| CH-0717 | VI.7 | its sentences, one section | 1 | L317.s13 |  |
| CH-0712 | VI.7 | its sentences, one section | 1 | L317.s14 |  |
| CH-0713 | VI.7 | its sentences, one section | 1 | L317.s14 |  |
| CH-0895 | VI.7 | its sentences, one section | 1 | L317.s14 |  |
| CH-0970 | VI.7 | its sentences, one section | 2 | L317.s14 |  |
| CH-0992 | VI.7 | its sentences, one section | 1 | L317.s14 |  |
| CH-1154 | VI.7 | its sentences, one section | 1 | L317.s14 |  |
| CH-0714 | VI.7 | its sentences, one section | 1 | L317.s15 |  |
| CH-0715 | VI.7 | its sentences, one section | 1 | L317.s16 |  |
| CH-0904 | VI.7 | its sentences, one section | 3 | L317.s16 |  |
| CH-1228 | VI.7 | its sentences, one section | 1 | L317.s16 |  |
| CH-1229 | VI.7 | its sentences, one section | 1 | L317.s16 |  |
| CH-0716 | VI.7 | its sentences, one section | 1 | L317.s17 |  |
| CH-0104 | VI.7 | section lead 0.56 (never applied) | 2 |  |  |
| CH-0097 | VI.x | Part only (never applied) | 2 |  |  |
| CH-0099 | VI.x | Part only (never applied) | 1 |  |  |
| CH-0100 | VI.x | Part only (never applied) | 3 |  |  |
| CH-0101 | VI.x | Part only (never applied) | 1 |  |  |
| CH-0102 | VI.x | Part only (never applied) | 3 |  |  |
| CH-0103 | VI.x | Part only (never applied) | 2 |  |  |
| CH-0164 | VI.x | Part only (never applied) | 2 |  |  |
| CH-0169 | VI.x | Part only (never applied) | 1 |  |  |
| CH-0475 | VII.1 | its sentences, one section | 1 | L321.s1 |  |
| CH-1271 | VII.1 | its sentences, one section | 1 | L321.s1 |  |
| CH-1014 | VII.1 | its sentences, one section | 2 | L325.s1 |  |
| CH-0448 | VII.1 | its sentences, one section | 2 | L325.s5 |  |
| CH-0541 | VII.1 | its sentences, one section | 1 | L325.s5 |  |
| CH-0718 | VII.1 | its sentences, one section | 1 | L325.s7 |  |
| CH-0550 | VII.1 | section its source names (not locatable) | 1 |  |  |
| CH-1015 | VII.2 | its sentences, one section | 5 | L329.s4 |  |
| CH-0719 | VII.2 | its sentences, one section | 1 | L331.s3 |  |
| CH-0930 | VII.2 | its sentences, one section | 3 | L331.s3 |  |
| CH-1139 | VII.2 | its sentences, one section | 1 | L331.s3 |  |
| CH-0720 | VII.2 | its sentences, one section | 1 | L335.s2 |  |
| CH-0721 | VII.2 | its sentences, one section | 1 | L335.s3 |  |
| CH-0931 | VII.2 | its sentences, one section | 3 | L335.s3 |  |
| CH-0571 | VII.2 | section its source names (never applied) | 1 |  |  |
| CH-0722 | VII.3 | its sentences, one section | 1 | L339.s3 |  |
| CH-1016 | VII.3 | its sentences, one section | 3 | L339.s3 |  |
| CH-0287 | VII.3 | its sentences, one section | 1 | L339.s4 |  |
| CH-0440 | VII.3 | its sentences, one section | 2 | L339.s4 |  |
| CH-0723 | VII.3 | its sentences, one section | 1 | L339.s4 |  |
| CH-0483 | VII.3 | its sentences, one section | 2 | L339.s5 |  |
| CH-0515 | VII.3 | its sentences, one section | 1 | L339.s5 |  |
| CH-1153 | VII.4 | its sentences, one section | 1 | L343.s1 |  |
| CH-0726 | VII.4 | its sentences, one section | 1 | L343.s3 |  |
| CH-0727 | VII.4 | its sentences, one section | 1 | L343.s4 |  |
| CH-0491 | VII.4 | its sentences, one section | 1 | L343.s5 |  |
| CH-0724 | VII.4 | its sentences, one section | 1 | L343.s5 |  |
| CH-1183 | VII.4 | most of its sentences (2 sections) | 1 | L343.s5 | XVI.9 (10. A two-layer episode, in exact form) |
| CH-0896 | VII.4 | its sentences, one section | 1 | L343.s6 |  |
| CH-0725 | VII.4 | its sentences, one section | 1 | L343.s9 |  |
| CH-1226 | VII.4 | its sentences, one section | 1 | L347.s1 |  |
| CH-0449 | VIII.1 | its sentences, one section | 2 | L353.s1 |  |
| CH-0476 | VIII.1 | its sentences, one section | 1 | L353.s2 |  |
| CH-0728 | VIII.1 | its sentences, one section | 1 | L353.s2 |  |
| CH-0729 | VIII.1 | its sentences, one section | 1 | L353.s3 |  |
| CH-0482 | VIII.2 | its sentences, one section | 1 | L363.s1 |  |
| CH-0409 | VIII.2 | its sentences, one section | 7 | L363.s2 |  |
| CH-0421 | VIII.2 | its sentences, one section | 1 | L363.s2 |  |
| CH-0574 | VIII.2 | its sentences, one section | 1 | L363.s2 |  |
| CH-0730 | VIII.2 | its sentences, one section | 1 | L363.s2 |  |
| CH-0288 | VIII.3 | its sentences, one section | 1 | L365.s1 |  |
| CH-0289 | VIII.3 | its sentences, one section | 1 | L365.s1 |  |
| CH-0384 | VIII.3 | its sentences, one section | 1 | L365.s1 |  |
| CH-0731 | VIII.3 | its sentences, one section | 1 | L365.s1 |  |
| CH-0290 | VIII.3 | its sentences, one section | 1 | L365.s2 |  |
| CH-0385 | VIII.3 | its sentences, one section | 1 | L365.s2 |  |
| CH-0163 | VIII.3 | section lead 0.77 (never applied) | 1 |  |  |
| CH-1256 | VIII.4 | its sentences, one section | 1 | L367.s1 |  |
| CH-1261 | VIII.4 | its sentences, one section | 1 | L367.s1 |  |
| CH-1269 | VIII.4 | its sentences, one section | 1 | L367.s1 |  |
| CH-0450 | VIII.4 | its sentences, one section | 1 | L367.s2 |  |
| CH-1272 | VIII.4 | its sentences, one section | 1 | L367.s2 |  |
| CH-0732 | VIII.5 | its sentences, one section | 1 | L369.s2 |  |
| CH-1265 | VIII.5 | its sentences, one section | 1 | L369.s2 |  |
| CH-0733 | VIII.5 | its sentences, one section | 1 | L369.s3 |  |
| CH-0734 | VIII.5 | its sentences, one section | 1 | L369.s4 |  |
| CH-0932 | VIII.5 | its sentences, one section | 3 | L369.s4 |  |
| CH-1108 | VIII.5 | its sentences, one section | 1 | L369.s4 |  |
| CH-1157 | VIII.5 | its sentences, one section | 1 | L369.s4 |  |
| CH-0543 | VIII.5 | its sentences, one section | 1 | L369.s5 |  |
| CH-1017 | VIII.5 | its sentences, one section | 2 | L369.s5 |  |
| CH-0542 | VIII.5 | its sentences, one section | 1 | L369.s6 |  |
| CH-0994 | VIII.5 | its sentences, one section | 1 | L369.s6 |  |
| CH-0142 | VIII.x | Part only (never applied) | 3 |  |  |
| CH-0735 | IX.1 | its sentences, one section | 1 | L373.s1 |  |
| CH-1053 | IX.1 | most of its sentences (2 sections) | 1 | L373.s1 | IX.2 (Usability) |
| CH-1171 | IX.1 | its sentences, one section | 1 | L373.s1 |  |
| CH-0736 | IX.1 | its sentences, one section | 1 | L375.s2 |  |
| CH-0291 | IX.1 | its sentences, one section | 1 | L375.s3 |  |
| CH-0386 | IX.1 | its sentences, one section | 1 | L375.s3 |  |
| CH-0737 | IX.1 | its sentences, one section | 1 | L377.s1 |  |
| CH-1018 | IX.1 | most of its sentences (6 sections) | 15 | L377.s1 | IX.2 (Usability); X.4 (Origin); XI.3 (Created explanation); XI.4 (Result, and the index of (EX)) |
| CH-1120 | IX.1 | most of its sentences (2 sections) | 2 | L377.s1 | XII.3 (Owned capability) |
| CH-0451 | IX.1 | its sentences, one section | 2 | L377.s2 |  |
| CH-0477 | IX.1 | its sentences, one section | 1 | L377.s2 |  |
| CH-0492 | IX.1 | its sentences, one section | 1 | L377.s2 |  |
| CH-1248 | IX.1 | its sentences, one section | 1 | L379.s1 |  |
| CH-0452 | IX.1 | its sentences, one section | 1 | L383.s2 |  |
| CH-0570 | IX.1 | its sentences, one section | 1 | L383.s2 |  |
| CH-0738 | IX.1 | its sentences, one section | 1 | L383.s2 |  |
| CH-1055 | IX.1 | its sentences, one section | 1 | L383.s2 |  |
| CH-0739 | IX.1 | its sentences, one section | 1 | L385.s2 |  |
| CH-0933 | IX.1 | its sentences, one section | 3 | L385.s2 |  |
| CH-1056 | IX.1 | its sentences, one section | 3 | L385.s2 |  |
| CH-0740 | IX.2 | its sentences, one section | 1 | L387.s1 |  |
| CH-1172 | IX.2 | its sentences, one section | 1 | L387.s1 |  |
| CH-0553 | IX.2 | its sentences, one section | 1 | L389.s1 |  |
| CH-0741 | IX.2 | its sentences, one section | 1 | L389.s1 |  |
| CH-0742 | IX.2 | its sentences, one section | 1 | L393.s1 |  |
| CH-0908 | IX.2 | its sentences, one section | 3 | L393.s1 |  |
| CH-1208 | IX.2 | its sentences, one section | 1 | L393.s1 |  |
| CH-0971 | IX.2 | its sentences, one section | 2 | L393.s2 |  |
| CH-1054 | IX.2 | most of its sentences (2 sections) | 1 | L393.s4 | XVI.7 (7. The frozen assessment and the moving question are consistent) |
| CH-1119 | IX.2 | most of its sentences (2 sections) | 3 | L393.s4 | XVI.7 (7. The frozen assessment and the moving question are consistent) |
| CH-1188 | IX.2 | its sentences, one section | 1 | L393.s4 |  |
| CH-0743 | IX.2 | its sentences, one section | 1 | L395.s1 |  |
| CH-1121 | IX.2 | its sentences, one section | 2 | L395.s1 |  |
| CH-0292 | IX.3 | its sentences, one section | 1 | L397.s1 |  |
| CH-0387 | IX.3 | its sentences, one section | 1 | L397.s1 |  |
| CH-0744 | IX.3 | its sentences, one section | 1 | L397.s1 |  |
| CH-0907 | IX.3 | its sentences, one section | 5 | L397.s1 |  |
| CH-1168 | IX.3 | its sentences, one section | 1 | L397.s1 |  |
| CH-1169 | IX.3 | its sentences, one section | 1 | L397.s1 |  |
| CH-1170 | IX.3 | its sentences, one section | 1 | L397.s1 |  |
| CH-0745 | IX.3 | its sentences, one section | 1 | L397.s2 |  |
| CH-1039 | IX.3 | its sentences, one section | 1 | L397.s5 |  |
| CH-1118 | IX.3 | its sentences, one section | 3 | L397.s5 |  |
| CH-0746 | IX.3 | its sentences, one section | 1 | L397.s6 |  |
| CH-0972 | IX.3 | its sentences, one section | 2 | L397.s7 |  |
| CH-0993 | IX.3 | its sentences, one section | 1 | L397.s7 |  |
| CH-1198 | IX.3 | its sentences, one section | 1 | L397.s7 |  |
| CH-0973 | IX.3 | its sentences, one section | 2 | L397.s11 |  |
| CH-0974 | IX.3 | its sentences, one section | 2 | L397.s12 |  |
| CH-0534 | IX.3 | its sentences, one section | 1 | L397.s13 |  |
| CH-0747 | IX.3 | its sentences, one section | 1 | L397.s16 |  |
| CH-0975 | IX.3 | its sentences, one section | 2 | L397.s16 |  |
| CH-1197 | IX.3 | its sentences, one section | 2 | L397.s16 |  |
| CH-0976 | IX.3 | its sentences, one section | 3 | L397.s18 |  |
| CH-0173 | IX.x | Part only (not locatable) | 1 |  |  |
| CH-0293 | X.1 | its sentences, one section | 1 | L403.s1 |  |
| CH-0748 | X.1 | its sentences, one section | 1 | L403.s1 |  |
| CH-0749 | X.1 | its sentences, one section | 1 | L403.s1 |  |
| CH-0750 | X.1 | its sentences, one section | 1 | L403.s3 |  |
| CH-1205 | X.1 | its sentences, one section | 2 | L403.s3 |  |
| CH-0294 | X.1 | its sentences, one section | 1 | L403.s4 |  |
| CH-0388 | X.1 | its sentences, one section | 1 | L403.s4 |  |
| CH-0751 | X.1 | its sentences, one section | 1 | L403.s4 |  |
| CH-1140 | X.1 | section lead 1.00 (not locatable) | 1 |  |  |
| CH-0085 | X.2 | its sentences, one section | 7 | L405.s1 |  |
| CH-0439 | X.2 | its sentences, one section | 2 | L405.s1 |  |
| CH-0752 | X.2 | its sentences, one section | 1 | L405.s1 |  |
| CH-0753 | X.2 | its sentences, one section | 1 | L405.s2 |  |
| CH-0295 | X.2 | its sentences, one section | 1 | L405.s4 |  |
| CH-0389 | X.2 | its sentences, one section | 1 | L405.s4 |  |
| CH-0578 | X.2 | its sentences, one section | 1 | L405.s4 |  |
| CH-0161 | X.2 | its sentences, one section | 2 | L405.s5 |  |
| CH-0296 | X.2 | its sentences, one section | 1 | L405.s5 |  |
| CH-0390 | X.2 | its sentences, one section | 2 | L405.s5 |  |
| CH-0513 | X.2 | its sentences, one section | 1 | L405.s5 |  |
| CH-0511 | X.3 | its sentences, one section | 1 | L409.s5 |  |
| CH-0512 | X.3 | its sentences, one section | 1 | L409.s5 |  |
| CH-0754 | X.3 | its sentences, one section | 1 | L409.s5 |  |
| CH-0755 | X.3 | its sentences, one section | 1 | L411.s3 |  |
| CH-0453 | X.4 | its sentences, one section | 1 | L413.s1 |  |
| CH-0502 | X.4 | its sentences, one section | 1 | L413.s1 |  |
| CH-0503 | X.4 | its sentences, one section | 1 | L413.s1 |  |
| CH-1019 | X.4 | its sentences, one section | 2 | L413.s1 |  |
| CH-0003 | X.4 | its sentences, one section | 1 | L425.s1 |  |
| CH-0297 | X.4 | its sentences, one section | 1 | L425.s3 |  |
| CH-0391 | X.4 | its sentences, one section | 1 | L425.s3 |  |
| CH-0298 | X.5 | its sentences, one section | 1 | L427.s1 |  |
| CH-0299 | X.5 | its sentences, one section | 1 | L427.s1 |  |
| CH-0300 | X.5 | its sentences, one section | 1 | L427.s2 |  |
| CH-0361 | X.5 | its sentences, one section | 2 | L427.s2 |  |
| CH-0365 | X.5 | most of its sentences (2 sections) | 3 | L427.s2 | XII.2 (System boundary and continuity) |
| CH-0392 | X.5 | its sentences, one section | 2 | L427.s2 |  |
| CH-0756 | X.5 | its sentences, one section | 1 | L427.s3 |  |
| CH-0301 | X.5 | its sentences, one section | 1 | L427.s4 |  |
| CH-0757 | X.5 | its sentences, one section | 1 | L427.s4 |  |
| CH-1071 | X.5 | most of its sentences (2 sections) | 1 | L427.s4 | XII.3 (Owned capability) |
| CH-1146 | X.5 | its sentences, one section | 1 | L427.s4 |  |
| CH-0168 | X.5 | section lead 0.56 (never applied) | 2 |  |  |
| CH-1064 | X.6 | its sentences, one section | 1 | L429.s1 |  |
| CH-1176 | X.6 | its sentences, one section | 1 | L429.s1 |  |
| CH-1236 | X.6 | its sentences, one section | 1 | L429.s1 |  |
| CH-0759 | X.6 | its sentences, one section | 1 | L429.s2 |  |
| CH-0760 | X.6 | its sentences, one section | 1 | L429.s2 |  |
| CH-1235 | X.6 | its sentences, one section | 1 | L429.s2 |  |
| CH-1246 | X.6 | its sentences, one section | 1 | L429.s2 |  |
| CH-0758 | X.6 | its sentences, one section | 1 | L429.s3 |  |
| CH-0934 | X.6 | its sentences, one section | 3 | L429.s4 |  |
| CH-0977 | X.6 | its sentences, one section | 2 | L429.s4 |  |
| CH-0111 | X.x | Part only (never applied) | 1 |  |  |
| CH-0112 | X.x | Part only (never applied) | 3 |  |  |
| CH-0113 | X.x | Part only (never applied) | 3 |  |  |
| CH-0114 | X.x | Part only (never applied) | 1 |  |  |
| CH-0115 | X.x | Part only (never applied) | 3 |  |  |
| CH-0116 | X.x | Part only (never applied) | 3 |  |  |
| CH-0117 | X.x | Part only (never applied) | 2 |  |  |
| CH-0153 | X.x | Part only (never applied) | 1 |  |  |
| CH-0154 | X.x | Part only (never applied) | 1 |  |  |
| CH-0761 | XI.1 | its sentences, one section | 1 | L433.s1 |  |
| CH-1104 | XI.1 | its sentences, one section | 1 | L433.s1 |  |
| CH-0454 | XI.1 | its sentences, one section | 1 | L435.s1 |  |
| CH-0762 | XI.1 | its sentences, one section | 1 | L435.s2 |  |
| CH-0763 | XI.1 | its sentences, one section | 1 | L435.s2 |  |
| CH-0581 | XI.1 | its sentences, one section | 1 | L437.s1 |  |
| CH-0158 | XI.1 | section its source names (never applied) | 5 |  |  |
| CH-0302 | XI.2 | its sentences, one section | 1 | L441.s1 |  |
| CH-0303 | XI.2 | its sentences, one section | 1 | L441.s1 |  |
| CH-0393 | XI.2 | its sentences, one section | 1 | L441.s1 |  |
| CH-0455 | XI.2 | its sentences, one section | 1 | L441.s1 |  |
| CH-0768 | XI.2 | its sentences, one section | 1 | L441.s1 |  |
| CH-0004 | XI.2 | its sentences, one section | 1 | L441.s2 |  |
| CH-0562 | XI.2 | its sentences, one section | 1 | L441.s2 |  |
| CH-0764 | XI.2 | its sentences, one section | 1 | L441.s2 |  |
| CH-0394 | XI.2 | its sentences, one section | 1 | L441.s3 |  |
| CH-0765 | XI.2 | its sentences, one section | 1 | L441.s3 |  |
| CH-1147 | XI.2 | its sentences, one section | 1 | L441.s3 |  |
| CH-1243 | XI.2 | its sentences, one section | 2 | L441.s4 |  |
| CH-0304 | XI.2 | its sentences, one section | 1 | L441.s5 |  |
| CH-0395 | XI.2 | its sentences, one section | 1 | L441.s5 |  |
| CH-0766 | XI.2 | its sentences, one section | 1 | L441.s5 |  |
| CH-0935 | XI.2 | its sentences, one section | 3 | L441.s5 |  |
| CH-0155 | XI.2 | its sentences, one section | 3 | L441.s6 |  |
| CH-0305 | XI.2 | its sentences, one section | 1 | L441.s6 |  |
| CH-0396 | XI.2 | its sentences, one section | 1 | L441.s6 |  |
| CH-0767 | XI.2 | its sentences, one section | 1 | L441.s6 |  |
| CH-0769 | XI.3 | its sentences, one section | 1 | L443.s1 |  |
| CH-1089 | XI.3 | its sentences, one section | 1 | L443.s1 |  |
| CH-1090 | XI.3 | its sentences, one section | 1 | L443.s1 |  |
| CH-1189 | XI.3 | its sentences, one section | 1 | L443.s2 |  |
| CH-0770 | XI.3 | its sentences, one section | 1 | L445.s1 |  |
| CH-0771 | XI.3 | its sentences, one section | 1 | L445.s1 |  |
| CH-0772 | XI.3 | its sentences, one section | 1 | L445.s1 |  |
| CH-0456 | XI.4 | its sentences, one section | 1 | L453.s2 |  |
| CH-0773 | XI.4 | its sentences, one section | 1 | L453.s2 |  |
| CH-0002 | XI.4 | its sentences, one section | 1 | L453.s5 |  |
| CH-0774 | XI.4 | its sentences, one section | 1 | L453.s5 |  |
| CH-0936 | XI.4 | its sentences, one section | 3 | L453.s5 |  |
| CH-0307 | XI.5 | its sentences, one section | 1 | L455.s1 |  |
| CH-0495 | XI.5 | its sentences, one section | 1 | L455.s1 |  |
| CH-0775 | XI.5 | its sentences, one section | 1 | L455.s1 |  |
| CH-1097 | XI.5 | its sentences, one section | 1 | L455.s1 |  |
| CH-1206 | XI.5 | its sentences, one section | 2 | L455.s1 |  |
| CH-0308 | XI.5 | its sentences, one section | 1 | L455.s2 |  |
| CH-0348 | XI.5 | its sentences, one section | 4 | L455.s2 |  |
| CH-0397 | XI.5 | its sentences, one section | 1 | L455.s2 |  |
| CH-0484 | XI.5 | its sentences, one section | 3 | L455.s2 |  |
| CH-0310 | XI.5 | its sentences, one section | 1 | L455.s3 |  |
| CH-0496 | XI.5 | its sentences, one section | 1 | L455.s3 |  |
| CH-1020 | XI.5 | its sentences, one section | 3 | L455.s3 |  |
| CH-0309 | XI.5 | its sentences, one section | 1 | L455.s4 |  |
| CH-0126 | XI.5 | its sentences, one section | 2 | L455.s5 |  |
| CH-0306 | XI.5 | its sentences, one section | 1 | L455.s5 |  |
| CH-0311 | XI.5 | its sentences, one section | 1 | L455.s5 |  |
| CH-0398 | XI.5 | its sentences, one section | 1 | L455.s5 |  |
| CH-0776 | XI.5 | its sentences, one section | 1 | L455.s5 |  |
| CH-0118 | XI.x | Part only (never applied) | 3 |  |  |
| CH-0119 | XI.x | Part only (never applied) | 3 |  |  |
| CH-0120 | XI.x | Part only (never applied) | 2 |  |  |
| CH-0121 | XI.x | Part only (never applied) | 3 |  |  |
| CH-0122 | XI.x | Part only (never applied) | 2 |  |  |
| CH-0123 | XI.x | Part only (never applied) | 2 |  |  |
| CH-0124 | XI.x | Part only (never applied) | 1 |  |  |
| CH-0125 | XI.x | Part only (never applied) | 2 |  |  |
| CH-0156 | XI.x | Part only (never applied) | 5 |  |  |
| CH-0433 | XI.x | Part only (not locatable) | 1 |  |  |
| CH-0937 | XII.1 | its sentences, one section | 3 | L461.s1 |  |
| CH-0777 | XII.1 | its sentences, one section | 1 | L461.s2 |  |
| CH-0897 | XII.1 | its sentences, one section | 1 | L461.s3 |  |
| CH-0978 | XII.1 | its sentences, one section | 2 | L461.s4 |  |
| CH-0778 | XII.1 | its sentences, one section | 1 | L469.s1 |  |
| CH-1102 | XII.1 | its sentences, one section | 1 | L469.s1 |  |
| CH-0312 | XII.2 | its sentences, one section | 1 | L473.s1 |  |
| CH-0313 | XII.2 | its sentences, one section | 1 | L473.s1 |  |
| CH-0399 | XII.2 | its sentences, one section | 2 | L473.s1 |  |
| CH-0314 | XII.2 | its sentences, one section | 1 | L473.s2 |  |
| CH-0567 | XII.2 | its sentences, one section | 1 | L473.s2 |  |
| CH-0315 | XII.2 | its sentences, one section | 1 | L473.s3 |  |
| CH-0316 | XII.3 | its sentences, one section | 1 | L475.s3 |  |
| CH-0400 | XII.3 | its sentences, one section | 1 | L475.s3 |  |
| CH-0779 | XII.3 | its sentences, one section | 1 | L475.s3 |  |
| CH-1148 | XII.3 | its sentences, one section | 1 | L475.s3 |  |
| CH-0780 | XII.3 | its sentences, one section | 1 | L477.s1 |  |
| CH-0130 | XII.3 | section lead 0.51 (never applied) | 2 |  |  |
| CH-0781 | XII.4 | its sentences, one section | 1 | L479.s1 |  |
| CH-0938 | XII.4 | its sentences, one section | 3 | L479.s1 |  |
| CH-1194 | XII.4 | its sentences, one section | 1 | L479.s1 |  |
| CH-0457 | XII.4 | its sentences, one section | 1 | L479.s2 |  |
| CH-0782 | XII.4 | its sentences, one section | 1 | L479.s2 |  |
| CH-0783 | XII.4 | its sentences, one section | 1 | L479.s2 |  |
| CH-0784 | XII.4 | its sentences, one section | 1 | L479.s2 |  |
| CH-0785 | XII.4 | its sentences, one section | 1 | L479.s4 |  |
| CH-1103 | XII.4 | its sentences, one section | 1 | L479.s4 |  |
| CH-0351 | XII.5 | its sentences, one section | 3 | L481.s1 |  |
| CH-0786 | XII.5 | its sentences, one section | 1 | L481.s2 |  |
| CH-0317 | XII.5 | its sentences, one section | 1 | L481.s3 |  |
| CH-0401 | XII.5 | its sentences, one section | 1 | L481.s3 |  |
| CH-0569 | XII.5 | its sentences, one section | 1 | L481.s3 |  |
| CH-0127 | XII.x | Part only (never applied) | 2 |  |  |
| CH-0128 | XII.x | Part only (never applied) | 3 |  |  |
| CH-0129 | XII.x | Part only (never applied) | 1 |  |  |
| CH-0131 | XII.x | Part only (never applied) | 2 |  |  |
| CH-0170 | XII.x | Part only (never applied) | 1 |  |  |
| CH-0432 | XII.x | Part only (never applied) | 1 |  |  |
| CH-0787 | XIII.1 | its sentences, one section | 1 | L495.s2 |  |
| CH-0939 | XIII.1 | its sentences, one section | 3 | L495.s2 |  |
| CH-1063 | XIII.1 | most of its sentences (3 sections) | 1 | L495.s2 | XV.5 ((Prov) Genesis); XV.6 ((QF) Question-finding) |
| CH-0458 | XIII.1 | its sentences, one section | 1 | L495.s3 |  |
| CH-0788 | XIII.1 | its sentences, one section | 1 | L495.s3 |  |
| CH-0559 | XIII.2 | its sentences, one section | 1 | L497.s1 |  |
| CH-0979 | XIII.2 | its sentences, one section | 2 | L497.s1 |  |
| CH-1021 | XIII.2 | most of its sentences (2 sections) | 5 | L497.s1 | XIII.1 (Barriers) |
| CH-1109 | XIII.2 | its sentences, one section | 1 | L497.s1 |  |
| CH-1196 | XIII.2 | its sentences, one section | 1 | L497.s1 |  |
| CH-0789 | XIII.2 | its sentences, one section | 1 | L509.s1 |  |
| CH-0139 | XIII.2 | section lead 0.72 (never applied) | 2 |  |  |
| CH-0132 | XIII.x | Part only (never applied) | 3 |  |  |
| CH-0133 | XIII.x | Part only (never applied) | 2 |  |  |
| CH-0134 | XIII.x | Part only (never applied) | 2 |  |  |
| CH-0135 | XIII.x | Part only (never applied) | 3 |  |  |
| CH-0136 | XIII.x | Part only (never applied) | 1 |  |  |
| CH-0137 | XIII.x | Part only (never applied) | 1 |  |  |
| CH-0138 | XIII.x | Part only (never applied) | 2 |  |  |
| CH-0140 | XIII.x | Part only (never applied) | 1 |  |  |
| CH-0157 | XIII.x | Part only (never applied) | 5 |  |  |
| CH-0790 | XIV.1 | its sentences, one section | 1 | L515.s1 |  |
| CH-0791 | XIV.1 | its sentences, one section | 1 | L517.s1 |  |
| CH-1249 | XIV.1 | its sentences, one section | 1 | L517.s1 |  |
| CH-0318 | XIV.1 | its sentences, one section | 1 | L518.s1 |  |
| CH-0319 | XIV.1 | its sentences, one section | 1 | L518.s1 |  |
| CH-0402 | XIV.1 | its sentences, one section | 1 | L518.s1 |  |
| CH-0792 | XIV.1 | its sentences, one section | 1 | L518.s1 |  |
| CH-0793 | XIV.1 | its sentences, one section | 1 | L518.s1 |  |
| CH-0940 | XIV.1 | its sentences, one section | 3 | L518.s1 |  |
| CH-0324 | XIV.2 | its sentences, one section | 1 | L520.s1 |  |
| CH-0354 | XIV.2 | its sentences, one section | 2 | L520.s1 |  |
| CH-0794 | XIV.2 | its sentences, one section | 1 | L520.s1 |  |
| CH-0998 | XIV.2 | most of its sentences (3 sections) | 5 | L520.s1 | 0.4 (What is imported, what is an index, and what is defined); XVI.6 (6. There are two imports) |
| CH-0320 | XIV.2 | its sentences, one section | 1 | L520.s6 |  |
| CH-0795 | XIV.2 | its sentences, one section | 1 | L520.s8 |  |
| CH-0321 | XIV.3 | its sentences, one section | 1 | L522.s1 |  |
| CH-0322 | XIV.3 | its sentences, one section | 1 | L522.s1 |  |
| CH-0403 | XIV.3 | its sentences, one section | 1 | L522.s1 |  |
| CH-0426 | XIV.3 | its sentences, one section | 1 | L522.s1 |  |
| CH-0556 | XIV.3 | its sentences, one section | 1 | L522.s1 |  |
| CH-0558 | XIV.3 | its sentences, one section | 1 | L522.s1 |  |
| CH-0796 | XIV.3 | its sentences, one section | 1 | L522.s1 |  |
| CH-0797 | XIV.3 | its sentences, one section | 1 | L522.s1 |  |
| CH-0798 | XIV.3 | its sentences, one section | 1 | L522.s1 |  |
| CH-0800 | XIV.3 | its sentences, one section | 1 | L522.s1 |  |
| CH-0941 | XIV.3 | its sentences, one section | 3 | L522.s1 |  |
| CH-0980 | XIV.3 | its sentences, one section | 2 | L522.s1 |  |
| CH-0323 | XIV.3 | its sentences, one section | 1 | L522.s2 |  |
| CH-0549 | XIV.3 | its sentences, one section | 1 | L522.s2 |  |
| CH-0563 | XIV.3 | its sentences, one section | 1 | L522.s2 |  |
| CH-0799 | XIV.3 | its sentences, one section | 1 | L522.s2 |  |
| CH-1059 | XIV.3 | most of its sentences (2 sections) | 1 | L522.s2 | 0.3 (What this document does not claim) |
| CH-0564 | XIV.3 | its sentences, one section | 1 | L522.s3 |  |
| CH-0424 | XIV.3 | its sentences, one section | 1 | L524.s1 |  |
| CH-0801 | XIV.3 | its sentences, one section | 1 | L524.s1 |  |
| CH-0802 | XIV.3 | its sentences, one section | 1 | L524.s2 |  |
| CH-0356 | XIV.4 | its sentences, one section | 2 | L526.s1 |  |
| CH-0517 | XIV.4 | its sentences, one section | 1 | L526.s1 |  |
| CH-0803 | XIV.4 | its sentences, one section | 1 | L526.s1 |  |
| CH-1180 | XIV.4 | its sentences, one section | 1 | L526.s1 |  |
| CH-0561 | XIV.4 | its sentences, one section | 1 | L526.s5 |  |
| CH-1232 | XIV.4 | its sentences, one section | 2 | L526.s5 |  |
| CH-0942 | XIV.4 | its sentences, one section | 3 | L526.s7 |  |
| CH-0478 | XIV.4 | its sentences, one section | 1 | L526.s12 |  |
| CH-0479 | XIV.4 | its sentences, one section | 2 | L526.s12 |  |
| CH-0499 | XIV.4 | its sentences, one section | 1 | L526.s13 |  |
| CH-0538 | XIV.4 | its sentences, one section | 1 | L526.s13 |  |
| CH-0539 | XIV.4 | its sentences, one section | 1 | L526.s13 |  |
| CH-0807 | XIV.4 | its sentences, one section | 1 | L526.s13 |  |
| CH-0808 | XIV.4 | its sentences, one section | 1 | L526.s13 |  |
| CH-0809 | XIV.4 | its sentences, one section | 1 | L526.s13 |  |
| CH-0459 | XIV.4 | its sentences, one section | 2 | L526.s15 |  |
| CH-0537 | XIV.4 | its sentences, one section | 1 | L526.s15 |  |
| CH-0804 | XIV.4 | its sentences, one section | 1 | L526.s15 |  |
| CH-0898 | XIV.4 | its sentences, one section | 1 | L526.s15 |  |
| CH-0981 | XIV.4 | its sentences, one section | 2 | L526.s15 |  |
| CH-1241 | XIV.4 | its sentences, one section | 1 | L526.s15 |  |
| CH-0805 | XIV.4 | its sentences, one section | 1 | L526.s16 |  |
| CH-0912 | XIV.4 | most of its sentences (2 sections) | 4 | L526.s16 | 0.4 (What is imported, what is an index, and what is defined) |
| CH-1022 | XIV.4 | its sentences, one section | 2 | L526.s17 |  |
| CH-1069 | XIV.4 | most of its sentences (2 sections) | 1 | L526.s17 | XVI.6 (6. There are two imports) |
| CH-1179 | XIV.4 | its sentences, one section | 1 | L526.s17 |  |
| CH-0325 | XIV.4 | its sentences, one section | 1 | L526.s18 |  |
| CH-0404 | XIV.4 | its sentences, one section | 2 | L526.s18 |  |
| CH-0806 | XIV.4 | its sentences, one section | 1 | L526.s18 |  |
| CH-0943 | XIV.4 | its sentences, one section | 3 | L526.s18 |  |
| CH-0982 | XIV.4 | its sentences, one section | 2 | L526.s18 |  |
| CH-1149 | XIV.4 | its sentences, one section | 1 | L526.s18 |  |
| CH-0810 | XIV.4 | its sentences, one section | 1 | L528.s1 |  |
| CH-0811 | XIV.4 | its sentences, one section | 1 | L528.s3 |  |
| CH-0090 | XIV.x | Part only (never applied) | 4 |  |  |
| CH-0091 | XIV.x | Part only (never applied) | 2 |  |  |
| CH-0092 | XIV.x | Part only (never applied) | 2 |  |  |
| CH-0093 | XIV.x | Part only (never applied) | 4 |  |  |
| CH-0094 | XIV.x | Part only (never applied) | 1 |  |  |
| CH-0095 | XIV.x | Part only (never applied) | 2 |  |  |
| CH-0096 | XIV.x | Part only (never applied) | 2 |  |  |
| CH-0171 | XIV.x | Part only (never applied) | 1 |  |  |
| CH-0944 | XV.1 | its sentences, one section | 3 | L532.s1 |  |
| CH-0326 | XV.1 | its sentences, one section | 1 | L534.s1 |  |
| CH-0812 | XV.1 | its sentences, one section | 1 | L534.s1 |  |
| CH-1114 | XV.1 | its sentences, one section | 2 | L534.s1 |  |
| CH-0236 | XV.1 | its sentences, one section | 1 | L534.s2 |  |
| CH-0337 | XV.1 | its sentences, one section | 1 | L534.s2 |  |
| CH-0460 | XV.1 | its sentences, one section | 1 | L534.s2 |  |
| CH-0813 | XV.1 | its sentences, one section | 1 | L534.s3 |  |
| CH-0008 | XV.2 | its sentences, one section | 1 | L536.s1 |  |
| CH-0015 | XV.2 | its sentences, one section | 1 | L536.s1 |  |
| CH-0016 | XV.2 | its sentences, one section | 1 | L536.s1 |  |
| CH-0234 | XV.2 | its sentences, one section | 1 | L536.s1 |  |
| CH-0235 | XV.2 | its sentences, one section | 1 | L536.s1 |  |
| CH-0329 | XV.2 | its sentences, one section | 1 | L536.s1 |  |
| CH-0330 | XV.2 | its sentences, one section | 1 | L536.s1 |  |
| CH-0331 | XV.2 | its sentences, one section | 1 | L536.s1 |  |
| CH-0814 | XV.2 | its sentences, one section | 1 | L536.s1 |  |
| CH-0899 | XV.2 | its sentences, one section | 3 | L536.s1 |  |
| CH-1023 | XV.2 | its sentences, one section | 3 | L536.s1 |  |
| CH-1217 | XV.2 | its sentences, one section | 1 | L536.s1 |  |
| CH-0005 | XV.2 | its sentences, one section | 1 | L536.s2 |  |
| CH-0009 | XV.2 | its sentences, one section | 1 | L536.s2 |  |
| CH-0237 | XV.2 | its sentences, one section | 1 | L536.s2 |  |
| CH-0327 | XV.2 | its sentences, one section | 1 | L536.s2 |  |
| CH-0328 | XV.2 | its sentences, one section | 1 | L536.s3 |  |
| CH-0405 | XV.2 | its sentences, one section | 1 | L536.s3 |  |
| CH-0461 | XV.2 | its sentences, one section | 1 | L536.s3 |  |
| CH-0945 | XV.2 | its sentences, one section | 3 | L536.s3 |  |
| CH-0010 | XV.3 | its sentences, one section | 1 | L538.s1 |  |
| CH-0017 | XV.3 | its sentences, one section | 1 | L538.s1 |  |
| CH-0238 | XV.3 | its sentences, one section | 1 | L538.s1 |  |
| CH-0239 | XV.3 | its sentences, one section | 1 | L538.s1 |  |
| CH-0333 | XV.3 | its sentences, one section | 1 | L538.s1 |  |
| CH-0815 | XV.3 | its sentences, one section | 1 | L538.s1 |  |
| CH-0900 | XV.3 | its sentences, one section | 3 | L538.s1 |  |
| CH-1084 | XV.3 | its sentences, one section | 1 | L538.s1 |  |
| CH-0018 | XV.3 | its sentences, one section | 1 | L538.s2 |  |
| CH-0240 | XV.3 | its sentences, one section | 1 | L538.s2 |  |
| CH-0332 | XV.3 | its sentences, one section | 1 | L538.s2 |  |
| CH-0334 | XV.3 | its sentences, one section | 1 | L538.s2 |  |
| CH-0011 | XV.4 | its sentences, one section | 1 | L540.s1 |  |
| CH-0019 | XV.4 | its sentences, one section | 1 | L540.s1 |  |
| CH-0020 | XV.4 | its sentences, one section | 1 | L540.s1 |  |
| CH-0241 | XV.4 | its sentences, one section | 1 | L540.s1 |  |
| CH-0242 | XV.4 | its sentences, one section | 1 | L540.s1 |  |
| CH-0243 | XV.4 | its sentences, one section | 1 | L540.s2 |  |
| CH-0816 | XV.4 | its sentences, one section | 1 | L540.s2 |  |
| CH-0946 | XV.4 | its sentences, one section | 3 | L540.s2 |  |
| CH-0983 | XV.4 | its sentences, one section | 2 | L540.s2 |  |
| CH-1024 | XV.4 | its sentences, one section | 2 | L540.s2 |  |
| CH-0021 | XV.5 | its sentences, one section | 1 | L542.s1 |  |
| CH-0025 | XV.5 | its sentences, one section | 1 | L542.s1 |  |
| CH-0335 | XV.5 | its sentences, one section | 1 | L542.s1 |  |
| CH-0336 | XV.5 | its sentences, one section | 1 | L542.s1 |  |
| CH-0817 | XV.5 | its sentences, one section | 1 | L542.s1 |  |
| CH-0818 | XV.5 | its sentences, one section | 1 | L542.s1 |  |
| CH-0819 | XV.5 | its sentences, one section | 1 | L542.s1 |  |
| CH-0820 | XV.5 | its sentences, one section | 1 | L542.s1 |  |
| CH-0947 | XV.5 | its sentences, one section | 3 | L542.s1 |  |
| CH-0013 | XV.6 | its sentences, one section | 1 | L544.s1 |  |
| CH-0014 | XV.6 | its sentences, one section | 1 | L544.s1 |  |
| CH-0022 | XV.6 | its sentences, one section | 1 | L544.s1 |  |
| CH-0024 | XV.6 | its sentences, one section | 1 | L544.s1 |  |
| CH-0246 | XV.6 | its sentences, one section | 1 | L544.s1 |  |
| CH-0247 | XV.6 | its sentences, one section | 1 | L544.s1 |  |
| CH-0357 | XV.6 | its sentences, one section | 1 | L544.s1 |  |
| CH-0821 | XV.6 | its sentences, one section | 1 | L544.s1 |  |
| CH-0822 | XV.6 | its sentences, one section | 1 | L544.s1 |  |
| CH-0948 | XV.6 | its sentences, one section | 3 | L544.s1 |  |
| CH-1105 | XV.6 | most of its sentences (2 sections) | 1 | L544.s1 | XVI.5 (5. Question-finding is representable) |
| CH-0023 | XV.7 | its sentences, one section | 1 | L546.s1 |  |
| CH-0823 | XV.7 | its sentences, one section | 1 | L546.s1 |  |
| CH-0824 | XV.7 | its sentences, one section | 1 | L546.s1 |  |
| CH-1060 | XV.7 | most of its sentences (2 sections) | 1 | L546.s1 | XVI.1 (opening of Part XVI) |
| CH-1122 | XV.7 | most of its sentences (2 sections) | 2 | L546.s1 | XVI.1 (opening of Part XVI) |
| CH-0572 | XV.x | Part only (never applied) | 1 |  |  |
| CH-0825 | XVI.1 | its sentences, one section | 1 | L550.s1 |  |
| CH-0826 | XVI.1 | its sentences, one section | 1 | L552.s1 |  |
| CH-1124 | XVI.1 | its sentences, one section | 2 | L552.s1 |  |
| CH-0827 | XVI.1 | its sentences, one section | 1 | L554.s1 |  |
| CH-0828 | XVI.1 | its sentences, one section | 1 | L556.s1 |  |
| CH-0527 | XVI.1 | its sentences, one section | 1 | L558.s1 |  |
| CH-0829 | XVI.1 | its sentences, one section | 1 | L558.s1 |  |
| CH-1175 | XVI.1 | its sentences, one section | 1 | L558.s1 |  |
| CH-0410 | XVI.2 | its sentences, one section | 4 | L560.s1 |  |
| CH-0830 | XVI.2 | its sentences, one section | 1 | L560.s1 |  |
| CH-0418 | XVI.2 | its sentences, one section | 1 | L562.s1 |  |
| CH-0832 | XVI.2 | its sentences, one section | 1 | L562.s1 |  |
| CH-0831 | XVI.2 | its sentences, one section | 1 | L562.s3 |  |
| CH-1025 | XVI.2 | its sentences, one section | 2 | L562.s3 |  |
| CH-0834 | XVI.2 | its sentences, one section | 1 | L564.s1 |  |
| CH-0833 | XVI.2 | its sentences, one section | 1 | L564.s3 |  |
| CH-0835 | XVI.2 | its sentences, one section | 1 | L566.s1 |  |
| CH-0836 | XVI.2 | its sentences, one section | 1 | L566.s1 |  |
| CH-0837 | XVI.2 | its sentences, one section | 1 | L566.s2 |  |
| CH-0494 | XVI.2 | its sentences, one section | 1 | L568.s1 |  |
| CH-0838 | XVI.2 | its sentences, one section | 1 | L568.s1 |  |
| CH-0839 | XVI.2 | its sentences, one section | 1 | L568.s1 |  |
| CH-0840 | XVI.2 | its sentences, one section | 1 | L568.s1 |  |
| CH-0929 | XVI.2 | most of its sentences (2 sections) | 4 | L568.s1 | VI.7 (Problems) |
| CH-1026 | XVI.2 | its sentences, one section | 2 | L568.s1 |  |
| CH-0244 | XVI.3 | most of its sentences (4 sections) | 14 | L570.s1 | XV.3 ((Nec) Necessity); XV.4 ((Elim) Reinstatement of kinds); XV.5 ((Prov) Genesis) |
| CH-0143 | XVI.3 | most of its sentences (3 sections) | 12 | L572.s2 | 0.7 (Grievances, anticipated / 3. "If correspondences are selected, you have made fidelity a matter of survival."); XV.5 ((Prov) Genesis) |
| CH-0420 | XVI.3 | its sentences, one section | 1 | L572.s2 |  |
| CH-0568 | XVI.3 | its sentences, one section | 1 | L572.s2 |  |
| CH-0352 | XVI.3 | its sentences, one section | 2 | L572.s3 |  |
| CH-0505 | XVI.3 | its sentences, one section | 1 | L572.s3 |  |
| CH-0841 | XVI.3 | its sentences, one section | 1 | L572.s3 |  |
| CH-0842 | XVI.3 | its sentences, one section | 1 | L574.s1 |  |
| CH-0174 | XVI.3 | its sentences, one section | 1 | L576.s1 |  |
| CH-0844 | XVI.3 | its sentences, one section | 1 | L576.s2 |  |
| CH-0843 | XVI.3 | its sentences, one section | 1 | L576.s4 |  |
| CH-0901 | XVI.4 | its sentences, one section | 1 | L580.s1 |  |
| CH-1227 | XVI.4 | its sentences, one section | 1 | L580.s1 |  |
| CH-0846 | XVI.4 | its sentences, one section | 1 | L582.s1 |  |
| CH-0544 | XVI.4 | its sentences, one section | 1 | L582.s2 |  |
| CH-1027 | XVI.4 | most of its sentences (2 sections) | 3 | L582.s2 | XVI.9 (10. A two-layer episode, in exact form) |
| CH-0845 | XVI.4 | its sentences, one section | 1 | L582.s3 |  |
| CH-0338 | XVI.4 | its sentences, one section | 1 | L584.s2 |  |
| CH-0847 | XVI.4 | its sentences, one section | 1 | L584.s2 |  |
| CH-1028 | XVI.5 | its sentences, one section | 3 | L588.s1 |  |
| CH-0848 | XVI.5 | its sentences, one section | 1 | L588.s2 |  |
| CH-0849 | XVI.5 | its sentences, one section | 1 | L590.s1 |  |
| CH-0358 | XVI.5 | its sentences, one section | 1 | L592.s1 |  |
| CH-0850 | XVI.5 | its sentences, one section | 1 | L592.s1 |  |
| CH-0949 | XVI.5 | its sentences, one section | 3 | L592.s1 |  |
| CH-1136 | XVI.5 | most of its sentences (2 sections) | 2 | L592.s1 | XV.6 ((QF) Question-finding) |
| CH-1156 | XVI.5 | its sentences, one section | 1 | L592.s1 |  |
| CH-0339 | XVI.5 | its sentences, one section | 1 | L592.s3 |  |
| CH-0359 | XVI.5 | its sentences, one section | 1 | L592.s3 |  |
| CH-0406 | XVI.5 | its sentences, one section | 1 | L592.s3 |  |
| CH-0851 | XVI.5 | its sentences, one section | 1 | L592.s3 |  |
| CH-0105 | XVI.5 | section its source names (never applied) | 2 |  |  |
| CH-0106 | XVI.5 | section its source names (never applied) | 1 |  |  |
| CH-0107 | XVI.5 | section its source names (never applied) | 2 |  |  |
| CH-0108 | XVI.5 | section its source names (never applied) | 3 |  |  |
| CH-0109 | XVI.5 | section its source names (never applied) | 5 |  |  |
| CH-0852 | XVI.6 | its sentences, one section | 1 | L594.s1 |  |
| CH-0340 | XVI.6 | its sentences, one section | 1 | L596.s1 |  |
| CH-0355 | XVI.6 | its sentences, one section | 1 | L596.s1 |  |
| CH-0407 | XVI.6 | its sentences, one section | 1 | L596.s1 |  |
| CH-0853 | XVI.6 | its sentences, one section | 1 | L596.s1 |  |
| CH-0554 | XVI.6 | its sentences, one section | 1 | L598.s1 |  |
| CH-0855 | XVI.6 | its sentences, one section | 1 | L598.s1 |  |
| CH-1178 | XVI.6 | its sentences, one section | 1 | L598.s1 |  |
| CH-0349 | XVI.6 | its sentences, one section | 2 | L598.s2 |  |
| CH-0854 | XVI.6 | its sentences, one section | 1 | L598.s2 |  |
| CH-0950 | XVI.6 | its sentences, one section | 3 | L598.s2 |  |
| CH-0951 | XVI.6 | its sentences, one section | 3 | L600.s1 |  |
| CH-0856 | XVI.6 | its sentences, one section | 1 | L600.s2 |  |
| CH-1029 | XVI.6 | its sentences, one section | 2 | L600.s2 |  |
| CH-0952 | XVI.6 | its sentences, one section | 3 | L600.s3 |  |
| CH-0089 | XVI.6 | section lead 0.74 (never applied) | 1 |  |  |
| CH-0857 | XVI.7 | its sentences, one section | 1 | L604.s1 |  |
| CH-0860 | XVI.7 | its sentences, one section | 1 | L606.s1 |  |
| CH-0858 | XVI.7 | its sentences, one section | 1 | L606.s2 |  |
| CH-0995 | XVI.7 | its sentences, one section | 1 | L606.s2 |  |
| CH-0861 | XVI.7 | its sentences, one section | 1 | L606.s3 |  |
| CH-0859 | XVI.7 | its sentences, one section | 1 | L606.s4 |  |
| CH-1030 | XVI.7 | its sentences, one section | 2 | L608.s1 |  |
| CH-0862 | XVI.7 | its sentences, one section | 1 | L608.s2 |  |
| CH-1073 | XVI.7 | its sentences, one section | 1 | L608.s2 |  |
| CH-1150 | XVI.7 | its sentences, one section | 1 | L608.s2 |  |
| CH-0863 | XVI.8 | its sentences, one section | 1 | L610.s1 |  |
| CH-0864 | XVI.8 | its sentences, one section | 1 | L612.s1 |  |
| CH-1031 | XVI.8 | its sentences, one section | 2 | L612.s1 |  |
| CH-0865 | XVI.8 | its sentences, one section | 1 | L612.s2 |  |
| CH-0867 | XVI.8 | its sentences, one section | 1 | L616.s2 |  |
| CH-0866 | XVI.8 | its sentences, one section | 1 | L616.s4 |  |
| CH-0868 | XVI.9 | its sentences, one section | 1 | L620.s1 |  |
| CH-0953 | XVI.9 | its sentences, one section | 3 | L620.s1 |  |
| CH-0341 | XVI.9 | its sentences, one section | 1 | L620.s2 |  |
| CH-0869 | XVI.9 | its sentences, one section | 1 | L624.s3 |  |
| CH-0870 | XVI.9 | its sentences, one section | 1 | L624.s4 |  |
| CH-0342 | XVI.9 | its sentences, one section | 1 | L626.s3 |  |
| CH-0350 | XVI.9 | its sentences, one section | 3 | L626.s3 |  |
| CH-0408 | XVI.9 | its sentences, one section | 1 | L626.s3 |  |
| CH-0343 | XVI.9 | its sentences, one section | 1 | L626.s4 |  |
| CH-0871 | XVI.9 | its sentences, one section | 1 | L626.s6 |  |
| CH-1032 | XVI.9 | its sentences, one section | 2 | L626.s8 |  |
| CH-0344 | XVI.9 | its sentences, one section | 1 | L628.s1 |  |
| CH-0872 | XVI.9 | its sentences, one section | 1 | L628.s1 |  |
| CH-0873 | XVI.9 | its sentences, one section | 1 | L628.s2 |  |
| CH-0874 | XVI.9 | its sentences, one section | 1 | L628.s2 |  |
| CH-0412 | XVI.9 | its sentences, one section | 3 | L630.s3 |  |
| CH-0493 | XVI.9 | its sentences, one section | 1 | L630.s3 |  |
| CH-0877 | XVI.9 | its sentences, one section | 1 | L630.s3 |  |
| CH-0878 | XVI.9 | its sentences, one section | 1 | L630.s3 |  |
| CH-0875 | XVI.9 | its sentences, one section | 1 | L630.s4 |  |
| CH-1033 | XVI.9 | its sentences, one section | 2 | L630.s4 |  |
| CH-1151 | XVI.9 | its sentences, one section | 1 | L630.s4 |  |
| CH-0876 | XVI.9 | its sentences, one section | 1 | L630.s5 |  |
| CH-0954 | XVI.9 | its sentences, one section | 3 | L630.s5 |  |
| CH-0879 | XVI.9 | its sentences, one section | 1 | L632.s1 |  |
| CH-0462 | XVI.9 | its sentences, one section | 1 | L632.s2 |  |
| CH-0144 | XVI.x | Part only (never applied) | 2 |  |  |
| CH-0145 | XVI.x | Part only (never applied) | 1 |  |  |
| CH-0146 | XVI.x | Part only (never applied) | 2 |  |  |
| CH-1066 | ALL | term-wide, 6 Parts | 1 | L13.s1 | 0.2 (What this document claims); 0.4 (What is imported, what is an index, and what is defined); 0.10 (Grievances, anticipated / 6. "You have replaced explanation with evolution."); IV.1 (The object layer and the simulation layer); IV.2 (Three provenances); XI.5 (Appraisal); XIV.1 (Imports); XIV.2 (What everything else is defined from); XIV.3 (Declared inputs); XIV.3 (Indices, not imports); XV.4 ((Elim) Reinstatement of kinds); XV.5 ((Prov) Genesis); XVI.3 (3. Selected transports are underdetermined on unseen changes their population leaves open); XVI.6 (6. There are two imports); XVI.9 (10. A two-layer episode, in exact form) |
| CH-1126 | ALL | term-wide, 10 Parts | 3 | L13.s1 | 0.2 (What this document claims); 0.4 (What is imported, what is an index, and what is defined); 0.10 (Grievances, anticipated / 6. "You have replaced explanation with evolution."); 0.14 (Grievances, anticipated / 10. "Freezing the question for assessment while letting questions change across episodes is having it both ways."); 0.16 (Where to attack this); II.1 (Kinds are edit-signatures); IV.1 (The object layer and the simulation layer); IV.2 (Three provenances); V.6 (Why there is no counterpart-kind condition); VI.3 (Redundant routes); VII.2 (Identification); XI.5 (Appraisal); XIV.1 (Imports); XIV.2 (What everything else is defined from); XIV.3 (Declared inputs); XIV.3 (Indices, not imports); XV.4 ((Elim) Reinstatement of kinds); XV.5 ((Prov) Genesis); XVI.2 (2. Same counterparts, one account); XVI.3 (3. Selected transports are underdetermined on unseen changes their population leaves open); XVI.4 (4. Surprise requires an incomplete history); XVI.6 (6. There are two imports); XVI.9 (10. A two-layer episode, in exact form) |
| CH-1131 | ALL | term-wide, 10 Parts | 11 | L17.s1 | 0.2 (What this document claims); 0.3 (What this document does not claim); 0.4 (What is imported, what is an index, and what is defined); I.2 (Fallibility without error-as-work); III.2 (The respect is the query); III.4 (Scope, and a question that can be in error); V.5 (What (E) excludes, and what it does not); XI.3 (Created explanation); XII.1 (Retained realization); XIII.2 (Universality); XIV.4 (Dependence order); XV.3 ((Nec) Necessity); XV.6 ((QF) Question-finding); XVI.3 (3. Selected transports are underdetermined on unseen changes their population leaves open); XVI.6 (6. There are two imports) |
| CH-1044 | ALL | term-wide, 3 Parts | 1 | L17.s3 | 0.2 (What this document claims); VI.6 (Rivals); VIII.5 (A failed answer stays failed) |
| CH-1127 | ALL | term-wide, 6 Parts | 6 | L21.s1 | 0.3 (What this document does not claim); 0.4 (What is imported, what is an index, and what is defined); II.1 (Roles are defined, not supplied); IV.3 (Representation is defined, not supplied); VII.1 (Production and direction); XI.5 (Appraisal); XIV.1 (Imports); XIV.2 (What everything else is defined from); XIV.4 (Dependence order) |
| CH-1098 | ALL | term-wide, 4 Parts | 1 | L25.s1 | 0.3 (What this document does not claim); VI.7 (Problems); XI.2 (The aims of a repair); XIV.3 (Declared inputs) |
| CH-1135 | ALL | term-wide, 6 Parts | 7 | L25.s1 | 0.3 (What this document does not claim); 0.4 (What is imported, what is an index, and what is defined); 0.12 (Grievances, anticipated / 8. "Where is aesthetics?"); V.5 (What (E) excludes, and what it does not); XI.1 (opening of Part XI); XI.2 (The aims of a repair); XI.5 (Appraisal); XIV.1 (Imports); XIV.3 (Declared inputs); XV.1 (opening of Part XV); XVI.5 (5. Question-finding is representable) |
| CH-1095 | ALL | term-wide, 4 Parts | 1 | L25.s2 | 0.3 (What this document does not claim); 0.4 (What is imported, what is an index, and what is defined); 0.12 (Grievances, anticipated / 8. "Where is aesthetics?"); XI.5 (Appraisal); XIV.1 (Imports); XIV.3 (Declared inputs); XV.1 (opening of Part XV) |
| CH-1047 | ALL | term-wide, 10 Parts | 1 | L25.s3 | 0.3 (What this document does not claim); VI.6 (Rivals); VI.7 (Problems); VII.2 (Obstruction); VIII.5 (A failed answer stays failed); IX.2 (What a test rules out); X.1 (Deployment); XI.2 (The aims of a repair); XI.5 (Appraisal); XIII.2 (Universality); XIV.4 (Dependence order); XVI.3 (3. Selected transports are underdetermined on unseen changes their population leaves open) |
| CH-1048 | ALL | term-wide, 3 Parts | 1 | L25.s3 | 0.3 (What this document does not claim); XI.2 (The aims of a repair); XI.5 (Appraisal); XVI.3 (3. Selected transports are underdetermined on unseen changes their population leaves open) |
| CH-1106 | ALL | term-wide, 5 Parts | 1 | L25.s3 | 0.3 (What this document does not claim); VI.3 (Redundant routes); X.5 (Ownership); XI.2 (The aims of a repair); XIV.3 (Declared inputs) |
| CH-1125 | ALL | term-wide, 5 Parts | 5 | L27.s1 | 0.3 (What this document does not claim); V.5 (What (E) excludes, and what it does not); XIII.1 (Barriers); XIV.4 (Dependence order); XV.5 ((Prov) Genesis); XV.6 ((QF) Question-finding) |
| CH-1129 | ALL | term-wide, 13 Parts | 7 | L31.s1 | 0.4 (What is imported, what is an index, and what is defined); I.4 (Substrate independence with physical conditions); III.2 (The respect is the query); IV.2 (Three provenances); V.1 (opening of Part V); V.3 (Non-circular dependence); VI.2 (Finite monotone claim); VI.6 (Rivals); VI.7 (Problems); VII.2 (Identification); VIII.1 (Functional transport); VIII.5 (A failed answer stays failed); X.1 (Deployment); X.2 (Construction); X.6 (Episodes); XI.2 (The aims of a repair); XI.4 (Result, and the index of (EX)); XIII.1 (Barriers); XIV.3 (Indices, not imports); XVI.4 (4. Surprise requires an incomplete history); XVI.5 (5. Question-finding is representable); XVI.7 (7. The frozen assessment and the moving question are consistent); XVI.8 (9. Output descriptions do not determine accounts); XVI.9 (10. A two-layer episode, in exact form) |
| CH-1132 | ALL | term-wide, 4 Parts | 2 | L31.s4 | 0.4 (What is imported, what is an index, and what is defined); XI.1 (opening of Part XI); XI.3 (Created explanation); XIV.2 (What everything else is defined from); XIV.4 (Dependence order); XIV.4 (Membership); XVI.6 (6. There are two imports) |
| CH-1083 | ALL | term-wide, 4 Parts | 1 | L39.s2 | 0.6 (Grievances, anticipated / 2. "So this is operationalism: a thing is what you can do to it."); V.2 (Component fidelity); XIV.4 (Membership); XVI.9 (10. A two-layer episode, in exact form) |
| CH-1195 | ALL | term-wide, 8 Parts | 1 | L45.s4 | 0.9 (Grievances, anticipated / 5. "This is teleosemantics, structural realism or functionalism with new words."); I.4 (Substrate independence with physical conditions); III.1 (Contracts); VI.7 (Problems); X.6 (Episodes); XI.1 (Repair); XI.2 (The aims of a repair); XI.3 (Created explanation); XI.5 (Appraisal); XIV.3 (Declared inputs); XIV.4 (Dependence order); XVI.9 (10. A two-layer episode, in exact form) |
| CH-1067 | ALL | term-wide, 4 Parts | 1 | L47.s1 | 0.10 (Grievances, anticipated / 6. "You have replaced explanation with evolution."); IV.1 (The object layer and the simulation layer); IV.2 (Three provenances); XV.5 ((Prov) Genesis); XVI.3 (3. Selected transports are underdetermined on unseen changes their population leaves open); XVI.9 (10. A two-layer episode, in exact form) |
| CH-1181 | ALL | term-wide, 4 Parts | 1 | L47.s1 | 0.10 (Grievances, anticipated / 6. "You have replaced explanation with evolution."); IV.1 (The object layer and the simulation layer); IV.2 (Three provenances); XV.5 ((Prov) Genesis); XVI.3 (3. Selected transports are underdetermined on unseen changes their population leaves open); XVI.9 (10. A two-layer episode, in exact form) |
| CH-1065 | ALL | term-wide, 8 Parts | 1 | L47.s2 | 0.10 (Grievances, anticipated / 6. "You have replaced explanation with evolution."); III.3 (Contracts have provenance); IV.2 (Three provenances); IV.3 (Representation is defined, not supplied); IV.4 (Prediction, surprise, violation); VI.4 (Infinitary routes); VII.4 (Odd-order skew-symmetric matrices); X.2 (Construction); X.3 (Representation in use; construction is not selection); XV.5 ((Prov) Genesis); XVI.4 (4. Surprise requires an incomplete history); XVI.7 (7. The frozen assessment and the moving question are consistent); XVI.9 (10. A two-layer episode, in exact form) |
| CH-1041 | ALL | term-wide, 6 Parts | 1 | L47.s3 | 0.10 (Grievances, anticipated / 6. "You have replaced explanation with evolution."); 0.16 (Where to attack this); VI.7 (Problems); VII.2 (Obstruction); IX.2 (What a test rules out); XIII.1 (Barriers); XV.1 (opening of Part XV); XV.4 ((Elim) Reinstatement of kinds); XV.5 ((Prov) Genesis) |
| CH-1061 | ALL | term-wide, 10 Parts | 1 | L49.s3 | 0.11 (Grievances, anticipated / 7. "Mathematics has no interventions."); II.1 (Organizations); V.5 (What (E) excludes, and what it does not); VI.2 (Finite monotone claim); VII.4 (Odd-order skew-symmetric matrices); VIII.1 (Functional transport); X.6 (Episodes); XIII.1 (Barriers); XIV.4 (Dependence order); XVI.1 (1. Kind preservation needs no condition of its own); XVI.2 (2. Same counterparts, one account); XVI.3 (3. Selected transports are underdetermined on unseen changes their population leaves open); XVI.4 (4. Surprise requires an incomplete history); XVI.5 (5. Question-finding is representable); XVI.6 (6. There are two imports); XVI.7 (7. The frozen assessment and the moving question are consistent); XVI.8 (8. Equivariance under structure-preserving recoding); XVI.8 (9. Output descriptions do not determine accounts) |
| CH-1077 | ALL | term-wide, 6 Parts | 1 | L67.s2 | I.1 (Faithfulness without assessors); I.2 (Fallibility without error-as-work); III.4 (Scope, and a question that can be in error); IV.3 (Representation is defined, not supplied); V.2 (Component fidelity); V.6 (Why there is no counterpart-kind condition); VI.7 (Problems); X.1 (Deployment) |
| CH-1187 | ALL | term-wide, 3 Parts | 1 | L67.s2 | I.1 (Faithfulness without assessors); III.4 (Scope, and a question that can be in error); V.2 (Component fidelity) |
| CH-1185 | ALL | term-wide, 3 Parts | 1 | L69.s3 | I.2 (Fallibility without error-as-work); IV.3 (Representation is defined, not supplied); X.1 (Deployment) |
| CH-1075 | ALL | term-wide, 3 Parts | 1 | L75.s4 | I.4 (Substrate independence with physical conditions); VIII.5 (A failed answer stays failed); XVI.8 (9. Output descriptions do not determine accounts) |
| CH-1070 | ALL | term-wide, 5 Parts | 1 | L119.s3 | II.1 (Kinds are edit-signatures); V.2 (Component fidelity); V.6 (Why there is no counterpart-kind condition); VI.6 (Rivals); VI.7 (Problems); VII.3 (Explanations that remove structure); XVI.1 (1. Kind preservation needs no condition of its own); XVI.2 (2. Same counterparts, one account) |
| CH-1128 | ALL | term-wide, 5 Parts | 2 | L119.s3 | II.1 (Kinds are edit-signatures); V.2 (Component fidelity); V.6 (Why there is no counterpart-kind condition); VI.6 (Rivals); VII.3 (Explanations that remove structure); XVI.1 (1. Kind preservation needs no condition of its own); XVI.2 (2. Same counterparts, one account) |
| CH-1076 | ALL | term-wide, 3 Parts | 1 | L151.s4 | III.2 (The respect is the query); V.3 (Non-circular dependence); XVI.7 (7. The frozen assessment and the moving question are consistent) |
| CH-1182 | ALL | term-wide, 5 Parts | 1 | L155.s4 | III.3 (Contracts have provenance); IV.2 (Three provenances); IV.4 (Prediction, surprise, violation); X.2 (Construction); X.3 (Representation in use; construction is not selection); XV.5 ((Prov) Genesis); XVI.7 (7. The frozen assessment and the moving question are consistent) |
| CH-1058 | ALL | term-wide, 3 Parts | 1 | L159.s7 | III.4 (Scope, and a question that can be in error); XIV.3 (Declared inputs); XV.1 (opening of Part XV) |
| CH-1200 | ALL | term-wide, 3 Parts | 2 | L215.s1 | IV.4 (Prediction, surprise, violation); XI.3 (Created explanation); XVI.3 (3. Selected transports are underdetermined on unseen changes their population leaves open); XVI.4 (4. Surprise requires an incomplete history); XVI.9 (10. A two-layer episode, in exact form) |
| CH-1202 | ALL | term-wide, 3 Parts | 2 | L223.s5 | IV.4 (Prediction, surprise, violation); VI.7 (Problems); X.6 (Episodes) |
| CH-1110 | ALL | term-wide, 4 Parts | 2 | L285.s1 | VI.1 (opening of Part VI); VI.2 (Finite monotone claim); VI.3 (Redundant routes); VI.4 (Infinitary routes); VI.5 (Commitments that do no work); VII.2 (Identification); IX.3 (Arguments); X.1 (Deployment) |
| CH-1062 | ALL | term-wide, 3 Parts | 1 | L305.s1 | VI.2 (Finite monotone claim); XV.5 ((Prov) Genesis); XV.7 (A mathematical error); XVI.1 (1. Kind preservation needs no condition of its own) |
| CH-1134 | ALL | term-wide, 4 Parts | 3 | L307.s5 | VI.3 (Redundant routes); VI.3 (Interference); VII.3 (Explanations that remove structure); XII.1 (Tasks); XII.1 (Retained realization); XVI.9 (10. A two-layer episode, in exact form) |
| CH-1034 | ALL | term-wide, 4 Parts | 1 | L315.s6 | VI.6 (Rivals); VI.7 (Problems); VIII.5 (A failed answer stays failed); IX.2 (What a test rules out); XIV.4 (Dependence order) |
| CH-1038 | ALL | term-wide, 4 Parts | 1 | L315.s6 | VI.6 (Rivals); VIII.5 (A failed answer stays failed); IX.3 (Arguments); XIV.4 (Dependence order) |
| CH-1111 | ALL | term-wide, 4 Parts | 2 | L315.s6 | VI.6 (Rivals); VI.7 (Problems); VIII.5 (A failed answer stays failed); IX.2 (What a test rules out); XIV.4 (Dependence order) |
| CH-1117 | ALL | term-wide, 4 Parts | 2 | L315.s6 | VI.6 (Rivals); VIII.5 (A failed answer stays failed); IX.3 (Arguments); XIV.4 (Dependence order) |
| CH-1040 | ALL | term-wide, no line named (not locatable) | 1 |  |  |
| CH-1091 | ALL | term-wide, no line named (not locatable) | 1 |  |  |
| CH-1100 | ALL | term-wide, no line named (not locatable) | 1 |  |  |
| CH-1123 | ALL | term-wide, no line named (not locatable) | 2 |  |  |
| CH-1138 | ALL | term-wide, no line named (not locatable) | 1 |  |  |
| CH-1165 | ALL | term-wide, no line named (not locatable) | 1 |  |  |
| CH-1166 | ALL | term-wide, no line named (not locatable) | 1 |  |  |
