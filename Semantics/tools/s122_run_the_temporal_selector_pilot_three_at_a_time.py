#!/usr/bin/env python3
# Plain note (log S122, written by Claude, Opus 5.5, 1 October 2026).
# What this does: runs the S122 pilot written down in "results/S122 Checking the Astra returns to
# S121/pilot - what would count, written before running.md": reply 01's own runner (unchanged,
# from a copy of tools/s122/01/temporal_selector/ in the scratch space), arms "full" and
# "memoryless", master seeds 2201 and 2202, 20 pieces of 1,000 updates, a 60 x 60 world, stock
# Avida at 47f13dad. At most three runs at once; each runner under "nice -n 19" and a 3-hour
# timeout; each Avida process under "nice -n 19" and a 900-second timeout through
# tools/s122_avida_wrapper_with_timeout_nice_and_cpu_log.py, which also logs each process's CPU
# time. Writes, in the scratch space s122/pilot/: one folder per run (the runner's own output),
# one log per run, "pids.txt" (the exact process number of each runner started, so that one
# can be stopped by number if needed), "cpu.jsonl" (one line per Avida process) and
# "jobs.json" (start, end, exit code, wall time and CPU time of each run).
# Usage: python3 tools/s122_run_the_temporal_selector_pilot_three_at_a_time.py <scratch s122 folder>
import json
import os
import resource
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
WRAPPER = HERE / "s122_avida_wrapper_with_timeout_nice_and_cpu_log.py"
ARMS = ["full", "memoryless"]
SEEDS = [2201, 2202]
PIECES = 20


def main():
    base = Path(sys.argv[1]).resolve()
    work = base / "work"
    pilot = base / "pilot"
    pilot.mkdir(parents=True, exist_ok=True)
    env = dict(os.environ, GIT_OPTIONAL_LOCKS="0",
               S122_AVIDA_BINARY=str((work / "avida-source" / "cbuild" / "bin" / "avida").resolve()),
               S122_CPU_LOG=str(pilot / "cpu.jsonl"), S122_AVIDA_TIMEOUT="900")
    jobs = [(arm, seed) for seed in SEEDS for arm in ARMS]
    running, records = {}, []
    while jobs or running:
        while jobs and len(running) < 3:
            arm, seed = jobs.pop(0)
            name = f"{arm}_{seed}"
            argv = ["timeout", "10800", "nice", "-n", "19", sys.executable, "runner.py",
                    "--avida", str(WRAPPER), "--source", str(work / "avida-source"),
                    "--out", str(pilot / name), "--seed", str(seed), "--arm", arm,
                    "--pieces", str(PIECES), "--width", "60", "--height", "60"]
            log = open(pilot / f"{name}.log", "w")
            process = subprocess.Popen(argv, cwd=work / "temporal_selector", env=env,
                                       stdout=log, stderr=subprocess.STDOUT)
            with open(pilot / "pids.txt", "a") as handle:
                handle.write(f"{process.pid} {name} {time.strftime('%H:%M:%S', time.gmtime())} UTC\n")
            running[process.pid] = dict(name=name, process=process, log=log, start=time.time(),
                                        argv=argv)
        pid, status, usage = os.wait4(-1, 0)
        if pid not in running:
            continue
        job = running.pop(pid)
        job["log"].close()
        records.append(dict(name=job["name"], argv=job["argv"], exit=os.waitstatus_to_exitcode(status),
                            wall_seconds=round(time.time() - job["start"], 1),
                            cpu_seconds=round(usage.ru_utime + usage.ru_stime, 1)))
        (pilot / "jobs.json").write_text(json.dumps(records, indent=2) + "\n")
    print("pilot finished:", json.dumps([(r["name"], r["exit"], r["cpu_seconds"]) for r in records]))


if __name__ == "__main__":
    main()
