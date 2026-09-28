# S107 round 4, area 2 (L229-L372, Parts V-VIII): test claims for the area's rulings (not moves, rule 16).
#   FC27.new1  the reversed calculation on the production contracts: C1 under τ and τ', C_H under τ and τ' (B4, C-K1; R4A2-01)
#   FC23.new4  Slot (D6.3) with Pin's translation clause; pins made by the pair's own edit (B8, S3; B9, R4A2-02)
#   FC23.new5  the owner's two-part sign on a target with one part (C-K3; I189)
#   FC42.new1  (D) Boundary with the designation carried by the operation (N1: B-N1, W-N1, S-N1, C-N1; R4A2-03)
# Every truth value is computed by core (account, slot, pin, F1_at, F2eq_at, hom, Roles, boundary) from the organizations,
# transports and contracts built here; nothing is a hand-set tag (lesson S39). Nothing orders candidates, counts
# questions or grades (S20, S23); what hard to vary covers is parked (P8).
import itertools
import random

from .core import (ONE, BOT, Org, Question, PortQuery, Candidate, Translation, Roles, account, slot, pin, pins,
                   F1_at, F2eq_at, hom, restrict, boundary, SLOT_QUANTIFIERS)
from .harness import claim, forall, computed, look, VAC
from .gen import gen_candidate, any_candidate, gen_lookup, rename_org
from .cases import pole, pole_fwd_candidate, pole_rev_candidate, single_settings, COT
from .claims_a import SMALL, BOTHFAM, D_and_p, pole_contracts, _T
from .claims_s106 import _org, COLOURS, sign_question, sign_two, sign_one, acc_r3_row, acc_s106_row, _tf


def _tau_prime(D):
    """Mimo's τ' (FC27's look): set H := h carried to a setting of E_rev's L (h·cot θ, θ as the edit sets it or 45°),
    set θ := t to set(θ = t, L = ·); built as claims_a.fc27 and s106_cases.py build it."""
    inv = D.meta["inv"]
    lab = {v: k for k, v in inv.items()}

    def tau2(a):
        sm = dict(inv[a])
        if not sm:
            return ONE
        t = sm.get("T", 45)
        new = {}
        if "T" in sm:
            new["T"] = t
        if "L" in sm:
            new["L"] = sm["L"]
        elif "H" in sm or "T" in sm:
            new["L"] = sm.get("H", 1) * COT[t]
        if "H" in sm and "L" in sm:
            new["H"] = sm["H"]
        return lab.get(tuple(sorted(new.items())))
    t2 = {a: tau2(a) for a in D.A}
    return {a: x for a, x in t2.items() if x is not None}


def _production(D, C, q_port="L"):
    """L151: a production question has a Q that reads an output port and a C containing interventions on upstream ports.
    Computed: Out(q_port, j) for the component j that assigns it (D2.3), and the upstream ports v ⇝ q_port (D3.3) that C sets."""
    R = Roles(D)
    inv = D.meta["inv"]
    j = R.asg.get(q_port)
    out = j is not None and R.output(q_port, j)
    ups = sorted(set(v for (a, b) in C for v, _ in inv[a] if v != q_port and R.upstream(v, q_port)))
    return out and bool(ups), j, ups


@claim("FC27.new1", ["I65", "I92", "I84"])
def fc27_new1(S):
    parts = []
    D = pole()
    C1, C2, _ = pole_contracts(D)
    CH = frozenset([(ONE, "b1_45")] + [(a, "b1_45") for a in single_settings(D, ["H"])])
    t2 = _tau_prime(D)
    # (a) C1 and C_H are production contracts (L151, D2.3, D3.3)
    rows, ok = [], True
    for nm, C in (("C1", C1), ("C_H", CH)):
        prod, j, ups = _production(D, C)
        rows.append("%s: Q reads L, Out(L, %s) and C sets upstream ports %s: a production contract %s" % (nm, j, ups, prod))
        ok = ok and prod
    parts.append(computed("(a) C1 and C_H are production contracts (L151)", "on each, Q reads L, an output of c_L, and C holds interventions on a port upstream of L",
                          ok, "; ".join(rows), ["I65"]))
    # (b) E_rev under τ (edits carried to themselves): (F2) fails on C1 and on C_H at a setting of H ≠ u_H
    rows, ok = [], True
    for nm, C in (("C1", C1), ("C_H", CH)):
        p = Question(D, C, "b1_45", PortQuery(), "L", name=nm)
        r = pole_rev_candidate(p)
        v, d = account(r, detail=True)
        bad = [a for (a, b) in sorted(C, key=repr) if not F2eq_at(r, a, b)]
        rows.append("%s: F2eq fails at %s; (E) %s, conjuncts F1 %s, F2 %s, A %s, Dep %s" % (nm, bad, v, d["F1"], d["F2"], d["A"], d["Dep"]))
        ok = ok and bool(bad) and not d["F2"] and not v
    parts.append(computed("(b) under τ, E_rev fails (F2) on C1 and on C_H", "with each edit carried to itself, intervening on H changes the target's L and not E_rev's: F2eq fails at a setting of H on C1 and on C_H",
                          ok, "; ".join(rows), ["I92"]))
    # (c) under τ': on C1 (F2) fails by its homomorphism clause; on C_H every conjunct of (E) holds
    p1 = Question(D, C1, "b1_45", PortQuery(), "L", name="C1")
    r1 = pole_rev_candidate(p1).replace(tau=t2, name="ℰ_rev under τ' on C1")
    v1, d1 = account(r1, detail=True)
    pH = Question(D, CH, "b1_45", PortQuery(), "L", name="C_H")
    rH = pole_rev_candidate(pH)
    rH = rH.replace(tau={a: t2[a] for a in sorted(set(x for x, _ in CH), key=repr)}, name="ℰ_rev under τ' on C_H")
    vH, dH = account(rH, detail=True)
    slots_H = {q: [k for k in rH.E.comps if slot(rH, k, quantifier=q)] for q in SLOT_QUANTIFIERS}
    r3H, sH = acc_r3_row(rH), acc_s106_row(rH)
    ok_c1 = (not v1) and (not d1["Hom"]) and d1["F2eq"]
    parts.append(computed("(c) under τ' on C1: (F2) fails by its homomorphism clause", "E_rev under τ' meets F2eq at every pair of C1 and fails Hom, so fails (F2) on C1",
                          ok_c1, "conjuncts %s" % d1, ["I84", "I92"]))
    ok_cH = vH and dH["F2"] and dH["F1"] and dH["A"] and dH["Dep"] and dH["NonVacuous"] and not dH["NC1"] and not any(r3H.values()) and all(sH.values())
    parts.append(computed("(d) under τ' on C_H: every conjunct of (E) holds; L271 read of every production contract states an (F2) failure the computation does not give",
                          "E_rev under τ' restricted to C_H meets (F1), (F2), (A), Dependence and non-vacuity after S106, under every reading of D6.3's quantifier; "
                          "round 3's (E) excluded it by NC1 alone (r_L a slot): a written-in candidate, an explanation under S44, S45; read of C1 (R4A2-01), L271 is (b) and (c)",
                          ok_cH, "conjuncts %s; slots under each reading %s; (E) under (every, some, some-exempt, some-exempt-set): after S106 %s, round 3's %s"
                          % (dH, slots_H, _tf(sH), _tf(r3H)), ["I65", "I92"]))
    return parts


class PartialPi(Candidate):
    """A candidate whose π is defined only on pi_dom, a set of solutions of the target (D5.1, I16: π: X_D ⇀ X_E, defined at
    least on Sol_D(a,b) at every pair t translates). core.Candidate's π is total (I81); this subclass is used by FC23.new4
    only, to reach the corner where t fails to translate a pair only through π's domain."""

    pi_dom = None

    def translates(self, a, b):
        if not (a in self.tau and b in self.sigma):
            return False
        if self.pi_dom is None:
            return True
        return all(z in self.pi_dom for z in self.p.D.sol(a, b))


def _partial(c, tau=None, pi_dom=None, name=None):
    x = PartialPi.__new__(PartialPi)
    x.__dict__.update(c.__dict__)
    if tau is not None:
        x.tau = dict(tau)
    x.pi_dom = pi_dom
    if name:
        x.name = name
    return x


def slot_as_displayed_s106(cand, k):
    """D6.3's Slot as displayed after S106, with no translation conjunct: δ_E ∈ V_k ∧ Det_C ≠ ∅ ∧ ∀(a,b) ∈ Det_C
    {w_δE : w ∈ L^E_k(τ(a),σ(b))} = {Ans_p(a,b)}. Returns None where the clause has no value (τ(a) or σ(b) undefined at a
    determined pair), else True or False."""
    p, E, w = cand.p, cand.E, cand.deltaE
    if getattr(p.Q, "kind", None) != "port" or w not in E.foot[k]:
        return False
    det = [(a, b) for (a, b) in p.C if p.ans(a, b) is not BOT]
    if not det:
        return False
    i = E.foot[k].index(w)
    val = True
    for (a, b) in det:
        if a not in cand.tau or b not in cand.sigma:
            return None
        if set(t[i] for t in E.L(k, cand.tau[a], cand.sigma[b])) != {p.ans(a, b)}:
            val = False
    return val


def slot_r4(cand, k):
    """D6.3 after round 4, area 2 (B8, S3): δ_E ∈ V_k ∧ Det_C ≠ ∅ ∧ ∀(a,b) ∈ Det_C [t translates (a,b) ∧ {w_δE : w ∈
    L^E_k(τ(a),σ(b))} = {Ans_p(a,b)}] (I184). core.slot under 'every' computes it."""
    return slot(cand, k, quantifier="every")


@claim("FC23.new4", ["I16", "I17", "I81", "I82", "I184", "I136"])
def fc23_new4(S):
    parts = []
    p = sign_question()
    one = sign_one(p)
    # (a) τ undefined at a determined pair (Tuesday): the clause as displayed has no value; D6.3 with the clause and Pin: False
    c_a = _partial(one, tau={ONE: ONE}, name="ℰ_one, τ at 1 only")
    disp_a, new_a, pin_a = slot_as_displayed_s106(c_a, "k"), slot_r4(c_a, "k"), pin(c_a, "k", "tue", "b0")
    ok_a = disp_a is None and new_a is False and pin_a is False and not account(c_a)
    parts.append(computed("(a) B8: τ undefined at a determined pair", "the displayed clause of D6.3 has no value there; D6.3 with Pin's translation clause is False, as Pin is, and (E) fails",
                          ok_a, "displayed clause: %s (None = no value); D6.3 with the clause: %s; Pin at (tue,b0): %s; (E): %s" % (disp_a, new_a, pin_a, account(c_a)), ["I17", "I184"]))
    # (b) π defined only off Sol_D(tue, b0) (τ, σ total): the displayed clause True, Pin False at Tuesday
    dom_b = frozenset(p.D.sol(ONE, "b0"))
    c_b = _partial(one, pi_dom=dom_b, name="ℰ_one, π defined on Sol_D(1,b0) only")
    disp_b, new_b = slot_as_displayed_s106(c_b, "k"), slot_r4(c_b, "k")
    pins_b = {x: pin(c_b, "k", *x) for x in ((ONE, "b0"), ("tue", "b0"))}
    ok_b = disp_b is True and new_b is False and pins_b[(ONE, "b0")] and not pins_b[("tue", "b0")] and not account(c_b)
    parts.append(computed("(b) S3: π partial exactly off Sol_D at a determined pair", "the displayed clause holds, Pin fails at that pair, so 'Slot ⟺ Det_C ≠ ∅ ∧ Pin at every pair of Det_C' fails for the displayed clause and holds for D6.3 with the clause",
                          ok_b, "displayed clause: %s; D6.3 with the clause: %s; Pin %s; (E): %s; t translates (tue,b0): %s" % (disp_b, new_b, pins_b, account(c_b), c_b.translates("tue", "b0")), ["I16", "I81", "I184"]))

    # (c) generated models with partial τ and partial π: D6.3 with the clause ⟺ Det_C ≠ ∅ ∧ Pin at every pair of Det_C
    def gen(rng, size):
        D, q = D_and_p(rng, size)
        if D is None or getattr(q.Q, "kind", None) != "port":
            return None
        r = rng.random()
        if r < 0.4:
            c = gen_candidate(rng, q, name="ℰ", perturb_p=0.05, background_p=0.0, random_tau_p=0.0, demote_p=0.0)
        elif r < 0.7:
            c = gen_lookup(rng, q)
        else:
            c = any_candidate(rng, q, size, name="ℰ")
        tau = {a: x for a, x in c.tau.items() if a == ONE or rng.random() < 0.8}
        sols = sorted(set(z for a in D.A for b in D.B for z in D.sol(a, b)), key=repr)
        pd = None if rng.random() < 0.4 else frozenset(z for z in sols if rng.random() < 0.8)
        return q, _partial(c, tau=tau, pi_dom=pd)

    tally = {"displayed has no value": 0, "displayed True, D6.3 with the clause False": 0}

    def cc(m):
        q, c = m
        det = [(a, b) for (a, b) in q.C if q.ans(a, b) is not BOT]
        for k in c.E.comps:
            s = slot_r4(c, k)
            pe = bool(det) and all(pin(c, k, a, b) for (a, b) in det)
            if s != pe:
                return "D6.3 with the clause %s, Pin at every determined pair %s, for %s\n%s\n%s" % (s, pe, k, q.describe(), c.describe())
            d = slot_as_displayed_s106(c, k)
            if d is None:
                tally["displayed has no value"] += 1
            elif d and not s:
                tally["displayed True, D6.3 with the clause False"] += 1
        return None

    part = forall(S, "FC23.new4", 3, "(c) D6.3 with the clause is Pin at every pair of Det_C, transports partial", "Slot_C(ℰ,k) ⟺ Det_C ≠ ∅ ∧ ∀(a,b) ∈ Det_C Pin(ℰ,k;a,b), τ partial and π partial",
                  gen, cc, SMALL, 60, BOTHFAM, ["I16", "I17", "I184"])
    part["note"] = "components where the displayed clause (no translation conjunct) has no value: %d; where it holds and D6.3 with the clause does not: %d" % (
        tally["displayed has no value"], tally["displayed True, D6.3 with the clause False"])
    parts.append(part)
    # (d) a look (B9, R4A2-02): the pole's forward candidate on C2 pins only where the pair's own edit alters c_L
    D = pole()
    C1, C2, _ = pole_contracts(D)
    rows, okd = [], True
    for nm, C in (("C1", C1), ("C2", C2)):
        q = Question(D, C, "b1_45", PortQuery(), "L", name=nm)
        c = pole_fwd_candidate(q)
        ps = pins(c)
        own = [(k, x) for k, x in ps if c.E.L(k, c.tau[x[0]], c.sigma[x[1]]) != c.E.L(k, ONE, c.sigma[x[1]])]
        sl = {qq: slot(c, "c_L", quantifier=qq) for qq in SLOT_QUANTIFIERS}
        rows.append("%s: %d pins, %d at a pair whose own edit alters the pinning component; Slot(c_L) under each reading %s; (E) %s" % (nm, len(ps), len(own), sl, account(c)))
        if nm == "C2":
            okd = okd and bool(ps) and len(own) == len(ps) and not sl["every"] and sl["some"] and not sl["some-exempt"]
        else:
            okd = okd and not ps
    parts.append(look("(d) B9: the pole's pins on C2 are made by the pair's own edit", "every pin of c_L on C2 is at a setting of L, whose edit alters c_L; I136's exempt reading would exempt each (R4A2-02, an other choice of I184 at one pair); (E) reads none",
                      okd, "; ".join(rows), ["I184", "I136"]))
    return parts


def _beh_target():
    """A sign seen at the grain of its behaviour only: one component c, red on Mondays (1), blue on Tuesdays (tue)."""
    return _org("D_beh", ["colour"], {"colour": COLOURS}, ["c"], {"c": ("colour",)}, ["b0"], [ONE, "tue"],
                {("c", ONE, "b0"): {("red",)}, ("c", "tue", "b0"): {("blue",)}})


def _two_parts_org():
    """E_2parts: a red part r (red on Mondays, off, the full relation, on Tuesdays) and a blue part u (the reverse), as I189's ℰ_two."""
    return _org("E_2parts", ["colour"], {"colour": COLOURS}, ["r", "u"], {"r": ("colour",), "u": ("colour",)}, ["b0"], [ONE, "tue"],
                {("r", ONE, "b0"): {("red",)}, ("u", "tue", "b0"): {("blue",)}})


@claim("FC23.new5", ["I14", "I189"])
def fc23_new5(S):
    parts = []
    Db = _beh_target()
    pb = Question(Db, [(ONE, "b0"), ("tue", "b0")], "b0", PortQuery(), "colour", name="p_beh")
    E2 = _two_parts_org()
    # (a) every λ D5.1 allows here: N_k ∈ {∅, {c}}; θ_k the one injection where N_k = {c}; κ_k any value map on COLOURS; τ(tue) ∈ {1, tue}
    maps = [dict(zip(COLOURS, img)) for img in itertools.product(COLOURS, repeat=len(COLOURS))]

    def trans(m):
        return {"colour": Translation(("colour",), fn=(lambda xs, m=m: m[xs[0]]), name="κ%s" % "".join(m[x][0] for x in COLOURS))}
    choices = [(frozenset(), _T("colour"))] + [(frozenset(["c"]), trans(m)) for m in maps]
    n, fails, bad = 0, {}, []
    for tt in ("tue", ONE):
        for lr in choices:
            for lu in choices:
                n += 1
                c = Candidate(E2, pb, _T("colour"), {ONE: ONE, "tue": tt}, {"b0": "b0"}, {"r": lr, "u": lu}, ["r", "u"], "colour", name="ℰ_two on D_beh")
                v, d = account(c, detail=True)
                f1 = {x: F1_at(c, *x) for x in ((ONE, "b0"), ("tue", "b0"))}
                if v or d["F1"]:
                    bad.append("%s" % c.describe())
                key = "fails (F1) at " + ", ".join(sorted("(%s,%s)" % x for x, ok in f1.items() if not ok))
                fails[key] = fails.get(key, 0) + 1
    parts.append(computed("(a) C-K3: the two-part candidate on a target with one part fails (F1) under every λ",
                          "on D_beh (one component c, red on Mondays, blue on Tuesdays) no λ in D5.1's range and no τ(tue) lets ℰ_two meet (F1): a decomposition the target lacks (L245), not a slot",
                          not bad, "λ tried: %d (N_k ∈ {∅, {c}}, κ_k every value map on %s, τ(tue) ∈ {tue, 1}); %s%s" % (n, COLOURS, fails, ("; meets (F1): " + bad[0]) if bad else ""), ["I14", "I189"]))
    # (b) on the same target the one-part candidate meets (E); its part is a slot (the answer written in, S44, S45)
    E1o = _org("E_one", ["colour"], {"colour": COLOURS}, ["k"], {"k": ("colour",)}, ["b0"], [ONE, "tue"],
               {("k", ONE, "b0"): {("red",)}, ("k", "tue", "b0"): {("blue",)}})
    c1 = Candidate(E1o, pb, _T("colour"), {ONE: ONE, "tue": "tue"}, {"b0": "b0"}, {"k": (frozenset(["c"]), _T("colour"))}, ["k"], "colour", name="ℰ_one on D_beh")
    v1, d1 = account(c1, detail=True)
    parts.append(computed("(b) on D_beh the one-part candidate meets (E); its part is a slot", "ℰ_one (k: red on Mondays, blue on Tuesdays, λ(k) = {c}) meets (E) after S106 and Slot_C(ℰ_one, k) holds",
                          v1 and slot(c1, "k"), "conjuncts %s; slot %s" % ({k: d1[k] for k in ("F1", "F2", "A", "Dep", "NC1", "NonVacuous")}, slot(c1, "k")), ["I189"]))
    # (c) on I189's target (the red part and the blue part in the target, as S44's "why is the red part or blue part there") ℰ_two meets (E)
    p = sign_question()
    two = sign_two(p)
    v2, d2 = account(two, detail=True)
    parts.append(computed("(c) on I189's target, where the parts are the target's, ℰ_two meets (E)", "as FC23.new2 (a): which candidate meets (F1) turns on the target's components at the declared grain (L31), not on a slot",
                          v2, "conjuncts %s; the target's components %s" % ({k: d2[k] for k in ("F1", "F2", "A", "Dep", "NC1", "NonVacuous")}, p.D.comps), ["I189"]))
    return parts


@claim("FC42.new1", ["I20", "I29", "I70"])
def fc42_new1(S):
    """(D), D7.4 after round 4, area 2: each v ∈ 𝒱 declares (E_v, t_v, Γ_v, δ_v), δ_v the designation the operation carries δ_E to
    (R4A2-03); Boundary := {(v,w) : Acc((E_v,p,t_v,Γ_v,δ_v)) ≠ Acc((E_w,p,t_w,Γ_w,δ_w))}."""
    parts = []
    D = pole()
    C1, _, _ = pole_contracts(D)
    p = Question(D, C1, "b1_45", PortQuery(), "L", name="p_prod")
    fwd = pole_fwd_candidate(p)
    # 𝒱: the restrictions E|W (D7.1, organization edits deleting commitments; δ_E carried unchanged) and a renaming (D18.2, I70)
    fam = {}
    for W in (("c_H", "c_T", "c_L"), ("c_H", "c_T"), ("c_H", "c_L"), ("c_T", "c_L"), ("c_L",)):
        fam["E|{%s}" % ",".join(W)] = restrict(fwd, W)
    o, pm, cm, bm, am = rename_org(D, random.Random(1070042), suffix="'")
    ren = Candidate(o, p, {pm[v]: Translation((v,)) for v in D.ports}, {a: am[a] for a in D.A}, {b: bm[b] for b in D.B},
                    {cm[j]: (frozenset([j]), {pm[v]: Translation((v,)) for v in D.foot[j]}) for j in D.comps},
                    [cm[j] for j in D.comps], pm["L"], name="ℰ renamed")
    fam["renamed"] = ren
    # (a) with δ_v carried: Boundary is determined
    acc = {v: account(c) for v, c in fam.items()}
    B = boundary(fam)
    parts.append(computed("(a) with δ_v carried by the operation, Boundary is determined", "each v declares (E_v, t_v, Γ_v, δ_v); Acc of each is computed and Boundary is the set of pairs whose Acc differs",
                          bool(B) and acc["renamed"] == acc["E|{c_H,c_T,c_L}"], "designations %s; Acc %s; |Boundary| = %d, e.g. %s"
                          % ({v: c.deltaE for v, c in fam.items()}, acc, len(B), sorted(B)[:3]), ["I20", "I29"]))
    # (b) δ_v not declared: Acc of (E_v, p, t_v, Γ_v) over the designations E_v allows takes both values, so Boundary is no function of the three
    rng_acc = {v: sorted(set(account(c.replace(deltaE=d)) for d in c.E.ports)) for v, c in fam.items()}
    two_valued = [v for v, vals in rng_acc.items() if vals == [False, True]]
    v0, w0 = "E|{c_H,c_T,c_L}", "renamed"
    in_carried = (v0, w0) in B
    alt = {v0: fam[v0].replace(deltaE="H"), w0: fam[w0]}
    in_other = (v0, w0) in boundary(alt)
    parts.append(computed("(b) N1: without δ_v, Acc(E_v, p) and Boundary are not fixed", "for some v the designations E_v allows give Acc both values; the pair (E|Γ, renamed) is in Boundary under one choice of designations and not under another",
                          bool(two_valued) and in_carried != in_other, "Acc over the designations of each E_v: %s; (E|Γ, renamed) in Boundary with δ carried: %s; with δ_{E|Γ} = H: %s"
                          % (rng_acc, in_carried, in_other), ["I20"]))
    # (c) a renaming: δ_E = L is no port of E_v; only the carried designation gives Acc a value
    parts.append(computed("(c) a renaming carries δ_E to a port of E_v", "δ_E = L is not a port of the renamed E_v, so Acc(E_v, p) with δ_E has no value; with δ_v = the port the renaming carries L to, Acc(E_v) = Acc(E)",
                          ("L" not in o.ports) and acc["renamed"] == acc[v0], "renamed ports %s; δ_v = %s; Acc(E_v) %s, Acc(E) %s" % (o.ports, pm["L"], acc["renamed"], acc[v0]), ["I70", "I20"]))
    # (d) a look: the other choice, δ_v quantified (∃δ, as D14.7 and D16.4 quantify δ); an edit that moves the answer onto a
    # new port L2 and leaves L constant, the operation carrying the designation L unchanged
    fam2 = {"E": fwd, "moved": _moved_answer(p)}
    fam2.update(fam)
    B2 = boundary(fam2)
    acc_ex = {v: any(account(c.replace(deltaE=d)) for d in c.E.ports) for v, c in fam2.items()}
    B_ex = frozenset((v, w) for v in fam2 for w in fam2 if acc_ex[v] != acc_ex[w])
    parts.append(look("(d) the other choice: δ_v quantified", "with ∃δ_v the designation may change from edit to edit, against L253's fixed query: the edit that moves the answer onto L2 keeps Acc under ∃δ_v and loses it with δ carried, so Boundary differs",
                      B_ex != B2 and ("E", "moved") in B2 and ("E", "moved") not in B_ex,
                      "Acc with δ carried %s; with ∃δ_v %s; |Boundary| with δ carried %d, with ∃δ_v %d; pairs only with δ carried %s; only under ∃δ_v %s"
                      % ({v: account(c) for v, c in fam2.items()}, acc_ex, len(B2), len(B_ex), sorted(B2 - B_ex)[:4], sorted(B_ex - B2)[:4]), ["I20"]))
    return parts


def _moved_answer(p):
    """An organization edit of the pole's forward organization (E1) that moves the answer onto a new port L2 (m_L2: L2 = H cot θ)
    and leaves L constant (m_L, background); the edit carries t to t_v (π(L2) := L, π(L) := the constant) and the designation
    δ_E = L to itself. Built for FC42.new1 (d)."""
    D = p.D
    inv, bval = D.meta["inv"], D.meta["bval"]
    one = next(x for x in D.dom["L"] if x == 1)
    dom = dict(D.dom)
    dom["L2"] = D.dom["L"]
    ports = ["H", "T", "L", "L2"]
    foot = {"m_H": ("H",), "m_T": ("T",), "m_L2": ("H", "T", "L2"), "m_L": ("L",)}
    home = {"m_H": "H", "m_T": "T", "m_L2": "L2", "m_L": "L"}
    sets = {"H": "H", "T": "T", "L": "L2"}

    def Lfun(j, a, b):
        sm = {sets[v]: x for v, x in dict(inv[a]).items()}
        v = home[j]
        if v in sm:
            i = foot[j].index(v)
            return frozenset(w for w in itertools.product(*[dom[u] for u in foot[j]]) if w[i] == sm[v])
        uH, uT = bval[b]
        if j == "m_H":
            return frozenset([(uH,)])
        if j == "m_T":
            return frozenset([(uT,)])
        if j == "m_L":
            return frozenset([(one,)])
        return frozenset(w for w in itertools.product(dom["H"], dom["T"], dom["L2"]) if w[2] == w[0] * COT[w[1]])

    E = Org("E_moved", ports, dom, ["m_H", "m_T", "m_L2", "m_L"], foot, D.B, D.A, D._compose, Lfun, meta=dict(bval=bval, inv=inv))
    pi = {"H": Translation(("H",)), "T": Translation(("T",)), "L2": Translation(("L",)), "L": Translation(("L",), fn=(lambda xs: one), name="const 1")}
    lam = {"m_H": (frozenset(["c_H"]), {"H": Translation(("H",))}), "m_T": (frozenset(["c_T"]), {"T": Translation(("T",))}),
           "m_L2": (frozenset(["c_L"]), {"H": Translation(("H",)), "T": Translation(("T",)), "L2": Translation(("L",))})}
    return Candidate(E, p, pi, {a: a for a in D.A}, {b: b for b in D.B}, lam, ["m_H", "m_T", "m_L2"], "L", name="ℰ moved")
