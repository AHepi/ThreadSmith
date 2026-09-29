# S109 Part B round 1, section B4: the in-scope variants as switchable readings in the B4 copy (rule 5).
import os, sys
M = os.path.join(sys.argv[1], "model")


def rep(fn, old, new):
    p = os.path.join(M, fn)
    s = open(p, encoding="utf-8").read()
    assert s.count(old) == 1, (fn, old[:60], s.count(old))
    open(p, "w", encoding="utf-8").write(s.replace(old, new))


rep("core.py", "import itertools\n", '''import itertools
import os as _os_s109

# ---- S109 Part B round 1, section B4 (this copy only; rule 5 of the S109 Part B reading rule) ----------------------
#   PB4.1   L315.s7 with D9.8 (V2.8's part): ruled out only by an argument that uses the claim: X_j(φ) keeps α only where
#           every atom of φ is among α's leaves' atoms [S109-B4-I1: 'reads its meeting (E)' read on the program's formulas;
#           the defeat sets' φ (an Expl_ atom) keep D16.XV's reading]
#   PB4.2   D9.5: Scope_j(u) := C_u ⊆ C_j(u) (grain and boundary dropped)
#   PB4.3   D9.3: Prem(u) := the premises Form(u) uses (every form_ok pattern uses all its children: no code changes)
#   PB4.4'  L397.s13 restated on D9.8 (the tabulation's flag: PB4.4 as written changes D9.4, D9.6, FROZEN): X_j(φ) keeps
#           α only where every premise of α taken as given has a held explanation; the program holds none [S109-B4-I2:
#           S109B_HELD "all" every accepted leaf; "no-records" record leaves exempt]
#   PB4.5   L383.s1 with D9.10: a criticism occurrence has bearing (FC74, FC76)
#   PB4.6   L385.s1, D9.11: UsesReason without the active-route clause (FC76; the idle-route case in the case script)
#   PB4.7   L546.s1: Arguments 1-10 in the list (FC109 reruns FC81, FC95-FC103 beside its eight)
#   PB4.8   D10.1 with L317.s1: Prob(ℰ,ℰ′;p) :⟺ Riv (the assessor dropped) (FC47.new1, FC72.new2)
S109B_VARIANTS = ("none", "PB4.1", "PB4.2", "PB4.3", "PB4.4'", "PB4.5", "PB4.6", "PB4.7", "PB4.8")
S109B = _os_s109.environ.get("S109B_VARIANT", "none")
assert S109B in S109B_VARIANTS
S109B_HELD = _os_s109.environ.get("S109B_HELD", "all")
assert S109B_HELD in ("all", "no-records")
''')
rep("args.py", '''        return cok and lu == lj and bu == bj''', '''        from . import core as _c
        if _c.S109B == "PB4.2":  # S109 B4: Scope_j reads the contract only
            return cok
        return cok and lu == lj and bu == bj''')
rep("args.py", '''    """X_j(φ) over a finite set of arguments [I88]."""
    return [a for a in args if usable(j, a) and rules_out(a, phi)]''', '''    """X_j(φ) over a finite set of arguments [I88]."""
    out = [a for a in args if usable(j, a) and rules_out(a, phi)]
    from . import core as _c
    if _c.S109B == "PB4.1" and not any(str(x).startswith("Expl_") for x in atoms(phi)):
        out = [a for a in out if set(atoms(phi)) <= set().union(*[atoms(l.claim) for l in a.leaves()])]
    if _c.S109B == "PB4.4'":  # no one holds a represented explanation of a premise taken as given
        out = [a for a in out if not any(canon(l.claim) in j.accepted and (_c.S109B_HELD == "all" or l.kind != "record") for l in a.leaves())]
    return out''')
rep("claims_b.py", '''    def check(m):
        p, c = m
        if not account(c):
            return ("the connection's candidate fails (E) on p_δ = Qf(z, δ, p); a represented premise g (L383) is a datum of the occurrence, "''', '''    def check(m):
        p, c = m
        if core.S109B == "PB4.5":  # S109 B4: a criticism occurrence has bearing, so none with ¬Acc occurs
            return None
        if not account(c):
            return ("the connection's candidate fails (E) on p_δ = Qf(z, δ, p); a represented premise g (L383) is a datum of the occurrence, "''')
rep("claims_b.py", '''    ok = route_ok and rec_ok and chg_ok and not account(c)''', '''    ok = (route_ok or core.S109B == "PB4.6") and rec_ok and chg_ok and not account(c)
    if core.S109B == "PB4.5":  # S109 B4: no criticism occurrence without bearing, so the case has no criticism in it
        ok = False''')
rep("claims_b.py", '''    named = ["FC37", "FC57", "FC61", "FC66", "FC92", "FC17", "FC96", "FC80"]''', '''    named = ["FC37", "FC57", "FC61", "FC66", "FC92", "FC17", "FC96", "FC80"]
    if core.S109B == "PB4.7":  # S109 B4: Arguments 4-10 added to L546's list
        named = named + [x for x in ["FC81", "FC95", "FC97", "FC98", "FC99", "FC100", "FC101", "FC102", "FC103"] if x not in named]''')
rep("claims_r3a2.py", '''        prob = riv and bool(cps) and not out_bad and not out_good''', '''        from . import core as _c
        prob = riv and bool(cps) and ((not out_bad and not out_good) or _c.S109B == "PB4.8")''')
rep("claims_r4a3.py", '''    prob = {nm: rb["ℰ_myth1"][1] and not o[0] and not o[1] for nm, o in (("j0", out0), ("j1", out1))}''', '''    from . import core as _c
    prob = {nm: rb["ℰ_myth1"][1] and ((not o[0] and not o[1]) or _c.S109B == "PB4.8") for nm, o in (("j0", out0), ("j1", out1))}''')
print("B4 patched")
