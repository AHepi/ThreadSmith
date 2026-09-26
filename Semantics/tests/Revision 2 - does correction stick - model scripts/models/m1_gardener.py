#!/usr/bin/env python3
"""M1 - the gardener and the north bed.

Everything is finite and enumerated. Vocabulary follows files 00 and 11 and draft 3:

  target D      the garden. A 'setting' is one edit-boundary pair: the values of
                W (wet spring), Wi (windy spring), V (the neighbour's variety on the
                north side), Sun (which bed gets more sun; 'N' means the south wall
                has been shaded, an admitted intervention).
  truth         the neighbour's early variety makes the north bed ripen first,
                whatever the weather; otherwise the sunnier bed ripens first.
  candidate     an organization: a 'sun' component (maps the sunnier bed to the bed
                that ripens first) plus zero or more OVERRIDE components (each a
                predicate on the setting; if any override fires, the answer is N).
  job           one setting of a contract. Account(E_v, job) is read as (A) at that
                pair: the version's answer equals the target's answer.
  variation family
                the product of the stated menus of the organization's components.
  Pres(F)       the versions in the family that do every job in F.

The narrowing is read as: five good summers were recorded (plus one shading test),
the sixth summer failed, and the gardener then says her explanation only covered
the summers seen before it.
"""
from itertools import product, combinations

ORDER = ('W', 'Wi', 'V', 'Sun')
DOM = {'W': (0, 1), 'Wi': (0, 1), 'V': ('late', 'early'), 'Sun': ('S', 'N')}
WORD = {'W': {0: 'dry', 1: 'wet'}, 'Wi': {0: 'calm', 1: 'windy'},
        'V': {'late': 'late', 'early': 'early'}, 'Sun': {'S': 'sunS', 'N': 'shadeS'}}
POS = {k: i for i, k in enumerate(ORDER)}
SETTINGS = [tuple(v) for v in product(*(DOM[k] for k in ORDER))]
SIDX = {s: j for j, s in enumerate(SETTINGS)}
NS = len(SETTINGS)


def get(s, k):
    return s[POS[k]]


def show(s):
    return '/'.join(WORD[k][get(s, k)] for k in ORDER)


def truth(s):
    return 'N' if get(s, 'V') == 'early' else get(s, 'Sun')


TRUTH = tuple(truth(s) for s in SETTINGS)

# ---------------------------------------------------------------- menus
SUN_MENU = [('id', {'S': 'S', 'N': 'N'}), ('allS', {'S': 'S', 'N': 'S'}),
            ('allN', {'S': 'N', 'N': 'N'}), ('swap', {'S': 'N', 'N': 'S'})]


def fn_menu(ports):
    """All predicates on the listed ports (all functions config -> {fire, not})."""
    configs = list(product(*(DOM[p] for p in ports)))
    menu = []
    for outs in product((False, True), repeat=len(configs)):
        fires = frozenset(c for c, o in zip(configs, outs) if o)
        if not fires:
            label = 'off'
        elif len(fires) == len(configs):
            label = 'always'
        else:
            label = '|'.join(sorted('&'.join(WORD[p][v] for p, v in zip(ports, c)) for c in fires))
        bits = tuple(tuple(get(s, p) for p in ports) in fires for s in SETTINGS)
        menu.append((label, bits))
    return menu


def single_menu():
    """An exception that fires at exactly one setting (the 'do-nothing patch' family)."""
    menu = [('off', tuple(False for _ in SETTINGS))]
    for t in SETTINGS:
        menu.append(('only@' + show(t), tuple(s == t for s in SETTINGS)))
    return menu


LITERALS = [('wet', 'W', 1), ('dry', 'W', 0), ('windy', 'Wi', 1), ('calm', 'Wi', 0),
            ('early', 'V', 'early'), ('late', 'V', 'late')]


def literal_menu():
    """Port-swap family: the override fires on one literal ('wet' could be 'windy')."""
    menu = [('off', tuple(False for _ in SETTINGS))]
    for nm, k, v in LITERALS:
        menu.append((nm, tuple(get(s, k) == v for s in SETTINGS)))
    return menu


# ---------------------------------------------------------------- families
class Family:
    """Product of the menus of an organization's components. comps[0] is 'sun'."""

    def __init__(self, name, comps):
        self.name = name
        self.names = [n for n, _ in comps]
        self.menus = [m for _, m in comps]
        assert self.names[0] == 'sun'
        self.sun_out = [tuple(item[1][get(s, 'Sun')] for s in SETTINGS) for item in self.menus[0]]

    def size(self):
        n = 1
        for m in self.menus:
            n *= len(m)
        return n

    def versions(self, fixed=None):
        """fixed: dict comp-name -> menu label (e.g. {'rain': 'off'}) restricting the family."""
        ranges = []
        for n, m in zip(self.names, self.menus):
            if fixed and n in fixed:
                ranges.append([i for i, it in enumerate(m) if it[0] == fixed[n]])
            else:
                ranges.append(range(len(m)))
        return product(*ranges)

    def profile(self, v, deleted=()):
        """Answer at every setting. deleted: comp names removed (sun -> undetermined, override -> off)."""
        if 'sun' in deleted:
            sun = (None,) * NS
        else:
            sun = self.sun_out[v[0]]
        ovs = [self.menus[c][v[c]][1] for c in range(1, len(v)) if self.names[c] not in deleted]
        return tuple('N' if any(o[j] for o in ovs) else sun[j] for j in range(NS))

    def label(self, v):
        return '(' + ', '.join('%s=%s' % (n, self.menus[c][v[c]][0]) for c, n in enumerate(self.names)) + ')'

    def find(self, **labels):
        v = []
        for n, m in zip(self.names, self.menus):
            want = labels.get(n, 'off')
            v.append([i for i, it in enumerate(m) if it[0] == want][0])
        return tuple(v)


def does_jobs(prof, jobs):
    return all(prof[j] == TRUTH[j] for j in jobs)


def pres(fam, jobs, fixed=None):
    return [v for v in fam.versions(fixed) if does_jobs(fam.profile(v), jobs)]


def pres_count(fam, jobs, fixed=None):
    return sum(1 for v in fam.versions(fixed) if does_jobs(fam.profile(v), jobs))


# ---------------------------------------------------------------- jobs and contracts
def S(W, Wi, V, Sun):
    return SIDX[(W, Wi, V, Sun)]


B0 = S(0, 0, 'late', 'S')           # baseline: the five recorded summers (all alike)
SHADE = S(0, 0, 'late', 'N')        # her shading test
FSTAR = S(1, 1, 'early', 'S')       # the sixth summer: wet, windy, neighbour planted early
J_BEFORE = [B0, SHADE]
J_AFTER = J_BEFORE + [FSTAR]
C_FULL = list(range(NS))
C_NARROW = list(J_BEFORE)           # "only the summers seen" (with the shading test kept)
C_NARROW_BARE = [B0]                # "only the summers seen", shading test dropped
BG_SEED = [S(0, 0, 'early', 'S')]   # seed trial: early variety, dry calm spring -> N first
BG_RAIN = [S(1, 0, 'late', 'S')]    # another wet spring, late variety -> S first


def jl(jobs):
    return '{' + ', '.join(show(SETTINGS[j]) for j in jobs) + '}'


# ---------------------------------------------------------------- theory checks on one candidate
def a_test(fam, v, contract):
    prof = fam.profile(v)
    bad = [j for j in contract if prof[j] != TRUTH[j]]
    return (not bad), bad


def noncircular(fam, v, contract):
    """Draft-3 S3 reading: some pair x of C and block G of active components such that
    the answer at x differs from the answer at the baseline, and the contrast is lost
    (equal, or undetermined) when G is deleted."""
    if B0 not in contract:
        return False, 'baseline not in contract'
    active = ['sun'] + [n for c, n in enumerate(fam.names) if c > 0 and fam.menus[c][v[c]][0] != 'off']
    prof = fam.profile(v)
    for r in range(1, len(active) + 1):
        for G in combinations(active, r):
            dp = fam.profile(v, deleted=G)
            for x in contract:
                if prof[x] != prof[B0]:
                    if dp[x] is None or dp[B0] is None or dp[x] == dp[B0]:
                        return True, 'x=%s, G=%s' % (show(SETTINGS[x]), '+'.join(G))
    return False, 'no pair of C changes the answer'


def consequences(fam, v, comp, contract, failed):
    """Option (b) of the 24 September analysis: pairs of the later claim's own contract,
    other than the failed pairs, where deleting the added component changes the answer."""
    prof = fam.profile(v)
    dp = fam.profile(v, deleted=(comp,))
    return [j for j in contract if j not in failed and prof[j] != dp[j]]


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


def main():
    print('=' * 78)
    print('M1  THE GARDENER')
    print('=' * 78)
    print('Settings: %d = W{dry,wet} x Wi{calm,windy} x V{late,early} x Sun{sunS,shadeS}' % NS)
    print('Truth: N first iff V=early; otherwise the sunnier bed first.')
    fam0 = Family('E0 own', [('sun', SUN_MENU)])
    e0 = fam0.find(sun='id')
    p0 = fam0.profile(e0)
    MIST = [j for j in range(NS) if p0[j] != TRUTH[j]]
    print('E0 = (sun=id): the sunnier bed ripens first.')
    print('M(E0) = pairs where E0 is wrong =', jl(MIST))
    print('J_before (records + shading test) =', jl(J_BEFORE))
    print('f* (the failed sixth summer)      =', show(SETTINGS[FSTAR]))
    print('J_after = J_before + f*')
    print('C_full = all 16 settings (every admitted change of the named variables)')
    print('BG_seed =', jl(BG_SEED), ' BG_rain =', jl(BG_RAIN))

    # ------------------------------------------------------------ own families
    MV, MW, MWWi, MVWWi = fn_menu(('V',)), fn_menu(('W',)), fn_menu(('W', 'Wi')), fn_menu(('V', 'W', 'Wi'))
    MSING = single_menu()
    fam_good = Family('E_good own [var reads V]', [('sun', SUN_MENU), ('var', MV)])
    fam_bad = Family('E_bad own [rain reads W]', [('sun', SUN_MENU), ('rain', MW)])
    fam_bad2 = Family('E_bad own [rain reads W,Wi]', [('sun', SUN_MENU), ('rain', MWWi)])
    fam_patch = Family('E_patch own [exception at one setting]', [('sun', SUN_MENU), ('exc', MSING)])
    good = fam_good.find(sun='id', var='early')
    bad = fam_bad.find(sun='id', rain='wet')
    bad2 = fam_bad2.find(sun='id', rain='wet&calm|wet&windy')
    patch = fam_patch.find(sun='id', exc='only@' + show(SETTINGS[FSTAR]))

    print()
    print('-' * 78)
    print('(i) THE (A) TEST AND NON-CIRCULAR DEPENDENCE, each candidate on its stated contract')
    print('-' * 78)
    rows = [
        ('E0 (before)', fam0, e0, J_BEFORE, 'J_before'),
        ('E0 (after the failure)', fam0, e0, J_AFTER, 'J_after'),
        ('E_good', fam_good, good, C_FULL, 'C_full'),
        ('E_good', fam_good, good, J_AFTER, 'J_after'),
        ('E_bad (wet->N)', fam_bad, bad, C_FULL, 'C_full'),
        ('E_bad (wet->N)', fam_bad, bad, J_AFTER, 'J_after (analysis Sit.3)'),
        ('E_patch (exception at f*)', fam_patch, patch, C_FULL, 'C_full'),
        ('E_patch (exception at f*)', fam_patch, patch, J_AFTER, 'J_after'),
        ('E_narrow = E0', fam0, e0, C_NARROW, 'C_narrow (summers seen + shading)'),
        ('E_narrow_bare = E0', fam0, e0, C_NARROW_BARE, 'C_narrow_bare (summers seen only)'),
    ]
    for nm, fam, v, C, cn in rows:
        ok, badp = a_test(fam, v, C)
        nc, why = noncircular(fam, v, C)
        print('%-27s on %-34s (A)=%-5s NonCirc=%-5s  %s' % (nm, cn, ok, nc,
              ('fails at ' + jl(badp)) if badp else why))

    print()
    print('-' * 78)
    print('(ii)-(iv) NAIVE: each candidate in its OWN family (different organizations)')
    print('-' * 78)
    print('Stated menus: sun = all 4 maps {S,N}->{S,N}; an override reading ports P = all')
    print('predicates on P (off included); the exception = fires at exactly one setting (or off).')
    naive = [
        ('E0 before', fam0, J_BEFORE),
        ('E0 after the failure', fam0, J_AFTER),
        ('E_good  [var reads V]', fam_good, J_AFTER),
        ('E_bad   [rain reads W]', fam_bad, J_AFTER),
        ('E_bad   [rain reads W,Wi]', fam_bad2, J_AFTER),
        ('E_patch [single exception]', fam_patch, J_AFTER),
        ('E_narrow (E0 on C_narrow)', fam0, C_NARROW),
    ]
    for nm, fam, J in naive:
        n = pres_count(fam, J)
        print('%-28s |V|=%6d  |Pres|=%5d  fraction=%.4f' % (nm, fam.size(), n, n / fam.size()))
    # the all-functions exception family: 4 x 65536 versions
    MALL = fn_menu(('W', 'Wi', 'V', 'Sun'))
    fam_patch_all = Family('E_patch own [exception = any predicate on all 4 ports]', [('sun', SUN_MENU), ('exc', MALL)])
    n = pres_count(fam_patch_all, J_AFTER)
    print('%-28s |V|=%6d  |Pres|=%5d  fraction=%.4f' % ('E_patch [any predicate, 4 ports]', fam_patch_all.size(), n, n / fam_patch_all.size()))
    print()
    print('Naive subset test Pres_after <= Pres_before: the elements are tuples of different')
    print('length (sun) vs (sun, override); as Python sets they are always disjoint:')
    for nm, fam, J in naive[2:6]:
        A = set(pres(fam, J))
        B = set(pres(fam0, J_BEFORE))
        print('   %-28s Pres_after & Pres_before = %s  -> "after is not inside before" for every rescue' % (nm, A & B or 'empty'))
    print('Answer profiles as the only common currency (profile on C_full):')
    B = {fam0.profile(v) for v in pres(fam0, J_BEFORE)}
    for nm, fam, J in naive[2:6]:
        A = {fam.profile(v) for v in pres(fam, J)}
        print('   %-28s profiles(after) inside profiles(before)? %s' % (nm, A <= B))
    print('   (any rescue changes the answer at f*, so this is False for every rescue; restricted')
    print('    to J_before every surviving profile equals the truth, so it is trivially "equal".)')

    # ------------------------------------------------------------ embedding
    for tag, rain_menu in (('rain reads W', MW), ('rain reads W,Wi', MWWi)):
        U = Family('U', [('sun', SUN_MENU), ('var', MV), ('rain', rain_menu), ('exc', MSING)])
        print()
        print('-' * 78)
        print('(v) EMBEDDING  U = sun x var[V] x rain[%s] x exc[single]   |U| = %d' % (tag.split(' reads ')[1], U.size()))
        print('    Vers(E) = points of U whose components absent from E are off.')
        print('-' * 78)
        e0u = U.find(sun='id')
        rain_lab = 'wet' if rain_menu is MW else 'wet&calm|wet&windy'
        cands = {
            'E_good': (U.find(sun='id', var='early'), 'var'),
            'E_bad': (U.find(sun='id', rain=rain_lab), 'rain'),
            'E_patch': (U.find(sun='id', exc='only@' + show(SETTINGS[FSTAR])), 'exc'),
        }
        vers = {
            'E0': {'var': 'off', 'rain': 'off', 'exc': 'off'},
            'E_good': {'rain': 'off', 'exc': 'off'},
            'E_bad': {'var': 'off', 'exc': 'off'},
            'E_patch': {'var': 'off', 'rain': 'off'},
        }
        P0b = pres(U, J_BEFORE, vers['E0'])
        P0a = pres(U, J_AFTER, vers['E0'])
        print('E0: |Vers|=%d  |Pres(J_before)|=%d  |Pres(J_after)|=%d  |Pres(C_narrow)|=%d  |Pres(C_full)|=%d' % (
            len(list(U.versions(vers['E0']))), len(P0b), len(P0a), len(pres(U, C_NARROW, vers['E0'])),
            len(pres(U, C_FULL, vers['E0']))))
        goodPa = None
        for nm in ('E_good', 'E_bad', 'E_patch'):
            v1, comp = cands[nm]
            fx = vers[nm]
            nV = len(list(U.versions(fx)))
            Pb = pres(U, J_BEFORE, fx)
            Pa = pres(U, J_AFTER, fx)
            Pf = pres(U, C_FULL, fx)
            if nm == 'E_good':
                goodPa = Pa
            reinst_f = [v for v in Pa if U.profile(v)[FSTAR] == p0[FSTAR]]
            reinst_any = [v for v in Pa if any(U.profile(v)[j] == p0[j] for j in MIST)]
            print()
            print('%s = %s   |Vers|=%d' % (nm, U.label(v1), nV))
            print('  (ii)  |Pres(J_before)|=%d  |Pres(J_after)|=%d  |Pres(C_full)|=%d' % (len(Pb), len(Pa), len(Pf)))
            print('        E0 (added component off) in Pres(J_before)? %s   in Pres(J_after)? %s' % (e0u in Pb, e0u in Pa))
            print('        versions in Pres(J_after) that give E0\'s wrong answer at f*: %d' % len(reinst_f))
            print('        versions in Pres(J_after) that give E0\'s wrong answer somewhere in M(E0): %d' % len(reinst_any))
            for v in reinst_any[:3]:
                prof = U.profile(v)
                print('           e.g. %s  wrong as E0 at %s' % (U.label(v), jl([j for j in MIST if prof[j] == p0[j]])))
            print('  (iii) Pres(J_after) vs Pres(J_before) [same family, more jobs, (H)]: %s' % rel(Pa, Pb))
            print('        Pres_E0(J_before) vs Pres_%s(J_before) [old jobs, before vs after family]: %s' % (nm, rel(P0b, Pb)))
            print('        Pres_%s(J_after) vs Pres_E0(J_before) [after on new jobs vs before on old]: %s' % (nm, rel(Pa, P0b)))
            print('  (iv)  |Pres_%s(J_after)| - |Pres_E0(J_before)| = %+d ;  vs E_good on J_after: %+d' % (
                nm, len(Pa) - len(P0b), len(Pa) - len(goodPa)))
            print('        does the candidate itself pass (A) on C_full? %s' % (U.profile(v1) == TRUTH))
        print()
        print('Narrowing in U: E_narrow = E0 on C_narrow.  Pres_E0(C_narrow) vs Pres_E0(J_before): %s;'
              % rel(pres(U, C_NARROW, vers['E0']), P0b))
        print('   vs Pres_E0(J_after): %s (%d vs %d)' % (rel(pres(U, C_NARROW, vers['E0']), P0a),
                                                       len(pres(U, C_NARROW, vers['E0'])), len(P0a)))

    # ------------------------------------------------------------ fully common family
    U = Family('U', [('sun', SUN_MENU), ('var', MV), ('rain', MW), ('exc', MSING)])
    print()
    print('-' * 78)
    print('FULLY COMMON FAMILY: all of U free (Pres depends on the jobs only)')
    print('-' * 78)
    named = {'E0': U.find(sun='id'), 'E_good': U.find(sun='id', var='early'),
             'E_bad': U.find(sun='id', rain='wet'),
             'E_patch': U.find(sun='id', exc='only@' + show(SETTINGS[FSTAR]))}
    for jn, J in (('J_before (= C_narrow)', J_BEFORE), ('J_after', J_AFTER), ('J_after + BG_seed', J_AFTER + BG_SEED),
                  ('J_after + BG_rain', J_AFTER + BG_RAIN), ('C_full', C_FULL)):
        P = pres(U, J)
        members = [k for k, v in named.items() if v in P]
        print('  |Pres(%-22s)| = %4d   members among named: %s' % (jn, len(P), ', '.join(members) or '-'))
    print('  Pres(J_after) vs Pres(J_before): %s  (the narrowing moves back from the first to the second)' %
          rel(pres(U, J_AFTER), pres(U, J_BEFORE)))

    # ------------------------------------------------------------ option (b)
    print()
    print('-' * 78)
    print('COMPARISON: what the record of option (b) marks (no consequence beyond the failed pair)')
    print('-' * 78)
    for nm, fam, v, comp in (('E_good', fam_good, good, 'var'), ('E_bad', fam_bad, bad, 'rain'),
                             ('E_patch', fam_patch, patch, 'exc')):
        for cn, C in (('C_full', C_FULL), ('J_after', J_AFTER)):
            cons = consequences(fam, v, comp, C, [FSTAR])
            print('  %-8s on %-8s consequences: %-3d -> %s' % (nm, cn, len(cons),
                  'not marked' if cons else 'MARKED (absorbed)'))
    print('  E_narrow: the limit follows from no component -> MARKED (absorbed)')


if __name__ == '__main__':
    main()
