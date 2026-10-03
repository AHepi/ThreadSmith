#!/usr/bin/env python3
"""pl.py - an independent pair-level engine (Account read as (A) at single pairs), written from the
description in 02 section 1, without importing ratchet/models. Used to re-derive 02/03 numbers and for
the family-choice attacks. Profiles are 16-bit masks of the pairs a version gets right.
"""
from itertools import product

PORTS = ('W', 'Wi', 'V', 'Sun')
DOM = {'W': (0, 1), 'Wi': (0, 1), 'V': (0, 1), 'Sun': (0, 1)}   # W 1=wet, Wi 1=windy, V 1=early, Sun 1=south shaded
SETTINGS = list(product((0, 1), repeat=4))
IDX = {s: i for i, s in enumerate(SETTINGS)}
NS = 16
FULLM = (1 << NS) - 1
NAME = {'W': ('dry', 'wet'), 'Wi': ('calm', 'windy'), 'V': ('late', 'early'), 'Sun': ('sunS', 'shadeS')}


def show(i):
    s = SETTINGS[i]
    return '/'.join(NAME[p][v] for p, v in zip(PORTS, s))


def get(s, p):
    return s[PORTS.index(p)]


# answers: 1 = north first, 0 = south first
TRUTH = [1 if get(s, 'V') == 1 else get(s, 'Sun') for s in SETTINGS]


def mask(idxs):
    m = 0
    for i in idxs:
        m |= 1 << i
    return m


def S(W, Wi, V, Sun):
    return IDX[(W, Wi, V, Sun)]


B0, SHADE, FSTAR = S(0, 0, 0, 0), S(0, 0, 0, 1), S(1, 1, 1, 0)
SEED, RAIN, ESHADE = S(0, 0, 1, 0), S(1, 0, 0, 0), S(0, 0, 1, 1)
J_BEFORE = mask([B0, SHADE])
J_AFTER = J_BEFORE | mask([FSTAR])
C_FULL = FULLM


def pred_menu(ports):
    """All predicates on the ports, as 16-bit fire masks (off first)."""
    configs = list(product((0, 1), repeat=len(ports)))
    menu = []
    for outs in product((0, 1), repeat=len(configs)):
        fire = {c for c, o in zip(configs, outs) if o}
        menu.append(mask(i for i, s in enumerate(SETTINGS) if tuple(get(s, p) for p in ports) in fire))
    return menu


def sun_menu(ports=('Sun',)):
    """Maps from the listed ports to an answer, as answer vectors (the old organization's component)."""
    configs = list(product((0, 1), repeat=len(ports)))
    menu = []
    for outs in product((0, 1), repeat=len(configs)):
        tab = dict(zip(configs, outs))
        menu.append(tuple(tab[tuple(get(s, p) for p in ports)] for s in SETTINGS))
    return menu


SUN4 = sun_menu(('Sun',))            # order: (0->0,1->0)=allS, (0->0,1->1)=id, (0->1,1->0)=swap, (0->1,1->1)=allN
SUN_ID = (tuple(get(s, 'Sun') for s in SETTINGS))
SINGLE = [0] + [1 << i for i in range(NS)]


def okmask(sunvec, fire):
    m = 0
    for i in range(NS):
        a = 1 if (fire >> i) & 1 else sunvec[i]
        if a == TRUTH[i]:
            m |= 1 << i
    return m


def family(sun_list, override_menus):
    """Versions of 'sun x override_1 x ... x override_k'. Returns list of (key, okmask)."""
    out = []
    for si, sv in enumerate(sun_list):
        for combo in product(*[range(len(m)) for m in override_menus]):
            fire = 0
            for m, c in zip(override_menus, combo):
                fire |= m[c]
            out.append(((si,) + combo, okmask(sv, fire)))
    return out


def pres(fam, F):
    return [k for k, m in fam if m & F == F]


def count(fam, F):
    return sum(1 for _, m in fam if m & F == F)


def answers(sunvec, fire):
    return tuple(1 if (fire >> i) & 1 else sunvec[i] for i in range(NS))


E0_ANS = SUN_ID
M0 = mask(i for i in range(NS) if E0_ANS[i] != TRUTH[i])
R0 = FULLM & ~M0
