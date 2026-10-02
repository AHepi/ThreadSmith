#!/usr/bin/env python3
"""s126_read_the_results.py

What it does, in plain words: for log S126 (the closing knock-out test), reads Avida's own data files from every arm
(the level of each task's store at every update, the number of times each task was executed at every update, the
programs and births every 10 updates) and applies the measures and the criteria fixed before running (the plan,
section 6): the window of updates 201 to 1,000 after a reload; the L0 band; whether the cut works, whether q's store
recovers under the cut and not under the sham, whether the other eight stores stay, whether the restored programs draw
the store down again. It changes nothing in any run. It writes the results JSON into the repository's results folder
and prints the tables used in the results file.

  python3 -B Semantics/tools/s126_read_the_results.py

Written 2 October 2026 by the one Opus 5.5 agent of log S126.
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import s126_run_the_arms as R  # noqa: E402

TASKS = R.TASKS
RESULTS = os.path.join(os.path.dirname(HERE), 'results', 'S126 The closing knock-out test - results.json')
WINDOW = (201, 1000)
MARKS = [0, 1, 5, 10, 25, 50, 100, 200, 300, 500, 750, 1000, 1500, 2000, 2500, 3000]


def rows(path):
    return [[float(x) for x in l.split()] for l in open(path) if l.strip() and not l.startswith('#')]


def read_run(d):
    meta = json.load(open(os.path.join(d, 'run.json')))
    res = rows(os.path.join(d, 'data', 'resource.dat'))
    exe = rows(os.path.join(d, 'data', 'tasks_exe.dat'))
    cnt = rows(os.path.join(d, 'data', 'count.dat'))
    tsk = rows(os.path.join(d, 'data', 'tasks.dat'))
    return {'meta': meta,
            'store': {t: {int(r[0]): r[1 + k] for r in res} for k, t in enumerate(TASKS)},
            'exe': {t: {int(r[0]): r[1 + k] for r in exe} for k, t in enumerate(TASKS)},
            'programs': {int(r[0]): r[2] for r in cnt},
            'births': {int(r[0]): r[8] for r in cnt},
            'credited': {t: {int(r[0]): r[1 + k] for r in tsk} for k, t in enumerate(TASKS)}}


def mean(xs):
    xs = list(xs)
    return sum(xs) / len(xs) if xs else float('nan')


def window_mean(series, lo=WINDOW[0], hi=WINDOW[1]):
    return mean(v for u, v in series.items() if lo <= u <= hi)


def band(values):
    lo, hi = min(values), max(values)
    t = max(2 * (hi - lo), 0.25 * mean(values))
    return lo - t, hi + t


def main():
    out = {'window': list(WINDOW), 'populations': {}, 'cpu_seconds': {}}
    total_cpu = 0.0
    for d in sorted(os.listdir(R.RUNS)):
        p = os.path.join(R.RUNS, d, 'run.json')
        if os.path.exists(p):
            m = json.load(open(p))
            total_cpu += m.get('cpu_seconds', 0)
            out['cpu_seconds'][d] = m.get('cpu_seconds')
    out['cpu_seconds_all_runs'] = round(total_cpu, 1)
    for pop in R.POPS:
        cuts = R.read_cuts(pop)
        q = cuts['summary']['q']
        runs = {}
        for arm in ['L0', 'Lq', 'Ls', 'Lr', 'Lq-then-restored', 'Lq-then-reloaded']:
            for seed in R.SEEDS[pop]:
                d = os.path.join(R.RUNS, 'pop%d_%s_seed%d' % (pop, arm, seed))
                if os.path.exists(os.path.join(d, 'data', 'resource.dat')):
                    runs[(arm, seed)] = read_run(d)
        P = {'q': q, 'arms': {}}
        l0 = [runs[('L0', s)] for s in R.SEEDS[pop] if ('L0', s) in runs]
        bands = {t: band([window_mean(r['store'][t]) for r in l0]) for t in TASKS}
        P['L0 band of each store'] = {t: [round(x, 1) for x in bands[t]] for t in TASKS}
        l0_exe_first100 = mean(mean(r['exe'][q][u] for u in range(1, 101)) for r in l0)
        l0_prog_1000 = mean(r['programs'][1000] for r in l0)
        P['L0 q executions per update, updates 1-100'] = round(l0_exe_first100, 2)
        for (arm, seed), r in sorted(runs.items()):
            n = r['meta']['updates']
            st = r['store'][q]
            row = {
                'updates': n, 'cpu_seconds': r['meta'].get('cpu_seconds'),
                'q store window mean': round(window_mean(st), 1),
                'q store in L0 band': bands[q][0] <= window_mean(st) <= bands[q][1],
                'q store at': {u: round(st[u], 1) for u in MARKS if u in st},
                'q executions per update, mean over bins': {
                    '%d-%d' % (a, b): round(mean(r['exe'][q][u] for u in range(a, b + 1) if u in r['exe'][q]), 2)
                    for a, b in [(1, 10), (11, 100), (101, 250), (251, 500), (501, 1000), (1001, 1500), (1501, 2000),
                                 (2001, 2500), (2501, 3000)] if b <= n},
                'programs at': {u: r['programs'][u] for u in (0, 100, 500, 1000, 2000, 3000) if u in r['programs']},
                'births per update, mean 1-1000': round(mean(r['births'][u] for u in r['births'] if 1 <= u <= 1000), 1),
                'other stores window mean': {t: round(window_mean(r['store'][t]), 1) for t in TASKS if t != q},
                'other stores outside their L0 band': [t for t in TASKS if t != q and not (
                    bands[t][0] <= window_mean(r['store'][t]) <= bands[t][1])],
                'programs credited with q at': {u: r['credited'][q][u] for u in (0, 10, 100, 500, 1000, 2000, 3000)
                                                if u in r['credited'][q]},
                'q store every 10 updates': [round(st[u], 1) for u in range(0, n + 1, 10)],
                'q executions per 10 updates': [round(sum(r['exe'][q].get(u, 0) for u in range(a + 1, a + 11)), 0)
                                                for a in range(0, n, 10)],
            }
            # re-evolution: first update after 100 from which q executions stay above 10% of L0's early rate for 50 updates
            thr = 0.1 * l0_exe_first100
            first = None
            for u in range(101, n - 49):
                if all(r['exe'][q].get(v, 0) > thr for v in range(u, u + 50)):
                    first = u
                    break
            row['q executions back above 10% of L0 rate for 50 updates, from update'] = first
            row['q store first above 5,000 at update'] = next((u for u in sorted(st) if st[u] >= 5000), None)
            P['arms']['%s seed %d' % (arm, seed)] = row
        # Lr against L0, same seed, over Lr's 1,000 updates
        lr_same = {}
        for seed in R.SEEDS[pop]:
            if ('Lr', seed) in runs and ('L0', seed) in runs:
                a, b = runs[('Lr', seed)], runs[('L0', seed)]
                lr_same[seed] = all(a['store'][t][u] == b['store'][t][u] for t in TASKS for u in a['store'][t]) and \
                    all(a['exe'][t][u] == b['exe'][t][u] for t in TASKS for u in a['exe'][t])
        P['Lr numbers identical to L0, same seed'] = lr_same
        # the criteria of the plan, section 6
        A = P['arms']
        seeds = R.SEEDS[pop]
        g = lambda arm, s: A.get('%s seed %d' % (arm, s))
        crit = {}
        crit['1 cut works'] = all(
            g('Lq', s) and mean(runs[('Lq', s)]['exe'][q][u] for u in range(1, 101)) < 0.05 * l0_exe_first100 and
            runs[('Lq', s)]['programs'][1000] >= 0.9 * l0_prog_1000 for s in seeds)
        crit['2 disappears'] = all(g('Lq', s) and g('Lq', s)['q store window mean'] >= 5000 and
                                   g('Lq', s)['q store window mean'] > bands[q][1] for s in seeds)
        crit['3 specific'] = all(g('Lq', s) and len(g('Lq', s)['other stores outside their L0 band']) <= 1 for s in seeds)
        crit['4 not generic damage'] = all(g('Ls', s) and g('Ls', s)['q store in L0 band'] for s in seeds)
        crit['5 handled alike'] = bool(lr_same) and all(lr_same.values()) and \
            json.load(open(os.path.join(R.PREP, 'seed%d' % pop, 'prepare_check.json')))['Lr file identical to L0 file']
        ret = []
        for s in seeds:
            a, b = g('Lq-then-restored', s), g('Lq-then-reloaded', s)
            if a and b:
                ret.append(a['q store window mean'] < 1000 and (b['q store window mean'] >= 5000 or
                                                                 b['q executions back above 10% of L0 rate for 50 updates, from update'] is not None))
            else:
                ret.append(None)
        crit['6 returns'] = all(x is True for x in ret) if ret and None not in ret else None
        crit['Lq q executions per update, updates 1-100, per seed'] = {
            s: round(mean(runs[('Lq', s)]['exe'][q][u] for u in range(1, 101)), 3) for s in seeds if ('Lq', s) in runs}
        crit['programs at 1,000: L0 mean, Lq per seed'] = [l0_prog_1000] + [runs[('Lq', s)]['programs'][1000] for s in seeds if ('Lq', s) in runs]
        P['criteria'] = crit
        out['populations']['seed %d' % pop] = P
    out['preparation'] = {('seed %d' % pop): R.read_cuts(pop)['summary'] for pop in R.POPS}
    for pop in R.POPS:
        p = os.path.join(R.PREP, 'seed%d' % pop, 'prepare_check.json')
        if os.path.exists(p):
            out['preparation']['seed %d' % pop]['prepare_check'] = json.load(open(p))
    for name in ['rig_check.json', 'restore_report.json']:
        p = os.path.join(R.PREP, name)
        if os.path.exists(p):
            out[name[:-5]] = json.load(open(p))
    json.dump(out, open(RESULTS, 'w'), indent=1)
    # print a compact view
    for k, P in out['populations'].items():
        print('==', k, 'q =', P['q'], 'L0 band', P['L0 band of each store'][P['q']])
        for arm, row in P['arms'].items():
            print('%-28s win %8.1f  at %s  exe %s  other-out %s  prog %s' % (
                arm, row['q store window mean'], {u: row['q store at'][u] for u in (0, 50, 100, 300, 1000, 2000, 3000) if u in row['q store at']},
                row['q executions per update, mean over bins'], row['other stores outside their L0 band'], row['programs at']))
        print(json.dumps(P['criteria']), P['Lr numbers identical to L0, same seed'])
    print('CPU seconds, all runs:', out['cpu_seconds_all_runs'])


if __name__ == '__main__':
    main()
