#!/usr/bin/env python3
"""OpenAI Codex: wait for sequential authoring closures, then execute ready ledgers."""
from pathlib import Path
import json, os, subprocess, time

ROOT = Path(__file__).resolve().parents[1]
started = time.monotonic()
while time.monotonic() - started < 7200:
    rows = [json.loads(line) for line in (ROOT/'evidence/translation_order.jsonl').read_text().splitlines() if line.strip()]
    pending = []
    for row in rows:
        p = row['passage']
        kinds = ['rig1','consequences']
        if (ROOT/'rigs/rig 2 - causes'/('ledger_'+p+'.pl')).exists():
            kinds.append('rig2')
        if any(not (ROOT/'evidence'/k/(p+'_OpenAI_Codex.receipt.json')).exists() for k in kinds):
            pending.append(p)
    if pending:
        print('OpenAI Codex executing closed translations: '+', '.join(pending), flush=True)
        result = subprocess.run(['python3',str(ROOT/'authoring/run_ready_evidence_OpenAI_Codex.py')], env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'))
        if result.returncode:
            raise SystemExit(result.returncode)
    elif len(rows) == 18:
        print('OpenAI Codex: all 18 original translation closures have complete run receipts.',flush=True)
        break
    else:
        time.sleep(3)
else:
    raise SystemExit('OpenAI Codex: watch deadline reached; all completed evidence remains intact.')
