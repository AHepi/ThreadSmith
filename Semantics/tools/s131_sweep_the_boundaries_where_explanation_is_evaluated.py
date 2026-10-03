#!/usr/bin/env python3
"""s131_sweep_the_boundaries_where_explanation_is_evaluated.py

What it does, in plain words: for log S131 (decision S86, explanation kept for what was worked out). S129 recomputed
every provenance verdict the suites make at every narrower system boundary (Reading C). The third decision changes a
verdict only where "explanation" is evaluated, that is, where the owner's condition or (Suff) is applied to a candidate
whose provenance is known: before S86 they ask whether the transport is declared, after it whether it is constructed,
so they differ exactly where the transport is SELECTED (neither declared nor constructed). This script runs, on the
S131 copy of the program, the claims that evaluate the owner's condition or (Suff) (found by searching the program for
suff_defeats and expl_ok: FC30.new1 and FC23.new2), with the copy's provenance functions wrapped as S129 wrapped them,
and for every provenance computation those claims make it records the verdict of the holding in question on the whole
stated history and at every narrower boundary (every proper subset of the stated occurrences, as S129's sweep took
them; for chains of holdings, those that keep the last holding), and whether S86 changes what the semantics says of
the candidate there (it does exactly where the verdict is Sel). The wrapped functions return what the copy computes
with no boundary, so each claim's own result is the copy's. Scale 1, time cap 20 s; the copy is imported, never
written. Output: printed, and results/S131 Explanation by construction carried into copies/suite boundary sweep where
explanation is evaluated.json.

  PYTHONHASHSEED=0 python3 -B Semantics/tools/s131_sweep_the_boundaries_where_explanation_is_evaluated.py

Written 2 October 2026 by the one Opus 5.5 agent of log S131.
"""
import copy as _copy, itertools, json, os, sys, time
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT, 'results', 'S131 Explanation by construction carried into copies')
COPY = os.path.join(OUT_DIR, 'model after Reading C and explanation by construction')
OUTF = os.path.join(OUT_DIR, 'suite boundary sweep where explanation is evaluated.json')
for k in ('S129_READING_C', 'S129_GRADED', 'S131_EXPL_BY_CONSTRUCTION', 'S131_CLAIMS_REWORDED'):
    os.environ.setdefault(k, '1')
sys.path.insert(0, COPY)

from model import claims_b as cb  # noqa: E402

ORIG = {'prov_fixed_points': cb.prov_fixed_points, 'sel': cb.sel, 'con': cb.con}
CUR = {'claim': None}
CLAIMS = ['FC23.new2', 'FC30.new1']
LOG = defaultdict(lambda: {'computations': 0, 'histories': {}, 'pairs': 0, 'pairs where S86 changes the verdict': 0,
                           'verdicts at the narrower boundaries': Counter(), 'verdicts on the whole history': Counter(),
                           'examples where S86 changes it at a narrower boundary only': []})


def lab(s, k):
    return 'Sel' if s else ('Con' if k else 'Dec')


def _subsets(items, keep=()):
    items = [x for x in items if x not in keep]
    for r in range(len(items)):
        for sub in itertools.combinations(items, r):
            yield set(sub) | set(keep)


def _record(key, whole, at, desc):
    rec = LOG[CUR['claim']]
    rec['computations'] += 1
    if key in rec['histories']:
        return
    rec['histories'][key] = desc
    rec['verdicts on the whole history'][whole] += 1
    for b, v in at:
        rec['pairs'] += 1
        rec['verdicts at the narrower boundaries'][v] += 1
        if v == 'Sel':
            rec['pairs where S86 changes the verdict'] += 1
            if whole != 'Sel' and len(rec['examples where S86 changes it at a narrower boundary only']) < 4:
                rec['examples where S86 changes it at a narrower boundary only'].append(
                    {'history': desc, 'on the whole history': whole, 'boundary (occurrences inside)': b, 'there': v})


def sel(cand, H, h, *a, **k):
    res = ORIG['sel'](cand, H, h, *a, **k)
    if getattr(h, 'beta', None) is None and CUR['claim'] is not None:
        names = list(dict.fromkeys(list(h.occ) + [o for o, _ in h.rep] + list(h.source)))
        whole = lab(res, ORIG['con'](h))
        at = []
        for b in _subsets(names):
            h2 = _copy.copy(h)
            h2.beta = set(b)
            at.append((sorted(b), lab(ORIG['sel'](cand, H, h2, *a, **k), ORIG['con'](h2))))
        key = ('tagged', tuple(h.occ), tuple(sorted(h.rep)), h.admitted, h.prepares, whole, tuple(sorted(k.items())))
        _record(key, whole, at, 'tagged history: occurrences %s, tags %s, admitted %s, prepares %s%s' % (
            list(h.occ), sorted(h.rep), h.admitted, h.prepares, (' ' + str(k)) if k else ''))
    return res


def pfp(n, held, trace, selc, rd, i161=True, eps=None, rec_of=None, beta=None):
    res = ORIG['prov_fixed_points'](n, held, trace, selc, rd, i161, eps, rec_of, beta)
    if beta is None and CUR['claim'] is not None:
        last = lambda fps: '/'.join(sorted(set(lab(sc[n - 1][0], sc[n - 1][1]) for R, sc in fps))) or 'no fixed point'
        whole = last(res)
        at = []
        for b in _subsets(range(n), keep=(n - 1,)):
            at.append((['o%d' % (o + 1) for o in sorted(b)], last(ORIG['prov_fixed_points'](n, held, trace, selc, rd, i161, eps, rec_of, b))))
        key = ('chain', n, tuple(held), tuple(trace), tuple(selc), rd, tuple(rec_of) if rec_of else None)
        _record(key, whole, at, 'chain of %d holdings: held %s, trace %s, Sel-conditions %s, cut %s, records %s' % (
            n, list(held), list(trace), list(selc), rd, rec_of))
    return res


cb.prov_fixed_points, cb.sel = pfp, sel
from model import run as mrun  # noqa: E402  (imports the claim modules after the wrapping)
from model.harness import Settings  # noqa: E402


def main():
    S = Settings(scale=1.0, time_cap=20.0)
    status = {}
    t0 = time.time()
    for cid in CLAIMS:
        CUR['claim'] = cid
        r = mrun.run_claim(cid, S)
        status[cid] = r['status'] + (' (error)' if r['error'] else '')
        CUR['claim'] = None
    out = {'about': 'S131: the claims that evaluate the owner\'s condition or (Suff) (FC23.new2, FC30.new1), run on the S131 copy '
                    '(READING_C %s, GRADED %s, EXPL_BY_CONSTRUCTION %s), with every provenance computation they make recomputed on '
                    'the whole stated history and at every narrower boundary; S86 changes what the semantics says of a candidate '
                    'exactly where the holding in question is Sel there. Scale 1, time cap 20 s. Built by '
                    'tools/s131_sweep_the_boundaries_where_explanation_is_evaluated.py.' % (cb.READING_C, cb.GRADED, cb.EXPL_BY_CONSTRUCTION),
           'seconds': round(time.time() - t0, 1), 'statuses at scale 1': status, 'claims': {}}
    for cid, d in LOG.items():
        out['claims'][cid] = {'provenance computations': d['computations'], 'distinct histories': len(d['histories']),
                              'verdicts on the whole history (distinct histories)': dict(d['verdicts on the whole history']),
                              'S86 changes the verdict on the whole history (Sel there)': d['verdicts on the whole history'].get('Sel', 0),
                              'narrower boundary and history pairs': d['pairs'],
                              'verdicts at the narrower boundaries': dict(d['verdicts at the narrower boundaries']),
                              'pairs where S86 changes the verdict (Sel there)': d['pairs where S86 changes the verdict'],
                              'examples where S86 changes it at a narrower boundary only': d['examples where S86 changes it at a narrower boundary only'],
                              'the distinct histories': sorted(d['histories'].values())}
    json.dump(out, open(OUTF, 'w', encoding='utf-8'), indent=1, ensure_ascii=False, default=str)
    print(json.dumps({k: v for k, v in out.items() if k != 'claims'}, ensure_ascii=False))
    for cid, v in out['claims'].items():
        print(cid, json.dumps({k: x for k, x in v.items() if k != 'the distinct histories'}, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
