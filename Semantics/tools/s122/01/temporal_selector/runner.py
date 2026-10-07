#!/usr/bin/env python3
"""Run stock Avida in restart-matched 1,000-update pieces. No C++ patch."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import shutil
import subprocess
from pathlib import Path

from assay import COMMIT, INPUTS, ORDERS, TASKS, assay, atomic_json, digest, environment, execute, prepare, table
from selector import Selector, UNITS


def piece_seed(master, piece, stream):
    message = f"temporal-selector-v1:{master}:{piece}:{stream}".encode()
    return 1 + int.from_bytes(hashlib.sha256(message).digest()[:8], "big") % 2147483646


def cell_programs(path):
    mapping = {}
    for row in table(path):
        count = int(row.get("num_units", row.get("num_cpus", 0)))
        if count == 0:
            continue
        cells = row["cells"].split(",")
        if len(cells) != count:
            raise ValueError("Cell list does not match saved multiplicity")
        for cell in cells:
            if cell in mapping:
                raise ValueError("Duplicate occupied cell in saved program population")
            mapping[cell] = row["sequence"]
    return mapping


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--avida", required=True, type=Path)
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--out", required=True, type=Path)
    parser.add_argument("--seed", required=True, type=int)
    parser.add_argument("--arm", default="full",
                        choices=["full", "memoryless", "replay", "fixed"] + ["no_" + u for u in UNITS])
    parser.add_argument("--pieces", type=int, default=50)
    parser.add_argument("--width", type=int, default=60)
    parser.add_argument("--height", type=int, default=60)
    parser.add_argument("--donor", type=Path, help="Completed full-arm run directory for replay/fixed")
    parser.add_argument("--resume", action="store_true")
    args = parser.parse_args()
    if args.pieces < 1 or args.width < 1 or args.height < 1:
        parser.error("Pieces and world dimensions must be positive")
    args.source, args.avida, args.out = args.source.resolve(), args.avida.resolve(), args.out.resolve()
    source_commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=args.source, text=True).strip()
    if source_commit != COMMIT:
        parser.error("Source checkout is not pinned commit " + COMMIT)
    tracked = subprocess.check_output(["git", "status", "--porcelain", "--untracked-files=no"],
                                     cwd=args.source, text=True).strip()
    if tracked:
        parser.error("Pinned source has tracked modifications")
    disabled = [args.arm[3:]] if args.arm.startswith("no_") else []
    selector = Selector(len(TASKS), disabled=disabled)
    manifest = dict(version=1, selector_spec="1.2", source_commit=source_commit, binary_sha256=digest(args.avida),
                    stock_config_sha256=digest(args.source / "avida-core/support/config/avida.cfg"),
                    tasks=TASKS, eligible=selector.eligible, inputs=INPUTS, orders=ORDERS,
                    seed=args.seed, arm=args.arm, pieces=args.pieces,
                    width=args.width, height=args.height, piece_updates=1000,
                    code_sha256={name: digest(Path(__file__).with_name(name))
                                 for name in ("runner.py", "assay.py", "selector.py")},
                    assay="neutral rewards; six orders; completed first-replication task records; time factor 20")
    donor_pay = None
    if args.arm in ("replay", "fixed"):
        if args.donor is None:
            parser.error("Replay/fixed require --donor")
        donor = json.loads((args.donor / "manifest.json").read_text())
        donor_pay = json.loads((args.donor / "schedule.json").read_text())
        for key in ("tasks", "eligible", "pieces", "width", "height", "binary_sha256", "inputs", "orders",
                    "piece_updates", "stock_config_sha256", "source_commit", "code_sha256"):
            if donor[key] != json.loads(json.dumps(manifest[key])):
                parser.error("Donor differs in " + key)
        if donor["seed"] == args.seed or donor["arm"] != "full" or len(donor_pay) != args.pieces:
            parser.error("Donor must be a completed full arm with another seed")
        manifest["donor_manifest_sha256"] = digest(args.donor / "manifest.json")
        manifest["donor_schedule_sha256"] = digest(args.donor / "schedule.json")
        if args.arm == "fixed":
            mean = [math.fsum(row[j] for row in donor_pay) / args.pieces for j in range(len(TASKS))]
            donor_pay = [mean[:] for _ in range(args.pieces)]
    # Normalize tuples to JSON's arrays before comparing resume manifests.
    manifest = json.loads(json.dumps(manifest))
    args.out.mkdir(parents=True, exist_ok=True)
    manifest_path = args.out / "manifest.json"
    if manifest_path.exists():
        if not args.resume or json.loads(manifest_path.read_text()) != manifest:
            parser.error("Existing run requires --resume with identical settings")
    else:
        atomic_json(manifest_path, manifest)
    pay, previous, schedule = selector.initial_pay(), None, []
    for piece in range(args.pieces):
        directory = args.out / f"piece_{piece:03d}"
        checkpoint = directory / "complete.json"
        if checkpoint.exists():
            saved = json.loads(checkpoint.read_text())
            pay = saved["next_pay"]
            selector.load(saved["selector_state"])
            previous = directory / "data/population-999.spop"
            if digest(previous) != saved["snapshot_sha256"]:
                raise ValueError("Completed snapshot changed")
            schedule.append(saved["applied_pay"])
            continue
        if directory.exists():
            raise RuntimeError(f"Partial piece retained at {directory}; move it aside before --resume")
        if donor_pay is not None:
            pay = donor_pay[piece]
        if (len(pay) != len(TASKS) or any(not math.isfinite(v) or v < 0 for v in pay)
                or abs(sum(pay) - 18) > 1e-10
                or any(pay[j] != 0 for j in range(len(TASKS)) if j not in selector.eligible)):
            raise ValueError("Invalid nominal pay")
        seed = piece_seed(args.seed, piece, "world")
        assay_seed = piece_seed(args.seed, piece, "assay")
        prepare(args.source, directory, {"RANDOM_SEED": seed, "WORLD_X": args.width,
                                        "WORLD_Y": args.height, "VERBOSITY": 1})
        (directory / "environment.cfg").write_text(environment(pay))
        inject = "u begin Inject default-heads.org"
        if previous is not None:
            shutil.copy2(previous, directory / "input.spop")
            inject = "u begin LoadPopulation input.spop"
        events = ["u begin SetEnvironmentInputs " + " ".join(map(str, INPUTS)), inject,
                  "u begin SavePopulation filename=initial:save_historic=0",
                  "u 999 PrintTimeData", "u 999 PrintCountData",
                  "u 999 SavePopulation filename=population:save_historic=0", "u 999 Exit"]
        (directory / "events.cfg").write_text("\n".join(events) + "\n")
        execute(args.avida, directory)
        labels = [int(x) for x in re.findall(r"(?m)^UD:\s*(\d+)", (directory / "stdout.log").read_text())]
        if labels != list(range(1000)):
            raise RuntimeError("Piece did not execute update labels 0 through 999 exactly once")
        seed_line = re.search(r"(?m)^Random Seed:.*$", (directory / "stdout.log").read_text())
        snapshot = directory / "data/population-999.spop"
        if previous is not None and cell_programs(previous) != cell_programs(directory / "data/initial--1.spop"):
            raise ValueError("Reload changed occupied cells or program multiplicities")
        obs = assay(args.avida, args.source, snapshot, directory / "assay", assay_seed)
        if args.arm == "memoryless":
            selector = Selector(len(TASKS))
        response = selector.step(obs) if donor_pay is None else {"pay": pay, "diagnostics": {}}
        eligible = set(selector.eligible)
        metrics = dict(piece=piece, completed_updates=1000*(piece+1), seed=seed, assay_seed=assay_seed,
                       program_population=obs["population_size"], world_common=sum(v >= .1 for v in obs["p"]),
                       all_order_common=sum(v >= .1 for v in obs["q"]),
                       never_paid_common=sum(obs["q"][j] >= .1 for j in range(len(TASKS)) if j not in eligible),
                       latches=sum(response["diagnostics"].get("latch", [])),
                       releases=sum(response["diagnostics"].get("release", [])))
        saved = dict(metrics=metrics, applied_pay=pay, next_pay=response["pay"],
                     avida_seed_line=seed_line.group(0) if seed_line else None,
                     selector_state=selector.state, diagnostics=response["diagnostics"],
                     snapshot_sha256=digest(snapshot))
        atomic_json(checkpoint, saved)
        schedule.append(pay)
        atomic_json(args.out / "schedule.json", schedule)
        print(json.dumps(metrics, sort_keys=True), flush=True)
        pay, previous = response["pay"], snapshot
    atomic_json(args.out / "schedule.json", schedule)


if __name__ == "__main__":
    main()
