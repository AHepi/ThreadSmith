#!/usr/bin/env python3
# Plain note (log S122, written by Claude, Opus 5.5, 1 October 2026).
# What this does: reads the S122 pilot's raw output in the scratch space (s122/pilot/, written by
# reply 01's own runner) and prints, for each run, piece by piece: capabilities common (at least
# 10 in 100 programs) in the world's input order and in all six orders, common withheld ones,
# latches open and released, the least and most pay offered to a paid detector, the paid total,
# and the share of the 18 doublings going to detectors with an open latch. Then: every latch
# episode (detector, piece set, piece cleared or still open, why it was set), the capabilities
# common at the last piece, the first piece at which the two arms of a seed were offered
# different pay, and the CPU time of the Avida pieces and of the assays (from cpu.jsonl).
# It also writes everything as JSON to s122/pilot/reading.json. Reads only; runs nothing.
# Usage: python3 tools/s122_read_the_temporal_selector_pilot.py <scratch s122 folder>
import json
import sys
from pathlib import Path

TASKS = None


def load_run(folder):
    pieces = []
    for path in sorted(folder.glob("piece_*/complete.json")):
        record = json.loads(path.read_text())
        observation = json.loads((path.parent / "assay" / "observation.json").read_text())
        pieces.append((record, observation))
    return pieces


def main():
    global TASKS
    base = Path(sys.argv[1]).resolve() / "pilot"
    out = {}
    for folder in sorted(p for p in base.iterdir() if p.is_dir()):
        manifest = json.loads((folder / "manifest.json").read_text())
        TASKS = manifest["tasks"]
        eligible = set(manifest["eligible"])
        pieces = load_run(folder)
        rows, episodes, open_latch = [], [], {}
        for index, (record, obs) in enumerate(pieces):
            applied = record["applied_pay"]
            paid = [applied[j] for j in sorted(eligible)]
            latch = record["diagnostics"].get("latch", [0] * len(TASKS))
            release = record["diagnostics"].get("release", [0] * len(TASKS))
            nxt = record["next_pay"]
            for j, v in enumerate(latch):
                if v and j not in open_latch:
                    why = ("order-fragile (common in world order, not in all orders)"
                           if obs["p"][j] >= .1 else "loss of an earlier common capability")
                    open_latch[j] = dict(task=TASKS[j], set_after_piece=index + 1, why=why,
                                         p=round(obs["p"][j], 4), q=round(obs["q"][j], 4))
                if not v and j in open_latch:
                    episode = open_latch.pop(j)
                    episode["cleared_after_piece"] = index + 1
                    episodes.append(episode)
            latched_share = sum(nxt[j] for j, v in enumerate(latch) if v) / 18.0
            rows.append(dict(piece=index + 1,
                             world_common=sum(v >= .1 for v in obs["p"]),
                             all_order_common=sum(v >= .1 for v in obs["q"]),
                             withheld_common=sum(obs["q"][j] >= .1 for j in range(len(TASKS)) if j not in eligible),
                             present_world=sum(v > 0 for v in obs["p"]),
                             latches_open=sum(latch), releases=sum(release),
                             applied_min=round(min(paid), 4), applied_max=round(max(paid), 4),
                             applied_total=round(sum(applied), 6),
                             next_latched_share=round(latched_share, 4),
                             programs=obs["population_size"]))
        for j, episode in open_latch.items():
            episode["cleared_after_piece"] = None
            episodes.append(episode)
        last_obs = pieces[-1][1] if pieces else None
        common_last = sorted(((TASKS[j], round(last_obs["p"][j], 3), round(last_obs["q"][j], 3))
                              for j in range(len(TASKS)) if last_obs["p"][j] >= .1),
                             key=lambda x: -x[1]) if last_obs else []
        out[folder.name] = dict(arm=manifest["arm"], seed=manifest["seed"], pieces=len(pieces),
                                rows=rows, latch_episodes=episodes, common_at_last_piece=common_last,
                                schedule=[r["applied_pay"] for r, _ in pieces])
    # First piece at which the two arms of a seed were offered different pay.
    runs_only = [v for v in out.values() if "seed" in v]
    for seed in sorted({v["seed"] for v in runs_only}):
        runs = {v["arm"]: v for v in runs_only if v["seed"] == seed}
        if "full" in runs and "memoryless" in runs:
            a, b = runs["full"]["schedule"], runs["memoryless"]["schedule"]
            first = next((i + 1 for i, (x, y) in enumerate(zip(a, b))
                          if max(abs(p - q) for p, q in zip(x, y)) > 1e-12), None)
            largest = max((max(abs(p - q) for p, q in zip(x, y)) for x, y in zip(a, b)), default=0)
            print(f"seed {seed}: arms first offered different pay in piece {first}; "
                  f"largest difference for one detector {largest:.4f} doublings")
            out[f"compare_{seed}"] = dict(first_different_piece=first, largest_difference=largest)
    # CPU time
    cpu = [json.loads(line) for line in (base / "cpu.jsonl").read_text().splitlines() if line.strip()]
    pieces_cpu = [c["user"] + c["system"] for c in cpu if not c["analyze"]]
    assays_cpu = [c["user"] + c["system"] for c in cpu if c["analyze"]]
    out["cpu"] = dict(avida_pieces=len(pieces_cpu), piece_cpu_seconds=round(sum(pieces_cpu), 1),
                      assays=len(assays_cpu), assay_cpu_seconds=round(sum(assays_cpu), 1),
                      assay_mean=round(sum(assays_cpu) / max(1, len(assays_cpu)), 2),
                      piece_mean=round(sum(pieces_cpu) / max(1, len(pieces_cpu)), 2),
                      failures=[c for c in cpu if c["exit"] != 0])
    for name, run in out.items():
        if not name.startswith(("full", "memoryless")):
            continue
        print(f"\n== {name}: {run['pieces']} pieces")
        print("piece world all withheld present latches releases min max total latched_share")
        for r in run["rows"]:
            print(f"{r['piece']:5} {r['world_common']:5} {r['all_order_common']:3} {r['withheld_common']:8} "
                  f"{r['present_world']:7} {r['latches_open']:7} {r['releases']:8} {r['applied_min']:.3f} "
                  f"{r['applied_max']:.3f} {r['applied_total']:.3f} {r['next_latched_share']:.3f}")
        print("latch episodes:", json.dumps(run["latch_episodes"]))
        print("common at last piece (task, world share, all-order share):", run["common_at_last_piece"])
    print("\nCPU:", json.dumps(out["cpu"]))
    for value in out.values():
        value.pop("schedule", None) if isinstance(value, dict) else None
    (base / "reading.json").write_text(json.dumps(out, indent=1) + "\n")


if __name__ == "__main__":
    main()
