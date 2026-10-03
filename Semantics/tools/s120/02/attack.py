#!/usr/bin/env python3
"""Added after planned cases passed: reject damaged donor schedules, without Avida."""
import json
from pathlib import Path
import tempfile
from types import SimpleNamespace
import run

with tempfile.TemporaryDirectory() as d:
    path = Path(d) / "schedule.json"
    args = SimpleNamespace(piece_updates=100, pieces=1, mode="replay", seed=2)
    original = {"complete": True, "tasks": [], "rig": {}, "piece_updates": 100,
                "values": [[]], "seed": 1}
    for key, value, label in (("complete", False, "incomplete schedule"),
                              ("rig", {"different": 1}, "different rig")):
        changed = dict(original)
        changed[key] = value
        path.write_text(json.dumps(changed))
        try:
            run.load_control(path, [], {}, args)
        except ValueError:
            print("rejected: " + label)
        else:
            raise AssertionError("accepted " + label)
print("added adversarial cases complete; no Avida process executed")
