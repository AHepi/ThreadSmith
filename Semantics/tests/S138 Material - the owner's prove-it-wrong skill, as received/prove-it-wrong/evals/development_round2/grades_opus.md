# Grading: Set 1 vs Set 2 (six held-out cases)

I graded against `marking.md`, including the amendments adopted before grading: h1 M4 reworded; h3 M4 reworded and M5 added; h4 M1 softened; h6 M4 merged into M2; extra-credit items; the X1 parenthetical. With the merge, h6 has three MUST items, so there are 24 MUST items in total.

Key: **F** = found, **P** = partly, **M** = missed. "Padding" counts points that would fit any claim, or that add nothing for this case. This includes "does not apply" or "N/A" rows and checks with no link to the case.

---

## case_h1: BP-220 battery pack

### Set 1
| Item | Grade | Evidence |
|---|---|---|
| M1 500 cycles vs real lifetime | **P** | Lists "beyond 500 cycles" among the added jobs. It never argues that years of daily use imply several times 500 cycles. It actually marks the 500-cycle margin "held… for the condition actually tested". |
| M2 single 23°C condition | **F** | "Swap it for 35°C or -10°C and the explanation gives no answer; it is a single point standing in for a range" |
| M3 no abuse/safety testing | **F** | "A real abuse/fault-injection test (short, puncture, overcharge) to justify 'safety'" |
| M4 n=5, variance/lots | **F** | "5 units cannot estimate scale variance; this is a sample-size claim dressed as a variance finding" |
| Extra credit | **2** | Vibration: "under vibration/road use". Calendar aging: "cold weather, abuse, scale variance, calendar aging". |

MUST-NOT:
- Accepting safety from the cycling data: not violated ("the recommendation reaches further than the evidence").
- Treating BMS logs as proof that no unsafe failure modes exist: not violated. It says the review "holds only if the test ever presented conditions that would trigger a fault".
- Inventing numeric standards: not violated.
- X1–X4: none violated.

Errors: none of substance.

Padding: 2 (the "Check patches: N/A" line; the "re-run with a different lab technician" control poke).

### Set 2
| Item | Grade | Evidence |
|---|---|---|
| M1 500 cycles vs real lifetime | **M** | 500 cycles is only used as the endpoint inside its falsifiers ("by cycle 500"). It is never questioned. |
| M2 single 23°C condition | **F** | F1: "At -10°C or 40°C+ ambient (seasonal extremes)…" |
| M3 no abuse/safety testing | **F** | F3: "short-circuit, crush, nail-penetration or overcharge test" |
| M4 n=5, variance/lots | **F** | F2: "30+ units across 3+ production lines" |
| Extra credit | **1** | Vibration, in Q6: "on-bike vibration and seasonal road use" |

MUST-NOT: none violated. F5 asks for an independent re-review of the BMS logs, which is weak but not the forbidden equation.

Errors:
- F4 is incoherent given the text. All units lost less than 4%, so no unit can be "within 1 point of the 10% threshold".
- "One apparent batch" is an inference the text does not support, though it is hedged.

Padding: 6 (Q2, Q3, Q4, Q5-C3 and Q8 "does not apply"; F5, the generic independent log re-review).

**Better: Set 1.** Set 1 partly gets M1, which Set 2 misses entirely. Set 1 also earns more extra credit and has no incoherent falsifier.

---

## case_h2: XR-14 RA trial

### Set 1
| Item | Grade | Evidence |
|---|---|---|
| M1 narrow enrollment vs broad label | **F** | "Safety and efficacy in patients the trial excluded (>65, cardiovascular disease, hepatic impairment, concurrent biologics), in non-academic/rural settings" |
| M2 12-week follow-up | **F** | "beyond 12 weeks of chronic RA treatment"; "longer follow-up would show rare or late adverse events" |
| M3 robustness, pre-specification, multiplicity | **F** | "no mention of a pre-specified primary endpoint or correction for multiple comparisons". It does not do the arithmetic on event counts (about 6 vs 16), but it asks the required questions. |
| M4 hospitalization ascertainment / blinded adjudication | **F** | "no detail given on… who adjudicated hospitalization (an outcome assessors could influence if unblinded)" |
| Extra credit (dropout) | **1** | "differential dropout before a hospitalization could be recorded" |

MUST-NOT: none violated. It does not accept the broad label, it does not call the drug unsafe ("That XR-14 doesn't work broadly — only that this trial doesn't yet demonstrate it"), and it does not fabricate numbers.

Errors: none.

Padding: 2 (the "Flip" check; the "Best rival" check, which restates M1).

### Set 2
| Item | Grade | Evidence |
|---|---|---|
| M1 narrow enrollment vs broad label | **F** | F1: "In over-65s, or cardiovascular/hepatic/biologic patients (excluded here)…" |
| M2 12-week follow-up | **P** | F2 covers long-term safety only ("52+ week follow-up"). On the durable hospitalization benefit, Q9 marks it the other way: "C1,C3 covered: 412 randomized, 8 centers, 12-week window". |
| M3 robustness, pre-specification, multiplicity | **F** | F3: "registry entry does not list hospitalization as the 1 primary endpoint". F4: an intention-to-treat sensitivity recount. |
| M4 hospitalization ascertainment / blinded adjudication | **M** | Argues the opposite in F6: "self-reported gain is unblinding-vulnerable; hospitalization is not". |
| Extra credit (dropout) | **1** | F4: "dropouts as events"; Q13 |

MUST-NOT:
- Label scope / fabricated numbers: not violated.
- **X2: violated (minor).** Q13 says "all 412 randomized patients followed for AEs", which the text never reports, and it contradicts the answer's own F4 dropout concern.

Errors:
- F6 wrongly treats hospitalization as immune to unblinding; admission decisions are clinical judgments.
- Q6 says randomization is "covered" with no baseline-balance check.
- Q9 treats 12 weeks as adequate for the efficacy claim.

Padding: 7 (Q2, Q4, Q5-C3, Q7-C2/C3, Q8 and Q10-C2/C3 "does not apply"; F5, the generic audit).

**Better: Set 1.** Set 1 gets M4, which Set 2 contradicts. Set 2 also has an unreported "covered" assertion.

---

## case_h3: Athena-7B benchmarks

### Set 1
| Item | Grade | Evidence |
|---|---|---|
| M1 contamination | **F** | "no decontamination check is reported between the training corpus and the MMLU/GSM8K test sets" |
| M2 baseline re-run vs copied | **P** | It notes the baseline "may be one model's mean against another's single reported point". But it accepts the "Matched 5-shot/8-shot-CoT protocol" as **held** and never asks whether the baseline was re-run under the same harness. |
| M3 narrow evaluation | **F** | "extrapolation from two static benchmarks"; "contamination-controlled or more recent held-out benchmarks"; whether chain-of-thought traces "are coherent reasoning or pattern completion" |
| M4 ±sd is prompt-ordering only | **P** | Asks whether the margin exceeds "the baseline's own run-to-run noise". But it calls the reported spread **held** because it "controls prompt-order noise", and never says that spread cannot support "comfortable margin". |
| M5 re-run both models under one harness using the released weights/scripts | **M** | Never mentions using the released weights and scripts to re-run both models. |

MUST-NOT: none violated. It does not decide whether the model is state of the art ("That Athena-7B is not actually better — only that…"), and it asks the authors to publish decontamination rather than demanding insider information.

Errors: none. Its "only one baseline / 'previous best' asserted" point is a fair extra.

Padding: 2 (the "Flip" check; "Check patches: N/A").

### Set 2
| Item | Grade | Evidence |
|---|---|---|
| M1 contamination | **F** | Q2/F1: "a 2.1T-token web/code/book corpus may already contain near-duplicates of benchmark items" |
| M2 baseline re-run vs copied | **M** | Accepts it outright in Q6: "covered — same harness, same 5-shot/8-shot protocol, as reported, for both models". |
| M3 narrow evaluation | **F** | F5: a new, unreleased word-problem set. F4: a human-graded sample of 200 GSM8K items. |
| M4 ±sd is prompt-ordering only | **P** | F3: "the ±0.3/±0.6 spread covers only prompt order". It points the fix at fine-tuning seeds rather than harness or baseline-measurement variance, and does not connect it to the margin. |
| M5 re-run both models under one harness using the released weights/scripts | **M** | F6 re-runs Athena only. It is marked "reported" and "Effect: none" although the receipt says "not rerun by us", so the release is treated as if it were a replication. |

MUST-NOT: none violated.

Errors:
- F2 (a majority-class or "copy the last number" baseline within 5 points) is implausible. Majority class on MMLU is about 25% against 89%. It is still chosen as one of the two "cheapest tests".
- F6's "reported" status overstates what the text says.

Padding: 5 (F2; Q4, Q5-C2 and Q10 "does not apply"; Q13).

**Better: Set 1.** Set 1 at least partly gets M2, which Set 2 marks "covered". Set 2 also leads with an implausible next test.

---

## case_h4: minimum wage and teen employment

### Set 1
| Item | Grade | Evidence |
|---|---|---|
| M1 COVID confound (with credit for the reported controls) | **F** | "Year fixed effects absorb common shocks, but if treated and comparison counties differed in pandemic exposure… parallel trends could… break"; "excluding or isolating the COVID years" |
| M2 adjacency spillover / non-adjacent comparison | **F** | "Swap 'neighboring' for 'non-adjacent, same state' counties… bias the estimate toward zero" |
| M3 outcome measure | **F** | "hours, scheduling, hiring freezes, or automation… did prices rise?" |
| M4 lagged effects / short post window | **M** | Automation appears only as a margin of adjustment. The length of the post-treatment window is never questioned. |
| Extra credit (endogenous adoption) | **0** | Not raised. It does add good points outside the key: CI width and power ("no power calculation is given") and the policy's "bite". |

MUST-NOT: none violated. It makes no outright effect claim ("no cost showed up on this outcome, in these counties"), and it does not demand a randomized trial.

Errors: none.

Padding: 2 (the "Flip" check; "Check patches: N/A").

### Set 2
| Item | Grade | Evidence |
|---|---|---|
| M1 COVID confound | **M** | COVID or the pandemic is never mentioned. |
| M2 adjacency spillover | **M** | F1 is about comparison counties experiencing "a similar increase", which is incoherent because by definition they did not raise wages. Spillover is never raised. |
| M3 outcome measure | **F** | F4: hours worked. F5: firm closures / survivor-only sample. |
| M4 lagged effects | **M** | Not raised. |
| Extra credit | **0** | Not raised. Good points outside the key: CI width (F2) and county heterogeneity (F3). |

MUST-NOT:
- No outright effect claim; no randomized-trial demand.
- **X2: violated (minor).** Q10 says the "specification and comparison group are described as fixed in advance". The text describes several specifications and alternative comparison groups and says nothing about pre-registration.

Errors:
- F1 is incoherent.
- F6 attributes "within 0.5 points/year" to the report, which only says "track closely".

Padding: 4 (Q2, Q3, Q4 and Q8 "does not apply").

**Better: Set 1, clearly.** Set 1 gets 3 of 4. Set 2 gets 1 of 4 and misses both central identification threats.

---

## case_h5: payment-gateway post-mortem (the well-tested control case)

### Set 1
| Item | Grade | Evidence |
|---|---|---|
| M1 credits the targeted testing | **F** | "reproduced in staging with the actual latency profile… This is a genuine poke (cause intervened on, effect moves)"; load metrics "look inside the mechanism" |
| M2 one real remaining scope limit | **F** | Several amendment-listed limits: cached payment responses must not "cause double charges or stale confirmations"; "'no rollback' may just mean normal traffic was fine"; "a short window understates confidence" |
| M3 48h/5% canary vs long-tail or seasonal traffic | **P** | Says the canary may not have met a real spike. It does not raise monthly or holiday peaks beyond the 3x synthetic load. |
| M4 other services sharing pool/dependency | **M** | Not raised. |

MUST-NOT: not violated. It asks for no core test to be redone and invents no contradicted failure mode. However, its top recommendation is a component-by-component ablation of the three fixes, which is low value for an operational fix and counts as padding.

Errors: none.

Padding: 1 (the ablation demand).

### Set 2
| Item | Grade | Evidence |
|---|---|---|
| M1 credits the targeted testing | **F** | F1–F3 marked "survived", "Effect on claim: none" |
| M2 one real remaining scope limit | **F** | The key's own example. F5: "A real (non-latency) gateway error is swallowed by the new breaker"; the next test is to "inject a real (non-timeout) gateway error". |
| M3 48h/5% canary vs long-tail traffic | **P** | F6: "'no recurrence' covers 1 canary, 1 spike size"; Q1: "one multiplier (3x)". It does not raise seasonal or billing peaks. |
| M4 other services sharing pool/dependency | **M** | Not raised. |

MUST-NOT: not violated. However, F4 makes the well-reproduced root cause "held if no other same-window change explains the outage", which slightly undercuts a cause that the replay with the old code directly showed.

Errors: F4's framing, as above (minor).

Padding: 5 (Q2, Q4 and Q8 "does not apply"; Q5-C1/C3; Q13).

**Better: tie.** Both get 2 found, 1 partly and 1 missed. Set 1 covers more of the amendment's limits, including payment-semantic caching. Set 2 hits the key's main example, fail-fast errors, and makes it the next test.

---

## case_h6: CFD flap simulation

### Set 1
| Item | Grade | Evidence |
|---|---|---|
| M1 mesh convergence | **F** | "no grid-convergence study (multiple refinement levels) is reported… Swap for a 2x-finer mesh" |
| M2 (merged with M4) validation only on the baseline / k-ω SST with separation | **F** | "a deflected flap introduces local separation… k-ω SST is known to be sensitive there. One validation point on the easy case does not bound the error on the hard one" |
| M3 single operating point (AoA/Re sweep) | **M** | No sweep across AoA or Re is requested. Re and AoA appear only as the validation condition. |
| Extra credit | **0** | No 3D extrapolation point. It touches on 3% vs 14% ("no uncertainty band"), but too thinly to count. |

MUST-NOT: none violated. It does not call the result confirmed or wrong, and it does not fault the authors for lacking flap wind-tunnel data: "the proposed wind-tunnel test is the right next step".

Errors: none.

Padding: 2 (the "Flip" check; "Check patches: N/A").

### Set 2
| Item | Grade | Evidence |
|---|---|---|
| M1 mesh convergence | **F** | F3: "a doubled mesh… the gain could be a mesh/model artifact" |
| M2 (merged with M4) validation only on the baseline | **F** | Q6/F1: "the validation ran on the unmodified baseline, not the flap case" |
| M3 single operating point | **F** | F2: "At AoA 2° or 8°"; F5: "At Re 2x or 0.5x" |
| Extra credit | **0** | — |

MUST-NOT: not violated, though borderline. Q7, Q11 and Q12 lean on the missing wind-tunnel comparison.

Errors: Q12 misreads the text. It says "a wing revision is planned on this before the tunnel test", but the text puts wind-tunnel testing *ahead of* the wing revision. F4 and Q11-C1 also speculate that convergence was not reported for the flap case.

Padding: 6 (Q2, Q4, Q5 and Q10 "does not apply"; Q13; F4).

**Better: Set 2.** It gets all three MUST items, including the sweep that Set 1 misses. Set 1's reasoning on the turbulence model is deeper, and Set 2 misreads the text in Q12.

---

## Summary table

| Case | Set 1 MUST F/P/M | Set 1 MUST-NOT violated | Set 2 MUST F/P/M | Set 2 MUST-NOT violated | Better |
|---|---|---|---|---|---|
| h1 battery | 3/1/0 | 0 | 3/0/1 | 0 | Set 1 |
| h2 XR-14 | 4/0/0 | 0 | 2/1/1 | 1 (X2, minor) | Set 1 |
| h3 Athena-7B | 2/2/1 | 0 | 2/1/2 | 0 | Set 1 |
| h4 min wage | 3/0/1 | 0 | 1/0/3 | 1 (X2, minor) | Set 1 |
| h5 post-mortem | 2/1/1 | 0 | 2/1/1 | 0 | Tie |
| h6 CFD | 2/0/1 | 0 | 3/0/0 | 0 | Set 2 |

## Totals (24 MUST items)

| | Found | Partly | Missed | MUST-NOT violations | Extra credit | Padding |
|---|---|---|---|---|---|---|
| **Set 1** | **16** | 4 | 4 | 0 | 3 | ~11 |
| **Set 2** | **13** | 3 | 8 | 2 (both minor X2) | 2 | ~33 |

Per case: Set 1 is better on 4, Set 2 on 1, and 1 is a tie.

## Three most important weaknesses

### Set 1
1. **It misses time-horizon and operating-envelope scope.** It misses the short post-treatment window in h4 (M4) and the AoA/Re sweep in h6 (M3), and only partly gets the cycle-life horizon in h1 (M1) and the seasonal canary limit in h5 (M3).
2. **It accepts the stated evaluation protocol too readily.** In h3 it marks the "matched protocol" and the prompt-order spread as held, so it only partly gets M2 and M4, and it never proposes the decisive re-run of both models from the released weights (M5).
3. **Its fixed checklist checks are sometimes filler, and its biggest asks can miss the target.** Most cases have Flip / "Check patches: N/A" filler. In h5 the top recommendation is a component ablation instead of shared-dependency or traffic-pattern scope, and M4 is missed there.

### Set 2
1. **It misses the central domain-specific confounds.** It misses COVID and spillover in h4 (M1, M2), blinded hospitalization adjudication in h2 (M4, where it asserts the opposite), and the baseline harness question in h3 (M2).
2. **Its "covered" / "does not apply" rows accept or assert facts the text does not give.** Examples: h2 Q13 ("all 412… followed for AEs") and Q9 (12 weeks adequate); h3 Q6 (same harness) and F6 (release treated as replication); h4 Q10 ("fixed in advance"); h6 Q12 (misreads the order of tunnel test and wing revision). These produce the two X2 violations.
3. **Its falsifiers can be incoherent, and its padding is heavy.** h1 F4 is already ruled out by the "<4%" result. h3 F2's majority-class baseline is implausible yet chosen as a next test. h4 F1 has comparison counties raising wages. Roughly a third of each Q table is boilerplate: about 33 padding points against 11 for Set 1.

## Overall judgement

Set 1 is the stronger set. It finds more required points (16 vs 13 found, 4 vs 8 missed), violates nothing, and reasons more accurately about mechanisms such as spillover, the COVID confound, blinded adjudication and the turbulence model. Set 2 is more compact and does better on h6, but its fixed table pushes it toward "covered" judgements that accept or invent facts, and toward misses on the confounds that matter most.

My confidence is moderate to high. A few grades are borderline (h2 M3 for both sets, h5 M3, and Set 2's two minor X2 calls), but changing any of them would not reverse the overall ranking.
