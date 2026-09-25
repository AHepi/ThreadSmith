#!/usr/bin/env python3
"""garden.py - the gardener's target and candidates, as in fe.py (correction-sticks analysis, 04b),
rebuilt on engine.py.

Target D (the garden): inputs W (dry/wet spring), Wi (calm/windy), V (late/early variety on the
north side), Sun (S = the south bed sunnier; N = the south wall shaded). Internal: ovrD, the
variety effect; first, which bed ripens first.
  dvar   (V, ovrD):         ovrD = 1 iff V = early
  dfirst (Sun, ovrD, first): first = N if ovrD else the sunnier bed
Candidates (the good rescue in two writings, as the analysis had them):
  Emb-1 (a mechanism): sun' (Sun, ovr, first) anchored to dfirst; var (V, W, Wi, [Sun,] ovr) anchored
        to dvar, with a predicate saying when the effect is on. pi reads ovr from ovrD.
  Emb-2 (a changed rule): rule (V, Sun, first) anchored to {dvar, dfirst}.
  E0    sun (Sun, first) anchored to {dvar, dfirst}.
Every var component reads the same ports (V, W, Wi), so that the good and bad rescues anchor one
subnetwork on the same D ports, as in the analysis's one-family runs (a5, a6).
"""
from itertools import product
from engine import Org, Target, Cand

DOM = {'W': ('dry', 'wet'), 'Wi': ('calm', 'windy'), 'V': ('late', 'early'), 'Sun': ('S', 'N')}
INPUTS = ('W', 'Wi', 'V', 'Sun')
SETTINGS = [dict(zip(INPUTS, t)) for t in product(*(DOM[k] for k in INPUTS))]
WORD = {'S': 'sunS', 'N': 'shadeS'}


def show(x):
    s = '/'.join(WORD.get(x[k], x[k]) if k == 'Sun' else x[k] for k in INPUTS if k in x)
    if 'ovrD' in x:
        s += '/set ovr=%d' % x['ovrD']
    return s


def S(W, Wi, V, Sun):
    return {'W': W, 'Wi': Wi, 'V': V, 'Sun': Sun}


B0 = S('dry', 'calm', 'late', 'S')       # the recorded summers, all alike: the baseline
SHADE = S('dry', 'calm', 'late', 'N')    # her shading test
FSTAR = S('wet', 'windy', 'early', 'S')  # the failed summer
SEED = S('dry', 'calm', 'early', 'S')    # a dry spring with the early variety (the seed trial)
ESHADE = S('dry', 'calm', 'early', 'N')  # a shaded year with the early variety
RAIN = S('wet', 'calm', 'late', 'S')     # a wet spring with the usual planting

D_ORG = Org('D', {'W': DOM['W'], 'Wi': DOM['Wi'], 'V': DOM['V'], 'Sun': DOM['Sun'],
                  'ovrD': (0, 1), 'first': ('N', 'S')},
            {'dvar': (('V', 'ovrD'), frozenset({('late', 0), ('early', 1)})),
             'dfirst': (('Sun', 'ovrD', 'first'),
                        frozenset({('S', 0, 'S'), ('N', 0, 'N'), ('S', 1, 'N'), ('N', 1, 'N')}))})
D = Target(D_ORG, 'first')

SUNMAPS = {'id': {'S': 'S', 'N': 'N'}, 'allS': {'S': 'S', 'N': 'S'}, 'allN': {'S': 'N', 'N': 'N'},
           'swap': {'S': 'N', 'N': 'S'}}


def tau_in(ports):
    return lambda x: {p: v for p, v in x.items() if p in ports}


def e0(question='p'):
    org = Org('E0', {'W': DOM['W'], 'Wi': DOM['Wi'], 'Sun': DOM['Sun'], 'first': ('N', 'S')},
              {'sun': (('Sun', 'first'), frozenset({('S', 'S'), ('N', 'N')}))})
    return Cand('E0', org, 'first', tau_in(('W', 'Wi', 'Sun')),
                lambda z: {'W': z['W'], 'Wi': z['Wi'], 'Sun': z['Sun'], 'first': z['first']},
                {'sun': ({'dvar', 'dfirst'}, {'Sun': 'Sun', 'first': 'first'})}, {'sun'}, question)


def emb1(name, pred, g='id', var_ports=('V', 'W', 'Wi'), question='p', effect='ovr', names=('sun1', 'var')):
    """pred: function of the var ports' values -> 0/1. effect: the E name of the variety-effect port."""
    ports = {'W': DOM['W'], 'Wi': DOM['Wi'], 'V': DOM['V'], 'Sun': DOM['Sun'], effect: (0, 1), 'first': ('N', 'S')}
    m = SUNMAPS[g]
    sunrel = frozenset({(s, 0, m[s]) for s in 'SN'} | {(s, 1, 'N') for s in 'SN'})
    varrel = frozenset({c + (pred(*c),) for c in product(*(DOM[p] for p in var_ports))})
    n_sun, n_var = names
    org = Org(name, ports, {n_sun: (('Sun', effect, 'first'), sunrel), n_var: (tuple(var_ports) + (effect,), varrel)})
    tr_var = {p: p for p in var_ports}
    tr_var[effect] = 'ovrD'

    def tau(x):
        ex = {p: v for p, v in x.items() if p in INPUTS}
        if 'ovrD' in x:
            ex[effect] = x['ovrD']
        return ex

    def pi(z):
        return {'W': z['W'], 'Wi': z['Wi'], 'V': z['V'], 'Sun': z['Sun'], effect: z['ovrD'], 'first': z['first']}

    return Cand(name, org, 'first', tau, pi,
                {n_sun: ({'dfirst'}, {'Sun': 'Sun', effect: 'ovrD', 'first': 'first'}), n_var: ({'dvar'}, tr_var)},
                {n_sun, n_var}, question)


def emb2(name, fn, question='p'):
    """fn: (V, Sun) -> first. One component anchored to {dvar, dfirst}."""
    ports = {'W': DOM['W'], 'Wi': DOM['Wi'], 'V': DOM['V'], 'Sun': DOM['Sun'], 'first': ('N', 'S')}
    rel = frozenset({(v, s, fn(v, s)) for v in DOM['V'] for s in DOM['Sun']})
    org = Org(name, ports, {'rule': (('V', 'Sun', 'first'), rel)})
    return Cand(name, org, 'first', tau_in(INPUTS),
                lambda z: {'W': z['W'], 'Wi': z['Wi'], 'V': z['V'], 'Sun': z['Sun'], 'first': z['first']},
                {'rule': ({'dvar', 'dfirst'}, {'V': 'V', 'Sun': 'Sun', 'first': 'first'})}, {'rule'}, question)


EARLY = lambda v, w, wi: int(v == 'early')
WET = lambda v, w, wi: int(w == 'wet')
WINDY = lambda v, w, wi: int(wi == 'windy')
PATCH = lambda v, w, wi: int(v == 'early' and w == 'wet' and wi == 'windy')
