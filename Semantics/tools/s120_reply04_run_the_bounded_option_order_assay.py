"""S120, continued: the "bounded next option" of GPT 6 Astra's reply 04 to S119's brief 04, done where S116 had not
already done it. Written by Claude (one Opus 5.5 agent) on 1 October 2026.

What S116 already did (its settlement's order check, tools/s116x_settle_order_check.py): the stock supplied-input
assay (analyze mode, RECALCULATE with the three input numbers given by hand) on EVERY saved program of all 18 S113
program populations at update 50,000, with the same three numbers in all six orders. It kept, per program, whether the
program copies itself ("viable") and which of the 77 logic tasks it was credited with; it did not keep the numbers the
program handed out.

What this script adds, and nothing more (reply 04 asks for "one saved order-sensitive program and one
order-insensitive program, preserving first outputs"):
  1. from S116's own per-program files for GROWING LIST seed 2 at update 50,000 (read only), it picks the most common
     program that copies itself and does NOT in the world's order but copies itself in at most one of the other five
     orders ("order-sensitive"), and the most common program that copies itself and does NOT in all six orders
     ("order-insensitive");
  2. it runs stock Avida in analyze mode only (nothing advanced) on those two programs with Avida's three fixed test
     numbers in each of the six orders: RECALCULATE plus DETAIL (copies itself? tasks credited) and TRACE (every
     executed step);
  3. from each trace it reads every number the program handed out with the IO instruction, in order, and which
     logic id (0 to 255) the first outputs correspond to.
Every Avida process runs under nice -n 19 and a 10-minute time limit; raw output goes to the scratch folder below.
"""
import itertools, json, os, re, resource, subprocess, sys, time

SCRATCH = '/tmp/claude-0/-home-user-ThreadSmith/8d9323da-c0ec-57ec-91fd-8f99ca99320a/scratchpad'
AVIDA_PROGRAM = SCRATCH + '/avida/cbuild/bin/avida'
S116_ORDER_CHECK = SCRATCH + '/s116x_settle/order_growing_seed2'
S116_RUN_FOLDER = SCRATCH + '/s116x_settle/order_rundir'
SAVED_POPULATION = SCRATCH + '/s116/copies/growing_seed2/u50000.spop'
OUTPUT_FOLDER = SCRATCH + '/s120_reply04/bounded_option'
TEST_NUMBERS = (0x0f13149f, 0x3308e53e, 0x556241eb)   # cEnvironment::SetupInputs, random = false
ORDERS = list(itertools.permutations(range(3)))         # S116's files t00 to t05 follow this same order


def read_s116_file(index):
    rows = {}
    for line in open('%s/data/t%02d.dat' % (S116_ORDER_CHECK, index)):
        if line.startswith('#') or not line.strip():
            continue
        words = line.split()
        rows[int(words[0])] = {'copies': int(words[1]), 'viable': int(words[2]) > 0, 'NOT': int(words[3]) > 0}
    return rows


def pick_two_programs():
    tables = [read_s116_file(i) for i in range(6)]
    candidates_sensitive, candidates_insensitive = [], []
    for program_id, first in tables[0].items():
        if not (first['viable'] and first['NOT']):
            continue
        viable_other_orders = sum(tables[k][program_id]['viable'] for k in range(1, 6))
        not_all_orders = all(tables[k][program_id]['viable'] and tables[k][program_id]['NOT'] for k in range(6))
        if viable_other_orders <= 1:
            candidates_sensitive.append((first['copies'], program_id))
        if not_all_orders:
            candidates_insensitive.append((first['copies'], program_id))
    candidates_sensitive.sort(reverse=True)
    candidates_insensitive.sort(reverse=True)
    summary = {
        'programs_viable_and_NOT_in_world_order': sum(1 for r in tables[0].values() if r['viable'] and r['NOT']),
        'order_sensitive_candidates': len(candidates_sensitive),
        'order_insensitive_candidates': len(candidates_insensitive),
        'order_sensitive_copies_in_population': sum(c for c, _ in candidates_sensitive),
        'order_insensitive_copies_in_population': sum(c for c, _ in candidates_insensitive),
    }
    return candidates_sensitive[0], candidates_insensitive[0], summary


def outputs_from_trace(path):
    """Every number handed out by IO: the register that IO overwrote held the output just before it ran."""
    steps = []
    lines = open(path).read().splitlines()
    for i, line in enumerate(lines):
        match = re.match(r'^\d+ IP:(\d+) \((\S+)\)', line)
        if match and i + 1 < len(lines):
            registers = [int(v) for v in re.findall(r'[ABC]X:(-?\d+)', lines[i + 1])]
            steps.append((match.group(2), registers))
    outputs = []
    for k, (instruction, registers) in enumerate(steps[:-1]):
        if instruction != 'IO':
            continue
        after = steps[k + 1][1]
        changed = [r for r in range(3) if registers[r] != after[r]]
        if changed:
            outputs.append(registers[changed[0]])
        else:
            outputs.append(None)   # the output equalled the next input read; recorded as unknown
    return outputs, len(steps)


def executed_positions(path):
    """The (step, instruction position, instruction name) of every executed step in a trace."""
    steps = []
    for line in open(path):
        match = re.match(r'^(\d+) IP:(\d+) \((\S+)\)', line)
        if match:
            steps.append((int(match.group(1)), int(match.group(2)), match.group(3)))
    return steps


def first_divergence(world_order_path, other_order_path):
    """Descriptive only: the first executed step at which the program's path differs from its path in the world's
    order, and the instruction executed just before it (the one whose result sent the path elsewhere)."""
    a, b = executed_positions(world_order_path), executed_positions(other_order_path)
    for k in range(min(len(a), len(b))):
        if a[k][1] != b[k][1]:
            return {'step': k, 'instruction_just_before': a[k - 1][2] if k else None,
                    'its_position': a[k - 1][1] if k else None,
                    'next_position_world_order': a[k][1], 'next_position_this_order': b[k][1],
                    'IO_steps_before_it': sum(1 for s in a[:k] if s[2] == 'IO')}
    return None if len(a) == len(b) else {'step': min(len(a), len(b)), 'note': 'one path is a prefix of the other'}


def logic_id(output, inputs_in_reading_order):
    """cTaskLib::SetupTests: Input A is the most recent input, B the one before, C the one before that."""
    if len(inputs_in_reading_order) < 3:
        return None   # fewer than three numbers read yet; not computed here
    recent_first = list(reversed(inputs_in_reading_order[-3:]))
    table = {}
    for bit in range(32):
        position = sum(((recent_first[k] >> bit) & 1) << k for k in range(3))
        value = (output >> bit) & 1
        if table.get(position, value) != value:
            return -1
        table[position] = value
    if len(table) < 8:
        return None
    return sum(table[p] << p for p in range(8))


def main():
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    (sensitive_copies, sensitive_id), (insensitive_copies, insensitive_id), summary = pick_two_programs()
    chosen = {'order-sensitive': sensitive_id, 'order-insensitive': insensitive_id}
    lines = []
    for batch, (label, program_id) in enumerate(chosen.items()):
        lines += ['SET_BATCH %d' % batch, 'PURGE_BATCH', 'LOAD ' + SAVED_POPULATION, 'FILTER id == %d' % program_id]
        for k, order in enumerate(ORDERS):
            numbers = [TEST_NUMBERS[i] for i in order]
            lines.append('RECALCULATE 0 -1 0 %d %d %d' % tuple(numbers))
            lines.append('DETAIL detail_order%d_%d.dat id num_units viable fitness gest_time length ' % (k, program_id)
                         + ' '.join('task.%d' % j for j in range(77)))
            lines.append('TRACE trace_order%d/ 0 -1 0 %d %d %d' % ((k,) + tuple(numbers)))
    open(OUTPUT_FOLDER + '/analyze.cfg', 'w').write('\n'.join(lines) + '\n')
    start_cpu = resource.getrusage(resource.RUSAGE_CHILDREN)
    start = time.time()
    exit_code = subprocess.run(
        ['timeout', '600', 'nice', '-n', '19', AVIDA_PROGRAM, '-c', S116_RUN_FOLDER + '/avida.cfg', '-a',
         '-set', 'ENVIRONMENT_FILE', S116_ORDER_CHECK + '/environment.cfg',
         '-set', 'ANALYZE_FILE', OUTPUT_FOLDER + '/analyze.cfg', '-set', 'EVENT_FILE', S116_ORDER_CHECK + '/events.cfg',
         '-set', 'DATA_DIR', OUTPUT_FOLDER + '/data', '-set', 'RANDOM_SEED', '20261001', '-set', 'VERBOSITY', '1',
         '-set', 'TASK_REFRACTORY_PERIOD', '0', '-set', 'TEST_CPU_TIME_MOD', '20'],
        cwd=S116_RUN_FOLDER, stdout=open(OUTPUT_FOLDER + '/run.log', 'w'), stderr=subprocess.STDOUT).returncode
    end_cpu = resource.getrusage(resource.RUSAGE_CHILDREN)
    cpu_seconds = (end_cpu.ru_utime - start_cpu.ru_utime) + (end_cpu.ru_stime - start_cpu.ru_stime)
    results = {'avida_exit_code': exit_code, 'cpu_seconds': round(cpu_seconds, 2), 'wall_seconds': round(time.time() - start, 2),
               'population_summary_from_S116_files': summary,
               'chosen': {'order-sensitive': {'id': sensitive_id, 'copies_in_population': sensitive_copies},
                          'order-insensitive': {'id': insensitive_id, 'copies_in_population': insensitive_copies}},
               'per_order': {}}
    for k, order in enumerate(ORDERS):
        numbers = [TEST_NUMBERS[i] for i in order]
        detail = {}
        for program_id in chosen.values():
            for line in open('%s/data/detail_order%d_%d.dat' % (OUTPUT_FOLDER, k, program_id)):
                if line.startswith('#') or not line.strip():
                    continue
                w = line.split()
                detail[int(w[0])] = {'viable': int(w[2]) > 0, 'fitness': float(w[3]), 'gestation_time': float(w[4]),
                                     'length': int(w[5]), 'tasks_credited': [j for j in range(77) if int(w[6 + j]) > 0]}
        entry = {'inputs_in_world_slots': ['%08x' % n for n in numbers], 'top_bytes': [n >> 24 for n in numbers]}
        for label, program_id in chosen.items():
            trace_files = [f for f in os.listdir('%s/data/trace_order%d' % (OUTPUT_FOLDER, k)) if f.endswith('.trace')]
            trace_name = [f for f in trace_files if f.startswith('%d' % program_id) or ('-%d.' % program_id) in f or f == '%d.trace' % program_id]
            outputs, executed_steps = outputs_from_trace('%s/data/trace_order%d/%s' % (OUTPUT_FOLDER, k, trace_name[0])) if trace_name else ([], 0)
            ids = []
            for n, output in enumerate(outputs[:6]):
                read_so_far = [numbers[i % 3] for i in range(n + 1)]   # IO hands out, then reads the next input in turn
                ids.append(None if output is None else logic_id(output, read_so_far[:-1] if n > 0 else []))
            entry[label] = dict(detail.get(program_id, {}), trace_file=trace_name[0] if trace_name else None,
                                executed_steps=executed_steps, number_of_outputs=len(outputs),
                                first_outputs_hex=['%08x' % (o & 0xffffffff) if o is not None else None for o in outputs[:6]],
                                logic_ids_of_first_outputs=ids)
        results['per_order'][' '.join(str(b) for b in entry['top_bytes'])] = entry
    results['first_divergence_from_the_world_order'] = {}
    for label, program_id in chosen.items():
        world_trace = '%s/data/trace_order0/org-%d.trace' % (OUTPUT_FOLDER, program_id)
        results['first_divergence_from_the_world_order'][label] = {
            ' '.join(str(TEST_NUMBERS[i] >> 24) for i in order): first_divergence(
                world_trace, '%s/data/trace_order%d/org-%d.trace' % (OUTPUT_FOLDER, k, program_id))
            for k, order in enumerate(ORDERS) if k > 0}
    json.dump(results, open(OUTPUT_FOLDER + '/result.json', 'w'), indent=1)
    print(json.dumps(results, indent=1))


if __name__ == '__main__':
    main()
