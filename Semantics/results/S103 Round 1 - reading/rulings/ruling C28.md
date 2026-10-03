# S103 Round 1 — ruling on C28 (L471)

*Written by a fresh checker (Opus 5.5), 27 September 2026, filled as it goes. Not committed. This file obeys decision S23 except where it quotes the text, a reader, a record or the owner.*

**Ruling: FIX.** The third clause changes; the first two and the label stay.

- **Old (L471, second sentence of the line):** `\(F\) is monotone; \(C\subseteq F(C)\) is the invariant form; the union of post-fixed sets is the greatest fixed point. (CT2)`
- **New:** `\(F\) is monotone; \(C\subseteq F(C)\) is the invariant form; the greatest fixed point is the union of the sets \(D\) with \(D\subseteq F(D)\). (CT2)` (Mimo's rival, reply line 228, word for word)
- **Easy to vary on this reading (rule 5):** yes, in the plain sense the brief asks about, and recorded as such. Mimo's rival is a rewording that changes nothing the theory needs from the sentence: it names the same sets, makes the same claim, keeps the three clauses apart and keeps the label (CT2) that L546 names. It is taken because it is clearer (reasons below), not because the text's wording is at fault.

This ruling settles nothing (decision S28).

## What was read

- The text under review, `tests/99 The semantics, standing alone.md`, md5 74f4a4c7619345747f4fa976ddac9548 (checked before reading; not written to): L440–L560 whole (the end of Part XI, Parts XII to XV, the start of Part XVI), L113, L138–L144, L183–L189, L287, L305 and L329; and the whole file searched by program for "CT1", "CT2", "RetReal", "post-fixed", "fixed point", "monotone", "retention", "retained", "invariant form", and for the letters \(D\), \(W\), \(Y\) and \(Z\).
- The reading rule, `results/S103 Round 1 - how the replies will be read, written before sending.md`, whole.
- The part 3 brief, `tests/S103 Round 1 - trying to vary the strong candidates - part 3, Parts V to XIV.md` (md5 44ef4fbdb179963c3e76fcdaf60ecf27): the C28 entry (brief lines 175–195) and the section 4 lines it points to (L461, L546), found by search.
- The tabulation, `results/S103 Round 1 - reading/tabulation.md` (md5 51e752c3e26ab822e69daf8e9ec9f387): C28's section (lines 2786–2899) and the two notes that name C28 (lines 3049 and 3051).
- The replies: `s103_vary_mimo_3.response.txt` (md5 a1491ae7b541cf691c5760cf07c93d44) lines 223–252, and `s103_vary_glm_3.response.txt` (md5 540429867c7029b78bcb9ad72c1af834) lines 110–124. All six replies were searched for "C28", "CT2", "L471", "post-fixed" and "fixed point"; there is no hit outside those two sections. No reasoning file was opened.
- The owner's decisions S20–S35 in `records/Semantics - Decisions.md` (md5 71459192867b1ebcf1bae914c9297129).
- For ties to cases and history: the S98 ledger, group 12 (`results/S98 Ledger of edits and recommendations/line-up/groups/12 The physical module (Part XII).md`), entries L471.s1 and L471.s2, and `line-up/data/by sentence.csv` and `line-up/data/records.jsonl`, searched for "L471", "CT2", "post-fixed" and "fixed point"; `results/S96 Check of the repaired copy - cases.md`, searched for "l. 463" to "l. 479", "(CT", "Part XII", "RetReal", "fixed point" and "post-fixed"; the S81 case book of 52 cases, the S89 candidate cases N1 to N25 and the S89 candidate case D3-T (`final.md`), searched for "fixed point", "post-fixed", "(CT", "RetReal", "monoton", "retain", "retention" and "constructor".
- One outside page, for how the name "post-fixed" is used: the Wikipedia article "Fixed point (mathematics)", its passage on prefixed and postfixed points, read through a fetch tool. It is not a book.

## The sentence and where it stands

L471 in full:

> **Retention fixed point.** \(F(C)\) = states whose executions all complete and return into \(C\). \(F\) is monotone; \(C\subseteq F(C)\) is the invariant form; the union of post-fixed sets is the greatest fixed point. (CT2)

The sentence under review is the second one (unit L471.s2). The terms it uses:

- L461: "an attribute a set of its states". So \(F\) takes a set of states to a set of states, and the sets are ordered by inclusion.
- L463: "For protocol \(\pi\), task \(T\), constructor attribute \(C\), and enabling conditions \(\chi\),"
- L466, (CT1): "\operatorname{RetReal}(\pi,T,C;\chi)\iff\forall z\in C\ \forall i\in\operatorname{dom}T\ \forall\eta\in\operatorname{Exec}(\pi,z,i;\chi),\ \eta\text{ completes with }o\in T[i]\text{ and }z'\in C."
- L469: "Execution families are nonempty on admitted inputs; deadlock is not a vacuous performance of the task."
- L546: "A counterexample to the finite monotone claim, (I2), (O1), (T2), (CT2), or Arguments 1–3 under their stated assumptions."

"Post-fixed" stands nowhere else in file 99 and is defined nowhere in it (search by program: L471 only). "Fixed point" and "greatest fixed point" stand only at L471. No other line of file 99 names (CT2) but L546. (CT1) is named at L466, L495 and L526.

**History (S98 ledger).** Group 12 heads both units of L471 "no change recorded" (L471.s1 and L471.s2), and no record in `records.jsonl` or `by sentence.csv` names L471. The only records that touch (CT2) are those on L546 (A-23, declined; D-242 and D-243, the S95 scrub's "theorem" to "claim" and "Derivations" to "Arguments"); none changes the label.

## What the sentence says, checked

With \(F(C)\) as L471 defines it (the states whose executions, for every input in \(\operatorname{dom}T\), all complete and return into \(C\)):

1. **\(F\) is monotone.** If \(C\subseteq C'\), a state whose executions all return into \(C\) has executions that all return into \(C'\); so \(F(C)\subseteq F(C')\). Both readers find the same (Mimo line 249, GLM line 121). Holds.
2. **\(C\subseteq F(C)\) is the invariant form.** \(C\subseteq F(C)\) says that every state of \(C\) has all its executions complete and return into \(C\): (CT1) for \(C\), read with L471's "complete" as (CT1)'s "completes with \(o\in T[i]\)". So (CT1) is the condition that \(C\) is carried into itself by \(F\). Holds, on that reading (see the last section for the reading).
3. **The union of post-fixed sets is the greatest fixed point.** The sets of states, ordered by inclusion, form a complete lattice. Let \(U\) be the union of the sets \(D\) with \(D\subseteq F(D)\). Each such \(D\) has \(D\subseteq F(D)\subseteq F(U)\), by monotonicity; so \(U\subseteq F(U)\). By monotonicity again \(F(U)\subseteq F(F(U))\), so \(F(U)\) is one of the sets whose union is \(U\), and \(F(U)\subseteq U\). So \(U=F(U)\); and every fixed point is one of the sets \(D\), so lies inside \(U\). Holds, and each step that needs monotonicity uses the first clause.
4. **Non-vacuity.** Were an execution family empty, a state would return into every set by default; L469 excludes it on admitted inputs (both readers). Holds.

What the sentence gives the theory: the sets \(D\) with \(D\subseteq F(D)\) are exactly the attributes \(D\) with \(\operatorname{RetReal}(\pi,T,D;\chi)\), by clause 2; so the greatest fixed point is the largest constructor attribute on which the protocol is a retained realization of the task, the union of every attribute (CT1) holds on. (CT2) states that this largest attribute exists and is a fixed point; L546 names it as a claim a counterexample to which would rule the class out.

**The name "post-fixed".** Clause 3 holds when "post-fixed set" means a set \(D\) with \(D\subseteq F(D)\), which is the usage the Wikipedia article gives ("a postfixed point of f is any p such that p ≤ f(p)"), with the remark "The opposite usage occasionally appears." Read the other way (a set \(D\) with \(F(D)\subseteq D\)), the set of all states is one such set, since \(F\) of anything is a set of states; the union is then the set of all states, and that is a fixed point only when every state's executions all complete and return, which fails for any protocol with a state from which some execution does not complete. So whether clause 3, a claim L546 exposes to counterexample, holds or has a counterexample turns on a naming convention the text neither states nor uses anywhere else. GLM's own variation shows it: with "pre-fixed" in its place the clause is "false for F as defined" (GLM line 118).

## What the theory needs from the sentence

1. That \(F\) is monotone, stated, since clause 3 stands on it (both readers: Mimo line 247, GLM line 119).
2. That (CT1) is the invariant form \(C\subseteq F(C)\), tied to (CT1)'s \(z'\in C\) (GLM line 117).
3. That the greatest fixed point is the union of every set that has the invariant form: the largest retained attribute exists.
4. The three as separate clauses under one label, (CT2), so that L546 can name them and each can be taken or ruled out on its own (GLM lines 112 and 116).

## Each side's argument (rule 7)

**Mimo (VARIES).** Rival: `\(F\) is monotone; \(C\subseteq F(C)\) is the invariant form; the greatest fixed point is the union of the sets \(D\) with \(D\subseteq F(D)\). (CT2)` (reply line 228; the closing line, line 251, gives it in plain Unicode). The argument: "'Post-fixed sets' is not defined in the lines given; spelling out the class names the same sets, and the three claims and the label (CT2) stay." (line 231). Variations said to break something: `\(C = F(C)\)` for `\(C\subseteq F(C)\)` breaks (CT1), which "asks only that states of \(C\) return into \(C\), not that nothing outside returns in" (lines 236–239); "least fixed point" for "greatest" "Breaks the third clause itself" and bears on L546 (lines 242–245); dropping "F is monotone" "leaves the union clause with nothing to stand on" (line 247). Step 3: "No fault." (line 249).

**GLM (HOLDS).** Closing line: "merging lost the separately citable claims that L546 targets, 'an invariant' broke the tie to (CT1)'s `z'∈C` (L466), and 'pre-fixed' is false." (line 123). Its variations: the merged sentence `F is monotone, so post-fixed sets C ⊆ F(C) are closed under union and their union is the greatest fixed point.`, which "entangles the three separable claims" (line 116); `C ⊆ F(C) is an invariant`, which drops "the invariant form" and "breaks the tie to (CT1)" (line 117); `pre-fixed` for `post-fixed`, "false for F as defined" (line 118); dropping `F is monotone`, which "leaves the third clause unsupported" (line 119). Fault sought and not found (line 121).

**Where they differ.** Not on the sentence's content: both find each clause holds, for the same reasons, and both find the same breaks in dropping "F is monotone" and in the wrong direction of fixed point or of inequality. They differ only on whether a wording that keeps the claim works as well; GLM tried no wording that spells out the class, and Mimo tried nothing but that.

**GLM's three grounds, weighed against Mimo's rival.**

- *Merging loses separate citability.* So it does, in GLM's merged sentence, which puts the three claims under one "so". Mimo's rival does not merge: it keeps the three clauses, the two semicolons and the label, as Mimo says (line 231). The ground does not bear on the rival.
- *"An invariant" breaks the tie to (CT1).* So it does, in GLM's variation. The rival keeps "the invariant form" word for word. The ground does not bear on the rival.
- *"Pre-fixed" fails.* So it does, under the usage the text evidently intends. It does not bear against the rival, which uses neither name; it bears for it, since it shows that whether the clause holds turns on a single undefined word (above).

So GLM's HOLDS stands as a finding that the sentence has no fault, which this ruling shares; it gives no argument why the text's wording and not Mimo's.

**Mimo's grounds, checked.** The break under \(C=F(C)\) is real: (CT1) at L466 asks that the states of \(C\) return into \(C\), and a fixed point asks also that every state returning into \(C\) be in \(C\), which (CT1) does not; so the "invariant form" would demand more than (CT1). The break under "least" is real: for a task with any input, \(F\) of the empty set is empty (by L469 each state has an execution, and no execution returns into the empty set), so the empty set is the least fixed point, and "the union of post-fixed sets is the least fixed point" would fail whenever any non-empty attribute is retained. The point on monotonicity is real (step 3 above).

## Is the rival a rewording or a different claim?

Against items 1–4 above:

- Item 1: kept word for word ("\(F\) is monotone").
- Item 2: kept word for word ("\(C\subseteq F(C)\) is the invariant form").
- Item 3: kept. "The sets \(D\) with \(D\subseteq F(D)\)" are the post-fixed sets under the usage on which the text's clause holds; the union of the same sets is said to be the same greatest fixed point. Turning the clause about ("the greatest fixed point is the union …" for "the union … is the greatest fixed point") states the same identity; a counterexample to either is a monotone \(F\) of this kind whose union of such sets is not a fixed point, or not the greatest.
- Item 4: kept; three clauses, the same label.

**Dependents under the rival.** L546 names (CT2) and reads as before. No other line uses "post-fixed", "fixed point" or (CT2). L475 ("requires an owned retained realization"), L495 ("in the sense of (CT1)") and L526 ("Deploy depends on (R) and (CT1)"; "owned capability on Ownership, (CT1) and a declared continuity") use (CT1), which is unchanged, and \(F\), which is unchanged.

**The owner's words.** The rival has no word or idea S23 forbids; "greatest" and "union" are the order of sets of states by inclusion, not an order on explanations, rivals or thinkers (S20, S23, L522). It says nothing about what must happen (S21); it lists, counts and grades no rivals (S20); it stands in Part XII, where the owner places physical possibility, as the retention of a carrier's capacity to perform a task (S25–S27), and changes nothing in that reach; it settles nothing (S28). Nothing in it is about what hard to vary covers (S33–S34); nothing here is parked. Values are not touched.

So the rival makes no different claim and is not weighed as a challenge; the sentence is easy to vary on this reading, and that is recorded.

## Is the rival clearer?

**For the rival.**

1. It defines what the text leaves undefined. "Post-fixed" is used once in file 99 and defined nowhere; a reader without the lattice-theory term cannot read the clause at all. The rival states the class in the notation the sentence has just used for \(C\).
2. It removes the dependence on a naming convention. Authors do not all use "post-fixed" one way (above), and read the other way the clause fails. Whether a clause that L546 exposes to counterexample holds should not turn on the reader's convention; the rival leaves no such room.
3. It shows the tie between clauses 2 and 3 on its face: \(D\subseteq F(D)\) has the shape of \(C\subseteq F(C)\), so a reader sees that the greatest fixed point is the union of every set with the invariant form, the largest attribute (CT1) holds on. In the text's wording that tie has to be supplied by knowing the term.

**Against the rival.**

1. It is longer: "post-fixed" goes, and "the", "with", the letter \(D\) and a formula come in.
2. It binds a letter, \(D\), that the text uses from Part II to Part VI for a question's target organization (L113, "Fix an organization \(D\)"; L138; L141, "\(D\) is the target"), and as the tag (D) at L526. The cost is small: the rival binds \(D\) in the clause that introduces it, as sets of states with a condition, and the text already uses letters locally (Part XII reuses \(C\), the contract of L113 and L141, as the constructor attribute of L463; L329's \(F\) is not L471's \(F\); L287 binds \(W\subseteq\Gamma\) for one definition). The other capital letters checked for a replacement are also used elsewhere in file 99 (\(W\) at L287, \(Y\) at L141 and L329, \(Z\) at L329); \(D\), the letter after \(C\), marks a set of the same kind as \(C\), which is the ordinary habit. No reason was found for another letter over Mimo's.
3. Readers who know the term lose nothing by it, and gain nothing from the rival but the convention stated.

Weighed together, the rival is clearer: points 1 and 2 for it remove a real way for the claim to be misread, and the costs against it are length and a bound letter the text's own habits already allow.

**Why this wording, and not a smaller change.** The smallest substitution, `the union of the sets \(D\) with \(D\subseteq F(D)\) is the greatest fixed point`, leaves the order as it is, but puts a formula directly before "is", right after the clause "\(C\subseteq F(C)\) is the invariant form", in which the formula is the subject of "is"; the parallel invites the reading "\(D\subseteq F(D)\) is the greatest fixed point". Mimo's order puts "the greatest fixed point" first and ends on the formula, so the misreading has no place, and states the identity in the form in which it is usually stated. A gloss that keeps the name (`the union of the post-fixed sets, the sets \(D\) with \(D\subseteq F(D)\), is the greatest fixed point`) is longer still, keeps a term that does no work once the class is spelled out, and keeps the formula before "is". So the FIX is Mimo's wording, word for word, in the LaTeX of reply line 228 (the text's own markup), not the Unicode of the closing line.

## The variations that change the claim, and what each breaks

None is a repair of a fault in the sentence, and none is taken.

- `\(C = F(C)\)` for `\(C\subseteq F(C)\)` (Mimo, line 236): the invariant form would ask more than (CT1) (above). Real.
- "least fixed point" for "greatest fixed point" (Mimo, line 242): fails for this \(F\) whenever a non-empty attribute is retained (above). Real.
- Dropping "\(F\) is monotone" (both readers, described): the union clause loses its ground, as both say; the claim would still hold of this \(F\), but the sentence would no longer say why, and L546's "finite monotone claim" and (CT2) would lose the stated premise a counterexample would have to break. A loss, and neither reader proposes it.
- GLM's merged sentence (line 116): the same content with the three claims tied by "so" into one; loses the separate clauses (item 4). Not taken, as GLM says.
- `C ⊆ F(C) is an invariant` (GLM, line 117): loses "the invariant form", the tie to (CT1)'s \(z'\in C\) (item 2). Not taken, as GLM says.
- `pre-fixed` for `post-fixed` (GLM, line 118): fails under the usage on which the text's clause holds (above). Real.

## Failures of the sentence itself

None shown by either reader, and none found. Sought: contradiction with (CT1) at L466, with L469, L475, L495, L526 or L546 (none); vacuity (excluded by L469, as both say); a part doing no work (each clause is used by the next, and the label by L546); the owner's words (as above).

## Cases

No fixed case verdict moves under this FIX.

- **S98 ledger.** L471.s1 and L471.s2: "no change recorded"; no record names L471, and none ties it to a case.
- **S96 cases.** The cases the S96 check reads on Part XII are O11, O17, O30, O41 and O51 ("Boundary, ownership and capability: l. 427, l. 473 and l. 475"), O49 ("given (l. 475, l. 526)") and N20 (l. 479, the tolerances). None cites l. 471 or (CT2). Those on l. 475 turn on owned capability, which "requires an owned retained realization" (L475), that is on (CT1) and \(F\); both are unchanged, and the FIX names the same sets.
- **The S81 case book, the S89 candidate cases N1 to N25 and D3-T.** No hit for "fixed point", "post-fixed", "(CT", "RetReal" or "monoton"; no case turns on (CT2).
- **The text's own cases.** None turns on (CT2). L477 (CA) says "retention is applied to the inquiry-enabling organization"; it does not use the third clause.

## Dependents (named for the record)

- L546: "A counterexample to the finite monotone claim, (I2), (O1), (T2), (CT2), or Arguments 1–3 under their stated assumptions." Reads as before; (CT2) names the same three clauses.
- L471's first sentence, which defines \(F\): unchanged, and read by the new clause as before.
- (CT1) at L466, and its users L475, L495 and L526: unchanged; they do not use the third clause.

## Outside this item's challenge (not ruled here)

For the orchestrator and the next round only; nothing in this ruling rests on these, and no wording is applied.

- **"Complete" in L471's first sentence.** Clause 2 is (CT1) only if "all complete" in \(F\)'s definition is read as (CT1)'s "completes with \(o\in T[i]\)". Read as ending alone, \(C\subseteq F(C)\) would be weaker than (CT1), and "the invariant form" would be the form of (CT1)'s return condition only. The first sentence is not under review, and neither reader raised it.
- **What \(F\) depends on.** \(F\) is defined for the \(\pi\), \(T\) and \(\chi\) of L463, which its notation leaves implicit; nothing turns on it here.
- **File name.** Rule 11 of the reading rule names `results/S103 Round 1 - rulings/ruling C<nn> L<line>.md`; the task named `results/S103 Round 1 - reading/rulings/ruling C28.md`, and that path was used. No second copy was written.

## Quotations checked

Every quotation of file 99 in this ruling was compared by program with the line given, byte for byte with its LaTeX markup, and each was found: L113, L141, L287, L461, L463, L466 (the display without its brackets and tag), L469, L471 (the line whole, and the sentence under review), L475, L477, L495, L522, L526 (both quotations) and L546. The quotations of the replies were compared with the reply files and found on the lines given: Mimo lines 228 (the rival, byte for byte, which is also the new wording), 231, 236, 239, 245, 247, 249 and 251; GLM lines 116, 117, 118, 119 and 123. Where a quoted passage holds double quotation marks of its own, they are set here as single quotation marks (Mimo line 231; GLM line 123). The S96 quotations ("Boundary, ownership and capability: l. 427, l. 473 and l. 475"; "given (l. 475, l. 526)") and the S98 heading ("no change recorded") were found. The two quotations of the Wikipedia article are as the fetched page gave them; they are a web page's words, not a book's. No book is quoted.

The new wording differs from the old only in the third clause: "the union of post-fixed sets is the greatest fixed point" becomes "the greatest fixed point is the union of the sets \(D\) with \(D\subseteq F(D)\)". The first two clauses, the semicolons, the full stop and the label "(CT2)" are unchanged.
