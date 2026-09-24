#!/usr/bin/env python3
"""M3 - check the proposed lemma "Correction in a common family" (H*) and its stated limits
against the finite models of m1_gardener.py and m2_seasons.py.

The proposed statement (plain form):
  Let V be a declared family of edits of the later organization E1 that contains a member v0
  giving the earlier organization E0. If E0 does every job in F and fails a job f*, then
  v0 is in Pres(F) and not in Pres(F + f*), so Pres(F + f*) is strictly inside Pres(F).
  If E1 does f* and the correction only adds a block B, then B is critical for f* in E1.
  Same argument with the identity edit as witness: a narrowing that omits a job its own
  candidate fails restores a strictly larger Pres.
Limits stated with it:
  (i)   a member of Pres(F + f*) may fail another job g that E0 fails (hybrids);
  (ii)  on the same jobs, the family of E0 inside V has Pres no larger than V's (extension);
  (iii) two extensions that both do F + f* are both in Pres(F + f*); only a job one fails separates them;
  (iv)  without v0 in V the strictness is not guaranteed.
Jobs are sets of pairs (a contract); Account(E_v, job) is read as (A) on every pair of it.
"""
import random
from itertools import combinations, product
from m1_gardener import (Family, SUN_MENU, fn_menu, single_menu, SETTINGS, NS, TRUTH, show, get,
                         J_BEFORE, J_AFTER, C_FULL, C_NARROW, FSTAR, BG_SEED, B0)
import m2_seasons as m2

random.seed(24)
FULL = (1 << NS) - 1


def mask(js):
    m = 0
    for j in js:
        m |= 1 << j
    return m


def okmask(fam, v):
    prof = fam.profile(v)
    return mask(j for j in range(NS) if prof[j] == TRUTH[j])


def build(fam):
    vs = list(fam.versions())
    return vs, [okmask(fam, v) for v in vs]


def pres_idx(masks, F):
    return {i for i, m in enumerate(masks) if m & F == F}


fam0 = Family('E0', [('sun', SUN_MENU)])
E0PROF = fam0.profile(fam0.find(sun='id'))
R0 = [j for j in range(NS) if E0PROF[j] == TRUTH[j]]       # pairs E0 gets right (12)
M0 = [j for j in range(NS) if E0PROF[j] != TRUTH[j]]       # pairs E0 gets wrong (4)
MR0, MM0 = mask(R0), mask(M0)


def v0_index(fam, vs):
    want = fam.find(sun='id')                               # every added part 'off'
    return vs.index(want)


def check_lemma(fam, label, n_contracts=400):
    vs, ms = build(fam)
    i0 = v0_index(fam, vs)
    n_checked = 0
    fails = 0
    min_gap = None
    # (1) every F within the pairs E0 gets right (all 4096 subsets; a sample of 300 for large families),
    #     every single failed pair f*
    allF = [mask(Fs) for r in range(len(R0) + 1) for Fs in combinations(R0, r)]
    if len(vs) > 5000:
        allF = random.sample(allF, 300)
    for F in allF:
        if True:
            cntF = sum(1 for m in ms if m & F == F)
            for fs in M0:
                Fp = F | (1 << fs)
                cntFp = sum(1 for m in ms if m & Fp == Fp)
                n_checked += 1
                in_F = ms[i0] & F == F
                in_Fp = ms[i0] & Fp == Fp
                if not (in_F and not in_Fp and cntFp < cntF):
                    fails += 1
                gap = cntF - cntFp
                min_gap = gap if min_gap is None else min(min_gap, gap)
    # (2) f* as a whole question: random contracts that hold at least one failed pair
    for _ in range(n_contracts):
        F = mask(random.sample(R0, random.randint(0, len(R0))))
        C = mask(random.sample(range(NS), random.randint(1, NS)))
        if not C & MM0:
            C |= 1 << random.choice(M0)
        Fp = F | C
        cntF = sum(1 for m in ms if m & F == F)
        cntFp = sum(1 for m in ms if m & Fp == Fp)
        n_checked += 1
        if not ((ms[i0] & F == F) and not (ms[i0] & Fp == Fp) and cntFp < cntF):
            fails += 1
    print('  %-44s |V|=%6d  instances checked=%6d  failures of (H*)=%d  min strict gap=%d'
          % (label, len(vs), n_checked, fails, min_gap))
    return fails


def hybrids(fam, label, F, fstar_contract):
    vs, ms = build(fam)
    Fp = F | fstar_contract
    P = [i for i, m in enumerate(ms) if m & Fp == Fp]
    rest = MM0 & ~Fp
    H = [i for i in P if (~ms[i]) & rest]
    return len(P), len(H), (fam.label(vs[H[0]]) if H else '')


def extension(fam, label):
    vs, ms = build(fam)
    v0set = {i for i, v in enumerate(vs)
             if all(fam.menus[c][v[c]][0] == 'off' for c in range(1, len(fam.names)))}
    strict = equal = bad = 0
    for F in range(1 << NS):
        P = {i for i, m in enumerate(ms) if m & F == F}
        P0 = P & v0set
        if not P0 <= P:
            bad += 1
        elif P0 < P:
            strict += 1
        else:
            equal += 1
    print('  %-44s all 65536 job sets F: Pres_V0(F) inside Pres_V(F) always? %s   strictly larger for %d, equal for %d'
          % (label, bad == 0, strict, equal))


def main():
    print('=' * 100)
    print('M3  THE PROPOSED LEMMA (H*) AND ITS LIMITS, CHECKED ON THE MODELS')
    print('=' * 100)
    print('E0 right at %d pairs, wrong at %d: %s' % (len(R0), len(M0), ', '.join(show(SETTINGS[j]) for j in M0)))

    MV, MW, MWWi = fn_menu(('V',)), fn_menu(('W',)), fn_menu(('W', 'Wi'))
    families = [
        ('U1 = sun x var[V] x rain[W] x exc[single]', Family('U1', [('sun', SUN_MENU), ('var', MV), ('rain', MW), ('exc', single_menu())])),
        ('U2 = sun x var[V] x rain[W,Wi] x exc[single]', Family('U2', [('sun', SUN_MENU), ('var', MV), ('rain', MWWi), ('exc', single_menu())])),
        ('E_good rich = sun x var[V,W,Wi]', Family('g3', [('sun', SUN_MENU), ('var', fn_menu(('V', 'W', 'Wi')))])),
        ('redescribed: sun x rainA[W] x rainB[W]', Family('split', [('sun', SUN_MENU), ('rainA', MW), ('rainB', MW)])),
        ('redescribed x10: sun x rain1..rain5[W]', Family('split5', [('sun', SUN_MENU)] + [('rain%d' % k, MW) for k in range(1, 6)])),
    ]
    grid_ports = [('V',), ('V', 'Wi'), ('V', 'Sun'), ('V', 'W', 'Wi')]
    grid_bad = [('W',), ('W', 'Wi'), ('W', 'Sun'), ('W', 'Wi', 'Sun')]
    for gp in grid_ports:
        for bp in grid_bad:
            f = Family('grid', [('sun', SUN_MENU), ('var', fn_menu(gp)), ('rain', fn_menu(bp))])
            if f.size() <= 70000:
                families.append(('grid sun x var[%s] x rain[%s]' % ('+'.join(gp), '+'.join(bp)), f))

    print('\n' + '-' * 100)
    print('(1) (H*): every F that E0 does, every f* that E0 fails (single failed pairs, and random whole contracts')
    print('    holding a failed pair). Strict containment with the embedded E0 as witness?')
    print('-' * 100)
    total = 0
    for label, fam in families:
        total += check_lemma(fam, label, n_contracts=200 if fam.size() > 5000 else 400)
    print('  TOTAL failures of (H*) across all families: %d' % total)

    print('\n' + '-' * 100)
    print('(1b) Counts on the gardener\'s own jobs (F = J_before, f* = the failed summer): strict in every family,')
    print('     while the SIZE of the gap depends on the menus')
    print('-' * 100)
    for label, fam in families[:5]:
        vs, ms = build(fam)
        F, Fp = mask(J_BEFORE), mask(J_AFTER)
        a = sum(1 for m in ms if m & F == F)
        b = sum(1 for m in ms if m & Fp == Fp)
        print('  %-44s |Pres(J_before)|=%5d  |Pres(J_after)|=%5d' % (label, a, b))

    print('\n' + '-' * 100)
    print('(iv) NEGATIVE CONTROLS: drop a hypothesis and strictness is no longer guaranteed')
    print('-' * 100)
    MV_noff = [it for it in MV if it[0] != 'off']
    famN = Family('noV0', [('sun', SUN_MENU), ('var', MV_noff)])
    vs, ms = build(famN)
    F, Fp = mask(J_BEFORE), mask(J_AFTER)
    a = {i for i, m in enumerate(ms) if m & F == F}
    b = {i for i, m in enumerate(ms) if m & Fp == Fp}
    print('  no v0 (var menu without "off"): Pres(J_before)=%s  Pres(J_after)=%s  strict? %s'
          % ([famN.label(vs[i]) for i in a], [famN.label(vs[i]) for i in b], b < a))
    famG = Family('gv', [('sun', SUN_MENU), ('var', MV)])
    vs, ms = build(famG)
    i0 = v0_index(famG, vs)
    # hypothesis "E0 does F" dropped: F already holds a failed pair (a job added after an earlier correction)
    F = mask(J_BEFORE + [M0[0]])
    Fp = F | (1 << M0[1])
    a = {i for i, m in enumerate(ms) if m & F == F}
    b = {i for i, m in enumerate(ms) if m & Fp == Fp}
    print('  E0 does not do F (sun x var[V]; F = J_before + %s; f* = %s): E0 in Pres(F)? %s  |Pres(F)|=%d  |Pres(F+f*)|=%d  strict? %s'
          % (show(SETTINGS[M0[0]]), show(SETTINGS[M0[1]]), ms[i0] & F == F, len(a), len(b), b < a))
    b2 = {i for i, m in enumerate(ms) if m & (mask(J_AFTER) | mask([s for s in range(NS) if get(SETTINGS[s], 'V') == 'late' and get(SETTINGS[s], 'W') == 1])) == (mask(J_AFTER) | mask([s for s in range(NS) if get(SETTINGS[s], 'V') == 'late' and get(SETTINGS[s], 'W') == 1]))}
    a2 = {i for i, m in enumerate(ms) if m & mask(J_AFTER) == mask(J_AFTER)}
    print('  a new job no member fails (sun x var[V]; wet springs with the late variety added to J_after): |Pres| %d -> %d, strict? %s  (file 00\'s non-strict case)'
          % (len(a2), len(b2), b2 < a2))
    fam = families[0][1]
    vs, ms = build(fam)
    i0 = v0_index(fam, vs)
    # a job E0 already does: (H) only, and non-strict (file 00's caveat)
    F = mask(J_AFTER)
    Fp = F | mask([s for s in range(NS) if get(SETTINGS[s], 'V') == 'late' and get(SETTINGS[s], 'W') == 1])
    a = {i for i, m in enumerate(ms) if m & F == F}
    b = {i for i, m in enumerate(ms) if m & Fp == Fp}
    print('  added job that E0 does (wet springs, late variety) on F = J_after: |Pres|=%d -> %d, strict? %s'
          % (len(a), len(b), b < a))

    print('\n' + '-' * 100)
    print('(i) HYBRIDS: members of Pres(F + f*) that fail another job E0 fails')
    print('-' * 100)
    for label, fam in families[:3]:
        n, h, ex = hybrids(fam, label, mask(J_BEFORE), 1 << FSTAR)
        n2, h2, _ = hybrids(fam, label, mask(J_BEFORE), mask(C_FULL))
        print('  %-44s f* = the failed summer: %4d in Pres, %4d hybrids %s' % (label, n, h, ('e.g. ' + ex) if ex else ''))
        print('  %-44s f* = the open question (all 16 pairs): %4d in Pres, %4d hybrids' % ('', n2, h2))

    print('\n' + '-' * 100)
    print('(ii) EXTENSION: on the same jobs, the embedded family of E0 never has the larger Pres')
    print('-' * 100)
    for label, fam in families[:3]:
        extension(fam, label)

    print('\n' + '-' * 100)
    print('(iii) GOOD AGAINST BAD in one family (U1): same witness, both kept; only a job one fails separates them')
    print('-' * 100)
    fam = families[0][1]
    vs, ms = build(fam)
    good = vs.index(fam.find(sun='id', var='early'))
    bad = vs.index(fam.find(sun='id', rain='wet'))
    patch = vs.index(fam.find(sun='id', exc='only@' + show(SETTINGS[FSTAR])))
    for nm, J in (('J_after', J_AFTER), ('J_after + seed trial', J_AFTER + BG_SEED), ('C_full', C_FULL)):
        P = pres_idx(ms, mask(J))
        print('  Pres(%-22s) |%4d|  E_good in? %-5s  E_bad in? %-5s  E_patch in? %s'
              % (nm, len(P), good in P, bad in P, patch in P))

    print('\n' + '-' * 100)
    print('NARROWING instance (identity edit as witness)')
    print('-' * 100)
    vs0, ms0 = build(fam0)
    e0 = vs0.index(fam0.find(sun='id'))
    a = pres_idx(ms0, mask(C_NARROW))
    b = pres_idx(ms0, mask(C_NARROW) | (1 << FSTAR))
    print('  E0 narrowed to the summers seen: |Pres(C_narrow)|=%d  |Pres(C_narrow + f*)|=%d  witness E0? %s'
          % (len(a), len(b), e0 in a and e0 not in b))
    print('  same set as the claim BEFORE the failure (Pres(J_before))? %s  -> the inclusion does not say whether the'
          % (a == pres_idx(ms0, mask(J_BEFORE))))
    print('     omitted job was dropped after a failure or never claimed; only the historical index says which')
    a = pres_idx(ms, mask(J_AFTER))
    b = pres_idx(ms, mask(C_FULL))
    print('  Situation 3 (E_bad confined to the recorded summers, open question dropped), U1: |Pres(J_after)|=%d'
          ' |Pres(J_after + open question)|=%d  witness E_bad? %s' % (len(a), len(b), bad in a and bad not in b))
    print('     the same inclusion has E_good\'s honest confinement to J_after inside it: E_good in both? %s'
          % (good in a and good in b))

    print('\n' + '-' * 100)
    print('COMPANION: the added block is critical for f* (B), and not critical for the old jobs')
    print('-' * 100)
    for nm, lab in (('E_good', dict(sun='id', var='early')), ('E_bad', dict(sun='id', rain='wet')),
                    ('E_patch', dict(sun='id', exc='only@' + show(SETTINGS[FSTAR])))):
        v = fam.find(**lab)
        added = [n for n in fam.names[1:] if lab.get(n, 'off') != 'off']
        full = fam.profile(v)
        rest = fam.profile(v, deleted=tuple(added))              # E1|Gamma0 = E0
        acc_full_f = full[FSTAR] == TRUTH[FSTAR]
        acc_rest_f = rest[FSTAR] == TRUTH[FSTAR]
        acc_rest_F = all(rest[j] == TRUTH[j] for j in J_BEFORE)
        acc_full_F = all(full[j] == TRUTH[j] for j in J_BEFORE)
        print('  %-8s Gamma1 support for f*? %-5s Gamma0 support for f*? %-5s -> block critical for f*: %-5s |'
              ' for J_before: Gamma1 %s, Gamma0 %s -> critical: %s'
              % (nm, acc_full_f, acc_rest_f, acc_full_f and not acc_rest_f, acc_full_F, acc_rest_F,
                 acc_full_F and not acc_rest_F))

    print('\n' + '-' * 100)
    print('M2  SEASONS: the myth amended and the tilt\'s own correction')
    print('-' * 100)
    myth = m2.Myth('amended', ['none', 'S', 'E'])
    MV2 = myth.versions()
    v0s = [v for v in MV2 if myth.dmenu[v[2]] == 'none']
    m0 = myth.find('none')
    truth_ok = lambda fam, v, xs: all(fam.ans(v, x) == m2.TRUTH[x] for x in xs)
    R = [x for x in m2.PAIRS if myth.ans(m0, x) == m2.TRUTH[x]]
    W = [x for x in m2.PAIRS if myth.ans(m0, x) != m2.TRUTH[x]]
    fails = n = 0
    for r in range(len(R) + 1):
        for Fs in combinations(R, r):
            for k in range(1, len(W) + 1):
                for Ws in combinations(W, k):
                    P = [v for v in MV2 if truth_ok(myth, v, Fs)]
                    Pp = [v for v in MV2 if truth_ok(myth, v, Fs + Ws)]
                    n += 1
                    if not (m0 in P and m0 not in Pp and len(Pp) < len(P)):
                        fails += 1
    print('  myth, law family (d in none,S,E): instances %d, failures of (H*) %d' % (n, fails))
    P = [v for v in MV2 if truth_ok(myth, v, m2.J_GREEK)]
    Pp = [v for v in MV2 if truth_ok(myth, v, m2.J_SAILOR)]
    hyb = [v for v in Pp if any(myth.ans(v, x) == myth.ans(m0, x) for x in W if x not in m2.J_SAILOR)]
    print('  J_greek -> J_sailor: |Pres| %d -> %d, witness M0 excluded? %s; hybrids keeping M0\'s error at the equator: %d of %d'
          % (len(P), len(Pp), m0 in P and m0 not in Pp, len(hyb), len(Pp)))
    tilt = m2.Tilt('law', m2.G_LAW, m2.H_LAW, False)
    esc = tilt.find('t+1', 'flat/escape', 'direct')
    TV = tilt.versions()
    Rt = [x for x in m2.PAIRS if tilt.ans(esc, x) == m2.TRUTH[x]]
    Wt = [x for x in m2.PAIRS if tilt.ans(esc, x) != m2.TRUTH[x]]
    fails = n = 0
    for r in range(len(Rt) + 1):
        for Fs in combinations(Rt, r):
            for k in range(1, len(Wt) + 1):
                for Ws in combinations(Wt, k):
                    P = [v for v in TV if truth_ok(tilt, v, Fs)]
                    Pp = [v for v in TV if truth_ok(tilt, v, Fs + Ws)]
                    n += 1
                    if not (esc in P and esc not in Pp and len(Pp) < len(P)):
                        fails += 1
    P = [v for v in TV if truth_ok(tilt, v, m2.J_GREEK)]
    Pp = [v for v in TV if truth_ok(tilt, v, m2.J_SAILOR)]
    print('  tilt, law family, escape version as v0: instances %d, failures %d; J_greek -> J_sailor |Pres| %d -> %d'
          % (n, fails, len(P), len(Pp)))
    print('  myth against tilt: no member of either family gives the other organization -> (H*) has no instance')


if __name__ == '__main__':
    main()
