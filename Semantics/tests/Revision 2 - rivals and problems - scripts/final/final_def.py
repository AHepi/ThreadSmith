#!/usr/bin/env python3
"""final_def.py - the definitions of W59.1 as finally worded for draft 4 (25 September), on the engine of
02 (models/engine.py) and the physics filter of 03b (attack/ext.py). Nothing in engine.py or ext.py is changed.

The wording implemented (W59.1, "Rivals" and "Problems", draft 4):
  conflict   Two candidates CONFLICT at an admitted edit-boundary pair of the target that both their transports
             translate when their answers there differ, or when each of them could meet (F1), (F2) and (A) there
             under some relations of the target that the adopted physics admits and no such relations let both.
             (03a's definition, with 03b's FIX-2 on the quantifier.)
  rivals     one has been offered as an answer to p in place of the other, and they conflict at some admitted
             pair, in C or outside it. (03a's rival test, with 03b's FIX-5 on the tense.)
  fits       as in engine.fits: no established result shows the candidate failing a condition of (E).
  problem    two rivals that both fit. Kind (i): they conflict at some pair of C. Kind (ii): only outside C.
The text's claims about the kinds are checked pair by pair (check_claims), over the relations the physics
admits at a pair:
  (i)   at a conflict pair of C, whatever the target does there, at most one of them meets the three conditions
        (so at most one is an account of p, whether or not anyone can establish it); establishing the target's
        relations there (its answer, where their answers differ) leaves at most one fitting, whatever it shows.
  (ii)  their answers agree at every pair of C; a finer contract that adds one pair outside C where they conflict
        gives a problem of kind (i) on the new question.
  both  if both are accounts on C, they conflict at no pair of C.
No function lists, counts or grades rivals: every verdict is an existential or universal statement over the
admitted pairs and the target's possible relations at one pair. Standard library only.
"""
import os
import sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'models'))
sys.path.insert(0, os.path.join(HERE, '..', 'attack'))
from engine import key, fits  # noqa: E402
from ext import applies  # noqa: E402


def rel_variants(D, x, space='all', phys=None, variants=None):
    """The target's possible relations at x that the adopted physics admits."""
    src = variants(x) if variants is not None else D.variants(x, space)
    for rels in src:
        if phys is not None and not phys(rels, x):
            continue
        yield rels


def conflict_final(c1, c2, x, D, space='all', phys=None, variants=None):
    """(conflict, route). Only for pairs both candidates translate (the caller checks)."""
    if c1.ans(x) != c2.ans(x):
        return True, 'answers differ'
    can1 = can2 = False
    for rels in rel_variants(D, x, space, phys, variants):
        m1, m2 = c1.meets(x, D, rels), c2.meets(x, D, rels)
        if m1 and m2:
            return False, ''
        can1 |= m1
        can2 |= m2
    if can1 and can2:
        return True, 'each could meet the three, no relations let both'
    return False, ''


def conflicts(c1, c2, pairs, D, space='all', phys=None, variants=None):
    out = []
    for x in pairs:
        if applies(c1, x) and applies(c2, x):
            c, route = conflict_final(c1, c2, x, D, space, phys, variants)
            if c:
                out.append((x, route))
    return out


def verdict_final(c1, c2, C, ADM, D, est, offered=True, space='all', phys=None, variants=None, nc=None):
    """Returns (verdict string, info dict). ADM: the admitted pairs of the target (a superset of C)."""
    info = {}
    if not offered:
        return 'not rivals: neither has been offered in place of the other', info
    cf = conflicts(c1, c2, ADM, D, space, phys, variants)
    info['conflicts'] = cf
    if not cf:
        return 'not rivals: they conflict at no admitted pair', info
    f1, f2 = fits(c1, est, D, nc), fits(c2, est, D, nc)
    info['fits'] = (f1, f2)
    if not (f1 and f2):
        return 'rivals; NO problem: %s does not fit what is established' % (
            ' and '.join(n for n, f in ((c1.name, f1), (c2.name, f2)) if not f)), info
    Ck = {key(y) for y in C}
    inC = [x for x, _ in cf if key(x) in Ck]
    out = [x for x, _ in cf if key(x) not in Ck]
    info['inC'], info['out'] = inC, out
    info['kind'] = 'i' if inC else 'ii'
    return 'PROBLEM for p, kind (%s): conflict at %d pair(s) of C, %d admitted pair(s) outside C' % (
        info['kind'], len(inC), len(out)), info


def check_claims(c1, c2, C, ADM, D, est, info, b0=None, space='all', phys=None, variants=None):
    """Checks the text's claims about the kind found. Returns a list of 'claim: True/False' strings."""
    res = []
    if 'kind' not in info:
        return res
    if info['kind'] == 'i':
        at_most_one = all(not (c1.meets(x, D, r) and c2.meets(x, D, r))
                          for x in info['inC'] for r in rel_variants(D, x, space, phys, variants))
        res.append('(i) at a conflict pair of C, whatever the target does, at most one meets the three: %s' % at_most_one)
        solves = True
        for x in info['inC']:
            ans_differ = c1.ans(x) != c2.ans(x)
            for r in rel_variants(D, x, space, phys, variants):
                e = dict(est)
                e[key(x)] = ('ans', D.ans(x, r)) if ans_differ else ('full', r)
                if fits(c1, e, D) and fits(c2, e, D):
                    solves = False
                    break
        res.append('(i) establishing the relations there (the answer, where the answers differ) solves it whatever '
                   'it shows: %s' % solves)
    else:
        agree = all(c1.ans(x) == c2.ans(x) for x in C)
        res.append('(ii) their answers agree at every pair of C: %s' % agree)
        x = info['out'][0]
        v, inf2 = verdict_final(c1, c2, C + [x], ADM, D, est, True, space, phys, variants)
        res.append('(ii) a finer contract adding one pair outside C where they conflict gives kind (i): %s' % (
            inf2.get('kind') == 'i'))
        alone = False
        for y in C:
            for r in rel_variants(D, y, space, phys, variants):
                if c1.meets(y, D, r) != c2.meets(y, D, r):
                    alone = True
                    break
            if alone:
                break
        res.append('(ii, information only) some outcome of a test inside C refutes one without the other: %s' % alone)
    if b0 is not None:
        a1, a2 = c1.account(C, b0, D), c2.account(C, b0, D)
        if a1 and a2:
            res.append('both are accounts on C, and they conflict at no pair of C: %s' % (not info.get('inC')))
    return res
