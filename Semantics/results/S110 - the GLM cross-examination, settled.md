# S110 - the GLM cross-examination, settled

*Written 29 September 2026 by one Opus 5.5 agent (decision S56: "It's capable of doing the whole thing on its own. Use GLM for cross examination."), under rules 3 to 6 of `results/S110 - how the GLM cross-examination will be read, written before sending.md` (committed before sending). This agent did not write the work cross-examined; it weighs arguments, not their source. An objection is a claim until settled; several jobs saying the same thing decides nothing; silence is not agreement. For a statement about a book, the settlement is made against the book's extracted text in the scratchpad (checked by script; never put in the repository beyond checked quotations of at most 25 words). "Candidate" or "explanation" for what the theory judges, never "model" (S43). Nothing here changes the theory's text, formal core, claims or program, any Part A, Part B or S111 file, the decisions record, `authority/` or the six frameworks. No owner decision is added. Since the files were sent, the owner has stated knowledge by three properties and asked for a program with them (decision S59; log S111, running separately); nothing here touches that work.*

## 0. The condition for opening, and what came back

The run log (`S110 - GLM cross-examination returns/run log.txt`) ends "s110x_glm_loop: every pass ended; accepted 4 of 4 jobs" and "loop ended 2026-09-29T10:12:08Z"; the process had exited. Receipts, checked by the orchestrator before any reply was read: key_found_in_output_and_replaced = 0 and sandbox_unchanged = true for all four; model glm-5.3; each reply ends END OF REPORT (job a 1,705 words, b 1,795, c 1,746, d 1,947). Returns at commit a1212ed. After sending, the orchestrator cut one run of 26 of Marletto's words in file 3 to 17 (commit 2227bbe, S19's 25-word limit); the version sent is in 42ef7a4; file 3's corrected copy starts from the cut version.

| job | angle | objections | stand | stand in part | do not stand |
|---|---|---|---|---|---|
| a | the change map against FW0 and I2 | 8 (Xa1–Xa8) | 6 | 2 | 0 |
| b | the change map against FW2, FW3, FW4 | 14 (Xb1–Xb14) | 13 | 1 | 0 |
| c | the change map against FW5, the present theory and the S89 audit | 11 (Xc1–Xc11) | 9 | 2 | 0 |
| d | files 1 and 3: consistency, readings passed off as the book's, the owner's decisions | 9 (Xd1–Xd9) | 6 | 2 | 1 |
| all | | **42** | **34** | **7** | **1** |

GLM's own ids (X1.1 … X4.9) are renamed Xa1 … Xd9 in the order each reply gives them. What each job checked without objection and what it did not reach is in its reply; nothing there is taken as agreement.

**What was used to settle**: the six frameworks as supplied (`tests/S110 Material - earlier frameworks, supplied by the owner/`), read at each place an objection names; the present theory (`tests/107`); `results/S89`, `results/S96 The scrubbed copy repaired - …`, `tests/Revision 2 - hard to vary restated through rivals and problems, 25 September.md`; the decisions record (read only); the book's extracted text for Xd1, Xd2, Xd4 and Xd7 (searched by script: counts of "error", "errors" and the forms of "error correction" per chapter; every passage on "abstract catalyst" in chapter 5; the paragraph of chapter 1 on bacterial DNA; Property Two in chapter 3).

## 1. The objections and their settlement

### Job a: the change map against FW0 and I2

**Xa1. Edge e98 (I2 → FW5, dropped) is marked "stated", though the FW5 sentence it cites is about specification 0.1 (S7), not I2 (0.4).**
*Settlement: **stands**.* FW5 line 1274 ends "[S7: Parts I–III; …]"; the map's own section 1 says "No document says FW5 read I2", and e96 and e97, which rest on the same section of FW5, are marked inferred for the same version gap. *Changes:* e98 inferred, its "by" naming the version gap; the I2 → FW5 step now has no stated edge.

**Xa2. e98's line ("implementation choices") does not describe two of its four sources: I2.13 (daydreaming and jolts) and I2.14 (finite resources are realisation conditions).**
*Settlement: **stands in part**.* For I2.13 it does not stand: I2 itself calls daydreaming "an operational allowance, not … a new semantic condition for creativity" (Part VIII), which is what FW5's "not a condition of this class" says of implementation choices; I2.13 stays in e98, the line now naming it. For I2.14 it stands: finite resources as realisation conditions are not dropped by FW5, which makes resources part of the declared "enabling conditions" under which a capability is claimed ("Enabling conditions and achievement conditions"). *Changes:* e98's sources I2.10, I2.11, I2.13 and its line rewritten; new edge e150, I2.14 → FW5.20, changed, inferred.

**Xa3. Section 5's "persisted" chains use links that are not edges of the map (rows 1, 3, 4, 7, 8, 9), one begins at a dropped node, and FW5.16 and FW5.17 have no incoming edge.**
*Settlement: **stands**.* Checked against the edge list: FW0.7 → FW2.11, FW2.11 → FW3.1, FW2.15 → FW5.10, FW4.9 → FW5.7, I2.9 → FW2.18, FW3 → FW4.1, FW0.17 → FW2.21 and anything into FW5.16 or FW5.17 are not edges; the section's definition ("a chain of kept or changed edges") is broken by its own rows (and by e49, e107, which are "added" and "replaced"). Two links were dead ends in the map itself: FW4.9 (Bearing as an instance of Account) had no later edge, and FW4.8 (Account) had none into FW5. *Changes:* section 5 rewritten so that every link is named by its edge and every link without one is marked [reading]; three inferred edges added where the frameworks' wording joins the nodes directly: e160 FW4.9 → FW5.7, e161 FW0.7 → FW2.11 (FW0.7's own line holds "prediction is not explanation"), e162 FW4.8 → FW5.4. The remaining gaps (newness through FW3 to FW5; I2.9 onward; FW3 to FW4.1; into FW5.16 and FW5.17) are left as readings, not filled by edges.

**Xa4. FW0 §16.2 (comparisons, Preferred, Defeated, GoodNow) has no node.**
*Settlement: **stands**.* §16.2 is FW0's device for present standing; "Preferred … a set; several maximal comparisons are reported, not collapsed" and "`GoodNow` does not entail `True`, finality, or wide reach" are its words. *Changes:* node FW0.21; edge e151 FW0.21 → FW2.18, changed, inferred; section 5's "no score" row now starts from it.

**Xa5. I2 Part II "Dependency effects are scoped, not a truth cascade" has no node.**
*Settlement: **stands**.* The section exists (I2 line 161) and bears on error correction as the map's FW0.4 and FW2.13 do. *Changes:* node I2.15; edge e152 I2.15 → FW5.31 (FW5's Usable_j, added under Xc3), kept, inferred, version gap as e96.

**Xa6. FW0 §7.5 (completeness certificates) and §6.4 (diversion and lapse) have no nodes; the second is proposed as the ancestor of PT.17.**
*Settlement: **stands in part**.* Both sections exist and say what the objection quotes ("Without the certificate, absence yields OPEN …"; "Diversion proves attention elsewhere, not abandonment"). The lineage to PT.17 crosses five missing documents and no supplied text names it; it is not made an edge. *Changes:* nodes FW0.22 and FW0.23, on no edge (section 11 of the corrected map says why).

**Xa7. Section 9 folds CR-1.0, FW0's standing authority, into M0, and the closing note omits Dung (1995), "deutsch-loop" and I2's research register R1–R17.**
*Settlement: **stands**.* FW0: "CR-1.0 remains the authority for what it says"; its placement names Revision D and its second audit as the immediate predecessors, so CR-1.0 is a different document from M0. The source map cites Dung (1995) "as used in deutsch-loop"; I2 has a research register. *Changes:* a CR-1.0 row (missing links now 21); M0's line without CR-1.0; the closing note extended.

**Xa8. FW0.11's and FW0.12's lines cite change-register rows instead of saying what §§12–14 say, and FW0.11 says "equated" where row 8 says "bound".**
*Settlement: **stands**.* Row 8: "Public classifiers bound to their witnesses"; §14: the system "must represent the criticism it answers". *Changes:* both lines rewritten.

### Job b: the change map against FW2, FW3 and FW4

**Xb1. e48 parks FW2.13 and FW2.28 as kept unchanged, but FW3's change register amends both ("Part II, dependencies"; "Part II, hierarchy").**
*Settlement: **stands**.* FW3 lines 352 and 357; T11 (line 168). *Changes:* both removed from e48; node FW3.24 (T11); edges e153 FW2.13 → FW3.24 and e154 FW2.28 → FW3.20, changed, stated.

**Xb2. e65 drops FW3.23 (the deployed set is a record fact), which FW4 keeps (R15; Part XII's record facts).**
*Settlement: **stands**.* FW4 line 205: "Operative role is a record fact; work is not." *Changes:* e65 from FW3.22 only; edge e157 FW3.23 → FW4.15, kept, inferred.

**Xb3. Section 1 says the five stated FW3 → FW4 edges are stated by FW5; e54 and e56 are stated by FW4's own header.**
*Settlement: **stands**.* *Changes:* the sentence corrected.

**Xb4. FW3.6 (Progress as a gain in Account or Bearing) has no incoming edge, though the register states it.**
*Settlement: **stands**.* Register row "Part II, progress". *Changes:* edge e155 FW2.31 → FW3.6, changed, stated.

**Xb5. FW2's jump conjecture, realization constraints 3 to 6, and "Refinement without semantic substitution" have no nodes.**
*Settlement: **stands**.* FW2 lines 566, 425–428, 576–580. *Changes:* nodes FW2.33, FW2.34 (both added to e48, since FW3 withdraws nothing of FW2) and FW2.35; e43's sources now FW2.14 and FW2.35 (the register row is "Part IV, refinement"), rather than a second edge for the same row.

**Xb6. Section 8 gives FW4's wording ("spread by imitation") to FW3 T5 and case 10 as well.**
*Settlement: **stands**.* FW3 T5 and case 10 say "uptake". *Changes:* each quoted in its own words.

**Xb7. Section 5's "no score" row omits FW4.16; the newness and authorship rows leave the FW4 gap unmarked.**
*Settlement: **stands**.* *Changes:* with Xa3's rewrite.

**Xb8. e35's "by" does not state the identification of Merit with FW2's "current good explanation"; FW3 I.5 does.**
*Settlement: **stands**.* FW3 line 124. *Changes:* e35's "by".

**Xb9. e42's "by" (register row on K-STANDING) does not state "warrant is eliminated"; T17 does.**
*Settlement: **stands in part**.* T17 is the direct statement and should be cited; but the register row is not wrong: its amendment, III.3, ends "'merits' … is to be read as this and not as residual warrant", citing the same N1 §6 C5. *Changes:* e42's "by" names T17, III.3 and the row.

**Xb10. Section 8 attributes "not permitted" to FW3 T2; the words are FW4's (Indexing); T2's title is "No existential closure".**
*Settlement: **stands**.* *Changes:* the attribution corrected.

**Xb11. e76's "by" does not state "no upward closure and no minimal member".**
*Settlement: **stands**.* FW5 "Support families without a minimality assumption" (line 267) does. *Changes:* e76's "by".

**Xb12. Section 8 gives D1 §3 and §6 C4 for both e37 and e38; T2 cites §6 C1.**
*Settlement: **stands**.* *Changes:* the two citations separated.

**Xb13. FW3's Contribution conjecture (I.4) has no node.**
*Settlement: **stands**.* FW3 line 114; register row "Part II, newness and authorship". *Changes:* node FW3.25; edge e156 FW2.16 → FW3.25, changed, stated; FW3.25 added to e64.

**Xb14. e56's "by" names only "transport"; the three cases are FW4 III.5.**
*Settlement: **stands**.* *Changes:* e56's "by".

### Job c: the change map against FW5, the present theory and the S89 audit

**Xc1. e125's line puts back "only", which the S96 repair removed and the present theory does not say.**
*Settlement: **stands**.* tests/107 line 75 has "enters … and it also enters"; S96: "Stage 2 drops 'only' (O-1)". *Changes:* e125's line.

**Xc2. e122 (a failed answer stays failed) says "the revision that added it is not traced here"; it is recorded as W60.1.**
*Settlement: **stands**.* The Revision 2 note on hard to vary, W60.1, "inserted after 'Historical index'". *Changes:* e122 recorded.

**Xc3. No node for the present theory's conflict with a claim and rivals given a claim; for the question-contract machinery (FW5, PT Part III); for FW5's Usable_j (K2), so that e110 hangs K2 on a node that has only K3.**
*Settlement: **stands**.* tests/107 Part VI "Rivals" ("Conflict with a claim"); Part III "Contracts have provenance"; FW5 "Questions and their contracts", "Standing and actual use" (K2). *Changes:* nodes PT.34, PT.35, FW5.31, FW5.32; edge e158 (none) → PT.34, added, recorded (decisions S25 to S27; S96); edge e159 FW5.32 → PT.35, changed, inferred; e110 from FW5.8 and FW5.31 (not a new edge, as the objection proposed, since e110 already carries the K2 change).

**Xc4. e113 marks FW5.18 (two kinds of defect) as dropped on a one-word search, though the present theory keeps the distinction in (R).**
*Settlement: **stands**.* tests/107 line 211: "A system can represent a theory in error: the transport from carrier to content is faithful while the transport from the content's target to the content fails." A damaged carrier is a failure of the first transport, a false theory of the second. *Changes:* e113 FW5.18 → PT.8, changed, inferred; "In brief" (4), section 3 item 4 and section 6's row reworded.

**Xc5. e103's "copying kept as a transformation" is not in the S89 observations it cites.**
*Settlement: **stands**.* Observations 3 and 8 do not mention copying. *Changes:* the clause marked as read in tests/107.

**Xc6. e105 (CT1, CT2 kept) cites observation 3, which is about the tasks paragraph.**
*Settlement: **stands in part**.* The citation is wrong; the standing is not: observation 8 records "CT1 and CT2 retention" in file 10. *Changes:* e105's "by" (observation 8; tests/107 Part XII); still recorded.

**Xc7. e101 cites observation 9 for declared provenance; that is observation 10.**
*Settlement: **stands**.* *Changes:* e101's "by".

**Xc8. File 1 section 6 item 5: "error correction without the word" is false; the words occur once.**
*Settlement: **stands**.* One occurrence, in the S27 sentence the item quotes. *Changes:* file 1's copy.

**Xc9. File 3 O11 attributes "with no represented target in that history" to Part IV; it is Part 0's wording (Part X has its like).**
*Settlement: **stands**.* The phrase is at tests/107 lines 13 (Part 0) and 411 (Part X) only. *Changes:* file 3's copy gives the phrase its places, "(Part 0; Part X, not Part IV)".

**Xc10. e73 is "stated" by a list that names "criticism as itself conjectural", not "reason-bearing".**
*Settlement: **stands**.* FW5 line 1272. *Changes:* e73's "by" marks the reason-bearing half inferred.

**Xc11. PT.3's "where" cites Part V for "Account(E) and not Dec(t)"; Part V defines only Account(E).**
*Settlement: **stands in part**.* The joined phrase is in Part 0 (line 17) and Part I (line 69), and Part I was already cited; Dec is defined in Part IV (line 199). *Changes:* PT.3's "where" names all four.

### Job d: files 1 and 3

**Xd1. File 1 section 3 claims every place the book speaks of error, but covers chapters 1, 5 and 7 while section 1 counts chapter 2.**
*Settlement: **stands**, with a fix other than the one proposed.* GLM proposed saying the chapter 2 occurrences are "not about correction"; the book's text shows the opposite. Counted in the extracted text: "error" and "errors" 17 (chapter 1: 14, chapter 2: 1, chapter 7: 2; none in chapter 5, where the cricket's changes are "no longer corrected"); the forms of "error correction" 5 (chapter 1: 2, chapter 2: 1, chapter 7: 2). The chapter 2 place, after Galileo's refutation of Aristotle, says testability “is central for the possibility of error correction, and therefore for the progress of science as a whole.” (Marletto, ch. 2) So file 1 was wrong three times: section 1 listed chapter 5, In brief and section 1 said the forms occur in chapters 1 and 7 only, and section 3 missed the place. *Changes:* file 1's copy: the counts, a new item 7a, and "What the book does not state" amended.

**Xd2. File 3 O3's paraphrase "every catalyst contains one" says more than the book, which restricts it to things with the appearance of design.**
*Settlement: **does not stand**.* Chapter 5 says, in the author's words, “all catalysts must contain an abstract catalyst” (Marletto, ch. 5), and repeats it a page later; the restriction to the appearance of design is a separate conclusion of the same chapter. GLM could not see the book. *Changes:* none.

**Xd3. File 3 section 3.1 gives FW4's wording to FW3 T5 as well; R2 and R5 are Part VIII, not Part VI.**
*Settlement: **stands**.* As Xb6. *Changes:* file 3's copy.

**Xd4. File 1 I3 calls the joined example (the repairing cell is built by the DNA it repairs) "the book's example", though the joining is Claude's.**
*Settlement: **stands in part**.* The joining is the book's own: in the paragraph of item 2 the book says that “the rest of the new cell is constructed by executing the recipe in the DNA” (Marletto, ch. 1), and then that the copy is error-corrected by the cell. What stands is that I3 cited the example as item 2 joined to chapter 5, which invited the objection. *Changes:* file 1's I3 cites the chapter 1 sentence; plain file 110's "the book's example" is kept.

**Xd5. File 1 section 8 cites the change map's section 6 for Shannon; it is section 7.**
*Settlement: **stands**.* *Changes:* file 1's copy.

**Xd6. File 1 section 6 item 5's range "PT.6 to PT.30" does not match its claim.**
*Settlement: **stands**.* *Changes:* "PT.20 to PT.23 and PT.32; PT.6".

**Xd7. File 1 I4 moves from what a corrector does (tell apart) to the corrected thing being an information medium (flip and copy) with an unnamed gap: telling apart is not copying.**
*Settlement: **stands in part**.* The book closes most of the gap: its second property of information is that states “can be received and distinguished in some other location” (Marletto, ch. 3), and the next sentences of the chapter call that property, in the book's own words, “the possibility of performing a copy-like operation.” (Marletto, ch. 3) What stands is that I4 did not show this, and a residue remains for states a corrector cannot read. *Changes:* I4 gives the book's words and a named step to attack.

**Xd8. File 3 section 3.2 marks as [implied] a premise ("fear makes it memorable") that is neither the book's nor the frameworks'.**
*Settlement: **stands**.* *Changes:* marked as the example's assumption [reading].

**Xd9. File 1 section 4 promises a step to attack for each [implied]; I5 to I7 give none.**
*Settlement: **stands**.* Writing them found one real weak point: the book calls copying slips and flaws in conjectures errors, but never a variant's failure to survive, so I5's third kind of "error" is the argument's classification. *Changes:* a step to attack for each of I5, I6, I7; plain file 110's sentence on the three ways adjusted.

## 2. What changed, in the corrected copies

- `results/S110 The change map - the earlier frameworks and the present theory, after the cross-examination.md` and `.json` (written by `tools/s110x_change_map_amend.py`, which imports `tools/s110_change_map.py`'s data and build and writes neither that tool nor the map as sent; its `--check` rebuilds and compares). Every node, edge and missing link touched carries its objection ids. **Totals: 185 nodes (was 172), 145 edges (was 132): 65 changed, 46 kept, 18 added, 10 dropped, 6 replaced; 48 stated, 18 recorded, 79 inferred (was 45, 16, 71); 21 missing links (was 20).** New nodes: FW0.21–FW0.23, I2.15, FW2.33–FW2.35, FW3.24, FW3.25, FW5.31, FW5.32, PT.34, PT.35. New edges: e150–e162. Two nodes (FW0.22, FW0.23) stand on no edge.
- `results/S110 Error correction from constructor theory's perspective, after the cross-examination.md`: Xc8, Xd1, Xd4, Xd5, Xd6, Xd7, Xd9. Quotations rechecked by `tools/s110_quote_check.py`: 67 (57 Marletto, 10 Deutsch), every check passes.
- `results/S110 When something in a creative agent is knowledge - what the sources offer, after the cross-examination.md`: Xc9, Xd3, Xd8; O3 unchanged (Xd2). Quotations rechecked: every check passes.
- `plain words/110 …`: updated in place to match; its note says it now follows the check; a section on what the check changed; the next step (S59's work, log S111).
- The files as sent, the tool `s110_change_map.py` and its `.json` are unchanged (`--check`: identical).

## 3. Recorded for the owner, not applied (rule 5)

None of the 42 objections would settle what the S110 files leave to the owner (which question to take forward; the readings of "capable" and of what a spreading idea is knowledge of; whether the two-types result holds). None ranks the options. Since the files were sent the owner has set the next step (S59: knowledge stated by three properties, measured on Avida, log S111; "The explanation kind comes next"); nothing here bears on it beyond what file 3 already lays out.

## 4. Unsure

- Xa3's three added edges (e160–e162) are Claude's reading, like every FW3 → FW4 → FW5 link across Q2 and M4; they were added because the frameworks' wording joins the two nodes directly, and the rest of section 5's gaps were left as readings rather than filled.
- The settlement read the frameworks at the places the objections name; a node the map and GLM both missed would not be found this way (the rule's own caveat).
- Xd1's counts are of this extraction of the book; a different extraction could split a hyphenated word differently. The counts per chapter were made on the same files the quotation check uses.

Settled by Claude under decisions S56, S57 and S58 and the reading rule. 29 September 2026.
