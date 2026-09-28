# S108 Part A, section 2 (the computing agent): the edges the reply names on routes (S), critical blocks (B), work
# (L313), problems (D10) and identification contracts, computed on the generated worlds at scale 4 (gen_p_cand over
# SMALL, 40 × scale per size, seed as s108_s2_gen.py's 'single', so the same candidates) and on the pairs population.
#   (a) V2.1: of the candidates that newly meet (E), how many have every commitment doing no work (NoWork, D7.6, L313),
#       with S computed under V2.1 and under off
#   (b) V2.1: candidates with ∅ ∈ S (a route with no commitments), off and on
#   (c) L299.s1: a block critical in a route while no singleton in it is, off and under each of V2.1-V2.4
#   (d) L307: S = {{a},{b},{a,b}} (two redundant routes) off; what S becomes under V2.2
#   (e) generated candidates on a contract {1} × B' (every pair's edit the identity): Acc off and under V2.3
#   (f) pairs population: conflict pairs, rivals and kind under V2.1-V2.4 (which read NC2 or NC1, not Conf)
#   (g) routes W ∈ S with no critical block, and with no critical singleton, off and under V2.1-V2.4
# Run from "results/S108 Part A - computation/section 2 model":  PYTHONHASHSEED=0 python3 -B s108_s2_routes.py
import random
import sys
import os

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from model import core  # noqa: E402
from model.core import ONE, account, routes, critical_block, no_work, conflict_pairs, problem_kind, rivals  # noqa: E402
from model.claims_a import SMALL, gen_p_cand  # noqa: E402
from model.claims_b import CONF, gen_pair  # noqa: E402

V = ("off", "V2.1", "V2.2", "V2.3", "V2.4")


def wv(v, fn, *a):
    old = core.S2_VARIANT
    core.S2_VARIANT = v
    try:
        return fn(*a)
    finally:
        core.S2_VARIANT = old


def blocks_critical_no_singleton(S, Gamma):
    out = []
    for W in S:
        Wl = sorted(W)
        for r in range(2, len(Wl) + 1):
            import itertools
            for B in itertools.combinations(Wl, r):
                B = frozenset(B)
                if critical_block(S, B, W) and not any(critical_block(S, frozenset([d]), W) for d in B):
                    out.append((W, B))
    return out


def fmt_S(S):
    return "{" + ", ".join("{" + ",".join(sorted(W)) + "}" for W in sorted(S, key=lambda W: (len(W), sorted(W)))) + "}"


def main(scale=4.0):
    P = print
    rng = random.Random(1082100)  # the seed of s108_s2_gen.py's population 'single': the same candidates
    per = int(40 * scale)
    n = 0
    a_new = a_allnowork_on = a_allnowork_off = 0
    a_wit = None
    empty_route = {v: 0 for v in V}
    empty_wit = None
    l299 = {v: 0 for v in V}
    l299_wit = {v: None for v in V}
    l307 = {v: 0 for v in V}
    l307_under = {}
    ident = {v: [0, 0] for v in V}
    nroutes = {v: 0 for v in V}
    no_cb = {v: 0 for v in V}
    no_cs = {v: 0 for v in V}
    no_cb_wit = {v: None for v in V}
    for size in SMALL:
        for i in range(per):
            m = gen_p_cand(rng, size)
            if m is None:
                continue
            p, c = m
            n += 1
            acc = {v: bool(wv(v, account, c)) for v in V}
            S = {v: wv(v, routes, c) for v in V}
            G = frozenset(c.Gamma)
            for v in V:
                for W in S[v]:
                    nroutes[v] += 1
                    import itertools as _it
                    blocks = [frozenset(B) for r in range(1, len(W) + 1) for B in _it.combinations(sorted(W), r)]
                    if not any(critical_block(S[v], B, W) for B in blocks):
                        no_cb[v] += 1
                        if no_cb_wit[v] is None:
                            no_cb_wit[v] = (repr(size), fmt_S(S[v]), sorted(W))
                    if not any(critical_block(S[v], frozenset([d]), W) for d in W):
                        no_cs[v] += 1
                if frozenset() in S[v]:
                    empty_route[v] += 1
                    if v == "V2.1" and empty_wit is None and frozenset() not in S["off"]:
                        empty_wit = (repr(size), p.describe(), c.describe(), fmt_S(S["off"]), fmt_S(S[v]))
                bc = blocks_critical_no_singleton(S[v], c.Gamma)
                if bc:
                    l299[v] += 1
                    if l299_wit[v] is None:
                        l299_wit[v] = (repr(size), fmt_S(S[v]), [(sorted(W), sorted(B)) for W, B in bc[:2]], c.describe())
                if len(G) == 2 and S[v] == frozenset([frozenset([d]) for d in G] + [G]):
                    l307[v] += 1
                    if v == "off":
                        l307_under.setdefault(fmt_S(S["V2.2"]).replace(sorted(G)[0], "a").replace(sorted(G)[1], "b"), 0)
                        l307_under[fmt_S(S["V2.2"]).replace(sorted(G)[0], "a").replace(sorted(G)[1], "b")] += 1
            if acc["V2.1"] and not acc["off"]:
                a_new += 1
                nw_on = all(no_work(S["V2.1"], d) for d in c.Gamma)
                nw_off = all(no_work(S["off"], d) for d in c.Gamma)
                a_allnowork_on += nw_on
                a_allnowork_off += nw_off
                if a_wit is None and not nw_on:
                    a_wit = (repr(size), fmt_S(S["off"]), fmt_S(S["V2.1"]), [(d, no_work(S["V2.1"], d)) for d in c.Gamma], c.describe())
            if all(a == ONE for (a, b) in p.C) and len(p.C) > 1:
                for v in V:
                    ident[v][0] += 1
                    ident[v][1] += acc[v]
    P("population: %d candidates (gen_p_cand, SMALL, %d per size, seed 1082100)" % (n, per))
    P("(a) V2.1: candidates newly meeting (E): %d; every commitment doing no work (NoWork, D7.6) with S under V2.1: %d; with S off: %d"
      % (a_new, a_allnowork_on, a_allnowork_off))
    if a_wit:
        P("    first newly meeting candidate with a commitment that does work (size %s): S off %s; S under V2.1 %s; NoWork %s\n%s" % a_wit)
    P("(b) candidates with ∅ ∈ S (a route with no commitments): %s" % empty_route)
    if empty_wit:
        P("    first under V2.1 (size %s):\n%s\n%s\n    S off %s; S under V2.1 %s" % empty_wit)
    P("(c) L299.s1, a block critical in a route while no singleton in it is: candidates %s" % l299)
    for v in V:
        if l299_wit[v]:
            P("    %s first (size %s): S %s; (route, block) %s" % ((v,) + l299_wit[v][:3]))
    P("(d) L307, S = {{a},{b},{a,b}}: candidates %s; under V2.2 those of 'off' have S = %s" % (l307, l307_under))
    P("(e) contracts {1} × B' with more than one pair: [candidates, meeting (E)] %s" % ident)
    P("(g) routes (W ∈ S, over every candidate): %s; with no critical block: %s; with no critical singleton: %s" % (nroutes, no_cb, no_cs))
    for v in V:
        if no_cb_wit[v]:
            P("    %s first route with no critical block (size %s): S %s; W %s" % ((v,) + no_cb_wit[v]))
    # (f) pairs
    rng = random.Random(1082200)
    per = int(20 * scale)
    npairs = 0
    moved = {v: 0 for v in V[1:]}
    for size in CONF:
        for i in range(per):
            m = gen_pair(rng, size)
            if m is None:
                continue
            p, c1, c2 = m
            npairs += 1
            r0 = (tuple(conflict_pairs(c1, c2)), problem_kind(c1, c2), bool(rivals(c1, c2)))
            for v in V[1:]:
                r1 = (tuple(wv(v, conflict_pairs, c1, c2)), wv(v, problem_kind, c1, c2), bool(wv(v, rivals, c1, c2)))
                moved[v] += r0 != r1
    P("(f) pairs population (gen_pair, CONF, %d per size, seed 1082200): %d pairs; pairs whose conflict pairs, rivals or kind differ from off: %s"
      % (per, npairs, moved))


if __name__ == "__main__":
    main(float(sys.argv[sys.argv.index("--scale") + 1]) if "--scale" in sys.argv else 4.0)
