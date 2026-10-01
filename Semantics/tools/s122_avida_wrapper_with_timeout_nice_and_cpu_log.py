#!/usr/bin/env python3
# Plain note (log S122, written by Claude, Opus 5.5, 1 October 2026).
# What this does: stands in for the Avida program when reply 01's runner calls it, so that every
# Avida process of the S122 pilot runs under "nice -n 19" and a timeout (900 seconds unless
# S122_AVIDA_TIMEOUT says otherwise), and so that the processor time of each Avida process is
# written down. It runs the real stock Avida binary named by S122_AVIDA_BINARY with the same
# arguments, in the same folder, and appends one line per process to the file named by
# S122_CPU_LOG: the folder, whether it was an analyze-mode (assay) run, user and system CPU
# seconds, wall seconds and the exit code. It changes nothing in what Avida does; the runner's
# output and Avida's output are passed through unchanged. Avida only; nothing here copies itself.
import json
import os
import resource
import subprocess
import sys
import time


def main():
    binary = os.environ["S122_AVIDA_BINARY"]
    log = os.environ["S122_CPU_LOG"]
    limit = os.environ.get("S122_AVIDA_TIMEOUT", "900")
    before = resource.getrusage(resource.RUSAGE_CHILDREN)
    start = time.time()
    code = subprocess.call(["timeout", limit, "nice", "-n", "19", binary] + sys.argv[1:])
    after = resource.getrusage(resource.RUSAGE_CHILDREN)
    record = dict(folder=os.getcwd(), analyze="-a" in sys.argv[1:],
                  user=round(after.ru_utime - before.ru_utime, 3),
                  system=round(after.ru_stime - before.ru_stime, 3),
                  wall=round(time.time() - start, 3), exit=code)
    with open(log, "a") as handle:
        handle.write(json.dumps(record) + "\n")
    sys.exit(code)


if __name__ == "__main__":
    main()
