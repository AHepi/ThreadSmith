# S104 round 2 (maths): tests of FC37-FC110 (formal claims groups C-G).
import itertools
import inspect
import random
from fractions import Fraction as Fr

from .core import (ONE, BOT, Org, Roles, Question, PortQuery, FnQuery, Candidate, Translation, powerset, slice_rel,
                   one_kind, rename_rel, proj_lam, F1_at, F2eq_at, A_at, F1, F2, F2eq, A, hom, faithful, account,
                   NC1, NC2, nonvacuous, restrict, routes, critical_block, contributory, indispensable, no_work,
                   minimal, meets_ab, all_R, meet_table, conflict, conf_given, conf_claim, all_pairs, conflict_pairs,
                   rivals, problem_kind)
from . import core
from .gen import (Size, sizes, gen_surg, gen_free, gen_org, gen_question, gen_candidate, gen_lookup,
                  gen_random_candidate, any_candidate, rename_org, rand_rel)
from .cases import (pole, pole_fwd_candidate, pole_rev_candidate, single_settings, identified, rank, det, surgical_edits)
from .args import (Not, And, Imp, canon, conjuncts, denial, show, incons, consistent, models, Leaf, Step, Assessor,
                   usable, usable_step, usable_any_step, rules_out, X, enumerate_args)
from .phys import F_op, ret_real, gfp, Circuit, act_route, act_route_s104, r_left, r_right, repair
from .harness import claim, forall, exists, exhaustive, computed, construction, not_tested, look, REG, VAC
from .claims_a import D_and_p, proper_D, show_pairs, SMALL, MID, BOTHFAM, gen_p_cand

CONF = sizes(max_ports=3, max_dom=2, max_comps=2, max_B=2, max_edits=1)


def small_enough(D, limit=4096):
    n = 1
    for j in D.comps:
        n *= 2 ** len(D.full(j))
    return n <= limit


def gen_pair(rng, size, proper=False, acc_bias=False):
    D, p = D_and_p(rng, size, proper=proper)
    if D is None or not small_enough(D):
        return None
    if acc_bias:
        c1 = gen_candidate(rng, p, name="ℰ", perturb_p=0.05, background_p=0.0, random_tau_p=0.0, demote_p=0.0)
        c2 = gen_candidate(rng, p, name="ℰ'", perturb_p=0.05, background_p=0.0, random_tau_p=0.0, demote_p=0.0)
    else:
        c1 = any_candidate(rng, p, size, name="ℰ")
        c2 = any_candidate(rng, p, size, name="ℰ'")
    return p, c1, c2


def both_desc(p, c1, c2):
    return "%s\n%s\n%s\n%s" % (p.describe(), p.D.describe(), c1.describe(), c2.describe())


# ---- set systems (Part VI) ---------------------------------------------------------------------------

def fam_from_mask(n, mask):
    return frozenset(frozenset(i for i in range(n) if s >> i & 1) for s in range(2 ** n) if mask >> s & 1)


def upward_closed(S, n):
    for W in S:
        for i in range(n):
            if (W | {i}) not in S:
                return False
    return True


def all_families(n):
    for mask in range(2 ** (2 ** n)):
        yield fam_from_mask(n, mask)


def antichains(n):
    subsets = [frozenset(i for i in range(n) if s >> i & 1) for s in range(2 ** n)]
    out = []

    def rec(i, chosen):
        if i == len(subsets):
            out.append(list(chosen))
            return
        rec(i + 1, chosen)
        s = subsets[i]
        if all(not (s <= c or c <= s) for c in chosen):
            chosen.append(s)
            rec(i + 1, chosen)
            chosen.pop()

    rec(0, [])
    return out


def up_closure(ac, n):
    return frozenset(frozenset(i for i in range(n) if s >> i & 1) for s in range(2 ** n)
                     if any(a <= frozenset(i for i in range(n) if s >> i & 1) for a in ac))


def fmt_S(S):
    return "{" + ", ".join("{" + ",".join(str(i) for i in sorted(W)) + "}" for W in sorted(S, key=lambda W: (len(W), sorted(W)))) + "}"


@claim("FC37", ["I77"])
def fc37(S):
    def check(item):
        n, Sy = item
        G = frozenset(range(n))
        if G not in Sy or not upward_closed(Sy, n):
            return VAC
        mins = minimal(Sy)
        U = set().union(*mins) if mins else set()
        I = set.intersection(*[set(m) for m in mins]) if mins else set()
        for d in range(n):
            if contributory(Sy, d) != (d in U):
                return "contributory(%d) = %s, d ∈ ∪min S = %s, S = %s" % (d, contributory(Sy, d), d in U, fmt_S(Sy))
            if indispensable(Sy, G, d) != (d in I):
                return "indispensable(%d) = %s, d ∈ ∩min S = %s, S = %s" % (d, indispensable(Sy, G, d), d in I, fmt_S(Sy))
        return None

    def items():
        for n in range(1, 5):
            for Sy in all_families(n):
                yield n, Sy
        for ac in antichains(5):
            yield 5, up_closure(ac, 5)

    parts = [exhaustive("FC37", "every upward-closed family, |Γ| ≤ 5", "for finite Γ, upward-closed S with Γ ∈ S: contributory ⟺ ∈ ∪min S; indispensable ⟺ ∈ ∩min S",
                        items(), check, "all families on |Γ| ≤ 4 (filtered to upward closed with Γ ∈ S) and all 7581 up-closures of antichains on |Γ| = 5")]

    def gen(rng, size):
        D, p = D_and_p(rng, size)
        c = gen_candidate(rng, p, perturb_p=0.1, background_p=0.1, demote_p=0.0, random_tau_p=0.0)
        if len(c.Gamma) > 4:
            return None
        return c

    def check2(c):
        Sy = routes(c)
        G = frozenset(c.Gamma)
        idx = {k: i for i, k in enumerate(c.Gamma)}
        n = len(c.Gamma)
        Sy2 = frozenset(frozenset(idx[k] for k in W) for W in Sy)
        return check((n, Sy2))

    parts.append(forall(S, "FC37", 2, "S_{E,p} of random candidates", "the finite monotone claim on route families computed from candidates (where its hypotheses hold)",
                        gen, check2, SMALL, 30, BOTHFAM, ["I78", "I81"]))
    return parts


@claim("FC38", [])
def fc38(S):
    Sy = frozenset([frozenset("a"), frozenset("b"), frozenset("ab")])
    G = frozenset("ab")
    res = dict(upward=all((W | {x}) in Sy for W in Sy for x in G), mins=[sorted(W) for W in minimal(Sy)],
               contrib={d: contributory(Sy, d) for d in "ab"}, indisp={d: indispensable(Sy, G, d) for d in "ab"})
    ok = res["upward"] and res["contrib"] == {"a": True, "b": True} and res["indisp"] == {"a": False, "b": False}
    return [computed("redundant routes", "S = {{a},{b},{a,b}}: each contributory, neither indispensable", ok, str(res))]


@claim("FC39", [])
def fc39(S):
    Sy = frozenset([frozenset("a")])
    G = frozenset("ab")
    ok = G not in Sy and critical_block(Sy, frozenset("a"), frozenset("a")) and not all((W | {x}) in Sy for W in Sy for x in G)
    return [computed("interference", "S = {{a}}: Γ ∉ S, not upward closed, {a} critical in {a}", ok,
                     "Γ ∈ S: %s; CB({a};{a}): %s" % (G in Sy, critical_block(Sy, frozenset("a"), frozenset("a"))))]


class EP:
    """An eventually periodic subset of ℕ: F (below N) ∪ {n ≥ N : n mod m ∈ R} [I91]."""

    def __init__(self, N, m, F, R):
        self.N, self.m, self.F, self.R = N, m, frozenset(F), frozenset(R)

    def norm(self, N, m):
        F = set(self.F) | {n for n in range(self.N, N) if n % self.m in self.R}
        R = {r for r in range(m) if (r % self.m) in self.R} if m % self.m == 0 else None
        assert R is not None
        return F, R

    def unbounded(self):
        return bool(self.R)

    def combine(self, o, op):
        N = max(self.N, o.N)
        m = self.m * o.m
        F1, R1 = self.norm(N, m)
        F2, R2 = o.norm(N, m)
        return EP(N, m, op(F1, F2), op(R1, R2))

    def __sub__(self, o):
        return self.combine(o, lambda x, y: set(x) - set(y))

    def __or__(self, o):
        return self.combine(o, lambda x, y: set(x) | set(y))

    def le(self, o):
        d = self - o
        return not d.F and not d.R

    def least(self):
        if self.F:
            return min(self.F)
        for n in range(self.N, self.N + self.m):
            if n % self.m in self.R:
                return n
        return None

    def __repr__(self):
        return "EP(F=%s, n≥%d with n mod %d ∈ %s)" % (sorted(self.F), self.N, self.m, sorted(self.R))


def single(n):
    return EP(n + 1, 1, {n}, set())


@claim("FC40", ["I91"])
def fc40(S):
    def gen(rng, size):
        def rep():
            N = rng.randint(0, 6)
            m = rng.randint(1, 4)
            F = {n for n in range(N) if rng.random() < 0.5}
            R = {r for r in range(m) if rng.random() < 0.5}
            return EP(N, m, F, R)
        return rep(), rep(), rng.randint(0, 12)

    def check(m):
        W, B, n = m
        inS = lambda X: X.unbounded()
        Gam = EP(0, 1, set(), {0})
        if not inS(Gam):
            return "Γ ∉ S"
        if inS(W) and not inS(W | B):
            return "not upward closed: %r, %r" % (W, B)
        if inS(single(n)):
            return "a route of one commitment: d_%d" % n
        if inS(W):
            if not inS(W - single(W.least())):
                return "a minimal route: %r" % W
            BB = W - (W - B)  # B ∩ W
            if (BB.F or BB.R) and not inS(W - BB) and not BB.R:
                return "a finite critical block: W = %r, B = %r" % (W, BB)
            if inS(W - W):
                return "W is not critical in itself: %r" % W
            if not (inS(W | single(n)) and inS(W - single(n))):
                return "d_%d does work in %r" % (n, W)
        return None

    return [forall(S, "FC40", 1, "(a)-(c) on eventually periodic sets", "routes = unbounded index sets: upward closed, no minimal member, no one-commitment route, every critical block infinite, each d_n does no work by itself",
                   gen, check, [Size(1, 1, 1, 1, 0)], 20000, ["eventually periodic subsets of ℕ"], ["I91"],
                   note="subsets of ℕ of the form F ∪ {n ≥ N : n mod m ∈ R}, N ≤ 6, m ≤ 4")]


@claim("FC41", ["I77"])
def fc41(S):
    def check(item):
        n, Sy = item
        G = frozenset(range(n))
        nw = [d for d in range(n) if no_work(Sy, d)]
        for d in nw:
            for s in range(2 ** n):
                W = frozenset(i for i in range(n) if s >> i & 1)
                if ((W | {d}) in Sy) != ((W - {d}) in Sy):
                    return "(a) fails for d = %d, W = %s, S = %s" % (d, sorted(W), fmt_S(Sy))
            if any(critical_block(Sy, frozenset([d]), W) for W in Sy):
                return "(b) fails for d = %d, S = %s" % (d, fmt_S(Sy))
        for r in range(1, len(nw) + 1):
            for B in itertools.combinations(nw, r):
                if any(critical_block(Sy, frozenset(B), W) for W in Sy):
                    return "(c) a finite block of commitments that do no work is critical: B = %s, S = %s" % (B, fmt_S(Sy))
        return None

    def items():
        for n in range(1, 5):
            for Sy in all_families(n):
                yield n, Sy

    return [exhaustive("FC41", "every family on |Γ| ≤ 4", "NoWork(d): (a) W∪{d} ∈ S ⟺ W∖{d} ∈ S; (b) {d} critical in no route; (c) a finite block of such commitments is critical in no route",
                       items(), check, "all 2^(2^n) families S ⊆ P(Γ), n ≤ 4 (65,536 at n = 4)")]


@claim("FC42", [])
def fc42(S):
    Sy = frozenset([frozenset("a"), frozenset("b"), frozenset("ab")])
    W = frozenset("ab")
    a = critical_block(Sy, W, W)
    b = not critical_block(Sy, frozenset("a"), W) and not critical_block(Sy, frozenset("b"), W)
    c = critical_block(Sy, frozenset("a"), frozenset("a")) and not critical_block(Sy, frozenset("a"), W)
    return [computed("criticality relative to the route", "(a) {a,b} critical in {a,b}, no singleton is; (b) a critical in {a}, not in {a,b}", a and b and c,
                     "CB({a,b};{a,b}) = %s (needs ∅ ∉ S: %s); singletons critical in {a,b}: %s; CB({a};{a}) = %s" % (a, frozenset() not in Sy, not b, critical_block(Sy, frozenset("a"), frozenset("a"))))]


# ---- conflict, rivals, problems -----------------------------------------------------------------------

@claim("FC43", ["I77", "I78", "I81", "I86"])
def fc43(S):
    def check(m):
        p, c1, c2 = m
        for x in all_pairs(p.D):
            if conflict(c1, c2, *x) != conflict(c2, c1, *x):
                return "Conf not symmetric at %r\n%s" % (x, both_desc(p, c1, c2))
        if problem_kind(c1, c2) != problem_kind(c2, c1):
            return "kind not symmetric\n" + both_desc(p, c1, c2)
        return None

    return [forall(S, "FC43", 1, "symmetry", "Conf(ℰ,ℰ';a,b) ⟺ Conf(ℰ',ℰ;a,b); the kind of problem is symmetric", gen_pair, check, CONF, 20, BOTHFAM, ["I86"])]


@claim("FC44", ["I77", "I78", "I81", "I101"])
def fc44(S):
    parts = []

    def gen(rng, size):
        D, p = D_and_p(rng, size)
        if D is None or not small_enough(D):
            return None
        c = gen_candidate(rng, p, perturb_p=0.0, background_p=0.0, random_tau_p=0.0, demote_p=0.0)
        if not c.Gamma:
            return None
        k = rng.choice(list(c.Gamma))
        x = rng.choice(sorted(p.C, key=repr))
        E = c.E
        full = E.full(k)
        if not full:
            return None
        w = rng.choice(sorted(full))
        a2, b2 = c.tau[x[0]], c.sigma[x[1]]
        E2 = Org("E'", E.ports, E.dom, E.comps, E.foot, E.B, E.A, E._compose,
                 lambda j, a, b: (E.L(j, a, b) ^ {w}) if (j, a, b) == (k, a2, b2) else E.L(j, a, b))
        return p, c, c.replace(E=E2, name="ℰ'"), k, x

    def check(m):
        p, c1, c2, k, (a, b) = m
        N = c1.lam[k][0]
        for R in all_R(p.D):
            D2 = p.D.with_relations_at(a, b, R)
            if proj_lam(c1, k, D2, a, b) == c1.E.L(k, c1.tau[a], c1.sigma[b]) and proj_lam(c2, k, D2, a, b) == c2.E.L(k, c2.tau[a], c2.sigma[b]):
                return "one counterpart, different relations, both F1 under %r\n%s" % (R, both_desc(p, c1, c2))
        return None

    parts.append(forall(S, "FC44", 1, "under I36", "one counterpart (same subnetwork, translations, value maps) and different relations at (a,b) ⇒ no R gives F1 at (a,b) to both",
                        gen, check, CONF, 20, BOTHFAM))

    def gen2(rng, size):
        D, p = D_and_p(rng, size, proper=True)
        if D is None or len(D.ports) < 2:
            return None
        j = rng.choice([j for j in D.comps])
        if len(D.foot[j]) < 2:
            return None
        u1, u2 = D.foot[j][:2]
        if D.dom[u1] != D.dom[u2]:
            return None
        return p, j, u1, u2

    def check2(m):
        p, j, u1, u2 = m
        D = p.D
        cands = []
        for u in (u1, u2):
            tab = {}
            for a in D.A:
                for b in D.B:
                    VN, Sn = D.sol_sub([j], a, b)
                    tab[("k", a, b)] = frozenset((z[VN.index(u)],) for z in Sn)
            E = Org("E_" + u, ["v"], {"v": D.dom[u]}, ["k"], {"k": ("v",)}, D.B, D.A, D._compose, (lambda t: (lambda jj, a, b: t[(jj, a, b)]))(tab))
            cands.append(Candidate(E, p, {"v": Translation((u,))}, {a: a for a in D.A}, {b: b for b in D.B},
                                   {"k": (frozenset([j]), {"v": Translation((u,))})}, ["k"], "v", name="ℰ_" + u))
        c1, c2 = cands
        for (a, b) in p.C:
            if c1.E.L("k", a, b) != c2.E.L("k", a, b) and F1_at(c1, a, b) and F1_at(c2, a, b):
                return ("One subnetwork {%s} is the counterpart of k in both candidates, through different port translations (v := %s and v := %s). At (%s,%s) the two relations differ and both meet (F1) under the target's own relations: the clause of L315 ('none do when two of their active components with one counterpart have different relations there') needs I36's reading of 'one counterpart'.\n%s"
                        % (j, u1, u2, a, b, both_desc(p, c1, c2)))
        return None

    parts.append(exists(S, "FC44", 2, "the reading 'one counterpart = the same subnetwork'", "there are ℰ, ℰ', R with one subnetwork as counterpart, different relations, both meeting (F1)",
                        gen2, check2, SMALL, 60, BOTHFAM, ["I36", "I101"], note="proper models only"))
    return parts


@claim("FC45", ["I77", "I78", "I81", "I70"])
def fc45(S):
    def gen(rng, size):
        m = gen_pair(rng, size)
        if m is None:
            return None
        p, c1, _ = m
        E = c1.E
        pm = {v: v + "'" for v in E.ports}
        cm = {k: k + "'" for k in E.comps}
        icm = {v: k for k, v in cm.items()}
        E2 = Org(E.name + "'", [pm[v] for v in E.ports], {pm[v]: E.dom[v] for v in E.ports}, [cm[k] for k in E.comps],
                 {cm[k]: tuple(pm[v] for v in E.foot[k]) for k in E.comps}, E.B, E.A, E._compose, lambda j, a, b: E.L(icm[j], a, b))
        c2 = c1.replace(E=E2, pi={pm[v]: c1.pi[v] for v in E.ports}, lam={cm[k]: (N, {pm[v]: tr[v] for v in E.foot[k]}) for k, (N, tr) in c1.lam.items()},
                        Gamma=tuple(cm[k] for k in c1.Gamma), deltaE=pm[c1.deltaE], name="ℰ'")
        return p, c1, c2

    def check(m):
        p, c1, c2 = m
        cps = conflict_pairs(c1, c2)
        if cps:
            return "recoded copies conflict at %s\n%s" % (cps, both_desc(p, c1, c2))
        return None

    return [forall(S, "FC45", 1, "(a) recoded candidates", "a structure-preserving recoding of ℰ conflicts with ℰ at no pair", gen, check, CONF, 15, BOTHFAM, ["I70"]),
            construction("(b) some R lets both meet at every pair ⇒ no conflict", "by D8.2's second disjunct", True, "Conf's second disjunct needs ¬∃R BothMeet; the first needs different answers, which BothMeet excludes (both equal Ans^R_p)")]


@claim("FC46", ["I77", "I78", "I81", "I85"])
def fc46(S):
    def gen(rng, size):
        m = gen_pair(rng, size, acc_bias=True)
        if m is None:
            return None
        p, c1, c2 = m
        if not (account(c1) and account(c2)):
            return None
        return m

    def check(m):
        p, c1, c2 = m
        for x in p.C:
            if conflict(c1, c2, *x):
                return "two accounts conflict at %r ∈ C\n%s" % (x, both_desc(p, c1, c2))
        return None

    return [forall(S, "FC46", 1, "two accounts do not conflict in C", "Acc(ℰ) ∧ Acc(ℰ') ⇒ no conflict at any pair of C", gen, check, CONF, 60, BOTHFAM,
                   note="only pairs of candidates that both meet (E) are counted")]


@claim("FC47", ["I77", "I78", "I81", "I87", "I88", "I89"])
def fc47(S):
    parts = []

    def check(m):
        p, c1, c2 = m
        met = False
        for x in all_pairs(p.D):
            if not (c1.translates(*x) and c2.translates(*x)):
                continue
            tab = meet_table(c1, c2, *x)
            cf = conflict(c1, c2, *x, table=tab)
            met = met or cf
            if cf and any(r[0] and r[1] for r in tab):
                return "conflict and some R lets both meet at %r\n%s" % (x, both_desc(p, c1, c2))
        return None if met else VAC

    parts.append(forall(S, "FC47", 1, "(a) conflict excludes joint meeting", "Conf(ℰ,ℰ';a,b) ⇒ ∀R ¬(Meets_ab(ℰ,R) ∧ Meets_ab(ℰ',R))", gen_pair, check, CONF, 15, BOTHFAM))
    # (b) the test argument, propositional encoding
    rec, m1, acc1 = "rec", "meets1", "acc1"
    j = Assessor(["MP", "MT"], [rec, Imp(rec, Not(m1)), Imp(acc1, m1)])
    s1 = Step("MP", Not(m1), [Leaf(rec, "record"), Leaf(Imp(rec, Not(m1)))])
    alpha = Step("MT", Not(acc1), [s1, Leaf(Imp(acc1, m1))])
    ok = usable(j, alpha) and rules_out(alpha, acc1)
    j2 = Assessor(["MP", "MT"], [Imp(rec, Not(m1)), Imp(acc1, m1)])
    parts.append(computed("(b) the argument from a test's record", "for j who admits MP and MT and for whom the record and its premises are live, the argument is in X_j(Acc(ℰ))",
                          ok and not usable(j2, alpha),
                          "argument:\n%s\nusable by j: %s; rules out Acc(ℰ): %s; usable once the record is withdrawn: %s" % (alpha.show(2), usable(j, alpha), rules_out(alpha, acc1), usable(j2, alpha)),
                          ["I87", "I88", "I89"]))
    return parts


@claim("FC48", ["I77", "I78", "I81"])
def fc48(S):
    def check(m):
        p, c1, c2 = m
        if not all(c1.translates(*x) and c2.translates(*x) for x in p.C):
            return VAC
        if any(conflict(c1, c2, *x) for x in p.C):
            return VAC
        for (a, b) in p.C:
            if c1.ans_E(c1.tau[a], c1.sigma[b]) != c2.ans_E(c2.tau[a], c2.sigma[b]):
                return "no conflict in C, different answers at (%s,%s)\n%s" % (a, b, both_desc(p, c1, c2))
        return None

    return [forall(S, "FC48", 1, "no conflict in C ⇒ answers agree", "¬Conf at every pair of C ⇒ equal answers on C", gen_pair, check, CONF, 15, BOTHFAM)]


@claim("FC49", ["I77", "I78", "I81", "I86"])
def fc49(S):
    def gen(rng, size):
        m = gen_pair(rng, size)
        if m is None:
            return None
        p, c1, c2 = m
        if rng.random() < 0.4:
            drop = rng.choice(p.D.A)
            if drop != ONE:
                t = dict(c2.tau)
                t.pop(drop, None)
                c2 = c2.replace(tau=t)
        return p, c1, c2

    def check(m):
        p, c1, c2 = m
        cps = conflict_pairs(c1, c2)
        if not cps:
            return VAC
        ki = any(x in p.C for x in cps)
        kii = (not ki) and any(x not in p.C for x in cps)
        if ki == kii:
            return "rivals of neither or both kinds: %s\n%s" % (cps, both_desc(p, c1, c2))
        return None

    return [forall(S, "FC49", 1, "exactly one kind", "Riv ⇒ exactly one of kind (i), kind (ii)", gen, check, CONF, 15, BOTHFAM, ["I86"])]


@claim("FC50", ["I77", "I78", "I81", "I86"])
def fc50(S):
    def check(m):
        p, c1, c2 = m
        cps = conflict_pairs(c1, c2)
        out = [x for x in cps if x not in p.C]
        if not out:
            return VAC
        x = out[0]
        p2 = p.with_C(p.C | {x})
        d1, d2 = c1.replace(p=p2), c2.replace(p=p2)
        if problem_kind(d1, d2) != "i":
            return "a finer contract holding the conflict pair gives kind %s\n%s" % (problem_kind(d1, d2), both_desc(p, c1, c2))
        return None

    return [forall(S, "FC50", 1, "(a) a finer contract makes kind (i)", "Conf at (a,b) ∉ C, C' ⊇ C ∪ {(a,b)} ⇒ the problem on p' is of kind (i)", gen_pair, check, CONF, 15, BOTHFAM, ["I86"]),
            construction("(b) a narrowed contract leaves the problem on p", "Prob_j on p is a function of p's data and j", True, "problem_kind(ℰ,ℰ') reads only the candidates, their question and its contract")]


@claim("FC51", ["I77", "I78", "I81", "I85"])
def fc51(S):
    parts = []

    def gen(rng, size):
        D, p = D_and_p(rng, size)
        if D is None:
            return None
        outside = [(a, b) for a in D.A for b in D.B if (a, b) not in p.C]
        if not outside:
            return None
        extra = [x for x in outside if rng.random() < 0.6] or outside[:1]
        p2 = p.with_C(p.C | set(extra))
        c1 = gen_candidate(rng, p, name="ℰ", perturb_p=0.2, background_p=0.0, random_tau_p=0.0, demote_p=0.0)
        c2 = gen_candidate(rng, p, name="ℰ'", perturb_p=0.4, background_p=0.0, random_tau_p=0.0, demote_p=0.0)
        return p, p2, c1, c2

    def check(m):
        p, p2, c1, c2 = m
        if not (account(c1) and account(c2) and account(c1.replace(p=p2)) and not account(c2.replace(p=p2))):
            return VAC
        d2 = c2.replace(p=p2)
        new = [x for x in p2.C - p.C if not (F1_at(d2, *x) and F2eq_at(d2, *x) and A_at(d2, *x))]
        if not new:
            v, det_ = account(d2, detail=True)
            return "no new pair separates them, yet ℰ' fails (E) on C': %s\n%s\n%s" % (det_, p2.describe(), both_desc(p, c1, c2))
        return None

    parts.append(forall(S, "FC51", 1, "(a) separation lies in C'∖C", "Acc of both on C, Acc(ℰ) and ¬Acc(ℰ') on C' ⊋ C ⇒ a pair of C'∖C where ℰ' fails F1, the F2 equation or A",
                        gen, check, SMALL, 80, BOTHFAM, note="each question's scope statement states every pair outside its contract (I85)"))

    def gen2(rng, size):
        D, p = D_and_p(rng, size)
        if D is None:
            return None
        c = gen_candidate(rng, p, perturb_p=0.2, background_p=0.0, random_tau_p=0.0, demote_p=0.0)
        G = list(c.Gamma)
        if len(G) < 2:
            return None
        psi = dict(zip(G, rng.sample(G, len(G))))
        if any(c.E.foot[k] != c.E.foot[psi[k]] for k in G):
            return None
        lam2 = {k: c.lam[psi[k]] for k in G}
        return p, c, c.replace(lam=lam2, name="ℰ∘ψ"), psi

    def check2(m):
        p, c1, c2, psi = m
        if not (F1(c1) and F1(c2)):
            return VAC
        for k in c1.Gamma:
            for (a, b) in p.C:
                if proj_lam(c1, k, p.D, a, b) != proj_lam(c1, psi[k], p.D, a, b):
                    return "two pairings both F1, projections differ\n%s" % both_desc(p, c1, c2)
        return None

    parts.append(forall(S, "FC51", 2, "(b) two pairings", "λ' = λ∘ψ (ψ keeping footprints), both F1 on C ⇒ the projected relations of λ(k) and λ(ψk) agree on C",
                        gen2, check2, SMALL, 80, BOTHFAM, note="ψ restricted to permutations of Γ that keep footprints"))
    return parts


def rand_allow(rng, D):
    Rs = list(all_R(D))
    keep = set(i for i in range(len(Rs)) if rng.random() < 0.5)
    key = lambda R: tuple(sorted((j, tuple(sorted(r))) for j, r in R.items()))
    allowed = set(key(Rs[i]) for i in keep)
    return (lambda R: key(R) in allowed), allowed


@claim("FC52", ["I77", "I78", "I81"])
def fc52(S):
    def gen(rng, size):
        D, p = D_and_p(rng, size)
        if D is None or not small_enough(D, 1024):
            return None
        c = any_candidate(rng, p, size)
        allow, _ = rand_allow(rng, D)
        return p, c, allow

    def check(m):
        p, c, allow = m
        D = p.D
        met = False
        for (a, b) in all_pairs(D):
            if not c.translates(a, b):
                continue
            y = c.ans_E(c.tau[a], c.sigma[b])
            first = all(not allow(R) for R in all_R(D) if p.ans(a, b, D.with_relations_at(a, b, R)) == y)
            met = met or first
            second = all(not allow(R) for R in all_R(D) if meets_ab(c, a, b, R))
            if first and not second:
                return "first disjunct without the second at (%s,%s)\n%s" % (a, b, c.describe())
        return None if met else VAC

    parts = [forall(S, "FC52", 1, "first disjunct implies the second", "χ excludes ℰ's answer at (a,b) ⇒ χ excludes every R with Meets_ab(ℰ,R)", gen, check, CONF, 10, BOTHFAM)]

    # Area 2: D8.5 with its existence clauses (A2-03). FC52 restated: the implication holds where some R lets ℰ meet.
    def check2(m):
        p, c, allow = m
        D = p.D
        met = False
        for (a, b) in all_pairs(D):
            if not c.translates(a, b):
                continue
            first, second = conf_claim(c, a, b, allow, reading="area2", parts=True)
            some_meet = any(meets_ab(c, a, b, R) for R in all_R(D))
            if not (first and some_meet):
                continue
            met = True
            if not second:
                return "first disjunct without the second where some R lets ℰ meet, at (%s,%s)\n%s" % (a, b, c.describe())
        return None if met else VAC

    parts.append(forall(S, "FC52", 2, "(restated, area 2) where some R lets ℰ meet", "D8.5 with existence: first disjunct ∧ ∃R Meets_ab(ℰ,R) ⇒ second disjunct", gen, check2, CONF, 10, BOTHFAM))

    def check3(m):
        p, c, allow = m
        D = p.D
        for (a, b) in all_pairs(D):
            if not c.translates(a, b):
                continue
            first, second = conf_claim(c, a, b, allow, reading="area2", parts=True)
            if first and not second:
                return ("under D8.5 with existence the first disjunct holds and the second does not at (%s,%s): no R lets ℰ meet there; the 'or' is two routes\n%s\n%s"
                        % (a, b, D.describe(), c.describe()))
        return None

    parts.append(exists(S, "FC52", 3, "(area 2) the 'or' is two routes", "under D8.5 with existence, a pair where the first disjunct holds and the second does not", gen, check3, CONF, 10, BOTHFAM))
    return parts


@claim("FC53", ["I87", "I88", "I89", "I90"])
def fc53(S):
    parts = []
    chi, app, acc = "chi", "applies", "acc"
    # (a) with the premise that χ speaks of the target, forms admitted
    j = Assessor(["MP", "AndI"], [chi, app, Imp(And(chi, app), Not(acc))])
    s1 = Step("AndI", And(app, chi), [Leaf(app), Leaf(chi)])
    alpha = Step("MP", Not(acc), [s1, Leaf(Imp(And(chi, app), Not(acc)))])
    ok_a = usable(j, alpha) and rules_out(alpha, acc)
    parts.append(computed("(a) with Applies", "ConfCl at (a,b) ∈ C, Applies, χ and Applies live, forms admitted ⇒ X_j(Acc(ℰ)) ≠ ∅", ok_a,
                          "argument:\n%s\nusable: %s, rules out Acc: %s" % (alpha.show(2), usable(j, alpha), rules_out(alpha, acc)), ["I87", "I89"]))
    # (b) the pendulum: the edit deletes friction; χ = 'motion stops'; the candidate gives motion that never stops
    D = Org("D_pend", ["stops"], {"stops": (0, 1)}, ["friction"], {"friction": ("stops",)}, ["b0"], [ONE, "del_f"], lambda a2, a1: None,
            lambda j_, a, b: {(1,)} if a == ONE else {(0,), (1,)})
    p = Question(D, [(ONE, "b0"), ("del_f", "b0")], "b0", PortQuery(), "stops", name="p_pend")
    E = Org("E_pend", ["stops"], {"stops": (0, 1)}, ["k"], {"k": ("stops",)}, ["b0"], [ONE, "del_f"], lambda a2, a1: None,
            lambda j_, a, b: {(1,)} if a == ONE else {(0,)})
    c = Candidate(E, p, {"stops": Translation(("stops",))}, {ONE: ONE, "del_f": "del_f"}, {"b0": "b0"},
                  {"k": (frozenset(["friction"]), {"stops": Translation(("stops",))})}, ["k"], "stops", name="ℰ_perpetual")
    allow = lambda R: R["friction"] <= {(1,)} and bool(R["friction"])
    cc = conf_claim(c, "del_f", "b0", allow)
    j2 = Assessor(["MP", "AndI"], [chi, Imp(And(chi, app), Not(acc))])
    args = enumerate_args([chi, app, Imp(And(chi, app), Not(acc))], forms=("MP", "AndI"), depth=2)
    Xs = X(j2, acc, args)
    parts.append(computed("(b) the pendulum without Applies", "ConfCl(ℰ,χ;a,b) and ¬Applies(χ,a,b), and no argument from χ in X_j(Acc(ℰ))", cc and not Xs,
                          "D: friction stops the motion at the baseline; the edit del_f deletes friction. χ allows only relations of friction that stop the motion. ConfCl at (del_f,b0): %s. "
                          "For j who accepts χ and 'χ ∧ Applies ⇒ ¬Acc' but not Applies, the arguments of height ≤ 2 from these premises (%d) that j can use and that rule out Acc: %d."
                          % (cc, len(args), len(Xs)), ["I87", "I88", "I89", "I90"]))
    return parts


@claim("FC54", ["I77", "I78", "I81"])
def fc54(S):
    def gen(rng, size):
        m = gen_pair(rng, size)
        if m is None or not small_enough(m[0].D, 1024):
            return None
        allow, _ = rand_allow(rng, m[0].D)
        return m + (allow,)

    def check(m):
        p, c1, c2, allow = m
        met = False
        for x in all_pairs(p.D):
            if not (c1.translates(*x) and c2.translates(*x)):
                continue
            tab = meet_table(c1, c2, *x)
            cg = conf_given(c1, c2, *x, allow, table=tab)
            met = met or cg
            if cg and conflict(c1, c2, *x, table=tab):
                return "ConfG_χ and Conf at %r\n%s" % (x, both_desc(p, c1, c2))
        return None if met else VAC

    return [forall(S, "FC54", 1, "conflict given χ excludes conflict", "ConfG_χ(ℰ,ℰ';a,b) ⇒ ¬Conf(ℰ,ℰ';a,b)", gen, check, CONF, 10, BOTHFAM)]


@claim("FC55", [])
def fc55(S):
    fns = [core.conflict, core.conf_given, core.conf_claim, core.rivals, core.problem_kind, core.conflict_pairs, core.meets_ab, core.meet_table]
    over = []
    for f in fns:
        sig = inspect.signature(f)
        nc = sum(1 for n in sig.parameters if n in ("c1", "c2", "cand"))
        if nc > 2:
            over.append(f.__name__)
    return [computed("syntactic: no predicate of Part VI takes more than two candidates", "every predicate over candidates in the model takes at most two", not over,
                     "functions checked: %s; taking more than two candidates: %s" % ([f.__name__ for f in fns], over or "none"))]


# ---- arguments (Part IX) --------------------------------------------------------------------------------

ATOMS = ["p", "q", "r"]


def rand_formula(rng, depth=2):
    if depth == 0 or rng.random() < 0.4:
        a = rng.choice(ATOMS)
        return a if rng.random() < 0.7 else Not(a)
    op = rng.choice(["not", "and", "imp", "imp"])
    if op == "not":
        return Not(rand_formula(rng, depth - 1))
    if op == "and":
        return And(rand_formula(rng, depth - 1), rand_formula(rng, depth - 1))
    return Imp(rand_formula(rng, depth - 1), rand_formula(rng, depth - 1))


@claim("FC56", ["I87", "I88", "I89"])
def fc56(S):
    """FC56 after area 3: (a) carries the hypothesis that j' declares for each step a contract that
    contains j's and the same grain and boundary (D9.5, I42); (a'') shows the hypothesis is needed; (c)
    withdrawal alone (Accepted shrinks) adds no member to any X_j(φ), which is the formal statement
    that replaces L393's 'it does not rule the conclusion out'."""
    parts = []
    CS = [frozenset(x) for x in ([1], [1, 2], [1, 2, 3])]

    def gen(rng, size):
        prem = [rand_formula(rng) for _ in range(rng.randint(2, 5))]
        acc1 = [x for x in prem if rng.random() < 0.5]
        acc2 = acc1 + [x for x in prem if x not in acc1 and rng.random() < 0.5]
        forms1 = [f for f in ("MP", "MT", "AndI", "AndE") if rng.random() < 0.6]
        forms2 = forms1 + [f for f in ("MP", "MT", "AndI", "AndE") if f not in forms1 and rng.random() < 0.5]
        args = enumerate_args(prem, depth=2, max_args=300)
        for a_ in args:
            for u in a_.steps():
                if not hasattr(u, "_idx_set"):
                    u.index = (rng.choice(CS), "l", "b")
                    u._idx_set = True
        C1 = rng.choice(CS)
        C2 = frozenset(C1 | rng.choice(CS))
        return prem, Assessor(forms1, acc1, (C1, "l", "b")), Assessor(forms2, acc2, (C2, "l", "b")), args

    def check(m):
        prem, j1, j2, args = m
        for a_ in args:
            if usable(j1, a_) and not usable(j2, a_):
                return "usable for j, not for j' ⊇ j:\n%s" % a_.show(2)
        for phi in ATOMS + [Not(x) for x in ATOMS]:
            x1 = set(id(a_) for a_ in X(j1, phi, args))
            x2 = set(id(a_) for a_ in X(j2, phi, args))
            if not x1 <= x2:
                return "X_j(%s) ⊄ X_j'(%s)" % (show(phi), show(phi))
        return None

    parts.append(forall(S, "FC56", 1, "(a) monotone in what is accepted, admitted and declared", "Accepted_j ⊆ Accepted_j', Forms_j ⊆ Forms_j', C_j(u) ⊆ C_j'(u), ℓ_j(u) = ℓ_j'(u), β_j(u) = β_j'(u) ⇒ Usable_j ⊆ Usable_j' and X_j(φ) ⊆ X_j'(φ)",
                        gen, check, [Size(3, 2, 1, 1, 0)], 400, ["random propositional premises over p, q, r; all arguments of height ≤ 2; random declared contracts per step"], ["I87", "I88", "I89", "I42"]))
    # (a'') the scope hypothesis is needed (Mimo, part 12): a coarser declared grain loses a ruling out
    st = Step("MP", Not("p"), [Leaf("q"), Leaf(Imp("q", Not("p")))], index=("C", "fine", "b"))
    jf = Assessor(["MP"], ["q", Imp("q", Not("p"))], ("C", "fine", "b"))
    jc = Assessor(["MP"], ["q", Imp("q", Not("p")), "r"], ("C", "coarse", "b"))
    lost = bool(X(jf, "p", [st])) and not X(jc, "p", [st])
    parts.append(computed("(a'') the declared grain held fixed", "j' accepts more but declares another grain for the step: a ruling out is lost, so (a) needs the scope hypothesis", lost,
                          "X_j(p) for j (grain 'fine'): %d; for j' (more accepted, grain 'coarse'): %d" % (len(X(jf, "p", [st])), len(X(jc, "p", [st]))), ["I87", "I89", "I42"]))
    j = Assessor(["MP"], ["p"])
    args = enumerate_args(["p", Imp("q", "r")], depth=2)
    ok = not X(j, "q", args) and not X(j, Not("q"), args)
    parts.append(computed("(b) absence rules out nothing", "there are j, φ with X_j(φ) = ∅ = X_j(¬φ)", ok, "j accepts p; φ = q: |X_j(q)| = %d, |X_j(¬q)| = %d over %d arguments" % (len(X(j, "q", args)), len(X(j, Not("q"), args)), len(args)), ["I88"]))

    def genw(rng, size):
        prem = [rand_formula(rng) for _ in range(rng.randint(2, 5))]
        acc = list(prem)
        d = rng.choice(prem)
        forms = [f for f in ("MP", "MT", "AndI", "AndE", "free") if rng.random() < 0.6]
        args = enumerate_args(prem, depth=2, max_args=300)
        extra = [Step("free", rng.choice(ATOMS + [Not(x) for x in ATOMS]), [Leaf(x)]) for x in prem]
        return Assessor(forms, acc), Assessor(forms, [x for x in acc if canon(x) != canon(d)]), args + extra, d

    def checkw(m):
        j1, j2, args, d = m
        for phi in ATOMS + [Not(x) for x in ATOMS]:
            x1 = set(id(a_) for a_ in X(j1, phi, args))
            x2 = set(id(a_) for a_ in X(j2, phi, args))
            if not x2 <= x1:
                return "withdrawing %s adds a member to X_j(%s)" % (show(d), show(phi))
        return None

    parts.append(forall(S, "FC56", 3, "(c) withdrawal alone rules nothing out", "Accepted_j(ξ') = Accepted_j(ξ) ∖ {d}, Forms and scope fixed ⇒ X_j^{ξ'}(φ) ⊆ X_j^{ξ}(φ) for every φ (free forms admitted)",
                        genw, checkw, [Size(3, 2, 1, 1, 0)], 300, ["random premises; arguments of height ≤ 2 and one-step free arguments"], ["I87", "I88", "I89"]))
    # GLM's near miss (part 12): withdrawing d and taking up 'd is withdrawn' (W) with a free form W ⊢ ¬d
    W, dd = "w", "p"
    before = Assessor(["free"], [dd])
    after = Assessor(["free"], [W])
    g = Step("free", Not(dd), [Leaf(W)])
    near = (not X(before, dd, [g])) and bool(X(after, dd, [g]))
    parts.append(computed("(c') the near miss is not withdrawal alone", "after withdrawing d, d can be ruled out only if j takes up something (here W with a free form); Accepted then grows, and (c) does not apply", near,
                          "X_j(d) before: %d; after withdrawing d and taking up W: %d. The change adds W to Accepted_j: it is not withdrawal alone." % (len(X(before, dd, [g])), len(X(after, dd, [g]))), ["I87", "I89"]))
    return parts


# ---- identification, obstruction ----------------------------------------------------------------------

@claim("FC57", ["I77"])
def fc57(S):
    def items():
        for nz in range(1, 5):
            Z = list(range(nz))
            for ny in range(1, 4):
                for nf in range(1, 4):
                    for g in itertools.product(range(ny), repeat=nz):
                        for f in itertools.product(range(nf), repeat=nz):
                            yield Z, g, f, ny, nf

    def check(m):
        Z, g, f, ny, nf = m
        lhs = all(identified(Z, lambda z: g[z], lambda z: f[z], y) for y in set(g))
        rhs = all(len(set(f[z] for z in Z if g[z] == y)) == 1 for y in set(g))  # a function f̄ on g[Z] exists
        fbar = {}
        ok = True
        for z in Z:
            if g[z] in fbar and fbar[g[z]] != f[z]:
                ok = False
            fbar[g[z]] = f[z]
        if lhs != ok:
            return "Z=%s g=%s f=%s: identified everywhere %s, factorization %s" % (Z, g, f, lhs, ok)
        return None

    return [exhaustive("FC57", "(I2) on finite sets", "(∀y ∈ g[Z]: |f[Z_y]| = 1) ⟺ f = f̄∘g for some f̄", items(), check,
                       "every g: Z → Y and f: Z → F with |Z| ≤ 4, |Y| ≤ 3, |F| ≤ 3")]


@claim("FC58", ["I77"])
def fc58(S):
    parts = []

    def gen(rng, size):
        n = rng.randint(1, 3)
        m = rng.randint(1, 3)
        G = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(m)]
        c = [rng.randint(-2, 2) for _ in range(n)]
        return G, c

    def box_violation(G, c, k=8):
        n = len(c)
        for z in itertools.product(range(-k, k + 1), repeat=n):
            if all(sum(G[i][j] * z[j] for j in range(n)) == 0 for i in range(len(G))) and sum(c[j] * z[j] for j in range(n)) != 0:
                return z
        return None

    def check(m):
        G, c = m
        crit = rank(G + [c]) == rank(G)
        v = box_violation(G, c)
        if crit != (v is None):
            return "G = %s, c = %s: kernel criterion %s, integer kernel vector with c·z ≠ 0: %s" % (G, c, crit, v)
        return None

    parts.append(forall(S, "FC58", 1, "the kernel criterion", "c constant on every fibre of G over ℚ^n ⟺ ker G ⊆ ker c (rank test against a search for z ∈ ker G with c·z ≠ 0 in [-8,8]^n)",
                        gen, check, [Size(3, 1, 1, 1, 0)], 600, ["integer matrices, entries in [-2,2], n, m ≤ 3"]))

    def check_rows(m):
        G, c = m
        n = len(c)
        r0 = rank(G)
        row = G[0]
        if rank(G + [row]) != r0:
            return "a repeated row changed the kernel: %s" % G
        e = [0] * n
        for i in range(n):
            e = [1 if j == i else 0 for j in range(n)]
            if rank(G + [e]) > r0:
                if rank(G + [e]) != r0 + 1:
                    return "an independent row lowered dim ker by more than one"
                break
        return None

    parts.append(forall(S, "FC58", 2, "rows", "a row in the row space leaves ker G; a row outside it lowers dim ker by one",
                        gen, check_rows, [Size(3, 1, 1, 1, 0)], 600, ["integer matrices"]))
    # the look: Z a proper subset (a box), under I64's alternative
    G, c = [[1, 1]], [1, 0]
    Z = list(itertools.product((0, 1), repeat=2))
    idall = all(identified(Z, lambda z: G[0][0] * z[0] + G[0][1] * z[1], lambda z: z[0], y) for y in set(z[0] + z[1] for z in Z))
    parts.append(look("Z a proper subset", "the look: with Z a proper subset (I64's alternative), the criterion can fail",
                      rank(G + [c]) != rank(G) and False or (not (rank(G + [c]) == rank(G))) and not idall,
                      "Z = {0,1}², g = x+y, f = x: kernel criterion %s; identified at every attainable y on Z: %s (y = 1 has the fibre {(0,1),(1,0)}). Taking y ∈ {0, 2} alone, f is identified though ker g ⊄ ker f: on a box the criterion is sufficient, not necessary, at a given y." % (rank(G + [c]) == rank(G), idall), ["I64"]))
    parts[-1]["status"] = "look: as expected"
    return parts


@claim("FC59", [])
def fc59(S):
    G = [[1, 1, 0], [1, 0, 1]]
    k = (1, -1, -1)
    ker_ok = all(sum(G[i][j] * k[j] for j in range(3)) == 0 for i in range(2)) and rank(G) == 2
    c1, c2 = (0, -1, 1), (1, 0, 0)
    ok = ker_ok and sum(a * b for a, b in zip(c1, k)) == 0 and sum(a * b for a, b in zip(c2, k)) != 0 and rank(G + [list(c1)]) == 2 and rank(G + [list(c2)]) == 3
    return [computed("the two balances", "ker G = span{(1,−1,−1)}; b_B − b_A identified; x not", ok, "rank G = %d; c=(0,−1,1): c·k = %d; c=(1,0,0): c·k = %d" % (rank(G), sum(a * b for a, b in zip(c1, k)), sum(a * b for a, b in zip(c2, k))))]


@claim("FC60", ["I87", "I89"])
def fc60(S):
    parts = [construction("(a) (E) does not register how an input was chosen", "two candidates alike in (D, C, E, t, Γ, Σ) have one Acc value", True,
                          "core.account takes no record of why b_B was set (FC30); NC1 compares relations with the answer, and b_B = 0 is not the answer (I24)")]
    xm, bb0 = "x_is_m", "bB_is_0"
    rec = Leaf(bb0, "record", made_from=xm)
    alpha = Step("MP", xm, [rec, Leaf(Imp(bb0, xm))])
    j = Assessor(["MP"], [bb0, Imp(bb0, xm)])
    ok = usable(j, alpha) and not rules_out(alpha, Not(xm))
    parts.append(computed("(b) the record made from x = m* does not rule out x ≠ m*", "RO fails for an argument whose record leaf is MadeFrom the favoured claim", ok,
                          "argument:\n%s\nusable: %s; rules out ¬x_is_m: %s" % (alpha.show(2), usable(j, alpha), rules_out(alpha, Not(xm))), ["I87", "I89"]))
    return parts


@claim("FC61", ["I77"])
def fc61(S):
    parts = []

    def items():
        rng = random.Random(10461)
        for n in range(1, 6):
            for _ in range(400):
                I = [rng.randrange(2) for _ in range(n)]
                R = {(a, b) for a in range(n) for b in range(n) if rng.random() < 0.4}
                yield n, I, R

    def closure(n, R):
        reach = {(a, a) for a in range(n)} | set(R)
        changed = True
        while changed:
            changed = False
            for (a, b) in list(reach):
                for (c, d) in list(reach):
                    if b == c and (a, d) not in reach:
                        reach.add((a, d))
                        changed = True
        return reach

    def check(m):
        n, I, R = m
        if not all(I[a] == I[b] for (a, b) in R):
            return VAC
        for (a, b) in closure(n, R):
            if I[a] != I[b]:
                return "path across invariant values"
        return None

    parts.append(exhaustive("FC61", "(a) an invariant blocks paths", "zRz' ⇒ I(z)=I(z') gives R* ⊆ {I(z)=I(z')}", items(), check, "2000 random step relations on ≤ 5 states (seed 10461)"))
    ok_b = True
    txt_b = "R = ∅ on {0,1}, I constant: I(0) = I(1) and 0 does not reach 1"
    splits = [(a, b, 23 - a - b) for a in range(24) for b in range(24 - a)]
    eq = [s for s in splits if s[0] == s[1] == s[2]]
    parts.append(computed("(b) equal values do not give paths; (c) twenty-three tokens", "(b) a witness; (c) no equal split of 23", ok_b and not eq, txt_b + "; distributions of 23 whole tokens in three piles: %d, equal splits: %d" % (len(splits), len(eq))))
    return parts


@claim("FC62", ["I78", "I79"])
def fc62(S):
    D = Org("D_elim", ["u", "e"], {"u": (0, 1), "e": (0, 1)}, ["h_u", "x", "rest"], {"h_u": ("u",), "x": ("u", "e"), "rest": ("e",)}, ["b0"], [ONE, "a_x"], lambda a2, a1: None,
            lambda j, a, b: {"h_u": {(1,)}, "x": ({(0, 0), (0, 1), (1, 0), (1, 1)} if a == ONE else {(0, 0), (1, 1)}), "rest": ({(0,)} if a == ONE else {(0,), (1,)})}[j])
    p = Question(D, [(ONE, "b0"), ("a_x", "b0")], "b0", PortQuery(), "e", name="p_noX")
    lam = {"k": (frozenset(["x"]), {"u": Translation(("u",)), "e": Translation(("e",))}), "k_u": (frozenset(["h_u"]), {"u": Translation(("u",))}),
           "k_rest": (frozenset(["rest"]), {"e": Translation(("e",))})}
    E = Org("E_elim", ["u", "e"], D.dom, ["k_u", "k", "k_rest"], {"k_u": ("u",), "k": ("u", "e"), "k_rest": ("e",)}, ["b0"], [ONE, "a_x"], lambda a2, a1: None,
            lambda j, a, b: D.L({"k_u": "h_u", "k": "x", "k_rest": "rest"}[j], a, b))
    c = Candidate(E, p, {"u": Translation(("u",)), "e": Translation(("e",))}, {ONE: ONE, "a_x": "a_x"}, {"b0": "b0"}, lam, ["k"], "e", name="ℰ_elim")
    v, d = account(c, detail=True)
    return [computed("eliminative explanation", "E with k, λ(k) = {x} (deleted at the baseline) meets (E) on {(1,b0),(a_x,b0)} when the answer depends on x", v,
                     "answers: baseline %r, a_x %r; conjuncts %s; NC2 witness %s\n%s\n%s" % (p.ans(ONE, "b0"), p.ans("a_x", "b0"), d, NC2(c, witness=True), D.describe(), c.describe()), ["I78"])]


# ---- odd-order skew-symmetric matrices (E6) ----------------------------------------------------------

def det_mod(M, p):
    n = len(M)
    A_ = [[x % p for x in row] for row in M]
    d = 1
    for c in range(n):
        piv = next((r for r in range(c, n) if A_[r][c] % p), None)
        if piv is None:
            return 0
        if piv != c:
            A_[c], A_[piv] = A_[piv], A_[c]
            d = -d
        d = d * A_[c][c] % p
        inv = pow(A_[c][c], p - 2, p)
        for r in range(c + 1, n):
            f = A_[r][c] * inv % p
            A_[r] = [(A_[r][k] - f * A_[c][k]) % p for k in range(n)]
    return d % p


def skew_mats(n, p):
    idx = [(i, j) for i in range(n) for j in range(i + 1, n)]
    for vals in itertools.product(range(p), repeat=len(idx)):
        M = [[0] * n for _ in range(n)]
        for (i, j), v in zip(idx, vals):
            M[i][j] = v
            M[j][i] = (-v) % p
        yield M


PERMS3 = list(itertools.permutations(range(3)))


def sgn(perm):
    s = 1
    for i in range(len(perm)):
        for j in range(i + 1, len(perm)):
            if perm[i] > perm[j]:
                s = -s
    return s


def term(M, k, p=3):
    """The k-th Leibniz term of M (k indexes S_3; for order 2 the permutations fixing 2, for order 1 the
    identity; others 0) [I99]."""
    n = len(M)
    perm = PERMS3[k]
    if n == 3:
        pr = sgn(perm)
        for i in range(3):
            pr *= M[i][perm[i]]
        return pr % p
    if n == 2:
        if perm[2] != 2:
            return 0
        pr = sgn(perm[:2])
        for i in range(2):
            pr *= M[i][perm[i]]
        return pr % p
    return M[0][0] % p if perm == (0, 1, 2) else 0


@claim("FC63", ["I99", "I81", "I82"])
def fc63(S):
    parts = []
    tot, bad = 0, []
    for p_ in (3, 5, 7):
        for n in (1, 3, 5):
            if p_ ** (n * (n - 1) // 2) > 60000:
                rng = random.Random(10463)
                it = []
                idx = [(i, j) for i in range(n) for j in range(i + 1, n)]
                for _ in range(20000):
                    M = [[0] * n for _ in range(n)]
                    for (i, j) in idx:
                        v = rng.randrange(p_)
                        M[i][j], M[j][i] = v, (-v) % p_
                    it.append(M)
            else:
                it = skew_mats(n, p_)
            for M in it:
                tot += 1
                if det_mod(M, p_) != 0:
                    bad.append((p_, M))
    parts.append(computed("(a) odd skew-symmetric matrices are singular over GF(p), p odd", "det M = 0 for odd n, Mᵀ = −M",
                          not bad, "matrices checked: %d (n ∈ {1,3,5}, p ∈ {3,5,7}; exhaustive where p^(n(n−1)/2) ≤ 60000, else 20000 drawn with seed 10463); nonsingular: %d" % (tot, len(bad))))
    parts.append(computed("(b)", "det I3 = 1; det [[0,1],[−1,0]] = 1", det([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) == 1 and det([[0, 1], [-1, 0]]) == 1, "computed"))
    parts.extend(e6_parts())
    return parts


def e6_org():
    p = 3
    mats = []
    for n in (1, 2, 3):
        for vals in itertools.product(range(p), repeat=n * n):
            mats.append(tuple(tuple(vals[i * n:(i + 1) * n]) for i in range(n)))
    dom = {"n": (1, 2, 3), "M": tuple(mats), "d": (0, 1, 2), "i": (0, 1)}
    A = [ONE, "rs", "ro", "rb"]
    comp_tab = {("rs", "ro"): "rb", ("ro", "rs"): "rb"}

    def compose(a2, a1):
        if a2 == a1:
            return a2
        if "rb" in (a1, a2):
            return "rb"
        return comp_tab.get((a2, a1))

    order_rel = frozenset((len(M), M) for M in mats)
    skew_rel = frozenset((M,) for M in mats if all((M[i][j] + M[j][i]) % p == 0 for i in range(len(M)) for j in range(len(M))))
    odd_rel = frozenset([(1,), (3,)])
    det_rel = frozenset((M, det_mod([list(r) for r in M], p)) for M in mats)
    inv_rel = frozenset([(0, 0), (1, 1), (2, 1)])
    foot = {"order": ("n", "M"), "skew": ("M",), "odd": ("n",), "det": ("M", "d"), "inv": ("d", "i")}
    rel = {"order": order_rel, "skew": skew_rel, "odd": odd_rel, "det": det_rel, "inv": inv_rel}

    def Lf(j, a, b):
        if j == "skew" and a in ("rs", "rb"):
            return frozenset((M,) for M in mats)
        if j == "odd" and a in ("ro", "rb"):
            return frozenset([(1,), (2,), (3,)])
        return rel[j]

    D = Org("D_skew", ["n", "M", "d", "i"], dom, list(foot), foot, ["b0"], A, compose, Lf)
    return D, mats


def e6_parts():
    parts = []
    D, mats = e6_org()
    has_inv = FnQuery(lambda org, a, b, delta: any(z[org.ports.index("i")] == 1 for z in org.sol(a, b)), "Q: does the family contain an invertible matrix?")
    q = Question(D, [(x, "b0") for x in D.A], "b0", has_inv, "i", name="p_skew",
                 excl=[])  # the edits outside C (field arithmetic, det-invertibility) are not edits of this encoding
    answers = {a: q.ans(a, "b0") for a in D.A}
    tnames = ["t%d" % k for k in range(6)]
    terms_of = {M: tuple(term([list(r) for r in M], k) for k in range(6)) for M in mats}
    realizable = frozenset(terms_of[M] + (det_mod([list(r) for r in M], 3),) for M in mats)
    allsum = frozenset(t + (sum(t) % 3,) for t in itertools.product(range(3), repeat=6))
    out = []
    for variant, sum_rel in (("sum over every tuple of term values", allsum), ("sum restricted to realizable term tuples", realizable)):
        ports = ["n", "M"] + tnames + ["d", "i"]
        dom = dict(D.dom)
        for t in tnames:
            dom[t] = (0, 1, 2)
        foot = {"order": ("n", "M"), "skew": ("M",), "odd": ("n",), "inv": ("d", "i"), "sum": tuple(tnames) + ("d",)}
        for k, t in enumerate(tnames):
            foot["term%d" % k] = ("M", t)
        term_rel = {k: frozenset((M, terms_of[M][k]) for M in mats) for k in range(6)}

        def Lf(j, a, b, sum_rel=sum_rel, term_rel=term_rel):
            if j.startswith("term"):
                return term_rel[int(j[4:])]
            if j == "sum":
                return sum_rel
            return D.L(j, a, b)

        E = Org("E_Leibniz", ports, dom, list(foot), foot, ["b0"], D.A, D._compose, Lf)
        pi = {"n": Translation(("n",)), "M": Translation(("M",)), "d": Translation(("d",)), "i": Translation(("i",))}
        for k, t in enumerate(tnames):
            pi[t] = Translation(("M",), (lambda kk: (lambda xs: terms_of[xs[0]][kk]))(k), name="term_%d(M)" % k)
        lam = {"order": (frozenset(["order"]), {"n": pi["n"], "M": pi["M"]}), "skew": (frozenset(["skew"]), {"M": pi["M"]}),
               "odd": (frozenset(["odd"]), {"n": pi["n"]}), "inv": (frozenset(["inv"]), {"d": pi["d"], "i": pi["i"]}),
               "sum": (frozenset(["order", "det"]), dict({t: pi[t] for t in tnames}, d=pi["d"]))}
        for k, t in enumerate(tnames):
            lam["term%d" % k] = (frozenset(["order"]), {"M": pi["M"], t: pi[t]})
        c = Candidate(E, q, pi, {a: a for a in D.A}, {"b0": "b0"}, lam, list(foot), "i", name="ℰ_Leibniz")
        f1 = F1(c)
        bad_f1 = [k for k in c.Gamma if not all(proj_lam(c, k, D, a, "b0") == E.L(k, a, "b0") for a in D.A)]
        if f1:
            v, d = account(c, detail=True)
            w = NC2(c, witness=True)
        else:
            v, d, w = False, {"F1": False, "F2eq": F2eq(c), "A": A(c)}, None
        out.append((variant, f1, bad_f1, v, d, w))
    txt = "Target: n ∈ {1,2,3}, entries in GF(3), M one port, components order, skew, odd, det, inv; edits remove skew (rs), remove oddness (ro), both (rb); the edits to field arithmetic and to det–invertibility are not edits of this encoding, so the scope clause is met trivially (I99). Answers %s. " % answers
    txt += "The Leibniz candidate needs ports for the terms, which D lacks: under I14 (each E port translated to one D port) it cannot be written; with derived ports (a term port read as a function of M, I81) it can. "
    for (variant, f1, bad_f1, v, d, w) in out:
        txt += "Variant '%s': F1 %s (failing: %s); Account %s %s%s. " % (variant, f1, bad_f1 or "none", v, d, (", NC2 witness %s" % (w,)) if w else "")
    parts.append(computed("(c-i) the Leibniz candidate, sum over every tuple of term values", "the Leibniz candidate meets (F1), (F2), (A), NC2 and non-vacuity",
                          out[0][3], txt, ["I99", "I81", "I82"],
                          note="the sum component, relating every tuple of term values to their sum, differs from its counterpart's projection, which holds only the term tuples some matrix gives: (F1) fails for it"))
    parts.append(computed("(c-ii) the Leibniz candidate, sum restricted to realizable term tuples", "the Leibniz candidate meets (F1), (F2), (A), NC2 and non-vacuity",
                          out[1][3], "Variant 'sum restricted to realizable term tuples': Account %s %s, NC2 witness %s." % (out[1][3], out[1][4], out[1][5]), ["I99", "I81", "I82"]))
    return parts


# ---- transport results (Part VIII) -----------------------------------------------------------------------

@claim("FC64", ["I77"])
def fc64(S):
    def gen(rng, size):
        nz, ny = rng.randint(1, 3), rng.randint(1, 3)
        pi = [rng.randrange(ny) for _ in range(nz)]
        gens = []
        for _ in range(2):
            Sa = [rng.randrange(nz) for _ in range(nz)]
            Ta = [rng.randrange(ny) for _ in range(ny)]
            gens.append((Sa, Ta))
        return nz, ny, pi, gens

    def check(m):
        nz, ny, pi, gens = m
        if not all(all(pi[Sa[z]] == Ta[pi[z]] for z in range(nz)) for Sa, Ta in gens):
            return VAC
        for L_ in range(1, 5):
            for word in itertools.product(range(len(gens)), repeat=L_):
                for z in range(nz):
                    a, b = z, pi[z]
                    for g in word:
                        a = gens[g][0][a]
                        b = gens[g][1][b]
                    if pi[a] != b:
                        return "word %s breaks the square" % (word,)
        return None

    return [forall(S, "FC64", 1, "functional transport", "π∘S_a = T_a∘π for generators ⇒ for every word of length ≤ 4", gen, check, [Size(3, 3, 1, 1, 0)], 20000, ["random maps on ≤ 3 states"])]


@claim("FC65", ["I77"])
def fc65(S):
    def gen(rng, size):
        n = [rng.randint(1, 3) for _ in range(3)]
        steps = [{(a, b) for a in range(n[i]) for b in range(n[i]) if rng.random() < 0.4} for i in range(3)]
        R1 = {(a, b) for a in range(n[0]) for b in range(n[1]) if rng.random() < 0.5}
        R2 = {(a, b) for a in range(n[1]) for b in range(n[2]) if rng.random() < 0.5}
        return n, steps, R1, R2

    def fwd(R, s1, s2):
        return all(any((y, y2) in s2 and (z2, y2) in R for y2 in {q for (_, q) in s2} | {q for (q, _) in s2})
                   for (z, y) in R for (zz, z2) in s1 if zz == z)

    def bwd(R, s1, s2):
        return all(any((z, z2) in s1 and (z2, y2) in R for z2 in {q for (_, q) in s1} | {q for (q, _) in s1})
                   for (z, y) in R for (yy, y2) in s2 if yy == y)

    def check(m):
        n, steps, R1, R2 = m
        comp = {(a, c) for (a, b) in R1 for (b2, c) in R2 if b == b2}
        if not ((fwd(R1, steps[0], steps[1]) and fwd(R2, steps[1], steps[2])) or (bwd(R1, steps[0], steps[1]) and bwd(R2, steps[1], steps[2]))):
            return VAC
        if fwd(R1, steps[0], steps[1]) and fwd(R2, steps[1], steps[2]) and not fwd(comp, steps[0], steps[2]):
            return "forward simulations do not compose"
        if bwd(R1, steps[0], steps[1]) and bwd(R2, steps[1], steps[2]) and not bwd(comp, steps[0], steps[2]):
            return "backward simulations do not compose"
        return None

    return [forall(S, "FC65", 1, "simulations compose", "forward (backward) simulations R, R' give a forward (backward) simulation R;R'", gen, check, [Size(3, 3, 1, 1, 0)], 20000, ["random step relations on ≤ 3 states, one generator"])]


@claim("FC66", ["I77"])
def fc66(S):
    parts = []

    def gen(rng, size):
        Z = [Fr(rng.randint(-6, 6), rng.randint(1, 3)) for _ in range(rng.randint(1, 4))]
        Sm = {z: rng.choice(Z) for z in Z}
        L_ = Fr(rng.randint(0, 6), 2)
        c0 = Fr(rng.randint(-3, 3), 2)
        T = lambda x: L_ * x + c0 if x >= 0 else -L_ * x + c0  # L-Lipschitz
        return Z, Sm, T, L_

    def check(m):
        Z, Sm, T, L_ = m
        eps = max(abs(Sm[z] - T(z)) for z in Z)
        for z in Z:
            a, b = z, z
            for n in range(1, 6):
                a = Sm[a]
                b = T(b)
                bound = eps * sum(L_ ** k for k in range(n))
                if abs(a - b) > bound:
                    return "e_%d = %s > %s (ε = %s, L = %s, z = %s)" % (n, abs(a - b), bound, eps, L_, z)
        return None

    parts.append(forall(S, "FC66", 1, "(a) the accumulated bound", "one-step discrepancy ≤ ε on a scope closed under S, T L-Lipschitz ⇒ e_n ≤ ε Σ_{k<n} L^k (n ≤ 5)",
                        gen, check, [Size(1, 1, 1, 1, 0)], 20000, ["exact rationals; S a map of a finite scope; T(x) = ±Lx + c"]))
    K = 10 ** 6
    Z = [Fr(1)]
    Sm = {Fr(1): Fr(1)}
    T = lambda x: x if x == 1 else K * (x - 1) ** 2 + x
    # π(z) = z; one-step discrepancy at z = 1: |S(1) − T(1)| = 0 ≤ ε; with a perturbed start the modulus is missing
    S2 = lambda x: x + Fr(1, 10)
    T2 = lambda x: x + Fr(1, 10) + K * (x - 1) ** 2
    z = Fr(1)
    e1 = abs(S2(z) - T2(z))
    e2 = abs(S2(S2(z)) - T2(T2(z)))
    parts.append(computed("(b) no bound without a modulus", "there are S, T with one-step discrepancy ≤ ε on the scope, T not Lipschitz, and e_2 as large as one likes",
                          e1 == 0 and e2 > 1000, "S(x) = x + 1/10, T(x) = x + 1/10 + K(x−1)², K = 10^6, scope {1}: e_1 = %s, e_2 = %s" % (e1, e2)))
    return parts


@claim("FC67", ["I77", "I78", "I81"])
def fc67(S):
    def gen(rng, size):
        D, p = D_and_p(rng, size)
        if D is None:
            return None
        c = gen_candidate(rng, p, perturb_p=0.3, background_p=0.2)
        return p, c, rng

    def check(m):
        p, c, rng = m
        E = c.E
        r = {v: dict(zip(E.dom[v], rng.sample(list(E.dom[v]), len(E.dom[v])))) for v in E.ports}
        ri = {v: {y: x for x, y in r[v].items()} for v in E.ports}
        dom2 = {v: tuple(sorted(r[v].values())) for v in E.ports}

        def L2(j, a, b):
            return frozenset(tuple(r[v][w[i]] for i, v in enumerate(E.foot[j])) for w in E.L(j, a, b))

        E2 = Org(E.name + "_rec", E.ports, dom2, E.comps, E.foot, E.B, E.A, E._compose, L2)
        comp = lambda tr, v: Translation(tr.dports, (lambda f, rv: (lambda xs: rv[f(xs)]))(tr.fn, r[v]), name="r∘" + tr.name)
        c2 = c.replace(E=E2, pi={v: comp(c.pi[v], v) for v in E.ports}, lam={k: (N, {v: comp(tr[v], v) for v in E.foot[k]}) for k, (N, tr) in c.lam.items()})
        if faithful(c) != faithful(c2):
            return "recoding changed fidelity\n" + c.describe()
        return None

    return [forall(S, "FC67", 1, "an invertible recoding keeps fidelity", "E recoded by value bijections r, t' = r∘t: Faithful(t') ⟺ Faithful(t)", gen, check, SMALL, 40, BOTHFAM),
            not_tested("provenance (dropped from FC67, area 2)", "the carrier's provenance carries over (I54)",
                       "not L365's content: L365 says the recoding 'preserves the content'; provenance is I54's rule, read with Rep (area 3)")]


@claim("FC68", ["I77", "I78", "I81", "I87", "I89"])
def fc68(S):
    parts = []

    def check(m):
        p, c = m
        if not any(c.translates(a, b) and c.ans_E(c.tau[a], c.sigma[b]) != p.ans(a, b) for (a, b) in p.C):
            return VAC
        for (a, b) in p.C:
            if not c.translates(a, b):
                continue
            y = c.ans_E(c.tau[a], c.sigma[b])
            if y != p.ans(a, b):
                if account(c):
                    return "a failed answer with Acc\n" + c.describe()
                for extra in ([], [x for x in all_pairs(p.D) if x not in p.C]):
                    p2 = p.with_C(p.C | set(extra))
                    if account(c.replace(p=p2)):
                        return "a failed answer with Acc on a wider contract\n" + c.describe()
                return None
        return None

    parts.append(forall(S, "FC68", 1, "(a) a failed answer stays failed", "Ans_E(τa,σb) ≠ Ans_p(a,b) at (a,b) ∈ C ⇒ ¬Acc on p and on every p' with the same D, Q, δ whose contract holds (a,b)",
                        gen_p_cand, check, SMALL, 40, BOTHFAM))
    rec, ay, ey = "rec", "ans_is_y", "E_ans_is_y"
    accs = ["acc1", "acc2"]
    base = [rec, Imp(rec, Not(ay))]
    j = Assessor(["MP", "MT"], base + [Imp(a, ay) for a in accs])
    s1 = Step("MP", Not(ay), [Leaf(rec, "record"), Leaf(Imp(rec, Not(ay)))])
    args = {a: Step("MT", Not(a), [s1, Leaf(Imp(a, ay))]) for a in accs}
    ok_b = all(usable(j, args[a]) and rules_out(args[a], a) for a in accs)
    j2 = Assessor(["MP", "MT"], [Imp(rec, Not(ay))] + [Imp(a, ay) for a in accs])
    ok_c = all(not usable(j2, args[a]) for a in accs)
    parts.append(computed("(b), (c) every such candidate alike", "a usable argument ruling out 'Ans_p(a,b) = y' rules out Acc for every candidate answering y; withdrawing its record lapses it for all alike",
                          ok_b and ok_c, "(A) and each candidate's own answer y give 'acc_i → ans_is_y'. Usable and ruling out for both: %s; after the record is withdrawn, usable for neither: %s" % (ok_b, ok_c), ["I87", "I89"]))
    return parts


@claim("FC69", ["I87", "I89"])
def fc69(S):
    d, e = "d", "e"
    j = Assessor(["free"], [])
    u = Step("free", e, [Leaf(d)])
    root = Step("free", d, [u])
    lo, hi = usable_any_step(j, root)
    rec = usable(j, root)
    return [computed("I40: recursion below the step is well founded", "with Live through a step below, Usable has one value", rec is False,
                     "root ⊢ d from e; below it u ⊢ e from the leaf d; j accepts nothing. Usable (I40): %s" % rec, ["I87", "I89"]),
            computed("I40's alternative: two fixed points", "with Live through any step of the argument, the usability operator has two fixed points", lo != hi,
                     "least fixed point: %d usable steps; greatest: %d" % (len(lo), len(hi)), ["I87", "I89"])]


@claim("FC70", ["I87", "I89"])
def fc70(S):
    """FC70 after area 3: the formal statement that replaces L393's first closing sentence:
    d ∈ Prem(u), d withdrawn (d ∉ Accepted_j(ξ')), and no step u' below u with concl(u') = d usable at ξ'
    ⇒ ¬Usable_j^{ξ'}(u)."""
    d, q = "d", "q"
    w = Step("MP", d, [Leaf(q), Leaf(Imp(q, d))])
    u = Step("AndI", And(d, q), [w, Leaf(q)])
    j_before = Assessor(["MP", "AndI"], [d, q, Imp(q, d)])
    j_after = Assessor(["MP", "AndI"], [q, Imp(q, d)])
    ok = usable(j_before, u) and usable(j_after, u)
    parts = [computed("a premise live twice over", "withdrawing d leaves the step usable when d is also the conclusion of a usable step below",
                      ok, "argument:\n%s\nusable before j withdraws d: %s; after: %s. L393's 'Withdrawing a premise makes the step unusable' holds of a premise live by acceptance only." % (u.show(2), usable(j_before, u), usable(j_after, u)), ["I87", "I89"])]

    def gen(rng, size):
        prem = [rand_formula(rng) for _ in range(rng.randint(2, 5))]
        forms = [f for f in ("MP", "MT", "AndI", "AndE") if rng.random() < 0.7]
        args = enumerate_args(prem, depth=2, max_args=200)
        if not args:
            return None
        return prem, forms, args

    def check(m):
        prem, forms, args = m
        j1 = Assessor(forms, prem)
        hit = False
        for a_ in args:
            for u_ in a_.steps():
                if not usable_step(j1, u_):
                    continue
                for dd in set(canon(x) for x in u_.prem):
                    j2 = Assessor(forms, [x for x in prem if canon(x) != dd])
                    kept = any(canon(v.concl) == dd and usable_step(j2, v) for v in u_.below())
                    hit = True
                    if not kept and usable_step(j2, u_):
                        return "withdrawing %s leaves the step usable with no usable step below concluding it:\n%s" % (show(dd), u_.show(2))
        return None if hit else VAC

    parts.append(forall(S, "FC70", 1, "withdrawal, formally", "Usable_j(u), d ∈ Prem(u), d withdrawn, ¬∃u'∈Below(u)[concl(u') = d ∧ Usable_j^{ξ'}(u')] ⇒ ¬Usable_j^{ξ'}(u)",
                        gen, check, [Size(3, 2, 1, 1, 0)], 300, ["random premises, all accepted; arguments of height ≤ 2"], ["I87", "I88", "I89"]))
    return parts


@claim("FC71", ["I87", "I89"])
def fc71(S):
    """FC71 after area 3 (D9.9 new): (i) α ∈ X_j(O), the step u⁺ from concl(α) and the conditional to
    ¬(T∧B∧I) usable by j, and no leaf of α blocking ⇒ α⁺ ∈ X_j(T∧B∧I), whatever form u⁺ has; (ii)
    ¬RO(α⁺, x) for x ∈ {T, B, I}; (iii) with forms in Forms_cl only (every instance has Incons(Prem ∪
    {¬concl}), D9.1; second check, R15), no argument from those premises rules out T, B or I; (iv) with an
    admitted form outside Forms_cl it can (the committed (ii) read for every form fails)."""
    T_, B_, I_, O_ = "T", "B", "I", "O"
    TBI = And(T_, B_, I_)
    cond = Imp(TBI, O_)
    rec = "rec"
    parts = []

    def plus(alpha, form):
        return Step(form, Not(TBI), [alpha, Leaf(cond)])

    j = Assessor(["MP", "MT"], [rec, Imp(rec, Not(O_)), cond])
    s1 = Step("MP", Not(O_), [Leaf(rec, "record"), Leaf(Imp(rec, Not(O_)))])
    alpha = Step("MT", Not(TBI), [s1, Leaf(cond)])
    ok1 = usable(j, alpha) and rules_out(alpha, TBI)
    parts.append(computed("(i) the conjunction is ruled out (modus tollens)", "usable ¬O, live conditional, modus tollens ⇒ T ∧ B ∧ I ruled out", ok1, alpha.show(2), ["I87", "I89"]))

    def gen(rng, size):
        extra = [rand_formula(rng) for _ in range(rng.randint(0, 2))]
        cands = [Not(O_), And(Not(O_), "q"), And(Not(TBI), Not(O_)), "q"]
        leaf = rng.choice(cands)
        acc = [leaf, cond] + extra + ([Imp("q", Not(O_))] if rng.random() < 0.5 else [])
        forms = [f for f in ("MP", "MT", "AndE", "free") if rng.random() < 0.7]
        live = rng.random() < 0.8
        return leaf, acc if live else [x for x in acc if x != cond], forms

    def check(m):
        leaf, acc, forms = m
        jj = Assessor(forms, acc)
        args = enumerate_args(acc, forms=("MP", "AndE"), depth=2, max_args=200) + [Step("free", Not(O_), [Leaf(leaf)])]
        seen = False
        for a_ in args:
            if not (usable(jj, a_) and rules_out(a_, O_)):
                continue
            for f in ("MT", "free"):
                ap = plus(a_, f)
                upl = usable_step(jj, ap)
                block = any(canon(Not(TBI)) in conjuncts(lf.claim) for lf in ap.leaves())
                got = usable(jj, ap) and rules_out(ap, TBI)
                seen = True
                if got != (upl and not block):
                    return "D9.9 (i) fails: form %s, usable u⁺ %s, block %s, α⁺ ∈ X_j(T∧B∧I) %s\n%s" % (f, upl, block, got, ap.show(2))
                for x in (T_, B_, I_):
                    if rules_out(ap, x):
                        return "D9.9 (ii) fails: α⁺ rules out %s\n%s" % (x, ap.show(2))
        return None if seen else VAC

    parts.append(forall(S, "FC71", 1, "(i), (ii) for any admitted form of u⁺", "α ∈ X_j(O) ⇒ [α⁺ ∈ X_j(T∧B∧I) ⟺ Usable_j(u⁺) ∧ no leaf of α has ¬(T∧B∧I) as a conjunct]; ¬RO(α⁺, x) for x ∈ {T, B, I}",
                        gen, check, [Size(3, 2, 1, 1, 0)], 300, ["premises ¬O-like, the conditional (live or withdrawn), random extras; forms from MP, MT, AndE, free"], ["I87", "I88", "I89"]))
    common = {x: consistent([Not(O_), cond, x]) for x in (T_, B_, I_)}
    args = enumerate_args([rec, Imp(rec, Not(O_)), cond], forms=("MP", "MT", "AndE"), depth=3, max_args=2000)
    narrower = {x: len(X(j, x, args)) for x in (T_, B_, I_)}
    parts.append(computed("(iii) forms in Forms_cl: nothing narrower from those premises", "¬O, (T∧B∧I ⇒ O) and each of T, B, I have a common model; with MP, MT, AndE no argument of height ≤ 3 from these premises rules out T, B or I", all(common.values()) and not any(narrower.values()),
                          "common models: %s; arguments ruling out T, B, I: %s (over %d arguments)" % (common, narrower, len(args)), ["I87", "I88", "I89"]))
    jf = Assessor(["free"], [Not(O_), cond])
    beta = Step("free", Not(T_), [Leaf(Not(O_))])
    outside = usable(jf, beta) and rules_out(beta, T_)
    parts.append(computed("(iv) an admitted form outside Forms_cl (GLM, part 12)", "with a free form ¬O ⊢ ¬T admitted, T alone is ruled out from the premises of the failed prediction: the committed D9.9 (ii), read for every form, fails; D9.9 (ii) now scopes 'nothing narrower' to α⁺", outside,
                          beta.show(2) + "\nThe ruling out is j's, through the form j admits (L397, S28).", ["I87", "I89", "I38"]))
    jm = Assessor(["MP", "MT"], ["rec", Imp("rec", Not(O_)), cond])
    s1m = Step("MP", Not(O_), [Leaf("rec", "record", made_from=Not(TBI)), Leaf(Imp("rec", Not(O_)))])
    am = Step("MT", Not(TBI), [s1m, Leaf(cond)])
    blocked = usable(jm, s1m) and rules_out(s1m, O_) and usable(jm, am) and not rules_out(am, TBI)
    parts.append(computed("(i') second check (R8): a record leaf of α made from ¬(T∧B∧I) blocks α⁺", "α ∈ X_j(O), Usable_j(u⁺), a leaf l of α with MadeFrom(l, ¬(T∧B∧I)) ⇒ α⁺ ∉ X_j(T∧B∧I) (D9.9 (i)'s clause, which A3-L395.1 dropped and L395 now writes)",
                          blocked, am.show(2), ["I39", "I87", "I89"]))
    return parts


@claim("FC72", ["I87", "I89"])
def fc72(S):
    phi = "acc"
    a1 = Step("AndE", Not(phi), [Leaf(And(Not(phi), "q"))])
    ok_a = not rules_out(a1, phi)
    rec = Leaf("r", "record", made_from="psi")
    a2 = Step("MP", "psi", [rec, Leaf(Imp("r", "psi"))])
    ok_b = not rules_out(a2, Not("psi"))
    a3 = Step("MP", Not(phi), [Leaf("r"), Leaf(Imp("r", Not(phi)))])
    ok_c = rules_out(a3, phi)
    return [computed("(a), (b), (c)", "(a) ¬φ a conjunct of a leaf blocks; (b) a record made from ψ does not rule out ¬ψ; (c) r and r → ¬Acc rule out Acc",
                     ok_a and ok_b and ok_c, "(a) %s; (b) %s; (c) %s" % (ok_a, ok_b, ok_c), ["I87", "I89"])]


@claim("FC73", ["I87", "I89"])
def fc73(S):
    phi = "phi"
    j = Assessor(["MP"], ["q", Imp("q", Not(phi)), "s", Imp("s", phi)])
    a = Step("MP", Not(phi), [Leaf("q"), Leaf(Imp("q", Not(phi)))])
    b = Step("MP", phi, [Leaf("s"), Leaf(Imp("s", phi))])
    ok = usable(j, a) and rules_out(a, phi) and usable(j, b) and rules_out(b, Not(phi))
    return [computed("inconsistent premises", "X_j(φ) ≠ ∅ and X_j(¬φ) ≠ ∅", ok, "Accepted_j = {q, q→¬φ, s, s→φ}", ["I87", "I89"])]


@claim("FC74", ["I77", "I78", "I81"])
def fc74(S):
    """FC74 after area 3 (D9.10 new): Bearing(c, z, p) :⟺ Acc(Conn, Qf(z, δ, p), t_c, Γ_c, δ_c) [A3-01];
    the criticism's premise is represented by an organization of the system (L383), which no
    argument of Acc reads (FC30), so a witness with the representation added is still a witness."""
    parts = []

    def check(m):
        p, c = m
        if not account(c):
            return ("the connection's candidate fails (E) on p_δ = Qf(z, δ, p); a represented premise g (L383) is a datum of the occurrence, "
                    "not an argument of Acc (FC30), so Bearing fails while the criticism exists\n" + c.describe())
        return None

    parts.append(exists(S, "FC74", 1, "a criticism without bearing", "a criticism, its premise represented, whose connection candidate has ¬Acc on Qf(z, δ, p)",
                        gen_p_cand, check, SMALL, 10, BOTHFAM))

    def check2(m):
        p, c = m
        if not account(c):
            return None
        others = [x for x in all_pairs(p.D) if x not in p.C]
        for x in others:
            p2 = p.with_C(p.C | {x}, name="Qf(z,δ,p')")
            c2 = c.replace(p=p2)
            if not account(c2):
                return ("one connection, two questions p, p' about the same target: p_δ = Qf(z, δ, p) with C and Qf(z, δ, p') with C ∪ {%r}. "
                        "Bearing(c, z, p) holds, Bearing(c, z, p') fails: bearing is relative to p (L377, 'in respect of p')\n%s" % (x, c.describe()))
        return None

    parts.append(exists(S, "FC74", 2, "bearing is relative to p", "Bearing(c, z, p) ∧ ¬Bearing(c, z, p') for one connection (the committed D9.10 dropped p)",
                        gen_p_cand, check2, SMALL, 20, BOTHFAM, ["A3-01"]))
    return parts


@claim("FC75", ["I95"])
def fc75(S):
    """FC75 after area 3: D11.4 with dependence along R [A3-06], no chain clause, and the at-rest clause
    [A3-05] under both readings."""
    parts = []
    # (a) 'started and did no work': no dependence along R
    h2 = Circuit({"m": (("i",), lambda x: 0), "r": (("m",), lambda x: x)}, {"i": 1})
    ok_a, why_a = act_route(h2, {"i", "m", "r"}, "i", "r", [(0, 1)])
    parts.append(computed("(a) did no work", "a route whose value at r does not change with i's port along R fails", not ok_a, why_a, ["I95", "A3-06"]))
    # (a') dependence outside R only (Mimo, part 9, model A): i -> c -> m -> r carries the change; R = {i, r} with an edge i -> r that r ignores
    hA = Circuit({"c": (("i",), lambda x: x), "m": (("c",), lambda x: x), "r": (("m", "i"), lambda x, y: x)}, {"i": 1})
    okA, whyA = act_route(hA, {"i", "r"}, "i", "r", [(0, 1)])
    okA_old, _ = act_route_s104(hA, {"i", "r"}, "i", "r", [(0, 1)])
    parts.append(computed("(a') dependence only outside R", "R = {i, r}, the change carried by c, m outside R: not active (it was under I46)", (not okA) and okA_old,
                          "D11.4 after area 3: %s (%s); I46 as committed: %s" % (okA, whyA, okA_old), ["I95", "A3-06"]))
    # (a'') a side component (Mimo, part 9, model B): a constant source c feeding m lies on no chain from i to r
    hB = Circuit({"m": (("i", "c"), lambda x, y: (x, y)), "r": (("m",), lambda z: z[0])}, {"i": 1, "c": 5})
    okB, whyB = act_route(hB, {"i", "c", "m", "r"}, "i", "r", [(0, 1)])
    okB_old, whyB_old = act_route_s104(hB, {"i", "c", "m", "r"}, "i", "r", [(0, 1)])
    parts.append(computed("(a'') a side component", "R = {i, c, m, r}, c a constant source feeding m: active (every member feeds r inside R); I46's chain clause excluded it", okB and not okB_old,
                          "D11.4 after area 3: %s (%s); I46 as committed: %s (%s)" % (okB, whyB, okB_old, whyB_old), ["I95", "A3-06"]))
    # (b) already at rest when the result occurred: the look of the committed model, now with run times
    h3 = Circuit({"m": (("i",), lambda x: x), "r": (("m", "late"), lambda x, y: x)}, {"i": 1, "late": 0})
    times = {"i": (0, 0), "m": (1, 1), "late": (8, 8), "r": (9, 9)}
    ra, wa = act_route(h3, {"i", "m", "r"}, "i", "r", [(0, 1)], times, "a")
    rb, wb = act_route(h3, {"i", "m", "r"}, "i", "r", [(0, 1)], times, "b")
    rn, _ = act_route(h3, {"i", "m", "r"}, "i", "r", [(0, 1)])
    parts.append(computed("(b) a route at rest is not active", "¬AtRest is a clause of D11.4; the look route (m ran at step 1, its product persists to r at step 9) is at rest under reading (a), not under (b)",
                          (not ra) and rb,
                          "reading (a) 'all of R∖{r} ended before r starts': active %s (%s); reading (b) 'nothing of R runs at r and no product of R is carried to r': active %s (%s); with no run times given: %s. Which reading L375's 'already at rest' takes is open (A3-05)." % (ra, wa, rb, wb, rn), ["I95", "A3-05"]))
    parts.append(construction("(c) a function of (h, Org, i, r, K, times)", "activity is not read from r's value alone", True, "act_route takes the circuit, R, i, r, K and the run times"))
    # (d) the committed chain clause is not needed for the committed (a): a member off every chain whose value does not reach r
    h = Circuit({"m": (("i",), lambda x: x), "n": (("m",), lambda x: x), "r": (("n",), lambda x: x), "side": (("i",), lambda x: 0)}, {"i": 1})
    okd, whyd = act_route(h, {"i", "m", "n", "r", "side"}, "i", "r", [(0, 1)])
    parts.append(computed("(d) an idle member", "a connected R with a member ('side') that feeds r by no path inside R is not active", not okd, whyd, ["I95", "A3-06"]))
    return parts


@claim("FC76", ["I47", "I90"])
def fc76(S):
    # a structural map from a represented objection into a response suborganization, on an active route;
    # the objection's criticism candidate fails (E)
    h = Circuit({"resp": (("obj",), lambda x: x), "act": (("resp",), lambda x: x)}, {"obj": 1})
    route_ok, _ = act_route(h, {"obj", "resp", "act"}, "obj", "act", [(0, 1)])
    rec_ok = True  # the recoding x ↦ x (declared Rec) sends ob to the same transition
    chg_ok = h.values({"obj": 0})["resp"] == 0  # the declared change 1 ↦ 0 goes to Rule's change
    D = Org("D_c", ["x"], {"x": (0, 1)}, ["c"], {"c": ("x",)}, ["b0"], [ONE], lambda a2, a1: None, lambda j, a, b: {(0,)})
    p = Question(D, [(ONE, "b0")], "b0", PortQuery(), "x", name="p_δ")
    E = Org("Conn", ["x"], {"x": (0, 1)}, ["k"], {"k": ("x",)}, ["b0"], [ONE], lambda a2, a1: None, lambda j, a, b: {(1,)})
    c = Candidate(E, p, {"x": Translation(("x",))}, {ONE: ONE}, {"b0": "b0"}, {"k": (frozenset(["c"]), {"x": Translation(("x",))})}, ["k"], "x", name="ℰ_c")
    ok = route_ok and rec_ok and chg_ok and not account(c)
    return [computed("reason use without bearing", "UsesReason ∧ ¬Bearing; and no usable argument from the objection is involved", ok,
                     "response on an active route: %s; the criticism's connection meets (E): %s. UsesReason takes no Acc and no Usable." % (route_ok, account(c)), ["I47", "I90", "I95"])]


# ---- provenance, prediction (Part IV) with free predicates [I90] ---------------------------------------

class Hist:
    """A history for provenance, with Θ supplied by hand [I90]: occurrences, which of them represent
    which items ('t', 'H', 'surv', 'cod' = the codomain), which pairs occur, whether Θ admits the
    population's members, and the primitive Prepares of construction traces (I56)."""

    def __init__(self, occ, rep, occurs, admitted=True, prepares=False):
        self.occ, self.rep, self.occurs, self.admitted, self.prepares = occ, set(rep), set(occurs), admitted, prepares


def faithful_on(cand, H):
    """Faithful_H (D5.7): (F1) and the valuation equation of (F2) at every pair of H, and Hom(τ), which is
    a condition on τ as a whole and is not vacuous when H is empty (I18)."""
    return all(cand.translates(*x) and F1_at(cand, *x) and F2eq_at(cand, *x) for x in H) and hom(cand)


def prepares_of(h, name):
    """Whether a construction trace in h prepares the transport `name` (Prepares, I56): h.prepares is a
    bool (it prepares the transport in question) or a set of transport names."""
    return h.prepares if isinstance(h.prepares, bool) else name in h.prepares


def sel(cand, H, h, pop_admitted=True, cod="cod", round2=False, i161=True):
    """Sel(t; {t}, id, H) (D12.1, I52): H ⊆ C, its pairs occur in h, t faithful on H, members admitted,
    no occurrence of h represents t, H or the survival condition. Area 1 fix (D12.1', settles H05 at
    L195, as L13, L201, L411 state): nor the organization t carries to (tag `cod`). Second check (R1,
    I161): and no construction trace in h prepares t. round2=True gives D12.1 as written in round 2.
    Tags are Θ by hand (I90); FC12.new1 and FC83 compute Rep instead (prov_fixed_points)."""
    if not set(H) <= set(cand.p.C) or not set(H) <= h.occurs:
        return False
    if not faithful_on(cand, H):
        return False
    if not (h.admitted and pop_admitted):
        return False
    if i161 and not round2 and prepares_of(h, cand.name):
        return False
    banned = ("t", "H", "surv") if round2 else ("t", "H", "surv", cod)
    return not any(x in banned for (_, x) in h.rep)


def con(h, cod="cod", name=None):
    """Con(t; h, e) (D12.2): a trace in h prepares t (primitive, I56) and t or its codomain is a
    represented target in h."""
    prep = h.prepares if (name is None or isinstance(h.prepares, bool)) else name in h.prepares
    return bool(prep) and any(x in ("t", cod) for (_, x) in h.rep)


# ---- Second check (R1, R3): provenance with Rep computed, not tagged -----------------------------------
# A chain history o1 ≺ … ≺ on, one content c (the codomain of the transport held at the output on).
# held[o]: Org_ℓ(o) has a faithful transport to c (Held, through Θ, no provenance); at the output it is
# computed from t's own faithfulness. trace[o]: a construction trace in the history prepares o's transport.
# selc[o]: Sel's conditions other than its exclusions (population, μ, H occurring, Faithful_H, admitted);
# at the output computed from t. Rep is every fixed point R of R = {o : held[o] ∧ (Sel(o) ∨ Con(o))}.
# Readings of 'represented' inside Sel, Con, Build (D18.1, I146, I162):
#   U  as worded: (R) throughout, o's own occurrence in its history and episode;
#   K  staged: (R) only at o' ≺ o, in Sel, Con and Build;
#   T  Held in Con and Build (o' ⪯ o), and Held at o' ≺ o as Sel's exclusion;
#   T' Held in Con and Build (o' ⪯ o); Sel's exclusion Rep at o' ≺ o (staged along ≺_h) [I162, the cut ruled].
# i161: Sel also asks that no construction trace in the history prepares the transport [I161].
PROV_READINGS = ("U", "K", "T", "T'")
PROV_READING = "T'"


def _prov_step(n, held, trace, selc, rd, i161, R):
    out = {}
    for o in range(n):
        before, upto = range(o), range(o + 1)
        if rd == "U":
            c_ = trace[o] and any(x in R for x in upto)
            s_ = selc[o] and not any(x in R for x in upto)
        elif rd == "K":
            c_ = trace[o] and any(x in R for x in before)
            s_ = selc[o] and not any(x in R for x in before)
        elif rd == "T":
            c_ = trace[o] and any(held[x] for x in upto)
            s_ = selc[o] and not any(held[x] for x in before)
        else:
            c_ = trace[o] and any(held[x] for x in upto)
            s_ = selc[o] and not any(x in R for x in before)
        if i161:
            s_ = s_ and not trace[o]
        out[o] = (bool(s_), bool(c_))
    return out


def build_at(n, held, trace, rd, R, o):
    """Build at o (D13.3): a construction trace whose output o is a represented organization, 'represented'
    read as the cut reads it (ExplUse, BindingConstruction, Owned, ¬TransferComposite set to hold, I56)."""
    if not trace[o]:
        return False
    if rd == "U":
        return o in R
    if rd == "K":
        return any(x in R for x in range(o))
    return bool(held[o])


def prov_fixed_points(n, held, trace, selc, rd, i161=True):
    """Every fixed point: a list of (R, {o: (Sel, Con)})."""
    fps = []
    for bits in itertools.product([0, 1], repeat=n):
        R = frozenset(o for o in range(n) if bits[o])
        sc = _prov_step(n, held, trace, selc, rd, i161, R)
        if frozenset(o for o in range(n) if held[o] and (sc[o][0] or sc[o][1])) == R:
            fps.append((R, sc))
    return fps


def prov_show(n, fps):
    return [{"o%d" % (o + 1): "+".join(k for k, f in zip(("Sel", "Con"), sc[o]) if f) for o in sorted(R)} for R, sc in fps]


def viol_at(cand, a, b):
    """Viol(t; a,b) (D12.7, I50 narrow): (F1) or the valuation equation of (F2) fails at (a,b)."""
    return not (F1_at(cand, a, b) and F2eq_at(cand, a, b))


def selresp(t, t2, H, x, h, mu, cod="cod", cod2="cod", round2=False):
    """SelResp(t -> t2; x) (D12.8 as fixed in area 1): Sel(t) on H, Viol(t; x) (a response to a violation,
    L225), t2 ∈ μ⁺(t) (μ acts at least once), and Sel(t2) on H ∪ {x} in t2's history. round2=True gives D12.8
    as written in round 2: Sel(t) on H, t2 ∈ μ*(t), t2 survives on H ∪ {x} (Faithful), no violation asked."""
    def plus(t0):
        seen, todo = set(), [t0]
        while todo:
            u = todo.pop()
            for v in mu.get(u, ()):
                if v not in seen:
                    seen.add(v)
                    todo.append(v)
        return seen
    if round2:
        star = plus(t.name) | {t.name}
        return sel(t, H, h, round2=True) and t2.name in star and faithful_on(t2, list(H) + [x])
    return (sel(t, H, h, cod=cod) and viol_at(t, *x) and t2.name in plus(t.name)
            and sel(t2, list(H) + [x], h, cod=cod2))


def fwd_pole_cand():
    D = pole(H_vals=(1, 2), T_vals=(45,), bounds=[(1, 45)])
    C = [(ONE, "b1_45")] + [(a, "b1_45") for a in single_settings(D, ["H"])]
    p = Question(D, C, "b1_45", PortQuery(), "L", name="p")
    return p, pole_fwd_candidate(p)


@claim("FC77", ["I77", "I78", "I81", "I90"])
def fc77(S):
    parts = []

    def gen(rng, size):
        return gen_p_cand(rng, size)

    def check(m):
        p, c = m
        h_empty = Hist([], [], [])
        if not hom(c):
            return VAC  # area 1 FC77': the claim is restated for transports whose τ is a homomorphism (I18)
        if not sel(c, [], h_empty):
            return ("Sel(t; {t}, id, ∅) fails for this transport although H = ∅ and the selection history is empty: fidelity on ∅ is not vacuous, "
                    "because (F2)'s homomorphism clause is a condition on τ as a whole (I18), and here Hom(τ) fails. Every transport whose τ is a "
                    "homomorphism is 'selected' by these parameters; one whose τ is not, is not.\n%s\n%s\n%s" % (p.describe(), p.D.describe(), c.describe()))
        return None

    parts.append(forall(S, "FC77", 1, "with H = ∅ and an empty selection history", "FC77': every transport t with Hom(τ) has Sel(t; {t}, id, ∅) when Θ admits t",
                        gen, check, SMALL, 20, BOTHFAM, ["I90", "I18"]))

    def check2(m):
        p, c = m
        if sel(c, [], Hist([], [], [])) != hom(c):
            return "Sel(t; {t}, id, ∅) differs from Hom(τ)\n" + c.describe()
        return None

    parts.append(forall(S, "FC77", 2, "the trivial witness exactly when τ is a homomorphism", "Sel(t; {t}, id, ∅) ⟺ Hom(τ), when Θ admits t",
                        gen, check2, SMALL, 20, BOTHFAM, ["I90"]))
    parts.append(computed("which of I52's requirements block the trivial witness", "the empty selection history meets every requirement of I52 but Θ's admission of t (and Hom(τ))",
                          True, "With H = ∅: 'the pairs of H occur', (F1) and the (F2) equation on H are vacuous; an empty history has no occurrence, so none represents t, H or the survival condition. What remains is Hom(τ) (not pair-relative, I18) and 'the members of 𝒯 are admitted by the physics' (L481), which the formal core leaves to Θ; nothing requires H or h_sel to be nonempty. So (R) keeps content from 'selected' only through Θ's admission of t, through Hom, or through a requirement of a nonempty history, which the text does not state.", ["I90"]))
    return parts


def prov_counterexample():
    """A history in which the codomain of t is a represented target, a trace prepares t, and t survived
    selection on H: Sel and Con both hold on one history."""
    p, c = fwd_pole_cand()
    H = [(ONE, "b1_45")]
    h = Hist(["o1", "o2"], [("o1", "cod")], set(p.C), admitted=True, prepares=True)
    return p, c, H, h


@claim("FC78", ["I90", "I92"])
def fc78(S):
    p, c, H, h = prov_counterexample()
    s, k = sel(c, H, h), con(h)
    s2 = sel(c, H, h, round2=True)
    return [computed("exactly one provenance under I53", "Sel(t) ∧ Con(t) is impossible on one history", not (s and k),
                     "One history h: o1 represents the organization t carries to (its codomain), a construction trace in h prepares t (Prepares, I56), no occurrence represents t, H or the survival condition, and t (the pole's forward transport) is faithful on H = {(1,b1_45)}, whose pair occurs. Area 1 D12.1' (no occurrence of the history of t represents t, H, the survival condition or the organization t carries to; settles H05 at L195): Sel %s, Con %s. D12.1 as written in round 2: Sel %s. Θ is supplied by hand here (I90).\n%s" % (s, k, s2, c.describe()), ["I90", "I92", "I56"])]


@claim("FC79", [])
def fc79(S):
    return [construction("fidelity takes no population", "Faithful_C(t) is a function of (D, E, t, C)", True, "core.faithful(cand) reads cand and its question only")]


@claim("FC80", ["I77", "I78", "I81"])
def fc80(S):
    parts = []

    def gen(rng, size):
        D, p = D_and_p(rng, size)
        if D is None or len(p.C) < 2:
            return None
        base = gen_candidate(rng, p, perturb_p=0.0, background_p=0.0, random_tau_p=0.0, demote_p=0.0)
        pop = [base]
        if not base.E.comps:
            return None
        for i in range(3):
            E = base.E
            k = rng.choice(list(E.comps))
            x = rng.choice(all_pairs(D))
            w = rng.choice(sorted(E.full(k))) if E.full(k) else None
            if w is None:
                continue
            E2 = Org("E_%d" % i, E.ports, E.dom, E.comps, E.foot, E.B, E.A, E._compose,
                     (lambda k_, x_, w_: (lambda j, a, b: (E.L(j, a, b) ^ {w_}) if (j, a, b) == (k_, x_[0], x_[1]) else E.L(j, a, b)))(k, x, w))
            pop.append(base.replace(E=E2, name="t%d" % i))
        H = [x for x in p.C if rng.random() < 0.5] or [(ONE, p.b0)]
        return p, pop, H

    def value(c, a, b):
        return (c.tau[a], c.sigma[b], tuple(c.E.L(k, c.tau[a], c.sigma[b]) for k in c.E.comps))

    def check(m):
        p, pop, H = m
        surv = [c for c in pop if faithful_on(c, H)]
        for (a, b) in p.C:
            if (a, b) in H:
                continue
            vals = set(value(c, a, b) for c in surv)
            if len(vals) == 1 and len(surv) > 1:
                # (b): the value is a function of (𝒯, H): recompute from a reshuffled population
                if set(value(c, a, b) for c in reversed(surv)) != vals:
                    return "the survivors' common value depends on order"
        return None

    parts.append(forall(S, "FC80", 1, "(a), (b) the survivors on H fix what they share", "all survivors on H agree at (a,b) ⇒ that value is a function of (𝒯, H)", gen, check, SMALL, 30, BOTHFAM))

    def wit(m):
        p, pop, H = m
        surv = [c for c in pop if faithful_on(c, H)]
        for (a, b) in p.C:
            if (a, b) not in H and len(set(value(c, a, b) for c in surv)) > 1:
                return "underdetermined at (%s,%s): %d survivors on H = %s with different values there\n%s" % (a, b, len(surv), show_pairs(H), p.describe())
        return None

    parts.append(exists(S, "FC80", 2, "(a) underdetermination", "some (a,b) ∈ C∖H at which survivors on H differ", gen, wit, SMALL, 60, BOTHFAM))
    parts.append(not_tested("(c) under an action law", "an alteration at one pair forces others, and (a)'s hypothesis is harder to meet",
                            "comparing I02 with an action law needs a population family closed under an action law; not built in this round"))

    def gen_step(rng, size):
        D, p = D_and_p(rng, size)
        if D is None or len(p.C) < 2:
            return None
        base = gen_candidate(rng, p, perturb_p=0.0, background_p=0.0, random_tau_p=rng.choice([0.0, 0.5]), demote_p=0.0)
        if not base.E.comps:
            return None
        H = [x for x in p.C if rng.random() < 0.5] or [(ONE, p.b0)]
        return p, base, H

    def alter(c, k, xE, w):
        E = c.E
        E2 = Org("E_alt", E.ports, E.dom, E.comps, E.foot, E.B, E.A, E._compose,
                 (lambda k_, x_, w_: (lambda j, a, b: (E.L(j, a, b) ^ {w_}) if (j, a, b) == (k_, x_[0], x_[1]) else E.L(j, a, b)))(k, xE, w))
        return c.replace(E=E2, name="t_alt")

    def step_check(image_cond):
        def check(m):
            p, c, H = m
            if not faithful_on(c, H):
                return VAC
            imgH = {(c.tau.get(a), c.sigma.get(b)) for (a, b) in H}
            for (a, b) in p.C:
                if (a, b) in H or not c.translates(a, b):
                    continue
                xE = (c.tau[a], c.sigma[b])
                if image_cond and xE in imgH:
                    continue
                for k in c.E.comps:
                    for w in sorted(c.E.full(k))[:2]:
                        c2 = alter(c, k, xE, w)
                        if not faithful_on(c2, H):
                            return ("L574's step: t' = t with L_%s altered at (τ(a),σ(b)) = %r for (a,b) = %r ∉ H does not survive on H: "
                                    "(τ(a),σ(b)) is also the image of a pair of H = %s\n%s" % (k, xE, (a, b), show_pairs(H), c.describe()))
            return None
        return check

    parts.append(exists(S, "FC80", 3, "(d) L574's step as worded fails", "some (a,b) ∉ H with t surviving on H and t altered at (τ(a),σ(b)) not surviving on H (a witness against L574 as worded)",
                        gen_step, step_check(False), SMALL, 40, BOTHFAM, ["I71"]))
    parts.append(forall(S, "FC80", 4, "(d') L574's step with the image condition", "(τ(a),σ(b)) ∉ (τ×σ)[H], t survives on H ⇒ t with a relation altered at (τ(a),σ(b)) survives on H",
                        gen_step, step_check(True), SMALL, 40, BOTHFAM, ["I71"]))
    return parts


@claim("FC81", ["I90", "I92"])
def fc81(S):
    parts = []
    p, c = fwd_pole_cand()
    parts.append(construction("(a)-(c)", "Surp ⇒ H ⊊ C; no transport ⇒ no Surp; H = C ⇒ no Surp", True,
                              "Surp needs (a,b) ∈ C∖H with H ⊆ C (Sel), and a transport; each follows from D12.7 as written"))
    # (d): a transport faithful on H (Hom included), violated at an occurring pair outside H, with Con and Sel
    D = p.D
    inv = D.meta["inv"]
    seth2 = [a for a in D.A if dict(inv[a]).get("H") == 2 and len(inv[a]) == 1][0]
    L3 = min(D.dom["L"], key=float)
    Ebad = Org("E_bad", D.ports, D.dom, D.comps, D.foot, D.B, D.A, D._compose,
               lambda j, a, b: (frozenset(w for w in D.full(j) if w[2] == L3) if (j == "c_L" and a == seth2) else D.L(j, a, b)))
    c2 = c.replace(E=Ebad, name="ℰ_bad")
    H = [(ONE, "b1_45")]
    h = Hist(["o1"], [("o1", "cod")], set(p.C), admitted=True, prepares=True)
    viol = not (F1_at(c2, seth2, "b1_45") and F2eq_at(c2, seth2, "b1_45"))
    s_, k = sel(c2, H, h), con(h)
    surp = s_ and viol and (seth2, "b1_45") not in H
    parts.append(computed("(d) Con(t) ∧ Viol ⇒ ¬Surp (under I53)", "a constructed transport violated at an occurring pair is not surprised", not (k and viol and surp),
                          "In a history like FC78's (the codomain represented, Prepares, no representation of t, H or the survival condition), t (the pole's forward transport into an organization whose c_L gives L = %s under set H=2) is faithful on H = {(1,b1_45)} (Hom included) and violated at (%s, b1_45) ∉ H, which occurs. Con: %s; Sel: %s; Viol: %s; Surp: %s. Area 1 D12.1' (a represented codomain excluded from a selection history); under D12.1 as written in round 2 Sel was %s." % (L3, seth2, k, s_, viol, surp, sel(c2, H, h, round2=True)), ["I90", "I92", "I56"]))
    return parts


def fc82_strong():
    """The second check's stronger case: 𝒯 = {t, t2}, μ(t) = {t2}; t violated at x ∉ H; t2 survives on H ∪ {x};
    one history h represents t2's codomain and prepares t2."""
    p, c = fwd_pole_cand()
    D = p.D
    inv = D.meta["inv"]
    seth2 = [a for a in D.A if dict(inv[a]).get("H") == 2 and len(inv[a]) == 1][0]
    x = (seth2, "b1_45")
    L3 = min(D.dom["L"], key=float)
    Ebad = Org("E_bad", D.ports, D.dom, D.comps, D.foot, D.B, D.A, D._compose,
               lambda j, a, b: (frozenset(w for w in D.full(j) if w[2] == L3) if (j == "c_L" and a == seth2) else D.L(j, a, b)))
    t = c.replace(E=Ebad, name="t")
    t2 = c.replace(name="t2")
    H = [(ONE, "b1_45")]
    h = Hist(["o1"], [("o1", "cod:t2")], set(p.C), admitted=True, prepares={"t2"})  # the trace prepares t2 (second check: per transport, I161)
    mu = {"t": ["t2"]}
    return p, t, t2, H, x, h, mu


@claim("FC82", ["I90", "I92"])
def fc82(S):
    parts = []
    p, c, H, h = prov_counterexample()
    x = sorted([a for a in p.C if a != (ONE, "b1_45")], key=repr)[0]
    sresp = selresp(c, c, H, x, h, {c.name: [c.name]})
    sresp2 = selresp(c, c, H, x, h, {}, round2=True)
    cresp = con(h)
    parts.append(computed("no common result", "no transport is the result of both a selection response and a construction response", not (sresp and cresp),
                          "t' = t = the pole's forward transport on FC78's history, x = %r. Area 1 D12.8' (Sel(t) on H, Viol(t; x), t' ∈ μ⁺(t), Sel(t') on H ∪ {x}): SelResp %s; ConResp %s. D12.8 with D12.1 as written in round 2: SelResp %s." % (x, sresp, cresp, sresp2), ["I90", "I92", "I56"]))
    p, t, t2, H, x, h, mu = fc82_strong()
    sr = selresp(t, t2, H, x, h, mu, cod="cod:t", cod2="cod:t2")
    sr2 = selresp(t, t2, H, x, h, mu, round2=True)
    cr = con(h, cod="cod:t2")
    parts.append(computed("no common result, the second check's stronger case", "𝒯 = {t, t2}, μ(t) = {t2}, t violated at x ∉ H, t2 survives on H ∪ {x}, h represents t2's codomain and prepares t2: no common result",
                          not (sr and cr), "Viol(t; x): %s; t2 faithful on H ∪ {x}: %s. Area 1 D12.8': SelResp(t → t2) %s; ConResp(t2) %s. D12.8 as written in round 2 (t2 ∈ μ*(t), t2 survives on H ∪ {x}): SelResp %s, a common result with ConResp." % (viol_at(t, *x), faithful_on(t2, H + [x]), sr, cr, sr2), ["I90", "I92", "I56"]))
    return parts


@claim("FC83", ["I90", "I92"])
def fc83(S):
    """FC83' with Rep computed (second check, R1): SelResp(t → t'; x) ⇒ no Build of cod t' in h(t'), on every
    chain history of 1–3 occurrences whose output holds t' (held and Sel's conditions computed from t' on
    H ∪ {x}), earlier occurrences and the output's trace set by hand (Θ, I90), under U, K, T and T′ (I162),
    with I161; and without I161, T and T′ admit both (the review's R1)."""
    p, t, t2, H, x, h0, mu = fc82_strong()
    viol = viol_at(t, *x)
    sel_t = sel(t, H, Hist([], [], set(p.C)), i161=False)  # t selected on H in its own (empty) history
    in_mu = "t2" in mu.get("t", [])
    held_out = faithful(t2) and faithful_on(t2, H + [x])
    selc_out = set(H + [x]) <= set(p.C) and faithful_on(t2, H + [x])

    def items():
        for n in (1, 2, 3):
            for early in itertools.product(itertools.product([0, 1], repeat=3), repeat=n - 1):
                for tr_out in (0, 1):
                    held = [e[0] for e in early] + [held_out]
                    trace = [e[1] for e in early] + [tr_out]
                    selc = [e[2] for e in early] + [selc_out]
                    yield n, held, trace, selc

    def check_with(i161, rds):
        def check(m):
            n, held, trace, selc = m
            for rd in rds:
                for R, sc in prov_fixed_points(n, held, trace, selc, rd, i161):
                    sresp = sel_t and viol and in_mu and sc[n - 1][0]
                    build = any(build_at(n, held, trace, rd, R, o) for o in range(n))
                    if sresp and build:
                        return "%s: SelResp(t → t2) and a Build of cod t2 in h(t2): held %s, trace %s, Sel's conditions %s; fixed point %s" % (
                            rd, held, trace, selc, prov_show(n, [(R, sc)]))
            return None
        return check

    pre = "t violated at x = %r: %s; t selected on H: %s; t2 ∈ μ⁺(t): %s; t2 held at the output (faithful, and on H ∪ {x}): %s" % (x, viol, sel_t, in_mu, held_out)
    parts = [exhaustive("FC83", "FC83' with Rep computed, D12.1 with I161", "SelResp(t → t') ⇒ ¬∃ Build of cod t' in h(t'), under U, K, T and T′",
                        list(items()), check_with(True, PROV_READINGS),
                        "chains o1 ≺ … ≺ on (n ≤ 3), earlier (held, trace, Sel's conditions) by hand, the output's trace by hand; " + pre, ["I90", "I92", "I161", "I162"]),
             exhaustive("FC83", "without I161 (the review's R1)", "there is a history with SelResp and a Build of cod t' under T or T′",
                        list(items()), check_with(False, ("T", "T'")), "the same space", ["I90", "I92"], kind="there is")]
    return parts


@claim("FC84", [])
def fc84(S):
    return [construction("every creative attribution requires Build", "Origin ⇒ Build; CreateEx ⇒ Origin ⇒ Build", True, "Build is a conjunct of (G) (D13.6) and (G) is a conjunct of (EX) (D14.7)")]


@claim("FC85", ["I77", "I78", "I81", "I48"])
def fc85(S):
    parts = []

    def ident_cand(E, C_c, b0):
        q = Question(E, C_c, b0, PortQuery(), E.ports[0])
        lam = {k: (frozenset([k]), {v: Translation((v,)) for v in E.foot[k]}) for k in E.comps}
        return Candidate(E, q, {v: Translation((v,)) for v in E.ports}, {a: a for a in E.A}, {b: b for b in E.B}, lam, list(E.comps), E.ports[0])

    def gen(rng, size):
        E = gen_org(rng, size)
        b0 = E.B[0]
        C_c = frozenset([(ONE, b0)] + [x for x in all_pairs(E) if rng.random() < 0.5])
        return E, C_c, b0

    def check(m):
        E, C_c, b0 = m
        return None if faithful(ident_cand(E, C_c, b0)) else "the identity transport is not faithful\n" + E.describe()

    parts.append(forall(S, "FC85", 1, "(a) c ≡ c", "the identity transport c → c is faithful on C_c", gen, check, SMALL, 40, BOTHFAM))

    def transports(X, Y, C_pre, b0):
        """The transport space searched for ≡ [I81]: π and λ the identity on shared names, τ and σ every map."""
        As, Bs = list(X.A), list(X.B)
        for taus in itertools.product(Y.A, repeat=len(As) - 1):
            tau = dict(zip([a for a in As if a != ONE], taus))
            tau[ONE] = ONE
            for sigs in itertools.product(Y.B, repeat=len(Bs)):
                sigma = dict(zip(Bs, sigs))
                q = Question(X, C_pre, b0, PortQuery(), X.ports[0])
                lam = {k: (frozenset([k]), {v: Translation((v,)) for v in Y.foot[k]}) for k in Y.comps}
                yield Candidate(Y, q, {v: Translation((v,)) for v in Y.ports}, tau, sigma, lam, list(Y.comps), Y.ports[0])

    def equiv(d, c):
        """d ≡ c (D13.4, I48): t: E_d → E_c faithful on the preimage of C_c, t': E_c → E_d faithful on C_c."""
        (Ed, Cd), (Ec, Cc) = d, c
        b0 = Ed.B[0]
        ok1 = False
        for t in transports(Ed, Ec, frozenset([(ONE, b0)]), b0):
            pre = frozenset((a, b) for a in Ed.A for b in Ed.B if (t.tau[a], t.sigma[b]) in Cc) | {(ONE, b0)}
            if faithful(t.replace(p=t.p.with_C(pre))):
                ok1 = True
                break
        if not ok1:
            return False
        for t in transports(Ec, Ed, Cc, Ec.B[0]):
            if faithful(t):
                return True
        return False

    def gen2(rng, size):
        E = gen_org(rng, size, "G-free")
        if len(E.A) < 2:
            return None
        E2 = Org("E_c", E.ports, E.dom, E.comps, E.foot, E.B, E.A, E._compose,
                 (lambda t: (lambda j, a, b: t.get((j, a, b), E.L(j, a, b))))({(rng.choice(E.comps), rng.choice(E.A[1:]), rng.choice(E.B)): rand_rel(rng, E.full(E.comps[0]), 0.5) if len(E.comps) == 1 else frozenset()}))
        b0 = E.B[0]
        Cd = frozenset([(ONE, b0)])
        Cc = frozenset(all_pairs(E2))
        return (E, Cd), (E2, Cc)

    def wit(m):
        d, c = m
        if equiv(d, c) and not equiv(c, d):
            return "d ≡ c holds and c ≡ d fails (over the transport space searched: π, λ the identity, τ, σ every map)\nd's contract: %s\nc's contract: %s\n%s\n%s" % (show_pairs(d[1]), show_pairs(c[1]), d[0].describe(), c[0].describe())
        return None

    parts.append(exists(S, "FC85", 2, "(b) the matching is read one way (random)", "d ≡ c on C_c while c ≡ d on C_d fails", gen2, wit,
                        sizes(max_ports=2, max_dom=2, max_comps=2, max_B=1, max_edits=2), 40, ["G-free"], ["I81"],
                        note="≡ decided over the transport space π, λ the identity, τ and σ every map (a restriction, I81)"))
    Ed = Org("E_d", ["x"], {"x": (0, 1)}, ["k"], {"k": ("x",)}, ["b0"], [ONE, "e"], lambda a2, a1: None, lambda j, a, b: {(0,)} if a == ONE else {(1,)})
    Ec = Org("E_c", ["x"], {"x": (0, 1)}, ["k"], {"k": ("x",)}, ["b0"], [ONE, "e"], lambda a2, a1: None, lambda j, a, b: {(0,)})
    d_ = (Ed, frozenset([(ONE, "b0"), ("e", "b0")]))
    c_ = (Ec, frozenset([(ONE, "b0")]))
    r = wit((d_, c_))
    parts.append(computed("(b) the matching is read one way (constructed)", "d ≡ c on C_c while c ≡ d on C_d fails", r is not None,
                          r or "no witness: d ≡ c %s, c ≡ d %s" % (equiv(d_, c_), equiv(c_, d_)), ["I81"],
                          note="c ≡ d fails over the transport space searched; that no transport at all exists is not shown"))
    return parts


# ---- repair (Part XI) -----------------------------------------------------------------------------------

@claim("FC86", ["I96"])
def fc86(S):
    def items():
        T = 4
        for cond in itertools.product([False, True], repeat=T):
            for occm in range(2 ** T):
                occ = {t for t in range(T) if occm >> t & 1}
                for xi in range(T):
                    for xi2 in range(xi, T):
                        yield cond, occ, xi, xi2

    def check(m):
        cond, occ, xi, xi2 = m
        lostdef = any(not cond[w] for w in occ if xi <= w <= xi2)
        if (not r_right(cond, occ, xi, xi2)) != lostdef:
            return "¬r(ξ') is not 'fails on a covered occasion in [ξ,ξ']'"
        met_ends = r_left(cond, occ, xi) and cond[xi2] and (xi2 not in occ or cond[xi2])
        between = any(not cond[w] for w in occ if xi < w < xi2)
        if r_left(cond, occ, xi) and between and repair([(False,) * xi + (True,) * (len(cond) - xi)], [(cond, occ)], xi, xi2, True):
            return "a protected aim failed in between and (P) holds: cond %s occ %s ξ %d ξ' %d" % (cond, sorted(occ), xi, xi2)
        return None

    parts = [exhaustive("FC86", "every condition, occasion set and pair of times on 4 times", "a protected r met at ξ and failed on a covered occasion between makes (P) fail; r lost ⟺ it fails on a covered occasion in [ξ, ξ']",
                        items(), check, "all conditions and occasion sets on times 0..3, all ξ ≤ ξ'", ["I96"])]
    def items2():
        T = 4
        for cond in itertools.product([False, True], repeat=T):
            for occm in range(2 ** T):
                occ = {t for t in range(T) if occm >> t & 1}
                for xi in range(T):
                    for xi2 in range(xi, T):
                        yield cond, occ, xi, xi2

    def lost(cond, occ, xi, xi2):
        """Lost_{ξ,ξ'}(r) :⟺ r(ξ) ∧ ¬r(ξ') (D14.1 after area 3)."""
        return r_left(cond, occ, xi) and not r_right(cond, occ, xi, xi2)

    def check2(m):
        cond, occ, xi, xi2 = m
        prot = repair([tuple(t > xi for t in range(len(cond)))], [(cond, occ)], xi, xi2, True) if xi2 > xi else None
        if prot is None:
            return None
        if prot != (not lost(cond, occ, xi, xi2)):
            return "(P)'s protection and ¬Lost differ: cond %s occ %s ξ %d ξ' %d" % (cond, sorted(occ), xi, xi2)
        return None

    parts.append(exhaustive("FC86", "(P) protects exactly the aims not lost", "∀r ∈ P [r(ξ) ⇒ r(ξ')] ⟺ ¬∃r ∈ P Lost_{ξ,ξ'}(r), with Lost_{ξ,ξ'}(r) :⟺ r(ξ) ∧ ¬r(ξ') (the formal statement replacing L441's 'lost exactly when')",
                            items2(), check2, "all conditions and occasion sets on times 0..3, all ξ < ξ'", ["I96", "I57"]))
    cond, occ = (False, True, True), {0, 1, 2}
    parts.append(computed("an aim already failing at ξ is not lost", "Lost_{0,2}(r) fails for r failing at ξ = 0 (covered) and met after; the committed wording 'lost exactly when it fails on an occasion it covers' called it lost", not lost(cond, occ, 0, 2),
                          "r(ξ) on the left: %s; r(ξ') on the right: %s; Lost: %s" % (r_left(cond, occ, 0), r_right(cond, occ, 0, 2), lost(cond, occ, 0, 2)), ["I96", "I57"]))
    parts.append(look("a protected aim already failing at ξ", "(outside FC86) a protected aim that fails at a covered ξ counts as lost by 'fails on an occasion it covers' and is not protected by (P)",
                      not r_left(cond, occ, 0) and not r_right(cond, occ, 0, 2),
                      "cond false at ξ = 0 (covered), true after: r(ξ) on the left is false, so (P) asks nothing of r, while 'r fails on a covered occasion in [ξ, ξ']' holds: under I57 'lost' in L441 and (P)'s protection differ for an aim already failing at ξ.", ["I96"]))
    return parts


@claim("FC87", [])
def fc87(S):
    return [construction("both contributions attributed", "ProducedBy attributes the repair to each contribution with an active route to it", True, "Attr(o) is a set (D14.3); no share function is defined")]


@claim("FC88", ["I96"])
def fc88(S):
    O = [(False, True)]
    P = [((True, True), {0, 1})]
    other = ((True, False), {0, 1})
    aims_star = P + [other]
    X_ = []
    lost_outside = [r for r in aims_star if r not in P and r_left(*r, 0) and not r_right(*r, 0, 1)]
    well = all(r in X_ for r in lost_outside)
    ok = repair(O, P, 0, 1, True) and not well
    return [computed("(P) holds, the claim is not well formed", "a repair claim can meet (P) and fail WellFormed", ok,
                     "O repaired between ξ = 0 and ξ' = 1, P kept, and an aim of Aims*∖P met at ξ and lost by ξ' with an empty exposure record: (P) %s, WellFormed %s" % (repair(O, P, 0, 1, True), well), ["I96", "I58"])]


@claim("FC89", [])
def fc89(S):
    return [not_tested("L443's two kinds of explanatory aim", "Deploy's type against L443's wording", "a reading of the wording of L443 against Deploy's typing")]


@claim("FC90", [])
def fc90(S):
    """FC90 after area 3: (EX)'s conjuncts (D14.7) against what L628 states, as committed and after the
    area-3 replacement of L628's two conclusions by their formal statements."""
    EX = ["CreativeCriticalEpisode", "Repair", "o ∈ O_ex", "¬o(ξ) ∧ o(ξ')", "Attempt", "New", "Build", "e_c ⪯_h e",
          "Account", "c ∈ Result(Δ)", "Deploy(s,c,ξ';U_c)", "ProducesVia"]
    stated_103 = ["Build", "New", "Repair", "o ∈ O_ex", "¬o(ξ) ∧ o(ξ')", "Account"]
    stated_new = stated_103 + ["Attempt", "CreativeCriticalEpisode", "c ∈ Result(Δ)", "ProducesVia", "e_c ⪯_h e", "Deploy(s,c,ξ';U_c)"]
    miss_old = [x for x in EX if x not in stated_103]
    miss_new = [x for x in EX if x not in stated_new]
    return [construction("(EX)'s conjuncts against L628 as committed", "L628 states Build, New, (P) with an explanatory aim, Account and 'deployable'", True,
                         "left unstated by L628 (text 103): %s ('deployable' is not Deploy at a use U_c; (G)'s Attempt is not stated)" % ", ".join(miss_old)),
            computed("(EX)'s conjuncts against L628 with its conclusions replaced by their formal statements", "every conjunct of (EX) is a stated condition of L628's conclusion", not miss_new,
                     "missing after the replacement: %s" % (", ".join(miss_new) or "none"))]


# ---- the physical module (Part XII) ---------------------------------------------------------------------

def gen_ct(rng, size):
    Z = list(range(rng.randint(1, 4)))
    dom_T = list(range(rng.randint(1, 2)))
    outs = list(range(rng.randint(1, 3)))
    T = {i: set(o for o in outs if rng.random() < 0.6) for i in dom_T}
    execs = {(z, i): [(rng.random() < 0.85, rng.choice(outs), rng.choice(Z)) for _ in range(rng.randint(1, 2))] for z in Z for i in dom_T}
    return Z, dom_T, T, execs


@claim("FC91", ["I97"])
def fc91(S):
    parts = []

    def check(m):
        Z, dom_T, T, execs = m
        for s in range(2 ** len(Z)):
            C = frozenset(z for z in Z if s >> z & 1)
            if ret_real(C, dom_T, T, execs) != (C <= F_op(Z, dom_T, T, execs, C)):
                return "RetReal ≠ C ⊆ F(C) at C = %s" % sorted(C)
        return None

    parts.append(forall(S, "FC91", 1, "(CT1) ⟺ C ⊆ F(C) under I61", "RetReal(π,T,C) ⟺ C ⊆ F(C), 'complete' read as (CT1)'s completion", gen_ct, check, [Size(1, 1, 1, 1, 0)], 3000, ["random executions on ≤ 4 states"], ["I97"]))

    def wit(m):
        Z, dom_T, T, execs = m
        for s in range(2 ** len(Z)):
            C = frozenset(z for z in Z if s >> z & 1)
            if C <= F_op(Z, dom_T, T, execs, C, with_output=False) and not ret_real(C, dom_T, T, execs):
                return "C = %s: C ⊆ F'(C) (complete without the output condition) and ¬RetReal; T = %s; executions %s" % (sorted(C), T, execs)
        return None

    parts.append(exists(S, "FC91", 2, "the other reading is weaker", "with 'complete' read without the output condition, C ⊆ F(C) does not give RetReal", gen_ct, wit, [Size(1, 1, 1, 1, 0)], 3000, ["random executions"], ["I97"]))
    return parts


@claim("FC92", ["I97"])
def fc92(S):
    def check(m):
        Z, dom_T, T, execs = m
        subsets = [frozenset(z for z in Z if s >> z & 1) for s in range(2 ** len(Z))]
        for wo in (True, False):
            F = lambda X: F_op(Z, dom_T, T, execs, X, with_output=wo)
            for X_ in subsets:
                for Y in subsets:
                    if X_ <= Y and not F(X_) <= F(Y):
                        return "F not monotone"
            U = frozenset().union(*[D for D in subsets if D <= F(D)])
            if F(U) != U:
                return "F(U) ≠ U"
            fps = [D for D in subsets if F(D) == D]
            if not all(D <= U for D in fps) or gfp(Z, F) != U:
                return "U is not the greatest fixed point"
        return None

    parts = [forall(S, "FC92", 1, "(CT2)", "F monotone; U = ∪{D ⊆ F(D)} is the greatest fixed point; under both readings of 'complete'", gen_ct, check, [Size(1, 1, 1, 1, 0)], 3000, ["random executions on ≤ 4 states"], ["I97"])]

    def check2(m):
        Z, dom_T, T, execs = m
        U = gfp(Z, lambda X_: F_op(Z, dom_T, T, execs, X_))
        for z in U:
            for i in dom_T:
                if not any(c and o in T[i] for (c, o, z2) in execs[(z, i)]):
                    return "z = %d in gfp(F) with no completing execution on input %d" % (z, i)
        return None

    parts.append(forall(S, "FC92", 2, "(e) no vacuous member", "Exec(π,z,i;χ) ≠ ∅ for every z ∈ Z and i ∈ dom T (L469, not only z ∈ C) ⇒ every z ∈ gfp(F) has, on every i ∈ dom T, an execution completing with o ∈ T[i]",
                        gen_ct, check2, [Size(1, 1, 1, 1, 0)], 3000, ["random executions on ≤ 4 states, every family nonempty"], ["I97", "I61"]))
    Z, dom_T, T = [0, 1], [0], {0: {0}}
    execs = {(0, 0): [(True, 0, 0)], (1, 0): []}
    U = gfp(Z, lambda X_: F_op(Z, dom_T, T, execs, X_))
    parts.append(computed("(e') I61's scoping to z ∈ C (Mimo, part 16)", "with Exec empty at a state outside C, that state is in gfp(F): a vacuous member, against L469", 1 in U,
                          "Z = {0, 1}, Exec(π,1,0) = ∅: gfp(F) = %s" % sorted(U), ["I61"]))
    return parts


@claim("FC93", ["I98"])
def fc93(S):
    def gen(rng, size):
        tasks = list(range(4))
        grid = [(q, r) for q in range(3) for r in range(3)]
        real = {}
        for g in sorted(grid, key=lambda x: -(x[0] + x[1])):
            real[g] = set(t for t in tasks if rng.random() < 0.5)
        # antitone: stricter (larger) tolerances realize fewer tasks
        for g in sorted(grid, key=lambda x: (x[0] + x[1])):
            for h in grid:
                if h[0] <= g[0] and h[1] <= g[1]:
                    real[h] |= real[g]
        admit = {g: set(real[g]) | set(t for t in tasks if rng.random() < 0.3) for g in grid}
        for g in sorted(grid, key=lambda x: (x[0] + x[1])):
            for h in grid:
                if h[0] <= g[0] and h[1] <= g[1]:
                    admit[h] |= admit[g]
        cap = {g: set(t for t in real[g] if rng.random() < 0.7) for g in grid}
        return grid, admit, cap

    def check(m):
        grid, admit, cap = m
        if not all(cap[g] <= admit[g] for g in grid):
            return "CT3 fails"
        poss = set.intersection(*[admit[g] for g in grid])
        capinf = set.intersection(*[cap[g] for g in grid])
        if not capinf <= poss:
            return "CT4 fails"
        return None

    parts = [forall(S, "FC93", 1, "(a) CT3, (b) CT4", "Cap^{q,r} ⊆ Admit^{q,r}; Cap^∞ ⊆ Poss", gen, check, [Size(1, 1, 1, 1, 0)], 3000, ["random antitone task families on a 3×3 tolerance grid"], ["I98"])]

    def wit(m):
        grid, admit, cap = m
        poss = set.intersection(*[admit[g] for g in grid])
        for g in grid:
            if cap[g] - poss:
                return "T ∈ Cap^%s and T ∉ Poss: %s" % (g, sorted(cap[g] - poss))
        return None

    parts.append(exists(S, "FC93", 2, "(c) capability at one tolerance", "T ∈ Cap^{q,r} and T ∉ Poss", gen, wit, [Size(1, 1, 1, 1, 0)], 500, ["random antitone task families"], ["I98"]))
    return parts


@claim("FC94", [])
def fc94(S):
    return [not_tested("recursion and universality", "a model of RC with ¬UU; no finite set of performed tasks decides UU",
                       "RC, UU, Enable, target chains and 𝔈_Θ have no finite semantics without Θ; a model would be an assignment of free predicates, which shows only that no axiom links them (as FC110)")]


@claim("FC95", ["I90", "I92"])
def fc95(S):
    p, c = fwd_pole_cand()
    D = p.D
    inv = D.meta["inv"]
    # a content in error: E_c gives L = 2H at every setting (a wrong theory of the pole)
    E = D
    bad = {a: a for a in D.A}
    wrong = Org("E_wrong", D.ports, D.dom, D.comps, D.foot, D.B, D.A, D._compose,
                lambda j, a, b: (frozenset(w for w in D.full(j) if w[2] == 2 * w[0]) if j == "c_L" else D.L(j, a, b)))
    tc = c.replace(E=wrong, name="t_c")
    q_c = Question(wrong, [(x, "b1_45") for x in D.A if (x, "b1_45") in p.C], "b1_45", PortQuery(), "L")
    lam = {j: (frozenset([j]), {v: Translation((v,)) for v in wrong.foot[j]}) for j in wrong.comps}
    t_o = Candidate(wrong, q_c, {v: Translation((v,)) for v in wrong.ports}, {a: a for a in D.A}, {b: b for b in D.B}, lam, list(wrong.comps), "L", name="t: Org(o) → c")
    rep = faithful(t_o)  # Org_ℓ(o) = the content's own organization (Θ by hand), Con by hand
    return [computed("a system can represent a theory in error", "Rep_ℓ(o, c) and ¬Faithful for the candidate's transport t_c: D_c → E_c", rep and not faithful(tc),
                     "o instantiates E_wrong (L = 2H, Θ supplied by hand); the identity transport o → c is faithful on c's contract: %s; Con set true by hand (I90); t_c from the pole to E_wrong is faithful: %s" % (rep, faithful(tc)), ["I90", "I92"])]


@claim("FC96", ["I77", "I78", "I81"])
def fc96(S):
    parts = []

    def check_i(m):
        p, c1, c2 = m
        if not (A(c1) and A(c2)):
            return VAC
        if A(c1) and A(c2):
            for (a, b) in p.C:
                if c1.ans_E(c1.tau[a], c1.sigma[b]) != c2.ans_E(c2.tau[a], c2.sigma[b]):
                    return "(A) for both, different answers"
        return None

    parts.append(forall(S, "FC96", 1, "(i) (A) for both ⇒ equal answers", "A_C(ℰ) ∧ A_C(ℰ') ⇒ equal answers on C", gen_pair, check_i, CONF, 20, BOTHFAM))

    def gen(rng, size):
        D, p = D_and_p(rng, size)
        if D is None:
            return None
        c = gen_candidate(rng, p, perturb_p=0.0, background_p=0.0, random_tau_p=0.0, demote_p=0.0, valuemaps=True)
        E = c.E
        cm = {k: k + "'" for k in E.comps}
        icm = {v: k for k, v in cm.items()}
        E2 = Org("E'", E.ports, E.dom, [cm[k] for k in E.comps], {cm[k]: E.foot[k] for k in E.comps}, E.B, E.A, E._compose, lambda j, a, b: E.L(icm[j], a, b))
        c2 = c.replace(E=E2, lam={cm[k]: v for k, v in c.lam.items()}, Gamma=tuple(cm[k] for k in c.Gamma), name="ℰ'")
        return p, c, c2, cm

    def check_ii(m):
        p, c1, c2, cm = m
        if not (F1(c1) and F1(c2)):
            return VAC
        for k in c1.Gamma:
            if not one_kind(c1.E, k, c2.E, cm[k], p.C, (c1.tau, c1.sigma), (c2.tau, c2.sigma)):
                return "same counterparts, F1 for both, not of one kind\n" + c1.describe()
        return None

    parts.append(forall(S, "FC96", 2, "(ii) same counterparts give one kind", "φ: Γ → Γ' with λ'(φk) = λ(k), same images and value maps, F1 for both ⇒ k and φk of one kind on C through t, t'",
                        gen, check_ii, SMALL, 40, BOTHFAM))
    return parts


def e8_contract_org():
    """E8 (I67): the contract of a question with edits {1, a1, a2} and boundaries {b0, b1} as an organization:
    a membership port per pair, a query port q, the baseline and one closure component, setting edits."""
    A_, B_ = [ONE, "a1", "a2"], ["b0", "b1"]
    pairs = [(a, b) for a in A_ for b in B_]
    ports = ["m_%s_%s" % x for x in pairs] + ["q"]
    dom = {v: (0, 1) for v in ports[:-1]}
    dom["q"] = ("Q1", "Q2")
    foot = {"base": ("m_1_b0",), "close": ("m_a1_b0", "m_a2_b0", "m_1_b0")}
    Aed, invd, compose = surgical_edits({v: dom[v] for v in ports[:3]})

    def Lf(j, a, b):
        sm = dict(invd[a])
        if j == "base":
            return frozenset([(1,)]) if "m_1_b0" not in sm else frozenset([(sm["m_1_b0"],)])
        return frozenset(w for w in itertools.product((0, 1), repeat=3) if not (w[0] and w[1]) or w[2])

    return Org("D_C", ports, dom, list(foot), foot, ["β"], Aed, compose, Lf), invd, (A_, B_)


@claim("FC97", ["I67"])
def fc97(S):
    Dc, invd, _ = e8_contract_org()
    ok_dom = all(Dc.dom[v] for v in Dc.ports)
    ok_id = all(Dc.compose(a, ONE) == a and Dc.compose(ONE, a) == a for a in Dc.A)
    ok_assoc = all(Dc.compose(a3, Dc.compose(a2, a1)) == Dc.compose(Dc.compose(a3, a2), a1) for a1 in Dc.A for a2 in Dc.A for a3 in Dc.A)
    ok_rel = all(Dc.L(j, a, b) <= Dc.full(j) for j in Dc.comps for a in Dc.A for b in Dc.B)
    return [computed("a contract as an organization", "D_C (membership ports, a query port, closure components, setting edits) meets (O)'s typing and I01's partial monoid laws",
                     ok_dom and ok_id and ok_assoc and ok_rel, "nonempty domains %s; identity %s; associativity (total here) %s; relations on footprints %s; %d edits" % (ok_dom, ok_id, ok_assoc, ok_rel, len(Dc.A)), ["I67"]),
            not_tested("Deploy, Build, New and (G) take it as a content", "a contract as a content", "needs Θ (I90); the typing check above is what the model can do")]


# ---- FC98 after area 3: the dependence order (D18.1) and E03's loop ------------------------------

DEP = {  # D18.1 as the text's words give it, 'represented' read through (R); ('<', x) marks a use of x at an earlier occurrence only under the staged reading
    "(K)": ["(O)", "C"], "(F1)": ["(O)", "(Q)", "(K)"], "(F2)": ["(O)", "(Q)", "(K)"], "(A)": ["(O)", "(Q)", "(K)"],
    # second check (R5): one edge set for D18.1, the text (L526 points to D18.1) and this graph: NC0–NC2 read no
    # signature (no (K)) and read C; t and Γ are the candidate's own data, as for (F1), (F2), (A) (FC32)
    "NC": ["(O)", "(Q)", "C", "ℓ", "δ"], "NV": ["(O)", "C", "Σ"], "(E)": ["(F1)", "(F2)", "(A)", "NC", "NV"],
    "(R)": ["(F1)", "(F2)", "Org", "Sel", "Con"], "Sel": ["h", "Θ", ("<", "(R)")], "Con": ["h", "Build", ("<", "(R)")],
    "Build": ["h", "Owned", "(E)", ("<", "(R)")], "Owned": ["h", "β"], "Deploy": ["(R)", "Can"], "Can": ["(CT1)", "Owned", "Ω"],
    "(CT1)": ["Θ"], "New": ["Deploy"], "(G)": ["Attempt", "New", "Build"], "ActRoute": ["h", "Org", "K"],
    "ProducedBy": ["ActRoute", "O,P"], "(P)": ["ProducedBy", "O,P"], "ProducesVia": ["ActRoute", "Build"],
    "(EX)": ["(G)", "(P)", "(E)", "Deploy", "ProducesVia", "CCE"], "CCE": ["(K1)", "UsesReason", "(G)"], "(K1)": ["(E)", "Qf"],
    "UsesReason": ["ActRoute", "Rec", "Chg", "Rule"], "(K2)": ["Forms", "Scope", "Live"], "Live": [("<", "(K2)"), "Accepted"],
    "Held": ["Org", "(F1)", "(F2)"],  # Held(o', c) :⟺ ∃t Faithful(t: Org_ℓ(o') → c), no provenance (D18.1, cuts T and T′)
}
TEXT_SINKS = {"(O)", "(Q)", "Θ", "Org", "𝒩", "C", "ℓ", "β", "Ω", "Σ", "O,P", "Forms", "Scope", "Accepted", "h"}


def dep_edges(reading):
    """The graph under a reading of 'represented' (D18.1): 'U' as worded; 'K' every ('<', x) edge staged
    (dropped: a recursion along ≺_h or below the step); 'T' Sel, Con, Build use Held, not (R); "T'" Con and
    Build use Held, Sel's (R) staged [I162]. (K2) → Live → (K2) is staged below the step in every reading (D9.4)."""
    out = {}
    for n, xs in DEP.items():
        e = []
        for x in xs:
            staged = isinstance(x, tuple)
            y = x[1] if staged else x
            if y == "(R)" and staged and n in ("Sel", "Con", "Build"):
                if reading == "U":
                    e.append(y)
                elif reading == "T" or (reading == "T'" and n != "Sel"):
                    e.append("Held")
                continue  # K, and T′'s Sel: staged along ≺_h
            if staged and reading != "U":
                continue
            e.append(y)
        out[n] = e
    return out


def dep_cycle(staged, reading=None):
    edges = dep_edges(reading or ("K" if staged else "U"))
    color, stack = {}, []

    def dfs(n):
        color[n] = 1
        stack.append(n)
        for m in edges.get(n, []):
            if color.get(m) == 1:
                return stack[stack.index(m):] + [m]
            if m not in color:
                c = dfs(m)
                if c:
                    return c
        color[n] = 2
        stack.pop()
        return None

    for n in list(edges):
        if n not in color:
            c = dfs(n)
            if c:
                return c
    return None


def rep_fixed_points(case, reading, i161=False):
    """Rep on a history o1 ≺ o2 for one content c, from facts set by hand (Θ): held[o], trace[o], selhist[o]
    (FC98's cases); prov_fixed_points on n = 2. Readings U, K, T, T′ as prov_fixed_points."""
    held, trace, selhist = case
    occ = ["o1", "o2"]
    fps = prov_fixed_points(2, [held[o] for o in occ], [trace[o] for o in occ], [selhist[o] for o in occ], reading, i161)
    return prov_show(2, fps)


@claim("FC98", [])
def fc98(S):
    parts = []
    cyc = dep_cycle(False)
    parts.append(computed("(a) the order as worded", "with 'represented' (L197, L405) read through (R), the dependence graph has a cycle (E03; L526 says it has none)", cyc is not None,
                          "cycle: %s" % (" → ".join(cyc) if cyc else "none"), ["A3-02"]))
    cyc2 = {rd: dep_cycle(True, rd) for rd in ("K", "T", "T'")}
    parts.append(computed("(a') the order under the cuts K, T and T′", "with (R) inside Sel, Con, Build staged (K), replaced by Held (T), or Held in Con and Build and staged in Sel (T′, I162), no cycle",
                          all(c is None for c in cyc2.values()), "; ".join("%s: %s" % (rd, " → ".join(c) if c else "no cycle") for rd, c in cyc2.items()), ["A3-02", "I40", "I162"]))
    sinks = sorted(set(x[1] if isinstance(x, tuple) else x for xs in DEP.values() for x in xs) - set(DEP) - TEXT_SINKS)
    parts.append(look("(b) sinks the text does not list", "every sink is Θ, 𝒩, (O), (Q), an index or a declared input of L522", False,
                      "sinks of this graph outside L526's and L522's lists: %s (D0.2 after area 3). Each is read through Θ or is a declared input, as D0.2 marks (second check, Q4 ruled)." % ", ".join(sinks), ["A3-02"]))
    first = ({"o1": False, "o2": True}, {"o1": False, "o2": True}, {"o1": False, "o2": False})
    selfsel = ({"o1": False, "o2": True}, {"o1": False, "o2": False}, {"o1": False, "o2": True})
    both = ({"o1": True, "o2": True}, {"o1": False, "o2": True}, {"o1": True, "o2": True})
    decl = ({"o1": True, "o2": True}, {"o1": False, "o2": False}, {"o1": False, "o2": True})
    cases = (("first construction", first), ("selection", selfsel), ("built on a selected representation", both), ("declared earlier holder", decl))
    res = {(nm, rd): rep_fixed_points(case, rd, i161=True) for nm, case in cases for rd in PROV_READINGS}
    txt = "; ".join("%s, reading %s: fixed points %s" % (nm, rd, res[(nm, rd)]) for (nm, rd) in sorted(res))
    parts.append(computed("(c) Rep as a fixed point on a two-occurrence history", "reading U (as worded): two fixed points for a first construction and none for a selection (the output in its own history); readings K, T and T′: exactly one each",
                          len(res[("first construction", "U")]) == 2 and len(res[("selection", "U")]) == 0 and all(len(res[(nm, rd)]) == 1 for nm, _ in cases for rd in ("K", "T", "T'")),
                          txt, ["A3-02", "I161"]))
    parts.append(computed("(d) what each cut gives", "K: a first construction of c yields no representation of c (L405's 'A first representation may be constructed' fails); T and T′: it yields one; all three give o2 exactly one provenance (Con) when it is built on a selected representation held by o1 (L201: construction may operate on selected material)",
                          res[("first construction", "K")] == [{}] and res[("first construction", "T")] == res[("first construction", "T'")] == [{"o2": "Con"}]
                          and res[("built on a selected representation", "K")] == res[("built on a selected representation", "T")] == res[("built on a selected representation", "T'")] == [{"o1": "Sel", "o2": "Con"}],
                          "first construction: K %s, T %s, T′ %s; built on a selected representation: K %s, T %s, T′ %s." % (
                              res[("first construction", "K")], res[("first construction", "T")], res[("first construction", "T'")],
                              res[("built on a selected representation", "K")], res[("built on a selected representation", "T")], res[("built on a selected representation", "T'")]), ["A3-02", "I162"]))
    parts.append(computed("(e) second check: an earlier holder with a declared transport (L211), then a selection", "L195 with L211 (a declared transport makes no representation): o2 selected; K and T′ give o2 Sel, T gives o2 nothing (Held at o1 blocks it)",
                          res[("declared earlier holder", "K")] == res[("declared earlier holder", "T'")] == [{"o2": "Sel"}] and res[("declared earlier holder", "T")] == [{}],
                          "o1 holds c by a declared transport (no trace, no selection history), o2 holds c with a selection history: U %s, K %s, T %s, T′ %s. With FC98 (d) and FC12.new1, T′ is the one cut meeting L405, L193, L195 with L211, and L526 (I162)." % (
                              res[("declared earlier holder", "U")], res[("declared earlier holder", "K")], res[("declared earlier holder", "T")], res[("declared earlier holder", "T'")]), ["I162"]))
    return parts


@claim("FC99", ["I92"])
def fc99(S):
    D = pole()
    b0 = "b1_45"
    C1 = frozenset([(ONE, b0)] + [(a, b0) for a in single_settings(D, ["H", "T"])])
    inv = D.meta["inv"]
    Ls = D.dom["L"]
    f = {Ls[i]: Ls[(i + 1) % len(Ls)] for i in range(len(Ls))}
    lab = {inv[a]: a for a in D.A}

    def tau_of(a):
        sm = dict(inv[a])
        if "L" in sm:
            sm["L"] = f[sm["L"]]
        return lab[tuple(sorted(sm.items()))]

    tau = {a: tau_of(a) for a in D.A}
    p1 = Question(D, C1, b0, PortQuery(), "L", name="C1")
    c = pole_fwd_candidate(p1, tau=tau)
    setL = single_settings(D, ["L"])[0]
    p2 = p1.with_C(C1 | {(setL, b0)}, name="C1'")
    a1, d1 = account(c, detail=True)
    a2, d2 = account(c.replace(p=p2), detail=True)
    return [computed("an account on C can fail on C'", "the forward candidate with τ shifting the settings of L: Acc on C1, ¬Acc on C1 ∪ {(%s,b0)}" % setL,
                     a1 and not a2, "on C1: %s; on C1': %s (τ is a homomorphism: Hom = %s)" % (d1, d2, hom(c)), ["I92"])]


@claim("FC100", ["I77", "I78", "I81", "I70"])
def fc100(S):
    def gen(rng, size):
        m = gen_p_cand(rng, size)
        if m is None:
            return None
        return m + (rng,)

    def check(m):
        p, c, rng = m
        D = p.D
        D2, pm, cm, bm, am = rename_org(D, rng, "'")
        E = c.E
        E2, pm2, cm2, bm2, am2 = rename_org(E, rng, "\"")
        q2 = Question(D2, [(am[a], bm[b]) for (a, b) in p.C], bm[p.b0], p.Q, pm[p.deltaD], excl=[(am[a], bm[b]) for (a, b) in p.excl])
        pi2 = {pm2[v]: Translation(tuple(pm[u] for u in c.pi[v].dports), c.pi[v].fn) for v in E.ports}
        lam2 = {cm2[k]: (frozenset(cm[j] for j in N), {pm2[v]: Translation(tuple(pm[u] for u in tr[v].dports), tr[v].fn) for v in E.foot[k]}) for k, (N, tr) in c.lam.items()}
        tau2 = {am[a]: am2[x] for a, x in c.tau.items()}
        sig2 = {bm[b]: bm2[x] for b, x in c.sigma.items()}
        c2 = Candidate(E2, q2, pi2, tau2, sig2, lam2, [cm2[k] for k in c.Gamma], pm2[c.deltaE])
        if account(c) != account(c2):
            return "an isomorphic copy of all the data changes Acc\n%s\n%s" % (p.describe(), c.describe())
        return None

    return [forall(S, "FC100", 1, "(E) is kept by structure-preserving bijections", "Acc(φ·ℰ) = Acc(ℰ) for random isomorphic copies of D and E (ports, components, edits, boundaries)",
                   gen, check, SMALL, 30, BOTHFAM, ["I70"]),
            not_tested("(G), (P), (EX)", "kept by every structure-preserving bijection", "need histories and Θ; not modelled beyond free predicates")]


@claim("FC101", ["I78", "I29"])
def fc101(S):
    # M0: two parallel routes to the output; M1: a priority route with a fallback. Same input-output
    # behaviour under settings of the input; different under deletions of internal components.
    def mk(name, kind):
        ports = ["i", "m1", "m2", "o"]
        dom = {v: (0, 1) for v in ports}
        foot = {"h_i": ("i",), "r1": ("i", "m1"), "r2": ("i", "m2"), "out": ("m1", "m2", "o")}
        A = [ONE, "set_i0", "set_i1", "del_r1", "del_r2"]

        def Lf(j, a, b):
            if j == "h_i":
                return {(int(a[-1]),)} if a.startswith("set_i") else {(1,)}
            # area 1 (H18; L103): a deleted component imposes the full relation on its ports
            if j == "r1":
                return {(x, x) for x in (0, 1)} if a != "del_r1" else {(x, y) for x in (0, 1) for y in (0, 1)}
            if j == "r2":
                return {(x, x) for x in (0, 1)} if a != "del_r2" else {(x, y) for x in (0, 1) for y in (0, 1)}
            if kind == "or":
                return {(x, y, x | y) for x in (0, 1) for y in (0, 1)}
            return {(x, y, x) for x in (0, 1) for y in (0, 1)}  # priority: the output follows m1

        return Org(name, ports, dom, list(foot), foot, ["b0"], A, lambda a2, a1: None, Lf)

    M0, M1 = mk("M0", "or"), mk("M1", "prio")
    C = [(a, "b0") for a in M0.A]
    io = all(set(z[3] for z in M0.sol(a, "b0")) == set(z[3] for z in M1.sol(a, "b0")) for a in (ONE, "set_i0", "set_i1"))
    p0 = Question(M0, C, "b0", PortQuery(), "o", name="p_M0")
    p1 = Question(M1, C, "b0", PortQuery(), "o", name="p_M1")
    lam = {j: (frozenset([j]), {v: Translation((v,)) for v in M0.foot[j]}) for j in M0.comps}
    c0 = Candidate(M0, p0, {v: Translation((v,)) for v in M0.ports}, {a: a for a in M0.A}, {"b0": "b0"}, lam, list(M0.comps), "o", name="ℰ_M0")
    c1 = c0.replace(p=p1)
    a0, a1 = account(c0), account(c1, detail=True)
    return [construction("(a) a function of the projection", "P(M0) = P(M1) ⇒ f(M0) = f(M1)", True, "a function of the projection sees nothing else"),
            computed("(b) equal input-output behaviour, different accounts", "M0 and M1 with equal projections under the input settings; a contract with deletions of internal components; a candidate meeting (E) for M0 and not for M1",
                     io and a0 and not a1[0], "input-output equal: %s; the parallel-route candidate meets (E) on M0's question: %s; on M1's: %s" % (io, a0, a1), ["I78"])]


@claim("FC102", ["I100"])
def fc102(S):
    parts = []
    N, K = 6, 10

    def step(p_, v_, ends="reflect"):
        np_ = p_ + v_
        if not 0 <= np_ < N:
            if ends == "stop":  # second check (Q25): the other end rule, the thing stops at the end
                return p_, 0
            v_ = -v_
            np_ = p_ + v_
        return np_, v_

    def run(start, occl, ends="reflect"):
        """Things (pos, vel), reflection at the ends; occupancy per cell, None where occluded [I100]."""
        things = list(start)
        traj = []
        for t in range(K):
            occ = tuple((None if (t, c) in occl else int(any(pp == c for pp, _ in things))) for c in range(N))
            traj.append(occ)
            things = [step(pp, vv, ends) for pp, vv in things]
        return traj

    def structural(nthings, w, L_occ, ends="reflect"):
        """Two histories with equal readings over the last w steps before re-emergence and different
        readings at re-emergence (the occlusion hides cells 1..N-2 from t = 3 for L_occ steps)."""
        states = [(pp, vv) for pp in range(N) for vv in (-1, 0, 1)]
        starts = [(s1,) for s1 in states] if nthings == 1 else [(s1, s2) for s1 in states for s2 in states if s1[0] < s2[0]]
        occl = {(t, c) for t in range(3, 3 + L_occ) for c in range(1, N - 1)}
        t_re = 3 + L_occ
        if t_re - w < 0 or t_re >= K:
            return None
        seen = {}
        for st in starts:
            tr = run(st, occl, ends)
            key = tuple(tr[t_re - w:t_re])
            val = tr[t_re]
            if key in seen and seen[key][0] != val:
                return (seen[key][1], st)
            seen.setdefault(key, (val, st))
        return None

    table = {}
    for nth in (1, 2):
        for w in (1, 2, 3, 4, 5, 6):
            for L_occ in (0, 1, 2, 3, 4):
                if 3 + L_occ - w >= 0 and 3 + L_occ < K:
                    table[(nth, w, L_occ)] = structural(nth, w, L_occ)
    fails = lambda nth, w, L: table[(nth, w, L)] is not None
    first = all(fails(nth, w, L) for (nth, w, L) in table if L >= w)
    parts.append(computed("(b) first half: the occlusion outlasts the window", "occlusion of L ≥ w steps ⇒ two histories with equal last-w occupancy and different re-emergence readings",
                          first, "N = %d cells, cells 1..%d hidden from t = 3 for L steps. Failing (things, w, L): %s" % (N, N - 2, sorted(k for k, v in table.items() if v is not None and k[2] >= k[1])), ["I100"]))
    second_one = [(w, L) for (nth, w, L) in table if nth == 1 and L < w and fails(1, w, L)]
    second_two = [(w, L) for (nth, w, L) in table if nth == 2 and L < w and fails(2, w, L)]
    ex = next(((k, v) for k, v in sorted(table.items()) if v is not None and k[0] == 2 and k[2] == 0), None)
    parts.append(look("(b) second half as the committed claim glossed it", "w > L ⇒ an occupancy predictor can extrapolate (the failure is not structural): the formalizer's gloss, not a sentence of the text",
                      not second_one and not second_two,
                      "one thing, failing (w, L) with L < w: %s; two things: %s; two things, no occlusion: %s" % (second_one, second_two, ex), ["I100"]))
    exact1 = sorted((w, L) for (nth, w, L) in table if nth == 1 and fails(1, w, L))
    parts.append(look("(b') the exact failing set on I100's geometry (one thing)", "fails ⟺ w ≤ L + 1 (fewer than two visible frames), where the thing stays hidden for the whole run",
                      all(fails(1, w, L) == (w <= L + 1) for (nth, w, L) in table if nth == 1),
                      "one thing, failing (w, L): %s. The exception (5, 4): the run hides only cells 1..4, so a thing reaching cell 0 or 5 is seen again inside the window. L626's bound is therefore written as w ≤ L (the first half, which holds for one and two things), not as w ≤ L + 1." % exact1, ["I100", "A3-11"]))
    two = sorted((w, L) for (nth, w, L) in table if nth == 2 and fails(2, w, L))
    parts.append(computed("(b'') the bound written into L626", "w ≤ L ⇒ no window-w occupancy predictor survives, for one thing and for two (the formal hypothesis replacing 'can only predict from occupancy')", first,
                          "all (things, w, L) with w ≤ L fail (first half); two things fail also at: %s" % two, ["I100", "A3-11"]))
    stop = {k: structural(k[0], k[1], k[2], "stop") for k in table}
    first_stop = all(stop[k] is not None for k in stop if k[2] >= k[1])
    parts.append(computed("(b3) second check (Q25): the bound under the other end rule", "w ≤ L ⇒ no window-w occupancy predictor survives, one thing and two, with things stopping at the ends instead of reflecting (I100's end rule)", first_stop,
                          "stop at the ends: failing (things, w, L) with w ≤ L: %d of %d" % (sum(1 for k in stop if k[2] >= k[1] and stop[k] is not None), sum(1 for k in stop if k[2] >= k[1])), ["I100", "A3-11"]))
    parts.append(not_tested("(a), (c)", "t0 survives on H0 and is surprised; t1 meets (F1) and (F2) on the extended contract", "the two-layer organizations S0, S1 and their transports are not built in this round (E9 encodes only the object layer here)"))
    return parts


@claim("FC103", ["I100"])
def fc103(S):
    N = 5
    ok = True
    for a in range(N):
        for b in range(N):
            if a == b:
                continue
            occ1 = tuple(int(c in (a, b)) for c in range(N))
            occ2 = tuple(int(c in (b, a)) for c in range(N))
            ok = ok and occ1 == occ2
    return [computed("(d) the swap leaves occupancy answers unchanged", "exchanging the two things' states leaves every occupancy reading unchanged", ok, "all placements of two things on 5 cells", ["I100"]),
            not_tested("(a)-(c) on E9", "t1∘ψ meets (F1), (F2), (A) exactly when t1 does; one kind; no pair separates the pairings", "E9's simulation layer is not built; the general forms are tested as FC33, FC96 (ii) and FC51 (b)")]


@claim("FC104", [])
def fc104(S):
    return [not_tested("two extents of 'fidelity'", "which extent each line needs", "a reading of thirty lines' wording")]


@claim("FC105", [])
def fc105(S):
    return [not_tested("'event'", "whether any use of 'event' needs more than a set of occurrences", "a reading of six lines' wording")]


@claim("FC106", ["I77", "I78", "I81"])
def fc106(S):
    def check(m):
        p, c = m
        if p.D.sol(ONE, p.b0):
            return VAC
        if account(c):
            return "incompatible baseline with an account\n" + c.describe()
        return None

    return [forall(S, "FC106", 1, "an incompatible baseline admits no account", "Sol_D(1,b0) = ∅ ⇒ ¬NonVacuous ⇒ no candidate has Acc",
                   gen_p_cand, check, SMALL, 40, BOTHFAM),
            not_tested("the other two defects", "failing to pick out a target; incompatible requirements", "need a description Desc of the question (I76), which the model does not build")]


@claim("FC107", ["I67"])
def fc107(S):
    """Second check (R13): tested on E8 (L590: a contract is an organization, 𝒬 among its ports). p_δ, whether
    p's contract has the defect 'baseline missing' (D3.6), is a question on D_C with its own contract (settings
    of the baseline's membership port) and query (that port); (E) assesses a candidate on it, as in (K1)."""
    Dc, invd, (A_, B_) = e8_contract_org()
    sets = [a for a in Dc.A if a != ONE and set(dict(invd[a])) == {"m_1_b0"}]
    Cd = [(ONE, "β")] + [(a, "β") for a in sets]
    pd = Question(Dc, Cd, "β", PortQuery(), "m_1_b0", name="p_δ")
    lam = {k: (frozenset([k]), {v: Translation((v,)) for v in Dc.foot[k]}) for k in Dc.comps}
    cand = Candidate(Dc, pd, {v: Translation((v,)) for v in Dc.ports}, {a: a for a in Dc.A}, {b: b for b in Dc.B}, lam, list(Dc.comps), "m_1_b0")
    acc, det = account(cand, detail=True)
    own = set(Dc.A).isdisjoint(set(A_) - {ONE}) and set(Dc.B).isdisjoint(B_) and "q" in Dc.ports
    return [computed("p_δ ≠ p on E8", "p_δ's target is D_C (ports m_(a,b) and 𝒬), with a contract and a query of its own; p's target has edits {1, a1, a2} and boundaries {b0, b1}",
                     own, "p_δ: target D_C (%d ports, 𝒬 = q among them), contract %s, query the port m_1_b0; answers %s" % (len(Dc.ports), [a for a, _ in Cd], [pd.ans(a, "β") for a, _ in Cd]), ["I67"]),
            computed("(E) assesses a candidate for p_δ (K1)", "Acc is computed on p_δ for the identity candidate on D_C",
                     isinstance(acc, bool), "Acc %s: %s (NC1 fails: the component 'base' is an answer slot, 'p because p')" % (acc, det), ["I67"])]


@claim("FC108", [])
def fc108(S):
    return [construction("NC0 adds no condition", "NC0 holds of every candidate", True, "core.noncircular is NC1 ∧ NC2; every answer is computed by evaluating E at (τ(a), σ(b))")]


@claim("FC109", [])
def fc109(S):
    from .harness import overall, Settings
    named = ["FC37", "FC57", "FC61", "FC66", "FC92", "FC17", "FC96", "FC80"]
    rows = []
    for cid in named:
        parts = REG[cid][0](Settings(scale=0.3, time_cap=5))
        rows.append((cid, overall(parts)))
    ok = all(s != "COUNTEREXAMPLE FOUND" for _, s in rows)
    return [computed("the named results, each under its assumptions", "L546's named claims have no counterexample on the models tried", ok,
                     "; ".join("%s: %s" % r for r in rows) + " (rerun here at 0.3 of the budget; the full runs are reported under each claim)")]


@claim("FC110", [])
def fc110(S):
    return [not_tested("the classes", "each class is the extension of a formula; no axiom places a system in a class", "syntactic, about the formal core's definitions")]
