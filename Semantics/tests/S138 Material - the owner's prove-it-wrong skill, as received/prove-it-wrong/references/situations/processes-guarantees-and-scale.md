# Processes, guarantees, durability and scale

Use this file for:
- claims about a human process (a checklist, training, a review step);
- a supplier's, library's or platform's guarantee;
- claims that something lasts ("fixed for good", "persists at six months");
- claims that a pilot's result will hold at scale;
- compliance and quality-control sign-offs.

## Typical claims

- "The checklist ended mislabelling."
- "The queue guarantees at-most-once delivery, per the docs."
- "The fix is permanent."
- "The pilot's unit costs hold at scale."
- "The audit found no violations."
- "The part passed incoming QC."

## Where the falsifiers usually are

- **Q11 Receipts: self-report against observation.**
  - That staff say they follow a process is a claim.
  - Observe worked samples blind, or audit unannounced, using someone who did not write the process.
- **Q2 Supplied answer: a guarantee taken from documents.**
  - "Per the docs" is the supplier's claim.
  - Run a hostile test on your own version and setup: duplicates, reordering, a crash mid-delivery, a network split.
- **Q1 Scope: an audit of documents, not practice.**
  - A compliance audit that read the written policy, not the records or the front line.
  - A QC pass on a pilot or demo batch rather than the production line (also Q13).
- **Q8 Unseen changes: time.**
  - "For good" and "persists" need a retest after a stated longer window, or a long soak run.
  - Look for delayed side effects that only appear later.
- **Q1 and Q8: scale.**
  - A pilot's numbers do not say where the first resource saturates.
  - Run at several times the load, and find the breakpoint in cost or performance, rather than extrapolating from one point.
- **Q13 What is counted: the boundary.** A footprint, cost or risk figure inside a narrow boundary, such as direct emissions only, excluding suppliers, equipment or disposal. Say what the boundary leaves out, and whether that could reverse the result.
- **Q6 Premise match: who measures.** A person or team measuring a change they want to work, with nothing blinded. Self-experiments are the extreme case.

## Mini example

**Claim:** "After the new review checklist, mislabelled shipments fell to zero last month."

**Missing:**
- Who counted the mislabels, and did the counting change (Q11, Q13)?
- Was last month's volume or product mix unusual (Q6)?
- Is one month enough at the old error rate (Q9)?

**Next test:** an unannounced audit of 200 shipments by someone outside the team, compared with the old error rate.
