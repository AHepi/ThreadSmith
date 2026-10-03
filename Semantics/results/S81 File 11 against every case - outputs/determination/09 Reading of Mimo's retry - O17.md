# 09 Reading of Mimo's retry - O17

*Written by a Claude subagent for the orchestrator on 23–24 September 2026, from about 00:00 UTC on 24 September. The reading follows 05 as extended by 05b and 05c. Mimo is "auditor 2" in the briefs. The re-reading of the row was done by a fresh Claude determiner, one that did not write the determination. It is kept unchanged as `raw readings/09a re-read O17.md`. This file records that re-reading and adds no ruling of its own.*

*What the recorder opened and did not open.*
- **Opened:**
  - the receipt and the reply of `s87_xexam_mimo_O17`;
  - 05, 05c and the READ ME in full, and 05b in part (its first 80 lines);
  - 04, at its section headings and at sections 5 and 6;
  - the determiner's re-reading, in full;
  - the retry text `tests/S87 Cross-examination - retry, O17 alone.md`, for its sha256 only.
- **Also opened, and disclosed:** 08, the reading of part P2. The recorder opened it before writing this file, to follow its form. 05c item 7 lists 08 among the files the reader of a retry reply does not open until its own reading is written.
  - The determiner who re-read the row did not open 08. Its own "Not opened" list names 06, 07 and 08.
  - This file takes its ruling from the determiner and adds none.
  - The only thing 08 says of O17 is that part P1 failed and the row was not examined by Mimo there (08, sections 2 and 6).
- **Not opened:** Atria's reply, 06 and 07; part P2's reply; any reasoning or attempt file. The other two retry calls were not opened either: of O5 and O30 the recorder saw only the names of their files in a folder listing.

---

## 1. The receipt

The call is `s87_xexam_mimo_O17`, run by `tools/s87_run.py` with `tools/s87_jobs - Mimo retry, one row per call.json` (sha256 2e2e61c841f8…).

| attempt | status | what came back | result |
|---|---|---|---|
| 1 | 200 | finish "stop" after 2,482.4 s (it waited 710.1 s for a slot first), 8,220 characters, 0 bad chunks | **accepted** |

- **It was accepted on its first attempt, in its one pass.** The last line of the reply is `END OF REPORT`.
- **The hashes match the receipt.**
  - The response's sha256, 368c1bb3d3b6…, matches the receipt.
  - The request's sha256, c38eb3b817f9…, matches the receipt's `request_sha256`.
  - The receipt's `user_sha256`, e1adbdde463b…, is the sha256 of the O17 retry text, as 05c section 3 gives it.
- **Length and usage.** The reply is 1,392 words by `wc -w`, against a limit of about 2,000. It used 23,928 prompt tokens and 123,261 completion tokens, of which 121,326 were reasoning, against the 131,072 allowed.
- **The container restart.** The reply came back at 23:26:18 UTC on 23 September. The container restarted at about 23:30. The reply was committed after the restart, at c137e86 (23:32:35), with its receipt and reasoning file. Its sha256 matches the receipt, so no data was lost.
- **So under rule 5 of 05 and item 1 of 05c's section 6, the reply can be read.**

---

## 2. The closing line

**Mimo's closing line:** `O17: RULING STANDS`

- The reply raises three attacks on the ruling and rejects each one (section 5).
- It names no new away-row.

---

## 3. Rule 2 does not send the row to a fresh determiner

- **What the rule asks for.** Rule 2 of 05 and item 4 of 05c's section 6 send a row to a fresh determiner in two cases only:
  - the reply says RULING FALLS;
  - the reply names a new away-row.

  Neither holds for O17.
- **Why a determiner read the row anyway.** The orchestrator's task asked for a re-reading, on the premise that the reply "says the ruling FALLS". The premise was wrong: the reply's closing line is RULING STANDS.
- **How the re-reading is recorded.** The determiner did the re-reading as asked and recorded it as a reading beyond rule 2. It comes to the determination's ruling on every column, so nothing depends on the wrong premise.

---

## 4. The determination's ruling (04, 04b)

- **04, ruled table:** "O17 | f11≠base; step 4 | A A · S A · S A A | AGREE (base) | AGREE | SAME | CHANGED (additive): f11 L467 last, L419 s1 | — | no change | no | T side check".
- **04, section 5, test (b).** O17 is one of the three rows, with O5 and O30, on which a file-11 SILENT would have been AGREE→SILENT through new sentences of file 11. That would be a change away, and test (b) would fail. 04 records 2 of 5 file-11 readings SILENT. It rules file 11 AGREE on f11 L467 last: "Ownership is grounded in the processes and resources the boundary includes, never in the capability being attributed".
- **04b, the four reasons for the file-11 AGREE:**
  - L467 gives the verdict's contrast exactly;
  - the boundary input is present, because the case names the system and places the process in it;
  - the casing clause of L419 applies where a declared boundary and the casing come apart (O41), or where the author is remote (O30), and O17 has neither;
  - at most, the theory adds "given that the robot's boundary includes the routine", and that is the same finding with a qualification.
- **The rest of the ruling.**
  - The file-10 mark is AGREE, the baseline, and both 1K returns agree with it.
  - The verdict is SAME, and the passage CHANGED (additive), through M45 and M37.
  - There is no direction and no change.
  - Confidence is medium.

---

## 5. Mimo's argument

The quotations below are from the reply. The determiner's re-reading gives them at more length.

1. **File 11 SILENT is put at full strength, and then rejected.**
   - The attack: the log shows only the casing fact, f11 L419 s2 disclaims it ("not where the process sits in the casing"), and f11 L465 and L514 make the boundary a declared input the case never states. Mimo grants that "The pressure is real".
   - It rejects the attack on the case's text: "The case's first sentence states whose processes the work is: 'A repair robot keeps a log of every comparison it runs.' … The input is therefore stated, not missing".
   - It names the condition the ruling turns on: "had the case said only that a routine ran 'inside the robot', with no 'every comparison it runs', the attack would succeed".
2. **DISAGREE, through f11 L467 s3 and L419 s2, is rejected.** The ground is "the processes themselves … with the boundary as qualifier", which is the fixed verdict's finding with "a qualification, a limit or a more exact wording" under "Same finding".
3. **SPLIT, reading the maker's routine as "work supplied from outside", is rejected.** "'whoever wrote it' is written for exactly this case … One reading, not two."
4. **The other elements hold.** The file-10 mark is AGREE by the baseline rule and on the text. The verdict is SAME, with no change, and the passage is CHANGED (additive). Mimo adds that Atria's blind mark is SILENT in one audit and AGREE in the other, "so the SILENT support is thinner than two names suggest".

---

## 6. The re-reading by the fresh determiner

The re-reading is `raw readings/09a re-read O17.md`, md5 bc6d65e342103644ec583d27f0e25f8f. It is copied unchanged from the working file `rerule O17.md`, written at about 23:51 UTC on 23 September. It opened 04, 04b (the O1 group), 04c, 04d, 04e (the O17 packet), 05, 05b, 05c, file 10, file 11, the case book at O17, O30, O41 and O51, the plan and the mark rules. It did not open Atria's reply, 06, 07, 08, part P2's reply, the other two retry replies, or any attempt file of part P1.

**Its ruling, column by column:**

| column | ruling |
|---|---|
| file-10 mark | AGREE, by the baseline rule. Both 1K returns are AGREE, which is the baseline itself. |
| file-11 mark | AGREE |
| verdict | SAME |
| passage | CHANGED (additive), through f11 L467 s3 last (M45) and L419 s1 (M37), with L465 (M44) for the boundary |
| direction | none |
| kind | no change |
| case disputed | not raised |
| confidence | medium, as in the determination |

**Its reasons for the file-11 AGREE:**
- **Points (ii) and (iii) of the fixed verdict are reached exactly.** f11 L467 s3 ("'owned because it can, and can because owned' grounds neither"), L419 s3 and L518's last sentence all refuse the manual's ground. No reading disputes this.
- **Point (i) is reached, with a qualification.** L467 s3 grounds ownership in "the processes and resources the boundary includes". The log is a record of those processes ("every comparison it runs"). The boundary enters as a qualifier, which is "Same finding".
- **The SILENT reading fails on the case as written.**
  - f11 L465 defines the boundary as "which processes and resources are the system's", and the situation names one system and its processes.
  - Only a boundary the situation does not state could exclude the routine. O41 and O51 show that where the case book means such a boundary, it states one in words.
  - So the input is given, not chosen from the verdict, and L514 is not engaged. This is the standard 04c applied to O35 and O30.
- **The casing clause of f11 L419 s2 is not engaged.** No fact of O17 separates the robot as a system from the robot as a body.
- **The same words of the case are read the same way under both files.** File 10 already makes the boundary a declared index (f10 L523 = f11 L516).
- **Mimo's "every comparison it runs" supports the ruling but does not settle it.** O51 uses "runs" of a module outside its declared boundary. What decides O17 is that it draws no boundary apart from the robot.
- **Neither SPLIT holds, DISAGREE does not hold, and Derivation 9 does not apply.**

**The hazard remains.** A reader who treats any situation without a boundary stated in words as missing the input can still read SILENT, and two of the five file-11 readings did. The repair recorded in 04, section 7.10 would remove the hazard. It is for L419 to say that "where a case names the system and places a process inside it, the boundary is given".

---

## 7. Changes of ruling

- **None.** No mark, verdict, passage, direction or kind changes on O17. Rule 3 of 05 has nothing to record.
- **Away: no.** O17 stays AGREE→AGREE, so it is not a theory change away from the thoughtful person.
  - Test (b) keeps its footing on this row, and rule 4 of 05 is not engaged.
  - The standing verdict is not applied again on account of O17.
- **04's counts stand, as 08 section 5 gives them.**
  - File 10: AGREE 44, SILENT 6, SPLIT 1, DISAGREE 1.
  - File 11: AGREE 46, SILENT 6.
  - Verdicts: 2 CHANGED (O45 and O48, both toward the thoughtful person).
  - S75 corrections: 3 (O20, O40, O45).
- **What the reply counts for.**
  - It is evidence, not a result (rule 1).
  - It is Mimo's independent examination of the row, with the closing line RULING STANDS.
  - Its point on Atria's blind mark is already recorded in 04, section 7.10.

---

## 8. The standing verdict after this reading

**This reading changes no ruling.** The standing verdict is therefore the one 04 section 6 gives, which 07 and 08 left unchanged:

> **File 11 stands as the authority under the plan's second clause, with P3's 41 undeclared CLAIM places inside the theory (none shown harmful by any case), P2's failure at O45 (a theory change toward the thoughtful person), the three S75 corrections and the seven errata recorded against its frozen note in S81 Results.**

**The limits of this support.**
- **It is evidence, not a result** (rule 1), and it covers O17 only.
- **What Mimo has now examined** of the rows that decided the verdict:
  - O35 (test (b)) and O40, in part P2 (08);
  - O17 (test (b)), here.
- **What Mimo has not examined:**
  - O5 and O30 (test (b)). They are pending (section 9).
  - O48 (test (a) and prediction P1), O45 (prediction P2) and the standing clause with the P2 scoring choice. Part P3 failed and is not sent again (05c section 2).

---

## 9. Pending: O5 and O30

- **Both calls were cut by the container restart.**
  - `s87_xexam_mimo_O5` and `s87_xexam_mimo_O30` were in pass 1 when the restart cut the proxy, at about 23:31 UTC.
  - Both ended as failed at 23:37:33. They failed on the dead proxy, not on anything the model did.
- **They are being sent again as pass 2,** under `results/S90 and S87 - seven calls rerun after the container restart - written before sending.md` (57482a5, faf91f6).
  - O5 started at 23:45:32.
  - O30 waits in the runner's queue for a Mimo slot.
  - There is no pass 3.
- **How each reply will be read.** On its own, under 05, 05b, 05c and the rerun note, independently of this reading. A pass-2 failure supports nothing, and its row is then recorded as not examined by Mimo.
- **The side-by-side comparison waits.** Under 05c item 7, the retry readings are set beside 06 and 08 only after all three are written. Where two readings rule differently on one row, both rulings are recorded, and the difference is resolved in writing from the texts.

---

## 10. Confounds, as they fell out

- **Selection by the ceiling.** The accepted run used 121,326 reasoning tokens of the 131,072 allowed. It finished on its first attempt.
- **One row per call.** The reply saw all of file 11, O17, the file-10 lines O17 needs and the determination's summary.
- **Cases the reasons cite without giving them.** The reasons cite O30 and O41, whose texts are not in the retry text. The reply uses them only as the determination's reasons name them. The determiner checked O30, O41 and O51 against the case book.
- **The premise of the task.** The re-reading was asked for on a premise the reply does not bear out (section 3). It is recorded as beyond rule 2 and changes nothing.
- **The recorder opened 08** before this file was written, against 05c item 7 (see the head of this file). The re-reading itself was made without it.
- **One model family on the ruling side** (04, section 8). The determiner and the recorder are Claude subagents, like the determiner of 04.

---

## 11. Files

- **The returns**, in `results/S87 Cross-examination - the S81 determination - returns/Mimo retry one row per call/`:
  - `s87_xexam_mimo_O17.response.txt`, the accepted reply (sha256 368c1bb3d3b6…);
  - `s87_xexam_mimo_O17.receipt.json`, the receipt;
  - `s87_xexam_mimo_O17.request.json`, the request;
  - `s87_xexam_mimo_O17.reasoning.txt`, kept and not read.
- **The text sent:** `tests/S87 Cross-examination - retry, O17 alone.md`.
- **The re-reading:** `raw readings/09a re-read O17.md`, copied unchanged from the working file.
- **The rules this reading follows:** 05, 05b and 05c in this folder, and the rerun note for O5 and O30.
