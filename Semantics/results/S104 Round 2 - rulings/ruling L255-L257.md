# S104 Round 2 - ruling L255-L257

*Written by a fresh checker (Opus 5.5) of round 2 (log S104) on 28 September 2026, for one group, L255-L257. This checker built nothing of this round and rules on no other group. It rules under the reading rule (`results/S104 Round 2 - how the replies will be read, written before sending.md`, rules 3 to 12), its two addenda (the external cross-examination; the creative transport case) and the grouping record. No theory text, reading rule, addendum, grouping record, tabulation, brief, reply or committed maths file was written, and nothing in `authority/` was written. This file obeys decision S23 except where it quotes the text, a reply, a brief, the external document or the owner.*

## The group

- **Lines:** L255 (**Non-circular dependence**) and L257 (**Non-vacuity**) of `tests/103 The semantics, standing alone, after round 1.md` (md5 f31ebb1f050783f1a84f6136cec20fcd, checked before reading).
- **Primary items (20):** D3.5, D6.3, D6.4, D6.5, D6.6, D6.9, FC01, FC21, FC23, FC26, I22, I24, I25, I26, I27, I28, I79, I83, U6, E19.
- **Shared items:** FC34 (L255 here; its other line is L151), I03 (L255 here; its other lines are L103, L339). This ruling weighs their points on L255 only and does not say what they come to.
- **Context items:** none. **Parts:** 1, 4, 6, 7, 8.

## What was read

- The reading rule and both addenda, whole; the grouping record (`.md` and the `.json` entry "L255-L257").
- The text around both lines and every definition they use: L85-L161, L189, L231-L281, L287-L317, L325-L343, L369, L375-L397, L516-L528.
- The tabulation's rows for every item (part 1: FC01, I03; part 4: D3.5, FC34, I27, I79, U6; part 6; part 7; part 8: D6.3, D6.4, I03; section 3: E13, E19).
- The replies, `.response.txt` only: `s104_maths_mimo_4`, `_6`, `_7` and `s104_maths_glm_4`, `_6`, `_7` whole; every passage of the other 28 replies that names one of the items or L255 or L257 (found by searching all 34 for the ids and the two line numbers): `s104_maths_mimo_1` (lines 42, 52, 60, 82), `_8` (lines 5, 7), `_11` (lines 31, 45), `_12` (line 65), `_17` (line 99); `s104_maths_glm_1` (lines 27, 37, 49-53, 63, 75), `_8` (lines 5-11, 23, 27), `_11` (lines 35, 45, 49).
- The briefs of parts 1, 4, 6 and 7 (sections 3 to 6) and part 8 (its D6.3 and D6.4).
- The maths: formal core §3 (D3.5), §6 and §18; formal claims FC01, FC21, FC23, FC26, FC34; register entries I03, I22, I24, I25, I26, I27, I28, I79, I83, I85; the check of the program §2 (FC23 (b)), §4.4, §4.5 and §5; the check of the formalization §1 (H10), §2 (T01-T15 and 2b), §3 (R01-R25), §4, §5 and §6.
- The external document, section 5 whole (saved file lines 426-443; E19 is lines 433-434), and the items file entry E19; E13's tabulation row, since the tabulation names it on the same sentence as D3.5.
- The round-1 critical review (C29 at L520 and matter 7 at L273 touch these lines by pointer only; no round-1 matter or change is an item of this group).
- Decisions S20, S21, S23, S25 to S28, S33, S34, S36 and S37 in `records/Semantics - Decisions.md`.

## What was run

- `python3 -m model.run --claim FC21 --scale 4 --time-cap 45` and the same for FC26, from `results/S104 Round 2 - maths`: the same results as the record (FC21 (b) witness found; FC26 computed as claimed on C1 and C2, and the look on C3 not as expected).
- A scratch script on `model/core.py` unchanged (Appendix A), building thirteen models. Their results are cited below as M1 to M13:

| # | model | who gave it | result on the program |
|---|---|---|---|
| M1 | the decorated lookup: k on (p0, p2) fixes p0 to the target's answer and p2 to 0 | GLM, part 6, reply lines 75-92 | Acc holds; no component is a slot |
| M2 | a copy of a target undetermined (empty) at e1; k restates the answer where it is determined | Mimo, part 6, reply lines 102-112 | Acc holds; no slot (I83) |
| M3 | one component k on (p0, p1) fixing both ports | Mimo, part 6, reply lines 114-124 | Acc holds; no slot |
| M4 | m full at the baseline and {L = 2} at e; n {L = 1} at the baseline and full at e | GLM, part 7, reply line 107 | no subnetwork of D, with either port translation, gives m's or n's relations: (F1) fails; Acc fails |
| M5 | a target whose answer is fixed at each pair by one component, a different one at each pair (a free edit e); E = D | this checker | Acc holds under the maths (every-pair slot test) |
| M6 | a contract of relabelings (answer 0 at both pairs); a candidate with τ(1) ≠ 1 | this checker | (A), NC1 and NC2 hold; Hom, so (F2), fails |
| M7 | an edit exchanging two components' values; E = D | Mimo, part 7, reply line 69 | (A) and NC2 hold; NC1 fails (c0 is a slot); Acc fails |
| M8 | an edit renaming the values 0 and 1 of every port, with the answer carried through c_p: p0 = q; E = D | this checker | Acc holds on a contract whose only edit is that renaming |
| M9 | a contract whose only edit is the identity, over two boundaries with different answers; E = D | this checker | Acc holds |
| M10 | the forward pole on C1 (settings of H and θ at b = (1, 45°)) | the record's E1 | Acc holds; the block Γ = {c_H, c_T, c_L} fixes L to the target's answer at every pair; no single component does |
| M11 | Mimo's non-copy model for FC34 (c: y = x, x = 1 at b1, x free at b0; E with c′) | Mimo, part 4, reply line 68 | with baseline b0: NC2 fails (and (A) fails if c′ is y = 1 at b0); with baseline b1 and c′ full at b0: Acc holds |
| M12 | FC21 (b) with two determined answers that differ: E answers 1 and 0 on a contract where the target answers 1 at both pairs | this checker | NC1 and NC2 hold; (A) fails |
| M13 | a question whose baseline answer is undetermined and whose edit fixes it; E = D, Γ = {c_y} | this checker | (F1), (F2), (A), NC1 hold; NC2 fails (D6.4 asks a determined baseline) |

- A scratch random search (Appendix B) on the program's own generators (both families, sizes up to three ports): for the relabeling sentence as fixed below, 309,046 models with τ(1) = 1 and (A) on a contract at whose every pair the target's answer is its baseline answer, 126,102 of them with the baseline answer undetermined; NC2 held in none.
- A quotation check by program: the 36 quotations of the text this ruling relies on were each found in the line it names (each once in that line).

---

## L255

> L255 | **Non-circular dependence.** The answer follows by evaluating \(E\) under its independent boundary conditions. The target's answer does not appear, at the declared grain, as an unanalysed boundary input or as a component; moving an assertion from an input slot into a component named "law" does not discharge this. Identity of that assertion with the target's answer is structural at the declared grain, not the indiscriminate identification of all logically equivalent mathematical statements. There exist \((a,b)\in C\) and a nonempty block \(G\subseteq\Gamma\) such that the answer of \(E\) at \((\tau(a),\sigma(b))\) differs from its answer at \((1,\sigma(b_0))\), or is not determined at \((\tau(a),\sigma(b))\) in the claimed way, and this contrast is lost when the components of \(G\) are deleted from \(E\) (a deleted component imposes the full relation on its ports, Part II): evaluated at \((\tau(a),\sigma(b))\) and at \((1,\sigma(b_0))\), the answers of \(E\) with \(G\) deleted are determined and equal, or an answer that \(E\) determines at one of these points is not determined there once \(G\) is deleted.

Four sentences: (1) the answer follows by evaluating \(E\) (NC0 in the maths); (2) and (3) the answer does not appear as a boundary input or a component, read structurally (NC1); (4) the contrast lost under deletion (NC2).

### Sentence 1 (NC0)

No point challenges it. D6.2, I23 and FC108 went to no checker: both readers read the sentence as a gloss, since a condition on how an answer is computed would need a notion of computation that (O) and (Q) do not give (Mimo part 6, reply line 76; GLM part 6, reply lines 5 and 51). **KEEP.**

### Sentences 2 and 3 (NC1)

**Challenge 1: the reach of "as a component" (D6.3, I24, FC23; E19).**
- *GLM* (part 6, reply lines 7 and 53; part 8, reply line 5): the maths and the words part: I24 bars only a component whose relation is exactly the answer "and constrains nothing else", while the words bar the answer's appearing as a component; "moving an assertion from an input slot into a component named 'law' does not discharge this" closes the decoration escape that I24 opens. The words stand; the maths should move to I24's alternative (b). No text change. Model M1.
- *Mimo* (part 6, reply lines 7, 78-86): "unanalysed", "at the declared grain" and "structural" have no definition in (O) or (Q); two candidates that restate the answer meet the maths' NC1 (M2, M3). The words stand; the test should be written into the text: proposal M6-B6 adds "The answer appears as a component when the relations of one component, or of a block of components, fix the answer ports of \(E\) to the target's answer at every pair of \(C\) at which that answer is determined; what else those relations constrain does not discharge this." Mimo part 8 (reply line 5): the words should stand; no proposal.
- *Checked:* M1, M2 and M3 meet (E) on the program as the maths is registered.
- *Ruling on the arguments.* Both readers hold that the words stand, and that holds: the words already exclude M1 and M3. L255 bars the answer's appearing "as a component" with no restriction to a component that constrains nothing else, and the text reads that identity elsewhere in so many words: L397 counts a premise that is a claim's denial "alone or joined to other claims by "and", read structurally as non-circular dependence reads identity (Part V) and not by logical equivalence alone". A component whose relation asserts the answer joined by "and" to a second constraint is, on that reading, the answer appearing. L273 says the same of a candidate: "So does an account whose only substantive component restates the answer it was asked for", and M1's k and M3's k restate it. So I24's "and constrains nothing else" is the maths' narrowing, not the text's; M1 and M3 are counterexamples to that way of writing the text (rule 6), and the maths should change. M6-B6 is not applied: its "or of a block of components" makes joint determination an appearance. On the forward pole (M10) the block of all three commitments fixes L to the target's answer at every pair of C1 while no single component does, so M6-B6 would fail the text's own production example on NC1, and with it every candidate whose commitments together fix the answer, which is what an account's commitments do. That is the "indiscriminate identification of all logically equivalent mathematical statements" that sentence 3 excludes. The "law" clause Mimo relies on concerns one assertion moved into one component, not a block.

**Challenge 2: pairs at which the target's answer is undetermined (I83, U6; FC34 shared).**
- *Mimo* (part 6, reply line 96): under I83 a lookup that restates the answer wherever there is one meets (E) (M2); I83's alternative, the slot asked at the pairs where the answer is determined, is what L273 needs; M6-B6 writes it in.
- *GLM* (part 6, reply lines 63-65): "does not appear" is silent where there is no answer; I83 is the mildest choice and can stay, recorded; if the text is to speak, G6-B7: "Where the target's answer is not determined at a pair of \(C\), nothing is asked to appear there." *GLM* (part 4, reply lines 108-117, under U6): the text should say that a component fixing the answer wherever it is determined is the answer's appearing; G4-B8: "The target's answer does not appear, at the declared grain, as an unanalysed boundary input or as a component: a component that fixes the answer wherever the answer is determined is that appearance, undetermined pairs notwithstanding." It adopts I83's other choice and says so.
- *Ruling on the arguments.* "Does not appear" has no clause that excuses a component restating the answer at every pair where the answer is determined because at some other pair of \(C\) the answer is not determined; the excuse is I83's, a choice of the program (its register entry gives its source as `model/`), and L273's "restates the answer it was asked for" reaches M2's k. So the text gives I83 no ground, and the maths should move to I83's alternative (b); the check re-ran the whole suite under that alternative and no claim or part changed status (check of the program, §5). G6-B7 is not applied: read with the maths' every-pair slot test it removes the undetermined pairs from the test, which is I83's alternative (b) and not I83 as GLM says, so its effect depends on a test the text does not state; and GLM's own reason for it ("can stay, recorded") asks for no text change. G4-B8 is not applied: on the two points it makes it says what the words already hold (above), and as worded ("is that appearance") it defines the appearance by the every-determined-pair form, settling the quantifier of challenge 3, which the text leaves open; as a replacement of the whole of L255, as tabulated, it would also drop the "law" clause.

**Challenge 3: at every pair of \(C\), or at some pair (D6.3, FC26; the check's R08).**
- *Mimo* (part 7, reply lines 9-13): the maths should stand: a pair-by-pair reading "would fail every faithful decomposition under an intervention on the answer port, since that intervention replaces the very component the answer flows through"; M7-B2 writes into sentence 3: "— a component whose relation is the answer at every pair of the contract, not one an intervention replaces at a single pair —".
- *GLM* (part 7, reply lines 12, 57-62 and 107): "at every (a,b) ∈ C" is a choice no entry records; a component that is the answer at some pairs and not at the baseline escapes NC1 (hand model M4); GLM recommends the some-pair reading with an exemption for a component the contract's own edit replaces, G7-B5: "The target's answer does not appear, at the declared grain, as an unanalysed boundary input or as a component at any pair of the contract, save that a component the contract's own edit replaces at a pair is not, at that pair, the answer's appearing, the value there being the edit's, an edit the target admits as well; moving an assertion from an input slot into a component named "law" does not discharge this."
- *Checked:* M4 does not meet (E): no subnetwork of its target, under either port translation, has m's relations (full at the baseline, {L = 2} at e) or n's, so (F1) fails for both (program). GLM's point survives it in another model: M5, a target whose answer is fixed at each pair by one component, a different one at each pair, and its copy, meets (E) under the every-pair test (program); the check's second FC34 witness under I83's alternative is of the same kind (check of the program, §5: "two components each fix the answer at one boundary, so neither is a slot").
- *Ruling on the arguments.* Mimo's argument against a pair-by-pair reading is met by GLM's exemption, not by the every-pair form; GLM's argument against the every-pair form stands on M5, not on M4. But neither reading is in the words: "does not appear" carries no quantifier over the pairs of \(C\), and the forward organization, which a pair-by-pair reading without the exemption would exclude on a contract holding settings of \(L\), is said at L325 to be "faithful under this contract", not to meet (E). M7-B2 is not applied: it writes in the every-pair form and, with "whose relation is the answer", the exact slot that challenge 1 found the text excludes. G7-B5 is not applied now: its exemption rests on "a component the contract's own edit replaces", which the text gives for setting edits (L103) while "A changed rule is a changed component" (L103) leaves an edit that changes several relations, as in M5, unplaced; the reading has not been run on the program; and with challenges 1 and 2 and with I79 (challenge 4, an owner question) it would fix how NC1 treats a component that reads boundary values carried inside it (the pole's reversed calculation, whose c'_L, `r_L` in `model/cases.py`, is "L = the observed value u_H·cot u_θ (from the boundary)"). The text should not now settle the quantifier; the choice is recorded below as an invention the register lacks, and the maths should run the three readings (every pair; every determined pair; some pair with the exemption) before any wording is proposed.

**Challenge 4: boundary inputs (I79). OWNER QUESTION (marked).** Mimo (part 4, reply line 91) reads "as an unanalysed boundary input or as a component" as separating the two, so the words carry I79's other choice, and proposes nothing, calling where values sit the owner's question. GLM (part 6, reply line 67) holds I79 licensed by the "law" clause ("the two routes name one failure"), and (part 4, reply line 102) that it should stay open with NC1's dependence on it recorded. Recorded under the owner questions below. The present wording names both routes and says that moving an assertion from one to the other does not discharge the condition; it says nothing about where boundary values sit, which is as the owner's words leave it.

**Challenge 5: the grain (I28).** Mimo (part 6, reply line 90): not fixed, stay open. GLM (part 6, reply line 57): settled in effect, since the declared indices are "stated, not defined" (L526). The text makes the grain a declared index ("Grain \(\ell\), boundary \(\beta\), continuity \(\Omega\), and the contract \(C\) are declared indices.", L524; L31), which is I28's reading; it defines no map between grains and L255 asks for none. No text change is proposed by either reader.

**Challenge 6: E19 (the external reader, document lines 433-434).** "Encoded variants require a more exact account of structural answer-identity at the declared grain before they can be adjudicated. I would call that an unresolved formalization obligation, not an exhibited counterexample." The finding holds as an open obligation: the text gives no exact test of structural answer-identity. What this round adds: the words already exclude the plain lookup (FC23 (a) held), the decorated lookup (M1, M3) and the lookup sheltered by an undetermined pair (M2), which the maths' present test lets through; whether a component that asserts the answer at single pairs (M5), a law reading boundary values carried inside a component (I79), or an answer hidden in a transport's value maps (FC20, I81) is an appearance, the text leaves open. The document gives no wording, and the readers' wordings either overshoot (M6-B6) or settle an open choice that has not been run (M7-B2, G4-B8, G7-B5). No line changes on it; recorded.

### Sentence 4 (NC2)

**Challenge a: "in the claimed way" (I22).** Mimo (part 6, reply lines 66-74): no referent; with I21, (A) makes the candidate's undeterminacy the target's own, so the phrase adds nothing inside (E); M6-B5 rewrites the contrast as "are two values that differ, or the answer of \(E\) at \((\tau(a),\sigma(b))\) is undetermined while its answer at \((1,\sigma(b_0))\) is a value". GLM (part 6, reply lines 47-49): no antecedent in (O) or (Q); G6-B6: "or is not determined at \((\tau(a),\sigma(b))\) while it is determined at \((1,\sigma(b_0))\)". *Ruling.* The phrase has a reading in the text's own terms: "A candidate offered for \(p\) is offered for the whole of \(p\): it claims (F1), (F2) and (A) at every pair of \(C\)" (L315), so the claimed way at a pair is the target's own answer there, as (A) claims it; that is I22's reading. Inside (E) it adds nothing to (A), as Mimo says, and does no harm. A claimed way of being undetermined that a single undetermined answer cannot carry (I22's alternative (a), "which values remain") can be put in the query, which may be any "specified set-theoretic operation on \(D\), its solutions and its component structure" (L141). Each of the offered wordings also settles challenge b (M6-B5 and G6-B6 by asking a determined baseline for the second disjunct and so reading "differs" as between two values, since otherwise the second disjunct would repeat the first; G7-B2 directly). None is applied.

**Challenge b: a value against an undetermined answer at the baseline (D6.4, I22). OWNER QUESTION (marked).** GLM part 8 (reply lines 7-11) finds the maths faithful "including the asymmetry" and says "Whether the words want that asymmetry is the owner's", giving the symmetric G8-B1 ("or is not determined at one of these points in the claimed way while determined at the other") and proposing nothing until the owner says. GLM part 7 (reply lines 14-19) would write the asymmetric reading in (G7-B2). Mimo part 6 (reply line 5) notes that "differs", with undetermined answers equal only to themselves, also covers a value at the edited point against an undetermined baseline, which the maths counts nowhere; Mimo part 7 (reply line 15) says the gap "admits no model". Recorded with both sides under the owner questions below. On the facts: the gap does admit models (M13: a baseline with several solutions, an edit that fixes the answer; under D6.4 no candidate meeting (A) meets NC2 on that contract, under the symmetric reading E = D does). The present wording leaves the matter open (its second disjunct names the edited point; its "differs" is not said to hold only between values), which is as the owner's words leave it. **KEEP** on this point.

**Challenge c: may \(G\) be the whole of \(\Gamma\)? (D6.4). OWNER QUESTION (marked).** GLM (part 6, reply lines 9 and 94): the maths reads "block" as any nonempty subset with no recorded choice; with \(G=\Gamma\) NC2 asks little; G6-B1 adds "\(G\neq\Gamma\)" "if the owner wants a proper part deleted (this writes content in; the owner decides)". The text states the matter: "a nonempty block \(G\subseteq\Gamma\)" (L255), and blocks are nonempty subsets where the text defines them ("For nonempty \(B\subseteq W\),", L293, with \(B = W\) allowed by (B)). With \(G=\Gamma\) NC2 still asks that the contrast be lost when the commitments go, which fails whenever background components alone carry it. G6-B1 would fail NC2 for every candidate with one commitment, since a singleton has no nonempty proper subset. Recorded below; **KEEP** on this point.

**Challenge d: what deletion does (I03, shared).** GLM part 7 (reply lines 84-89) says "The text never says what deletion does" and proposes G7-B8: "Deleting a component removes its constraint and changes nothing else in \(E\)." The premise is not found: L255 itself carries "(a deleted component imposes the full relation on its ports, Part II)", as L103 does ("A deleted component imposes the full relation on its ports."); "the components of \(G\) are deleted from \(E\)" deletes those and no others. G7-B8 adds nothing the line lacks. **KEEP** on this point.

**Challenge e: FC01's look (GLM part 1, reply lines 27 and 75).** The look found that deleting a component with an empty relation can make an undetermined answer determined; GLM says it bears on NC2's wording. The loss clause names that case in its first disjunct ("the answers of \(E\) with \(G\) deleted are determined and equal"); where the newly determined answer differs from the baseline's, the contrast is not lost, as the words say. The look turns on I21's merging of "none" and "several" into one undetermined answer (check of the formalization, §5), not on L255.

### Ruling on L255: **KEEP** (all four sentences)

No point shows a sentence of L255 saying something it should not. The departures found are the maths' (I24's "and constrains nothing else", I83, and the every-pair quantifier the register does not list with alternatives); the first two are excluded by the text's own words (L255 read with L273 and L397), and the maths should change and re-run; the third, the reading of the contrast when an answer is undetermined, and I79 stay open, the last two as owner questions. No wording offered for L255 (M6-B5, M6-B6, M7-B2, G4-B8, G6-B1, G6-B6, G6-B7, G7-B2, G7-B5, G7-B8, G8-B1) is applied, for the reasons given under each challenge.

---

## L257

> L257 | **Non-vacuity.** \(\operatorname{Sol}_D(1,b_0)\neq\varnothing\). The contract \(C\) is a stated subset of the edits the target admits, and every edit the target admits that is excluded from \(C\) is excluded by a stated scope, not silently. A contract consisting only of relabelings, or excluding every change under which the active commitments could matter to \(\mathcal Q\), admits no candidate that meets non-circular dependence, and is therefore not a contract on which an account can be claimed.

### Sentence 1

No point challenges it. **KEEP.**

### Sentence 2: the stated scope (D3.5, I27, D6.6; FC26)

- *Mimo* (part 4, reply lines 25-31 and 81): L141 writes \(C\) as edit-boundary pairs, L257 as "edits"; the pair reading stands, "because the scope clause is checkable only against the same items C omits"; M4-B3: "The contract \(C\) is a stated subset of the edit–boundary pairs the target admits, and every pair the target admits that is excluded from \(C\) is excluded by a stated scope, not silently. The pairs the target admits are all \((a,b)\) of its edits and boundaries."
- *GLM* (part 4, reply lines 19 and 57-64): "The text contradicts itself here; the maths follows L141"; G4-B4: "The contract \(C\) is a stated subset of the admitted edit–boundary pairs, and every admitted pair excluded from \(C\) is excluded by a stated scope, not silently."
- *GLM* (part 7, reply lines 21 and 107): "excluded by a stated scope, not silently" does not say where the scope is stated or by whom; under I85 the clause is never at risk in a search. No wording.
- *The check of the formalization* (§2b) reads the text's word "edit" as pointing to I27's other choice (edits, not pairs), with no search result changed.
- *Ruling on the arguments.* The sentence as written makes a set of pairs a subset of a set of edits: "The **contract** \(C\subseteq A\times B\) is the set of admitted edit–boundary pairs the claim ranges over" (L141). On the edit reading, a contract could leave out an edit at some boundaries while keeping it at others, or leave out every boundary but one, with nothing stated, since only an edit with no pair in \(C\) would need naming. That is the quiet exclusion the text says the clause catches: "A contract that quietly excludes changes its target admits to protect an account is not caught by a rule about intentions; it is caught by the requirement that the exclusion be stated (non-vacuity, Part V)" (L43), where the changes a contract holds are its pairs (L141; "the changes in \(C\)", L265), and "A contract is a stated subset of the changes its target admits (Part II), and a stated scope is what makes it one." (L159). So the text's other lines require the pair reading, and the check's literal reading of "edit" at L257 conflicts with L141. The text should now settle I27 as pairs. The smallest wording is Mimo's first sentence, which changes only the two words that carry the edit reading and keeps "the target admits". Mimo's second sentence is not taken: the target's admitted edits \(A\) and boundaries \(B\) are given at L91 and \(C\subseteq A\times B\) at L141, so it repeats them. GLM's wording drops "the target", which the sentence uses to say whose admitted pairs these are. GLM's "where or by whom" is answered by the text: "the scope of a contract and why the question asked is answered on that restriction and not on a wider one (Part III)" is among the declared inputs (L522), and "the scope a claim states for its contract, are values of indices and are declared inputs (above)" (L524); I85, the search's default statement, stays a search device, as both readers say (Mimo part 4, reply line 93; GLM part 4, reply line 104). I27's other choice (b), a yes-or-no flag, is excluded by the words kept: every excluded pair "is excluded by a stated scope", which a flag naming no pair cannot do (Mimo part 4, reply line 81).

### Sentence 3: relabelings (D6.9, FC21, I26)

- *Mimo* (part 6, reply lines 21-29): with "relabeling" read on the target's answer, a candidate meeting (A) answers constantly and NC2 has nothing to hold on, but a candidate not meeting (A) can answer differently at two relabelings; M6-B2: "admits no candidate that meets (A) and non-circular dependence". *Mimo* (part 7, reply lines 19, 35-39, 59, 69): FC21 (b)'s witness is a counterexample to L257 read literally; under I26's automorphism reading a candidate meeting (A) can meet NC2 (M7); M7-B3 adds "— edits under which the target's answer to \(\mathcal Q\) does not change —" and "(A) and", writing I26 in.
- *GLM* (part 7, reply lines 23, 27, 50-55, 68-73, 101): FC21 (b)'s witness refutes the sentence under any reading of "relabeling", since NC2 concerns the candidate's own answers; the sentence must demand agreement; G7-B4: "admits no candidate that answers as the target does and meets non-circular dependence"; and, since "relabeling" occurs once, undefined, G7-B6 adds "A relabeling is an edit \(a\) such that at every pair \((a,b)\) of the contract the target's answer to \(\mathcal Q\) is determined and equal to its answer at the baseline pair."
- *The check of the formalization* (§5): FC21 is "less": "(a) adds the hypothesis (A), which L257 does not have; (b) is a witness that L257's 'admits no candidate that meets non-circular dependence' fails as written for candidates failing (A)".
- *Checked.* The record's FC21 (b) witness reran. M12 gives another with two determined answers that differ, so the failure does not turn on the undetermined answer of the record's witness. M6 shows that (A) alone is not enough: with τ(1) ≠ 1, a candidate meets (A), NC1 and NC2 on a contract of relabelings, because NC2 compares with \(E\)'s own identity edit, "\((1,\sigma(b_0))\)", which (A) does not reach unless "\tau(1)=1" (L242, part of (F2)). M8 and M9 show that under I26's two other choices the sentence fails even for candidates meeting all of (E): an edit that renames the values of every port changes the answer the fixed query reads (M8), and an edit that changes no relation of \(D\) can sit at a boundary where the answer differs (M9). M7, Mimo's automorphism model, meets (A) and NC2 but fails NC1 (its c0 is a slot), so it does not by itself show a candidate meeting non-circular dependence; M8 does.
- *Ruling on the arguments.* The sentence says something it should not, for reasons that rest on no invention: NC2's contrast is in \(E\)'s own answers (L255), so "admits no candidate that meets non-circular dependence" fails for a candidate that does not answer as the target does (FC21 (b), M12), and, since NC2's baseline point is \(E\)'s identity, for one whose transport does not carry the identity to the identity (M6). Both readers' wordings add (A); neither covers M6, which needs the "\tau(1)=1" of (F2). The conclusion the sentence draws, "not a contract on which an account can be claimed", needs only that no candidate meeting (E) exists, and (E) holds (F2) and (A), so naming them costs the sentence nothing. With them added, the sentence holds only when "relabeling" means an edit under which the target's answer stays as at the baseline: under the automorphism reading and the no-relation-changed reading it fails for candidates meeting all of (E) (M8, M9). That is I26's reading, and it is the one the text's own talk of renaming bears out: two candidates carried one onto the other by "a structure-preserving bijection that takes its transport with it and leaves its answers as they are" (L315). So the text should now settle I26. It does not need I26's "≠ ⊥": where every answer, the baseline's included, is undetermined, (A) and "\tau(1)=1" make \(E\)'s answers all equal to its baseline answer, and no disjunct of the contrast can hold (the search of Appendix B covered 126,102 such models). The gloss goes in brackets beside the word, so the sentence keeps its form; M7-B3's "does not change" is not taken, because it leaves open "compared with what", and read as "compared with the identity edit at the same boundary" it lets the identity edit over two boundaries count as a relabeling, which is M9. G7-B6 is not taken as a separate sentence, since the bracket says the same in fewer words.

### Ruling on L257: **FIX** (sentences 2 and 3; sentence 1 unchanged). Settles I27 and I26.

**Old** (the exact span of L257 replaced, from "The contract" to the end of the line; it occurs once in the line):

```
The contract \(C\) is a stated subset of the edits the target admits, and every edit the target admits that is excluded from \(C\) is excluded by a stated scope, not silently. A contract consisting only of relabelings, or excluding every change under which the active commitments could matter to \(\mathcal Q\), admits no candidate that meets non-circular dependence, and is therefore not a contract on which an account can be claimed.
```

**New:**

```
The contract \(C\) is a stated subset of the edit–boundary pairs the target admits, and every pair the target admits that is excluded from \(C\) is excluded by a stated scope, not silently. A contract consisting only of relabelings (edits at whose pairs in \(C\) the target's answer to \(\mathcal Q\) is its answer at the baseline \((1,b_0)\)), or excluding every change under which the active commitments could matter to \(\mathcal Q\), admits no candidate that meets (F2), (A) and non-circular dependence, and is therefore not a contract on which an account can be claimed.
```

The dash in "edit–boundary" is the en dash of L141, copied from it by program.

**Why this wording and not the text's:** the text's second sentence makes a set of pairs a subset of edits and, read as it stands, leaves unstated the exclusions L43 says the clause catches; its third sentence fails as written for candidates that do not answer as the target does, or whose transport does not keep the identity (FC21 (b), M12, M6), and holds only under one reading of an undefined word (M8, M9). **Why not a reader's:** M4-B3 and G4-B4 as given under sentence 2; M6-B2 and G7-B4 miss M6; M7-B3's gloss leaves the comparison open (M9); G7-B6 needs a sentence of its own and adds "determined", which the sentence does not need.

**What the change says, and what it does not.** Rule 6: it settles I27 (pairs, not edits; the scope a declared statement naming the excluded pairs) and I26 (a relabeling is an edit under which the target's answer at its pairs in \(C\) is the baseline answer; I26's "≠ ⊥" dropped). It adds no condition to (E): non-vacuity's scope clause asks, of pairs, what it asked of edits, and the relabeling sentence names conjuncts (E) already has. Rule 10: no list, count or ranking does work here (S20); nothing is said about what must happen to a candidate (S21); no word S23 forbids is used, and nothing is said to be settled (S28); physical possibility does not enter (S25-S27); nothing concerns what hard to vary covers (S33, S34) or where values are placed.

**Sentences that bear on the changed ones** (none depends on the words removed): L43 ("it is caught by the requirement that the exclusion be stated (non-vacuity, Part V)") reads the same, now matched by pairs; L159 ("a stated scope is what makes it one") unchanged; L343 ("the edits the target admits outside the contract ... are left out by the stated scope") reads as every pair of those edits left out, which is what the Leibniz example states; L275 ("no edit the target admits realizes") unchanged; L520 and L526 name non-vacuity by heading and are unchanged. "Relabeling" occurs nowhere else in the text.

---

## Items: what each comes to (rule 5, second paragraph)

- **D3.5 (scope statement).** The maths (a declared input naming excluded pairs) should stand, and the words change to it: the FIX of L257 settles I27. Its L159 half ("why" as a further declared input) is unchallenged.
- **D6.3 (NC1).** The words should stand. The maths departs from them in two places the text settles against it, I24's "and constrains nothing else" (L255 with L397 and L273; M1, M3) and I83 (L273; M2), and the maths should be rewritten to I24's alternative (b), a component whose relation by itself fixes the answer ports to the target's answer whatever else it constrains, with I83's alternative (b), and re-run. In a third place, the every-pair quantifier, the text leaves the choice open (recorded as an invention below).
- **D6.4 (NC2).** Contrast and Lost say what the words say under I21 and I22 (Mimo part 8, reply line 7; GLM part 8, reply line 7). GLM part 7's point, that Contrast asks a determined baseline where the words say only "differs", is the owner question on the asymmetry; "block" is fixed by the text (\(G\subseteq\Gamma\), L255; L293). The words stand; no line changes.
- **D6.5 (non-circular dependence).** The conjunction NC0 ∧ NC1 ∧ NC2 is what the words say (I25, settled by L273). E19's obligation bears on NC1's exactness, not on the conjunction. Stands.
- **D6.6 (non-vacuity).** Says what the sentence says (both readers). GLM's "where or by whom" is answered by L522 and L524 (the scope is a declared input the claim states). Its sentence changes by the FIX (pairs), which D6.6, through D3.5, already formalizes.
- **D6.9 (relabeling).** The maths' reading, I26, is the one under which L257's sentence holds once (F2) and (A) are named; the words should carry it, and the FIX writes it in without I26's "≠ ⊥". D6.9 should be formalized again without "≠ ⊥".
- **FC01.** A claim that stands: (O) and the deletion sentence give it for any domains (GLM part 1, reply line 75; Mimo part 1, reply line 82). The look's witness tells against nothing in L255: the loss clause's first disjunct names the case; it turns on I21's merging of "none" and "several".
- **FC21.** (a) says what the sentence says only with (A) and τ(1) = 1 in the antecedent, which the sentence lacked. (b)'s witness tells against the text as written, not only against an invention, as do M12 (another witness) and M6 (with (A), τ(1) ≠ 1). Under I26's two other choices the sentence fails even for candidates meeting (E) (M8, M9), so the FIX settles I26 as well. (c) is analytic, as Mimo says (part 7, reply line 19). All three are removed by the FIX.
- **FC23.** The counterexample (b) tells against the claim's own wording ("through NC1 only") and U3's footprint reading, not against the text: the lookup still fails non-circular dependence, and L273 stands (both readers; both checks). The finding it carries, that NC2 alone does not exclude a lookup, stands and is what settles I25. The readers' further models (M1 to M3) meet (E) under the maths and are counterexamples to I24's "and constrains nothing else" and to I83, which the text's words do not carry; FC23 (a) and FC24 should be re-run under I24 (b) and I83 (b).
- **FC26.** The claim stands (computed as claimed on C1 and C2, and rerun here). The look on C3 tells against no sentence: L325 says only that the forward organization is "faithful under this contract". It shows the every-pair quantifier is a choice (R08). GLM's hand model (M4) fails (F1), so it exhibits no candidate meeting (E) with the answer appearing at one pair. The point it aims at stands in M5 and in the check's second FC34 witness, under the every-pair reading, and tells against the text only if the text is read pair by pair, which it leaves open. So L255 is KEEP. GLM's non-vacuity point is answered by L522 and L524; the pair FIX of L257 comes from D3.5 and I27, not from FC26.
- **I22.** The text gives "in the claimed way" a reading in its own terms (L315: a candidate "claims (F1), (F2) and (A) at every pair of \(C\)"), under which I22's reading of the second disjunct is the text's. Whether "differs" reaches a value against an undetermined answer, which decides whether the contrast is asymmetric, the text leaves open; that is the owner question below. Leave open.
- **I24.** The text settles part of it against the invention: "and constrains nothing else" is excluded (L255, L397, L273), so the maths should move to alternative (b), reading "fixes" as a relation whose tuples all carry the target's answer on the answer ports, which is structural in L397's sense, not logical equivalence. Its "structural at the grain: relations of one component of \(E\) as given" is the text's own (sentence 3 with L397), and a block of components is excluded (M10). Its quantifier over pairs is left open by the text (new invention). The text should not now carry a wording.
- **I25.** The text settles it: L273 ("\"\(p\) because \(p\)\" fails non-circular dependence") needs NC1 among the conditions, since under NC2 alone the lookup meets non-circular dependence (FC23; the check's R07; both readers). No change.
- **I26.** The text should now settle it. The FIX writes it in as answer-constancy relative to the baseline, without "≠ ⊥". Its other choices are excluded by M8 and M9 and by L315's "leaves its answers as they are".
- **I27.** The text should now settle it. The FIX writes in pairs, as L141, L159 and L43 require. The scope as a declared statement is the text's (L522, L524), and the flag reading is excluded by "every ... excluded by a stated scope".
- **I28.** The text settles the index part: the grain is a declared index, stated and not defined (L31, L524, L526). No map between grains is defined, and L255 asks for none. Alternative (a) stays open; no change.
- **I79.** An owner question (marked). The present wording states both routes and that moving between them does not discharge the condition; it does not say where boundary values sit, which is as the owner's words leave it. Leave open. The register should record that NC1's verdict on an "unanalysed boundary input", and on any component that reads boundary values carried inside it, turns on I79 (GLM part 4, reply line 102).
- **I83.** Not the text's: the words give no ground for letting an undetermined pair shelter a component that restates the answer wherever it is determined (L255; L273; M2). The maths should move to its alternative (b); no status changed under it (check of the program, §5). No text change.
- **U6.** Its register point stands as a change to the maths' record: I83 runs inside every NC1 and I84 inside every (F2), so every result computing (E) or (F2) should list them (both readers). Its text point (G4-B8) is not applied (challenge 2). The question it raises, whether the target itself counts as an explanation of the target, the text answers by its conditions: a copy is a candidate like any other, and "a mechanism meets (E) or fails it whatever led anyone to guess it" (L277); a table that encodes the response "is an account when it meets the other conjuncts of (E)" (L269). Whether NC1 excludes the two witnesses of record turns, for the first, on I83, which the text gives no ground, and for the second on the open quantifier.
- **E19.** The obligation stands as a finding: the text does not give an exact test of structural answer-identity at the declared grain. It does not say something it should not: it claims no test beyond "structural at the declared grain, not the indiscriminate identification of all logically equivalent mathematical statements". The plain, decorated and undetermined-pair lookups are excluded by the words already (L255 with L273 and L397), though not by the maths. What remains open (M5, I79, value maps in the transport) is recorded, and no line changes. The maths should run the widened test first (decision S36).

## Shared items (their points on L255 only)

- **FC34 (L255 here).** GLM's G4-B8 would change L255; it is not applied (challenge 2). Mimo's non-copy model (part 4, reply line 68) was checked on the program (M11). With the baseline at b0, as its names suggest, NC2 fails (the baseline answer is undetermined, and D6.4 asks a determined one), and with c′ read as y = 1 at b0, (A) fails too. With the baseline at b1 and c′ full at b0 it meets (E) on C, and on C′ = {(1, b1)} c′ is a slot. The mechanism it shows runs through I83 and I79. What FC34 comes to is its primary checker's.
- **I03 (L255 here).** G7-B8 is not applied: L255 already carries I03's deletion half in its parenthesis, and GLM's premise ("The text never says what deletion does") is not found in the text (L103, L255). I03's other halves (fixed ports and components; absent ports) belong to L103 and L339.

## Shared notes (lines not mine; no ruling on them)

- **L273** (FC23, FC24, matter 7): M1 to M3 show the maths' NC1 lets through what L273's second sentence names; the words of L255 and L273 exclude them. Nothing here asks a change of L273; its checker may wish to know that the "holds" of FC23 (a) and FC24 is confined to exact slots until the maths is re-run.
- **L397**: its cross-reference ("read structurally as non-circular dependence reads identity (Part V)") is undisturbed, since L255 is kept, and this ruling relies on it.
- **L151** (FC34): see M11 above.
- **L315 and L317** (H10, R06): the reading of "differs" when one answer is undetermined is recorded here as an owner question for L255; the conflict clause's reading is the L315 checker's. If that checker rules on "differ" at L315, the two rulings should be read side by side (H10).
- **L265** (FC33): after the FIX, non-vacuity's second sentence is a condition on a statement about pairs, not edits; FC33's point about L265 stands as before and is that checker's.
- **L159 and L522** (E13, another checker): the FIX changes "edits" to "edit–boundary pairs" and keeps the stated scope a declared input; E13's procedural point is untouched by it.
- **L343** (not mine): "the edits the target admits outside the contract ... are left out by the stated scope" reads, after the FIX, as every pair of those edits left out; no change there seems needed.
- **L325** (FC26, FC27, FC28): if a later round writes a pair-by-pair NC1, the production contract's holding settings of \(L\) will matter (FC26's look); L325 says only "faithful".

## New inventions (rule 6, last sentence; for the orchestrator's later record)

1. **The quantifier of the answer-slot test.** D6.3 and I24 ask the slot relation "for every (a,b) in C"; the register lists no other choice for it (check of the formalization, R08: "the quantifier is in the entry; no other choice listed"). The unrecorded choices are: (i) the answer's appearing as a component at some pair of \(C\); (ii) at some pair, a component that the contract's own edit replaces at that pair excepted (GLM part 7, reply lines 57-62; G7-B5). A third, every pair at which the target's answer is determined, is I83's alternative (b). M5 separates the every-pair form from (i) and (ii), and FC26's look on C3 separates (i) from (ii). Found by GLM (part 7) and the check.

## Owner questions (rule 9; rule 10; addendum points 8)

1. **NC2's contrast when the baseline answer is undetermined (D6.4, I22; H10, R24).**
   - *For the asymmetric reading* (only undeterminedness at the edited point counts, the baseline determined): GLM part 7 (reply lines 14-19), "a contrast needs two determined ends, and without it a candidate sloppy at the baseline could meet NC2 cheaply"; Mimo part 6 (reply line 74), the asymmetry "follows the deletion clause's 'an answer that \(E\) determines at one of these points'"; the maths (I22); the second disjunct of the words names only the edited point.
   - *For the symmetric reading* (a value at one point against an undetermined answer at the other is a contrast): GLM part 8 (reply lines 7-11, G8-B1), if the owner does not want the asymmetry; Mimo part 6 (reply line 5), "differs" with undetermined answers equal only to themselves covers the case, "the maths counts that case nowhere"; the check (H10, R24), under which L315 reads "differ" so and NC2 can change.
   - *This checker's reading of the arguments* (no ruling): inside (E), (A) ties \(E\)'s baseline answer to the target's, so a candidate cannot be "sloppy at the baseline" there; the deletion clause is symmetric ("at one of these points"), so it gives the asymmetry no ground. Under the asymmetric reading a question whose baseline answer is undetermined and whose edit fixes it admits no candidate meeting NC2 (M13). The present wording leaves the matter open, as the owner's words leave it: KEEP.
2. **Whether the deleted block may be the whole of \(\Gamma\) (D6.4).**
   - *For \(G\neq\Gamma\)*: GLM part 6 (reply lines 9 and 94), with \(G=\Gamma\) and a two-valued answer port NC2 asks only for a contrast on \(C\), and all the bite against lookups lies in NC1.
   - *For the text's \(G\subseteq\Gamma\)*: NC2 with \(G=\Gamma\) still asks that the contrast be lost when the commitments go, which fails where background components alone carry it; blocks are nonempty subsets where the text defines them (L293); and \(G\neq\Gamma\) would fail NC2 for every candidate with one commitment.
   - The present wording states the matter, as the owner's words leave it: KEEP.
3. **Where boundary values sit for NC1 (I79).**
   - *For boundary coordinates of their own*: Mimo part 4 (reply line 91), "L255's 'as an unanalysed boundary input or as a component' separates the two"; the tabulation reads Mimo's "where values sit" as where coordinate values sit.
   - *For the program's collapse*: GLM part 6 (reply line 67), the "law" clause makes the two routes one failure.
   - *For leaving it open with the dependence recorded*: GLM part 4 (reply line 102).
   - What turns on it: whether a component that reads boundary values carried inside it (the reversed calculation's r_L) is an appearance of the answer. The present wording names both routes and says nothing on where values sit: KEEP.

## Parked (decisions S33, S34)

None: no point on these lines concerns what hard to vary covers.

## Formal claims and definitions to formalize again (their sentences change by the FIX of L257)

- **D3.5**: its sentence now says pairs; the formal stays (Excl(Σ) ⊆ A × B).
- **D6.6**: its sentence changes; the formal stays.
- **D6.9**: now the text's reading; drop "≠ ⊥" (a is a relabeling for p when, at every b with (a,b) ∈ C, Ans_p(a,b) = Ans_p(1,b0), with ⊥ = ⊥).
- **FC21**: (a) matches the new sentence with its hypothesis F2_C ∧ A_C (τ(1) = 1 within F2); (b) is no longer against the sentence; add M6 (τ(1) ≠ 1), M8 and M9 as the parts that show why (F2) and I26's reading are needed.
- The register entries **I26** and **I27** become the text's, and I26 loses "≠ ⊥".

Maths changes asked by the item rulings, though no sentence changes for them: D6.3 with I24 (b) and I83 (b); the quantifier's readings (new invention 1); the register's listing of I83 and I84 against every result computing (E) or (F2) (U6); and FC23 (a), FC24, FC26 and FC34 re-run under them.

## Quotations (rule 11)

Every quotation of the text above was compared by program with the line it names and found there (36 quotations; L31, L43, L103, L141, L144, L159, L242, L250, L255, L257, L262, L265, L269, L273, L277, L293, L299, L315, L325, L343, L397, L522, L524, L526). The readers' quotations relied on were checked by the tabulation and found where it says; GLM part 7's premise at reply line 84 ("The text never says what deletion does") is a claim about the text that is not so (L103, L255). The external document's words are quoted from its saved file, lines 433-434.

---

## Appendix A: the models (scratch script, run from `results/S104 Round 2 - maths` against `model/` unchanged)

The script is reproduced below so that M1 to M13 can be rebuilt; it writes nothing.

```python
# Scratch checks for the ruling on L255-L257 (S104 round 2). Uses model/ unchanged.
import sys
sys.path.insert(0, "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths")
from model.core import *

def org(name, ports, dom, comps, foot, B, A, rel, compose=None):
    """rel: dict (j, a, b) -> set of tuples; missing -> full relation."""
    o = None
    def Lfun(j, a, b):
        if (j, a, b) in rel:
            return frozenset(rel[(j, a, b)])
        return o.full(j)
    o = Org(name, ports, dom, comps, foot, B, A, compose or (lambda a2, a1: None), Lfun)
    return o

def T(*ps):
    return {p: Translation([p]) for p in ps}

def report(label, cand):
    val, d = account(cand, detail=True)
    print(label, "Acc =", val, {k: d[k] for k in ("F1", "F2", "A", "NC1", "NC2", "NonVacuous") if k in d},
          "NC2 witness:", NC2(cand, witness=True), "slots:", [k for k in cand.E.comps if slot(cand, k)])

# 1. GLM part 6, the decorated lookup
D = org("D", ["p0", "p2"], {"p0": (0, 1), "p2": (0, 1)}, ["c0", "c2"], {"c0": ["p0"], "c2": ["p2"]},
        ["b0"], [ONE, "e1"], {("c0", ONE, "b0"): {(0,)}, ("c0", "e1", "b0"): {(1,)},
                              ("c2", ONE, "b0"): {(0,)}, ("c2", "e1", "b0"): {(0,)}})
p = Question(D, [(ONE, "b0"), ("e1", "b0")], "b0", PortQuery(), "p0")
E = org("E", ["p0", "p2"], {"p0": (0, 1), "p2": (0, 1)}, ["k", "m"], {"k": ["p0", "p2"], "m": ["p2"]},
        ["b0"], [ONE, "e1"], {("k", ONE, "b0"): {(0, 0)}, ("k", "e1", "b0"): {(1, 0)},
                              ("m", ONE, "b0"): {(0,)}, ("m", "e1", "b0"): {(0,)}})
c = Candidate(E, p, T("p0", "p2"), {ONE: ONE, "e1": "e1"}, {"b0": "b0"},
              {"k": (frozenset(["c0", "c2"]), T("p0", "p2")), "m": (frozenset(["c2"]), T("p2"))}, ["k", "m"], "p0")
report("1 GLM decorated lookup:", c)

# 2. Mimo part 6, lookup under I83 (target undetermined, empty, at e1)
D = org("D", ["p0", "p1"], {"p0": (0, 1), "p1": (0, 1)}, ["c0", "c1"], {"c0": ["p0"], "c1": ["p1"]},
        ["b0"], [ONE, "e1"], {("c0", ONE, "b0"): {(0,)}, ("c1", ONE, "b0"): {(0,)}, ("c1", "e1", "b0"): set()})
p = Question(D, [(ONE, "b0"), ("e1", "b0")], "b0", PortQuery(), "p0")
E = org("E", ["p0", "p1"], {"p0": (0, 1), "p1": (0, 1)}, ["k", "bg"], {"k": ["p0"], "bg": ["p1"]},
        ["b0"], [ONE, "e1"], {("k", ONE, "b0"): {(0,)}, ("bg", ONE, "b0"): {(0,)}, ("bg", "e1", "b0"): set()})
c = Candidate(E, p, T("p0", "p1"), {ONE: ONE, "e1": "e1"}, {"b0": "b0"},
              {"k": (frozenset(["c0"]), T("p0")), "bg": (frozenset(["c1"]), T("p1"))}, ["k"], "p0")
report("2 Mimo lookup under I83:", c)
print("   Ans_p:", p.ans(ONE, "b0"), p.ans("e1", "b0"))

# 3. Mimo part 6, second model: one component fixing p0 and p1
D = org("D", ["p0", "p1"], {"p0": (0, 1), "p1": (0, 1)}, ["c0", "c1"], {"c0": ["p0"], "c1": ["p1"]},
        ["b0"], [ONE, "e1"], {("c0", ONE, "b0"): {(0,)}, ("c0", "e1", "b0"): {(1,)},
                              ("c1", ONE, "b0"): {(0,)}, ("c1", "e1", "b0"): {(1,)}})
p = Question(D, [(ONE, "b0"), ("e1", "b0")], "b0", PortQuery(), "p0")
E = org("E", ["p0", "p1"], {"p0": (0, 1), "p1": (0, 1)}, ["k"], {"k": ["p0", "p1"]},
        ["b0"], [ONE, "e1"], {("k", ONE, "b0"): {(0, 0)}, ("k", "e1", "b0"): {(1, 1)}})
c = Candidate(E, p, T("p0", "p1"), {ONE: ONE, "e1": "e1"}, {"b0": "b0"},
              {"k": (frozenset(["c0", "c1"]), T("p0", "p1"))}, ["k"], "p0")
report("3 Mimo one component on two ports:", c)

# 4. GLM part 7, the per-pair model: m full at baseline, {L=2} at e; n {L=1} at baseline, full at e
D = org("D", ["H", "L"], {"H": (1, 2), "L": (1, 2)}, ["cH", "cL"], {"cH": ["H"], "cL": ["H", "L"]},
        ["b0"], [ONE, "e"], {("cH", ONE, "b0"): {(1,)}, ("cH", "e", "b0"): {(2,)},
                             ("cL", ONE, "b0"): {(1, 1), (2, 2)}, ("cL", "e", "b0"): {(1, 1), (2, 2)}})
p = Question(D, [(ONE, "b0"), ("e", "b0")], "b0", PortQuery(), "L")
E = org("E", ["L"], {"L": (1, 2)}, ["m", "n"], {"m": ["L"], "n": ["L"]},
        ["b0"], [ONE, "e"], {("m", "e", "b0"): {(2,)}, ("n", ONE, "b0"): {(1,)}})
best = None
import itertools as it
subs = [frozenset(s) for s in powerset(D.comps)]
found = []
for Nm in subs:
    for Nn in subs:
        for um in ("H", "L"):
            for un in ("H", "L"):
                lam = {"m": (Nm, {"L": Translation([um])}), "n": (Nn, {"L": Translation([un])})}
                c = Candidate(E, p, {"L": Translation(["L"])}, {ONE: ONE, "e": "e"}, {"b0": "b0"}, lam, ["m", "n"], "L")
                if F1(c):
                    found.append((Nm, Nn, um, un))
print("4 GLM per-pair model: counterparts making (F1) hold (identity value maps):", found)
c = Candidate(E, p, {"L": Translation(["L"])}, {ONE: ONE, "e": "e"}, {"b0": "b0"},
              {"m": (frozenset(["cL"]), {"L": Translation(["L"])}), "n": (frozenset(["cH", "cL"]), {"L": Translation(["L"])})}, ["m", "n"], "L")
report("4 GLM per-pair model with λ(m)={cL}, λ(n)={cH,cL}:", c)
print("   A:", A(c), "F2:", F2(c), "NC1:", NC1(c), "NC2:", NC2(c, witness=True))

# 5. My free-edit model: a target whose answer is fixed at each pair by one component, a different one at each pair
D = org("D", ["y"], {"y": (1, 2)}, ["ca", "cb"], {"ca": ["y"], "cb": ["y"]},
        ["b0"], [ONE, "e"], {("ca", "e", "b0"): {(2,)}, ("cb", ONE, "b0"): {(1,)}})
p = Question(D, [(ONE, "b0"), ("e", "b0")], "b0", PortQuery(), "y")
c = Candidate(D, p, T("y"), {ONE: ONE, "e": "e"}, {"b0": "b0"},
              {"ca": (frozenset(["ca"]), T("y")), "cb": (frozenset(["cb"]), T("y"))}, ["ca", "cb"], "y")
report("5 copy of a target whose answer is asserted by one component at each pair:", c)

# 6. My relabeling model with τ(1) ≠ 1: (A) and non-circular dependence met, (F2) not
D = org("D", ["y"], {"y": (0, 1)}, ["c"], {"c": ["y"]}, ["b0"], [ONE, "a"],
        {("c", ONE, "b0"): {(0,)}, ("c", "a", "b0"): {(0,)}})
p = Question(D, [(ONE, "b0"), ("a", "b0")], "b0", PortQuery(), "y")
print("6 Ans_p:", p.ans(ONE, "b0"), p.ans("a", "b0"), "(every pair has the baseline answer: a contract of relabelings under I26)")
E = org("E", ["y", "z"], {"y": (0, 1), "z": (0, 1)}, ["k", "m"], {"k": ["y", "z"], "m": ["z"]},
        ["b0"], [ONE, "e1", "e2"], {("k", ONE, "b0"): {(0, 0), (1, 1)}, ("k", "e1", "b0"): {(0, 0), (1, 1)},
                                    ("k", "e2", "b0"): {(0, 0), (1, 1)},
                                    ("m", ONE, "b0"): {(1,)}, ("m", "e1", "b0"): {(0,)}, ("m", "e2", "b0"): {(0,)}})
c = Candidate(E, p, {"y": Translation(["y"]), "z": Translation(["y"])}, {ONE: "e1", "a": "e2"}, {"b0": "b0"},
              {"k": (frozenset(["c"]), {"y": Translation(["y"]), "z": Translation(["y"])}), "m": (frozenset(["c"]), {"z": Translation(["y"])})},
              ["k", "m"], "y")
print("6 τ(1) ≠ 1 candidate: A =", A(c), "NC1 =", NC1(c), "NC2 =", NC2(c, witness=True), "Hom (τ(1)=1 part of F2) =", hom(c), "F2 =", F2(c))

# 7. Mimo part 7, FC21 under I26's automorphism reading
D = org("D", ["p0", "p1"], {"p0": (0, 1), "p1": (0, 1)}, ["c0", "c1"], {"c0": ["p0"], "c1": ["p1"]},
        ["b0"], [ONE, "a"], {("c0", ONE, "b0"): {(0,)}, ("c1", ONE, "b0"): {(1,)},
                             ("c0", "a", "b0"): {(1,)}, ("c1", "a", "b0"): {(0,)}})
p = Question(D, [(ONE, "b0"), ("a", "b0")], "b0", PortQuery(), "p0")
c = Candidate(D, p, T("p0", "p1"), {ONE: ONE, "a": "a"}, {"b0": "b0"},
              {"c0": (frozenset(["c0"]), T("p0")), "c1": (frozenset(["c1"]), T("p1"))}, ["c0", "c1"], "p0")
report("7 Mimo automorphism relabeling, E = D:", c)

# 8. An automorphism-type relabeling under which a candidate meets (E), (F2) included
D = org("D", ["p0", "q"], {"p0": (0, 1), "q": (0, 1)}, ["cq", "cp"], {"cq": ["q"], "cp": ["p0", "q"]},
        ["b0"], [ONE, "a"], {("cq", ONE, "b0"): {(0,)}, ("cq", "a", "b0"): {(1,)},
                             ("cp", ONE, "b0"): {(0, 0), (1, 1)}, ("cp", "a", "b0"): {(0, 0), (1, 1)}})
p = Question(D, [(ONE, "b0"), ("a", "b0")], "b0", PortQuery(), "p0")
c = Candidate(D, p, T("p0", "q"), {ONE: ONE, "a": "a"}, {"b0": "b0"},
              {"cq": (frozenset(["cq"]), T("q")), "cp": (frozenset(["cp"]), T("p0", "q"))}, ["cq", "cp"], "p0")
report("8 edit a renames the values 0,1 of every port (D under a is D renamed); E = D:", c)

# 9. The 'no relation changed' reading: a contract whose only edit is 1, over two boundaries
D = org("D", ["x", "y"], {"x": (0, 1), "y": (0, 1)}, ["cx", "cy"], {"cx": ["x"], "cy": ["x", "y"]},
        ["b0", "b1"], [ONE], {("cx", ONE, "b0"): {(0,)}, ("cx", ONE, "b1"): {(1,)},
                              ("cy", ONE, "b0"): {(0, 0), (1, 1)}, ("cy", ONE, "b1"): {(0, 0), (1, 1)}})
p = Question(D, [(ONE, "b0"), (ONE, "b1")], "b0", PortQuery(), "y")
c = Candidate(D, p, T("x", "y"), {ONE: ONE}, {"b0": "b0", "b1": "b1"},
              {"cx": (frozenset(["cx"]), T("x")), "cy": (frozenset(["cy"]), T("x", "y"))}, ["cx", "cy"], "y")
report("9 contract of the identity edit only, two boundaries, E = D:", c)

# 10. The forward pole on C1: does Γ as a block fix L to the target's answer at every pair (Mimo's M6-B6)?
from model.cases import pole, pole_fwd_candidate, single_settings
Dp = pole()
b0 = [b for b in Dp.B if Dp.meta["bval"][b] == (1, 45)][0]
C1 = [(ONE, b0)] + [(a, b0) for a in single_settings(Dp, ("H", "T"))]
pp = Question(Dp, C1, b0, PortQuery(), "L")
cf = pole_fwd_candidate(pp)
report("10 forward pole on C1:", cf)
allfix = True
for (a, b) in pp.C:
    VN, S = cf.E.sol_sub(frozenset(cf.Gamma), cf.tau[a], cf.sigma[b])
    Ls = set(z[VN.index("L")] for z in S)
    if Ls != {pp.ans(a, b)}:
        allfix = False
print("   the block Γ = {c_H, c_T, c_L} alone fixes L to the target's answer at every pair of C1:", allfix)
for k in cf.E.comps:
    fixes = all(len(set(w[cf.E.foot[k].index("L")] for w in cf.E.L(k, cf.tau[a], cf.sigma[b]))) == 1 if "L" in cf.E.foot[k] else False for (a, b) in pp.C)
    print("   single component", k, "fixes L at every pair of C1:", fixes)

# 11. Mimo part 4 (FC34, shared): D: c: y = x, x = 1 carried at b1 (I79), x free at b0; E: one component c': y = 1
for base in ("b0", "b1"):
    D = org("D", ["x", "y"], {"x": (0, 1), "y": (0, 1)}, ["cx", "c"], {"cx": ["x"], "c": ["x", "y"]},
            ["b0", "b1"], [ONE], {("cx", ONE, "b1"): {(1,)}, ("c", ONE, "b0"): {(0, 0), (1, 1)}, ("c", ONE, "b1"): {(0, 0), (1, 1)}})
    p = Question(D, [(ONE, "b0"), (ONE, "b1")], base, PortQuery(), "y")
    for rel_b0, lab in (({(1,)}, "c': y = 1 at both boundaries"), (None, "c': y = 1 at b1, full at b0")):
        rel = {("k", ONE, "b1"): {(1,)}}
        if rel_b0 is not None:
            rel[("k", ONE, "b0")] = rel_b0
        E = org("E", ["y"], {"y": (0, 1)}, ["k"], {"k": ["y"]}, ["b0", "b1"], [ONE], rel)
        c = Candidate(E, p, {"y": Translation(["y"])}, {ONE: ONE}, {"b0": "b0", "b1": "b1"},
                      {"k": (frozenset(["cx", "c"]), {"y": Translation(["y"])})}, ["k"], "y")
        report("11 baseline %s, %s:" % (base, lab), c)
        pC = p.with_C([(ONE, base)] + ([(ONE, "b1")] if base == "b0" else []), name="p'") if base == "b0" else None

# 12. FC21 (b) with the contrast in its first disjunct: two determined answers that differ, (A) failing
D = org("D", ["p0"], {"p0": (0, 1)}, ["h"], {"h": ["p0"]}, ["b0"], [ONE, "a"], {("h", ONE, "b0"): {(1,)}, ("h", "a", "b0"): {(1,)}})
p = Question(D, [(ONE, "b0"), ("a", "b0")], "b0", PortQuery(), "p0")
E = org("E", ["p0"], {"p0": (0, 1)}, ["k0"], {"k0": ["p0"]}, ["b0"], [ONE, "a"], {("k0", ONE, "b0"): {(1,)}, ("k0", "a", "b0"): {(0,)}})
c = Candidate(E, p, T("p0"), {ONE: ONE, "a": "a"}, {"b0": "b0"}, {"k0": (frozenset(["h"]), T("p0"))}, ["k0"], "p0")
print("12 A =", A(c), "NC1 =", NC1(c), "NC2 =", NC2(c, witness=True), "answers of E:", c.ans_E(ONE, "b0"), c.ans_E("a", "b0"))

# 13. A question whose baseline answer is undetermined and whose edit fixes it (the owner question on the contrast)
D = org("D", ["x", "y"], {"x": (0, 1), "y": (0, 1)}, ["cx", "cy"], {"cx": ["x"], "cy": ["x", "y"]},
        ["b0"], [ONE, "e"], {("cx", "e", "b0"): {(1,)}, ("cy", ONE, "b0"): {(0, 0), (1, 1)}, ("cy", "e", "b0"): {(0, 0), (1, 1)}})
p = Question(D, [(ONE, "b0"), ("e", "b0")], "b0", PortQuery(), "y")
c = Candidate(D, p, T("x", "y"), {ONE: ONE, "e": "e"}, {"b0": "b0"},
              {"cx": (frozenset(["cx"]), T("x")), "cy": (frozenset(["cy"]), T("x", "y"))}, ["cy"], "y")
report("13 baseline answer undetermined, e fixes it; E = D, Γ = {cy}:", c)
print("   Ans_p:", p.ans(ONE, "b0"), p.ans("e", "b0"), "; e sets x through cx:", sets_through(D, "e", "b0", "x", "cx"),
      "; after deleting cy the answer at e is", c.ans_E("e", "b0", E=D.delete(["cy"])))
```

Its output (the lines that the ruling cites):

```
1 GLM decorated lookup: Acc = True {'F1': True, 'F2': True, 'A': True, 'NC1': True, 'NC2': True, 'NonVacuous': True} NC2 witness: (('e1', 'b0'), ['k']) slots: []
2 Mimo lookup under I83: Acc = True {'F1': True, 'F2': True, 'A': True, 'NC1': True, 'NC2': True, 'NonVacuous': True} NC2 witness: (('e1', 'b0'), ['k']) slots: []
   Ans_p: 0 ⊥
3 Mimo one component on two ports: Acc = True {'F1': True, 'F2': True, 'A': True, 'NC1': True, 'NC2': True, 'NonVacuous': True} NC2 witness: (('e1', 'b0'), ['k']) slots: []
4 GLM per-pair model: counterparts making (F1) hold (identity value maps): []
4 GLM per-pair model with λ(m)={cL}, λ(n)={cH,cL}: Acc = False {'F1': False, 'F2': True, 'A': True, 'NC1': True, 'NC2': True, 'NonVacuous': True} NC2 witness: (('e', 'b0'), ['m']) slots: []
   A: True F2: True NC1: True NC2: (('e', 'b0'), ['m'])
5 copy of a target whose answer is asserted by one component at each pair: Acc = True {'F1': True, 'F2': True, 'A': True, 'NC1': True, 'NC2': True, 'NonVacuous': True} NC2 witness: (('e', 'b0'), ['ca']) slots: []
6 Ans_p: 0 0 (every pair has the baseline answer: a contract of relabelings under I26)
6 τ(1) ≠ 1 candidate: A = True NC1 = True NC2 = (('1', 'b0'), ['k']) Hom (τ(1)=1 part of F2) = False F2 = False
7 Mimo automorphism relabeling, E = D: Acc = False {'F1': True, 'F2': True, 'A': True, 'NC1': False, 'NC2': True, 'NonVacuous': True} NC2 witness: (('a', 'b0'), ['c0']) slots: ['c0']
8 edit a renames the values 0,1 of every port (D under a is D renamed); E = D: Acc = True {'F1': True, 'F2': True, 'A': True, 'NC1': True, 'NC2': True, 'NonVacuous': True} NC2 witness: (('a', 'b0'), ['cq']) slots: []
9 contract of the identity edit only, two boundaries, E = D: Acc = True {'F1': True, 'F2': True, 'A': True, 'NC1': True, 'NC2': True, 'NonVacuous': True} NC2 witness: (('1', 'b1'), ['cx']) slots: []
10 forward pole on C1: Acc = True {'F1': True, 'F2': True, 'A': True, 'NC1': True, 'NC2': True, 'NonVacuous': True} NC2 witness: (('set(H=2)', 'b1_45'), ['c_H']) slots: []
   the block Γ = {c_H, c_T, c_L} alone fixes L to the target's answer at every pair of C1: True
   single component c_H fixes L at every pair of C1: False
   single component c_T fixes L at every pair of C1: False
   single component c_L fixes L at every pair of C1: False
11 baseline b0, c': y = 1 at both boundaries: Acc = False {'F1': False, 'F2': False, 'A': False, 'NC1': True, 'NC2': False, 'NonVacuous': True} NC2 witness: None slots: []
11 baseline b0, c': y = 1 at b1, full at b0: Acc = False {'F1': True, 'F2': True, 'A': True, 'NC1': True, 'NC2': False, 'NonVacuous': True} NC2 witness: None slots: []
11 baseline b1, c': y = 1 at both boundaries: Acc = False {'F1': False, 'F2': False, 'A': False, 'NC1': True, 'NC2': False, 'NonVacuous': True} NC2 witness: None slots: []
11 baseline b1, c': y = 1 at b1, full at b0: Acc = True {'F1': True, 'F2': True, 'A': True, 'NC1': True, 'NC2': True, 'NonVacuous': True} NC2 witness: (('1', 'b0'), ['k']) slots: []
12 A = False NC1 = True NC2 = (('a', 'b0'), ['k0']) answers of E: 1 0
13 baseline answer undetermined, e fixes it; E = D, Γ = {cy}: Acc = False {'F1': True, 'F2': True, 'A': True, 'NC1': True, 'NC2': False, 'NonVacuous': True} NC2 witness: None slots: []
   Ans_p: ⊥ 1 ; e sets x through cx: True ; after deleting cy the answer at e is ⊥
```

## Appendix B: the search on the relabeling sentence as fixed (scratch script, same folder)

```python
# The new L257 sentence: a contract at whose every pair the target's answer is its answer at (1,b0) (⊥ allowed),
# candidates with τ(1) = 1 and (A): does any meet NC2? (FC21 (a) with I26's "≠ ⊥" dropped.)
import sys, random, time
sys.path.insert(0, "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths")
from model.core import *
from model import gen as G
SIZES = G.sizes(max_ports=3, max_dom=2, max_comps=3, max_B=2, max_edits=2)
rng = random.Random(20260928)
t0 = time.time(); n = n_bot = hits = 0
while time.time() - t0 < 90:
    size = rng.choice(SIZES)
    D = G.gen_org(rng, size, family=rng.choice(['G-surg', 'G-free']))
    b0 = rng.choice(D.B)
    q = Question(D, [(ONE, b0)], b0, PortQuery(), rng.choice(D.ports))
    y0 = q.ans(ONE, b0)
    C = [(a, b) for a in D.A for b in D.B if q.ans(a, b) == y0]
    p = Question(D, C, b0, PortQuery(), q.deltaD)
    c = G.any_candidate(rng, p, size)
    if c is None or c.tau.get(ONE) != ONE or not A(c):
        continue
    n += 1
    if y0 is BOT:
        n_bot += 1
    if NC2(c):
        hits += 1
        print("NC2 holds:", p.describe()); print(c.describe()); break
print("models with τ(1)=1 and (A):", n, "of which baseline answer ⊥:", n_bot, "NC2 held in:", hits)
```

Its output:

```
models with τ(1)=1 and (A): 309046 of which baseline answer ⊥: 126102 NC2 held in: 0
```

END OF RULING
