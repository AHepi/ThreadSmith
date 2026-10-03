# Four-stage thinking-machine experiment: final report

## Outcome

The bounded experiment succeeded on its declared four-stage task in a finite,
synthetic visual world. Two confirmation runs, using seeds `20261007` and
`20261011`, each passed all 788 deterministic assessment cases across 33 test conditions and replayed
exactly. The frozen model hash is
`db1a600307e297543d3e37f1ff99956973474b7955685c6772b2ba4f086a0228`; the
aggregate frozen-source hash is
`8cbde548a869fdaccc9b086a3eb324bf6a2887a9e73d24aeb5118b95d4c89f67`.
The [confirmation contract](confirmation_lock.json) pins the development seal,
source files, model, acceptance condition, and future seeds.

| Stage | Per confirmation | Combined confirmations |
| --- | ---: | ---: |
| Shape and partial-view integration | 244/244 | 488/488 |
| Conditional object permanence | 176/176 | 352/352 |
| Distinct-object tracking | 96/96 | 192/192 |
| Spatial translation and planning | 272/272 | 544/544 |
| **Total** | **788/788** | **1,576/1,576** |

These 1,576 checks are not 1,576 interchangeable accuracy trials. They include
positive predictions, ambiguity and out-of-model UNKNOWN cases, state-history
comparisons, causal interventions, and exact pixel comparisons. Replay is a separate validation. The visual
summary is [four_stage_results_v2.png](four_stage_results_v2.png).

The independent evidence is consistent across both confirmations. Each sealed
run contains 1,556 runtime transitions. Replay rederived the raw training rows
and targets, reconstructed all 29,174 proposals and their paired feedback in
order, reproduced the selected programs, replayed every transition, and
independently recomputed all 33 assessment-cell predicates rather than trusting
stored pass flags. See the receipts for
[seed 20261007](runs/replay_confirmation_20261007_worker_receipt.json) and
[seed 20261011](runs/replay_confirmation_20261011_worker_receipt.json), and the
underlying 20261007 [summary](runs/confirmation_20261007/summary.json) and
[seal](runs/confirmation_20261007/seal.json), plus the 20261011
[summary](runs/confirmation_20261011/summary.json) and
[seal](runs/confirmation_20261011/seal.json).

The [43 focused unit tests](checks/unit_tests_boundary_final.json) passed with no
failures, errors, or skips. The bounded exhaustive
[geometry receipt](checks/geometry_final_receipt.json) checked all 8,852 legal
single-object poses against the independently implemented evaluator renderer. It
grounded all 3,952 learned-bank templates, covering 3,628 distinct rasters. All
324 cross-concept alias masks were retained as UNKNOWN, and the sweep reported
zero failures.

## What was learned, and why it matters

The finite arithmetic constructor acquired three reusable expressions from raw
teaching measurements, exported in [learned_model.json](learned_model.json):

- `max(abs(x), abs(y)) <= 3`
- `x*x + y*y <= 9`
- `cur + (cur - prev) * lag`

The first two became unnamed geometric concept slots before the arbitrary words
`tov` and `mip` were attached. The third was learned from raw-decoded motion
demonstrations. The same serialized predicates generated unseen pose rasters and
constrained partial views; the same motion expression forecast hidden positions,
performed commanded displacements, and supported routes whose steps were
independently rendered and perceived.

This is the functional point drawn from Pinker's books and the supplied reading
record: a representation matters when it carries a relationship and causally
organizes later computation. A remembered label alone is weak evidence. A
generative relation that makes several linked predictions, survives fresh
inputs, and fails in a specific way when altered is harder to vary. Here,
clearing the actual geometry bank removed geometric answers; replacing the
motion AST with `cur` produced the predicted stale hidden location and unmoved
translated raster while leaving perception intact. Memory erasure, binding
erasure and swap, sham controls, restoration, matched camera/object motion, and
same-current-frame/different-history cases isolate further causal roles. The
detailed argument and book-page references are in [RATIONALE.md](RATIONALE.md).

## What was supplied

The result depends on substantial declared priors: a 24×24 calibrated binary
world; canonical panels; a fixed arithmetic grammar and first-exact-fit search;
convex level-set support; finite radii, rotations, centers, and object count;
camera calibration; persistent tokens; one-to-one continuity and bounded
matching; explicit commands and references; four cardinal actions; and bounded
breadth-first search. Shape predicates and the motion formula were learned.
Pose transformation, convexity, tracking, object enumeration, task selection,
and planning machinery were supplied.

This distinction caught a real development error. Discrete clipping initially
admitted 564 rotated-box edge templates that violated the evaluator's continuous
fully-visible rule. The fix was a generic, charged convex-support optimizer over
the learned expression, without circle/square AST special cases. It removed all
564 inconsistent templates while leaving the learned formulas and independent
world renderer unchanged; the exhaustive geometry gate then passed.

Object permanence here is conditional: given the learned motion relation and
supplied continuity assumptions, the machine predicts an occluded location and
revises it when visible evidence returns. Symmetric identity cases and
byte-identical circle/rotated-box rasters correctly remain UNKNOWN. Translation
means spatial coordinate translation only, as explicitly confirmed for this
experiment. The result does not establish natural vision, unrestricted object
identity, language translation, general intelligence, or that these priors were
learned.

Input integrity is recorded in [input_integrity.json](checks/input_integrity.json):
all four original inputs remained present, 373 supplied archive files were
checked unchanged, and no archive API code was executed. The new experiment
used no neural network or provider call. An early run itself passed, but its
controller mistakenly expected a `status` field from `verify_seal` and therefore
marked that receipt invalid. The original evidence was preserved; corrected
read-only validation and frozen baseline replay passed. Final qualification
rests on the later frozen bounded receipts, seals, exact replays, independent
assessment audits, and exhaustive geometry receipt linked above.

See the [independent final review](checks/final_independent_review.json) and
[README](README.md) for bounded replay commands and the runtime entry point.
