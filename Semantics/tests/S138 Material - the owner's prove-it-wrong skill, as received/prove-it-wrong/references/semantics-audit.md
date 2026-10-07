# The semantics audit

This file turns the owner's theory, **Claude Fable Semantics** (revision 1, file 11), into audit checks. Use it when:
- a claim rests on a model, a simulator or a learned part;
- a test design is being audited before it runs;
- the forcing questions leave you unsure which test is missing.

Each check gives:
- the semantics' idea in one plain sentence, with its Part;
- the audit question;
- which forcing question it feeds (see `forcing-questions.md`);
- what a failure looks like.

The semantics is about explanations: what makes an organization of parts an account of a target under a set of admitted changes. A claim of a result is checked the same way. The result is an account of the world only as far as the changes it was tested under reach.

## A1. The contract of admitted changes (Parts III, V: non-vacuity)

- **The idea.** Every claim ranges over a declared set of changes, its **contract**. Every physically possible change left out must be left out by a stated scope, not silently.
- **Audit.**
  - List the changes the tests made.
  - List the changes the world could make that the claim would be expected to survive.
  - Every gap between the two lists is either stated in the claim's scope or a **missing condition**.
- **Feeds:** Q1.
- **Failure looks like:** a guarantee stated without its "only if the world obeys the supplied list"; a contract made only of relabelings, or that leaves out every change under which the claimed part could matter.

## A2. The answer must not be supplied (Part V: non-circular dependence; Part X: ownership)

- **The idea.** The answer must follow from evaluating the account under independent conditions. It may not sit in an input or in a component labelled "law". Work supplied from outside a system's boundary remains an outside contribution, however it is executed inside.
- **Audit.**
  - Draw the boundary: what is the claimed part, and what was supplied (formulas, features, candidates, labels, word-to-moment links)?
  - Find a change that removes or replaces a block of the claimed part while keeping what was supplied. Under it the answer must change, or stop being settled in the claimed way.
  - If no such change exists, the result belongs to what was supplied.
- **Feeds:** Q2, Q3.
- **Failure looks like:**
  - a "learned" readout on features that are already the physics;
  - a score against the variable the estimator was computed from;
  - credit for the system given to work done by its designer.

## A3. The question is fixed (Part III: "the respect is the query"; Part V: question fidelity)

- **The idea.** What a question asks is fixed by its query and its admitted changes.
  - A **production** question intervenes upstream.
  - An **identification** question changes what is observed.
  - The two are different questions, and an answer to one is not an answer to the other.
  - A measure that identifies an outcome, with a reliable prediction from it, does not show that the measured part produces the outcome.
- **Audit.** For each claim, write its question type. Then check that the evidence used changes of that type.
- **Feeds:** Q7.
- **Failure looks like:** prediction accuracy offered for causation; a score offered for capability; a before-and-after difference offered for an effect.

## A4. Parts as well as whole (Part V: conditions F1 and F2; Derivation 9)

- **The idea.**
  - Fidelity is required component by component (F1) and for the assembled whole (F2).
  - Matching outputs can hide a wrong decomposition, and locally right pieces can hide a lost shared constraint.
  - Two systems with the same outputs and different internal routes are different, and no function of the outputs alone can tell them apart (Derivation 9).
- **Audit.**
  - If the claim is about how something works, require a change that reaches inside: one under which the claimed route and a rival route with the same outputs would come apart.
  - If only outputs were tested, the claim is about outputs.
- **Feeds:** Q7, Q12.
- **Failure looks like:** "it works the way we think because the outputs match"; attribution read from logs or emitted text.

## A5. Indistinguishable is identical (Derivation 2; Part II: kinds are edit-signatures)

- **The idea.** Two candidates that respond the same to every admitted change are one thing at that grain. A claim that they "really" differ must name a change that separates them.
- **Audit.**
  - For each pair of arms, controls or measures, ask whether any admitted change separates them.
  - If none does, count them as one. Their agreement is not evidence.
  - If a separating change exists but was not run, they are not yet shown different.
- **Feeds:** Q4.
- **Failure looks like:** five arms that are really four; two columns that are one measurement; a control that reduces to the tie-break rule.

## A6. Provenance: fitted, built, declared (Part IV; Derivations 3 and 4)

- **The idea.**
  - A **selected (fitted)** correspondence is faithful where it was tested.
  - Wherever its population allows a different survivor, its value on an unseen change is not fixed by its history (Derivation 3).
  - Surprise is only possible where the history is smaller than the changes the world allows (Derivation 4).
  - A **constructed (built)** correspondence says something definite about unseen changes, so it can be caught out.
  - A **declared** one is asserted by its author and earns nothing.
- **Audit.**
  - Tag every part that does work as fitted, built or declared.
  - For each fitted part, name an unseen change and a different survivor of the same history that would act otherwise there, then run that change.
  - If the family admits no such survivor, say so: the family then fixes the value, and the family is what must be checked (A1).
- **Feeds:** Q8, Q1.
- **Failure looks like:** a predictor fitted in one regime trusted in another; a "learned" law that is really declared.

## A7. Receipts (Part IX)

- **The idea.**
  - An evidence leaf is a reference to an event with an interpreted claim. A receipt is a derivation from such leaves.
  - Missing evidence stays missing.
  - A record reconstructed from the claim it is meant to support is not a receipt for that claim.
  - A later record derived from a carrier is not a second, independent witness to it.
- **Audit.**
  - For each "checked", trace it to an event: what ran, when, what it printed.
  - Reject records written from the claim.
  - Reject counting copies of one record as several witnesses.
- **Feeds:** Q11, Q9.
- **Failure looks like:** "verified (see log)" where the log was written by the claimant; a rerun of the same seed counted as replication; a check described as done before it ran.

## A8. What a failed test refutes (Part IX, K3)

- **The idea.** A test of T together with background B and instrument I refutes only the bundle (T and B and I). It does not single out T.
- **Audit.** When a falsifier fires, say which of the theory, the background or the instrument you are changing, and why that one. When a falsifier does not fire, ask whether the instrument could have fired at all.
- **Feeds:** Q4, Q10.
- **Failure looks like:** dropping the claim when the probe was broken; keeping the claim by blaming the probe without checking the probe.

## A9. Moving goalposts and historical index (Part III; Part VIII; Derivation 7)

- **The idea.**
  - An assessment is fixed to its contract. A narrowing adopted after a failure is a new claim at a new index.
  - Changing the index without recording the change is a failure of the record.
- **Audit.** Compare the claim, metric, scope, stopping rule and comparison with the ones fixed before the results. Each difference becomes a separate, newer claim, and the old one stays as it was.
- **Feeds:** Q10.
- **Failure looks like:** a metric changed mid-test; "we meant only X" after X failed elsewhere; a post-hoc analysis presented as the planned test.

## A10. Repairs and what they protect (Part XI)

- **The idea.**
  - A repair fixes a stated obligation while protecting stated others.
  - Losses outside the protected set must be exposed.
  - A correct account that produced nothing, a repair made without an account, and a repair produced through an account are three different things.
- **Audit.**
  - For any fix, list what it was meant to repair and what it must protect, and check each protected item after the fix.
  - Ask whether the fix was produced by the claimed explanation, or would have been made anyway.
- **Feeds:** Q12.
- **Failure looks like:** a fix that removes a feature; a fix credited to a root cause it does not test.

## A11. Adding a part can break the whole (Part VI: interference)

- **The idea.** Success of a subset does not imply success of the whole. An added part can destroy a support that worked without it.
- **Audit.** When a claim adds a part (a module, a feature, a rule), test the whole with and without it, not only the new part alone.
- **Feeds:** Q3, Q12.
- **Failure looks like:** a new component tested alone and declared safe to integrate.

## A12. A finite list is not a barrier proof (Part XIII)

- **The idea.** A finite list of failures does not prove something cannot be done; one bypass refutes a proposed barrier. In the same way, a finite list of successes does not prove "always".
- **Audit.** For any "cannot" or "never", ask what one bypass would look like, and whether anyone looked for one.
- **Feeds:** Q5, Q9.
- **Failure looks like:** "no learner could tell them apart" from one classifier's 54%; "never happens" from a short trial.

## How this differs from hard-to-vary

The hard-to-vary skill asks whether each part of an explanation is held in place. This skill asks whether each claim met the observations that could have sunk it. They share A4 to A6. Use both on an explanation that is also offered as a tested result.
