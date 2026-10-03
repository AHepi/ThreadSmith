# NOTE (added by Claude, log S115): this file is 'Run the probe battery and summaries', copied unchanged from the appendix of
# GPT 6 Astra's reply 01 ('tests/S115 Returns from GPT 6 Astra/01 Return - measuring what is learned,
# with stock Avida only.md'). Only these note lines were added. It has not been run on S113's data;
# see 'results/S115 Checking the Astra returns/01 Check of reply 01 - measuring what is learned.md'.
AVIDA_BIN=/absolute/path/to/avida
AVIDA_SOURCE=/absolute/path/to/avida-source
ORIGINAL_RUN=/absolute/path/to/original-run
MEASUREMENT_DIR="$PWD"
PROBE_OUT="$MEASUREMENT_DIR/probes"
python probe_task_audit.py --source "$AVIDA_SOURCE" --run-dir "$ORIGINAL_RUN" \
  --snapshot u10000 10000 "$ORIGINAL_RUN/data/history-10000.spop" \
  --snapshot u20000 20000 "$ORIGINAL_RUN/data/history-20000.spop" \
  --out "$PROBE_OUT" --avida "$AVIDA_BIN" --profiles safe --run
python summarize_probes.py "$PROBE_OUT"
# After checking and completing the history template:
# python summarize_probes.py "$PROBE_OUT" --rewards complete-reward-history.tsv
