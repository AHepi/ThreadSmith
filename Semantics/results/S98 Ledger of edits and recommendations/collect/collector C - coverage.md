# Collector C - coverage

*Written by collector C for S98, 26 September 2026, on the tree at commit 81e7ac0. The records are in `collector C.jsonl` beside this file: 209 records, one JSON object per line, in the shape the S98 task gives (md5 of the file as written: see the last section). The scripts that made them are in `collector C - scripts/` (run in the order step0 to step3; the scratchpad holds their working files). This collector committed nothing and wrote nothing outside this folder; the orchestrator's work-in-progress commit 4a857f8 (11:03 UTC) holds an earlier state of this file and of three of the scripts.*

**Stretch.** Revision 2 up to draft 5: (1) every entry of the change list as it stands at draft 5; (2) every earlier wording of an entry, in change-list drafts 1 to 4 and so in file 13 drafts 1 to 4, with the S90 and S93 brief ids that carried it; (3) the wordings of the S90 and S93 rulings: the FIX wordings, and the wordings the readers proposed that a ruling kept out or passed on; (4) the worklist items whose wording never became an entry. The change list's own findings with wording are added under (3).

## The records

| rids | what | count | status |
|---|---|---|---|
| C-1 to C-67 | every entry of change list draft 5 (W1.1 to W1.2, with W61.1 and W35.5); old and new are the entry's OLD and NEW byte for byte, target file 11 | 67 | applied 67 (62 theory and meta entries; the 5 record-only entries W3.1 to W3.5 are "applied" to layer 2 of the revision record, with the theory text unchanged) |
| C-68 to C-85 | earlier OLD/NEW of 13 entries in change-list drafts 1 to 4 (W38.1 twice, W37.1, W36.1, W19.1 twice, W35.1, W35.2 twice, W20.1 twice, W34.1, W33.1, W59.1, W24.1, W22.1, W7.5 twice) | 18 | superseded 18 |
| C-86 to C-88 | the three held placeholders of change list draft 1 (W19, W20, W31) | 3 | superseded 3 |
| C-89, C-90 | the two edits the S90 rulings made to the note only (W40.1's declaration; W6.3's declaration, added) | 2 | applied 2 |
| C-91 to C-110 | the FIX wordings of the rulings, one record per ruling, read off the line diff draft 2 → draft 3 (S90) and draft 4 → draft 5 (S93), plus the X18 fix to the sources note and the three declaration fixes | 20 | applied 18, superseded 2 |
| C-111 to C-145 | S90: the readers' proposals (from the replies, as the rulings quote them) and the rulings' own options | 35 | declined 21, not applied 9, superseded 3, applied 1, open for the owner 1 |
| C-146 to C-185 | S93: the readers' proposals (cut from the tabulation, which copies them from the replies), the rulings' options, and the findings carried forward without wording | 40 | declined 21, not applied 12, open for the owner 6, applied 1 |
| C-186 to C-189 | the change list's own findings with wording ("Findings carried forward"; "Found in draft 4") | 4 | not applied 2, superseded 2 |
| C-190 to C-209 | worklist items with wording that is in no entry | 20 | superseded 9, declined 7, not applied 4 |

**Counts by kind and status.**

| kind | applied | superseded | declined | not applied | open for the owner | total |
|---|---|---|---|---|---|---|
| edit | 69 | 18 | 0 | 0 | 0 | 87 |
| recommendation | 20 | 19 | 49 | 27 | 7 | 122 |
| **all** | 89 | 37 | 49 | 27 | 7 | 209 |

By round: S90 146 (the change list as drafted and fixed in S90, the S90 rulings, the worklist), S91 7 (the draft-4 wordings of group H and the "Found in draft 4" finding), S93 56. By scope: sentence 100, span 79, paragraph 22, term 5, whole text 3 (the note of sources and departures). Records whose "new" is a description ("[no wording given] …"): 25. Records with a same_as entry: 45, of which 5 point to collector B (the S88 settled wordings that W19.1, W19.2, W19.3 + W10(b).1, W20.2 and W20.3 carry byte for byte). By target text: file 11 111, file 13 draft 2 32, file 13 draft 4 36, the note of file 13 (declarations) 22, the note of sources and departures 7, file 12 1.

## How the records were made

- **Change-list versions.** The change list was parsed by program (`lib_c.parse_changelist`: `###` sections, the fields, and OLD/NEW between four-backtick fences) at each of its five commits (`step0_git_versions.py`). Every OLD occurs once in file 11 in every version. The first version whose OLD and NEW equal the draft-5 entry gives the record's round (drafts 1-3 S90, draft 4 S91, draft 5 S93). A change in an entry's OLD or NEW between versions gives one superseded record per distinct wording, with applied_in the file 13 drafts built from those versions; each such NEW was found verbatim in each of those drafts.
- **Briefs.** Every item of the S90 brief (C01-C48), the five S90 parts (R01-R55) and the eleven S93 parts (X01-X18) was matched by program to the change-list version its OLD and NEW come from, and its id is named in the record's source_ref. All match the version the brief was built on, except: X09 and X10 give NEW by reference to their excerpt and X18 leaves out the anchor, so they were matched by containment (by hand, then by program); X11 is the proposed entry, whose wording entered draft 5 unchanged as W61.1. No brief carries a wording that is in no change-list version.
- **FIX wordings.** Draft 3 differs from draft 2 in 8 lines (8 entries), and draft 5 from draft 4 in 7 lines (7 entries); each changed line was assigned to its entry by program and to the ruling that fixed it. old and new are the changed words, widened to whole words (at least three where the sentence allows); old_sentence and new_sentence are the whole sentences around them. target_text is the draft the ruling read, and target_line is that draft's line.
- **Proposals.** Every quoted wording was cut from its source file by program (a marker pair, a fence, or a literal checked to occur), never retyped. old is the wording of the draft it would replace, checked to occur there. Where a proposal adds words and no replacement can be built, old is empty and target_line is found from an anchor. Where a source gives a description only, "new" begins "[no wording given]".
- **Statuses.** applied: the wording stands in the text named in applied_in. superseded: it stood in an earlier draft, or was taken in other words, and was replaced. declined: a ruling, a check or a decision of the change list kept it out. not applied: it never entered, and no ruling kept it out (carried forward, or an optional wording). open for the owner: the six (c2) proposals of S93 and the R31 note "for the owner".
- **applied_in** lists every theory text in which the new wording is found verbatim, from file 13 draft 1 to the latest text; a wording changed later (by the scrub or the repairs) is simply not listed for those texts.
- **same_as** links only records of one change: a ruling's FIX wording, the change-list wording it produced, and a reader's proposal the ruling took word for word; links are symmetric and transitive. A link from a declined or replaced proposal to the wording taken instead is written in source_ref ("wording taken instead, or the related change"). Collector A and B records whose "new" (40 characters or more) equals a record's new, or lies inside it and not inside its old or file 11, are linked.
- **Declarations** of the note are recorded only where a ruling changed nothing but a declaration (C-89, C-90 and their rulings) or a reader proposed declaration wording.
- **No reasons.** No record carries why a change was made or refused; source_ref names the entry, ruling, reply point or worklist item, and the outcome (FIX, KEEP, refused, not taken).

## Program checks (`step3_finish.py`)

- Shape: every record has the task's sixteen fields in order, a kind, status and scope from the task's lists, and a source_file that exists. No miss.
- Every "old" of a record whose status is applied (89 records) is found verbatim in its target text: file 11 for the change-list records, file 13 draft 2 or draft 4 for the ruling records, the change-list declarations or W38.1 NEW of the named draft for the note records. **Misses: none.**
- Every "new" of an applied or superseded record is found verbatim in each theory text its applied_in names. **Misses: none.**
- Every FILE-11 LINE field agrees with the line on which OLD begins. The step scripts report no problem (cut markers unique, anchors found, entries identified).
- The book quotations inside the recorded wordings are the ones already in the change list and its earlier versions (the note of sources and departures, three short quotations, none over three words); no quotation from a book was added.

## Sources read

Read in part by eye and whole by program unless marked "program only". md5 of the file as read.

| md5 | source | how |
|---|---|---|
| c6d25ec1ccc3ea3e72136a75a794be62 | tests/Revision 2 - change list, draft of 23 September.md | frame sections and entries read; all parsed |
| (git) 12e73da, 587eebf, 99e9cd0, 3f7c3ab, 8816fcf | the same file at its five commits (md5 f50930771cb582fd49311b9e66daae9c, a5c92adc9f1e3806c0f9c6394cffde1e, 1488a9cd41c4a284be78769019acf7ca, b6b2ea95ea9e21ebea3316d8e9fa4b40, c6d25ec1ccc3ea3e72136a75a794be62) | parsed; held placeholders read |
| 0fd2dae035c44469045a89ee9cea44dd | tests/Revision 2 - worklist, draft of 23 September.md | parsed; Handling fields of W1-W50 read |
| 5e494c1095d920d128b9a79de378f923 | authority/11 … revision 1.md | program only |
| ce7e8e2c5f89d982fa888c19587d508b | authority/12 … causality, standalone theory.md | one search (L325) |
| dd2741b0d5a18617d845b19b874943f4 | tests/Revision 2 - file 13 draft, theory text, as sent for cross-examination.md | program only |
| 9aecf2f30ce0b4523606b2b8409fdf37 | … file 13 draft 2, theory text, as sent for cross-examination.md | program; lines read |
| 403c4f2fb3e5d57bb48a5647011c9f91 | … file 13 draft 3, theory text.md | program only |
| fc55b470c63cd4b3c27d6aa64d8d8c17 | … file 13 draft 4, theory text.md | program; lines read |
| 7f1d8ad02adf96e27622593bd263252e | … file 13 draft 5, theory text.md | program only |
| 2517ef4ec1f274e8de2bfb7e6661ef94 | … draft 5, scrubbed of verificationist words, theory text.md | program only (applied_in) |
| 8bb4d19d5aad53de2492b2193fd23ff1 | … scrubbed copy, repaired (S96), theory text.md | program only (applied_in) |
| ebca15a047f686b15d5f5766b69825c9 | … scrubbed copy, repaired (S96), after cross-examination, theory text.md | program only (applied_in) |
| a7cfeb263f11c27f7f781b701eeabeeb | tests/S90 Cross-examination - revision 2 draft, the first 48 changes.md | items parsed |
| 1364c50fdc388e091552bbf41b538d76, 234bf749788fc3ab3ddcb1e06e249f98, 130a5eace514ebb02b736d12a311ade2, d214f495e0b9fcac4f423d522bee0d37, 2183faa5005b112347f484b6c8ace196 | tests/S90 Cross-examination - part A1, A2, B1, B2, C | items parsed; A1's item form read |
| 852342f348dac7baa52b87b2deab333f, 712ae2d47e35ad96083ef208d808f8f3, 902c9ea16de250837e05a607aaf6179d, 3acf25ca82b9873888287528b4ca3c15, d91a2a693b5e69e3a43b44e9a245f5cb, 9331bd89299b5dc76f29144a26cbf431, 116b65985d098eb606855954fa34bc71, 4be1172e57216bd67a9a9dce66ba2040, 2be35c1ec040d791e348acacaae6a79c, 48c0e74429d7be0b3de79b1382199e37, 0c3bb649152a55104195e908f38ec498 | tests/S93 Cross-examination - draft 4 - parts A to K | items parsed; A, E and F items read |
| 56219a1d3bf20e22ea241cb18ff8a426 | results/S90 Reading of the replies - batch 1 (…).md | rulings and pending edits read |
| 4579cec0541b1af1f4757c783e05f1cb | results/S90 Reading of the replies - batch 2 (…).md | rulings and pending edits read (fences cut by program) |
| 6849fb4cc9f1ce00fbdc6555a0a05d21 | results/S90 Reading of the replies - batch 3 (…).md | rulings and reconciliation read (fences cut by program) |
| 31 files, md5 in `sources` below | results/S90 reading rulings/*.md | all fences parsed and searched; the passages quoting repairs read |
| 10 files, md5 in `sources` below | results/S93 reading rulings/*.md | searched; the passages on offers not taken read |
| 2f3551b8017c9e6e0de6c575a42f9c8d | results/S93 Reading of the replies.md | sections 4, 6, 9 and 10 read |
| 739d4d6bccc83caa03589bd45d030396 | results/S93 Tabulation of the replies, before any ruling.md | sections 3, 4 and 6.2: the proposed wordings cut by program |
| 19b8545b…, d9fc7c6c…, b18f8534…, 368eddf9…, 5efafef1…, 6d8323bf…, 4ba1fdf2…, cdcb11d2…, 4b04caa8…, 6e2307cd… | results/S90 Cross-examination - revision 2 draft - returns/parts/*.response.txt (Atria A1, A2, B1, B2, C; Mimo A1, A2, B1, B2, C) | searched for repairs; the repair lines cut by program |
| eb3779a3415a4bbec9f056b0194afb28 | records/Semantics - project story.md | entries S90, S91 and S93 read in part |
| d3a6b746b7c15c2527bd2cea65122c07 | records/Semantics - Decisions.md | S23 and S28 read (the words rule for this file's prose) |

`sources`: the S90 rulings, with md5: atria_A1 item 1 R01 350b00ba83df86898875ce993f691093; atria_A1 item 2 R17 1db4518b806bb9334ae654bd663b56dd; atria_A2 item 1 R51 6e1af65fedc5f743d1eeba9121978bea; atria_B1 R39 71e79d6308a363a77e014f82b206af47; atria_B2 item 1 R42 47000fd11f286be3a676298c90f566f3; atria_B2 item 2 R31 b1d84e98d086d354df938d76a7397be6; atria_B2 item 3 R32-R33 d07e56b2b2bc048ad33a6b6f993fa6c6; atria_C item 1 R13 5a35bb939c214d156be7ed9160645c0e; atria_C item 2 R06 6ca49961f50f78586c819d565ef221da; atria_C item 3 R21 e72966e1242786033e9cc68f04d905a2; atria_C item 4 R24 2474458947460c4d758775530d6a9b3a; atria_C item 5 R25 c2b72cbeefd03e5e7dd7cf0641b44720; atria_C item 6 R30 4703e729928f2ac500bfea3b07db0d12; atria_C item 7 R34 e797c134e2ea366d478a0ca042889041; mimo_A1 R01 7eb829599cde0a94543c750394d23e00; mimo_A1 R08 96500cef6c7087b60c4770f1ea14d008; mimo_A1 R15 16f0d68796b43058b528de5caf1c57a1; mimo_A2 R26 a071d566df2858d110ab72f904f64b37; mimo_A2 R28 c36fa775835af83ea5c7c98302905112; mimo_A2 R51 a586279ae712f1ae74022bfffb82f688; mimo_B1 item 1 R04 78fa498408bfe4366d5fa1f7964f4b2d; mimo_B1 item 2 R39 503df60170a2e307a0f1aa6db1bf0685; mimo_B1 item 3 R48 532245a0c17f0db620d245b3438313b0; mimo_B2 item 1 R31 405d2e895ce435b914beda407b45ca94; mimo_B2 item 2 R52 c8cc0df57aad3a91f65d8cf64a1e53ab; mimo_C item 1 R12 670a4e95a95fd4148de0b1fa2f5db289; mimo_C item 2 R07 5b2d1637ea37a88d58375f63a70e634a; mimo_C item 3 R30 dd2ffd6a178a29c438ba745db3d6e362; mimo_C item 4 R13 cacaa8ee869cf81aee7cbc5e93f34486; mimo_C item 5 R25 9d43fc63ac8a9a69d95c111d5ab82a19. The S93 rulings: X03 ca75c0085d1835cae3a2ca88ba1e9136; X04 b82f1d1c8dd2ac7c4a363c834d283f07; X05 74b825b2d3c40fdbf58442a7402a8e31; X06 aa9a21e9b55e2138f2b66a840470ca3c; X09 f92389a295496d37c00b530b0b6c61dd; X10 ae10f9be471c1e1546eab6197c15d088; X11 38c477ab95ba986fc16c8719e76c3188; X14 7db95a43415b4b09c95ded7a013fd78b; X17 d0dd8a27c934fa5c6255422826ca66d9; X18 2a440ee25b144a65e12484a3eeacdc36. (The S90 ruling "item 4 R24 - check script.py" was not opened.)

**Git commits used:** 12e73da, 587eebf, 99e9cd0, 3f7c3ab and 8816fcf (`git show <commit>:Semantics/tests/Revision 2 - change list, draft of 23 September.md`); `git log` on the change list and the file-13 drafts to find them. HEAD 81e7ac0.

## Sources skipped, and why

- `tests/Revision 2 - plan and test round, draft of 23 September.md` and `tests/Revision 2 - revision note, draft of 23 September.md`: not in this collector's list. The plan weighs the worklist items (its choices reach this file through the change list's decisions D1-D11 and entries); the revision note is generated from the change list by program.
- `tests/Revision 2 - hard to vary restated through rivals and problems, 25 September.md` and its scripts, and the two S91 analyses (`… error correction and grading …`, `… does correction stick …`): the draft-4 pass and the analyses before it. Their proposals (the first "Rivals" wording, which both attacks refuted before draft 4 was committed; option (b), a record of "absorbed failures"; the Pres lemma) are in no committed change list and were not collected here.
- `results/S93 Cross-examination - draft 4 - returns/`: not opened; the tabulation copies every proposed wording "exactly from the response file".
- The S90 reply files' reasoning and attempt files, and the failed single S90 call to Atria (it "supports nothing"): not opened.
- S87, S88 and S89 returns and readings (collector B); S95 and later (the scrub, the repairs, S97).
- `tests/working files/revision2/` (copies of the original worklist and plan) and `tests/Revision 2 - S93 rulings applied - scripts/`: not needed; the committed worklist and change list were used.
- `plain words/` files 92 and 93: renderings of the theory, not changes to it.

## What could not be recovered

- **The change list's wordings before its two adversarial checks** (19 entries fixed, W26.1 dropped, W35.4 added): the entry files and the checks are only in the session scratchpad of 23 September, not in the repository (log S93). The table "What the checks changed" describes each fix but gives no earlier wording in full; nothing was recorded from it.
- **W26.1** as drafted: recorded from the worklist's W26 and the change list's "Dropped: 1 entry" (C-199).
- **The R51 task-(d) ruling file** is missing (batch 1 and 2 say so); it was a KEEP with no wording, so nothing is lost for this file.
- **Proposals given only as descriptions** (25 records): the letter G, the moves of R08, blindness in Part IV's Selected, R39's folding, the S93 findings for later entries, and others; "new" says so.
- **Placement of four additions** (the R55 bijection clause, the R03 gloss, Mimo's "For that assessor", and L524's closing words): the sources give the words but not the exact place, so new_sentence is left empty and target_line comes from an anchor.

## Notes for the ledger

- target_text differs by source: the change-list records are written against file 11 (line = file-11 line); the ruling and reply records against file 13 draft 2 (S90) or draft 4 (S93), with that draft's line; note records have no line. The part names are those of the target text.
- The meta entries W1.1, W38.1 and W1.2 are cut from every theory text; their applied_in names the full drafts' meta blocks.
- Kind and declaration changes of the entries (for example W6.3 WORDING to CLAIM, W37.1's fallback line) are not recorded except where a declaration was the only edit.
- `collector C.jsonl` as written by `step3_finish.py`: 209 lines, md5 15d79f11570f3269d57e50182604bfa0.
