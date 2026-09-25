# S93: verification of draft 5

*Written on 25 September 2026 by a Claude subagent for the orchestrator. It is an independent check of draft 5 of revision 2, as committed at 8816fcf, which applied the S93 rulings to draft 4 (6cf57ae). The writer did not draft, check or apply the change list, wrote no ruling and wrote no brief. It read:*
- *the ten ruling files in `results/S93 reading rulings/`, whole;*
- *`results/S93 Reading of the replies.md`;*
- *the change list before the pass (6cf57ae, md5 b6b2ea95ea9e21ebea3316d8e9fa4b40, the text every ruling read) and after it (8816fcf, md5 c6d25ec1ccc3ea3e72136a75a794be62);*
- *the theory texts of draft 4 and draft 5, and the revision note;*
- *in the tabulation, only the rows for X01–X18 in sections 2.1, 4 and 6 (printed by a search), and its section headings;*
- *`tools/s89_apply_changes.py`, and the applier's `verify_output.txt`;*
- *file 11, read only, at the places the entries cite;*
- *the S90 verification and its script, as the template.*

*It opened no S93 reply, receipt, request, reasoning or attempt file, and not the session's key file. It wrote only this file and its check script, `results/S93 Verification of draft 5 - check script.py`. The script reads and never writes. It imports the apply tool with bytecode writing off and builds in memory. It runs all five checks and the grep, and it reports **PASS 202, FAIL 0**. Nothing was written into `authority/`.*

## Result

| check | result | in short |
|---|---|---|
| 1. Every FIX stands in the change list as its ruling gives it | **PASS** | The script takes every ruled text from its ruling file and finds each one in its entry byte for byte: 7 FIX, and the ruled lines of the 3 KEEP. X11 is entered as W61.1 with the ruling's fields. W35.5 is the X04 ruling's block, whole. Superseded texts are gone. |
| 2. Nothing else changed | **PASS** | Draft 4 of the list plus 43 listed operations gives draft 5's entries byte for byte. Each operation is a ruled text, an S93 CHECK line, a new entry or declared bookkeeping. All 12 hunks of the frame are frame or count updates, or ruled record edits. Nothing is left over. |
| 3. The theory text | **PASS** | The rebuild gives md5 7f1d8ad02adf96e27622593bd263252e, equal to the committed draft 5, and the self-test refuses both planted edits. Draft 4 against draft 5 differs in exactly L119, L223, L231, L315, L325, L526 and L582, one ruling each. |
| 4. Counts | **PASS** | Recounted: CLAIM 52, WORDING 5, ORDER 2; N 52 of M 59; K 42. The frame, the revision note and the program agree. All 52 declaration lines in the note equal their entries' declarations. |
| 5. The reading | **PASS** | All 18 items are there with the right outcomes, ruling files and md5s. Every item has its "S93 cross-examination:" line, and W59.1 has two (X09 and X10). |
| The grep | **no fault** | No hit brings back a list, a count of versions, a grade or a record of rivals. The hits are disclaimers, ordinary uses of "count", and Part XII's accuracy grades. |

## 1. The ruled texts

**How it was checked.** The script reads each ruling file's fenced blocks, keyed by the line of the opening fence, whether of three, four or five backticks.
- One block is indented, X11's declaration. It is read with its list indent removed.
- Suggested CHECK lines and other one-line texts are read from named lines, between quotation marks or backticks.
- NEW, OLD and DECLARATION must equal the entry's block or field. CHECK, REASON, CASES AT RISK, GAIN and LOSS texts must stand in the field. A CHECK line must stand as a line of its own, exactly once.
- For each FIX, the script also confirms that the text the ruling read is draft 4's.

| item · entry | ruling | what stands in the change list, byte for byte |
|---|---|---|
| X03 · W19.1 | FIX | NEW (L84): 132 words, once in draft 5 and not in draft 4. DECLARATION (L90). KIND CLAIM unchanged. The CHECK line (L122). The superseded NEW (L17) is absent from the list and from draft 5. |
| X04 · W35.1 | KEEP | OLD, NEW, KIND and DECLARATION as the ruling quotes them. These four, and REASON WORD, GAIN, LOSS and CASES AT RISK, are unchanged from draft 4. The CHECK line (L248) keeps the ruling's indent. The REASON sentence (L305) is replaced by the ruling's words (L306). **W35.5** is the ruling's five-backtick block (L259–283), whole: heading, WHERE and every field. It occurs once and stands directly after W35.4. Its OLD occurs once in draft 4, and its NEW once in draft 5. |
| X05 · W35.2 | FIX | NEW (L135) and DECLARATION (L141). KIND CLAIM and REASON WORD clarification unchanged. The CHECK line (L152). LOSS ends with the ruling's optional sentence (L158). "fails at a pair of its contract" is gone from the list and from draft 5. |
| X06 · W20.1 | FIX | NEW (L254) and DECLARATION (L259); OLD, KIND, REASON WORD, GAIN and LOSS unchanged. The CHECK line (L264). The three record edits (L267–269): (1) the finding on "active" carries the ruled words, and the old words are gone; (2) the O7 line carries the ruled words after "assigns an input and is named background"; (3) the carried-forward finding on the two readings, and REASON's matching bullet, are marked "Closed after the S93 cross-examination". |
| X09 · W59.1 "Rivals" | FIX | "as none do when" (L116) stands, and "as when" (L110) is gone from NEW. NEW opens with the ruled Rivals paragraph (L122), whole, which is draft-5 L315. DECLARATION equals the ruled whole (L154), with the third sentence replaced (L142 → L148). OLD and KIND CLAIM unchanged. The CHECK line (L184). |
| X10 · W59.1 "Problems" | KEEP | The Problems paragraph (L20) is unchanged in NEW and at L317 of both drafts. Draft-4 NEW with only the Rivals paragraph replaced gives draft-5 NEW. The CHECK line (L91). |
| X11 · W61.1 (new) | FIX | OLD (L14) and NEW (L18) as proposed. DECLARATION (L106, indent removed). STATUS applied, FILE-11 LINE 323, REASON WORD erratum and KIND CLAIM (L99–103), with the list items' closing full stops dropped as in every entry. WHERE (L101) and CASES AT RISK (L109) byte for byte. The CHECK line (L110). W61.1 stands between W59.1 and W40.1. OLD occurs once in file 11, on line 323. |
| X14 · W60.1 | KEEP | OLD, NEW, KIND, DECLARATION, REASON, CASES AT RISK, GAIN and LOSS unchanged. The CHECK line (L330). |
| X17 · W7.5 | FIX | OLD (L252), NEW (L256) and DECLARATION (L261). The heading (L265) and WHERE (L266). KIND CLAIM, REASON WORD erratum and FILE-11 LINE 518 unchanged. The CHECK line (L334). The REASON bullet (L335) and CASES AT RISK line (L336). The GAIN (L337) and LOSS (L338) sentences. "Found in draft 4", first bullet, carries L339's two sentences. NEW is draft-4 NEW, then the (RC) sentence, then one sentence of 62 words. |
| X18 · W38.1 | FIX | The *Surprise and problems* line: OLD (L74) is gone and NEW (L80) stands once. Draft-4 NEW with only that line replaced gives draft-5 NEW. OLD, KIND META and DECLARATION unchanged. The CHECK line (L88). The new clause equals the clause at draft-5 L429. |

**The ruling files.** Each of the ten ends with its ruling line: FIX for X03, X05, X06, X09, X11, X17 and X18, and KEEP for X04, X10 and X14.

**One occurrence left in place.** The phrase "as when two of their active components" still occurs once in the list, in X09's own ruled CHECK line, which quotes it.

## 2. Draft 4 against draft 5, the change list

**The entries.** The script starts from draft 4's entries (6cf57ae) and applies 43 listed operations. Each operation names its source.

| where | operations | source |
|---|---|---|
| W19.1, W35.2, W20.1, W59.1, W7.5, W38.1 | NEW and DECLARATION (and W7.5's OLD, heading and WHERE) | the ruled texts, as in check 1 |
| W35.1 | the REASON sentence | X04, L305–306 |
| W35.2 | LOSS | X05's optional sentence, L158 |
| W20.1 | the O7 line; REASON's closed bullet | X06, L269; the applier's closing words |
| W7.5 | the REASON bullet, CASES AT RISK line, and GAIN and LOSS sentences | X17, L335–338; GAIN and LOSS are joined after "After the S93 cross-examination: " |
| W34.1 and W59.1 | "N7 (O59)" becomes "N7 (O58)", with a dated note | bookkeeping |
| 17 CHECK lines | the ruled lines of X03, X04, X05, X06, X09, X10, X14, X17 and X18, and the eight "upheld by both readers" lines (X11's line is in the new W61.1) | the rulings; the reading |
| W35.5 and W61.1 | inserted after W35.4 and after W59.1 | the X04 ruling's block; X11's ruled fields |

**What the operations give.**
- **Byte for byte.** The rebuilt entries section equals draft 5's.
- **Order.** Draft 4's order holds, with the two insertions.
- **Everything else is untouched:** the lines before the first entry, the meta record after the last, and every entry not named.
- **Scope.** OLD, NEW, KIND or DECLARATION changed only in W19.1, W35.2, W20.1, W59.1, W7.5 and W38.1. In all, 16 entries changed and 2 were added.

**W61.1's fields beyond the ruling.** The following are the applier's bookkeeping, declared in the reading's section 6:
- the title;
- GROUP "S93 (entered after the S93 cross-examination; not one of the drafting groups)";
- ITEM;
- the first CHECK line;
- REASON;
- GAIN / LOSS.

They say what the ruling says. REASON's file-11 pointers were checked: L105 holds "An edit that sets a port replaces the component assigning that port", and L273 holds the reversed-calculation sentence.

**The frame.** Every hunk is accounted for:

| hunk (new lines) | what it is |
|---|---|
| 3 | the header, DRAFT 5 |
| 5 | the opening paragraph: the draft-5 sentence is added, and its last sentence is brought up to date |
| 7 | the italic record, with one pass appended |
| 19–20 | What this is: a paragraph on draft 5 |
| 25 | Counts: the theory entries (recounted in check 4) |
| 29 | Counts, "The checks": the S93 sentence appended, and "None has been cross-examined." put in the past tense ("… when draft 4 was made") |
| 148 | the S90 paragraph, with "(After S93: …)" appended |
| 188–216 | the new section "After the cross-examination (S93)" (its table is checked in check 4) |
| 236 | the held items, with "(After S93: …)" inserted |
| 263–264 | X06's record edits: the finding on "active" (the ruled words) and the finding on the two readings (closed) |
| 268 | X17: "Found in draft 4", first bullet, with the ruling's two sentences |
| 304–331 | the new section "Carried forward after S93", which says none of it is an edit |

**Beyond the kinds the instruction lists.** The following were found; each is either ruled or declared:
- X06's edits to the "active" finding and to the O7 line, and X17's heading, WHERE, REASON bullet and CASES AT RISK line. Each ruling asks for these.
- X17's "Found in draft 4" sentence. The ruling offers it ("can say"), and the frame declares it under "Also changed with the rulings".
- W61.1's title, GROUP, ITEM and first CHECK line. The reading declares these.
- The frame's tense change in "The checks", and the two "(After S93: …)" parentheses. These are frame updates.

## 3. The theory text

**The command.** `python3 -B Semantics/tools/s89_apply_changes.py <scratchpad>/draft5_full.md --theory-output <scratchpad>/draft5_theory.md --self-test` exited 0. It reported:
- 67 entries parsed: 62 applied (59 theory and 3 meta), 5 record-only and 0 held;
- CLAIM 52, ORDER 2 and WORDING 5;
- every OLD, locator and anchor once in file 11, with no overlap;
- N = 52 of M = 59, and K = 42;
- 57 diff hunks, each inside an entry;
- both planted edits refused, and the clean draft passed.

**The outputs.**
- **The theory text.** Its md5 is 7f1d8ad02adf96e27622593bd263252e, the committed draft 5, with 12,650 words by the runner's count.
- **The full draft.** With `--date "draft of 25 September 2026, not frozen"`, it has md5 40cefd9b586f43762e0a58c54e843cb0 and 30,426 words, as the frame states.
- **By `wc -w`.** The counts are 12,622 and 30,382 in the C locale. In a UTF-8 locale they are 12,650 and 30,426, the same as the runner's count.

The script repeats the build in memory, with the same results.

**Cross-checks.** Also built in memory:
- **Draft 4 of the list.** It gives draft 4's theory text and a full md5 of 57c94ab5f0bada4e9443904253dc2db3, with 29,864 words, 55 hunks and N 51 of M 57. This is the reading's draft-4 column.
- **Draft 4 plus W35.5 alone.** It gives theory md5 5f7888dba8be366f5caed39672bdd096, as the X04 checker found.
- **Draft 4 plus the X17 fix alone.** It gives f7fb94d3ad26c089c6abbf60b83baf67 and 12,639 words, as the X17 checker found.

**Draft 4 (md5 fc55b470c63cd4b3c27d6aa64d8d8c17) against draft 5.** Both have 632 lines. Exactly seven differ. Draft 4, with each entry's draft-4 text replaced by its draft-5 text, gives draft 5 byte for byte:

| line | entry | ruling | change |
|---|---|---|---|
| 119 | W19.1 | X03 | "an active component \(k\)" |
| 223 | W35.2 | X05 | "fails at an actually occurring pair" |
| 231 | W20.1 | X06 | "boundary conditions"; "including any of them that" |
| 315 | W59.1 | X09 | "as none do when" |
| 325 | W61.1 | X11 | "but not the calculation's \(L\)" |
| 526 | W7.5 | X17 | one sentence of 62 words after "(RC), (U1)–(U3) depend on all of the above." |
| 582 | W35.5 | X04 (companion) | "a violation of a selected transport at" |

X10 and X14 are KEEP and change no line. X18 changes only the sources note, which is not part of the theory text.

## 4. Counts and declarations

**The recount.** The script counts the entries itself:
- 67 entries: 62 applied (3 of them META) and 5 record-only.
- The 59 theory entries: CLAIM 52, WORDING 5 and ORDER 2, so N = 52 of M = 59.
- K = 42 layer-2 locators, from the one entry that carries them.
- By group: A 14 of 18, B1 14 of 15, B2 11 of 11, C 10 of 12, H 2 of 2 and S93 1 of 1. The group names "C; edited 25 September (group H)" count as C.

**Where the figures agree.**
- **The frame.** They match its Counts line, its layer-2 line, its build paragraph and the program's summary.
- **The revision note:**
  - section 1: "N = 52 of M = 59 changes; K = 42 places", "52 of the 59 changes" and "42 places";
  - section 5's Counts line.

**The declarations.**
- **The list.** The 52 lines "- File 11, line n: …" in the note's section 1 equal, in order and byte for byte, the declarations of the 52 CLAIM entries, sorted by the place of their OLD in file 11.
- **The NOTE block.** The program's NOTE block occurs whole in section 1.
- **The six changed or added lines** carry their entries' present declarations: W19.1 (line 121), W35.2 (225), W20.1 (233), W59.1 (317), W61.1 (323) and W7.5 (518).

**The note's other tables.**
- **The map (section 5).** It has 59 rows. Each has the R2 number the program gives, and the entry's file-11 line, reason, expected ruling and "declared".
- **Its S93 column.** It gives each of the 17 items that have an R2 number with its outcome. W35.5 reads "— (added after S93, from the X04 ruling)".
- **The undeclared entries.** They are the 7 non-CLAIM entries, with their kinds.
- **The layer-2 column (section 2).** It equals the program's, in 42 rows.

**The frame's S93 table.** Its 10 rows give the R2 numbers, file-11 lines and rulings the entries and rulings give (R2-08, R2-12, R2-13, R2-15, R2-25 twice, R2-26, R2-30 and R2-51, and "meta" for X18).

## 5. The reading of the replies

**The table.** The reading's table has X01 to X18, with the expected outcomes:
- **FIX:** X03, X05, X06, X09, X11, X17 and X18;
- **KEEP:** X04, X10 and X14;
- **upheld by both readers; not thereby confirmed:** X01, X02, X07, X08, X12, X13, X15 and X16.

Its "In all" sentence agrees.

**The ruling files.** Each of the ten is named, its md5 matches the file, and its last line agrees. The eight upheld items name none.

**Against the tabulation.** The entry, part and closing lines of all 18 agree with the tabulation's section 2.1.

**The CHECK lines.** Each of the 18 items has its "S93 cross-examination:" line in its entry's CHECK field.
- **The eight upheld items.** Each has exactly one line, "upheld by both readers (s93_xexam_atria_<p>, s93_xexam_mimo_<p>); not thereby confirmed.", with the right part: F for W37.1; D for W36.1, W34.1 and W33.1; I for W40.1; J for W24.1 and W22.1; K for W6.3.
- **W59.1.** It carries two lines, X09's and X10's.
- **Other entries.** The only other entry with such a line is W35.5, whose CHECK is the X04 ruling's.

## The grep

The search was word-bounded: count(s), counted, counting, number of, list of, grade(s/d), grading, rank(s/ed/ing), record(s) of, enumerat-. It covered the draft-5 theory text and the lines draft 5 added to the change list.

**Theory text.** No hit brings back a list, a count of versions, a grade or a record of rivals.
- **Disclaimers:**
  - L25 and L522: "a ranking of thinkers", "no ranking of thinkers";
  - L315: "No list of all rivals is supposed";
  - L317: "Nothing here counts rivals, grades a candidate or ranks candidates";
  - L369: "with no record of which candidates failed before";
  - L441: "(P) does not rank alternatives".
- **Ordinary uses of "count":** L17 "counts against" and "what would count"; L69 "cannot count as explanation"; L526 "counts only when the account uses it".
- **The physical module's accuracy grades,** for (CT3) and (CT4), with nothing to do with grading candidates: L479 and L517.
- **L495:** "A finite list of failures is not a barrier proof".
- **The changed lines.** Two of the seven carry hits, L315 and L526. Both hits stand in wording that draft 4 already had. The words the S93 fixes wrote have no hit, and neither does X18's new line.

**Change list, added lines.** These hits are also harmless:
- **Bookkeeping:** word counts, "the cumulative list of edits" and "the record of that pass".
- **"Counts as established"** in the (c2) lines, and "is not counted" in the (d) losses.
- **Disclaimers copied with the X09 fix:** "No list of all rivals is supposed" and "Nothing here counts, grades or ranks".
- **X14's carried-forward condition:** "a record of rescues would not detect it".
- **X17's GAIN:** "not on a list, count, grade or record".

## Discrepancies and observations

**Discrepancies against the five checks: none.**

**Observations.** None bears on a ruled text or on the theory text.
- **The reading's section 7 is loose.** It says "the change list's entries differ from draft 4's only in W19.1, W35.2, W20.1, W59.1, W7.5 and W38.1". That is true of OLD, NEW, KIND and DECLARATION, as the applier's `verify_output.txt` puts it ("fields changed"). Counting whole entries, 16 changed: the other 10 gained CHECK lines or bookkeeping.
- **W20.1's O7 line reads as a run-on.** After the ruled insertion it reads "… is named background where the candidate does not offer it as doing the work; offered, it is a commitment, and O7 holds on both identifications (W20.2), and the salt's action on the ice is the commitment." This is exactly what the X06 ruling asks. It is record-only, and a later tidy could split the sentence.
- **W7.5's LOSS now has two growths.** It reads "None; the order grows by two sentences. After the S93 cross-examination: The order grows by one sentence of 62 words." The capital "The" is the ruling's. Cosmetic.
- **"Upheld by both readers" matches nine lines, not eight.** W60.1's S93 line is the X14 checker's own wording and begins "upheld by both readers (part C)", although X14 went to a checker and was ruled KEEP. So a search for "upheld by both readers" finds nine CHECK lines. Only eight end "not thereby confirmed".
- **Closing words.** The words that mark the X06 findings closed ("**Closed after the S93 cross-examination:** …") and the dated notes on N7 are the applier's. The rulings ask only that the findings be closed, and the N7 slip was noted by the reading rule.
- **`wc -w` depends on the locale.** The frame's `wc -w` figures (12,622 and 30,382) are the C locale's. A UTF-8 locale gives the runner's figures.

Dated 25 September 2026.
