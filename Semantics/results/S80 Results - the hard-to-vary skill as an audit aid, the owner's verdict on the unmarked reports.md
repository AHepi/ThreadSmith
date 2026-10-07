# S80 Results - the hard-to-vary skill as an audit aid, the owner's verdict on the unmarked reports

23 September 2026. Plan: `tests/S80 Plan - third version, cut to a quick verdict.md`. Outputs: `results/S80 Quick verdict - outputs/readers/` (request, response, reasoning and receipt per call).

## The verdict
**The skill is not worth it as an audit aid.** The owner's word (decision S14), given on the preview below: "I think we have all the results we need. The skill isn't worth it." The round stops here: the reports are not marked, the sealed list and addendum stay sealed outside the repository, and the predictions Q1 to Q9 are not read. Mimo's three runs still in flight are kept going and stored as they arrive; they are not read into this verdict.

## What the verdict was given on
A program's count of which planted errors each report *mentions* (a pattern search per error; a mention is not a finding: the marker pass that would say whether the report says correctly what is wrong was not run). Fifteen reports were in: DeepSeek 9 of 9, Atria 6 of 9, Mimo 0 of 9. Mean mentions per report; HV the four errors of the skill's own kind, GEN the four ordinary ones:

| reader | nothing: HV / GEN | placebo: HV / GEN | skill: HV / GEN |
|---|---|---|---|
| DeepSeek (3, 3, 3) | 3.3 / 1.3 | 3.7 / 1.7 | 3.3 / 2.3 |
| Atria (1, 2, 3) | 2 / 1 | 2.5 / 2.5 | 3 / 3.7 |

Report lengths were alike across conditions (about 700 to 1,800 words).

## How Claude reads it
On DeepSeek the skill adds nothing on its own kind of error: the reader with no method at all already mentions the vacuous condition, the collapsed distinction and the protecting sentence about as often. On Atria the skill cells lead, on cells of one to three reports, inside the noise the plan named. Nothing here shows the skill finding what a reader without it misses; the placebo, a plain reviewing method of the same length, does as well where it can be compared. That agrees with the owner's verdict, and it is weaker evidence than a marked table would be: the counts are mentions, three repetitions at most, one document, and the plants are the skill's author's own.

## What follows
- The skill is not handed to readers in this project's audits from here; the other model already gets file 24 in its place, and nothing replaces it for API models (they get the task alone).
- The HV Skill project's own record is outside this folder and is not edited (decision S12); whether the skill is kept there is that project's matter.
- The second version of the plan, the placebo, the tools and the seeded document stay in `tests/` and `tools/` as the apparatus of a round that can be picked up if a case ever calls for it.

## Not tested
Everything the plan's three versions list; and in this cut, the marking itself.
