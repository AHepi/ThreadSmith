# S108 Part A, section 4: the reply's (d) on D18.2 (Argument 8): "V4.1 is safe (a pin at one pair is carried along by φ)".
# FC100's generator and bijections (rename_org, I70) at scale 4 (30 × 4 per size of SMALL, seed 108404): is Slot_C(ℰ) (each
# reading of D6.3's quantifier), and so V4.1's being an explanation, kept by structure-preserving bijections?
#   PYTHONHASHSEED=0 python3 -B s108_s4_bij.py
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from model.core import Question, Candidate, Translation, account, slot, pins, SLOT_QUANTIFIERS  # noqa: E402
from model.gen import rename_org  # noqa: E402
from model.claims_a import SMALL, gen_p_cand  # noqa: E402


def main():
    rng = random.Random(108404)
    n = port = moved = 0
    first = None
    for size in SMALL:
        for i in range(120):
            m = gen_p_cand(rng, size)
            if m is None:
                continue
            p, c = m
            D, E = p.D, c.E
            D2, pm, cm, bm, am = rename_org(D, rng, "'")
            E2, pm2, cm2, bm2, am2 = rename_org(E, rng, "\"")
            q2 = Question(D2, [(am[a], bm[b]) for (a, b) in p.C], bm[p.b0], p.Q, pm[p.deltaD], excl=[(am[a], bm[b]) for (a, b) in p.excl])
            pi2 = {pm2[v]: Translation(tuple(pm[u] for u in c.pi[v].dports), c.pi[v].fn) for v in E.ports}
            lam2 = {cm2[k]: (frozenset(cm[j] for j in N), {pm2[v]: Translation(tuple(pm[u] for u in tr[v].dports), tr[v].fn) for v in E.foot[k]}) for k, (N, tr) in c.lam.items()}
            c2 = Candidate(E2, q2, pi2, {am[a]: am2[x] for a, x in c.tau.items()}, {bm[b]: bm2[x] for b, x in c.sigma.items()}, lam2,
                           [cm2[k] for k in c.Gamma], pm2[c.deltaE])
            n += 1
            if getattr(p.Q, "kind", None) != "port":
                continue
            port += 1
            s1 = tuple(any(slot(c, k, quantifier=q) for k in E.comps) for q in SLOT_QUANTIFIERS)
            s2 = tuple(any(slot(c2, k, quantifier=q) for k in E2.comps) for q in SLOT_QUANTIFIERS)
            if s1 != s2 or len(pins(c)) != len(pins(c2)) or account(c) != account(c2):
                moved += 1
                if first is None:
                    first = (repr(size), i, s1, s2)
    print("models %d; port queries %d; Slot (four readings), pins or Acc not kept by the bijection: %d; first: %s" % (n, port, moved, first))


if __name__ == "__main__":
    main()
