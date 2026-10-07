# S109 Part B round 1 (rule 5): the scope of each in-scope variant of one section, computed off against on.
#   PYTHONHASHSEED=0 python3 -B s109b_scope.py --model-dir "<section Bn model>" --section Bn --out OUT.json [--scale 4]
# Imports the package `model` of the section's copy (which holds only that section's switches, core.S109B). For each
# variant (and each reading it is computed under), against 'none' (the definition after round 4):
#   A. the worked cases (Part A's list, `S108 Part A round 2 - computation/section 1 model/s108_s1_cases.py`, rebuilt here)
#      and the owner's two cases under the three readings of the owner's change (edit, boundary, mixed: owner_cases.py, a
#      copy of Part A round 2's), E_enc on each question: Acc with its conjuncts, and Expl := Acc ∧ ¬Dec(t) with t's history
#      set by hand three ways (claims_s41.provenance_of: 'Dec', 'Con', 'Sel' on H = {(1, b0)}; Θ by hand, I90);
#   B. the student's copy (FC30.new1 (d)): Acc, and Dec(t) at the student's holding on the chain (T′), H = {(1,b1_45)} and ∅;
#   C. the generated worlds (claims_a.gen_p_cand over SMALL, 40 per size times the scale, seed 109001): candidates built once
#      under 'none', judged under each variant; Acc and Expl (Sel history) entering and leaving, by kind, smallest witness;
#   D. (B3) every chain of 1 to 3 holdings (held, trace, selc bits; T′; no relay): Dec at the last holding, and at the
#      student's-copy shape, off against on;
#   E. the program's made-up cases of the copy (s104_external.py: FC-E1-E5; s104_creative_transport.py: CT1-CT8),
#      run under the variant and compared by md5 with their output under 'none' (the differing lines kept).
# F. (B3) the bridge (FC84.new1 (a1), (a2)): Con and Build at the output. The bridge is also read from the whole-suite runs. Writes only OUT.json (and OUT.json's .txt summary).
import argparse
import hashlib
import itertools
import json
import os
import random
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))

ap = argparse.ArgumentParser()
ap.add_argument("--model-dir", required=True)
ap.add_argument("--section", required=True)
ap.add_argument("--out", required=True)
ap.add_argument("--scale", type=float, default=4.0)
ap.add_argument("--no-worlds", action="store_true")
ARGS = ap.parse_args()
MD = os.path.abspath(ARGS.model_dir)
sys.path.insert(0, MD)
sys.path.insert(0, HERE)

from model import core  # noqa: E402
from model.core import ONE, BOT, Org, Question, PortQuery, Candidate, Translation, account  # noqa: E402
from model.cases import pole, pole_fwd_candidate, pole_rev_candidate, single_settings, fibre_query, COT  # noqa: E402
from model.claims_a import pole_contracts, table_candidate, area2_lookups, _org, _T, SMALL, gen_p_cand  # noqa: E402
from model.claims_r3a2 import m5, m13, elim  # noqa: E402
from model.claims_b import e8_contract_org, prov_fixed_points, prov_show, faithful_on  # noqa: E402
from model.claims_s106 import sign_question, sign_two, sign_one, sign_mech  # noqa: E402
from model.claims_s41 import provenance_of  # noqa: E402
from model import e9  # noqa: E402
import owner_cases as OW  # noqa: E402

# (label, variant, {core attribute: value}) per section; the readings the owner's cases or the variant turn on
READINGS = {
    "B1": [("PB1.1", "PB1.1", {}), ("PB1.2 Θ all", "PB1.2", {"S109B_THETA": "all"}), ("PB1.2 Θ strict", "PB1.2", {"S109B_THETA": "strict"}),
           ("PB1.3", "PB1.3", {}), ("PB1.4", "PB1.4", {}), ("PB1.5", "PB1.5", {}), ("PB1.6", "PB1.6", {}), ("PB1.7", "PB1.7", {}),
           ("PB1.8", "PB1.8", {}), ("PB1.9", "PB1.9", {})],
    "B2": [("PB2.1", "PB2.1", {}), ("PB2.2", "PB2.2", {}), ("PB2.3", "PB2.3", {}), ("PB2.4", "PB2.4", {}),
           ("PB2.5 bg", "PB2.5", {"S109B_NC0": "bg"}), ("PB2.5 bg-input", "PB2.5", {"S109B_NC0": "bg-input"}), ("PB2.6", "PB2.6", {}),
           ("PB2.7 every", "PB2.7", {"SLOT_QUANTIFIER": "every"}), ("PB2.7 some", "PB2.7", {"SLOT_QUANTIFIER": "some"}),
           ("PB2.7 some-exempt", "PB2.7", {"SLOT_QUANTIFIER": "some-exempt"}), ("PB2.7 some-exempt-set", "PB2.7", {"SLOT_QUANTIFIER": "some-exempt-set"}),
           ("PB2.8", "PB2.8", {}), ("PB2.9", "PB2.9", {})],
    "B3": [("PB3.1", "PB3.1", {}), ("PB3.2", "PB3.2", {}), ("PB3.3", "PB3.3", {}), ("PB3.4", "PB3.4", {}), ("PB3.5", "PB3.5", {}),
           ("PB3.6", "PB3.6", {}), ("PB3.7", "PB3.7", {})],
    "B4": [("PB4.1", "PB4.1", {}), ("PB4.2", "PB4.2", {}), ("PB4.3", "PB4.3", {}), ("PB4.4' all", "PB4.4'", {"S109B_HELD": "all"}),
           ("PB4.4' no-records", "PB4.4'", {"S109B_HELD": "no-records"}), ("PB4.5", "PB4.5", {}), ("PB4.6", "PB4.6", {}), ("PB4.7", "PB4.7", {}),
           ("PB4.8", "PB4.8", {})],
}[ARGS.section]
DEFAULTS = {"S109B": "none", "SLOT_QUANTIFIER": "every", "S109B_THETA": "all", "S109B_NC0": "bg", "S109B_HELD": "all"}
ENVNAME = {"S109B": "S109B_VARIANT", "SLOT_QUANTIFIER": "S105_SLOT_QUANTIFIER", "S109B_THETA": "S109B_THETA", "S109B_NC0": "S109B_NC0", "S109B_HELD": "S109B_HELD"}


def setv(v, extra=None):
    for k, x in DEFAULTS.items():
        if hasattr(core, k):
            setattr(core, k, x)
    core.S109B = v
    for k, x in (extra or {}).items():
        setattr(core, k, x)


def tf(x):
    return "T" if x else "F"


def evaluate(c):
    acc, d = account(c, detail=True)
    H = [(ONE, c.p.b0)]
    prov = {}
    for kind in ("Dec", "Con", "Sel"):
        s, k, dec = provenance_of(c, kind, H)
        prov[kind] = [bool(s), bool(k), bool(dec), bool(acc and not dec)]
    keys = [k for k in ("F1", "F2", "A", "Dep", "NonVacuous", "question") if k in d]
    return dict(acc=bool(acc), conj={k: bool(d[k]) for k in keys}, prov=prov)


def show(e):
    return "Acc %s [%s] | Expl on histories Dec/Con/Sel: %s" % (tf(e["acc"]), " ".join("%s %s" % (k, tf(v)) for k, v in e["conj"].items()),
                                                               "/".join(tf(e["prov"][k][3]) for k in ("Dec", "Con", "Sel")))


def worked_cases():
    """Part A's worked cases (s108_s1_cases.worked_cases, labels unchanged), then the owner's two cases under three readings."""
    out = []
    D = pole()
    C1, C2, C2s = pole_contracts(D)
    C3 = frozenset([(ONE, "b1_45")] + [(a, "b1_45") for a in single_settings(D, ["L"])])
    for nm, C in (("C1", C1), ("C2", C2), ("C3", C3)):
        p = Question(D, C, "b1_45", PortQuery(), "L", name=nm)
        out.append(("E1 pole, forward organization, %s" % nm, pole_fwd_candidate(p)))
    p1 = Question(D, C1, "b1_45", PortQuery(), "L", name="p_prod")
    r = pole_rev_candidate(p1)
    out.append(("E1 pole, reversed calculation, production C1", r))
    inv = D.meta["inv"]
    lab = {v: k for k, v in inv.items()}

    def tau2(a):
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
    out.append(("E1 pole, reversed calculation under Mimo's τ', C1", r.replace(tau={a: x for a, x in t2.items() if x is not None}, name="ℰ_rev τ'")))
    CH = frozenset([(ONE, "b1_45")] + [(a, "b1_45") for a in single_settings(D, ["H"])])
    pH = Question(D, CH, "b1_45", PortQuery(), "L", name="C_H")
    rH = pole_rev_candidate(pH)
    out.append(("E1 pole, reversed calculation under Mimo's τ', H only", rH.replace(tau={a: t2[a] for a in sorted(set(x for x, _ in CH), key=repr)}, name="ℰ_rev τ' (H only)")))
    Did = pole(bounds=[(1, 45), (2, 45), (3, 45)])
    pid = Question(Did, frozenset((ONE, b) for b in Did.B), "b1_45", fibre_query(), ("H", "T", "L"), name="p_ident")
    out.append(("E1 pole, reversed calculation, identification C_id", pole_rev_candidate(pid, delta=("H", "T", "L"))))
    for nm, C in (("C1", C1), ("C2", C2)):
        p = Question(D, C, "b1_45", PortQuery(), "L", name=nm)
        out.append(("L269 table of observed answers E_tab, pole %s" % nm, table_candidate(p, list(D.ports))))
        out.append(("L269 encoding table E_enc, pole %s" % nm, table_candidate(p, list(D.ports), encode=True)))
    p = Question(D, C1, "b1_45", PortQuery(), "L", name="C1")
    tab = {(a, b): (frozenset([(p.ans(a, b),)]) if p.ans(a, b) is not BOT else frozenset((x,) for x in D.dom["L"])) for a in D.A for b in D.B}
    E = Org("E_lk", ["L"], {"L": D.dom["L"]}, ["k"], {"k": ("L",)}, D.B, D.A, D._compose, lambda j, a, b: tab[(a, b)])
    out.append(("L273 'p because p': the pole's L written in, C1", Candidate(E, p, {"L": Translation(("L",))}, {a: a for a in D.A}, {b: b for b in D.B},
                                                                             {"k": (frozenset(D.comps), {"L": Translation(("L",))})}, ["k"], "L", name="ℰ_lk")))
    D6 = Org("D", ["y"], {"y": (0, 1)}, ["c"], {"c": ["y"]}, ["b0"], [ONE, "a"], lambda a2, a1: None, lambda j, a, b: {(0,)})
    p6 = Question(D6, [(ONE, "b0"), ("a", "b0")], "b0", PortQuery(), "y")
    rel6 = {("k", ONE, "b0"): {(0, 0), (1, 1)}, ("k", "e1", "b0"): {(0, 0), (1, 1)}, ("k", "e2", "b0"): {(0, 0), (1, 1)},
            ("m", ONE, "b0"): {(1,)}, ("m", "e1", "b0"): {(0,)}, ("m", "e2", "b0"): {(0,)}}
    E6 = Org("E", ["y", "z"], {"y": (0, 1), "z": (0, 1)}, ["k", "m"], {"k": ["y", "z"], "m": ["z"]}, ["b0"], [ONE, "e1", "e2"],
             lambda a2, a1: None, lambda j, a, b: rel6[(j, a, b)])
    out.append(("L257 a contract of relabelings, τ(1) ≠ 1", Candidate(E6, p6, {"y": Translation(["y"]), "z": Translation(["y"])}, {ONE: "e1", "a": "e2"}, {"b0": "b0"},
                                                                     {"k": (frozenset(["c"]), {"y": Translation(["y"]), "z": Translation(["y"])}), "m": (frozenset(["c"]), {"z": Translation(["y"])})},
                                                                     ["k", "m"], "y")))
    for nm, (c, _ans) in area2_lookups().items():
        out.append((nm, c))
    out.append(("M5: the answer fixed at each pair by another part", m5()))
    out.append(("M13: the owner's weathervane (S41 Q15)", m13()))
    Dv = _org("D_vane", ["y"], {"y": ("N", "S")}, ["c_y"], {"c_y": ("y",)}, ["b0"], [ONE, "turn"], {("c_y", "turn", "b0"): {("N",)}})
    pv = Question(Dv, [(ONE, "b0"), ("turn", "b0")], "b0", PortQuery(), "y", name="p_vane")
    out.append(("R3-Q1: the hand-turned vane ('north when turned')", Candidate(Dv, pv, _T("y"), {ONE: ONE, "turn": "turn"}, {"b0": "b0"},
                                                                              {"c_y": (frozenset(["c_y"]), _T("y"))}, ["c_y"], "y", name="ℰ_vane")))
    for nm, kind in (("FC62's encoding", "const"), ("the second encoding", "two")):
        _p, c = elim(kind)
        out.append(("E5 eliminative (L339), %s" % nm, c))
    Dc, invd, _ = e8_contract_org()
    sets = [a for a in Dc.A if a != ONE and set(dict(invd[a])) == {"m_1_b0"}]
    pd = Question(Dc, [(ONE, "β")] + [(a, "β") for a in sets], "β", PortQuery(), "m_1_b0", name="p_δ")
    lam = {k: (frozenset([k]), {v: Translation((v,)) for v in Dc.foot[k]}) for k in Dc.comps}
    out.append(("E8 p_δ, the identity candidate (K1's criticism question)", Candidate(Dc, pd, {v: Translation((v,)) for v in Dc.ports},
                                                                                        {a: a for a in Dc.A}, {b: b for b in Dc.B}, lam, list(Dc.comps), "m_1_b0")))
    D9 = e9.object_layer()
    p9 = e9.question(D9, [(a, b) for a in D9.A for b in D9.B])
    E9 = e9.sim_layer_S1()
    out.append(("E9 two-layer episode, S1 with t1 (L626)", e9.t1_candidate(p9, E9)))
    out.append(("E9 two-layer episode, S1 with t1∘ψ (L630)", e9.t1_candidate(p9, E9, swapped=True)))
    p = sign_question()
    out.append(("S44 the shop sign, two parts (red on Mon, blue on Tue)", sign_two(p)))
    out.append(("S44 the shop sign, one part (red on Mon, blue on Tue)", sign_one(p)))
    out.append(("the sign with a day port and a palette rule", sign_mech()))
    worked = len(out)
    for ph, en, lab_, c in OW.all_cases():
        out.append(("owner's %s, change as %s: %s" % (ph, en, lab_), c))
    return out, worked


def student_copy():
    """FC30.new1 (d): Acc(ℰ_fwd) and Dec(t) at the student's holding o2 on the chain (source o1 with a trace), T′; PB3.1 reads o2
    as a whole-content copy of o1 (rec_of), PB3.6 drops o1 (outside β)."""
    D = pole(H_vals=(1, 2), T_vals=(45,), bounds=[(1, 45)])
    C = [(ONE, "b1_45")] + [(a, "b1_45") for a in single_settings(D, ["H"])]
    c = pole_fwd_candidate(Question(D, C, "b1_45", PortQuery(), "L", name="p"))
    acc = bool(account(c))
    rows = {}
    for Hx, lab in (([(ONE, "b1_45")], "H={(1,b1_45)}"), ([], "H=∅")):
        held_o = bool(core.faithful(c))
        selc_o = bool(Hx) and set(Hx) <= set(c.p.C) and faithful_on(c, Hx)
        if core.S109B == "PB3.6":
            fps = prov_fixed_points(1, [held_o], [0], [selc_o], "T'", True)
            decs = [not sc[0][0] and not sc[0][1] for R, sc in fps]
            shown = prov_show(1, fps)
        else:
            fps = prov_fixed_points(2, [1, held_o], [1, 0], [0, selc_o], "T'", True, rec_of=([None, 0] if core.S109B == "PB3.1" else None))
            decs = [not sc[1][0] and not sc[1][1] for R, sc in fps]
            shown = prov_show(2, fps)
        rows[lab] = dict(held=held_o, selc=bool(selc_o), fixed_points=shown, dec=decs, expl=[acc and not d for d in decs])
    return dict(acc=acc, rows=rows)


def chains():
    """(B3) every chain of 1 to 3 holdings: Dec(t) at each held holding, T′, no relay."""
    res = {}
    for n in (1, 2, 3):
        for held in itertools.product((0, 1), repeat=n):
            for trace in itertools.product((0, 1), repeat=n):
                for selc in itertools.product((0, 1), repeat=n):
                    fps = prov_fixed_points(n, list(held), list(trace), list(selc), "T'", True)
                    res[repr((n, held, trace, selc))] = [prov_show(n, fps), [[bool(held[o]) and not sc[o][0] and not sc[o][1] for o in range(n)] for R, sc in fps]]
    return res


def bridge():
    """(B3) the owner's bridge, FC84.new1 (a1) and (a2): the chain as the claim builds it (q = C_brief throughout, no record,
    T′, D13.8 as S41 has it): the fixed points, Con at the output, Build at the output. [Added before section B2's and B3's
    scope runs; section B1's run was made without it.]"""
    from model.claims_b import chain_eps
    from model.claims_b import build_at
    out = {}
    for key, held_, trace_ in (("a1", [0, 1], [0, 1]), ("a2", [0, 0, 1], [0, 0, 1])):
        n_ = len(held_)
        fps = prov_fixed_points(n_, held_, trace_, [0] * n_, "T'", True, chain_eps(["C_brief"] * n_, [False] * n_, "S41"))
        out[key] = dict(fixed_points=prov_show(n_, fps), con_at_output=[bool(sc[n_ - 1][1]) for R, sc in fps],
                        build=bool(build_at(n_, held_, trace_, "T'", fps[0][0] if fps else frozenset(), n_ - 1)))
    return out


def run_script(name, env_extra):
    env = dict(os.environ)
    env["PYTHONHASHSEED"] = "0"
    for k in ENVNAME.values():
        env.pop(k, None)
    env.update(env_extra)
    t = time.time()
    r = subprocess.run(["timeout", "900", "python3", "-B", name], cwd=MD, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    out = r.stdout.decode("utf-8", "replace")
    return dict(exit=r.returncode, seconds=round(time.time() - t, 1), md5=hashlib.md5(r.stdout).hexdigest(), text=out)


def main():
    t0 = time.time()
    cases, n_worked = worked_cases()
    setv("none")
    base = [evaluate(c) for _, c in cases]
    setv("none")
    sbase = student_copy()
    cbase = chains() if ARGS.section == "B3" else None
    bbase = bridge() if ARGS.section == "B3" else None
    scripts = ["s104_external.py", "s104_creative_transport.py"]  # s106_cases.py: its cases are part A's worked list, rebuilt above (A)
    sc_base = {s: run_script(s, {}) for s in scripts}
    worlds = []
    if not ARGS.no_worlds and ARGS.section in ("B1", "B2", "B3"):
        rng = random.Random(109001)
        per = max(1, int(40 * ARGS.scale))
        setv("none")
        for size in SMALL:
            for i in range(per):
                m = gen_p_cand(rng, size)
                if m is None:
                    continue
                p, c = m
                worlds.append((size, i, p, c, evaluate(c)))
    out = dict(section=ARGS.section, model_dir=MD, cases=[lab for lab, _ in cases], n_worked=n_worked,
               base=[dict(label=lab, **b) for (lab, _), b in zip(cases, base)], student_base=sbase,
               scripts_base={s: dict(exit=v["exit"], md5=v["md5"], seconds=v["seconds"]) for s, v in sc_base.items()},
               worlds_n=len(worlds), worlds_acc_base=sum(1 for w in worlds if w[4]["acc"]),
               worlds_expl_sel_base=sum(1 for w in worlds if w[4]["prov"]["Sel"][3]), variants={})
    lines = ["section %s: %d cases (%d worked, %d owner's-case encodings), %d generated" % (ARGS.section, len(cases), n_worked, len(cases) - n_worked, len(worlds))]
    for lab, v, extra in READINGS:
        setv(v, extra)
        rec = dict(variant=v, reading=extra, moved=[])
        for (clab, c), b in zip(cases, base):
            e = evaluate(c)
            if e != b:
                rec["moved"].append(dict(label=clab, off=show(b), on=show(e), acc=[b["acc"], e["acc"]],
                                         expl=[[b["prov"][k][3], e["prov"][k][3]] for k in ("Dec", "Con", "Sel")]))
        rec["student"] = student_copy()
        rec["student_moves"] = rec["student"] != sbase
        if bbase is not None:
            rec["bridge"] = dict(off=bbase, on=bridge())
        if cbase is not None:
            cv = chains()
            diff = [k for k in cbase if cbase[k] != cv[k]]
            dec_in = sum(1 for k in diff for (a, b) in [(cbase[k][1], cv[k][1])] if a and b and a[0] and b[0] and a[0][-1] and not b[0][-1])
            rec["chains"] = dict(total=len(cbase), differ=len(diff), first=diff[:5], examples={k: [cbase[k], cv[k]] for k in diff[:5]},
                                 output_dec_to_not=dec_in,
                                 output_not_to_dec=sum(1 for k in diff for (a, b) in [(cbase[k][1], cv[k][1])] if a and b and a[0] and b[0] and (not a[0][-1]) and b[0][-1]),
                                 fixed_point_count_changed=sum(1 for k in diff if len(cbase[k][0]) != len(cv[k][0])))
        if worlds:
            summ = dict(acc_in=0, acc_out=0, expl_in=0, expl_out=0, kinds={}, conj_moved={}, witness={})
            for size, i, p, c, b in worlds:
                e = evaluate(c)
                if e["acc"] == b["acc"] and e["prov"]["Sel"][3] == b["prov"]["Sel"][3]:
                    continue
                if e["acc"] != b["acc"]:
                    summ["acc_in" if e["acc"] else "acc_out"] += 1
                if e["prov"]["Sel"][3] != b["prov"]["Sel"][3]:
                    summ["expl_in" if e["prov"]["Sel"][3] else "expl_out"] += 1
                direction = ("Acc in" if e["acc"] and not b["acc"] else ("Acc out" if b["acc"] and not e["acc"] else "Expl only"))
                kind = "%s | %s | %s" % (c.E.meta.get("family", "?"), p.D.meta.get("family", "?"), direction)
                summ["kinds"][kind] = summ["kinds"].get(kind, 0) + 1
                moved = ",".join(k for k in b["conj"] if b["conj"][k] != e["conj"].get(k)) or "-"
                summ["conj_moved"][moved] = summ["conj_moved"].get(moved, 0) + 1
                if kind not in summ["witness"]:
                    summ["witness"][kind] = dict(size=repr(size), index=i, off=show(b), on=show(e), question=p.describe(), candidate=c.describe())
            rec["worlds"] = summ
        env_extra = {ENVNAME["S109B"]: v}
        for k, x in extra.items():
            env_extra[ENVNAME[k]] = x
        rec["scripts"] = {}
        for s in scripts:
            r = run_script(s, env_extra)
            same = r["md5"] == sc_base[s]["md5"]
            d = dict(exit=r["exit"], md5=r["md5"], same=same)
            if not same:
                bl = sc_base[s]["text"].split("\n")
                vl = r["text"].split("\n")
                d["lines_only_off"] = [l for l in bl if l not in set(vl)][:40]
                d["lines_only_on"] = [l for l in vl if l not in set(bl)][:40]
            rec["scripts"][s] = d
        setv("none")
        out["variants"][lab] = rec
        w = rec.get("worlds")
        lines.append("%s: cases moved %d (Acc moves %d); student's copy moves %s; %s%sscripts differing: %s" % (
            lab, len(rec["moved"]), sum(1 for m in rec["moved"] if m["acc"][0] != m["acc"][1]), rec["student_moves"],
            ("worlds Acc in %d out %d, Expl(Sel) in %d out %d; " % (w["acc_in"], w["acc_out"], w["expl_in"], w["expl_out"])) if w else "",
            ("chains differ %d of %d; " % (rec["chains"]["differ"], rec["chains"]["total"])) if "chains" in rec else "",
            [s for s in scripts if not rec["scripts"][s]["same"]]))
        for m in rec["moved"]:
            lines.append("   %s\n      off: %s\n      on:  %s" % (m["label"], m["off"], m["on"]))
    out["seconds"] = round(time.time() - t0, 1)
    with open(ARGS.out, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1, default=str)
    with open(ARGS.out[:-5] + ".txt", "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\ntotal %.1f s\n" % out["seconds"])
    print("\n".join(lines))


if __name__ == "__main__":
    main()
