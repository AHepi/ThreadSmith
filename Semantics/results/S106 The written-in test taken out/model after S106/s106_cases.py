# S106 (decisions S44, S45): every worked case of the text, the round-2 and round-3 models that stand for the text's
# sentences, and the owner's own examples (the weathervane, S41 Q15; the shop sign, S44; the hand-turned vane of R3-Q1),
# each candidate's (E) computed twice: round 3's (E) (NC1 a conjunct; under the four readings of D6.3's quantifier)
# and (E) after S106 (NC1 out; the quantifier then changes nothing). A case MOVES when its (E) after S106 differs from
# round 3's (E) under the default reading ('every'); a move under another reading only is marked too.
# Run from "results/S106 The written-in test taken out/model after S106":  PYTHONHASHSEED=0 python3 -B s106_cases.py
# Standard library only; imports the package model/ of this folder and changes none of it; writes nothing.
# FC-E1 to FC-E5 (s104_external.py) and CT1 to CT8 (s104_creative_transport.py) are run separately.
# S106, second checker on the critical review: objection 5's case added (Mimo's τ' restricted to a contract of H settings
# only, θ at 45); objection 1: the row of D⁺'s organization on the further question p^r deleted (parked, P8).
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from model import core  # noqa: E402
from model.core import (ONE, BOT, Org, Question, PortQuery, Candidate, Translation, account, slot,  # noqa: E402
                        SLOT_QUANTIFIERS)
from model.cases import pole, pole_fwd_candidate, pole_rev_candidate, single_settings, fibre_query, COT  # noqa: E402
from model.claims_a import pole_contracts, table_candidate, area2_lookups, _org, _T  # noqa: E402
from model.claims_r3a2 import m5, m13, elim  # noqa: E402
from model.claims_b import e8_contract_org, e6_parts  # noqa: E402
from model.claims_s106 import sign_question, sign_two, sign_one, sign_mech  # noqa: E402
from model import e9  # noqa: E402


def row(c):
    old = {}
    q0 = core.SLOT_QUANTIFIER
    try:
        for q in SLOT_QUANTIFIERS:
            core.SLOT_QUANTIFIER = q
            old[q] = account(c, reading="r3")
    finally:
        core.SLOT_QUANTIFIER = q0
    new, d = account(c, detail=True, reading="S106")
    slots = [k for k in c.E.comps if slot(c, k)] if getattr(c.p.Q, "kind", None) == "port" else []
    return old, new, d, slots


def tf(x):
    return "T" if x else "F"


RESULTS = []


def case(label, where, c, note=""):
    old, new, d, slots = row(c)
    moved_every = old["every"] != new
    moved_other = [q for q in SLOT_QUANTIFIERS[1:] if old[q] != new]
    mark = "MOVED" if moved_every else ("moves under %s only" % ", ".join(moved_other) if moved_other else "-")
    RESULTS.append((label, mark))
    conj = ", ".join("%s %s" % (k, tf(d[k])) for k in ("F1", "F2", "A", "Dep", "NonVacuous", "NC1") if k in d)
    print("%-58s %-26s round 3's (E) %s | after S106 %s | %s" % (label, where, "(" + ",".join(tf(old[q]) for q in SLOT_QUANTIFIERS) + ")", tf(new), mark))
    print("%58s %-26s conjuncts: %s; slots (every): %s%s" % ("", "", conj, slots or "none", ("; " + note) if note else ""))


def main():
    print("S106: every worked case, round 3's (E) under the readings (every, some, some-exempt, some-exempt-set) and (E) after S106")
    print("=" * 150)
    # E1 the pole and its shadow (L325; FC26, FC27, FC28, FC23.new1)
    D = pole()
    C1, C2, _ = pole_contracts(D)
    C3 = frozenset([(ONE, "b1_45")] + [(a, "b1_45") for a in single_settings(D, ["L"])])
    for nm, C in (("C1", C1), ("C2", C2), ("C3", C3)):
        p = Question(D, C, "b1_45", PortQuery(), "L", name=nm)
        case("E1 pole, forward organization, %s" % nm, "L325, L271; FC26", pole_fwd_candidate(p))
    p1 = Question(D, C1, "b1_45", PortQuery(), "L", name="p_prod")
    r = pole_rev_candidate(p1)
    case("E1 pole, reversed calculation, production C1", "L271, L325; FC27", r)
    inv = D.meta["inv"]
    lab = {v: k for k, v in inv.items()}

    def tau2(a):  # Mimo's τ' (FC27's look), as claims_a.fc27 builds it
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
    case("E1 pole, reversed calculation under Mimo's τ', C1", "FC27 (look)", r.replace(tau={a: x for a, x in t2.items() if x is not None}, name="ℰ_rev τ'"))
    # critical review, objection 5: τ' restricted to a production contract of H settings only (θ at 45)
    CH = frozenset([(ONE, "b1_45")] + [(a, "b1_45") for a in single_settings(D, ["H"])])
    pH = Question(D, CH, "b1_45", PortQuery(), "L", name="C_H")
    rH = pole_rev_candidate(pH)
    case("E1 pole, reversed calculation under Mimo's τ', H only", "FC27 (look); review obj. 5",
         rH.replace(tau={a: t2[a] for a in sorted(set(x for x, _ in CH), key=repr)}, name="ℰ_rev τ' (H only)"),
         "τ' restricted to C_H's edits; L271, L325 speak of C1 (H and θ settings), where (F2)'s composition clause excludes it")
    Did = pole(bounds=[(1, 45), (2, 45), (3, 45)])
    pid = Question(Did, frozenset((ONE, b) for b in Did.B), "b1_45", fibre_query(), ("H", "T", "L"), name="p_ident")
    case("E1 pole, reversed calculation, identification C_id", "L325, L151; FC28", pole_rev_candidate(pid, delta=("H", "T", "L")),
         "fibre query: no slot is defined for it (I82)")
    # tables (L269; FC25, FC25.new2)
    for nm, C in (("C1", C1), ("C2", C2)):
        p = Question(D, C, "b1_45", PortQuery(), "L", name=nm)
        case("L269 table of observed answers E_tab, pole %s" % nm, "L269; FC25", table_candidate(p, list(D.ports)))
        case("L269 encoding table E_enc, pole %s" % nm, "L269; FC25, FC25.new2", table_candidate(p, list(D.ports), encode=True))
    # 'p because p' (L273): the pole's answer written into one component on L
    for nm, C in (("C1", C1),):
        p = Question(D, C, "b1_45", PortQuery(), "L", name=nm)
        tab = {(a, b): (frozenset([(p.ans(a, b),)]) if p.ans(a, b) is not BOT else frozenset((x,) for x in D.dom["L"])) for a in D.A for b in D.B}
        E = Org("E_lk", ["L"], {"L": D.dom["L"]}, ["k"], {"k": ("L",)}, D.B, D.A, D._compose, lambda j, a, b: tab[(a, b)])
        c = Candidate(E, p, {"L": Translation(("L",))}, {a: a for a in D.A}, {b: b for b in D.B}, {"k": (frozenset(D.comps), {"L": Translation(("L",))})}, ["k"], "L",
                      name="ℰ_lk")
        case("L273 'p because p': the pole's L written in, %s" % nm, "L273; FC23", c)
    # relabelings (L257; FC21 (d))
    D6 = Org("D", ["y"], {"y": (0, 1)}, ["c"], {"c": ["y"]}, ["b0"], [ONE, "a"], lambda a2, a1: None, lambda j, a, b: {(0,)})
    p6 = Question(D6, [(ONE, "b0"), ("a", "b0")], "b0", PortQuery(), "y")
    rel6 = {("k", ONE, "b0"): {(0, 0), (1, 1)}, ("k", "e1", "b0"): {(0, 0), (1, 1)}, ("k", "e2", "b0"): {(0, 0), (1, 1)},
            ("m", ONE, "b0"): {(1,)}, ("m", "e1", "b0"): {(0,)}, ("m", "e2", "b0"): {(0,)}}
    E6 = Org("E", ["y", "z"], {"y": (0, 1), "z": (0, 1)}, ["k", "m"], {"k": ["y", "z"], "m": ["z"]}, ["b0"], [ONE, "e1", "e2"],
             lambda a2, a1: None, lambda j, a, b: rel6[(j, a, b)])
    c6 = Candidate(E6, p6, {"y": Translation(["y"]), "z": Translation(["y"])}, {ONE: "e1", "a": "e2"}, {"b0": "b0"},
                   {"k": (frozenset(["c"]), {"y": Translation(["y"]), "z": Translation(["y"])}), "m": (frozenset(["c"]), {"z": Translation(["y"])})},
                   ["k", "m"], "y")
    case("L257 a contract of relabelings, τ(1) ≠ 1", "L257; FC21 (d)", c6)
    # the readers' lookups M1-M3, M5 (FC23 (c), (d)), the weathervane M13 (S41 Q15)
    for nm, (c, _ans) in area2_lookups().items():
        case(nm, "L255-L257 ruling; FC23 (c)", c)
    case("M5: the answer fixed at each pair by another part", "FC23 (d), FC23.new1", m5())
    case("M13: the owner's weathervane (S41 Q15)", "FC22 (b)", m13())
    # R3-Q1's hand-turned vane: still air, any direction; turned north by hand
    Dv = _org("D_vane", ["y"], {"y": ("N", "S")}, ["c_y"], {"c_y": ("y",)}, ["b0"], [ONE, "turn"], {("c_y", "turn", "b0"): {("N",)}})
    pv = Question(Dv, [(ONE, "b0"), ("turn", "b0")], "b0", PortQuery(), "y", name="p_vane")
    case("R3-Q1: the hand-turned vane ('north when turned')", "R3-Q1 side 1", Candidate(Dv, pv, _T("y"), {ONE: ONE, "turn": "turn"}, {"b0": "b0"},
                                                                                   {"c_y": (frozenset(["c_y"]), _T("y"))}, ["c_y"], "y", name="ℰ_vane"))
    # E5 eliminative explanation (L339; FC62; FC23.new1 (g))
    for nm, kind in (("FC62's encoding", "const"), ("the second encoding", "two")):
        _p, c = elim(kind)
        case("E5 eliminative (L339), %s" % nm, "L339; FC62, FC23.new1 (g)", c)
    # E8: the question whether p's contract has a defect, a criticism's question (K1; FC107)
    Dc, invd, _ = e8_contract_org()
    sets = [a for a in Dc.A if a != ONE and set(dict(invd[a])) == {"m_1_b0"}]
    pd = Question(Dc, [(ONE, "β")] + [(a, "β") for a in sets], "β", PortQuery(), "m_1_b0", name="p_δ")
    lam = {k: (frozenset([k]), {v: Translation((v,)) for v in Dc.foot[k]}) for k in Dc.comps}
    case("E8 p_δ, the identity candidate (K1's criticism question)", "L590, L377; FC107", Candidate(Dc, pd, {v: Translation((v,)) for v in Dc.ports},
                                                                                                    {a: a for a in Dc.A}, {b: b for b in Dc.B}, lam, list(Dc.comps), "m_1_b0"))
    # E9: the two-layer episode, S1 with t1 on the extended contract (Argument 10; FC102.new1, FC103.new1)
    D9 = e9.object_layer()
    C9 = [(a, b) for a in D9.A for b in D9.B]
    p9 = e9.question(D9, C9)
    E9 = e9.sim_layer_S1()
    case("E9 two-layer episode, S1 with t1 (L626)", "L626; FC102.new1", e9.t1_candidate(p9, E9))
    case("E9 two-layer episode, S1 with t1∘ψ (L630)", "L630; FC103.new1", e9.t1_candidate(p9, E9, swapped=True))
    # E6 odd-order skew-symmetric matrices (L343; FC63): the Leibniz candidate, fibre-free query (no slot, I82)
    for rd in ("r3", "S106"):
        core.ACCOUNT_READING = rd
        parts = e6_parts()
        print("%-58s %-26s %s: %s" % ("E6 skew-symmetric, Leibniz candidate (c-i), (c-ii)", "L343; FC63", "round 3's (E)" if rd == "r3" else "after S106",
                                      "; ".join("%s %s" % (p["label"][:6], p["status"]) for p in parts)))
    core.ACCOUNT_READING = "S106"
    RESULTS.append(("E6 skew-symmetric (FC63 (c-i), (c-ii))", "- (query not a port query: no slot, I82)"))
    # the owner's shop sign (S44)
    p = sign_question()
    case("S44 the shop sign, two parts (red on Mon, blue on Tue)", "S44; FC23.new2 (a)", sign_two(p))
    case("S44 the shop sign, one part (red on Mon, blue on Tue)", "S44; FC23.new2 (b)", sign_one(p))
    case("the sign with a day port and a palette rule", "I189", sign_mech())
    print("=" * 150)
    print("Worked cases with no candidate's (E) computed (unchanged: no NC1 in them): E2 identification (L329; FC57, FC58), E3 the two balances (L331; FC59, FC60),")
    print("E4 obstruction (L335; FC61), E7 transport results (L353-L363; FC64-FC66), the route examples of Part VI (L307-L311; FC37-FC40, set systems).")
    moved = [(l, m) for l, m in RESULTS if m == "MOVED"]
    other = [(l, m) for l, m in RESULTS if m not in ("MOVED", "-") and not m.startswith("-")]
    print("MOVED (round 3's (E) under 'every' -> after S106): %d" % len(moved))
    for l, m in moved:
        print("   %s" % l)
    print("moves under another reading of the quantifier only: %d" % len(other))
    for l, m in other:
        print("   %s: %s" % (l, m))
    print("cases: %d; unchanged under every reading: %d" % (len(RESULTS), sum(1 for _, m in RESULTS if m.startswith("-"))))


if __name__ == "__main__":
    main()
