# S105 round 3, area 3 (L373-L632): the checker's claims. Each computes from the program's own functions (lesson
# S39): Rep, Sel, Con by fixed points; Acc by core.account; usability and ruling out by args; nothing is tagged by
# hand except what the formal core reads through Θ (I90), and each such input is named.
# Ids FC<n>.new<m> (m chosen not to collide with areas 1 and 2). Stated in the area 3 verdicts file.
import itertools
import os
import re

from .core import ONE, BOT, Org, Question, PortQuery, FnQuery, Candidate, Translation, account, F1, F2, A, F1_at, F2eq_at, A_at, hom, faithful, one_kind
from .args import Not, And, Imp, canon, Leaf, Step, Assessor, usable, rules_out, X, enumerate_args, incons
from .harness import claim, forall, exists, exhaustive, computed, construction, look, not_tested, VAC
from .cases import pole, pole_fwd_candidate, pole_rev_candidate, single_settings
from . import claims_b
from .claims_b import Hist, sel, faithful_on, fwd_pole_cand

HERE = os.path.dirname(os.path.abspath(__file__))

# ---- S1: the cut loop on an infinite descending history (D11.3, D18.1, I162) ------------------------------
# A history as a strict partial order on occurrences; per occurrence: held (Θ: a faithful transport to c, no
# provenance), selc (Sel's conditions other than its exclusions), trace (a construction trace prepares o's
# transport). Readings of 'represented' as claims_b (U, K, T, T'); episodes: one contract throughout.


def poset_step(occ, below, held, selc, trace, rd, R, i161=True):
    """One application of the provenance operator on a finite poset: below[o] the occurrences o' ≺ o."""
    out = {}
    for o in occ:
        upto = below[o] | {o}
        if rd == "U":
            s_ = selc[o] and not (R & upto)
            c_ = trace[o] and bool(R & upto)
        elif rd == "K":
            s_ = selc[o] and not (R & below[o])
            c_ = trace[o] and bool(R & below[o])
        elif rd == "T":
            s_ = selc[o] and not any(held[x] for x in below[o])
            c_ = trace[o] and any(held[x] for x in upto)
        else:  # T'
            s_ = selc[o] and not (R & below[o])
            c_ = trace[o] and any(held[x] for x in upto)
        if i161:
            s_ = s_ and not trace[o]
        out[o] = (bool(s_), bool(c_))
    return out


def poset_fixed_points(occ, below, held, selc, trace, rd):
    fps = []
    for bits in itertools.product([0, 1], repeat=len(occ)):
        R = frozenset(o for o, b in zip(occ, bits) if b)
        sc = poset_step(occ, below, held, selc, trace, rd, R)
        if frozenset(o for o in occ if held[o] and (sc[o][0] or sc[o][1])) == R:
            fps.append(R)
    return fps


def strict_orders(n):
    """Every strict partial order on {0..n-1} (irreflexive, transitive), as below[o] sets."""
    pairs = [(a, b) for a in range(n) for b in range(n) if a != b]
    seen = set()
    for bits in itertools.product([0, 1], repeat=len(pairs)):
        rel = {pairs[i] for i in range(len(pairs)) if bits[i]}
        if any((b, a) in rel for (a, b) in rel):
            continue
        if any((a, c) not in rel for (a, b) in rel for (b2, c) in rel if b == b2 and a != c):
            continue
        key = frozenset(rel)
        if key in seen:
            continue
        seen.add(key)
        yield {o: frozenset(a for (a, b) in rel if b == o) for o in range(n)}


def infinite_chain_check(R, n_window):
    """o_0 ≻ o_1 ≻ o_2 ≻ … (o_(k+1) ≺ o_k), every o_k held, Sel's other conditions met, no trace (S1's witness).
    T': Rep(o_k) ⟺ ¬∃m > k Rep(o_m). For a finite R ⊆ {0..n}: the first k at which the equation fails."""
    for k in range(n_window + 2):
        need = not any(m > k for m in R)
        if need != (k in R):
            return k
    return None


@claim("FC98.new2", ["I162"])
def fc98_new2(S):
    parts = []
    # (a) S1's two witnesses, and every finite R, on the infinite descending chain
    s1 = {"{o_1}": {1}, "{o_2}": {2}}
    fails = {nm: infinite_chain_check(R, 8) for nm, R in s1.items()}
    n = 12
    bad = [R for bits in itertools.product([0, 1], repeat=n + 1) for R in [{k for k in range(n + 1) if bits[k]}] if infinite_chain_check(R, n) is None]
    parts.append(computed("(a) S1's witness, run: an infinite descending chain below o_t (D11.3 as after round 2 admits it)",
                          "T′: no set of occurrences is a fixed point: S1's {o_1} and {o_2} each fail, and so does every finite set (every infinite one fails by construction)",
                          all(v is not None for v in fails.values()) and not bad,
                          "Rep(o_k) ⟺ ¬∃m>k Rep(o_m). S1's {o_1} fails the equation at o_%d; {o_2} at o_%d (no deeper member is in R, so the equation puts it in R). "
                          "Every finite R ⊆ {o_0..o_%d} (%d sets, nothing deeper in R) fails at some o_k, k ≤ %d: %s. An infinite R holds some o_k and a deeper o_m, so o_k's "
                          "equation fails. So no fixed point: B3 (area 1) is right, S1's 'two incomparable fixed points' is not; S1's conclusion (L526's 'no endless descent' fails on "
                          "such a history) stands." % (fails["{o_1}"], fails["{o_2}"], n, 2 ** (n + 1), n + 1, "none passes" if not bad else bad[:3]), ["I162"]))
    # (b) truncations: one fixed point each, Rep at the deepest occurrence only; its limit is no fixed point
    trunc = {}
    for m in range(1, 9):
        occ = list(range(m))  # o_0 ≻ … ≻ o_(m-1): below[o_k] = {o_j : j > k}
        below = {k: frozenset(range(k + 1, m)) for k in occ}
        allT = {k: True for k in occ}
        noT = {k: False for k in occ}
        trunc[m] = poset_fixed_points(occ, below, allT, allT, noT, "T'")
    ok_b = all(len(v) == 1 and v[0] == frozenset([m - 1]) for m, v in trunc.items())
    parts.append(computed("(b) finite truncations of the chain", "T′: every truncation o_0 ≻ … ≻ o_(m-1) has one fixed point, {o_(m-1)}; the limit ∅ is not a fixed point of the infinite chain",
                          ok_b and infinite_chain_check(set(), 4) == 0,
                          "m = 1..8: %s; ∅ fails at o_0 on the infinite chain." % "; ".join("%d: %s" % (m, [sorted(R) for R in v]) for m, v in trunc.items()), ["I162"]))
    # (c) D11.3 well founded: every finite strict partial order (well founded) on ≤ 4 occurrences, T': one fixed point
    t_ok, t_n, t_first = True, 0, None
    readings_n = {"U": [0, 0], "K": [0, 0], "T": [0, 0], "T'": [0, 0]}
    for size in (1, 2, 3):
        occ = list(range(size))
        for below in strict_orders(size):
            for vals in itertools.product([0, 1], repeat=3 * size):
                held = {o: bool(vals[o]) for o in occ}
                selc = {o: bool(vals[size + o]) for o in occ}
                trace = {o: bool(vals[2 * size + o]) for o in occ}
                for rd in readings_n:
                    k = len(poset_fixed_points(occ, below, held, selc, trace, rd))
                    readings_n[rd][0] += 1
                    readings_n[rd][1] += (k == 1)
                t_n += 1
    occ = list(range(4))
    n4 = 0
    for below in strict_orders(4):
        for vals in itertools.product([0, 1], repeat=8):
            held = {o: True for o in occ}
            selc = {o: bool(vals[o]) for o in occ}
            trace = {o: bool(vals[4 + o]) for o in occ}
            k = len(poset_fixed_points(occ, below, held, selc, trace, "T'"))
            n4 += 1
            if k != 1:
                t_ok = False
                t_first = t_first or (below, selc, trace, k)
    ok_c = t_ok and readings_n["T'"][0] == readings_n["T'"][1]
    parts.append(computed("(c) with D11.3 well founded: finite histories that are partial orders, not only chains",
                          "T′: exactly one fixed point on every strict partial order of ≤ 3 occurrences (all held/Sel/trace inputs) and of 4 occurrences (all held; Sel's conditions and traces all ways)",
                          ok_c, "≤ 3 occurrences: %d cases; one fixed point: U %d, K %d, T %d, T′ %d (of %d each). 4 occurrences, all held: %d cases, T′ one fixed point in every one: %s%s. "
                          "On a well-founded history the T′ equations are a recursion on ≺_h (D18.1), so one fixed point is the recursion theorem; the counts are its check."
                          % (t_n, readings_n["U"][1], readings_n["K"][1], readings_n["T"][1], readings_n["T'"][1], readings_n["T'"][0], n4, t_ok, "" if t_ok else "; first failure %r" % (t_first,)), ["I162"]))
    # (d) the other cuts on the same infinite chain (a record, not a proposal)
    def chain_ok(R, rd, n_window):
        for k in range(n_window + 2):
            if rd == "T":
                need = False  # Sel(o_k): some o_m, m > k, is held; no trace, so no Con
            else:  # U: o_k's own occurrence is in its history
                need = not any(m >= k for m in R)
            if need != (k in R):
                return False
        return True

    fpT = [R for bits in itertools.product([0, 1], repeat=n + 1) for R in [{k for k in range(n + 1) if bits[k]}] if chain_ok(R, "T", n)]
    fpU = [R for bits in itertools.product([0, 1], repeat=n + 1) for R in [{k for k in range(n + 1) if bits[k]}] if chain_ok(R, "U", n)]
    parts.append(computed("(d) the same infinite chain under T and U (record)", "T: ∅ is the one finite fixed point (every occurrence has an earlier holder); U: none",
                          fpT == [set()] and not fpU,
                          "finite R ⊆ {o_0..o_%d}: T fixed points %s; U fixed points %s. T was rejected on FC98 (e) (L195 with L211), so the fix is on the history (D11.3), not the cut."
                          % (n, [sorted(R) for R in fpT], [sorted(R) for R in fpU]), ["I162"]))
    return parts


# ---- L397 after the owner's Q23 (S41): B-Q23n, O4, O5, O6 ---------------------------------------------------

def usable_words(j, alpha):
    """L397's words read alone: 'usable by j when each of its steps is (K2)'. A premise alone has no step, so the
    condition is met by every j (the reading I166 records as the other choice)."""
    return all(claims_b.usable_step(j, u) for u in alpha.steps())


@claim("FC72.new1", ["I87", "I89", "I166"])
def fc72_new1(S):
    from .claims_b import rand_formula
    parts = []
    PM, design = "PM", "design"
    chi = Not(PM)
    phi = And(design, PM)
    bare = Leaf(chi)
    j = Assessor(["MP"], [chi])
    j0 = Assessor(["MP"], [])
    # (a) B-Q23n: L397's words alone vs D9.6 (I166)
    w_j0 = usable_words(j0, bare) and rules_out(bare, phi)
    d_j0 = usable(j0, bare) and rules_out(bare, phi)
    parts.append(computed("(a) B-Q23n: 'usable by j when each of its steps is (K2)' read alone, against D9.6 (I166)",
                          "for j who has never taken ¬PM up: the words make ¬PM alone usable and ruling out design ∧ PM (no step, so every step is (K2)); D9.6 does not",
                          w_j0 and not d_j0,
                          "j0 accepts nothing. Words alone: usable %s, rules out design ∧ PM %s. D9.6 (I166): usable %s. The words' reading makes the claim rule out 'by itself', against "
                          "L397 ('not something the claim does by itself (Part 0)') and L393 ('a claim j has never taken up is not live for j'). j accepts ¬PM: words %s, D9.6 %s."
                          % (usable_words(j0, bare), rules_out(bare, phi), usable(j0, bare), usable_words(j, bare), usable(j, bare)), ["I166"]))
    # (b) O4, O5: premises alone, random: what separates a premise taken as given from the denial is D9.7's block, not steps
    import random
    rng = random.Random(105372)
    n, n_rule, n_block, bad = 0, 0, 0, None
    for _ in range(4000):
        f = rand_formula(rng)
        g = rand_formula(rng)
        if not incons(f, g):
            continue
        n += 1
        leaf = Leaf(g)
        ro = rules_out(leaf, f)
        blocked = canon(Not(f)) in claims_b.conjuncts(g)
        n_rule += ro
        n_block += blocked
        if ro == blocked or leaf.steps():
            bad = bad or (f, g, ro, blocked)
    ok_b = bad is None and n_rule > 0 and n_block > 0
    parts.append(computed("(b) O4, O5: a premise alone rules out with no step; the block alone tells it from the denial",
                          "for every ψ, φ with Incons(φ, ψ): ψ alone has no step, and RO(ψ alone, φ) ⟺ ¬φ is not a conjunct of ψ (read structurally, D9.7)",
                          ok_b and rules_out(bare, phi) and not bare.steps() and not rules_out(bare, PM),
                          "%d random pairs with Incons: %d ruled out by ψ alone (no step), %d blocked (ψ has ¬φ as a conjunct); no other case. ¬PM alone rules out design ∧ PM with no step "
                          "(so 'cannot stand in for the steps' and 'has steps from it to what it rules out' are false of it, S41 Q23); ¬PM alone does not rule out PM (the block, FC72 (e))."
                          % (n, n_rule, n_block), ["I39", "I87"]))
    # (c) O6: the claim triggers the conflict whatever anyone accepts; the ruling out is the assessor's taking it up
    trig = incons(phi, chi)
    out_j = bool(X(j, phi, enumerate_args([chi])))
    out_j0 = bool(X(j0, phi, enumerate_args([chi])))
    acc_before = set(j.accepted)
    _ = X(j, phi, enumerate_args([chi]))
    parts.append(computed("(c) O6: S27 with S28 and Q23", "Incons(design ∧ PM, ¬PM) holds for every assessor (the bare claim triggers the conflict); design ∧ PM is ruled out for j exactly when j has taken ¬PM up (the choice, S28); ruling out changes no claim and no accepted set",
                          trig and out_j and not out_j0 and set(j.accepted) == acc_before,
                          "conflict (no assessor in it): %s; ruled out for j (accepts ¬PM): %s; for j0 (accepts nothing): %s; j's accepted set unchanged by the ruling out: %s. "
                          "What S27 calls not enough is the conflict (the claim) alone: for j0 it does nothing. What does something is j's taking ¬PM as given and going on with it (S28, "
                          "L315); that use, the claim alone as premise, is an argument (S41 Q23). No clash." % (trig, out_j, out_j0, set(j.accepted) == acc_before), ["I166"]))
    # (d) 'already doing something about it' (S28): the ruling out decides the problem for j; the candidate is unchanged
    a1, a2 = "acc1", "acc2"
    prem = [chi, Imp(a1, PM)]
    riv = Not(And(a1, a2))  # the two rivals conflict: not both accounts
    jj = Assessor(["MP", "MT"], prem + [riv])
    jn = Assessor(["MP", "MT"], [Imp(a1, PM), riv])
    args_ = enumerate_args(prem + [riv], forms=("MP", "MT"), depth=2)
    out1_j, out2_j = bool(X(jj, a1, args_)), bool(X(jj, a2, args_))
    out1_n, out2_n = bool(X(jn, a1, args_)), bool(X(jn, a2, args_))
    parts.append(computed("(d) O6: ruling out by ¬PM is already doing something (S28): the problem is decided for j, the candidate is not repaired",
                          "rivals acc1 (gives PM) and acc2: with ¬PM taken up, acc1 is ruled out and acc2 is not (the problem is decided for j, D10.1, D10.6); without it, neither (a problem for jn); acc1's content 'acc1 → PM' is the same in both",
                          out1_j and not out2_j and not out1_n and not out2_n,
                          "j (accepts ¬PM): Out(acc1) %s, Out(acc2) %s; jn: Out(acc1) %s, Out(acc2) %s. The ruling out is the doing (S28); a response that changes acc1 or ¬PM would be "
                          "construction and repair (D12.8, D14.2), which nothing here computes from Out_j (L315)." % (out1_j, out2_j, out1_n, out2_n), ["I87", "I89", "I166"]))
    return parts


# ---- W6: the survival condition (D12.1; L195, L481, L574) ----------------------------------------------------

def value_at(c, a, b):
    """value_t(a,b) (D12.9): (τ(a), σ(b), the relations of every component of E at (τ(a), σ(b)))."""
    return (c.tau[a], c.sigma[b], tuple(c.E.L(k, c.tau[a], c.sigma[b]) for k in c.E.comps))


def alter_at(c, k, xE, w, name):
    E = c.E
    E2 = Org(name, E.ports, E.dom, E.comps, E.foot, E.B, E.A, E._compose,
             (lambda k_, x_, w_: (lambda j, a, b: (E.L(j, a, b) ^ {w_}) if (j, a, b) == (k_, x_[0], x_[1]) else E.L(j, a, b)))(k, xE, w))
    return c.replace(E=E2, name=name)


@claim("FC80.new1", ["I71", "I77", "I78", "I81", "I90"])
def fc80_new1(S):
    from .claims_a import D_and_p, SMALL, BOTHFAM
    from .gen import gen_candidate
    parts = []

    def gen(rng, size):
        D, p = D_and_p(rng, size, proper=True)
        if D is None or len(p.C) < 1 or not D.sol(ONE, p.b0):
            return None
        base = gen_candidate(rng, p, perturb_p=0.0, background_p=0.9, random_tau_p=0.0, demote_p=0.0)
        if not all(base.E.sol(base.tau[a], base.sigma[b]) for (a, b) in p.C if base.translates(a, b)):
            return None
        if not base.E.comps:
            return None
        H = [x for x in p.C if rng.random() < 0.6] or [(ONE, p.b0)]
        pop = [base]
        for i in range(4):
            k = rng.choice(list(base.E.comps))
            x = rng.choice(H)
            if not base.translates(*x):
                continue
            xE = (base.tau[x[0]], base.sigma[x[1]])
            full = sorted(base.E.full(k))
            if not full:
                continue
            pop.append(alter_at(base, k, xE, rng.choice(full), "t%d" % i))
        return p, pop, H

    def wit(m):
        p, pop, H = m
        h = Hist(["o1"], [], set(p.C), admitted=True, prepares=False)
        surv = [c for c in pop if sel(c, H, h)]
        for x in H:
            vals = {}
            for c in surv:
                vals.setdefault(value_at(c, *x), c)
            if len(vals) > 1:
                keep = next(iter(vals))
                env = (lambda x_, v_: (lambda c, H_: value_at(c, *x_) == v_))(x, keep)
                c_out = [c for c in surv if value_at(c, *x) != keep][0]
                s_old, s_new = sel(c_out, H, h), sel(c_out, H, h, env=env)
                if s_old and not s_new:
                    return ("two members of 𝒯 faithful on H = %s with different values at %r ∈ H (a background relation there); an environment keeping only the first "
                            "(the survival condition asks fidelity and that value at %r: a condition on H, L195, L574): the second is Sel under D12.1 as after round 2 (%s), "
                            "not under D12.1 with the environment's condition (%s)\n%s\n%s" % (H, x, x, s_old, s_new, p.describe(), c_out.describe()))
        return None

    parts.append(exists(S, "FC80.new1", 1, "(a) W6: fidelity on H is required, not all the environment asks",
                        "some member of 𝒯 is faithful on H and fails an environment's further condition on its values at H: Sel under D12.1 as after round 2, not under D12.1 with surv",
                        gen, wit, SMALL, 60, BOTHFAM, ["I71", "I90"], note="proper targets (D_and_p proper), nonempty solutions of D and of E at every translated pair of C"))

    def gen_step(rng, size):
        D, p = D_and_p(rng, size)
        if D is None or len(p.C) < 2:
            return None
        base = gen_candidate(rng, p, perturb_p=0.0, background_p=0.5, random_tau_p=rng.choice([0.0, 0.5]), demote_p=0.0)
        if not base.E.comps:
            return None
        H = [x for x in p.C if rng.random() < 0.5] or [(ONE, p.b0)]
        salt = rng.randrange(1 << 30)
        env = lambda c, H_: hash((salt, tuple(repr(value_at(c, *x)) for x in H_ if c.translates(*x)))) % 3 != 0
        return p, base, H, env

    def check(m):
        p, c, H, env = m
        h = Hist(["o1"], [], set(p.C), admitted=True, prepares=False)
        if not sel(c, H, h, env=env):
            return VAC
        imgH = {(c.tau.get(a), c.sigma.get(b)) for (a, b) in H}
        for (a, b) in p.C:
            if (a, b) in H or not c.translates(a, b):
                continue
            xE = (c.tau[a], c.sigma[b])
            if xE in imgH:
                continue
            for k in c.E.comps:
                for w in sorted(c.E.full(k))[:2]:
                    c2 = alter_at(c, k, xE, w, "t_alt")
                    if not sel(c2, H, h, env=env):
                        return "L574's step fails under an environment's condition on H: %r\n%s" % ((a, b), c.describe())
        return None

    parts.append(forall(S, "FC80.new1", 2, "(b) L574's step (Argument 3) with the environment's condition",
                        "t survives on H under fidelity and an environment's condition on its values at H; (τ(a),σ(b)) ∉ (τ×σ)[H] ⇒ t altered at (τ(a),σ(b)) survives too",
                        gen_step, check, SMALL, 40, BOTHFAM, ["I71"]))
    return parts


# ---- S2(i), S2(ii), S2(iii), S3, S-b: D18.1's graph against the formal core and against L526 ----------------------

L526_PAIRS = [  # (x, y): L526 says x depends on y; grouped subjects read collectively (R3A3-06)
    ("(K)", "(O)"), ("(K)", "C"),
    ("(F1)", "(O)"), ("(F1)", "(Q)"), ("(F1)", "(K)"), ("(F2)", "(O)"), ("(F2)", "(Q)"), ("(F2)", "(K)"), ("(A)", "(O)"), ("(A)", "(Q)"), ("(A)", "(K)"),
    ("(E)", "(F1)"), ("(E)", "(F2)"), ("(E)", "(A)"), ("(S)", "(E)"), ("(B)", "(E)"), ("(D)", "(E)"),
    ("(R)", "(F1)"), ("(R)", "(F2)"), ("(R)", "h"), ("(K1)", "(E)"), ("(K2)", "Forms"), ("(K2)", "Scope"), ("(K2)", "Accepted"), ("(K3)", "(K2)"),
    ("Deploy", "(R)"), ("Deploy", "(CT1)"), ("Owned", "h"), ("Owned", "β"), ("Can", "Owned"), ("Can", "(CT1)"), ("Can", "Ω"),
    ("Build", "h"), ("Build", "Owned"), ("Build", "(E)"), ("New", "Deploy"), ("(G)", "Deploy"), ("(G)", "Build"),
    ("(EX)", "(G)"), ("(EX)", "(E)"), ("(EX)", "Deploy"), ("(P)", "ProducedBy"), ("(P)", "O,P"), ("(EX)", "(P)"), ("ProducedBy", "h"), ("ProducedBy", "ActRoute"),
    ("Conf", "(F1)"), ("Conf", "(F2)"), ("Conf", "(A)"), ("Conf", "(O)"), ("ConfCl", "(F1)"), ("ConfCl", "Allow_χ"), ("Riv", "Conf"), ("Riv", "Offered"),
    ("Riv_χ", "ConfCl"), ("Riv_χ", "Offered"), ("OutCand", "(K2)"), ("OutCand", "(E)"), ("Prob", "Riv"), ("Prob", "OutCand"), ("ETV", "Prob"),
]
L526_DISTRIBUTIVE = [("New", "Build"), ("(P)", "(G)"), ("(P)", "(E)"), ("(P)", "Deploy")]  # read each subject alone


def dep_ancestors(dep, n, reading="T'"):
    edges = claims_b.dep_edges(reading, dep)
    seen, todo = set(), [n]
    while todo:
        u = todo.pop()
        for y in edges.get(u, []):
            if y not in seen:
                seen.add(y)
                todo.append(y)
    return seen


def core_def_ids():
    """The definition paragraphs D1.1–D16.XV of the formal core, and what was read: (ids, "name (md5 …)"), or
    (None, the places tried). S107 round 4, area 3 (B14, W6, S1): the core is found by model/corefile.py (one list
    with FC14: the committed layout, a copy under results/, the readers' sandbox); round 3's list fell back to the
    formal core after round 3, then round 2's, and raised FileNotFoundError where none stood."""
    from .corefile import formal_core, describe
    path, md5 = formal_core()
    if path is None:
        return None, md5
    ids = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            m = re.match(r"\*\*(D(\d+)\.(?:\d+|new\d+|XV))\b", line)
            if m and 1 <= int(m.group(2)) <= 16:
                ids.append(m.group(1))
    return ids, describe(path, md5)


@claim("FC32.new1", [])
def fc32_new1(S):
    DEP, DEP_R2 = claims_b.DEP, claims_b.DEP_R2
    parts = []
    ids, read = core_def_ids()
    lab_a = "(a) S2(i): D18.1's nodes against the formal core's paragraphs (§§1–16)"
    st_a = "every definition paragraph of §§1–16 is a node of DEP or folded into one; round 2's DEP (28 nodes) lacked nodes for many"
    if ids is None:  # S107 round 4, area 3 (B14, W6, S1): no core found; the other parts read none
        parts.append(not_tested(lab_a, st_a, "no formal core found at: %s" % read))
    else:
        miss = [d for d in ids if d not in claims_b.D_TO_NODE]
        extra = [d for d in claims_b.D_TO_NODE if d not in ids]
        nodes = set(DEP) | claims_b.TEXT_SINKS | set(claims_b.D0_2)
        bad_fold = sorted(set(v for v in claims_b.D_TO_NODE.values() if v not in nodes))
        r2_missing = sorted(set(claims_b.D_TO_NODE.values()) - set(DEP_R2) - claims_b.TEXT_SINKS - set(claims_b.D0_2))
        parts.append(computed(lab_a, st_a, not miss and not extra and not bad_fold and len(r2_missing) > 0,
                              "%d paragraphs read from %s; not mapped: %s; mapped but not in the core: %s; folds into a missing node: %s. DEP now %d nodes (round 2: %d). "
                              "Holders round 2's DEP lacked: %s." % (len(ids), read, miss or "none", extra or "none", bad_fold or "none", len(DEP), len(DEP_R2), ", ".join(r2_missing))))
    cyc = {rd: claims_b.dep_cycle(False, rd) for rd in ("U", "K", "T", "T'")}
    cyc_r = claims_b.dep_cycle(False, "U", through="(R)")
    parts.append(computed("(b) cycles of the extended graph", "U (as worded): a cycle through (R); K, T, T′: none (the new nodes and edges, Sel → (F1), (F2), CT among them, hide no cycle: S2(ii))",
                          cyc_r is not None and all(cyc[rd] is None for rd in ("K", "T", "T'")),
                          "U: %s (through (R): %s); K: %s; T: %s; T′: %s" % (" → ".join(cyc["U"]) if cyc["U"] else "none", " → ".join(cyc_r) if cyc_r else "none",
                                                                            cyc["K"], cyc["T"], cyc["T'"])))
    sinks = sorted(set(x[1] if isinstance(x, tuple) else x for xs in DEP.values() for x in xs) - set(DEP) - claims_b.TEXT_SINKS)
    unl = [x for x in sinks if x not in claims_b.D0_2]
    # S107 round 4, area 3 (S6): D16.XV's undefined symbols are sinks too (DEP["DefeatConds"]); D0.2 after round 4,
    # area 3 lists them (D0_2_R4A3). (S4: 'subhistory', D11.3's, is no longer a sink.)
    classes = dict(claims_b.D0_2_R3A3, **claims_b.D0_2_R4A3)
    unl_after = [x for x in unl if x not in classes]
    parts.append(computed("(c) S-b: sinks outside the text's lists and D0.2's", "the sinks D0.2 (after round 2) does not list are the symbols S-b names that the graph uses; D0.2 after area 3 (round 3) and after area 3 (round 4, S6) classes every one",
                          len(unl) > 0 and not unl_after,
                          "unlisted by D0.2 after round 2: %s. After area 3: %s. Classes: %s" % (", ".join(unl), unl_after or "none",
                                                                                              "; ".join("%s: %s" % (x, classes[x]) for x in unl))))
    res = {(x, y): y in dep_ancestors(DEP, x) for (x, y) in L526_PAIRS}
    bad = [p for p, v in res.items() if not v]
    b_prim = "(E)" in dep_ancestors(claims_b.DEP_EXPLUSE_PRIMITIVE, "Build")
    k3_r2 = "(K3)" in DEP_R2
    sel_dir = [y for y in ("(F1)", "(F2)", "CT") if y in DEP["Sel"]]
    sel_r2 = [y for y in ("(F1)", "(F2)", "CT", "Build") if y in DEP_R2["Sel"]]
    dist = {p: p[1] in dep_ancestors(DEP, p[0]) for p in L526_DISTRIBUTIVE}
    parts.append(computed("(d) S2(ii), S2(iii), S3: L526's dependences as paths of the graph (T′)",
                          "every dependence L526 states (grouped subjects read collectively, R3A3-06) is a path of DEP; with ExplUse a primitive (round 2's D13.3), Build does not reach (E); round 2's DEP has no (K3)",
                          not bad and not b_prim and not k3_r2 and len(sel_dir) == 3,
                          "%d pairs; failing: %s. Build ⇝ (E) with ExplUse a primitive: %s; with ExplUse defined through the claim 'Acc(ℰ)' (R3A3-05): %s. (K3) a node of round 2's DEP: %s; (K3) ⇝ (K2) now: %s. "
                          "Sel's direct edges now %s (round 2: %s). Read distributively (each subject alone), L526 also says: %s."
                          % (len(res), bad or "none", b_prim, res[("Build", "(E)")], k3_r2, res[("(K3)", "(K2)")], sel_dir, sel_r2 or "none",
                             "; ".join("%s on %s: %s" % (x, y, v) for (x, y), v in dist.items()))))
    uses_expl = sorted(n for n in DEP if "Expl" in dep_ancestors(DEP, n))
    parts.append(computed("(e) L526: 'Nothing depends on an undefined predicate that says \"explains\"'", "only D16.XV's defeat conditions reach the atom Expl; (EX) is a node, defined",
                          uses_expl == ["DefeatConds"] and "(EX)" in DEP, "nodes reaching Expl: %s" % uses_expl))
    # (f) S105 round 3, second checker (critical review, objection 2): L13's "produced by an episode of conjecture and
    # criticism". Crit is D9.10's criticism; CCE, D13.8's complete critical episode, is (EX)'s (D14.7), not Con's.
    # S47 (28 September 2026): the computed fact stands (the maths asks for no criticism event); the reading drawn from
    # it does not: L13's "an episode of conjecture and criticism" names D13.8's episode, which includes one in which no
    # question occurred to the agent as worth investigating (I190), and " and criticism" is back in L13 (S47-T1).
    crit = {rd: {n: "Crit" in dep_ancestors(DEP, n, rd) for n in ("Con", "CT", "Episode", "(EX)")} for rd in ("U", "K", "T", "T'")}
    parts.append(computed("(f) L13: construction asks for no criticism event; created explanation does (critical review, objection 2; S47)",
                          "under U, K, T and T′, Con (D12.2), CT and Episode (D13.8) reach no Crit (D9.10) in DEP; (EX) (D14.7) does, through CCE: the maths asks construction for no criticism event, and an episode of conjecture and criticism (L13) includes one in which no question occurred to the agent (I190; FC84.new1 (a1), (a2): the bridge, Con with or without criticism of designs)",
                          all(not v["Con"] and not v["CT"] and not v["Episode"] and v["(EX)"] for v in crit.values()),
                          "; ".join("%s: %s" % (rd, ", ".join("%s ⇝ Crit %s" % kv for kv in v.items())) for rd, v in crit.items())))
    return parts


# ---- S2(iii): 'explanatory use' (D13.3, L405, L425, L526); S-e-Acc: (EX)'s Account and the designation (D14.7, L449) --

EXPLUSE_READINGS = ("R3A3-05: uses the claim 'Acc(ℰ)', c its organization, transport or contract",
                    "P5: uses the claim 'Acc(ℰ)', c its organization only", "the claim must hold: Acc(ℰ)")


def expl_use(reading, c_role, acc):
    """ExplUse(o, c) given that o uses the claim 'Acc(ℰ)' (Θ, I90), c_role the role c has in ℰ, acc = Acc(ℰ) computed."""
    if reading.startswith("R3A3"):
        return c_role in ("organization", "transport", "contract")
    if reading.startswith("P5"):
        return c_role == "organization"
    return c_role in ("organization", "transport", "contract") and acc


@claim("FC90.new1", ["I56", "I90", "I148"])
def fc90_new1(S):
    from .claims_a import pole_contracts
    parts = []
    D = pole()
    C1, C2, C2s = pole_contracts(D)
    p = Question(D, C1, "b1_45", PortQuery(), "L", name="p_prod")
    fwd, rev = pole_fwd_candidate(p), pole_rev_candidate(p)
    acc = {"ℰ_fwd": account(fwd), "ℰ_rev": account(rev)}
    # Build's other conjuncts (Owned, Prepares, Held, BindingConstruction, ¬TransferComposite) and Attempt, New: set to hold (Θ, I90)
    rows = []
    for nm in ("ℰ_fwd", "ℰ_rev"):
        for rd in EXPLUSE_READINGS:
            build = expl_use(rd, "organization", acc[nm])
            rows.append((nm, rd, build, build and acc[nm]))
    tbl = {(r[0], r[1][:4]): r for r in rows}
    # S108 V3.4: Build for ℰ_rev under D13.3 as the program now reads it (s108s3.expl_use: R3A3-05 by default, the claim must
    # hold under V3.4); under 'none' this is tbl[("ℰ_rev", "R3A3")][2]
    from . import s108s3
    build_rev_now = s108s3.expl_use(True, acc["ℰ_rev"])
    ok_a = (build_rev_now and not (build_rev_now and acc["ℰ_rev"]) and not tbl[("ℰ_rev", "the ")][2]
            and acc["ℰ_fwd"] and not acc["ℰ_rev"])
    parts.append(computed("(a) S2(iii): a system builds the reversed calculation and uses it as an account, in error",
                          "Acc computed (ℰ_fwd yes, ℰ_rev no, FC27); with ExplUse through the claim 'Acc(ℰ)' (R3A3-05) Build holds for ℰ_rev and (EX) fails at its Account conjunct; if the claim had to hold, Build would fail and (EX)'s Account conjunct would add nothing to Origin",
                          ok_a, "Acc: %s. Per candidate and reading, (Build, (EX) with the other conjuncts met): %s. L403 ('A system may understand a theory in error') and (EX)'s own Account conjunct "
                          "(L449) need Build not to ask that the claim hold; L526 ('Build depends on … (E)') needs (E) in Build's definition: the claim's content supplies it."
                          % (acc, "; ".join("%s, %s: (%s, %s)" % (r[0], r[1][:40], r[2], r[3]) for r in rows))
                          + (" [S108 V3.4: D13.3 as switched, Build for ℰ_rev %s]" % build_rev_now if s108s3.on("V3.4") else ""), ["I56", "I90"]))
    # (b) L425: c may be a contract; the found question is used explanatorily as the contract of a claimed account
    role_contract = C1 == frozenset(p.C)
    rb = {rd[:4]: expl_use(rd, "contract", acc["ℰ_fwd"]) for rd in EXPLUSE_READINGS}
    parts.append(computed("(b) L425, Argument 5: c a contract (the pole's production contract C1)", "under R3A3-05 a contract is used explanatorily as the contract of a claimed account; under P5 (organization only) no contract ever is, so (G) never holds of a contract, against L588",
                          role_contract and rb["R3A3"] and not rb["P5: "],
                          "C1 is the contract of ℰ_fwd's question: %s; ExplUse(o, C1): R3A3-05 %s, P5 %s, claim must hold %s." % (role_contract, rb["R3A3"], rb["P5: "], rb["the "]), ["I67"]))
    # (c) S-e-Acc: Acc needs δ_E (D5.3, D6.7); (EX)'s Account((c, p_c, t_c, Γ_c)) (D14.7, L449) supplies none
    aL, aH = account(fwd.replace(deltaE="L"), detail=True), account(fwd.replace(deltaE="H"), detail=True)
    parts.append(computed("(c) S-e-Acc: one (c, p_c, t_c, Γ_c), two designations", "Acc differs between δ_E = L and δ_E = H for the pole's forward candidate: Account((c, p_c, t_c, Γ_c)) is not a function of the four",
                          aL[0] != aH[0], "δ_E = L: %s; δ_E = H: %s" % (aL, aH), ["I20"]))
    return parts


# ---- K4: E9's simulation layers built (L620-L630); FC102 (a), (c) and FC103 (a)-(c) computed ------------------------

def e9_setup():
    from . import e9
    D = e9.object_layer()
    C = [(a, b) for a in D.A for b in D.B]
    p = e9.question(D, C)
    E = e9.sim_layer_S1()
    return e9, D, C, p, E


def fid_table(cand, C):
    out = {}
    for (a, b) in C:
        out[(a, b)] = (F1_at(cand, a, b), F2eq_at(cand, a, b), A_at(cand, a, b))
    return out


@claim("FC102.new1", ["I68", "I100", "I155", "I160"])
def fc102_new1(S):
    from .claims_b import viol_at
    e9, D, C, p, E = e9_setup()
    parts = []
    # (a) S0 and t0: H0 has displacements and velocity changes, no occlusion; B0 is built so a window predictor survives
    A_H0 = [a for a in D.A if a == ONE or a.startswith("disp") or a.startswith("vel")]
    table, B0 = {}, []
    for b in D.B:
        new, ok = {}, True
        for a in A_H0:
            g = e9.frames_of(D, a, b)
            for w, nxt in (((g[0], g[1]), g[2]), ((g[1], g[2]), g[3])):
                old = table.get(w, new.get(w))
                if old is not None and old != nxt:
                    ok = False
                new.setdefault(w, nxt)
        if ok:
            B0.append(b)
            table.update(new)
    f0 = lambda prev, cur: table.get((prev, cur), cur)  # a member of the population: the survivor that keeps the frame where H0 is silent
    A_occ = [a for a in D.A if a.startswith("occ") and not a.endswith("swap")]
    C0 = [(a, b) for a in A_H0 + A_occ for b in B0]
    p0 = e9.question(D, C0) if (ONE, e9.BOUNDS[0]) in C0 else None
    if p0 is None:
        p0 = Question(D, C0, B0[0], PortQuery(), "o1_3", name="p_E9_0")
    S0 = e9.sim_layer_S0(D, f0)
    t0 = e9.t0_candidate(p0, S0)
    H0 = [(a, b) for a in A_H0 for b in B0]
    h = Hist(["o1"], [], set(C0), admitted=True, prepares=False)
    s_t0 = sel(t0, H0, h)
    viol = [(a, b) for (a, b) in C0 if (a, b) not in H0 and viol_at(t0, a, b)]
    reemerge = []
    for (a, b) in viol:
        g = e9.frames_of(D, a, b)
        pred = next(iter(S0.sol(a, b)))
        pf = [tuple(pred[S0.ports.index("o%d_%d" % (c, t))] for c in range(e9.N)) for t in range(e9.T + 1)]
        if pf[3] != g[3] and any(g[3][c] == 1 and pf[3][c] == 0 for c in range(e9.N)):
            reemerge.append((a, b))
    parts.append(computed("(a) t0 survives on H0 and is surprised at re-emergence", "t0 (window-2 occupancy predictor, R3A3-09) meets Sel on H0 (displacements, velocity changes, no occlusion); at occlusion pairs outside H0 it is violated, among them where a hidden thing re-emerges: Surp",
                          s_t0 and bool(reemerge),
                          "B0: %d of %d initial states (those on which H0's windows never conflict); |H0| = %d; Sel(t0; 𝒯, μ, H0): %s; occlusion pairs violated: %d of %d; violated at a re-emergence "
                          "(a thing shown at t = 3 that t0 predicts absent): %d, first %r. Surp = Sel ∧ (a,b) ∉ H0 ∧ Viol (D12.7): %s."
                          % (len(B0), len(D.B), len(H0), s_t0, len(viol), len([x for x in C0 if x not in H0]), len(reemerge), reemerge[:1], s_t0 and bool(reemerge)), ["I68", "I155"]))
    groups = {}
    for (a, b) in [x for x in C0 if x[0] in A_occ]:
        g = e9.frames_of(D, a, b)
        groups.setdefault((g[0], g[1]), set()).add((g[2], g[3]))
    amb = [k for k, v in groups.items() if len(v) > 1]
    parts.append(computed("(b'') in this instance: no window-2 predictor survives the extended history", "two occlusion pairs give S0 the same observed frames and differ at t = 2 or 3, so every f fails at one of them (structural, not parametric)",
                          bool(amb), "observed-frame pairs shared by occlusion pairs with different later frames: %d of %d (w = 2 ≤ L_occ = 2)" % (len(amb), len(groups)), ["I155"]))
    # (c) t1 meets (F1), (F2) and (A) on the extended contract (occlusion, swap and every other edit, every initial state)
    t1 = e9.t1_candidate(p, E)
    ft = fid_table(t1, C)
    ok_c = all(all(v) for v in ft.values())
    parts.append(computed("(c) t1 meets (F1), (F2) on the extended contract", "S1's persistence components carry each thing through occlusion; t1 (λ(k_i) = thing i's continuity subnetwork) meets (F1), the (F2) equation and (A) at every pair, and Hom(τ)",
                          ok_c and hom(t1), "|C| = %d pairs (%d edits × %d initial states); pairs failing (F1, F2eq, A): %d; Hom(τ): %s; Acc's fidelity part F1 ∧ F2: %s"
                          % (len(C), len(D.A), len(D.B), sum(1 for v in ft.values() if not all(v)), hom(t1), F1(t1) and F2(t1)), ["I68", "I69", "I160"]))
    return parts


@claim("FC103.new1", ["I69", "I160"])
def fc103_new1(S):
    e9, D, C, p, E = e9_setup()
    parts = []
    t1, t1s = e9.t1_candidate(p, E), e9.t1_candidate(p, E, swapped=True)
    psiC = {(e9.psi_edit(a), e9.psi_bound(b)) for (a, b) in C} == set(C)
    ans_sym = all(p.ans(a, b) == p.ans(e9.psi_edit(a), e9.psi_bound(b)) for (a, b) in C)
    f1, f2 = fid_table(t1, C), fid_table(t1s, C)
    same = all(f1[x] == f2[x] for x in C)
    parts.append(computed("(a) t1∘ψ meets (F1), (F2), (A) on C exactly when t1 does", "ψ[C] = C and Ans_p∘ψ = Ans_p; at every pair, (F1, F2eq, A) of t1∘ψ equal t1's; Hom for both",
                          psiC and ans_sym and same and hom(t1) == hom(t1s),
                          "ψ[C] = C: %s; Ans_p∘ψ = Ans_p: %s; per-pair equality over %d pairs: %s; both meet all three everywhere: %s; Hom: %s, %s"
                          % (psiC, ans_sym, len(C), same, all(all(v) for v in f1.values()) and all(all(v) for v in f2.values()), hom(t1), hom(t1s)), ["I69"]))
    prem = t1.lam["k1"][0] == t1s.lam["k2"][0] and t1.lam["k2"][0] == t1s.lam["k1"][0]
    ok_kind = one_kind(E, "k1", E, "k2", C, (t1.tau, t1.sigma), (t1s.tau, t1s.sigma)) and one_kind(E, "k2", E, "k1", C, (t1.tau, t1.sigma), (t1s.tau, t1s.sigma))
    parts.append(computed("(b) the exchange meets Argument 2 (ii)'s premise, and each k and its image are of one kind on C", "λ(k1) = λ'(k2), λ(k2) = λ'(k1) (one counterpart, the same subnetwork); k1 through t1 and k2 through t1∘ψ of one kind on C, and k2, k1 likewise (core.one_kind)",
                          prem and ok_kind, "one counterpart: %s; one kind: %s" % (prem, ok_kind), ["I69"]))
    sep = [x for x in C if all(f1[x]) != all(f2[x])]
    parts.append(computed("(c) no pair of C separates the two pairings", "no (a,b) ∈ C at which one pairing meets (F1), (F2), (A) and the other does not (FC51 (b) on E9)",
                          not sep, "separating pairs: %d of %d" % (len(sep), len(C)), ["I69"]))
    return parts
