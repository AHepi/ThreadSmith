# S108 Part A, section 4: the external examples FC-E1–FC-E5 (s104_external.py) and the creative transport case CT1–CT8
# (s104_creative_transport.py): every candidate each script hands to core.account is recorded (the scripts run unchanged,
# their printout discarded; their own printouts under each variant are compared in section 4 runs/scripts/), then
# Acc, Slot and being an explanation are computed under each reading, with the hand-set histories of s108_s4_cases.py;
# CT8's own provenance (its readings R1–R5, T′ as the script computes it) is carried to being an explanation.
#   PYTHONHASHSEED=0 python3 -B s108_s4_scripts_expl.py > OUT.txt
import contextlib
import io
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from model import core, s108_s4  # noqa: E402
from model.core import account, faithful  # noqa: E402
from model.claims_b import Hist, sel, con, faithful_on  # noqa: E402
import s108_s4_cases as SC  # noqa: E402
import s104_external as EXT  # noqa: E402
import s104_creative_transport as CTM  # noqa: E402

P = print


def record(mod, fn):
    got = []
    orig = mod.account

    def wrap(c, *a, **k):
        got.append(c)
        return orig(c, *a, **k)
    mod.account = wrap
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            fn()
    finally:
        mod.account = orig
    seen, out = set(), []
    for c in got:
        if id(c) not in seen:
            seen.add(id(c))
            out.append(c)
    return out


def summarize(name, cands):
    P("%s: %d candidates handed to account" % (name, len(cands)))
    accT = [c for c in cands if account(c)]
    slotT = [c for c in accT if SC.slot_row(c) and SC.slot_row(c)["every"]]
    P("   meeting (E): %d; of them with a slot under 'every': %d %s" % (len(accT), len(slotT), sorted(set(c.name for c in slotT))[:8]))
    tally = {}
    for c in accT:
        sr = SC.slot_row(c)
        s_every = bool(sr and sr["every"])
        for h in SC.HISTS:
            s, k, dec, sa, sb = SC.prov(c, h)
            ex = SC.expl_all(True, dec, s_every, sa, sb)
            for v in SC.VREADS[1:]:
                if ex[v] != ex["none"]:
                    tally[(v, h)] = tally.get((v, h), 0) + 1
    for v in SC.VREADS[1:]:
        P("   %s: (candidate, history) pairs whose being an explanation moves: %d (%s)" % (
            v, sum(n for (w, _), n in tally.items() if w == v), ", ".join("%s %d" % (h, tally.get((v, h), 0)) for h in SC.HISTS)))
    names = {}
    for c in accT:
        names[c.name] = names.get(c.name, 0) + 1
    P("   candidates meeting (E), by name: %s" % dict(sorted(names.items())))


def ct8():
    """CT8's five readings, as the script computes Sel and Con under T′, carried to being an explanation."""
    D, pol = CTM.target(CTM.EQ, "D_EQ")
    p, cases = CTM.question(D, pol, "p_EQ")
    cq = CTM.candidate(p, CTM.EQ, CTM.EQ, ["b"])
    acc = account(cq)
    sr = SC.slot_row(cq)
    s_every = bool(sr and sr["every"])
    H = [x for x, _ in cases]
    P("CT8: the chosen pair's transport, Acc %s, slot under 'every' %s" % (acc, s_every))
    reps = {"R1": ([("o_cases", "H"), ("o_score", "surv"), ("o_trees", "t"), ("o_trees", "cod")], True),
            "R2": ([("o_cases", "H"), ("o_score", "surv"), ("o_trees", "t"), ("o_trees", "cod")], False),
            "R3": ([("o_trees", "cod")], True), "R4": ([("o_trees", "cod")], False), "R5": ([], True)}
    for rid, (rep, prep) in reps.items():
        h = Hist(["o_cases", "o_score", "o_trees", "o_channel", "o_switch"], rep, set(H), admitted=True, prepares=prep)
        held_out = bool(faithful(cq))
        selc_out = bool(H) and set(H) <= set(cq.p.C) and faithful_on(cq, H) and h.admitted
        s_t = selc_out and not prep and not any(x in ("t", "H", "surv", "cod") for (_, x) in h.rep)
        k_t = bool(prep) and held_out
        dec = not s_t and not k_t
        ex = SC.expl_all(acc, dec, s_every, s_t or bool(prep), s_t or bool(prep))
        P("   %s (T′): Sel %s, Con %s, Dec %s; Expl (none, V4.1, V4.2, V4.3a, V4.3b) %s" % (rid, s_t, k_t, dec, "".join(SC.tf(ex[v]) for v in SC.VREADS)))


def main():
    P("S108 Part A, section 4: external examples and the creative transport case, being an explanation under each reading")
    P("=" * 150)
    summarize("FC-E1–FC-E5 (s104_external.py)", record(EXT, EXT.main))
    summarize("CT1–CT8 (s104_creative_transport.py)", record(CTM, CTM.main))
    ct8()


if __name__ == "__main__":
    main()
