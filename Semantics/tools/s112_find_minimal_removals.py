#!/usr/bin/env python3
"""s112_find_minimal_removals.py

What it does, in plain words: for log S112, finds what had to be removed from each evolved program for it to stop doing
each of its logic sums. "Removing" an instruction means replacing it by nop-X, an instruction that does nothing (as in
S111). A removal "stops a sum" if, afterwards, the program still makes an exact copy of itself in Avida's test processor
and no longer does the sum (a removal that stops the copying stops every sum there, and is counted separately as part of
the copying). A "minimal removal set" stops the sum while no smaller part of it does. Every program is run by Avida's own
test processor (analysis mode, RECALCULATE); this script only chooses which sites to remove and reads the answers.

Stages (each writes JSON lines into the scratch space, s112/removals/; nothing into the repository):
  singles      every single site of every living genotype of the nine S111 runs at update 50,000 (exhaustive)
  pairs        every pair of sites among those whose single removal leaves the program copying (exhaustive to size 2);
               a pair is kept for a sum if it stops the sum and neither of its sites does alone
  irreducible  for each program and sum not stopped by any set of 1 or 2 sites: start from the sites of the sum's routes
               in Avida's trace (every output the sum's check accepts, and the instructions that made it, as read by
               s112_read_what_the_programs_compute_from_avidas_traces.py), restricted to sites whose single removal leaves
               copying; if removing the start set stops the sum, put sites back one at a time in 5 random orders
               (seeded), keeping each back if the sum stays stopped, and repeat whole passes until a pass puts nothing
               back; each order ends in a set from which no single site can be put back. If the start set does not stop
               the sum, start from all sites whose single removal leaves copying. Chains of many programs are run side
               by side, one Avida call per round.
  triples      for the most common genotype of each run: every triple of such sites (to see what the irreducible search
               misses at size 3)
  without_copying  for the most common genotype of each run: each site whose removal stops the copying, traced by
               Avida: are the sums' outputs still written during the run, although nothing is credited?

  python3 -B Semantics/tools/s112_find_minimal_removals.py singles|pairs|irreducible|triples|without_copying [jobs]

Written 30 September 2026 by the one Opus 5.5 agent of log S112.
"""
import itertools, json, os, random, sys
from concurrent.futures import ProcessPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import s112_run_programs_in_avidas_test_processor as P  # noqa: E402

OUT = P.SCRATCH + '/s112/removals'
TRACES = P.SCRATCH + '/s112/traces'
ORDERS = 5


def knock(seq, sites):
    s = list(seq)
    for i in sites:
        s[i] = P.NULL
    return ''.join(s)


def code(row):
    """viable bit + 2 * (bit mask of the sums done)"""
    return row['viable'] + 2 * sum(1 << k for k in range(9) if row['task.%d' % k] > 0)


def sums_in(c):
    return [P.TASKS[k] for k in range(9) if (c >> 1) & (1 << k)]


def stops(c, t):
    """the removal leaves the program copying and the sum t not done"""
    return (c & 1) == 1 and not ((c >> 1) & (1 << P.TASKS.index(t)))


# ---------------------------------------------------------------- singles
def singles_work(args):
    run, items = args
    seqs = [s for s, _ in items]
    base = P.evaluate(seqs)
    flat = [knock(s, [i]) for s in seqs for i in range(len(s))]
    kos = P.evaluate(flat)
    out, k = [], 0
    for (s, n), b in zip(items, base):
        rows = kos[k:k + len(s)]
        k += len(s)
        out.append({'run': run, 'seq': s, 'organisms': n, 'base': code(b), 'sites': [code(r) for r in rows]})
    return out


def run_singles(jobs):
    os.makedirs(OUT, exist_ok=True)
    for run in P.RUN_NAMES:
        target = os.path.join(OUT, run + '.singles.jsonl')
        if os.path.exists(target):
            continue
        pop = P.living(run)
        batches = [(run, pop[i:i + 200]) for i in range(0, len(pop), 200)]
        with open(target + '.part', 'w') as f, ProcessPoolExecutor(jobs) as ex:
            for res in ex.map(singles_work, batches):
                for r in res:
                    f.write(json.dumps(r) + '\n')
        os.rename(target + '.part', target)
        print(run, 'singles done', len(pop), flush=True)


def load(run, stage):
    return [json.loads(x) for x in open(os.path.join(OUT, '%s.%s.jsonl' % (run, stage)))]


# ---------------------------------------------------------------- pairs
def pairs_work(recs):
    out, seqs, index = [], [], []
    for r in recs:
        V = [i for i, c in enumerate(r['sites']) if c & 1]
        prs = list(itertools.combinations(V, 2))
        index.append((r, V, prs, len(seqs)))
        seqs += [knock(r['seq'], p) for p in prs]
    rows = P.evaluate(seqs) if seqs else []
    for r, V, prs, start in index:
        base_sums = sums_in(r['base'])
        mp = {t: [] for t in base_sums}
        for p, row in zip(prs, rows[start:start + len(prs)]):
            c = code(row)
            for t in base_sums:
                if stops(c, t) and not stops(r['sites'][p[0]], t) and not stops(r['sites'][p[1]], t):
                    mp[t].append(list(p))
        out.append({'seq': r['seq'], 'viable_single_sites': len(V), 'pairs_tested': len(prs), 'minimal_pairs': mp})
    return out


def run_pairs(jobs):
    for run in P.RUN_NAMES:
        target = os.path.join(OUT, run + '.pairs.jsonl')
        if os.path.exists(target):
            continue
        recs = [r for r in load(run, 'singles') if (r['base'] & 1) and (r['base'] >> 1)]
        batches = [recs[i:i + 6] for i in range(0, len(recs), 6)]
        with open(target + '.part', 'w') as f, ProcessPoolExecutor(jobs) as ex:
            for res in ex.map(pairs_work, batches, chunksize=4):
                for r in res:
                    f.write(json.dumps(r) + '\n')
        os.rename(target + '.part', target)
        print(run, 'pairs done', len(recs), flush=True)


# ---------------------------------------------------------------- irreducible
def route_sites(trace_rec, t):
    e = trace_rec['sums'].get(t)
    if not e:
        return set()
    return {int(i) for ro in e['routes'] for i in ro['sites']}


def irreducible_run(run):
    singles = {r['seq']: r for r in load(run, 'singles')}
    pairs = {r['seq']: r for r in load(run, 'pairs')}
    traces = {}
    for line in open(os.path.join(TRACES, run + '.jsonl')):
        r = json.loads(line)
        traces[r['seq']] = r
    chains = []          # each: dict(seq, t, order, current, queue, changed, start_kind)
    todo = []
    for seq, r in singles.items():
        if not ((r['base'] & 1) and (r['base'] >> 1)):
            continue
        for t in sums_in(r['base']):
            if any(stops(c, t) for c in r['sites']) or pairs[seq]['minimal_pairs'].get(t):
                continue
            V = {i for i, c in enumerate(r['sites']) if c & 1}
            todo.append((seq, t, sorted(route_sites(traces[seq], t) & V), sorted(V)))
    # test the start sets
    starts = P.evaluate([knock(seq, rs) for seq, t, rs, V in todo]) if todo else []
    alt = [k for k, (row, (seq, t, rs, V)) in enumerate(zip(starts, todo)) if not stops(code(row), t)]
    starts2 = P.evaluate([knock(todo[k][0], todo[k][3]) for k in alt]) if alt else []
    kind = {}
    for k in range(len(todo)):
        kind[k] = 'routes'
    for k, row in zip(alt, starts2):
        kind[k] = 'all copying-safe sites' if stops(code(row), todo[k][1]) else None
    rng = random.Random(1120)
    results = {}
    for k, (seq, t, rs, V) in enumerate(todo):
        results[k] = {'seq': seq, 'sum': t, 'start_kind': kind[k], 'route_sites': len(rs), 'sets': []}
        if kind[k] is None:
            continue
        start = rs if kind[k] == 'routes' else V
        for o in range(ORDERS):
            order = list(start)
            rng.shuffle(order)
            chains.append({'k': k, 'seq': seq, 't': t, 'current': set(start), 'order': order, 'pos': 0,
                           'changed': False, 'done': False})
    rounds = 0
    while True:
        live = [c for c in chains if not c['done']]
        if not live:
            break
        rounds += 1
        trials = []
        for c in live:
            site = c['order'][c['pos']]
            trials.append((c, site, knock(c['seq'], sorted(c['current'] - {site}))))
        rows = P.evaluate([x[2] for x in trials])
        for (c, site, _), row in zip(trials, rows):
            if stops(code(row), c['t']):
                c['current'].discard(site)
                c['changed'] = True
            c['pos'] += 1
            if c['pos'] >= len(c['order']):
                if c['changed']:
                    c['order'] = [s for s in c['order'] if s in c['current']]
                    c['pos'], c['changed'] = 0, False
                    if not c['order']:
                        c['done'] = True
                else:
                    c['done'] = True
    for c in chains:
        s = sorted(c['current'])
        if s not in results[c['k']]['sets']:
            results[c['k']]['sets'].append(s)
    with open(os.path.join(OUT, run + '.irreducible.jsonl'), 'w') as f:
        for k in sorted(results):
            f.write(json.dumps(results[k]) + '\n')
    return run, len(todo), rounds


def run_irreducible(jobs):
    runs = [r for r in P.RUN_NAMES if not os.path.exists(os.path.join(OUT, r + '.irreducible.jsonl'))]
    with ProcessPoolExecutor(jobs) as ex:
        for run, n, rounds in ex.map(irreducible_run, runs):
            print(run, 'irreducible done', n, 'program-sum pairs', rounds, 'rounds', flush=True)


# ---------------------------------------------------------------- triples
def triples_run(run):
    singles = load(run, 'singles')
    pairs = {r['seq']: r for r in load(run, 'pairs')}
    r = singles[0]                          # the most common genotype (living() sorts by organisms)
    seq = r['seq']
    V = [i for i, c in enumerate(r['sites']) if c & 1]
    base_sums = sums_in(r['base'])
    pair_sets = {t: {tuple(p) for p in pairs[seq]['minimal_pairs'].get(t, [])} for t in base_sums}
    trip = list(itertools.combinations(V, 3))
    rows = P.evaluate([knock(seq, x) for x in trip])
    mt = {t: [] for t in base_sums}
    for x, row in zip(trip, rows):
        c = code(row)
        for t in base_sums:
            if not stops(c, t) or any(stops(r['sites'][i], t) for i in x):
                continue
            if any(p in pair_sets[t] for p in itertools.combinations(x, 2)):
                continue
            mt[t].append(list(x))
    rec = {'run': run, 'seq': seq, 'organisms': r['organisms'], 'triples_tested': len(trip), 'minimal_triples': mt}
    with open(os.path.join(OUT, run + '.triples.json'), 'w') as f:
        json.dump(rec, f)
    return run, len(trip), {t: len(v) for t, v in mt.items()}


def run_triples(jobs):
    runs = [r for r in P.RUN_NAMES if not os.path.exists(os.path.join(OUT, r + '.triples.json'))]
    with ProcessPoolExecutor(jobs) as ex:
        for res in ex.map(triples_run, runs):
            print(*res, flush=True)


# ---------------------------------------------------------------- without_copying
def without_copying_run(run):
    """For the most common genotype: each site whose single removal stops the copying; Avida's trace of the program
    with that site removed, read by the trace reader: are the sums' outputs still written during the run?"""
    import shutil
    import s112_read_what_the_programs_compute_from_avidas_traces as R
    r = load(run, 'singles')[0]
    seq = r['seq']
    base_sums = sums_in(r['base'])
    ess = [i for i, c in enumerate(r['sites']) if not (c & 1)]
    progs = [knock(seq, [i]) for i in ess]
    d, paths = P.trace(progs)
    out = []
    try:
        for i, prog, p in zip(ess, progs, paths):
            x = R.read_program(prog, p)
            out.append({'site': i, 'instruction': P.name_of(seq[i]), 'divided': x['divided'],
                        'sums_written_in_trace': x['tasks_in_trace'],
                        'sums_credited_by_test_processor': sums_in(r['sites'][i])})
    finally:
        shutil.rmtree(d)
    rec = {'run': run, 'seq': seq, 'sums': base_sums, 'copying_sites': out}
    with open(os.path.join(OUT, run + '.without_copying.json'), 'w') as f:
        json.dump(rec, f)
    return run, len(ess)


def run_without_copying(jobs):
    with ProcessPoolExecutor(jobs) as ex:
        for res in ex.map(without_copying_run, P.RUN_NAMES):
            print(*res, flush=True)


if __name__ == '__main__':
    stage, jobs = sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 3
    {'singles': run_singles, 'pairs': run_pairs, 'irreducible': run_irreducible, 'triples': run_triples,
     'without_copying': run_without_copying}[stage](jobs)
