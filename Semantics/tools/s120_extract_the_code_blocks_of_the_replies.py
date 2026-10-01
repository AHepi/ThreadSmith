# Plain note (log S120, written by Claude, Opus 5.5, 1 October 2026).
# What this does: copies every fenced code block of GPT 6 Astra's replies 01 and 02 to S119's
# briefs, UNCHANGED, into tools/s120/01/ and tools/s120/02/. Reply 03 has no code blocks.
# Each file holds exactly the lines between the opening and closing fence, followed by one
# newline (the same rule the replies' own extraction commands use). Nothing is added inside
# the files; where each file came from (reply, line numbers, SHA-256) is written to a note
# file "00 Where each file came from.md" in each folder.
# Run with "--check" to re-read the replies and confirm, byte for byte, that every file still
# equals its block.
import hashlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RETURNS = ROOT / "tests" / "S119 Returns from GPT 6 Astra"
OUT = ROOT / "tools" / "s120"

REPLIES = {
    "01": "01 Return - paying for anticipating what the world hands in next.md",
    "02": "02 Return - an execution environment that changes what it selects as it goes.md",
    "03": "03 Return - research, selecting with drives but no fixed objectives.md",
}

# Names for the blocks, in order of appearance. Named files keep the reply's own name.
NAMES = {
    "01": [
        "block-01 environment line for payment.txt",
        "work/anticipation.patch",
        "block-03 build steps, extraction command.sh",
        "block-04 build steps, clone, patch, build, test.sh",
        "tests/echo.org (as printed in the Tests section).txt",
        "tests/inc.org (as printed in the Tests section).txt",
        "block-07 ordinary runs unchanged, commands.sh",
        "block-08 reported build output.txt",
        "block-09 reported first harness compile error.txt",
        "block-10 reported final harness output.txt",
        "block-11 reported final comparison output.txt",
        "block-12 reported last line of each 400-update run.txt",
        "work/setup_tests.py",
        "work/build_test.py",
        "tests/check.cc",
        "work/compare.py",
    ],
    "02": [
        "block-01 reported configure and build commands.sh",
        "block-02 reported build output.txt",
        "block-03 reported task-check extraction output.txt",
        "block-04 path aliases.sh",
        "block-05 reported development arithmetic output.txt",
        "block-06 dry-run command.sh",
        "block-07 reported dry-run output.txt",
        "block-08 smoke-progress command.sh",
        "block-09 reported smoke-progress output.txt",
        "block-10 selftest command.sh",
        "block-11 reported selftest output.txt",
        "block-12 smoke-archive command.sh",
        "block-13 reported smoke-archive output.txt",
        "block-14 smoke-replay command.sh",
        "block-15 reported smoke-replay output.txt",
        "block-16 smoke-fixed command.sh",
        "block-17 reported smoke-fixed output.txt",
        "block-18 attack command.sh",
        "block-19 reported attack output.txt",
        "block-20 reported check_aggregation output.txt",
        "block-21 reported first measurement error.txt",
        "block-22 measure_orders smoke command.sh",
        "block-23 reported measure_orders smoke output.txt",
        "block-24 make_positive_fixture command.sh",
        "block-25 reported make_positive_fixture output.txt",
        "block-26 measure_orders positive fixture command.sh",
        "block-27 reported measure_orders positive fixture output.txt",
        "block-28 reported independent inspection output.txt",
        "block-29 reported calculate_sizes output.txt",
        "block-30 extraction command.sh",
        "block-31 illustrative 100,000-update commands, unrun.sh",
        "run.py",
        "avida.cfg.changes",
        "environment.cfg.template",
        "events-first.cfg",
        "events-reload.cfg",
        "measure_orders.py",
        "selftest.py",
        "attack.py",
        "check_aggregation.py",
        "make_positive_fixture.py",
        "calculate_sizes.py",
    ],
    "03": [],
}


def blocks(text):
    """Yield (first content line number, last content line number, info, body) per fenced block."""
    lines = text.split("\n")
    inside, start, info, body = False, 0, "", []
    for number, line in enumerate(lines, 1):
        if line.startswith("```"):
            if not inside:
                inside, start, info, body = True, number, line[3:], []
            else:
                inside = False
                yield start + 1, number - 1, info, "\n".join(body) + "\n"
        elif inside:
            body.append(line)
    if inside:
        raise SystemExit("unclosed code block")


def main(check):
    problems = 0
    for key, name in REPLIES.items():
        text = (RETURNS / name).read_text(encoding="utf-8")
        found = list(blocks(text))
        names = NAMES[key]
        if len(found) != len(names):
            raise SystemExit(f"reply {key}: {len(found)} blocks, {len(names)} names")
        folder = OUT / key
        rows = []
        for (first, last, info, body), filename in zip(found, names):
            target = folder / filename
            data = body.encode("utf-8")
            if check:
                same = target.read_bytes() == data
                problems += not same
                print(f"{key} {filename}: {'identical' if same else 'DIFFERENT'}")
            else:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(data)
            rows.append(f"| `{filename}` | {first}-{last} | {info or '(none)'} | "
                        f"{hashlib.sha256(data).hexdigest()} |")
        if not check:
            folder.mkdir(parents=True, exist_ok=True)
            note = [f"# Where each file came from (reply {key}, log S120)", "",
                    f"*Written by `tools/s120_extract_the_code_blocks_of_the_replies.py`. Every file in this "
                    f"folder is one fenced code block of GPT 6 Astra's reply `tests/S119 Returns from GPT 6 "
                    f"Astra/{name}`, copied unchanged: the lines between the fences, then one newline. "
                    f"Nothing was added inside any file. Line numbers are those of the reply's content lines. "
                    f"Files named `block-NN ...` had no name in the reply; the others keep the name the reply "
                    f"gives them. Run the script with `--check` to confirm byte for byte.*", ""]
            if rows:
                note += ["| File | Reply lines | Fence label | SHA-256 |", "|---|---|---|---|"] + rows
            else:
                note += ["The reply has no code blocks."]
            (folder / "00 Where each file came from.md").write_text("\n".join(note) + "\n", encoding="utf-8")
            print(f"reply {key}: {len(rows)} blocks written")
    if check:
        print("all identical" if problems == 0 else f"{problems} DIFFERENT")
        sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main("--check" in sys.argv[1:])
