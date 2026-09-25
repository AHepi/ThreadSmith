# S93: tabulation of the replies, before any ruling

*Written by a Claude subagent, the first reader of the S93 replies, for the orchestrator on 25 September 2026, after every one of the 22 calls of the S93 cross-examination of draft 4 had ended (all 22 were accepted on pass 1; the returns were committed unread at 5cd5950). This file tabulates. It rules on nothing: no point below is judged sound or unsound, and no item is kept, fixed or dropped here. Rulings are made later, by one fresh checker per item, under the reading rule committed before sending, `results/S93 How the cross-examination of draft 4 will be read - written before sending.md` ("the reading rule"; "rule n" is its numbered paragraph n). Nothing was written into `authority/`.*

**What was read.** The reading rule, whole. The 22 `.response.txt` files and their `.receipt.json` files in `results/S93 Cross-examination - draft 4 - returns/`. The eleven part briefs in `tests/` (each md5 equals the reading rule's table). The draft-4 theory text, `tests/Revision 2 - file 13 draft 4, theory text.md` (md5 fc55b470c63cd4b3c27d6aa64d8d8c17, as the reading rule gives). The change list, `tests/Revision 2 - change list, draft of 23 September.md`, was checked by md5 only (b6b2ea95ea9e21ebea3316d8e9fa4b40, as the reading rule gives); it is for the checkers (rule 4).

**What was not read.** No `.reasoning.txt` file and no `.request.json` file was opened. The failed first attempt of `s93_xexam_atria_E` (`s93_xexam_atria_E.pass1.a1.truncated.txt`, 0 bytes by its listed size, and `s93_xexam_atria_E.pass1.a1.reasoning.txt`) was not opened and is not read for arguments (rule 8). The session's key file was not opened.

**How the tables were made.**

- *Words* are whitespace-separated tokens of the response file (Python `str.split()`, equal to `LC_ALL=C.UTF-8 wc -w`). Plain `wc -w` in this container's POSIX locale gives smaller numbers, because it does not count a free-standing em dash as a word.
- *Quotations (rule 9).* Every quotation a reply relies on was searched first in the draft-4 text and then in the part's brief. "FOUND L315" means draft-4 line 315 (the briefs print the same numbers as `L315|`). "FOUND brief A §7 l.549" means line 549 of the part-A brief file, in its section 7 (§2 the owner's words and the drafters' rule, §4 the items with their old wordings and declarations, §5 the questions, §7 the described situations). The search ignored markdown emphasis, spacing, the kind of quotation mark, and LaTeX-versus-Unicode notation; an ellipsis or a bracketed alteration splits a quotation into pieces, each of which must be found. "FOUND (punct.)" means found once punctuation is ignored. "NOT FOUND" means not found word for word under those allowances; the nearest text is given where there is one. Words that are the reply's own (a proposal, a paraphrase it gives as its own, an invented example) are marked "own words" and are not quotations. Where a reply gives a line number other than the line where the words stand, that is noted; the point is then to be ruled on what the texts say (rule 9).
- *Challenged (rule 3).* An item is marked challenged by a reply when (i) its closing line reads CHALLENGED; or (ii) one of its points itself asserts, on that item, a false statement, a wrong kind or declaration, an incoherence (including an unchanged sentence made stale), a verdict moved away from the fixed verdict, or a return of a list, count, grade or record, whatever its closing line says; or (iii) it proposes exact new wording for the item; or (iv) one of its verdict words reads NOT FAITHFUL, FAILS, DEFECT, SAY DIFFERENTLY or WRONG. Where an item is marked challenged only under (ii) or (iii), that is said. This applies the rule as written; it is not a judgment that the point is right.
- *Disagreement (rule 5)* is marked where one reply upholds and the other challenges, where two challenges give different wordings or incompatible reasons, or where the verdict words on one question and item differ.
- *Points from outside the part (rule 11)* are listed under the item they bear on, marked "raised outside its part", and do not count that item as examined by that model.

---

## 1. Receipts

All 22 calls were accepted on pass 1 by rule 8: every receipt has `finish_reason` "stop", `saw_done` true and `pass` 1, and every response file's last line is `END OF REPORT`. Every response file's sha256 equals the `response_sha256` in its receipt, and its length in characters equals `response_chars`. Atria is `Atria-Dawn-Preview` (ceiling 65,536 tokens), Mimo is `mimo-v2.6-pro` (ceiling 131,072), effort medium for all.

| tag | accepted (rule 8) | pass | finish | attempts in the accepted pass (status / finish) | response words |
|---|---|---|---|---|---|
| s93_xexam_atria_A | yes | 1 | stop | 4: no HTTP status ×3 (each ≈1,802 s), then 200 / stop | 1,666 |
| s93_xexam_atria_B | yes | 1 | stop | 1: 200 / stop | 1,978 |
| s93_xexam_atria_C | yes | 1 | stop | 2: no HTTP status, then 200 / stop | 1,702 |
| s93_xexam_atria_D | yes | 1 | stop | 2: no HTTP status, then 200 / stop | 1,853 |
| s93_xexam_atria_E | yes | 1 | stop | 2: 200 / **length** (0 content characters; rejected "finish length"; its files are kept and not read), then 200 / stop | 611 |
| s93_xexam_atria_F | yes | 1 | stop | 2: no HTTP status, then 200 / stop | 1,582 |
| s93_xexam_atria_G | yes | 1 | stop | 1: 200 / stop | 1,516 |
| s93_xexam_atria_H | yes | 1 | stop | 1: 200 / stop | 1,208 |
| s93_xexam_atria_I | yes | 1 | stop | 2: no HTTP status, then 200 / stop | 1,479 |
| s93_xexam_atria_J | yes | 1 | stop | 1: 200 / stop | 936 |
| s93_xexam_atria_K | yes | 1 | stop | 4: no HTTP status ×3, then 200 / stop | 1,619 |
| s93_xexam_mimo_A | yes | 1 | stop | 1: 200 / stop | 2,186 |
| s93_xexam_mimo_B | yes | 1 | stop | 1: 200 / stop | 1,970 |
| s93_xexam_mimo_C | yes | 1 | stop | 1: 200 / stop | 2,097 |
| s93_xexam_mimo_D | yes | 1 | stop | 1: 200 / stop | 2,161 |
| s93_xexam_mimo_E | yes | 1 | stop | 1: 200 / stop | 1,333 |
| s93_xexam_mimo_F | yes | 1 | stop | 1: 200 / stop | 1,516 |
| s93_xexam_mimo_G | yes | 1 | stop | 1: 200 / stop | 1,475 |
| s93_xexam_mimo_H | yes | 1 | stop | 1: 200 / stop | 1,518 |
| s93_xexam_mimo_I | yes | 1 | stop | 1: 200 / stop | 1,071 |
| s93_xexam_mimo_J | yes | 1 | stop | 1: 200 / stop | 1,213 |
| s93_xexam_mimo_K | yes | 1 | stop | 1: 200 / stop | 1,597 |

The attempts with no HTTP status are connection-level failures inside the one pass, not answers from the model (lessons S21 and S24, as rule 8 recalls). The one attempt that was an answer and failed is atria_E's first, which ran to the length ceiling with no content; the accepted reply is the second attempt, made with a byte-identical request (the same `request_sha256`). No item is "not examined" by either model.

**Form.** Every reply gives one closing line per item and one OVERALL line. Some depart from the exact form without changing what is said: most of Atria's UPHELD lines carry a reason after a dash (the briefs asked for `Xnn: UPHELD` alone); Mimo F and Mimo H print their (d) verdict lines inside backticks; Atria's verdict lines in B and E are in bold. Parts G, I and K asked (a) only as a point, with no verdict line; what each reply says there is recorded in words.

---

## 2. Per item: closing lines, verdict words, challenge and disagreement

### 2.1 Summary

A = Atria, M = Mimo. "–" means the question was not asked of the item in its part. In parts G, I and K, (a) was asked only as a point; the entry gives the reply's words in brief.

| item | entry | part | A closing | M closing | (a) A / M | (b) A / M | (c1) A / M | (c2) A / M | (d) A / M | challenged (rule 3) | rule 5 | checker |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X01 | W37.1 | F | UPHELD | UPHELD | – | – | – | – | – | no | – | none |
| X02 | W36.1 | D | UPHELD | UPHELD | FAITHFUL / FAITHFUL | – | – | – | – | no | – | none |
| X03 | W19.1 | F | UPHELD | CHALLENGED | – | – | – | – | RIGHT / RIGHT, WITH A LOSS | by M | DISAGREEMENT | yes |
| X04 | W35.1 | G | UPHELD | UPHELD | point: "faithful to, or merely neutral" / point: "Faithful" | – | – | – | – | by M, under (ii) only (M point 2) | DISAGREEMENT | yes |
| X05 | W35.2 | G | UPHELD | CHALLENGED | as X04 | – | – | – | – | by M | DISAGREEMENT | yes |
| X06 | W20.1 | H | UPHELD | CHALLENGED | – | – | – | – | RIGHT / RIGHT, WITH A LOSS | by M; by A under (iii) only (an optional phrase, A point 3) | DISAGREEMENT | yes |
| X07 | W34.1 | D | UPHELD | UPHELD | FAITHFUL / FAITHFUL | – | – | – | – | no | – | none |
| X08 | W33.1 | D | UPHELD | UPHELD | FAITHFUL / FAITHFUL | – | – | – | RIGHT / RIGHT | no | – | none |
| X09 | W59.1 "Rivals" | A | CHALLENGED | CHALLENGED | FAITHFUL / FAITHFUL | – | – | UNSETTLED BY THE TEXT / UNSETTLED BY THE TEXT | RIGHT / RIGHT, WITH A LOSS | by both; and from outside part A (rule 11) | DISAGREEMENT | yes |
| X10 | W59.1 "Problems" | B | UPHELD | UPHELD | FAITHFUL / FAITHFUL | – | HARMLESS / HARMLESS | UNSETTLED BY THE TEXT / **ESTABLISHED** | – | by M under (iii) only (an optional phrase, M point 5); and from outside part B (rule 11) | DISAGREEMENT on (c2) | yes |
| X11 | proposed | I | UPHELD | CHALLENGED | point: no bearing / point: "no new (a) issue" | – | – | – | – | by M | DISAGREEMENT | yes |
| X12 | W40.1 | I | UPHELD | UPHELD | point: "not engaged and is not violated" / point: "consistent" | – | – | – | – | no | – | none |
| X13 | W24.1 | J | UPHELD | UPHELD | – | – | – | – | – | no | – | none |
| X14 | W60.1 | C | UPHELD | UPHELD | FAITHFUL / FAITHFUL | HOLDS AS STATED / HOLDS AS STATED | – | UNSETTLED BY THE TEXT / UNSETTLED BY THE TEXT | – | by M under (iii) only (optional wordings, M points 2 and 4) | DISAGREEMENT (A upholds; M's rule-3 challenge; verdict words agree) | yes |
| X15 | W22.1 | J | UPHELD | UPHELD | FAITHFUL / FAITHFUL | – | – | – | – | no | – | none |
| X16 | W6.3 | K | UPHELD | UPHELD | point: "Not applicable" / point: "Faithful" | – | – | – | – | no (a residual on L524 is flagged, §4) | – (flagged, §2.2) | none |
| X17 | W7.5 | K | UPHELD | CHALLENGED | point: "Faithful" / point: "Faithful" | – | – | – | – | by M | DISAGREEMENT | yes |
| X18 | W38.1 | E | CHALLENGED | CHALLENGED | FAITHFUL / FAITHFUL | – | HARMLESS / HARMLESS | – | – | by both | DISAGREEMENT (different reasons and wordings; one fix shared) | yes |

Ten items go to a checker: X03, X04, X05, X06, X09, X10, X11, X14, X17, X18. Eight go to none: X01, X02, X07, X08, X12, X13, X15, X16 (§4).

**OVERALL lines.**

| part | items | Atria | Mimo |
|---|---|---|---|
| A | X09 | NEEDS REPAIR | NEEDS REPAIR |
| B | X10 | SOUND | SOUND |
| C | X14 | SOUND | SOUND |
| D | X02, X07, X08 | SOUND | SOUND |
| E | X18 | NEEDS REPAIR | NEEDS REPAIR |
| F | X01, X03 | SOUND | NEEDS REPAIR |
| G | X04, X05 | SOUND | NEEDS REPAIR |
| H | X06 | SOUND | NEEDS REPAIR |
| I | X11, X12 | SOUND | NEEDS REPAIR |
| J | X13, X15 | SOUND | SOUND |
| K | X16, X17 | SOUND | NEEDS REPAIR |

Atria reads NEEDS REPAIR in 2 parts of 11, Mimo in 7. A count settles nothing (rule 5); it is given only as the record.

**Question (a), faithfulness to the owner's decision S20 and to the drafters' rule of lesson S26 (brief §2), where it was asked with a verdict line:** X02, X07, X08 (D), X09 (A), X10 (B), X14 (C), X15 (J) and X18 (E): FAITHFUL from both replies on every one. No reply returned NOT FAITHFUL on any item, and no point in any reply asserts that an item brings back a list, an enumeration, a count of versions, a grade or a record.

### 2.2 Item by item

Closing lines are copied exactly.

**X01 · W37.1 · Part 0, L13 · ORDER · part F.**
- Atria: `X01: UPHELD — attacks on ORDER-vs-CLAIM, on the clause's literal truth, and on the O11/N9/N11 classifications all fail: L195 and L201 already state it, and the cases still turn on Part IV.`
- Mimo: `X01: UPHELD`
- Verdict words: none asked. Both replies name Part IV, L195 and L201, as the place that already states the clause (the ORDER test).
- Challenged: no. Points from outside part F: none.
- Route: no checker (§4).

**X02 · W36.1 · Part I, L69 · CLAIM · part D.**
- Atria: `X02: UPHELD — the gloss is true, declared exactly, forward-consistent with Part V, and moves N3/N2/N25 toward the fixed verdicts.`
- Mimo: `X02: UPHELD`
- (a): FAITHFUL / FAITHFUL.
- Challenged: no. Points from outside part D: none.
- Route: no checker (§4).

**X03 · W19.1 · Part II, L119 · CLAIM · part F.**
- Atria: `X03: UPHELD — attacks on the definition's well-formedness, on the kind and declaration, on coherence with L245/L558, and on O10/O22/O9/N25 all fail; the definition is the one Derivations 1 and 2 already use.`
- Mimo: `X03: CHALLENGED — the cross-candidate comparison is left without a value or index identification, and it reports Derivation 1 for a component where Derivation 1 speaks only of an active one`
- (d): Atria `(d) X03: RIGHT`; Mimo `(d) X03: RIGHT, WITH A LOSS — "easy to vary" is never said of a candidate whose discovered variation conflicts at no admitted pair or only inside C, so the swappable pick of N25 cannot be called easy to vary at all`
- Challenged: yes, by Mimo (closing line; exact wording and declaration proposed).
- Rule 5: DISAGREEMENT (UPHELD against CHALLENGED; different (d) verdict words).
- Points from outside part F: none. (Mimo's (d) loss bears on X10's definition of easy to vary and on X09's condition; it is listed under those items as raised outside their parts.)
- Route: checker (§3.1).

**X04 · W35.1 · Part IV, L217–221 · CLAIM · part G.**
- Atria: `X04: UPHELD`
- Mimo: `X04: UPHELD`
- (a), as points: Atria (point 9, on X04 and X05) "Both are faithful to, or merely neutral with respect to, the owner's words and the rule"; Mimo (point 8) "Faithful".
- Challenged: yes, by Mimo under (ii) only: Mimo's point 2, headed "X04 · T3 — X04 pulls against Derivation 4's proof sentence", says that after X04 the unchanged proof sentence at L582 reports a broader definition of surprise than the text has, and gives words for L582; the same point says "X04 is not the place to fix this, so it does not overturn the item".
- Rule 5: DISAGREEMENT. Atria's point 7 examines the same sentence and calls the proof's omission of "selected" "a simplification inside a claim already about a selected transport, not a contradiction"; the two reasons are incompatible.
- Points from outside part G: none.
- Route: checker (§3.2).

**X05 · W35.2 · Part IV, L223 · CLAIM · part G.**
- Atria: `X05: UPHELD`
- Mimo: `X05: CHALLENGED — the restatement omits the block's "actually occurring" scoping and its declaration repeats the omission`
- (a), as points: as X04.
- Challenged: yes, by Mimo (closing line; exact wording and declaration proposed).
- Rule 5: DISAGREEMENT.
- Points from outside part G: none.
- Route: checker (§3.3).

**X06 · W20.1 · Part V, L231 · CLAIM · part H.**
- Atria: `X06: UPHELD — the input-assigner edge case is settled by unchanged lines L103/L255/(F2), the kind and declaration are exact, the "named background" reference repairs a dangling antecedent, and the only verdict moves (O45, N1) are toward the fixed verdicts and declared.`
- Mimo: `X06: CHALLENGED — its two halves contradict for a candidate that offers an input-assigning component as doing the work (Part VII, L331), and "boundary values" is undefined at L231.`
- (d): Atria `(d) X06: RIGHT`; Mimo `(d) X06: RIGHT, WITH A LOSS — two discovered variations that both fit but differ only in what no admitted change reaches (and a variation nobody has offered in place of another) pose no problem, though the owner counts both as competitors.`
- Challenged: yes, by Mimo (closing line; exact new wording, declaration, and repairs of L245, L299 and L558 proposed); and by Atria under (iii) only, for the optional phrase in its point 3 ("A tighter phrasing ("what Part VI calls the named background") would be smoother but changes no claim").
- Rule 5: DISAGREEMENT (UPHELD against CHALLENGED; different (d) verdict words; different wordings).
- Points from outside part H: none. (Mimo's (d) loss bears on X09's condition and is listed there as raised outside part A.)
- Route: checker (§3.4).

**X07 · W34.1 · Part VI, L313 · CLAIM · part D.**
- Atria: `X07: UPHELD — the lemma and Pres are gone, the declaration is exact, nothing in the revised text depended on them, and no verdict moves away.`
- Mimo: `X07: UPHELD`
- (a): FAITHFUL / FAITHFUL.
- Challenged: no. Both replies raise, and both decline to press against X07, that \(\mathcal V\) survives in (D) and is not among Part XIV's declared inputs (flagged in §4).
- Route: no checker (§4).

**X08 · W33.1 · Part VI, L313 · CLAIM · part D.**
- Atria: `X08: UPHELD — the no-work definition and both consequences are derivable from (S) and (B), the infinitary clause is verified, and the paragraph is coherent with L305–L317.`
- Mimo: `X08: UPHELD`
- (a): FAITHFUL / FAITHFUL. (d): RIGHT / RIGHT.
- Challenged: no. Points from outside part D: none that assert a defect of X08.
- Route: no checker (§4). Both (d) paragraphs concern the rivals condition of L315 and are listed under X09 as raised outside part A.

**X09 · W59.1, "Rivals" · Part VI, L315 · CLAIM · part A.**
- Atria: `X09: CHALLENGED — "established" does not settle whether a candidate's own structural failure (circularity, contradiction, anchor to nothing) counts, and the rivals-and-problems machinery needs it to; repair in point 1.`
- Mimo: `X09: CHALLENGED — the illustration of conflict is not entailed by the definition, and the exclusion sentence reverses on a literal parse`
- (a): FAITHFUL / FAITHFUL. (c2): UNSETTLED BY THE TEXT / UNSETTLED BY THE TEXT. (d): Atria `(d) X09: RIGHT`; Mimo `(d) X09: RIGHT, WITH A LOSS — a conflict at a pair only one of the two transports translates is not counted.`
- Challenged: yes, by both (closing lines; each proposes exact wording).
- Rule 5: DISAGREEMENT (two challenges with different reasons and different wordings; different (d) verdict words).
- Points from outside part A (rule 11): Atria B point 1 and (c2); Mimo B point 3 and (c2); Atria C (c2); Mimo C point 1 and (c2); Atria K on X17 · T3; Mimo K point 2; and the (d) paragraphs of parts D, F and H, which answer whether the rivals condition of L315 is right (Atria D, Mimo D, Atria F, Mimo F, Atria H, Mimo H). Digested in §3.5.
- Route: checker (§3.5).

**X10 · W59.1, "Problems" · Part VI, L317 · CLAIM · part B.**
- Atria: `X10: UPHELD — every attack failed: the internal-failure gap lies in X09/Part IX, not in X10; the two T1 counterexamples dissolve on the definitions of conflict and fit; the declaration is complete and the kind right; all pointers and cross-references check out; no listed set, count, grade or record is reintroduced; and no verdict on the named situations moves away from the fixed verdict.`
- Mimo: `X10: UPHELD`
- (a): FAITHFUL / FAITHFUL. (c1): HARMLESS / HARMLESS. (c2): Atria `UNSETTLED BY THE TEXT`; Mimo `ESTABLISHED`.
- Challenged: not by either closing line or verdict word. By Mimo under (iii) only, for an optional phrase (point 5: ""For that assessor" would be smoother; without it the text is not incoherent"). From outside part B (rule 11): Atria K, on X17 · T3, says the dependence order places none of the Part VI notions and that "the gap ... belongs to the items that introduced lines 315/317"; the other outside points are listed in §3.6.
- Rule 5: DISAGREEMENT on (c2) (UNSETTLED BY THE TEXT against ESTABLISHED). (c2) is also a matter for the owner (rule 6; §6).
- Route: checker (§3.6).

**X11 · proposed WORDING · Part VII, L325 · part I.**
- Atria: `X11: UPHELD — the symbol must be *L*: an edit setting *H* replaces the component that assigns *H* (Part II), so the calculation's *H* changes while its *L* does not, as line 271 already says.`
- Mimo: `X11: CHALLENGED — the wordings name different ports, so WORDING is the wrong kind; should be CLAIM.`
- (a), as points: Atria "No bearing on rivals, variation, criticism or error correction; the rule is not engaged"; Mimo "X11 raises no new (a) issue".
- Challenged: yes, by Mimo (closing line; kind and declaration proposed). Both replies hold the change of symbol itself correct.
- Rule 5: DISAGREEMENT (on the kind).
- Route: checker (§3.7).

**X12 · W40.1 · Part VII, L339 · CLAIM · part I.**
- Atria: `X12: UPHELD — every clause is supported by (E) and Part III, the declaration matches it clause for clause, and it moves no fixed verdict.`
- Mimo: `X12: UPHELD`
- (a), as points: Atria "The rule is not engaged and is not violated"; Mimo "consistent with the owner's position ... and the drafters' rule".
- Challenged: no. Route: no checker (§4).

**X13 · W24.1 · Part VIII, L353 · WORDING · part J.**
- Atria: `X13: UPHELD`
- Mimo: `X13: UPHELD`
- Verdict words: none asked. Both replies attacked the kind (WORDING against CLAIM or ORDER) and found WORDING right.
- Challenged: no. Route: no checker (§4).

**X14 · W60.1 · Part VIII, L369 · CLAIM · part C.**
- Atria: `X14: UPHELD — the three attacks above (the technical sense of "established," the over-strong "ceases," the tension with L317) each fail for the reasons given; the kind and declaration match the wording; no verdict on O1, D3-T, O27, O8, N7, N2 or O24 moves in either direction.`
- Mimo: `X14: UPHELD`
- (a): FAITHFUL / FAITHFUL. (b): HOLDS AS STATED / HOLDS AS STATED. (c2): UNSETTLED BY THE TEXT / UNSETTLED BY THE TEXT.
- Challenged: by Mimo under (iii) only. Mimo's point 2 offers exact wording for the closing sentence if the drafters want a wording hazard closed ("being an account of it is not thereby an account of \(p\)"), and point 4 offers "the result" for "the exclusion"; point 2 says the attack "fails to defeat the item", point 4 calls its three nits "none fatal", and point 1 ends "X14 states nothing contrary; it stands." Atria calls one sentence "at most a wording imprecision" (point 2) and proposes no wording.
- Rule 5: marked DISAGREEMENT (Atria upholds with no change; Mimo's rule-3 challenge by optional wording). The verdict words agree.
- Points from outside part C: none asserting a defect of X14.
- Route: checker (§3.8).

**X15 · W22.1 · Part IX, L377 · CLAIM · part J.**
- Atria: `X15: UPHELD`
- Mimo: `X15: UPHELD`
- (a): FAITHFUL / FAITHFUL.
- Challenged: no. Route: no checker (§4).

**X16 · W6.3 · Part XI, L455 · CLAIM · part K.**
- Atria: `X16: UPHELD — the attacks that it is mere WORDING and that it clashes with Part XIV both fail: "declared" mis-categorized a primitive, and "taken" is Part XIV's own verb for primitives.`
- Mimo: `X16: UPHELD`
- (a), as points: Atria "Not applicable"; Mimo "Faithful". Neither is a verdict line in the brief's form and neither finds the item unfaithful; this tabulation does not count the pair as different verdict words under rule 5, and flags it here for the orchestrator.
- Challenged: no. Flagged (§4): Mimo's point 7 gives words for L524 ("and which is not one of the two primitives") as a "Residual, outside this item" and says "I do not press it against X16".
- Route: no checker (§4).

**X17 · W7.5 · Part XIV, L526 · CLAIM · part K.**
- Atria: `X17: UPHELD — every added dependence is supported by Parts X–XII, the declaration matches the new wording clause for clause, no verdict moves, and the order's silence on Part VI's rival/problem terms is a pre-existing incompleteness, not a falsity X17 introduces.`
- Mimo: `X17: CHALLENGED — (EK)'s entry omits the declared obligations with their occasions and ProducesVia, which (EK) uses directly and not only through (P)`
- (a), as points: Atria "Faithful"; Mimo "Faithful".
- Challenged: yes, by Mimo (closing line; exact wording and declaration proposed).
- Rule 5: DISAGREEMENT.
- Route: checker (§3.9).

**X18 · W38.1 · the note of sources and departures · META · part E.**
- Atria: `X18: CHALLENGED — the *Reach* bullet cites Parts I and VI where L317 cites Parts I and V, and the *Hard to vary* bullet asserts an application the text does not make.`
- Mimo: `X18: CHALLENGED — the note's definition of recognized difficulty omits "what the system holds" and "only," giving a broader definition than Part X, L429.`
- (a): FAITHFUL / FAITHFUL. (c1): HARMLESS / HARMLESS.
- Challenged: yes, by both.
- Rule 5: DISAGREEMENT (different reasons and wordings; both replies propose the same change of the Reach pointer to "(Parts I and V)").
- Route: checker (§3.10).

---
## 3. Digest of the points on the items that go to a checker

For each item: every point either reply makes on it, in the reply's order, numbered here as Xnn.k. Each entry gives the model, part and point number, the claim in a sentence or two (the reply's claim, not a finding), any exact wording proposed (copied exactly from the response file, between fence lines that are not part of it), and the quotations the point relies on with the rule-9 check. Short quotations are cited by their first words; "…" marks where this file shortens them. Points raised on the item in another part are listed last and marked **raised outside its part (rule 11)**.

### 3.1 X03 · W19.1 · Part II, L119 · CLAIM · part F

**X03.1 · Atria · F · point 1 (T1).** The new sentence looks ill-formed, since the two signatures are sets of triples indexed in different organizations; the reply holds that "read on \(C\) through \(\tau\) and \(\tau'\)" fixes the common index \((a,b)\in C\), which is the construction Derivation 1 and Derivation 2's proof already use, and that O9's float- and dial-anchored components stay apart. Attack reported as failing. No wording.
- "of one kind on \(C\)" FOUND L119, L562. "coincide under a footprint bijection" FOUND L119. "read on \(C\) through \(\tau\) and \(\tau'\)" FOUND L119. "has the same signature on \(\tau[C]\) as its anchor \(\lambda(k)\) has on \(C\), up to the port translation" FOUND L554. "composing the one translation with the inverse of the other …" FOUND L564. "candidates that anchor different subnetworks … are different candidates with one answer profile" FOUND L566.

**X03.2 · Atria · F · point 2 (T2).** CLAIM is right, not WORDING: Derivation 2 used the notion but Part II never defined it; the declaration's three clauses match the wording; restating \((\pi,\tau,\sigma,\lambda)\) is notation. No wording.
- "read on \(C\) through \(\tau\)" FOUND L119. "read on \(C\) directly with its hidden ports projected away" FOUND L119.

**X03.3 · Atria · F · point 3 (T3).** No clash with L245 or L558, which concern the definition of an account; the two uses of "of one kind on \(C\)" agree, the cross-candidate case reducing to the single-candidate case when \(E=E'\); the pointers check. No wording.
- "there is no further condition about kinds to state" FOUND L245. "The word 'kind' is therefore eliminable from the definition of an account" FOUND L558 (the text puts "kind" in double quotes). "explanatory candidates (Part V)" FOUND L119.

**X03.4 · Atria · F · point 4 (T4).** No move on O10, O22, O9 or N25: the thermostats' set point is a boundary value; O9's candidates stay apart "and they remain rivals"; N25's dog and turtle are one kind on \(C\) and neither is an account (L257). No wording.
- "a signature is built from a component's relation … not from the values its ports take" FOUND L119. "excluding every change under which the active commitments could matter to \(\mathcal Q\)" FOUND L257. "turn both": own words (O22 says the knobs are "turned together", brief F §7 l.616). "really a dog": own words. "idle difference": NOT FOUND (N25's verdict reads "the difference between them is idle", brief F §7 l.637).

**X03.5 · Atria · F · (d) X03: RIGHT.** Two candidates that agree at every admitted pair both transports translate make the same claim, so there is nothing for rivalry to be about; recodings and no-work parts fall outside, and a no-work part that answers differently outside \(C\) makes rivals and a second-kind problem, correctly; nothing is lost; a narrow reading of "offered … in place of the other" would lose something, but the gloss at L315 fixes the broad reading. No wording.
- "two of their active components with one anchor have different relations there" FOUND L315. "Nothing here counts rivals, grades a candidate or ranks candidates" FOUND L317. "offered … in place of the other" FOUND L315. "a candidate's rivals are among the candidates someone has offered, and …" FOUND L315.

**X03.6 · Mimo · F · point 1 (T1).** The relation is not evaluable across two organizations: the wording supplies only a footprint map, while the index elements \((\tau(a),\sigma(b))\) and \((\tau'(a),\sigma'(b))\) lie in different organizations and the values lie in different port domains with no value map (O9: float heights against dial labels); Derivation 2 gets the identification from a shared anchor, which the general relation does not require; so the declaration's "Part II now defines when…" is too strong. Proposed wording, then declaration:

~~~~text
A kind is an equivalence class of components under this relation. For two explanatory candidates for one question (Part V), with one target \(D\), let \(E\) and \(E'\) be their organizations and \(t=(\pi,\tau,\sigma,\lambda)\) and \(t'=(\pi',\tau',\sigma',\lambda')\) their transports from \(D\), where \(\tau\) translates edits, \(\sigma\) translates boundaries, and \(\lambda\) assigns each component of \(E\) a subnetwork of \(D\), its anchor, with a port translation (Part IV). A component \(k\) of \(E\) and a component \(k'\) of \(E'\) are of one kind on \(C\) when, for every \((a,b)\in C\), \(L_k(\tau(a),\sigma(b))\) and \(L_{k'}(\tau'(a),\sigma'(b))\) correspond under one bijection of \(V_k\) onto \(V_{k'}\) that carries the value domain of each port of one onto the value domain of the other; this is their signatures read on \(C\) through \(\tau\) and \(\tau'\), and it extends the relation above to components of different organizations, whose classes are kinds in the same sense; Derivation 2 uses kinds in this sense. Derivation 1 makes the like comparison between an active component \(k\) of \(E\), read on \(C\) through \(\tau\), and its anchor \(\lambda(k)\), read on \(C\) directly with its hidden ports projected away, up to the port translation.
~~~~

~~~~text
Part II now defines when a component of one candidate's organization and a component of another's, the two candidates for one question with one target, are of one kind on C: their relations at every (a,b) of C, read through the two candidates' transports, correspond under a bijection of their footprints that carries the value domain of each port of one onto that of the other. It says that Derivation 2 uses kinds in this sense, and that Derivation 1 makes the like comparison between an active component, read through its transport, and its anchor, read on C directly with its hidden ports projected away, up to the port translation.
~~~~

- "read on \(C\) through \(\tau\) and \(\tau'\), coincide under a footprint bijection" FOUND L119. "the two signatures, read on \(C\), coincide" FOUND L564. "one anchor, the same subnetwork of \(D\) with port translations onto the same ports of \(D\)" FOUND L562. "composing the one translation with the inverse of the other gives a footprint bijection" FOUND L564. "Part II now defines when…" FOUND brief F §4 l.544 (the declaration).

**X03.7 · Mimo · F · point 2 (T2).** The insertion reports Derivation 1 as comparing "a component \(k\) of \(E\)" with its anchor, while (F1) and Derivation 1 speak of every active component; since \(\lambda\) anchors every component, a reader concludes that every component has its anchor's signature, which is false outside \(\Gamma\) (L245 already says the wider thing, which (F1) does not support); the declaration repeats "a component" and drops "up to the port translation". Repaired by X03.6's wording.
- "every active component \(k\) of \(E\)" FOUND L233, L554. "a component \(k\) of \(E\)" FOUND L119. "up to the port translation" FOUND L119, L554.

**X03.8 · Mimo · F · point 3 (T3).** L119's "A kind is an equivalence class of components under this relation" covers only the relation inside one organization, while three comparisons now share "of one kind on \(C\)" and only one has classes attached; the clause "whose classes are kinds in the same sense" in X03.6's wording closes this.
- "A kind is an equivalence class of components under this relation" FOUND L119. "whose classes are kinds in the same sense": own words (its proposal).

**X03.9 · Mimo · F · (d) X03: RIGHT, WITH A LOSS.** Requiring a locus is right, and recodings and pairs that some relations let both meet fall outside; a no-work part that changes answers outside \(C\) makes rivals and a second-kind problem, as the owner's words ask. The loss: "easy to vary" is never said of N25's swappable picks, which either conflict inside \(C\) (a first-kind problem) or conflict nowhere; both of N25's fixed verdicts stand, "only the name is missing". (This bears on X10's definition and X09's condition; see §3.5 and §3.6.)
- "in \(C\) or outside it" FOUND L315. "two candidates that differ only in how they are written… conflict at no pair" FOUND L315. "if two discovered variations fit, that constitutes a problem" FOUND brief F §2 l.28. "arbitrary picks that could be swapped for any other creature" FOUND brief F §7 l.633. "a dog is not a turtle" FOUND brief F §7 l.637. "Two components no admitted change can separate are one kind at that level, whatever labels anyone attach to them": NOT FOUND (L11 reads "attaches").

No point on X03 was raised outside part F.

### 3.2 X04 · W35.1 · Part IV, L217–221 · CLAIM · part G

**X04.1 · Atria · G · point 1 (T1).** Attack: the new lead-in gives declared transports an expectation although a declared transport makes nothing represent (L211) and \(S\) is where expectation lives (L177). Reported as failing: expectation is an answer-profile value, the theory already evaluates fidelity for declared transports on the same footing (L265), the provenance taxonomy governs representation, and the declaration's "whatever its provenance" makes the reading explicit.
- "Let \(t\) be a transport to the simulation layer \(S\)" FOUND L217. "A declared transport does not make an occurrence represent anything; it makes a modeller assert that it does" FOUND L211. "\(S\) is where expectation lives." FOUND L177. "Surprise is not a feeling added to the semantics." FOUND L584. "Every conjunct is a condition on how supplied relations behave under the changes in \(C\)" FOUND L265. "exactly one of three provenances" FOUND L193. "whatever its provenance" FOUND brief G §4 l.524 (the declaration).

**X04.2 · Atria · G · point 3 (T2).** Attack: ORDER or WORDING, since L225 already spoke of responses to a violation. Reported as failing: the old block scoped all three definitions to a selected \(t\), so the extension concludes something new; the declaration is exact.
- "Let \(t\) be selected on history \(H\) with contract \(C\)" FOUND brief G §4 l.529 (old wording). "Two responses to a violation" FOUND L225. "A construction response" FOUND L225. "expectation and violation ... for every transport to the simulation layer, whatever its provenance" FOUND L223 and brief G §4 l.524. "keeps surprise for a violation of a selected one at a pair outside its history" FOUND brief G §4 l.524. "surprise is a violation of a selected transport at \((a,b)\notin H\)" FOUND L221.

**X04.3 · Atria · G · point 5 (T4, N18).** The one verdict that moves: under the old text the theory was silent on whether Rhea's constructed theory was violated; now both designers' expectations are violated, which moves toward the fixed verdict and is declared; Rhea's violation is not surprise and Dov's is.
- "survival on \(H\) does not distinguish \(t\) from \(t'\) there" FOUND L572. "the blanket claim that every untested value is unconstrained" FOUND L576.

**X04.4 · Atria · G · point 7 (T3).** Terms are defined before use; Derivation 4's claim and proof "remain correct under the narrower new definition of surprise; the proof's omission of "selected" is a simplification inside a claim already about a selected transport, not a contradiction"; the earlier form's forward reference is repaired. No wording. (Compare X04.6.)
- "surprised only if it holds a transport selected on a history \(H\) strictly smaller than the contract \(C\)" FOUND L580. "Surprise is defined as a violation at \((a,b)\notin H\)" FOUND L582. "Let \(t\) be a transport with contract \(C\)" FOUND brief G §4 l.553 (the earlier reading's wording).

**X04.5 · Atria · G · point 9 ((a), X04 and X05).** Neither item touches hard to vary, rivals, counts, grades or records; both are "faithful to, or merely neutral with respect to" the owner's words and the rule.
- "with no record of which candidates failed before or of how any was changed" FOUND L369.

**X04.6 · Mimo · G · point 2 (T3).** X04 pulls against Derivation 4's proof sentence: after X04 surprise is "a violation of a selected transport at \((a,b)\notin H\)" (L221), but the unchanged proof at L582 reports the broader definition, on which the claim at L580 would be false; the claim and the consequence match the revised definition, so "what lags is one proof sentence"; "X04 is not the place to fix this, so it does not overturn the item". Words proposed for L582 (not an item's wording): `Surprise is defined as a violation of a selected transport at \((a,b)\notin H\); a transport that is not selected is not subject to surprise at all.`
- "*Proof.* Surprise is defined as a violation at \((a,b)\notin H\)." FOUND L582. "a violation of a selected transport at \((a,b)\notin H\)" FOUND L221. "A system can be surprised only if it holds a transport selected on a history \(H\) strictly smaller than the contract \(C\)" FOUND L580. "the signature of a selected transport meeting a change outside its history" FOUND L584.

**X04.7 · Mimo · G · point 3 (T1).** Attack on "whatever its provenance" against (R): reported as failing, since the block defines values and events on transports as such, (R) governs representation, surprise stays with selected transports, and X05's clause needs a violation the system represents.
- "A declared transport does not make an occurrence represent anything; it makes a modeller assert that it does" FOUND L211. "a modelling convenience" FOUND L13. "whatever its provenance" FOUND brief G §4 l.524. "a violation the system represents" FOUND L223.

**X04.8 · Mimo · G · point 4 (T3).** The \(H\) in the surprise bullet is bound only "where \(t\) is selected"; reported as failing as a defect of claim; "A tightening would be welcome but is not required." No wording.
- "where \(t\) is selected" FOUND L217. "a violation of a selected transport at \((a,b)\notin H\)" FOUND L221. "at a pair outside its history" FOUND brief G §4 l.524 (the declaration).

**X04.9 · Mimo · G · point 5 (T4, N18).** The move on N18 is toward the fixed verdict and is what the declaration states; no move away.
- "Let \(t\) be selected" FOUND brief G §4 l.529 (old wording). "the expectation is \(\operatorname{Ans}_S(\tau(a),\sigma(b))\)" FOUND L219. "Yes, the swaying went against what both expected" FOUND brief G §7 l.628. "contradicted what Rhea had reason to expect" FOUND brief G §7 l.628. "nothing Dov had reason to expect" FOUND brief G §7 l.628. "Whether the correspondence could have been otherwise at such a change is a fact about its population (Derivation 3)" FOUND L223. "did the swaying go against what she expected": NOT FOUND (N18's question reads "Did the swaying go against what each designer expected?", brief G §7 l.626).

**X04.10 · Mimo · G · point 6 (T3, T4).** O3, O48, O11 and O5 do not move: restricting surprise to selected transports is unchanged, and O5 is governed by L159.
- "is often surprised" FOUND brief G §7 l.662. "No member of the history represents \(t\), \(H\), or the survival condition" FOUND L195. "a narrowing adopted after a failure is a new claim at a new index" FOUND L159. "Where the claim states the ground of its restriction, a verdict on the restriction is given with that ground" FOUND L159. "days other than Tuesdays" FOUND brief G §7 l.674.

**X04.11 · Mimo · G · point 8 ((a), X04 and X05).** No listed set, enumeration, count, grade or record; faithful.
- "No list of all rivals is supposed" FOUND L315. "A failed answer stays failed" FOUND L369. "with no record of which candidates failed before or of how any was changed" FOUND L369. "Closing an episode is a decision, not a proof" FOUND L429.

No point on X04 was raised outside part G.

### 3.3 X05 · W35.2 · Part IV, L223 · CLAIM · part G

**X05.1 · Atria · G · point 2 (T1).** Attack: "a violation the system represents can be a recognized difficulty (Part X)" is unsupported, since no text makes a transport's fidelity a claimed obligation. Reported as failing: "can be" is existential; Derivation 10 is a model (the obligation "predict displacements correctly"); L201 gives the shape; L317 uses the same device.
- "a violation the system represents can be a recognized difficulty (Part X)" FOUND L223. "a failure of a claimed obligation, or a conflict in which what the system holds meets a claimed obligation only by failing a protected one (Part XI), when the system represents it" FOUND L429. "predict displacements correctly" FOUND L628. "a represented target and criticism in its history": NOT FOUND (L201 reads "a selected transport has no represented target and no criticism in its history; a constructed one has both"). "A problem that a system represents can be a recognized difficulty (Part X)" FOUND L317.

**X05.2 · Atria · G · point 4 (T2).** Attack: ORDER with one appended clause. Reported as failing: the sentence carries two claims beyond the restatement (a constructed transport's failure "is violated, and the failure is not surprise"; the link to recognized difficulty, stated nowhere in the current text); CLAIM right; the declaration names all three parts.
- "restating its definitions" FOUND brief G §4 l.566 (the declaration). "is violated, and the failure is not surprise" FOUND L223. "can be a recognized difficulty (Part X)" FOUND L223.

**X05.3 · Atria · G · point 6 (T3).** X04 and X05 interlock: X05's link needs a violation the system represents, which (R) withholds from declared transports; L225 and L429 stay consistent; L223's unchanged sentences stay true.
- "a violation *the system represents*" FOUND L223. "does not make an occurrence represent anything" FOUND L211. "A system with no transport cannot be surprised" FOUND L223. "A system whose history exhausts its contract cannot be surprised" FOUND L223.

**X05.4 · Atria · G · point 8 (T4).** O23, O13, O3, O24, O11, O48 and O5 do not move away.
- "A dimension of variation mentioned in passing is not thereby a port of the account" FOUND L425.

**X05.5 · Atria · G · point 9 ((a)).** As X04.5.

**X05.6 · Mimo · G · point 1 (T1, T2).** The restatement drops the block's occurrence scoping: L217 defines for a pair "actually occurring", but L223 says a constructed transport "that fails at a pair of its contract is violated", so a failure at a pair that never occurs would be a violation, which the definitions do not support and which in O24 would turn a fact about fit and rivals into an event; the declaration repeats the unscoped phrase; the third clause is a link to L429 rather than one of the definitions (so CLAIM is right). Proposed wording, then declaration:

~~~~text
Whether the correspondence could have been otherwise at such a change is a fact about its population (Derivation 3). Expectation and violation are defined for every transport to the simulation layer, surprise only for a selected one: a constructed one whose fidelity fails at a pair of its contract that actually occurs is violated, and the failure is not surprise; a violation the system represents can be a recognized difficulty (Part X).
~~~~

~~~~text
Part IV now says, restating its definitions, that expectation and violation are defined for every transport to the simulation layer and surprise only for a selected one; that a constructed transport to the simulation layer whose fidelity fails at a pair of its contract that actually occurs is violated, and the failure is not surprise; and, a link to Part X rather than one of those definitions, that a violation the system represents can be a recognized difficulty.
~~~~

- "Let \(t\) be a transport to the simulation layer \(S\) … For an edit–boundary pair \((a,b)\in C\) **actually occurring**:" FOUND L217. "a **violation** occurs when fidelity fails at \((a,b)\)" FOUND L220. "a constructed one that fails at **a pair of its contract** is violated" FOUND L223. "claims (F1), (F2) and (A) at every pair of \(C\), tested or not" FOUND L315. "a pair \((a,b)\in C\)" FOUND L369. "the signature of a selected transport **meeting a change** outside its history" FOUND L584. "the record has not chosen between them" FOUND brief G §7 l.646. "restating its definitions" FOUND brief G §4 l.566. "a violation the system represents can be a recognized difficulty (Part X)" FOUND L223. "A **recognized difficulty** is a failure of a claimed obligation … when the system represents it" FOUND L429.

**X05.7 · Mimo · G · point 7 (T3).** The present "every transport to the simulation layer" removes the earlier form's clash with L219 and L177; clause three points correctly at L429 and parallels L317; O13 and O23 are untouched.
- "defined for every transport" FOUND brief G §4 l.587 (the earlier reading's wording; also inside L223). "\(S\) is where expectation lives" FOUND L177. "every transport to the simulation layer" FOUND L223. "A problem that a system represents can be a recognized difficulty (Part X)" FOUND L317. "the contributions whose active routes ran to it" FOUND L307 (the reply cites L308). "A dimension of variation mentioned in passing is not thereby a port of the account" FOUND L425.

**X05.8 · Mimo · G · point 8 ((a)).** As X04.11.

No point on X05 was raised outside part G.

### 3.4 X06 · W20.1 · Part V, L231 · CLAIM · part H

**X06.1 · Atria · H · point 1 (T1).** A counterexample tried: a component \(j\) that assigns an input, on which the answer depends over a contract that never exercises the edit setting that input; X06 puts \(j\) outside \(\Gamma\), so (F1) never checks it and (B) never records it. Reported as failing: L103 makes such a contribution provisional, L255 forbids resting the answer on a value assigned to a settable port, and (F2) still checks the assembled organization; no listed situation turns on it.
- "including any that assigns an input" FOUND L231. "moving an assertion from an input slot into a component named 'law' does not discharge this" FOUND L255 (the text puts "law" in double quotes).

**X06.2 · Atria · H · point 2 (T2).** Attack: WORDING, not CLAIM. Reported as failing: membership in \(\Gamma\) now turns on the candidate's offer rather than someone's identification, so O45's undescribed second spring is a commitment from the start; the declaration states exactly the two additions.
- "an identified set \(\Gamma\) of active commitments in \(E\)" FOUND L231. "those the candidate offers as doing the work, whether or not anyone has described their work" FOUND L231. "the named background of Part VI" FOUND L231. "whether or not described": own abbreviation.

**X06.3 · Atria · H · point 3 (T3).** The "named background" looks mutually referential (L231 points to Part VI; L287 names nothing); reported as failing, since X06 is the naming and Part V precedes Part VI. Optional phrase offered: "A tighter phrasing ("what Part VI calls the named background") would be smoother but changes no claim." Exact words: `what Part VI calls the named background`
- "the named background of Part VI" FOUND L231. "with the named background fixed" FOUND L287.

**X06.4 · Atria · H · point 4 (T4).** X06 moves O45 and N1 toward their fixed verdicts, inside the declaration; O46, O36, O47, O2, O5 and O7 are untouched.
- "whether or not anyone has described their work" FOUND L231. "a route already present in the candidate is a route whether or not anyone has described its work" FOUND L307. "an unsupported belief riding along with a good explanation, not a part of it" FOUND brief H §7 l.600. "Yes, Tomas explains the seasons" FOUND brief H §7 l.600. "identified active commitment": own words (a reading of the old wording).

**X06.5 · Atria · H · (d) X06: RIGHT.** Admitted pairs are forced (what is not admitted is not testable, and with no conflict there is nothing to settle); "or outside it" is needed for second-kind problems; recodings and inert no-work parts fall outside, and X06 makes the no-work case expressible; what is given up follows from the owner's rule against grading and counting.
- "at some admitted edit–boundary pair of the target that both their transports translate, in \(C\) or outside it" FOUND L315. "a conflict between ideas that what the assessor has established has not settled" FOUND L317. "two discovered variations that fit": NOT FOUND (the owner's words, brief H §2 l.28, read "If two discovered variations fit, that constitutes a problem").

**X06.6 · Mimo · H · point 1 (T1).** The two halves of the sentence contradict for a candidate that offers an input-assigning component as doing the work, and the text supplies one: Part VII's stipulation "Set \(b_B=0\) …" (L331) is offered as the support and assigns the bias port, which calibration edits set; as background it would sit in every \(E|W\), no \(G\subseteq\Gamma\) could delete it, and "its support is circular" would have no object. Proposed replacement, whole:

~~~~text
and an identified set \(\Gamma\) of active commitments in \(E\). The commitments \(\Gamma\) are components of \(E\), those the candidate offers as doing the work, whether or not anyone has described their work, except that a component that assigns an input is never one of them; the boundary conditions of \(E\) (its \(B\), Part II) and the components of \(E\) outside \(\Gamma\) belong to the named background that Part VI holds fixed in \(E|W\).
~~~~

- "The commitments \(\Gamma\) are components of \(E\), those the candidate offers as doing the work" FOUND L231. "the components of \(E\) outside \(\Gamma\), **including any that assigns an input**, belong to the named background of Part VI" FOUND L231. "A port \(v\) is an **input** under \(A\) when \(A\) contains an edit that sets \(v\) directly" FOUND L109. "An edit that sets a port replaces the component assigning that port" FOUND L103. "'Set \(b_B=0\) because it gives the mass I favour' is not an inference from the readings; **its support is circular** though its content might be true." FOUND L331 (the text uses double quotes). "an independent calibration can" FOUND L329 (the reply cites L330). "let \(E|W\) retain the commitments in \(W\) with the named background fixed" FOUND L287.

**X06.7 · Mimo · H · point 2 (T3).** The partition makes two standing sentences false or stale. (a) L245 says (F1) entails that every component of \(E\) has its anchor's signature, but (F1) binds only active components and X06 guarantees components outside \(\Gamma\); proposed replacement of L245's sentence:

~~~~text
By (K), (F1) entails that every active component of \(E\) has the signature of its anchor; there is no further condition about kinds to state (Derivation 1).
~~~~

(b) L299's "commitments outside \(\Gamma\)" now names nothing, since components outside \(\Gamma\) are background: replace "commitments outside \(\Gamma\)" with `components outside \(\Gamma\)`; and Derivation 1's Corollary (L558, "each component must anchor to a component of the same kind") should read `each active component`.
- "By (K), (F1) entails that **every component of \(E\)** has the signature of its anchor" FOUND L245. "For every **active component** \(k\) of \(E\)" FOUND L233. "every active component \(k\) of \(E\)" FOUND L554. "not a support someone could write with **commitments** outside \(\Gamma\)" FOUND L299. "each component must anchor to a component of the same kind" FOUND L558.

**X06.8 · Mimo · H · point 3 (T3).** "boundary values" is not a defined term (the datum is \(B\), "a set of boundary conditions"), and "belong to the named background of Part VI" sends the reader to Part VI, which only holds the background fixed; both are repaired by X06.6's wording.
- "\(B\) is a set of boundary conditions" FOUND L91. "\(\sigma\) translates boundaries" FOUND L119, L189. "an unanalysed boundary input" FOUND L255. "its independent boundary conditions" FOUND L255. "boundary values" FOUND L231. "belong to the named background **of Part VI**" FOUND L231. "with the named background fixed" FOUND L287. "the boundary conditions of \(E\) (its \(B\), Part II) … the named background that Part VI holds fixed in \(E|W\)": own words (X06.6's proposal).

**X06.9 · Mimo · H · point 4 (T2).** CLAIM is the right kind; the declaration mirrors the new wording "including its defect". Proposed declaration:

~~~~text
Part V now types a candidate's commitments: they are components of its organization, those the candidate offers as doing the work, whether or not anyone has described their work, except that a component that assigns an input is never a commitment; and the organization's boundary conditions and its other components belong to the named background that Part VI holds fixed.
~~~~

- "an identified set \(\Gamma\) of active commitments in \(E\)" FOUND L231. "the components of \(G\) are deleted from \(E\)" FOUND L255. "whether or not anyone has described their work" FOUND L231.

**X06.10 · Mimo · H · point 5 (T4).** No listed situation moves away; the O45 move is declared; on N1 the sun god is either a no-work commitment or, if it assigns an input, background, and the account stands either way.
- "whether or not anyone has described their work" FOUND L231. "A route already present in the candidate is a route whether or not anyone has described its work" FOUND L307. "a component reassigned to a new target after a deletion belongs to a new candidate with its own assessment" FOUND L307. "every support stays a support after \(d\) is added to it and after \(d\) is removed from it" FOUND L313. "an account whose only substantive component restates the answer it was asked for" FOUND L273.

**X06.11 · Mimo · H · (d) X06: RIGHT, WITH A LOSS.** The condition keeps mechanism rivals (the anchor clause) and correctly excludes recodings and inert no-work parts, but drops two things: (i) variations that differ only where no admitted change reaches are never rivals and pose no problem, though the owner's words make two discovered variations that fit a problem; (ii) rivalry needs an offer "in place of the other", where the owner makes discovery sufficient; and a transport that does not translate a pair never conflicts there. (Also listed under X09, §3.5.)
- "Two components no admitted change can separate are one kind at that level" FOUND L11. "two of their active components with one anchor have different relations there" FOUND L315. "conflict[s] at no pair (Part VIII, Recoding; Derivation 8)" FOUND L315. "the sun god, who approves" FOUND brief H §7 l.596. "the sun god, who is indifferent": own words. "If two discovered variations fit, that constitutes a problem" FOUND brief H §2 l.28. "a candidate that nobody has offered is no one's rival" FOUND L315. "in place of the other" FOUND L315.

No point on X06 was raised outside part H.

### 3.5 X09 · W59.1, "Rivals" · Part VI, L315 · CLAIM · part A

**X09.1 · Atria · A · point 1 ((c2), T3).** "Established" (L315, through Part IX's receipts) does not settle whether a failure found by examining the candidate itself (of non-circular dependence, of non-vacuity, a component anchored to nothing) is established; since "fits" gates the problems of L317, a candidate whose circularity has been caught would still fit and could pose or share a problem. Proposed insertion after the "fits" sentence of L315, before "No list of all rivals is supposed":

~~~~text
A verification the assessor holds is a receipt for what it verifies. A failure of non-circular dependence, a contradiction inside the candidate, or a component anchored to nothing, is found by examining the candidate itself and not the world; the verification is an argument application whose premises are the definitions and the adopted physics it relies on, usable while those premises are live (K2), and telling against the candidate only together with them (K3). A candidate with such a failure established against it therefore does not fit, whether or not anything is established about the world.
~~~~

The reply adds that this brings back no record, the receipt being the assessor's evidence state, as with L369's "with no record of which candidates failed before".
- "until what is established leaves at most one of them fitting" FOUND L317. "A result is **established** for an assessor who holds a usable receipt for it (Part IX)" FOUND L315. "A candidate **fits** … when no result established for that assessor shows it failing a condition of (E)" FOUND L315. "An evidence leaf is a reference to an event with an interpreted claim. A receipt is a derivation tree over leaves" FOUND L397. "the test that yields it" FOUND L315, L369 (the reply attributes the words to (K3), line 395; they stand at L315 and L369). "No list of all rivals is supposed" FOUND L315. "with no record of which candidates failed before" FOUND L369.

**X09.2 · Atria · A · point 2 (T2).** The declaration is silent on "A candidate offered for \(p\) is offered for the whole of \(p\) …"; the reply calls this ORDER-like (L262, L367) and "a small incompleteness, not an error"; the kind CLAIM is right. Not pressed as a challenge. No wording.
- "A candidate offered for \(p\) is offered for the whole of \(p\): it claims (F1), (F2) and (A) at every pair of \(C\), tested or not, …" FOUND L315.

**X09.3 · Atria · A · point 3 (T1).** No falsehood found; tried a recoding (Derivation 8), a candidate with and without an idle commitment (N1), O24's two arrangements, and the second disjunct of conflict against Derivations 2 and 3. No wording.
- "conflict at no pair" FOUND L315.

**X09.4 · Atria · A · point 4 (T4).** No verdict moves away; moves toward are declared (N25, D3-T, O48, O36, O24; N1, N3, N7, N5, O46, N2 rest on unchanged text). No wording.
- "Nor are rivals a selection population … fixed by its population (Derivation 3)" FOUND L315. "it must be a member of \(\mathcal T\) … and it must survive on \(H\)" FOUND L572. "nobody has offered" and "no one's rival" FOUND L315.

**X09.5 · Atria · A · point 5 (T3).** Pointers, notation and forward references resolve. No wording.
- "relations of the target that the adopted physics admits (Part I)" FOUND L315 (the reply says it rests on line 75).

**X09.6 · Atria · A · (a) X09: FAITHFUL.** The wording keeps hard to vary on discovered rivals and problems and keeps out lists, counts, grades and records; one narrowness is noted "not a fault": "offered as an answer to \(p\) in place of the other" is slightly tighter than the owner's words.
- "No list of all rivals is supposed: a candidate's rivals are among the candidates someone has offered, …" FOUND L315. "Nor are rivals a selection population: …" FOUND L315. "Nothing here counts rivals, grades a candidate or ranks candidates" FOUND L317. "from the candidate's own answer there, with no record of which candidates failed before or of how any was changed." FOUND L369. "one of them has been offered as an answer to \(p\) in place of the other" FOUND L315. "two discovered variations that fit": NOT FOUND (the owner's words, brief A §2 l.28, read "If two discovered variations fit, that constitutes a problem"). "a rival is a discovered competitor" FOUND brief A §2 l.32.

**X09.7 · Atria · A · (c2) X09: UNSETTLED BY THE TEXT.** "Result" is unrestricted and a verification arguably fits Part IX's receipts, but (K3)'s test and the evidence leaf point at empirical tests; it should be settled by X09.1's repair; what turns on it is whether a candidate with a caught structural failure still fits, and whether examining the candidate can solve a problem, since X10's named solver is a test that "cannot catch a circularity at all".
- "A result is established for an assessor who holds a usable receipt for it (Part IX)" FOUND L315. "the test that yields it" FOUND L315, L369. "evidence leaf … reference to an event" FOUND L397.

**X09.8 · Atria · A · (d) X09: RIGHT.** Candidates differing only by a no-work part, or only in writing, correctly fall outside rivals; nothing the theory should keep is lost (Derivation 2's Consequence; the remedy is a finer contract). No new quotations.

**X09.9 · Mimo · A · point 1 (T1, T3).** The exclusion sentence reverses on a literal parse: in "… conflict at no pair (…), and nor do two candidates, however differently they are cut, that some such relations … would let both meet …; neither pair is a pair of rivals", the elided verb phrase is "conflict at no pair", and "nor do [they conflict at no pair]" reads as "they conflict at some pair", the opposite of the declaration, settled only by the last clause. Repaired in X09.13's replacement wording.
- "...one carried onto the other by a structure-preserving bijection that takes its transport with it and leaves its answers as they are, **conflict at no pair** (Part VIII, Recoding; Derivation 8), **and nor do two candidates**, however differently they are cut, …" FOUND L315 (bold added by the reply). "neither pair is a pair of rivals" FOUND L315. "...are not rivals" FOUND brief A §4 l.487 (the declaration). "nor do these candidates [conflict at no pair]" and "these candidates conflict at some pair": own words (the parse).

**X09.10 · Mimo · A · point 2 (T1).** The illustration "as when two of their active components with one anchor have different relations there" is not an instance of the defined conflict. Counterexample: \(E\) has \(k_1\) with \(\{y\ge x\}\) and \(k_2\) with \(\{y\ge x+1\}\), both anchored to one subnetwork; \(E'\) has \(k'\) with \(\{y\ge x+1\}\); their solution sets and answers coincide, and \(E\) can never meet (F1), so neither disjunct fires, yet \(k_1\) and \(k'\) have one anchor and different relations. Repair: make the anchor clash a disjunct of its own (in X09.13's wording). The reply links the \(k_1/k_2\) clash to question (c2)'s "contradiction inside the candidate".
- "their answers there differ, **or** when each of them could meet (F1), (F2) and (A) there under some relations of the target that the adopted physics admits (Part I) and no such relations let both, **as when two of their active components with one anchor have different relations there**" FOUND L315 (bold added). "two of their active components with one anchor [having] different relations there" FOUND L315 (bracketed alteration). "contradiction inside the candidate" FOUND brief A §5 l.518.

**X09.11 · Mimo · A · point 3 (T2).** The declaration omits one claim (a candidate offered for \(p\) is offered for the whole of \(p\), including untested pairs, which is load-bearing for O24 and for "Problems") and compresses another (it drops the bijection condition and "both translate" from the two non-rival pairs). Exact additions to the declaration (the block also carries the (c2) sentence of X09.14):

~~~~text
It says that a candidate offered for p is offered for the whole of p: it claims (F1), (F2) and (A) at every pair of C, tested or not, and the rest of (E) on C, while outside C it claims nothing on p. It says that a failure which inspecting the candidate itself shows — a component anchored to nothing, a failure of non-circular dependence, a contradiction inside the candidate — is a result established for an assessor who holds a usable receipt for the inspection, and needs no test of the target. Where the declaration says of the two non-rival pairs, "two candidates that differ only in how they are written", it means differ only in how they are written and be carried one onto the other by a structure-preserving bijection that takes its transport with it and leaves its answers as they are; and "at each admitted pair" means at each admitted pair both translate.
~~~~

- "A candidate offered for \(p\) is offered for the whole of \(p\): it claims (F1), (F2) and (A) at every pair of \(C\), tested or not, and the rest of (E) on \(C\)" FOUND L315. "Two candidates that differ only in how they are written ... are not rivals" FOUND brief A §4 l.487 (the declaration). "one carried onto the other by a structure-preserving bijection that takes its transport with it and leaves its answers as they are" FOUND L315. "both translate" FOUND L315. "at each admitted pair" FOUND L315.

**X09.12 · Mimo · A · point 4 (T4).** No verdict moves (N1, N25, O24, D3-T, O48, O36, N7, O46, N5); on N25 the attack that the dog and turtle differ only in a label fails, because (K) fixes kind identity of components while (A) individuates answers.
- "Strike it out and the account works exactly as before" FOUND brief A §7 l.549. "two components that differ only in those values are of one kind on \(C\), whatever the difference is called" FOUND L119. "both stories cannot be true" FOUND brief A §7 l.582. "whether or not anyone can establish what it does" FOUND L317. "nothing anyone could see ... depends on which is true" FOUND brief A §7 l.582. "the record has not chosen between them" FOUND brief A §7 l.588. "Nor are rivals a selection population: …" FOUND L315. "a candidate that nobody has offered is no one's rival" FOUND L315. "The rule itself cannot tell him which reading to trust." FOUND brief A §7 l.634.

**X09.13 · Mimo · A · replacement wording (for the whole paragraph "Rivals", carrying the repairs of X09.9, X09.10 and X09.14):**

~~~~text
**Rivals.** Two explanatory candidates for one question \(p\) are **rivals** when one of them has been offered as an answer to \(p\) in place of the other and they conflict at some admitted edit–boundary pair of the target that both their transports translate, in \(C\) or outside it. Two candidates **conflict** at such a pair \((a,b)\) when their answers there differ, when two of their active components have one anchor and different relations there, or when each of them could meet (F1), (F2) and (A) there under some relations of the target that the adopted physics admits (Part I) and no such relations let both. A candidate offered for \(p\) is offered for the whole of \(p\): it claims (F1), (F2) and (A) at every pair of \(C\), tested or not, and the rest of (E) on \(C\); outside \(C\) it claims nothing on \(p\), but what its organization and transport give there can conflict with what another's give. Two candidates that differ only in how they are written, one carried onto the other by a structure-preserving bijection that takes its transport with it and leaves its answers as they are, do not conflict at any pair (Part VIII, Recoding; Derivation 8); nor do two candidates conflict at any pair, however differently they are cut, when some such relations of the target would let both meet (F1), (F2) and (A) at each admitted pair both translate. Neither pair is a pair of rivals. A result is **established** for an assessor who holds a usable receipt for it (Part IX); by (K3), a result that tells against a candidate tells against it only together with the background and instruments of the test that yields it. A candidate **fits** what is established for an assessor when no result established for that assessor shows it failing a condition of (E); a failure that inspecting the candidate itself shows — a component anchored to nothing, a failure of non-circular dependence, a contradiction inside the candidate — is such a result once the assessor holds a usable receipt for the inspection, and needs no test of the target. No list of all rivals is supposed: a candidate's rivals are among the candidates someone has offered, and a candidate that nobody has offered is no one's rival. Nor are rivals a selection population: whether a selected transport is underdetermined at an unseen pair is fixed by its population (Derivation 3), whatever rivals anyone offers.
~~~~

**X09.14 · Mimo · A · (c2) X09: UNSETTLED BY THE TEXT.** Receipts could carry an inspection of the written candidate, but "established" is introduced beside tests and L369 ties it to the target's answer; it should be settled, because "fits" gates problems: if inspection failures do not count, a candidate broken on inspection "fits for ever, pairs with any rival, and holds a problem open that reading alone closes"; if they count, easy to vary can be charged only against candidates that survive inspection ("this pulls on the companion item X10"). Words to add after the "fits" sentence:

~~~~text
a failure that inspecting the candidate itself shows — a component anchored to nothing, a failure of non-circular dependence, a contradiction inside the candidate — is such a result once the assessor holds a usable receipt for the inspection, and needs no test of the target.
~~~~

- "A result is established for an assessor who holds a usable receipt for it (Part IX)" FOUND L315. "a derivation tree over leaves" FOUND L397. "evidence leaf" and "a reference to an event with an interpreted claim" FOUND L397. "the target's answer at \((a,b)\)" FOUND L369.

**X09.15 · Mimo · A · (a) X09: FAITHFUL.** The owner's correction is built in twice (no list of rivals; rivals are not a selection population); nothing counts, grades or ranks; residual worry: "offered … in place of" is narrow if it means replacement of that particular other (two sibling variations of one original could escape rivalry); on the natural reading it renders "discovered competitor".
- "No list of all rivals is supposed: …" FOUND L315. "Nor are rivals a selection population: …" FOUND L315. "Once the explanation is rescued, the mistake shouldn't be able to creep back in" FOUND brief A §2 l.28. "with no record of which candidates failed before or of how any was changed" FOUND L369. "harder to fit" FOUND brief A §2 l.28. "one of them has been offered as an answer to \(p\) in place of the other" FOUND L315. "variation is a competitor" FOUND brief A §2 l.28. "discovered competitor" FOUND brief A §2 l.32. "as a replacement of that particular other": own words.

**X09.16 · Mimo · A · (d) X09: RIGHT, WITH A LOSS — a conflict at a pair only one of the two transports translates is not counted.** Requiring conflict at an admitted pair is right and excludes the two named classes; per-pair form loses nothing to joint incompatibility; the loss is one of reach: the paragraph says what an organization and transport give outside \(C\) "can conflict with what another's give", yet counts only pairs "that both their transports translate".
- "are supplied independently for each \((a,b)\)" FOUND L574. "that both their transports translate" FOUND L315. "outside \(C\) it claims nothing on \(p\), but what its organization and transport give there can conflict with what another's give" FOUND L315.

**Raised outside part A (rule 11).** None of these counts X09 as examined by the model in its own part.

**X09.17 · Atria · B · point 1 and (c2) — raised outside its part.** The gap about internal failures is "upstream, in the notions X09 and Part IX supply"; the text should settle it, and "The settling clause belongs in X09 or Part IX, not in X10". The reply adds that a self-contradictory candidate has an empty answer profile and so conflicts with the target inside \(C\) (a first-kind problem), and that an unexamined circular candidate fits only for that assessor. Proposed clause (for X09 or Part IX):

~~~~text
A failure of (E) that is decidable from the candidate, the question and the
contract alone is established for an assessor who has examined the candidate,
without a test of the target; (K3) does not qualify it, because the failure is
in the candidate itself and rests on no background or instrument.
~~~~

- "no result established for that assessor shows it failing a condition of (E)" FOUND L315. "An evidence leaf is a reference to an event with an interpreted claim. A receipt is a derivation tree over leaves" FOUND L397. "pose, **for that assessor**" FOUND L317. "is independent of whether anyone accepts it" FOUND L67. "only together with the background and instruments of the test that yields it" FOUND L315 (the reply cites L395).

**X09.18 · Mimo · B · point 3 and (c2) — raised outside its part.** (c2) X10: ESTABLISHED. The fit clause names "a condition of (E)", receipts are proposition-general, and Part VIII already derives an exclusion from the candidate's own answer, so a derivation over the candidate's own content is an established result; the (K3) gloss is a caveat on reach, not a restriction. If the drafters want the room gone, insert after "…shows it failing a condition of (E)" (L315): `A result may show this from the candidate's own content, by analysis; it need not come from a test.`
- "no result established for that assessor shows it failing **a condition of (E)**" FOUND L315. "(F1), (F2) and (A) … and the rest of (E) on \(C\)" FOUND L315. "For \(\phi\), \(P_j(\phi)\) and \(N_j(\phi)\) are the usable receipts for and against." FOUND L397. "this is established for that assessor of every such candidate alike, **from the candidate's own answer there**, …" FOUND L369. "the background and instruments of **the test that yields it**" FOUND L315. "this component restates the answer" and "this component's anchor is empty": own words (examples).

**X09.19 · Atria · C · (c2) X14 — raised outside its part.** UNSETTLED BY THE TEXT; it should be settled "in favour of the inspection reading for candidate-side facts, with receipts reserved for target-side and world-side claims"; otherwise a provably circular rival would still fit and the assessor would be sent to test the world. No wording.
- "a condition on how supplied relations behave under the changes in \(C\)" FOUND L265 (the reply cites L231 and L265). "reference[s] to an event" FOUND L397. "no result established for that assessor shows it failing a condition of (E)" FOUND L315. "from the candidate's own answer there" FOUND L369.

**X09.20 · Mimo · C · point 1 and (c2) — raised outside its part.** UNSETTLED BY THE TEXT; it should be settled for establishment, by a receipt whose leaf is the candidate's own content, with (K3) reading the definitions, declared indices and reading convention as background. Words for Part IX (Receipts), which is not an item: `A leaf may reference a candidate's own content; where a derivation over that content shows a condition of (E) unmet, the result is established on a usable receipt, and (K3) takes the definitions, the declared indices and the reading convention as background and instruments.`
- "the assessor holds a usable receipt for the target's answer at \((a,b)\) (Part IX), and by (K3) the test that yields it …" FOUND L369. "A result is **established** for an assessor who holds a usable receipt for it (Part IX)" FOUND L315. "establishing it, the target's relations as well as its answer where their answers there agree" FOUND L317. "a derivation tree over leaves", "evidence leaf", "a reference to an event with an interpreted claim" FOUND L397. "no result established for that assessor shows it failing a condition of (E)" FOUND L315.

**X09.21 · Atria · K · on X17 · T3 — raised outside its part.** The dependence order at L526 places none of rivals, conflict, established, fits and problem, so Derivation 6's claim, proved "By the dependence order of Part XIV", is not carried by the order as written; "The gap predates X17 and belongs to the items that introduced lines 315/317." The order is called "incomplete, not untrue". No wording.
- "(S), (B), (D) depend on (E)" FOUND L526. "Every predicate in Parts II–XIII is defined from Θ (including Org_ℓ) and, where invoked, 𝒩, together with declared indices and declared inputs" FOUND L596. "By the dependence order of Part XIV" FOUND L598.

**X09.22 · Mimo · K · point 2 — raised outside its part.** The order stays true (nothing in Part VI feeds back; the closing clause survives) but does not place the new notions, nor (K2), (K3) or receipts, though L598 rests on the order as listing "the definitions that rest on them". Words offered for the order: `Rivals, conflict, problems and easy to vary rest on (E), on the relations the adopted physics admits, and on acts of offering; established and fits rest on receipts, (K2), (K3) and (E).`
- "relations of the target that the adopted physics admits (Part I)" FOUND L315. "a usable receipt for it (Part IX)" FOUND L315. "A record reconstructed from the claim it is meant to support is not a receipt for that claim" FOUND L397. "which lists the declared indices and the declared inputs with the definitions that rest on them" FOUND L598.

**X09.23 · The (d) paragraphs of parts D, F and H — raised outside its part.** Question (d) asked, of X08, X03 and X06, whether the condition of L315 is right.
- Atria D, (d) X08: RIGHT. Recodings fall outside; candidates differing by a no-work commitment fall outside when it is inert at every admitted pair; a commitment idle on \(C\) that binds outside \(C\) makes rivals, correctly. Quotations checked: "good explanations make bad ones harder to fit" FOUND brief D §2 l.28; "more reach constrains variation" FOUND brief D §4 l.547 (old wording).
- Mimo D, (d) X08: RIGHT. "in \(C\) or outside it" is needed for N3 and N2; X08's "does no work" is over \(C\) only, so the two notions can come apart. Quotations: "two candidates that differ only in how they are written, one carried onto the other by a structure-preserving bijection … conflict at no pair" FOUND L315; "fitting the facts is not enough" FOUND brief D §7 l.649; "an unsupported belief riding along" FOUND brief D §7 l.618 (N1's verdict; the reply attributes it to Part IV); "both stories cannot be true" FOUND brief D §7 l.637; "no observation could ever favour one" FOUND brief D §7 l.633; "whether or not anyone can establish what it does" FOUND L317.
- Atria F, (d) X03: RIGHT (X03.5); notes that a narrow reading of "offered … in place of the other" would lose something and that L315's gloss fixes the broad reading.
- Mimo F, (d) X03: RIGHT, WITH A LOSS (X03.9): "easy to vary" cannot be said of N25's swappable picks.
- Atria H, (d) X06: RIGHT (X06.5).
- Mimo H, (d) X06: RIGHT, WITH A LOSS (X06.11): variations differing only where no admitted change reaches are never rivals; rivalry needs an offer "in place of the other", where the owner makes discovery enough.

### 3.6 X10 · W59.1, "Problems" · Part VI, L317 · CLAIM · part B

**X10.1 · Atria · B · point 1 ((c2)).** "Both fit" leaves internal failures unresolved, but the reply holds the gap is upstream (X09, Part IX) and X10 uses the notions correctly; X10's claims stay true on either reading of "established"; the settling clause belongs in X09 or Part IX and "X10 needs no change". Wording and quotations: see X09.17.

**X10.2 · Atria · B · point 2 (T1).** Attack on "a test that solves the problem whatever it shows" (neither rival may meet the conditions) and on "an answer it refutes stays refuted" as an undeclared claim; reported as failing ("at most one" is met by zero; Part VIII already carries persistence).
- "a test that solves the problem whatever it shows" FOUND L317. "an answer it refutes stays refuted on p (Part VIII)" FOUND L317. "At most one of them fits" FOUND L317. "stays failed… from the candidate's own answer there, with no record of which candidates failed before" FOUND L369. "solved": own word.

**X10.3 · Atria · B · point 3 (T1).** Attack on "a test inside C can refute one of them without the other only for a failure of its own"; reported as failing, the sentence being about a test's power to adjudicate between rivals.
- "a test inside C can refute one of them without the other only for a failure of its own" FOUND L317.

**X10.4 · Atria · B · point 4 (T2).** CLAIM and "change of claim" are right; every sentence of the wording is in the declaration.
- "It is of one of two kinds" FOUND L317. "change of claim" FOUND brief B §4 l.506.

**X10.5 · Atria · B · point 5 (T3).** Every pointer lands; the terms are defined at L315 before L317 uses them; (D) at L301 is a separate notion. No quotations beyond single words.

**X10.6 · Atria · B · point 6 (T4).** No move away (O1, N4, D3-T, O48, O24; N2, N3, N5, N1, O27 framed, not moved).
- "A contract narrowed to leave out the pairs at which two rivals conflict… solves nothing on p, and the problem for p stands" FOUND L317. "whether a candidate is an account of a question is fixed by the candidate, the question and the world, not by when anyone first asks the question" FOUND L317. "already accounted for it" FOUND brief B §7 l.609. "nobody had explained it" FOUND brief B §7 l.610. "one reachable setting is enough" FOUND brief B §7 l.600.

**X10.7 · Atria · B · point 7, (a) X10: FAITHFUL.** Easy to vary is stated only through discovered rivals and problems; the forbidden devices are disclaimed; the symmetry keeps it from being a grade.
- "Two rivals that both fit what is established for an assessor pose, for that assessor, a problem for p" FOUND L317. "A candidate is easy to vary… when it and a rival pose a problem of the second kind" FOUND L317. "if two discovered variations fit, that is a problem": NOT FOUND (the owner's words, brief B §2 l.28, read "If two discovered variations fit, that constitutes a problem"). "among the candidates someone has offered" FOUND L315. "Nothing here counts rivals, grades a candidate or ranks candidates" FOUND L317. "the term says nothing about which of them is right" FOUND L317. "No list of all rivals is supposed" FOUND L315. "stands until what is established leaves at most one of them fitting" FOUND L317. "from the candidate's own answer there, with no record of which candidates failed before" FOUND L369. "the mistake shouldn't be able to creep back in" FOUND brief B §2 l.28.

**X10.8 · Atria · B · point 8, (c1) X10: HARMLESS.** Digested in §6.1.
- "makes a new question… on which… they pose a problem of the first kind while both fit" FOUND L317. "its details… could be swapped for others that fit the Greeks' facts just as well" FOUND brief B §7 l.582.

**X10.9 · Atria · B · point 9, (c2) X10: UNSETTLED BY THE TEXT.** Digested in §6.2.
- "only together with the background and instruments of the test that yields it" FOUND L315 (the reply cites L395).

**X10.10 · Mimo · B · point 1 (T1).** Attack: "where their answers there agree" may restrict "its answer", so that where the answers differ the test would establish only the relations; reported as failing (the object of "establishing it" is carried from the preceding clause; the next clause presupposes refutation; the relations fix the answer). "The wording is compressed, not false."
- "establishing it, the target's relations as well as its answer where their answers there agree, is a **test** …" FOUND L317. "its relations as well as its answer" FOUND brief B §4 l.508 (the declaration). "whether or not anyone can establish what it does; establishing it, …" FOUND L317.

**X10.11 · Mimo · B · point 2 (T1).** Tried to build a second-kind pair that a test inside \(C\) separates for a reason not the refuted candidate's own; reported as failing.
- "a test inside \(C\) can refute one of them without the other only for a failure of its own" FOUND L317.

**X10.12 · Mimo · B · point 3 (T3, (c2)).** Attack: if only tests yield results, a second-kind problem could never close and a defective rival would keep a clean candidate "easy to vary" for good; reported as failing, because the fit clause reaches every condition of (E) and receipts can rest on the candidate's own content. Quotations: see X09.18.

**X10.13 · Mimo · B · point 4 (T2).** The declaration's paraphrase is the reading the paragraph forces; nothing is claimed that the declaration does not cover; CLAIM is right.
- "establishing what the target does there, its relations as well as its answer" FOUND brief B §4 l.508. "An answer it refutes stays refuted on \(p\) (Part VIII)" FOUND L317. "while both fit" FOUND L317. "Two rivals that both fit what is established … pose … a problem" FOUND L317.

**X10.14 · Mimo · B · point 5 (T3).** The definition of easy to vary drops the assessor index that the opening sentence carries; reported as failing (the index is inherited through "fits"). Optional phrase: ""For that assessor" would be smoother; without it the text is not incoherent." Exact words: `For that assessor`
- "pose, **for that assessor**, a problem" FOUND L317. "A candidate is **easy to vary** … when it and a rival pose a problem of the second kind" FOUND L317.

**X10.15 · Mimo · B · point 6 (T4).** No verdict moves away (N4, N2, N3, O24, D3-T, O48, O1, O27, N1, N5).
- "whether a candidate is an account of a question is fixed by the candidate, the question and the world, not by when anyone first asks the question or by whether anyone has checked the candidate against it (Parts I and V)" FOUND L317. "the yearly return is simply written into the terms of the bargain" FOUND brief B §7 l.580. "its details could be swapped for others that fit": NOT FOUND (N3 reads "Its details (which gods, what bargain, why grief brings cold) could be swapped for others that fit", brief B §7 l.582; the parenthesis is dropped without a mark). "(i) … whatever the target does there, at most one of them is an account of \(p\), whether or not anyone can establish what it does" FOUND L317. "the record has not chosen between them; one reachable setting is enough" FOUND (punct.) brief B §7 l.600 (two sentences in the case). "Nor are rivals a selection population: …" FOUND L315. "makes a different question; it solves nothing on \(p\)" FOUND L317. "an answer it refutes stays refuted" FOUND L317. "the rule itself cannot tell him which reading to trust" FOUND brief B §7 l.594.

**X10.16 · Mimo · B · (a) X10: FAITHFUL.** Stated only through a discovered rival and the problem they make; symmetric; no record does any work.
- "A candidate is **easy to vary**, in the sense used here, when it and a rival pose a problem of the second kind" FOUND L317. "Nothing here counts rivals, grades a candidate or ranks candidates" FOUND L317. "the term says nothing about which of them is right" FOUND L317. "the rival is then easy to vary too" FOUND L317. "an answer it refutes stays refuted on \(p\) (Part VIII)" FOUND L317. "with no record of which candidates failed before or of how any was changed" FOUND L369. "the problem for \(p\) stands until what is established leaves at most one of them fitting" FOUND L317.

**X10.17 · Mimo · B · (c1) X10: HARMLESS.** Digested in §6.1.
- "the contract does not contain their conflict" FOUND L317. "never as a grade" FOUND brief B §2 l.38.

**X10.18 · Mimo · B · (c2) X10: ESTABLISHED.** Digested in §6.2; the optional insertion is at X09.18.
- "a condition of (E)" FOUND L315. "from the candidate's own answer there" FOUND L369. "until what is established leaves at most one of them fitting" FOUND L317. "A criticism that a candidate is easy to vary must supply such a rival" FOUND L317.

**Raised outside part B (rule 11).**

**X10.19 · Atria · A · (c2) X09 — raised outside its part.** X10's named solver "is a test establishing what the target does, which cannot catch a circularity at all" (X09.7).

**X10.20 · Mimo · A · (c2) X09 — raised outside its part.** If inspection failures do not count, a broken candidate holds a problem open for ever; if they count, easy to vary can be charged only against candidates that survive inspection; "this pulls on the companion item X10" (X09.14).

**X10.21 · Atria · C · (c2) X14 — raised outside its part.** A provably circular rival would still fit, so the pair would pose a problem and the assessor would be sent to test the world (X09.19).

**X10.22 · Mimo · C · point 1 and (c2) X14 — raised outside its part.** If internal failures are never results, a candidate that fails (E) outright still fits, and with a sound twin can "pose a problem of the second kind", so the sound account is labelled easy to vary: "the theory would condemn a good account on the strength of a twin that is not an account at all" (X09.20).
- "pose a problem of the second kind" FOUND L317. "where both meet (E) on C both are accounts of p" FOUND L317.

**X10.23 · Mimo · F · (d) X03 — raised outside its part.** "easy to vary" is never said of N25's swappable picks (X03.9).

**X10.24 · Atria · K and Mimo · K, on X17 · T3 — raised outside its part.** The dependence order does not place "problem" or "easy to vary" (X09.21, X09.22; Mimo's words there include "problems and easy to vary").

**Related, not counted as a point on X10:** question (c1) was asked of X18 in part E about the same symmetry of L317; both replies there say HARMLESS (§6.1).

### 3.7 X11 · proposed WORDING · Part VII, L325 · part I

The proposal (reading rule, "What is cross-examined"): in "intervening on \(H\) changes the target's \(L\) but not the calculation's \(H\)" replace the last \(H\) by \(L\); KIND WORDING, REASON WORD erratum, no declaration.

**X11.1 · Atria · I · point 6 (T1).** Attack: perhaps the old symbol was right, the calculation's computed \(H\) staying at \(L\tan\theta\). Reported as failing: an edit that sets a port replaces the component assigning it, so under the reversed calculation an intervention on \(H\) sets the calculation's \(H\) and leaves its \(L\) unconstrained, while the target's \(L\) moves; (F2) fails in \(L\); the new symbol is the one L271 requires, and the old wording contradicted L271.
- "not the calculation's *H*" FOUND L325. "An edit that sets a port replaces the component assigning that port" FOUND L103. "intervening on the upstream port changes the target's downstream value but not the calculation's" FOUND L271.

**X11.2 · Atria · I · point 7 (T2, T3, T4).** WORDING is right: the claim that the reversed calculation is not faithful under the production contract is unchanged, and only the description of how it fails is corrected ("the erratum removes a false sub-claim rather than adding one"); with the change L325 agrees with L271; O6 and O4 do not move; the one-symbol change is the right repair.
- "the reversed calculation *H* = *L* tan θ is not [faithful] under this contract" FOUND L325 (pieces; bracketed insertion; the text reads "The reversed calculation \(H=L\tan\theta\) is not: …", and "under this contract" closes the sentence before it).

**X11.3 · Atria · I · (a), as a point.** "No bearing on rivals, variation, criticism or error correction; the rule is not engaged."

**X11.4 · Mimo · I · point 1 (T2).** WORDING is the wrong kind: the old wording names \(H\) as the port the intervention leaves unchanged, the new names \(L\), so a reader of the current text can conclude something the new wording withdraws; the item should be CLAIM. Proposed kind and declaration:

~~~~text
Kind: CLAIM.

Declaration: The revision corrects the port named in the last clause of the reversed-calculation sentence. The current text's sentence named \(H\) as the port unchanged by the intervention on \(H\); the revision names \(L\). The claim now stated in Part VII is the same one line 271 states of the same reversed calculation: intervening on the upstream port changes the target's downstream value but not the calculation's.
~~~~

- "the new wording says what the old wording said, in other words." FOUND brief I §1 l.10 (the definition of WORDING). "the calculation's \(H\) is unchanged by the intervention on \(H\)": own words (what the reply says a reader of the current text can conclude; L325 reads "… changes the target's \(L\) but not the calculation's \(H\)").

**X11.5 · Mimo · I · point 2 (T1, T3, T4).** The fix is correct and improves coherence: the mismatch that breaks (F2) is in \(L\); L325 and L271 now agree; no verdict moves; naming \(L\) is the minimal correction.
- "fails (F2) under the production contract: intervening on the upstream port changes the target's downstream value but not the calculation's." FOUND L271.

**X11.6 · Mimo · I · point 7 ((a), as a point).** "X11 raises no new (a) issue: the reversed calculation remains a rival assessed the same way; only the symbol naming the mismatch is corrected."

No point on X11 was raised outside part I.

### 3.8 X14 · W60.1 · Part VIII, "A failed answer stays failed", L369 · CLAIM · part C

**X14.1 · Atria · C · point 1 (T1).** Attack: "established of every such candidate" uses "established" outside its technical sense, a candidate's answer not being an event. Reported as failing: X14 anchors "established" on the target's answer, and reading a candidate's own answer is the theory's standard mode (L231, L265); the residue is question (c2).
- "established of every such candidate": NOT FOUND (L369 reads "this is established for that assessor of every such candidate alike"). "is established for an assessor who holds a usable receipt for it (Part IX)" FOUND L315. "a derivation tree over leaves" and "an evidence leaf is a reference to an event with an interpreted claim" FOUND L397. "is established for that assessor of every such candidate alike, **from the candidate's own answer there**" FOUND L369. "Here 'established' is meant as in Part VI: the assessor holds a usable receipt for the target's answer at (a,b) (Part IX)" FOUND L369 (quotation marks differ). "a condition on supplied relations under the changes in C" FOUND L231. "Every conjunct is a condition on how supplied relations behave under the changes in C. None inspects a label" FOUND L265. "with no record of which candidates failed before" FOUND L369.

**X14.2 · Atria · C · point 2 (T1).** Attack: "the exclusion ceases to be established" is too strong where a second usable receipt establishes the target's answer. Reported as failing: "the receipt" is the one the test produced; "At most a wording imprecision, not a falsehood; no verdict turns on it." No wording proposed.
- "If a premise about them ceases to be live, the receipt is not usable and the exclusion ceases to be established, for every such candidate alike" FOUND L369. "the test that yields it" FOUND L369.

**X14.3 · Atria · C · point 3 (T3).** Attack: contradiction with L317's "stays refuted". Reported as failing: "stays refuted" is the indexed fact and "ceases to be established" the assessor's warrant; X14 supplies the target that L317's pointer "(Part VIII)" lacked.
- "an answer it refutes stays refuted on p (Part VIII)" FOUND L317 (first use). "solves the problem whatever it shows, since afterwards at most one of them fits; an answer it refuted stays refuted on p (Part VIII)": NOT FOUND (L317 reads "an answer it refutes stays refuted"). "ceases to be established" FOUND L369. "A proposition indexed to a contract remains that proposition when a later theory changes the current contract" FOUND L367.

**X14.4 · Atria · C · point 4 (T2).** The declaration matches part by part; the core exclusion was derivable, but persistence across re-offerings and changes and the receipt-fragility of the warrant are stated here first, so CLAIM with "clarification" is right, not ORDER.
- "keeps y there" FOUND L369. "clarification" FOUND brief C §4 l.513.

**X14.5 · Atria · C · point 5 (T4).** No move on O1, D3-T, O27, O8, N7, N2 or O24.
- "no explanation of the floods, each limit honest alone, the series a retreat": NOT FOUND (O1's verdict, brief C §7 l.577, reads "Bruno has no explanation of the floods. Each limit is honest taken alone, and the series as a whole is a retreat."). "must be a member of 𝒯 … and it must survive on H" FOUND L572.

**X14.6 · Atria · C · (a) X14: FAITHFUL.** The exclusion is carried by the candidate's own content; the four-case list is four descriptions of one candidate's history under one condition; nothing enumerates, grades or records.
- "from the candidate's own answer there, with no record of which candidates failed before or of how any was changed" FOUND L369. "error correction is carried by the explanation itself" and "a record of rescues is redundant" FOUND brief C §2 l.32. "the candidate that gave y there and failed, that candidate offered again, a rival, or a changed candidate that keeps y there" FOUND L369. "every such candidate alike" FOUND L369. "whose answer at (a,b) is y" FOUND L369.

**X14.7 · Atria · C · (b) X14: HOLDS AS STATED.** On the same question the correction sticks, for every wrong value; a narrowed contract or changed query makes a new question and the failure on \(p\) stands; through (K3)/(K2) the warrant can lapse, and should; at an untested neighbouring pair the exclusion is not established; a change of grain or target is a new index.
- "an account on it does not answer p, and the failure on p stands" FOUND L369. "ceases to be established" FOUND L369. "no candidate is thereby shown to be an account" FOUND L369. "Withdrawing a premise removes a license; it does not make the conclusion false" FOUND L393. "at every pair of C, tested or not" FOUND L315. "missing evidence stays missing" FOUND L397. "slightly different": own words (echoing question (b), brief C §5 l.548, "only slightly").

**X14.8 · Atria · C · (c2) X14: UNSETTLED BY THE TEXT.** Digested in §6.2 (and X09.19).
- "a condition on how supplied relations behave under the changes in C" FOUND L265. "reference[s] to an event" FOUND L397. "no result established for that assessor shows it failing a condition of (E)" FOUND L315. "from the candidate's own answer there" FOUND L369.

**X14.9 · Mimo · C · point 1 ((c2)).** Whether a leaf may be the candidate's own content is unclassified; it should be settled for establishment, with words for Part IX (X09.20); "X14 states nothing contrary; it stands."

**X14.10 · Mimo · C · point 2 (T1).** The closing sentence is false if read generically: a contract \(C'\) that omits \((a_1,b_0)\), or a changed query agreeing with \(\mathcal Q\) on \(C\), can have an account that is also an account of \(p\). Reported as failing to defeat the item, since the paragraph's frame (a fixed failing answer) fixes the true reading; "the hazard is a wording hazard only". Optional exact wording: "(If the drafters want it closed: "being an account of it is not thereby an account of \(p\)".)" Exact words: `being an account of it is not thereby an account of \(p\)`
- "A contract that omits \((a,b)\), or a changed query, makes a different question (Part III): an account on it does not answer \(p\)" FOUND L369. "Fix a question \(p\), a pair \((a,b)\in C\) and a value \(y\neq\operatorname{Ans}_p(a,b)\)" FOUND L369. "an answer to one is not an answer to the other" FOUND L151. "an account on which does not answer the original" FOUND brief C §4 l.515 (the declaration).

**X14.11 · Mimo · C · point 3 (T2).** Every part of the declaration is true of the wording; its general form is the universal closure of the single-value schema, licensed by "Negation exchanges them"; CLAIM with "clarification" is right (it would be ORDER, with the places named, if derivability were held enough).
- "a candidate whose answer at a pair of the contract differs from the target's is not an account" FOUND brief C §4 l.515. "Fix … a value \(y\neq\operatorname{Ans}_p(a,b)\)" FOUND L369. "Negation exchanges them" FOUND L397. "the same holds on every question with the same target and query whose contract contains \((a,b)\)" FOUND L369. "an answer it refutes stays refuted on \(p\) (Part VIII)" FOUND L317.

**X14.12 · Mimo · C · point 4 (T3).** Three wording nits, "none fatal": (i) "the exclusion" is an undefined coinage and "the result" would carry the meaning; (ii) "established … of every such candidate alike" is loose; (iii) "a rival" could be misread as any rival. Pointers resolve; the apparent clash with L317 dissolves inside Part VI. Exact word offered for (i): `the result`
- "the exclusion" FOUND L369. "this is established … of every such candidate alike" FOUND L369. "whether it is … a rival …" FOUND L369. "whose answer at \((a,b)\) is \(y\)" FOUND L369. "whatever candidate it is" FOUND brief C §4 l.515. "Withdrawing a premise removes a license; it does not make the conclusion false" FOUND L393. "the background and instruments of the test that yields it" FOUND L315. "established of each that it is not an account" and "undone by no lapse of premises": own words.

**X14.13 · Mimo · C · point 5 (T1).** A slightly changed wrong answer is covered (negation of receipts); a mistake repeated at an untested neighbouring pair is rightly untouched. Attack reported as failing.
- "Two rivals that both fit what is established … pose … a problem" FOUND L317.

**X14.14 · Mimo · C · point 6 (T4).** No verdict moves (O1, D3-T, O27, O8, N7, N2, O24).
- "no explanation of the floods" FOUND brief C §7 l.577. "does not answer a broader question that failed" FOUND L159. "a population with no such survivor is the theorem's own qualification" FOUND L542 (Part XV, (D); the reply attributes it to Derivation 3). "for every such candidate alike" FOUND L369. "no candidate is thereby shown to be an account (K2)" FOUND L369. "an account at a coarse grain is an account of the coarse question" FOUND L277. "a changed candidate that keeps \(y\) there" FOUND L369. "One reachable setting is enough" FOUND brief C §7 l.619.

**X14.15 · Mimo · C · (a) X14: FAITHFUL.** The four-case list names roles of one failing answer under a universal quantifier; the record clause is the owner's point; the receipts are for the target's answer.
- "the candidate that gave \(y\) there and failed, …" FOUND L369. "whatever candidate it is" FOUND brief C §4 l.515. "every such candidate alike" FOUND L369. "with no record of which candidates failed before or of how any was changed" FOUND L369. "from the candidate's own answer there" FOUND L369. "A record is redundant" FOUND brief C §2 l.28. "do not propose a record or log where the explanation's own content does the work" FOUND brief C §2 l.38. "A record reconstructed from the claim it is meant to support is not a receipt for that claim" FOUND L397.

**X14.16 · Mimo · C · (b) X14: HOLDS AS STATED.** On the same question it sticks; what returns through (K3)/(K2) is unsettled status, never an account; every avenue the text lets through is one it names.
- "no candidate is thereby shown to be an account (K2)" FOUND L369. "a different question … an account on it does not answer \(p\), and the failure on \(p\) stands (Historical index)" FOUND L369. "If a premise about them ceases to be live, the receipt is not usable and the exclusion ceases to be established" FOUND L369. "A new index is a new claim" FOUND L367 (the reply cites L368).

**X14.17 · Mimo · C · (c2) X14: UNSETTLED BY THE TEXT.** Digested in §6.2.
- "the target's relations as well as its answer" FOUND L317. "the test that yields it" FOUND L369. "both fits": own words.

No point on X14 that asserts a defect of it was raised outside part C. (Atria B point 2 and Mimo C read L317's "stays refuted" against L369 and find no clash; they are listed at X10.2 and X14.12.)

### 3.9 X17 · W7.5 · Part XIV, "Dependence order", L526 · CLAIM · part K

**X17.1 · Atria · K · T3 (the directed question).** The order places none of Part VI's new notions, so Derivation 6's claim is not carried by the order as written; but X17 neither adds nor removes a placement for them, the gap predates X17 and "belongs to the items that introduced lines 315/317"; the order "stays true": nothing X17 adds is contradicted, and it is "incomplete, not untrue". (Also listed at X09.21.)
- "(S), (B), (D) depend on (E)" FOUND L526. "Every predicate in Parts II–XIII is defined from Θ …" FOUND L596. "By the dependence order of Part XIV" FOUND L598. "Ownership depends … and ProducedBy on histories and their active routes." FOUND L526. "Build depends on histories and (E). (N), (G) depend on Deploy and Build. (P), (EK) depend on (G), (E), Deploy." FOUND brief K §4 l.620 (old wording). "(P) also on ProducedBy and on the declared obligations with their occasions" FOUND L526. "In (P), accordingly, r(ξ′) says of a protected condition r that it held on every occasion it covers from ξ to ξ′, not only at ξ′" FOUND L441. "the obligations O and P of a repair, with the occasions each covers" FOUND L522. "ProducedBy on histories and their active routes" FOUND L526. "ProducedBy holds when an active route (Part IX) runs from Δ to the repair" FOUND L441. "(RC), (U1)–(U3) depend on all of the above" FOUND L526. "Nothing depends on a predicate meaning 'really explains,' 'is a cause,' or 'is knowledge'" FOUND L526 (quotation marks differ).

**X17.2 · Atria · K · T1.** Attack: "Build depends on histories, Ownership and (E)" is imprecise. Reported as failing: the "(E)" is carried over verbatim; the additions X17 makes are supported (L427, L473, L475, L438, L447, L375, L441); no cycle.
- "Build depends on histories, Ownership and (E)" FOUND L526. "an actual subhistory owned by s … prepares a represented organization … contains a nontrivial binding construction" FOUND L405. "(F1)–(F2) and physical provenance" FOUND L526. "Build depends on histories and (E)" FOUND brief K §4 l.620. "for explanatory use of c" and "the resulting representation" FOUND L405. "Can_{Ω,β}(ξ,T;χ) requires an owned retained realization or an owned, physically admitted, finite construction of one under the same continuity and resource contract" FOUND L475. "nor do the declared indices and the declared inputs, which are stated, not derived" FOUND L526.

**X17.3 · Atria · K · T2.** Attack: the declaration's "Build on Ownership" omits the retained histories and (E). Reported as failing: a declaration reports what changes; CLAIM is right.
- "Build on Ownership" FOUND brief K §4 l.615 (the declaration). "(EK) also on (P)" FOUND L526. "(P), (EK) depend on (G), (E), Deploy" FOUND L526.

**X17.4 · Atria · K · T4.** No move on O49, O35, O38 or O37.
- "owned capability on Ownership, (CT1) and a declared continuity" FOUND L526. "owned means capable" FOUND brief K §7 l.691. "'owned because it can, and can because owned' grounds neither" FOUND L475. "an ownership and a capability justified only by each other has not supplied its place in it" FOUND (punct.) L526 (the text has a comma after "each other"). "on every occasion it covers from ξ to ξ′, not only at ξ′" FOUND L441. "a separate proof that would supply it counts only when the account uses it" FOUND L526.

**X17.5 · Atria · K · (a), as a point.** Faithful: no record or log; ProducedBy on histories and active routes.
- "with no record of which candidates failed before or of how any was changed" FOUND L369.

**X17.6 · Mimo · K · point 1 (T1).** (EK) is placed on (P) but not on the obligations it quantifies over directly (\(\neg o(\xi)\land o(\xi')\) over \(O_{\mathrm{ep}}\subseteq O\)) nor on ProducesVia, which is not ProducedBy; by the item's own erratum standard "(EK) also on (P)" is false read as an exhaustive entry; with \(O=\{o_1,o_2\}\), the choice of \(O_{\mathrm{ep}}\) decides (EK) while (P) is untouched. Proposed wording, then declaration:

~~~~text
Ownership depends on histories and a declared boundary, and owned capability on Ownership, (CT1) and a declared continuity (Part XII). Build depends on histories, Ownership and (E). (N), (G) depend on Deploy and Build. (P), (EK) depend on (G), (E), Deploy; (P) also on ProducedBy and on the declared obligations with their occasions, (EK) also on (P), on the declared obligations with their occasions through \(O_{\mathrm{ep}}\), and on ProducesVia, and ProducedBy on histories and their active routes, and ProducesVia on those and on the binding of \(c\).
~~~~

~~~~text
Part XIV's dependence order now places Ownership on histories and a declared boundary, owned capability on Ownership, (CT1) and a declared continuity, Build on Ownership, (P) on ProducedBy and the declared obligations with their occasions, (EK) on (P), on the declared obligations with their occasions through \(O_{\mathrm{ep}}\), and on ProducesVia, and ProducedBy on histories and their active routes, and ProducesVia on those and on the binding of \(c\).
~~~~

"Unpressed": Result and CreativeCriticalEpisode for (EK), Attempt for (G), the restriction operation for (S), \(\mathcal V\) for (D); and \(O_{\mathrm{ep}}\) appears in no list of declared inputs.
- The block quotation of (EK) (reply lines 7–8): NOT FOUND word for word; it is a condensed rendering of L446–L450 that drops the argument lists of CreativeCriticalEpisode, Origin and Deploy. "With \(O_{\mathrm{ep}}\subseteq O\) the epistemic obligations" FOUND L443. "(P), (EK) depend on (G), (E), Deploy" FOUND L526 and brief K §4 l.620. "(EK) also on (P)" FOUND L526. "erratum" FOUND brief K §4 l.613.

**X17.7 · Mimo · K · point 2 (T3, the directed question).** The order stays true but does not place the Part VI notions; words offered (X09.22).

**X17.8 · Mimo · K · point 3 (T2).** CLAIM is right (the old entry licensed conclusions the definitions deny; not ORDER); the declaration matches clause for clause but "repeats the incomplete (EK) clause".
- "an actual subhistory owned by \(s\)" FOUND L405 (the reply cites L406). "(P) rests only on (G), (E), Deploy" and "Build does not rest on Ownership": own words (what the old entry licensed).

**X17.9 · Mimo · K · point 4 (T4).** No verdict moves (O38, O35, O37, O49).
- "a protected condition is lost exactly when it fails on an occasion it covers" FOUND L441. "it held on every occasion it covers from \(\xi\) to \(\xi'\)" FOUND L441. "runs at all times" FOUND brief K §7 l.681. "Losses outside \(P\) must be exposed" FOUND L441. "not a loss" FOUND brief K §7 l.677. "an ownership and a capability justified only by each other, has not supplied its place in it, and a separate proof …" FOUND L526. "'owned because it can, and can because owned' grounds neither" FOUND L475.

**X17.10 · Mimo · K · point 5 (T1, second attack).** Ownership rests on "the system boundary and resource contract", capability on "the same continuity and resource contract", but the entry names only "a declared boundary"; reported as failing on L473 (the boundary carries the resources); residual: "resource contract" has no place of its own in L522, "not this item's doing".
- "the system boundary and resource contract declared for \(s\)" FOUND L427 (the reply cites L428). "under the same continuity and resource contract" FOUND L475. "a declared boundary (which processes and resources are the system's)" FOUND L473.

**X17.11 · Mimo · K · point 9 ((a), as a point).** Faithful: grounding entries only; no set, count, grade or record.
- "never through a listed set, an enumeration or a count of versions, and never as a grade; do not propose a record or log where the explanation's own content does the work" FOUND brief K §2 l.38. "A record is redundant" FOUND brief K §2 l.28.

No point on X17 was raised outside part K.

### 3.10 X18 · W38.1 · the note of sources and departures · META · part E

The note is not in the draft-4 line numbering; its lines are in brief E §4 (l.488–509). No reply quotes either book; the quotations below are of the note.

**X18.1 · Atria · E · point 1 (T3).** The *Reach* bullet ends "(Parts I and VI)" where the revised text's own sentence at L317 ends "(Parts I and V)", so the note is incoherent with the text it describes. Proposed wording in its place:

~~~~text
Here the word is not defined, and nothing is measured by how many questions a candidate answers; whether a candidate is an account of a question is fixed by the candidate, the question and the world, not by when anyone first asks the question or by whether anyone has checked the candidate against it (Parts I and V).
~~~~

- "whether a candidate is an account of a question is fixed by the candidate, the question and the world, not by when anyone first asks the question or by whether anyone has checked the candidate against it (Parts I and VI)" FOUND brief E §4 l.499. "(Parts I and V)" FOUND L317.

**X18.2 · Atria · E · point 2 (T2).** The *Hard to vary* bullet asserts an application the revised text never makes (that on the Greeks' question the axis-tilt theory "is easy to vary relative to the myth"), against the note's own declaration that it says nothing about what follows. Proposed wording in its place (the change is "is easy to vary" to "would be easy to vary"):

~~~~text
Here being easy to vary is relative to the question and symmetric between two rivals, and prefers neither: on the question of the seasons the Greeks knew, the axis-tilt theory, which he calls hard to vary (p.24), would be easy to vary relative to the myth when the two are offered in place of each other, and relative to a variant that keeps its predictions where the Greeks looked and changes them elsewhere, which for him is no longer an explanation but a rule of thumb (pp.27–28).
~~~~

- "says nothing about what follows from them" FOUND brief E §4 l.491. "on the question of the seasons the Greeks knew, the axis-tilt theory, which he calls hard to vary (p.24), is easy to vary relative to the myth when the two are offered in place of each other" FOUND brief E §4 l.498 (the note's words).

**X18.3 · Atria · E · (a) X18: FAITHFUL.** No listed set, enumeration, count, grade or record; where the note mentions a grading it gives it to Deutsch.
- "Here hard-to-vary is stated through rivals and problems, with no measure or count of variants (Part VI)" FOUND brief E §4 l.498. "nothing in the semantics grades a candidate for carrying one" FOUND brief E §4 l.497. "which for him is no longer an explanation but a rule of thumb" FOUND brief E §4 l.498.

**X18.4 · Atria · E · (c1) X18: HARMLESS.** Digested in §6.1.
- "A candidate is easy to vary, in the sense used here, when it and a rival pose a problem of the second kind; the rival is then easy to vary too, and the term says nothing about which of them is right." FOUND L317.

**X18.5 · Mimo · E · point 1 (T3).** The note's definition of a recognized difficulty drops two qualifiers of L429, "what the system holds" and "only by", and so counts as a difficulty a case where the system holds another route that meets the obligation without failing the protected one (example: a rushed route and a legal route). Proposed replacement for the whole sentence:

~~~~text
A problem in his wider sense can be a recognized difficulty (Part X): a failure of a claimed obligation, or a conflict in which what the system holds meets a claimed obligation only by failing a protected one (Part XI), when the system represents it.
~~~~

- "a conflict in which meeting a claimed obligation fails a protected one (Part XI), when the system represents it" FOUND brief E §4 l.502 (the note). "a conflict in which **what the system holds** meets a claimed obligation **only by** failing a protected one (Part XI), when the system represents it" FOUND L429.

**X18.6 · Mimo · E · point 2 (T2).** The same line states a claim the revised text does not make (the note's version is strictly broader), against the note's declaration that it adds nothing. No further wording (see X18.5).
- The two definitions: FOUND brief E §4 l.502 and L429.

**X18.7 · Mimo · E · point 3 (T3).** The account-status sentence points to "(Parts I and VI)" where L317 has "(Parts I and V)"; Part V defines Account. Proposed replacement for the parenthetical: `(Parts I and V)`
- The note's sentence FOUND brief E §4 l.499. "(Parts I and V)" FOUND L317.

**X18.8 · Mimo · E · point 4 (T1).** The other "Here" sentences and the book descriptions are otherwise accurate (the Elimination bullet omits "its own target" but the substance is right; the count "Four departures" is correct; page numbers not verifiable by the reply).
- "nothing in the semantics grades a candidate" FOUND brief E §4 l.497. "no merit function" FOUND L522. "No member of the history represents *t*, *H*, or the survival condition" FOUND L195. "its own target" FOUND L339. "Four departures" FOUND brief E §4 l.498. "conflict at no pair… neither pair is a pair of rivals" FOUND L315.

**X18.9 · Mimo · E · point 5 (T4).** The note moves no verdict (N2, N3, N4, N1, N22, N5).
- "whether a candidate is an account… not by when anyone first asks" FOUND L317 and brief E §4 l.499.

**X18.10 · Mimo · E · (a) X18: FAITHFUL.** Easy to vary is described through a discovered, offered rival; "prefers neither"; the four departures agree with the owner's position.
- "through rivals and problems, with no measure or count of variants (Part VI)" FOUND brief E §4 l.498. "a rival that fits as well and conflicts with it only outside what the question covers" FOUND brief E §4 l.498. "prefers neither" FOUND brief E §4 l.498. "the term says nothing about which of them is right" FOUND L317. "Nothing here counts rivals, grades a candidate or ranks candidates." FOUND L317. "shown only by offering the rival, which is the criticism" FOUND brief E §4 l.498.

**X18.11 · Mimo · E · (c1) X18: HARMLESS.** Digested in §6.1.
- "in the sense used here" and "the rival is then easy to vary too, and the term says nothing about which of them is right" FOUND L317. "A finer contract… makes a new question" FOUND L317.

Both replies propose the same change of the *Reach* pointer, "(Parts I and VI)" to "(Parts I and V)" (X18.1, X18.7); their other challenges differ (X18.2 on the *Hard to vary* bullet; X18.5–X18.6 on the recognized-difficulty sentence). No point on X18 was raised outside part E.

---
## 4. Items that go to no checker

Neither reply challenges these items under rule 3, and where verdict words were asked the two replies' words agree. Each is recorded, as rule 5 requires, as **upheld by both readers; not thereby confirmed** (rule 2: silence is not support, and an UPHELD is not a confirmation).

| item | entry | part | verdict words (Atria / Mimo) | record |
|---|---|---|---|---|
| X01 | W37.1 | F | none asked | upheld by both readers; not thereby confirmed |
| X02 | W36.1 | D | (a) FAITHFUL / FAITHFUL | upheld by both readers; not thereby confirmed |
| X07 | W34.1 | D | (a) FAITHFUL / FAITHFUL | upheld by both readers; not thereby confirmed |
| X08 | W33.1 | D | (a) FAITHFUL / FAITHFUL; (d) RIGHT / RIGHT | upheld by both readers; not thereby confirmed |
| X12 | W40.1 | I | (a) asked as a point only: "not engaged and is not violated" / "consistent" | upheld by both readers; not thereby confirmed |
| X13 | W24.1 | J | none asked | upheld by both readers; not thereby confirmed |
| X15 | W22.1 | J | (a) FAITHFUL / FAITHFUL | upheld by both readers; not thereby confirmed |
| X16 | W6.3 | K | (a) asked as a point only: "Not applicable" / "Faithful" | upheld by both readers; not thereby confirmed |

**Flagged for the orchestrator, not counted as challenges.**

- *X07, and \(\mathcal V\).* Both part-D replies note that \(\mathcal V\) survives in (D) (L299, L302) and is not among Part XIV's declared inputs (L522), the gap the owner's correction named; both decline to press it against X07, since (D) is not X07's wording and states nothing about hard to vary (Atria D point 1, Mimo D point 4). Mimo K point 1 lists "\(\mathcal V\) for (D)" among the matters it leaves "Unpressed". Mimo D point 4 asks for a check it could not make on its excerpts: that no line of the full text cites \(\operatorname{Pres}\), "jobs" or a "reach" of \(E\). A search of the whole draft-4 text finds "Pres" 0 times and "job" 0 times, and "reach" only inside "reachability" (L151, L335) and as a verb (L245, L562, L630). This is a search result, not a ruling.
- *X16, and L524.* Mimo K point 7 says that L524's definition of a declared input ("something a claim takes as stated, which the semantics records and does not supply") still admits \(\mathcal N\), and gives words to close it: `and which is not one of the two primitives`. It calls this "Residual, outside this item" and says "I do not press it against X16". L524 is not an item. Not counted as a challenge to X16; the orchestrator may route it.
- *X16, (a).* Atria answers "Not applicable" and Mimo "Faithful". Part K asked (a) only as a point, with no verdict line, and neither reply finds the item unfaithful, so the pair is not counted as different verdict words under rule 5.
- *X17's residuals* (\(O_{\mathrm{ep}}\) and "resource contract" in no list of declared inputs) are in X17's digest (X17.6, X17.10), since X17 goes to a checker.

**Quotations in the replies on these items that were not found (rule 9), for the record.**

- X01 · Atria F point 6: "a variation operator on \(\mathcal T\)": NOT FOUND (L195 reads "a variation operator \(\mu\) on \(\mathcal T\)").
- X02, X07, X08 · Atria D points 1 and 10: "Pres(F′)⊆Pres(F)": FOUND brief D §4 l.509 and l.516, written there in LaTeX.
- X02, X08 · Mimo D point 1: "not a part of what explains them": NOT FOUND (N1's verdict, brief D §7 l.618, reads "not part of what explains them"). Mimo D points 1 and 2 cite L120 for the sentence of (K) that stands at L119. Mimo D (d) gives "an unsupported belief riding along" as what "Part IV says"; the words are N1's verdict (brief D §7 l.618).
- X12 · Atria I point 1: "there are no inner experiences, people are mistaken": FOUND (punct.) brief I §7 l.593.
- X13, X15 · Atria J point 1: "physically located carriers": NOT FOUND (L169 reads "a physically located carrier"). Atria J (a): "the explanatory candidate that the criticism offers": NOT FOUND (the earlier reading's wording, brief J §4 l.560, reads "the explanatory candidate (Part V) that the criticism offers"); "with no record of which candidates failed before or how any was changed": NOT FOUND (L369 reads "or of how").
- Every other quotation in the replies on these items was found.

---

## 5. Points that dispute a fixed verdict (rule 10)

None. No reply says that a fixed verdict of a described situation is wrong. For the record, the nearest passages, none of which disputes a fixed verdict:

- Mimo B, (c1) X10: "One correction to the paraphrase: the tilt does not wait for the question to be widened to lose the label". This corrects the brief's statement of question (c1), not a case verdict.
- Mimo D point 2: reads N25's "As explanations they make the same empty claim" as ordinary usage, the theory's own verdict being that neither story meets (E); stated as agreeing with the case.
- Mimo H, (d) X06; Atria A and Mimo A, (a) X09: weigh L315's "offered … in place of the other" against the owner's words. The owner's words are not a fixed verdict.
- Atria F point 4: says O9's two candidates "remain rivals", with no disagreement stated with O9's verdict.

---

## 6. Findings that are choices for the owner (rule 6)

Rule 6: a finding that asks for a change of the theory text goes to the item's checker as a challenge; a finding that is a choice for the owner is recorded with both replies' reasons, and the checker says only whether the present wording states the matter truly. Which findings below are choices and which are defects is not decided here.

### 6.1 (c1): whether "easy to vary" should point at one side (the tilt and the myth on the Greeks' question)

| asked of | part | Atria | Mimo |
|---|---|---|---|
| X10 | B | HARMLESS | HARMLESS |
| X18 | E | HARMLESS | HARMLESS |

- **Atria B (X10).** The text says it: the two conflict only outside \(C\), so the problem is of the second kind and each is easy to vary relative to the other until a finer question containing a southern pair turns it into a first-kind problem; once the southern seasons are established the myth no longer fits and the tilt ceases to be easy to vary. Harmless because the term is question- and assessor-relative and says nothing about correctness (the tilt stays an account throughout), the myth's being easy to vary is N3's verdict, and the tilt's hardness appears relative to the widened question. To call the tilt hard to vary on the Greek question "would require counting how many of its own variations still fit, which is the enumeration and the grade the owner's rule forbids; there is no wording that says differently without bringing one back."
- **Mimo B (X10).** The text says it, with one correction: the label ends when the problem ends, either by a finer contract or when the rival stops fitting (for the myth, "its non-circular failure does that as soon as a receipt for it exists", which ties (c1) to (c2)). Harmless: the label is a statement about the dispute, not about the tilt's own variability; the asymmetry the fixed verdicts need is carried by (E) (the myth fails non-circular dependence, N3; the tilt does not, N1) and by the first-kind problem a wider question makes (N2, N4); "The Deutschian asymmetry appears on the other side" (the myth has a fitting self-variation, N2; a variant tilt would conflict inside \(C\)). Words marking the tilt hard and the myth easy on the restricted question "would be exactly the grade the owner's rule forbids", and words tracking swappable details would need the set of versions.
- **Atria E (X18).** L317 defines easy to vary symmetrically; the consequence is a declared departure from Deutsch's grading use and coheres with the theory's abstention from merit functions (L25); "The theory should not say differently."
- **Mimo E (X18).** The narrow contract does not contain their difference and a wider question is needed; "in the sense used here", the symmetry clause and "Nothing here counts rivals, grades a candidate or ranks candidates" keep it from being a grade; a harmless consequence of question-relativity.

All four say HARMLESS; none proposes words. Atria E's point 2 (X18.2) is a separate matter: whether the *note* may state this application of L317, not whether L317 should state it.

### 6.2 (c2): whether a failure found by examining a candidate counts as established

| asked of | part | Atria | Mimo |
|---|---|---|---|
| X09 | A | UNSETTLED BY THE TEXT | UNSETTLED BY THE TEXT |
| X10 | B | UNSETTLED BY THE TEXT | **ESTABLISHED** |
| X14 | C | UNSETTLED BY THE TEXT | UNSETTLED BY THE TEXT |

Five of the six answers say the text does not settle it and that it should be settled so that such a failure counts; Mimo B says the text already settles it that way. The reasons:

- **Atria A (X09).** "Result" is unrestricted and (K2) could be met by a verification over definitions, but (K3)'s "the test that yields it" and the evidence leaf, "a reference to an event", point at empirical tests; "capacious is not settled". Settle by making a verification a receipt, usable while its premises (the definitions and the adopted physics) are live (K2), and telling against the candidate only together with them (K3) (X09.1).
- **Mimo A (X09).** A leaf could carry an inspection of the written candidate, but "established" is introduced beside tests and L369 ties it to the target's answer. Settle so that an inspection failure is a result "once the assessor holds a usable receipt for the inspection, and needs no test of the target" (X09.14).
- **Atria B (X10).** Nothing says whether an examination is such an event, and nothing says it is not (an examination is an occurrence in a history, L375). Settle in X09 or Part IX: a failure decidable from the candidate, the question and the contract alone is established for one who has examined the candidate, and "(K3) does not qualify it, because the failure is in the candidate itself and rests on no background or instrument" (X09.17).
- **Mimo B (X10), ESTABLISHED.** The fit clause says "a condition of (E)", which includes conditions no test can show; receipts are proposition-general; Part VIII already derives an exclusion "from the candidate's own answer there"; otherwise "until what is established leaves at most one of them fitting" would be idle for second-kind problems. Optional words to remove the room at L315 (X09.18).
- **Atria C (X14).** The text pulls both ways (Part V's conditions are on supplied relations; receipts are trees over events). Settle "in favour of the inspection reading for candidate-side facts, with receipts reserved for target-side and world-side claims"; this also backs X14's "no record" claim, which needs a candidate's own answer to be available "without a receipt" (X09.19).
- **Mimo C (X14).** Neither stated nor excluded. Settle for establishment "by a receipt whose leaf is the candidate's own content", with (K3) reading the definitions, the declared indices and the reading convention as background; words for Part IX (X09.20).

What each says turns on it: whether a candidate with an internal failure still "fits" and so can pose or share a problem, and in particular whether such a candidate can make a sound account "easy to vary" (Mimo C: "the theory would condemn a good account on the strength of a twin that is not an account at all"; Atria B: whether easy to vary "tracks genuine underdetermination or also tracks unexamined junk").

The settling proposals differ, and the differences are recorded, not ruled: whether the examination is itself a receipt (Atria A, Mimo A, Mimo C) or candidate-side facts need no receipt (Atria C); whether (K3) qualifies such a result (yes: Atria A, with the definitions and adopted physics as background, and Mimo C, with the definitions, declared indices and reading convention; no: Atria B); and where the words go (after the "fits" sentence of L315: Atria A, Mimo A, Mimo B; X09 or Part IX: Atria B; Part IX: Mimo C). X10's (c2) verdict words differ between the two replies and go to X10's checker under rule 5; the proposals of wording go to X09's checker (§3.5).

### 6.3 (d): losses the replies weigh against the owner's words

Question (d) asks whether the rivals condition of L315 is right, and "is anything lost that the theory should keep?". Three of Mimo's answers name a loss; whether each is a defect of the wording (a challenge, to the checker) or a choice for the owner is not decided here. All are listed under X09 (§3.5) and, where they bear on easy to vary, under X10 (§3.6).

| asked of | part | Atria | Mimo | Mimo's loss, in brief |
|---|---|---|---|---|
| X09 | A | RIGHT | RIGHT, WITH A LOSS | a conflict at a pair only one transport translates is not counted |
| X08 | D | RIGHT | RIGHT | – |
| X03 | F | RIGHT | RIGHT, WITH A LOSS | "easy to vary" cannot be said of N25's swappable picks |
| X06 | H | RIGHT | RIGHT, WITH A LOSS | variations differing only where no admitted change reaches pose no problem, and rivalry needs an offer "in place of" another, "though the owner counts both as competitors" |

Related remarks on "offered … in place of the other" (L315), none pressed as a defect: Atria A (a) calls it "slightly tighter than the owner's"; Mimo A (a) says it is narrow if it means replacement of that particular other, so that "two sibling variations of one original could then escape rivalry"; Atria F (d) says a narrow reading would lose something but L315's gloss fixes the broad reading; Mimo H (d) counts it as part of the loss.

---

## 7. The items that go to a checker, and what each checker receives

Each checker also receives, by rule 4, the item's entry from the change list (`Semantics/tests/Revision 2 - change list, draft of 23 September.md`) and the draft-4 theory text (`Semantics/tests/Revision 2 - file 13 draft 4, theory text.md`), and this file's digest of the item (§3). Reply files are in `Semantics/results/S93 Cross-examination - draft 4 - returns/`; briefs are in `Semantics/tests/`. Rulings go to `Semantics/results/S93 reading rulings/ruling S93 <item id> <entry>.md` (rule 7).

1. **X03 · W19.1** (Atria upholds; Mimo challenges the cross-candidate definition and its report of Derivation 1; (d) RIGHT against RIGHT, WITH A LOSS). Replies: `s93_xexam_atria_F.response.txt`, `s93_xexam_mimo_F.response.txt`. Brief: `S93 Cross-examination - draft 4 - part F, selection in Part 0, and kinds across two candidates.md`. Ruling file: `ruling S93 X03 W19.1.md`.
2. **X04 · W35.1** (both closing lines UPHELD; Mimo's point 2 says X04 leaves Derivation 4's proof sentence, L582, stale, against Atria's point 7). Replies: `s93_xexam_atria_G.response.txt`, `s93_xexam_mimo_G.response.txt`. Brief: `S93 Cross-examination - draft 4 - part G, expectation, violation and surprise.md`. Ruling file: `ruling S93 X04 W35.1.md`.
3. **X05 · W35.2** (Atria upholds; Mimo challenges the dropped "actually occurring" scoping, in the wording and the declaration). Replies and brief: as X04. Ruling file: `ruling S93 X05 W35.2.md`.
4. **X06 · W20.1** (Atria upholds, with an optional phrase; Mimo challenges the input-assigner clause, "boundary values", the pointer to Part VI, and the declaration, and proposes repairs of L245, L299 and L558; (d) RIGHT against RIGHT, WITH A LOSS). Replies: `s93_xexam_atria_H.response.txt`, `s93_xexam_mimo_H.response.txt`. Brief: `S93 Cross-examination - draft 4 - part H, the commitments of a candidate.md`. Ruling file: `ruling S93 X06 W20.1.md`.
5. **X09 · W59.1, "Rivals"** (both challenge, for different reasons and with different wordings: Atria on "established" and internal failures; Mimo on the exclusion sentence's parse, the "as when" illustration and the declaration; (d) RIGHT against RIGHT, WITH A LOSS; many points from outside part A). Replies: `s93_xexam_atria_A.response.txt`, `s93_xexam_mimo_A.response.txt`; and, for the points raised outside part A (rule 11): `s93_xexam_atria_B.response.txt`, `s93_xexam_mimo_B.response.txt`, `s93_xexam_atria_C.response.txt`, `s93_xexam_mimo_C.response.txt`, `s93_xexam_atria_K.response.txt`, `s93_xexam_mimo_K.response.txt`, and the (d) paragraphs of `s93_xexam_atria_D.response.txt`, `s93_xexam_mimo_D.response.txt`, `s93_xexam_atria_F.response.txt`, `s93_xexam_mimo_F.response.txt`, `s93_xexam_atria_H.response.txt`, `s93_xexam_mimo_H.response.txt`. Brief: `S93 Cross-examination - draft 4 - part A, rivals.md`; for the outside points, the briefs of parts B, C, D, F, H and K. Ruling file: `ruling S93 X09 W59.1.md`.
6. **X10 · W59.1, "Problems"** (both closing lines UPHELD; (c2) UNSETTLED BY THE TEXT against ESTABLISHED; Mimo's optional phrase "For that assessor"; from outside part B, the dependence order's silence on "problem" and "easy to vary", the (c2) consequences for easy to vary, and Mimo F's (d) loss). Replies: `s93_xexam_atria_B.response.txt`, `s93_xexam_mimo_B.response.txt`; and, for the points raised outside part B: `s93_xexam_atria_A.response.txt`, `s93_xexam_mimo_A.response.txt`, `s93_xexam_atria_C.response.txt`, `s93_xexam_mimo_C.response.txt`, `s93_xexam_mimo_F.response.txt`, `s93_xexam_atria_K.response.txt`, `s93_xexam_mimo_K.response.txt`; related, the (c1) paragraphs of `s93_xexam_atria_E.response.txt` and `s93_xexam_mimo_E.response.txt`. Brief: `S93 Cross-examination - draft 4 - part B, problems.md`; for the outside points, the briefs of parts A, C, F and K (and E for (c1)). Ruling file: `ruling S93 X10 W59.1.md`.
7. **X11 · proposed** (both hold the change of symbol right; Mimo challenges the kind, WORDING, as CLAIM). Replies: `s93_xexam_atria_I.response.txt`, `s93_xexam_mimo_I.response.txt`. Brief: `S93 Cross-examination - draft 4 - part I, Part VII, the pole sentence and the absent structure.md`. Ruling file: `ruling S93 X11 proposed.md`.
8. **X14 · W60.1** (both closing lines UPHELD and all verdict words agree; challenged only under rule 3's third limb, by Mimo's optional wordings for the closing sentence and for "the exclusion"). Replies: `s93_xexam_atria_C.response.txt`, `s93_xexam_mimo_C.response.txt`. Brief: `S93 Cross-examination - draft 4 - part C, a failed answer stays failed.md`. Ruling file: `ruling S93 X14 W60.1.md`.
9. **X17 · W7.5** (Atria upholds; Mimo challenges the (EK) entry as omitting the declared obligations with their occasions and ProducesVia; both say the order does not place Part VI's new notions). Replies: `s93_xexam_atria_K.response.txt`, `s93_xexam_mimo_K.response.txt`. Brief: `S93 Cross-examination - draft 4 - part K, the normative relation, and the dependence order.md`. Ruling file: `ruling S93 X17 W7.5.md`.
10. **X18 · W38.1** (both challenge: both on the *Reach* pointer "(Parts I and VI)", Atria also on the *Hard to vary* bullet's application, Mimo also on the recognized-difficulty sentence). Replies: `s93_xexam_atria_E.response.txt`, `s93_xexam_mimo_E.response.txt`. Brief: `S93 Cross-examination - draft 4 - part E, the note of sources and departures.md`. Ruling file: `ruling S93 X18 W38.1.md`.

*End of the tabulation. Nothing here is a ruling.*
