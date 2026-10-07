# S98 — The ledger checked: completeness

*Log S98, 26 September 2026. Written by a checker that built none of the ledger. An earlier checker was lost in a restart. Its partial file had reconciled the S95/S96 counts and found two gaps; both findings are kept below, re-checked by program, and marked where they were. The checks ran from the scratchpad. Nothing in the ledger, the collectors' files or any text was changed. Nothing is committed.*

**What was asked.** For each round of the project story's log (`records/Semantics - project story.md`, entries 24 to S97) and each file listed in `INDEX.md` that changed or proposed wording for the theory, does the ledger (`line-up/data/records.jsonl`, 1850 records) hold its changes? Where the round gives a count, is the count met, and do samples of three or more per round hold?

**How it was checked.**

- By program: every stated count below; every id that a source numbers (quotation rows, amendment rows, table rows, errata, worklist items, change-list entries at each of their five versions, ruling files, repair numbers, ruling heads); and every JSON replacement entry.
- By search: every file under `results/`, `tests/`, `plain words/` and `records/` that no record uses and no collector's coverage note names (84 such entries). Each was either placed as a pack, plan, rule or test file, or scanned for proposed wording.
- By eye: the passages each gap is found in.

## 1. Missing or under-counted: where to find each

1. **The change list's pre-draft-1 fixes (log S90).**
   - **Where:** `tests/Revision 2 - change list, draft of 23 September.md`, section "What the checks changed", table "Fixed: 19 entries" (file lines 111–133).
   - **What:** 19 fixes the two adversarial checks made before draft 1, and the addition of W35.4.
     - Two of the 19 change only the expected ruling (W37.1, W58(ii).1).
     - The other 17 change wording: W22.1, W22.2, W30.1, W39.1, W7.3, W57.1 + W32(b).1, W17.2, W12.1, W23.1, W36.1, W45.1, W35.2, W33.1, W40.1, W41.1, W1.1, W38.1.
     - Several give the old and new words, for example W36.1 "a separate matter", not "a separate measure"; W17.2 "candidate transports", not "realizable transports"; W45.1 "physical medium" in place of "kind of carrier".
   - **Held:** no record. The entries' wordings after the fixes are held (C-1 … C-67 and the earlier versions), and W35.4 itself is C-16. The fixes as changes are not, not even as "[no wording given]" descriptions. The entry wordings before the checks exist only in a session scratchpad of 23 September (collector C's coverage), so the table is the only source.
   - *(Found by the earlier checker; found again here.)*
2. **S88: the outside reader's own wordings.**
   - **Where:** `results/S88 Cross-examination - three defects - returns/Mimo in three parts/`.
   - **What:**
     - (a) `s88_xexam_mimo_F3.response.txt`: Mimo's own S3 ("S3 becomes: …") and its sentence for line 246 ("line 246 add: 'The commitments \(\Gamma\) are active components of \(E\); …'"). The final positions say "Mimo's own S3 wording is not adopted" (`results/S88 Reading of Mimo's reply in three parts, and the settled positions.md`, lines 310 and 402). This is a declined recommendation.
     - (b) `s88_xexam_mimo_F2.response.txt`, point 4 (file line 13): Mimo's own "**Approximate transport.** …" wording, with the side note moved into the sentence. The final F2 wording takes parts of it in other words (final positions, "Changes from the post-Atria position", points 1, 2 and 4).
   - **Held:** no record for either. Collector B read only the reading files and skipped the raw returns.
   - *(a was found by the earlier checker; b is new.)*
3. **The revision 2 plan's own wordings (log S90).**
   - **Where:** `tests/Revision 2 - plan and test round, draft of 23 September.md`. The plan's "Take" column gives wording, later superseded by the change-list entries in other words:
     - W7 (file line 97): L33 and L512 read "derived from these, the declared indices and the declared inputs";
     - W11 (line 101): at L271, "is not excluded by (F1), and is an account when it meets the other conditions of (E)";
     - W22 (line 112): the gloss of \(p_\delta\), "the question whether z has \(\delta\) in respect of p";
     - W33 (line 123): "(E) is fidelity: a commitment that does no work passes (E), …";
     - W35 (line 125): option (b′), with "recognized difficulty" defined as "a represented failure of a claimed obligation, or a represented conflict …";
     - W41 (line 131): the relay guard, "a witness may identify a binding by its use (reason use, Part IX); …";
     - W57 (line 143): "where the claim states the ground of its restriction, the verdict is given with that ground; …";
     - W58 (line 144): at L301, "the supports assessed are subsets of the written Γ, …", and at L33 s4, "is defined or presupposed (Derivation 6)";
     - the F3 option (line 204): replace "in \(E|(\Gamma\setminus G)\), with the named background fixed" with "in \(E\) with the components of \(G\) deleted (Part II: …)".
   - **Held:** none of these wordings is in any record's `new` or `new_sentence`. Collector C left the plan out ("its choices reach this file through the change list"), and collector B used six plan pointers, not its wording.
4. **Worklist items with no record (log S90).**
   - **Where:** `tests/Revision 2 - worklist, draft of 23 September.md`:
     - **W49** ("Absence and prevention constructions; attack B widened", from file 12; handling "New constructions for Part VII. Defer.");
     - **W50** ("What a failed intervention refutes (K3; 12:411)", handling "Clarification", with the proposition "An intervention whose prediction fails refutes the conjunction that includes 'the intervention realized the intended edit'");
     - **W2** ("Carry Derivation 3's qualification (only if file 10 stays the base)", moot on the file-11 base).
   - **Held:** no record names them. The plan defers W49 and W50 ("W47, W48 (beyond defining ProducedBy), W49 and W50. File 12 is under no round."). W47 and W48 are recorded (C-208, C-209), so W49 and W50 are the only file-12 items left out.
   - All other items W1–W50 have a change-list entry (35), a worklist record (10) or a record of the same proposal in its earlier round (W42, W43, W46 by B-305, B-300, B-299). W51–W56 are process items with no theory text.
5. **S95, the sceptic's rulings, section 3.**
   - **Where:** `tests/S95 Scrub - vocabulary, sceptic's rulings.md`, section 3 ("Occurrences the proposal does not cover"), second table, file lines 110, 111, 112 and 113:
     - "unsettled" → "left open";
     - l. 43's objection and reply → "What is independent of any assessor lies in the physics and in whether transports are faithful; scope-honesty lies in the record";
     - "verdict" → "assessment";
     - "credit" → "attribution".
   - **Held:** no record of the sceptic's rows. Collector D's coverage says section 3's rows are recorded, and its records D-598 … D-621 name lines 89–103 and 109, 114–121. The change of words itself is held as as-used vocabulary records (D-517, D-538, D-516, D-564) and as the S95 edits. The sceptic's proposal, including the one whole sentence for l. 43, is not. Line 122 proposes no change and is rightly left out.
6. **Texts made by rewriting the whole theory, with no record and no note in the ledger's index.**
   - **File 11 → file 12 (log S77):** `authority/12 Claude Fable Semantics - causality, standalone theory.md`, the whole theory rewritten with causation as its object. The only record touching file 12 is C-178, its pole-sentence slip. Collector A left it out as "a separate causality text".
   - **File 00 (FW5) → file 10:** collector A left it out, since the two texts differ as wholes.
   - The seeded copies of file 10 (logs S79 and S80; two and eight planted errors) are test material and are rightly left out.
   - Neither `00 Index.md` nor `line-up/index.md` says that these texts were left out, or why. A reader of the ledger cannot tell that file 12 exists. At least one "whole text" record, or a line in the index, is missing for each of the first two.

## 2. Recoverable only in part (stated by the collectors, and found so here)

These are gaps in the repository, not in the ledger. The ledger could say so in its index; at present only the coverage notes do.

- **R2 (log 25):** the amendments file "Claude Fable Proposed Amendments R2" was never in the repository. The ledger holds every sentence the returns quote: all 42 R2 rows of `results/S62 …/07 Quotations.md` and 27 of the 32 S64-R2 rows. The five left out (A02, B04, C06, I04, J03) are R2's "Expected benefit … Risk" paragraphs; D04, E04, F03, G01 and H01 are the other five.
- **Stage B rows 1–32 (log 41):** never reached the repository. Rows 33–112 are held, except 66, 90, 100, 101, 111 and 112, whose phrases all come from R2's reason paragraphs.
- **File 20 (logs 25–27, S62):** not held. Only its quoted passages are recorded. Q05/Q06, Q11/Q12 and Q19/Q20 are the same in both versions and are rightly left out.
- **The S76 patch (log S76):** description only (A-321).
- **The change list's working files** (the decisions as taken, the entry files, the two checks) are in a scratchpad of 23 September, not in the repository (lesson S23). Gap 1 above is what survives of them.

## 3. Round by round

| log | round | wording changed or proposed | held in the ledger | checked |
| --- | --- | --- | --- | --- |
| 24 | audit workflow | none for the theory | — | — |
| 25–27 | R2; file 20; round 3 | R2 amendments A–J; file 20's revisions; round 3's four outside cases (cases, no wording) | A-27 … A-163 (137), A-1 … A-26 (26) | all 42 R2 rows of S62/07 and 27 of 32 S64-R2 rows named (the other 5 are reason paragraphs); all 16 Q ids that differ, all 11 ATT and 14 XV rows named; sampled A-57, A-133, A-160 (at their rows) and A-3, A-20, A-21 |
| 28 | round 4 | clauses A-prime (4 sentences), C-prime (4) | A-238 … A-245 (8) | sentence counts of `tests/28` lines 8 and 11: 4 and 4; sampled A-239, A-242, A-244 |
| 29–31 | round 5, Stage A | A-second (7), C-second (6); skill changes (not the theory) | A-246 … A-258 (13) | `tests/30` line 21: 7 sentences, 7 records; sampled A-246, A-251, A-256 |
| 41, 55, 57 | Stage B, Stage C | Stage B phrase rows; Stage C cards (no wording) | A-164 … A-237 (74) | rows 33–112 less 6 reason-only rows: 74 of 74; sampled A-202, A-217, A-228 |
| S60–S62, S63 | S62 fix cards | A (1), C (8), G (2), H (2) | A-259 … A-271 (13) | sampled A-266, A-268, A-269; S63 itself proposes nothing |
| S64–S65, S70 | tighter pairs | H64, I64, H65 (3 each) | A-272 … A-280 (9) | sampled A-272, A-275, A-276, A-277, A-278, A-279, A-280 |
| S71 | S70 return | 21 clarifying lines | A-281 … A-301 (21) | sampled A-287, A-296, A-298, A-300 |
| S72–S75 | Stage 1 and 2; S75 | D3-1, D3-2, W01–W12; S75's claim and four sentences | A-302 … A-320 (19) | W01–W12 all present; sampled A-305, A-308, A-309, A-310, A-315 (S72) and A-316, A-318, A-320 (S75) |
| S76 | file 10 → file 11 | the whole revision | B-1 … B-182 (182); A-321 | independent sentence diff: every sentence of either file not in the other lies inside a B record, apart from layout (grievance headings joined to their answers) and splitter differences; the earlier checker found the same; sampled B-6, B-30, B-80, B-136, B-156 at their file-10 and file-11 lines |
| S77 | file 12 | a whole rewrite | none | **gap 6** |
| S78–S80, S82, S83 | reviews, seeded rounds, skill verdict, DeepSeek trial | none for the theory (planted errors are test material; S83's holes go to the worklist) | — | files scanned |
| S81 | file 11 determined | errata XR1–XR7; 12 unclear wordings; 3 reading hazards; 42 places to declare | B-183 … B-258 (76) | XR1–XR7 all named; 12 numbered items in det. 03 §8 → 23 records; 42 layer-2 rows; all 76 are descriptions, and B-184, B-215, B-234, B-251 were read against their source lines by eye |
| S87 | cross-examination of S81 | none (collector B's reading of the replies) | — | — |
| S88 | three defects | first and final wordings, fallbacks, F4, Atria's own wording | B-259 … B-290 (32) | final wordings held; sampled B-259, B-272, B-273, B-285, B-289; **gap 2** |
| S89 | the sources | 15 observations, M2–M6 handlings | B-291 … B-310 (20) | observations 1–14 held; 15 is cases; B-291, B-298, B-307 read against the source by eye |
| S90 | revision 2: worklist, plan, change list drafts 1–3, S90 rulings | see the next four rows | C-1 … C-145, C-190 … C-209 | — |
| | the change list at its five commits | 51, 58, 58, 60, 62 NEW blocks (55 theory changes and 3 meta at draft 3) | every NEW and OLD block is a record's `new` / `old` byte for byte | all five versions re-checked |
| | the S90 rulings | 32 rulings, 13 FIX on 10 entries | FIX wordings C-91 … C-110, declarations C-89, C-90, readers' proposals C-111 … C-145 | all 31 ruling files named; R01–R55 named (earlier checker); the optional wordings of batches 2 and 3 held via the ruling files (C-118, C-121, C-126) |
| | the worklist and the plan | worklist W1–W56; the plan's "Take" wordings | C-190 … C-209 | **gaps 3, 4**, and **gap 1** (pre-draft-1 fixes) |
| S91 | hard to vary, error correction, draft 4 | option (b), the lemma, the first rivals wording, draft-4 entries | E-38 … E-58 (21), C records of draft 4 (7) | sampled E-39, E-41, E-52, E-54, E-56 |
| S92 | plain words, file 92 | the pole-sentence slip (later W61.1) | C-104, C-178 | — |
| S93 | draft 4 cross-examined; draft 5 | X01–X18; FIX on 7 (X03, X05, X06, X09, X11, X17, X18); W35.5; findings carried forward | C records of S93 (56), E-36, E-37 | each of the 7 FIXes has its record (C-100 … C-105, C-107); W35.5 C-106; all 10 ruling files named; carried-forward items held |
| S94 | the owner's statement on choosing | changes 1–6; readers A–D | E-1 … E-35 (35) | every reader's "Proposed change" that is not "None" is held (A3, A4, A6, A10; B2, B3, B8; C2, C6, C8; D4, D14) |
| S95 | the scrub | 298 replacements + 2 filled lines; three vocabularies; three readings | D-1 … D-300; D-492 … D-717; D-718 … D-841 | 298 + 2 = 300 records, each entry's old and new matched; range 1 R1–R19 all named; range 2 repairs 1–23 all named; results §7 B-ids all named, §8 and §9 lines named; as-used 76 rows and proposed 96 rows all held; **gap 5** (sceptic's section 3) |
| S96 | the repairs, stages 1 and 2 | stage 1: 77 + line 2; stage 2: 28; two check files | D-301 … D-406; D-842 … D-875 | 78 and 28 records, each entry matched; whole-text section 5, 23 ids all named; the not-applied lists of both stages are held or propose no text (K l. 275 proposes none) |
| S97 | the replies ruled; stage 3 | 85 entries (74 from the replies, 8 from S28, 3 to the note); 53 rulings, 45 FIX | D-407 … D-491 (85); D-876 … D-952 (77) | 85 records, each entry matched; every ruling head of the reading's section 3 is named; 13 not-applied items held as declined or superseded, or have no wording ("S28 (i), places considered and left") |

**Three per round, by program.** Three records drawn at random from every round × collector cell that has wording (63 records, `sample.json` seed 3) were looked for at their `source_ref`. All 63 were found in their source: 41 at the named line, row or JSON entry, and 22 inside the named entry or item where the reference gives no line. With the 86-record sample of the fidelity check, every round with wording has at least three records checked at the source.

**Counts the task named, reconciled:**

- 55 changes at draft 3: yes, 58 NEW blocks = 55 theory + 3 meta, all held.
- 298 S95 replacements: yes, plus the 2 filled lines.
- 77 + stage 2 + 85 S96 replacements: 77 + 1, 28, and 85, all held.
- 45 FIX rulings in S96/S97: every ruling head held.
- 7 S93 FIXes: yes.
- The S88 repairs: yes for the final and earlier wordings; gap 2 for the reader's own.
- The file 10 → file 11 edits: yes.

## 4. Files listed in INDEX.md that no record uses and no coverage note names

84 entries. By kind:

- the cross-examination packs and briefs (S87, S88, S90, S93 parts);
- the "how it will be read" rules;
- the S80 and S81 plans, prompts and case books;
- the S79 and S80 seeded copies;
- the instruction pack;
- the draft theory texts themselves (used as targets, not sources);
- plain-words files 91–97;
- `records/` files.

Scanned for proposed wording:

- S90 reading batches 2 and 3: their optional wordings are held through the ruling files.
- The S90 and S93 files that check drafts 3 and 5: no wording beyond the entries.
- The DeepSeek trial: none.
- File 91: none.
- The Status file: none beyond what is held.

The one file here that carries unheld wording is the plan (gap 3). It is named in collector C's coverage as skipped.
