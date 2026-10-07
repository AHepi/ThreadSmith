#!/usr/bin/env python3
"""A10 - does the space of target relations change a verdict in 02's models? (02 section 4 says no, citing M1 (3).)
Re-runs 02's M3 (d), the door (spring against a slack cable), with the space 'functional' (each component's
assigned port a function of its other ports) as well as 'all' (every relation), and spells out the witness."""
from ext import Org, Target, Cand, key, fits, test_solves, draft_verdict, conflict_p, rule

DO = Org('door', {'push': (0, 1), 'sp_t': (0, 1), 'cb_t': (0, 1), 'ret': (0, 1)},
         {'dspring': (('push', 'sp_t'), frozenset({(0, 0), (1, 1)})),
          'dcable': (('push', 'cb_t'), frozenset({(0, 0), (1, 0)})),
          'ddoor': (('sp_t', 'cb_t', 'ret'), frozenset({(0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 1)}))})
DD = Target(DO, 'ret')
CD = [{'push': 0}, {'push': 1}]
idrel = frozenset({(0, 0), (1, 1)})


def door_cand(name, t_port, a_first, a_door):
    org = Org(name, {'push': (0, 1), 't': (0, 1), 'ret': (0, 1)},
              {'pull': (('push', 't'), idrel), 'shut': (('t', 'ret'), idrel)})
    return Cand(name, org, 'ret', lambda x: dict(x), lambda z, tp=t_port: {'push': z['push'], 't': z[tp], 'ret': z['ret']},
                {'pull': (a_first, {'push': 'push', 't': t_port}), 'shut': (a_door, {'t': t_port, 'ret': 'ret'})},
                {'pull', 'shut'}, 'p_door')


def main():
    print('=' * 100)
    print('A10  THE SPACE OF TARGET RELATIONS: 02\'s M3 (d) RE-RUN')
    print('=' * 100)
    SPR = door_cand('spring', 'sp_t', {'dspring'}, {'ddoor', 'dcable'})
    CAB = door_cand('cable', 'cb_t', {'dcable'}, {'ddoor', 'dspring'})
    est = {key(x): ('ans', DD.ans(x)) for x in CD}
    x1 = {'push': 1}
    for sp in ('all', 'functional'):
        print('  space %-10s conflict at push=1: %-5s  draft verdict: %-26s test at push=1 sure to solve (relations): %s' % (
            sp, conflict_p(SPR, CAB, x1, DD, sp)[0], draft_verdict(SPR, CAB, CD, DD, est, True, sp),
            test_solves(SPR, CAB, x1, DD, est, sp, 'full')[0]))
    wit = [r for r in DD.variants(x1, 'all') if SPR.meets(x1, DD, r) and CAB.meets(x1, DD, r)]
    print('  target relations at push=1 under which both meet (space all): %d; the first:' % len(wit))
    for c, rel in sorted(wit[0].items()):
        print('    %-8s %s' % (c, sorted(rel)))


if __name__ == '__main__':
    main()
