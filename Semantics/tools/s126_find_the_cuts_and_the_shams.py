#!/usr/bin/env python3
"""s126_find_the_cuts_and_the_shams.py

What it does, in plain words: for log S126 (the closing knock-out test), takes the two saved program populations of
S113's COMMON TASKS PAY LESS execution environment (seeds 1 and 2, at 50,000 updates), picks in each the task q by the
rule written before running (the task the most programs were credited with at the save, ties to the higher reward),
and finds, for every distinct instruction sequence that does q:

  the CUT   the smallest set of instruction replacements (each instruction replaced by nop-X, an instruction that does
            nothing and is no label) after which the program, on every input of a four-input panel, no longer does q,
            still copies itself, and does every other task exactly as before;
  the SHAM  the same number of replacements at sites that change nothing on the panel (copying, all nine tasks, and the
            time a copy takes all identical).

Every program is run alone by Avida's own analysis mode (its test processor; no variation, no neighbours) in an
execution environment that lists the nine tasks at pay 0. This script only chooses which sites to replace and reads
Avida's answers. It reads S113's scratch folder and never writes there: the two saves and their resource files are
copied into the scratch folder s126/source/. Output: s126/prep/cuts_seed<k>.json. Nothing is written into the
repository. Avida's programs copy themselves only inside Avida's simulated processor; nothing here copies itself on
the real machine. Every Avida process runs under a time limit and at the lowest priority (nice 19), at most 3 at once.

  python3 -B Semantics/tools/s126_find_the_cuts_and_the_shams.py [seed ...]

Written 2 October 2026 by the one Opus 5.5 agent of log S126.
"""
import itertools, json, os, random, shutil, subprocess, sys, tempfile, time
from concurrent.futures import ThreadPoolExecutor

SCRATCH = '/tmp/claude-0/-home-user-ThreadSmith/8d9323da-c0ec-57ec-91fd-8f99ca99320a/scratchpad'
AVIDA = SCRATCH + '/avida/cbuild/bin/avida'
S113RUNS = SCRATCH + '/s113/runs'
OUT = SCRATCH + '/s126'
WORK = OUT + '/work'
HERE = os.path.dirname(os.path.abspath(__file__))
CONF = os.path.join(os.path.dirname(HERE), 'results', 'S111 Avida - the runs', 'configuration')

TASKS = ['not', 'nand', 'and', 'orn', 'or', 'andn', 'nor', 'xor', 'equ']
LEVEL = {'not': 1, 'nand': 1, 'and': 2, 'orn': 2, 'or': 3, 'andn': 3, 'nor': 4, 'xor': 4, 'equ': 5}
NULL = 'A'                      # nop-X, the 27th instruction, never made by copying errors (mutation weight 0)
FIELDS = ['viable', 'gest_time'] + ['task.%d' % i for i in range(9)] + ['sequence']
CHUNK = 4000
FIXED = (0x0f13149f, 0x3308e53e, 0x556241eb)   # Avida's test-processor inputs (cEnvironment.cc 1284-1288)
PANEL_SEED = 126
SHAM_SEED = 1260
PARALLEL = 3
TIMEOUT = 1800


def panel():
    """Avida's fixed test inputs and three more in Avida's input form (top bytes 0x0f, 0x33, 0x55; low 24 bits drawn)."""
    rng = random.Random(PANEL_SEED)
    out = [None]
    for _ in range(3):
        out.append(tuple((top << 24) | rng.getrandbits(24) for top in (0x0f, 0x33, 0x55)))
    return out


def instset_text():
    with open(os.path.join(CONF, 'instset-heads.cfg')) as f:
        base = f.read().rstrip('\n')
    return base + '\nINST nop-X:redundancy=0   # A (log S126: does nothing, is no label, never made by copying errors)\n'


def probe_environment_text():
    return ''.join('REACTION %s %s process:value=0.0:type=pow requisite:max_count=1\n' % (t.upper(), t) for t in TASKS)


def _evaluate_chunk(seqs, inputs):
    os.makedirs(WORK, exist_ok=True)
    d = tempfile.mkdtemp(prefix='a_', dir=WORK)
    shutil.copy(os.path.join(CONF, 'avida.cfg'), d)
    open(os.path.join(d, 'instset-heads.cfg'), 'w').write(instset_text())
    open(os.path.join(d, 'environment.cfg'), 'w').write(probe_environment_text())
    open(os.path.join(d, 'events.cfg'), 'w').write('u begin Exit\n')
    rc = 'RECALCULATE' if inputs is None else 'RECALCULATE 0 -1 0 %d %d %d' % tuple(inputs)
    with open(os.path.join(d, 'analyze.cfg'), 'w') as f:
        f.write('\n'.join(['LOAD_SEQUENCE ' + s for s in seqs] + [rc, 'DETAIL out.dat ' + ' '.join(FIELDS)]) + '\n')
    with open(os.path.join(d, 'analyze.log'), 'w') as log:
        r = subprocess.run(['timeout', str(TIMEOUT), 'nice', '-n', '19', AVIDA, '-a', '-s', '1', '-set', 'VERBOSITY',
                            '0'], cwd=d, stdout=log, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL).returncode
    if r != 0:
        raise RuntimeError('Avida analysis mode exited %d in %s' % (r, d))
    rows = []
    for line in open(os.path.join(d, 'data', 'out.dat')):
        if line.startswith('#') or not line.strip():
            continue
        v = line.split()
        tasks = frozenset(TASKS[k] for k in range(9) if float(v[2 + k]) > 0)
        rows.append((int(float(v[0])), int(float(v[1])), tasks, v[11]))
    if len(rows) != len(seqs) or any(r[3] != s for r, s in zip(rows, seqs)):
        raise RuntimeError('Avida returned %d rows for %d sequences, or out of order, in %s' % (len(rows), len(seqs), d))
    shutil.rmtree(d)
    return [r[:3] for r in rows]


CPU_SECONDS = [0.0]


def evaluate(seqs, inputs):
    """(viable, gestation time, set of tasks done) for each sequence, on one input triple (None = Avida's fixed)."""
    seqs = list(seqs)
    if not seqs:
        return []
    parts = [seqs[i:i + CHUNK] for i in range(0, len(seqs), CHUNK)]
    t0 = os.times()
    with ThreadPoolExecutor(max_workers=PARALLEL) as pool:
        res = list(pool.map(lambda p: _evaluate_chunk(p, inputs), parts))
    t1 = os.times()
    CPU_SECONDS[0] += (t1.children_user - t0.children_user) + (t1.children_system - t0.children_system)
    return [r for part in res for r in part]


def evaluate_panel(seqs, inputs_list):
    """dict sequence -> list over the panel of (viable, gest, tasks)."""
    seqs = sorted(set(seqs))
    out = {s: [] for s in seqs}
    for inp in inputs_list:
        for s, r in zip(seqs, evaluate(seqs, inp)):
            out[s].append(r)
    return out


def knock(seq, sites):
    s = list(seq)
    for i in sites:
        s[i] = NULL
    return ''.join(s)


def copy_sources(seed):
    src = os.path.join(S113RUNS, 'common_pays_less_seed%d' % seed, 'piece_49')
    dst = os.path.join(OUT, 'source', 'seed%d' % seed)
    os.makedirs(dst, exist_ok=True)
    for rel in ['data/detail-1000.spop', 'data/resource.dat', 'data/tasks.dat', 'data/count.dat', 'environment.cfg',
                'events.cfg']:
        shutil.copy(os.path.join(src, rel), os.path.join(dst, os.path.basename(rel)))
    return dst


def living(spop):
    fmt, out = None, []
    for line in open(spop):
        if line.startswith('#format'):
            fmt = line.split()[1:]
            continue
        if line.startswith('#') or not line.strip():
            continue
        r = dict(zip(fmt, line.split()))
        if int(r['num_units']) > 0:
            out.append((r['sequence'], int(r['num_units'])))
    return out


def choose_q(src):
    """The rule written before running: the task the most programs were credited with at the save (tasks.dat, last
    row), ties to the higher reward level, then to the later task in Avida's order."""
    last = [l for l in open(os.path.join(src, 'tasks.dat')) if l.strip() and not l.startswith('#')][-1].split()
    counts = {t: int(float(last[1 + k])) for k, t in enumerate(TASKS)}
    q = max(TASKS, key=lambda t: (counts[t], LEVEL[t], TASKS.index(t)))
    res_line = [l for l in open(os.path.join(src, 'resource.dat')) if l.strip() and not l.startswith('#')][-1].split()
    stores = {t: float(res_line[1 + k]) for k, t in enumerate(TASKS)}
    return q, counts, stores


def same_except(base_r, new_r, q):
    """new keeps copying and does every task other than q exactly as base, on one input."""
    return new_r[0] == 1 and (new_r[2] - {q}) == (base_r[2] - {q})


def main(seeds):
    inputs = panel()
    for seed in seeds:
        t_start = time.time()
        CPU_SECONDS[0] = 0.0
        src = copy_sources(seed)
        q, counts, stores = choose_q(src)
        pop = living(os.path.join(src, 'detail-1000.spop'))
        programs = sum(n for _, n in pop)
        seqs = sorted(set(s for s, _ in pop))
        n_of = {}
        for s, n in pop:
            n_of[s] = n_of.get(s, 0) + n
        base = evaluate_panel(seqs, inputs)
        qseqs = [s for s in seqs if any(q in r[2] for r in base[s])]
        print('seed %d: q = %s; %d programs, %d sequences, %d do q on the panel (%d programs)' % (
            seed, q, programs, len(seqs), len(qseqs), sum(n_of[s] for s in qseqs)), flush=True)

        # 1. every single site of every q-sequence, on Avida's fixed inputs first
        singles = {s: [knock(s, [i]) for i in range(len(s))] for s in qseqs}
        flat = [v for s in qseqs for v in singles[s]]
        r0 = dict(zip(flat, evaluate(flat, inputs[0])))
        cut1_cand, sham_cand, viable_sites = {}, {}, {}
        for s in qseqs:
            b = base[s][0]
            cut1_cand[s], sham_cand[s], viable_sites[s] = [], [], []
            for i, v in enumerate(singles[s]):
                r = r0[v]
                if r[0] == 1:
                    viable_sites[s].append(i)
                if q not in r[2] and same_except(b, r, q):
                    cut1_cand[s].append(i)
                if r == b and s[i] != NULL:
                    sham_cand[s].append(i)
        # verify single-site candidates on the other three inputs
        check = sorted(set(knock(s, [i]) for s in qseqs for i in set(cut1_cand[s]) | set(sham_cand[s])))
        rest = evaluate_panel(check, inputs[1:])
        full = lambda v, s: [r0[v]] + rest[v]
        cuts, shams = {}, {}
        for s in qseqs:
            good = []
            for i in cut1_cand[s]:
                v = knock(s, [i])
                rr = full(v, s)
                if all(q not in rr[k][2] and same_except(base[s][k], rr[k], q) for k in range(4)):
                    good.append((abs(rr[0][1] - base[s][0][1]), i))
            if good:
                good.sort()
                cuts[s] = {'sites': [good[0][1]], 'kind': 'clean', 'gest_change': rr_gest(full(knock(s, [good[0][1]]), s), base[s]),
                           'lost': []}
            shams[s] = [i for i in sham_cand[s] if full(knock(s, [i]), s) == base[s]]

        # 2. pairs, for q-sequences with no clean single cut, among sites whose single replacement keeps copying
        need = [s for s in qseqs if s not in cuts]
        print('seed %d: %d sequences have a clean single cut; %d need pairs' % (seed, len(cuts), len(need)), flush=True)
        for b0 in range(0, len(need), 150):
            batch = need[b0:b0 + 150]
            pair_variants = {}
            for s in batch:
                sites = viable_sites[s]
                pair_variants[s] = [(a, b) for a, b in itertools.combinations(sites, 2)]
            flat = sorted(set(knock(s, p) for s in batch for p in pair_variants[s]))
            rp0 = dict(zip(flat, evaluate(flat, inputs[0]))) if flat else {}
            cand2 = {}
            for s in batch:
                b = base[s][0]
                cand2[s] = [p for p in pair_variants[s] if q not in rp0[knock(s, p)][2] and rp0[knock(s, p)][0] == 1]
            check = sorted(set(knock(s, p) for s in batch for p in cand2[s]))
            rest2 = evaluate_panel(check, inputs[1:])
            for s in batch:
                clean, dirty = [], []
                for p in cand2[s]:
                    v = knock(s, p)
                    rr = [rp0[v]] + rest2[v]
                    if not all(q not in rr[k][2] and rr[k][0] == 1 for k in range(4)):
                        continue
                    lost = sorted((k, t) for k in range(4) for t in (base[s][k][2] - {q}) - rr[k][2])
                    gained = sorted((k, t) for k in range(4) for t in rr[k][2] - base[s][k][2])
                    key = (abs(rr[0][1] - base[s][0][1]), p)
                    if not lost and not gained:
                        clean.append(key)
                    else:
                        dirty.append((len(lost) + len(gained), key[0], p, lost, gained, rr))
                if clean:
                    clean.sort()
                    p = clean[0][1]
                    cuts[s] = {'sites': list(p), 'kind': 'clean', 'gest_change': rr_gest([rp0[knock(s, p)]] + rest2[knock(s, p)], base[s]),
                               'lost': []}
                else:
                    # the smallest set of size 1 or 2 that stops q and keeps copying, losing the fewest other tasks
                    singles_dirty = []
                    for i in viable_sites[s]:
                        v = knock(s, [i])
                        if q in r0[v][2]:
                            continue
                        singles_dirty.append(i)
                    found = None
                    if singles_dirty:
                        vs = [knock(s, [i]) for i in singles_dirty]
                        rs = evaluate_panel(vs, inputs[1:])
                        opts = []
                        for i, v in zip(singles_dirty, vs):
                            rr = [r0[v]] + rs[v]
                            if all(q not in rr[k][2] and rr[k][0] == 1 for k in range(4)):
                                lost = sorted((k, t) for k in range(4) for t in (base[s][k][2] - {q}) - rr[k][2])
                                gained = sorted((k, t) for k in range(4) for t in rr[k][2] - base[s][k][2])
                                opts.append((len(lost) + len(gained), abs(rr[0][1] - base[s][0][1]), [i], lost, gained, rr))
                        if opts:
                            opts.sort(key=lambda o: (o[0], o[1], o[2]))
                            found = opts[0]
                    if found is None and dirty:
                        dirty.sort(key=lambda o: (o[0], o[1], o[2]))
                        found = dirty[0]
                    if found is None:
                        cuts[s] = {'sites': [], 'kind': 'none', 'gest_change': None, 'lost': []}
                    else:
                        cuts[s] = {'sites': list(found[2]), 'kind': 'collateral', 'gest_change': rr_gest(found[5], base[s]),
                                   'lost': [[k, t] for k, t in found[3]], 'gained': [[k, t] for k, t in found[4]]}

        # 3. the shams: as many replacements as the cut, at sites that change nothing on the panel
        rng = random.Random(SHAM_SEED + seed)
        sham_of = {}
        pair_checks = []
        for s in qseqs:
            k = len(cuts[s]['sites'])
            pool = [i for i in shams[s] if i not in cuts[s]['sites']]
            if k == 0:
                sham_of[s] = {'sites': [], 'kind': 'no cut'}
            elif k == 1:
                sham_of[s] = {'sites': [rng.choice(pool)], 'kind': 'single'} if pool else {'sites': [], 'kind': 'none'}
            else:
                draws = []
                for _ in range(50):
                    if len(pool) < k:
                        break
                    draws.append(sorted(rng.sample(pool, k)))
                sham_of[s] = {'sites': [], 'kind': 'none', 'draws': draws}
                pair_checks += [knock(s, d) for d in draws]
        if pair_checks:
            rpc = evaluate_panel(pair_checks, inputs)
            for s in qseqs:
                if 'draws' in sham_of[s]:
                    draws = sham_of[s].pop('draws')
                    for d in draws:
                        if rpc[knock(s, d)] == base[s]:
                            sham_of[s] = {'sites': d, 'kind': 'set of %d' % len(d)}
                            break

        # 4. final check: every cut and sham sequence on the whole panel, read once more
        finals = sorted(set([knock(s, cuts[s]['sites']) for s in qseqs] + [knock(s, sham_of[s]['sites']) for s in qseqs]))
        rf = evaluate_panel(finals, inputs)
        recs = []
        for s in qseqs:
            c, h = knock(s, cuts[s]['sites']), knock(s, sham_of[s]['sites'])
            recs.append({'sequence': s, 'programs': n_of[s], 'cut_sites': cuts[s]['sites'], 'cut_kind': cuts[s]['kind'],
                         'cut_removed': [s[i] for i in cuts[s]['sites']], 'cut_sequence': c,
                         'cut_does_q_on_panel': any(q in r[2] for r in rf[c]),
                         'cut_copies_on_panel': all(r[0] == 1 for r in rf[c]),
                         'cut_other_tasks_kept': all((rf[c][k][2] - {q}) == (base[s][k][2] - {q}) for k in range(4)),
                         'cut_gestation_change': [rf[c][k][1] - base[s][k][1] for k in range(4)],
                         'cut_lost': cuts[s].get('lost', []), 'cut_gained': cuts[s].get('gained', []),
                         'sham_sites': sham_of[s]['sites'], 'sham_kind': sham_of[s]['kind'], 'sham_sequence': h,
                         'sham_changes_nothing_on_panel': rf[h] == base[s],
                         'original_on_panel': [[r[0], r[1], sorted(r[2])] for r in base[s]]})
        not_q = [s for s in seqs if s not in set(qseqs)]
        summary = {
            'seed': seed, 'q': q, 'task_counts_at_save': counts, 'stores_at_save': stores,
            'programs': programs, 'sequences': len(seqs),
            'q_sequences': len(qseqs), 'q_programs': sum(n_of[s] for s in qseqs),
            'sequences_not_viable_on_panel': sum(1 for s in seqs if not all(r[0] == 1 for r in base[s])),
            'programs_in_sequences_not_viable_on_any_input': sum(n_of[s] for s in seqs if not any(r[0] == 1 for r in base[s])),
            'cut_kinds': {k: [sum(1 for r in recs if r['cut_kind'] == k), sum(r['programs'] for r in recs if r['cut_kind'] == k)]
                          for k in ('clean', 'collateral', 'none')},
            'cut_sizes': {str(n): sum(1 for r in recs if len(r['cut_sites']) == n) for n in (0, 1, 2)},
            'sham_kinds': {k: sum(1 for r in recs if r['sham_kind'] == k) for k in set(r['sham_kind'] for r in recs)},
            'programs_with_no_sham_although_cut': sum(r['programs'] for r in recs if r['cut_sites'] and not r['sham_sites']),
            'cuts_failing_final_check': sum(1 for r in recs if r['cut_sites'] and (r['cut_does_q_on_panel'] or not r['cut_copies_on_panel'])),
            'shams_failing_final_check': sum(1 for r in recs if r['sham_sites'] and not r['sham_changes_nothing_on_panel']),
            'panel_inputs': [list(FIXED)] + [list(p) for p in inputs[1:]],
            'analysis_cpu_seconds': round(CPU_SECONDS[0], 1), 'wall_seconds': round(time.time() - t_start),
        }
        os.makedirs(os.path.join(OUT, 'prep'), exist_ok=True)
        json.dump({'summary': summary, 'records': recs}, open(os.path.join(OUT, 'prep', 'cuts_seed%d.json' % seed), 'w'), indent=0)
        print(json.dumps(summary), flush=True)


def rr_gest(rr, b):
    return [rr[k][1] - b[k][1] for k in range(4)]


if __name__ == '__main__':
    main([int(a) for a in sys.argv[1:]] or [1, 2])
