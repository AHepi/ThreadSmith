#!/usr/bin/env python3
"""ext.py - small extensions of rivals/models/engine.py for the attack scripts (03b).

Nothing here changes engine.py. Added:
  conflict_p      engine.conflict with an optional PHYSICS filter: only target relations at x that the
                  adopted physics admits (a predicate on the relation assignment) are quantified over.
  applies         whether a candidate makes claims at x (its transport translates x). Cand.scope = None
                  means every admitted pair; otherwise a set of pair keys.
  verdict_fix     the proposed repair: rivals = offered in place of each other AND each claims something the
                  other does not, at admitted pairs (in C or outside it) to which both apply. Kinds as in the
                  draft. No count, list or grade: existentials over the admitted pairs and the target's
                  possible relations, as the draft's own conflict is.
  VCand           a candidate whose port translations carry VALUE maps (a recoding of E's values), used to
                  test whether a pure recoding is a rival.
Standard library only.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'models'))
from engine import Org, Target, Cand, key, one_account, fits, problem, test_solves, fmt_problem  # noqa: E402


def conflict_p(c1, c2, x, D, space='all', phys=None):
    """(conflict, can1, can2): whatever target relations at x the physics admits, not both meet the three."""
    can1 = can2 = joint = False
    for rels in D.variants(x, space):
        if phys is not None and not phys(rels, x):
            continue
        m1, m2 = c1.meets(x, D, rels), c2.meets(x, D, rels)
        can1 |= m1
        can2 |= m2
        if m1 and m2:
            joint = True
            break
    if joint:
        can1 = can2 = True
    return (not joint), can1, can2


def applies(c, x):
    sc = getattr(c, 'scope', None)
    return sc is None or key(x) in sc


def draft_verdict(c1, c2, C, D, est, offered, space='all', phys=None):
    """The draft as written (engine.problem), with the physics filter available for the conflict test."""
    if phys is None:
        return problem(c1, c2, C, D, est, offered=offered, space=space)['verdict']
    oa, why = one_account(c1, c2, C)
    if not offered:
        return 'not rivals: not offered in place of each other'
    if oa:
        return 'not rivals: one account (%s)' % why
    if not (fits(c1, est, D) and fits(c2, est, D)):
        return 'rivals; NO problem (one does not fit)'
    cf = [x for x in C if conflict_p(c1, c2, x, D, space, phys)[0]]
    return 'PROBLEM for p, kind (%s)' % ('i' if cf else 'ii')


def profile(c1, c2, x, D, space='all', phys=None):
    """Over the target relations at x (that the physics admits): (both, only1, only2) = some relation lets
    both meet (F1), (F2), (A) there / lets c1 and not c2 / lets c2 and not c1."""
    both = o1 = o2 = False
    for rels in D.variants(x, space):
        if phys is not None and not phys(rels, x):
            continue
        m1, m2 = c1.meets(x, D, rels), c2.meets(x, D, rels)
        both |= m1 and m2
        o1 |= m1 and not m2
        o2 |= m2 and not m1
        if both and o1 and o2:
            break
    return both, o1, o2


def verdict_fix(c1, c2, C, ADM, D, est, offered, space='all', phys=None):
    """The repair proposed in 03b. ADM: the admitted pairs (a superset of C).
    Rivals: offered in place of each other, and EACH CLAIMS SOMETHING THE OTHER DOES NOT: at some admitted
    pair to which both apply (in C or not) the target could be such that c1 meets (F1), (F2), (A) there and
    c2 does not, and at some such pair the reverse. Kinds as in the draft: (i) they conflict (the draft's
    'whatever the target's relations there, not both meet') at a pair of C; (ii) otherwise.
    Returns (verdict, detail)."""
    if not offered:
        return 'not rivals: not offered in place of each other', ''
    both = [x for x in ADM if applies(c1, x) and applies(c2, x)]
    O1 = O2 = False
    sep = []
    for x in both:
        b, o1, o2 = profile(c1, c2, x, D, space, phys)
        O1 |= o1
        O2 |= o2
        if not b and (o1 or o2):
            sep.append(x)
    if not (O1 and O2):
        # O1: some relation lets c1 meet and not c2, i.e. c2 claims something c1 does not.
        if not (O1 or O2):
            who = 'neither claims anything the other does not'
        elif not O1:
            who = '%s claims nothing %s does not' % (c2.name, c1.name)
        else:
            who = '%s claims nothing %s does not' % (c1.name, c2.name)
        return 'not rivals: ' + who, ''
    if not (fits(c1, est, D) and fits(c2, est, D)):
        return 'rivals; NO problem (one does not fit)', ''
    kC = [x for x in C if conflict_p(c1, c2, x, D, space, phys)[0]]
    Ck = {key(y) for y in C}
    out = [x for x in sep if key(x) not in Ck]
    det = 'a pair outside C where they conflict (a finer contract separates them): %s' % ('yes' if out else 'NO')
    return ('PROBLEM for p, kind (i)' if kC else 'PROBLEM for p, kind (ii)'), det


class VCand(Cand):
    """A candidate whose anchor port translations carry value maps: vmap[E-port] = {D-value: E-value}.
    (F1) compares the anchor's projected relation, with values mapped, to the component's relation."""

    def __init__(self, *a, vmap=None, **k):
        super().__init__(*a, **k)
        self.vmap = vmap or {}

    def F1(self, x, D, rels=None, which=False):
        ex = self.tau(x)
        bad = []
        for kk in sorted(self.gamma):
            fp, rel = self.org.comps[kk]
            dcomps, tr = self.anchors[kk]
            proj = {tuple(self.vmap.get(p, {}).get(z[tr[p]], z[tr[p]]) for p in fp)
                    for z in D.org.sol(x, only=set(dcomps), rels=rels)}
            if proj != set(self.org.rel_under(kk, ex)):
                bad.append(kk)
                if not which:
                    return False
        return (not bad) if not which else bad


def rule(title):
    print()
    print('-' * 100)
    print(title)
    print('-' * 100)
