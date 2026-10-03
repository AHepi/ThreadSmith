# Plain note (log S120, written by Claude, Opus 5.5, 1 October 2026).
# What this does, for GPT 6 Astra's reply 02 (an execution environment whose pay changes with
# its own record of the program population):
#   smoke - Claude's own version of the reply's "independent inspection" (whose script the
#           reply did not supply): in the four 200-update smoke runs, the blind replay's pay
#           equals the donor's piece by piece; the fixed control's pay equals the donor's mean
#           per task; each saved program population holds as many programs as the driver
#           recorded; every piece has its own seed.
#   pilot - reads the S120 pilot (A, B and the fixed control, 20 pieces of 1,000 updates) from
#           the driver's own observations.json and prints, piece by piece, the total pay
#           offered, the tasks present and common, and the tasks first common, lost and
#           regained; and the share of pieces in which A offered no pay at all.
# Reads files only; runs no Avida process.
import json
import sys
from pathlib import Path

SCRATCH = Path("/tmp/claude-0/-home-user-ThreadSmith/8d9323da-c0ec-57ec-91fd-8f99ca99320a/scratchpad/s120")


def living(spop):
    lines = Path(spop).read_text().splitlines()
    fmt = next(l for l in lines if l.startswith("#format")).split()[1:]
    k = fmt.index("num_units")
    return sum(int(l.split()[k]) for l in lines if l.strip() and not l.startswith("#"))


def smoke():
    base = SCRATCH / "r02/stage1"
    donor = json.loads((base / "smoke-progress/schedule.json").read_text())
    replay = json.loads((base / "smoke-replay/schedule.json").read_text())
    fixed = json.loads((base / "smoke-fixed/schedule.json").read_text())
    print("replay pay equals donor pay, piece by piece:", replay["values"] == donor["values"])
    means = [sum(c) / len(donor["values"]) for c in zip(*donor["values"])]
    ok = all(all(abs(a - b) < 1e-12 for a, b in zip(row, means)) for row in fixed["values"])
    print("fixed pay equals donor mean per task, every piece:", ok)
    seeds, counts_ok = [], True
    for run in ("smoke-progress", "smoke-archive", "smoke-replay", "smoke-fixed"):
        for obs in json.loads((base / run / "observations.json").read_text()):
            seeds.append(obs["seed"])
            counts_ok &= living(base / run / obs["snapshot"]) == obs["living"]
    print("saved populations hold the recorded number of programs:", counts_ok)
    print("eight piece seeds distinct:", len(set(seeds)) == len(seeds) == 8)


def pilot():
    out = {}
    for arm in ("A-progress", "B-archive", "fixed-all77"):
        obs = json.loads((SCRATCH / "pilot02" / arm / "observations.json").read_text())
        print(arm)
        rows = []
        for o in obs:
            row = {"updates": o["global_updates"], "pay_offered": round(o["pay_total"], 4),
                   "present": o["tasks_present"], "common": o["common_10pct"],
                   "first_common": o["first_common"], "lost": o["lost"], "regained": o["reacquired"],
                   "cumulative_common": o["cumulative_common"], "living": o["living"]}
            rows.append(row)
            print("  %6d pay %8.4f present %2d common %2d first %s lost %s regained %s" % (
                row["updates"], row["pay_offered"], row["present"], row["common"],
                row["first_common"], row["lost"], row["regained"]))
        zero = sum(1 for o in obs[1:] if o["zero_pay"])
        print("  pieces 2-%d with no pay offered at all: %d" % (len(obs), zero))
        out[arm] = {"pieces": rows, "pieces_after_first_with_zero_pay": zero}
    (SCRATCH / "pilot02" / "read.json").write_text(json.dumps(out, indent=1))


if __name__ == "__main__":
    {"smoke": smoke, "pilot": pilot}[sys.argv[1]]()
