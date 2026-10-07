# S104 round 2, area 1 (L1-L228): the new claims of the area 1 checker's formal fixes.
# Ids: FC<section>.new<n>. Each is stated in "area 1 - verdicts and formal fixes.md".
import itertools

from .core import ONE, Roles, OBS_READING
from .gen import gen_org, gen_surg
from .harness import claim, forall, exists, exhaustive, computed, VAC
from .cases import pole
from .claims_a import SMALL, MID, BOTHFAM, pole_contracts
from .claims_b import Hist, sel, con, fwd_pole_cand


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
    """D12.1' (area 1): Sel and Con exclude each other on one history. Exhaustive over the tags a history's
    occurrences can represent and over Prepares."""
    p, c = fwd_pole_cand()
    H = [(ONE, "b1_45")]
    tags = ["t", "H", "surv", "cod", "other"]
    items = []
    for r in range(len(tags) + 1):
        for T in itertools.combinations(tags, r):
            for prep in (False, True):
                items.append((T, prep))

    def check(m):
        T, prep = m
        h = Hist(["o%d" % i for i in range(len(T))], [("o%d" % i, x) for i, x in enumerate(T)], set(p.C), admitted=True, prepares=prep)
        if sel(c, H, h) and con(h):
            return "Sel and Con both hold: represented %s, Prepares %s" % (T, prep)
        return None

    def check2(m):
        T, prep = m
        h = Hist(["o%d" % i for i in range(len(T))], [("o%d" % i, x) for i, x in enumerate(T)], set(p.C), admitted=True, prepares=prep)
        if sel(c, H, h, round2=True) and con(h):
            return "round 2 D12.1: Sel and Con both hold: represented %s, Prepares %s" % (T, prep)
        return None

    return [exhaustive("FC12.new1", "D12.1': exactly one of Sel, Con, Dec", "¬(Sel(t) ∧ Con(t)) on every history h", items, check,
                       "every set of represented items ⊆ {t, H, surv, cod, other} × Prepares ∈ {no, yes}; the pole's forward transport, H = {(1,b1_45)}", ["I90", "I92"]),
            exhaustive("FC12.new1", "round 2's D12.1, for comparison", "there is h with Sel(t) ∧ Con(t)", items, check2,
                       "the same space", ["I90", "I92"], kind="there is")]
