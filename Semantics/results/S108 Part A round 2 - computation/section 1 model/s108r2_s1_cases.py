# S108 Part A round 2, section 1: the in-scope variants' cases (R2V1.1, R2V1.6 with R2V1.6s, R2V1.10), the round-1
# candidates resting on the readings they vary (C2 on S108-1-I5, C1 on S108-1-I1), and the computations for round 1's
# claimed-only edges of section 1's share (e1.02, e1.03, e1.14, e1.37, e1.38, e1.39).
#   PYTHONHASHSEED=0 python3 -B s108r2_s1_cases.py OUT.json
# Standard library only; imports this folder's model/ and round 1's case script (worked_cases); prints a report and writes
# only OUT.json. Every history is set by hand (Θ by hand, I90), as the program's own claims set them.
import itertools
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from model import core  # noqa: E402
from model.core import (ONE, BOT, Org, Question, PortQuery, Candidate, Translation, account, proj_lam, F1_at, solve, slice_rel,  # noqa: E402
                        adn, translated_C, Roles)
from model.cases import pole, pole_fwd_candidate, COT  # noqa: E402
from model.claims_a import pole_contracts, table_candidate, SMALL, gen_p_cand  # noqa: E402
from model.claims_r3a2 import m13  # noqa: E402
from model.claims_b import Hist, con, prov_fixed_points, build_at, chain_eps, faithful_on, EPISODE_READINGS  # noqa: E402
from model.claims_s106 import sign_question, sign_two, sign_one  # noqa: E402
from model.claims_s41 import provenance_of, expl_ruled_out, suff_defeats, SUFF_READINGS  # noqa: E402
from model.args import Not, Imp, Assessor  # noqa: E402
from s108_s1_cases import worked_cases  # noqa: E402

OUT = {}


def tf(x):
    return "T" if x else "F"


def set_state(r1="none", r2="none", rho="declared", i1="follows"):
    core.S108_S1 = r1
    core.OBS_READING = "R-i" if r1 == "V1.3" else "R-ii"
    core.S108R2_S1 = r2
    core.S108R2_S1_RHO = rho
    core.S108R2_S1_I1 = i1


def section(t):
    print("=" * 150)
    print(t)
    print("-" * 150)


def hist3(c):
    """(Sel, Con, Dec) under the three hand-set histories of claims_s41.provenance_of, H = {(1, b0)}."""
    H = [(ONE, c.p.b0)]
    return {kind: provenance_of(c, kind, H) for kind in ("Dec", "Con", "Sel")}


# ============================================================================================================== A
# R2V1.1 and C2: S108-1-I5 under each choice. C2 = round 1's V1.5: Account ∧ ρ_p ∈ {selected, constructed} ∧ ¬Dec(t).
C2_STATES = [
    ("none", dict()),
    ("I5: unrecorded ⇒ declared (round 1)", dict(r1="V1.5")),
    ("R2V1.1: recorded declared", dict(r2="R2V1.1", rho="declared")),
    ("R2V1.1: recorded selected", dict(r2="R2V1.1", rho="selected")),
    ("R2V1.1: recorded constructed", dict(r2="R2V1.1", rho="constructed")),
]


def owner_cases():
    """The owner's cases on which C2's flags turn, and the program's companions on the same questions."""
    ps = sign_question()
    c13 = m13()
    return [("S44: the shop sign, two parts (the owner's case)", sign_two(ps)),
            ("S44: the shop sign, one part (the program's companion)", sign_one(ps)),
            ("S44: E_enc on the sign's question", table_candidate(ps, list(ps.D.ports), encode=True)),
            ("S41 Q15: the weathervane's mechanism M13", c13),
            ("S41 Q15: E_enc on the weathervane's question", table_candidate(c13.p, list(c13.p.D.ports), encode=True))]


THETA4 = ("recognized difficulty", "target represented before its criticism", "a response using the criticism (D9.11)",
          "Conn(G, h')", "Repair (P)", "o in O_ex", "Attempt, New", "Deploy", "ProducesVia", "Acc(c, p_c, t_c, Γ_c, δ_c)")


class BriefQuestion:
    """The bridge's question p_c = the fixed brief [S108r2-1-I3]. FC84.new1 builds no (D, C, Q) for it; V1.5's conjunct reads
    only ρ_p, so only ρ_p is carried. rho None: nothing recorded."""
    name = "p_brief"

    def __init__(self, rho):
        self.rho = rho


def brief_rho_from_chain():
    """ρ(C_brief) by D3.4 on FC84.new1's own chain (o1 ≺ o2, q = C_brief throughout, a trace at o2 preparing t, the design):
    constructed :⟺ an episode with a construction trace has C_brief as its content (E8; Con with the contract as the content,
    [S108r2-1-I4]); selected: no population of contracts is in the chain (Sel's conditions none, by hand); declared: neither."""
    h = Hist(["o1", "o2"], [("o2", "cod")], set(), prepares={"t"}, contracts=["C_brief"] * 2, records=[False] * 2)
    constructed = con(h, name="C_brief")
    selected = False
    return "constructed" if constructed else ("selected" if selected else "declared"), constructed


def bridge(rho_brief):
    """FC84.new1 (a1), (a2), (a4): Con and Build at the output (T′, both readings of L55), and CreateEx (D14.7) over the
    1,024 Θ-values of its other conjuncts, with Acc((c, p_c, …)) := the Θ label ∧ (p_c a question, under V1.5 / R2V1.1)."""
    out = {}
    pc = BriefQuestion(rho_brief)
    chains = (("a1: no criticism", 2, [0, 1], [0, 1], [None, None]),
              ("a2: a first design criticized before the built one", 3, [0, 0, 1], [0, 0, 1],
               [None, ("t0 (the first design, at o1)", "fails the load case"), None]),
              ("a4 (I191): a question about the brief labelled a criticism aimed at it", 2, [0, 1], [0, 1],
               [("C_brief (the contract)", "why this brief?"), None]))
    for lab, n, held, trace, crit in chains:
        cb = {}
        for rd in EPISODE_READINGS:
            fps = prov_fixed_points(n, held, trace, [0] * n, "T'", True, chain_eps(["C_brief"] * n, [False] * n, rd))
            cb[rd] = ([sc[n - 1][1] for R, sc in fps], build_at(n, held, trace, "T'", fps[0][0] if fps else frozenset(), n - 1))
        crit_clause = any(x is not None for x in crit)
        q_ok = core.is_question(pc)
        cnt = 0
        for bits in itertools.product([False, True], repeat=len(THETA4)):
            v = dict(zip(THETA4, bits))
            cce = (crit_clause and v["recognized difficulty"] and v["target represented before its criticism"]
                   and v["a response using the criticism (D9.11)"] and v["Conn(G, h')"] and cb["S41"][1] and v["Attempt, New"])
            acc_c = v["Acc(c, p_c, t_c, Γ_c, δ_c)"] and q_ok
            cnt += bool(cce and v["Repair (P)"] and v["o in O_ex"] and v["Deploy"] and v["ProducesVia"] and acc_c)
        out[lab] = dict(con_S41=cb["S41"][0], build_S41=cb["S41"][1], con_L55=cb["L55"][0], build_L55=cb["L55"][1],
                        p_c_question=q_ok, createex_valuations=cnt, of=2 ** len(THETA4))
    return out


def student_copy():
    """FC30.new1 (d): the student's declared copy of the pole's forward candidate on C1; Dec(t) at the student's holding
    computed on the chain (T′), H = {(1, b1_45)}; Expl := Acc ∧ ¬Dec."""
    D = pole()
    C1, _, _ = pole_contracts(D)
    c = pole_fwd_candidate(Question(D, C1, "b1_45", PortQuery(), "L", name="p"))
    acc = bool(account(c))
    held_o = bool(core.faithful(c))
    selc_o = faithful_on(c, [(ONE, "b1_45")])
    fps = prov_fixed_points(2, [1, held_o], [1, 0], [0, selc_o], "T'", True)
    decs = [not sc[1][0] and not sc[1][1] for R, sc in fps]
    return dict(acc=acc, dec=decs, expl=[acc and not d for d in decs])


def part_a():
    section("A. R2V1.1 and C2 (round 1's V1.5) under each choice of S108-1-I5: worked cases, the owner's cases, the bridge, the student's copy")
    wc = worked_cases()
    res = {"worked": {}, "owner": {}, "bridge": {}, "student": {}}
    for st, kw in C2_STATES:
        set_state(**kw)
        acc_t, rows = 0, []
        for lab, c in wc:
            a = bool(account(c))
            h = hist3(c)
            rows.append((lab, a, {k: bool(a and not v[2]) for k, v in h.items()}))
            acc_t += a
        res["worked"][st] = dict(acc_true=acc_t, of=len(wc), expl_con=sum(1 for r in rows if r[2]["Con"]),
                                 expl_sel=sum(1 for r in rows if r[2]["Sel"]), rows=[(r[0], r[1]) for r in rows])
        ow = {}
        for lab, c in owner_cases():
            a, d = account(c, detail=True)
            h = hist3(c)
            ow[lab] = dict(acc=bool(a), question=d.get("question"), expl_con=bool(a and not h["Con"][2]), expl_sel=bool(a and not h["Sel"][2]))
        res["owner"][st] = ow
        res["student"][st] = student_copy()
        print("%-40s worked: Acc T %d of %d; Expl (Con-history) %d, (Sel-history) %d" % (st, acc_t, len(wc), res["worked"][st]["expl_con"], res["worked"][st]["expl_sel"]))
        for lab, v in ow.items():
            print("   %-58s Acc %s%s; Expl Con-history %s, Sel-history %s" % (lab, tf(v["acc"]), "" if v["question"] is None else " (p a question: %s)" % tf(v["question"]), tf(v["expl_con"]), tf(v["expl_sel"])))
        s = res["student"][st]
        print("   S41 Q2: the student's declared copy: Acc %s; Dec(t) at the student's holding %s; Expl %s" % (tf(s["acc"]), s["dec"], s["expl"]))
    # the bridge (S41 Q6): ρ(C_brief) computed from FC84.new1's chain, and each value by hand
    rho_c, constructed = brief_rho_from_chain()
    print("S41 Q6: the bridge. ρ(C_brief) by D3.4 on FC84.new1's chain (Con with the brief as content: %s; no population of contracts): %s" % (tf(constructed), rho_c))
    res["bridge"]["rho_from_chain"] = rho_c
    for st, kw in C2_STATES:
        for rb_lab, rb in (("ρ(brief) as computed from the chain (%s)" % rho_c, rho_c), ("ρ(brief) not recorded", None),
                           ("ρ(brief) selected", "selected"), ("ρ(brief) constructed", "constructed")):
            set_state(**kw)
            b = bridge(rb)
            res["bridge"]["%s | %s" % (st, rb_lab)] = b
            print("   %-40s %-45s %s" % (st, rb_lab, " | ".join("%s: Con(S41) %s Build %s; Con(L55) %s; p_c a question %s; CreateEx at %d of %d" % (
                k.split(":")[0], v["con_S41"], tf(v["build_S41"]), v["con_L55"], tf(v["p_c_question"]), v["createex_valuations"], v["of"]) for k, v in b.items())))
    # which worked cases move (Acc), per state, against none
    base = dict(res["worked"]["none"]["rows"])
    for st, _ in C2_STATES[1:]:
        now = dict(res["worked"][st]["rows"])
        moved = [lab for lab in base if base[lab] != now[lab]]
        res["worked"][st]["moved"] = moved
        print("%s: %d worked case(s) move (all Acc T → F): %s" % (st, len(moved), "; ".join(moved) if len(moved) < 6 else "%s … (%d)" % ("; ".join(moved[:3]), len(moved))))
    set_state()
    OUT["A"] = res


# ============================================================================================================== B
# R2V1.6: Expl := (A) ∧ Dependence ∧ NonVacuous ∧ ¬Dec(t). R2V1.6s: (Suff)'s and (Nec)'s antecedent co-varied.


def judge6(c):
    acc, d = account(c, detail=True)
    n = adn(c)
    h = hist3(c)
    return dict(acc=bool(acc), F1=bool(d.get("F1")), F2=bool(d.get("F2")), A=bool(d.get("A")), Dep=bool(d.get("Dep")),
                NV=bool(d.get("NonVacuous")), adn=bool(n),
                expl_none={k: bool(acc and not v[2]) for k, v in h.items()},
                expl_r2v16={k: bool(n and not v[2]) for k, v in h.items()},
                dec={k: bool(v[2]) for k, v in h.items()})


def defeat_rows(c):
    """(Suff)'s defeat set (L17 as S41 writes it) and (Nec)'s (L61's 'their', FC30.new1 (g)) for c, an argument usable by j
    that rules out Expl(ℰ) (resp. ¬Expl(ℰ)) and does not use (E), under R2V1.6 and R2V1.6s, each hand-set history."""
    from model.claims_s41 import not_using_E
    from model.args import Step, Leaf, X
    rows = {}
    j = Assessor(["MP"], ["r", Imp("r", Not("Expl_" + c.name))])
    out, _ = expl_ruled_out(j, c.name)
    e = "Expl_" + c.name
    beta = Step("MP", e, [Leaf("r", "record"), Leaf(Imp("r", e))])
    jn = Assessor(["MP"], ["r", Imp("r", e)])
    outn = bool([a for a in X(jn, Not(e), [beta]) if not_using_E(a, c.name)])
    for st in ("none", "R2V1.6", "R2V1.6s"):
        set_state(r2=st)
        acc = bool(account(c))
        for kind, (s_, k_, dec) in hist3(c).items():
            base = core.defeat_base(c, acc)
            rows["%s | %s" % (st, kind)] = dict(suff=suff_defeats(base, dec, out, "L17 (S41)"), nec=bool(outn and not (base and not dec)),
                                                expl=bool(core.expl_base(c) and not dec), acc_not_dec=bool(acc and not dec))
    set_state()
    return rows


def capture_script(modname, funcs):
    """Every candidate a script passes to account() (the script's own name for it) while its main() runs, deduplicated by
    identity; its printout is discarded (it is compared elsewhere)."""
    import importlib
    m = importlib.import_module(modname)
    seen, got = set(), []
    orig = m.account

    def wrap(c, *a, **k):
        if id(c) not in seen:
            seen.add(id(c))
            got.append(c)
        return orig(c, *a, **k)
    m.account = wrap
    import io
    import contextlib
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        argv = sys.argv
        sys.argv = [modname + ".py"]
        try:
            m.main()
        finally:
            sys.argv = argv
    m.account = orig
    return got


def part_b():
    section("B. R2V1.6 (Expl without (F1), (F2)) and R2V1.6s: worked cases, the student's copy, FC-E1–E5, CT1–CT8")
    res = {}
    groups = [("worked", worked_cases())]
    ext = capture_script("s104_external", None)
    groups.append(("FC-E1–E5", [("FC-E cand %d: %s on %s" % (i + 1, getattr(c, "name", "?"), getattr(c.p, "name", "?")), c) for i, c in enumerate(ext)]))
    ctc = capture_script("s104_creative_transport", None)
    groups.append(("CT1–CT8", [("CT cand %d: %s on %s" % (i + 1, getattr(c, "name", "?"), getattr(c.p, "name", "?")), c) for i, c in enumerate(ctc)]))
    print("captured while each script's main() ran: FC-E1–E5 %d candidates; CT1–CT8 %d candidates" % (len(ext), len(ctc)))
    for gname, cases in groups:
        set_state()
        rows, entering = [], []
        for lab, c in cases:
            if not translated_C(c) and not getattr(c, "p", None):
                continue
            j = judge6(c)
            rows.append((lab, j))
            if j["adn"] and not j["acc"]:
                entering.append((lab, j))
        res[gname] = dict(n=len(rows), acc_true=sum(1 for _, j in rows if j["acc"]), adn_true=sum(1 for _, j in rows if j["adn"]),
                          a_nv_nodep=[lab for lab, j in rows if j["A"] and j["NV"] and not j["Dep"]],
                          entering=[dict(case=lab, F1=j["F1"], F2=j["F2"], expl_none=j["expl_none"], expl_r2v16=j["expl_r2v16"]) for lab, j in entering],
                          leaving=[lab for lab, j in rows if any(j["expl_none"][k] and not j["expl_r2v16"][k] for k in j["expl_none"])])
        print("%s: %d candidates; Acc T %d; (A) ∧ Dep ∧ NonVacuous T %d; enter being an explanation under R2V1.6 (ADN T, Acc F): %d; leave: %d; (A) ∧ NonVacuous without Dependence (out under R2V1.6 too): %d%s"
              % (gname, len(rows), res[gname]["acc_true"], res[gname]["adn_true"], len(entering), len(res[gname]["leaving"]), len(res[gname]["a_nv_nodep"]),
                 (" (%s)" % "; ".join(res[gname]["a_nv_nodep"])) if 0 < len(res[gname]["a_nv_nodep"]) < 8 else ""))
        for lab, j in entering:
            print("   in: %-70s F1 %s F2 %s | Expl none %s → R2V1.6 %s (Dec-, Con-, Sel-history)" % (
                lab, tf(j["F1"]), tf(j["F2"]), "".join(tf(j["expl_none"][k]) for k in ("Dec", "Con", "Sel")), "".join(tf(j["expl_r2v16"][k]) for k in ("Dec", "Con", "Sel"))))
    # (Suff) and (Nec) under R2V1.6 and R2V1.6s, on the worked cases that enter and on a case that meets (E)
    wc = dict(worked_cases())
    picks = [lab for lab in (e["case"] for e in res["worked"]["entering"])] + ["E1 pole, forward organization, C1"]
    dres = {}
    for lab in picks:
        dres[lab] = defeat_rows(wc[lab])
        print("defeat sets, %s:" % lab)
        for k, v in dres[lab].items():
            print("   %-22s Expl %s; Acc ∧ ¬Dec %s; in (Suff)'s defeat set (L17, S41) %s; in (Nec)'s (L61's 'their') %s" % (k, tf(v["expl"]), tf(v["acc_not_dec"]), tf(v["suff"]), tf(v["nec"])))
    res["defeat_sets"] = dres
    # (Suff) and (Nec) as written, read as conditions on Expl: Account ∧ ¬Dec ⇒ Expl; Expl ⇒ Account ∧ ¬Dec
    viol = {"Suff": 0, "Nec": 0}
    for lab, c in worked_cases():
        for st in ("R2V1.6",):
            set_state(r2=st)
            acc = bool(account(c))
            for kind, (s_, k_, dec) in hist3(c).items():
                ex = bool(core.expl_base(c) and not dec)
                viol["Suff"] += bool(acc and not dec and not ex)
                viol["Nec"] += bool(ex and not (acc and not dec))
    set_state()
    res["as_written"] = viol
    print("under R2V1.6, over the worked cases × 3 histories: (Suff) as written (Account ∧ ¬Dec ⇒ Expl) fails %d times; (Nec) as written (Expl ⇒ Account ∧ ¬Dec) fails %d times" % (viol["Suff"], viol["Nec"]))
    # the student's copy under R2V1.6
    for st in ("none", "R2V1.6"):
        set_state(r2=st)
        D = pole()
        C1, _, _ = pole_contracts(D)
        c = pole_fwd_candidate(Question(D, C1, "b1_45", PortQuery(), "L", name="p"))
        s = student_copy()
        print("S41 Q2, the student's declared copy, %s: Acc %s; ADN %s; Dec %s; Expl %s" % (st, tf(s["acc"]), tf(adn(c)), s["dec"], [bool(core.expl_base(c) and not d) for d in s["dec"]]))
        res["student %s" % st] = dict(s, adn=adn(c))
    set_state()
    OUT["B"] = res


# ============================================================================================================== C
# R2V1.10: S108-1-I1's three readings of ℰ_bv's relation at a ≠ 1, under 'none' and round 1's V1.1 (C1).


def ebv(D, rd):
    bval = D.meta["bval"]

    def Lbv(j, a, b, rd=rd):
        if j == "c_bv":
            if a == ONE:
                uH, uT = bval[b]
                return frozenset([(uH, uT, uH * COT[uT])])
            if rd == "follows":
                return D.sol(a, b)
            if rd == "baseline":
                uH, uT = bval[b]
                return frozenset([(uH, uT, uH * COT[uT])])
            return frozenset(z for b2 in D.B for z in D.sol(a, b2))  # (iii): ∪_{b′∈B} proj_{V_cbv} Sol_D(a, b′) (V_cbv = V_D)
        return D.L({"c_H": "c_H", "c_T": "c_T"}[j], a, b)
    return Org("E_bv", ["H", "T", "L"], dict(D.dom), ["c_H", "c_T", "c_bv"], {"c_H": ("H",), "c_T": ("T",), "c_bv": ("H", "T", "L")}, D.B, D.A, D._compose, Lbv)


def part_c():
    section("C. R2V1.10 and C1 (round 1's V1.1) under each reading of S108-1-I1: ℰ_bv, and C1's flags")
    D = pole()
    C1, C2, _ = pole_contracts(D)
    b0 = "b1_45"
    res = {}
    for rd in ("follows", "baseline", "iii"):
        for nm, C in (("C1", C1), ("C2", C2)):
            p = Question(D, C, b0, PortQuery(), "L", name=nm)
            cbv = Candidate(ebv(D, rd), p, {v: Translation((v,)) for v in D.ports}, {a: a for a in D.A}, {b: b for b in D.B},
                            {"c_bv": (frozenset(["c_L"]), {v: Translation((v,)) for v in ("H", "T", "L")})}, ["c_bv"], "L", name="ℰ_bv")
            for v in ("none", "V1.1"):
                set_state(r1=v)
                acc, d = account(cbv, detail=True)
                f1bad = sorted(((a, b) for (a, b) in C if not F1_at(cbv, a, b)), key=repr)
                ex = f1bad[0] if f1bad else None
                detail = ""
                if ex:
                    detail = "at %s: proj^λ Sol_{c_L} %d tuple(s), L_bv %d tuple(s)" % (ex, len(proj_lam(cbv, "c_bv", D, *ex)), len(cbv.E.L("c_bv", *ex)))
                res["%s | %s | %s" % (rd, nm, v)] = dict(acc=bool(acc), conj={k: bool(d[k]) for k in ("F1", "F2", "A", "Dep", "NonVacuous")}, f1_fails=len(f1bad), of=len(C), first=repr(ex))
                print("   ℰ_bv, I1 %-9s on %s, %-4s: Acc %s [F1 %s F2 %s A %s Dep %s NonVacuous %s]; (F1) fails at %d of %d pairs %s" % (
                    rd, nm, v, tf(acc), tf(d["F1"]), tf(d["F2"]), tf(d["A"]), tf(d["Dep"]), tf(d["NonVacuous"]), len(f1bad), len(C), detail))
    # C1's flag cases do not read I1: the two-part sign, M13, E_enc on M13's question, under none and V1.1
    for v in ("none", "V1.1"):
        set_state(r1=v)
        oc = {lab: bool(account(c)) for lab, c in owner_cases()}
        res["owner | %s" % v] = oc
        print("   owner's cases under %s: %s" % (v, "; ".join("%s %s" % (k.split(":")[1].strip(), tf(x)) for k, x in oc.items())))
    set_state()
    OUT["C"] = res


# ============================================================================================================== D
# Round 1's claimed-only edges of section 1's share.


def part_d():
    section("D. Round 1's claimed-only edges: e1.02, e1.03, e1.14, e1.37, e1.38, e1.39 (the nearest the program computes)")
    res = {}
    wc = worked_cases()
    # e1.02: L233.s1's words, two readings: W1 impose λ(k)'s constraints alone (I14); W2 impose them in D, restrict to V_N (V1.1)
    agree = {"W1 = proj_lam under none": [0, 0], "W2 = proj_lam under V1.1": [0, 0], "W1 = W2": [0, 0]}
    for lab, c in wc:
        D = c.p.D
        for k in c.Gamma:
            N, tr = c.lam[k]
            for (a, b) in c.p.C:
                VN = D.ports if frozenset(N) >= frozenset(D.comps) else D.ports_of(N)
                cons = [(D.foot[j], D.L(j, a, b)) for j in D.comps if j in N]
                w1 = frozenset(solve(VN, D.dom, cons))
                full = [z for z in D.sol(a, b) if all(tuple(dict(zip(D.ports, z))[u] for u in D.foot[j]) in D.L(j, a, b) for j in N)]
                w2 = D.proj(frozenset(full), D.ports, VN)
                for st in ("none", "V1.1"):
                    set_state(r1=st)
                    _, S = D.sol_sub(N, a, b)
                    key = "W1 = proj_lam under none" if st == "none" else "W2 = proj_lam under V1.1"
                    agree[key][0] += (S == (w1 if st == "none" else w2))
                    agree[key][1] += 1
                agree["W1 = W2"][0] += (w1 == w2)
                agree["W1 = W2"][1] += 1
    set_state()
    res["e1.02"] = agree
    print("e1.02: over every worked candidate, k ∈ Γ, (a,b) ∈ C: %s" % "; ".join("%s at %d of %d" % (k, v[0], v[1]) for k, v in agree.items()))
    # e1.03: L556.n2 under V1.1: sig_C(λ(k)) by D4.4 (reads Sol_N), sig_{τ[C]}(k) by (K) (D4.1); (F1) at (a,b) ⟺ third coordinates equal
    ok, tot, k_ext, k_tot = 0, 0, 0, 0
    set_state(r1="V1.1")
    for lab, c in wc:
        D = c.p.D
        for (a, b) in c.p.C:
            if not c.translates(a, b):
                continue
            eq = all(proj_lam(c, k, D, a, b) == c.E.L(k, c.tau[a], c.sigma[b]) for k in c.Gamma)
            ok += (eq == F1_at(c, a, b))
            tot += 1
            for j in D.comps:  # D4.4's 'extends (K)' for N = {j}: sig_C({j})(a,b) = L_j(a,b)?
                VN, S = D.sol_sub([j], a, b)
                k_ext += (D.proj(S, VN, D.foot[j]) == D.L(j, a, b))
                k_tot += 1
    set_state()
    res["e1.03"] = dict(l556n2_holds=ok, of=tot, extends_K_holds=k_ext, extends_K_of=k_tot)
    print("e1.03 under V1.1: L556.n2's statement ((F1) at (a,b) ⟺ D4.4's sig_C(λ(k)) and (K)'s sig_τ[C](k) agree) at %d of %d translated pairs; D4.4's 'extends (K)' (sig_C({j}) = sig_C(j)) at %d of %d (j, pair)" % (ok, tot, k_ext, k_tot))
    # e1.14: V1.2's new setting edits (pole and SMALL): does an altered other component k leave an equation on v incompatible with the set value?
    import random
    rng = random.Random(108001)  # round 1's SMALL stream (s108_s1_worlds.py, seed 108001, 160 per size): the same targets
    kinds = {"new pairs": 0, "k ≠ j altered at some b": 0, "an altered k alone excludes the set value (an incompatible equation beside)": 0,
             "Sol_D empty at some b": 0, "Sol_D empty with no single altered k excluding the value": 0, "targets": 0}
    targets = [pole()]
    for size in SMALL:
        for i in range(160):
            m = gen_p_cand(rng, size)
            if m is not None:
                targets.append(m[0].D)
    for D in targets:
        set_state(r1="V1.2")
        R2 = Roles(D)
        set_state()
        R0 = Roles(D)
        new = [(v, a) for v in D.ports for a in R2.Set[v] - R0.Set[v]]
        kinds["targets"] += 1
        for (v, a) in new:
            kinds["new pairs"] += 1
            alt_any = incompat = False
            for b in D.B:
                # the component j through which a sets v at b (V1.2's reading: the slice clause alone)
                js = [(j, x) for j in D.comps if v in D.foot[j] for x in D.dom[v] if D.L(j, a, b) == slice_rel(D, j, v, x)]
                if not js:
                    continue
                j, x = js[0]
                for k in D.comps:
                    if k == j or D.L(k, a, b) == D.L(k, ONE, b):
                        continue
                    alt_any = True
                    if v in D.foot[k] and not any(w[D.foot[k].index(v)] == x for w in D.L(k, a, b)):
                        incompat = True
            empty = any(not D.sol(a, b2) for b2 in D.B)
            kinds["k ≠ j altered at some b"] += alt_any
            kinds["an altered k alone excludes the set value (an incompatible equation beside)"] += incompat
            kinds["Sol_D empty at some b"] += empty
            kinds["Sol_D empty with no single altered k excluding the value"] += (empty and not incompat)
    set_state()
    res["e1.14"] = kinds
    print("e1.14 (V1.2, the pole + round 1's SMALL targets, 160 per size, seed 108001): %s" % "; ".join("%s %d" % kv for kv in kinds.items()))
    # e1.37: a found question with its trace (E8's arrangement: the contract as the content); ρ computed by D3.4 through Con
    D = pole()
    C1, C2, _ = pole_contracts(D)
    rows37 = {}
    for lab, prep, recs in (("a trace at o2 prepares C2 as a content, the change C1 → C2 recorded", {"C2"}, [False, True]),
                            ("a trace at o2 prepares C2, the change unrecorded", {"C2"}, [False, False]),
                            ("no trace prepares C2 (C2 operative at o2, nothing else)", set(), [False, True])):
        h = Hist(["o1", "o2"], [("o2", "t")], set(), prepares=prep, contracts=["C1", "C2"], records=recs)
        cn = {rd: con(h, name="C2", reading=rd) for rd in EPISODE_READINGS}
        rho = "constructed" if cn["S41"] else "declared"
        found_claim_allowed = (rho == "constructed")  # L155.s6: a claim that an episode found p′ requires ρ = constructed
        p2 = Question(D, C2, "b1_45", PortQuery(), "L", name="p′", rho=rho)
        c2 = pole_fwd_candidate(p2)
        accs = {}
        for st, kw in (("none", {}), ("V1.5", dict(r1="V1.5")), ("R2V1.1 (recorded)", dict(r2="R2V1.1"))):
            set_state(**kw)
            accs[st] = bool(account(c2))
        set_state()
        rows37[lab] = dict(con=cn, rho=rho, found_claim_allowed=found_claim_allowed, acc=accs)
        print("e1.37: %s: Con(C2) S41 %s, L55 %s ⇒ ρ(C2) %s (D3.1's slot holds it); L155.s6's Found claim allowed %s; Acc(E_fwd on p′): %s"
              % (lab, tf(cn["S41"]), tf(cn["L55"]), rho, tf(found_claim_allowed), "; ".join("%s %s" % (k, tf(v)) for k, v in accs.items())))
    res["e1.37"] = rows37
    # e1.38: D13.8's Episode, Con and Build on the bridge's chains read no ρ; CreateEx reads Acc (D14.7)
    rows38 = {}
    for st, kw in C2_STATES:
        for rb in ("declared", "selected", "constructed"):
            set_state(**kw)
            b = bridge(rb)
            rows38["%s | ρ(brief) %s" % (st, rb)] = {k.split(":")[0]: (tuple(v["con_S41"]), v["build_S41"], tuple(v["con_L55"]), v["createex_valuations"]) for k, v in b.items()}
    set_state()
    res["e1.38"] = rows38
    ep_same = len(set(tuple((k, v[0], v[1], v[2]) for k, v in sorted(r.items())) for r in rows38.values())) == 1
    print("e1.38: Episode/Con/Build at the bridge's output identical in every state and every ρ(brief): %s; CreateEx valuations (a2) per state and ρ: %s"
          % (ep_same, "; ".join("%s %d" % (k, v["a2"][3]) for k, v in rows38.items())))
    res["e1.38 Episode/Con/Build unchanged"] = ep_same
    # e1.39: 𝔈_Θ over the worked cases: {c : Acc((c, p, t, Γ, δ)) for some worked (p, t, Γ, δ)}, Θ admitting every carrier (by hand)
    rows39 = {}
    for st, kw in C2_STATES:
        set_state(**kw)
        mem = sorted(set(c.E.name for lab, c in wc if account(c)))
        rows39[st] = mem
        print("e1.39: 𝔈_Θ over the worked cases, %-40s %d organization(s)%s" % (st, len(mem), (": " + ", ".join(mem)) if len(mem) < 30 else ""))
    set_state()
    res["e1.39"] = rows39
    OUT["D"] = res


def main():
    out = sys.argv[1] if len(sys.argv) > 1 else None
    parts = sys.argv[2] if len(sys.argv) > 2 else "ABCD"
    for k, f in (("A", part_a), ("B", part_b), ("C", part_c), ("D", part_d)):
        if k in parts:
            f()
    if out:
        with open(out, "w", encoding="utf-8") as f:
            json.dump(OUT, f, ensure_ascii=False, indent=1, default=repr)


if __name__ == "__main__":
    main()
