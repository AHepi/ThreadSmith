#!/usr/bin/env python3
"""Create header-free reconstructed whole-rig logs with a byte-offset receipt."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sys


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> int:
    if len(sys.argv) != 2:
        raise SystemExit("usage: make_aggregate_logs.py DELIVERABLE_ROOT")
    root = Path(sys.argv[1]).resolve()
    outdir = root / "raw_logs" / "aggregate"
    outdir.mkdir(parents=True, exist_ok=True)

    buckets: dict[str, list[Path]] = {
        "rig1": [root / "raw_logs/historical/rig1_raw_log_before_plan45.txt"],
        "rig2": [root / "raw_logs/historical/rig2_raw_log_before_plan45.txt"],
    }
    buckets["rig1"].extend(sorted((root / "part_a/runs").glob("*/*/raw_log.txt")))
    for path in sorted((root / "part_b/runs").glob("**/raw_log.txt")):
        execution = path.with_name("execution.json")
        if not execution.is_file():
            continue
        rig = json.loads(execution.read_text(encoding="utf-8"))["rig"]
        buckets[rig].append(path)

    receipt: dict[str, object] = {
        "written_by": "OpenAI Codex, under frozen plan 45",
        "method": "Header-free byte concatenation: supplied whole historical log first, then isolated native plan-45 raw logs in lexicographic relative-path order.",
        "limits": "These are reconstructed convenience files, not contemporaneous shared append logs. Per-invocation raw_log.txt files remain primary evidence.",
        "rigs": {},
    }
    for rig, paths in buckets.items():
        target = outdir / f"{rig}_raw_log_reconstructed_whole.txt"
        offset = 0
        entries = []
        with target.open("wb") as stream:
            for path in paths:
                data = path.read_bytes()
                stream.write(data)
                entries.append({
                    "path": path.relative_to(root).as_posix(),
                    "start_byte": offset,
                    "end_byte_exclusive": offset + len(data),
                    "bytes": len(data),
                    "sha256": sha(data),
                })
                offset += len(data)
        whole = target.read_bytes()
        receipt["rigs"][rig] = {
            "aggregate_path": target.relative_to(root).as_posix(),
            "aggregate_bytes": len(whole),
            "aggregate_sha256": sha(whole),
            "segments": entries,
        }
    (outdir / "AGGREGATION_ORDER.json").write_text(
        json.dumps(receipt, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
