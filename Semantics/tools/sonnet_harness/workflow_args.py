#!/usr/bin/env python3
"""Build the args of workflow/sonnet_jobs.workflow.js from task specs (runs nothing).

  python3 -B workflow_args.py --run <label> --job "<spec>" [--job ...] [--after "<spec>" ...] [--out args.json]

Prints {"jobs": [brief, ...], "after": [brief, ...], "opus_check_extraction": true}, each brief the output of
run_task.py --phase brief. Pass the printed object itself (not a string holding it) as the Workflow's args.
"""
import argparse
import json
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hcommon as H  # noqa: E402


def brief(spec, run):
    r = H.run([sys.executable, "-B", os.path.join(H.HERE, "run_task.py"), spec, "--phase", "brief", "--run", run], timeout=60)
    if r["exit"] != 0:
        H.refuse("the brief of %s failed" % spec, stdout=r["stdout"][-500:], stderr=r["stderr"][-500:])
    b = json.loads(r["stdout"])
    b.pop("ok", None)
    return b


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    ap.add_argument("--job", action="append", default=[])
    ap.add_argument("--after", action="append", default=[])
    ap.add_argument("--out")
    a = ap.parse_args()
    out = dict(jobs=[brief(s, a.run) for s in a.job], after=[brief(s, a.run) for s in a.after], opus_check_extraction=True)
    if a.out:
        H.write_json(a.out, out)
    sys.stdout.write(json.dumps(out, ensure_ascii=False, indent=1) + "\n")


if __name__ == "__main__":
    main()
