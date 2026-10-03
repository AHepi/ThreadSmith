#!/usr/bin/env python3
"""s111_measure_copying_and_knockouts.py

What it does, in plain words: the measures of "copied" from the S111 plan that need no world run, all made in Avida's own
test processor (see s111_avida_test_processor.py):
  C1  the default ancestor: does it make an exact copy of itself, how many instructions a copy takes;
  C2  the knockout test: each of the ancestor's 100 instructions in turn replaced by the do-nothing instruction nop-X;
      for each, does the program still make an exact copy of itself;
  C3  copy fidelity: the share of offspring identical to the parent, expected from the error rates, and counted over
      1,000 offspring made by Avida at each of the three rates (Avida's SAMPLE_OFFSPRING);
  K1  10,000 random programs of the ancestor's length: how many make an exact copy of themselves;
  K2  the ancestor with the h-copy of its copy loop knocked out.
Writes a compact summary (JSON and a Markdown table) into "Semantics/results/S111 Avida - the runs/"; raw Avida output
stays in the scratch space.

  python3 Semantics/tools/s111_measure_copying_and_knockouts.py

Written 29 September 2026 by the one Opus 5.5 agent of log S111.
"""
import json, os, random, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import s111_avida_test_processor as T  # noqa: E402
from s111_run_the_avida_worlds import ancestor_letters, RATES  # noqa: E402

OUTDIR = os.path.join(os.path.dirname(HERE), 'results', 'S111 Avida - the runs')
DIVIDE_INS = DIVIDE_DEL = 0.05   # Avida's defaults, unchanged in every main run


def knockouts(seq):
    muts = [seq[:i] + T.NULL + seq[i + 1:] for i in range(len(seq))]
    base = T.evaluate([seq])[0]
    rows = T.evaluate(muts)
    out = []
    for i, r in enumerate(rows):
        out.append({'site': i + 1, 'instruction': T.name_of(seq[i]), 'letter': seq[i], 'viable': r['viable'],
                    'fitness_ratio': round(r['fitness'] / base['fitness'], 6) if base['fitness'] else None})
    return base, out


def main():
    anc = ancestor_letters()
    base, ko = knockouts(anc)
    essential = [k['site'] for k in ko if not k['viable']]
    res = {'ancestor': {'letters': anc, 'length': len(anc), 'viable': base['viable'], 'gestation_instructions': base['gest_time'],
                        'copy_length': base['copy_length'], 'executed_length': base['exe_length'], 'fitness': base['fitness']},
           'knockouts': ko, 'essential_sites': essential,
           'essential_instructions': [T.name_of(anc[s - 1]) for s in essential]}
    # C3: fidelity
    fid = {}
    L = len(anc)
    for cond, mu in RATES.items():
        exp_any = (1 - mu) ** L * (1 - DIVIDE_INS) * (1 - DIVIDE_DEL)
        exp_changed = (1 - mu * 25 / 26) ** L * (1 - DIVIDE_INS) * (1 - DIVIDE_DEL)
        counts = T.sample_offspring(anc, 1000, [('COPY_MUT_PROB', mu)])
        n = sum(counts.values())
        same = counts.get(anc, 0)
        viable_offspring = T.evaluate(sorted(counts))
        via = sum(counts[r['sequence']] for r in viable_offspring if r['viable'])
        fid[cond] = {'copy_error_rate': mu, 'expected_identical_if_every_error_changes_the_instruction': round(exp_any, 4),
                     'expected_identical_if_an_error_can_redraw_the_same_instruction': round(exp_changed, 4),
                     'sampled_offspring': n, 'identical_to_parent': same, 'share_identical': round(same / n, 4),
                     'offspring_that_copy_themselves': via, 'share_offspring_viable': round(via / n, 4)}
    res['fidelity'] = fid
    # K1, K2
    rng = random.Random(1111)
    rand = [''.join(rng.choice(T.LETTERS) for _ in range(L)) for _ in range(10000)]
    rv = T.evaluate(rand)
    res['K1_random_programs'] = {'tested': len(rv), 'viable': sum(r['viable'] for r in rv),
                                 'that_split_at_all_note': 'viable means an exact copy of itself (or a cycle back to it)'}
    ko_seq = anc[:anc.rindex('v')] + T.NULL + anc[anc.rindex('v') + 1:]
    res['K2_copy_loop_knocked_out'] = {'letters': ko_seq, 'viable': T.evaluate([ko_seq])[0]['viable']}
    os.makedirs(OUTDIR, exist_ok=True)
    with open(os.path.join(OUTDIR, 'copying and knockouts.json'), 'w') as f:
        json.dump(res, f, indent=1)
    lines = ['# S111 copying and knockouts (written by tools/s111_measure_copying_and_knockouts.py)', '',
             'Ancestor: %d instructions, makes an exact copy of itself: %s; %d instructions executed per copy.'
             % (len(anc), 'yes' if base['viable'] else 'no', base['gest_time']), '',
             '## Knockout test (C2): sites whose knockout stops exact self-copying', '',
             '%d of %d sites: %s' % (len(essential), L, ', '.join('%d %s' % (s, T.name_of(anc[s - 1])) for s in essential)), '',
             'The other %d sites: knockout leaves self-copying and fitness as they were (fitness ratios: %s).'
             % (L - len(essential), sorted({k['fitness_ratio'] for k in ko if k['viable']})), '',
             '## Copy fidelity (C3)', '', '| condition | error rate per copied instruction | expected identical | identical of 1,000 sampled | offspring that copy themselves |',
             '|---|---|---|---|---|']
    for cond, v in fid.items():
        lines.append('| %s | %s | %.3f to %.3f | %d | %d |' % (cond, v['copy_error_rate'],
                     v['expected_identical_if_every_error_changes_the_instruction'],
                     v['expected_identical_if_an_error_can_redraw_the_same_instruction'], v['identical_to_parent'],
                     v['offspring_that_copy_themselves']))
    lines += ['', '## Controls', '', 'K1: %d of %d random programs of length %d make an exact copy of themselves.'
              % (res['K1_random_programs']['viable'], len(rv), L),
              'K2: the ancestor with its copy loop knocked out makes an exact copy of itself: %s.'
              % ('yes' if res['K2_copy_loop_knocked_out']['viable'] else 'no'), '']
    with open(os.path.join(OUTDIR, 'copying and knockouts.md'), 'w') as f:
        f.write('\n'.join(lines))
    print('\n'.join(lines))


if __name__ == '__main__':
    main()
