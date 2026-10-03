#!/usr/bin/env python3
"""s111_marletto_test_on_the_logic_tasks.py

What it does, in plain words: section 5 of the S111 plan. Marletto's test for knowledge, as log S110 quotes it: knowledge
"is exactly the thing one would ultimately have to eliminate in order to prevent a particular transformation from being
performed reliably." (Marletto, ch. 5). Here the transformation is one of Avida's logic tasks (NOT, NAND, ... EQU: the
organism reads numbers the world gives it and writes back their logical combination). For each world run at update
50,000, and each task performed by at least 10% of its organisms:
  T1  in the most common genotype, each instruction in turn is replaced by the do-nothing instruction nop-X; the sites whose
      knockout stops the task are listed, with whether the program still copies itself;
  T2  across the population (the most common genotypes, together at least 90% of the organisms, at most 300 genotypes,
      each run alone in the test processor), the share of organisms whose genotype performs the task: (i) as found;
      (ii) with the task's sites knocked out in the most common genotype only; (iii) with every genotype's own task sites
      (from its own knockout map) knocked out at once, in every genotype.
Added after the plan was written (marked so in the results): (iv) as (iii) but only the "task-only" sites, whose single
knockout stops the task and leaves copying (the planned (iii) also removes the copying machinery, which stops every task
in the test processor); and every measure repeated without the cap of 300 genotypes, which kept coverage well under 90%.
Writes a compact summary (JSON and Markdown) into "Semantics/results/S111 Avida - the runs/".

  python3 Semantics/tools/s111_marletto_test_on_the_logic_tasks.py

Written 29 September 2026 by the one Opus 5.5 agent of log S111.
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import s111_avida_test_processor as T  # noqa: E402
from s111_run_the_avida_worlds import OUT as RUNS, RATES, SEEDS  # noqa: E402
from s111_measure_the_worlds_over_time import spop, table  # noqa: E402

RES = os.path.join(os.path.dirname(HERE), 'results', 'S111 Avida - the runs')
UPDATE = 50000
NAMES = ['NOT', 'NAND', 'AND', 'ORN', 'OR', 'ANDN', 'NOR', 'XOR', 'EQU']


def knock(seq, sites):
    s = list(seq)
    for i in sites:
        s[i] = T.NULL
    return ''.join(s)


def maps(seqs):
    """For each genotype: its own evaluation and, per task, the sites whose single knockout stops that task."""
    base = T.evaluate(seqs)
    flat = [knock(s, [i]) for s in seqs for i in range(len(s))]
    kos = T.evaluate(flat)
    out, k = [], 0
    for s, b in zip(seqs, base):
        rows = kos[k:k + len(s)]
        k += len(s)
        out.append({'base': b, 'ko': rows,
                    'task_sites': {t: [i for i, r in enumerate(rows) if b['task.%d' % t] > 0 and r['task.%d' % t] == 0]
                                   for t in range(9)}})
    return out


def one_run(run, cap=300):
    d = os.path.join(RUNS, run, 'data')
    p = os.path.join(d, 'detail-%d.spop' % UPDATE)
    if not os.path.exists(p):
        return None
    tasks = [r for r in table(os.path.join(d, 'tasks.dat')) if int(r[0]) == UPDATE][0]
    count = [r for r in table(os.path.join(d, 'count.dat')) if int(r[0]) == UPDATE][0]
    orgs = count[2]
    chosen = [t for t in range(9) if tasks[t + 1] / orgs >= 0.10]
    if not chosen:
        return {'tasks_at_10_percent': []}
    pop = sorted(spop(p), key=lambda x: -x[1])
    total = sum(n for _, n in pop)
    top, cov = [], 0
    for s, n in pop:
        if cov / total >= 0.90 or (cap and len(top) >= cap):
            break
        top.append((s, n))
        cov += n
    m = maps([s for s, _ in top])
    dom_seq, dom_n = top[0]
    res = {'organisms': total, 'genotypes_used': len(top), 'organisms_covered': cov, 'cap': cap,
           'dominant': {'length': len(dom_seq), 'abundance': dom_n, 'sequence': dom_seq}, 'tasks': {}}
    for t in chosen:
        dm = m[0]
        sites = dm['task_sites'][t]
        still_copies = [i for i in sites if dm['ko'][i]['viable']]
        found = sum(n for (s, n), g in zip(top, m) if g['base']['task.%d' % t] > 0)
        # (ii) the dominant only
        if sites:
            dko = T.evaluate([knock(dom_seq, sites)])[0]
            dom_after = dom_n if dko['task.%d' % t] > 0 else 0
        else:
            dko, dom_after = None, (dom_n if dm['base']['task.%d' % t] > 0 else 0)
        dom_before = dom_n if dm['base']['task.%d' % t] > 0 else 0
        one_copy = found - dom_before + dom_after
        # (iii) every genotype, its own sites, all at once
        joint = [knock(s, g['task_sites'][t]) for (s, _), g in zip(top, m) if g['task_sites'][t]]
        jr = iter(T.evaluate(joint)) if joint else iter([])
        after_all, copying_after_all, performers = 0, 0, 0
        no_single_site = 0
        for (s, n), g in zip(top, m):
            if g['base']['task.%d' % t] == 0:
                continue
            performers += n
            if g['task_sites'][t]:
                r = next(jr)
                after_all += n if r['task.%d' % t] > 0 else 0
                copying_after_all += n if r['viable'] else 0
            else:
                no_single_site += n
                after_all += n   # no single knockout stops it: left as it is (redundant sites; recorded)
                copying_after_all += n
        # added after the plan (see the results file): only the sites whose knockout stops the task and leaves copying
        only = [[i for i in g['task_sites'][t] if g['ko'][i]['viable']] for g in m]
        jo = [knock(s, o) for (s, _), g, o in zip(top, m, only) if g['base']['task.%d' % t] > 0 and o]
        jor = iter(T.evaluate(jo)) if jo else iter([])
        only_after, only_copying, only_none = 0, 0, 0
        for (s, n), g, o in zip(top, m, only):
            if g['base']['task.%d' % t] == 0:
                continue
            if o:
                r = next(jor)
                only_after += n if r['task.%d' % t] > 0 else 0
                only_copying += n if r['viable'] else 0
            else:
                only_none += n
                only_after += n
                only_copying += n
        res['tasks'][NAMES[t]] = {
            'task_only_sites_in_dominant': [i + 1 for i in only[0]],
            'task_only_site_instructions_in_dominant': [T.name_of(dom_seq[i]) for i in only[0]],
            'share_performing_after_every_genotype_task_only_sites': round(only_after / cov, 4),
            'share_copying_among_performers_after_every_genotype_task_only_sites': round(only_copying / performers, 4) if performers else None,
            'share_of_performers_with_no_task_only_site': round(only_none / performers, 4) if performers else None,
            'share_performing_world_count': round(tasks[t + 1] / orgs, 4),
            'dominant_performs': bool(dm['base']['task.%d' % t] > 0),
            'dominant_task_sites': [i + 1 for i in sites],
            'dominant_task_site_instructions': [T.name_of(dom_seq[i]) for i in sites],
            'dominant_task_sites_whose_knockout_leaves_copying': len(still_copies),
            'dominant_all_task_sites_knocked_out_copies_itself': (bool(dko['viable']) if dko else None),
            'share_performing_as_found': round(found / cov, 4),
            'share_performing_after_dominant_only': round(one_copy / cov, 4),
            'share_performing_after_every_genotype': round(after_all / cov, 4),
            'share_copying_among_performers_after_every_genotype': round(copying_after_all / performers, 4) if performers else None,
            'share_of_performers_with_no_single_site': round(no_single_site / performers, 4) if performers else None,
            'task_sites_per_performing_genotype_mean': round(
                sum(len(g['task_sites'][t]) * n for (s, n), g in zip(top, m) if g['base']['task.%d' % t] > 0) / performers, 2)
            if performers else None}
    return res


def main():
    out = {}
    for cond in RATES:
        for seed in SEEDS:
            run = 'main_%s_seed%d' % (cond, seed)
            r = one_run(run)
            if r is not None:
                if r.get('tasks'):
                    r['without_the_300_cap'] = one_run(run, cap=None)   # added after the plan: 90% coverage in full
                out[run] = r
                print(run, {k: (v['share_performing_as_found'], v['share_performing_after_dominant_only'],
                                v['share_performing_after_every_genotype']) for k, v in r.get('tasks', {}).items()}, flush=True)
    with open(os.path.join(RES, 'Marletto test on the logic tasks.json'), 'w') as f:
        json.dump(out, f, indent=1)
    L = ['# S111 Marletto\'s test on the logic tasks (written by tools/s111_marletto_test_on_the_logic_tasks.py)', '',
         'Update 50,000. Tasks performed by at least 10% of the organisms. Shares are of the organisms covered (the most common '
         'genotypes, together at least 90% of the organisms, at most 300 genotypes), each genotype run alone in the test processor.', '',
         'Columns: the sites of the most common genotype whose single knockout stops the task; of them, the "task-only" sites '
         '(copying survives their knockout), with their instructions; then the share of covered organisms whose genotype '
         'performs the task: as found; after the dominant\'s task sites are knocked out in the dominant only; after every '
         'genotype\'s own task sites are knocked out (all of them, as planned; this also stops copying); after every genotype\'s '
         'own task-only sites are knocked out (added), with the share of the former performers that still copy themselves. '
         'Last column: organisms covered / organisms (with the plan\'s cap of 300 genotypes; then without it).', '',
         '| run | task | dominant: stopping sites | task-only sites (instructions) | as found | dominant only | every genotype, all sites | every genotype, task-only sites | still copying | covered |',
         '|---|---|---|---|---|---|---|---|---|---|']
    for run, r in out.items():
        for label, rr in [('', r), (' (no cap)', r.get('without_the_300_cap'))]:
            if not rr:
                continue
            for t, v in rr.get('tasks', {}).items():
                L.append('| %s%s | %s | %d | %d (%s) | %.3f | %.3f | %.3f | %.3f | %.3f | %d / %d |' % (
                    run, label, t, len(v['dominant_task_sites']), len(v['task_only_sites_in_dominant']),
                    ' '.join(v['task_only_site_instructions_in_dominant']), v['share_performing_as_found'],
                    v['share_performing_after_dominant_only'], v['share_performing_after_every_genotype'],
                    v['share_performing_after_every_genotype_task_only_sites'],
                    v['share_copying_among_performers_after_every_genotype_task_only_sites'] or 0,
                    rr['organisms_covered'], rr['organisms']))
        if not r.get('tasks'):
            L.append('| %s | none at 10%% | - | - | - | - | - | - | - | - |' % run)
    with open(os.path.join(RES, 'Marletto test on the logic tasks.md'), 'w') as f:
        f.write('\n'.join(L) + '\n')
    print('\n'.join(L))


if __name__ == '__main__':
    main()
