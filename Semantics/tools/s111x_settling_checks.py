#!/usr/bin/env python3
"""s111x_settling_checks.py - log S111, the GLM cross-examination settled (results/S111 Avida - the GLM cross-examination, settled.md).
Written 29 September 2026 by the Opus 5.5 agent that settled the cross-examination; run from the scratch space, output there;
the numbers are in "results/S111 Avida - the three properties measured, after the cross-examination.json". Modes:
  inputs_scan  : Xc4/Xa6 - one-change scan of the 9 dominants at 50,000 under two other input triples; neutral/viable shares
  inputs_tasks : Xa6 - genotypes covering 90% at 50,000: share performing each task under fixed vs two other input triples
  evolved_map  : Xc1 - each dominant's own nop-X knockout map; conservation relative to the dominant, its essential vs rest
Uses only Avida's analysis mode (test processor); nothing self-copying runs on the real machine."""
import json, os, random, shutil, sys, statistics
T_DIR = '/home/user/ThreadSmith/Semantics/tools'
sys.path.insert(0, T_DIR)
import numpy as np
import s111_avida_test_processor as T
from s111_run_the_avida_worlds import RATES, SEEDS
from s111_measure_the_worlds_over_time import spop, align
from s111_measure_mutational_robustness import dominant, EPS
OUT = '/tmp/claude-0/-home-user-ThreadSmith/8d9323da-c0ec-57ec-91fd-8f99ca99320a/scratchpad/s111x_settle'   # scratch only
RUNS = ['main_%s_seed%d' % (c, s) for c in RATES for s in SEEDS]
rng = random.Random(1110)
INPUTS = {'alt%d' % k: [(15 << 24) + rng.getrandbits(24), (51 << 24) + rng.getrandbits(24), (85 << 24) + rng.getrandbits(24)]
          for k in (1, 2)}


def evaluate(seqs, inputs=None, timeout=3600):
    out = []
    for start in range(0, len(seqs), T.CHUNK):
        part = seqs[start:start + T.CHUNK]
        d, argv = T._folder(None)
        rc = 'RECALCULATE' if inputs is None else 'RECALCULATE 0 -1 0 %d %d %d' % tuple(inputs)
        T._run(d, argv, ['LOAD_SEQUENCE ' + s for s in part] + [rc, 'DETAIL out.dat ' + ' '.join(T.FIELDS)], timeout)
        rows = T._read(os.path.join(d, 'data', 'out.dat'), T.FIELDS)
        assert len(rows) == len(part) and all(r['sequence'] == s for r, s in zip(rows, part)), d
        out += rows
        shutil.rmtree(d)
    return out


def scan_shares(seq, inputs):
    base = evaluate([seq], inputs)[0]
    muts = [seq[:i] + c + seq[i + 1:] for i in range(len(seq)) for c in T.LETTERS if c != seq[i]]
    rows = evaluate(muts, inputs)
    w = base['fitness']
    via = [r for r in rows if r['viable']]
    neu = [r for r in via if w > 0 and abs(r['fitness'] / w - 1) <= EPS]
    near = [r for r in via if w > 0 and abs(r['fitness'] / w - 1) <= 0.01]
    return {'base_fitness': w, 'base_tasks': [T.TASKS[k] for k in range(9) if base['task.%d' % k] > 0],
            'viable': round(len(via) / len(rows), 4), 'neutral': round(len(neu) / len(rows), 4),
            'within_1_percent': round(len(near) / len(rows), 4)}


def top90(pop):
    pop = sorted(pop, key=lambda x: -x[1])
    tot, acc, top = sum(n for _, n in pop), 0, []
    for s, n in pop:
        if acc >= 0.9 * tot:
            break
        top.append((s, n)); acc += n
    return top, tot


mode = sys.argv[1]
res = {'inputs': INPUTS}
for run in RUNS:
    seq, n, tot = dominant(run, 50000)
    if mode == 'inputs_scan':
        res[run] = {k: scan_shares(seq, v) for k, v in [('fixed', None)] + list(INPUTS.items())}
    elif mode == 'inputs_tasks':
        top, tot = top90(spop(os.path.join(T.SCRATCH, 's111', 'runs', run, 'data', 'detail-50000.spop')))
        cov = sum(n for _, n in top)
        r = {'covered': cov}
        for k, v in [('fixed', None)] + list(INPUTS.items()):
            rows = evaluate([s for s, _ in top], v)
            r[k] = {T.TASKS[t]: round(sum(n for (s, n), x in zip(top, rows) if x['task.%d' % t] > 0) / cov, 4) for t in range(9)}
            r[k]['viable'] = round(sum(n for (s, n), x in zip(top, rows) if x['viable']) / cov, 4)
        # genotypes whose task set differs between fixed and either alternative
        rows_f = evaluate([s for s, _ in top]); rows_a = [evaluate([s for s, _ in top], v) for v in INPUTS.values()]
        diff = sum(n for i, (s, n) in enumerate(top)
                   if any(any((rows_f[i]['task.%d' % t] > 0) != (ra[i]['task.%d' % t] > 0) for t in range(9)) for ra in rows_a))
        r['share_with_task_set_changed_by_inputs'] = round(diff / cov, 4)
        res[run] = r
    elif mode == 'evolved_map':
        kos = evaluate([seq[:i] + T.NULL + seq[i + 1:] for i in range(len(seq))])
        ess = [i for i, r in enumerate(kos) if not r['viable']]
        pop = spop(os.path.join(T.SCRATCH, 's111', 'runs', run, 'data', 'detail-50000.spop'))
        per = np.zeros(len(seq)); total = 0
        for s, k in pop:
            al = align(seq, s)
            per += k * np.array([1.0 if al[j] == seq[j] else 0.0 for j in range(len(seq))]); total += k
        per /= total
        non = [j for j in range(len(seq)) if j not in ess]
        res[run] = {'dominant_length': len(seq), 'dominant_abundance': n, 'essential_sites_in_dominant': len(ess),
                    'essential_sites': [j + 1 for j in ess],
                    'conserved_essential_rel_dominant': round(float(per[ess].mean()), 4),
                    'conserved_non_essential_rel_dominant': round(float(per[non].mean()), 4)}
    print(run, json.dumps(res[run])[:300], flush=True)
json.dump(res, open(os.path.join(OUT, mode + '.json'), 'w'), indent=1)
print('done', mode)
