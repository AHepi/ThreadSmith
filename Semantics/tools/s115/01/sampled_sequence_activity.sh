# NOTE (added by Claude, log S115): this file is 'Sampled sequence activity', copied unchanged from the appendix of
# GPT 6 Astra's reply 01 ('tests/S115 Returns from GPT 6 Astra/01 Return - measuring what is learned,
# with stock Avida only.md'). Only these note lines were added. It has not been run on S113's data;
# see 'results/S115 Checking the Astra returns/01 Check of reply 01 - measuring what is learned.md'.
python - "$PROBE_OUT" <<'PYRUN'
import csv,pathlib,sys
p=pathlib.Path(sys.argv[1])
with (p/'snapshots.tsv').open() as f:
    rows=list(csv.DictReader(f,delimiter='\t'))
with (p/'snapshots.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,['update','path']);w.writeheader()
    w.writerows({k:r[k] for k in ['update','path']} for r in rows)
PYRUN
python dynamics_metrics.py "$PROBE_OUT/snapshots.csv" "$PROBE_OUT/dynamics.csv" \
  --band-low 1 --band-high 2
