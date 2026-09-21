#!/usr/bin/env python3
"""Run one frozen plan-45 ledger/driver pair with isolated evidence.

Written by OpenAI Codex for the plan-45 execution return.
This wrapper does not alter the ledger, driver, rules, or solver. It creates a
fresh raw log, captures the driver's exact stdout/stderr, and writes hashes and
basic integrity observations beside them.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys


AUTHOR = "OpenAI Codex, under frozen plan 45"
SCASP = Path("/home/claude/sCASP/scasp")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def validate_pair(ledger: Path) -> dict:
    metadata_path = ledger.with_suffix(".json")
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    prolog = ledger.read_text(encoding="utf-8")
    json_ids = set(metadata.get("lines", {}))
    declarations = set(re.findall(r"\bline\((\w+)\)\.", prolog))
    guard_ids = set(re.findall(r"\bline\((\w+)\)", prolog))
    if json_ids != declarations:
        raise SystemExit(
            f"JSON/Prolog line mismatch: json={sorted(json_ids)} prolog={sorted(declarations)}"
        )
    if not guard_ids <= json_ids:
        raise SystemExit(f"Unknown Prolog line guards: {sorted(guard_ids - json_ids)}")
    parsed = subprocess.run(
        ["swipl", "-q", "-g", "halt", "-s", str(ledger)],
        stdin=subprocess.DEVNULL,
        capture_output=True,
        text=True,
    )
    if parsed.returncode != 0:
        raise SystemExit(
            "SWI-Prolog parse failed\nSTDOUT:\n"
            + parsed.stdout
            + "\nSTDERR:\n"
            + parsed.stderr
        )
    return {
        "paragraph": metadata.get("paragraph"),
        "whose": metadata.get("whose"),
        "json_line_ids": sorted(json_ids),
        "swipl_parse_returncode": parsed.returncode,
        "swipl_parse_stderr": parsed.stderr,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--driver", required=True, type=Path)
    parser.add_argument("--rules", required=True, type=Path)
    parser.add_argument("--ledger", required=True, type=Path)
    parser.add_argument("--outdir", required=True, type=Path)
    parser.add_argument("--case-id", required=True)
    parser.add_argument("--rig", required=True)
    parser.add_argument("--version", required=True, choices=["frozen", "patched"])
    parser.add_argument("--role", required=True)
    args = parser.parse_args()

    if args.outdir.exists() and any(args.outdir.iterdir()):
        raise SystemExit(f"Refusing nonempty evidence directory: {args.outdir}")
    args.outdir.mkdir(parents=True, exist_ok=True)

    validation = validate_pair(args.ledger)
    raw_log = args.outdir / "raw_log.txt"
    command = [sys.executable, str(args.driver), str(args.ledger), str(raw_log)]
    completed = subprocess.run(
        command,
        stdin=subprocess.DEVNULL,
        capture_output=True,
        text=False,
    )
    (args.outdir / "report.stdout.txt").write_bytes(completed.stdout)
    (args.outdir / "wrapper.stderr.txt").write_bytes(completed.stderr)
    (args.outdir / "exit_code.txt").write_text(str(completed.returncode) + "\n", encoding="utf-8")

    raw_text = raw_log.read_text(encoding="utf-8", errors="replace") if raw_log.exists() else ""
    report_path = args.outdir / "report.stdout.txt"
    stderr_path = args.outdir / "wrapper.stderr.txt"
    metadata_path = args.ledger.with_suffix(".json")
    error_lines = [line for line in raw_text.splitlines() if "ERROR" in line.upper()]
    missing_predicate_lines = [
        line for line in error_lines if "unknown procedure" in line.lower() or "no rules for" in line.lower()
    ]
    material_error_lines = [line for line in error_lines if line not in missing_predicate_lines]
    query_headers = [line for line in raw_text.splitlines() if line.startswith("=== ")]

    evidence = {
        "written_by": AUTHOR,
        "case_id": args.case_id,
        "role": args.role,
        "rig": args.rig,
        "version": args.version,
        "command": command,
        "wrapper_exit_code": completed.returncode,
        "validation": validation,
        "hashes": {
            "ledger_pl": sha256(args.ledger),
            "ledger_json": sha256(metadata_path),
            "driver": sha256(args.driver),
            "rules": sha256(args.rules),
            "scasp": sha256(SCASP),
            "report_stdout": sha256(report_path),
            "wrapper_stderr": sha256(stderr_path),
            "raw_log": sha256(raw_log) if raw_log.exists() else None,
        },
        "raw_observations": {
            "query_block_count": len(query_headers),
            "timed_out_true_count": len(re.findall(r"timed out:\s*True", raw_text, re.I)),
            "error_line_count": len(error_lines),
            "missing_predicate_error_line_count": len(missing_predicate_lines),
            "material_error_line_count": len(material_error_lines),
            "error_lines": error_lines,
        },
        "interpretation_limit": (
            "The historical drivers suppress solver child return codes. This record proves what the "
            "wrapper and driver printed; it does not convert an errored query into semantic silence."
        ),
    }
    (args.outdir / "execution.json").write_text(
        json.dumps(evidence, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(json.dumps(evidence, indent=2, ensure_ascii=False))
    return completed.returncode


if __name__ == "__main__":
    raise SystemExit(main())
