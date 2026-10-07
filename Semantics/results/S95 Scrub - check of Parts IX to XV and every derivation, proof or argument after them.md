# S95 Scrub: check of Parts IX to XV and every derivation, proof or argument after them

Checker: Claude. I did not write the vocabulary or the scrubbed text. Date: 25 September 2026. Not committed.

- Scrubbed text: `tests/Revision 2 - file 13 draft 5, scrubbed of verificationist words, theory text.md` (md5 2517ef4ec1f274e8de2bfb7e6661ef94).
- Draft 5: `tests/Revision 2 - file 13 draft 5, theory text.md` (md5 7f1d8ad02adf96e27622593bd263252e). It was not edited.
- Range: lines 373–632. That is Parts IX–XV and Part XVI, Arguments 1–10. The two files are line-aligned. A program listed the differing lines: 82 of them are in the range. Each was read as a word diff, in full context. A second program scanned the range for forbidden words and near-synonyms.

The owner's standard, as quoted in the instruction: "argument is short hand for: reasons why this and not that. Not reasons for this and not that." Decision S21: "sees no option but to choose the one that isn't ruled out by its best argument".

## Verdict for the range: HOLDS_WITH_REPAIRS

Every argument in Part XVI still goes through, and each is now headed *Why this and not its denial*, which matches the owner's sense exactly. The theory's structure survives the scrub: (K1)–(K3), (P), (EX), (CT1)–(CT4), (RC), (U1)–(U3), the dependence order and the defeat conditions. What fails is local, and each failure has a wording that repairs it (below):

- a clash between a refused predicate and the provisional name for (EX);
- one widened attribution clause;
- a loophole: an assessor can rule out a claim by a stated assumption;
- assessor inputs of (K2) that are neither defined nor declared;
- one ordering phrase that presumes a chain;
- an asymmetry between defeat conditions (A) and (B);
- a handful of phrasings that still read as "argument for".

None of these needs a word the owner forbade.

---

## 1. Residue (words that still carry the forbidden idea)

**R1. "An argument that X", which is "reasons for".** At l. 495 "A finite list of failures is not an argument that no bypass exists". At l. 542 "an argument that every construction trace can be rewritten as a selection history without loss" and "an argument that the object layer of Part IV is not what explanation operates on". At l. 544 "An argument that treating a contract as a content … either trivializes creativity or fails to capture …". Part 0 (l. 8) says an argument "is never a reason *for* a claim". The surface form "an argument that P" is still the reasons-for form. Every one can be put as ruling out or as a counter-case (repairs 1–3).

**R2. l. 391: `Form_j(u)` is "the inference form of u is one j admits".** This is an assessor accepting an inference form, and it is not marked tentative. The owner: "Anything that is accepted is always tentatively". The word "admits" is also the contract's word for admitted changes, so j's acceptance and a contract's scope now share one verb (repair 4).

**R3. l. 518: the appraisal relation is "taken as an input and never defined in terms of anything else".** Draft 5 said only that the semantics never derives it. The new words say it is indefinable outright, which is the foundational sense of "primitive" coming back. l. 455 has the right form: "The semantics does not define \(\mathcal N\)" (repair 5).

**R4. l. 532: the heading "What defeats this class".** "Defeat" and "defeater" are the working words of defeasible justification. Part XV's own text already says "what would rule it out" (repair 6).

**R5. l. 461: a task is "a permitted input-to-output attribute transformation".** The vocabulary keeps this, marked BORDERLINE. "Permitted" is an authority word. It also clashes with the same Part: \(\mathsf{Admit}^{q,r}_\Theta\) and \(\mathsf{Poss}_\Theta\) sort *tasks* into those that can be achieved and those that cannot, so a task must be able to be impossible. The fault predates the scrub (it is in draft 5), but it lies on a word in the list (repair 7).

**R6. l. 538: "An explanation, argued to be one and not a non-explanation by an argument that does not use (E)".** The contrast "and not a non-explanation" keeps this inside the owner's sense. Even so, "argued to be one" is the argued-for form. The same content fits the rule-out form Part VI uses (repair 8).

**R7. l. 526: "a separate argument that would supply it is part of the account only when the account uses it".** Here an argument *supplies* a place in the dependence order. That is a positive supplier, not "why this and not that". What supplies a place in a definitional order is a definition (repair 9).

**Borderline, no repair needed:**
- l. 403 "a theory in error". "Error" is the fallibilist word and l. 211 defines it. An optional sharper form is in repair 18.
- l. 481 "testable". It has no absolute sense.
- l. 497 "advanceable challenges". The vocabulary marks it BORDERLINE. It is fixed by (CA), so nothing is being compared.
- "understand" and "understanding" in Part X. The scrubbed text already marks them for the owner, at l. 443.

## 2. Broken (definitions, cross-references, terms, arguments)

**B1. The refused predicate collides with the new name (l. 526; also l. 31 and l. 600, outside or at the edge of the range).**
- l. 526 says "Nothing depends on a predicate that says … 'is a created explanation.'"
- l. 31 says "no definition depends on one".
- Yet l. 443–450 define CreateEx under the heading "Created explanation", and l. 528 makes "The explanation-creation class: an instance of (EX)".

Draft 5 kept the unanalysed "is knowledge" apart from the defined "CreateEK". The provisional rename puts both under one name, so the text now says that something it defines and uses is something nothing depends on. l. 600 survives only because of the word "residual" (repair 10). This depends on the owner's ruling on the name. The collision exists under any ruling that renames (EK) to "created explanation".

**B2. l. 441 widens the attribution.** Draft 5 said ProducedBy "credits each contribution the history establishes". The scrubbed text says it "attributes the repair to each contribution the history contains". Read literally, that is every contribution in the history, including ones on no route to the repair. l. 307, in the same scrubbed text, gives the intended scope: ProducedBy "attributes a repair to the contributions whose active routes ran to it". The two now disagree (repair 11).

**B3. A dangling cross-reference, and an undefined "usable argument".**
- Part 0, l. 8, says: "Each of its steps rules out the case in which the step's premises are met and its conclusion fails (Part IX)." Part IX (l. 397) never says this. It defines an argument only as "an argument tree: argument steps whose leaves are premises".
- (K2) defines `Usable_j(u)` for a *step* u. Yet "an argument usable by j" is used at l. 395 (K3), at l. 397 (\(R_j\)), and in Parts VI and VIII, and it is never defined.

Draft 5 had the same gap with "usable receipts", so only the missing cross-reference is new. The repair is one sentence (repair 12).

**B4. Stated assumptions as leaves let an assessor rule out by stipulation (l. 397).** Draft 5's receipts were trees over *evidence* leaves. The scrubbed argument admits "record leaves or stated assumptions and definitions", so that Arguments 1–10 fall inside the definition. That is sound, but nothing now stops j from stating the assumption "the candidate does not meet (E)" and so ruling the candidate out.

The block the text does have ("A record reconstructed from a claim does not rule out that claim's denial") covers records and not assumptions. Unrepaired, "not ruled out" (Part VI), "a problem for p" (l. 317) and S21's choice "the one that isn't ruled out by its best argument" can all be dissolved by assuming. The repair (13) extends the existing block from records to assumptions. It keeps definitional failures such as a reversed calculation or a circular dependence, which need no record, and it keeps the Duhem background of (K3).

**B5. (K2)'s assessor inputs are neither defined nor declared, so Argument 6 has a gap.**
- `Form_j`, `Scope_j` and `Live_j` (l. 390) are not defined in terms of Θ, \(\mathcal N\), the indices or the declared inputs.
- Part XIV's list of declared inputs (l. 522) does not include them.
- Argument 6 claims that *every* predicate in Parts II–XIII is so defined, and Part IX is inside that range.

The gap predates the scrub (`Lic_j` and `Live_j` were undefined in draft 5). The reading "one j admits" now makes explicit that these are an assessor's inputs, so they belong on the list (repair 14). With that, Argument 6 goes through. A second gap also predates the scrub: Argument 6's walk "until it reaches the imports, the indices or the declared inputs" never reaches any of them from (O) and (Q), which "depend on nothing" (l. 526). One clause fixes it (repair 14).

**B6. l. 479: "each admitting no performance the one before it excludes".** "The one before it" exists only in a chain. \(Q_\Theta\) is declared a directed preorder, where a tolerance can have many predecessors, or none that are comparable. Reading the order as set inclusion is right; the wording is not (repair 15).

**B7. Defeat conditions (A) and (B) no longer match (l. 536–538).**
- (B) now names what an outside judgement must be: "argued … by an argument that does not use (E)".
- (A) lost its "plainly" and now rests on a bare "explains nothing", twice. That is the unqualified predicate l. 31 and l. 526 say nothing depends on.

A defeat condition has to be stated from outside (E), and only (B) now says how (repair 8).

**B8. Small breaks:**
- l. 620: "Stipulate a object layer". It should be "an".
- l. 630: "it is what the contract contains: identity, at this grain, is exhausted by trajectory". A contract contains admitted changes. That identity is exhausted by trajectory *follows from* what it contains; it is not itself contained.
- l. 540: "Such a case would rule out Argument 1". What is ruled out is a claim, namely Argument 1's Claim, not an argument.
- l. 600: "Neither is a predicate about explanation taken as an import". Both *are* the imports, so the tail clause makes the sentence read as if they were not.
- l. 453: "to rescue its meeting (E)". The "its" is loose and should be c's.

Repairs 16–17.

**B9. Notation (minor).** \(R_j(\psi)\) (l. 397) sits next to the repertoire \(R_{\beta,\ell}(s,\xi)\) (l. 403) and \(R_{<e}\) (l. 413), and it is never used again. Draft 5's \(P_j,N_j\) did not clash (repair 12).

**Arguments that go through as written:** 1, 2, 3, 4, 5, 7, 8, 9 and 10.
- Argument 1's Claim is now in exclusion form ("no active component … has a signature … that differs"). It is equivalent to the old form, and Argument 2 (ii) uses it by contraposition without a gap.
- Argument 7's last step ("\(\mathcal E\) can meet (E) on \(C\) and fail it on \(C'\)") says more precisely what "may both be true" meant.
- Argument 6 goes through with repair 14.

No cross-reference in the range points to the wrong place: (K1)–(K3), (EX), "import 2, Part XIV", "Part VIII, historical index", "finite monotone claim" (l. 305), Arguments 1–9 as cited, and "object layer" (l. 171–175). The exceptions are B1 and B3.

## 3. Changed claims

**More than removing a verificationist commitment:**

| line | draft 5 | scrubbed | what changed |
|---|---|---|---|
| 385 | "Using an invalid objection does not make it valid." | "Using an objection gives it no bearing (K1) and makes no argument from it usable (K2)." | Widened from invalid objections to all objections, and "valid" split into its two senses. It is a gain, but "gives it no bearing" can be read as "takes its bearing away" (repair 19). |
| 390–391 | `Lic_j(u)`, undefined | `Form_j(u)`: "the inference form of u is one j admits" [Claude's reading] | New content: logic becomes relative to the assessor's acceptance. It is harmless only because Part 0 builds validity into "step". See R2 and B5. |
| 397 | receipts: derivation trees over *evidence* leaves, \(P_j\) (for) and \(N_j\) (against) | arguments whose leaves are records *or stated assumptions and definitions*; one set \(R_j\) | The set change is information-neutral: \(P_j(\phi)=R_j(\neg\phi)\) and \(N_j(\phi)=R_j(\phi)\). The widened leaves are more than a word change and open B4. |
| 429 | "Closing an episode is a decision, not a proof." | "… a choice, not an argument." | Draft 5 said no proof forces closure. The new sentence can be read as saying arguments have no part in closing, which is against S21, where the choice is made by what arguments leave not ruled out (repair 20). |
| 441 | "credits each contribution the history establishes" | "attributes the repair to each contribution the history contains" | Widened (B2). |
| 455 | "Repairing an obligation establishes that it was repaired; it establishes nothing about whether the obligation … was worth having." | "Repairing an aim repairs it and says nothing about how anyone appraises the aim …" | Worth, a property of the aim, becomes appraisal, a relation to appraisers. "Normative relation (primitive 2)" becomes "appraisal relation (import 2)". The value dimension now reads as person-relative (see Losses). |
| 479 | "increasingly demanding and short of perfection" | "each admitting no performance the one before it excludes, and short of exact" | A loose description becomes a chain-shaped inclusion claim (B6). |
| 518 | "never derived" | "never defined in terms of anything else" | "The semantics does not derive it" becomes "it is indefinable" (R3). |
| 536 | "that plainly provides no account" | "that nonetheless explains nothing" | The outside judgement lost its marker (B7). |
| 538 | "A genuine explanation" | "An explanation, argued to be one and not a non-explanation by an argument that does not use (E)" | An objective status becomes the argument that would have to be given. Intended. It is stricter and clearer, and it creates B7. |
| 544, 592 | "finding the right question"; "on the same footing as answering one" | "finding a new question"; "as answering one is" | Broader. The theory now claims to capture *every* finding of a new question, not just the right one. That exposes more to defeat and matches what (G) formalizes (New ∧ Build ∧ Attempt). "Finding" must be read as owned construction: a relayed new question is not creative (repair 21). |
| 526 | refused: "is knowledge" | refused: "is a created explanation" | Collides with the defined (EX) (B1). |
| 630 | "it is the correct report that identity … is exhausted by trajectory" | "it is what the contract contains: identity …" | Category slip (B8). |
| 632 | "has been shown to instantiate it" | "instantiates it" | A stronger disclaimer: no claim about actual instances at all. Intended, and a gain. |

**Only the removal of the verificationist commitment (intended):**

| line | draft 5 | scrubbed |
|---|---|---|
| 373, 387 | "standing" | "usable arguments", "Usability" |
| 377, 383 | "grounds g", "grounds for an alleged defect" | "premise g", "the premise of a criticism alleging a defect" |
| 393 | "removes a license; it does not make the conclusion false" | "makes the step unusable; it does not rule the conclusion out" |
| 395 | "an established ¬O yields ¬(T∧B∧I)" | "an argument usable by j that rules out O rules out T∧B∧I together for j" |
| 403 | "establishes neither" | "suffices neither for" |
| 403 | "a false theory" | "a theory in error" |
| 405, 409, 411, 584, 604 | construction "witness" | "trace" |
| 427 | "Credit for content", "ground" | "Contribution of content", "attributed through it" |
| 429, 435–455 | obligations | aims |
| 441 | "A correct account", "does not rank alternatives" | "An account" ("account" already means meeting (E)), "puts no order on alternatives" |
| 443–528 | (EK) | (EX), provisional, OWNER |
| 461, 469 | "success", "legitimate inputs" | "performed the task", "admitted inputs" |
| 475 | "grounded in" | "defined by" |
| 481 | "checkable" | "testable" |
| 495 | "not a barrier proof; a bypass refutes" | "not an argument that no bypass exists; one bypass rules out" (see R1) |
| 509 | "does not certify it"; "does not establish it" | "leaves it open"; "does not suffice for it" |
| 515–526 | primitives, derived, well founded, justified, proof | imports; defined in terms of; no cycle and no endless descent (exactly the mathematical content of well-foundedness); defined; argument (R7) |
| 522 | verdict, unsettled; "no probability of truth, no merit function and no ranking of thinkers" | assessment, left open; "no probability on claims and no function that orders explanations or thinkers" |
| 524 | "could be true or false" | "a case meets or fails" |
| 526 | "what is established … fits … a problem for p on rivals and fits" | "being ruled out for an assessor on usable arguments (Part IX) and (E) … on neither being ruled out". Consistent with Part VI, l. 315–317. |
| 528 | "correct typing, satisfying" | "typing as declared, meeting" |
| 534 | "load-bearing claims … refute … not a refutation" | "the claims the rest depends on … rule it out … not an argument that rules a claim out" |
| 540 | "This refutes Derivation 1 and reinstates correspondence as primitive" | "Such a case would rule out Argument 1 and make correspondence an import again" (B8) |
| 546, 550–632 | theorem, Derivation(s), *Proof.*, Corollary | claim, Argument(s), *Why this and not its denial.*, Consequence |
| 554, 558, 560–568 | anchor | counterpart |
| 568 | "one assignment is 'really' right" | "one assignment, and not the other, is the target's" (repair 22 makes it plainer) |
| 572 | "does not establish that such a t′ exists" | "leaves open whether such a t′ exists". Slightly stronger, since it also covers non-existence, and true. |
| 576, 620 | "primitive layer", "guarantee" | "object layer" (l. 175's own term), "claim" |
| 582, 624 | expectation, expects | prediction, predicts |
| 606 | "its truth is fixed … may both be true" | "whether \(\mathcal E\) meets (E) on C is fixed … can meet (E) on C and fail it on C′" |
| 608 | "a licensed operation of the semantics" | "an operation the semantics admits" |
| 610 | "genuine recoding" | "structure-preserving recoding" |
| 628 | "predict displacements correctly"; "the account is adequate" | "predict the displacements that occur"; "S_1 is an account" |

## 4. Losses

1. **No positive status.** In the range the theory can no longer say that a claim is established for an assessor, or that a candidate fits. It says only that a candidate is ruled out for j or not ruled out. This is intended, and it is what S21 asks for. What goes is any way of marking a candidate that has *survived* tests as different from one never tested. Both are simply "not ruled out".
2. **Worth becomes appraisal (l. 455, 518, 522, 592).** The theory can mark where someone's appraisal enters. It can no longer name a claim that an aim or a question *is worth having*, as distinct from anyone's appraisal of it. Deutsch treats values, beauty included, as objective and open to conjecture and criticism. The new wording ("how anyone appraises") leans toward a person-relative reading the sources do not hold. The \(\mathcal N\) slot itself survives, and it can hold an appraisal that is itself a criticizable claim (see repair 23).
3. **"Knowledge" (l. 433–528), pending the OWNER ruling.** In Deutsch and Marletto, knowledge is not belief: it is information that keeps itself instantiated and can act as a constructor. Dropping the word loses the direct bridge from (EK) to the sources' central concept, and it creates B1.
4. **"The right question" (l. 544, 592).** The theory no longer says anything about which question to find. It only says that finding a new one is creative. Draft 5 had never formalized "right", so no formal content is lost, only a stated aim.
5. **The permanence of a bypass.** "a bypass refutes a proposed barrier" (l. 495) was permanent. "one bypass rules out" now lasts only while the argument from the bypass stays usable (K2). This is intended.

## 5. Gains

1. **Part IX is clearer than draft 5.** "Where no argument usable by j rules out φ, that absence rules out nothing, neither φ nor ¬φ" says exactly what "missing evidence stays missing" gestured at. One set \(R_j\) replaces two sets and an exchange rule, and loses no information.
2. **(K3)** now keeps both the Duhem point and its dependence on the assessor and on usability, with no appeal to an established ¬O.
3. **"Using an objection gives it no bearing (K1) and makes no argument from it usable (K2)"** names both senses that "valid" left unsaid.
4. **Part XVI's heading *Why this and not its denial.*** is the owner's "reasons why this and not that", applied to every argument. Argument 1's Claim, stated as an exclusion, is the same form.
5. **Argument 7** now says precisely *how* the two claims coexist (meets (E) on C, fails it on C′), not just that both "may be true".
6. **Part XIV's "no cycle and no endless descent"** is the exact mathematical content of well-foundedness, without the foundation metaphor.
7. **Argument 5's Consequence and (E) of Part XV** now claim only what (G) actually formalizes.
8. **Argument 10's disclaimer** ("not a claim that any … program instantiates it") no longer implies that showing someone instantiates it is the missing step.
9. **(B)** now says what an outside judgement of "explanation" must be: an argument that does not use (E). This is stricter than "genuine".
10. **Tolerances read as inclusion** remove the merit reading of "grades" (lesson S26), once B6 is repaired.

## 6. Repairs (exact wordings, in the new vocabulary)

1. **l. 495.** "A finite list of failures does not rule out a bypass; one bypass rules out a proposed barrier."
2. **l. 542.** Replace from "; an argument that every construction trace" to the end of the item with: "; a method that rewrites every construction trace as a selection history without loss (against Part IV, collapsing the two provenances and removing creativity from the semantics); or an argument that rules out that explanation operates on the object layer of Part IV."
3. **l. 544.** "**(E) Question-finding.** A case of finding a new question that treating a contract as a content, something that can be constructed, be new, and be the originative contribution of an episode, fails to capture; or an episode that is not creative which that treatment counts as creative (against Argument 5)."
4. **l. 391.** "\(\operatorname{Form}_j(u)\): the inference form of \(u\) is one \(j\) tentatively accepts (Part 0) [Claude's reading; draft 5 names this predicate and does not define it]." Optionally also: "\(\operatorname{Scope}_j(u)\): \(u\) is applied within the contract, grain and boundary \(j\) has declared for it; \(\operatorname{Live}_j(d;u)\): \(j\) has not withdrawn \(d\) [Claude's readings]."
5. **l. 518.** "It is taken as an input and the semantics does not define it; the aesthetic relation of Part XI is one instance."
6. **l. 532.** "# Part XV — What would rule this class out"
7. **l. 461.** "…a task a specified input-to-output attribute transformation with explicit resources and side effects." With this, a task can be possible or impossible, as \(\mathsf{Admit}\) and \(\mathsf{Poss}\) require.
8. **l. 536–538.**
   - (A): "A candidate meeting all four conditions of (E) on a physically admitted contract, with a non-declared transport, that an argument not using (E) rules out as an explanation of what its question asks."
   - End of (A): "…it is a counterexample only if it fails none of the four and such an argument rules it out as an explanation."
   - (B): "A candidate that an argument not using (E) rules out as a non-explanation, whose organization no transport can preserve under any physically admitted contract."
9. **l. 526.** "…has not supplied its place in it, and a separate definition that would supply it is part of the account only when the account uses it."
10. **l. 526** (and the same at l. 31): "Nothing depends on an undefined predicate that says "explains" without a question and a contract, or "is a cause"; (EX) is a defined relation of an episode, not such a predicate." If the owner keeps the name "created explanation", l. 600 should read "…no residual, undefined predicate meaning "explains," "represents," or "is a cause"; (EX) is defined (Part XI)."
11. **l. 441.** "…it attributes the repair to each contribution whose active route ran to it in the history, and where two sufficient contributions both ran, the repair is attributed to both…"
12. **l. 397.** Add after the first two sentences: "Each step of an argument rules out the case in which the step's premises are met and its conclusion fails; an argument is usable by \(j\) when each of its steps is (K2), and it rules out what its last step rules out." Rename \(R_j(\psi)\) to \(X_j(\psi)\), since \(R\) is the repertoire at l. 403.
13. **l. 397.** Replace the last sentence with: "A record reconstructed from a claim does not rule out that claim's denial, and neither does a stated assumption of the claim, or of a claim that contains it."
14. **l. 522.** After "(Part XII);" insert: "for an assessor \(j\), the inference forms \(j\) tentatively accepts, the scope \(j\) declares and the premises \(j\) has not withdrawn (K2, Part IX);".
    - **l. 526**: after "(K1) depends on (E)." insert "(K2) depends on those inputs of the assessor; (K3) on (K2)."
    - **l. 598**: "…following each definition back until it reaches the imports, the indices, the declared inputs, or (O) and (Q), which depend on nothing."
15. **l. 479.** "The tolerances of the physical module (Part XIV) form a directed preorder \(Q_\Theta\), in which \(q\) precedes \(q'\) when \(q'\) admits no performance \(q\) excludes; none of them is exact."
16. **l. 620.** "Stipulate an object layer". **l. 630:** "That is not a defect of \(S_1\): the contract contains no change that separates the two things except by their trajectories, so identity, at this grain, is exhausted by trajectory."
17. **l. 540.** "Such a case would rule out the Claim of Argument 1 and make correspondence an import again." **l. 600:** "Neither is a predicate about explanation." **l. 453:** "to rescue \(c\)'s meeting (E)".
18. **Optional, l. 403.** "A system may understand a theory that is not an account of its question."
19. **l. 385.** "Using an objection does not give it bearing (K1) or make any argument from it usable (K2)."
20. **l. 429.** "Closing an episode is a choice: an argument can rule out some ways of closing it, but no argument makes the choice."
21. **l. 592.** "Finding a new question, by an owned construction (G), is a creative act, as answering one is."
22. **l. 568** (and l. 317, outside the range): "a claim that the target pairs its components one way and not the other is a claim that some admitted change separates them, and must supply it."
23. **Optional, l. 455, if the owner wants the Deutschian reading kept open.** "Repairing an aim repairs it and says nothing about any appraisal of the aim, or of the question that led to it; an appraisal, where one is invoked, is itself a claim open to criticism."
