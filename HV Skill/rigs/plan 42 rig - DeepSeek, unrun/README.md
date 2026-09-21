# DeepSeek rig for test plan 42 with corpus 43

Order of work:
1. `python3 extract_cases.py "../43 Corpus ....md"` - already done; passages.json (sent) and keys.json (never sent).
2. `DEEPSEEK_API_KEY=... python3 run.py --limit 4` - a pilot of four runs; look at replies/ and the cost line.
3. `DEEPSEEK_API_KEY=... python3 run.py` - all 312 runs. Resumable. Then delete the key at DeepSeek.
4. `python3 hide.py` - labels stripped, replies shuffled and numbered into marking/to_mark.md.
5. Fill marking/marks.csv: NAMED / PARTLY / MISSED for the twenty; LEFT STANDING / FALSE ALARM for the five controls;
   Y or N for "reason given as a change someone could make". Never open marking/secret_mapping.json.
6. `python3 restore.py` - the table, case by setup, three marks a box, plus the reworded rows.

`python3 run.py --fake` runs the whole pipeline with a stub reply and no network.
Send nothing in this folder but the passages to DeepSeek. keys.json and the plans hold the answer key.
