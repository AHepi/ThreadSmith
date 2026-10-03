# S104 round 2 (maths): the text's worked constructions (formal core §17, E1-E9), encoded.
# Each encoding is an invention of the formal core (I65-I69) and, where this program had to fix more,
# of this program (I92, I99, I100); the tags say which.
import itertools
from fractions import Fraction as Fr

from .core import (ONE, Org, Question, PortQuery, FnQuery, Candidate, Translation, BOT)


# ---- exact arithmetic in Q(√3) for the pole [I92] ------------------------------------------------

class Q3:
    """r + s·√3 with rational r, s: exact values of H·cot θ for θ in {30°, 45°, 60°} [I92]."""
    __slots__ = ("r", "s")

    def __init__(self, r, s=0):
        self.r, self.s = Fr(r), Fr(s)

    def __mul__(self, o):
        o = o if isinstance(o, Q3) else Q3(o)
        return Q3(self.r * o.r + 3 * self.s * o.s, self.r * o.s + self.s * o.r)

    __rmul__ = __mul__

    def __eq__(self, o):
        if not isinstance(o, (Q3, int, Fr)):
            return False
        o = o if isinstance(o, Q3) else Q3(o)
        return self.r == o.r and self.s == o.s

    def __hash__(self):
        return hash((self.r, self.s))

    def __lt__(self, o):
        return float(self) < float(o)

    def __float__(self):
        return float(self.r) + float(self.s) * 3 ** 0.5

    def __repr__(self):
        if self.s == 0:
            return str(self.r)
        if self.r == 0:
            return ("%s√3" % ("" if self.s == 1 else self.s))
        return "%s+%s√3" % (self.r, self.s)


COT = {30: Q3(0, 1), 45: Q3(1, 0), 60: Q3(0, Fr(1, 3))}
TAN = {30: Q3(0, Fr(1, 3)), 45: Q3(1, 0), 60: Q3(0, 1)}


# ---- E1 the pole and its shadow (I65, I93) --------------------------------------------------------

def surgical_edits(ports_vals):
    """All partial assignments over the given ports (override composition): the closure of the single
    settings under composition (I65: 'and their composites'; a total monoid, I01)."""
    keys = []
    names = sorted(ports_vals)
    for combo in itertools.product(*[[None] + list(ports_vals[v]) for v in names]):
        keys.append(tuple((v, x) for v, x in zip(names, combo) if x is not None))
    keys.sort(key=lambda k: (len(k), repr(k)))

    def label(k):
        return ONE if not k else "set(" + ",".join("%s=%s" % kv for kv in k) + ")"

    lab = {k: label(k) for k in keys}
    inv = {v: k for k, v in lab.items()}

    def compose(a2, a1):
        d = dict(inv[a1])
        d.update(dict(inv[a2]))
        return lab[tuple(sorted(d.items()))]

    return [lab[k] for k in keys], inv, compose


def pole(H_vals=(1, 2, 3), T_vals=(30, 45, 60), bounds=None, settable=("H", "T", "L")):
    """D_pole (E1): ports H, T (θ), L; boundaries b = (u_H, u_θ); components c_H (H = u_H), c_T (θ = u_θ),
    c_L (L = H cot θ); edits: settings of the settable ports and their composites (I04, I65)."""
    L_vals = sorted(set(h * COT[t] for h in H_vals for t in T_vals), key=float)
    dom = {"H": tuple(H_vals), "T": tuple(T_vals), "L": tuple(L_vals)}
    bounds = bounds or [(h, t) for h in H_vals for t in T_vals]
    B = ["b%s_%s" % bt for bt in bounds]
    bval = {("b%s_%s" % bt): bt for bt in bounds}
    A, inv, compose = surgical_edits({v: dom[v] for v in settable})
    home = {"c_H": "H", "c_T": "T", "c_L": "L"}
    foot = {"c_H": ("H",), "c_T": ("T",), "c_L": ("H", "T", "L")}
    fullL = frozenset((h, t, l) for h in H_vals for t in T_vals for l in L_vals)

    def Lfun(j, a, b):
        sm = dict(inv[a])
        v = home[j]
        if v in sm:
            i = foot[j].index(v)
            return frozenset(w for w in itertools.product(*[dom[u] for u in foot[j]]) if w[i] == sm[v])
        uH, uT = bval[b]
        if j == "c_H":
            return frozenset([(uH,)])
        if j == "c_T":
            return frozenset([(uT,)])
        return frozenset(w for w in fullL if w[2] == w[0] * COT[w[1]])

    D = Org("D_pole", ["H", "T", "L"], dom, ["c_H", "c_T", "c_L"], foot, B, A, compose, Lfun, meta=dict(bval=bval, inv=inv))
    return D


def pole_rev(D):
    """E_rev (E1, FC27, FC28): c'_L: L = the observed value u_H·cot u_θ (from the boundary); c'_T: θ = u_θ;
    c'_H: H = L tan θ. Same edit labels, each setting replacing E_rev's own assigning component (I04)."""
    dom = dict(D.dom)
    inv = D.meta["inv"]
    bval = D.meta["bval"]
    home = {"r_L": "L", "r_T": "T", "r_H": "H"}
    foot = {"r_L": ("L",), "r_T": ("T",), "r_H": ("H", "T", "L")}

    def Lfun(j, a, b):
        sm = dict(inv[a])
        v = home[j]
        if v in sm:
            i = foot[j].index(v)
            return frozenset(w for w in itertools.product(*[dom[u] for u in foot[j]]) if w[i] == sm[v])
        uH, uT = bval[b]
        if j == "r_L":
            return frozenset([(uH * COT[uT],)])
        if j == "r_T":
            return frozenset([(uT,)])
        return frozenset(w for w in itertools.product(dom["H"], dom["T"], dom["L"]) if w[2] * TAN[w[1]] == w[0])

    return Org("E_rev", ["H", "T", "L"], dom, ["r_L", "r_T", "r_H"], foot, D.B, D.A, D._compose, Lfun, meta=dict(bval=bval, inv=inv))


def ident_pi(ports):
    return {v: Translation((v,)) for v in ports}


def pole_fwd_candidate(p, name="ℰ_fwd", tau=None):
    D = p.D
    lam = {j: (frozenset([j]), {v: Translation((v,)) for v in D.foot[j]}) for j in D.comps}
    return Candidate(D, p, ident_pi(D.ports), tau or {a: a for a in D.A}, {b: b for b in D.B}, lam, list(D.comps), "L", name=name)


def pole_rev_candidate(p, name="ℰ_rev", delta="L"):
    D = p.D
    E = pole_rev(D)
    lam = {"r_L": (frozenset(D.comps), {"L": Translation(("L",))}),
           "r_T": (frozenset(["c_T"]), {"T": Translation(("T",))}),
           "r_H": (frozenset(["c_L"]), {v: Translation((v,)) for v in ("H", "T", "L")})}
    return Candidate(E, p, ident_pi(D.ports), {a: a for a in D.A}, {b: b for b in D.B}, lam, list(E.comps), delta, name=name)


def single_settings(D, ports):
    inv = D.meta["inv"]
    return [a for a in D.A if len(inv[a]) == 1 and inv[a][0][0] in ports]


def fibre_query():
    """I65's identification query: the fibre {H : H cot θ = observed L}, computed from the single value
    of (θ, L) in Sol, ⊥ when that is not single [I92]."""
    def fn(org, a, b, delta):
        iT, iL = org.ports.index("T"), org.ports.index("L")
        vals = set((z[iT], z[iL]) for z in org.sol(a, b))
        if len(vals) != 1:
            return BOT
        t, l = next(iter(vals))
        return frozenset(h for h in org.dom["H"] if h * COT[t] == l)
    return FnQuery(fn, "Q_fib (the fibre {H : H cot θ = observed L})")


# ---- E2/E3 identification (I63, I64) ---------------------------------------------------------------

def identified(Z, g, f, y):
    Zy = [z for z in Z if g(z) == y]
    return bool(Zy) and len(set(f(z) for z in Zy)) == 1


# ---- linear algebra over Q (for I3) -----------------------------------------------------------------

def rank(M):
    M = [[Fr(x) for x in row] for row in M]
    r = 0
    rows, cols = len(M), (len(M[0]) if M else 0)
    for c in range(cols):
        piv = None
        for i in range(r, rows):
            if M[i][c] != 0:
                piv = i
                break
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        for i in range(rows):
            if i != r and M[i][c] != 0:
                f = M[i][c] / M[r][c]
                M[i] = [M[i][k] - f * M[r][k] for k in range(cols)]
        r += 1
    return r


def det(M, p=None):
    n = len(M)
    tot = 0
    for perm in itertools.permutations(range(n)):
        sgn = 1
        for i in range(n):
            for j in range(i + 1, n):
                if perm[i] > perm[j]:
                    sgn = -sgn
        prod = 1
        for i in range(n):
            prod *= M[i][perm[i]]
        tot += sgn * prod
    return tot % p if p else tot
