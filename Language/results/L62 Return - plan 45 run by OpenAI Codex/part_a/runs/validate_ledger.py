#!/usr/bin/env python3
"""Preflight a Part A JSON/Prolog ledger pair without changing either file."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def compact(term: str) -> str:
    return re.sub(r"\s+", "", term)


def main() -> int:
    if len(sys.argv) != 3:
        print("usage: validate_ledger.py LEDGER.json LEDGER.pl", file=sys.stderr)
        return 2

    json_path = Path(sys.argv[1]).resolve()
    pl_path = Path(sys.argv[2]).resolve()
    failures: list[str] = []

    try:
        with json_path.open("r", encoding="utf-8") as handle:
            document = json.load(handle)
    except Exception as exc:
        print(json.dumps({"status": "FAIL", "json_error": str(exc)}, indent=2))
        return 1

    lines = document.get("lines")
    if not isinstance(lines, dict):
        print(json.dumps({"status": "FAIL", "json_error": "top-level lines is not an object"}, indent=2))
        return 1

    source = pl_path.read_text(encoding="utf-8")
    uncommented = "\n".join(row.split("%", 1)[0] for row in source.splitlines())

    fact_ids = re.findall(r"(?m)^\s*line\(\s*([a-z][A-Za-z0-9_]*)\s*\)\s*\.\s*$", uncommented)
    guarded = re.findall(
        r"(?m)^\s*(.*?)\s*:-\s*line\(\s*([a-z][A-Za-z0-9_]*)\s*\)\s*\.\s*$",
        uncommented,
    )
    guard_heads: dict[str, list[str]] = defaultdict(list)
    for head, line_id in guarded:
        guard_heads[line_id].append(compact(head))

    json_ids = set(lines)
    fact_set = set(fact_ids)
    guard_set = set(guard_heads)

    duplicate_facts = sorted(line_id for line_id, count in Counter(fact_ids).items() if count != 1)
    if duplicate_facts:
        failures.append("line/1 declarations are not unique: " + ", ".join(duplicate_facts))
    if json_ids != fact_set:
        failures.append(
            "JSON IDs differ from PL line/1 IDs: "
            f"json_only={sorted(json_ids - fact_set)}, pl_only={sorted(fact_set - json_ids)}"
        )
    if json_ids != guard_set:
        failures.append(
            "JSON IDs differ from PL guard IDs: "
            f"json_without_guard={sorted(json_ids - guard_set)}, unknown_guards={sorted(guard_set - json_ids)}"
        )

    encoded_head_checks: dict[str, str] = {}
    for line_id, info in lines.items():
        expected = info.get("encoded_heads") if isinstance(info, dict) else None
        if expected is None:
            encoded_head_checks[line_id] = "not supplied"
            continue
        if not isinstance(expected, list) or not all(isinstance(item, str) for item in expected):
            failures.append(f"JSON encoded_heads for {line_id} is not a string list")
            encoded_head_checks[line_id] = "invalid"
            continue
        wanted = sorted(compact(item) for item in expected)
        got = sorted(guard_heads.get(line_id, []))
        if wanted != got:
            failures.append(f"encoded_heads mismatch for {line_id}: json={wanted}, pl={got}")
            encoded_head_checks[line_id] = "mismatch"
        else:
            encoded_head_checks[line_id] = "match"

    output = {
        "author": "OpenAI Codex",
        "status": "PASS" if not failures else "FAIL",
        "json_path": str(json_path),
        "pl_path": str(pl_path),
        "json_sha256": sha256(json_path),
        "pl_sha256": sha256(pl_path),
        "json_parse": "PASS",
        "json_line_ids": sorted(json_ids),
        "pl_line_ids": sorted(fact_set),
        "pl_guard_ids": sorted(guard_set),
        "encoded_head_checks": encoded_head_checks,
        "failures": failures,
    }
    print(json.dumps(output, indent=2, ensure_ascii=False, sort_keys=True))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
