# NOTE (added by Claude, log S115): this file is 'probe_task_audit.py', copied unchanged from the appendix of
# GPT 6 Astra's reply 01 ('tests/S115 Returns from GPT 6 Astra/01 Return - measuring what is learned,
# with stock Avida only.md'). Only these note lines were added. It has not been run on S113's data;
# see 'results/S115 Checking the Astra returns/01 Check of reply 01 - measuring what is learned.md'.
#!/usr/bin/env python3
"""Generate stock-Avida 47f13dad probe environments and analyze scripts.

This is an external file generator, not an Avida modification. Each observation
is a fresh test-CPU execution. Existing run files and snapshots are read only.
Use --run to execute the generated commands sequentially (one Avida process).
All task claims are source-checked; an unrun profile is not a measured result.
"""
import argparse
import csv
import hashlib
import json
from pathlib import Path
import random
import re
import shlex
import subprocess
import time

COMMIT = "47f13dadb547fcf10f620ace60247f38b30b8b16"
BOOL = "not nand and orn or andn nor xor equ".split()
# Every parameter here is a chosen probe specification, not a task's identity.
# These profiles run separately because loaders can change buffer capacities.
PARAMS = {
    "matchstr": "string=01011010,partial=0,binary=0",
    "match_number": "target=12345,threshold=0,halflife=1",
    "matchprodstr": "string=01011010,partial=0,binary=0,tag=-1",
    "sort_inputs": "size=3,direction=0,contiguous=1,halflife=1",
    "fibonacci_seq": "target=8,penalty=0",
    **{n: "threshold=0,halflife=1" for n in
       "mult div log log2 log10 sqrt sine cosine".split()},
    "optimize": "function=22,binary=1,varlength=8,numvars=1,maxFx=8,minFx=0,thresh=0",
    "all-ones": "length=1",
    # length=1 avoids reading output-buffer entries before they are written.
    "royal-road": "length=1,block_count=1",
    "royal-road-wd": "length=1,block_count=1,width=1,height=1",
}
ALIASES = {n + "_dup": n for n in ["echo", *BOOL]}
ALIASES.update({"math_2AX": "math_2AT", "math_2AN": "add",
                "math_2AO": "sub", "math_2AY": "math_2AS",
                "math_3AH": "add3", "matchprodstr": "matchstr"})
CONTEXT = {
    "xor-max": "Reads resources, changes reaction resource; requires a resource profile.",
    "nand-resourceDependent": "Requires named pheromone resource and population resource table; cutoff 100.",
    "nor-resourceDependent": "Requires named pheromone resource and population resource table; cutoff 100.",
    "comm_echo": "Requires actual neighbor input buffers; test CPU has no neighbors.",
    "comm_not": "Requires actual neighbor input buffers; test CPU has no neighbors.",
    "sg_path_traversal": "Requires STATE_GRID, pathlen/sgname/poison and state-grid instructions absent from heads.",
    "form-group": "Reads population group sizes; isolated test CPU supplies no populated social context.",
    "form-group-id": "Requires group membership, group ID and population group sizes.",
    "live-on-patch-id": "Reads opinion attribute; relevant state-setting instruction absent from heads.",
    "collect-odd-cell": "Tests cell-ID parity; test CPU cell ID is -1, a misleading positive is possible.",
    "perfect_strings": "Reads stored-string state rather than generic IO; production context absent.",
    "event_killed": "Reads event-killed flag; event world and relevant instructions absent.",
    "consume-public-good": "Reads and modifies living neighboring programs; no such test-CPU population.",
    "ai-display-cost": "Reads lyse-display flag; relevant state-setting instruction absent from heads.",
    "produce-public-good": "Reads explosion/public-good phenotype state; relevant instructions absent from heads.",
    "exploded": "Reads explosion flag; explosion instruction absent from heads.",
    "exploded2": "Reads second explosion flag; explosion instruction absent from heads.",
    "opinion_is": "Reads opinion attribute; relevant state-setting instruction absent from heads.",
}


def function_body(source, function):
    m = re.search(r"(?:void|double) cTaskLib::" + re.escape(function) + r"\(", source)
    if not m:
        raise ValueError("Cannot locate function " + function)
    start = source.index("{", m.end())
    depth = 1
    end = start + 1
    while depth:
        depth += (source[end] == "{") - (source[end] == "}")
        end += 1
    return source[start:end], source[:m.start()].count("\n") + 1


def audit(source):
    registration = source[:source.index("void cTaskLib::NewTask")]
    found = list(re.finditer(r'name == "([^"]+)"', registration))
    rows = []
    for k, m in enumerate(found):
        name = m.group(1)
        chunk = registration[m.end():found[k + 1].start() if k + 1 < len(found) else len(registration)]
        load = re.search(r"(Load_\w+)\(name", chunk)
        call = re.search(r"&cTaskLib::(Task_\w+)", chunk)
        loader, args = "", []
        if load:
            loader = load.group(1)
            body, _ = function_body(source, loader)
            call = re.search(r"&cTaskLib::(Task_\w+)", body)
            args = re.findall(r'schema.AddEntry\("(\w+)"\s*,\s*\d+\s*,\s*([^;]+)\);', body)
        handler = call.group(1) if call else ""
        if not handler:
            raise ValueError("No handler for " + name)
        _, handler_line = function_body(source, handler)
        core = (name in ["echo", "echo_dup", "add", "add3", "sub", "dontcare"] or
                name.removesuffix("_dup") in BOOL or name.startswith(("logic_", "math_", "fib_")))
        profile = "core" if core else name if name in PARAMS else ""
        if name == "dontcare":
            status, reason = "control", "Always returns one when evaluated; exclude from capability richness."
        elif name.startswith("fib_"):
            status, reason = "constant_output", "Checks a fixed number after input; not an input-to-output function."
        elif name == "all-ones":
            status, reason = "output_domain_required", "Raw output/length can be negative and fail Avida's nonnegative-quality assertion. Disabled by default."
        elif name in ALIASES:
            status, reason = "alias", "Same detector behavior as canonical within this three-input profile; do not count twice."
        elif core:
            status, reason = "supported", "Source detector uses input/output buffers; fixed low input domain in this profile."
        elif name in PARAMS:
            status, reason = "parameterized", "Fresh isolated execution with the explicit parameters listed; interpretation is profile-specific."
        else:
            status = "context_missing"
            reason = CONTEXT.get(name)
            if name.startswith("eat-target"):
                reason = "Requires forage-target state; target-setting instruction absent from standard heads; fresh default is -1."
            elif name.startswith("move"):
                reason = "Requires population movement/location/event state; test interface returns cell -1, no deme, and Move false; detector may be vacuous or unsafe."
            if reason is None:
                raise ValueError("Unclassified task: " + name)
        if name == "fibonacci_seq":
            reason = "Eight-step prefix, fresh state; max_count=8 stops evaluation before large Fibonacci sums. task count 8 denotes full prefix."
        if name in ["matchstr", "matchprodstr", "sort_inputs", "optimize", "royal-road", "royal-road-wd"]:
            reason += " Nonzero count alone is not exact completion; quality is accumulated, not a maximum."
        if name.startswith("royal-road"):
            reason += " Length-one probe only; larger lengths can read unwritten output-buffer entries."
        if name == "optimize":
            reason += " Detector returns 0.001 even on failure; task count measures opportunities, not success."
        rows.append(dict(name=name, profile=profile, task_index="", status=status,
                         canonical=ALIASES.get(name, name), args=PARAMS.get(name, ""),
                         default_enabled=bool(profile) and name != "all-ones", reason=reason,
                         source_status="checked", loader=loader, handler=handler,
                         registration_line=registration[:m.start()].count("\n") + 1,
                         handler_line=handler_line, argument_schema=args))
    if len(rows) != 214 or len({r["name"] for r in rows}) != 214:
        raise ValueError("Expected exactly 214 names at the pinned commit")
    return rows


def write_tsv(path, rows, fields):
    with path.open("w", newline="") as f:
        w = csv.DictWriter(f, fields, delimiter="\t", extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def safe_path(path):
    path = Path(path).resolve()
    if re.search(r"\s|[#$]", str(path)):
        raise ValueError("Avida analyze paths must have no spaces, # or $: " + str(path))
    return path


def triples(count, seed, high=False):
    rng = random.Random(seed)
    result = []
    for i in range(count):
        if high:
            values = [(mask << 24) | rng.randrange(1 << 24) for mask in [15, 51, 85]]
        else:
            # Place all 8 Boolean cases in low bits, then vary bit order,
            # input-channel order, and two additional bits. All values 15..1023.
            bit_order = list(range(8))
            rng.shuffle(bit_order)
            values = [sum(((mask >> j) & 1) << bit_order[j] for j in range(8)) |
                      (rng.randrange(4) << 8) for mask in [15, 51, 85]]
        rng.shuffle(values)
        patterns = {sum(((v >> b) & 1) << j for j, v in enumerate(values)) for b in range(32)}
        assert patterns == set(range(8)) and len(set(values)) == 3
        if not high:
            assert all(3 <= v <= 1023 and v != 7 for v in values)
        result.append(values)
    return result


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--source", required=True, help="Pinned Avida source checkout")
    p.add_argument("--run-dir", required=True, help="Original run folder (instruction-set/config dependencies)")
    p.add_argument("--config", default="avida.cfg")
    p.add_argument("--snapshot", nargs=3, action="append", required=True, metavar=("LABEL", "UPDATE", "PATH"))
    p.add_argument("--out", required=True, help="New output directory; must not already exist")
    p.add_argument("--inputs", type=int, default=8)
    p.add_argument("--seed", type=int, default=20260930)
    p.add_argument("--avida", default="avida", help="Executable path or name on PATH")
    p.add_argument("--profiles", default="core", help="core, safe, all, or comma-separated profile names; safe includes 16 parameter profiles and logic_high")
    p.add_argument("--run", action="store_true", help="Execute selected profiles sequentially, preserving logs and first outputs")
    a = p.parse_args()
    if a.inputs < 2:
        p.error("Use at least two input triples")
    src, run_dir, out = map(safe_path, [a.source, a.run_dir, a.out])
    config = safe_path(run_dir / a.config)
    source_path = src / "avida-core/source/main/cTaskLib.cc"
    source = source_path.read_text()
    # Refuse silent use of a different revision when this is a Git checkout.
    head = subprocess.run(["git", "-C", str(src), "rev-parse", "HEAD"], text=True, capture_output=True)
    if head.returncode == 0 and head.stdout.strip() != COMMIT:
        p.error("Source checkout must be " + COMMIT)
    if not config.is_file():
        p.error("Missing config: " + str(config))
    snapshots = []
    for label, update, path in a.snapshot:
        if not re.fullmatch(r"[A-Za-z0-9_-]+", label):
            p.error("Labels may contain letters, digits, underscores, hyphens")
        path = safe_path(path)
        if not path.is_file():
            p.error("Missing snapshot: " + str(path))
        snapshots.append(dict(label=label, update=int(update), path=str(path)))
    if len({s["label"] for s in snapshots}) != len(snapshots):
        p.error("Snapshot labels must be unique")
    rows = audit(source)
    profiles = {}
    for row in rows:
        if row["profile"]:
            profile_rows = profiles.setdefault(row["profile"], [])
            row["task_index"] = len(profile_rows)
            profile_rows.append(row)
    # This companion isolates Boolean transfer to original-size input numbers,
    # so arithmetic detectors cannot overflow in the high-range execution.
    profiles["logic_high"] = []
    for row in rows:
        if row["name"] in BOOL or row["name"].startswith("logic_"):
            r = dict(row, profile="logic_high", task_index=len(profiles["logic_high"]))
            r["reason"] = "Boolean-only companion with original-size inputs; separate magnitude-transfer profile."
            profiles["logic_high"].append(r)
    if a.profiles == "safe":
        selected = [n for n in profiles if n != "all-ones"]
    elif a.profiles == "all":
        selected = list(profiles)
    else:
        selected = a.profiles.split(",")
    if set(selected) - profiles.keys():
        p.error("Unknown profiles: " + ", ".join(set(selected) - profiles.keys()))
    out.mkdir(parents=True, exist_ok=False)
    (out / "events.cfg").write_text("# Analyze-only; no population is advanced.\n")
    write_tsv(out / "snapshots.tsv", snapshots, ["label", "update", "path"])
    tsv_rows = [*rows, *profiles["logic_high"]]
    write_tsv(out / "tasks.tsv", tsv_rows, ["profile", "task_index", "name", "status", "canonical", "args", "reason", "default_enabled"])
    (out / "task_audit.json").write_text(json.dumps(dict(source_commit=COMMIT,
        source_sha256=hashlib.sha256(source.encode()).hexdigest(), task_names=rows,
        note="214 names audited, not 214 interchangeable capabilities. Runtime status is in run_status.json after --run."), indent=2) + "\n")
    # DETAIL drops .N suffixes in #format, so preserve the requested schema
    # separately. `parents` is omitted: the stock loader does not retain its
    # original string, so it prints an empty token and breaks whitespace rows.
    base = "id num_units viable length gest_time fitness update_born parent_id depth sequence hw_type inst_set env_input.0 env_input.1 env_input.2"
    input_rows, schema_rows, commands = [], [], []
    for profile, task_rows in profiles.items():
        d = out / profile
        d.mkdir()
        result_dir = out / "results" / profile
        result_dir.mkdir(parents=True)
        env_lines = ["# Source-checked at " + COMMIT]
        for row in task_rows:
            spec = row["name"] + (":" + row["args"] if row["args"] else "")
            req = " requisite:max_count=8" if row["name"] == "fibonacci_seq" else ""
            env_lines.append(f"REACTION P{row['task_index']:03d} {spec} process:value=0:type=pow{req}")
        env = d / "environment.cfg"
        env.write_text("\n".join(env_lines) + "\n")
        values = triples(a.inputs, a.seed, high=profile == "logic_high")
        for i, v in enumerate(values):
            input_rows.append(dict(profile=profile, input_id=i, input0=v[0], input1=v[1], input2=v[2]))
        fields = base + " " + " ".join(f"task.{i} task_quality.{i}" for i in range(len(task_rows)))
        schema_rows.extend(dict(profile=profile, position=i, column=column)
                           for i, column in enumerate(fields.split()))
        lines = []
        for snap in snapshots:
            lines += ["PURGE_BATCH", "LOAD " + snap["path"], "FILTER num_units > 0"]
            for i, v in enumerate(values):
                lines += ["RECALCULATE 0 -1 0 " + " ".join(map(str, v)),
                          f"DETAIL {snap['label']}-input{i}.dat {fields}"]
        analyze = d / "analyze.cfg"
        analyze.write_text("\n".join(lines) + "\n")
        cmd = [a.avida, "-c", str(config), "-a", "-set", "ENVIRONMENT_FILE", str(env),
               "-set", "ANALYZE_FILE", str(analyze), "-set", "EVENT_FILE", str(out / "events.cfg"),
               "-set", "DATA_DIR", str(result_dir), "-set", "RANDOM_SEED", str(a.seed),
               "-set", "VERBOSITY", "2",
               "-set", "TASK_REFRACTORY_PERIOD", "0", "-set", "TEST_CPU_TIME_MOD", "20"]
        commands.append(dict(profile=profile, cwd=str(run_dir), command=cmd, selected=profile in selected))
    write_tsv(out / "inputs.tsv", input_rows, ["profile", "input_id", "input0", "input1", "input2"])
    write_tsv(out / "schema.tsv", schema_rows, ["profile", "position", "column"])
    (out / "commands.json").write_text(json.dumps(commands, indent=2) + "\n")
    script = ["#!/usr/bin/env bash", "set -u", "cd " + shlex.quote(str(run_dir)), "status=0"]
    for c in commands:
        if c["selected"]:
            log = out / c["profile"] / "run.log"
            script.append(shlex.join(c["command"]) + " > " + shlex.quote(str(log)) + " 2>&1 || status=1")
    script.append('exit "$status"')
    (out / "run.sh").write_text("\n".join(script) + "\n")
    if a.run:
        status = []
        for c in commands:
            if not c["selected"]:
                continue
            start = time.monotonic()
            with (out / c["profile"] / "run.log").open("w") as log:
                run = subprocess.run(c["command"], cwd=c["cwd"], stdout=log, stderr=subprocess.STDOUT)
            expected = [out / "results" / c["profile"] / f"{s['label']}-input{i}.dat"
                        for s in snapshots for i in range(a.inputs)]
            missing = [str(path) for path in expected if not path.exists()]
            status.append(dict(profile=c["profile"], exit_code=run.returncode,
                               seconds=time.monotonic() - start, missing_outputs=missing,
                               complete=(run.returncode == 0 and not missing)))
            (out / "run_status.json").write_text(json.dumps(status, indent=2) + "\n")
            print(c["profile"], "exit", run.returncode, "missing", len(missing), flush=True)
        if any(not s["complete"] for s in status):
            raise SystemExit("At least one profile is incomplete; retain its log and do not treat absent rows as task failures.")
    print("Generated", out, "with", len(rows), "audited task names.")


if __name__ == "__main__":
    main()
