# S103 Round 1 — critical review of the rulings

*Written by Fable 5.1 on 27 September 2026, the critical reviewer of decision S35 ("use Fable 5.1 sparingly for critical reviews"), under rule 12 of `results/S103 Round 1 - how the replies will be read, written before sending.md`. Created at once and filled as it went. This file obeys decision S23 except where it quotes the text, a ruling, a reply or the owner. Nothing here is settled (S28): where this review finds nothing to object to, that is a finding on the arguments in the rulings, open to any later argument. No theory text was edited; nothing was committed by this file's author.*

**Where this file stands.** Rule 12 of the reading rule names `results/S103 Round 1 - critical review of the rulings.md`. The task named `results/S103 Round 1 - reading/critical review.md`, beside the rulings, and that path was used; no second copy was written. The difference is the orchestrator's to settle, as every checker noted of rule 11.

## The finding, in one line

**No objection to any of the 29 rulings.** The four FIXes (C07, C27, C28, C29) each say what the challenge calls for and no more, bring back no word or idea S23 forbids, add no list, count, grade or record (S20), state nothing about what must happen (S21), bring physical possibility nowhere it does not already stand (S25–S27), settle nothing (S28), and say nothing about what hard to vary covers or where values are placed (S33–S34). Every KEEP answers, with a reason from the text, each point a reader offered as a defect. There is no DROP, so no dependents are left unhandled. No two rulings conflict; two places where rulings touch the same matter are recorded below and are consistent. A handful of small points in the rulings' own prose and citations are recorded at the end; none bears on an outcome.

## What was read

- The text under review, `tests/99 The semantics, standing alone.md`, md5 74f4a4c7619345747f4fa976ddac9548 (checked before reading), whole; and, for each FIX, the line changed and the lines the ruling ties to it, compared again by program (the old wordings at L123, L443, L471 and L520 stand in file 99 byte for byte as the rulings quote them; "post-fixed" stands at L471 only, "deployable" at L403, L443 and L628 only, "deliberative" at L385 only, "four conditions" at L61, L231 and L536, "Question fidelity" at L247).
- The owner's decisions S20–S35 in `records/Semantics - Decisions.md`.
- The reading rule, whole.
- All 29 rulings in `results/S103 Round 1 - reading/rulings/`, whole.
- The tabulation's closing sections (`results/S103 Round 1 - reading/tabulation.md`, lines 3013–3060: passages naming a candidate outside its own section; points that allege a defect whatever the closing line; notes).
- The replies, at the lines the FIX rulings take their new wordings from: `s103_vary_glm_1.response.txt` line 154 and `s103_vary_mimo_1.response.txt` line 172 (C07); `s103_vary_mimo_3.response.txt` lines 200 (C27), 228 (C28) and 279 (C29). Each new wording was compared with the reply line and found there as the ruling says (C07's from GLM line 154 without the comma Mimo's line 172 keeps; C28's in the LaTeX of Mimo's fenced rival, not the Unicode of its closing line). No reasoning file was opened.
- The three part briefs were not re-read whole; the rulings quote the sections they use, and the tabulation records every reader's quotation as found (with one wrong line number, GLM's L267 for L269, which the C21 and C24 rulings both caught).

## The rulings, as they stand

| candidate | line | ruling | new wording (FIX only) |
|---|---|---|---|
| C01 | 27 | KEEP | |
| C02 | 41 | KEEP | |
| C03 | 47 | KEEP | |
| C04 | 113 | KEEP | |
| C05 | 113 | KEEP | |
| C06 | 115–117 | KEEP | |
| C07 | 123 | FIX | `- a **causal assignment** has a signature that changes under intervention on its output port and is invariant under observation edits;` |
| C08 | 124 | KEEP | |
| C09 | 125 | KEEP | |
| C10 | 127 | KEEP | |
| C11 | 127 | KEEP | |
| C12 | 127 | KEEP | |
| C13 | 161 | KEEP | |
| C14 | 161 | KEEP | |
| C15 | 161 | KEEP | |
| C16 | 217 | KEEP | |
| C17 | 219 | KEEP | |
| C18 | 220 | KEEP | |
| C19 | 225 | KEEP | |
| C20 | 225 | KEEP | |
| C21 | 273 | KEEP | |
| C22 | 311 | KEEP | |
| C23 | 375 | KEEP | |
| C24 | 383 | KEEP | |
| C25 | 385 | KEEP | |
| C26 | 393 | KEEP | |
| C27 | 443 | FIX | `An explanatory aim requires a deployable account, or the correction of a use through one.` |
| C28 | 471 | FIX | `\(F\) is monotone; \(C\subseteq F(C)\) is the invariant form; the greatest fixed point is the union of the sets \(D\) with \(D\subseteq F(D)\). (CT2)` |
| C29 | 520 | FIX | `Account, from fidelity under change, non-circular dependence and non-vacuity (E).` |

This table records what each ruling is; it grades, counts and ranks nothing (S20).

## The four FIXes, each read against the text and the owner's words

### C07 (L123): the replacement clause deleted

**What the ruling does.** It removes "and under replacement of the component" (and the comma after it) on the ground Mimo named and did not press ("Inertness, not contradiction", Mimo reply line 174) and GLM contested: that the clause does no work.

**Does the FIX say more or less than the challenge calls for?** No. The challenge is that the clause is inert; the FIX removes it and nothing else. The new wording is GLM's own variation at reply line 154, byte for byte.

**Is the fault shown?** Yes, on the text's own definitions, and this review went through it again because it is a change to Part II's families and one other checker (C08, line 165) remarked the other way. By L103, "An edit that sets a port replaces the component assigning that port"; by L109 a component's output port is the port its relation determines; so the intervention clause 1 names is itself a replacement of the component, and the contract that meets clause 1 already holds a replacement of it. By (K) at L116 and L119 ("A signature is built from a component's relation under each \((a,b)\in C\)"), a replacement changes any component's signature. So on the plain reading clause 2 is entailed by clause 1 and (K) and marks no family off from another. On the one reading where it is not idle (a replacement of the component other than the intervention, such as a change of mechanism), it would ask of a contract what the text's own production case at L325 (interventions on \(H\), \(\theta\) and \(L\), no change of mechanism) and the case book's O9 (the bent needle and the wire) do not supply, and so would put the pole's forward component and the float outside the causal family on the very contracts the text and the cases use to show production. The ruling's point 3 is also right and matters most: with clause 2 gone, a measurement is still kept out of the causal family, because an intervention on the reading is, by L109, an observation edit for the measured port, and the measurement's own signature changes under it, so it fails clause 3. The distinction L127 relies on ("Which of the two an account offers as producing an outcome is fixed by that signature") is carried by clauses 1 and 3 alone.

**The owner's words.** The FIX removes words and adds none (S23). It lists, counts and grades nothing (S20); says nothing about what must happen (S21); touches no physical possibility (S25–S27); settles nothing (S28); says nothing about what hard to vary covers, and moves no value (S33–S34).

**Dependents.** The ruling names L37, L57, L109, L121, L124–L125, L127, L151, L245, L269, L325, L347, L520 and Argument 1, and shows each reads as before; this review checked L57 and L127 in particular and agrees. No fixed case verdict moves (O4, O6, O7, O9 read as before).

**Finding: nothing to object to.**

### C27 (L443): "to be deployable" moved onto the account

**What the ruling does.** Both readers closed FAILS on the same fault: the trailing infinitive governs the whole disjunction, so a *correction of a use* is asked to be deployable, while Deploy is a relation on contents (L403: "\(s\) at \(\xi\) holds a representation of \(c\)"; L425: a content is "an organization, a transport, or a contract") and a correction is a repair, "a subhistory together with the changes of content it makes" (L435). The ruling takes Mimo's line 200 wording.

**Does the FIX say more or less than the challenge calls for?** No. It moves one adjective onto the noun Deploy applies to and changes the article; "the correction of a use through one" stays word for word, and "one" takes up "a deployable account", so deployability still covers both kinds of aim, as (EX) at L449 asks (\(\operatorname{Deploy}_{\beta,\ell}(s,c,\xi';U_c)\) for every \(o\in O_{\mathrm{ex}}\)). The ruling's reasons for this wording over Mimo's closing line (which loses deployability on the second kind) and GLM's (which makes an aim an account, against L441's "a stated condition over stated occasions" and L628's "possess a deployable account") are reasons from the text and stand.

**The owner's words.** "Deployable", "account", "correction" and "use" are the text's terms; nothing S23 forbids enters, and the words S95 took out of this sentence stay out. "Requires" is the text's own word in the same definitional role: it says which aims are explanatory, not what must happen to any candidate (S21). Nothing about physical possibility (S25–S27); nothing settled (S28); nothing about what hard to vary covers (S34).

**Dependents.** L443.s3 and (EX), L526 and L528 unchanged; the worked case at L628 reads as before (its aim is stated in the new first disjunct's own words). No fixed verdict moves (N10 stays where S96 left it; O13 reads as before).

**Finding: nothing to object to.**

### C28 (L471): "post-fixed sets" spelled out

**What the ruling does.** Mimo closed VARIES with a wording that names the class of sets in the notation the sentence has just used; the ruling finds it a rewording that changes nothing the theory needs and, under rule 5, takes it because it is clearer.

**Is "clearer" a reason from the text?** Yes, here. "Post-fixed" occurs once in file 99 (L471) and is defined nowhere in it; the clause is one L546 exposes to counterexample ("A counterexample to the finite monotone claim, (I2), (O1), (T2), (CT2), or Arguments 1–3"); and, as the ruling shows, whether the clause holds or has a counterexample turns on which of two usages of the undefined word a reader brings (under the other usage the set of all states is one of the sets, and its union is a fixed point only when every state's executions complete and return). A wording that removes that dependence is clearer in the sense rule 5 asks. This review went through the ruling's own working of the clause (monotonicity of \(F\); \(U\subseteq F(U)\) and \(F(U)\subseteq U\) for the union \(U\) of the sets \(D\) with \(D\subseteq F(D)\)); it goes through.

**Does the FIX say more or less?** No. The three clauses, the semicolons and the label (CT2) stay; the third clause states the same identity with the class written out. The letter \(D\) is bound locally, and the ruling gives the text's own habit of local letters (Part XII already reuses \(C\); L287 binds \(W\)); no reason was found for another letter.

**The owner's words.** No forbidden word or idea (S23); "greatest" and "union" order sets of states by inclusion, not explanations or thinkers (S20, L522). Nothing about what must happen (S21); the sentence stands in Part XII, where the owner places physical possibility (S25–S27), and reaches no further; nothing settled (S28); nothing about what hard to vary covers (S34).

**Dependents.** L546 names (CT2) and reads as before; (CT1) and its users (L475, L495, L526) unchanged. No case turns on (CT2).

**A note, not an objection.** The ruling read one outside web page for the usage of "post-fixed". That is not a book, and no book is quoted; the rules given to this round are met.

**Finding: nothing to object to.**

### C29 (L520): the Account gloss names all of (E)

**What the ruling does.** Mimo closed FAILS: the gloss "Account, from fidelity under change (E)" names the fidelity conjuncts of (E) and leaves out non-circular dependence and non-vacuity (L262, L255, L257). GLM closed HOLDS: the gloss names the source by sense, as L265 characterizes every conjunct. The ruling finds the failure shown and takes Mimo's repair.

**Is the failure shown?** This review weighed GLM's side again, since the list's other items are not exhaustive either ("Roles, from admitted edits (Part II)" leaves out the relation \(L_j\) that L109 uses for an output; "Kinds, from signatures (K)" leaves out the footprint bijection). What decides it for the FIX is that "fidelity" is a defined term of the text (L189; L245, "Together they are fidelity at every level the contract reaches"; L247, "Question fidelity") that never covers the two conditions left out, and that those two are the conditions Part V uses to keep an account apart from a faithful restatement: L269, "it is an account when it meets the other conjuncts of (E)"; L273, ""\(p\) because \(p\)" fails non-circular dependence". Read on the list's own pattern, the gloss lets a faithful table be an account, which L269 denies. The text itself counts "the four conditions of Account" (L61, L231, L536), not fidelity. So the ruling's reason is from the text and stands; GLM's point about L265 is answered where the ruling says (L265 says every conjunct is a condition "under the changes in \(C\)", not that every conjunct is fidelity).

**Does the FIX say more or less?** No. It keeps every word of the gloss, adds the two conditions by the headings the text gives them (L255, L257; the words at L43, L273, L536), and joins them as the item for (R) joins its two ("from fidelity and provenance"). The ruling's reasons against the other placements of "under change" and against the bare tag are reasons from the text.

**Cross-check with C18.** The C18 ruling records that "fidelity" has two extents across the text (L189 and L245 against L247 and L520, with L630 on the narrow side). The C29 FIX is consistent with C18 on either extent: the two conditions it adds fall outside "fidelity" on both, and for an account the text's own heading at L247 counts (A) as "Question fidelity", so "fidelity under change" reaches it. No conflict; recorded in the cross-ruling section below.

**The owner's words.** The added words are the text's own names for two of its conditions (S23). Naming the conditions of one definition is the explanation's own content, not a list, count or record of rivals (S20). Nothing about what must happen (S21); no physical possibility (S25–S27); nothing settled (S28); nothing about what hard to vary covers, and GLM's mention of S34 concerns a word ("variation") the FIX does not use (S34).

**Dependents.** No sentence quotes or relies on the gloss's wording; L526 and Argument 6 rest on the dependence order, which is unchanged. No case verdict moves.

**Finding: nothing to object to.**

## The KEEPs where a reader offered a point as a defect

The tabulation (lines 3022–3042) lists every point either reader offered as a defect, whatever the closing line. Each was read against its ruling and the text.

- **C01** (Mimo: the sentence's work is a role, not new content). The ruling answers it from the line itself: "the classes defined" in L27's first sentence has no agent, and C01 supplies it, which L520 and L528 state more exactly (L35). Answered.
- **C02** (Mimo: "it" could be read as fidelity; the clause alone invites an unindexed reading). The ruling answers it from L31 (every claim relative to the declared indices) and L43 ("Within any contract, whether a transport is faithful at a pair turns on the transport and the target"). Answered.
- **C03** (Mimo: "Construction is a separate provenance" loose against L193). The ruling answers it from the body's own usage of the noun at L201 ("Neither provenance is reducible to the other") and L542 ("the two provenances"), and from GLM's point that construction *is* a provenance and does not have one. Answered.
- **C04** (Mimo: the typing is the sentence's only strict content). The ruling answers it: the sentence also names the parameters \(D\) and \(C\) that (K), L119 and L121–L127 are indexed to, which both readers' own C12 sections rely on. Answered.
- **C07** (Mimo: the replacement clause is inert). Taken as a FIX; examined above.
- **C08** and **C09** (Mimo: the second clauses apply to any component, like C07's). Both rulings answer it with the asymmetry this review checked: C08's and C09's first clauses are invariances, met vacuously by any component the contract never edits, so their second clauses do the work of requiring the contract to hold an edit to the component (L109's "\(A\) contains an edit that alters the relation reporting it"; L57's "a rule's application changes when the rule is edited"); C07's first clause is a change, and by L103 already requires such an edit. Answered, and consistent with C07 (see cross-ruling below).
- **C13** (GLM, set aside by GLM: "incompatible" does not say with what). The ruling answers it from L161 s3 and L377: the relatum is supplied by the question that exposes the defect and the criticism that alleges it, and the owner's words leave the grounds open (S21: "The problem may, for whatever reason, be ill posed."; S27's perpetual-motion example). Answered; Mimo's rival is rightly weighed as a different, narrower claim.
- **C15** (Mimo: "is" loose against L377). The ruling answers it from the text's own idiom at L271 ("which is a different question (Part III)"), and shows that "poses" would state L377's premise and connection no more than "is" does. Answered.
- **C18** (Mimo: L189 makes fidelity the component and global conditions while the sentence's uses attribute (A) to a violation; GLM reads "fidelity" as including (A)). The ruling shows that on the simulation layer, for a prediction read through the transport, (F2) at a pair gives (A) at that pair (L242 with L177), so a prediction contradicted at an occurring pair is a violation on either reading, and every use of the sentence (L223, L225, L582, L624–L626) lies where the readings agree. This review followed that argument and agrees. The two extents of the term are recorded as a matter for the term across lines, not for L220. Answered.
- **C22** (GLM, set aside: "contribution" in two senses, L305 and L435). The ruling shows the sentence fixes its own sense (the contribution that (B), a deletion test on commitments, records), and that L307 has already kept the Part XI sense apart. Answered.
- **C23** (Mimo: read as exhaustive, the definition would clash with L375's third sentence; "operative result" and "applicable relations" undefined). The ruling answers the first by showing that both excluded routes fail the definition's own clauses read in the history (the join, and the dependence clause, for that result), and the second by finding the phrases nowhere defined in file 99 and reading them as plain words fixed by the text's other uses (L73, L385, L487, L606; L91). Neither reader called either a failure. Answered; Mimo's rival is rightly weighed as a different claim (it moves the dependence from the route to the result, which every route to that result shares, against L307, L616 and L375's "read from the history, not from the result"), with the case verdicts O25, O20 and O39 shown at risk under it.
- **C24** (both readers: the idiom "(K1) fails" for a biconditional). The ruling shows the idiom is the text's own for a tag as the name of its condition (L281, "(F1) already fails"; L220; L277 and L606 for (E)). Answered.
- **C25** (Mimo: "the same transition" has no antecedent; "operative deliberative rule" and "structural map" undefined). The ruling answers the first from the map's own argument (the transition the map sends the objection to, which L409 uses in the same words), and the second as for C23: parts of the text's own vocabulary (L413, L397, L520; L125, L103; L375, L487, L606), with no case or definition turning on more. Answered.
- **C26** (Mimo: "a premise" unqualified). The ruling shows the sentence picks up the Live clause's "and not withdrawn it" on the same line, under (K2)'s quantifier over \(\operatorname{Prem}(u)\). Answered.
- **C27**, **C29**: taken as FIXes; examined above.

No KEEP leaves standing a defect a reader showed.

## The VARIES rivals not taken

Under rule 5, a rewording that changes nothing the theory needs is a FIX only if clearer. Fifteen rulings record a sentence as easy to vary in its wording on a reader's rival and keep the text's wording (C01, C02, C03, C04, C05, C06, C08, C09, C10, C11, C12, C19, C21, C24, C25, C26; C16, C17, C18, C14 and C22 record lesser rewordings of their own or a reader's). In each the ruling gives a reason from the text's own idiom why the text's wording and not the rival: the section's pattern (C01, L21; C10, L107 and L203), the verb the text keeps for holding named objects while others range (C04, L287 and L369), the shared idiom of the three bullets and L347 (C08, C09), the uniform unindexed run of "signature" between L121 and L127 (C12), the L11 frame and the "is"/"is" contrast (C11), the passive register of L77 and L13 (C19), the echo with L397 and Part IX's vocabulary (C21), the text's use of "meet" and "fails" for tags (C24), the order L409 points back to (C25), the named conclusion the S95 scrub put in (C26). None of these is a count of readers or of rivals (S20; rule 7), and none is settled (S28). This review found no rival among them that is clearer on a reason the ruling missed. Five rulings find a rival to be a different claim, not a rewording (C13, C15, C20, C22, C23), each with the line or case the different claim would break; this review agrees with each.

## Cross-ruling: no conflict; two matters recorded

1. **C08 (line 165) and C07.** The C08 ruling, having found that C08's second clause does work, adds: "The same holds of C07's replacement clause, on Mimo's own comparison. That is for C07's checker." The C07 ruling finds that clause idle, and the C09 ruling (line 113) gives the reason the two cases differ. This is not a conflict of rulings: the C08 remark is expressly deferred, the C08 KEEP does not rest on it, and the asymmetry (an invariance clause against a change clause that already requires, by L103, an edit replacing the component) answers the analogy. Recorded so the orchestrator sees that C07, C08 and C09 were read together here and stand together.
2. **C18 and C29.** C18 records two extents of "fidelity" across L189, L245, L247, L520 and L630 and proposes nothing; C29 changes the L520 gloss. Consistent: the C29 FIX adds two conditions that fall outside "fidelity" on either extent, and keeps "fidelity under change", which on the text's own heading at L247 reaches (A) for an account. Recorded as the one place where a FIX of this round touches a term another ruling flagged.
3. **C11 and C12** (one pair on L127): the C12 ruling was written while C11 was a stub and conditions its reading of "It" and "its" on C11's outcome; C11 is KEEP, so C12's reading stands. Consistent.
4. **C19 and C20** (one line, L225): each reads "the second" as fixed by the order of the two definitions; consistent.
5. **C04, C05 and C06** (one display and its lead-in): consistent, and they converge on one matter outside their candidates (next section, item 1).

## Matters the checkers recorded outside their candidates, collected

These are not objections and not rulings; they are what the checkers put down for the orchestrator and the next round, gathered in one place so that none is lost (lesson S28 of the reading rule's spirit: fill as you go, lose nothing). Each is the checker's, with the ruling it stands in.

1. **(K) applied beyond components of \(D\).** C04 (its closing note): Argument 1 reads (K) on \(\tau[C]\), a set of \(E\)'s pairs, and whether \(\tau[C]\) is a contract of \(E\) in L141's sense is a question for L554–L556 and L119. C05 (its section on the rival): L556 writes "By (K)" of a subnetwork \(\lambda(k)\), while (K) is stated for a component. C06 (its search for a failure): the same bridge, supplied at L119 and L233, "belongs to L119 and L556, not to this display". Three checkers, independently, on one matter.
2. **"event" is used at L53, L55, L161, L397, L604 and L612 and defined nowhere; "occurrence" is defined at L169; the text does not say how they are related** (C14, its observation beyond the item; to be read with L596's claim).
3. **"signature" in the everyday sense at L584** ("the signature of a selected transport meeting a change outside its history"), beside the defined term (C12, its note).
4. **L121 names four things and gives three bullets**; by L347 the rule-application bullet covers "a rule" and "a constitutive status" (C09, its dependents section).
5. **L109 gives roles "under \(A\)" while (K) builds a signature on a contract \(C\)** (C08, "Noticed, outside this item").
6. **L151's "prediction"** is used of a transport not said to be to the simulation layer, while L219 defines the term for transports to \(S\) only (C17, "One thing seen beside it").
7. **L273's second sentence** says an *account* fails non-circular dependence, where L269 and L277 use "account" strictly (C21, "Outside this item").
8. **L311's first sentence** does not say in words that each \(d_n\) does no work by itself, which L313's "such commitments" needs; one step shows it (C22, its result).
9. **A premise live twice over** (a leaf that is also a usable step's conclusion): withdrawing it leaves the step usable by the first disjunct of Live, so C26's first clause, read without restriction, says more than (K2) gives in that narrow configuration (C26, "Outside this item's challenge").
10. **"complete" in L471's first sentence** must be read as (CT1)'s "completes with \(o\in T[i]\)" for clause 2 of (CT2) to be (CT1) (C28, "Outside this item's challenge").
11. **"operative result", "applicable relations" (L375), "deliberative", "structural map" (L385)** occur only there and are defined nowhere; read as plain words (C23, C25).
12. **The two extents of "fidelity"** (C18; item 2 of the cross-ruling section).
13. **"contribution" in Part VI and Part XI** (L305; L435, L441), each sense fixed where it stands (C22).
14. **L27 gives no pointer to Part XIV** where L23 and L25 give theirs (C01, its note).

None of these was raised by a reader as a defect of the candidate it stands beside; none is applied; each is material for the next round's briefs if the orchestrator chooses.

## Small points in the rulings' own prose and citations (none bears on an outcome)

- **C04, line 48:** "Mimo is right that nothing becomes false" uses, in the checker's own voice, a word of the kind S23 scrubs ("true, not true"). It is a remark about a variation, not a proposed wording, and the KEEP does not rest on it. Recorded because the owner's words bind every sentence written; no other such word was found in any ruling's own voice (every other hit of the scrub's words in the rulings is inside a quotation of a reply, a record or the owner).
- **C29:** the ruling writes that Mimo's argument has "fidelity" name "(F1), (F2) and (A) (L245)" and "the three together at L630". L245 speaks of (F1) and (F2) only ("Together they are fidelity"), and L630's "so far as (F1), (F2) and (A) reach" lists the three without calling them fidelity, while L630's other clause keeps "the fidelity and the answers" apart. The imprecision is in the citation, not in the outcome: the two conditions the FIX adds fall outside "fidelity" on any reading (above).
- **C24 and C21:** both catch GLM's L267 for L269; the tabulation records the same. Nothing affected.
- **C28:** the two quotations of a web page are given as such; no book is quoted anywhere in the rulings.
- **File names:** every ruling stands at the task's path, not rule 11's; this review likewise. For the orchestrator.

## Checks against the owner's words, for this file

- **S20:** this review lists rulings and points made about them; it lists, counts, grades or ranks no rivals and no readers, and no argument here turns on how many readers or rivals stood on a side.
- **S21:** nothing here says what must happen to any candidate or to any person; where a ruling leaves a choice to the person choosing, this review leaves it there.
- **S23:** no word or idea the scrub forbids is used in this file's own voice; "argument" is used for reasons why this and not that; nothing is accepted otherwise than tentatively.
- **S25–S27:** no FIX and no KEEP examined here puts physical possibility where the owner's words do not place it; this review adds nothing there.
- **S28:** nothing here is settled. "Nothing to object to" means that the reasons in each ruling, read against the text and the replies, gave this reviewer no reason from the texts to contest it; a later argument can.
- **S33–S34:** nothing here proposes anything about what hard to vary covers; nothing is parked from this review because nothing in the rulings needed parking (each ruling records "Parked: nothing", and this review found the same); no value is moved in or out.

## Result

- **Objections:** none.
- **Cross-ruling conflicts:** none; five consistencies recorded above.
- **For the orchestrator (rule 12):** every ruling may be applied as written under rule 13; the fourteen matters collected above are material for the next round's briefs, not for this one's application.

*Finished 27 September 2026. Not committed.*
