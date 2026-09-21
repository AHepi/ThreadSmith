#!/usr/bin/env python3
"""Compare the extracted handoff tree with every file byte in its source ZIP."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sys
import zipfile


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> int:
    if len(sys.argv) != 3:
        raise SystemExit("usage: source_identity.py SOURCE.zip EXTRACTED_ROOT")
    archive = Path(sys.argv[1])
    root = Path(sys.argv[2])
    rows: dict[str, dict[str, object]] = {}
    mismatches: list[str] = []
    missing: list[str] = []
    with zipfile.ZipFile(archive) as zf:
        names = [name for name in zf.namelist() if not name.endswith("/")]
        prefixes = {name.split("/", 1)[0] for name in names if "/" in name}
        if len(prefixes) != 1:
            raise SystemExit(f"expected one archive root, found {sorted(prefixes)}")
        prefix = next(iter(prefixes)) + "/"
        for name in sorted(names):
            rel = name[len(prefix):] if name.startswith(prefix) else name
            archived = zf.read(name)
            current_path = root / rel
            if not current_path.is_file():
                missing.append(rel)
                continue
            current = current_path.read_bytes()
            equal = archived == current
            if not equal:
                mismatches.append(rel)
            rows[rel] = {
                "archive_sha256": sha(archived),
                "extracted_sha256": sha(current),
                "bytes_equal": equal,
            }
    report = {
        "written_by": "OpenAI Codex, under frozen plan 45",
        "source_archive": str(archive),
        "source_archive_sha256": sha(archive.read_bytes()),
        "extracted_root": str(root),
        "file_count": len(rows),
        "missing_from_extraction": missing,
        "byte_mismatches": mismatches,
        "all_source_files_byte_identical": not missing and not mismatches,
        "files": rows,
    }
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0 if report["all_source_files_byte_identical"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
