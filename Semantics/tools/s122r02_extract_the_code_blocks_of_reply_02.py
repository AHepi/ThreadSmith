# Plain note (log S122, reply 02; written by Claude, Opus 5.5, 1 October 2026).
# What this does: copies every fenced code block of GPT 6 Astra's reply 02 to S121's briefs
# ("programs that need history"), UNCHANGED, into tools/s122/02/. Each file holds exactly the
# lines between the opening and closing fence, followed by one newline (the rule S120 and the
# S122 agent used; it is also the rule of the reply's own extractor, which writes body + "\n").
# Nothing is added inside the files. Files the reply names ("<!-- artifact: path -->") keep that
# path; the others are named "block-NN ...". Where each file came from (reply lines, fence label,
# SHA-256) is written to "00 Where each file came from.md".
# Run with "--check" to re-read the reply and confirm, byte for byte, that every file still
# equals its block, and that the reply's one stated hash (of the combined patch) matches.
import hashlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPLY = ROOT / "tests" / "S121 Returns from GPT 6 Astra" / "02 Return - programs that need history.md"
OUT = ROOT / "tools" / "s122" / "02"
STATED_PATCH_SHA256 = "2c0457b79294a6f0c8562588a31e48149dcc4f71c8650e8a1982fc0e62975ef6"

NAMES = [
    "block-01 example training reaction.txt",
    "history/full.patch",
    "block-03 order specimen.org",
    "block-04 interval specimen, W=2.org",
    "block-05 sequence specimen.org",
    "block-06 the reply's own extractor.sh",
    "block-07 build and test commands.sh",
    "block-08 400-update run commands.sh",
    "block-09 reported comparison output.txt",
    "block-10 reported final run line.txt",
    "block-11 reported final build lines.txt",
    "block-12 reported earlier build failures.txt",
    "block-13 reported final history-harness output.txt",
    "block-14 reported anticipation-regression output.txt",
    "history/spec-v1.txt",
    "history/setup.py",
    "history/check.cc",
    "history/build.py",
    "work/setup_tests.py",
    "work/build_test.py",
    "tests/check.cc",
    "work/compare.py",
    "history/test-first.log",
]


def blocks(text):
    """Yield (first content line, last content line, fence label, body) per fenced block."""
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
    text = REPLY.read_text(encoding="utf-8")
    found = list(blocks(text))
    if len(found) != len(NAMES):
        raise SystemExit(f"{len(found)} blocks, {len(NAMES)} names")
    problems, rows = 0, []
    for (first, last, info, body), name in zip(found, NAMES):
        data = body.encode("utf-8")
        target = OUT / name
        if check:
            same = target.read_bytes() == data
            problems += not same
            print(f"{name}: {'identical' if same else 'DIFFERENT'}")
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
        rows.append(f"| `{name}` | {first}-{last} | {info or '(none)'} | {hashlib.sha256(data).hexdigest()} |")
    patch_hash = hashlib.sha256((OUT / "history/full.patch").read_bytes()).hexdigest()
    patch_ok = patch_hash == STATED_PATCH_SHA256
    print(f"history/full.patch SHA-256 {patch_hash}: {'matches' if patch_ok else 'DOES NOT match'} the reply's stated hash")
    if not check:
        note = ["# Where each file came from (reply 02, log S122)", "",
                "*Written by `tools/s122r02_extract_the_code_blocks_of_reply_02.py`. Every file in this folder is one "
                "fenced code block of GPT 6 Astra's reply `tests/S121 Returns from GPT 6 Astra/02 Return - programs "
                "that need history.md`, copied unchanged: the lines between the fences, then one newline (the reply's "
                "own extractor writes files the same way). Nothing was added inside any file. Line numbers are those "
                "of the reply's content lines. Files the reply names (`<!-- artifact: ... -->`) keep its path; the "
                "others are named `block-NN ...`. Run the script with `--check` to confirm byte for byte.*", "",
                f"*The reply gives one hash: the combined patch's SHA-256 `{STATED_PATCH_SHA256}`. "
                f"`history/full.patch` here {'matches it' if patch_ok else 'does NOT match it'}. The reply's own "
                "extractor (block 06), run on the reply, gives the same ten named files byte for byte.*", "",
                "| File | Reply lines | Fence label | SHA-256 |", "|---|---|---|---|"] + rows
        (OUT / "00 Where each file came from.md").write_text("\n".join(note) + "\n", encoding="utf-8")
        print(f"{len(rows)} blocks written")
    if problems or not patch_ok:
        raise SystemExit(1)


if __name__ == "__main__":
    main("--check" in sys.argv[1:])
