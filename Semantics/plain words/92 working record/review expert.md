# Expert review of "whole v1.md" against draft 4

*Written 25 September 2026. I read both documents in full: `whole v1.md` (859 lines) and draft 4's theory text (632 lines). I checked the examples against the S81 case book (O1–O52), the S89 case book (N1–N25), D3-T `final.md`, the S81 rulings (04 and S81 Results), and the change list's CASES AT RISK and CHECK fields. I also read the built draft's note and sources note, decision S20, and the S88 readings where the document cites them. I did not edit the document.*

*Line references: "doc Lnn" is a line of `whole v1.md`. "D4 Lnn" is a line of `Semantics/tests/Revision 2 - file 13 draft 4, theory text.md`. "CL Lnn" is a line of the change list. Severity is High (a reader would take away a claim draft 4 does not make, or miss one it does), Medium (a condition, label or attribution is wrong in a way that matters), or Low (precision, labelling or style).*

## Counts

| kind | High | Medium | Low | total |
|---|---|---|---|---|
| Faithfulness | 5 | 11 | 18 | 34 |
| Coverage | 0 | 0 | 6 | 6 |
| Examples | 0 | 3 | 9 | 12 |
| Consistency and style | 0 | 1 | 6 | 7 |
| **all** | **5** | **15** | **39** | **59** |

Item 48 is a slip in draft 4 itself, recorded for the owner and not counted.

**Coverage in brief.** Every Part (0 to XVI) is rendered, and so are all ten Derivations, all eleven grievances, all five load-bearing claims and the mathematical-error entry. The gaps are sentences, not Parts (C1–C6).

---

## Findings, most serious first

### 1. [Faithfulness, High] The summary drops the declared indices and inputs from what the theory rests on
- **Doc L24:** "It rests on two things only, the physics and, where a question is about worth, a standard of worth taken from outside".
- **D4 L31, L520, L522–524, L596:** "Everything else is derived from the two primitives, the declared indices and the **declared inputs**". This is a draft-4 change of claim (W7.1, W7.2, W7.6). File 11 said "Everything else is derived", and draft 4 added the indices and inputs on purpose.
- **Problem:** the one-page summary restates the file-11 position that draft 4 corrected. Section 12 has it right, so the document also contradicts itself.
- **Should say:** "It has two foundations, the physics and, where a question is about worth, a standard of worth taken from outside. Everything else is built from those two, from each claim's frame, and from the inputs a claim must state (section 12)."

### 2. [Faithfulness, High] A full response table is said to fail one of the requirements
- **Doc L576:** "The known tricks each fail one requirement (section 3), a full response table included".
- **D4 L536:** "A table that encodes the response to every admitted change does not fail (F1); like any new attempt, it is a counterexample only if it fails none of the four and still explains nothing." D4 L269 says the same. Both follow from W11.1 and W11.2, which are changes of claim.
- **Problem:** the sentence says the full table fails a requirement. Draft 4 says it passes matching and is judged like any other attempt. Section 3 (doc L127) has it right, so the document contradicts itself here too.
- **Should say:** "The known tricks each fail one requirement (section 3). A full response table passes matching; like any new attempt, it would defeat this claim only if it met all four and still explained nothing."

### 3. [Faithfulness, High] The four requirements are said to hold "at every setting"
- **Doc L114:** "A candidate is an **account** of a question exactly when, at every setting of the range, it meets four requirements."
- **D4 L231, L255, L257:** the requirements are "each a condition on supplied relations under the changes in \(C\)". Non-circular dependence is existential: "There exist \((a,b)\in C\) and a nonempty block…". Non-vacuity concerns the baseline and the contract as a whole.
- **Problem:** this misstates the logical form of the central definition. The doc's own requirement 3 then says "at some setting", so the section contradicts itself.
- **Should say:** "A candidate is an **account** of a question exactly when it meets four requirements, each about how it behaves under the changes the range holds. None looks at a label."

### 4. [Faithfulness, High] "Blindly" is back in the account of selection
- **Doc L19:** "shaped blindly by selection".
- **D4 L13:** "produced by variation and survival on a history of encountered changes, with no represented target in that history". See also L195 and L201. After S90, W37.1 deleted "blind" from Part 0 because its ordinary sense ("variation not directed in any way") says more than Parts I–XVI state (CL L409–L413).
- **Problem:** this puts back the exact word the owner's text removed, and with it a claim the body does not make.
- **Should say:** "shaped by selection, with nothing in its history picturing what it ties to".

### 5. [Faithfulness, High] The missing-input rule is widened to any unstated input
- **Doc L334:** "A case whose verdict turns on an input it does not state is a case with a missing input, not a refutation (section 12)." **Doc L582:** "A case whose verdict turns on an input it does not state, or on the standard of worth, has a missing input and is not a refutation."
- **D4 L534:** "A case whose verdict turns on an input the case does not state, **where the input is one of the declared inputs Part XIV lists or the normative relation**, is a case with a missing input, not a refutation."
- **Problem:** the condition is dropped. As the doc words it, any unstated fact, a physical one included, would excuse the theory from a counterexample. That makes the theory harder to refute than draft 4 does.
- **Should say:** "…turns on one of the stated inputs listed in section 12 (or on the standard of worth) that the case does not state…".

### 6. [Faithfulness, Medium] "Certifies nothing" is back
- **Doc L312:** "the theory records the limit and certifies nothing".
- **D4 L159:** "the semantics records the restriction and supplies no rule that certifies it. Meeting the conditions of an account (Part V) on the restricted contract does not certify the restriction **as appropriate**."
- **Problem:** check 1 rejected "certifies nothing about the restriction" because it is false against non-vacuity (CL L649). Non-vacuity does certify that a limit is stated and does not empty the range.
- **Should say:** "the theory records the limit and gives no rule that certifies it as right; meeting the requirements on the narrowed range does not certify it as right either".

### 7. [Faithfulness, Medium] "The cure is a finer range" overstates and drops conditions
- **Doc L286–288:** the heading "The cure is a finer range", and "A finer range holding that change makes a different question, on which the two pose a problem inside the range."
- **D4 L317:** "A finer contract that contains a change at which two rivals conflict makes a new question (Part III), on which, **offered for it**, they pose a problem of the first kind **while both fit**". The attacks refuted the unscoped "the remedy is a finer contract" (CL L1205). On the original question both rivals remain accounts, and its problem is untouched.
- **Problem:** the heading presents the finer question as curing the problem, and two conditions are lost.
- **Should say:** use the heading "A finer question", add "if both are offered for it and both still fit", and add one sentence: "On the original question nothing changes: both remain accounts there."

### 8. [Faithfulness, Medium] A condition becomes an assertion: "keeping every rival that fits is a stated safeguard"
- **Doc L292:** "as when choosing one rival meets a demand only by dropping the other, and keeping every rival that fits is a stated safeguard."
- **D4 L317:** "…meets a claimed obligation only by dropping the other, which fits as well, **where** keeping every rival that fits is among the protected obligations".
- **Should say:** "…only by dropping the other, which fits as well, in a case where keeping every rival that fits has been stated as a safeguard."

### 9. [Faithfulness, Medium] The state of draft 4 is misreported
- **Doc L38:** "every point they raised was ruled on; they have not seen its last paragraphs, on rivals, problems and failed answers." Doc L602 is similar.
- **CL L244–L271 ("Carried forward after S90"):** "The S90 readings passed these on without a ruling". These include the letter G, the block that revised L339 does not name, R55's bijection, "the ground of its restriction", and the bolded "declared inputs". **CL L146, L27:** "No outside reader has seen the texts and declarations the ten fixes wrote." Those fixes include W19.1's and W20.1's new wording. The group-H edits to W34.1, W33.1, W36.1 and the sources note are also unseen.
- **Should say:** "…most points they raised were ruled on, and a few were passed on for later; they have not seen the paragraphs on rivals, problems and failed answers, the wording of the ten fixes made after their reading, or the edits made with the new paragraphs."

### 10. [Examples, Medium] "The machine that runs forever" is used for a point about barriers, which is a different idea
- **Doc L88:** "Pia gives a list of failures, which has no piece that responds to any change, and a finite list of failures does not prove that something cannot be done (section 11)." **Doc L540:** "A finite list of failures proves no barrier (Pia's machines, section 2; Kofi's phrasebook, section 9)".
- **D4 L495:** a barrier is "an independently characterized domain for which every admitted, non-question-begging enabling condition leaves the relevant capability unavailable". That is a limit on a system's explanatory capability. A perpetual-motion machine is an obstruction question (D4 L335). Pia never claims impossibility; she hopes a design will work. The fixed verdict faults her for giving "no reason", not for failing to prove a barrier.
- **Problem:** the second half of the reason at L88 misses the verdict's point, and L540 applies the barrier sentence to a physics case. Kofi's case rests on a different sentence (D4 L403: a narrow use establishes no "permanent inability"). "Marletto's book draws the same line…" (L88) is a claim about a source that draft 4's sources note does not make. The source audit supports it (obs 7, M p.61), but the doc gives no page.
- **Should say (L88):** "Pia gives a list of failures: it has no piece that responds to any change, so it is a table of observed answers and fails matching." **L540:** drop "Pia's machines"; keep Kofi's only with D4 L403's wording.

### 11. [Faithfulness, Medium] The glossary's "conflict" drops "each could match"
- **Doc L661:** "answers differ at a setting, or no behaviour the physics allows lets both match."
- **D4 L315:** "or when **each of them could meet** (F1), (F2) and (A) there under some relations … and no such relations let both". The change list says this condition is load-bearing: "A candidate that could not meet the conditions at a pair whatever the target does is excluded from the second route … it would otherwise conflict with its own relabelling" (CL L1245).
- **Should say:** "answers differ at a setting, or each could match there under some behaviour the physics allows but no such behaviour lets both."

### 12. [Faithfulness, Medium] Idle commitment: "any support", and the glossary drops the scoping
- **Doc L232:** "an **idle commitment** is one whose adding to, and removal from, any support both leave a support." **Doc L703 (glossary):** "adding or removing it leaves every support a support."
- **D4 L313:** "A commitment \(d\) **of a candidate that has a support** … when **every** support stays a support…". Check 2 changed "any" to "every" because "any" can be read as "some" (CL L1172). The model attack added the scoping (CL L1174).
- **Should say (L232):** "every support". **Glossary:** "in a candidate that has a support: adding it to, or removing it from, every support leaves a support."

### 13. [Faithfulness, Medium] Deutsch's wider "problem" is said to be a noticed difficulty
- **Doc L404:** "His 'problem' … is wider than surprise; here it is a noticed difficulty (section 10)."
- **Draft 4 sources note (file13_draft4.md L77):** "A problem for a question is narrower: two rivals that both fit what is established (Part VI). A problem in his wider sense **can be** a recognized difficulty". Draft 4 changed "is" to "can be" on purpose, to agree with D4 L317 (CL L320).
- **Should say:** "here a problem for a question is narrower (section 6), and a problem in his wider sense can be a noticed difficulty (section 10)."

### 14. [Faithfulness, Medium] The history of "reach" is wrong
- **Doc L238:** "File 11 counted how many changed forms of an account still pass as more 'explanatory jobs' are demanded, and defined 'reach' from those jobs; draft 4 drops both".
- **File 11 L315:** "More reach constrains variation" uses "reach" undefined. An earlier draft of the change list (draft 3's W34.1) added a definition, and draft 4 drops it along with the lemma (CL L1126, L1149).
- **Should say:** "File 11 compared which changed forms of an account still pass as more 'explanatory jobs' are demanded, and used the word 'reach' without defining it; draft 4 drops the comparison and the word."

### 15. [Faithfulness, Medium] The change to "no assumed answer" is misdescribed
- **Doc L154:** "the third requirement now removes a group of commitments, where file 11's wording left open which pieces those were and, on one view, gave wrong verdicts".
- **D4 L255 and declaration W20.2:** "It no longer asks for a pair of the contract that itself removes or replaces a block of the commitments." The group is now deleted outside the range's changes, and the test is whether a contrast between two settings of the range is lost. File 11 also "removed or replaced" a block.
- **Should say:** "the third requirement no longer asks the range to hold a change that removes some commitments; it asks that deleting a group of commitments lose a difference between two settings of the range. File 11's wording also left open which pieces were commitments and, on one view, gave wrong verdicts."

### 16. [Examples, Medium] "The novelist's two demands" is mislabelled, and made conditional against the record
- **Doc L484:** "*Not yet ruled; this document's view.* … if her demand is 'rich and fast together', or rich prose is a stated safeguard, the first draft is no repair and the second is; the theory takes that statement as an input, not as something it reads off the case."
- **Record:** CL L1703ff (W35.3, N19: "toward… The first draft meets one demand by failing the other, so it is not a Repair; the second draft is") and CL L1764ff (W5.1: "N19 (O69) stays AGREE. The first draft fails the protected condition on the chapter it covers"). The case states both demands: she "wants two things from every chapter".
- **Problem:** a recorded view exists, and the doc presents its own, more doubtful one. It also implies the case lacks the input, when the case states it.
- **Should say:** "*Not yet ruled; the view recorded with the draft:* her two stated demands clash in the chapter before anyone reads it, which is a noticed difficulty. The first draft meets one demand by breaking the other, so it is no repair; the second is."

### 17. [Examples, Medium] Nadia's ownership under draft 4
- **Doc L526:** "Nadia's case (section 8) states no boundary; the ruling read 'her own' in the ordinary sense, a doubt the readers noted."
- **D4 L473:** "a statement that names the system and says whether a process runs inside it or outside it declares the boundary for that process". CL W12.1 (L1905ff): "O3, O14, O18 and O31 stay AGREE … Each says the process runs in the named system: 'she starts keeping a tally'".
- **Problem:** this is exactly where draft 4's new sentence applies, and the doc leaves the point open. "The readers" in S81 01 were Claude's two readers, not the outside readers, and the doc does not say which.
- **Should say:** "Nadia's case states no boundary outright, but 'she starts keeping a tally' names her and places the process in her, which under draft 4 states the boundary for that process. On file 11, the project's two readers had noted the doubt."

### 18. [Consistency, Medium] "Allowed" carries several ideas, and the glossary blurs the range with the target's changes
- **Doc L629:** "**allowed change**: a change the set-up **or question** counts as makeable". The body then uses "allowed" for changes outside the range (L256, L288: "some allowed change outside the range separates them"). It also uses it for what physics permits (L532: "Possible means allowed at every degree"; L544, L570), for task inputs (L530), for continuations (L536) and for aids (L540, L695).
- **D4:** "admitted edit" (the target's \(A\)), "physically admitted", legitimate inputs, "admitted continuation" and "admitted enabling condition" are distinct. Rivals and Problems (L315, L317) need "an admitted change outside \(C\)", which "allowed by the question" cannot express.
- **Should say:** in the glossary, "a change the set-up counts as one that can be made (a range holds some of them)". Use "possible" for physics throughout, as the word sheet reserves it.

### 19. [Faithfulness, Medium] The source of re-tuning is widened to every miss
- **Doc L380:** "A miss can be met by **re-tuning**, adding the setting to the trials and letting variation adjust the link within its pool, or by a **response by construction**".
- **D4 L225:** "A **selection response** extends the history \(H\) **of a selected transport** and lets \(\mu\) act". W35.4 added this because a constructed link has no trials and no pool.
- **Should say:** "A miss by a selected link can be met by re-tuning …; any miss can be met by a response by construction."

### 20. [Faithfulness, Medium] "Draft 4 changed nothing here", and an added claim about faulty questions
- **Doc L96:** "**Draft 4 changed nothing here.** The theory gives no way to choose a question's level of detail, or to tell that a question is faulty."
- **D4 L161:** "Exposing the defect is another question with its own contract." The theory does give a way: an account on that other question. Section 2 also covers Part III (doc L98), whose scope paragraph draft 4 changed (W57.1, D4 L159); the doc renders that change in section 7.
- **Should say:** "Draft 4's change to this Part, on limits, is in section 7. The theory gives no rule for choosing a question's level of detail; showing that a question is faulty is itself a different question."

### 21. [Examples, Low] "Upheld by the outside readers" overstates, for three cases
- **Doc L434 (Order of adjectives):** "upheld by the outside readers". CL L1502 (R30): Mimo said FALLS on the witness sentence; Atria named the move toward. It was ruled KEEP.
- **Doc L150 (A myth about winter):** "upheld by the outside readers". CL L535 (R06): only Atria named N3; Mimo gave STANDS with no point.
- **Doc L236 (Tomas):** "accepted by the outside readers on an earlier draft". CL L1173 (R24): only Atria named N1, and the equivalence Atria claimed was ruled false.
- **Should say:** "one outside reader (of two) named this move on an earlier draft; the project kept the text."

### 22. [Faithfulness, Low] The classes are ordered "widest first"
- **Doc L570:** "Its **classes**, widest first: … the knowledge-creation class …; the criticism-at-any-depth class; and the universal class."
- **D4 L528:** it lists the classes and orders none of them. The criticism-at-any-depth class is not contained in the knowledge-creation class.
- **Should say:** "Its **classes**:" and add "The creative-episode class lies inside the base class and the knowledge-creation class inside it; the universal class lies inside the criticism-at-any-depth class; the others are not ordered."

### 23. [Examples, Low] "The unused joint setting": the file-11 ground is gone
- **Doc L278:** "*Ruled on file 11: agrees*, on file 11's remark that a claim that two candidates really differ must name a separating change."
- **File 11 L558**, the old Consequence of Derivation 2, is what S81 rested on. Draft 4 narrows it to anchor assignments (D4 L568). CL W19.2 (L2274ff): under draft 4 "The verdict rests on Derivation 3 (L562; W17.3)". W59.1 adds the problem reading. The case also never says one arrangement was offered in place of the other, and "rivals" needs that.
- **Should say:** add "draft 4 narrows that remark to anchor assignments, so the verdict now rests on survival (section 8) and on the problem reading below, which assumes one arrangement is offered in place of the other."

### 24. [Faithfulness, Low] Worth: "four things … None is defined as another"
- **Doc L506.**
- **D4 L455:** achievement \(\mathcal R[a,k]\neq\varnothing\land\mathcal R[a,k]\subseteq G[k]\) is defined from effect and purpose. **D4 L51:** "three distinct carriers".
- **Should say:** "three things apart … effect, purpose, and artistic value with its reasons of taste; achieved purpose is defined from the first two. None of the three is defined as another."

### 25. [Faithfulness, Low] Tilt and myth: a condition is dropped, and section 13 contradicts it
- **Doc L298:** "on the seasons the Greeks knew, the axis tilt … is easy to vary relative to the myth." Also: "He holds that an explanation which could easily explain anything explains nothing; here such a candidate is still an account".
- **Sources note:** "when the two are offered in place of each other", and "a candidate **with such a rival**". **Doc L615** itself says whether the myth and the tilt pose a problem "turns on" whether a failure worked out from the candidate alone counts as established (CL L240).
- **Should say:** "…is easy to vary relative to the myth, when the two are offered in place of each other and the myth fits what is established (a point still open, section 13)"; and "here a candidate with such a rival is still an account if it meets the requirements".

### 26. [Faithfulness, Low] "A stated input is something a claim must state"
- **Doc L562, L767.**
- **D4 L524:** "something a claim takes as stated". A claim may lack it, and the verdict is then unsettled; "must" makes it an obligation.
- **Should say:** "something a claim takes as given and states".

### 27. [Faithfulness, Low] "The criticism *is* the rival"
- **Doc L282.**
- **D4 L317:** "A criticism that a candidate is easy to vary must supply such a rival (Part IX)". A criticism has a target, alleged fault, grounds and connection (L377).
- **Should say:** "must supply such a rival: offering the rival is the criticism".

### 28. [Faithfulness, Low] Rivals paragraph: small conditions lost
- **Doc L260:** "that some behaviour the physics allows would let both match at every allowed setting". **D4 L315:** "meet (F1), (F2) and (A) at each admitted pair both translate". "And answer" and "that both links carry over" are lost.
- **Doc L276:** "an answer it refutes stays refuted". **D4 L317:** "stays refuted **on \(p\)**". "since afterwards at most one of them fits" is also dropped.
- **Doc L398:** "so the two are one account". **D4 L630:** "so far as (F1), (F2) and (A) reach".

### 29. [Faithfulness, Low] Supports: "never ones someone could write instead"
- **Doc L210.**
- **D4 L299:** "not a support someone could write **with commitments outside \(\Gamma\)**". Without that condition the phrase can be read as excluding groups of the written commitments that someone might set out afresh.
- **Should say:** "never ones that need commitments the candidate does not carry".

### 30. [Faithfulness, Low] "Any that merely gives an input its value"
- **Doc L110** (and L615). **D4 L231:** "including any that assigns an input".
- **Problem:** "merely" adds a restriction: a piece that gives an input its value and does other work would seem to escape the background.
- **Should say:** drop "merely".

### 31. [Faithfulness, Low] The draft-4 change to the pool is misdescribed
- **Doc L404:** "the pool is what the physics and stated design allow".
- File 11 already said that (its L473, last sentence). **Draft 4's change (W17.2):** the population is of candidate transports, not realized ones.
- **Should say:** "the pool is of candidate links, not only ones that were built".

### 32. [Faithfulness, Low] "Episode" is given a definition the theory does not have
- **Doc L482:** "An **episode** is a stretch of inquiry, from a difficulty to a response." Also "An **episode of criticism** holds…".
- **D4 L429:** it defines only "A complete critical episode". The doc drops "complete" and invents the general definition.
- **Should say:** "A **complete episode of criticism** holds…"; describe "episode" loosely, without a bolded definition.

### 33. [Faithfulness, Low] The owner's words are hardened and misdated
- **Doc L252:** "On 24 and 25 September you said…". Both quotes are from 24 September; the 25 September words are "As long as this correct is logged somewhere…" (Decisions S20).
- **Doc L264:** "as you decided, nobody can make one, even in principle". S20 says "As far as I'm aware, that's not possible, even in principle."
- **Should say:** "On 24 September you said…"; and "as you said, as far as you know nobody can make one, even in principle."

### 34. [Faithfulness, Low] "The world, and every explanation of it, is a set-up"
- **Doc L15.**
- **D4 L31, L213:** the physics says which organization a physical occurrence instantiates at a grain. A target is an organization relative to a level of detail.
- **Should say:** "The theory describes the world, and every explanation of it, as a **set-up**…".

### 35. [Faithfulness, Low] "Ten short proofs"
- **Doc L32.**
- **D4 L618–632:** Derivation 10 is a worked episode, "a relative-consistency witness", not a proof.
- **Should say:** "nine short proofs and a worked example, Derivations 1 to 10".

### 36. [Faithfulness, Low] The proposed cases are not all "drawn from the source books"
- **Doc L34.**
- **S89 case book:** N5, N7, N10, N11 and N18 were made for the set. The doc uses N5, N7, N11 and N18. N6 and N14 are set aside.
- **Should say:** "the other holds 25 proposed cases, most drawn from the source books and five made for the set; 23 are to be used".

### 37. [Faithfulness, Low] Section 13: "no case yet aims at" question-finding
- **Doc L619:** "that questions can be found (section 9)".
- **The rota (O12)** is a question-finding case. It is silent only on merit, and "Noor found a better question" otherwise holds.
- **Should say:** "no case yet aims at whether treating a range as constructed, new and originated cheapens creativity".

### 38. [Faithfulness, Low] The source of the document's case views is not named
- **Doc L30:** the note, sources note and record "are used here only to say what changed and where the theory departs from its sources".
- **Problem:** every "view recorded with the draft" comes from the change list's CASES AT RISK notes. Those are not in the note or the record (the built record has no case entries).
- **Should say:** add "the views of cases 'recorded with the draft' come from the list of changes behind it".

### 39. [Faithfulness, Low] "Tasks … in the wording of a 2013 paper by Deutsch" is stated as part of the theory
- **Doc L530.**
- **Problem:** the theory text says only that "the physical module adopts a task-based formulation" (D4 L461). The attribution is in the sources note, which is not part of the theory. It is accurate, but it should be marked like the other source remarks.
- **Should say:** "(the sources note: the wording is from Deutsch's 2013 paper on constructor theory)".

### 40. [Faithfulness, Low] The building order leaves out lasting performance
- **Doc L568:** "understanding on pictures".
- **D4 L526:** "Deploy depends on (R) and (CT1)", so understanding also rests on lasting performance.
- **Should say:** "understanding on pictures and lasting performance".

### 41. [Examples, Low] "The theory's odd-sized tables" misdescribes the tables
- **Doc L140:** "each number minus its mirror image across the diagonal". This reads as subtraction.
- **D4 L343:** skew-symmetric, each entry the negative of its mirror image.
- **Should say:** "each number is the negative of its mirror image across the diagonal (so the diagonal is all noughts)".

### 42. [Examples, Low] "The planets tonight" carries a view the record does not hold
- **Doc L132:** "Her 'because' answers 'where were they?', a pinning-down question" appears under "the view recorded with the draft".
- **CL W20.2 (N23):** the record gives only the forward account (laws as commitments) and the two failures of the backward one.
- **Should say:** mark the last sentence "(this document's view, following Part VII's reversed calculation)".

### 43. [Examples, Low] "Two bakers": the recorded watch is omitted
- **Doc L316.**
- **CL W59.1 N7:** "Watched only if Maya's candidate gives something outside her range that conflicts with Bea's there."
- **Should say:** add "unless Maya's explanation says something outside her limits that conflicts with Bea's".

### 44. [Examples, Low] "The rota": the fixed verdict is cut
- **Doc L444:** the verdict is cut at "its merit is real".
- **O12:** "…even though the need it met was only recognised afterwards." This clause is what W35.3's episode reading turns on.
- **Should say:** give the full verdict.

### 45. [Examples, Low] "Keeping count with string": operations are named but not described
- **Doc L192, L194:** the reasoning speaks of error "per operation", but the situation omits the joins and cuts (N20: "Both groups also add flocks together by joining strings, and split flocks by cutting").
- **Should say:** add the joining and cutting to the situation.

### 46. [Examples, Low] A case sits under a heading for the theory's own examples
- **Doc L82:** "Pinning down and blocking: the theory's examples" includes "The machine that runs forever", a proposed case.
- **Should say:** "…the theory's examples, and one case".

### 47. [Examples, Low] The examples index has wrong section pointers
- **Doc L795:** Bruno is listed in sections 7, 12 and 13; he is not in 12.
- **Doc L804:** the rota is listed in 9 and 12; it is in 9 and 13.
- **Doc L820:** "Four seconds" is listed in 10, 12 and 13; it is not in 12.
- **Doc L849:** the footbridges are listed in 8 and 13; they are not in 13.
- **Doc L609, L610:** section 13 also points to section 6 for the owner's Demeter example and for the "two partial claims", which section 6 does not discuss.

### 48. [Note, not counted] Draft slip, for the owner: the reversed calculation in Part VII
- **D4 L325:** "intervening on \(H\) changes the target's \(L\) but not the calculation's \(H\)". This is inherited from file 11 L323.
- **D4 L271:** "changes the target's downstream value but not the calculation's".
- **Note:** doc L128 follows L271, which is the sensible reading ("in the calculation … it stays"). The slip in L325 should be recorded for the next draft. It is not a fault of the doc.

### 49. [Consistency, Low] "Finding out" is used where the defined word is "established", and "test" carries two senses
- **Doc L276:** "whether or not anyone can find out. Finding out what the target does there, by looking or by experiment, is a **test**". Glossary L773: "finding out what the target does at a setting".
- **D4 L317:** "**establishing** it … is a test". "Established" is defined (a usable receipt).
- **Doc L270:** "test" is also used for the (K3) sense, "the test's other assumptions", which draft 4 also has.
- **Should say:** "Establishing what the target does there … is a **test**". The glossary should read "establishing what the target does at a setting where two rivals conflict".

### 50. [Consistency, Low] The glossary is incomplete against section 1's promise
- **Doc L42:** "Each idea has one plain word, explained at first use and gathered in 'Words used here'."
- **Glossary (L623–787):** about 70 words. Missing words that the body defines in bold include: judge, assessment, task, ability, lasting performance, episode, creative episode, created knowledge, demand for knowledge, unsettled, boundary, resource terms, stock, join, reconstruction, fault question, route that ran (only as part of "route"), cut-down candidate, smallest support, needed in every support, tipping edge, look-alike states, pinned down, unchanging quantity, status rule, re-tuning, tracker, thread, left open, recoding, rewriting.
- **Should say:** either add them, or change section 1 to "the main words are gathered in 'Words used here'".

### 51. [Consistency, Low] Reserved words used in other senses
- **Doc L334:** "'not an account on the new'". "New" is reserved for newness; write "the replacement range".
- **Doc L19:** "The tie between a mind and what it pictures". Write "The link"; "tie" is used elsewhere as a verb for anchors.
- **Doc L210:** "cut down in a way the judge states". "Judge" is used before it is defined (L270). Here the draft's subject is the claim's declared restriction, not the assessor; write "in a stated way".
- **Doc L68, L94, L119, L130, L140:** "range holds changes" alternates with the defined "settings" (L66, L741). Pick "settings".

### 52. [Consistency, Low] Abbreviation
- **Doc L34:** "two AI systems". The owner's style excludes abbreviations. Write "two computer programs that write and reason in language, from outside the project".

### 53. [Consistency, Low] Owner's style: paragraph length and example-first
- **Paragraph length:** 18 body paragraphs exceed 150 words, at doc L34, L84, L88, L110, L140, L146, L178, L194, L270, L284, L312, L324, L432, L444, L530, L532, L562 and L568.
- **Example first:** several subsections open with a general statement and give no example before it. These are "Matching over many steps" (L190), "Tasks, and what is possible" (L530–532), "Criticism at any depth" (L536), "Created knowledge" (L502), "Worth" (L506) and "Foundations" (L562). The owner asked for an example before any general statement.

### 54. [Consistency, Low] Divergence from the word sheet (for the orchestrator)
- **Doc L194, L785:** "widening factor". The word sheet says "stretch factor". The doc is consistent with itself, so either sheet or doc should be changed so later writers match.

---

## Coverage: sentences of draft 4 not rendered (all Low)

- **C1.** An outside reader's note bearing on the sufficiency claim is missing from "What is still open". The S88 reading of Atria's reply records that "The identity account (E = D) … passes all four conditions trivially", not offered as a failure and "not ruled on". Doc L576 says only that the reader "offered none". This is from the record, not the theory, but section 13 is where it belongs.
- **C2.** D4 L13: "Declaration is permitted only as a modelling convenience". Doc L360 gives only "No claim of creativity may rest on it".
- **C3.** D4 L255, first sentence: "The answer follows by evaluating \(E\) under its independent boundary conditions."
- **C4.** D4 L481: the variation operator is "physically admitted" and the survival condition is "enacted by the environment".
- **C5.** D4 L161: a faulty question's "formulation is still an event".
- **C6.** D4 L569: "A coarsening is not a recoding (Derivation 8)" is not given with Derivation 2. Section 8 covers blurring under Derivation 8, so this is minor.

---

## What was checked and holds

- Every fixed verdict quoted matches its case book: O-cases, N-cases and D3-T. Truncations are noted above where they matter (O12).
- Every "ruled on file 11" mark matches S81: 46 agree and 6 silent (O1, O12, O21, O27, O35, O50). O20 and O40 are S75 corrections and are rightly "agrees". O45 is rightly one of the two moves toward.
- The Greta account of the round (4 of 5 silent, Mimo's retry "falls", a fresh determiner upholding at medium) matches S81 Results.
- Derivation 2's defeat "stands triggered for files 10 and 11" matches the Status record. The "sketch … not a proof" remark on Derivation 5 and the project's ruling (a step missing, outside the defeat list) match the S88 reading. The correction-sticks analysis's finding that only the record tells a retreat from an honest limit matches its text.
- The new paragraphs (Rivals, Problems, A failed answer stays failed) are rendered closely, apart from items 7, 8, 11, 25, 27 and 28. The case views for O24, O36, O45, O48, D3-T, N1, N2, N4, N5, N7, N25 and O27 match the CASES AT RISK notes.
