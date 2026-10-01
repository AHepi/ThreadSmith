#!/usr/bin/env python3
# Plain note (log S122, written by Claude, Opus 5.5, 1 October 2026).
# What this does: finishes the S122 pilot after the container restart of about 22:40 UTC stopped
# it part way. The plan is unchanged ("results/S122 Checking the Astra returns to S121/pilot -
# what would count, written before running.md"): arms "full" and "memoryless", master seeds 2201
# and 2202, 20 pieces of 1,000 updates, 60 x 60 world, stock Avida at 47f13dad, reply 01's own
# runner unchanged. Only the way of starting differs (a departure, recorded): each run that was
# stopped part way has its unfinished piece folder moved aside (to
# pilot/partial_pieces_moved_aside_after_restart/) and is then continued with the runner's own
# "--resume", which re-reads every finished piece (its saved selector state, pay and population,
# checked against its recorded SHA-256) and runs the rest; a run that never started is started.
# Because every piece's Avida seed comes from the master seed and the piece number, a continued
# run does exactly what an uninterrupted one would have done.
# At most TWO runs at once (so that, with the other S122 agent's one-at-a-time runs, no more than
# three Avida processes run at once on 4 CPUs). Each runner under "nice -n 19" and a 3-hour
# timeout; each Avida process under "nice -n 19" and a 900-second timeout through
# tools/s122_avida_wrapper_with_timeout_nice_and_cpu_log.py (CPU time appended to pilot/cpu.jsonl).
# Writes pilot/pids_after_restart.txt and pilot/jobs_after_restart.json. Nothing copies itself.
# Usage: python3 tools/s122_resume_the_temporal_selector_pilot_after_the_restart.py <scratch s122 folder>
import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
WRAPPER = HERE / "s122_avida_wrapper_with_timeout_nice_and_cpu_log.py"
ARMS = ["full", "memoryless"]
SEEDS = [2201, 2202]
PIECES = 20
AT_ONCE = 2


def main():
    base = Path(sys.argv[1]).resolve()
    work = base / "work"
    pilot = base / "pilot"
    aside = pilot / "partial_pieces_moved_aside_after_restart"
    env = dict(os.environ, GIT_OPTIONAL_LOCKS="0",
               S122_AVIDA_BINARY=str((work / "avida-source" / "cbuild" / "bin" / "avida").resolve()),
               S122_CPU_LOG=str(pilot / "cpu.jsonl"), S122_AVIDA_TIMEOUT="900")
    jobs = []
    for seed in SEEDS:
        for arm in ARMS:
            name = f"{arm}_{seed}"
            out = pilot / name
            done = out.exists() and all((out / f"piece_{p:03d}" / "complete.json").exists()
                                        for p in range(PIECES))
            if done:
                continue
            resume = out.exists()
            if resume:
                for piece in sorted(out.glob("piece_*")):
                    if not (piece / "complete.json").exists():
                        aside.mkdir(parents=True, exist_ok=True)
                        shutil.move(str(piece), str(aside / f"{name}_{piece.name}"))
            jobs.append((name, arm, seed, resume))
    running, records = {}, []
    while jobs or running:
        while jobs and len(running) < AT_ONCE:
            name, arm, seed, resume = jobs.pop(0)
            argv = ["timeout", "10800", "nice", "-n", "19", sys.executable, "runner.py",
                    "--avida", str(WRAPPER), "--source", str(work / "avida-source"),
                    "--out", str(pilot / name), "--seed", str(seed), "--arm", arm,
                    "--pieces", str(PIECES), "--width", "60", "--height", "60"]
            if resume:
                argv.append("--resume")
            log = open(pilot / f"{name}.log", "a")
            process = subprocess.Popen(argv, cwd=work / "temporal_selector", env=env,
                                       stdout=log, stderr=subprocess.STDOUT)
            with open(pilot / "pids_after_restart.txt", "a") as handle:
                handle.write(f"{process.pid} {name} {time.strftime('%H:%M:%S', time.gmtime())} UTC\n")
            running[process.pid] = dict(name=name, log=log, start=time.time(), argv=argv)
        pid, status, usage = os.wait4(-1, 0)
        if pid not in running:
            continue
        job = running.pop(pid)
        job["log"].close()
        records.append(dict(name=job["name"], argv=job["argv"], exit=os.waitstatus_to_exitcode(status),
                            wall_seconds=round(time.time() - job["start"], 1),
                            cpu_seconds=round(usage.ru_utime + usage.ru_stime, 1)))
        (pilot / "jobs_after_restart.json").write_text(json.dumps(records, indent=2) + "\n")
    print("pilot finished after restart:", json.dumps([(r["name"], r["exit"], r["cpu_seconds"]) for r in records]))


if __name__ == "__main__":
    main()
