# S81 step 4, adversarial verification of the rulings

**What this is.** A check of the step-4 rulings in `rulings R1.md`, `rulings R2.md` and `rulings R3.md` (this folder). The places checked were selected by five criteria, listed below. For each place I tried to refute the ruling from the texts of file 10 and file 11, quoting by line. Each place gets one verdict: UPHELD, OVERTURNED (with the correct ruling) or UNCERTAIN (with what it turns on). A claim difference is any change in what is asserted, in its scope, conditions, quantifiers or definitions, or in what follows from it. Written by Claude, 23 September 2026.

**Opened.**
- `alignment.md`, `rulings R1.md`, `rulings R2.md` and `rulings R3.md`, all in full.
- File 10 and file 11, both in full, plus a `grep` of both for "blind", "episode" and "preserve".
- Claude's pre-reading (determination/02), in full.
- Tester A's 1D list: records D1–D15, D20–D22, D31–D34, D47, D57–D61, and every closing section.
- Tester B's 1D list: records D1, D4, D5, D10, D12–D15, D19, D20, D30, D34, D47, D59, D61–D63, D72, and every closing section.
- The 2D returns of Atria and Mimo:
  - their Part 1 records for A's D13, D14, D20, D21, D30, D34, D47, D57, D59, D60 and D63, and for B's D13, D20, D21, D30, D47, D57, D59, D60 and D63;
  - Part 2, the missed differences, and the cross-references.
- The S81 plan, second version: a `grep` for P3, E1 and (d), with lines 115–166.
- The case book: O11, O35, O38 and O47, and a `grep` for "guess", "bad reason" and "blind".
- Claude's case rulings (determination/01): a `grep` for O35.

**Not opened.** Any 1C, 1K, 2a or 2b return, any reasoning file, any receipt, the effort-controls folder, the sample JSONs, `stage1/` and any table. Also not opened: the `master` files, the briefs, raw readings 02a and 02b, and the plan's third version.

---

## Selection

| criterion | places |
|---|---|
| (a) The ruling differs from Claude's pre-reading | M5 (in form), M24, M27 |
| (b) Ruled WORDING or ORDER, but A, B, Atria-2D or Mimo-2D said CLAIM | M2, M6, M9, M10, M11, M15, M16, M27, M51 |
| (c) Ruled CLAIM, but two or more of those four said WORDING or ORDER | none (see below) |
| (d) The named places | Derivation 3 and its three sentences: M8, M12 (the L63 short form, as the other referent of "attack point (D)"), M52, M53, M54, M55, M56. The occasions clause: M38. Declared inputs: M48. |
| (e) Cross-references ruled other than CORRECT | XR1–XR7 |
| Added | NEW-XR1. It is ruled CORRECT, but the ruler marks it uncertain, and A, B and Mimo call it wrong. |

- **Criterion (c) selects nothing.** No place ruled CLAIM has two WORDING or ORDER marks among A, B, Atria and Mimo.
  - The nearest is M43, where Atria alone says WORDING.
  - The other near case is M42 s3, where B alone says WORDING. The ruler agrees that s3 alone is WORDING.
- **Total selected:** 28 (20 master places and 8 cross-references).

---

## Verdicts

| # | place | selected by | ruling | verdict |
|---|---|---|---|---|
| 1 | M2 (C3), "blind variation … history of predictions" | b | WORDING (borderline) | UPHELD |
| 2 | M5 (C9a), \(\mathcal N\) "wherever a question invokes worth" | a | CLAIM, the same change as M47 | UPHELD |
| 3 | M6 (C9b), indices, "Everything else is derived", "appears anywhere" | b | ORDER | UPHELD |
| 4 | M8 (C13), Grievance 3 | d | CLAIM, declared | UPHELD |
| 5 | M9 (C15), Grievance 5 drops "not about whether it is right" | b | WORDING | UPHELD |
| 6 | M10 (C19), Grievance 9 drops "hypothesis/stipulation" | b | WORDING | UPHELD |
| 7 | M11 (C20), Grievance 10 "can change" → "change" | b | WORDING | UPHELD |
| 8 | M12 (C22), the L63 (D) short form | d | ORDER | UPHELD |
| 9 | M15 (C28), "a stated scope is what makes it one" | b | ORDER | UPHELD |
| 10 | M16 (C29), the scoped account and the post-failure narrowing | b | ORDER | UPHELD |
| 11 | M24 (C41 s1), "satisfies (E)" → "does not exclude" | a | CLAIM (narrowed) | UPHELD |
| 12 | M27 (C44), the monotone theorem's reach | a, b | ORDER | UPHELD |
| 13 | M38 (C56), the occasions clause | d | CLAIM | UPHELD |
| 14 | M48 (C66), Declared inputs | d | CLAIM | UPHELD |
| 15 | M51 (C71), (B) Necessity | b | ORDER | UPHELD |
| 16 | M52 (C73), (D) Genesis | d | CLAIM in limb 1; limbs 2–3 ORDER; declared | UPHELD |
| 17 | M53 (C75), the Derivation 3 title | d | CLAIM, declared | UPHELD |
| 18 | M54 (C76), the Derivation 3 Claim | d | CLAIM, declared | UPHELD |
| 19 | M55 (C77), the Derivation 3 Proof | d | CLAIM, declared | UPHELD |
| 20 | M56 (C78), the Derivation 3 Consequence | d | CLAIM, declared | UPHELD |
| 21 | XR1, L5, the note's list of three sentences | e | SLIP | UPHELD |
| 22 | XR2, L5, "the audit's case O48", "(Semantics results S75)" | e | SLIP, with a steering flag | UPHELD |
| 23 | XR3, L27, "(Parts XI, XIV)" | e | SLIP | UPHELD |
| 24 | XR4, L275, "(the bell does not explain the tide)" | e | SLIP, with a steering flag | UPHELD |
| 25 | XR5, L447, "(Part XIV)" | e | SLIP | UPHELD |
| 26 | XR6, L588, "By the dependence order of Part XIV" | e | SLIP | UPHELD |
| 27 | XR7, L616, "Derivation 3's qualification seen from the other side" | e | SLIP | UPHELD |
| 28 | NEW-XR1, L620, "(Derivation 2)" | added | CORRECT (loose); not CLAIM-CHANGING | UPHELD |

**Counts:** UPHELD 28, OVERTURNED 0, UNCERTAIN 0.

Five rulings are upheld although part of their supporting reasoning needs correction: M5, M11, M48, M51 and XR1. The corrections are listed at the end. None changes a ruling.

---

## Details

Line numbers are each file's own. "f10" is file 10 and "f11" is file 11.

### 1. M2 (C3). WORDING, borderline. UPHELD.
- **The change.**
  - f10 L13: "*selected* — produced by blind variation and survival on a history of predictions — or *constructed* — produced by an episode of conjecture and criticism".
  - f11 L15: "*selected*, produced by variation and survival on a history of encountered changes; or *constructed*, produced by an episode of conjecture and criticism".
- **The refutation tried.** "blind" occurs only at f10 L13 (`grep`). If "blind" puts a condition on the variation operator \(\mu\), such as excluding steered variation, then file 11 drops a condition. That is the TEST that A and B give.
- **Why it fails.**
  - File 10's own sentence pairs "blind variation" with "conjecture", and "survival" with "criticism".
  - The body defines conjecture's mark as a represented target: "in which \(t\), or the organization it targets, is available as a represented target" (f10 L212 = f11 L199).
  - The body states the contrast exactly, in the same words in both files: "a selected transport has no represented target and no criticism in its history; a constructed one has both" (f10 L216 = f11 L203); "No member of the history represents \(t\), \(H\), or the survival condition" (f10 L210 = f11 L197).
  - So "blind" in f10 L13 is a gloss of non-representation, which file 11 keeps.
  - "History of predictions" and "history of encountered changes" both gloss the body's \(H\), "edit–boundary pairs actually encountered", which is word for word the same in both files.
- **What would overturn it.** Reading "blind" as a restriction on \(\mu\) beyond non-representation. Neither body supports that reading.
- **Harm.** O11's verdict, "Monday is blind fitting", is reached through L216/L203 under both files. No case moves.

### 2. M5 (C9 part a). CLAIM, counted with M47. UPHELD.
- **The change.**
  - f10 L519: "The **normative relation** \(\mathcal N\), when a question invokes one."
  - f11 L33 s1: "taken as an input wherever a question invokes worth".
- **The refutation tried (ORDER).** L33 s1 copies f11 L510.
- **Why it fails.** ORDER requires file 10 to state the claim somewhere, and it does not:
  - "worth" occurs nowhere in file 10;
  - file 10 types \(\mathcal N\) only for aesthetics: "declared as a substantive input when aesthetic value is claimed" (L458);
  - file 10 leaves a merit function as an empty place: "marks those places as empty" (L25).
- **The difference from Claude-pre is one of form only.** Claude-pre rules the whole of C9 ORDER but rules this phrase at C65. That is the same ruling.
- **Bookkeeping, not a ruling.** R1 lists M5 among its 13 CLAIM places and R3 counts M47 separately, although R1 says "counted once". The determiner should count this change once.

### 3. M6 (C9 part b). ORDER. UPHELD.
- **Sentences 2 and 3.**
  - s2 is f10 L523, word for word apart from "the contract \(C\)" becoming "the contract of admitted changes".
  - s3 is f10 L521 with the order of L525.
  - L33's tension with f11 L514 comes from L514 (M48). L33 uses file 10's own words.
- **Sentence 4: the refutation tried.** "No predicate meaning "really explains", "is a cause" or "is knowledge" appears anywhere (Derivation 6)" is stronger than f10 L525, "Nothing depends on a predicate meaning …". That is the reading of A, Atria and Mimo.
- **Why it fails.**
  - File 10 already denies existence, not only dependence: "There is no residual predicate meaning "explains," "represents," "is a cause," or "is knowledge."" (f10 L597, kept at f11 L590). That is the sentence the pointer "(Derivation 6)" names.
  - The literal reading ("anywhere", with no "residual") is refuted by file 11 itself:
    - the phrase "is a cause" appears at L55 and L129;
    - "What ordinary language calls a cause" appears at L123;
    - a knowledge predicate is defined at L435–442 ("Created explanatory knowledge", (EK)).
  - So s4 can only mean what L590 means. f10 L144 ("The semantics never asks whether a component "is" a cause") adds the same.
- **To record.** "appears anywhere" is an unclear wording, for the errata.

### 4. M8 (C13). CLAIM, declared. UPHELD.
- f10 L38: "selected transports are *always* underdetermined on unseen changes".
- f11 L43: "underdetermined by its history on an unseen change wherever its population admits a differing survivor there".
- The quantifier moves from every unseen change to a condition on the population.
- The note declares it: "the answer to grievance 3".
- It cannot be ruled WORDING.

### 5. M9 (C15). WORDING. UPHELD.
- **The change.** f10 L44: "Whether the combination is new is a question about the literature, not about whether it is right." File 11 at L47 drops the last clause.
- **The refutation tried.** Dropping an explicit assertion is a change in what is asserted. That is A's TEST: "Someone argues the theory is wrong because it is not new."
- **Why it fails.** Both files fix what would count against the theory, and novelty is in neither list:
  - f10 L17, with the attack list L66–76 and "Anything else is a detail." (L78);
  - f11 L19, "Part XV lists what would count", with L63 "Anything else is a detail." and Part XV (L526–538).
- A reader of file 11 therefore rejects "wrong because not new" on the same ground as a reader of file 10.

### 6. M10 (C19). WORDING. UPHELD.
- **The change.** f10 L56 adds "it is a label. The difference is the difference between a hypothesis and a stipulation." File 11 at L55 keeps "Whether it occurred is a claim about the physical module, fallible but checkable in principle. A kind-label is not a claim about anything."
- **The refutation tried.** A's TEST asks whether a kind-label is a stipulation.
- **Why it fails.** File 11 answers it in the same way as file 10:
  - labels are declared: "A declared label adds no discriminating power" (f11 L39; f10 L32 "Declared kind-labels");
  - declared means stipulated: "A declared contract is stipulated by the modeller" (f10 L172 = f11 L157);
  - selection is a checkable claim: "It is fallible and checkable as any physical claim is" (f10 L482 = f11 L473).

### 7. M11 (C20). WORDING. UPHELD.
- **The change.**
  - f10 L59: "An episode is a history in which contracts can change".
  - f11 L57: "An episode is a history in which contracts change".
- **The refutation tried.** A modal change in a sentence of the form "An episode is …" would make contract change necessary in every episode. All four readers say CLAIM.
- **Why it fails.**
  - The sentence is generic and set against "An assessment is an event with a frozen contract". The grievance it answers speaks of "*letting* questions change across episodes" (L57, f10 L58).
  - File 11 uses restrictive clauses that presuppose episodes without a new contract:
    - "an episode whose originative contribution is a new contract" (L578 = f10 L585);
    - "an episode in which \(C\) is replaced by \(C'\)" (L594 = f10 L601).
  - It also speaks of construction episodes with no contract change stated: "There is an episode (Part X) whose construction witness prepares \(t\)" (L199).
  - Every TEST the readers give (an episode with a fixed contract) gets the same answer under both whole texts.
- **Correction to R1's reasoning.** R1 says "The definition of an episode requires no contract change (f11 L421 = f10 L432)". L421 defines a *complete* critical episode and a *creative* critical episode. It does not define "episode". The ruling rests on the generic reading and on L199, L578 and L594, not on L421.

### 8. M12 (C22, the L63 (D) short form). ORDER. UPHELD.
- **The texts.**
  - f11 L63: "… are stated exactly in Part XV together with what would refute each. In short: … (D) the two provenances and the underdetermination of selected transports; …". This is new wording for f10 L66–78.
  - f10's (D) (L74) moves in full to f11 L534 (M52).
- **The refutation tried (CLAIM).** An unqualified "underdetermination of selected transports" restates Derivation 3 without its qualification.
- **Why it fails.** The short form asserts no theorem. It names a load-bearing claim and defers in words to Part XV, where the qualified statement stands. No reader marks it CLAIM.
- **To record.**
  - If "attack point (D)" in the note (L5) means L63, the note's promise that "every restatement of a theorem carries the theorem's own qualification" fails here (XR1).
  - L63's "(B) their necessity" names the necessity of "the four conditions of Account". L530 states a refuter about transport preservation. The labels are loose; the exact statement is L530. This is an erratum candidate, not a claim difference, because L63 defers to Part XV.

### 9. M15 (C28). ORDER. UPHELD.
- **The text.** f11 L161 s1: "A contract is a declared subset of the physically admitted changes, and a stated scope is what makes it one."
- **The refutation tried.** "One" means "a contract", so an unscoped set is not a contract. That is A's TEST.
- **Why it fails.**
  - Grammatically, "one" stands for the predicate noun "a declared subset". The sentence says that the stated scope is what declares the subset.
  - That is f10 L272 (kept at f11 L259): "The contract \(C\) is a declared subset of the physically admitted edits, and every physically admitted edit excluded from \(C\) is excluded by a stated scope, not silently."
  - It is also f10 L41 (kept at f11 L45): "A contract is a declared subset of those."
  - A's TEST gets the same answer in both files. File 11 keeps f10 L290 word for word at L277: "fails non-vacuity by having a silently narrowed contract". A silently narrowed set is still called a contract in file 11.

### 10. M16 (C29). ORDER. UPHELD.
- **The refutation tried.** A, B, Atria and Mimo all say that file 10 has the narrowing rule "only for (EK)" (f10 L456).
- **Why it fails.** File 10 states each clause at the same or wider scope:
  - "answers the question asked at that scope": f10 L41, "An account is scoped to its contract and says so."
  - "does not answer a broader question": f10 L168, "Two questions with the same \(D\) and different \((C,\mathcal Q)\) are different questions, and an answer to one is not an answer to the other." A broader question has a different \(C\).
  - "a narrowing … is a new claim at a new index": f10 L378, "A new index is a new claim". With L523 ("the contract \(C\) [is a] declared ind[ex]"), a narrowing changes the index. f10 L603 says the same.
- **Pointer.** "(Part VIII)" lands on f11 L365.

### 11. M24 (C41 s1). CLAIM, narrowed. UPHELD.
- **The change.**
  - f10 L294: "A true mechanism guessed for bad reasons satisfies (E)".
  - f11 L279: "(E) does not exclude a true mechanism guessed for bad reasons".
- **The refutation tried (WORDING, as in Claude-pre).** File 10's heading, "What (E) does not exclude" (L292), frames the sentence as non-exclusion.
- **Why it fails.**
  - File 10's sentence asserts, of every such mechanism, all five conjuncts of (E) (f10 L277).
  - Neither file defines "true mechanism". Truth gives at most fidelity (f10 L204, L226). It does not give the stated-scope requirement of non-vacuity (f10 L272).
  - So file 10 licenses B's TEST conclusion (a true mechanism that fails non-vacuity "satisfies (E)"), and file 11 does not.
  - The change is selective. The same file-11 paragraph keeps "satisfies (E) for that question" for the proof (f11 L279 s4).
- **Harm.** No case has a mechanism guessed for bad reasons (`grep` of the case book).

### 12. M27 (C44). ORDER. UPHELD.
- **The text.** f11 L307: "The theorem applies only where its assumptions hold; an addition to \(\Gamma\) that destroys a support is the interference case below, and there upward closure fails."
- **The refutation tried (CLAIM, application, as in Claude-pre).** File 10 "never says that an addition is that case".
- **Why it fails.**
  - f10 L326: "\(\Gamma=\{a,b\}\), \(\mathsf S=\{\{a\}\}\): the full candidate fails although a subset succeeds. Success of a subset does not imply success of the whole". This is an addition, \(b\), that destroys the support \(\{a\}\), stated in general form.
  - "There upward closure fails" is the definition of upward closure applied to that case. f10 L310 already says "No upward closure … [is] assumed".
  - "Applies only where its assumptions hold" is what the conditional form "If … then" (f10 L322) means.
  - The ruler is consistent with its other rulings. At M43 file 10 entails but never states the conclusion, so the place is CLAIM (application). Here file 10 states it.

### 13. M38 (C56), the occasions clause. CLAIM. UPHELD.
- **The texts.**
  - f10 L438–444: "For claimed obligations \(O\) and protected obligations \(P\), fixed for the comparison," then (P) with \(\forall r\in P[r(\xi)\Rightarrow r(\xi')]\), then "(P) does not rank alternatives."
  - f11 keeps L427 and (P) at L430. It adds L433 s1: "each as a stated condition over stated occasions, and a protected condition is lost exactly when it fails on an occasion it covers".
- **The refutation tried (WORDING).** Take "stated occasions" to be the two compared configurations \(\xi,\xi'\).
- **Why it fails.**
  - The "exactly when" makes failure on any covered occasion a loss. The formula counts a loss only when \(r(\xi)\land\neg r(\xi')\), so the minimal reading does not make the prose match the formula.
  - f11 L514 then lists "the obligations \(O\) and \(P\) of a repair, with the occasions each covers (Part XI)" as an input whose absence leaves "the verdict … unsettled". No file-10 verdict turns on occasions.
  - f10 L122 allows history-valued ports, so a history condition is possible in file 10. File 10 never requires one.
- **So the clause adds a requirement, an outside input and a loss criterion.**
- **E1.** It holds, 2 of 2 on the 1D lists:
  - B's D47 quotes only the occasions sentence, MARK CLAIM;
  - A's D47 joins it with the next sentence, MARK CLAIM, and its WHY names "stated occasions" and "an exact loss condition".
- **Harm.** The ruler's O35 reading matches the texts:
  - under file 10, the tap "then runs as before" gives \(r(\xi')\), so there is no loss (AGREE);
  - under file 11, the occasions are unstated, so the verdict is unsettled (SILENT).
  - Whether this is harm depends on step 3's file-10 mark, as R2 and 01 say (01 L94, L563).

### 14. M48 (C66), Declared inputs. CLAIM. UPHELD.
- **The refutation tried (ORDER or WORDING).**
  - File 10 already takes the obligations as supplied data. They are a component of every question: "\(O_p\) is the set of obligations being addressed or protected" (f10 L164 = f11 L149), and they are "fixed for the comparison" (f10 L438).
  - Boundary, continuity and the contract are already declared indices, and "Every claim is relative to them" (f10 L523).
  - So much of L514's list is already input in file 10.
- **Why it fails.** Three things in L514 are in no sentence of file 10:
  1. "the occasions each covers";
  2. "what makes a restriction appropriate";
  3. the rule "where the input is missing, the verdict is unsettled and the semantics says so rather than choosing the input from the verdict wanted".
- File 10's nearest sentences give instances, not the rule: f10 L344 ("Set \(b_B=0\) because it gives the mass I favour" is not an inference) and L406 ("missing evidence stays missing"). The rule moves O35 (see M38) and bears on O1.
- **Correction to R3's reasoning.** R3 says "Only the boundary, continuity and scope items meet the first condition". \(O\) and \(P\) meet it too (f10 L164, L438). The ruling rests on items 1–3 above, which are enough.

### 15. M51 (C71), (B) Necessity. ORDER. UPHELD.
- **The texts.**
  - f10 L70: "cannot be captured by *any* transport satisfying component fidelity under *any* physically admitted contract".
  - f10 L535: "A genuine explanation whose organization no transport can preserve under any physically admitted contract. This refutes necessity."
  - f11 L530 is f10 L535's sentence.
- **The refutation tried.** Mimo's NEW1: file 11 drops L70's narrower condition.
- **Why it fails.**
  - Every transport that fails component fidelity fails to be faithful. So every explanation that L70 counts as refuting, file 10's own L535 counts too, as Mimo concedes ("A's Part XV uses B's wording").
  - L70 does not say that only its case refutes necessity.
  - What file 11 drops is L70's narrower description, which file 10's L535 already contradicts.
- **Correction to R3's reasoning.** R3 says that L63 ("(B) their necessity", said of the four conditions of Account) "still tells the reader what 'preserve' means". Read that way, "preserve" would mean meeting all four conditions of Account. That would widen the refuter beyond file 10's "without a faithful transport" (f10 L535 heading).
  - The better support is that preserving an organization is a transport property. Faithfulness is "the component and global fidelity conditions" (f11 L191). On that reading L530 is f10 L535.
  - Record L63's "(B) their necessity" as a loose label (see M12).

### 16. M52 (C73), (D) Genesis. CLAIM in limb 1; limbs 2–3 ORDER; declared. UPHELD.
- **Limb 1.**
  - f10 counts as a refuter any "selection history \(H\subsetneq C\) whose survivor is determined on \(C\setminus H\)" (L539), or a selected transport "non-underdetermined on unseen changes" (L74).
  - f11 counts only one "whose value at an unseen change is determined by its history although its population admits a differing survivor there", and adds "a population with no such survivor is the theorem's own qualification, not a refutation" (L534).
  - A condition is added, and the quantifier becomes pointwise.
- **Limb 2** is f10 L541 with L74's "(against Part IV)". **Limb 3** is f10 L74's third disjunct, without "in fact". Both are ORDER.
- The note declares the place: "attack point (D), the Part XV entry".

### 17–20. M53–M56, Derivation 3. CLAIM, declared. UPHELD.
- **Title (M53).** f10 L567 "underdetermined on unseen changes" becomes f11 L560 "… on unseen changes their population leaves open". The title states the theorem in short, and the restriction is a change of scope.
- **Claim (M54).** An unconditional existence claim becomes a conditional one.
  - f10 L569: "For every \((a,b)\in C\setminus H\) there exists a transport \(t'\), also surviving on \(H\), with a different value".
  - f11 L562: "For every \((a,b)\in C\setminus H\) at which some \(t'\in\mathcal T\) … has a different value", adding "The presence of an unseen pair alone does not establish that such a \(t'\) exists; it must be admitted, realizable, a member of \(\mathcal T\), and a survivor of \(H\)."
- **Proof (M55).** f10 L571 builds the alternative freely ("Alter \(L_j(a,b)\) … the result survives on \(H\)"). f11 L564 adds a new assertion: "Where \(\mathcal T\) contains no such transport, \(H\) is silent on the value at \((a,b)\) and the population fixes it."
- **Consequence (M56).** f11 L566 adds "wherever its population admits an alternative" and a sentence that gives up "the blanket claim that every untested value is unconstrained".
- No reading makes any of the four WORDING.

### 21. XR1 (L5). SLIP. UPHELD.
- **The pointer.** "(the answer to grievance 3, attack point (D), the Part XV entry)".
  - In file 11, grievance 3 is L43.
  - Attack point (D) and the Part XV entry are one passage, L534. Or, if "attack point (D)" means L63, that short form carries no qualification.
- **Test (d).** The list is the note's own content, and the note is a meta sentence (M1). No theory sentence changes what it claims.
- **Correction to R3's reasoning.** R3 says "L63 did not change". L63 is new wording (f10 has no short form; f10 L66–78 is the full list). Its claim is what did not change (ORDER, M12).

### 22. XR2 (L5). SLIP, with a steering flag. UPHELD.
- The references "the audit's case O48" and "(Semantics results S75)" point outside the document.
- The note's statement about Derivation 3 stands without them. No theory sentence depends on them.

### 23. XR3 (L27). SLIP. UPHELD.
- **The refutation tried (CLAIM-CHANGING).**
  - Parts XI and XIV mark places only for \(\mathcal N\) (worth and aesthetics; f11 L447, L510), and L514's list does not include a probability of truth, a merit function or a ranking of thinkers.
  - With L37 ("the front matter states nothing the body does not state more exactly"), a reader could let the pointer's targets narrow what L27 claims.
- **Why it fails.** L27's claim is set by its own words ("Where a claim needs one of these, the semantics takes it as a declared input and marks the place"). The pointer names places that do not carry part of it. That leaves the claim unsupported for three items, which is the overreach ruled at M3 (CLAIM). It does not give L27 a different claim.
- Atria's CORRECT names no place that carries a probability of truth, and there is none (`grep` in R3).
- This is the closest of the seven SLIPs to CLAIM-CHANGING.

### 24. XR4 (L275). SLIP, with a steering flag. UPHELD.
- The parenthesis "(the bell does not explain the tide)" has no referent in the document; the bell and the tide are case O2's content.
- The sentence's rule ("packaging a genuine dependence that answers a different question beside it does not repair this") stands without it.
- The example's content is part of M23, which is ruled CLAIM. The steering bears on the cases, not on test (d).

### 25. XR5 (L447). SLIP. UPHELD.
- "(Part XIV)" lands on L510, which marks \(\mathcal N\)'s place: "It is taken as an input and never derived".
- L514's "Besides the two primitives" classes \(\mathcal N\) apart from the declared inputs, while L447 calls it "a declared input".
- Either way \(\mathcal N\) is an input the semantics does not supply. The claim does not change, and O12 is SILENT under either reading.
- The pointer arguably lands (CORRECT). SLIP or CORRECT, test (d) is unaffected.

### 26. XR6 (L588). SLIP. UPHELD.
- The claim at L586 now reads "together with declared indices and declared inputs".
- The order cited, L518, lists no declared input. It also lists none of the definitions that rest on one: Ownership (L419), ProducedBy (L433), and System boundary and continuity (L465).
- The pointer lands on the paragraph it names, and the proof is incomplete. Derivation 6's claim is set by L586's words.

### 27. XR7 (L616). SLIP. UPHELD.
- "a population that admits no survivor at the new change" misdescribes Derivation 3's qualification. The qualification is no *differing* survivor of \(H\) (f11 L562, L564).
- The two coincide only if every \(H_0\)-survivor agrees at the occlusion, and Derivation 10 does not state that.
- The pointer lands on Derivation 3. The inexact clause is itself the CLAIM place M59.
- Derivation 10's conclusions do not rest on the clause: (G), (P) and (EK) at L618, and the one-kind point at L620.

### 28. NEW-XR1 (L620; f10 L627, the same words). CORRECT (loose). UPHELD.
- **The refutation tried.** Derivation 2 (f11 L554) is about "Two candidates \(\mathcal E,\mathcal E'\) for the same \(p\)", not about two components of one organization. The direct basis is (K) with Derivation 1. A, B and Mimo say this.
- **Why the ruling stands.**
  - Take the swapped assignment as a second candidate. Derivation 2 then yields "their components are pairwise of one kind on \(C\)".
  - L620's next sentence restates Derivation 2's Consequence (L558) almost word for word: "A claim that "component 1 is *really* thing 1" is a claim that some admitted change distinguishes them". Compare L558: "A claim that two such candidates "really" differ is a claim that some admitted change separates them".
- **Test (d).** On any reading the sentence's claim holds, through (K) and Derivation 1, so the pointer is not CLAIM-CHANGING. It is identical in file 10, so it is not a difference between the files. At worst it is a shared erratum.

---

## Spot checks outside the selection (not counted)

- **The undeclared places of the Derivation 3 cluster.** Each is a sentence file 10 lacks; CLAIM is confirmed at each:
  - M19: f11 L197, last sentence, against f10 L210;
  - M21: f11 L225, last sentence, against f10 L238;
  - M46: f11 L473, last sentence, against f10 L482;
  - M59: f11 L616, the added clause, against f10 L623.
- **M43.** f10 L458 entails "no aesthetics follows from achieving a stated effect" through "declared as a substantive input when aesthetic value is claimed" and "The semantics does not derive \(\mathcal N\)". File 10 does not state it. CLAIM (application) is consistent with the policy and with M27.

## What the verification leaves standing

- **P3 fails.**
  - Both named places, the occasions clause (M38) and Declared inputs (M48), are CLAIM. P3 stands only if both are WORDING.
  - Many undeclared CLAIM places lie outside Derivation 3 and its three sentences.
- **E1 holds.** Testers A and B both mark the occasions clause CLAIM on their 1D lists.
- **Test (d) holds.** No pointer is CLAIM-CHANGING.
  - XR1–XR7 are SLIPs for the errata list.
  - NEW-XR1 is loose, and file 10 has the same pointer.
- **Harm on the selected places.**
  - Among the selected places, O35 is the only case that moves away from the thoughtful person, through M38 and M48 together. Whether that counts as harm turns on step 3's file-10 mark (baseline SILENT; 01 AGREE).
  - The declared places (M8, M52–M56) move O48 toward the thoughtful person.
  - M5 and M24 touch no case that moves.

## Corrections to the rulers' reasoning (no ruling changes)

1. **M5.** It is counted in R1's 13 CLAIM places, and M47 is counted in R3, although R1 says "counted once". Count the change once.
2. **M11.** f11 L421 defines complete and creative critical episodes, not "episode". The WORDING ruling rests on the generic reading and on L199, L578 and L594.
3. **M48.** \(O\) and \(P\) are already supplied data in file 10 (f10 L164, L438). The CLAIM rests on the occasions, the appropriateness input and the unsettled-verdict rule.
4. **M51.** The support that "L63 tells the reader what 'preserve' means" points the wrong way. It would widen "preserve" to the four conditions of Account. The support should be f11 L191. L63's "(B) their necessity" is a loose label (an erratum candidate).
5. **XR1.** "L63 did not change" should read "L63's claim did not change". L63 is new wording, ruled ORDER at M12.
