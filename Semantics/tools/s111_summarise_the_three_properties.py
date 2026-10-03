#!/usr/bin/env python3
"""s111_summarise_the_three_properties.py

What it does, in plain words: gathers the numbers the S111 results file quotes from the four summary tables in
"Semantics/results/S111 Avida - the runs/" (copying and knockouts; the worlds over time; mutational robustness; Marletto
test on the logic tasks) into one file, "Semantics/results/S111 Avida - the three properties measured.json", with, for
Marletto's test, each task's numbers gathered over the runs where it was performed by at least 10% of the organisms
(the uncapped coverage, and the plan's capped one). It computes nothing new from the runs; it only collects and averages.
It also prints a short table of the gathered Marletto numbers for the results file.

  python3 Semantics/tools/s111_summarise_the_three_properties.py

Written 29 September 2026 by the one Opus 5.5 agent of log S111.
"""
import json, os, statistics

HERE = os.path.dirname(os.path.abspath(__file__))
SEM = os.path.dirname(HERE)
RUNS = os.path.join(SEM, 'results', 'S111 Avida - the runs')
OUT = os.path.join(SEM, 'results', 'S111 Avida - the three properties measured.json')
TASKS = ['NOT', 'NAND', 'AND', 'ORN', 'OR', 'ANDN', 'NOR', 'XOR', 'EQU']


def load(name):
    with open(os.path.join(RUNS, name + '.json')) as f:
        return json.load(f)


def spread(v):
    v = [x for x in v if x is not None]
    if not v:
        return None
    return {'mean': round(statistics.mean(v), 4), 'min': round(min(v), 4), 'max': round(max(v), 4), 'n': len(v)}


def main():
    ck, w, rb, mt = (load('copying and knockouts'), load('the worlds over time'), load('mutational robustness'),
                     load('Marletto test on the logic tasks'))
    marl = {}
    for label, pick in [('uncapped', lambda r: r.get('without_the_300_cap')), ('capped_300', lambda r: r)]:
        per = {}
        for run, r in mt.items():
            rr = pick(r)
            if not rr:
                continue
            for t, v in rr.get('tasks', {}).items():
                p = per.setdefault(t, {'runs': [], 'as_found': [], 'dominant_only': [], 'every_genotype_all_sites': [],
                                       'every_genotype_task_only_sites': [], 'still_copying': [],
                                       'task_only_sites_in_dominant': [], 'stopping_sites_in_dominant': [], 'coverage': []})
                p['runs'].append(run)
                p['as_found'].append(v['share_performing_as_found'])
                p['dominant_only'].append(v['share_performing_after_dominant_only'])
                p['every_genotype_all_sites'].append(v['share_performing_after_every_genotype'])
                p['every_genotype_task_only_sites'].append(v['share_performing_after_every_genotype_task_only_sites'])
                p['still_copying'].append(v['share_copying_among_performers_after_every_genotype_task_only_sites'])
                p['task_only_sites_in_dominant'].append(len(v['task_only_sites_in_dominant']))
                p['stopping_sites_in_dominant'].append(len(v['dominant_task_sites']))
                p['coverage'].append(round(rr['organisms_covered'] / rr['organisms'], 4))
        marl[label] = {t: dict({'runs': per[t]['runs']}, **{k: spread(v) for k, v in per[t].items() if k != 'runs'})
                       for t in TASKS if t in per}
    out = {'log': 'S111', 'decision': 'S59',
           'note': 'Collected by tools/s111_summarise_the_three_properties.py from the four summary tables in '
                   '"results/S111 Avida - the runs/"; nothing here is computed from the runs directly.',
           'copied': {'ancestor': ck['ancestor'], 'essential_sites': ck['essential_sites'],
                      'essential_instructions': ck['essential_instructions'],
                      'knockouts_stopping_copying': len(ck['essential_sites']),
                      'knockouts_leaving_copying_and_fitness': sum(1 for k in ck['knockouts'] if k['viable'] and k['fitness_ratio'] == 1.0),
                      'fidelity_sampled_in_test_processor': ck['fidelity'],
                      'in_the_worlds': {c: {k: v[k] for k in ('share_births_identical_to_parent', 'births_per_organism_per_update',
                                                                 'average_generation_at_end', 'organisms_min_from_1000')}
                                        for c, v in w['by_condition'].items()},
                      'K1_random_programs': ck['K1_random_programs'], 'K2_copy_loop_knocked_out': ck['K2_copy_loop_knocked_out']},
           'resists_change': {'robustness_ancestor': rb['ancestor'], 'robustness_by_condition': rb['by_condition'],
                              'low_beside_high': rb['low_beside_high'],
                              'conservation_at_last_save': {c: {k: v['at_last_save'][k] for k in
                                                                ('conserved_essential', 'conserved_non_essential')}
                                                            for c, v in w['by_condition'].items()}},
           'remains': {c: {k: v['at_last_save'][k] for k in ('copy_loop_exact', 'head_exact', 'whole_ancestor',
                                                              'share_organisms_self_copying', 'mean_length', 'genotypes')}
                       for c, v in w['by_condition'].items()},
           'tasks_at_end_runs_with_any': {c: v['tasks_at_end_runs_with_any'] for c, v in w['by_condition'].items()},
           'controls': w['controls'],
           'marletto_test_by_task': marl}
    with open(OUT, 'w') as f:
        json.dump(out, f, indent=1)
    print('| task | runs | task-only sites in the dominant | performing as found | after the dominant only | after every genotype\'s task-only sites | of former performers, still copying |')
    print('|---|---|---|---|---|---|---|')
    for t, v in marl['uncapped'].items():
        f = lambda s, p=3: '%.*f (%.*f to %.*f)' % (p, s['mean'], p, s['min'], p, s['max'])
        print('| %s | %d | %s | %s | %s | %s | %s |' % (t, len(v['runs']), f(v['task_only_sites_in_dominant'], 1),
              f(v['as_found']), f(v['dominant_only']), f(v['every_genotype_task_only_sites']), f(v['still_copying'])))


if __name__ == '__main__':
    main()
