#!/usr/bin/env python3
"""s113_print_the_results_tables.py

What it does, in plain words: prints, as Markdown tables, the numbers of log S113's results file
(results/S113 Which execution environments learn - results.json, written by tools/s113_count_new_capabilities_over_time.py),
so that the tables in the results .md are copied from the .json and not typed by hand: per Avida execution environment
and seed, the number of computational capabilities (logic tasks) present by any program and common (at least 10% of the
program population) every 5,000 updates; at update 50,000; the last new high and levelling off; keeping; the first
appearance of each two-input task; the growing list's steps; the checks; the reuse measure if present. It reads the
.json only and writes nothing.
Written 30 September 2026 by the one Opus 5.5 agent of log S113.
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(os.path.dirname(HERE), 'results', 'S113 Which execution environments learn - results.json')
ENVS = ['fixed_graded', 'equ_only', 'no_rewards', 'growing', 'common_pays_less', 'fixed_large']
TWO = ['not', 'nand', 'and', 'orn', 'or', 'andn', 'nor', 'xor', 'equ']


def fmt(x):
    if isinstance(x, bool):
        return 'yes' if x else 'no'
    return '-' if x is None else str(x)


def main():
    d = json.load(open(sys.argv[1] if len(sys.argv) > 1 else PATH))
    per, envs = d['per run'], d['environments']
    marks = [str(u) for u in range(5000, 50001, 5000)]
    for what in ['common', 'any']:
        print('\n### %s, per seed (seeds 1 / 2 / 3), every 5,000 updates\n' % (
            'Common (performed by at least 10% of the programs)' if what == 'common' else 'Present (performed by at least one program)'))
        print('| environment | ' + ' | '.join('%dk' % (int(u) // 1000) for u in marks) + ' |')
        print('|---|' + '---|' * len(marks))
        for env in ENVS:
            if env not in envs:
                continue
            cells = []
            for u in marks:
                cells.append(' / '.join(fmt(per.get('%s_seed%d' % (env, s), {}).get('%s_at_marks' % what, {}).get(u))
                                        for s in (1, 2, 3)))
            print('| %s | %s |' % (envs[env]['label'], ' | '.join(cells)))
    print('\n### At update 50,000, and levelling off\n')
    print('| environment | common (1/2/3) | two-input common | three-input common | present (1/2/3) | two-input present | '
          'three-input present | last new high of common | levelled off | rise of common over last 10,000 |')
    print('|---|---|---|---|---|---|---|---|---|---|')
    for env in ENVS:
        if env not in envs:
            continue
        rs = [per.get('%s_seed%d' % (env, s)) for s in (1, 2, 3)]

        def col(f):
            return ' / '.join(fmt(r[f]) if r else '-' for r in rs)
        print('| %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |' % (
            envs[env]['label'], col('common_at_end'), col('common_two_input_at_end'), col('common_three_input_at_end'),
            col('any_at_end'), col('any_two_input_at_end'), col('any_three_input_at_end'),
            col('last_new_high_of_common'), col('levelled_off'), col('rise_of_common_over_last_10000')))
    print('\n### Keeping\n')
    print('| environment | ever common (1/2/3) | common at 50,000 of those | performed by none at 50,000 | times a common task fell to none | highest common count |')
    print('|---|---|---|---|---|---|')
    for env in ENVS:
        if env not in envs:
            continue
        rs = [per.get('%s_seed%d' % (env, s)) for s in (1, 2, 3)]

        def col(f):
            return ' / '.join(fmt(r[f]) if r else '-' for r in rs)
        print('| %s | %s | %s | %s | %s | %s |' % (envs[env]['label'], col('ever_common'), col('kept_common_at_end'),
                                                   col('ever_common_performed_by_none_at_end'),
                                                   col('times_a_common_task_fell_to_none'), col('highest_common')))
    print('\n### First update at which each two-input task was common (seeds 1 / 2 / 3; "-" never)\n')
    print('| environment | ' + ' | '.join(t.upper() for t in TWO) + ' |')
    print('|---|' + '---|' * len(TWO))
    for env in ENVS:
        if env not in envs:
            continue
        cells = []
        for t in TWO:
            cells.append(' / '.join(fmt(per.get('%s_seed%d' % (env, s), {}).get('first_common', {}).get(t)) for s in (1, 2, 3)))
        print('| %s | %s |' % (envs[env]['label'], ' | '.join(cells)))
    print('\n### First update at which each two-input task was performed by any program\n')
    print('| environment | ' + ' | '.join(t.upper() for t in TWO) + ' |')
    print('|---|' + '---|' * len(TWO))
    for env in ENVS:
        if env not in envs:
            continue
        cells = []
        for t in TWO:
            cells.append(' / '.join(fmt(per.get('%s_seed%d' % (env, s), {}).get('first_any', {}).get(t)) for s in (1, 2, 3)))
        print('| %s | %s |' % (envs[env]['label'], ' | '.join(cells)))
    ranks = {}
    for env in ENVS:
        for t, f in envs.get(env, {}).get('first_appearance', {}).items():
            ranks[t] = f['level']
    print('\n### Tasks ever common, by level (seeds 1 / 2 / 3), and the earliest update any task of the level was common\n')
    levels = sorted(set(ranks.values()))
    print('| environment | ' + ' | '.join('level %d' % l for l in levels) + ' |')
    print('|---|' + '---|' * len(levels))
    for env in ENVS:
        if env not in envs:
            continue
        cells = []
        for l in levels:
            parts = []
            for s in (1, 2, 3):
                fc = per.get('%s_seed%d' % (env, s), {}).get('first_common', {})
                ts = [t for t in fc if ranks.get(t) == l]
                parts.append('%d (%s)' % (len(ts), min(fc[t] for t in ts)) if ts else '0')
            cells.append(' / '.join(parts))
        print('| %s | %s |' % (envs[env]['label'], ' | '.join(cells)))
    print('\n### Growing list: update from which each level was rewarded\n')
    for k, steps in d['growing list steps'].items():
        print('- %s: %s; highest level rewarded at the end: %s' % (
            k, ', '.join('level %d from %d' % (s['level_added'], s['rewarded_from_update']) for s in steps),
            per[k].get('highest_level_rewarded_at_end')))
    print('\n### Checks\n')
    print('- S111 unbroken runs:', json.dumps(d['check: S111 unbroken runs (nine tasks)']))
    print('- performances counted 250 updates after a load:',
          json.dumps(d['check: performances counted 250 updates after a load, against the previous piece end']))
    print('- programs at end:', {k: v['programs_at_end'] for k, v in per.items()})
    print('- seconds per run:', {k: v['seconds'] for k, v in per.items()})
    if 'reuse (M6)' in d:
        print('\n### Reuse\n')
        print('| run | programs with this sequence | length | replicates | required for replication | tasks performed | '
              'pairs | mean shared | mean expected | pairs above | pairs below | pairs sharing nothing |')
        print('|---|---|---|---|---|---|---|---|---|---|---|---|')
        for r in d['reuse (M6)']['runs']:
            print('| %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |' % (
                r['run'], r['programs_with_this_sequence'], r['length'], fmt(r['replicates']), r['required_for_replication'],
                r['tasks_performed'], r['pairs'], fmt(r['mean_shared']), fmt(r['mean_expected']),
                r['pairs_above_expected'], r['pairs_below_expected'], r['pairs_sharing_nothing']))
        print('\n', json.dumps(d['reuse (M6)']['all runs']))
    if 'test processor reading' in d:
        tp = d['test processor reading']
        print('\n## Test processor reading\n')
        for what in ['common', 'any']:
            print('\n### %s, test processor, per seed, every 5,000 updates\n' % what)
            print('| environment | ' + ' | '.join('%dk' % (int(u) // 1000) for u in marks) + ' |')
            print('|---|' + '---|' * len(marks))
            for env in ENVS:
                if env not in tp['environments']:
                    continue
                cells = [' / '.join(fmt(tp['per run'].get('%s_seed%d' % (env, s), {}).get('%s_at_marks' % what, {}).get(u))
                                    for s in (1, 2, 3)) for u in marks]
                print('| %s | %s |' % (tp['environments'][env]['label'], ' | '.join(cells)))
        print('\n### At update 50,000, test processor\n')
        print('| environment | common at 50,000 | two-input | three-input | present at 50,000 | common and replicating | '
              'last new high | levelled off | ever common | kept common |')
        print('|---|---|---|---|---|---|---|---|---|---|')
        for env in ENVS:
            if env not in tp['environments']:
                continue
            rs = [tp['per run'].get('%s_seed%d' % (env, s)) for s in (1, 2, 3)]

            def col(f):
                return ' / '.join(fmt(r[f]) if r else '-' for r in rs)
            print('| %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |' % (
                tp['environments'][env]['label'], col('common_at_end'), col('common_two_input_at_end'),
                col('common_three_input_at_end'), col('any_at_end'),
                ' / '.join(fmt(r['performing_and_replicating']['common_at_end']) for r in rs),
                col('last_new_high_of_common'), col('levelled_off'), col('ever_common'), col('kept_common_at_end')))
        print('\n### Comparisons, test processor reading\n')
        print(json.dumps(tp['comparisons'], indent=1))
        print('\n### World count against test processor\n')
        print(json.dumps(d['check: world count against test processor count at the saved updates'], indent=None)[:3000])
        print(json.dumps(d['check: performances counted 250 updates after a load, by environment']))
    print('\n### Comparisons\n')
    print(json.dumps(d['comparisons'], indent=1))


if __name__ == '__main__':
    main()
