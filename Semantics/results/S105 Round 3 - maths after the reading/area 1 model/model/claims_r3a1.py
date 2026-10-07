# S105 round 3, area 1 (L1-L228): test claims for the checker's fixes. Ids FC<n>.new<m>; each names the
# finding it answers (B*, W*, S*, K*, N* of results/S105 Round 3 - tabulation of the replies, before any ruling.md)
# and the fix (results/S105 Round 3 - area 1 - verdicts and formal fixes.md). Θ by hand where marked (I90).
import itertools
import random

from .core import ONE, BOT, Org, Roles, Question, FnQuery, F1_at, F2eq_at, A_at, faithful, hom
from .harness import claim, exhaustive, computed, construction
from .claims_a import SMALL, gen_p_cand
from .claims_b import (Hist, sel, con, prov_fixed_points, prov_show, _prov_step, PROV_READINGS, fwd_pole_cand,
                       faithful_on, episode)
from .cases import pole, single_settings, fibre_query, COT


def _sc(fps, n, held=None):
    """Per holding: Sel, Con or Dec (neither); '–' where the occurrence holds nothing (held 0)."""
    return [{("o%d" % (o + 1)): ("–" if held is not None and not held[o] else (("Sel" if sc[o][0] else "") + ("Con" if sc[o][1] else "") or "Dec"))
             for o in range(n)} for R, sc in fps]


# ---- FC12.new2: provenance per holding; records carry their source's (B1, B-e6, K5/N1; D12.1-D12.3′) -------

def _fp_b1fix(n, held, trace, selc, rd):
    """B1's proposed D12.2: Con also asks that no earlier holding of the content be selected."""
    out = []
    for bits in itertools.product([0, 1], repeat=n):
        R = frozenset(o for o in range(n) if bits[o])
        sc = dict(_prov_step(n, held, trace, selc, rd, True, R))
        for o in range(n):
            if sc[o][1] and any(held[x] and sc[x][0] for x in range(o)):
                sc[o] = (sc[o][0], False)
        if frozenset(o for o in range(n) if held[o] and (sc[o][0] or sc[o][1])) == R:
            out.append((R, sc))
    return out


@claim("FC12.new2", ["I90"])
def fc12_new2(S):
    parts = []
    # (a) B1 / B-e6: o1 holds t selected; o2 a trace preparing another transport; o3 a record made from o1's carrier
    n, held, trace, selc = 3, [1, 0, 1], [0, 1, 0], [1, 0, 1]
    rows, ok = [], True
    for rd in PROV_READINGS:
        own = prov_fixed_points(n, held, trace, selc, rd, True)
        rec = prov_fixed_points(n, held, trace, selc, rd, True, rec_of=[None, None, 0])
        rows.append("%s: D12.1–D12.3 on the record's own history %s; D12.3′ (the record carries o1's) %s" % (rd, _sc(own, n, held), _sc(rec, n, held)))
        if rd in ("K", "T", "T'"):
            ok = ok and len(rec) == 1 and _sc(rec, n, held)[0]["o3"] == "Sel" and len(own) == 1 and _sc(own, n, held)[0]["o3"] == "Dec"
    parts.append(computed("(a) B1 / B-e6: a record made from a selected carrier", "without D12.3′ the record's own history makes it Dec (o1 represents cod t before it), against L211; with D12.3′ it carries o1's Sel; under K, T, T′",
                          ok, "held %s, trace %s, Sel's conditions %s.\n%s" % (held, trace, selc, "\n".join(rows)), ["I90", "I54"]))
    # (b) B1: the holding at o3 prepared anew by o2's trace (re-construction of a selected transport)
    trace_b = [0, 1, 1]
    rows, ok = [], True
    for rd in PROV_READINGS:
        f = prov_fixed_points(n, held, trace_b, selc, rd, True)
        g = _fp_b1fix(n, held, trace_b, selc, rd)
        rows.append("%s: per holding %s; B1's fix (Con blocked by an earlier Sel holding) %s" % (rd, _sc(f, n, held), _sc(g, n, held)))
        if rd in ("T", "T'"):
            ok = ok and _sc(f, n, held) == [{"o1": "Sel", "o2": "–", "o3": "Con"}] and _sc(g, n, held) == [{"o1": "Sel", "o2": "–", "o3": "Dec"}]
    parts.append(computed("(b) B1: a selected transport prepared again by a construction trace", "per holding: o1 Sel, o3 Con (L405: construction; L201: construction may operate on selected material); B1's fix makes o3 Dec",
                          ok, "held %s, trace %s, Sel's conditions %s.\n%s" % (held, trace_b, selc, "\n".join(rows)), ["I90"]))
    # (c) B1's fix on FC98 (d)'s case: built on a selected representation
    nb, hb, tb, sb = 2, [1, 1], [0, 1], [1, 1]
    rows, ok = [], True
    for rd in ("K", "T", "T'"):
        f, g = prov_fixed_points(nb, hb, tb, sb, rd, True), _fp_b1fix(nb, hb, tb, sb, rd)
        rows.append("%s: D12.2 %s; B1's fix %s" % (rd, _sc(f, nb), _sc(g, nb)))
        ok = ok and _sc(f, nb) == [{"o1": "Sel", "o2": "Con"}] and _sc(g, nb) == [{"o1": "Sel", "o2": "Dec"}]
    parts.append(computed("(c) B1's fix on FC98 (d): built on a selected representation", "D12.2 gives o2 Con (L201); B1's fix gives o2 Dec, against L201 and L405", ok, "\n".join(rows), ["I90"]))

    # (d) every chain of ≤ 3 holdings, each a record of an earlier one or not: one fixed point under T′,
    # each record with its source's provenance, no Sel ∧ Con; and without D12.3′ records that differ from their source
    def items():
        for n_ in (1, 2, 3):
            for bits in itertools.product(itertools.product([0, 1], repeat=3), repeat=n_):
                for rof in itertools.product(*[[None] + [x for x in range(o) if bits[x][0]] for o in range(n_)]):
                    h_ = [1 if rof[o] is not None else b[0] for o, b in enumerate(bits)]
                    yield n_, h_, [b[1] for b in bits], [b[2] for b in bits], list(rof)

    def check(m):
        n_, h_, t_, s_, rof = m
        f = prov_fixed_points(n_, h_, t_, s_, "T'", True, rec_of=rof)
        if len(f) != 1:
            return "not one fixed point under T′ with D12.3′: %s" % (m,)
        R, sc = f[0]
        for o in range(n_):
            if sc[o][0] and sc[o][1]:
                return "Sel ∧ Con at o%d: %s" % (o + 1, m)
            if rof[o] is not None and sc[o] != sc[rof[o]]:
                return "a record differs from its source: %s" % (m,)
        return None

    def check_own(m):
        n_, h_, t_, s_, rof = m
        f = prov_fixed_points(n_, h_, t_, s_, "T'", True)
        if len(f) == 1:
            R, sc = f[0]
            for o in range(n_):
                if rof[o] is not None and sc[o] != sc[rof[o]]:
                    return "o%d, a record of o%d, gets %s from its own history, its source %s: %s" % (
                        o + 1, rof[o] + 1, _sc(f, n_)[0]["o%d" % (o + 1)], _sc(f, n_)[0]["o%d" % (rof[o] + 1)], m)
        return None

    its = list(items())
    parts.append(exhaustive("FC12.new2", "(d) D12.3′ on every chain of ≤ 3 holdings", "one fixed point under T′; every record has its source's provenance; Sel ∧ Con nowhere",
                            its, check, "chains n ≤ 3; held, trace, Sel's conditions per holding; each holding a record of an earlier holding or not (a record is held)", ["I90", "I161", "I162"]))
    parts.append(exhaustive("FC12.new2", "(d′) without D12.3′", "there is a record whose own history gives it a provenance its source lacks (D12.3 against D12.4, B-e6)",
                            its, check_own, "the same space", ["I90"], kind="there is"))
    # (e) N1 (K5): a selection history whose trace prepares t; t held at its output
    p, c = fwd_pole_cand()
    H = [(ONE, "b1_45")]
    h = Hist(["o1"], [], set(p.C), admitted=True, prepares=True)
    tag = (sel(c, H, h), con(h), sel(c, H, h, i161=False))
    ho, so = bool(faithful(c)), set(H) <= set(p.C) and faithful_on(c, H)
    f = {rd: _sc(prov_fixed_points(1, [ho], [1], [so], rd, True), 1) for rd in PROV_READINGS}
    parts.append(computed("(e) N1 (K5): a trace prepares t on a selection history", "tags (Con read from (R)-tags, the reading T′ replaced): Sel no, Con no, Dec; T′ with Held computed at the output: Con",
                          tag == (False, False, True) and f["T'"] == [{"o1": "Con"}],
                          "tag model: Sel %s, Con %s, Sel without I161 %s; computed (held %s, Sel's conditions %s, trace 1): %s" % (tag[0], tag[1], tag[2], ho, so, f), ["I90", "I161", "I162"]))
    return parts


# ---- FC12.new3: CT(h′, t) exact, not transitive (B2; D12.2) -----------------------------------------

@claim("FC12.new3", ["I90"])
def fc12_new3(S):
    p, c = fwd_pole_cand()
    H = [(ONE, "b1_45")]
    ho, so = bool(faithful(c)), set(H) <= set(p.C) and faithful_on(c, H)
    # o1: a construction trace whose output is a part u of the population's members (u is not cod t: held 0);
    # o2: t, selected from a population whose members are built with u; exact: no trace prepares t; transitive: one does
    held, selc = [0, ho], [0, so]
    rows, ok = [], True
    for rd in PROV_READINGS:
        ex = _sc(prov_fixed_points(2, held, [1, 0], selc, rd, True), 2, held)
        tr = _sc(prov_fixed_points(2, held, [1, 1], selc, rd, True), 2, held)
        rows.append("%s: exact %s; transitive %s" % (rd, ex, tr))
        if rd in ("K", "T", "T'"):
            ok = ok and ex == [{"o1": "–", "o2": "Sel"}]
        if rd in ("T", "T'"):
            ok = ok and tr == [{"o1": "–", "o2": "Con"}]
    return [computed("B2: selection on material a trace built", "CT(h′, t) with t an output of the trace (exact): t selected; transitive: t 'constructed' though no trace prepared it (against L405's 'the rest of the content keeps its inherited provenance', L201)",
                     ok, "t the pole's forward transport (held %s, Sel's conditions on H %s).\n%s" % (ho, so, "\n".join(rows)), ["I90", "I56", "I161"])]


# ---- FC98.new1: well-founded histories (B3, S1, S-fQ2); L195's formula as written (B4) ----------------

def _posets(n):
    pairs = [(i, j) for i in range(n) for j in range(n) if i != j]
    for bits in itertools.product([0, 1], repeat=len(pairs)):
        R = {pr for pr, b in zip(pairs, bits) if b}
        if any((j, i) in R for (i, j) in R):
            continue
        if any((i, k) not in R for (i, j) in R for (j2, k) in R if j == j2 and i != k):
            continue
        yield frozenset(R)


def _dag_fixed_points(n, lt, held, trace, selc):
    """T′ on a finite partial order lt (x ≺⁺ o): Sel(o) = Sel's conditions ∧ ¬trace ∧ no Rep at x ≺ o;
    Con(o) = trace ∧ Held at some x ⪯ o (one contract throughout); Rep = held ∧ (Sel ∨ Con)."""
    fps = []
    for bits in itertools.product([0, 1], repeat=n):
        R = frozenset(o for o in range(n) if bits[o])
        sc = {}
        for o in range(n):
            below = [x for x in range(n) if (x, o) in lt]
            s_ = selc[o] and not trace[o] and not any(x in R for x in below)
            k_ = trace[o] and (held[o] or any(held[x] for x in below))
            sc[o] = (bool(s_), bool(k_))
        if frozenset(o for o in range(n) if held[o] and (sc[o][0] or sc[o][1])) == R:
            fps.append((R, sc))
    return fps


@claim("FC98.new1", ["I90"])
def fc98_new1(S):
    parts = []
    # (a) the descending chain below o_t, truncated at depth N: held, Sel's conditions, no trace everywhere
    rows, ok, bottoms = [], True, []
    for N in range(1, 11):
        n = N + 1  # o_N ≺ … ≺ o_1 ≺ o_t, listed deepest first
        f = prov_fixed_points(n, [1] * n, [0] * n, [1] * n, "T'", True)
        ok = ok and len(f) == 1 and f[0][0] == frozenset([0])
        bottoms.append(len(f) == 1 and f[0][0] == frozenset([0]))
        rows.append("N = %d: %d fixed point(s), Rep at depth %s, o_t %s" % (N, len(f), sorted(N - o for o in f[0][0]) if f else "-", _sc(f, n)[0]["o%d" % n] if f else "-"))

    def cond_fails(Rset, W):
        """The infinite chain o_1 ≻ o_2 ≻ … (depth k): k ∈ R ⟺ no m > k in R. First depth where R fails it."""
        for k in range(1, W + 2):
            if (k in Rset) != (not any(m > k for m in Rset)):
                return k
        return None

    W = 10
    every_finite_fails = all(cond_fails(set(k for k in range(1, W + 1) if bits[k - 1]), W) is not None for bits in itertools.product([0, 1], repeat=W))
    s1 = {"{o_1}": cond_fails({1}, W), "{o_2}": cond_fails({2}, W), "∅": cond_fails(set(), W)}
    ok = ok and every_finite_fails and all(v is not None for v in s1.values())
    parts.append(computed("(a) B3 / S1: an infinite descending chain below o_t (D11.3 acyclic only)",
                          "each truncation at depth N has one fixed point, Rep at its deepest occurrence only, so the pointwise limit is ∅; the infinite chain has no fixed point: ∅ and every finite R fail the equations at some depth (checked for all R within depth 10), and an infinite R fails at each member (a member lies below it); S1's {o_1}, {o_2} fail",
                          ok, "%s\nfirst depth at which S1's candidates fail: %s; every R ⊆ depths 1..%d fails: %s" % ("\n".join(rows), s1, W, every_finite_fails), ["I90", "I162"]))

    # (b) D11.3 with ≺_h well founded: every finite partial order (≤ 3 occurrences), every held/trace/Sel's conditions
    def items():
        for n in (1, 2, 3):
            for lt in _posets(n):
                for bits in itertools.product(itertools.product([0, 1], repeat=3), repeat=n):
                    yield n, lt, [b[0] for b in bits], [b[1] for b in bits], [b[2] for b in bits]

    def check(m):
        n, lt, h_, t_, s_ = m
        f = _dag_fixed_points(n, lt, h_, t_, s_)
        if len(f) != 1:
            return "%d fixed points: %s" % (len(f), m)
        R, sc = f[0]
        if not R <= frozenset(o for o in range(n) if h_[o]):
            return "Rep without Held: %s" % (m,)
        if any(sc[o][0] and sc[o][1] for o in range(n)):
            return "Sel ∧ Con: %s" % (m,)
        return None

    parts.append(exhaustive("FC98.new1", "(b) well-founded histories, branching included", "T′ has exactly one fixed point; Rep ⊆ Held; Sel ∧ Con nowhere",
                            list(items()), check, "every labelled partial order on ≤ 3 occurrences; held, trace, Sel's conditions per occurrence", ["I90", "I161", "I162"]))
    # (c) B4: L195's formula as written, o ≺_{h(t)} o_t strict, with (R) of L208: a selection
    rows, ok = [], True
    for n in (1, 2):
        held, trace, selc = [0] * (n - 1) + [1], [0] * n, [0] * (n - 1) + [1]
        for rd in PROV_READINGS:
            f = prov_fixed_points(n, held, trace, selc, rd, True)
            rows.append("n = %d, %s: %s" % (n, rd, _sc(f, n, held)))
            if rd in ("K", "T'"):
                ok = ok and _sc(f, n, held) == [dict([("o%d" % (o + 1), "–") for o in range(n - 1)] + [("o%d" % n, "Sel")])]
            if rd == "U":
                ok = ok and f == []
    parts.append(computed("(c) B4: L195's formula (strict ≺) read with (R)", "a selection has one fixed point with the output Sel under the strict exclusion (K, T′); only U, which puts o_t in its own history, has none",
                          ok, "\n".join(rows), ["I90"]))
    return parts


# ---- FC84.new2: "immediately after" in D13.8 (B9, S-fQ6) ---------------------------------------------

@claim("FC84.new2", ["I90"])
def fc84_new2(S):
    def episode_forms(n, lt, q, recs):
        cover = {(i, j) for (i, j) in lt if not any((i, k) in lt and (k, j) in lt for k in range(n))}
        imm = all(q[j] in recs for (i, j) in cover if q[i] != q[j])
        ordd = all(q[j] in recs for (i, j) in lt if q[i] != q[j])
        unord = all(q[j] in recs for i in range(n) for j in range(n) if i != j and q[i] != q[j])
        return imm, ordd, unord

    def items():
        for n in (1, 2, 3, 4):
            for lt in _posets(n):
                for q in itertools.product(["C", "C'", "C''"], repeat=n):
                    used = sorted(set(q))
                    for r in itertools.product([0, 1], repeat=len(used)):
                        yield n, lt, q, frozenset(x for x, b in zip(used, r) if b)

    its = list(items())

    def check(m):
        imm, ordd, unord = episode_forms(*m)
        return None if imm == ordd else "covering %s, ordered pairs %s: %s" % (imm, ordd, m)

    def check_un(m):
        imm, ordd, unord = episode_forms(*m)
        return None if imm == unord else "covering %s, P4 as written (unordered) %s: n %d, order %s, q %s, recorded %s" % (imm, unord, m[0], sorted(m[1]), m[2], sorted(m[3]))

    # (c) on chains, the program's episode (a record per change, positional) = covering with a record per change
    def items_c():
        for n in (1, 2, 3, 4):
            for q in itertools.product(["C", "C'"], repeat=n):
                for r in itertools.product([False, True], repeat=n):
                    yield n, list(q), list(r)

    def check_c(m):
        n, q, r = m
        cover_ok = all(r[i] for i in range(1, n) if q[i] != q[i - 1])
        return None if episode(q, r, "S41") == cover_ok else "program %s, covering %s: %s" % (episode(q, r, "S41"), cover_ok, m)

    return [exhaustive("FC84.new2", "(a) covering (B9) and every ordered pair", "Episode with 'o′ immediately after o' as the covering relation of ≺⁺_h′ = Episode over every o ≺⁺ o′, records Rec_h′(ρ_{q(o′)}) as D13.8 keys them",
                       its, check, "every labelled partial order on ≤ 4 occurrences, q(o) ∈ {C, C′, C″}, any set of recorded contracts", ["I165"]),
            exhaustive("FC84.new2", "(b) P4 as written (every o, o′ ∈ h′, unordered)", "there is h′ where P4's form and the covering form differ",
                       its, check_un, "the same space", ["I165"], kind="there is"),
            exhaustive("FC84.new2", "(c) the program's episode on chains", "claims_b.episode (a record per change into o_i) = the covering form with a record per covering change",
                       list(items_c()), check_c, "chains ≤ 4, q ∈ {C, C′}, a record flag per occurrence", ["I165"])]


# ---- FC13.new1: D4.6 with the set O_j of ports j assigns (S-D1, P8) ------------------------------------

@claim("FC13.new1", [])
def fc13_new1(S):
    def compose(a2, a1):
        if a1 == ONE:
            return a2
        if a2 == ONE:
            return a1
        return None

    def Lf(j, a, b):
        if a == "sv0":
            return frozenset((0, y) for y in (0, 1))
        if a == "sw0":
            return frozenset((x, 0) for x in (0, 1))
        return frozenset([(0, 0), (1, 1)])

    D = Org("Dcoll", ["v", "w"], {"v": (0, 1), "w": (0, 1)}, ["k"], {"k": ("v", "w")}, ["b"], [ONE, "sv0", "sw0"], compose, Lf)
    R = Roles(D)
    C = frozenset([(ONE, "b"), ("sv0", "b"), ("sw0", "b")])
    asg = dict(R.asg)
    ok_j = [v for v, k in asg.items() if k == "k"]
    causal = {rd: R.causal("k", C, rd) for rd in ("R-i", "R-ii")}
    return [computed("P8: one component assigning two ports", "asg(v) = asg(w) = k, so D4.6's 'o_k, the port k assigns' has no value; with O_k := {v : asg(v) = k} and Set_{O_k} := ∪ Set_v (P2, I124) Causal_C(k) is defined, as the program computes it, under both readings of observation edits (I06)",
                     sorted(ok_j) == ["v", "w"] and R.set_oj("k") == frozenset(["sv0", "sw0"]) and all(causal.values()),
                     "asg %s; ports k assigns %s; Set_{O_k} %s; Causal_C(k) %s" % (asg, sorted(ok_j), sorted(R.set_oj("k")), causal), ["I124", "I06"])]


# ---- FC104.new1: the extent of 'fidelity' at L220 (W1/W2) ----------------------------------------------

@claim("FC104.new1", ["I90"])
def fc104_new1(S):
    """W1/W2: the pole's forward transport with δ_E designating θ (T) while the question reads L: (F1), (F2) hold,
    (A) fails at every pair. A random search (gen_p_cand, 172,800 candidates at scale 4, identity value maps)
    found no pair with (F1) ∧ F2eq ∧ ¬(A): there δ_E always carries the target's designation."""
    p, c0 = fwd_pole_cand()
    c = c0.replace(deltaE="T", name="ℰ_fwd, δ_E = θ")
    rows = []
    for (a, b) in sorted(p.C, key=repr):
        rows.append("(%s, %s): F1 %s, F2eq %s, (A) %s" % (a, b, F1_at(c, a, b), F2eq_at(c, a, b), A_at(c, a, b)))
    x = (ONE, "b1_45")
    narrow = not (F1_at(c, *x) and F2eq_at(c, *x))
    wide = narrow or not A_at(c, *x)
    s_ = sel(c, [x], Hist(["o1"], [], {x}))
    return [computed("(a) W1: (F1) and the (F2) equation at a pair, (A) failing there", "narrow Viol (D12.7; L189's 'faithful') fails at the pair, Viol⁺ (with (A)) holds: the two extents differ",
                     (not narrow) and wide, "\n".join(rows), ["I50"]),
            computed("(b) under the wide extent a selected transport is violated at a pair of its own history", "Sel(t; {t}, id, H) with H = {(1, b1_45)}: Viol⁺ at a pair of H, so D12.7's Sel ∧ Viol(a,b) ⇒ (a,b) ∉ H (L221, L223) holds only under the narrow extent",
                     s_ and wide and not narrow, "Sel %s; Viol (narrow) %s; Viol⁺ (wide) %s at %r ∈ H" % (s_, narrow, wide, x), ["I50", "I90"])]


# ---- FC28.new1, FC28.new2: identification (B7 and N3 run; B6's obs at a non-single Sol) ------------------

def obs_value(D, port, a, b, reading="bot"):
    """obs(a,b) (D3.3): 'bot' the single value of port on Sol_D(a,b), ⊥ otherwise (R3A1-06, as D3.2, D6.4);
    'image' the set of its values (B6's I168); 'single' the single value, None where there is none."""
    vals = frozenset(z[D.ports.index(port)] for z in D.sol(a, b))
    if reading == "image":
        return vals
    return next(iter(vals)) if len(vals) == 1 else (BOT if reading == "bot" else None)


def ident(D, C, port, reading="bot"):
    """Ident's contract clause (D3.3, I163): ∃(a,b),(a′,b′) ∈ C: obs(a,b) ≠ obs(a′,b′); 'single' asks one value at both."""
    ob = [obs_value(D, port, a, b, reading) for (a, b) in sorted(C, key=repr)]
    if reading == "single":
        return any(x is not None and y is not None and x != y for x in ob for y in ob)
    return len(set(ob)) > 1


@claim("FC28.new1", ["I92"])
def fc28_new1(S):
    parts = []
    D = pole()
    b0 = "b1_45"
    Cs = [(frozenset([(ONE, b0)] + [(ONE, b) for b in D.B]), "C_id: boundaries only"),
          (frozenset([(ONE, b0)] + [(a, b0) for a in single_settings(D, ["H"])]), "settings of H"),
          (frozenset([(ONE, b0)] + [(a, b0) for a in single_settings(D, ["L"])]), "settings of L")]
    res = [(why, ident(D, C, "L")) for C, why in Cs]
    parts.append(computed("(a) B7's FC28.new1, run: Ident on the pole under D3.3 (I163), the fibre query", "Ident met on C_id, on settings of H and on settings of L", all(r for _, r in res),
                          "; ".join("%s %s" % r for r in res), ["I92", "I163"]))

    # (b) N3, run: a setting of the observed port that leaves its value constant
    def Lf(j, a, b):
        if j == "cH":
            return frozenset([(1,), (2,)])
        return frozenset([(1, 1), (2, 1)]) if a == "setL1" else frozenset([(1, 1)])

    def compose(a2, a1):
        return a2 if a1 == ONE else (a1 if a2 == ONE else None)

    D3 = Org("D3", ["H", "L"], {"H": (1, 2), "L": (1, 2)}, ["cH", "cL"], {"cH": ["H"], "cL": ["H", "L"]}, ["b0"], [ONE, "setL1"], compose, Lf)
    C3 = frozenset([(ONE, "b0"), ("setL1", "b0")])
    R3 = Roles(D3)
    sets_L = "setL1" in R3.Set["L"]
    i163 = ident(D3, C3, "L")
    parts.append(computed("(b) N3, run: a contract setting the observed port without changing its value", "Ident not met under D3.3 (I163: obs equal at both pairs); met under the round-1 wording 'C holds edits to the observed value' (setL1 sets L)",
                          (not i163) and sets_L, "obs at the two pairs %s; I163 %s; setL1 ∈ Set_L %s" % ([obs_value(D3, "L", a, b) for (a, b) in sorted(C3, key=repr)], i163, sets_L), ["I163"]))
    return parts


@claim("FC28.new2", [])
def fc28_new2(S):
    """B6: obs where the observed port is not single on Sol (L105: several solutions remain several). A weathervane:
    W the wind (0 still, 1 north, 2 gusty), P where it points; b_still leaves P ∈ {n, s}, b_north gives n, b_gusty {s, e}."""
    def Lf(j, a, b):
        if j == "cW":
            return frozenset([({"b_still": 0, "b_north": 1, "b_gusty": 2}[b],)])
        return frozenset([(0, "n"), (0, "s"), (1, "n"), (2, "s"), (2, "e")])

    D = Org("D_vane", ["W", "P"], {"W": (0, 1, 2), "P": ("n", "s", "e")}, ["cW", "cP"], {"cW": ["W"], "cP": ["W", "P"]},
            ["b_still", "b_north", "b_gusty"], [ONE], lambda a2, a1: ONE, Lf)
    cases = [("still/north", frozenset([(ONE, "b_still"), (ONE, "b_north")])), ("still/gusty", frozenset([(ONE, "b_still"), (ONE, "b_gusty")])),
             ("north only", frozenset([(ONE, "b_north")]))]
    rows, got = [], {}
    for nm, C in cases:
        got[nm] = {rd: ident(D, C, "P", rd) for rd in ("bot", "image", "single")}
        rows.append("%s: obs %s; Ident bot %s, image %s, single %s" % (nm, {b: obs_value(D, "P", a, b) for (a, b) in sorted(C, key=repr)}, got[nm]["bot"], got[nm]["image"], got[nm]["single"]))
    Dp = pole()
    Cid = frozenset((ONE, b) for b in Dp.B)
    pole_same = len(set(ident(Dp, Cid, "L", rd) for rd in ("bot", "image", "single"))) == 1
    ok = got["still/north"] == {"bot": True, "image": True, "single": False} and got["still/gusty"] == {"bot": False, "image": True, "single": False} and pole_same
    return [computed("B6: obs where Sol has several observed values", "⊥-reading (R3A1-06): Ident on still/north (⊥ ≠ n, as Q15's contrast), not on still/gusty (⊥ = ⊥); the image reading also on still/gusty; the singleton reading on neither; the three agree on the pole's C_id",
                     ok, "\n".join(rows) + "\npole C_id: the three readings agree %s" % pole_same, [])]


# ---- FC97.new1: H and the survival condition typed as contents (B5, S-D2; D11.2′ by L590's construction) ---

@claim("FC97.new1", [])
def fc97_new1(S):
    """L590's construction applied to a finite H ⊆ A × B and to the survival condition Faithful_H over a population:
    a membership port per pair (and a survival port per member), one component fixing them, settings as edits."""
    p, c = fwd_pole_cand()
    pairs = sorted(p.C, key=repr)
    H = set(pairs[:2])
    pop = {"t": c}
    ports = ["m%d" % i for i in range(len(pairs))] + ["s_%s" % k for k in pop]
    dom = {v: (0, 1) for v in ports}
    val = tuple([1 if x in H else 0 for x in pairs] + [1 if faithful_on(pop[k], list(H)) else 0 for k in pop])

    def Lf(j, a, b):
        return frozenset([val])

    O = Org("D_H_surv", ports, dom, ["fix"], {"fix": tuple(ports)}, ["β"], [ONE], lambda a2, a1: ONE, Lf)
    sols = O.sol(ONE, "β")
    ok = len(sols) == 1 and all(O.dom[v] for v in O.ports)
    return [construction("H and the survival condition as organizations (L590)", "a finite H ⊆ A × B and Faithful_H over 𝒯 are organizations in the sense of (O), so Rep(o, H) and Rep(o, surv) in D12.1 are typed as D12.5 types Rep",
                         ok, "ports %s; one solution %s" % (list(O.ports), sorted(sols)), [])]
