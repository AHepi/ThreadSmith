# S104 round 2 (maths): finite toys for Parts IV and IX-XII (formal core §§11-15).
# The physical module Θ is not computed here: where the formal core reads something through Θ, the
# model supplies it as a finite relation set by hand ("free predicates", I90). Every tag names an
# invention in `inventions register.md`.
import itertools


# ---- (CT1)-(CT2) on a finite state set [I97] -----------------------------------------------------

def F_op(Z, dom_T, T, execs, X, with_output=True):
    """F(X) (D15.3, I61): states whose executions all complete (with o ∈ T[i] when with_output) and end
    in X. execs[(z, i)] is a list of (complete, o, z2)."""
    out = set()
    for z in Z:
        ok = True
        for i in dom_T:
            for (c, o, z2) in execs[(z, i)]:
                if not c or (with_output and o not in T[i]) or z2 not in X:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            out.add(z)
    return frozenset(out)


def ret_real(C, dom_T, T, execs):
    """(CT1) (D15.2)."""
    return all(c and o in T[i] and z2 in C for z in C for i in dom_T for (c, o, z2) in execs[(z, i)])


def gfp(Z, f):
    X = frozenset(Z)
    while True:
        Y = f(X)
        if Y == X:
            return X
        X = Y


# ---- active routes in a toy history [I95] ----------------------------------------------------------

class Circuit:
    """A history as a finite DAG of occurrences (D11.3): node -> (parents, function of the parents'
    values); inputs have no parents and a value. Precedence ≺ is reachability; the instantiated
    connections are the edges; Org_ℓ(h) is the circuit itself [I95]."""

    def __init__(self, nodes, inputs):
        self.nodes = dict(nodes)  # name -> (parents tuple, fn)
        self.inputs = dict(inputs)  # name -> value
        self.order = self._topo()

    def _topo(self):
        seen, out = set(), []

        def visit(n):
            if n in seen:
                return
            seen.add(n)
            for p in self.nodes.get(n, ((), None))[0]:
                visit(p)
            out.append(n)

        for n in list(self.inputs) + list(self.nodes):
            visit(n)
        return out

    def values(self, set_=None):
        v = {}
        for n in self.order:
            if set_ and n in set_:
                v[n] = set_[n]
            elif n in self.inputs:
                v[n] = self.inputs[n]
            else:
                ps, fn = self.nodes[n]
                v[n] = fn(*[v[p] for p in ps])
        return v

    def edges(self):
        return {(p, n) for n, (ps, _) in self.nodes.items() for p in ps}

    def prec(self, x, y):
        """x ≺ y: a directed path from x to y."""
        E = self.edges()
        front, seen = [x], set()
        while front:
            n = front.pop()
            for (p, q) in E:
                if p == n and q not in seen:
                    if q == y:
                        return True
                    seen.add(q)
                    front.append(q)
        return False


def act_route(h, R, i, r, K):
    """ActRoute_h(R; i, r, K) (D11.4, I46): R connected by edges inside R (weakly); i, r ∈ R; every
    member of R on a ≺-chain from i to r inside R; the members meet their relations (true of the
    actual values); some (x, x') ∈ K set at i gives different values at r."""
    R = set(R)
    if i not in R or r not in R:
        return False, "i or r not in R"
    E = {(p, q) for (p, q) in h.edges() if p in R and q in R}
    # weak connectivity
    comp, front = {i}, [i]
    while front:
        n = front.pop()
        for (p, q) in E:
            for a, b in ((p, q), (q, p)):
                if a == n and b not in comp:
                    comp.add(b)
                    front.append(b)
    if comp != R:
        return False, "not connected"

    def reach(src, dst):
        front, seen = [src], {src}
        while front:
            n = front.pop()
            if n == dst:
                return True
            for (p, q) in E:
                if p == n and q not in seen:
                    seen.add(q)
                    front.append(q)
        return False

    for n in R:
        if not (reach(i, n) and reach(n, r)):
            return False, "%s is on no chain from i to r inside R" % n
    for (x, x2) in K:
        if h.values({i: x})[r] != h.values({i: x2})[r]:
            return True, "dependence on the contrast (%s, %s)" % (x, x2)
    return False, "no dependence on the declared contrasts"


# ---- repair aims on discrete time [I96] -------------------------------------------------------------

def o_at(cond, xi):
    return cond[xi]


def r_left(cond, occ, xi):
    """r(ξ) on the left of (P) (D14.1, I57)."""
    return cond[xi] if xi in occ else True


def r_right(cond, occ, xi, xi2):
    """r(ξ') on the right of (P): met at every covered occasion in [ξ, ξ'] (D14.1, I57)."""
    return all(cond[w] for w in occ if xi <= w <= xi2)


def repair(O, P, xi, xi2, produced_by):
    """(P) (D14.2) with ProducedBy supplied as a truth value (read through an active route, I90)."""
    return any(not o_at(c, xi) and o_at(c, xi2) for c in O) and \
        all((not r_left(c, occ, xi)) or r_right(c, occ, xi, xi2) for (c, occ) in P) and produced_by
