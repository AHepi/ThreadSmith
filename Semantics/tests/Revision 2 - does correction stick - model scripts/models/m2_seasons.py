#!/usr/bin/env python3
"""M2 - the seasons: the tilt explanation, the myth, and the myth amended.

Target D: three places N (Greece), E (the equator), S (far south) and two halves of
the year H1 (Greek summer months) and H2. Answer at a pair (place, half):
summer / winter / none. Truth (the tilt): season = sign(latitude) x sign(half),
with 0 meaning no seasons.

Tilt organization: tilt t in {+1, 0, -1}; latitude factor g (place -> {+1,0,-1});
heating law h (exposure in {+1,0,-1} -> season). season(p, half) = h[t * g(p) * s(half)].
The tilt also takes two component jobs outside the seasons question (Deutsch p.24:
"we know - and can test independently of our experience of seasons"):
  BG_heat : a plate facing a lamp warms, one turned away cools, one edge-on neither
            (pins h);
  BG_elev : the noon sun at N is high in H1 and low in H2 (pins t * g(N)).
The myth takes no such job: nothing but the seasons bears on Demeter's grief.

Myth organization: schedule (half -> Persephone away/home); grief u (away/home ->
season, the same everywhere); in the AMENDED organization also a destination d in
{none, S, E}: the place d gets the opposite of the rest of the world ("she sends the
warmth south, and calls it home"). The original myth is the amended organization
with d = none.
"""
from itertools import product

PLACES = ('N', 'E', 'S')
LAT = {'N': 1, 'E': 0, 'S': -1}
HALVES = ('H1', 'H2')
SG = {'H1': 1, 'H2': -1}
SEAS = {1: 'summer', -1: 'winter', 0: 'none'}
SEASONS = ('summer', 'winter', 'none')
OPP = {'summer': 'winter', 'winter': 'summer', 'none': 'none'}
PAIRS = [(p, h) for p in PLACES for h in HALVES]
TRUTH = {x: SEAS[LAT[x[0]] * SG[x[1]]] for x in PAIRS}

J_GREEK = [('N', 'H1'), ('N', 'H2')]
J_SAILOR = J_GREEK + [('S', 'H1'), ('S', 'H2')]
J_WORLD = list(PAIRS)
SAILOR_BLOCK = [('S', 'H1'), ('S', 'H2')]


def pl(xs):
    return '{' + ', '.join('%s,%s' % x for x in xs) + '}'


# ---------------------------------------------------------------- tilt
G_LAW = [('sphere', {'N': 1, 'E': 0, 'S': -1}), ('flat/escape', {'N': 1, 'E': 1, 'S': 1})]
G_SPHERE = G_LAW[:1]
G_TABLE = [('g' + ''.join('%+d' % v for v in vals), dict(zip(PLACES, vals))) for vals in product((1, 0, -1), repeat=3)]
H_LAW = [('direct', {1: 'summer', -1: 'winter', 0: 'none'}), ('inverse', {1: 'winter', -1: 'summer', 0: 'none'})]
H_TABLE = [('h' + '/'.join(v[0] for v in vals), dict(zip((1, -1, 0), vals))) for vals in product(SEASONS, repeat=3)]
T_MENU = [('t+1', 1), ('t0', 0), ('t-1', -1)]


class Tilt:
    kind = 'tilt'

    def __init__(self, name, gmenu, hmenu, background):
        self.name, self.gmenu, self.hmenu, self.bg = name, gmenu, hmenu, background

    def versions(self):
        return list(product(range(3), range(len(self.gmenu)), range(len(self.hmenu))))

    def ans(self, v, x):
        t = T_MENU[v[0]][1]
        g = self.gmenu[v[1]][1]
        h = self.hmenu[v[2]][1]
        return h[t * g[x[0]] * SG[x[1]]]

    def bg_ok(self, v):
        if not self.bg:
            return True
        t = T_MENU[v[0]][1]
        g = self.gmenu[v[1]][1]
        h = self.hmenu[v[2]][1]
        heat = h[1] == 'summer' and h[-1] == 'winter' and h[0] == 'none'
        elev = t * g['N'] * SG['H1'] == 1 and t * g['N'] * SG['H2'] == -1
        return heat and elev

    def label(self, v):
        return '(%s, %s, %s)' % (T_MENU[v[0]][0], self.gmenu[v[1]][0], self.hmenu[v[2]][0])

    def find(self, t, g, h):
        return ([i for i, m in enumerate(T_MENU) if m[0] == t][0], [i for i, m in enumerate(self.gmenu) if m[0] == g][0],
                [i for i, m in enumerate(self.hmenu) if m[0] == h][0])


# ---------------------------------------------------------------- myth
SCHED = [('sched:' + ''.join(a[0] for a in vals), dict(zip(HALVES, vals))) for vals in product(('home', 'away'), repeat=2)]
U_MENU = [('u:home->%s,away->%s' % vals, {'home': vals[0], 'away': vals[1]}) for vals in product(SEASONS, repeat=2)]


class Myth:
    """Law-like myth family: schedule x uniform grief x destination (menu stated per run)."""
    kind = 'myth'

    def __init__(self, name, dmenu):
        self.name, self.dmenu, self.bg = name, dmenu, False

    def versions(self):
        return list(product(range(len(SCHED)), range(len(U_MENU)), range(len(self.dmenu))))

    def ans(self, v, x):
        st = SCHED[v[0]][1][x[1]]
        s = U_MENU[v[1]][1][st]
        return OPP[s] if x[0] == self.dmenu[v[2]] else s

    def bg_ok(self, v):
        return True

    def label(self, v):
        return '(%s, %s, d=%s)' % (SCHED[v[0]][0], U_MENU[v[1]][0], self.dmenu[v[2]])

    def find(self, d):
        return ([i for i, m in enumerate(SCHED) if m[1] == {'H1': 'home', 'H2': 'away'}][0],
                [i for i, m in enumerate(U_MENU) if m[1] == {'home': 'summer', 'away': 'winter'}][0],
                self.dmenu.index(d))


class MythTable:
    """Table-like amended myth: grief reads (state, place); every table is a version."""
    kind = 'myth-table'

    def __init__(self, name):
        self.name, self.bg = name, False
        self.keys = [(st, p) for st in ('home', 'away') for p in PLACES]

    def versions(self):
        return list(product(range(len(SCHED)), product(SEASONS, repeat=len(self.keys))))

    def ans(self, v, x):
        st = SCHED[v[0]][1][x[1]]
        return dict(zip(self.keys, v[1]))[(st, x[0])]

    def bg_ok(self, v):
        return True


def pres(fam, jobs, only=None):
    vs = only if only is not None else fam.versions()
    return [v for v in vs if fam.bg_ok(v) and all(fam.ans(v, x) == TRUTH[x] for x in jobs)]


def spread(fam, P, xs):
    return {('%s,%s' % x): sorted({fam.ans(v, x) for v in P}) for x in xs}


def rel(A, B):
    A, B = set(A), set(B)
    if A == B:
        return 'equal'
    if A < B:
        return 'first STRICTLY INSIDE second'
    if A > B:
        return 'first STRICTLY CONTAINS second'
    if not (A & B):
        return 'disjoint'
    return 'incomparable (overlap %d)' % len(A & B)


def a_test(fam, v, jobs):
    bad = [x for x in jobs if fam.ans(v, x) != TRUTH[x]]
    return (not bad), bad


def main():
    print('=' * 78)
    print('M2  THE SEASONS')
    print('=' * 78)
    print('Truth:', ', '.join('%s,%s=%s' % (x[0], x[1], TRUTH[x]) for x in PAIRS))
    print('J_greek =', pl(J_GREEK), '  J_sailor = J_greek +', pl(SAILOR_BLOCK), '  J_world = all 6 pairs')

    T1 = Tilt('tilt, law menus, no background jobs', G_LAW, H_LAW, False)
    T2 = Tilt('tilt, law menus + BG_heat, BG_elev', G_LAW, H_LAW, True)
    T3 = Tilt('tilt, sphere only (one law everywhere) + BG', G_SPHERE, H_LAW, True)
    T4 = Tilt('tilt, TABLE menus (all g, all h) + BG', G_TABLE, H_TABLE, True)
    Mo = Myth('myth, original organization (d fixed none)', ['none'])
    Me = Myth('myth, amended organization (d in none,S,E)', ['none', 'S', 'E'])
    Mt = MythTable('myth amended, TABLE menu (grief reads state and place)')

    tstar = T1.find('t+1', 'sphere', 'direct')
    tesc = T1.find('t+1', 'flat/escape', 'direct')
    m0 = Me.find('none')
    m1 = Me.find('S')
    m0o = Mo.find('none')

    print()
    print('-' * 78)
    print('(i) THE (A) TEST')
    print('-' * 78)
    for nm, fam, v in (('Tilt T* (t+1, sphere, direct)', T1, tstar), ('Tilt with escape clause (flat)', T1, tesc),
                       ('Myth M0 (original)', Me, m0), ('Myth M1 (amended, d=S)', Me, m1)):
        for jn, J in (('J_greek', J_GREEK), ('J_sailor', J_SAILOR), ('J_world', J_WORLD)):
            ok, bad = a_test(fam, v, J)
            print('  %-32s on %-8s (A)=%-5s %s' % (nm, jn, ok, ('fails at ' + pl(bad)) if bad else ''))

    print()
    print('-' * 78)
    print('(ii) Pres AND WHAT IT LEAVES OPEN AT UNSEEN PAIRS (spread = answers across Pres)')
    print('-' * 78)
    unseen_g = [('S', 'H1'), ('E', 'H1')]
    for fam in (T1, T2, T3, T4, Mo, Me):
        for jn, J, look in (('J_greek', J_GREEK, unseen_g), ('J_sailor', J_SAILOR, [('E', 'H1')]),
                            ('J_world', J_WORLD, [])):
            P = pres(fam, J)
            print('  %-46s |V|=%5d  |Pres(%-8s)|=%4d  spread %s' % (fam.name, len(fam.versions()), jn, len(P),
                                                                   spread(fam, P, look) if look else ''))
    P = pres(Mt, J_SAILOR)
    print('  %-46s |V|=%5d  |Pres(J_sailor)|=%4d  spread %s' % (Mt.name, len(Mt.versions()), len(P),
                                                               spread(Mt, P, [('E', 'H1')])))

    print()
    print('-' * 78)
    print('(ii)-(iv) THE MYTH\'S RESCUE: naive (own families) and embedded (d switched to none)')
    print('-' * 78)
    Pb_own = pres(Mo, J_GREEK)
    Pa_own = pres(Me, J_SAILOR)
    print('  NAIVE own families: original on J_greek |Pres|=%d of %d (%.4f); amended on J_sailor |Pres|=%d of %d (%.4f)'
          % (len(Pb_own), len(Mo.versions()), len(Pb_own) / len(Mo.versions()), len(Pa_own), len(Me.versions()),
             len(Pa_own) / len(Me.versions())))
    Pa_tab = pres(Mt, J_SAILOR)
    print('  NAIVE, table menu for the amended grief: amended on J_sailor |Pres|=%d of %d  (original: %d)' % (
        len(Pa_tab), len(Mt.versions()), len(Pb_own)))
    vers0 = [v for v in Me.versions() if Me.dmenu[v[2]] == 'none']
    P0b = pres(Me, J_GREEK, vers0)
    P0a = pres(Me, J_SAILOR, vers0)
    P1b = pres(Me, J_GREEK)
    P1a = pres(Me, J_SAILOR)
    print('  EMBEDDED in the amended organization; Vers(M0) = d=none (%d), Vers(M1) = all d (%d):' % (len(vers0), len(Me.versions())))
    print('    |Pres_M0(J_greek)|=%d  |Pres_M0(J_sailor)|=%d  |Pres_M1(J_greek)|=%d  |Pres_M1(J_sailor)|=%d' % (
        len(P0b), len(P0a), len(P1b), len(P1a)))
    print('    M0 (d switched off) in Pres_M1(J_sailor)? %s' % (m0 in P1a))
    print('    (iii) Pres_M1(J_sailor) vs Pres_M1(J_greek) [(H)]: %s' % rel(P1a, P1b))
    print('          Pres_M0(J_greek) vs Pres_M1(J_greek) [old jobs]: %s' % rel(P0b, P1b))
    print('          Pres_M1(J_sailor) vs Pres_M0(J_greek): %s' % rel(P1a, P0b))
    print('    (iv) |Pres_M1(J_sailor)| - |Pres_M0(J_greek)| = %+d  -> the amendment does %s enlarge Pres' % (
        len(P1a) - len(P0b), 'NOT' if len(P1a) <= len(P0b) else ''))
    print('         |Pres_M1(J_sailor)| - |Pres_M1(J_greek)| = %+d  (the same shrink a correction shows)' % (len(P1a) - len(P1b)))
    old_mist = [x for x in PAIRS if Me.ans(m0, x) != TRUTH[x]]
    print('    M(M0) =', pl(old_mist))
    keep = [v for v in P1a if any(Me.ans(v, x) == Me.ans(m0, x) for x in old_mist)]
    print('    versions in Pres_M1(J_sailor) that keep M0\'s wrong answer somewhere in M(M0): %d of %d (at E)' % (len(keep), len(P1a)))
    print('    spread of Pres_M1(J_greek) at the sailor\'s pairs:', spread(Me, P1b, SAILOR_BLOCK))

    print()
    print('-' * 78)
    print('THE TILT\'S OWN CORRECTION (escape clause -> sphere): same organization, file 00 condition met')
    print('-' * 78)
    for fam in (T1, T2):
        Pg = pres(fam, J_GREEK)
        Ps = pres(fam, J_SAILOR)
        print('  %-40s |Pres(J_greek)|=%d  |Pres(J_sailor)|=%d  (H): %s;  escape version in Pres(J_sailor)? %s' % (
            fam.name, len(Pg), len(Ps), rel(Ps, Pg), tesc in Ps))
    esc_mist = [x for x in PAIRS if T1.ans(tesc, x) != TRUTH[x]]
    print('  M(escape version) =', pl(esc_mist))
    for fam in (T1, T2, T4):
        Ps = pres(fam, J_SAILOR)
        # the escape version's answers, computed directly (it is (t+1, flat, direct))
        esc_ans = {x: T1.ans(tesc, x) for x in PAIRS}
        keep = [v for v in Ps if any(fam.ans(v, x) == esc_ans[x] for x in esc_mist)]
        print('  %-40s versions in Pres(J_sailor) giving the escape version\'s wrong answer somewhere: %d of %d' % (
            fam.name, len(keep), len(Ps)))

    print()
    print('-' * 78)
    print('"NOWHERE TO GO" (Deutsch p.25): a hypothetical report that the south is IN phase with Greece')
    print('-' * 78)
    inphase = {('N', 'H1'): 'summer', ('N', 'H2'): 'winter', ('S', 'H1'): 'summer', ('S', 'H2'): 'winter'}
    for fam in (T1, T2, T3, T4, Mo, Me):
        P = [v for v in fam.versions() if fam.bg_ok(v) and all(fam.ans(v, x) == a for x, a in inphase.items())]
        ex = fam.label(P[0]) if P and hasattr(fam, 'label') else ''
        print('  %-46s |Pres(in-phase report)| = %3d  %s' % (fam.name, len(P), ('e.g. ' + ex) if ex else '-> nowhere to go'))

    print()
    print('-' * 78)
    print('TILT vs AMENDED MYTH on the jobs each now does')
    print('-' * 78)
    for fam in (T1, T2, T3):
        print('  %-46s |Pres(J_sailor)| = %d' % (fam.name, len(pres(fam, J_SAILOR))))
    print('  %-46s |Pres(J_sailor)| = %d' % (Me.name, len(P1a)))
    for v in P1a:
        print('      myth version in Pres:', Me.label(v))
    for v in pres(T1, J_SAILOR):
        print('      tilt version in Pres (T1):', T1.label(v))

    print()
    print('-' * 78)
    print('HISTORY-FREE vs HISTORY-USING detection of a fitted part')
    print('  LOO(x): is the answer at x fixed by Pres(F - {x})?  BLOCK: is it fixed by Pres(F - block)?')
    print('-' * 78)
    for nm, fam in (('amended myth (embedded family)', Me), ('tilt T1 (no background)', T1), ('tilt T2 (+BG)', T2),
                    ('tilt T3 (sphere only, +BG)', T3)):
        for x in SAILOR_BLOCK:
            P = pres(fam, [y for y in J_SAILOR if y != x])
            print('  %-32s LOO at %s,%s: answers %s' % (nm, x[0], x[1], sorted({fam.ans(v, x) for v in P})))
        P = pres(fam, J_GREEK)
        print('  %-32s BLOCK (sailor\'s report left out): answers at S,H1 %s, at S,H2 %s' % (
            nm, sorted({fam.ans(v, ('S', 'H1')) for v in P}), sorted({fam.ans(v, ('S', 'H2')) for v in P})))

    print()
    print('-' * 78)
    print('NARROWING: "the myth only covers Greece" (after the report)')
    print('-' * 78)
    Pn = pres(Mo, J_GREEK)
    print('  Pres_M0(J_greek) after narrowing vs before the report: %s (|%d| vs |%d|);  vs Pres_M0(J_sailor): %s (%d)' % (
        rel(Pn, Pb_own), len(Pn), len(Pb_own), rel(Pn, pres(Mo, J_SAILOR)), len(pres(Mo, J_SAILOR))))

    print()
    print('-' * 78)
    print('OPTION (b) consequences (pairs of J_world other than the sailor\'s where the change matters)')
    print('-' * 78)
    cons_m = [x for x in J_WORLD if x not in SAILOR_BLOCK and Me.ans(m1, x) != Me.ans(m0, x)]
    cons_t = [x for x in J_WORLD if x not in SAILOR_BLOCK and T1.ans(tstar, x) != T1.ans(tesc, x)]
    print('  myth amendment d: none -> S        consequences %s -> %s' % (pl(cons_m), 'not marked' if cons_m else 'MARKED (absorbed)'))
    print('  tilt correction flat -> sphere     consequences %s -> %s' % (pl(cons_t), 'not marked' if cons_t else 'MARKED (absorbed)'))


if __name__ == '__main__':
    main()
