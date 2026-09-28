# S106 (decisions S44, S45): the written-in test taken out of (E). New test claims (not moves, rule 16 of round 3):
#   FC23.new2  the owner's shop sign (S44): an explanation under (E) after S106; the further question it leaves open,
#              "why is the red part there in the first place?", built as content (D6.11).
#   FC23.new3  D6.11 on generated models: Slot and Pin; at a pin the answer is read off the further question's answer;
#              a candidate that leaves a question open meets (A) and Dependence on it with no Γ, δ; the pole.
#   FC25.new2  L269's encoding table meets (E) where its answer varies (its one component a slot).
# Every value is computed by core.account, core.pin, core.further_question, core.leaves_open; nothing is tagged by
# hand. Nothing here orders candidates, counts questions or grades (S20, S23); what hard to vary covers is parked.
import itertools

from .core import (ONE, BOT, Org, Question, PortQuery, Candidate, Translation, account, slot, NC1, NC2, dep, A, F1, F1_at,
                   pin, pins, further_question, leaves_open, RelQuery, SLOT_QUANTIFIERS, powerset)
from .harness import claim, forall, exists, computed, construction, look, VAC
from .gen import gen_candidate, any_candidate, gen_lookup
from .cases import pole, pole_fwd_candidate, single_settings
from .claims_a import SMALL, BOTHFAM, D_and_p, pole_contracts, table_candidate, _T

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
    The target also admits 'repaint' (the owner picks another palette, green on Mondays), which the sign question's
    stated scope leaves out: the further question 'why this palette?' contrasts it with the baseline."""
    pal = {("Mon", "red"), ("Tue", "blue")}
    D = _org("D_sign_day", ["day", "colour"], {"day": ("Mon", "Tue"), "colour": COLOURS}, ["c_day", "c_col"],
             {"c_day": ("day",), "c_col": ("day", "colour")}, ["b0"], [ONE, "tue", "repaint"],
             {("c_day", ONE, "b0"): {("Mon",)}, ("c_day", "tue", "b0"): {("Tue",)}, ("c_day", "repaint", "b0"): {("Mon",)},
              ("c_col", ONE, "b0"): pal, ("c_col", "tue", "b0"): pal, ("c_col", "repaint", "b0"): {("Mon", "green"), ("Tue", "blue")}})
    p = Question(D, [(ONE, "b0"), ("tue", "b0")], "b0", PortQuery(), "colour", name="p_sign_day")
    return Candidate(D, p, _T("day", "colour"), {ONE: ONE, "tue": "tue"}, {"b0": "b0"}, _ident_lam(D), ["c_day", "c_col"], "colour", name="ℰ_day")


def sign_plus():
    """D⁺: the sign with what puts the red part there, the shop owner's choice (a port set by c_choice; the edit
    'otherwise' sets it to 'none'); the red part reads the choice. The further question p^r: what relation does
    the red part, as the choice installs it ({c_choice, r}), give on the colour; contract: the baseline and
    'otherwise' (the owner decides otherwise) [I189]."""
    rel = {("c_choice", a, "b0"): {("red-Mon",)} for a in (ONE, "tue")}
    rel[("c_choice", "otherwise", "b0")] = {("none",)}
    r_on = {("red-Mon", "red")} | {("none", x) for x in COLOURS}
    rel[("r", ONE, "b0")] = r_on
    rel[("r", "otherwise", "b0")] = r_on
    rel[("u", "tue", "b0")] = {("blue",)}
    D = _org("D_sign+", ["choice", "colour"], {"choice": ("red-Mon", "none"), "colour": COLOURS}, ["c_choice", "r", "u"],
             {"c_choice": ("choice",), "r": ("choice", "colour"), "u": ("colour",)}, ["b0"], [ONE, "tue", "otherwise"], rel)
    pr = Question(D, [(ONE, "b0"), ("otherwise", "b0")], "b0", RelQuery(("colour",)), ("c_choice", "r"), name="p^r (why is the red part there?)")
    mech = Candidate(D, pr, _T("choice", "colour"), {a: a for a in D.A}, {"b0": "b0"}, _ident_lam(D), ["c_choice", "r", "u"], ("c_choice", "r"),
                     name="ℰ⁺ (the owner's choice)")
    return D, pr, mech


def read_off(c, k, a, b):
    """The values δ_E takes, read through k's port translation, on the further question's answer at (a, b)."""
    pk = further_question(c, k)
    ans_k = pk.ans(a, b)
    if ans_k is BOT:
        return None
    onto = list(pk.Q.onto)
    tr = c.lam[k][1][c.deltaE]
    return set(tr.fn(tuple(z[onto.index(u)] for u in tr.dports)) for z in ans_k)


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


@claim("FC23.new2", ["I184", "I185", "I186", "I189"])
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
    # (c) the further question: why is the red part there in the first place?
    Dp, pr, mech = sign_plus()
    y0, y1 = pr.ans(ONE, "b0"), pr.ans("otherwise", "b0")
    lo_two, lo_one = leaves_open(two, pr), leaves_open(one, pr)
    vm, dm = account(mech, detail=True)
    retarget = [(G, dl) for G in powerset(two.E.comps) for dl in two.E.ports
                if A(two.replace(p=pr, Gamma=tuple(G), deltaE=dl)) and dep(two.replace(p=pr, Gamma=tuple(G), deltaE=dl))]
    ok_c = y0 != y1 and lo_two and lo_one and vm and not retarget
    parts.append(computed("(c) the further question 'why is the red part there in the first place?' as content (D6.11)",
                          "p^r on D⁺ (the sign with the shop owner's choice): its answer differs between the baseline and 'the owner decides otherwise'; "
                          "both sign candidates leave it open (every pair of its contract they translate is a relabeling for it), so none with their transport meets (A) and "
                          "Dependence on it; D⁺'s own organization, the owner's choice, meets (E) on it",
                          ok_c, "p^r: %s; answers: baseline %s, otherwise %s; LeavesOpen: ℰ_two %s, ℰ_one %s (pairs of C' they translate: %s); ℰ_two re-aimed at p^r with some Γ', δ' "
                          "meeting (A) and Dependence: %s; ℰ⁺ (E) %s, conjuncts %s, Dependence witness %s\n%s"
                          % (pr.describe(), sorted(y0), sorted(y1), lo_two, lo_one, [x for x in sorted(pr.C, key=repr) if two.translates(*x)],
                             retarget or "none", vm, {k: dm[k] for k in ("F1", "F2", "A", "Dep", "NonVacuous")}, NC2(mech, witness=True), Dp.describe()),
                          ["I185", "I186", "I189"]))
    # (d) at a pin the answer is read off the further question at the part
    rows, ok_d = [], True
    for c in (two, one):
        for (k, (a, b)) in pins(c):
            got = read_off(c, k, a, b)
            rows.append("%s: %s at (%s,%s): Ans_p %r; read off p^%s's answer %s" % (c.name, k, a, b, p.ans(a, b), k, sorted(got) if got else got))
            ok_d = ok_d and F1_at(c, a, b) and got == {p.ans(a, b)}
    parts.append(computed("(d) at a pin, Ans_p is read off the further question's answer (D6.11 (b))",
                          "at every pin of ℰ_two and ℰ_one, with (F1) there, the value the part's counterpart gives on the colour is the target's answer",
                          ok_d, "; ".join(rows), ["I184", "I185"]))
    # (e) a sign with no pin: the day is set by the edit and a palette component reads it
    mc = sign_mech()
    vmc = account(mc)
    pcol = further_question(mc, "c_col", C2=[(ONE, "b0"), ("repaint", "b0")], name="p^c_col (why this palette?)")
    ok_e = vmc and not pins(mc) and pcol.ans(ONE, "b0") != pcol.ans("repaint", "b0") and leaves_open(mc, pcol)
    parts.append(look("(e) a sign with a day port and a palette rule", "the look: it meets (E), no part pins the answer (the colour is read off the palette jointly with the day the edit sets), "
                      "and it too leaves a further question open (why this palette and not green on Mondays?): LeavesOpen is a relation of one candidate and one question, not a grade",
                      ok_e, "(E) %s; pins %s; %s: answers baseline %s, repaint %s; left open: %s\n%s"
                      % (vmc, pins(mc), pcol.name, sorted(pcol.ans(ONE, "b0")), sorted(pcol.ans("repaint", "b0")), leaves_open(mc, pcol), mc.describe()),
                      ["I185", "I186"]))
    # (f) S41 Q2 kept; (g) no order
    parts.append(construction("(f) S41 (Q2) kept: a declared link is no explanation", "Acc(ℰ) ∧ Dec(t) ⇒ ¬Expl(ℰ) (D16.XV) applies to the sign candidates as to any: (E) takes no provenance (FC30)",
                              True, "core.account reads no provenance; D16.XV's rule is unchanged by S106; a sign candidate whose transport was only declared is no explanation (S41), one whose "
                              "transport was found or worked out is, under (Suff), unless an argument not using (E) rules that out"))
    parts.append(construction("(g) no grade (S20, S23)", "pin, further_question and leaves_open are relations of one candidate (and one question); no function of this program takes two candidates and returns an order",
                              True, "the functions of D6.11 in core.py take one candidate (pin, pins, leaves_open) or one candidate and one part (further_question)"))
    return parts


@claim("FC23.new3", ["I77", "I78", "I81", "I82", "I184", "I185", "I186"])
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

    # (b) at a pin with (F1) there, the answer is read off the further question's answer
    def cb(m):
        p, c = m
        hit = False
        for (k, (a, b)) in pins(c):
            if k not in c.Gamma or not F1_at(c, a, b):  # (F1) and λ are the commitments' (D5.4)
                continue
            hit = True
            got = read_off(c, k, a, b)
            if got != {p.ans(a, b)}:
                return "Pin at (%s,%s) by %s with (F1), and the further question's answer gives %s, not {%r}\n%s\n%s" % (a, b, k, got, p.ans(a, b), p.describe(), c.describe())
        return None if hit else VAC

    parts.append(forall(S, "FC23.new3", 2, "(b) at a pin, Ans_p is read off Ans_{p^k}", "k ∈ Γ ∧ Pin(ℰ,k;a,b) ∧ F1 at (a,b) ⇒ the values λ(k)'s relation gives δ_E at (a,b) are {Ans_p(a,b)}",
                        gen, cb, SMALL, 60, BOTHFAM, ["I184", "I185"]))

    # (c) LeavesOpen(ℰ, p') ∧ τ(1) = 1 ⇒ no Γ', δ' makes (E, p', t, Γ', δ') meet (A) and Dependence
    def gen_c(rng, size):
        m = gen(rng, size)
        if m is None:
            return None
        p, c = m
        D = p.D
        pairs = [(a, b) for a in D.A for b in D.B if (a, b) != (ONE, p.b0)]
        C2 = [(ONE, p.b0)] + [x for x in pairs if rng.random() < 0.5]
        p2 = Question(D, C2, p.b0, PortQuery(), rng.choice(D.ports), name="p'")
        return p, c, p2

    def cc(m):
        p, c, p2 = m
        if c.tau.get(ONE) != ONE or not leaves_open(c, p2):
            return VAC
        for G in powerset(c.E.comps):
            for dl in c.E.ports:
                c2 = c.replace(p=p2, Gamma=tuple(G), deltaE=dl)
                if A(c2) and dep(c2):
                    return "LeavesOpen(ℰ, p') and yet Γ' = %s, δ' = %s meet (A) and Dependence on p'\n%s\n%s\n%s" % (sorted(G), dl, p2.describe(), p2.D.describe(), c.describe())
        return None

    parts.append(forall(S, "FC23.new3", 3, "(c) a question left open is answered with ℰ's transport under no Γ', δ'",
                        "LeavesOpen(ℰ, p') ∧ τ(1) = 1 ⇒ ∀Γ' ⊆ J_E ∀δ': ¬(A ∧ Dependence) for (E, p', t, Γ', δ') (FC21 (a); pairs not translated fail (A))",
                        gen_c, cc, SMALL, 60, BOTHFAM, ["I186"]))

    # (d) the pole: E_fwd on C1 has no pin; on C2 it pins only at the settings of L, where the pair's own edit puts
    # c_L's slice there, and the further question at c_L on C2 is not left open (t translates those settings)
    D = pole()
    C1, C2, _ = pole_contracts(D)
    rows, ok = [], True
    for nm, C in (("C1", C1), ("C2", C2)):
        q = Question(D, C, "b1_45", PortQuery(), "L", name=nm)
        c = pole_fwd_candidate(q)
        ps = pins(c)
        Lset = [(a, b) for (a, b) in C if "L" in dict(D.meta["inv"][a])]
        at = sorted(set(x for _, x in ps), key=repr)
        lo = leaves_open(c, further_question(c, "c_L"))
        rows.append("%s: (E) %s; pins %d, all by c_L: %s, at exactly the settings of L: %s; p^c_L on %s left open: %s"
                    % (nm, account(c), len(ps), all(k == "c_L" for k, _ in ps), at == sorted(Lset, key=repr), nm, lo))
        if nm == "C1":
            ok = ok and account(c) and not ps
        else:
            ok = ok and account(c) and bool(ps) and all(k == "c_L" for k, _ in ps) and at == sorted(Lset, key=repr) and not lo
    parts.append(computed("(d) the pole's forward candidate (E1)", "on C1 no part pins the answer; on C2 c_L pins it exactly at the settings of L (the pair's own edit puts the slice there), "
                          "and the further question at c_L is not left open on C2 (t translates the settings of L, at which c_L's relation changes)", ok, "; ".join(rows), ["I184", "I185", "I186"]))
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
