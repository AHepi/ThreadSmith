#!/usr/bin/env python3
"""Run one validated Part A ledger through the frozen patched rig-1 driver."""

from __future__ import annotations

import hashlib
import json
import re
import shlex
import subprocess
import sys
from pathlib import Path


ROOT = Path("/workspace/scratch/a549554d080c")
RIG_DIR = ROOT / "worktree/Language_handoff/rigs/rig 1 - arguments"
DRIVER = RIG_DIR / "patched/run_check.py"
RULES = RIG_DIR / "patched/checker_rules.pl"
RUNTIME = Path("/home/claude/sCASP/scasp")
VALIDATOR = ROOT / "deliverable/part_a/runs/validate_ledger.py"
OPTIONAL_PREDICATES = {
    "claim_because/3",
    "claim_since/3",
    "claim_plan/3",
    "claim_like/3",
    "exempt/2",
    "denied_because/3",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def identity(path: Path) -> dict[str, object]:
    return {"path": str(path), "sha256": sha256(path), "bytes": path.stat().st_size}


def command_text(command: list[str], cwd: Path | None = None, stdout: Path | None = None, stderr: Path | None = None) -> str:
    rendered = shlex.join(command)
    if stdout is not None:
        rendered += " > " + shlex.quote(str(stdout))
    if stderr is not None:
        rendered += " 2> " + shlex.quote(str(stderr))
    return (f"cd {shlex.quote(str(cwd))} && " if cwd is not None else "") + rendered


def run_to_files(command: list[str], stdout_path: Path, stderr_path: Path, cwd: Path | None = None) -> int:
    with stdout_path.open("wb") as stdout_handle, stderr_path.open("wb") as stderr_handle:
        done = subprocess.run(command, cwd=cwd, stdin=subprocess.DEVNULL, stdout=stdout_handle, stderr=stderr_handle)
    return done.returncode


def write_metadata(path: Path, metadata: dict[str, object]) -> None:
    path.write_text(json.dumps(metadata, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")


def classify_raw_errors(raw_text: str) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    expected: list[dict[str, object]] = []
    material: list[dict[str, object]] = []
    for block in re.split(r"(?=^=== )", raw_text, flags=re.MULTILINE):
        if not block.startswith("=== "):
            continue
        header = block.splitlines()[0]
        error_lines = [line for line in block.splitlines() if line.startswith("ERROR:")]
        if not error_lines:
            continue
        missing = re.findall(r"^ERROR: scasp_predicate `([^']+)' does not exist$", block, flags=re.MULTILINE)
        record = {"query_header": header, "missing_predicates": missing, "error_lines": error_lines}
        if missing and set(missing) <= OPTIONAL_PREDICATES:
            record["classification"] = "expected_missing_optional_predicate"
            expected.append(record)
        else:
            record["classification"] = "material_error"
            material.append(record)
    return expected, material


def main() -> int:
    if len(sys.argv) != 5 or sys.argv[1] not in {"new", "other"}:
        print("usage: run_case.py {new|other} LEDGER.json LEDGER.pl OUTPUT_DIR", file=sys.stderr)
        return 2

    side = sys.argv[1]
    json_path = Path(sys.argv[2]).resolve()
    pl_path = Path(sys.argv[3]).resolve()
    output_dir = Path(sys.argv[4]).resolve()
    output_dir.mkdir(parents=True, exist_ok=False)

    validation_stdout = output_dir / "validation.json"
    validation_stderr = output_dir / "validation.stderr.txt"
    pl_stdout = output_dir / "pl_parse.stdout.txt"
    pl_stderr = output_dir / "pl_parse.stderr.txt"
    report_path = output_dir / "report.txt"
    raw_path = output_dir / "raw_log.txt"
    driver_stderr = output_dir / "driver.stderr.txt"
    metadata_path = output_dir / "metadata.json"

    validator_command = [sys.executable, str(VALIDATOR), str(json_path), str(pl_path)]
    pl_command = ["swipl", "-q", "-f", "none", "-s", str(pl_path), "-t", "halt"]
    driver_command = ["python3", "patched/run_check.py", str(pl_path), str(raw_path)]

    metadata: dict[str, object] = {
        "author": "OpenAI Codex",
        "side": side,
        "case": pl_path.stem,
        "ledger_json": identity(json_path),
        "ledger_pl": identity(pl_path),
        "validator": identity(VALIDATOR),
        "driver": identity(DRIVER),
        "rules": identity(RULES),
        "runtime": identity(RUNTIME),
        "commands": {
            "validation": command_text(validator_command, stdout=validation_stdout, stderr=validation_stderr),
            "pl_parse": command_text(pl_command, stdout=pl_stdout, stderr=pl_stderr),
            "driver": command_text(driver_command, cwd=RIG_DIR, stdout=report_path, stderr=driver_stderr),
        },
    }

    validation_exit = run_to_files(validator_command, validation_stdout, validation_stderr)
    metadata["validation_exit_code"] = validation_exit
    if validation_exit != 0:
        metadata["status"] = "STOPPED_VALIDATION_ERROR"
        metadata["driver_run"] = False
        write_metadata(metadata_path, metadata)
        return 1

    pl_exit = run_to_files(pl_command, pl_stdout, pl_stderr)
    metadata["pl_parse_exit_code"] = pl_exit
    if pl_exit != 0:
        metadata["status"] = "STOPPED_PL_PARSE_ERROR"
        metadata["driver_run"] = False
        write_metadata(metadata_path, metadata)
        return 1

    scasp_version = subprocess.run([str(RUNTIME), "--version"], capture_output=True, text=True)
    swipl_version = subprocess.run(["swipl", "--version"], capture_output=True, text=True)
    metadata["versions"] = {
        "scasp": {"exit_code": scasp_version.returncode, "stdout": scasp_version.stdout.strip(), "stderr": scasp_version.stderr.strip()},
        "swipl": {"exit_code": swipl_version.returncode, "stdout": swipl_version.stdout.strip(), "stderr": swipl_version.stderr.strip()},
    }

    driver_exit = run_to_files(driver_command, report_path, driver_stderr, cwd=RIG_DIR)
    raw_text = raw_path.read_text(encoding="utf-8") if raw_path.exists() else ""
    expected_errors, material_errors = classify_raw_errors(raw_text)
    if driver_exit != 0:
        material_errors.append({"classification": "material_error", "driver_exit_code": driver_exit})

    metadata.update(
        {
            "driver_run": True,
            "driver_exit_code": driver_exit,
            "report": identity(report_path),
            "raw_log": identity(raw_path),
            "driver_stderr": identity(driver_stderr),
            "query_block_count": len(re.findall(r"^=== ", raw_text, flags=re.MULTILINE)),
            "timeout_true_count": len(re.findall(r"timed out: True", raw_text)),
            "expected_missing_optional_predicate_errors": expected_errors,
            "material_errors": material_errors,
            "status": "RUN_COMPLETED_WITH_EXPECTED_MISSING_OPTIONAL_PREDICATE_ERRORS" if expected_errors and not material_errors else ("RUN_COMPLETED_NO_ERRORS" if not material_errors else "STOPPED_MATERIAL_ERROR"),
            "interpretation_limit": "A missing optional-predicate query is an execution error, not a successful negative finding.",
        }
    )
    write_metadata(metadata_path, metadata)
    return 0 if not material_errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
