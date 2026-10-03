"""Second checker (S108 Part A round 1): the owner's two cases, the change read as an edit (the program's M13 and
claims_s106 sign) and as a boundary (FC28.new2's D_vane; the sign with Monday/Tuesday as boundaries). Run from inside a
section copy (cwd = 'section N model'); reads only; writes nothing. Prints (E), its conjuncts, Dependence's witness,
and the slots under the four readings of D6.3's quantifier."""
import sys
from model import core
from model.core import Org, Question, Candidate, Translation, PortQuery, ONE, account, NC2, slot, SLOT_QUANTIFIERS
from model.claims_r3a2 import m13
from model.claims_s106 import sign_two, sign_one, sign_mech

COL = ("red", "blue", "green")


def T(*vs):
    return {v: Translation([v]) for v in vs}


def vane_boundary(gamma):
    def Lf(j, a, b):
        if j == "cW":
            return frozenset([({"b_still": 0, "b_north": 1, "b_gusty": 2}[b],)])
        return frozenset([(0, "n"), (0, "s"), (1, "n"), (2, "s"), (2, "e")])
    D = Org("D_vane", ["W", "P"], {"W": (0, 1, 2), "P": ("n", "s", "e")}, ["cW", "cP"], {"cW": ["W"], "cP": ["W", "P"]},
            ["b_still", "b_north", "b_gusty"], [ONE], lambda a2, a1: ONE, Lf)
    p = Question(D, [(ONE, "b_still"), (ONE, "b_north")], "b_still", PortQuery(), "P")
    lam = {"cW": (frozenset(["cW"]), {"W": Translation(["W"])}),
           "cP": (frozenset(["cP"]), {"W": Translation(["W"]), "P": Translation(["P"])})}
    return Candidate(D, p, T("W", "P"), {ONE: ONE}, {b: b for b in D.B}, lam, list(gamma), "P",
                     name="vane-boundary Γ=" + "".join(gamma))


def _sign_org(name, comps, rel):
    box = {}

    def Lf(j, a, b):
        return frozenset(rel[(j, b)]) if (j, b) in rel else box["o"].full(j)
    box["o"] = Org(name, ["colour"], {"colour": COL}, comps, {k: ("colour",) for k in comps}, ["mon", "tue"], [ONE],
                   lambda a2, a1: ONE, Lf)
    return box["o"]


def sign_boundary(parts):
    D = _sign_org("D_sign_b", ["r", "u"], {("r", "mon"): {("red",)}, ("u", "tue"): {("blue",)}})
    p = Question(D, [(ONE, "mon"), (ONE, "tue")], "mon", PortQuery(), "colour")
    if parts == 2:
        E, lam, G = D, {k: (frozenset([k]), T("colour")) for k in ("r", "u")}, ["r", "u"]
    else:
        E = _sign_org("E_one_b", ["k"], {("k", "mon"): {("red",)}, ("k", "tue"): {("blue",)}})
        lam, G = {"k": (frozenset(["r", "u"]), T("colour"))}, ["k"]
    return Candidate(E, p, T("colour"), {ONE: ONE}, {"mon": "mon", "tue": "tue"}, lam, G, "colour",
                     name="sign-boundary %d-part" % parts)


CASES = [("vane as edit (M13)", m13), ("vane as boundary Γ={cP}", lambda: vane_boundary(["cP"])),
         ("vane as boundary Γ={cW,cP}", lambda: vane_boundary(["cW", "cP"])),
         ("sign as edit, two parts (ℰ_two)", sign_two), ("sign as edit, one part (ℰ_one)", sign_one),
         ("sign as edit, day port (ℰ_day)", sign_mech),
         ("sign as boundary, two parts", lambda: sign_boundary(2)), ("sign as boundary, one part", lambda: sign_boundary(1))]


def row(nm, c):
    acc, d = account(c, detail=True)
    conj = {k: d.get(k) for k in ("F1", "F2", "A", "Dep", "NC1", "NonVacuous") if k in d}
    w = NC2(c, witness=True)
    sl = {q: [k for k in c.E.comps if slot(c, k, quantifier=q)] for q in SLOT_QUANTIFIERS}
    return "%-34s Acc %-5s %s witness %s slots %s" % (nm, acc, conj, w, sl)


if __name__ == "__main__":
    tag = sys.argv[1] if len(sys.argv) > 1 else ""
    print("==", tag)
    for nm, f in CASES:
        print(row(nm, f()))
