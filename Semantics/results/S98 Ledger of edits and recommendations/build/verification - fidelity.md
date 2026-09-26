# S98 — The ledger checked: fidelity

*Log S98, 26 September 2026. Written by a checker that built none of the ledger, after an earlier checker was lost in a restart (its partial file had found nothing yet). Every check below was run by program from the scratchpad (`verify/place.py`, `views.py`, `wording_in_views.py`, `src.py`, `applied.py`, `applied2.py`, `lists.py`, `sample.py`, `loc.py`, `eye.py`, `reasons.py`). The looks by eye are named as such. Nothing in the ledger, the collectors' files or any text was changed. Nothing is committed.*

Inputs read: `collect/collector A.jsonl` … `collector E.jsonl`, `group/anchored.jsonl`, `line-up/data/records.jsonl`, the specification `group/grouping and structure, chosen.md` (§3–§6, §8), its placement inputs (`sentence index of the latest text.jsonl`, `proposal by place - scripts/sections.json` and `assignment.jsonl`), the sixteen group files, and each record's `source_file` and target text. The stage-1 text of S96, which is not on disk, was rebuilt here from the scrubbed copy and `tests/S96 Repair - scripts/replacements.json`; its md5 is c1eecbd1587e5aec91fd0ba7d46e1469, the md5 the S96 scripts ask for. The earlier versions of the change list were read from git (12e73da, 587eebf, 99e9cd0, 3f7c3ab, with 8816fcf on disk).

## 1. Counts: every collected record appears once

| check | result |
| --- | --- |
| records in the five collector files | 1850 (A 321, B 310, C 209, D 952, E 58); no rid twice |
| records in `anchored.jsonl` and in `line-up/data/records.jsonl` | 1850 each; no rid lost, added or repeated |
| the 16 collected fields (rid … same_as), collector file against ledger | equal byte for byte for all 1850 records; nothing was edited on the way |
| changes (`change_id`) | 1275; each record's `change_members` is exactly the set of records with its `change_id` |
| `same_as` naming a rid | every such pair lies inside one change (0 pairs split over two changes) |
| `same_as` naming a file entry, not a rid | 143 ids on 100 records: change list 65, revision note 42, worklist 30, plan 6. This matches the builder's note 2 (the specification's "78" counts only the last three kinds) |
| showings in the group files, counted by rid | each `full` and `block` record shown in full once, each `vocabulary only` record once (in G16), each `term line` record once per sentence it touches (plus once in G16 when its change is there): 2569 showings, 1850 of 1850 records as expected |
| pointer lines | 249 in G01–G15 and 1 in G16, as the specification's table says |
| wording shown under each showing, against the record's four fields by the rule of §8.1 (Before, After, Old wording, New wording) | 2569 of 2569 equal byte for byte, "same wording" buckets included |

Duplicates: no record is dropped as a duplicate. Records of one change are kept as separate records under one change entry, each with its own `source_ref`, and records with the same four wording fields share one wording block ("Records X, Y (same wording)"). So every source reference survives.

## 2. Wording, sampled against the sources

### 2.1 All 1850 records, by program

| check | misses |
| --- | --- |
| `new` (not a description) found byte for byte in its `source_file` (with the blockquote marker `> ` removed, table `\|` read as `\|`, JSON strings decoded, and the four earlier git versions for the change list) | 10: B-264, B-267, B-276, B-280, B-285, B-289, C-145, C-154, C-170, D-621 (see §5, items 3–5) |
| `old` found in its target text (file 10, 11, 12, draft 2–5, scrubbed copy, stage-1 text, repaired copy) | 1 outside the vocabulary rows: D-736 (§5, item 6). The 213 vocabulary-row records (D-492 … D-717, scope `term`) name words in a description, as collector D's coverage says, and are not wording to find |
| `old_sentence` found in its target text | 0 misses |
| `old` inside `old_sentence` | 0 misses |
| `new` inside `new_sentence` | 79 misses: A-164 … A-237 (74 Stage B phrase cells, whose `new` is the underlined cell and whose `new_sentence` is the R2 sentence; by collector A's design) and B-264, B-267, B-276, B-280, B-285 (§5, item 3) |

### 2.2 The sample: 86 records at their `source_ref`

Drawn by program (`sample.py`, seeds 98 and 981): one record from every group × collector cell that has one, topped up so that each collector has at least 14 and the S96 stage-2 and stage-3 edits, the replies and G16 are all in. By collector: A 14, B 15, C 15, D 28, E 14. By group: every group G01–G16 (G16 holds only D records; 5 are in the sample).

A-2, A-13, A-48, A-86, A-109, A-158, A-164, A-188, A-208, A-249, A-275, A-300, A-305, A-308; B-6, B-30, B-32, B-45, B-62, B-75, B-86, B-118, B-124, B-129, B-150, B-234, B-251, B-272, B-289; C-12, C-19, C-31, C-39, C-44, C-51, C-59, C-83, C-97, C-101, C-107, C-113, C-159, C-187, C-193; D-24, D-34, D-105, D-153, D-196, D-273, D-317, D-331, D-356, D-394, D-400, D-407, D-412, D-471, D-475, D-516, D-538, D-541, D-563, D-585, D-659, D-672, D-717, D-744, D-885, D-893, D-898, D-950; E-14, E-15, E-17, E-19, E-20, E-25, E-29, E-35, E-36, E-39, E-41, E-52, E-54, E-56.

How each was checked:

- **The 16 D edits from the replacement files:** the JSON entry that `source_ref` names (`entries[i]`) has `old` and `new` equal to the record's, byte for byte: 16 of 16.
- **The 11 B edits (file 10 → file 11):** `old_sentence` stands on the file-10 line and `new_sentence` on the file-11 line that `source_ref` names: 11 of 11 (B-62 is a removal, B-86, B-118 and B-124 additions).
- **Records whose `source_ref` gives a source line or table row** (A, D vocabulary rows, B-272): the wording stands at that line: 26 of 26.
- **Change-list entries (C-12, C-19, C-31, C-39, C-44, C-51, C-83):** the wording stands inside the `###` entry that `source_ref` names (by the nearest heading above the hit), in the version named: 7 of 7.
- **The rest** (rulings, replies, tabulation, working files, analyses): the label above each hit was read by eye (`eye.py`) and is the item that `source_ref` names (for example "X09.18 · Mimo · B", "**F10 · Q5 · L526.**", "**(c) Optional pointer, end of D3:L363.**", "Proposed change" under reader A's A3): all.
- **Six descriptions** (B-234, B-251, C-59, C-187, D-893, E-36) carry no wording to find; read by eye for reasons (§4).
- **One miss:** B-289, whose `new` is built (§5, item 3).

### 2.3 Applied edits against the text that carries them

For every record with status `applied` and a wording (1198 checks over the texts `applied_in` names; vocabulary rows, descriptions and deletions left out), `new_sentence` (or `new`) was looked for in each named text.

- **Found as named:** all of A's (which say "in other wording"), all 182 of B's file-11 edits, the S95 edits in the scrubbed copy (300 of 300), the S96 stage-2 edits in the repaired copy (28 of 28), and the stage-3 edits in the latest text (85 of 85).
- **Not found as named:** the two classes of §5, items 1 and 2, and four small cases of built sentences (§5, item 7).

## 3. Placement against the specification's rule

The rule of §3, §4.1 and §4.2 was written again from the specification alone (`place.py`) and run on the inputs. It was then compared with the ledger's `lineup_change_group`, `lineup_display`, `lineup_home_sentence`, `lineup_pointer_sentences`, `lineup_term_sentences`, `lineup_group` and `lineup_section` for all 1850 records.

- **Units per group:** 46, 66, 56, 98, 68, 67, 48, 27, 51, 80, 27, 35, 14, 55, 18, as §3 says.
- **Changes per group:** 86, 52, 74, 118, 153, 143, 42, 37, 65, 105, 77, 50, 22, 116, 89 and 46, as §4.1 says.
- **Showings per group, recomputed:** display `full`, pointer lines, vocabulary lines and blocks all equal §4.2's table. The totals are 1309 full, 249 + 1 pointer lines, 863 vocabulary lines from 224 records, 309 in blocks and 8 vocabulary only.
- **Records placed differently from the rule:** none.
- **Rest-block ids:** the only differences are the `lineup_section` values of the 213 rest-block records (`rest-<Part key>` where the rule gives no section). Ten of them (B-1 … B-5, B-305, E-33, E-34, E-35, E-37) are filed under `rest-OUT`, the Part key of their place entry's `section`, while its `group` names `FM`. §5 lists `OUT` as a rest-block key, so this follows the specification.
- **Sections of full records:** every `full` record's section is its home sentence's section.
- **`term line` records:** as in the builder's note 3, they carry their change's section, or none when the change is in G16.

## 4. Reasons copied into wording fields

**The four wording fields.** `old`, `new`, `old_sentence` and `new_sentence` were scanned for "because", "reason(s)", "so that", "since", "in order to", "to avoid" and "why" (`reasons.py`), 323 hits in all:

- 198 hits are in wording that stands verbatim in a theory text (file 00, 10, 11, 12, the drafts, the scrubbed, stage-1, repaired or latest text), or whose context around the word does.
- The other 125 were read by eye. All are the proposed theory wording itself, for example:
  - R2's sentences ("merely because …", "reason use");
  - the note of sources and departures ("the reason it is made (erratum, clarification or change of claim)"; "a myth easy to vary because …");
  - the replies' proposed sentences ("since (N) tests each \(d\) against \(c\) separately");
  - the vocabulary cells.
- None is a reason for making the change, with two exceptions:
  - **A-164, A-177, A-180, A-188, A-191, A-205, A-210, A-214** (Stage B phrase cells): each `new` holds one or two underlined phrases taken from R2's "Expected benefit … Risk" paragraphs. Those paragraphs are why R2 proposed its amendments, and collector A skipped them for that cause. The phrases:
    - "share a working kind", "an irrelevant alteration elsewhere" (A-164);
    - "a substantive account of content use" (A-177);
    - "deliberate first construction" (A-180);
    - "complete grounding of representation" (A-188);
    - "genuinely redundant routes" (A-191);
    - "a useful question" (A-205);
    - "the normative problem" (A-210);
    - "explanation-based leak repair" (A-214).

    `source_ref` says so ("part of the cell is in R2 reason text"). Each phrase is two to five words, and none is shown as theory wording elsewhere.
  - **C-181** (a description): "[no wording given] define (K2)'s Lic_j, Scope_j and Live_j (L390 only), so that Derivation 6 can be followed through receipts to the primitives". The clause after "so that" says what the change is for.

**The 137 descriptions.** These are the `new` values that begin "[no wording given]": B 101, C 25, D 5, E 4, A 2. They were scanned more widely (for "would", "must", "should", "needs", "fails", "undefined", "unclear" and similar) and the 33 hits read by eye.

- Apart from C-181, they say what the change is, not why.
- B-191 … B-213 (23 records) all read "unclear wording or tension, recorded for a later revision". That names the kind of item, not the change, but it gives no reason either.
- C-180 ("which governs 'footprint bijection' at L119 (twice) and L564") and D-893 ("… and must change with them") are pointers to the places the change touches, not reasons.

**`source_ref`, `applied_in` and `target_part`.** These were scanned the same way. `applied_in` has no hits. In `source_ref` and `target_part`, the only hits are:

- headings of the texts ("Why there is no anchoring condition");
- R2's amendment titles ("Work and reason use keep their match-up");
- the label "reasons-FOR form" (D-758 … D-760);
- "so that '**Finite monotone theorem.**' (L305) follows the paragraph" (E-4), which says where the deletion leaves the text.

## 5. Problems, by rid

1. **Stage-1 edits named as carried by the repaired copy, whose words stage 2 changed again.** D-301, D-302, D-307, D-309, D-312, D-316, D-322, D-326, D-327, D-328, D-354, D-362, D-365, D-368, D-378 (15). Their `applied_in` is "repaired copy", but their `new` stands only in the stage-1 text (rebuilt in memory, not on disk). The repaired copy carries stage 2's later wording at those places. For D-314 and D-317 the span stands in the repaired copy and the whole sentence does not.
2. **Recommendations with status `applied` whose own words are not verbatim in the text `applied_in` names.** Collector D counts a proposal as applied when an S96 entry names it or a ruling took it "as proposed or near it". The words used often differ: markup added, an ellipsis filled in, a clause changed.
   - 69 in the repaired copy: D-718, D-719, D-721 … D-725, D-728 … D-735, D-737, D-738, D-740, D-741, D-744, D-745, D-747, D-748, D-750, D-752 … D-756, D-758, D-760, D-771, D-774, D-779, D-782, D-793, D-795, D-797, D-800 … D-804, D-809, D-813, D-816 … D-820, D-822 … D-824, D-828 … D-830, D-833, D-838, D-847, D-848, D-850 … D-852, D-854, D-857, D-860, D-870 … D-872.
   - 18 in the latest text: D-876, D-883, D-885, D-892, D-916, D-920 … D-922, D-924, D-930, D-931, D-935, D-943, D-944, D-947, D-949, D-950, D-952.

   All 87 have `new_in_latest` = "no", so each record line in the views says "wording not in the latest text". A reader is told that the words differ, but the status alone reads as if they stand. Collector A marks the same situation "applied … in other wording"; collector D does not.
3. **`new` built from the old words plus the source's added words, not copied as one piece.**
   - B-264, B-267, B-276, B-280 and B-285 are insertions. For each, `new` is the old sentence followed by the added sentence, and `new_sentence` holds only the added sentence, so the view's "After" shows the added sentence alone.
   - B-289: `new` is "with the named background fixed" (the old words) followed by the source's ending "; the commitments of \(E|W\) are \(W\), and \((E|W)|W'=E|W'\) for \(W'\subseteq W\)."

   In every one of the six, the source's own words are verbatim inside `new`.
4. **`new` built from a word the source offers.**
   - C-154: the source gives `each active component`, and `new` is "each active component must anchor".
   - C-170: the source gives `the result` for "the exclusion", and `new` is "the result ceases to be established".

   The source's words are verbatim inside `new`, and `source_ref` says what was offered.
5. **Small differences from the source.**
   - C-145: `new` ends with a full stop that the source's quoted wording does not hold. The source has `could read "Here selection has no represented target in its history (Parts 0 and IV)".`, with the stop outside the quotation marks.
   - D-621: a bracketed clause giving a reason was cut from the table cell. Collector D's coverage names this and 16 more cells (D-541, D-544, D-555, D-598, D-599, D-601 … D-604, D-610, D-613 … D-616, D-619, D-682). Only D-621 fails the search for its `new` in the source. In the other 16 the remaining words are still found as one piece.
6. **`old` not verbatim in its target text.** D-736: "Here a route of the candidate is a member of S" is written without the text's markup (`\(\mathsf S\)`). D-798, the same proposal from the other S95 reading, has the markup and is found. Collector D's coverage says so.
7. **`new_sentence` built on file 11 alone.** C-42 (entry W13.2 + W12.2): `new_sentence` keeps "the system's own today whoever wrote it", but the drafts read "the system's own whoever wrote it", so the sentence stands in no text. C-22, C-32 and C-63 have their `new` in the scrubbed, repaired and latest texts, and their `new_sentence` only in the drafts, because the scrub changed other words of the sentence. For these three this is as it should be, since `applied_in` is set by `new`.
8. **Reason phrases in wording fields.** A-164, A-177, A-180, A-188, A-191, A-205, A-210, A-214 (the R2 reason phrases of §4) and C-181 (the "so that" clause of §4).
9. **Same change, not joined.** B's records point at worklist items by file pointer, and collector C records the same worklist items. Six such pairs are shown as separate changes, each pair in one group:
   - B-208 and C-200 (W27, G15);
   - B-294 and C-203 (W33, G06);
   - B-296 and C-204 (W34, G06);
   - B-302 and C-207 (W44, G03);
   - B-303 and C-205 (W39, G05);
   - B-306 and C-206 (W41, G10).

   B-186 and B-188 point at W6, which C records as C-191 and C-192 (G14), but they are errata on other places and may not be the same change.
10. **"linked (not joined)" on changes that are joined.** The specification's rule marks every file pointer as "not joined". But all 65 pointers into the change list point at entries whose collector C record is already in the same change, through C's own links: 59 directly, and 6 by compound entry ids such as "W57.1 + W32(b).1". The label holds of the pointer and misleads about the change.

11. **Status `applied` where the source records part of the proposal as not applied.** D-857 (the S96 whole-text check's B-2): its `new` includes "of the first kind where the pair is in \(C\) and of the second where it is not". Stage 2's `not_applied` list (`tests/S96 Repair - scripts/replacements_stage2.json`) names exactly that clause as not applied, and it is not in the repaired copy. The record's status is "applied" with no word of the part left out. D-849 and D-850 show the right way to record such a case: W P-1's first part, declined, and its second part, applied.

No problem was found in the counts, the joins by rid, the placement, or the wording shown in the views against the record fields. The order of entries within the views was not checked here.
