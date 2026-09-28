# S108 Part A, section 3: the worked cases, histories and the reply's small cases, each section-3 variant off and on.
#   PYTHONHASHSEED=0 python3 -B s108_s3_cases.py
# A. Every worked case the program builds (the cases of the written-in step's script, s106_cases.py, collected by running
#    its main() with its `case` replaced by a collector, labels unchanged): Acc(ℰ) with its conjuncts, and Account ∧ ¬Dec(t)
#    with t's history set by hand (Θ by hand, I90): the three histories of claims_s41.provenance_of ('Dec', 'Con', 'Sel' on
#    H = {(1, b0)}), and four more where a section-3 variant can bite:
#      'Con-chg (tags)': cod t represented at o1, the contract changes C → C' into o2 unrecorded, a trace prepares t at o2
#                        (the tag model of claims_b.con, as provenance_of uses it);
#      'Con-chg (chain, cut)': the same chain in the chain model (prov_fixed_points), Held at o1 by hand, at o2 computed from t
#                        (Faithful), under each cut U, K, T, T′;
#      'Sel-parts': a selection history on H whose stated construction lacks one of t's parts (parts(t) := E's components,
#                        the stated construction := all but E's last component; S108-3-I4);
#      'Con-explu': a Con history whose trace's output uses the claim 'Acc(ℰ)' of the candidate itself (ExplUse, D13.3).
#    and Build at the output (D13.3) with ExplUse computed from the candidate's own Acc, Build's other conjuncts (Owned,
#    Prepares, Held of the built content, BindingConstruction, ¬TransferComposite) set to hold as FC90.new1 sets them.
# B. The student's declared copy (FC30.new1 (d)), in the chain model.
# C. The reply's small cases, V3.1 … V3.8, each off and on.
# Standard library only; imports the package model/ of this folder; writes nothing.
import contextlib
import io
import itertools
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from model import s108s3  # noqa: E402
from model.core import ONE, Org, Question, PortQuery, account, faithful  # noqa: E402
from model.args import Not, And, Imp, Leaf, Step, Assessor, X, usable, rules_out, enumerate_args, show  # noqa: E402
from model.cases import pole, pole_fwd_candidate, pole_rev_candidate, fibre_query  # noqa: E402
from model.claims_a import pole_contracts  # noqa: E402
from model.claims_b import (Hist, sel, con, episode, chain_eps, prov_fixed_points, prov_show, build_at, faithful_on,  # noqa: E402
                            fwd_pole_cand, EPISODE_READINGS)
from model.claims_s41 import provenance_of, suff_defeats, expl_ruled_out, not_using_E  # noqa: E402
from model.phys import Circuit, act_route  # noqa: E402
import s106_cases  # noqa: E402

VARIANTS = [v for v in s108s3.VARIANTS if v != "none"]
READINGS = [(v, "prepares") for v in VARIANTS] + [("V3.4", "build")]
CUTS = ("U", "K", "T", "T'")


def rname(v, ct):
    return v + (" (CT reads ExplUse, S108-3-I2)" if ct == "build" else "")


def tf(x):
    return "T" if x else "F"


def section(title):
    print("=" * 150)
    print(title)
    print("-" * 150)


# ---- A. worked cases -----------------------------------------------------------------------------------------------------

def worked_cases():
    got = []
    orig = s106_cases.case
    s106_cases.case = lambda label, where, c, note="": got.append((label, where, c))
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            s106_cases.main()
    finally:
        s106_cases.case = orig
    return got


def with_parts(c, stated):
    occ = set(c.p.C)
    return Hist(["o1"], [], occ, admitted=True, prepares=False, parts=list(c.E.comps), stated=list(stated))


def evaluate(c):
    acc, d = account(c, detail=True)
    acc = bool(acc)
    H = [(ONE, c.p.b0)]
    occ = set(c.p.C)
    prov = {}
    for kind in ("Dec", "Con", "Sel"):
        s, k, dec = provenance_of(c, kind, H)
        prov[kind] = (s, k, dec)
    h = Hist(["o1", "o2"], [("o1", "cod")], occ, admitted=True, prepares=True, contracts=["C", "C'"], records=[False, False])
    s, k = sel(c, H, h), con(h)
    prov["Con-chg (tags)"] = (s, k, not s and not k)
    held_out = bool(faithful(c))
    for rd in CUTS:
        fps = prov_fixed_points(2, [1, held_out], [0, 1], [0, 0], rd, True, chain_eps(["C", "C'"], [False, False]))
        decs = sorted(set(not sc[1][0] and not sc[1][1] for R, sc in fps))
        prov["Con-chg (chain, %s)" % rd] = (None, None, tuple(decs) if len(decs) != 1 else decs[0])
    stated = list(c.E.comps)[:-1]
    h = with_parts(c, stated)
    s, k = sel(c, H, h), con(h)
    prov["Sel-parts"] = (s, k, not s and not k)
    ex = s108s3.expl_use(True, acc)
    h = Hist(["o1", "o2"], [("o2", "cod")], occ, admitted=True, prepares=True, explu=ex)
    s, k = sel(c, H, h), con(h)
    prov["Con-explu"] = (s, k, not s and not k)
    build = build_at(1, [1], [1], "T'", frozenset(), 0, explu=[ex])  # Build's other conjuncts set to hold, as FC90.new1 (Θ, I90)
    expl = {kind: (acc and not v[2]) if isinstance(v[2], bool) else tuple(acc and not x for x in v[2]) for kind, v in prov.items()}
    conj = {k_: bool(d[k_]) for k_ in ("F1", "F2", "A", "Dep", "NonVacuous") if k_ in d}
    return dict(acc=acc, conj=conj, prov=prov, expl=expl, build=build, held_out=held_out)


def part_a():
    section("A. Worked cases: Acc with conjuncts; Dec(t) and Account ∧ ¬Dec(t) per hand-set history; Build at the output — 'none' and each variant")
    cases = worked_cases()
    print("%d worked cases (s106_cases.py's, collected)" % len(cases))
    base = {}
    s108s3.set_variant("none", "prepares")
    for label, where, c in cases:
        base[label] = evaluate(c)
        e = base[label]
        print("%-62s Acc %s [%s] | %s | Build %s" % (label[:62], tf(e["acc"]), " ".join("%s %s" % (k, tf(v)) for k, v in e["conj"].items()),
                                                     "; ".join("%s: Dec %s Expl %s" % (k, e["prov"][k][2], e["expl"][k]) for k in e["prov"]), tf(e["build"])))
    summary = {}
    for v, ct in READINGS:
        s108s3.set_variant(v, ct)
        rows, cnt = [], dict(acc=0, build=0)
        for label, where, c in cases:
            e = evaluate(c)
            b = base[label]
            if e["acc"] != b["acc"]:
                cnt["acc"] += 1
                rows.append("  %s: Acc %s → %s" % (label, tf(b["acc"]), tf(e["acc"])))
            for k in e["prov"]:
                if e["prov"][k][2] != b["prov"][k][2]:
                    cnt["dec " + k] = cnt.get("dec " + k, 0) + 1
                if e["expl"][k] != b["expl"][k]:
                    cnt["expl " + k] = cnt.get("expl " + k, 0) + 1
                    rows.append("  %s | %s: Dec %s → %s; Account ∧ ¬Dec(t) %s → %s" % (label, k, b["prov"][k][2], e["prov"][k][2], b["expl"][k], e["expl"][k]))
            if e["build"] != b["build"]:
                cnt["build"] += 1
                rows.append("  %s: Build %s → %s (Acc %s)" % (label, tf(b["build"]), tf(e["build"]), tf(e["acc"])))
        summary[(v, ct)] = cnt
        print("--- %s: %s" % (rname(v, ct), cnt))
        for r in rows:
            print(r)
    s108s3.set_variant("none", "prepares")
    print("--- summary (moves out of %d cases): %s" % (len(cases), "; ".join("%s %s" % (rname(*k), v) for k, v in summary.items())))
    return cases


# ---- B. the student's declared copy ---------------------------------------------------------------------------------------

def part_b():
    section("B. The student's declared copy (FC30.new1 (d)): source o1 (held, trace), the student's holding o2 (held and Sel's conditions from t, no trace)")
    for v, ct in [("none", "prepares")] + READINGS:
        s108s3.set_variant(v, ct)
        D = pole()
        C1, _, _ = pole_contracts(D)
        c = pole_fwd_candidate(Question(D, C1, "b1_45", PortQuery(), "L", name="p"))
        acc = bool(account(c))
        rows = []
        for Hx, lab in (([(ONE, "b1_45")], "H={(1,b1_45)}"), ([], "H=∅")):
            held_o = bool(faithful(c))
            selc_o = bool(Hx) and set(Hx) <= set(c.p.C) and faithful_on(c, Hx)
            for rd in ("T'",):
                fps = prov_fixed_points(2, [1, held_o], [1, 0], [0, selc_o], rd, True)
                decs = [not sc[1][0] and not sc[1][1] for R, sc in fps]
                rows.append("%s %s: %s Dec(t) at o2 %s, Expl %s" % (lab, rd, prov_show(2, fps), decs, [acc and not d for d in decs]))
        print("%-45s Acc %s | %s" % (rname(v, ct), tf(acc), " | ".join(rows)))
    s108s3.set_variant("none", "prepares")


# ---- C. the reply's small cases ---------------------------------------------------------------------------------------------

def both(fn):
    """fn() under 'none' and under the variant set by the caller's loop; returns (off, on)."""
    return fn


def small_v31():
    section("C. V3.1 (D9.7: RO(α, φ) :⟺ Incons(φ, concl(α)))")
    out = {}
    for v in ("none", "V3.1"):
        s108s3.set_variant(v)
        PM, design = "PM", "design"
        j = Assessor(["MP"], [Not(PM)])
        bare = Leaf(Not(PM))
        rec = Leaf("r", "record", made_from="psi")
        a2 = Step("MP", "psi", [rec, Leaf(Imp("r", "psi"))])
        a1 = Step("AndE", Not("acc"), [Leaf(And(Not("acc"), "q"))])
        jp = Assessor(["MP"], ["p"])
        jnp = Assessor(["MP"], [])
        pbp = Leaf("p")
        A = "Ans_p(a,b)=y"
        jA = Assessor(["MP", "MT"], [Not(A)])
        jAl = Assessor(["MP", "MT"], [Not(A), Imp("Acc_E", A)])
        mt = Step("MT", Not("Acc_E"), [Leaf(Not(A)), Leaf(Imp("Acc_E", A))])
        e = "Expl_E"
        jx = Assessor(["MP"], [Not(e)])
        xs = [a for a in X(jx, e, [Leaf(Not(e))]) if not_using_E(a, "E")]
        # (Suff): Acc ∧ ¬Dec ∧ an argument not using (E) ruling out Expl(ℰ); the forward pole candidate, constructed
        p, c = fwd_pole_cand()
        s_, k_, dec = provenance_of(c, "Con", [(ONE, "b1_45")])
        suff = suff_defeats(bool(account(c)), dec, bool(xs), "L536")
        # (Nec) as L61 reads after R3A1-T1: an argument not using (E) ruling out ¬Expl(ℰ) where ℰ lacks Account ∧ ¬Dec
        jn = Assessor(["MP"], [e])
        xn = [a for a in X(jn, Not(e), [Leaf(e)]) if not_using_E(a, "E")]
        out[v] = [
            ("FC72 (e): ¬PM alone, j accepts ¬PM: rules out PM", usable(j, bare) and rules_out(bare, PM)),
            ("FC72 (b): a record made from ψ rules out ¬ψ", rules_out(a2, Not("psi"))),
            ("FC72 (a): a leaf ¬φ ∧ q rules out φ (AndE)", rules_out(a1, "acc")),
            ("'p because p': p alone, j accepts p: rules out ¬p", usable(jp, pbp) and rules_out(pbp, Not("p"))),
            ("'p because p': p alone, j accepts nothing: rules out ¬p", usable(jnp, pbp) and rules_out(pbp, Not("p"))),
            ("j accepts ¬(Ans=y) alone: the answer y ruled out (X_j(Ans=y) ≠ ∅)", bool(X(jA, A, [Leaf(Not(A))]))),
            ("j accepts ¬(Ans=y) alone: Acc(ℰ) of a candidate answering y ruled out", bool(X(jA, "Acc_E", [Leaf(Not(A))]))),
            ("j accepts ¬(Ans=y) and Acc(ℰ) → Ans=y: MT rules out Acc(ℰ)", bool(X(jAl, "Acc_E", [mt]))),
            ("j accepts ¬Expl(ℰ) alone: an argument not using (E) rules out Expl(ℰ)", bool(xs)),
            ("  so the pole's forward candidate (Acc T, constructed) is in (Suff)'s defeat set Def(L536)", suff),
            ("j accepts Expl(ℰ) alone: an argument not using (E) rules out ¬Expl(ℰ) ((Nec)'s defeat, L61)", bool(xn)),
        ]
    s108s3.set_variant("none")
    for (lab, a), (_, b) in zip(out["none"], out["V3.1"]):
        print("%-100s none %s | V3.1 %s%s" % (lab, tf(a), tf(b), "   MOVES" if a != b else ""))


def small_v32():
    section("C. V3.2 (D9.4: Live_j(d; u) :⟺ d ∈ Accepted_j(ξ))")
    out = {}
    for v in ("none", "V3.2"):
        s108s3.set_variant(v)
        d, q = "d", "q"
        w = Step("MP", d, [Leaf(q), Leaf(Imp(q, d))])
        u = Step("AndI", And(d, q), [w, Leaf(q)])
        jb = Assessor(["MP", "AndI"], [d, q, Imp(q, d)])
        ja = Assessor(["MP", "AndI"], [q, Imp(q, d)])
        O_, TBI = "O", And("T", "B", "I")
        cond = Imp(TBI, O_)
        s1 = Step("MP", Not(O_), [Leaf("rec", "record"), Leaf(Imp("rec", Not(O_)))])
        alpha = Step("MT", Not(TBI), [s1, Leaf(cond)])
        jt = Assessor(["MP", "MT"], ["rec", Imp("rec", Not(O_)), cond])
        jt2 = Assessor(["MP", "MT"], ["rec", Imp("rec", Not(O_)), cond, Not(O_)])
        out[v] = [
            ("FC70: u (d also concluded below), usable before j withdraws d", usable(jb, u)),
            ("FC70: u usable after j withdraws d", usable(ja, u)),
            ("Arg_test (record, r → ¬O, then MT): usable by j accepting the leaves", usable(jt, alpha)),
            ("Arg_test: rules out T∧B∧I for that j (X_j ≠ ∅)", bool(X(jt, TBI, [alpha]))),
            ("Arg_test: usable once j also accepts the intermediate ¬O", usable(jt2, alpha)),
        ]
    s108s3.set_variant("none")
    for (lab, a), (_, b) in zip(out["none"], out["V3.2"]):
        print("%-100s none %s | V3.2 %s%s" % (lab, tf(a), tf(b), "   MOVES" if a != b else ""))


def small_v33():
    section("C. V3.3 (D9.6: Usable_j(α) :⟺ ∀u ∈ steps(α) Usable_j(u); a premise alone usable by every j)")
    out = {}
    for v in ("none", "V3.3"):
        s108s3.set_variant(v)
        PM, design = "PM", "design"
        bare = Leaf(Not(PM))
        phi = And(design, PM)
        args = enumerate_args([Not(PM)])
        j0 = Assessor(["MP"], [])
        j = Assessor(["MP"], [Not(PM)])
        jr = Assessor(["MP"], ["PM_possible_as_given"])
        out[v] = [
            ("FC72 (f): j0 accepts nothing: ¬PM alone usable", usable(j0, bare)),
            ("FC72 (f): |X_j0(design ∧ PM)| over the arguments from ¬PM", len(X(j0, phi, args))),
            ("FC72 (d): j accepts ¬PM: ¬PM alone usable; |X_j(design ∧ PM)|", (usable(j, bare), len(X(j, phi, args)))),
            ("X_j(design ∧ PM) the same for j0 and j (assessor-independent)", [id(a) for a in X(j0, phi, args)] == [id(a) for a in X(j, phi, args)]),
            ("j' who accepts something else: ¬PM alone usable", usable(jr, bare)),
            ("(Suff)'s defeat: ψ = r ∧ (r → ¬Expl(ℰ)) alone, j0 accepts nothing: rules out Expl(ℰ), not using (E)",
             bool([a for a in X(j0, "Expl_E", [Leaf(And("r", Imp("r", Not("Expl_E"))))]) if not_using_E(a, "E")])),
            ("the same, j accepts ψ", bool([a for a in X(Assessor(["MP"], [And("r", Imp("r", Not("Expl_E")))]), "Expl_E", [Leaf(And("r", Imp("r", Not("Expl_E"))))]) if not_using_E(a, "E")])),
            ("bare ¬Expl(ℰ) alone, j0 accepts nothing (the block: ¬φ is the premise)", bool(X(j0, "Expl_E", [Leaf(Not("Expl_E"))]))),
        ]
    s108s3.set_variant("none")
    for (lab, a), (_, b) in zip(out["none"], out["V3.3"]):
        print("%-100s none %s | V3.3 %s%s" % (lab, a, b, "   MOVES" if a != b else ""))


def small_v34():
    section("C. V3.4 (D13.3: ExplUse(o, c) :⟺ UsesClaim(o, 'Acc(ℰ)') ∧ Acc(ℰ)): the reversed calculation worked out, claimed on C1, judged on C_id")
    D = pole()
    C1, _, _ = pole_contracts(D)
    p1 = Question(D, C1, "b1_45", PortQuery(), "L", name="p_prod")
    rev1 = pole_rev_candidate(p1)
    Did = pole(bounds=[(1, 45), (2, 45), (3, 45)])
    pid = Question(Did, frozenset((ONE, b) for b in Did.B), "b1_45", fibre_query(), ("H", "T", "L"), name="p_ident")
    revid = pole_rev_candidate(pid, delta=("H", "T", "L"))
    acc1, accid = bool(account(rev1)), bool(account(revid))
    _, d1 = account(rev1, detail=True)
    _, did = account(revid, detail=True)
    print("Acc(ℰ_rev on C1, production) %s %s; Acc(ℰ_rev on C_id, identification) %s %s" % (tf(acc1), {k: d1[k] for k in ("F1", "F2", "A", "Dep", "NonVacuous")},
                                                                                               tf(accid), {k: did[k] for k in ("F1", "F2", "A", "Dep", "NonVacuous")}))
    held = bool(faithful(revid))
    for v, ct in (("none", "prepares"), ("V3.4", "prepares"), ("V3.4", "build")):
        s108s3.set_variant(v, ct)
        rows = []
        for used, lab in ((acc1, "claim used: Acc(ℰ_rev on C1)"), (accid, "claim used: Acc(ℰ_rev on C_id)")):
            ex = s108s3.expl_use(True, used)
            build = build_at(1, [held], [1], "T'", frozenset(), 0, explu=[ex])
            fps = prov_fixed_points(1, [held], [1], [0], "T'", True, explu=[ex])
            decs = [not sc[0][0] and not sc[0][1] for R, sc in fps]
            h = Hist(["o1"], [("o1", "cod")], set(pid.C), admitted=True, prepares=True, explu=ex)
            ktag = con(h)
            rows.append("%s: ExplUse %s, Build %s; chain T′: %s Dec %s, Account ∧ ¬Dec(t) on C_id %s; tags: Con %s"
                        % (lab, tf(ex), tf(build), prov_show(1, fps), decs, [accid and not d for d in decs], tf(ktag)))
        print("%-45s %s" % (rname(v, ct), "\n%-45s %s" % ("", rows[1]) if False else rows[0]))
        print("%-45s %s" % ("", rows[1]))
    s108s3.set_variant("none", "prepares")


def small_v35():
    section("C. V3.5 (D13.8: Episode(h') :⟺ h' ⊆ h a subhistory): FC84.new1 (c), (iv-u), and a chain where Con moves")
    Q_B = "C_brief? (a question found at o1)"
    for v in ("none", "V3.5"):
        s108s3.set_variant(v)
        ep = {rd: (episode(["C_brief"] * 2, [False] * 2, rd), episode([Q_B, "C_brief"], [False, False], rd), episode(["C", "C'"], [False, False], rd)) for rd in EPISODE_READINGS}
        print("%s: Episode(o1 ≺ o2) on (base, iv-u, (c) unrecorded C → C'): %s" % (v, "; ".join("%s %s" % kv for kv in ep.items())))
        for lab, held, trace in (("(c): held [T, T], trace at o2", [1, 1], [0, 1]), ("added: held [T, F], trace at o2", [1, 0], [0, 1]),
                                 ("added: held [T, T], trace at o1 and o2", [1, 1], [1, 1])):
            cols = []
            for rd in CUTS:
                for er in EPISODE_READINGS:
                    fps = prov_fixed_points(2, held, trace, [0, 0], rd, True, chain_eps(["C", "C'"], [False, False], er))
                    cols.append("%s/%s: %s" % (rd, er, [sc[1][1] for R, sc in fps]))
            print("   %-40s Con at o2 per cut/episode reading: %s" % (lab, "; ".join(cols)))
    s108s3.set_variant("none")


def extra_part(c, mode, x=None):
    """t' = t with one more part k_x (S108-3-I4), not committed (not in Γ). 'idle': on the footprint of E's first component,
    the full relation at every pair (it constrains nothing). 'copy': on that footprint, that component's own relation at every
    pair (redundant). 'deviate': on the queried port δ_E, the full relation at every
    pair but x = (τa, σb), where it admits one value of δ_E only, one E's own answer there does not take (so E's solution at x
    moves and t' differs from t at (a, b))."""
    E = c.E
    foot = dict(E.foot)
    if mode in ("copy", "idle"):
        k0 = E.comps[0]
        foot["k_x"] = E.foot[k0]
    else:
        foot["k_x"] = (c.deltaE,)
        cur = c.ans_E(*x)
        others = [w for w in E.dom[c.deltaE] if w != cur]
        bad = others[0] if others else None

    def Lfun(j, a, b):
        if j != "k_x":
            return E.L(j, a, b)
        if mode == "copy":
            return E.L(E.comps[0], a, b)
        if mode == "idle":
            return E.full(E.comps[0])
        if (a, b) == x and bad is not None:
            return frozenset([(bad,)])
        return frozenset((w,) for w in E.dom[c.deltaE])
    E2 = Org(E.name + "+k_x", E.ports, E.dom, list(E.comps) + ["k_x"], foot, E.B, E.A, E._compose, Lfun, meta=E.meta)
    return c.replace(E=E2, name=c.name + "+k_x")


def small_v36():
    section("C. V3.6 (D15.8: 𝒯 := {t : Θ admits t}): the pole's forward organization, t and t' = t plus a part the stated construction lacks")
    D = pole()
    C1, _, _ = pole_contracts(D)
    p = Question(D, C1, "b1_45", PortQuery(), "L", name="p_prod")
    t = pole_fwd_candidate(p)
    H = [(ONE, "b1_45")]
    others = [x for x in sorted(p.C, key=repr) if x not in H]
    stated = list(t.E.comps)
    variants = [("idle", extra_part(t, "idle")), ("copy", extra_part(t, "copy"))]
    for (a, b) in others:
        variants.append(("deviate at (%s,%s)" % (a, b), extra_part(t, "deviate", (t.tau[a], t.sigma[b]))))
    rows = []
    for v in ("none", "V3.6"):
        s108s3.set_variant(v)
        for lab, t2 in variants:
            h2 = Hist(["o1"], [], set(p.C), admitted=True, prepares=False, parts=list(t2.E.comps), stated=stated)
            h1 = Hist(["o1"], [], set(p.C), admitted=True, prepares=False, parts=list(t.E.comps), stated=stated)
            s2, k2 = sel(t2, H, h2), con(h2)
            s1 = sel(t, H, h1)
            pop = [x for x, h in ((t, h1), (t2, h2)) if s108s3.in_population(True, h.parts, h.stated)]
            surv = [x for x in pop if faithful_on(x, H)]
            under = [(a, b) for (a, b) in others if len(set(repr(x.ans_E(x.tau[a], x.sigma[b])) for x in surv)) > 1]
            acc2 = bool(account(t2))
            rows.append((v, lab, "Acc(t) %s, Acc(t') %s; t' faithful on H %s; Sel(t) %s, Sel(t') %s, Dec(t') %s, Account ∧ ¬Dec(t') %s; |𝒯| %d, survivors on H %d; underdetermined pairs of C1∖H: %d %s"
                         % (tf(account(t)), tf(acc2), tf(faithful_on(t2, H)), tf(s1), tf(s2), tf(not s2 and not k2), tf(acc2 and s2), len(pop), len(surv), len(under), under[:3])))
    s108s3.set_variant("none")
    for r in rows:
        print("%-6s %-38s %s" % r)


def small_v37():
    section("C. V3.7 (D11.4 without the dependence conjunct): FC75's and FC76's routes")
    cases = [
        ("FC75 (a) did no work: i→m (m := 0)→r", Circuit({"m": (("i",), lambda x: 0), "r": (("m",), lambda x: x)}, {"i": 1}), {"i", "m", "r"}, None),
        ("FC75 (a′) dependence only outside R: R = {i, r}", Circuit({"c": (("i",), lambda x: x), "m": (("c",), lambda x: x), "r": (("m", "i"), lambda x, y: x)}, {"i": 1}), {"i", "r"}, None),
        ("FC75 (a″) a side component c", Circuit({"m": (("i", "c"), lambda x, y: (x, y)), "r": (("m",), lambda z: z[0])}, {"i": 1, "c": 5}), {"i", "c", "m", "r"}, None),
        ("FC75 (b) at rest, reading (a)", Circuit({"m": (("i",), lambda x: x), "r": (("m", "late"), lambda x, y: x)}, {"i": 1, "late": 0}), {"i", "m", "r"}, {"i": (0, 0), "m": (1, 1), "late": (8, 8), "r": (9, 9)}),
        ("FC75 (d) an idle member 'side'", Circuit({"m": (("i",), lambda x: x), "n": (("m",), lambda x: x), "r": (("n",), lambda x: x), "side": (("i",), lambda x: 0)}, {"i": 1}), {"i", "m", "n", "r", "side"}, None),
        ("FC76 the response route obj→resp→act", Circuit({"resp": (("obj",), lambda x: x), "act": (("resp",), lambda x: x)}, {"obj": 1}), {"obj", "resp", "act"}, None),
    ]
    for lab, h, R, times in cases:
        i = "obj" if "obj" in R else "i"
        r = "act" if "act" in R else "r"
        res = []
        for v in ("none", "V3.7"):
            s108s3.set_variant(v)
            res.append(act_route(h, R, i, r, [(0, 1)], times, "a"))
        s108s3.set_variant("none")
        print("%-52s none %s (%s) | V3.7 %s (%s)%s" % (lab, tf(res[0][0]), res[0][1], tf(res[1][0]), res[1][1], "   MOVES" if res[0][0] != res[1][0] else ""))


def small_v38():
    section("C. V3.8 (D14.7 without CreativeCriticalEpisode): the bridge (FC84.new1 (a1), (a2)) and (a4)'s labellings, CreateEx over the Θ-values of its other conjuncts")
    theta = ("recognized difficulty", "target represented before its criticism", "a response using the criticism (D9.11)", "Conn(G, h')",
             "Repair (P)", "o in O_ex", "Attempt, New", "Deploy", "ProducesVia", "Acc(c, p_c, t_c, Γ_c, δ_c)")
    chains = (("(a1) no criticism, one contract", [None, None], [0, 1], [0, 1]),
              ("(a2) a first design criticized", [None, ("t0", "fails the load case"), None], [0, 0, 1], [0, 0, 1]),
              ("(a4) I191: the question a criticism aimed at the brief", [("C_brief (the contract)", "why this brief?"), None], [0, 1], [0, 1]),
              ("(a4) I192 (d): a question label, no criticism", [None, None], [0, 1], [0, 1]))
    for lab, crit, held, trace in chains:
        n = len(held)
        fps = prov_fixed_points(n, held, trace, [0] * n, "T'", True, chain_eps(["C_brief"] * n, [False] * n))
        build = build_at(n, held, trace, "T'", fps[0][0] if fps else frozenset(), n - 1)
        crit_clause = any(x is not None for x in crit)
        res = {}
        for v in ("none", "V3.8"):
            s108s3.set_variant(v)
            vals, true_n = set(), 0
            for bits in itertools.product([False, True], repeat=len(theta)):
                w = dict(zip(theta, bits))
                cce = (crit_clause and w["recognized difficulty"] and w["target represented before its criticism"] and w["a response using the criticism (D9.11)"]
                       and w["Conn(G, h')"] and build and w["Attempt, New"])
                cx = s108s3.create_ex(cce, w["Attempt, New"] and build, w["Repair (P)"] and w["o in O_ex"] and w["Deploy"] and w["ProducesVia"] and w["Acc(c, p_c, t_c, Γ_c, δ_c)"])
                vals.add(cx)
                true_n += cx
            res[v] = (sorted(vals), true_n)
        s108s3.set_variant("none")
        print("%-58s Con at output %s, Build %s | CreateEx values none %s (%d of 1024 true) | V3.8 %s (%d of 1024 true)"
              % (lab, [sc[n - 1][1] for R, sc in fps], tf(build), res["none"][0], res["none"][1], res["V3.8"][0], res["V3.8"][1]))
    print("   with every other conjunct met (repair, origin, Account, Deploy, ProducesVia): CreateEx none = the criticism clause ∧ CCE's own conjuncts; V3.8 = T on every chain above")


def main():
    part_a()
    part_b()
    small_v31()
    small_v32()
    small_v33()
    small_v34()
    small_v35()
    small_v36()
    small_v37()
    small_v38()


if __name__ == "__main__":
    main()
