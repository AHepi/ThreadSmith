#!/usr/bin/env python3
"""OpenAI Codex: separately execute explicitly released correction-1 ledger pairs."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import hashlib, importlib.util, json

ROOT = Path(__file__).resolve().parents[1]
SOURCE = Path('/workspace/scratch/984d5d85cc67/work/L66_blind_corpus')
spec = importlib.util.spec_from_file_location('original_evidence_runner', ROOT/'authoring/run_ready_evidence_OpenAI_Codex.py')
runner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)

def process(row):
    for name, expected in row['files'].items():
        assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest() == expected, 'Correction changed before execution: '+name
    label = row['passage']+'_correction1'
    ledger = ROOT/row['correction']
    ledger = ledger.with_suffix('.pl')
    runner.run('rig1',label,ledger,SOURCE/'rigs/rig 1 - arguments/patched/run_check.py')
    runner.run('consequences',label,ledger,SOURCE/'tools/consequences.py')
    causal = ROOT/'rigs/rig 2 - causes'/('ledger_'+label+'.pl')
    if causal.exists():
        runner.run('rig2',label,causal,SOURCE/'rigs/rig 2 - causes/patched/check2.py')

if __name__ == '__main__':
    rows = json.loads((ROOT/'evidence/corrections_OpenAI_Codex.json').read_text())['corrections']
    assert sorted(r['passage'] for r in rows) == ['P01','P03','P07','P10','P14']
    with ThreadPoolExecutor(max_workers=3) as executor:
        list(executor.map(process,rows))
