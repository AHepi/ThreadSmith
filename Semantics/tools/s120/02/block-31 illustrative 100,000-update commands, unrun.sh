python3 run.py --source "$SRC" --avida "$BIN" --out A-001 --mode progress --seed 1001 --pieces 100
python3 run.py --source "$SRC" --avida "$BIN" --out A-replay-001 --mode replay --seed 2001 --pieces 100 --schedule A-001/schedule.json
python3 run.py --source "$SRC" --avida "$BIN" --out A-fixed-001 --mode fixed --seed 3001 --pieces 100 --schedule A-001/schedule.json
python3 run.py --source "$SRC" --avida "$BIN" --out B-001 --mode archive --seed 4001 --pieces 100
python3 run.py --source "$SRC" --avida "$BIN" --out B-replay-001 --mode replay --seed 5001 --pieces 100 --schedule B-001/schedule.json
python3 run.py --source "$SRC" --avida "$BIN" --out B-fixed-001 --mode fixed --seed 6001 --pieces 100 --schedule B-001/schedule.json
python3 run.py --source "$SRC" --avida "$BIN" --out uniform-001 --mode all77 --seed 7001 --pieces 100
python3 measure_orders.py --avida "$BIN" --piece A-001/piece-00024 --snapshot A-001/piece-00024/data/population-999.spop --manifest A-001/task_manifest.json --schedule A-001/schedule.json --out measure-A-25000
python3 measure_orders.py --avida "$BIN" --piece A-001/piece-00049 --snapshot A-001/piece-00049/data/population-999.spop --manifest A-001/task_manifest.json --schedule A-001/schedule.json --baseline measure-A-25000/measurement.json --out measure-A-50000
