#!/usr/bin/env python3
"""Look at a detached run: is its process alive, has it ended, what do its progress lines say.

  python3 -B watch_run.py --log <run log> --pidfile <pid file> [--tail 15]

Reads only the run's log and pid file. Prints only log lines that are progress lines (launched, pass, start, sent,
still running, accepted, not accepted, ok, failed, done, waiting, every pass ended, loop ended); any other line is
counted and withheld, so no reply text is ever shown (the reading rules let the progress lines be watched, nothing
else). It never opens a reply, receipt or attempt file, never reads a key file, and never stops or starts a process.
state: "running" | "ended" (log says loop ended, process gone) | "stopped without ending" (process gone, no end
line: e.g. a container restart; relaunching is the orchestrator's when the run needs a key).
ok = state is running or ended.
"""
import argparse
import os
import re
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import hcommon as H  # noqa: E402
from s80_common import live_pid  # noqa: E402

PROGRESS = re.compile(r"\b(launched|pass \d|start(ed)?|sent|still running|accepted|not accepted|ok|failed|done|"
                      r"waiting|every pass ended|loop ended|attempt \d+)\b", re.I)
MAXLEN = 240


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--log", required=True)
    ap.add_argument("--pidfile", required=True)
    ap.add_argument("--tail", type=int, default=15)
    a = ap.parse_args()
    lines = H.read_text(a.log).split("\n") if os.path.exists(a.log) else []
    shown, withheld = [], 0
    for l in lines[-max(1, a.tail * 4):]:
        if not l.strip():
            continue
        if PROGRESS.search(l) and len(l) <= MAXLEN:
            shown.append(l)
        else:
            withheld += 1
    pid = live_pid(a.pidfile) if os.path.exists(a.pidfile) else None
    ended_line = any("loop ended" in l for l in lines)
    state = "running" if pid else ("ended" if ended_line else "stopped without ending")
    H.emit(dict(ok=state in ("running", "ended"), job="watch_run", log=H.rel(a.log), log_lines=len(lines),
                pid_alive=pid, state=state, progress_tail=shown[-a.tail:], lines_withheld=withheld))


if __name__ == "__main__":
    main()
