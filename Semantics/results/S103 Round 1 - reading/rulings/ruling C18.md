# S103 Round 1 — ruling on C18 (L220)

*Written by a fresh checker (Opus 5.5), 27 September 2026, filled as it went (this file was created first as a stub and then filled; no other file was written over). Not committed by this checker; the orchestrator committed the stub as work in progress (d34c929). This file obeys decision S23 except where it quotes the text, a reader or the owner.*

**Ruling: KEEP.** The sentence stands as it is at L220 of `tests/99 The semantics, standing alone.md` (md5 74f4a4c7619345747f4fa976ddac9548, checked before reading; not written to):

> - a **violation** occurs when fidelity fails at \((a,b)\);

This ruling settles nothing (decision S28). It records that the sentence came through both readers' attempts and this checker's own; that the doubt which sent it here (which conditions the unqualified word "fidelity" names) is real as a matter of the term across several lines of the text, but shows no defect in this sentence, since the two readings give the same violations on everything the passage and the text's cases use; and that no wording tried reads more plainly while keeping what the theory needs from the sentence.

## How this checker came to the item

The tabulation (`results/S103 Round 1 - reading/tabulation.md`, the C18 section at its lines 1690–1720 and the notes at its lines 40, 3035 and 3047) records both readers closing HOLDS and sends C18 to a checker under rule 5's clause on doubt: "Mimo's step 3 records that the text forces a transport's faithfulness to be the component and global conditions (L189), while "Question fidelity" heads (A) (L247) and the sentence's uses attribute (A) to a violation, and GLM reads the sentence's "fidelity" as including (A). Neither reader calls this a failure; whether it shows one is in doubt." The readers do not differ in their closing lines, so rule 7 has no disagreement of verdicts to rule between; where their readings of the word differ, each is weighed below on its argument. This file stands where the task names it, not where rule 11 of the reading rule names it (`results/S103 Round 1 - rulings/ruling C<nn> L<line>.md`); the sibling rulings stand at the task's path too.

Read for this ruling: the reading rule (`results/S103 Round 1 - how the replies will be read, written before sending.md`); decisions S20 to S35 in `records/Semantics - Decisions.md`; the part 2 brief (`tests/S103 Round 1 - trying to vary the strong candidates - part 2, Parts III and IV.md`, md5 387f826f93ba0922458007feefc6bd61), its section 1, its entries for C17 and C18 (lines 105–124) and its task and report sections (lines 343–371); the tabulation's C18 section; Mimo's C18 section (`s103_vary_mimo_2.response.txt`, lines 131–152) and GLM's (`s103_vary_glm_2.response.txt`, lines 123–147), whole; a search of all six replies for "C18", "L220", "violat" and "fidelity fails", which turned up, as bearing on this item, GLM's C17 remark (reply line 115), Mimo's C17 variation (reply line 125) and Mimo's C29 step 3 (`s103_vary_mimo_3.response.txt`, line 277); no `.reasoning.txt` file. In file 99: L17, L41–L43, L67, L83–L149, L165–L225, L229–L277, L520, L554–L632. The S98 ledger (`results/S98 Ledger of edits and recommendations/line-up/data/by sentence.csv`), searched by program for rows on L189, L219–L226, L245–L253, L576–L584 and L622–L632 and for "violation": it holds no row for L220.s1, the sentence under review, which stands word for word as it stood in the earliest text the project holds. The case books (`tests/S81 Case book - the 52 cases, situations and fixed verdicts, as the tested agent sees them.md`, `tests/S89 Case book - candidate cases N1 to N25 drawn from the sources.md`), searched for violation, surprise and prediction. Every quotation of file 99 below was compared with it by program, each found on the line given.

## The sentence in its place

> L217| Let \(t\) be a transport to the simulation layer \(S\), with contract \(C\) and, where \(t\) is selected, history \(H\). For an edit–boundary pair \((a,b)\in C\) actually occurring:
>
> L219| - the **prediction** is \(\operatorname{Ans}_S(\tau(a),\sigma(b))\);
>
> L220| - a **violation** occurs when fidelity fails at \((a,b)\);
>
> L221| - **surprise** is a violation of a selected transport at \((a,b)\notin H\).

What it uses:

- **faithful**, L189: "A transport is **faithful on \(C\)** when it meets the component and global fidelity conditions of Part V."
- **the fidelity conditions**, stated for every pair of the contract: (F1), L233, "and every \((a,b)\in C\)" … L236; (F2), L242: "\pi[\operatorname{Sol}_D(a,b)]=\operatorname{Sol}_E(\tau(a),\sigma(b))" with "\tau(1)=1,\quad \tau(a_2a_1)=\tau(a_2)\tau(a_1)"; and L245: "(F1) prevents an assembled match from hiding a decomposition in error. (F2) prevents a set of pieces each faithful locally from hiding a lost shared constraint. Together they are fidelity at every level the contract reaches."
- **question fidelity**, L247: "**Question fidelity.** For every \((a,b)\in C\)," with (A) at L250, "\operatorname{Ans}_E(\tau(a),\sigma(b))=\operatorname{Ans}_p(a,b)", and L253: "The query \(\mathcal Q\) is held fixed; an account of a different query is not an account of this one."
- **the prediction**, L219, and the simulation layer's queries, L177: "whose queries are predictions: what a port of \(P\) will take under an admitted edit."
- **survival**, L195: "a survival condition requiring fidelity on \(H\)".

## What the sentence does

1. **It makes a violation an event at the occurring pair.** With C16's head ("actually occurring", L217) it says a violation "occurs" there; the standing relation is fidelity itself, which L41 keeps apart from what happens to the transport: "Survival is how the transport got there; fidelity is what it is."
2. **It locates the failure at one pair.** Every fidelity condition is stated over the whole contract (L233 "and every \((a,b)\in C\)", L247 "For every \((a,b)\in C\)"), and "faithful on \(C\)" (L189) is the whole-contract relation; this sentence takes the instance of the conditions at the one pair that occurs. GLM's remark on this (reply line 145) holds: "In fact this sentence is what *does* the localization". L43 uses the pair-local relation in words: "whether a transport is faithful at a pair turns on the transport and the target".
3. **It makes a violation the failure of the very relation selection is tested on.** Survival requires "fidelity on \(H\)" (L195); a violation is a failure of fidelity at a pair; surprise (L221) is such a failure outside \(H\). Argument 3's consequence joins the two sides in one relation: "A correspondence produced by selection is faithful where it was tested" … "It is also why surprise is possible." (L576), and its proof works on component relations: "Survival on \(H\) constrains only \(\{L_j(a,b):(a,b)\in H\}\)." (L574). Argument 10 names the event in the same word: "the fidelity failure is structural, not parametric" (L626).
4. **It keeps a violation apart from anyone's noticing it.** Fidelity turns on the transport and the target; L67: "Whether a transport is faithful on a contract is independent of whether anyone tentatively accepts it." L223 then separates a violation from "a violation the system represents", which "can be a recognized difficulty (Part X)".

## The doubt, and why it shows no defect in this sentence

**The two readings.** The text uses "fidelity" with two extents.

- *Narrow, (F1) and (F2):* L189 defines "faithful" by "the component and global fidelity conditions of Part V", and L245 says of (F1) and (F2): "Together they are fidelity at every level the contract reaches." L630 keeps the fidelity apart from the answers: "the exchange carries the fidelity and the answers of \(t_1\) over to the second transport". This is Mimo's reading of L189 (reply line 150: "the text forces a transport's faithfulness to be the component and global conditions (L189)"). The drafters' plain-words word sheet (`plain words/92 working record/word sheet.md`, line 95) glosses "global fidelity" as "whole matching", which is (F2); this ruling does not rest on it.
- *Wide, (F1), (F2) and (A):* L247 heads (A) "**Question fidelity.**"; L520 glosses all of (E) as "Account, from fidelity under change (E)." GLM reads the sentence this way (reply line 131: "Fidelity has parts: (F1) and (F2) at L233–L243, and (A) at L247–L251"), and so does GLM's C17 remark (reply line 115: "fidelity can fail, which is what violation is (L220)", said of (A) at L250); so does the brief's list of what C18 uses ("fidelity: (F1), (F2), (A): L233–L253"). Mimo's own C29 step 3 counts (A) among the fidelity conjuncts ("The gloss thus names one of three groups and omits two", `s103_vary_mimo_3.response.txt`, line 277), against its C18 step 3.

Mimo's own conclusion (reply line 150) is "the sentence's word covers the passage either way". This checker weighed whether that holds.

**Where the readings part.** Only where (A) fails at the pair while (F1) and (F2) both hold there. On the passage's own setting that does not arise. The simulation layer's queries are predictions of "what a port of \(P\) will take under an admitted edit" (L177), and the one tie the passage gives between the valuations of \(S\) and the ports of its target is the transport's \(\pi\) (L189). Where (F2) holds at \((a,b)\), \(\pi[\operatorname{Sol}_D(a,b)]=\operatorname{Sol}_S(\tau(a),\sigma(b))\): the valuations of \(S\) at the pair are the target's carried over. A prediction read from them at the port the transport ties to the predicted port (where \(\pi\) carries that port's value) is then the target's answer at the pair, and (A) is met there. So:

- a prediction contradicted at the occurring pair goes with a failure of (F2) there, and is a violation on either reading;
- a failure of (F1) or (F2) at the pair with the prediction uncontradicted is a violation on either reading;
- the readings part only where \(S\)'s query reads something other than what the transport carries to the predicted port, that is, where the prediction answers a query other than the one the correspondence carries (compare L253: "The query \(\mathcal Q\) is held fixed; an account of a different query is not an account of this one."). The text states no such case, and no line or verdict turns on how it would be classed.

**Every use of the sentence lies where the readings agree.**

- L582: "If there is no transport there is no prediction and hence no violation." With no transport there is neither a prediction nor a fidelity relation; the chain reads alike on either reading.
- L622–L626, Argument 10: \(S_0\) "is faithful on \(H_0\)" (L622); at the occlusion, "\(S_0\), predicting from occupancy, predicts nothing there and is violated when the thing re-emerges at a cell consistent with its velocity." (L624). Port values may be histories (L105: "Values of ports may be paths, functions, fields, mathematical structures or histories."); the target's solutions at the occlusion pair hold the thing re-emerging, \(S_0\)'s hold nothing there, so (F2) fails at that pair, the prediction is contradicted, and L626 calls the event "the fidelity failure". The verdict "This is surprise (Argument 4)." (L624) is reached on either reading.
- L223 and L225 speak of violations of any transport to the simulation layer and of the two responses to one; L580–L584 restate surprise as "a violation of a selected transport at an occurring \((a,b)\in C\) with \((a,b)\notin H\)" (L582). None of them turns on the corner where the readings part.

**So the doubt shows no defect in L220.** What it does show is that the word "fidelity" has two extents across the text (L189 and L245 against L247 and L520, with L630 on the narrow side). That is a matter of the term in several lines, not of this sentence alone, and the sentence uses the word in the sense its neighbours (L195, L576, L626) use it. C29 (L520) is before its own checker; this ruling proposes nothing for L189, L245, L247 or L520, and records the point for the orchestrator as a matter of the term, not of C18.

## Why not a FIX naming the conditions

Two wordings would write the extent into the sentence:

```
- a **violation** occurs when (F1) or (F2) fails at \((a,b)\);
```

(Mimo, reply line 146, called on reply line 148 "a re-spelling rather than a rival"), and the wide reading written out, which neither reader offered:

```
- a **violation** occurs when (F1), (F2) or (A) fails at \((a,b)\);
```

On the argument above, each changes nothing the passage uses: they are rewordings on this reading, and the sentence is easy to vary in this respect. Under the reading rule, a rewording is taken only if it is clearer. Neither is:

- **Each parts L220 from the word its neighbours use for the same relation**: L195 "a survival condition requiring fidelity on \(H\)", L576 "faithful where it was tested", L626 "the fidelity failure is structural, not parametric". The tie by which surprise (L221) is a failure, outside \(H\), of the relation survival holds on \(H\) would then rest on reading "fidelity" in L195 as the tags in L220, which is the very question the doubt raises. The doubt would move, not go.
- **The wide wording opens, in words, a situation the passage never meets.** A selected transport could be violated at a pair of its own \(H\) by (A) alone while its survival condition, read by L189, is met. On the argument above that situation is empty on the simulation layer, but the wording would invite a reader to look for it, and L223 says nothing of it.
- **Neither is more exact at a pair.** (F2) carries "\tau(1)=1,\quad \tau(a_2a_1)=\tau(a_2)\tau(a_1)" (L242), conditions on \(\tau\) and not at an edit–boundary pair, so "(F2) fails at \((a,b)\)" needs the same reading as "fidelity fails at \((a,b)\)": the instance of the per-pair equations at the pair.

## The readers' points, weighed

Each proposal stands or falls on what it breaks; the number of readers on a side decides nothing.

**"when the prediction fails"** (Mimo, reply line 136) and **"a wrong prediction"** (GLM, reply line 129). A different claim: a violation would be the prediction's contradiction alone. GLM's point holds (reply line 131): "A transport whose answer at $(a,b)$ is right while a component relation is wrong — (F1) failing — is violated on the original and unviolated on this rival." That undoes the work L245 gives (F1): "(F1) prevents an assembled match from hiding a decomposition in error." It also parts violation from the relation survival is tested on (L195) and on which Argument 3 works (L574), so that surprise would no longer be the failure outside \(H\) of what selection held on \(H\) (L576). GLM's "wrong" would also bring back a word the S23 scrub replaced with "in error" (S98 ledger, CH-1187). Two of Mimo's further grounds are not shown: S27 speaks of explanations that "can contradict each other at the level of explanation without ever having to be tested against reality", and a violation is a relation between a transport and its target at an occurring pair, not a conflict between explanations, so defining it by the prediction would make no conflict between explanations need a test; and L582's chain, "no prediction and hence no violation", reads alike on the rival. The break at L245, L195 and L574–L576 is enough.

**"when the transport breaks down"** (Mimo, reply line 141). "Breaks down" names no condition; the sentence would lose the criterion L189 gives and L626 names ("the fidelity failure"). The point holds.

**"when (F1) or (F2) fails"** (Mimo, reply line 146). Weighed above: a rewording on this reading, not clearer, recorded and not taken. Mimo's further claim (reply line 148), that "where it would differ it drops question fidelity (A) at L247–L253, which this sentence's uses attribute to it", is met by the argument above: the uses (L582, L624–L626) lie where (A) at the pair goes with (F2) at it, so nothing they need is dropped.

**"when reality falsifies the prediction"** (GLM, reply line 135). The point holds: decision S23 removes "Anything that could be interpreted as needing verification or falsification in any absolute sense", and the wording puts an unmediated comparison with "reality" in the place of the relation the text defines (L189, L233–L253), against L67's "Faithfulness without assessors".

**"where fidelity fails somewhere in $C$"** (GLM, reply line 141). The point holds: the violation would lose its pair and its event. L221 needs a violation "at \((a,b)\notin H\)", and L582 one "at an occurring \((a,b)\in C\)"; Argument 10's violation is at the occlusion pair.

## This checker's own attempts

- **"when the transport is not faithful at \((a,b)\)"**: `- a **violation** occurs when the transport is not faithful at \((a,b)\);`. A rewording that uses L189's adjective at a pair, as L43 does. Not clearer: L189 defines "faithful" by the same "fidelity conditions", so the doubt moves to L189's "global"; and it parts the sentence from L626's "the fidelity failure". Recorded, not taken.
- **Tying the prediction in**: `- a **violation** occurs when fidelity fails at \((a,b)\), as it does wherever the prediction is contradicted there;`. A different claim: it states in the text the step argued above (a query read through the transport), which the text leaves unstated, and so says more than the passage needs. Not taken.
- **Word order**: `- a **violation** occurs at \((a,b)\) when fidelity fails there;`. A rewording; not clearer. Recorded, not taken.
- **Two named kinds of violation**, one for (F1) or (F2) and one for (A): the text never uses such a distinction, and on the argument above the second kind is empty on the simulation layer. Not taken.

## The owner's decisions

- **S23.** No word or idea S23 removes; "fails" and "violation" name the relation's not being met at a pair, with no assessor and no verdict of truth. The sentence claims only what a violation is; whether one occurred stays a claim that can be in error.
- **S25–S27.** The sentence puts no condition of physical possibility on a question, an account or a conflict. Where the target is physical, a violation is a transport a system holds, an instantiated correspondence, meeting a change; that is where S26 lets physical possibility come in. Where the episode is stipulated, as in Argument 10 (L632: "This episode is a relative-consistency instance for the class."), the violation is stipulated with it.
- **S28.** KEEP settles nothing; this ruling records only that the attempts made broke what each is said above to break.
- **S20, S21.** No list, count, grade or record of rivals does any work here; nothing is said about what happens to a candidate or what the person choosing does.
- **S33–S34 (parked).** No point of either reader proposes anything about what hard to vary covers, and this ruling proposes nothing about it. "Easy to vary" above is meant plainly, as the brief asks. No value is moved in or out.
- **Open proposals left alone.** The S98 ledger holds S95 proposals, open for the owner, to rename "surprise" (CH-1199, CH-1200) and the heading (CH-1201). This ruling does not touch them; the word "violation" stands in each.

## Fixed case verdicts

- **Argument 10** (L618–L632), the worked case the text ties to this sentence: "This is surprise (Argument 4)." (L624) and "the fidelity failure is structural, not parametric" (L626) stand; with KEEP nothing changes. The violation there lies where both readings of "fidelity" agree.
- **Case book O3** (Nadia, who "predicts the next card from the cards just played, and is often surprised"): her surprises are predictions contradicted, violations on either reading; the fixed verdict ("Nadia built something new: a part that stands for cards she has never observed. That is construction, and it is her own.") turns on construction, not on this sentence. Nothing moves.
- **S89 case book, N18** (Rhea's and Dov's footbridges): a candidate case whose verdict is in ordinary words ("the swaying went against what both expected"); the ledger ties it to no line of Part IV; on either reading of "fidelity" the swaying against each design's prediction is a violation. Nothing moves.
- **The S98 ledger** has no row for L220.s1 and ties no case to it.

## What depends on the sentence (nothing changes under KEEP)

- L221: "- **surprise** is a violation of a selected transport at \((a,b)\notin H\)."
- L223: "A system with no transport cannot be surprised." … "Prediction and violation are defined for every transport to the simulation layer, surprise only for a selected one: a constructed one that fails at an actually occurring pair of its contract is violated, and the failure is not surprise; a violation the system represents can be a recognized difficulty (Part X)."
- L225: "Two responses to a violation are distinguished." and the two responses defined after it (C19, C20).
- L576: "It is also why surprise is possible."
- L580–L584: Argument 4, its claim, its reasons (L582: "Surprise is defined (Part IV) as a violation of a selected transport at an occurring \((a,b)\in C\) with \((a,b)\notin H\). If there is no transport there is no prediction and hence no violation.") and its consequence.
- L624–L626: Argument 10's violation, surprise and "the fidelity failure".

## Result

- **Ruling:** KEEP.
- **old = new** (L220): `- a **violation** occurs when fidelity fails at \((a,b)\);`
- **The doubt:** real as a matter of the term "fidelity" across L189, L245, L247, L520 and L630; no defect of this sentence, since on the simulation layer (A) at a pair goes with (F2) at it for predictions read through the transport, and every use of the sentence (L223, L225, L582, L624–L626) lies where the narrow and wide readings agree. Recorded for the orchestrator as a matter of the term, not of C18; nothing proposed for those lines here.
- **Easy to vary?** No reader closed VARIES. Mimo's "(F1) or (F2) fails" (reply line 146), the wide re-spelling "(F1), (F2) or (A) fails", and this checker's "is not faithful at" and reordered wording are rewordings that change nothing the passage uses; none is clearer, each parts the sentence from the word L195, L576 and L626 use for the same relation, so each is recorded, not taken. Every wording that changes the claim (the prediction alone, "breaks down", "reality falsifies", "somewhere in \(C\)") breaks a line named above.
- **Parked (S34):** nothing.
- **Recorded:** held under both readers' attempts and this checker's; not thereby final.
