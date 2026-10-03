#!/usr/bin/env python3
"""s116_read_the_evaluation_banks.py

What it does, in plain words (log S116, batch 3 of S115's plan, GPT 6 Astra's reply 02): after reply 02's own suite
(tools/s115/02/make_experiments.py and the run_suite.py it writes, both unchanged) has run its six 5,000-update runs and
36 bank assays, this script reads the assays' own summaries (contrasts.csv, written by reply 02's summarize_bank.py) and
says, for every distinct instruction sequence living at update 1,000 and at update 5,000, which of the three cues
(0, 1, 2) its programs give energy to. Then, weighted by the number of Avida programs carrying each sequence: the share
that gives to no cue ("reject all"), to every cue ("accept all"), or to some cues and not others ("discriminating"),
and the most common response pattern. It also checks that the swapped and off arms show no cue contrast.
No Avida process is started. Reads scratch s116/r02/results_5000/; writes s116/r02/summary.json.
Written 30 September 2026 by the one Opus 5.5 agent of log S116.
"""
import csv, json, os, sys
from collections import defaultdict

ROOT = '/tmp/claude-0/-home-user-ThreadSmith/8d9323da-c0ec-57ec-91fd-8f99ca99320a/scratchpad/s116/r02'


def read_bank(bank):
    rows = list(csv.DictReader(open(os.path.join(bank, 'contrasts.csv'))))
    grants = defaultdict(lambda: defaultdict(list))
    weight = {}
    control_max = 0.0
    for r in rows:
        if r['arm'] != 'active':
            control_max = max(control_max, abs(float(r['contrast'])))
            continue
        g = r['genotype_id']
        weight[g] = int(r['weight'])
        grants[g][int(r['cue_left'])].append(float(r['grant_left']))
        grants[g][int(r['cue_right'])].append(float(r['grant_right']))
    patterns = defaultdict(int)
    inconsistent = 0
    for g, per in grants.items():
        given = []
        for cue in (0, 1, 2):
            vals = per[cue]
            if len(set(vals)) > 1:
                inconsistent += 1
            if sum(vals) / len(vals) >= 5:
                given.append(cue)
        patterns[tuple(given)] += weight[g]
    total = sum(patterns.values())
    reject = patterns.get((), 0)
    accept_all = patterns.get((0, 1, 2), 0)
    top = max(patterns.items(), key=lambda kv: kv[1])
    name = lambda p: 'reject all' if not p else ('accept all' if p == (0, 1, 2) else
                                                  'accept only ' + ' and '.join(map(str, p)))
    return {'programs': total, 'distinct_sequences': len(grants),
            'share_reject_all': round(reject / total, 4), 'share_accept_all': round(accept_all / total, 4),
            'share_discriminating': round((total - reject - accept_all) / total, 4),
            'most_common_pattern': name(top[0]), 'most_common_share': round(top[1] / total, 4),
            'patterns': {name(p): n for p, n in sorted(patterns.items())},
            'sequences_with_inconsistent_grants': inconsistent,
            'largest_contrast_in_swapped_or_off_arm': control_max}


def main():
    res = {}
    for mech in ('scalar', 'reputation'):
        for seed in (101, 102, 103):
            for u in (1000, 5000):
                bank = os.path.join(ROOT, 'results_5000', mech, 'seed-%d' % seed, 'bank-%d' % u)
                res['%s seed %d update %d' % (mech, seed, u)] = read_bank(bank)
    runs = json.load(open(os.path.join(ROOT, 'results_5000', 'runs.json')))
    cpu = sum(r['cpu'].get('cpu_seconds', 0) for r in runs['evolution'] + runs['assays'])
    json.dump({'what': 'log S116 batch 3a: reply 02 banks read', 'banks': res, 'avida_cpu_seconds': round(cpu)},
              open(os.path.join(ROOT, 'summary.json'), 'w'), indent=1)
    for k, v in res.items():
        print(k, v['programs'], v['distinct_sequences'], v['share_reject_all'], v['share_discriminating'],
              v['share_accept_all'], v['most_common_pattern'], v['largest_contrast_in_swapped_or_off_arm'])
    print('Avida CPU seconds', round(cpu))


if __name__ == '__main__':
    main()
