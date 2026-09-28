# S108 Part A, Sonnet 5.5 trial, section 2: the small cases the reply gives (and a few it names by line), each built here and
# computed with no variant on (off) and with each of V2.1 to V2.7 on (V2.3b: V2.3 read as tau(a) other than 1).
# Cases: A (V2.1's x, y, z), B (L307, redundant routes), C (a finite cousin of L311, routes of two or more), D (L309,
# interference), E (V2.7's wheel), F (the tilt and the myth, FC72.new2 (b), (d)), G (a candidate with no commitments),
# H (the pole's forward and reversed calculation on the identification contract, FC28), I (a contract {1} x B, any candidate),
# J (the x, y, z target with the contract {(1, b0)} only: the contrast the reply's case A has lies outside C; L275.n1, FC29).
# Run from the folder "section 2 model":  PYTHONHASHSEED=0 python3 -B s108_section2_small.py [json path]
# Standard library only; imports the package model/; writes nothing but the printout (and the json when a path is given).
# Nothing here changes the theory (S40).
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from model import core, claims_b  # noqa: E402
from model.core import (ONE, BOT, Question, PortQuery, Candidate, account, routes, minimal, NC2, conflict_pairs, rivals,  # noqa: E402
                        problem_kind, conf_claim, F1, NC1)
from model.claims_s106 import _org, _ident_lam  # noqa: E402
from model.claims_a import _T  # noqa: E402
from model.claims_r4a3 import seasons_target, seasons_question, tilt, myth_written, myth_told, GREEKS, EVERY_PAIR  # noqa: E402
from model.cases import pole, pole_fwd_candidate, pole_rev_candidate, fibre_query  # noqa: E402

VARIANTS = ["V2.1", "V2.2", "V2.3", "V2.3b", "V2.4", "V2.5", "V2.6", "V2.7"]


def set_on(v):
    core.S2_ON.clear()
    if v:
        core.S2_ON.add(v)
    claims_b.SEL_H_NONEMPTY = "V2.5" not in core.S2_ON


def tf(x):
    return "T" if x else "F"


def sv(x):
    return "⊥" if x is BOT else str(x)


def fmt_routes(S):
    return "{" + ", ".join("{" + ",".join(sorted(W)) + "}" for W in sorted(S, key=lambda W: (len(W), sorted(W)))) + "}"


def cand_row(c):
    v, d = account(c, detail=True)
    S = routes(c) if len(c.Gamma) <= 6 else None
    w = NC2(c, witness=True)
    return dict(acc=bool(v), conj={k: bool(d[k]) for k in ("F1", "F2", "A", "NC1", "Dep", "NonVacuous") if k in d},
                witness=repr(w) if w else None, routes=fmt_routes(S) if S is not None else "skipped",
                min_routes=fmt_routes(minimal(S)) if S is not None else "skipped")


# ---- the cases ----------------------------------------------------------------------------------------------------

def case_A():
    """V2.1's x, y, z (the reply, section (b))."""
    full_xy = None  # noqa: F841
    rel = {("cx", "e", "b0"): {(1,)}, ("cy", ONE, "b0"): {(0, 0), (1, 1)}, ("cy", "e", "b0"): {(0, 0), (1, 1)}}
    D = _org("D_xyz", ["x", "y", "z"], {"x": (0, 1), "y": (0, 1), "z": (0, 1)}, ["cx", "cy", "dz"],
             {"cx": ("x",), "cy": ("x", "y"), "dz": ("z",)}, ["b0"], [ONE, "e"], rel)
    p = Question(D, [(ONE, "b0"), ("e", "b0")], "b0", PortQuery(), "y", name="p_xyz")
    c = Candidate(D, p, _T("x", "y", "z"), {ONE: ONE, "e": "e"}, {"b0": "b0"}, _ident_lam(D), ["dz"], "y", name="ℰ_xyz (Γ = {dz})")
    return [("A. V2.1's x, y, z: identity transport, Γ = {dz}", c, "Ans_p(1,b0) = ⊥ and Ans_p(e,b0) = 1 are the reply's values")]


def case_B():
    """L307: Γ = {ja, jb}, each alone a route (redundant routes)."""
    rel = {("ja", ONE, "b0"): {(1,)}, ("jb", ONE, "b0"): {(1,)}, ("ja", "e", "b0"): {(0,)}, ("jb", "e", "b0"): {(0,)}}
    D = _org("D_red", ["x"], {"x": (0, 1)}, ["ja", "jb"], {"ja": ("x",), "jb": ("x",)}, ["b0"], [ONE, "e"], rel)
    p = Question(D, [(ONE, "b0"), ("e", "b0")], "b0", PortQuery(), "x", name="p_red")
    c = Candidate(D, p, _T("x"), {ONE: ONE, "e": "e"}, {"b0": "b0"}, _ident_lam(D), ["ja", "jb"], "x", name="ℰ_red (Γ = {ja,jb})")
    return [("B. L307 redundant routes: two parts each giving the answer", c, "S = {{a},{b},{a,b}} is L307's set system")]


def case_C():
    """A finite cousin of L311: three commitments, x in {0,1,2,3}; any one leaves two values open, any two fix x."""
    dom = (0, 1, 2, 3)
    rel = {}
    excl1 = {"d1": {1, 2}, "d2": {2, 3}, "d3": {1, 3}}     # at (1,b0): any two leave only 0
    excl2 = {"d1": {0, 1}, "d2": {1, 2}, "d3": {0, 2}}     # at (e,b0): any two leave only 3
    for d in ("d1", "d2", "d3"):
        rel[(d, ONE, "b0")] = {(v,) for v in dom if v not in excl1[d]}
        rel[(d, "e", "b0")] = {(v,) for v in dom if v not in excl2[d]}
    D = _org("D_thr2", ["x"], {"x": dom}, ["d1", "d2", "d3"], {"d1": ("x",), "d2": ("x",), "d3": ("x",)}, ["b0"], [ONE, "e"], rel)
    p = Question(D, [(ONE, "b0"), ("e", "b0")], "b0", PortQuery(), "x", name="p_thr2")
    c = Candidate(D, p, _T("x"), {ONE: ONE, "e": "e"}, {"b0": "b0"}, _ident_lam(D), ["d1", "d2", "d3"], "x", name="ℰ_thr2 (Γ = {d1,d2,d3})")
    return [("C. a finite cousin of L311: no route of one commitment, every pair a route", c, "the text's Γ = {d_n : n in N} is infinite; a Candidate is finite [I77]; this cousin has no one-commitment route")]


def case_D():
    """L309: Γ = {ka, kb}; kb is not faithful to its counterpart, ka is; y reads x (no slot: the answer port is fixed by a background part)."""
    rel = {("ja", ONE, "b0"): {(1,)}, ("ja", "e", "b0"): {(0,)}, ("jc", ONE, "b0"): {(0, 0), (1, 1)}, ("jc", "e", "b0"): {(0, 0), (1, 1)}}
    D = _org("D_int", ["x", "y"], {"x": (0, 1), "y": (0, 1)}, ["ja", "jb", "jc"], {"ja": ("x",), "jb": ("x",), "jc": ("x", "y")}, ["b0"], [ONE, "e"], rel)
    p = Question(D, [(ONE, "b0"), ("e", "b0")], "b0", PortQuery(), "y", name="p_int")
    rel2 = {("ka", ONE, "b0"): {(1,)}, ("ka", "e", "b0"): {(0,)}, ("kb", ONE, "b0"): {(0,)},
            ("kc", ONE, "b0"): {(0, 0), (1, 1)}, ("kc", "e", "b0"): {(0, 0), (1, 1)}}
    E = _org("E_int", ["x", "y"], {"x": (0, 1), "y": (0, 1)}, ["ka", "kb", "kc"], {"ka": ("x",), "kb": ("x",), "kc": ("x", "y")}, ["b0"], [ONE, "e"], rel2)
    lam = {"ka": (frozenset(["ja"]), _T("x")), "kb": (frozenset(["jb"]), _T("x")), "kc": (frozenset(["jc"]), _T("x", "y"))}
    c = Candidate(E, p, _T("x", "y"), {ONE: ONE, "e": "e"}, {"b0": "b0"}, lam, ["ka", "kb"], "y", name="ℰ_int (Γ = {ka,kb}, kb unfaithful)")
    return [("D. L309 interference: the full candidate fails, a subset meets", c, "S = {{a}} is L309's set system: kb's relation at (1,b0) differs from its counterpart's, so (F1) fails for the full Γ")]


def case_E():
    """V2.7's wheel: D with ports w, y; comp c; L_c(1,b0) = {(1,0)}; C = {(1,b0)}; chi allows only R with R_c = {(0,0)}."""
    D = _org("D_wheel", ["w", "y"], {"w": (0, 1), "y": (0, 1)}, ["c"], {"c": ("w", "y")}, ["b0"], [ONE], {("c", ONE, "b0"): {(1, 0)}})
    p = Question(D, [(ONE, "b0")], "b0", PortQuery(), "y", name="p_wheel")
    c = Candidate(D, p, _T("w", "y"), {ONE: ONE}, {"b0": "b0"}, _ident_lam(D), ["c"], "y", name="ℰ_wheel")
    allow = lambda R: R["c"] == frozenset({(0, 0)})  # noqa: E731
    return c, allow


def case_G():
    """A candidate with no commitments: the identity transport on the x, y, z target with Γ = {} (V2.1)."""
    (_, cA, _), = case_A()
    c = cA.replace(Gamma=(), name="ℰ_xyz (Γ = {})")
    return [("G. a candidate with no commitments (Γ = {}), the x, y, z target", c, "not in the reply: what V2.1 does at Γ = {}")]


def case_H():
    """The pole's forward and reversed calculation on the identification contract {1} x B (FC28; s106_cases' C_id)."""
    Did = pole(bounds=[(1, 45), (2, 45), (3, 45)])
    pid = Question(Did, frozenset((ONE, b) for b in Did.B), "b1_45", fibre_query(), ("H", "T", "L"), name="p_ident")
    rev = pole_rev_candidate(pid, delta=("H", "T", "L"))
    fwd = pole_fwd_candidate(pid)
    return [("H1. the reversed calculation on C_id = {1} x B (FC28)", rev, "the reply: meets (E) before, stops under V2.3"),
            ("H2. the forward calculation (identity) on C_id = {1} x B", fwd, "the reply: stops under V2.3 as well")]


def case_I():
    """A contract {1} x B with two boundaries on a small target: any candidate; here the x, y, z target with B = {b0, b1}."""
    rel = {("cx", ONE, "b1"): {(1,)}, ("cy", ONE, "b0"): {(0, 0), (1, 1)}, ("cy", ONE, "b1"): {(0, 0), (1, 1)}}
    D = _org("D_id2", ["x", "y", "z"], {"x": (0, 1), "y": (0, 1), "z": (0, 1)}, ["cx", "cy", "dz"],
             {"cx": ("x",), "cy": ("x", "y"), "dz": ("z",)}, ["b0", "b1"], [ONE], rel)
    p = Question(D, [(ONE, "b0"), (ONE, "b1")], "b0", PortQuery(), "y", name="p_id2")
    c = Candidate(D, p, _T("x", "y", "z"), {ONE: ONE}, {"b0": "b0", "b1": "b1"}, _ident_lam(D), ["cx", "dz"], "y", name="ℰ_id2 (Γ = {cx,dz})")
    return [("I. a contract {1} x B with two boundaries: identity transport, Γ = {cx,dz}", c, "the reply: no candidate meets (E) on any {1} x B contract under V2.3")]


def case_J():
    """As case A, but the contract is {(1,b0)} only: the pair (e,b0), where the answer changes, is outside C (L275.n1, FC29)."""
    rel = {("cx", "e", "b0"): {(1,)}, ("cy", ONE, "b0"): {(0, 0), (1, 1)}, ("cy", "e", "b0"): {(0, 0), (1, 1)}}
    D = _org("D_xyz1", ["x", "y", "z"], {"x": (0, 1), "y": (0, 1), "z": (0, 1)}, ["cx", "cy", "dz"],
             {"cx": ("x",), "cy": ("x", "y"), "dz": ("z",)}, ["b0"], [ONE, "e"], rel)
    p = Question(D, [(ONE, "b0")], "b0", PortQuery(), "y", name="p_xyz_1")
    c = Candidate(D, p, _T("x", "y", "z"), {ONE: ONE, "e": "e"}, {"b0": "b0"}, _ident_lam(D), ["dz"], "y", name="ℰ_xyz1 (Γ = {dz}, C = {(1,b0)})")
    return [("J. as case A with the contract {(1,b0)} only: the contrast lies outside C", c, "L275.n1 / FC29: NC2's contrast lies on tau[C]; V2.1 must not read a contrast outside C")]


def main():
    cands = []
    for f in (case_A, case_B, case_C, case_D, case_G, case_H, case_I, case_J):
        cands.extend(f())
    out = {"candidate_cases": {}, "conflict_cases": {}}
    print("S108 section 2, the small cases: Acc (E) with no variant on (off) and with each variant on; T holds, F fails")
    print("=" * 140)
    for label, c, note in cands:
        p = c.p
        print("%s   [%s]" % (label, note))
        print("   answers Ans_p at C: %s" % ", ".join("(%s,%s)=%s" % (a, b, sv(p.ans(a, b))) for (a, b) in sorted(p.C, key=repr)))
        print("   candidate's answers: %s" % ", ".join("(%s,%s)=%s" % (a, b, sv(c.ans_E(c.tau[a], c.sigma[b]))) for (a, b) in sorted(p.C, key=repr)))
        rows = {}
        for v in [""] + VARIANTS:
            set_on(v)
            rows[v or "off"] = cand_row(c)
        set_on("")
        off = rows["off"]
        print("   off : Acc %s  conj %s  witness %s  S %s" % (tf(off["acc"]), off["conj"], off["witness"], off["routes"]))
        for v in VARIANTS:
            r = rows[v]
            mv = []
            if r["acc"] != off["acc"]:
                mv.append("Acc %s->%s" % (tf(off["acc"]), tf(r["acc"])))
            if r["routes"] != off["routes"]:
                mv.append("S %s -> %s" % (off["routes"], r["routes"]))
            if r["witness"] != off["witness"]:
                mv.append("witness %s -> %s" % (off["witness"], r["witness"]))
            print("   %-5s %s   (Acc %s; conj %s)" % (v, ("MOVES: " + "; ".join(mv)) if mv else "no move", tf(r["acc"]), r["conj"]))
        out["candidate_cases"][label] = rows
    # E: the wheel
    print("=" * 140)
    c, allow = case_E()
    print("E. V2.7's wheel: ConfCl(ℰ, χ; 1, b0), χ = perpetual motion is impossible (Allow: R_c = {(0,0)}); parts (first, second disjunct, area 2 reading)")
    print("   Ans_p(1,b0) = %s; ℰ answers %s" % (sv(c.p.ans(ONE, "b0")), sv(c.ans_E(ONE, "b0"))))
    wheel = {}
    for v in [""] + VARIANTS:
        set_on(v)
        parts = conf_claim(c, ONE, "b0", allow, parts=True)
        whole = conf_claim(c, ONE, "b0", allow)
        wheel[v or "off"] = dict(first=bool(parts[0]), second=bool(parts[1]), ConfCl=bool(whole))
        print("   %-5s first %s second %s  ConfCl %s" % (v or "off", tf(parts[0]), tf(parts[1]), tf(whole)))
    set_on("")
    out["conflict_cases"]["E wheel"] = wheel
    # F: the tilt and the myth
    print("=" * 140)
    D = seasons_target()
    pG = seasons_question(GREEKS, "p_Greeks", D)
    pF = seasons_question(EVERY_PAIR, "p_finer", D)
    print("F. FC72.new2 (b), (d): the tilt against the myth (written in, and as told), on the Greeks' contract and on the finer contract")
    fres = {}
    for v in [""] + VARIANTS:
        set_on(v)
        row = {}
        for q, qn in ((pG, "Greeks"), (pF, "finer")):
            t = tilt(q)
            for mk, mn in ((myth_written, "myth1"), (myth_told, "myth2")):
                m = mk(q)
                cps = conflict_pairs(t, m)
                row["%s/%s" % (qn, mn)] = dict(conflict_pairs=[list(x) for x in cps], rivals=bool(rivals(t, m)), kind=problem_kind(t, m),
                                             acc_tilt=bool(account(t)), acc_myth=bool(account(m)))
        fres[v or "off"] = row
        print("   %-5s %s" % (v or "off", "; ".join("%s: pairs %s rivals %s kind %s Acc(tilt) %s Acc(myth) %s" % (k, r["conflict_pairs"], tf(r["rivals"]), r["kind"], tf(r["acc_tilt"]), tf(r["acc_myth"])) for k, r in row.items())))
    set_on("")
    out["conflict_cases"]["F tilt and myth"] = fres
    if len(sys.argv) > 1:
        with open(sys.argv[1], "w", encoding="utf-8") as f:
            json.dump(out, f, ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
