# F3 reading (Mimo's reply): finite exact models of the instances in dispute.
# Components are relations over finite port domains (Fractions); a deleted component imposes
# the full relation (theory line 120); an edit that sets a port replaces the component assigning it.
# E is a copy of D with the identity transport, so (F1), (F2), (A) hold and only the third
# sentence of non-circular dependence (S3) and its repairs are at issue.
from fractions import Fraction as Fr
from itertools import product

DOM = {"H": [Fr(1), Fr(2), Fr(3)], "c": [Fr(1), Fr(2)],          # c = cot(theta): theta = pi/4 gives c = 1 exactly
       "L": [Fr(n) for n in range(0, 7)], "K": [Fr(0), Fr(1)]}
PORTS = list(DOM)

def comp(ports, pred): return (tuple(ports), pred)
def assign(port, key): return comp([port], lambda z, b, p=port, k=key: z[p] == b[k])   # port := boundary value
def setto(port, v):    return comp([port], lambda z, b, p=port, v=v: z[p] == v)        # intervention
LAW  = comp(["L", "H", "c"], lambda z, b: z["L"] == z["H"] * z["c"])                   # L := H cot(theta)
LAW2 = comp(["L", "H", "c"], lambda z, b: z["L"] == z["c"] * z["H"])                   # a relabelled law, same relation
BASE_E = {"aH": assign("H", "UH"), "ac": assign("c", "Uc"), "law": LAW, "aK": assign("K", "UK")}
ASSIGNS = {"H": "aH", "c": "ac", "L": "law", "K": "aK"}
b0 = {"UH": Fr(1), "Uc": Fr(1), "UK": Fr(0)}

# edits: lists of primitive steps ("set", port, v) | ("del", name) | ("repl", name, comp)
def apply(org, edit):
    org = dict(org); touched = set()
    for step in edit:
        if step[0] == "set":
            name = ASSIGNS[step[1]]; org[name] = setto(step[1], step[2]); touched.add(name)
        elif step[0] == "del":
            org.pop(step[1], None); touched.add(step[1])
        elif step[0] == "repl":
            org[step[1]] = step[2]; touched.add(step[1])
    return org, touched

def ans(org, b):
    """Answer profile: the value of the output port L if the solutions fix it; None if not determined."""
    vals = set()
    for vs in product(*(DOM[p] for p in PORTS)):
        z = dict(zip(PORTS, vs))
        if all(pred(z, b) for (_, pred) in org.values()):
            vals.add(z["L"])
    return next(iter(vals)) if len(vals) == 1 else None

def restrict(org, gamma, W):
    """E|W: keep W and the named background (every component outside Gamma, and the boundary values);
    delete Gamma minus W (full relation)."""
    return {k: v for k, v in org.items() if k not in gamma or k in W}

def blocks(gamma):
    g = sorted(gamma)
    for m in range(1, 1 << len(g)):
        yield {g[i] for i in range(len(g)) if m >> i & 1}

BASE = ((), "base")
def s3_as_written(E, gamma, C):
    base = ans(E, b0)
    for edit, name in C:
        org, touched = apply(E, edit)
        if touched & gamma:
            a = ans(org, b0)
            if a != base or a is None:
                return True, name
    return False, None

def option_b(E, gamma, C, reading):
    base = ans(E, b0)
    for edit, name in C:
        a = ans(apply(E, edit)[0], b0)
        contrast = (a != base) or (a is None and base is not None)
        if not contrast: continue
        for G in blocks(gamma):
            R = restrict(E, gamma, gamma - G)
            ra, rb = ans(apply(R, edit)[0], b0), ans(R, b0)
            if reading == "current-strict":      # 'that difference is lost or the answer ceases to be determined', ceases = change from E
                ok = (ra is not None and ra == rb) or (a is not None and ra is None) or (base is not None and rb is None)
            elif reading == "current-loose":     # 'ceases to be determined' read as 'is not determined' in the restriction
                ok = (ra is not None and ra == rb) or ra is None or rb is None
            elif reading == "mimo":              # Mimo point 7: equal, 'or one of these values is not determined'
                ok = (ra == rb) or ra is None or rb is None
            elif reading == "proposed":          # both determined and equal, or an answer E determines at one point is not determined
                ok = (ra is not None and ra == rb) or (a is not None and ra is None) or (base is not None and rb is None)
            if ok: return True, (name, sorted(G))
    return False, None

def report(title, E, gamma, C):
    print(f"\n== {title}\n   Gamma = {sorted(gamma)}; C = {[n for _, n in C]}")
    print(f"   answers: " + ", ".join(f"{n}->{ans(apply(E, e)[0], b0)}" for e, n in C))
    print(f"   S3 as written          : {s3_as_written(E, gamma, C)}")
    for r in ["current-strict", "current-loose", "mimo", "proposed"]:
        print(f"   option B [{r:14}]: {option_b(E, gamma, C, r)}")

E = BASE_E
Cprod = [BASE, ((("set", "H", Fr(2)),), "set H=2"), ((("set", "H", Fr(3)),), "set H=3"), ((("set", "c", Fr(2)),), "set c=2")]
report("1a production, R-tau-mech (Gamma = the law only), production contract", E, {"law"}, Cprod)
report("1b production, R-tau-in (input-assigning components in Gamma)", E, {"aH", "ac", "law"}, Cprod)
report("2  production contract that also admits an intervention on L", E, {"law"}, Cprod + [((("set", "L", Fr(5)),), "set L=5")])
Cleak = [BASE, ((("set", "H", Fr(2)),), "set H=2"), ((("del", "law"),), "delete law")]
report("3  idle Gamma, contract with a law-deleting edit (line 50): leak test", E, {"aK"}, Cleak)
Ccomp = [BASE, ((("set", "H", Fr(2)),), "set H=2"), ((("del", "aK"), ("set", "H", Fr(2))), "del aK o set H=2")]
report("4  idle Gamma, composite edit (line 108): Mimo's 'not sufficient' instance", E, {"aK"}, Ccomp)
Crel = [BASE, ((("repl", "law", LAW2),), "relabel law")]
report("5  relabelings only (line 272)", E, {"law"}, Crel)

# O33: joint turns only. Ports k1,k2 (knobs), T (compartment reading); T := 10 - 2 k1 - k2 (a stand-in mechanism).
DOM.clear(); DOM.update({"k1": [Fr(i) for i in range(3)], "k2": [Fr(i) for i in range(3)], "L": [Fr(i) for i in range(0, 11)]})
PORTS[:] = list(DOM)
ASSIGNS.clear(); ASSIGNS.update({"k1": "a1", "k2": "a2", "L": "mech"})
b0.clear(); b0.update({"U1": Fr(0), "U2": Fr(0)})
EO = {"a1": assign("k1", "U1"), "a2": assign("k2", "U2"), "mech": comp(["L", "k1", "k2"], lambda z, b: z["L"] == 10 - 2 * z["k1"] - z["k2"])}
Cj = [BASE] + [((("set", "k1", Fr(v)), ("set", "k2", Fr(v))), f"joint {v}") for v in (1, 2)]
report("6a O33 joint turns only, R-tau-mech", EO, {"mech"}, Cj)
report("6b O33 joint turns only, R-tau-in", EO, {"a1", "a2", "mech"}, Cj)

# Skew-symmetric case (line 356), exact: Leibniz determinant over Fractions.
from itertools import permutations
import random
def det(M):
    n = len(M); tot = Fr(0)
    for perm in permutations(range(n)):
        sgn = 1
        for i in range(n):
            for j in range(i + 1, n):
                if perm[i] > perm[j]: sgn = -sgn
        prod = Fr(1)
        for i in range(n): prod *= M[i][perm[i]]
        tot += sgn * prod
    return tot
def rskew(n, rng):
    M = [[Fr(0)] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            v = Fr(rng.randint(-9, 9), rng.randint(1, 9)); M[i][j] = v; M[j][i] = -v
    return M
rng = random.Random(88)
print("\n== 7 skew-symmetric case (line 356)")
for n in (3, 5):
    ds = {det(rskew(n, rng)) for _ in range(200)}
    print(f"   200 random rational {n}x{n} skew-symmetric matrices: determinants = {sorted(ds)}")
I3 = [[Fr(int(i == j)) for j in range(3)] for i in range(3)]
print(f"   det I_3 = {det(I3)}  (removal of skewness: the family now holds an invertible matrix)")
print(f"   det [[0,1],[-1,0]] = {det([[Fr(0), Fr(1)], [Fr(-1), Fr(0)]])}  (removal of oddness: likewise)")

# O5 on its narrowed contract (rooms warmer than 20 degrees). Ports: Y (yeast present, 0/1), T (room
# temperature, 21 or 25), g (gas rate), L (answer: 1 if the dough doubles in two hours, else 0).
# Mechanism: g := Y * (2 if T > 20 else 1)  (the yeast makes the gas, slowly in the cold); L := 1 if g >= 2.
DOM.clear(); DOM.update({"Y": [Fr(0), Fr(1)], "T": [Fr(21), Fr(25)], "g": [Fr(0), Fr(1), Fr(2)], "L": [Fr(0), Fr(1)]})
PORTS[:] = list(DOM)
ASSIGNS.clear(); ASSIGNS.update({"Y": "aY", "T": "aT", "g": "gas", "L": "rise"})
b0.clear(); b0.update({"UY": Fr(1), "UT": Fr(21)})
E5 = {"aY": assign("Y", "UY"), "aT": assign("T", "UT"),
      "gas": comp(["g", "Y", "T"], lambda z, b: z["g"] == z["Y"] * (2 if z["T"] > 20 else 1)),
      "rise": comp(["L", "g"], lambda z, b: z["L"] == (1 if z["g"] >= 2 else 0))}
C5in = [BASE, ((("set", "T", Fr(25)),), "set T=25"), ((("set", "Y", Fr(0)),), "yeast out as input setting")]
report("8a O5, yeast out formalized as an input setting, R-tau-mech", E5, {"gas", "rise"}, C5in)
C5del = [BASE, ((("set", "T", Fr(25)),), "set T=25"), ((("del", "gas"),), "yeast out as deleting the gas component")]
report("8b O5, yeast out formalized as deleting the gas component, R-tau-mech", E5, {"gas", "rise"}, C5del)
