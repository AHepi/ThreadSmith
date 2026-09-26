#!/usr/bin/env python3
"""seasons.py - the seasons target, the tilt, and the myths, on engine.py.

Target D: inputs place (N = Greece, E = the equator, S = far south) and half (H1 = the Greek summer
months, H2 = the other half). Internal ports: exp (how directly the sun strikes: +1, 0, -1), ins (the
warmth received: +1, 0, -1), season (summer, none, winter).
  dexp    (place, half, exp):  exp = lat(place) * sign(half)      (the tilted axis, kept steady)
  dins    (exp, ins):          ins = exp                           (direct rays warm)
  dseason (ins, season):       +1 summer, 0 none, -1 winter
Query: season.

Candidates. Every myth component is given an anchor, as Part IV requires. Two readings:
  R-real  each myth component is anchored to the real subnetwork that plays its part (Persephone's being
          away <-> the low sun, dexp; Demeter's grief <-> the warmth received, dins; the cold <-> dseason).
          Then the myth is the tilt with place ignored, relabelled.
  R-none  each myth component is anchored to NO component of D (the gods do not exist), with the same
          port translations: its anchor imposes nothing, so (F1) compares it with the full relation.
The myths:
  dem     "Demeter grieves": sched (half -> away), grief (away -> grief), gcold (grief -> season).
  dem_p   the same, but gcold also reads place (and ignores it): the same story, written with one more port.
  sorrow  dem with 'grief' renamed 'sorrow' (a label swap).
  und     "Persephone is underground" (as the cause, no grief): sched, cold (away -> season) anchored to
          {dins, dseason}: one mediating step fewer.
  dem2    "Demeter's grief makes the cold", written without a separate grief state: sched, cold' ; the
          same cut as und.
  freyr   und relabelled: Freyr's fortunes in his war (Deutsch p.20), same cut as und.
  south   N2's amended myth: dem_p, but at the far south the season is the opposite.
"""
from engine import Org, Target, Cand

PLACES = ('N', 'E', 'S')
HALVES = ('H1', 'H2')
LAT = {'N': 1, 'E': 0, 'S': -1}
SG = {'H1': 1, 'H2': -1}
SEAS = {1: 'summer', 0: 'none', -1: 'winter'}
OPP = {'summer': 'winter', 'winter': 'summer', 'none': 'none'}
V3 = (1, 0, -1)
PAIRS = [{'place': p, 'half': h} for p in PLACES for h in HALVES]
GREEK = [{'place': 'N', 'half': 'H1'}, {'place': 'N', 'half': 'H2'}]
SOUTH = [{'place': 'S', 'half': 'H1'}, {'place': 'S', 'half': 'H2'}]
B0 = {'place': 'N', 'half': 'H1'}


def show(x):
    return '%s,%s' % (x['place'], x['half'])


D_ORG = Org('D', {'place': PLACES, 'half': HALVES, 'exp': V3, 'ins': V3, 'season': ('summer', 'none', 'winter')},
            {'dexp': (('place', 'half', 'exp'), frozenset((p, h, LAT[p] * SG[h]) for p in PLACES for h in HALVES)),
             'dins': (('exp', 'ins'), frozenset((e, e) for e in V3)),
             'dseason': (('ins', 'season'), frozenset((i, SEAS[i]) for i in V3))})
D = Target(D_ORG, 'season')

SEASONS = ('summer', 'none', 'winter')
SCHED = frozenset({('H1', 1), ('H2', -1)})                  # Persephone home in H1, away in H2
LAW = frozenset((v, SEAS[v]) for v in V3)                   # home -> summer, away -> winter
MID = frozenset((v, v) for v in V3)                         # away -> grieving, home -> calm


def tilt(question):
    org = Org('tilt', {'place': PLACES, 'half': HALVES, 'exp': V3, 'ins': V3, 'season': SEASONS},
              {'geo': (('place', 'half', 'exp'), D_ORG.comps['dexp'][1]),
               'heat': (('exp', 'ins'), D_ORG.comps['dins'][1]),
               'seas': (('ins', 'season'), D_ORG.comps['dseason'][1])})
    return Cand('tilt', org, 'season', lambda x: dict(x), lambda z: dict(z),
                {'geo': ({'dexp'}, {'place': 'place', 'half': 'half', 'exp': 'exp'}),
                 'heat': ({'dins'}, {'exp': 'exp', 'ins': 'ins'}),
                 'seas': ({'dseason'}, {'ins': 'ins', 'season': 'season'})},
                {'geo', 'heat', 'seas'}, question)


def myth3(name, question, real=True, reads_place=False, south=False, mid='grief', names=('sched', 'griefc', 'gcold')):
    """Three components: schedule, a mediating state (grief), cold. reads_place: gcold also reads place."""
    n_s, n_g, n_c = names
    ports = {'half': HALVES, 'away': V3, mid: V3, 'season': SEASONS}
    if reads_place:
        ports['place'] = PLACES
        rel = frozenset((p, v, (OPP[SEAS[v]] if (south and p == 'S') else SEAS[v])) for p in PLACES for v in V3)
        gcold = (('place', mid, 'season'), rel)
        tr_c = {'place': 'place', mid: 'ins', 'season': 'season'}
    else:
        gcold = ((mid, 'season'), LAW)
        tr_c = {mid: 'ins', 'season': 'season'}
    org = Org(name, ports, {n_s: (('half', 'away'), SCHED), n_g: (('away', mid), MID), n_c: gcold})
    A = (lambda s: s) if real else (lambda s: set())
    tau = (lambda x: dict(x)) if reads_place else (lambda x: {'half': x['half']})

    def pi(z):
        out = {'half': z['half'], 'away': z['exp'], mid: z['ins'], 'season': z['season']}
        if reads_place:
            out['place'] = z['place']
        return out

    return Cand(name, org, 'season', tau, pi,
                {n_s: (A({'dexp'}), {'half': 'half', 'away': 'exp'}),
                 n_g: (A({'dins'}), {'away': 'exp', mid: 'ins'}),
                 n_c: (A({'dseason'}), tr_c)},
                {n_s, n_g, n_c}, question)


def myth2(name, question, real=True, state='away', names=('sched', 'cold')):
    """Two components: schedule, and the state -> season (the coarse cut)."""
    n_s, n_c = names
    org = Org(name, {'half': HALVES, state: V3, 'season': SEASONS},
              {n_s: (('half', state), SCHED), n_c: ((state, 'season'), LAW)})
    A = (lambda s: s) if real else (lambda s: set())
    return Cand(name, org, 'season', lambda x: {'half': x['half']},
                lambda z: {'half': z['half'], state: z['exp'], 'season': z['season']},
                {n_s: (A({'dexp'}), {'half': 'half', state: 'exp'}),
                 n_c: (A({'dins', 'dseason'}), {state: 'exp', 'season': 'season'})},
                {n_s, n_c}, question)
