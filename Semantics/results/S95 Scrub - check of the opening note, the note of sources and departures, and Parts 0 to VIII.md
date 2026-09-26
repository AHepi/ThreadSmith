# S95 Scrub — check of the opening note, the note of sources and departures, and Parts 0 to VIII

*25 September 2026, log S95, under decision S23. Checker: Claude, who did not write the vocabulary or the scrubbed text. Not committed.*

Compared, lines 1 to 372 (title, the experiment note at l. 2, Part 0 with its "Two words" note at l. 8, and Parts I to VIII): draft 5 (`tests/Revision 2 - file 13 draft 5, theory text.md`, md5 7f1d8ad02adf96e27622593bd263252e) against the scrubbed text (`tests/Revision 2 - file 13 draft 5, scrubbed of verificationist words, theory text.md`, md5 2517ef4ec1f274e8de2bfb7e6661ef94). The two texts share line numbers. A program listed the lines that differ and gave word-level differences; every differing line was read in full, and a second program searched the whole range, changed lines and unchanged ones, for the forbidden words, their synonyms, belief words and authority words. Line numbers below are the shared ones.

The owner's instruction, quoted exactly:

> Next step. Get rid of all words that imply verificationism and see if the semantics still holds. Forbidden words and phrases.
>
> Fits, supports, supported, verifies, verified, corroborates, corroborated, proves, proved, disproves, disproved, reason to believe, reason to reject. In fact, anything belief related at all must be scrubbed. Better than, worse than, true, not true, more true, established, authority, foundation, foundational, derived, derived from. Anything that could imply some sort of foundational truth or authority. Anything that could be interpreted as needing verification or falsification in any absolute sense. Anything that is accepted is always tentatively, and mean anywhere that "accept" or "accepted" is used.
>
> Also, argument is short hand for: reasons why this and not that. Not reasons for this and not that. An argument is merely something that can be strung together into a coherent structure to decide why this and not another.

## Verdict for this range: HOLDS WITH REPAIRS

None of the listed words is left in the range: fits, support, verify, corroborate, prove, disprove, true, established, authority, foundation and derived are all gone, and so are truth, fact, knowledge, belief, expectation, primitive, anchor, witness, correct, genuine and "Derivation". "Accept" appears twice, at l. 8 where it is defined as tentative and at l. 67 as "tentatively accepts". "Argument" is always a structure that rules out a denial or a rival for someone who can use it, and never a reason for a claim. Every numbered reference to Arguments 1 to 10 in the range points to the same item as the matching Derivation in draft 5; a program compared them line by line.

In this range the semantics still works in the new words. Organizations, kinds as edit-signatures, questions and contracts, the three provenances, representation, (E) with its four conditions, routes and criticality, rivals and problems, the exact constructions, and the transport results are all defined as before. The mathematical arguments (finite monotone claim, functional transport, approximate transport, odd-order skew-symmetric matrices) keep every step. What draft 5 said with a positive status ("established", "fits") is now said with exclusions only ("ruled out for j", "not ruled out"), and no step in the range needed the positive status.

Two kinds of repair are needed. (1) A few places break: the new word "rules out" is never defined for an argument as a whole; l. 369 points to a Part VI definition that no longer covers what l. 369 applies it to; one step at l. 317 no longer goes through; one sentence at l. 277 has become empty; and a few other sentences no longer say what their paragraphs need. (2) Some residue is left: "rule out" is used without an assessor in several places, which is falsification in the absolute sense; two authority words remain in lines the scrub did not touch; and the belief words "surprise" and "recognized" are still in Part IV. Each item below comes with its wording.

---

## Residue

Words or phrases in the range that still carry verification or falsification in an absolute sense, justification, belief, authority or ranking, or that go against the vocabulary's own rule ("rule out … Used only for an argument usable by someone, lasting while it stays usable").

1. **l. 8, the step clause: "Each of its steps rules out the case in which the step's premises are met and its conclusion fails (Part IX)."** This "rules out" names no assessor and has no limit on how long it lasts, so it is the absolute sense. It is also a second sense of the word, next to the one the same line gives for arguments ("for someone who can use it, and only while it stays usable"). Part IX does not contain the clause either. What Part IX has is \(\operatorname{Form}_j(u)\), "the inference form of u is one j admits", and that is where the step's force belongs. Repair R1.

2. **l. 17: "An explanatory achievement that these four cannot represent would rule out the conjecture; so would a candidate that meets all four and explains nothing."** The subject is a case, not an argument, and no one is named for whom it rules the conjecture out. That is falsification in the absolute sense. It is also stronger than draft 5's "counts against", which was a weight (and a weight is a "reason to reject", so it had to go). Repair R2.

3. **l. 47 "Part XV names what would rule it out"; l. 61 "together with what would rule out each"; l. 335 "does not rule out the scoped result".** The same absolute "rule out", with a case or a change as subject. This is milder at l. 47 and l. 61, which are hypothetical, and a plain mismatch at l. 335, where the subject is a change to the state space. Repairs R3 and R17.

4. **l. 317: "an answer it rules out stays ruled out" (the test is the subject) and "a test inside \(C\) can rule out one of them".** Here a test rules out, where the vocabulary keeps "rule out" for arguments. Repair R14.

5. **Authority words in lines the scrub did not touch: l. 47 "Part IV forbids the reduction"; l. 161 "What is prohibited is changing \(C\) or \(\mathcal Q\) during an assessment without recording that the claim has changed."** Both put the text in the position of a lawgiver. The owner's instruction covers "anything that could imply some sort of … authority." Repairs R3 and R4.

6. **l. 211: "a later record made from the carrier is not a second, independent trace of its history."** "Trace" replaces "witness", but "second, independent witness" was the vocabulary of corroboration: a copy does not corroborate. The idea is still there under the new noun. What the sentence needs is only that a copy has no provenance of its own. Repair R5.

7. **l. 215, 221, 223: "surprise", "surprised"; l. 223 and l. 317: "recognized difficulty".** These are attitude words. Surprise implies an expectation someone held, and recognizing is a way of knowing. The owner: "anything belief related at all must be scrubbed." Both are defined without any attitude: surprise is a violation of a selected transport at \((a,b)\notin H\), and a recognized difficulty is a represented failure or conflict (Part X, l. 429). But the words carry belief in ordinary use. The scrub kept "surprise" and put it to the owner in the marker at l. 443, which is outside this range, and nothing at l. 215 to 223 points a reader to that marker. "Recognized" is not marked anywhere. This is the owner's call. Repair R6 gives both options.

8. **Borderline. l. 43: "The physical theory fixes which changes are possible at all" and "What is independent of the modeller lies in the physics".** Read without l. 75, "the physical theory" is the last word on what is possible. Read with l. 75 ("to adopt something is to take it tentatively"), it is the adopted theory and is tentative. The sentence does not say which reading it means, and "the physics" also runs together the adopted theory, which somebody chose, and the world it describes. Repair R7.

9. **Borderline. l. 8: "what it does is rule out a claim's denial".** To rule out ¬P is, in classical logic, to have P. That is a proof under another name, unless nothing then gives P a status. Nothing in the range does. But l. 8 says only that a claim that is not ruled out "gets nothing from that". It does not say the same of a claim whose denial is ruled out, and that is the half a justificationist would reach for. The same goes for the proof heading "*Why this and not its denial.*" (l. 305, l. 353). Repair R1 says it outright.

10. **Borderline. l. 201: "that is the usual arrangement, not a requirement".** "Expected" (an attitude) became "usual", which is a claim about frequency in physical systems that the text gives no argument for. Repair R10.

Considered and **not** residue:
- "meets" and "fails" (E) are world-level predicates with no assessor. They are what an assessor's arguments are about. They need no verification, and they match S21's "It must match reality, but not by some fixed infallible metric."
- "in error" is the owner's word, and l. 211 defines it as the content's transport to the world failing.
- "faithful" and "fidelity" are the theory's structural relation.
- "tested" and "testable" are used in the sense of an attempt to rule out.
- Within this range, "admit", "admits" and "admitted" always mean "allows as possible" (a physics, a population, an organization, the world), never a person accepting something. Part IX's "one j admits" is a person's acceptance, but it lies outside this range; see R1.
- "decide" is the owner's own verb.
- l. 61's "in the order of how much falls if they fail" orders claims by what depends on them, not by merit.

---

## Broken

1. **The argument-level "rules out" has no definition (l. 8, used at l. 315, 317, 369).** l. 8 says what a step rules out. l. 315 defines "ruled out for j" by "an argument usable by j … rules out that the candidate meets (E)", and Part IX's \(R_j(\psi)\) is "the arguments usable by j that rule out ψ". Nowhere is it said when an *argument* rules out a *claim*. Draft 5 did not need this, because a receipt was "for" a result. Repair R1 adds the definition: an argument rules out a claim when the claim is inconsistent with its conclusion.

2. **l. 369: "Here "ruled out" is meant as in Part VI: the assessor holds an argument … that rules out \(y\) as the target's answer at \((a,b)\)".** Part VI (l. 315) now defines "ruled out" for a candidate only ("rules out that the candidate meets (E)"). l. 369 applies it to an answer. In draft 5 the pointer worked, because l. 315 defined "established" for a result and l. 369 applied it to a result. The step from "y is ruled out as the target's answer" to "every such candidate is ruled out" also needs (A) and the candidate's own answer, and the gloss does not say so. Repairs R13 and R18.

3. **l. 317 (i): the test "solves the problem whatever it records, since an argument from what it records rules out at least one of them".** The problem is "for that assessor", but the argument from the record is not said to be usable by that assessor. By (K2) and (K3) it rules out nothing for j unless j's premises about the test's background and instruments are live and j admits its form. In draft 5 this came built into "establishing it" and "at most one of them fits [what is established for an assessor]". Without it, "solves the problem" does not follow. Repair R14.

4. **l. 317: "of one candidate, the only thing said is whether it is ruled out for an assessor".** The same paragraph also says of one candidate whether it is an account of \(p\) ("at most one of them is an account of \(p\)"; "where both meet (E) on \(C\) both are accounts of \(p\)"; "whether a candidate is an account of a question is fixed by the candidate, the question and the world"). So the new sentence is false of its own paragraph. Repair R15.

5. **l. 277: "(E) does not exclude a mechanism that meets (E) whatever led anyone to guess it".** Nothing that meets (E) is excluded by (E), so the head of this sentence is empty, and its content has moved to the subordinate clause. Draft 5's point was that (E) has no condition on origin: "a true mechanism guessed for bad reasons" is not excluded. Repair R11 says this.

6. **l. 17: the defeaters are stated in a predicate that l. 31 now declines to take as an import.** l. 31 now reads the refused predicate as "'explains' without a question and a contract". l. 17 uses "explains nothing" and "an explanatory achievement" with no question, no contract, and (with "genuine" and "plainly" dropped) no word on how either is to be told apart from (E). Draft 5's "genuine" and "plainly" pointed, however loosely, to a judgement made without (E). Part XV (B) already carries the fix: "argued to be one and not a non-explanation by an argument that does not use (E)". l. 17 should say the same. Repair R2.

7. **l. 299: "route" is used before it is defined.** "Criticality is relative to the route \(W\) it is assessed in" comes before l. 307's "Here a route of the candidate is a member of \(\mathsf S\)". Draft 5's "support" was used in the same order, but "support" of an account more or less explained itself. "Route" does not, and from here on it also names two things: a member of \(\mathsf S\) (a set of commitments, Part VI) and, in "active route", a subnetwork of occurrences in a history (Part IX). l. 307 separates them, but only after the first use. Repair R12.

8. **l. 151 and l. 331: "faithful" is applied to things that are not transports.** l. 151 has "a prediction from it that is faithful on the contract", and l. 331 has "its content might be faithful on the contract". Fidelity is defined for a transport (l. 189). A prediction is \(\operatorname{Ans}_S(\tau(a),\sigma(b))\) (l. 219), and the "content" at l. 331 is a chosen value of \(b_B\). Draft 5 had "reliable" and "true", which were informal. Their replacements use a defined term outside its definition. Repairs R8 and R16.

9. **l. 159: "leaves open whether the restriction drops changes the question asked contains".** The question asked has the restricted contract (same line: "An account at a stated scope answers the question asked at that scope"), so a restriction never drops a change that this question contains, and the sentence always comes out "no". It also reads as a garden path ("drops changes the question…"). This reading of draft 5's "appropriate" either says nothing or depends on a question-before-restriction that the text does not name. The first sentence of the paragraph, which is contrastive, already carries the point. Repair R9.

No other definition, cross-reference or argument in the range is affected. Specifically:
- l. 245's "no component … whose signature differs from its counterpart's meets (F1)" is the contrapositive of draft 5's "(F1) entails that every component … has the signature of its anchor", and it agrees with the Claim of Argument 1.
- l. 317's "(Argument 2, Consequence)" points to the sentence at l. 568 that it paraphrases.
- "counterpart" was not used in draft 5, so the rename of "anchor" does not collide with anything.
- "prediction" matches draft 5's own l. 177 ("whose queries are predictions").
- "import" is defined by l. 31 before it is used.
- l. 8 defines "argument" and "tentatively accept" before either is first used.

---

## Changed claims

Draft 5 wording, then scrubbed wording, then the reading. "Intended" means only a verificationist, belief or authority commitment has been removed. "More" means the sentence now says something else as well.

1. **l. 2 and l. 8 (new text on lines that are blank in draft 5).** The experiment note, and the definitions of *argument* (the owner's words, quoted exactly) and *tentatively accept* (a person's choice "for whatever reason", which is the owner's phrase from S21). Intended. There is one addition beyond the owner's words, the step clause, and it is residue 1.

2. **l. 13.** Draft 5: "Declaration is permitted only as a modelling convenience". Scrubbed: "Declaration is used only as a modelling convenience". A rule has become a description. The restriction survives in the rest of the sentence ("a claim about creativity cannot depend on it"). Intended.

3. **l. 17.** Draft 5: "A genuine explanatory achievement that these four cannot represent counts against the conjecture. A candidate that satisfies all four while plainly explaining nothing counts against it too. Part XV lists what would count." Scrubbed: "An explanatory achievement that these four cannot represent would rule out the conjecture; so would a candidate that meets all four and explains nothing. Part XV lists what would rule it out." **More.** A weight has become an exclusion with no assessor (residue 2), and the requirement that the defeater be judged independently has been lost (broken 6).

4. **l. 25.** Draft 5: "an objective aesthetics, a probability of truth, a merit function, a measure of worth, or a ranking of thinkers … a claim of worth … is unsettled … a division of credit among contributors beyond what a history establishes". Scrubbed: "an aesthetics independent of any declared appraisal, a probability on claims, an appraisal of its own, or a function that orders explanations or thinkers … a claim that invokes an appraisal … is left open … divide an achievement among contributors beyond what a history contains". Intended, with two small changes. The refusal now also covers ordering explanations (the merit function had covered that). And "divide an achievement" is not "divide the credit". Repair R19 restores "attribute".

5. **l. 27.** Draft 5: "It does not prove that any human … belongs". Scrubbed: "It does not decide whether any human … belongs". The disclaimer is wider: it now also disclaims ruling membership out. That is true of the semantics alone, since membership needs a history the semantics does not supply. Intended.

6. **l. 31.** Draft 5: 'No predicate meaning "really explains", "is a cause" or "is knowledge" is taken as primitive'. Scrubbed: 'No predicate that says "explains" without a question and a contract, or "is a cause", or "is a created explanation", is taken as an import'. The rewriter flagged this: "really explains" is read as bare "explains" (Claude's reading), and "knowledge" is provisionally renamed. **More**, because this reading turns l. 17's "explains nothing" into the refused predicate (broken 6). "A predicate that could be true or false" becomes "a predicate that a case meets or fails". Intended.

7. **l. 39.** Draft 5: "which is correct rather than a loss". Scrubbed: "which is what that level contains, not a loss". Intended.

8. **l. 41.** The objection "made truth a matter of survival" becomes "made fidelity a matter of survival". "Is a fact about the transport and the world, independent of whether it survived" becomes "turns on the transport and the world alone, not on whether it survived". The reply is unchanged in substance. The critic's own word has been replaced (see losses).

9. **l. 43.** Draft 5: "and there is no objectivity … Within any contract there is a fact of the matter about fidelity … Objectivity lives in the physics and the fidelity facts; scope-honesty lives in the record." Scrubbed: "and nothing is independent of the modeller … Within any contract, whether a transport is faithful at a pair turns on the transport and the target, and no assessor appears in (E) … What is independent of the modeller lies in the physics and in fidelity; what the modeller chose to leave out lies in the stated scope, and so in the record." Intended. The new reply is sharper: the independence it claims is that (E) names no assessor. It now says outright that "the physics" is independent of the modeller, which is residue 8.

10. **l. 51.** "does not pretend to know which aesthetic reasons are true" becomes "does not decide between rival aesthetic reasons". Intended, and contrastive.

11. **l. 55.** "Derivation 7 shows the two are consistent" becomes "Argument 7 rules out a conflict between them". Same claim.

12. **l. 57.** The critic's "Kinds obviously exist" becomes "Kinds exist". Intended. The opponent's words are altered.

13. **l. 67.** Heading "Explanatory realism" becomes "Faithfulness without assessors", and "whether anyone accepts it" becomes "whether anyone tentatively accepts it". Intended. The content still commits to a world that transports can match or fail to match. The name linking the commitment to Deutsch's realism is gone (see losses).

14. **l. 71.** "An idea may be entertained without justification … act on an appraisal without certifying it" becomes "entertained with no argument that rules out its rivals … act on an appraisal that no argument has decided". Intended. It now says specifically what a conjecture may lack.

15. **l. 75.** "obligations" becomes "conditions", "must be permitted by" becomes "must be possible under", a tentativeness declaration for "adopt" is added, and "holds so far as" becomes "reaches as far as". Intended.

16. **l. 151.** "with a reliable prediction from it" becomes "with a prediction from it that is faithful on the contract". **More**: a defined term has been applied outside its definition (broken 8).

17. **l. 159.** "What makes a restriction appropriate to the question asked … supplies no rule that certifies it. Meeting the conditions of an account … does not certify the restriction as appropriate." becomes "Why the question asked is answered on this restriction and not on a wider one … supplies no rule that decides it. Meeting the conditions … leaves open whether the restriction drops changes the question asked contains." The first sentence is intended and is contrastive. The second is **more**: "appropriate" has been narrowed to a reading that says nothing (broken 9).

18. **l. 201.** "the expected arrangement" becomes "the usual arrangement". A small change of claim: an anticipation has become a frequency (residue 10).

19. **l. 211.** "fidelity fact" becomes "fidelity relation", "false theory" becomes "theory in error" (now defined in the same sentence), and "independent witness to" becomes "independent trace of". The claims are the same; for the last, see residue 6.

20. **l. 245.** "(F1) entails that every component of \(E\) has the signature of its anchor" becomes "no component of \(E\) whose signature differs from its counterpart's meets (F1)". Same claim (contrapositive). "wrong decomposition" becomes "decomposition in error", and "locally correct pieces" becomes "pieces each faithful locally". Same claims.

21. **l. 277.** Draft 5: "(E) does not exclude a true mechanism guessed for bad reasons; the reasons for adopting it are assessed elsewhere (Part IX). It does not prefer an elegant account to a less elegant one with the same fidelity. … its strength is fixed by its contract". Scrubbed: "(E) does not exclude a mechanism that meets (E) whatever led anyone to guess it; how it came to be taken up is assessed elsewhere (Part IX). It draws no line between two candidates with the same fidelity that differ only in elegance: both meet it or both fail it. … what it answers is fixed by its contract". The first sentence is **more**: it is wider (any origin, not only bad reasons) and its head is empty (broken 5). The elegance sentence is intended and exact. "Strength" becoming "what it answers" is intended.

22. **l. 281.** "a component anchored to the wrong one" becomes "a component whose counterpart is of the other kind". Same claim ("the other" of the two kinds the change separates).

23. **l. 285 to 313.** "support" becomes "route", "theorem" becomes "claim", "*Proof.*" becomes "*Why this and not its denial.*", and "singleton witness" becomes "singleton instance". "Success of a subset does not imply success of the whole" becomes "A subset can meet (E) while the whole fails it". The claims are the same, and every step of the finite monotone argument still goes through. See broken 7 for "route".

24. **l. 315.** Draft 5: "A result is **established** for an assessor who holds a usable receipt for it … A candidate **fits** what is established for an assessor when no result established for that assessor shows it failing a condition of (E)." Scrubbed: "A candidate is **ruled out** for an assessor \(j\) when an argument usable by \(j\) (Part IX) rules out that the candidate meets (E) … A candidate is **not ruled out** for \(j\) when no argument usable by \(j\) rules it out." The rewriter flagged this. The positive status is gone and only the exclusion is left. Intended, and this is the central change. "Fits" (no established result shows it failing) and "not ruled out" (no usable argument rules it out) pick out the same candidates as far as a usable receipt and a usable argument come to the same thing, and the scrub makes them the same thing (Part IX), so nothing downstream in the range changes its extension.

25. **l. 317.** Four changes:
    - (a) "since afterwards at most one of them fits; an answer it refutes stays refuted on \(p\)" becomes "since an argument from what it records rules out at least one of them for as long as that argument stays usable; an answer it rules out stays ruled out on \(p\) for as long as the argument that rules it out stays usable". Flagged by the rewriter. The permanence at the assessor's level is intended to go. The permanence at the world level stays at l. 369's first sentence. What is left of "stays … on \(p\)" is the index, which means a later question does not lift the exclusion. The step is weaker (broken 3).
    - (b) "the term says nothing about which of them is right" becomes "which of them, and not the other, is an account on a finer contract". Intended; it is more exact.
    - (c) "a claim that one is right and the other wrong is a claim that some admitted change outside \(C\) separates them" becomes "a claim that one of them and not the other meets (E) on a contract with some admitted change outside \(C\) is a claim that such a change separates them". Intended. The claim now follows almost by definition. The substance is what remains: the claimant "must supply it".
    - (d) "Nothing here counts rivals, grades a candidate or ranks candidates." becomes the same with an added clause, and that clause is false of its own paragraph (broken 4).

26. **l. 325, 335, 339, 343, 353, 363, 365.** "derived from" becomes "set by", "establish" becomes "suffice for", "refute" becomes "rule out", "anchored to" becomes "has as its counterpart", "offered as adequate" becomes "offered as an account", "witnessed by" becomes "met: … is an instance", "satisfies" becomes "meets the bound", and "*Proof.*" becomes "*Why this and not its denial.*". The claims are the same, except for l. 335's subject for "rule out" (residue 3).

27. **l. 331.** "its support is circular though its content might be true" becomes "it is circular, though its content might be faithful on the contract". The circularity is now said of the choice itself rather than of its support, which is intended and consistent with l. 8: a choice made "for whatever reason" is not an inference. "Faithful" is misapplied (broken 8).

28. **l. 369.** "Once it is established for an assessor that the target's answer at \((a,b)\) is not \(y\), this is established … of every such candidate alike" becomes "Once an argument usable by an assessor rules out \(y\) as the target's answer at \((a,b)\), every such candidate alike is ruled out for that assessor". "the exclusion ceases to be established" becomes "those candidates are no longer ruled out by it". "no candidate is thereby shown to be an account" becomes "no candidate becomes an account by that". Intended. The "as in Part VI" pointer is broken (broken 2).

---

## Losses

- **A positive status for an assessor.** The range can no longer say that a result (for example "the target's answer at \((a,b)\) is \(y_0\)") is anything for anyone. It can say only that rival values are ruled out. No definition or argument in the range needed the positive form: the test of l. 317 and the frozen failure of l. 369 both go through as exclusions. What is lost is a way of speaking, not a result.
- **Permanence of an exclusion at the assessor's level** (l. 317, 369). This was an absolute, and the owner asked for it to go. The world-level permanence ("by (A) … is not an account of \(p\)") stays.
- **The critics' own words.** Objections 3, 4 and 11 (l. 41, 43, 57) are now stated in the text's vocabulary ("fidelity", "independent of the modeller", no "obviously"). The replies answer the objection as reworded. A reader who holds the objection in terms of *truth* or *objectivity* no longer sees it quoted and answered. A note at l. 35 could say that objections are restated in the text's words.
- **The names "Explanatory realism" and "scope-honesty"** (l. 43, 67). The content is kept. What is lost is the explicit tie to the realism of the sources.
- **"Genuine" at l. 17** (independence of the defeater from the conjecture), until R2 restores it in contrastive form.
- **Draft 5's broader notion of an "appropriate" restriction** (l. 159). The narrowed reading loses it. R9 restores the breadth without the appraisal word.
- **"A true mechanism guessed for bad reasons"** (l. 277). The specific point that bad reasons for a guess do not disqualify the mechanism is now only implicit. R11 restores it as a statement about what (E) contains.

## Gains

- **l. 8 puts the owner's two definitions at the top**, and separates acceptance (a person's choice, "for whatever reason", always tentative) from anything the semantics defines. This matches S21's "sees no option but to choose the one that isn't ruled out by its best argument". The semantics supplies the "ruled out", and the choosing belongs to the person.
- **Only exclusions, and they are tentative.** "Not ruled out … gets nothing from that" removes draft 5's justificationist asymmetry, in which a candidate *fit* what was *established*. Every exclusion is now tied to an argument someone can use and lasts only while that argument stays usable. That is fallibilism in Deutsch's and Marletto's sense, stated in the text's own terms.
- **Two levels made visible.** World-level "meets or fails (E)", with no assessor, is kept apart from assessor-level "ruled out for j". Draft 5 mixed "established", "fits", "refuted" and "right" across these levels. l. 43's reply ("no assessor appears in (E)") and l. 67's heading now say where independence from anyone's view lies without the word "fact".
- **Contrastive statements.** "One of them and not the other", "why … on this restriction and not on a wider one", "*Why this and not its denial*" and "a conflict … that no argument … has decided" all use the owner's "why this and not that" and Deutsch's "a problem is a conflict between ideas".
- **"Import" for "primitive"** says where \(\Theta\) and \(\mathcal N\) come from, not what standing they have.
- **l. 245** now states what (F1) excludes, instead of an entailment claim.
- **l. 277's elegance sentence** is exact: two candidates that differ only in elegance both meet (E) or both fail it.

---

## Repairs (exact wordings, in the scrubbed vocabulary)

**R1 (l. 8; residue 1 and 9, broken 1).** Replace "Each of its steps rules out the case in which the step's premises are met and its conclusion fails (Part IX). An argument is never a reason *for* a claim: what it does is rule out a claim's denial, or a rival, for someone who can use it, and only while it stays usable (K2); a claim that no argument rules out is only not ruled out, and gets nothing from that." with:

> Each of its steps is of an inference form that the person using it admits (\(\operatorname{Form}_j\), Part IX), and admitting a form, like accepting a claim, is tentative; for that person, while the form stays admitted, the step rules out the case in which its premises are met and its conclusion fails. An argument rules out a claim when the claim is inconsistent with its conclusion. An argument is never a reason *for* a claim: what it does is rule out a claim's denial, or a rival, for someone who can use it, and only while it stays usable (K2). A claim that no argument rules out is only not ruled out, and gets nothing from that; a claim whose denial an argument rules out gets nothing more than that ruling out.

**R2 (l. 17; residue 2, broken 6).** Replace the last two sentences with:

> An explanatory achievement that these four cannot represent, argued to be one by an argument that does not use them, would conflict with the conjecture; so would a candidate that meets all four and that such an argument rules out as an explanation on its question and contract. An argument that exhibits either rules the conjecture out for whoever can use it, while it stays usable. Part XV lists what such an argument would have to exhibit.

**R3 (l. 47 and l. 61; residue 3 and 5).** l. 47: "Nothing about construction is reduced to selection; Part IV keeps the two apart by what their histories contain, and Part XV names what an argument would have to exhibit to rule that out." l. 61: "…are stated exactly in Part XV together with what an argument would have to exhibit to rule out each."

**R4 (l. 161; residue 5).** Replace "What is prohibited is changing \(C\) or \(\mathcal Q\) during an assessment without recording that the claim has changed." with:

> An assessment is an event with a frozen contract (Part 0, grievance 10): a change to \(C\) or \(\mathcal Q\) during it, left unrecorded, makes the record name a claim other than the one assessed.

**R5 (l. 211; residue 6).** "A carrier keeps its provenance when present access to it is lost, and a later record made from the carrier carries that provenance, not a second, independent one."

**R6 (l. 215 to 223, l. 317; residue 7; the owner's call).** Option A, rename: at l. 221, "- an **unshaped violation** is a violation of a selected transport at \((a,b)\notin H\)." At l. 223: "A system with no transport has no unshaped violation. A system whose history exhausts its contract has none either. An unshaped violation requires an incomplete selection history: …; prediction and violation are defined for every transport to the simulation layer, unshaped violation only for a selected one: a constructed one that fails at an actually occurring pair of its contract is violated, and the failure is not an unshaped violation; a violation the system represents can be a **registered difficulty** (Part X)." The heading at l. 215 becomes "## Prediction and violation", and "recognized difficulty" becomes "registered difficulty" at l. 317 and in Part X. Option B, keep and point: at the end of l. 221 add "(the name is provisional; see the marker in Part XI)", and give "recognized difficulty" the same pointer at its first use (l. 223).

**R7 (l. 43; residue 8).** "The adopted physical theory says which changes are possible at all." Last sentence: "What is independent of the modeller lies in the world the adopted physics describes and in fidelity; what the modeller chose to leave out lies in the stated scope, and so in the record."

**R8 (l. 151; broken 8).** "A measure that identifies an outcome, together with a prediction of the outcome from it through a transport faithful on the contract, answers the identification question; …"

**R9 (l. 159; broken 9).** Replace "Meeting the conditions of an account (Part V) on the restricted contract leaves open whether the restriction drops changes the question asked contains." with:

> Meeting the conditions of an account (Part V) on the restricted contract leaves open why the claim is made on this restriction and not on a wider one.

**R10 (l. 201; residue 10).** "…that is one arrangement, not a requirement."

**R11 (l. 277; broken 5).** Replace the first sentence with:

> (E) has no condition on how a mechanism came to be guessed: a mechanism meets (E) or fails it whatever led anyone to guess it, and how it came to be taken up is assessed elsewhere (Part IX).

**R12 (l. 299; broken 7).** "Criticality is relative to the route \(W\) it is assessed in, a **route** of the candidate being a member of \(\mathsf S_{E,p}\) (not an active route of a history, Part IX): …" At l. 307, "Here a route of the candidate is a member of \(\mathsf S\)" can then become "A route of the candidate".

**R13 (l. 315; broken 2).** Replace "A candidate is **ruled out** for an assessor \(j\) when an argument usable by \(j\) (Part IX) rules out that the candidate meets (E);" with:

> A claim is **ruled out** for an assessor \(j\) when an argument usable by \(j\) (Part IX) rules it out, and a candidate is ruled out for \(j\) when the claim that it meets (E) is;

**R14 (l. 317; residue 4, broken 3).** In (i): "…is a **test** that solves the problem for that assessor whatever it records, so long as the premises about the test's background and instruments are live for that assessor (K2, K3): an argument from what it records then rules out at least one of them for that assessor, while it stays usable; an answer that such an argument rules out stays ruled out on \(p\) for as long as the argument stays usable (Part VIII)." In (ii): "…an argument from a test inside \(C\) can rule out one of them without the other only for a failure of its own…"

**R15 (l. 317; broken 4).** "Nothing here counts rivals or orders candidates: of one candidate, what is said is whether it meets (E) on a contract and whether it is ruled out for an assessor; of two, whether they conflict."

**R16 (l. 331; broken 8).** "…is not an inference from the readings; it is circular, though the value it sets might be the target's."

**R17 (l. 335; residue 3).** "…permitting division changes the state space and makes a new question (Part III); the scoped result on its own question is as it was."

**R18 (l. 369; broken 2).** "Here "ruled out" is meant as in Part VI: the assessor holds an argument usable by that assessor (Part IX) that rules out the claim that \(y\) is the target's answer at \((a,b)\); joined to a candidate's own answer \(y\) there and to (A), it rules out that the candidate meets (E); and by (K3) an argument from the test that records it rules out a candidate only together with the background and instruments the test uses."

**R19 (l. 25; changed claim 4).** "It does not attribute an achievement to contributors beyond what a history contains (Part XI)."

Optional clarity, with no change of claim: l. 305 "Deletion of \(d\) from \(\Gamma\) leaves \(\Gamma\setminus\{d\}\) a route exactly when a minimal route omits \(d\)." l. 311 "no minimal route, and no route of one commitment, exists."

**For the Part IX checker (outside this range):** "\(\operatorname{Form}_j(u)\): the inference form of u is one j admits" is a person's acceptance. Nothing in Part IX declares it tentative, and l. 75 declares only "adopt". R1 covers it from l. 8. Part IX's "rule out" for arguments should match R1's definition.
