# S104 round 2, the owner's answers (decision S41, 28 September 2026): the new claims for Q2 and Q6.
# Q15 is carried by core.contrast (FC22 (b)); Q23 by args.usable and args.enumerate_args (FC72 (d)-(f)).
# Ids: FC<n>.new<m>. Stated in "formal claims, after round 2.md", marked [owner S41: Qn].
import itertools

from .core import ONE, account, faithful
from .args import Not, Imp, Leaf, Step, Assessor, X, atoms
from .harness import claim, forall, exhaustive, computed, construction, VAC
from .claims_a import SMALL, BOTHFAM, gen_p_cand
from .claims_b import (Hist, sel, con, fwd_pole_cand, prov_fixed_points, prov_show, build_at, episode, chain_eps,
                       EPISODE_READINGS, faithful_on)


# ---- Part XV, (Suff) (D16.XV) [owner S41: Q2] ------------------------------------------------------------
# Expl(ℰ) is an atom. "An argument not using (E)": Acc ∉ Uses(α), Uses(α) the atoms of α's leaves.
SUFF_READINGS = ("L536", "L17 as text 104 words it", "L17 (S41)")


def suff_defeats(acc, dec, out, reading):
    """ℰ ∈ Def_j(reading): L536 and L17 as S41 writes it ask Acc ∧ ¬Dec(t) ∧ an argument not using (E) that
    rules out Expl(ℰ); L17 as text 104 words it has no ¬Dec(t) (E06)."""
    if reading == "L17 as text 104 words it":
        return bool(acc and out)
    return bool(acc and not dec and out)


def expl_ok(acc, dec, expl):
    """The owner's condition on the atom (S41, Q2): Acc(ℰ) ∧ Dec(t) ⇒ ¬Expl(ℰ)."""
    return not (acc and dec and expl)


def uses(alpha):
    return set().union(*[atoms(l.claim) for l in alpha.leaves()])


def expl_ruled_out(j, name):
    """An argument usable by j, not using (E), that rules out Expl(ℰ): a record r and 'r → ¬Expl', modus ponens."""
    e = "Expl_" + name
    alpha = Step("MP", Not(e), [Leaf("r", "record"), Leaf(Imp("r", Not(e)))])
    got = [a for a in X(j, e, [alpha]) if "Acc_" + name not in uses(a)]
    return bool(got), alpha


def provenance_of(cand, kind, H):
    """A history for t, Θ by hand (I90): 'Dec' no selection admitted and no trace; 'Con' a trace preparing t and
    cod t represented; 'Sel' a selection history on H. Returns (Sel, Con, Dec) as computed by sel and con."""
    occ = set(cand.p.C)
    if kind == "Dec":
        h = Hist(["o1"], [], occ, admitted=False, prepares=False)
    elif kind == "Con":
        h = Hist(["o1", "o2"], [("o2", "cod")], occ, admitted=True, prepares=True)
    else:
        h = Hist(["o1"], [], occ, admitted=True, prepares=False)
    s, k = sel(cand, H, h), con(h)
    return s, k, (not s and not k)


@claim("FC30.new1", ["I90"])
def fc30_new1(S):
    parts = []
    p, c = fwd_pole_cand()
    H = [(ONE, "b1_45")]
    acc = account(c)
    rows, ok = [], acc
    for kind in ("Dec", "Con", "Sel"):
        s, k, dec = provenance_of(c, kind, H)
        for accepts in (True, False):
            j = Assessor(["MP"], ["r", Imp("r", Not("Expl_" + c.name))] if accepts else [])
            out, _ = expl_ruled_out(j, c.name)
            d = {r: suff_defeats(acc, dec, out, r) for r in SUFF_READINGS}
            rows.append("%s (Sel %s, Con %s, Dec %s), argument usable %s: %s" % (kind, s, k, dec, out, "; ".join("%s %s" % (r, d[r]) for r in SUFF_READINGS)))
            ok = ok and d["L17 (S41)"] == d["L536"] and d["L536"] <= d["L17 as text 104 words it"]
            if kind == "Dec" and accepts:
                ok = ok and d["L17 as text 104 words it"] and not d["L536"] and not d["L17 (S41)"]
            if kind == "Con" and accepts:
                ok = ok and all(d.values())
    _, alpha = expl_ruled_out(Assessor(["MP"], []), c.name)
    parts.append(computed("(a) the student's formula: a declared account ruled out as an explanation",
                          "the pole's forward candidate meets (E) (FC26); with a declared transport and an argument not using (E) that rules out Expl(ℰ), it is in Def(L17 as text 104 words it) and in neither Def(L536) nor Def(L17) as S41 writes it; with a constructed transport it is in all three",
                          ok, "Acc(ℰ_fwd) %s; argument:\n%s\n%s" % (acc, alpha.show(2), "\n".join(rows)), ["I90"]))

    def gen(rng, size):
        m = gen_p_cand(rng, size)
        if m is None:
            return None
        q, cand = m
        return cand, rng.choice(("Dec", "Con", "Sel")), rng.random() < 0.5

    def check(m):
        cand, kind, accepts = m
        a = account(cand)
        s, k, dec = provenance_of(cand, kind, [(ONE, cand.p.b0)])
        j = Assessor(["MP"], ["r", Imp("r", Not("Expl_" + cand.name))] if accepts else [])
        out, _ = expl_ruled_out(j, cand.name)
        d = {r: suff_defeats(a, dec, out, r) for r in SUFF_READINGS}
        if d["L17 (S41)"] != d["L536"]:
            return "Def(L17, S41) ≠ Def(L536): %s\n%s" % (d, cand.describe())
        if d["L17 as text 104 words it"] != (d["L536"] or (a and dec and out)):
            return "Def(L17 as text 104) is not Def(L536) with the declared accounts ruled out as explanations: %s\n%s" % (d, cand.describe())
        return None

    parts.append(forall(S, "FC30.new1", 2, "(b) one defeat set", "Def_j(L17, S41) = Def_j(L536); Def_j(L17 as text 104 words it) = Def_j(L536) ∪ {ℰ : Acc ∧ Dec(t) ∧ Expl(ℰ) ruled out}",
                        gen, check, SMALL, 40, BOTHFAM, ["I90"], note="provenance Θ by hand (I90): Dec, Con or Sel, each computed by sel and con"))
    both = True
    for a, d_ in itertools.product((False, True), repeat=2):
        expl = a and not d_  # Expl := Acc ∧ ¬Dec
        suff = (not (a and not d_)) or expl  # (Suff) as conjectured: Acc ∧ ¬Dec ⇒ Expl
        both = both and suff and expl_ok(a, d_, expl)  # the owner's condition: Acc ∧ Dec ⇒ ¬Expl
    parts.append(construction("(c) the owner's condition and (Suff) have a common model", "Expl := Acc ∧ ¬Dec meets Acc ∧ ¬Dec ⇒ Expl ((Suff) as conjectured) and Acc ∧ Dec ⇒ ¬Expl (S41, Q2), on every candidate",
                              both, "checked on the four values of (Acc, Dec); (E) itself takes no provenance (FC30): ¬Dec(t) stands beside it"))

    # S105 round 3, area 1 (B8, K3): the student's case computed from its history, not from admitted=False.
    # o1 the source the formula is copied from (it holds cod t, E's organization; its transport was prepared by
    # its author's construction trace, inherited by the copy it is: Θ by hand, I90); o2 the student's holding
    # of t (held and Sel's conditions computed from t; no trace: copying and declaring build no binding).
    j = Assessor(["MP"], ["r", Imp("r", Not("Expl_" + c.name))])
    out, _ = expl_ruled_out(j, c.name)
    rows, ok = [], acc and out
    for Hx, lab in ((H, "H = {(1,b1_45)}"), ([], "H = ∅")):
        held_o, selc_o = bool(faithful(c)), bool(Hx) and set(Hx) <= set(c.p.C) and faithful_on(c, Hx)
        for rd in ("U", "K", "T", "T'"):
            fps = prov_fixed_points(2, [1, held_o], [1, 0], [0, selc_o], rd, True)
            decs = [not sc[1][0] and not sc[1][1] for R, sc in fps]
            rows.append("%s, %s: fixed points %s; Dec(t) at o2 %s; Def(L17, S41) %s" % (lab, rd, prov_show(2, fps), decs, [suff_defeats(acc, d, out, "L17 (S41)") for d in decs]))
            if rd != "K":
                ok = ok and fps != [] and all(decs) and not any(suff_defeats(acc, d, out, "L17 (S41)") for d in decs)
    parts.append(computed("(d) the student's copy, provenance computed (B8)", "a source holding E (constructed) before the student's holding, no trace at the student's: Dec(t) under U, T and T′, whether or not one pair was tried; so Acc ∧ Dec ⇒ ¬Expl reaches the owner's example (K, rejected in round 2 because a first construction represents nothing there, FC98 (d), leaves the source unrepresented and gives Sel when one pair was tried)",
                          ok, "Acc(ℰ_fwd) %s; argument usable, not using (E): %s\n%s" % (acc, out, "\n".join(rows)), ["I90", "I161", "I162"]))
    # (e) a link written from nothing and declared: no earlier holding of E, no trace, no pair tried (H = ∅)
    rows, res = [], {}
    for hn in (False, True):
        selc_o = sel(c, [], Hist([], [], set(c.p.C)), h_nonempty=hn)
        fps = prov_fixed_points(1, [bool(faithful(c))], [0], [selc_o], "T'", True)
        dec = all(not sc[0][0] and not sc[0][1] for R, sc in fps)
        res[hn] = (dec, suff_defeats(acc, dec, out, "L17 (S41)"))
        rows.append("D12.1 %s: Sel's conditions %s; fixed points %s; Dec %s; in Def(L17, S41) %s" % ("with H ≠ ∅ (R3A1-05)" if hn else "after round 2 (H = ∅ allowed)", selc_o, prov_show(1, fps), dec, res[hn][1]))
    parts.append(computed("(e) a link no pair tried and nobody worked out (B8, FC77)", "after round 2 it is selected (H = ∅), so ¬Dec and Q2's condition misses it; with H ≠ ∅ it is declared and the owner's condition applies",
                          res[False] == (False, True) and res[True] == (True, False), "\n".join(rows), ["I90"]))
    # (f) K3: provenance per part (D12.4). A part is a component with its counterpart binding; the student copied the
    # components and declared the bindings. D12.4 carries a part's value over only if the part was transferred.
    rows, ok = [], True
    for k in c.Gamma:
        per = {}
        for lab, rof in (("D12.4 (component with its binding: the binding declared, not transferred)", None), ("K3's reading (the component alone, transferred)", 0)):
            fps = prov_fixed_points(2, [1, 1], [1, 0], [0, 0], "T'", True, rec_of=[None, rof])
            per[lab] = prov_show(2, fps)
        rows.append("part %s: %s" % (k, "; ".join("%s %s" % kv for kv in per.items())))
        v = list(per.values())
        ok = ok and v[0] == [{"o1": "Con"}] and v[1] == [{"o1": "Con", "o2": "Con"}]
    parts.append(computed("(f) K3: the student's parts under D12.4", "under D12.4's parts (component with its binding) no part of the student's t is a transfer, so each is Dec, as the whole t is (D12.3, D16.XV); only reading a part as the component alone gives the source's Con",
                          ok, "\n".join(rows), ["I54", "I90"]))
    # (g) S105 round 3, second checker (critical review, objection 3): L61's "(Nec) their necessity" after R3A1-T1
    # against L538 (D16.XV's (Nec)). After R3A1-T1 'their' has Account(ℰ) ∧ ¬Dec(t) as antecedent, so (Nec) so read
    # is defeated by an argument not using (E) that rules out ¬Expl(ℰ) where ℰ does not meet Account ∧ ¬Dec. L538 asks
    # instead that no transport under any contract preserve E; t faithful on C is one that does, so L538's defeat
    # fails wherever Faithful_C(t) (only that failure is computed, which is all this case needs).
    e = "Expl_" + c.name
    beta = Step("MP", e, [Leaf("r", "record"), Leaf(Imp("r", e))])  # rules out ¬Expl(ℰ)
    rows, res = [], {}
    pres = bool(faithful(c))
    for kind in ("Dec", "Con", "Sel"):
        s_, k_, dec = provenance_of(c, kind, H)
        jn = Assessor(["MP"], ["r", Imp("r", e)])
        outn = bool([a for a in X(jn, Not(e), [beta]) if "Acc_" + c.name not in uses(a)])
        res[kind] = (outn and not pres, outn and not (acc and not dec))
        rows.append("%s (Sel %s, Con %s, Dec %s): argument not using (E) that rules out ¬Expl(ℰ), usable: %s; defeats (Nec) as L538 (D16.XV) states it: %s; as L61's 'their' reads after R3A1-T1: %s"
                    % (kind, s_, k_, dec, outn, res[kind][0], res[kind][1]))
    ok_g = acc and pres and res["Dec"] == (False, True) and res["Con"] == (False, False) and res["Sel"] == (False, False)
    parts.append(computed("(g) L61's (Nec) against L538 (critical review, objection 3)",
                          "the student's declared copy, with an argument not using (E) that rules out ¬Expl(ℰ): in the defeat set of (Nec) as L61's 'their' reads after R3A1-T1 (necessity of Account ∧ ¬Dec), not in L538's (a transport, t, preserves E on C); with a constructed or selected transport in neither: the two differ exactly on Dec, which L538 names nowhere",
                          ok_g, "Acc(ℰ_fwd) %s; Faithful_C(t) %s\n%s" % (acc, pres, "\n".join(rows)), ["I90"]))
    return parts


# ---- Episodes and construction (D13.8, D12.2) [owner S41: Q6] ---------------------------------------------


def no_brief_question(qs, crit, brief="C_brief"):
    """S47 (I191): no question about the brief (the contract) occurred to the agent as worth investigating in the chain:
    the contract operative at every occurrence is the brief, and no occurrence is a criticism (D9.10) whose target z is
    the brief. crit[o]: None, or (z, δ) for a criticism occurrence; which occurrences are criticisms, and of what, is
    read through Θ (I90). A criticism of a design (z a transport) is allowed: the agent asks, the maths asks nothing (I190)."""
    return all(q == brief for q in qs) and not any(c is not None and c[0].startswith(brief) for c in crit)


def no_question_about_brief(qs, quest, brief="C_brief"):
    """S107 round 4, area 1 (N6: B11, W-N6; R4A1-01): the other reading of S47's "no question about the brief occurred
    to the agent as worth investigating": a question-occurrence is its own Θ label (I90), apart from criticism (D9.10),
    with or without an alleged defect. quest[o]: None, or the target of the question that occurred to the agent at o.
    Nothing in (R), Sel, Con, Dec, Episode or Build reads it (S47: the maths asks nothing)."""
    return all(q == brief for q in qs) and not any(t is not None and t.startswith(brief) for t in quest)


@claim("FC84.new1", ["I90"])
def fc84_new1(S):
    parts = []
    # (a) S47 (28 September 2026): the bridge to a fixed brief is an episode in which no question about the brief (the
    # contract) occurred to the agent as worth investigating (I191), not a history with no criticism. Criticism of
    # designs may or may not be in the history; Con (D12.2) reads no criticism event (the maths asks for nothing, I190),
    # so Con holds either way: (a1) no criticism occurrence; (a2) a first design criticized ("fails the load case")
    # before the design that is built. Θ by hand (I90): the chain, held, trace, q(o), records, and crit[o], the
    # criticism an occurrence is (D9.10: its target z and alleged defect δ), or None.
    n = 2  # kept for parts (b), (c)
    trace, selc = [0, 1], [0, 0]
    rows, res, ok_a = [], {}, {}
    cases = (("a1", "no criticism in the history", ["o1", "o2"], [0, 1], [0, 1], [None, None]),
             ("a2", "a first design criticized before the built one", ["o1", "o2", "o3"], [0, 0, 1], [0, 0, 1],
              [None, ("t0 (the first design, at o1)", "fails the load case"), None]))
    for key, lab, occ, held_, trace_, crit in cases:
        n_ = len(occ)
        qs = ["C_brief"] * n_
        recs = [False] * n_
        noq = no_brief_question(qs, crit)
        sub_rows, r_ = [], {}
        for rd in EPISODE_READINGS:
            fps = prov_fixed_points(n_, held_, trace_, [0] * n_, "T'", True, chain_eps(qs, recs, rd))
            conv = [sc[n_ - 1][1] for R, sc in fps]
            r_[rd] = (len(fps), conv, build_at(n_, held_, trace_, "T'", fps[0][0] if fps else frozenset(), n_ - 1))
            sub_rows.append("%s: %d fixed point(s) %s; Con at %s %s; Build %s" % (rd, len(fps), prov_show(n_, fps), occ[-1], conv, r_[rd][2]))
        h_ = Hist(occ, [(occ[-1], "cod")], set(), prepares=True, contracts=qs, records=recs)
        tag = {rd: con(h_, reading=rd) for rd in EPISODE_READINGS}
        # the same history with the criticism aimed at the brief instead: a question about the brief occurred to the
        # agent; the encoding tells the two apart, and Con, which reads no criticism, is the same (the maths asks nothing)
        crit_b = [x if x is None else ("C_brief (the contract)", x[1]) for x in crit]
        noq_b = no_brief_question(qs, crit_b) if any(crit) else None
        ok_a[key] = (noq and r_["S41"][0] == 1 and r_["S41"][1] == [True] and r_["S41"][2] and r_["L55"][1] == [False] and r_["L55"][2]
                     and tag["S41"] and not tag["L55"] and (noq_b is None or noq_b is False))
        rows.append((key, lab, occ, crit, noq, noq_b, sub_rows, tag))
    for key, lab, occ, crit, noq, noq_b, sub_rows, tag in rows:
        parts.append(computed("(%s) S47: the bridge to a fixed brief, %s" % (key, lab),
                              "an episode in which no question about the brief occurred to the agent as worth investigating (one contract throughout, no criticism aimed at it; I191), "
                              "a trace preparing t, cod t held at the output: Con(t) under D13.8 as S41 has it, %s; under L55 as text 104 words it Con fails; Build holds under both"
                              % ("with no criticism in the history" if key == "a1" else "with a criticism of an earlier design in the history (Con reads no criticism event, I190)"),
                              ok_a[key], "chain %s; q = C_brief throughout; criticism per occurrence %s; no question about the brief occurred: %s%s; cut T′ (I162), I161.\n%s\ntag model (con): S41 %s, L55 %s"
                              % (" ≺ ".join(occ), crit, noq, ("; with the criticism aimed at the brief instead: no question about the brief %s (Con's computation takes no criticism: its value is the same)" % noq_b) if noq_b is not None else "",
                                 "\n".join(sub_rows), tag["S41"], tag["L55"]), ["I90", "I162", "I165", "I190", "I191"]))
    # (a3) S107 round 4, area 1 (N6: B11, W-N6, S-N6, C-N6): which occurrences are "a question about the brief occurred to
    # the agent as worth investigating" is read through Θ (I90). I191 reads them as criticisms (D9.10) aimed at the brief
    # (crit[o]); R4A1-01 records two other readings: (d) a question-occurrence as its own label, with or without an alleged
    # defect (quest[o]); (e) a question found (L15, L155; L161: "another question with its own contract"), operative at
    # its occurrence (q(o) is not the brief there). On (a1)'s chain, with the labels and contracts set as each case says
    # (Θ by hand, I90), the three readings are computed from them, and Con and Build at the output from the chain (T′,
    # both readings of L55). The readings part ways; under D13.8 as S41 has it Con and Build are the same in every case
    # (the maths asks nothing, S47); under L55 as text 104 words it only a recorded change of contract moves Con, as (b).
    Q_B = "C_brief? (a question found at o1, its target the brief)"
    cases3 = (("base", "(a1)'s chain: no criticism, no question", [None, None], [None, None], ["C_brief"] * 2, [False] * 2),
              ("i", "a question about the brief occurred at o1, no defect alleged, the brief kept (B11 (i))",
               [None, None], ["C_brief (the contract)", None], ["C_brief"] * 2, [False] * 2),
              ("ii", "a criticism aimed at the brief used as a given, no question occurred to the agent (B11 (ii); S27)",
               [("C_brief (the contract)", "the brief is wrong"), None], [None, None], ["C_brief"] * 2, [False] * 2),
              ("iii", "a question about the brief occurred at o1 and was not pursued (C-N6's NC4)",
               [("C_brief (the contract)", "why this brief?"), None], ["C_brief (the contract)", None], ["C_brief"] * 2, [False] * 2),
              ("iv-r", "a question about the brief found at o1 and operative there, the brief taken up again at o2, the change recorded",
               [None, None], ["C_brief (the contract)", None], [Q_B, "C_brief"], [False, True]),
              ("iv-u", "as iv-r, the change back to the brief unrecorded",
               [None, None], ["C_brief (the contract)", None], [Q_B, "C_brief"], [False, False]))
    held3, trace3 = [0, 1], [0, 1]
    vals3, rows3 = {}, []
    for key, lab, crit, quest, qs3, recs3 in cases3:
        rd3 = (no_brief_question(qs3, crit), no_question_about_brief(qs3, quest), all(q == "C_brief" for q in qs3))
        cb = {}
        for rd in EPISODE_READINGS:
            fps = prov_fixed_points(2, held3, trace3, [0, 0], "T'", True, chain_eps(qs3, recs3, rd))
            cb[rd] = (len(fps), [sc[1][1] for R, sc in fps], build_at(2, held3, trace3, "T'", fps[0][0] if fps else frozenset(), 1))
        vals3[key] = (rd3, cb)
        rows3.append("(%s) %s: q per occurrence %s, records %s; criticism per occurrence %s; question per occurrence %s; "
                     "no question about the brief: I191 %s, R4A1-01 (d) %s, (e) %s; %s"
                     % (key, lab, qs3, recs3, crit, quest, rd3[0], rd3[1], rd3[2],
                        "; ".join("%s: %d fixed point(s), Con at o2 %s, Build %s" % (rd, cb[rd][0], cb[rd][1], cb[rd][2]) for rd in EPISODE_READINGS)))
    T_, F_ = True, False
    readings_as_claimed = [vals3[k][0] for k, *_ in cases3] == [(T_, T_, T_), (T_, F_, T_), (F_, T_, T_), (F_, F_, T_), (F_, F_, F_), (F_, F_, F_)]
    s41_same = all(vals3[k][1]["S41"] == (1, [True], True) for k in vals3)
    l55_as_b = all(vals3[k][1]["L55"] == ((1, [True], True) if k == "iv-r" else (1, [False], True)) for k in vals3)
    parts.append(computed("(a3) N6: the readings of 'no question about the brief occurred' (I191; R4A1-01 (d), (e))",
                          "which occurrences are a question about the brief is read through Θ (I90): as criticisms (D9.10) aimed at the brief (I191); as "
                          "question-occurrences, with or without an alleged defect (R4A1-01 (d)); or as a question found (L15, L155, L161), operative at its "
                          "occurrence (R4A1-01 (e)). The readings part ways (B11's (i), (ii); a question found and operative); under D13.8 as S41 has it, Con "
                          "and Build at the output are the same in every case, one fixed point each (T′): no computed value reads the labels (S47: the maths "
                          "asks nothing); under L55 as text 104 words it, only a recorded change of contract moves Con, as in (b)",
                          readings_as_claimed and s41_same and l55_as_b,
                          "chain o1 ≺ o2; held, trace at o2 (Θ by hand, I90).\n" + "\n".join(rows3),
                          ["I90", "I162", "I165", "I190", "I191", "R4A1-01"]))
    # (b) a recorded change of contract C → C' at o2; (c) the same change unrecorded
    out = []
    ok_b = ok_c = True
    for recd in (True, False):
        q2, r2 = ["C", "C'"], [False, recd]
        for rd in EPISODE_READINGS:
            eps = chain_eps(q2, r2, rd)
            span = episode(q2, r2, rd)
            fps = prov_fixed_points(n, [1, 1], trace, selc, "T'", True, eps)
            conv = [sc[1][1] for R, sc in fps]
            out.append("change %s, %s: o1 ≺ o2 an episode %s; Con at o2 %s" % ("recorded" if recd else "unrecorded", rd, span, conv))
            if recd:
                ok_b = ok_b and span and conv == [True]
            else:
                ok_c = ok_c and not span and conv == ([True] if rd == "S41" else [False])
    parts.append(computed("(b) a recorded change of contract", "C → C' at o2 with its provenance record: o1 ≺ o2 is an episode under both readings, and Con(t) at o2", ok_b, "\n".join(o for o in out if "unrecorded" not in o), ["I90", "I165"]))
    parts.append(computed("(c) an unrecorded change of contract", "o1 ≺ o2 is then no episode (L55's record clause, I165); Con at o2 needs an episode after the change holding the target: {o2} under S41, none under L55's wording", ok_c,
                          "\n".join(o for o in out if "unrecorded" in o), ["I90", "I165"]))

    # (d) every chain of ≤ 3 occurrences with contracts and records: Con under S41 ⊇ Con under L55's wording, differing
    # exactly where no episode ending at the output holds a change of contract; Sel ∧ Con at no fixed point
    def items():
        for n_ in (1, 2, 3):
            for bits in itertools.product(itertools.product([0, 1], repeat=3), repeat=n_):
                held_, trace_, selc_ = [b[0] for b in bits], [b[1] for b in bits], [b[2] for b in bits]
                for q_ in itertools.product(["C", "C'"], repeat=n_):
                    if q_[0] != "C":
                        continue
                    for r_ in itertools.product([False, True], repeat=n_):
                        if r_[0]:
                            continue
                        yield n_, held_, trace_, selc_, list(q_), list(r_)

    def check(m):
        n_, held_, trace_, selc_, q_, r_ = m
        fs = {rd: prov_fixed_points(n_, held_, trace_, selc_, "T'", True, chain_eps(q_, r_, rd)) for rd in EPISODE_READINGS}
        if len(fs["S41"]) != 1 or len(fs["L55"]) != 1:
            return "not one fixed point under T′: %s" % m
        o = n_ - 1
        cs, cl = fs["S41"][0][1][o][1], fs["L55"][0][1][o][1]
        if cl and not cs:
            return "Con under L55's wording but not under S41: %s" % (m,)
        for rd in EPISODE_READINGS:
            R, sc = fs[rd][0]
            if any(sc[x][0] and sc[x][1] for x in range(n_)):
                return "Sel ∧ Con under %s: %s" % (rd, m)
        if cs and not cl:
            chg_eps = [i for i in range(o + 1) if episode(q_[i:o + 1], r_[i:o + 1], "S41") and episode(q_[i:o + 1], r_[i:o + 1], "L55")
                       and any(held_[x] for x in range(i, o + 1))]
            if chg_eps:
                return "Con differs although an episode with a change holds the target: %s" % (m,)
        return None

    parts.append(exhaustive("FC84.new1", "(d) every chain of ≤ 3 occurrences", "Con(S41) ⊇ Con(L55's wording), the difference exactly where no episode ending at the output holds a change of contract and the target; Sel ∧ Con at no fixed point; one fixed point each (T′)",
                            list(items()), check, "chains o1 ≺ … ≺ on, n ≤ 3; held, trace, Sel's conditions per occurrence; q(o) ∈ {C, C'}; records per change", ["I90", "I161", "I162", "I165"]))
    return parts
