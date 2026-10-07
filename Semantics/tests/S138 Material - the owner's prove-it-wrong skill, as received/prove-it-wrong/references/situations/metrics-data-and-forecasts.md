# Metrics, data pipelines and forecasts

Use this file for:
- dashboard numbers;
- operational metrics (time to fix incidents, resolution time, satisfaction scores);
- match rates and data joins;
- forecasts and backtests;
- "no difference" or "just as good" claims.

## Typical claims

- "Time to fix incidents fell 40%."
- "Live accuracy is 95%."
- "The forecast is 90% accurate."
- "We matched 96% of orders to users."
- "The rewrite is just as fast."
- "Revenue per user rose."

## Where the falsifiers usually are

- **Q4 Same by construction: the instrument itself.**
  - Does the pipeline record what it claims to? Inject synthetic events of known size and confirm they appear, correctly sized.
  - A metric whose collection changed (new logging, new sampling) cannot be compared across the change.
- **Q13 What is counted: censoring and silent drops.**
  - Items lost to timeouts, filters, deduplication or escalation to humans vanish from the denominator.
  - Recount with them back in, and report how many there were.
- **Q2 Supplied answer: look-ahead leakage.**
  - A forecast or backtest that uses data not available at the moment of prediction (revised figures, features computed over the whole period) scores well by construction.
  - Rerun strictly out of time, with each prediction using only what was known then.
  - Audit each feature for when it becomes known.
- **Q5 Worst single case: mix shift.**
  - An average can rise while every segment falls, if the mix of segments changes (Simpson's paradox).
  - Split the change into within-segment change and mix change, and check the largest segments separately.
- **Q9 Draws and size: "no difference" is not "the same".**
  - An equivalence claim needs a margin fixed in advance ("within 5%") and enough data to rule out differences beyond it.
  - Failing to find a difference with too little data shows nothing.
- **Q7 Same question: match rates.**
  - "96% matched" says how many got a match, not how many matches are right.
  - Hand-audit a random sample for false matches.
  - Confirm known non-matches stay unmatched.
- **Q10 Order of events: metric redefinitions.** Check the metric's definition history across the compared periods. Checking it can feel like someone else's job.
- **Q4: the raw data's sanity.** Before trusting a headline number, look for duplicates, impossible values, out-of-order timestamps, and unit or dimension errors.

## Mini example

**Claim:** "The new matching job links 96% of orders to customers, up from 81%."

**Missing:**
- Were false matches counted? Hand-audit a random 200 (Q7).
- Did the rise come from looser matching rules (Q4, Q10)?
- Were unmatchable orders filtered out before counting (Q13)?

**Next test:** hand-audit 200 random matches from each version and compare the false-match rates.
