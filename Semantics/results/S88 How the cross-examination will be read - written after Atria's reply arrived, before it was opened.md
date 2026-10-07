# S88: how the cross-examination will be read

*Written by a Claude subagent for the orchestrator on 23 September 2026. Begun at 15:35 UTC and finished at 15:36 UTC. Atria's reply had arrived at 14:24 UTC. No one had opened it. Mimo's reply had not arrived.*

## The fault this repeats

The S88 brief, `tests/S88 Cross-examination - three defects in the theory's own defeat list.md` (sha256 8485bb425b21…), went out with no rule for how the replies would be read. The brief does not say how they will be read, and no rule was committed beside it.

- **The same fault as the effort controls.** Their rule was written at 11:29 UTC, after the Mimo control had already returned. That is recorded in `results/S81 File 11 against every case - outputs/returns/effort controls/READ ME - effort controls, outside the S81 table.md`.
- **Lesson S2.** The rule that decides is written before the run. A rule adopted after the data is recorded as adopted then.
- **S87 got this right.** The S87 brief carries its rule, which "was written and committed before this file was sent".

So this rule was adopted after Atria's reply arrived and before Mimo's reply arrived. Any reading of Atria's reply must carry that fact with it.

## The times, and what had been seen

- **Atria's call started at 14:07:37 UTC.** The runner log `s87_run.log`, in the session scratchpad, has the line "14:07:37 start atria s88_xexam_atria effort medium max_tokens [65536, 65536]".
- **Atria's reply arrived at 14:24 UTC.** The same log has the line "14:24:02 atria s88_xexam_atria ok". This rule does not rely on the word "ok". R1 below checks acceptance from the receipt.
- **This rule was written from 15:35 to 15:36 UTC,** over an hour after the reply arrived. It is committed on its own, before any other file of the S88 returns.
- **Mimo's call, `s88_xexam_mimo`, had not started.** It is in the same run as Atria's call (`tools/s87_jobs - S81 Mimo A parts and S88, as sent.json`), but the runner allows at most three calls per provider in flight at once, across every process. At 15:35 UTC the slot locks showed all three Mimo slots held by parts 1, 2 and 4 of the supplementary S81 audit of tester A. The log has no "start" line for it, and its returns folder has no request file for it.
- **What the writer saw.** Of the S88 returns, the writer saw file names only. The writer also read the S88 brief, the runner log, the runner's slot locks and the runner's code. At 15:35 UTC the folder `results/S88 Cross-examination - three defects - returns/` held these files, listed by name only:
  - `s88_xexam_atria.reasoning.txt`
  - `s88_xexam_atria.receipt.json`
  - `s88_xexam_atria.request.json`
  - `s88_xexam_atria.response.txt`
- **What no one has opened.** No one has opened the response file, the reasoning file or the receipt of Atria's call. They are committed after this rule, unopened.

## The rule

**R1. A failed call supports nothing.** Before a reply is read, its receipt is checked for acceptance. The runner's test is that the call finished with "stop" and that the reply's last line is END OF REPORT. A reply that was not accepted counts neither for nor against any finding or repair, and it is not read for arguments. This covers a reply that failed, was cut off, or never came back. The receipt is the first file of the call that anyone opens.

**R2. Verdict lines and numbered points are evidence, not results.** The brief asks each reply to close its F1, F2 and F3 sections with a verdict line: UPHELD, PARTLY UPHELD or REFUTED. It also asks for numbered points. These lines and points are evidence, not results.
- A verdict line alone changes nothing. Only an argument that survives the check in R3 does.
- Verdicts are not counted across the two replies. Two replies that both say REFUTED are worth no more than the argument that REFUTED rests on.

**R3. Each finding is read in a fixed order, by a fresh Claude reader.** "Fresh" means a reader who did not write the findings. For each of F1, F2 and F3, the reader writes these four steps in order and finishes each step before starting the next.

1. **Claude's current position**, stated first, as it stood when this rule was written. The positions are frozen in this file:
   - **F1.** Derivation 2's component claim is false under its stated assumptions, so Part XV's defeat clause is triggered. The repair narrows the claim to what the proof proves. This is the brief's "Same anchors, one account" wording, a recorded change of claim.
   - **F2.** (T2) omits three hypotheses: matching starts, whose Lipschitz constant, and where ε holds (the brief's h1–h3). This is a drafting omission, fixed by an erratum that restores the predecessor's hypotheses.
   - **F3.** Γ in non-circular dependence is untyped. On the "mechanism only" reading (the brief's R-τ-mech), the fixed verdicts of O33 and O5 flip. Of the brief's two repairs, option B is preferred over option A.
2. **The reply's argument on that finding.** The reader restates it in their own words, under the reply's own point numbers, and quotes the reply's verdict line.
3. **The check against the theory text.** The theory text is the one the S88 brief carries between its BEGIN THEORY TEXT and END THEORY TEXT lines. It is byte for byte file 10 in `authority/` (sha256 4aa2c97ea0cf…), and theory line 1 is its title line, as the brief states. The check has four parts:
   - Every theory line the argument relies on is quoted with its line number.
   - Every quotation in the reply is checked word for word against that text. A misquotation is recorded.
   - Where the argument turns on an instance, each of its stated assumptions is checked against the quoted lines, and its arithmetic is redone.
   - Where the argument turns on a reading of a sentence, the reader says which words fix that reading, or that no words do.
4. **The ruling.** The reader rules UPHELD, NARROWED or WITHDRAWN and gives the reasons.
   - **UPHELD:** the finding stands as stated, including how it is classified (F1 false as stated, F2 a drafting omission, F3 a defect with option B preferred).
   - **NARROWED:** part of the finding stands. The ruling says which part, and the finding is restated to that part.
   - **WITHDRAWN:** the defect does not exist under the theory's stated assumptions. The finding is recorded as withdrawn, with the reason.
   A reply's REFUTED does not make a WITHDRAWN, and a reply's UPHELD does not make an UPHELD. The ruling follows from step 3 alone.

**R4. Further counterexamples.** Each item in a reply's "Further counterexamples" section is checked the same way:
- The reader states the claimed instance and checks it against the quoted theory text (steps 2 and 3 of R3).
- If it holds, it is added as a new finding, F4, F5 and so on in the order it is added. The record names the reply that offered it.
- If it does not hold, it is recorded as not holding, with the reason.
- An item that is really a variant of F1, F2 or F3 is checked under that finding.

**R5. The two replies are read independently.** Atria's reply is read first. Mimo's reply is read later, by the same rule, by a reader who has read neither Atria's reply nor its reading.
- Both readers start from the positions frozen in R3 step 1, not from positions revised after the other reading.
- The two readings are put side by side only after both are written.
- Where they rule differently on one finding, both rulings are recorded. The difference is then resolved in writing, from the theory text, with reasons.

**R6. Changes to the repairs are recorded with their reasons.** The proposed repairs are judged under the same check. They are the F1 wording "Same anchors, one account", the F2 erratum, and F3 option B (with option A as the alternative).
- Any change to a repair is recorded with its reason, the reply that prompted it, and the fact that it came after the cross-examination.
- This includes a change of wording, a change of preferred option, or a change from erratum to change of claim or back.

**R7. The late rule goes with the reading.** Every report of Atria's reply states that this rule was written after the reply arrived and before it was opened. The same statement goes with Mimo's reply only if that reply turns out to have arrived before this file was committed. The runner log gives its time of arrival.
