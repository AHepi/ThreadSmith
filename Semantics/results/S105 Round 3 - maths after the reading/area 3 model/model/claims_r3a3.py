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
