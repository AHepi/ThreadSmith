# NOTE (added by Claude, log S115): this file is 'dynamics_metrics.py', copied unchanged from the appendix of
# GPT 6 Astra's reply 01 ('tests/S115 Returns from GPT 6 Astra/01 Return - measuring what is learned,
# with stock Avida only.md'). Only these note lines were added. It has not been run on S113's data;
# see 'results/S115 Checking the Astra returns/01 Check of reply 01 - measuring what is learned.md'.
#!/usr/bin/env python3
"""Raw sampled sequence dynamics from stock Avida .spop files.

Usage: python3 dynamics_metrics.py snapshots.csv dynamics.csv --band-low 2 --band-high 4
snapshots.csv columns: update,path (paths relative to that CSV).
These are raw sampled statistics, not normalized evolutionary activity or MODES.
For a sequence g, a_g is its number of observed snapshots, including the current
one. Optional band activity is sum(a_g for current g with low <= a_g <= high)
divided by the number of current sequences. Its units are observed snapshots.
"""
import argparse
import csv
import math
from collections import Counter
from pathlib import Path


def living_counts(path):
    counts = Counter()
    columns = None
    with path.open() as stream:
        for line_no, line in enumerate(stream, 1):
            line = line.strip()
            if not line:
                continue
            if line.startswith("#format "):
                columns = line.split()[1:]
                continue
            if line.startswith("#"):
                continue
            if columns is None:
                raise ValueError(f"{path}:{line_no}: missing #format header")
            values = line.split()
            # Historical rows omit per-cell trailing fields in stock saves.
            if len(values) > len(columns):
                raise ValueError(f"{path}:{line_no}: too many fields")
            row = dict(zip(columns, values))
            abundance_name = "num_units" if "num_units" in row else "num_cpus"
            if abundance_name not in row:
                raise ValueError(f"{path}:{line_no}: missing abundance")
            abundance = int(row[abundance_name])
            if abundance < 0:
                raise ValueError(f"{path}:{line_no}: negative abundance")
            if abundance:
                key = (row["hw_type"], row["inst_set"], row["sequence"])
                counts[key] += abundance
    return counts


def main(manifest_name, output_name, band_low=None, band_high=None):
    if (band_low is None) != (band_high is None):
        raise ValueError("Supply both --band-low and --band-high, or neither")
    if band_low is not None and not (1 <= band_low <= band_high):
        raise ValueError("Activity band must satisfy 1 <= low <= high")
    manifest = Path(manifest_name)
    with manifest.open(newline="") as stream:
        snapshots = [(int(row["update"]), manifest.parent / row["path"])
                     for row in csv.DictReader(stream)]
    if not snapshots:
        raise ValueError("The snapshot manifest is empty")
    if any(b[0] <= a[0] for a, b in zip(snapshots, snapshots[1:])):
        raise ValueError("Global update values must be strictly increasing")
    seen = set()
    previous = None
    observations = Counter()
    columns = ["update", "program_count", "distinct_sequences", "raw_additions",
               "raw_losses", "raw_first_observations", "raw_sequence_entropy_bits",
               "mean_observed_presence_snapshots", "band_low_snapshots",
               "band_high_snapshots", "raw_band_activity_snapshots"]
    with Path(output_name).open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=columns)
        writer.writeheader()
        for update, path in snapshots:
            counts = living_counts(path)
            current = set(counts)
            total = sum(counts.values())
            observations.update(current)
            entropy = -sum((n / total) * math.log2(n / total) for n in counts.values()) if total else 0.0
            writer.writerow({
                "update": update,
                "program_count": total,
                "distinct_sequences": len(current),
                "raw_additions": len(current - previous) if previous is not None else "",
                "raw_losses": len(previous - current) if previous is not None else "",
                "raw_first_observations": len(current - seen) if previous is not None else "",
                "raw_sequence_entropy_bits": entropy,
                "mean_observed_presence_snapshots": sum(observations[g] for g in current) / len(current) if current else "",
                "band_low_snapshots": band_low if band_low is not None else "",
                "band_high_snapshots": band_high if band_high is not None else "",
                "raw_band_activity_snapshots": sum(observations[g] for g in current
                    if band_low <= observations[g] <= band_high) / len(current)
                    if current and band_low is not None else "",
            })
            seen.update(current)
            previous = current


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest")
    parser.add_argument("output")
    parser.add_argument("--band-low", type=int)
    parser.add_argument("--band-high", type=int)
    args = parser.parse_args()
    main(args.manifest, args.output, args.band_low, args.band_high)
