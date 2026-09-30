#!/usr/bin/env python3
"""s116_gather_the_results_after_the_cross_examination.py

A corrected copy of s116_gather_the_results.py (kept unchanged), made when log S116's GLM cross-examination was settled
(results/S116 Routine runs from Astra's replies - the GLM cross-examination, settled.md). Each change is marked with the
objection it answers: [Xa2/Xb3] the input-order check, [Xa4/Xc1] the plan's B2.1 rule per run, [Xb1] the median's
name, [Xb2] per-input counts, A's and B's copying time, the AND resource, [Xb6] inconsistent grants, [Xb7/Xc2] K's
median, maximum and the share of programs the 100 sequences carry, [Xc2] never-rewarded arithmetic ever seen, [Xc3]
distinct sequences in the continuation. It reads, besides S116's scratch summaries, the settlement's own readings in
the scratch space (s116x_settle/, made by tools/s116x_settle_*.py) and writes
results/S116 Routine runs from Astra's replies - results, after the cross-examination.json. No Avida process is started.

What the original does, in plain words:

What it does, in plain words (log S116): gathers the summaries the S116 scripts wrote in the scratch space (the probe of
S113's saved program populations, the K count, reply 02's banks, the rare-kind competition, the continuation of FIXED
LARGE LIST seed 2) and applies to them, one by one, the rules for "counts for" and "counts against" written before
running (results/S116 Routine runs from Astra's replies - how they will be tested, written before running.md). It sets
S113's own numbers beside them where the plan compares (read from S113's corrected results .json, unchanged). It writes
the results .json into the repository (results/S116 Routine runs from Astra's replies - results.json) and prints the
tables the results .md copies. No Avida process is started.
Written 30 September 2026 by the one Opus 5.5 agent of log S116.
"""
import json, os, statistics, sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
SEM = os.path.dirname(HERE)
S116 = '/tmp/claude-0/-home-user-ThreadSmith/8d9323da-c0ec-57ec-91fd-8f99ca99320a/scratchpad/s116'
OUT = os.path.join(SEM, 'results', "S116 Routine runs from Astra's replies - results, after the cross-examination.json")
SETTLE = '/tmp/claude-0/-home-user-ThreadSmith/8d9323da-c0ec-57ec-91fd-8f99ca99320a/scratchpad/s116x_settle'  # the settlement's readings
S113J = os.path.join(SEM, 'results', 'S113 Which execution environments learn - results, after the cross-examination.json')
ENVS = ['fixed_graded', 'equ_only', 'no_rewards', 'growing', 'common_pays_less', 'fixed_large']
NAMES = {'fixed_graded': 'FIXED LIST, GRADED', 'equ_only': 'ONE HARD TASK ONLY', 'no_rewards': 'NO TASK REWARDS',
         'growing': 'GROWING LIST', 'common_pays_less': 'COMMON TASKS PAY LESS', 'fixed_large': 'FIXED LARGE LIST'}
PAYING = ['fixed_graded', 'growing', 'common_pays_less', 'fixed_large']   # equ_only never paid (S113)
SEEDS = [1, 2, 3]
MARKS = [str(m) for m in range(5000, 50001, 5000)]


def three_seed(a, b):
    """S113's rule: 'more' only if every seed of a is above every seed of b; 'fewer' the reverse."""
    if min(a) > max(b):
        return 'more'
    if max(a) < min(b):
        return 'fewer'
    return 'not separated by three seeds'


def runs(env):
    return ['%s_seed%d' % (env, s) for s in SEEDS]


def main():
    probe = json.load(open(S116 + '/probes/summary.json'))['per run']
    k = json.load(open(S116 + '/k/summary.json'))['per run']
    r02 = json.load(open(S116 + '/r02/summary.json'))
    comp = json.load(open(S116 + '/competition/summary.json'))
    ext = json.load(open(S116 + '/extension/counts.json'))
    s113 = json.load(open(S113J))
    tp113 = s113['test processor reading']['per run']
    res = {'what': 'log S116: routine runs from GPT 6 Astra\'s replies (S115 batches 2 and 3) and FIXED LARGE LIST seed 2 '
                   'continued to 75,000; written by tools/s116_gather_the_results.py from the scratch summaries',
           'plan': "results/S116 Routine runs from Astra's replies - how they will be tested, written before running.md"}

    # ---------------- batch 2: the probe
    table = {}
    for e in ENVS:
        for r in runs(e):
            p = probe[r]['per_save']
            table[r] = {m: p[m] for m in MARKS}
    res['B2 probe per run and save'] = table
    b21 = {}
    for e in ENVS:
        rows = {}
        for r in runs(e):
            rise = probe[r]['ever_seen_rise_25000_to_50000']
            change = probe[r]['present_change_25000_to_50000']
            rows[r] = {'ever_seen_rise_25000_to_50000': rise, 'present_change_25000_to_50000': change,
                       'turnover_without_accumulation': rise >= 3 and change < 0}
            # [Xa4/Xc1] the plan's whole B2.1 rule, per run: for / against / neither
            a, b = probe[r]['per_save']['25000'], probe[r]['per_save']['50000']
            f = (b['ever_seen_all'] > a['ever_seen_all'] and b['present_all'] > a['present_all']) or \
                b['present_all'] >= b['ever_seen_all'] - 1
            rows[r]['by the plan\'s rule'] = 'against' if rows[r]['turnover_without_accumulation'] else ('for' if f else 'neither')
        rows['runs with turnover without accumulation'] = sum(v['turnover_without_accumulation'] for v in rows.values())
        v3 = [rows[r]['by the plan\'s rule'] for r in runs(e)]
        rows['[Xa4/Xc1] by three seeds'] = ('for' if v3 == ['for'] * 3 else 'against' if v3 == ['against'] * 3
                                            else 'not the same in all three seeds: ' + ' / '.join(v3))
        b21[NAMES[e]] = rows
    res['B2.1 accumulation (logic plus never-rewarded arithmetic)'] = b21
    b22 = {}
    for e in ENVS:
        rows = {}
        fr = []
        for r in runs(e):
            t = probe[r]['retention_25000_to_50000']
            f = t['present_at_every_save_between'] / t['present_at_both_ends'] if t['present_at_both_ends'] else None
            rows[r] = dict((x, t[x]) for x in ['present_at_25000', 'present_at_both_ends', 'present_at_every_save_between',
                                               'present_after_a_sampled_gap'])
            rows[r]['continuous_over_endpoint'] = round(f, 3) if f is not None else None
            if f is not None:
                fr.append(f)
        mid = statistics.median(fr) if fr else None
        # [Xb1] the median of the three seeds' shares: the value of the middle run by this share, not seed 2
        rows['median of the three seeds (the middle run by this share)'] = round(mid, 3) if mid is not None else None
        if e in PAYING:
            rows['verdict'] = 'for' if mid >= 0.8 else 'against'
        b22[NAMES[e]] = rows
    res['B2.2 kept at every save, 25,000 to 50,000'] = b22
    nr = [len(probe[r]['present_at_50000']['arith_present']) for r in runs('no_rewards')]
    b23 = {'NO TASK REWARDS, arithmetic present at 50,000': nr}
    for measure, get in [('present at 50,000', lambda r: len(probe[r]['present_at_50000']['arith_present'])),
                         ('common at 50,000', lambda r: len(probe[r]['present_at_50000']['arith_common']))]:
        base = [get(r) for r in runs('no_rewards')]
        out = {'NO TASK REWARDS': base}
        for e in ENVS:
            if e == 'no_rewards':
                continue
            v = [get(r) for r in runs(e)]
            out[NAMES[e]] = {'seeds': v, 'against NO TASK REWARDS': three_seed(v, base)}
        b23[measure] = out
    b23['[Xc2] ever seen by 50,000 (the settlement\'s reading)'] = json.load(open(SETTLE + '/arith_ever_seen.json'))
    res['B2.3 never-rewarded arithmetic'] = b23
    b24 = {}
    rises = {}
    for e in ENVS:
        rows = {}
        rr = []
        for r in runs(e):
            a, b = k[r]['5000']['K_weighted_mean'], k[r]['50000']['K_weighted_mean']
            rows[r] = {m: k[r][m]['K_weighted_mean'] for m in MARKS}
            rows[r]['viable of the 100 at 5,000 and 50,000'] = [k[r]['5000']['viable'], k[r]['50000']['viable']]
            rows[r]['viable of the 100 at every save'] = {m: k[r][m]['viable'] for m in MARKS}
            # [Xb7/Xc2] the median and maximum the plan named, and how many programs the 100 sequences carry
            for m in ('5000', '50000'):
                rows[r]['at %s: K median, K max, programs in the 100 tested, programs in the population' % m] = [
                    k[r][m]['K_median'], k[r][m]['K_max'], k[r][m]['programs_in_tested'], k[r][m]['programs_in_population']]
            rr.append(round(b - a, 3))
        rows['rise 5,000 to 50,000'] = rr
        rows['rose in all three seeds'] = all(x > 0 for x in rr)
        rises[e] = rr
        b24[NAMES[e]] = rows
    for e in PAYING:
        b24[NAMES[e]]['rise against NO TASK REWARDS rise'] = three_seed(rises[e], rises['no_rewards'])
    any_for = [NAMES[e] for e in PAYING if b24[NAMES[e]]['rose in all three seeds']
               and b24[NAMES[e]]['rise against NO TASK REWARDS rise'] == 'more']
    b24['verdict'] = ('for, in ' + ', '.join(any_for)) if any_for else (
        'against: no paying environment rose in all three seeds' if not any(b24[NAMES[e]]['rose in all three seeds']
                                                                           for e in PAYING)
        else 'against: the paying rises are not above NO TASK REWARDS by the three-seed rule')
    res['B2.4 K (reply 05)'] = b24
    b25 = {}
    worst = []
    for e in ENVS:
        rows = {}
        for r in runs(e):
            c = probe[r]['per_save']['50000']
            h = probe[r]['logic_high']['50000']
            rows[r] = {'core present': c['present_logic'], 'logic_high present': h['present'],
                       'core common': c['common_logic'], 'logic_high common': h['common']}
            if e in PAYING:
                for kind in ('present', 'common'):
                    cc = c['%s_logic' % kind]
                    if cc and (cc - h[kind]) / cc > 0.10:
                        worst.append('%s %s: core %d, logic_high %d' % (r, kind, cc, h[kind]))
        b25[NAMES[e]] = rows
    b25['paying runs where logic_high is more than 10% below core'] = worst
    b25['verdict'] = 'against (a caution on S113\'s counts)' if worst else 'for'
    res['B2.5 small against large inputs, logic tasks at 50,000'] = b25
    order = {}
    for e in ENVS:
        order[NAMES[e]] = {'probe common logic at 50,000': [probe[r]['per_save']['50000']['common_logic'] for r in runs(e)],
                           'S113 test processor common at 50,000': [tp113[r]['common_at_marks']['50000'] for r in runs(e)],
                           'probe present logic at 50,000': [probe[r]['per_save']['50000']['present_logic'] for r in runs(e)],
                           'S113 test processor present at 50,000': [tp113[r]['any_at_marks']['50000'] for r in runs(e)]}
    res['B2 probe against S113 test processor, logic tasks at 50,000'] = order
    pairs = {}
    for a, b in [('growing', 'fixed_large'), ('growing', 'fixed_graded'), ('fixed_large', 'fixed_graded'),
                 ('common_pays_less', 'fixed_graded'), ('fixed_graded', 'no_rewards')]:
        va = [probe[r]['per_save']['50000']['common_logic'] for r in runs(a)]
        vb = [probe[r]['per_save']['50000']['common_logic'] for r in runs(b)]
        pairs['%s against %s' % (NAMES[a], NAMES[b])] = three_seed(va, vb)
    res['B2 probe, common logic at 50,000, by the three-seed rule'] = pairs
    # descriptive readings added after the first results (departures, not in the plan)
    wo = {}
    for e in ENVS:
        wo[NAMES[e]] = {'common, large inputs in the world\'s order, at 25,000 and 50,000':
                        [[probe[r]['logic_high_world_order'][m]['common'] for m in ('25000', '50000')] for r in runs(e)],
                        'present, large inputs in the world\'s order, at 50,000':
                        [probe[r]['logic_high_world_order']['50000']['present'] for r in runs(e)],
                        'common, on at least one of the 8 small inputs, at 50,000':
                        [probe[r]['per_save']['50000']['common_logic_on_any_input'] for r in runs(e)]}
    res['B2 added readings (departures): logic tasks by input kind'] = wo
    pairs2 = {}
    for a, b in [('growing', 'fixed_large'), ('growing', 'fixed_graded'), ('fixed_large', 'fixed_graded'),
                 ('common_pays_less', 'fixed_graded')]:
        va = [probe[r]['logic_high_world_order']['50000']['common'] for r in runs(a)]
        vb = [probe[r]['logic_high_world_order']['50000']['common'] for r in runs(b)]
        pairs2['%s against %s' % (NAMES[a], NAMES[b])] = three_seed(va, vb)
    res['B2 added reading, world-order large inputs, common logic at 50,000, by the three-seed rule'] = pairs2
    # [Xb2] per-input counts behind results section 2.1 (read from the probe's raw files by tools/s116x_settle_per_input.py)
    res['[Xb2] programs viable, and viable and performing NOT, per input set, at 50,000'] = json.load(
        open(SETTLE + '/per_input_at_50000.json'))
    # [Xa2/Xb3] the order check: the same three numbers in all six orders, fresh numbers in the world's order, the same
    # numbers made small (tools/s116x_settle_order_check.py, analyze mode, every run at 50,000)
    oc = {}
    for e in ENVS:
        for r in runs(e):
            d = json.load(open(SETTLE + '/order_%s/result.json' % r))
            oc[r] = {n: {'viable': v['viable'], 'logic common': v['logic_common'], 'logic present': v['logic_present']}
                     for n, v in d['results'].items()}
            oc[r]['programs'] = next(iter(d['results'].values()))['programs']
            oc[r]['exit'] = d['exit']
    res['[Xa2/Xb3] order check at 50,000'] = oc

    # ---------------- batch 3a: reply 02
    banks = r02['banks']
    b3a = {}
    for mech in ('scalar', 'reputation'):
        disc = [banks['%s seed %d update 5000' % (mech, s)]['share_discriminating'] for s in (101, 102, 103)]
        rej = [banks['%s seed %d update 5000' % (mech, s)]['share_reject_all'] for s in (101, 102, 103)]
        top = [banks['%s seed %d update 5000' % (mech, s)]['most_common_pattern'] for s in (101, 102, 103)]
        top1 = [banks['%s seed %d update 1000' % (mech, s)]['most_common_pattern'] for s in (101, 102, 103)]
        against = all(r >= 0.90 and d < 0.05 for r, d in zip(rej, disc))
        forr = sum(d >= 0.10 for d in disc) >= 2 and any(t != 'accept only 1' or t != t1 for t, t1 in zip(top, top1))
        b3a[mech] = {'discriminating at 5,000': disc, 'reject all at 5,000': rej, 'most common at 5,000': top,
                     'most common at 1,000': top1,
                     'discriminating at 1,000': [banks['%s seed %d update 1000' % (mech, s)]['share_discriminating']
                                                 for s in (101, 102, 103)],
                     'founder pattern (accept only 1) share at 1,000 and 5,000':
                         [[round(banks['%s seed %d update %d' % (mech, s, u)]['patterns'].get('accept only 1', 0) / 3600, 4)
                           for u in (1000, 5000)] for s in (101, 102, 103)],
                     'verdict B3a.1': 'against' if against else ('for, by the letter of the rule' if forr else 'unclear')}
    b3a['B3a.2 largest contrast in the swapped or off arms'] = max(v['largest_contrast_in_swapped_or_off_arm']
                                                                   for v in banks.values())
    b3a['banks'] = banks
    b3a['Avida CPU seconds (runs and assays, from reply 02\'s own timing)'] = r02['avida_cpu_seconds']
    # [Xb6] sequences whose grants to one cue differ between the pairs (the reader's >= 5 would count them as giving)
    b3a['[Xb6] sequences with inconsistent grants, largest in any bank'] = max(
        v.get('sequences_with_inconsistent_grants', 0) for v in banks.values())
    res['B3a reply 02'] = b3a

    # ---------------- batch 3b: competition
    rows = comp['runs']
    b3b = {'kinds': comp['kinds'], 'runs': rows}
    end = {}
    for key, v in rows.items():
        end.setdefault(v['start_share_A'], []).append(v['saves']['2000']['share_A'])
    b3b['share of A at 2,000, by starting share (three placements)'] = {str(s): end[s] for s in sorted(end)}
    up_rare = all(x > 0.01 for x in end[0.01]) and all(x > 0.10 for x in end[0.10])
    down_common = all(x < 0.90 for x in end[0.90]) and all(x < 0.99 for x in end[0.99])
    a_falls_rare = all(x < 0.01 for x in end[0.01])
    a_rises_common = all(x > 0.99 for x in end[0.99])
    b3b['verdict B3b.1'] = ('for: both kinds grow when rare' if up_rare and down_common else
                            'against: no growth from rare' if a_falls_rare or a_rises_common else 'unclear (B3b.2)')
    b3b['other sequences at 2,000 (should be 0 with instruction changes off)'] = {
        k2: v['saves']['2000']['other'] for k2, v in rows.items()}
    # [Xb2] A's and B's copying time on the test CPU without resources (the one analyze call made when the kinds were
    # chosen, scratch competition_check/), and the AND resource in each run (tools/s116x_settle_resource_levels.py)
    ab = [l.split() for l in open(S116 + '/competition_check/data/ab.dat') if l.strip() and not l.startswith('#')]
    b3b['[Xb2] gestation time on the test CPU, A and B'] = {'A': int(ab[0][4]), 'B': int(ab[1][4])}
    b3b['[Xb2] AND resource per run (full pay needs 400)'] = json.load(open(SETTLE + '/resource_levels.json'))
    res['B3b rare-kind competition'] = b3b

    # ---------------- extension
    tp = ext['test_processor']
    wc = ext['world_count_every_250']
    tp_counts = {m: tp[m]['common'] for m in tp}
    after50 = {int(u): v['common'] for u, v in wc.items() if int(u) > 50000}
    upto = {int(u): v['common'] for u, v in wc.items() if int(u) <= 50000}
    run_high = max(s113['per run']['fixed_large_seed2']['highest_common'], max(upto.values()))  # S113: 41, at 48,250
    last_new_high = None
    for u in sorted(after50):
        if after50[u] > run_high:
            run_high = after50[u]
            last_new_high = u
    e_for = tp_counts['75000'] >= 44 and last_new_high is not None and last_new_high >= 65000
    tp_after60_new = any(tp_counts[m] > max(tp_counts[x] for x in tp_counts if int(x) <= 60000)
                         for m in tp_counts if int(m) > 60000)
    e_against = abs(tp_counts['75000'] - 41) <= 1 and not tp_after60_new and (last_new_high is None or last_new_high <= 60000)
    res['E continuation of FIXED LARGE LIST seed 2'] = {
        'test processor common': tp_counts,
        'test processor present': {m: tp[m]['present'] for m in tp},
        'test processor common and replicating': {m: tp[m]['common_and_replicating'] for m in tp},
        'world count common every 250 (49,250 to 75,000)': {u: v['common'] for u, v in wc.items()},
        'world count common, highest up to 50,000 (S113 per run, and 49,250 to 50,000 here)':
            max(s113['per run']['fixed_large_seed2']['highest_common'], max(upto.values())),
        'world count: last new high after 50,000': last_new_high,
        'pieces': ext['pieces'],
        '[Xc3] distinct sequences': {m: tp[m]['distinct_sequences'] for m in tp},
        'verdict': 'E.1 keeps rising' if e_for else ('levelled off' if e_against else 'E.2 rising slowly or unclear')}
    json.dump(res, open(OUT, 'w'), indent=1, ensure_ascii=False)
    print('written', OUT)


if __name__ == '__main__':
    main()
