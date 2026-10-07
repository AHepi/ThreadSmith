#!/usr/bin/env python3
"""A3 - the companion clause of (H*), under Part II's solution semantics.

03, section 2(b): "Where E1 only adds a block B, E0 = E1|(Gamma1 minus B). ... If also Account(E1, f*) and
E0 = E1|(Gamma1 minus B), then CriticalBlock(B; Gamma1, f*)."
03, section 1(2): "a rescuing addition is critical at the failed job, and all three rescues (good, wet
spring, one-summer exception) are (M3, companion)."
m3_lemma_check.py computes that with Family.profile(v, deleted=...), whose docstring says
"override -> off": a deleted override is switched off. Part II (D3:L101): "A deleted component imposes the
full relation on its ports." Part VI (D3:L287): E|W is taken under "a declared restriction operation".

(a) Pure addition: (O) makes Sol an intersection over components, so adding a block can only shrink Sol.
    If E0 gives a determined wrong answer at f*, no E0 + B gives the right one.
(b) The gardener's rescue (Emb-1 of a1): the two restriction operations give different criticality.
(c) Where the companion does apply: an E0 that was silent (undetermined) at f*, not wrong.
"""
import random
from itertools import product
from fe import (Org, Cand, SETTINGS, DOM_IN, B0, SHADE, ESHADE, FSTAR, truth, emb1_member, show, PORTS1, pi1)

random.seed(4)
J_SEEN, J_ESHADE, J_FAIL = [B0, SHADE], [B0, ESHADE], [B0, FSTAR]
SUN_REL = frozenset({('S', 'S'), ('N', 'N')})


def bare(org, gamma):
    """A candidate assessed on (A) and NonCircular only (transport irrelevant to these two)."""
    return Cand(org.name, org, None, {}, gamma)


def part_a():
    print('-' * 100)
    print('(a) PURE ADDITION: E1 = E0 + B, E0 = "the sunnier bed first" kept unchanged')
    print('-' * 100)
    base_ports = {'V': DOM_IN['V'], 'Sun': DOM_IN['Sun'], 'first': ('N', 'S')}
    for label, extra, fp in (('B any relation on (V, Sun, first)', {}, ('V', 'Sun', 'first')),
                             ('B any relation on (V, Sun, ovr, first), ovr a new port', {'ovr': (0, 1)},
                              ('V', 'Sun', 'ovr', 'first'))):
        ports = dict(base_ports)
        ports.update(extra)
        tuples = list(product(*(ports[p] for p in fp)))
        n = rescued = 0
        shrink_ok = True
        e0 = Org('E0', ports, {'sun': (('Sun', 'first'), SUN_REL)})
        a0 = {tuple(sorted(x.items())): e0.ans(x) for x in SETTINGS}
        for bits in range(1 << len(tuples)):
            rel = frozenset(t for i, t in enumerate(tuples) if bits >> i & 1)
            e1 = Org('E1', ports, {'sun': (('Sun', 'first'), SUN_REL), 'B': (fp, rel)})
            n += 1
            if e1.ans(FSTAR) == truth(FSTAR):
                rescued += 1
            if len(tuples) <= 8:
                for x in SETTINGS:
                    if not e1.ans(x) <= a0[tuple(sorted(x.items()))]:
                        shrink_ok = False
        print('  %-58s relations tried=%6d  E0+B answers north at f*: %d  Ans(E0+B) inside Ans(E0) everywhere: %s'
              % (label, n, rescued, shrink_ok if len(tuples) <= 8 else 'not run (f* checked)'))
    # random sample with W, Wi read too
    ports = {'W': DOM_IN['W'], 'Wi': DOM_IN['Wi'], 'V': DOM_IN['V'], 'Sun': DOM_IN['Sun'], 'ovr': (0, 1),
             'first': ('N', 'S')}
    fp = ('W', 'Wi', 'V', 'Sun', 'ovr', 'first')
    tuples = list(product(*(ports[p] for p in fp)))
    e0 = Org('E0', ports, {'sun': (('Sun', 'first'), SUN_REL)})
    rescued = 0
    for _ in range(3000):
        rel = frozenset(t for t in tuples if random.random() < 0.5)
        e1 = Org('E1', ports, {'sun': (('Sun', 'first'), SUN_REL), 'B': (fp, rel)})
        if e1.ans(FSTAR) == truth(FSTAR):
            rescued += 1
    print('  %-58s random relations=%5d  E0+B answers north at f*: %d' % ('B reads W, Wi, V, Sun, ovr, first', 3000, rescued))
    print('  So a block added beside a component that already fixes a WRONG answer cannot rescue: the rescue')
    print('  must change a component, and then E0 = E1|(Gamma1 - B) is false and the companion is silent.')


def part_b():
    print()
    print('-' * 100)
    print('(b) THE GARDENER\'S RESCUE (a1, Emb-1): E1 = {sun\': N if ovr else Sun, var: ovr = [V=early]}, B = {var}')
    print('-' * 100)
    e1 = emb1_member('id', 'early')
    e0 = Org('E0', {'W': DOM_IN['W'], 'Wi': DOM_IN['Wi'], 'Sun': DOM_IN['Sun'], 'first': ('N', 'S')},
             {'sun': (('Sun', 'first'), SUN_REL)})
    # restriction by deletion (Part II): var removed, ovr free
    r_del = Org('E1|{sun\'} by deletion', PORTS1, {"sun'": e1.org.comps["sun'"]})
    # restriction by switching off (the models' reading)
    r_off = Org('E1|{sun\'} by switch-off', PORTS1,
                {"sun'": e1.org.comps["sun'"], 'var': (('V', 'ovr'), frozenset({('late', 0), ('early', 0)}))})
    print('  E1|(Gamma1 - B) answers equal E0\'s at every pair?  deletion: %s   switch-off: %s' % (
        all(r_del.ans(x) == e0.ans(x) for x in SETTINGS), all(r_off.ans(x) == e0.ans(x) for x in SETTINGS)))
    print('  e.g. at %s: E0 %s, deletion %s, switch-off %s' % (show(B0), sorted(e0.ans(B0)), sorted(r_del.ans(B0)),
                                                              sorted(r_off.ans(B0))))
    for conj, cn in ((('A', 'NC'), '(A)+NonCircular'), (('A', 'F1', 'F2', 'NC'), 'full (E), E1\'s transport')):
        for rname, rorg in (('deletion', r_del), ('switch-off', r_off)):
            anchors = {"sun'": e1.anchors["sun'"]}
            rc = Cand(rorg.name, rorg, pi1, anchors, {"sun'"})
            row = []
            for jn, J in (('j_seen', J_SEEN), ('j_eshade', J_ESHADE), ('j_fail', J_FAIL)):
                full_ok = e1.account(J, conj)
                rest_ok = rc.account(J, conj)
                row.append('%s: %s' % (jn, 'CRITICAL' if (full_ok and not rest_ok) else 'not critical'))
            print('  %-28s restriction by %-10s  B=var is  %s' % (cn, rname, ';  '.join(row)))


def part_c():
    print()
    print('-' * 100)
    print('(c) WHERE THE COMPANION APPLIES: an E0 that was SILENT at f* (undetermined), not wrong')
    print('-' * 100)
    ports = {'V': DOM_IN['V'], 'Sun': DOM_IN['Sun'], 'ovr': (0, 1), 'first': ('N', 'S')}
    sunp = (('Sun', 'ovr', 'first'), frozenset({('S', 0, 'S'), ('N', 0, 'N'), ('S', 1, 'N'), ('N', 1, 'N')}))
    guard = (('V', 'ovr'), frozenset({('late', 0), ('early', 0), ('early', 1)}))   # "about a changed planting I say nothing"
    var = (('V', 'ovr'), frozenset({('late', 0), ('early', 1)}))
    e0s = Org("E0' silent", ports, {"sun'": sunp, 'guard': guard})
    e1s = Org("E1' = E0' + var", ports, {"sun'": sunp, 'guard': guard, 'var': var})
    c0 = bare(e0s, {"sun'", 'guard'})
    c1 = bare(e1s, {"sun'", 'guard', 'var'})
    rest = Org('E1\'|(Gamma - var) by deletion', ports, {"sun'": sunp, 'guard': guard})
    print('  E0\' answers at f*: %s (target %s)   E1\' answers at f*: %s' % (
        sorted(e0s.ans(FSTAR)), sorted(truth(FSTAR)), sorted(e1s.ans(FSTAR))))
    print('  E0\' does j_seen: %s  j_eshade: %s  j_fail: %s ;  E1\' does j_fail: %s' % (
        c0.account(J_SEEN, ('A', 'NC')), c0.account(J_ESHADE, ('A', 'NC')), c0.account(J_FAIL, ('A', 'NC')),
        c1.account(J_FAIL, ('A', 'NC'))))
    print('  E1\'|(Gamma - var) = E0\' exactly (same ports, same components)? %s' % (
        rest.ports == e0s.ports and rest.comps == e0s.comps))
    print('  -> CriticalBlock(var; Gamma1, j_fail): %s. The companion holds here, where E0 said nothing at f*.' % (
        c1.account(J_FAIL, ('A', 'NC')) and not bare(rest, {"sun'", 'guard'}).account(J_FAIL, ('A', 'NC'))))


if __name__ == '__main__':
    print('=' * 100)
    print('A3  THE COMPANION CLAUSE UNDER PART II DELETION')
    print('=' * 100)
    part_a()
    part_b()
    part_c()
