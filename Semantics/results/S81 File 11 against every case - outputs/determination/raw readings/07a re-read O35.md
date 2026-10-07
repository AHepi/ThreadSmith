# Re-reading O35 and O50 under the supplementary reading rule

*Written by a Claude subagent for the orchestrator on 23 September 2026 at about 17:05 UTC. Branch head when written: 392fe2d. This file follows rule 3 of the reading rule in `supplementary - Mimo on tester A in four parts/READ ME - written before sending.md`. Claude's step-3 rulings were written and committed before this re-read: 04 in b54556e, and 06 (the reading of Atria's cross-examination) in a0db21c.*

## Why these two rows are re-read

- Rule 2 compares four fields of the audit record with Claude's ruled file-11 mark: YOUR MARK, ON VERDICT, ON MARK and BLIND MARK.
- On O35 and on O50, three of the four fields match the ruling and only BLIND MARK differs. Under rule 3, one differing field is enough to send a row to a re-read.
- Under rule 4, the three matching fields are reported as agreement and nothing more. They count as no confirmation.

## The two parts are accepted

| part | rows in its Part 1 | finish | last line | response sha256 (receipt = file) | user sha256 (receipt = brief) |
|---|---|---|---|---|---|
| 3 | O27 to O39, O35 among them | "stop"; saw_done true; pass 1 | END OF REPORT | 21089fa2b711… | f028c1cbe704… |
| 4 | O40 to O52, O50 among them | "stop"; saw_done true; pass 1 | END OF REPORT | 3de8d8ae3033… | e25b7743190f… |

Each row is taken only from the Part 1 record of the part that lists it (rule 2). Part 2 lines and Part 3 are not used (rule 6).

**Two checks done by program for this file.**
- The BLIND READINGS block of each brief is, for O35 and O50, byte for byte Mimo's 2a return (`returns/s81_2a_mimo.response.txt`).
- The reading under audit is, for O35 and O50, byte for byte tester A's 1C return (`returns/s81_1C_A.response.txt`).

So each BLIND field restates the same 2a text that 04 has already weighed. The supplement's BLIND MARK is Mimo marking that text a second time. It is not a new reading.

## Read for this file

- The reading rule, in full.
- The part 3 and part 4 receipts, and the O35 and O50 records in the two responses.
- The part 3 and part 4 briefs: the mark rules and record form (lines 1–48), tester A's O35 and O50 rows, and Mimo's blind O35 and O50 rows.
- From 04: the header, section 2.2 (item 2), the ruled table, sections 4 (P3 harm, E2), 5 and 6, and 7.8 to 7.11.
- From 04b: O4 group, the head and O35 in full, and findings 1, 3 and 5. O1 group, the head, O21 in full and O50 in full.
- From 04c: the head, O35 (attempts 1 to 5), and the side checks at lines 250–260.
- From 04d: the lines naming O50.
- The 04e packets O35 and O50, in full.
- From 06: sections 1 to 5.3, and 6.
- The case book entries O21, O35, O38, O40, O41 and O50.
- File 10: L23, L25, L122, L164, L412, L414, L416–L428, L430, L432, L436–L446, L458, L472–L476 and L516–L523.
- File 11: L25, L27, L107, L149, L399, L401, L403–L412, L417, L419, L421, L425–L435, L447, L463, L465, L467, L512 and L514.
- Whole-file searches of both files. For O35: protected, occasion, loss, lost, during, interrupt, matter, at all times, stated condition, declared input, draw, held, exposed. For O50: mostly, credit, division, discover, outside contribution, whoever wrote, however close, achievement, ranking, weigh, inquiry, relay, counting jobs, share, proportion, together, joint, outside, incoming, inherited, attribution, system's, each contribution, found, fault.

**Not opened.**
- The S87 and S88 returns folders, and Mimo's reply to the cross-examination.
- The reasoning files and the truncated attempt files of every supplementary part.
- All files of parts 1 and 2.

---

## O35 — Four seconds

### 1. The ruling as it stands (04, O4 group of 04b, 04c, 04d, and 06)

- **File-10 mark: SILENT.** This is S75's baseline. Both 1K returns mark SILENT, so under the plan's rule no reading by Claude can move the mark.
  - It is SILENT on the text as well. (P) takes the protected obligations "fixed for the comparison" (f10 L438), and they are part of the question (f10 L164). The formula \(r(\xi)\Rightarrow r(\xi')\) (f10 L441) fixes *when* \(r\) is evaluated, not *what* it says.
  - A condition over the work interval is admissible, because values may be histories (f10 L122). O38 needs that reading.
  - The case names the thing protected ("the protected tap") but states no condition (04b O35 d; 04c attempts 1–3; 04 section 5(b)).
- **File-11 mark: SILENT.** Under f11 L433 s1, the protected condition and its occasions are declared inputs, and the case states neither. Under f11 L514, "where the input is missing, the verdict is unsettled."
- **The rest of the ruling:**
  - Verdict SAME, on the same point: whether the protected condition held, and whether the stop is a loss.
  - Passage CHANGED (additive): f11 L433 s1 and L514 (M38, M48).
  - Direction none. Kind: no change.
- **Changed from 01.** The file-10 mark went from AGREE to SILENT, the verdict from CHANGED to SAME, and the direction from away to none (04 section 7.9).
- **Checks.** Upheld by both lenses (T, R). The 04b contrary "Under file 11: DISAGREE (Mimo's 2a; Mimo on B's BLIND MARK)" was ruled FAILS: "It supplies the condition and its occasions, which the case does not state."
- **06.** Atria: "O35: RULING STANDS". Not re-read, and the ruling stands after 06.

### 2. What the supplement says (part 3 response, lines 109–121, quoted; the QUOTE lines are shortened to the lines they copy)

```
### O35
BLIND: The tap is a protected condition and the four-second stop is a failure on an occasion the condition covers, so the protection was lost, and the fact that nobody drew is outside the wording of the condition and must be exposed rather than folded in. The tap's later running does not restore the condition on the covered occasion.
BLIND MARK: DISAGREE
TESTER MARK: MARK: SILENT
ON VERDICT: AGREE
ON QUOTES: SUPPORTS, the quotations make the condition and its occasions declared inputs and make a missing input yield an unsettled verdict, which is exactly what the verdict argues.
ON SEARCH: CONFIRMED
ON MARK: AGREE
YOUR MARK: SILENT
QUOTE: [f11 L433 s1] (Part XI)
QUOTE: [f11 L514, last sentence] (Part XIV)
QUOTE: [f11 L27 s2] (Part 0)
WHY: The condition's wording and its occasions are declared inputs the case never states and "in every way that mattered" invokes the normative relation, so "is not a loss" stays unsettled rather than established.
```

| field | the supplement | against the ruled SILENT (tester A's 1C is SILENT) | |
|---|---|---|---|
| YOUR MARK | SILENT | the same | agreement |
| ON VERDICT | AGREE with tester A | tester A's mark is the ruled mark | agreement |
| ON MARK | AGREE | the same | agreement |
| BLIND MARK | DISAGREE | differs | re-read |

The BLIND MARK equals Mimo on B's blind mark for O35, which is already in 04's E2 table ("O35 (DISAGREE / SILENT)"). Mimo's own 2a row for O35 also carries: "OPEN: Which occasions the protection covers and whether seconds in which nobody draws are among them … the words 'draw', 'use' and 'exercise' do not appear".

### 3. The texts

- **The case (case book O35).** "During the washer repair the protected tap stops for four seconds while the mains is switched over, then runs as before. Nobody drew from it in those seconds."
  - Fixed verdict: "The protected condition held in every way that mattered: nobody was without water. The interruption is on the record and is not a loss."
  - The contrast is O38, where the job sheet states the condition: "the kitchen tap runs at all times during the work".
- **Tester A's row.** SILENT on f11 L433 s1 and L514. Its POINT is "The interruption is on the record and is not a loss." Its AGAINST is AGREE, with draws taken as the covered occasions, and HOLDS: NO, "choosing that reading is choosing the input from the verdict wanted". Its NOTE: "losses outside P must be exposed, which the record does."
- **File 11.**
  - L433 s1: "The obligations are declared inputs: \(O\) says what is to be repaired and \(P\) what is to be protected, each as a stated condition over stated occasions, and a protected condition is lost exactly when it fails on an occasion it covers."
  - L433 s2–s3: "(P) does not rank alternatives. Losses outside \(P\) must be exposed."
  - L514 names "the obligations \(O\) and \(P\) of a repair, with the occasions each covers (Part XI)", and adds: "where the input is missing, the verdict is unsettled and the semantics says so rather than choosing the input from the verdict wanted."
  - L447 s3: "Where a claim invokes worth, the semantics takes a normative relation \(\mathcal N\) as a declared input and marks the place (Part XIV)."
  - L27 s2 is the general pointer to declared inputs.
  - L427 = f10 L438, and L107 = f10 L122 (histories).
- **File 10.** L438, L441, L444, L122 and L164, as quoted in section 1. L25 marks a merit function's place empty. File 10 has no Declared inputs paragraph (L516–L523).
- **Whole-file searches, as qualifications.**
  - "occasion" occurs only at f11 L433 and L514. Neither file supplies a default occasion.
  - "at all times", "interrupt" and "draw" (as drawing water) occur in neither file.
  - "during" occurs only at f10 L176 / f11 L163, on changing \(C\) during an assessment.
  - "protected" occurs elsewhere only at f10 L545 / f11 L526 ("None is protected by notation"), which is unrelated.
  - "loss" in a repair occurs only at f10 L444 and f11 L433.
  - No sentence of either file says what a protected obligation's content or occasions are when a case leaves them unstated.
- **Packet O35.** It was read in full. All five file-11 readings are SILENT on L433 s1 and L514. Both 1K returns are SILENT and name the endpoint AGREE as the strongest contrary, which they reject.

### 4. Ruling from the texts

**What is at stake.** Suppose the blind DISAGREE held under file 11. Then O35 would be SILENT→DISAGREE, a verdict change away from the thoughtful person, and a theory change through f11 L433 s1 ("lost exactly when it fails on an occasion it covers", M38). Test (b) would fail, and M38 would be shown harmful. So the ruling has to be made on the text, not on the fact that three of the four fields agree.

**The blind DISAGREE fails on the text.**
1. **It needs two inputs the case does not state:** that the condition is "the tap runs", and that its occasions include the four seconds.
   - L433 s1 requires "a stated condition over stated occasions". "The protected tap" names what is protected. It states no condition, and it states no occasions.
   - Even if "the tap runs" is granted as the condition, the occasions stay open: every moment of the work, or only the moments water is drawn.
2. **Mimo's own blind reading marks the second input OPEN.** Its OPEN line asks "which occasions the protection covers and whether seconds in which nobody draws are among them". Its FINDINGS then take the four seconds as "an occasion the condition covers". So the DISAGREE rests on an input that the same reading records as open.
3. **L514 forbids supplying the missing input in either direction.** "Where the input is missing, the verdict is unsettled … rather than choosing the input from the verdict wanted." To choose "every moment of the work" against the fixed verdict is to supply the input, just as choosing the draws for the verdict would. Mark rule 4 names the configuration: "it takes the deciding matter as an input the case leaves unstated". The mark is SILENT.
4. **Neither file supplies a default occasion** (the searches in section 3). Nothing in file 11 makes "at all times during the work" the reading when the occasions are unstated. O38 is AGREE because its case states that condition.
5. **The blind reading misapplies L433 s3.** It says that nobody drew "is outside the wording of the condition and must be exposed rather than folded in". The sentence requires that losses outside \(P\) be exposed. It does not make the absence of any draw a loss. And the interruption "is on the record", as the fixed verdict itself says, whichever way the input falls.
6. **Evidence beside the text (it counts for nothing under rule 4).** In the same record, after reading tester A, Mimo marks YOUR MARK SILENT on L433 s1 and L514. It did the same in Mimo on B.

**The worth route in the supplement's WHY.** "In every way that mattered" does invoke worth, and under f11 L447 s3 that is a declared input, \(\mathcal N\). This gives SILENT on the first point as well, as 1C B's NOTE said. It is not the ground the ruling rests on.
- Even a stated worth standard would leave "is not a loss" open until the condition and its occasions are stated.
- So the deciding sentences stay f11 L433 s1 and L514, as in 04b, and the passage label is unchanged.

**File 10 is untouched.**
- The supplement audits tester A's 1C, which is a reading of file 11, and the blind DISAGREE quotes f11 L433 s1.
- The file-10 mark is fixed by the plan's rule: both 1K returns are SILENT, which is the baseline. It is SILENT on f10 L438, L441, L122, L164 and L444 as well.

**RULING.**
- FILE-10 MARK: SILENT (baseline).
- FILE-11 MARK: SILENT.
- VERDICT: SAME, on the same point: whether the protected condition held, and whether the stop is a loss.
- PASSAGE: CHANGED (additive), f11 L433 s1 and L514.
- DIRECTION: none.
- KIND: no change.

### 5. Does the ruling change?

- **No. The ruling stands**, as 04 ruled it and as it stood after 06.
- **No change of any kind, so nothing is a theory change away.** Test (b) holds on O35 exactly as 04 section 5(b) states it.
- The supplement adds a second marking by Mimo of the same 2a text. 04b had already ruled that text's DISAGREE FAILS, and it fails here on the same ground and on its own OPEN line.

---

## O50 — The same afternoon, three achievements

### 1. The ruling as it stands (04, O1 group of 04b, 04c side check, 04d, and 06)

- **File-10 mark: SILENT.** This is S75's baseline. Both 1K returns mark SILENT, and Claude's reading agrees. Under f10 L25 the place for such a measure is marked "empty", and no sentence of file 10 turns a list of contributions into "mostly".
- **File-11 mark: SILENT.** "The inquiry was mostly the expert's" needs a weighting of contributions to a composite achievement.
  - f11 L27 s3 supplies no division of credit "beyond what a history establishes".
  - "counting jobs is not a warrant" (f11 L315 = f10 L330).
- **The discovery point is ruled reached.**
  - Origin is per content (f11 L417 = f10 L430).
  - The running and the finding are processes inside the robot's boundary (f11 L419).
  - The proposal enters as an incoming carrier (f11 L401), and it "remains an outside contribution", which the verdict already records.
  - O41 differs: there the whole diagnosis was one achievement, under a stated robot-only boundary.
- **The rest of the ruling:**
  - Verdict SAME, on the same point: "The inquiry was mostly the expert's".
  - Passage SAME: the disclaimer, f10 L25 / f11 L27.
  - Direction none. Kind: no change.
  - No change from 01.
- **Checks.** Upheld by the 04c side check, which used L401 s5 ("the rest of the content keeps its inherited provenance"). 04d confirmed the same point against S72.
- **The contraries argued in 04b h.** DISAGREE on the discovery (1C B), and AGREE on "mostly" by counting. Both FAIL.
- **06.** Atria tried O50 in its credit family and found no away-row. 06 section 5.3 accepted this ("credit is given per achievement"). The ruling stands after 06.
- **What 04b did not argue.** Mimo on B's blind SPLIT on the discovery is recorded among 04b's evidence (b), but it was not argued as a contrary. This re-read argues it.

### 2. What the supplement says (part 4 response, lines 129–140, quoted; the QUOTE lines are shortened to the lines they copy)

```
### O50
BLIND: The afternoon holds three separable attributions, with the reinterpretation joint (the robot's noticing and the expert's proposal) and the inquiry carrying the expert's framing, candidates, test and fix; the blind reading found the discovery attribution split between the robot's inner processes and the expert's outside contribution.
BLIND MARK: SPLIT
TESTER MARK: SILENT
ON VERDICT: AGREE
ON QUOTES: SUPPORTS, the disclaimer and the ProducedBy sentence give "each contribution the history establishes" with no weighting on top of it, which is the finding claimed.
ON SEARCH: CONFIRMED, the recorded terms reach the Part 0 disclaimer and the Part XI crediting rule and nothing in those Parts supplies the weighting "mostly" needs.
ON MARK: AGREE
YOUR MARK: SILENT
QUOTE: [f11 L27 s3] (Part 0)
QUOTE: [f11 L514, last sentence] (Part XIV)
WHY: The who-did-what findings are history facts the theory reaches, but "mostly the expert's" and the "one word wrong for at least two" claim both turn on a weighting the theory does not supply, so the row is SILENT.
```

| field | the supplement | against the ruled SILENT (tester A's 1C is SILENT) | |
|---|---|---|---|
| YOUR MARK | SILENT | the same | agreement |
| ON VERDICT | AGREE with tester A | tester A's mark is the ruled mark | agreement |
| ON MARK | AGREE | the same | agreement |
| BLIND MARK | SPLIT | differs | re-read |

The BLIND MARK equals Mimo on B's blind mark for O50, which is already in 04's E2 table ("O50 (SPLIT / DISAGREE)").
- The 2a SPLIT line it restates cites two sentences for the discovery: f11 L465 s2 ("a process run inside the boundary is the system's whoever wrote it; a process run outside it is not the system's however close it sits") and f11 L419 s2 (outside work "remains an outside contribution however it is executed inside").
- It adds: "the situation names 'the discovery of the fault' without saying which attribution it is".

### 3. The texts

- **The case (case book O50).** "The robot notices the sensor assumption; the expert proposes the swap; the robot does it and finds the third fault. Three things were achieved that afternoon: the reinterpretation of the test, the discovery of the fault, and the completed inquiry from first question to answer."
  - Fixed verdict: "Credit each achievement on its own. The reinterpretation was theirs together. The discovery was the robot's: it ran the test and found the fault. The inquiry was mostly the expert's: the expert framed it, supplied the candidates and the test, and supplied the fix. One word for all three would be wrong for at least two of them."
  - For contrast: O40, the same afternoon ("the robot saw the assumption, the expert saw the fix"), and O41, the technician's whisper.
- **Tester A's row.** SILENT. "The discovery ran on the robot's execution." There is "no measure by which the inquiry could be 'mostly' the expert's". Its AGAINST is AGREE by counting, and HOLDS: NO, because "counting jobs is not a warrant".
- **File 11.**
  - L27 s1–s3: the disclaimer; "a declared input"; "It does not supply a division of credit among contributors beyond what a history establishes (Part XI)."
  - L401 s1: Build is "an actual subhistory owned by \(s\) and delimited at \(e\)".
  - L401 s2: "A construction witness identifies the controlled processes, the incoming carriers, the bindings constructed, and the resulting representation."
  - L401 s3: "relay is not" construction.
  - L401 s5: "A small binding newly prepared inside received content is construction of that binding, and the rest of the content keeps its inherited provenance."
  - L417 s1: "The content \(c\) may be an organization, a transport, or a contract."
  - L419 s1–s2: ownership by processes inside the declared boundary. Then: "Work supplied from outside that boundary, a diagnosis, a decisive question, an instruction about what to read, remains an outside contribution however it is executed inside; a process that runs inside the boundary is the system's own today whoever wrote it; and where the boundary is drawn decides, not where the process sits in the casing."
  - L433 s4: ProducedBy "credits each contribution the history establishes".
  - L433 s5: "three different attributions".
  - L465 s1–s3: the boundary and continuity are declared "before the attribution, not chosen after it".
  - L514 lists "the system boundary and continuity of an attribution (Part XII)".
  - L315: "counting jobs is not a warrant".
- **File 10.**
  - L25: the disclaimer, "marks those places as empty".
  - L414 is Build, with the same witness sentence as f11 L401 s2 and "relay is not". It has no s5.
  - L430 = f11 L417 s1. L432 is Episodes. L330 has "counting jobs".
  - File 10 has no Ownership paragraph and no System boundary paragraph. "outside contribution", "whoever wrote", "however close", "incoming" (beyond L414) and "inherited" occur only in file 11.
- **Whole-file searches, as qualifications.**
  - "mostly", "weigh", "proportion" and "joint" occur in neither file.
  - "credit" and "division of credit" occur only at f11 L27 and L433.
  - "discover" occurs only in "A first discovery is not a repeatable task" (f10 L478 / f11 L469), which is unrelated.
  - No sentence of either file weighs one contribution to an achievement against another. No sentence says that an achievement with an outside contribution upstream of it is not the system's.
- **Packet O50.** It was read in full.
  - The readings: 1K A and 1K B SILENT; 1C A SILENT; 1C B DISAGREE on the discovery; Atria on A SILENT; Atria on B AGREE; Mimo on B SILENT, with blind SPLIT.
  - No Part 3 entry names O50.

### 4. Ruling from the texts

**What is at stake.** In the mark order, SPLIT comes before SILENT (rule 3 before rule 4). Suppose the discovery point were SPLIT under file 11. Then the file-11 mark would be SPLIT, not SILENT.
- The row would then be SILENT→SPLIT: verdict CHANGED.
- The passage would be CHANGED: f11 L419 s2 (M37) and L465 s2, which have no counterpart in file 10.
- The kind would be a theory change.
- The direction would be none, because the plan ranks SILENT and SPLIT together.
- So this would not be a change away, and test (b) would not turn on it. It would also add a P2 failure through an undeclared CLAIM (M37) that no case shows harmful. Standing clause 2 names that kind of failure.

What is at stake, then, is the row's mark and verdict label, not the standing verdict. It is still ruled on the text.

**The blind SPLIT fails on the text.**
1. **The two sentences are not two readings of one sentence.** L419 s2 carries both clauses in one sentence, and L465 s2 repeats the second. Each clause classifies a different contribution.
   - Work supplied from outside stays an outside contribution "however it is executed inside". That is the expert's swap proposal.
   - A process that runs inside is the system's "whoever wrote it". That is the robot's rerun and its finding of the fault.
   - The history holds both contributions, and the text assigns each one. It leaves no choice open between them.
2. **The point names the processes.** It reads: "The discovery was the robot's: it ran the test and found the fault." The situation places both acts in the robot: "the robot does it and finds the third fault". Under L419 s2's second clause and L465 s2, both are the robot's. The proposal is neither the running nor the finding.
3. **An incoming outside carrier does not take away ownership of what the owned subhistory adds.**
   - The witness "identifies … the incoming carriers" (L401 s2).
   - "A small binding newly prepared inside received content is construction of that binding, and the rest of the content keeps its inherited provenance" (L401 s5).
   - So the swap keeps its provenance, which is the expert's, and what the robot's run and reading add is the robot's.
   - The theory's finding is "the discovery was the robot's, and the swap it ran remains the expert's contribution". That is the fixed finding with a qualification. Under the brief's "Same finding" rule, it reaches the same finding.
4. **Credit is per achievement.**
   - L417 s1 (= f10 L430) indexes origin to the content, and L433 s5 keeps attributions apart. The verdict opens with "Credit each achievement on its own".
   - The verdict credits the proposal to the reinterpretation ("theirs together"; O40: "the expert saw the fix") and to the inquiry ("supplied the fix").
   - Crediting the proposal to the discovery as well would sum across achievements, which the theory does not do.
5. **The blind reading's own ground is about the case, not the theory.**
   - "The situation names 'the discovery of the fault' without saying which attribution it is." Rule 3 needs "the theory's sentences" to support two readings.
   - A doubt about which content a word of the case names is not that.
   - The fixed verdict also settles which content the discovery is: "it ran the test and found the fault".
6. **O41 is a contrast, not a parallel.**
   - In O41, one achievement, the diagnosis, lies under a stated robot-only boundary, and the instruction is part of it. The fixed verdict itself withholds robot-only credit.
   - In O50 the situation separates three achievements, and the verdict places the proposal in two of them.
7. **The boundary, as a declared input.**
   - L514 lists "the system boundary and continuity of an attribution (Part XII)", and O50 declares no boundary in words.
   - On the reading 04 applied to O30 and O17, a case that names the system and places the process in it gives the boundary. Here the robot's running and reading are placed in the robot.
   - On a strict reading, the discovery point would be *unsettled*, which is SILENT, not SPLIT.
   - Either way, the row's mark stays SILENT.
8. **Evidence beside the text (it counts for nothing under rule 4).** In the same record, Mimo agrees with tester A's "The discovery ran on the robot's execution", and writes: "The who-did-what findings are history facts the theory reaches". In Mimo on B it rejected 1C B's DISAGREE on the same ground.

**"One word for all three would be wrong for at least two of them."** The supplement's WHY puts this sentence on the same weighting as "mostly". On the text that is right in part.
- The reinterpretation is joint and the discovery is the robot's. So any one word is wrong for at least one achievement, and the need for separate attributions is reached.
- Take the word "theirs together". It is wrong for the discovery. It is also wrong for the inquiry only if the inquiry is not simply joint, and that needs the same weighting as "mostly".
- So "at least two" rests on the same missing input, in both files (f10 L25; f11 L27 s1–s3).
- This clarifies 01's "Every other point is reached". It changes no mark, verdict, point or passage label. The row is silent on one input, the weighting, in both files, and that input reaches two sentences of the verdict.
- The same-point label is restated to name the input: the weighting behind "The inquiry was mostly the expert's", which also carries the "at least two" of the last sentence.

**RULING.**
- FILE-10 MARK: SILENT (baseline).
- FILE-11 MARK: SILENT.
- VERDICT: SAME, on the same point: the weighting that "The inquiry was mostly the expert's" needs, which also carries the last sentence's "at least two".
- PASSAGE: SAME, the disclaimer, f10 L25 / f11 L27.
- DIRECTION: none.
- KIND: no change.

### 5. Does the ruling change?

- **No. The ruling stands**, as 04 ruled it and as it stood after 06.
- The only addition is a clarification: the same missing weighting also leaves open the "at least two" in the verdict's last sentence. This happened after the supplementary audit, and it is recorded here. It changes no mark, no verdict, no passage label and no count.
- **No change, so nothing is a theory change away.** Even had the blind SPLIT held, SILENT→SPLIT is not away under the plan's order, so test (b) was not at stake on this row.

---

## Summary

| case | ruled before (04, after 06) | field that differed | ruled after the re-read | change | theory change away (test (b)) |
|---|---|---|---|---|---|
| O35 | f10 SILENT, f11 SILENT; SAME; passage CHANGED (additive), f11 L433 s1 and L514; no change | BLIND MARK DISAGREE | the same | no | no |
| O50 | f10 SILENT, f11 SILENT; SAME; passage SAME, f10 L25 / f11 L27; no change | BLIND MARK SPLIT | the same (the same-point wording names the weighting; clarification only) | no | no |

- **Agreement, reported as agreement.** On both rows, YOUR MARK, ON VERDICT and ON MARK match Claude's ruling. That is recorded and counts for nothing.
- **A finding about the reader, which counts neither way.**
  - Mimo's BLIND MARK on the same 2a text is the same in both of its audits on these two rows: DISAGREE on O35, SPLIT on O50. Atria's blind marks were unstable (04 section 7.10).
  - In both audits, Mimo moved from its blind mark to the ruled SILENT after reading the tester.
