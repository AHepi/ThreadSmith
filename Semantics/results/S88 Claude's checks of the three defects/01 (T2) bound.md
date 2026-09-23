# W31: the (T2) accumulated-error bound and unequal starting states

*Moved into the repository on 23 September 2026 from the session scratchpad, where it was `revision2/checks/W31 T2 bound.md`; only this paragraph was added. The first of Claude's three checks of the defects later put to Atria and Mimo in S88, written on 23 September 2026 by a Claude subagent for the revision-2 worklist (item W31; the worklist is now `tests/Revision 2 - worklist, draft of 23 September.md`). It tests whether (T2), Part VIII's accumulated-error bound, fails when the two runs start from unequal states. They underpin S88: the S88 brief (`tests/S88 Cross-examination - three defects in the theory's own defeat list.md`) states the three defects and the theory's defence that these checks set out, and the S88 reading (`results/S88 Reading of Atria's reply - the three defects.md`) read them under their scratchpad names, `revision2/checks/W31 T2 bound.md`, `W19 W20 Mimo holes.md` and `defence of T2 and Derivation 2.md`, which are 01, 02 and 03 in this folder.*

**The claim under test** (worklist W31, from S78 Results item 10 and the S72 Stage 2 return's quotation of R2 J): (T2) holds only when the two runs start from matching states. With a starting error e0, the correct bound is L^n·e0 + ε·Σ_{k<n} L^k. As stated, (T2) therefore has a literal counterexample, and Part XV lists (T2) among the results whose failure would refute the theory.

**Verdict: CONFIRMED BUT HARMLESS**, for files 10, 11 and 12. It is **REFUTED for file 00** (the FW5 predecessor), because its line 578 states e0 = 0.

- **Files 10 to 12.** As written, (T2) is false under the assumptions those files state. Nothing in them fixes the starting error. No line even defines e_n. The n = 0 case of (T2) says e_0 ≤ 0, so (T2) quietly assumes matching starts without saying so. The example given below meets every stated assumption and still breaks the bound, and at every n.
- **Why it is harmless.** No other claim in files 10, 11 or 12 uses (T2). The corrected bound is a generalisation that becomes (T2) exactly when e0 = 0.
- **The one place it is not harmless.** Part XV lists (T2) under "A mathematical error ... under their stated assumptions". Read literally, the counterexample triggers that clause, so the files need an erratum and not just a reading note.
- **How to fix it.** Put back the hypothesis that FW5 stated and files 10 to 12 dropped when they were condensed from it.

---

## 1. The texts

### File 00 (FW5 predecessor): where (T2) was first stated, with its hypothesis

`Semantics/authority/00 FW5 JUMP from FW2+FW3+FW4 - Explanatory construction (predecessor, 8 September 2026).md`

- 564–570: "Suppose three representations have maps \(f:X\to Y\), \(g:Y\to Z\), and an actual map \(h:X\to Z\). If \(d_Z(h(x),g(f(x)))\le\varepsilon\) on a stated scope, then that bound is the claim. It does not automatically survive repeated use."
- 572: "For stepwise dynamics, suppose the discrepancy after one mapped step is at most \(\varepsilon\), and the represented next-step map is \(L\)-Lipschitz. Writing \(e_n\) for the discrepancy after \(n\) steps gives"
- 575: \(e_{n+1}\le L e_n+\varepsilon.\)
- **578: "With \(e_0=0\),"**
- 581–582: \(e_n\le\varepsilon\sum_{k=0}^{n-1}L^k.\) (T2)
- 585: "**Proof.** Substitute the preceding bound into the recurrence and induct. ∎"
- 587: "Without a Lipschitz bound, a stated modulus of continuity can replace multiplication by \(L\). Without either, a general accumulated-error bound does not follow. ..."
- 1390, the counterpart of Part XV: "A counterexample to (M1), (M2), (I2), (O1), (T2), or the retention fixed-point result while all stated assumptions hold would expose a mathematical error. Finding that real inquiries do not satisfy those assumptions instead restricts the application; it does not refute the conditional theorem."

FW5 defines e_n generally, as "the discrepancy after n steps". It states the recurrence for any e_0 and then assumes e_0 = 0 as a separate hypothesis. So the author of FW5 treated the starting error as something that had to be fixed by assumption.

### Files 10, 11 and 12: (T2) with that hypothesis gone

The (T2) sentence is identical in all three files:

> **Approximate transport.** With one-step discrepancy \(\varepsilon\) and an \(L\)-Lipschitz next-step map, \(e_n\le\varepsilon\sum_{k<n}L^k\). (T2) Without a modulus, no accumulated bound follows. An exact question is not silently replaced by an approximate one.

- File 10 (`10 Claude Fable Semantics - standalone theory.md`): line **376**. Part VIII heading at 364. Functional transport at 366: "If \(\pi\circ S_a=T_a\circ\pi\) for every generator \(a\), the same holds for every admitted finite composition with matching scopes." π is defined at 204: "\(\pi:X_D\to X_E\) on the stated scope". Part XV heading at 531; entry at **543**: "**A mathematical error.** A counterexample to the finite monotone theorem, (I2), (O1), (T2), (CT2), or Derivations 1–3 under their stated assumptions."
- File 11 (`... revision 1.md`): (T2) at line **361**, functional transport at 351, Part XV entry at **538** (same wording as file 10).
- File 12 (`... causality, standalone theory.md`): (T2) at line **371**, functional transport at 361, Part XV entry at **556** ("Derivations 1–4").

**What files 10 to 12 state:** a per-step discrepancy ε, and a next-step map that is L-Lipschitz.

**What they never state or define:**
- what e_n is;
- the metric;
- which next-step map must be Lipschitz (FW5 says "represented");
- that ε bounds the discrepancy at every state of a scope (FW5 says "on a stated scope");
- the starting condition.

`grep -ic initial` returns 0 for all three files, which confirms S78's remark and extends it to file 12. `grep` also finds "Lipschitz", "approximat", "accumulat", "modulus" and "e_n" only on the (T2) line itself.

### The objection as it was raised

- R2 J, source `Semantics/results/S64 Near cases - return/05 Quotations.md` line 139, row S64-R2-J01. It is quoted verbatim as [T-R27] in `Semantics/results/S72 Stage 2 audit - return/01 Audit of the bare version table.md` lines 494, 808 and 1064, in `03 Audit of the quotations.md` line 1060, and in `04 Fix card for Derivation 3.md` line 58:
  > "In Part VIII, the accumulated-error bound without an initial-error term presupposes matching initial states. With initial discrepancy, retain its propagated contribution as well as the sum of new discrepancies."
- The S72 Stage 2 return, `05 Report addendum.md` line 138: "Likewise R2 J's separate initial-error qualification and the advertised dependence-order question are not resolved by this population fix."
- S78 Results, line 26 (item 10): "**R2 J's second qualification has no case.** Its Part VIII sentence on the accumulated-error bound with unmatched initial states was named unresolved by Stage 2, is absent from S75, and is unchanged in file 11; the word "initial" occurs in neither file 10 nor file 11." Line 46: "'What this does not show' should have listed R2 J's Part VIII qualification, untested by any case."

R2 J describes the problem as a hidden presupposition. W31 describes it as a literal counterexample. The two are the same fact seen from two sides. Because no line in files 10 to 12 states the presupposition, the literal text is open to a counterexample.

---

## 2. Is (T2) true under its own stated hypotheses?

In what follows, S is the target's next-step map, T the represented one, and π the transport map. The one-step discrepancy is ε ≥ d(π S w, T π w), the target's step projected against the model's step, taken over the states visited.

**Reading M: e_n compares two maps applied to the same state z.** Here e_n := d(π S^n z, T^n π z). This is the approximate version of the functional-transport square directly above (T2) (file 10 line 366). Under this reading e_0 = d(πz, πz) = 0 automatically, and (T2) is **true**:

  e_{n+1} = d(π S z_n, T y_n) ≤ d(π S z_n, T π z_n) + d(T π z_n, T y_n) ≤ ε + L·e_n,

where y_n = T^n π z. Induction from e_0 = 0 then gives e_n ≤ ε Σ_{k<n} L^k.

**Reading R: e_n tracks two runs, and the model's run starts from a state it is given.** Here y_0 is supplied, for example an estimated or measured starting state, and e_n := d(π z_n, y_n) with e_0 = d(π z_0, y_0). This is FW5's own general definition ("the discrepancy after n steps"), the one for which FW5 had to add "With e_0 = 0". Under this reading (T2) is **false** whenever e_0 > 0.

**No line in files 10 to 12 picks reading M.** e_n is never defined, reading M is only suggested by where (T2) sits, and the (T2) sentence does not refer back to π, S_a or T_a. So both readings fit the stated hypotheses. Separately from which reading is chosen, the n = 0 case of the formula (an empty sum) reads e_0 ≤ 0. So (T2) as written either assumes matching starts without saying so, or asserts them. It cannot hold for a start the hypotheses leave free.

### The counterexample (meets every hypothesis stated in files 10 to 12)

Take the state spaces to be ℝ with d(x, y) = |x − y|, π = id, S(z) = 2z + ε, T(y) = 2y, ε = 0.1, z_0 = 0, y_0 = −1 (so e_0 = 1).

- One-step discrepancy: |S(w) − T(w)| = ε = 0.1 at every w. ✓
- T is 2-Lipschitz, so L = 2. S is also 2-Lipschitz, so it does not matter which "next-step map" is meant. ✓
- e_n = 2^n + 0.1·(2^n − 1). At n = 3: e_3 = 8.7.
- (T2) bound at n = 3: 0.1·(1 + 2 + 4) = 0.7. **Violated, and at every n ≥ 0.**
- Corrected bound at n = 3: 2^3·1 + 0.7 = 8.7. It holds with equality, so it is tight.

**The simplest version:** S = T = identity, L = 1, ε = 0, e_0 = 1. Here e_n = 1 for every n, while (T2) gives 0 for every n.

The numbers were checked by the script in §6: the affine family with L ∈ {2, 1, 0.5}, the exact identity case, and 20,000 random nonlinear runs. Across those runs, (T2) failed in 5,095 of the runs with unequal starts, in 0 of the runs with matching starts, and the corrected bound failed in 0.

---

## 3. Is the bound otherwise correct?

- **Index range and where the error enters.** When ε is the discrepancy measured after the step (FW5 line 572: "after one mapped step"), the recurrence is e_{n+1} ≤ L e_n + ε. This gives Σ_{k=0}^{n−1} L^k, and "k < n" in files 10 to 12 is the right range. If ε were instead a perturbation of the input before the map, the step discrepancy after the map would be Lε and the sum would run over k = 1..n, which is larger by a factor of L when L > 1 (script, part D). The words "one-step discrepancy" in files 10 to 12 read naturally as the after-map quantity, so this is a minor wording point, not an error.
- **General form.** e_n ≤ L^n e_0 + ε Σ_{k<n} L^k, proved by induction: L(L^n e_0 + ε Σ_{k<n} L^k) + ε = L^{n+1} e_0 + ε Σ_{k<n+1} L^k. The affine family attains it exactly, so no smaller bound holds in general.
- **L = 1:** e_0 + nε. **L < 1:** L^n e_0 + ε(1 − L^n)/(1 − L) ≤ L^n e_0 + ε/(1 − L), so the starting error dies away but is positive at every finite n and (T2) fails at every n (script, L = 0.5). **L > 1:** the starting error grows like L^n, so leaving it out is the largest mistake in exactly the case where accumulated error matters most.
- **Three smaller gaps.** FW5 fills each of these in its own wording; files 10 to 12 dropped that wording. None of them is part of W31, but each alone would also produce a counterexample to the literal text:
  1. ε must bound the discrepancy at **every state visited**, not only at the starting state. FW5 line 570 has "on a stated scope". Script part E: a discrepancy of 0.1 at z_0 only gives e_2 = 0.31 > 0.3.
  2. The Lipschitz constant must belong to the **represented** map T, measured in the representation's metric. FW5 line 572 says "represented". Script part F: with π(z) = z³, the target map S(z) = 2z is 2-Lipschitz on its own scale, but T is 8-Lipschitz, and e_3 = 7.3 against the L = 2 bound of 0.7.
  3. Both runs must stay inside the region where ε and L hold.
- **Notation clash (cosmetic).** In files 10 to 12, L also names the component relations L_j (line 111), the last entry of the organization tuple (line 105), and the shadow length L := H cot θ (line 338).

---

## 4. Does anything later use (T2)?

No. In every file, (T2) appears only on its own line and in the Part XV list: file 10 lines 376 and 543, file 11 lines 361 and 538, file 12 lines 371 and 556. No derivation, dependence-order entry (file 10 line 525, file 11 line 518, file 12 line 536) or worked episode cites it. In file 00, the only other mention of T2 is at line 1328 ("[S5: T2]"), which is a pointer to a source document, not this theorem.

The corrected bound only adds a term that is never negative and becomes (T2) when e0 = 0, so it cannot break any use. The sentences after (T2) ("Without a modulus ...", "An exact question is not silently replaced ...") are unaffected.

The only thing exposed is Part XV. It names (T2) as something whose counterexample "under their stated assumptions" defeats the class. For files 10 to 12 that condition is met by the example in §2. FW5 line 1390 draws exactly the distinction needed here: a failed assumption restricts where a theorem applies but does not refute it. That distinction only works once the assumption is written down.

---

## 5. Proposed restatement and edits

**Minimal correct restatement:**

> **Approximate transport.** With one-step discrepancy \(\varepsilon\) at every state of the stated scope, an \(L\)-Lipschitz represented next-step map, and initial discrepancy \(e_0\), \(e_n\le L^ne_0+\varepsilon\sum_{k<n}L^k\); from matching initial states (\(e_0=0\)), \(e_n\le\varepsilon\sum_{k<n}L^k\). (T2) Without a modulus, no accumulated bound follows. An exact question is not silently replaced by an approximate one.

### Per-file edits

**File 10, line 376. File 11, line 361. File 12, line 371.** The (T2) sentence is identical in all three, so the same edit applies to each:

- **Option A: smallest (a clarification restoring FW5 line 578).**
  - Old: "With one-step discrepancy \(\varepsilon\) and an \(L\)-Lipschitz next-step map, \(e_n\le\ldots\)"
  - New: "With one-step discrepancy \(\varepsilon\), an \(L\)-Lipschitz next-step map and matching initial states (\(e_0=0\)), \(e_n\le\ldots\)"
  - **Gained:** (T2) is true under what the files state; Part XV is no longer triggered; the text matches FW5 and the first sentence of R2 J.
  - **Lost:** nothing that was true. Runs with unequal starts are still not covered (the second sentence of R2 J), but after this edit that is an admitted limit of scope, not a false claim.
- **Option B: recommended (A plus the general bound).** Use the restatement above, or the same text without "at every state of the stated scope" and "represented" if the smallest change is wanted.
  - **Gained:** also covers unequal starts, with a bound that cannot be improved, which settles R2 J's second qualification.
  - **Lost:** nothing. Strictly, it adds a claim, a generalisation that FW5 did not state.
- **Option C: optional hardening.** Add "at every state of the stated scope" and "represented", as in the restatement. This closes the three smaller gaps in §3 by restoring FW5's wording from lines 570 and 572. Nothing is lost.

**File 11's header** (line 5: "One claim changes: Derivation 3 ... Nothing else changes in what is claimed"). Strictly, either option changes what (T2) claims: it narrows the literal statement to its true form, and Option B also generalises it. So the header needs one clause, or an erratum line such as: "Erratum: (T2) regains the matching-start hypothesis \(e_0=0\) that FW5 stated and file 10 dropped [and states the bound with an initial error]." The same erratum wording could be added to file 10 without rewriting it.

**File 12's header** promises only the transport results "in the same names and notation", so it needs no change beyond the (T2) line.

**Part XV** (file 10 line 543, file 11 line 538, file 12 line 556): no edit. Once the hypothesis is written into (T2), "under their stated assumptions" does the protecting correctly.

**File 00:** no edit. Line 578 already carries the hypothesis, and line 1390 is correct as written. Adding the general bound after line 581 is optional and not needed for correctness.

**For the testing record (S78 item 10).** The mathematical question is now settled by proof and counterexample; it does not need a case. What is still missing is on the testing side: S75's "What this does not show" should record that (T2) was settled by this check and not by a case.

---

## 6. Script (run with `python3 -`, not saved elsewhere) and its output

```python
import math, random

def run(S, T, pi, z0, y0, n):
    """Target z_{k+1}=S(z_k); represented y_{k+1}=T(y_k); e_k=|pi(z_k)-y_k|."""
    z, y, es = z0, y0, []
    for k in range(n+1):
        es.append(abs(pi(z)-y))
        z, y = S(z), T(y)
    return es

def T2(eps, L, n):        return eps*sum(L**k for k in range(n))
def corrected(e0, eps, L, n): return L**n*e0 + T2(eps, L, n)

ident = lambda x: x
print("A. Affine family: S(z)=L*z+eps, T(y)=L*y, pi=id.")
print("   one-step discrepancy |S(w)-T(w)| = eps at every w; T exactly L-Lipschitz.")
for L in (2.0, 1.0, 0.5):
    eps, e0 = 0.1, 1.0
    S = lambda z, L=L, eps=eps: L*z+eps
    T = lambda y, L=L: L*y
    print(f"  L={L}, eps={eps}")
    # mismatched start: z0=0, y0=-e0 (errors aligned)
    es = run(S, T, ident, 0.0, -e0, 5)
    for n in range(6):
        b2, bc = T2(eps, L, n), corrected(e0, eps, L, n)
        print(f"    n={n}: e_n={es[n]:.6f}  T2 bound={b2:.6f}  {'VIOLATED' if es[n]>b2+1e-12 else 'ok'}"
              f"  corrected={bc:.6f}  {'ok' if es[n]<=bc+1e-12 else 'VIOLATED'}")
    # matched start: y0 = pi(z0)
    es0 = run(S, T, ident, 0.0, 0.0, 5)
    assert all(es0[n] <= T2(eps, L, n)+1e-12 for n in range(6))
    print(f"    matched start (e0=0): e_n = {[round(e,6) for e in es0]} <= T2 at every n")

print("\nB. Exact dynamics: S=T=identity, eps=0, L=1, e0=1.")
es = run(ident, ident, ident, 0.0, 1.0, 5)
print("   e_n =", es, " T2 bound = 0 for every n  -> violated at every n")

print("\nC. Random nonlinear check: T(y)=L*sin(y) (L-Lipschitz), S(z)=T(z)+eps*cos(3z) (defect<=eps).")
random.seed(1)
viol_T2_mismatch = viol_T2_match = viol_corr = trials = 0
for _ in range(20000):
    L = random.choice([0.3, 0.9, 1.0, 1.5, 2.5]); eps = random.uniform(0, 0.5)
    S = lambda z, L=L, eps=eps: L*math.sin(z)+eps*math.cos(3*z)
    T = lambda y, L=L: L*math.sin(y)
    z0 = random.uniform(-3, 3); e0 = random.uniform(0, 1); y0 = z0 + random.choice([-1, 1])*e0
    n = random.randint(0, 8)
    e_mis = run(S, T, ident, z0, y0, n)[n]
    e_mat = run(S, T, ident, z0, z0, n)[n]
    trials += 1
    viol_T2_mismatch += e_mis > T2(eps, L, n)+1e-9
    viol_T2_match    += e_mat > T2(eps, L, n)+1e-9
    viol_corr        += e_mis > corrected(e0, eps, L, n)+1e-9
print(f"   {trials} runs: T2 violated with unmatched starts: {viol_T2_mismatch};"
      f" T2 violated with matched starts: {viol_T2_match}; corrected bound violated: {viol_corr}")

print("\nD. Side check, error entering BEFORE the map: S(z)=T(z+eps), T(y)=2y, matched start.")
L, eps = 2.0, 0.1
es = run(lambda z: L*(z+eps), lambda y: L*y, ident, 0.0, 0.0, 4)
for n in range(5):
    print(f"   n={n}: e_n={es[n]:.4f}  T2 (eps as input perturbation)={T2(eps,L,n):.4f}"
          f"  T2 (eps := post-map discrepancy L*eps)={T2(L*eps,L,n):.4f}")

print("\nE. Side check, one-step discrepancy bounded only at the start state:")
print("   T(y)=2y, S(z)=2z+0.1+z^2, matched start z0=0: defect at z0 is 0.1, larger later.")
es = run(lambda z: 2*z+0.1+z*z, lambda y: 2*y, ident, 0.0, 0.0, 3)
for n in range(4): print(f"   n={n}: e_n={es[n]:.4f}  T2={T2(0.1,2,n):.4f}")

print("\nF. Side check, Lipschitz constant taken on the TARGET map in the target's own metric:")
print("   pi(z)=z^3, S(z)=2z (2-Lipschitz on R), T(y)=8y+0.1 (defect |pi S z - T pi z| = 0.1), matched start z0=0.")
es = run(lambda z: 2*z, lambda y: 8*y+0.1, lambda z: z**3, 0.0, 0.0, 4)
for n in range(5): print(f"   n={n}: e_n={es[n]:.4f}  T2 with L=2: {T2(0.1,2,n):.4f}  T2 with L=8 (represented map): {T2(0.1,8,n):.4f}")
```

Output:

```
A. Affine family: S(z)=L*z+eps, T(y)=L*y, pi=id.
   one-step discrepancy |S(w)-T(w)| = eps at every w; T exactly L-Lipschitz.
  L=2.0, eps=0.1
    n=0: e_n=1.000000  T2 bound=0.000000  VIOLATED  corrected=1.000000  ok
    n=1: e_n=2.100000  T2 bound=0.100000  VIOLATED  corrected=2.100000  ok
    n=2: e_n=4.300000  T2 bound=0.300000  VIOLATED  corrected=4.300000  ok
    n=3: e_n=8.700000  T2 bound=0.700000  VIOLATED  corrected=8.700000  ok
    n=4: e_n=17.500000  T2 bound=1.500000  VIOLATED  corrected=17.500000  ok
    n=5: e_n=35.100000  T2 bound=3.100000  VIOLATED  corrected=35.100000  ok
    matched start (e0=0): e_n = [0.0, 0.1, 0.3, 0.7, 1.5, 3.1] <= T2 at every n
  L=1.0, eps=0.1
    n=0: e_n=1.000000  T2 bound=0.000000  VIOLATED  corrected=1.000000  ok
    n=1: e_n=1.100000  T2 bound=0.100000  VIOLATED  corrected=1.100000  ok
    n=2: e_n=1.200000  T2 bound=0.200000  VIOLATED  corrected=1.200000  ok
    n=3: e_n=1.300000  T2 bound=0.300000  VIOLATED  corrected=1.300000  ok
    n=4: e_n=1.400000  T2 bound=0.400000  VIOLATED  corrected=1.400000  ok
    n=5: e_n=1.500000  T2 bound=0.500000  VIOLATED  corrected=1.500000  ok
    matched start (e0=0): e_n = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5] <= T2 at every n
  L=0.5, eps=0.1
    n=0: e_n=1.000000  T2 bound=0.000000  VIOLATED  corrected=1.000000  ok
    n=1: e_n=0.600000  T2 bound=0.100000  VIOLATED  corrected=0.600000  ok
    n=2: e_n=0.400000  T2 bound=0.150000  VIOLATED  corrected=0.400000  ok
    n=3: e_n=0.300000  T2 bound=0.175000  VIOLATED  corrected=0.300000  ok
    n=4: e_n=0.250000  T2 bound=0.187500  VIOLATED  corrected=0.250000  ok
    n=5: e_n=0.225000  T2 bound=0.193750  VIOLATED  corrected=0.225000  ok
    matched start (e0=0): e_n = [0.0, 0.1, 0.15, 0.175, 0.1875, 0.19375] <= T2 at every n

B. Exact dynamics: S=T=identity, eps=0, L=1, e0=1.
   e_n = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0]  T2 bound = 0 for every n  -> violated at every n

C. Random nonlinear check: T(y)=L*sin(y) (L-Lipschitz), S(z)=T(z)+eps*cos(3z) (defect<=eps).
   20000 runs: T2 violated with unmatched starts: 5095; T2 violated with matched starts: 0; corrected bound violated: 0

D. Side check, error entering BEFORE the map: S(z)=T(z+eps), T(y)=2y, matched start.
   n=0: e_n=0.0000  T2 (eps as input perturbation)=0.0000  T2 (eps := post-map discrepancy L*eps)=0.0000
   n=1: e_n=0.2000  T2 (eps as input perturbation)=0.1000  T2 (eps := post-map discrepancy L*eps)=0.2000
   n=2: e_n=0.6000  T2 (eps as input perturbation)=0.3000  T2 (eps := post-map discrepancy L*eps)=0.6000
   n=3: e_n=1.4000  T2 (eps as input perturbation)=0.7000  T2 (eps := post-map discrepancy L*eps)=1.4000
   n=4: e_n=3.0000  T2 (eps as input perturbation)=1.5000  T2 (eps := post-map discrepancy L*eps)=3.0000

E. Side check, one-step discrepancy bounded only at the start state:
   T(y)=2y, S(z)=2z+0.1+z^2, matched start z0=0: defect at z0 is 0.1, larger later.
   n=0: e_n=0.0000  T2=0.0000
   n=1: e_n=0.1000  T2=0.1000
   n=2: e_n=0.3100  T2=0.3000
   n=3: e_n=0.8161  T2=0.7000

F. Side check, Lipschitz constant taken on the TARGET map in the target's own metric:
   pi(z)=z^3, S(z)=2z (2-Lipschitz on R), T(y)=8y+0.1 (defect |pi S z - T pi z| = 0.1), matched start z0=0.
   n=0: e_n=0.0000  T2 with L=2: 0.0000  T2 with L=8 (represented map): 0.0000
   n=1: e_n=0.1000  T2 with L=2: 0.1000  T2 with L=8 (represented map): 0.1000
   n=2: e_n=0.9000  T2 with L=2: 0.3000  T2 with L=8 (represented map): 0.9000
   n=3: e_n=7.3000  T2 with L=2: 0.7000  T2 with L=8 (represented map): 7.3000
   n=4: e_n=58.5000  T2 with L=2: 1.5000  T2 with L=8 (represented map): 58.5000
```

The small gaps (for example 0.31 against 0.3 in part E) are real, not rounding. The comparison tolerances are 1e-12 and 1e-9, far below the gaps shown.

---

## What this check does not show

- It does not say which reading of e_n the author intended. The position of (T2) after functional transport suggests reading M, under which (T2) is true. The verdict rests on the fact that no line of files 10 to 12 states that reading, together with the n = 0 case of the formula.
- It does not test any case or verdict that depends on approximate transport, because none exists in files 10 to 12.
- It was checked against the repository at commit 2788a77. No authority file was edited.
