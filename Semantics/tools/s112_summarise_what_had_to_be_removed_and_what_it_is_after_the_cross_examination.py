#!/usr/bin/env python3
"""s112_summarise_what_had_to_be_removed_and_what_it_is_after_the_cross_examination.py

A CORRECTED COPY of s112_summarise_what_had_to_be_removed_and_what_it_is.py (log S112), made 30 September 2026 by the
Opus 5.5 agent that settled the GLM cross-examination of S112 (results/S112 What the evolved sums are - the GLM
cross-examination, settled.md). The script as sent is kept unchanged beside it. It writes
  results/S112 What the evolved sums are - what had to be removed and what it is, after the cross-examination.json
Changes, each marked in the code with its objection id:
  Xc6, Xc3  the trace records of the sequences read again by the corrected reader
            (s112_read_what_the_programs_compute_from_avidas_traces_after_the_cross_examination.py, reread) replace the
            sent ones: nand(ONES,ONES) folded to ZERO; each route's reduced form also with its constants' values; and
            the distinct reduced circuits are also counted with the values of constants folded as OTHER kept apart;
  Xb1       the smallest removal set is also given after the settling rerun of every pair holding a site whose single
            ablation stops replication, for the 91 sequence-task pairs the sent search left at 3 or more or not stopped
            (s112x_settling_checks.py, s112x_settle/Xb1_pairs_per_sequence_and_task.json);
  Xb3       the number of minimal pairs per task, and the sizes of the irreducible sets found, are written out;
  Xa7       the kinds and roles of the required instructions are also given run by run;
  Xb4       the traced replication-required sites are also counted by whether the program split in the trace.
Everything else is as sent; the numbers it shares with the sent summary come out the same (checked by the settling).

The original description follows.

s112_summarise_what_had_to_be_removed_and_what_it_is.py

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
                       'what it is, after the cross-examination.json')
SETTLE = P.SCRATCH + '/s112x_settle'
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
    if 'IO' in names:
        return 'IO outside the routes (it takes the next number of the input rotation, so later reads get other numbers)'
    if 'swap-stk' in names:
        return 'stack switch outside the routes (decides which stack later push and pop use)'
    if names & {'push', 'pop', 'swap'}:
        return 'mover outside the routes'
    if names & {'nand', 'add', 'sub', 'inc', 'dec', 'shift-l', 'shift-r'}:
        return 'operation outside the routes'
    return 'other executed instruction outside the routes'


PATTERN = [0x0f0f0f0f, 0x33333333, 0x55555555]    # every byte holds all eight combinations of three bits


def truth_table(v):
    """the bit-by-bit function (8-bit truth table over x0, x1, x2) a 32-bit number computed from PATTERN is, or None"""
    tt = [-1] * 8
    for b in range(32):
        pos = sum(((PATTERN[i] >> b) & 1) << i for i in range(3))
        bit = (v >> b) & 1
        if tt[pos] not in (-1, bit):
            return None
        tt[pos] = bit
    return sum(tt[i] << i for i in range(8))


def permute_tt(tt, p):
    """the same truth table with the inputs renamed by p (x_i becomes x_p[i])"""
    out = 0
    for pos in range(8):
        bits = [(pos >> i) & 1 for i in range(3)]
        new = sum(bits[i] << p[i] for i in range(3))
        out |= ((tt >> pos) & 1) << new
    return out


def evaluate_circuit(form):
    """computes each part of a written circuit (g1=nand(x0,x1); ...) on PATTERN, as Avida's 32-bit registers would;
    returns the list of the parts' truth tables (None: not a bit-by-bit function) or None if a constant OTHER occurs"""
    if form.startswith('out='):
        return []
    val = {'x0': PATTERN[0], 'x1': PATTERN[1], 'x2': PATTERN[2], 'ZERO': 0, 'ONES': 0xffffffff}
    tts = []
    for part in form.split('; '):
        name, rhs = part.split('=', 1)
        op, args = rhs[:-1].split('(', 1)
        ks = args.split(',')
        if any(k not in val for k in ks):
            return None
        a = [val[k] for k in ks]
        v = {'nand': lambda: ~(a[0] & a[1]), 'add': lambda: a[0] + a[1], 'sub': lambda: a[0] - a[1],
             'inc': lambda: a[0] + 1, 'dec': lambda: a[0] - 1, 'shift-l': lambda: a[0] << 1,
             'shift-r': lambda: R.s32(a[0]) >> 1}[op]() & 0xffffffff
        val[name] = v
        tts.append(truth_table(v))
    return tts


def function_skeleton(form):
    """the distinct bit-by-bit functions the circuit's parts compute, as truth tables, with the inputs renamed to give
    the smallest list: what the circuit computes on the way, whatever instructions compute it"""
    tts = evaluate_circuit(form)
    if tts is None:
        return None
    best = None
    for p in R.PERMS:
        x = tuple(sorted({permute_tt(t, p) for t in tts if t is not None}))
        if best is None or x < best:
            best = x
    return best


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
        for r in jl('%s/traces_reread/%s.jsonl' % (SETTLE, run)):          # Xc6, Xc3: the sequences read again
            assert r['seq'] in traces
            traces[r['seq']] = r
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
    xb1 = collections.defaultdict(dict)                     # Xb1: the settling rerun, per (run, sequence) and task
    for x in json.load(open(SETTLE + '/Xb1_pairs_per_sequence_and_task.json')):
        xb1[(x['run'], x['seq'])][x['task']] = x['minimal_pairs_with_a_replication_required_site']
    for T in TASKS:
        doers = []          # (run, sequence, number of Avida programs with it)
        for run in runs:
            for seq, s in data[run][0].items():
                if (s['base'] & 1) and T in sums_in(s['base']):
                    doers.append((run, seq, s['organisms']))
        n_seq, n_prog = len(doers), sum(x[2] for x in doers)
        # Avida's test processor credits the tasks of a program's last split (GetLastTaskCount, cAnalyzeGenotype.cc
        # 590), and calls a program viable only if it forms a colony (its copy is exact, or leads back to it; cTestCPU.cc
        # 282-313). So a program that splits but does not replicate is still credited; one that never splits is not.
        # Those programs, and the replication-required sites of the replicating ones, are counted apart.
        nonrep = [(run, seq, s['organisms']) for run in runs for seq, s in data[run][0].items()
                  if not (s['base'] & 1) and T in sums_in(s['base'])]
        nonrep_single = sum(1 for run, seq, n in nonrep
                            if any(not ((c >> 1) & (1 << TASKS.index(T))) for c in data[run][0][seq]['sites']))
        repl_sites = collections.Counter()
        for run, seq, n in doers:
            for c in data[run][0][seq]['sites']:
                if not (c & 1):
                    repl_sites['task still credited (the ablated program still splits)' if (c >> 1) & (1 << TASKS.index(T))
                               else 'task no longer credited'] += 1
        entry = {'sequences': n_seq, 'programs': n_prog, 'share_of_all_programs_pct': pct(n_prog, total_programs),
                 'credited_with_it_but_not_replicating (splits, copy not exact)': {'sequences': len(nonrep), 'programs': sum(x[2] for x in nonrep),
                                                       'with_a_single_site_whose_ablation_stops_it': nonrep_single},
                 'replication_required_sites_of_performing_sequences': dict(repl_sites),
                 'world_count_at_update_50000': sum(world[r][T] for r in runs),
                 'runs_with_doers': sorted({x[0] for x in doers}, key=runs.index)}
        if not doers:
            out['tasks'][T] = entry
            continue
        size = collections.Counter()
        size_w = collections.Counter()
        size_after, size_after_w = collections.Counter(), collections.Counter()        # Xb1
        n_minimal_pairs = 0                                                              # Xb3
        irr_sizes = []                                                                   # Xb3
        kinds_run, roles_run = collections.defaultdict(collections.Counter), collections.defaultdict(collections.Counter)  # Xa7
        circ_red_values = collections.Counter()                                          # Xc3
        kinds1, roles1 = collections.Counter(), collections.Counter()
        roles1_w = collections.Counter()
        n_required = []
        cut_all_routes = collections.Counter()
        pair_roles = collections.Counter()
        irr_kind = collections.Counter()
        redundancy = collections.Counter()
        circ, circ_red, circ_any = {}, {}, collections.Counter()
        req_strings, req_names = collections.Counter(), collections.Counter()
        overlap = collections.Counter()
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
            n_minimal_pairs += len(mp)                                                   # Xb3
            if ir and ir['sets']:
                irr_sizes.append(sorted(len(x) for x in ir['sets']))
            ka = k                                                                       # Xb1
            if k == 'none found' and xb1.get((run, seq), {}).get(T):
                ka = '2 (a pair holding a site whose single ablation stops replication; settling rerun)'
            elif k == '3 or more (irreducible-set search)' and (run, seq) in xb1 and T in xb1[(run, seq)]:
                ka = '3 or more (irreducible-set search; no pair holding a replication-required site stops it)'
            elif k == 'none found' and (run, seq) in xb1 and T in xb1[(run, seq)]:
                ka = 'none found (not by any pair, nor by the irreducible-set search)'
            size_after[ka] += 1
            size_after_w[ka] += n
            n_required.append(len(one))
            if tr is None:
                continue
            e = tr['sums'].get(T)
            nroutes = len(e['routes']) if e else 0
            redundancy[(k == '1', 'one route' if nroutes == 1 else ('no route' if nroutes == 0 else 'more routes'))] += 1
            if one:
                req_strings[''.join(s['seq'][i] for i in one)] += 1
                req_names[' '.join(P.name_of(s['seq'][i]) for i in one)] += n
            for i in one:
                kinds1[P.name_of(s['seq'][i])] += 1
                r = site_role(i, T, tr)
                roles1[r] += 1
                roles1_w[r] += n
                kinds_run[run][P.name_of(s['seq'][i])] += 1                              # Xa7
                roles_run[run][r] += n                                                   # Xa7
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
                rs0 = {int(x) for x in ro['sites']}
                one_set = set(one)
                overlap['credited route sites'] += len(rs0)
                overlap['credited route sites that are required'] += len(rs0 & one_set)
                overlap['required sites'] += len(one_set)
                overlap['required sites in the credited route'] += len(one_set & rs0)
                overlap['required sites in some route of the task'] += len(one_set & set().union(*rsets))
                credited_agree[bool(e['agree'])] += 1
                generality[ro['generality']] += 1
                circ_red_values[ro.get('reduced_values', ro['reduced'])] += 1             # Xc3
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
                tts = evaluate_circuit(form)
                out_tt = tts[-1] if tts else None
                rows.append({'circuit': form, 'nested': c['nested'], 'parts': c['gates'],
                             'part_truth_tables': tts,
                             'output_accepted_for_the_task': None if out_tt is None else out_tt in R.ACCEPT[T],
                             'function_skeleton': function_skeleton(form),
                             'nand_only': ops <= {'nand'} or form.startswith('out='),
                             'sequences': c['sequences'], 'programs': c['programs'], 'runs': len(c['runs']),
                             'distinct_route_instruction_strings': len(c['route_letters']),
                             'example': {'run': c['example'][1], 'sequence': c['example'][2],
                                         'programs': c['example'][0]}})
            return rows
        full, red = table(circ), table(circ_red)
        skel = collections.Counter()
        skel_seq = collections.Counter()
        for r in red:
            skel[r['function_skeleton']] += r['programs']
            skel_seq[r['function_skeleton']] += r['sequences']
        checked = collections.Counter(str(r['output_accepted_for_the_task']) for r in red)
        def shares(c, top=8):                                                           # Xa7
            tot = sum(c.values())
            return {k: round(100.0 * v / tot, 1) for k, v in c.most_common(top)}
        entry.update({
            'smallest_ablation_stopping_it': {'by_sequence': dict(size), 'by_program': dict(size_w)},
            'smallest_ablation_stopping_it_after_the_settling_rerun (Xb1)': {'by_sequence': dict(size_after),
                                                                             'by_program': dict(size_after_w)},
            'minimal_pairs_total (Xb3)': n_minimal_pairs,
            'irreducible_set_sizes (Xb3)': irr_sizes,
            'required_instruction_kinds_by_run_pct_top8 (Xa7)': {r: shares(kinds_run[r]) for r in runs if kinds_run[r]},
            'required_instruction_roles_by_run_pct_weighted_by_programs_top8 (Xa7)': {
                r: shares(roles_run[r]) for r in runs if roles_run[r]},
            'distinct_reduced_circuits_with_constant_values_kept_apart (Xc3)': len(circ_red_values),
            'irreducible_search_start': dict(irr_kind),
            'required_instructions_per_sequence': {'mean': round(sum(n_required) / len(n_required), 2),
                                                   'min': min(n_required), 'max': max(n_required)},
            'required_instruction_kinds': dict(kinds1.most_common()),
            'distinct_required_instruction_strings': len(req_strings),
            'most_common_required_instruction_strings_by_programs': dict(req_names.most_common(5)),
            'required_instruction_roles': dict(roles1.most_common()),
            'required_instruction_roles_weighted_by_programs': dict(roles1_w.most_common()),
            'ablation_against_routes': dict(cut_all_routes),
            'required_sites_against_the_credited_route': dict(overlap),
            'minimal_pair_roles': {' + '.join(k): v for k, v in pair_roles.most_common(12)},
            'single_site_stops_it_vs_number_of_routes': {'%s, %s' % ('a single site stops it' if a else
                                                                     'no single site stops it', b): v
                                                         for (a, b), v in sorted(redundancy.items())},
            'credited_output_is_first_accepted_output': {str(k): v for k, v in credited_agree.items()},
            'generality_of_credited_circuit': {str(k): v for k, v in sorted(generality.items())},
            'distinct_circuits': len(full), 'distinct_reduced_circuits': len(red),
            'reduced_circuits_output_checked_on_all_eight_bit_combinations': dict(checked),
            'distinct_function_skeletons': len(skel),
            'function_skeletons_top': [{'truth_tables': list(k) if k is not None else None, 'programs': v,
                                        'sequences': skel_seq[k]} for k, v in skel.most_common(8)],
            'distinct_reduced_circuits_over_all_routes': len(circ_any),
            'smallest_nand_circuit_possible': SMALLEST_NAND[T],
            'smallest_reduced_circuit_found': min(r['parts'] for r in red),
            'smallest_nand_only_circuit_found': min([r['parts'] for r in red if r['nand_only']] or [None],
                                                    key=lambda x: 99 if x is None else x),
            'reduced_circuits_top': red[:12], 'circuits_top': full[:5],
        })
        x = red[0]['example']
        examples_wanted[T] = (x['programs'], x['run'], x['sequence'])
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
                    if T not in r['variants']['unchanged']['sums'] or not r['variants']['unchanged']['viable']:
                        continue          # the same set of Avida programs as the ablations: replicating and performing T
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
            cd = collections.Counter()                                                   # Xb4
            for x in w['copying_sites']:
                cd['%s, %s' % ('splits in the trace' if x['divided'] else 'does not split in the trace',
                               'credited with some task' if x['sums_credited_by_test_processor'] else 'credited with none')] += 1
                c['tasks still performed in the trace: %s' % ('all' if set(w['sums']) <= set(x['sums_written_in_trace'])
                                                             else ('some' if x['sums_written_in_trace'] else 'none'))] += 1
            out['without_replication'][run] = {'sequence': w['seq'], 'replication_required_sites': len(w['copying_sites']),
                                               'counts': dict(c), 'split_and_credit (Xb4)': dict(cd)}

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
