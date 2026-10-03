# Plain note (log S120, written by Claude, Opus 5.5, 1 October 2026).
# What this does: runs a list of shell commands (the S120 pilots), never more than three at
# once, each under "nice -n 19" and "timeout", in its own folder, and records for each one
# when it started and ended, its exit code, and the processor time it and the programs it
# waited for used (user + system seconds, read from the operating system when it ends).
# Usage: python3 s120_run_jobs_three_at_a_time_and_record_cpu_time.py JOBS.json LOG.json
# JOBS.json is a list of {"name", "cwd", "command", "timeout_seconds"}. The command is run by
# /bin/bash in "cwd". Avida itself must also be under a timeout inside the command when the
# command starts Avida more than once (the S120 jobs use a small wrapper for that).
# Nothing here copies or replicates itself; all program replication happens inside Avida.
import json
import os
import subprocess
import sys
import time

MAX_AT_ONCE = 3


def main(jobs_path, log_path):
    jobs = json.load(open(jobs_path))
    waiting = list(jobs)
    running = {}
    records = []

    def save():
        with open(log_path + ".tmp", "w") as stream:
            json.dump({"max_at_once": MAX_AT_ONCE, "jobs": records,
                       "running": [running[p]["name"] for p in running],
                       "waiting": [j["name"] for j in waiting]}, stream, indent=2)
        os.replace(log_path + ".tmp", log_path)

    while waiting or running:
        while waiting and len(running) < MAX_AT_ONCE:
            job = waiting.pop(0)
            os.makedirs(job["cwd"], exist_ok=True)
            out = open(os.path.join(job["cwd"], "job.out"), "w")
            command = "exec timeout %d nice -n 19 bash -c %s" % (
                job["timeout_seconds"], json.dumps(job["command"]))
            process = subprocess.Popen(["/bin/bash", "-c", command], cwd=job["cwd"],
                                       stdout=out, stderr=subprocess.STDOUT)
            running[process.pid] = {"name": job["name"], "start": time.time(), "out": out,
                                    "process": process}
            print("started %s pid %d" % (job["name"], process.pid), flush=True)
            save()
        pid, status, usage = os.wait4(-1, 0)
        if pid not in running:
            continue
        item = running.pop(pid)
        item["out"].close()
        item["process"].returncode = os.waitstatus_to_exitcode(status)
        records.append({"name": item["name"], "pid": pid,
                        "started_utc": time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(item["start"])),
                        "wall_seconds": round(time.time() - item["start"], 1),
                        "exit": os.waitstatus_to_exitcode(status),
                        "cpu_seconds": round(usage.ru_utime + usage.ru_stime, 1)})
        print("ended %s exit %d cpu %.1f s" % (item["name"], records[-1]["exit"],
                                               records[-1]["cpu_seconds"]), flush=True)
        save()
    print("all jobs ended", flush=True)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
