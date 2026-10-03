# S109 Part B round 1, section B2: the in-scope variants as switchable readings in the B2 copy (rule 5).
import os, sys
M = os.path.join(sys.argv[1], "model")


def rep(fn, old, new):
    p = os.path.join(M, fn)
    s = open(p, encoding="utf-8").read()
    assert s.count(old) == 1, (fn, old[:60], s.count(old))
    open(p, "w", encoding="utf-8").write(s.replace(old, new))


rep("core.py", "import itertools\n", '''import itertools
import os as _os_s109

# ---- S109 Part B round 1, section B2 (this copy only; rule 5 of the S109 Part B reading rule) ----------------------
#   PB2.1  L189.s2 with D5.7, D12.7 (R2V2.7): Faithful_C := F1 ∧ F2 ∧ A; Faithful_H and Viol read (A) at the pairs too
#   PB2.2  D5.5: F2 := F2eq (Hom dropped; Faithful_H drops it too)
#   PB2.3  D5.4: (F1) over every component of E; a component with no counterpart (not in λ) fails it [S109-B2-I1]
#   PB2.4  D5.6: (A) over Det_C only (a pair where the target's answer is ⊥ asks nothing)
#   PB2.5  D6.2: NC0 := no background component (k ∉ Γ) pins δ_E to Ans_p at a pair of C [S109-B2-I2: S109B_NC0 "bg" any
#          background component; "bg-input" only one that assigns an input port of E (Roles(E).asg of a port with Set_v ≠ ∅)]
#   PB2.6  D6.6: NonVacuous := Sol_D(1,b0) ≠ ∅ (Stated leaves (E))
#   PB2.7  D5.6 reads D6.3: (A) := (A) ∧ NC1 (Slot's quantifier as S105_SLOT_QUANTIFIER gives, 'every' by default)
#   PB2.8  D7.3: a critical block is finite (every block of a finite Γ is; FC40's infinitary blocks: the case script)
#   PB2.9  D5.1: π total (the program's π is total already, I81: no code changes)
S109B_VARIANTS = ("none", "PB2.1", "PB2.2", "PB2.3", "PB2.4", "PB2.5", "PB2.6", "PB2.7", "PB2.8", "PB2.9")
S109B = _os_s109.environ.get("S109B_VARIANT", "none")
assert S109B in S109B_VARIANTS
S109B_NC0 = _os_s109.environ.get("S109B_NC0", "bg")
assert S109B_NC0 in ("bg", "bg-input")
''')
rep("core.py", '''    E = cand.E
    for k in cand.Gamma:
        if proj_lam(cand, k, D, a, b) != E.L(k, cand.tau[a], cand.sigma[b]):
            return False
    return True''', '''    E = cand.E
    for k in (E.comps if S109B == "PB2.3" else cand.Gamma):
        if S109B == "PB2.3" and k not in cand.lam:
            return False  # [S109-B2-I1] a background component with no counterpart
        if proj_lam(cand, k, D, a, b) != E.L(k, cand.tau[a], cand.sigma[b]):
            return False
    return True''')
rep("core.py", '''def A_at(cand, a, b, D=None):
    return cand.ans_E(cand.tau[a], cand.sigma[b]) == cand.p.ans(a, b, D)''', '''def A_at(cand, a, b, D=None):
    y = cand.p.ans(a, b, D)
    if S109B == "PB2.4" and y is BOT:
        return True
    return cand.ans_E(cand.tau[a], cand.sigma[b]) == y''')
rep("core.py", '''def F2(cand):
    return F2eq(cand) and hom(cand)


def A(cand):
    return translated_C(cand) and all(A_at(cand, a, b) for (a, b) in cand.p.C)


def faithful(cand):
    """Faithful_C (D5.7, I49): the narrow extent."""
    return F1(cand) and F2(cand)''', '''def F2(cand):
    if S109B == "PB2.2":
        return F2eq(cand)
    return F2eq(cand) and hom(cand)


def A(cand):
    ok = translated_C(cand) and all(A_at(cand, a, b) for (a, b) in cand.p.C)
    if S109B == "PB2.7":
        return ok and NC1(cand)
    return ok


def faithful(cand):
    """Faithful_C (D5.7, I49): the narrow extent. S109 B2, PB2.1: the wide extent, (A) inside."""
    if S109B == "PB2.1":
        return F1(cand) and F2(cand) and A(cand)
    return F1(cand) and F2(cand)''')
rep("core.py", '''def dep(cand):''', '''def NC0(cand):
    """D6.2. After round 4: holds of every candidate (I23). S109 B2, PB2.5 (I23's other choice (a)): no background
    component of E pins δ_E to the target's answer at a pair of C [S109-B2-I2]."""
    if S109B != "PB2.5":
        return True
    bg = [k for k in cand.E.comps if k not in cand.Gamma]
    if S109B_NC0 == "bg-input":
        R = Roles(cand.E)
        ins = set(R.asg[v] for v in cand.E.ports if v in R.asg and R.input(v))
        bg = [k for k in bg if k in ins]
    return not any(pin(cand, k, a, b) for k in bg for (a, b) in cand.p.C)


def dep(cand):''')
rep("core.py", '''    candidate (D6.2, I23), so Dep is NC2: some contrast of E's answers at a pair of C is lost when a nonempty
    block of Γ is deleted (D6.4)."""
    return bool(NC2(cand))''', '''    candidate (D6.2, I23), so Dep is NC2: some contrast of E's answers at a pair of C is lost when a nonempty
    block of Γ is deleted (D6.4)."""
    if S109B == "PB2.5":
        return NC0(cand) and bool(NC2(cand))
    return bool(NC2(cand))''')
rep("core.py", '''    allpairs = frozenset((a, b) for a in p.D.A for b in p.D.B)
    return bool(p.D.sol(ONE, p.b0)) and (allpairs - p.C) <= p.excl''', '''    allpairs = frozenset((a, b) for a in p.D.A for b in p.D.B)
    if S109B == "PB2.6":
        return bool(p.D.sol(ONE, p.b0))
    return bool(p.D.sol(ONE, p.b0)) and (allpairs - p.C) <= p.excl''')
# account's detail: F2 and A as the variant reads them; Dep with NC0
rep("core.py", '''        d["F2"] = d["F2eq"] and d["Hom"]
        d["A"] = A(cand)
        d["NC1"] = NC1(cand)
        d["NC2"] = NC2(cand)
        d["Dep"] = bool(d["NC2"])''', '''        d["F2"] = d["F2eq"] and (d["Hom"] or S109B == "PB2.2")
        d["A"] = A(cand)
        d["NC1"] = NC1(cand)
        d["NC2"] = NC2(cand)
        d["NC0"] = NC0(cand)
        d["Dep"] = bool(d["NC2"]) and d["NC0"]''')
rep("core.py", '''def critical_block(S, B, W):
    return bool(B) and B <= W and W in S and (W - B) not in S''', '''def critical_block(S, B, W):
    # S109 B2, PB2.8: |B| < ∞; every B here is a finite set, so the clause is idle on finite Γ
    return bool(B) and B <= W and W in S and (W - B) not in S''')
# claims_b: Viol and Faithful_H read (A) under PB2.1; Faithful_H drops Hom under PB2.2
rep("claims_b.py", '''    return all(cand.translates(*x) and F1_at(cand, *x) and F2eq_at(cand, *x) for x in H) and hom(cand)''', '''    from . import core as _c
    if _c.S109B == "PB2.1":  # S109 B2, PB2.1: Faithful_H with (A) at the pairs of H
        return all(cand.translates(*x) and F1_at(cand, *x) and F2eq_at(cand, *x) and A_at(cand, *x) for x in H) and hom(cand)
    if _c.S109B == "PB2.2":  # S109 B2, PB2.2: Hom dropped
        return all(cand.translates(*x) and F1_at(cand, *x) and F2eq_at(cand, *x) for x in H)
    return all(cand.translates(*x) and F1_at(cand, *x) and F2eq_at(cand, *x) for x in H) and hom(cand)''')
rep("claims_b.py", '''    """Viol(t; a,b) (D12.7, I50 narrow): (F1) or the valuation equation of (F2) fails at (a,b)."""
    return not (F1_at(cand, a, b) and F2eq_at(cand, a, b))''', '''    """Viol(t; a,b) (D12.7, I50 narrow): (F1) or the valuation equation of (F2) fails at (a,b). S109 B2, PB2.1: Viol⁺."""
    from . import core as _c
    if _c.S109B == "PB2.1":
        return not (F1_at(cand, a, b) and F2eq_at(cand, a, b) and A_at(cand, a, b))
    return not (F1_at(cand, a, b) and F2eq_at(cand, a, b))''')
print("B2 patched")
