# S81 Stage 2 audit - check the Stage 1 return

*Frozen before the run, with its plan (`S81 Plan - file 11 against every case, rebuilt with the S78 repairs, for two API models.md`). Written by Claude (an Opus 5.5 subagent, for the orchestrator) on 23 September 2026. Three paste parts, each between a BEGIN and an END marker, lifted out word for word by `tools/s81_build.py`. The marker `{{ROWS}}` in brief 2b is replaced by the build with the list of rows the plan's sampling rule draws; nothing else in a brief is filled in. Everything outside the markers travels in no call.*

Three briefs, each run by both models, each model auditing the other's Stage 1 (the plan says why):
- **Brief 2a, the blind reading.** File 11 (revision note withheld) and the 52 situations with every fixed verdict withheld. The auditor writes what the theory finds on each case before it has seen a fixed verdict or the other model's reading. It shares nothing with Stage 1's returns and may run beside Stage 1.
- **Brief 2b, the open audit.** File 11, the case book with the verdicts, the other model's 1C return whole, and the auditor's own 2a return. The deep audit covers the rows the plan's rule draws after both 1C returns are in; every other row gets a one-line comparison.
- **Brief 2D, the difference audit.** File 10 and file 11 as Text A and Text B, the other model's 1D list as the list under audit, and the auditor's own 1D list as the second list, unlabelled as its own.

<!-- BRIEF 2a BEGIN -->
# Reading a theory against cases, from the situations alone

Below this instruction are two things: a theory of explanation, in the section headed THE THEORY, and fifty-two short cases, in the section headed THE CASES, each with an identifier, a title and a situation. Your task: for each case, say what the theory, read as it stands, finds. Say who did what, what counts as what, what is present or lacking, and what the theory leaves open, each with the sentences of the theory that give it. The theory's own sentences are your authority. Where the theory leaves a word undefined, read it in its ordinary sense. Keep each situation exactly as written.

The identifiers O1 to O52 name the cases. The theory has labels of its own in brackets, such as (O), (O1), (E) and (T2), and those name parts of the theory.

Copy each quoted sentence from THE THEORY exactly, character for character, including any mathematical notation, and give its Part and the nearest heading above it. Every quotation is checked against the text by program. Quote whole sentences, prefer sentences in words, and give one to three quotations per case.

## What to return

Plain text, in exactly this form. One record per case, O1 to O52, each label at the start of its own line:

```
### O1
FINDINGS: <the theory's findings on this case, in two to six sentences, each a finding a reader could check against the situation>
QUOTE: "<a sentence copied exactly>" (Part <number> - <heading>)
QUOTE: <up to three QUOTE lines in all>
OPEN: <each matter the case raises that the theory leaves open, with the Parts read and the words looked for; or the word NONE>
SPLIT: <each matter on which the theory's sentences support two findings and the text leaves the choice between them open, both findings given with their sentences; or the word NONE>
```

Then this section, opening with its count, stated even when it is zero:

```
## Noticed beyond the cases
COUNT: <n>
- <one line each: a sentence of the theory that seems to you wrong, unclear, or in tension with another of its sentences, or a reference in the theory that points to the wrong place; quote the sentence and give its Part>
```

Close your reply with this line, on its own:
END OF REPORT
<!-- BRIEF 2a END -->

<!-- BRIEF 2b BEGIN -->
# Checking another reader's case-by-case reading of a theory

Below this instruction are four sections:
- THE THEORY: a theory of explanation.
- THE CASES: fifty-two cases, each with a situation and a thoughtful person's verdict, which is fixed and stays exactly as written.
- THE READING UNDER AUDIT: another reader's reading of the theory against every case, written with the fixed verdicts in view.
- YOUR BLIND READINGS: your own findings on every case, written earlier from the theory and the situations alone, before you had seen any fixed verdict or the reading under audit.

Your task: audit the reading under audit against the theory's text, row by row, starting each row from your blind reading. The theory's own sentences are your authority. Where the theory leaves a word undefined, read it in its ordinary sense.

## The words the other reader worked under, which you use too

These were fixed for the other reader before it began.

- **Fixed verdict.** The thoughtful person's verdict printed with each case.
- **Point.** Each sentence of the fixed verdict that states a finding: who did what, what counts as what, what is present or what is lacking.
- **Same finding.** A verdict of the theory that reaches the fixed verdict's finding and adds a qualification, a limit or a more exact wording reaches the same finding.
- **Marks**, one per case, the first rule that fits, in this order:
  1. **CASE DISPUTED**: the situation itself, read in ordinary terms before any theory, decides a point against the fixed verdict.
  2. **DISAGREE**: on at least one point, the theory's verdict reaches a different finding from the fixed verdict.
  3. **SPLIT**: on at least one point, the theory's sentences support two readings that reach different findings, and the text leaves the choice between them open.
  4. **SILENT**: on at least one point, the theory leaves the finding open, because it takes the deciding matter as an input the case leaves unstated, or because its sentences stop short of deciding it.
  5. **AGREE**: on every point, the theory's verdict reaches the same finding as the fixed verdict.

## Part 1 - The rows to audit in full

These rows: {{ROWS}}

For each, one record, in this order. Write BLIND and BLIND MARK from your blind reading first, and then open the other reader's row.

```
### O1
BLIND: <your blind reading's findings on this case, in one or two sentences, as YOUR BLIND READINGS gives them>
BLIND MARK: <the mark your blind reading earns against the fixed verdict, by the rules above>
TESTER MARK: <the MARK line of the reading under audit for this case, copied>
ON VERDICT: <AGREE or DISAGREE with the other reader's VERDICT>, <one sentence where DISAGREE>
ON QUOTES: <SUPPORTS, PARTLY or FAILS>, <one sentence: whether the sentences it quotes give the finding it says they give>
ON SEARCH: <for a row the other reader marked SILENT, run its recorded search on the text and write CONFIRMED, or FOUND with the sentence the search missed, quoted; for every other row, the word NONE>
ON MARK: <AGREE or DISAGREE with the other reader's MARK>
YOUR MARK: <your mark after reading both, by the rules above>
QUOTE: "<a sentence of the theory your mark rests on, copied exactly>" (Part <number> - <heading>)
QUOTE: <up to three QUOTE lines in all>
WHY: <one sentence>
```

## Part 2 - Every other row, in one line each

For each case outside the Part 1 list, in order, one line:
`O7: BLIND MARK <mark> ; TESTER MARK <mark> ; SAME or DIFFERENT - <for DIFFERENT, one sentence saying which reading the text supports>`

## Part 3 - What the reading under audit has left unmarked

Each heading opens with its count, stated even when it is zero.

```
## Disagreements the reading under audit left unmarked
COUNT: <n>
- <case>: the other reader marked AGREE; the theory's text gives <a different finding, a split, or leaves the point open> on the point "<the point, quoted>", by "<the sentence of the theory, quoted>" (Part - heading)

## Wrong, and uncorrected anywhere in the theory
COUNT: <n>
- "<a sentence of the theory that gives a verdict different from a fixed verdict>" (Part - heading) - cases: <identifiers> - the sentences you read for a correction: <Parts>

## Cases to rule on
COUNT: <n>
- <case>: <which reading marked it CASE DISPUTED>; what in the situation, and in the situation alone, decides the point: <one sentence>

## The other reader's "Noticed beyond the cases", checked
COUNT: <n>
- <the item, quoted>: <CONFIRMED or DISPUTED>, <one sentence>

## Noticed beyond the cases, your own
COUNT: <n>
- <one line each, the sentence quoted, with its Part>

## Counts
ROWS IN PART 1: <n>
ON VERDICT: AGREE <n> ; DISAGREE <n>
ON QUOTES: SUPPORTS <n> ; PARTLY <n> ; FAILS <n>
ON MARK: AGREE <n> ; DISAGREE <n>
YOUR MARK: AGREE <n> ; DISAGREE <n> ; SPLIT <n> ; SILENT <n> ; CASE DISPUTED <n>
PART 2 DIFFERENT: <n> - <case identifiers>
```

Close your reply with this line, on its own:
END OF REPORT
<!-- BRIEF 2b END -->

<!-- BRIEF 2D BEGIN -->
# Checking two lists of differences between two texts of one theory

Below this instruction are four sections: TEXT A and TEXT B, two texts of one theory, B a rewrite of A; THE LIST UNDER AUDIT, one reader's list of the places where the two texts differ; and THE SECOND LIST, a list of the same places made by a reader working alone. Your task: check both lists against the two texts, and say which differences in what the texts claim survive your check.

## The words both readers worked under, which you use too

- **CLAIM**: at this place a reader can conclude, from one text, something the other text leaves unconcluded. Text B asserts something Text A leaves unasserted; or B drops, narrows, widens or qualifies something A asserts; or B adds or removes a requirement, a condition, an exception, a quantifier, or an input the theory takes from outside itself.
- **WORDING**: at this place both texts assert the same thing, in different words, order or detail, and every conclusion a reader can draw from one, the reader can draw from the other.

Copy every quoted sentence exactly, character for character; every quotation is checked against the texts by program.

## Part 1 - Every CLAIM record on either list

One record each, in this form, each label at the start of its own line:

```
### <AUDIT or SECOND> D7
AT: <Part and heading>
IN THE OTHER LIST: <the other list's record number for the same place, or the word ABSENT>
ON THE QUOTES: <MATCH where both texts carry the quoted sentences as quoted, or DIFFERS with the texts' own wording copied>
ON THE MARK: <AGREE or DISAGREE>, <one sentence>
YOUR MARK: <CLAIM or WORDING>
```

## Part 2 - WORDING records you would mark CLAIM

The same form, for each WORDING record on either list that you would mark CLAIM.

## Part 3 - Differences in claim that both lists missed

```
## Differences in claim that both lists missed
COUNT: <n>
### NEW1
PART: <Part and heading>
A: "<sentence of A, copied exactly>", or the word NONE
B: "<sentence of B, copied exactly>", or the word DROPPED
WHY: <one sentence>
TEST: <a short situation on which the two texts give different answers>
```

## Part 4 - Cross-references

```
## Cross-references
COUNT: <n>
- <each reference in B that either list says points to the wrong place, and each further one you find>: <CONFIRMED or DISPUTED>, <one sentence>
```

## Part 5 - The differences in claim that survive

```
## Surviving differences in claim
COUNT: <n>
- <Part and heading>: <one sentence saying what changes in what is claimed> - <the record numbers on each list>
```

Close your reply with this line, on its own:
END OF REPORT
<!-- BRIEF 2D END -->

---
(Below this line is for the owner and the orchestrator. It travels in no call.)

## What each call is, exactly

| Call | Brief | Joined to | Tag (per auditor) |
| --- | --- | --- | --- |
| 2a | 2a | THE THEORY = file 11, note withheld; THE CASES = the case book with its opening paragraph replaced by one that mentions no verdict and every "Thoughtful person's verdict" line cut | `s81_2a_<auditor>` |
| 2b | 2b, rows filled | THE THEORY = file 11, note withheld; THE CASES = the case book as written; THE READING UNDER AUDIT = the other model's 1C return, exactly as received; YOUR BLIND READINGS = the auditor's own 2a return, exactly as received | `s81_2b_<auditor>` |
| 2D | 2D | TEXT A = file 10; TEXT B = file 11, note withheld; THE LIST UNDER AUDIT = the other model's 1D return; THE SECOND LIST = the auditor's own 1D return | `s81_2D_<auditor>` |
| 2W | 2b, rows filled | as 2b, with the widened rows (the plan's stopping rule) | `s81_2W_<auditor>` |

Atria audits Mimo and Mimo audits Atria. The rows for 2b are drawn by `tools/s81_build.py build2` by the rule the plan fixes, after both 1C and both 1K returns are in; the rule is written only in the plan and the script, and the row list appears only in the 2b brief. The build asserts that no Stage 1 brief and no 2a brief carries a row list.

## How the S78 repairs that bear on Stage 2 are carried

- **Blind first, then open (A2).** In a single-call API setting a column cannot be withheld inside one prompt, so the withholding is by call: 2a is written before the auditor has any fixed verdict or any Stage 1 reading, and 2b opens both. 2a covers all 52 cases, which also measures, within each model, how far seeing the fixed verdict moved the reading (1C beside 2a).
- **The sample is drawn after the return, by a rule the tester never sees (A2, A3).** Mandatory rows, a residual draw keyed to the return's own hash, and a stopping rule that widens the audit (2W), all in the plan.
- **The audit can add (A5).** "Disagreements the reading under audit left unmarked", "Wrong, and uncorrected anywhere in the theory", "Differences in claim that both lists missed", each counted at zero; "Cases to rule on" carries CASE DISPUTED to the determiner.
- **Quotation counts (A6).** Every quotation in S81 is of a text inside the same call, so every one is source-checkable and none is chained. The program checks them all; the auditor is asked only whether a quoted sentence gives the finding (ON QUOTES).
- **Zero counts are asked about (S78 item 12, reader 5).** Every heading states its count, and a count of zero under "Wrong, and uncorrected anywhere in the theory" names the Parts read.

## Traps

- Building 2b before the auditor's own 2a return is in. The build refuses it.
- Labelling the second list in 2D as the auditor's own. It is left unlabelled so that neither list is defended as one's own.
- Reading 2b's YOUR MARK as the result. Claude rules on every row the plan names, from the text.
