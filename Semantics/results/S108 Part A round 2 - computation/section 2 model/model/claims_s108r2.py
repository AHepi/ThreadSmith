# S108 Part A round 2, section 2 (the computing agent, rule 5): R2V2.11, two claims beside FC21, proposed by the reply
# (results/S108 Part A round 2 - returns/s108r2_glm_section2.response.txt) to close the suite's blind spots e2.38 (no claim
# separates D6.4 from round 1's V2.2) and e2.39 (none separates it from V2.1). Registered only when S108R2_S2_VARIANT is
# R2V2.11, so that with the switch off the suite is the suite after round 4, claim for claim. A copy: no theory text changed.
#   FC21.v1  the reply's "∃ℰ: F1 ∧ F2 ∧ A ∧ NonVacuous ∧ Contrast at some (a,b) ∈ C ∧ no ∅ ≠ G ⊆ Γ with Lost" is read, as the
#            reply's trace uses it ("holds under D6.4's negation and fails under D6.4"), with (E) in place of its first four
#            conjuncts, and written as its negation, a claim that holds under D6.4 (P-R2S2-5): every candidate meeting (E) has
#            a pair of C with a contrast that a nonempty block of Γ loses. Under V2.1 its counterexamples are the candidates
#            whose contrast no block carries.
#   FC21.v2  ∃ℰ meeting (E) with S_{E,p} = {{a},{b},{a,b}} on Γ = {a,b} (L307.s1's redundancy realized by a candidate).
from . import core
from .core import ONE, Org, Question, PortQuery, Candidate, Translation, account, contrast, lost, routes
from .harness import claim, forall, exists, computed, VAC
from .claims_a import SMALL, BOTHFAM, gen_p_cand


def block_carries_contrast(c):
    """∃(a,b) ∈ C, ∅ ≠ G ⊆ Γ: Contrast(E; x) ∧ Lost(E, G; x) (D6.4 as after round 4), computed here directly, not
    through core.NC2 (which round 1's switch varies)."""
    p = c.p
    x0 = (ONE, c.sigma[p.b0])
    a0 = c.ans_E(*x0)
    blocks = [G for G in core.powerset(c.Gamma) if G]
    for (a, b) in sorted(p.C, key=repr):
        x = (c.tau[a], c.sigma[b])
        if contrast(c.ans_E(*x), a0) and any(lost(c, G, x, x0) for G in blocks):
            return True
    return False


def v21_case():
    """Round 1's V2.1 case (the reply of round 1, built in round 1's s108_s2_cases.py): ports x, y, z; cx:(x), cy:(x,y),
    dz:(z); edit e sets x = 1; y = x; Q_w reads y; ℰ = D, identity transport, Γ = {dz} (a commitment on z alone)."""
    rel = {("cx", "e", "b0"): {(1,)}}
    for a in (ONE, "e"):
        rel[("cy", a, "b0")] = {(0, 0), (1, 1)}
    box = {}

    def L(j, a, b):
        return frozenset(rel[(j, a, b)]) if (j, a, b) in rel else box["D"].full(j)
    D = Org("D_v21", ["x", "y", "z"], {"x": (0, 1), "y": (0, 1), "z": (0, 1)}, ["cx", "cy", "dz"],
            {"cx": ("x",), "cy": ("x", "y"), "dz": ("z",)}, ["b0"], [ONE, "e"], lambda a2, a1: None, L)
    box["D"] = D
    p = Question(D, [(ONE, "b0"), ("e", "b0")], "b0", PortQuery(), "y", name="p_v21")
    lam = {"dz": (frozenset(["dz"]), {"z": Translation(("z",))})}
    return Candidate(D, p, {v: Translation((v,)) for v in D.ports}, {ONE: ONE, "e": "e"}, {"b0": "b0"}, lam, ["dz"], "y", name="ℰ_v21")


def l307_case():
    """L307's redundancy as a candidate (round 1, P-S2-5): target x an input (edit e sets x = 1), y = x; Γ = {a, b}, both
    y = x, each alone a route."""
    def Ld(j, a, b):
        if j == "c_x":
            return frozenset([(1,)]) if a == "e" else frozenset([(0,)])
        return frozenset([(0, 0), (1, 1)])
    D = Org("D_xy", ["x", "y"], {"x": (0, 1), "y": (0, 1)}, ["c_x", "c_y"], {"c_x": ("x",), "c_y": ("x", "y")}, ["b0"], [ONE, "e"],
            lambda a2, a1: None, Ld)
    p = Question(D, [(ONE, "b0"), ("e", "b0")], "b0", PortQuery(), "y", name="p_xy")

    def Le(j, a, b):
        return Ld(j, a, b) if j == "c_x" else frozenset([(0, 0), (1, 1)])
    E = Org("E_redundant", ["x", "y"], {"x": (0, 1), "y": (0, 1)}, ["c_x", "a", "b"], {"c_x": ("x",), "a": ("x", "y"), "b": ("x", "y")},
            ["b0"], [ONE, "e"], lambda a2, a1: None, Le)
    T = {"x": Translation(("x",)), "y": Translation(("y",))}
    lam = {"c_x": (frozenset(["c_x"]), {"x": Translation(("x",))}), "a": (frozenset(["c_y"]), T), "b": (frozenset(["c_y"]), T)}
    return Candidate(E, p, {v: Translation((v,)) for v in E.ports}, {ONE: ONE, "e": "e"}, {"b0": "b0"}, lam, ["a", "b"], "y", name="ℰ_L307")


L307_S = frozenset([frozenset(["a"]), frozenset(["b"]), frozenset(["a", "b"])])


def fmt_S(S):
    return "{" + ", ".join("{" + ",".join(sorted(W)) + "}" for W in sorted(S, key=lambda W: (len(W), sorted(W)))) + "}"


if core.S2R2 == "R2V2.11":

    @claim("FC21.v1", ["I77", "I78", "I81"])
    def fc21_v1(S):
        parts = []
        c = v21_case()
        acc = account(c)
        parts.append(computed("(a) round 1's V2.1 case: a commitment that carries no contrast", "ℰ_v21 (Γ = {dz}: the contrast at (e,b0) is carried by the background, not by Γ) does not meet (E)",
                              not acc, "Acc %s; a nonempty block of Γ losing a contrast at a pair of C: %s; Ans_E (1,b0) %r, (e,b0) %r"
                              % (acc, block_carries_contrast(c), c.ans_E(ONE, "b0"), c.ans_E("e", "b0"))))

        def check(m):
            p, cand = m
            if not account(cand):
                return VAC
            if not block_carries_contrast(cand):
                return "a candidate meets (E) and no nonempty block of Γ loses a contrast at a pair of C\n%s\n%s\n%s" % (p.describe(), p.D.describe(), cand.describe())
            return None

        parts.append(forall(S, "FC21.v1", 2, "(b) every candidate meeting (E) has a contrast a block of Γ carries",
                            "Acc(ℰ) ⇒ ∃(a,b) ∈ C, ∅ ≠ G ⊆ Γ: Contrast(E;x) ∧ Lost(E,G;x) (the negation of the reply's FC21.v1)",
                            gen_p_cand, check, SMALL, 40, BOTHFAM))
        return parts

    @claim("FC21.v2", ["I77", "I78", "I81"])
    def fc21_v2(S):
        parts = []
        c = l307_case()
        acc, S_ = account(c), routes(c)
        parts.append(computed("(a) L307's redundancy built as a candidate", "ℰ_L307 (Γ = {a, b}, both y = x) meets (E) with S = {{a},{b},{a,b}}",
                              bool(acc) and S_ == L307_S, "Acc %s; S = %s" % (acc, fmt_S(S_))))

        def check(m):
            p, cand = m
            if len(cand.Gamma) != 2 or not account(cand):
                return None
            a, b = cand.Gamma
            if routes(cand) == frozenset([frozenset([a]), frozenset([b]), frozenset([a, b])]):
                return "S = {{%s},{%s},{%s,%s}}\n%s\n%s\n%s" % (a, b, a, b, p.describe(), p.D.describe(), cand.describe())
            return None

        parts.append(exists(S, "FC21.v2", 2, "(b) a generated candidate realizing L307's S", "∃ℰ meeting (E), Γ = {a,b}, S_{E,p} = {{a},{b},{a,b}}",
                            gen_p_cand, check, SMALL, 40, BOTHFAM))
        return parts
