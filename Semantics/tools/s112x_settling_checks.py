#!/usr/bin/env python3
"""s112x_settling_checks.py

What it does, in plain words: the reruns and new checks made to settle the GLM cross-examination of log S112
(results/S112 What the evolved sums are - the GLM cross-examination, settled.md). Every Avida program is run by Avida's
own analysis mode (the test processor, or TRACE), inside Avida's virtual CPU, through the S112 helper; nothing that
copies itself runs on the real machine. Reads the S112 raw output in the scratch space; writes one JSON file into the
scratch space (s112x_settle/settling_checks.json); nothing into the repository.

  Xa2  the NOT worked example (low seed 2's most common NOT sequence): sites 15 and 17 ablated one at a time; what the
       test processor credits, and what Avida's trace shows the program computing and writing.
  Xb1  for the 91 sequence-task pairs no set of one or two copying-safe sites stops (89 not stopped, 2 stopped by 3):
       (i) whether the sent search's start sets left the program replicating; (ii) every pair of sites with at least one
       site whose single ablation stops replication, ablated: does any stop the task while the program replicates?
  Xb2  for the 89 not stopped: how many of their route sites are replication-required, and which instructions.
  Xb3  the irreducible sets' sizes.
  Xb4  the 159 traces of each run's most common sequence with one replication-required site ablated: did the program
       split (divide) in the trace, against whether the test processor credited any task.

  python3 -B Semantics/tools/s112x_settling_checks.py [jobs]

Written 30 September 2026 by the Opus 5.5 agent that settled the S112 cross-examination, in the owner's Avida terms (S61).
"""
import collections, itertools, json, os, shutil, sys
from concurrent.futures import ProcessPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import s112_run_programs_in_avidas_test_processor as P  # noqa: E402
import s112_read_what_the_programs_compute_from_avidas_traces as R  # noqa: E402
import s112_find_minimal_removals as M  # noqa: E402

REM = P.SCRATCH + '/s112/removals'
TR = P.SCRATCH + '/s112/traces'
OUTDIR = P.SCRATCH + '/s112x_settle'


def jl(p):
    return [json.loads(x) for x in open(p)] if os.path.exists(p) else []


def trace_record(run, seqs):
    out = {}
    for line in open('%s/%s.jsonl' % (TR, run)):
        r = json.loads(line)
        if r['seq'] in seqs:
            out[r['seq']] = r
    return out


def xa2():
    run = 'main_low_seed2'
    seq = P.living(run)[0][0]
    out = {'run': run, 'sequence_length': len(seq), 'sites': {}}
    progs = {i: M.knock(seq, [i]) for i in (15, 17)}
    rows = P.evaluate([seq] + list(progs.values()))
    out['unablated'] = {'replicates': rows[0]['viable'], 'tasks': sorted(P.tasks_of(rows[0]))}
    d, paths = P.trace(list(progs.values()))
    try:
        for (i, prog), row, p in zip(progs.items(), rows[1:], paths):
            x = R.read_program(prog, p)
            e = x['sums'].get('NOT')
            out['sites'][i] = {
                'instruction': P.name_of(seq[i]), 'the instruction before it': P.name_of(seq[i - 1]),
                'replicates': row['viable'], 'tasks_credited': sorted(P.tasks_of(row)),
                'NOT_routes_in_trace': len(e['routes']) if e else 0,
                'NOT_credited_route': ({k: e['routes'][0][k] for k in ('output_site', 'exact', 'reduced', 'sites')}
                                       if e and e['routes'] else None),
                'replay_mismatches': x['mismatches']}
    finally:
        shutil.rmtree(d)
    # the unablated trace's first NOT route, for comparison
    t0 = trace_record(run, {seq})[seq]
    out['unablated_NOT_credited_route'] = {k: t0['sums']['NOT']['routes'][0][k] for k in ('output_site', 'exact', 'sites')}
    return out


def pairs_with_replication_sites(args):
    seq, sums, sites = args
    Rq = [i for i, c in enumerate(sites) if not (c & 1)]
    prs = sorted({tuple(sorted(p)) for p in itertools.product(Rq, range(len(seq))) if p[0] != p[1]})
    rows = P.evaluate([M.knock(seq, p) for p in prs])
    res = {t: [] for t in sums}
    replicating = 0
    for p, row in zip(prs, rows):
        c = M.code(row)
        replicating += c & 1
        for t in sums:
            if M.stops(c, t):
                res[t].append(list(p))
    return seq, len(Rq), len(prs), replicating, res


def xb(jobs):
    out = {}
    targets = []           # (run, seq, task, kind)
    irr_sizes = []
    for run in P.RUN_NAMES:
        for r in jl('%s/%s.irreducible.jsonl' % (REM, run)):
            targets.append((run, r['seq'], r['sum'], 'stopped by 3 or more' if r['sets'] else 'not stopped'))
            if r['sets']:
                irr_sizes.append({'run': run, 'task': r['sum'], 'start': r['start_kind'],
                                  'set_sizes': sorted(len(s) for s in r['sets'])})
    out['Xb3_irreducible_sets_found'] = irr_sizes
    singles, traces = {}, {}
    for run in {t[0] for t in targets}:
        seqs = {t[1] for t in targets if t[0] == run}
        for r in jl('%s/%s.singles.jsonl' % (REM, run)):
            if r['seq'] in seqs:
                singles[r['seq']] = r
        traces.update(trace_record(run, seqs))
    # Xb2
    per = []
    for run, seq, t, kind in targets:
        if kind != 'not stopped':
            continue
        s, e = singles[seq], traces[seq]['sums'][t]
        rs = {int(i) for ro in e['routes'] for i in ro['sites']}
        rq = [i for i in rs if not (s['sites'][i] & 1)]
        per.append({'run': run, 'task': t, 'programs': s['organisms'], 'routes': len(e['routes']),
                    'route_sites': len(rs), 'route_sites_replication_required': len(rq),
                    'every_route_has_a_replication_required_site':
                        all(any(not (s['sites'][int(i)] & 1) for i in ro['sites']) for ro in e['routes']),
                    'replication_required_route_instructions': sorted({P.name_of(seq[i]) for i in rq})})
    out['Xb2_not_stopped'] = {
        'sequence_task_pairs': len(per), 'programs': sum(p['programs'] for p in per),
        'runs': dict(collections.Counter(p['run'] for p in per)),
        'every_route_holds_a_replication_required_site': sum(p['every_route_has_a_replication_required_site'] for p in per),
        'share_of_route_sites_replication_required': round(sum(p['route_sites_replication_required'] for p in per) /
                                                           sum(p['route_sites'] for p in per), 3),
        'replication_required_route_instructions': dict(collections.Counter(
            k for p in per for k in p['replication_required_route_instructions']))}
    # Xb1 (i): the sent search's two start sets, run again: does the program still replicate?
    start = []
    for run, seq, t, kind in targets:
        s = singles[seq]
        V = sorted(i for i, c in enumerate(s['sites']) if c & 1)
        rs = sorted({int(i) for ro in traces[seq]['sums'][t]['routes'] for i in ro['sites']} & set(V))
        start.append((M.knock(seq, rs), M.knock(seq, V)))
    rows = P.evaluate([a for a, b in start] + [b for a, b in start])
    n = len(start)
    c1 = collections.Counter()
    for k, (run, seq, t, kind) in enumerate(targets):
        a, b = M.code(rows[k]), M.code(rows[n + k])
        c1[(kind, 'route start set: ' + ('replicates, task %s' % ('stopped' if M.stops(a, t) else 'still performed')
                                          if a & 1 else 'fails replication'),
            'all copying-safe sites: ' + ('replicates, task %s' % ('stopped' if M.stops(b, t) else 'still performed')
                                          if b & 1 else 'fails replication'))] += 1
    out['Xb1_start_sets'] = {' | '.join(k): v for k, v in sorted(c1.items())}
    # Xb1 (ii): every pair with at least one replication-required site, in each distinct sequence of the 91
    by_seq = collections.defaultdict(set)
    for run, seq, t, kind in targets:
        by_seq[seq].add(t)
    work = [(seq, sorted(ts), singles[seq]['sites']) for seq, ts in by_seq.items()]
    found = collections.Counter()
    tested = replicating = 0
    examples = []
    per_target = []
    with ProcessPoolExecutor(jobs) as ex:
        for seq, nrq, npairs, nrep, res in ex.map(pairs_with_replication_sites, work):
            tested += npairs
            replicating += nrep
            for t, ps in res.items():
                kind = [k for r_, s_, t_, k in targets if s_ == seq and t_ == t][0]
                found[(kind, 'a pair with a replication-required site stops it' if ps else 'no such pair stops it')] += 1
                run = [r_ for r_, s_, t_, k in targets if s_ == seq and t_ == t][0]
                per_target.append({'run': run, 'seq': seq, 'task': t, 'kind': kind, 'programs': singles[seq]['organisms'],
                                   'minimal_pairs_with_a_replication_required_site': ps})
                if ps and len(examples) < 10:
                    examples.append({'task': t, 'pairs': len(ps), 'first': [(i, P.name_of(seq[i])) for i in ps[0]]})
    out['Xb1_pairs_with_a_replication_required_site'] = {
        'distinct_sequences': len(work), 'pairs_tested': tested, 'pairs_leaving_replication': replicating,
        'sequence_task_pairs': {' | '.join(k): v for k, v in sorted(found.items())}, 'examples': examples,
        'by_task': {t: dict(collections.Counter('%s: %s' % (x['kind'], 'stopped by such a pair' if
                                                              x['minimal_pairs_with_a_replication_required_site']
                                                              else 'not stopped by such a pair')
                                                for x in per_target if x['task'] == t))
                    for t in sorted({x['task'] for x in per_target})},
        'by_task_programs': {t: dict(sum((collections.Counter({'%s: %s' % (x['kind'], 'stopped by such a pair' if
                                                                  x['minimal_pairs_with_a_replication_required_site']
                                                                  else 'not stopped by such a pair'): x['programs']})
                                          for x in per_target if x['task'] == t), collections.Counter()))
                             for t in sorted({x['task'] for x in per_target})}}
    with open(os.path.join(OUTDIR, 'Xb1_pairs_per_sequence_and_task.json'), 'w') as f:
        json.dump(per_target, f)
    return out


def xb4():
    c = collections.Counter()
    for run in P.RUN_NAMES:
        w = json.load(open('%s/%s.without_copying.json' % (REM, run)))
        for x in w['copying_sites']:
            c[('splits in the trace' if x['divided'] else 'does not split in the trace',
               'credited with some task' if x['sums_credited_by_test_processor'] else 'credited with none')] += 1
    return {' | '.join(k): v for k, v in sorted(c.items())}


def main():
    jobs = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    os.makedirs(OUTDIR, exist_ok=True)
    out = {'Xa2_NOT_example_sites_15_and_17': xa2(), 'Xb4_replication_required_sites_traced': xb4()}
    out.update(xb(jobs))
    with open(os.path.join(OUTDIR, 'settling_checks.json'), 'w') as f:
        json.dump(out, f, indent=1)
    print(json.dumps(out, indent=1))


if __name__ == '__main__':
    main()
