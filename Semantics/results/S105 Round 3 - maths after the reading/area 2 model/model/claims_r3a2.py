# S105 round 3, area 2 (L229-L372): new test claims, not counted as moves (rule 16).
#   FC23.new1  W3: the slot quantifier over Det_C (D6.3, I136), four readings, on the text's cases and on generated models.
#   FC25.new1  A2-T5: L269's formula (FC25 (a*)) for a table component constant in the edit, varying with the boundary.
#   FC47.new1  W5: a problem solved by a test's argument is posed again where a premise of the argument is withdrawn
#              (D10.1, D10.6 with D9.8's X^ξ_j), on the pole's forward and reversed candidates (L271, L325).
# Every input is computed from organizations and questions; the offer records (D8.3, primitives) are the only
# declared inputs.
from .core import (ONE, BOT, Org, Question, PortQuery, Candidate, Translation, account, slot, F1, SLOT_QUANTIFIERS)
from . import core
from .gen import rand_rel, gen_candidate, any_candidate
from .cases import pole, pole_fwd_candidate, pole_rev_candidate, single_settings
from .args import Not, And, Imp, Leaf, Step, Assessor, X, enumerate_args
from .harness import claim, forall, exists, computed, VAC
from .claims_a import SMALL, BOTHFAM, D_and_p, pole_contracts, area2_lookups, _org, _T


def acc_q(c, q):
    """Acc(ℰ) with D6.3's quantifier read as q."""
    old = core.SLOT_QUANTIFIER
    core.SLOT_QUANTIFIER = q
    try:
        return account(c)
    finally:
        core.SLOT_QUANTIFIER = old


def acc_row(c):
    return {q: acc_q(c, q) for q in SLOT_QUANTIFIERS}


def m5():
    """M5 (FC23 (d)): the answer fixed at each pair by one component, a different one at each pair; E = D."""
    D5 = _org("D", ["y"], {"y": (1, 2)}, ["ca", "cb"], {"ca": ["y"], "cb": ["y"]}, ["b0"], [ONE, "e"],
              {("ca", "e", "b0"): {(2,)}, ("cb", ONE, "b0"): {(1,)}})
    p5 = Question(D5, [(ONE, "b0"), ("e", "b0")], "b0", PortQuery(), "y")
    return Candidate(D5, p5, _T("y"), {ONE: ONE, "e": "e"}, {"b0": "b0"},
                     {"ca": (frozenset(["ca"]), _T("y")), "cb": (frozenset(["cb"]), _T("y"))}, ["ca", "cb"], "y", name="ℰ_M5")


def m13():
    """M13 (FC22 (b), the owner's weathervane, S41 Q15)."""
    D = _org("D", ["x", "y"], {"x": (0, 1), "y": (0, 1)}, ["cx", "cy"], {"cx": ["x"], "cy": ["x", "y"]}, ["b0"], [ONE, "e"],
             {("cx", "e", "b0"): {(1,)}, ("cy", ONE, "b0"): {(0, 0), (1, 1)}, ("cy", "e", "b0"): {(0, 0), (1, 1)}})
    p = Question(D, [(ONE, "b0"), ("e", "b0")], "b0", PortQuery(), "y")
    return Candidate(D, p, _T("x", "y"), {ONE: ONE, "e": "e"}, {"b0": "b0"},
                     {"cx": (frozenset(["cx"]), _T("x")), "cy": (frozenset(["cy"]), _T("x", "y"))}, ["cy"], "y", name="ℰ_M13")


def pole_cases():
    D = pole()
    C1, C2, _ = pole_contracts(D)
    C3 = frozenset([(ONE, "b1_45")] + [(a, "b1_45") for a in single_settings(D, ["L"])])
    out = {}
    for nm, C in (("pole C1 (settings of H, θ)", C1), ("pole C2 (C1 + settings of L)", C2), ("pole C3 (baseline + settings of L)", C3)):
        out[nm] = pole_fwd_candidate(Question(D, C, "b1_45", PortQuery(), "L", name=nm))
    return out


def pins(c, k, a, b):
    """k's relation at (τa, σb) by itself fixes δ_E to the target's determined answer there."""
    p, E, w = c.p, c.E, c.deltaE
    if w not in E.foot[k] or not c.translates(a, b):
        return False
    y = p.ans(a, b)
    if y is BOT:
        return False
    i = E.foot[k].index(w)
    return set(t[i] for t in E.L(k, c.tau[a], c.sigma[b])) == {y}


def unaltered(c, k, a, b):
    """τ(a) = 1, or τ(a) leaves k's relation at σ(b) as at the identity edit (not exempt under 'some-exempt')."""
    a2, b2 = c.tau[a], c.sigma[b]
    return a2 == ONE or c.E.L(k, a2, b2) == c.E.L(k, ONE, b2)


def gen_acc(rng, size):
    """A generated question and a candidate built from its target (the construction gen_pair uses with its
    acc bias), or any candidate; port query only (NC1 reads only a port query, I82)."""
    D, p = D_and_p(rng, size)
    if D is None or getattr(p.Q, "kind", None) != "port":
        return None
    if rng.random() < 0.7:
        c = gen_candidate(rng, p, name="ℰ", perturb_p=0.05, background_p=0.0, random_tau_p=0.0, demote_p=0.0)
    else:
        c = any_candidate(rng, p, size, name="ℰ")
    return p, c


def both(p, c):
    return "%s\n%s\n%s" % (p.describe(), p.D.describe(), c.describe())


@claim("FC23.new1", ["I77", "I78", "I81", "I82", "I79", "I136"])
def fc23new1(S):
    parts = []
    # (a) the text's cases and the round-2 models, under each reading
    cases = {}
    cases.update(pole_cases())
    cases["M5 (FC23 (d))"] = m5()
    cases["M13 (FC22 (b), S41 Q15)"] = m13()
    for nm, (c, _ans) in area2_lookups().items():
        cases[nm + " (FC23 (c))"] = c
    rows = {nm: acc_row(c) for nm, c in cases.items()}
    expect = {"pole C1 (settings of H, θ)": (True, True, True, True), "pole C2 (C1 + settings of L)": (True, False, True, True),
              "pole C3 (baseline + settings of L)": (True, False, True, True), "M5 (FC23 (d))": (True, False, False, False),
              "M13 (FC22 (b), S41 Q15)": (True, True, True, True)}
    ok = all(tuple(rows[nm][q] for q in SLOT_QUANTIFIERS) == expect[nm] for nm in expect)
    ok = ok and all(not any(rows[nm + " (FC23 (c))"].values()) for nm in area2_lookups())
    txt = "readings %s. " % (SLOT_QUANTIFIERS,) + "; ".join("%s: %s" % (nm, tuple(r[q] for q in SLOT_QUANTIFIERS)) for nm, r in rows.items())
    parts.append(computed("(a) Acc on the pole (E1) and the round-2 models under the four readings of D6.3's quantifier",
                          "pole C1 (T,T,T,T); C2 and C3 (T,F,T,T): 'some' makes the setting of L, which replaces c_L by L = l, an answer slot; "
                          "M5 (T,F,F,F); M13 (T,T,T,T); M1-M3 fail under all four", ok, txt, ["I136", "I79", "I82"]))

    # (b) W3's partial lookup, on generated models: Acc under 'every', a component fixing the answer at a determined
    # pair its own edit leaves unaltered, and not at another determined pair
    def cb(m):
        p, c = m
        if not acc_q(c, "every"):
            return None
        det = [(a, b) for (a, b) in sorted(p.C, key=repr) if p.ans(a, b) is not BOT]
        for k in c.E.comps:
            hit = [x for x in det if pins(c, k, *x) and unaltered(c, k, *x)]
            miss = [x for x in det if not pins(c, k, *x)]
            if hit and miss:
                return ("%s fixes the answer by itself at %s (its edit leaves it as at 1) and not at %s; Acc under the four readings %s\n%s"
                        % (k, hit, miss, tuple(acc_q(c, q) for q in SLOT_QUANTIFIERS), both(p, c)))
        return None

    parts.append(exists(S, "FC23.new1", 2, "(b) W3's partial lookup meets (E) under D6.3 as it stands",
                        "∃ℰ: Acc under 'every' ∧ ∃k, (a,b), (a',b') ∈ Det_C: k fixes δ_E to Ans_p at (a,b), τ(a) leaves k as at 1 there, and not at (a',b')",
                        gen_acc, cb, SMALL, 200, BOTHFAM, ["I136"]))

    # (c) W3's reading on generated models: a candidate meeting (E) under 'every' and the exempt readings fails under 'some'
    def cc(m):
        p, c = m
        r = acc_row(c)
        if r["every"] and r["some-exempt"] and r["some-exempt-set"] and not r["some"]:
            ks = [k for k in c.E.comps if slot(c, k, quantifier="some")]
            return "Acc %s; slots under 'some' only: %s\n%s" % (tuple(r[q] for q in SLOT_QUANTIFIERS), ks, both(p, c))
        return None

    parts.append(exists(S, "FC23.new1", 3, "(c) 'some' excludes a candidate the other readings keep",
                        "∃ℰ: Acc under 'every', 'some-exempt', 'some-exempt-set' ∧ ¬Acc under 'some'", gen_acc, cc, SMALL, 200, BOTHFAM, ["I136"]))

    # (d) the exempt reading is not stronger than 'every': the answer supplied by the contract's own edits at every determined pair
    def cd(m):
        p, c = m
        r = acc_row(c)
        if r["some-exempt"] and not r["every"]:
            ks = [k for k in c.E.comps if slot(c, k, quantifier="every")]
            return "Acc %s; slots under 'every': %s\n%s" % (tuple(r[q] for q in SLOT_QUANTIFIERS), ks, both(p, c))
        return None

    parts.append(exists(S, "FC23.new1", 4, "(d) 'some-exempt' keeps a candidate 'every' excludes",
                        "∃ℰ: Acc under 'some-exempt' ∧ ¬Acc under 'every'", gen_acc, cd, SMALL, 200, BOTHFAM, ["I136"]))

    # (e) 'some' is the strongest reading
    def ce(m):
        p, c = m
        r = acc_row(c)
        if r["some"] and not all(r.values()):
            return "Acc %s\n%s" % (tuple(r[q] for q in SLOT_QUANTIFIERS), both(p, c))
        return None

    parts.append(forall(S, "FC23.new1", 5, "(e) 'some' implies the other three", "Acc under 'some' ⇒ Acc under 'every', 'some-exempt', 'some-exempt-set'",
                        gen_acc, ce, SMALL, 60, BOTHFAM, ["I136"]))

    # (f) the exemption's two extents (R3A2-02): an edit that alters k without setting δ_E through k alone
    def cf(m):
        p, c = m
        r = acc_row(c)
        if r["some-exempt"] != r["some-exempt-set"]:
            return "Acc %s\n%s" % (tuple(r[q] for q in SLOT_QUANTIFIERS), both(p, c))
        return None

    parts.append(exists(S, "FC23.new1", 6, "(f) the exemption's two extents differ",
                        "∃ℰ: Acc under 'some-exempt' ≠ Acc under 'some-exempt-set'", gen_acc, cf, SMALL, 200, BOTHFAM, ["I136"]))

    # (g) the eliminative construction (L339, FC62) under the four readings: FC62's encoding, whose background
    # component 'rest' is the constant e = 0 at the baseline, and a second encoding whose baseline e = 0 comes from two
    # components (h_u: u = 1; rest: e = 1 - u), with the same answers, the same edit a_x and the same commitment k (λ(k) = {x})
    def elim(rest_base):
        fu = {(0, 0), (0, 1), (1, 0), (1, 1)}
        foot_rest = ("e",) if rest_base == "const" else ("u", "e")
        base = {(0,)} if rest_base == "const" else {(0, 1), (1, 0)}
        full_rest = {(0,), (1,)} if rest_base == "const" else fu
        D = Org("D_elim" + ("" if rest_base == "const" else "2"), ["u", "e"], {"u": (0, 1), "e": (0, 1)}, ["h_u", "x", "rest"],
                {"h_u": ("u",), "x": ("u", "e"), "rest": foot_rest}, ["b0"], [ONE, "a_x"], lambda a2, a1: None,
                lambda j, a, b: {"h_u": {(1,)}, "x": (fu if a == ONE else {(0, 0), (1, 1)}), "rest": (base if a == ONE else full_rest)}[j])
        p = Question(D, [(ONE, "b0"), ("a_x", "b0")], "b0", PortQuery(), "e", name="p_noX")
        lam = {"k": (frozenset(["x"]), _T("u", "e")), "k_u": (frozenset(["h_u"]), _T("u")), "k_rest": (frozenset(["rest"]), _T(*foot_rest))}
        E = Org("E_elim", ["u", "e"], D.dom, ["k_u", "k", "k_rest"], {"k_u": ("u",), "k": ("u", "e"), "k_rest": foot_rest}, ["b0"], [ONE, "a_x"],
                lambda a2, a1: None, lambda j, a, b: D.L({"k_u": "h_u", "k": "x", "k_rest": "rest"}[j], a, b))
        return p, Candidate(E, p, _T("u", "e"), {ONE: ONE, "a_x": "a_x"}, {"b0": "b0"}, lam, ["k"], "e", name="ℰ_elim")

    (p1, c1), (p2, c2) = elim("const"), elim("two")
    r1, r2 = acc_row(c1), acc_row(c2)
    same_ans = (p1.ans(ONE, "b0"), p1.ans("a_x", "b0")) == (p2.ans(ONE, "b0"), p2.ans("a_x", "b0")) == (0, 1)
    parts.append(computed("(g) the eliminative construction (L339) under the four readings",
                          "FC62's encoding (rest: e = 0 at the baseline): Acc (T,F,F,F); the second encoding (rest: e = 1 − u, h_u: u = 1): Acc (T,T,T,T); answers 0 at the baseline, 1 at a_x in both",
                          same_ans and tuple(r1[q] for q in SLOT_QUANTIFIERS) == (True, False, False, False) and all(r2.values()),
                          "FC62's encoding: %s; second encoding: %s; slots of FC62's encoding under 'some-exempt': %s\n%s\n%s"
                          % (tuple(r1[q] for q in SLOT_QUANTIFIERS), tuple(r2[q] for q in SLOT_QUANTIFIERS),
                             [k for k in c1.E.comps if slot(c1, k, quantifier="some-exempt")], p2.D.describe(), c2.describe()),
                          ["I136", "I03", "I78"]))
    return parts


@claim("FC25.new1", ["I77", "I78", "I80", "I101", "I138"])
def fc25new1(S):
    """L269 (A2-T5): a table component k whose relation is constant in the edit (it may vary with the boundary):
    (1,b), (a,b) ∈ C ∧ proj^λ_{V_k}Sol_{λ(k)}(a,b) ≠ proj^λ_{V_k}Sol_{λ(k)}(1,b) ⇒ ¬F1."""
    def gen(rng, size):
        D, p = D_and_p(rng, size, family="G-surg")
        if D is None:
            return None
        U = [v for v in D.ports if rng.random() < 0.7] or [p.deltaD]
        rel = {}
        for b in D.B:
            full = frozenset(__import__("itertools").product(*[D.dom[v] for v in U]))
            rel[b] = D.proj(D.sol(ONE, b), D.ports, U) if rng.random() < 0.6 else rand_rel(rng, full, 0.5)
        E = Org("E_tabB", U, {v: D.dom[v] for v in U}, ["tab"], {"tab": tuple(U)}, D.B, D.A, D._compose, lambda j, a, b: rel[b])
        lam = {"tab": (frozenset(D.comps), {v: Translation((v,)) for v in U})}
        c = Candidate(E, p, {v: Translation((v,)) for v in U}, {a: a for a in D.A}, {b: b for b in D.B}, lam, ["tab"],
                      p.deltaD if p.deltaD in U else U[0], name="ℰ_tabB")
        return p, c

    def check(m):
        p, c = m
        D = p.D
        hyp = [(a, b) for (a, b) in p.C if a != ONE and (ONE, b) in p.C
               and D.proj(D.sol(a, b), D.ports, c.E.ports) != D.proj(D.sol(ONE, b), D.ports, c.E.ports)]
        if not hyp:
            return VAC
        if F1(c):
            return "the projection moves at %s and the table meets (F1)\n%s" % (hyp, both(p, c))
        return None

    return [forall(S, "FC25.new1", 1, "(a*) for a table constant in the edit",
                   "L_k(τa,σb) = L_k(1,σb) ∀a,b ∧ (1,b),(a,b) ∈ C ∧ proj(a,b) ≠ proj(1,b) ⇒ ¬F1_C", gen, check, SMALL, 60, ["G-surg"], ["I101", "I138"])]


@claim("FC47.new1", ["I87", "I88", "I89", "I140", "I141", "I166"])
def fc47new1(S):
    """D10.6 'solved while Out_j' and D10.1 at two places ξ, ξ' (D9.8's X^ξ_j; Accepted_j(ξ) a declared input, D9.4)."""
    D = pole()
    C1, _, _ = pole_contracts(D)
    p = Question(D, C1, "b1_45", PortQuery(), "L", name="p_prod")
    fwd, rev = pole_fwd_candidate(p), pole_rev_candidate(p)
    # Conf by D8.2's first disjunct (answers differ); the second disjunct's enumeration of every relation assignment
    # is too large on the pole and is not needed for a conflict in C (kind i, D10.2)
    cps = [x for x in sorted(C1, key=repr) if fwd.ans_E(fwd.tau[x[0]], fwd.sigma[x[1]]) != rev.ans_E(rev.tau[x[0]], rev.sigma[x[1]])]
    kind = "i" if any(x in C1 for x in cps) else None
    a, b = cps[0]
    y = p.ans(a, b)
    # which candidate's answer differs from the recorded answer: computed
    bad = [c for c in (fwd, rev) if c.ans_E(c.tau[a], c.sigma[b]) != y]
    rec, bg = "rec", "bg"                              # rec: 'Ans_p(a,b) = y' (the test's record); bg: its background premise (K3)
    ab, acc = "A_ab_bad", "acc_bad"                     # A at (a,b) for the candidate whose answer differs; Acc(that candidate)
    acc_good = "acc_good"                               # Acc(the other candidate): no premise speaks of it
    prem = [rec, bg, Imp(And(rec, bg), Not(ab)), Imp(acc, ab)]
    # X_j over a finite set of arguments [I88]: every argument of height ≤ 2 over the premises (the premises alone
    # among them, S41 Q23), and the test's argument α of height 3: AndI(rec, bg); MP to ¬A_ab; MT to ¬Acc.
    s0 = Step("AndI", And(rec, bg), [Leaf(rec, "record"), Leaf(bg)])
    s1 = Step("MP", Not(ab), [s0, Leaf(Imp(And(rec, bg), Not(ab)))])
    alpha = Step("MT", Not(acc), [s1, Leaf(Imp(acc, ab))])
    args = enumerate_args(prem, forms=("MP", "MT", "AndI"), depth=2, max_args=300) + [alpha]
    forms = ["MP", "MT", "AndI"]
    j_xi = Assessor(forms, prem)                        # at ξ: every premise taken up
    j_xi2 = Assessor(forms, [x for x in prem if x != bg])  # at ξ': the background premise withdrawn
    j_xi3 = Assessor(forms, prem)                       # at ξ'': taken up again
    riv = True                                          # Off(ℰ,p) ∧ Off(ℰ',p) ∧ Offered: the declared offer records (D8.3, I33)
    rows = []
    res = {}
    for nm, j in (("ξ", j_xi), ("ξ'", j_xi2), ("ξ''", j_xi3)):
        out_bad = bool(X(j, acc, args))
        out_good = bool(X(j, acc_good, args))
        prob = riv and bool(cps) and not out_bad and not out_good
        solved = out_bad or out_good
        res[nm] = (solved, prob)
        rows.append("%s: |X_j(Acc(%s))| = %d; Solved %s; Prob_j %s" % (nm, bad[0].name, len(X(j, acc, args)), solved, prob))
    ok = len(bad) == 1 and kind == "i" and res["ξ"] == (True, False) and res["ξ'"] == (False, True) and res["ξ''"] == (True, False)
    return [computed("the pole, forward against reversed on C1: solved at ξ, posed again at ξ', solved at ξ''",
                     "Conf at a pair of C1 (kind i, computed); the test's argument rules out the candidate whose answer differs "
                     "while its background premise is in Accepted_j; where the premise is withdrawn D10.6 gives not solved and D10.1 gives the problem again",
                     ok, "conflict pairs in C1: %d (first %s, target answer %s, %s answers %s, %s answers %s); kind %s; %d arguments. %s"
                     % (len(cps), (a, b), y, fwd.name, fwd.ans_E(a, b), rev.name, rev.ans_E(a, b), kind, len(args), "; ".join(rows)),
                     ["I140", "I141", "I166", "I33"])]
