# S104 round 2 (maths), addendum: the formal examples of the external cross-examination the owner
# supplied (`results/S104 Round 2 - external cross-examination supplied by the owner.txt`), reproduced
# on the S104 model. Run from the folder "results/S104 Round 2 - maths":
#   python3 s104_external.py            every example, FC-E1 to FC-E5
#   python3 s104_external.py FC-E1      one example
# Standard library only. It imports the package `model/` as committed and changes none of it; it reads
# the text under review only to compare its md5, and writes nothing. Every choice this file makes that
# the text leaves open is an invention: I01-I102 in `inventions register.md`, I103-I108 in
# `inventions register - addendum for the external examples.md`; the tags in the code say which.
# The claims are stated in `formal claims - addendum for the external examples.md`.
import hashlib
import itertools
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from model.core import (ONE, BOT, Org, Roles, Question, PortQuery, Candidate, Translation, account,  # noqa: E402
                        restrict, routes, critical_block, contributory, indispensable, no_work, minimal,
                        NC2)
from model.cases import surgical_edits  # noqa: E402
from model.claims_b import all_families, upward_closed  # noqa: E402

TEXT = os.path.join(HERE, "..", "..", "..", "tests", "103 The semantics, standing alone, after round 1.md")  # area 2 copy: one folder deeper
TEXT_MD5 = "f31ebb1f050783f1a84f6136cec20fcd"


def yn(x):
    return "yes" if x else "no"


def fmt_acc(d, val):
    keys = ["F1", "F2eq", "Hom", "F2", "A", "NC1", "NC2", "NonVacuous"]
    return ", ".join("%s %s" % (k, yn(d[k])) for k in keys if k in d) + " => (E) %s" % yn(val)


def fmt_S(S):
    return "{" + ", ".join("{" + ",".join(sorted(W)) + "}" for W in sorted(S, key=lambda W: (len(W), sorted(W)))) + "}"


# ---- organizations of the surgical family (I04, I78, I79) ---------------------------------------------

def surgical_org(name, ports, dom, comps, settable, base, extra=None):
    """One boundary b0. comps: {j: (footprint, home port)}. The edits are every partial setting of the
    settable ports, composed by override (I78); a setting of v replaces v's home component by the slice
    v = x and leaves every other component as it was (I04); exogenous values are carried by components
    (I79). extra: {label: {j: relation}}, edits that alter the named components only; a composite with
    such an edit is undefined (partial composition, I01)."""
    extra = extra or {}
    A, inv, comp_s = surgical_edits({v: dom[v] for v in settable})
    A = list(A) + list(extra)
    foot = {j: f for j, (f, h) in comps.items()}
    home = {j: h for j, (f, h) in comps.items()}

    def compose(a2, a1):
        if a2 in extra or a1 in extra:
            return None
        return comp_s(a2, a1)

    def Lfun(j, a, b):
        if a in extra:
            return frozenset(extra[a].get(j, base[j]))
        sm = dict(inv[a])
        v = home[j]
        if v in sm:
            i = foot[j].index(v)
            return frozenset(w for w in itertools.product(*[dom[u] for u in foot[j]]) if w[i] == sm[v])
        return frozenset(base[j])

    lab = {k: a for a, k in inv.items()}
    return Org(name, ports, dom, list(comps), foot, ["b0"], A, compose, Lfun, meta=dict(inv=inv, lab=lab))


def edit(D, **kw):
    return D.meta["lab"][tuple(sorted(kw.items()))]


def copy_candidate(D, p, E, Gamma, deltaE, lam=None):
    """The identity transport from D to an organization E with the same ports and edit labels; λ(j) = {j}
    with identity port translations unless given (I14, I81)."""
    lam = lam or {j: (frozenset([j]), {v: Translation((v,)) for v in E.foot[j]}) for j in E.comps}
    pi = {v: Translation((v,)) for v in E.ports}
    return Candidate(E, p, pi, {a: a for a in D.A}, {"b0": "b0"}, lam, Gamma, deltaE)


# ---- FC-E1: the external 2.1, an unrelated commitment made critical (I103, I104) ------------------------

def e1_org(name):
    """I103: ports X, Y, U, V in {0,1}; background c_X: X = 0 and c_U: U = 0 (unset inputs set to zero);
    commitments k: Y = X and d: V = U; the edits: the nine partial settings of X and U."""
    ports = ["X", "Y", "U", "V"]
    dom = {v: (0, 1) for v in ports}
    comps = {"c_X": (("X",), "X"), "c_U": (("U",), "U"), "k": (("X", "Y"), "Y"), "d": (("U", "V"), "V")}
    base = {"c_X": {(0,)}, "c_U": {(0,)}, "k": {(0, 0), (1, 1)}, "d": {(0, 0), (1, 1)}}
    return surgical_org(name, ports, dom, comps, ("X", "U"), base)


def restrict_removing(c, W):
    """I104: E|W with the components of Γ \\ W removed, together with every port that lies in no footprint
    of a component left, except the designated answer port (kept, free where nothing constrains it); π
    followed by the projection onto the ports left; λ restricted; commitments W."""
    E = c.E
    keep = [j for j in E.comps if j not in c.Gamma or j in W]
    ports = [v for v in E.ports if v == c.deltaE or any(v in E.foot[j] for j in keep)]
    E2 = Org(E.name + "|{" + ",".join(sorted(W)) + "} (ports removed)", ports, {v: E.dom[v] for v in ports}, keep,
             {j: E.foot[j] for j in keep}, E.B, E.A, E._compose, E._L, meta=E.meta)
    return c.replace(E=E2, pi={v: c.pi[v] for v in ports}, lam={k: v for k, v in c.lam.items() if k in keep},
                     Gamma=tuple(k for k in c.Gamma if k in W), name=c.name + "|" + ",".join(sorted(W)))


def fc_e1():
    out = []
    D = e1_org("D_E1")
    C = [(a, "b0") for a in D.A]
    p = Question(D, C, "b0", PortQuery(), "Y", name="p_E1")
    c = copy_candidate(D, p, e1_org("E_E1"), ["k", "d"], "Y")
    out.append("Target D_E1: ports X, Y, U, V in {0,1}; c_X: X = 0, c_U: U = 0 (background); k: Y = X, d: V = U.")
    out.append("Edits (%d): %s. Contract: every edit at b0. Query: the value of Y." % (len(D.A), ", ".join(D.A)))
    v_full, d_full = account(c, detail=True)
    out.append("Full candidate, Γ = {k,d}: " + fmt_acc(d_full, v_full))
    out.append("  NC2 witness (pair, block): %s" % (NC2(c, witness=True),))
    ck = restrict(c, {"k"})
    v_k, d_k = account(ck, detail=True)
    out.append("E|{k} (I29, deletion): " + fmt_acc(d_k, v_k))
    rows = []
    for (a, b) in C:
        rows.append("%s: target Y = %s, E|{k} Y = %s" % (a, p.ans(a, b), ck.ans_E(a, b)))
    out.append("  answers about Y across the contract: " + "; ".join(rows))
    Sol_D = sorted(D.sol(ONE, "b0"))
    Sol_k = sorted(ck.E.sol(ONE, "b0"))
    out.append("  at the baseline, π[Sol_D] = %s (ports X,Y,U,V); Sol of E|{k} = %s" % (Sol_D, Sol_k))
    S = routes(c)
    G = frozenset(c.Gamma)
    cb = critical_block(S, frozenset({"d"}), G)
    out.append("Routes S_{E,p} = %s; min S = %s" % (fmt_S(S), fmt_S(minimal(S))))
    res = dict(CB_d=cb, indisp_d=indispensable(S, G, "d"), contrib_d=contributory(S, "d"), nowork_d=no_work(S, "d"),
               indisp_k=indispensable(S, G, "k"))
    out.append("CriticalBlock({d}; {k,d}) %s; d globally indispensable %s; d contributory %s; d does no work by itself (L313) %s"
               % (yn(cb), yn(res["indisp_d"]), yn(res["contrib_d"]), yn(res["nowork_d"])))
    reproduced = (v_full and d_k["F1"] and not d_k["F2"] and d_k["A"] and cb and res["indisp_d"] and not res["nowork_d"]
                  and all(p.ans(a, b) == ck.ans_E(a, b) for (a, b) in C))
    # variant (a): d named in the background, not among the commitments
    cbg = c.replace(Gamma=("k",), name="ℰ with d in the background")
    v_bg = account(cbg)
    out.append("Variant (a), d in the named background (Γ = {k}): (E) %s; routes %s" % (yn(v_bg), fmt_S(routes(cbg))))
    # variant (b): the restriction of I104
    S2 = frozenset(frozenset(W) for W in (frozenset(x) for x in itertools.chain.from_iterable(
        itertools.combinations(c.Gamma, r) for r in range(len(c.Gamma) + 1))) if account(restrict_removing(c, W)))
    v_k2, d_k2 = account(restrict_removing(c, {"k"}), detail=True)
    out.append("Variant (b), the restriction of I104 (ports no component left constrains removed, π projected): E|{k}: "
               + fmt_acc(d_k2, v_k2))
    out.append("  routes %s; CriticalBlock({d}; {k,d}) %s; d globally indispensable %s; d does no work by itself %s"
               % (fmt_S(S2), yn(critical_block(S2, frozenset({"d"}), G)), yn(indispensable(S2, G, "d")), yn(no_work(S2, "d"))))
    return reproduced, out


# ---- FC-E2: the external 2.3, first half: outputs by functional determination (I105, I106) ------------

def out_at(org, v, j, which):
    """Out(v, j) with L_j read at: 'identity' (I05); 'not replacing' (I05's first other choice, at every
    edit of A that does not replace j, read as: every edit at which L_j is as at the identity edit, I106
    (a)); 'every' (at every edit of A, those that alter j included, I106 (b))."""
    if v not in org.foot[j]:
        return False
    i = org.foot[j].index(v)
    for a in org.A:
        if which == "identity" and a != ONE:
            continue
        for b in org.B:
            if which == "not replacing" and org.L(j, a, b) != org.L(j, ONE, b):
                continue
            seen = {}
            for w in org.L(j, a, b):
                key = w[:i] + w[i + 1:]
                if key in seen and seen[key] != w[i]:
                    return False
                seen[key] = w[i]
    return True


def fc_e2():
    out = []
    dom = {"X": (0, 1), "Y": (0, 1)}
    rel = {(0, 0), (1, 1)}
    # I105: D_fwd (Y := X: k's home port is Y) and D_rev (X := Y: k's home port is X); both ports settable
    D_fwd = surgical_org("D_fwd", ["X", "Y"], dom, {"c_X": (("X",), "X"), "k": (("X", "Y"), "Y")}, ("X", "Y"),
                         {"c_X": {(0,)}, "k": rel})
    D_rev = surgical_org("D_rev", ["X", "Y"], dom, {"c_Y": (("Y",), "Y"), "k": (("X", "Y"), "X")}, ("X", "Y"),
                         {"c_Y": {(0,)}, "k": rel})
    ok = True
    for D in (D_fwd, D_rev):
        out.append("%s: L_k(1,b0) = %s; edits %s" % (D.name, sorted(D.L("k", ONE, "b0")), ", ".join(D.A)))
        for which in ("identity", "not replacing", "every"):
            ox, oy = out_at(D, "X", "k", which), out_at(D, "Y", "k", which)
            out.append("  L109 output of k, relation read at %s: X %s, Y %s" % (
                {"identity": "the identity edit (I05)", "not replacing": "every edit that leaves L_k as it is (I106 (a))",
                 "every": "every edit, those that alter k included (I106 (b))"}[which], yn(ox), yn(oy)))
            if which in ("identity", "not replacing"):
                ok = ok and ox and oy
        for excl in (False, True):
            R = Roles(D, exclude_identity=excl)
            out.append("  asg (I04%s): %s; inputs: %s" % (", identity excluded (I80 other choice)" if excl else ", I80",
                                                          dict(sorted(R.asg.items())), [v for v in D.ports if R.input(v)]))
    ok = ok and Roles(D_fwd).asg.get("Y") == "k" and Roles(D_rev).asg.get("X") == "k"
    return ok, out


# ---- FC-E3: the external 2.3, second half: a response and a reading of one port (I107) -----------------

def fc_e3():
    out = []
    dom = {v: (0, 1) for v in ("X", "N", "Y")}
    comps = {"c_X": (("X",), "X"), "c_N": (("X", "N"), "N"), "c_Y": (("X", "Y"), "Y")}
    base = {"c_X": {(0,)}, "c_N": {(0, 0), (1, 1)}, "c_Y": {(0, 0), (1, 1)}}
    D = surgical_org("D_ro", ["X", "N", "Y"], dom, comps, ("X", "N", "Y"), base)
    Dr = surgical_org("D_ro+recal", ["X", "N", "Y"], dom, comps, ("X", "N", "Y"), base,
                      extra={"recal(c_N)": {"c_N": {(0, 1), (1, 0)}}})
    single = [ONE] + [a for a in D.A if a != ONE and len(D.meta["inv"][a]) == 1]
    C_single = [(a, "b0") for a in single]
    C_all = [(a, "b0") for a in D.A]
    same, same_i80 = True, True
    for label, org, C in (("C_single (baseline and every single setting)", D, C_single), ("C_all (every edit)", D, C_all),
                          ("C_single plus recal(c_N)", Dr, C_single + [("recal(c_N)", "b0")])):
        for excl in (False, True):
            R = Roles(org, exclude_identity=excl)
            upX = R.Set["X"]
            inv_up = (R.inv("c_N", upX, C), R.inv("c_Y", upX, C))
            for reading in ("R-i", "R-ii"):
                fam = R.families(C, reading)
                mem = {j: (j in fam["causal"], [m for (jj, m) in fam["meas"] if jj == j], j in fam["rule"]) for j in ("c_N", "c_Y")}
                if not excl:
                    out.append("%s, %s, %s: c_N causal %s, measurement of %s, rule %s | c_Y causal %s, measurement of %s, rule %s"
                               " | both invariant under the settings of X: %s" % (
                                   org.name, label, reading, yn(mem["c_N"][0]), mem["c_N"][1] or "none", yn(mem["c_N"][2]),
                                   yn(mem["c_Y"][0]), mem["c_Y"][1] or "none", yn(mem["c_Y"][2]), yn(all(inv_up))))
                if org is D:
                    same = same and mem["c_N"] == mem["c_Y"] and all(inv_up)
                    if excl:
                        same_i80 = same_i80 and fam == Roles(org).families(C, reading)
    R = Roles(Dr)
    Cr = C_single + [("recal(c_N)", "b0")]
    sep = {}
    for reading in ("R-i", "R-ii"):
        fam = R.families(Cr, reading)
        m = {j: (j in fam["causal"], sorted(mm for (jj, mm) in fam["meas"] if jj == j), j in fam["rule"]) for j in ("c_N", "c_Y")}
        sep[reading] = m["c_N"] != m["c_Y"]
    out.append("Under I80's other choice (identity excluded) the families on D_ro are the same as under I80: %s" % yn(same_i80))
    out.append("On D_ro, under both readings and on both contracts, c_N and c_Y share every family and are both invariant"
               " under the settings of X: %s" % yn(same))
    out.append("With recal(c_N) admitted and in the contract they no longer share their families: under R-i %s, under R-ii %s"
               % (yn(sep["R-i"]), yn(sep["R-ii"])))
    return same, out


# ---- FC-E4: the external 3.1, a readout offered as a cause (I108) --------------------------------------

def mem_orgs():
    dom = {v: (0, 1) for v in ("X", "M", "N", "Y")}
    idr = {(0, 0), (1, 1)}
    D = surgical_org("D_mem", ["X", "M", "N", "Y"], dom,
                     {"c_X": (("X",), "X"), "c_M": (("X", "M"), "M"), "c_N": (("M", "N"), "N"), "c_Y": (("M", "Y"), "Y")},
                     ("X", "M", "N", "Y"), {"c_X": {(0,)}, "c_M": idr, "c_N": idr, "c_Y": idr})
    E = surgical_org("E_readout", ["X", "M", "N", "Y"], dom,
                     {"c_X": (("X",), "X"), "c_M": (("X", "M"), "M"), "c_N": (("M", "N"), "N"), "c_Yp": (("N", "Y"), "Y")},
                     ("X", "M", "N", "Y"), {"c_X": {(0,)}, "c_M": idr, "c_N": idr, "c_Yp": idr})
    return D, E


def fc_e4():
    out = []
    D, E = mem_orgs()
    tr = lambda j: {v: Translation((v,)) for v in E.foot[j]}  # noqa: E731
    lam = {"c_X": (frozenset(["c_X"]), tr("c_X")), "c_M": (frozenset(["c_M"]), tr("c_M")),
           "c_N": (frozenset(["c_N"]), tr("c_N")), "c_Yp": (frozenset(["c_N", "c_Y"]), tr("c_Yp"))}
    C1 = [(ONE, "b0"), (edit(D, X=0), "b0"), (edit(D, X=1), "b0")]
    x_do = edit(D, X=1, N=0)
    C2 = C1 + [(x_do, "b0")]
    out.append("Target D_mem: c_X: X = 0, c_M: M = X, c_N: N = M, c_Y: Y = M; candidate E_readout: c_Yp: Y = N in place of c_Y,"
               " λ(c_Yp) = {c_N, c_Y} (M hidden); identity τ on the %d edits." % len(D.A))
    res = {}
    for Gname, Gamma in (("Γ = {c_M, c_N, c_Yp}", ["c_M", "c_N", "c_Yp"]), ("Γ = {c_Yp}", ["c_Yp"])):
        for Cname, C in (("C1 (cue changes)", C1), ("C2 (C1 and %s)" % x_do, C2)):
            p = Question(D, C, "b0", PortQuery(), "Y", name="p_mem")
            c = copy_candidate(D, p, E, Gamma, "Y", lam=lam)
            v, d = account(c, detail=True)
            res[(Gname, Cname[:2])] = (v, d)
            out.append("%s, %s: %s" % (Gname, Cname, fmt_acc(d, v)))
    tsol = D.sol(x_do, "b0")
    esol = E.sol(x_do, "b0")
    out.append("At %s: target solutions (X,M,N,Y) %s; candidate's %s" % (x_do, sorted(tsol), sorted(esol)))
    p = Question(D, C2, "b0", PortQuery(), "Y")
    c = copy_candidate(D, p, E, ["c_Yp"], "Y", lam=lam)
    from model.core import proj_lam
    out.append("  (F1) for c_Yp there: proj of Sol_{c_N,c_Y} on (N,Y) = %s; L_c_Yp = %s" % (
        sorted(proj_lam(c, "c_Yp", D, x_do, "b0")), sorted(E.L("c_Yp", x_do, "b0"))))
    ok = all(res[(g, "C1")][0] for g in ("Γ = {c_M, c_N, c_Yp}", "Γ = {c_Yp}")) and all(
        not res[(g, "C2")][1]["F1"] and not res[(g, "C2")][1]["F2"] and not res[(g, "C2")][1]["A"]
        for g in ("Γ = {c_M, c_N, c_Yp}", "Γ = {c_Yp}")) and sorted(tsol) == [(1, 1, 0, 1)] and sorted(esol) == [(1, 1, 0, 0)]
    return ok, out


# ---- FC-E5: the external section 5, the count of route families checked ------------------------------

def fc_e5():
    out = []
    total = 0
    bad = []
    for n in range(1, 5):
        G = frozenset(range(n))
        cnt = 0
        for Sy in all_families(n):
            if G not in Sy or not upward_closed(Sy, n):
                continue
            cnt += 1
            mins = minimal(Sy)
            U = set().union(*mins)
            I = set.intersection(*[set(m) for m in mins])
            for d in range(n):
                if contributory(Sy, d) != (d in U) or indispensable(Sy, G, d) != (d in I):
                    bad.append((n, Sy, d))
        out.append("|Γ| = %d: %d upward-closed families containing Γ" % (n, cnt))
        total += cnt
    out.append("total %d; the finite monotone claim fails on %d of them" % (total, len(bad)))
    return total == 193 and not bad, out


EXAMPLES = [("FC-E1", "external 2.1: an unrelated commitment is critical and globally indispensable", fc_e1),
            ("FC-E2", "external 2.3, first half: both ports of {(0,0),(1,1)} are outputs", fc_e2),
            ("FC-E3", "external 2.3, second half: a response and a reading of one port share their families", fc_e3),
            ("FC-E4", "external 3.1: a readout offered as a cause fails once the contract holds do(N = 0)", fc_e4),
            ("FC-E5", "external section 5: 193 route families, no counterexample to the finite monotone claim", fc_e5)]


def main():
    with open(TEXT, "rb") as f:
        md5 = hashlib.md5(f.read()).hexdigest()
    if md5 != TEXT_MD5:
        sys.exit("the text under review has md5 %s, not %s; nothing run" % (md5, TEXT_MD5))
    want = set(sys.argv[1:])
    for cid, title, fn in EXAMPLES:
        if want and cid not in want:
            continue
        ok, lines = fn()
        print("=" * 100)
        print("%s  %s" % (cid, title))
        for ln in lines:
            print("   " + ln)
        print("   reproduced: %s" % yn(ok))


if __name__ == "__main__":
    main()
