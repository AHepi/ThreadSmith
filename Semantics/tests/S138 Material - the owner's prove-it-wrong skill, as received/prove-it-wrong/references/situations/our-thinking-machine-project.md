# Our use case: reviewing the thinking-machine project

This section is for one project. It is a machine for language and physical reasoning, built from Pinker's ideas in numbered versions (V1, V2 ... V23) by an engineer agent. The owner is not a programmer. The project keeps:
- frozen versions with source seals;
- a register of claims it cannot make (CANNOT_CLAIMS.md);
- viability reports;
- evaluation contracts written before experiments;
- independent reviews, by Claude and other models, of each version's packet of evidence.

The same missing test conditions kept turning up in those reviews, and in our own reports about them. This file lists them, so they are found before a report goes out, not after.

Use it:
- when reviewing a version's report, a viability report or a proposed next step;
- when writing our own test reports about the project;
- when drafting a request to the engineer.

## 1. Before you start

- **Read the register** (CANNOT_CLAIMS.md) and the version's own list of what it does not establish. Map each new claim onto a register entry. A claim that narrows or overturns an entry must say which entry, and with what evidence.
- **Separate inherited credit from new credit.** A version that composes earlier sealed versions inherits their results. Only what was newly built and newly tested counts for it. Write the inherited parts as claims with the label *inherited, not retested*.
- **List what was supplied by hand.** The project supplies a great deal: law families, hypothesis spaces, candidate programs, endpoint mappings, feature equations, curricula and labels. Put each on the ledger under Q2.

## 2. The conditions that kept going missing

Each row is a forcing question as it shows up in this project, with the case where it was missed.

| Question | How it shows up here | Missed in |
|---|---|---|
| Q1 Scope | "Exact" or "complete" answers hold only inside a supplied family (of laws, regimes, a perception cover). Test scenes outside the family, where the departure is visible in what the system sees and where it is hidden until later. | timing-memory V2: no out-of-family scene; V12 to V13: what happens past the 32-frame memory |
| Q2 Supplied answer | Supplied features can be the physics itself. Two running force totals are momentum and displacement times mass, so the "learning" amounts to about 1 over the mass. Supplied hypothesis spaces can make a "learner" a lookup table. | V2 "persistent memory"; V13's 10 situation types |
| Q3 Rivals | Rival methods: the plan's network contract asks for a rival without the learned part; also run one that uses the same supplied structure with no learning (plain Newton, "keep the same speed", "stays where it is"). Rival explanations: an engine or renderer artefact, a camera position that differs, a parameter the author chose (tremor size). | V2 had no physics rival without learning; our own Newton check used the wrong rival |
| Q4 Same by construction | Ablation arms can collapse: a zeroed readout equals the tie-break rule, and "checks" equals "misses" plus a constant. In a simulator, a null control can be large, because collisions amplify a micrometre change. | V2's five arms were really four; test 2's null control in file 05 |
| Q5 Worst single case | "Never confused" or "always told apart" must hold per speed pair and per frame rate, not per condition summary. Cases where the event fell outside the clip are outside the claim. | file 05, C-002: one pair met after the last frame at 4 frames per second |
| Q6 Premise match | The register's claims have exact premises ("the complete accessible evidence is identical"). A simulation that matches the steady force may still differ in position or command. | file 05 test 1B: the learner's position and press differed |
| Q7 Same question | A score is not understanding. A forecast is not an outcome. "Tells apart" is not "produces". Watch past-tense sentences that state forecasts. | V2 states forecasts as "finally, A was right of B" |
| Q8 Unseen changes | Fitted readouts meet only rest-start, no-contact, fixed-regime worlds. Contact, a start that is not at rest, and varying weight are where they break. | V2's look-alike tests: worse than "stays where it is" when not at rest |
| Q9 Draws and size | Fixed 8-case benchmarks, one draw of five lessons, 672 coordinates from 18 runs. A rerun with the same fingerprint is repeatability, not replication. | V2 |
| Q10 Order of events | Analyses added after a predeclared observer failed (force wobble) must be labelled. A "frozen" contract must predate the run. | file 05 test 1B |
| Q11 Receipts | "Checked by agent N" only after the check has finished and its report is in hand. Review receipts must name a reviewer other than the maker. | our file 06 said "checked" before the check ran |
| Q12 Consequences | A ranker "with no say" still decides which workable option is chosen. A fix that removes a part gives up what the part did. | file 06, first version |
| Q13 What is counted | Pooled coordinates that include a still circle every method gets right. Inherited "unknown" cases left out of a success count. Cases where the event fell outside the clip, counted as support. | V2's 672 coordinates; file 05, C-002 |

## 2b. Reading an engineer's report fairly

- **"Not reported" is not "not done".** The project's reports are long, and the register and earlier versions carry much of the evidence. Before marking something *missing*, search the report and the register. Write "the report does not say" when you cannot find it.
- **Quote the report's own words** for every *reported* row. Its caveats are often already there: "This remains approximate prediction", "not established". Credit them.
- **Check the mechanism's lever.** If a learned part is credited with a gain, check that its output actually changed what was chosen, not only that the final score moved.

## 3. Simulations and renders

Most of the project's evidence comes from simulated worlds: Pymunk, MuJoCo, rendered cameras. Extra falsifiers apply:
- **Engine artefacts.** Soft contacts creep. A teleported body carries nothing by friction. Bounciness near 1 can gain energy. Before trusting a difference, show it is not an engine or renderer artefact: vary the timestep, contact settings and renderer.
- **Exact against realistic observers.** An exact observer sees renderer-level differences no real learner could use. Report a realistic observer too, with random jitter in positions, sizes, camera and light, and say how its result depends on the classifier.
- **The chance band.** Measure what "chance" looks like on real renders of one world against itself. Scores inside that band cannot be called either way.

## 4. Writing the next step for the engineer

- **One request**, written as a test with a pass mark, chosen to overturn the most for the least new building. Example: "run the existing benchmark on three new scenes outside the law family; pass if no confident wrong yes".
- **Say what would count against the version.** Then the engineer can fix the prediction before running.
- **For the owner, write the result in plain words.** Say what was tested, what was not, and what is uncertain, with one next step.

## 5. A mini ledger, for a typical version report

Claims:
- **C1.** The new module improves planning.
- **C2.** Answers are exact.

Falsifiers to look for:
- **For C2:**
  - an out-of-family scene answered with a confident wrong "yes";
  - a seen departure not flagged as "unknown".
- **For C1:**
  - a rival using the supplied structure with no learning matches it;
  - the gain vanishes across lesson draws;
  - two arms are the same by construction;
  - the gain rests on one or two cases.
- **For both:** the inherited results are counted as new credit.
