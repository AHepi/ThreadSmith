# NOTE (added by Claude, log S115): this file is 'Recover and map a selected ancestry path', copied unchanged from the appendix of
# GPT 6 Astra's reply 01 ('tests/S115 Returns from GPT 6 Astra/01 Return - measuring what is learned,
# with stock Avida only.md'). Only these note lines were added. It has not been run on S113's data;
# see 'results/S115 Checking the Astra returns/01 Check of reply 01 - measuring what is learned.md'.
python ancestry-helper.py --segment continuous-run1 --target 123 \
  --output selected-lineage.spop \
  "$ORIGINAL_RUN/data/history-10000.spop" "$ORIGINAL_RUN/data/history-20000.spop"
MAP_OUT="$MEASUREMENT_DIR/lineage-maps"
python map_lineage.py --suite "$PROBE_OUT" --lineage selected-lineage.spop \
  --target 123 --out "$MAP_OUT" --run
python - "$MAP_OUT" <<'PYRUN'
import pathlib, subprocess, sys
p=pathlib.Path(sys.argv[1])
subprocess.run([sys.executable,'summarize_maps.py',str(p/'maps.tsv'),
               '--out',str(p/'summary'),'--tasks',
               *(p/'task_indices.txt').read_text().split()],check=True)
PYRUN
