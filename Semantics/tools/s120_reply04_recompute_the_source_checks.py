"""S120, continued: recompute, independently, the "source_checks" outputs that GPT 6 Astra's reply 04 to S119's brief 04
says it ran (tests/S119 Returns from GPT 6 Astra/04 Return - the execution environment as an autonomous agent.md,
section "Execution record"). Written by Claude (one Opus 5.5 agent) on 1 October 2026; no code of the reply is used.

What it does, in plain words:
  1. reads Avida's task library (avida-core/source/main/cTaskLib.cc at commit 47f13dad, read only), finds the nine
     standard logic tasks and every Task_Logic3in_* task, and collects the logic numbers ("logic ids", 0 to 255, one
     for each way of combining three input bits) each of them accepts;
  2. counts the tasks, the logic ids accepted by at least one task, and the ids accepted by none;
  3. checks, for every one of the six orders of Avida's three fixed test numbers (0x0f13149f, 0x3308e53e,
     0x556241eb), how many of the eight three-bit patterns occur across the 32 bit positions (Avida's checking code,
     cTaskLib::SetupTests, needs all eight to name a logic id);
  4. redoes the reply's arithmetic (S113 spreads, CPU-hours, wall-hours, the largest probe budget) and the size of
     its 36-cell trial region.
It prints everything and writes a JSON copy into the scratch folder given below. Nothing in Avida is run.
"""
import itertools, json, os, re, subprocess

SCRATCH = '/tmp/claude-0/-home-user-ThreadSmith/8d9323da-c0ec-57ec-91fd-8f99ca99320a/scratchpad'
AVIDA_CLONE = SCRATCH + '/avida'
TASK_LIBRARY = AVIDA_CLONE + '/avida-core/source/main/cTaskLib.cc'
OUTPUT_FOLDER = SCRATCH + '/s120_reply04'
STANDARD_LOGIC_TASKS = ['Not', 'Nand', 'And', 'OrNot', 'Or', 'AndNot', 'Nor', 'Xor', 'Equ']


def method_bodies(source_text):
    """Every 'double cTaskLib::Task_<name>(...)' method with its body, up to the closing brace at line start."""
    pattern = re.compile(r'^double cTaskLib::Task_(\w+)\(cTaskContext& ctx\) const\n\{\n(.*?)^\}', re.M | re.S)
    return {match.group(1): match.group(2) for match in pattern.finditer(source_text)}


def smallest_detectable_split(seeds_per_arm=12, threshold=0.05):
    """For a yes/no outcome per seed (for example "the standing question closed"), the pairs (a, b) of yes-counts in
    two arms of 12 seeds for which a one-sided Fisher exact test gives p < 0.05; returns, for each b, the smallest a."""
    from math import comb
    n = seeds_per_arm
    smallest = {}
    for b in range(n + 1):
        for a in range(b, n + 1):
            total = a + b
            p_value = sum(comb(n, x) * comb(n, total - x) for x in range(a, min(n, total) + 1)) / comb(2 * n, total)
            if p_value < threshold:
                smallest[b] = a
                break
    return smallest


def main():
    commit = subprocess.run(['git', '-C', AVIDA_CLONE, 'rev-parse', 'HEAD'], capture_output=True, text=True).stdout.strip()
    source_text = open(TASK_LIBRARY).read()
    bodies = method_bodies(source_text)
    logic_task_names = [name for name in STANDARD_LOGIC_TASKS if name in bodies]
    logic_task_names += sorted(name for name in bodies if name.startswith('Logic3in_'))
    accepted_by_task = {}
    for name in logic_task_names:
        ids = [int(number) for number in re.findall(r'logic_id\s*==\s*(\d+)', bodies[name])]
        accepted_by_task[name] = ids
    every_accepted_id = sorted(set(i for ids in accepted_by_task.values() for i in ids))
    excluded_ids = [i for i in range(256) if i not in every_accepted_id]
    ids_accepted_by_more_than_one_task = sorted(
        i for i in every_accepted_id if sum(i in ids for ids in accepted_by_task.values()) > 1)
    tasks_accepting_no_id = [name for name, ids in accepted_by_task.items() if not ids]

    test_numbers = (0x0f13149f, 0x3308e53e, 0x556241eb)
    patterns_per_order = {}
    for order in itertools.permutations(range(3)):
        numbers = [test_numbers[i] for i in order]
        patterns = set()
        for bit in range(32):
            patterns.add(sum(((numbers[k] >> bit) & 1) << k for k in range(3)))
        patterns_per_order['/'.join('%08x' % n for n in numbers)] = len(patterns)

    arithmetic = {
        'S113_spreads (65-48, 41-13, 17-8, 8-7)': [65 - 48, 41 - 13, 17 - 8, 8 - 7],
        'two_arms_twelve_seeds_reference_CPU_hours': 2 * 12 * 1,
        'four_arms_twelve_seeds_reference_CPU_hours': 4 * 12 * 1,
        'reference_wall_hours_at_three_processes': (2 * 12 / 3, 4 * 12 / 3),
        'fifty_epochs_256_candidates_6_tests_10000_cycles': 50 * 256 * 6 * 10000,
        'trial_region_cells_and_share_of_world': (36, 36 / 3600),
        'cells_0_to_35_in_a_60_wide_world_rows_used': sorted(set(cell // 60 for cell in range(36))),
        'twelve_seeds_per_arm_smallest_yes_count_beating_b_one_sided_Fisher_p_below_0.05': smallest_detectable_split(),
    }
    result = {
        'avida_commit': commit,
        'logic_task_functions': len(logic_task_names),
        'standard_logic_tasks_found': [n for n in STANDARD_LOGIC_TASKS if n in bodies],
        'logic3in_tasks_found': len([n for n in logic_task_names if n.startswith('Logic3in_')]),
        'accepted_logic_ids': len(every_accepted_id),
        'excluded_logic_ids': excluded_ids,
        'ids_accepted_by_more_than_one_task': ids_accepted_by_more_than_one_task,
        'tasks_accepting_no_id': tasks_accepting_no_id,
        'complete_bit_patterns_per_permutation': list(patterns_per_order.values()),
        'patterns_per_order': patterns_per_order,
        'arithmetic': arithmetic,
    }
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    json.dump(result, open(OUTPUT_FOLDER + '/source_checks_recomputed.json', 'w'), indent=1)
    for key, value in result.items():
        print(key, '=', value)


if __name__ == '__main__':
    main()
