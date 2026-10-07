#!/usr/bin/env python3
"""Stock 47f13dad saved-sequence assays; Python 3 standard library only.

Run six serial test-CPU assays. This measures the stock last-cycle task record,
not every output, and uses a fixed diagnostic triple rather than live cell input
numbers. An all-orders task requires the SAME saved sequence to pass all orders.
"""
import argparse
import hashlib
import itertools
import json
from pathlib import Path
import re
import subprocess
import sys


DEFAULT_INPUTS = (0x0F13149F, 0x3308E53E, 0x556241EB)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def read_table(path):
    columns, rows, legends = None, [], {}
    for line in Path(path).read_text().splitlines():
        if line.startswith("#format "):
            require(columns is None, f"Duplicate #format in {path}")
            columns = line.split()[1:]
        match = re.fullmatch(r"#\s*(\d+):\s*(.*)", line)
        if match:
            key = int(match[1]) - 1
            require(key not in legends, f"Duplicate legend in {path}")
            legends[key] = match[2].strip()
        if line.strip() and not line.startswith("#"):
            rows.append(line.split())
    require(columns, f"Missing #format in {path}")
    require(rows, f"No saved sequence rows in {path}")
    require(all(len(row) == len(columns) for row in rows), f"Wrong row width in {path}")
    return columns, rows, legends


def source_rows(path):
    columns, rows, _ = read_table(path)
    require({"id", "sequence", "num_units"} <= set(columns),
            "Snapshot must be stock SavePopulation with id, sequence, num_units")
    require(len(columns) == len(set(columns)), "Repeated snapshot column")
    result = {}
    for values in rows:
        row = dict(zip(columns, values))
        key, count = int(row["id"]), int(row["num_units"])
        require(key not in result and count >= 0, "Duplicate ID or negative abundance")
        result[key] = (count, row["sequence"])
    require(sum(r[0] for r in result.values()) > 0, "Empty program population")
    return result


def assay_rows(path, source, manifest):
    columns, rows, legends = read_table(path)
    expected = ["id", "num_cpus", "sequence", "viable"]
    # This pinned build writes repeated 'task' names; match numbered descriptions.
    expected += ["task"] * len(manifest)
    require(columns == expected, f"Unexpected assay columns in {path}")
    for j, task in enumerate(manifest):
        require(legends.get(4 + j) == task["description"],
                f"Absent or mismatched task detector {task['task']} in {path}")
    result = {}
    for values in rows:
        row = dict(zip(columns[:4], values[:4]))
        key, count, passes = int(row["id"]), int(row["num_cpus"]), int(row["viable"])
        require(key not in result, "Repeated ID in assay")
        require(key in source and source[key] == (count, row["sequence"]),
                "Assay ID, abundance or sequence differs from snapshot")
        require(passes in (0, 1), "Invalid replication-pass flag")
        counts = tuple(map(int, values[4:]))
        require(all(n >= 0 for n in counts), "Negative task count")
        result[key] = (passes, counts)
    require(set(result) == set(source), "Missing saved sequences in assay")
    return result


def weighted_counts(source, orders, task_count, require_replication=False):
    return [sum(n for key, (n, _) in source.items()
                if all(row[key][1][j] > 0 and
                       (not require_replication or row[key][0] == 1)
                       for row in orders))
            for j in range(task_count)]


def summarize(source, orders, task_names):
    total = sum(n for n, _ in source.values())
    result = {}
    for scope, selected in (("native", orders[:1]), ("all6", orders)):
        for replication in (False, True):
            label = scope + ("_replication_pass" if replication else "_task_record")
            counts = weighted_counts(source, selected, len(task_names), replication)
            common = [name for name, count in zip(task_names, counts) if 10 * count >= total]
            result[label] = {"counts": counts, "shares": [n / total for n in counts],
                             "common_tasks": common, "common_count": len(common)}
    return result


def file_sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--avida", type=Path, required=True)
    parser.add_argument("--piece", type=Path, required=True, help="Driver piece directory")
    parser.add_argument("--snapshot", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True, help="New output directory")
    parser.add_argument("--inputs", type=lambda s: int(s, 0), nargs=3, default=DEFAULT_INPUTS)
    parser.add_argument("--baseline", type=Path, help="Earlier measurement.json for the same assay")
    parser.add_argument("--schedule", type=Path, help="Driver schedule.json; include offers through this piece")
    parser.add_argument("--ever-offered", type=Path,
                        help="JSON array of task names offered positive pay up to this snapshot")
    parser.add_argument("--timeout", type=float, default=600.0, help="Seconds per order")
    args = parser.parse_args()
    args.avida, args.piece = args.avida.resolve(), args.piece.resolve()
    args.snapshot, args.manifest = args.snapshot.resolve(), args.manifest.resolve()
    args.out = args.out.resolve()
    require(not args.out.exists(), "Output directory already exists; use a new directory")
    require(args.timeout > 0, "Timeout must be positive")
    require(all(-(1 << 31) <= n < (1 << 31) for n in args.inputs), "Inputs need signed 32-bit range")
    require(len(set(args.inputs)) == 3, "Use three distinct input numbers")
    require({sum(((n >> bit) & 1) << j for j, n in enumerate(args.inputs))
             for bit in range(32)} == set(range(8)),
            "Diagnostic triple must contain every three-input bit combination")
    # Avida's LOAD/DETAIL command parser separates words on whitespace.
    for path in (args.snapshot, args.out):
        require(not any(c.isspace() for c in str(path)), "Use paths without whitespace")
    manifest = json.loads(args.manifest.read_text())
    require(isinstance(manifest, list) and len(manifest) == 77, "Expected the ordered 77-task manifest")
    names = [item["task"] for item in manifest]
    require(len(set(names)) == 77, "Duplicate task name in manifest")
    require(not (args.schedule and args.ever_offered), "Use schedule or ever-offered, not both")
    offered = None
    if args.schedule:
        schedule = json.loads(args.schedule.read_text())
        match = re.fullmatch(r"piece-(\d+)", args.piece.name)
        require(match is not None, "Schedule requires driver directory piece-NNNNN")
        number = int(match[1])
        require(schedule["tasks"] == manifest and len(schedule["values"]) > number,
                "Schedule does not match manifest or cover this piece")
        values = schedule["values"][:number + 1]
        require(all(len(row) == 77 and all(isinstance(v, (int, float)) and
                    v >= 0 and v < float("inf") for v in row) for row in values),
                "Invalid schedule values")
        offered = [name for j, name in enumerate(names) if any(row[j] > 0 for row in values)]
    elif args.ever_offered:
        offered = json.loads(args.ever_offered.read_text())
        require(isinstance(offered, list) and set(offered) <= set(names), "Invalid offered-task list")
    source = source_rows(args.snapshot)
    args.out.mkdir(parents=True)
    orders, invocations = [], []
    for k, permutation in enumerate(itertools.permutations(args.inputs)):
        directory = args.out / f"order-{k}"
        directory.mkdir()
        analyze = directory / "analyze.cfg"
        detail = directory / "counts.dat"
        fields = " ".join(f"task.{j}" for j in range(77))
        analyze.write_text(f"LOAD {args.snapshot}\nRECALCULATE 0 -1 0 " +
                           " ".join(map(str, permutation)) +
                           f"\nDETAIL {detail} id num_cpus sequence viable {fields}\n")
        (directory / "events.cfg").write_text("# No simulation events in this assay.\n")
        command = [str(args.avida), "-a", "-c", "avida.cfg", "-s", "1",
                   "-set", "ANALYZE_FILE", str(analyze),
                   "-set", "DATA_DIR", str(directory / "data"),
                   "-set", "EVENT_FILE", str(directory / "events.cfg")]
        record = {"cwd": str(args.piece), "argv": command, "inputs": list(permutation)}
        invocations.append(record)
        (directory / "command.json").write_text(json.dumps(record, indent=2) + "\n")
        with (directory / "avida.log").open("w") as log:
            completed = subprocess.run(command, cwd=args.piece, stdout=log,
                                       stderr=subprocess.STDOUT, timeout=args.timeout)
        require(completed.returncode == 0, f"Avida failed in {directory}; inspect avida.log")
        log = (directory / "avida.log").read_text()
        require(not re.search(r"(?im)^\s*(?:error|fatal)(?:\s|:)", log),
                f"Avida reported an error in {directory}")
        require(detail.is_file(), f"No assay output in {directory}")
        orders.append(assay_rows(detail, source, manifest))
    result = {"schema": 1, "method": "stock_last_cycle_fixed_input_diagnostic",
              "native_inputs": list(args.inputs), "task_names": names,
              "total_programs": sum(n for n, _ in source.values()),
              "saved_sequence_rows": len(source),
              "assays": invocations,
              "sha256": {"avida": file_sha256(args.avida),
                         "snapshot": file_sha256(args.snapshot),
                         "manifest": file_sha256(args.manifest),
                         "avida.cfg": file_sha256(args.piece / "avida.cfg"),
                         "environment.cfg": file_sha256(args.piece / "environment.cfg"),
                         "instset-heads.cfg": file_sha256(args.piece / "instset-heads.cfg")},
              "replication_failed_programs_per_order":
                  [sum(n for key, (n, _) in source.items() if order[key][0] == 0)
                   for order in orders],
              "measures": summarize(source, orders, names)}
    if offered is not None:
        result["never_offered_tasks"] = [name for name in names if name not in offered]
        for measure in result["measures"].values():
            measure["common_never_offered"] = [name for name in measure["common_tasks"] if name not in offered]
    else:
        result["never_offered_tasks"] = None
    if args.baseline:
        baseline = json.loads(args.baseline.read_text())
        require(baseline["method"] == result["method"] and
                baseline["native_inputs"] == result["native_inputs"] and
                baseline["task_names"] == names and
                baseline["sha256"]["instset-heads.cfg"] == result["sha256"]["instset-heads.cfg"] and
                baseline["sha256"]["avida"] == result["sha256"]["avida"],
                "Baseline assay differs in method, inputs, tasks, instruction set or executable")
        for key, measure in result["measures"].items():
            initial = set(baseline["measures"][key]["common_tasks"])
            measure["newly_common_since_baseline"] = [n for n in measure["common_tasks"] if n not in initial]
            measure["common_count_change"] = measure["common_count"] - len(initial)
    destination = args.out / "measurement.json"
    destination.write_text(json.dumps(result, indent=2) + "\n")
    print("programs=" + str(result["total_programs"]))
    print("orders=6; all6 uses the same saved sequence in every order")
    for key, measure in result["measures"].items():
        print(key + " common=" + str(measure["common_count"]))
    print("never_offered=" + ("unknown" if result["never_offered_tasks"] is None
                              else str(len(result["never_offered_tasks"]))))


if __name__ == "__main__":
    try:
        main()
    except (ValueError, KeyError, OSError, subprocess.TimeoutExpired) as error:
        print("measurement error: " + str(error), file=sys.stderr)
        sys.exit(1)
