# S108 Part A, section 2 (the computing agent, rule 5.1): every worked case the program builds, with each in-scope
# variant of section 2 off and on: Acc (E) and Account ∧ ¬Dec(t) under four histories set by hand (Θ, I90), as
# claims_s41.provenance_of has them. Also the reply's own small cases, built and run, and the cases its traces name.
# Run from "results/S108 Part A - computation/section 2 model":  PYTHONHASHSEED=0 python3 -B s108_s2_cases.py [--json FILE]
# Standard library only. Imports the package model/ of this folder (the copy, with core.S2_VARIANT) and s106_cases.py;
# changes neither's files; writes only the --json file if asked. An experiment on a copy: no theory text is changed.
import itertools
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from model import core  # noqa: E402
from model.core import (ONE, BOT, Org, Question, PortQuery, Candidate, Translation, account, NC2, NC1, hom,  # noqa: E402
                        restrict, routes, conf_claim, conflict_pairs, problem_kind, rivals, F1, F2, A)
from model.cases import pole, pole_fwd_candidate, pole_rev_candidate, fibre_query  # noqa: E402
from model.claims_b import Hist, sel, con, fwd_pole_cand, e6_parts  # noqa: E402
from model.claims_s41 import provenance_of  # noqa: E402
from model.claims_r4a3 import seasons_target, seasons_question, tilt, myth_written, myth_told, GREEKS, EVERY_PAIR  # noqa: E402
import s106_cases  # noqa: E402

VARIANTS = [v for v in core.S2_VARIANTS if v != "off"]
HISTORIES = ("Con", "Sel H={(1,b0)}", "nothing tried, H=∅", "Dec (not admitted)")


def with_variant(v, fn, *a, **k):
    old = core.S2_VARIANT
    core.S2_VARIANT = v
    try:
        return fn(*a, **k)
    finally:
        core.S2_VARIANT = old


def dec_of(c, hist):
    """Dec(t) for one history set by hand (I90): Con = a trace prepares t, cod t held; Sel = a selection history on
    H = {(1,b0)}; 'nothing tried' = no pair tried, no trace, Θ admits t (FC30.new1 (e), FC77); Dec = Θ admits no selection."""
    if hist == "Con":
        return provenance_of(c, "Con", [(ONE, c.p.b0)])[2]
    if hist == "Sel H={(1,b0)}":
        return provenance_of(c, "Sel", [(ONE, c.p.b0)])[2]
    if hist == "Dec (not admitted)":
        return provenance_of(c, "Dec", [(ONE, c.p.b0)])[2]
    h = Hist([], [], set(c.p.C), admitted=True, prepares=False)
    return not sel(c, [], h) and not con(h)


def conj(d):
    return ",".join("%s%s" % (k, "T" if d.get(k) else "F") for k in ("F1", "F2", "A", "Dep", "NonVacuous", "NC1") if k in d)


def row(label, where, c):
    out = {"label": label, "where": where, "acc": {}, "detail": {}, "expl": {}}
    for v in core.S2_VARIANTS:
        val, d = with_variant(v, account, c, detail=True)
        out["acc"][v] = bool(val)
        out["detail"][v] = conj(d)
        try:
            out["expl"][v] = {h: bool(val) and not with_variant(v, dec_of, c, h) for h in HISTORIES}
        except Exception as e:  # a candidate whose transport does not translate the pairs of H
            out["expl"][v] = {h: None for h in HISTORIES}
            out["expl_error"] = repr(e)[:120]
    return out


# ---- the cases ---------------------------------------------------------------------------------------

def written_in_step_cases():
    """Every candidate s106_cases.py builds (the case script of the written-in step), collected, not printed."""
    got = []
    orig_case, orig_print = s106_cases.case, s106_cases.__dict__.get("print")
    s106_cases.case = lambda label, where, c, note="": got.append((label, where, c))
    orig_e6 = s106_cases.e6_parts
    s106_cases.e6_parts = lambda: []
    import builtins
    real_print = builtins.print
    builtins.print = lambda *a, **k: None
    try:
        s106_cases.main()
    finally:
        builtins.print = real_print
        s106_cases.case = orig_case
        s106_cases.e6_parts = orig_e6
        core.ACCOUNT_READING = "S106"
    return got


def more_worked_cases():
    got = []
    # E_fwd on the identification contract C_id = {1} × B (the reply's V2.3 trace names it)
    Did = pole(bounds=[(1, 45), (2, 45), (3, 45)])
    pid = Question(Did, frozenset((ONE, b) for b in Did.B), "b1_45", fibre_query(), ("H", "T", "L"), name="p_ident")
    got.append(("E1 pole, forward organization, identification C_id", "L329, E1; V2.3 trace", pole_fwd_candidate(pid)))
    # the student's declared formula (FC30.new1): the pole's forward candidate on H settings, θ at 45
    p, c = fwd_pole_cand()
    got.append(("the student's declared formula (FC30.new1): ℰ_fwd on H settings", "S41 Q2; FC30.new1", c))
    # the winter myth (FC72.new2): the Greeks' contract and the finer one
    D = seasons_target()
    pG, pF = seasons_question(GREEKS, "p_Greeks", D), seasons_question(EVERY_PAIR, "p_finer", D)
    for q, nm in ((pG, "Greeks' C"), (pF, "finer C")):
        got.append(("FC72.new2 the tilt, %s" % nm, "FC72.new2", tilt(q)))
        got.append(("FC72.new2 the myth written in (ℰ_myth1), %s" % nm, "FC72.new2", myth_written(q)))
        got.append(("FC72.new2 the myth as told (ℰ_myth2), %s" % nm, "FC72.new2", myth_told(q)))
    return got


def v21_case():
    """The reply's V2.1 case, as written: ports x, y, z ∈ {0,1}; cx:(x), cy:(x,y), dz:(z); B = {b0}; A = {1, e}, e·e
    undefined; L_cx(1,b0) full, L_cx(e,b0) = {(1)}; L_cy = {(0,0),(1,1)}; L_dz full at both pairs; Q_w reads y; C = both
    pairs; ℰ = D with the identity transport, Γ = {dz}, λ(dz) = ({dz}, z := id(z)), δ_E = y."""
    rel = {("cx", "e", "b0"): {(1,)}}
    for a in (ONE, "e"):
        rel[("cy", a, "b0")] = {(0, 0), (1, 1)}

    def L(j, a, b):
        if (j, a, b) in rel:
            return frozenset(rel[(j, a, b)])
        return D.full(j)
    D = Org("D_v21", ["x", "y", "z"], {"x": (0, 1), "y": (0, 1), "z": (0, 1)}, ["cx", "cy", "dz"],
            {"cx": ("x",), "cy": ("x", "y"), "dz": ("z",)}, ["b0"], [ONE, "e"], lambda a2, a1: None, L)
    p = Question(D, [(ONE, "b0"), ("e", "b0")], "b0", PortQuery(), "y", name="p_v21")
    lam = {"dz": (frozenset(["dz"]), {"z": Translation(("z",))})}
    return Candidate(D, p, {v: Translation((v,)) for v in D.ports}, {ONE: ONE, "e": "e"}, {"b0": "b0"}, lam, ["dz"], "y", name="ℰ_v21")


def two_commitment(kind):
    """Finite route cases of Part VI built as candidates (the reply's V2.2 trace and its unsettled edge on L309):
    target: x an input (edit e sets x = 1), y = x (component c_y). 'redundant' (L307): Γ = {a, b}, both y = x, each alone
    a route. 'interference' (L309): Γ = {a, b}, a: y = x, b: y = 0; the full candidate fails (E), {a} meets it."""
    def Ld(j, a, b):
        if j == "c_x":
            return frozenset([(1,)]) if a == "e" else frozenset([(0,)])
        return frozenset([(0, 0), (1, 1)])
    D = Org("D_xy", ["x", "y"], {"x": (0, 1), "y": (0, 1)}, ["c_x", "c_y"], {"c_x": ("x",), "c_y": ("x", "y")}, ["b0"], [ONE, "e"],
            lambda a2, a1: None, Ld)
    p = Question(D, [(ONE, "b0"), ("e", "b0")], "b0", PortQuery(), "y", name="p_xy")
    if kind == "redundant":
        rb = frozenset([(0, 0), (1, 1)])
    else:
        rb = frozenset([(0, 0), (1, 0)])

    def Le(j, a, b):
        if j == "c_x":
            return Ld(j, a, b)
        if j == "a":
            return frozenset([(0, 0), (1, 1)])
        return rb
    E = Org("E_" + kind, ["x", "y"], {"x": (0, 1), "y": (0, 1)}, ["c_x", "a", "b"], {"c_x": ("x",), "a": ("x", "y"), "b": ("x", "y")},
            ["b0"], [ONE, "e"], lambda a2, a1: None, Le)
    lam = {"c_x": (frozenset(["c_x"]), {"x": Translation(("x",))}),
           "a": (frozenset(["c_y"]), {"x": Translation(("x",)), "y": Translation(("y",))}),
           "b": (frozenset(["c_y"]), {"x": Translation(("x",)), "y": Translation(("y",))})}
    return Candidate(E, p, {v: Translation((v,)) for v in E.ports}, {ONE: ONE, "e": "e"}, {"b0": "b0"}, lam, ["a", "b"], "y",
                     name="ℰ_" + kind)


def fmt_S(S):
    return "{" + ", ".join("{" + ",".join(sorted(W)) + "}" for W in sorted(S, key=lambda W: (len(W), sorted(W)))) + "}"


def v27_case():
    """The reply's V2.7 case, as written: ports w, y ∈ {0,1}; c:(w,y); B = {b0}; A = {1}; L_c(1,b0) = {(1,0)}; Q_w reads
    y; C = {(1,b0)}; ℰ = D, identity transport, Γ = {c}, δ_E = y; χ: Allow_χ(1,b0) = {R : R_c = {(0,0)}}."""
    D = Org("D_v27", ["w", "y"], {"w": (0, 1), "y": (0, 1)}, ["c"], {"c": ("w", "y")}, ["b0"], [ONE], lambda a2, a1: None,
            lambda j, a, b: frozenset([(1, 0)]))
    p = Question(D, [(ONE, "b0")], "b0", PortQuery(), "y", name="p_v27")
    c = Candidate(D, p, {"w": Translation(("w",)), "y": Translation(("y",))}, {ONE: ONE}, {"b0": "b0"},
                  {"c": (frozenset(["c"]), {"w": Translation(("w",)), "y": Translation(("y",))})}, ["c"], "y", name="ℰ_v27")
    allow = lambda R: R["c"] == frozenset([(0, 0)])  # noqa: E731
    return c, allow


def main():
    want_json = sys.argv[sys.argv.index("--json") + 1] if "--json" in sys.argv else None
    P = print
    rows = []
    cases = written_in_step_cases() + more_worked_cases()
    for label, where, c in cases:
        rows.append(row(label, where, c))
    P("S108 Part A, section 2: the worked cases, Acc (E) with each variant off and on, and Account ∧ ¬Dec(t) under four histories set by hand")
    P("cases: %d (the %d of the written-in step's script, then %d more)" % (len(rows), len(rows) - len(more_worked_cases()), len(more_worked_cases())))
    P("=" * 140)
    P("%-66s %s" % ("case", "Acc: off | " + " ".join(VARIANTS)))
    for r in rows:
        P("%-66s %s | %s" % (r["label"][:66], "T" if r["acc"]["off"] else "F", " ".join(("T" if r["acc"][v] else "F") + ("*" if r["acc"][v] != r["acc"]["off"] else " ") for v in VARIANTS)))
    P("(* = differs from off)")
    P("=" * 140)
    moved = {}
    for v in VARIANTS:
        acc_moves = [(r["label"], r["acc"]["off"], r["acc"][v], r["detail"]["off"], r["detail"][v]) for r in rows if r["acc"][v] != r["acc"]["off"]]
        ex_moves = []
        for r in rows:
            for h in HISTORIES:
                a, b = r["expl"]["off"][h], r["expl"][v][h]
                if a != b:
                    ex_moves.append((r["label"], h, a, b))
        moved[v] = dict(acc=acc_moves, expl=ex_moves)
        P("%s: Acc moves on %d case(s); Account ∧ ¬Dec(t) moves on %d (case, history) pair(s)" % (v, len(acc_moves), len(ex_moves)))
        for lab, a, b, d0, d1 in acc_moves:
            P("   Acc %s -> %s  %s   [off %s | on %s]" % ("T" if a else "F", "T" if b else "F", lab, d0, d1))
        for lab, h, a, b in ex_moves:
            P("   Account ∧ ¬Dec(t) %s -> %s  %s, history '%s'" % (a, b, lab, h))
    P("=" * 140)
    # E6: the Leibniz candidate, computed inside e6_parts (its account and NC2 witness in the part's text)
    P("E6 skew-symmetric, the Leibniz candidate (FC63 (c-i), (c-ii)): status of each part, off and on")
    e6 = {}
    for v in core.S2_VARIANTS:
        parts = with_variant(v, e6_parts)
        e6[v] = [(pp["label"][:6], pp["status"], pp["result"][-160:]) for pp in parts]
        P("   %-5s %s" % (v, "; ".join("%s %s" % (a, b) for a, b, _ in e6[v])))
    P("=" * 140)
    # the reply's own small cases
    P("The reply's small cases, built and run")
    c = v21_case()
    for v in ("off", "V2.1"):
        val, d = with_variant(v, account, c, detail=True)
        P("   V2.1 case (%s): Ans at (1,b0) %r, at (e,b0) %r; conjuncts %s; NC2 witness %s; (E) %s" % (
            v, c.ans_E(ONE, "b0"), c.ans_E("e", "b0"), conj(d), with_variant(v, NC2, c, witness=True), val))
    P("   V2.1 case: the transport's provenance is not in the case; Account ∧ ¬Dec(t) under the four histories, off / V2.1: %s / %s"
      % (row("", "", c)["expl"]["off"], row("", "", c)["expl"]["V2.1"]))
    for kind in ("redundant", "interference"):
        c = two_commitment(kind)
        for v in ("off", "V2.1", "V2.2", "V2.3", "V2.4"):
            val, d = with_variant(v, account, c, detail=True)
            S = with_variant(v, routes, c)
            P("   %s (L%s) %-5s: full candidate (E) %s [%s]; routes S = %s; NC2 witness %s" % (
                kind, "307" if kind == "redundant" else "309", v, val, conj(d), fmt_S(S), with_variant(v, NC2, c, witness=True)))
    c, allow = v27_case()
    for v in ("off", "V2.7"):
        first, second = with_variant(v, conf_claim, c, ONE, "b0", allow, parts=True)
        whole = with_variant(v, conf_claim, c, ONE, "b0", allow)
        P("   V2.7 case (%s): ConfCl first disjunct %s, second %s, ConfCl %s; the candidate's (E) %s [%s]" % (
            v, first, second, whole, with_variant(v, account, c), conj(with_variant(v, account, c, detail=True)[1])))
    # V2.6: the tilt and the myth (FC72.new2 (b), (d))
    D = seasons_target()
    pG, pF = seasons_question(GREEKS, "p_Greeks", D), seasons_question(EVERY_PAIR, "p_finer", D)
    for v in ("off", "V2.6"):
        for q, nm in ((pG, "Greeks' C"), (pF, "finer C")):
            t = tilt(q)
            for m in (myth_written(q), myth_told(q)):
                P("   V2.6 %-5s %-9s tilt against %s: conflict pairs %s; rivals %s; kind %s" % (
                    v, nm, m.name, with_variant(v, conflict_pairs, t, m), with_variant(v, rivals, t, m), with_variant(v, problem_kind, t, m)))
    # V2.5: the student's declared copy, H = ∅ (FC30.new1 (e)), and Hom(τ)
    p, c = fwd_pole_cand()
    for v in ("off", "V2.5"):
        h = Hist([], [], set(c.p.C))
        s = with_variant(v, sel, c, [], h)
        s_explicit = with_variant(v, sel, c, [], h, h_nonempty=True)
        P("   V2.5 %-5s the student's copy, nothing tried (H = ∅): Sel %s (explicit 'H ≠ ∅' reading %s); Con %s; Dec %s; Hom(τ) %s; Acc %s; Account ∧ ¬Dec(t) %s"
          % (v, s, s_explicit, con(h), not s and not con(h), hom(c), account(c), account(c) and (s or con(h))))
    if want_json:
        with open(want_json, "w", encoding="utf-8") as f:
            json.dump(dict(rows=[{k: r[k] for k in ("label", "where", "acc", "detail", "expl")} for r in rows], moved=moved,
                           e6={v: [(a, b) for a, b, _ in e6[v]] for v in e6}), f, ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
