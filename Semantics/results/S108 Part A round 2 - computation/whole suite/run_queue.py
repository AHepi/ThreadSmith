#!/usr/bin/env python3
"""S108 Part A round 2, after S56: one Opus agent runs the whole-suite runs (and the section runs cut off when the per-section
agents were stopped) itself, by script, in place of the Sonnet harness's worker and verifier (a departure from the round-2 rule's
harness clause, recorded; S55, S56: cost). A job list (JSON: [{name, cwd, argv, env, timeout, stdout}]) is run with at most P
jobs at once, each under `timeout`, PYTHONHASHSEED=0; each job's stdout goes to its `stdout` file; a line per start and end goes
to the log. Writes nothing else.
  python3 -B run_queue.py JOBS.json LOG P
"""
import json, os, subprocess, sys, time
from concurrent.futures import ThreadPoolExecutor

jobs = json.load(open(sys.argv[1], encoding="utf-8"))
log = sys.argv[2]
P = int(sys.argv[3])


def say(s):
    with open(log, "a", encoding="utf-8") as f:
        f.write(time.strftime("%H:%M:%S", time.gmtime()) + " " + s + "\n")


def one(j):
    if os.path.exists(j["stdout"]) and os.path.getsize(j["stdout"]) > 0 and not j.get("force"):
        say("skip (done) " + j["name"]); return
    os.makedirs(os.path.dirname(j["stdout"]), exist_ok=True)
    env = dict(os.environ); env["PYTHONHASHSEED"] = "0"
    for k in j.get("unset", []): env.pop(k, None)
    env.update(j.get("env", {}))
    say("start " + j["name"]); t = time.time()
    with open(j["stdout"] + ".part", "w", encoding="utf-8") as out:
        r = subprocess.run(["timeout", str(j["timeout"])] + j["argv"], cwd=j["cwd"], env=env, stdout=out, stderr=subprocess.STDOUT)
    os.replace(j["stdout"] + ".part", j["stdout"])
    say("end %s exit %d %.0fs" % (j["name"], r.returncode, time.time() - t))


with ThreadPoolExecutor(max_workers=P) as ex:
    list(ex.map(one, jobs))
say("all ended")
