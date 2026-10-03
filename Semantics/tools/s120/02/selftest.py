#!/usr/bin/env python3
"""Self-authored rig cases fixed in SPEC-v1.md; no Avida process is invoked."""
import json
from pathlib import Path
import tempfile
from types import SimpleNamespace
import run


def close(actual, expected):
    assert len(actual) == len(expected)
    assert all(abs(a - e) < 1e-12 for a, e in zip(actual, expected)), (actual, expected)


def rejects(fn):
    try:
        fn()
    except ValueError:
        return
    raise AssertionError("case was not rejected")


def main():
    close(run.progress([[0.0], [0.2]], 5, 7.7), [1.54])
    print("development: A 0 -> 0.2 gives 1.54")
    close(run.progress([[0.0], [0.2], [0.2]], 1, 7.7), [0.0])
    close(run.progress([[0.2], [0.1]], 5, 7.7), [0.0])
    close(run.progress([[0.0, 0.0], [0.2, 0.1]], 5, 7.7), [1.54, 0.77])
    close(run.rarity([0, 0], 7.7), [3.85, 3.85])
    close(run.rarity([1, 0], 7.7), [7.7 / 3, 7.7 * 2 / 3])
    close(run.mean_schedule([[0.0, 2.0], [2.0, 4.0]]), [1.0, 3.0])
    current, changes = run.common_changes([0.2, 0.0, 0.2], [720, 0, 720], {1}, {0, 1})
    assert current == {0, 2}
    assert changes == {"common_360cells": 2, "cumulative_common": 3,
                       "first_common": [2], "reacquired": [0], "lost": [1]}
    assert "u 1 Exit\n" in run.event_text(2 - 1, False)
    assert "u begin LoadPopulation input.spop\n" in run.event_text(1, True)
    print("selectors: plateau=0 decline=0 growth_ratio=2 archive_ratio=1:2 fixed_means=1,3")
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        (root / "data").mkdir()
        tp, cp = root / "data/tasks.dat", root / "data/count.dat"
        tasks = [{"description": "Alpha"}, {"description": "Beta"}]
        good_tasks = "# 3: Alpha\n# 1: Update\n# 2: Beta\n1 2 4\n"
        good_counts = "# 1: update\n# 2: number of organisms\n1 10\n"
        tp.write_text(good_tasks)
        cp.write_text(good_counts)
        count, counts, shares = run.observe(root, tasks, 1)
        assert count == 10 and counts == [4, 2]
        close(shares, [0.4, 0.2])
        for bad in ("# 1: Update\n# 2: Beta\n1 2\n",
                    good_tasks.replace("# 3: Alpha", "# 2: Alpha"),
                    good_tasks.replace("1 2 4", "2 2 4"),
                    good_tasks.replace("1 2 4", "1 2 11")):
            tp.write_text(bad)
            rejects(lambda: run.observe(root, tasks, 1))
        tp.write_text(good_tasks)
        cp.write_text(good_counts.replace("1 10", "1 0"))
        rejects(lambda: run.observe(root, tasks, 1))
        path = root / "schedule.json"
        values = [[0.0, 2.0], [2.0, 4.0]]
        path.write_text(json.dumps({"complete": True, "tasks": tasks, "rig": {},
                                    "piece_updates": 2, "values": values, "seed": 1}))
        args = SimpleNamespace(piece_updates=2, pieces=2, mode="replay", seed=2)
        assert run.load_control(path, tasks, {}, args) == values
        args.seed = 1
        rejects(lambda: run.load_control(path, tasks, {}, args))
        args.mode = "fixed"
        rejects(lambda: run.load_control(path, tasks, {}, args))
    print("tables: reordered descriptions accepted; missing/duplicate/misaligned/oversized/empty rejected")
    print("controls: replay unchanged; same-seed fixed/replay rejected; N=2 exits at label 1")
    print("measurement: first=[2] reacquired=[0] lost=[1] cumulative=3")
    print("selftest complete; no Avida process executed")


if __name__ == "__main__":
    main()
