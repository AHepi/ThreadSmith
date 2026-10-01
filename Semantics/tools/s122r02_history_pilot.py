# Plain note (log S122, reply 02; written by Claude, Opus 5.5, 1 October 2026).
# What this does, for ONE SMALL pilot of GPT 6 Astra's reply 02 (tasks that need history):
#   prepare - writes one folder per run: the order task (HISTORY_MODE 0) and the interval task
#             (HISTORY_MODE 1, window W=2), each paid (one doubling per copy cycle, the reply's own
#             reaction line) and unpaid (the same reaction with value 0: the task is still detected
#             and counted, but pays nothing); seed 1; 10,000 updates; from the task-free ancestor
#             default-heads.org; 60 x 60 cells; the settings of the S120 anticipation pilot. Writes
#             a job list for s122r02_run_jobs_one_at_a_time_when_free.py (one Avida at a time, under
#             nice and a timeout). Nothing replicates outside Avida.
#   read    - reads tasks.dat and count.dat: every 1,000 updates, how many programs performed the
#             task in their last copy cycle, and when 1 and 10 in 100 first did.
#   probe   - takes the most common programs of each run's last saved population, writes each as an
#             instruction file, and runs it in Avida's test processor with the probe
#             (s122r02_probe.cc): (a) with the history stream on, ten random-pair seeds, the program
#             living copy cycle after copy cycle as a parent does (its stream not rewound): what share
#             of the pairs it completes is paid, against the most a read-counting rule can earn?
#             (b) with history off, the test processor hands
#             in 40 random event sequences (A, B, C, X at random); at each read position, does the
#             number output after a B (the event the task asks about) differ between sequences?
#             At a fixed read position the position in the frame is the same in every sequence,
#             so a difference can only come from what was read earlier: the program carries event
#             history. A program whose answer after B never differs uses position only (or nothing).
# Usage: python3 s122r02_history_pilot.py prepare|read|probe
import json
import random
import subprocess
import sys
from pathlib import Path

SCRATCH = Path("/tmp/claude-0/-home-user-ThreadSmith/8d9323da-c0ec-57ec-91fd-8f99ca99320a/scratchpad")
SUPPORT = SCRATCH / "avida/avida-core/support/config"
WORK = SCRATCH / "s122_reply02"
PATCHED = WORK / "src-history/build/bin/avida"
PROBE = WORK / "r02/probe/probe"
PILOT = WORK / "pilot"
UPDATES = 10000
TASK = {0: "hist_order", 1: "hist_interval"}
RUNS = [("order-paid", 0, 1, 1), ("order-unpaid", 0, 1, 0), ("interval-paid", 1, 1, 1), ("interval-unpaid", 1, 1, 0)]
SETTINGS = ["-set SPECULATIVE 0", "-set MERIT_INC_APPLY_IMMEDIATE 1", "-set REQUIRE_SINGLE_REACTION 0",
            "-set COPY_MUT_PROB 0.0075", "-set DIVIDE_INS_PROB 0.05", "-set DIVIDE_DEL_PROB 0.05",
            "-set VERBOSITY 1", "-set ANTICIPATE_MODE -1", "-set HISTORY_WINDOW 2", "-set HISTORY_CASE -1"]
LETTERS = "abcdefghijklmnopqrstuvwxyz"


def prepare():
    jobs = []
    for name, mode, seed, value in RUNS:
        folder = PILOT / name
        folder.mkdir(parents=True, exist_ok=False)
        for item in ("avida.cfg", "instset-heads.cfg", "default-heads.org"):
            (folder / item).write_bytes((SUPPORT / item).read_bytes())
        (folder / "environment.cfg").write_text(
            "REACTION H %s process:value=%d:type=pow requisite:max_count=1\n" % (TASK[mode], value))
        (folder / "events.cfg").write_text(
            "u begin Inject default-heads.org\n"
            "u 0:100:end PrintTasksData\n"
            "u 0:100:end PrintCountData\n"
            "u 0:100:end PrintAverageData\n"
            "u 5000 SavePopulation filename=population:save_historic=0\n"
            "u %d SavePopulation filename=population:save_historic=0\n"
            "u %d Exit\n" % (UPDATES, UPDATES))
        command = "%s -s %d %s -set HISTORY_MODE %d > avida.log 2>&1" % (PATCHED, seed, " ".join(SETTINGS), mode)
        jobs.append({"name": name, "cwd": str(folder), "timeout_seconds": 2 * 3600, "command": command})
    (PILOT / "jobs.json").write_text(json.dumps(jobs, indent=1))
    print("prepared", len(jobs), "runs in", PILOT)


def table(path):
    return [[float(x) for x in line.split()] for line in Path(path).read_text().splitlines()
            if line.strip() and not line.startswith("#")]


def read():
    result = {}
    for name, mode, seed, value in RUNS:
        folder = PILOT / name / "data"
        if not (folder / "tasks.dat").exists():
            continue
        assert "#  3: number of organisms" in (folder / "count.dat").read_text()
        tasks = {int(r[0]): r[1] for r in table(folder / "tasks.dat")}
        counts = {int(r[0]): r[2] for r in table(folder / "count.dat")}
        first1 = first10 = None
        series = []
        for update in sorted(tasks):
            programs = counts.get(update, 0)
            share = tasks[update] / programs if programs else 0.0
            if first1 is None and share >= 0.01:
                first1 = update
            if first10 is None and share >= 0.10:
                first10 = update
            if update % 1000 == 0:
                series.append((update, int(programs), int(tasks[update]), round(share, 3)))
        peak = max(tasks.values()) if tasks else 0
        result[name] = {"first_1_in_100": first1, "first_10_in_100": first10, "peak_count": int(peak),
                        "every_1000": series}
        print(name, "first >=1/100:", first1, "first >=10/100:", first10, "peak count:", int(peak))
        for row in series:
            print("  update %6d programs %5d doing the task %5d share %.3f" % row)
    (PILOT / "read.json").write_text(json.dumps(result, indent=1))


def run_probe(args, cwd):
    out = subprocess.run(["timeout", "120", "nice", "-n", "19", str(PROBE)] + args, cwd=cwd,
                         stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    return out.returncode, out.stdout


def parse_trace(text):
    values = {}
    for line in text.splitlines():
        line = line.strip()
        for key in ("inputs=", "outputs="):
            if line.startswith(key):
                body = line[len(key):]
                values[key[:-1]] = [int(x) for x in body.split(",")] if body else []
    return values.get("inputs", []), values.get("outputs", [])


def probe(top=10):
    # (a) history on: each program lives as a parent does in a world, copy cycle after copy cycle with
    #     its stream never rewound ("probe cycles", until it stops dividing or dies of age), at ten
    #     random-pair seeds; counted: pairs completed, pairs paid, copy cycles with a paid pair.
    #     A program whose share of pairs paid is clearly above the most any read-counting rule can
    #     earn (order 1.0, interval 0.51, sequence 0.80; "probe pairclock") must use earlier events.
    # (b) history off: 40 random event sequences handed in through the stock input path; at a read
    #     position where a B was read, does the answer after it differ between sequences? (it then
    #     depends on events read earlier; for the order task this alone is not needed to earn).
    rng = random.Random(122)
    sequences = [[rng.randrange(4) for _ in range(240)] for _ in range(40)]
    clock_max = {0: 1.0, 1: 0.51, 2: 0.80}
    result = {}
    for name, mode, seed, value in RUNS:
        snapshot = PILOT / name / "data" / ("population-%d.spop" % UPDATES)
        if not snapshot.exists():
            continue
        rows = []
        for line in snapshot.read_text().splitlines():
            if line.strip() and not line.startswith("#"):
                parts = line.split()
                rows.append((int(parts[4]), parts[0], parts[16]))
        total = sum(r[0] for r in rows)
        rows.sort(key=lambda r: -r[0])
        folder = PILOT / name / "probe"
        folder.mkdir(exist_ok=True)
        for item in ("avida.cfg", "instset-heads.cfg", "environment.cfg", "events.cfg"):
            (folder / item).write_bytes((WORK / "r02/probe" / item).read_bytes())
        entries = []
        for count, gid, seq in rows[:top]:
            org = folder / ("g%s.org" % gid)
            org.write_text("#inst_set heads_default\n#hw_type 0\n" +
                           "\n".join(LINES[LETTERS.index(ch)] for ch in seq) + "\n")
            pairs = paid = cycles = paid_cycles = 0
            for s in range(1, 11):
                code, text = run_probe(["cycles", str(mode), org.name, "200", str(s)], folder)
                last = text.strip().splitlines()[-1] if code == 0 else ""
                fields = dict(f.split("=", 1) for f in last.split() if "=" in f)
                pairs += int(fields.get("pairs_completed", 0)); paid += int(fields.get("pairs_paid", 0))
                cycles += int(fields.get("copy_cycles", 0)); paid_cycles += int(fields.get("cycles_with_a_paid_pair", 0))
            answers = {}
            for events in sequences:
                code, text = run_probe(["stock", org.name, ",".join(map(str, events)), "20"], folder)
                ins, outs = parse_trace(text)
                for k in range(len(ins) - 1):
                    if ins[k] == 2:
                        answers.setdefault(k, set()).add(outs[k + 1] == 1)
            varies = sorted(k for k, a in answers.items() if len(a) > 1)
            share = round(paid / pairs, 3) if pairs else 0.0
            entries.append({"genotype": gid, "programs": count, "length": len(seq),
                            "copy_cycles": cycles, "cycles_with_a_paid_pair": paid_cycles,
                            "pairs_completed": pairs, "pairs_paid": paid, "share_of_pairs_paid": share,
                            "above_read_counting_maximum": share > clock_max[mode] + 0.05,
                            "read_positions_after_B": len(answers),
                            "positions_where_answer_after_B_depends_on_earlier_events": varies})
            print(name, gid, count, "cycles", cycles, "paid cycles", paid_cycles, "pairs", pairs, "paid", paid,
                  "share", share, "history-dependent at", varies, flush=True)
        covered = sum(e["programs"] for e in entries)
        earning = sum(e["programs"] for e in entries if e["pairs_paid"] > 0)
        above = sum(e["programs"] for e in entries if e["above_read_counting_maximum"])
        result[name] = {"programs": total, "genotypes": len(rows), "top_programs": covered,
                        "top_programs_earning": earning, "top_programs_above_read_counting_maximum": above,
                        "top": entries}
        print(name, "programs", total, "genotypes", len(rows), "top", top, "cover", covered, "earning", earning,
              "above read-counting maximum", above, flush=True)
    (PILOT / "probe.json").write_text(json.dumps(result, indent=1))


LINES = [line.split()[1] for line in (SUPPORT / "instset-heads.cfg").read_text().splitlines()
         if line.startswith("INST ")]

if __name__ == "__main__":
    {"prepare": prepare, "read": read, "probe": probe}[sys.argv[1]]()
