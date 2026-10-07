#!/usr/bin/env python3
"""s113_count_new_capabilities_over_time.py

What it does, in plain words: for log S113, reads what Avida wrote every 250 updates in each run (how many Avida
programs performed each of the 77 logic tasks, and how many programs there were) and counts, over time, how many
distinct computational capabilities (tasks) were present in the program population: performed by at least one program
("by any program") and by at least 10% of the programs ("common"). For every task it finds when it first appeared;
whether tasks once common were kept to the end; whether the count kept rising or levelled off (no new highest count
of common tasks after update 40,000); and the spread over the three seeds of each Avida execution environment. It then
makes the comparisons the plan named (results/S113 Which execution environments learn - how it will be tested, written
before running.md, section 6), by the plan's rule: "more" only if every seed of one environment is above every seed
of the other. It also compares the FIXED GRADED runs with S111's three unbroken runs, and reads the growing list's
steps. If the reuse file of tools/s113_measure_reuse_of_task_circuits.py exists, its summary is added. If the summary of
tools/s113_measure_capabilities_in_the_saved_program_populations.py exists (a second reading, added after the runs:
the saved program populations every 5,000 updates, each distinct instruction sequence run in Avida's test processor),
the same measures and comparisons are also made on it and added as "test processor reading".

It reads only the scratch space and the S113 ranking file, and writes one JSON file (the path given as the first
argument; default: the S113 results .json). It runs nothing in Avida.
Written 30 September 2026 by the one Opus 5.5 agent of log S113.
"""
import json, os, statistics, sys

SCRATCH = '/tmp/claude-0/-home-user-ThreadSmith/8d9323da-c0ec-57ec-91fd-8f99ca99320a/scratchpad'
RUNS = SCRATCH + '/s113/runs'
S111 = SCRATCH + '/s111/runs'
HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(os.path.dirname(HERE), 'results')
RANKS = os.path.join(RESULTS, 'S113 Which execution environments learn - the runs',
                     'the 77 tasks ranked by the fewest nand steps.json')
REUSE = SCRATCH + '/s113/reuse/reuse_summary.json'
TPSUM = SCRATCH + '/s113/test_processor/summary.json'
DEFAULT_OUT = os.path.join(RESULTS, 'S113 Which execution environments learn - results.json')

ENVS = ['fixed_graded', 'equ_only', 'no_rewards', 'growing', 'common_pays_less', 'fixed_large']
LABEL = {'fixed_graded': 'FIXED LIST, GRADED', 'equ_only': 'ONE HARD TASK ONLY', 'no_rewards': 'NO TASK REWARDS',
         'growing': 'GROWING LIST', 'common_pays_less': 'COMMON TASKS PAY LESS', 'fixed_large': 'FIXED LARGE LIST'}
SEEDS = [1, 2, 3]
COMMON = 0.10
LEVEL_OFF_BY = 40000
TWO = ['not', 'nand', 'and', 'orn', 'or', 'andn', 'nor', 'xor', 'equ']
MARKS = list(range(5000, 50001, 5000))


def dat(path):
    rows = []
    for line in open(path):
        if line.startswith('#') or not line.strip():
            continue
        rows.append([float(x) for x in line.split()])
    return rows


def read_run(env, seed, tasks):
    d = os.path.join(RUNS, '%s_seed%d' % (env, seed))
    state = json.load(open(os.path.join(d, 'state.json')))
    samples = []          # (update, programs, [count per task])
    for k in range(state['done']):
        p = os.path.join(d, 'piece_%02d' % k, 'data')
        t = dat(os.path.join(p, 'tasks.dat'))
        c = dat(os.path.join(p, 'count.dat'))
        assert len(t) == len(c) == 4, (env, seed, k)
        for tr, cr in zip(t, c):
            assert tr[0] == cr[0] and len(tr) == len(tasks) + 1
            samples.append((k * 1000 + int(tr[0]), int(cr[2]), [int(x) for x in tr[1:]]))
    return state, samples


def measure(samples, tasks, levels):
    n = len(tasks)
    any_count, common_count, any2, any3, com2, com3 = [], [], [], [], [], []
    first_any, first_common = [None] * n, [None] * n
    ever_common = [False] * n
    drops = 0
    was_common = [False] * n
    for upd, progs, counts in samples:
        present = [c > 0 for c in counts]
        common = [progs > 0 and c / progs >= COMMON for c in counts]
        for i in range(n):
            if present[i] and first_any[i] is None:
                first_any[i] = upd
            if common[i] and first_common[i] is None:
                first_common[i] = upd
            if common[i]:
                ever_common[i] = True
            if was_common[i] and not present[i]:
                drops += 1
            if common[i]:
                was_common[i] = True
            elif not present[i]:
                was_common[i] = False
        any_count.append(sum(present))
        common_count.append(sum(common))
        any2.append(sum(present[i] for i in range(n) if tasks[i] in TWO))
        any3.append(sum(present[i] for i in range(n) if tasks[i] not in TWO))
        com2.append(sum(common[i] for i in range(n) if tasks[i] in TWO))
        com3.append(sum(common[i] for i in range(n) if tasks[i] not in TWO))
    upd = [s[0] for s in samples]
    last_new_high, high = 0, -1
    for u, c in zip(upd, common_count):
        if c > high:
            high, last_new_high = c, u
    end_counts, end_progs = samples[-1][2], samples[-1][1]
    end_common = [end_progs > 0 and c / end_progs >= COMMON for c in end_counts]
    end_present = [c > 0 for c in end_counts]
    kept = sum(1 for i in range(n) if ever_common[i] and end_common[i])
    lost = sum(1 for i in range(n) if ever_common[i] and not end_present[i])

    def at(series, u):
        i = upd.index(u) if u in upd else None
        return series[i] if i is not None else None
    ten_before = at(common_count, upd[-1] - 10000) if upd[-1] >= 10000 else None
    return {
        'updates_reached': upd[-1],
        'programs_at_end': end_progs,
        'any_at_end': any_count[-1], 'common_at_end': common_count[-1],
        'any_two_input_at_end': any2[-1], 'any_three_input_at_end': any3[-1],
        'common_two_input_at_end': com2[-1], 'common_three_input_at_end': com3[-1],
        'highest_common': max(common_count), 'highest_any': max(any_count),
        'last_new_high_of_common': last_new_high,
        'levelled_off': last_new_high <= LEVEL_OFF_BY,
        'rise_of_common_over_last_10000': (common_count[-1] - ten_before) if ten_before is not None else None,
        'ever_common': sum(ever_common), 'kept_common_at_end': kept, 'ever_common_performed_by_none_at_end': lost,
        'times_a_common_task_fell_to_none': drops,
        'common_at_marks': {str(u): at(common_count, u) for u in MARKS},
        'any_at_marks': {str(u): at(any_count, u) for u in MARKS},
        'first_any': {tasks[i]: first_any[i] for i in range(n) if first_any[i] is not None},
        'first_common': {tasks[i]: first_common[i] for i in range(n) if first_common[i] is not None},
        'share_at_end': {tasks[i]: round(end_counts[i] / end_progs, 4) for i in range(n)
                         if end_progs and end_counts[i]},
        'series': {'update': upd[3::4], 'any': any_count[3::4], 'common': common_count[3::4]},
    }


def spread(vals):
    v = [x for x in vals if x is not None]
    if not v:
        return None
    return {'smallest': min(v), 'middle': statistics.median(v), 'largest': max(v), 'per_seed': vals}


def compare(a, b):
    """The plan's rule: 'more' if every seed of a is above every seed of b; 'fewer' the reverse."""
    a = [x for x in a if x is not None]
    b = [x for x in b if x is not None]
    if not a or not b:
        return 'not measured'
    if min(a) > max(b):
        return 'more'
    if max(a) < min(b):
        return 'fewer'
    return 'not separated by three seeds'


def undercount_check(env, seed, tasks):
    """Loaded programs have an empty task record until they finish one copy: compare, for pieces 1 on, the number of
    task performances counted at the piece's update 250 with those at the previous piece's update 1000."""
    d = os.path.join(RUNS, '%s_seed%d' % (env, seed))
    ratios = []
    state = json.load(open(os.path.join(d, 'state.json')))
    for k in range(1, state['done']):
        a = dat(os.path.join(d, 'piece_%02d' % (k - 1), 'data', 'tasks.dat'))[-1]
        b = dat(os.path.join(d, 'piece_%02d' % k, 'data', 'tasks.dat'))[0]
        sa, sb = sum(a[1:]), sum(b[1:])
        if sa > 0:
            ratios.append(sb / sa)
    return ratios


def s111_check():
    out = {}
    for s in SEEDS:
        rows = dat(os.path.join(S111, 'main_default_seed%d' % s, 'data', 'tasks.dat'))
        cnt = dat(os.path.join(S111, 'main_default_seed%d' % s, 'data', 'count.dat'))
        progs = {int(r[0]): int(r[2]) for r in cnt}
        first_any_equ = next((int(r[0]) for r in rows if r[9] > 0), None)
        first_com_equ = next((int(r[0]) for r in rows if progs.get(int(r[0])) and r[9] / progs[int(r[0])] >= COMMON),
                             None)
        last = rows[-1]
        common_end = sum(1 for x in last[1:] if x / progs[int(last[0])] >= COMMON)
        out['seed%d' % s] = {'equ_first_any': first_any_equ, 'equ_first_common': first_com_equ,
                             'nine_common_at_50000': common_end, 'nine_any_at_50000': sum(1 for x in last[1:] if x > 0)}
    return out


def by_environment(per, tasks, levels, marks):
    by_env = {}
    for env in ENVS:
        runs = [per.get('%s_seed%d' % (env, s)) for s in SEEDS]
        if not any(runs):
            continue

        def col(f):
            return [r[f] if r else None for r in runs]
        e = {'label': LABEL[env]}
        for f in ['common_at_end', 'any_at_end', 'common_two_input_at_end', 'common_three_input_at_end',
                  'any_two_input_at_end', 'any_three_input_at_end', 'last_new_high_of_common',
                  'rise_of_common_over_last_10000', 'ever_common', 'kept_common_at_end',
                  'ever_common_performed_by_none_at_end']:
            e[f] = spread(col(f))
        for f in ['highest_common', 'times_a_common_task_fell_to_none', 'updates_reached', 'programs_at_end']:
            if runs[0] and f in runs[0]:
                e[f] = spread(col(f))
        e['levelled_off_per_seed'] = col('levelled_off')
        e['common_at_marks'] = {u: spread([r['common_at_marks'][u] if r else None for r in runs]) for u in map(str, marks)}
        e['any_at_marks'] = {u: spread([r['any_at_marks'][u] if r else None for r in runs]) for u in map(str, marks)}
        firsts = {}
        for t in tasks:
            fa = [r['first_any'].get(t) if r else None for r in runs]
            fc = [r['first_common'].get(t) if r else None for r in runs]
            if any(x is not None for x in fa):
                firsts[t] = {'level': levels[t], 'first_any_per_seed': fa, 'first_common_per_seed': fc}
        e['first_appearance'] = firsts
        by_env[env] = e
    return by_env


def comparisons(per, by_env):
    def endv(env, f='common_at_end'):
        return [per['%s_seed%d' % (env, s)][f] if '%s_seed%d' % (env, s) in per else None for s in SEEDS]

    def equ_common(env):
        return [per['%s_seed%d' % (env, s)]['first_common'].get('equ') if '%s_seed%d' % (env, s) in per else None
                for s in SEEDS]

    comp = {}
    if 'equ_only' in by_env and 'fixed_graded' in by_env:
        eo, fg = equ_common('equ_only'), equ_common('fixed_graded')
        n_eo, n_fg = sum(x is not None for x in eo), sum(x is not None for x in fg)
        med = lambda v: statistics.median([x for x in v if x is not None]) if any(x is not None for x in v) else None
        comp['E1 one hard task against graded'] = {
            'EQU first common, ONE HARD TASK ONLY, per seed': eo, 'EQU first common, FIXED GRADED, per seed': fg,
            'seeds with EQU common': [n_eo, n_fg],
            'middle first-common update': [med(eo), med(fg)],
            'against the expectation': bool(n_eo >= n_fg and (med(eo) is not None and med(fg) is not None
                                                              and med(eo) <= med(fg)))}
    if 'no_rewards' in by_env:
        nr = endv('no_rewards')
        others = {env: compare(nr, endv(env)) for env in ENVS if env != 'no_rewards' and env in by_env}
        comp['E2 no rewards'] = {'common at 50,000 per seed': nr, 'against the others': others,
                                 'against the expectation': bool(any(x is not None and x >= 3 for x in nr)
                                                                 or others.get('fixed_graded') != 'fewer')}
    if 'growing' in by_env and 'fixed_graded' in by_env:
        r = compare(endv('growing'), endv('fixed_graded'))
        comp['E3 growing against fixed graded'] = {'result': r, 'against the expectation': r != 'more'}
    if 'growing' in by_env and 'fixed_large' in by_env:
        r = compare(endv('growing'), endv('fixed_large'))
        comp['E4 growing against fixed large'] = {
            'common at 50,000': [endv('growing'), endv('fixed_large')],
            'any at 50,000': [endv('growing', 'any_at_end'), endv('fixed_large', 'any_at_end')],
            'result (common)': r, 'result (any)': compare(endv('growing', 'any_at_end'), endv('fixed_large', 'any_at_end')),
            "against the proposition 'a growing list learns more than a fixed list'": r != 'more',
            "against Claude's expectation 'not separated'": r != 'not separated by three seeds'}
    lo = {env: by_env[env]['levelled_off_per_seed'] for env in by_env}
    comp['E5 levelling off'] = {
        'levelled off per seed (last new high of common at or before 40,000)': lo,
        'against the expectation': bool(
            any(x is False for env in ('fixed_graded', 'equ_only') for x in lo.get(env, []))
            or any(sum(1 for x in lo.get(env, []) if x is False) < 2 for env in ('growing', 'fixed_large')))}
    if 'common_pays_less' in by_env and 'fixed_graded' in by_env:
        r = compare(endv('common_pays_less'), endv('fixed_graded'))
        comp['E6 common tasks pay less against fixed graded'] = {
            'common at 50,000': [endv('common_pays_less'), endv('fixed_graded')],
            'two-input tasks present by any program at 50,000': [endv('common_pays_less', 'any_two_input_at_end'),
                                                                 endv('fixed_graded', 'any_two_input_at_end')],
            'result (common)': r, 'against the expectation': r == 'fewer'}
    keep = {}
    for env in by_env:
        vals = []
        for s in SEEDS:
            k = '%s_seed%d' % (env, s)
            if k in per and per[k]['ever_common']:
                vals.append(per[k]['kept_common_at_end'] / per[k]['ever_common'])
        keep[env] = [round(v, 3) for v in vals]
    comp['E7 keeping'] = {'share of ever-common tasks common at 50,000, per seed': keep,
                          'against the expectation': any(statistics.median(v) < 0.9 for env, v in keep.items()
                                                         if v and env != 'no_rewards')}
    return comp


def main():
    ranks = json.load(open(RANKS))['tasks']
    tasks = [r['task'] for r in ranks]
    levels = {r['task']: r['fewest_nand_steps'] for r in ranks}
    per = {}
    growing_steps = {}
    under = []
    for env in ENVS:
        for seed in SEEDS:
            key = '%s_seed%d' % (env, seed)
            if not os.path.exists(os.path.join(RUNS, key, 'state.json')):
                continue
            state, samples = read_run(env, seed, tasks)
            if not samples:
                continue
            per[key] = measure(samples, tasks, levels)
            per[key]['pieces_done'] = state['done']
            per[key]['seconds'] = sum(h['seconds'] for h in state['history'])
            if env == 'growing':
                steps = []
                for h in state['history']:
                    if h.get('unlocked_after_piece', 0) > h['unlocked_during_piece']:
                        steps.append({'level_added': h['unlocked_after_piece'], 'rewarded_from_update': h['update_end']})
                growing_steps[key] = steps
                per[key]['highest_level_rewarded_at_end'] = state['unlocked']
            under += undercount_check(env, seed, tasks)
    by_env = by_environment(per, tasks, levels, MARKS)
    comp = comparisons(per, by_env)
    out = {'what': 'log S113: computational capabilities in the program population over time, per Avida execution '
                   'environment (written by tools/s113_count_new_capabilities_over_time.py)',
           'common share': COMMON, 'levelled off if the last new high is at or before': LEVEL_OFF_BY,
           'environments': by_env, 'comparisons': comp, 'growing list steps': growing_steps,
           'check: S111 unbroken runs (nine tasks)': s111_check(),
           'check: performances counted 250 updates after a load, against the previous piece end': {
               'pieces': len(under), 'smallest': min(under) if under else None,
               'middle': statistics.median(under) if under else None, 'largest': max(under) if under else None},
           'per run': per}
    if os.path.exists(REUSE):
        out['reuse (M6)'] = json.load(open(REUSE))
    if os.path.exists(TPSUM):
        tp = json.load(open(TPSUM))
        per_tp = {}
        for k, v in tp['per run'].items():
            r = dict(v['performing'])
            r['performing_and_replicating'] = {f: v['performing_and_replicating'][f] for f in
                                               ['common_at_end', 'any_at_end', 'common_at_marks', 'any_at_marks',
                                                'last_new_high_of_common', 'ever_common', 'kept_common_at_end']}
            r['replicating_share_at_marks'] = v['replicating_share_at_marks']
            r['programs_at_marks'] = v['programs_at_marks']
            r['distinct_sequences_at_marks'] = v['distinct_sequences_at_marks']
            per_tp[k] = r
        be = by_environment(per_tp, tasks, levels, MARKS)
        out['test processor reading'] = {
            'what': 'the second reading, added after the runs (a departure from the plan): the program populations '
                    'saved every 5,000 updates, each distinct instruction sequence run alone in Avida\'s test processor '
                    '(tools/s113_measure_capabilities_in_the_saved_program_populations.py); "levelled off" and the '
                    'rise are read at 5,000-update steps',
            'environments': be, 'comparisons': comparisons(per_tp, be), 'per run': per_tp}
        # the two readings side by side at the ten saved updates: common and present, world count / test processor
        side = {}
        for k in per:
            if k in per_tp:
                side[k] = {u: [per[k]['common_at_marks'][u], per_tp[k]['common_at_marks'][u],
                               per[k]['any_at_marks'][u], per_tp[k]['any_at_marks'][u]] for u in map(str, MARKS)}
        out['check: world count against test processor count at the saved updates'] = {
            'columns': ['common, world count', 'common, test processor', 'present, world count',
                        'present, test processor'], 'per run': side}
    by_env_under = {}
    for env in ENVS:
        r = []
        for seed in SEEDS:
            if os.path.exists(os.path.join(RUNS, '%s_seed%d' % (env, seed), 'state.json')):
                r += undercount_check(env, seed, tasks)
        if r:
            by_env_under[env] = {'pieces': len(r), 'smallest': round(min(r), 3), 'middle': round(statistics.median(r), 3),
                                 'largest': round(max(r), 3), 'pieces under 0.5': sum(1 for x in r if x < 0.5)}
    out['check: performances counted 250 updates after a load, by environment'] = by_env_under
    # growing list: for each task that became common, was its level already rewarded when it first became common?
    before = {}
    for k, steps in growing_steps.items():
        rewarded_from = {1: 0}
        for st in steps:
            rewarded_from[st['level_added']] = st['rewarded_from_update']
        fc = per[k]['first_common']
        early = sorted(t for t, u in fc.items() if levels[t] not in rewarded_from or u < rewarded_from[levels[t]])
        never_rewarded_common = sorted(t for t in fc if levels[t] not in rewarded_from)
        before[k] = {'tasks ever common': len(fc), 'common before their level was rewarded': len(early),
                     'of which never rewarded in the run': len(never_rewarded_common), 'tasks': early}
    out['growing list: tasks common before their level was rewarded (world count)'] = before
    path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_OUT
    json.dump(out, open(path, 'w'), indent=1)
    for env in by_env:
        e = by_env[env]
        print('%-22s common@end %s any@end %s lastnewhigh %s levelled %s' % (
            env, e['common_at_end']['per_seed'], e['any_at_end']['per_seed'],
            e['last_new_high_of_common']['per_seed'], e['levelled_off_per_seed']))
    print(json.dumps(comp, indent=1))


if __name__ == '__main__':
    main()
