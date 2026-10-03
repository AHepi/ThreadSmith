# Plain note (log S122, reply 02; written by Claude, Opus 5.5, 1 October 2026).
# What this does: runs a list of shell commands ONE AT A TIME, each under "nice -n 19" and
# "timeout", in its own folder. Before starting each one it looks at the machine's process list
# and waits (checking every 5 seconds) while 2 or more other Avida processes are running, so
# that this job and another agent's runs stay within 3 Avida processes on 4 CPUs. It records for
# each job when it started and ended, its exit code and the processor time it used (user +
# system seconds, read from the operating system when it ends).
# Usage: python3 s122r02_run_jobs_one_at_a_time_when_free.py JOBS.json LOG.json
# JOBS.json is a list of {"name", "cwd", "command", "timeout_seconds"}; the command is run by
# /bin/bash in "cwd". Nothing here copies or replicates itself; all program replication
# happens inside Avida.
import json
import os
import subprocess
import sys
import time

BUSY_LIMIT = 2


def other_avida_processes(own):
    """Count running processes whose program is an Avida binary, other than our own children."""
    count = 0
    for entry in os.listdir("/proc"):
        if not entry.isdigit() or int(entry) in own:
            continue
        try:
            argv = open("/proc/%s/cmdline" % entry, "rb").read().split(b"\0")
        except OSError:
            continue
        if argv and os.path.basename(argv[0].decode("utf-8", "replace")) == "avida":
            count += 1
    return count


def main(jobs_path, log_path):
    jobs = json.load(open(jobs_path))
    records = []
    for job in jobs:
        waited = 0
        while other_avida_processes(set()) >= BUSY_LIMIT:
            time.sleep(5)
            waited += 5
        os.makedirs(job["cwd"], exist_ok=True)
        out = open(os.path.join(job["cwd"], "job.out"), "w")
        command = "exec timeout %d nice -n 19 bash -c %s" % (job["timeout_seconds"], json.dumps(job["command"]))
        start = time.time()
        process = subprocess.Popen(["/bin/bash", "-c", command], cwd=job["cwd"], stdout=out, stderr=subprocess.STDOUT)
        print("started %s pid %d after waiting %d s" % (job["name"], process.pid, waited), flush=True)
        _, status, usage = os.wait4(process.pid, 0)
        out.close()
        records.append({"name": job["name"], "pid": process.pid, "waited_seconds": waited,
                        "started_utc": time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(start)),
                        "wall_seconds": round(time.time() - start, 1),
                        "exit": os.waitstatus_to_exitcode(status),
                        "cpu_seconds": round(usage.ru_utime + usage.ru_stime, 1)})
        print("ended %s exit %d cpu %.1f s" % (job["name"], records[-1]["exit"], records[-1]["cpu_seconds"]), flush=True)
        with open(log_path + ".tmp", "w") as stream:
            json.dump({"jobs": records}, stream, indent=2)
        os.replace(log_path + ".tmp", log_path)
    print("all jobs ended", flush=True)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
