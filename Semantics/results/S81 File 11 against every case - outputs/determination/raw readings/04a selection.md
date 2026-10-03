# 04a Selection: the rows step 3 rules, and the counts the returns give by program

*The selector's output for the S81 determination, 23 September 2026. The selection was made by a program, `build_packets.py`, kept in the working folder with its log. It reads `table.md`, the accepted returns, 01 and 03 without changing them, applies the plan's step-3 criteria, and builds one evidence packet per selected row (`04e packets/`). It rules on no row. Its structured record is `selection.json` in the working folder. The text below is the selector's output as passed to the determination, set out by field. It is data for the determination, not a ruling.*

**Two notes added when this file was written.**
- The `k_vs_s72` text as passed ends at the words "For comparison,". Nothing after them reached the determination. The structured fields it summarises (`k_vs_s72`, `both_1K_agree_on_non_baseline`) are given after it.
- The `k_vs_s72` text says "The union is 16 rows" and then lists 15. The count is 15: 8 rows for 1K A and 13 for 1K B, 6 of them shared (O15, O18, O20, O31, O40, O45). The determination uses 15.

---

## rows

The 33 selected rows, with the reason or reasons for each.

| case | reasons |
|---|---|
| O1 | 1K differs from baseline: 1K B DISAGREE vs baseline SILENT; step 4 flag; step 5 SILENT |
| O2 | step 4 flag |
| O3 | step 4 flag |
| O4 | 1K differs from baseline: 1K A SPLIT vs baseline AGREE; both 1C AGREE, a BLIND MARK not AGREE (table: READ: mimo on B SPLIT) |
| O5 | file-11 reading differs from baseline: 1C A SILENT vs baseline AGREE; file-11 reading differs from baseline: 1C B SILENT vs baseline AGREE; file-11 reading differs from baseline: 2b Atria on A (high) YOUR MARK SILENT vs baseline AGREE; file-11 reading differs from baseline: 2b Mimo on B (medium) YOUR MARK SILENT vs baseline AGREE; step 4 flag |
| O8 | both 1C AGREE, a BLIND MARK not AGREE (table: READ: atria on A SILENT); step 4 flag |
| O10 | file-11 reading differs from baseline: 1C B SILENT vs baseline AGREE; file-11 reading differs from baseline: 2b Atria on B (medium) YOUR MARK SILENT vs baseline AGREE; file-11 reading differs from baseline: 2b Mimo on B (medium) YOUR MARK SILENT vs baseline AGREE; 1K differs from baseline: 1K B SILENT vs baseline AGREE |
| O12 | step 4 flag; step 5 SILENT |
| O13 | both 1C AGREE, a BLIND MARK not AGREE (table: READ: atria on A DISAGREE, atria on B DISAGREE) |
| O14 | step 4 flag |
| O15 | file-11 reading differs from baseline: 1C A SPLIT vs baseline AGREE; 1K differs from baseline: 1K A SPLIT vs baseline AGREE; 1K differs from baseline: 1K B SPLIT vs baseline AGREE |
| O16 | step 4 flag |
| O17 | file-11 reading differs from baseline: 1C A SILENT vs baseline AGREE; file-11 reading differs from baseline: 2b Atria on A (high) YOUR MARK SILENT vs baseline AGREE; step 4 flag |
| O18 | 1K differs from baseline: 1K A SPLIT vs baseline AGREE; 1K differs from baseline: 1K B DISAGREE vs baseline AGREE; step 4 flag; pre-reading differs from baseline: 01 file-10 SPLIT vs baseline AGREE |
| O19 | both 1C AGREE, a BLIND MARK not AGREE (table: READ: mimo on B SPLIT) |
| O20 | file-11 reading differs from baseline: 1C A AGREE vs baseline SILENT; file-11 reading differs from baseline: 1C B AGREE vs baseline SILENT; file-11 reading differs from baseline: 2b Atria on A (high) YOUR MARK AGREE vs baseline SILENT; file-11 reading differs from baseline: 2b Atria on B (medium) YOUR MARK AGREE vs baseline SILENT; file-11 reading differs from baseline: 2b Mimo on B (medium) YOUR MARK AGREE vs baseline SILENT; 1K differs from baseline: 1K A AGREE vs baseline SILENT; 1K differs from baseline: 1K B AGREE vs baseline SILENT; step 4 flag; step 5 SILENT; pre-reading differs from baseline: 01 file-10 AGREE vs baseline SILENT |
| O21 | file-11 reading differs from baseline: 2b Atria on B (medium) YOUR MARK AGREE vs baseline SILENT; step 4 flag; step 5 SILENT; pre-reading differs from baseline: 01 file-10 AGREE vs baseline SILENT |
| O24 | step 4 flag |
| O27 | file-11 reading differs from baseline: 2b Atria on B (medium) YOUR MARK AGREE vs baseline SILENT; step 4 flag; step 5 SILENT; pre-reading differs from baseline: 01 file-10 AGREE vs baseline SILENT |
| O30 | file-11 reading differs from baseline: 1C A SILENT vs baseline AGREE; file-11 reading differs from baseline: 2b Atria on A (high) YOUR MARK SILENT vs baseline AGREE; file-11 reading differs from baseline: 2b Atria on B (medium) YOUR MARK SPLIT vs baseline AGREE; named in 2b Atria on B (medium) under "Disagreements the reading under audit left unmarked" (COUNT 1); step 4 flag |
| O31 | 1K differs from baseline: 1K A SPLIT vs baseline AGREE; 1K differs from baseline: 1K B DISAGREE vs baseline AGREE; step 4 flag |
| O32 | file-11 reading differs from baseline: 1C A DISAGREE vs baseline AGREE; 1K differs from baseline: 1K B SILENT vs baseline AGREE; mentioned in 2b Atria on A (high) under "Wrong, and uncorrected anywhere in the theory" in an entry that reports none (COUNT 0); not a listed row |
| O33 | both 1C AGREE, a BLIND MARK not AGREE (table: READ: atria on A DISAGREE, atria on B DISAGREE) |
| O35 | step 4 flag (decisive); step 5 SILENT; pre-reading differs from baseline: 01 file-10 AGREE vs baseline SILENT |
| O37 | step 4 flag; pre-reading differs from baseline: 01 file-10 SPLIT vs baseline AGREE |
| O38 | 1K differs from baseline: 1K B SPLIT vs baseline AGREE; step 4 flag |
| O39 | 1K differs from baseline: 1K B SPLIT vs baseline AGREE |
| O40 | file-11 reading differs from baseline: 1C A AGREE vs baseline SILENT; file-11 reading differs from baseline: 1C B AGREE vs baseline SILENT; file-11 reading differs from baseline: 2b Atria on A (high) YOUR MARK AGREE vs baseline SILENT; file-11 reading differs from baseline: 2b Atria on B (medium) YOUR MARK AGREE vs baseline SILENT; file-11 reading differs from baseline: 2b Mimo on B (medium) YOUR MARK AGREE vs baseline SILENT; 1K differs from baseline: 1K A AGREE vs baseline SILENT; 1K differs from baseline: 1K B AGREE vs baseline SILENT; both 1C AGREE, a BLIND MARK not AGREE (table: READ: atria on B SPLIT); step 4 flag; step 5 SILENT; pre-reading differs from baseline: 01 file-10 AGREE vs baseline SILENT |
| O41 | 1K differs from baseline: 1K A SPLIT vs baseline AGREE; step 4 flag; pre-reading differs from baseline: 01 file-10 SPLIT vs baseline AGREE |
| O45 | 1K differs from baseline: 1K A SPLIT vs baseline AGREE; 1K differs from baseline: 1K B SPLIT vs baseline AGREE |
| O46 | 1K differs from baseline: 1K B SILENT vs baseline AGREE |
| O48 | O48 in full (plan step 3); file-11 reading differs from baseline: 1C A AGREE vs baseline DISAGREE; file-11 reading differs from baseline: 1C B AGREE vs baseline DISAGREE; file-11 reading differs from baseline: 2b Atria on A (high) YOUR MARK AGREE vs baseline DISAGREE; file-11 reading differs from baseline: 2b Atria on B (medium) YOUR MARK AGREE vs baseline DISAGREE; file-11 reading differs from baseline: 2b Mimo on B (medium) YOUR MARK AGREE vs baseline DISAGREE; 1K differs from baseline: 1K B SPLIT vs baseline DISAGREE; step 4 flag |
| O50 | file-11 reading differs from baseline: 1C B DISAGREE vs baseline SILENT; file-11 reading differs from baseline: 2b Atria on B (medium) YOUR MARK AGREE vs baseline SILENT; step 5 SILENT |

## silent_rows

O1, O12, O20, O21, O27, O35, O40, O50.

## p4

P4 FAILS for both testers, because neither set is exactly {O48}. Tester A: 1K and 1C differ on 10 cases: O4 (1K SPLIT / 1C AGREE), O5 (AGREE / SILENT), O17 (AGREE / SILENT), O18 (SPLIT / AGREE), O30 (AGREE / SILENT), O31 (SPLIT / AGREE), O32 (AGREE / DISAGREE), O41 (SPLIT / AGREE), O45 (SPLIT / AGREE), O48 (DISAGREE / AGREE). Tester B: they differ on 12 cases: O1 (1K DISAGREE / 1C SILENT), O5 (AGREE / SILENT), O15 (SPLIT / AGREE), O18 (DISAGREE / AGREE), O31 (DISAGREE / AGREE), O32 (SILENT / AGREE), O38 (SPLIT / AGREE), O39 (SPLIT / AGREE), O45 (SPLIT / AGREE), O46 (SILENT / AGREE), O48 (SPLIT / AGREE), O50 (SILENT / DISAGREE). O48 is in both sets. "Model" is read as "tester", as the plan says. P4 is a claim about the readers, not about the theory.

## e2_substitute

This is not E2. E2 cannot be scored as written, because no model now writes both a 2a and a 1C. The substitute sets each auditor's BLIND MARK (its 2a reading, as marked in its own 2b) against the audited tester's 1C mark, row by row, over all 52 rows. Beside it stands the count of rows where that tester's 1K and 1C marks differ. (1) Atria on A (high): 7 rows differ: O8 (blind SILENT / 1C AGREE), O10 (SPLIT / AGREE), O13 (DISAGREE / AGREE), O15 (AGREE / SPLIT), O30 (SPLIT / SILENT), O32 (AGREE / DISAGREE), O33 (DISAGREE / AGREE). Tester A's 1K and 1C differ on 10 rows. (2) Atria on B (medium): 8 rows differ: O5 (blind AGREE / 1C SILENT), O13 (DISAGREE / AGREE), O21 (AGREE / SILENT), O27 (AGREE / SILENT), O30 (SPLIT / AGREE), O33 (DISAGREE / AGREE), O40 (SPLIT / AGREE), O50 (AGREE / DISAGREE). Tester B's 1K and 1C differ on 12 rows. (3) Mimo on B (medium): 6 rows differ: O1 (blind SPLIT / 1C SILENT), O4 (SPLIT / AGREE), O10 (SPLIT / SILENT), O19 (SPLIT / AGREE), O35 (DISAGREE / SILENT), O50 (SPLIT / DISAGREE). Again 12 rows for tester B. (4) Mimo on A cannot be counted: its 2b is MISSING (failed twice). On all three counted pairs, the blind-versus-1C count is lower than the tester's 1K-versus-1C count (7 < 10, 8 < 12, 6 < 12). The comparison mixes two things: seeing the fixed verdict and the tester's reading, and a change of family (Atria or Mimo against Claude testers). It also carries the effort confound: Atria on A ran at high, and the other two at medium. It is recorded as such, and it scores no expectation. For reference only, the auditors' YOUR MARK differs from the tester's 1C on 2 rows for Atria on A (O15, O32), 5 for Atria on B (O5, O21, O27, O30, O50) and 1 for Mimo on B (O50).

## stopping_rule

The rule did not fire. The R rows are O24, O11 and O22 for tester A, and O22 and O11 for tester B. 2b Atria on A (high) gave ON VERDICT AGREE and ON MARK AGREE on O24, O11 and O22. 2b Atria on B (medium) gave ON VERDICT AGREE and ON MARK AGREE on O22 and O11. 2b Mimo on B (medium) did the same on O22 and O11. 2b Mimo on A is MISSING (failed twice), so its R rows (O24, O11, O22) cannot be scored. No auditor marked DISAGREE, ON VERDICT or ON MARK, on any R row. No row lies outside either sample: each covers all 52 rows (plan third version, change i). So no widen could have been built even if the rule had fired, and no 2W exists. All three returns have an empty Part 2.

## case_disputed

There are none. No return marks any case CASE DISPUTED. 1C A, 1C B, 1K A and 1K B each count "CASE DISPUTED: 0 - none", and no MARK line in them reads CASE DISPUTED. The three accepted 2b returns (Atria on A, Atria on B, Mimo on B) count "YOUR MARK ... CASE DISPUTED 0". Parsing finds no BLIND MARK, TESTER MARK or YOUR MARK of CASE DISPUTED. Each "Cases to rule on" section has COUNT 0. Atria on A adds: "neither reading marked any case CASE DISPUTED, and no situation, read in ordinary terms before any theory, decides a point against its fixed verdict". The 2a returns carry no marks. 2b Mimo on A is MISSING. Step 6 has nothing to set aside on the returns' evidence, and the provenance file was not opened.

## k_vs_s72

This is not a verdict on file 10 for the record. The baseline is S75's determination from the S72 table as audited. 1K A differs from it on 8 rows: O4 (SPLIT vs AGREE), O15 (SPLIT vs AGREE), O18 (SPLIT vs AGREE), O20 (AGREE vs SILENT), O31 (SPLIT vs AGREE), O40 (AGREE vs SILENT), O41 (SPLIT vs AGREE), O45 (SPLIT vs AGREE). 1K B differs from it on 13 rows: O1 (DISAGREE vs SILENT), O10 (SILENT vs AGREE), O15 (SPLIT vs AGREE), O18 (DISAGREE vs AGREE), O20 (AGREE vs SILENT), O31 (DISAGREE vs AGREE), O32 (SILENT vs AGREE), O38 (SPLIT vs AGREE), O39 (SPLIT vs AGREE), O40 (AGREE vs SILENT), O45 (SPLIT vs AGREE), O46 (SILENT vs AGREE), O48 (SPLIT vs DISAGREE). The union is 16 rows: O1, O4, O10, O15, O18, O20, O31, O32, O38, O39, O40, O41, O45, O46, O48. Both 1K returns agree on the same non-baseline mark on 4 rows: O15 SPLIT, O20 AGREE, O40 AGREE and O45 SPLIT. These are the only rows where the plan's condition for correcting the baseline can arise, and it applies only if Claude's own reading of file 10 confirms the mark. On O18 and O31 the two 1K returns differ from the baseline but not from each other in the same way (A SPLIT, B DISAGREE). On O48, 1K A keeps DISAGREE and 1K B gives SPLIT. For comparison,

*(The text as passed ends here. See the two notes at the head of this file.)*

**The structured fields behind it** (`selection.json`):
- `k_vs_s72`, tester A (1K mark, baseline): O4 SPLIT, AGREE; O15 SPLIT, AGREE; O18 SPLIT, AGREE; O20 AGREE, SILENT; O31 SPLIT, AGREE; O40 AGREE, SILENT; O41 SPLIT, AGREE; O45 SPLIT, AGREE.
- `k_vs_s72`, tester B: O1 DISAGREE, SILENT; O10 SILENT, AGREE; O15 SPLIT, AGREE; O18 DISAGREE, AGREE; O20 AGREE, SILENT; O31 DISAGREE, AGREE; O32 SILENT, AGREE; O38 SPLIT, AGREE; O39 SPLIT, AGREE; O40 AGREE, SILENT; O45 SPLIT, AGREE; O46 SILENT, AGREE; O48 SPLIT, DISAGREE.
- `both_1K_agree_on_non_baseline` (mark, baseline): O15 SPLIT, AGREE; O20 AGREE, SILENT; O40 AGREE, SILENT; O45 SPLIT, AGREE.
- `missing_records`, `incomplete_packets` and `table_vs_parse_checks`: empty. Every selected row has a complete packet, and the parsed marks match `table.md`.
