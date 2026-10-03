# S108 Part A round 2, section 3: what the cases script and the worlds script share. Imports the package model/ of this folder;
# writes nothing. Standard library only.
#   STATES      the switch states computed (round 2's variants and sub-readings; round 1's C8, C9, C10 and section 2's C7 under
#               round 2's readings), each a function that sets the switches
#   chain_out   Sel and Con at each occurrence of a chain o1 ≺ … ≺ on under the cuts T′, T, K by the staging (the unique fixed
#               point, D18.1), with the program's own episode (claims_b.chain_eps, so D13.8's key and V3.5 as switched) and
#               s108r2s3.witnesses (D11.3's ⪯ as switched); start[o]: the first occurrence of o's construction trace (None: o
#               itself, the program's one-occurrence trace, I56). With start None it equals claims_b.prov_fixed_points (checked:
#               s108r2_s3_worlds.py chains, 'crosscheck')
#   judge       every result for one candidate under the current switches: Acc; Dec(t) and Account ∧ ¬Dec(t) on each history;
#               Build
#   claim_ep    the ℰ′ whose claim 'Acc(ℰ′)' a trace's output uses (R2V3.1; S108-3-I5 and R2-3-I1)
import itertools
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from model import s108s3, s108r2s3  # noqa: E402
from model import claims_b  # noqa: E402
from model.core import ONE, Question, PortQuery, account, faithful  # noqa: E402
from model.claims_b import Hist, sel, con, chain_eps, prov_fixed_points, build_at  # noqa: E402
from model.claims_s41 import provenance_of  # noqa: E402

CLAIMS = ("own", "widest", "designation", "gamma", "port")


def set_state(r1="none", ct="prepares", r2="none", reckey=None, parts=None, i8=None, h_nonempty=True):
    """Round 1's switch (s108s3), round 2's (s108r2s3), and D12.1's H ≠ ∅ (claims_b.SEL_H_NONEMPTY; False = section 2's V2.5,
    Sel with an empty trial history, C7)."""
    s108r2s3.set_variant(r2, reckey=reckey, parts=parts, i8=i8)
    if r2 != "R2V3.1":
        s108s3.set_variant(r1, ct)
    claims_b.SEL_H_NONEMPTY = h_nonempty


def reset():
    set_state()


# name -> keyword arguments of set_state. 'none' first. Round 2's variants alone, then the round-1 candidates under each reading.
STATES = [
    ("none", {}),
    ("R2V3.1", dict(r2="R2V3.1")),
    ("R2V3.2 (key: new contract, the formal core's words)", dict(reckey="contract")),
    ("R2V3.4 (parts: ports)", dict(r2="R2V3.4", parts="ports")),
    ("R2V3.4 (parts: edits)", dict(r2="R2V3.4", parts="edits")),
    ("R2V3.5", dict(r2="R2V3.5")),
    ("R2V3.6", dict(r2="R2V3.6")),
    ("R2V3.7", dict(r2="R2V3.7")),
    ("R2V3.8", dict(r2="R2V3.8")),
    ("R2V3.9", dict(r2="R2V3.9")),
    ("R2V3.10", dict(r2="R2V3.10")),
    # C8 (V3.4) under S108-3-I2's two choices (CT reads Prepares / ExplUse); the claim choice (I5) is per history
    ("C8: V3.4, CT reads Prepares", dict(r1="V3.4", ct="prepares")),
    ("C8: V3.4, CT reads ExplUse (= R2V3.1)", dict(r1="V3.4", ct="build")),
    # C9 (V3.5) under D13.8's two keys; the extent and the encoding are per history
    ("C9: V3.5 (key: change)", dict(r1="V3.5")),
    ("C9: V3.5 (key: new contract)", dict(r1="V3.5", reckey="contract")),
    ("C9: V3.5 with R2V3.7", dict(r1="V3.5", r2="R2V3.7")),
    ("C9: V3.5 with R2V3.6", dict(r1="V3.5", r2="R2V3.6")),
    # C10 (V3.6) under S108-3-I4's three readings and S108-3-I3's two
    ("C10: V3.6 (parts: components)", dict(r1="V3.6")),
    ("C10: V3.6 (parts: ports)", dict(r1="V3.6", parts="ports")),
    ("C10: V3.6 (parts: edits)", dict(r1="V3.6", parts="edits")),
    ("C10: V3.6 with R2V3.6", dict(r1="V3.6", r2="R2V3.6")),
    # C7 (section 2's V2.5: Sel with H = ∅) on hand-set and on chain histories (I90, the reply's R2V3.6 names it)
    ("C7: V2.5 (H = ∅ allowed)", dict(h_nonempty=False)),
    ("C7: V2.5 with R2V3.6", dict(h_nonempty=False, r2="R2V3.6")),
]
# the baseline each state is compared with (the same sub-readings with the round-1 candidate's variant off)
BASE = {
    "C9: V3.5 (key: new contract)": "R2V3.2 (key: new contract, the formal core's words)",
    "C9: V3.5 with R2V3.7": "R2V3.7",
    "C9: V3.5 with R2V3.6": "R2V3.6",
    "C10: V3.6 (parts: ports)": "R2V3.4 (parts: ports)",
    "C10: V3.6 (parts: edits)": "R2V3.4 (parts: edits)",
    "C10: V3.6 with R2V3.6": "R2V3.6",
    "C7: V2.5 with R2V3.6": "R2V3.6",
}
# C10 under S108-3-I3's other choice (𝒯 = ∅ with no construction stated, R2V3.5): V3.6 against R2V3.5
STATES.append(("C10: V3.6 against R2V3.5 (I3: 𝒯 = ∅)", dict(r1="V3.6", r2="R2V3.5")))
BASE["C10: V3.6 against R2V3.5 (I3: 𝒯 = ∅)"] = "R2V3.5"


# ---- the chain evaluator ---------------------------------------------------------------------------------------------------

def chain_out(n, held, trace, selc, qs, rs, rd, start=None, explu=None):
    """[(Sel, Con)] per occurrence under the cut rd ∈ {T', T, K}, with the program's episode and ⪯ as switched."""
    eps = chain_eps(qs, rs)
    R, out = set(), []
    for o in range(n):
        c_ = False
        if trace[o] and not (s108s3.ct_reads_expluse() and explu is not None and not explu[o]):
            st = o if start is None else start[o]
            for i in range(st + 1):  # h' = o_i … o_o holds the trace's occurrences o_st … o_o
                if not eps(i, o):
                    continue
                if rd == "K":
                    ok = any(x in R for x in s108r2s3.witnesses(i, o, strict=True))
                else:
                    ok = any(held[x] for x in s108r2s3.witnesses(i, o))
                if ok:
                    c_ = True
                    break
        if rd == "T":
            s_ = selc[o] and not any(held[x] for x in range(o))
        else:
            s_ = selc[o] and not any(x in R for x in range(o))
        s_ = s_ and not trace[o]  # I161
        if held[o] and (s_ or c_):
            R.add(o)
        out.append((bool(s_), bool(c_)))
    return out


def chain_dec(n, held, trace, selc, qs, rs, rd, start=None, explu=None):
    """Dec at the output (the last occurrence): a bool under T′, T, K; under U a tuple of the values over every fixed point
    (claims_b.prov_fixed_points, or, with a trace extent, the same enumeration with the extent)."""
    if rd != "U":
        s, k = chain_out(n, held, trace, selc, qs, rs, rd, start, explu)[n - 1]
        return not s and not k
    if start is None:
        fps = prov_fixed_points(n, held, trace, selc, "U", True, chain_eps(qs, rs), explu=explu)
    else:
        fps = u_fixed_points(n, held, trace, selc, qs, rs, start)
    return tuple(sorted(set(not sc[n - 1][0] and not sc[n - 1][1] for R, sc in fps)))


def u_fixed_points(n, held, trace, selc, qs, rs, start):
    """Cut U with a trace extent (the second checker's o3_trace_extent.py, with the program's episode and ⪯ as switched)."""
    eps = chain_eps(qs, rs)
    fps = []
    for bits in itertools.product([0, 1], repeat=n):
        R = frozenset(o for o in range(n) if bits[o])
        sc = {}
        for o in range(n):
            c_ = False
            if trace[o]:
                for i in range(start[o] + 1):
                    if eps(i, o) and any(x in R for x in s108r2s3.witnesses(i, o)):
                        c_ = True
                        break
            s_ = selc[o] and not any(x in R for x in range(o + 1)) and not trace[o]
            sc[o] = (bool(s_), bool(c_))
        if frozenset(o for o in range(n) if held[o] and (sc[o][0] or sc[o][1])) == R:
            fps.append((R, sc))
    return fps


# ---- the claim a trace's output uses (R2V3.1) ------------------------------------------------------------------------------

def claim_ep(c, which):
    """ℰ′ = (E, p′, t, Γ′, δ′) sharing t with ℰ = c, or None where the choice gives none. own: ℰ itself; widest: ℰ on the widest
    contract t translates (S108-3-I5, round 1's); designation: δ′ the first port of E other than δ_E (R2-3-I1, the reply's
    δ′ = H for the pole); gamma: Γ′ every component of E where Γ is not all of them, else Γ without its last (S108r2-3-I1);
    port: the question on the first port of D other than p's, E designating the same port (S108r2-3-I1; only where E has it)."""
    if which == "own":
        return c
    if which == "widest":
        wide = frozenset((a, b) for a in c.p.D.A for b in c.p.D.B if a in c.tau and b in c.sigma)
        return c.replace(p=c.p.with_C(wide)) if (ONE, c.p.b0) in wide else c
    if which == "designation":
        others = [v for v in c.E.ports if v != c.deltaE]
        return c.replace(deltaE=others[0]) if others else None
    if which == "gamma":
        allc = tuple(c.E.comps)
        if tuple(sorted(c.Gamma)) != tuple(sorted(allc)):
            return c.replace(Gamma=allc)
        return c.replace(Gamma=tuple(c.Gamma)[:-1]) if len(c.Gamma) > 1 else None
    if which == "port":
        if not isinstance(c.p.Q, PortQuery):
            return None
        others = [u for u in c.p.D.ports if u != c.p.deltaD and u in c.E.ports]
        if not others:
            return None
        p2 = Question(c.p.D, c.p.C, c.p.b0, c.p.Q, others[0], excl=c.p.excl, name=c.p.name + "[" + others[0] + "]")
        return c.replace(p=p2, deltaE=others[0])
    raise ValueError(which)


def acc_of(c):
    try:
        return bool(account(c))
    except Exception:  # a choice the organization cannot carry is recorded as no ℰ′
        return None


# ---- one candidate, every history ------------------------------------------------------------------------------------------

HIST_NOTE = {
    "Dec": "hand-set (provenance_of): no selection admitted, no trace",
    "Con": "hand-set: o1 ≺ o2, a trace, cod t tagged at o2",
    "Sel": "hand-set: a selection on H, no construction stated",
    "Sel (H = ∅)": "hand-set: a selection history with nothing tried (C7's)",
    "Sel-parts": "a selection on H whose stated construction lacks E's last component (round 1's S108-3-I4 history)",
    "Con-chg (tags)": "cod t tagged at o1, C → C′ unrecorded into o2, the trace at o2 (tag encoding)",
    "Con-chg (chain T′)": "the same, Held computed (t at o2 from Faithful), the trace at o2 only",
    "Con-span (chain T′)": "the same, the output's trace spanning o1 … o2 (R2V3.3 (b))",
    "Con-far (tags)": "o1 ≺ o2 ≺ o3, one contract, cod t tagged at o1, the trace at o3",
    "Con-far (chain T′)": "the same, Held at o1 and at o3 computed, not at o2",
    "Con-reentry (tags)": "q = [C′, C, C], one record, of ρ_C, at o3; cod t tagged at o1; the trace at o3 (R2V3.2's case)",
    "Con-reentry (chain T′)": "the same, Held computed at o3",
    "Con-reentry-span (chain T′)": "the same, the output's trace spanning o1 … o3",
}


def pre_of(c, claims=CLAIMS):
    """What no switch of section 3 moves, computed once per candidate: Acc(ℰ) and Acc(ℰ′) for each claim choice (checked: no
    section-3 switch reaches account; the cases script computes them under every state)."""
    out = {"acc": bool(account(c))}
    for w in claims:
        e2 = claim_ep(c, w)
        out[w] = acc_of(e2) if e2 is not None else None
    return out


def judge(c, H, claims=CLAIMS, pre=None):
    acc = bool(account(c)) if pre is None else pre["acc"]
    occ = set(c.p.C)
    res = {"Acc": acc}
    held_out = bool(faithful(c))
    for kind in ("Dec", "Con", "Sel"):
        res["Dec " + kind] = provenance_of(c, kind, H)[2]
    res["Dec Sel (H = ∅)"] = provenance_of(c, "Sel", [])[2]  # C7's history: nothing tried
    if c.E.comps:
        h = Hist(["o1"], [], occ, admitted=True, prepares=False, parts=list(c.E.comps), stated=list(c.E.comps)[:-1])
        res["Dec Sel-parts"] = not sel(c, H, h) and not con(h)
    h = Hist(["o1", "o2"], [("o1", "cod")], occ, admitted=True, prepares=True, contracts=["C", "C'"], records=[False, False])
    res["Dec Con-chg (tags)"] = not sel(c, H, h) and not con(h)
    res["Dec Con-chg (chain T′)"] = chain_dec(2, [1, held_out], [0, 1], [0, 0], ["C", "C'"], [False, False], "T'")
    res["Dec Con-span (chain T′)"] = chain_dec(2, [1, held_out], [0, 1], [0, 0], ["C", "C'"], [False, False], "T'", start=[0, 0])
    h = Hist(["o1", "o2", "o3"], [("o1", "cod")], occ, admitted=True, prepares=True)
    res["Dec Con-far (tags)"] = not sel(c, H, h) and not con(h)
    res["Dec Con-far (chain T′)"] = chain_dec(3, [1, 0, held_out], [0, 0, 1], [0, 0, 0], ["C"] * 3, [False] * 3, "T'")
    h = Hist(["o1", "o2", "o3"], [("o1", "cod")], occ, admitted=True, prepares=True, contracts=["C'", "C", "C"], records=[False, False, True])
    res["Dec Con-reentry (tags)"] = not sel(c, H, h) and not con(h)
    res["Dec Con-reentry (chain T′)"] = chain_dec(3, [1, 0, held_out], [0, 0, 1], [0, 0, 0], ["C'", "C", "C"], [False, False, True], "T'")
    res["Dec Con-reentry-span (chain T′)"] = chain_dec(3, [1, 0, held_out], [0, 0, 1], [0, 0, 0], ["C'", "C", "C"], [False, False, True], "T'",
                                                       start=[0, 1, 0])
    for w in claims:
        if pre is None:
            e2 = claim_ep(c, w)
            a2 = acc_of(e2) if e2 is not None else None
        else:
            a2 = pre[w]
        res["Acc(ℰ′) " + w] = a2
        if a2 is None:
            continue
        ex = s108s3.expl_use(True, a2)
        h = Hist(["o1", "o2"], [("o2", "cod")], occ, admitted=True, prepares=True, explu=ex)
        res["Dec Con-explu " + w] = not sel(c, H, h) and not con(h)
        res["Build " + w] = build_at(1, [1], [1], "T'", frozenset(), 0, explu=[ex])
    for k in list(res):
        if k.startswith("Dec "):
            d = res[k]
            res["Expl" + k[3:]] = (acc and not d) if isinstance(d, bool) else tuple(acc and not x for x in d)
    return res


# ---- t′ = t with one more part (S108-3-I4's cases, round 1's extra_part) ---------------------------------------------------

def extras(c, H, K):
    """t′ = t + a part k_x ('idle', 'copy', 'deviate' at the first pair of C∖H t translates), on a selection history whose stated
    construction is t's own parts; Acc(t′), Dec(t′), and the pairs of C∖H at which the survivors on H of {t, t′} ∩ 𝒯 differ."""
    out = {}
    others = [x for x in sorted(c.p.C, key=repr) if x not in H and c.translates(*x)]
    variants = [("idle", K.extra_part(c, "idle")), ("copy", K.extra_part(c, "copy"))] if c.E.comps else []
    if others and c.deltaE in c.E.ports:
        a, b = others[0]
        variants.append(("deviate", K.extra_part(c, "deviate", (c.tau[a], c.sigma[b]))))
    for lab, t2 in variants:
        try:
            acc2 = bool(account(t2))
            h2 = Hist(["o1"], [], set(c.p.C), admitted=True, prepares=False, parts=list(t2.E.comps), stated=list(c.E.comps))
            h1 = Hist(["o1"], [], set(c.p.C), admitted=True, prepares=False, parts=list(c.E.comps), stated=list(c.E.comps))
            s2 = sel(t2, H, h2)
            pop = [x for x, h in ((c, h1), (t2, h2)) if in_pop(x, h)]
            surv = [x for x in pop if claims_b.faithful_on(x, H)]
            under = sum(1 for (a, b) in others if len(set(repr(x.ans_E(x.tau[a], x.sigma[b])) for x in surv)) > 1)
            out[lab] = dict(acc=acc2, dec=not s2, expl=acc2 and s2, under=under)
        except Exception as e:  # recorded, not hidden
            out[lab] = dict(error=repr(e)[:200])
    return out


def in_pop(x, h):
    """t ∈ 𝒯 (D15.8) as claims_b.sel reads it (the parts reading and R2V3.5 as switched)."""
    parts_r = s108r2s3.parts_read(x, h.parts)
    stated_r = s108r2s3.parts_read(x, h.stated)
    if (parts_r is None or stated_r is None) and not s108r2s3.no_construction_admits() and not s108s3.on("V3.6"):
        return False
    return s108s3.in_population(h.admitted, parts_r, stated_r)
