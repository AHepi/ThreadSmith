# S106 (decisions S44, S45): the written-in test taken out of (E). New test claims (not moves, rule 16 of round 3):
#   FC23.new2  the owner's shop sign (S44): an explanation under (E) after S106; S41 (Q2) kept for it.
#   FC23.new3  Pin (D6.3's clause at one pair) on generated models and on the pole.
#   FC25.new2  L269's encoding table meets (E) where its answer varies (its one component a slot).
# Every value is computed by core.account, core.slot, core.pin and, for FC23.new2 (f), by claims_s41's provenance_of,
# expl_ruled_out and suff_defeats, as FC30.new1 computes them. Nothing here orders candidates, counts questions or grades
# (S20, S23); what hard to vary covers is parked.
# S106, second checker on the critical review: D6.11 withdrawn (objection 1): the further question at a part and
# LeavesOpen (I185, I186) are deleted and parked (P8), with FC23.new2 (c), (d), (e), FC23.new3 (b), (c) and (d)'s
# LeavesOpen clause; sign_plus (D⁺, p^r) and read_off with them; letters of the parts kept. FC23.new2 (f) is computed
# and (g) is a look (objection 3).
import inspect

from .core import (ONE, BOT, Org, Question, PortQuery, Candidate, Translation, account, slot, NC1, NC2,
                   pin, pins, SLOT_QUANTIFIERS)
from .harness import claim, forall, exists, computed, look, VAC
from .gen import gen_candidate, any_candidate, gen_lookup
from .cases import pole, pole_fwd_candidate, single_settings
from .claims_a import SMALL, BOTHFAM, D_and_p, pole_contracts, table_candidate, _T
from .claims_s41 import provenance_of, suff_defeats, expl_ruled_out, expl_ok, SUFF_READINGS
from .args import Assessor, Imp, Not

COLOURS = ("red", "blue", "green")


def _org(name, ports, dom, comps, foot, B, A_, rel, compose=None):
    """rel: (j, a, b) -> relation; missing -> the full relation."""
    box = {}

    def Lfun(j, a, b):
        if (j, a, b) in rel:
            return frozenset(rel[(j, a, b)])
        return box["o"].full(j)
    box["o"] = Org(name, ports, dom, comps, foot, B, A_, compose or (lambda a2, a1: None), Lfun)
    return box["o"]


def _ident_lam(E):
    return {k: (frozenset([k]), _T(*E.foot[k])) for k in E.comps}


def sign_target():
    """The owner's shop sign (S44) as the question takes it: red on Mondays (the baseline 1), blue on Tuesdays (the
    edit tue); its red part r gives red on Mondays and is off (the full relation) on Tuesdays; its blue part u the
    reverse [I189]."""
    return _org("D_sign", ["colour"], {"colour": COLOURS}, ["r", "u"], {"r": ("colour",), "u": ("colour",)}, ["b0"], [ONE, "tue"],
                {("r", ONE, "b0"): {("red",)}, ("u", "tue", "b0"): {("blue",)}})


def sign_question(D=None):
    D = D or sign_target()
    return Question(D, [(ONE, "b0"), ("tue", "b0")], "b0", PortQuery(), "colour", name="p_sign")


def sign_two(p=None):
    """ℰ_two: 'a red part that switches on on Mondays and a blue part that switches on on Tuesdays' (S44)."""
    p = p or sign_question()
    E = p.D
    return Candidate(E, p, _T("colour"), {ONE: ONE, "tue": "tue"}, {"b0": "b0"}, _ident_lam(E), ["r", "u"], "colour", name="ℰ_two")


def sign_one(p=None):
    """ℰ_one: one part giving red on Mondays and blue on Tuesdays (the lookup; R3-Q1's side 1 counts it written in)."""
    p = p or sign_question()
    E = _org("E_one", ["colour"], {"colour": COLOURS}, ["k"], {"k": ("colour",)}, ["b0"], [ONE, "tue"],
             {("k", ONE, "b0"): {("red",)}, ("k", "tue", "b0"): {("blue",)}})
    return Candidate(E, p, _T("colour"), {ONE: ONE, "tue": "tue"}, {"b0": "b0"}, {"k": (frozenset(["r", "u"]), _T("colour"))}, ["k"], "colour",
                     name="ℰ_one")


def sign_mech():
    """A sign with a day port and a palette rule (no pin): the edit tue sets the day; the palette component reads it.
    S106, second checker: the edit 'plain' (the palette deleted), built only for the further question 'why is the
    palette there at all?', is deleted with it (parked, P8)."""
    pal = {("Mon", "red"), ("Tue", "blue")}
    D = _org("D_sign_day", ["day", "colour"], {"day": ("Mon", "Tue"), "colour": COLOURS}, ["c_day", "c_col"],
             {"c_day": ("day",), "c_col": ("day", "colour")}, ["b0"], [ONE, "tue"],
             {("c_day", ONE, "b0"): {("Mon",)}, ("c_day", "tue", "b0"): {("Tue",)},
              ("c_col", ONE, "b0"): pal, ("c_col", "tue", "b0"): pal})
    p = Question(D, [(ONE, "b0"), ("tue", "b0")], "b0", PortQuery(), "colour", name="p_sign_day")
    return Candidate(D, p, _T("day", "colour"), {ONE: ONE, "tue": "tue"}, {"b0": "b0"}, _ident_lam(D), ["c_day", "c_col"], "colour", name="ℰ_day")


def acc_r3_row(c):
    """Round 3's (E) (NC1 a conjunct) under the four readings of D6.3's quantifier: Acc ∧ NC1_q."""
    from . import core
    old = core.SLOT_QUANTIFIER
    out = {}
    try:
        for q in SLOT_QUANTIFIERS:
            core.SLOT_QUANTIFIER = q
            out[q] = account(c, reading="r3")
    finally:
        core.SLOT_QUANTIFIER = old
    return out


def acc_s106_row(c):
    from . import core
    old = core.SLOT_QUANTIFIER
    out = {}
    try:
        for q in SLOT_QUANTIFIERS:
            core.SLOT_QUANTIFIER = q
            out[q] = account(c, reading="S106")
    finally:
        core.SLOT_QUANTIFIER = old
    return out


def _tf(row):
    return "(" + ",".join("T" if row[q] else "F" for q in SLOT_QUANTIFIERS) + ")"


@claim("FC23.new2", ["I184", "I189", "I90"])
def fc23new2(S):
    parts = []
    p = sign_question()
    two, one = sign_two(p), sign_one(p)
    # (a) the owner's two-part sign
    v2, d2 = account(two, detail=True)
    r3_two, s_two = acc_r3_row(two), acc_s106_row(two)
    pins_two = pins(two)
    slots_two = {q: [k for k in two.E.comps if slot(two, k, quantifier=q)] for q in SLOT_QUANTIFIERS}
    ok_a = (v2 and all(s_two.values()) and p.ans(ONE, "b0") == "red" and p.ans("tue", "b0") == "blue"
            and pins_two == [("r", (ONE, "b0")), ("u", ("tue", "b0"))] and not slots_two["every"])
    parts.append(computed("(a) S44: the two-part sign is an explanation under (E) after S106",
                          "ℰ_two (a red part that switches on on Mondays, a blue part on Tuesdays) meets (E) under every reading of D6.3's quantifier; "
                          "the red part pins the answer on Mondays, the blue part on Tuesdays; no part is a slot under 'every'",
                          ok_a, "answers: Monday %r, Tuesday %r; (E) after S106: %s, conjuncts %s; Dependence witness %s; under the four readings (every, some, some-exempt, "
                          "some-exempt-set): after S106 %s, round 3's (E) %s; pins %s; slots under each reading %s\n%s\n%s"
                          % (p.ans(ONE, "b0"), p.ans("tue", "b0"), v2, {k: d2[k] for k in ("F1", "F2", "A", "Dep", "NC1", "NonVacuous")}, NC2(two, witness=True),
                             _tf(s_two), _tf(r3_two), pins_two, slots_two, p.D.describe(), two.describe()), ["I184", "I189"]))
    # (b) the one-part sign (the lookup): the result that moves
    v1, d1 = account(one, detail=True)
    r3_one, s_one = acc_r3_row(one), acc_s106_row(one)
    ok_b = v1 and all(s_one.values()) and not any(r3_one.values()) and slot(one, "k", quantifier="every")
    parts.append(computed("(b) the one-part sign: a slot, an explanation under (E) after S106, none under round 3's",
                          "ℰ_one (one part giving red on Mondays and blue on Tuesdays) has a slot under every reading and meets (E) after S106; round 3's (E) excluded it under every reading",
                          ok_b, "(E) after S106 %s (conjuncts %s); under the four readings: after S106 %s, round 3's %s; Slot_C(ℰ_one, k): %s\n%s"
                          % (v1, {k: d1[k] for k in ("F1", "F2", "A", "Dep", "NC1", "NonVacuous")}, _tf(s_one), _tf(r3_one),
                             {q: slot(one, "k", quantifier=q) for q in SLOT_QUANTIFIERS}, one.describe()), ["I184", "I189"]))
    # (f) S41 (Q2) kept, computed as FC30.new1 (a) computes it: provenance by hand (I90) through sel and con; an
    # argument not using (E) that rules out Expl(ℰ); (Suff)'s defeat set under each reading (D16.XV)
    rows, ok_f = [], True
    for c in (two, one):
        acc = account(c)
        ok_f = ok_f and acc
        for kind in ("Dec", "Con", "Sel"):
            s_, k_, dec = provenance_of(c, kind, [(ONE, "b0")])
            j = Assessor(["MP"], ["r", Imp("r", Not("Expl_" + c.name))])
            out, _ = expl_ruled_out(j, c.name)
            d = {r: suff_defeats(acc, dec, out, r) for r in SUFF_READINGS}
            expl = acc and not dec  # Expl := Acc ∧ ¬Dec, FC30.new1 (c)'s common model
            rows.append("%s, %s (Sel %s, Con %s, Dec %s), argument usable %s: %s; Acc ∧ Dec ⇒ ¬Expl with Expl := Acc ∧ ¬Dec: %s"
                        % (c.name, kind, s_, k_, dec, out, "; ".join("%s %s" % (r, d[r]) for r in SUFF_READINGS), expl_ok(acc, dec, expl)))
            ok_f = ok_f and out and expl_ok(acc, dec, expl) and d["L17 (S41)"] == d["L536"]
            if kind == "Dec":
                ok_f = ok_f and dec and not d["L17 (S41)"] and d["L17 as text 104 words it"]
            if kind == "Con":
                ok_f = ok_f and not dec and d["L17 (S41)"]
    parts.append(computed("(f) S41 (Q2) kept: a declared link is no explanation",
                          "ℰ_two and ℰ_one meet (E); with a declared transport (Dec) and an argument not using (E) that rules out Expl(ℰ), each is outside (Suff)'s defeat set as S41 writes it "
                          "and as L536 writes it (Acc ∧ Dec ⇒ ¬Expl applies), inside it as text 104's L17 words it; with a constructed transport it is inside all three (as FC30.new1 (a))",
                          ok_f, "\n".join(rows), ["I90"]))
    # (g) a look: the functions of D6.3 take one candidate
    sigs = {f.__name__: list(inspect.signature(f).parameters) for f in (slot, NC1, pin, pins)}
    ok_g = all(ps[0] == "cand" and sum(1 for x in ps if x.startswith("cand")) == 1 for ps in sigs.values())
    parts.append(look("(g) no grade (S20, S23)", "the look: slot, NC1, pin and pins each take one candidate; none takes two candidates, so none orders candidates",
                      ok_g, "; ".join("%s(%s)" % (n, ", ".join(ps)) for n, ps in sigs.items())))
    return parts


@claim("FC23.new3", ["I77", "I78", "I81", "I82", "I184"])
def fc23new3(S):
    parts = []

    def gen(rng, size):
        D, p = D_and_p(rng, size)
        if D is None or getattr(p.Q, "kind", None) != "port":
            return None
        r = rng.random()
        if r < 0.4:
            c = gen_candidate(rng, p, name="ℰ", perturb_p=0.05, background_p=0.0, random_tau_p=0.0, demote_p=0.0)
        elif r < 0.7:
            c = gen_lookup(rng, p)
        else:
            c = any_candidate(rng, p, size, name="ℰ")
        return p, c

    # (a) Slot under 'every' is Pin at every determined pair
    def ca(m):
        p, c = m
        det = [(a, b) for (a, b) in p.C if p.ans(a, b) is not BOT]
        for k in c.E.comps:
            s = slot(c, k, quantifier="every")
            q = bool(det) and all(pin(c, k, a, b) for (a, b) in det)
            if s != q:
                return "Slot %s, Pin at every determined pair %s, for %s\n%s\n%s" % (s, q, k, p.describe(), c.describe())
        return None

    parts.append(forall(S, "FC23.new3", 1, "(a) Slot (D6.3, 'every') is Pin at every pair of Det_C", "Slot_C(ℰ,k) ⟺ Det_C ≠ ∅ ∧ ∀(a,b) ∈ Det_C Pin(ℰ,k;a,b)",
                        gen, ca, SMALL, 60, BOTHFAM, ["I184"]))

    # (d) the pole: E_fwd on C1 has no pin; on C2 it pins only at the settings of L, where the pair's own edit puts
    # c_L's slice there
    D = pole()
    C1, C2, _ = pole_contracts(D)
    rows, ok = [], True
    for nm, C in (("C1", C1), ("C2", C2)):
        q = Question(D, C, "b1_45", PortQuery(), "L", name=nm)
        c = pole_fwd_candidate(q)
        ps = pins(c)
        Lset = [(a, b) for (a, b) in C if "L" in dict(D.meta["inv"][a])]
        at = sorted(set(x for _, x in ps), key=repr)
        rows.append("%s: (E) %s; pins %d, all by c_L: %s, at exactly the settings of L: %s"
                    % (nm, account(c), len(ps), all(k == "c_L" for k, _ in ps), at == sorted(Lset, key=repr)))
        if nm == "C1":
            ok = ok and account(c) and not ps
        else:
            ok = ok and account(c) and bool(ps) and all(k == "c_L" for k, _ in ps) and at == sorted(Lset, key=repr)
    parts.append(computed("(d) the pole's forward candidate (E1)", "on C1 no part pins the answer; on C2 c_L pins it exactly at the settings of L (the pair's own edit puts the slice there)",
                          ok, "; ".join(rows), ["I184"]))
    return parts


@claim("FC25.new2", ["I77", "I78", "I80", "I101", "I138"])
def fc25new2(S):
    """L269: the table that encodes an organization's response to every admitted change (E_enc, D6.10, I32)."""
    parts = []

    def gen(rng, size):
        D, p = D_and_p(rng, size, family="G-surg")
        fp = set(v for j in D.comps for v in D.foot[j])
        if fp != set(D.ports):
            return None
        U = sorted(set([p.deltaD] + [v for v in D.ports if rng.random() < 0.7]), key=D.ports.index)
        return p, table_candidate(p, U, encode=True)

    def ca(m):
        p, c = m
        vals = set(p.ans(a, b) for (a, b) in p.C)
        if len(vals) < 2 or not p.D.sol(ONE, p.b0):
            return VAC
        v, d = account(c, detail=True)
        if not v:
            return "E_enc, answers varying on C (%s), fails (E): %s\n%s\n%s\n%s" % (sorted(vals, key=repr), d, p.describe(), p.D.describe(), c.describe())
        return None

    parts.append(forall(S, "FC25.new2", 1, "(a) E_enc meets (E) where its answer varies", "Ans_p not constant on C ∧ Sol_D(1,b0) ≠ ∅ ∧ every port of D in a footprint ⇒ Acc(E_enc)",
                        gen, ca, SMALL, 40, ["G-surg"], ["I32"], note="targets whose every port lies in a footprint"))

    def cb(m):
        p, c = m
        if not any(p.ans(a, b) is not BOT for (a, b) in p.C):
            return VAC
        if not slot(c, "tab", quantifier="every"):
            return "E_enc with a determined answer on C and no slot\n%s\n%s" % (p.describe(), c.describe())
        return None

    parts.append(forall(S, "FC25.new2", 2, "(b) E_enc's one component is a slot", "Det_C ≠ ∅ ⇒ Slot_C(E_enc, tab) (D6.3, 'every')",
                        gen, cb, SMALL, 40, ["G-surg"], ["I32", "I184"]))
    # (c) the pole's C1: E_enc with δ = L meets (E) after S106, not under round 3's
    D = pole()
    C1, C2, _ = pole_contracts(D)
    rows, ok = [], True
    for nm, C in (("C1", C1), ("C2", C2)):
        q = Question(D, C, "b1_45", PortQuery(), "L", name=nm)
        c = table_candidate(q, list(D.ports), encode=True)
        a_new, a_r3 = account(c), account(c, reading="r3")
        rows.append("%s: (E) after S106 %s, round 3's %s, slot %s" % (nm, a_new, a_r3, slot(c, "tab")))
        ok = ok and a_new and not a_r3
    parts.append(computed("(c) the pole: E_enc on C1 and C2", "E_enc (δ = L) meets (E) after S106 and failed round 3's (E) (NC1), on C1 and on C2", ok, "; ".join(rows), ["I32"]))
    return parts
