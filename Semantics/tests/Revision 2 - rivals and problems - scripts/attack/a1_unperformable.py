#!/usr/bin/env python3
"""A1 - two rivals that conflict only at an admitted change that nobody can perform.

Target D (a planet's seasons): inputs tilt (1 = tilted, as it is; 0 = no tilt) and half (H1, H2).
Setting the tilt to 0 is physically admitted (an impact could do it) but no agent can perform it and no
history contains it. Internal: ins (warmth received, +1/0/-1); query: season.
  dins    (tilt, half, ins):  tilted -> +1 in H1, -1 in H2;  no tilt -> 0
  dseason (ins, season)
R1 "tilt":         geo = dins's relation;  seas = dseason's.
R2 "eccentricity": the same cut and anchors; geo' says that with no tilt the orbit's eccentricity still
                   gives +1 in H1 and -1 in H2.
Question p_dep  ("how do the seasons depend on the tilt?"): contract = all four pairs.
Question p_here ("why are there seasons here?"):              contract = the two tilt-1 pairs.
Established: the answers at the tilt-1 pairs (the only pairs anyone can observe).
Receipts are modelled as premise sets (K2): usable iff every premise is live, and a record reconstructed
from the claim it supports is not a receipt for it (Part IX, Receipts).
"""
from ext import Org, Target, Cand, key, fits, test_solves, verdict_fix, draft_verdict, conflict_p, rule, one_account

TILT, HALF, V3 = (1, 0), ('H1', 'H2'), (1, 0, -1)
SEAS = {1: 'summer', 0: 'none', -1: 'winter'}
PAIRS = [{'tilt': t, 'half': h} for t in TILT for h in HALF]
HERE = [x for x in PAIRS if x['tilt'] == 1]
NOTILT = [x for x in PAIRS if x['tilt'] == 0]
B0 = {'tilt': 1, 'half': 'H1'}
SG = {'H1': 1, 'H2': -1}
PORTS = {'tilt': TILT, 'half': HALF, 'ins': V3, 'season': ('summer', 'none', 'winter')}
INS = frozenset((t, h, SG[h] if t == 1 else 0) for t in TILT for h in HALF)
INS_ECC = frozenset((t, h, SG[h]) for t in TILT for h in HALF)
SEASREL = frozenset((i, SEAS[i]) for i in V3)
D = Target(Org('planet', PORTS, {'dins': (('tilt', 'half', 'ins'), INS), 'dseason': (('ins', 'season'), SEASREL)}), 'season')


def show(x):
    return 'tilt=%d,%s' % (x['tilt'], x['half'])


def cand(name, insrel, q):
    org = Org(name, PORTS, {'geo': (('tilt', 'half', 'ins'), insrel), 'seas': (('ins', 'season'), SEASREL)})
    return Cand(name, org, 'season', lambda x: dict(x), lambda z: dict(z),
                {'geo': ({'dins'}, {'tilt': 'tilt', 'half': 'half', 'ins': 'ins'}),
                 'seas': ({'dseason'}, {'ins': 'ins', 'season': 'season'})}, {'geo', 'seas'}, q)


def main():
    print('=' * 100)
    print('A1  RIVALS THAT CONFLICT ONLY AT AN ADMITTED CHANGE NOBODY CAN PERFORM')
    print('=' * 100)
    R1, R2 = cand('R1 tilt', INS, 'p_dep'), cand('R2 eccentricity', INS_ECC, 'p_dep')
    EST = {key(x): ('ans', D.ans(x)) for x in HERE}
    rule('(1) p_dep: contract = all four pairs; performable/observable: tilt=1 only')
    for c in (R1, R2):
        print('  %-16s Account(p_dep)=%-5s fits=%s' % (c.name, c.account(PAIRS, B0, D), fits(c, EST, D)))
    print('  conflict pairs:', [show(x) for x in PAIRS if conflict_p(R1, R2, x, D)[0]])
    print('  draft verdict:   ', draft_verdict(R1, R2, PAIRS, D, EST, True))
    print('  repair verdict:  ', " ".join(verdict_fix(R1, R2, PAIRS, PAIRS, D, EST, True)))
    x0 = NOTILT[0]
    print('  "a test there solves it whatever it shows" at %s: relations=%s answer=%s  (conditional: IF established)' % (
        show(x0), test_solves(R1, R2, x0, D, EST, 'all', 'full')[0], test_solves(R1, R2, x0, D, EST, 'all', 'ans')[0]))
    print('  whatever the world is at tilt=0, at most one of R1, R2 is an account of p_dep:',
          all(not (R1.meets(x0, D, r) and R2.meets(x0, D, r)) for r in D.variants(x0, 'all')))
    print('  actual world: R1 account=%s, R2 account=%s' % (R1.account(PAIRS, B0, D), R2.account(PAIRS, B0, D)))

    rule('(2) receipts for the answer at tilt=0 (no event there: every receipt is a derivation)')
    receipts = {
        'derived from R1 itself': {'premises': {'R1'}, 'claim': ('ans', 'tilt=0', 'none')},
        'derived from R2 itself': {'premises': {'R2'}, 'claim': ('ans', 'tilt=0', 'summer')},
        'derived from U (inclined-plate law, tested apart from seasons) + tilt=1 results':
            {'premises': {'U', 'obs tilt=1'}, 'claim': ('ans', 'tilt=0', 'none')},
    }
    content = {'R1': ('ans', 'tilt=0', 'none'), 'R2': ('ans', 'tilt=0', 'summer')}
    for live in ({'U', 'obs tilt=1', 'R1', 'R2'}, {'obs tilt=1', 'R1', 'R2'}):
        print('  live premises: %s' % sorted(live))
        for nm, r in receipts.items():
            circular = any(content.get(p) == r['claim'] for p in r['premises'])
            usable = r['premises'] <= live and not circular
            print('    %-78s usable=%-5s%s' % (nm, usable, '  (reconstructed from the claim it supports)' if circular else ''))
        est2 = dict(EST)
        if {'U', 'obs tilt=1'} <= live:
            for x in NOTILT:
                est2[key(x)] = ('ans', D.ans(x))
        print('    -> R1 fits %s, R2 fits %s; draft verdict: %s' % (
            fits(R1, est2, D), fits(R2, est2, D), draft_verdict(R1, R2, PAIRS, D, est2, True)))

    rule('(3) p_here: the contract omits the unperformable pairs')
    H1_, H2_ = R1.with_question('p_here'), R2.with_question('p_here')
    print('  one account on C_here (draft parenthesis):', one_account(H1_, H2_, HERE))
    print('  draft verdict:   ', draft_verdict(H1_, H2_, HERE, D, EST, True))
    print('  repair verdict:  ', " ".join(verdict_fix(H1_, H2_, HERE, PAIRS, D, EST, True)))


if __name__ == '__main__':
    main()
