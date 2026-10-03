# Defence of (T2) and Derivation 2 against checks W31 and W19

23 September 2026. Written by Claude (a subagent) for the revision-2 worklist, arguing the theory's side. This is a check, not a decision. The repository was only read (commit 2788a77); nothing in it was edited.

**The brief.** Two checks say Part XV's "mathematical error" clause is triggered:
- `W31 T2 bound.md`: a starting error \(e_0\) breaks (T2).
- `W19 W20 Mimo holes.md` §1: two faithful candidates whose components do not pair break Derivation 2.

The job here is to try, as hard as honesty allows, to show that each counterexample fails under the theory's own definitions, and to concede plainly where it does not.

**Read.**
- The two checks.
- File 10 and file 11 in full.
- File 00, lines 90–240, 515–590, 1196–1210 and 1380–1395.

**Not opened.**
- File 12.
- Any S81 1C/1K/2a/2b return, reasoning file, receipt, sample or table.
- The determination folder, the effort-controls folder, and the case book.

**Conventions.**
- "F10 L376" means file 10, line 376. "F11" is file 11. "00:572" is file 00, line 572.
- Every file 10 line cited has identical text in file 11, at the F11 line given where it matters (checked by diff).

**Rulings, as the brief defines them.**
- **SUCCEEDS:** the counterexample violates a stated assumption, quoted.
- **PARTLY:** the result is true on the natural reading, but the text does not state that reading. That calls for an erratum, not a defeat.
- **FAILS.**

---

## Verdicts

| item | counterexample | ruling | decisive lines |
|---|---|---|---|
| **(T2), starting error** | W31 §2: \(S=2z+0.1\), \(T=2y\), \(\pi=\mathrm{id}\), \(z_0=0\), \(y_0=-1\) | **PARTLY (strong).** No stated assumption is violated, so the defence does not fully succeed. But the counterexample needs a meaning of \(e_n\) that the files never give, and a starting state for the explanation's run that the files never introduce. On the only reading the files' own objects support, \(e_0=0\) by definition and (T2) is true. | (T2) F10 L376 = F11 L361. Functional transport F10 L366 = F11 L351. π at F10 L204 = F11 L191. Expectation, (F2) and (A) at F10 L234, L257, L265. 00:564–585 |
| (T2), side gap: ε bounded only at the start (W31 §3.1) | \(S=2z+0.1+z^2\), \(T=2y\) | **SUCCEEDS**, on the natural reading of "one-step discrepancy ε" | F10 L376 |
| (T2), side gap: which map must be Lipschitz (W31 §3.2) | W31 part F; a sharper example in §A.6 | **PARTLY (weak).** Files 10 and 11 do not say which map. On the target-map reading, (T2) is false even from matching starts. FW5 says "represented" (00:572), and the proof needs it. | F10 L376; 00:572 |
| **Derivation 2, instance 1** | D: \(x=u,\ y=2x,\ z=y+1\); \(E_1=D\); \(E_2=\{x=u,\ z=2x+1\}\) | **FAILS** on every defence line, (i) to (iv) | Claim F10 L561 = F11 L554. Proof L563 = L556. λ at L204. (F1) at L248. Gloss at L260. (K) at L130–136. Derivation 1 at L553–555. Derivation 8 at L609 |
| **Derivation 2, instance 2** (equal component counts) | the chain \(x\to y\to z\to w\), cut at \(y\) in one candidate and at \(z\) in the other | **FAILS**, more cleanly than instance 1: the subnetwork line (iii) fails in both directions | same |

**Bottom line.**
- **Part XV's defeat clause is genuinely triggered, and the trigger is Derivation 2, not (T2).**
- **(T2) triggers it only through a drafting omission.** On the reading the text's own objects fix, (T2) is true. The text never writes that reading down. Restoring what FW5 stated is an erratum.
- **Derivation 2's component conjunct is false on the natural reading of its words.**
  - Both counter-instances meet every stated assumption.
  - The best defence reads the claim as pairing components only through shared anchors. That is the reading the proof proves, but the words do not say it and no line states it.
  - Adopting that reading is a claim change of the kind file 11 recorded for Derivation 3, not an erratum.
  - The damage is contained: the only use of Derivation 2 (Derivation 10) lies inside the part that is true.

---

## A. (T2) and the starting error

### A.1 The text

- **(T2)**, F10 L376 = F11 L361: "**Approximate transport.** With one-step discrepancy \(\varepsilon\) and an \(L\)-Lipschitz next-step map, \(e_n\le\varepsilon\sum_{k<n}L^k\). (T2) Without a modulus, no accumulated bound follows. An exact question is not silently replaced by an approximate one."
- **Directly above it**, F10 L366 = F11 L351: "**Functional transport.** If \(\pi\circ S_a=T_a\circ\pi\) for every generator \(a\), the same holds for every admitted finite composition with matching scopes. *Proof.* \(\pi S_bS_a=T_b\pi S_a=T_bT_a\pi\); induct. ∎"
- **Part XV**, F10 L543 = F11 L538: "**A mathematical error.** A counterexample to the finite monotone theorem, (I2), (O1), (T2), (CT2), or Derivations 1–3 under their stated assumptions."

(T2) states two assumptions: a one-step discrepancy ε, and an L-Lipschitz next-step map. The symbol \(e_n\) is used and never defined. The word "discrepancy" occurs nowhere else in either file (checked with grep).

### A.2 Defence line 1: where (T2) sits fixes \(e_n\) as the n-step failure of the square

**The reading.**
- (T2) sits in Part VIII, straight after "Functional transport", under the heading "Approximate transport".
- Exact transport is the commuting square \(\pi\circ S=T\circ\pi\). It compares the images of one state \(z\): \(\pi(Sz)\) against \(T(\pi z)\).
- The approximate version relaxes that equality to a distance. So the one-step discrepancy is \(d(\pi Sz,T\pi z)\).
- W31 checks its own example in exactly this sense: "|S(w) − T(w)| = ε at every w" (W31 L81), a comparison at one state \(w\).
- The n-step square is \(\pi S^n=T^n\pi\). Its failure is \(e_n=d(\pi S^nz,\,T^n\pi z)\), so \(e_0=d(\pi z,\pi z)=0\) by definition.
- W31 §2 proves that (T2) is true on this reading, its "reading M".

**Three instances of (T2) itself fix the reading.** W31's two-run reading R lets the explanation's run start from its own \(y_0\), with \(e_n=d(\pi z_n,y_n)\).

- **ε = 0.** (T2) then says \(e_n=0\) for all n.
  - On reading M, that is the functional-transport result directly above it.
  - On reading R, it says two runs from different starts coincide forever. That is false even when both maps are the identity (script, §E).
  - A result headed "approximate transport" whose exact case is not the exact-transport result just above it is not being read as written.
- **n = 1.** (T2) reads \(e_1\le\varepsilon\), which is the hypothesis restated.
  - On M, \(e_1=d(\pi Sz,T\pi z)\) is the one-step discrepancy, so it is.
  - On R, W31's own example gives \(e_1=|0.1-(-2)|=2.1\), not the one-step discrepancy 0.1.
  - So R takes "one-step discrepancy" in the same-state sense and \(e_n\) in the two-run sense, and (T2)'s n = 1 case stops restating its hypothesis.
- **n = 0.** (T2) reads \(e_0\le0\).
  - On M, this is an identity.
  - On R, it is false for every system with unequal starts, whatever the dynamics.
  - W31 treats this as a hidden assumption. The defence treats it as the statement telling the reader which \(e_n\) is meant.

### A.3 Defence line 2: is "discrepancy" defined anywhere as a comparison of images of one state?

- **Files 10 and 11: no.** The word occurs only on the (T2) line. There \(e_n\) is not even called a discrepancy.
- **File 00: implicitly, yes.**
  - Before 00 first uses the word, its approximate-transport section introduces exactly one quantity, at 00:564–570: "Suppose three representations have maps \(f:X\to Y\), \(g:Y\to Z\), and an actual map \(h:X\to Z\). If \(d_Z(h(x),g(f(x)))\le\varepsilon\) on a stated scope, then that bound is the claim." That compares two maps applied to one \(x\).
  - 00:572 then speaks of "the discrepancy after one mapped step" and writes \(e_n\) "for the discrepancy after \(n\) steps".
  - 00:534 says of exact transport: "The proof is about a fixed map and compatible scopes."
- **00:578 ("With \(e_0=0\),") cuts both ways.**
  - Read as a hypothesis, as W31 reads it, it suggests the FW5 author thought the start needed fixing.
  - Read as the base case that 00:585's "induct" needs, it holds automatically on the same-state reading.
  - Either way, FW5 wrote it and files 10 and 11 dropped it.
- **So W31's statement that FW5 "defines e_n generally" (W31 §1) is one reading, not an established one.** The only quantity FW5 introduces before it uses the word "discrepancy" is a same-state one.

### A.4 Defence line 3: the files have no starting state for the explanation's run

Everywhere files 10 and 11 compare D with E, E is evaluated at the translated point:
- the transport's state map, F10 L204: "\(\pi:X_D\to X_E\) on the stated scope";
- the expectation, F10 L234: "\(\operatorname{Ans}_S(\tau(a),\sigma(b))\)";
- (F2), F10 L257: \(\pi[\operatorname{Sol}_D(a,b)]=\operatorname{Sol}_E(\tau(a),\sigma(b))\);
- (A), F10 L265;
- functional transport, L366;
- relational transport, L368–374. There the explanation's state is any \(y\) with \(zRy\), which still ties it to \(z\).

No line introduces a run of E from a state that is neither \(\pi(z_0)\) nor R-related to \(z_0\). W31's \(y_0=-1\), set against \(\pi(z_0)=0\), is such a run, and it has to be brought in from outside the text.

**Consistency with the W19/W20 check.** That check applied this standard to the \(\tau\) missing from the third sentence of non-circular dependence: "Every other conjunct of Part V reads a pair from \(C\) on \(E\) as \((\tau(a),\sigma(b))\) … So the missing \(\tau\), taken alone, is a drafting fault. **As a misfire, REFUTED**" (W19/W20 §2.3). Applied here, the same standard makes the starting-error objection a drafting fault.

### A.5 Is a reader bound to reading M "under their stated assumptions"?

**Not by any sentence of the text.** Neither stated assumption of (T2) mentions the start, π or \(e_n\). So the counterexample violates no assumption that can be quoted, and the defence cannot fully succeed.

**By everything else, yes.** A reader who adopts R has to:
- give \(e_n\) a meaning the files never give;
- introduce an object, a free starting state for E's run, that the files never introduce;
- take "discrepancy" in two senses within one sentence;
- accept that (T2)'s own exact case is false.

**The concession.** None of this is written down, so the literal defeat clause can be aimed at the text. That is what "triggered only by a drafting omission" means here.

**Ruling A (starting error): PARTLY (strong).**
- (T2) is true on the natural reading, the one the text's own objects support.
- The text does not state that reading.
- An erratum is needed, not a defeat.

### A.6 The side gaps W31 lists in §3

The brief did not ask about these, but they bear on the bottom line.

**ε bounded only at the start (W31 part E): SUCCEEDS.**
- In a result about n steps, "With one-step discrepancy ε" bounds one-step discrepancies. The natural reading is that it bounds each of them.
- In W31's example the second step's discrepancy is 0.11 > ε. The stated assumption is violated.

**Which next-step map is L-Lipschitz (W31 part F): PARTLY (weak). This is the point on which (T2) is least defensible.**
- W31's own example leans on a metric on \(X_D\) that the files never supply.
  - Measure in the only metric (T2) uses, the one on \(X_E\) where the discrepancies are taken.
  - In that metric its target map is 8-Lipschitz, and the bound holds.
- That rescue does not generalise. Take:
  - \(S=\mathrm{id}\) on ℝ, which is 1-Lipschitz in *every* metric;
  - \(\pi(z)=(z,0)\) into ℝ²;
  - \(T(a,b)=(a+100b,\ b+0.1)\).
- Then:
  - the one-step discrepancy is exactly 0.1 at every state;
  - the start matches (reading M);
  - yet \(e_2=10.002\), above the bound 0.2 with L = 1;
  - with \(L=\operatorname{Lip}(T)\approx100.01\) the bound is 10.101, and it holds (script, §E).
- So if "an L-Lipschitz next-step map" means the target's map, (T2) is false even from matching starts.
- Nothing in files 10 or 11 picks out the represented map \(T\). FW5 does, at 00:572: "the represented next-step map is \(L\)-Lipschitz". The proof needs it: \(e_{n+1}\le d(\pi Sz_n,T\pi z_n)+d(T\pi z_n,Ty_n)\).
- This is still a drafting omission, since the predecessor states the right hypothesis. But a reader of files 10 and 11 alone gets nothing like the steer toward \(T\) that §A.2–A.4 give toward \(e_0=0\).

---

## B. Derivation 2

### B.1 The text

**Claim**, F10 L561 = F11 L554: "Two candidates \(\mathcal E,\mathcal E'\) for the same \(p\) that both satisfy (F1), (F2), and (A) on \(C\) are one account at grain \(C\): their components are pairwise of one kind on \(C\) and their answer profiles coincide."

**Proof**, F10 L563 = F11 L556: "Immediate from Derivation 1 and (A). ∎"

**Stated assumptions:** the same \(p\), and (F1), (F2) and (A) on \(C\). Non-circular dependence, non-vacuity and \(\Gamma\) are not among them.

### B.2 Both counter-instances meet the stated assumptions

The script (§E) checks both instances exactly, in rational arithmetic, at the baseline and at \(\mathrm{do}(x{=}c)\) for six values of \(c\).
- **Instance 1:** \(E_1=D\); \(E_2=\{x=u,\ z=2x+1\}\), with \(m_z\) anchored to \(\{j_y,j_z\}\). (F1), (F2) and (A) hold for both.
- **Instance 2:** \(E_a=\{x=u,\ z=x+2,\ w=z\}\) and \(E_b=\{x=u,\ y=x+1,\ w=y+1\}\). (F1), (F2) and (A) hold for both.

The hand proofs are in W19 §1.4.

### B.3 Defence (i): is \(E_2\) inadmissible? Does (F1) forbid a merged anchor?

**FAILS.** The text admits merged anchors in so many words.
- F10 L204: "\(\lambda\) assigns each component of \(E\) a *subnetwork* of \(D\) with a port translation".
- (F1), F10 L248: "every active component \(k\) of \(E\) with anchor subnetwork \(\lambda(k)\subseteq D\) … the relation obtained by imposing the constraints of \(\lambda(k)\) and projecting away its hidden ports". An anchor that is a single component has no hidden ports to project away; hidden ports exist only because anchors may be merged.
- **The "wrong decomposition" gloss**, F10 L260: "(F1) prevents an assembled match from hiding a wrong decomposition."
  - This makes (F1) the test for a wrong decomposition. \(E_2\) passes (F1), so by the theory's own test its decomposition is not wrong.
  - Nothing in the gloss says only one decomposition can be right.
- F10 L296–298 abolished FW5's separate Anchoring condition. Even that condition allowed merged anchors:
  - 00:170: "The map \(\lambda\) anchors explanatory components to target components or specified subnetworks."
  - 00:174 allows "a derived causal suborganization".
- The theory's own worked Account uses merged anchors. F10 L356: "every intermediate product is a determinant suborganization whose hidden ports project away".
- F11 L279: (E) "does not reject a coarse dependence for omitting finer workings".

### B.4 Defence (ii): does "pairwise of one kind" mean something weaker than a bijection?

**(ii-a) Any correspondence of components.** Each component of either candidate would be of one kind with *some* component of the other, with no bijection required. **FAILS.**
- The exhaustive search (§E) finds no partner component in the other candidate for:
  - \(k_y\), \(k_z\) and \(m_z\) in instance 1;
  - \(a_z\), \(a_w\), \(b_y\) and \(b_w\) in instance 2.
- Only the input components \(x=u\) pair.

**(ii-b) Pairing through shared anchors.** Only a component of \(E\) and a component of \(E'\) anchored to the same subnetwork of \(D\) are paired, and they are of one kind. Components with different anchors are not paired at all.

- **On this reading the claim is true in both instances.** The only co-anchored pairs are \((k_x,m_x)\) and \((a_x,b_x)\), and both are of one kind.
- **For it:** it is exactly what the proof proves. "Immediate from Derivation 1" can work only through anchors, because Derivation 1 (F10 L553) relates each component to its own anchor and to nothing else.
- **Against it:**
  - **The words.** "*their* components are pairwise of one kind" names all their components. "Pairwise" between two collections, as in "the angles of the two triangles are pairwise equal", pairs every member.
  - **The conclusion.** "one account at grain \(C\)" and the title "Indistinguishable is identical" assert identity. Under (ii-b), \(E_1\) and \(E_2\) would be "one account" although they are different organizations, against F10 L23 = F11 L25: "Two systems with identical outputs and different internal routes are different organizations here".
  - **No line states the anchor restriction.**
  - **Derivation 10 gives no independent support.** Its swap case (F10 L627) is a case of shared, exchanged anchors. There the bijection reading and (ii-b) give the same answer, since the swap is the pairing that works once signatures are read through \(\tau\) and \(\tau'\). So it cannot decide between the readings. It shows only that the one use of Derivation 2 lies inside the part that is true, which W19 §1.5 also says.

**So (ii-b) is the repair, not the reading.** As a defence of the claim as written, it **FAILS**.

### B.5 Defence (iii): does (K) apply to subnetworks as well as components?

**Yes, and the text itself does this once.** Derivation 1's proof (F10 L555) writes \(\operatorname{sig}_C(\lambda(k))=\{(a,b,\operatorname{proj}_{V_k}\operatorname{Sol}_{\lambda(k)}(a,b))\}\): the signature of a subnetwork, projected onto a port set. So \(E_1\)'s \(\{k_y,k_z\}\), projected onto \(\{x,z\}\), **is** of one kind with \(E_2\)'s \(m_z\). The script confirms it.

**It still does not rescue the claim.**
- **Instance 1: the match runs one way only.**
  - \(k_y\) and \(k_z\), each taken alone, are of one kind with no component *and* no subnetwork of \(E_2\).
  - The claim is symmetric ("their components are pairwise"). Nothing in it says which candidate is the finer one.
- **Instance 2: the match fails in both directions.**
  - \(a_w\) has no partner subnetwork in \(E_b\).
  - \(b_y\) and \(b_w\) have none in \(E_a\).
  - Neither candidate is a coarsening of the other.
- **(iii′) The block reading.** Partition each candidate into blocks and pair the blocks as projected subnetworks.
  - This does rescue both instances: \(\{a_z,a_w\}\leftrightarrow\{b_y,b_w\}\) on \(\{x,w\}\) holds (script, last part).
  - But that is a notion of *common coarsening*, which the text never defines.
  - The text's own lines resist it:
    - F10 L609 = F11 L602, Derivation 8: "The result does not apply to coarsenings".
    - 00:154: "Coarsening is not automatically an isomorphism".
    - 00:1206: "a coarsening that identifies a relevant distinction".

**FAILS.**

### B.6 Defence (iv): does \(C\)'s grain exclude \(y\), making \(y\)'s component inactive and uncounted?

**FAILS.**
- **Grain and contract are separate declared indices.** F10 L523 = F11 L516: "Grain \(\ell\), boundary \(\beta\), continuity \(\Omega\), and the contract \(C\) are declared indices". "Grain \(C\)" occurs only in Derivation 2's conclusion. No line says a grain or a contract removes ports or merges components.
- **(K) does not merge these components.** (K) is the text's only notion of kinds indexed to \(C\), and it is defined component by component (F10 L130–136).
  - On \(C\) it gives \(k_y\) the constant relation \(\{(s,2s)\}\), \(k_z\) the relation \(\{(s,s+1)\}\), and \(m_z\) the relation \(\{(s,2s+1)\}\). These are three different kinds on \(C\).
  - Nothing merges components just because no edit in \(C\) reaches them separately.
  - The Part 0 phrase "components that no change at that level separates … are one kind at that level" (F10 L35) is not met. These components are separated by their relations at every pair in \(C\), including the baseline.
- **"Active" does not help.**
  - \(\Gamma\) is "identified" by the candidate (F10 L246), and the claim ranges over all candidates. The counter-instance may identify every component as active.
  - On any objective test, \(k_y\) matters. Deleting it imposes the full relation on \((x,y)\) (F10 L120), which leaves \(z\) undetermined, so (A) fails.
  - In any case the claim says "their components", not "their active components".

### B.7 Defence (v): the equal-count variant

The tests come out the same as for instance 1, and more decisively.
- **(i)** fails. Both candidates use merged anchors in the way the text permits.
- **(ii-a)** fails. Bijections exist, since each candidate has three components, but none makes every pair of one kind; only \((a_x,b_x)\) pairs.
- **(ii-b)** makes the claim true, with one co-anchored pair, but it is not the claim.
- **(iii)** fails in both directions, so "one is a refinement of the other" is not available either.
- **(iv)** fails. Every component lies on the dependence from \(x\) to \(w\).

### B.8 Rulings

| defence line | instance 1 | instance 2 |
|---|---|---|
| (i) \(E_2\) inadmissible; anchoring; "wrong decomposition" | FAILS | FAILS |
| (ii-a) any correspondence of components | FAILS | FAILS |
| (ii-b) pairing only through shared anchors | the claim becomes true, but this is not what the words say: FAILS as a defence | same |
| (iii) (K) applied to subnetworks | FAILS (the match runs one way only) | FAILS (no match in either direction) |
| (iii′) common coarsening | rescues, but the notion is undefined and runs against L609 and 00:154: FAILS | same |
| (iv) grain or activity drops \(y\) | FAILS | FAILS |
| **overall** | **FAILS** | **FAILS** |

**A precedent the defence would want, and cannot use.** File 11 handled Derivation 3 in the same way.
- Its header, F11 L5, says: "One claim changes: Derivation 3, whose unqualified form gave the wrong verdict … and whose proof already assumed the qualification."
- F11 L534 then calls the qualification "the theorem's own qualification, not a refutation", but only *after* the claim had been changed.

By the project's own practice, a claim broader than its proof is corrected by a recorded claim change, not by rereading it.

---

## C. What the theory would need to say

### C.1 (T2): an erratum suffices

**Minimal wording**, at F10 L376 = F11 L361:

> **Approximate transport.** With one-step discrepancy \(d(\pi Sz,T\pi z)\le\varepsilon\) at every state \(z\) of the stated scope and an \(L\)-Lipschitz represented next-step map \(T\), the discrepancy after \(n\) steps from one state, \(e_n=d(\pi S^nz,T^n\pi z)\) (so \(e_0=0\)), satisfies \(e_n\le\varepsilon\sum_{k<n}L^k\). (T2) Without a modulus, no accumulated bound follows. An exact question is not silently replaced by an approximate one.

- **"from one state (so \(e_0=0\))"** is already implied: by where (T2) sits, by the files' uniform convention, and by (T2)'s own ε = 0, n = 0 and n = 1 instances (§A.2–A.4). It is an erratum, and it is W31's Option A.
- **"represented"** restores 00:572, and **"at every state of the stated scope"** restores 00:570. Both are errata by descent from FW5.
  - "Represented" does choose between two readings that files 10 and 11 alone leave open (§A.6), so a stricter referee could call it a narrowing.
  - It withdraws nothing FW5 claimed.
- **W31's Option B**, the general bound \(L^ne_0+\varepsilon\sum_{k<n}L^k\), is a *new* claim (a generalisation). It is welcome but not needed.
- **File 11's header** ("Nothing else changes in what is claimed") needs one erratum line for (T2).

### C.2 Derivation 2: a revision is needed

**Minimal wording**, replacing the claim at F10 L561 = F11 L554:

> **Claim.** Two candidates \(\mathcal E,\mathcal E'\) for the same \(p\) that both satisfy (F1), (F2) and (A) on \(C\) have one answer profile on \(C\); and a component of \(E\) and a component of \(E'\) anchored to one subnetwork of \(D\), up to port translation, are of one kind on \(C\), their signatures read through \(\tau\) and \(\tau'\).
>
> *Proof.* Answers: (A) for each candidate. Components: Derivation 1 for each, and kind on \(C\) is an equivalence (K). ∎ Candidates that anchor different subnetworks are not thereby one account: a coarsening is not a recoding (Derivation 8).

**The typing phrase is an erratum.** "Their signatures read through \(\tau\) and \(\tau'\)" adds nothing new: Derivation 1 already reads signatures "on \(\tau[C]\) … up to the port translation" (F10 L553).

**The narrowing is not already implied as the claim.**
- It is exactly what the proof proves, so it is not a *new* claim.
- But it withdraws what the words assert, namely that the components of any two faithful candidates pair.
- It also changes the title ("Indistinguishable is identical") and the reach of the Consequence (F10 L565).
- So it is a claim change, to be recorded as file 11 recorded Derivation 3.

**No wording can keep the original conclusion for arbitrary faithful pairs.** Both counter-instances meet every hypothesis. The only alternative is a new identity, "common coarsening", which would be a new claim and would conflict with F10 L609 and 00:154/1206.

**Edits that follow from the change:**
- the title;
- the Consequence, narrowed to candidates that differ only in which component carries which anchor;
- Derivation 10's sentence, restated as the claim about two transports (as W19 §1.7 proposes). It then falls inside the narrowed claim.

W19 §1.7's repair is compatible with this. It requires a full bijection that preserves anchors before it concludes "one account"; the wording above is the smaller change.

---

## D. Bottom line

### (T2): triggered only by a drafting omission

- **The \(e_0\) counterexample.**
  - Its arithmetic is sound.
  - It is aimed at a reading, a free starting state for E's run, that the text never introduces.
  - It makes the text's own exact case false.
- **On the reading the files support, (T2) is true** (W31 §2's own proof).
- **The defence concedes two things:**
  - the literal text never defines \(e_n\);
  - from files 10 and 11 alone, the "which map is Lipschitz" gap is only weakly defended.
- **Both are repaired by restoring what FW5 stated.** That is an erratum, not a defeat.
- **W31's verdict, "CONFIRMED BUT HARMLESS", stands in substance.** One sentence needs changing. W31's "As written, (T2) is false under the assumptions those files state" should become "as written, (T2) is indeterminate. It is true on the files' own reading and false only on a reading brought in from outside."

### Derivation 2: genuinely triggered

- Both counter-instances meet every stated assumption.
- The component conjunct is false on the natural reading of its words, and "Immediate" hides a step that fails.
- No defence line, (i) to (iv), survives the text.
- The one reading on which the claim is true, pairing through shared anchors, is the one the proof uses. The words do not carry it, and no line states it.
- The repair is a recorded claim change.
- The damage is contained. The true part is the only part the theory uses (Derivation 10).
- W19's verdict, "CONFIRMED", stands.

### Part XV overall

Genuinely triggered, once, by Derivation 2.

---

## E. Script (run with `python3 -`, not saved elsewhere) and its output

The script checks the two Derivation 2 counter-instances exactly, in rational arithmetic. It tests the pairing readings (ii-a), (ii-b), (iii) and (iii′), and the (T2) readings M and R. It also runs the side-gap example of §A.6.

- The equalities are checked at six values of \(c\). The hand proofs for all \(c\) are in W19 §1.4.
- Each "no partner" result needs only one failing edit.
- The 4-link chain's \(E_a,E_b\) print under their own names.

```python
from fractions import Fraction as F
from itertools import combinations, permutations

# ---------- exact affine linear algebra ----------
def rref(rows, ncols):
    rows = [r[:] for r in rows]; piv = []; r = 0
    for c in range(ncols):
        p = next((i for i in range(r, len(rows)) if rows[i][c] != 0), None)
        if p is None: continue
        rows[r], rows[p] = rows[p], rows[r]
        pv = rows[r][c]; rows[r] = [v / pv for v in rows[r]]
        for i in range(len(rows)):
            if i != r and rows[i][c] != 0:
                f = rows[i][c]; rows[i] = [a - f * b for a, b in zip(rows[i], rows[r])]
        piv.append(c); r += 1
        if r == len(rows): break
    return rows[:r], piv

def rank(vecs):
    if not vecs: return 0
    return len(rref([list(v) for v in vecs], len(vecs[0]))[1])

def solve(eqs, ports):
    """eqs: list of (dict port->coef, const). Returns affine set (point, directions) in ports order, or None if empty."""
    n = len(ports); idx = {p: i for i, p in enumerate(ports)}
    rows = []
    for coefs, const in eqs:
        row = [F(0)] * (n + 1)
        for p, c in coefs.items(): row[idx[p]] += F(c)
        row[n] = F(const); rows.append(row)
    if not rows:
        return ([F(0)] * n, [[F(int(i == j)) for j in range(n)] for i in range(n)])
    R, piv = rref(rows, n + 1)
    if n in piv: return None
    free = [c for c in range(n) if c not in piv]
    pt = [F(0)] * n
    for row, c in zip(R, piv): pt[c] = row[n]
    dirs = []
    for f in free:
        d = [F(0)] * n; d[f] = F(1)
        for row, c in zip(R, piv): d[c] = -row[f]
        dirs.append(d)
    return (pt, dirs)

def project(aff, ports, onto):
    if aff is None: return None
    ix = [ports.index(q) for q in onto]
    pt, dirs = aff
    return ([pt[i] for i in ix], [[d[i] for i in ix] for d in dirs])

def same(a, b):
    if a is None or b is None: return a is None and b is None
    (p, V), (q, W) = a, b
    rv, rw = rank(V) if V else 0, rank(W) if W else 0
    if rv != rw or rank(V + W if (V or W) else [[0]*len(p)]) != rv and (V or W): return False
    diff = [x - y for x, y in zip(q, p)]
    if all(x == 0 for x in diff): return True
    return (rank(V + [diff]) if V else 1) == rv

# ---------- organizations ----------
# component: (footprint tuple, function(edit) -> list of equations or None for 'full relation')
EDITS = ['id'] + [('do_x', c) for c in (-2, -1, 0, 1, 3, 7)]
def xcomp(e):   # x = u with u = 0 at b0; do(x=c) replaces it by x = c
    return [({'x': 1}, 0)] if e == 'id' else [({'x': 1}, e[1])]
def lin(out, inp, a, b):  # out = a*inp + b, untouched by do(x=c)
    return lambda e: [({out: 1, inp: -a}, b)]

def sol(org, names, e):
    ports = sorted({p for n in names for p in org[n][0]})
    eqs = [q for n in names for q in org[n][1](e)]
    return ports, solve(eqs, ports)

def rel(org, name, e, onto=None):
    fp = org[name][0]
    ports, s = sol(org, [name], e)
    return project(s, ports, onto or list(fp))

def sig_equal_component(o1, k1, o2, k2):
    fp1, fp2 = org_fp(o1, k1), org_fp(o2, k2)
    if len(fp1) != len(fp2): return False
    for perm in permutations(fp2):
        if all(same(rel(o1, k1, e, list(fp1)), rel(o2, k2, e, list(perm))) for e in EDITS): return True
    return False
def org_fp(o, k): return o[k][0]

def subnetwork_partner(o1, k1, o2):
    """components-to-subnetwork test (iii): some subnetwork W of o2 and an injective port map
    from k1's footprint into W's ports with proj Sol_W = L_k1 at every edit."""
    fp1 = org_fp(o1, k1); hits = []
    names = list(o2)
    for r in range(1, len(names) + 1):
        for W in combinations(names, r):
            ports = sorted({p for n in W for p in o2[n][0]})
            for tgt in permutations(ports, len(fp1)):
                ok = True
                for e in EDITS:
                    ps, s = sol(o2, list(W), e)
                    if not same(rel(o1, k1, e, list(fp1)), project(s, ps, list(tgt))): ok = False; break
                if ok: hits.append((W, tgt))
    return hits

def check_pair(title, D, E1, lam1, E2, lam2, query, n1="E1", n2="E2"):
    print(f"\n=== {title}")
    for Ename, E, lam in ((n1, E1, lam1), (n2, E2, lam2)):
        f1 = all(same(project(sol(D, lam[k], e)[1], sol(D, lam[k], e)[0], list(E[k][0])), rel(E, k, e)) for k in E for e in EDITS)
        Dports = sorted({p for n in D for p in D[n][0]}); Eports = sorted({p for n in E for p in E[n][0]})
        f2 = all(same(project(sol(D, list(D), e)[1], Dports, Eports), sol(E, list(E), e)[1]) for e in EDITS)
        A = all(same(project(sol(D, list(D), e)[1], Dports, [query]), project(sol(E, list(E), e)[1], Eports, [query])) for e in EDITS)
        print(f"  {Ename}: (F1) {f1}  (F2) {f2}  (A) {A}")
    print("  component-to-component 'one kind' (K, with footprint bijection):")
    for k1 in E1:
        partners = [k2 for k2 in E2 if sig_equal_component(E1, k1, E2, k2)]
        print(f"    {n1}.{k1:3s} ~ {partners}")
    for k2 in E2:
        partners = [k1 for k1 in E1 if sig_equal_component(E2, k2, E1, k1)]
        print(f"    {n2}.{k2:3s} ~ {partners}")
    print("  component-to-subnetwork (defence line iii):")
    for k1 in E1:
        h = subnetwork_partner(E1, k1, E2); print(f"    {n1}.{k1:3s} -> subnetworks of {n2}: {[(list(W), t) for W, t in h] or 'none'}")
    for k2 in E2:
        h = subnetwork_partner(E2, k2, E1); print(f"    {n2}.{k2:3s} -> subnetworks of {n1}: {[(list(W), t) for W, t in h] or 'none'}")
    shared = [(k1, k2) for k1 in E1 for k2 in E2 if set(lam1[k1]) == set(lam2[k2])]
    print(f"  anchor-sharing pairs (defence line ii-b): {shared}; of one kind: {[sig_equal_component(E1,a,E2,b) for a,b in shared]}")

# three-link chain: D = {x=u, y=2x, z=y+1}; E1 = D; E2 = {x=u, z=2x+1}
D3 = {'jx': (('x',), xcomp), 'jy': (('x', 'y'), lin('y', 'x', 2, 0)), 'jz': (('y', 'z'), lin('z', 'y', 1, 1))}
E1 = {'kx': (('x',), xcomp), 'ky': (('x', 'y'), lin('y', 'x', 2, 0)), 'kz': (('y', 'z'), lin('z', 'y', 1, 1))}
E2 = {'mx': (('x',), xcomp), 'mz': (('x', 'z'), lin('z', 'x', 2, 1))}
check_pair("Counter-instance 1: x=u, y=2x, z=y+1; E1 = D, E2 = {x=u, z=2x+1}", D3,
           E1, {'kx': ['jx'], 'ky': ['jy'], 'kz': ['jz']}, E2, {'mx': ['jx'], 'mz': ['jy', 'jz']}, 'z')

# equal-count variant: D = {x=u, y=x+1, z=y+1, w=z}; Ea = {x=u, z=x+2, w=z}; Eb = {x=u, y=x+1, w=y+1}
D4 = {'jx': (('x',), xcomp), 'jy': (('x', 'y'), lin('y', 'x', 1, 1)), 'jz': (('y', 'z'), lin('z', 'y', 1, 1)), 'jw': (('z', 'w'), lin('w', 'z', 1, 0))}
Ea = {'ax': (('x',), xcomp), 'az': (('x', 'z'), lin('z', 'x', 1, 2)), 'aw': (('z', 'w'), lin('w', 'z', 1, 0))}
Eb = {'bx': (('x',), xcomp), 'by': (('x', 'y'), lin('y', 'x', 1, 1)), 'bw': (('y', 'w'), lin('w', 'y', 1, 1))}
check_pair("Counter-instance 2 (equal counts): x=u, y=x+1, z=y+1, w=z; Ea cuts at y, Eb cuts at z", D4,
           Ea, {'ax': ['jx'], 'az': ['jy', 'jz'], 'aw': ['jw']}, Eb, {'bx': ['jx'], 'by': ['jy'], 'bw': ['jz', 'jw']}, 'w', 'Ea', 'Eb')

# ---------- (T2) ----------
import math
print("\n=== (T2) readings on W31's example: S(z)=2z+0.1, T(y)=2y, pi=id, eps=0.1, L=2")
S = lambda z: 2*z + 0.1; T = lambda y: 2*y
bound = lambda n, eps=0.1, L=2: eps*sum(L**k for k in range(n))
z = 0.0
for n in range(5):
    zn, yM, yR = z, z, -1.0
    for _ in range(n): zn, yM, yR = S(zn), T(yM), T(yR)
    print(f"  n={n}: reading M (both from z0) e_n={abs(zn-yM):.4f}; reading R (y0=-1) e_n={abs(zn-yR):.4f}; (T2) bound={bound(n):.4f}")
print("  Note: under R, e_1 = 2.1 is not the one-step discrepancy 0.1; under M, e_1 = 0.1 is it.")
I = lambda v: v
eM = [abs(I(0.0) - I(0.0)) for n in range(4)]; eR = [abs(0.0 - 1.0) for n in range(4)]
print(f"  eps=0, exact square (S=T=id, L=1): reading M e_n={eM} (= functional transport, L366); reading R with y0=z0+1 e_n={eR}; (T2) bound=0 at every n")

print("\n=== Side gap: 'an L-Lipschitz next-step map' read as the TARGET's map, matching start (reading M)")
eps = 0.1
Sd = lambda z: z                       # target step: identity on R, 1-Lipschitz in any metric
pi = lambda z: (z, 0.0)                # pi: R -> R^2, not onto
Tr = lambda p: (p[0] + 100*p[1], p[1] + eps)   # represented step
d = lambda p, q: math.hypot(p[0]-q[0], p[1]-q[1])
print("  one-step discrepancy at sample target states:", [round(d(pi(Sd(w)), Tr(pi(w))), 12) for w in (-3, 0, 2.5, 10)])
z0 = 0.0; zt, y = z0, pi(z0)
for n in range(4):
    print(f"  n={n}: e_n={d(pi(zt), y):.4f}  (T2) with L=1 (target map): {eps*n:.4f}   with L=Lip(T)~100.01: {eps*sum(100.01**k for k in range(n)):.4f}")
    zt, y = Sd(zt), Tr(y)

print("\n=== Block (common-coarsening) reading, equal-count variant: {az,aw} vs {by,bw} projected onto (x,w)")
pa, sa = sol(Ea, ['az', 'aw'], 'id'); pb, sb = sol(Eb, ['by', 'bw'], 'id')
print("  equal:", all(same(project(sol(Ea, ['az','aw'], e)[1], pa, ['x','w']), project(sol(Eb, ['by','bw'], e)[1], pb, ['x','w'])) for e in EDITS),
      "(true only after merging components; no such notion is defined in files 10/11)")
```

Output:

```

=== Counter-instance 1: x=u, y=2x, z=y+1; E1 = D, E2 = {x=u, z=2x+1}
  E1: (F1) True  (F2) True  (A) True
  E2: (F1) True  (F2) True  (A) True
  component-to-component 'one kind' (K, with footprint bijection):
    E1.kx  ~ ['mx']
    E1.ky  ~ []
    E1.kz  ~ []
    E2.mx  ~ ['kx']
    E2.mz  ~ []
  component-to-subnetwork (defence line iii):
    E1.kx  -> subnetworks of E2: [(['mx'], ('x',)), (['mx', 'mz'], ('x',))]
    E1.ky  -> subnetworks of E2: none
    E1.kz  -> subnetworks of E2: none
    E2.mx  -> subnetworks of E1: [(['kx'], ('x',)), (['kx', 'ky'], ('x',)), (['kx', 'kz'], ('x',)), (['kx', 'ky', 'kz'], ('x',))]
    E2.mz  -> subnetworks of E1: [(['ky', 'kz'], ('x', 'z'))]
  anchor-sharing pairs (defence line ii-b): [('kx', 'mx')]; of one kind: [True]

=== Counter-instance 2 (equal counts): x=u, y=x+1, z=y+1, w=z; Ea cuts at y, Eb cuts at z
  Ea: (F1) True  (F2) True  (A) True
  Eb: (F1) True  (F2) True  (A) True
  component-to-component 'one kind' (K, with footprint bijection):
    Ea.ax  ~ ['bx']
    Ea.az  ~ []
    Ea.aw  ~ []
    Eb.bx  ~ ['ax']
    Eb.by  ~ []
    Eb.bw  ~ []
  component-to-subnetwork (defence line iii):
    Ea.ax  -> subnetworks of Eb: [(['bx'], ('x',)), (['bx', 'by'], ('x',)), (['bx', 'bw'], ('x',)), (['bx', 'by', 'bw'], ('x',))]
    Ea.az  -> subnetworks of Eb: [(['by', 'bw'], ('x', 'w'))]
    Ea.aw  -> subnetworks of Eb: none
    Eb.bx  -> subnetworks of Ea: [(['ax'], ('x',)), (['ax', 'az'], ('x',)), (['ax', 'aw'], ('x',)), (['ax', 'az', 'aw'], ('x',))]
    Eb.by  -> subnetworks of Ea: none
    Eb.bw  -> subnetworks of Ea: none
  anchor-sharing pairs (defence line ii-b): [('ax', 'bx')]; of one kind: [True]

=== (T2) readings on W31's example: S(z)=2z+0.1, T(y)=2y, pi=id, eps=0.1, L=2
  n=0: reading M (both from z0) e_n=0.0000; reading R (y0=-1) e_n=1.0000; (T2) bound=0.0000
  n=1: reading M (both from z0) e_n=0.1000; reading R (y0=-1) e_n=2.1000; (T2) bound=0.1000
  n=2: reading M (both from z0) e_n=0.3000; reading R (y0=-1) e_n=4.3000; (T2) bound=0.3000
  n=3: reading M (both from z0) e_n=0.7000; reading R (y0=-1) e_n=8.7000; (T2) bound=0.7000
  n=4: reading M (both from z0) e_n=1.5000; reading R (y0=-1) e_n=17.5000; (T2) bound=1.5000
  Note: under R, e_1 = 2.1 is not the one-step discrepancy 0.1; under M, e_1 = 0.1 is it.
  eps=0, exact square (S=T=id, L=1): reading M e_n=[0.0, 0.0, 0.0, 0.0] (= functional transport, L366); reading R with y0=z0+1 e_n=[1.0, 1.0, 1.0, 1.0]; (T2) bound=0 at every n

=== Side gap: 'an L-Lipschitz next-step map' read as the TARGET's map, matching start (reading M)
  one-step discrepancy at sample target states: [0.1, 0.1, 0.1, 0.1]
  n=0: e_n=0.0000  (T2) with L=1 (target map): 0.0000   with L=Lip(T)~100.01: 0.0000
  n=1: e_n=0.1000  (T2) with L=1 (target map): 0.1000   with L=Lip(T)~100.01: 0.1000
  n=2: e_n=10.0020  (T2) with L=1 (target map): 0.2000   with L=Lip(T)~100.01: 10.1010
  n=3: e_n=30.0015  (T2) with L=1 (target map): 0.3000   with L=Lip(T)~100.01: 1010.3010

=== Block (common-coarsening) reading, equal-count variant: {az,aw} vs {by,bw} projected onto (x,w)
  equal: True (true only after merging components; no such notion is defined in files 10/11)
```

---

## What this defence does not show

- **It does not show what the author intended.**
  - For (T2), the defence rests on the text's objects and on the formula's own instances.
  - For Derivation 2, the ruling rests on the words. The author may well have meant the co-anchored reading.
- **File 12 was not opened.**
  - W31 reports that the (T2) line there is identical.
  - Whether file 12's Derivation 2 matches was not checked.
- **The case book was not opened.**
  - W19 §1.5's statements about case consequences are neither confirmed nor disputed here.
- **No authority file was edited.** Checked against commit 2788a77.
