# S108 Part A round 2, section 4 (rule 5.4; after S56 one Opus agent computes every section): the round-2 variants of
# section 4 on generated worlds at scale 4, on round 1's own stream (s108_s4_worlds.gen_world, seed 108401, 160 per size of
# claims_a.SMALL; MID with seed 108405), so every count is comparable with round 1's section 4.
#   PYTHONHASHSEED=0 python3 -B s108r2_s4_worlds.py SMALL|MID OUT.json
# R2V4.1  being an explanation := Acc ∧ ¬Dec ∧ ¬Slot_q, each quantifier q of D6.3, round 1's hand-set histories (SC.HISTS);
#         (Suff) as conjectured (its antecedent ⇒ Expl) failing with the antecedent kept (Acc ∧ ¬Dec) / co-varied.
# R2V4.4  histories built as chains (S108r2-4-I1): o1 a selection on (1, b0) where (1, b0) ∈ C and t is faithful there, else
#         declared; o2 a relay of o1; cut T′: Account ∧ ¬Dec at o2 now, and under round 1's V4.3 (a) at the holding.
# R2V4.8  cut U admitted (L526.s18 deleted): the number of fixed points per (candidate, history) under U against T′.
# R2V4.5 (E9 only), R2V4.6 (no code), R2V4.7 (arguments only) read nothing here: said in the results file.
# Standard library only; imports the package model/ of this folder; writes only OUT.json.
import json
import os
import random
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from model.core import ONE, account, faithful, SLOT_QUANTIFIERS  # noqa: E402
from model.claims_a import SMALL, MID  # noqa: E402
from model.claims_b import prov_fixed_points, _prov_step, faithful_on  # noqa: E402
import s108_s4_cases as SC  # noqa: E402
from s108_s4_worlds import gen_world, size_d  # noqa: E402


def main():
    which, outp = sys.argv[1], sys.argv[2]
    sizes, seed = (SMALL, 108401) if which == "SMALL" else (MID, 108405)
    rng = random.Random(seed)
    t0 = time.time()
    n = accT = 0
    v41 = {q: {"drop": 0, "cands": 0, "suff_fail_kept": 0, "suff_fail_cov": 0, "first": None} for q in SLOT_QUANTIFIERS}
    v44 = {"acc": 0, "trial": 0, "expl_chain": 0, "v43a_chain": 0, "first_no_trial": None}
    v48 = {"T'": {}, "U": {}}
    for size in sizes:
        for i in range(160):
            fam, kind, p, c = gen_world(rng, size)
            n += 1
            acc = account(c)
            if not acc:
                continue
            accT += 1
            wit = dict(size=size_d(size), index=i, family=fam, kind=kind)
            sr = SC.slot_row(c)
            decs = {h: SC.prov(c, h)[2] for h in SC.HISTS}
            for q in SLOT_QUANTIFIERS:
                s = bool(sr and sr[q])
                moved = False
                for h, dec in decs.items():
                    now = bool(not dec)
                    v = bool(not dec and not s)
                    if now != v:
                        v41[q]["drop"] += 1
                        moved = True
                        v41[q]["suff_fail_kept"] += 1          # antecedent Acc ∧ ¬Dec holds, Expl fails
                    # co-varied: antecedent Acc ∧ ¬Dec ∧ ¬Slot ⇒ Expl, never fails by construction; counted to show it
                    if (not dec and not s) and not v:
                        v41[q]["suff_fail_cov"] += 1
                if moved:
                    v41[q]["cands"] += 1
                    if v41[q]["first"] is None:
                        v41[q]["first"] = wit
            # R2V4.4
            v44["acc"] += 1
            H = [(ONE, p.b0)]
            trial = bool((ONE, p.b0) in p.C and faithful_on(c, H))
            v44["trial"] += trial
            if not trial and v44["first_no_trial"] is None:
                v44["first_no_trial"] = wit
            held = int(bool(faithful(c)))
            fps = prov_fixed_points(2, [held, held], [0, 0], [int(trial), 0], "T'", True, rec_of=[None, 0])
            R, sc = fps[0]
            dec = not sc[1][0] and not sc[1][1]
            direct = _prov_step(2, [held, held], [0, 0], [int(trial), 0], "T'", True, R)
            v44["expl_chain"] += (not dec)
            v44["v43a_chain"] += bool(not dec and direct[1][0])
            # R2V4.8
            selc = int(trial)
            for hname, (hv, tr, sc_, rec) in {"Con": ([held, held], [0, 1], [0, 0], [None, None]),
                                              "Sel": ([held], [0], [selc], [None]),
                                              "rCon": ([held, held], [1, 0], [0, 0], [None, 0]),
                                              "rSel": ([held, held], [0, 0], [selc, 0], [None, 0])}.items():
                for rd in ("T'", "U"):
                    k = len(prov_fixed_points(len(hv), hv, tr, sc_, rd, True, rec_of=rec))
                    d = v48[rd].setdefault(hname, {})
                    d[str(k)] = d.get(str(k), 0) + 1
    res = dict(which=which, seed=seed, models=n, acc_true=accT, seconds=round(time.time() - t0, 1), R2V4_1=v41, R2V4_4=v44, R2V4_8=v48)
    with open(outp, "w", encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False, indent=1, default=repr)
    print(json.dumps(res, ensure_ascii=False, default=repr))


if __name__ == "__main__":
    main()
