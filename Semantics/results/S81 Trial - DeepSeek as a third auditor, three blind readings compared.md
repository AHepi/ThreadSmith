# S81 Trial - DeepSeek as a third auditor, three blind readings compared

23 September 2026. The question: should DeepSeek sit beside Atria and Mimo as a third outside auditor? The owner's condition was "If it actually catches valid holes. It's the least intelligent of the three." This report decides the question on the evidence of one blind reading per model. No API calls were made for it.

## Verdict

**DO NOT ADD.** The owner's condition is not met. DeepSeek reported **no holes at all** in file 11. Its "Noticed beyond the cases" section reads `COUNT: 0`. Nothing in its per-case OPEN and SPLIT fields raises a valid hole that the other two missed either. On the same brief, Mimo found 6 valid holes (5 found by no other reader) and Atria found 2 (1 found by no other reader).

DeepSeek did well on the cases themselves. It matched 43 of 52 fixed verdicts, departed outright on none, and misread the theory 3 times. That is second of the three, behind Mimo. But it is never the only reader to get a row right, so as a verdict checker it adds cost and nothing that Mimo does not already supply. Its reasoning trace shows why the hole count is zero. It weighed one candidate hole (the ownership tension that Atria reported) and set it aside: "Need not invent... I can choose count 0." Its weakness here is silence, not invention. That makes its invalid-claim rate trivially tolerable, and it also makes it useless for the job the owner named.

Headline numbers:

| | DeepSeek | Atria | Mimo |
|---|---|---|---|
| Cases matching the fixed verdict in substance | **43** | 42 | **46** |
| Partial (reaches part, or leaves open what the verdict settles) | 9 | 7 | 4 |
| Outright departures | 0 | 3 | 2 |
| Departures or partials that misread the theory | 3 | 6 | 2 |
| Holes reported in "Noticed beyond the cases" | 0 | 6 | 8 |
| of which VALID / JUDGEMENT / INVALID | 0 / 0 / 0 | 2 / 1 / 3 | 6 / 1 / 1 |
| Valid holes no other reader found (all sources) | **0** | 1 | 6 |
| Quotations checked / altered in words (not only escaping) | 101 / 4 | 108 / 0 | 109 / 2 |

## What was compared

- **Brief.** All three readers received the same text: `S81 File 11 against every case - outputs/briefs/s81_2a_atria.txt`. Its SHA-256 is `a2cef715…4b6963`, and the three receipts' `user_sha256` values match it, as does the message body of the DeepSeek request. The brief holds the task, file 11 minus its revision note (checked by diff, with no other difference), and the 52 situations with their verdicts cut.
- **Returns.** Atria: `returns/s81_2a_atria.response.txt`. Mimo: `returns/s81_2a_mimo.response.txt`. DeepSeek: `trial - DeepSeek as a third auditor/s81_2a_deepseek.response.txt` (deepseek-v4-pro, thinking on, temperature 0.7, finish `stop`, 37,408 reasoning tokens).
- **Fixed verdicts.** `tests/S81 Case book - the 52 cases, situations and fixed verdicts, as the tested agent sees them.md`.
- **Theory.** `authority/11 Claude Fable Semantics - standalone theory, revision 1.md`. Every quotation below is from it.

**Scoring.** The brief asks what the theory finds, not what the thoughtful person would say. So a row is scored **M** when the reading reaches the fixed verdict's finding in substance, conditions and all. It is scored **P** when the reading reaches part of the finding, or leaves open something the verdict settles, without contradicting it. It is scored **D** when the reading contradicts the verdict. Every P and D row is also marked **d** (a defensible reading of the theory's text) or **x** (a misreading of the theory's text or of the situation).

## 1. Per-case table

Columns: DeepSeek | Atria | Mimo.

| Case | DS | At | Mi | Note |
|---|---|---|---|---|
| O1 forecaster | P d | P d | P d | None of the three reaches "no explanation... a retreat". The theory "records the restriction and supplies no rule that certifies it" (Part III). |
| O2 tide and bell | M | M | M | |
| O3 Nadia | M | M | M | |
| O4 somnic index | M | M | M | |
| O5 dough | M | M | M | |
| O6 thermometer | M | M | M | Atria's signature reasoning is muddled, but its conclusion is right. |
| O7 salt | M | M | P d | Mimo leaves the account status open despite the spread and sweep contrasts. |
| O8 ovens | M | M | M | |
| O9 float | M | M | M | |
| O10 thermostats | P d | P x | P x | All leave it contract-relative. Atria and Mimo get the kind mechanics wrong (see §2). |
| O11 three locks | M | M | M | |
| O12 rota | P d | P d | P d | "Merit is real" is not given by the theory: "That a question was found says nothing about its worth" (Part XVI, Derivation 5). |
| O13 two plumbers | M | **D x** | M | Atria credits Ana's account as a second sufficient route. |
| O14 phrasebook | M | M | M | |
| O15 inherited arrows | P x | M | M | DeepSeek calls "unrecorded" "declared". |
| O16 diary | M | M | M | |
| O17 log and manual | M | M | M | |
| O18 one tooth | M | M | M | |
| O19 diagram in hand | M | M | M | |
| O20 two valves, one second | M | M | M | |
| O21 expert's question | M | M | M | |
| O22 two knobs | M | **D x** | M | Atria says the lead is not represented under joint turns. |
| O23 seal | M | M | M | |
| O24 unused joint setting | M | P x | M | Atria confuses the tested history with the contract. |
| O25 one second apart | M | M | M | |
| O26 two feeds | M | M | M | |
| O27 test fitted neither | M | M | M | |
| O28 card nobody can read | M | M | M | |
| O29 margin note | M | M | M | |
| O30 uploaded routine | M | P x | M | Atria reads a tension that the sentence itself resolves. |
| O31 wrong valve | M | M | M | |
| O32 found aloud, drawn later | P x | M | M | DeepSeek calls the drawing of the bypass "relay". |
| O33 table with empty columns | P d | **D x** | M | Atria: "not a contract on which an account can be claimed". |
| O34 second compartment | M | M | M | |
| O35 four seconds | P d | P d | **D x** | Mimo asserts a loss using an occasion the situation never states. |
| O36 premise P | M | M | M | |
| O37 uncited textbook | M | M | M | |
| O38 job sheet | M | M | M | |
| O39 two routes, both running | M | M | M | |
| O40 two hands | M | M | M | |
| O41 whisper | M | M | M | |
| O42 new board | M | M | M | |
| O43 mirrored marks | M | M | M | |
| O44 half from the shelf | M | M | M | |
| O45 spring nobody mentioned | P x | M | M | DeepSeek brings Part IX activity into a question about Part VI candidates. |
| O46 cable | M | M | M | |
| O47 one more commitment | M | M | M | |
| O48 forbidden wire | M | M | M | |
| O49 owned means capable | M | M | M | |
| O50 three achievements | P d | P d | D d | None assigns all three credits. Mimo calls the discovery "mixed". |
| O51 module in casing | M | M | M | |
| O52 route that stopped | M | M | M | |
| **M / P / D** | **43 / 9 / 0** | **42 / 7 / 3** | **46 / 4 / 2** | |

Three rows are partial for all three readers: O1, O12 and O50. So is O35, where Mimo departs outright. On O1, O12 and O35 the fixed verdict asks for something the theory's text withholds on purpose: a certificate for a restriction, a judgement of worth, or an occasion that the situation does not state. These are rows about the theory or the verdict, not about the readers.

## 2. The departures and misreadings, checked against file 11

### DeepSeek

- **O15, P x.** DeepSeek says the arrow's provenance is unrecorded, "so its correspondence is only declared". But provenance is fixed by history, not by the record: "A transport \(t\) between organizations of a physical system has exactly one of three provenances, determined by its history in the physical module" (Part IV). A transport is declared when it is "entered into the model by its author" (Part IV, **Declared.**). A missing record leaves the provenance unsettled, not declared: "where the input is missing, the verdict is unsettled and the semantics says so" (Part XIV). DeepSeek's own OPEN line concedes this ("whether the arrow actually had a selected or constructed provenance that was not recorded"). It still reaches the verdict's main point, that the gap carries into Sam's cut.
- **O32, P x.** DeepSeek calls the second engineer's drawing "a content-preserving transfer or relay, not the origin". But what was said aloud was a dependence (pressure on the second pump), and what was drawn was a bypass, which is a different content. Build excludes only what "is not a composition of content-preserving transfers" (Part X). DeepSeek misreads the situation, and so loses "the bypass by the one who drew it".
- **O45, P x.** DeepSeek splits the case on whether the second spring was "active" in the Part IX sense. Part VI settles the question directly: "A route already present in the candidate is a route whether or not anyone has described its work". Part IX's "active route" is "a connected subnetwork of actual occurrences" in a history, while O45 concerns the contents of an account. (Whether "route" means the same thing in Parts VI and IX is a real question of wording. See hole J-4.)
- **Defensible partials.** On O1 and O12, see the note under the table. On O10, its conditional ("If the two thermostats have the same signature... and differ only in setpoint or state, they are one kind") is correct, and it is the only O10 reading without a mechanical error. On O33, it leaves open whether the single-knob exclusion is stated. On O35, it gives a conditional that leans toward a loss while noting that "if it protects only water availability... the finding may differ". On O50, it keeps the three achievements apart without assigning them.

### Atria

- **O13, D x.** Atria writes: "Both contributions ran, so both are credited". That treats Ana's diagnosis as a second sufficient route to the repair. But Ana never acted. "\(\operatorname{ProducedBy}\) holds when an active route (Part IX) runs from \(\Delta\) to the repair" (Part XI). The theory names this exact case: "A correct account that produced nothing, an act that repaired without an account, and a repair produced through use of an account are three different attributions." (Part XI)
- **O22, D x.** Atria says the lead "becomes representable only when the contract admits finer temporal or single-knob edits". But ports can carry time courses: "Values of ports may be paths, functions, fields, proofs or histories." (Part II). So the lead belongs to the answer to the joint question, as the verdict says.
- **O33, D x.** Atria says the joint-turn contract excludes "the very changes under which the active commitments could matter", so the table is "not a contract on which an account can be claimed". But the joint turns themselves change the answer. Non-vacuity rules out only a contract "excluding *every* change under which the active commitments could matter" (Part V), and Lea's joint question is a different question from any single-knob one ("Two questions with the same \(D\) and different \((C,\mathcal Q)\) are different questions", Part III). The reading also contradicts Atria's own O22, where it said "Lea's question admits only joint turns".
- **O24, P x.** Atria says the two arrangements "are one account at that grain" on the tested history, and that the reachable setting is "a finer contract... a new question". That confuses the history with the contract. The theory has "a finite history \(H\subseteq C\) of edit–boundary pairs actually encountered" (Part IV) and \(H\subsetneq C\) (Derivation 3), and a physically admitted edit leaves the contract only "by a stated scope, not silently" (Part V). The setting is reachable and nothing excludes it, so it is already in \(C\).
- **O30, P x.** Atria splits the case, saying that the routine is and is not the robot's own. But the sentence it quotes resolves the question: "a process that runs inside the boundary is the system's own today whoever wrote it" (Part X). An uploaded routine is exactly the "whoever wrote it" case. The fixed verdict says the same: the robot owns today's history, and the person owns the routine's origin.
- **O10, P x.** Atria writes: "on a contract containing the set-point edit the two thermostats have different signatures". An edit that sets a set-point acts alike on both devices, so it cannot separate them under (K), which reads "\(\operatorname{sig}_C(j)=\{(a,b,L_j(a,b)):(a,b)\in C\}\)". The 18/22 difference is a state or a parameter, fixed by how the organization is written, not by adding that edit.
- **Defensible partials.** O1, O12, O35 (conditional on "whether 'at all times' covers those seconds"), and O50.

### Mimo

- **O35, D x.** Mimo writes: "it failed on an occasion the condition covers... so the protection was lost". But O35 states no occasions. The "at all times" wording belongs to O38. The theory takes the occasions as a declared input: "each as a stated condition over stated occasions" (Part XI). Without that input, "the verdict is unsettled and the semantics says so rather than choosing the input from the verdict wanted" (Part XIV). Mimo's own OPEN line asks the question that its finding had already answered.
- **O10, P x.** Mimo says that on a contract with no setting change, "the signatures separate and Emil's two-kind finding stands". That runs against the theory's monotonicity: "a coarser contract identifies more components, and two components of one kind on \(C\) may separate on a finer contract" (Part II). Removing edits cannot separate components.
- **O50, D d.** Mimo calls the discovery "mixed, since the expert proposed the swap". The verdict gives the discovery to the robot. Mimo's reading is defensible on "Work supplied from outside that boundary... remains an outside contribution however it is executed inside" (Part X).
- **Defensible partials.** O1 and O12. On O7 it hedges too much, but it does not contradict the verdict.

## 3. Every hole reported, verified against file 11

### 3a. "Noticed beyond the cases" (the explicit list)

**DeepSeek: none.** `COUNT: 0`, with one empty bullet.

**Atria: 6 reported.**

| # | Claim | Class | Evidence from file 11 |
|---|---|---|---|
| A1 | The tag (E) collides with the organization variable \(E\) | JUDGEMENT | The tag is always written in parentheses, "(E)", and the variable never is. No reference is actually ambiguous. A stronger collision exists that Atria did not name: Part XV's attack labels "**(A) Sufficiency.**", "**(B) Necessity.**", "**(D) Genesis.**" and "**(E) Question-finding.**" reuse the equation tags (A), (B), (D) and (E), and Part 0 cites both kinds of label in the same style ("(D) the two provenances"). |
| A2 | Tags run (I1), (I2), (I4), with no (I3) | **VALID** | Part VII: "...\(|f[Z_y]|=1\). (I1) ... for some \(\bar f\). (I2) For linear \(A\) ... \(\ker A\subseteq\ker c^\top\). (I4) Repeating rows changes no kernel". The string "I3" appears nowhere. A minor labelling gap. |
| A3 | \(S_a\) and \(T_a\) undefined in Functional transport | **VALID** | Part VIII: "If \(\pi\circ S_a=T_a\circ\pi\) for every generator \(a\)". Each symbol appears once in the file, and "generator" is also used only there. A transport is "\(t=(\pi,\tau,\sigma,\lambda)\)" (Part IV), with no \(S\) or \(T\). |
| A4 | Part X's "however it is executed inside" pulls against Part XII's "whoever wrote it", and nothing says which governs an uploaded routine | INVALID | The same Part X sentence answers it: "...remains an outside contribution however it is executed inside; a process that runs inside the boundary is the system's own today whoever wrote it". The outside examples are contents ("a diagnosis, a decisive question, an instruction about what to read"). The running process is the system's own, and its authorship stays an outside fact, which is exactly O30's fixed verdict. Drafting note: one clause saying that the two halves assign different things (process ownership, content credit) would stop the misreading. |
| A5 | "(Part II, Derivation 1)" in Part 0 points to the wrong Part | INVALID | This is the document's two-pointer citation style, "Part II **and** Derivation 1". The same paragraph group has "(Part III, Derivation 5)", and Derivation 5 is also in Part XVI. Part II ("Kinds are edit-signatures") is the right Part for the kind claim. |
| A6 | Non-circular dependence does not say whether the edit is required, or whether it constrains contracts or candidates | INVALID | It is an existence conjunct of (E): "There exists \((a,b)\in C\) that removes or replaces a nonempty block of \(\Gamma\)...". Non-vacuity states the contract side: "A contract ... excluding every change under which the active commitments could matter to \(\mathcal Q\), does not satisfy non-circular dependence and is therefore not a contract on which an account can be claimed." (Part V). The real defect in this sentence is a different one, M3. |

**Mimo: 8 reported.**

| # | Claim | Class | Evidence from file 11 |
|---|---|---|---|
| M1 | "A criticism occurrence can exist when (K1) fails" is in tension with "An adverse signal is not a criticism until an organization represents how it bears" | JUDGEMENT | The two are reconciled if "represents how it bears" means the *alleged* connection: "A criticism has target \(z\), alleged defect \(\delta\), grounds \(g\), and a connection" (Part IX). (K1) is whether that connection is an Account. The wording invites the reading Mimo gave. |
| M2 | In (K1), \(\mathcal E_c\) is never defined, and \(p\) does not appear on the right-hand side | **VALID** | "\(\operatorname{Bearing}(c,z,p)\iff\operatorname{Account}(\mathcal E_c,p_\delta)\)" (Part IX). \(\mathcal E_c\) occurs once in the file. Neither \(p\) nor \(z\) occurs on the right, and only \(p_\delta\) ("the question about the defect") is defined. |
| M3 | Non-circular dependence has an edit in \(C\) (over the target \(D\)) act on \(\Gamma\) (commitments in \(E\)) without saying which organization it acts on | **VALID** | "The **contract** \(C\subseteq A\times B\)" is over \(D\)'s edits (Part III). "an identified set \(\Gamma\) of active commitments in \(E\)" (Part V). Then "There exists \((a,b)\in C\) that removes or replaces a nonempty block of \(\Gamma\) while preserving the *other* boundary conditions". So a \(D\)-edit is said to act on \(E\)'s commitments, with no \(\tau\), and "other boundary conditions" treats blocks of \(\Gamma\) as boundary conditions. This is the defining clause of the condition that decides O2, O5 and O33. |
| M4 | \(\equiv_\ell\) in (N) is undefined | **VALID** | "\(\operatorname{New}(s,c,h,e)\iff\neg\exists d\in R_{<e}(s,h),\ d\equiv_\ell c.\)" (Part X) is the only occurrence. Derivation 2 gives an identity "at grain \(C\)", a contract, not \(\ell\). Newness, and so (G) and (EK), rest on it. |
| M5 | "exactly one of three provenances" is in tension with "Construction may operate on selected material" and "A physical system may exhibit both" | INVALID | A transport built by an episode from selected material is **Constructed**: "There is an episode (Part X) whose construction witness prepares \(t\)" (Part IV). "A physical system may exhibit both" is about systems, not about one transport. Mixed content is handled per binding: "construction of that binding, and the rest of the content keeps its inherited provenance" (Part X). |
| M6 | Derivation 2's proof does not show that two different candidates' components match each other | **VALID** | Claim: "their components are pairwise of one kind on \(C\)". Proof: "Immediate from Derivation 1 and (A). ∎". Derivation 1 only pairs each component with *its own* anchor ("every active component \(k\) of \(E\) has the same signature ... as its anchor \(\lambda(k)\)"). Two candidates with different \(\lambda\), or different numbers of components, are not paired by anything shown. The claim needs shared anchors or a further argument. Part XV lists "Derivations 1–3 under their stated assumptions" as refutable, so this is load-bearing. |
| M7 | \(S_a\), \(T_a\) undefined | **VALID** | Same as A3. |
| M8 | \(\mathsf{Admit}^{q,r}_\Theta\) and \(\mathsf{Poss}_\Theta\) undefined | **VALID** (in part) | "\(\mathsf{Cap}^{q,r}_\Omega(\xi)\subseteq\mathsf{Admit}^{q,r}_\Theta\); \(\mathsf{Cap}^\infty=\bigcap_{q,r}\mathsf{Cap}^{q,r}\subseteq\mathsf{Poss}_\Theta\)" (Part XII). \(\mathsf{Admit}\), \(\mathsf{Cap}\) and the grades \(q,r\) are defined nowhere. \(\mathsf{Poss}\) can be read off "Possibility is the absence of a law-imposed limit short of perfection on performance and retention" (Part XII, Tasks), so that half is weak. |

### 3b. Theory-level claims made inside OPEN and SPLIT lines

The brief's OPEN field invites "the words looked for", so readers also raised gaps there. Only claims about the theory are listed. Remarks that the situation fails to state something are left out.

| Reader, case | Claim | Class | Evidence |
|---|---|---|---|
| Mimo O2 | Same as M3 | VALID | See M3 above. |
| Mimo O3, O11, O18, O27, O31 | \(\equiv_\ell\) undefined | VALID | Same as M4. |
| Mimo O13 | \(\Delta\) in ProducedBy "is never typed" | **VALID** | \(\Delta\) appears only as an argument of \(\operatorname{Repair}_{O,P}(\xi,\xi';\Delta)\), CreateEK and \(\operatorname{Result}(\Delta)\) (Part XI). \(\operatorname{Result}\) and \(\operatorname{ProducesVia}\) each occur once, undefined. |
| Mimo O4 | Whether recalibration is an observation edit or an edit to the measuring relation; the word "calibration" is absent | INVALID | "A port is an **observation** when \(A\) contains an edit that alters the relation reporting it without altering what it reports" (Part II). Recalibration is that edit. |
| Mimo O5 | "relabelings" undefined | JUDGEMENT | It occurs once (Part V). The ordinary sense, plus "structure-preserving bijections" (Derivation 8), is probably enough. |
| Mimo O15 | There is no fourth status for an unrecorded provenance | INVALID | Provenance is fixed by history ("determined by its history in the physical module", Part IV), and a missing input leaves the verdict "unsettled" (Part XIV). No fourth status is needed. |
| Mimo O20 | "would have" and "sufficient" undefined: are they history evidence or counterfactual? | JUDGEMENT | "sufficient" occurs once ("where two sufficient contributions both ran", Part XI). The active route is defined by "nonconstant dependence ... under the declared contrasts" (Part IX), which lets the reader supply the counterfactual. |
| Mimo O30 | Is an uploaded routine "work supplied" or an enabling condition? | INVALID | As A4: "whoever wrote it". |
| Mimo O33 | Are columns that no edit varies ports at all? | INVALID | "No role assignment is supplied. A port \(v\) is an **input** under \(A\) when \(A\) contains an edit that sets \(v\) directly." (Part II). A port that no edit sets is simply not an input. |
| Mimo O38 | Whether an interruption nobody exercised is a loss | INVALID | "a protected condition is lost exactly when it fails on an occasion it covers" (Part XI). The stated occasions decide. |
| Mimo O40 | No rule for a binding prompted outside but built inside | INVALID | "Work supplied from outside that boundary, a diagnosis, a decisive question, an instruction about what to read, remains an outside contribution however it is executed inside" (Part X). |
| Mimo O41 | "robot-only" and "assessment" have no index | INVALID | Boundary \(\beta\) is a declared index (Part XIV), "declared before the attribution, not chosen after it" (Part XII). |
| Mimo O42 | Repair acts by another hand are unclassified | JUDGEMENT | "A replaced part that preserves the declared continuity leaves the same system" (Part XII) settles identity. Whether the fitting is outside *work on the task* is not addressed. |
| Mimo O45 | Does an undescribed commitment enter \(\Gamma\)? | INVALID | "A route already present in the candidate is a route whether or not anyone has described its work" (Part VI). |
| Mimo O50 | One origin relation cannot handle three achievements | INVALID | (G) is a relation instantiated per content \(c\), and nothing limits the number of instances. |
| DeepSeek O45, Mimo O19 (SPLITs) | "route" in Part VI against "active route" in Part IX | JUDGEMENT (J-4) | Part IX defines only "An **active route** is a connected subnetwork of actual occurrences...". Part VI's "route" (a member of a support) is undefined and is read by example. Both readers used it to split a case the verdict settles. |
| DeepSeek O48 (OPEN) | The stated population "may itself be a declared restriction that needs statement" | INVALID | "The population is the set of transports the physics and the stated construction admit" (Part XII). The restriction is part of the stated construction. |
| Atria O30, O40 (SPLITs) | The ownership tension | INVALID | As A4. |

### 3c. Tally of holes

| | DeepSeek | Atria | Mimo |
|---|---|---|---|
| Explicit list: VALID / JUDGEMENT / INVALID | 0 / 0 / 0 | 2 / 1 / 3 | 6 / 1 / 1 |
| Explicit list: share invalid | n/a (nothing claimed) | 50% | 12.5% |
| Embedded claims: VALID / JUDGEMENT / INVALID (distinct, excluding repeats of the explicit list) | 0 / 1 / 1 | 0 / 0 / 0 | 1 / 3 / 8 |

## 4. Valid holes found by one reader only

- **DeepSeek: none.** It found no valid hole, shared or unique.
- **Atria: 1.** A2, the missing (I3).
- **Mimo: 6.** M2 (\(\mathcal E_c\) and the unused \(p\) in (K1)), M3 (the non-circular clause mixes \(D\)-edits and \(E\)-commitments), M4 (\(\equiv_\ell\)), M6 (the gap in Derivation 2's proof), M8 (\(\mathsf{Admit}\), \(\mathsf{Cap}\), \(q,r\)), and the embedded \(\Delta\)/\(\operatorname{Result}\)/\(\operatorname{ProducesVia}\) typing gap.
- **Shared: 1.** \(S_a\), \(T_a\) (A3 = M7), found by Atria and Mimo.

The most serious are M6 and M3. M6 is a proof gap in a derivation that Part XV exposes to refutation. M3 is a type error in the defining clause of one of the four conditions of Account. Mimo alone found both.

Found by no reader while verifying (for the record, not scored): the attack labels (A), (B), (D) and (E) collide with the equation tags (A), (B), (D) and (E) (see A1). "Enable" in (U1) and (U2) is undefined. \(\mathsf{Cap}^{q,r}\) is never defined from Can.

## 5. Verdict in full

**Does DeepSeek catch valid holes the other two miss?** No. On this evidence it caught none, unique or shared. Its only theory-level remarks were an invalid one (O48) and a matter of judgement that it turned into a wrong split (O45). Its reasoning trace (`s81_2a_deepseek.reasoning.txt`) shows it chose silence deliberately. It considered the Part X/XII ownership sentences, judged them "reconciled by boundary", and wrote `COUNT: 0` because it "need not invent". On that one item it was right and Atria was wrong. But restraint that never produces a valid hole does not meet the owner's condition.

**Is its rate of invalid claims tolerable?** Yes, trivially: it made no explicit claims. Tolerability is not the constraint here. Yield is.

**As a verdict reader** it scored 43/52, with no outright departures and 3 misreadings. That is respectable, and better than Atria's 6 misreadings. But it is below Mimo (46/52, 2 misreadings), and it is never the only reader right on a row. O10 is its best row, and even there it only avoids the others' mechanical errors without reaching the verdict. As a third verdict reader it would add cost without adding coverage.

**Recommendation: DO NOT ADD.** A narrow role was considered: DeepSeek as a verdict tie-breaker, or as a low-noise second opinion on disputed rows. It is not recommended, because Mimo already covers that ground better on the same evidence. One qualification. This is one run on one document. In S80, DeepSeek *mentioned* all 9 planted errors (unmarked mentions, not findings) when the task was to hunt planted errors. It may find holes when the brief makes hunting the whole job, rather than an optional closing section. That would be a separate trial, and it is not evidence under the owner's condition as it stands.

**Atria and Mimo on the same evidence.** Mimo is the stronger auditor here on every count except quotation care:
- 46 against 42 verdict matches, and 2 against 6 misreadings.
- 6 against 2 valid holes, 5 against 1 of them unique, and 1 against 3 invalid explicit claims.
- Atria's invalid claims are the kind an auditor must not make. It reported a cross-reference style as a wrong reference (A5), and read a tension into a sentence that resolves it (A4). That second misreading then drove its O30 and O40 splits.
- Mimo's weaknesses are over-hedging (O7), and a loose OPEN field that raises many non-holes (8 invalid embedded claims) alongside its real ones.
- Atria's quotations are the most exact: none altered in words, with its 7 mismatches being escaping or tags. Mimo altered 2 in words: one splice and one dropped word. DeepSeek altered 4, all the same splice: Part X's "the system's own today" pasted into the Part XII sentence, which reads "the system's whoever wrote it". Its other 2 mismatches are dropped bold marks.
