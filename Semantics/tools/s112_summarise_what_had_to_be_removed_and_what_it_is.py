#!/usr/bin/env python3
"""s112_summarise_what_had_to_be_removed_and_what_it_is.py

What it does, in plain words: for log S112, reads the raw output of the other S112 scripts (kept in the scratch space)
and writes the compact summary that goes into the repository:
  results/S112 What the evolved sums are - what had to be removed and what it is.json
It reads, for every distinct instruction sequence alive at update 50,000 in the nine S111 runs:
  - the instruction ablations (s112/removals/: every single site; every pair; the irreducible-set search; the triples of
    the most common sequence of each run; the traces of that sequence with each replication-required site removed),
  - Avida's own trace, as read by the trace reader (s112/traces/: the routes of each logic task from input read to
    output written, and each route's circuit),
  - the Avida execution-environment tests (s112/environment/).
and counts, per logic task (NOT, NAND, AND, ORN, OR, ANDN, NOR, XOR, EQU): the Avida programs and distinct instruction
sequences performing it; the size of the smallest instruction ablation that stops it; the kinds and roles of the
required instructions; the distinct circuits, how many sequences realise each, and one worked example traced by Avida;
what the environment tests changed; and what is left over. It runs no Avida program itself except, for the worked
examples, one Avida TRACE per example (through the trace reader's explain_route), inside Avida's virtual CPU.

  python3 -B Semantics/tools/s112_summarise_what_had_to_be_removed_and_what_it_is.py

Written 30 September 2026 by the one Opus 5.5 agent of log S112, in the owner's Avida terms (decision S61).
"""
import collections, itertools, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import s112_run_programs_in_avidas_test_processor as P  # noqa: E402
import s112_read_what_the_programs_compute_from_avidas_traces as R  # noqa: E402

S = P.SCRATCH + '/s112'
OUTFILE = os.path.join(os.path.dirname(HERE), 'results', 'S112 What the evolved sums are - what had to be removed and '
                       'what it is.json')
TASKS = P.TASKS
DUAL = {'NOT': 'NOT', 'NAND': 'NOR', 'NOR': 'NAND', 'AND': 'OR', 'OR': 'AND', 'ORN': 'ANDN', 'ANDN': 'ORN',
        'XOR': 'EQU', 'EQU': 'XOR'}
SMALLEST_NAND = {'NOT': 1, 'NAND': 1, 'AND': 2, 'ORN': 2, 'OR': 3, 'ANDN': 3, 'NOR': 4, 'XOR': 4, 'EQU': 5}
ROLE_ORDER = ['output write', 'input read', 'gate', 'arithmetic', 'mover', 'register choice', 'constant-making']


def sums_in(c):
    return [TASKS[k] for k in range(9) if (c >> 1) & (1 << k)]


def stops(c, t):
    return (c & 1) == 1 and not ((c >> 1) & (1 << TASKS.index(t)))


def jl(path):
    return [json.loads(x) for x in open(path)] if os.path.exists(path) else []


def main_role(roles):
    for r in ROLE_ORDER:
        for x in roles:
            if x == r or x.startswith(r):
                return r
    return None


def site_role(site, T, trace):
    """the role of a site for task T: its role in T's routes, if any; else what it was executed as"""
    e = trace['sums'].get(T)
    roles = set()
    if e:
        for ro in e['routes']:
            roles |= set(ro['sites'].get(str(site), []))
    r = main_role(roles)
    if r:
        return r
    ex = trace['executed'].get(str(site))
    if not ex:
        return 'not executed'
    ex = set(ex)
    if any(x.startswith('label of') for x in ex):
        return 'label read by a control instruction'
    if any(x.startswith('modifier of') for x in ex):
        return 'register or head choice of an instruction outside the routes'
    names = {x for x in ex if not x.startswith(('label of', 'modifier of'))}
    if names & R.CONTROL:
        return 'control (jumps, heads, conditions, labels)'
    if names & R.COPYING:
        return 'replication instruction'
    return 'other executed instruction outside the routes'


def pct(a, b):
    return round(100.0 * a / b, 2) if b else None


def main():
    runs = P.RUN_NAMES
    data = {}
    for run in runs:
        singles = {r['seq']: r for r in jl('%s/removals/%s.singles.jsonl' % (S, run))}
        pairs = {r['seq']: r for r in jl('%s/removals/%s.pairs.jsonl' % (S, run))}
        irr = collections.defaultdict(dict)
        for r in jl('%s/removals/%s.irreducible.jsonl' % (S, run)):
            irr[r['seq']][r['sum']] = r
        traces = {r['seq']: r for r in jl('%s/traces/%s.jsonl' % (S, run))}
        env = {r['seq']: r for r in jl('%s/environment/%s.jsonl' % (S, run))}
        data[run] = (singles, pairs, irr, traces, env)

    world = {}
    for run in runs:
        last = [l for l in open('%s/../s111/runs/%s/data/tasks.dat' % (S, run)) if l.strip() and not l.startswith('#')][-1]
        w = last.split()
        world[run] = {T: int(w[1 + k]) for k, T in enumerate(TASKS)}
    total_programs = sum(r['organisms'] for run in runs for r in data[run][0].values())
    total_seqs = sum(len(data[run][0]) for run in runs)

    out = {'what': 'log S112: per logic task, what instruction ablation had to remove for the task performance to stop, '
                   'and the circuit of instructions the Avida programs execute; counts over every distinct instruction '
                   'sequence alive at update 50,000 in the nine S111 runs',
           'programs_total': total_programs, 'sequences_total': total_seqs, 'tasks': {}, 'leftover': {},
           'environment': {}, 'triples': {}, 'without_replication': {}}

    # overall checks of the trace reading
    mm = sum(1 for run in runs for t in data[run][3].values() if t['mismatches'])
    mm_steps = sum(t['mismatches'] for run in runs for t in data[run][3].values())
    tp_vs_trace = collections.Counter()
    for run in runs:
        singles, pairs, irr, traces, env = data[run]
        for seq, s in singles.items():
            t = traces.get(seq)
            if t is None:
                tp_vs_trace['no trace'] += 1
                continue
            a = set(sums_in(s['base'])) if s['base'] & 1 else set()
            b = set(t['tasks_in_trace'])
            if s['base'] & 1:
                tp_vs_trace['replicating: same tasks' if a == b else 'replicating: tasks differ'] += 1
            else:
                tp_vs_trace['fails replication in the test processor'] += 1
    out['leftover']['trace_reading'] = {'sequences_with_any_step_where_replay_differs_from_trace': mm,
                                        'steps_where_replay_differs_from_trace': mm_steps,
                                        'test_processor_tasks_vs_trace_tasks': dict(tp_vs_trace)}

    examples_wanted = {}
    for T in TASKS:
        doers = []          # (run, seq, organisms)
        for run in runs:
            for seq, s in data[run][0].items():
                if (s['base'] & 1) and T in sums_in(s['base']):
                    doers.append((run, seq, s['organisms']))
        n_seq, n_prog = len(doers), sum(x[2] for x in doers)
        entry = {'sequences': n_seq, 'programs': n_prog, 'share_of_all_programs_pct': pct(n_prog, total_programs),
                 'world_count_at_update_50000': sum(world[r][T] for r in runs),
                 'runs_with_doers': sorted({x[0] for x in doers}, key=runs.index)}
        if not doers:
            out['tasks'][T] = entry
            continue
        size = collections.Counter()
        size_w = collections.Counter()
        kinds1, roles1 = collections.Counter(), collections.Counter()
        roles1_w = collections.Counter()
        n_required = []
        cut_all_routes = collections.Counter()
        pair_roles = collections.Counter()
        irr_kind = collections.Counter()
        redundancy = collections.Counter()
        circ, circ_red, circ_any = {}, {}, collections.Counter()
        credited_agree = collections.Counter()
        generality = collections.Counter()
        for run, seq, n in doers:
            singles, pairs, irr, traces, env = data[run]
            s, tr = singles[seq], traces.get(seq)
            one = [i for i, c in enumerate(s['sites']) if stops(c, T)]
            mp = pairs.get(seq, {}).get('minimal_pairs', {}).get(T, [])
            ir = irr.get(seq, {}).get(T)
            if one:
                k = '1'
            elif mp:
                k = '2'
            elif ir and ir['sets']:
                k = '3 or more (irreducible-set search)'
                irr_kind[ir['start_kind']] += 1
            else:
                k = 'none found'
                if ir:
                    irr_kind['not stopped: ' + str(ir['start_kind'])] += 1
            size[k] += 1
            size_w[k] += n
            n_required.append(len(one))
            if tr is None:
                continue
            e = tr['sums'].get(T)
            nroutes = len(e['routes']) if e else 0
            redundancy[(k == '1', 'one route' if nroutes == 1 else ('no route' if nroutes == 0 else 'more routes'))] += 1
            for i in one:
                kinds1[P.name_of(s['seq'][i])] += 1
                r = site_role(i, T, tr)
                roles1[r] += 1
                roles1_w[r] += n
            if e:
                rsets = [set(int(x) for x in ro['sites']) for ro in e['routes']]
                for i in one:
                    cut_all_routes['single site in every route' if all(i in rs for rs in rsets) else
                                   'single site not in every route'] += 1
                for p in mp:
                    cut_all_routes['pair cuts every route' if all(set(p) & rs for rs in rsets) else
                                   'pair does not cut every route'] += 1
                    pair_roles[tuple(sorted(site_role(i, T, tr) for i in p))] += 1
                ro = e['routes'][0]
                credited_agree[bool(e['agree'])] += 1
                generality[ro['generality']] += 1
                for key, store in (('canonical', circ), ('reduced', circ_red)):
                    c = store.setdefault(ro[key], {'sequences': 0, 'programs': 0, 'runs': set(), 'route_letters': set(),
                                                   'gates': ro['gates' if key == 'canonical' else 'reduced_gates'],
                                                   'nested': ro['nested' if key == 'canonical' else 'reduced_nested'],
                                                   'example': (n, run, seq)})
                    c['sequences'] += 1
                    c['programs'] += n
                    c['runs'].add(run)
                    c['route_letters'].add(ro['letters'])
                    if n > c['example'][0]:
                        c['example'] = (n, run, seq)
                for ro2 in e['routes']:
                    circ_any[ro2['reduced']] += 1
        def table(store):
            rows = []
            for form, c in sorted(store.items(), key=lambda kv: -kv[1]['programs']):
                ops = set(x.split('(')[0].split('=')[-1] for x in form.split('; '))
                rows.append({'circuit': form, 'nested': c['nested'], 'parts': c['gates'],
                             'nand_only': ops <= {'nand'} or form.startswith('out='),
                             'sequences': c['sequences'], 'programs': c['programs'], 'runs': len(c['runs']),
                             'distinct_route_instruction_strings': len(c['route_letters']),
                             'example': {'run': c['example'][1], 'sequence': c['example'][2],
                                         'programs': c['example'][0]}})
            return rows
        full, red = table(circ), table(circ_red)
        entry.update({
            'smallest_ablation_stopping_it': {'by_sequence': dict(size), 'by_program': dict(size_w)},
            'irreducible_search_start': dict(irr_kind),
            'required_instructions_per_sequence': {'mean': round(sum(n_required) / len(n_required), 2),
                                                   'min': min(n_required), 'max': max(n_required)},
            'required_instruction_kinds': dict(kinds1.most_common()),
            'required_instruction_roles': dict(roles1.most_common()),
            'required_instruction_roles_weighted_by_programs': dict(roles1_w.most_common()),
            'ablation_against_routes': dict(cut_all_routes),
            'minimal_pair_roles': {' + '.join(k): v for k, v in pair_roles.most_common(12)},
            'single_site_stops_it_vs_number_of_routes': {'%s, %s' % ('a single site stops it' if a else
                                                                     'no single site stops it', b): v
                                                         for (a, b), v in sorted(redundancy.items())},
            'credited_output_is_first_accepted_output': {str(k): v for k, v in credited_agree.items()},
            'generality_of_credited_circuit': {str(k): v for k, v in sorted(generality.items())},
            'distinct_circuits': len(full), 'distinct_reduced_circuits': len(red),
            'distinct_reduced_circuits_over_all_routes': len(circ_any),
            'smallest_nand_circuit_possible': SMALLEST_NAND[T],
            'smallest_reduced_circuit_found': min(r['parts'] for r in red),
            'smallest_nand_only_circuit_found': min([r['parts'] for r in red if r['nand_only']] or [None],
                                                    key=lambda x: 99 if x is None else x),
            'reduced_circuits_top': red[:12], 'circuits_top': full[:5],
        })
        examples_wanted[T] = red[0]['example']
        out['tasks'][T] = entry

    # environment tests
    variants = None
    for run in runs:
        for r in data[run][4].values():
            variants = list(r['variants'])
            break
        if variants:
            break
    env_out = {}
    for v in variants or []:
        per = {}
        for T in TASKS:
            n = keep = viable = dual = pred_ok = pred_n = 0
            for run in runs:
                singles, pairs, irr, traces, env = data[run]
                for seq, r in env.items():
                    if T not in r['variants']['unchanged']['sums']:
                        continue
                    n += 1
                    x = r['variants'][v]
                    viable += x['viable']
                    keep += T in x['sums']
                    dual += DUAL[T] in x['sums']
                    tr = traces.get(seq)
                    if tr and v in tr['predicted'] and x['viable']:
                        pred_n += 1
                        pred_ok += (T in tr['predicted'][v]) == (T in x['sums'])
            per[T] = {'doers': n, 'still_replicating': viable, 'still_doing_it': keep, 'doing_its_dual': dual,
                      'prediction_checked_on': pred_n, 'prediction_right': pred_ok}
        env_out[v] = per
    out['environment'] = env_out

    # triples and replication-required sites of the most common sequences
    for run in runs:
        p = '%s/removals/%s.triples.json' % (S, run)
        if os.path.exists(p):
            t = json.load(open(p))
            out['triples'][run] = {'sequence': t['seq'], 'programs': t['organisms'], 'triples_tested': t['triples_tested'],
                                   'minimal_triples': {k: len(v) for k, v in t['minimal_triples'].items()}}
        p = '%s/removals/%s.without_copying.json' % (S, run)
        if os.path.exists(p):
            w = json.load(open(p))
            c = collections.Counter()
            for x in w['copying_sites']:
                c['tasks still performed in the trace: %s' % ('all' if set(w['sums']) <= set(x['sums_written_in_trace'])
                                                             else ('some' if x['sums_written_in_trace'] else 'none'))] += 1
            out['without_replication'][run] = {'sequence': w['seq'], 'replication_required_sites': len(w['copying_sites']),
                                               'counts': dict(c)}

    # left over: executed sites that are neither in a route nor required for replication
    lo = collections.Counter()
    for run in runs:
        singles, pairs, irr, traces, env = data[run]
        for seq, s in singles.items():
            tr = traces.get(seq)
            if tr is None or not (s['base'] & 1) or not sums_in(s['base']):
                continue
            route = set()
            for e in tr['sums'].values():
                for ro in e['routes']:
                    route |= {int(x) for x in ro['sites']}
            repl = {i for i, c in enumerate(s['sites']) if not (c & 1)}
            ex = {int(x) for x in tr['executed']}
            L = len(seq)
            for i in range(L):
                if i in route and i in repl:
                    lo['in a route and required for replication'] += 1
                elif i in route:
                    lo['in a route only'] += 1
                elif i in repl:
                    lo['required for replication only'] += 1
                elif i in ex:
                    lo['executed, in no route, not required for replication'] += 1
                else:
                    lo['never executed'] += 1
    out['leftover']['sites_of_task_performing_sequences'] = dict(lo)

    # worked examples: the most common reduced circuit of each task, in its most common sequence, traced by Avida
    ex = {}
    for T, (n, run, seq) in examples_wanted.items():
        singles, pairs, irr, traces, env = data[run]
        s, tr = singles[seq], traces[seq]
        e = R.explain_route(seq, T)
        one = [i for i, c in enumerate(s['sites']) if stops(c, T)]
        mp = pairs.get(seq, {}).get('minimal_pairs', {}).get(T, [])
        e.update({'run': run, 'programs': n,
                  'required_instructions': [{'site': i, 'instruction': P.name_of(seq[i]),
                                             'role': site_role(i, T, tr)} for i in one],
                  'minimal_pairs': [[{'site': i, 'instruction': P.name_of(seq[i]), 'role': site_role(i, T, tr)}
                                     for i in p] for p in mp[:6]],
                  'minimal_pairs_total': len(mp),
                  'replication_required_sites': [i for i, c in enumerate(s['sites']) if not (c & 1)],
                  'credited_route': {k: tr['sums'][T]['routes'][0][k] for k in
                                     ('reduced', 'reduced_nested', 'reduced_part_ids', 'exact', 'letters', 'sites')},
                  'routes': len(tr['sums'][T]['routes'])})
        ex[T] = e
    out['worked_examples'] = ex
    with open(OUTFILE, 'w') as f:
        json.dump(out, f, indent=1, default=list)
    print('written', OUTFILE, os.path.getsize(OUTFILE), 'bytes')


if __name__ == '__main__':
    main()
