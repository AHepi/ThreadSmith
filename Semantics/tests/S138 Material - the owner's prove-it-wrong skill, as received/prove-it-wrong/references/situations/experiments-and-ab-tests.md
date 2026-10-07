# Experiments, A/B tests and business results

Use this file for product experiments, growth and retention claims, marketing results, survey findings, pilots, and policy changes measured before and after.

## Typical claims

- "The change raised conversion by 15%."
- "The email improved retention."
- "The pilot worked; roll it out."

## Where the falsifiers usually are

- **Q6 Premise match: no comparison group.** Before and after differ in season, cohort, channel mix, pricing and news. The falsifier: the same period last year shows the same lift, or a holdout that did not get the change shows it too.
- **Q3 Rivals: events at the same time, and spillover.** A launch, a price change, a holiday, a pandemic or a competitor's move in the same window. Compared groups that affect each other: neighbouring regions, shared customers, users in both arms. Ask what would differ if the rival were true.
- **Q10 Order of events: stopping and metrics.** Was the stopping point fixed, or was the test stopped when it looked good? Was the metric chosen before the test? Were other metrics looked at and dropped?
- **Q7 Same question: significance against cause.** A small p-value says the difference is unlikely to be noise. It says nothing about bias in who got the change. Large samples make biased differences very significant.
- **Q9 Draws and size: novelty and regression.** Early lifts fade. Groups picked because they were extreme drift back. The falsifier: the lift shrinks in the later weeks, or in a second cohort.
- **Q1 Scope: rollout beyond the evidence.** One region, one segment, one season. Say where the result was observed, and treat each new place as a new claim.
- **Q5 Worst single case: segments.** An overall lift can hide a loss in a segment that matters: new users, a region, mobile.
- **Q12 Consequences: what else moved.** Unsubscribes, support tickets, refunds, long-term retention.
- **Q4 Same by construction: metric definitions.** A 30-day retention measured on users who have not yet had 30 days. Compare like windows.
- **Q13 What is counted: who is in the numbers.**
  - A survey whose wording or audience changed in the same period.
  - A support bot whose hard tickets were passed to humans and dropped from its numbers.
  - A pilot measured only on the sites that finished it.

  Recount with the excluded items put back.
- **Q7 Same question: proxy metrics.** An offline score or click-through standing in for revenue, satisfaction or retention. Check that the proxy moves with the real outcome.

- **Surveys and user research.** Who answered, compared with who was asked: response bias. Leading wording. A sample of five users stated as a finding.
- **"Studies show".** Which studies were left out? Publication bias and selection among studies. One large trial can outweigh many small ones.

## Mini example

**Claim:** "The new checkout raised conversion 15% (A/B test, p = 0.01)."

**Missing:**
- Was the stopping point fixed in advance (Q10)?
- Were both arms on the same traffic mix for the whole test (Q6)?
- Does the lift hold in week 2 alone (Q9)?

**Next test:** rerun for a fixed, preset length, with the analysis written first.
