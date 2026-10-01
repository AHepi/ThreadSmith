#!/usr/bin/env python3
# Plain note (log S122, written by Claude, Opus 5.5, 1 October 2026).
# What this does: the cheapest test replies 03 and 04 ask of any selector with a memory, applied to
# reply 01's selector (tools/s122/01/temporal_selector/selector.py, imported unchanged): give it two
# histories made of the SAME assay observations in a DIFFERENT order, ending in the SAME present
# observation, and see whether the pay it offers next differs. The memory-wiped arm (a fresh
# selector stepped once on the present) must offer the same pay after both. The observations are
# real: the six-order assays of the S122 pilot's run "full_2201" (scratch space s122/pilot/).
# History A is the pieces in the order they happened; history B is the same pieces reversed
# (except the last, which is the shared present). No Avida process is run; only Python.
# Usage: python3 tools/s122_identical_present_different_history_check.py <scratch s122 folder>
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "s122" / "01" / "temporal_selector"))
from selector import Selector  # noqa: E402  (reply 01's code, unchanged)


def main():
    run = Path(sys.argv[1]).resolve() / "pilot" / "full_2201"
    observations = [json.loads(p.read_text()) for p in sorted(run.glob("piece_*/assay/observation.json"))]
    tasks = json.loads((run / "manifest.json").read_text())["tasks"]
    obs = [{k: o[k] for k in ("p", "q", "cooc")} for o in observations]
    present, earlier = obs[-1], obs[:-1]
    histories = {"as it happened": earlier, "reversed": list(reversed(earlier))}
    results = {}
    for name, history in histories.items():
        full = Selector(len(tasks))
        for o in history:
            full.step(o)
        results[name] = full.step(present)
    wiped = Selector(len(tasks)).step(present)["pay"]
    a, b = results["as it happened"]["pay"], results["reversed"]["pay"]
    diff = [abs(x - y) for x, y in zip(a, b)]
    j = max(range(len(diff)), key=diff.__getitem__)
    print(f"{len(earlier)} earlier observations, one shared present (piece {len(obs)})")
    print(f"temporal selector: largest pay difference between the two histories {diff[j]:.4f} doublings "
          f"({tasks[j]}: {a[j]:.4f} as it happened, {b[j]:.4f} reversed); "
          f"detectors differing by more than 0.01: {sum(d > 0.01 for d in diff)}")
    for name, r in results.items():
        d = r["diagnostics"]
        print(f"  {name}: open latches {sum(d['latch'])}, largest pay {max(r['pay']):.4f}, "
              f"smallest paid {min(r['pay'][i] for i in range(len(tasks)) if i % 7 != 6):.4f}")
    print("memory-wiped selector: the same present gives the same pay whatever came before "
          f"(it never sees the history); its largest pay {max(wiped):.4f}")
    common = [tasks[i] for i in range(len(tasks)) if present["q"][i] >= .1]
    print("common in all orders at the present:", common)


if __name__ == "__main__":
    main()
