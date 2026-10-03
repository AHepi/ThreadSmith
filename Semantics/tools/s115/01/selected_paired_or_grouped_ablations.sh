# NOTE (added by Claude, log S115): this file is 'Selected paired or grouped ablations', copied unchanged from the appendix of
# GPT 6 Astra's reply 01 ('tests/S115 Returns from GPT 6 Astra/01 Return - measuring what is learned,
# with stock Avida only.md'). Only these note lines were added. It has not been run on S113's data;
# see 'results/S115 Checking the Astra returns/01 Check of reply 01 - measuring what is learned.md'.
python group_ablation.py selected-lineage.spop groups.csv group-analyze.cfg \
  6 22 --inputs "$PROBE_OUT/inputs.tsv"
mkdir -p "$MEASUREMENT_DIR/group-results"
cd "$ORIGINAL_RUN"
"$AVIDA_BIN" -c avida.cfg -a \
  -set ANALYZE_FILE "$MEASUREMENT_DIR/group-analyze.cfg" \
  -set ENVIRONMENT_FILE "$PROBE_OUT/core/environment.cfg" \
  -set EVENT_FILE "$PROBE_OUT/events.cfg" \
  -set DATA_DIR "$MEASUREMENT_DIR/group-results" \
  -set RANDOM_SEED 20260930 -set TASK_REFRACTORY_PERIOD 0 -set TEST_CPU_TIME_MOD 20
cd "$MEASUREMENT_DIR"
