#!/usr/bin/env python3
"""s111_measure_the_worlds_over_time.py

What it does, in plain words: reads what Avida wrote during the S111 world runs (in the scratch space) and measures, per
run and at each saved moment:
  C3  copy fidelity in the world: births whose offspring was identical to its parent, divided by all births
      (Avida's own counts, at the 50 updates it saved, 1,000 to 50,000);
  C4  offspring per organism: births per organism per update; the average generation reached;
  C5, M1  the number of organisms over time;
  R3  conservation: every living genotype aligned to the ancestor (one point for a match, minus one for a mismatch or a
      gap); for each of the ancestor's sites, the share of organisms whose aligned instruction is still the ancestor's;
      averaged separately over the 15 essential sites (whose knockout stops self-copying, from
      "copying and knockouts.json") and the 85 others;
  M2  the share of organisms carrying the ancestor's copy loop and its head exactly, and the whole ancestral genome;
      added after the plan (marked so in the results): the share of organisms whose genotype, run alone in Avida's test
      processor, still makes an exact copy of itself;
  tasks: organisms performing each of the nine logic tasks at the end;
and the controls K1 to K5. Writes a compact summary (JSON and a Markdown table) into
"Semantics/results/S111 Avida - the runs/".

  python3 Semantics/tools/s111_measure_the_worlds_over_time.py

Written 29 September 2026 by the one Opus 5.5 agent of log S111.
"""
import json, os, statistics, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from s111_run_the_avida_worlds import OUT as RUNS, RATES, SEEDS  # noqa: E402
import s111_avida_test_processor as T  # noqa: E402

RES = os.path.join(os.path.dirname(HERE), 'results', 'S111 Avida - the runs')
TASKS = ['NOT', 'NAND', 'AND', 'ORN', 'OR', 'ANDN', 'NOR', 'XOR', 'EQU']
SAVES = [1000, 10000, 20000, 30000, 40000, 50000]


def table(path):
    rows = []
    for line in open(path):
        if line.startswith('#') or not line.strip():
            continue
        rows.append([float(x) for x in line.split()[:20] if _num(x)])
    return rows


def _num(x):
    try:
        float(x)
        return True
    except ValueError:
        return False


def spop(path):
    """Living genotypes: list of (sequence, number alive)."""
    fmt, out = None, []
    for line in open(path):
        if line.startswith('#format'):
            fmt = line.split()[1:]
            continue
        if line.startswith('#') or not line.strip():
            continue
        w = line.split()
        r = dict(zip(fmt, w))
        n = int(r['num_units'])
        if n > 0:
            out.append((r['sequence'], n))
    return out


def align(anc, seq):
    """Global alignment (match +1, mismatch -1, gap -1). Returns, for each ancestral site, the aligned letter or '-'."""
    a = np.frombuffer(anc.encode(), dtype=np.uint8)
    b = np.frombuffer(seq.encode(), dtype=np.uint8)
    n, m = len(a), len(b)
    H = np.zeros((n + 1, m + 1), dtype=np.int32)
    H[0, :] = -np.arange(m + 1)
    H[:, 0] = -np.arange(n + 1)
    ar = np.arange(m + 1)
    for i in range(1, n + 1):
        s = np.where(b == a[i - 1], 1, -1)
        X = np.empty(m + 1, dtype=np.int32)
        X[0] = H[i, 0]
        X[1:] = np.maximum(H[i - 1, :-1] + s, H[i - 1, 1:] - 1)
        H[i] = np.maximum.accumulate(X + ar) - ar
    out = ['-'] * n
    i, j = n, m
    while i > 0 and j > 0:
        s = 1 if a[i - 1] == b[j - 1] else -1
        if H[i, j] == H[i - 1, j - 1] + s:
            out[i - 1] = seq[j - 1]
            i, j = i - 1, j - 1
        elif H[i, j] == H[i - 1, j] - 1:
            i -= 1
        else:
            j -= 1
    return out


def conservation(anc, pop, essential):
    total = sum(n for _, n in pop)
    per_site = np.zeros(len(anc))
    for seq, n in pop:
        al = align(anc, seq)
        per_site += n * np.array([1.0 if al[k] == anc[k] else 0.0 for k in range(len(anc))])
    per_site /= total
    ess = [s - 1 for s in essential]
    non = [k for k in range(len(anc)) if k not in ess]
    return {'essential': round(float(per_site[ess].mean()), 4), 'non_essential': round(float(per_site[non].mean()), 4),
            'essential_min_site': round(float(per_site[ess].min()), 4),
            'per_site': [round(float(x), 3) for x in per_site]}


def shares(anc, pop):
    total = sum(n for _, n in pop)
    loop, head = anc[-9:], anc[:5]
    return {'organisms': total, 'genotypes': len(pop),
            'copy_loop_exact': round(sum(n for s, n in pop if loop in s) / total, 4),
            'head_exact': round(sum(n for s, n in pop if head in s) / total, 4),
            'whole_ancestor': round(sum(n for s, n in pop if s == anc) / total, 4),
            'mean_length': round(sum(len(s) * n for s, n in pop) / total, 1)}


def one_run(name, anc, essential, saves):
    d = os.path.join(RUNS, name, 'data')
    count = table(os.path.join(d, 'count.dat'))
    time_ = table(os.path.join(d, 'time.dat'))
    tasks = table(os.path.join(d, 'tasks.dat'))
    later = [r for r in count if r[0] >= 1000]
    births = sum(r[8] for r in later)
    same = sum(r[10] for r in later)
    res = {'run': name, 'last_update': int(count[-1][0]),
           'organisms_min_from_1000': int(min(r[2] for r in later)), 'organisms_at_end': int(count[-1][2]),
           'births_sampled': int(births), 'share_births_identical_to_parent': round(same / births, 4) if births else None,
           'births_per_organism_per_update': round(statistics.mean(r[8] / r[2] for r in later), 4),
           'average_generation_at_end': round(time_[-1][2], 1),
           'tasks_at_end': {t: int(tasks[-1][k + 1]) for k, t in enumerate(TASKS)},
           'first_update_task_seen': {t: next((int(r[0]) for r in tasks if r[k + 1] > 0), None) for k, t in enumerate(TASKS)},
           'saves': {}}
    for u in saves:
        p = os.path.join(d, 'detail-%d.spop' % u)
        if not os.path.exists(p):
            continue
        pop = spop(p)
        s = shares(anc, pop)
        c = conservation(anc, pop, essential)
        s.update({'conserved_essential': c['essential'], 'conserved_non_essential': c['non_essential'],
                  'conserved_essential_least_site': c['essential_min_site']})
        # added after the plan (see the results file): the share of organisms whose genotype, run alone in the test
        # processor, still makes an exact copy of itself; every living genotype is run
        ev = T.evaluate([q for q, _ in pop])
        s['share_organisms_self_copying'] = round(sum(n for (q, n), r in zip(pop, ev) if r['viable']) / s['organisms'], 4)
        res['saves'][u] = s
        res['per_site_conservation_at_last_save'] = c['per_site']
    return res


def spread(vals):
    vals = [v for v in vals if v is not None]
    return {'mean': round(statistics.mean(vals), 4), 'min': round(min(vals), 4), 'max': round(max(vals), 4), 'each': vals}


def main():
    ck = json.load(open(os.path.join(RES, 'copying and knockouts.json')))
    anc, essential = ck['ancestor']['letters'], ck['essential_sites']
    out = {'runs': {}, 'by_condition': {}, 'controls': {}}
    for cond in RATES:
        rs = []
        for seed in SEEDS:
            name = 'main_%s_seed%d' % (cond, seed)
            if not os.path.exists(os.path.join(RUNS, name, 'data', 'count.dat')):
                continue
            r = one_run(name, anc, essential, SAVES)
            out['runs'][name] = r
            rs.append(r)
            print(name, 'done', flush=True)
        if not rs:
            continue
        last = [r['saves'][max(r['saves'])] for r in rs]
        out['by_condition'][cond] = {
            'copy_error_rate': RATES[cond], 'runs': len(rs),
            'share_births_identical_to_parent': spread([r['share_births_identical_to_parent'] for r in rs]),
            'births_per_organism_per_update': spread([r['births_per_organism_per_update'] for r in rs]),
            'average_generation_at_end': spread([r['average_generation_at_end'] for r in rs]),
            'organisms_min_from_1000': spread([r['organisms_min_from_1000'] for r in rs]),
            'at_last_save': {k: spread([s[k] for s in last]) for k in
                             ['conserved_essential', 'conserved_non_essential', 'copy_loop_exact', 'head_exact',
                              'share_organisms_self_copying',
                              'whole_ancestor', 'mean_length', 'genotypes']},
            'tasks_at_end_runs_with_any': {t: sum(1 for r in rs if r['tasks_at_end'][t] > 0) for t in TASKS}}
    # controls
    for name in sorted(os.listdir(RUNS)):
        if not name.startswith('control_'):
            continue
        d = os.path.join(RUNS, name, 'data')
        count = table(os.path.join(d, 'count.dat'))
        c = {'last_update_with_organisms': int(max(r[0] for r in count if r[2] > 0)),
             'organisms_at_last_line': int(count[-1][2]), 'births_after_update_0': int(sum(r[8] for r in count if r[0] > 0))}
        if 'K4' in name:
            ko = anc[:anc.rindex('v')] + 'A' + anc[anc.rindex('v') + 1:]
            for u in [500, 1000, 1500, 2000]:
                p = os.path.join(d, 'detail-%d.spop' % u)
                if os.path.exists(p):
                    pop = spop(p)
                    c['knocked_out_alive_at_%d' % u] = sum(n for s, n in pop if s == ko)
                    c['organisms_at_%d' % u] = sum(n for s, n in pop)
        if 'K5' in name:
            pop = spop(os.path.join(d, 'detail-5000.spop'))
            s = shares(anc, pop)
            cc = conservation(anc, pop, essential)
            s.update({'conserved_essential': cc['essential'], 'conserved_non_essential': cc['non_essential']})
            c['at_5000'] = s
            later = [r for r in count if r[0] >= 1000]
            c['share_births_identical_to_parent'] = round(sum(r[10] for r in later) / sum(r[8] for r in later), 4)
        out['controls'][name] = c
    with open(os.path.join(RES, 'the worlds over time.json'), 'w') as f:
        json.dump(out, f, indent=1)
    write_md(out)


def fmt(s, p=3):
    return '%.*f (%.*f to %.*f)' % (p, s['mean'], p, s['min'], p, s['max'])


def write_md(out):
    L = ['# S111 the worlds over time (written by tools/s111_measure_the_worlds_over_time.py)', '',
         'Each cell: the mean over the seeds, with the smallest and largest in brackets. "At the last save": update 50,000.', '',
         '| measure | ' + ' | '.join(out['by_condition']) + ' |', '|---|' + '---|' * len(out['by_condition'])]
    rows = [('copy error rate', lambda c: str(c['copy_error_rate'])),
            ('runs', lambda c: str(c['runs'])),
            ('births with offspring identical to parent (C3)', lambda c: fmt(c['share_births_identical_to_parent'])),
            ('births per organism per update (C4)', lambda c: fmt(c['births_per_organism_per_update'], 4)),
            ('average generation at the end (C4)', lambda c: fmt(c['average_generation_at_end'], 0)),
            ('fewest organisms from update 1,000 on (M1)', lambda c: fmt(c['organisms_min_from_1000'], 0))]
    for k, lab in [('conserved_essential', 'essential sites still the ancestor\'s (R3)'),
                   ('conserved_non_essential', 'non-essential sites still the ancestor\'s (R3)'),
                   ('copy_loop_exact', 'organisms with the ancestor\'s copy loop exactly (M2)'),
                   ('head_exact', 'organisms with the ancestor\'s head exactly (M2)'),
                   ('share_organisms_self_copying', 'organisms whose genotype still copies itself exactly (added)'),
                   ('whole_ancestor', 'organisms identical to the ancestor (M2)'),
                   ('mean_length', 'mean genome length'), ('genotypes', 'living genotypes')]:
        rows.append((lab + ', at the last save', (lambda k: lambda c: fmt(c['at_last_save'][k], 1 if k in ('mean_length', 'genotypes') else 3))(k)))
    rows.append(('runs performing each task at the end (NOT, NAND, AND, ORN, OR, ANDN, NOR, XOR, EQU)',
                 lambda c: ' '.join(str(v) for v in c['tasks_at_end_runs_with_any'].values())))
    for lab, f in rows:
        L.append('| %s | %s |' % (lab, ' | '.join(f(c) for c in out['by_condition'].values())))
    L += ['', '## Over time, per run: essential / non-essential sites still the ancestor\'s, and share with the copy loop exactly', '',
          'Each cell: essential sites / non-essential sites still the ancestor\'s / share with the copy loop exactly / share '
          'whose genotype still copies itself exactly (added).', '',
          '| run | ' + ' | '.join(str(u) for u in SAVES) + ' |', '|---|' + '---|' * len(SAVES)]
    for name, r in out['runs'].items():
        L.append('| %s | %s |' % (name, ' | '.join('%.2f / %.2f / %.2f / %.2f' % (r['saves'][u]['conserved_essential'],
                 r['saves'][u]['conserved_non_essential'], r['saves'][u]['copy_loop_exact'],
                 r['saves'][u]['share_organisms_self_copying']) if u in r['saves'] else '-' for u in SAVES)))
    L += ['', '## Tasks at the end, organisms performing each (of about 3,600)', '', '| run | ' + ' | '.join(TASKS) + ' |',
          '|---|' + '---|' * len(TASKS)]
    for name, r in out['runs'].items():
        L.append('| %s | %s |' % (name, ' | '.join(str(r['tasks_at_end'][t]) for t in TASKS)))
    L += ['', '## Controls', '']
    for name, c in out['controls'].items():
        L.append('- %s: %s' % (name, json.dumps(c)))
    with open(os.path.join(RES, 'the worlds over time.md'), 'w') as f:
        f.write('\n'.join(L) + '\n')
    print('\n'.join(L))


if __name__ == '__main__':
    main()
