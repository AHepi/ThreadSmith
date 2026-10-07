# S107 round 4, area 3: a new test claim (not a move, rule 16).
#   FC72.new2  K1, the winter-myth knock-on (the addendum to the reading rule): S106-T8 and T10 deleted, at L317 and
#              L397, the clause that finding by argument that a candidate assumes its own answer rules it out. What the
#              theory now says of the myth about winter (file 93's first choice, file 96's second question), computed.
# The seasons and the myth are encoded as R4A3-02 records: the noon sun's height and the temperature where the question
# is asked; the hemisphere a boundary (N, the Greeks'; S); the time of year an edit (1 = June, dec = December). The tilt
# gives the sun's height by hemisphere and month; the myth gives the same seasons everywhere at once. Every value below
# is computed by core.account, core.slot, core.pins, core.conflict_pairs, core.problem_kind and args (usable, rules_out,
# X); the assessors' premises are declared inputs (L522), each built from a computed value. Nothing here orders
# candidates, counts questions or grades (S20, S23); what makes the myth a bad explanation is parked (P8).
from .core import ONE, Question, PortQuery, Candidate, Translation, account, slot, NC1, pins, conflict_pairs, problem_kind, rivals
from .args import Not, And, Imp, Leaf, Step, Assessor, usable, rules_out, X, enumerate_args
from .harness import claim, computed
from .claims_s106 import _org, _ident_lam, acc_r3_row, acc_s106_row, _tf
from .claims_a import _T

SUN = {("1", "N"): "high", ("dec", "N"): "low", ("1", "S"): "low", ("dec", "S"): "high"}  # the tilt (R4A3-02)
TEMP_REL = {("high", "warm"), ("low", "cold")}
GREEKS = [(ONE, "N"), ("dec", "N")]
EVERY_PAIR = [(a, b) for a in (ONE, "dec") for b in ("N", "S")]


def _k(a):
    return "1" if a == ONE else a


def seasons_target():
    rel = {}
    for a in (ONE, "dec"):
        for b in ("N", "S"):
            rel[("c_sun", a, b)] = {(SUN[(_k(a), b)],)}
            rel[("c_temp", a, b)] = TEMP_REL
    return _org("D_seasons", ["sun", "temp"], {"sun": ("high", "low"), "temp": ("warm", "cold")}, ["c_sun", "c_temp"],
                {"c_sun": ("sun",), "c_temp": ("sun", "temp")}, ["N", "S"], [ONE, "dec"], rel)


def seasons_question(C, name, D=None):
    return Question(D or seasons_target(), C, "N", PortQuery(), "temp", name=name)


def tilt(p):
    return Candidate(p.D, p, _T("sun", "temp"), {ONE: ONE, "dec": "dec"}, {"N": "N", "S": "S"}, _ident_lam(p.D),
                     ["c_sun", "c_temp"], "temp", name="ℰ_tilt")


def myth_written(p):
    """The myth with its answer written in: one part, 'the bargain', giving warm in June and cold in December, in
    both hemispheres alike (the whole world is cold at once)."""
    rel = {("bargain", a, b): {("warm" if a == ONE else "cold",)} for a in (ONE, "dec") for b in ("N", "S")}
    E = _org("E_myth_written", ["temp"], {"temp": ("warm", "cold")}, ["bargain"], {"bargain": ("temp",)}, ["N", "S"], [ONE, "dec"], rel)
    return Candidate(E, p, _T("temp"), {ONE: ONE, "dec": "dec"}, {"N": "N", "S": "S"},
                     {"bargain": (frozenset(["c_sun", "c_temp"]), _T("temp"))}, ["bargain"], "temp", name="ℰ_myth1")


def myth_told(p):
    """The myth as told, two parts: the bargain puts Persephone above in June and below in December, in both
    hemispheres alike; Demeter's grief makes it cold while she is below. π reads her place off the sun's height."""
    place = Translation(("sun",), lambda xs: {"high": "above", "low": "below"}[xs[0]], name="place(sun)")
    rel = {}
    for a in (ONE, "dec"):
        for b in ("N", "S"):
            rel[("bargain", a, b)] = {("above" if a == ONE else "below",)}
            rel[("grief", a, b)] = {("above", "warm"), ("below", "cold")}
    E = _org("E_myth_told", ["pers", "temp"], {"pers": ("above", "below"), "temp": ("warm", "cold")}, ["bargain", "grief"],
             {"bargain": ("pers",), "grief": ("pers", "temp")}, ["N", "S"], [ONE, "dec"], rel)
    return Candidate(E, p, {"pers": place, "temp": Translation(("temp",))}, {ONE: ONE, "dec": "dec"}, {"N": "N", "S": "S"},
                     {"bargain": (frozenset(["c_sun"]), {"pers": place}),
                      "grief": (frozenset(["c_temp"]), {"pers": place, "temp": Translation(("temp",))})},
                     ["bargain", "grief"], "temp", name="ℰ_myth2")


def _slots(c):
    return [k for k in c.E.comps if slot(c, k, quantifier="every")]


def _out(j, phi, premises):
    """X_j(φ) ≠ ∅ over every argument of height ≤ 2 from the premises j accepts (D9.8; I88)."""
    return bool(X(j, phi, enumerate_args(premises, depth=2)))


@claim("FC72.new2", ["R4A3-02"])
def fc72_new2(S):
    parts = []
    D = seasons_target()
    pG = seasons_question(GREEKS, "p_Greeks", D)
    pF = seasons_question(EVERY_PAIR, "p_finer", D)
    tG, m1, m2 = tilt(pG), myth_written(pG), myth_told(pG)
    # (a) what (E) says of each on the Greeks' question, after S106 and under round 3's (E)
    row = {}
    for c in (tG, m1, m2):
        v, d = account(c, detail=True)
        row[c.name] = (v, d, _slots(c), pins(c), acc_s106_row(c), acc_r3_row(c))
    ok_a = (row["ℰ_tilt"][0] and not row["ℰ_tilt"][2] and row["ℰ_myth1"][0] and row["ℰ_myth1"][2] == ["bargain"]
            and all(row["ℰ_myth1"][4].values()) and not any(row["ℰ_myth1"][5].values())
            and row["ℰ_myth2"][0] and not row["ℰ_myth2"][2] and all(row["ℰ_myth2"][5].values())
            and pG.ans(ONE, "N") == "warm" and pG.ans("dec", "N") == "cold")
    parts.append(computed("(a) K1: the myth on the Greeks' question, after S106",
                          "on the Greeks' contract (June and December in the north) the tilt meets (E); the myth with its answer written in (one part, a slot) meets (E) after S106 "
                          "and failed round 3's (E) under every reading; the myth as told (two parts) has no slot under 'every' and meets (E) under both",
                          ok_a, "answers: June %r, December %r (north)\n%s" % (pG.ans(ONE, "N"), pG.ans("dec", "N"), "\n".join(
                              "%s: (E) %s; conjuncts %s; slots (every) %s; pins %s; after S106 %s, round 3's (E) %s (every, some, some-exempt, some-exempt-set)"
                              % (n, r[0], {k: r[1][k] for k in ("F1", "F2", "A", "Dep", "NonVacuous", "NC1")}, r[2], r[3], _tf(r[4]), _tf(r[5])) for n, r in row.items())),
                          ["R4A3-02"]))
    # (b) the tilt and the myth offered one in place of the other on the Greeks' question (Offered: a declared record, I33)
    rb = {}
    for m in (m1, m2):
        cps = conflict_pairs(tG, m)
        rb[m.name] = (cps, rivals(tG, m), problem_kind(tG, m))
    ok_b = all(set(v[0]) == {(ONE, "S"), ("dec", "S")} and v[1] and v[2] == "ii" for v in rb.values())
    parts.append(computed("(b) the tilt against the myth, one offered in place of the other",
                          "they conflict only in the south, outside the Greeks' contract: rivals, and for an assessor who rules out neither a problem of the second kind, "
                          "each easy to vary against the other (D10.2, D10.4); for either encoding of the myth",
                          ok_b, "; ".join("tilt against %s: conflict pairs %s; rivals %s; kind %s" % (n, v[0], v[1], v[2]) for n, v in rb.items()),
                          ["R4A3-02", "I33"]))
    # (c) arguments with no test (L397, D9.6–D9.8): the finding that the myth has its answer written in, taken up
    slot1 = bool(_slots(m1))
    acc1 = account(m1)
    fnd = "Slot_myth1" if slot1 else Not("Slot_myth1")  # the finding by examining the myth, as computed
    ground = Imp("Slot_myth1", Not("Acc_myth1"))  # the clause S106-T8, T10 deleted, taken as given
    j0 = Assessor(["MP", "MT", "AndI", "AndE"], [fnd])
    j1 = Assessor(["MP", "MT", "AndI", "AndE"], [fnd, ground])
    j2 = Assessor(["MP", "MT", "AndI", "AndE"], [And(fnd, Not("Acc_myth1"))])
    out0 = (_out(j0, "Acc_myth1", [fnd]), _out(j0, "Acc_tilt", [fnd]))
    out1 = (_out(j1, "Acc_myth1", [fnd, ground]), _out(j1, "Acc_tilt", [fnd, ground]))
    out2 = _out(j2, "Acc_myth1", [And(fnd, Not("Acc_myth1"))])
    alpha1 = Step("MP", Not("Acc_myth1"), [Leaf(fnd), Leaf(ground)])
    alpha2 = Step("AndE", Not("Acc_myth1"), [Leaf(And(fnd, Not("Acc_myth1")))])
    prob = {nm: rb["ℰ_myth1"][1] and not o[0] and not o[1] for nm, o in (("j0", out0), ("j1", out1))}
    ok_c = (slot1 and acc1 and out0 == (False, False) and out1 == (True, False) and not out2
            and usable(j1, alpha1) and rules_out(alpha1, "Acc_myth1") and usable(j2, alpha2) and not rules_out(alpha2, "Acc_myth1")
            and prob == {"j0": True, "j1": False})
    parts.append(computed("(c) the finding rules nothing out by itself; taking a ground as given is the person's choice",
                          "j0 takes up the finding (the myth has its answer written in: Slot, computed): no argument usable by j0 rules out that the myth meets (E), "
                          "so the problem stands for j0; j1 also takes as given 'a candidate with its answer written in fails (E)', which (E) does not give "
                          "(the myth has a slot and meets (E)): j1's argument rules the myth out for j1, not blocked (its premise is not the denial), the ruling out j1's choice (L397, S28), "
                          "and for j1 there is no problem; j2 holds the denial among its premises: blocked (D9.7), nothing ruled out",
                          ok_c, "computed: Slot(ℰ_myth1) %s, Acc(ℰ_myth1) %s. Ruled out (myth, tilt): j0 %s, j1 %s; j2 (myth) %s. Problem (kind ii) for j0 %s, for j1 %s.\n"
                          "j1's argument:\n%s\nusable %s, rules out Acc(ℰ_myth1) %s\nj2's argument:\n%s\nusable %s, rules out Acc(ℰ_myth1) %s"
                          % (slot1, acc1, out0, out1, out2, prob["j0"], prob["j1"], alpha1.show(2), usable(j1, alpha1), rules_out(alpha1, "Acc_myth1"),
                             alpha2.show(2), usable(j2, alpha2), rules_out(alpha2, "Acc_myth1")), ["R4A3-02", "I87", "I88", "I166"]))
    # (d) the finer question (the south in): a problem of the first kind, which a record decides for whoever can use it
    tF, mF = tilt(pF), myth_written(pF)
    vF_t, dF_t = account(tF, detail=True)
    vF_m, dF_m = account(mF, detail=True)
    kind_F = problem_kind(tF, mF)
    x = (ONE, "S")
    y_rec = pF.ans(*x)  # what the target gives there; recording it is a test (L317, D10.3)
    rec = "rec_june_south_%s" % y_rec
    links = [Imp(rec, Not("Acc_%s_F" % c.name)) for c in (tF, mF) if c.ans_E(c.tau[x[0]], c.sigma[x[1]]) != y_rec]  # (A) fails there
    j3 = Assessor(["MP"], [rec] + links)
    prem3 = [rec] + links
    out3 = (_out(j3, "Acc_ℰ_myth1_F", prem3), _out(j3, "Acc_ℰ_tilt_F", prem3))
    ok_d = vF_t and not vF_m and kind_F == "i" and out3 == (True, False)
    parts.append(computed("(d) the finer question: a test decides",
                          "with the south in the contract the myth fails (E) and the tilt meets it; they conflict inside the contract (a problem of the first kind); "
                          "a record of June in the south rules out the myth, not the tilt, for an assessor who takes it and (A)'s premise up (L317, K2, K3)",
                          ok_d, "on the finer contract: tilt (E) %s; myth (E) %s, conjuncts %s; kind %s; June in the south, the target gives %r, the tilt %r, the myth %r; "
                          "ruled out for j3 (myth, tilt): %s" % (vF_t, vF_m, {k: dF_m[k] for k in ("F1", "F2", "A", "Dep", "NonVacuous")}, kind_F, y_rec,
                                                                tF.ans_E(ONE, "S"), mF.ans_E(ONE, "S"), out3), ["R4A3-02"]))
    return parts
