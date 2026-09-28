# S104: Round 2 (the maths) — tabulation of the replies, before any ruling

*Written by the tabulating agent of rule 4 (a fresh Opus 5.5 agent that built nothing of this round and had read no reply before this file was created), on 28 September 2026. Created at once and filled as it goes (lesson S28). It rules on nothing: it records what each reader said, copies each proposal exactly, names the lines each proposal would change, compares each quotation with the text under review, and says, under rule 5 and the two addenda, whether each item goes to a checker. No theory text, brief, reply, reading rule, addendum or committed maths file was written; nothing in `authority/` was written. This file obeys decision S23 except where it quotes the text, a reply, a brief, the external document, the case card or the owner.*

## How this file was made

- **Read first, whole:** the reading rule (`results/S104 Round 2 - how the replies will be read, written before sending.md`) and its two addenda (the external cross-examination; the creative transport case); the owner's decisions S20 to S39 in `records/Semantics - Decisions.md`.
- **The text under review:** `tests/103 The semantics, standing alone, after round 1.md`, md5 checked: f31ebb1f050783f1a84f6136cec20fcd (as the rule states), 632 lines, read whole.
- **The briefs:** the seventeen part briefs in `tests/`; the items of each part (definitions and encodings printed in section 3, claims, inventions in full, U- and H-entries, NF entries, round-1 matters and changes) and the lines each quotes were taken from the briefs by program and checked by reading.
- **The replies:** for each of the 34 tags, the receipt, then the `.response.txt` only. The replies were read whole. Proposals are copied from the reply files by program, byte for byte, between fence lines (a reader's own fence lines are not repeated; a reader's proposal written as a quoted line `> Lnnn | …` is copied whole, with its `>`). Each proposal is given an id: the reader's letter (M Mimo, G GLM), the part, and the block's number in that reply (for example `G1-B3`: GLM, part 1, block 3). "Reply lines" are line numbers of the `.response.txt`.
- **Quotations:** every quotation in the reply lines a point rests on (text in double quotation marks, or a quoted line `> Lnnn | …` that stands in the text) was compared by program with the text under review, after normalizing markup (the text's `\(…\)` and `\operatorname` and the like, Greek letters and symbols written in Unicode or in markup, spacing and punctuation); " … " joins fragments that must stand in one line. Each is recorded "found at L…" or "not found in the text"; where not found in the text, the part brief was searched as well and the record says "found in the brief" where it stands there (the maths' own wording, the owner's words, or the search's printouts). A quotation of a single word is compared too; one that stands on many lines is recorded with its first lines found.
- **What goes to a checker** follows rule 5 and the addenda: an item goes when any point challenges it (the maths says other than the sentence; a counterexample tells against the text; the text settles an invention or should carry wording that settles it; a counterexample to a claim that held; a proposed change for a round-1 matter or change; any other proposed change to the text; in doubt, it goes), and the twelve counterexamples the second check reproduced go whether raised or not. The external reader's findings that challenge the text, and the case card's C01 to C07 and C11, go too. A point that only says the maths should change (a register entry, a formal statement) is still a point that the maths says other than the sentence, and sends its item.
- **Marks** (rule 9; addendum points 8; decisions S33, S34): **PARKED** where a point is about what hard to vary covers; **OWNER QUESTION** where a point would move where values are placed, turns on the reading of "argument" (L8, L397; decision S23), or turns on a choice the owner has not made. Marked, not weighed.
- **Lines** given for an item going to a checker are the lines its proposals would change; for an item whose points change no line of the text, the lines its claim, definition or invention formalizes (the lines the brief quotes for it).
- Nothing here is a ruling: "challenges" names what a point does, not whether it holds.

## 1. Receipts (rule 2)

Each receipt was read (`.receipt.json`), then the reply (`.response.txt`) only; no reasoning file, request file or attempt file was opened. Every tag is pass 1: no `_pass2` or `_pass3` file exists in the returns folder. The last non-blank line of every reply was checked by program.

| tag | accepted | pass | how | last line END OF REPORT | words (`wc -w` count) |
|---|---|---|---|---|---|
| `s104_maths_mimo_1` | accepted | 1 | finish "stop"; 1 attempt(s) | yes | 1373 |
| `s104_maths_mimo_2` | accepted | 1 | finish "stop"; 1 attempt(s) | yes | 2007 |
| `s104_maths_mimo_3` | accepted | 1 | finish "stop"; 1 attempt(s) | yes | 2022 |
| `s104_maths_mimo_4` | accepted | 1 | finish "stop"; 1 attempt(s) | yes | 2237 |
| `s104_maths_mimo_5` | accepted | 1 | finish "stop"; 1 attempt(s) | yes | 2407 |
| `s104_maths_mimo_6` | accepted | 1 | finish "stop"; 1 attempt(s) | yes | 2627 |
| `s104_maths_mimo_7` | accepted | 1 | finish "stop"; 1 attempt(s) | yes | 2101 |
| `s104_maths_mimo_8` | accepted | 1 | finish "stop"; 1 attempt(s) | yes | 1672 |
| `s104_maths_mimo_9` | accepted | 1 | finish "stop"; 1 attempt(s) | yes | 2779 |
| `s104_maths_mimo_10` | accepted | 1 | finish "stop"; 1 attempt(s) | yes | 1899 |
| `s104_maths_mimo_11` | accepted | 1 | finish "stop"; 1 attempt(s) | yes | 1920 |
| `s104_maths_mimo_12` | accepted | 1 | finish "stop"; 1 attempt(s) | yes | 2171 |
| `s104_maths_mimo_13` | accepted | 1 | finish "stop"; 1 attempt(s) | yes | 2063 |
| `s104_maths_mimo_14` | accepted | 1 | finish "stop"; 2 attempt(s); attempt 1 ended with no HTTP status (status 0, no answer: a connection failure, not counted against the reader, rule 2), attempt 2 accepted | yes | 2037 |
| `s104_maths_mimo_15` | accepted | 1 | finish "stop"; 1 attempt(s) | yes | 2460 |
| `s104_maths_mimo_16` | accepted | 1 | finish "stop"; 1 attempt(s) | yes | 1948 |
| `s104_maths_mimo_17` | accepted | 1 | finish "stop"; 1 attempt(s) | yes | 2613 |
| `s104_maths_glm_1` | accepted | 1 | 1 attempt(s); connection failures 0; answers rejected 0; rule "the reply's last non-blank line carries END OF REPORT" | yes | 2756 |
| `s104_maths_glm_2` | accepted | 1 | 1 attempt(s); connection failures 0; answers rejected 0; rule "the reply's last non-blank line carries END OF REPORT" | yes | 2413 |
| `s104_maths_glm_3` | accepted | 1 | 1 attempt(s); connection failures 0; answers rejected 0; rule "the reply's last non-blank line carries END OF REPORT" | yes | 2503 |
| `s104_maths_glm_4` | accepted | 1 | 1 attempt(s); connection failures 0; answers rejected 0; rule "the reply's last non-blank line carries END OF REPORT" | yes | 2430 |
| `s104_maths_glm_5` | accepted | 1 | 1 attempt(s); connection failures 0; answers rejected 0; rule "the reply's last non-blank line carries END OF REPORT" | yes | 2280 |
| `s104_maths_glm_6` | accepted | 1 | 1 attempt(s); connection failures 0; answers rejected 0; rule "the reply's last non-blank line carries END OF REPORT" | yes | 2514 |
| `s104_maths_glm_7` | accepted | 1 | 1 attempt(s); connection failures 0; answers rejected 0; rule "the reply's last non-blank line carries END OF REPORT" | yes | 2335 |
| `s104_maths_glm_8` | accepted | 1 | 1 attempt(s); connection failures 0; answers rejected 0; rule "the reply's last non-blank line carries END OF REPORT" | yes | 2013 |
| `s104_maths_glm_9` | accepted | 1 | 1 attempt(s); connection failures 0; answers rejected 0; rule "the reply's last non-blank line carries END OF REPORT" | yes | 2425 |
| `s104_maths_glm_10` | accepted | 1 | 1 attempt(s); connection failures 0; answers rejected 0; rule "the reply's last non-blank line carries END OF REPORT" | yes | 2479 |
| `s104_maths_glm_11` | accepted | 1 | 1 attempt(s); connection failures 0; answers rejected 0; rule "the reply's last non-blank line carries END OF REPORT" | yes | 2122 |
| `s104_maths_glm_12` | accepted | 1 | 1 attempt(s); connection failures 0; answers rejected 0; rule "the reply's last non-blank line carries END OF REPORT" | yes | 2156 |
| `s104_maths_glm_13` | accepted | 1 | 1 attempt(s); connection failures 0; answers rejected 0; rule "the reply's last non-blank line carries END OF REPORT" | yes | 2564 |
| `s104_maths_glm_14` | accepted | 1 | 1 attempt(s); connection failures 0; answers rejected 0; rule "the reply's last non-blank line carries END OF REPORT" | yes | 2096 |
| `s104_maths_glm_15` | accepted | 1 | 1 attempt(s); connection failures 0; answers rejected 0; rule "the reply's last non-blank line carries END OF REPORT" | yes | 2772 |
| `s104_maths_glm_16` | accepted | 1 | 1 attempt(s); connection failures 0; answers rejected 0; rule "the reply's last non-blank line carries END OF REPORT" | yes | 1773 |
| `s104_maths_glm_17` | accepted | 1 | 1 attempt(s); connection failures 0; answers rejected 0; rule "the reply's last non-blank line carries END OF REPORT" | yes | 2558 |

All 34 calls accepted on pass 1; every reply ends with END OF REPORT. No item of any part is "not examined" by either reader (rule 7's second and third forms do not arise).

## 2. Part by part, item by item

