#!/usr/bin/env python3
"""M1 - the gardener: rivals, a problem of kind (i), the test, correction without a record, the retreat.

Question p: the garden target D, contract C_full = every kind of spring and planting (all 16 settings),
baseline B0, query 'which bed ripens first'. Established before any rescue: the answers at the recorded
summers (B0), the shading test (SHADE) and the failed summer (FSTAR). Answers only: the gardener saw
which bed ripened first, not the variety effect itself.
"""
from engine import key, one_account, conflict, conflict_route, fits, problem, test_solves, fmt_problem
from garden import (D, SETTINGS, B0, SHADE, FSTAR, SEED, ESHADE, RAIN, show, e0, emb1, emb2, SUNMAPS,
                    EARLY, WET, WINDY, PATCH)
from itertools import product, combinations

C_FULL = list(SETTINGS)
C_REC = [B0, SHADE, FSTAR]
C_NARROW = [B0, SHADE]


def est_of(pairs):
    return {key(x): ('ans', D.ans(x)) for x in pairs}


def main():
    print('=' * 100)
    print('M1  THE GARDENER')
    print('=' * 100)
    EST0 = est_of([B0, SHADE, FSTAR])
    print('p: contract C_full (16 settings), baseline %s' % show(B0))
    print('established (answers only): %s' % ', '.join('%s -> %s' % (show(dict(k)), sorted(v[1])) for k, v in EST0.items()))
    E0 = e0()
    GOOD = emb1('E_good', EARLY)
    BAD = emb1('E_bad', WET)
    WIND = emb1('E_windy', WINDY)
    PAT = emb1('E_patch', PATCH)
    RULE = emb2('E_rule', lambda v, s: 'N' if v == 'early' else s)
    cands = [E0, GOOD, BAD, WIND, PAT, RULE]

    print()
    print('-' * 100)
    print('(1) each candidate: fits what is established? NonCircular on C_full? Account on p?')
    print('-' * 100)
    for c in cands:
        print('  %-8s fits=%-5s NC=%-5s Account(p)=%-5s %s' % (
            c.name, fits(c, EST0, D), c.nc(C_FULL, B0), c.account(C_FULL, B0, D),
            ' '.join(c.account_why(C_FULL, B0, D, show)[:4])))

    print()
    print('-' * 100)
    print('(2) the draft\'s verdict on pairs offered in place of each other, on p (space: all relations)')
    print('-' * 100)
    pairs = [(GOOD, BAD), (GOOD, WIND), (BAD, WIND), (GOOD, PAT), (GOOD, E0), (BAD, E0)]
    for a, b in pairs:
        res = problem(a, b, C_FULL, D, EST0, offered=True, space='all')
        print('  %s vs %s' % (a.name, b.name))
        print(fmt_problem(res, show))

    print()
    print('-' * 100)
    print('(3) does the space of target relations matter? conflict pairs, all relations vs functional')
    print('-' * 100)
    for a, b in pairs[:4]:
        sa = [show(x) for x in C_FULL if conflict(a, b, x, D, 'all')[0]]
        sf = [show(x) for x in C_FULL if conflict(a, b, x, D, 'functional')[0]]
        print('  %-8s vs %-8s all: %2d  functional: %2d  same set: %s' % (a.name, b.name, len(sa), len(sf), sa == sf))

    print()
    print('-' * 100)
    print('(4) E_good vs E_bad: which pairs of C separate them, and does a test there solve the problem')
    print('    "whatever it shows"? (full = the target\'s relations there are established; ans = only its answer)')
    print('-' * 100)
    for x in C_FULL:
        c, a, b, n = conflict(GOOD, BAD, x, D, 'all')
        if not c:
            continue
        sf = test_solves(GOOD, BAD, x, D, EST0, 'all', 'full')
        sa = test_solves(GOOD, BAD, x, D, EST0, 'all', 'ans')
        print('  %-24s routes: %-58s full: solves=%-5s  ans: solves=%-5s (outcomes where both still fit: %d of %d)' % (
            show(x), '; '.join(conflict_route(GOOD, BAD, x)), sf[0], sa[0], sa[1], sa[2]))

    print()
    print('-' * 100)
    print('(5) the seed trial is run: the target\'s answer at %s is established' % show(SEED))
    print('-' * 100)
    EST1 = dict(EST0)
    EST1.update(est_of([SEED]))
    for c in cands:
        print('  %-8s fits=%s' % (c.name, fits(c, EST1, D)))
    res = problem(GOOD, BAD, C_FULL, D, EST1, offered=True)
    print('  E_good vs E_bad after the test:')
    print(fmt_problem(res, show))

    print()
    print('-' * 100)
    print('(6) W60.1 "a failed answer stays failed": test harness over 1,041 candidates for p')
    print('    (Emb-1: 4 sun\' maps x all 256 predicates on V,W,Wi; Emb-2: all 16 rules on V,Sun; E0).')
    print('    The harness only tests the universal claim; the draft\'s claim itself lists nothing.')
    print('-' * 100)
    harness = [E0]
    cfgs = list(product(('late', 'early'), ('dry', 'wet'), ('calm', 'windy')))
    for g in SUNMAPS:
        for outs in product((0, 1), repeat=8):
            tab = dict(zip(cfgs, outs))
            harness.append(emb1('E1[%s,%s]' % (g, ''.join(map(str, outs))), lambda v, w, wi, t=tab: t[(v, w, wi)], g=g))
    for outs in product(('N', 'S'), repeat=4):
        tab = dict(zip(product(('late', 'early'), ('S', 'N')), outs))
        harness.append(emb2('E2[%s]' % ''.join(outs), lambda v, s, t=tab: t[(v, s)]))
    y_bad = frozenset({'S'})                                   # E0's answer at the failed summer
    others = [x for x in C_FULL if key(x) not in (key(B0), key(FSTAR))]
    contracts = [[B0, FSTAR] + list(s) for r in range(0, 3) for s in combinations(others[:6], r)]
    rep = [c for c in harness if c.ans(FSTAR) == y_bad]
    viol_fit = [c.name for c in rep if fits(c, EST0, D)]
    viol_acc = [c.name for c in rep if any(c.account(K, B0, D) for K in contracts)]
    only_f = {key(FSTAR): ('ans', D.ans(FSTAR))}
    kept = [c for c in harness if c.ans(FSTAR) == D.ans(FSTAR)]
    excl_by_f = [c.name for c in kept if not fits(c, only_f, D)]
    print('  candidates answering S at the failed summer (repeat the failed answer): %d' % len(rep))
    print('    of these, fit what is established: %d   are an account on any of %d contracts holding it: %d' % (
        len(viol_fit), len(contracts), len(viol_acc)))
    print('  candidates answering N there: %d; excluded by the failed-summer result alone: %d' % (len(kept), len(excl_by_f)))
    fit0 = [c for c in harness if fits(c, EST0, D)]
    early_S = [x for x in C_FULL if x['V'] == 'early' and x['Sun'] == 'S']
    rep_else = [c for c in fit0 if any(c.ans(x) == frozenset({'S'}) for x in early_S)]
    print('  LIMIT (not claimed by W60.1): candidates that fit and repeat E0\'s error at another early/sunS setting: %d of %d' % (
        len(rep_else), len(fit0)))
    ex = [c for c in rep_else if c.name.startswith('E1[id')][:1]
    for c in ex:
        at = [show(x) for x in early_S if c.ans(x) == frozenset({'S'})]
        print('    e.g. %s, wrong as E0 at %s' % (c.name, ', '.join(at)))
        res = problem(GOOD, c, C_FULL, D, EST0, offered=True)
        print('    offered in place of E_good ->', res['verdict'], '; conflict pairs:', len(res.get('conflicts', [])))
    fit1 = [c for c in harness if fits(c, EST1, D)]
    rep1 = [c for c in fit1 if any(c.ans(x) == frozenset({'S'}) for x in early_S)]
    print('  after the seed trial: fit %d; still repeating E0\'s error somewhere untested: %d; at the seed trial: %d' % (
        len(fit1), len(rep1), sum(1 for c in fit1 if c.ans(SEED) == frozenset({'S'}))))

    print()
    print('-' * 100)
    print('(7) the retreat: "my explanation only covered the summers seen" (contract C_narrow = {B0, SHADE})')
    print('-' * 100)
    E0n = e0(question="p' (C_narrow)")
    print('  E0 for p\': Account = %s' % E0n.account(C_NARROW, B0, D))
    print('  E0 for p : Account = %s  (%s);  fits what is established = %s' % (
        E0.account(C_FULL, B0, D), ' '.join(E0.account_why(C_FULL, B0, D, show)[:3]), fits(E0, EST0, D)))
    res = problem(GOOD, E0n, C_FULL, D, EST0, offered=True)
    print('  E0-for-p\' offered in place of E_good-for-p ->', res['verdict'])
    res = problem(GOOD, E0, C_FULL, D, EST0, offered=True)
    print('  E0 offered again for p, in place of E_good ->', res['verdict'])
    Kf = [K for K in contracts if any(key(x) == key(FSTAR) for x in K)]
    print('  E0 an account on any of the %d contracts holding the failed summer? %s' % (
        len(Kf), any(E0.account(K, B0, D) for K in Kf)))
    print('  E0 an account on the narrowed contract, where the failed summer is omitted? %s  (a different question)' %
          E0n.account(C_NARROW, B0, D))

    print()
    print('-' * 100)
    print('(8) the same pair on the record-only question p_rec (C = {B0, SHADE, FSTAR})')
    print('-' * 100)
    Gr, Br, Wr = GOOD.with_question('p_rec'), BAD.with_question('p_rec'), WIND.with_question('p_rec')
    for a, b in ((Gr, Br), (Br, Wr)):
        res = problem(a, b, C_REC, D, EST0, offered=True)
        print('  %s vs %s on p_rec' % (a.name, b.name))
        print(fmt_problem(res, show))
    print('  accounts of p_rec: E_good %s, E_bad %s, E_windy %s' % (
        Gr.account(C_REC, B0, D), Br.account(C_REC, B0, D), Wr.account(C_REC, B0, D)))
    print('  REPAIR tested: "one account" judged on every admitted setting (all 16), not on C_rec:')
    for a, b in ((Gr, Br), (Br, Wr)):
        res = problem(a, b, C_REC, D, EST0, offered=True, oa_C=C_FULL)
        print('  %s vs %s on p_rec, repaired rule' % (a.name, b.name))
        print(fmt_problem(res, show))

    print()
    print('-' * 100)
    print('(9) same-cut lemma, checked on the harness: two Emb-1 candidates (paired components, one anchor each)')
    print('    that conflict at no pair of a contract are one account on it. Contracts: C_rec and C_full.')
    print('-' * 100)
    e1 = [c for c in harness if c.name.startswith('E1[id')]
    for nm, K in (('C_rec', C_REC), ('C_full', C_FULL)):
        fitK = [c for c in e1 if fits(c, EST0, D)]
        n = viol = 0
        for i in range(len(fitK)):
            for j in range(i + 1, len(fitK)):
                a, b = fitK[i], fitK[j]
                noconf = not any(conflict(a, b, x, D, 'functional')[0] for x in K)
                if noconf:
                    n += 1
                    if not one_account(a, b, K)[0]:
                        viol += 1
        print('  %-6s pairs of fitting sun\'=id candidates with no conflict on the contract: %d; of these NOT one account: %d' % (nm, n, viol))


if __name__ == '__main__':
    main()
