#!/usr/bin/env python3
"""s129_check_the_provenance_claims_at_every_boundary.py

What it does, in plain words: for log S129 (decision S83, Reading C). The formal claims about provenance (FC12.new1,
FC12.new2 (d), FC78, FC98.new1 (b), FC83) are universal statements the suite tests on every chain history of up to three
holdings, with no boundary declared. Under Reading C a provenance claim is made at a declared boundary. This script
recomputes each statement, on the S129 copy of the model, on the same exhaustive family of chains (each holding a record
of an earlier one or not; every pattern of held, trace and Sel's other conditions), at EVERY boundary that keeps the
last holding inside, and says whether the statement holds at every boundary as written, or only after rewording:
  (1) FC12.new1  ¬(Sel ∧ Con) at every fixed point, under the cuts U, K, T and T′
  (2) FC98.new1 (b), FC12.new2 (d)  exactly one fixed point under T′
  (3) FC12.new2 (d)  every record has its source's provenance (as written; and with the source outside β)
  (4) FC78  exactly one provenance per holding, at one boundary; and across two boundaries
  (5) FC83  a selected holding has no Build at the same boundary (Build read as Held under T′; holdings that are not
      records, as FC83's own family)
Output: printed, and results/S129 Reading C carried into copies/the provenance claims at every boundary.json.

  PYTHONHASHSEED=0 python3 -B Semantics/tools/s129_check_the_provenance_claims_at_every_boundary.py

Written 2 October 2026 by the one Opus 5.5 agent of log S129.
"""
import itertools, json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COPY = os.path.join(ROOT, 'results', 'S129 Reading C carried into copies', 'model after Reading C')
OUTF = os.path.join(ROOT, 'results', 'S129 Reading C carried into copies', 'the provenance claims at every boundary.json')
sys.path.insert(0, COPY)
os.environ.setdefault('S129_READING_C', '1')
os.environ.setdefault('S129_GRADED', '1')
from model.claims_b import prov_fixed_points, build_at, PROV_READINGS  # noqa: E402


def chains():
    for n in (1, 2, 3):
        for bits in itertools.product(itertools.product([0, 1], repeat=3), repeat=n):
            for rof in itertools.product(*[[None] + list(range(o)) for o in range(n)]):
                held = [1 if rof[o] is not None else b[0] for o, b in enumerate(bits)]
                yield n, held, [b[1] for b in bits], [b[2] for b in bits], list(rof)


def boundaries(n):
    for r in range(n):
        for sub in itertools.combinations(range(n - 1), r):
            yield frozenset(sub) | {n - 1}


def lab(sc):
    return 'Sel' if sc[0] else ('Con' if sc[1] else 'Dec')


def main():
    c = {k: 0 for k in ('chains', 'chain-boundary pairs', 'narrower boundaries')}
    bad = {k: [] for k in ('(1) Sel and Con together', '(2) not one fixed point under T′',
                           '(3) a record inside β with its source inside β differs from it',
                           '(5) Sel and Build at one holding')}
    rec_out = {'records inside β whose source is outside β': 0, 'of them, the source Sel or Con on the whole history': 0,
               'of them, the record Dec at β': 0}
    across = {'holdings inside a narrower β': 0, 'whose verdict at β differs from the whole history': 0, 'examples': []}
    for n, held, trace, selc, rof in chains():
        c['chains'] += 1
        whole = prov_fixed_points(n, held, trace, selc, "T'", True, rec_of=rof)
        for beta in boundaries(n):
            full = len(beta) == n
            b = None if full else set(beta)
            c['chain-boundary pairs'] += 1
            c['narrower boundaries'] += 0 if full else 1
            for rd in PROV_READINGS:
                fps = prov_fixed_points(n, held, trace, selc, rd, True, rec_of=rof, beta=b)
                for R, sc in fps:
                    if any(sc[o][0] and sc[o][1] for o in beta):
                        bad['(1) Sel and Con together'].append((n, held, trace, selc, rof, sorted(beta), rd))
            f = prov_fixed_points(n, held, trace, selc, "T'", True, rec_of=rof, beta=b)
            if len(f) != 1:
                bad['(2) not one fixed point under T′'].append((n, held, trace, selc, rof, sorted(beta)))
                continue
            R, sc = f[0]
            for o in beta:
                if rof[o] is not None and rof[o] in beta and sc[o] != sc[rof[o]]:
                    bad['(3) a record inside β with its source inside β differs from it'].append((n, held, trace, selc, rof, sorted(beta)))
                if rof[o] is not None and rof[o] not in beta:
                    rec_out['records inside β whose source is outside β'] += 1
                    if len(whole) == 1 and any(whole[0][1][rof[o]]):
                        rec_out['of them, the source Sel or Con on the whole history'] += 1
                    if not any(sc[o]):
                        rec_out['of them, the record Dec at β'] += 1
                # FC83's family has no records; a record that also has a trace of its own is an encoding D12.3 does not
                # cover (a composition of content-preserving transfers prepares nothing), so it is left out here
                if rof[o] is None and sc[o][0] and build_at(n, held, trace, "T'", R, o, b):
                    bad['(5) Sel and Build at one holding'].append((n, held, trace, selc, rof, sorted(beta)))
            if not full and len(whole) == 1:
                for o in beta:
                    across['holdings inside a narrower β'] += 1
                    if sc[o] != whole[0][1][o]:
                        across['whose verdict at β differs from the whole history'] += 1
                        if len(across['examples']) < 6:
                            across['examples'].append({'chain': 'n=%d held=%s trace=%s Sel-conditions=%s records=%s' % (n, held, trace, selc, rof),
                                                       'boundary': ['o%d' % (x + 1) for x in sorted(beta)], 'holding': 'o%d' % (o + 1),
                                                       'whole history': lab(whole[0][1][o]), 'at the boundary': lab(sc[o])})
    out = {'about': 'S129: the provenance claims recomputed at every boundary that keeps the last holding, on every chain of up to three '
                    'holdings (each a record of an earlier one or not), on the S129 copy of the model. Built by '
                    'tools/s129_check_the_provenance_claims_at_every_boundary.py.',
           'counts': c, 'failures (examples, at most 5 each)': {k: v[:5] for k, v in bad.items()},
           'failure counts': {k: len(v) for k, v in bad.items()},
           '(3) records whose source is outside β': rec_out, '(4) one holding, two boundaries': across}
    json.dump(out, open(OUTF, 'w', encoding='utf-8'), indent=1, ensure_ascii=False, default=str)
    print(json.dumps({k: v for k, v in out.items() if k != 'failures (examples, at most 5 each)'}, indent=1, ensure_ascii=False, default=str))


if __name__ == '__main__':
    main()
