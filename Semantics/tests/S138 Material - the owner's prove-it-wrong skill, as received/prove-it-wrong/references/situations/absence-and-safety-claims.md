# Absence, safety and "cannot" claims

Use this file for claims that something does not happen or cannot happen:
- "No side effects."
- "No security holes found."
- "This cannot fail."
- "No learner could tell these apart."
- "It never happens in production."

## Why these are special

An absence claim is easy to "confirm" by not looking hard. Its strength depends entirely on how hard the search was, and on whether the search could have found the thing.

## Where the falsifiers usually are

- **Q9 Draws and size: search power.** How many cases were examined, and how likely was the search to find the thing if it was there? Zero events in 100 trials is weak for a 1-in-1,000 event. State the rate the search could have detected.
- **Q4 Same by construction: a probe that could not fire.** Run the search on a planted instance, a known vulnerability or a seeded bug, to show it can find one. A search that misses a planted instance shows nothing by finding nothing.
- **Q5 Worst single case: the strongest attempt.** "No learner could tell them apart" from one weak classifier is a claim about that classifier. Try the strongest available method, or one built for the purpose.
- **Q1 Scope: the conditions searched.** Absence in tested conditions says nothing about untested ones. List what was outside the search.
- **Q2 Supplied answer: the same instrument.** A fix checked only by the scanner that flagged it. Check the attack path itself.
- **Q8 Unseen changes: adversaries and drift.** For security and safety, the world adapts. A defence tested against yesterday's attacks says nothing about tomorrow's.
- **Q9 Draws and size: "no difference" or "just as safe".** An equivalence claim needs a margin fixed in advance and enough data to rule out differences beyond it. Failing to find a difference is not finding none.
- **Missing evidence stays missing.** "Not found" means unknown unless the search is shown able to find it.
- **A finite list is not a barrier proof.** One counter-example refutes "cannot". Ask what a bypass would look like, and whether anyone looked for one.

## Mini example

**Claim:** "The security scan found no vulnerabilities, so the service is secure."

**Missing:**
- Does the scanner find a planted known vulnerability in this service (Q4)?
- Which parts were outside the scan: authentication flows, configuration, dependencies (Q1)?
- Was the strongest available method used, such as a manual review of authentication (Q5)?

**Next test:** plant one known vulnerability in a copy and rerun the scan.
