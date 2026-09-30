# NOTE (added by Claude, 30 September 2026, log S115): this is the generator
# "make_runs.py" from GPT 6 Astra's reply 04 ("Testing the execution environment
# claim in stock Avida"), copied unchanged from the reply's appendix; only these
# note lines were added above the code. It writes the Avida files for Experiment A
# (four hand-built founder programs checked on Avida's test CPU) and Experiment B
# (twelve continuous 60,000-update runs), then runs one chosen phase.
# Check: "results/S115 Checking the Astra returns/04 Check of reply 04 - ...md".
#!/usr/bin/env python3
"""Create exact Brief 04 inputs; run only the explicitly chosen phase."""
import concurrent.futures as cf
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys

PIN = "47f13dadb547fcf10f620ace60247f38b30b8b16"
TASKS = "NOT NAND AND ORN OR ANDN NOR XOR EQU".split()
VALUES = [1, 1, 2, 2, 3, 3, 4, 4, 5]
OPS = ("nop-A nop-B nop-C if-n-equ if-less if-label mov-head jmp-head "
       "get-head set-flow shift-r shift-l inc dec push pop swap-stk swap "
       "add sub nand h-copy h-alloc h-divide IO h-search").split()
CONFIG = """VERSION_ID 2.14.0
VERBOSITY 0
RANDOM_SEED 4101
MAX_CONCURRENCY 1
WORLD_X 60
WORLD_Y 60
WORLD_GEOMETRY 2
EVENT_FILE events.cfg
ENVIRONMENT_FILE environment.cfg
ANALYZE_FILE analyze.cfg
DATA_DIR data
COPY_MUT_PROB 0.0075
COPY_INS_PROB 0
COPY_DEL_PROB 0
COPY_UNIFORM_PROB 0
COPY_SLIP_PROB 0
POINT_MUT_PROB 0
DIV_MUT_PROB 0
DIV_INS_PROB 0
DIV_DEL_PROB 0
DIV_UNIFORM_PROB 0
DIV_SLIP_PROB 0
DIVIDE_MUT_PROB 0
DIVIDE_INS_PROB 0.05
DIVIDE_DEL_PROB 0.05
DIVIDE_UNIFORM_PROB 0
DIVIDE_SLIP_PROB 0
DIVIDE_POISSON_MUT_MEAN 0
DIVIDE_POISSON_INS_MEAN 0
DIVIDE_POISSON_DEL_MEAN 0
DIVIDE_POISSON_SLIP_MEAN 0
INJECT_MUT_PROB 0
INJECT_INS_PROB 0
INJECT_DEL_PROB 0
PARENT_MUT_PROB 0
META_COPY_MUT 0
BIRTH_METHOD 0
PREFER_EMPTY 1
AVE_TIME_SLICE 30
SLICING_METHOD 1
TEST_CPU_TIME_MOD 20
""" + "INSTSET heads_default:hw_type=0\n" + "".join(
    "INST " + op + "\n" for op in OPS)
FIELDS = ("name viable length merit gest_time fitness copy_length exe_length "
          + " ".join("task." + str(i) for i in range(9))
          + " sequence env_input.0 env_input.1 env_input.2")
SNAPSHOTS = [0, 19000, 20000, 21000, 39000, 40000, 41000, 60000]

def put(path, text):
    path.write_text(text, encoding="utf-8")

def environment(values):
    return "".join(f"REACTION {t} {t.lower()} process:value={v}:type=pow "
                   "requisite:max_count=1\n" for t, v in zip(TASKS, values))

def config(seed, assay=False):
    s = CONFIG.replace("RANDOM_SEED 4101", f"RANDOM_SEED {seed}")
    if assay:
        for key, old in [("COPY_MUT_PROB", "0.0075"),
                         ("DIVIDE_INS_PROB", "0.05"),
                         ("DIVIDE_DEL_PROB", "0.05")]:
            s = s.replace(f"{key} {old}\n", f"{key} 0\n")
    return s

def founders():
    ancestor = (["h-alloc", "h-search", "nop-C", "nop-A", "mov-head"]
                + ["nop-C"] * 86
                + ["h-search", "h-copy", "if-label", "nop-C", "nop-A",
                   "h-divide", "mov-head", "nop-A", "nop-B"])
    assert len(ancestor) == 100
    a = ancestor.copy()
    a[20:34] = "IO nop-B IO nop-C nand nop-A push nop-B pop nop-C nand nop-B IO nop-B".split()
    c = a.copy()
    c[25] = "nop-C"
    result = {"A": a, "C": c}
    for name, tokens in list(result.items()):
        probe = tokens.copy()
        probe[33] = "nop-A"
        result[name + "_probe"] = probe
    return {n: "#inst_set heads_default\n#hw_type 0\n\n" + "\n".join(v) + "\n"
            for n, v in result.items()}

def events(schedule):
    lines = ["u begin InjectRange founder.org 0 3600"]
    for action in ["PrintTasksData", "PrintCountData", "PrintAverageData",
                   "PrintTimeData", "PrintTotalsData"]:
        lines.append(f"u 0:100:60000 {action}")
    lines.append("u 0:1000:60000 SavePopulation filename=detail:save_historic=0")
    for update in [20000, 40000]:
        values = [0] * 8 + [5] if schedule == "switch" and update == 20000 else VALUES
        for task, value in zip(TASKS, values):
            lines.append(f"u {update} SetReactionValue {task} {value}")
    lines.append("u 60000 Exit")
    return "\n".join(lines) + "\n"

def make(root):
    root.mkdir(parents=True, exist_ok=False)
    inputs = founders()
    assay = root / "A_assay"
    assay.mkdir()
    put(assay / "avida.cfg", config(1701, True))
    put(assay / "environment.cfg", environment([0] * 9))
    put(assay / "events.cfg", "u 0 Exit\n")
    for name, text in inputs.items():
        put(assay / (name + ".org"), text)
    lines = [f"LOAD_ORGANISM {n}.org" for n in inputs]
    lines += ["RECALCULATE 0 -1 0", f"DETAIL fixed.dat {FIELDS}", "TRACE traces/ 0 -1 0"]
    triple = [252908703, 856220990, 1432502763]
    for i in range(3):
        rotated = triple[i:] + triple[:i]
        lines += ["RECALCULATE 0 -1 0 " + " ".join(map(str, rotated)),
                  f"DETAIL rotation-{i}.dat {FIELDS}"]
    for i in range(32):
        lines += ["RECALCULATE 0 -1 1", f"DETAIL random-{i:02d}.dat {FIELDS}"]
    put(assay / "analyze.cfg", "\n".join(lines) + "\n")
    for label, values in [("graded", VALUES), ("equ", [0] * 8 + [5])]:
        baseline = root / ("A_baseline_" + label)
        baseline.mkdir()
        put(baseline / "avida.cfg", config(1701, True))
        put(baseline / "environment.cfg", environment(values))
        put(baseline / "events.cfg", "u 0 Exit\n")
        for name, text in inputs.items():
            put(baseline / (name + ".org"), text)
        put(baseline / "analyze.cfg", "\n".join(
            [f"LOAD_ORGANISM {n}.org" for n in inputs]
            + ["RECALCULATE 0 -1 0", f"DETAIL fixed.dat {FIELDS}"]) + "\n")
    for name in ["A", "C"]:
        for schedule in ["fixed", "switch"]:
            for seed in [4101, 4102, 4103]:
                job = root / f"B_{name}_{schedule}_{seed}"
                job.mkdir()
                put(job / "avida.cfg", config(seed))
                put(job / "environment.cfg", environment(VALUES))
                put(job / "events.cfg", events(schedule))
                put(job / "founder.org", inputs[name])
                put(job / "analyze.cfg", "# Offline common assays use separate folders.\n")
    manifest = {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
                for p in sorted(root.rglob("*")) if p.is_file()}
    put(root / "input_manifest.json", json.dumps({"source_commit": PIN,
        "sha256": manifest}, indent=2) + "\n")
    print(root)

def execute(job, binary, analyze=False):
    log = job / ("assay.log" if analyze else "run.log")
    command = [str(binary), "-c", "avida.cfg"] + (["-a"] if analyze else [])
    with log.open("x", encoding="utf-8") as output:
        result = subprocess.run(command, cwd=job, stdout=output,
                                stderr=subprocess.STDOUT, check=False)
    if result.returncode:
        raise RuntimeError(f"Run failed: {job}; preserve {log}")
    return str(job)

def gate(root):
    files = [root / "A_assay" / "data" / "fixed.dat"]
    files += sorted((root / "A_assay" / "data").glob("rotation-*.dat"))
    files += sorted((root / "A_assay" / "data").glob("random-*.dat"))
    if len(files) != 36:
        raise RuntimeError("Expected fixed, three rotation, and 32 random outputs")
    files += [root / ("A_baseline_" + label) / "data" / "fixed.dat"
              for label in ["graded", "equ"]]
    for file in files:
        rows = {}
        for line in file.read_text().splitlines():
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            cells = line.split()
            name = cells[0].removesuffix(".org")
            rows[name] = [float(x) for x in cells[1:17]]
        if set(rows) != {"A", "C", "A_probe", "C_probe"}:
            raise RuntimeError(f"Unexpected assay rows: {file}")
        for name, values in rows.items():
            expected = [0] * 9
            if name in ("A", "C"):
                expected[0] = 1
            elif name == "A_probe":
                expected[1] = 1
            if values[0] != 1 or values[1] != 100 or [int(x > 0) for x in values[7:]] != expected:
                raise RuntimeError(f"Frozen prediction failed: {file}, {name}")
        if rows["A"][:7] != rows["C"][:7]:
            raise RuntimeError(f"Unmatched baseline: {file}")

def parallel(jobs, binary, analyze=False):
    with cf.ThreadPoolExecutor(max_workers=3) as pool:
        futures = [pool.submit(execute, job, binary, analyze) for job in jobs]
        errors = []
        for future in cf.as_completed(futures):
            try:
                print(future.result())
            except Exception as error:
                errors.append(str(error))
        if errors:
            raise RuntimeError("\n".join(errors))

def snapshots(root, binary):
    jobs = []
    for run in sorted(root.glob("B_*")):
        for update in SNAPSHOTS:
            src = run / "data" / f"detail-{update}.spop"
            if not src.is_file():
                raise RuntimeError(f"Missing snapshot: {src}")
            job = root / "common_assays" / run.name / str(update)
            job.mkdir(parents=True, exist_ok=False)
            shutil.copyfile(src, job / "population.spop")
            put(job / "avida.cfg", config(1701, True))
            put(job / "environment.cfg", environment([0] * 9))
            put(job / "events.cfg", "u 0 Exit\n")
            fields = "id num_cpus viable length merit gest_time fitness " + " ".join(
                f"task.{i}:binary" for i in range(9)) + " sequence"
            put(job / "analyze.cfg", "LOAD population.spop\nFILTER num_cpus > 0\n"
                "RECALCULATE 0 -1 0\nDETAIL common.dat " + fields + "\n")
            jobs.append(job)
    parallel(jobs, binary, True)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        make(Path(sys.argv[1]).resolve())
    elif len(sys.argv) == 4:
        phase, directory, executable = sys.argv[1:]
        root, binary = Path(directory).resolve(), Path(executable).resolve()
        if phase == "--assay":
            execute(root / "A_assay", binary, True)
            execute(root / "A_baseline_graded", binary, True)
            execute(root / "A_baseline_equ", binary, True)
            gate(root)
        elif phase == "--run":
            gate(root)
            parallel(sorted(root.glob("B_*")), binary)
        elif phase == "--snapshots":
            snapshots(root, binary)
        else:
            raise SystemExit("Unknown phase")
    else:
        raise SystemExit("make_runs.py OUTPUT | --assay/--run/--snapshots OUTPUT AVIDA")
