# S98 — Fixes after the two checks

*Log S98, 26 September 2026. Written by the finishing agent, after the two checks in this folder (`verification - fidelity.md`, `verification - completeness.md`), which stay as they were written: their figures are for the ledger as first built. The corrections and additions below were made by the scripts in `finishing fixes - scripts/`, and the whole chain was then rerun (last section).*

## In figures

| | first built | after the fixes |
|---|---|---|
| records | 1850 | 1894 (44 added, `collect/collector F.jsonl`) |
| changes | 1275 | 1293 (24 new; 20 of the added records joined changes already there; 6 pairs joined, which retires CH-0572 and CH-0575 to CH-0579) |
| records corrected in collectors A to D | — | 133 (165 fields) |
| records in full under their home sentence | 1309 | 1346 |
| pointer lines in G01–G15 | 249 | 284 |
| vocabulary lines (records) | 863 (224) | 896 (229) |
| records in blocks | 309 | 309 |
| G16 records in full | 88 | 92 |
| rows of `by sentence.csv` | 2819 | 2928 |

## Corrected (the fidelity check, section 5)

1. **Stage-1 edits of S96 that stage 2 rewrote** (D-301, D-302, D-307, D-309, D-312, D-316, D-322, D-326, D-327, D-328, D-354, D-362, D-365, D-368, D-378): status `superseded`; carried by "stage-1 text of S96 (rebuilt in memory, not kept); stage 2 rewrote it before the repaired copy".
2. **Recommendations taken in other words** (the 86 listed in the check, other than D-857): "carried by" now reads "repaired copy, in other wording" (68) or "latest text, in other wording" (18), the form collector A already used.
3. **D-857**, taken in part: carried by "repaired copy, in part and in other wording; not applied:" and the clause stage 2 names.
4. **Additions written as old plus new** (B-264, B-267, B-276, B-280, B-285): `new` is now the added sentence alone, as the source gives it, and `old` is empty; `old_sentence` still names the sentence it follows. B-289: `old` is the full stop the source's new ending replaces, and `new` is that ending.
5. **Words the source offers** (C-154, C-170): `old` and `new` are now just the words replaced and the words offered.
6. **C-145**: the full stop that stands outside the source's quotation marks is gone from `old` and `new`.
7. **D-736**: `old` now has the text's markup, as D-798 has it, and is found in the scrubbed copy.
8. **Phrases from R2's reason paragraphs** are gone from A-164, A-177, A-180, A-188, A-191, A-205, A-210 and A-214; each `source_ref` says they were left out. C-181's "so that" clause is gone.
9. **Six pairs of one change** (B-208 and C-200, B-294 and C-203, B-296 and C-204, B-302 and C-207, B-303 and C-205, B-306 and C-206): each record names the other in `same_as`, so each pair is one change.
10. **"linked (not joined)"**: a pointer to a change-list entry whose record is already in the same change now reads "joined through the change-list entry"; no change-list pointer is left under "linked (not joined)".

## Added (the completeness check, section 1): collector F

- **F-1 to F-17**: the change list's fixes before draft 1, one record per row of "Fixed: 19 entries" that touches wording (8 with the wording the row quotes, 9 as descriptions); each is joined to its entry's change through a change-list pointer.
- **F-18, F-19**: Mimo's own S3 and its sentences for line 246 (S88, F3), declined. **F-20**: Mimo's own "Approximate transport" (S88, F2), superseded by the settled wording.
- **F-21 to F-35**: the revision 2 plan's own "Take" wordings (W7, W11, W22, W33, W35 (b′), W41, W57, W58) and its F3 rider (plan lines 204 and 205). Where the plan's words stand in no later text, the status is `superseded`, carried by the change list's entries for the item.
- **F-36 to F-38**: worklist items W49, W50 and W2, which the plan left out; `declined`, as collector C records W47 and W48.
- **F-39 to F-42**: the S95 sceptic's rows for "unsettled", line 43's objectivity sentences, "verdict" and "credit". Three are joined to the as-used records of the same word (D-517, D-516, D-564).
- **F-43, F-44**: one whole-text record each for file 10 made from file 00, and file 12 made from file 11.
- **The two index pages** now say what the ledger does not hold (`../line-up/index.md`, "What is not here"; `../00 Index.md`).

Every `new` with wording in collector F was found by program, byte for byte, in its source; every `old` against file 11 in file 11; and the status of every wording was set by searching drafts 1 to 5, the scrubbed copy, the repaired copy and the latest text.

## Left as it was

- **D-314, D-317**: the span stands in the repaired copy. The rest of the sentence carries a later stage-2 edit, which is its own record.
- **C-42**: its `new_sentence` applies this entry alone to file 11's sentence, as the record shape asks. The dropped "today" is entry W13.1, record C-41, shown beside it.
- **D-621, and the 16 cells collector D names**: the cut brackets give the grounds for the change, which the ledger leaves out by rule. The words kept are the source's, in their order.
- **B-186, B-188 against C-191, C-192 (W6)**: errata at other places; the check itself left open whether they are one change.
- **W37.1 and W58(ii).1**: these two fixes change only the expected ruling, no wording.
- **Sources the repository never held or holds only in part** (R2's amendments file, Stage B rows 1 to 32, file 20, the text of the S76 patch, the change list's working files of 23 September): no wording to take. The index says so.
- **Files 10 and 12, sentence by sentence**: each is a new text, not a revision of its predecessor line by line, and file 12 stands outside the chain that leads to the latest text; each has one whole-text record.

## How the chain was rerun

1. `finishing fixes - scripts/fix_collectors.py`: the corrections to collectors A to D. Each names the value it expects before; a second run changes nothing.
2. `finishing fixes - scripts/build_F.py`: writes `collect/collector F.jsonl`.
3. `group/anchor - scripts/step3_anchor.py` and `step4_check.py`, now reading collectors A to F (step 4 reports no faults). The change ids first made are kept (`change ids as first made.json`): a joined change keeps the lower id, and changes of new records only are CH-1276 to CH-1299. The target version `f00` (file 00) is added.
4. `group/proposal by place - scripts/place.py` (its `assignment.jsonl`, `sections.json` and `measures.json`; in `sections.json` only the joined-group label of "Indices, not imports" changed, which the builder does not read), and `group/proposal by idea - scripts/write_proposal.py` for its assignment file only; `proposal by idea.md` was put back as the grouping step wrote it. The pages of the anchor and grouping steps (`anchoring summary.md`, `proposal by place.md`, `proposal by idea.md`, `grouping and structure, chosen.md`) keep their figures for the 1850 records. The collectors' coverage notes likewise keep their own figures and md5s, for their files as they wrote them (commit 130ea45).
5. `line-up/scripts/build.py`, with the new input md5s, the rounds "file 10 (before log 25)" and "S77" and the target version `f00` added to the order, and the joined-entry label. `check.py` carries the new figures; the specification's figures stay in its comments.
6. `build/build_ledger.py`, which runs both and writes `00 Index.md`. All eight checks pass, and a second run gives the same bytes.

**What moved.** Of the 1850 records first built, 9 are shown differently: B-302 and C-200 now stand under sentences through their joined partners; B-289 and six stage-1 edits (D-301, D-307, D-309, D-312, D-328, D-378) stand under another sentence of the same line. One change moved group: CH-0365 (entry W12.1), from G10 to G12, with its added fix F-8. In the idea cross-index, nine changes with an added or joined record changed idea; for 13 changes with none, the "also" list changed, and for 6 the near-tie mark, because the idea proposal's shares are computed over all records.
