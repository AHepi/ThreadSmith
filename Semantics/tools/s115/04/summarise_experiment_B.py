# NOTE (written by Claude, 30 September 2026, log S115; NOT part of Astra's reply 04):
# reads the outputs of reply 04's Experiment B (after its --run and --snapshots
# phases) and computes the measures the reply defines in words:
#   - per snapshot, per task: sum(n*v*t)/sum(n), sum(n*v*t)/sum(n*v), sum(n*v)/sum(n)
#     from each common_assays/<run>/<update>/data/common.dat
#     (n = num_cpus, v = viable, t = task indicator);
#   - from each run's tasks.dat and count.dat: first update with any EQU program, the
#     first update starting three consecutive 100-update readings with EQU >= 10% of
#     living programs, and EQU and NOT fractions at 19,000 / 39,000 / 60,000;
#   - from totals.dat: program births after update 0 (the update-0 value is the 3,600
#     injected founders).
# Usage: python3 summarise_experiment_B.py <brief04_runs directory>
# Prints two tab-separated tables. It computes; it does not judge any forecast.
import sys
from pathlib import Path

TASKS = "NOT NAND AND ORN OR ANDN NOR XOR EQU".split()


def rows(path):
    for line in Path(path).read_text().splitlines():
        if line.strip() and not line.lstrip().startswith("#"):
            yield line.split()


def by_update(path):
    return {int(r[0]): r for r in rows(path)}


def snapshot_table(root):
    print("run\tupdate\tviable_share\t" + "\t".join(
        f"{t}_of_all\t{t}_of_viable" for t in TASKS))
    for run in sorted(root.glob("B_*")):
        base = root / "common_assays" / run.name
        if not base.is_dir():
            continue
        for upd in sorted((int(p.name) for p in base.iterdir() if p.name.isdigit())):
            f = base / str(upd) / "data" / "common.dat"
            n_all = n_viable = 0
            hits = [0] * 9
            for r in rows(f):  # id num_cpus viable length merit gest fitness task x9 seq
                n, v = int(r[1]), int(r[2])
                n_all += n
                n_viable += n * v
                for i in range(9):
                    hits[i] += n * v * int(r[7 + i])
            cells = [f"{run.name}\t{upd}\t{n_viable / n_all:.4f}" if n_all else f"{run.name}\t{upd}\tNA"]
            for h in hits:
                a = f"{h / n_all:.4f}" if n_all else "NA"
                b = f"{h / n_viable:.4f}" if n_viable else "NA"
                cells.append(f"{a}\t{b}")
            print("\t".join(cells))


def live_table(root):
    print("run\tfirst_EQU\tfirst_3x_EQU_10pct\tEQU_19000\tEQU_39000\tEQU_60000"
          "\tNOT_19000\tNOT_39000\tNOT_60000\tbirths_after_0\tlast_update")
    for run in sorted(root.glob("B_*")):
        d = run / "data"
        if not (d / "tasks.dat").is_file():
            continue
        tasks = by_update(d / "tasks.dat")          # update, then 9 task counts
        count = by_update(d / "count.dat")          # column 3 = living programs
        totals = by_update(d / "totals.dat")        # column 4 = total programs born
        ups = sorted(tasks)
        frac = {}
        for u in ups:
            alive = int(count[u][2]) if u in count else 0
            frac[u] = [int(x) / alive if alive else 0.0 for x in tasks[u][1:10]]
        first = next((u for u in ups if int(tasks[u][9]) > 0), "none")
        streak = "none"
        for i in range(len(ups) - 2):
            if all(frac[ups[i + k]][8] >= 0.10 for k in range(3)):
                streak = ups[i]
                break
        def at(u, k):
            return f"{frac[u][k]:.4f}" if u in frac else "NA"
        born = (int(totals[max(totals)][3]) - int(totals[0][3])) if 0 in totals else "NA"
        print("\t".join(map(str, [run.name, first, streak, at(19000, 8), at(39000, 8),
                                  at(60000, 8), at(19000, 0), at(39000, 0), at(60000, 0),
                                  born, ups[-1]])))


if __name__ == "__main__":
    root = Path(sys.argv[1])
    snapshot_table(root)
    print()
    live_table(root)
