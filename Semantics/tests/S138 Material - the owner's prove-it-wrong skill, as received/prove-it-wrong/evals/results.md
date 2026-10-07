# Results so far

**Fingerprints.** Every round's cases and marking lists were fingerprinted before its runs:
- round 1: `test_suite/round1_fingerprints.txt`;
- round 2: `G/heldout_fingerprints.txt`;
- round 3: `H3/fingerprints.txt` (copied into `heldout_round3/`);
- round 4: `H4/fingerprints_before_runs.txt` (copied into `heldout_round4/`).

All are in the test-runs zip.

All test agents ran on `claude-sonnet-5`, the model named exactly and recorded from each run's own report. Marking, from round 2 on, was by Opus 5.5 (`claude-opus-5-5`) and GLM (`glm-5.3`), each working blind and apart. Costs are those printed by each run.

## Round 1: practice (8 cases; fitted, so not evidence)

- **What ran:** version 1 of the skill, on `practice_cases/`.
- **Marking:** one agent on `claude-sonnet-5`, against `practice_marking.md`. This was before the owner asked that marking be done by GLM and Opus 5.5.
- **Result:** 27 of 31 MUST items found, 3 partly, 1 missed, no MUST-NOT violated.
- **Why it is not evidence:** the skill's examples were drawn from the same history as these cases.
- **Cost:** $1.67 for the test run.
- **What it showed:**
  - related points merged into one row;
  - sample size checked unevenly;
  - the question table repeating the falsifier table;
  - scope limits wrongly marked *missing*;
  - generic padding.
- **Changed for version 2:**
  - question 13;
  - the three answer rules;
  - the reassuring-words table;
  - the *outside the claim* status;
  - the live-risk rule.

## Round 2: blind cases h1 to h6 (now a development set)

**Setup:**
- **The cases:** written by a separate agent (`claude-sonnet-5`) that had not seen this skill.
- **The marking lists:** audited by GLM. The case-writer then adopted 10 amendments before grading.
- **The comparison:** version 3 of this skill against the hard-to-vary skill, the strongest existing alternative. Same model, same instructions, same cases.

| Marker | hard-to-vary: MUST found / partly / missed | MUST-NOT violated | prove-it-wrong v3: MUST found / partly / missed | MUST-NOT violated |
|---|---|---|---|---|
| Opus 5.5 (24 items) | 16 / 4 / 4 | 0 | 13 / 3 / 8 | 2 (minor) |
| GLM, two halves (24 items) | 18 / 1 / 5 | 0 | 13 / 4 / 7 | 0 |

- **Cases won:** both markers had hard-to-vary better on 4 or 5 of 6. Version 3 won only the simulation case, where it alone caught that a single operating point was tested.
- **Cost of the test runs:**
  - version 3: $5.41, 162 steps, 60 checker runs;
  - hard-to-vary: $1.09, 41 steps.

  Opus marking cost $0.83.

**Why version 3 lost**, as both markers found:
1. **No question for rival explanations.** Q3 asked only for rival methods (baselines). Events at the same time (a pandemic) and spillover between compared groups were missed. The answer even marked Q3 "does not apply" because a comparison group existed.
2. **The fixed table invited agreement.** *Covered* and *reported* were ticked "as reported". Twice a fact the case did not give was filled in ("fixed in advance", "all 412 followed").
3. **Effort went into form.** There were ten checker runs per answer, mostly to make every question answer every claim.

**Contamination note:** before the round ran, the skill's author saw a few details of these cases in summaries: their six fields, which case was well tested, and a few words from the marking amendments. Suggestions that matched those details were held back until after the round.

**Changed for version 4:**
- Q3 becomes "Rivals", asking first for rival explanations;
- "think first, then classify";
- "quote it, or it is missing", enforced for *reported* rows;
- Q1 asks about time spans and operating points;
- the checker is run at most three times, and warnings are advice;
- an empty claims cell means all;
- fewer false warnings.

## Round 3: fresh blind cases n1 to n6

**Setup:**
- **The cases and marking lists:** written by GLM, avoiding every earlier topic, and audited by Opus 5.5 before any run.
- **The comparison:** version 4 against hard-to-vary, both on `claude-sonnet-5`.
- **Marking:** blind, by Opus 5.5 and GLM.

**Results:**

| Marker | hard-to-vary: MUST found / partly / missed | MUST-NOT violated | prove-it-wrong v4: MUST found / partly / missed | MUST-NOT violated | Cases won (v4 : hard-to-vary) |
|---|---|---|---|---|---|
| Opus 5.5 (24 items) | 14 / 6 / 4 | 0 | 15 / 5 / 4 | 4 | 4 : 2 |
| GLM, two halves (24 items) | 15 / 5 / 4 | 2 (minor) | 17 / 3 / 4 | 2 (minor) | 5 : 1 |

**Extra credit:** version 4 earned about 9 to 10 points, hard-to-vary about 3 to 5.

**Verdicts:**
- **GLM:** version 4 the stronger set, moderate confidence: "its falsifier-first format forces engagement with the case-decisive tests".
- **Opus:** a slight edge to hard-to-vary, low to moderate confidence, for reliability. On the well-tested case (n3), version 4 stated a fact the case does not give ("self-reported by Sentinel-4's own team") and made acceptance depend on extra checks the claim did not need.

**Both markers:** version 4 still sometimes states a guess as a fact ("crews who knew the assignment", "chose to adopt").

**Cost of the test runs:**
- version 4: $2.18, 79 steps, 25 checker runs;
- hard-to-vary: $0.41, 22 steps.

Marking cost $0.82 (Opus); the Opus audit of the cases cost $0.57.

**What this round shows:**
- **Coverage.** Version 4 moved from clearly behind (round 2) to level, or slightly ahead, at finding missing tests, with much broader extra coverage.
- **Reliability.** It is less careful than hard-to-vary about facts, and it over-reached once on a well-tested claim.
- **Cost.** It takes about five times the usage.
- **Uncertainty.** These are 6 cases and two markers who disagree on the overall winner. Treat the result as "about even, with different strengths", not as a win.

## Version 5

These changes were made after round 3, and are applied and tested in round 4. They take in proposals 1 and 2 of the "Proposed for version 5" list below, which is kept as it was written. Proposal 3 (merging the two tables) was not applied.
- "Test only the claims that were made."
- One row per condition (merge duplicates).
- Write the strongest rival explanation out in full.
- Use the untreated units' trend over the same period.
- Check the mechanism's lever.
- Look for displacement.
- A fact-check pass (Step 7b): unquoted statements become "if" conditions or "not reported"; "not reported" is not "not done".
- A *held if* must be able to overturn the claim, so a well-tested claim gets no new conditions.
- Hard rule 11: state only what the source says.
- Shared "does not apply" rows.
- A clearer section of the project file on reading an engineer's report fairly.

## Round 4: 12 fresh blind cases, three arms

**Setup:**
- **The cases:** 6 written by GLM (g1 to g6), each list audited by Opus 5.5; 6 written by Opus 5.5 (o1 to o6), each list audited by GLM. Two of Opus's cases are in the style of our project's version reports, and one is an agent's self-report.
- **Fingerprints:** cases and lists fingerprinted before the runs. The amendments were adopted before any answer was seen.
- **The arms**, all on `claude-sonnet-5`, answers up to 1,000 words:
  - prove-it-wrong version 5;
  - hard-to-vary;
  - both skills given at once (`both_skills_wrapper_SKILL.md`).
- **Marking:** blind, with the three sets shuffled. Opus 5.5 marked in two sessions of six cases; GLM in four parts of three.

| Marker (53 MUST items) | Arm | Found / partly / missed | MUST-NOT violated | Extra credit | Padding | Cases ranked first |
|---|---|---|---|---|---|---|
| Opus 5.5 | version 5 | 37 / 11 / 5 | 2 (1 minor) | 14 | 22 | 9 (2 tied) |
| Opus 5.5 | hard-to-vary | 38 / 8 / 7 | 6 | 8 | 10 | 3 (2 tied) |
| Opus 5.5 | both | 35 / 11 / 7 | 7 | 9 | 22 | 2 |
| GLM | version 5 | 40 / 9 / 4 | 0 | about 14 | about 37 | 7 (1 tied) |
| GLM | hard-to-vary | 41 / 4 / 8 | 2 | about 9 | about 3 | 2 (1 tied) |
| GLM | both | 41 / 4 / 8 | 7 | about 12 | about 32 | 4 |

GLM counted every "does not apply" row as padding in one of its four parts, and not in the others; that is most of version 5's GLM padding.

**Cost of the test runs:**
- version 5: $14.13, 244 steps, 84 checker runs, 100 edits;
- hard-to-vary: $0.96, 25 steps;
- both: $26.36, 456 steps, 173 checker runs. One advisory warning was chased 112 times.

Marking cost $2.61 (Opus, two sessions). The Opus case writing and audit cost $0.31 and $0.91.

**What this round shows:**
- **Version 5 is the most effective of the three on these 12 cases, by both markers:**
  - the fewest missed items;
  - far fewer stated-but-unreported facts;
  - the most extra credit;
  - the most cases ranked first.
- **The fact-check pass worked.** Version 4's main flaw (stating guesses as facts) dropped to 0 (GLM) and 2 (Opus) violations. Hard-to-vary had 2 and 6.
- **Hard-to-vary stays close on MUST coverage.** It is far cheaper (about 15 times) and pads far less.
- **Giving an agent both skills was worst:** the most invented results (one invented pilot and its result), the most cost, and no gain in coverage.

**Version 5's remaining weaknesses, both markers:**
- it does not explicitly credit a strong design on the well-tested case (g3);
- it uses cousin tests instead of the named one at times;
- it pads, with many "does not apply" rows;
- it missed that an agent's action log was written by the agent itself (o4).

**Process:** it edits row by row and reruns the checker after almost every edit.

**Uncertainty:** 12 cases and two markers. The markers agree on version 5 first for reliability and breadth. They disagree on hard-to-vary against "both" for second place.

## Proposed for version 5 (not applied, not tested)

1. **Guesses as conditions, not facts.** A falsifier or answer that depends on something the source does not say must be written as a condition ("if the crews knew which plots were treated..."), never as a statement. The checker could flag answers that assert unquoted facts in "covered" or "reported" rows; that needs testing for false alarms.
2. **No new conditions on a well-tested claim.** When the main falsifiers were sought and survived, extra checks go under "Routine checks" or "outside the claim". They are not *held if* conditions of acceptance.
3. **Lighter to follow.** Merge the falsifier and question tables for single-claim cases, so that one table carries both; aim for the cost of hard-to-vary.

Test version 5 the same way: fresh cases written and audited by GLM and Opus 5.5, both skills run on claude-sonnet-5, marked blind by both.


## Proposed for version 6 (not applied, not tested)

From round 4's markers:
1. **Credit a strong design out loud.** When randomization, blinding, preregistration or independent measurement are present, name each one and what it rules out, before listing any caveat.
2. **Use the named test, not a cousin.** When a falsifier has an obvious specific form (respondent selection, the original definition rerun at the new threshold), use that form.
3. **Self-written records in agent reports.** When an agent or pipeline reports its own actions, treat its log as a claim (Q11) and ask for an independent trace. Version 5 missed this in o4.
4. **Group the "does not apply" rows by default,** to cut padding.
5. **Work in one pass.** Write the ledger in one go, do the fact-check by rewriting the file once, and run the checker once at the end and once after fixes. Remove the "no falsifier naming it alone" warning, which agents chased.
