# S108 Part A, Sonnet 5.5 trial, section 2: the external examples FC-E1 to FC-E5 (s104_external.py) and the creative transport
# case CT1 to CT8 (s104_creative_transport.py), each named candidate computed with no variant on and with each of V2.1 to V2.7
# on (core.S2_ON): Acc (E), and Acc and not Dec in three provenance scenarios (Theta by hand, I90; claims_s41.provenance_of):
# (i) constructed (Con), (ii) declared, no pair tried (H = empty), (iii) declared with one pair tried (H = {(1, b0)}).
# The candidates are built by the two scripts' own functions (e1_org, copy_candidate, restrict, restrict_removing, mem_orgs,
# target, question, candidate); the populations of 256 pairs (CT2, CT4, CT5) are covered by the printouts of the two scripts run
# with each variant on (their lines do not move; see the .md), FC-E2, FC-E3 and FC-E5 build no candidate and call no Acc.
# Run from the folder "section 2 model":  PYTHONHASHSEED=0 python3 -B s108_section2_external.py [json path]
# Standard library only; imports the package model/ and the two scripts of this folder; writes nothing but the printout (and
# the json when a path is given). Nothing here changes the theory (S40).
import io
import json
import os
import sys
from contextlib import redirect_stdout

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from model import core  # noqa: E402
from model import claims_b  # noqa: E402
from model.core import ONE, account, restrict, Question, PortQuery, Translation  # noqa: E402
from model.claims_s41 import provenance_of  # noqa: E402
import s104_external as ext  # noqa: E402
import s104_creative_transport as ct  # noqa: E402

VARIANTS = ["V2.1", "V2.2", "V2.3", "V2.3b", "V2.4", "V2.5", "V2.6", "V2.7"]


def set_on(v):
    core.S2_ON.clear()
    if v:
        core.S2_ON.add(v)
    claims_b.SEL_H_NONEMPTY = "V2.5" not in core.S2_ON


def tf(x):
    return "T" if x else "F"


def build():
    cands = []
    # FC-E1 (I103, I104)
    D = ext.e1_org("D_E1")
    C = [(a, "b0") for a in D.A]
    p = Question(D, C, "b0", PortQuery(), "Y", name="p_E1")
    c = ext.copy_candidate(D, p, ext.e1_org("E_E1"), ["k", "d"], "Y")
    cands.append(("FC-E1 full candidate, Gamma = {k,d}", c))
    cands.append(("FC-E1 E|{k} (I29, deletion)", restrict(c, {"k"})))
    cands.append(("FC-E1 variant (a), d in the named background, Gamma = {k}", c.replace(Gamma=("k",), name="E with d in the background")))
    cands.append(("FC-E1 variant (b), the restriction of I104 (E|{k}, ports removed)", ext.restrict_removing(c, {"k"})))
    # FC-E4
    D4, E4 = ext.mem_orgs()
    tr = lambda j: {v: Translation((v,)) for v in E4.foot[j]}  # noqa: E731
    lam = {"c_X": (frozenset(["c_X"]), tr("c_X")), "c_M": (frozenset(["c_M"]), tr("c_M")),
           "c_N": (frozenset(["c_N"]), tr("c_N")), "c_Yp": (frozenset(["c_N", "c_Y"]), tr("c_Yp"))}
    C1 = [(ONE, "b0"), (ext.edit(D4, X=0), "b0"), (ext.edit(D4, X=1), "b0")]
    C2 = C1 + [(ext.edit(D4, X=1, N=0), "b0")]
    for Gname, Gamma in (("Gamma = {c_M,c_N,c_Yp}", ["c_M", "c_N", "c_Yp"]), ("Gamma = {c_Yp}", ["c_Yp"])):
        for Cname, CC in (("C1", C1), ("C2", C2)):
            pp = Question(D4, CC, "b0", PortQuery(), "Y", name="p_mem")
            cands.append(("FC-E4 %s, %s" % (Gname, Cname), ext.copy_candidate(D4, pp, E4, Gamma, "Y", lam=lam)))
    # CT1, CT3, CT5, CT6, CT7, CT8 (the candidates the printout names)
    EQ, XOR, SECOND = ct.EQ, ct.XOR, ct.SECOND
    Dq, pol = ct.target(EQ, "D_EQ")
    pq, cases = ct.question(Dq, pol, "p_EQ")
    cands.append(("CT1 chosen pair (equality, equality) on p_EQ", ct.candidate(pq, EQ, EQ, pol, name="E_EQ,EQ")))
    D0, pol0 = ct.target(EQ, "D_nosender", with_sender=False)
    p0, _ = ct.question(D0, pol0, "p_nosender")
    cands.append(("CT3 reading R-B, target without the sender, Gamma = {dec}", ct.candidate(p0, EQ, EQ, pol0, with_sender=False, name="E_EQ,EQ on R-B")))
    Dn, poln = ct.target(SECOND, "D_noninverting", b_dom=(0,))
    pn, _ = ct.question(Dn, poln, "p_noninverting")
    cands.append(("CT5 the direct pair on the target whose polarity cannot invert", ct.candidate(pn, SECOND, SECOND, poln, name="E_direct")))
    Ds, pols = ct.target(SECOND, "D_direct")
    ps, _ = ct.question(Ds, ["b"], "p")
    cands.append(("CT5 the direct pair on the full target p", ct.candidate(ps, SECOND, SECOND, ["b"], name="E_direct_full")))
    polcp = ["b1", "b2"]
    for s_, nm in ((EQ, "equality pair"), (XOR, "xor pair")):
        Dx, _ = ct.target(s_, "D_changing", two_polarities=True)
        px, _ = ct.question(Dx, polcp, "p_changing")
        cands.append(("CT6 varying polarity, the %s" % nm, ct.candidate(px, s_, s_, polcp)))
    Dp, polp = ct.target(EQ, "D_e")
    pp2, _ = ct.question(Dp, ["b"], "p_e")
    cands.append(("CT7 the chosen pair, no reference level", ct.candidate(pp2, EQ, EQ, ["b"], history=False, name="E_EQ,EQ, no reference")))
    cands.append(("CT8 the chosen pair on the run's eight settings", ct.candidate(pp2, EQ, EQ, ["b"])))
    return cands


def evaluate(c):
    v = bool(account(c))
    prov = {}
    b0 = c.p.b0
    for lab, kind, H in (("con", "Con", [(ONE, b0)]), ("decl_H0", "Sel", []), ("decl_H1", "Sel", [(ONE, b0)])):
        s, k, dec = provenance_of(c, kind, H)
        prov[lab] = bool(v and not dec)
    return {"acc": v, "acc_not_dec": prov}


def main():
    cands = build()
    table = {}
    for v in [""] + VARIANTS:
        set_on(v)
        for label, c in cands:
            table.setdefault(label, {})[v or "off"] = evaluate(c)
    set_on("")
    print("S108 section 2, external examples FC-E1..FC-E5 and creative transport CT1..CT8: named candidates, Acc (E) and")
    print("Acc and not Dec, no variant on (off) and each variant on; T holds, F fails; scenarios (i) constructed, (ii) declared with")
    print("no pair tried, (iii) declared with one pair tried")
    print("=" * 130)
    moves = 0
    for label, c in cands:
        row = table[label]
        off = row["off"]
        print("%s   |Gamma| = %d" % (label, len(c.Gamma)))
        print("   off: Acc %s   Acc&notDec (i) %s (ii) %s (iii) %s" % (tf(off["acc"]), tf(off["acc_not_dec"]["con"]), tf(off["acc_not_dec"]["decl_H0"]), tf(off["acc_not_dec"]["decl_H1"])))
        for v in VARIANTS:
            on = row[v]
            mv = []
            if on["acc"] != off["acc"]:
                mv.append("Acc %s->%s" % (tf(off["acc"]), tf(on["acc"])))
            for k, nm in (("con", "(i)"), ("decl_H0", "(ii)"), ("decl_H1", "(iii)")):
                if on["acc_not_dec"][k] != off["acc_not_dec"][k]:
                    mv.append("Acc&notDec %s %s->%s" % (nm, tf(off["acc_not_dec"][k]), tf(on["acc_not_dec"][k])))
            if mv:
                moves += 1
                print("   %-5s MOVES: %s" % (v, "; ".join(mv)))
    print("=" * 130)
    print("candidate-by-variant results that move: %d" % moves)
    if len(sys.argv) > 1:
        with open(sys.argv[1], "w", encoding="utf-8") as f:
            json.dump(table, f, ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
