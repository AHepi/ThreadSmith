# Plain note (log S120, written by Claude, Opus 5.5, 1 October 2026).
# What this does, for the small pilot of GPT 6 Astra's reply 01 (the execution environment
# that pays a program when its output equals the next number it will be handed):
#   prepare  - writes one folder per run (R2 seeds 1 and 2, R1 seed 1; 20,000 updates; the
#              settings of the reply's proposed experiment) and a job list for
#              s120_run_jobs_three_at_a_time_and_record_cpu_time.py. Avida runs inside the
#              patched copy's binary, under nice and a timeout; nothing replicates outside Avida.
#   read     - reads each run's tasks.dat and count.dat and prints, every 1,000 updates, how
#              many programs performed the match in their last copy cycle, and when the match
#              was first performed by 1 and by 10 in 100 programs.
#   cross    - reruns every saved program of each run on Avida's test CPU (analyze mode, the
#              patched binary) under each rule (R0 random, R1 repeat, R2 add one), with fresh
#              number streams, and prints the share of programs that match under each rule.
#              This separates "adds one" from "repeats" from "lucky".
# Usage: python3 s120_anticipation_pilot_prepare_read_and_cross_test.py prepare|read|cross
import json
import re
import subprocess
import sys
from pathlib import Path

SCRATCH = Path("/tmp/claude-0/-home-user-ThreadSmith/8d9323da-c0ec-57ec-91fd-8f99ca99320a/scratchpad/s120")
SUPPORT = SCRATCH / "src-stock/avida-core/support/config"
PATCHED = SCRATCH / "src-anticipate/build/bin/avida"
PILOT = SCRATCH / "pilot01"
UPDATES = 20000
RUNS = [("R2-seed1", 2, 1), ("R2-seed2", 2, 2), ("R1-seed1", 1, 1)]
ENVIRONMENT = "REACTION ANT anticipate process:value=1:type=pow requisite:max_count=1\n"
SETTINGS = ["-set SPECULATIVE 0", "-set MERIT_INC_APPLY_IMMEDIATE 1", "-set ANTICIPATE_START -1",
            "-set REQUIRE_SINGLE_REACTION 0", "-set COPY_MUT_PROB 0.0075",
            "-set DIVIDE_INS_PROB 0.05", "-set DIVIDE_DEL_PROB 0.05", "-set VERBOSITY 1"]


def prepare():
    jobs = []
    for name, mode, seed in RUNS:
        folder = PILOT / name
        folder.mkdir(parents=True, exist_ok=False)
        for item in ("avida.cfg", "instset-heads.cfg", "default-heads.org"):
            (folder / item).write_bytes((SUPPORT / item).read_bytes())
        (folder / "environment.cfg").write_text(ENVIRONMENT)
        (folder / "events.cfg").write_text(
            "u begin Inject default-heads.org\n"
            "u 0:100:end PrintTasksData\n"
            "u 0:100:end PrintCountData\n"
            "u 0:100:end PrintAverageData\n"
            "u 0:100:end PrintTimeData\n"
            "u 10000 SavePopulation filename=population:save_historic=0\n"
            "u %d SavePopulation filename=population:save_historic=0\n"
            "u %d Exit\n" % (UPDATES, UPDATES))
        command = "%s -s %d %s -set ANTICIPATE_MODE %d > avida.log 2>&1" % (
            PATCHED, seed, " ".join(SETTINGS), mode)
        jobs.append({"name": name, "cwd": str(folder), "timeout_seconds": 3 * 3600, "command": command})
    (PILOT / "jobs.json").write_text(json.dumps(jobs, indent=1))
    print("prepared", len(jobs), "runs in", PILOT)


def table(path):
    rows = []
    for line in Path(path).read_text().splitlines():
        if line.strip() and not line.startswith("#"):
            rows.append([float(x) for x in line.split()])
    return rows


def read():
    result = {}
    for name, mode, seed in RUNS:
        folder = PILOT / name / "data"
        tasks = {int(r[0]): r[1] for r in table(folder / "tasks.dat")}
        counts = {int(r[0]): r[2] for r in table(folder / "count.dat")}
        # count.dat column 3 is the number of programs (checked against its header below)
        header = (folder / "count.dat").read_text()
        assert re.search(r"#\s*3:\s*Number of Organisms", header, re.I) or "organisms" in header.lower()
        series = []
        first1 = first10 = None
        for update in sorted(tasks):
            programs = counts.get(update, 0)
            share = tasks[update] / programs if programs else 0.0
            if first1 is None and share >= 0.01:
                first1 = update
            if first10 is None and share >= 0.10:
                first10 = update
            if update % 1000 == 0:
                series.append((update, int(programs), int(tasks[update]), round(share, 3)))
        result[name] = {"first_1_in_100": first1, "first_10_in_100": first10, "every_1000": series}
        print(name, "first >=1/100:", first1, "first >=10/100:", first10)
        for row in series:
            print("  update %6d programs %5d matching %5d share %.3f" % row)
    (PILOT / "read.json").write_text(json.dumps(result, indent=1))


def cross():
    result = {}
    for name, mode, seed in RUNS:
        for update in (10000, UPDATES):
            snapshot = PILOT / name / "data" / ("population-%d.spop" % update)
            for rule in (0, 1, 2):
                out = PILOT / name / ("cross-u%d-rule%d" % (update, rule))
                out.mkdir(exist_ok=True)
                (out / "analyze.cfg").write_text(
                    "LOAD %s\nRECALCULATE\nDETAIL %s/detail.dat id num_cpus viable task.0\n" % (snapshot, out))
                (out / "events.cfg").write_text("")
                command = ["timeout", "900", "nice", "-n", "19", str(PATCHED), "-a", "-s", "7",
                           "-set", "ANALYZE_FILE", str(out / "analyze.cfg"),
                           "-set", "EVENT_FILE", str(out / "events.cfg"),
                           "-set", "DATA_DIR", str(out / "data"),
                           "-set", "ANTICIPATE_MODE", str(rule), "-set", "ANTICIPATE_START", "-1",
                           "-set", "SPECULATIVE", "0"]
                with open(out / "avida.log", "w") as log:
                    code = subprocess.run(command, cwd=PILOT / name, stdout=log, stderr=subprocess.STDOUT).returncode
                rows = table(out / "detail.dat")
                total = sum(r[1] for r in rows)
                matching = sum(r[1] for r in rows if r[3] > 0)
                viable_matching = sum(r[1] for r in rows if r[3] > 0 and r[2] > 0)
                viable = sum(r[1] for r in rows if r[2] > 0)
                key = "%s u%d R%d" % (name, update, rule)
                result[key] = {"exit": code, "programs": int(total), "matching": int(matching),
                               "share": round(matching / total, 4) if total else None,
                               "can_copy": int(viable), "matching_and_can_copy": int(viable_matching)}
                print(key, result[key])
    (PILOT / "cross.json").write_text(json.dumps(result, indent=1))


if __name__ == "__main__":
    {"prepare": prepare, "read": read, "cross": cross}[sys.argv[1]]()
