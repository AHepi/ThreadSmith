# 10 Reading of Mimo's retry - O5 and O30

*Written by a Claude subagent for the orchestrator on 24 September 2026, from about 03:00 UTC. The reading follows 05 as extended by 05b and 05c. The two calls were pass 2 under `results/S90 and S87 - seven calls rerun after the container restart - written before sending.md` (the rerun note). Mimo is "auditor 2" in the briefs.*

*O5 was re-read by a fresh Claude determiner, one that did not write the determination. That re-reading is kept unchanged as `raw readings/10a re-read O5.md`. O30 was not re-read (section 3). This file records the re-reading and adds no ruling of its own. Section 11 then sets every reading of the cross-examination side by side, as 05c item 7 allows now that all three retry readings are written, and gives the standing verdict and the coverage of the pressed rows by each outside model.*

*What the recorder opened and did not open.*
- **Opened:**
  - the receipts and replies of `s87_xexam_mimo_O5` and `s87_xexam_mimo_O30`;
  - the two retry texts, for their sha256 and for the determination's words that the O30 reply quotes;
  - 05, 05b, 05c, the READ ME and the rerun note, in full;
  - 04, at its ruled rows for O5 and O30 and at sections 5(b) and 7.10;
  - the determiner's re-reading of O5, in full;
  - 06, 07, 08 and 09, for section 11;
  - file 10 and file 11 at the lines the O30 reply quotes, and the case book at O30;
  - the change-list entry W12.1 (R40), for section 9.
- **Disclosed.** The recorder opened 06, 07, 08 and 09 before writing this file, because section 11 sets all the readings side by side. 05c item 7 asks the reader of a retry reply not to open them until its own reading is written.
  - For O5 the reading is the determiner's (10a). It was written without them. It discloses one sentence of R10's REASON that reports 06, and does not rely on it.
  - For O30 this file adds no ruling. The reply says RULING STANDS and names no away-row, so rule 2 sends nothing to a determiner. What this file records of O30 is the receipt, the closing line and a check of the quotations against the texts.
- **Not opened:**
  - any reasoning or attempt file of either call, including the rejected pass-2 attempt 1 of each (`*.pass2.a1.*`);
  - Atria's reply, part P2's reply and the O17 retry reply. Those replies are known here only through 06, 08 and 09.

---

## 1. The receipts

Both calls went in pass 2 under the rerun note, with the job list `tools/s90 and s87 jobs - rerun after restart.json` (sha256 dfd30a792ca1…). Each used the same text and settings as pass 1 (effort medium, max_tokens 131,072 on both rungs, 6 attempts, `max_rejects` 3), except `max_pass`, which the rerun note raised from 1 to 2.
- **Pass 1 of both was cut by the container restart** (rerun note, section 1). Each ended as failed at 23:37:33, on the dead proxy, not on anything the model did.
- **Pass 2's replies were committed as returned at 286d69c** (01:58:22 UTC on 24 September), with the receipts, requests and attempt files.

**O5** (`s87_xexam_mimo_O5`). Pass 2 was asked at 23:45:32 UTC on 23 September and ended at 01:55:48 on 24 September (7,816.7 s).

| attempt | status | what came back | result |
|---|---|---|---|
| 1 | 200 | finish "length" after 2,996.7 s, 0 characters | rejected ("finish length") |
| 2 | 0 | nothing, after 1,102.5 s | no answer |
| 3 | 0 | nothing, after 1,059.9 s | no answer |
| 4 | 200 | finish "stop" after 2,537.6 s, 7,605 characters, 0 bad chunks | **accepted** |

- The response's sha256, 074802f4181c…, matches the receipt.
- The request's sha256, 910816995820…, matches the receipt's `request_sha256`, and the pass-2 request is byte-identical to pass 1's.
- The receipt's `user_sha256`, 97297d856d51…, is the sha256 of `tests/S87 Cross-examination - retry, O5 alone.md`, as 05c section 3 gives it.
- The last line is END OF REPORT. The reply is 1,237 words by `wc -w`, against a limit of about 2,000.
- Usage: 24,585 prompt tokens and 108,731 completion tokens, of which 106,892 were reasoning, against the 131,072 allowed.

**O30** (`s87_xexam_mimo_O30`). It waited in the runner's queue until Mimo B2 freed a slot. Pass 2 was asked at 00:19:58 and ended at 00:51:27 on 24 September (1,889.2 s).

| attempt | status | what came back | result |
|---|---|---|---|
| 1 | 200 | finish None after 630.1 s, 0 characters | rejected ("finish None") |
| 2 | 200 | finish "stop" after 1,259.0 s, 7,990 characters, 0 bad chunks | **accepted** |

- The response's sha256, 62d24d9408a2…, matches the receipt.
- The request's sha256, ef65034f01f9…, matches the receipt's `request_sha256`, and the pass-2 request is byte-identical to pass 1's.
- The receipt's `user_sha256`, a6db38cc09e2…, is the sha256 of `tests/S87 Cross-examination - retry, O30 alone.md`.
- The last line is END OF REPORT. The reply is 1,335 words by `wc -w`.
- Usage: 24,331 prompt tokens and 63,253 completion tokens, of which 61,285 were reasoning.

**So both replies can be read**, under rule 5 of 05 and item 1 of 05c's section 6, as the rerun note (ruling 4) extends them to pass 2.

---

## 2. The closing lines

- **O5:** `O5: RULING FALLS — file 11 SILENT`
- **O30:** `O30: RULING STANDS`

Neither reply names a new away-row.

---

## 3. What rule 2 sends to a fresh determiner

- **O5 goes to a fresh determiner.** The reply says RULING FALLS (rule 2 of 05; item 4 of 05c's section 6). The re-reading is `raw readings/10a re-read O5.md` (section 6).
- **O30 does not.** The reply says RULING STANDS and names no away-row, so neither condition of rule 2 holds. That is how 09 treated O17, and O30 has no re-reading.

---

## 4. The determination's rulings (04)

- **O5, 04's ruled table:** "O5 | f11≠base; step 4 | A A · S S · S A S | AGREE (base) | AGREE | SAME | CHANGED (additive): f11 L161 s3, L514 | — | no change | no | T, R: UPHELD (medium)".
- **O30, 04's ruled table:** "O30 | f11≠base; Part 3; step 4 | A A · S A · S P A | AGREE (base) | AGREE | SAME | CHANGED (additive): f11 L419 s2, L465 | — | no change | no | T, R: UPHELD (medium)".
- **04, section 5, test (b).** O5, O30 and O17 are the three rows on which a file-11 SILENT would have been AGREE→SILENT, a change away through new sentences of file 11, and (b) would have failed.
  - **O5**, "Greta's dough": "4 of 5 file-11 readings SILENT, on f11 L161 s3 ("the semantics records the restriction and supplies no rule that certifies it"). Ruled AGREE: Greta's account states the ground of her limit, and f11 L514 makes "what makes a restriction appropriate" a stated input on which the verdict is "a verdict given the input". Upheld at medium confidence."
  - **O30**, "The routine uploaded that morning": "2 SILENT and 1 SPLIT of 5, on f11 L419 and L514 (no boundary declared in words). Ruled AGREE: the situation says "The robot compares the pressures itself", which names the system and places the process in it, and f11 L419 s2's "a process that runs inside the boundary is the system's own today whoever wrote it" gives both halves of the verdict. Upheld at medium confidence."
- **04, section 7.10, the two reading hazards.** It records one hazard in f11 L161 s3 (O5) and one boundary hazard in f11 L419 with L514 (O30, O17), each "for a later revision".

---

## 5. O5: Mimo's argument

The determiner's re-reading gives the argument at length (10a, section 2). In short:
- **SILENT on the first point of the fixed verdict, "This is a legitimate narrowing".** f11 L161 s3 and L514 "each time withhold" an evaluation of appropriateness: "On this point they record the claim's ground and abstain. SILENT precedes AGREE in the rules' order, so if it fits, AGREE is not reached."
- **The analogy with Part XI.** "f11 L514 *classifies* verdicts … it does not manufacture one." The obligations O and P are recorded and not judged, so the theory gives repair verdicts given O and P, "never a verdict on their merits". Restriction-appropriateness is "the same kind of item".
- **Reading L161 s3 as a criterion contradicts it.** Read that way, the semantics "would be supplying exactly 'a rule that certifies it'".
- **"Same finding" is applied without its first condition.** "Recorded, uncertified, criticizable" is "a statement that no finding is established."
- **The theory cannot tell Greta's limit from the Tuesday limit.** Non-vacuity cannot separate them, and "A machinery that can never find a narrowing illegitimate is not finding 'legitimate' here."
- **The consequence.** SILENT makes O5 a theory change away through M17 and M48. SPLIT is considered and rejected. The file-10 mark stands.

Every quotation the reply relies on was found word for word (10a, section 2).

---

## 6. O5: the re-reading by the fresh determiner

The re-reading is `raw readings/10a re-read O5.md`, md5 cf572768966a0ef1a4d4e641b0112b76. It is copied unchanged from the working file `rerule O5.md`.
- **What it opened:** 04 (sections 1–7), 04b (the O1 group), 04c and 04d at O5, 04e's O5 packet, 05, 05b, 05c, the rerun note, the S90 rule and the S90 Parts rule, files 10 and 11 at the lines it names, and the case book at O1 and O5. For its reconciliation it also searched the S90 batch-1 and batch-2 readings and read the change-list entry W57.1 + W32(b).1 (R10).
- **What it did not open:** Atria's reply, 06, 07, 08, 09, the O30 and O17 retry replies and their readings, 07a, 09a, part P2's reply, and any attempt or reasoning file.
- **Its one disclosure.** It read one sentence of the R10 entry's REASON that reports Atria's position, and nothing in its ruling relies on it.

**Its ruling, column by column:**

| column | ruling |
|---|---|
| file-10 mark | AGREE, by the baseline rule. Both 1K returns are AGREE. The reply does not contest it. |
| file-11 mark | AGREE |
| verdict | SAME |
| passage | CHANGED (additive): f11 L161 s3 (M17) and L514 (M48), which have no file-10 counterpart |
| direction | none |
| kind | no change |
| confidence | medium, as in the determination |

**Its reasons for the file-11 AGREE.**
- **Neither route to SILENT that the mark rules name fits.**
  - *"An input the case leaves unstated."* L514 does take "what makes a restriction appropriate (Part III)" as a stated input, but the case states it: "her account says why: the yeast that makes the gas works slowly in the cold." This route fits O1, where no ground is given, and O1 is ruled SILENT.
  - *"Its sentences stop short of deciding it."* L514 does not stop short. It sets "a verdict given the input" against "where the input is missing, the verdict is unsettled". A reading on which the verdict stays unsettled when the input is present, Mimo's "abstention in both directions", denies that contrast in its own terms.
- **Point (ii), "The limit follows from a part of her account", is reached.** The yeast's relation to the gas changes under the temperature edit, which is the causal-assignment signature of f11 L125 (= f10 L140).
- **"Same finding".** "Given the stated ground, and open to criticism" is a qualification. The fixed verdict states legitimacy on the same ground.
- **SPLIT is not ruled.** L514's second sentence settles the choice, and the reply itself rejects SPLIT.
- **The reply's points answered.**
  - **The Part XI analogy fits the ruling.** The inputs O and P are recorded and not judged, and Repair is given with them. Worth is a different verdict that needs another input, \(\mathcal N\) (L27, L447), which L514's list does not include.
  - **Reading L161 s3 as placement is the ruling's reading too.** The verdict comes from L514 and is relative to the claim's own ground, so the semantics certifies nothing.
  - **What separates Greta's limit from the Tuesday limit is L514's contrast**, not non-vacuity: a stated ground against a missing one.
  - **"Can never find a narrowing illegitimate" is a limit of the theory, recorded as a residual hazard.** It is not a failure to reach "legitimate" where a ground is stated.

**Its record line (05 rule 3), exact:**

````text
After the cross-examination (s87_xexam_mimo_O5, pass 2, attempt 4, accepted; "O5: RULING FALLS — file 11 SILENT"): re-read by a fresh determiner; RULING STANDS. File 10 AGREE (baseline, both 1K AGREE); file 11 AGREE; verdict SAME; passage CHANGED (additive), f11 L161 s3 and L514; no change; not away; test (b) unaffected. The reply reads L161 s3 and L514 as withholding a verdict on appropriateness even where the claim states its ground. L514 contrasts "a verdict given the input" with "where the input is missing, the verdict is unsettled", and the mark rules make SILENT on an input turn on an input "the case leaves unstated"; Greta's case states it ("her account says why"). The reply's Part XI analogy fits the ruling: inputs are recorded and not judged, and verdicts that depend on them are given with them. Worth is a different input (N; L27, L447). Confidence medium; the L161 s3 reading hazard stands as recorded.
````

**The hazard remains.** Four of five earlier file-11 readings and this reply took L161 s3's wording to withhold the verdict. 04 section 7.10 records the repair for a later revision (section 9).

---

## 7. O30: Mimo's argument, and the quotations checked

Mimo's closing line is `O30: RULING STANDS`. The reply raises three attacks and rejects each, then checks the rest of the row.
1. **SILENT on points A and C, from the declared-boundary rules.** Mimo calls this "the strongest attack on the ruling; it fails, but on a single hinge".
   - *The attack.* f11 L419 s1, L465 s3 and L514 s2 make ownership turn on a declared boundary. L419 s2 closes "not where the process sits in the casing". The case states only seat and possession facts, and 04's words "places the process inside it" take the step that clause bars.
   - *Why it fails.*
     - The SILENT prong keys on an input "the case leaves unstated". f11 L465 s1 defines the boundary as "which processes and resources are the system's", and the situation states exactly that: "The robot compares the pressures itself" says whose act the comparison is, and "a routine a remote person uploaded to it" states the routine's outside source.
     - 04's word "places" is loose, but its actual ground is the situation's "itself".
     - On dependence, no boundary consistent with the situation flips a finding, so nothing is unsettled.
2. **SPLIT from f11 L419 s2's two clauses.** This fails in three steps.
   - Part XII states the process rule flat (f11 L465 s2: "a process run inside the boundary is the system's whoever wrote it").
   - "Whoever wrote it" would have no case if a process written outside and handed in were outside work.
   - The two clauses compose into the fixed verdict's own division: the routine keeps its source (with f11 L401 s3, "relay is not"), and the running is the system's today.

   Nor does clause 1 give DISAGREE.
3. **Point D read through the defined term "Origin" (G)** fails quickly. The verdict glosses its own word: "Who wrote the routine is a separate fact, and a true one". File 10 carries the same vocabulary (f10 L414 s3).
4. **The rest of the ruling checked.**
   - The file-10 AGREE is fixed by the mark rule, and the text supports it (f10 L414).
   - The verdict is SAME.
   - The passage is CHANGED (additive). f10 L523, "declared indices", says nothing of ownership, and "I cannot overturn" the CLAIM reading of f11 L419 s2 and L465.
   - Direction and kind follow. The row's stakes are "correctly stated", "and that consequence is exactly why the boundary hazard the determination records for a later revision is worth recording."

**Checked by the recorder.** Every quotation the reply relies on is word for word in the texts:
- **file 11:** L419 s1 and s2 (including "and where the boundary is drawn decides, not where the process sits in the casing"), L465 s1, s2 and s3, L467 last, L514 s2 and L401 s3;
- **file 10:** L414 ("relay is not") and L523;
- **the case book, at O30** (md5 4f488d149e44669240d5db546c8e946a): "The robot compares the pressures itself", "a routine a remote person uploaded to it", "Who wrote the routine is a separate fact, and a true one" and "Ownership of today's history is the robot's; the origin of the routine is the person's";
- **the determination's words, as the retry text's section 5 gives them:** "The case names the system and places the process inside it", "open to the strict reading, and three of five readers took it", "an input is missing where the situation leaves open alternatives that give different verdicts" and "No boundary consistent with the situation excludes the comparison".

**What bears on the verdict.** Nothing changes. The reply takes up the boundary hazard of 04 section 7.10 and confirms the ruling on the situation's "itself". 1C A had called "itself" "the verdict's word", and 04 section 7.10 records that misreading.

---

## 8. Changes of ruling

- **None.** No mark, verdict, passage, direction or kind changes on O5 or O30. Rule 3 of 05 has nothing to record as a change. The O5 record line in section 6 records the re-reading and its result.
- **Away: no.** O5 and O30 both stay AGREE→AGREE, so neither is a theory change away from the thoughtful person.
  - Test (b) keeps its footing on both rows, and rule 4 of 05 is not engaged.
  - The standing verdict is not applied again on account of either row.
- **04's counts stand**, as 07, 08 and 09 give them:
  - file 10: AGREE 44, SILENT 6, SPLIT 1, DISAGREE 1;
  - file 11: AGREE 46, SILENT 6;
  - verdicts: 50 SAME, 2 CHANGED (O45 and O48, both toward the thoughtful person);
  - passages: 20 CHANGED;
  - S75 corrections: 3 (O20, O40, O45).

---

## 9. The two rows and revision 2

These notes follow the determiner's reconciliation (10a, section 6). They are not rulings on revision 2.
- **O5 and R10.** R10 is W57.1 + W32(b).1, the revision-2 entry at f11 L161.
  - Its CASES AT RISK reads "O5 stays AGREE, and the hazard is closed". That is the file-11 mark 10a upholds, so nothing needs reconciling.
  - Both S90 replies to part B1 gave R10 STANDS, and neither contested it (S90 batches 1 and 2). Mimo B1's point 4 on R10's phrase "the ground of its restriction" was passed to the orchestrator as a presentation point.
- **O30 and R40.** R40 is W12.1, the revision-2 entry at f11 L465. It drafts the boundary repair that 04 section 7.10 asks for: "Where the system's boundary is not declared explicitly, a statement that names the system and says whether a process runs inside it or outside it declares the boundary for that process". Its REASON names the O30 and O17 hazard. Both S90 replies to part B2 gave R40 STANDS, and neither contested it (S90 batch 3).

---

## 10. Confounds, as they fell out

- **Selection by the ceiling.**
  - O5's accepted run used 106,892 reasoning tokens of the 131,072 allowed. Its first pass-2 attempt ran into the limit with no content.
  - O30's accepted run used 61,285, about half of what the other two retry replies used. Its first attempt came back empty (finish None).
- **A second pass.** Both rows had two passes, where O17 had one. Pass 1 was cut by the network, not by the model (rerun note, ruling 1). In pass 2, O5 needed four attempts and O30 two.
- **Timing.** Pass 2 went out after 06, 08 and 09 were written, and after S90 batches 1 and 2 were read. Mimo saw none of them.
- **Cases the reasons cite without giving them.** O5's reasons cite O1. O30's cite O17, O35, O41 and O51. The O5 reply uses O1 only as the determination's reasons name it, and the O5 determiner checked O1 against the case book. The O30 reply names no other case.
- **The recorder opened 06, 07, 08 and 09 before writing this file** (see the head of this file). The O5 re-reading was made without them, and O30 had no re-reading.
- **One model family on the ruling side** (04, section 8). The determiner and the recorder are Claude subagents, like the determiner of 04.

---

## 11. After every reading: side by side, the standing verdict, and the coverage of the pressed rows

All the readings of the cross-examination of the S81 determination are now written:
- **06**, Atria's reply to the whole brief;
- **07**, the supplementary audit of Mimo on tester A, read under its own rule and outside the cross-examination;
- **08**, Mimo's three parts, of which only P2 was accepted;
- **09**, Mimo's retry of O17;
- **10**, this file: Mimo's retry of O5 and O30.

05c item 7 and 05b item 7 set them side by side only now.

### 11.1 The seven pressed rows, side by side

| row | what it decides | the determination (04) | Atria (06, whole brief) | Mimo, cross-examination | Mimo, supplementary audit of tester A (07) | ruling after all readings |
|---|---|---|---|---|---|---|
| O5 | test (b) | f10 AGREE (base), f11 AGREE, SAME, CHANGED (additive) | RULING STANDS | part P1 failed (08). Retry (10): RULING FALLS — file 11 SILENT; re-read by a fresh determiner (10a): stands | not audited (parts 1 and 2 failed) | **stands** |
| O30 | test (b) | f10 AGREE (base), f11 AGREE, SAME, CHANGED (additive) | RULING STANDS | part P1 failed (08). Retry (10): RULING STANDS | part 3: the four fields agree; the audit takes the ruling's side against tester A | **stands** |
| O17 | test (b) | f10 AGREE (base), f11 AGREE, SAME, CHANGED (additive) | RULING STANDS | part P1 failed (08). Retry (09): RULING STANDS | not audited (parts 1 and 2 failed) | **stands** |
| O35 | test (b) | f10 SILENT (base), f11 SILENT, SAME on the same point | RULING STANDS | part P2 (08): RULING STANDS | part 3: BLIND MARK DISAGREE differs; re-read (07a): stands | **stands** |
| O40 | S75 correction, or a change toward | f10 AGREE (S75 corrected), f11 AGREE, SAME | RULING STANDS | part P2 (08): RULING STANDS | part 4: the four fields agree | **stands** |
| O48 | test (a) and prediction P1 | f10 DISAGREE, f11 AGREE, CHANGED, toward | RULING STANDS | part P3 failed (08); not sent again (05c section 2): **not examined by Mimo** | part 4: the four fields agree | **stands** |
| O45 | prediction P2 | f10 SPLIT (S75 corrected), f11 AGREE, CHANGED, toward | RULING STANDS | part P3 failed; not sent again: **not examined by Mimo** | part 4: the four fields agree | **stands** |

- **The supplementary audit's column is for reference only.** It audits tester A's marks, not the determination's rulings, and it stands outside the plan's table. Its agreements count as no confirmation and as no test passed (07, rule 4).

**Where two readings rule differently on one row.** None do. Every reading leaves every ruling standing: 06 without re-reading any row, 07 after re-reading O35 and O50, 08 without re-reading, 09 after a re-reading beyond rule 2, and 10 after re-reading O5.

**Where the two outside models' replies differ.** They differ on one row, O5.
- Atria says RULING STANDS (06).
- Mimo says RULING FALLS — file 11 SILENT (10).
- Under 05c item 7, both are recorded and the difference is resolved in writing from the texts. That is 10a's re-reading, made without 06. It comes to the determination's ruling on every column, on two grounds:
  - L514's contrast between "a verdict given the input" and "where the input is missing, the verdict is unsettled";
  - O1 as the contrast where the input is missing.
- 06 records that Atria rejected the SILENT reading on the same two grounds, after trying it as "the strongest challenge on the row". The two readings reached them independently.
- 10a also answers what Atria did not raise: Mimo's analogy with Part XI, its point that reading L161 s3 as a criterion contradicts it, and its point that the theory "can never find a narrowing illegitimate".

**Differences of route or citation.** None changes a ruling. 06 and 08 recorded those of Atria and of part P2; the one on O30 from Mimo's retry is new here.
- **O30.** Atria gave "running inside the robot" as the situation's words. They come from O30's fixed verdict ("The comparison ran inside the robot") and from O17's situation (06). Mimo quotes the situation correctly, and calls 04's word "places" loose, with "itself" as its real ground (section 7).
- **O40.** Atria cited f11 L27 s3 and L433 s4 for the file-11 route (06). Mimo had each file reach the "mostly" point "by its own route" (08). Both differ from 04's listing, and neither changes an element.
- **O5.** Atria cited f11 L149 for the yeast's signature; the causal-assignment clause is f11 L125 (06).

### 11.2 Coverage of the pressed rows by each outside model

| | O5 | O30 | O17 | O35 | O40 | O48 | O45 | the standing clause and the P2 scoring choice | task 2: other rows that move away | task 4: anything else |
|---|---|---|---|---|---|---|---|---|---|---|
| **Atria** (the whole brief, one call, 06) | STANDS | STANDS | STANDS | STANDS | STANDS | STANDS | STANDS | STANDING VERDICT: UPHELD | none found, 7 families tried | answered (06 section 5) |
| **Mimo** (the single call failed; three parts, 08; one row per call, 09 and 10) | FALLS; re-read, stands | STANDS | STANDS | STANDS | STANDS | not examined | not examined | not examined | not asked | not asked |

- **Atria examined all seven pressed rows**, the standing clause, the P2 scoring choice, and tasks 2 and 4, in one reply.
- **Mimo examined five of the seven pressed rows:** O35 and O40 in part P2, O17 in its retry, and O5 and O30 in theirs.
  - O48, O45 and the standing clause went only in part P3, which failed and was not sent again (05c section 2).
  - Mimo's single call on the whole brief failed, and no Mimo call was asked tasks 2 or 4.
- **By what each row decides:**
  - **Test (b)** turned on O5, O30, O17 and O35. All four have now been examined by both outside models. On three, both said RULING STANDS. On O5, one said STANDS and the other FALLS, and the fresh determiner's re-reading upholds the ruling.
  - **Test (a) and prediction P1** (O48), **prediction P2** (O45) and **the standing clause** each have one outside reading, Atria's.
  - **O40** (an S75 correction rather than a change toward) has both.
- **Formats differ,** as 05b and 05c said they would.
  - Atria answered the whole brief in one reply.
  - Mimo answered one part of two rows (P2) and three texts of one row each.
  - Mimo's texts were cut from the brief Atria answered. Each carried all of file 11 and the determination's summary, but only its own rows' cases and the file-10 lines those rows need, so no Mimo reply could draw on work on the other rows.

### 11.3 The standing verdict after every reading

No reading changed a ruling, so the inputs are 04's.
- **Tests.**
  - **(a) HOLDS** (O48).
  - **(b) HOLDS.** No ruled file-11 mark lies further from AGREE than its ruled file-10 mark. O5, O30 and O17 stand AGREE in both files, and O35 stands SILENT in both, on the same point. No reply names a new away-row.
  - **(c) HOLDS.**
  - **(d) HOLDS.**
- **Predictions.**
  - **P1 HOLDS.**
  - **P2 FAILS**, at O45 alone, by a theory change toward the thoughtful person, on the adopted reading.
  - **P3 FAILS**, only by undeclared CLAIM places, none shown harmful by any case.
- **Clauses.** The first does not apply, and the third does not apply. The second applies.

> **THE STANDING VERDICT AFTER EVERY READING OF THE CROSS-EXAMINATION (06, 07, 08, 09, 10):** File 11 stands as the authority under the plan's second clause, with P3's 41 undeclared CLAIM places inside the theory (none shown harmful by any case), P2's failure at O45 (a theory change toward the thoughtful person), the three S75 corrections and the seven errata recorded against its frozen note in S81 Results. This does not differ from the determination's verdict.

**The limits of this support.**
- **Each reply is evidence, not a result** (rule 1).
- **O48, O45 and the standing clause rest on one outside reading.**
- **The rows test (b) turned on now have two,** and on one of them (O5) the two replies disagree. There the ruling rests on the re-reading from the texts, at medium confidence, with the L161 s3 hazard recorded.
- **One model family is on the ruling side** (04, section 8).

**For S81 Results.**
- No ruling changed after the cross-examination.
- One pressed row, O5, was said to fall by one outside reply, and it was re-read and upheld.
- The findings about the readers recorded in 06, 07 and 08 stand. This file adds none.

---

## 12. Files

- **The returns**, in `results/S87 Cross-examination - the S81 determination - returns/Mimo retry one row per call/`, committed at 286d69c:
  - `s87_xexam_mimo_O5.response.txt` (sha256 074802f4181c…) and `s87_xexam_mimo_O30.response.txt` (sha256 62d24d9408a2…), the accepted replies;
  - their `.receipt.json` and `.request.json`;
  - their `.reasoning.txt` and the rejected attempts `*.pass2.a1.*`, kept and not read;
  - pass 1's files, under their `.pass1.*` names.
- **The texts sent:** `tests/S87 Cross-examination - retry, O5 alone.md` and `… retry, O30 alone.md`.
- **The re-reading:** `raw readings/10a re-read O5.md`, copied unchanged from the working file.
- **The rules this reading follows:** 05, 05b and 05c in this folder, and the rerun note.
- **The S90 reading of the same rerun:** `results/S90 Reading of the replies - batch 3 (Mimo B2, Mimo C, Atria B2, Atria A1, Atria C).md`.
