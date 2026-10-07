# Derivation 10 replacement: does "exchanging the two persistence components' anchors" give a faithful transport?
# Minimal exact model. P: two things with positions x1, x2 over a finite domain; continuity components
# c1: x1 = u1, c2: x2 = u2 (boundary values u1, u2). Admitted edits: identity, displace thing i to v
# (replaces c_i by x_i = v), swap the two identities (replaces c1, c2 by x1 = u2, x2 = u1).
# S1: persistence components k1: y1 = w1, k2: y2 = w2 over the same domain.
from itertools import product
DOM = [0, 1, 2, 3]
B0 = {"u1": 0, "u2": 3}
EDITS = [("id",)] + [("disp", i, v) for i in (1, 2) for v in DOM] + [("swap",)]

def comps_P(e, b):
    c = {1: ("x1", b["u1"]), 2: ("x2", b["u2"])}
    if e[0] == "disp": c[e[1]] = (f"x{e[1]}", e[2])
    if e[0] == "swap": c = {1: ("x1", b["u2"]), 2: ("x2", b["u1"])}
    return c                                    # component i fixes port to value
def comps_S(e, b):                              # S1 is a copy of P with y-ports and w-boundaries
    c = {1: ("y1", b["w1"]), 2: ("y2", b["w2"])}
    if e[0] == "disp": c[e[1]] = (f"y{e[1]}", e[2])
    if e[0] == "swap": c = {1: ("y1", b["w2"]), 2: ("y2", b["w1"])}
    return c
def sol_one(comp): return {comp[1]}             # relation of one component on its single port
def sol_all(cs, ports):
    return {tuple(dict(c for c in cs.values())[p] for p in ports)}

def check(name, lam, tau, sig, pi):
    ok1 = ok2 = True
    for e in EDITS:
        b = B0
        cP, cS = comps_P(e, b), comps_S(tau(e), sig(b))
        for k in (1, 2):                        # (F1): anchor lam[k] of S1-component k, translated
            if sol_one(cP[lam[k]]) != sol_one(cS[k]): ok1 = False
        solD = sol_all(cP, ["x1", "x2"]); solE = sol_all(cS, ["y1", "y2"])
        if {pi(z) for z in solD} != solE: ok2 = False
    print(f"  {name}: (F1) {ok1}  (F2) {ok2}")

ident = lambda e: e
swap_e = lambda e: ("disp", 3 - e[1], e[2]) if e[0] == "disp" else e
sig_id = lambda b: {"w1": b["u1"], "w2": b["u2"]}
sig_sw = lambda b: {"w1": b["u2"], "w2": b["u1"]}
print("t1 (identity):"); check("t1", {1: 1, 2: 2}, ident, sig_id, lambda z: z)
print("anchors exchanged only (lambda swapped; pi, tau, sigma kept):")
check("t1 with lambda exchanged", {1: 2, 2: 1}, ident, sig_id, lambda z: z)
print("the two things exchanged throughout t1 (pi, tau, sigma and lambda):")
check("t1 composed with the exchange", {1: 2, 2: 1}, swap_e, sig_sw, lambda z: (z[1], z[0]))
