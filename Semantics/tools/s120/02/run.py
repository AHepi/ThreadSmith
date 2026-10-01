#!/usr/bin/env python3
"""Stock Avida selector v1. Python 3 standard library; see SPEC-v1.md.

Reads only pinned stock sources; runs Avida in newly created piece directories.
All replication is performed by Avida virtual-machine instructions in Avida.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path
import re
import shutil
import subprocess
import sys

PIN = "47f13dadb547fcf10f620ace60247f38b30b8b16"
SPEC = "selector-v1"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def dump(path, value):
    path = Path(path)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, allow_nan=False) + "\n")
    temporary.replace(path)


def manifest(source):
    support = source / "avida-core/support/config"
    entries = re.findall(r'^REACTION\s+(\S+)\s+(\S+)\s+',
                         (support / "misc/environment-all-logic.cfg").read_text(), re.M)
    # Capture the task key and full printed description, not a guessed column order.
    descriptions = dict(re.findall(r'name\s*==\s*"([^"\n]+)"\)\s*NewTask\(name,\s*"([^"\n]+)"',
                                   (source / "avida-core/source/main/cTaskLib.cc").read_text()))
    expected = "not nand and orn or andn nor xor equ".split()
    expected += ["logic_3" + a + b for a in "ABC" for b in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                 if a != "C" or b <= "P"]
    require(len(entries) == 77 and {t for _, t in entries} == set(expected),
            "expected exactly the pinned stock 77-task manifest")
    require(all(t in descriptions for _, t in entries), "task description missing in source")
    result = [{"reaction": r, "task": t, "description": descriptions[t]} for r, t in entries]
    require(len({m["description"] for m in result}) == 77, "duplicate task description")
    return result


def table(path):
    columns, rows = {}, []
    for line in Path(path).read_text().splitlines():
        match = re.match(r'^\s*#\s*(\d+)\s*:\s*(.*?)\s*$', line)
        if match:
            index, name = int(match[1]) - 1, match[2].casefold()
            require(index >= 0 and index not in columns and name not in columns.values(),
                    "duplicate/invalid column in " + str(path))
            columns[index] = name
        elif line.strip() and not line.lstrip().startswith("#"):
            row = [float(x) for x in line.split()]
            require(all(math.isfinite(x) for x in row), "nonfinite data in " + str(path))
            rows.append(row)
    require(columns and rows, "empty table " + str(path))
    require(set(columns) == set(range(len(columns))), "noncontiguous columns in " + str(path))
    require(all(len(row) == len(columns) for row in rows), "ragged data in " + str(path))
    return [{columns[i]: value for i, value in enumerate(row)} for row in rows]


def observe(piece, tasks, boundary):
    task_rows, count_rows = table(piece / "data/tasks.dat"), table(piece / "data/count.dat")
    tr, cr = task_rows[-1], count_rows[-1]
    require(tr.get("update") == cr.get("update") == boundary, "missing/mismatched boundary update")
    require("number of organisms" in cr, "living-program count column missing")
    count = cr["number of organisms"]
    require(count == int(count) and 0 < count <= 3600, "empty/invalid living program population")
    require(set(tr) == {"update"} | {m["description"].casefold() for m in tasks},
            "task columns differ from source manifest")
    counts = [tr[m["description"].casefold()] for m in tasks]
    require(all(x == int(x) and 0 <= x <= count for x in counts), "invalid per-program task count")
    return int(count), [int(x) for x in counts], [x / count for x in counts]


def progress(history, window, budget):
    width = min(window, len(history) - 1)
    require(width > 0, "progress needs one observed piece")
    slopes = [max(0.0, (new - old) / width)
              for new, old in zip(history[-1], history[-1 - width])]
    scale = budget / max(1.0, sum(slopes))
    return [scale * slope for slope in slopes]


def rarity(exposure, budget):
    scores = [1.0 / (1.0 + x) for x in exposure]
    return [budget * x / sum(scores) for x in scores]


def mean_schedule(values):
    require(values and len({len(row) for row in values}) == 1, "empty/ragged schedule")
    return [sum(column) / len(values) for column in zip(*values)]


def common_changes(shares, counts, previous, cumulative):
    current = {j for j, p in enumerate(shares) if p >= 0.1}
    return current, {"common_360cells": sum(x >= 360 for x in counts),
                     "cumulative_common": len(cumulative | current),
                     "first_common": sorted(current - cumulative),
                     "reacquired": sorted((current & cumulative) - previous),
                     "lost": sorted(previous - current)}


def piece_seed(master, index):
    raw = hashlib.sha256((SPEC + ":" + str(master) + ":" + str(index)).encode()).digest()
    return 1 + int.from_bytes(raw[:8], "big") % 2147483646


def configured(base, overrides):
    for key, value in overrides.items():
        base, count = re.subn(r'^' + re.escape(key) + r'\s+[^\n]*$', key + " " + str(value), base, flags=re.M)
        require(count == 1, "missing/duplicate config key " + key)
    return base


def event_text(boundary, reload):
    first = "u begin LoadPopulation input.spop" if reload else "u begin Inject ancestor.org"
    return first + "\n" + "\n".join(
        "u " + str(boundary) + " " + action for action in (
            "PrintTasksData", "PrintCountData", "PrintAverageData", "PrintTimeData",
            "SavePopulation filename=population:save_historic=0", "Exit")) + "\n"


def prepare(piece, support, tasks, values, seed, boundary, previous):
    piece.mkdir()
    for original, dest in (("instset-heads.cfg", "instset-heads.cfg"),
                           ("default-heads.org", "ancestor.org"), ("analyze.cfg", "analyze.cfg")):
        shutil.copyfile(support / original, piece / dest)
    overrides = {"RANDOM_SEED": seed, "VERBOSITY": 0, "WORLD_X": 60, "WORLD_Y": 60,
                 "WORLD_GEOMETRY": 2, "DATA_DIR": "data", "ENVIRONMENT_FILE": "environment.cfg",
                 "EVENT_FILE": "events.cfg", "COPY_MUT_PROB": 0.0075,
                 "DIVIDE_INS_PROB": 0.05, "DIVIDE_DEL_PROB": 0.05}
    (piece / "avida.cfg").write_text(configured((support / "avida.cfg").read_text(), overrides))
    (piece / "environment.cfg").write_text("# selector-v1; all 77 detectors remain present\n" + "".join(
        "REACTION {reaction} {task} process:value={value:.17g}:type=pow requisite:max_count=1\n".format(
            **task, value=value) for task, value in zip(tasks, values)))
    (piece / "events.cfg").write_text(event_text(boundary, previous is not None))
    if previous is not None:
        shutil.copyfile(previous, piece / "input.spop")
    dump(piece / "pay.json", {"seed": seed, "values": values})


def load_control(path, tasks, rig, args):
    donor = json.loads(Path(path).read_text())
    require(donor.get("complete") is True, "donor schedule is incomplete")
    require(donor["tasks"] == tasks and donor["rig"] == rig, "donor task manifest/rig differs")
    require(donor["piece_updates"] == args.piece_updates and len(donor["values"]) == args.pieces,
            "donor duration differs")
    require(donor["seed"] != args.seed, "fixed/replay requires a different recipient seed")
    require(all(len(row) == len(tasks) and all(isinstance(x, (int, float)) and math.isfinite(x) and x >= 0
                                            for x in row) for row in donor["values"]), "invalid pay vector")
    return donor["values"]


def run(args):
    source, binary, output = Path(args.source).resolve(), Path(args.avida).resolve(), Path(args.out).resolve()
    require(binary.is_file(), "Avida executable missing")
    head = subprocess.check_output(["git", "-C", str(source), "rev-parse", "HEAD"], text=True).strip()
    require(head == PIN, "source checkout is not pinned commit " + PIN)
    clean = subprocess.run(["git", "-C", str(source), "diff", "--quiet", "HEAD", "--"])
    require(clean.returncode == 0, "pinned source has tracked modifications")
    tasks = manifest(source)
    support = source / "avida-core/support/config"
    rig_files = [support / n for n in ("avida.cfg", "instset-heads.cfg", "default-heads.org", "analyze.cfg")]
    rig_files += [support / "misc/environment-all-logic.cfg", source / "avida-core/source/main/cTaskLib.cc"]
    rig = {"commit": head, "spec": SPEC, "binary_sha256": sha(binary),
           "inputs": {str(p.relative_to(source)): sha(p) for p in rig_files}, "world": [60, 60]}
    require(not output.exists(), "output directory already exists; preserve it and choose a new path")
    donor_values = load_control(args.schedule, tasks, rig, args) if args.mode in ("replay", "fixed") else None
    fixed = mean_schedule(donor_values) if args.mode == "fixed" else None
    output.mkdir(parents=True)
    dump(output / "task_manifest.json", tasks)
    dump(output / "run_config.json", {"args": vars(args), "rig": rig, "driver_sha256": sha(__file__)})
    history, exposure = [[0.0] * len(tasks)], [0.0] * len(tasks)
    schedule = {"spec": SPEC, "rig": rig, "tasks": tasks, "mode": args.mode, "seed": args.seed,
                "piece_updates": args.piece_updates, "values": [], "complete": False}
    observations, previous = [], None
    previous_common, cumulative_common = set(), set()
    boundary = args.piece_updates - 1
    for index in range(args.pieces):
        if args.mode == "replay":
            values = list(donor_values[index])
        elif args.mode == "fixed":
            values = list(fixed)
        elif index == 0 or args.mode == "all77":
            values = [args.budget / len(tasks)] * len(tasks)
        elif args.mode == "progress":
            values = progress(history, args.window, args.budget)
        else:
            values = rarity(exposure, args.budget)
        require(all(math.isfinite(v) and v >= 0 for v in values), "invalid selector output")
        piece = output / ("piece-%05d" % index)
        seed = piece_seed(args.seed, index)
        prepare(piece, support, tasks, values, seed, boundary, previous)
        command = [str(binary), "-c", "avida.cfg"]
        dump(piece / "command.json", {"cwd": str(piece), "argv": command})
        if args.dry_run:
            print("DRY RUN: prepared piece 1 only; no Avida process executed")
            print("tasks=77 world=60x60 local_exit=" + str(boundary) + " actual_updates=" + str(args.piece_updates))
            print("next pieces require observed counts or a donor schedule; no counts fabricated")
            return
        with (piece / "stdout.log").open("w") as out, (piece / "stderr.log").open("w") as err:
            result = subprocess.run(command, cwd=piece, stdout=out, stderr=err)
        require(result.returncode == 0, "Avida failed; inspect " + str(piece / "stderr.log"))
        count, counts, shares = observe(piece, tasks, boundary)
        previous = piece / "data" / ("population-%d.spop" % boundary)
        require(previous.is_file() and previous.stat().st_size > 0, "saved program population missing")
        history.append(shares)
        exposure = [a + p for a, p in zip(exposure, shares)]
        schedule["values"].append(values)
        offered = [any(row[j] > 0 for row in schedule["values"]) for j in range(len(tasks))]
        current_common, changes = common_changes(shares, counts, previous_common, cumulative_common)
        record = {"piece": index, "global_updates": (index + 1) * args.piece_updates,
                  "local_label": boundary, "seed": seed, "living": count, "counts": counts, "shares": shares,
                  "tasks_present": sum(x > 0 for x in counts), "common_10pct": sum(x >= 0.1 for x in shares),
                  "never_offered_pay_common": sum(p >= 0.1 and not paid for p, paid in zip(shares, offered)),
                  "pay_total": sum(values), "zero_pay": not any(values),
                  "snapshot": str(previous.relative_to(output)), "snapshot_sha256": sha(previous)}
        record.update(changes)
        previous_common = current_common
        cumulative_common |= current_common
        observations.append(record)
        dump(output / "observations.json", observations)
        dump(output / "state.json", {"history": history, "exposure": exposure, "completed_pieces": index + 1})
        dump(output / "schedule.json", schedule)
        print("piece=%d global_updates=%d local_label=%d live=%d present=%d common10=%d pay_total=%.6g" % (
            index + 1, record["global_updates"], boundary, count, record["tasks_present"],
            record["common_10pct"], record["pay_total"]), flush=True)
    schedule["complete"] = True
    dump(output / "schedule.json", schedule)
    dump(output / "fixed_values.json", {"tasks": tasks, "values": mean_schedule(schedule["values"])})
    print("complete pieces=%d actual_updates=%d" % (args.pieces, args.pieces * args.piece_updates))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", required=True, help="read-only pinned Avida git checkout")
    parser.add_argument("--avida", required=True)
    parser.add_argument("--out", required=True, help="new output directory")
    parser.add_argument("--mode", choices=("progress", "archive", "fixed", "replay", "all77"), required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--piece-updates", type=int, default=1000)
    parser.add_argument("--pieces", type=int, default=50)
    parser.add_argument("--window", type=int, default=5)
    parser.add_argument("--budget", type=float, default=7.7)
    parser.add_argument("--schedule", help="complete donor schedule.json for fixed/replay")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    require(args.piece_updates > 0 and args.pieces > 0 and args.window > 0, "lengths/window must be positive")
    require(math.isfinite(args.budget) and 0 < args.budget <= 20, "budget must be in (0,20]")
    require((args.mode in ("replay", "fixed")) == bool(args.schedule), "schedule required only for fixed/replay")
    run(args)


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError, KeyError, subprocess.SubprocessError) as error:
        print("ERROR: " + str(error), file=sys.stderr)
        sys.exit(1)
