#!/usr/bin/env python3
"""fe.py - a finite implementation of draft 3's Account (E), with Part II's solution semantics.

Unlike ratchet/models (which read Account as (A) alone, at single pairs), this module keeps the
organization, the transport and three more conjuncts of (E):

  Organization   ports (name -> domain) and components (name -> (footprint, relation)).
                 Sol(x) = valuations satisfying every component (O); the input ports W, Wi, V, Sun
                 are set by the edit of the pair x. A DELETED component imposes the full relation
                 on its ports (Part II), so a port it assigned becomes free.
  Query          Ans(x) = the set of values of port 'first' across Sol(x) (which bed ripens first).
  (A)            Ans_E(x) = Ans_D(x) at every pair of the contract.
  (F2)           pi[Sol_D(x)] = Sol_E(x) at every pair (pi is the candidate's transport map).
  (F1)           for every active component k: the projection of Sol of its anchor subnetwork of D
                 (other D components deleted) onto k's footprint, through the port translation,
                 equals k's relation with the inputs the pair sets.
  NonCircular    draft 3 D3:L255: some pair x of C and nonempty block G of Gamma such that the answer
                 at x differs from the answer at the baseline B0, and the contrast is lost when G is
                 deleted (determined and equal, or a determined answer becomes undetermined).
  NonVacuous     Sol_D(B0) nonempty; contracts are declared with a stated scope (taken as met).

A job is a question (the proposal's edit (a)): here, a contract (a list of pairs) holding the baseline.
Standard library only.
"""
from itertools import product, combinations

INPUTS = ('W', 'Wi', 'V', 'Sun')
DOM_IN = {'W': ('dry', 'wet'), 'Wi': ('calm', 'windy'), 'V': ('late', 'early'), 'Sun': ('S', 'N')}
SETTINGS = [dict(zip(INPUTS, t)) for t in product(*(DOM_IN[k] for k in INPUTS))]
WORDS = {'S': 'sunS', 'N': 'shadeS'}


def show(x):
    return '/'.join(WORDS.get(x[k], x[k]) for k in INPUTS)


def S(W, Wi, V, Sun):
    return {'W': W, 'Wi': Wi, 'V': V, 'Sun': Sun}


B0 = S('dry', 'calm', 'late', 'S')        # the recorded summers (all alike) - the baseline
SHADE = S('dry', 'calm', 'late', 'N')     # her shading test
ESHADE = S('dry', 'calm', 'early', 'N')   # a shaded year in which the neighbour planted early
FSTAR = S('wet', 'windy', 'early', 'S')   # the failed sixth summer
SEED = S('dry', 'calm', 'early', 'S')     # the seed trial
RAIN = S('wet', 'calm', 'late', 'S')      # another wet spring, usual planting


class Org:
    def __init__(self, name, ports, comps):
        self.name = name
        self.ports = dict(ports)
        self.comps = dict(comps)          # cname -> (footprint tuple, frozenset of value tuples)

    def sol(self, x, deleted=()):
        fixed = {p: x[p] for p in self.ports if p in x}
        free = [p for p in self.ports if p not in x]
        out = []
        live = [(fp, rel) for c, (fp, rel) in self.comps.items() if c not in deleted]
        for vals in product(*(self.ports[p] for p in free)):
            z = dict(fixed)
            z.update(zip(free, vals))
            if all(tuple(z[p] for p in fp) in rel for fp, rel in live):
                out.append(z)
        return out

    def ans(self, x, deleted=()):
        return frozenset(z['first'] for z in self.sol(x, deleted))


def freeze(z):
    return tuple(sorted(z.items()))


# ------------------------------------------------------------------ the target D
D = Org('D', {'W': DOM_IN['W'], 'Wi': DOM_IN['Wi'], 'V': DOM_IN['V'], 'Sun': DOM_IN['Sun'],
              'ovrD': (0, 1), 'first': ('N', 'S')},
        {'dvar': (('V', 'ovrD'), frozenset({('late', 0), ('early', 1)})),
         'dfirst': (('Sun', 'ovrD', 'first'),
                    frozenset({('S', 0, 'S'), ('N', 0, 'N'), ('S', 1, 'N'), ('N', 1, 'N')}))})


def truth(x):
    return D.ans(x)


class Cand:
    """(E, t, Gamma): organization, transport map pi, anchors (comp -> (D comps, port translation)), Gamma."""

    def __init__(self, name, org, pi, anchors, gamma):
        self.name, self.org, self.pi, self.anchors, self.gamma = name, org, pi, anchors, set(gamma)

    def A(self, x):
        return self.org.ans(x) == truth(x)

    def F2(self, x):
        return {freeze(self.pi(z)) for z in D.sol(x)} == {freeze(z) for z in self.org.sol(x)}

    def F1(self, x):
        for k in self.gamma:
            fp, rel = self.org.comps[k]
            dcomps, tr = self.anchors[k]
            others = [c for c in D.comps if c not in dcomps]
            proj = {tuple(z[tr[p]] for p in fp) for z in D.sol(x, deleted=others)}
            lk = {t for t in rel if all(t[i] == x[p] for i, p in enumerate(fp) if p in x and p in self.org.ports)}
            if proj != lk:
                return False
        return True

    def noncirc(self, C):
        if not any(freeze(y) == freeze(B0) for y in C):
            return False
        g = sorted(self.gamma)
        ab = self.org.ans(B0)
        for x in C:
            ax = self.org.ans(x)
            if ax == ab:
                continue
            for r in range(1, len(g) + 1):
                for G in combinations(g, r):
                    ax2, ab2 = self.org.ans(x, G), self.org.ans(B0, G)
                    det = lambda a: len(a) == 1
                    if (det(ax2) and det(ab2) and ax2 == ab2) or (det(ax) and not det(ax2)) or (det(ab) and not det(ab2)):
                        return True
        return False

    def account(self, C, conj=('A', 'F1', 'F2', 'NC')):
        if not D.sol(B0):
            return False
        for x in C:
            if 'A' in conj and not self.A(x):
                return False
            if 'F2' in conj and not self.F2(x):
                return False
            if 'F1' in conj and not self.F1(x):
                return False
        if 'NC' in conj and not self.noncirc(C):
            return False
        return True

    def why(self, C):
        bad = []
        for x in C:
            for nm, f in (('A', self.A), ('F2', self.F2), ('F1', self.F1)):
                if not f(x):
                    bad.append('%s@%s' % (nm, show(x)))
        if not self.noncirc(C):
            bad.append('NonCircular')
        return bad


def pres(members, F, conj=('A', 'F1', 'F2', 'NC')):
    return [m for m in members if all(m.account(C, conj) for C in F)]


# ------------------------------------------------------------------ menus
SUNMAPS = {'id': {'S': 'S', 'N': 'N'}, 'allS': {'S': 'S', 'N': 'S'}, 'allN': {'S': 'N', 'N': 'N'},
           'swap': {'S': 'N', 'N': 'S'}}
PRED_V = {'off': lambda v: 0, 'always': lambda v: 1, 'early': lambda v: int(v == 'early'),
          'late': lambda v: int(v == 'late')}

# ------------------------------------------------------------------ E0, the earlier candidate (own transport)
E0_ORG = Org('E0', {'W': DOM_IN['W'], 'Wi': DOM_IN['Wi'], 'Sun': DOM_IN['Sun'], 'first': ('N', 'S')},
             {'sun': (('Sun', 'first'), frozenset({('S', 'S'), ('N', 'N')}))})
E0 = Cand('E0 (own transport)', E0_ORG,
          lambda z: {'W': z['W'], 'Wi': z['Wi'], 'Sun': z['Sun'], 'first': z['first']},
          {'sun': ({'dvar', 'dfirst'}, {'Sun': 'Sun', 'first': 'first'})}, {'sun'})


# ------------------------------------------------------------------ Embedding 1: the correction adds a mechanism with its own port
def pi1(z):
    return {'W': z['W'], 'Wi': z['Wi'], 'V': z['V'], 'Sun': z['Sun'], 'ovr': z['ovrD'], 'first': z['first']}


PORTS1 = {'W': DOM_IN['W'], 'Wi': DOM_IN['Wi'], 'V': DOM_IN['V'], 'Sun': DOM_IN['Sun'], 'ovr': (0, 1),
          'first': ('N', 'S')}


def sunp_rel(g):
    m = SUNMAPS[g]
    return frozenset({(s, 0, m[s]) for s in 'SN'} | {(s, 1, 'N') for s in 'SN'})


def emb1_member(g, p, var_ports=('V',), pred=None, label=None):
    if pred is None:
        pred = PRED_V[p]
        rel = frozenset({(v, pred(v)) for v in DOM_IN['V']})
        fp = ('V', 'ovr')
    else:
        rel = frozenset({tuple(c) + (pred(*c),) for c in product(*(DOM_IN[q] for q in var_ports))})
        fp = tuple(var_ports) + ('ovr',)
    org = Org('E1[%s,%s]' % (g, label or p), PORTS1,
              {"sun'": (('Sun', 'ovr', 'first'), sunp_rel(g)), 'var': (fp, rel)})
    tr_var = {q: q for q in var_ports}
    tr_var['ovr'] = 'ovrD'
    return Cand("(sun'=%s, var=%s)" % (g, label or p), org, pi1,
                {"sun'": ({'dfirst'}, {'Sun': 'Sun', 'ovr': 'ovrD', 'first': 'first'}),
                 'var': ({'dvar'}, tr_var)}, {"sun'", 'var'})


def emb1_alpha():
    """The proposal's v0 read literally: restore the old sun component, delete the added block."""
    org = Org('E1 with var deleted and sun restored', PORTS1,
              {'sun': (('Sun', 'first'), frozenset({('S', 'S'), ('N', 'N')}))})
    return Cand('(sun restored, var deleted)', org, pi1,
                {'sun': ({'dvar', 'dfirst'}, {'Sun': 'Sun', 'first': 'first'})}, {'sun'})


# ------------------------------------------------------------------ Embedding 2: the same correction as a changed rule, no new port
PORTS2 = {'W': DOM_IN['W'], 'Wi': DOM_IN['Wi'], 'V': DOM_IN['V'], 'Sun': DOM_IN['Sun'], 'first': ('N', 'S')}


def pi2(z):
    return {'W': z['W'], 'Wi': z['Wi'], 'V': z['V'], 'Sun': z['Sun'], 'first': z['first']}


def emb2_member(g, p):
    m, pr = SUNMAPS[g], PRED_V[p]
    rel = frozenset({(v, s, 'N' if pr(v) else m[s]) for v in DOM_IN['V'] for s in 'SN'})
    org = Org('E1b[%s,%s]' % (g, p), PORTS2, {'rule': (('V', 'Sun', 'first'), rel)})
    return Cand('(rule: N if %s else %s(Sun))' % (p, g), org, pi2,
                {'rule': ({'dvar', 'dfirst'}, {'V': 'V', 'Sun': 'Sun', 'first': 'first'})}, {'rule'})
