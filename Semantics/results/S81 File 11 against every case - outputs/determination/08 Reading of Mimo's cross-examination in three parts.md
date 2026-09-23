# 08 Reading of Mimo's cross-examination in three parts

*Written by a Claude subagent for the orchestrator on 23 September 2026. The reading follows 05 as extended by 05b. Mimo is "auditor 2" in the briefs.*

*What the reader opened and did not open.*
- **Opened:** the three receipts and the two error files; part P2's reply; the P2 brief; 04; 04b (the O2 group, for O38 only); file 10; file 11; the case book.
- **Opened in part:** 07, at its headings and its section 5 ("Changes of ruling") only. This was to learn whether any ruling had changed before this reading. None had.
- **Not opened:** Atria's reply, 06, and every part of 07 that names Atria or 06.
- **Not read:** any reasoning file of any part. The attempt files of the failed parts P1 and P3 were not read for arguments, including P1's partial text from attempt 6.

---

## 1. The three parts: the receipts

All three parts went on 23 September 2026, as `tools/s87_run.py` with `tools/s87_jobs - Mimo in three parts.json` (sha256 079ebcd6f483…). Each part had one pass and at most 6 attempts. It was accepted only on finish "stop" with END OF REPORT on its last line.

| part | rows | attempts | what the attempts gave | result |
|---|---|---|---|---|
| P1 | O5, O30, O17 | 6 (8,634.6 s in all) | 1–4: status 0, nothing came back. 5: status 200, finish None, 0 characters, rejected. 6: status 200, finish "length" after 4,457.9 s, 6,910 characters, rejected. The reply ran into the 131,072-token limit before END OF REPORT. | **FAILED.** Error file: "status 200 after 6 attempts (2 came back but were not accepted) / finish length". |
| P2 | O35, O40 | 4 (4,884.3 s over the attempts; the receipt gives 5,004.4 s in all) | 1: status 200, finish None, 0 characters, rejected. 2 and 3: status 0. 4: status 200, finish "stop" after 2,756.1 s, 10,062 characters, **accepted**. | **ACCEPTED.** The last line is "END OF REPORT". The reply's sha256 is 334d9215cd4e…, which matches the receipt. It is 1,677 words by `wc -w`. Usage: 26,355 prompt tokens and 108,949 completion tokens, of which 106,392 were reasoning. |
| P3 | O48, O45, the standing clause | 6 (9,636.3 s in all) | 1, 2, 4, 5 and 6: status 0, nothing came back. 3: status 200, finish None, 0 characters, rejected. | **FAILED.** Error file: "status 0 after 6 attempts (1 came back but were not accepted) / ChunkedEncodingError(ProtocolError('Response ended prematurely'))". |

The files of all three parts are committed as e373275: receipts, error files, attempt files and P2's reply. The requests had been committed in 8bfefc1.

---

## 2. The failed parts support nothing (rule 5 of 05; 05b item 1)

- **Part P1 failed.** Its rows O5, O30 and O17 are **not examined by Mimo** in these parts. These are the three rows on which test (b) turned apart from O35 (04 section 5).
- **Part P3 failed.** Its rows O48 and O45 are **not examined by Mimo** in these parts. So is the standing clause, with the scoring choice for prediction P2. Mimo gives no STANDING VERDICT line.
- **Neither failed part counts** for or against the determination, and no ruling cites either.
- **Their attempt files are kept and not read for arguments.** P1's attempt 6 wrote 6,910 characters before it hit the limit. That text is not a reply, and this reading does not use it.
- **A retry of P1's rows is being prepared, one row per call.** It is not part of this reading. See the note to follow, which will set out how the retry is sent and read.

---

## 3. Part P2's reply, row by row

The reply is evidence, not a result (rule 1). It is read on its own (05b item 7).

### O35, "Four seconds"

**The determination's ruling** (04, table and section 5 (b); 04b, O4 group):
- file 10 SILENT, the baseline;
- file 11 SILENT;
- verdict SAME, on the same point ("whether the protected condition held, and whether the stop is a loss");
- passage CHANGED (additive): f11 L433 s1 and L514;
- no change.

**Mimo's closing line:** `O35: RULING STANDS`

**Mimo's argument, in order:**
1. **The rule sets the mark.** The counted file-10 mark is SILENT by the plan's rule "however the text reads", because both 1K returns are SILENT, which is the baseline. Mimo takes the text question anyway, because 04 section 7.9 records that 01's reading was AGREE.
2. **The endpoint reading (file 10 AGREE) fails** for three reasons:
   - (a) (P) is parametric: "The formula fixes *when* \(r\) is evaluated, not *what* \(r\) says" (f10 L438 = f11 L427, "fixed for the comparison").
   - (b) File 10 admits history-valued conditions: "Values of ports may be paths, functions, fields, proofs, or histories" (f10 L122). On such a condition, (P) finds a loss using the endpoints alone, as the O38 ruling reads it.
   - (c) "In every way that mattered" invokes a standard that f10 L25 marks as empty.

   Mark rule 4 fits: "the deciding matter (the content and the occasions of \(P\)) is an input the case leaves unstated".
3. **SPLIT does not fit.** "The two candidate contents are two fillings of one unfilled input, not two readings of the theory's sentences". A SPLIT would in any case rank with SILENT.
4. **File 11's SILENT is on the same point.** This rests on f11 L433 s1 and L514. Both contrary file-11 readings "choose the input from the verdict wanted", and one of them is "auditor 2's blind DISAGREE". Under f11 L433 s1, "held" and "not lost" are one fact.
5. **The comparison elements hold.** Mimo tested whether the passage could be SAME, resting on the shared f10 L438 = f11 L427. It rejected that: the file-11 SILENT is rule-governed only through the CLAIM places M38 and M48.

**Checked by the reader.** Every quotation Mimo relies on is word for word in the files:
- f10 L25, L122 and L438;
- f11 L107, L427, L433 s1 and L514.

O38 is one of the cases the part cites without giving. Its fixed verdict's "it was broken, for four seconds" is word for word in the case book, and its situation opens with the job sheet stating the protected condition, as the brief's quotation of 04b ("when the job sheet states such a condition") says. The O38 ruling Mimo cites is file 10 AGREE (baseline), file 11 AGREE, SAME (04 table; 04b, O2 group).

**What bears on the verdict.**
- The reply takes up the question 04 section 7.11 put to the cross-examination: is file 10 SILENT on the text as well as by the rule? It answers yes, on grounds 04 and 04c give, and adds grounds 2(b) and 3.
- Test (b) turned on O35. The reply supports the determination there and changes nothing.
- **A finding about the reader, not the theory.** The blind DISAGREE on O35 that the brief credits to auditor 2 is Mimo's own 2a reading, and this reply rejects it.

### O40, "Two hands on the test"

**The determination's ruling** (04 section 2.2 and table):
- file 10 AGREE, correcting S75's SILENT;
- file 11 AGREE;
- verdict SAME;
- passage CHANGED (additive): f11 L419 s2 and L433 s4 carry "theirs together", and the "mostly" point rests on the shared disclaimer;
- no change.

**Mimo's closing line:** `O40: RULING STANDS`

**Mimo's argument, in order:**
1. **The point is about claim availability.** "The verb "say" and the quotation marks around "mostly" mark the claim a party would make", not a finding of shares. The contrast is O21, O27 and O50, which "state shares in plain form".
2. **File 10 reaches the finding.**
   - f10 L414 establishes the two contributions ("relay is not").
   - f10 L25's empty place establishes that no weighing is in play.
   - So "on the record neither party has a ground for 'mostly'", and "absent a ranking" is a qualification under "Same finding".
3. **The SILENT contrary fails.** For a finding about what can be claimed, "the deciding matter is what the record warrants". "'If anyone had them' (f10 L25) describes other applications … it does not posit an unstated ranking in this one." Mimo contrasts O35, where the case posits a condition and leaves its content unstated.
4. **The consistency test.** Mimo sets O40 beside the SILENT rulings on O21, O27 and O50, and beside f11 L27 s3 and L433 s4.
   - Read as a share-finding, O40 needs one of two packages, and each costs more than it buys.
   - (a) If both files are SILENT, f11 L433 s4's "both are credited … no division of credit that it does not contain" reaches nothing, although it plainly reaches the case.
   - (b) The third reading, SILENT→AGREE, needs "an asymmetric reading of one point across the two files".
5. **The robot-credit contrary fails** on f11 L419 s2 ("remains an outside contribution however it is executed inside") and f10 L414 ("relay is not").
6. **No reading moves O40 away:** "None makes the file-11 mark further from AGREE than the file-10 mark". Mimo ends with a residual request for file-10 text that the part did not excerpt (below).

**Checked by the reader.**
- **Quotations.** Every quotation from the files is word for word: f10 L25 and L414; f11 L27 s3, L419 s2 and L433 s4.
- **Cases the part cites without giving.** "mostly the expert's" is in O21, and in O50 ("The inquiry was mostly the expert's"). "mostly the robot's" is in O27. Each is word for word in the case book.
- **One difference in route, which changes no element.**
  - 04's reason 4 has both files reach the "mostly" point "by the same route": f10 L25, and f11 L27 with s3 "of the same form".
  - Mimo has each file reach it "by its own route": file 10 through L25's empty place, and file 11 through L27 s3 and L433 s4.
  - On either route, both marks are AGREE, the verdict is SAME, the passage is CHANGED (additive) because file 11's route runs through new sentences, and the direction and kind are unchanged.
  - The difference is recorded. It is not a change of ruling.

**The residual request, answered from file 10.**
- **What Mimo asks for:** file 10's definition of \(\operatorname{ProducedBy}\) and any crediting rule beside it (its Part IX histories text, and Part XI between L444 and L447), and anything on the normative relation beyond f10 L519. Mimo says these would settle "whether file 10 carries *some* credit-division provision that f11 L27 s3 and L433 s4 replace".
- **The search.** The reader searched file 10 (md5 3a8cd7c8ca6f3ad3b8a85ab9984d850e) for "ProducedBy", "credit", "division", "contribut", "share" and "mostly". It also read the passages Mimo names:
  - Part IX, "Histories" (f10 L384);
  - f10 L444–L447, which are the end of Repair and the opening of "Created explanatory knowledge";
  - the places \(\mathcal N\) appears (L53, L458, L519, L593).
- **What it found.**
  - "ProducedBy" occurs only inside (P), at f10 L441, and is not defined.
  - "credit" does not occur.
  - "division" occurs only in the tokens example at L348.
  - "contribut" occurs only in Part VI's support results ("Redundant routes … each is contributory, neither indispensable", L324; "(B) records the collective contribution", L328) and at L76 ("the originative contribution of an episode").
  - "share" occurs only at L44 ("It shares commitments with each"), and "mostly" does not occur.
  - None of these divides credit among contributors.
- **What follows.** File 10 carries no credit-division provision for f11 L27 s3 and L433 s4 to replace. Those sentences add to file 10 and replace nothing in it, which is the determination's "CHANGED (additive)". The door Mimo leaves ajar is closed. This supports the ruling and changes nothing.

**What bears on the verdict.** Nothing. O40 decides only whether the row is an S75 correction or a theory change toward the thoughtful person (04 section 2.2). The reply supports the correction.

---

## 4. The fresh determiner (rule 2 of 05; 05b item 3): not called

- **No row goes to a fresh determiner from this part.** The reply says RULING STANDS on both rows, and it names no new away-row. On O40 it says that no reading moves the row away.
- **No ruling is re-read under rule 2.** The checks in section 3 are the reader's checks, of quotations, of the cases the part cites without giving, and of Mimo's residual request. They are not a re-ruling.

---

## 5. Changes of ruling

- **None.** No mark, verdict, passage, direction or kind changes on O35 or O40.
- **04's counts stand, as 07 left them.**
  - File 10: AGREE 44, SILENT 6, SPLIT 1, DISAGREE 1.
  - File 11: AGREE 46, SILENT 6.
  - Verdicts: 2 CHANGED (O45 and O48, both toward the thoughtful person).
  - S75 corrections: 3 (O20, O40, O45).
- **Test (b).** The only row of this part on which test (b) turned was O35. It holds there, unchanged.

---

## 6. What Mimo has not examined in these parts

- **Rows:** O5, O30 and O17 (part P1 failed), and O48 and O45 (part P3 failed).
- **The standing clause and the P2 scoring choice** (part P3 failed).
- **The brief's task 2**, the hunt for other rows that move away. No part asked it, and P2 raised no such row.
- **The brief's task 4**, anything else. No part asked it, and P2 raised no such point.
- **O21 and O27.** P2 cites them as contrasts, and raises neither as a row.

---

## 7. The standing verdict after this reading

**This reading changes no ruling.** The standing verdict is therefore the one 04 section 6 gives, which 07 left unchanged:

> **File 11 stands as the authority under the plan's second clause, with P3's 41 undeclared CLAIM places inside the theory (none shown harmful by any case), P2's failure at O45 (a theory change toward the thoughtful person), the three S75 corrections and the seven errata recorded against its frozen note in S81 Results.**

**The limits of this support.**
- **It is evidence, not a result** (rule 1).
- **It covers O35 and O40 only.** Of the rows that decided the verdict, Mimo has examined only O35, for test (b). It has not examined:
  - O5, O30 and O17 (test (b));
  - O48 (test (a) and prediction P1);
  - O45 (prediction P2);
  - the standing clause.
- **The retry of P1's rows** will be read under its own note when it returns.
- **The comparison with Atria's reading.** This reading is set beside 06 only after all the readings are written, as 05b item 7 requires. That includes the reading of the P1 retry. Any row where the two readings differ is then resolved in writing from the texts.

---

## 8. Confounds, as they fell out

- **What part P2 carried.** It carried file 11 in full, O35 and O40, and only the file-10 lines those two rows need.
  - Mimo argued from four cases the part cites without giving: O21, O27, O38 and O50. It used only the quotations the brief carries, and each matches the case book.
- **Selection by the ceiling.** The accepted run used 106,392 reasoning tokens against the 131,072 limit.
  - Attempt 1 came back empty (finish None) and was rejected.
  - Attempts 2 and 3 failed in transport.
  - Of the two answers that came back, the accepted reply is the one that finished.
- **The failures differ in kind.**
  - P1 made two answers that came back: one empty, and one that ran out at the limit.
  - P3 made one answer that came back empty, and its other five attempts ended in transport failures.
- **Two formats.** Atria answered the whole brief, and Mimo answered parts, of which one of three was accepted. The side-by-side comparison must say so.
- **One model family on the ruling side** (04 section 8). The reader of this part is a Claude subagent, like the determiner.

---

## 9. Files

- **The returns:** `results/S87 Cross-examination - the S81 determination - returns/Mimo in three parts/`.
  - `s87_xexam_mimo_P2.response.txt`: the one accepted reply (sha256 334d9215cd4e…).
  - `s87_xexam_mimo_P1.receipt.json`, `…_P2.receipt.json`, `…_P3.receipt.json`: the receipts.
  - `…_P1.error.txt`, `…_P3.error.txt`: the error files.
  - The `*.reasoning.txt` and `*.truncated.txt` files: attempt files, kept and not read.
- **The texts sent:** `tests/S87 Cross-examination - part P1, O5 O30 O17.md`, `… part P2, O35 O40.md` and `… part P3, O48 O45 and the standing clause.md`.
- **The rules this reading follows:** 05 and 05b in this folder.
