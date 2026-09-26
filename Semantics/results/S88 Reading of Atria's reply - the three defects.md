# S88: reading of Atria's reply on the three defects

*23 September 2026. Written by a Claude subagent for the orchestrator, from 15:38 to 15:54 UTC. This subagent is the fresh reader required by rule R3: it did not write the findings. It followed the rule committed at cc87b45. Mimo's reply was not read.*

## The late rule goes with this reading (R7)

This reading follows the rule in `results/S88 How the cross-examination will be read - written after Atria's reply arrived, before it was opened.md`.

- That rule was written from 15:35 to 15:36 UTC. Atria's reply had arrived at 14:24:02 UTC.
- No one had opened the reply when the rule was written.
- So the rule was adopted after the data arrived, and it is recorded as adopted then (lesson S2).

## What was read, and in what order

1. **The receipt, first (R1).** `s88_xexam_atria.receipt.json` shows finish_reason "stop", one attempt, and "accepted": true. The reply used 54,162 completion tokens, 47,960 of them reasoning.
   - The response file's sha256, a29932e3…, matches the receipt.
   - Its last line is END OF REPORT. This was checked by a script that printed only true or false, before the reply was read.
   - The call is accepted, so the reply is read for its arguments.
2. **The S88 brief.** Its sha256, 8485bb42…, matches the receipt's user_sha256. Its theory text is byte for byte file 10 (sha256 4aa2c97e…).
3. **Claude's checks**, in the session scratchpad under `revision2/checks/`: `W31 T2 bound.md`, `W19 W20 Mimo holes.md` and `defence of T2 and Derivation 2.md`.
4. **Atria's reply**, `results/S88 Cross-examination - three defects - returns/s88_xexam_atria.response.txt`, in full.

**The reasoning file was not opened.**

**Also read.**
- File 10 and file 11, wherever they bear on the findings.
- The case book entries O5, O7 and O33, in `tests/S81 Case book - the 52 cases, situations and fixed verdicts, as the tested agent sees them.md`.
- The first part of the S81 determination packet for O33, `results/S81 File 11 against every case - outputs/determination/raw readings/04e packets/O33.md`. It was read for the case text and for the basis both S81 readers gave for the verdict.

Every counterexample and instance below was recomputed by a script in exact rational arithmetic. The script and its output are in the appendix.

**Conventions.**
- "L204" means file 10, line 204, which is theory line 204 of the brief. "F11 L191" is the same text in file 11.
- Where the two files differ on a point, the difference is stated.
- S1, S2 and S3 are the three sentences of non-circular dependence (L270 = F11 L257).
- R-τ-in, R-τ-mech and R-E are the brief's readings of S3.

## Summary

| finding | Claude's position, frozen in R3 | Atria's verdict line | ruling | repair |
|---|---|---|---|---|
| **F1**, Derivation 2 | The component claim is false as stated. Repair: "Same anchors, one account", a change of claim. | F1: UPHELD | **UPHELD** | Two wording changes to the claim: the premise names the exposed ports, and the conclusion says it rests on (F1), (F2) and (A). |
| **F2**, (T2) | (T2) omits h1–h3. This is a drafting omission, fixed by an erratum. | F2: UPHELD | **UPHELD** | The erratum also requires the run to stay in the scope. |
| **F3**, non-circular dependence | Γ is untyped. O33 and O5 flip on R-τ-mech. Option B is preferred to option A. | F3: PARTLY UPHELD | **NARROWED**: the O33 flip is withdrawn | Option B names τ and σ, and a typing sentence for Γ is added. |
| **F4** (new, from Atria's further item 1), Derivation 3 of file 10 | none | none | **Holds** against file 10. File 11 already repairs it. | File 11's qualified Derivation 3. Atria's own wording is rejected. |

Atria's further items 2, 3 and 4 do not hold, and item 5 offers no counterexample.

---

## F1. Derivation 2, "Indistinguishable is identical"

### 1. Claude's current position

As frozen in R3:
- Derivation 2's component claim is false under its stated assumptions, so Part XV's defeat clause is triggered.
- The repair narrows the claim to what the proof proves. It is the brief's "Same anchors, one account" wording, a recorded change of claim.

### 2. Atria's argument

The verdict line reads: **"F1: UPHELD"**.

- **Point 1. E₂ is admissible.** The text permits merged anchors and uses them:
  - L204: "λ assigns each component of E a subnetwork of D with a port translation";
  - L248: (F1) projects "away its hidden ports";
  - L356: the skew case uses "a determinant suborganization whose hidden ports project away".

  Atria rechecked (F1), (F2) and (A) for E₂. L260 is "a test E₂ passes, not a prohibition". Defence (i) fails.
- **Point 2. Half (a) is false.** Derivation 1 "is a *within-one-candidate* statement". (F1), (F2) and (A) "each constrain one candidate against D separately". The counts differ in instance 1, and in instance 2 only the input components pair. "The proof's word 'Immediate' hides exactly the failed step."
- **Point 3. Defence (ii) "describes a true but different claim".**
  - L561 names "*their* components", and the conclusion and title assert identity.
  - L23 says that systems with different routes are different organizations.
  - "A theorem whose proof works only after an unstated restriction to a weaker reading is not a theorem as stated."
- **Point 4. Defence (iii) does not save the claim.** It works one way in instance 1 and neither way in instance 2. The block reading needs a notion of common coarsening that the theory never defines, and L609 excludes coarsenings from Derivation 8.
- **Point 5. Defence (iv) fails.** Grain and contract are separate indices (L523). (K) gives three distinct relations. Deleting k_y leaves z undetermined (L120).
- **Point 6. Derivation 10's sentence at L627 fails (K) when read literally.** "Displace a thing" (L617) replaces one persistence component's relation and not the other's. Its intended content is the exchange of anchors, and there the pairing exists.
- **Point 7. The repair "is sound".**
  - Its premise is rightly "the same subnetworks", not "anchors of one kind".
  - It "breaks nothing I checked": Derivations 1, 8 and 9, Part VI, Part VII's cases, and "What (E) excludes / does not exclude".
  - The supporting sentence after (K) "is needed for the cross-candidate comparison to typecheck at all".
  - One caveat: "the conclusion 'the two are one account on C' is drawn from (F1), (F2), (A) alone, so it should say so or add the non-circular/non-vacuous conjuncts."
- **Point 8.** "I could not refute the finding at any step."

### 3. Check against the theory text

**Lines relied on.**
- **The claim**, L561 = F11 L554: "Two candidates ℰ, ℰ′ for the same p that both satisfy (F1), (F2), and (A) on C are one account at grain C: their components are pairwise of one kind on C and their answer profiles coincide."
- **The proof**, L563 = F11 L556: "Immediate from Derivation 1 and (A). ∎"
- **Derivation 1**, L553 = F11 L546: "every active component k of E has the same signature on τ[C] as its anchor λ(k) has on C, up to the port translation."
- **(K)**, L136, and F11 L121, which adds a clause about finer contracts: "Two components j, j′ are of one kind on C when there is a bijection of their footprints under which sig_C(j) and sig_C(j′) coincide."
- **λ**, L204 = F11 L191: "λ assigns each component of E a subnetwork of D with a port translation."
- **(O)**, L117, and L120 = F11 L105: "A deleted component imposes the full relation on its ports. An edit that sets a port replaces the component assigning that port".
- **Different routes**, L23 (the same sentence is at F11 L25): "Two systems with identical outputs and different internal routes are different organizations here".
- **Derivation 8**, L609 = F11 L602: "The result does not apply to coarsenings, changed boundaries, or lost event identities."
- **(E)**, L277: Account is (F1) ∧ (F2) ∧ (A) ∧ NonCircular ∧ NonVacuous.

**Quotations in the reply.**
- Every quotation matches file 10 word for word.
- One reference is loose. Point 7 gives "lines 284–298" for "What (E) excludes / does not exclude". Those paragraphs are L282–294, and L296–298 is "Why there is no anchoring condition".
- No words are misquoted.

**The instances, recomputed** (appendix, parts 1 and 2). They were checked at the baseline and at do(x=c) for seven values of c. Every relation is affine in c, so the result holds for all c.
- **Instance 1.** E₁ and E₂ both satisfy (F1), (F2) and (A). k_x pairs only with m_x. k_y, k_z and m_z are each of one kind with no component of the other candidate. E₁ has three components and E₂ has two.
- **Instance 2.** E_a and E_b both satisfy (F1), (F2) and (A). There are six bijections between their components, and none makes every pair of one kind. Only a_x and b_x pair.

**How an edit acts inside an anchor.** Both instances rest on one reading of Sol_{λ(k)}(a,b): under do(x=c), the anchor {j_y, j_z} keeps its own relations and leaves x free, so m_z's relation stays {(s, 2s+1)}. The words fix this reading:
- (O) (L117) imposes only the components of the organization being solved.
- L120 makes do(x=c) replace j_x, which lies outside the anchor.

The other reading has the edit fix x inside every anchor that contains x. On that reading even E = D with the identity transport would fail (F1): Sol_{j_y}(do(x=c), b₀) would be {(c, 2c)}, while k_y's relation is {(s, 2s)}. This also settles the "imprecision" that Atria lists under Derivation 1 in its further item 5.

**The reading of "pairwise".** The words "their components are pairwise of one kind" name every component of both candidates. No words restrict the pairing to shared anchors. Atria's point 3 stands.

**The repair, checked further than Atria's point 7 goes.** Atria writes that clause (ii) "follows by composing Derivation 1's two signature identifications through the common anchor".
- That step needs the two port translations to land on the same ports of D.
- The premise "λ′(φ(k)) = λ(k) for every k, up to port translation" does not say so.
- L204 lets two components anchored to one subnetwork expose different ports of it.

The following instance uses the D of instance 1 (appendix, part 3):
- **P** has three components:
  - x = u, anchored to {j_x};
  - y = 2x, anchored to {j_y, j_z} with ports x, y;
  - z = 2x + 1, anchored to {j_y, j_z} with ports x, z.
- **Q** has three components:
  - x = u, anchored to {j_x};
  - y = 2x, anchored to {j_y, j_z} with ports x, y;
  - z = y + 1, anchored to {j_y, j_z} with ports y, z.
- **P and Q both satisfy (F1), (F2) and (A).**
- **Two bijections keep every anchor subnetwork.** Under each of them, at least one pair is not of one kind. P's z = 2x + 1 has the relation {(s, 2s+1)} and Q's z = y + 1 has {(s, s+1)}, and these differ under both footprint bijections.

So clause (ii) is false when the port translations are left free. It is true when each pair's translations land on the same ports of D, because composing them then gives the footprint bijection the proof names. The brief's smaller alternative wording ("a component of E and a component of E′ anchored to one subnetwork of D, up to port translation, are of one kind on C") fails on the same pair.

**Atria's caveat holds.**
- The claim's premises are (F1), (F2) and (A).
- An account in the sense of (E) (L277) also needs non-circular dependence and non-vacuity, and nothing in the premises gives either candidate those.
- So "one account" says more than the premises give. The original claim at L561 is loose in the same way.

**Derivation 10.** Read literally, L627 fails (K). Under "displace a thing" (L617 = F11 L610), the displaced thing's persistence component changes and the other's does not, so the two are not of one kind. Atria's point 6 stands. The exchange of anchors keeps each thing's continuity subnetwork and the same exposed ports, position and velocity. So the reworded sentence meets the tightened premise below.

### 4. Ruling: UPHELD

- The component half of Derivation 2 is false under the claim's stated assumptions. Both instances meet every stated assumption, recomputed exactly.
- The answer-profile half is true.
- No reading that the words fix saves the component half.
- The classification stands: the claim is false as stated, and the repair is a recorded change of claim.
- The reply offers no argument against any part of the finding.

### The repair, changed after the cross-examination (R6)

Both changes below are wording changes to "Same anchors, one account". Both were made after the cross-examination, and neither changes the classification.

1. **The premise names the exposed ports.** The reason is the P and Q instance above. It was found while checking Atria's point 7 (the composition step). Atria did not raise it.
2. **The conclusion says what it rests on.** The reason is Atria's caveat in point 7, which holds.

The claim becomes:

> **Claim.** Let ℰ, ℰ′ be candidates for the same p that both satisfy (F1), (F2) and (A) on C. (i) Their answer profiles coincide on C. (ii) If a bijection φ of their active components gives each k and φ(k) one anchor, the same subnetwork of D with port translations onto the same ports of D, then k and φ(k) are of one kind on C for every k; so far as (F1), (F2) and (A) reach, the two are one account on C.
>
> *Proof.* (i) By (A), Ans_E(τ(a),σ(b)) = Ans_p(a,b) = Ans_E′(τ′(a),σ′(b)) for every (a,b) ∈ C. (ii) By Derivation 1, k has the signature of its anchor on the ports its translation names, and φ(k) the signature of the same anchor on the same ports; composing the one translation with the inverse of the other gives a footprint bijection under which the two signatures, read on C, coincide. ∎

- **Unchanged:** the sentence "Without the premise of (ii) nothing more follows …", the Consequence, the supporting sentence after (K), and the Derivation 10 wording.
- **The smaller alternative wording is not adopted as it stands.** If it is used, it needs the same words, "onto the same ports of D".

---

## F2. (T2), approximate transport

### 1. Claude's current position

As frozen in R3:
- (T2) omits three hypotheses: matching starts, whose Lipschitz constant, and where ε holds (h1–h3).
- This is a drafting omission, fixed by an erratum that restores the predecessor's hypotheses.

### 2. Atria's argument

The verdict line reads: **"F2: UPHELD"**.

- **Point 1.** "The omission is real and is not covered by 'stated assumptions'." e_n is never defined, the word "discrepancy" occurs only on L376, and the predecessor states all three hypotheses.
- **Point 2.** "Counterexample 2b is decisive on a reading the text permits." "An L-Lipschitz next-step map" does not say which map. On the target-map reading, (T2) is false even from matching starts. "This alone sustains the finding."
- **Point 3.** "Counterexample 2a is refuted." 2a needs unequal starts, which "the theory's reading excludes". Atria's reasons:
  - the ε = 0, n = 0 and n = 1 instances of (T2);
  - the theory's practice of evaluating E at the translated point (L204, L234, L257, L265, L366, L368–374).

  "So e_n = d(πSⁿz, Tⁿπz) with e₀ = 0 is the theory's reading, and on it (T2) is true."
- **Point 4.** "Counterexample 2c is weak but the gap it points at is real."
- **Point 5.** "The erratum is correct and minimal." It defines e_n, names T, and "scopes ε to every reached state". The optional unequal-start clause is "a genuine addition". The side notes are correct. Nothing else cites (T2).
- **Point 6.** The classification is right. "The one respect in which the finding overreaches is counterexample 2a".

### 3. Check against the theory text

**Lines relied on.**
- **(T2)**, L376 = F11 L361, in full: "**Approximate transport.** With one-step discrepancy ε and an L-Lipschitz next-step map, e_n ≤ ε Σ_{k<n} L^k. (T2) Without a modulus, no accumulated bound follows. An exact question is not silently replaced by an approximate one."
- **Functional transport**, L366 = F11 L351: "If π∘S_a = T_a∘π for every generator a, the same holds for every admitted finite composition with matching scopes."
- **Part XV**, L543 = F11 L538: "A counterexample to the finite monotone theorem, (I2), (O1), (T2), (CT2), or Derivations 1–3 under their stated assumptions."
- **π**, L204 = F11 L191: "π: X_D → X_E on the stated scope".

**Quotations in the reply.**
- **"In full" is wrong.** Point 1 says that L376 "reads in full" and then gives only its first two sentences. It leaves out the third: "An exact question is not silently replaced by an approximate one." No word is changed.
- **The other quotations match.** The predecessor quotations match passage 1, and point 2's "π∘S_a = T_a∘π" matches L366.
- **One statement is an inference, not a quotation.** In L366, S_a and T_a are indexed by generators, and "next-step" occurs only on L376. So "both S and T are next-step maps" is Atria's inference. It is a fair one.

**Arithmetic**, exact (appendix, part 4).
- **2a on reading R.** On this reading the explanation's run starts at y₀ = −1. Then e_n = 1, 21/10, 43/10, 87/10 against the bound 0, 1/10, 3/10, 7/10. On reading M, where both runs share one start, the same maps give e_n equal to the bound at every n.
- **2b.** e₂² = 2501/25 = 100.04, against 0.2² = 0.04 with L = 1. With L = Lip(T) = 100.0099…, the bound at n = 2 is 10.101, above e₂ = 10.002. The one-step discrepancy is 1/10 at every state.
- **2c.** e₂ = 31/100 against the bound 3/10. The step discrepancy is 1/10 at z₀ and 11/100 at z₁.

**Readings.**
- **e_n (h1).** No words define e_n. The symbol and the word "discrepancy" occur only on L376. The same-state reading M is supported by context alone:
  - the placement of (T2) after L366;
  - the theory's evaluation of E at the translated point everywhere it compares D with E;
  - (T2)'s own instances: with ε = 0, reading M gives L366's exact result, and at n = 0 the formula reads e₀ ≤ 0.

  Atria's point 3 is correct as a finding about context: 2a needs a second, free starting state, and no line introduces one. It is not correct as a claim that a stated assumption excludes 2a, because 2a breaks neither assumption that L376 states. The finding never relied on 2a under reading M: the brief's F2 point 3 already says that (T2) is true on that reading, given h2 and h3. The missing item is best called the undefined e_n, whose definition gives e₀ = 0. The erratum supplies exactly that definition.
- **Which map (h2).** "An L-Lipschitz next-step map" names no map. 2b meets both stated assumptions on reading M, from one start, with the target's map as "the next-step map". So the literal text is open to a counterexample even on the theory's own reading of e_n. Atria's point 2 stands.
- **Where ε holds (h3).** "With one-step discrepancy ε" most naturally bounds every step, and 2c breaks that reading. No word says "every". Atria's point 4 stands.

**The erratum, checked further than Atria's point 5 goes.** Atria says the erratum "scopes ε to every reached state". Its words say "at every state z of the stated scope", and they do not say that the run stays in the scope.
- **If the stated scope is π's domain** (L204), the hypothesis "d(πSz, Tπz) ≤ ε at every state z of the stated scope" is defined only when Sz also lies in the scope. The run then stays in the scope, and the words suffice.
- **If it is a separate scope for ε**, as the predecessor's "on a stated scope" is, the words do not suffice. Take the scope {0}, the maps of 2c, and π = id on ℝ:
  - the discrepancy at the only state of the scope is 1/10 = ε;
  - T is 2-Lipschitz;
  - e₂ = 31/100 > 3/10.

The brief's side note ("both runs must stay inside the region where ε and L hold") covers this case, and Atria calls the side note correct. It belongs in the erratum itself.

### 4. Ruling: UPHELD

- **All three omissions exist under the theory's stated assumptions.** e_n is never defined, no words name the map whose constant is L, and no words say where ε holds.
- **The classification stands.** The predecessor states each item (passage 1), so restoring them is an erratum. No other claim cites (T2): the only lines that name it are L376 and L543.
- **Atria's refutation of 2a is accepted as far as it goes.** 2a works only on a reading that the text's context speaks against. The finding did not rely on it.
- **The defeat clause is met literally by 2b,** which holds on the theory's own reading of e_n.

### The repair, changed after the cross-examination (R6)

One wording change: the brief's side note moves into the erratum.
- The reason is the scope {0} instance above.
- It was prompted by Atria's point 5, which describes the erratum as doing something its words did not yet say.
- The classification is unchanged: this is still an erratum.
- The optional unequal-start clause stays optional. It is a new claim, as the brief and Atria both say.

> **Approximate transport.** With one-step discrepancy d(πSz, Tπz) ≤ ε at every state z of the stated scope and an L-Lipschitz represented next-step map T, the discrepancy after n steps from one state z, e_n = d(πSⁿz, Tⁿπz) (so e₀ = 0), satisfies e_n ≤ ε Σ_{k<n} L^k whenever z, Sz, …, S^{n−1}z lie in that scope. (T2) Without a modulus, no accumulated bound follows. An exact question is not silently replaced by an approximate one.

**The proof goes through under these words.** For k < n, e_{k+1} ≤ d(πS(Sᵏz), Tπ(Sᵏz)) + d(Tπ(Sᵏz), T(Tᵏπz)) ≤ ε + L·e_k, and e₀ = 0.

---

## F3. Non-circular dependence

### 1. Claude's current position

As frozen in R3:
- Γ in non-circular dependence is untyped.
- On the "mechanism only" reading, R-τ-mech, the fixed verdicts of O33 and O5 flip.
- Of the brief's two repairs, option B is preferred over option A.

### 2. Atria's argument

The verdict line reads: **"F3: PARTLY UPHELD"**.

- **Point 1.** Part (a), the missing τ and σ, "does not stand — the finding itself withdraws it". L248, L257, L265 and L356 read the pairs of C on E through the translation.
- **Point 2.** Part (b) "is a real ambiguity with consequences, and the text pulls both ways". The pull comes from L246, L248, S3's "the other boundary conditions" and L304. "No sentence decides."
- **Point 3.** "On R-τ-mech the theory's paradigm case fails S3." With Γ = {L := H cot θ}, the interventions on H and θ replace the input components, not the law. L286 implies that the forward organization is what (E) includes. Yet "no sentence is contradicted outright — but the theory needs R-τ-in here".
- **Point 4.** "O5 is the strongest external case; O33 is weaker."
  - O5's verdict treats the yeast explanation as an account.
  - "O33's fixed verdict is only that the table is 'faithful', which R-τ-mech does not contradict — the tension is with the rationale ('A form that could ask more has not asked more'), not with a stated verdict."
- **Point 5.** The finding's point 6 is correct. Under R-E, a contract of relabelings only passes S3, against L272. "a repair must keep the witnessing contrast inside C".
- **Point 6.** S2's "as a component" may exclude too much: a coarse law that is a single component. "Unanalysed" should be glossed as "not anchored to a subnetwork of D under (F1)". "This is prose-level, not a counterexample".
- **Point 7.** "Option B is the right one and is sound."
  - Atria checked it against the skew case, the production case, identification and obstruction, Derivations 1, 8, 9 and 10, Part VI and its examples, and the (E) paragraphs.
  - Option A's cost is real.
  - Atria would add to L246: "Γ is a set of components of E; boundary values not in Γ are the named background of Part VI."
- **Point 8.** "part (a) does not stand …; part (b) — the typing ambiguity and the R-τ-mech verdicts it forces against Part VII's production case and O5 — does."

### 3. Check against the theory text

**Lines relied on.**
- **S3**, L270 = F11 L257: "There exists (a,b) ∈ C that removes or replaces a nonempty block of Γ while preserving the other boundary conditions, under which the answer profile changes or ceases to be determined in the claimed way."
- **Γ**, L246 = F11 L233: "an identified set Γ of active commitments in E".
- **Non-vacuity**, L272 = F11 L259, last sentence: "A contract consisting only of relabelings, or excluding every change under which the active commitments could matter to 𝒬, does not satisfy non-circular dependence and is therefore not a contract on which an account can be claimed."
- **Part VI**, L304 = F11 L289: "let E|W retain the commitments in W with the named background fixed".
- **Faithful**, L204 = F11 L191: "A transport is **faithful on C** when it satisfies the component and global fidelity conditions of Part V."
- **Questions**, L168 = F11 L153: "Two questions with the same D and different (C,𝒬) are different questions".
- **Part VII production case**, L338 = F11 L323: "The forward organization is faithful under this contract."
- **Reversed calculation**, L286 (F11 L273).

**Quotations in the reply.** The words match file 10. The line references are wrong in four places:
- Point 3 gives "line 340" for Part VII's "faithful" and "line 342" for "direction is derived from the admitted edits". Both phrases are in L338. L340 is the heading "Identification", and L342 is the identification paragraph.
- Point 7 and further item 5 give "line 328" for interference. Interference is L326; L328 is infinitary support.
- Point 7 gives "lines 294–298" for "What (E) does not exclude". That paragraph is L294, and L296–298 is "Why there is no anchoring condition".

Point 1 also misdescribes the finding. The brief's F3 point 1 classifies (a) as a drafting slip that the text's conventions fill; it does not withdraw it. On (a) the reply and Claude's frozen position agree, since the frozen position lists no defect under (a).

**(b): Γ is untyped.**
- L246 is the only line that introduces Γ, and it says only "an identified set Γ of active commitments in E".
- The brief's three pulls are all in the text: L248's "active component k", S3's "the other boundary conditions", and L304's "the commitments in W" set against "the named background".
- No line decides between them. Atria's point 2 stands.

**O33.** The case book's situation: "Lea's question is what happens when the two freezer knobs are turned together. A colleague rewrites it as a table with one column for each knob. Every row moves both knobs together; no row moves one alone." The fixed verdict: "The table is faithful. Its columns could have carried single-knob rows, and none was added. A form that could ask more has not asked more."
- **"Faithful" does not involve S3.** L204 defines it by the fidelity conditions of Part V, which are (F1) and (F2). Non-circular dependence is not a fidelity condition.
- **L168 fixes that the table asks Lea's question,** because the table has Lea's (C, 𝒬). Both S81 readers decided O33 on this Part III passage (F11 L153), and Claude's pre-ruling record cites L168 (determination packet O33).
- **On R-τ-mech, L272 makes Lea's joint contract "not a contract on which an account can be claimed".** The verdict claims no account.
- **So on R-τ-mech no word of O33's verdict is contradicted.** Atria's point 4 holds for O33. One consequence remains, and the case does not address it: on R-τ-mech, no account of Lea's joint question could be claimed at all.

**O5.** The fixed verdict: "This is a legitimate narrowing. The limit follows from a part of her account." That says she has an account on the narrowed contract.
- On R-τ-mech, leaving the yeast out sets an input and replaces no mechanism component.
- Unless the narrowed contract also holds an edit that removes a mechanism commitment, S3 has no witness, and L272 bars any account.
- The situation does not list the contract's edits. So the verdict flips on every narrowed contract that lacks such an edit.

Atria's point 4 holds for O5.

**Part VII's production case.** With Γ = {L := H cot θ}, no edit in C removes or replaces the law component: C holds interventions on H and θ, and by L120 those replace the input components. So S3 fails on R-τ-mech. But L338 claims only "faithful", and L286 says only that the reversed calculation fails (F2), so no sentence is contradicted. Atria's point 3 holds as a tension.

**O7, which is not in the frozen position.** Claude's check `W19 W20 Mimo holes.md` also named O7. Neither the brief nor Atria takes it up.
- Its fixed verdict, "Ines has a genuine explanation, a coarse one", claims an account.
- Its situation gives the contract: spread the salt, or sweep it off at once. Both edits set the salt port and replace no mechanism component.
- So on R-τ-mech S3 has no witness, and L272 bars an account.

This supports the narrowed finding. It is not added to the finding, because R3 rules on the frozen position.

**Point 5 (R-E).** Under R-E the witness lies outside C. So a contract of the baseline plus relabelings passes S3, by deleting a working block. That runs against L272: "A contract consisting only of relabelings … does not satisfy non-circular dependence". Atria's point 5 holds.

**Option B, checked further than Atria's point 7 goes.**
- **Relabelings only.** No pair in C changes the answer, so S3 fails, and L272 stays true.
- **"p because p".** S3 can hold through the installed answer. S2 still fails the candidate, so L288 stays true.
- **The production case.** do(H = h′) changes the answer. In E|∅, with the inputs as background, L is unconstrained (L120), so the answer ceases to be determined.
- **The skew case.** Removing skewness changes the answer, and dropping the skewness commitment loses the change.
- **The wording repeats the slip of part (a).** Option B evaluates E|(Γ∖G) "at (a,b)", a pair of D's edits and boundaries, without τ and σ. The text's conventions fill the gap here, as they fill it in S3. A repair should not carry the slip it was written to remove.
- **Atria's typing sentence fits the text.** It agrees with L248's "active component" and with every Part VI example (L324–328), in each of which Γ is a set of components or constraints. It types Γ, which option B's wording leaves untyped. Once Γ holds only components, the phrase "not in Γ" is redundant.

### 4. Ruling: NARROWED

- **What stands:**
  - Γ is untyped, and S3's "the other boundary conditions" presupposes a type.
  - On R-τ-mech, O5's fixed verdict flips on a narrowed contract that has no edit removing a mechanism commitment.
  - On R-τ-mech, Part VII's forward organization fails S3 on its production contract.
  - Option B is preferred over option A.
- **What is withdrawn:** the O33 flip. O33's verdict asserts faithfulness (L204) and sameness of question (L168), and S3 bears on neither.

The finding, restated: "Γ in non-circular dependence is untyped. On the mechanism-only reading R-τ-mech, O5's fixed verdict flips on a narrowed contract with no edit that removes a mechanism commitment, and Part VII's forward organization fails S3 on its production contract. O33's fixed verdict does not flip. Of the brief's two repairs, option B is preferred over option A."

### The repairs, changed after the cross-examination (R6)

Option B stays preferred, and it stays a change of claim. Both wording changes below were made after the cross-examination.

1. **S3 under option B names the translation.**
   - Reason: the slip of part (a) recurs in option B's text.
   - It was found while checking Atria's points 1 and 7. Atria did not raise it.

   > "There exist (a,b) ∈ C and a nonempty block G ⊆ Γ such that the answer profile at (a,b) differs from its value at (1,b₀), or is not determined there in the claimed way, and in E|(Γ∖G), evaluated at (τ(a),σ(b)) and at (1,σ(b₀)) with the named background fixed, that difference is lost or the answer ceases to be determined."
2. **L246 gains a typing sentence.**
   - Reason: option B leaves Γ untyped, and the untyped Γ is the defect.
   - It was prompted by Atria's point 7. It is reworded to drop the redundant clause.

   > "The commitments Γ are components of E; the boundary values of E belong to the named background of Part VI."

Option A is unchanged as the alternative.

---

## Further counterexamples (R4)

### Item 1. Derivation 3: holds against file 10, added as F4

**What Atria claims.** Derivation 3 of file 10 is false as stated, "in exactly the way Part XV's own defeat class describes".
- **The claim**, L569: "Let t be selected on a finite history H ⊊ C. For every (a,b) ∈ C∖H there exists a transport t′, also surviving on H, with a different value at (a,b)."
- **The proof**, L571: "Alter L_j(a,b) for one (a,b) ∉ H to any other admitted relation; the result survives on H and differs at (a,b)."

**Atria's instance.**
- D = E. There is one port x with domain {0,1} and one component j: x = u. At the boundary b₀, u = 1.
- A = {1, do(x=0), do(x=1)}, and C is those three edits at b₀.
- The population is 𝒯 = {t, t\*}. t is the identity transport. t\* has π\*(x) = 1 − x, with τ\*, σ\* and λ\* the identity.
- H = {(1,b₀)}, and survival requires fidelity on H.

**The check against the text.**
- **"Selected"**, L210 = F11 L197: "There is a population 𝒯 of candidate transports, a variation operator μ on 𝒯, a finite history H ⊆ C of edit–boundary pairs actually encountered, and a survival condition requiring fidelity on H. The transport t is a member of 𝒯 that survived." Atria names no μ. Any μ on 𝒯 will do, for example the exchange of t and t\*. The other clauses hold.
- **Fidelity on H**, which is (F1) and (F2) (L204):
  - t is faithful at (1,b₀): π[{1}] = {1} = Sol_E(1,b₀).
  - t\* is not faithful there: π\*[{1}] = {0}.
  - (F1) holds for both, because λ and τ are the identity and E = D.

  See the script, part 5.
- **The survivors are {t}.** At (do(x=0),b₀), which lies in C∖H, no member of 𝒯 that survived H differs from t.
- **The words fix the population reading.** "Surviving" is L210's word: t "is a member of 𝒯 that survived". Part XV reads Derivation 3 the same way at L539: "A non-fallible selected transport. A selection history H ⊊ C whose survivor is determined on C∖H. This refutes Derivation 3." Atria's instance is such a history. On the weaker reading, "any transport faithful on H", the claim does hold here: π′ ≡ 1 is faithful on H and differs from t at (do(x=0),b₀) (script, part 5).
- **Atria's second gap: altering L_j changes the organization E**, so the result is "not obviously 'a transport'". A transport runs "from an organization D to an organization E" (L198), so an altered relation gives a transport to another organization. The proof's wording is loose, not false. This is not a separate defect.

**Ruling: the item holds.** Under file 10's stated assumptions, Derivation 3 is false, and Atria's instance meets the description of Part XV's entry at L539. It is added as F4, offered by Atria.

**The defect is already known and already repaired.**
- File 11 records the claim change in its header, F11 L5: "One claim changes: Derivation 3, whose unqualified form gave the wrong verdict on the audit's case O48 and whose proof already assumed the qualification (Semantics results S75)".
- File 11's Derivation 3, at F11 L562, holds only at a pair "at which some t′ ∈ 𝒯, also surviving on H, has a different value from t". On Atria's instance no such t′ exists. F11 L534 calls that case "the theorem's own qualification, not a refutation".
- The brief itself mentions this precedent, in its F1 section under "A precedent".

So F4 is new to the S88 findings but not to the project.

> **F4 (offered by Atria, further item 1).** Derivation 3 of file 10 (L569–571) is false under its stated assumptions. A population whose only survivor on H is t leaves t determined on C∖H (the instance above), which is Part XV's defeater at L539. File 11 repairs it by a recorded change of claim.

**The proposed repair.** File 11's qualified Derivation 3 as it stands (F11 L560–566), with its Part XV entry (D) at F11 L534. File 10 is not rewritten. If it is corrected, the correction points to file 11's change of claim.

**Atria's own repair is not adopted.** Atria proposes: "for every (a,b) ∈ C∖H there exists a member of T, faithful on H, differing from t at (a,b), provided the population admits more than one faithful member". This is false:
- Let x have domain {0,1,2}, with j: x = u and u = 1 at b₀. The edits are 1, do(x=0) and do(x=2). H = {(1,b₀)}, and E = D.
- Let 𝒯 = {t, t′}, where t is the identity and π′ sends 0 to 0, 1 to 1 and 2 to 0.
- Both members are faithful on H, so the population has more than one faithful member.
- At (do(x=0),b₀) the two agree, so no member differs from t there (script, part 6).

File 11's qualification, stated pair by pair, does not have this fault.

### Item 2. Non-vacuity's record clause: does not hold

**What Atria claims.** The record clause cannot be checked from inside (E), so "(E) alone cannot detect the sufficiency failure attack (A) describes — a candidate on a silently narrowed contract with a selected transport". Atria calls this "not a counterexample to a stated theorem".

**The check.**
- The clause "every physically admitted edit excluded from C is excluded by a stated scope, not silently" (L272) is part of non-vacuity, and non-vacuity is a conjunct of (E) (L277).
- A silently narrowed contract fails that clause. L290 says so: "An account whose only substantive contrast is one that no physically admitted edit realizes fails non-vacuity by having a silently narrowed contract."
- Attack (A) (L68) asks for a candidate "on a physically admitted contract".
- L41 puts scope-honesty in the record on purpose: a narrowed contract "is caught by the requirement that the exclusion be stated".

So (E) does exclude the case. What Atria describes is that the exclusion is checked in the record rather than in the relations.

**Ruling: the item does not hold.**

**A note, not a finding.** L246 ("each a condition on supplied relations under the changes in C") and L280 ("Every conjunct is a condition on how supplied relations behave under the changes in C"), which are F11 L233 and L267, do not describe non-vacuity's record clause. That clause concerns edits outside C and whether their exclusion is stated. This is a prose inaccuracy, and it lies outside Part XV's list.

### Item 3. S2's "as a component": a variant of F3, does not hold

**What Atria claims.** S2's words "as a component" bar a coarse account made of a single component whose relation "is the answer". The word "unanalysed" should be glossed as "not anchored under (F1)". Atria adds: "No text presents such an account, so no verdict conflicts".

**The check.** S2 is a sentence of non-circular dependence, so under R4 the item is checked as a variant of F3.
- **The words.** S2 (L270): "The target's answer does not appear, at the declared grain, as an unanalysed boundary input or as a component".
- **The paragraph keeps the answer and the answer profile apart.** S1 says "The answer follows by evaluating E", S2 says "The target's answer", and S3 says "the answer profile changes". A component whose relation yields the answer when evaluated, such as L := H cot θ or z = 2x + 1, is a dependence, not the answer.
- **File 11 names what S2 is aimed at.** F11 L275: "an account whose only substantive component restates the answer it was asked for". File 11 also protects coarse dependence, at F11 L279: "It does not reject a coarse dependence for omitting finer workings or an instrument".
- **Atria offers no instance and no verdict conflict.**

**Ruling: the item does not hold.** The gloss is not adopted, and S2 stays unchanged under option B.

### Item 4. Derivation 5: does not hold

**What Atria claims.** The contract-as-organization construction in Derivation 5 is "a sketch with a regress, not a proof". Atria adds: "Nothing here is false".

**The check.**
- L587 names ports, components and admitted edits for a contract and supplies no relations L_j(a,b). Atria describes this accurately.
- Derivation 5 is not on Part XV's list, since L543 names Derivations 1–3.
- The brief's search for further counterexamples covered only Derivations 1–3, (T1), (T2) and the four conditions.

**Ruling: the item does not hold as a counterexample.** It is outside the scope of the defeat list.

### Item 5. What Atria tried: no counterexample offered

Atria tried Derivation 1; (T1) and its composition sentence; (I2), (I4), (O1) and (CT2); the finite monotone theorem; attempts on sufficiency and necessity; and Derivations 4 and 6–9. It offers no counterexample.

- **The Derivation 1 "imprecision"** is settled by (O) and L120, as shown under F1.
- **The identity account (E = D).** Atria records that it passes all four conditions trivially, and does not offer it as a sufficiency failure. It is not ruled on here.
- **Spot checks agree with Atria.**
  - (T1)'s composition works with τ = τ₂∘τ₁ when τ₁(a) lies among the edits that the second relation preserves. That is what "when intermediate scopes agree" (L374) supplies.
  - (I2) at L342 is factorization through g.

---

## Changes to the repairs, collected (R6)

Every change below was made after the cross-examination.

| repair | change | reason | prompted by |
|---|---|---|---|
| F1, clause (ii), premise | "the same subnetwork of D with port translations onto the same ports of D" | The P and Q instance: two faithful candidates whose anchor-preserving bijections pair components that are not of one kind | The reader's check of Atria's F1 point 7 (the composition step) |
| F1, clause (ii), conclusion | "so far as (F1), (F2) and (A) reach, the two are one account on C" | The premises give neither non-circular dependence nor non-vacuity | Atria's F1 point 7 caveat |
| F1, smaller alternative wording | Not adopted as it stands | It fails on the same P and Q pair | The reader's check |
| F2 erratum | Adds "whenever z, Sz, …, S^{n−1}z lie in that scope" | The scope {0} instance | Atria's F2 point 5, which describes the erratum as scoping ε "to every reached state" |
| F3, option B | Names (τ(a),σ(b)) and (1,σ(b₀)) | Option B's text repeats the slip of part (a) | The reader's check of Atria's F3 points 1 and 7 |
| F3, typing of Γ | A sentence added at L246 | Option B alone leaves Γ untyped | Atria's F3 point 7, reworded |
| F4 | File 11's qualified Derivation 3, already in file 11 | Atria's instance | Atria's further item 1; Atria's own wording rejected |

**What does not change.**
- No change moves a repair between erratum and change of claim.
- F1 stays a change of claim, F2 stays an erratum, and F3 option B stays a change of claim.
- No preferred option changes: option B stays preferred to option A.

## What this reading does not do

- It does not read Mimo's reply. Under R5, that reply is read by a reader who has read neither Atria's reply nor this reading, starting from the positions frozen in R3.
- It does not put the two readings side by side. That comes after both are written.
- It does not edit any authority file. Files 10 and 11 were read only.
- It does not use Atria's reasoning file.

---

## Appendix: script and output

The script is run with `python3`. Every relation and number is computed in exact rational arithmetic, except Lip(T) and e₂ in part 4, which are printed in floating point. Their gap from the bound, 10.101 against 10.002, is about 0.1.

- Parts 1–3 are the F1 instances and the P and Q instance.
- Part 4 is the (T2) counterexamples.
- Part 5 is Atria's Derivation 3 instance.
- Part 6 is the test of Atria's proposed repair.

```python
# S88 reading of Atria's reply: exact checks (run with python3).
from fractions import Fraction as Fr
from itertools import permutations, product
import math

# ---------- affine sets over Q: solve linear equations, project, compare ----------
def rref(M):
    M=[r[:] for r in M]; piv=[]; r=0; n=len(M[0])-1 if M else 0
    for c in range(n+1):
        p=next((i for i in range(r,len(M)) if M[i][c]!=0),None)
        if p is None: continue
        M[r],M[p]=M[p],M[r]; pv=M[r][c]; M[r]=[v/pv for v in M[r]]
        for i in range(len(M)):
            if i!=r and M[i][c]!=0:
                f=M[i][c]; M[i]=[a-f*b for a,b in zip(M[i],M[r])]
        piv.append(c); r+=1
        if r==len(M): break
    return M[:r],piv
def solve(eqs,ports):
    n=len(ports); ix={p:i for i,p in enumerate(ports)}
    rows=[]
    for co,k in eqs:
        row=[Fr(0)]*(n+1)
        for p,v in co.items(): row[ix[p]]+=Fr(v)
        row[n]=Fr(k); rows.append(row)
    if not rows: return ([Fr(0)]*n,[[Fr(int(i==j)) for j in range(n)] for i in range(n)])
    R,piv=rref(rows)
    if n in piv: return None
    free=[c for c in range(n) if c not in piv]; pt=[Fr(0)]*n
    for row,c in zip(R,piv): pt[c]=row[n]
    dirs=[]
    for f in free:
        d=[Fr(0)]*n; d[f]=Fr(1)
        for row,c in zip(R,piv): d[c]=-row[f]
        dirs.append(d)
    return (pt,dirs)
def rank(V):
    if not V: return 0
    return len(rref([v[:]+[Fr(0)] for v in V])[1])
def proj(A,ports,onto):
    if A is None: return None
    ix=[ports.index(q) for q in onto]; p,D=A
    return ([p[i] for i in ix],[[d[i] for i in ix] for d in D])
def same(A,B):
    if A is None or B is None: return A is None and B is None
    (p,V),(q,W)=A,B
    rv,rw=rank(V),rank(W)
    if rv!=rw or rank(V+W)!=rv: return False
    diff=[a-b for a,b in zip(q,p)]
    return rank(V+[diff])==rv if any(diff) else True

# ---------- organizations: component = (footprint, eqs(edit)) ----------
CS=[Fr(c) for c in (-3,-1,0,1,2,5,Fr(7,3))]
EDITS=['id']+[('do_x',c) for c in CS]
def xin(e): return [({'x':1},0)] if e=='id' else [({'x':1},e[1])]   # x=u, u=0 at b0; do(x=c) replaces it
def lin(out,inp,a,b): return lambda e:[({out:1,inp:-Fr(a)},Fr(b))]  # out = a*inp + b
def sol(org,names,e):
    ports=sorted({p for n in names for p in org[n][0]})
    return ports,solve([q for n in names for q in org[n][1](e)],ports)
def rel(org,k,e,onto): ps,s=sol(org,[k],e); return proj(s,ps,onto)
def one_kind(o1,k1,o2,k2):
    f1,f2=o1[k1][0],o2[k2][0]
    if len(f1)!=len(f2): return False
    return any(all(same(rel(o1,k1,e,list(f1)),rel(o2,k2,e,list(pm))) for e in EDITS) for pm in permutations(f2))
def F1(D,E,lam,expose):
    # lam[k] = anchor subnetwork (names in D); expose[k] = D-ports that k's footprint translates to (in footprint order)
    def anchored(k,e):
        ps,s=sol(D,lam[k],e); return proj(s,ps,list(expose[k]))
    return all(same(anchored(k,e),rel(E,k,e,list(E[k][0]))) for k in E for e in EDITS)
def F2(D,E):
    Dp=sorted({p for n in D for p in D[n][0]}); Ep=sorted({p for n in E for p in E[n][0]})
    return all(same(proj(sol(D,list(D),e)[1],Dp,Ep),sol(E,list(E),e)[1]) for e in EDITS)
def Aq(D,E,q):
    Dp=sorted({p for n in D for p in D[n][0]}); Ep=sorted({p for n in E for p in E[n][0]})
    return all(same(proj(sol(D,list(D),e)[1],Dp,[q]),proj(sol(E,list(E),e)[1],Ep,[q])) for e in EDITS)
def full_bijections(E1,E2):
    k1=list(E1); k2=list(E2)
    if len(k1)!=len(k2): return 0,0
    tot=good=0
    for pm in permutations(k2):
        tot+=1; good+=all(one_kind(E1,a,E2,b) for a,b in zip(k1,pm))
    return tot,good

print("=== Part 1. F1 counter-instance 1: D = {x=u, y=2x, z=y+1}, Q reads z")
D3={'jx':(('x',),xin),'jy':(('x','y'),lin('y','x',2,0)),'jz':(('y','z'),lin('z','y',1,1))}
E1={'kx':(('x',),xin),'ky':(('x','y'),lin('y','x',2,0)),'kz':(('y','z'),lin('z','y',1,1))}
E2={'mx':(('x',),xin),'mz':(('x','z'),lin('z','x',2,1))}
L1={'kx':['jx'],'ky':['jy'],'kz':['jz']}; X1={'kx':('x',),'ky':('x','y'),'kz':('y','z')}
L2={'mx':['jx'],'mz':['jy','jz']};        X2={'mx':('x',),'mz':('x','z')}
for n,E,L,X in (('E1',E1,L1,X1),('E2',E2,L2,X2)):
    print(f"  {n}: (F1) {F1(D3,E,L,X)}  (F2) {F2(D3,E)}  (A) {Aq(D3,E,'z')}")
for a in E1: print(f"  E1.{a} one kind with:",[b for b in E2 if one_kind(E1,a,E2,b)])
for b in E2: print(f"  E2.{b} one kind with:",[a for a in E1 if one_kind(E2,b,E1,a)])
print("  component counts",len(E1),len(E2),"-> no bijection")

print("\n=== Part 2. F1 counter-instance 2: D = {x=u, y=x+1, z=y+1, w=z}, Q reads w")
D4={'jx':(('x',),xin),'jy':(('x','y'),lin('y','x',1,1)),'jz':(('y','z'),lin('z','y',1,1)),'jw':(('z','w'),lin('w','z',1,0))}
Ea={'ax':(('x',),xin),'az':(('x','z'),lin('z','x',1,2)),'aw':(('z','w'),lin('w','z',1,0))}
Eb={'bx':(('x',),xin),'by':(('x','y'),lin('y','x',1,1)),'bw':(('y','w'),lin('w','y',1,1))}
La={'ax':['jx'],'az':['jy','jz'],'aw':['jw']}; Xa={'ax':('x',),'az':('x','z'),'aw':('z','w')}
Lb={'bx':['jx'],'by':['jy'],'bw':['jz','jw']}; Xb={'bx':('x',),'by':('x','y'),'bw':('y','w')}
for n,E,L,X in (('Ea',Ea,La,Xa),('Eb',Eb,Lb,Xb)):
    print(f"  {n}: (F1) {F1(D4,E,L,X)}  (F2) {F2(D4,E)}  (A) {Aq(D4,E,'w')}")
t,g=full_bijections(Ea,Eb); print(f"  bijections Ea->Eb: {t}; making every pair of one kind: {g}")
for a in Ea: print(f"  Ea.{a} one kind with:",[b for b in Eb if one_kind(Ea,a,Eb,b)])

print("\n=== Part 3. F1 repair, clause (ii): one anchor subnetwork, different exposed ports")
# Both candidates anchor two components to the SAME subnetwork {jy,jz}; they expose different D-ports.
P={'px':(('x',),xin),'py':(('x','y'),lin('y','x',2,0)),'pz':(('x','z'),lin('z','x',2,1))}
LP={'px':['jx'],'py':['jy','jz'],'pz':['jy','jz']}; XP={'px':('x',),'py':('x','y'),'pz':('x','z')}
Q={'qx':(('x',),xin),'qy':(('x','y'),lin('y','x',2,0)),'qz':(('y','z'),lin('z','y',1,1))}
LQ={'qx':['jx'],'qy':['jy','jz'],'qz':['jy','jz']}; XQ={'qx':('x',),'qy':('x','y'),'qz':('y','z')}
for n,E,L,X in (('P',P,LP,XP),('Q',Q,LQ,XQ)):
    print(f"  {n}: (F1) {F1(D3,E,L,X)}  (F2) {F2(D3,E)}  (A) {Aq(D3,E,'z')}")
kp,kq=list(P),list(Q)
for pm in permutations(kq):
    anchors_equal=all(set(LP[a])==set(LQ[b]) for a,b in zip(kp,pm))
    ports_equal=all(set(XP[a])==set(XQ[b]) for a,b in zip(kp,pm))
    kinds=[one_kind(P,a,Q,b) for a,b in zip(kp,pm)]
    print(f"  phi={dict(zip(kp,pm))}: same subnetworks {anchors_equal}; same exposed D-ports {ports_equal}; pairs of one kind {kinds}")

print("\n=== Part 4. (T2) counterexamples, exact")
def run(S,T,pi,z0,y0,n):
    z,y,out=z0,y0,[]
    for _ in range(n+1): out.append((pi(z),y)); z,y=S(z),T(y)
    return out
bnd=lambda eps,L,n: eps*sum(L**k for k in range(n))
e=Fr(1,10)
r=run(lambda z:2*z+e,lambda y:2*y,lambda z:z,Fr(0),Fr(-1),3)
print("  2a (two-run reading R, y0=-1): e_n =",[abs(a-b) for a,b in r],"; (T2) bound =",[bnd(e,2,n) for n in range(4)])
r=run(lambda z:2*z+e,lambda y:2*y,lambda z:z,Fr(0),Fr(0),3)
print("  2a on reading M (same start): e_n =",[abs(a-b) for a,b in r],"<= bound:",all(abs(a-b)<=bnd(e,2,n) for n,(a,b) in enumerate(r)))
# 2b: S=id on Q, pi(z)=(z,0), T(a,b)=(a+100b, b+1/10); e_n^2 exact
T2b=lambda p:(p[0]+100*p[1],p[1]+e)
y=(Fr(0),Fr(0)); sq=[]
for n in range(3): sq.append(y[0]**2+y[1]**2); y=T2b(y)
print("  2b: e_n^2 =",sq,"; (T2) bound^2 with L=1:",[bnd(e,1,n)**2 for n in range(3)])
lam=(10002+math.sqrt(10002**2-4))/2; LipT=math.sqrt(lam)
print(f"  2b: Lip(T) = {LipT:.6f}; bound at n=2 with L=Lip(T): {0.1*(1+LipT):.6f}; e_2 = {math.sqrt(100.04):.6f}")
# one-step discrepancy of 2b at any z: d((z,0),(z,1/10)) = 1/10 exactly
r=run(lambda z:2*z+e+z*z,lambda y:2*y,lambda z:z,Fr(0),Fr(0),2)
print("  2c: e_n =",[abs(a-b) for a,b in r],"; bound =",[bnd(e,2,n) for n in range(3)],"; step discrepancies at z0,z1:",[e+Fr(0)**2,e+Fr(1,10)**2])

print("\n=== Part 5. Derivation 3 (file 10), Atria's instance")
# D = E: one port x in {0,1}; component j: x=u; b0: u=1. Edits: 1, do(x=0), do(x=1). C = all three at b0. H = {(1,b0)}.
def SolD(a): return {1} if a=='1' else {0} if a=='do0' else {1}
C=['1','do0','do1']; H=['1']
def faithful_at(pi,a): return {pi(v) for v in SolD(a)}==SolD(a)   # (F2) with tau,sigma,lambda identity; (F1) holds since E=D and lambda,tau identity
t=lambda v:v; tstar=lambda v:1-v
for name,pi in (('t',t),('t*',tstar)):
    print(f"  {name}: faithful on H {all(faithful_at(pi,a) for a in H)}; values on C:",{a:sorted({pi(v) for v in SolD(a)}) for a in C})
surv=[n for n,pi in (('t',t),('t*',tstar)) if all(faithful_at(pi,a) for a in H)]
print("  survivors in population {t,t*}:",surv,"-> survivor determined on C\\H")
# weak reading: any transport faithful on H
allmaps=[dict(zip((0,1),img)) for img in product((0,1),repeat=2)]
weak=[m for m in allmaps if all({m[v] for v in SolD(a)}==SolD(a) for a in H)]
print("  all maps pi:{0,1}->{0,1} faithful on H:",weak)
print("  of these, differing from t at do(x=0):",[m for m in weak if {m[v] for v in SolD('do0')}!={0}])

print("\n=== Part 6. Atria's proposed repair of Derivation 3, tested")
# x in {0,1,2}; j: x=u, u=1 at b0; edits 1, do(x=0), do(x=2); H = {(1,b0)}; E = D; tau, sigma, lambda identity.
def Sol3(a): return {'1':{1},'do0':{0},'do2':{2}}[a]
C3=['1','do0','do2']; H3=['1']
pis={'t':{0:0,1:1,2:2},"t'":{0:0,1:1,2:0}}
for n,m in pis.items():
    print(f"  {n}: faithful on H {all({m[v] for v in Sol3(a)}==Sol3(a) for a in H3)}; values:",{a:sorted({m[v] for v in Sol3(a)}) for a in C3})
print("  population has two members faithful on H; at (do(x=0),b0) they agree -> no member differs from t there")
```

Output:

```
=== Part 1. F1 counter-instance 1: D = {x=u, y=2x, z=y+1}, Q reads z
  E1: (F1) True  (F2) True  (A) True
  E2: (F1) True  (F2) True  (A) True
  E1.kx one kind with: ['mx']
  E1.ky one kind with: []
  E1.kz one kind with: []
  E2.mx one kind with: ['kx']
  E2.mz one kind with: []
  component counts 3 2 -> no bijection

=== Part 2. F1 counter-instance 2: D = {x=u, y=x+1, z=y+1, w=z}, Q reads w
  Ea: (F1) True  (F2) True  (A) True
  Eb: (F1) True  (F2) True  (A) True
  bijections Ea->Eb: 6; making every pair of one kind: 0
  Ea.ax one kind with: ['bx']
  Ea.az one kind with: []
  Ea.aw one kind with: []

=== Part 3. F1 repair, clause (ii): one anchor subnetwork, different exposed ports
  P: (F1) True  (F2) True  (A) True
  Q: (F1) True  (F2) True  (A) True
  phi={'px': 'qx', 'py': 'qy', 'pz': 'qz'}: same subnetworks True; same exposed D-ports False; pairs of one kind [True, True, False]
  phi={'px': 'qx', 'py': 'qz', 'pz': 'qy'}: same subnetworks True; same exposed D-ports False; pairs of one kind [True, False, False]
  phi={'px': 'qy', 'py': 'qx', 'pz': 'qz'}: same subnetworks False; same exposed D-ports False; pairs of one kind [False, False, False]
  phi={'px': 'qy', 'py': 'qz', 'pz': 'qx'}: same subnetworks False; same exposed D-ports False; pairs of one kind [False, False, False]
  phi={'px': 'qz', 'py': 'qx', 'pz': 'qy'}: same subnetworks False; same exposed D-ports False; pairs of one kind [False, False, False]
  phi={'px': 'qz', 'py': 'qy', 'pz': 'qx'}: same subnetworks False; same exposed D-ports False; pairs of one kind [False, True, False]

=== Part 4. (T2) counterexamples, exact
  2a (two-run reading R, y0=-1): e_n = [Fraction(1, 1), Fraction(21, 10), Fraction(43, 10), Fraction(87, 10)] ; (T2) bound = [Fraction(0, 1), Fraction(1, 10), Fraction(3, 10), Fraction(7, 10)]
  2a on reading M (same start): e_n = [Fraction(0, 1), Fraction(1, 10), Fraction(3, 10), Fraction(7, 10)] <= bound: True
  2b: e_n^2 = [Fraction(0, 1), Fraction(1, 100), Fraction(2501, 25)] ; (T2) bound^2 with L=1: [Fraction(0, 1), Fraction(1, 100), Fraction(1, 25)]
  2b: Lip(T) = 100.009999; bound at n=2 with L=Lip(T): 10.101000; e_2 = 10.002000
  2c: e_n = [Fraction(0, 1), Fraction(1, 10), Fraction(31, 100)] ; bound = [Fraction(0, 1), Fraction(1, 10), Fraction(3, 10)] ; step discrepancies at z0,z1: [Fraction(1, 10), Fraction(11, 100)]

=== Part 5. Derivation 3 (file 10), Atria's instance
  t: faithful on H True; values on C: {'1': [1], 'do0': [0], 'do1': [1]}
  t*: faithful on H False; values on C: {'1': [0], 'do0': [1], 'do1': [0]}
  survivors in population {t,t*}: ['t'] -> survivor determined on C\H
  all maps pi:{0,1}->{0,1} faithful on H: [{0: 0, 1: 1}, {0: 1, 1: 1}]
  of these, differing from t at do(x=0): [{0: 1, 1: 1}]

=== Part 6. Atria's proposed repair of Derivation 3, tested
  t: faithful on H True; values: {'1': [1], 'do0': [0], 'do2': [2]}
  t': faithful on H True; values: {'1': [1], 'do0': [0], 'do2': [0]}
  population has two members faithful on H; at (do(x=0),b0) they agree -> no member differs from t there
```
