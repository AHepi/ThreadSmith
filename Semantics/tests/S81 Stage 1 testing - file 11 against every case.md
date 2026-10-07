# S81 Stage 1 testing - file 11 against every case

*Frozen before the run, as its plan is (`S81 Plan - file 11 against every case, rebuilt with the S78 repairs, for two API models.md`). Written by Claude (an Opus 5.5 subagent, for the orchestrator) on 23 September 2026. This file holds two paste parts, each between a BEGIN and an END marker, which `tools/s81_build.py` lifts out word for word and joins to the texts named in the plan. Everything outside the markers is for the orchestrator and travels in no call.*

Two briefs:
- **Brief 1-cases** is the testing brief proper. It goes out in two arms that share it word for word: arm **1C**, joined to file 11 (with its revision note withheld) and the case book; and arm **1K**, the control, joined to file 10 and the same case book. Neither arm names a version, a file number, an earlier round or an expected result, so neither agent can tell which arm it is in or that the other exists.
- **Brief 1-texts** is the difference test that S76 Stage 1 ran as its Part 2: file 10 and file 11 side by side, as Text A and Text B, with the revision note withheld, so the claim count is found and not handed over.

Each brief ends its return with the line `END OF REPORT`, which `tools/s80_call.py` requires before it accepts a return.

<!-- BRIEF 1-cases BEGIN -->
# Reading a theory against fifty-two cases

Below this instruction are two things: a theory of explanation, in the section headed THE THEORY, and fifty-two short cases, in the section headed THE CASES. Each case has a situation and a thoughtful person's verdict. Your task: read the theory as it stands and say, case by case, what verdict the theory gives, which of its sentences give it, and how that verdict compares with the thoughtful person's. The theory's own sentences are your authority. Keep each situation and each verdict exactly as written.

## Words used here, fixed before you read the cases

- **Fixed verdict.** The thoughtful person's verdict printed with each case. It is the reference you compare against.
- **Point.** Each sentence of the fixed verdict that states a finding: who did what, what counts as what, what is present or what is lacking.
- **The theory's verdict.** What the theory, read as it stands, finds on each point, by its own definitions and conditions. Where the theory leaves a word undefined, read it in its ordinary sense.
- **Same finding.** A verdict of the theory that reaches the fixed verdict's finding and adds a qualification, a limit or a more exact wording reaches the same finding. Write the addition under NOTE. A mark records findings; differences of wording belong in NOTE.
- **Marks.** Give each case exactly one mark. Take the first rule, in this order, that fits:
  1. **CASE DISPUTED**: the situation itself, read in ordinary terms before any theory, decides a point against the fixed verdict. Name what in the situation, and in the situation alone, decides it, and give the theory's verdict as well.
  2. **DISAGREE**: on at least one point, the theory's verdict reaches a different finding from the fixed verdict. Name that point and quote the sentence of the theory that gives the different finding.
  3. **SPLIT**: on at least one point, the theory's sentences support two readings that reach different findings, and the text leaves the choice between them open. Give both readings, each with its sentence.
  4. **SILENT**: on at least one point, the theory leaves the finding open, because it takes the deciding matter as an input the case leaves unstated, or because its sentences stop short of deciding it. Name the point and record your search: the Parts you read for it and the words you looked for.
  5. **AGREE**: on every point, the theory's verdict reaches the same finding as the fixed verdict.

## How to work each case

Work the cases in order, O1 to O52. For each:
1. Read the situation. Write EXPECT first: the mark you expect and the Part of the theory you expect to decide the case.
2. Read the theory for the case. Write its verdict, point by point, with the sentences it rests on.
3. Set the theory's verdict beside the fixed verdict and choose the mark by the rules above.
4. Write the strongest reading of the theory that would give a different mark, with the sentence that reading uses, and say whether that reading holds against the text as well as yours does.

## Quotations

Copy each quoted sentence from THE THEORY exactly, character for character, including any mathematical notation, and give its Part and the nearest heading above it as they stand in the text. Every quotation is checked against the text by program. Quote whole sentences, prefer sentences in words, and give one to three quotations per case.

## The identifiers

The identifiers O1 to O52 name the cases. The theory has labels of its own in brackets, such as (O), (O1), (E) and (T2), and those name parts of the theory. Write a case as O12, and a label of the theory as it appears in the text, brackets included.

## What to return

Plain text, in exactly this form. First, one record per case, O1 to O52, each opening with its heading line and holding these labelled lines, each label at the start of its own line:

```
### O1
EXPECT: <mark> ; <Part>
VERDICT: <the theory's verdict on this case, in two to five sentences>
QUOTE: "<a sentence copied exactly>" (Part <number> - <heading>)
QUOTE: <up to three QUOTE lines in all>
MARK: <one of AGREE, DISAGREE, SPLIT, SILENT, CASE DISPUTED>
POINT: <for AGREE, the word ALL; for every other mark, the sentence of the fixed verdict at issue, quoted>
WHY: <one sentence: how the quoted sentences give this mark>
SEARCH: <for SILENT, the Parts read and the words looked for; for every other mark, the word NONE>
AGAINST: <the strongest reading that would give a different mark, with the sentence it uses; for CASE DISPUTED, what in the situation alone decides the point>
HOLDS: <YES or NO>, <one clause saying why>
NOTE: <any qualification, limit or added wording the theory brings, or the word NONE>
```

Then these three sections, in this order. Each opens with its count, and the count is stated even when it is zero.

```
## Counts
AGREE: <n> - <case identifiers>
DISAGREE: <n> - <case identifiers>
SPLIT: <n> - <case identifiers>
SILENT: <n> - <case identifiers>
CASE DISPUTED: <n> - <case identifiers>

## Sentences of the theory that give a verdict different from a fixed verdict
COUNT: <n>
- "<the sentence>" (Part - heading) - cases: <identifiers>

## Noticed beyond the cases
COUNT: <n>
- <one line each: a sentence of the theory that seems to you wrong, unclear, or in tension with another of its sentences, or a reference in the theory that points to the wrong place; quote the sentence and give its Part>
```

Close your reply with this line, on its own:
END OF REPORT
<!-- BRIEF 1-cases END -->

<!-- BRIEF 1-texts BEGIN -->
# Two texts of one theory: every difference in what they claim

Below this instruction are two texts of one theory, in the sections headed TEXT A and TEXT B. Text B is a rewrite of Text A. Your task: find every place where the two texts differ in what they claim, and mark each one.

## Words used here, fixed before you read the texts

- **CLAIM**: at this place a reader can conclude, from one text, something the other text leaves unconcluded. Text B asserts something Text A leaves unasserted; or B drops, narrows, widens or qualifies something A asserts; or B adds or removes a requirement, a condition, an exception, a quantifier, or an input the theory takes from outside itself.
- **WORDING**: at this place both texts assert the same thing, in different words, order or detail, and every conclusion a reader can draw from one, the reader can draw from the other.
- **ORDER**: the same sentence, moved.
- Where a place could take either CLAIM or WORDING, mark it CLAIM and give the reason under WHY; the choice between them is settled later by a reader holding both texts.

## How to work

Read both texts whole. Then go Part by Part (both texts run from Part 0 to Part XVI), setting the sentences of A beside those of B. Copy every quoted sentence exactly, character for character, including any mathematical notation; every quotation is checked against the texts by program.

## What to return

Plain text, in exactly this form. First, one record per place, numbered D1, D2 and onward, each label at the start of its own line:

```
### D1
PART: <Part number and heading in B, with A's heading as well where it differs>
A: "<the sentence or sentences of A, copied exactly>", or the word NONE where the place is in B alone
B: "<the sentence or sentences of B, copied exactly>", or the word DROPPED where the place is in A alone
MARK: <CLAIM or WORDING>
WHY: <one sentence: for CLAIM, what a reader concludes from one text and leaves unconcluded from the other; for WORDING, why both say the same>
TEST: <for CLAIM, a short situation on which the two texts give different answers, in one or two sentences; for WORDING, the word NONE>
```

Give a record for every CLAIM place. Give a WORDING record for each place whose sentence carries a condition, a requirement, a quantifier, an input the theory takes from outside itself, or a verdict, since those are the places where a rewording could carry a change; up to forty WORDING records, the closest calls first.

Then these sections, in this order, each opening with its count, stated even when it is zero:

```
## ORDER
<one line per Part: the Part and the number of sentences moved>

## Cross-references in Text B
CHECKED: <the number of references in B to a Part, to a numbered derivation or to a bracketed label>
WRONG: <n>
- "<the sentence holding the reference>" (Part - heading) - points to <where it points>; the matter is at <where it is>

## Counts
CLAIM: <n> - <record numbers>
WORDING: <n>

## Noticed beyond the differences
COUNT: <n>
- <one line each: a sentence of either text that seems to you wrong, unclear, or in tension with another; quote it and name its text and Part>
```

Close your reply with this line, on its own:
END OF REPORT
<!-- BRIEF 1-texts END -->

---
(Below this line is for the owner and the orchestrator. It travels in no call.)

## What each call is, exactly

| Call | Brief | Joined to | Tag (per model) |
| --- | --- | --- | --- |
| 1C | 1-cases | THE THEORY = file 11 with line 5 (the revision note) and the blank line after it withheld; THE CASES = the case book as written | `s81_1C_<model>` |
| 1K | 1-cases | THE THEORY = file 10 whole; THE CASES = the same case book | `s81_1K_<model>` |
| 1D | 1-texts | TEXT A = file 10 whole; TEXT B = file 11 with the revision note withheld | `s81_1D_<model>` |

Each goes to Atria and to Mimo: six calls. `tools/s81_build.py build` writes each call's exact user text and prints its word count; the counts are in the plan.

## Why the briefs read as they do (the S78 repairs that bear on Stage 1)

- **The answer is out of the brief (A1).** No brief names a version, a file number, a round, an earlier verdict, the prediction or any case expected to move; the build asserts it by program. File 11's revision note names O48 and S75 and states the one-claim count, so it is withheld from every call; the frozen file is not edited, and the build checks the file's md5 before it cuts the note.
- **The marks are defined before the data, by the brief (A4).** Five marks with a fixed order of precedence, and the S72 agent's own rule ("clarification is not itself a changed verdict") written in advance as "Same finding". SAME and CHANGED between the versions are the determiner's columns, defined in the plan and computed from the two arms; the tested agent is asked for neither.
- **SILENT carries a recorded search (A4; S78 reader 1, finding 6).**
- **The agreeing rows are put under pressure (S78 reader 1, finding 5).** EXPECT is written before the case is worked, and every row carries its strongest contrary reading and whether it holds.
- **Two headings the S72 form lacked (A5):** "Sentences of the theory that give a verdict different from a fixed verdict" and "Noticed beyond the cases", each counted even at zero; CASE DISPUTED is a mark with its required field.
- **The claim count is tested, not handed over (S78 item 6, correction to S75 point 2).** Brief 1-texts runs S76's Part 2 with the note withheld and the rule for close calls fixed: CLAIM, reason given, for the determiner to settle.
- **Positive wording (decision 20; A7).** The build scans every brief for negative words and prints each hit; at freeze the count is zero in all five briefs of Stage 1 and Stage 2, apart from the values NONE and NO, which the scan skips as values.

## Traps

- Sending a 1C text whose theory still carries the revision note. The build refuses it.
- Reading a 1K return as a new verdict on file 10 for the record. It is the control arm of this round; where it differs from S72, the determiner reads the row and says so in S81 Results.
- Sending any Stage 2 call before both 1C returns are in. The 2b sample is drawn from them.
