# Ruling: s90_xexam_mimo_C, item 4, R13 (W35.2)

*A fresh Claude checker, 24 September 2026. It works under the S90 rule as extended by "S90 Parts - how they will be read, written before sending.md" (rules 2 and 3), and under the rerun note "S90 and S87 - seven calls rerun after the container restart - written before sending.md" (ruling 4: the pass-2 reply stands where the pass-1 reply would have stood). This checker did not draft, assemble or check the change list and did not write the part briefs.*

*The call counts. Pass 2, attempt 1 of 1: status 200, finish "stop", 0 bad chunks, accepted. END OF REPORT is on the last line. The reply's sha256 is 9ea0342fa8d813c269086400a6be74deaa4cecfdc372c9857faaabe1c954eb90, which matches the receipt. It is 1,321 words by `wc -w`. The other reply to part C, Atria C (pass 2, sha256 bd51b78593b3ac9e7d194d7f0b62e43e223f8c487d6e611a6118999d50d7a72f, which matches its receipt), also contests R13 and is stated in section 2.*

*Sources:*
- *change list md5 a5c92adc9f1e3806c0f9c6394cffde1e (as at 587eebf; no later commit touches it);*
- *revised text `tests/Revision 2 - file 13 draft 2, theory text, as sent for cross-examination.md`, md5 9aecf2f30ce0b4523606b2b8409fdf37;*
- *file 11 md5 5e494c1095d920d128b9a79de378f923, read only;*
- *part C brief md5 2183faa5005b112347f484b6c8ace196 (its R13 block and tasks (a)–(d));*
- *S81 book md5 4f488d149e44669240d5db546c8e946a; S89 book md5 b2e535777976a511935430bd089ba500; D3-T `final.md`.*

*Map (part-rule table): "R13 | W35.2 | C12 | C | 225 | 223 | CLAIM | O23, N18".*

*Earlier rulings.* Neither batch 1 (Mimo A1, Mimo A2, Atria B1) nor batch 2 (Atria A2, Mimo B1) rules R13, W35.2 or C12, so there is no batch ruling to reconcile. The ruling on this reply's item 1 (R12, W35.1, FIX) passes R13's L223 clause to this checker: "'Expectation and violation are defined for every transport, surprise only for a selected one' has to follow this fix, as '… for every transport to the simulation layer, surprise only for a selected one'". This ruling is reconciled with that one (section 4).

## 1. The entry and its checkers' verdict

W35.2, "Part IV: a constructed transport is violated, not surprised".
- Group C, item W35 (b′).
- Part IV, "Expectation, surprise, violation". File-11 L225, revised L223. One sentence is added after s4; s1–s4 are unchanged.
- REASON WORD: clarification. KIND: CLAIM.

**OLD:**
````text
Whether the correspondence could have been otherwise at such a change is a fact about its population (Derivation 3).
````

**NEW:**
````text
Whether the correspondence could have been otherwise at such a change is a fact about its population (Derivation 3). Expectation and violation are defined for every transport, surprise only for a selected one: a constructed transport that fails at a pair of its contract is violated, and the failure is not surprise; a violation the system represents can be a recognized difficulty (Part X).
````

**DECLARATION:** "Part IV now says that a constructed transport that fails at a pair of its contract is violated, that the failure is not surprise, and that a violation the system represents can be a recognized difficulty."

**Checkers' verdict (CHECK):** "check 2, FIX. File 11 says a system is surprised and a transport is violated, never surprised; NEW reads "is violated, and the failure is not surprise". N18 Q3's Dov half stays watched (his transport need not be read as selected). Companion entry W35.4 added."

**The drafter's REASON on this point:** "Plan 1.2 asks for surprise to be kept for selected transports "and said so". This sentence says it." So by the REASON, the opening clause, "surprise only for a selected one", is what the sentence is for.

**CASES AT RISK:**
- N18: toward on Q3. Rhea's constructed transport is violated; Dov's copy, read as selected, meets a change outside its record, which is surprise. The Dov half is watched.
- O3 holds. O13 and O23 were checked; no other O-case turns on a constructed transport's failure.

**Companion entries:** W35.1 (R12) rewrites the preamble and third bullet at L217–221; W35.3 (R34) defines the recognized difficulty at L423; W35.4 (R14) types L225's selection response to a selected transport.

## 2. The replies' arguments

**Mimo C, point 4** (closing line: "R13: STANDS"). Under S90 Parts rule 2 the change is contested all the same, because the point names a part of a CLAIM change that its declaration does not mention (task (b)'s last sentence):

> R13's new wording (line 223) begins: "**Expectation and violation are defined for every transport, surprise only for a selected one**: a constructed transport that fails at a pair of its contract is violated …". The declaration lists only the three claims after the colon. The opening clause is not mentioned. It largely restates R12's preamble change, so it is not an independent new claim; but it is a claim the new wording makes, the declaration is silent about it, and — because it inherits R12's defect (point 1) — it is also false as written ("expectation … for every transport"). […]
>
> **Repair.** Add to the declaration: "and restates that expectation and violation hold for every transport (to the simulation layer) and surprise only for a selected one." If R12 is repaired as suggested in point 1, the restatement should track the repair.

R12's defect, from point 1: "Unless \(E = S\), \(\operatorname{Ans}_S(\tau(a),\sigma(b))\) does not type-check. […] So the expectation is well-defined only for transports whose target is \(S\)".

**Atria C, point 1** (closing line: "R13: FALLS — "defined for every transport" contradicts the section's \(\operatorname{Ans}_S\) formula and Part IV's primitive-layer transports."). It makes the same typing point and puts the fall on R13's sentence:

> For a transport whose target is not \(S\), \(\operatorname{Ans}_S(\tau(a),\sigma(b))\) is undefined, so "defined for every transport" is false as written. The current text did not assert this […]. R12's setup line […] generalizes the section; R13's sentence then turns a latent looseness into an explicit contradiction with unchanged text. *(d) check:* no verdict moves — in N18 both designers' transports are simulation-layer […]. *Repair:* "Expectation and violation are defined for every transport into the simulation layer, surprise only for a selected one," or replace \(\operatorname{Ans}_S\) with \(\operatorname{Ans}_E\) […]. I hold R13 to fall: its sentence is the false statement.

Its point 2 works N18 on R12–R14 and finds "the declared distinction is exactly the fixed verdict".

**Quotations checked (rule 8).**
- Both replies quote the L223 sentence as it stands in the revised text. Mimo is right that the declaration names only the three claims after the colon.
- Mimo says the new wording "begins" with the opening clause. Strictly, NEW begins with the unchanged s4 ("Whether the correspondence …"), carried inside the block; the added sentence begins with the clause. Nothing turns on this.
- The expectation \(\operatorname{Ans}_S(\tau(a),\sigma(b))\) is at revised L219; R12's setup line, quoted by Atria, is at L217; file 11's "Let \(t\) be selected on history \(H\) with contract \(C\)" is at file-11 L219. All found as quoted.
- Atria's "A physical system may hold selected transports at the primitive layer and constructed transports at the simulation layer" is at revised **L201**, not "line ~203". Its "\(S\) is where expectation lives" is at revised **L177** ("line ~179" is the file-11 line). Both are found word for word.
- Atria's "(R)'s transports run from a carrier to a content" is a paraphrase of (R) at L208, \(t:\operatorname{Org}_\ell(o)\to c\). It is accurate.

## 3. The texts, and the cases

**The opening clause is a claim the declaration leaves out.**
- Against file 11 it is new. File 11's section opens "Let \(t\) be selected on history \(H\) with contract \(C\)" (file-11 L219), so there expectation and violation exist only for selected transports. "Expectation and violation are defined for every transport" lets a reader conclude what file 11 did not allow: that a constructed transport has an expectation and can be violated.
- It is the same claim W35.1 declares ("Part IV now defines expectation and violation for every transport, and keeps surprise for …"). Mimo is right that it is not independent. But each entry carries its own declaration into the record, and the brief's task (a) asks whether "the new wording claim[s] more than the declaration says". It does.
- The drafter's own REASON makes the gap plain: plan 1.2's "and said so" is met by this sentence ("This sentence says it"). The declaration leaves out the one part of the sentence the REASON says it exists for.

**The clause is false as written, whatever happens to R12.**
- As the item-1 ruling found, \(\operatorname{Ans}_X\) is a query evaluated on \(X\) at \(X\)'s own edits and boundaries ((Q) at L144; (A) at L250). For a transport \(D\to E\), \(\tau(a)\) is an edit of \(E\) and \(\sigma(b)\) a boundary of \(E\) (L183–189). So the expectation \(\operatorname{Ans}_S(\tau(a),\sigma(b))\) has a value only when \(t\)'s target is \(S\).
- Transports whose target is not \(S\) are in the text: (R)'s carrier-to-content transports (L208), a Part V candidate's transport from \(D\) to \(E\) (L231), and, on Atria's reading of L201, selected transports "at the primitive layer". For them the sentence's "expectation … defined for every transport" is false. Its violation half is true, since fidelity is stated for any transport.
- Atria's distinction between R12 and R13 is sound as far as it goes. R12's preamble can be read in the context of L177 ("\(S\) is where expectation lives"). R13's sentence cannot: it states the universal in prose, in words a reader takes at face value. So R13 needs the scope even if R12 were kept as drafted. The item-1 ruling fixes R12 as well, and the two fixes use the same words.

**The colon's second half.** After the colon, "a constructed transport that fails at a pair of its contract is violated" is meant as an instance of the clause before it. Once the clause names the target, "a constructed transport" should too, or a strict reader takes it to stretch "violated" to constructed transports with any target (a Part V candidate's, a carrier-to-content transport), which the section no longer defines. Writing "a constructed one", parallel to "a selected one", keeps it inside the scope just named, with no new term.

**Repairs weighed.**
- **Adding the clause to the declaration alone (Mimo's repair, without the scope)** is not enough: the declaration would then declare a false claim.
- **Scoping the clause (Atria's first repair; Mimo's parenthesis)** is adopted, in the words of the item-1 ruling: "to the simulation layer". Atria's "into" says the same; "to" is kept for one wording across R12 and R13.
- **\(\operatorname{Ans}_E\) (Atria's second repair)** is not adopted, for the item-1 ruling's reasons: a general \(E\) supplies no query in this section, and unchanged L177 keeps expectation at \(S\).
- **Cutting the opening clause** would remove both the undeclared claim and the false universal, and leave the declaration complete. It is not adopted: it would take out what the REASON says the sentence is for (surprise kept for selected transports "and said so"), and both replies would keep it once scoped.
- **Dropping the entry** is not warranted. Its three declared claims are true once scoped: surprise is "a violation of a selected transport" (L221), a transport has exactly one provenance (L193), so a constructed transport's failure is not surprise; and a recognized difficulty is a failure of a claimed obligation "when the system represents it" (L423, in Part X, L395–426), so "can be" is right and the pointer holds.

**Cases, worked on the fixed wording.**
- **N18 (S89): holds, as drafted.**
  - Q2 (against what each expected): Rhea's worked-out theory is a constructed transport to her simulation layer; her expectation is \(\operatorname{Ans}_S\) at the translated crowd edit (steady). Dov's copy, read as selected on the village bridge's record, also goes to his simulation layer; he expects trouble-free. Both expectations fail. Agrees.
  - Q3 (contradicted what either had reason to expect): the crowd on Rhea's bridge is "no larger than the crowds she had calculated for", so the failing pair lies in her contract. By the fixed sentence "a constructed one that fails at a pair of its contract is violated, and the failure is not surprise": her grounds are contradicted. Dov's large crowd is \((a,b)\notin H\) for a selected transport: surprise, and by Derivation 3 his record left that value open. Agrees with "nothing Dov had reason to expect". The Dov half stays watched on reading his transport as selected; the scope does not touch that.
  - The scope costs N18 nothing, since both designers' transports go to their simulation layers (as Atria says).
- **O23 (S81): not reached.** The case turns on a variable becoming a dimension of her account (measured, not mentioned in passing). No expectation, violation or surprise is at issue, before or after the change.
- **O3 (S81): holds.** Nadia's next-card prediction is a selected transport to her simulation layer; "often surprised" stays surprise. The verdict turns on construction.
- **D3-T (O76): not reached.** The discarded design fails at a tested setting, which is a failure of the survival condition on \(H\) (Derivation 3; "survives on \(H\)", L195). Whether that failure is also a Part IV violation does not bear on the question, which asks whether passing leaves the untried setting open; and the case gives the controller no simulation layer.
- No other case in the S81 or S89 books turns on expectation, violation or surprise. The words occur in the revised text only at L177, L201, L215–225, L570–578 and L618.

## 4. Ruling: FIX

**The arguments succeed.**
- Mimo is right that the declaration leaves out the opening clause, and right that the clause carries R12's typing defect.
- Atria is right that the clause, as prose, states a false universal.
- Neither reply overstates the point on R13. Mimo's "not an independent new claim" is true, and it does not excuse the omission.

**The fix** scopes the clause and its instance to transports to the simulation layer, and completes the declaration. It keeps the sentence's aim and its three declared claims.

- **OLD:** unchanged, file-11 L225 as above.
- **NEW:**
````text
Whether the correspondence could have been otherwise at such a change is a fact about its population (Derivation 3). Expectation and violation are defined for every transport to the simulation layer, surprise only for a selected one: a constructed one that fails at a pair of its contract is violated, and the failure is not surprise; a violation the system represents can be a recognized difficulty (Part X).
````
- **KIND:** CLAIM (unchanged). **REASON WORD:** clarification (unchanged).
- **DECLARATION:**
````text
Part IV now says, restating its definitions, that expectation and violation are defined for every transport to the simulation layer and surprise only for a selected one; that a constructed transport to the simulation layer that fails at a pair of its contract is violated, and the failure is not surprise; and that a violation the system represents can be a recognized difficulty.
````
- **For the CHECK field and the list of what the checks changed (after the cross-examination):** "S90, Mimo part C point 4 (closing line R13 STANDS, but it names an undeclared clause) and Atria part C point 1 (R13 FALLS); fresh checker FIX after the cross-examination. The opening clause reads 'for every transport to the simulation layer', since \(\operatorname{Ans}_S(\tau(a),\sigma(b))\) is typed only when \(t\)'s target is \(S\); its instance reads 'a constructed one', parallel to 'a selected one', so that 'violated' stays inside that scope. The declaration now includes the restated clause, which the REASON names as the sentence's purpose. Follows the R12 (W35.1) fix."
- **What is lost:** the unscoped "for every transport", which was false for expectation. A constructed transport with another target (a Part V candidate's, or (R)'s carrier-to-content transport) is not called violated by this section. It was not in file 11 either, where the section covered only selected transports.
- **What is gained:**
  - The prose restatement matches the definitions it restates, once R12 is fixed.
  - The declaration says everything the sentence claims.

**Conflicts with other entries.**
- **W35.1 (R12):** this fix follows the item-1 ruling's FIX ("Let \(t\) be a transport to the simulation layer \(S\), with contract \(C\) …"; declaration "for every transport to the simulation layer, whatever its provenance"). The two should be applied together. If R12's fix were not adopted, this sentence would still need its scope, since it is false as prose on its own; but it would then be narrower than an unscoped preamble, and R12's typing defect would remain.
- **W35.4 (R14):** unaffected. "The history \(H\) of a selected transport" still has a referent.
- **W35.3 (R34):** unaffected. The recognized difficulty at L423 is unchanged, and "(Part X)" still points to it.
- No other entry has an OLD at file-11 L225.
