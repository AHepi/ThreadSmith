"""Stock Avida 47f13dad: abundance-weighted, six-input-order cold-start assay."""
from __future__ import annotations

import hashlib
import itertools
import json
import re
import shutil
import subprocess
from pathlib import Path

COMMIT = "47f13dadb547fcf10f620ace60247f38b30b8b16"
INPUTS = (0x0F13149F, 0x3308E53E, 0x556241EB)
ORDERS = tuple(itertools.permutations(range(3)))
TASKS = ("not nand and orn or andn nor xor equ".split()
         + ["logic_3" + a + b for a, b in itertools.product("ABC", "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
            if a + b <= "CP"])


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def atomic_json(path, value):
    path = Path(path)
    temp = path.with_name(path.name + ".tmp")
    temp.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")
    temp.replace(path)


def table(path):
    """Read Avida's explicit #format header; never assume .spop column numbers."""
    fields, rows = None, []
    for line in Path(path).read_text().splitlines():
        if line.startswith("#format "):
            fields = line.split()[1:]
        elif line.strip() and not line.lstrip().startswith("#"):
            values = line.split()
            if fields is None or len(values) != len(fields):
                raise ValueError(f"Malformed table: {path}")
            rows.append(dict(zip(fields, values)))
    if fields is None:
        raise ValueError(f"Missing format header: {path}")
    return rows


def environment(pay):
    if len(pay) != len(TASKS):
        raise ValueError("Expected 77 task rewards")
    return "".join(f"REACTION T{i:02d} {task} process:value={value:.17g}:type=pow "
                   "requisite:max_count=1\n"
                   for i, (task, value) in enumerate(zip(TASKS, pay)))


def prepare(source, dest, settings):
    """Use the pinned stock configuration and its 26-instruction heads set."""
    source, dest = Path(source), Path(dest)
    dest.mkdir(parents=True, exist_ok=True)
    support = source / "avida-core/support/config"
    cfg = (support / "avida.cfg").read_text()
    for key, value in settings.items():
        pattern = rf"(?m)^{re.escape(key)}\s+[^\n]*$"
        if not re.search(pattern, cfg):
            raise ValueError(f"Setting absent from stock config: {key}")
        cfg = re.sub(pattern, f"{key} {value}", cfg)
    (dest / "avida.cfg").write_text(cfg)
    for name in ("instset-heads.cfg", "default-heads.org"):
        shutil.copy2(support / name, dest / name)


def execute(binary, cwd, analyze=False):
    argv = [str(Path(binary).resolve()), "-c", "avida.cfg"]
    if analyze:
        argv.append("-a")
    cwd = Path(cwd)
    atomic_json(cwd / "command.json", argv)
    with (cwd / "stdout.log").open("w") as stdout, (cwd / "stderr.log").open("w") as stderr:
        result = subprocess.run(argv, cwd=cwd, stdout=stdout, stderr=stderr, check=False)
    if result.returncode:
        raise RuntimeError(f"Avida exit {result.returncode}; see {cwd}/stderr.log and stdout.log")
    for log in ("stdout.log", "stderr.log"):
        if re.search(r"(?im)^\s*error\s*:", (cwd / log).read_text()):
            raise RuntimeError(f"Avida reported an error in {cwd / log}")


def assay(binary, source, snapshot, dest, seed):
    """Count tasks recorded at first replication; does not count all outputs.

    All orders use the same three numbers, fixed neutral rewards, one trial,
    and stock TEST_CPU_TIME_MOD=20. No live task counters enter the result.
    """
    dest = Path(dest)
    prepare(source, dest, {"RANDOM_SEED": seed, "WORLD_X": 1, "WORLD_Y": 1,
                          "VERBOSITY": 1, "TEST_CPU_TIME_MOD": 20})
    shutil.copy2(snapshot, dest / "population.spop")
    (dest / "environment.cfg").write_text(environment([0.0] * len(TASKS)))
    (dest / "events.cfg").write_text("")
    lines = ["LOAD population.spop", "FILTER num_units > 0"]
    for order in ORDERS:
        values = " ".join(str(INPUTS[i]) for i in order)
        name = "order_" + "".join(map(str, order)) + ".dat"
        lines += [f"RECALCULATE 0 -1 0 {values}",
                  f"DETAIL {name} id num_units viable task_list sequence"]
    (dest / "analyze.cfg").write_text("\n".join(lines) + "\n")
    execute(binary, dest, analyze=True)
    original = {row["id"]: int(row.get("num_units", row.get("num_cpus", 0)))
                for row in table(snapshot)
                if int(row.get("num_units", row.get("num_cpus", 0))) > 0}
    if not original or sum(original.values()) <= 0:
        raise RuntimeError("Empty saved program population")
    by_order = []
    for order in ORDERS:
        filename = "order_" + "".join(map(str, order)) + ".dat"
        rows = table(dest / "data" / filename)
        result = {row["id"]: row for row in rows}
        if len(result) != len(rows) or set(result) != set(original):
            raise ValueError("Assay IDs do not match saved program population")
        for key, row in result.items():
            if int(row["num_units"]) != original[key] or len(row["task_list"]) != len(TASKS):
                raise ValueError("Assay abundance or task catalog mismatch")
        by_order.append(result)
    n, k = sum(original.values()), len(TASKS)
    p, q = [0.0] * k, [0.0] * k
    cooc = [[0.0] * k for _ in range(k)]
    programs = []
    for key, count in original.items():
        records = [result[key] for result in by_order]
        if len({row["sequence"] for row in records}) != 1:
            raise ValueError("Program sequence changed across orders")
        bits = [[c != "0" for c in row["task_list"]] for row in records]
        robust = [all(order[j] for order in bits) for j in range(k)]
        active = [j for j in range(k) if robust[j]]
        for j in range(k):
            p[j] += count * bits[0][j]
            q[j] += count * robust[j]
        for j in active:
            for l in active:
                if j != l:
                    cooc[j][l] += count
        programs.append({"id": key, "count": count, "orders": bits,
                         "robust": robust, "replication_test": [int(r["viable"]) for r in records]})
    obs = {"p": [v / n for v in p], "q": [v / n for v in q],
           "cooc": [[v / n for v in row] for row in cooc], "population_size": n,
           "distinct_program_records": len(original)}
    atomic_json(dest / "programs.json", programs)
    atomic_json(dest / "observation.json", obs)
    return obs
