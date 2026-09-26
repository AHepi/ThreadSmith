# S90 parts: how they will be read

*Written by a Claude subagent for the orchestrator on 23 September 2026, from 21:29 UTC, before any part was sent, and committed in the same commit as the five part briefs, the job list and the copy of the draft. When it was written, the folder `results/S90 Cross-examination - revision 2 draft - returns/parts/` did not exist. The reasoning files of the failed S90 call were committed without being read, and no S87, S88 or S90 reply was opened.*

## Why parts

**The single S90 call failed.** `s90_xexam_atria` sent the S90 brief (48 changes, 25,790 words by `wc -w`) to Atria at medium effort with max_tokens 65,536. It was asked at 19:02:13 UTC and ended at 21:20:55 UTC as failed after 6 attempts:

| attempt | status | max_tokens | seconds | finish |
|---|---|---|---|---|
| 1 | none | 65,536 | 1,802.5 | none |
| 2 | none | 65,536 | 1,618.3 | none |
| 3 | none | 65,536 | 1,802.3 | none |
| 4 | none | 65,536 | 607.9 | none |
| 5 | 200 | 65,536 | 1,103.8 | length, no content, not accepted |
| 6 | 200 | 65,536 | 1,127.7 | length, no content, not accepted |

The error note, the receipt and the attempt files were committed at 9a9d4bb. Under rule 4 of the S90 rule (`results/S90 How the cross-examination of the revision 2 draft will be read - written before sending.md`) the call supports nothing, and it is not rerun. This note is the new note, written before sending, that rule asks for.

**Smaller briefs.** Atria failed on 26,000 words with 48 changes. Mimo's S88 parts, of about 10,000 words each, came back. So the cross-examination is rebuilt as five parts of at most 18,000 words, each with its own group of changes, and each part is sent to both Atria and Mimo.

## What is sent

- **Five part briefs**, in `tests/`. Together they cover all 55 changes of the current draft, each change in exactly one part (the build checks this). They include the seven entries for Derivation 2, (T2) and Γ (W19.1–W19.3, W20.1–W20.3 and W31.1). Those were written after S88 was settled, from the settled positions (3ebb6d8), and entered in the change list at 587eebf. No outside reader has seen them.
- **To both Atria and Mimo**, ten calls in all. The job list is `tools/s90_jobs - revision 2 draft in five parts.json` (sha256 43d62bcf49bcb02445d5bd300fcf6f76b931847f37ee6db3b4cb5fce5877f80a), run by `tools/s87_run.py`. For each part X it holds `s90_xexam_atria_X` (Atria, effort medium, ladder 65,536 and 65,536) and `s90_xexam_mimo_X` (Mimo, effort medium, ladder 131,072 and 131,072). Every job has 6 attempts, `max_rejects` 3 and `max_pass` 1. Medium is the map's "audit" effort for both. The returns go to `results/S90 Cross-examination - revision 2 draft - returns/parts/`. A dry run of the list was checked. It needed no keys and sent nothing: 10 calls, 5 to each provider, every one pass 1 of at most 1, with no file already in the way.
- **Each part is sent whole**, as the one user message, with no system text.

| part | file in `tests/` | changes | ids | words (runner / `wc -w`) | md5 | cases given / named |
|---|---|---|---|---|---|---|
| A1 | `S90 Cross-examination - part A1, errata and pointers, Parts 0 to VI.md` | 9 (CLAIM 6) | R01, R05, R08, R09, R15, R16, R17, R19, R20 | 17,872 / 17,834 | 1364c50fdc388e091552bbf41b538d76 | 24 / 25 |
| A2 | `S90 Cross-examination - part A2, errata and pointers, Parts VIII to XVI.md` | 9 (CLAIM 8) | R26, R27, R28, R29, R41, R43, R51, R54, R55 | 17,750 / 17,709 | 234bf749788fc3ab3ddcb1e06e249f98 | 23 / 23 |
| B1 | `S90 Cross-examination - part B1, declared inputs.md` | 15 (CLAIM 13) | R02, R03, R04, R10, R18, R38, R39, R44, R45, R46, R47, R48, R49, R50, R53 | 17,930 / 17,884 | 130a5eace514ebb02b736d12a311ade2 | 20 / 45 |
| B2 | `S90 Cross-examination - part B2, ownership, repair, selection, newness.md` | 11 (CLAIM 11) | R11, R22, R31, R32, R33, R35, R36, R37, R40, R42, R52 | 17,834 / 17,790 | d214f495e0b9fcac4f423d522bee0d37 | 31 / 45 |
| C | `S90 Cross-examination - part C, source-derived clarifications.md` | 11 (CLAIM 10) | R06, R07, R12, R13, R14, R21, R23, R24, R25, R30, R34 | 17,969 / 17,929 | 2183faa5005b112347f484b6c8ace196 | 17 / 53 |

Words are counted by the runner (Python's `split()`) and by `wc -w` in the C locale. Every part is within 18,000 by both counts. Each part comes close to the limit because the described situations fill what the rest leaves (see "The cases in section 5").

## How the change list was split

The list's own GROUP field gives four groups: A 18 entries, B1 15, B2 11 and C 11. The list puts all seven held entries in group A ("Counts": "All seven are group A"). Group A owns every paragraph that W19, W20 and W31 change (L121, L233, L257, L289, L361, L552–558 and L620), so there is no group H. W20.1–W20.3 go with A, not with B1, because that is where the list puts them.

Four groups would make four parts, one of them 18 changes. To get five parts of similar size, group A is cut in two in the order of the text, nine changes each:

- **A1, errata and pointers, Parts 0 to VI:** W37.1, W8.1, W19.1, W30.1, W20.1, W39.1, W20.2, W9.1 and W20.3.
- **A2, errata and pointers, Parts VIII to XVI:** W24.1, W31.1, W22.1, W22.2, W25.1, W25.2, W19.2, W10a.1 and W19.3 + W10(b).1.
- **B1, declared inputs** (15), **B2, ownership, repair, selection, newness** (11) and **C, source-derived clarifications** (11) are the list's groups as they stand.

The cut keeps together the two pairs of entries that share a paragraph: W19.1 and W30.1 at L121, and W39.1 and W20.2 at L257. It also keeps the three W20 entries together, and puts W19.2, W10a.1 and W19.3 (Derivations 2 and 10) in one part with W31.1. It does separate W19.1, the sentence after (K), from W19.2, which uses that sentence. Every part carries the whole revised text, so the reader of A2 reads W19.2 with W19.1's sentence in place, but is not told that the sentence is new. A cut into the seven held entries and the other eleven would have made a group H that the list does not have, and would have split both shared paragraphs.

The sizes are 9, 9, 15, 11 and 11 changes. B1 is the largest, and it is kept whole because it is the list's own group.

## What each part carries

Each part follows the S90 brief section by section, with these differences.

- **Section 1** is the S90 brief's introduction, reworded to say that the revised text makes 55 changes and that this cross-examination covers only the ones listed in section 3, named by their ids. It says that the other changes are examined separately and are not listed. The reader is to read them as part of the revised text and leave them out of the report, except where a listed change depends on one of them or pulls against it. The S90 paragraph on the three repairs "drafted separately" is dropped, because they are now in the revised text. Like the S90 brief, the introduction names no model, file number, record or round.
- **Section 2** is the whole revised text, between the same two marker lines. It is byte-identical in every part to the regenerated draft (md5 9aecf2f30ce0b4523606b2b8409fdf37).
- **Section 3** gives only the part's changes, in the S90 form: the id; the Part and heading, in the words the program uses for layer 1 of the record; the revised-text line or lines of NEW; KIND and REASON WORD; the DECLARATION for a CLAIM entry, and "none" for a WORDING or ORDER entry; OLD and NEW byte for byte; and the section-5 cases among those the entry's CASES AT RISK names, as ids only.
- **Section 4** gives tasks (a)–(d) in the S90 brief's words, for the listed changes only. The closing lines read exactly `Rnn: STANDS` or `Rnn: FALLS — <the reason in a phrase>`, one per contested change, then `OVERALL: SOUND` or `OVERALL: NEEDS REPAIR`, and last `END OF REPORT`. The reply is to stay under about 3,000 words (S90 asked for 6,000 over 48 changes).
- **Section 5** gives the described situations, verbatim (see below).
- **Withheld**, as in S90: every W-number; the entries' REASON, CHECK, GAIN and LOSS, and the direction the drafters expect on each case; decisions D1–D11; the meta entries W1.1, W38.1 and W1.2; and the record-only entries W3.1–W3.5. The list of the other parts' changes is withheld too.
- **Words.** The build checked each part's frame, which is everything outside the revised text, the fenced wordings and the case texts. It found none of the marker words ("Revision 2", "revision record", "file 13", "Deutsch", "Marletto"), no W-number, log number, file number or "R2-", no model name, and neither "round" nor "revision". The case texts were checked for the same words. The only hits are "round" in its ordinary sense ("round the sun", "round Earth") in N1 and N4. As in S87, S88 and S90, the only name of a model in any part is the theory's own title inside the revised text.

## The ids

R*nn* numbers the 55 theory entries in file-11 order. The program numbers the entries of layer 1 of the record, R2-*nn*, in the same order (`tests/Revision 2 - revision note, draft of 23 September.md`, section 5), so R*nn* = R2-*nn*. **The ids are not the S90 brief's C-numbers.** C01–C07 are R01–R07. From C08 on, each C-number is a higher R-number, and the seven new entries have no C-number. A letter other than C was chosen so that no reply to a part can be read as a reply to the S90 brief. The map from the old S90 C-numbers to the entry ids, the revision note's "S90 brief" column, is kept here:

| id | entry | old S90 id | part | file-11 line | revised-text line | kind | cases given in the part |
|---|---|---|---|---|---|---|---|
| R01 | W37.1 | C01 | A1 | 15 | 13 | ORDER | O11, N9, N11 |
| R02 | W6.1 | C02 | B1 | 27 | 25 | CLAIM | O6, O8, O12, O21, O27, O35, O40, O50, N11 |
| R03 | W7.1 | C03 | B1 | 33 | 31 | CLAIM | O12, O35, O37 |
| R04 | W58(ii).1 | C04 | B1 | 33 | 31 | WORDING | — |
| R05 | W8.1 | C05 | A1 | 63 | 61 | ORDER | O24, O48 |
| R06 | W36.1 | C06 | C | 71 | 69 | CLAIM | O8, O15, N1, N2, N3, N22 |
| R07 | W45.1 | C07 | C | 77 | 75 | CLAIM | O14 |
| R08 | W19.1 | — | A1 | 121 | 119 | CLAIM | O9, O10, O22, N25 |
| R09 | W30.1 | C08 | A1 | 121 | 119 | CLAIM | O10, O22, N16 |
| R10 | W57.1 + W32(b).1 | C09 | B1 | 161 | 159 | CLAIM | O1, O5, O8, O33, N7 |
| R11 | W17.1 | C10 | B2 | 197 | 195 | CLAIM | O11, O24, O48, N5 |
| R12 | W35.1 | C11 | C | 219–223 | 217–221 | CLAIM | N18 |
| R13 | W35.2 | C12 | C | 225 | 223 | CLAIM | O23, N18 |
| R14 | W35.4 | C13 | C | 227 | 225 | WORDING | N18 |
| R15 | W20.1 | — | A1 | 233 | 231 | CLAIM | O2, O5, O7, O36, O45, O46, O47, N1 |
| R16 | W39.1 | C14 | A1 | 257 | 255 | CLAIM | O2, O4, N2, N3, N8, N25 |
| R17 | W20.2 | — | A1 | 257 | 255 | CLAIM | O2, O4, O5, O7, O33, O36, O45, O46, O47, N1, N3, N23, N25 |
| R18 | W11.1 | C15 | B1 | 271 | 269 | CLAIM | O33, N17 |
| R19 | W9.1 | C16 | A1 | 275 | 273 | WORDING | O2, N1 |
| R20 | W20.3 | — | A1 | 289 | 287 | CLAIM | O36, O45, O46, O47, N1 |
| R21 | W58(i).1 | C17 | C | 301 | 299 | CLAIM | O45, N1 |
| R22 | W28.1 | C18 | B2 | 309 | 307 | CLAIM | O13, O20, O25, O39, O45, O52 |
| R23 | W34.1 | C19 | C | 315 | 313 | CLAIM | N4, N5 |
| R24 | W33.1 | C20 | C | 315 | 313 | CLAIM | O8, O45, N1, N2 |
| R25 | W40.1 | C21 | C | 337 | 335 | CLAIM | N22 |
| R26 | W24.1 | C22 | A2 | 351 | 349 | WORDING | N20 |
| R27 | W31.1 | — | A2 | 361 | 359 | CLAIM | N20 |
| R28 | W22.1 | C23 | A2 | 373 | 371 | CLAIM | O27, O40, O50, N11 |
| R29 | W22.2 | C24 | A2 | 379 | 377 | CLAIM | O3, O27, O40, O50, N11 |
| R30 | W41.1 | C25 | C | 401 | 399–403 | CLAIM | O14, O15, O23, O32, N21 |
| R31 | W21.1 | C26 | B2 | 405 | 407 | CLAIM | O3, O11, O18, O27, O31, N4, N10, N15, N21 |
| R32 | W13.1 | C27 | B2 | 419 | 421 | CLAIM | O17, O30, O51 |
| R33 | W13.2 + W12.2 | C28 | B2 | 419 | 421 | CLAIM | O17, O21, O27, O30, O40, O41, O49, O50, N11, N13, N15 |
| R34 | W35.3 | C29 | C | 421 | 423 | CLAIM | O12, O27, N18, N19 |
| R35 | W23.1 | C30 | B2 | 427 | 429 | CLAIM | O13, O20, O25, O26, O39, O52, N10 |
| R36 | W5.1 | C31 | B2 | 433 | 435 | CLAIM | O13, O20, O25, O26, O35, O39, O52 |
| R37 | W23.2 | C32 | B2 | 445 | 447 | CLAIM | O13, O20, O39, N10 |
| R38 | W6.2 | C33 | B1 | 447 | 449 | CLAIM | O12, O35 |
| R39 | W6.3 | C34 | B1 | 447 | 449 | WORDING | — |
| R40 | W12.1 | C35 | B2 | 465 | 467 | CLAIM | O3, O14, O17, O18, O21, O30, O31, O40, O41, O49, O50, O51, N11, N13, N15, N21 |
| R41 | W25.1 | C36 | A2 | 471 | 473 | CLAIM | O1, O42, O49, O52, N24 |
| R42 | W17.2 | C37 | B2 | 473 | 475 | CLAIM | O11, O24, O48, N5 |
| R43 | W25.2 | C38 | A2 | 487 | 489 | CLAIM | O49, N24 |
| R44 | W7.2 | C39 | B1 | 512 | 514 | CLAIM | O12 |
| R45 | W6.4 + W14.1 | C40 | B1 | 514 | 516 | CLAIM | O1, O5, O6, O8, O12, O21, O26, O27, O35, O40, O50, N11, N23 |
| R46 | W7.3 | C41 | B1 | 516 | 518 | CLAIM | O1, O5, O8, O21, N11, N13, N15, N21 |
| R47 | W7.4 | C42 | B1 | 518 | 520 | CLAIM | O37 |
| R48 | W7.5 | C43 | B1 | 518 | 520 | CLAIM | O35, O37 |
| R49 | W15.1 | C44 | B1 | 526 | 528 | CLAIM | O1, O12, O21, O27, O35, O50 |
| R50 | W11.2 | C45 | B1 | 528 | 530 | CLAIM | O33, N17 |
| R51 | W19.2 | — | A2 | 552–558 | 554–562 | CLAIM | O10, O11, O18, O24, O36, O45, O46, N15, N17, N25 |
| R52 | W17.3 | C46 | B2 | 562 | 566 | CLAIM | O24, O48, N5 |
| R53 | W7.6 | C47 | B1 | 588 | 592 | CLAIM | — |
| R54 | W10a.1 | C48 | A2 | 616 | 620 | CLAIM | O24, O48 |
| R55 | W19.3 + W10(b).1 | — | A2 | 620 | 624 | CLAIM | O43 |

## The cases in section 5

- **The pool.** For each part, the pool is every case named in the CASES AT RISK field of that part's entries. O53–O75 are read as the N-cases they will become under D8. N6 and N14 (set aside under D8) and D3-T (O76, not yet agreed) are not given.
- **The order they were added in**, as in S90 but counted over the part's own entries. Each case was ranked first by the number of the part's entries that have a sentence on it speaking of a possible move: "toward", "away", "watched", "may move", "could move" or "can move", SPLIT, "→" or "risk", but not "no move is expected", "moves no mark" or "no case". It was ranked next by the number of the part's entries that name it. Cases were added in that order while the part stayed within 18,000 words by both counts. Adding stopped at the first case that did not fit.

- **A1**: 24 given of 25 named. Given: O2, O4, O5, O7, O9, O10, O11, O22, O24, O33, O36, O45, O46, O47, O48, N1, N2, N3, N8, N9, N11, N16, N23, N25. Left out: N17.
- **A2**: 23 given of 23 named. Given: O1, O3, O10, O11, O18, O24, O27, O36, O40, O42, O43, O45, O46, O48, O49, O50, O52, N11, N15, N17, N20, N24, N25. Left out: none.
- **B1**: 20 given of 45 named. Given: O1, O5, O6, O8, O12, O21, O26, O27, O33, O35, O37, O40, O50, N7, N11, N13, N15, N17, N21, N23. Left out: O38, O49, O2, O3, O7, O14, O17, O18, O30, O31, O41, O51, O4, O10, O20, O22, O32, O34, O39, O43, O44, O48, N2, N5, N16.
- **B2**: 31 given of 45 named. Given: O3, O11, O13, O14, O17, O18, O20, O21, O24, O25, O26, O27, O30, O31, O35, O39, O40, O41, O45, O48, O49, O50, O51, O52, N4, N5, N10, N11, N13, N15, N21. Left out: N18, N19, O15, O19, O32, O36, O38, O42, O46, N1, N2, N9, N23, N25.
- **C**: 17 given of 53 named. Given: O8, O12, O14, O15, O23, O27, O32, O45, N1, N2, N3, N4, N5, N18, N19, N21, N22. Left out: N24, O3, O13, O36, N25, O2, O11, O43, O44, O47, O49, N7, N8, O1, O4, O5, O7, O18, O19, O21, O24, O28, O31, O34, O35, O38, O40, O42, O46, O48, O50, N12, N13, N15, N16, N17.

- **How they are given**, as in S90. The O-cases are the S81 book's entries byte for byte (md5 4f488d149e44669240d5db546c8e946a). The N-cases take their title, **Situation**, **Question(s)** and **Verdict** word for word from the S89 candidate book (md5 b2e535777976a511935430bd089ba500), with the verdict under "Thoughtful person's verdict". Words that only report how a verdict was agreed are cut, and each cut is marked […]. These are the S90 cuts, together with the two for N9 and N20, which S90 did not give:
  - N4: "(R2 A1)"; "Both round-1 authors said the same, and the reconciled proposal expected this answer."
  - N5: "The authors differ only in emphasis. A2 calls the seasons reading "a sensible first guess". A1 says only an understanding from outside the rule could tell him to sow in April or May. Both agree that the rule alone cannot settle it."
  - N9: "This is the answer the reconciled proposal drew from both round-1 authors."
  - N17: "(A1)"; "Round 1 was disputed on the old wording: A1 said both explain, at different levels, and A2 said only B, as given. Round-1 A2 had already said that a full A "would be a real physical account ... an explanation of a sort", which is where round 2 lands."
  - N18: "Round 1 was disputed on Dov's surprise because the sketch did not say what Dov expected or knew. The rewrite supplies both."
  - N20: "(R1 A1)".
  - N21: "Both round-1 authors leaned this way, and the reconciled proposal expected it."
  - N22: "This is the answer the reconciled proposal expected. Round 1 was disputed only on the old question, which asked whether either theorist had explained why people "seem" to have inner experiences."
  - N23: "(R2 A1, A2)".

## Sources, each checked by md5 when the parts were built

- **File 11**: `authority/11 … revision 1.md`, md5 5e494c1095d920d128b9a79de378f923, read only. Nothing was written into `authority/`.
- **The change list**: `tests/Revision 2 - change list, draft of 23 September.md`, md5 a5c92adc9f1e3806c0f9c6394cffde1e. `git show` confirmed it is byte-identical to the file committed in 587eebf. It has 63 entries: 58 applied (55 theory entries, of which CLAIM 48, WORDING 5 and ORDER 2, and 3 meta), 5 record-only and none held.
- **The draft.** It was regenerated by `tools/s89_apply_changes.py --theory-output --self-test` into the scratchpad. The program reported every check passed: 54 diff hunks, each inside an entry, and both planted edits refused. N = 48 of M = 55, K = 42.
  - The theory text alone has md5 **9aecf2f30ce0b4523606b2b8409fdf37**: 626 lines, 11,501 words by the runner's count and 11,473 by `wc -w`. It is committed with this note as `tests/Revision 2 - file 13 draft 2, theory text, as sent for cross-examination.md`, with the same md5. It is a draft, not an authority.
  - The full draft, with its meta blocks, has md5 f2bd0631034e4a7a0818265540a7f2fe with the program's default date text. It has 1d51c77eb591ace473e556568a7c4636, the md5 the change list records, with the date text "draft of 23 September 2026, not frozen". Only the note's date slot differs, and the theory text is the same either way.
  - The build script checked the draft again. It applied the 55 entries to file 11 and cut file 11's note, which gave the same text as the program's theory output. It located every NEW in the draft and checked that the block between the marker lines of each part is byte-identical to the draft.
- **The previous draft**, `tests/Revision 2 - file 13 draft, theory text, as sent for cross-examination.md` (md5 dd2741b0d5a18617d845b19b874943f4, the 48 changes), stays as the text the S90 brief carried.
- **The case books**: as above.

## How the replies will be read

This rule was written and committed before any part was sent.

1. **Each reply is read by the S90 rule on its own**, independently of the other model's reply to the same part and of the replies to the other parts. Rules 1 (evidence, not results), 5 (silence is not support), 7 (fixed verdicts are not in question) and 8 (quotations are checked) apply as written.
2. **What is contested.** A change is contested by a reply when the reply says it FALLS, or names an undeclared change of claim or a moved verdict on it, whatever line it gives the change (S90 rule 2).
3. **A change contested by either reply goes to a fresh Claude checker.** The checker did not draft, assemble or check the change list, and did not write these briefs. For each such change it works in this order:
   - first, it states the entry: OLD, NEW, KIND and DECLARATION, and its checkers' verdict, which is the entry's CHECK field (for the seven entries drafted from the settled S88 positions, that field says they were checked by their drafter only);
   - then, it states the reply's argument, or each reply's argument separately where both contest the change;
   - then, it rules: **keep**, **fix with new wording** (the exact new OLD or NEW, KIND or DECLARATION, with the reason), or **drop**.
4. **Edits are recorded as after the cross-examination** (S90 rule 3). Each edit goes in the entry itself, with its reason and the note that it came after the cross-examination, and in the list of what the checks changed. The counts, the note's N and M, and the record follow by program when the draft is rebuilt. A ruling of keep is recorded in the entry's CHECK field. W20.2's CHECK field already names the fallback for W20 if the deletion rider breaks a worked case.
5. **A failed part supports nothing** (S90 rule 4). A reply the runner does not accept, because it did not finish "stop" with END OF REPORT on its last line, counts neither for nor against any change. Its attempt files are kept and not read for arguments. The changes of that part are reported as **not examined by that model**. The part is not rerun without a new note written before sending.
6. **S90 rule 6 no longer applies.** That rule held the three repairs for a later cross-examination. The seven entries that carry them are in parts A1 and A2, and they are ruled like every other change.
7. **A point on a change outside the reply's part.** A reply may cite any id from R01 to R55. Such a point is passed to the checker of that change and marked as raised outside its part. It does not count that change as examined by that model.

## Decided

Decided by Claude under decision S18. 23 September 2026.
