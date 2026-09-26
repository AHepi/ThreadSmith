# Collector B - coverage

*Written by collector B for S98, 26 September 2026, on the tree at commit 81e7ac0 (with this folder untracked). The records are in `collector B.jsonl` beside this file: 310 records, one JSON object per line, in the shape the S98 task gives. Nothing was committed.*

**Stretch.** File 10 to file 11, and the checks on file 11: (1) the edits that made file 11 from file 10, by a sentence-level diff; (2) the S81 recommendations about file 11; (3) the S87 cross-examination returns, where they propose theory wording; (4) the S88 three defects and their repair wordings; (5) S89's suggested wordings against the two source books.

## The records

| rids | round | what | count |
|---|---|---|---|
| B-1 to B-182 | S76 | edits, file 10 to file 11, by program | 182 |
| B-183 to B-190 | S81 | errata XR1 to XR7 (XR2 has two pointers) | 8 |
| B-191 to B-213 | S81 | the twelve unclear wordings of determination 03 §8, one record per place | 23 |
| B-214 to B-216 | S81 | the three reading hazards (determination 04 §7.10) | 3 |
| B-217 to B-258 | S81 | the 42 undeclared places to declare (41 inside the theory and M7), one per layer-2 row | 42 |
| B-259 to B-278 | S88 | wordings as first proposed (Claude's checks 01 to 03), the post-Atria wordings, F4 and Atria's own wording | 20 |
| B-279 to B-290 | S88 | the settled wordings, the held-back general bound, the fallback, the L514 clause | 12 |
| B-291 to B-310 | S89 | handlings of the fifteen observations and the missed relations M2, M3, M4, M6 | 20 |

S87 gives no records (see below).

### Counts by kind and status

| kind | applied | not applied | declined | superseded | open for the owner | unknown | total |
|---|---|---|---|---|---|---|---|
| edit | 182 | 0 | 0 | 0 | 0 | 0 | 182 |
| recommendation | 92 | 13 | 9 | 13 | 0 | 1 | 128 |
| **all** | 274 | 13 | 9 | 13 | 0 | 1 | 310 |

By round: S76 edits 182 (applied). S81: 70 applied, 4 not applied, 1 declined, 1 unknown. S88: 8 applied, 9 not applied, 2 declined, 13 superseded. S89: 14 applied, 6 declined.

By scope: edits 121 sentence, 61 span; recommendations 78 sentence, 30 span, 16 paragraph, 4 whole text. Records whose "new" is a description ("[no wording given] …"): 101. Records with a same_as entry: 126.

The edits by how the sentence changed: 75 changed in place, 71 added, 29 removed, 5 moved unchanged (Part XV's five attack labels, from Part 0 to Part XV), 2 moved and changed.

## How the records were made

**Part 1, the diff (B-1 to B-182).** A program split each line of file 10 and file 11 into sentences, with inline and display math (`\(…\)`, `\[…\]`) masked so that no split falls inside it. A sentence ends at `.`, `?`, `!` or the end-of-proof mark `∎`, with any closing marks, before a space and a capital, digit, opening mark or math. Headings are units of their own. The two sentence lists (752 and 794 units) were aligned with a sequence matcher. Unmatched sentences were then paired: first identical sentences anywhere (moves), then, inside each changed block, pairs whose word similarity is at least 0.5 (or where the shorter sentence is carried almost whole by the longer), then across blocks at 0.65. What is left is recorded as added or removed.
- Each record's `target_text` is file 10 and `target_line` its file-10 line; for an added sentence, the line of the file-10 sentence it follows. `source_ref` gives both places, for example "changed f10 L569 s3 -> f11 L562 s3", and the S81 place ids (M1 to M59, determination 03 §1) whose file-11 lines the record falls on (125 of the 182).
- For a changed sentence with one short changed stretch, `old` and `new` hold that stretch in whole words (scope "span"), and `old_sentence` and `new_sentence` the whole sentences. Where one side of the stretch is empty, one word of context is kept on each side. Otherwise `old` and `new` are the whole sentences (scope "sentence").
- **Sentence numbers.** The diff counts a bold run-in label ("**Claim.**", "**Ownership.**") as a sentence. The S81 files, the change list and the revision note do not. So f11 L257 s4 in a diff record is "the third sentence of line 257" in S88 and the change list. The recommendation records use the sources' own numbering in `source_ref`, and quote the text itself in `old`.

**Parts 2 to 5.** A second program built each recommendation from its source by line number and marker, so that every wording is copied byte for byte (LaTeX included). Two marks were removed from quoted wordings and nothing else: the `> ` blockquote marker at the start of a quoted line, and the four-backtick fence lines. Where a source abbreviates the rest of a sentence (check 01's Option A ends "\(e_n\le\ldots\)"), the record holds the stretch before the abbreviation and says so in `source_ref`. The `old` of each recommendation is taken from file 11 by the place the source names (file 10 for F4 and Atria's own wording, which are about file 10's Derivation 3).
- **Status.** A recommendation with exact wording is "applied" where its wording is verbatim in a later text, and `applied_in` names those texts, found by program in draft 1 to the latest text. A description carried by a revision 2 change-list entry is "applied", and `applied_in` names the entry and the texts in which the entry's NEW text is verbatim. "Superseded" marks an earlier wording that a later wording in the same round replaced. "Declined" marks an item the revision 2 plan or change list left out (W18, W27 as narrowed, W32(c), W34 for reach, W42, W43 with its reason, W44, W46), and wordings the sources did not adopt. "Not applied" marks fallbacks, options not taken and items with no change-list entry.
- **same_as.** A record of the same change seen elsewhere, given as a rid (B-…) or as `path#id` for a later round's source: `tests/Revision 2 - change list, draft of 23 September.md#W19.2`, `tests/Revision 2 - worklist, draft of 23 September.md#W30`, `tests/Revision 2 - revision note, draft of 23 September.md#L2-17`, `tests/Revision 2 - plan and test round, draft of 23 September.md#W42`. The grouping step can join on these with the collectors of revision 2. Inside S88, each earlier wording points to the settled wording that replaced it, and back. F4 (B-277) points to the file-11 edits of Derivation 3 and of Part XV's entry (D) (B-70, B-161 to B-163, B-165, B-168 to B-175), and they point back.
- **No reasons.** No record copies why a change was made or proposed. Where a source gives no wording, `new` holds its description of the change, taken from the source's own handling words where it has them, prefixed "[no wording given] ".

## The program checks

Run over all 310 records after the last write:
- **Shape.** Every record has the sixteen fields in order, a listed status, kind and scope. Faults: none.
- **Every `old` is verbatim in its target text** (file 10 or file 11 as `target_text` names it): 310 of 310 with no miss (the records with an empty `old` are additions and descriptions with no place). **Every `old_sentence` is verbatim** in its target text: no miss.
- **Every edit's `new` and `new_sentence` is verbatim in file 11**: no miss.
- **Every same_as pointer resolves** to a rid in this file or to a file that exists: no miss.
- **S23 words in collector B's own fields** (`source_ref`, `applied_in`, `target_part`, and descriptions in `new`), quoted words set aside: none left except the theory's own Part and heading names in `target_part` ("Part VI — Work, support, and interference", "What is primitive, what is an index, and what is derived", "Representation is derived"), which are the target text's words.

## Sources read

md5 of each file as read (tree at 81e7ac0).

| source | md5 | how read |
|---|---|---|
| `authority/10 Claude Fable Semantics - standalone theory.md` | 3a8cd7c8ca6f3ad3b8a85ab9984d850e | whole, by program |
| `authority/11 Claude Fable Semantics - standalone theory, revision 1.md` | 5e494c1095d920d128b9a79de378f923 | whole, by program; the lines named by the sources in full |
| `results/S81 Results - file 11 against file 10, determined.md` | 62313c32700aee59c1f0887ceaa66331 | headings; The result, Errata, Rulings adopted after the data, Findings beyond the round, Not tested, Next step |
| `results/S81 … outputs/determination/03 Step 4 - every difference … ruled ….md` | f4ae3b540ff4807da7ad00ae93d94df4 | head, §1 table (by program), §5, §8 |
| `results/S81 … outputs/determination/04 Step 3 and the determination - file 11 against file 10.md` | 2f25f0f8012132967acc2af6c6692f7b | headings, §7.8, §7.10 |
| `results/S81 … outputs/determination/10 Reading of Mimo's retry - O5 and O30.md` | d518d161e038379d1011ddef0c72fa29 | §9 (revision 2 notes) |
| `results/S81 … outputs/determination/` 01, 02, 05 to 09 (md5 00aa0145…, 172597ed…, 706d4207…, 8bd1cfd5…, 419be115…, 66f50284…, 2d7a0dda…, e5bcfa9a…, 9b312ab0…) | as given | program scan for proposed wording; the matching lines only |
| `results/S81 … outputs/determination/raw readings/` (all files) and `returns/*.response.txt` | not hashed | program scan for proposed wording; the matching lines only. Every match is one of the items 03 §8 and 04 §7.10 collect, or not a proposal |
| `results/S87 … returns/s87_xexam_atria.response.txt` | b0d40330609a95ed215012ec5f5c9494 | headings and a scan for proposals |
| `results/S87 … returns/Mimo in three parts/s87_xexam_mimo_P2.response.txt` | 7b1c7e971ab00db0ce87ce5c08d57038 | point headings; point 6 in full |
| `results/S87 … returns/Mimo retry one row per call/s87_xexam_mimo_O5.response.txt`, `…_O17…`, `…_O30…` | 2700173d57b93d5e55b47f120798869d, 7c6d9812f56bb7063209e100ad91ab6d, fd019812032d83877c790293987b43ff | point headings and a scan for proposals |
| `results/S88 Reading of Atria's reply - the three defects.md` | b19acbc191749a1dce059b8deeb8bcad | headings; the three R6 repair sections; Further counterexamples item 1; Changes to the repairs |
| `results/S88 Reading of Mimo's reply in three parts, and the settled positions.md` | 1137aaac24409e2cfa6f48b4c7ffd1f9 | the three settled positions and final wordings; Further counterexamples and further defects; the held entries |
| `results/S88 Claude's checks of the three defects/01 (T2) bound.md` | acc3c711649cfa990381dc3f21b358a0 | §5 |
| `results/S88 Claude's checks of the three defects/02 Derivation 2 and non-circular dependence.md` | 21fb77e9f968a0e2d3724208ce144e80 | §1.7, §2.8, §3 |
| `results/S88 Claude's checks of the three defects/03 the defence.md` | a0456f7494c268ec71c86cf636f6c355 | §C |
| `results/S89 The theory against its sources - Deutsch and Marletto.md` | 74880c47b03cb8d97a071602b826ab32 | head, summary table, the Handling lines, Relations the first reader missed, The observations most worth acting on. No book quotation is copied into any record |
| `tests/Revision 2 - change list, draft of 23 September.md` | c6d25ec1ccc3ea3e72136a75a794be62 | join keys only: conventions, entry headings, STATUS, FILE-11 LINE, OLD and NEW fences (by program); decision lines on W18, W27, W42 to W46 |
| `tests/Revision 2 - worklist, draft of 23 September.md` | 0fd2dae035c44469045a89ee9cea44dd | join keys only: the summary table |
| `tests/Revision 2 - revision note, draft of 23 September.md` | c638b0caef45bc05f873f889abd241bf | join keys only: layer 2 rows (id, M, part, file-10 and file-11 locators) |
| `tests/Revision 2 - plan and test round, draft of 23 September.md` | 1096707365316533600737921957002d | the lines on W18, W27, W42, W43, W44, W46 |
| draft 1 to the latest text (the eight `tests/Revision 2 - …` theory texts) | dd2741b0…, 9aecf2f3…, 403c4f2f…, fc55b470…, 7f1d8ad0…, 2517ef4e…, 8bb4d19d…, ebca15a0… | by program only: whether a wording is verbatim in them; the first lines of draft 1 and the latest text |
| `records/Semantics - Decisions.md` | d3a6b746b7c15c2527bd2cea65122c07 | S17 to S29 |
| `records/Semantics - project story.md` | not hashed | grep for file 11 and S76 |

## Sources skipped, and why

- **S81 outputs:** every `*.request.json`, every `*reasoning*` file, `briefs/`, `stage1/`, the sample JSONs, `table.md`, `trial - DeepSeek as a third auditor/`, `supplementary - Mimo on tester A in four parts/` (its reading, determination 07, changed no ruling), the Sonnet testers set aside by decision S16, and the effort controls. They carry the calls, the marks and the readers' reasoning, not recommendations about file 11's wording.
- **S87:** requests, reasoning, truncated passes, errors and receipts. **No S87 reply proposes theory wording.** Atria and Mimo rule on the determination's rows. Atria calls the L161 s3 hazard "properly recorded for a later revision", and Mimo's O30 reply calls the boundary hazard "worth recording"; both endorse S81 items already recorded (B-214, B-215). Mimo's P2 point 6 asks for file-10 text, not for a change.
- **S88:** the raw returns (`results/S88 Cross-examination - three defects - returns/`), `results/S88 Mimo reading parts/`, and the two "how it will be read" files. The reading files quote what the replies proposed and settle it, and the settled positions file gives the final wordings; the reading rules propose no wording.
- **S89 handlings with no change proposed:** aesthetics ("(d) keep empty"), observation 15's cases (cases, not text), and missed relations M1, M5, M8 to M11 (descriptions of agreement or abstention; M7 and M8 are folded into observations 2 and 5, which are recorded).
- **S81 items that are not about the theory text:** the S75 corrections (case verdicts), the rulings adopted after the data, and the notes on readers, effort and receipts.

## What could not be recovered, and limits

- **The third reading hazard (O10, B-216)** names no place and no wording; its status is "unknown". The worklist's item for O10 is W30, and the record points there.
- **Twelve unclear wordings become 23 records**, one per place the item names. Where an item quotes no phrase (item 3; item 5 at L586 and L518; item 7), `old` is the whole sentence at the place.
- **Unclear wording 5 at L586, and item 7 (L536, L582)** have no change-list entry; they are "not applied". A later collector may find that a different entry reworded those lines.
- **The count of undeclared places.** S81 counts "41 undeclared CLAIM places inside the theory (and M7)". The revision note's layer 2 has the same 42 rows, and they match the master table of 03 §1 once M38 and M48 (whose rulings are in bold) are counted. B-217 to B-258 follow layer 2. These are recommendations to declare, carried by the revision note, not by any theory text.
- **The diff pairs by similarity.** Eight changed pairs sit between 0.5 and 0.66 in word similarity; each was read and kept (for example f10 L444 s1 "(P) does not rank alternatives." carried whole inside f11 L433 s2). The diff cannot tell a rewrite from a deletion plus an addition when the words share little; such cases are recorded as removed and added. Its 182 sentence records are finer than S81's 59 places, and one S81 place can span several records (the M ids in `source_ref` join them).
- **The settled S88 wordings** entered revision 2 at draft 2 (draft 1, sent for S90, carried only the first 48 changes). Several were then changed by later rounds: the sentence after (K) is verbatim in drafts 2 to 4 only, and the typing of \(\Gamma\) in draft 2 only. `applied_in` gives the texts for each, and the later changes are for the collectors of revision 2.
- **Theory headings in `target_part`** are the target text's own words and are left as they stand, although three contain words from S23's list.
- The programs were run from the session scratchpad (`b_diff.py`, `b_lib.py`, `b_recs.py`, `b_check.py`) and are not in the repository. The method above is enough to rerun them.
