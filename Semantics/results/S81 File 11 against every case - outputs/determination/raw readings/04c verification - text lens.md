# S81 step 3: adversarial verification of the decisive rows, text lens

*Written by Claude, a verifier for the S81 determination, 23 September 2026. For each decisive row it tries to refute the step-3 ruling from the texts of file 10 and file 11 and the case book. Where the texts do not refute the ruling, the ruling is upheld. "f10" is file 10 and "f11" is file 11. Line numbers are those files' lines.*

**Sources read.**
- The four step-3 rulings files (`rulings - O1 group.md` to `rulings - O4 group.md`), in full, and `run.log`.
- File 10 and file 11, in full.
- The case book entries for O1, O5, O10, O15, O17, O20, O21, O25–O27, O30, O35–O41, O45, O46, O48, O50–O52.
- The plan, second version, lines 95–225, and its third version, in full.
- `table.md`. The mark rules at the head of `briefs/s81_1C_A.txt` (lines 1–45).
- The step-3 packets for O5, O15, O30, O35 and O40 (sections 5–15).
- `determination/01` on O35 (lines 373–390), and `determination/03` section 6 (lines 231–250).
- S75 Results line 17. The S72 Stage 1 return `01 The bare earlier version against every case.md`, lines 33, 48 and 53 (O20, O35, O40).
- A search of the seven accepted 1C, 1K and 2b returns for "CASE DISPUTED".

**Not opened.** The effort-controls folder. The supplementary audit of Mimo on tester A and its returns. The folders set aside by decision S16. The provenance file, because no reader and no ruling marks CASE DISPUTED.

**The decisive rows, as the task defines them.**
- O35, for test (b).
- O48, for test (a) and P1.
- Every row ruled a theory change away. There are none. The rows where a reading would have given one are checked in section 7.
- Every S75 correction: O45, O20 and O40. O15 is added, because both 1K returns agree on a different mark there and the ruling refuses the correction.
- Every CASE DISPUTED ruling. There are none (section 8).
- Every row whose file-11 ruling departs from the majority of the five file-11 readings (both 1C marks and the three YOUR MARKs): O5 (4 SILENT, 1 AGREE; ruled AGREE), O10 (3 SILENT, 2 AGREE; ruled AGREE) and O30 (2 SILENT, 1 SPLIT, 2 AGREE; ruled AGREE).

---

## 1. Result

| row | why decisive | step-3 ruling | verdict | what it turns on |
|---|---|---|---|---|
| O35 | test (b) | f10 SILENT (baseline), f11 SILENT, SAME, passage CHANGED (additive), no change | **UPHELD** | nothing open: the plan's rule fixes the file-10 mark |
| O48 | test (a), P1 | f10 DISAGREE (baseline), f11 AGREE, CHANGED, passage CHANGED (alteration), toward, theory change; P1 HOLDS | **UPHELD** | nothing open |
| O45 | S75 correction | f10 SPLIT (corrected from AGREE), f11 AGREE, CHANGED, toward, theory change (M28) | **UPHELD** | whether "an identified set \(\Gamma\)" (f10 L246) is fixed by fact or by the candidate; toward either way |
| O20 | S75 correction | f10 AGREE (corrected from SILENT), f11 AGREE, SAME, no change | **UPHELD** | nothing open that changes a mark |
| O40 | S75 correction | f10 AGREE (corrected from SILENT), f11 AGREE, SAME, no change | **UNCERTAIN** | whether f10 L25's empty place "if anyone had them" gives "Neither can say 'mostly'" (AGREE) or leaves it to an input (SILENT). No reading gives a change away |
| O15 | refused correction (both 1K SPLIT) | f10 AGREE (baseline kept), f11 AGREE, SAME | **UPHELD** | nothing open |
| O5 | departs from majority; decisive for test (b) | f11 AGREE, f10 AGREE, SAME | **UPHELD** (medium) | whether "a verdict given the input" (f11 L514) counts as reaching "legitimate" with a qualification |
| O10 | departs from majority | f11 AGREE, f10 AGREE, SAME | **UPHELD** | nothing that could give a change away (shared text) |
| O30 | departs from majority; decisive for test (b) | f11 AGREE, f10 AGREE, SAME | **UPHELD** (medium) | whether the situation's "compares the pressures itself" supplies the boundary input of f11 L514 |

**Counts.** Nine decisive rows examined: 8 UPHELD, 0 OVERTURNED, 1 UNCERTAIN (O40). No row was ruled a theory change away, and no reading examined here shows one (section 7). No CASE DISPUTED was raised or ruled (section 8). The side checks are all upheld: O17, O13, O19, O50, O32, O15 (file 11), and the rule applications on O18, O31, O37 and O41.

**Consequences.**
- Test (a) and P1 hold on O48.
- Test (b) holds on the text. It now turns on three file-11 AGREE rulings that stand against a SILENT reading, not on O35: O5 (f11 L161 s3 with L514), and O30 and O17 (f11 L419, L465, L514). Each of those SILENT readings would rest on new sentences of file 11. If one of them held, the row would be AGREE→SILENT, a theory change away. These three rows are the ones to put to the Atria and Mimo cross-examination (plan v3 (g)).
- If O40 is SILENT under file 10, the S75 corrections number two (O45, O20), not three. O40 becomes SILENT→AGREE: CHANGED, toward, a theory change through f11 L27 s3 and L433 s4 (M4, M40). P2 then fails at O40 by a theory change toward, which the standing rule's saving clause names. Test (b) is unaffected.

---

## 2. O35: Four seconds (test (b))

**Case** (case book, O35). "During the washer repair the protected tap stops for four seconds while the mains is switched over, then runs as before. Nobody drew from it in those seconds." Fixed verdict: "The protected condition held in every way that mattered: nobody was without water. The interruption is on the record and is not a loss."

**The ruling** (`rulings - O4 group.md`, lines 352–425). File-10 mark SILENT (baseline). File-11 mark SILENT. Verdict SAME on the same point. Passage CHANGED (additive). No change. It is a change from 01, which had file 10 AGREE, CHANGED, away and a theory change.

**Attempt 1: the file-10 mark should be AGREE, from the 1K returns and Claude's file-10 reading.** This fails on the plan's rule before any reading of the text. The rule reads: "S75's baseline, unless both 1K returns agree on a different mark and Claude's own reading of file 10 confirms it" (plan v2, "The words Claude rules with"). The baseline is SILENT. Both 1K returns mark SILENT (table row O35; packet sections 7 and 8, "MARK: SILENT" in each). Both returns name the endpoint AGREE as their strongest contrary and rule it "HOLDS: NO". The first condition of a correction is therefore unmet, and Claude's reading of file 10 cannot move the mark. Even 01's AGREE, written before the returns, could only have been recorded as a finding about S75, as the rulings do for O18 and O41. The counted file-10 mark is SILENT.

**Attempt 2: on the text, file 10 is AGREE (01's reader 1, the endpoint reading).** The argument runs as follows.
- f10 L441 checks a protected obligation at two states only: \(\forall r\in P[r(\xi)\Rightarrow r(\xi')]\).
- The tap "then runs as before", so any condition on a state holds at \(\xi'\).
- f10 L444 asks only that "Losses outside \(P\) must be exposed", and the interruption is on the record.

The argument fails, on three grounds.
- The formula fixes *when* \(r\) is evaluated. It does not fix *what* \(r\) says. f10 L438 takes the obligations as "fixed for the comparison", and f10 L164 makes them part of the question: "\(O_p\) is the set of obligations being addressed or protected." The case names the thing protected ("the protected tap") and states no condition.
- A condition over the work interval is admissible in file 10. f10 L122: "Values of ports may be paths, functions, fields, proofs, or histories." S75 needs that reading elsewhere. Its baseline for O38 is AGREE under file 10, and O38's fixed verdict ("it was broken, for four seconds") can be reached only if (P) finds a loss when the tap runs at both endpoints (case book O38: "the kitchen tap runs at all times during the work"). So the endpoint content is one content among several. It is not the text's default.
- The endpoint reading also leaves the ground of point 1 unreached. "In every way that mattered" invokes a standard of what matters, and f10 L25 marks that place empty ("a merit function … marks those places as empty").

S72's own reading of file 10 takes the same view (S72 Stage 1 return 01, line 48): "the protected predicate and its time range are unstated; protection is satisfied for an actual-demand obligation and violated for continuous-flow protection … the bare formula requires protected obligations 'fixed for the comparison' and the case does not specify that input". S75 records the row as "O35 (the unstated protected condition)" (S75 Results, line 17). The file-10 SILENT stands on the text as well as on the rule.

**Attempt 3: file 10 is SPLIT, not SILENT.** The two contents are two readings of the case's unstated input. They are not two readings of the theory's sentences. Mark rule 4 of the brief names this configuration: "it takes the deciding matter as an input the case leaves unstated". For direction, SPLIT and SILENT rank together, so this attempt could not make the row a change away in any case.

**Attempt 4: file 11 is AGREE or DISAGREE.**
- AGREE needs the covered occasions to be the draws.
- DISAGREE needs the condition to be "the tap runs" (Mimo's 2a).
- Either choice supplies an input the case does not state. f11 L433 s1 makes the obligations "declared inputs … each as a stated condition over stated occasions". f11 L514 says "where the input is missing, the verdict is unsettled and the semantics says so rather than choosing the input from the verdict wanted."
- The file-11 SILENT stands. All five file-11 readings rest it on L433 s1 and L514. Only 1C B mentions worth, and only in a NOTE.

**Attempt 5: the two SILENTs are on different points.** The 1K readers name point 1 ("held in every way that mattered"). The 1C readers name point 2 ("is not a loss"). The two are one point:
- f11 L433 s1 makes "held" and "not lost" the same fact: "a protected condition is lost exactly when it fails on an occasion it covers".
- In file 10 both turn on the content of \(P\). S72 marks "the full no-loss verdict" SILENT on that ground.
- Even if the points were ruled different, SILENT→SILENT has no direction, so the row could not be a change away.

**Kind.** The ruled marks are equal, so the verdict is SAME and the row is not a theory change. The marks do not differ, so it is not reader variation either. The passage label (CHANGED, additive, on f11 L433 s1 and L514) is right, since both sentences are new (M38, M48). With the verdict SAME it does not change the kind.

**Verdict: UPHELD.** O35 is SILENT→SILENT, SAME, no change. The file-11 SILENT is neither a theory change away nor reader variation. O35 does not fail test (b). The condition in 03 section 6 (line 238) is met, and M38 and M48 are not shown harmful on this row.
- **Recorded for S81 Results.** Claude's pre-registered reading in 01 was file 10 AGREE, and the step-3 reading changed it after the 1K returns were opened. The counted mark does not depend on that change. The rule gives SILENT whenever both 1K returns are SILENT, and S72's and S75's own ground is the one the step-3 reading now adopts. S81 Results should say both things, so that test (b) is seen to rest on the rule.
- The rule is applied evenly. It withholds a change toward the thoughtful person at O18 and O41 (Claude's file-10 reading SPLIT, both kept at the baseline AGREE), and a change away at O35.

---

## 3. O48: The forbidden wire (test (a), P1)

**The ruling** (`rulings - O4 group.md`, lines 487–557). f10 DISAGREE (baseline; 1K A DISAGREE, 1K B SPLIT). f11 AGREE. CHANGED, passage CHANGED (alteration), toward, theory change. P1 HOLDS.

**Attempt 1: file 10 is SPLIT (1K B).** 1K B's point: f10 L210 makes the selected transport "a member of \(\mathcal T\) that survived", so the \(t'\) of the claim may be confined to the population. The ruling answers that "surviving" is only "fidelity on \(H\)". A stronger answer holds on either reading:
- If \(t'\) need not be in \(\mathcal T\): f10 L569 asserts, without condition, that "For every \((a,b)\in C\setminus H\) there exists a transport \(t'\), also surviving on \(H\), with a different value at \((a,b)\)". f10 L573 adds "unconstrained where it was not". The verdict's "The premise is not met" is then a different finding, because the claim has no premise about a population.
- If \(t'\) must be in \(\mathcal T\): f10 L569 then asserts that such a member exists at every unseen pair, which the case contradicts. f10 L539 classes exactly this as a refutation: "A selection history \(H\subsetneq C\) whose survivor is determined on \(C\setminus H\). This refutes Derivation 3." f10 L38 adds "*always*". File 10 then finds a counterexample to its theorem, not an unmet premise.

On both readings, at least one point reaches a different finding. DISAGREE is the first mark rule that fits.

**Attempt 2: file 11 is DISAGREE, because the wired arrangement is imaginable and so admitted (1C B's AGAINST).** This fails.
- f11 L562 s3: "The presence of an unseen pair alone does not establish that such a \(t'\) exists; it must be admitted, realizable, a member of \(\mathcal T\), and a survivor of \(H\)."
- f11 L473: "a transport that would need a part every member of the population is built without is not in it."
- Both fit the case's words ("needs a wire … every device in the stated population is built without that wire").

**Attempt 3: P1 fails because the AGREE rests on L473 (undeclared, M46) rather than on the declared change.**
- L473 excludes the wired arrangement from \(\mathcal T\). Under file 10's claim that exclusion leaves the DISAGREE standing: the claim's \(t'\) need not be in \(\mathcal T\), or, if it must, the case becomes a refutation by f10 L539.
- The verdict's third point needs the antecedent of f11 L562 s2 ("at which some \(t'\in\mathcal T\) … has a different value"). It also needs f11 L564 ("Where \(\mathcal T\) contains no such transport, \(H\) is silent on the value at \((a,b)\) and the population fixes it") and f11 L534 ("a population with no such survivor is the theorem's own qualification, not a refutation").
- The change is carried by the declared sentences, and L473 applies them to the case's words.

**Verdict: UPHELD.** Test (a) holds, and P1 holds. Neither 1K return marks O48 AGREE, so the plan's clause on a file-10 AGREE is not triggered.

---

## 4. The S75 corrections, and the one refused

### O45: The spring nobody mentioned (AGREE → SPLIT). UPHELD.

**The ruling** (`rulings - O2 group.md`, lines 365–425). Both 1K returns mark SPLIT at the same point ("It was already a route."), on f10 L246, and Claude's reading confirms it. Step 4 had already found the same openness at M28, before any 1K return was opened.

**Attempt: file 10 is AGREE.** The case says the account "contains two springs, both connected, both sufficient", and f10 L324 makes each of two sufficient routes "contributory".
- This fails, because file 10 separates what \(E\) contains from what \(\Gamma\) holds. f10 L246: "an organization \(E\), a transport …, and an identified set \(\Gamma\) of active commitments in \(E\)". f10 L304 has a class of components of \(E\) outside \(\Gamma\): "let \(E|W\) retain the commitments in \(W\) with the named background fixed."
- f10 L324's routes are members of \(\Gamma\) ("\(\Gamma=\{a,b\}\)").
- No sentence of file 10 says how \(\Gamma\) is identified. So "contained and connected" does not settle "a route". The reading on which the undescribed spring was named background, and entered \(\Gamma\) only when the author named it, also stands on file 10's sentences, and it reaches a different finding on "It was already a route". The text leaves the choice open, so the mark is SPLIT.
- f11 L309 s3 closes the choice: "A route already present in the candidate is a route whether or not anyone has described its work".

**Residual.** L309 s3's subject ("A route") could be read as presupposing membership in \(\Gamma\). Read so, the sentence says only that description is irrelevant, and that is the reason Reading 2 of file 10 needed. The file-11 AGREE stands.

The direction is toward the thoughtful person on every reading, and the file-11 mark equals S75's, so P2 is untouched.

### O20: Two valves in one second (SILENT → AGREE). UPHELD.

**The ruling** (`rulings - O4 group.md`, lines 237–291). Both 1K returns mark AGREE. 01 had file 10 AGREE before any return was opened, and the step-3 reading confirms it.

**Attempt: file 10 is SILENT.** The argument: f10 L441 names \(\operatorname{ProducedBy}\) and never defines it, so file 10 cannot say who may claim the repair (S72 return 01, line 33). And on single-removal contrasts neither closing has "nonconstant dependence" (f10 L384), so neither route is active.

This fails, because every point of the verdict is reached without a definition of ProducedBy.
- *"Both did something that would have stopped it."* The situation says so: "The records are complete: either valve alone would have stopped it."
- *"Neither can claim it alone."* An exclusive claim is refuted by that record. f10 L324 gives "each is contributory, neither indispensable". f10 L406 gives "missing evidence stays missing".
- *"No way to say whose water stopped."* This follows from the same record and L406.
- On the constant-dependence reading neither closing is active, so neither can claim the repair at all. That still gives "neither … alone".
- S72's own finding is the verdict's: "the record warrants neither exclusive claim". S72's SILENT is "on a further allocation", which the verdict does not claim.
- O39 has the same structure (two sufficient acts, both of which ran), and its baseline is AGREE on the same sentences.

### O40: Two hands on the test (SILENT → AGREE). UNCERTAIN.

**The ruling** (`rulings - O4 group.md`, lines 429–483). Both 1K returns mark AGREE, and 01's two readers had AGREE before any return was opened. The ruling reads "Neither can say 'mostly'" as a point about what either can assert: "a comparison the theory leaves empty is one no one can assert." It records that the SILENT contrary "HOLDS if the point is read as the claim that the two contributions are equal in weight."

**Attempt: file 10 is SILENT by the brief's mark order.** This does not rest on the balance reading.
- f10 L25 does not say that a ranking cannot be had. It says: "It supplies places where such things would go if anyone had them, and marks those places as empty." A "mostly" between two contributors is a ranking. On file 10, whether either can say it is decided by what fills that place, and the case supplies nothing.
- That is mark rule 4's configuration: "the theory leaves the finding open, because it takes the deciding matter as an input the case leaves unstated". The brief takes the first rule that fits, and SILENT comes before AGREE.
- S72 read file 10 so (S72 return 01, line 53): "SILENT on a comparative rule entailing that neither can say mostly".
- 1C B marks its own SILENT contrary "HOLDS: YES" (packet O40, section 6): "the theory's refusal to divide credit can be read either as denying 'mostly' or as leaving it undecided".

**What stands against the attempt.**
- The verdict quotes the word ("can say 'mostly'"), which points to the speech act.
- With the place empty, no party is entitled to fill it. On that reading the theory's verdict is the fixed verdict with the qualification "absent a declared ranking", and the brief's "Same finding" counts that as the same finding.
- Seven readers take this reading: 01's two, both 1K returns, and every file-11 reading.

**Why the row is left open, not overturned.** The two files differ at exactly this point. f11 L27 s3 adds a sentence file 10 lacks: "It does not supply a division of credit among contributors beyond what a history establishes". f11 L433 s4 adds "the history supplies no division of credit that it does not contain". These bind "mostly" to the history rather than to an input place. So a third reading is available: file 10 SILENT (L25, a place an input could fill) and file 11 AGREE (L27 s3, bound to the history). On that reading the row is CHANGED, toward, a theory change through M4 and M40, and S75 is not corrected.

**What it turns on.** Whether f10 L25's "if anyone had them" leaves "Neither can say 'mostly'" to an input (SILENT) or empties it for both parties (AGREE).
- Every reading gives AGREE, SILENT or a change toward. None gives a change away.
- The O21, O27 and O50 SILENT rulings are consistent with all three readings, since those verdicts assert a "mostly".
- The "theirs together" point is not what the row turns on. f10 L414's witness keeps the expert's fix as the expert's binding, which is the same treatment the ruling gives O31. 01's readers found a nontrivial binding in the expert's subhistory as well.

### O15: Sam's inherited marks (both 1K SPLIT; correction refused). UPHELD.

**The ruling** (`rulings - O3 group.md`, lines 213–277). Both 1K returns mark SPLIT on point 3 ("it is a hole in his account"). One reading takes the witness sentence (f10 L414 s2) to put the hole only in the diagrams. The other takes f10 L226 or L406 to put it in his account as well. Claude's reading does not confirm the split.

**Attempt: confirm the SPLIT.** This fails.
- f10 L414 s2 says what a witness identifies: "the controlled processes, the incoming carriers, the bindings constructed, and the resulting representation". It gives point 1 ("his account of his own work is complete").
- It contains no sentence that an account resting on a carrier is complete without the carrier's history. So it yields no finding that the hole is *not* in his account.
- Point 3 is given by f10 L406 ("missing evidence stays missing") together with the active route (f10 L384), on which the arrows lie ("his cut followed them"). It is also given by "relay is not" construction (f10 L414 s3).
- The two 1K readings do not reach different findings on one point.
- The verdict separates "his account of his own work" from "his account". That is how both halves are consistent (1K B's NOTE reads them as one).

Had the SPLIT been confirmed, the row would move toward the thoughtful person, never away.

---

## 5. The rows departing from the majority of the file-11 readings

### O5: Greta's dough. UPHELD, medium. This is the most consequential file-11 ruling.

**The ruling** (`rulings - O1 group.md`, lines 103–153). f11 AGREE against four SILENT readings (1C A, 1C B, Atria on A, Mimo on B) and one AGREE (Atria on B). The file-10 mark is AGREE (baseline; both 1K AGREE). A file-11 SILENT would be AGREE→SILENT, away, through f11 L161 s3 and L514 (M17, M48), and test (b) would fail.

**Attempt: file 11 is SILENT.** The argument rests on f11 L161 s3: "What makes a restriction appropriate to the question asked is a substantive, criticizable part of the claim; the semantics records the restriction and supplies no rule that certifies it." "This is a legitimate narrowing" is a certification, and the semantics supplies none; "the endorsement is the reader's, not the theory's" (1C A, HOLDS).

This fails, on the text.
- L161 s3 puts what makes the restriction appropriate *inside the claim*. Greta's claim states it: "her account says why: the yeast that makes the gas works slowly in the cold" (case book O5).
- f11 L514 lists "what makes a restriction appropriate (Part III)" among the "stated inputs that the semantics records and does not supply". It rules: "A verdict that depends on one of these is a verdict given the input; where the input is missing, the verdict is unsettled".
- Here the input is stated, so the theory gives the verdict given it: the narrowing is appropriate on her stated ground, and open to criticism. The brief's "Same finding" counts a verdict with a qualification as the same finding. The fixed verdict's second sentence ("The limit follows from a part of her account") is that ground.
- "Supplies no rule that certifies it" denies a rule of the semantics' own. It does not deny the verdict given the claim's input, which L514 grants in terms.
- The SILENT reading leaves L514's contrast ("where the input is missing") with no work to do in Part III. It also cannot tell Greta's limit from the Tuesday limit, which the situation sets against it. The ruling tells them apart by whether the input is present: O5 AGREE, O1 SILENT.

**What it turns on.** Whether a verdict "given the input" reaches "legitimate" with a qualification. It is a reading judgment on two new sentences. The wording of L161 s3 invites the SILENT reading: four of five readers took it, and Atria's blind mark was SILENT on A and AGREE on B from one 2a text. The ruling is upheld because L514 is the more specific sentence and speaks to this configuration. It is the row the cross-examination should press first.

### O10: Two thermostats. UPHELD.

**The ruling** (`rulings - O3 group.md`, lines 143–209). f11 AGREE against three SILENT readings (1C B, Atria on B, Mimo on B).

**Attempt: file 11 is SILENT, because every kind-claim is indexed to a contract the case does not state** (f11 L41; L121 "two components of one kind on \(C\) may separate on a finer contract"). This fails.
- "Same make" and "set to" place the difference in a valuation. f11 L93: "A valuation is an element of \(X_D\)". f11 L105: "An edit that sets a port replaces the component assigning that port". f11 L111: "A port \(v\) is an **input** under \(A\) when \(A\) contains an edit that sets \(v\) directly."
- Components whose relations coincide at every pair are one kind on every contract, so the finding does not wait on a contract.
- Emil's difference is a difference of outputs. f11 L171: "contents are not identified by having the same outputs". f11 L558: a claim that two things "really" differ "must supply" a separating admitted change.

**Whatever the answer, not a change away.** The SILENT readings rest on f11 L121 and L41. Their claim is in file 10 at f10 L136 and L35 ("At a finer level with more admitted changes they may separate."), and 02 and both 1D lists rule C24 WORDING. A file-11 SILENT would therefore change the verdict on a passage that is SAME. That is not a theory change. Tester B marks SILENT in both arms.

### O30: The routine uploaded that morning. UPHELD, medium. This is decisive for test (b).

**The ruling** (`rulings - O4 group.md`, lines 295–348). f11 AGREE against two SILENT readings (1C A, Atria on A) and one SPLIT (Atria on B). A file-11 SILENT or SPLIT would be AGREE→SILENT or SPLIT, away, through f11 L419, L465 and L514 (M37, M44, M48), and test (b) would fail.

**Attempt 1: SILENT, because no boundary is declared.**
- f11 L419 s1 grounds ownership in "the system boundary and resource contract declared for \(s\)".
- f11 L419 s2: "where the boundary is drawn decides, not where the process sits in the casing".
- f11 L465: "Both are declared before the attribution, not chosen after it."
- f11 L514: a missing boundary leaves the verdict unsettled.

This fails. f11 L465 defines the boundary as "which processes and resources are the system's", and the situation states that for the process at issue: "The robot compares the pressures itself" (case book O30). The word "itself" is in the situation, not only in the verdict (1C A's HOLDS line misplaces it; its own VERDICT line quotes it from the situation). No boundary consistent with the situation excludes the comparison. Nothing sets a boundary apart from the robot, as O51's declared boundary does or O41's stated robot-only boundary does.

**Consistency with O35.** Under f11 L514, an input is missing where the situation leaves open alternatives that give different verdicts.
- In O35 it does: "the protected tap" fits a condition that holds (supply to anyone who draws) and one that fails (runs at all times).
- In O30 it does not.
- The two rulings apply one standard.

**Attempt 2: SPLIT, because the uploaded routine is "work supplied from outside … however it is executed inside" (f11 L419 s2).** This fails on the same sentence. Its next clause is "a process that runs inside the boundary is the system's own today whoever wrote it". Its examples of outside work are results handed in: "a diagnosis, a decisive question, an instruction about what to read". If writing a process outside made its run outside work, "whoever wrote it" would have no case.

**What it turns on.** Whether the situation's "compares the pressures itself" supplies the boundary input. f11 L419 and L514 are open to the strict reading, and three of five readers took it. The same hazard stands on O17 (section 7). It is recorded for a later revision, as the rulings propose.

---

## 6. The rule applications on the other file-10 marks

Each of these is upheld. The plan's words are "both 1K returns agree on a different mark".
- **O18.** 1K A SPLIT and 1K B DISAGREE are different marks, so the baseline AGREE stands. Claude's SPLIT reading of file 10 is recorded as a finding about S75.
- **O31.** SPLIT and DISAGREE, so the baseline AGREE stands.
- **O41.** SPLIT and AGREE, so the baseline AGREE stands. Claude's SPLIT reading is a finding about S75.
- **O37.** Both 1K returns are AGREE, the baseline. Claude's reading moves to AGREE on f10 L406's indexed receipts ("\(P_j(\phi)\) and \(N_j(\phi)\) are the usable receipts") and L270. The rule gives AGREE either way.

---

## 7. Theory changes away: none ruled. The rows where a reading would have given one

Each reading below would have made its row a change away through a new sentence of file 11. Each fails on the text, and each ruling is upheld.
- **O17** (1C A, Atria on A: SILENT for want of a declared boundary, f11 L419, L514).
  - f11 L467 gives the verdict's contrast exactly: "Ownership is grounded in the processes and resources the boundary includes, never in the capability being attributed".
  - The log shows the process and the manual offers only the capability.
  - The boundary adds at most the qualification "given that the robot's boundary includes the routine". That is the same finding.
  - The same hazard stands as at O30.
- **O13** (Atria's blind DISAGREE through f11 L433 s4, "both are credited"). f11 L371: "A route that started and did no work … is not active for that result". The situation says "Before she can replace it", so only Ben's contribution ran.
- **O19** (Mimo's blind SPLIT through f11 L309 s3). That sentence says a present route is a route "whether or not anyone has described its work". It says nothing on whether the route did work in a history. f11 L309 s2 keeps presence and activity apart: routes "may differ in which routes are active".
- **O50** (1C B's DISAGREE on the discovery, through f11 L419 s2 and L433 s4). The verdict credits "each achievement on its own".
  - The swap proposal belongs to the reinterpretation, which is credited jointly, and to the inquiry.
  - It enters the discovery's subhistory as an incoming carrier, and f11 L401 s5 keeps received content received: "the rest of the content keeps its inherited provenance".
  - O41 differs. There one achievement lay under a stated robot-only boundary.
- **O15, file 11** (1C A's SPLIT through f11 L213 s-last against L393). Both readings put a hole in his account: in the record on one reading, in the receipts on the other. The situation's hole is a hole in the record ("nobody recorded who first drew it"), so the readings do not reach different findings.
- **O32** (1C A's DISAGREE through f11 L606). The sentence is shared word for word with f10 L613, so at most this is reader variation. It concerns inferring account claims "from emitted text", not a record of who said what and when.

---

## 8. CASE DISPUTED: none raised, none ruled. UPHELD.

- No cell of `table.md` carries CASE DISPUTED.
- A search of the seven accepted returns (1C A, 1C B, 1K A, 1K B, 2b Atria on A, 2b Atria on B, 2b Mimo on B) finds no "MARK: CASE DISPUTED".
- 2b Atria on A records, at line 648, "neither reading marked any case CASE DISPUTED".
- No step-3 ruling raises one. Step 6 of the plan has nothing to set aside.

---

## 9. Findings for the orchestrator

1. **Test (b) does not turn on O35.** The plan's rule fixes O35's file-10 mark at SILENT, because both 1K returns are SILENT. The text agrees, on S72's and S75's own ground (the unstated protected condition, "fixed for the comparison", f10 L438). O35 is SILENT→SILENT, SAME, no change.
2. **Test (b) now turns on O5, O30 and O17.** Each file-11 AGREE is upheld on the text, but each stands against a SILENT reading that rests on new sentences (f11 L161 s3 with L514; f11 L419, L465 and L514), and that reading has substantial support among the readers. These three rows should go to the cross-examination first. The revision notes the rulings already record (L161, and L419 with L514) are the repairs that would remove the hazard.
3. **O40's S75 correction is uncertain** (section 4). It does not bear on tests (a) to (d). It changes the count of S75 corrections (three or two), and whether P2's failure at O40 is "by S75" or by a theory change toward.
4. **P2's standing rule names two ways P2 may fail and file 11 still stand**: a theory change toward, or an undeclared CLAIM no case shows harmful. The rulings' phrase "by S75, not by file 11" (O20, O40) is neither. Either way file 11 stands.
   - With the corrections, O20 and O40 are SAME between the files.
   - Without them, both would be SILENT→AGREE theory changes toward, through f11 L433 s4 and L27 s3 (M40, M4), which the saving clause names.
   - S81 Results should say which reading it takes.
5. **One sharpening of the O48 ruling.** The answer to 1K B's SPLIT does not need the point that \(t'\) lies outside \(\mathcal T\). On either reading of f10 L569, file 10 reaches a finding different from "The premise is not met". If \(t'\) may lie outside \(\mathcal T\), the claim has no population premise. If \(t'\) must lie inside it, f10 L539 makes the case a refutation of Derivation 3.
