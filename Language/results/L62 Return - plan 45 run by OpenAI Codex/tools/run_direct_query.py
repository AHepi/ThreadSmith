#!/usr/bin/env python3
"""Run one transparent supplemental s(CASP) query for plan 45.

Written by OpenAI Codex. The query is assessment machinery, not a source line.
The exact rules and ledger bytes are preserved by hash. An optional line removal
uses the same declaration-removal operation as the native drivers.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import tempfile


AUTHOR = "OpenAI Codex, under frozen plan 45"
SCASP = Path("/home/claude/sCASP/scasp")


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--rules", required=True, type=Path)
    parser.add_argument("--ledger", required=True, type=Path)
    parser.add_argument("--query", required=True)
    parser.add_argument("--outdir", required=True, type=Path)
    parser.add_argument("--remove-line", action="append", default=[])
    parser.add_argument("--label", required=True)
    args = parser.parse_args()

    if args.outdir.exists() and any(args.outdir.iterdir()):
        raise SystemExit(f"Refusing nonempty output directory: {args.outdir}")
    args.outdir.mkdir(parents=True, exist_ok=True)

    ledger_text = args.ledger.read_text(encoding="utf-8")
    for line_id in args.remove_line:
        pattern = r"\bline\(%s\)\.\s*" % re.escape(line_id)
        ledger_text, count = re.subn(pattern, "", ledger_text, count=1)
        if count != 1:
            raise SystemExit(f"Could not remove exactly one declaration for line {line_id}")

    program = args.rules.read_text(encoding="utf-8") + "\n" + ledger_text + "\n?- " + args.query + ".\n"
    with tempfile.NamedTemporaryFile("w", suffix=".pl", encoding="utf-8", delete=False) as handle:
        handle.write(program)
        program_path = Path(handle.name)
    try:
        completed = subprocess.run(
            [str(SCASP), "--tree", "--human", "-s0", "--unknown=fail", str(program_path)],
            stdin=subprocess.DEVNULL,
            capture_output=True,
            text=False,
            timeout=20,
            env={"LANG": "C.UTF-8"},
        )
    except subprocess.TimeoutExpired as exc:
        completed = None
        stdout = exc.stdout or b""
        stderr = exc.stderr or b""
        timed_out = True
    else:
        stdout = completed.stdout
        stderr = completed.stderr
        timed_out = False
    finally:
        program_path.unlink(missing_ok=True)

    stdout_path = args.outdir / "solver.stdout.txt"
    stderr_path = args.outdir / "solver.stderr.txt"
    stdout_path.write_bytes(stdout)
    stderr_path.write_bytes(stderr)
    record = {
        "written_by": AUTHOR,
        "label": args.label,
        "rules": {"path": str(args.rules), "sha256": digest(args.rules)},
        "ledger": {"path": str(args.ledger), "sha256": digest(args.ledger)},
        "scasp": {"path": str(SCASP), "sha256": digest(SCASP)},
        "query": args.query,
        "removed_line_declarations": args.remove_line,
        "timed_out": timed_out,
        "solver_exit_code": None if completed is None else completed.returncode,
        "stdout_sha256": digest(stdout_path),
        "stderr_sha256": digest(stderr_path),
        "answer_block_count": len(re.findall(rb"%\s+Answer \d+", stdout)),
        "error_present": b"ERROR" in stdout.upper() or b"ERROR" in stderr.upper(),
        "interpretation_limit": "A supplemental query is not a native report and does not become a source commitment.",
    }
    (args.outdir / "query.json").write_text(
        json.dumps(record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    (args.outdir / "exit_code.txt").write_text(
        ("TIMEOUT" if completed is None else str(completed.returncode)) + "\n", encoding="utf-8"
    )
    print(json.dumps(record, indent=2, ensure_ascii=False))
    return 124 if completed is None else completed.returncode


if __name__ == "__main__":
    raise SystemExit(main())
