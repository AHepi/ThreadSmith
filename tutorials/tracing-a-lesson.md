# Tracing a lesson

**TERM: Lesson.** Something that failed while being made or tested, and how it was fixed. Only failures; each points at evidence.

## Plain-language meaning
A lesson is worth little on its own. Its value is that you can walk from it back to the test that exposed the failure and forward to the file that fixed it.

## Tiny demonstration
Open [Lessons](<../records/Checked reasoning language - Lessons.md>), entry 35:

> The judgement-phrase pass written into file 30 could be passed by any phrase at all: it asked for one change showing "met" and one showing "unmet", and far-apart changes are always available. Shown on first use: zero marks in 32 rows, and both phrases already known to rest on judgement passed. Fix: each pair is held against a near case (file 41).

Walk it back:
1. **The thing that failed:** the Stage B instruction in [30 Next instruction - workflow update and re-audit](<../Semantics/tests/30 Next instruction for the other model - workflow update and re-audit.md>), "Add a judgement-phrase pass".
2. **The evidence:** the other model's Stage B table, 32 rows, zero BORROWED: JUDGEMENT marks. Not in this repository (the owner pasted it into a chat); log 41 in the project story counts the rows by hand and says what it did well and where it failed.
3. **Why it counts as a failure:** rounds 3 and 4 ([27](<../Semantics/tests/27 Next instruction for the other model - round 3, outside cases.md>), [28](<../Semantics/tests/28 Next instruction for the other model - round 4, two change-based clauses.md>)) had already shown that "appropriate to the intended question" and "independently grounded dependency" rest on judgement. A pass that clears both has not measured anything.

Walk it forward:
4. **The fix:** [41 Next instruction - finish Stage B and near cases](<../Semantics/tests/41 Next instruction for the other model - finish Stage B and near cases.md>), Task 2: for each outside case already run, say which change of the pair it matches, and whether that placing agrees with the round's verdict.
5. **What the fix gives up:** "What each patch gave up" in the project story: "Near-case check (audit workflow): bounded to cases that already exist. Gives up: a row that no outside case has strained keeps its far-apart pair unchallenged."
6. **Where it went next:** log 42 considered adding a closeness rule to the skill's poke test and held it out until tested; the near-case routine stays in the workflow, outside the skill.

## Contrast
- **A lesson is not a decision.** Decisions 30 to 34 are the owner's instructions in the owner's words. Lesson 35 is what broke.
- **A lesson is not a synthesis.** It is tied to one authority, one test, one run. If the same pattern shows up across several states, that is for a later synthesis file, which does not exist yet.

## Where to find it
`records/Checked reasoning language - Lessons.md`, numbered. The log entry with the nearest number gives the fuller account.

## Follow the chain
Authority (the audit workflow as updated at Stage A, log 31) -> Test (30, Stage B) -> Raw result (the Stage B table; not in bundle) -> Interpretation (log 41) -> Lesson 35 -> Next authority (41).
