# L81 review - hard to vary, by an Opus agent

Run 22 September 2026, read-only, no git, nothing executed. Skill: `hard-to-vary` (SKILL.md whole, plus `building.md`, `testing-against-cases.md`, `reporting.md`). Under test: `Language/authority/L81 Calibration - what Arm B measures, in file 11's terms, and when a vague translation is acceptable.md`. Source theory: `Semantics/authority/11 Claude Fable Semantics - standalone theory, revision 1.md`, Parts 0, II, III, V, VI and Derivation 2 read whole; Parts I and IV read for the transport and provenance definitions L81 leans on. Context: L64 sections 1, 6, 8 (and 5, 7, reached by the argument), L72 whole, `Language/tests/L82 Arm B corpus brief/` whole, L76 synthesis and reviews A1, A3, A4, files 38, 39, L80, the D7 gauge spec in the frozen L79 plan, Decisions L4 and L11.

How I know each claim: **seen** (I read the artefact myself, at the path given), **worked out** (follows from things tagged seen), **claimed** (a document in the record says so and I did not re-derive it). No claim below is *recalled*.

Marks are `reporting.md`'s eight. Provenance is fitted / built / asserted, one per part, in its own column. Nothing is counted or added up. Failures of mine are at the end, under Lessons, and nowhere else.

---

## 1. The question, frozen

**What is being explained.** Why Arm B's measurements are the right ones, and what makes a translation from prose to ledger wrong rather than merely different. L81 is a *rule* with a *rationale*: the rationale is that each of its parts is a named condition of file 11's (E); the rule is section 3's last paragraph.

**Over what range.** Arm B: ten short prose passages, two translators, rig 1 old and new, the reader on shuffled reports. Not rig 2, not the L66 corpus, not texts past a dozen sentences.

**What is asked.** Two questions of the owner's, quoted from Decisions L11 (**seen**): "whether your goals and targets are calibrated to semantics 11", and "whether vaguely incorrect translations are acceptable and when". The second is the one L81 alone answers.

**Kind of question.** Mostly *what counts as what under this rule?* - so the tests that bite are: remove a condition and show a counter-case; run the rule on the thing it is meant to catch and on that thing's nearest innocent neighbour. The flip test is reported below, but it is not the test that decides a rule, and I say so where it cannot bite.

**Frozen, and not drifted.** I held D = the prose, E = the ledger throughout. Where L81 slides between them I record the slide rather than following it.

## 2. The parts, and the jobs

### The jobs

| # | Job | Tag | Where |
|---|---|---|---|
| J1 | Say whether the targets are calibrated to file 11 | given | Decisions L11, owner's words (**seen**) |
| J2 | Say when a vaguely incorrect translation is acceptable | given | Decisions L11, owner's words (**seen**) |
| J3 | Keep the goal "reasoning with prose" in view | given | Decisions L11 and L4 (**seen**) |
| J4 | Give Arm B a marking rule before its plan leans on it | added (L81's own, header) | L81 header (**seen**) |
| J5 | Stop Arm B being marked by sameness_2's counts | added (from A3, L72) | L81 Traps (**seen**) |
| J6 | Tell a translator fault from a language fault | added (mine, from A4's B1) | A4 line 224 (**seen**) |

J6 is mine. L81 does not state it. A part held only by J6 is *held if* J6 is real, and I say so where it arises.

### The parts, in the owner's words

1. "the prose is the target organisation D; the ledger is a second organisation E; the translator is a transport t from D to E"
2. "the checker's questions are queries Q on E"
3. "the contract C is L64's six admitted changes (take out a line; deny a line; withdraw; make not so; open a told world alone; a named case)"
4. "The claim 'this ledger is the prose's ledger' is an Account claim (file 11 Part V, (E))"
5. "the transport is the translator's, and F1/F2 are the translator's conditions"
6. "the checker's report is a second transport, from E to the reader's understanding, and the read-back test is its fidelity condition"
7. Table row 1: two translators, same answer profile, warranted by "Derivation 2: two candidates that satisfy F1, F2, (A) on C are one account at grain C"
8. Section 3 case 1 (F1/F2, the variation test)
9. Section 3 case 2 ((A), the claim put where no query reaches it)
10. Section 3 case 3 (non-circularity, an added line supplies the answer)
11. Section 3 case 4 ("non-vacuity of the record", a sentence reaches neither line nor bin)
12. The marking rule: "counts as an error only under one of the four; everything else is variation"
13. The two vagueness bullets ("acceptable and expected"; "acceptable and desirable")
14. Section 4's four recalibrations
15. Section 5's two refutation conditions

## 3. Part by part

| # | Part | Mark | Provenance | What holds it, or what would |
|---|---|---|---|---|
| 1 | D = prose, E = ledger, t = translator | Held | fitted | L64 line 143 already applies "F1 and F2 of file 10 ... to the translator's transport" (**seen**). Remove it and parts 4-14 have nothing to attach to |
| 2 | Q is a query "on E" | Held if | asserted | Held only if an `Ans_p` on the prose exists. File 11 Part III: "**Q** is a specified set-theoretic operation on **D**, its solutions and its component structure ... Ans_p(a,b) = Q(D,a,b)". With Q living on E alone, (A) reads `Ans_E = Ans_E` and is satisfied by every ledger. What would settle it: one run in which a reader produces the prose's own answer under an admitted change, to compare against |
| 3 | C = "L64's six" | Loose | asserted | Its near neighbour - L64's actual six - does the job and does one more. L81 drops "change what fills a slot: response class, direction, strength level" and inserts "deny a line", which L64 lists not in the contract but in the variation test (a *prose* edit). See 4(a) |
| 4 | An Account claim, (E) | Loose | asserted | Replaceable, and better replaced, by file 11's (R): `Rep(o,c) ⟺ ∃t [Faithful_C(t) ∧ (Sel(t) ∨ Con(t))]`. The replacement does every job part 4 does and adds the provenance obligation L64 already met |
| 5 | F1/F2 are the translator's conditions | Held | fitted | Part IV: "A transport is **faithful on C** when it satisfies the component and global fidelity conditions of Part V". This sentence of L81 is exactly right and is the note's load-bearing true claim |
| 6 | The report is a second transport | Loose | asserted | Replaceable by Part II's measurement signature: "a part that reads or reports another part has a measurement's signature". As written it is a *declared* transport (Part IV), and "A declared transport does not make an occurrence represent anything; it makes a modeller assert that it does" |
| 7 | Same answer profile ⟹ one account (Derivation 2) | Held if | fitted (on L72's Thing lines) | Held only if F1 and F2 hold too, which the row's measurement cannot see. Derivation 2's antecedent is F1 ∧ F2 ∧ (A); the row measures (A) alone. Derivation 9: "If M₀, M₁ have the same input-output projection and differ on an account claim, no function of the projection agrees with the claim on both" |
| 8 | Case 1, F1/F2 | Held | built | Held by L64 line 143 and A3's finding that it "is the one instrument that reads the text" and "has never been run" (**seen**). Removing it leaves Arm B with no instrument that compares a ledger to its prose |
| 9 | Case 2, (A) | Held if | built | Held if J6 (translator fault vs language fault) is not wanted. L72 finding 1 (**seen**): "This is ... a finding about the language, not about either translator." As a marking rule for *translators* it charges the wrong layer |
| 10 | Case 3, non-circularity | Held, jointly with part 13 | borrowed (patch 10; 38 line 113) | Held by patch 10's "added lines alone give the conclusion" and 38 line 113's note. Alone it covers only filled-in lines; the licence to fill in is part 13's, and neither stands without the other |
| 11 | Case 4, "non-vacuity of the record" | Loose | asserted | Its near neighbour is 39's final check 4, "Every sentence of the text appears in the ledger, in the bin, or in both" (**seen**), which does the job exactly. File 11's non-vacuity is `Sol_D(1,b₀) ≠ ∅` plus the stated-scope clause, and a dropped sentence is neither |
| 12 | "Only under one of the four" | Loose | asserted | Its near neighbour - "under one of the four, or a reader's verdict against the prose" - does every job and does one more (section 5's). See 4(b) |
| 13 | The two vagueness bullets | Held | fitted (L66's four refusals; L72 T11-D) | The only part that answers J2, which nothing else in the record answers. L66: "The translator noticed and refused to repair four of the six" (**seen**). This is L81's unique work |
| 14 | Section 4's four recalibrations | Held | built | Each names the record item that forced it: L66's plants, L64's bin threshold, L64 section 8 condition 5, decision L4's goal. Remove any one and a live L76 correction goes unanswered |
| 15 | Section 5's two conditions | Held if | built | Held if some Arm B role can compare a ledger with its prose. Under A4's cast none can: the Reader is "blind to ... ledgers; texts", the Predictor to "the texts themselves", the Marker works "against the frozen table" (**seen**, A4 lines 197-203) |

Nothing here is added up, and no part's mark is stronger for the number of parts around it.

## 4. Whole-explanation checks

### (a) Is every mapping in sections 1 and 2 a correct use of file 11's terms?

Five are correct. Four are loose analogies, and two of those change what Arm B will measure.

**Correct.** (i) Prose as D and ledger as E is a legitimate reading of Part II's organisation, and L64 made it first. (ii) "F1/F2 are the translator's conditions" is exactly right, by Part IV's definition of `faithful`. (iii) Table row 3's mapping of the variation test to F1 and F2 on C is right. (iv) Table row 1's "Not measured: which ledger is right; whether the prose is right" is right, and is the note's most honest line. (v) Section 5's remedy - "C needs a seventh change" - is precisely file 11's own: Derivation 2's Consequence, "The remedy is a finer contract, which is a new question." L81 gets the remedy right and omits only the clause that makes it a *new claim at a new index* (Part III: "a narrowing adopted after a failure is a new claim at a new index").

**Loose analogy 1: "an Account claim".** Part V opens: "An explanatory candidate for question p is an organization E, a transport t = (π,τ,σ,λ) from D to E, and an identified set Γ of active commitments in E." The ledger is not offered as an *explanation of the prose*; it is offered as a re-presentation of what the prose commits its writer to. File 11 has the exact home for that, and it is not (E) but (R):

> `Rep_ℓ(o,c) ⟺ ∃t [Faithful_C(t : Org_ℓ(o) → c) ∧ (Sel(t) ∨ Con(t))]`

(R) asks for F1 and F2 (that is what `Faithful` means) *plus a provenance*. L81's (E) asks for F1, F2, (A), non-circularity and non-vacuity, and asks for no provenance at all. The swap costs two things. It pulls in three conditions that belong to a candidate explanation of the prose's *conclusion*, not to a translation - and section 3 then has to bend two of them (see (b)). And it drops Derivation 3, which is the derivation that actually governs Arm B. L64's own row supplies it (**seen**): the prose-to-ledger layer is "selected: tuned on cases it met; underdetermined on unseen changes (Derivation 3)". Arm B's texts are, by design, unseen. Derivation 3 therefore predicts translator disagreement on Arm B and says what it does and does not show. L81 cites Derivation 2 and never cites Derivation 3.

**Loose analogy 2: "queries Q on E".** Part III: "Q is a specified set-theoretic operation on **D**, its solutions and its component structure ... The answer profile is `Ans_p(a,b) = Q(D,a,b)`." Q is defined on the target. (A) then reads `Ans_E(τ(a),σ(b)) = Ans_p(a,b)` - the ledger's answer must equal *the prose's*. Put Q on E alone, as L81 does, and there is no `Ans_p`; (A) becomes an identity and holds of any ledger whatever. This one word - "on E" - is the formal shape of everything that goes wrong in section 3: the marking rule only ever compares one E with another E, and the prose never enters.

**Loose analogy 3: the six admitted changes.** L81 says "the contract C is L64's six admitted changes (take out a line; deny a line; withdraw; make not so; open a told world alone; a named case)". L64's six are (**seen**, L64 section 1): take out one line or a group; WITHDRAW a line; MAKE a fact NOT SO; **change what fills a slot: response class, direction, strength level**; add supposed lines in a named case; open a told world alone. L81 has dropped the slot change and inserted "deny a line", which in L64 belongs to the *variation test* on the prose (line 143: "deny a clause"), not to the contract on the ledger. Two faults in one list:

- The contract is now half prose edits and half ledger edits, and L81 never says which side it lives on. Under file 11 the contract lives on D and τ carries it to E; "open a told world alone" and "a named case" have no prose counterpart at all, so as stated C cannot be a contract on the prose.
- The dropped change is dropped silently, which is the one thing Part V's non-vacuity forbids: "The contract C is a declared subset of the physically admitted edits, and every physically admitted edit excluded from C is excluded by a **stated scope, not silently**." L81 violates, in section 1, the very condition it names in section 3 case 4. There may be a good reason for the drop - the slot change is rig 2's, and Arm B runs rig 1 - but file 11 requires it said, and L64 section 5 already shows the house style for saying it.

**Loose analogy 4: "the report is a second transport ... from E to the reader's understanding".** A transport in file 11 is `t = (π,τ,σ,λ)` between two *organisations*. "The reader's understanding" is nowhere given ports, components or admitted edits, so there is no organisation at the far end and no transport. Worse, every transport has exactly one of three provenances, and this one has none of the first two: there is no population and survival history, and no construction witness for a transport into a fresh agent's understanding. By Part IV's own definition it is therefore **Declared** - "Neither of the above. The transport is entered into the model by its author" - and Part IV says what that is worth: "A declared transport does not make an occurrence represent anything; it makes a modeller assert that it does."

The right file 11 term is in Part II, and it is better for the project than the one L81 chose:

> "a part that reads or reports another part has a measurement's signature: change only the reading and the part it reports stays as it was; change the part and the reading follows. Which of the two an account offers as producing an outcome is settled by that signature, not by the account's wording."

The report is a **measurement** of the ledger. Calling it a transport dresses a measurement as a representation, which is exactly the error Part III warns against: "A measure that identifies an outcome ... answers the identification question; whether the measured part also produces the outcome is the production question, and the first answer is not the second." The read-back test is an *identification* question about the reader, and it should be stated as one. Nothing in the practical design changes; the term does.

**On row 1 and Derivation 2.** Derivation 2's claim runs F1 ∧ F2 ∧ (A) ⟹ one account and coinciding answer profiles. L81 runs it backwards: it measures coinciding answer profiles and concludes "one account at grain C". The converse is not in file 11 and is denied by it. F1 exists precisely to stop this: "(F1) prevents an assembled match from hiding a wrong decomposition." And Derivation 9 is the general form of the denial. "Answer profile" is also doing double duty: file 11's `Ans_p` is a function of D; L81's is the checker's report kind and consequences list, which is a projection of E through a patched instrument that A3 showed "takes the ledger as given" (**seen**). So row 1 measures a projection of E, cites a theorem about D, and concludes about accounts. It is the weakest of the three rows and file 11 says so twice.

### (b) Section 3's four cases

**Is each a condition of (E)?** Three are, at a stretch; one is not.

- Case 1 is F2, correctly. It is not F1. File 11 keeps them apart on purpose: "(F1) prevents an assembled match from hiding a wrong decomposition. (F2) prevents a set of locally correct pieces from hiding a lost shared constraint." Every instance L81 gives ("the ledger keeps a cause"; "the ledger's dryness survives") is global. The F1 fault - right answers under every admitted change, wrong decomposition - has no case, and L81 explicitly waves it through under "acceptable, and expected" ("the form of a line"). At this grain Derivation 1 licenses that; at a finer contract it will not, and the note does not say so.
- Case 2 is (A), roughly, but the quotation attached to it does not support it. L81 quotes "an account of a different query is not an account of this one". That sentence of Part V is a prohibition on changing Q mid-assessment; it is not about a query failing to reach a claim. The support case 2 wants is (A) itself plus Part III's "Two questions with the same D and different (C,Q) are different questions".
- Case 3 is non-circularity's *negative* half only. File 11's condition has a positive half that L81 omits: "There exists (a,b) ∈ C that removes or replaces a nonempty block of Γ while preserving the other boundary conditions, under which the answer profile changes or ceases to be determined in the claimed way." A ledger on which no admitted change changes anything fails (E) however faithful it is. That is a fifth case, and it is Arm B's most likely silent failure on the sound sides and the controls.
- Case 4 is not a condition of (E) at all. Non-vacuity is `Sol_D(1,b₀) ≠ ∅` and the stated-scope clause. A sentence that reaches neither a line nor the bin is either a special case of F2 (if the sentence carried a commitment, the ledger now admits solutions the prose excludes) or no error at all (if it carried none). Its true home is 39's final check 4, which states it word for word. Nothing practical is lost by re-sourcing it, and one thing is gained: 39's version is checkable by the gauge, and file 11's is not.

**Are they exhaustive against Part V?** No. Three gaps:

1. Non-circularity's positive half, above.
2. Non-vacuity's stated-scope clause, which has no case - and which L81 breaks in its own section 1.
3. Part V's further clause, live because of the drop in (a): "A contract consisting only of relabelings, or **excluding every change under which the active commitments could matter to Q**, does not satisfy non-circular dependence and is therefore not a contract on which an account can be claimed."

**Is the "acceptable" rule sound?** No, and the failure is in the direction that produces false findings about the prose.

The rule is: same answer profile under every admitted change ⟹ same ledger at this grain ⟹ acceptable. Three things let a wrong translation through.

*It never looks at the prose.* Both halves of the comparison are E's. This follows from part 2 ("Q on E"): with no `Ans_p`, "same answer profile" is agreement between two ledgers, and Derivation 9 says no function of their outputs decides an account claim about D.

*It only looks at differences.* The rule is stated over "a difference between two translators, or between a translation and the text", but its criterion - answer-profile equality - can only be computed between two ledgers. A shared error produces no difference and is never marked. Both Arm B translators are language models running the same prompt (39), so shared errors are the likely kind, and L72 already wrote the warning: "two translators agreeing may both be wrong" (**seen**).

*Its C is short by one change*, and the missing one is the change its own vagueness bullet needs. L81 says "the lamp drew the visitor back" must stay a drawing, "not a pull"; the change that separates a drawing from a pull is a response-class change - the slot change L81 dropped. With L81's six, the note's own worked example of a wrong translation is marked acceptable by the note's own rule.

**A concrete prose example.** Section 5's refutation condition, reachable today, and reachable inside the L82 corpus as briefed:

> "The inspector reported that the cellar flooded because the valve may have been left open."

L64 section 5 sends "may, must, should, can, obliged, optional" to the bin (**seen**). So a translator bins "may", records the reason - a *marked* act, not an unmarked addition - and writes the content as `holds(open(valve))` TOLD in the inspector's world, with `claim_because(..., flooded(cellar), open(valve))`. Both translators will do this, because 39, 38 and L80 say nothing about what survives when the modality is binned (**seen**: no occurrence of "may", "might", "modal" or "perhaps" in 39 or L80). Now:

- No admitted change of L81's six separates "the valve was open" from "the valve may have been left open". Modality is excluded from C.
- The two answer profiles are identical. L81's rule marks both acceptable.
- A competent reader says both are wrong about the prose: the inspector committed to a possibility, and the ledger commits him to a fact.
- The consequence is not cosmetic. The checker will report the BECAUSE as a bare claim - a *fault* - against a sentence whose writer hedged precisely to avoid claiming it. That is a false finding about the prose, generated by the language and endorsed by the marking rule.

The error also escapes L81's other guard. The "acceptable and desirable" bullet catches sharpening only when it is "an unmarked addition"; here the addition is marked, in the bin, and the ledger is wrong anyway.

**Is section 5's condition reachable?** In principle, yes: the example above meets it. In Arm B as A4 staffs it, no. The condition needs "a competent reader [who] says one is wrong about the prose", and no role in the cast ever sees a ledger beside its prose: the Reader is blind to ledgers and texts, the Predictor to the texts, the Marker works against a frozen table, and the translators write no verdict (**seen**, A4 lines 197-203). So L81's own refutation condition cannot fire in the run it was written for. That is the single most important thing in this review.

### (c) The L82 brief

**Does it exercise the four cases?**

| Case | Exercised? | Why |
|---|---|---|
| 1 (F1/F2, variation) | Partly | Pairs A, C, D differ by an *added sentence* (a general rule or route); pair B by the *object of a denial*, within the clause. Only B is the clause-level difference L81's row 3 describes |
| 2 ((A), claim out of reach of the query) | Strongly, by construction | Every passage contains a report, so every argument is told-world content |
| 3 (an added line supplies the answer) | Designed away | The encoding guide instructs: "Do not also write a rule that makes the cause produce the effect unless the text states such a rule" (**seen**). Arm B will test obedience to that line, not case 3 |
| 4 (a sentence reaches neither line nor bin) | Yes | The encoding guide requires a structured bin with an integer `sentence` (**seen**), so the D7 gauge line `sentences with no line and no bin entry` will read a number rather than `not recorded`. This is a real strengthening over 39, which asks only for "the words from the text, and the reason" |

**Does it exercise the variation test?** Only inside told worlds. Every argument in the corpus is the reported person's; the brief allows the narrator "one plain fact of their own per passage" and no argument. So on every one of the ten texts, a difference between two ledgers can be the varied clause *or* the world placement, and nothing tells them apart. L81's three questions are entangled on the whole corpus. One added text - the same argument as the narrator's own, outside any report - separates them, and costs a paragraph.

**Is each pair a matched pair in the skill's sense?** One is. Three are not.

The skill asks for "one change to the world that should alter the outcome, and one that should not; the second must sit next to the disputed line, not remove the ability or the grounds wholesale", and adds: "run it on the very thing it is meant to catch, and on that thing's nearest innocent neighbour. A test that both pass is measuring something else."

- **Pair B is a matched pair.** B-faulty denies the same cause the report asserts; B-sound denies a different one. Same shape, one referent changed, and the checker must fire on one and stay silent on the other. This is the design the other three want.
- **Pairs A, C and D are not.** Their two sides are the change that *should* matter (add the connecting rule) with no neighbour beside it. The missing half is a third text per pair: the same faulty report with a general rule added that does **not** connect the cause to the effect. If the checker falls silent whenever any ALWAYS line is present, it is measuring "is there a general line", not "does the argument connect", and as briefed nothing would show it.
- **Controls E1 and E2 are the wrong neighbour.** They remove the argument wholesale, which is the case the skill names as not a poke pair. They are worth keeping - they answer A4's B3 - but they cannot stand in for the near neighbour A, C and D lack.

**Three further things in the brief and its folder.**

1. *An instruction conflict that would destroy the matching.* The brief says pairs are "alike in setting" (A) and "Same setting" (B), and also "Vary the settings" with ten named settings for ten passages. A writer who reads the second instruction as binding gives every passage a different setting, and pairs A and B stop being matched. Pairs C and D never say "same setting" at all. One sentence fixes it: pairs share a setting, and the four pairs plus two controls use six of the ten.
2. *The encoding guide breaks A4's blinding.* A4 has Translator 1 "blind to ... the earlier ledgers". The guide attaches `example_T10D.json`, which I checked byte-for-byte against `L72 Return - Astra Ultra/rigs/rig 1 - arguments/ledger_T10D.json`: same `whose`, same sentence, same six line ids (**seen**). It is Astra Ultra's L72 ledger of T10-D - the earlier ledger of the exact structure Arm B's B1 tests, a report with a cause claim inside a told world. L72 recorded this failure mode in its own "What this test does not show": "the two 'independent' translators are not independent of the examples" (**seen**). Arm B is about to repeat it, with an example chosen from the phenomenon under test. `example_A.json` and `example_P14.json` do not have this problem; T10-D does.
3. *One line of the guide carries more weight than 39 or L80.* "A told world does not inherit the actual ledger; state inside it every fact its argument needs." Whether B1 and B2 can fire depends on it, and it appears in no authority file and carries no mark in L81.

**What the corpus cannot test at all.** J2 - the owner's own question. The brief says "Plain words; no metaphor that would need unpacking", which removes exactly the vague verb the "acceptable and desirable" bullet is about, and nothing in the brief produces a hedge, a figure, or an unsettled standing. So the one part of L81 that is held (part 13) has no text in Arm B that reaches it.

### (d) Swap, flip, poke on the central claim

The central claim: *same answer profile under every admitted change ⟹ the same ledger at this grain ⟹ acceptable.*

**Swap "answer profile" for L64's "said-content".** Breaks. L72's Thing lines and line forms (50 lines against 21, half of them Thing lines) would all read as differences. The swap fails, so "answer profile" is held in place by the L72 result - this part is doing real work and is L81's genuine advance on L64 section 8.

**Swap "under the admitted changes" for "the report kind alone".** Breaks on T10-D, where both reports are silent and the ledgers differ in where the BECAUSE sits. Held.

**Swap "L81's six" for "L64's six".** The verdict changes on L81's own T11-D example: with the slot change restored, drawing-into-pull is caught; without it, it is marked acceptable. The list is load-bearing and it is wrong. This is the swap that matters most.

**Swap Derivation 2 for Derivation 9.** The verdict of row 1 reverses. The citation is doing work and is the wrong citation.

**Flip.** The flip does not bite here, and I say so rather than leave it out. L81 is a rule, not a causal story, and file 11's own treatment of a derived conclusion applies: it is tested by removing a condition, not by flipping the outcome. But the flip's *shadow* does bite, and it is worth recording. If Arm B's two translators agree everywhere, L81 says the grain is working. If they disagree in answer profile, section 4 says that "shows the language wrong". Both outcomes leave L81 itself untouched; the only thing that can charge L81 is section 5, and section 5 cannot fire in the run (above). So as things stand there is no Arm B result that counts against this calibration.

**Poke, both halves.**
- *Should not move the outcome, sitting next to the line:* swap a name throughout a text. L81's rule says the answer profile is unchanged; the checker's own rule lists "a finding that changes when a name changes" as an unacceptable error (L64 line 144, **seen**). This half holds.
- *Should move the outcome:* remove a hedge from one text of a pair ("the valve may have been left open" → "the valve was left open"). The prose's commitments change. The ledgers do not, because modality is excluded from C. The rule reads identically in both halves of the pair, so it is measuring the checker's output, not the ledger's fidelity to the prose. This half fails, and it is the failure the example in (b) turns on.

**Reverse.** Poke the cause, poke the effect. Is L81 running backwards from L72? Partly, and this is worth the owner's eye. L72's awkward result was that the sameness program found 4 matches in 21 and the hand pairing found 21 of 21; A1 and A3 then found that the hand pairing was *wrong* to absorb the TOLD/CLAIMED difference, because L72's finding 1 says TOLD content is never checked (**seen**, L76 line 13). L81's rule is precisely what makes the hand pairing right again by fiat. Poke the supposed cause: remove file 11 entirely - does the rule move? No. L64's give-up line already said it: "Exactness of wording; one right translation. Never the writer's commitments", and "the same said-content, differences only in marked readings" (**seen**). So the conclusion was already in the starting points; what file 11 adds is the *criterion* (answer profile under admitted changes) that L64 lacked. The criterion is new work; the conclusion is not.

**Hunt the answer in the starting points.** Found once, above. Also: L81 cites "L64 section 8's fifth condition, as review A1 read it" in support of absorbing differences. A1's actual reading (**seen**, A1 line 188) is the opposite: the condition "could not have fired", is "worded to a quantity that misses it", and "the difference that matters did occur: the checker's report differs on two of eight texts". A1 said the condition was too coarse to catch a real difference; L81 cites it for the proposition that differences should be absorbed. Section 4's restatement of the condition in terms of answer profile *is* faithful to A1. The section 3 citation is not.

**Add a job.** J6 - tell a translator fault from a language fault. L81 survives it only in part. A4's B1 already draws the line ("Silence on one ledger only charges the translator ... Silence on both charges the language"), and L81's marking rule, which marks a difference "between two translators" as an error under case 2, loses it. Adding J6 rules out nothing that was not already ruled out by A4, so on this job L81 adds nothing and subtracts something.

**Look inside.** Matching the reports is not matching the workings. L81's entire measurement runs through the checker's report, and A3 found that "every instrument takes the ledger as given; none reads the text beside the ledger, so all five read identically when the translator errs and the ledger stays consistent" (**seen**). The one instrument that reaches inside is the variation test, which L81 rightly makes its third row - and which remains, on the L82 corpus, un-separable from the told-world question (see (c)).

**Pairs that pull.** One pair, and it is sharp. *The vagueness bullet* against *the marking rule*. The bullet says a translation that sharpens is "the error, not the vagueness". The rule says anything no admitted change detects is variation. Sharpening is, by construction, the case where no admitted change detects it - a sharper commitment differs from a vaguer one only under changes that reach the sharpened slot. The two parts contradict each other on the class of cases the owner asked about. The rule wins, because it is the operative sentence ("So the marking rule for Arm B"). Where the line should be drawn: the bullet is right and the rule needs the exception.

**Check the patches.** L81 is itself a patch on L64 section 8's condition 5, which A1 showed could not fire. What does the patch give up? It gives up the comparison of a translation with its text - the only comparison that could have caught a shared error - and replaces it with a comparison of two translations. `reporting.md` asks for what a change gives up as well as what it fixes; L81 records the fix (section 4, third bullet) and not the give-up. Catch-alls: L81 introduces none, and its "everything else is variation, recorded in the sameness diagnostic and not scored" is a bin with a gauge (sameness_2's buckets), which is the right shape - but the gauge has no threshold and L81's own trap forbids reading it, so nothing could show it swallowing a job.

**What the change list leaves out.** L64 section 5's excluded list, which L81 never mentions: amounts, places, times beyond order, beliefs, purposes, modality, numbers, several causes together, figures of speech, unshaped verbs. Every one of these is a class on which a shared sharpening is undetectable by construction. L64 gave each a gauge; L81 inherits none of them.

**Build the best rival.** The rival is A4's B1-B5 plus A3's variation test - both already in the record, both already adopted at L76. Run the change list against the pair. On row 1 (two translators): the rival is A4's B1, which additionally assigns the layer charged. On row 2 (where the question lives): A4's B1 and B2. On row 3 (the variation test): A3's recommendation, adopted at L76. On row 4 (read-back): A4's A2 and the Reader role. Section 4's recalibrations: A4 and A1 already forced three of the four. So on every job but one, no change on the list tells L81 from the rival, and they are the same explanation at this level. The one job that separates them is J2 - when a vague translation is acceptable - which A4 does not address and which is the owner's own standing question. **L81's unique work is section 3's first two bullets and section 4. Its four cases and its marking rule add a layer the record already had, in terms that do not survive the check.**

**Where the parts came from.** Written into the table in section 3, one per part. Three of the four loose parts are *asserted*; the held ones are *fitted* (on L66 and L72) or *built*. The skill's first place to look is the fitted and borrowed parts, and here it is the asserted ones that gave way.

## 5. What would make it harder to vary

Two, in order.

1. **Give section 5's first condition someone who can fire it.** Add one role to Arm B: a fresh agent given a text and both ledgers of it, asked one question - "does either ledger commit the writer to something the text does not, or fail to commit them to something it does?" - and blind to the map, the reports and the plan. Without it, L81's refutation condition is decoration, and the whole calibration is untestable by the run it calibrates. This is the one change that turns the note from a rule into a claim.
2. **Restore L64's sixth change, or state the exclusion.** Either put "change what fills a slot: response class, direction, strength level" back into section 1's list, or write the scope sentence that excludes it (Arm B runs rig 1 only). File 11 requires one or the other, and the note's own case 4 is the condition it breaks.

A third, cheaper than either: add the missing near neighbour to pairs A, C and D - one more text per pair, with a general rule that does not connect - and one text whose argument is the narrator's own, outside any report. Four passages, and the corpus can tell L81's three questions apart.

## 6. What this does not show

Hard to vary is not true. Nothing here shows L81's marking rule gives the wrong verdict on any text that has actually been translated; the modality example is a case I constructed, not a run. Nothing here shows the four cases are *false* - case 1 in particular is right, well sourced, and the instrument the project most needs. "Loose" on parts 3, 4, 6, 11 and 12 says only that a near neighbour would do as well or better, not that the part is wrong. I did not test L81 against file 11's Parts VII-XV, did not run the checker, did not read the ten Arm B texts (they do not exist yet), and did not re-derive A5's or A3's claims about the git history or the scratch runs.

## 7. One next step

Before the Arm B plan is written: decide the reader-with-both role of (5.1). Everything else in this review is an edit to two documents; that one is a change to the cast, and the plan cannot be frozen twice.

---

## (e) The one sentence

**Add**, to the end of section 3:

> A difference between a translation and the prose is judged by a reader who sees both, not by the answer profile; where no admitted change reaches the difference, that is section 5's finding and C is short a change.

It does three things at once. It removes the force of "or between a translation and the text" in the marking rule, which is the clause that extends a two-ledger criterion to a comparison the criterion cannot compute. It makes the modality case, and any shared sharpening, land where it belongs - as a finding about the grain rather than as unmarked variation. And it names the role that section 5 currently has no one to fill.

If the owner would rather strike than add, the sentence to strike is the marking rule's opening clause, "a difference between two translators, **or between a translation and the text**," down to the comma. Striking it makes the rule honest about what it measures. It does not make section 5 reachable, which is why the add is the better of the two.

---

## Lessons

Failures in this review, mine, listed here and nowhere else.

- **L1. I nearly reported case 4's gauge as dead.** From 39 alone (a bin of "the words from the text, and the reason") and the D7 spec (`sentences with no line and no bin entry`, structured bin only, "else `not recorded`"), I concluded the gauge would read `not recorded` on every Arm B ledger, and had written it up. It was wrong: the encoding guide, which I had not yet read because the task named only the brief, requires an integer `sentence` on every bin entry. The occasion this covers: a folder named for one document usually holds more than one, and a verdict about what a run will produce must be checked against every file in the folder before it is written, not after.
- **L2. My first reading took "deny a line" for a wording of MAKE NOT SO** and let the six-change list pass. It survived only because I set L81's list beside L64's section 1 line by line instead of reading them for sense. A citation that says "L64's six" must be counted against L64's six, every time, and the count is cheap.
- **L3. I ran the flip test before noticing it could not bite** on a rule, and had to go back to SKILL.md's own note that a derived conclusion is tested by removing a condition instead. I did not open `by-domain.md`, which holds the full treatment and which the skill's table sends you to for "what is a part in this field" - so my reading of what the flip does to a rule rests on the main file alone. The skill names the kind of question in step 1 for this reason, and I named it after choosing the tests rather than before.
