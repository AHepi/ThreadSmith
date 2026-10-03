# Plain note (log S122, written by Claude, Opus 5.5, 1 October 2026).
# What this does: copies every fenced code block of GPT 6 Astra's reply 01 to S121's briefs,
# UNCHANGED, into tools/s122/01/. Each file holds exactly the lines between the opening and
# closing fence, followed by one newline (the rule S120 used). Nothing is added inside the files.
# Replies 03 and 04 came as Word files and hold no code. Reply 04 does hold two pasted outputs of
# arithmetic checks, set in a fixed-width font; those paragraphs are copied, unchanged and in
# order (one paragraph per line), into tools/s122/04/, so they can be compared with a rerun.
# Reply 03 has no code and no fixed-width text; its folder note says so.
# Where each file came from (reply, line numbers or paragraph numbers, SHA-256) is written to
# "00 Where each file came from.md" in each folder.
# Run with "--check" to re-read the replies and confirm, byte for byte, that every file still
# equals its block.
import hashlib
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RETURNS = ROOT / "tests" / "S121 Returns from GPT 6 Astra"
OUT = ROOT / "tools" / "s122"

REPLY01 = "01 Return - the execution environment as a temporal, neuron-like selector.md"
REPLY03 = "03 Return - research, temporal mechanisms that evaluate or select.docx"
REPLY04 = "04 Return - does temporal state close the gaps.docx"

# Names for reply 01's blocks, in order of appearance. Named files keep the reply's own path.
NAMES01 = [
    "block-01 build commands.sh",
    "block-02 reported selected build output.txt",
    "block-03 initial tiny run command.sh",
    "block-04 final frozen tiny run command.sh",
    "block-05 reported output of both full runs.txt",
    "block-06 replay command.sh",
    "block-07 reported replay output.txt",
    "block-08 fixed command.sh",
    "block-09 reported fixed output.txt",
    "block-10 completed-run resume command.sh",
    "block-11 two failed fixture development commands.sh",
    "block-12 reported failure output of each fixture attempt.txt",
    "block-13 final fixture command.sh",
    "block-14 reported final fixture output.txt",
    "block-15 reported component probes after version 1.2.txt",
    "block-16 reported independent probes of version 1.1, before the amendment.txt",
    "block-17 reported independent probes after version 1.2.txt",
    "block-18 reported task label permutation probe.txt",
    "block-19 reported final integration summaries.txt",
    "temporal_selector/selector.py",
    "temporal_selector/assay.py",
    "temporal_selector/runner.py",
    "temporal_selector/summarize.py",
    "temporal_selector/checks.py",
    "temporal_selector/integration_checks.py",
    "independent_test.py",
    "evidence/additional_check.py",
    "block-28 reported file hashes.txt",
]

# Reply 04's fixed-width paragraphs fall in two runs: paragraphs of the first check, then the second.
NAMES04 = ["block-01 reported output of the first arithmetic check.txt",
           "block-02 reported output of the second arithmetic check.txt"]


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


def docx_fixed_width_runs(path):
    """Return runs of consecutive fixed-width (Consolas) paragraphs as (first, last, text)."""
    xml = zipfile.ZipFile(path).read("word/document.xml").decode("utf-8")
    paragraphs = re.findall(r"<w:p[ >].*?</w:p>", xml, flags=re.S)
    runs, current = [], []
    for number, p in enumerate(paragraphs, 1):
        if "Consolas" in p:
            text = "".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", p))
            text = text.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
            current.append((number, text))
        elif current:
            runs.append(current)
            current = []
    if current:
        runs.append(current)
    return [(r[0][0], r[-1][0], "\n".join(t for _, t in r) + "\n") for r in runs]


def write_or_check(folder, filename, data, check, problems):
    target = folder / filename
    if check:
        same = target.read_bytes() == data
        problems[0] += not same
        print(f"{folder.name} {filename}: {'identical' if same else 'DIFFERENT'}")
    else:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)


def main(check):
    problems = [0]
    # Reply 01
    text = (RETURNS / REPLY01).read_text(encoding="utf-8")
    found = list(blocks(text))
    if len(found) != len(NAMES01):
        raise SystemExit(f"reply 01: {len(found)} blocks, {len(NAMES01)} names")
    folder = OUT / "01"
    rows = []
    for (first, last, info, body), filename in zip(found, NAMES01):
        data = body.encode("utf-8")
        write_or_check(folder, filename, data, check, problems)
        rows.append(f"| `{filename}` | {first}-{last} | {info or '(none)'} | {hashlib.sha256(data).hexdigest()} |")
    if not check:
        note = ["# Where each file came from (reply 01, log S122)", "",
                f"*Written by `tools/s122_extract_the_code_blocks_of_the_replies.py`. Every file in this folder "
                f"is one fenced code block of GPT 6 Astra's reply `tests/S121 Returns from GPT 6 Astra/{REPLY01}`, "
                f"copied unchanged: the lines between the fences, then one newline. Nothing was added inside any "
                f"file. Line numbers are those of the reply's content lines. Files named `block-NN ...` had no name "
                f"in the reply; the others keep the path the reply gives them (its section \"Files to save\"). Run "
                f"the script with `--check` to confirm byte for byte. The reply's own SHA-256 list (block 28) "
                f"is compared with these files in the check of reply 01.*", "",
                "| File | Reply lines | Fence label | SHA-256 |", "|---|---|---|---|"] + rows
        (folder / "00 Where each file came from.md").write_text("\n".join(note) + "\n", encoding="utf-8")
        print(f"reply 01: {len(rows)} blocks written")
    # Reply 03: nothing to extract; confirm there is no fixed-width text.
    runs03 = docx_fixed_width_runs(RETURNS / REPLY03)
    if runs03:
        raise SystemExit("reply 03 has fixed-width text; extend this script")
    if not check:
        folder = OUT / "03"
        folder.mkdir(parents=True, exist_ok=True)
        (folder / "00 Where each file came from.md").write_text(
            "# Where each file came from (reply 03, log S122)\n\n"
            f"*Reply 03 (`tests/S121 Returns from GPT 6 Astra/{REPLY03}`) holds no code and no fixed-width "
            "text: nothing to extract. Its one reported output line (\"AUDIT_ROWS=22...\", in its last section) "
            "is ordinary text and is quoted in the check of reply 03.*\n", encoding="utf-8")
    # Reply 04: two runs of fixed-width output paragraphs.
    runs04 = docx_fixed_width_runs(RETURNS / REPLY04)
    if len(runs04) != len(NAMES04):
        raise SystemExit(f"reply 04: {len(runs04)} fixed-width runs, {len(NAMES04)} names")
    folder = OUT / "04"
    rows = []
    for (first, last, body), filename in zip(runs04, NAMES04):
        data = body.encode("utf-8")
        write_or_check(folder, filename, data, check, problems)
        rows.append(f"| `{filename}` | paragraphs {first}-{last} | {hashlib.sha256(data).hexdigest()} |")
    if not check:
        note = ["# Where each file came from (reply 04, log S122)", "",
                f"*Written by `tools/s122_extract_the_code_blocks_of_the_replies.py`. Reply 04 "
                f"(`tests/S121 Returns from GPT 6 Astra/{REPLY04}`) holds no code. It does hold two pasted "
                f"outputs of its arithmetic checks, set in a fixed-width font. Each file is one run of "
                f"consecutive fixed-width paragraphs of `word/document.xml`, copied unchanged, one paragraph per "
                f"line, then one newline. Paragraph numbers count every `w:p` of the document body from 1.*", "",
                "| File | Where | SHA-256 |", "|---|---|---|"] + rows
        (folder / "00 Where each file came from.md").write_text("\n".join(note) + "\n", encoding="utf-8")
        print(f"reply 04: {len(rows)} output runs written")
    if check:
        print("all identical" if problems[0] == 0 else f"{problems[0]} DIFFERENT")
        sys.exit(1 if problems[0] else 0)


if __name__ == "__main__":
    main("--check" in sys.argv[1:])
