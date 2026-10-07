#!/usr/bin/env python3
"""Re-encode a pinned stock Avida test fixture by instruction name; no live run."""
from pathlib import Path
import sys


def words(path):
    return [text.split() for line in path.read_text().splitlines()
            if (text := line.split("#", 1)[0].strip())]


source, piece, destination = map(Path, sys.argv[1:])
instructions = [row[1] for row in words(piece / "instset-heads.cfg") if row[0] == "INST"]
assert len(instructions) == 26 and len(set(instructions)) == 26
symbols = dict(zip(instructions, "abcdefghijklmnopqrstuvwxyz"))
paths = [source / "avida-core/tests/resources_9r/config/9task.org", piece / "ancestor.org"]
sequences = ["".join(symbols[row[0]] for row in words(path)) for path in paths]
with destination.open("x") as stream:
    stream.write("#filetype genotype_data\n#format id num_units sequence\n")
    for key, count, sequence in zip((1, 2), (1, 9), sequences):
        stream.write(f"{key} {count} {sequence}\n")
print("synthetic fixture: stock 9task.org abundance=1; stock ancestor abundance=9")
print("instruction counts=" + ",".join(str(len(s)) for s in sequences))
