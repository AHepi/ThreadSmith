#!/usr/bin/env python3
"""s129_sweep_the_boundaries_of_every_provenance_case.py

What it does, in plain words: for log S129 (decision S83, Reading C). The model program's suites compute provenance
(selected, constructed, declared) on many small histories, none of which declares a system boundary. In the copy of the
program (results/S129 Reading C carried into copies/model after Reading C/), a case with no declared boundary is read
with every occurrence it states inside the boundary (invention I198 of the copy), which gives the original's verdicts.
This script asks the further question: for every provenance computation the suites make, would the verdict change if
the claim declared a NARROWER boundary, one that leaves some earlier occurrences outside? It wraps the copy's three
provenance functions (prov_fixed_points, sel, con) so that each call made while a claim runs is also computed at every
narrower boundary (every subset of the stated occurrences that keeps the holding in question; for sel and con, every
subset of the named occurrences), and records which calls give a different verdict there, and how. The wrapped
functions return what the copy computes with no boundary, so every claim's own result is the copy's.
Every claim of the suite is run once, at scale 1 and a 20 s time cap (the sweep is about which histories the suites
build, not about the record's numbers); the copy is imported, never written. Output: printed, and
results/S129 Reading C carried into copies/suite boundary sweep.json (and the scratch file s129/sweep.json).

  PYTHONHASHSEED=0 python3 -B Semantics/tools/s129_sweep_the_boundaries_of_every_provenance_case.py

Written 2 October 2026 by the one Opus 5.5 agent of log S129.
"""
import copy as _copy, itertools, json, os, sys, time
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COPY = os.path.join(ROOT, 'results', 'S129 Reading C carried into copies', 'model after Reading C')
SC = '/tmp/claude-0/-home-user-ThreadSmith/8d9323da-c0ec-57ec-91fd-8f99ca99320a/scratchpad/s129'
os.environ.setdefault('S129_READING_C', '1')
os.environ.setdefault('S129_GRADED', '1')
sys.path.insert(0, COPY)

from model import claims_b as cb  # noqa: E402

ORIG = {'prov_fixed_points': cb.prov_fixed_points, 'sel': cb.sel, 'con': cb.con}
CUR = {'claim': None}
LOG = defaultdict(lambda: defaultdict(lambda: {'calls': 0, 'distinct': set(), 'flipping': set(), 'examples': [],
                                                'changes': defaultdict(set)}))


def _subsets(items, keep=()):
    items = [x for x in items if x not in keep]
    for r in range(len(items)):          # proper subsets only: the full set is the case's own reading
        for sub in itertools.combinations(items, r):
            yield set(sub) | set(keep)


def _note(fn, key, base, flips, describe):
    if CUR['claim'] is None:
        return
    rec = LOG[CUR['claim']][fn]
    rec['calls'] += 1
    rec['distinct'].add(key)
    if flips:
        rec['flipping'].add(key)
        for f in flips:
            rec['changes'][f.get('change', '?')].add(key)
        if len(rec['examples']) < 4 and describe not in [e['case'] for e in rec['examples']]:
            rec['examples'].append({'case': describe, 'verdict with no boundary declared': base,
                                    'narrower boundaries that change it': flips[:4], 'how many': len(flips)})


def _fp_view(fps, inside):
    """The verdict of a provenance computation at the occurrences inside a boundary: for each fixed point, each inside
    occurrence's (Sel, Con), as 'Sel', 'Con' or 'Dec'."""
    lab = lambda sc: 'Sel' if sc[0] else ('Con' if sc[1] else 'Dec')
    return sorted(tuple('o%d %s' % (o + 1, lab(sc[o])) for o in sorted(inside)) for R, sc in fps) or ['no fixed point']


def _change(res, r2, o):
    """How the verdict of the last holding moves: 'Dec -> Sel', 'Con -> Dec', 'no fixed point -> ...', and so on."""
    lab = lambda sc: 'Sel' if sc[0] else ('Con' if sc[1] else 'Dec')
    a = '/'.join(sorted(set(lab(sc[o]) for R, sc in res))) or 'no fixed point'
    b = '/'.join(sorted(set(lab(sc[o]) for R, sc in r2))) or 'no fixed point'
    return '%s -> %s' % (a, b) if a != b else 'last holding unchanged; an earlier holding inside the boundary changes'


def pfp(n, held, trace, selc, rd, i161=True, eps=None, rec_of=None, beta=None):
    res = ORIG['prov_fixed_points'](n, held, trace, selc, rd, i161, eps, rec_of, beta)
    if beta is None and CUR['claim'] is not None and n >= 2:
        flips = []
        for b in _subsets(range(n), keep=(n - 1,)):
            r2 = ORIG['prov_fixed_points'](n, held, trace, selc, rd, i161, eps, rec_of, b)
            if _fp_view(r2, b) != _fp_view(res, b):
                flips.append({'boundary (occurrences inside)': ['o%d' % (o + 1) for o in sorted(b)],
                              'verdict there': _fp_view(r2, b), 'the same occurrences with no boundary': _fp_view(res, b),
                              'change': 'cut %s: %s' % (rd, _change(res, r2, n - 1))})
        key = (n, tuple(held), tuple(trace), tuple(selc), rd, i161, tuple(rec_of) if rec_of else None, eps is not None)
        desc = 'n=%d held=%s trace=%s Sel-conditions=%s reading=%s records=%s%s' % (
            n, list(held), list(trace), list(selc), rd, rec_of, ' (episodes given)' if eps is not None else '')
        _note('prov_fixed_points', key, _fp_view(res, range(n)), flips, desc)
    return res


def _names(h):
    return list(dict.fromkeys(list(h.occ) + [o for o, _ in h.rep] + list(h.source)))


def sel(cand, H, h, *a, **k):
    res = ORIG['sel'](cand, H, h, *a, **k)
    if getattr(h, 'beta', None) is None and CUR['claim'] is not None:
        flips = []
        for b in _subsets(_names(h)):
            h2 = _copy.copy(h)
            h2.beta = set(b)
            r2 = ORIG['sel'](cand, H, h2, *a, **k)
            if r2 != res:
                flips.append({'boundary (occurrences inside)': sorted(b), 'Sel there': r2, 'change': 'Sel %s -> %s' % (res, r2)})
        key = (tuple(h.occ), tuple(sorted(h.rep)), res, tuple(sorted(k.items())))
        desc = 'occurrences %s, tags %s, Sel with no boundary %s%s' % (list(h.occ), sorted(h.rep), res,
                                                                      (' ' + str(k)) if k else '')
        _note('sel', key, res, flips, desc)
    return res


def con(h, *a, **k):
    res = ORIG['con'](h, *a, **k)
    if getattr(h, 'beta', None) is None and CUR['claim'] is not None:
        flips = []
        for b in _subsets(_names(h)):
            h2 = _copy.copy(h)
            h2.beta = set(b)
            r2 = ORIG['con'](h2, *a, **k)
            if r2 != res:
                flips.append({'boundary (occurrences inside)': sorted(b), 'Con there': r2, 'change': 'Con %s -> %s' % (res, r2)})
        key = (tuple(h.occ), tuple(sorted(h.rep)), res, tuple(sorted(k.items())))
        desc = 'occurrences %s, tags %s, Con with no boundary %s' % (list(h.occ), sorted(h.rep), res)
        _note('con', key, res, flips, desc)
    return res


cb.prov_fixed_points, cb.sel, cb.con = pfp, sel, con
# the claim modules import these names when they are imported: they are imported now, after the wrapping
from model import run as mrun  # noqa: E402
from model.harness import REG, Settings  # noqa: E402


def main():
    S = Settings(scale=1.0, time_cap=20.0)
    ids = sorted(REG, key=lambda s: (int(s[2:].split('.')[0]), s))
    status = {}
    t0 = time.time()
    for cid in ids:
        CUR['claim'] = cid
        r = mrun.run_claim(cid, S)
        status[cid] = r['status'] + (' (error)' if r['error'] else '')
        CUR['claim'] = None
    out = {'about': 'S129: every provenance computation the suites make, recomputed at every narrower boundary (Reading C, '
                    'copy only). Copy: results/S129 Reading C carried into copies/model after Reading C/ (READING_C=%s, GRADED=%s). '
                    'Scale 1, time cap 20 s.' % (cb.READING_C, cb.GRADED),
           'seconds': round(time.time() - t0, 1), 'claims_run': len(ids),
           'claims_that_compute_provenance': {}, 'statuses_at_scale_1': status}
    for cid, fns in LOG.items():
        out['claims_that_compute_provenance'][cid] = {
            fn: {'calls': d['calls'], 'distinct histories': len(d['distinct']),
                 'distinct histories whose verdict changes at some narrower boundary': len(d['flipping']),
                 'how the verdict changes (distinct histories with at least one such change)': {k: len(v) for k, v in sorted(d['changes'].items())},
                 'examples': d['examples']} for fn, d in fns.items()}
    json.dump(out, open(os.path.join(SC, 'sweep.json'), 'w', encoding='utf-8'), indent=1, ensure_ascii=False, default=str)
    json.dump(out, open(os.path.join(ROOT, 'results', 'S129 Reading C carried into copies', 'suite boundary sweep.json'), 'w',
                        encoding='utf-8'), indent=1, ensure_ascii=False, default=str)
    print('claims run %d in %.0f s; claims computing provenance: %d' % (len(ids), out['seconds'], len(LOG)))
    for cid, fns in sorted(out['claims_that_compute_provenance'].items(), key=lambda kv: (int(kv[0][2:].split('.')[0]), kv[0])):
        print('%-11s %s | %s' % (cid, status[cid][:24], '; '.join('%s: %d distinct, %d boundary-relative' % (
            fn, d['distinct histories'], d['distinct histories whose verdict changes at some narrower boundary']) for fn, d in fns.items())))


if __name__ == '__main__':
    main()
