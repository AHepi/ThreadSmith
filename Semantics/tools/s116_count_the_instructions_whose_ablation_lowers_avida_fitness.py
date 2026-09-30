#!/usr/bin/env python3
"""s116_count_the_instructions_whose_ablation_lowers_avida_fitness.py

What it does, in plain words (log S116, batch 2, GPT 6 Astra's reply 05 procedure "K"): for every program population
S113 saved (copies made by tools/s116_probe_the_saved_program_populations.py), takes its 100 most common distinct
instruction sequences (by the number of Avida programs carrying each), and runs Avida's own instruction ablation
(ANALYZE_KNOCKOUTS: each instruction in turn replaced by Avida's null instruction, the program run again on the test
CPU) under ONE fixed reference Avida execution environment: S113's FIXED GRADED environment (the nine two-input logic
tasks rewarded 1 to 5, the other 68 listed at 0, no resources), made by S113's own function, imported unchanged.
K of a sequence = the number of its instructions whose ablation makes it nonfunctional or lowers its Avida fitness
(Avida's "lethal" plus "detrimental"). Per saved population: K's mean weighted by programs, median and maximum over the
viable sequences, and how many of the 100 were viable.

One Avida process per S113 run (10 saved populations in it), analyze mode only, through the wrapper s116/bin/avida
(nice -n 19, one-hour limit), at most two at once. Raw output stays in the scratch space (s116/k/).
  python3 s116_count_the_instructions_whose_ablation_lowers_avida_fitness.py [N]      (N at once, default 2)
Written 30 September 2026 by the one Opus 5.5 agent of log S116.
"""
import json, os, shutil, statistics, subprocess, sys
from concurrent.futures import ThreadPoolExecutor

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import s113_run_the_avida_execution_environments as R      # noqa: E402  (environment text; read only)
import s116_probe_the_saved_program_populations as P       # noqa: E402  (copies, keys, marks)

KDIR = P.S116 + '/k'
TOP = 100


def top_sequences(path):
    pop = []
    for line in open(path):
        if line.startswith('#') or not line.strip():
            continue
        w = line.split()
        if int(w[4]) > 0:
            pop.append((int(w[4]), w[16]))
    pop.sort(key=lambda x: -x[0])      # stable: ties keep the file's order
    return pop[:TOP], sum(n for n, _ in pop)


def one_run(key):
    d = os.path.join(KDIR, key)
    if os.path.exists(os.path.join(d, 'done.json')):
        return key, json.load(open(os.path.join(d, 'done.json')))
    if os.path.exists(d):
        shutil.rmtree(d)
    os.makedirs(d)
    for f in ['avida.cfg', 'instset-heads.cfg']:
        shutil.copy(os.path.join(R.S111CONF, f), d)
    open(os.path.join(d, 'environment.cfg'), 'w').write(R.environment_text('fixed_graded', R.load_ranks()))
    open(os.path.join(d, 'events.cfg'), 'w').write('u begin Exit\n')
    lines, tops = [], {}
    for m in P.MARKS:
        top, total = top_sequences(os.path.join(P.COPIES, key, 'u%d.spop' % m))
        tops[m] = (top, total)
        lines += ['PURGE_BATCH'] + ['LOAD_SEQUENCE ' + s for _, s in top] + [
            'RECALCULATE', 'FILTER viable == 1', 'DETAIL seqs_u%d.dat viable fitness sequence' % m,
            'ANALYZE_KNOCKOUTS knock_u%d.dat 1' % m]
    open(os.path.join(d, 'analyze.cfg'), 'w').write('\n'.join(lines) + '\n')
    rc = subprocess.run([P.WRAPPER, '-a', '-s', '1', '-set', 'VERBOSITY', '0'], cwd=d,
                        stdout=open(os.path.join(d, 'analyze.log'), 'w'), stderr=subprocess.STDOUT,
                        stdin=subprocess.DEVNULL).returncode
    if rc != 0:
        return key, {'error': 'exit %d' % rc}
    res = {}
    for m in P.MARKS:
        top, total = tops[m]
        count = {}
        for n, s in top:
            count[s] = count.get(s, 0) + n
        seqs = [l.split()[-1] for l in open(os.path.join(d, 'data', 'seqs_u%d.dat' % m))
                if l.strip() and not l.startswith('#')]
        knock = [[int(x) for x in l.split()] for l in open(os.path.join(d, 'data', 'knock_u%d.dat' % m))
                 if l.strip() and not l.startswith('#')]
        assert len(seqs) == len(knock), (key, m)
        ks = [(count[s], k[1] + k[2]) for s, k in zip(seqs, knock)]
        w = sum(n for n, _ in ks)
        res[str(m)] = {'sequences_tested': len(top), 'viable': len(ks), 'programs_in_tested': sum(n for n, _ in top),
                       'programs_in_population': total,
                       'K_weighted_mean': round(sum(n * k for n, k in ks) / w, 3) if w else None,
                       'K_median': statistics.median([k for _, k in ks]) if ks else None,
                       'K_max': max([k for _, k in ks]) if ks else None,
                       'lethal_weighted_mean': round(sum(count[s] * k[1] for s, k in zip(seqs, knock)) / w, 3)
                       if w else None}
    json.dump(res, open(os.path.join(d, 'done.json'), 'w'), indent=1)
    return key, res


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 2
    os.makedirs(KDIR, exist_ok=True)
    out = {}
    with ThreadPoolExecutor(max_workers=n) as pool:
        for key, res in pool.map(one_run, P.KEYS):
            out[key] = res
            print(key, {m: (r.get('K_weighted_mean'), r.get('viable')) for m, r in res.items()}
                  if 'error' not in res else res, flush=True)
    json.dump({'what': 'log S116 batch 2: reply 05 K under S113 FIXED GRADED, top %d sequences' % TOP,
               'per run': out}, open(os.path.join(KDIR, 'summary.json'), 'w'), indent=1)


if __name__ == '__main__':
    main()
