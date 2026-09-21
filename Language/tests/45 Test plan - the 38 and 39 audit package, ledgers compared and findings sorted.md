# 45 Test plan - the 38 and 39 audit package: ledgers compared, findings sorted

Written before translating, running or sorting anything. Not edited afterwards.
Authority document: "Claude Fable Semantics - standalone theory" (file 10). Language under test: file 38, with the translator prompt, file 39. The rigs as they stand in the current bundle (patches 1 to 16 on rig 1, 1 to 3 on rig 2).

## What the package is
Made by the other model, 20 September 2026, and kept unchanged at "results/45 Audit package - the other model on 38 and 39". Checked before writing this plan: its own validator passes (23 files hashed, 384 inputs with no duplicate identifier, 324 receipts, 30 new contrast families, 6 worked translation tables); its copies of 38 and 39 are byte for byte the files in this repository; the 324 inherited inputs are the literary stress test corpus of log 37, unchanged.

What it holds: a manual audit of 38 and 39 (nothing run; no checker; the same assistant wrote and criticised the cases); fifteen findings F01 to F15, each with a source anchor, a case, a strongest defence and a finding; twelve repair families R01 to R12, each attacked with rivals and controls, with rejected variants kept; proposed amendment clauses to 38 (R01 to R11; R12 not adopted); a candidate revision of 39 conditional on those amendments; sixty new texts in thirty contrast families (nine controls); a document-level receipt for every one of the 324 inherited inputs; and six worked translations in 39's five-section form, written by the other model: T02-B and T02-D (the kingfisher pair), L09 (one Hopkins line), N03-A and N03-B (pear colouring, pear contact), N05-A (a denied belief).

What it does not hold: any translation of the eight texts Claude ran at log 37 (T05, T07, T10, T11); any ledger in the rig's `.pl` or `.json` form; any run. So the comparison named as the next step at log 39, "compare ledgers line by line", has no text yet that both translators have done. This plan makes the overlap and freezes what is expected of it.

## The two questions, frozen
1. Given the same text, 38 and 39, do Claude and the other model write the same ledger? Where they differ, is the difference in the text, in the language, or in a reading of 39?
2. Of the fifteen findings, which are conflicts in the wording of 38 and 39, which force a change to the rig or the language, and which are boundaries already declared or give-ups already logged?

## Part A - six ledgers, line by line
Claude translates the six texts the other model translated, under 38 and 39 as they stand (not the candidate 39, not the amendments), in 39's five-section form, and then runs the sameness test from rig 1 on each pair: what both say, what only one says, and where the same fact has a different standing.

**Trap, stated first.** Claude read the other model's six ledgers while checking the package. This is not blind on Claude's side. The predictions below were written after that reading and before translating; they are frozen so that the comparison can still be scored.

| Text | I expect the sameness test to say |
| --- | --- |
| All six | **Same facts, different standing, on every held line.** The other model writes every fixture as TOLD in a named world ("the test paragraphs are treated as narrated fixtures"). Claude's practice since plan 37 writes the fixture itself as the actual ledger (CLAIMED and GIVEN) and uses TOLD only for what a story, report or note *inside* the text says. This is two readings of 39's story instruction, not a difference about the texts. It needs a decision from the owner, not a patch |
| T02-B kingfisher, colour | Both: kingfisher and feathers as things, feathers belong to kingfisher, feathers unharmed; the fire image to the bin. Only theirs: "feathers were the subject of Mara's description". Claude sends "Mara was describing their colour" to the bin, as who-describes-what (38, outside the language). Four both, one only theirs, none only mine |
| T02-D kingfisher, burning | Both: spark STRUCK feathers, reported "not checked" for the verb; feathers burned; caught fire. One line differs in kind: Claude writes "kingfisher BECOMES [on fire], as a result of happening p" with the "as a result of" marked filled in, because "when" is not "because"; the other model keeps it a Fact. Both are legal under 38. This is F04's case, seen |
| L09 Hopkins line | Identical: empty ledger, the whole line in the bin |
| N03-A pear, colouring | Identical: two said (pear is a pear; yellow skin), one filled in (red colouring), both readings of "touched red" in the bin, no TOUCHES |
| N03-B pear, contact | Same happening (painter TOUCHED pear, "not checked" for the verb) and things. Claude sends "The text states the contact" to the bin as a sentence about the text; if the other model kept it as a line, one only theirs |
| N05-A denied belief | Identical: nothing held, the whole attribution in the bin. Two translators reaching the same safe reading is the evidence F02 asks for: 39's line 30 conflicts with 38's exclusion, and both translators followed 38 |

**What would count as failure of the language.** A pair where the same text, under the same rules, gives ledgers that differ in what is said (not in standing, not in a filled-in reading both mark as such), on N03-A or L09, the two easy cases.

**What would count as failure of the comparison.** If the standing difference swamps the sameness test so that it cannot show facts shared: then compare with standing stripped, and say so.

## Part B - the fifteen findings sorted by evidence
Three piles, as at log 33: (1) a conflict or gap in the wording of 38 or 39, fixed by wording, no rig change; (2) a change to the rig or the language, forced by a case, built only after being run on that case; (3) a boundary 38 already declares, or a give-up already in "What each patch gave up", so no change. Sorting is by running the forcing case through the current rig wherever a run can settle it, not by reading the finding.

| Finding | Forcing case | What I expect the current rig to say | Pile I expect |
| --- | --- | --- | --- |
| F01 exception against ALWAYS | N12-A | No run: the translation stops at rule 12, which forbids the line. The rig itself already reports "Exemption from an ALWAYS line" (38, what the checker can say), so only rule 12 and 39's exceptions rule are wrong. Confirmed by reading 38 lines 51 and 128 and 39 line 25 before this plan | 1 |
| F02 embedded content as TOLD | N05-A, N06 | No run needed: Part A. Claude and the other model both bin it | 1: a guard on 39's line 30 |
| F03 a chosen reading is not a resolved source | T39, C03, N27 | Not run. A practice note in 39's "Readings I chose": findings on a chosen reading are conditional on it | 1 |
| F04 a Result needs a producer | N14-A, N15-A | Translate: the Result form cannot be written without inventing a happening; a Fact is used; rig 1 finds nothing; the movement is not checked by the laws. Confirmed at translation. R05a changes what a Result is, which reaches rig 2's laws | 2, forcing case N14-A; control N15-B |
| F05 enabling is not achieving | T21, N17 | Run N17: LETS reported against a stated tendency, no result claimed; nothing false. 38 line 81 already reads conservatively | 3 |
| F06 MAKES with a prior tendency | N16 | Run N16: "the word rests on something nobody stated" or a strength failure, depending on the tendency line. A declared choice, R06, which is the owner's | 3, with a decision |
| F07 endpoint support and the offered route | N19, N20 | Run N19: the circular route is reported as a circle and the conclusion stands by the other route, since "a conclusion stands if any one step for it holds". N20: the conclusion stated first is missed; that is patch 7's logged give-up | N19: 1, wording; N20: 3 |
| F08 the added-lines test is silent | N23-A, N23-B | Run: silent on A, fires on B. Patch 10's logged give-up, rediscovered by someone who never saw the log. Evidence the audit is real | 3 |
| F09 an actual observation in a what-if | N25 | Run: the photograph line is a Fact not tied to the push, so it is not set aside, and the what-if "without the push" answers that the box still moved. Wrongly holds | 2, forcing case N25; the fix must not touch the declared two-cause limit |
| F10 only-ways makes nothing | T26, T27 | Run T27: nothing found, no alternative picked. 38 line 50 already says "denied", not "produced"; say SHOWS | 1 |
| F11 one event, several mentions | N29 | Translate: one happening, two sentence anchors, the repetition noted in the bin. Nothing the rig can see | 3, with a translator note |
| F12 a mentioned goal | N22 | Run: SO THAT answers "cannot tell", as 38 line 89 says; the goal is not used as a premise | 1: write the MENTION form into the examples |
| F13 a clean report is not coverage | T61, T76 | Not run. Wording of the read-back's closing line | 1 |
| F14 a verb with no object | N30 | Translate "the bell rang" as a Fact; rig finds nothing; the verb is not in the happenings. R12 stays optional | 3 |
| F15 a BECAUSE and its exact denial | N18-A, N18-B | Run N18-A: the BECAUSE is reported as a jump (no line MAKES); the NOT [E BECAUSE C] is "fine"; **no contradiction is reported between the two**. On N18-B, correctly nothing. That is a real gap: 38 line 111 promises contradictions among commitments | 2, forcing case N18-A; control N18-B must stay silent |

Expected count: pile 1, seven (F01, F02, F03, F07 in part, F10, F12, F13); pile 2, three (F04, F09, F15); pile 3, five (F05, F06, F08, F11, F14). The count is a prediction, not a target.

**What would count as failure of the audit.** A finding whose forcing case, run on the current rig, already produces the finding 38 promises: then the audit misread 38, and the finding goes to no pile. I expect none, because the four findings I checked against the text before writing this (F01, F02, F04, F15) each rest on a line I could quote.

**What would count as failure of the language.** F15 or F09 confirmed by a run. Either means a ledger of legal lines lets a real clash or a wrong what-if pass, which is what 38 line 17 says cannot be the case for clashes.

## Order of work
1. Part A first, all six, before any rig change. Ledgers as `.json` and `.pl` in rig 1, named T02B, T02D, L09, N03A, N03B, N05A, with `"whose"` naming the other model's corpus and this plan.
2. Then the runs of Part B, on the frozen and patched copies as they stand, every forcing case and every control, logged in `raw_log.txt`.
3. Then the sort. Piles written as a results file, 45. Only after the sort: the first pile-2 change, built on its forcing case, then every earlier ledger rerun and compared report against report, as at log 34.
4. Then the next instruction for the other model: the eight texts of plan 37, so that the comparison runs in both directions; and the pile-1 wording changes as a new language file, numbered when made, superseding 38.

## Not tested by this plan
- The 324 receipts. They are the other model's readings against 38, not runs; a sample of them, chosen by status, is a later plan.
- The candidate 39 as a whole, and R06 and R12, which are the owner's choices.
- The other model's 30 families beyond the forcing cases named above.
- A translator other than Claude and the other model.
- Whether the other model's ledgers, in its table form, can be carried into `.pl` without a reading of my own. Where I have to choose, the line is marked filled in and the choice recorded.

## Traps
- Editing this file after the runs.
- Scoring Part A as agreement when the only difference is TOLD against CLAIMED. That is a decision for the owner, and the sameness test must show it as standing, not as fact.
- Adopting an amendment because its case is convincing. Pile 2 changes are built only after the forcing case has been run on the rig as it stands, and each records what it gives up.
- Reading "384 inputs" as evidence weight. The package itself says it is inventory.
- Treating the other model's "02" as a file of this project. This project has no theory file numbered 02; the package says it did not use it, and its reference is unexplained.
