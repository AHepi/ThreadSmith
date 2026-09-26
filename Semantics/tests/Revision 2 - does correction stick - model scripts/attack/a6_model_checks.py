#!/usr/bin/env python3
"""A6 - checks of the scripts behind 02 and 03 (ratchet/models), read-only.

(a) m3 negative control "a new job no member fails" is run with F = J_after, which already holds f*.
(b) 02 CX2/CX3: rows whose two port lists are the same set are one family under two names.
(c) m3 check (1): the witness's profile is E0's by construction, so no failure was possible.
(d) m1/m3 delete an override by switching it off; Part II deletes by imposing the full relation.
    Does that change any NonCircular verdict in m1 (i)?  (The companion is in a3.)
(e) 03 s1(2): "Only the seed trial ... or the open question ... separates them."
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'models'))
from itertools import combinations
import m1_gardener as m1
from pl import (pred_menu, SUN4, family, count, J_BEFORE, J_AFTER, RAIN, SEED, mask, SINGLE, M0, R0, FULLM, NS,
                answers, TRUTH, SUN_ID)


def part_a():
    print('-' * 100)
    print('(a) m3 control "a new job no member fails" (sun x var[V]; wet springs with the usual planting)')
    print('-' * 100)
    fam = family(SUN4, [pred_menu(('V',))])
    from pl import SETTINGS, get
    wet_late = mask(i for i, s in enumerate(SETTINGS) if get(s, 'V') == 0 and get(s, 'W') == 1)
    e0_does = lambda F: (F & M0) == 0
    for nm, F in (('m3 as run: F = J_after', J_AFTER), ('clean: F = J_before', J_BEFORE)):
        a, b = count(fam, F), count(fam, F | wet_late)
        print('  %-26s E0 does F? %-5s E0 does the added job? %-5s |Pres| %d -> %d  strict? %s'
              % (nm, e0_does(F), e0_does(wet_late), a, b, b < a))
    print('  -> as run, two hypotheses are dropped at once (E0 already fails f* in F); the clean control')
    print('     drops one and still gives the non-strict case.')


def part_b():
    print()
    print('-' * 100)
    print('(b) 02 CX2 and CX3: are the "good" and "bad" families different families?')
    print('-' * 100)
    from pl import SETTINGS
    for gp, bp in ((('V', 'W'), ('W', 'V')), (('V', 'W', 'Wi'), ('W', 'V', 'Wi')), (('V',), ('W',)), (('V', 'Wi'), ('W', 'Wi'))):
        g, b = set(pred_menu(gp)), set(pred_menu(bp))
        print('  good reads %-8s bad reads %-8s same set of override predicates? %s' % ('+'.join(gp), '+'.join(bp), g == b))
    wet = mask(i for i, s in enumerate(SETTINGS) if s[0] == 1)
    early = mask(i for i, s in enumerate(SETTINGS) if s[2] == 1)
    for ports in (('V', 'W', 'Wi'), ('V', 'W')):
        menu = set(pred_menu(ports))
        print('  "good" family var[%s] contains the rain rescue (fires iff wet)? %s ; the variety rescue? %s'
              % ('+'.join(ports), wet in menu, early in menu))
    print('  -> CX2\'s 4:4 (V+W vs W+V) and 64:64 rows compare a family with itself; CX3\'s "good:V+W+Wi" row')
    print('     is a family holding BOTH rescues, set against one holding only the bad one.')


def part_c():
    print()
    print('-' * 100)
    print('(c) m3 check (1): is a failure possible under its encoding?')
    print('-' * 100)
    fam = family(SUN4, [pred_menu(('V',)), pred_menu(('W',)), SINGLE])
    v0 = [m for k, m in fam if k == (1, 0, 0, 0)]
    print('  okmask of v0 (sun=id, all added parts off) == pairs E0 gets right: %s' % (v0[0] == R0))
    print('  so for every F inside R0 and every f* in M(E0): v0 in Pres(F) and not in Pres(F+f*), by construction.')
    print('  The ~274,000 instances test the encoding, not the lemma; the lemma\'s content is the equality above,')
    print('  which a1 shows fails under full (E) with one interpretation.')


def part_d():
    print()
    print('-' * 100)
    print('(d) m1 (i) NonCircular with Part II deletion (override deleted -> its port free) instead of "off"')
    print('-' * 100)

    def profile_full(fam, v, deleted):
        base = fam.profile(v, deleted=deleted)       # overrides deleted -> off, sun deleted -> None
        if any(n != 'sun' for n in deleted):
            out = []
            for j in range(m1.NS):
                if base[j] is None or base[j] == 'N':
                    out.append(base[j])
                else:                                # a free override port could send N here
                    out.append(None)
            return tuple(out)
        return base

    def nc_full(fam, v, contract):
        if m1.B0 not in contract:
            return False
        active = ['sun'] + [n for c, n in enumerate(fam.names) if c > 0 and fam.menus[c][v[c]][0] != 'off']
        prof = fam.profile(v)
        for r in range(1, len(active) + 1):
            for G in combinations(active, r):
                dp = profile_full(fam, v, G)
                for x in contract:
                    if prof[x] != prof[m1.B0]:
                        if dp[x] is None or dp[m1.B0] is None or dp[x] == dp[m1.B0]:
                            return True
        return False

    fam0 = m1.Family('E0', [('sun', m1.SUN_MENU)])
    MV, MW = m1.fn_menu(('V',)), m1.fn_menu(('W',))
    fg = m1.Family('g', [('sun', m1.SUN_MENU), ('var', MV)])
    fb = m1.Family('b', [('sun', m1.SUN_MENU), ('rain', MW)])
    fp = m1.Family('p', [('sun', m1.SUN_MENU), ('exc', m1.single_menu())])
    rows = [('E0', fam0, fam0.find(sun='id'), m1.J_BEFORE), ('E0', fam0, fam0.find(sun='id'), m1.J_AFTER),
            ('E_good', fg, fg.find(sun='id', var='early'), m1.C_FULL), ('E_good', fg, fg.find(sun='id', var='early'), m1.J_AFTER),
            ('E_bad', fb, fb.find(sun='id', rain='wet'), m1.C_FULL), ('E_bad', fb, fb.find(sun='id', rain='wet'), m1.J_AFTER),
            ('E_patch', fp, fp.find(sun='id', exc='only@' + m1.show(m1.SETTINGS[m1.FSTAR])), m1.J_AFTER),
            ('E_narrow', fam0, fam0.find(sun='id'), m1.C_NARROW), ('E_narrow_bare', fam0, fam0.find(sun='id'), m1.C_NARROW_BARE)]
    changed = 0
    for nm, fam, v, C in rows:
        a, _ = m1.noncircular(fam, v, C)
        b = nc_full(fam, v, C)
        changed += a != b
        print('  %-14s |C|=%2d  NonCirc (m1, off)=%-5s  NonCirc (Part II)=%-5s' % (nm, len(C), a, b))
    print('  verdicts changed: %d' % changed)


def part_e():
    print()
    print('-' * 100)
    print('(e) which added jobs separate the good rescue from the wet-spring rescue on the record (U1)?')
    print('-' * 100)
    from pl import SETTINGS
    U1 = family(SUN4, [pred_menu(('V',)), pred_menu(('W',)), SINGLE])
    MVl, MWl = pred_menu(('V',)), pred_menu(('W',))
    gi = MVl.index(mask(i for i, s in enumerate(SETTINGS) if s[2] == 1))
    bi = MWl.index(mask(i for i, s in enumerate(SETTINGS) if s[0] == 1))
    kg, kb = (1, gi, 0, 0), (1, 0, bi, 0)
    ok = dict(U1)
    for i in range(NS):
        F = J_AFTER | (1 << i)
        g_in, b_in = ok[kg] & F == F, ok[kb] & F == F
        if g_in != b_in:
            from pl import show
            print('  J_after + %-24s good in? %-5s bad in? %-5s' % (show(i), g_in, b_in))
    print('  -> four single summers separate them: the early variety in a dry spring (the seed trial and its windy')
    print('     twin) and a wet spring with the usual planting (calm or windy); "only the seed trial or the open')
    print('     question" is too narrow.')


def part_f():
    print()
    print('-' * 100)
    print('(f) 02 CX4 / 03 s2 third control, with a job read as a QUESTION (03 edit (a)): baseline + pairs')
    print('-' * 100)
    from fe import emb1_member, B0 as b0, SHADE as sh, FSTAR as fs, RAIN as rn, pres as fpres, PRED_V, SUNMAPS
    fam = [emb1_member(g, p) for g in SUNMAPS for p in PRED_V]
    base = [[b0, sh], [b0, fs]]
    for nm, extra in (('none', []), ('{B0, wet spring}  (no pair contrasts with the baseline)', [[b0, rn]]),
                      ('{B0, shade, wet spring}', [[b0, sh, rn]])):
        for conj, cn in ((('A',), '(A) only'), (('A', 'F1', 'F2', 'NC'), 'full (E)')):
            P = fpres(fam, base + extra, conj)
            print('  E1 family sun\' x var[V], jobs {j_seen, j_fail} + %-55s %-9s |Pres|=%d' % (nm, cn, len(P)))
    print('  -> read as a question, "another wet spring" alone is a job NO member can do (NonCircular needs a')
    print('     contrast with the baseline), so adding it is strict (1 -> 0), not file 00\'s non-strict case.')


def part_g():
    print()
    print('-' * 100)
    print('(g) 02 s2/s7 option (b) marks, with "deleted" read as Part II deletion (port freed) instead of "off"')
    print('-' * 100)

    def prof_part2(fam, v, comp):
        base = fam.profile(v)
        off = fam.profile(v, deleted=(comp,))
        # a freed override port can send N wherever the rest would say S: undetermined there
        return tuple(None if (off[j] == 'S') else off[j] for j in range(m1.NS))

    MV, MW = m1.fn_menu(('V',)), m1.fn_menu(('W',))
    fg = m1.Family('g', [('sun', m1.SUN_MENU), ('var', MV)])
    fb = m1.Family('b', [('sun', m1.SUN_MENU), ('rain', MW)])
    fp = m1.Family('p', [('sun', m1.SUN_MENU), ('exc', m1.single_menu())])
    cands = (('E_good', fg, fg.find(sun='id', var='early'), 'var'), ('E_bad', fb, fb.find(sun='id', rain='wet'), 'rain'),
             ('E_patch', fp, fp.find(sun='id', exc='only@' + m1.show(m1.SETTINGS[m1.FSTAR])), 'exc'))
    for nm, fam, v, comp in cands:
        for cn, C in (('C_full', m1.C_FULL), ('J_after', m1.J_AFTER)):
            prof = fam.profile(v)
            off = fam.profile(v, deleted=(comp,))
            p2 = prof_part2(fam, v, comp)
            c_off = [j for j in C if j != m1.FSTAR and prof[j] != off[j]]
            c_p2 = [j for j in C if j != m1.FSTAR and prof[j] != p2[j]]
            print('  %-8s on %-8s consequences (off): %-2d -> %-17s  consequences (Part II): %-2d -> %s'
                  % (nm, cn, len(c_off), 'MARKED' if not c_off else 'not marked', len(c_p2),
                     'MARKED' if not c_p2 else 'not marked'))
    print('  -> with Part II deletion every added override has a "consequence" at every sunny-south pair of its')
    print('     contract (its deletion leaves the answer undetermined there), so (b) marks none of the three.')


if __name__ == '__main__':
    print('=' * 100)
    print('A6  CHECKS OF ratchet/models')
    print('=' * 100)
    part_a()
    part_b()
    part_c()
    part_d()
    part_e()
    part_f()
    part_g()
