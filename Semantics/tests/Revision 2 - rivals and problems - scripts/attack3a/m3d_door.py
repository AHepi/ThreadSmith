"""03a: 02's door (M3(d)), spring against a slack cable, under the fixed rival test; the contract admits
only pushes; run once with no other admitted change, once with 'hold the spring slack' admitted outside C."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'models'))
from engine import Org, Target, Cand, key, conflict, fits
DO = Org('door', {'push': (0, 1), 'sp_t': (0, 1), 'cb_t': (0, 1), 'ret': (0, 1)},
         {'dspring': (('push', 'sp_t'), frozenset({(0, 0), (1, 1)})),
          'dcable': (('push', 'cb_t'), frozenset({(0, 0), (1, 0)})),
          'ddoor': (('sp_t', 'cb_t', 'ret'), frozenset({(0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 1)}))})
DD = Target(DO, 'ret')
CD = [{'push': 0}, {'push': 1}]
idrel = frozenset({(0, 0), (1, 1)})
def door_cand(name, t_port, a_first, a_door, tau):
    org = Org(name, {'push': (0, 1), 't': (0, 1), 'ret': (0, 1)},
              {'pull': (('push', 't'), idrel), 'shut': (('t', 'ret'), idrel)})
    return Cand(name, org, 'ret', tau, lambda z, tp=t_port: {'push': z['push'], 't': z[tp], 'ret': z['ret']},
                {'pull': (a_first, {'push': 'push', 't': t_port}), 'shut': (a_door, {'t': t_port, 'ret': 'ret'})},
                {'pull', 'shut'}, 'p_door')
SPR = door_cand('spring', 'sp_t', {'dspring'}, {'ddoor', 'dcable'},
                lambda x: dict({'push': x['push']}, **({'t': x['sp_t']} if 'sp_t' in x else {})))
CAB = door_cand('cable', 'cb_t', {'dcable'}, {'ddoor', 'dspring'}, lambda x: {'push': x['push']})
def confB(c1, c2, x):
    if c1.ans(x) != c2.ans(x):
        return True
    c, a, b, n = conflict(c1, c2, x, DD, 'all')
    return c and a and b
EST = {key(x): ('ans', DD.ans(x)) for x in CD}
print('Account: spring', SPR.account(CD, CD[0], DD), 'cable', CAB.account(CD, CD[0], DD), '| fit answers:', fits(SPR, EST, DD), fits(CAB, EST, DD))
for lab, ADM in (('only pushes admitted', CD), ('also "hold the spring slack" admitted', CD + [{'push': p, 'sp_t': 0} for p in (0, 1)])):
    cf = [x for x in ADM if confB(SPR, CAB, x)]
    inC = [x for x in cf if x in CD]
    print('  %-40s conflict pairs %d (in C %d) -> %s' % (lab, len(cf), len(inC),
          ('rivals, kind (%s)' % ('i' if inC else 'ii')) if cf else 'not rivals (compatible: both could be faithful at once)'))
