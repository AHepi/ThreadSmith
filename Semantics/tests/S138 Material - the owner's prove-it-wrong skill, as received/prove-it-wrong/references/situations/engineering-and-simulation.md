# Engineering, physical tests and simulation

Use this file for load and endurance tests, sensor and estimator claims, control systems, simulation results, and "the model matches the experiment".

## Typical claims

- "The part survives 10,000 cycles."
- "The estimator is accurate."
- "The simulation shows X cannot happen."
- "The controller is stable."

## Where the falsifiers usually are

- **Q2 Supplied answer: checking a model against itself.** An estimator scored against the simulator variable it was computed from. A controller tuned and tested on the same model. A fit judged on its own fitting data. The falsifier: an independent measurement, or a model the estimator was not built from.
- **Q1 Scope: conditions outside the test rig.** Temperature, humidity, vibration, wear, manufacturing spread, real noise against simulated noise. Name which could matter, and test the worst plausible one.
- **Q5 Worst single case: the weakest unit.** "Survives 10,000 cycles" on an average of five parts says nothing about the weakest part in production. Report each unit, and the spread.
- **Q4 Same by construction: null controls in chaotic systems.** In collisions and other chaotic dynamics, a tiny change grows. Measure the null floor before calling a difference real. Check that the instrument (renderer, sensor, sampling) can resolve what is claimed.
- **Q8 Unseen changes: regimes the model was not built for.** Contact, saturation, slip, resonance, or a start that is not at rest. A model fitted in one regime says nothing reliable outside it.
- **Q6 Premise match: idealised parts.** A perfect motor, a rigid mount, noiseless sensing. Replace the idealised part with a realistic one and see whether the result holds.
- **Q12 Consequences: what else the design must survive.** Fatigue, heat, failure modes when a sensor drops out.
- **Q13 What is counted: the sample's origin.** A pilot batch or hand-picked units for quality control, rather than the production line. A measurement boundary that leaves out upstream or downstream effects, such as a carbon figure for the factory alone.

## Mini example

**Claim:** "The speed estimator is perfect: zero error on 1,000 simulated runs."

**Missing:**
- The zero is guaranteed, because the estimator differences the simulator's own positions (Q2).
- Real sensors add noise and jitter (Q1, Q8).
- No rival filter was compared (Q3).

**Next test:** add realistic noise and sampling jitter, and compare with a filtered estimator against an independent speed reference.
