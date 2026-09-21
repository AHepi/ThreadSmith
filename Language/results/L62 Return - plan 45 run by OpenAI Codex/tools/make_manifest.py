#!/usr/bin/env python3
"""Print a deterministic SHA-256 manifest for the plan-45 return tree."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sys


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def main() -> int:
    if len(sys.argv) != 2:
        raise SystemExit("usage: make_manifest.py DELIVERABLE_ROOT")
    root = Path(sys.argv[1]).resolve()
    excluded = {
        "BUNDLE_MANIFEST.json",
        # Superseded F05 drafting artifacts are deliberately not returned.
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
    excluded_prefixes = ("part_b/runs/F06_F10/_launcher/",)

    def included(path: Path) -> bool:
        relative = path.relative_to(root).as_posix()
        return relative not in excluded and not relative.startswith(excluded_prefixes)

    files = {
        path.relative_to(root).as_posix(): {
            "sha256": digest(path),
            "bytes": path.stat().st_size,
        }
        for path in sorted(root.rglob("*"))
        if path.is_file() and included(path)
    }
    result = {
        "written_by": "OpenAI Codex, under frozen plan 45",
        "purpose": "Execution evidence and draft results for frozen Language test plan 45",
        "hash_algorithm": "SHA-256",
        "path_base": "archive root",
        "manifest_self_excluded": True,
        "excluded_staging_artifacts": sorted(excluded - {"BUNDLE_MANIFEST.json"}),
        "excluded_staging_prefixes": list(excluded_prefixes),
        "file_count": len(files),
        "files": files,
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
