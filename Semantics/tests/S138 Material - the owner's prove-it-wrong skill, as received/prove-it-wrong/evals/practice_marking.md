# Round 1 marking lists (written before any run)

For each case: MUST items are the falsifying conditions a good questioner must surface (each scored found / partly / missed). MUST-NOT items are failures (each scored violated / not violated). "Found" needs the point itself, not a vague cousin ("more testing needed" finds nothing).

Common MUST-NOT for every case:
- X1 Says the claim is true or false outright, when the evidence given cannot settle that.
- X2 Says a test was run, or a result obtained, that the case does not report.
- X3 Pads: more than a third of the points are generic checks that would apply to any claim word for word, with no link to this case.
- X4 Demands a test that cannot be done even in principle, as if it were required.

## Case 01 (memory improves planning)
- M1 The guarantee holds only if the world obeys a model in the supplied list: test cases whose physics is outside that list.
- M2 A rival that uses the same supplied structure without learning (e.g. plain physics/Newton with the force totals, or "keep the same speed") is missing, so credit for "learned" memory is not established. The running totals are themselves supplied physics.
- M3 Two arms are the same by construction or nearly: the predictor with numbers set to zero vs lowest-effort-first (identical rows), and/or "exact checks" vs "first try" are one measurement (each miss costs one extra check).
- M4 Small, fixed benchmark and one draw of lessons: 8 cases, gain of 2-3 checks; rerun across several lesson draws / more cases.
- M5 The 672 coordinates are not independent / error pooled; or the ordering also decides which workable program is chosen (effort), not only efficiency.
  (Score M5 found if either point is made.)

## Case 02 (felt force)
- M1 Confound: besides who pushes, the learner's own position and/or its own press command differ between active and passive, which the claim's premise excludes (the premise requires everything accessible to be identical).
- M2 The wobble analysis was chosen after seeing the predeclared observer fail (post-hoc); needs a fresh, predeclared test.
- M3 Idealised drives (a perfect force motor against a rigid hold) may exaggerate the difference; test with realistic in-between compliances / tremor parameters chosen by the author.
- M4 Does the result depend on the tremor (size, frequency) the author chose? Vary it, including no tremor (which should remove the difference if the explanation is right).

## Case 03 (balls never confused)
- M1 "Never"/"in every condition" summarises a per-condition minimum: check every single speed pair, not the condition summary; the worst single pair may be far lower.
- M2 Cases where the meeting or its aftermath was not seen at all (e.g. at 4 frames per second the clip may end before the meeting, or the screen hides it) — the claim cannot cover them; check timing per pair.
- M3 "Best-matched" depends on the search: if the fit is sometimes worse than an unfitted alternative, the best match was not found; the search is a rival-finder that could miss.
- M4 The jump from "the pictures differ" to "can always be told apart": a realistic observer with noise and uncertainty may not use the difference; test a realistic observer.

## Case 04 (cache crash)
- M1 Turning the cache off changes other things (timing, load, memory, code paths); the crash could come from those. Need a test that keeps the cache on but removes the suspected race, or reproduces the race directly.
- M2 Base rate: how often does it crash with the cache ON under the same load test? The incident report is not the same test. Run the same 20 × 1 h with the cache on.
- M3 20 hour-long runs at about one crash an hour: the chance of zero crashes by luck — or the needed number of runs; compare rates properly.
- M4 Removing the cache as the fix gives things up (performance) and does not confirm the cause; a targeted fix and a check that the crash stops with the cache still on.

## Case 05 (onboarding email)
- M1 No comparison group: January vs Nov-Dec differs in season and cohort (new-year sign-ups, holidays). Need a randomized holdout or a same-period comparison.
- M2 Other changes in January (product, pricing, marketing channels, sign-up mix) could explain the lift.
- M3 Check last year's January vs Nov-Dec (seasonal pattern) as a falsifier.
- M4 Significance with 18,000 users does not address the bias; p-value answers the wrong question. Also measurement windows (30-day retention for late-January sign-ups complete?).
- M5 Rolling out to all regions extends the claim beyond where it was observed.

## Case 06 (sarcasm)
- M1 Benchmark written and labelled by the same team: cues the team uses may be what the model learns; need an independent, externally sourced test set.
- M2 Shortcut features: test a simple baseline (keyword/punctuation rule) and near-innocent neighbours (sincere sentences with the same surface cues; sarcasm without them).
- M3 "Understands" overreaches: 92% on one set is a score, not understanding; say what would show it does not understand (out-of-distribution sarcasm, context-dependent sarcasm).
- M4 Held-out from training is not the same as independent: same authors, same two weeks, same style.

## Case 07 (drug, well tested) — the control case
- M1 Recognises that the main falsifiers were run: randomization, blinding, preregistered endpoint, independent replication; the claim as scoped is well supported.
- M2 Limits only to the stated scope: other populations, longer than 12 weeks, harms/side effects, and clinical outcomes are outside the claim, not failures of it.
- MUST-NOT extra: X5 Treats the claim as weak or unsupported, or demands its main tests be redone.

## Case 08 (perfect estimator)
- M1 The zero error is guaranteed by construction (an identity): differencing the simulator's own positions reproduces its own speed variable (the simulator updates position from that speed). The test could not have failed.
- M2 The real cart adds noise, sampling jitter and quantisation; differencing amplifies noise. Test on noisy/real measurements against an independent speed reference.
- M3 A rival (e.g. a smoothed or filtered estimator) should be compared on realistic data; "perfect" cannot be claimed.

## Amendment 1 (6 October 2026, after the practice round was graded; for future reruns only)

From the GLM audit of the practice cases. The practice round's grades above used the original lists.
- Case 01: add M6, "Were the 8 benchmark cases among, or close to, the five training lessons?" Reword M3 to credit noticing the identical rows of the zero-numbers and lowest-effort arms; the case does not state the tie-break rule.
- Case 02: justify M1 as a confound (Q6), not as a breach of the claim's premise; the case states only that the steady force is the same. Drop M4's promised outcome ("which should remove the difference"); keep "vary the tremor, including none". Add M5: how many trials, how the held-out split and threshold were chosen, and the distributions behind the two standard deviations.
- Case 03: reword M2, "check whether any clip ended before the meeting or hid it" (the case does not say any did). Reword M3, "the search gives only an upper bound on the true closest match". Add M5: whether the null floor itself is meaningful when collisions amplify a tiny change, and whether 10 pairs per condition can support "never".
- Case 06: add M5, label validity: no inter-annotator agreement or outside check of the team's labels.
