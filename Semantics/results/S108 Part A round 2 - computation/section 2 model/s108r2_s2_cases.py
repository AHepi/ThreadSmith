# S108 Part A round 2, section 2 (the computing agent, rule 5): the worked cases with each in-scope variant of round 2's
# reply off and on (Acc (E); Account ∧ ¬Dec(t) under the four histories round 1 set by hand, P-S2-3), the readings the
# round-1 candidates rest on computed under each choice (rule 5 (1)), the Desc of V1.6's formula per case (rule 5 (3)), and
# the cases the reply proposes for round 1's claimed-only edges (rule 5 (2)).
# Run from "results/S108 Part A round 2 - computation/section 2 model":  PYTHONHASHSEED=0 python3 -B s108r2_s2_cases.py [--json F]
# Standard library only. Imports this copy's package model/ (with core.S2_VARIANT, core.S2R2 ...), round 1's case script
# s108_s2_cases.py and s108r2_owner_cases.py; writes only the --json file. An experiment on a copy: no theory text changed.
import contextlib
import itertools
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from model import core  # noqa: E402
from model.core import (ONE, BOT, Org, Question, PortQuery, Candidate, Translation, account, NC2, slot, hom, faithful,  # noqa: E402
                        restrict, routes, conf_claim, F1_at, F2eq_at, A_at, SLOT_QUANTIFIERS, relabeling)
from model.claims_b import Hist, sel, con, fwd_pole_cand, prov_fixed_points, prov_show, faithful_on, selresp, viol_at  # noqa: E402
from model.claims_s41 import provenance_of, expl_ruled_out, not_using_E, suff_defeats  # noqa: E402
from model.args import Not, Imp, And, Leaf, Step, Assessor, X  # noqa: E402
from model.cases import pole, pole_fwd_candidate, fibre_query  # noqa: E402
from model.claims_a import pole_contracts, table_candidate  # noqa: E402
from model.claims_r3a1 import obs_value  # noqa: E402
import s108_s2_cases as R1  # noqa: E402  (round 1's cases: written_in_step_cases, more_worked_cases, v27_case, two_commitment)
import s108r2_owner_cases as OW  # noqa: E402

HISTORIES = R1.HISTORIES
SETTINGS = {  # label -> the module settings (core.S2_VARIANT round 1's; core.S2R2 round 2's; readings)
    "off": {},
    "R2V2.3a": dict(S2R2="R2V2.3a"),
    "R2V2.5": dict(S2R2="R2V2.5"),
    "R2V2.6 written": dict(S2R2="R2V2.6", S2R2_R26="written"),
    "R2V2.6 HS": dict(S2R2="R2V2.6", S2R2_R26="HS"),
    "R2V2.6 reply": dict(S2R2="R2V2.6", S2R2_R26="reply"),
    "R2V2.8 target": dict(S2R2="R2V2.8", S2R2_DESC="target"),
    "R2V2.8 program": dict(S2R2="R2V2.8", S2R2_DESC="program"),
    "R2V2.8 widest": dict(S2R2="R2V2.8", S2R2_DESC="widest"),
    "R2V2.9": dict(S2R2="R2V2.9"),
    "R2V2.10": dict(S2R2="R2V2.10"),
    "q some": dict(SLOT_QUANTIFIER="some"),
    "q some-exempt": dict(SLOT_QUANTIFIER="some-exempt"),
    "q some-exempt-set": dict(SLOT_QUANTIFIER="some-exempt-set"),
    "V2.4 q every": dict(S2_VARIANT="V2.4"),
    "V2.4 q some": dict(S2_VARIANT="V2.4", SLOT_QUANTIFIER="some"),
    "V2.4 q some-exempt": dict(S2_VARIANT="V2.4", SLOT_QUANTIFIER="some-exempt"),
    "V2.4 q some-exempt-set": dict(S2_VARIANT="V2.4", SLOT_QUANTIFIER="some-exempt-set"),
    "V2.5 (C7)": dict(S2_VARIANT="V2.5"),
    "V2.5 (C7) × R2V2.3a": dict(S2_VARIANT="V2.5", S2R2="R2V2.3a"),
}


@contextlib.contextmanager
def setting(**kw):
    keys = ("S2_VARIANT", "S2R2", "S2R2_R26", "S2R2_DESC", "SLOT_QUANTIFIER")
    old = {k: getattr(core, k) for k in keys}
    try:
        for k in keys:
            setattr(core, k, {"S2_VARIANT": "off", "S2R2": "off", "S2R2_R26": "written", "S2R2_DESC": "program", "SLOT_QUANTIFIER": "every"}[k])
        for k, v in kw.items():
            setattr(core, k, v)
        yield
    finally:
        for k, v in old.items():
            setattr(core, k, v)


def under(label, fn, *a, **k):
    with setting(**SETTINGS[label]):
        return fn(*a, **k)


def conj(d):
    return ",".join("%s%s" % (k, "T" if d.get(k) else "F") for k in ("F1", "F2", "A", "Dep", "NonVacuous", "NC1", "¬BadTarget") if k in d)


def expl_row(c):
    """Account ∧ ¬Dec(t) under the four hand-set histories (round 1's dec_of), in the current setting."""
    acc = bool(account(c))
    out = {}
    for h in HISTORIES:
        try:
            out[h] = acc and not R1.dec_of(c, h)
        except Exception:
            out[h] = None
    return out


def any_slot(c, q):
    return any(slot(c, k, quantifier=q) for k in c.E.comps)


P = print


# ---- 1. the worked cases under every setting ------------------------------------------------------------------------

_WC = []


def worked_cases():
    if _WC:
        return _WC[0]
    got = [(lab, where, c) for lab, where, c in R1.written_in_step_cases() + R1.more_worked_cases()]
    for ph, en, lab, c in OW.all_cases():
        got.append(("owner %s (%s): %s" % (ph, en, lab), "R2V2.1", c))
    got.append(("e2.06c: the two balances as a question with a candidate (ℰ_bal, Γ = {cd})", "e2.06c; Inv-R2-5", balances()))
    got.append(("R2V2.3 (b): ℰ_bad (M13 with L_cy(e,b0) = {(0,1),(1,0)} in E)", "R2V2.3 (b)", e_bad()))
    got.append(("R2V2.5: a two-pair contract answering ⊥ at both, identity candidate", "R2V2.5", r25_case()))
    _WC.append(got)
    return got


def section_worked(json_out):
    cases = worked_cases()
    labels = [s for s in SETTINGS if s != "off"]
    P("=" * 150)
    P("1. THE WORKED CASES: %d (round 1's 35, the owner's two cases under three encodings with E_enc on each question, and 3 built for this round)" % len(cases))
    P("   Acc (E) under each setting; * = differs from off. Settings: %s" % "; ".join("%d=%s" % (i + 1, s) for i, s in enumerate(labels)))
    rows = []
    for lab, where, c in cases:
        r = {"label": lab, "where": where, "acc": {}, "detail": {}, "expl": {}}
        for s in SETTINGS:
            with setting(**SETTINGS[s]):
                v, d = account(c, detail=True)
                r["acc"][s] = bool(v)
                r["detail"][s] = conj(d)
                r["expl"][s] = expl_row(c)
        rows.append(r)
        P("   %-78s %s | %s" % (lab[:78], "T" if r["acc"]["off"] else "F",
                                " ".join(("T" if r["acc"][s] else "F") + ("*" if r["acc"][s] != r["acc"]["off"] else " ") for s in labels)))
    P("-" * 150)
    for s in labels:
        am = [(r["label"], r["acc"]["off"], r["acc"][s], r["detail"]["off"], r["detail"][s]) for r in rows if r["acc"][s] != r["acc"]["off"]]
        em = [(r["label"], h, r["expl"]["off"][h], r["expl"][s][h]) for r in rows for h in HISTORIES if r["expl"]["off"][h] != r["expl"][s][h]]
        P("%-24s Acc moves on %d case(s); Account ∧ ¬Dec(t) moves on %d (case, history) pair(s)" % (s, len(am), len(em)))
        for lab, a, b, d0, d1 in am:
            P("      Acc %s->%s  %s   [off %s | on %s]" % ("T" if a else "F", "T" if b else "F", lab[:90], d0, d1))
        for lab, h, a, b in em[:60]:
            P("      Account ∧ ¬Dec(t) %s->%s  %s, history '%s'" % (a, b, lab[:80], h))
        if len(em) > 60:
            P("      ... %d more" % (len(em) - 60))
    json_out["worked"] = rows
    return rows


# ---- 2. the readings the round-1 candidates rest on (rule 5 (1)) ------------------------------------------------------

def section_encodings(json_out):
    """R2V2.1: edit / boundary / mixed. The candidates computed in this copy: C3 (V2.1), C4 (V2.2), C5 (V2.3), C6 (V2.4 with each
    quantifier), C11 (Acc ∧ ¬Slot_q, the holding not declared), C7 (V2.5: Account ∧ ¬Dec(t) with nothing tried), C12 (Acc alone).
    C1, C2 in section 1's copy (s108r2_other_sections.py); C8, C9, C10, C13 read Acc and a history set by hand (see the file)."""
    P("=" * 150)
    P("2a. R2V2.1: THE OWNER'S CHANGE AS AN EDIT, A BOUNDARY, OR BOTH (MIXED); each round-1 candidate computed in this copy")
    out = []
    for ph, en, lab, c in OW.all_cases():
        r = {"phenomenon": ph, "encoding": en, "label": lab}
        with setting():
            r["off"] = bool(account(c))
            r["Dep witness off"] = repr(NC2(c, witness=True))
            r["ans"] = {"%s,%s" % x: repr(c.p.ans(*x)) for x in sorted(c.p.C, key=repr)}
            r["slots"] = {q: [k for k in c.E.comps if slot(c, k, quantifier=q)] for q in SLOT_QUANTIFIERS}
            r["C11"] = {q: r["off"] and not any_slot(c, q) for q in SLOT_QUANTIFIERS}
            r["C12"] = r["off"]
        for v in ("V2.1", "V2.2", "V2.3"):
            with setting(S2_VARIANT=v):
                r["C%d (%s)" % ({"V2.1": 3, "V2.2": 4, "V2.3": 5}[v], v)] = bool(account(c))
                if v == "V2.3":
                    r["V2.3 witness"] = repr(NC2(c, witness=True))
        r["C6 (V2.4)"] = {}
        for q in SLOT_QUANTIFIERS:
            with setting(S2_VARIANT="V2.4", SLOT_QUANTIFIER=q):
                r["C6 (V2.4)"][q] = bool(account(c))
        with setting(S2_VARIANT="V2.5"):
            r["C7 (V2.5), nothing tried"] = expl_row(c)["nothing tried, H=∅"]
        with setting():
            r["off, nothing tried"] = expl_row(c)["nothing tried, H=∅"]
        out.append(r)
        P("   %-5s %-9s %-44s Acc %s | C3 %s C4 %s C5 %s | C6 e/s/se/ses %s | C11 e/s/se/ses %s | C7 nothing-tried %s (off %s) | answers %s | slots %s"
          % (ph, en, lab[:44], tf(r["off"]), tf(r["C3 (V2.1)"]), tf(r["C4 (V2.2)"]), tf(r["C5 (V2.3)"]),
             "".join(tf(r["C6 (V2.4)"][q]) for q in SLOT_QUANTIFIERS), "".join(tf(r["C11"][q]) for q in SLOT_QUANTIFIERS),
             tf(r["C7 (V2.5), nothing tried"]), tf(r["off, nothing tried"]), r["ans"], {q: v for q, v in r["slots"].items() if v}))
    # the flags: does anything on each question meet (E) under C5, under each encoding?
    P("   -- per (phenomenon, encoding): does any candidate built on the question meet (E) under C5 (V2.3)? off?")
    agg = {}
    for r in out:
        k = (r["phenomenon"], r["encoding"])
        a = agg.setdefault(k, {"off": False, "C5": False, "C6 every": False, "C6 other": False, "C11 every": False, "C11 other": False})
        a["off"] |= r["off"]
        a["C5"] |= r["C5 (V2.3)"]
        a["C6 every"] |= r["C6 (V2.4)"]["every"]
        a["C6 other"] |= all(r["C6 (V2.4)"][q] for q in SLOT_QUANTIFIERS[1:])
        a["C11 every"] |= r["C11"]["every"]
        a["C11 other"] |= all(r["C11"][q] for q in SLOT_QUANTIFIERS[1:])
    for k, a in sorted(agg.items()):
        P("      %-5s %-9s something meets (E): off %s; C5 %s; C6 'every' %s, under all three others %s; C11 'every' %s, under all three others %s"
          % (k[0], k[1], tf(a["off"]), tf(a["C5"]), tf(a["C6 every"]), tf(a["C6 other"]), tf(a["C11 every"]), tf(a["C11 other"])))
    json_out["encodings"] = out
    json_out["encodings_agg"] = {"%s|%s" % k: v for k, v in agg.items()}


def tf(x):
    return "T" if x else ("F" if x is not None else "-")


def section_quantifier(rows, json_out):
    """R2V2.2: D6.3's quantifier, with (E) as it is and with V2.4 on: C6 and C11 on every worked case."""
    P("=" * 150)
    P("2b. R2V2.2: D6.3'S QUANTIFIER. (E) as it is: Acc under each reading; C6 = V2.4 (NC1 in (E)); C11 = Acc ∧ ¬Slot_q (the holding not declared)")
    cases = worked_cases()
    res = []
    for lab, where, c in cases:
        with setting():
            acc = bool(account(c))
            c11 = {q: acc and not any_slot(c, q) for q in SLOT_QUANTIFIERS}
        e_as_is = {q: under("q " + q if q != "every" else "off", lambda: bool(account(c))) for q in SLOT_QUANTIFIERS}
        c6 = {q: under("V2.4 q " + q, lambda: bool(account(c))) for q in SLOT_QUANTIFIERS}
        res.append(dict(label=lab, acc=acc, e_as_is=e_as_is, c6=c6, c11=c11))
    moved_e = [r["label"] for r in res if len(set(r["e_as_is"].values())) > 1]
    P("   (E) as it is: cases whose Acc differs across the four readings: %d %s" % (len(moved_e), moved_e))
    for q in SLOT_QUANTIFIERS:
        d6 = [r["label"] for r in res if r["acc"] and not r["c6"][q]]
        d11 = [r["label"] for r in res if r["acc"] and not r["c11"][q]]
        P("   %-16s C6 drops %2d of %d accounts; C11 drops %2d" % (q, len(d6), sum(r["acc"] for r in res), len(d11)))
        if q != "every":
            base6 = set(r["label"] for r in res if r["acc"] and not r["c6"]["every"])
            base11 = set(r["label"] for r in res if r["acc"] and not r["c11"]["every"])
            P("       C6 drops beyond 'every': %s" % sorted(set(d6) - base6))
            P("       C11 drops beyond 'every': %s" % sorted(set(d11) - base11))
            P("       C6 = C11 on every case: %s" % all(r["c6"][q] == r["c11"][q] for r in res))
    json_out["quantifier"] = res


def section_histories(json_out):
    """R2V2.3: the hand-set histories (I90) against provenance computed on chains; C7 (V2.5) under each."""
    P("=" * 150)
    P("2c. R2V2.3 (a): C7 (V2.5) ON CHAINS. For every worked account: chains o1 ≺ … ≺ on (n ≤ 3), every pattern of the earlier")
    P("    occurrences (held: a faithful transport to cod t; a trace), t held at on with its own faithfulness, no trace at on, Sel's")
    P("    conditions at on on H = ∅ and on H = {(1,b0)}; Dec at on at every fixed point, cut T′ (and U, T), off and under V2.5.")
    accounts = [(lab, c) for lab, where, c in worked_cases() if under("off", lambda: bool(account(c)))]
    stats = {}
    shapes = {}
    for lab, c in accounts:
        fa = 1 if under("off", faithful, c) else 0
        for Hx, hlab in (([], "H=∅"), ([(ONE, c.p.b0)], "H={(1,b0)}")):
            s0 = {}
            for v in ("off", "V2.5 (C7)"):
                with setting(**SETTINGS[v]):
                    s0[v] = bool(sel(c, Hx, Hist(["o1"], [], set(c.p.C), admitted=True, prepares=False)))
            for n in (1, 2, 3):
                for pat in itertools.product([(0, 0), (1, 0), (0, 1), (1, 1)], repeat=n - 1):
                    held = [x[0] for x in pat] + [fa]
                    trace = [x[1] for x in pat] + [0]
                    for rd in ("T'", "U", "T"):
                        vals = {}
                        for v in ("off", "V2.5 (C7)"):
                            with setting(**SETTINGS[v]):
                                fps = prov_fixed_points(n, held, trace, [0] * (n - 1) + [1 if s0[v] else 0], rd, True)
                                vals[v] = tuple(sorted(set(not sc[n - 1][0] and not sc[n - 1][1] for R, sc in fps)))
                        key = (hlab, rd)
                        st = stats.setdefault(key, {"chains": 0, "Dec off": 0, "C7 admits (Dec off → not Dec on)": 0})
                        st["chains"] += 1
                        st["Dec off"] += (True in vals["off"])
                        if vals["off"] == (True,) and vals["V2.5 (C7)"] == (False,):
                            st["C7 admits (Dec off → not Dec on)"] += 1
                            sh = ("earlier held" if any(held[:-1]) else "nothing earlier held") + (", a trace earlier" if any(trace[:-1]) else "")
                            shapes.setdefault(key, {}).setdefault(sh, 0)
                            shapes[key][sh] += 1
                        elif vals["off"] != vals["V2.5 (C7)"]:
                            sh = "other change %s -> %s" % (vals["off"], vals["V2.5 (C7)"])
                            shapes.setdefault(key, {}).setdefault(sh, 0)
                            shapes[key][sh] += 1
    for key in sorted(stats):
        P("   %-12s cut %-3s chains %5d; Dec at the output off %5d; C7 admits %5d; by shape %s" % (key[0], key[1], stats[key]["chains"], stats[key]["Dec off"],
                                                                                           stats[key]["C7 admits (Dec off → not Dec on)"], shapes.get(key, {})))
    # which shapes C7 admits, in words: with H = ∅, exactly the chains in which no earlier occurrence is represented (T′: in R)
    P("   (b) tried pairs that nothing survives: every worked account survives on every nonempty H ⊆ C (Env ≡ ⊤, I177)?")
    bad = []
    for lab, c in accounts:
        C = sorted(c.p.C, key=repr)
        for r in range(1, len(C) + 1):
            for H in itertools.combinations(C, r):
                if not faithful_on(c, list(H)):
                    bad.append((lab, H))
    P("       accounts %d; (account, H) with surv false: %d" % (len(accounts), len(bad)))
    cb = e_bad()
    with setting():
        acc = account(cb, detail=True)
        H = [("e", "b0")]
        s = sel(cb, H, Hist(["o1"], [], set(cb.p.C), admitted=True, prepares=False))
    with setting(S2_VARIANT="V2.5"):
        s5 = sel(cb, H, Hist(["o1"], [], set(cb.p.C), admitted=True, prepares=False))
    P("       ℰ_bad: Acc %s [%s]; F1 at (e,b0) %s; surv on H = {(e,b0)}: %s; Sel off %s, under V2.5 %s; so Dec (no trace) off and on"
      % (acc[0], conj(acc[1]), F1_at(cb, "e", "b0"), faithful_on(cb, H), s, s5))
    json_out["histories"] = dict(stats={"%s|%s" % k: v for k, v in stats.items()}, shapes={"%s|%s" % k: v for k, v in shapes.items()},
                                 accounts=len(accounts), surv_false=len(bad))


# ---- 3. R2V2.8: Desc per case (rule 5 (3)) ----------------------------------------------------------------------------

def invariants(D):
    return (len(D.ports), tuple(sorted(len(D.dom[v]) for v in D.ports)), len(D.comps), tuple(sorted(len(D.foot[j]) for j in D.comps)),
            len(D.A), len(D.B))


def with_idle(D):
    """D plus an idle component on its first port (the full relation at every pair): same solutions, one more component."""
    comps = list(D.comps) + ["idle"]
    foot = dict(D.foot)
    foot["idle"] = (D.ports[0],)
    E = Org(D.name + "+idle", D.ports, D.dom, comps, foot, D.B, D.A, D._compose,
            lambda j, a, b: (frozenset((x,) for x in D.dom[D.ports[0]]) if j == "idle" else D.L(j, a, b)))
    return E


def section_desc(json_out):
    P("=" * 150)
    P("3. R2V2.8: V1.6'S FORMULA, Acc ∧ ¬BadTarget ∧ ¬BadReq (D3.6), WITH A DESC PER CASE (Inv-R2-2; the agent's invention, P-R2S2-3)")
    # the program's targets per phenomenon (the organizations the program builds that meet the phenomenon Desc names)
    from model.claims_r3a2 import m13
    from model.claims_s106 import sign_target, sign_mech
    vane_b = OW.vane_boundary(["cP"]).p.D
    lib = {
        "sign": [("D_sign (claims_s106; the day an edit)", sign_target()), ("D_sign_day (claims_s106; a day port)", sign_mech().p.D),
                 ("D_sign_b (round 1's second checker; the day a boundary)", OW.sign_boundary(2).p.D),
                 ("D_sign_mix (this round, P-R2S2-7)", OW.sign_mixed(2).p.D)],
        "vane": [("M13's D (claims_r3a2; the wind an edit)", m13().p.D), ("D_vane (FC28.new2; the wind a boundary)", vane_b),
                 ("D_vane^mix (the reply's)", OW.vane_mixed_target())],
    }
    descs = {
        "sign": "a sign whose colour is red on Mondays and blue on Tuesdays (the owner's words, S44)",
        "vane": "a vane that may point anywhere in still air and points north in a north wind (S41 Q15)",
    }
    bad = {}
    for ph, lst in lib.items():
        inv = [invariants(D) for _, D in lst]
        distinct = len(set(inv))
        bad[ph] = distinct > 1
        P("   phenomenon '%s': Desc = %s" % (ph, descs[ph]))
        for (nm, D), iv in zip(lst, inv):
            P("      %-58s invariants (ports, domain sizes, components, footprint sizes, |A|, |B|) %s" % (nm, iv))
        P("      organizations meeting Desc among the program's targets, up to renaming: at least %d (their invariants differ) -> BadTarget %s" % (distinct, bad[ph]))
    P("   core.BAD_PHENOMENA = %s; computed here: %s; equal: %s" % (sorted(core.BAD_PHENOMENA), sorted(k for k, v in bad.items() if v),
                                                                  set(core.BAD_PHENOMENA) == set(k for k, v in bad.items() if v)))
    # the worked cases' Desc at each grain, and Acc
    table = [
        ("the pole, E1 (C1, C2, C_id; the student's formula)", "the shadow L of a pole of height H at elevation θ, with the question's own value ranges", "pole", "one target (pole() with those ranges)"),
        ("the two balances (E3, e2.06c's ℰ_bal)", "two readings r1 = x + b_A, r2 = x + b_B of one mass x, and their difference d", "balances", "one target (ℰ_bal's D)"),
        ("the sign (S44)", descs["sign"], "sign", "four targets, pairwise different invariants"),
        ("the weathervane (S41 Q15)", descs["vane"], "vane", "three targets, pairwise different invariants"),
        ("R3-Q1's hand-turned vane", "a vane that points anywhere and points north when turned by hand", "vane-hand", "one target"),
        ("the bridge (FC84.new1)", "a bridge built to a fixed brief", "bridge", "no organization built (FC84.new1 builds provenance only)"),
    ]
    for nm, d, ph, tg in table:
        bt = bad.get(ph, False) if ph in bad else (None if ph == "bridge" else False)
        P("   %-48s Desc (phenomenon) = %s -> %s -> BadTarget %s; BadReq F (p is an instance of Desc's conditions on (C, Q))" % (nm, d, tg, tf(bt)))
    P("   target grain: Desc := 'D as given' for every question -> BadTarget F, BadReq F everywhere (the variant idle).")
    # widest: D plus an idle component meets the same Desc (same answers on C) and is not D up to renaming
    P("   widest grain: every organization over Desc's ports with Desc's answers meets it. For each worked target D, D + an idle component:")
    ok_all = True
    seen = set()
    for lab, where, c in worked_cases():
        D = c.p.D
        if id(D) in seen:
            continue
        seen.add(id(D))
        D2 = with_idle(D)
        same = all(c.p.Q(D2, a, b, c.p.deltaD) == c.p.ans(a, b) for (a, b) in c.p.C)
        diff = invariants(D2) != invariants(D)
        ok_all = ok_all and same and diff
    P("      on every worked target (%d): the same answers on C and different invariants: %s -> BadTarget T for every question" % (len(seen), ok_all))
    json_out["desc"] = dict(bad=bad, table=table, widest_all=ok_all, n_targets=len(seen))


# ---- 4. the built cases of round 2's reply ---------------------------------------------------------------------------

def balances():
    """e2.06c (Inv-R2-5): the two balances as a question with a candidate. Ports x, bA, bB, r1, r2, d over {0,1,2} (GF(3));
    cx, cA, cB pin x, bA, bB per boundary (b1: 1, 0, 1; b2: 1, 0, 2: u_B − u_A differs); cr1: r1 = x + bA; cr2: r2 = x + bB;
    cd: d = r2 − r1; A = {1}; C = {1} × {b1, b2}; Q_w on d; ℰ_bal = D, identity transport, Γ = {cd}."""
    F = (0, 1, 2)
    pin = {"b1": {"x": 1, "bA": 0, "bB": 1}, "b2": {"x": 1, "bA": 0, "bB": 2}}

    def Lf(j, a, b):
        if j in ("cx", "cA", "cB"):
            return frozenset([(pin[b][{"cx": "x", "cA": "bA", "cB": "bB"}[j]],)])
        if j == "cr1":
            return frozenset((x, u, (x + u) % 3) for x in F for u in F)
        if j == "cr2":
            return frozenset((x, u, (x + u) % 3) for x in F for u in F)
        return frozenset((r1, r2, (r2 - r1) % 3) for r1 in F for r2 in F)
    ports = ["x", "bA", "bB", "r1", "r2", "d"]
    foot = {"cx": ("x",), "cA": ("bA",), "cB": ("bB",), "cr1": ("x", "bA", "r1"), "cr2": ("x", "bB", "r2"), "cd": ("r1", "r2", "d")}
    D = Org("D_bal", ports, {v: F for v in ports}, list(foot), foot, ["b1", "b2"], [ONE], lambda a2, a1: ONE, Lf)
    p = Question(D, [(ONE, "b1"), (ONE, "b2")], "b1", PortQuery(), "d", name="p_bal")
    lam = {k: (frozenset([k]), {v: Translation([v]) for v in foot[k]}) for k in foot}
    return Candidate(D, p, {v: Translation([v]) for v in ports}, {ONE: ONE}, {"b1": "b1", "b2": "b2"}, lam, ["cd"], "d", name="ℰ_bal")


def e_bad():
    """R2V2.3 (b)'s ℰ_bad: D as in M13; E = D with L_cy(e,b0) = {(0,1),(1,0)} (so (F1) fails at (e,b0))."""
    from model.claims_r3a2 import m13
    c = m13()
    D = c.p.D
    E = Org("E_bad", D.ports, D.dom, D.comps, D.foot, D.B, D.A, D._compose,
            lambda j, a, b: frozenset([(0, 1), (1, 0)]) if (j == "cy" and a == "e") else D.L(j, a, b))
    return c.replace(E=E, name="ℰ_bad")


def r25_case():
    """R2V2.5's small case: p0 ∈ {0,1}; h on (p0); B = {b0}; A = {1, a}; L_h full at both; C = {(1,b0),(a,b0)}; ⊥ at both."""
    D = Org("D_r25", ["p0"], {"p0": (0, 1)}, ["h"], {"h": ("p0",)}, ["b0"], [ONE, "a"], lambda a2, a1: None,
            lambda j, a, b: frozenset([(0,), (1,)]))
    p = Question(D, [(ONE, "b0"), ("a", "b0")], "b0", PortQuery(), "p0", name="p_r25")
    return Candidate(D, p, {"p0": Translation(["p0"])}, {ONE: ONE, "a": "a"}, {"b0": "b0"}, {"h": (frozenset(["h"]), {"p0": Translation(["p0"])})},
                     ["h"], "p0", name="ℰ_r25")


def section_small(json_out):
    P("=" * 150)
    P("4. THE REPLY'S SMALL CASES AND ITS OTHER CLAIMS, BUILT AND RUN")
    out = {}
    c = r25_case()
    for s in ("off", "R2V2.5"):
        with setting(**SETTINGS[s]):
            P("   R2V2.5 case (%s): Ans %s; 'a' a relabeling (D6.9) %s; NC2 %s; Acc %s" % (s, {x: c.p.ans(*x) for x in sorted(c.p.C, key=repr)},
                                                                                   relabeling(c.p, "a"), NC2(c, witness=True), account(c)))
            out["r25 " + s] = (relabeling(c.p, "a"), bool(account(c)))
    # R2V2.6: histories with an earlier representation of t, H, surv, cod t (tags, Θ by hand), on every worked account
    P("   R2V2.6: Sel of every worked account on H = {(1,b0)} in a history whose earlier occurrence o1 represents x (tag), o_t = o2:")
    accs = [(lab, c) for lab, w, c in worked_cases() if under("off", lambda: bool(account(c)))]
    for x in ("t", "H", "surv", "cod", "nothing"):
        row = {}
        for s in ("off", "R2V2.6 written", "R2V2.6 HS", "R2V2.6 reply"):
            with setting(**SETTINGS[s]):
                n = 0
                for lab, c in accs:
                    h = Hist(["o1", "o2"], [] if x == "nothing" else [("o1", x)], set(c.p.C), admitted=True, prepares=False)
                    n += bool(sel(c, [(ONE, c.p.b0)], h))
                row[s] = n
        P("      o1 represents %-8s Sel on %s of %d accounts" % (x, row, len(accs)))
        out["r26 " + x] = row
    # the student's copy (FC30.new1 (d)) under the three reaches: the chain source ≺ copy
    p, c = fwd_pole_cand()
    for s in ("off", "R2V2.6 written", "R2V2.6 HS", "R2V2.6 reply"):
        with setting(**SETTINGS[s]):
            held_o = bool(faithful(c))
            res = []
            for Hx in ([(ONE, "b1_45")], []):
                selc = bool(Hx) and faithful_on(c, Hx)
                fps = prov_fixed_points(2, [1, held_o], [1, 0], [0, selc], "T'", True)
                res.append(prov_show(2, fps))
        P("   the student's copy (source ≺ copy), %-15s H = {(1,b1_45)}: %s; H = ∅: %s" % (s, res[0], res[1]))
        out["student " + s] = res
    # R2V2.10: FC104.new1's case (δ_E = θ): Sel on H = {(1,b1_45)}; Viol at that pair of H; SelResp there; Surp there
    p, c0 = fwd_pole_cand()
    c = c0.replace(deltaE="T", name="ℰ_fwd, δ_E = θ")
    x = (ONE, "b1_45")
    t2 = c.replace(name="t2")
    mu = {c.name: [t2.name]}
    for s in ("off", "R2V2.10"):
        with setting(**SETTINGS[s]):
            h = Hist(["o1"], [], {x})
            sl = sel(c, [x], h)
            vi = viol_at(c, *x)
            sr = selresp(c, t2, [x], x, h, mu)
            surp = sl and (x not in [x]) and vi
        P("   R2V2.10 FC104.new1's case (%s): Sel on H = {%s} %s; Viol at that pair of H %s; SelResp(t → t2) at it %s; Surp at it %s (D12.7 asks (a,b) ∉ H)"
          % (s, x, sl, vi, sr, surp))
        out["r210 " + s] = (sl, vi, sr, surp)
    json_out["small"] = out


# ---- 5. the claimed-only edges of round 1 (rule 5 (2)) ----------------------------------------------------------------

def section_edges(json_out):
    P("=" * 150)
    P("5. ROUND 1'S CLAIMED-ONLY EDGES OF THE SHARE, THE REPLY'S SETTLEMENTS COMPUTED")
    out = {}
    # e2.06c: V2.3 blocks L331.s2 and E2: the balances as a question with a candidate
    c = balances()
    for s in ("off", "V2.3"):
        with setting(S2_VARIANT="off" if s == "off" else "V2.3"):
            v, d = account(c, detail=True)
            out["e2.06c " + s] = bool(v)
            P("   e2.06c ℰ_bal (%s): answers %s; Acc %s [%s]; Dependence witness %s" % (s, {x: c.p.ans(*x) for x in sorted(c.p.C, key=repr)}, v, conj(d), NC2(c, witness=True)))
    P("          E2's identification reads no (E) (FC28's Ident part, FC57, FC58 unchanged under V2.3, round 1 §6); Ident's contract clause on C = {1}×B: %s"
      % (len(set(obs_value(c.p.D, "d", a, b) for (a, b) in c.p.C)) > 1))
    # e2.07: V2.3 with V1.4 (section 1's D3.3 variant, re-implemented here: ∃(a,b) ∈ C: a ≠ 1 ∧ obs(a,b) ≠ obs(1,b0))
    Did = pole(bounds=[(1, 45), (2, 45), (3, 45)])
    pid = Question(Did, frozenset((ONE, b) for b in Did.B), "b1_45", fibre_query(), ("H", "T", "L"), name="p_ident")
    cf = pole_fwd_candidate(pid)
    from model.cases import pole_rev_candidate
    cr = pole_rev_candidate(pid)
    obs = {x: obs_value(Did, "L", *x) for x in sorted(pid.C, key=repr)}
    ident_i163 = len(set(obs.values())) > 1
    ident_v14 = any(a != ONE and obs[(a, b)] != obs[(ONE, "b1_45")] for (a, b) in obs)
    rows = {}
    for s in ("off", "V2.3"):
        with setting(S2_VARIANT="off" if s == "off" else "V2.3"):
            rows[s] = (bool(account(cf)), bool(account(cr)), bool(faithful(cr)), bool(A_ok(cr)))
    P("   e2.07 C_id (the pole, fibre query): Ident's contract clause I163 %s, V1.4 %s; E_fwd, E_rev: Acc off %s, %s; under V2.3 %s, %s; E_rev faithful and (A) off %s, under V2.3 %s"
      % (ident_i163, ident_v14, rows["off"][0], rows["off"][1], rows["V2.3"][0], rows["V2.3"][1], rows["off"][2:], rows["V2.3"][2:]))
    out["e2.07 C_id"] = dict(ident_i163=ident_i163, ident_v14=ident_v14, acc=rows)
    # e2.11b: (Nec)'s defeat set with ℰ = E_enc on C1, V2.4 off and on, an argument not using (E) that rules out ¬Expl(ℰ)
    D = pole()
    C1, C2, _ = pole_contracts(D)
    p1 = Question(D, C1, "b1_45", PortQuery(), "L", name="C1")
    ee = table_candidate(p1, set(D.ports), encode=True)
    e = "Expl_" + ee.name
    beta = Step("MP", e, [Leaf("r", "record"), Leaf(Imp("r", e))])
    jn = Assessor(["MP"], ["r", Imp("r", e)])
    outn = bool([a for a in X(jn, Not(e), [beta]) if not_using_E(a, ee.name)])
    for s in ("off", "V2.4 q every"):
        with setting(**SETTINGS[s]):
            acc = bool(account(ee))
            pres = bool(faithful(ee))
            res = {}
            for kind in ("Dec", "Con", "Sel"):
                _, _, dec = provenance_of(ee, kind, [(ONE, "b1_45")])
                res[kind] = (outn and not pres, outn and not (acc and not dec))
        P("   e2.11b E_enc on C1 (%s): Acc %s; Faithful_C(t) %s; an argument not using (E) ruling out ¬Expl usable %s; in (Nec)'s defeat set as L538 (D16.XV) states it / as L61's 'their' reads: %s"
          % (s, acc, pres, outn, {k: "%s/%s" % v for k, v in res.items()}))
        out["e2.11b " + s] = res
    # e2.16c: an argument whose premise is ETV_j(ℰ; p) and whose conclusion is ¬Expl(ℰ)
    etv = "ETV_" + ee.name
    alpha = Step("MP", Not(e), [Leaf(etv, "record"), Leaf(Imp(etv, Not(e)))])
    j = Assessor(["MP"], [etv, Imp(etv, Not(e))])
    ro_expl = bool(X(j, e, [alpha]))
    ro_nexpl = bool(X(j, Not(e), [alpha]))
    P("   e2.16c α: ETV_j(ℰ;p), ETV → ¬Expl(ℰ) ⊢ ¬Expl(ℰ): rules out Expl(ℰ) (a (Suff) defeat's work) %s, not using (E) %s; rules out ¬Expl(ℰ) (what (Nec)'s defeat needs) %s"
      % (ro_expl, not_using_E(alpha, ee.name), ro_nexpl))
    out["e2.16c"] = dict(rules_out_expl=ro_expl, rules_out_not_expl=ro_nexpl, not_using_E=not_using_E(alpha, ee.name))
    # e2.19: the argument from ConfCl (L315.s13-s14), round 1's V2.7 case
    c, allow = R1.v27_case()
    for s in ("off", "V2.7"):
        with setting(S2_VARIANT="off" if s == "off" else "V2.7"):
            cc = bool(conf_claim(c, ONE, "b0", allow))
            got = alpha_from_confcl(c, cc)
        P("   e2.19 round 1's V2.7 case (%s): ConfCl %s; the record constructible %s; α usable and rules out Acc(ℰ) for j accepting χ: %s"
          % (s, cc, cc, got))
        out["e2.19 " + s] = dict(confcl=cc, out=got)
    # D8.6 itself: ConfG_χ does not read D8.5 (core.conf_given): unchanged under V2.7 (round 1's FC54; the generated pairs in s108r2_s2_gen.py)
    json_out["edges"] = out


def A_ok(c):
    from model.core import A
    return A(c)


def alpha_from_confcl(c, confcl):
    """α := MP on {r, r → ¬Acc(ℰ)}, r the record 'ConfCl(ℰ,χ;a,b) ∧ (a,b) ∈ C ∧ χ', made from the computed ConfCl: it exists only
    where ConfCl holds (the reply's reading). j tentatively accepts χ, the pair's membership, and the rule; Out_j('Acc(ℰ)')?"""
    if not confcl:
        return False
    acc = "Acc_" + c.name
    r = And("ConfCl", "inC", "chi")
    alpha = Step("MP", Not(acc), [Leaf(r, "record"), Leaf(Imp(r, Not(acc)))])
    j = Assessor(["MP"], [r, Imp(r, Not(acc))])
    return bool(X(j, acc, [alpha]))


def main():
    json_out = {}
    only = sys.argv[sys.argv.index("--sections") + 1].split(",") if "--sections" in sys.argv else ["1", "2a", "2b", "2c", "3", "4", "5"]
    rows = section_worked(json_out) if "1" in only else None
    if "2a" in only:
        section_encodings(json_out)
    if "2b" in only:
        section_quantifier(rows, json_out)
    if "2c" in only:
        section_histories(json_out)
    if "3" in only:
        section_desc(json_out)
    if "4" in only:
        section_small(json_out)
    if "5" in only:
        section_edges(json_out)
    if "--json" in sys.argv:
        with open(sys.argv[sys.argv.index("--json") + 1], "w", encoding="utf-8") as f:
            json.dump(json_out, f, ensure_ascii=False, indent=1, default=repr)


if __name__ == "__main__":
    main()
