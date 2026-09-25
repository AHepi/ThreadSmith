#!/usr/bin/env python3
"""M3 - redescription and cutting.

(a) One explanation in two wordings: E_good, and E_good with its variety effect called 'boost' and its
    components renamed. Expected: one account (Derivation 2), not rivals, no problem.
(b) Two cuttings, NOT one account under revised Derivation 2's premise (different subnetworks, same
    answers): the good rescue as a mechanism (Emb-1: two components, anchored to dvar and dfirst) and
    as a changed rule (Emb-2: one component anchored to {dvar, dfirst}). Both are accounts on C_full.
    A finer contract adds edits that set the variety effect directly (ovrD := 0 or 1).
(c) Same answers at every pair of C, one anchor, different relations: var fires on 'early' against
    var fires on 'early and the south bed sunny'. Tests the REASON's inference "they give one answer at
    every pair, so they conflict at no pair of C".
(d) Two cuttings with the same answers where one is not an account: a door returned by a spring,
    and a rival that says a (slack) cable returns it. Kind (ii), yet a test inside C can solve it.
"""
from engine import Org, Target, Cand, key, one_account, conflict, conflict_route, fits, problem, test_solves, fmt_problem
from garden import D, SETTINGS, B0, SHADE, FSTAR, ESHADE, show, emb1, emb2, EARLY

C_FULL = list(SETTINGS)
C_FINE = C_FULL + [dict(x, ovrD=o) for x in SETTINGS for o in (0, 1)]


def est_of(pairs, T=D):
    return {key(x): ('ans', T.ans(x)) for x in pairs}


def main():
    print('=' * 100)
    print('M3  REDESCRIPTION AND CUTTING')
    print('=' * 100)
    EST0 = est_of([B0, SHADE, FSTAR])
    GOOD = emb1('E_good', EARLY)
    REN = emb1('E_good renamed', EARLY, effect='boost', names=('suncomp', 'boostcomp'))
    RULE = emb2('E_rule', lambda v, s: 'N' if v == 'early' else s)

    print()
    print('-' * 100)
    print('(a) one explanation, two wordings')
    print('-' * 100)
    print(fmt_problem(problem(GOOD, REN, C_FULL, D, EST0, offered=True), show))

    print()
    print('-' * 100)
    print('(b) two cuttings with one answer profile: mechanism (Emb-1) against rule (Emb-2), on p = C_full')
    print('-' * 100)
    print('  Account on C_full: E_good %s, E_rule %s; answers agree at every pair: %s' % (
        GOOD.account(C_FULL, B0, D), RULE.account(C_FULL, B0, D), all(GOOD.ans(x) == RULE.ans(x) for x in C_FULL)))
    print('  not offered in place of each other:')
    print(fmt_problem(problem(GOOD, RULE, C_FULL, D, EST0, offered=False), show))
    print('  offered in place of each other:')
    print(fmt_problem(problem(GOOD, RULE, C_FULL, D, EST0, offered=True), show))
    print('  the finer contract (adds ovrD := 0/1 at every setting, %d pairs):' % len(C_FINE))
    print('    Account: E_good %s ; E_rule %s  %s' % (
        GOOD.account(C_FINE, B0, D), RULE.account(C_FINE, B0, D), ' '.join(RULE.account_why(C_FINE, B0, D, show)[:3])))
    G2, R2 = GOOD.with_question('p_fine'), RULE.with_question('p_fine')
    ESTF = dict(EST0)
    print('    on p_fine, offered in place of each other:')
    res = problem(G2, R2, C_FINE, D, ESTF, offered=True, space='functional')
    print('    VERDICT: %s; conflict pairs: %d (all at edits that set ovrD: %s)' % (
        res['verdict'], len(res.get('conflicts', [])), all('ovrD' in x for x, _, _ in res.get('conflicts', []))))

    print()
    print('-' * 100)
    print('(c) one answer at every pair, one anchor, different relations')
    print('-' * 100)
    VP = ('V', 'W', 'Wi', 'Sun')
    A_ = emb1('var[early]', lambda v, w, wi, s: int(v == 'early'), var_ports=VP)
    B_ = emb1('var[early & sunS]', lambda v, w, wi, s: int(v == 'early' and s == 'S'), var_ports=VP)
    print('  answers agree at all 16 pairs: %s ; Account on C_full: %s / %s' % (
        all(A_.ans(x) == B_.ans(x) for x in C_FULL), A_.account(C_FULL, B0, D), B_.account(C_FULL, B0, D)))
    res = problem(A_, B_, C_FULL, D, EST0, offered=True)
    print(fmt_problem(res, show))
    print('  test at %s: full solves=%s ; answer-only solves=%s' % (
        show(ESHADE), test_solves(A_, B_, ESHADE, D, EST0, 'all', 'full')[0], test_solves(A_, B_, ESHADE, D, EST0, 'all', 'ans')[0]))

    print()
    print('-' * 100)
    print('(d) the door: a spring, and a slack cable offered in its place')
    print('-' * 100)
    DO = Org('door', {'push': (0, 1), 'sp_t': (0, 1), 'cb_t': (0, 1), 'ret': (0, 1)},
             {'dspring': (('push', 'sp_t'), frozenset({(0, 0), (1, 1)})),
              'dcable': (('push', 'cb_t'), frozenset({(0, 0), (1, 0)})),
              'ddoor': (('sp_t', 'cb_t', 'ret'), frozenset({(0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 1)}))})
    DD = Target(DO, 'ret')
    CD = [{'push': 0}, {'push': 1}]
    b0 = {'push': 0}
    idrel = frozenset({(0, 0), (1, 1)})

    def door_cand(name, t_port, a_first, a_door):
        org = Org(name, {'push': (0, 1), 't': (0, 1), 'ret': (0, 1)},
                  {'pull': (('push', 't'), idrel), 'shut': (('t', 'ret'), idrel)})
        return Cand(name, org, 'ret', lambda x: dict(x),
                    lambda z, tp=t_port: {'push': z['push'], 't': z[tp], 'ret': z['ret']},
                    {'pull': (a_first, {'push': 'push', 't': t_port}), 'shut': (a_door, {'t': t_port, 'ret': 'ret'})},
                    {'pull', 'shut'}, 'p_door')

    SPR = door_cand('spring', 'sp_t', {'dspring'}, {'ddoor', 'dcable'})
    CAB = door_cand('cable', 'cb_t', {'dcable'}, {'ddoor', 'dspring'})
    ESTD = {key(x): ('ans', DD.ans(x)) for x in CD}
    print('  Account on the door question: spring %s ; cable %s  (%s)' % (
        SPR.account(CD, b0, DD), CAB.account(CD, b0, DD), ' '.join(CAB.account_why(CD, b0, DD, lambda x: 'push=%d' % x['push']))))
    res = problem(SPR, CAB, CD, DD, ESTD, offered=True)
    print(fmt_problem(res, lambda x: 'push=%d' % x['push']))
    x1 = {'push': 1}
    print('  a test at push=1: sure to solve, whatever it shows? relations established: %s ; only the answer: %s' % (
        test_solves(SPR, CAB, x1, DD, ESTD, 'all', 'full')[0], test_solves(SPR, CAB, x1, DD, ESTD, 'all', 'ans')[0]))
    E2 = dict(ESTD)
    E2[key(x1)] = ('full', None)
    print('  with the actual relations at push=1 established: spring fits %s, cable fits %s' % (fits(SPR, E2, DD), fits(CAB, E2, DD)))


if __name__ == '__main__':
    main()
