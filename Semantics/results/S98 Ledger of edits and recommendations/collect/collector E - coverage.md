# Collector E - coverage

*Written by collector E for log S98, 26 September 2026. Stretch: recommendations of new wording for the semantics that sit in the records and were never applied (the owner's statement on choosing and its S94 working files; the S93 findings for later entries; the three analyses of 24 and 25 September; the S95 and S96 results files' open points; the plain-words files 93 to 97; file 12 where a record proposes a change to it). Also: decision S30 recorded, and the log number found. The ledger is not committed; only the decisions file was.*

## Decision S30 and the log number

- **Decision S30** is in `records/Semantics - Decisions.md`, after S29: a "[Claude's reading: …]" bracket, the context "Next step after log S97", the owner's words of 26 September 2026 in three paragraphs (the second in two lines), the date. Nothing else in the file changed. Commit **8fee0af** ("Semantics: decision S30 — line up every edit and recommendation by the part of the semantics it affects (verbatim)"), pushed to `claude/semantics-folder-work-9rtd5s`; HEAD equalled origin afterwards (8fee0af4cc3d441f7730a64386ff3f2e95008bb7). The key scan of `Semantics/` listed nothing before the commit.
- **Log number: S98.** After `git fetch --all`, the story logs of every project on this branch and on the six remote branches (`hv-skill-scope-kl0oyr`, `hv-skill-scope-kl0oyr-oz6b4c`, `main-branch-cleanup-is0h1f`, `semantics-folder-work-9rtd5s`, `session-continuation-6gktfz`, `main`) were searched for entry numbers. The highest in the shared sequence is S97 (Semantics, this branch); Language reaches L86, HV Skill 69 (on the hv-skill-scope branches), Planning 3, Workflow 11. No entry numbered 98 or above exists on any branch.

## Output

- `collector E.jsonl` — **58 records**, one JSON object per line, the 16 fields in the given order. md5 **d41c763264297b8aa0dc7f56a185f8a1**.
- `collector E - scripts/` — `lib.py` (texts with their md5s, headings, sentence bounds, extraction), `build_E.py` (writes the ledger; refuses to overwrite a non-empty ledger unless given `--force`), `check_E.py` (the checks below). Rebuild: `PYTHONDONTWRITEBYTECODE=1 python3 build_E.py --force`, then `python3 check_E.py`. A rebuild gives the same bytes.
- Every `new` with wording was taken from its source by program (a span between two markers, a quoted string after a marker, a fenced block of an entry, or a whole blockquote line) or typed and then matched against the source byte for byte. Where the source sets the wording as a Markdown blockquote, the `> ` markers were removed and nothing else (E-38, E-43, E-46, E-47, E-48, E-50, E-51). No reason is copied; `source_ref` points to the place and, where a later record carries the same proposal, names it.

## The records

| rids | round | source | what | status |
|---|---|---|---|---|
| E-1 – E-14 | S94 | `tests/Revision 2 - the owner's statement on choosing, against draft 5, 25 September.md`, section 8 | changes 1 to 6: change 1 (L317) and its declaration; change 2, removing Boundary (D), as three edits (L299, L301–L303, L526) and its declaration; change 3 (L317); change 4 (L429) and its declaration; change 5, two edits (L315); change 6, three edits (L315 twice, L526) | not applied 11; open for the owner 3 (change 6) |
| E-15 – E-16 | S94 | the same file, section 9 | reader B's clarification after L159's first sentence; reader A's L441 rewording | not applied 1; declined 1 |
| E-17 – E-21 | S94 | `tests/working files/S94 owner statement on choosing/reader A-text.md` | A3 (L317) and its optional Part 0 pointer (after L25); A4 (L441); A6 (L429); A10 (L317) | superseded 3; not applied 1; declined 1 |
| E-22 – E-26 | S94 | `…/reader B-scope.md` | B2 (L159); B3's two edits (L315) and its alternative sentence for Part IX after (K1); B8 (L517) | not applied 4; declined 1 |
| E-27 – E-32 | S94 | `…/reader C-choices.md` | C2's two edits (L315); C8's variant (L317); C6's three edits removing Boundary (D) | open for the owner 2; superseded 1; not applied 3 |
| E-33 – E-35 | S94 | `…/reader D-sources.md` | D4's sentence for the note's *Surprise and problems* line (change list L403); D14's rewording of the *Hard to vary* line and its conditional sentence (change list L399) | declined 1; not applied 2 |
| E-36 – E-37 | S93 | `tests/Revision 2 - change list, draft of 23 September.md`, "Carried forward after S93" (from rulings X03 and X18) | classes of components across candidates (draft 4 L119); the fallback of the note's *Surprise and problems* line (change list L435) | not applied 2, both "[no wording given]" |
| E-38 – E-42 | S91 | `tests/Revision 2 - error correction and grading, analysis of 24 September.md`, section 4 | option (b): the paragraph "Absorbed failure" (draft 3 L363) and three pointer sentences (L159, L313, L277); option (c), grading from Pres ("[no wording given]") | declined 5 |
| E-43 – E-45 | S91 | `tests/working files/errcorr/03 synthesis.md` | option (b) before its check: the paragraph and two pointers | superseded 3 |
| E-46 – E-48 | S91 | `tests/Revision 2 - does correction stick, …, analysis of 24 September.md`, section 2 | the checked wording: (a) the edit in draft 3 L313, (b) the paragraph "Witness in a common family", (c) the pointer at L363 | declined 3 |
| E-49 – E-52 | S91 | the same file, Appendix C (working file 03, the proposal before the attacks) | (a) two replacements in L313, (b) the paragraph "Correction in a common family", (c) the pointer at L363 | superseded 4 |
| E-53 – E-56 | S91 | `tests/working files/rivals/01 entries.md` | the first-drafted NEW of W33.1, W59.1 (Rivals and Problems), W60.1 and W38.1 (the note), as they stood before the text and model attacks; W34.1's first draft is the same as its draft-4 form and is not recorded | superseded 4 |
| E-57 – E-58 | S91 | `tests/working files/rivals/02 models.md`, section 3 | the models' repairs 1 (example wording) and 4 ("[no wording given]") of the first-drafted rivals sentence | declined 2 |

## Counts

| kind | not applied | open for the owner | declined | superseded | applied | all |
|---|---|---|---|---|---|---|
| recommendation | 24 | 5 | 14 | 15 | 0 | 58 |
| edit | 0 | 0 | 0 | 0 | 0 | 0 |

By round: S94 35, S91 21, S93 2. By scope: sentence 30, span 15, paragraph 12, whole text 1. "[no wording given]": 4 (E-36, E-37, E-42, E-58). Records whose `same_as` names another record: 10, all inside this file (a reader's wording that the statement file repeats, or the S91 pointer sentence that stayed the same between the working file and the analysis).

**How the statuses were set.** *not applied*: proposed and never entered, and not turned down in a record. *open for the owner*: the source makes the wording wait on an answer of the owner's that has not been given (change 6, the second choice of file 93). *declined*: a record or the owner's words turn the wording down (the statement file's "Not proposed" items and dropped A4; option (b) and the Pres lemma under decision S20; the models' repairs "not used"). *superseded*: a later record carries the same proposal in other words (named in `source_ref`). Change 5 is *not applied*, not *open*: the words it edits ("of the test that yields it") are no longer in the latest text.

## Target texts and places

- The statement file and the S94 readers write against **file 13 draft 5** (md5 7f1d8ad0…); `target_line` is draft 5's line, which is also the line in the scrubbed copy, the repaired copy and the latest text (all 632 lines, line for line).
- The note of sources and departures is not in the theory text: reader D's lines are the **change list's** (entry W38.1, lines 399 and 403 of the change list as it stands, md5 c6d25ec1…, unchanged since commit 8816fcf).
- The three **declarations** (E-2, E-6, E-9) are written, as collector C writes them, against "the note of file 13, its list of changes of claim", with no line; `target_part` names the change and its draft-5 line.
- The two S91 analyses write against **file 13 draft 3** (md5 403c4f2f…), whose lines match every line they cite. The rivals working files write against **file 11** (each entry's FILE-11 LINE); their OLD blocks match change list draft 4 (commit 3f7c3ab) and file 11.
- `target_part` is "Part / section / bold paragraph label" in force at the line, so "Rivals" (L315) and "Problems" (L317) of Part VI are told apart.
- For an insertion, `old` and `old_sentence` are empty and `source_ref` quotes the sentence the new words follow. `new_sentence` is the new words where they are whole sentences; for E-41 (a clause added to a sentence) it is the whole resulting sentence.

## Checks run by program (`check_E.py`)

1. Shape: 58 records, all 16 fields in order, no rid twice, every `same_as` names an existing record.
2. **Every `old` found verbatim in its target text:** 23 records have an `old`; **0 misses**. No record of this collector is "applied", so none of the 23 is an applied edit; the check was run on all of them.
3. Every `old_sentence` found verbatim in its target text: 24 checked, 0 misses.
4. The new wording of every record with wording was looked for in the latest text, the repaired copy and the scrubbed copy, whole and as the words it adds to its `old` (12 characters or more): **no hit**. No record in collectors A to D has the same `new`. So no `same_as` to an applied edit was set. Two later edits come near in substance, in other words, and are left to the lining up by line: the latest text's L317 says an answer ruled out "stays ruled out on \(p\) for as long as the argument stays usable (Part VIII)" (compare change 3, E-7, and A10, E-21), and the latest L159 and L317 speak of non-physical targets and of ruling out by examining a candidate (compare E-15, E-22 and change 5, E-10, E-11).
5. Every `new` with wording found verbatim in its source file (after removing blockquote markers where the source quotes it): 0 misses.
6. Collector C's record of file 12's pole-sentence slip (C-178) was also matched: its `old` and `old_sentence` are on line 325 of file 12, once.

## Sources read

| md5 or commit | source | read |
|---|---|---|
| fb95db9bda64146cbf72faa09dd670b9 | tests/Revision 2 - the owner's statement on choosing, against draft 5, 25 September.md | sections 0, 5–11 |
| 46c723438445321e21a343484da8c76f | tests/working files/S94 owner statement on choosing/reader A-text.md | every "Proposed change" and its finding |
| 91f5bdb1f0727499c346a6245c5823c5 | …/reader B-scope.md | section 2.7, findings B2, B8, the rest searched |
| 4a44611f25ba90e82f588714a75b77ca | …/reader C-choices.md | sections 1.2, 2.6, 3.1–3.8, the findings table |
| 429b2cb967ec75f8db22f5f96c2f3da2 | …/reader D-sources.md | findings D4, D14, the rest searched |
| c6d25ec1ccc3ea3e72136a75a794be62 | tests/Revision 2 - change list, draft of 23 September.md | "Carried forward after S93"; lines 399, 403, 435 |
| commit 3f7c3ab (md5 b6b2ea95ea9e21ebea3316d8e9fa4b40) | the change list as at draft 4 | entries W33.1, W34.1, W38.1, W59.1, W60.1, by program |
| 2f3551b8017c9e6e0de6c575a42f9c8d | results/S93 Reading of the replies.md | section 10 |
| ca75c0085d1835cae3a2ca88ba1e9136, b82f1d1c8dd2ac7c4a363c834d283f07, 74b825b2d3c40fdbf58442a7402a8e31, aa9a21e9b55e2138f2b66a840470ca3c, d0dd8a27c934fa5c6255422826ca66d9 | results/S93 reading rulings/ X03, X04, X05, X06, X17 | "Findings for later entries" |
| 38c477ab95ba986fc16c8719e76c3188 | results/S93 reading rulings/ruling S93 X11 proposed.md | point 6 (file 12), searched |
| d9f439d0d4f58972e5f4ae08b378829a | tests/Revision 2 - error correction and grading, analysis of 24 September.md | sections 4–5; the appendices searched |
| 1b9af415cd04ce3c5a9f9915551804a2 | tests/working files/errcorr/03 synthesis.md | section 4 |
| 0f4d8e6f0b34bf358e03c995c25a3f13 | tests/Revision 2 - does correction stick, …, analysis of 24 September.md | section 0 head, section 2, Appendix C section 2; Appendices D and E searched |
| 265e9c7cdb9d7d0955fe6c7a920fc727 | tests/Revision 2 - hard to vary restated through rivals and problems, 25 September.md | sections 1, 3, 5, 6 |
| be52829942b4761818d049fa7d4375b2 | tests/working files/rivals/01 entries.md | the five entries, by program |
| 72ad3c29c33505eb48ef525d43612bfa | tests/working files/rivals/02 models.md | section 3 |
| 3ad4571e10b394098750e828becfbc89 | tests/working files/README.md | what each working folder holds |
| 82ee665fbb7db748522df644c1f38d0c | results/S96 The scrubbed copy repaired - physical possibility, conflict by argument, premises taken as given.md | sections 6, 9, 10 |
| 5bbb207285cb2f3a6a252a3e2d2aef23 | results/S95 Does the semantics hold without verificationist words.md | sections 10–13 |
| f0bcc486…, e8fd1ddd…, 0ba87fb6…, e655024f…, 7b68e18e… | plain words/93, 94, 95, 96, 97 | searched for proposed wording |
| 5e494c1095d920d128b9a79de378f923, 403c4f2fb3e5d57bb48a5647011c9f91, fc55b470c63cd4b3c27d6aa64d8d8c17, 7f1d8ad02adf96e27622593bd263252e, 2517ef4ec1f274e8de2bfb7e6661ef94, 8bb4d19d5aad53de2492b2193fd23ff1, ebca15a047f686b15d5f5766b69825c9, ce7e8e2c5f89d982fa888c19587d508b | file 11, draft 3, draft 4, draft 5, the scrubbed copy, the repaired copy, the latest text, file 12 | the target lines, by program |
| records/Semantics - Decisions.md (before: d3a6b746b7c15c2527bd2cea65122c07) | the decisions file | S20–S29, to write S30 |
| collector A to D ledgers and coverage notes (as on disk at 11:12 UTC) | results/S98 …/collect/ | to avoid holding the same record twice |

## Held by collector C, not recorded again

The S93 findings for later entries that collector C already records from the same rulings: L245 and L558 against (F1) (C-152, C-154, C-179); port translations and values (C-180); (K2)'s undefined terms (C-181); receipts, (K2), (K3) and L598 (C-182); "conflict" in two senses (C-183); \(O_{\mathrm{ep}}\) and "resource contract" (C-184); \(\mathcal V\) (C-185); L524 and \(\mathcal N\), with Mimo's words (C-177); the *Reach* pointer "(Parts I, V and VI)" (C-174); the first choice's six proposals (C-156 to C-161); and **file 12's pole-sentence slip at its L325** (C-178, "but not the calculation's \(H\)" to "… \(L\)"), the only change to file 12 that any record proposes (the change list, the S93 reading and ruling X11 were searched).

## Sources skipped, or read and not recorded, and why

- **S93 items that propose no change:** "Test" and "does no work" unplaced (their bases are placed); L325's "\(L\) is an output" ("noted only"); "(RC), (U1)–(U3) depend on all of the above" ("recorded here only"); Derivation 10's obligation (about a reply's quotation, not the text); where a corrected mistake can come back (the ruling claims nothing there); the *Elimination* line's missing "its own target" ("its substance right", "not a challenge"); ruling X04's second finding, which is wording for an entry's REASON field, not for the theory; the owner's questions (c1) and the losses (d) of "Carried forward after S93", which name no change (change 6, E-12 to E-14, is the wording for the second choice).
- **Plain-words files 93 to 97:** they render proposals in plain words (file 94, section 4, gives change 1 that way) or quote applied edits (file 95); none gives theory wording not held in the records above or by collector D.
- **results/S96 The scrubbed copy repaired …, sections 6 and 10**, and **results/S95 Does the semantics hold …, sections 10–13:** the items not applied and the open questions are those collector D records from the stage-2 file, the Check files and the S95 sections 7–9 (D-718 onward, D-842 onward, D-873); no further wording.
- **The attacks on the correction-sticks proposal (Appendices D and E) and on the rivals entries (working files 03a, 03b):** their fixes are carried in the checked wording (E-46 to E-48) and in the draft-4 entries (collector C); only the first drafts they changed are recorded here.
- **The error-correction analysis's Appendices A and B** (the theory map and the source reading): no proposed wording.
- **Reader D's note on found criteria of a problem** ("none now … to be drafted and checked separately") and reader A's and C's questions for the owner: no wording for the theory.
- **Working files errcorr/04 (the checked answer, the analysis's body), ratchet/ (the analysis's appendices, byte for byte), rivals/ builds and splices:** the same words as the committed analyses or the change list.
- Not opened: `cross_examiner_keys.env`; any reply's reasoning file.

## What could not be recovered, or is given only as a description

- **Four records have no wording** (E-36, E-37, E-42, E-58): the sources describe the change and give no words.
- **The earliest wording of option (b)** is as working file 03 has it (E-43 to E-45); anything before 03 is not in the repository.
- **E-57** (the models' repair 1) is written against a sentence of the first-drafted W59.1, which never stood in a theory text; its `target_line` is file 11's L317 (where W59.1 was to go) and `old` is empty.
- **E-18** (reader A's Part 0 pointer) and **E-26** (reader B's sentence at L517) give no anchor beyond "after L25" and "after the description of the physical module"; the words are placed at the end of those lines.
