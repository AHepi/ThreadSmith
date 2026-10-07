#!/usr/bin/env python3
"""A3 - pairs that look alike but differ, and pairs that look different but claim the same.

For each pair: the draft (W59.1 as written: rivals = offered in place and "not one account on C" by the
parenthesis), 02's repair 1 ("one account" judged on every admitted pair), 02's repair 4 (set aside every
single commitment that does no work by W33.1's test, then compare), and the repair proposed here
(verdict_fix in ext.py: each claims something the other does not, at admitted pairs in or outside C).

(a) LOOK ALIKE, DIFFER. The garden with a soil-moisture port. Two candidates with the same active
    components, anchors, kinds and answers, differing only in a component of their named background
    (outside Gamma): moisture follows the wet spring, or the dry one. (F2) reads the whole organization.
(b) LOOK DIFFERENT, CLAIM THE SAME (a finer and a coarser cut at a place no admitted change reaches):
    x -> y -> z with y reached by no admitted edit; "two steps" against "one step". Then (b') the same with
    an admitted edit that sets y.
(c) A RECODING: E_good with its variety-effect values written the other way round (0 <-> 1), (i) with a
    port translation that carries the value map, (ii) with a translation that only renames ports.
(d) A DUPLICATE: E_good with its variety component stated twice (var, var2: same relation, same anchor).
(e) The tilt against its own coarsening ("season is fixed by place and half"), on the world question:
    (e1) the admitted changes are place and half only; (e2) shading, which sets the warmth received, is
    also admitted (outside the question's contract).
(f) A residual of the repair: two candidates each exact about a different link (including values no admitted
    change reaches), plus the whole step; both true.
"""
import itertools
from ext import (Org, Target, Cand, VCand, key, one_account, fits, problem, test_solves, verdict_fix,
                 draft_verdict, conflict_p, rule)
from engine import does_no_work
import garden as G
import seasons as S


def repair1(a, b, C, ADM, D, est, space='all'):
    return problem(a, b, C, D, est, offered=True, oa_C=ADM, space=space)['verdict']


def repair4(a, b, C, b0, D, est, space='all'):
    out = []
    for c in (a, b):
        idle = [d for d in sorted(c.gamma) if all(does_no_work(c, d, C, b0, D)[:2])]
        out.append((c.restrict(c.gamma - set(idle), name=c.name) if idle else c, idle))
    (a2, ia), (b2, ib) = out
    v = problem(a2, b2, C, D, est, offered=True, space=space)['verdict']
    return '%s   [set aside: %s | %s]' % (v, ia or '-', ib or '-')


def report(label, a, b, C, ADM, D, est, b0, show, space='all', do4=True):
    print('  %s' % label)
    print('    accounts on C: %s / %s' % (a.account(C, b0, D), b.account(C, b0, D)))
    print('    draft:         %s' % draft_verdict(a, b, C, D, est, True, space))
    print('    02 repair 1:   %s' % repair1(a, b, C, ADM, D, est, space))
    if do4:
        print('    02 repair 4:   %s' % repair4(a, b, C, b0, D, est, space))
    v, det = verdict_fix(a, b, C, ADM, D, est, True, space)
    print('    03b repair:    %s%s' % (v, ('   [' + det + ']') if det else ''))
    cf = [show(x) for x in C if conflict_p(a, b, x, D, space)[0]]
    print('    conflict pairs in C (draft\'s definition): %s' % (', '.join(cf) if cf else 'none'))


def part_a():
    rule('(a) look alike, differ: the same active components, anchors, kinds and answers; different background')
    DO = G.D_ORG
    ports = dict(DO.ports)
    ports['moist'] = (0, 1)
    comps = dict(DO.comps)
    comps['dmoist'] = (('W', 'moist'), frozenset({('dry', 0), ('wet', 1)}))
    DM = Target(Org('D+moist', ports, comps), 'first')

    def cand(name, bgrel):
        base = G.emb1(name, G.EARLY)
        p = dict(base.org.ports)
        p['moist'] = (0, 1)
        cc = dict(base.org.comps)
        cc['bg'] = (('W', 'moist'), bgrel)                  # named background: not in Gamma
        pi0 = base.pi
        return Cand(name, Org(name, p, cc), 'first', base.tau, lambda z: dict(pi0(z), moist=z['moist']),
                    base.anchors, base.gamma, 'p')

    WETM = cand('E_good + moisture follows the wet spring', frozenset({('dry', 0), ('wet', 1)}))
    DRYM = cand('E_good + moisture follows the dry spring', frozenset({('dry', 1), ('wet', 0)}))
    C = list(G.SETTINGS)
    est = {key(x): ('ans', DM.ans(x)) for x in (G.B0, G.SHADE, G.FSTAR)}
    print('    one account on C by the draft\'s parenthesis: %s' % (one_account(WETM, DRYM, C),))
    report('WETM vs DRYM on p (C = the 16 settings)', WETM, DRYM, C, C, DM, est, G.B0, G.show)
    x = G.B0
    print('    test at %s: sure to solve with relations established: %s ; with the answer only: %s' % (
        G.show(x), test_solves(WETM, DRYM, x, DM, est, 'all', 'full')[0], test_solves(WETM, DRYM, x, DM, est, 'all', 'ans')[0]))
    est2 = dict(est)
    est2[key(x)] = ('full', None)
    print('    with the actual relations at %s established: WETM fits %s, DRYM fits %s' % (
        G.show(x), fits(WETM, est2, DM), fits(DRYM, est2, DM)))
    E0 = G.e0()
    print('    W33.1\'s test on a candidate with no support at all: DRYM supports: %s; E0 supports: %s; '
          'E0\'s only component "does no work by itself": %s' % (
              does_no_work(DRYM, 'var', C, G.B0, DM)[2], does_no_work(E0, 'sun', C, G.B0, G.D)[2],
              all(does_no_work(E0, 'sun', C, G.B0, G.D)[:2])))


def part_b():
    rule('(b) look different, claim the same: two steps against one, at a place no admitted change reaches')
    B = (0, 1)
    ports = {'x': B, 'y': B, 'z': B}
    idr = frozenset({(0, 0), (1, 1)})
    D = Target(Org('chain', ports, {'a': (('x', 'y'), idr), 'b': (('y', 'z'), idr)}), 'z')
    C = [{'x': 0}, {'x': 1}]
    b0 = {'x': 0}
    ADM2 = C + [{'x': v, 'y': w} for v in B for w in B]      # (b'): edits that set y are admitted too
    two = Cand('two steps', Org('two', ports, {'k1': (('x', 'y'), idr), 'k2': (('y', 'z'), idr)}), 'z',
               lambda x: dict(x), lambda z: dict(z),
               {'k1': ({'a'}, {'x': 'x', 'y': 'y'}), 'k2': ({'b'}, {'y': 'y', 'z': 'z'})}, {'k1', 'k2'}, 'p')
    one = Cand('one step', Org('one', {'x': B, 'z': B}, {'k': (('x', 'z'), idr)}), 'z',
               lambda x: {p: v for p, v in x.items() if p == 'x'}, lambda z: {'x': z['x'], 'z': z['z']},
               {'k': ({'a', 'b'}, {'x': 'x', 'z': 'z'})}, {'k'}, 'p')
    est = {key(x): ('ans', D.ans(x)) for x in C}
    sh = lambda x: ','.join('%s=%d' % kv for kv in sorted(x.items()))
    report('(b) admitted changes: set x only (C = every admitted change)', two, one, C, C, D, est, b0, sh)
    print('    is any admitted pair one at which they conflict (a finer contract to remedy it)? %s' %
          any(conflict_p(two, one, x, D)[0] for x in C))
    report("(b') edits that set y are admitted too (outside C)", two, one, C, ADM2, D, est, b0, sh, do4=False)
    print("    conflict pairs outside C: %s" % [sh(x) for x in ADM2 if 'y' in x and conflict_p(two, one, x, D)[0]])


def part_c():
    rule('(c) a recoding: the variety effect written 0 <-> 1')
    GOOD = G.emb1('E_good', G.EARLY)
    flip = {0: 1, 1: 0}
    org = GOOD.org
    comps = {}
    for c, (fp, rel) in org.comps.items():
        i = fp.index('ovr')
        comps[c] = (fp, frozenset(tuple(flip[v] if j == i else v for j, v in enumerate(t)) for t in rel))
    rorg = Org('recoded', org.ports, comps)

    def tau(x):
        ex = GOOD.tau(x)
        if 'ovr' in ex:
            ex['ovr'] = flip[ex['ovr']]
        return ex
    pi = lambda z: dict(GOOD.pi(z), ovr=flip[z['ovrD']])
    REC_V = VCand('E_good recoded (value-map translation)', rorg, 'first', tau, pi, GOOD.anchors, GOOD.gamma, 'p',
                  vmap={'ovr': flip})
    REC_R = Cand('E_good recoded (rename-only translation)', rorg, 'first', tau, pi, GOOD.anchors, GOOD.gamma, 'p')
    C = list(G.SETTINGS)
    FINE = C + [dict(x, ovrD=o) for x in G.SETTINGS for o in (0, 1)]
    est = {key(x): ('ans', G.D.ans(x)) for x in (G.B0, G.SHADE, G.FSTAR)}
    for R in (REC_V, REC_R):
        report('E_good vs %s (admitted: the 48 pairs of the finer contract)' % R.name, GOOD, R, C, FINE, G.D, est, G.B0, G.show,
               do4=False)


def part_d():
    rule('(d) a duplicate: the variety component stated twice')
    GOOD = G.emb1('E_good', G.EARLY)
    org = GOOD.org
    comps = dict(org.comps)
    comps['var2'] = org.comps['var']
    anchors = dict(GOOD.anchors)
    anchors['var2'] = GOOD.anchors['var']
    DUP = Cand('E_good + var stated twice', Org('dup', org.ports, comps), 'first', GOOD.tau, GOOD.pi, anchors,
               GOOD.gamma | {'var2'}, 'p')
    C = list(G.SETTINGS)
    est = {key(x): ('ans', G.D.ans(x)) for x in (G.B0, G.SHADE, G.FSTAR)}
    add, rem, Sup = does_no_work(DUP, 'var2', C, G.B0, G.D)
    print('    W33.1\'s test on var2: addition half=%s removal half=%s  supports: %s' % (
        add, rem, ', '.join('{%s}' % ','.join(sorted(W)) for W in sorted(Sup, key=lambda W: (len(W), sorted(W))))))
    report('E_good vs the duplicate', GOOD, DUP, C, C, G.D, est, G.B0, G.show)


def part_e():
    rule('(e) the tilt against its own coarsening ("the season is fixed by place and half"), world question')
    D = S.D
    T = S.tilt('p_world')
    rel = frozenset((p, h, S.SEAS[S.LAT[p] * S.SG[h]]) for p in S.PLACES for h in S.HALVES)
    COARSE = Cand('coarse tilt', Org('coarse', {'place': S.PLACES, 'half': S.HALVES, 'season': S.SEASONS},
                                     {'rule': (('place', 'half', 'season'), rel)}), 'season',
                  lambda x: {p: v for p, v in x.items() if p in ('place', 'half')},
                  lambda z: {'place': z['place'], 'half': z['half'], 'season': z['season']},
                  {'rule': ({'dexp', 'dins', 'dseason'}, {'place': 'place', 'half': 'half', 'season': 'season'})},
                  {'rule'}, 'p_world')
    C = list(S.PAIRS)
    SHADE = [dict(x, ins=v) for x in S.PAIRS for v in S.V3]
    est = {key(x): ('ans', D.ans(x)) for x in S.GREEK + S.SOUTH}
    report('(e1) admitted: place and half only', T, COARSE, C, C, D, est, S.B0, S.show, space='functional')
    report('(e2) shading (sets ins) admitted too, outside C', T, COARSE, C, C + SHADE, D, est, S.B0, S.show,
           space='functional', do4=False)


def part_f():
    rule('(f) residual of the 03b repair: two compatible partial claims, each exact about one link, both true')
    B = (0, 1)
    ports = {'x': B, 'w': B, 'y': B, 'z': B}
    idr = frozenset({(0, 0), (1, 1)})
    XOR = frozenset((x, w, x ^ w) for x in B for w in B)
    W0 = frozenset({(0,)})
    D = Target(Org('chain', ports, {'dw': (('w',), W0), 'a': (('x', 'w', 'y'), XOR), 'b': (('y', 'z'), idr)}), 'z')
    C = [{'x': 0}, {'x': 1}]
    b0 = {'x': 0}
    P = Cand('P: link a exact + whole step', Org('P', ports, {'bw': (('w',), W0), 'kA': (('x', 'w', 'y'), XOR),
                                                           'kAB': (('x', 'z'), idr)}), 'z',
             lambda x: dict(x), lambda z: dict(z),
             {'kA': ({'a'}, {'x': 'x', 'w': 'w', 'y': 'y'}), 'kAB': ({'dw', 'a', 'b'}, {'x': 'x', 'z': 'z'})}, {'kA', 'kAB'}, 'p')
    Q = Cand('Q: link b exact + whole step', Org('Q', ports, {'bw': (('w',), W0), 'kB': (('y', 'z'), idr),
                                                           'kAB': (('x', 'z'), idr)}), 'z',
             lambda x: dict(x), lambda z: dict(z),
             {'kB': ({'b'}, {'y': 'y', 'z': 'z'}), 'kAB': ({'dw', 'a', 'b'}, {'x': 'x', 'z': 'z'})}, {'kB', 'kAB'}, 'p')
    est = {key(x): ('ans', D.ans(x)) for x in C}
    sh = lambda x: ','.join('%s=%d' % kv for kv in sorted(x.items()))
    ADM = C + [{'x': v, 'w': u} for v in B for u in B]
    report('P vs Q (admitted: set x, and set w outside C)', P, Q, C, ADM, D, est, b0, sh, do4=False)
    print('    in the actual world P and Q stand or fall together at every admitted pair: %s (both meet the three at: %s; '
          'both fail at: %s)' % (all(P.meets(x, D) == Q.meets(x, D) for x in ADM),
                                 [sh(x) for x in ADM if P.meets(x, D)], [sh(x) for x in ADM if not P.meets(x, D)]))
    print('    so the finer contract\'s test refutes both on the finer question, both stay accounts of p, and only a '
          'candidate exact about both links (claiming all that each claims) ends the contest.')


def main():
    print('=' * 100)
    print('A3  LOOK ALIKE BUT DIFFER; LOOK DIFFERENT BUT CLAIM THE SAME')
    print('=' * 100)
    part_a()
    part_b()
    part_c()
    part_d()
    part_e()
    part_f()


if __name__ == '__main__':
    main()
