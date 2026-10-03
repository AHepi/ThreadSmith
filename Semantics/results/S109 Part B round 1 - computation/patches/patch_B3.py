# S109 Part B round 1, section B3: the in-scope variants as switchable readings in the B3 copy (rule 5).
import os, sys
M = os.path.join(sys.argv[1], "model")


def rep(fn, old, new):
    p = os.path.join(M, fn)
    s = open(p, encoding="utf-8").read()
    assert s.count(old) == 1, (fn, old[:60], s.count(old))
    open(p, "w", encoding="utf-8").write(s.replace(old, new))


rep("core.py", "import itertools\n", '''import itertools
import os as _os_s109

# ---- S109 Part B round 1, section B3 (this copy only; rule 5 of the S109 Part B reading rule) ----------------------
#   PB3.1  D12.4 (R2V2.4): a holding reached by a copy of a carrier's whole content inherits its provenance whole: the
#          student's copy (FC30.new1 (d), (f)) read as such a copy (rec_of = the source) [S109-B3-I1: only holdings the
#          case names as copies; the program's other chains name none]
#   PB3.2  D12.5: Rep := Held; Sel's exclusion reads Held at o′ ≺ o (prov reading T′ becomes T in Sel's exclusion)
#   PB3.3  L195.s1, s5 with D12.1: Sel also asks C ∩ Occ(h) ⊆ H (every pair of C that occurred in h lies in H)
#   PB3.4  L199.s1, s3 with D12.3: provenance read on h∪(t): on a chain, every held holding of t takes Sel (Con) when some
#          holding of t has it [S109-B3-I2: every held holding of a chain holds the one transport t]
#   PB3.5  D11.5: Occurs(a,b,ξ) := a admitted at ξ ∧ b actual at ξ: Sel's H-clause reads the history's admission
#          [S109-B3-I3: every boundary of H actual]
#   PB3.6  D11.1: occurrences only inside the declared boundary β: the student's copy with the textbook's carrier outside
#          β (on that reading) is a chain of one holding
#   PB3.7  D13.4: d ≡_ℓ c :⟺ equal answers (port query on the first port) at every pair of C_c
S109B_VARIANTS = ("none", "PB3.1", "PB3.2", "PB3.3", "PB3.4", "PB3.5", "PB3.6", "PB3.7")
S109B = _os_s109.environ.get("S109B_VARIANT", "none")
assert S109B in S109B_VARIANTS
''')
rep("claims_b.py", '''    if not set(H) <= set(cand.p.C) or not set(H) <= h.occurs:
        return False''', '''    from . import core as _c
    if not set(H) <= set(cand.p.C):
        return False
    if _c.S109B == "PB3.5":  # S109 B3: occurrence := admission (and every boundary of H actual) [S109-B3-I3]
        if not h.admitted:
            return False
    elif not set(H) <= h.occurs:
        return False
    if _c.S109B == "PB3.3" and not (set(cand.p.C) & set(h.occurs)) <= set(H):  # S109 B3: every occurred pair of C in H
        return False''')
rep("claims_b.py", '''        else:
            s_ = selc[o] and not any(x in R for x in before)
        if i161:
            s_ = s_ and not trace[o]
        out[o] = (bool(s_), bool(c_))
    return out''', '''        else:
            from . import core as _c
            if _c.S109B == "PB3.2":  # S109 B3: Rep := Held, so Sel's exclusion reads Held at o′ ≺ o
                s_ = selc[o] and not any(held[x] for x in before)
            else:
                s_ = selc[o] and not any(x in R for x in before)
        if i161:
            s_ = s_ and not trace[o]
        out[o] = (bool(s_), bool(c_))
    from . import core as _c
    if _c.S109B == "PB3.4":  # S109 B3: provenance on h∪(t): a value some held holding of t has, every held holding has
        hs = [o for o in range(n) if held[o]]
        s_any = any(out[o][0] for o in hs)
        c_any = any(out[o][1] for o in hs)
        for o in hs:
            out[o] = (s_any, c_any)
    return out''')
rep("claims_b.py", '''    def equiv(d, c):
        """d ≡ c (D13.4, I48): t: E_d → E_c faithful on the preimage of C_c, t': E_c → E_d faithful on C_c."""
        (Ed, Cd), (Ec, Cc) = d, c''', '''    def equiv(d, c):
        """d ≡ c (D13.4, I48): t: E_d → E_c faithful on the preimage of C_c, t': E_c → E_d faithful on C_c.
        S109 B3, PB3.7: equal answers of the port query on the first port at every pair of C_c."""
        (Ed, Cd), (Ec, Cc) = d, c
        from . import core as _c
        if _c.S109B == "PB3.7":
            if Ed.ports[0] != Ec.ports[0]:
                return False
            Q = PortQuery()
            return all(a in Ed.A and b in Ed.B and Q(Ed, a, b, Ed.ports[0]) == Q(Ec, a, b, Ec.ports[0]) for (a, b) in Cc)''')
# the student's copy, FC30.new1 (d) and (f)
rep("claims_s41.py", '''        for rd in ("U", "K", "T", "T'"):
            fps = prov_fixed_points(2, [1, held_o], [1, 0], [0, selc_o], rd, True)
            decs = [not sc[1][0] and not sc[1][1] for R, sc in fps]''', '''        for rd in ("U", "K", "T", "T'"):
            from . import core as _c
            if _c.S109B == "PB3.6":  # S109 B3: the textbook's carrier outside β: a chain of the student's holding alone
                fps = prov_fixed_points(1, [held_o], [0], [selc_o], rd, True)
                decs = [not sc[0][0] and not sc[0][1] for R, sc in fps]
            else:
                fps = prov_fixed_points(2, [1, held_o], [1, 0], [0, selc_o], rd, True, rec_of=([None, 0] if _c.S109B == "PB3.1" else None))
                decs = [not sc[1][0] and not sc[1][1] for R, sc in fps]''')
rep("claims_s41.py", '''            rows.append("%s, %s: fixed points %s; Dec(t) at o2 %s; Def(L17, S41) %s" % (lab, rd, prov_show(2, fps), decs, [suff_defeats(acc, d, out, "L17 (S41)") for d in decs]))''', '''            rows.append("%s, %s: fixed points %s; Dec(t) at o2 %s; Def(L17, S41) %s" % (lab, rd, prov_show(1 if _c.S109B == "PB3.6" else 2, fps), decs, [suff_defeats(acc, d, out, "L17 (S41)") for d in decs]))''')
rep("claims_s41.py", '''        for lab, rof in (("D12.4 (component with its binding: the binding declared, not transferred)", None), ("K3's reading (the component alone, transferred)", 0)):''', '''        from . import core as _c
        for lab, rof in (("D12.4 (component with its binding: the binding declared, not transferred)", 0 if _c.S109B == "PB3.1" else None), ("K3's reading (the component alone, transferred)", 0)):''')
print("B3 patched")
