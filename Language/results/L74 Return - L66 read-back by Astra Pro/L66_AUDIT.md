# L66 — report-only audit

**Auditor:** ChatGPT  
**Date:** 22 September 2026  
**Material:** the reader brief and reports P01–P18, including the supplied consequence and single-line-removal outputs.

## Verdict

**The bundle does not fully meet its own read-back contract.** Several local findings can be stated plainly, and some have explicit sentence references. But a reader cannot consistently recover the source sentences, distinguish an unexercised check from a successful one, or tell a newly inferred commitment from a different encoding of an existing statement.

The most consequential issue is in **P14**: an unsupported causal link is rejected as a production explanation, yet the asserted dependency is used to remove the effect in a counterfactual that receives a positive verdict. That can be a legitimate check of consistency with an assumed model. It is not independent support for the model, and the report needs to say which job it has performed. [P14, lines 7–13](sources/P14.md)

This is an audit of what the reports communicate, not a verdict on the original writers, biological theories, historical claims, or the correctness of unavailable software. The bundle explicitly withholds passages, ledgers and rules. There are no executable checkers in the supplied archive. [Reader brief](sources/READ%20ME%20FIRST.md)

## 1. The question and the evidence boundary

**Frozen question:** Can a reader, using only the supplied printed reports, recover what was found, where it was found, what unstated commitments follow, and what remains unclear?

The jobs below come from the brief, rather than being requirements invented to make the system fail:

| Job | Origin | Required contrast |
|---|---|---|
| J1. State each finding plainly. | Given | A concrete finding, not merely a diagnostic label or a judgment about the writer. |
| J2. Identify the source sentence. | Given | A source sentence number, not just an internal ledger identifier. |
| J3. Recover unstated consequences and their support. | Given | A new commitment, not a restatement; source support, not an unexplained list of letters. |
| J4. Identify uncertainty and a sentence that would resolve it. | Given | An explicit limit, not a guessed completion. |
| F1. Use reports only; do not assess whether the writer is right. | Fixed | Read-back, not reconstruction from outside knowledge. |

The withholding of source materials is an intentional test condition, not itself a fault. A self-contained report must therefore supply whatever source anchors and operational definitions are necessary for these jobs.

**Evidence labels used here:** *Observed* means text inspected directly. *Reported* means an outcome asserted by the supplied checker or consequences output, not independently rerun. *Inferred* means an audit conclusion from that text. *Not tested* means the required execution, source, history or independent reader evidence is absent.

P01–P04 were inspected before fixing the expectations in [the audit protocol](audit_protocol.md). P05–P18 were then inspected without changing those criteria. This was not a blind reader study, and these reports are not established as unseen cases for L66 itself. No performance or correctness score is inferred from them.

## 2. Findings

### A. Source attribution is not consistently recoverable

**Observed.** P01 identifies failed links by `g` and `s`, and their endpoints by other ledger letters. The removal output explains the letters' content, but does not provide a complete line-to-sentence map. P11 and P14 list consequences supported by `m,n`, `m,o` and `m,p` without attaching those premises to source sentences. [P01, lines 7–20 and 30–68](sources/P01.md); [P11, lines 23–26 and 53–65](sources/P11.md)

There are genuine counterexamples to a blanket criticism: the what-if headings in P11 and P14 explicitly identify **sentence 8**; P13 identifies **sentence 2**; P16's gauge connects plan `b` with **sentence 3**. These are usable anchors. [P11, lines 9–11](sources/P11.md); [P13, lines 9–13](sources/P13.md); [P16, lines 9–12](sources/P16.md)

**Inferred.** The missing element is not more reasoning terminology. It is a dependable mapping from every finding and supporting premise to the quoted source span. A reader may sometimes infer a topic's location from an exclusion note, but cannot safely turn a plausible location into an exact attribution.

**Removal and substitution.** Consistently replacing `g` with `claim_17` changes no meaning. Replacing an exact sentence anchor with an unmapped letter destroys J2. The identifier's spelling is a free choice; the source association is necessary.

**Repair.** Print the sentence number, short source quotation, ledger identifier and interpretive status beside every finding and premise. Do not make the reader recover the map from the exclusion appendix.

### B. The clean header does not disclose which checks succeeded

**Observed.** P13 opens with “NO FAULT FOUND in the lines that were checked” and subsequently says that its what-if fails. P16 uses the same clean header before saying it cannot tell whether the proposed plan can work. These can be different classes of check, but the header does not name that distinction. [P13, lines 7–11](sources/P13.md); [P16, lines 7–10](sources/P16.md)

P04 supplies a particularly weak basis for a reassuring summary: its gauge says zero lines were “said” and five were “filled in”; its consequences section reports no directly stated facts, no found facts, and no derived facts. Every printed single-line removal leaves that output unchanged. The report does not identify the successful checks or whether they encountered eligible targets. [P04, lines 7–9 and 21–37](sources/P04.md)

**Inferred.** The wording is not necessarily a false statement. It is an underspecified result: “no diagnosed fault,” “no eligible instance,” “not evaluated,” and “test passed” are different answers. J1 requires the report to distinguish them.

**Important qualification.** Zero newly derived facts does **not** prove that no inference was executed. A rule may derive something already explicitly stated. P01's copying rule, copied-gene fact and explicit selected-gene claim illustrate why novelty and rule execution must be kept separate. [P01, lines 26–34 and 65–66](sources/P01.md)

**Repair.** Replace the umbrella header with named check outcomes: checked and passed; checked and failed; not checked; or no eligible target. Keep these separate from a summary of coverage.

### C. The exclusion gauge is useful, but its sentence count is not a coverage partition

**Observed.** P09 says eleven of eleven sentences went to the leftover bin, while also reporting twenty-six “said” lines and two checked causal links. Its bin entries often identify excluded fragments, not an entirely discarded sentence. P02 similarly lists all seven sentences in the bin while retaining several facts. [P09, lines 7–13](sources/P09.md); [P02, lines 7–9 and 14–34](sources/P02.md)

**Inferred.** “Every sentence has an excluded fragment” and “no sentence was checked” cannot be treated as equivalent. The printed count does not establish the proportion of an argument that was tested. I have not interpreted these gauges as percentages of wholly unchecked prose.

The gauge does valuable work: it exposes omitted probability, quantity, modality, timing and metaphor, and repeatedly refuses to replace qualified claims with stronger unconditional ones. Removing that disclosure would conceal the limits of the result. However, the decisive support for a conclusion may be in an excluded fragment even when surrounding facts remain represented. P01 explicitly leaves the mathematical and probabilistic support around sentence 6 unexecuted. [P01, line 22](sources/P01.md)

**Repair.** Distinguish fully represented sentences, partially represented sentences, and unrepresented sentences. More importantly, identify which conclusion-supporting steps were unrepresented. Where a missing bridge is reported, state whether it is absent from the passage, absent from the chosen ledger, or present in material that this language cannot express. Only the second is established by the current “nothing in the ledger” wording.

### D. P14's counterfactual pass depends on a causal assertion the report does not justify

**Observed.** P14 says that even granting group structure, no recorded production route yields the spread of helping. It then removes group structure, sets aside the spread of helping because the ledger says it came from the changed item, and declares the prediction that helping stops to hold. [P14, lines 7–13](sources/P14.md)

The consequence listing identifies the dependency as reconstructed line `h`: “line g BECAUSE line f.” That listing says deleting `h` changes none of the reported facts. Thus the fact-removal display and the counterfactual procedure are tracking different kinds of consequence. [P14, lines 38–47](sources/P14.md)

**Inferred.** The dependency is insufficient for one stated purpose—establishing production—but still operative for another—deciding which assertions to withdraw. This can be internally coherent under an assumption-relative policy. The report does not give enough information to read its positive verdict as anything stronger.

P11 provides the useful nearby comparison. There the causal link is denied, helping is retained, and the opposite counterfactual—helping continues without group structure—holds. This is **not** a demonstration that the checker accepts opposite results with identical inputs: the causal assertions and the status of the spread premise differ. It instead shows why the accepted dependency model must be printed as part of the result. [P11, lines 9–14 and 39–48](sources/P11.md)

**Unsettled.** The bundle does not provide the intervention rules, proof traces or recomputed positive and negative query states. I cannot establish whether the system distinguishes an explicitly false proposition from one that is no longer derivable, or whether accepting unvalidated causal links is deliberate. This is not a demonstrated implementation bug.

**Repair.** A defensible replacement for the P14 success statement is: “The encoded counterfactual is satisfied after withdrawing the effect using causal dependency h, which the production check above did not establish.” Also state whether the query is false, unsupported or contradicted after the intervention. “Spread stops” should not silently stand for the weaker condition “spread is not retained”; the gauge itself says stopping time is not modelled.

### E. Formal novelty is not the same as an unstated commitment

**Observed.** P10 lists `depends_on(our_bliss,blamed_conditions)` as derived and “not stated by any line.” Its sole supporting line `g` already reads, in plain language, “our bliss DEPENDS ON the conditions we blame.” Removing `g` removes both `depends(...)` and `depends_on(...)`. [P10, lines 14–17 and 32–34](sources/P10.md)

**Inferred.** The printer may be accurately identifying a new internal atom. It is not thereby identifying a new proposition the writer left unsaid. At the level of the reader's requested paraphrase, the printed premise and consequence state the same dependency unless an additional semantic distinction is supplied.

P11 and P14 offer a different pattern: a general rule `m` plus three cooperation-spread instances yields three group-selection claims. Those are intelligible conditional consequences of the encoded rule, not independent evidence for it. In both reports the rule is explicitly marked “filled in,” which must travel with the conclusions. [P11, lines 23–26 and 53–65](sources/P11.md); [P14, lines 22–25 and 52–64](sources/P14.md)

P13's “the void yields” is a further boundary case: it instantiates the printed general yielding description at the item classified as void. A reader needs to know whether this is a new commitment, an instance of an already stated universal, or just a reporting normalisation. [P13, lines 33–34 and 49–54](sources/P13.md)

**Repair.** Separate “restated in another notation,” “instance of a general claim,” and “additional consequence.” For each, print whether the supporting premise was explicit, interpretive, assumed or supplied by a rule. Do not use machine-level novelty alone to answer J3.

### F. A zero single-line delta does not establish that the line does no work

**Observed.** P09 says both `c` and `y` assert that void exists. Removing either one alone changes nothing. Each can cover for the other. [P09, lines 34–35 and 78–79](sources/P09.md)

P01 supplies the more instructive version: `a` gives the faithfully-copied-to-selected rule, `b` says the gene is faithfully copied, and `r` explicitly says genes are selected. Both removal of `a` and removal of `r` leave the reported fact set unchanged. The printed meanings reveal two candidate support routes: direct assertion `r`, or rule `a` with fact `b`. [P01, lines 31–34 and 65–66](sources/P01.md)

**Inferred.** Before calling either route unnecessary, remove both. The expected loss under joint removal is a report-based deduction to test, not an execution I performed. These examples also show why zero novel conclusions and zero single-line deltas cannot be used as measures of explanatory inactivity.

P14 adds a different limitation: deleting a relation may leave the fact set unchanged while changing which effects an intervention procedure withdraws. A fact-only delta is not a complete account of dependency.

**Repair.** Say “no change in the reported fact set,” not an unqualified “nothing changes.” Provide alternative support sets or selected group removals, and distinguish changes to facts, diagnostic results and counterfactual verdicts. Do not rank explanatory importance by the total number of lost output lines.

### G. Causal categories and unsupported verbs need their operating meanings beside the verdict

**Observed.** P03 says its `MAKES` reading requires an unstated condition that the remedy was not already heading toward the stated result. The report does not show the rule that imposes this condition. P13 explicitly declines to check the motion-producing event because `bears` lacks a recognised shape, yet both rigs reject the no-swerve/no-fall counterfactual. [P03, lines 17–18](sources/P03.md); [P13, lines 20–24](sources/P13.md)

P09 lists `pass` and `yield` as verbs without shape; P07 leaves the causal `PRODUCED` event without a shape in its exclusion note. These are concrete limits of the representation, not evidence that no causal relation exists in the passage or world. [P09, line 20](sources/P09.md); [P07, line 22](sources/P07.md)

**Inferred.** A reader can report the checker convention, but should not turn it into a universal claim about what causation requires. Likewise, a failed what-if with an unchecked producer needs the actual retained-premise or counterexample trace. P13's printed downward-motion fact is a possible source of the result; the report does not print the recomputed witness.

**Repair.** Define the relevant category in one sentence and attach a worked trace or explicit scope note. Preserve the distinction between “not represented,” “represented but unsupported,” and “contradicted in the encoded case.”

## 3. What is doing useful work, and what is not

The statuses below concern the reporting jobs, not the truth of the source passages. **Held** means a stated reader job needs the part; it does not mean the present implementation fulfils that job. **Held if** names an unresolved dependency. **Loose** means an alternative would serve as well. **Two routes** identifies substitutable support. **Idle** means removable for these reader jobs. **Unknown** means the required test is unavailable. No statuses are added into a score.

For provenance, **asserted here** means that the functional commitment or metadata is supplied by the brief/report; it is not a claim that the original system was developed only by assertion. Its construction, fitting and validation history is not supplied.

| Part | Status and concrete test | Scope | Dependency | Provenance |
|---|---|---|---|---|
| Withholding passages, ledgers and rules | Not assessed; this is the test condition, not a defect. | Owner-fixed / outside test | Reader-test design | Asserted here |
| Exact finding and premise source anchors | Held jointly with the finding content by J2/J3; replace an anchor with an unmapped letter and source recovery fails. Their provision is incomplete. | In test | Source-to-ledger mapping, not independently verified | Asserted here |
| Concrete endpoints and support-versus-production wording | Held jointly for J1; swapping an epistemic gap for a production gap changes the finding. | In test | Chosen interpretation of the passage | Asserted here |
| “Said” versus “filled in” labels | Held for J3's attribution; erasing the labels hides the status of rule m in P11/P14. Correct assignment of labels is unknown without the source. | In test | Mapper's provenance assignments | Asserted here |
| Generic clean header | Loose; named check outcomes can replace it without losing a reader job and with less ambiguity. | In test | Check inventory, currently not printed | Asserted here |
| Exclusion disclosure | Held for J4; deleting it hides important limits. Sentence-hit count is loose as a measure of whole-sentence coverage. | In test | Representational scope and counting policy | Asserted here |
| P10 atom novelty as textual novelty | Loose; a different predicate name gives the same plain proposition. Semantic equivalence, not the spelling, matters to J3. | In test | Unprinted meaning of normalisation rules | Asserted here |
| P14 counterfactual as an established causal conclusion | Held if causal dependency h and intervention semantics are justified; those dependencies are unknown here. The weaker assumed-model result remains reportable. | In test | Causal interpretation and intervention rules | Asserted here |
| P09 existence support; P01 selection support | Two routes: P09 c or y; P01 r or a with b, at the level of the printed meanings. Joint-removal execution is unknown. | In test | Consequence engine's rule and output semantics | Asserted here |
| Elapsed times and aggregate delta totals | Idle for J1–J4: removing them together leaves the findings, local supports and source references unchanged. They may serve a separate engineering purpose. | In test for reader jobs only | None needed for read-back | Reported measurements; asserted here |

## 4. Whole-report checks

| Check | Result |
|---|---|
| **Flip the outcome while keeping inputs fixed** | **Not settled for the executable system.** No executable is supplied. P11/P14 are not a valid fixed-input flip because their causal premises differ. The reports should not be accused of accepting both answers under identical starting conditions on this evidence. |
| **Reverse the claimed direction** | **Result at report level.** Conclusions read back from a ledger concern what that ledger represents; modifying the report or its interpretation does not establish a change in the original phenomenon. P14 needs an explicit boundary between inferred support and causal intervention. The underlying causal procedure remains untested. |
| **Find the answer in the starting points** | **Result.** P14's effect withdrawal uses an asserted dependency, and P11/P14's instance conclusions use a reconstructed general rule containing the classification. These can be valid conditional deductions; they are not independent support for the dependency or classification rule. |
| **Check where the jobs came from** | **Result.** J1–J4 are given by the brief and F1 is fixed. Judging the writers' truth or requiring unrestricted natural-language understanding was not added as a pass condition. |
| **Add an already implied job** | **Result.** J3 implies that merely changing internal notation must not create a supposedly unsaid commitment. P10 exposes this distinction without requiring any new source knowledge. |
| **Look inside the process** | **Not settled.** Printed traces can be inspected, but parser decisions, rule definitions, negation semantics and fresh executions are unavailable. Several different implementations could produce these reports. |
| **Find pairs that conflict** | **Result.** Conservative exclusion limits coverage; compact ledger references obstruct sentence recovery; distrust of an unsupported causal edge coexists with using it for effect withdrawal. Each trade-off needs an explicit boundary rather than a single reassuring verdict. |
| **Check patches and catch-alls** | **Not settled for revision history.** “Correction 1” and an adapter correction are visible, but earlier versions and motivating failures are absent. The leftover bin has a useful gauge; its present wording does not measure the loss of conclusion-supporting work. |
| **Check the changes and exclusions** | **Result.** Source truth, translation fidelity, engine soundness, population-wide reader success and generalisation beyond these cases are outside what the supplied evidence can establish. These limits were not introduced after a failed test. |
| **Build the best rival account** | **Result: not distinguished beyond the report interface.** The outputs fit a narrow account—consistency and consequences of a chosen encoding—without establishing the stronger account that original arguments or causal mechanisms were independently validated. The narrower account preserves the useful findings. |
| **Check origin of the parts** | **Not settled historically.** The archive supplies reports and labels, not evidence of which features were fitted, deliberately constructed, or tested on unseen cases. Their reported outputs cannot establish that history. |

## 5. Changes that should matter, and nearby changes that should not

These are proposed acceptance tests, **not checker executions performed in this audit**. They also test the audit's criticisms against nearby innocent cases.

| Test | Change that should matter | Nearby change that should not matter | Acceptance condition |
|---|---|---|---|
| Source recovery | Remove the sentence/quotation association from a finding. | Rename all its ledger identifiers consistently. | The first loses traceability; the second preserves the same source and finding. |
| Novel consequence | Add a genuinely different consequence with a supporting derivation. | Express P10's existing dependency using an equivalent internal predicate name. | Only the first creates a new semantic commitment. |
| Alternative support | Remove both P09 c and y; separately remove both P01 a and r. | Remove just one of the alternative routes. | Report collective dependence without calling every individually replaceable premise idle. |
| Assumed causal dependency | In P14, vary whether h is unsupported, independently supported, or absent. | Rename group-structure and helping identifiers consistently. | Separate assumption-relative compatibility from a counterfactual whose needed dependency is established. Print the resulting positive/negative query states. |
| Exercise a general rule | Add an explicitly qualifying instance to a rule-only case. | Add an unrelated fact that does not satisfy its antecedent. | The report distinguishes an exercised check from no eligible target. |
| Grounding versus imported knowledge | For P15, explicitly add a great-person premise for one already misunderstood individual. | Keep only the printed list of misunderstood individuals. | Under the printed great-person-to-not-misunderstood rule, flag the grounded conflict; do not import the missing greatness premise from reputation. |

A separate, broader future question would be whether different faithful encodings or declared equivalent verb paraphrases preserve verdicts. That would audit translation and vocabulary adequacy, not merely the present report-only contract. It should be registered as a new question, not retroactively treated as a failed requirement here.

## 6. The two changes with the greatest value

**First: emit a source-anchored record for every finding.** It should contain the quoted sentence, ledger interpretation, finding in ordinary language, supporting lines with their sentence anchors, and an explicit/interpretive/assumed provenance label. P11/P13/P14's what-if headings show that usable anchoring is already possible.

**Second: separate verdict types and show the support behind them.** A report should distinguish a fault, an unsupported inference, an unsupported causal dependency, an assumption-relative counterfactual result, an unexercised check, an unrepresented clause, a normalised restatement and an additional consequence. Existing labels can remain as secondary terminology, but cannot substitute for these distinctions.

A compact record for P14 could read:

> **Sentence 8 — conditional result only.** The encoded prediction that helping would not remain after removing group structure is satisfied by withdrawing the spread assertion under causal dependency h. The production check did not establish h. Cessation through time is not modelled. The exact source span for h and the recomputed query state must be supplied.

This preserves the result without turning an assumed dependency into its own validation.

## 7. What this audit does not show

It does not show that the original conclusions are false, that a particular formal causal convention is wrong, or that L66's implementation is unsound. A missing ledger bridge can reflect the passage, its encoding, the admitted language or the checking policy; this bundle cannot always distinguish them. It also does not show that all readers will fail: this is one complete read-back and structural audit, not a reader experiment.

The useful core should be preserved: concrete unsupported-link diagnoses, explicit unrepresented material, careful treatment of qualified claims, separation of a proposed plan from an achieved goal, and visible provenance labels. The defect is that the current reports do not consistently let these strengths produce the source-grounded, appropriately limited answers the brief requests.

**Next step:** regenerate this same bundle with source-anchored findings and disaggregated verdicts, then run an independent report-only read-back against a separately maintained answer key, including the boundary cases above. The complete current read-back is in [ANSWERS_ChatGPT.md](ANSWERS_ChatGPT.md).
