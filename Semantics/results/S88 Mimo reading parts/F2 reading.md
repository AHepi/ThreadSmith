# S88: reading of Mimo's reply to part F2, (T2)

*Written by a fresh Claude reader on 23 September 2026, about 18:40 to 19:05 UTC. This reader wrote none of the findings. The reply is read under the S88 rule (`results/S88 How the cross-examination will be read - written after Atria's reply arrived, before it was opened.md`) as changed, before sending, by `results/S88 Mimo's reply in three parts - how it will be read, written before sending.md` (committed at db05b18, 17:47 UTC).*

**What this reader opened.** The rule, the note, the F2 part brief (`tests/S88 Cross-examination - part F2, (T2).md`), the F2 receipt and the F2 response, and files 10 and 11 in `authority/`. **What this reader did not open:** Atria's reply, its reasoning or receipt; `S88 Reading of Atria's reply - the three defects.md`; the F1 and F3 replies and any reading of them; the F2 reasoning file; any file of the failed single Mimo call. This reader also saw file names in the returns folders, and nothing more of them.

**Late rule (R7).** The note says the rule was committed at 15:36 UTC, before any part was sent. So R7's late-rule statement does not go with this reading.

**Starting positions (the note's change to R3 and R5).** This reading starts from Claude's positions after Atria's reading, as the note sets them out. Atria's reading started from the positions frozen at 15:35 UTC. When the readings are put side by side, the comparison must say so.

## R1. The receipt

The receipt `s88_xexam_mimo_F2.receipt.json` was opened first.

- finish_reason "stop", saw_done true, bad_chunks 0.
- One attempt, accepted, with 12,028 reply characters.
- `user_sha256` 9c24e62f7ef1…, which is the sha256 of the part brief as committed.
- `response_sha256` 83875787e7c4…, which matches the response file.
- The reply's last line is END OF REPORT, with no trailing newline.

**The part is accepted, and it is read.**

The theory text between the brief's marker lines (brief lines 22–650) is byte for byte file 10 (`cmp`: identical, sha256 4aa2c97ea0cf…). Theory line numbers below are file 10's. File 11 carries line 376 word for word as its line 361, so every point below applies to file 11 too. The file 11 line numbers are 351 for functional transport, 191 for π, 179 for the simulation layer, 455 for (CT1) and 538 for the Part XV entry.

## Step 1. Claude's position on F2, after Atria's reading (copied from the note)

> **F2: UPHELD.** (T2) omits h1 to h3, and this is a drafting omission, fixed by an erratum. The erratum now carries the scope clause:
>
> > **Approximate transport.** With one-step discrepancy d(πSz, Tπz) ≤ ε at every state z of the stated scope and an L-Lipschitz represented next-step map T, the discrepancy after n steps from one state z, e_n = d(πSⁿz, Tⁿπz) (so e₀ = 0), satisfies e_n ≤ ε Σ_{k<n} L^k whenever z, Sz, …, S^{n−1}z lie in that scope. (T2) Without a modulus, no accumulated bound follows. An exact question is not silently replaced by an approximate one.
>
> The unequal-start clause stays optional.

The part brief carries the erratum **as sent to Atria**. That version has no clause "whenever z, Sz, …, S^{n−1}z lie in that scope", and its first clause reads "at every state \(z\) of the stated scope". The side note "both runs must stay inside the region where \(\varepsilon\) and \(L\) hold" sits outside the wording.

## Step 2. Mimo's argument

**Verdict line (reply line 23):** "F2: PARTLY UPHELD".

Restated under the reply's own point numbers:

1. **(h2) and counterexample 2b stand.** "Counterexample 2b stands; I could not refute it. This is the part of the finding that carries the defect." Line 376 states two assumptions, and 2b meets both, taking the target map \(S=\mathrm{id}\) as the "L-Lipschitz next-step map" with \(L=1\). Its \(e_2\approx10.002\) exceeds 0.2. The induction closes only with \(L=\operatorname{Lip}(T)\), and "Nothing else fixes the referent ('Lipschitz' occurs only on line 376)". So Part XV's test is engaged.
2. **(h1) fails, and so does 2a.** "on the theory's stated setup there is no free starting error to fix." Every comparison of D with E is at the translated point (lines 204, 257, 265, 234, 366, 371). So \(e_n\) "can only be the transport-square defect" and "\(e_0=d(\pi z,\pi z)=0\) is definitional, not a hypothesis". With a matched start, 2a meets the bound with equality. Its failure lies "in the imported datum \(y_0=-1\)". The predecessor's discrepancy is a same-input one, so its "With \(e_0=0\)," is a base case. "What survives of (h1) is one true but smaller observation: line 376 never defines \(e_n\)", which is "a notation gap, closed by the repair's definition".
3. **(h3) survives only in reduced form.** Counterexample 2c "breaks a stated assumption under the natural reading", on which each step's discrepancy is at most ε. The discrepancy at \(z_1\) is 0.11. The start-only reading "is not available", because on it "line 376 would be false in every case". What survives is the missing scope clause. Mimo gives a corrected instance: \(\pi=\mathrm{id}\), \(T(y)=2y\), \(S(z)=2z+0.1+\varphi(z)\) with \(\varphi=0\) on \([-1,1]\) and \((|z|-1)^2\) outside, scope \([-1,1]\). Then \(e_5=3.35>3.1\).
4. **The repair as sent is defeated by that instance.** "the side note must be moved into the sentence." The point has two parts: (a) "the stated scope" points at nothing in (T2); (b) the bound can hold on a scope that the orbit later leaves. "The same containment is needed for \(L\)." Mimo offers its own wording.
5. **The optional unequal-start clause is incoherent as placed.** Under the definition "(so \(e_0=0\))" it is vacuous. It should be dropped, or stated "as a separate two-run generalization with its own \(e_n\)".
6. **The repair breaks nothing.** "(T2)" occurs only at line 376 and in Part XV's list. The reply goes through Derivations 1, 8, 9 and 10, Part VI, Part VII's worked cases and the two paragraphs on what (E) excludes and does not exclude.
7. **Notation.** The letter \(S\) collides with the simulation layer (line 192) and with \(S_0\) and \(S_1\) (Derivation 10). \(T\) collides with the task of (CT1). \(L\) is overloaded four ways. The repair should tie \(S\) and \(T\) to line 366's \(S_a\) and \(T_a\).
8. **Summary.** Held: (h2) with 2b; the reduced (h3) with the corrected instance; the undefined \(e_n\); the classification as a drafting omission. Not held: (h1) as a missing hypothesis; 2a; 2c as given.

## Step 3. Check against the theory text

### Lines relied on (file 10)

- **376:** "**Approximate transport.** With one-step discrepancy \(\varepsilon\) and an \(L\)-Lipschitz next-step map, \(e_n\le\varepsilon\sum_{k<n}L^k\). (T2) Without a modulus, no accumulated bound follows. An exact question is not silently replaced by an approximate one."
- **366:** "**Functional transport.** If \(\pi\circ S_a=T_a\circ\pi\) for every generator \(a\), the same holds for every admitted finite composition with matching scopes. *Proof.* \(\pi S_bS_a=T_b\pi S_a=T_bT_a\pi\); induct. ∎"
- **204:** "where \(\pi:X_D\to X_E\) on the stated scope, …"
- **371:** "zRy\land z\xrightarrow{a}z'\Rightarrow\exists y'[y\xrightarrow{\tau(a)}y'\land z'Ry'], \tag{T1}"
- **374:** "… Composition of relations preserves both directions when intermediate scopes agree."
- **543:** "**A mathematical error.** A counterexample to the finite monotone theorem, (I2), (O1), (T2), (CT2), or Derivations 1–3 under their stated assumptions."
- **192:** "The **simulation layer** \(S\) is an organization over \(P\) …"
- **234:** "the **expectation** is \(\operatorname{Ans}_S(\tau(a),\sigma(b))\);"
- **466:** "**Retained realization.** For protocol \(\pi\), task \(T\), …" This is the definition tagged (CT1), at line 469.

### Searches over file 10

- **"Lipschitz", "discrepancy" and "modulus"** each occur only on line 376.
- **"initial"** does not occur.
- **\(e_n\)** occurs only on line 376, and it is never defined.
- **"(T2)"** occurs only on lines 376 and 543.
- **\(S_a\) and \(T_a\)** occur only on line 366.
- **"generator"** occurs only on line 366.

### Quotations

Every quotation in the reply was checked word for word against file 10 and against the part brief. The checked lines are 105, 111, 192, 204, 234, 257, 265, 338, 366, 371, 374, 376, 466, 543, 555, 609, 613 and 619, plus the predecessor passage and the finding's side note and reply. **No misquotation was found.**

Three small inaccuracies, none of them a misquotation:

- Point 6 lists (F2) and (A) among Derivation 10's grounds. Its text (615–629) names (F1), (G), (P), (EK) and Derivations 1, 2 and 4. (F2) and (A) enter only through "faithful", which line 204 defines by "the component and global fidelity conditions of Part V".
- Point 1 says \(\pi\circ S=\pi\) is 1-Lipschitz "in every metric". That is true only for a metric on \(\mathbb R\) that makes π an isometry. It does no work, because \(S=\mathrm{id}\) alone supplies \(L=1\).
- Point 3 says that on the start-only reading "line 376 would be false in every case". That is too strong. On that reading line 376 is false in some cases (2c) and true in others (\(S=T\), for example). What follows is only that it would not be a theorem.

### Instances, redone in exact rational arithmetic

The script is `s88m/f2_check.py`, in this reader's scratchpad, and uses `fractions.Fraction` throughout.

**2b.** The one-step discrepancy is exactly 1/10 at every z.
- \(e_n^2=(5n(n-1))^2+(n/10)^2\), so \(e_2^2=2501/25\), and \(e_2=\sqrt{100.04}\).
- With \(L=1\), the bound is 1/5, which fails. It also fails at n=3.
- \(\operatorname{Lip}(T)=\sigma\), where \(\sigma^2\) is the larger root of \(x^2-10002x+1\). A rational bracket gives \(100.009<\sigma<100.01\).
- With \(L\) set to the lower bracket, the bound holds for n = 1 to 59. So it holds with \(L=\sigma\).

**Confirmed.**

**2a.** Two runs, with \(y_0=-1\).
- \(e_n=1,\ 21/10,\ 43/10,\ 87/10,\ 35/2,\ 351/10\) against bounds \(0,\ 1/10,\ 3/10,\ 7/10,\ 3/2,\ 31/10\). It fails at every n, and it meets \(L^ne_0+\varepsilon\sum L^k\) exactly.
- With a matched start, \(e_n=0.1(2^n-1)\), which equals the bound at every n.

**Mimo's arithmetic is confirmed.**

**2c.** The orbit is 0, 1/10, 31/100.
- The discrepancy is 1/10 at \(z_0\) and 11/100 at \(z_1\).
- \(e_2=31/100\) against a bound of 3/10.

**Confirmed.**

**Mimo's scope instance.** The orbit is 0, 1/10, 3/10, 7/10, 3/2, 67/20.
- \(e_n\) equals the bound for n ≤ 4.
- \(e_5=67/20>31/10\).
- The step discrepancies at \(z_0\) to \(z_4\) are 1/10, 1/10, 1/10, 1/10 and **7/20**.

**The arithmetic is confirmed.** The last discrepancy matters below.

**The current wording.** Randomized exact check:
- T is continuous piecewise-linear on \(\mathbb R\), with global Lipschitz constant equal to its largest absolute slope.
- S is arbitrary piecewise-linear, and π = id.
- ε is taken as the largest discrepancy on a grid over the scope. The grid can only underestimate that largest value, so the check is conservative.
- 2,144 cases have \(z,\dots,S^{n-1}z\) in the scope, with no violation.

**The restated unequal-start clause (below).** Checked over 200 random pairs of starts under 2a's maps, with no violation, and 2a meets it exactly.

### Readings: which words fix them

**(h2), whose Lipschitz constant.** No words fix it. Line 376 has "an \(L\)-Lipschitz next-step map", with the indefinite article. Line 366 has two step maps, and "Lipschitz" occurs nowhere else. So 2b meets both stated assumptions under a reading that uses only objects the line names, and the claim fails. **Point 1 holds, and it agrees with the finding.**

**(h1), matching starts.** No words define \(e_n\). Mimo's argument was checked line by line:
- Every comparison of D with E in the text is at the translated point (204, 234, 257, 265, 366) or through a relation that ties y to z (371).
- The text has no second starting state, and the word "initial" does not occur.
- 2a needs \(y_0\), an object that no line of the theory introduces.

2b and 2c differ from 2a here: each uses only what line 376 itself names, a next-step map and a one-step discrepancy. So there is a real asymmetry.
- 2a is a counterexample only if the undefined \(e_n\) is filled in with an object brought in from outside the text.
- The reading from a matched start is built from π, the step maps of line 366 and the line's own n=1 instance. At n=1, "\(e_1\le\varepsilon\)" restates the hypothesis only when the start is matched.

Mimo's further claim that \(e_0=0\) "is definitional" presupposes a definition the text does not give. The same holds for its claim that "no corrected counter-instance exists". So the surviving defect is exactly the one Mimo names: **line 376 never defines \(e_n\)**. Without a definition, what (T2) bounds is not stated, and Part XV's "under their stated assumptions" cannot be run on it. "Matching starts" is not a further hypothesis that needs restoring. It follows at once from the only definition the text's objects support. **Point 2 holds, as a restatement of (h1).** It does not remove (h1).

**(h3), where ε holds.** No words fix it. Line 376 has only "With one-step discrepancy \(\varepsilon\)". Mimo rejects 2c on the "each step" reading. That is the brief's own defence ("most naturally bounds each step's discrepancy"), and the finding's reply already met it: a reading that the text suggests but does not state is not a stated assumption. Mimo adds one ground, that the start-only reading would make line 376 "false in every case". That ground is overstated (see above), and an argument that picks whichever reading makes the claim true would seal every underspecified claim against Part XV.

**Mimo's corrected instance does not do what point 3 says.** It too breaks the "each step" reading that Mimo uses against 2c: its fifth step discrepancy is 7/20 > 1/10. Against line 376 as written, then, it is no stronger than 2c. It holds only on a reading that brings in a scope line 376 does not state. Its real target is the erratum **as sent**, which bounds ε "at every state z of the stated scope" and does not require the orbit to stay in that scope. Against that wording it is a valid counter-instance (point 4(b)).

**(h3) stands as the finding states it.**

**Classification.** The theorem is true with the predecessor's hypotheses: \(L=\operatorname{Lip}(T)\), ε at every state reached, and \(e_n\) the n-step defect of the square from one state. The proof is the finding's point 3, and the randomized check agrees. Line 376 dropped those hypotheses in condensing. **The classification as a drafting omission holds, and Mimo agrees (point 8).**

### The repair (R6)

**Point 4(b), containment.** This point argues against wording since tightened. Against the erratum as sent it holds: Mimo's instance satisfies "at every state \(z\) of the stated scope" on \([-1,1]\) and breaks the bound at n=5. Against the current wording it does not hold: n=5 needs \(z_4=3/2\) in the scope, so the current wording claims only n ≤ 4, where the bound holds with equality. Under the note's rule, this is recorded as bearing only on changed wording. It neither reopens that change nor counts as support for it.

**Point 4, "the same containment is needed for \(L\)".** This does not hold against either wording. Both require T to be L-Lipschitz with no restriction, which is global. The step \(d(T\pi z_n,Ty_n)\le L\,d(\pi z_n,y_n)\) needs nothing more.

**Point 4(a), "the stated scope points at nothing".** Only partly right. "the stated scope" does have an antecedent in the theory: π's scope at line 204 (file 11: 191). But (T2) states no scope of its own, and the predecessor's article is "a" ("on a stated scope"). Changing "the" to "a" removes the objection at no cost. It also lets ε be claimed on a region smaller than π's scope. This holds against the current wording as well.

**Point 5, the optional clause.** This holds against the current wording, which keeps the clause as optional. Under the erratum's own definition, \(e_n=d(\pi S^nz,T^n\pi z)\), \(e_0\) is 0 for every system. So "with initial discrepancy \(e_0\), \(e_n\le L^ne_0+\dots\)" says nothing beyond the erratum. A two-run quantity needs a second start, and by the (h1) check above the theory has none. The clause is true only as a separate claim about its own quantity.

**Point 7, the letter S.** This holds against the current wording. The erratum names T ("represented next-step map T") but never introduces S. The theory's only other bare S is the simulation layer (line 192; file 11: 179). That layer is a representing organization: "the **expectation** is \(\operatorname{Ans}_S(\tau(a),\sigma(b))\)" (line 234). So in a two-layer case like Derivation 10, a reader can take the erratum's S, which is the target's step, for the side the erratum calls T. The collision of T with the task of (CT1) (line 466) is harmless, because (CT1) is far away. The collision of π with the protocol π of (CT1) predates the repair. The collision of L is already recorded in the finding's side note.

**Mimo's own wording.** Not adopted as a whole, for three reasons:
- It asks for ε "at every iterate of a start \(z\)", a scope that contains the whole forward orbit. So it yields no bound at all when the orbit leaves the scope. The current clause gives the bound for every n up to the exit.
- It puts states of \(X_D\) and pairs in \(X_E\) into one "scope".
- Its restriction of Lipschitz to "there" is a generalization, not a fix.

Its one useful element is adopted: fixing the roles of S and T by line 366.

**Point 6, breakage.** Confirmed. "(T2)" is cited nowhere but line 543. The quotations that point 6 relies on (lines 555, 609, 613, 619) are exact. Part VI's cases (lines 322–330) and Part VII's cases (lines 336–360) contain no metric or accumulated-error claim. The repair strengthens the stated hypotheses of an uncited result and defines its symbol, so it cannot break the exact cases. After the repair, Part XV's test becomes runnable on (T2).

## Step 4. Ruling

**F2: NARROWED.** The narrowing touches only (h1). Everything else stands, including the classification.

- **What stands:**
  - (h2), with counterexample 2b. Every step of 2b was rechecked, and Mimo confirms it.
  - (h3) as stated, with counterexample 2c on the start-only reading, which no words exclude. Mimo's rejection of 2c rests on a reading no words fix. Its corrected instance breaks that same reading.
  - The classification, a drafting omission fixed by an erratum.
- **What is narrowed.** (h1) is restated. The defect is that line 376 never defines \(e_n\). It is not that a "matching starts" hypothesis was omitted. The theory has no second starting state: every comparison of D with E is at the translated point (lines 204, 234, 257, 265, 366, 371), and "initial" does not occur. So counterexample 2a is not a counterexample under the stated assumptions. It illustrates what the undefined symbol admits once an object from outside the text (\(y_0\)) is brought in. Once \(e_n\) is defined as the n-step defect of line 366's square from one state, \(e_0=0\) follows by definition. The erratum already does exactly this, so the narrowing changes no part of the erratum's defining clause.
- **The finding, restated:** "(T2) omits two hypotheses its proof needs, namely whose Lipschitz constant (h2) and where ε holds (h3), and it leaves \(e_n\) undefined (h1), so the start is fixed by no words. On readings that leave these open it has counterexamples (2b for h2, 2c for h3). 2a is a counterexample only on a two-run reading whose second start the theory never introduces. This is a drafting omission, fixed by an erratum that restores the predecessor's hypotheses and defines \(e_n\)."
- **Not a basis for the ruling.** Mimo's verdict line (PARTLY UPHELD) did not decide this ruling (R2). It rests on the check above. On two points the reading and Mimo differ: Mimo's reduction of (h3) is not accepted, and neither is its "same containment for L".

## R6. Changes to the repair, prompted by Mimo's reply to part F2, after the cross-examination

Three changes. Each came after the cross-examination and was prompted by this part.

1. **S is introduced and tied to the roles in line 366** (Mimo, point 7). Reason: the current wording never introduces S, and the theory's only other bare S is the simulation layer, a representing organization (lines 192, 234). This change is required.
2. **"the stated scope" becomes "a stated scope"** (Mimo, point 4(a)). Reason: (T2) states no scope of its own; the predecessor, which the erratum restores, says "on a stated scope"; and ε may hold on less than π's scope. This change is minor; the claim is true either way.
3. **The unequal-start clause is dropped from the erratum** (Mimo, point 5). Reason: under the erratum's definition \(e_0=0\) for every system, so the clause as worded is vacuous, and it is a claim the predecessor did not make. If it is wanted at all, it is added separately and recorded as an addition, not as part of the erratum, in the wording below.

Not changed: the containment clause (point 4(b) bears only on the wording as sent) and the Lipschitz hypothesis (point 4's "containment for L" fails against both wordings).

**Erratum, exact wording (replace line 376 of file 10 and line 361 of file 11):**

> **Approximate transport.** Write \(S\) for the target's next-step map and \(T\) for the represented one, in the places \(S_a\) and \(T_a\) hold in functional transport. With one-step discrepancy \(d(\pi Sz,T\pi z)\le\varepsilon\) at every state \(z\) of a stated scope and \(T\) \(L\)-Lipschitz, the discrepancy after \(n\) steps from one state \(z\), \(e_n=d(\pi S^nz,T^n\pi z)\) (so \(e_0=0\)), satisfies \(e_n\le\varepsilon\sum_{k<n}L^k\) whenever \(z,Sz,\dots,S^{n-1}z\) lie in that scope. (T2) Without a modulus, no accumulated bound follows. An exact question is not silently replaced by an approximate one.

**Optional separate addition, not part of the erratum (only if wanted):**

> If the represented run starts instead at a state \(y\) of \(X_E\), then under the same conditions \(d(\pi S^nz,T^ny)\le L^n\,d(\pi z,y)+\varepsilon\sum_{k<n}L^k\).

The optional addition's proof is the same induction: \(d(\pi Sz_n,Ty_n)\le d(\pi Sz_n,T\pi z_n)+d(T\pi z_n,Ty_n)\le\varepsilon+L\,d(\pi z_n,y_n)\). 2a meets it exactly, and the random-start check found no violation.

## R4. Further defects offered

The part asks for none, and the reply offers no further counterexample to the theory. Two items were checked as possible further defects.

- **Mimo's scope instance.** It is a counter-instance to the erratum as sent, not to the theory. It is recorded under F2 above. It is not a new finding.
- **Point 7's notation collisions.** They make no claim false, so Part XV's "mathematical error" is not engaged, and they are not a new finding. They are met in the erratum by change 1.

**Observed in passing, and not offered by Mimo.** Line 366's \(S_a\), \(T_a\) and "generator" occur nowhere else in file 10, so functional transport itself uses letters the text never introduces. Their types come only from \(\pi:X_D\to X_E\) (line 204). No claim becomes false: the proof in line 366 holds for any maps typed so the square makes sense. This is recorded here for the orchestrator. It is not added as a finding under R4, because no reply offered it.

## Files

- `results/S88 Cross-examination - three defects - returns/Mimo in three parts/s88_xexam_mimo_F2.receipt.json` and `…F2.response.txt`: read. The reasoning file was not opened.
- `tests/S88 Cross-examination - part F2, (T2).md`: the part as sent (sha256 9c24e62f7ef1…).
- `authority/10 …` (sha256 4aa2c97ea0cf…) and `authority/11 …` (sha256 054d76522773…): the theory text.
- Scratchpad `s88m/f2_check.py`: the exact-arithmetic checks.
