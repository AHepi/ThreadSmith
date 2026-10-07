# Testing this skill

This folder holds the skill's test suite, the marking lists, a script to run the suite, and the results so far. Open it when you test or change the skill, never while using it on a real claim.

## What is here

| Item | What it is |
|---|---|
| `practice_cases/` | 8 practice cases: claims with known missing tests, most taken from real reviews |
| `practice_marking.md` | what a good answer to each practice case must raise, and must not do, written before any answer existed |
| `development_round2/` | round 2: 6 cases written by a separate agent that had not seen the skill, the marking lists with dated amendments, both markers' grades, and the key. Now a development set |
| `heldout_round3/` | round 3: 6 fresh cases written by GLM, the marking lists with Opus 5.5's dated amendments, fingerprints taken before any run, both markers' grades, and the key |
| `heldout_round4/` | round 4: 12 fresh cases (6 by GLM, 6 by Opus 5.5, each audited by the other), the amended marking lists, fingerprints, both markers' grades, the key, and the wrapper used for the both-skills arm |
| `run_suite.sh` | runs one skill on one folder of cases, with one named model, in a clean folder |
| `results.md` | what each round found, with costs, and what changed in the skill afterwards |

## Rules for a fair test

These are the skill's own rules, applied to itself:
- **Marking lists come first.** They are written and fingerprinted before any answer exists. Changes to them are dated amendments, made before grading.
- **The agent under test never sees the marking lists.** `run_suite.sh` deletes this `evals/` folder from its copy of the skill.
- **A grader who did not write the answers** scores them. When two skills are compared, the grader sees their answers under neutral names (Set 1, Set 2).
- **Practice cases are not evidence the skill works.** The skill's examples were drawn from the same history, so it is fitted to them. Only the held-out cases, written by someone who had not seen the skill, count.
- **Run a rival.** The comparison is with the strongest available alternative (here, the hard-to-vary skill), on the same cases, with the same model and the same instructions.
- **Name the model exactly** (for example `claude-sonnet-5`, not `sonnet`), and record it from the run's own report.

## How to run a round

```
bash evals/run_suite.sh  path/to/skill  path/to/cases  path/to/work_folder  claude-sonnet-5
```

The answers land in `work_folder/answers/`. The script prints the models used and the cost.

Then give a grader, a separate agent or person:
- the cases;
- the marking list;
- the answers, under neutral names.

Ask it to score each MUST item *found*, *partly* or *missed*, with a quote, and each MUST-NOT *violated* or *not*. It should also list anything the answer got wrong about the case.

## Results

See `results.md`.
