# S109 Part B round 1, section B1: the in-scope variants as switchable readings in the B1 copy (rule 5).
# Run once on a fresh copy of `model after round 4`; each replacement must match exactly once.
import os, sys
M = os.path.join(sys.argv[1], "model")


def rep(fn, old, new):
    p = os.path.join(M, fn)
    s = open(p, encoding="utf-8").read()
    assert s.count(old) == 1, (fn, old[:60], s.count(old))
    open(p, "w", encoding="utf-8").write(s.replace(old, new))


rep("core.py", "import itertools\n", '''import itertools
import os as _os_s109

# ---- S109 Part B round 1, section B1 (this copy only; rule 5 of the S109 Part B reading rule) ----------------------
# Each in-scope variant of section B1 is a switchable reading; "none" is the definition after round 4 (the default).
#   PB1.1  D3.5 (V1.7): Excl(Σ) := (A×B)∖C, so Stated(C,Σ) holds of every question (NonVacuous's second conjunct vacuous)
#   PB1.2  D3.1 (R2V1.9): a contract holding an edit Θ does not admit names no question [S109-B1-I1: Θ_admits of a bare
#          edit, which the program never computes: S109B_THETA "all" (Θ admits every edit, the program's worlds),
#          "strict" (Θ admits the identity only, the reading on which a mathematical target's edits are not admitted),
#          or a case's own D.meta["theta_excludes"]]
#   PB1.3  D3.2 (R2V1.8): Y_p := X_δD; a query with an answer on C outside X_δD ∪ {⊥} names no question
#   PB1.4  D4.2 (R2V1.7): j ~_C j′ :⟺ V_j = V_j′ as ordered tuples (same port names, same domains) ∧ sig equal (β dropped)
#   PB1.5  L155.s6 with D3.4 (R2V1.4): Found(p) :⟺ ρ_p ∈ {selected, constructed} (found(); read by no claim)
#   PB1.6  D1.3: a deleted component imposes the empty relation (Org.L); D6.1 and D7.1 read the same deletion
#   PB1.7  D3.1 (L141.s2): a question's contract holds an edit other than 1
#   PB1.8  D4.1 (L115.s1): sig⁺_C(j) adds Sol_D(a,b)|V_j to each entry
#   PB1.9  L113.s1 with D4.1-D4.4: kinds read on A×B (every pair both transports translate), not on C
# S109B_VARIANT in the environment sets it for a whole-suite run; the case scripts set core.S109B directly.
S109B_VARIANTS = ("none", "PB1.1", "PB1.2", "PB1.3", "PB1.4", "PB1.5", "PB1.6", "PB1.7", "PB1.8", "PB1.9")
S109B = _os_s109.environ.get("S109B_VARIANT", "none")
assert S109B in S109B_VARIANTS
S109B_THETA = _os_s109.environ.get("S109B_THETA", "all")
assert S109B_THETA in ("all", "strict")
''')

# PB1.6: deletion
rep("core.py", '''    def L(self, j, a, b):
        if j in self.deleted:
            return self.full(j)''', '''    def L(self, j, a, b):
        if j in self.deleted:
            return frozenset() if S109B == "PB1.6" else self.full(j)''')

# PB1.8, PB1.9: signatures
rep("core.py", '''    if through is None:
        return {(a, b): org.L(j, a, b) for (a, b) in C}
    tau, sigma = through
    return {(a, b): org.L(j, tau[a], sigma[b]) for (a, b) in C}''', '''    if S109B == "PB1.8":  # sig⁺: the relation and the values j's ports take in the solutions
        def ent(a2, b2):
            return (org.L(j, a2, b2), org.proj(org.sol(a2, b2), org.ports, org.foot[j]))
    else:
        def ent(a2, b2):
            return org.L(j, a2, b2)
    if through is None:
        return {(a, b): ent(a, b) for (a, b) in C}
    tau, sigma = through
    return {(a, b): ent(tau[a], sigma[b]) for (a, b) in C}''')
rep("core.py", '''def one_kind(org1, j1, org2, j2, C, t1=None, t2=None, witness=False):
    s1, s2 = sig_fn(org1, j1, C, t1), sig_fn(org2, j2, C, t2)''', '''def one_kind(org1, j1, org2, j2, C, t1=None, t2=None, witness=False):
    if S109B == "PB1.9":  # kinds on the level's whole edit set: every pair (of D) both readings reach [S109-B1-I3]
        if t1 is None and t2 is None:
            C = [(a, b) for a in org1.A for b in org1.B if (a, b) in set((x, y) for x in org2.A for y in org2.B)]
        else:
            ta, sa = (t1 if t1 is not None else ({a: a for a in org1.A}, {b: b for b in org1.B}))
            tb, sb = (t2 if t2 is not None else ({a: a for a in org2.A}, {b: b for b in org2.B}))
            C = [(a, b) for a in ta if a in tb for b in sa if b in sb]
    s1, s2 = sig_fn(org1, j1, C, t1), sig_fn(org2, j2, C, t2)''')
rep("core.py", '''    for perm in footprint_bijections(org1, j1, org2, j2):
        if all(rename_rel(s1[x], perm) == s2[x] for x in C):''', '''    for perm in footprint_bijections(org1, j1, org2, j2):
        if S109B == "PB1.8":
            if all(rename_rel(s1[x][0], perm) == s2[x][0] and rename_rel(s1[x][1], perm) == s2[x][1] for x in C):
                return perm if witness else True
            continue
        if all(rename_rel(s1[x], perm) == s2[x] for x in C):''')
# PB1.4: no β
rep("core.py", '''    f1, f2 = org1.foot[j1], org2.foot[j2]
    if len(f1) != len(f2):
        return''', '''    f1, f2 = org1.foot[j1], org2.foot[j2]
    if len(f1) != len(f2):
        return
    if S109B == "PB1.4":  # β dropped: the same ordered footprint (names and domains), the identity only
        if tuple(f1) == tuple(f2) and all(set(org1.dom[f1[i]]) == set(org2.dom[f2[i]]) for i in range(len(f1))):
            yield tuple(range(len(f1)))
        return''')
# PB1.1: Stated always
rep("core.py", '''    allpairs = frozenset((a, b) for a in p.D.A for b in p.D.B)
    return bool(p.D.sol(ONE, p.b0)) and (allpairs - p.C) <= p.excl''', '''    allpairs = frozenset((a, b) for a in p.D.A for b in p.D.B)
    if S109B == "PB1.1":  # Excl(Σ) := (A×B)∖C: Stated(C, Σ) holds of every question
        return bool(p.D.sol(ONE, p.b0))
    return bool(p.D.sol(ONE, p.b0)) and (allpairs - p.C) <= p.excl''')
# PB1.2, PB1.3, PB1.7: whether p is a question
rep("core.py", '''    keys = ("F1", "F2", "A", "NC1", "NC2", "NonVacuous") if reading == "r3" else ("F1", "F2", "A", "Dep", "NonVacuous")
    val = all(d[k] for k in keys)''', '''    keys = ("F1", "F2", "A", "NC1", "NC2", "NonVacuous") if reading == "r3" else ("F1", "F2", "A", "Dep", "NonVacuous")
    val = all(d[k] for k in keys)
    if S109B in ("PB1.2", "PB1.3", "PB1.7"):  # S109 B1: p a question (D3.1, D3.2 varied)
        d["question"] = is_question(cand.p)
        val = val and d["question"]''')
rep("core.py", '''# ---- S106: a pin (D6.3''', '''def theta_admits(D, a):
    """S109 B1, PB1.2 [S109-B1-I1]: whether Θ admits the bare edit a of D. "all": every edit; "strict": the identity only;
    a case may name edits Θ excludes in D.meta["theta_excludes"]."""
    if a in D.meta.get("theta_excludes", ()):
        return False
    return S109B_THETA == "all" or a == ONE


def is_question(p):
    """S109 B1: whether p names a question under the section's variant (every p does under 'none')."""
    if S109B == "PB1.2":
        return all(theta_admits(p.D, a) for (a, b) in p.C)
    if S109B == "PB1.3":  # Y_p := X_δD [S109-B1-I2: checked at the pairs of C]
        if not isinstance(p.deltaD, str) or p.deltaD not in p.D.dom:
            return False
        X = set(p.D.dom[p.deltaD])
        return all((y is BOT) or (y in X) for y in (p.ans(a, b) for (a, b) in p.C))
    if S109B == "PB1.7":
        return any(a != ONE for (a, b) in p.C)
    return True


def found(p, rho=None):
    """S109 B1, PB1.5 (L155.s6 with D3.4): Found(p). After round 4: ρ_p = constructed; PB1.5: selected or constructed.
    The program records no ρ_p (None read as declared, S108-1-I5); no claim reads Found."""
    r = rho if rho is not None else (getattr(p, "rho", None) or "declared")
    return r in (("selected", "constructed") if S109B == "PB1.5" else ("constructed",))


# ---- S106: a pin (D6.3''')
print("B1 patched")
