#!/usr/bin/env python3
"""s114_restart_audit_compare_the_pieces_with_the_continuous_runs.py

What it does, in plain words: reads the output of log S114's restart audit (the Avida runs made by
tools/s114_restart_audit_run_the_pieces_and_the_continuous_runs.py, kept in the scratch space) and compares, for each
Avida execution environment and seed, the run made in pieces of 1,000 updates (S113's procedure: the program population
saved and reloaded between pieces) with the same run made in one continuous Avida process. It computes the measures and
applies the thresholds written before running in "results/S114 Restart audit - how it will be tested, written before
running.md" (sections 2 and 3), and writes a compact summary to "results/S114 Restart audit - results.json".
It reads Avida's output files only; it runs nothing. Written 30 September 2026 by the one Opus 5.5 agent of log S114.
"""
import importlib.util, json, os, re, statistics, sys

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('s113', os.path.join(HERE, 's113_run_the_avida_execution_environments.py'))
s113 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(s113)

AUDIT = s113.SCRATCH + '/s114_restart_audit'
PIECES_OUT = AUDIT + '/runs/pieces'
CONT_OUT = AUDIT + '/runs/continuous'
CHECKS = AUDIT + '/checks'
OUT_JSON = os.path.join(os.path.dirname(HERE), 'results', 'S114 Restart audit - results.json')
ENVS = ['fixed_graded', 'common_pays_less']
SEEDS = [int(x) for x in os.environ.get('S114_SEEDS', '11401,11402,11403').split(',')]
PIECES = 10
TWO = s113.TWO
RANKS = s113.load_ranks()
TASKS = [t for t, _ in RANKS]
LATE = list(range(5000, 10001, 1000))          # piece-end samples used for T1 and T2
LOCAL250 = [1000 * k + 250 for k in range(1, PIECES)]   # first sample after each reload


def rows(path):
    out = {}
    for line in open(path):
        if line.startswith('#') or not line.strip():
            continue
        v = [float(x) for x in line.split()]
        out[int(v[0])] = v
    return out


def series_pieces(env, seed):
    """cumulative update -> dict of measures, for the run made in pieces."""
    run = os.path.join(PIECES_OUT, '%s_seed%d' % (env, seed))
    s, gen_sum, reloads = {}, 0.0, []
    for k in range(PIECES):
        d = os.path.join(run, 'piece_%02d' % k, 'data')
        t, c = rows(os.path.join(d, 'tasks.dat')), rows(os.path.join(d, 'count.dat'))
        a = rows(os.path.join(d, 'average.dat'))
        for u in t:
            s[1000 * k + u] = measures(t[u], c[u])
        gen_sum += a[1000][12]
        s[1000 * (k + 1)]['generation'] = gen_sum
        s[1000 * (k + 1)]['generation_this_piece'] = a[1000][12]
        if env == 'common_pays_less':
            r = rows(os.path.join(d, 'resource.dat'))[1000][1:]
            s[1000 * (k + 1)]['resources'] = r
            if k + 1 < PIECES:
                envtext = open(os.path.join(run, 'piece_%02d' % (k + 1), 'environment.cfg')).read()
                init = [float(x) for x in re.findall(r'initial=([0-9.eE+-]+)', envtext)]
                reloads.append({'update': 1000 * (k + 1), 'before': r, 'after_initial_written': init})
    return s, reloads


def series_continuous(env, seed):
    d = os.path.join(CONT_OUT, '%s_seed%d' % (env, seed), 'data')
    t, c, a = rows(os.path.join(d, 'tasks.dat')), rows(os.path.join(d, 'count.dat')), rows(os.path.join(d, 'average.dat'))
    s = {u: measures(t[u], c[u]) for u in t}
    for u in a:
        s[u]['generation'] = a[u][12]
    res = rows(os.path.join(d, 'resource.dat')) if env == 'common_pays_less' else {}
    return s, res


def measures(trow, crow):
    n = crow[2]
    shares = {task: (trow[i + 1] / n if n else 0.0) for i, task in enumerate(TASKS)}
    return {'programs': n, 'births': crow[8], 'insts': crow[1],
            'present': sum(1 for v in shares.values() if v > 0),
            'common': sum(1 for v in shares.values() if v >= 0.10),
            'prevalence': {t: 100.0 * shares[t] for t in TWO}}


def classify(diffs, thr):
    if all(d > 0 for d in diffs) or all(d < 0 for d in diffs):
        return 'COUNTS' if min(abs(d) for d in diffs) >= thr else 'same direction, below the threshold'
    return 'not separated by three seeds'


def mean(xs):
    return sum(xs) / len(xs)


def check_c1(env, seed, sp, sc):
    same = all(sp[u]['programs'] == sc[u]['programs'] and sp[u]['births'] == sc[u]['births']
               and sp[u]['prevalence'] == sc[u]['prevalence'] and sp[u]['insts'] == sc[u]['insts']
               for u in (250, 500, 750, 1000))
    return same


def check_c2():
    d = os.path.join(CHECKS, 'reload_resource_check')
    orig = os.path.join(PIECES_OUT, 'common_pays_less_seed11401')
    if not os.path.exists(os.path.join(d, 'data', 'tasks.dat')):
        return None
    same = all(open(os.path.join(d, 'data', f)).read().split('\n')[3:] ==
               open(os.path.join(orig, 'piece_05', 'data', f)).read().split('\n')[3:]
               for f in ['tasks.dat', 'count.dat'])
    r = rows(os.path.join(d, 'data', 'resource.dat'))
    init = [float(x) for x in re.findall(r'initial=([0-9.eE+-]+)',
                                         open(os.path.join(orig, 'piece_05', 'environment.cfg')).read())]
    before = rows(os.path.join(orig, 'piece_04', 'data', 'resource.dat'))[1000][1:]
    # For comparison (added after the plan, when the update-0 print turned out to come after one update of running):
    # how much a resource level changes in one update in the continuous run of the same seed, updates 5,000-6,000,
    # for the resources in use (level below 9,000), against the changes in the rerun's first 20 updates.
    cres = rows(os.path.join(CONT_OUT, 'common_pays_less_seed11401', 'data', 'resource.dat'))
    def steps(get, us):
        out = []
        for u in us:
            a, b = get(u), get(u + 1)
            out += [abs(y - x) / x for x, y in zip(a, b) if 0 < x < 9000]
        return sorted(out)
    cont = steps(lambda u: cres[u][1:], range(5000, 6000))
    rer = steps(lambda u: r[u][1:], range(0, 20))
    first = [abs(y - x) / x for x, y in zip(init, r[0][1:]) if 0 < x < 9000]
    q = lambda xs, p: xs[min(len(xs) - 1, int(p * len(xs)))]
    return {'rerun_repeats_original_counts_exactly': same, 'before_piece4_end': before, 'initial_written': init,
            'printed_update_0': r[0][1:], 'printed_update_1': r[1][1:], 'printed_update_2': r[2][1:],
            'printed_updates_0_to_20': {u: r[u][1:] for u in range(0, 21)},
            'max_relative_difference_update0_vs_initial': max(abs(a - b) / b for a, b in zip(r[0][1:], init) if b),
            'one_update_relative_change': {
                'continuous_5000_6000_median': q(cont, 0.5), 'continuous_5000_6000_p99': q(cont, 0.99),
                'continuous_5000_6000_max': cont[-1],
                'rerun_initial_to_update0_median': statistics.median(first), 'rerun_initial_to_update0_max': max(first),
                'rerun_updates_0_20_median': q(rer, 0.5), 'rerun_updates_0_20_p99': q(rer, 0.99)}}


def check_reload_of_continuous(env, seed):
    """The follow-up check (a departure, added after the first results): the continuous run's program population at
    update 5,000 loaded as S113 loads a piece, run 1,000 updates, against the continuous run's own updates 5,000-6,000."""
    d = os.path.join(CHECKS, 'reload_the_continuous_population', '%s_seed%d' % (env, seed), 'data')
    if not os.path.exists(os.path.join(d, 'count.dat')):
        return None
    c, a = rows(os.path.join(d, 'count.dat')), rows(os.path.join(d, 'average.dat'))
    cc = rows(os.path.join(CONT_OUT, '%s_seed%d' % (env, seed), 'data', 'count.dat'))
    ca = rows(os.path.join(CONT_OUT, '%s_seed%d' % (env, seed), 'data', 'average.dat'))
    b = lambda lo, hi: sum(c[u][8] for u in range(lo, hi)) / (hi - lo)
    cont_b = mean([cc[u][8] for u in (5250, 5500, 5750, 6000)])
    return {'births_per_update_after_reload': {'1-10': round(b(1, 10), 1), '10-50': round(b(10, 50), 1),
                                               '50-250': round(b(50, 250), 1), '250-1000': round(b(250, 1000), 1)},
            'births_continuous_samples_5250_6000_mean': cont_b,
            'births_250_1000_relative_to_continuous': round((b(250, 1000) - cont_b) / cont_b, 3),
            'gestation_time_at_1000': {'reloaded': round(a[1000][2], 1), 'continuous_6000': round(ca[6000][2], 1)},
            'generations_over_1000_updates': {'reloaded_piece_measure': round(a[1000][12], 1),
                                              'continuous_increase_5000_6000': round(ca[6000][12] - ca[5000][12], 1)}}


def main():
    out = {'plan': 'results/S114 Restart audit - how it will be tested, written before running.md', 'seeds': SEEDS,
           'environments': {}}
    for env in ENVS:
        E = {'per_seed': {}, 'tests': {}}
        diffs = {'T1_mean': [], 'T1_at_10000': [], 'T3': [], 'T5_common': [], 'T5_births_rel': [],
                 'T2': {t: [] for t in TWO}, 'T5_prev': {t: [] for t in TWO}}
        t4 = []
        for seed in SEEDS:
            sp, reloads = series_pieces(env, seed)
            sc, cres = series_continuous(env, seed)
            ps = {'C1_first_1000_identical': check_c1(env, seed, sp, sc)}
            ups = sorted(u for u in sc if u % 250 == 0 and u > 0)
            ps['series'] = {str(u): {'pieces': {k: sp[u][k] for k in ('present', 'common', 'programs', 'births')},
                                     'continuous': {k: sc[u][k] for k in ('present', 'common', 'programs', 'births')}}
                            for u in ups}
            for u in range(1000, 10001, 1000):
                ps['series'][str(u)]['pieces']['generation'] = round(sp[u]['generation'], 2)
                ps['series'][str(u)]['continuous']['generation'] = round(sc[u]['generation'], 2)
                ps['series'][str(u)]['pieces']['prevalence'] = {t: round(v, 1) for t, v in sp[u]['prevalence'].items()}
                ps['series'][str(u)]['continuous']['prevalence'] = {t: round(v, 1) for t, v in sc[u]['prevalence'].items()}
            d1 = mean([sp[u]['common'] for u in LATE]) - mean([sc[u]['common'] for u in LATE])
            diffs['T1_mean'].append(d1)
            diffs['T1_at_10000'].append(sp[10000]['common'] - sc[10000]['common'])
            for t in TWO:
                diffs['T2'][t].append(mean([sp[u]['prevalence'][t] for u in LATE]) -
                                      mean([sc[u]['prevalence'][t] for u in LATE]))
                diffs['T5_prev'][t].append(mean([sp[u]['prevalence'][t] for u in LOCAL250]) -
                                           mean([sc[u]['prevalence'][t] for u in LOCAL250]))
            g_p, g_c = sp[10000]['generation'], sc[10000]['generation']
            diffs['T3'].append((g_p - g_c) / g_c)
            diffs['T5_common'].append(mean([sp[u]['common'] for u in LOCAL250]) - mean([sc[u]['common'] for u in LOCAL250]))
            b_p, b_c = mean([sp[u]['births'] for u in LOCAL250]), mean([sc[u]['births'] for u in LOCAL250])
            diffs['T5_births_rel'].append((b_p - b_c) / b_c)
            ps['generation_at_10000'] = {'pieces_sum_of_piece_ends': round(g_p, 1), 'continuous': round(g_c, 1),
                                         'pieces_as_printed_at_10000': round(sp[10000]['generation_this_piece'], 1)}
            ps['births_mean_at_local_250'] = {'pieces': round(b_p, 1), 'continuous': round(b_c, 1)}
            ps['births_mean_at_piece_ends_5000_10000'] = {
                'pieces': round(mean([sp[u]['births'] for u in LATE]), 1),
                'continuous': round(mean([sc[u]['births'] for u in LATE]), 1)}
            if env == 'common_pays_less':
                rl = []
                for r in reloads:
                    rel = [abs(a - b) / b if b else 0.0 for a, b in zip(r['after_initial_written'], r['before'])]
                    t4.append(max(rel))
                    u = r['update']
                    rl.append({'update': u, 'before': r['before'], 'after_initial_written': r['after_initial_written'],
                               'max_relative_change': max(rel),
                               'continuous_at_same_update': cres[u][1:], 'continuous_next_update': cres[u + 1][1:]})
                ps['reloads'] = rl
            E['per_seed'][str(seed)] = ps
        E['tests']['T1 common capabilities, mean of 5,000-10,000'] = {
            'differences_pieces_minus_continuous': [round(x, 2) for x in diffs['T1_mean']],
            'verdict': classify(diffs['T1_mean'], 1)}
        E['tests']['T1 common capabilities at 10,000'] = {
            'differences_pieces_minus_continuous': diffs['T1_at_10000'], 'verdict': classify(diffs['T1_at_10000'], 1)}
        E['tests']['T2 prevalence points, mean of 5,000-10,000'] = {
            t: {'differences': [round(x, 1) for x in diffs['T2'][t]], 'verdict': classify(diffs['T2'][t], 5)} for t in TWO}
        E['tests']['T3 generations at 10,000 (relative)'] = {
            'differences': [round(x, 3) for x in diffs['T3']], 'verdict': classify(diffs['T3'], 0.10)}
        if env == 'common_pays_less':
            E['tests']['T4 resources reset at a reload'] = {
                'largest_relative_change_at_any_reload': max(t4),
                'verdict': 'COUNTS' if max(t4) > 0.01 else 'no reset (largest change %.2g of the level)' % max(t4)}
        E['tests']['T5 just after a reload (local update 250)'] = {
            'common': {'differences': [round(x, 2) for x in diffs['T5_common']], 'verdict': classify(diffs['T5_common'], 1)},
            'births_relative': {'differences': [round(x, 3) for x in diffs['T5_births_rel']],
                                'verdict': classify(diffs['T5_births_rel'], 0.10)},
            'prevalence': {t: {'differences': [round(x, 1) for x in diffs['T5_prev'][t]],
                               'verdict': classify(diffs['T5_prev'][t], 5)} for t in TWO}}
        out['environments'][env] = E
    out['C2_reload_resource_check'] = check_c2()
    out['follow_up_reload_of_the_continuous_population_at_5000'] = {
        env: {str(s): check_reload_of_continuous(env, s) for s in SEEDS} for env in ENVS}
    for env in ENVS:
        E = out['environments'][env]
        E['births_mean_at_piece_ends_5000_10000_relative'] = [
            round((E['per_seed'][str(s)]['births_mean_at_piece_ends_5000_10000']['pieces'] -
                   E['per_seed'][str(s)]['births_mean_at_piece_ends_5000_10000']['continuous']) /
                  E['per_seed'][str(s)]['births_mean_at_piece_ends_5000_10000']['continuous'], 3) for s in SEEDS]
    json.dump(out, open(OUT_JSON, 'w'), indent=1)
    for env in ENVS:
        print('==', env)
        for k, v in out['environments'][env]['tests'].items():
            print(k, json.dumps(v)[:600])
        for seed in SEEDS:
            ps = out['environments'][env]['per_seed'][str(seed)]
            print(seed, 'C1', ps['C1_first_1000_identical'], 'gen', ps['generation_at_10000'],
                  'births250', ps['births_mean_at_local_250'], 'birthsLate', ps['births_mean_at_piece_ends_5000_10000'])
    print('C2', json.dumps(out['C2_reload_resource_check'])[:900])


if __name__ == '__main__':
    main()
