# S98 — the anchoring summary: every collected record placed on the latest text

*Log S98, 26 September 2026, under the owner's instruction of that day (decision S30). This is the anchor step of the ledger: it takes the five collectors' records in `collect/`, places each on the sentences of the latest text that it touches, names the theory's terms in its wording, and joins the records that are one change seen in several sources. Nothing in `collect/` was changed; every collector field is carried into `anchored.jsonl` byte for byte. The files were written by the programs in `anchor - scripts/`, and this page by `step4_summary.py`.*

## In brief

- **Records:** 1850, from five collectors. **Changes:** 1275, after joining duplicates.
- **Placed on sentences of the latest text:** 1533 (83%). The rest have an empty `latest_sentences`: removed 9, never applied 262, not locatable 46.
- **Wording still standing:** in 575 records the new wording (or the whole new sentence) is found word for word in the latest text.
- **Records with no place but a Part:** every record with an empty anchor keeps `latest_part` and `latest_parts` from the Part its source names (Part numbers are the same in every version). 127 of them also carry `latest_nearest`: the latest-text sentence sharing most content words with the record, in that Part. It is offered to the grouping step as a lead and is not an anchor.
- **Latest text:** `Revision 2 - scrubbed copy, repaired (S96), after cross-examination, theory text.md`, md5 ebca15a047f686b15d5f5766b69825c9, 632 lines.

## The three files

- **`sentence index of the latest text.jsonl`** — 756 units: 666 sentences, 55 headings, 27 displayed formulas (each one unit, however many lines), 8 list items (each one unit). Fields: `id` (`L<line>.s<n>`), `line`, `line_end`, `n`, `kind`, `part`, `heading` (the `##` heading above it), `label` (the bold run-in label of its paragraph), `text`, and `start`/`end` (character offsets in its line). Sentences are cut as collector A cut them (mathematics and code never cut; a bare bold label joins the sentence after it), with two additions: a numbered bold label such as `**1.` does not end a sentence, and a closing tag such as `(K3)` stays with the sentence before it.
- **`line maps.json`** — maps between consecutive versions: file 10 → file 11 → draft 1 → draft 2 → draft 3 → draft 4 → draft 5 → scrubbed copy → repaired copy → latest text, and each version composed to the latest text (`to_latest`). It also holds the sentence-level map file 10 → file 11 and the check of the change list's FILE-11 LINE fields.
- **`anchored.jsonl`** — the 1850 records, in collector order, each with the collector's fields unchanged and these added: `latest_sentences`, `latest_status`, `latest_reason` (only when the anchor is empty), `latest_part`, `latest_heading`, `latest_parts`, `latest_lines`, `latest_nearest` (only for some records with no anchor), `anchor_method`, `anchor_ratio`, `new_in_latest` (yes / no / n/a), `target_version`, `terms`, `change_id`, `change_members`.

## How the line maps were made

| pair | method | equal | changed | moved | removed | lines new in the later text |
| --- | --- | --- | --- | --- | --- | --- |
| f10 → f11 | difflib + sentence map | 532 | 58 | 27 | 13 | 19 |
| f11 → d1 | difflib | 578 | 43 | 0 | 2 | 4 |
| d1 → d2 | difflib | 615 | 9 | 0 | 1 | 3 |
| d2 → d3 | difflib | 619 | 8 | 0 | 0 | 0 |
| d3 → d4 | difflib | 625 | 2 | 0 | 0 | 6 |
| d4 → d5 | difflib | 626 | 7 | 0 | 0 | 0 |
| d5 → scrubbed | line for line | 473 | 160 | 0 | 0 | 0 |
| scrubbed → repaired | line for line | 573 | 60 | 0 | 0 | 0 |
| repaired → latest | line for line | 561 | 72 | 0 | 0 | 0 |

Draft 5, the scrubbed copy, the repaired copy and the latest text keep the same 632 lines, so those three maps send each line to itself. The other maps use difflib on lines; inside a changed block, lines are paired by similarity (ratio 0.3 or more), and lines left over are paired across the text as moved (ratio 0.6 or more). Between file 10 and file 11, 17 lines that difflib could not place were placed through the sentence-level map (the file-11 line of their most similar sentence). 

The change list has 62 entries. For each, the program found the first line of its NEW text in each draft and compared that line with where the difflib maps send its FILE-11 LINE: 49 agree, 5 differ, and 8 have no FILE-11 LINE or no NEW line to find (record-only entries and meta blocks). The 5 that differ are entries whose NEW stands before or after the anchor lines their FILE-11 LINE names (W59.1 and W60.1 insert next to their anchor; W7.2 and W10a.1 add lines before the changed one; W30.1's NEW stands at draft 5 line 119, away from its OLD at file-11 line 161). They are listed in the file.

## How each record was placed

The program tries these in order and stops at the first that gives a place. The `anchor_method` field says which one was used.

1. **Notes and other texts.** A change to a note (file 11's revision note, file 13's note and record, the note of sources and departures) is not in any theory text after file 11. If the note entry declares a change at a named place ("file-11 line 337", "draft 5 L317"), the record is placed on that place; otherwise it is left empty as *not locatable*. The one change to file 12 is *not locatable* (a separate text). Changes to the whole text are *not locatable*.
2. **The place of the change.** A line in the latest text, found from: the new wording's line in the text that first carried it (for applied records); the file-11 line in collector B's source reference; the line named in `applied_in`; the record's `target_line` in its target text; or its old wording's line in the target text. Each is carried to the latest text by the line maps. The stage-1 text of S96 is not on disk; it keeps the repaired copy's lines, so its line numbers are read as the repaired copy's.
3. **Vocabulary entries** (scope `term`): the lines the entry names ("l. 317"), then a phrase the entry quotes as its new wording found in the latest text, then the places where its old words stood in the target text, carried to the latest text.
4. **New wording, word for word** (whitespace and quotation marks normalised): the whole new sentence, then the new span. A span under 25 characters is only looked for within two lines of the place. Where the place is known, a span, and any wording of a record that was not applied, counts only within five lines of it, so that a phrase a proposal borrowed from elsewhere in the text does not move it. Where the wording stands in several places, the one nearest the place is taken.
5. **Old wording, word for word:** the place still reads as it did (a recommendation not taken, or an old sentence kept).
6. **The mapped line:** the sentence on that line most similar to the record (difflib ratio for whole sentences; for a span, the ratio against the window of the sentence that matches it most closely). Applied records are compared by their new wording first, the others by their old wording first. If nothing on the line comes to 0.5, the two lines each side are tried, then the whole Part (a sentence at 0.6 or more that is at least 0.15 closer is taken). Below 0.25 the whole paragraph on the line is taken. A record with no wording to compare takes the paragraph.
7. **The whole Part:** with no place at all, the most similar sentence in the Part the source names, at a ratio of 0.6 or more.
8. **A record of the same change:** a record still without a place takes the place of the most similar record of its change group.

What is left is empty, with the reason in `latest_reason`: *removed* when the place of the change was last present in an earlier text and is gone after it; *never applied* when a proposal that was not taken has no place the program can find; *not locatable* otherwise.

### Placed records by method

| method | records |
| --- | --- |
| line map (…), most similar sentence on that line | 511 |
| new sentence verbatim in the latest text (…) | 484 |
| new wording verbatim in the latest text (…) | 91 |
| old sentence verbatim in the latest text (…) | 82 |
| term: the N places where its old words stood in file 13 draft 5, carried to the latest text | 80 |
| term: the lines the entry names, sentences holding its new words | 65 |
| term: the lines the entry names (…) | 32 |
| term: a phrase the entry quotes as new wording, found in the latest text | 30 |
| line map (…), the paragraph on that line (…) | 27 |
| old wording verbatim in the latest text (…) | 25 |
| line map (…); no sentence on that line is close, so the whole paragraph | 21 |
| a declaration in the note about the place at file 11 line N; the most similar sentence now there | 21 |
| line map (…), most similar sentence within two lines of it | 16 |
| same change as A-176 | 6 |
| term: the lines the entry names, sentences holding its old words | 5 |
| term: the N places where its old words stood in scrubbed copy, carried to the latest text | 4 |
| most similar sentence in Part XI (…) | 3 |
| a declaration in the note about the place at file 13 draft 5 line N; the most similar sentence now there | 3 |
| same change as A-316 | 2 |
| same change as A-318 | 2 |
| same change as A-293 | 2 |
| most similar sentence in Part III (…) | 2 |
| term: the N places where its old words stood in file 13 draft 2 (…), carried to the latest text | 2 |
| same change as A-303 | 1 |
| most similar sentence in Part X (…) | 1 |
| most similar sentence in Part XVI (…) | 1 |
| same change as A-286 | 1 |
| same change as A-320 | 1 |
| same change as A-302 | 1 |
| same change as C-11 | 1 |
| most similar sentence in Part VIII (…) | 1 |
| most similar sentence in Part XIV (…) | 1 |
| a declaration in the note about the place at file 11 line N; the whole paragraph now there | 1 |
| same change as D-624 | 1 |
| same change as D-627 | 1 |
| same change as D-630 | 1 |
| same change as D-662 | 1 |
| same change as D-580 | 1 |
| same change as D-720 | 1 |
| most similar sentence in Part VI (…) | 1 |

Similarity of the sentences placed by a line map or by similarity (583 records): 0.0–0.1: 8, 0.1–0.2: 6, 0.2–0.3: 21, 0.3–0.4: 56, 0.4–0.5: 60, 0.5–0.6: 53, 0.6–0.7: 83, 0.7–0.8: 87, 0.8–0.9: 86, 0.9–1.0: 123. Records below 0.4 are the ones to read first when checking.

## Counts

### By collector

| collector | records | anchored | removed | never applied | not locatable | new wording in the latest text | changes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A — the earliest rounds, before file 11 | 321 | 56 | 1 | 253 | 11 | 1 | 174 |
| B — file 10 to file 11, and the checks on file 11 | 310 | 289 | 8 | 3 | 10 | 75 | 268 |
| C — the revision 2 change list and its rulings | 209 | 194 | 0 | 3 | 12 | 27 | 178 |
| D — the scrub, the repairs and the last cross-examination | 952 | 943 | 0 | 1 | 8 | 472 | 646 |
| E — recommendations never applied, and the decision record | 58 | 51 | 0 | 2 | 5 | 0 | 48 |
| **all** | 1850 | 1533 | 9 | 262 | 46 | 575 | 1275 |

### By the record's own status

| status | records | anchored | removed | never applied | not locatable |
| --- | --- | --- | --- | --- | --- |
| applied | 1222 | 1182 | 8 | 0 | 32 |
| not applied | 273 | 70 | 0 | 197 | 6 |
| superseded | 207 | 146 | 0 | 57 | 4 |
| declined | 121 | 108 | 1 | 8 | 4 |
| open for the owner | 26 | 26 | 0 | 0 | 0 |
| unknown | 1 | 1 | 0 | 0 | 0 |

### By kind

| kind | records | anchored | removed | never applied | not locatable |
| --- | --- | --- | --- | --- | --- |
| recommendation | 987 | 686 | 0 | 262 | 39 |
| edit | 863 | 847 | 9 | 0 | 7 |

### By Part of the latest text

A record placed on sentences in two Parts is counted in each (third column). The fourth column counts each placed record once, by its first sentence. The fifth counts records with no anchor, by the Part their source names.

| Part of the latest text | sentences in it | placed records touching it | placed records, first sentence here | records with no anchor, Part named | changes touching it |
| --- | --- | --- | --- | --- | --- |
| Front matter (before Part 0) | 9 | 6 | 6 | 0 | 6 |
| Part 0 — Read this first | 97 | 235 | 235 | 31 | 213 |
| Part I — Commitments | 20 | 45 | 42 | 1 | 40 |
| Part II — Organizations and their changes | 46 | 43 | 41 | 9 | 41 |
| Part III — Questions | 39 | 65 | 61 | 41 | 62 |
| Part IV — Layers, transports, and provenance | 59 | 95 | 85 | 34 | 86 |
| Part V — Account | 47 | 118 | 108 | 75 | 140 |
| Part VI — Work, routes, and interference | 67 | 203 | 187 | 23 | 167 |
| Part VII — Exact constructions | 43 | 60 | 50 | 2 | 47 |
| Part VIII — Transport results | 23 | 55 | 42 | 4 | 43 |
| Part IX — Criticism, use, and usable arguments | 39 | 94 | 85 | 4 | 64 |
| Part X — Understanding, construction, and origin | 42 | 84 | 72 | 40 | 86 |
| Part XI — Repair, created explanation, and appraisal | 24 | 96 | 82 | 31 | 84 |
| Part XII — The physical module | 28 | 45 | 42 | 15 | 45 |
| Part XIII — Recursion and universality | 13 | 24 | 19 | 20 | 27 |
| Part XIV — The class collected | 43 | 125 | 97 | 24 | 107 |
| Part XV — What would rule this class out | 14 | 129 | 111 | 2 | 100 |
| Part XVI — Arguments | 103 | 205 | 168 | 35 | 168 |
| (no Part named) | 0 | 0 | 0 | 18 | 17 |

### By heading inside each Part (placed records, by first sentence)

| Part | heading or run-in label | records |
| --- | --- | --- |
| Part 0 — Read this first | What this document claims | 40 |
| Part 0 — Read this first | What this document does not claim | 36 |
| Part 0 — Read this first | What is imported, what is an index, and what is defined | 33 |
| Part 0 — Read this first | Grievances, anticipated / 4. "Then everything is relative to a contract of admitted changes, and nothing is independent of the modeller." | 19 |
| Part 0 — Read this first | Where to attack this | 16 |
| Part 0 — Read this first | Grievances, anticipated / 6. "You have replaced explanation with evolution." | 15 |
| Part 0 — Read this first | Grievances, anticipated / 7. "Mathematics has no interventions." | 14 |
| Part 0 — Read this first | Grievances, anticipated / 3. "If correspondences are selected, you have made fidelity a matter of survival." | 12 |
| Part 0 — Read this first | Grievances, anticipated / 8. "Where is aesthetics?" | 10 |
| Part 0 — Read this first | Two words, as used here | 9 |
| Part I — Commitments | Substrate independence with physical conditions | 18 |
| Part I — Commitments | Faithfulness without assessors | 10 |
| Part I — Commitments | Fallibility without error-as-work | 9 |
| Part II — Organizations and their changes | Kinds are edit-signatures | 33 |
| Part III — Questions | Scope, and a question that can be in error | 37 |
| Part III — Questions | The respect is the query | 14 |
| Part IV — Layers, transports, and provenance | Prediction, surprise, violation | 41 |
| Part IV — Layers, transports, and provenance | Representation is defined, not supplied | 19 |
| Part IV — Layers, transports, and provenance | Three provenances | 8 |
| Part V — Account | What (E) excludes, and what it does not | 46 |
| Part V — Account | (opening of the Part) | 27 |
| Part V — Account | Non-circular dependence | 17 |
| Part VI — Work, routes, and interference | Problems | 55 |
| Part VI — Work, routes, and interference | Rivals | 54 |
| Part VI — Work, routes, and interference | (opening of the Part) | 28 |
| Part VI — Work, routes, and interference | Commitments that do no work | 19 |
| Part VI — Work, routes, and interference | Redundant routes | 13 |
| Part VI — Work, routes, and interference | Finite monotone claim | 11 |
| Part VII — Exact constructions | Explanations that remove structure | 14 |
| Part VII — Exact constructions | Identification | 11 |
| Part VII — Exact constructions | Odd-order skew-symmetric matrices | 9 |
| Part VIII — Transport results | A failed answer stays failed | 15 |
| Part VIII — Transport results | Approximate transport | 11 |
| Part IX — Criticism, use, and usable arguments | Arguments | 34 |
| Part IX — Criticism, use, and usable arguments | (opening of the Part) | 20 |
| Part IX — Criticism, use, and usable arguments | Bearing | 10 |
| Part X — Understanding, construction, and origin | Construction | 20 |
| Part X — Understanding, construction, and origin | Episodes | 15 |
| Part X — Understanding, construction, and origin | Ownership | 14 |
| Part X — Understanding, construction, and origin | Deployment | 9 |
| Part XI — Repair, created explanation, and appraisal | (opening of the Part) | 38 |
| Part XI — Repair, created explanation, and appraisal | Appraisal | 27 |
| Part XI — Repair, created explanation, and appraisal | Created explanation | 13 |
| Part XII — The physical module | Tolerances | 11 |
| Part XII — The physical module | System boundary and continuity | 8 |
| Part XIII — Recursion and universality | Barriers | 9 |
| Part XIII — Recursion and universality | Universality | 9 |
| Part XIV — The class collected | Dependence order | 47 |
| Part XIV — The class collected | Declared inputs | 23 |
| Part XIV — The class collected | Imports | 11 |
| Part XIV — The class collected | (opening of the Part) | 8 |
| Part XV — What would rule this class out | (Suff) Sufficiency | 27 |
| Part XV — What would rule this class out | (Nec) Necessity | 17 |
| Part XV — What would rule this class out | (Elim) Reinstatement of kinds | 17 |
| Part XV — What would rule this class out | (Prov) Genesis | 17 |
| Part XV — What would rule this class out | (QF) Question-finding | 16 |
| Part XV — What would rule this class out | (opening of the Part) | 11 |
| Part XVI — Arguments | 10. A two-layer episode, in exact form | 38 |
| Part XVI — Arguments | 3. Selected transports are underdetermined on unseen changes their population leaves open / Claim | 15 |
| Part XVI — Arguments | 5. Question-finding is representable / Consequence | 10 |
| Part XVI — Arguments | 6. There are two imports | 10 |
| Part XVI — Arguments | 2. Same counterparts, one account | 10 |
| Part XVI — Arguments | 2. Same counterparts, one account / Consequence | 9 |
| Part XVI — Arguments | 6. There are two imports / Consequence | 9 |
| Part XVI — Arguments | 3. Selected transports are underdetermined on unseen changes their population leaves open / Consequence | 8 |

Headings with fewer than 8 placed records are left out of this table; `anchored.jsonl` has them all.

## The records with no anchor, and why

| empty as | why | records | which |
| --- | --- | --- | --- |
| removed | its place was last present in file 11 and is gone from the text after it; no sentence of the latest text is similar (ratio under the threshold) | 5 | B-1, B-2, B-3, B-4, B-5 |
| removed | its place was last present in file 10 and is gone from the text after it; no sentence of the latest text is similar (ratio under the threshold) | 4 | A-12, B-39, B-50, B-71 |
| never applied | no line to map and no sentence of the latest text is similar enough (ratio under the threshold) | 254 | A: 253; E: 1 (listed in the file by `latest_reason`) |
| never applied | no wording to search for | 4 | B-299, B-302, B-305, E-58 |
| never applied | a vocabulary entry whose words could not be placed on sentences of the latest text | 4 | C-134, C-199, C-200, D-650 |
| not locatable | the change is to a note (the revision note, the note of sources and departures, or the revision record); the theory texts after file 11 carry no such note | 22 | B-183, B-184, B-185, B-212, B-213, B-262, C-1, C-2, C-68, C-69, C-107, C-145, C-172, C-173, C-174, C-175, C-176, E-33, E-34, E-35, E-37, E-56 |
| not locatable | no line to map and no sentence of the latest text is similar enough (ratio under the threshold) | 11 | A-304, A-305, A-306, A-307, A-308, A-310, A-311, A-312, A-313, A-314, A-315 |
| not locatable | a vocabulary entry whose words could not be placed on sentences of the latest text | 8 | D-498, D-549, D-558, D-582, D-597, D-599, D-631, D-632 |
| not locatable | a change to the whole text, with no one place | 4 | B-291, B-292, B-293, B-300 |
| not locatable | file 12 is a separate text (the causality text); the latest text does not hold it | 1 | C-178 |

Most records never applied are collector A's: the R2 amendments and Stage B phrases were written against file 20, which is not held, and give no old wording or line; the file 10 Part they name is kept in `latest_part`. Collector A's S72 Stage 2 lines (W01 to W12), carried into file 11 in other wording, have no line either and are *not locatable*; most of them have a `latest_nearest`. By collector, never applied: A 253, B 3, C 3, D 1, E 2.

## Duplicates joined

Records are one change when a collector linked them (`same_as`, by record id, or by a change-list entry id that collector C holds), or when they have the same old and new wording after normalising whitespace and quotation marks **and** the same place (overlapping latest sentences, or the same target line). The place is required because one wording can be changed the same way at many places (the scrub turned `*Proof.*` into `*Why this and not its denial.*` at eleven lines, and these stay eleven changes). Vocabulary entries with the same old and new cells are joined without a place. A record with the same wording but no place joins only a group that has one place.

Links made: same_as 645, same old and new, same place 106, same old and new 2. Groups by size: 1 record: 994, 2 records: 149, 3 records: 89, 4 records: 10, 5 records: 14, 6 records: 3, 7 records: 7, 8 records: 1, 10 records: 1, 11 records: 1, 12 records: 1, 13 records: 2, 14 records: 1, 15 records: 1, 18 records: 1.

78 `same_as` pointers name a place in a file no collector recorded entry by entry (Revision 2 - revision note, draft of 23 September.md: 42; Revision 2 - worklist, draft of 23 September.md: 30; Revision 2 - plan and test round, draft of 23 September.md: 6). They point to a worklist item, a plan item or a row of the revision note's layer 2, each of which can cover several changes, so they are kept in the record and not joined.

The largest groups come from collectors' links between a proposal and its later restatements (collector A), or between a ruling and the several edits that carry it (collector D). The grouping step may want to split them:

| change | records | members |
| --- | --- | --- |
| CH-0152 | 18 | A-245, A-253, A-254, A-255, A-256, A-257, A-258, A-260, A-261, A-262, A-263, A-264, A-265, A-266, A-267, A-282, A-284, A-305 |
| CH-1018 | 15 | D-454, D-455, D-456, D-457, D-459, D-460, D-461, D-462, D-463, D-922, D-923, D-924, D-925, D-926, D-927 |
| CH-0244 | 14 | B-70, B-161, B-162, B-163, B-165, B-168, B-169, B-170, B-171, B-172, B-173, B-174, B-175, B-277 |
| CH-0148 | 13 | A-239, A-240, A-241, A-246, A-247, A-248, A-249, A-250, A-251, A-252, A-259, A-283, A-304 |
| CH-0997 | 13 | D-420, D-426, D-427, D-451, D-471, D-474, D-475, D-477, D-478, D-879, D-880, D-887, D-939 |
| CH-0143 | 12 | A-159, A-160, A-234, A-235, A-299, A-302, A-303, A-316, A-318, A-319, A-320, A-321 |
| CH-1131 | 11 | D-590, D-688, D-689, D-690, D-691, D-692, D-693, D-694, D-695, D-696, D-697 |
| CH-0437 | 10 | B-304, B-308, C-14, C-15, C-16, C-17, C-43, C-94, C-101, C-106 |

## The 40 latest-text sentences touched by the most records

Counted over placed records. A vocabulary entry (scope `term`) touches every place its words stood, so the table also gives the count without them.

| sentence | Part / heading | records | without vocabulary entries | changes | opening words |
| --- | --- | --- | --- | --- | --- |
| L542.s1 | Part XV / (Prov) Genesis | 27 | 16 | 23 | "**(Prov) Genesis.** Any of three: a selected transport whose value at an …" |
| L522.s1 | Part XIV / Declared inputs | 23 | 18 | 18 | "**Declared inputs.** Besides the two imports, some claims take stated inputs that …" |
| L526.s15 | Part XIV / Dependence order | 22 | 9 | 17 | "In Part VI, conflict depends on (F1), (F2), (A) and the target's …" |
| L317.s4 | Part VI / Problems | 20 | 8 | 17 | "Whatever the target does there, at most one of them is an …" |
| L369.s4 | Part VIII / A failed answer stays failed | 19 | 4 | 13 | "Here 'ruled out' is meant as in Part VI: the assessor holds …" |
| L526.s18 | Part XIV / Dependence order | 19 | 12 | 14 | "A representation defined only by its own construction, or an ownership and …" |
| L544.s1 | Part XV / (QF) Question-finding | 19 | 13 | 16 | "**(QF) Question-finding.** A case of finding a new question that treating a …" |
| L317.s7 | Part VI / Problems | 18 | 8 | 15 | "Their answers then agree at every pair of \(C\), so no argument …" |
| L536.s1 | Part XV / (Suff) Sufficiency | 18 | 16 | 15 | "**(Suff) Sufficiency.** A candidate meeting all four conditions of (E) on a …" |
| L315.s6 | Part VI / Rivals | 17 | 6 | 12 | "A claim is **ruled out** for an assessor \(j\) when an argument …" |
| L223.s5 | Part IV / Prediction, surprise, violation | 16 | 11 | 13 | "Prediction and violation are defined for every transport to the simulation layer, …" |
| L31.s4 | Part 0 / What is imported, what is an index, and what is defined | 15 | 8 | 14 | "No undefined predicate that says 'explains' without a question and a contract, …" |
| L299.s2 | Part VI | 15 | 13 | 9 | "Criticality is relative to the route \(W\) it is assessed in, a …" |
| L315.s7 | Part VI / Rivals | 15 | 4 | 10 | "A candidate is **not ruled out** for \(j\) when no argument usable …" |
| L540.s2 | Part XV / (Elim) Reinstatement of kinds | 15 | 12 | 10 | "An argument that exhibits such a case would rule out the Consequence …" |
| L25.s3 | Part 0 / What this document does not claim | 13 | 8 | 11 | "It does not attribute an achievement to contributors beyond what a history …" |
| L31.s1 | Part 0 / What is imported, what is an index, and what is defined | 13 | 6 | 13 | "The semantics has two imports: the **physical module** \(\Theta\), which says what …" |
| L313.s2 | Part VI / Commitments that do no work | 13 | 11 | 12 | "A commitment \(d\) of a candidate that has a route does no …" |
| L317.s14 | Part VI / Problems | 13 | 9 | 12 | "A finer contract that contains a change at which two rivals conflict …" |
| L455.s2 | Part XI / Appraisal | 13 | 8 | 10 | "Where a claim invokes an appraisal, the semantics takes the **appraisal relation** …" |
| L538.s1 | Part XV / (Nec) Necessity | 13 | 11 | 10 | "**(Nec) Necessity.** A candidate such that an argument not using (E) rules …" |
| L31.s3 | Part 0 / What is imported, what is an index, and what is defined | 12 | 6 | 10 | "Everything else is defined in terms of the two imports, the structural …" |
| L119.s3 | Part II / Kinds are edit-signatures | 12 | 10 | 11 | "For two explanatory candidates (Part V), let \(E\) and \(E'\) be their …" |
| L201.s1 | Part IV / Three provenances | 12 | 5 | 10 | "A physical system may hold selected transports at the object layer and …" |
| L245.s4 | Part V | 12 | 7 | 10 | "By (K), no component of \(E\) whose signature on \(C\) differs from …" |
| L313.s3 | Part VI / Commitments that do no work | 12 | 10 | 11 | "When \(\Gamma\) is infinite, a block of such commitments can still be …" |
| L317.s1 | Part VI / Problems | 12 | 5 | 11 | "**Problems.** Two rivals, neither of them ruled out for an assessor, pose, …" |
| L317.s15 | Part VI / Problems | 12 | 4 | 10 | "A contract narrowed to leave out the pairs at which two rivals …" |
| L317.s17 | Part VI / Problems | 12 | 4 | 10 | "A problem that a system represents can be a recognized difficulty (Part …" |
| L455.s1 | Part XI / Appraisal | 12 | 5 | 10 | "**Appraisal.** Repairing an aim repairs it and says nothing about how anyone …" |
| L598.s2 | Part XVI / 6. There are two imports | 12 | 7 | 9 | "By the dependence order of Part XIV, which lists the declared indices …" |
| L211.s4 | Part IV / Representation is defined, not supplied | 11 | 6 | 8 | "A carrier keeps its provenance when present access to it is lost, …" |
| L317.s13 | Part VI / Problems | 11 | 7 | 11 | "Two rivals that are both accounts on \(C\) conflict only outside it, …" |
| L317.s16 | Part VI / Problems | 11 | 9 | 9 | "Nothing here counts rivals or orders candidates: of one candidate, what is …" |
| L369.s5 | Part VIII / A failed answer stays failed | 11 | 3 | 8 | "If a premise about them ceases to be live, the argument is …" |
| L397.s1 | Part IX / Arguments | 11 | 4 | 10 | "**Arguments.** A record leaf is a reference to an event with an …" |
| L429.s2 | Part X / Episodes | 11 | 5 | 10 | "A **recognized difficulty** is a failure of a claimed aim, or a …" |
| L518.s1 | Part XIV / Imports | 11 | 8 | 9 | "2. The **appraisal relation** \(\mathcal N\), when a question invokes an appraisal. …" |
| L526.s13 | Part XIV / Dependence order | 11 | 8 | 11 | "(P), (EX) depend on (G), (E), Deploy; (P) also on ProducedBy and …" |
| L536.s3 | Part XV / (Suff) Sufficiency | 11 | 11 | 9 | "A table that encodes the response to every admitted change does not …" |

Sentences of the latest text touched by at least one record: 540 of 756 units.

## The 40 terms met in the most records

The term list (204 terms) is in `anchor - scripts/step3 side data.json`. It holds the bold defined terms of the latest text, the run-in labels that name a defined notion, the tagged conditions with names of two or more characters, and the old names the S95 vocabulary replaced (the draft 5 column of `tests/S95 Scrub - vocabulary, as used.md`, plus the old names it gives in prose). A term is matched in a record's `old` and `new` wording, ignoring case and allowing a plural or past ending. Old names are shown in backticks: they are quoted words, not this page's own.

| term | kind | records | changes |
| --- | --- | --- | --- |
| argument | defined | 238 | 164 |
| contract | defined | 197 | 136 |
| declared | defined | 194 | 154 |
| transport | defined | 141 | 94 |
| `derivation` | old name (S95) | 119 | 103 |
| input | defined | 102 | 77 |
| content | defined | 77 | 58 |
| test | defined | 73 | 60 |
| Repair | defined (run-in label) | 72 | 57 |
| conflict | defined | 68 | 50 |
| `obligation` | old name (S95) | 67 | 58 |
| `primitive` | old name (S95) | 67 | 59 |
| route | defined | 61 | 45 |
| selected | defined | 60 | 43 |
| `anchor` | old name (S95) | 55 | 48 |
| (F1) | defined (tagged condition) | 50 | 41 |
| problem | defined | 50 | 41 |
| ruled out | defined | 50 | 34 |
| provenance | defined | 49 | 34 |
| `proof` | old name (S95) | 49 | 40 |
| faithful | defined | 46 | 36 |
| `established` | old name (S95) | 45 | 41 |
| `derive` | old name (S95) | 42 | 35 |
| signature | defined | 41 | 32 |
| `worth` | old name (S95) | 41 | 38 |
| `ground` | old name (S95) | 40 | 35 |
| surprise | defined | 39 | 31 |
| `receipt` | old name (S95) | 37 | 34 |
| declared inputs | defined | 37 | 28 |
| rivals | defined | 37 | 31 |
| `witness` | old name (S95) | 35 | 35 |
| represents | defined | 33 | 27 |
| `refute` | old name (S95) | 32 | 30 |
| Ownership | defined (run-in label) | 32 | 27 |
| (K2) | defined (tagged condition) | 32 | 20 |
| tentatively accept | defined | 32 | 22 |
| (F2) | defined (tagged condition) | 31 | 24 |
| constructed | defined | 29 | 25 |
| `satisfies` | old name (S95) | 29 | 26 |
| `normative relation` | old name (S95) | 29 | 25 |

Records with no term in their wording: 430.

## Where the program needed judgement

- **Paragraph anchors.** Where no sentence on the mapped line comes to 0.25, the whole paragraph is the anchor (54 records). Declarations placed on a named line take the paragraph when their text is a paraphrase.
- **Vocabulary entries.** Their cells mix words, quoted phrases and descriptions; the program reads the quoted phrases, the words before any bracket, and any line numbers. 224 entries are placed; 12 could not be (listed above).
- **Removals.** A record that deleted a sentence is placed on the sentence of the same paragraph most similar to what was deleted, or on the paragraph.
- **Anchors taken from the group.** 23 records took the place of another record of their change; `anchor_method` names it.
- **`latest_nearest`** is a lead, not a place: it is the sentence sharing most content words with the record in the Part its source names (word overlap of 0.15 or more).
- **Parts and headings** for records with no anchor come from the Part number their source gives; the Part titles changed (for example Part VI's), the numbers did not.

## Rerun

From `group/anchor - scripts/`: `PYTHONDONTWRITEBYTECODE=1 python3 step1_index.py`, then `step2_maps.py`, `step3_anchor.py`, `step4_summary.py` and `step4_check.py`. The check confirms that every collector field is unchanged, every sentence id exists, the status agrees with the anchor, every "yes" in `new_in_latest` is found in the latest text and in the anchored sentences, the change groups agree, and that the words of decision S23 are absent from this step's own prose.
