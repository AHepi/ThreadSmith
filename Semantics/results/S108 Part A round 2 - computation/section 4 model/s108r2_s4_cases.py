# S108 Part A round 2, section 4 (rule 5 of the round-2 reading rule; after S56 one Opus agent computes every section): the
# round-2 variants of section 4 (R2V4.1-R2V4.10) on the worked cases, the owner's cases and the reply's small cases, and
# round 1's claimed-only edges of the share (e4.22, e4.40). Every value is computed by the program in this folder
# (core, claims_b, claims_s41, args, e9) or by round 1's section-4 script (s108_s4_cases, imported, unchanged).
#   PYTHONHASHSEED=0 python3 -B s108r2_s4_cases.py > OUT.txt
# Inventions of this computation (S36), S108r2-4-In in the results file:
#   I1  R2V4.4: a worked case "has a named trial history" when (1, b0) ∈ C and t is faithful there (the one tried pair H0 =
#       {(1, b0)}); o1 then a selection on H0, else o1 declared; o2 a relay of o1 (D12.3, D12.4), cut T′.
#   I2  R2V4.7: "not statable" read as: no declared input, so no step by a declared form and no accepted premise; usable
#       false for every α (model/s108r2_s4.py).
#   I3  R2V4.3 (e): the chain's holdings all hold t's content (D11.2); (e) at o_t := some holding o of the chain, held, with
#       Sel's conditions (their exclusions, D12.1) or a trace at o.
#   I4  e4.40: the four sentences read at their own wording on the pole case (R2-4-I7), 𝒯 = {t, t_ab, t_ab,H} (round 1's
#       FC80 (d) shapes), at every unseen pair of C.
import contextlib
import io
import itertools
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from model import core, s108_s4, s108r2_s4  # noqa: E402
from model.core import ONE, Org, Question, PortQuery, account, slot, faithful, SLOT_QUANTIFIERS, A_at, F1_at, F2eq_at, hom  # noqa: E402
from model.claims_b import Hist, sel, con, prov_fixed_points, prov_show, faithful_on, fwd_pole_cand, _prov_step, dep_cycle, DEP  # noqa: E402
from model.claims_s41 import provenance_of, suff_defeats, expl_ruled_out, SUFF_READINGS  # noqa: E402
from model.args import Not, Imp, Leaf, Step, Assessor, X, usable  # noqa: E402
from model.cases import pole, single_settings  # noqa: E402
from model.claims_a import pole_contracts  # noqa: E402
from model.claims_s106 import sign_question, sign_two, sign_one  # noqa: E402
from model import e9  # noqa: E402
import s108_s4_cases as R1  # noqa: E402

P = print
HISTS = ("H0", "Dec", "Con", "Sel", "rCon", "rSel")


def tf(x):
    return "-" if x is None else ("T" if x else "F")


def cases_all():
    with contextlib.redirect_stdout(io.StringIO()):
        cs = R1.collect_worked()
    labels = [l for l, _, _ in cs]
    if not any("ℰ_two" == getattr(c, "name", "") for _, _, c in cs):
        cs.append(("the owner's two-part sign ℰ_two (S44)", "S44; FC23.new2", sign_two()))
    if not any("ℰ_one" == getattr(c, "name", "") for _, _, c in cs):
        cs.append(("the one-part sign ℰ_one", "S44; FC23.new2", sign_one()))
    return cs


def r2v41(cases):
    P("=" * 150)
    P("§1 R2V4.1: being an explanation := Acc ∧ ¬Dec(t) ∧ ¬Slot_C(ℰ), Slot under each quantifier of D6.3; (Suff) as conjectured")
    P("   (antecedent ⇒ Expl) with the antecedent kept (Acc ∧ ¬Dec) and co-varied (Acc ∧ ¬Dec ∧ ¬Slot). Histories as round 1 (I90).")
    P("-" * 150)
    tot = {q: {"drop": 0, "suff_fail_kept": 0, "suff_fail_cov": 0, "cases": set()} for q in SLOT_QUANTIFIERS}
    for label, where, c in cases:
        acc = account(c)
        sr = R1.slot_row(c)
        if sr is None:
            continue
        row = []
        for q in SLOT_QUANTIFIERS:
            s = bool(sr[q])
            for h in HISTS:
                _, _, dec, _, _ = R1.prov(c, h)
                now = bool(acc and not dec)
                v = bool(acc and not dec and not s)
                if now != v:
                    tot[q]["drop"] += 1
                    tot[q]["cases"].add(label)
                if (acc and not dec) and not v:
                    tot[q]["suff_fail_kept"] += 1
                if (acc and not dec and not s) and not v:
                    tot[q]["suff_fail_cov"] += 1
            row.append("%s %s" % (q, sr[q] or "none"))
        if any(sr[q] for q in SLOT_QUANTIFIERS) and acc:
            P("   %-58s Acc %s; slots: %s" % (label[:58], tf(acc), "; ".join(row)))
    P("-" * 150)
    for q in SLOT_QUANTIFIERS:
        P("   %-16s (case, history) whose being an explanation drops: %3d; (Suff) as conjectured fails, antecedent kept: %3d, co-varied: %d; cases: %d"
          % (q, tot[q]["drop"], tot[q]["suff_fail_kept"], tot[q]["suff_fail_cov"], len(tot[q]["cases"])))
    for q in SLOT_QUANTIFIERS[1:]:
        extra = sorted(tot[q]["cases"] - tot["every"]["cases"])
        P("   beyond 'every' under %s: %s" % (q, "; ".join(extra) or "none"))
    # the reply's small case: ℰ_two, constructed, j with r and r → ¬Expl_two
    c = sign_two()
    acc = account(c)
    s, k, dec = provenance_of(c, "Con", [(ONE, c.p.b0)])
    j = Assessor(["MP"], ["r", Imp("r", Not("Expl_two"))])
    out, _ = expl_ruled_out(j, "two")
    for q in SLOT_QUANTIFIERS:
        sl = R1.slot_row(c)[q]
        e = bool(acc and not dec and not sl)
        P("   ℰ_two (Con history), %-16s: Acc %s, Dec %s, slots %s, Expl %s; in Def(L536) kept %s, co-varied %s; (Suff) as conjectured (kept) %s"
          % (q, tf(acc), tf(dec), sl or "none", tf(e), tf(bool(acc and not dec and out)), tf(bool(acc and not dec and not sl and out)),
             "holds" if (not (acc and not dec) or e) else "FAILS"))


def r2v42():
    P("=" * 150)
    P("§2 R2V4.2: Expl := Acc, (Suff)'s shape 'both'; the reply's small case: the student's declared copy, α = MP on r and r → ¬Expl")
    P("-" * 150)
    p, c = fwd_pole_cand()
    acc = account(c)
    held = bool(faithful(c))
    Hx = [(ONE, "b1_45")]
    fps = prov_fixed_points(2, [1, held], [1, 0], [0, faithful_on(c, Hx)], "T'", True)
    R, sc = fps[0]
    dec = not sc[1][0] and not sc[1][1]
    j = Assessor(["MP"], ["r", Imp("r", Not("Expl_dec"))])
    out, alpha = expl_ruled_out(j, "dec")
    P("   ℰ_dec: Acc %s; the copy's holding o2 (source constructed, no trace at o2, H = {(1,b1_45)}): fixed points %s, Dec %s; α usable, not using (E), rules out Expl: %s"
      % (tf(acc), prov_show(2, fps), tf(dec), tf(out)))
    save = (s108_s4.VARIANT, s108_s4.V42_SUFF)
    try:
        for v, shape in (("none", "rule"), ("V4.2", "rule"), ("V4.2", "L17"), ("V4.2", "both")):
            s108_s4.VARIANT, s108_s4.V42_SUFF = v, shape
            ex = s108_s4.expl(acc, dec)
            mem = {r: suff_defeats(acc, dec, out, r) for r in SUFF_READINGS}
            P("   %-5s %-5s Expl(ℰ_dec) %s; in Def: %s; (Suff) as conjectured (antecedent at L536 ⇒ Expl) %s"
              % (v, shape if v != "none" else "", tf(ex), "; ".join("%s %s" % (r, tf(m)) for r, m in mem.items()),
                 "holds" if (not s108_s4.suff_conjecture(acc, dec) or ex) else "FAILS"))
    finally:
        s108_s4.VARIANT, s108_s4.V42_SUFF = save
    P("   α's tree: %s; its leaves %s (the leaf r is labelled 'record' by the program; R2-4-I2 reads it as a reason: the tree and every value are the same)"
      % (alpha.concl, [str(l.claim) for l in alpha.leaves()]))


def r2v43_chains():
    P("=" * 150)
    P("§3 R2V4.3, reading (e) at the content: every chain n ≤ 3 (held, trace, Sel's conditions per holding; each later holding a relay")
    P("   of an earlier one or not), cut T′: ¬Dec at the last holding against (e), (a) at the holding, (b) along transfers")
    P("-" * 150)
    n_tot = n_fp = 0
    diff = {"e": 0, "a": 0, "b": 0}
    ex = {"e": None, "a": None, "b": None}
    for n in (1, 2, 3):
        rec_choices = [[None]] + [list(range(o)) + [None] for o in range(1, n)]
        for held in itertools.product([0, 1], repeat=n):
            for trace in itertools.product([0, 1], repeat=n):
                for selc in itertools.product([0, 1], repeat=n):
                    for rec in itertools.product(*rec_choices):
                        n_tot += 1
                        fps = prov_fixed_points(n, list(held), list(trace), list(selc), "T'", True, rec_of=list(rec))
                        if len(fps) != 1:
                            continue
                        n_fp += 1
                        R, sc = fps[0]
                        last = n - 1
                        nd = bool(sc[last][0] or sc[last][1])
                        direct = _prov_step(n, list(held), list(trace), list(selc), "T'", True, R)
                        e = any(held[o] and (direct[o][0] or trace[o]) for o in range(n))
                        a = bool(direct[last][0] or trace[last])
                        o, back = last, [last]
                        while rec[o] is not None:
                            o = rec[o]
                            back.append(o)
                        b = bool(direct[last][0]) or any(trace[x] for x in back)
                        for k, v in (("e", e), ("a", a), ("b", b)):
                            if (nd and v) != nd:
                                diff[k] += 1
                                if ex[k] is None:
                                    ex[k] = dict(n=n, held=held, trace=trace, selc=selc, rec=rec, prov=prov_show(n, fps))
    P("   chains: %d; with one fixed point under T′: %d" % (n_tot, n_fp))
    for k in ("e", "a", "b"):
        P("   reading (%s): holdings where ¬Dec ∧ (Sel ∨ CT) ≠ ¬Dec: %d%s" % (k, diff[k], ("; smallest: %s" % ex[k]) if ex[k] else ""))


def r2v44(cases):
    P("=" * 150)
    P("§4 R2V4.4: histories built as chains (S108r2-4-I1): o1 a selection on the case's tried pair (1, b0) where t is faithful there, else declared;")
    P("   o2 a relay of o1; cut T′. Being an explanation now, and under round 1's V4.3 (a) at the holding")
    P("-" * 150)
    n = nt = now_t = a_t = 0
    for label, where, c in cases:
        acc = account(c)
        if not acc:
            continue
        n += 1
        H = [(ONE, c.p.b0)]
        trial = bool((ONE, c.p.b0) in c.p.C and faithful_on(c, H))
        nt += trial
        held = bool(faithful(c))
        fps = prov_fixed_points(2, [int(held), int(held)], [0, 0], [int(trial), 0], "T'", True, rec_of=[None, 0])
        R, sc = fps[0]
        dec = not sc[1][0] and not sc[1][1]
        direct = _prov_step(2, [int(held), int(held)], [0, 0], [int(trial), 0], "T'", True, R)
        now_t += (not dec)
        a_t += bool(not dec and (direct[1][0] or False))
    P("   worked candidates meeting (E): %d; with a named trial history (I1): %d; explanations now on the chain: %d; under V4.3 (a): %d"
      % (n, nt, now_t, a_t))
    p, c = fwd_pole_cand()
    H = [(ONE, "b1_45")]
    held = bool(faithful(c))
    for name, selc0, trace0 in (("FC30.new1 (d)'s chain: o1 constructed", 0, 1), ("R2V4.4: o1 a selection on H = {(1,b1_45)}", int(faithful_on(c, H)), 0)):
        fps = prov_fixed_points(2, [1, int(held)], [trace0, 0], [selc0, 0], "T'", True, rec_of=[None, 0])
        R, sc = fps[0]
        dec = not sc[1][0] and not sc[1][1]
        direct = _prov_step(2, [1, int(held)], [trace0, 0], [selc0, 0], "T'", True, R)
        P("   the pole's forward candidate, %s, o2 a relay of o1: fixed points %s; Dec at o2 %s; Expl now %s; V4.3 (a) %s"
          % (name, prov_show(2, fps), tf(dec), tf(account(c) and not dec), tf(account(c) and not dec and bool(direct[1][0] or 0))))
    fps = prov_fixed_points(2, [1, int(held)], [1, 0], [0, 0], "T'", True)
    R, sc = fps[0]
    P("   the same with o2 not a relay (the student's holding as FC30.new1 (d) computes it): fixed points %s; Dec at o2 %s" % (prov_show(2, fps), tf(not sc[1][0] and not sc[1][1])))


def r2v45():
    P("=" * 150)
    P("§5 R2V4.5: E9's question with Q_id, the set query (x1_3, x2_3) (R2-4-I5), against the occupancy query o1_3")
    P("-" * 150)
    D = e9.object_layer()
    C = [(a, b) for a in D.A for b in D.B]
    E = e9.sim_layer_S1()
    for qname in ("occupancy o1_3 (now)", "Q_id (R2V4.5)"):
        if qname.startswith("Q_id"):
            p = Question(D, C, e9.BOUNDS[0], s108r2_s4.q_id(), "o1_3", name="p_E9_id")
        else:
            p = e9.question(D, C)
        t1, t1s = e9.t1_candidate(p, E), e9.t1_candidate(p, E, swapped=True)
        psiC = {(e9.psi_edit(a), e9.psi_bound(b)) for (a, b) in C} == set(C)
        ans_sym = sum(1 for (a, b) in C if p.ans(a, b) != p.ans(e9.psi_edit(a), e9.psi_bound(b)))
        failA = [sum(1 for (a, b) in C if not A_at(t, a, b)) for t in (t1, t1s)]
        sep = 0
        for (a, b) in C:
            v1 = F1_at(t1, a, b) and F2eq_at(t1, a, b) and A_at(t1, a, b)
            v2 = F1_at(t1s, a, b) and F2eq_at(t1s, a, b) and A_at(t1s, a, b)
            sep += v1 != v2
        acc1, acc2 = account(t1), account(t1s)
        P("   %-22s ψ[C] = C %s; pairs with Ans_p∘ψ ≠ Ans_p %d of %d; (A) fails: t1 %d, t1∘ψ %d; separating pairs %d; Acc: t1 %s, t1∘ψ %s"
          % (qname, psiC, ans_sym, len(C), failA[0], failA[1], sep, tf(acc1), tf(acc2)))


def r2v46():
    P("=" * 150)
    P("§6 R2V4.6: one candidate on two contracts (the pole's forward candidate on C1 and on C2), Acc at each index")
    P("-" * 150)
    from model.cases import pole_fwd_candidate
    D = pole()
    C1, C2, C3 = pole_contracts(D)
    CH = frozenset([(ONE, "b1_45")] + [(a, "b1_45") for a in single_settings(D, ["H"])])
    Cid = frozenset((ONE, b) for b in D.B)
    conts = (("C1", C1), ("C2", C2), ("C3", C3), ("C_H", CH), ("C_id (all boundaries, a = 1)", Cid))
    for cname, mk in (("the forward candidate ℰ_fwd", pole_fwd_candidate), ("the reversed candidate ℰ_rev", R1.pole_rev_candidate)):
        vals = {}
        for name, C in conts:
            if (ONE, "b1_45") not in C:
                continue
            vals[name] = account(mk(R1.pole_q(C, name, D)))
        P("   %s: Acc per contract %s; read as one predicate of the candidate alone (R2-4-I6): %s"
          % (cname, "; ".join("%s %s" % (k, tf(v)) for k, v in vals.items()),
             "one predicate takes both values (T and F)" if len(set(vals.values())) > 1 else "no conflict on these contracts"))


def r2v47():
    P("=" * 150)
    P("§7 R2V4.7: K2's declared inputs struck (S108r2-4-I2): the record argument of FC30.new1 (a), usable before and after")
    P("-" * 150)
    j = Assessor(["MP"], ["r", Imp("r", Not("Expl_fwd"))])
    save = s108r2_s4.VARIANT
    try:
        for v in ("none", "R2V4.7"):
            s108r2_s4.VARIANT = v
            out, alpha = expl_ruled_out(j, "fwd")
            P("   %-7s α usable by j: %s; an argument not using (E) rules out Expl(ℰ_fwd): %s; a premise alone r usable: %s"
              % (v, tf(usable(j, alpha)), tf(out), tf(usable(j, Leaf("r")))))
    finally:
        s108r2_s4.VARIANT = save


def r2v48(cases):
    P("=" * 150)
    P("§8 R2V4.8: L526.s18 deleted, so the loop Build → (R) → Con → Build is a supplied place: the cut U (as worded) admitted in place of T′")
    P("-" * 150)
    P("   DEP cycles: U %s; T′ %s" % (dep_cycle(False, "U"), dep_cycle(False, "T'")))
    cnt = {"T'": {}, "U": {}}
    for label, where, c in cases:
        held = bool(faithful(c))
        H = [(ONE, c.p.b0)]
        selc = int(bool((ONE, c.p.b0) in c.p.C and faithful_on(c, H)))
        for kind, (hv, tr, sc_, rec) in {"Con (o1 ≺ o2, trace at o2)": ([int(held), int(held)], [0, 1], [0, 0], [None, None]),
                                         "Sel (one holding)": ([int(held)], [0], [selc], [None]),
                                         "rCon": ([int(held), int(held)], [1, 0], [0, 0], [None, 0]),
                                         "rSel": ([int(held), int(held)], [0, 0], [selc, 0], [None, 0])}.items():
            for rd in ("T'", "U"):
                k = len(prov_fixed_points(len(hv), hv, tr, sc_, rd, True, rec_of=rec))
                cnt[rd].setdefault(kind, {}).setdefault(k, 0)
                cnt[rd][kind][k] += 1
    for rd in ("T'", "U"):
        P("   %-3s fixed points per (case, history): %s" % (rd, "; ".join("%s: %s" % (k, dict(sorted(v.items()))) for k, v in cnt[rd].items())))


def e440():
    P("=" * 150)
    P("§9 e4.40 (R2V4.9 flagged, not implemented; the settlement computed, S108r2-4-I4): the four sentences at their own wording on the pole case,")
    P("   𝒯 = {t, t_ab (altered at one unseen pair's image only), t_ab,H (altered there and at H's image)}, at every unseen pair of C")
    P("-" * 150)
    from model.claims_b import faithful_on as fo
    p, c = fwd_pole_cand()
    H = [(ONE, "b1_45")]
    E = c.E

    def value(t, a, b):
        return (t.tau[a], t.sigma[b], tuple(t.E.L(k, t.tau[a], t.sigma[b]) for k in t.E.comps))
    unseen = [x for x in sorted(p.C, key=repr) if x not in H]
    w = sorted(E.full("c_L"))[0]
    rows = []
    for (a, b) in unseen:
        img = (c.tau[a], c.sigma[b])

        def mk(points, name):
            E2 = Org("E_alt", E.ports, E.dom, E.comps, E.foot, E.B, E.A, E._compose,
                     (lambda pts: (lambda j, a_, b_: (E.L(j, a_, b_) ^ {w}) if (j == "c_L" and (a_, b_) in pts) else E.L(j, a_, b_)))(points))
            return c.replace(E=E2, name=name)
        t_ab = mk({img}, "t_ab")
        t_abH = mk({img, (c.tau[ONE], c.sigma["b1_45"])}, "t_ab,H")
        for popname, pop in (("{t, t_ab,H}", [c, t_abH]), ("{t, t_ab}", [c, t_ab])):
            surv_diff = any(fo(t, H) and value(t, a, b) != value(c, a, b) for t in pop)
            mem_diff = any(value(t, a, b) != value(c, a, b) for t in pop)
            surv_vals = set(value(t, a, b) for t in pop if fo(t, H))
            rows.append(((a, b), popname, surv_diff, mem_diff, len(surv_vals) == 1, fo(t_ab, H), fo(t_abH, H)))
    for popname in ("{t, t_ab,H}", "{t, t_ab}"):
        rs = [r for r in rows if r[1] == popname]
        P("   𝒯 = %-12s unseen pairs %d: L572.s2's condition (a surviving differer) %d; Underdet under V4.8 (a differing member) %d; now's Underdet %d;"
          % (popname, len(rs), sum(r[2] for r in rs), sum(r[3] for r in rs), sum(r[2] for r in rs)))
        P("      L574.s5's 'the population fixes it' (survivors agree) %d; pairs where V4.8 calls the value underdetermined while survival on H separates t from every differer: %d"
          % (sum(r[4] for r in rs), sum(1 for r in rs if r[3] and not r[2])))
    P("   L574.n4's route: t_ab survives on H at every unseen pair: %s; t_ab,H survives at none: %s"
      % (all(r[5] for r in rows), not any(r[6] for r in rows)))


def e422():
    P("=" * 150)
    P("§10 e4.22 (R2V4.10): two histories differing only in a trace at o2 (h: Con; h′: the same with no trace), the pole's forward candidate;")
    P("   being an explanation now and under V4.3 (a) on each")
    P("-" * 150)
    p, c = fwd_pole_cand()
    acc = account(c)
    occ = set(p.C)
    h = Hist(["o1", "o2"], [("o2", "cod")], occ, admitted=True, prepares=True)
    h2 = Hist(["o1", "o2"], [("o2", "cod")], occ, admitted=True, prepares=False)
    H = [(ONE, "b1_45")]
    for name, hh in (("h (trace at o2)", h), ("h′ (no trace)", h2)):
        s, k = sel(c, H, hh), con(hh)
        dec = not s and not k
        P("   %-16s Sel %s, Con %s, Dec %s; Expl now %s; V4.3 (a) %s" % (name, tf(s), tf(k), tf(dec), tf(acc and not dec), tf(acc and not dec and (s or hh.prepares))))
    P("   D18.2 as written: φ preserves ≺_h and Θ's interpretation; D0.2 lists Prepares and Rec among the primitives read through Θ.")


def main():
    P("S108 Part A round 2, section 4: the round-2 variants on the worked cases and the reply's small cases (every 'after' was marked not run by the reply)")
    cases = cases_all()
    P("cases: %d (round 1's 29 and the owner's signs where not already among them)" % len(cases))
    which = sys.argv[1:] or ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    if "1" in which: r2v41(cases)
    if "2" in which: r2v42()
    if "3" in which: r2v43_chains()
    if "4" in which: r2v44(cases)
    if "5" in which: r2v45()
    if "6" in which: r2v46()
    if "7" in which: r2v47()
    if "8" in which: r2v48(cases)
    if "9" in which: e440()
    if "10" in which: e422()


if __name__ == "__main__":
    main()
