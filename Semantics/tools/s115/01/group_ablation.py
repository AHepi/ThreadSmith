# NOTE (added by Claude, log S115): this file is 'group_ablation.py', copied unchanged from the appendix of
# GPT 6 Astra's reply 01 ('tests/S115 Returns from GPT 6 Astra/01 Return - measuring what is learned,
# with stock Avida only.md'). Only these note lines were added. It has not been run on S113's data;
# see 'results/S115 Checking the Astra returns/01 Check of reply 01 - measuring what is learned.md'.
#!/usr/bin/env python3
"""python group_ablation.py selected-lineage.spop groups.csv group-analyze.cfg 0 8 --inputs suite/inputs.tsv"""
import csv
import json
import argparse
import re
import sys
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('population',type=Path)
parser.add_argument('groupfile',type=Path)
parser.add_argument('outfile',type=Path)
parser.add_argument('task_ids',nargs='+',type=int)
parser.add_argument('--inputs',type=Path,required=True,help='Suite inputs.tsv; core profile only')
args=parser.parse_args()
population, groupfile, outfile=args.population,args.groupfile,args.outfile
task_ids=list(dict.fromkeys(args.task_ids))
with args.inputs.open(newline='') as f:
    triples=[tuple(int(r['input'+str(i)]) for i in range(3)) for r in csv.DictReader(f,delimiter='\t') if r['profile']=='core']
if len(triples)<2 or len(set(triples))!=len(triples): raise SystemExit('Need distinct core triples')
if not task_ids or min(task_ids) < 0:
    raise SystemExit("Supply nonnegative task indices from the assay manifest")
columns = None
sequences = {}
for line in population.read_text().splitlines():
    if line.startswith("#format "):
        columns = line.split()[1:]
    elif line.strip() and not line.lstrip().startswith("#"):
        if columns is None:
            raise SystemExit("Missing #format header")
        fields = line.split()
        if len(fields) != len(columns):
            raise SystemExit("Malformed population row")
        row = dict(zip(columns, fields))
        seq = row["sequence"]
        if re.fullmatch("[a-z]+", seq) is None:
            raise SystemExit("Expected unchanged 26-instruction heads sequences")
        ident = int(row["id"])
        if ident in sequences:
            raise SystemExit("Duplicate sequence ID: use one segment")
        sequences[ident] = seq
groups = []
with groupfile.open(newline="") as handle:
    for row in csv.DictReader(handle):
        ident = int(row["id"])
        sites = sorted(set(int(x) for x in row["sites"].split(";")))
        seq = sequences[ident]
        if not sites or sites[0] < 1 or sites[-1] > len(seq):
            raise SystemExit("Group has an out-of-range site")
        groups.append((ident, sites))
if not groups:
    raise SystemExit("No groups specified")
lines = ["PURGE_BATCH", "NAME_BATCH activate_null",
         f"LOAD_SEQUENCE {sequences[groups[0][0]]} initialize_null",
         "MAP_TASKS group-null-init/ text use_manual_inputs 15 51 85 viable",
         "PURGE_BATCH", "NAME_BATCH selected_groups"]
for ident in sorted({g[0] for g in groups}):
    lines.append(f"LOAD_SEQUENCE {sequences[ident]} base_{ident}")
for number, (ident, sites) in enumerate(groups):
    mutant = list(sequences[ident])
    for site in sites:
        mutant[site - 1] = "A"
    name = f"group_{number}_id_{ident}_sites_" + "_".join(map(str, sites))
    lines.append(f"LOAD_SEQUENCE {''.join(mutant)} {name}")
fields = "name viable fitness gest_time " + " ".join(f"task.{t}" for t in task_ids)
for k, triple in enumerate(triples):
    lines.append("RECALCULATE 0 -1 0 " + " ".join(map(str, triple)))
    lines.append(f"DETAIL reuse-groups-I{k}.dat {fields}")
outfile.write_text("\n".join(lines) + "\n")

outfile.with_suffix(".columns.json").write_text(json.dumps(fields.split(),indent=2)+"\n")
