# Grading

## Case h1 — battery pack (BP-220)

### Set 1

| MUST | Verdict | Evidence |
|---|---|---|
| M1 500 cycles vs longevity | **Found** | "Holding up across the claimed outdoor temperature range… beyond 500 cycles… **added** by this review, because the conclusion… already commits to them." Brief, but the point itself is made. |
| M2 single 23°C condition vs four seasons | **Found** | "*23°C ambient test condition* — **loose**: nothing holds this to 'four seasons.' Swap it for 35°C or -10°C and the explanation gives no answer." |
| M3 abuse/safety testing absent | **Found** | "A real abuse/fault-injection test (short, puncture, overcharge) to justify 'safety,' since BMS log review alone doesn't poke failure modes." |
| M4 (amended) n=5 / batch variance | **Found** | "n=5 units → 'no indication of manufacturing variance at scale' — **loose, likely overreach**: 5 units cannot estimate scale variance"; asks for "a larger sample." No multi-lot ask, but the questioning is explicit. |

**Extra credit (amdt 2):** 2 raised — vibration ("under vibration/road use") and calendar aging ("Add a job (cold weather, abuse, scale variance, calendar aging)"). IP/water-ingress not raised.

**MUST-NOT:** N1 not violated (challenges safety conclusion); N2 not violated ("passive monitoring of normal cycling doesn't poke the BMS"); N3 not violated. X1–X4: none violated (§6 explicitly non-adjudicating).

**Errors:** none.
**Padding:** 1 ("Check patches: … nothing to check. N/A." — pure scaffolding).
**Verdict line:** n/a — compare below.

### Set 2

| MUST | Verdict | Evidence |
|---|---|---|
| M1 500 cycles vs longevity | **Missed** | No falsifier or Q-row questions cycle count vs product lifetime; closest is F4, which probes margin *within* 500 cycles ("within 1 point of the 10% threshold… at cycle 500"). |
| M2 temperature range | **Found** | "At -10°C or 40°C+ ambient (seasonal extremes)… C3 held only at the tested 23°C, not four seasons." |
| M3 abuse testing | **Found** | F3: "short-circuit, crush, nail-penetration or overcharge test… 'meets safety targets' unsupported for fault conditions." |
| M4 n=5 / batch | **Found** | F2: "30+ units across 3+ production lines… 'no variance at scale' unsupported by n=5, one apparent batch" — hedged "apparent," consistent with amendment 1. |

**Extra credit:** 1 raised — vibration (Q6: "stationary climate-controlled bench differs from on-bike vibration"). No calendar aging, no IP.

**MUST-NOT:** N1, N2, N3 not violated (its invented thresholds like "-10°C/40°C+" are proposed falsifier conditions, not fabricated cited standards). X1–X4: none violated.

**Errors:** minor — Q5/F4 treats "<4%" and "no unit >45°C" as aggregates "hiding" per-unit data; the text's figures are already per-unit (exact margins unknown, but not hidden aggregates).
**Padding:** 0 substantive (the many "does not apply" rows are scaffolding, not claims).
**Better: Set 1** — identical on M2–M4, but Set 1 also raises the 500-cycle/longevity gap and one more extra-credit item.

---

## Case h2 — XR-14 trial

### Set 1

| MUST | Verdict | Evidence |
|---|---|---|
| M1 narrow enrollment vs broad label | **Found** | "Safety and efficacy in patients the trial excluded (>65, cardiovascular disease, hepatic impairment, concurrent biologics), in non-academic/rural settings… — **added**, because 'broad label…' and 'rapid adoption' already claim these." |
| M2 12-week adequacy | **Found** | "beyond 12 weeks of chronic RA treatment — **added**" plus "a larger n or longer follow-up would show rare or late adverse events this trial has no power to detect… named test: extended-duration, larger-n safety study." |
| M3 robustness of headline comparison | **Found** | "no mention of a pre-specified primary endpoint or correction for multiple comparisons. A trial that measured several outcomes and highlighted the ones that worked is a different, weaker claim." Gap: never notes the ~6-vs-16 event counts, and no sensitivity-analysis ask. |
| M4 hospitalization ascertainment/blinded adjudication | **Found** | "no detail given on allocation concealment or who adjudicated hospitalization (an outcome assessors could influence if unblinded)." |

**Extra credit (amdt 3):** 1 raised (in passing) — "differential dropout before a hospitalization could be recorded."

**MUST-NOT:** N1 not violated (neither accepts the label nor declares the drug unsafe/ineffective: "only that this trial doesn't yet demonstrate it"); N2 not violated (no invented counts). X1–X4: none violated.

**Errors:** none.
**Padding:** 0 (all framework checks carry case content).
**Verdict line:** n/a.

### Set 2

| MUST | Verdict | Evidence |
|---|---|---|
| M1 narrow enrollment vs broad label | **Found** | F1: "In over-65s, or cardiovascular/hepatic/biologic patients (excluded here), rates differ… 'broad label, adult patients' unsupported outside enrolled population" (+Q1, urban centers). |
| M2 12-week adequacy | **Partly** | F2 covers long-term **safety** only ("2,000+ patient or 52+ week follow-up… 'no serious events' limited to 412 patients, 12 weeks"); nowhere questions whether the *hospitalization benefit* is durable over years of treatment. |
| M3 robustness of headline comparison | **Found** | F3: "The dated registry entry does not list hospitalization as the 1 primary endpoint, or lists 2+ unreported endpoints… p=0.02 on an after-chosen endpoint is a new, weaker claim"; F4 adds an ITT sensitivity check. Same gap as Set 1: no event-count arithmetic; no multiplicity ask. |
| M4 ascertainment/blinded adjudication | **Partly** | F5 proposes a general blinding audit ("assignment-guessing above chance at 1+ of 8 centers"), but F6 explicitly waves off the endpoint-specific concern: "self-reported gain is unblinding-vulnerable; **hospitalization is not**" — hospitalization adjudication/ascertainment is dismissed, not questioned. |

**Extra credit:** 1 raised — F4/Q13 (dropouts as events, analysis population).

**MUST-NOT:** N1 not violated ("unsupported beyond the tested population," conditional); N2 not violated (proposes tests, asserts no dropout rate). X1–X4: none violated.

**Errors:** minor — Q13 marks "all 412 randomized patients followed for AEs" as "covered"; the text nowhere states complete follow-up.
**Padding:** 0 substantive.
**Better: Set 1** — full marks on M2 and M4 where Set 2 is partial; comparable elsewhere.

---

## Case h3 — Athena-7B

### Set 1

| MUST | Verdict | Evidence |
|---|---|---|
| M1 contamination | **Found** | "no decontamination check is reported between the training corpus and the MMLU/GSM8K test sets"; asks for "an n-gram or embedding-overlap decontamination analysis." |
| M2 baseline re-run vs copied | **Partly** | Notices the copy issue obliquely — "the comparison may be one model's mean against another's single reported point… whether the margin exceeds the baseline's own run-to-run noise" — but never asks whether the baseline was re-run under the same harness or flags shot-count/prompt-template/harness-version shifts. Also ratifies the report's framing ("matched harness… **held**"). |
| M3 narrow evaluation | **Found** | "performance on contamination-controlled or more recent held-out benchmarks is a job the 'reasoning advance' claim already owes. Result: fails"; plus qualitative evaluation ("whether chain-of-thought traces are coherent reasoning or pattern completion"). |
| M4 (amended) variance understates margin | **Found** | "3 runs averaged with std… it controls prompt-order noise" (i.e., ±sd is prompt-order-only) combined with the baseline-noise/margin point directly undercutting "comfortable margin." |
| M5 (amdt 5) re-run both under one harness | **Missed** | Released weights/scripts never mentioned; no re-run ask for either model. |

**MUST-NOT:** N1 not violated ("the numbers alone cannot distinguish 'better reasoning' from 'more benchmark exposure'"); N2 not violated (asks the *authors* for decontamination). X1–X4: none violated.

**Errors:** none factual; the "matched… held" acceptance is a missed question, not a misstatement.
**Padding:** 1 ("Check patches: none described… N/A").

### Set 2

| MUST | Verdict | Evidence |
|---|---|---|
| M1 contamination | **Found** | F1: "2,000 MMLU/GSM8K items rewritten to avoid wording close to the 2.1T-token crawl… 'surpassing' and 'advance' unsupported if the margin is crawl-overlap, not reasoning." |
| M2 baseline re-run vs copied | **Missed** | Q6 marks harness comparability "**covered** | same harness, same 5-shot/8-shot protocol, as reported, for both models" — the case only says Athena's protocol *matched the baseline's reported protocol*; it does not report the baseline was run under this harness. No baseline-variance point either. |
| M3 narrow evaluation | **Found** | F5 ("a new, unreleased set of grade-school word problems in a different register") and F4 ("A human-graded sample of 200 GSM8K items"). |
| M4 variance | **Partly** | "the ±0.3/±0.6 spread covers only prompt order" is correct, but the vehicle is 5 SFT **training-seed re-runs** (off-target per amendment 4) and the link to the unsupported "comfortable margin" is never drawn. |
| M5 re-run both under one harness | **Partly** | F6 notes the rerun lever from released weights/scripts, but only for Athena ("A sample of 500 items reruns independently from the released weights/scripts") — not both models under one identical configuration. |

**MUST-NOT:** N1 not violated (conclusion held-if, unresolved); N2 not violated. X1–X4: none violated (F6 carefully says "reported… not rerun by us," avoiding X2; seed re-runs are costly, not impossible, so no X4).

**Errors:** Q6's "covered… for both models" overstates what the case reports; "the one learned open-weights rival **tested**" repeats the same implication.
**Padding:** 0 substantive.
**Better: Set 1** — M4 found vs partly, M2 partly vs missed; Set 2's only edge is the partial M5 (vs Set 1's miss), which does not offset.

---

## Summary table

| Case | Set 1 MUST (found/partly/missed) | Set 1 MUST-NOT violated | Set 2 MUST (found/partly/missed) | Set 2 MUST-NOT violated | Better |
|---|---|---|---|---|---|
| h1 | 4 / 0 / 0 (+2 extra credit) | none | 3 / 0 / 1 (+1 extra credit) | none | Set 1 |
| h2 | 4 / 0 / 0 (+1 extra credit) | none | 2 / 2 / 0 (+1 extra credit) | none | Set 1 |
| h3 | 3 / 1 / 1 | none | 2 / 2 / 1 | none | Set 1 |

**Totals (13 MUST items each):**
- **Set 1:** 11 found / 1 partly / 1 missed; 3 extra-credit points; 0 MUST-NOT violations; 2 padding points.
- **Set 2:** 7 found / 4 partly / 2 missed; 2 extra-credit points; 0 MUST-NOT violations; 0 padding points (but many contentless "does not apply" rows).

## Three most important weaknesses

**Set 1**
1. Never notices the released weights/evaluation scripts in h3, missing the decisive feasible check (M5) entirely and leaving the baseline re-run question (M2) only half-raised — its one outright miss and one partial.
2. Found-but-thin: key MUSTs are sometimes a single clause with no mechanism — h1 M1 ("beyond 500 cycles" with no years-of-use/cycle-life reasoning) and h2 M3 (neither set does the ~6-vs-16 event-count arithmetic; Set 1 also omits a sensitivity-analysis ask).
3. Framework scaffolding produces contentless rows (h1, h3 "patches N/A") and can ratify the report's own framing instead of questioning it (h3: "matched harness… held").

**Set 2**
1. Misses the 500-cycle/longevity question entirely in h1 — its falsifiers probe margins *within* 500 cycles, never whether 500 cycles suffices.
2. h3: marks harness comparability "covered… for both models" (Q6), missing M2 outright and reducing M5 to an Athena-only rerun; substitutes off-target training-seed variance (F3) for the margin-relevant uncertainty (M4 partly).
3. h2: durability of the hospitalization benefit is never questioned (M2 partly) and hospitalization adjudication is waved off rather than questioned ("hospitalization is not [unblinding-vulnerable]", F6; M4 partly), plus a minor unsupported assertion ("all 412 randomized patients followed for AEs").

## Overall judgement

Set 1 handled all three cases better: it found 11 of 13 MUST items outright against Set 2's 7, with the same clean record on every MUST-NOT and no factual errors; Set 2's falsifier tables are admirably concrete and testable, but they repeatedly miss the longitudinal/comparability dimension (cycle life, benefit durability, baseline re-run) and once accept a framing the case text does not support. Confidence: high for h1 and h2, where the differentials are unambiguous; moderate for h3 and for the M2/M4 "partly vs found" calls generally, since those rest on judgment about how much of each compound item is enough.# Grading report — cases h4, h5, h6

---

## case_h4 — minimum wage / teen employment

### Set 1

**MUST items**

- **M1 (amended: acknowledge state-level growth controls + ask pandemic-specific checks) — Found.** Acknowledges the reported checks: *"Robustness to alternative comparison groups / state controls, stable estimate — held, this is a real check against specification-fishing."* Then presses the pandemic: *"if treated and comparison counties differed in pandemic exposure (industry mix, reopening timing), parallel trends could hold pre-period and still break during the shock. Not addressed"* and *"Check whether results hold excluding or isolating the COVID years."*
- **M2 (spillover / non-adjacent comparison) — Found.** *"neighboring counties sharing a commuting zone can absorb spillover… bias the estimate toward zero. Swap 'neighboring' for 'non-adjacent, same state' counties — would the estimate move? Unknown, not run"*; and *"Re-run with non-adjacent, non-commuting-zone comparison counties to rule out spillover."* Acknowledges the reported alternative-comparison-group check while still asking (per grader note, no penalty).
- **M3 (outcome measure beyond headcount) — Found.** *"hours, scheduling, hiring freezes, or automation could all absorb the wage increase without changing headcount. … none of these margins are reported."*
- **M4 (post-treatment window / lagged effects) — Missed.** Automation appears only as an unmeasured *margin*; the time-horizon question (effects emerging later than the captured window) is never raised. Closest cousin: *"automation could all absorb the wage increase without changing headcount."*
- **Extra credit (endogenous adoption / self-selection of the 14 counties):** Not raised.

**MUST-NOT:** X1–X4: none violated (explicitly declines to adjudicate: *"only that, in this design, no cost showed up on this outcome, in these counties"*) ; case-specific: no outright "had/didn't have an effect"; no randomized-experiment demand. **No violations.**

**Wrong about the case:** Nothing material.

**Padding:** 1 (*"Check patches: no prior failed version is mentioned. N/A."*).

### Set 2

**MUST items**

- **M1 (pandemic / COVID window) — Missed.** COVID is never mentioned anywhere in the answer; the state-level growth controls are not acknowledged either.
- **M2 (spillover / adjacency) — Missed.** F1 addresses demographic similarity and generalization to "similar labor markets," not cross-border contamination of the comparison group; no non-adjacent-county or spillover test is requested.
- **M3 (outcome measure) — Found.** F4: *"Re-estimating with hours worked, not binary headcount, shows a 5%+ decline"*; F5: *"job losses via closure could be dropped from a survivor-only sample"*; Q7: *"headcount is one proxy… hours, firm survival are others."*
- **M4 (lagged effects / window length) — Missed.** Nothing on time horizon.
- **Extra credit (endogenous adoption):** Not raised.

**MUST-NOT:** X1–X4: none violated (the claim-as-it-stands is careful: CI "not distinguishable from zero… does not rule out a moderate loss"); case-specific: neither violated. **No violations.**

**Wrong about the case:** (i) F6 marks pre-trends tracking *"within 0.5 points/year"* as "reported" — the text says only "track closely"; invented precision. (ii) Q10: *"specification and comparison group are described as fixed in advance"* — the text does not say this. (iii) F2's *"a size other studies call meaningful"* imports an external judgment. All minor; none rises to X2.

**Padding:** 0 substantive ("does not apply" rows are table structure, not points).

**Better: Set 1** — it catches the case's two central design issues (COVID confound, spillover), which Set 2 misses entirely; Set 2's good points (CI width, heterogeneity, survivorship) are off-list.

---

## case_h5 — payment-gateway post-mortem (well-tested control)

### Set 1

**MUST items**

- **M1 (testing directly targets the failure mode; genuine strength) — Found.** *"Unbounded retry loop as root cause — held: reproduced in staging with the actual latency profile (p99 4.2s); old code cascades, new code doesn't… This is a genuine poke (cause intervened on, effect moves) and a real reverse check."*
- **M2 (at least one real remaining scope limit) — Found**, several times over: *"cached payment-status responses must not cause double charges or stale confirmations — that is not addressed anywhere"* (payment-semantic correctness, amendment-9 listed); plus breaker false-positive (*"the 'should not trip' half… was not run"*) and the short no-recurrence window (*"no duration is given… a short window understates confidence"*).
- **M3 (canary window doesn't cover longer-tail/seasonal traffic) — Missed.** Canary critique is about spike exposure (*"nothing indicates a live latency spike… occurred during the canary"*), not monthly billing spikes or holiday peaks.
- **M4 (other clients/services sharing the pool; compounding) — Missed.** Never raised.

**MUST-NOT:** Case-specific: no violation — all four core tests are credited as done and adequate (*"Regression suite, canary — given"*); the asks (component ablation, cached-response correctness, should-not-trip test) are new tests, not redoes; no contradicted failure mode invented. X1–X4: none (crediting the well-supported fix is permitted per amendment 12). **No violations.**

**Wrong about the case:** Nothing material.

**Padding:** 0 (its "check patches" entry carries case content).

### Set 2

**MUST items**

- **M1 — Found.** F1–F3 marked *"survived"* with receipts matching the text; Q11: *"fault-injection, load-test, suite results shown"*; claim-as-it-stands affirms *"the new client avoided it at that spike, load, and suite."*
- **M2 — Found.** F5: *"A real (non-latency) gateway error is swallowed by the new breaker, no alert fires… breaker could hide a failure, not surface it"* — the fast-fail vs slow-timeout gap, the canonical example.
- **M3 — Missed.** F6/Q9 cover canary duration and spike size; Q1's *"one multiplier (3x), not every prod condition"* is a vague gesture; no seasonal/billing/holiday traffic point.
- **M4 — Missed.** No other-services/shared-pool/compounding point.

**MUST-NOT:** Case-specific: no formal violation — core tests marked survived, next test is a new injection, not a redo. F4 (*"a same-window deploy/dependency bump, retries untouched"* as unruled-out alternate cause) is speculative doubt in the deliberately well-tested case and slightly undercuts the diagnosis, but it is not contradicted by the text and not a "dramatic invented failure mode." X1–X4: none. **No violations.**

**Wrong about the case:** Nothing factually wrong; F4 is low-value rather than false.

**Padding:** 0.

**Better: Set 1, narrowly (near-tie).** Identical MUST profile (2 found / 2 missed, same items); Set 1's remaining limits (payment-semantic correctness, breaker false-positive, ablation) are richer and it never stretches for doubt, whereas Set 2's F4 chips at a well-supported diagnosis.

---

## case_h6 — CFD airfoil flap

### Set 1

**MUST items**

- **M1 (mesh/grid convergence) — Found.** *"Single mesh (1.2M cells, y+≈1) — unknown: no grid-convergence study (multiple refinement levels) is reported, so discretization error, separate from residual convergence, is untested."*
- **M2 (merged: baseline-only validation / k-ω SST for separated flap flow) — Found.** *"a deflected flap introduces local separation… near the hinge that the baseline never exercises, and k-ω SST is known to be sensitive there. One validation point on the easy case does not bound the error on the hard one."*
- **M3 (single operating point; AoA/Re sweep) — Missed.** Re=3×10⁶ / AoA=4° is restated in the frozen question but never questioned; no sweep or envelope ask anywhere.
- **Extra credit (2D→3D extrapolation; 3%-vs-14% delta):** Not raised (the "easy case / hard case" point is M2 itself).

**MUST-NOT:** Case-specific: no violation — treats 14% as neither confirmed nor wrong (*"'confident… is accurate' is stronger than a baseline-only validation can support"*) and calls the wind-tunnel test *"the right next step, not an optional confirmation,"* criticizing the confidence claim rather than the absence of physical testing. X1–X4: none. **No violations.**

**Wrong about the case:** Minor technical slip only: "corner flow near the hinge" in a 2D simulation.

**Padding:** 1 (*"Check patches: no prior failure to check; this is a first version. N/A."*).

### Set 2

**MUST items**

- **M1 — Found.** F3: *"A second turbulence model or a doubled mesh, same Re/AoA, gives a gain differing from 14%… the gain could be a mesh/model artifact"*; Q9: *"one mesh, one turbulence model, one run, no second."*
- **M2 — Found.** F1: *"'accurate' is reported only via baseline validation, never the flap geometry"*; Q6: *"the validation ran on the unmodified baseline, not the flap case"* (satisfies the merged item per amendment 10).
- **M3 — Found.** F2: *"At AoA 2° or 8°… 14% is scoped to one AoA; nearby points untested"* and F5: *"At Re 2x or 0.5x… 14% holds at one Re; other conditions untested."*
- **Extra credit:** Partly raised — F1's threshold (*"differing from 14% by more than the baseline's 3% error"*) engages the 3%-vs-14%-delta question; the 2D→3D wing extrapolation is not raised.

**MUST-NOT:** Case-specific: no violation — does not declare the gain confirmed or wrong; the "Next test" is the numerical check *"before the tunnel prototype,"* and F1 targets the "accurate" claim, not the authors' plan to run the tunnel. X1–X4: none. **No violations.**

**Wrong about the case:** Two misreadings: (i) F4 claims *"convergence is reported for the setup, not the flap case"* — the text's convergence report covers the flap simulations; (ii) Q12: *"a wing revision is planned on this before the tunnel test"* — the text puts wind-tunnel testing *ahead of* wing-revision integration.

**Padding:** 0.

**Better: Set 2** — 3/3 MUSTs (uniquely catches the single-operating-point issue) plus partial extra credit, outweighing its two case-reading errors.

---

## Summary table

| Case | Set 1 MUST (F/P/M) | Set 1 MUST-NOT violated | Set 2 MUST (F/P/M) | Set 2 MUST-NOT violated | Better |
|---|---|---|---|---|---|
| h4 | 3/0/1 | none | 1/0/3 | none | Set 1 |
| h5 | 2/0/2 | none | 2/0/2 | none | Set 1 (narrow) |
| h6 | 2/0/1 | none | 3/0/0 | none | Set 2 |

**Totals** (11 MUST items): **Set 1 — 7 found / 0 partly / 4 missed; 0 MUST-NOT violations; 0 extra credit; 2 padding items. Set 2 — 6 found / 0 partly / 5 missed; 0 MUST-NOT violations; partial extra credit on h6 (3%-vs-14% element); 0 padding items.**

## Three most important weaknesses

**Set 1**
1. **Never questions whether the tested operating range is representative** — the single Re/AoA point in h6 (M3 missed) and seasonal/longer-tail traffic in h5 (M3 missed); strong on internal mechanism, weak on scope-of-conditions. (h6, h5)
2. **Ecosystem/interaction blind spot** — other clients or services sharing the connection pool and compounding during a simultaneous incident in h5 (M4 missed); the fix-in-isolation question is never asked. (h5)
3. **Time-horizon questioning absent** — h4's lagged-effects point (M4) missed; automation is treated as an unmeasured margin, never as a reason the post-treatment window may be too short. Minor corollaries: framework filler slots ("check patches N/A") and the "corner flow" slip in a 2D case. (h4, h6)

**Set 2**
1. **Missed h4's design-level confounds entirely** — the COVID window (M1) and neighboring-county spillover/SUTVA (M2), the case's two central issues, in favor of off-list points (CI width, heterogeneity, survivorship). (h4)
2. **Case-text misreadings** — h6 F4 (asserts flap-case convergence was not reported when it was) and Q12 (reverses the tunnel-test/wing-revision ordering); h4 F6/Q10 attribute precision and claims ("0.5 points/year", "fixed in advance") the text does not contain. (h6, h4)
3. **Same representativeness/ecosystem gaps plus manufactured doubt** — h5 M3 (seasonal traffic) and M4 (shared pool) missed, and F4's speculative alternate-cause point runs against the grain of the deliberately well-tested control case; h4 M4 (lagged effects) also missed. (h5, h4)

## Overall judgement

The sets are close in aggregate (7 vs 6 of 11 MUST items, zero MUST-NOT violations for either), but their failure profiles differ sharply: Set 1 dominates the causal-inference case by catching the pandemic confound and spillover — the vulnerabilities the case is built around — while Set 2 dominates the simulation case by uniquely catching the single-operating-point issue, though partly offset by two factual misreadings of the case text. I judge **Set 1 marginally better overall**, because its advantage covers the most central items of the hardest case and its case-reading is cleaner; Set 2's tabular falsifier format, however, proved better at surfacing scoped-point checks (h6) and should not be discounted. **Confidence: moderate** — the found/missed calls above follow the key closely, but a handful of borderline judgments (Set 2's h5 M1 "found", both sets' h5 M3 "missed" rather than "partly", and the partial extra-credit award) could each shift one item without changing the qualitative picture.