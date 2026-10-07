# S104 round 2, the owner's answers (decision S41, 28 September 2026): the new claims for Q2 and Q6.
# Q15 is carried by core.contrast (FC22 (b)); Q23 by args.usable and args.enumerate_args (FC72 (d)-(f)).
# Ids: FC<n>.new<m>. Stated in "formal claims, after round 2.md", marked [owner S41: Qn].
import itertools

from .core import ONE, account
from .args import Not, Imp, Leaf, Step, Assessor, X, atoms
from .harness import claim, forall, exhaustive, computed, construction, VAC
from .claims_a import SMALL, BOTHFAM, gen_p_cand
from .claims_b import (Hist, sel, con, fwd_pole_cand, prov_fixed_points, prov_show, build_at, episode, chain_eps,
                       EPISODE_READINGS)


# ---- Part XV, (Suff) (D16.XV) [owner S41: Q2] ------------------------------------------------------------
# Expl(ℰ) is an atom. "An argument not using (E)": Acc ∉ Uses(α), Uses(α) the atoms of α's leaves.
SUFF_READINGS = ("L536", "L17 as text 104 words it", "L17 (S41)")


def suff_defeats(acc, dec, out, reading):
    """ℰ ∈ Def_j(reading): L536 and L17 as S41 writes it ask Acc ∧ ¬Dec(t) ∧ an argument not using (E) that
    rules out Expl(ℰ); L17 as text 104 words it has no ¬Dec(t) (E06)."""
    if reading == "L17 as text 104 words it":
        return bool(acc and out)
    return bool(acc and not dec and out)


def expl_ok(acc, dec, expl):
    """The owner's condition on the atom (S41, Q2): Acc(ℰ) ∧ Dec(t) ⇒ ¬Expl(ℰ)."""
    return not (acc and dec and expl)


def uses(alpha):
    return set().union(*[atoms(l.claim) for l in alpha.leaves()])


def expl_ruled_out(j, name):
    """An argument usable by j, not using (E), that rules out Expl(ℰ): a record r and 'r → ¬Expl', modus ponens."""
    e = "Expl_" + name
    alpha = Step("MP", Not(e), [Leaf("r", "record"), Leaf(Imp("r", Not(e)))])
    got = [a for a in X(j, e, [alpha]) if "Acc_" + name not in uses(a)]
    return bool(got), alpha


def provenance_of(cand, kind, H):
    """A history for t, Θ by hand (I90): 'Dec' no selection admitted and no trace; 'Con' a trace preparing t and
    cod t represented; 'Sel' a selection history on H. Returns (Sel, Con, Dec) as computed by sel and con."""
    occ = set(cand.p.C)
    if kind == "Dec":
        h = Hist(["o1"], [], occ, admitted=False, prepares=False)
    elif kind == "Con":
        h = Hist(["o1", "o2"], [("o2", "cod")], occ, admitted=True, prepares=True)
    else:
        h = Hist(["o1"], [], occ, admitted=True, prepares=False)
    s, k = sel(cand, H, h), con(h)
    return s, k, (not s and not k)


@claim("FC30.new1", ["I90"])
def fc30_new1(S):
    parts = []
    p, c = fwd_pole_cand()
    H = [(ONE, "b1_45")]
    acc = account(c)
    rows, ok = [], acc
    for kind in ("Dec", "Con", "Sel"):
        s, k, dec = provenance_of(c, kind, H)
        for accepts in (True, False):
            j = Assessor(["MP"], ["r", Imp("r", Not("Expl_" + c.name))] if accepts else [])
            out, _ = expl_ruled_out(j, c.name)
            d = {r: suff_defeats(acc, dec, out, r) for r in SUFF_READINGS}
            rows.append("%s (Sel %s, Con %s, Dec %s), argument usable %s: %s" % (kind, s, k, dec, out, "; ".join("%s %s" % (r, d[r]) for r in SUFF_READINGS)))
            ok = ok and d["L17 (S41)"] == d["L536"] and d["L536"] <= d["L17 as text 104 words it"]
            if kind == "Dec" and accepts:
                ok = ok and d["L17 as text 104 words it"] and not d["L536"] and not d["L17 (S41)"]
            if kind == "Con" and accepts:
                ok = ok and all(d.values())
    _, alpha = expl_ruled_out(Assessor(["MP"], []), c.name)
    parts.append(computed("(a) the student's formula: a declared account ruled out as an explanation",
                          "the pole's forward candidate meets (E) (FC26); with a declared transport and an argument not using (E) that rules out Expl(ℰ), it is in Def(L17 as text 104 words it) and in neither Def(L536) nor Def(L17) as S41 writes it; with a constructed transport it is in all three",
                          ok, "Acc(ℰ_fwd) %s; argument:\n%s\n%s" % (acc, alpha.show(2), "\n".join(rows)), ["I90"]))

    def gen(rng, size):
        m = gen_p_cand(rng, size)
        if m is None:
            return None
        q, cand = m
        return cand, rng.choice(("Dec", "Con", "Sel")), rng.random() < 0.5

    def check(m):
        cand, kind, accepts = m
        a = account(cand)
        s, k, dec = provenance_of(cand, kind, [(ONE, cand.p.b0)])
        j = Assessor(["MP"], ["r", Imp("r", Not("Expl_" + cand.name))] if accepts else [])
        out, _ = expl_ruled_out(j, cand.name)
        d = {r: suff_defeats(a, dec, out, r) for r in SUFF_READINGS}
        if d["L17 (S41)"] != d["L536"]:
            return "Def(L17, S41) ≠ Def(L536): %s\n%s" % (d, cand.describe())
        if d["L17 as text 104 words it"] != (d["L536"] or (a and dec and out)):
            return "Def(L17 as text 104) is not Def(L536) with the declared accounts ruled out as explanations: %s\n%s" % (d, cand.describe())
        return None

    parts.append(forall(S, "FC30.new1", 2, "(b) one defeat set", "Def_j(L17, S41) = Def_j(L536); Def_j(L17 as text 104 words it) = Def_j(L536) ∪ {ℰ : Acc ∧ Dec(t) ∧ Expl(ℰ) ruled out}",
                        gen, check, SMALL, 40, BOTHFAM, ["I90"], note="provenance Θ by hand (I90): Dec, Con or Sel, each computed by sel and con"))
    both = True
    for a, d_ in itertools.product((False, True), repeat=2):
        expl = a and not d_  # Expl := Acc ∧ ¬Dec
        suff = (not (a and not d_)) or expl  # (Suff) as conjectured: Acc ∧ ¬Dec ⇒ Expl
        both = both and suff and expl_ok(a, d_, expl)  # the owner's condition: Acc ∧ Dec ⇒ ¬Expl
    parts.append(construction("(c) the owner's condition and (Suff) have a common model", "Expl := Acc ∧ ¬Dec meets Acc ∧ ¬Dec ⇒ Expl ((Suff) as conjectured) and Acc ∧ Dec ⇒ ¬Expl (S41, Q2), on every candidate",
                              both, "checked on the four values of (Acc, Dec); (E) itself takes no provenance (FC30): ¬Dec(t) stands beside it"))
    return parts


# ---- Episodes and construction (D13.8, D12.2) [owner S41: Q6] ---------------------------------------------

@claim("FC84.new1", ["I90"])
def fc84_new1(S):
    parts = []
    # (a) the bridge to a fixed brief: o1 ≺ o2, one contract throughout; a trace prepares t (at o2); cod t held at o2
    n, held, trace, selc = 2, [0, 1], [0, 1], [0, 0]
    qs = ["C_brief", "C_brief"]
    rows, res = [], {}
    for rd in EPISODE_READINGS:
        eps = chain_eps(qs, [False, False], rd)
        fps = prov_fixed_points(n, held, trace, selc, "T'", True, eps)
        conv = [sc[1][1] for R, sc in fps]
        res[rd] = (len(fps), conv, build_at(n, held, trace, "T'", fps[0][0] if fps else frozenset(), 1))
        rows.append("%s: %d fixed point(s) %s; Con at o2 %s; Build at o2 %s" % (rd, len(fps), prov_show(n, fps), conv, res[rd][2]))
    h_s41 = Hist(["o1", "o2"], [("o2", "cod")], set(), prepares=True, contracts=qs, records=[False, False])
    tag = {rd: con(h_s41, reading=rd) for rd in EPISODE_READINGS}
    ok_a = res["S41"][0] == 1 and res["S41"][1] == [True] and res["S41"][2] and res["L55"][1] == [False] and res["L55"][2] and tag["S41"] and not tag["L55"]
    parts.append(computed("(a) the bridge to a fixed brief", "one contract throughout, a trace preparing t, cod t held at the output: Con(t) under D13.8 as S41 has it; under L55 as text 104 words it Con fails; Build holds under both",
                          ok_a, "chain o1 ≺ o2, q = %s; held %s, trace %s, Sel's conditions %s; cut T′ (I162), I161.\n%s\ntag model (con): S41 %s, L55 %s" % (qs, held, trace, selc, "\n".join(rows), tag["S41"], tag["L55"]), ["I90", "I162", "I165"]))
    # (b) a recorded change of contract C → C' at o2; (c) the same change unrecorded
    out = []
    ok_b = ok_c = True
    for recd in (True, False):
        q2, r2 = ["C", "C'"], [False, recd]
        for rd in EPISODE_READINGS:
            eps = chain_eps(q2, r2, rd)
            span = episode(q2, r2, rd)
            fps = prov_fixed_points(n, [1, 1], trace, selc, "T'", True, eps)
            conv = [sc[1][1] for R, sc in fps]
            out.append("change %s, %s: o1 ≺ o2 an episode %s; Con at o2 %s" % ("recorded" if recd else "unrecorded", rd, span, conv))
            if recd:
                ok_b = ok_b and span and conv == [True]
            else:
                ok_c = ok_c and not span and conv == ([True] if rd == "S41" else [False])
    parts.append(computed("(b) a recorded change of contract", "C → C' at o2 with its provenance record: o1 ≺ o2 is an episode under both readings, and Con(t) at o2", ok_b, "\n".join(o for o in out if "unrecorded" not in o), ["I90", "I165"]))
    parts.append(computed("(c) an unrecorded change of contract", "o1 ≺ o2 is then no episode (L55's record clause, I165); Con at o2 needs an episode after the change holding the target: {o2} under S41, none under L55's wording", ok_c,
                          "\n".join(o for o in out if "unrecorded" in o), ["I90", "I165"]))

    # (d) every chain of ≤ 3 occurrences with contracts and records: Con under S41 ⊇ Con under L55's wording, differing
    # exactly where no episode ending at the output holds a change of contract; Sel ∧ Con at no fixed point
    def items():
        for n_ in (1, 2, 3):
            for bits in itertools.product(itertools.product([0, 1], repeat=3), repeat=n_):
                held_, trace_, selc_ = [b[0] for b in bits], [b[1] for b in bits], [b[2] for b in bits]
                for q_ in itertools.product(["C", "C'"], repeat=n_):
                    if q_[0] != "C":
                        continue
                    for r_ in itertools.product([False, True], repeat=n_):
                        if r_[0]:
                            continue
                        yield n_, held_, trace_, selc_, list(q_), list(r_)

    def check(m):
        n_, held_, trace_, selc_, q_, r_ = m
        fs = {rd: prov_fixed_points(n_, held_, trace_, selc_, "T'", True, chain_eps(q_, r_, rd)) for rd in EPISODE_READINGS}
        if len(fs["S41"]) != 1 or len(fs["L55"]) != 1:
            return "not one fixed point under T′: %s" % m
        o = n_ - 1
        cs, cl = fs["S41"][0][1][o][1], fs["L55"][0][1][o][1]
        if cl and not cs:
            return "Con under L55's wording but not under S41: %s" % (m,)
        for rd in EPISODE_READINGS:
            R, sc = fs[rd][0]
            if any(sc[x][0] and sc[x][1] for x in range(n_)):
                return "Sel ∧ Con under %s: %s" % (rd, m)
        if cs and not cl:
            chg_eps = [i for i in range(o + 1) if episode(q_[i:o + 1], r_[i:o + 1], "S41") and episode(q_[i:o + 1], r_[i:o + 1], "L55")
                       and any(held_[x] for x in range(i, o + 1))]
            if chg_eps:
                return "Con differs although an episode with a change holds the target: %s" % (m,)
        return None

    parts.append(exhaustive("FC84.new1", "(d) every chain of ≤ 3 occurrences", "Con(S41) ⊇ Con(L55's wording), the difference exactly where no episode ending at the output holds a change of contract and the target; Sel ∧ Con at no fixed point; one fixed point each (T′)",
                            list(items()), check, "chains o1 ≺ … ≺ on, n ≤ 3; held, trace, Sel's conditions per occurrence; q(o) ∈ {C, C'}; records per change", ["I90", "I161", "I162", "I165"]))
    return parts
