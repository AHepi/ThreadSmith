# S88: Mimo's reply in three parts, and the settled positions

*23 September 2026. Written by a Claude subagent for the orchestrator after the three part readings were finished. This writer wrote none of the findings and none of the three part readings. It read the S88 rule (`results/S88 How the cross-examination will be read - written after Atria's reply arrived, before it was opened.md`, committed at cc87b45) as amended before sending by `results/S88 Mimo's reply in three parts - how it will be read, written before sending.md` (committed at db05b18).*

## What this file does

It does three things.

1. It records, for each finding, Mimo's verdict and the fresh reader's ruling on Mimo's reply. The three readings are copied verbatim into `results/S88 Mimo reading parts/` as `F1 reading.md`, `F2 reading.md` and `F3 reading.md`, and their check scripts are copied into `checks/` there.
2. It puts the Mimo readings beside `results/S88 Reading of Atria's reply - the three defects.md` (R5) and resolves each difference from the theory text.
3. It gives **the settled position** on each finding after both outside replies:
   - the status (UPHELD, NARROWED or WITHDRAWN);
   - the final repair wording for revision 2, as exact text;
   - every change from the position after Atria's reading, with its reason.

It applies the rules on S88 in the revision 2 plan (`02 plan for revision 2 and its test.md`, 1.3.2–1.3.4). Those rules were fixed before any S88 reply was read.

### What was read, and what was not

- **Read:**
  - the rule and the note;
  - the three Mimo part readings;
  - the reading of Atria's reply;
  - the repair sections of the F1 and F2 part briefs in `tests/`;
  - file 11 at every anchor used below, and file 10 where the readings cite it;
  - the held entries W19, W20 and W31, and W24.1, in `tests/Revision 2 - change list, draft of 23 September.md`;
  - the revision 2 plan's section 1.3 and the item skeleton's conflicts, both in the session scratchpad.
- **Run again:** the readings' scripts `f1_check.py`, `f2_check.py` and `f3_check.py`. Their outputs match what the readings report.
- **Written and run for this file:** one new script, for the Derivation 10 point (appendix).
- **Not opened:**
  - Mimo's replies, receipts and reasoning files, for any part, and the files of the failed single Mimo call;
  - Atria's reply and reasoning;
  - anything in the S87 or S90 returns folders.

  So every statement below about what Mimo argued rests on the part readings, which quote and check the replies.

### The late rule (R7)

R7's late-rule statement does not go with Mimo's parts. The rule was committed at 15:36 UTC, the note at 17:47:42 UTC, and the first part was asked for at 17:48:46 UTC. The statement still goes with every report of Atria's reply, and it goes with the side-by-side comparison below wherever that comparison reports Atria's reading.

### The receipts (R1)

All three parts were accepted. Each receipt shows finish "stop", and each reply ends with END OF REPORT.

| part | attempts | accepted on | reply characters | user_sha256 (first 12) | matches the part brief |
|---|---|---|---|---|---|
| F1 | 3 | attempt 3 (attempts 1 and 2: status 0, no content) | 11,860 | 45e210160953 | yes |
| F2 | 1 | attempt 1 | 12,028 | 9c24e62f7ef1 | yes |
| F3 | 1 | attempt 1 | not stated in the reading | 370ba7cb2f64 | yes |

**So no finding is "not examined by Mimo".**

### The comparison has to state where each reader started

The two sets of readings started from different positions, as the note says the comparison must record.

- **Atria's reader** started from the positions frozen in the rule at 15:35 UTC.
- **Mimo's three readers** started from the positions after Atria's reading.

So a label from one set can differ from a label from the other on the same finding without any conflict between them. Where that happens, it is said below.

## Summary

| finding | Atria's verdict; reading's ruling (from the frozen position) | Mimo's verdict; reading's ruling (from the post-Atria position) | **settled status** | repair for revision 2 |
|---|---|---|---|---|
| **F1**, Derivation 2 | F1: UPHELD; **UPHELD** | F1: UPHELD; **UPHELD** | **UPHELD** | "Same anchors, one account", a change of claim. Four wording changes since the post-Atria position. |
| **F2**, (T2) | F2: UPHELD; **UPHELD** | F2: PARTLY UPHELD; **NARROWED** ((h1) restated) | **NARROWED** ((h1) is an undefined \(e_n\), not an omitted hypothesis on starts) | The erratum. S, T and d are introduced, "the stated scope" becomes "a stated scope", and the unequal-start clause is dropped. |
| **F3**, non-circular dependence | F3: PARTLY UPHELD; **NARROWED** (the O33 flip withdrawn) | F3: PARTLY UPHELD; **UPHELD** (the narrowed finding, with a precision) | **NARROWED** (from the finding as sent; the narrowed finding stands) | Option B with the deletion rider (plan 1.3.4), an explicit "lost" test, a wider typing sentence, and one clause at Part VI. |

Neither Mimo reading adds a new finding. Atria's F4 was not put to Mimo, and this file says nothing new about it.

---

## F1. Derivation 2, "Indistinguishable is identical"

### Mimo's verdict

**"F1: UPHELD".**

Mimo found both counter-instances valid under every stated assumption. It judged that all four defences fail and that the repair is sound, and it called the classification (false as stated, remedied by a change of claim) apt.

### The ruling on Mimo's reply (`F1 reading.md`): UPHELD

- **The finding.**
  - Both instances meet lines 108, 120, 158, 204 and 248 of file 10, checked exactly for every real c.
  - The component half fails under every reading the text supports.
  - No words state the one reading that would save it, pairing through shared anchors. The words "their components", the colon at line 561, the title and line 23 all speak against that reading.
- **Where Mimo was wrong.**
  - **Mimo endorsed the premise of (ii) as sent** ("λ′(φ(k)) = λ(k) … up to port translation") and called the proof valid.
    - That premise is false on the reader's instance E₃, E₄. There, two components anchored to one subnetwork expose different ports, and a pair under φ is not of one kind.
    - The current premise ("port translations onto the same ports of D") excludes the instance.
    - This bears only on wording already tightened, so it neither reopens the tightening nor counts as support for it.
  - **Mimo praised the smaller alternative wording.** It fails on the same instance.
- **Five small slips in the reply:**
  - one paraphrase inside quotation marks;
  - "precisely when an anchor merges components";
  - "non-input components";
  - an incomplete list of projected relations;
  - "the only one that typechecks".
- **Two points survive in narrowed form and bear on current wording.**
  - "One account" is never defined once the repair drops the colon of line 561.
  - The sentence after (K) says Derivation 1 uses kinds "in this sense". It does not: Derivation 1 compares a component with an anchor subnetwork of D, read on C directly.

### Side by side with Atria's reading (R5)

Both readings rule UPHELD, so there is no difference to resolve.

- **One counter-instance was found by both readings.** The F1 reader's E₃ and E₄ are, up to names, the Atria reading's P and Q. They share one D and one anchor subnetwork {j_y, j_z}, and z = 2x + 1 on (x, z) stands against z = y + 1 on (y, z).
- **The second finding was not independent.** The F1 reader knew the current premise, which the note gives in words, and that premise points at the gap. The agreement is recorded, not counted.
- **Mimo, which saw only the wording as sent, missed the gap.** Atria did not raise it either. The Atria reading found it while checking Atria's composition step.

### The settled position: **UPHELD**

- **The finding.** The component half of Derivation 2 is false under its stated assumptions, and the answer-profile half is true.
- **The remedy.** It is a recorded change of claim.
- **The plan's rule.** Plan 1.3.3 says: "F1 UPHELD: take (i)". Wording (i), "Same anchors, one account", is taken with the changes below. The smaller wording (ii) is not adopted.

#### The final repair wording, exact text for revision 2

**1. Derivation 2** replaces file 11 lines 552–558, from the heading "## 2. Indistinguishable is identical" through the Consequence:

````text
## 2. Same anchors, one account

**Claim.** Let \(\mathcal E,\mathcal E'\) be candidates for the same \(p\) that both satisfy (F1), (F2) and (A) on \(C\). (i) Their answer profiles coincide on \(C\). (ii) If a bijection \(\varphi\) of their active components gives each \(k\) and \(\varphi(k)\) one anchor, the same subnetwork of \(D\) with port translations onto the same ports of \(D\), then \(k\) and \(\varphi(k)\) are of one kind on \(C\) for every \(k\); so far as (F1), (F2) and (A) reach, the two are one account on \(C\): \(\varphi\) pairs their active components, each pair of one kind on \(C\), and by (i) their answer profiles coincide.

*Proof.* (i) By (A), \(\operatorname{Ans}_E(\tau(a),\sigma(b))=\operatorname{Ans}_p(a,b)=\operatorname{Ans}_{E'}(\tau'(a),\sigma'(b))\) for every \((a,b)\in C\). (ii) By Derivation 1, \(k\) has the signature of its anchor on the ports its translation names, and \(\varphi(k)\) the signature of the same anchor on the same ports; composing the one translation with the inverse of the other gives a footprint bijection under which the two signatures, read on \(C\), coincide. ∎

Without the premise of (ii) nothing more follows: candidates that anchor different subnetworks, or cut \(D\) at different places, are different candidates with one answer profile (Derivation 9; Part VI, redundant routes). A coarsening is not a recoding (Derivation 8).

**Consequence.** Where two candidates that satisfy (F1), (F2) and (A) differ only in which component carries which anchor, the contract does not contain the distinction; a claim that one assignment is "really" right is a claim that some admitted change separates them, and must supply it. The remedy is a finer contract, which is a new question.
````

**2. The sentence after (K).** It is inserted in file 11 line 121, after "A kind is an equivalence class of components under this relation.", which is the anchor W19 reserves, sentences 1–2.

````text
A component of \(E\) and a component of \(E'\) are of one kind on \(C\) when their signatures, read on \(C\) through \(\tau\) and \(\tau'\), coincide under a footprint bijection; Derivation 2 uses kinds in this sense. Derivation 1 makes the like comparison between a component \(k\) of \(E\), read on \(C\) through \(\tau\), and its anchor \(\lambda(k)\), read on \(C\) directly with its hidden ports projected away, up to the port translation.
````

**3. Derivation 10.** It replaces the file 11 line 620 sentence "On any contract containing it, the two persistence components are of one kind (Derivation 2)." The sentences before and after it are unchanged.

````text
On any contract containing it that admits each edit for both things alike, composing \(t_1\) with the exchange of the two things gives a second transport, which sends each persistence component to the other thing's continuity subnetwork. The two things are built alike in \(P\), and their persistence components alike in \(S_1\), so the exchange carries the fidelity and the answers of \(t_1\) over to the second transport (Derivation 8); so far as (F1), (F2) and (A) reach, the two candidates are one account (Derivation 2).
````

#### Changes from the post-Atria position, with reasons

Every change below was made after the cross-examination. None of them moves the repair between erratum and change of claim.

1. **The conclusion of (ii) now says what "one account" is.**
   - **The change.** The clause "\(\varphi\) pairs their active components, each pair of one kind on \(C\), and by (i) their answer profiles coincide" is added after the colon.
   - **Reason.** File 10 gives "one account" content only through the colon of line 561. The repair dropped that colon, so the qualified conclusion named a relation that no sentence defines. The added clause restores the colon construction and adds no claim.
   - **Prompted by** Mimo's reply to part F1, point 4 ("'one account' is never formally defined"). The F1 reading's change A kept it in narrowed form.
2. **The sentence after (K) no longer says Derivation 1 uses cross-candidate kinds.**
   - **Reason.** Derivation 1 (file 11 line 546) compares a component of E, read through τ, with an anchor subnetwork of D, read on C directly. It does not compare a component of E with a component of E′ through τ and τ′.
   - **Prompted by** Mimo's reply to part F1, point 4, the breakage check on Derivation 1. The F1 reading kept it in narrowed form as change B.
   - **Settling reworded the reader's proposal.** The reader's words introduced k without naming it, and they said "in the same way" of a comparison they then described as read "directly". The settled sentence names k and says which side is read through τ and which directly.
3. **The Consequence says "candidates that satisfy (F1), (F2) and (A)" in place of "faithful candidates".**
   - **Reason.** File 11 line 191 defines "faithful on C" by "the component and global fidelity conditions of Part V", which are (F1) and (F2). (A) is "question fidelity" (line 249) and is not among them. The claim's premise includes (A).
   - **Prompted by** the F1 reader's own note. Mimo did not raise it.
4. **Derivation 10's sentence is rewritten.** Four things change:
   - "exchanging the two persistence components' anchors" becomes "composing \(t_1\) with the exchange of the two things".
   - The transport's fidelity now rests on Derivation 8.
   - "the two transports are one account" becomes "the two candidates are one account", with the qualifier of (ii).
   - The contract is restricted to one "that admits each edit for both things alike".

   The reasons follow.
   - **An exchange of anchors alone is not faithful.** If λ alone is exchanged, (F1) fails at "displace thing 1": the S₁ component that τ displaces is anchored to thing 2's continuity subnetwork, which the edit leaves alone. The exchange must run through π, τ, σ and λ together. The appendix checks this exactly: λ alone gives (F1) False, and the whole exchange gives (F1) and (F2) True. It is a defect in the repair's wording, not in the theory. It is found in settling, and it extends the F1 reader's note that Mimo "does not check the replacement's other assertion".
   - **The exchange is faithful because the two things are alike.** It is faithful because it is a structure-preserving bijection, which requires the two things to be alike in P and their components alike in S₁. File 11 line 602 carries Derivation 8. The words "built alike" state the symmetry that lines 610 and 616 imply ("two things, each with a position and a velocity"; "a component per thing").
   - **The contract must be symmetric.** Derivation 8 carries the contract along the exchange, so the second transport is faithful on C when t₁ is faithful on the exchanged C. The two are the same exactly when C admits each edit for both things alike.
   - **Derivation 2 speaks of candidates, and it carries the qualifier.** The words "so far as (F1), (F2) and (A) reach" resolve skeleton conflict 5, Derivation 10 against amended clause (ii). On a contract other than the one where line 618 calls the account adequate, nothing else supplies the rest of (E).

#### What does not change

- **The premise of (ii).** It stays "port translations onto the same ports of D". Mimo's endorsement of the premise as sent bears only on wording already tightened.
- **The proof** is unchanged. With the current premise it holds: take β = ρ′⁻¹∘ρ, which the F1 reading checks.
- **"Without the premise of (ii) nothing more follows …"** is unchanged.
- **The classification** is unchanged: a change of claim.
- **The stated costs** are unchanged, as in the brief. The slogan goes, the Consequence's reach narrows to anchor assignments, and identity of differently decomposed candidates is left undefined.
- **The smaller alternative** is not adopted. It fails on E₃ and E₄, which are the Atria reading's P and Q.

---

## F2. (T2), approximate transport

### Mimo's verdict

**"F2: PARTLY UPHELD".** Mimo judged each part of the finding separately.

- **(h2) and counterexample 2b.** Held, and in Mimo's words they carry the defect.
- **(h1) and counterexample 2a.** Not held. Mimo's reason is that the theory has no free starting error. What survives is that \(e_n\) is never defined.
- **(h3).** Held only in reduced form. Mimo rejected 2c on the "each step" reading and gave a corrected instance aimed at the scope.
- **The repair.**
  - The side note must move into the sentence.
  - "The stated scope" points at nothing.
  - The optional unequal-start clause is incoherent as placed.
  - The letter S collides with the simulation layer.
- **The classification**, a drafting omission, is right.

### The ruling on Mimo's reply (`F2 reading.md`): NARROWED

- **What stands:**
  - **(h2) with 2b.** No words say whose Lipschitz constant L is. 2b meets both stated assumptions from one start: e₂² = 2501/25 against a bound of 0.2² at L = 1.
  - **(h3) with 2c.** No words say where ε holds. Mimo's rejection of 2c rests on a reading that no words fix, and its own corrected instance breaks that same reading: its fifth step discrepancy is 7/20.
  - **The classification**, a drafting omission fixed by an erratum.
- **What is narrowed: (h1).**
  - No line of the theory introduces a second starting state. "Initial" occurs in neither file 10 nor file 11. Every comparison of D with E is at the translated point: file 10 lines 204, 234, 257, 265, 366 and 371, which are file 11 lines 191, 221, 244, 252, 351 and 356.
  - So the defect is that \(e_n\) is never defined. It is not that a hypothesis on starts was omitted.
  - 2a is a counterexample only once an outside object, y₀, is brought in.
  - The erratum's "from one state z … (so \(e_0=0\))" is exactly the missing definition.
- **Not accepted:**
  - Mimo's reduction of (h3);
  - "the same containment is needed for L". Both wordings require T to be Lipschitz globally.
- **Accepted as bearing on current wording:**
  - "the stated scope" should be "a stated scope";
  - the unequal-start clause is vacuous under the erratum's own definition;
  - the erratum never introduces S.
- **Bears only on the wording as sent:** Mimo's containment instance. It defeats the erratum as sent at n = 5. The current wording claims only n ≤ 4, where the bound holds with equality.

### Side by side with Atria's reading (R5): the rulings differ

- **The Atria reading ruled UPHELD.** It already wrote that "the missing item is best called the undefined \(e_n\), whose definition gives \(e_0 = 0\)". It accepted Atria's refutation of 2a "as far as it goes", and it held that 2a "breaks neither assumption that L376 states".
- **The F2 reading ruled NARROWED**, restating (h1).

**Resolved from the text: NARROWED.** R3 defines UPHELD as "the finding stands as stated". The finding as frozen names "matching starts" as an omitted hypothesis, and the text supports no such hypothesis:

- file 11 has no second start and no "initial";
- \(e_n\) occurs only on line 361, undefined;
- every D–E comparison is made at the translated point.

A hypothesis that the starts match presupposes two starts, and the theory has one. What line 361 omits is the definition of \(e_n\).

The two readings agree on every substantive point:
- 2b is decisive;
- 2c holds on a reading no words exclude;
- 2a needs an object the text never introduces;
- the erratum defines \(e_n\).

They differ only on whether that restatement is a narrowing. By R3's own definitions it is.

The Atria reading held that 2a "breaks neither assumption that L376 states", and the F2 reading does not dispute it. The F2 reading's further point is that 2a refutes a quantity the text does not define, not the claim as stated. That point is accepted.

### The settled position: **NARROWED**

The settled finding is the F2 reading's restatement, adopted as it stands:

> "(T2) omits two hypotheses its proof needs, namely whose Lipschitz constant (h2) and where ε holds (h3), and it leaves \(e_n\) undefined (h1), so the start is fixed by no words. On readings that leave these open it has counterexamples (2b for h2, 2c for h3). 2a is a counterexample only on a two-run reading whose second start the theory never introduces. This is a drafting omission, fixed by an erratum that restores the predecessor's hypotheses and defines \(e_n\)."

**The plan's rule (1.3.2) applies:**
- **The erratum is taken.** The rule takes the erratum "unless the S88 reading rules one of the three hypotheses false or excessive". Neither reading does. The narrowing turns (h1) into a definition, and the erratum keeps that definition word for word.
- **The general bound waits.** The rule adds it "only if neither S88 reading finds a flaw in it", and the F2 reading found one: as worded it is vacuous, because the erratum's definition makes \(e_0=0\) for every system.

#### The final repair wording, exact text for revision 2

**The erratum.** It replaces all of file 11 line 361. W24.1, which is applied, lands first at line 351 and introduces \(S_a\) as a target process and \(T_a\) as a represented process.

````text
**Approximate transport.** Let \(S\) be a target next-step process and \(T\) a represented next-step process, as \(S_a\) and \(T_a\) are in functional transport, and let \(d\) be a metric on \(X_E\). With one-step discrepancy \(d(\pi Sz,T\pi z)\le\varepsilon\) at every state \(z\) of a stated scope, and with \(T\) \(L\)-Lipschitz for \(d\), the discrepancy after \(n\) steps from one state \(z\), \(e_n=d(\pi S^nz,T^n\pi z)\) (so \(e_0=0\)), satisfies \(e_n\le\varepsilon\sum_{k<n}L^k\) whenever \(z,Sz,\dots,S^{n-1}z\) lie in that scope. (T2) Without a modulus, no accumulated bound follows. An exact question is not silently replaced by an approximate one.
````

**The proof goes through under these words.** For k < n, e_{k+1} ≤ d(πS(Sᵏz), Tπ(Sᵏz)) + d(Tπ(Sᵏz), T(Tᵏπz)) ≤ ε + L·e_k, with e₀ = 0. The first term is bounded because Sᵏz lies in the scope, and the second because T is Lipschitz globally.

**Not in revision 2: the general bound.** Under the plan's rule it waits. If a later revision wants it, it is a recorded addition, not part of the erratum, in the F2 reading's wording: "If the represented run starts instead at a state \(y\) of \(X_E\), then under the same conditions \(d(\pi S^nz,T^ny)\le L^n\,d(\pi z,y)+\varepsilon\sum_{k<n}L^k\)."
- It was checked on 2a, where it holds with equality, and on 200 random starts with no violation.
- It is not in revision 2 because the theory nowhere uses a second start.

#### Changes from the post-Atria position, with reasons

Every change was made after the cross-examination. The erratum stays an erratum.

1. **S and T are introduced and tied to functional transport.**
   - **Reason.** The post-Atria wording never introduced S. The theory's only other bare S is the simulation layer, which is a representing organization (file 11 lines 179 and 221). So a reader could take the erratum's S for the side the erratum calls T.
   - **How it is worded.** It follows W24.1's words, "target process" and "represented process". Check 1 on W24.1 had already required that W31 "say which process S is".
   - **Prompted by** Mimo's reply to part F2, point 7.
2. **"the stated scope" becomes "a stated scope".**
   - **Reason.** (T2) states no scope of its own, and the predecessor says "on a stated scope". The indefinite article lets ε be claimed on a region smaller than π's scope. The containment clause already covers a separate scope.
   - **Prompted by** Mimo's point 4(a), partly right.
3. **"let d be a metric on X_E" is added, and "an L-Lipschitz represented next-step map T" becomes "T L-Lipschitz for d".**
   - **Reason.** The erratum used a d that no line of file 11 defines, and "Lipschitz" presupposes a metric. The predecessor writes d_Z.
   - **Found in settling.** Neither reply nor any reading raised it. The change is of the same kind as the definition of \(e_n\): it restores a symbol the predecessor had.
4. **The optional unequal-start clause is dropped from the erratum.**
   - **Reason.** Under the erratum's definition, \(e_0=0\) for every system, so "with initial discrepancy \(e_0\)" says nothing. Plan 1.3.2 holds the addition back once a reading finds a flaw in it.
   - **Prompted by** Mimo's point 5.

#### What does not change

- **The containment clause, "whenever z, Sz, …, S^{n−1}z lie in that scope".** Mimo's point 4(b) bears only on the wording as sent.
- **The Lipschitz hypothesis, which stays global.** Mimo's "containment for L" fails against both wordings.
- **The definition of \(e_n\).**
- **The classification.**

---

## F3. Non-circular dependence

### Mimo's verdict

**"F3: PARTLY UPHELD".**

- **Γ.** Mimo holds that Γ's type is fixed, as components, and that its membership is not. The operative gap is whether an input-assigning component is a commitment or named background.
- **Readings.** Only two readings are live, not four, and "presupposes" is too strong.
- **The instances.**
  - Production is pressure, not contradiction.
  - O33 misfires as quoted.
  - O5 depends on how it is formalized.
- **Option B.** Mimo says option B repairs what it targets. It reports three breaks:
  - Derivation 6 unless the restriction operation is declared;
  - the dangling "that difference is lost";
  - a shift from sensitivity to edits to sensitivity to variation.
- **Its own wordings.** Mimo offers its own S3 and a sentence for line 246.
- **The composite edit.** S3 as written can be witnessed by an idle block through a composite edit.

### The ruling on Mimo's reply (`F3 reading.md`): UPHELD, of the finding as it stood after Atria's reading

- **"Untyped" stands.** Mimo's argument that Γ is typed as components fails. S3's witness is a pair (a,b), and the b in that pair moves boundary conditions. S3 also counts the block among "the other boundary conditions", and the (B) formula of Part VI (file 10 line 313) names a commitment block B, the letter of the boundary set.
- **Mimo's sharper point is right: membership is the operative gap.** It is added as a precision.
- **The production clause stands.** In exact model 1a, S3 as written has no witness. The clause holds on a production contract of interventions on H and θ only.
- **The O5 clause stands** with its condition (models 8a and 8b).
- **The O33 clause** ("does not flip") stands, and Mimo agrees with it.
- **Option B stays preferred.** The composite-edit instance (model 4) is a further reason: S3 as written and option A can be witnessed by an idle block, and option B cannot.
- **Parts of the brief's supporting text are corrected, since the current statement does not carry them:**
  - "four readings";
  - "presupposes", which becomes "suggests";
  - point 5 as a defect;
  - O33 as quoted.
- **Changes the reading makes to the repair:**
  - an explicit "lost" test, adopted below;
  - a wider typing sentence, adopted below in merged form;
  - the restriction operation named among the declared indices, with composition. This one is replaced below by the plan's deletion rider.

### Side by side with Atria's reading (R5): the labels differ, but the positions do not conflict

- **The Atria reading ruled NARROWED.** It started from the frozen position, and it withdrew the O33 flip.
- **The F3 reading ruled UPHELD.** It started from the position after that narrowing, and it upheld that narrowed position.
- **So the readings do not conflict.**
  - Measured against the finding as sent, both lead to one status, NARROWED.
  - Neither reading restores the O33 flip, and neither narrows further.
  - Both readings hold that "the other boundary conditions" does not fix Γ's type. The Atria reading shows that file 10 line 246 (file 11 line 233) alone introduces Γ. The F3 reading shows that the S3 witness pair moves boundary conditions.
- **O7.** The Atria reading also noted O7 as a supporting instance on R-τ-mech. Its fixed verdict, "Ines has a genuine explanation, a coarse one", claims an account whose contract only sets the salt port. O7 is recorded here as supporting the settled finding. It is not added to the finding's text, because neither outside reply examined it.

### The settled position: **NARROWED** (from the finding as sent)

The settled finding is the post-Atria statement with the F3 reading's precision:

> "Γ in non-circular dependence is untyped: no sentence says whether its members are components or boundary values, or whether a component that assigns an input is a commitment or named background, and the verdicts below turn on the second question. On the mechanism-only reading R-τ-mech, O5's fixed verdict flips on a narrowed contract with no edit that removes a mechanism commitment, and Part VII's forward organization fails S3 on its production contract of interventions on H and θ. O33's fixed verdict does not flip. Of the brief's two repairs, option B is preferred over option A."

**The plan's rule (1.3.4) chooses option B with the rider.**
- The rule reads: "F3 UPHELD: take B, with the rider unless X1 finds that the rider breaks a worked case".
- The branch that would take option A, "F3 NARROWED against B", does not apply. The narrowing (O33) is against the finding's instances, not against option B: B holds on O33, O5, O7, Part VII's production case and the skew-symmetric case (plan 1.3.4; the F3 reading's exact models for production, O33 and O5, and its determinant check for the skew-symmetric case).
- The rule has no branch for a narrowing that leaves option B intact. Its first branch is the one whose substance holds here, since option B is unbroken. So option B is taken, with the deletion rider.
- **The rider has not been put to an outside reader.** X1 must test it.
- **The F3 reading's exact models already test the rider's S3.** Their restriction keeps W and every component outside Γ, and deletes Γ∖W with the full relation (`f3_check.py`, function `restrict`). That is deletion under (O). The "proposed" column of the reading's table is the rider's test.

#### The final repair wording, exact text for revision 2

**1. S3 (option B with the deletion rider).** It replaces the third sentence of file 11 line 257, "There exists \((a,b)\in C\) that removes or replaces … in the claimed way.". S1 and S2 are unchanged, and W39.1's sentence after S2 is unchanged.

````text
There exist \((a,b)\in C\) and a nonempty block \(G\subseteq\Gamma\) such that the answer profile at \((a,b)\) differs from its value at \((1,b_0)\), or is not determined there in the claimed way, and this contrast is lost when the components of \(G\) are deleted from \(E\) (a deleted component imposes the full relation on its ports, Part II): evaluated at \((\tau(a),\sigma(b))\) and at \((1,\sigma(b_0))\), the answers of \(E\) with \(G\) deleted are determined and equal, or an answer that \(E\) determines at one of these points is not determined there once \(G\) is deleted.
````

**2. Typing Γ.** It is inserted in file 11 line 233 after sentence 1, which ends "… and an identified set \(\Gamma\) of active commitments in \(E\).".

````text
The commitments \(\Gamma\) are components of \(E\), those the candidate offers as doing the work; the boundary values of \(E\) and the components of \(E\) outside \(\Gamma\), including any that assigns an input, belong to the named background of Part VI.
````

**3. Part VI.** File 11 line 289, sentence 2, "For \(W\subseteq\Gamma\), let \(E|W\) retain the commitments in \(W\) with the named background fixed.", becomes:

````text
For \(W\subseteq\Gamma\), let \(E|W\) retain the commitments in \(W\) with the named background fixed; the commitments of \(E|W\) are \(W\).
````

**4. The dependence order (file 11 line 518) does not change.**
- Under the rider, (E) uses (O)'s deletion rule, the sentence after (O) at line 105.
- The order already has "(F1), (F2), (A) depend on (O), (Q), (K). (E) depends on those."
- The two sentences that B1 left free for W20 stay free.

**Option A stays the alternative**, unchanged, as in plan 1.3.4. It now has one more stated weakness. It keeps S3's edit-reach form, so an idle block can witness through a composite edit (model 4, on the reading of "the other boundary conditions" as the boundary set B).

**The fallback if X1 finds that the rider breaks a worked case.**

(a) S3 reads:

````text
There exist \((a,b)\in C\) and a nonempty block \(G\subseteq\Gamma\) such that the answer profile at \((a,b)\) differs from its value at \((1,b_0)\), or is not determined there in the claimed way, and this contrast is lost in \(E|(\Gamma\setminus G)\) with the named background fixed: evaluated at \((\tau(a),\sigma(b))\) and at \((1,\sigma(b_0))\), its two answers are determined and equal, or an answer that \(E\) determines at one of these points is not determined at that point.
````

(b) The typing sentence is the one given in item 2 above.

(c) Line 516's list of declared indices gains "the restriction operation of Part VI". Line 289, sentence 2, ends "; the commitments of \(E|W\) are \(W\), and \((E|W)|W'=E|W'\) for \(W'\subseteq W\)."

The plan's further fallback stays: if both options break something, only the τ, σ erratum is taken.

#### Changes from the post-Atria position, with reasons

Every change was made after the cross-examination. Option B stays preferred, and it stays a change of claim.

1. **S3 states when the contrast counts as lost.**
   - **The change.** It replaces "that difference is lost or the answer ceases to be determined" with an explicit test: the restricted answers are determined and equal, or an answer E determines becomes undetermined.
   - **Reason.** When the first conjunct holds because the answer is not determined, "that difference" has no antecedent. On the loose reading of "ceases to be determined", an idle Γ then passes: model 3, a contract with a law-deleting edit, gives a witness through the idle block. Under the explicit test it gives none.
   - **Mimo's own S3 wording is not adopted.** It leaks on the same model.
   - **Prompted by** Mimo's point 5(ii), second half.
2. **The restriction in S3 is deletion under (O)** ("when the components of \(G\) are deleted from \(E\)"), not \(E|(\Gamma\setminus G)\) with the named background fixed.
   - **Why the reader's change was not taken.** Mimo's point 5(i) is that option B makes Account depend on Part VI's restriction operation, which is not a declared index. The F3 reading answered by naming the operation among the declared indices, which puts a new declared input into the core definition. The plan's rider, fixed before any S88 reply was read, answers the same point without a new input: deletion is the restriction the text already has (line 105).
   - **The rider agrees with the typing sentence** (skeleton conflict 4). Deleting G from E leaves Γ∖G and everything the typing sentence puts in the named background. That is \(E|(\Gamma\setminus G)\) whenever Part VI's operation is deletion.
   - **The models support it.** They implement restriction as deletion, and they give the same witnesses as the reading's "proposed" column. Production holds on both identifications, as do O33 on R-τ-mech and O5 on both formalizations. Relabelings do not pass, and an idle block never witnesses. The reading's determinant check of the skew-symmetric case also reads the removal of skewness as deletion, since the matrix entries become unconstrained, and under that reading the case holds.
   - **Prompted by** Mimo's point 5(i), answered by plan 1.3.4's rider rather than by the reading's change 3.
3. **The typing sentence puts every component outside Γ into the named background, and says Γ is what the candidate offers as doing the work.**
   - **The change.** The post-Atria sentence ("the boundary values of E belong to the named background") put a component that lies outside Γ and is not a boundary value in no class: it was neither a commitment nor named background. Its fate under restriction was undefined.
   - **The words have two sources.** "including any that assigns an input" is Mimo's point 7. "those the candidate offers as doing the work" is the rider's sentence in plan 1.3.4.
   - **What it settles.** The sentence settles who decides membership: the candidate's identification decides. Option B makes the named verdicts insensitive to that choice, as models 1a and 1b show.
   - **Not adopted from Mimo's sentence:**
     - "active", which is undefined;
     - "every verdict is relative to it". Line 233 already makes Γ a coordinate of \(\mathcal E=(E,p,t,\Gamma)\).
4. **Part VI says the commitments of \(E|W\) are \(W\).**
   - **Reason.** (S) applies Account to \(E|W\). S3, under either option, quantifies over blocks of that candidate's Γ. Line 289's "retain the commitments in W" suggests that its commitments are W but does not state it.
   - **The gap predates option B.** The F3 reading notes this.
   - **Only part of the reading's change 3 is kept.** That change also named the restriction operation among the indices and made restriction compose. Under the rider, (E) no longer uses Part VI's operation, so neither is needed.
   - **Prompted by** Mimo's point 5(i), on composition, kept in narrowed form.

#### What does not change

- **S2** is unchanged, and W39.1's sentence after it is unchanged.
- **File 11 line 275's rule (W9)** is unchanged. It agrees with option B, under which an idle block cannot witness.
- **Option A** remains the alternative.
- **The classification** is unchanged: option B is a change of claim.
- **00:210's counterfactual-law sentence is still not restored** (plan conflict 14).

---

## Further counterexamples and further defects

### Offered by Mimo (R4)

- **F1:** none.
- **F2:** Mimo's containment instance is a counter-instance to the erratum as sent, not to the theory. The current wording already excludes it.
- **F3:** the composite edit. It holds only on one reading of "the other boundary conditions". It is a variant of F3, checked under F3, and it is not a new finding. It is recorded as a further weakness of option A.

**No new finding is added.**

### Found in settling

These are not new findings under R4, because no reply offered them. Three of them are defects in the repair wordings, fixed above:

1. **Derivation 10's replacement (F1).** "Exchanging the two persistence components' anchors gives a second faithful transport" is false read literally: λ alone exchanged fails (F1). This is fixed above (F1, change 4), and the appendix checks it.
2. **The (T2) erratum's d (F2).** The erratum's d was undefined. This is fixed above (F2, change 3).
3. **The Consequence's "faithful" (F1).** It named (F1) and (F2) only. The F1 reader noted this, and it is fixed above (F1, change 3).

Two points bear on the theory but are not findings:

4. **The declared inputs (file 11 line 514) do not list Part VI's declared restriction operation.**
   - (S) and (B) depend on it (line 289: "Fix \(\mathcal E\) and a declared restriction operation").
   - Derivation 6 (line 586) is not made false. It allows "declared indices and declared inputs", and Part VI declares the operation where it uses it.
   - The looseness predates every S88 repair. Under the rider, option B adds nothing to it.
   - It is carried forward for the change list, with the candidate clause "the restriction operation of Part VI (\(E|W\))" for line 514. It is not part of F3's repair.
5. **Functional transport uses \(S_a\), \(T_a\) and "generator" without introducing them** (the F2 reader's observation, file 10 line 366). Revision 2 already meets this with W24.1, which is applied. There is nothing further to do.

## What this means for the held entries

| held entry | settled status | plan rule applied | text to draft |
|---|---|---|---|
| W19 (L121, L552–558, L620; W10(b)) | F1 UPHELD | 1.3.3, "take (i)" | The three blocks under F1 above. Expected kind: CLAIM. |
| W31 (L361, after W24.1) | F2 NARROWED | 1.3.2, the erratum taken, the general bound waits | The erratum under F2 above. Expected kind: CLAIM, narrowed (plan 1.2). |
| W20 (L233, L257 S3, L289) | F3 NARROWED; option B not narrowed against | 1.3.4, "take B, with the rider unless X1 finds that the rider breaks a worked case" | The three blocks under F3 above. L518 is not changed. Expected kind: CLAIM. |

- **No final wording above has been put to an outside reader in its final form.**
- **The cross-examination of revision 2 (X1) must carry the three held entries.** The S90 brief carries only the first 48 changes, so it does not.
- **Within X1, the rider and the Derivation 10 sentence are the least tested.** The rider was never put to either reply, and the Derivation 10 sentence was rewritten in settling.

## What this file does not do

- It does not edit `authority/`, the change list, or any brief.
- It does not open any Mimo or Atria reply, reasoning or receipt.
- It does not open the S87 or S90 returns.
- It says nothing about F4, which was not put to Mimo.

---

## Appendix: the Derivation 10 exchange, checked exactly

This is a minimal model of Derivation 10's layers, restricted to positions, over the finite domain {0, 1, 2, 3}.

- **P** has continuity components c₁: x₁ = u₁ and c₂: x₂ = u₂, with the boundary u₁ = 0, u₂ = 3.
- **The admitted edits** are:
  - the identity;
  - "displace thing i to v", which replaces cᵢ by xᵢ = v;
  - "swap the two identities", which replaces c₁ and c₂ by x₁ = u₂ and x₂ = u₁.
- **S₁** is a copy of P with persistence components k₁ and k₂.
- **t₁** is the identity transport.

The script is `S88 Mimo reading parts/checks/d10_exchange.py`.

```python
from itertools import product
DOM = [0, 1, 2, 3]
B0 = {"u1": 0, "u2": 3}
EDITS = [("id",)] + [("disp", i, v) for i in (1, 2) for v in DOM] + [("swap",)]

def comps_P(e, b):
    c = {1: ("x1", b["u1"]), 2: ("x2", b["u2"])}
    if e[0] == "disp": c[e[1]] = (f"x{e[1]}", e[2])
    if e[0] == "swap": c = {1: ("x1", b["u2"]), 2: ("x2", b["u1"])}
    return c                                    # component i fixes port to value
def comps_S(e, b):                              # S1 is a copy of P with y-ports and w-boundaries
    c = {1: ("y1", b["w1"]), 2: ("y2", b["w2"])}
    if e[0] == "disp": c[e[1]] = (f"y{e[1]}", e[2])
    if e[0] == "swap": c = {1: ("y1", b["w2"]), 2: ("y2", b["w1"])}
    return c
def sol_one(comp): return {comp[1]}             # relation of one component on its single port
def sol_all(cs, ports):
    return {tuple(dict(c for c in cs.values())[p] for p in ports)}

def check(name, lam, tau, sig, pi):
    ok1 = ok2 = True
    for e in EDITS:
        b = B0
        cP, cS = comps_P(e, b), comps_S(tau(e), sig(b))
        for k in (1, 2):                        # (F1): anchor lam[k] of S1-component k, translated
            if sol_one(cP[lam[k]]) != sol_one(cS[k]): ok1 = False
        solD = sol_all(cP, ["x1", "x2"]); solE = sol_all(cS, ["y1", "y2"])
        if {pi(z) for z in solD} != solE: ok2 = False
    print(f"  {name}: (F1) {ok1}  (F2) {ok2}")

ident = lambda e: e
swap_e = lambda e: ("disp", 3 - e[1], e[2]) if e[0] == "disp" else e
sig_id = lambda b: {"w1": b["u1"], "w2": b["u2"]}
sig_sw = lambda b: {"w1": b["u2"], "w2": b["u1"]}
print("t1 (identity):"); check("t1", {1: 1, 2: 2}, ident, sig_id, lambda z: z)
print("anchors exchanged only (lambda swapped; pi, tau, sigma kept):")
check("t1 with lambda exchanged", {1: 2, 2: 1}, ident, sig_id, lambda z: z)
print("the two things exchanged throughout t1 (pi, tau, sigma and lambda):")
check("t1 composed with the exchange", {1: 2, 2: 1}, swap_e, sig_sw, lambda z: (z[1], z[0]))
```

Output:

```
t1 (identity):
  t1: (F1) True  (F2) True
anchors exchanged only (lambda swapped; pi, tau, sigma kept):
  t1 with lambda exchanged: (F1) False  (F2) True
the two things exchanged throughout t1 (pi, tau, sigma and lambda):
  t1 composed with the exchange: (F1) True  (F2) True
```
