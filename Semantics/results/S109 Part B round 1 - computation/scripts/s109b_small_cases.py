# S109 Part B round 1 (rule 5): the replies' own small cases ("first case to move") that the scope script does not build,
# each computed off ('none') and on (the variant), in the section's copy.
#   PYTHONHASHSEED=0 python3 -B s109b_small_cases.py --model-dir "<section Bn model>" --section Bn
# Writes nothing; prints one block per case.
import argparse
import os
import sys

ap = argparse.ArgumentParser()
ap.add_argument("--model-dir", required=True)
ap.add_argument("--section", required=True)
A_ = ap.parse_args()
sys.path.insert(0, os.path.abspath(A_.model_dir))

from model import core  # noqa: E402
from model.core import ONE, BOT, Org, Question, PortQuery, Candidate, Translation, account  # noqa: E402
from model.claims_a import _org, _T, pole_contracts  # noqa: E402
from model.cases import pole, pole_fwd_candidate  # noqa: E402


def row(label, c, variants):
    out = []
    for v, extra in variants:
        core.S109B = v
        for k, x in extra.items():
            setattr(core, k, x)
        acc, d = account(c, detail=True)
        out.append("   %-22s Acc %s  %s" % (v + (" " + str(extra) if extra else ""), acc, {k: d[k] for k in ("F1", "F2", "A", "Dep", "NonVacuous", "question", "NC0") if k in d}))
        core.S109B = "none"
    print(label + "\n" + "\n".join(out))


def m13_like(L_cy_base, extra_bg=None):
    rel = {("cx", "e", "b0"): {(1,)}, ("cy", ONE, "b0"): {(0, 0), (1, 1)}, ("cy", "e", "b0"): {(0, 0), (1, 1)}}
    D = _org("D", ["x", "y"], {"x": (0, 1), "y": (0, 1)}, ["cx", "cy"], {"cx": ["x"], "cy": ["x", "y"]}, ["b0"], [ONE, "e"], rel)
    p = Question(D, [(ONE, "b0"), ("e", "b0")], "b0", PortQuery(), "y")
    relE = dict(rel)
    if L_cy_base is not None:
        relE[("cy", ONE, "b0")] = L_cy_base
    comps, foot, lam = ["cx", "cy"], {"cx": ["x"], "cy": ["x", "y"]}, {"cx": (frozenset(["cx"]), _T("x")), "cy": (frozenset(["cy"]), _T("x", "y"))}
    if extra_bg:
        comps = comps + ["bg"]
        foot["bg"] = ["y"]
        for a in (ONE, "e"):
            relE[("bg", a, "b0")] = extra_bg[a]
    E = _org("E", ["x", "y"], {"x": (0, 1), "y": (0, 1)}, comps, foot, ["b0"], [ONE, "e"], relE)
    return Candidate(E, p, _T("x", "y"), {ONE: ONE, "e": "e"}, {"b0": "b0"}, lam, ["cy"], "y", name="ℰ")


S = A_.section
if S == "B1":
    # PB1.6: the reply's idle-commitment case: E = D, h on p0 answers, c on p1 idle (full), Γ = {c}
    rel = {("h", ONE, "b0"): {(0,)}, ("h", "e", "b0"): {(1,)}}
    D = _org("D", ["p0", "p1"], {"p0": (0, 1), "p1": (0, 1)}, ["h", "c"], {"h": ["p0"], "c": ["p1"]}, ["b0"], [ONE, "e"], rel)
    p = Question(D, [(ONE, "b0"), ("e", "b0")], "b0", PortQuery(), "p0")
    c = Candidate(D, p, _T("p0", "p1"), {ONE: ONE, "e": "e"}, {"b0": "b0"}, {"h": (frozenset(["h"]), _T("p0")), "c": (frozenset(["c"]), _T("p1"))}, ["c"], "p0")
    row("PB1.6 the reply's case: Γ = {c}, c idle for the answer (full relation on p1)", c, [("none", {}), ("PB1.6", {})])
    # PB1.1: a question stating a smaller exclusion than (A×B)∖C (Excl(Σ) = ∅), the pole's forward candidate on C1
    Dp = pole()
    C1, _, _ = pole_contracts(Dp)
    cp = pole_fwd_candidate(Question(Dp, C1, "b1_45", PortQuery(), "L", excl=frozenset(), name="C1, Excl(Σ) = ∅"))
    row("PB1.1 the pole's forward candidate on C1 with Excl(Σ) = ∅ (a silently narrowed contract)", cp, [("none", {}), ("PB1.1", {})])
    # PB1.7 / PB1.3: the pole's identification question is in the scope script's worked cases (C_id); nothing more here
if S == "B2":
    row("PB2.4 the reply's case: M13 with E's L_cy(1,b0) = {(0,1)} (E answers 1 where the target gives ⊥)", m13_like({(0, 1)}), [("none", {}), ("PB2.4", {})])
    row("PB2.4 a second case: M13 with E's L_cy(1,b0) = {(0,0)} (E answers 0 where the target gives ⊥)", m13_like({(0, 0)}), [("none", {}), ("PB2.4", {})])
    row("PB2.5 the reply's case: M13 with a background component bg fixing y := 1 at every pair", m13_like(None, {ONE: {(1,)}, "e": {(1,)}}),
        [("none", {}), ("PB2.5", {"S109B_NC0": "bg"}), ("PB2.5", {"S109B_NC0": "bg-input"})])
    row("PB2.5 M13 with a background component bg fixing y := 1 only at e (where the target's answer is 1)", m13_like(None, {ONE: {(0,), (1,)}, "e": {(1,)}}),
        [("none", {}), ("PB2.5", {"S109B_NC0": "bg"}), ("PB2.5", {"S109B_NC0": "bg-input"})])
    row("PB2.3 M13 (Γ = {cy}); cx is a background component with a counterpart", m13_like(None), [("none", {}), ("PB2.3", {})])
    c = m13_like(None)
    E2 = _org("E", ["x", "y"], {"x": (0, 1), "y": (0, 1)}, ["cx", "cy", "k1"], {"cx": ["x"], "cy": ["x", "y"], "k1": ["x"]}, ["b0"], [ONE, "e"],
              {("cx", "e", "b0"): {(1,)}, ("cy", ONE, "b0"): {(0, 0), (1, 1)}, ("cy", "e", "b0"): {(0, 0), (1, 1)}})
    c2 = c.replace(E=E2)
    row("PB2.3 M13 with an added background component k1 on x with no counterpart (full relation, Γ = {cy})", c2, [("none", {}), ("PB2.3", {})])
