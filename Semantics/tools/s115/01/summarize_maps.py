# NOTE (added by Claude, log S115): this file is 'summarize_maps.py', copied unchanged from the appendix of
# GPT 6 Astra's reply 01 ('tests/S115 Returns from GPT 6 Astra/01 Return - measuring what is learned,
# with stock Avida only.md'). Only these note lines were added. It has not been run on S113's data;
# see 'results/S115 Checking the Astra returns/01 Check of reply 01 - measuring what is learned.md'.
#!/usr/bin/env python3
"""Summarize stock MAP_TASKS outputs; no sequence execution or homology inference.

MAP_TASKS must request columns in this exact order:
viable fitness gest_time env_input.0 env_input.1 env_input.2 task.N ...
The final task columns must match --tasks in order.
maps.tsv: input_id, input0, input1, input2, directory (tab separated).
Optional matches.tsv: ancestor_id, ancestor_site, ancestor_task, descendant_id,
descendant_site, descendant_task, basis. Sites are one based; basis records the
user-supplied positional reconstruction. Overlap remains conditional on it.
Fitness summaries compare printed fitness values, include viability-losing
ablations, and apply no persistence filter. Rounding can hide small differences.
The positional skeleton uses '_' as an output placeholder; it is not executable.
"""
import argparse
import csv
import math
from collections import Counter, defaultdict
from pathlib import Path


def read_tsv(path):
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path, rows):
    if not rows:
        return
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, list(rows[0]), delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)


def phenotype(words, task_ids, inputs, where):
    if len(words) != 6 + len(task_ids):
        raise ValueError(f"{where}: wrong width; check MAP_TASKS column order")
    viable, gestation = int(words[0]), int(words[2])
    fitness = float(words[1])
    counts = [int(x) for x in words[6:]]
    if viable not in (0, 1) or not math.isfinite(fitness) or min(counts) < 0:
        raise ValueError(f"{where}: invalid phenotype values")
    if tuple(map(int, words[3:6])) != inputs:
        raise ValueError(f"{where}: actual input values differ from maps.tsv")
    return viable, fitness, gestation, dict(zip(task_ids, counts))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--tasks", nargs="+", required=True, type=int)
    parser.add_argument("--out", required=True, type=Path)
    parser.add_argument("--matches", type=Path)
    args = parser.parse_args()
    if min(args.tasks) < 0 or len(set(args.tasks)) != len(args.tasks):
        raise ValueError("Task indices must be distinct and nonnegative")
    manifests = read_tsv(args.manifest)
    if not manifests or len({r["input_id"] for r in manifests}) != len(manifests):
        raise ValueError("Need nonempty maps.tsv with distinct input_id values")
    sites, summaries, fitness_rows, lookup = [], [], [], {}
    signatures = {}
    expected_ids = None
    for m in manifests:
        input_id = m["input_id"]
        inputs = tuple(int(m[f"input{i}"]) for i in range(3))
        directory = Path(m["directory"])
        if not directory.is_absolute():
            directory = args.manifest.resolve().parent / directory
        files = sorted(directory.glob("tasksites.*.dat"))
        if not files:
            raise ValueError(f"{directory}: no MAP_TASKS files")
        seen_ids = set()
        for path in files:
            rows = [line.split() for line in path.read_text().splitlines()
                    if line.strip() and not line.lstrip().startswith("#")]
            if not rows or len(rows[0]) < 3 or rows[0][0] != "-1":
                raise ValueError(f"{path}: missing baseline row")
            ident = int(rows[0][2])
            if ident in seen_ids:
                raise ValueError(f"{path}: duplicate ID within one input")
            seen_ids.add(ident)
            base = phenotype(rows[0][3:], args.tasks, inputs, str(path))
            if not rows[1:] or [int(r[0]) for r in rows[1:]] != list(range(1, len(rows))):
                raise ValueError(f"{path}: noncontiguous or missing site rows")
            signature = tuple((r[1], r[2]) for r in rows[1:])
            if ident in signatures and signatures[ident] != signature:
                raise ValueError(f"{path}: source instructions changed between inputs")
            signatures[ident] = signature
            tallies = {task: Counter() for task in args.tasks}
            fitness_sites = []
            skeleton = []
            for raw in rows[1:]:
                site = int(raw[0])
                mutant = phenotype(raw[3:], args.tasks, inputs, f"{path}:{site}")
                decreases = bool(base[0] and mutant[1] < base[1])
                if decreases:
                    fitness_sites.append(site)
                skeleton.append(raw[1] if decreases else "_")
                for task in args.tasks:
                    baseline_count, mutant_count = base[3][task], mutant[3][task]
                    if not base[0]:
                        status = "baseline_ineligible"
                    elif not baseline_count:
                        status = "baseline_task_absent"
                    elif not mutant[0]:
                        status = "viability_confounded"
                    elif not mutant_count:
                        status = "required"
                    else:
                        status = "task_preserved"
                    record = dict(input_id=input_id, id=ident, site=site, task=task,
                        original_symbol=raw[1], original_instruction=raw[2],
                        baseline_viable=base[0], baseline_task_count=baseline_count,
                        baseline_fitness=base[1], baseline_gest_time=base[2],
                        mutant_viable=mutant[0], mutant_task_count=mutant_count,
                        mutant_fitness=mutant[1], mutant_gest_time=mutant[2], status=status,
                        neutral_for_task=int(status == "task_preserved"),
                        fitness_unchanged=int(base[1] == mutant[1]),
                        count_unchanged=int(baseline_count == mutant_count))
                    sites.append(record)
                    lookup[(input_id, ident, site, task)] = record
                    tallies[task][status] += 1
            for task in args.tasks:
                summary = dict(input_id=input_id, id=ident, task=task,
                    baseline_viable=base[0], baseline_task_count=base[3][task],
                    length=len(rows)-1)
                summary.update({name: tallies[task][name] for name in
                    ("required", "task_preserved", "viability_confounded",
                     "baseline_ineligible", "baseline_task_absent")})
                summaries.append(summary)
            fitness_rows.append(dict(input_id=input_id, id=ident,
                baseline_viable=base[0], baseline_fitness=base[1], length=len(rows)-1,
                fitness_required_sites=len(fitness_sites) if base[0] else "",
                required_positions=";".join(map(str, fitness_sites)) if base[0] else "",
                ordered_required_symbols="".join(symbol for symbol in skeleton if symbol != "_") if base[0] else "",
                positional_skeleton="".join(skeleton) if base[0] else ""))
        if expected_ids is not None and seen_ids != expected_ids:
            raise ValueError("Different sequence-ID sets between input panels")
        expected_ids = seen_ids
    grouped = defaultdict(list)
    for row in sites:
        grouped[(row["id"], row["site"], row["task"])].append(row)
    across = [dict(id=k[0], site=k[1], task=k[2], inputs=len(rows),
        baseline_eligible_all=int(all(r["baseline_viable"] and r["baseline_task_count"] for r in rows)),
        required_all=int(all(r["status"] == "required" for r in rows)),
        task_preserved_all=int(all(r["status"] == "task_preserved" for r in rows)),
        viability_confounded_any=int(any(r["status"] == "viability_confounded" for r in rows)))
        for k, rows in grouped.items()]
    overlaps = []
    if args.matches:
        for n, match in enumerate(read_tsv(args.matches)):
            if not match["basis"].strip():
                raise ValueError("Each matched position requires a reconstruction basis")
            for m in manifests:
                inp = m["input_id"]
                old = lookup[(inp, int(match["ancestor_id"]), int(match["ancestor_site"]), int(match["ancestor_task"]))]
                new = lookup[(inp, int(match["descendant_id"]), int(match["descendant_site"]), int(match["descendant_task"]))]
                overlaps.append(dict(match=n, input_id=inp, **match,
                    ancestor_status=old["status"], descendant_status=new["status"],
                    endpoint_symbols_equal=int(old["original_symbol"] == new["original_symbol"]),
                    shared_dependence_conditional=int(old["status"] == new["status"] == "required")))
    args.out.mkdir(parents=True, exist_ok=True)
    write_tsv(args.out / "sites.tsv", sites)
    write_tsv(args.out / "summary.tsv", summaries)
    write_tsv(args.out / "sites_all_inputs.tsv", across)
    write_tsv(args.out / "conditional_overlap.tsv", overlaps)
    write_tsv(args.out / "fitness_sites.tsv", fitness_rows)
    fitness_summary = []
    for m in manifests:
        eligible = [row for row in fitness_rows if row["input_id"] == m["input_id"] and row["baseline_viable"]]
        fitness_summary.append(dict(input_id=m["input_id"], viable_baselines=len(eligible),
            max_fitness_required_sites=max((row["fitness_required_sites"] for row in eligible), default="")))
    write_tsv(args.out / "fitness_summary.tsv", fitness_summary)
    print(args.out)


if __name__ == "__main__":
    main()
