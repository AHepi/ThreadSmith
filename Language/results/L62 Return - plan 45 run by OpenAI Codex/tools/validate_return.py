#!/usr/bin/env python3
"""Validate the frozen-plan-45 return tree and print a JSON receipt."""

from __future__ import annotations

from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
from typing import Any


EXCLUDED_EXACT = {
    "BUNDLE_MANIFEST.json",
    "RETURN_VALIDATION.json",
    "part_b/selected/F05_N17A_TRANSLATION.md",
    "part_b/selected/F05_N17B_TRANSLATION.md",
    "part_b/drafts/F01_F05/F05_TRANSLATIONS.md",
    "part_b/drafts/F01_F05/COVERAGE_AND_RUN_MATRIX.md",
    "part_b/drafts/F01_F05/README.md",
    "part_b/drafts/F01_F05/rig1/ledger_F05_N17A.json",
    "part_b/drafts/F01_F05/rig1/ledger_F05_N17A.pl",
    "part_b/drafts/F01_F05/rig1/ledger_F05_N17B.json",
    "part_b/drafts/F01_F05/rig1/ledger_F05_N17B.pl",
    "part_b/drafts/F01_F05/rig2/ledger_F05_N17B.json",
    "part_b/drafts/F01_F05/rig2/ledger_F05_N17B.pl",
}
EXCLUDED_PREFIXES = ("part_b/runs/F06_F10/_launcher/",)


def digest(path: Path) -> str:
    result = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            result.update(block)
    return result.hexdigest()


def included(root: Path, path: Path) -> bool:
    relative = path.relative_to(root).as_posix()
    return relative not in EXCLUDED_EXACT and not relative.startswith(EXCLUDED_PREFIXES)


def resolve_recorded(path_text: str, workspace: Path) -> Path:
    path = Path(path_text)
    return path if path.is_absolute() else workspace / path


def path_hash_records(value: Any) -> list[tuple[str, str]]:
    records: list[tuple[str, str]] = []
    if isinstance(value, dict):
        if isinstance(value.get("path"), str) and isinstance(value.get("sha256"), str):
            records.append((value["path"], value["sha256"]))
        for child in value.values():
            records.extend(path_hash_records(child))
    elif isinstance(value, list):
        for child in value:
            records.extend(path_hash_records(child))
    return records


def main() -> int:
    if len(sys.argv) != 3:
        raise SystemExit("usage: validate_return.py DELIVERABLE_ROOT SOURCE_ROOT")
    root = Path(sys.argv[1]).resolve()
    source = Path(sys.argv[2]).resolve()
    workspace = root.parent
    failures: list[str] = []

    files = [path for path in sorted(root.rglob("*")) if path.is_file() and included(root, path)]
    json_files = [path for path in files if path.suffix == ".json"]
    parsed: dict[Path, Any] = {}
    for path in json_files:
        try:
            parsed[path] = json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            failures.append(f"JSON parse failed: {path.relative_to(root)}: {exc}")

    pair_paths = [path for path in files if path.suffix == ".pl" and path.with_suffix(".json") in parsed]
    line_pairs_checked = 0
    swipl_pairs_checked = 0
    declaration_pattern = re.compile(r"(?:\A|(?<=\.))\s*line\(\s*([A-Za-z0-9_]+)\s*\)\s*\.", re.MULTILINE)
    reference_pattern = re.compile(r"\bline\(\s*([A-Za-z0-9_]+)\s*\)")
    for pl_path in pair_paths:
        json_path = pl_path.with_suffix(".json")
        document = parsed[json_path]
        lines = document.get("lines") if isinstance(document, dict) else None
        if not isinstance(lines, dict):
            failures.append(f"Ledger lines is not an object: {json_path.relative_to(root)}")
            continue
        text = "\n".join(row.split("%", 1)[0] for row in pl_path.read_text(encoding="utf-8").splitlines())
        declarations = declaration_pattern.findall(text)
        references = reference_pattern.findall(text)
        wanted = set(lines)
        if set(declarations) != wanted:
            failures.append(
                f"Line declaration mismatch: {pl_path.relative_to(root)}: "
                f"json_only={sorted(wanted - set(declarations))}, pl_only={sorted(set(declarations) - wanted)}"
            )
        if Counter(declarations) != Counter({line_id: 1 for line_id in wanted}):
            failures.append(f"Line declarations not unique: {pl_path.relative_to(root)}")
        if not wanted.issubset(set(references)):
            failures.append(f"Missing line references: {pl_path.relative_to(root)}")
        line_pairs_checked += 1
        result = subprocess.run(
            ["swipl", "-q", "-f", "none", "-s", str(pl_path), "-t", "halt"],
            capture_output=True,
            text=True,
            timeout=30,
            check=False,
        )
        if result.returncode != 0:
            failures.append(f"SWI-Prolog load failed: {pl_path.relative_to(root)}: {result.stderr.strip()}")
        swipl_pairs_checked += 1

    recorded_hashes_checked = 0
    receipt_files = [
        path for path in json_files if path.name in {"metadata.json", "execution.json", "query.json"}
    ]
    for receipt in receipt_files:
        data = parsed[receipt]
        for path_text, expected in path_hash_records(data):
            target = resolve_recorded(path_text, workspace)
            if not target.is_file():
                failures.append(f"Recorded component missing: {receipt.relative_to(root)} -> {path_text}")
                continue
            if digest(target) != expected:
                failures.append(f"Recorded component hash mismatch: {receipt.relative_to(root)} -> {path_text}")
            recorded_hashes_checked += 1

        if receipt.name == "execution.json":
            command = data.get("command", [])
            hashes = data.get("hashes", {})
            if len(command) < 3 or not isinstance(hashes, dict):
                failures.append(f"Malformed execution receipt: {receipt.relative_to(root)}")
                continue
            ledger_path = resolve_recorded(command[2], workspace)
            driver_path = resolve_recorded(command[1], workspace)
            rules_name = "laws.pl" if driver_path.name == "check2.py" else "checker_rules.pl"
            targets = {
                "ledger_pl": ledger_path,
                "ledger_json": ledger_path.with_suffix(".json"),
                "driver": driver_path,
                "rules": driver_path.parent / rules_name,
                "scasp": Path("/home/claude/sCASP/scasp"),
                "report_stdout": receipt.parent / "report.stdout.txt",
                "wrapper_stderr": receipt.parent / "wrapper.stderr.txt",
                "raw_log": receipt.parent / "raw_log.txt",
            }
            for key, target in targets.items():
                expected = hashes.get(key)
                if not isinstance(expected, str) or not target.is_file():
                    failures.append(f"Missing execution hash target: {receipt.relative_to(root)}:{key}")
                    continue
                if digest(target) != expected:
                    failures.append(f"Execution hash mismatch: {receipt.relative_to(root)}:{key}")
                recorded_hashes_checked += 1

        if receipt.name == "query.json":
            for key, filename in (("stdout_sha256", "solver.stdout.txt"), ("stderr_sha256", "solver.stderr.txt")):
                target = receipt.parent / filename
                expected = data.get(key)
                if not isinstance(expected, str) or not target.is_file():
                    failures.append(f"Missing query hash target: {receipt.relative_to(root)}:{key}")
                    continue
                if digest(target) != expected:
                    failures.append(f"Query output hash mismatch: {receipt.relative_to(root)}:{key}")
                recorded_hashes_checked += 1

    source_identity = parsed.get(root / "SOURCE_IDENTITY.json", {})
    source_identity_ok = bool(
        source_identity.get("all_source_files_byte_identical")
        and source_identity.get("file_count") == 194
        and not source_identity.get("byte_mismatches")
        and not source_identity.get("missing_from_extraction")
    )
    if not source_identity_ok:
        failures.append("Source identity receipt does not report a complete 194-file byte match")

    manifest_path = source / "results/58 Execution attempt - the other model on plan 45/prepared/part_b_manifest.json"
    expected_ids: list[str] = []
    if manifest_path.is_file():
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        for finding in manifest:
            expected_ids.extend(finding["resolved_input_ids"])
    else:
        failures.append(f"Source Part B manifest missing: {manifest_path}")
    coverage_rows = [
        line for line in (root / "part_b/PART_B_COVERAGE.md").read_text(encoding="utf-8").splitlines()
        if re.match(r"^\| F\d\d \|", line)
    ]
    coverage_ids: list[str] = []
    for row in coverage_rows:
        cells = row.split("|")
        coverage_ids.extend(re.findall(r"`([^`]+)`", cells[2]))
    if Counter(coverage_ids) != Counter(expected_ids) or len(expected_ids) != 48:
        failures.append("Part B coverage does not match the 48 source-manifest IDs exactly once")

    markdown_without_author = [
        path.relative_to(root).as_posix()
        for path in files
        if path.suffix == ".md" and "OpenAI Codex" not in path.read_text(encoding="utf-8")
    ]
    if markdown_without_author:
        failures.append("Markdown missing OpenAI Codex authorship: " + ", ".join(markdown_without_author))

    native_counts = Counter(
        path.relative_to(root).parts[2] for path in files
        if path.name == "execution.json" and path.relative_to(root).parts[:2] == ("part_b", "runs")
    )
    query_counts = Counter(
        path.relative_to(root).parts[2] for path in files
        if path.name == "query.json" and path.relative_to(root).parts[:2] == ("part_b", "runs")
    )
    expected_native = {"F01_F05": 10, "F06_F10": 28, "F11_F15": 12}
    expected_queries = {"F01_F05": 48, "F06_F10": 54, "F11_F15": 47}
    if dict(native_counts) != expected_native:
        failures.append(f"Part B native-run count mismatch: {dict(native_counts)}")
    if dict(query_counts) != expected_queries:
        failures.append(f"Part B direct-query count mismatch: {dict(query_counts)}")

    aggregate_receipt = parsed.get(root / "raw_logs/aggregate/AGGREGATION_ORDER.json", {})
    aggregate_segments = 0
    for rig, info in aggregate_receipt.get("rigs", {}).items():
        aggregate = root / info["aggregate_path"]
        if not aggregate.is_file() or digest(aggregate) != info["aggregate_sha256"]:
            failures.append(f"Aggregate hash mismatch: {rig}")
        aggregate_segments += len(info.get("segments", []))

    result = {
        "written_by": "OpenAI Codex, under frozen plan 45",
        "status": "PASS" if not failures else "FAIL",
        "scope": "Final return tree after deliberate staging exclusions",
        "checks": {
            "included_files_before_manifest_and_validation": len(files),
            "json_files_parsed": len(json_files),
            "json_prolog_pairs_line_checked": line_pairs_checked,
            "json_prolog_pairs_swipl_loaded": swipl_pairs_checked,
            "recorded_hashes_checked": recorded_hashes_checked,
            "source_files_byte_identical": 194 if source_identity_ok else 0,
            "part_a_translations": len(list((root / "part_a/translations").glob("*_translation.md"))),
            "part_a_ledger_pairs": len(list((root / "part_a/ledgers").glob("*/*.json"))),
            "part_a_sameness_outputs": len(list((root / "part_a/sameness/raw").glob("*_sameness.txt"))),
            "part_b_coverage_ids": len(coverage_ids),
            "part_b_native_runs": sum(native_counts.values()),
            "part_b_native_by_slice": dict(sorted(native_counts.items())),
            "part_b_direct_queries": sum(query_counts.values()),
            "part_b_direct_by_slice": dict(sorted(query_counts.items())),
            "markdown_files_with_authorship": sum(path.suffix == ".md" for path in files),
            "aggregate_rig_logs": len(aggregate_receipt.get("rigs", {})),
            "aggregate_segments": aggregate_segments,
        },
        "excluded_staging_artifacts": sorted(EXCLUDED_EXACT - {"BUNDLE_MANIFEST.json", "RETURN_VALIDATION.json"}),
        "excluded_staging_prefixes": list(EXCLUDED_PREFIXES),
        "failures": failures,
    }
    print(json.dumps(result, indent=2, ensure_ascii=False, sort_keys=True))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
