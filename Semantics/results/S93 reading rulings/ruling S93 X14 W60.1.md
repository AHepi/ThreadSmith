# Ruling S93 X14 W60.1: a failed answer stays failed

*Written on 25 September 2026 by a fresh Claude checker, under rules 4, 5, 6, 9, 10, 11 and 12 of `results/S93 How the cross-examination of draft 4 will be read - written before sending.md`. I did not draft, assemble or check the change list, did not write the briefs, and had read no S93 reply before the two named here.*

*Read, in this order: the reading rule; decision S20 and lesson S26; in `results/S93 Tabulation of the replies, before any ruling.md`, section 2.2's entry for X14, section 3.8, sections 6.2 and 6.3, and section 7's X14 entry; the replies `s93_xexam_atria_C.response.txt` and `s93_xexam_mimo_C.response.txt` (response files only); the brief `tests/S93 Cross-examination - draft 4 - part C, a failed answer stays failed.md` (md5 902c9ea16de250837e05a607aaf6179d, as the reading rule gives it); W60.1 in `tests/Revision 2 - change list, draft of 23 September.md` (md5 b6b2ea95ea9e21ebea3316d8e9fa4b40); the draft-4 theory text `tests/Revision 2 - file 13 draft 4, theory text.md` (md5 fc55b470c63cd4b3c27d6aa64d8d8c17) at L131–163, L229–283, L285–319, L351–370, L373–400, L524, L542, L572 and L602–608; and, for background only, the correction-sticks analysis of 24 September (its body, sections 0 to 6, and Appendix A (b)).*

*What else was seen. Sections 6.2 and 6.3 were read whole, so their rows for other items were seen; 6.3 has no X14 row. Printing section 7 also showed the other items' routing lines, and printing section 2.2 showed the last line of the X13 entry. Nothing in them is relied on here. No other ruling, no reasoning, request, receipt or attempt file, no key file and nothing in `authority/` was opened.*

*How quotations were checked. A short script matched each quoted run against draft 4 and the brief, after stripping LaTeX delimiters, emphasis and differences of quote mark. Every miss was then checked by hand. Line numbers without a prefix are draft 4's; "brief L" numbers are the part-C brief's.*

## The entry

**W60.1: Part VIII, a failed answer stays failed.**
- **Group:** H.
- **Place:** inserted after "Historical index", at draft 4 L369 (file 11 L365).
- **REASON WORD:** clarification.
- **KIND:** CLAIM.

**OLD:**

````text
A new index is a new claim.
````

**NEW:**

````text
A new index is a new claim.

**A failed answer stays failed.** Fix a question \(p\), a pair \((a,b)\in C\) and a value \(y\neq\operatorname{Ans}_p(a,b)\). By (A), a candidate for \(p\) whose answer at \((a,b)\) is \(y\), \(\operatorname{Ans}_E(\tau(a),\sigma(b))=y\), is not an account of \(p\), whether it is the candidate that gave \(y\) there and failed, that candidate offered again, a rival, or a changed candidate that keeps \(y\) there; and the same holds on every question with the same target and query whose contract contains \((a,b)\). Once it is established for an assessor that the target's answer at \((a,b)\) is not \(y\), this is established for that assessor of every such candidate alike, from the candidate's own answer there, with no record of which candidates failed before or of how any was changed. Here "established" is meant as in Part VI: the assessor holds a usable receipt for the target's answer at \((a,b)\) (Part IX), and by (K3) the test that yields it tells against a candidate only together with the background and instruments it relies on. If a premise about them ceases to be live, the receipt is not usable and the exclusion ceases to be established, for every such candidate alike; no candidate is thereby shown to be an account (K2). A contract that omits \((a,b)\), or a changed query, makes a different question (Part III): an account on it does not answer \(p\), and the failure on \(p\) stands (Historical index).
````

**DECLARATION:**

> Part VIII now states that on a question, a candidate whose answer at a pair of the contract differs from the target's is not an account of it, nor of any question with the same target and query whose contract contains that pair, whatever candidate it is. Once the target's answer there is established for an assessor, by a usable receipt, this is established for that assessor of every such candidate alike, from its own answer there, with no record of earlier failures or changes. By (K3) the exclusion is established only together with the background and instruments of the test; if a premise about them ceases to be live, it ceases to be established for every such candidate alike, without any candidate being shown to be an account. A contract omitting the pair, or a changed query, makes a different question, an account on which does not answer the original, whose failure stands.

**CHECK** (as it stands):

- Drafted 25 September on the owner's position (rivals and problems); model-tested and attacked; not yet cross-examined by Atria or Mimo. OLD occurs once in file 11. Each claim was checked against (A), D3:L151, D3:L159, D3:L363, (K2) and (K3) in draft 3 (see REASON).
  - The text attack (03a) found it true under its hypotheses, including (K3)'s caveat, once three phrases were made exact: the assessor is named; "alike" is "from the candidate's own answer there"; what lapses under (K3) is the establishing, not the fact (K2). It also corrected the D3-T row. The model attack (03b) upheld every clause on the models (02 M1 (6); A6; A7: 67 of 67 candidates that fail only at the failed summer revive alike when the background premise is dropped, and no other candidate moves) and asked for one addition: a changed query, like a narrowed contract, makes a different question (A6 (4)). All four are applied.
  - One unit with W34.1 and W33.1 as edited, W59.1 and the W36.1 companion edit: its "established" is Part VI's. No outside reader has seen this text.

**CASES AT RISK, in short:**
- O1 is moved toward the fixed verdict on its first half, and its second half stays silent.
- D3-T, O27, O8, N7 (watched) and N2 hold.
- O24 and eleven other cases are untouched.

**How it came here.** Both closing lines read UPHELD, and the verdict words agree:
- (a): FAITHFUL from both;
- (b): HOLDS AS STATED from both;
- (c2): UNSETTLED BY THE TEXT from both.

The item is challenged only under the third limb of rule 3. Mimo offers exact wording twice: for the closing clause (point 2), and "the result" for "the exclusion" (point 4 (i)). The tabulation marks this as a rule-5 disagreement, since Atria upholds with no change. No point raised outside part C asserts a defect of X14 (rule 11).

## Atria's argument

Closing line: `X14: UPHELD`, followed by the reason that its three attacks (on "established", on "ceases", and on the tension with L317) fail, that the kind and declaration match, and that no verdict on the seven cases moves in either direction. OVERALL: SOUND.

**Point 1 (T1): "established" is used outside its technical sense.**
- *The attack.* A receipt is a tree over leaves that refer to events (L397). A candidate's answer at a pair is a value computed from its relations, not an event. So the exclusion of each candidate is derivable, not established.
- *Why Atria says it fails.* X14 anchors "established" on the target: the assessor "holds a usable receipt for the target's answer" (L369). The candidate side is read "from the candidate's own answer there", which is how every conjunct of (E) is read (L231, L265). What is left over, a failure that no target-side receipt reaches, is question (c2).
- *Quotation check.*
  - Not found: the heading's "established of every such candidate". L369 reads "this is established for that assessor of every such candidate alike", and the point is ruled on those words.
  - Found at L315: "is established for an assessor who holds a usable receipt for it (Part IX)".
  - Found at L397: "a derivation tree over leaves", and "an evidence leaf is a reference to an event with an interpreted claim" (capital A in the text).
  - Found at L369: "… from the candidate's own answer there", and "Here 'established' is meant as in Part VI: …" (the text has double quotes).
  - Found at L231: "a condition on supplied relations under the changes in C".
  - Found at L265: "Every conjunct is a condition … None inspects a label".
  - Found at L369: "with no record of which candidates failed before".

**Point 2 (T1): "the exclusion ceases to be established" is too strong.**
- *The attack.* If a second usable receipt also establishes the target's answer, losing one receipt does not end the exclusion.
- *Why Atria says it fails.* "The receipt" is the one that "the test that yields it" produced. Atria calls it "At most a wording imprecision, not a falsehood; no verdict turns on it", and proposes no wording.
- *Quotation check.* Both quotations are found at L369.

**Point 3 (T3): a clash with L317's "stays refuted".**
- *Atria's answer.* There is no clash. "Stays refuted" is the fact at its index. "Ceases to be established" is the assessor's warrant, which L315 already makes subject to (K3) for every result. X14 supplies the target of L317's pointer "(Part VIII)".
- *Quotation check.*
  - Found at L317: "an answer it refutes stays refuted on p (Part VIII)".
  - Not found as quoted: the longer run in the body, "an answer it refuted stays refuted". L317 reads "refutes", and the rest of that run is found at L317.
  - Found at L367: "A proposition indexed to a contract remains that proposition when a later theory changes the current contract".

**Point 4 (T2): kind and declaration.**
- *Atria's answer.* The declaration matches the wording part by part. The core exclusion was already derivable from (E) and (A). What is stated here for the first time is that the exclusion persists when a candidate is offered again or changed, and that the assessor's warrant is fragile under the receipt. So CLAIM with "clarification" is right, not ORDER.
- *Quotation check.* "keeps y there" is found at L369, and "clarification" at brief L513.

**Point 5 (T4): the seven cases.** Atria finds no move on any of them.
- *O1:* the failure on the flood question already stands by L159.
- *D3-T:* the discarded design is already excluded by (A) and Derivation 3 ("reinforced, not moved").
- *O27:* the (K3) clause restates L315.
- *O8 and N7:* no failed answer is in play.
- *N2:* the changed myth changes its answer, so X14 does not bear on it, and the verdict rests on Part VI.
- *O24:* the candidates agree on every tested pair.
- *Quotation check.* O1's verdict is given in paraphrase and is not found as quoted; brief L577 gives it in two sentences, and the paraphrase keeps their sense. "must be a member of 𝒯 … and it must survive on H" is found at L572.

**(a) FAITHFUL.**
- *Atria's reasons.* The candidate's own content carries the exclusion. The four descriptions ("the candidate that gave y there and failed, …") are one condition ("whose answer at (a,b) is y"), not a set. Nothing enumerates, grades, ranks or records, and the passage expressly declines a record.
- *Quotation check.* The L369 runs are found. "error correction is carried by the explanation itself" and "a record of rescues is redundant" are found at brief L32.

**(b) HOLDS AS STATED.**
- *Atria's reasons.*
  - On the same question the correction sticks for every wrong value, once the target's value is established.
  - A narrowed contract or a changed query makes a new question, and the failure on p stands.
  - Through (K3) and (K2) the warrant lapses, and it should: "immunity would make tests infallible".
  - At an untested neighbouring pair, a wrong candidate fails in fact, but nothing is established there.
  - A change of grain or target is a new index (L524).
  - A corrected candidate that reverts to y is excluded again, from its own answer.
- *Quotation check.* The runs cited are found at L369, L393, L315 ("at every pair of C, tested or not") and L397 ("missing evidence stays missing"). "slightly different" is Atria's own phrase, after brief L548 ("only slightly").

**(c2) UNSETTLED BY THE TEXT.** The reasons are set out under "For the owner".
- *Quotation check.* The L231, L265, L315 and L369 runs are found. "reference[s] to an event" is L397's "a reference to an event" with a bracket added.

## Mimo's argument

Closing line: `X14: UPHELD`. OVERALL: SOUND.

**Point 1 ((c2)).**
- *Mimo's argument.* Nothing says whether a leaf of a receipt may be the candidate's own content, so a failure found inside a candidate is unclassified. Mimo would settle it in favour of establishment and offers words for Part IX. Mimo adds: "X14 states nothing contrary; it stands."
- The Part IX words propose a change to another Part, not to X14's wording. They are taken up under "For the owner"; the tabulation sends the wording proposals to X09's checker.
- *Quotation check.* The L369, L315, L317 and L397 runs are found. The proposed Part IX sentence is Mimo's own.

**Point 2 (T1): the closing sentence, read generically.**
- *The attack.* Read generically, "an account on it does not answer \(p\)" is false, and Mimo gives two counterexamples:
  - Take C = {(1,b0),(a1,b0)} and C′ = {(1,b0)}. An account on C is also an account on C′.
  - Take a query Q′ that agrees with Q on C. Then an account of the new question p′ is also an account of p.
- *Why Mimo says it fails to defeat the item.* The paragraph's frame, a fixed failing answer, fixes the true reading: "the retreat is not *thereby* an answer to \(p\)". That matches L151 and the declaration. For Mimo "the hazard is a wording hazard only".
- *The optional wording.* "being an account of it is not thereby an account of \(p\)".
- *Quotation check.* Found: the L369 sentence; "Fix a question …" (L369); "an answer to one is not an answer to the other" (L151); "an account on which does not answer the original" (brief L515).

**Point 3 (T2): kind and declaration.**
- *Mimo's argument.* Every part of the declaration is true of the wording. Its general form is the closure of the per-value schema: once the target's answer is established as a value z, "Negation exchanges them" (L397) gives "not y" for every y ≠ z. CLAIM with "clarification" is right. It would be ORDER, with the places named, only if being derivable were held to be enough.
- *Quotation check.* The brief L515, L369, L397 and L317 runs are found.

**Point 4 (T3): three nits, "none fatal".**
- *(i)* "the exclusion" is a coinage the text never defines; "the result" would carry the meaning.
- *(ii)* "established … of every such candidate alike" is loose for "established of each that it is not an account".
- *(iii)* "a rival" could be misread as any rival. The governing phrase "whose answer at (a,b) is y" and the declaration's "whatever candidate it is" rule that reading out.
- *Also in the point.* The pointers resolve. The apparent clash with L317 dissolves inside Part VI, because L315 qualifies every established result.
- *Quotation check.*
  - "the exclusion" is found at L369, but once there, not "twice" as Mimo says; the second use is the declaration's (brief L515).
  - Found at L369: "this is established … of every such candidate alike", "whether it is … a rival …" and "whose answer at (a,b) is y".
  - Found at brief L515: "whatever candidate it is".
  - Found: L393's sentence, and "the background and instruments of the test that yields it" (L315).
  - Mimo's own words: "established of each that it is not an account" and "undone by no lapse of premises".

**Point 5 (T1): a slightly changed answer, and a neighbouring pair.**
- *Mimo's argument.* A changed wrong answer y′ at the pair is covered once the target's value is established. The same mistake at an untested neighbouring pair is rightly left alone, because Part VI's problems and tests are the route there.
- *Quotation check.* "Two rivals that both fit what is established … pose … a problem" is found at L317.

**Point 6 (T4): the seven cases.**
- *Mimo's argument.* No verdict moves, for reasons like Atria's. On O27, X14's clause "is the episode's own shape". On N2, X14 reaches only "a changed candidate that keeps y there".
- *Quotation check.* All found: brief L577, L159, L369, L277 and brief L619. "a population with no such survivor is the theorem's own qualification" is found at L542 (Part XV, (D)); the reply gives it as Derivation 3's.

**(a) FAITHFUL.**
- *Mimo's reasons.* The four descriptions name roles of one failing answer under a universal quantifier. There is no Pres and no grade. The record clause is the owner's own point. The receipts are for the target's answer, and L397's last sentence keeps them from becoming records of rescues.
- *Quotation check.* All found: L369; brief L515, L28 and L38; L397.

**(b) HOLDS AS STATED.**
- *Mimo's reasons.*
  - On the same question the correction sticks.
  - What can return through (K3) and (K2) is "unsettled status, never an account".
  - A narrowed contract or a changed query is a different question.
  - A changed answer at the pair is covered.
  - The untested neighbouring pair is rightly left alone.
  - A change of grain or target is a new index or a different question, since D is part of p (L137–141).
  - A recoding preserves content (Derivation 8).
- *Quotation check.* Found. "A new index is a new claim" is at L367; the reply says L368.

**(c2) UNSETTLED BY THE TEXT.** The reasons are set out under "For the owner".
- *Quotation check.* The L317 and L369 runs are found. "both fits" is Mimo's own.

## Rulings

### Ruling 1. The closing clause, and Mimo's wording for it (Mimo point 2): KEEP

The challenge is Mimo's offer of "being an account of it is not thereby an account of \(p\)" in place of "an account on it does not answer \(p\)". The clause stays as it is, because it is not false, incoherent or misleading. There are four reasons.

1. **It is true in the theory's own terms.**
   - A candidate is tied to its question: the tuple 𝓔 = (E, p, t, Γ) of L231 includes p.
   - The text already says the same thing about a change of question, in the same idiom:
     - "an answer to one is not an answer to the other" (L151);
     - a narrowed account "does not answer a broader question that failed" (L159);
     - a replacement query "does not answer the original one" (L161);
     - "an account of a different query is not an account of this one" (L253).
   - An account on a different question is a claim at another index: "A new index is a new claim" (L367). That claim does not answer p.
   - Whether the same organization and transport also make an account of p is a separate claim. Derivation 7 (L606) says outright that claims at two indices "may both be true". X14's clause asserts the first point and denies nothing of the second.
2. **The paragraph's frame rules out the false reading.**
   - The paragraph is about a candidate that keeps y at a pair of C. Its first sentence already says that no such candidate is an account of p, nor of any question with the same target and query whose contract contains the pair.
   - The closing clause ends "and the failure on \(p\) stands".
   - Read inside its paragraph, the clause cannot be taken to say that nothing that answers the narrowed question could ever answer p.
3. **The counterexample does not work as written, and even repaired it does not touch the clause.**
   - C′ = {(1,b0)} holds no change. By L257 such a contract is "not a contract on which an account can be claimed", so nothing is an account on C′.
   - A contract of three pairs repairs the example. Even then it shows only what Derivation 7 allows: one organization, assessed at two indices, meets (E) at both.
   - The changed-query version runs into L253, which X14 leaves unchanged.
   - If "does not answer" were a defect, L151, L159, L161 and L253 would share it, and they lie outside this item.
4. **The offered wording would need its own repair.**
   - "Being an account of it" has no subject.
   - The sentence says that a state ("being an account") "is not … an account of \(p\)".
   - It would set X14 apart from the idiom of the Part III lines to which its own pointer "(Part III)" sends the reader.

Rule 5: Atria (no change) and Mimo (the attack fails, and the wording is optional) agree that the clause stands. They differ only in Mimo's offer, which is not taken.

### Ruling 2. "the exclusion", and Mimo's "the result" (Mimo point 4 (i)): KEEP

- **What fixes "the exclusion".**
  - Its antecedent: sentence 3 says it is "established for that assessor of every such candidate alike" that such a candidate is not an account of p.
  - Its own clause: "for every such candidate alike".
  - The text already speaks of what (E) "excludes" (the heading at L267, "What (E) excludes, and what it does not").
- **The noun's only other use does not interfere.** That use is in Part 0 (L43), for the stated exclusion of a change from a contract. Within L369, the order of the clauses and "for every such candidate alike" rule that sense out.
- **"The result" would be worse.**
  - In Part VI a result is what a receipt establishes (L315), and the receipt here is for the target's answer.
  - So "the result ceases to be established, for every such candidate alike" would leave open whether the target-side result or the candidate-side exclusion is meant.
  - The paragraph needs the candidate-side one. The target-side one is already covered by "the receipt is not usable".

The present word is not false, incoherent or misleading.

### Ruling 3. Points that are not challenges: no change

- **Mimo point 4 (ii).** It offers no wording and is called not fatal. In "this is established for that assessor of every such candidate alike", "this" can only mean the claim that such a candidate is not an account. The target's answer is not something established "of" a candidate.
- **Mimo point 4 (iii).** It offers no wording. "A rival" stands under "a candidate for \(p\) whose answer at \((a,b)\) is \(y\)". It is one of four descriptions of a candidate that meets that condition.
- **Atria point 2.** Atria calls it not a falsehood and offers no wording. I agree, for two reasons.
  - The clause concerns "the receipt" that "the test that yields it" produced. By L315 a result is established for an assessor who holds *a* usable receipt, and L397 speaks of "the usable receipts" for a claim, in the plural. So a reader who applies Part VI to an assessor holding a second receipt finds the exclusion still established, on that second receipt.
  - The singular, one-test idiom is also L315's own ("the test that yields it").

  The consequence is recorded under "Does the result hold" as a condition. It needs no new words.

### Ruling 4. The attacks both readers made and reported as failing: agreed

- **Atria point 1.** "Established" is anchored on the receipt for the target's answer (L369). What is left over is question (c2).
- **Atria point 3, and Mimo point 4 on L317.**
  - L315 attaches (K3) to every result that tells against a candidate. "Stays refuted on \(p\)" (L317) is therefore read under it, and X14 spells that reading out. No sentence contradicts another.
  - L317 belongs to X10's item, and nothing here bears on that item.
- **Mimo point 5.** Taken up under "Does the result hold", conditions 3 and 4.
- **Kind and declaration.** I agree with both readers that CLAIM with "clarification" is right.
  - The declaration is the universal closure of the per-value schema.
  - The NEW text's gloss, "a usable receipt for the target's answer at \((a,b)\)", is the declaration's "Once the target's answer there is established for an assessor, by a usable receipt".

### Ruling 5. Cases and fixed verdicts

Both rulings are KEEP, so no wording changes and no verdict can move. Neither reply disputes a fixed verdict (rule 10).

One difference from the entry is recorded. CASES AT RISK reads O1 as moved "toward" on its first half, while both readers find no move, because L159 already gives that half. Either way there is no undeclared change of claim: the declaration's last sentence covers the narrowing.

## Does the result hold

**Yes. "A failed answer stays failed" holds as stated.**

- **The fact** (the first two sentences) follows from (A) and (Q) alone.
  - On a fixed question p, a candidate whose answer at a pair of C differs from the target's answer there is not an account of p.
  - The same holds on every question with the same target and query whose contract contains the pair.
  - It holds whoever the candidate is and however it came about, whether or not anyone has tested it, and with no record. It rests on the world's answer, not on the observation.
- **Being established for an assessor** (the next three sentences) follows from Part VI's "established", Part IX's receipts, and (K2) and (K3). Each sentence states its own condition.

So the owner's point that "the mistake shouldn't be able to creep back in" holds exactly. It holds on the failed question, at the failed pair, for every candidate, and nothing in it lists, counts, grades or records.

**How a corrected mistake could come back.** There are seven ways. The paragraph states each one, or leaves it outside what it claims.

1. **On the same question, at the failed pair.** It never comes back as an account.
   - For one assessor it can return only to "not shown to fail", when a premise about the test's background or instruments ceases to be live (K2, K3).
   - It then returns for every such candidate alike, exempting none, and "no candidate is thereby shown to be an account".
   - That is as it should be; otherwise a test could never be wrong.
   - If the assessor holds another usable receipt for the target's answer there, whose premises stay live, the exclusion stays established on that receipt.
   - For an assessor who holds no such receipt, nothing is established at that pair, although the fact is the same for everyone.
2. **If the test itself was wrong,** and the target's answer at the pair is y after all.
   - Then the candidate never failed in fact: the paragraph's hypothesis, y ≠ Ans_p(a,b), is not met.
   - Only the establishing lapses. That is the right outcome.
3. **A slightly changed wrong answer y′ at the same pair.**
   - It is excluded in fact: the paragraph applies again with y′ in place of y.
   - It is established as excluded when what is established rules out y′ too, as it does when the receipt establishes the target's value there.
   - A test that rules out only y leaves y′ open for that assessor until another test. The text claims no more than this, since it is stated one value at a time.
4. **The same mistake at another pair of C that has not been tested.**
   - It is excluded in fact if it is wrong there, but it is established for no one until the target's answer there is established.
   - This is the one place where a corrected mistake can creep back unnoticed. The background analysis's models show corrected versions that fit the failed pair and repeat the old error at an untested one.
   - X14 claims nothing at such a pair. The route is Part VI's rivals, problems and tests; a record of rescues would not detect it either.
5. **A narrowed contract that omits the pair, or a changed query.**
   - The candidate may be an account of the new question. That is a new claim at a new index: it does not answer p, and "the failure on \(p\) stands" (L151, L159, L161, L367; Derivation 7).
   - The narrowing is not forbidden, and the semantics does not certify it as appropriate (L159).
6. **A changed transport that reads the pair differently.**
   - The candidate's answer there is then a new value. If it is y, the candidate is excluded.
   - If it is not y, this is a different candidate, judged by (E) at every pair of C. If it meets (E) it is a correction, not the mistake coming back.
   - A recoding changes no answer (L365; Derivation 8), so a recoded candidate that keeps y stays excluded.
7. **A change of grain or of target.**
   - A change of grain is a new index (L524). A change of target is a different question, because D is part of p (L137–141).
   - On another target the failed answer may be right, as the entry's LOSS says.
   - The failure on p stands.

## For the owner

### (c2): whether a failure found by examining a candidate counts as established

Both readers answer UNSETTLED BY THE TEXT for X14 (tabulation §6.2). It is the owner's choice, and it is not settled here.

**Does the present wording state the matter truly? Yes.**
- X14 claims establishment only for a failure at a pair, against a target answer that a receipt has established. For that it needs only one thing: that the assessor can read the candidate's own answer at the pair.
- Both readers' settlements grant that. Atria would have it read by inspection, with no receipt. Mimo would have it read through a receipt whose leaf is the candidate's own content.
- The drafters' REASON reads it the same way: "derived from its organization, over the same leaf".
- X14 says nothing about failures that no target-side receipt reaches: a failure of non-circular dependence, a component anchored to nothing, a contradiction inside the candidate. It neither asserts nor denies that such failures are established.

**One caution.** Atria holds that X14's "no record" clause relies on the candidate's own answer being available to an assessor. Suppose (c2) were settled in a way neither reply proposes: a candidate's content could enter no receipt and could not be read without one. Then X14's third sentence would lose its support. Either settlement that the replies do propose leaves it standing.

**Atria's reasons.**
- The text pulls both ways. Part V's conditions are conditions "on supplied relations", checked by inspecting the candidate (L231, L265). But "established" runs through receipts over leaves that refer to events (L315, L397), and a structural failure is not an event.
- Atria would settle it in favour of inspection for facts about a candidate, and keep receipts for claims about the target and the world.
- *What turns on it.* Otherwise a circular or self-contradictory rival would still fit, for an assessor who has not tested it. With a sound account it would pose a problem, and the assessor would be sent to test the world when the rival's own content already shows it is no account.
- Settling it this way also backs X14's "no record" clause.

**Mimo's reasons** (the (c2) paragraph and point 1).
- The text neither states nor excludes it.
- Mimo would settle it in favour of establishment, by a receipt whose leaf is the candidate's own content. (K3) would then take the definitions, the declared indices and the reading convention as the background and instruments. Mimo offers words for Part IX.
- *What turns on it.* If internal failures are never results, a candidate that fails (E) still fits. Together with a sound twin it can then pose a problem of the second kind and brand the sound account "easy to vary" (L317). Mimo calls that "a verdict the theory should never reach".

**Where the two differ.**
- Whether an examination is itself a receipt (Mimo), or facts about a candidate need none (Atria).
- Whether (K3) qualifies such a result. Mimo says yes, with the definitions, declared indices and reading convention as the background; Atria's part-C paragraph does not say.
- Where any words would go: Mimo says Part IX.

The tabulation sends the wording proposals to X09's checker.

### Faithfulness to S20 and S26

Both readers say FAITHFUL, and I agree.
- The four descriptions are one universal condition, "whose answer at \((a,b)\) is \(y\)". They are not a set of versions or rivals to be listed.
- No count, grade or rank appears.
- The paragraph expressly declines a record of which candidates failed or of how any was changed.
- The only receipt in it is for the target's answer. That is a record of the world, not of candidates, and L397 keeps a reconstructed record from counting as a receipt.
- The limit in condition 4 above is not one that a record would close.

### A line for the CHECK field (rule 12), if wanted

"S93 cross-examination: upheld by both readers (part C); (a) FAITHFUL, (b) HOLDS AS STATED and (c2) UNSETTLED BY THE TEXT from both. Mimo's optional wordings, for the closing clause (point 2) and "the result" for "the exclusion" (point 4), ruled KEEP by the checker: the clause is in the idiom of L151, L159, L161 and L253 and is true under it, and "the exclusion" is fixed by its antecedent. No change."

X14: KEEP
