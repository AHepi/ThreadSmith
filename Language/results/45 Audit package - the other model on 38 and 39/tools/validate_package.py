#!/usr/bin/env python3
"""Validate package structure and preservation, not the meaning of its texts.

Uses only the Python standard library. No network calls or semantic checker.
The manifest and this validator's generated result are excluded from the
manifest's own file inventory to avoid self-referential hashes.
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED = {"audit/file_manifest.json", "audit/structural_validation.json"}
CORPORA = {
    "corpus/inputs.jsonl": 260,
    "corpus/late_challenges.jsonl": 16,
    "corpus/literary_probes.jsonl": 48,
    "corpus/new_60.jsonl": 60,
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows = []
    for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        item = json.loads(line)
        require(isinstance(item, dict), f"{path.name}:{lineno}: expected object")
        rows.append(item)
    return rows


def sha_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def validate() -> dict[str, Any]:
    baseline = read_json(ROOT / "audit/baseline_freeze.json")
    for relative, expected in baseline["sha256"].items():
        require(sha_bytes((ROOT / relative).read_bytes()) == expected,
                f"Frozen input changed: {relative}")

    by_id: dict[str, dict[str, Any]] = {}
    inherited: dict[str, dict[str, Any]] = {}
    counts: dict[str, int] = {}
    for relative, expected_count in CORPORA.items():
        rows = read_jsonl(ROOT / relative)
        require(len(rows) == expected_count, f"Wrong input count: {relative}")
        counts[relative] = len(rows)
        for row in rows:
            identifier = row.get("id")
            require(isinstance(identifier, str) and bool(identifier),
                    f"Missing identifier in {relative}")
            require(identifier not in by_id, f"Duplicate identifier: {identifier}")
            require(isinstance(row.get("text"), str) and bool(row["text"].strip()),
                    f"Empty text: {identifier}")
            by_id[identifier] = row
            if relative != "corpus/new_60.jsonl":
                inherited[identifier] = row
    require(len(by_id) == 384 and len(inherited) == 324, "Inventory mismatch")

    receipts = read_jsonl(ROOT / "audit/coverage_324.jsonl")
    require(len(receipts) == 324, "Wrong inherited receipt count")
    receipt_ids = [r["id"] for r in receipts]
    require(len(set(receipt_ids)) == 324, "Duplicate receipt identifier")
    require(set(receipt_ids) == set(inherited), "Receipt/input coverage mismatch")
    for receipt in receipts:
        original = inherited[receipt["id"]]["text"].encode("utf-8")
        require(sha_bytes(original) == receipt["text_sha256"],
                f"Receipt refers to changed text: {receipt['id']}")
        require(receipt.get("evaluation_kind") ==
                "MANUAL_DOCUMENT_RULE_AUDIT_NOT_CHECKER_EXECUTION",
                f"Unexpected evaluation label: {receipt['id']}")
        require(bool(receipt.get("assessment")), f"Empty assessment: {receipt['id']}")

    cards = read_json(ROOT / "audit/new_case_cards.json")
    require(isinstance(cards, list) and len(cards) == 30, "Wrong new family count")
    new_ids = set()
    for card in cards:
        for suffix, field in (("A", "a"), ("B", "b")):
            identifier = f"{card['id']}-{suffix}"
            require(identifier not in new_ids, f"Duplicate new case: {identifier}")
            new_ids.add(identifier)
            require(identifier in by_id and by_id[identifier]["text"] == card[field],
                    f"New text/card mismatch: {identifier}")
    require(new_ids == set(by_id) - set(inherited), "New family coverage mismatch")

    seed_records = read_json(ROOT / "sources/inherited_literary_seeds.json")
    require(len(seed_records) == 20, "Wrong inherited literary metadata count")
    for seed in seed_records:
        require(seed["id"] in inherited and seed["text"] == inherited[seed["id"]]["text"],
                f"Literary source record mismatch: {seed['id']}")

    # Count the actual rows in the six new worked translation tables.
    worked = (ROOT / "03_Worked_translations.md").read_text(encoding="utf-8")
    sections = [s for s in re.split(r"(?m)^## ", worked)[1:] if "### The ledger" in s]
    require(len(sections) == 6, "Wrong worked translation count")
    expected_tables = [(5, 0, 0), (7, 0, 0), (0, 0, 0), (2, 1, 0), (5, 0, 0), (0, 0, 0)]
    table_counts = []
    for section, expected in zip(sections, expected_tables):
        ledger = section.split("### The ledger", 1)[1].split("### The bin", 1)[0]
        marks: Counter[str] = Counter()
        for line in ledger.splitlines():
            if not line.startswith("|"):
                continue
            cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
            if len(cells) == 5 and cells[3] in {"said", "filled in", "usual case"}:
                marks[cells[3]] += 1
        actual = (marks["said"], marks["filled in"], marks["usual case"])
        require(actual == expected, f"Wrong worked table counts: {section.splitlines()[0]}")
        require("TRANSLATION COMPLETE." in section, "Missing translation closing line")
        table_counts.append({"case": section.splitlines()[0], "said": actual[0],
                             "filled_in": actual[1], "usual_case": actual[2]})

    manifest = read_json(ROOT / "audit/file_manifest.json")
    actual_paths = {p.relative_to(ROOT).as_posix() for p in ROOT.rglob("*")
                    if p.is_file() and p.relative_to(ROOT).as_posix() not in EXCLUDED
                    and "__pycache__" not in p.parts}
    require(actual_paths == set(manifest["sha256"]), "Manifest inventory mismatch")
    for relative, expected in manifest["sha256"].items():
        payload = (ROOT / relative).read_bytes()
        require(bool(payload), f"Empty file: {relative}")
        require(sha_bytes(payload) == expected, f"Manifest hash mismatch: {relative}")

    return {
        "status": "STRUCTURAL_CHECKS_COMPLETED",
        "structural_validation_only": True,
        "semantic_checker_executed": False,
        "independent_witness_run": False,
        "semantic_pass_rate": None,
        "counts_by_corpus_file": counts,
        "registered_inputs": len(by_id),
        "inherited_text_receipts": len(receipts),
        "new_contrast_families": len(cards),
        "inherited_literary_source_records": len(seed_records),
        "frozen_files_verified": len(baseline["sha256"]),
        "manifest_files_verified": len(manifest["sha256"]),
        "worked_translation_tables": table_counts,
        "limitations": "Hashes and identifiers do not establish semantic validity or exhaustive audit coverage.",
    }


def main() -> int:
    try:
        result = validate()
    except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError) as exc:
        print(f"Structural validation failed: {exc}", file=sys.stderr)
        return 1
    destination = ROOT / "audit/structural_validation.json"
    destination.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
