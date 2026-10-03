python3 $BASE/measurement/measure_orders.py \
  --avida $BASE/build/bin/avida \
  --piece $BASE/stage1/smoke-progress/piece-00001 \
  --snapshot $BASE/stage1/smoke-progress/piece-00001/data/population-99.spop \
  --manifest $BASE/stage1/smoke-progress/task_manifest.json \
  --schedule $BASE/stage1/smoke-progress/schedule.json \
  --out $BASE/measurement/smoke-orders-v2
