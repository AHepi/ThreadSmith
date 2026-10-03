#!/usr/bin/env python3
"""Small source-bound checks, including real stock Avida positive assay data."""
import argparse
import json
from pathlib import Path

from assay import TASKS, assay, atomic_json


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--source", type=Path, required=True)
    p.add_argument("--avida", type=Path, required=True)
    p.add_argument("--out", type=Path, required=True)
    args = p.parse_args()
    out = args.out.resolve()
    out.mkdir(parents=True, exist_ok=False)
    support = args.source / "avida-core/support/config"
    instructions = [line.split()[1] for line in (support / "instset-heads.cfg").read_text().splitlines()
                    if line.startswith("INST ")]
    symbols = dict(zip(instructions, "abcdefghijklmnopqrstuvwxyz"))
    ancestor = [line.split("#")[0].strip() for line in (support / "default-heads.org").read_text().splitlines()
                if line.split("#")[0].strip()]
    # All following instructions execute only inside Avida's virtual machine.
    prefixes = ["IO IO nop-C if-less nand IO nop-B", "IO IO nop-C swap if-less nand IO nop-B",
                "IO push pop nop-C nand IO nop-B"]
    rows = []
    for i, (prefix, count) in enumerate(zip(prefixes, (3, 1, 4)), 1):
        program = ancestor[:6] + prefix.split() + ancestor[6:]
        sequence = "".join(symbols[instruction] for instruction in program)
        (out / f"fixture_{i}.org").write_text("#inst_set heads_default\n#hw_type 0\n" + "\n".join(program) + "\n")
        rows.append(f"{i} {count} {sequence}")
    snapshot = out / "fixture.spop"
    snapshot.write_text("#filetype genotype_data\n#format id num_units sequence\n" + "\n".join(rows) + "\n")
    observation = assay(args.avida, args.source, snapshot, out / "assay", 73)
    programs = json.loads((out / "assay/programs.json").read_text())
    not_id, nand_id = TASKS.index("not"), TASKS.index("nand")
    nand_shares = [sum(row["count"] * row["orders"][order][nand_id] for row in programs)/8
                   for order in range(6)]
    assert observation["p"][not_id] == .5 and observation["q"][not_id] == .5
    assert observation["p"][nand_id] == .375 and observation["q"][nand_id] == 0
    assert min(nand_shares) == .125
    assert observation["cooc"][not_id][nand_id] == 0
    assert all(all(row["replication_test"]) for row in programs)
    summary = dict(population=8, virtual_programs=3, NOT_world=.5, NOT_all_orders=.5,
                   NAND_world=.375, NAND_each_order=nand_shares, NAND_all_orders=0,
                   NOT_NAND_same_program_all_orders=0,
                   checks="Positive task parsing, multiplicity weighting, all-six same-program conjunction, replication passed")
    atomic_json(out / "summary.json", summary)
    print(json.dumps(summary, sort_keys=True))


if __name__ == "__main__":
    main()
