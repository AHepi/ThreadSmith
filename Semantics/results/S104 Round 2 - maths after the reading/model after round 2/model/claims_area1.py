# S104 round 2, area 1 (L1-L228): the new claims of the area 1 checker's formal fixes.
# Ids: FC<section>.new<n>. Each is stated in "area 1 - verdicts and formal fixes.md".
import itertools

from .core import ONE, Roles, OBS_READING
from .gen import gen_org, gen_surg
from .harness import claim, forall, exists, exhaustive, computed, VAC
from .cases import pole
from .claims_a import SMALL, MID, BOTHFAM, pole_contracts
from .claims_b import Hist, sel, con, fwd_pole_cand, faithful_on, prov_fixed_points, prov_show, PROV_READINGS
from .claims_a import gen_p_cand
from .core import faithful


def _rand_C(rng, D):
    b0 = D.B[0]
    return frozenset([(ONE, b0)] + [(a, b) for a in D.A for b in D.B if (a, b) != (ONE, b0) and rng.random() < 0.5])


@claim("FC2.new1", ["I77", "I78"])
def fc2_new1(S):
    """Why D2.4 is settled to R-ii (A1-04): under R-i no component that reads a port another component
    assigns is ever a causal assignment; under R-ii one can be."""
    parts = []

    def gen(rng, size):
        D = gen_org(rng, size)
        return D, _rand_C(rng, D)

    def reads_assigned(R, D, j):
        return any(m in R.asg and R.asg[m] != j for m in D.foot[j] if R.asg.get(m) != j)

    def check(m):
        D, C = m
        R = Roles(D)
        hit = False
        for j in D.comps:
            if not reads_assigned(R, D, j) or not R.outputs_of(j):
                continue
            hit = True
            if R.causal(j, C, "R-i"):
                return "under R-i, %s reads a port another component assigns and is causal on C = %s\n%s" % (j, sorted(C, key=repr), D.describe())
        return None if hit else VAC

    parts.append(forall(S, "FC2.new1", 1, "R-i: a reader of an assigned port is never causal",
                        "under R-i: j assigns a port, j reads m with asg(m) defined ≠ j ⇒ ¬Causal_C(j), every C",
                        gen, check, MID, 60, BOTHFAM))

    def wit(m):
        D, C = m
        R = Roles(D)
        for j in D.comps:
            if reads_assigned(R, D, j) and R.outputs_of(j) and R.causal(j, C, "R-ii"):
                return "under R-ii, %s reads a port another component assigns and is causal on C = %s\n%s" % (j, sorted(C, key=repr), D.describe(comps=[j]))
        return None

    parts.append(exists(S, "FC2.new1", 2, "R-ii: a reader of an assigned port can be causal",
                        "under R-ii: some j reading m with asg(m) ≠ j has Causal_C(j)", gen, wit, SMALL, 60, BOTHFAM))
    D = pole()
    R = Roles(D)
    C1, C2, C2s = pole_contracts(D)
    parts.append(computed("the pole's c_L (L := H cot θ, reads H and θ)", "Causal_{C2}(c_L) under R-ii and not under R-i",
                          R.causal("c_L", C2, "R-ii") and not R.causal("c_L", C2, "R-i"),
                          "R-i: %s; R-ii: %s; OBS_READING = %s" % (R.causal("c_L", C2, "R-i"), R.causal("c_L", C2, "R-ii"), OBS_READING), ["I92"]))
    return parts


@claim("FC4.new1", ["I77", "I78"])
def fc4_new1(S):
    """L127's fourth sentence in symbols (area 1 text change): m ∈ V_j, asg(m) defined ≠ j,
    Changes_C(j, A∖Slc_j) ⇒ Meas_C(j, m); under R-i with Changes_C(j, A)."""
    parts = []

    def gen(rng, size):
        D = gen_org(rng, size)
        return D, _rand_C(rng, D)

    def check(m, rd):
        D, C = m
        R = Roles(D)
        hit = False
        for j in D.comps:
            X = frozenset(D.A) - R.slc[j] if rd == "R-ii" else frozenset(D.A)
            if not R.changes(j, X, C):
                continue
            for mm in D.foot[j]:
                if mm in R.asg and R.asg[mm] != j:
                    hit = True
                    if not R.meas(j, mm, C, rd):
                        return "%s reads %s (asg = %s), changes under an edit to its relation in C, and is no measurement of it under %s\n%s" % (
                            j, mm, R.asg[mm], rd, D.describe())
        return None if hit else VAC

    for k, rd in ((1, "R-ii"), (2, "R-i")):
        parts.append(forall(S, "FC4.new1", k, "L127 in symbols, %s" % rd,
                            "m ∈ V_j ∧ asg(m) ∉ {j, undefined} ∧ Changes_C(j, %s) ⇒ Meas_C(j, m)" % ("A∖Slc_j" if rd == "R-ii" else "A"),
                            gen, lambda mdl, rd=rd: check(mdl, rd), MID, 60, BOTHFAM))
    D = pole()
    R = Roles(D)
    C1, C2, C2s = pole_contracts(D)
    parts.append(computed("the pole's C1 (settings of H, θ)", "c_L reads H and θ and has no family on C1; the formal L127 asks nothing of it there (Changes_{C1}(c_L, A) fails)",
                          not R.changes("c_L", frozenset(D.A), C1) and R.families(C1, OBS_READING) == dict(causal=["c_H", "c_T"], meas=[], rule=[]),
                          "families on C1 under %s: %s" % (OBS_READING, R.families(C1, OBS_READING)), ["I92"]))
    return parts


@claim("FC12.new1", ["I90", "I92"])
def fc12_new1(S):
    """D12.1 with I161 (second check, R1): Sel and Con exclude each other on one history, with Rep computed
    as the fixed points of (R), not tagged: the output occurrence holds t, and its holding of cod t and Sel's
    other conditions are computed from t's own faithfulness; earlier occurrences (held, trace, Sel's
    conditions) and the output's trace are Θ by hand (I90). Under U, K, T and T′ (I162)."""
    p, c = fwd_pole_cand()
    H = [(ONE, "b1_45")]

    def computed_from(cand, H_):
        held = bool(faithful(cand))
        selc = set(H_) <= set(cand.p.C) and faithful_on(cand, H_)
        return held, selc

    def histories(held_out, selc_out, nmax=3):
        for n in range(1, nmax + 1):
            for early in itertools.product(itertools.product([0, 1], repeat=3), repeat=n - 1):
                for tr_out in (0, 1):
                    yield (n, [e[0] for e in early] + [held_out], [e[1] for e in early] + [tr_out], [e[2] for e in early] + [selc_out])

    def bad(n, held, trace, selc, i161, rds):
        for rd in rds:
            for R, sc in prov_fixed_points(n, held, trace, selc, rd, i161):
                if (n - 1) in R and sc[n - 1][0] and sc[n - 1][1]:
                    return "%s: Sel and Con both hold at the output: held %s, trace %s, Sel's conditions %s; fixed point %s" % (rd, held, trace, selc, prov_show(n, [(R, sc)]))
        return None

    ho, so = computed_from(c, H)
    parts = [exhaustive("FC12.new1", "D12.1 with I161, the pole's forward transport", "¬(Sel(t) ∧ Con(t)) at every fixed point of (R), under U, K, T and T′",
                        list(histories(ho, so)), lambda m: bad(*m, True, PROV_READINGS),
                        "chains o1 ≺ … ≺ on, n ≤ 3; t held at on (computed: Faithful_C(t) %s; Sel's conditions on H = {(1,b1_45)} %s)" % (ho, so), ["I90", "I92", "I161", "I162"])]

    def gen(rng, size):
        m = gen_p_cand(rng, size)
        if m is None:
            return None
        q, cand = m
        b0 = q.b0
        return cand, [(ONE, b0)]

    def check(m):
        cand, H_ = m
        h_, s_ = computed_from(cand, H_)
        for hist in histories(h_, s_, 2):
            r = bad(*hist, True, PROV_READINGS)
            if r:
                return r + "\n" + cand.describe()
        return None

    parts.append(forall(S, "FC12.new1", 2, "D12.1 with I161, random transports", "¬(Sel(t) ∧ Con(t)) at every fixed point, t's holding and Sel's conditions computed from t, under U, K, T and T′",
                        gen, check, SMALL, 20, BOTHFAM, ["I90", "I161", "I162"], note="histories of 1–2 occurrences per transport"))
    parts.append(exhaustive("FC12.new1", "without I161 (the review's R1)", "there is a history with Sel(t) ∧ Con(t) under T or T′", list(histories(ho, so)),
                            lambda m: bad(*m, False, ("T", "T'")), "the same space as part 1", ["I90", "I92"], kind="there is"))

    tags = ["t", "H", "surv", "cod", "other"]
    items = [(T, prep) for r in range(len(tags) + 1) for T in itertools.combinations(tags, r) for prep in (False, True)]

    def check2(m):
        T, prep = m
        h = Hist(["o%d" % i for i in range(len(T))], [("o%d" % i, x) for i, x in enumerate(T)], set(p.C), admitted=True, prepares=prep)
        if sel(c, H, h, round2=True) and con(h):
            return "round 2 D12.1: Sel and Con both hold: represented %s, Prepares %s" % (T, prep)
        return None

    parts.append(exhaustive("FC12.new1", "round 2's D12.1 (no cod t exclusion), tags", "there is h with Sel(t) ∧ Con(t)", items, check2,
                            "every set of tagged items ⊆ {t, H, surv, cod, other} × Prepares", ["I90", "I92"], kind="there is"))
    return parts
