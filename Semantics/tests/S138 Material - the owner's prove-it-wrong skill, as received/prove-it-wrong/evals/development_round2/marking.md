# Heldout marking key

Written before seeing any reviewer answers. Not to be edited afterward.

Common MUST-NOT items, apply to every case below in addition to the case-specific list:
- X1: states outright that the claim is true or false when the reported evidence cannot settle that.
- X2: asserts a test was run or a result obtained that the case text does not report.
- X3: more than a third of the listed points are generic ("check the methodology", "get peer review") with no specific link to this case's facts.
- X4: demands a test that is impossible even in principle (e.g. a randomized trial of history, infinite follow-up, zero-variance replication) as though it were a required gate.

---

## case_h1 — battery pack validation (engineering/hardware)

MUST:
- Question whether 500 cycles is enough to support "longevity"/mass-production sign-off claims for a product whose real-world lifetime (daily e-bike use over years) likely implies several times that many cycles; the test stopped at 500 with no stated target cycle life for end-of-use.
- Question the single ambient test condition (23°C lab climate control) given the pack is "rated for outdoor consumer use across four seasons" — no hot-climate (e.g. 40°C+) or cold-climate (sub-zero) charge/discharge data is reported, yet thermal/capacity behavior is strongly temperature-dependent.
- Question the absence of any abuse/safety-specific testing (short-circuit, puncture, crush, overcharge, drop) before accepting a "meets our internal safety... targets" claim — the described tests are cycling/thermal-under-normal-use only, not safety-fault testing.
- Question whether n=5 units from one production run is sufficient to rule out manufacturing/cell-batch variance at scale; ask for sample size justification or multiple production batches/lots.

MUST-NOT (case-specific):
- Must not accept the "safety" conclusion as supported by the cycling data alone (that data speaks to longevity/thermal performance under normal cycling, not to safety-fault tolerance).
- Must not treat "no fault codes in BMS logs" as equivalent to "no unsafe failure modes exist" — that is evidence of absence only within the conditions tested.
- Must not invent specific numeric standards (e.g. "UL 2271 requires X") not mentioned in the text and then grade the case against them as if cited.

---

## case_h2 — XR-14 rheumatoid arthritis trial (medicine/public health)

MUST:
- Question the mismatch between the trial's narrow enrollment (ages 18-65, no cardiovascular disease, no hepatic impairment, no concurrent biologics, urban academic centers only) and the sponsor's intended "broad label covering adult patients" — safety/efficacy in excluded groups (elderly, comorbid, rural/community-care populations) is untested.
- Question whether 12 weeks of follow-up is adequate to claim a durable hospitalization-rate benefit and an acceptable long-term safety profile for a chronic disease typically treated for years.
- Question the robustness of the headline comparison given the likely small absolute event counts behind 3.1% vs 7.8% of ~412 patients (roughly 6 vs 16 hospitalizations) — ask whether this was pre-specified as a primary endpoint or is one of several outcomes examined, and whether the effect survives multiplicity/sensitivity checks.
- Question how hospitalization was ascertained and whether outcome assessment was blinded, since the case states blinding/randomization were "sound" but does not describe blinded adjudication of the hospitalization endpoint specifically.

MUST-NOT (case-specific):
- Must not accept the recommendation for "rapid adoption" and a "broad label" as supported, since the tested population is narrower than the proposed label — but must not declare the drug "unsafe" or "ineffective" either; the issue is scope, not refutation.
- Must not fabricate missing numbers (e.g., inventing an actual death count or dropout rate not given in the text).

---

## case_h3 — Athena-7B benchmark claim (machine-learning evaluation)

MUST:
- Question whether the training corpus (public web crawls) was screened for contamination/overlap with MMLU and GSM8K items; a 2.1T-token web crawl plausibly contains benchmark text, and no decontamination procedure is mentioned.
- Question whether the comparison to Mistral-Lux-7B's 85.1%/71.0% figures was obtained by re-running that baseline under the same harness/prompting setup used here, or merely copied from the other model's own report (different shot counts, prompt templates, or harness versions can shift scores by several points).
- Question the narrowness of the evaluation: only two benchmarks (both well-known, static, and widely gamed) are reported, with no held-out/contamination-resistant or more recent benchmark, and no qualitative/human evaluation of failure modes.
- Question the variance reporting: the three repeated runs vary only prompt ordering, not seed, decoding temperature, or benchmark version, so the reported ±0.3/±0.6 understates the true uncertainty relevant to the "comfortable margin" claim.

MUST-NOT (case-specific):
- Must not conclude the model is or is not actually state-of-the-art in absolute terms — the evidence as reported cannot rule out contamination or baseline mismatch, so it must be flagged as unresolved, not adjudicated either way.
- Must not demand the reviewer obtain insider information about the baseline model's training data (impossible to verify) — the correct ask is for the authors to run/report their own decontamination check, not for the reviewer to prove contamination occurred.

---

## case_h4 — minimum wage and teen employment (social science/economics)

MUST:
- Question the 2019-2023 window: it spans the COVID-19 pandemic, which caused massive, uneven disruption to retail/food-service employment independent of minimum wage policy, and the case gives no indication this confound was addressed (e.g., excluding or separately modeling 2020-2021).
- Question the "neighboring counties" comparison group for spillover/contamination: workers or employers can move across adjacent county lines in response to the wage differential, which would bias the diff-in-diff toward finding no effect (violates the no-spillover/SUTVA assumption) — ask whether this was tested (e.g., with non-adjacent comparison counties).
- Question the outcome measure: only teen employment *levels* in two sectors are examined; hours worked, hiring rates, job turnover, prices, or firm exit/entry are not reported, any of which could show effects the employment-count measure misses.
- Question whether the post-treatment window is long enough to detect lagged effects (e.g., automation investment, gradual staff reduction) that often emerge over a longer horizon than captured here.

MUST-NOT (case-specific):
- Must not state the minimum wage increase "had no effect" or "did have an effect" on employment outright — the reported design, with the pandemic-era confound and spillover risk, cannot settle the causal question as presented.
- Must not demand a randomized experiment assigning minimum wage laws to counties (not feasible/legal) as if that were a realistic missing test.

---

## case_h5 — payment-gateway retry storm post-mortem (software operations) — WELL TESTED

This is the case meant to be mostly confirmed. A good reviewer should recognize the breadth of testing already done (incident reproduction via fault injection, load test at 3x peak, multi-region canary with automated rollback, full regression suite, circuit-breaker recovery test) and should not ask for these to be redone or treat the claim as weak.

MUST:
- Note that the testing performed directly targets the actual failure mode (latency-spike-induced retry storm) and credibly rules out recurrence of *that* specific scenario — this should be stated as a genuine strength, not hedged away.
- Identify at least one real remaining scope limit, e.g.: the fix was validated against a slow-upstream (high-latency) failure mode, but not against an upstream that fails fast with errors (e.g., HTTP 500s) rather than timing out, which could exercise the retry/circuit-breaker logic differently.
- Identify that the 48-hour, 5%-traffic canary window, while reasonable, does not cover longer-tail or seasonal traffic patterns (e.g., a monthly billing spike or holiday peak) beyond the tested 3x-peak synthetic load.
- Identify that the fix was evaluated in isolation for the payment-gateway client; whether other clients/services sharing the same connection pool or downstream dependency were checked for compounding effects during a simultaneous incident is not stated.

MUST-NOT (case-specific):
- Must not characterize this claim as weakly supported, under-tested, or in need of its core tests (fault injection, load test, canary, regression suite) being redone — doing so is a scoring error for this case specifically.
- Must not invent a dramatic unaddressed failure mode contradicted by the text (e.g., claiming "they never tested in production" when a canary rollout to real traffic is explicitly described).

---

## case_h6 — CFD airfoil flap simulation (physics/simulation)

MUST:
- Question the absence of a mesh/grid convergence study: only one mesh density (1.2M cells) is reported; convergence of residuals within that single mesh does not establish that the 14% L/D result is independent of mesh resolution (a standard grid-refinement/Richardson-extrapolation check is missing).
- Question the validation scope: the solver was validated against wind-tunnel data only for the baseline, unflapped airfoil at one Re/AoA — it was never validated against any experimental case with a deflected flap, where flow separation near the flap hinge is common and RANS/k-ω SST is known to be less reliable.
- Question the single operating point: the 14% improvement is reported at one Reynolds number and one angle of attack only; no sweep across the AoA range (including near stall, where flap-induced separation is most likely) or across other Reynolds numbers relevant to the actual flight/operating envelope is presented.
- Question turbulence-model suitability for the flapped geometry specifically: k-ω SST accuracy for attached, mild-pressure-gradient baseline flow does not guarantee accuracy for the higher-gradient, potentially separated flow around a 10° deflected flap.

MUST-NOT (case-specific):
- Must not declare the predicted 14% L/D gain "confirmed" or "wrong" — the authors themselves propose wind-tunnel testing as the next step, and the reviewer should treat the simulation as suggestive pending that validation, not settled either way.
- Must not fault the authors for not already having wind-tunnel data on the flap (they explicitly say that is the planned next step) — the valid criticism is the missing convergence/validation/sweep work that should precede or accompany committing to build a physical prototype, not the absence of physical testing itself.

---

Fields used: engineering/hardware (battery pack), medicine/public health (RA drug trial), machine-learning evaluation (Athena-7B benchmarks), social science/economics (minimum wage study), software operations (payment-gateway post-mortem), physics/simulation (CFD airfoil flap).

---

## Amendments adopted before grading (6 October 2026)

An outside audit (GLM) reviewed this marking key against the case texts before any reviewer answers existed. All ten of its recommended amendments were checked against the case text and adopted; none were rejected. The original MUST / MUST-NOT lists above are left unedited; the amendments below govern grading alongside them.

**Adopted:**

1. **h1 — amend M4** to: "Question whether n=5 units suffices to rule out manufacturing/cell-batch variance (batch/lot provenance is not stated in the text); ask for sample-size justification or multi-lot sampling." (The original M4 wrongly assumed the text states the five units came from one production run; it only says "five production-line units.")
2. **h1 — add extra credit** (not required, but should be credited if raised): vibration/mechanical and water/dust-ingress (IP) durability for an outdoor pack; calendar-aging (storage) fade. Neither is covered by M1–M3.
3. **h2 — add extra credit**: dropout/attrition and missing-outcome handling are not reported anywhere in the case text.
4. **h3 — reword M4's rationale** to: "the ±sd reflects only prompt-ordering variance and cannot by itself support the 'comfortable margin' claim, since harness/version differences and baseline-measurement variance (M2) shift scores by points." Drop "seed, decoding temperature" — MMLU/GSM8K evaluation is standardly deterministic/greedy, so demanding variation along that axis is off-target.
5. **h3 — extend M2 (add M5)**: "Since weights and evaluation scripts are stated to be released, the decisive check is re-running Athena-7B *and* Mistral-Lux-7B under one identical harness configuration; noting this feasibility counts as MUST, not extra credit."
6. **h4 — soften M1** to: "acknowledge the reported state-level growth controls, but ask for pandemic-specific checks (excluding or separately modeling 2020–21; county-level pandemic severity), since COVID disruption was uneven at county/sector level." (The original M1 overstated the gap: the text does report state-level growth controls as a robustness check.)
7. **h4 — add grader note to M2**: the text's "robustness to alternative comparison groups" does not by itself address adjacency/spillover; only answers that specifically press for non-adjacent comparison groups or a spillover test satisfy M2, but a reviewer who acknowledges the reported robustness check while still asking this must not be penalized for failing to ignore it.
8. **h4 — add extra credit**: endogenous adoption (the 14 treated counties self-selected into the $15 policy; two years of pre-trends does not fully rule out selection on unobservables/anticipated trends).
9. **h5 — expand the "remaining scope limit" example list** (satisfying the MUST that asks for at least one real remaining limit) to also accept: the rollback machinery was configured but never exercised ("no rollback triggered"); payment-semantic correctness of degraded mode (cached responses in a payment flow could mislead about payment status, not just serve stale content); "no recurrence" rests on a short (~2-week) post-rollout window.
10. **h6 — merge M4 into M2**: treat as one item (baseline-only wind-tunnel validation plus k-ω SST's known unreliability for separated flow, both pointing at the same gap for the deflected-flap case) — a reviewer who makes either observation satisfies both; do not require it twice or double-penalize for stating it once.
11. **h6 — add extra credit**: 2D-section-to-3D-wing extrapolation, given the stated next step is "integration into the next wing revision"; whether 3% baseline agreement is enough to trust a 14% delta, noted as largely subsumed by M2 and so extra credit at most.
12. **Common X1 — append clarifying parenthetical**: "(X1 does not bar crediting well-supported claims — see h5 M1.)" This prevents a grader from treating a correct affirmation of a claim that the evidence *can* settle (as in the h5 control case) as an X1 violation, which only applies when the evidence *cannot* settle the claim.

**Rejected:** none. All ten recommendations were checked against the case text and found accurate and fairness-improving; none introduced a requirement unsupported by the text or softened a point that the text does not actually support softening.
