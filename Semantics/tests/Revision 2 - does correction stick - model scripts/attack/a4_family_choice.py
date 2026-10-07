#!/usr/bin/env python3
"""A4 - results that turn on the declared family (pair level, Account = (A), as in 02/03).

Claims attacked:
  03 s4:  "'A correction must be harder to vary than what it corrects' refuses the neighbour's-variety
           rescue: on the old jobs every extension is at least as easy to vary (limit (ii); 1 -> 2 in 02 s4)."
  02 s0.3: "On fixed jobs, every added component makes Pres weakly larger, whether the rescue is good or bad."
  02 s0.3/s4: "Pres before and Pres after are disjoint in every rescue that added a part ... never nested."
  03 s2, point 4: "It is a statement that a witness exists, not a count. So ... no choice of menus flips it."
Every family below contains a member that answers exactly as E0 does (the witness, in the (A) reading).
"""
from pl import (pred_menu, sun_menu, SUN4, family, count, pres, J_BEFORE, J_AFTER, FSTAR, TRUTH, SETTINGS,
                answers, show, NS, mask, get, SUN_ID)

ANS = lambda sv, fire=0: answers(sv, fire)
E0A = tuple(SUN_ID)


def has_e0(fam_vectors):
    return any(v == E0A for v in fam_vectors)


def main():
    print('=' * 100)
    print('A4  RESULTS THAT TURN ON THE DECLARED FAMILY')
    print('=' * 100)
    MV = pred_menu(('V',))
    sunSW = sun_menu(('Sun', 'W'))
    sunSWWi = sun_menu(('Sun', 'W', 'Wi'))

    print('-' * 100)
    print('(i) Is the correction harder to vary than E0 on the OLD jobs (J_before)?  Each own family declared separately.')
    print('-' * 100)
    rows = [
        ('A', 'E0: sun reads Sun (4 maps)', family(SUN4, []), 'E1: sun reads Sun x var[V]', family(SUN4, [MV])),
        ('B', 'E0: sun reads Sun, W (16 maps)', family(sunSW, []), 'E1: sun reads Sun x var[V]', family(SUN4, [MV])),
        ('C', 'E0: sun reads Sun, W, Wi (256 maps)', family(sunSWWi, []), 'E1: sun fixed (id) x var[V]',
         family([SUN_ID], [MV])),
    ]
    for tag, n0, f0, n1, f1 in rows:
        e0in = any(ANS(sunSW[k[0]]) == E0A for k, _ in f0) if tag == 'B' else True
        a, b = count(f0, J_BEFORE), count(f1, J_BEFORE)
        verdict = 'E1 EASIER to vary' if b > a else ('E1 HARDER to vary' if b < a else 'equal')
        print('  pair %s  %-38s |Pres(J_before)|=%3d   %-30s |Pres(J_before)|=%3d  -> %s' % (tag, n0, a, n1, b, verdict))
    wit = []
    for tag, n0, f0, n1, f1 in rows:
        for fam, sl, menus in ((f0, {'A': SUN4, 'B': sunSW, 'C': sunSWWi}[tag], []), (f1, SUN4 if tag != 'C' else [SUN_ID], [MV])):
            wit.append(any(ANS(sl[k[0]], 0 if not menus else menus[0][k[1]]) == E0A for k, _ in fam))
    print('  every one of the six families holds a member answering exactly as E0 at all 16 pairs: %s' % all(wit))
    print('  -> "every extension is at least as easy to vary on the old jobs" holds in pair A only; it is the')
    print('     embedding (E0\'s own family placed inside E1\'s) that makes it true, not the correction.')

    print()
    print('-' * 100)
    print('(ii) The bad rescue as a member of E0\'s OWN family (sun reads Sun and W): no organization change at all')
    print('-' * 100)
    f0 = family(sunSW, [])
    Pb = pres(f0, J_BEFORE)
    Pa = pres(f0, J_AFTER)
    print('  |Pres(J_before)| = %d   |Pres(J_after)| = %d   (the rescue registers as a SHRINK: harder to vary)' % (len(Pb), len(Pa)))
    for k in Pa:
        sv = sunSW[k[0]]
        tab = {('dry', 'sunS'): None, ('dry', 'shadeS'): None, ('wet', 'sunS'): None, ('wet', 'shadeS'): None}
        for i in range(NS):
            s_ = SETTINGS[i]
            tab[(('dry', 'wet')[get(s_, 'W')], ('sunS', 'shadeS')[get(s_, 'Sun')])] = 'N' if sv[i] else 'S'
        print('    member of Pres(J_after): sun map %s' % ', '.join('%s/%s->%s' % (a, b, v) for (a, b), v in tab.items()))
    print('  -> "in a wet spring the north bed ripens first" is a member of the old family; by (H) adding the')
    print('     failed summer shrinks Pres. Owner\'s (2) ("more versions fit") is reversed under file 00\'s own premise.')

    print()
    print('-' * 100)
    print('(iii) "Pres before and Pres after are disjoint in every rescue that added a part": embedded family')
    print('      U_B = sun[Sun,W] x var[V]; Vers(E0) = var off')
    print('-' * 100)
    UB = family(sunSW, [MV])
    P0b = {k for k in pres(UB, J_BEFORE) if k[1] == 0}
    P1a = set(pres(UB, J_AFTER))
    print('  |Pres_E0(J_before)| = %d  |Pres_E1(J_after)| = %d  overlap = %d  -> %s'
          % (len(P0b), len(P1a), len(P0b & P1a), 'NOT disjoint' if P0b & P1a else 'disjoint'))
    UA = family(SUN4, [MV])
    P0b = {k for k in pres(UA, J_BEFORE) if k[1] == 0}
    P1a = set(pres(UA, J_AFTER))
    print('  (02\'s menu, sun[Sun] x var[V]: overlap = %d -> %s)' % (len(P0b & P1a), 'disjoint' if not P0b & P1a else 'not'))

    print()
    print('-' * 100)
    print('(iv) Strictness of (H*) for ONE correction, two menus ("no choice of menus flips it")')
    print('-' * 100)
    fam_prod = family(SUN4, [MV])
    # the same correction written as one rule with a parameter: which variety sends north first
    rule_menu = [mask(i for i in range(NS) if get(SETTINGS[i], 'V') == 1),
                 mask(i for i in range(NS) if get(SETTINGS[i], 'V') == 0)]
    fam_rule = family([SUN_ID], [rule_menu])
    for nm, fam in (('sun[4] x var[V]  (holds v0 = var off)', fam_prod),
                    ('rule "north first if the variety is P", P in {early, late} (no v0)', fam_rule)):
        a, b = count(fam, J_BEFORE), count(fam, J_AFTER)
        print('  %-70s |Pres(J_before)|=%d  |Pres(J_after)|=%d  strict? %s' % (nm, a, b, b < a))
    print('  Both families hold the corrected candidate; they differ only in whether the menu lists "off".')


if __name__ == '__main__':
    main()
