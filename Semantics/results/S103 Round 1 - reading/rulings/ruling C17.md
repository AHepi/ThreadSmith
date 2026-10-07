# S103 Round 1 — ruling on C17 (L219)

*Written on 27 September 2026 by a fresh Opus 5.5 checker that built nothing of this round, read no reply before this task, and rules on no other candidate of it. This file obeys decision S23 except where it quotes the text, a reply, a record or the owner. Nothing here is settled (S28): the ruling is reasons why this and not that, open to any later criticism, and setting a wording aside is a choice made here for the reasons given.*

**Ruling: KEEP.** The sentence stands as it is.

**How C17 came here.** The tabulation marks C17 under rule 6 of the reading rule (both readers close HOLDS; no point of either shows a defect), which sends it to no checker and records it "held under both readers' attempts; not thereby final". The orchestrator sent it to a checker all the same. This ruling reads the readers' points afresh and looks for a failure of its own; it finds none, so its KEEP and the rule-6 record say the same thing, and neither is final.

**File name.** The reading rule (rule 11) names `results/S103 Round 1 - rulings/ruling C<nn> L<line>.md`; this file is at the path the orchestrator's task gave, `results/S103 Round 1 - reading/rulings/ruling C17.md`, as the other rulings of this round are.

## What was read

- The text under review, `tests/99 The semantics, standing alone.md` (md5 74f4a4c7619345747f4fa976ddac9548, checked before reading): L60–L260 whole, L570–L590 (Arguments 3 and 4), L616–L632 (the two-layer episode), and every line that uses `Ans` or `predict` (found by search): L23, L144, L151, L177, L215, L219, L223, L250, L369, L564, L582, L622–L630.
- The part 2 brief's section for C17 (`tests/S103 Round 1 - trying to vary the strong candidates - part 2, Parts III and IV.md`, lines 80–112), which gives the readers L133–L147, L175–L177, L183–L189 and L233–L253, and not the two-layer episode.
- The tabulation's section for C17 (`results/S103 Round 1 - reading/tabulation.md`, lines 1593–1685) and its rule-6 paragraph (line 38).
- Mimo's section on C17 (`s103_vary_mimo_2.response.txt`, lines 108–129) and GLM's (`s103_vary_glm_2.response.txt`, lines 101–121). A search of all six replies for `C17`, `L219`, `Ans_S` and `predict` found no other passage that bears on this sentence beyond the two readers' C18 sections, which argue about L220 and not about L219.
- The reading rule, `results/S103 Round 1 - how the replies will be read, written before sending.md`.
- The S98 ledger's entry for this sentence (`results/S98 Ledger of edits and recommendations/line-up/groups/04 Layers, transports, and provenance (Part IV).md`, lines 911–941: "L219.s1 · list item · line 219 · 3 changes, 3 records"), and the S90 point it records as declined (`results/S90 Cross-examination - revision 2 draft - returns/parts/s90_xexam_atria_C.response.txt`, point 1).
- The case the records tie to this section, N18 (Two footbridges on opening day), in the S89 case book and in its re-reading on the latest text (`results/S96 Check of the repaired copy - cases.md`, lines 581–595).
- The owner's decisions S20–S35 in `records/Semantics - Decisions.md`.

Every quotation of file 99 below was compared with its own line by program (`grep -F` on that line); every one was found there.

## The sentence

L219, the first item of the list that L217 opens:

```
- the **prediction** is \(\operatorname{Ans}_S(\tau(a),\sigma(b))\);
```

Its setting, L217: "Let \(t\) be a transport to the simulation layer \(S\), with contract \(C\) and, where \(t\) is selected, history \(H\). For an edit–boundary pair \((a,b)\in C\) actually occurring:"

Its terms:

- **\(\operatorname{Ans}\).** (Q), L144: "\operatorname{Ans}_p(a,b)=\mathcal Q(D,a,b). \tag{Q}", with L141: "\(\mathcal Q\) is a specified set-theoretic operation on \(D\), its solutions and its component structure, with codomain \(Y_p\)." With an organization in the subscript, as in (A) at L250 ("\operatorname{Ans}_E(\tau(a),\sigma(b))=\operatorname{Ans}_p(a,b). \tag{A}"), it is that organization's answer under the query, with L253: "The query \(\mathcal Q\) is held fixed; an account of a different query is not an account of this one."
- **\(S\) and its query.** L177: "The **simulation layer** \(S\) is an organization over \(P\) whose components are dependencies among things and whose queries are predictions: what a port of \(P\) will take under an admitted edit. \(S\) is where prediction lives."
- **\(\tau\), \(\sigma\).** L189: "\(\tau\) translates edits, \(\sigma\) translates boundaries", the translations of the transport \(t\) that L217 names.

So the sentence says: at an occurring pair of \(t\)'s contract, the prediction is what \(S\) answers, under its query, at the pair \(t\) carries that pair to.

## What the text asks of it

Read by line, the text uses the defined prediction for these:

1. **Whose answer it is: the simulation layer's, through a transport.** L177: "\(S\) is where prediction lives." L582 (Argument 4): "If there is no transport there is no prediction and hence no violation." The prediction must be \(S\)'s and must need \(t\).
2. **Defined whether or not the transport is faithful.** L223: "Prediction and violation are defined for every transport to the simulation layer, surprise only for a selected one: a constructed one that fails at an actually occurring pair of its contract is violated, and the failure is not surprise".
3. **Able to differ from what occurs.** The two-layer episode, L622: "\(S_0\) predicts occupancy from recent occupancy."; L624: "\(S_0\), predicting from occupancy, predicts nothing there and is violated when the thing re-emerges at a cell consistent with its velocity."; L626: "If the population's transports can only predict from occupancy, no member survives the extended history"; L628, the protected aim "predict the displacements that occur"; L630: "The swap edit is invisible in the sensory field and leaves every prediction unchanged." And the case N18 as re-read on the latest text (S96, line 591): "his prediction reached past anything his record rules out."
4. **Comparable with the target's answer in the form (A) states.** (A) at L250 equates an organization's answer at \((\tau(a),\sigma(b))\) with \(\operatorname{Ans}_p(a,b)\). For a transport to \(S\), (A) reads: the prediction equals the target's answer.
5. **Not an account.** L23: "It does not say prediction is explanation." The prediction is an answer, an output of a query, and not the component structure that (F1) and (F2) reach.

So what the theory needs from L219 is this: the answer of \(S\), not of the target; taken at the pair \(t\) carries the occurring pair to, so that it exists only where there is a transport; defined for a faithful and an unfaithful transport alike; and written in the form of (A), so that question fidelity for a transport to \(S\) reads as the prediction's equality with \(\operatorname{Ans}_p(a,b)\).

## The readers' points, weighed

Both readers close HOLDS. Neither alleges a failure of the sentence itself. Each wording is weighed on its own argument; how many readers tried which is not weighed.

**Mimo, `\(\operatorname{Ans}_S(a,b)\)` (translations dropped).** Mimo says this breaks L189 and (A) at L250. That stands: \(a\) and \(b\) are edits and boundaries of the transport's domain, and \(S\)'s answer is defined at \(S\)'s own edits and boundaries, which L189 reaches only through \(\tau\) and \(\sigma\); the expression is well formed only where the domain and \(S\) share their edits and boundaries. It also breaks item 1: \(\operatorname{Ans}_S(a,b)\) no longer mentions \(t\), so L582's "If there is no transport there is no prediction" would no longer follow from the definition. A different claim; set aside.

**Mimo and GLM, `\(\operatorname{Ans}_p(a,b)\)`.** Mimo says this breaks L177 and L144 (it is the question's profile, not the simulation's); GLM says it "makes the prediction correct by definition" and "abolishes violation". Mimo's break stands, and there is more: \(\operatorname{Ans}_p(a,b)\) needs no transport, which breaks L582 (item 1); and it cannot differ from the target's answer, which breaks the episode (item 3): at L624 the prediction at the occlusion pair would be where the thing is, not "nothing there". GLM's wording of the break needs one correction. Violation is defined at L220 as a failure of fidelity ("- a **violation** occurs when fidelity fails at \((a,b)\);"), not as a wrong prediction, so this wording would leave L220's violation in place. What it removes is the prediction's ability to go wrong, which the episode and N18 turn on. GLM's appeals to S20 and S23 are paraphrases (the tabulation records them as such), and neither decision speaks to what a prediction is; the break rests on L177, L582 and L624, not on them. A different claim; set aside.

**Mimo, `\(\operatorname{Ans}_S(\tau(a),\sigma(b))\) when \(t\) is faithful`.** Mimo says this breaks L223 and L582. The break of L223 stands: L223 defines prediction "for every transport to the simulation layer" and names a constructed transport that "is violated" at a pair of its contract; the episode at L624 gives a violated transport a prediction ("predicts nothing there and is violated"). The appeal to L582 adds little: "no transport, no prediction" is untouched by a condition on faithfulness. The break rests on L223 and L624. A different claim; set aside.

**GLM, `$\operatorname{Ans}_S(\sigma(a),\tau(b))$` (translations swapped).** GLM calls it a type error against L189. It is: \(\sigma\) translates boundaries and \(\tau\) edits (L189), so \(\sigma(a)\) and \(\tau(b)\) are undefined. Set aside.

**GLM, `- the **prediction** is what $S$ answers at the translated edit and boundary;`.** GLM says the verbal form "no longer pairs with (A)", so that question fidelity "can no longer be read as: the prediction equals the question's answer". That overstates it. The words name the same value: "what \(S\) answers" is \(\operatorname{Ans}_S\), and "the translated edit and boundary" is \((\tau(a),\sigma(b))\), since L217 fixes \(t\) and L189 fixes which translation takes which. Every item of the list above is kept. On this reading it is **a rewording that changes nothing the theory needs**, and the sentence is easy to vary in its notation, plainly meant (Mimo's step 3 says the same: "only re-spellings of the same expression survive"). It is not clearer. It leaves unsaid whose translations are meant, which the symbols carry, and it hides the shared form with (Q) at L144 and (A) at L250: set beside (A), the formula shows at a glance that for a transport to \(S\) question fidelity is the prediction's equality with \(\operatorname{Ans}_p(a,b)\) (item 4). A rewording that is not clearer leaves the sentence as it is (rule 5): KEEP.

## A failure of the sentence itself, sought

- **Is \(\operatorname{Ans}_S\) defined?** (Q) defines \(\operatorname{Ans}\) with a question in the subscript; L217 names a transport and a contract but no question. The query that \(\operatorname{Ans}_S\) evaluates is given by L177: \(S\)'s queries "are predictions: what a port of \(P\) will take under an admitted edit". That is the same reading (A) and L253 give \(\operatorname{Ans}_E\): the organization's answer under the query in play. No gap is shown. Writing the query into L219 would repeat L177.
- **A circle between L177 and L219?** L177 says what kind of query \(S\) has (it reads a port of \(P\) under an edit); L219 names that query's value at the pair \(t\) carries the occurring pair to. Neither defines the other's term by itself. No circle.
- **A part that does no work?** Each part does work that another reading lacks: the subscript \(S\) (item 1, against \(\operatorname{Ans}_p\)), \(\tau\) and \(\sigma\) (item 1, against \(\operatorname{Ans}_S(a,b)\)), and their order (L189).
- **Is the defined prediction idle, since L220 defines violation by fidelity and not by the prediction?** No. The prediction is the term by which L177, L223, L582 and the episode at L622–L630 speak, and N18 is read through it. Whether L220's "fidelity" should reach (A), so that a wrong prediction is a violation, is C18's matter (the tabulation sends C18 to a checker on it). C17's sentence stands under either reading of L220.
- **Several solutions, or none.** Where \(\operatorname{Sol}_S(\tau(a),\sigma(b))\) holds several solutions ("Several solutions remain several.", L105) or none, \(\mathcal Q\) is a set-theoretic operation (L141) and returns a value there as well; nothing in L219 presumes a single one.
- **Only at occurring pairs, and L630.** L217 gives "the prediction" at an occurring pair; L630 says the swap "leaves every prediction unchanged", which compares values at a pair with and without the swap. The formula is defined at every translated pair of the contract, as L177's query is ("under an admitted edit"); L219 names its value on the occasion. L630 reads on that basis. What "actually occurring" adds is C16's matter, not this sentence's.
- **The owner's decisions.** The sentence holds no word S23 forbids and no idea of belief or of verification; "prediction" is itself the word the S95 scrub put in place of "expectation" (S98 ledger, D-82 and D-551). It says nothing about physical possibility (S25–S27), nothing about what must happen (S21), and settles nothing (S28). It holds no list, count or grade (S20). It says nothing about what hard to vary covers (S33, S34) and places no value.
- **The S90 point.** At S90 a reader held that \(\operatorname{Ans}_S\) was undefined for a transport whose target is not \(S\), and offered either to scope the section to transports to the simulation layer or to write \(\operatorname{Ans}_E\). The first was taken, and file 99 carries it: L217 ("a transport to the simulation layer \(S\)") and L223 ("defined for every transport to the simulation layer"). The ledger records the \(\operatorname{Ans}_E\) wording as declined. With that scope, \(\operatorname{Ans}_S\) is typed for every transport the section speaks of.

No failure of the sentence is shown.

## One thing seen beside it, not ruled on

L151 (Part III) uses the word for a transport not said to be to the simulation layer: "A measure that identifies an outcome, together with a prediction of the outcome from it through a transport faithful on the contract, answers the identification question". L219 defines "the prediction" only for transports to \(S\) (L217). L151 reads in the ordinary sense, and its prediction has the same shape (an organization's answer at the translated pair), so nothing in it contradicts L219, and widening L219 to cover it would undo the S90 scope just described. This is recorded for whoever looks at L151; it is not a ruling on it, and nothing in it calls for a change to L219.

## What the ruling touches

KEEP changes nothing, so no line moves and no case verdict moves. The sentences that rely on L219, and read as before: L177.s2 ("\(S\) is where prediction lives."), L223 ("Prediction and violation are defined for every transport to the simulation layer, …"), L582 ("If there is no transport there is no prediction and hence no violation."), and the two-layer episode at L622, L624, L626, L628 and L630. The case N18, whose fixed verdict the S96 re-reading gives through "his prediction reached past anything his record rules out", reads as it did: Rhea's constructed transport and Dov's selected one each have a prediction at the large-crowd pair, each is violated there, and only Dov's violation, at a pair outside his history, is surprise (L221, L223).

**Parked (S34).** No point of either reader, and nothing in this ruling, proposes anything about what hard to vary covers.

## For the structured result

- **Ruling:** KEEP.
- **Line:** 219.
- **Old = new:** `- the **prediction** is \(\operatorname{Ans}_S(\tau(a),\sigma(b))\);`
- **Easy to vary:** no reader closed VARIES. GLM's verbal wording is a rewording that changes nothing the theory needs, so the sentence is easy to vary in its notation only; it is not clearer, and the sentence is kept. Every other wording tried is a different claim and breaks a named line.
