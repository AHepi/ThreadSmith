# S104 round 2 (maths): tests of FC01-FC36 (formal claims groups A and B).
import itertools
import re
import os

from .core import (ONE, BOT, Org, Roles, Question, PortQuery, FnQuery, Candidate, Translation, powerset, slice_rel,
                   one_kind, footprint_bijections, rename_rel, sig_fn, proj_lam, F1_at, F2eq_at, A_at, F1, F2, F2eq,
                   A, hom, faithful, account, NC1, NC2, slot, contrast, lost, nonvacuous, restrict, routes)
from .gen import (Size, sizes, gen_surg, gen_free, gen_org, gen_question, gen_candidate, gen_lookup,
                  gen_random_candidate, any_candidate, rename_org, rand_rel)
from .cases import (pole, pole_rev, pole_fwd_candidate, pole_rev_candidate, single_settings, fibre_query, COT, TAN)
from .harness import claim, forall, exists, exhaustive, computed, construction, not_tested, look, VAC

SMALL = sizes(max_ports=3, max_dom=2, max_comps=3, max_B=2, max_edits=2)
MID = sizes(max_ports=3, max_dom=3, max_comps=3, max_B=2, max_edits=2)
BOTHFAM = ["G-surg", "G-free"]


def proper_D(D):
    """A model that is not degenerate: every domain has two values or more, every port lies in some
    footprint, and Sol_D(1,b) is nonempty at every boundary [I101]. Used where a degenerate witness would say
    nothing (the search space is recorded with the part)."""
    covered = set(v for j in D.comps for v in D.foot[j])
    return all(len(D.dom[v]) >= 2 for v in D.ports) and covered == set(D.ports) and all(D.sol(ONE, b) for b in D.B)


def D_and_p(rng, size, family=None, full_C=False, proper=False):
    D = gen_org(rng, size, family)
    if proper and not proper_D(D):
        return None, None
    return D, gen_question(rng, D, full_C=full_C)


def show_pairs(C):
    return "{" + ", ".join("(%s,%s)" % x for x in sorted(C, key=repr)) + "}"


# ---------------------------------------------------------------------------------------------------
@claim("FC01", ["I77", "I78"])
def fc01(S):
    parts = []

    def gen(rng, size):
        D = gen_org(rng, size)
        extra = {}
        for j in D.comps:
            for a in D.A:
                for b in D.B:
                    extra[(j, a, b)] = rand_rel(rng, D.full(j), 0.3)
        D2 = Org("D'", D.ports, D.dom, D.comps, D.foot, D.B, D.A, D._compose, lambda j, a, b: D.L(j, a, b) | extra[(j, a, b)])
        G = [j for j in D.comps if rng.random() < 0.5]
        return D, D2, G

    def check(m):
        D, D2, G = m
        for a in D.A:
            for b in D.B:
                if not D.sol(a, b) <= D2.sol(a, b):
                    return "Sol_D(%s,%s) ⊄ Sol_D'(%s,%s)\n%s\n%s" % (a, b, a, b, D.describe(), D2.describe())
                if G and not D.sol(a, b) <= D.delete(G).sol(a, b):
                    return "deletion removed a solution at (%s,%s)\n%s" % (a, b, D.describe())
        return None

    parts.append(forall(S, "FC01", 1, "(a) monotone; deletion keeps solutions",
                        "L_j ⊆ L'_j for every j ⇒ Sol_D ⊆ Sol_D'; Sol_{D−G} ⊇ Sol_D", gen, check, SMALL, 60, BOTHFAM))

    def gen2(rng, size):
        D, p = D_and_p(rng, size)
        return D, p

    def check2(m):
        D, p = m
        for (a, b) in [(a, b) for a in D.A for b in D.B]:
            if p.ans(a, b) is BOT and not D.sol(a, b):
                for G in powerset(D.comps):
                    if G and p.ans(a, b, D.delete(G)) is not BOT:
                        return ("As the Look expects: at (%s,%s) Sol_D is empty, so the port query answers ⊥; deleting {%s} gives the determined answer %r.\n%s\n%s"
                                % (a, b, ",".join(sorted(G)), p.ans(a, b, D.delete(G)), p.describe(), D.describe(pairs=[(a, b)])))
        return None

    parts.append(exists(S, "FC01", 2, "(look) deletion can make an undetermined answer determined",
                        "there are D, (a,b), G with Ans_p(a,b) = ⊥ (Sol empty) and Ans on D−G determined", gen2, check2, SMALL, 40, BOTHFAM))
    return parts


# ---------------------------------------------------------------------------------------------------
@claim("FC02", ["I77", "I78", "I80", "I92"])
def fc02(S):
    parts = []

    def gen(rng, size):
        D = gen_surg(rng, size)
        if len(D.A) < 2:
            return None
        R = Roles(D)
        vs = [v for v in D.ports if R.Set[v] - {ONE}]
        if not vs:
            return None
        v = rng.choice(vs)
        keep = [a for a in D.A if a not in R.Set[v] or a == ONE]
        keepset = set(keep)

        def comp2(a2, a1):
            c = D._compose(a2, a1)
            return c if c in keepset else None

        D2 = Org("D'", D.ports, D.dom, D.comps, D.foot, D.B, keep, comp2, D._L)
        return D, D2, v

    def check(m):
        D, D2, v = m
        R, R2 = Roles(D), Roles(D2)
        if (R.input(v) != R2.input(v)) or (R.asg.get(v) != R2.asg.get(v)):
            return ("D and D' have the same relations and differ only in A (D' lacks the setting edits of %s other than 1).\n"
                    "Input(%s): %s in D, %s in D'; asg(%s): %s in D, %s in D'.\n%s\nA of D' = {%s}"
                    % (v, v, R.input(v), R2.input(v), v, R.asg.get(v), R2.asg.get(v), D.describe(), ",".join(D2.A)))
        return None

    parts.append(exists(S, "FC02", 1, "(a) Input and asg depend on A", "two organizations with the same L and different A differ in Input or asg",
                        gen, check, SMALL, 40, ["G-surg"]))

    def check_b(m):
        D, D2, v = m
        R, R2 = Roles(D), Roles(D2)
        for u in D.ports:
            for j in D.comps:
                if R.output(u, j) != R2.output(u, j):
                    return "Output(%s,%s) differs between D and D' (same L, different A)\n%s" % (u, j, D.describe())
        return None

    parts.append(forall(S, "FC02", 2, "(b) Output does not depend on A", "Out(v, j) is the same for D and D' (same L_j(1,·), different A)",
                        gen, check_b, SMALL, 40, ["G-surg"]))
    D = pole()
    R = Roles(D)
    outs = {v: R.output(v, "c_L") for v in ("H", "T", "L")}
    ok = all(outs.values())
    parts.append(computed("(c) pole: c_L determines each of its ports", "Out(H,c_L), Out(θ,c_L), Out(L,c_L) all hold on the grid (I65)",
                          ok, "Out(v, c_L) for v = H, θ, L: %s. asg (read off the setting edits, I04): %s. The identity edit is a setting edit of H and of θ (I80): %s."
                          % (outs, R.asg, ONE in R.Set["H"] and ONE in R.Set["T"]), ["I92"]))
    return parts


# ---- kinds ------------------------------------------------------------------------------------------

def gen_kinds_org(rng, size):
    """G-free organizations with equal domains and footprints of one size, so that one-kind pairs occur."""
    D = gen_free(rng, size, dvar=False)
    fp = max(1, min(2, len(D.ports)))
    for j in D.comps:
        D.foot[j] = tuple(sorted(rng.sample(list(D.ports), fp), key=D.ports.index))
    table = {}
    for j in D.comps:
        for a in D.A:
            for b in D.B:
                r = rng.random()
                if r < 0.5 and D.comps.index(j) > 0:
                    j0 = D.comps[0]
                    perm = next(footprint_bijections(D, j0, D, j), None)
                    table[(j, a, b)] = rename_rel(table[(j0, a, b)], list(rng.sample(range(fp), fp))) if perm is not None else rand_rel(rng, D.full(j))
                else:
                    table[(j, a, b)] = rand_rel(rng, D.full(j), 0.5)
    D._L = lambda j, a, b: table[(j, a, b)]
    D._full = {}
    return D


def rand_C(rng, D, b0=None):
    b0 = b0 or D.B[0]
    return frozenset([(ONE, b0)] + [(a, b) for a in D.A for b in D.B if rng.random() < 0.5])


@claim("FC03", ["I77", "I78"])
def fc03(S):
    def gen(rng, size):
        D = gen_kinds_org(rng, size)
        return D, rand_C(rng, D)

    def check(m):
        D, C = m
        J = D.comps
        k = {(x, y): one_kind(D, x, D, y, C) for x in J for y in J}
        for x in J:
            if not k[(x, x)]:
                return "not reflexive at %s\n%s\nC = %s" % (x, D.describe(), show_pairs(C))
            for y in J:
                if k[(x, y)] != k[(y, x)]:
                    return "not symmetric at %s,%s\n%s\nC = %s" % (x, y, D.describe(), show_pairs(C))
                for z in J:
                    if k[(x, y)] and k[(y, z)] and not k[(x, z)]:
                        return "not transitive at %s,%s,%s\n%s\nC = %s" % (x, y, z, D.describe(), show_pairs(C))
        return None

    return [forall(S, "FC03", 1, "equivalence", "~_C is reflexive, symmetric and transitive", gen, check,
                   sizes(max_ports=3, max_dom=2, max_comps=4, max_B=2, max_edits=2), 40, ["G-free (equal domains)"])]


@claim("FC04", ["I77", "I78"])
def fc04(S):
    parts = []

    def gen(rng, size):
        D = gen_kinds_org(rng, size)
        C = rand_C(rng, D)
        C2 = frozenset([x for x in C if x == (ONE, D.B[0]) or rng.random() < 0.5])
        return D, C, C2

    def check(m):
        D, C, C2 = m
        for x in D.comps:
            for y in D.comps:
                if one_kind(D, x, D, y, C) and not one_kind(D, x, D, y, C2):
                    return "%s ~_C %s but not on C' ⊆ C\n%s\nC = %s\nC' = %s" % (x, y, D.describe(), show_pairs(C), show_pairs(C2))
        return None

    parts.append(forall(S, "FC04", 1, "(a) coarser identifies more", "C' ⊆ C ∧ j ~_C j' ⇒ j ~_C' j'", gen, check,
                        sizes(max_ports=3, max_dom=2, max_comps=4, max_B=2, max_edits=2), 40, ["G-free (equal domains)"]))

    def check2(m):
        D, C, C2 = m
        for x in D.comps:
            for y in D.comps:
                if x != y and one_kind(D, x, D, y, C2) and not one_kind(D, x, D, y, C):
                    return "%s ~_C' %s and not on C ⊋ C'\n%s\nC = %s\nC' = %s" % (x, y, D.describe(), show_pairs(C), show_pairs(C2))
        return None

    parts.append(exists(S, "FC04", 2, "(b) a finer contract can separate", "there are D, C' ⊊ C, j, j' with j ~_C' j' and not j ~_C j'",
                        gen, check2, sizes(max_ports=3, max_dom=2, max_comps=4, max_B=2, max_edits=2), 40, ["G-free (equal domains)"]))
    return parts


@claim("FC05", ["I77", "I78", "I93"])
def fc05(S):
    parts = []

    def gen(rng, size):
        D = gen_kinds_org(rng, size)
        if len(D.comps) < 2:
            return None
        C = rand_C(rng, D)
        j, j2 = rng.sample(list(D.comps), 2)
        # a pair outside C at which the two relations agree under some bijection
        outside = [(a, b) for a in D.A for b in D.B if (a, b) not in C]
        if not outside:
            return None
        return D, C, j, j2, rng.choice(outside)

    def witness_perms(D, j, j2, C):
        return [perm for perm in footprint_bijections(D, j, D, j2)
                if all(rename_rel(D.L(j, a, b), perm) == D.L(j2, a, b) for (a, b) in C)]

    def check_witness(m):
        D, C, j, j2, x = m
        W = witness_perms(D, j, j2, C)
        agree = [perm for perm in W if rename_rel(D.L(j, *x), perm) == D.L(j2, *x)]
        if not agree:
            return VAC
        before = bool(W)
        after = one_kind(D, j, D, j2, C | {x})
        if agree and before != after:
            return "reading (i) fails\n%s" % D.describe()
        return None

    parts.append(forall(S, "FC05", 1, "(ii) reading (i): β a witness of ~_C",
                        "if β witnesses j ~_C j' and β_*L_j = L_j' at a new pair x, then j ~_{C∪{x}} j'", gen, check_witness,
                        sizes(max_ports=3, max_dom=2, max_comps=3, max_B=2, max_edits=2), 60, ["G-free (equal domains)"], ["I93"]))

    def check_any(m):
        D, C, j, j2, x = m
        anyb = [perm for perm in footprint_bijections(D, j, D, j2) if rename_rel(D.L(j, *x), perm) == D.L(j2, *x)]
        before = one_kind(D, j, D, j2, C)
        if not (anyb and before):
            return VAC
        after = one_kind(D, j, D, j2, C | {x})
        if anyb and before and not after:
            return ("L119: 'an edit under which the two relations stay equal does not separate the components'. Here %s ~_C %s (witness %r), "
                    "the relations agree at the new pair %r under the bijection %r, and yet %s and %s are not of one kind on C ∪ {%r}: "
                    "the pair separates them because they agree there only under a bijection that does not witness ~_C.\n%s\nC = %s"
                    % (j, j2, one_kind(D, j, D, j2, C, witness=True), x, anyb[0], j, j2, x, D.describe(comps=[j, j2]), show_pairs(C)))
        return None

    r2 = forall(S, "FC05", 2, "(ii) reading (ii): any bijection",
                "if j ~_C j' and β_*L_j = L_j' at a new pair x for some footprint bijection β, then j ~_{C∪{x}} j'", gen, check_any,
                sizes(max_ports=3, max_dom=2, max_comps=3, max_B=2, max_edits=2), 200, ["G-free (equal domains)"], ["I93"])
    # area 1: L119 now states reading (i) in symbols (settles I93); reading (ii) is no reading of the text, so its
    # search is reported as a look, not as the claim.
    parts.append(look("(ii) reading (ii), no longer a reading of L119", r2["statement"], r2["status"] == "counterexample found",
                      "reading (ii) search: %s after %s models. %s" % (r2["status"], r2.get("models_tried"), r2.get("counterexample", "")), ["I93"]))

    def gen3(rng, size):
        D = gen_kinds_org(rng, size)
        return D, rand_C(rng, D)

    def check3(m):
        D, C = m
        # sig depends on relations alone: add a component that changes every solution, kinds unchanged
        extra = "zz"
        v = D.ports[0]
        D2 = Org("D+", D.ports, D.dom, list(D.comps) + [extra], dict(D.foot, **{extra: (v,)}), D.B, D.A, D._compose,
                 lambda j, a, b: (D.L(j, a, b) if j != extra else frozenset([(D.dom[v][0],)])))
        for x in D.comps:
            for y in D.comps:
                if one_kind(D, x, D, y, C) != one_kind(D2, x, D2, y, C):
                    return "adding a component changed the kind relation\n%s" % D.describe()
        return None

    parts.append(forall(S, "FC05", 3, "(i) signatures use relations only",
                        "adding a component that changes Sol leaves ~_C among the other components unchanged", gen3, check3,
                        sizes(max_ports=3, max_dom=2, max_comps=3, max_B=2, max_edits=2), 30, ["G-free (equal domains)"]))
    return parts


# ---- setting edits and families -----------------------------------------------------------------------

@claim("FC06", ["I77", "I78", "I80", "I102"])
def fc06(S):
    def gen(rng, size):
        return gen_org(rng, size)

    def check(D):
        R = Roles(D)
        allC = frozenset((a, b) for a in D.A for b in D.B)
        for m, jm in R.asg.items():
            for a in R.Set[m]:
                for j in D.comps:
                    if j == jm:
                        continue
                    for b in D.B:
                        if D.L(j, a, b) != D.L(j, ONE, b):
                            return "setting edit %s of %s changes %s ≠ asg(%s)\n%s" % (a, m, j, m, D.describe())
            for j in D.comps:
                if j != jm and m in D.foot[j] and not R.inv(j, R.Set[m], allC):
                    return "reader %s of %s not invariant under Set_%s\n%s" % (j, m, m, D.describe())
        return None

    return [forall(S, "FC06", 1, "setting edits leave readers as they were",
                   "∀m with asg(m) defined, ∀a ∈ Set_m, ∀j ≠ asg(m): L_j(a,b) = L_j(1,b); every reader of m is invariant under Set_m on every contract",
                   gen, check, MID, 40, BOTHFAM)]


def pole_contracts(D, b0="b1_45"):
    C1 = frozenset([(ONE, b0)] + [(a, b0) for a in single_settings(D, ["H", "T"])])
    C2 = C1 | frozenset((a, b0) for a in single_settings(D, ["L"]))
    inv = D.meta["inv"]
    comp = [a for a in D.A if len(inv[a]) == 2 and "L" in dict(inv[a])]
    C2s = C2 | frozenset((a, b0) for a in comp)
    return C1, C2, C2s


@claim("FC07", ["I92", "I80", "I102"])
def fc07(S):
    D = pole()
    R = Roles(D)
    C1, C2, C2s = pole_contracts(D)
    parts = []
    exp = {("C1", "R-i"): dict(causal=["c_H", "c_T"], meas=[], rule=[]),
           ("C1", "R-ii"): dict(causal=["c_H", "c_T"], meas=[], rule=[]),
           ("C2", "R-i"): dict(causal=["c_H", "c_T"], meas=[("c_L", "H"), ("c_L", "T")], rule=[]),
           ("C2", "R-ii"): dict(causal=["c_H", "c_L", "c_T"], meas=[], rule=[])}
    for (cn, C) in (("C1", C1), ("C2", C2)):
        for rd in ("R-i", "R-ii"):
            got = R.families(C, rd)
            parts.append(computed("pole %s under %s" % (cn, rd), "the families FC07 states for %s under %s: %s" % (cn, rd, exp[(cn, rd)]),
                                  got == exp[(cn, rd)], "computed: %s; Obs(%s) = {%s}" % (got, rd, ", ".join(sorted(R.obs(rd)))), ["I92"]))
    got = {rd: R.families(C2s, rd) for rd in ("R-i", "R-ii")}
    parts.append(computed("pole C2 with composites (outside FC07's statement)",
                          "C2* = C2 plus the composite settings that set L together with H or θ: families under both readings",
                          True, "R-i: %s; R-ii: %s. Slc_j (edits replacing j by a slice on a port j assigns) = %s. Area 1 fix (H01): such an edit is an intervention on j, no edit to j's rule (L57) and, under R-ii, no observation edit of j's reading and no edit to its measuring relation; under R-ii (OBS_READING) C2* then gives C2's families. Round 2's D2.1 with I08 counted composites as rule edits and gave no causal component and the rule signature to every component."
                          % (got["R-i"], got["R-ii"], {j: sorted(R.slc[j]) for j in D.comps}), ["I92"]))
    return parts


@claim("FC08", ["I77", "I78"])
def fc08(S):
    parts = []

    def gen(rng, size):
        D = gen_surg(rng, size)
        return D

    def check(D):
        R = Roles(D)
        allC = frozenset((a, b) for a in D.A for b in D.B)
        for rd in ("R-i", "R-ii"):
            for j in D.comps:
                o = R.outputs_of(j)
                if len(o) != 1:
                    continue
                o = o[0]
                for m in D.foot[j]:
                    if m == o or not R.meas(j, m, allC, rd):
                        continue
                    if len(D.dom[m]) < 2 or len(D.dom[o]) < 2:
                        continue  # a reading that cannot vary, or a part that cannot, witnesses nothing
                    im = D.ports.index(m)
                    moved = [a for a in R.Set[m] - {ONE} for b in D.B
                             if D.sol(ONE, b) and D.sol(a, b) and set(z[im] for z in D.sol(a, b)) != set(z[im] for z in D.sol(ONE, b))]
                    if not moved:
                        continue  # no setting of m that changes the part
                    io = D.ports.index(o)
                    follows = False
                    for a in moved:
                        for b in D.B:
                            if set(z[io] for z in D.sol(a, b)) != set(z[io] for z in D.sol(ONE, b)):
                                follows = True
                    if R.Set[m] - {ONE} and not follows:
                        return ("Under %s, %s is a measurement of %s on the contract of every pair (both clauses of L124 hold), and no setting edit of %s changes the projection of Sol on the reading %s: 'change the part and the reading follows' fails.\n%s"
                                % (rd, j, m, m, o, D.describe()))
        return None

    parts.append(exists(S, "FC08", 1, "a measurement whose reading does not follow",
                        "there are D and j reading m with Meas_C(j,m) (both clauses) whose reading's projection does not follow a setting of m",
                        gen, check, SMALL, 60, ["G-surg"]))
    return parts


@claim("FC09", ["I78"])
def fc09(S):
    # L347: a rule relation C_r ⊆ Z × S; ports z, s; components h_z (z = u_b) and c_r (the rule);
    # edits: set z (interventions on Z), set s, and an alternative relation of c_r (an edit to C_r).
    from .gen import Size
    ports = ["z", "s"]
    dom = {"z": (0, 1), "s": (0, 1)}
    comps = ["h_z", "c_r"]
    foot = {"h_z": ("z",), "c_r": ("z", "s")}
    B = ["b0", "b1"]
    base = {("h_z", "b0"): {(0,)}, ("h_z", "b1"): {(1,)}, ("c_r", "b0"): {(0, 0), (1, 1)}, ("c_r", "b1"): {(0, 0), (1, 1)}}
    altr = {(0, 1), (1, 0)}  # the rule edited: s = not z
    A = [ONE, "set_z0", "set_z1", "set_s0", "alt_r"]

    def Lf(j, a, b):
        if a.startswith("set_z") and j == "h_z":
            return {(int(a[-1]),)}
        if a.startswith("set_s") and j == "c_r":
            return {(x, int(a[-1])) for x in (0, 1)}
        if a == "alt_r" and j == "c_r":
            return altr
        return base[(j, b)]

    D = Org("D_rule", ports, dom, comps, foot, B, A, lambda a2, a1: None, Lf)
    R = Roles(D)
    allC = frozenset((a, b) for a in A for b in B)
    fam = {rd: R.families(allC, rd) for rd in ("R-i", "R-ii")}
    ok = all("c_r" in fam[rd]["rule"] for rd in fam)
    return [computed("L347's rule relation has Rule_C's signature", "Rule_C(c_r) on the contract of every pair (I08)", ok,
                     "families: %s. So 'a constitutive status' (L347) and 'a rule' (L125) both map to Rule_C. Under both readings c_r also has the signature of a measurement of z (the edits setting s and the rule edit alter c_r and leave h_z): the families overlap." % fam,
                     ["I78"])]


@claim("FC10", ["I77", "I78"])
def fc10(S):
    def check(D):
        R = Roles(D)
        rng_pairs = [(a, b) for a in D.A for b in D.B]
        C = frozenset(rng_pairs)
        for j in D.comps:
            if R.rule(j, C) and not (R.changes(j, R.alt[j] - R.set_oj(j), C) and R.inv(j, R.world(j), C)):
                return "Rule without its clauses\n" + D.describe()
            for rd in ("R-i", "R-ii"):
                if R.causal(j, C, rd) and not R.changes(j, R.set_oj(j), C):
                    return "Causal without change under its output's setting\n" + D.describe()
        return None

    return [forall(S, "FC10", 1, "families imply L57's clauses", "Rule_C ⇒ variable under rule edits ∧ invariant under world interventions; Causal_C ⇒ changes under intervention on its output",
                   lambda rng, size: gen_org(rng, size), check, SMALL, 40, BOTHFAM),
            not_tested("L57 names no condition on observation edits; the removed clause", "textual comparison of L57 with L123",
                       "a reading of two sentences' wording, not a property of models")]


@claim("FC11", ["I92", "I80"])
def fc11(S):
    D = pole()
    R = Roles(D)
    C = frozenset([(ONE, "b1_45")])
    ok = R.input("H") and not R.causal(R.asg["H"], C, "R-i") and not R.causal(R.asg["H"], C, "R-ii")
    return [computed("Input(v) without Causal_C(asg(v))", "there are D, C, v with Input(v) and ¬Causal_C(asg(v))", ok,
                     "pole, C = {(1,b1_45)}: Input(H) = %s, Causal_C(c_H) = %s (R-i), %s (R-ii)" % (R.input("H"), R.causal("c_H", C, "R-i"), R.causal("c_H", C, "R-ii")), ["I92"]),
            construction("families use edits of A only", "no family predicate needs an edit A lacks", True,
                         "Roles quantifies over org.A and over the pairs of C only.")]


@claim("FC12", ["I77", "I78", "I80"])
def fc12(S):
    def check(D):
        R = Roles(D)
        for b0 in D.B:
            C = frozenset([(ONE, b0)])
            for rd in ("R-i", "R-ii"):
                f = R.families(C, rd)
                if f["causal"] or f["meas"] or f["rule"]:
                    return "C = {(1,%s)}: families %s under %s\n%s" % (b0, f, rd, D.describe())
        return None

    return [forall(S, "FC12", 1, "the baseline contract puts no component in any family", "C = {(1,b0)} ⇒ no component in any family, both readings",
                   lambda rng, size: gen_org(rng, size), check, MID, 40, BOTHFAM)]


@claim("FC13", ["I77", "I78", "I70"])
def fc13(S):
    def gen(rng, size):
        D = gen_org(rng, size)
        return D, rng

    def check(m):
        D, rng = m
        D2, pm, cm, bm, am = rename_org(D, rng)
        C = frozenset((a, b) for a in D.A for b in D.B)
        C2 = frozenset((am[a], bm[b]) for (a, b) in C)
        R, R2 = Roles(D), Roles(D2)
        for rd in ("R-i", "R-ii"):
            f, f2 = R.families(C, rd), R2.families(C2, rd)
            mapped = dict(causal=sorted(cm[j] for j in f["causal"]), meas=sorted((cm[j], pm[m]) for j, m in f["meas"]), rule=sorted(cm[j] for j in f["rule"]))
            if mapped != f2:
                return "families not carried by a renaming\n%s" % D.describe()
        return None

    return [forall(S, "FC13", 1, "families are carried by renamings", "the family predicates, computed from (D, C) alone, are carried along by every renaming of ports, components, edits and boundaries",
                   gen, check, SMALL, 40, BOTHFAM, ["I70"]),
            construction("no further data", "Causal_C, Meas_C, Rule_C take (D, C) and a reading of observation edits, nothing else", True,
                         "Roles(org) and families(C, reading): no declared asg, no declared measured port.")]


@claim("FC14", [])
def fc14(S):
    here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # integration (areas 1 + 2 combined): the first formal core found, in this order: the formal core after
    # round 2 beside this model's folder; one beside model/ (the original layout); the committed one (read only).
    # S105 round 3, integration: the formal core after round 3 beside this model's folder first, then the committed
    # formal core after round 2 (read only), then the older places.
    # S106: the formal core after S106 beside this model's folder first, then round 3's (read only).
    tries = [os.path.join(here, "..", "formal core, after S106.md"),
             os.path.join(here, "..", "..", "S105 Round 3 - maths after the reading", "formal core, after round 3.md"),
             os.path.join(here, "..", "formal core, after round 3.md"),
             os.path.join(here, "..", "..", "S104 Round 2 - maths after the reading", "formal core, after round 2.md"),
             os.path.join(here, "..", "formal core, after round 2.md"), os.path.join(here, "formal core, after round 2.md"),
             os.path.join(here, "formal core.md"), os.path.join(here, "..", "..", "S104 Round 2 - maths", "formal core.md")]
    fc = next((x for x in tries if os.path.exists(x)), None)
    if fc is None:
        return [not_tested("syntactic scan", "no definition of the formal core takes a predicate 'is a cause'", "no formal core found at: %s" % "; ".join(tries))]
    txt = open(fc, encoding="utf-8").read().split("\n")
    hits = [l for l in txt if l.startswith("**D") and re.search(r"\bis a cause\b|IsCause|Cause\(", l)]
    ndef = sum(1 for l in txt if l.startswith("**D"))
    return [computed("syntactic scan", "no definition of the formal core takes a predicate 'is a cause'", not hits,
                     "read %s: %d definition lines; matching 'is a cause' / 'IsCause' / 'Cause(': %d" % (os.path.basename(fc), ndef, len(hits)))]


# ---- transports -----------------------------------------------------------------------------------

def gen_p_cand(rng, size, valuemaps=False, family=None, proper=False):
    D, p = D_and_p(rng, size, family, proper=proper)
    if D is None:
        return None
    c = any_candidate(rng, p, size, valuemaps=valuemaps)
    if proper and not c.Gamma:
        return None
    return p, c


def gen_p_cand_proper(rng, size):
    return gen_p_cand(rng, size, proper=True)


@claim("FC15", ["I77", "I78", "I81"])
def fc15(S):
    def check(m):
        p, c = m
        if c.tau.get(ONE) != ONE:
            return VAC
        img = frozenset((c.tau[a], c.sigma[b]) for (a, b) in p.C if a in c.tau and b in c.sigma)
        if (ONE, c.sigma[p.b0]) not in img or not all(a in c.E.A and b in c.E.B for (a, b) in img):
            return "τ[C] is not a contract of E\n" + c.describe()
        return None

    return [forall(S, "FC15", 1, "τ[C] holds (1, σ(b0))", "τ(1) = 1 ⇒ τ[C] ⊆ A_E × B_E and (1, σ(b0)) ∈ τ[C]", gen_p_cand, check, SMALL, 40, BOTHFAM)]


@claim("FC16", ["I77", "I78", "I81"])
def fc16(S):
    def check(m):
        p, c = m
        E = c.E
        img = frozenset((c.tau[a], c.sigma[b]) for (a, b) in p.C)
        for k in E.comps:
            for k2 in E.comps:
                x = one_kind(E, k, E, k2, p.C, (c.tau, c.sigma), (c.tau, c.sigma))
                y = one_kind(E, k, E, k2, img)
                if x != y:
                    return "through t: %s, on τ[C]: %s for %s,%s\n%s" % (x, y, k, k2, c.describe())
        return None

    return [forall(S, "FC16", 1, "reading through t agrees with (K) on τ[C]", "k, k' coincide on C through t ⟺ k ~_{τ[C]} k'",
                   gen_p_cand, check, SMALL, 40, BOTHFAM)]


@claim("FC17", ["I77", "I78", "I81"])
def fc17(S):
    def check(m):
        p, c = m
        if not F1(c):
            return VAC
        for k in c.Gamma:
            for (a, b) in p.C:
                if c.E.L(k, c.tau[a], c.sigma[b]) != proj_lam(c, k, p.D, a, b):
                    return "F1 holds and the signatures differ\n" + c.describe()
        return None

    return [forall(S, "FC17", 1, "(F1) makes each commitment's signature its counterpart's", "F1_C ⇒ sig of k through t = sig_C(λ(k)) on C",
                   lambda rng, size: gen_p_cand(rng, size, valuemaps=True), check, SMALL, 40, BOTHFAM)]


@claim("FC18", ["I77", "I78", "I81", "I94"])
def fc18(S):
    parts = []

    def check_a(m):
        p, c = m
        if not F1(c):
            return VAC
        for k in c.Gamma:
            ident = tuple(range(len(c.E.foot[k])))
            if not all(rename_rel(c.E.L(k, c.tau[a], c.sigma[b]), ident) == proj_lam(c, k, p.D, a, b) for (a, b) in p.C):
                return "F1 without SameKind (D4.4 reading)\n" + c.describe()
        return None

    parts.append(forall(S, "FC18", 1, "D4.4's reading (counterpart carried to V_k)", "F1_C ⇒ SameKind_C, the counterpart's signature read on V_k (D4.4)",
                        lambda rng, size: gen_p_cand(rng, size, valuemaps=True), check_a, SMALL, 40, BOTHFAM))

    def check_b(m):
        p, c = m
        if not F1(c):
            return VAC
        D = p.D
        for k in c.Gamma:
            N, tr = c.lam[k]
            dports = [tr[v].dports[0] for v in c.E.foot[k]]
            if len(set(dports)) != len(dports):
                continue
            # the counterpart read 'directly': its projection on its own D ports, D's domains [I94]
            ok_any = False
            for perm in itertools.permutations(range(len(dports))):
                if not all(set(c.E.dom[c.E.foot[k][i]]) == set(D.dom[dports[perm[i]]]) for i in range(len(dports))):
                    continue
                good = True
                for (a, b) in p.C:
                    VN, Sn = D.sol_sub(N, a, b)
                    direct = frozenset(tuple(z[VN.index(u)] for u in dports) for z in Sn)
                    through = c.E.L(k, c.tau[a], c.sigma[b])
                    if rename_rel(through, [perm.index(i) for i in range(len(perm))]) != direct and rename_rel(through, perm) != direct:
                        good = False
                        break
                if good:
                    ok_any = True
                    break
            if not ok_any:
                return ("Under the untranslated reading of 'read on C directly … up to the port translation' (I94), (F1) holds and "
                        "commitment %s is of no kind with its counterpart: its port domains are the images of value maps, so no footprint "
                        "bijection between equal domains exists (I10). Argument 1's Consequence then needs I10's value-bijection alternative.\n%s\n%s"
                        % (k, p.describe(), c.describe()))
        return None

    # S105 round 3, area 3 (W8): L554 reads the counterpart 'up to the port translation' (D4.4), which the untranslated
    # reading (I94) drops; its search is kept as a look, so FC18's status is the claim L558 cites, not I94's reading.
    r = forall(S, "FC18", 2, "untranslated reading (I94)", "F1_C ⇒ SameKind_C, the counterpart read on its own D ports with D's domains",
               lambda rng, size: gen_p_cand(rng, size, valuemaps=True), check_b, SMALL, 60, BOTHFAM, ["I94"])
    txt = "search: %s; models tried %s, hypothesis met %s%s" % (r["status"], r.get("models_tried"), r.get("hypothesis_met"),
                                                                 ("; smallest size %s; counterexample:\n%s" % (r.get("smallest_size"), r["counterexample"])) if r.get("counterexample") else "")
    parts.append(look("untranslated reading (I94), not the text's (L554: 'up to the port translation')", "F1_C ⇒ SameKind_C with the counterpart read on its own D ports with D's domains: expected to fail (value maps)",
                      r["status"] == "counterexample found", txt, ["I94"]))
    return parts


@claim("FC19", ["I77", "I78", "I81", "I101"])
def fc19(S):
    parts = []

    def ca(m):
        p, c = m
        if F2(c) and A(c) and not F1(c):
            return "F2 ∧ A ∧ ¬F1\n%s\n%s\n%s" % (p.describe(), p.D.describe(), c.describe())
        return None

    def cb(m):
        p, c = m
        if F1(c) and not F2(c):
            return "F1 ∧ ¬F2 (F2eq %s, Hom %s)\n%s\n%s\n%s" % (F2eq(c), hom(c), p.describe(), p.D.describe(), c.describe())
        return None

    parts.append(exists(S, "FC19", 1, "(a) F2 ∧ A ∧ ¬F1", "there is ℰ with F2_C ∧ A_C ∧ ¬F1_C", gen_p_cand_proper, ca, SMALL, 200, BOTHFAM, ["I101"],
                        note="proper models only: domains ≥ 2, every port in a footprint, Sol_D(1,b) ≠ ∅, Γ ≠ ∅"))

    def cb2(m):
        p, c = m
        if len(c.Gamma) < 2 or set(c.E.comps) != set(c.Gamma) or not F1(c) or F2(c):
            return None
        return cb(m)

    parts.append(exists(S, "FC19", 2, "(b) F1 ∧ ¬F2", "there is ℰ with two or more commitments, no background component, and F1_C ∧ ¬F2_C", gen_p_cand_proper, cb2, SMALL, 300, BOTHFAM, ["I101"],
                        note="proper models only: domains ≥ 2, every port in a footprint, Sol_D(1,b) ≠ ∅, |Γ| ≥ 2"))
    return parts


@claim("FC20", ["I77", "I78", "I81"])
def fc20(S):
    parts = []

    def gen(rng, size):
        p, c = gen_p_cand(rng, size, valuemaps=True)
        if c.deltaE not in c.pi or c.pi[c.deltaE].dports != (p.deltaD,):
            return None
        return p, c

    def chk(m, identity_only):
        p, c = m
        kap = c.pi[c.deltaE].fn
        ident = all(kap((x,)) == x for x in p.D.dom[p.deltaD])
        if identity_only and not ident:
            return VAC
        met = False
        for (a, b) in p.C:
            if not F2eq_at(c, a, b):
                continue
            y = p.ans(a, b)
            if y is BOT:
                continue  # area 1 FC20': the claim is restated for pairs where Ans_p is determined
            met = True
            ky = BOT if y is BOT else kap((y,))
            if c.ans_E(c.tau[a], c.sigma[b]) != ky:
                vals = sorted(set(z[p.D.ports.index(p.deltaD)] for z in p.D.sol(a, b)))
                return ("At (%s,%s) the valuation equation of (F2) holds and π acts on the designated port as the value map %s, yet "
                        "Ans_E = %r while κ(Ans_p) = %r: the target's port takes the values %s, so Ans_p = ⊥, and κ sends them to one value, "
                        "so E's answer is determined. FC20's conclusion needs κ injective on the values Sol_D takes.\n%s\n%s\n%s"
                        % (a, b, c.pi[c.deltaE].name, c.ans_E(c.tau[a], c.sigma[b]), ky, vals, p.describe(), p.D.describe(pairs=[(a, b)]), c.describe()))
        return None if met else VAC

    parts.append(forall(S, "FC20", 1, "any value map κ", "FC20': F2eq at (a,b) ∧ Ans_p(a,b) ≠ ⊥ ∧ π acts on the designated port as κ ⇒ Ans_E(τa,σb) = κ(Ans_p(a,b))",
                        gen, lambda m: chk(m, False), SMALL, 150, BOTHFAM, ["I14"]))
    parts.append(forall(S, "FC20", 2, "κ the identity", "F2eq at (a,b) ∧ π the identity on the designated port ⇒ (A) at (a,b)",
                        gen, lambda m: chk(m, True), SMALL, 100, BOTHFAM))

    def viol(m):
        p, c = m
        kap = c.pi[c.deltaE].fn
        if not all(kap((x,)) == x for x in p.D.dom[p.deltaD]):
            return VAC
        for (a, b) in p.C:
            v = not (F1_at(c, a, b) and F2eq_at(c, a, b))
            vp = not (F1_at(c, a, b) and F2eq_at(c, a, b) and A_at(c, a, b))
            if v != vp:
                return "Violation ≠ Violation⁺ at (%s,%s)\n%s" % (a, b, c.describe())
        return None

    parts.append(forall(S, "FC20", 3, "Violation and Violation⁺ coincide where κ = id", "κ the identity ⇒ Viol(t;a,b) ⟺ Viol⁺(t;a,b)", gen, viol, SMALL, 60, BOTHFAM))
    return parts


@claim("FC21", ["I77", "I78", "I81", "I85", "I101"])
def fc21(S):
    parts = []

    def gen(rng, size, proper=False):
        D = gen_org(rng, size)
        if proper and not proper_D(D):
            return None
        b0 = rng.choice(D.B)
        q = Question(D, [(ONE, b0)], b0, PortQuery(), rng.choice(D.ports))
        y0 = q.ans(ONE, b0)
        if y0 is BOT:
            return None
        C = [(a, b) for a in D.A for b in D.B if q.ans(a, b) == y0]
        p = Question(D, C, b0, PortQuery(), q.deltaD)
        return p, any_candidate(rng, p, size)

    def ca(m):
        p, c = m
        if c.tau.get(ONE) != ONE or not A(c):
            return VAC
        if NC2(c):
            return "relabeling contract, A holds, NC2 holds\n%s\n%s" % (p.describe(), c.describe())
        return None

    def cb(m):
        p, c = m
        if NC2(c) and len(p.C) >= 1:
            return ("On a contract of relabelings (every pair of C has the baseline answer %r), a candidate without (A) meets NC2 (witness %s).\n%s\n%s\n%s"
                    % (p.ans(ONE, p.b0), NC2(c, witness=True), p.describe(), p.D.describe(), c.describe()))
        return None

    parts.append(forall(S, "FC21", 1, "(a) relabelings and (A) exclude NC2", "every edit of C a relabeling ∧ A_C ∧ τ(1) = 1 ⇒ ¬NC2", gen, ca, SMALL, 60, BOTHFAM))
    parts.append(exists(S, "FC21", 2, "(b) without (A)", "a candidate whose answers vary over τ[C] meets NC2 on a contract of relabelings",
                        lambda rng, size: gen(rng, size, True), cb, SMALL, 200, BOTHFAM, ["I101"], note="proper models only"))
    parts.append(construction("(c) 'excluding every change under which the commitments could matter'", "is ¬NC2 for every candidate", True,
                              "read as the definition of NC2 negated; nothing to search"))

    # Area 2: D6.9 without I26's '≠ ⊥' (relabeling: Ans_p(a,b) = Ans_p(1,b0), ⊥ = ⊥), settles I26 at L257.
    def gen_bot(rng, size):
        D = gen_org(rng, size)
        b0 = rng.choice(D.B)
        q = Question(D, [(ONE, b0)], b0, PortQuery(), rng.choice(D.ports))
        y0 = q.ans(ONE, b0)
        C = [(a, b) for a in D.A for b in D.B if q.ans(a, b) == y0]
        p = Question(D, C, b0, PortQuery(), q.deltaD)
        return p, any_candidate(rng, p, size)

    parts.append(forall(S, "FC21", 4, "(a2) area 2: relabelings with ⊥ allowed, τ(1) = 1 and (A) exclude NC2",
                        "every edit of C a relabeling (Ans_p(a,b) = Ans_p(1,b0), ⊥ = ⊥) ∧ A_C ∧ τ(1) = 1 ⇒ ¬NC2", gen_bot, ca, SMALL, 60, BOTHFAM))

    # (d) area 2: with τ(1) ≠ 1 a candidate meets (A), NC1 and NC2 on a contract of relabelings (the ruling's M6), so (F2) is needed.
    D6 = Org("D", ["y"], {"y": (0, 1)}, ["c"], {"c": ["y"]}, ["b0"], [ONE, "a"], lambda a2, a1: None,
             lambda j, a, b: {(0,)})
    p6 = Question(D6, [(ONE, "b0"), ("a", "b0")], "b0", PortQuery(), "y")
    rel6 = {("k", ONE, "b0"): {(0, 0), (1, 1)}, ("k", "e1", "b0"): {(0, 0), (1, 1)}, ("k", "e2", "b0"): {(0, 0), (1, 1)},
            ("m", ONE, "b0"): {(1,)}, ("m", "e1", "b0"): {(0,)}, ("m", "e2", "b0"): {(0,)}}
    E6 = Org("E", ["y", "z"], {"y": (0, 1), "z": (0, 1)}, ["k", "m"], {"k": ["y", "z"], "m": ["z"]}, ["b0"], [ONE, "e1", "e2"],
             lambda a2, a1: None, lambda j, a, b: rel6[(j, a, b)])
    c6 = Candidate(E6, p6, {"y": Translation(["y"]), "z": Translation(["y"])}, {ONE: "e1", "a": "e2"}, {"b0": "b0"},
                   {"k": (frozenset(["c"]), {"y": Translation(["y"]), "z": Translation(["y"])}), "m": (frozenset(["c"]), {"z": Translation(["y"])})},
                   ["k", "m"], "y")
    # S106: Dependence is NC2 (D6.5); NC1 is no longer a conjunct and no longer asked here (it holds for c6: printed).
    ok6 = A(c6) and bool(NC2(c6)) and not hom(c6)
    parts.append(computed("(d) area 2: τ(1) ≠ 1", "on a contract of relabelings a candidate with τ(1) ≠ 1 meets (A) and Dependence (NC2) and fails (F2)", ok6,
                          "A %s, Dependence (NC2) witness %s, NC1 %s (not a conjunct after S106), Hom (τ(1) = 1 in (F2)) %s, F2 %s: so L257's sentence needs (F2) as well as (A)"
                          % (A(c6), NC2(c6, witness=True), NC1(c6), hom(c6), F2(c6))))
    return parts


@claim("FC22", ["I77", "I78", "I81"])
def fc22(S):
    def gen(rng, size):
        D = gen_org(rng, size)
        b0 = rng.choice(D.B)
        p = Question(D, [(ONE, b0)], b0, PortQuery(), rng.choice(D.ports))
        return p, any_candidate(rng, p, size)

    def check(m):
        p, c = m
        if c.tau.get(ONE) == ONE and NC2(c):
            return "baseline contract with NC2\n" + c.describe()
        return None

    parts = [forall(S, "FC22", 1, "the baseline alone gives no contrast", "C = {(1,b0)} ∧ τ(1) = 1 ⇒ ¬NC2", gen, check, SMALL, 60, BOTHFAM)]
    # [owner S41: Q15] (b) M13 of the ruling on L255-L257 (the weathervane): Ans_p(1,b0) = ⊥ (several solutions),
    # the edit e fixes the answer; E = D, Γ = {c_y}. NC2 holds under the symmetric contrast (D6.4 as S41 has it),
    # not under round 2's D6.4 (a determined baseline asked).
    D = _org("D", ["x", "y"], {"x": (0, 1), "y": (0, 1)}, ["cx", "cy"], {"cx": ["x"], "cy": ["x", "y"]}, ["b0"], [ONE, "e"],
             {("cx", "e", "b0"): {(1,)}, ("cy", ONE, "b0"): {(0, 0), (1, 1)}, ("cy", "e", "b0"): {(0, 0), (1, 1)}})
    p = Question(D, [(ONE, "b0"), ("e", "b0")], "b0", PortQuery(), "y")
    c = Candidate(D, p, _T("x", "y"), {ONE: ONE, "e": "e"}, {"b0": "b0"},
                  {"cx": (frozenset(["cx"]), _T("x")), "cy": (frozenset(["cy"]), _T("x", "y"))}, ["cy"], "y", name="ℰ_M13")
    w_s41, w_r2 = NC2(c, witness=True), NC2(c, witness=True, reading="round2")
    acc, d = account(c, detail=True)
    ok = p.ans(ONE, "b0") is BOT and p.ans("e", "b0") is not BOT and w_s41 is not None and w_r2 is None and acc
    parts.append(computed("(b) owner S41, Q15: a contrast from ⊥ to a determined answer counts (M13)",
                          "Ans_E(1,σb0) = ⊥, Ans_E(τe,σb0) determined, the contrast lost when c_y is deleted ⇒ NC2 (D6.4, symmetric); E = D meets (E) on M13's contract",
                          ok, "Ans_p: baseline %r, at e %r; NC2 witness under D6.4 as S41 has it: %s; under round 2's D6.4: %s; (E): %s %s\n%s\n%s"
                          % (p.ans(ONE, "b0"), p.ans("e", "b0"), w_s41, w_r2, acc, {k: d[k] for k in ("F1", "F2", "A", "NC1", "NC2", "NonVacuous")}, D.describe(), c.describe()),
                          ["I21"]))
    return parts


@claim("FC23", ["I77", "I78", "I81", "I82", "I83", "I79"])
def fc23(S):
    parts = []

    def gen(rng, size):
        D, p = D_and_p(rng, size)
        if any(p.ans(a, b) is BOT for (a, b) in p.C):
            return None
        return p, gen_lookup(rng, p)

    def ca(m):
        p, c = m
        if NC1(c):
            return "the lookup meets NC1\n" + c.describe()
        return None

    def cb(m):
        p, c = m
        vals = set(p.ans(a, b) for (a, b) in p.C)
        if len(vals) < 2:
            return VAC
        if not NC2(c):
            E = c.E
            empt = [(a, b) for (a, b) in p.C if not E.sol(a, b)]
            return ("Ans_p is not constant on C (values %s), and the lookup E_lk fails NC2: its background component makes Sol_E empty at %s, so E_lk's answer is ⊥ there and "
                    "no contrast of the kind NC2 names appears. FC23 (b) needs a lookup whose other components are satisfiable.\n%s\n%s\n%s"
                    % (sorted(vals, key=repr), show_pairs(empt), p.describe(), p.D.describe(), c.describe()))
        return None

    def cb2(m):
        p, c = m
        vals = set(p.ans(a, b) for (a, b) in p.C)
        if len(vals) < 2 or any(not c.E.sol(a, b) for (a, b) in p.C):
            return VAC
        if not NC2(c):
            return "satisfiable lookup without NC2\n%s\n%s" % (p.describe(), c.describe())
        return None

    parts.append(forall(S, "FC23", 1, "(a) NC1 fails for the lookup", "Ans_p determined on C ⇒ some component of E_lk is an answer slot", gen, ca, SMALL, 60, BOTHFAM))
    parts.append(forall(S, "FC23", 2, "(b) as stated", "Ans_p not constant on C ⇒ NC2(E_lk) with G = {k}", gen, cb, SMALL, 80, BOTHFAM))
    parts.append(forall(S, "FC23", 3, "(b) with satisfiable background", "Ans_p not constant on C ∧ Sol_E(τa,σb) ≠ ∅ on C ⇒ NC2(E_lk)", gen, cb2, SMALL, 80, BOTHFAM))
    # Area 2 (c): the readers' lookups M1-M3 (the ruling L255-L257), under D6.3 as registered and as rewritten (A2-01).
    # S106 (S44, S45): NC1 is no longer a conjunct of (E); M1-M3 have slots under D6.3 as rewritten and meet (E).
    rows, ok = [], True
    for name, (c, ans) in area2_lookups().items():
        nc1_reg, nc1_new = NC1(c, "registered"), NC1(c, "area2")
        acc, acc_r3 = account(c), _acc_with(c, "area2", "r3")
        rows.append("%s: NC1 as registered %s, as rewritten (A2-01) %s; (E) after S106 %s; round 3's (E) %s; answers %s" % (name, nc1_reg, nc1_new, acc, acc_r3, ans))
        ok = ok and nc1_reg and not nc1_new and acc and not acc_r3
    parts.append(computed("(c) area 2: restating lookups", "M1 (a slot with a pin beside it), M2 (a slot sheltered by an undetermined pair), M3 (one component on two ports) fail NC1 as rewritten (D6.3: slots) and meet (E) after S106 (round 3's (E) excluded them)",
                          ok, "; ".join(rows)))
    # Area 2 (d): the quantifier left open (A2-02): M5, a target whose answer is fixed at each pair by a different component.
    D5 = _org("D", ["y"], {"y": (1, 2)}, ["ca", "cb"], {"ca": ["y"], "cb": ["y"]}, ["b0"], [ONE, "e"],
              {("ca", "e", "b0"): {(2,)}, ("cb", ONE, "b0"): {(1,)}})
    p5 = Question(D5, [(ONE, "b0"), ("e", "b0")], "b0", PortQuery(), "y")
    c5 = Candidate(D5, p5, _T("y"), {ONE: ONE, "e": "e"}, {"b0": "b0"},
                   {"ca": (frozenset(["ca"]), _T("y")), "cb": (frozenset(["cb"]), _T("y"))}, ["ca", "cb"], "y")
    parts.append(look("(d) area 2: the slot quantifier (A2-02; R3-Q1, answered by S44, S45)", "M5 (the answer asserted at each pair by a different component) meets (E) under A2-01's every-determined-pair test",
                      _acc_with(c5, "area2"), "Acc under A2-01: %s; under D6.3 as registered: %s. After S106 (E) reads no slot, so no reading of the quantifier changes it (FC23.new1 (h))." % (_acc_with(c5, "area2"), _acc_with(c5, "registered"))))

    # S106 (e): the lookup E_lk ('p because p', L273) meets (E) on some models
    def ce(m):
        p, c = m
        if account(c):
            return "E_lk meets (E) after S106 (NC1 %s, a slot: %s)\n%s\n%s\n%s" % (NC1(c), [k for k in c.E.comps if slot(c, k)], p.describe(), p.D.describe(), c.describe())
        return None

    parts.append(exists(S, "FC23", 5, "(e) S106: a lookup E_lk meets (E)", "there is an E_lk (an answer slot, NC1 failing) meeting (E) after S106", gen, ce, SMALL, 200, BOTHFAM, ["I101"]))
    return parts


def _org(name, ports, dom, comps, foot, B, A_, rel):
    """rel: (j, a, b) -> relation; missing -> the full relation."""
    box = {}

    def Lfun(j, a, b):
        if (j, a, b) in rel:
            return frozenset(rel[(j, a, b)])
        return box["o"].full(j)
    box["o"] = Org(name, ports, dom, comps, foot, B, A_, lambda a2, a1: None, Lfun)
    return box["o"]


def _T(*ps):
    return {v: Translation([v]) for v in ps}


def _acc_with(c, reading, account_reading=None):
    """Acc with NC1 read as `reading`; account_reading "r3" gives round 3's (E), in which NC1 is a conjunct (S106:
    after S106 NC1_READING changes no Acc value)."""
    from . import core as _core
    old = _core.NC1_READING
    _core.NC1_READING = reading
    try:
        return account(c, reading=account_reading)
    finally:
        _core.NC1_READING = old


def area2_lookups():
    """The readers' models M1-M3 of the ruling L255-L257 (GLM part 6; Mimo part 6), rebuilt."""
    out = {}
    D = _org("D", ["p0", "p2"], {"p0": (0, 1), "p2": (0, 1)}, ["c0", "c2"], {"c0": ["p0"], "c2": ["p2"]}, ["b0"], [ONE, "e1"],
             {("c0", ONE, "b0"): {(0,)}, ("c0", "e1", "b0"): {(1,)}, ("c2", ONE, "b0"): {(0,)}, ("c2", "e1", "b0"): {(0,)}})
    p = Question(D, [(ONE, "b0"), ("e1", "b0")], "b0", PortQuery(), "p0")
    E = _org("E", ["p0", "p2"], {"p0": (0, 1), "p2": (0, 1)}, ["k", "m"], {"k": ["p0", "p2"], "m": ["p2"]}, ["b0"], [ONE, "e1"],
             {("k", ONE, "b0"): {(0, 0)}, ("k", "e1", "b0"): {(1, 0)}, ("m", ONE, "b0"): {(0,)}, ("m", "e1", "b0"): {(0,)}})
    out["M1 decorated lookup"] = (Candidate(E, p, _T("p0", "p2"), {ONE: ONE, "e1": "e1"}, {"b0": "b0"},
                                            {"k": (frozenset(["c0", "c2"]), _T("p0", "p2")), "m": (frozenset(["c2"]), _T("p2"))}, ["k", "m"], "p0"),
                                  (p.ans(ONE, "b0"), p.ans("e1", "b0")))
    D = _org("D", ["p0", "p1"], {"p0": (0, 1), "p1": (0, 1)}, ["c0", "c1"], {"c0": ["p0"], "c1": ["p1"]}, ["b0"], [ONE, "e1"],
             {("c0", ONE, "b0"): {(0,)}, ("c1", ONE, "b0"): {(0,)}, ("c1", "e1", "b0"): set()})
    p = Question(D, [(ONE, "b0"), ("e1", "b0")], "b0", PortQuery(), "p0")
    E = _org("E", ["p0", "p1"], {"p0": (0, 1), "p1": (0, 1)}, ["k", "bg"], {"k": ["p0"], "bg": ["p1"]}, ["b0"], [ONE, "e1"],
             {("k", ONE, "b0"): {(0,)}, ("bg", ONE, "b0"): {(0,)}, ("bg", "e1", "b0"): set()})
    out["M2 lookup under I83"] = (Candidate(E, p, _T("p0", "p1"), {ONE: ONE, "e1": "e1"}, {"b0": "b0"},
                                            {"k": (frozenset(["c0"]), _T("p0")), "bg": (frozenset(["c1"]), _T("p1"))}, ["k"], "p0"),
                                  (p.ans(ONE, "b0"), p.ans("e1", "b0")))
    D = _org("D", ["p0", "p1"], {"p0": (0, 1), "p1": (0, 1)}, ["c0", "c1"], {"c0": ["p0"], "c1": ["p1"]}, ["b0"], [ONE, "e1"],
             {("c0", ONE, "b0"): {(0,)}, ("c0", "e1", "b0"): {(1,)}, ("c1", ONE, "b0"): {(0,)}, ("c1", "e1", "b0"): {(1,)}})
    p = Question(D, [(ONE, "b0"), ("e1", "b0")], "b0", PortQuery(), "p0")
    E = _org("E", ["p0", "p1"], {"p0": (0, 1), "p1": (0, 1)}, ["k"], {"k": ["p0", "p1"]}, ["b0"], [ONE, "e1"],
             {("k", ONE, "b0"): {(0, 0)}, ("k", "e1", "b0"): {(1, 1)}})
    out["M3 one component on two ports"] = (Candidate(E, p, _T("p0", "p1"), {ONE: ONE, "e1": "e1"}, {"b0": "b0"},
                                                      {"k": (frozenset(["c0", "c1"]), _T("p0", "p1"))}, ["k"], "p0"),
                                            (p.ans(ONE, "b0"), p.ans("e1", "b0")))
    return out


@claim("FC24", ["I77", "I78", "I81", "I83", "I79"])
def fc24(S):
    def gen(rng, size):
        D, p = D_and_p(rng, size)
        if any(p.ans(a, b) is BOT for (a, b) in p.C):
            return None
        c = gen_lookup(rng, p, background=False)
        # add a commitment that answers another question: a copy of a D component on another port
        others = [j for j in p.D.comps if p.deltaD not in p.D.foot[j]]
        if not others:
            return None
        j = rng.choice(others)
        E = c.E
        ports = list(E.ports) + [v for v in p.D.foot[j] if v not in E.ports]
        dom = {v: p.D.dom[v] for v in ports}
        comps = list(E.comps) + ["k2"]
        foot = dict(E.foot)
        foot["k2"] = p.D.foot[j]
        E2 = Org("E_lk+", ports, dom, comps, foot, E.B, E.A, E._compose, lambda jj, a, b: (E.L(jj, a, b) if jj != "k2" else p.D.L(j, a, b)))
        lam = dict(c.lam)
        lam["k2"] = (frozenset([j]), {v: Translation((v,)) for v in foot["k2"]})
        return p, c.replace(E=E2, lam=lam, Gamma=("k", "k2"), pi={v: Translation((v,)) for v in ports})

    def check(m):
        p, c = m
        if NC1(c):
            return "NC1 holds after adding a commitment\n" + c.describe()
        return None

    return [forall(S, "FC24", 1, "packaging another dependence leaves the slot", "E_lk with an added commitment still fails NC1", gen, check, SMALL, 60, BOTHFAM),
            not_tested("L273's 'an account' names a candidate", "reading of the word 'account' at L273", "a reading of wording; S106: L273 is replaced by a pointer to D6.3, FC23 and FC24 (S106-T6), and the slot left in place is content (D6.3), not a failure of (E)")]


def table_candidate(p, U, encode=False):
    D, b0 = p.D, p.b0
    Eports = [v for v in D.ports if v in U]
    dom = {v: D.dom[v] for v in Eports}
    table = {}
    for a in D.A:
        for b in D.B:
            src = (a, b) if encode else (ONE, b0)
            table[("tab", a, b)] = D.proj(D.sol(*src), D.ports, Eports)
    E = Org("E_tab" if not encode else "E_enc", Eports, dom, ["tab"], {"tab": tuple(Eports)}, D.B, D.A, D._compose, lambda j, a, b: table[(j, a, b)])
    lam = {"tab": (frozenset(D.comps), {v: Translation((v,)) for v in Eports})}
    delta = p.deltaD if p.deltaD in Eports else Eports[0]
    return Candidate(E, p, {v: Translation((v,)) for v in Eports}, {a: a for a in D.A}, {b: b for b in D.B}, lam, ["tab"], delta, name=E.name)


@claim("FC25", ["I77", "I78", "I80", "I101"])
def fc25(S):
    parts = []

    def gen(rng, size, covered=True):
        D, p = D_and_p(rng, size, family="G-surg")
        fp = set(v for j in D.comps for v in D.foot[j])
        if covered and fp != set(D.ports):
            return None
        if not covered and fp == set(D.ports):
            return None
        U = [v for v in D.ports if rng.random() < 0.7] or [p.deltaD]
        return p, U

    def ca(m):
        p, U = m
        c = table_candidate(p, U)
        D = p.D
        for (a, b) in p.C:
            moves = D.proj(D.sol(a, b), D.ports, c.E.ports) != D.proj(D.sol(ONE, p.b0), D.ports, c.E.ports)
            if F1_at(c, a, b) == moves:
                return "F1 at (%s,%s) is %s and the projection %s\n%s\n%s\n%s" % (a, b, F1_at(c, a, b), "moves" if moves else "does not move", p.describe(), D.describe(), c.describe())
        return None

    parts.append(forall(S, "FC25", 1, "(a) E_tab's F1", "F1 at (a,b) for E_tab ⟺ the projection of Sol_D on its ports is that at (1,b0)",
                        gen, ca, SMALL, 40, ["G-surg"], note="targets whose every port lies in a footprint"))

    def cw(m):
        p, U = m
        c = table_candidate(p, U)
        R = Roles(p.D)
        D = p.D
        setting = [(a, b) for (a, b) in p.C if a != ONE and a.startswith("[") and "alt" not in a
                   and any(a in R.Set[v] and len(D.dom[v]) >= 2 for v in D.ports)]
        if setting and F1(c) and proper_D(D):
            return ("L269 says a table of observed answers 'fails (F1) under any contract containing' an intervention. Here C contains the setting edits %s "
                    "and E_tab meets (F1) on C: none of them moves the projection of Sol_D on the table's ports.\n%s\n%s\n%s"
                    % (show_pairs(setting), p.describe(), p.D.describe(), c.describe()))
        return None

    parts.append(exists(S, "FC25", 2, "(a) a setting edit that leaves the table faithful",
                        "there is a contract holding a setting edit (of a port with two values or more) on which E_tab meets (F1)", gen, cw, SMALL, 200, ["G-surg"], ["I80", "I101"],
                        note="proper models only"))

    def cb(m):
        p, U = m
        c = table_candidate(p, U, encode=True)
        return None if F1(c) else "E_enc fails F1\n%s\n%s\n%s" % (p.describe(), p.D.describe(), c.describe())

    parts.append(forall(S, "FC25", 3, "(b) E_enc meets F1", "E_enc meets (F1) on every C", gen, cb, SMALL, 40, ["G-surg"], note="targets whose every port lies in a footprint"))

    def cb_unc(m):
        p, U = m
        D = p.D
        fp = set(v for j in D.comps for v in D.foot[j])
        U2 = sorted(set(U) | (set(D.ports) - fp), key=D.ports.index)
        c = table_candidate(p, U2, encode=True)
        if F1(c):
            return None
        return ("E_enc (I32: λ(k) = the whole target, projected on k's ports) fails (F1): its ports include %s, which lies in no footprint of D, "
                "so it is not a port of the subnetwork J_D (D1.4 and I14 build V_N from footprints) and no port translation can reach it; "
                "the value of such a port is free in Sol_D and the table records it, but proj^λ cannot. FC25 (b) holds only where every port of D lies in some footprint.\n%s\n%s\n%s"
                % (sorted(set(D.ports) - fp), p.describe(), D.describe(), c.describe()))

    parts.append(forall(S, "FC25", 4, "(b) with a port of D in no footprint", "E_enc meets (F1) on every C, D having a port in no footprint",
                        lambda rng, size: gen(rng, size, covered=False), cb_unc, SMALL, 40, ["G-surg"]))
    return parts


# ---- the pole ---------------------------------------------------------------------------------------

@claim("FC26", ["I92", "I85", "I79"])
def fc26(S):
    D = pole()
    C1, C2, C2s = pole_contracts(D)
    parts = []
    for nm, C in (("C1", C1), ("C2", C2)):
        p = Question(D, C, "b1_45", PortQuery(), "L", name=nm)
        v, d = account(pole_fwd_candidate(p), detail=True)
        parts.append(computed("forward organization on %s" % nm, "E_fwd meets (F1), (F2), (A), NC1, NC2 and non-vacuity on %s" % nm, v and d["NC1"], "conjuncts: %s (S106: (E) is (F1), (F2), (A), Dependence = NC2 and non-vacuity; NC1 holds too)" % d, ["I92", "I85"]))
    C3 = frozenset([(ONE, "b1_45")] + [(a, "b1_45") for a in single_settings(D, ["L"])])
    p3 = Question(D, C3, "b1_45", PortQuery(), "L", name="C3")
    c3 = pole_fwd_candidate(p3)
    v, d = account(c3, detail=True)
    w = NC2(c3, witness=True)
    parts.append(look("a contract whose only non-baseline edits set L", "the look: on it c_L is an answer slot and NC1 fails for the forward organization",
                      not d["NC1"], "conjuncts on C3 = the baseline plus the settings of L: %s. NC1 holds: c_L is no answer slot at the baseline pair, and D6.3 asks for a slot at every pair of C. NC2 holds too (witness %s): deleting c_L frees L at a setting pair as well, since a deleted component imposes the full relation under every edit (D1.3), so the answer determined there is lost. The forward organization meets (E) on C3." % (d, w), ["I92"]))
    return parts


@claim("FC27", ["I92"])
def fc27(S):
    D = pole()
    C1, C2, C2s = pole_contracts(D)
    p = Question(D, C1, "b1_45", PortQuery(), "L", name="p_prod")
    r = pole_rev_candidate(p)
    bad = []
    for (a, b) in sorted(C1, key=repr):
        sm = dict(D.meta["inv"][a])
        if "H" in sm and sm["H"] != 1:
            ok = F2eq_at(r, a, b)
            L_D = sorted(set(z[2] for z in D.sol(a, b)), key=float)
            L_E = sorted(set(z[2] for z in r.E.sol(a, b)), key=float)
            bad.append((a, ok, L_D, L_E))
    ok = all(not x[1] for x in bad)
    parts = [computed("the reversed calculation fails (F2) at setH := h ≠ u_H", "F2eq fails for E_rev at (set H := h, b0) with h ≠ u_H",
                      ok, "; ".join("%s: F2eq %s, L in π[Sol_D] %s, L in Sol_E %s" % x for x in bad) + ". Account on C1: %s." % (account(r, detail=True)[1],), ["I92"])]
    # Area 2: Mimo's transport τ' (part 7, reply line 73): set H := h carried to a setting of E_rev's L (to h·cot θ, θ as
    # the edit sets it or b0's 45°), set θ := t to set(θ = t, L = ·). τ' is defined on every edit of D.
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
        key = tuple(sorted(new.items()))
        return lab.get(key)

    t2 = {a: tau2(a) for a in D.A}
    t2 = {a: x for a, x in t2.items() if x is not None}
    r2 = r.replace(tau=t2, name="ℰ_rev under τ'")
    f2eq_C1 = all(F2eq_at(r2, a, b) for (a, b) in C1)
    v2, d2 = account(r2, detail=True)
    slots = [k for k in r2.E.comps if slot(r2, k)]
    parts.append(look("area 2: Mimo's τ' (set H := h carried to a setting of L)", "under τ' E_rev meets the valuation equation of (F2) at every pair of C1, fails the homomorphism clause of (F2), and fails NC1 (r_L a slot)",
                      f2eq_C1 and not d2["Hom"] and not d2["NC1"],
                      "F2eq at every pair of C1: %s; conjuncts %s; slots %s. So the lever moves only the pointwise equation: (F2)'s homomorphism clause (L242) still excludes the reversed calculation on the production contract; NC1 fails too, and after S106 it is not a conjunct of (E)."
                      % (f2eq_C1, d2, slots), ["I92", "I84"]))
    return parts


@claim("FC28", ["I92"])
def fc28(S):
    parts = []
    bounds = [(1, 45), (2, 45), (3, 45)]
    D = pole(bounds=bounds)
    C = frozenset((ONE, b) for b in D.B)
    p = Question(D, C, "b1_45", fibre_query(), ("H", "T", "L"), name="p_ident")
    r = pole_rev_candidate(p, delta=("H", "T", "L"))
    res = dict(F1=F1(r), F2=F2(r), A=A(r))
    parts.append(computed("identification contract: boundaries varying u_H", "E_rev with τ, σ the identity meets (F1), (F2), (A)", all(res.values()),
                          "%s; answers (target, E_rev): %s" % (res, {b: (sorted(p.ans(ONE, b)), sorted(r.ans_E(ONE, b))) for b in D.B}), ["I92"]))
    C2 = C | frozenset((a, "b1_45") for a in single_settings(D, ["L"]))
    p2 = Question(D, C2, "b1_45", fibre_query(), ("H", "T", "L"), name="p_ident_setL")
    r2 = pole_rev_candidate(p2, delta=("H", "T", "L"))
    res2 = dict(F1=F1(r2), F2=F2(r2), A=A(r2))
    rows = []
    for a in single_settings(D, ["L"]):
        rows.append("%s: target fibre %s, E_rev %s, F1 %s, F2eq %s" % (a, sorted(p2.ans(a, "b1_45")) if p2.ans(a, "b1_45") is not BOT else "⊥",
                                                                    "⊥" if r2.ans_E(a, "b1_45") is BOT else sorted(r2.ans_E(a, "b1_45")), F1_at(r2, a, "b1_45"), F2eq_at(r2, a, "b1_45")))
    every_H = any(p2.ans(a, "b1_45") == frozenset(D.dom["H"]) for a in single_settings(D, ["L"]))
    parts.append(look("with edits that set L (replacing c_L)", "the look: D's fibre over the set value is every H, and (A) fails for E_rev",
                      every_H and not res2["A"],
                      "%s. Rows: %s. With this program's fibre query (the fibre over the single value of (θ, L) in Sol, I92) the target's fibre at a setting of L is {l·tan θ} ∩ X_H, not every H. (A) fails where that set is empty: E_rev, whose own c'_H still imposes H = L tan θ, then has no solution and answers ⊥, while the target answers the empty fibre. (F1) and (F2) fail at every setting of L: E_rev's c'_H is not replaced by the setting, D's c_L is." % (res2, "; ".join(rows)), ["I92"]))
    # Area 2 (E1 settled at L325): C_id := {1} × B, every boundary (u_H and u_θ varying), no setting edit.
    Dall = pole()
    Cid = frozenset((ONE, b) for b in Dall.B)
    pid = Question(Dall, Cid, "b1_45", fibre_query(), ("H", "T", "L"), name="p_ident_all")
    rid = pole_rev_candidate(pid, delta=("H", "T", "L"))
    res3 = dict(F1=F1(rid), F2=F2(rid), A=A(rid))
    parts.append(computed("area 2: C_id = {1} × B (u_H and u_θ both varying)", "E_rev with τ, σ the identity meets (F1), (F2), (A) on C_id",
                          all(res3.values()), "%s on the %d boundaries" % (res3, len(Dall.B)), ["I92"]))
    setT = [a for a in single_settings(Dall, ["T"]) if dict(Dall.meta["inv"][a])["T"] == 60][0]
    pid2 = Question(Dall, Cid | {(setT, "b1_45")}, "b1_45", fibre_query(), ("H", "T", "L"), name="p_ident_all+setT")
    rid2 = pole_rev_candidate(pid2, delta=("H", "T", "L"))
    parts.append(look("area 2: C_id plus one setting of θ (GLM part 7, reply line 111)", "one setting edit in the identification contract makes (F1) fail for E_rev",
                      not F1(rid2), "F1 at (%s, b1_45): %s; F1 on the contract: %s" % (setT, F1_at(rid2, setT, "b1_45"), F1(rid2)), ["I92"]))
    # Second check (R4): is p_ident on C_id an identification question by D3.3 (L151)?
    iL = Dall.ports.index("L")

    def obs(a, b):
        vals = set(z[iL] for z in Dall.sol(a, b))
        return next(iter(vals)) if len(vals) == 1 else None

    fibre = str(getattr(pid.Q, "name", "")).startswith("Q_fib")  # the fibre query of E1 (cases.fibre_query)
    varies = len(set(obs(a, b) for (a, b) in Cid)) > 1
    edit_alters = any(a != ONE and any(obs(a, b) != obs(ONE, b) for b in Dall.B) for (a, b) in Cid)
    parts.append(computed("second check (R4): C_id is an identification contract under D3.3", "Ident(p) :⟺ Q returns a fibre ∧ ∃(a,b),(a',b') ∈ C: obs(a,b) ≠ obs(a',b') (I163) holds on C_id; D3.3 read as an edit a ≠ 1 of C altering obs does not",
                          fibre and varies and not edit_alters,
                          "Q a fibre: %s; observed L over C_id: %s (varies: %s); an edit a ≠ 1 in C_id altering the observed L: %s" % (fibre, sorted(set(obs(a, b) for (a, b) in Cid)), varies, edit_alters), ["I92", "I163"]))
    return parts


@claim("FC29", ["I77", "I78", "I81"])
def fc29(S):
    def check(m):
        p, c = m
        w = NC2(c, witness=True)
        if w is None:
            return VAC
        (a, b), G = w
        x0 = (ONE, c.sigma[p.b0])
        if not contrast(c.ans_E(c.tau[a], c.sigma[b]), c.ans_E(*x0)):
            return "NC2 witnessed off τ[C]\n" + c.describe()
        return None

    return [forall(S, "FC29", 1, "NC2's contrast lies on τ[C]", "NC2 ⇒ a contrast at some (τa,σb) with (a,b) ∈ C", gen_p_cand, check, SMALL, 40, BOTHFAM)]


@claim("FC30", [])
def fc30(S):
    import inspect
    from . import core
    src = inspect.getsource(core.account)
    return [construction("Acc takes no assessor, history or provenance", "Acc is a function of (D, C, b0, Q, δ, E, t, Γ, Σ, ℓ)", True,
                         "core.account(cand) reads cand.E, cand.p (D, C, b0, Q, δ_D, Σ), cand.pi/tau/sigma/lam, cand.Gamma, cand.deltaE only; the model has one grain.")]


@claim("FC31", [])
def fc31(S):
    # S107 round 4, area 1 (N2: B-N2, W-N2, S-N2, C-N2): re-based; L61's phrase was replaced in round 3 (R3A1-T1), and
    # L520 writes (E)'s five conjuncts (round 2, A3-L520.1; S106-T12). The part's label is kept.
    return [not_tested("five conjuncts, four headings, L520's sources", "counting and reading of L231, L520, L536", "a reading of wording, not a model property")]


@claim("FC32", [])
def fc32(S):
    """Second check (R5): L526 now points to D18.1 for (E)'s ancestors, and D18.1's graph is the program's DEP.
    (1) every argument of Acc (FC30's list) is (O), (Q), an index, a declared input or δ, and each is an
    ancestor of (E) in DEP; t and Γ are the candidate's own data, as for (F1), (F2), (A). (2) DEP's edges for
    NonCircular and NonVacuous are the classes of symbols core's NC1, NC2 and nonvacuous read (a scan).
    S106 (S44, S45): (E)'s fourth conjunct is Dependence := NC0 ∧ NC2 (D6.5); its edges are the classes NC2 and dep
    read, and ℓ, which only NC1's 'at the declared grain' read (I28), is no longer an argument of Acc (D6.7) nor an
    edge of Dependence (D18.1); NC1 is the node Slot (D6.3), not an ancestor of (E)."""
    import inspect
    from . import core
    from .claims_b import DEP

    def ancestors(n):
        seen, todo = set(), [n]
        while todo:
            u = todo.pop()
            for x in DEP.get(u, []):
                y = x[1] if isinstance(x, tuple) else x
                if y not in seen:
                    seen.add(y)
                    todo.append(y)
        return seen

    acc_args = {"D": "(O)", "E": "(O)", "C": "C", "b0": "(Q)", "Q": "(Q)", "δ": "δ", "Σ": "Σ"}  # S106: ℓ dropped (D6.7)
    anc = ancestors("(E)")
    miss = sorted(set(v for v in acc_args.values() if v not in anc))
    # NC2 reads the designation δ_E through Candidate.ans_E (the query at δ_E), so its source is scanned too
    src_nc = "".join(inspect.getsource(f) for f in (core.contrast, core.lost, core.NC2, core.dep, core.Candidate.ans_E))
    src_nv = inspect.getsource(core.nonvacuous)

    def classes(src):
        out = set()
        for tok, cl in ((".sol(", "(O)"), (".L(", "(O)"), (".delete(", "(O)"), (".foot", "(O)"), (".ans(", "(Q)"), (".ans_E(", "(Q)"), (".Q", "(Q)"),
                        (".C", "C"), ("deltaE", "δ"), (".excl", "Σ"), ("sig_", "(K)"), ("one_kind", "(K)")):
            if tok in src:
                out.add(cl)
        return out

    nc_code, nv_code = classes(src_nc), classes(src_nv)
    nc_dep, nv_dep = set(DEP["Dep"]), set(DEP["NV"])
    return [computed("(1) Acc's arguments are ancestors of (E) in D18.1 (L526 points there)", "every argument of Acc other than the candidate's own t and Γ maps to an ancestor of (E)",
                     not miss, "Acc's arguments → nodes: %s; ancestors of (E): %s; missing: %s; ℓ an ancestor of (E): %s; Slot an ancestor of (E): %s" % (acc_args, sorted(anc), miss or "none", "ℓ" in anc, "Slot" in anc)),
            computed("(2) D18.1's Dependence and NonVacuous edges are what the program reads", "classes read by NC2 and dep = DEP['Dep'] (S106: no ℓ); by nonvacuous = DEP['NV']",
                     nc_code == nc_dep and nv_code == nv_dep, "Dependence: code %s, D18.1 %s; NV: code %s, D18.1 %s. No signature (K) is read." % (sorted(nc_code), sorted(nc_dep), sorted(nv_code), sorted(nv_dep)))]


@claim("FC33", ["I77", "I78", "I81", "I70"])
def fc33(S):
    def gen(rng, size):
        p, c = gen_p_cand(rng, size)
        return p, c, rng

    def check(m):
        p, c, rng = m
        E = c.E
        pm = {v: v + "'" for v in E.ports}
        cm = {k: k + "'" for k in E.comps}
        icm = {v: k for k, v in cm.items()}
        E2 = Org(E.name + "'", [pm[v] for v in E.ports], {pm[v]: E.dom[v] for v in E.ports}, [cm[k] for k in E.comps],
                 {cm[k]: tuple(pm[v] for v in E.foot[k]) for k in E.comps}, E.B, E.A, E._compose, lambda j, a, b: E.L(icm[j], a, b))
        pi2 = {pm[v]: c.pi[v] for v in E.ports}
        lam2 = {cm[k]: (N, {pm[v]: tr[v] for v in E.foot[k]}) for k, (N, tr) in c.lam.items()}
        c2 = c.replace(E=E2, pi=pi2, lam=lam2, Gamma=tuple(cm[k] for k in c.Gamma), deltaE=pm[c.deltaE])
        if account(c) != account(c2):
            return "renaming changed Acc\n" + c.describe()
        return None

    return [forall(S, "FC33", 1, "(a) Acc is kept by renaming E's components and ports", "Acc(ℰ') = Acc(ℰ) for a renamed copy with t, δ, Γ carried along",
                   gen, check, SMALL, 40, BOTHFAM, ["I70"]),
            not_tested("(b) which conjuncts inspect a declared statement or a grain", "non-vacuity's scope clause and NC1's grain", "a reading of the conjuncts' arguments; see FC30. S106: NC1 is not a conjunct, so no conjunct reads the grain; the scope clause is the one exception L265 names")]


@claim("FC34", ["I77", "I78", "I81", "I85", "I101", "I79"])
def fc34(S):
    parts = []

    def gen(rng, size):
        D, p = D_and_p(rng, size, proper=True)
        if D is None:
            return None
        c = gen_candidate(rng, p, perturb_p=0.1, background_p=0.1, demote_p=0.0, random_tau_p=0.0)
        sub = [x for x in p.C if x == (ONE, p.b0) or rng.random() < 0.5]
        p2 = p.with_C(sub)
        return p, p2, c

    def narrow(m):
        p, p2, c = m
        c2 = c.replace(p=p2)
        if account(c) != account(c2):
            return ("Acc on C: %s; on C' ⊆ C: %s\n%s\n%s\n%s\n%s" % (account(c), account(c2), p.describe(), p2.describe(), p.D.describe(), c.describe()))
        return None

    parts.append(exists(S, "FC34", 1, "narrow reading: Acc on one question and not the other", "there are p, p' (same D) and ℰ with Acc on exactly one", gen, narrow, SMALL, 200, BOTHFAM, ["I101"], note="proper models only"))

    def wide(m):
        p, p2, c = m
        c2 = c.replace(p=p2)
        if p2.C != p.C and account(c) and account(c2):
            return ("A candidate meeting (E) on two different questions with one target (C' ⊊ C): an instance against the wide reading (I73's alternative).\n%s\n%s\n%s\n%s"
                    % (p.describe(), p2.describe(), p.D.describe(), c.describe()))
        return None

    parts.append(exists(S, "FC34", 2, "wide reading: a candidate meeting (E) on both", "there are p ≠ p' with one D and ℰ with Acc on both (against the wide reading)", gen, wide, SMALL, 300, BOTHFAM, ["I73", "I101"], note="proper models only"))

    def mono_down(m):
        p, p2, c = m
        c2 = c.replace(p=p2)
        if account(c) and not account(c2):
            return "Acc on C, not on C' ⊆ C\n%s\n%s\n%s\n%s" % (p.describe(), p2.describe(), p.D.describe(), c.describe())
        return None

    def mono_up(m):
        p, p2, c = m
        c2 = c.replace(p=p2)
        if account(c2) and not account(c):
            return "Acc on C' ⊆ C, not on C\n%s\n%s\n%s\n%s" % (p.describe(), p2.describe(), p.D.describe(), c.describe())
        return None

    parts.append(exists(S, "FC34", 3, "Acc not antitone in C", "there are C' ⊆ C with Acc on C and not on C'", gen, mono_down, SMALL, 300, BOTHFAM, ["I101"], note="proper models only"))
    parts.append(exists(S, "FC34", 4, "Acc not monotone in C", "there are C' ⊆ C with Acc on C' and not on C", gen, mono_up, SMALL, 300, BOTHFAM, ["I101"], note="proper models only"))

    def nc1(m):
        p, p2, c = m
        c2 = c.replace(p=p2)
        if NC1(c) and not NC1(c2):
            return "NC1 holds on C and fails on C' ⊆ C\n%s\n%s\n%s\n%s" % (p.describe(), p2.describe(), p.D.describe(), c.describe())
        return None

    parts.append(exists(S, "FC34", 5, "NC1 can fail on C' while holding on C", "there are C' ⊆ C with NC1 on C and not on C'", gen, nc1, SMALL, 400, BOTHFAM, ["I101"], note="proper models only"))
    return parts


@claim("FC35", [])
def fc35(S):
    return [not_tested("L151's 'prediction'", "whether L151's use lies inside L219's definition", "a question of which lines a definition covers (I51)")]


@claim("FC36", ["I72"])
def fc36(S):
    # a production question whose output port has the domain {reachable, unreachable}
    dom = {"v": (0, 1), "w": ("reachable", "unreachable")}
    foot = {"h_v": ("v",), "h_w": ("v", "w")}

    def Lf(j, a, b):
        if j == "h_v":
            return {(1,)} if a == ONE else {(int(a[-1]),)}
        return {(0, "unreachable"), (1, "reachable")}

    D = Org("D_po", ["v", "w"], dom, ["h_v", "h_w"], foot, ["b0"], [ONE, "set_v0", "set_v1"], lambda a2, a1: a2, Lf)
    R = Roles(D)
    prod = R.output("w", "h_w") and R.upstream("v", "w") and any(a in R.Set["v"] for a in ("set_v0", "set_v1"))  # D3.3 as fixed (area 1)
    obst = set(D.dom["w"]) == {"reachable", "unreachable"}
    return [computed("production and obstruction at once", "a query can meet two respects' sufficient conditions (I72)", prod and obst,
                     "Q reads w, an output of h_w, C holds settings of v upstream of w (Prod: %s), and Y_p = {reachable, unreachable} (Obst: %s)." % (prod, obst), ["I72"]),
            construction("respects are carried by renamings", "Prod, Obst are functions of (D, Q, δ, C)", True, "they read only D's relations, A, the designated port's domain and C")]
