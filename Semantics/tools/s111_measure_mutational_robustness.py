#!/usr/bin/env python3
"""s111_measure_mutational_robustness.py

What it does, in plain words: the measure R1 of "resists change" from the S111 plan. For the ancestor, and for the most
common genotype (the "dominant") of each world run at updates 10,000, 30,000 and 50,000, it makes every program that
differs from it in exactly one instruction (each site changed to each of the 25 other instructions of the set) and runs
each alone in Avida's test processor (s111_avida_test_processor.py). It reports the share of these one-change programs
that still make an exact copy of themselves ("viable"), the share whose fitness is also unchanged ("neutral": viable and
fitness within one part in a million), the share that no longer copy themselves ("lethal"), and the share with higher
fitness. Added after the plan was written (and marked so in the results): the share that are viable with fitness within
1% (the plan's "within one part in a million" counts a one-cycle change in copying time as a change). Then it sets the low error rate beside the high one (R2). Writes a compact summary (JSON and Markdown) into
"Semantics/results/S111 Avida - the runs/".

  python3 Semantics/tools/s111_measure_mutational_robustness.py

Written 29 September 2026 by the one Opus 5.5 agent of log S111.
"""
import json, os, statistics, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import s111_avida_test_processor as T  # noqa: E402
from s111_run_the_avida_worlds import OUT as RUNS, RATES, SEEDS, ancestor_letters  # noqa: E402
from s111_measure_the_worlds_over_time import spop  # noqa: E402

RES = os.path.join(os.path.dirname(HERE), 'results', 'S111 Avida - the runs')
SAVES = [10000, 30000, 50000]
EPS = 1e-6


def scan(seq):
    base = T.evaluate([seq])[0]
    muts = [seq[:i] + c + seq[i + 1:] for i in range(len(seq)) for c in T.LETTERS if c != seq[i]]
    rows = T.evaluate(muts)
    w = base['fitness']
    n = len(rows)
    viable = [r for r in rows if r['viable']]
    neutral = [r for r in viable if w > 0 and abs(r['fitness'] / w - 1) <= EPS]
    better = [r for r in viable if w > 0 and r['fitness'] / w > 1 + EPS]
    near = [r for r in viable if w > 0 and abs(r['fitness'] / w - 1) <= 0.01]   # added after the plan: see the results file
    per_site_viable = [sum(rows[i * 25 + k]['viable'] for k in range(25)) / 25 for i in range(len(seq))]
    return {'length': len(seq), 'viable_itself': base['viable'], 'fitness': w, 'gestation': base['gest_time'],
            'tasks': [T.TASKS[k] for k in range(9) if base['task.%d' % k] > 0],
            'mutants': n, 'share_viable': round(len(viable) / n, 4), 'share_neutral': round(len(neutral) / n, 4),
            'share_viable_fitness_within_1_percent': round(len(near) / n, 4),
            'share_lethal': round(1 - len(viable) / n, 4), 'share_higher_fitness': round(len(better) / n, 4),
            'sites_where_every_change_is_lethal': sum(1 for v in per_site_viable if v == 0),
            'sites_where_no_change_is_lethal': sum(1 for v in per_site_viable if v == 1)}


def dominant(run, u):
    p = os.path.join(RUNS, run, 'data', 'detail-%d.spop' % u)
    if not os.path.exists(p):
        return None
    pop = spop(p)
    seq, n = max(pop, key=lambda x: x[1])
    return seq, n, sum(k for _, k in pop)


def spread(v):
    return {'mean': round(statistics.mean(v), 4), 'min': round(min(v), 4), 'max': round(max(v), 4), 'each': v}


def main():
    out = {'ancestor': scan(ancestor_letters()), 'runs': {}, 'by_condition': {}}
    print('ancestor', out['ancestor'], flush=True)
    for cond in RATES:
        for seed in SEEDS:
            run = 'main_%s_seed%d' % (cond, seed)
            for u in SAVES:
                d = dominant(run, u)
                if not d:
                    continue
                r = scan(d[0])
                r.update({'abundance': d[1], 'organisms': d[2], 'sequence': d[0]})
                out['runs'].setdefault(run, {})[u] = r
                print(run, u, {k: r[k] for k in ('length', 'share_viable', 'share_neutral', 'tasks')}, flush=True)
        for u in SAVES:
            rs = [out['runs'][('main_%s_seed%d' % (cond, s))][u] for s in SEEDS
                  if u in out['runs'].get('main_%s_seed%d' % (cond, s), {})]
            if rs:
                out['by_condition'].setdefault(cond, {})[u] = {k: spread([r[k] for r in rs]) for k in
                                                               ('share_viable', 'share_neutral', 'share_lethal',
                                                                'share_higher_fitness', 'length',
                                                                'share_viable_fitness_within_1_percent')}
    # R2: low beside high, the rule of the plan: a difference only if every seed of one lies beyond every seed of the other
    cmp = {}
    for u in SAVES:
        lo, hi = out['by_condition'].get('low', {}).get(u), out['by_condition'].get('high', {}).get(u)
        if lo and hi:
            for k in ('share_viable', 'share_neutral', 'share_viable_fitness_within_1_percent'):
                a, b = lo[k], hi[k]
                verdict = 'high above low' if b['min'] > a['max'] else 'low above high' if a['min'] > b['max'] else 'no clear difference'
                cmp['%s at %d' % (k, u)] = verdict
    out['low_beside_high'] = cmp
    with open(os.path.join(RES, 'mutational robustness.json'), 'w') as f:
        json.dump(out, f, indent=1)
    L = ['# S111 mutational robustness (written by tools/s111_measure_mutational_robustness.py)', '',
         'Every one-instruction change of each genotype, run alone in the test processor. "viable": still makes an exact copy '
         'of itself; "neutral": viable and fitness unchanged (within one part in a million).', '',
         'Ancestor: %(length)d instructions, %(mutants)d one-change programs; viable %(share_viable).3f, neutral '
         '%(share_neutral).3f, lethal %(share_lethal).3f, higher fitness %(share_higher_fitness).3f.' % out['ancestor'], '',
         '| run | update | length | tasks | viable | neutral | within 1% | lethal | higher fitness |', '|---|---|---|---|---|---|---|---|---|']
    for run, d in out['runs'].items():
        for u, r in d.items():
            L.append('| %s | %d | %d | %s | %.3f | %.3f | %.3f | %.3f | %.3f |' % (run, u, r['length'], ' '.join(r['tasks']) or '-',
                     r['share_viable'], r['share_neutral'], r['share_viable_fitness_within_1_percent'], r['share_lethal'],
                     r['share_higher_fitness']))
    L += ['', '## By condition (mean, smallest to largest over the three seeds)', '',
          '| condition | update | viable | neutral | within 1% | lethal | length |', '|---|---|---|---|---|---|---|']
    for cond, d in out['by_condition'].items():
        for u, s in d.items():
            L.append('| %s | %d | %s | %s | %s | %s | %s |' % (cond, u, *('%.3f (%.3f to %.3f)' % (s[k]['mean'], s[k]['min'], s[k]['max'])
                     for k in ('share_viable', 'share_neutral', 'share_viable_fitness_within_1_percent', 'share_lethal')),
                     '%.0f (%.0f to %.0f)' % (s['length']['mean'], s['length']['min'], s['length']['max'])))
    L += ['', '## Low beside high (R2; the plan\'s rule: a difference only if every seed of one lies beyond every seed of the other)', '']
    L += ['- %s: %s' % (k, v) for k, v in cmp.items()]
    with open(os.path.join(RES, 'mutational robustness.md'), 'w') as f:
        f.write('\n'.join(L) + '\n')
    print('\n'.join(L))


if __name__ == '__main__':
    main()
