#!/usr/bin/env python3
"""s112_test_what_the_sums_depend_on_in_the_environment.py

What it does, in plain words: for log S112, runs the same evolved programs (every living genotype of the nine S111 runs at
update 50,000; their letters unchanged) in Avida's test processor with one thing of the environment changed, and records
which sums each program still does and whether it still copies itself. The changes:
  E1  the letter u means "nor" instead of "nand"; then "and" instead of "nand" (one line of the instruction-set file)
  E2  the letter y (IO, the input and output channel) means nop-X, an instruction that does nothing
  E3  other numbers handed in: three triples of random 32-bit numbers, and Avida's fixed three in another order
      (Avida's RECALCULATE with manual inputs; the numbers are those of the trace reader, so that its predictions,
      made from the circuits before this runs, can be compared)
  E4  the 26 meanings assigned to the 26 letters in another order (three random shufflings, seeded)
Writes one JSON line per genotype into the scratch space (s112/environment/<run>.jsonl); nothing into the repository.
Everything runs inside Avida's simulated processor.

  python3 -B Semantics/tools/s112_test_what_the_sums_depend_on_in_the_environment.py [jobs]

Written 30 September 2026 by the one Opus 5.5 agent of log S112.
"""
import json, os, random, sys
from concurrent.futures import ProcessPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import s112_run_programs_in_avidas_test_processor as P  # noqa: E402
from s112_read_what_the_programs_compute_from_avidas_traces import OTHER_INPUTS  # noqa: E402

OUT = P.SCRATCH + '/s112/environment'
_rng = random.Random(1122)
SHUFFLES = {}
for k in (1, 2, 3):
    names = list(P.NAMES)
    _rng.shuffle(names)
    SHUFFLES['letters shuffled %d' % k] = names


def variants():
    v = [('unchanged', {}),
         ('nand read as nor', {'names': [('nor' if n == 'nand' else n) for n in P.NAMES]}),
         ('nand read as and', {'names': [('and' if n == 'nand' else n) for n in P.NAMES]}),
         ('IO read as nop-X', {'names': [('nop-X' if n == 'IO' else n) for n in P.NAMES], 'with_null': False})]
    v += [(k, {'inputs': x}) for k, x in OTHER_INPUTS.items()]
    v += [(k, {'names': x, 'with_null': False}) for k, x in SHUFFLES.items()]
    return v


def one_run(run):
    pop = P.living(run)
    seqs = [s for s, _ in pop]
    res = {s: {'run': run, 'seq': s, 'organisms': n, 'variants': {}} for s, n in pop}
    for name, kw in variants():
        rows = P.evaluate(seqs, **kw)
        for s, r in zip(seqs, rows):
            res[s]['variants'][name] = {'viable': r['viable'], 'sums': sorted(P.tasks_of(r), key=P.TASKS.index)}
    with open(os.path.join(OUT, run + '.jsonl'), 'w') as f:
        for s in seqs:
            f.write(json.dumps(res[s]) + '\n')
    return run, len(seqs)


if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    jobs = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    runs = [r for r in P.RUN_NAMES if not os.path.exists(os.path.join(OUT, r + '.jsonl'))]
    with open(os.path.join(OUT, 'variants.json'), 'w') as f:
        json.dump({'shuffles': SHUFFLES, 'other_inputs': OTHER_INPUTS}, f, indent=1)
    with ProcessPoolExecutor(jobs) as ex:
        for run, n in ex.map(one_run, runs):
            print(run, n, 'genotypes', flush=True)
