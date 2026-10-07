# S108 Part A, section 4: the worked cases (rule 5.1), with Acc and being an explanation (Account ∧ ¬Dec(t) now; each
# variant's reading when on), and the reply's small cases, run. Every value is computed by the program in this folder
# (core.account, core.slot, claims_b's provenance, claims_s41's arguments and defeat sets) or by model/s108_s4*.py.
#   PYTHONHASHSEED=0 python3 -B s108_s4_cases.py > OUT.txt
# Provenance (Θ by hand, I90, as the program's own claims set it; no worked case carries a history of its own except the
# student's copy, the bridge and CT8), one holding of t for each candidate:
#   H0 none recorded: a history with no occurrence (the reply's "no provenance record")
#   Dec: provenance_of(·, 'Dec')  (no selection admitted, no trace)
#   Con: provenance_of(·, 'Con')  (a trace prepares t; cod t represented)
#   Sel: provenance_of(·, 'Sel', H = {(1,b0)})
#   rCon: a relay (content-preserving transfer, D12.3, D12.4) of a constructed holding: chain o1 (trace, held) ≺ o2 (relay of o1)
#   rSel: a relay of a selected holding: o1 (Sel's conditions computed on H = {(1,b0)}) ≺ o2 (relay of o1)
# the chains' provenance by prov_fixed_points under the cut T′ (the program's reading, I162); Held at o1 := Faithful_C(t).
# V4.3's "Sel(t) ∨ CT(t)" at the holding [S108-4-I3]: (a) Sel's conditions with their exclusions at o_t, and CT := a
# construction trace prepares t's holding at o_t (the program's trace[o_t]); (b) the same with CT := a trace's output
# holds t at or before o_t in the chain of transfers; (c) through D12.3's inherited provenance (= now).
import contextlib
import io
import itertools
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from model import core, s108_s4, s108_s4_nec as NEC  # noqa: E402
from model.core import (ONE, BOT, Org, Question, PortQuery, Candidate, Translation, account, slot, pins,  # noqa: E402
                        SLOT_QUANTIFIERS, faithful, F1_at, F2eq_at, hom)
from model.claims_b import (Hist, sel, con, prov_fixed_points, prov_show, faithful_on, fwd_pole_cand,  # noqa: E402
                            _prov_step)
from model import claims_b  # noqa: E402
from model.claims_s41 import provenance_of, suff_defeats, expl_ruled_out, not_using_E, uses, SUFF_READINGS  # noqa: E402
from model.args import Not, Imp, Leaf, Step, Assessor, X  # noqa: E402
from model.cases import pole, pole_fwd_candidate, pole_rev_candidate, single_settings  # noqa: E402
from model.claims_a import pole_contracts, table_candidate  # noqa: E402
from model.claims_s106 import sign_question, sign_two, sign_one  # noqa: E402
from model.claims_r3a2 import elim  # noqa: E402
from model import e9  # noqa: E402

P = print
HISTS = ("H0", "Dec", "Con", "Sel", "rCon", "rSel")
VREADS = ("none", "V4.1", "V4.2", "V4.3a", "V4.3b")


def tf(x):
    return "-" if x is None else ("T" if x else "F")


def chain_prov(c, kind):
    """rCon / rSel: (Dec at o2, Sel's conditions with exclusions at o2, CT (a), CT (b), shown)."""
    held = bool(faithful(c))
    H = [(ONE, c.p.b0)]
    if kind == "rCon":
        trace, selc = [1, 0], [0, 0]
    else:
        trace, selc = [0, 0], [int(bool(set(H) <= set(c.p.C) and faithful_on(c, H))), 0]
    heldv = [int(held), int(held)]
    fps = prov_fixed_points(2, heldv, trace, selc, "T'", True, rec_of=[None, 0])
    if len(fps) != 1:
        return None
    R, sc = fps[0]
    dec = not sc[1][0] and not sc[1][1]
    direct = _prov_step(2, heldv, trace, selc, "T'", True, R)
    sel_d = direct[1][0]
    ct_a = bool(trace[1])
    ct_b = bool(trace[1] or trace[0])
    return dec, sel_d, ct_a, ct_b, prov_show(2, fps)


def prov(c, kind):
    """(Sel, Con, Dec, selct (a), selct (b)) of one holding of t."""
    H = [(ONE, c.p.b0)]
    if kind == "H0":
        h = Hist([], [], set())
        s, k = sel(c, H, h), con(h)
        return s, k, (not s and not k), (s or bool(h.prepares)), (s or bool(h.prepares))
    if kind in ("Dec", "Con", "Sel"):
        s, k, dec = provenance_of(c, kind, H)
        prep = kind == "Con"
        return s, k, dec, (s or prep), (s or prep)
    r = chain_prov(c, kind)
    dec, sel_d, ct_a, ct_b, _ = r
    return None, None, dec, (sel_d or ct_a), (sel_d or ct_b)


def expl_all(acc, dec, slot_every, sa, sb):
    return {"none": s108_s4.expl(acc, dec, variant="none"),
            "V4.1": s108_s4.expl(acc, dec, slot=slot_every, variant="V4.1"),
            "V4.2": s108_s4.expl(acc, dec, variant="V4.2"),
            "V4.3a": bool(acc and not dec and sa),
            "V4.3b": bool(acc and not dec and sb)}


def slot_row(c):
    if getattr(c.p.Q, "kind", None) != "port":
        return None
    return {q: [k for k in c.E.comps if slot(c, k, quantifier=q)] for q in SLOT_QUANTIFIERS}


def collect_worked():
    """The written-in step's case script's candidates (s106_cases.case collected), E6's, and the student's copy."""
    import s106_cases
    got = []
    s106_cases.case = lambda label, where, c, note="": got.append((label, where, c))
    e6 = []
    orig = claims_b.account

    def wrap(c, *a, **k):
        if getattr(c, "name", "") == "ℰ_Leibniz" and core.ACCOUNT_READING == "S106":
            e6.append(c)
        return orig(c, *a, **k)
    claims_b.account = wrap
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            s106_cases.main()
    finally:
        claims_b.account = orig
        core.ACCOUNT_READING = "S106"
    for i, c in enumerate(e6):
        got.append(("E6 skew-symmetric, Leibniz candidate (%s)" % ("c-i" if i == 0 else "c-ii"), "L343; FC63", c))
    p, c = fwd_pole_cand()
    got.append(("the student's copy's candidate (pole, T at 45)", "L17, L536; FC30.new1", c))
    return got


def main():
    P("S108 Part A, section 4: the worked cases, Acc and being an explanation under each reading; the reply's small cases")
    P("variants' switch: s108_s4 (this run computes every reading explicitly; S108_S4_VARIANT = %s)" % s108_s4.VARIANT)
    P("=" * 150)
    cases = collect_worked()
    P("§1 Worked cases (%d): Acc; Slot (the components that are slots under every / some / some-exempt / some-exempt-set);" % len(cases))
    P("   Expl under (none, V4.1, V4.2, V4.3a, V4.3b) for each hand-set history H0, Dec, Con, Sel, rCon, rSel")
    moves = {v: [] for v in VREADS[1:]}
    moves_by_hist = {(v, h): 0 for v in VREADS[1:] for h in HISTS}
    decs = {h: [] for h in HISTS}
    for label, where, c in cases:
        acc, d = account(c, detail=True)
        sr = slot_row(c)
        s_every = bool(sr and sr["every"])
        P("%-62s %-24s Acc %s  slots %s" % (label[:62], where[:24], tf(acc),
                                          "n/a (not a port query, I82)" if sr is None else "; ".join("%s %s" % (q, sr[q] or "none") for q in SLOT_QUANTIFIERS)))
        row = []
        for h in HISTS:
            s, k, dec, sa, sb = prov(c, h)
            decs[h].append(dec)
            ex = expl_all(acc, dec, s_every, sa, sb)
            for v in VREADS[1:]:
                if ex[v] != ex["none"]:
                    moves[v].append((label, h, ex["none"], ex[v]))
                    moves_by_hist[(v, h)] += 1
            row.append("%s: Dec %s, Sel∨CT a/b %s/%s -> %s" % (h, tf(dec), tf(sa), tf(sb), "".join(tf(ex[v]) for v in VREADS)))
        P("      " + " | ".join(row[:3]))
        P("      " + " | ".join(row[3:]))
    P("-" * 150)
    P("Dec(t) per history over the %d cases: %s" % (len(cases), "; ".join("%s %d of %d" % (h, sum(1 for x in decs[h] if x), len(decs[h])) for h in HISTS)))
    for v in VREADS[1:]:
        P("%s: (case, history) pairs whose being an explanation moves: %d; per history %s" % (
            v, len(moves[v]), ", ".join("%s %d" % (h, moves_by_hist[(v, h)]) for h in HISTS)))
        for label, h, a, b in moves[v]:
            if h in ("Con", "Dec", "rSel", "rCon") or v == "V4.1":
                pass
        cs = sorted(set(l for l, _, _, _ in moves[v]))
        P("   cases that move under some history: %d: %s" % (len(cs), "; ".join(cs)))
    P("   (the other variants, V4.4-V4.8, read nothing being an explanation reads: s108_s4.expl returns now's value for them)")
    for v in ("V4.4", "V4.5", "V4.6", "V4.7", "V4.8"):
        same = all(s108_s4.expl(a, d_, variant=v) == s108_s4.expl(a, d_, variant="none") for a in (False, True) for d_ in (False, True))
        P("   %s: Expl equal to now's on the four values of (Acc, Dec): %s" % (v, same))

    # the student's copy, computed as FC30.new1 (d), (e), (f) compute it
    P("=" * 150)
    P("§2 The student's copy (FC30.new1 (d), (f)) and a link no pair tried (FC30.new1 (e)): provenance computed on the chain, then Expl")
    p, c = fwd_pole_cand()
    acc = account(c)
    held = bool(faithful(c))
    Hx = [(ONE, "b1_45")]
    selc_o = faithful_on(c, Hx)
    fps = prov_fixed_points(2, [1, held], [1, 0], [0, selc_o], "T'", True)
    R, sc = fps[0]
    dec_d = not sc[1][0] and not sc[1][1]
    selct_d = bool(sc[1][0] or sc[1][1])  # o2 is no transfer: Sel ∨ CT there is ¬Dec (D12.3)
    ex = expl_all(acc, dec_d, False, selct_d, selct_d)
    P("(d) the student's holding o2 (source o1 constructed; no trace at o2; H = {(1,b1_45)} tried): fixed points %s; Dec %s; Expl (none, V4.1, V4.2, V4.3a, V4.3b) %s"
      % (prov_show(2, fps), dec_d, "".join(tf(ex[v]) for v in VREADS)))
    fpsK = prov_fixed_points(2, [1, 1], [1, 0], [0, 0], "T'", True, rec_of=[None, 0])
    RK, scK = fpsK[0]
    decK = not scK[1][0] and not scK[1][1]
    dirK = _prov_step(2, [1, 1], [1, 0], [0, 0], "T'", True, RK)
    exK = expl_all(acc, decK, False, dirK[1][0] or False, True)
    P("(f) K3's reading (the component alone, transferred from o1): fixed points %s; Dec %s; Sel at o2 read as a holding %s; trace at o2 0, at o1 1; Expl %s"
      % (prov_show(2, fpsK), decK, dirK[1][0], "".join(tf(exK[v]) for v in VREADS)))
    for hn in (False, True):
        selc0 = sel(c, [], Hist([], [], set(c.p.C)), h_nonempty=hn)
        fps0 = prov_fixed_points(1, [held], [0], [selc0], "T'", True)
        dec0 = all(not s_[0][0] and not s_[0][1] for _, s_ in fps0)
        ex0 = expl_all(acc, dec0, False, not dec0, not dec0)
        P("(e) a link no pair tried, D12.1 %s: Dec %s; Expl %s" % ("with H ≠ ∅" if hn else "with H = ∅ allowed", dec0, "".join(tf(ex0[v]) for v in VREADS)))

    small_cases()


def pole_q(C, name, D=None):
    D = D or pole()
    return Question(D, C, "b1_45", PortQuery(), "L", name=name)


def small_cases():
    P("=" * 150)
    P("§3 The reply's small cases, run (every 'after' was marked not run by the reply)")
    D = pole()
    C1, C2, _ = pole_contracts(D)
    CH = frozenset([(ONE, "b1_45")] + [(a, "b1_45") for a in single_settings(D, ["H"])])
    from model.claims_r4a2 import _tau_prime
    t2 = _tau_prime(D)
    p1, p2, pH = pole_q(C1, "C1", D), pole_q(C2, "C2", D), pole_q(CH, "C_H", D)
    rH = pole_rev_candidate(pH)
    rH = rH.replace(tau={a: t2[a] for a in sorted(set(x for x, _ in CH), key=repr)}, name="ℰ_rev τ' (C_H)")
    ps = sign_question()
    V41 = [("ℰ_one (sign, one part)", sign_one(ps)), ("ℰ_two (sign, two parts)", sign_two(ps)),
           ("E_enc pole C1", table_candidate(p1, list(D.ports), encode=True)), ("E_enc pole C2", table_candidate(p2, list(D.ports), encode=True)),
           ("E_rev under τ' on C_H", rH), ("pole forward C1", pole_fwd_candidate(p1)), ("pole forward C2", pole_fwd_candidate(p2))]
    P("V4.1 (Expl gains ¬Slot): with a constructed transport (Con, ¬Dec)")
    for nm, c in V41:
        acc = account(c)
        sr = slot_row(c)
        s, k, dec = provenance_of(c, "Con", [(ONE, c.p.b0)])
        pn = pins(c)
        per_q = {q: s108_s4.expl(acc, dec, slot=bool(sr[q]), variant="V4.1") for q in SLOT_QUANTIFIERS}
        P("   %-26s Acc %s; pins %d (by %s); slots %s; Expl now %s; V4.1 under (every, some, some-exempt, some-exempt-set) %s"
          % (nm, tf(acc), len(pn), sorted(set(x for x, _ in pn)) or "-", {q: sr[q] for q in SLOT_QUANTIFIERS},
             tf(s108_s4.expl(acc, dec, variant="none")), "".join(tf(per_q[q]) for q in SLOT_QUANTIFIERS)))
    # (Suff): FC30.new1 (c)'s common model and the defeat set, V4.1 kept vs covaried
    P("   (Suff) and V4.1: ℰ_one constructed, with an argument not using (E) that rules out Expl(ℰ_one):")
    c = sign_one(ps)
    acc = account(c)
    s, k, dec = provenance_of(c, "Con", [(ONE, "b0")])
    j = Assessor(["MP"], ["r", Imp("r", Not("Expl_" + c.name))])
    out, _ = expl_ruled_out(j, c.name)
    old = s108_s4.V41_SUFF
    for sub in ("kept", "covaried"):
        s108_s4.V41_SUFF = sub
        d = {r: bool(s108_s4.suff_antecedent(acc, dec, r, slot=True, variant="V4.1") and out) for r in SUFF_READINGS}
        ex = s108_s4.expl(acc, dec, slot=True, variant="V4.1")
        conj = (not s108_s4.suff_conjecture(acc, dec, slot=True, variant="V4.1")) or ex
        P("      (Suff) %s: in the defeat set %s; Expl %s; (Suff) as conjectured holds of ℰ_one %s" % (sub, d, ex, conj))
    s108_s4.V41_SUFF = old

    P("V4.2 (Expl := Acc): the student's declared copy (FC30.new1 (a)), with the argument from a record ruling out Expl")
    p, c = fwd_pole_cand()
    acc = account(c)
    j = Assessor(["MP"], ["r", Imp("r", Not("Expl_" + c.name))])
    out, _ = expl_ruled_out(j, c.name)
    old = s108_s4.V42_SUFF
    for kind in ("Dec", "Con"):
        s, k, dec = provenance_of(c, kind, [(ONE, "b1_45")])
        row = []
        for sub in ("rule", "L17", "both"):
            s108_s4.V42_SUFF = sub
            d = {r: bool(s108_s4.suff_antecedent(acc, dec, r, variant="V4.2") and out) for r in SUFF_READINGS}
            row.append("%s: Def %s; Def(L17,S41) = Def(L536) %s" % (sub, {r[:9]: d[r] for r in SUFF_READINGS}, d["L17 (S41)"] == d["L536"]))
        s108_s4.V42_SUFF = old
        P("   %s: Acc %s, Dec %s; Expl now %s, V4.2 %s; the owner's condition Acc ∧ Dec ⇒ ¬Expl under V4.2: %s" % (
            kind, tf(acc), tf(dec), tf(s108_s4.expl(acc, dec, variant="none")), tf(s108_s4.expl(acc, dec, variant="V4.2")),
            not (acc and dec and s108_s4.expl(acc, dec, variant="V4.2"))))
        for r in row:
            P("      " + r)

    P("V4.3 (¬Dec(t) → ¬Dec(t) ∧ (Sel ∨ CT)): E_enc and E_rev τ' with no provenance record (H0), and relays")
    for nm, c in (("E_enc pole C1", table_candidate(p1, list(D.ports), encode=True)), ("E_rev under τ' on C_H", rH)):
        acc = account(c)
        for h in ("H0", "Con", "Sel", "rCon", "rSel"):
            s, k, dec, sa, sb = prov(c, h)
            ex = expl_all(acc, dec, False, sa, sb)
            P("   %-24s %-5s Acc %s; Dec %s; Sel ∨ CT (a) %s, (b) %s; Expl now %s, V4.3a %s, V4.3b %s" % (
                nm, h, tf(acc), tf(dec), tf(sa), tf(sb), tf(ex["none"]), tf(ex["V4.3a"]), tf(ex["V4.3b"])))
    P("   E9's t1 (Con) and t0 (Sel), by hand:")
    D9 = e9.object_layer()
    C9 = [(a, b) for a in D9.A for b in D9.B]
    p9 = e9.question(D9, C9)
    t1 = e9.t1_candidate(p9, e9.sim_layer_S1())
    a1 = account(t1)
    for h in ("Con", "Sel", "rCon"):
        s, k, dec, sa, sb = prov(t1, h)
        ex = expl_all(a1, dec, False, sa, sb)
        P("      t1 %-5s Acc %s; Dec %s; Expl now %s, V4.3a %s, V4.3b %s" % (h, tf(a1), tf(dec), tf(ex["none"]), tf(ex["V4.3a"]), tf(ex["V4.3b"])))

    P("V4.4 ('not using (E)' at the instance): arguments whose only use of (E) is another candidate's Acc")
    p, c = fwd_pole_cand()
    rev = pole_rev_candidate(c.p)
    acc = account(c)
    e = "Expl_" + c.name
    a_other = "Acc_" + rev.name
    gamma = Step("MP", Not(e), [Leaf(a_other), Leaf(Imp(a_other, Not(e)))])
    jh = Assessor(["MP"], [a_other, Imp(a_other, Not(e))])
    xh = X(jh, e, [gamma])
    for kind in ("Con", "Dec", "Sel"):
        s, k, dec = provenance_of(c, kind, [(ONE, "b1_45")])
        ins = {rd: suff_defeats(acc, dec, bool([a for a in xh if not_using_E(a, c.name, rd)]), "L536") for rd in ("symbol", "instance")}
        P("   (Suff), FC30.new1 (h)'s argument [Acc(ℰ_rev), Acc(ℰ_rev) → ¬Expl(ℰ_fwd)], ℰ_fwd %s (Dec %s): usable %s; in the defeat set: symbol %s, instance %s"
          % (kind, dec, bool(xh), ins["symbol"], ins["instance"]))
    # t1 and t1∘ψ (E9, FC103.new1): an argument citing Acc(t1) against Expl(t1∘ψ)
    t1s = e9.t1_candidate(p9, e9.sim_layer_S1(), swapped=True)
    a_t1s = account(t1s)
    e2 = "Expl_" + t1s.name
    g2 = Step("MP", Not(e2), [Leaf("Acc_" + t1.name), Leaf(Imp("Acc_" + t1.name, Not(e2)))])
    j2 = Assessor(["MP"], ["Acc_" + t1.name, Imp("Acc_" + t1.name, Not(e2))])
    x2 = X(j2, e2, [g2])
    s, k, dec = provenance_of(t1s, "Con", [(ONE, t1s.p.b0)])
    ins2 = {rd: suff_defeats(a_t1s, dec, bool([a for a in x2 if not_using_E(a, t1s.name, rd)]), "L536") for rd in ("symbol", "instance")}
    P("   (Suff), E9: [Acc(t1), Acc(t1) → ¬Expl(t1∘ψ)], t1∘ψ constructed: Acc(t1) %s, Acc(t1∘ψ) %s; usable %s; in the defeat set: symbol %s, instance %s"
      % (a1, a_t1s, bool(x2), ins2["symbol"], ins2["instance"]))
    # (Nec) side: an argument citing Acc(ℰ_fwd) rules out ¬Expl(ℰ_rev); exposure now and under V4.5
    er = "Expl_" + rev.name
    beta = Step("MP", er, [Leaf("Acc_" + c.name), Leaf(Imp("Acc_" + c.name, er))])
    jb = Assessor(["MP"], ["Acc_" + c.name, Imp("Acc_" + c.name, er)])
    xb = X(jb, Not(er), [beta])
    nu = {rd: bool([a for a in xb if not_using_E(a, rev.name, rd)]) for rd in ("symbol", "instance")}
    P("   (Nec), the pole (T at 45): [Acc(ℰ_fwd), Acc(ℰ_fwd) → Expl(ℰ_rev)] rules out ¬Expl(ℰ_rev): usable %s; not using (E): symbol %s, instance %s (the defeat asks exposure too: §4)"
      % (bool(xb), nu["symbol"], nu["instance"]))

    P("V4.5 ((Nec)'s exposure on C alone): the class searched is S108-4-I5 (model/s108_s4_nec.py)")
    rev1 = pole_rev_candidate(p1)
    rows = [("E_rev under τ on C1", rev1, C1), ("E_rev under τ' on C1", rev1.replace(tau={a: x for a, x in t2.items() if x is not None}), C1),
            ("E_rev under τ' on C_H", rH, CH), ("pole forward on C1", pole_fwd_candidate(p1), C1)]
    for nm, kind in (("E5 eliminative, FC62's encoding", "const"), ("E5 eliminative, the second encoding", "two")):
        _p, ce = elim(kind)
        rows.append((nm, ce, ce.p.C))
    for nm, c, C in rows:
        en, wb, st = NEC.exposed_none(c.p.D, c.E, list(c.Gamma), time_cap=120)
        e5, w5, st5 = NEC.exposed_v45(c.p.D, c.E, list(c.Gamma), C, time_cap=300)
        P("   %-36s Acc %s; Faithful_C(t) %s; exposed now %s%s; exposed under V4.5 %s%s" % (
            nm, tf(account(c)), tf(faithful(c)), tf(en), (" (a faithful t' on {(1,%s)})" % wb) if wb else (" (" + st + ")" if st else ""),
            tf(e5), (" (witness: %s)" % w5[:160]) if w5 else (" (" + st5 + ")" if st5 else " (no t' in the class)")))

    P("V4.6 (𝔈_Θ without 'δ the designation of Q in c'): Acc with each port of E as δ")
    for Dx, nm in ((D, "the pole (T ∈ {30,45,60})"), (fwd_pole_cand()[0].D, "the pole with T at 45 (FC30.new1's)")):
        for Cn, C in ((("C1", C1) if Dx is D else ("C_H", fwd_pole_cand()[0].C)),):
            q = Question(Dx, C, "b1_45", PortQuery(), "L", name=Cn)
            c = pole_fwd_candidate(q)
            res = {v: account(c.replace(deltaE=v)) for v in Dx.ports}
            P("   %s, forward candidate on %s: Acc with δ_E = %s; designated (π reads L): L" % (nm, Cn, res))
    P("   the generated search: s108_s4_worlds.py")

    P("V4.8 (Underdet without surv; (Prov)(i)'s middle conjunct read through it): FC80 (d)'s witness shape, built on the pole")
    v48_case()


def v48_case():
    """A selected t on H, a member t' altered at an unseen pair's image that also sits in H's image (so t' does not survive),
    and the survivors agreeing there: (Prov)(i) now and under V4.8."""
    from model.claims_b import faithful_on as fo
    p, c = fwd_pole_cand()
    D = p.D
    H = [(ONE, "b1_45")]
    # value at a pair (I71): (τ(a), σ(b), relations of E there)
    def value(t, a, b):
        return (t.tau[a], t.sigma[b], tuple(t.E.L(k, t.tau[a], t.sigma[b]) for k in t.E.comps))
    # t' = t with c_L's relation altered at (1, b1_45): the unseen pairs' images differ from (1,b1_45)'s, so choose an
    # alteration at the image of an unseen pair (a,b) ∉ H; and t'' altered at H's image (does not survive)
    unseen = [x for x in sorted(p.C, key=repr) if x not in H]
    a, b = unseen[0]
    E = c.E

    def alter(k, xE, w, name):
        E2 = Org("E_alt", E.ports, E.dom, E.comps, E.foot, E.B, E.A, E._compose,
                 (lambda k_, x_, w_: (lambda j, a_, b_: (E.L(j, a_, b_) ^ {w_}) if (j, a_, b_) == (k_, x_[0], x_[1]) else E.L(j, a_, b_)))(k, xE, w))
        return c.replace(E=E2, name=name)
    w = sorted(E.full("c_L"))[0]
    t_diff = alter("c_L", (c.tau[a], c.sigma[b]), w, "t_ab")  # altered at (a,b)'s image only
    E3 = Org("E_alt2", E.ports, E.dom, E.comps, E.foot, E.B, E.A, E._compose,
             (lambda j, a_, b_: (E.L(j, a_, b_) ^ {w}) if (j, (a_, b_)) in (("c_L", (ONE, "b1_45")), ("c_L", (c.tau[a], c.sigma[b]))) else E.L(j, a_, b_)))
    t_nonsurv_diff = c.replace(E=E3, name="t_ab,H")
    pop = [c, t_nonsurv_diff]
    surv = [t for t in pop if fo(t, H)]
    agree = len(set(value(t, a, b) for t in surv)) == 1
    s_now = any(fo(t, H) and value(t, a, b) != value(c, a, b) for t in pop)
    s_v48 = any(value(t, a, b) != value(c, a, b) for t in pop)
    sel_t = sel(c, H, Hist(["o1"], [], set(p.C), admitted=True, prepares=False))
    P("   𝒯 = {t, t_ab,H} (t_ab,H: c_L altered at H's image and at (τ(a),σ(b)) for (a,b) = %r ∉ H); Sel(t) on H %s; t_ab,H survives on H %s;" % ((a, b), sel_t, fo(t_nonsurv_diff, H)))
    P("   survivors on H agree at (a,b) (value a function of (𝒯,H)) %s; a differing surviving member (now's middle conjunct) %s; a differing member (V4.8's Underdet) %s"
      % (agree, s_now, s_v48))
    P("   (Prov)(i): now %s; under V4.8 %s" % (sel_t and s_now and agree, sel_t and s_v48 and agree))
    t_ab_surv = fo(t_diff, H)
    P("   FC80 (d)'s other shape: t altered at (τ(a),σ(b)) only survives on H: %s (then now's middle conjunct holds and the value is no function of (𝒯,H): (Prov)(i) fails both ways)" % t_ab_surv)


if __name__ == "__main__":
    main()
