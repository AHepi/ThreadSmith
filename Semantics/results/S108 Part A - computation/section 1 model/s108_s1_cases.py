# S108 Part A, section 1: the worked cases and the reply's small cases, each section-1 variant off and on.
#   PYTHONHASHSEED=0 python3 -B s108_s1_cases.py
# For every worked case the program builds (the cases of the written-in step's script, s106_cases.py, rebuilt here, and
# the student's declared copy of FC30.new1 (d)): Acc(ℰ) with its conjuncts, and Account ∧ ¬Dec(t) with t's history set
# by hand three ways (Θ by hand, I90; claims_s41.provenance_of: 'Dec' no selection and no trace; 'Con' a trace and cod t
# represented; 'Sel' a selection history on H = {(1, b0)}), under the definition after round 4 ('none') and under each
# in-scope variant of section 1 (core.S108_S1_VARIANTS). A row is printed for a variant only where something differs from
# 'none'. Then the reply's own small cases (V1.1 … V1.8) and the baseline side of the two flagged variants' cases.
# FC-E1 to FC-E5 (s104_external.py), CT1 to CT8 (s104_creative_transport.py) and s106_cases.py itself are run under
# S108_S1_VARIANT and compared with their output under 'none' (see the md). Standard library only; writes nothing.
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from model import core  # noqa: E402
from model.core import (ONE, BOT, Org, Question, PortQuery, Candidate, Translation, account, Roles, F1_at, F2eq_at,  # noqa: E402
                        faithful, proj_lam, ident_contract)
from model.cases import pole, pole_fwd_candidate, pole_rev_candidate, single_settings, fibre_query, COT  # noqa: E402
from model.claims_a import pole_contracts, table_candidate, area2_lookups, _org, _T  # noqa: E402
from model.claims_r3a2 import m5, m13, elim  # noqa: E402
from model.claims_b import e8_contract_org, e6_parts, prov_fixed_points, prov_show, faithful_on  # noqa: E402
from model.claims_s106 import sign_question, sign_two, sign_one, sign_mech  # noqa: E402
from model.claims_s41 import provenance_of  # noqa: E402
from model import e9  # noqa: E402

VARIANTS = [v for v in core.S108_S1_VARIANTS if v != "none"]


def set_variant(v):
    core.S108_S1 = v
    core.OBS_READING = "R-i" if v == "V1.3" else "R-ii"


def tf(x):
    return "T" if x else "F"


def evaluate(c):
    """Acc with conjuncts; (Sel, Con, Dec) and Expl := Acc ∧ ¬Dec for each hand-set history."""
    acc, d = account(c, detail=True)
    H = [(ONE, c.p.b0)]
    prov = {}
    for kind in ("Dec", "Con", "Sel"):
        s, k, dec = provenance_of(c, kind, H)
        prov[kind] = (s, k, dec, bool(acc and not dec))
    keys = [k for k in ("F1", "F2", "A", "Dep", "NonVacuous") if k in d]
    if d.get("question") is False:  # V1.5 only: p is no question (its contract declared)
        keys.append("question")
    return dict(acc=bool(acc), conj={k: bool(d[k]) for k in keys}, prov=prov)


def show(e):
    conj = " ".join("%s %s" % (k, tf(v)) for k, v in e["conj"].items())
    pv = "; ".join("%s-history: Sel %s Con %s Dec %s Expl %s" % (kind, tf(s), tf(k), tf(dec), tf(ex)) for kind, (s, k, dec, ex) in e["prov"].items())
    return "Acc %s [%s] | %s" % (tf(e["acc"]), conj, pv)


def worked_cases():
    """The cases of s106_cases.py, rebuilt as that script builds them (labels unchanged)."""
    out = []
    D = pole()
    C1, C2, C2s = pole_contracts(D)
    C3 = frozenset([(ONE, "b1_45")] + [(a, "b1_45") for a in single_settings(D, ["L"])])
    for nm, C in (("C1", C1), ("C2", C2), ("C3", C3)):
        p = Question(D, C, "b1_45", PortQuery(), "L", name=nm)
        out.append(("E1 pole, forward organization, %s" % nm, pole_fwd_candidate(p)))
    p1 = Question(D, C1, "b1_45", PortQuery(), "L", name="p_prod")
    r = pole_rev_candidate(p1)
    out.append(("E1 pole, reversed calculation, production C1", r))
    inv = D.meta["inv"]
    lab = {v: k for k, v in inv.items()}

    def tau2(a):
        sm = dict(inv[a])
        if not sm:
            return ONE
        t = sm.get("T", 45)
        new = {}
        if "T" in sm:
            new["T"] = t
        if "L" in sm:
            new["L"] = sm["L"]
        elif "H" in sm or "T" in sm:
            new["L"] = sm.get("H", 1) * COT[t]
        if "H" in sm and "L" in sm:
            new["H"] = sm["H"]
        return lab.get(tuple(sorted(new.items())))
    t2 = {a: tau2(a) for a in D.A}
    out.append(("E1 pole, reversed calculation under Mimo's τ', C1", r.replace(tau={a: x for a, x in t2.items() if x is not None}, name="ℰ_rev τ'")))
    CH = frozenset([(ONE, "b1_45")] + [(a, "b1_45") for a in single_settings(D, ["H"])])
    pH = Question(D, CH, "b1_45", PortQuery(), "L", name="C_H")
    rH = pole_rev_candidate(pH)
    out.append(("E1 pole, reversed calculation under Mimo's τ', H only", rH.replace(tau={a: t2[a] for a in sorted(set(x for x, _ in CH), key=repr)}, name="ℰ_rev τ' (H only)")))
    Did = pole(bounds=[(1, 45), (2, 45), (3, 45)])
    pid = Question(Did, frozenset((ONE, b) for b in Did.B), "b1_45", fibre_query(), ("H", "T", "L"), name="p_ident")
    out.append(("E1 pole, reversed calculation, identification C_id", pole_rev_candidate(pid, delta=("H", "T", "L"))))
    for nm, C in (("C1", C1), ("C2", C2)):
        p = Question(D, C, "b1_45", PortQuery(), "L", name=nm)
        out.append(("L269 table of observed answers E_tab, pole %s" % nm, table_candidate(p, list(D.ports))))
        out.append(("L269 encoding table E_enc, pole %s" % nm, table_candidate(p, list(D.ports), encode=True)))
    p = Question(D, C1, "b1_45", PortQuery(), "L", name="C1")
    tab = {(a, b): (frozenset([(p.ans(a, b),)]) if p.ans(a, b) is not BOT else frozenset((x,) for x in D.dom["L"])) for a in D.A for b in D.B}
    E = Org("E_lk", ["L"], {"L": D.dom["L"]}, ["k"], {"k": ("L",)}, D.B, D.A, D._compose, lambda j, a, b: tab[(a, b)])
    out.append(("L273 'p because p': the pole's L written in, C1", Candidate(E, p, {"L": Translation(("L",))}, {a: a for a in D.A}, {b: b for b in D.B},
                                                                             {"k": (frozenset(D.comps), {"L": Translation(("L",))})}, ["k"], "L", name="ℰ_lk")))
    D6 = Org("D", ["y"], {"y": (0, 1)}, ["c"], {"c": ["y"]}, ["b0"], [ONE, "a"], lambda a2, a1: None, lambda j, a, b: {(0,)})
    p6 = Question(D6, [(ONE, "b0"), ("a", "b0")], "b0", PortQuery(), "y")
    rel6 = {("k", ONE, "b0"): {(0, 0), (1, 1)}, ("k", "e1", "b0"): {(0, 0), (1, 1)}, ("k", "e2", "b0"): {(0, 0), (1, 1)},
            ("m", ONE, "b0"): {(1,)}, ("m", "e1", "b0"): {(0,)}, ("m", "e2", "b0"): {(0,)}}
    E6 = Org("E", ["y", "z"], {"y": (0, 1), "z": (0, 1)}, ["k", "m"], {"k": ["y", "z"], "m": ["z"]}, ["b0"], [ONE, "e1", "e2"],
             lambda a2, a1: None, lambda j, a, b: rel6[(j, a, b)])
    out.append(("L257 a contract of relabelings, τ(1) ≠ 1", Candidate(E6, p6, {"y": Translation(["y"]), "z": Translation(["y"])}, {ONE: "e1", "a": "e2"}, {"b0": "b0"},
                                                                     {"k": (frozenset(["c"]), {"y": Translation(["y"]), "z": Translation(["y"])}), "m": (frozenset(["c"]), {"z": Translation(["y"])})},
                                                                     ["k", "m"], "y")))
    for nm, (c, _ans) in area2_lookups().items():
        out.append((nm, c))
    out.append(("M5: the answer fixed at each pair by another part", m5()))
    out.append(("M13: the owner's weathervane (S41 Q15)", m13()))
    Dv = _org("D_vane", ["y"], {"y": ("N", "S")}, ["c_y"], {"c_y": ("y",)}, ["b0"], [ONE, "turn"], {("c_y", "turn", "b0"): {("N",)}})
    pv = Question(Dv, [(ONE, "b0"), ("turn", "b0")], "b0", PortQuery(), "y", name="p_vane")
    out.append(("R3-Q1: the hand-turned vane ('north when turned')", Candidate(Dv, pv, _T("y"), {ONE: ONE, "turn": "turn"}, {"b0": "b0"},
                                                                              {"c_y": (frozenset(["c_y"]), _T("y"))}, ["c_y"], "y", name="ℰ_vane")))
    for nm, kind in (("FC62's encoding", "const"), ("the second encoding", "two")):
        _p, c = elim(kind)
        out.append(("E5 eliminative (L339), %s" % nm, c))
    Dc, invd, _ = e8_contract_org()
    sets = [a for a in Dc.A if a != ONE and set(dict(invd[a])) == {"m_1_b0"}]
    pd = Question(Dc, [(ONE, "β")] + [(a, "β") for a in sets], "β", PortQuery(), "m_1_b0", name="p_δ")
    lam = {k: (frozenset([k]), {v: Translation((v,)) for v in Dc.foot[k]}) for k in Dc.comps}
    out.append(("E8 p_δ, the identity candidate (K1's criticism question)", Candidate(Dc, pd, {v: Translation((v,)) for v in Dc.ports},
                                                                                        {a: a for a in Dc.A}, {b: b for b in Dc.B}, lam, list(Dc.comps), "m_1_b0")))
    D9 = e9.object_layer()
    p9 = e9.question(D9, [(a, b) for a in D9.A for b in D9.B])
    E9 = e9.sim_layer_S1()
    out.append(("E9 two-layer episode, S1 with t1 (L626)", e9.t1_candidate(p9, E9)))
    out.append(("E9 two-layer episode, S1 with t1∘ψ (L630)", e9.t1_candidate(p9, E9, swapped=True)))
    p = sign_question()
    out.append(("S44 the shop sign, two parts (red on Mon, blue on Tue)", sign_two(p)))
    out.append(("S44 the shop sign, one part (red on Mon, blue on Tue)", sign_one(p)))
    out.append(("the sign with a day port and a palette rule", sign_mech()))
    return out


def student_copy(v):
    """FC30.new1 (d), the student's declared copy of the pole's forward candidate on C1: Acc, and Dec(t) at the student's
    holding o2 computed from the chain (a source o1 with a trace, held; o2 held and Sel's conditions computed from t)."""
    set_variant(v)
    D = pole()
    C1, _, _ = pole_contracts(D)
    c = pole_fwd_candidate(Question(D, C1, "b1_45", PortQuery(), "L", name="p"))
    acc = bool(account(c))
    rows = []
    for Hx, lab in (([(ONE, "b1_45")], "H={(1,b1_45)}"), ([], "H=∅")):
        held_o = bool(faithful(c))
        selc_o = bool(Hx) and set(Hx) <= set(c.p.C) and faithful_on(c, Hx)
        fps = prov_fixed_points(2, [1, held_o], [1, 0], [0, selc_o], "T'", True)
        decs = [not sc[1][0] and not sc[1][1] for R, sc in fps]
        rows.append("%s: held %s, Sel's conditions %s, fixed points %s, Dec(t) at o2 %s, Expl %s" % (lab, tf(held_o), tf(selc_o), prov_show(2, fps), decs, [acc and not d for d in decs]))
    set_variant("none")
    return acc, rows


def section(title):
    print("=" * 150)
    print(title)
    print("-" * 150)


def main():
    section("A. Worked cases: Acc with conjuncts, and Account ∧ ¬Dec(t) under three hand-set histories (Θ by hand, I90), 'none' and each variant")
    cases = worked_cases()
    moved = {v: [] for v in VARIANTS + ["V1.5 (ρ_p constructed by hand)"]}
    for label, c in cases:
        set_variant("none")
        base = evaluate(c)
        print("%s\n   none: %s" % (label, show(base)))
        for v in VARIANTS:
            set_variant(v)
            e = evaluate(c)
            if e != base:
                print("   %s: %s" % (v, show(e)))
                moved[v].append((label, base["acc"], e["acc"], base["prov"]["Sel"][2], e["prov"]["Sel"][2]))
        # V1.5 with the contract's provenance set to constructed by hand: (E) reads no ρ_p otherwise
        set_variant("V1.5")
        c.p.rho = "constructed"
        e = evaluate(c)
        c.p.rho = None
        if e != base:
            print("   V1.5 (ρ_p constructed by hand): %s" % show(e))
            moved["V1.5 (ρ_p constructed by hand)"].append((label, base["acc"], e["acc"], None, None))
        set_variant("none")
    # E6 (FC63): the Leibniz candidate, computed by claims_b.e6_parts
    for v in ["none"] + VARIANTS:
        set_variant(v)
        parts = e6_parts()
        print("E6 skew-symmetric (FC63) under %s: %s" % (v, "; ".join("%s %s" % (p["label"][:6], p["status"]) for p in parts)))
    set_variant("none")
    section("A'. The student's declared copy (FC30.new1 (d)): Acc, Dec(t) at the student's holding computed on the chain (T′), Expl")
    for v in ["none"] + VARIANTS:
        acc, rows = student_copy(v)
        print("%s: Acc(ℰ_fwd) %s; %s" % (v, tf(acc), " | ".join(rows)))
    section("A''. Summary: worked cases whose Acc or Account ∧ ¬Dec(t) moves (label, Acc off → on, Dec under the Sel-history off → on)")
    for v, rows in moved.items():
        print("%s: %d case(s) move" % (v, len(rows)))
        for r in rows:
            print("   %s: Acc %s → %s; Dec (Sel-history) %s → %s" % (r[0], tf(r[1]), tf(r[2]), r[3], r[4]))
    small_cases()


def f1_pairs(c):
    return sorted(((a, b) for (a, b) in c.p.C if not F1_at(c, a, b)), key=repr)


def prod(p, R):
    """Prod(p) (D3.3): Q = Q_w with Out(w, j) for some j, and C holds a setting edit of some v ⇝ w."""
    if getattr(p.Q, "kind", None) != "port":
        return False
    w = p.deltaD
    D = p.D
    if not any(R.output(w, j) for j in D.comps):
        return False
    return any(a in R.Set[v] and R.upstream(v, w) for (a, b) in p.C for v in D.ports)


def small_cases():
    D = pole()
    C1, C2, C2s = pole_contracts(D)
    inv = D.meta["inv"]
    lab = {v: k for k, v in inv.items()}
    b0 = "b1_45"
    section("B. The reply's small cases, run")
    # ---- V1.1
    print("V1.1 (D1.4: Sol_N := the projection of Sol_D)")
    for nm, C in (("C1", C1), ("C2", C2)):
        c = pole_fwd_candidate(Question(D, C, b0, PortQuery(), "L", name=nm))
        for v in ("none", "V1.1"):
            set_variant(v)
            acc, d = account(c, detail=True)
            print("   E_fwd on %s, %s: Acc %s; (F1) fails at %d of %d pairs; at (1,b1_45) proj^λ Sol_{c_L} = %s, L_cL = %d tuples"
                  % (nm, v, tf(acc), len(f1_pairs(c)), len(C), sorted(proj_lam(c, "c_L", D, ONE, b0), key=repr)[:3], len(D.L("c_L", ONE, b0))))
    # ℰ_bv: E_bv = D_pole with c_L replaced by c_bv on (H, T, L); L_bv(1,b) := {(u_H, u_θ, u_H·cot u_θ)}; Γ = {c_bv}; λ(c_bv) = {c_L}.
    # The reply gives L_bv at the identity edit only. Two readings at the other edits [S108-1-I1]: (i) 'follows': L_bv(a,b) :=
    # the one solution of D at (a,b) (the boundary's and the settings' values written in); (ii) 'baseline': L_bv(a,b) := L_bv(1,b).
    bval = D.meta["bval"]
    for rd in ("follows", "baseline"):
        def Lbv(j, a, b, rd=rd):
            if j == "c_bv":
                if rd == "follows":
                    return D.sol(a, b)
                uH, uT = bval[b]
                return frozenset([(uH, uT, uH * COT[uT])])
            return D.L({"c_H": "c_H", "c_T": "c_T"}[j], a, b)
        Ebv = Org("E_bv", ["H", "T", "L"], dict(D.dom), ["c_H", "c_T", "c_bv"], {"c_H": ("H",), "c_T": ("T",), "c_bv": ("H", "T", "L")}, D.B, D.A, D._compose, Lbv)
        for nm, C in (("C1", C1), ("C2", C2)):
            p = Question(D, C, b0, PortQuery(), "L", name=nm)
            cbv = Candidate(Ebv, p, {v: Translation((v,)) for v in D.ports}, {a: a for a in D.A}, {b: b for b in D.B},
                            {"c_bv": (frozenset(["c_L"]), {v: Translation((v,)) for v in ("H", "T", "L")})}, ["c_bv"], "L", name="ℰ_bv")
            for v in ("none", "V1.1"):
                set_variant(v)
                acc, d = account(cbv, detail=True)
                print("   ℰ_bv (%s) on %s, %s: Acc %s [F1 %s F2 %s A %s Dep %s NonVacuous %s]; (F1) fails at %d pairs"
                      % (rd, nm, v, tf(acc), tf(d["F1"]), tf(d["F2"]), tf(d["A"]), tf(d["Dep"]), tf(d["NonVacuous"]), len(f1_pairs(cbv))))
    # E_rev on C_id under V1.1 (not named by the reply)
    Did = pole(bounds=[(1, 45), (2, 45), (3, 45)])
    pid = Question(Did, frozenset((ONE, b) for b in Did.B), b0, fibre_query(), ("H", "T", "L"), name="p_ident")
    rid = pole_rev_candidate(pid, delta=("H", "T", "L"))
    for v in ("none", "V1.1"):
        set_variant(v)
        acc, d = account(rid, detail=True)
        print("   E_rev on C_id, %s: Acc %s [F1 %s F2 %s A %s Dep %s]; (F1) fails at %d of %d pairs (r_H's λ = {c_L})" % (v, tf(acc), tf(d["F1"]), tf(d["F2"]), tf(d["A"]), tf(d["Dep"]), len(f1_pairs(rid)), len(pid.C)))
    set_variant("none")
    # ---- V1.2
    print("V1.2 (D2.1: the clause ∀k ≠ j: L_k(a,b) = L_k(1,b) deleted)")
    a_star = lab[(("H", 2), ("T", 60))]
    Cst = frozenset([(ONE, b0), (a_star, b0)])
    pst = Question(D, Cst, b0, PortQuery(), "L", name="p*")
    for v in ("none", "V1.2"):
        set_variant(v)
        R = Roles(D)
        c = pole_fwd_candidate(pst)
        print("   %s: %s ∈ Set_H %s, ∈ Set_T %s; |Set_H| %d |Set_T| %d |Set_L| %d; asg %s; Prod(p*) %s; E_fwd on C*: Acc %s"
              % (v, a_star, tf(a_star in R.Set["H"]), tf(a_star in R.Set["T"]), len(R.Set["H"]), len(R.Set["T"]), len(R.Set["L"]), R.asg, tf(prod(pst, R)), tf(account(c))))
        for rd in ("R-i", "R-ii"):
            print("      families on C2* under %s: %s; on C2: %s; |Slc| %s; |Obs| %d" % (rd, R.families(C2s, rd), R.families(C2, rd), {j: len(R.slc[j]) for j in D.comps}, len(R.obs(rd))))
    set_variant("none")
    # ---- V1.3
    print("V1.3 (D2.4: R-i the one reading)")
    for v in ("none", "V1.3"):
        set_variant(v)
        R = Roles(D)
        c = pole_fwd_candidate(Question(D, C2, b0, PortQuery(), "L", name="C2"))
        print("   %s: OBS_READING %s; families on C1 %s; on C2 %s; Acc(E_fwd, C2) %s" % (v, core.OBS_READING, R.families(C1, core.OBS_READING), R.families(C2, core.OBS_READING), tf(account(c))))
    set_variant("none")
    # ---- V1.4
    print("V1.4 (D3.3: Ident's contract clause ∃(a,b) ∈ C: a ≠ 1 ∧ obs(a,b) ≠ obs(1,b0))")
    Dall = pole()
    iL = Dall.ports.index("L")

    def obs_L(Dx):
        def f(a, b):
            vals = set(z[Dx.ports.index("L")] for z in Dx.sol(a, b))
            return next(iter(vals)) if len(vals) == 1 else BOT
        return f
    Cid_all = frozenset((ONE, b) for b in Dall.B)
    CH = frozenset([(ONE, b0)] + [(a, b0) for a in single_settings(Dall, ["H"])])
    CL = frozenset([(ONE, b0)] + [(a, b0) for a in single_settings(Dall, ["L"])])
    for v in ("none", "V1.4"):
        set_variant(v)
        rows = ["%s %s" % (nm, tf(ident_contract(obs_L(Dall), C, b0))) for nm, C in (("C_id", Cid_all), ("settings of H", CH), ("settings of L", CL), ("C1", C1))]
        pid2 = Question(Dall, Cid_all, b0, fibre_query(), ("H", "T", "L"), name="p_ident_all")
        r2 = pole_rev_candidate(pid2, delta=("H", "T", "L"))
        print("   %s: Ident's contract clause (fibre query, observed L): %s; E_rev on C_id (9 boundaries): Acc %s" % (v, "; ".join(rows), tf(account(r2))))
    set_variant("none")
    # ---- V1.5
    print("V1.5 (D3.4: ρ_p ∈ {selected, constructed}; declared contracts are no question's)")
    for rho in (None, "constructed", "selected"):
        c = pole_fwd_candidate(Question(D, C1, b0, PortQuery(), "L", name="C1", rho=rho))
        vals = []
        for v in ("none", "V1.5"):
            set_variant(v)
            acc, d = account(c, detail=True)
            vals.append("%s: Acc %s%s" % (v, tf(acc), (" (p a question: %s)" % tf(d["question"])) if "question" in d else ""))
        print("   E_fwd on C1, ρ_p %s: %s" % (rho or "not recorded (declared, S108-1-I5)", "; ".join(vals)))
    set_variant("none")
    # ---- V1.8
    print("V1.8 (D2.6: Slc_j := Alt_j)")
    for v in ("none", "V1.8"):
        set_variant(v)
        R = Roles(D)
        c = pole_fwd_candidate(Question(D, C2, b0, PortQuery(), "L", name="C2"))
        print("   %s: |Slc| %s; Obs(R-ii) %d edits; families on C2 (R-ii) %s; on C2* (R-ii) %s; Acc(E_fwd, C2) %s"
              % (v, {j: len(R.slc[j]) for j in D.comps}, len(R.obs("R-ii")), R.families(C2, "R-ii"), R.families(C2s, "R-ii"), tf(account(c))))
    set_variant("none")
    # ---- V1.6, V1.7: flagged by the tabulation (rule 4), not implemented; the baseline side of V1.7's case only
    print("V1.7 (flagged, not implemented): the baseline side of the reply's case (FC34's 'Acc not monotone in C' witness)")
    Lw = {("h_p0", ONE, "b0"): {(1,)}, ("h_p0", "alt", "b0"): set(), ("h_p0", "alt", "b1"): {(0,)}}
    Dw = _org("D", ["p0"], {"p0": (0, 1)}, ["h_p0"], {"h_p0": ("p0",)}, ["b0", "b1"], [ONE, "alt"], Lw)
    Ew = _org("E", ["p0"], {"p0": (0, 1)}, ["k0"], {"k0": ("p0",)}, ["b0", "b1"], [ONE, "alt"],
              {("k0", ONE, "b0"): {(1,)}, ("k0", "alt", "b0"): set(), ("k0", "alt", "b1"): set()})
    for nm, C, excl in (("C (default scope, I85)", [(ONE, "b0"), (ONE, "b1"), ("alt", "b1")], None),
                        ("C' (default scope, I85: Excl = (A×B)∖C', which V1.7's formula defines)", [(ONE, "b0"), (ONE, "b1")], None),
                        ("C' with Σ' stating Excl(Σ') = ∅", [(ONE, "b0"), (ONE, "b1")], [])):
        pw = Question(Dw, C, "b0", PortQuery(), "p0", excl=excl)
        cw = Candidate(Ew, pw, _T("p0"), {ONE: ONE, "alt": "alt"}, {"b0": "b0", "b1": "b1"}, {"k0": (frozenset(["h_p0"]), _T("p0"))}, ["k0"], "p0")
        acc, d = account(cw, detail=True)
        print("   %s: Acc %s [F1 %s F2 %s A %s Dep %s NonVacuous %s]" % (nm, tf(acc), tf(d["F1"]), tf(d["F2"]), tf(d["A"]), tf(d["Dep"]), tf(d["NonVacuous"])))


if __name__ == "__main__":
    main()
