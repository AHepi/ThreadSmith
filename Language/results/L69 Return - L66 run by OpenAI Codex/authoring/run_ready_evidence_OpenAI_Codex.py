#!/usr/bin/env python3
"""OpenAI Codex: execute only completed translations; preserve exact raw evidence."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib, json, os, subprocess

ROOT = Path(__file__).resolve().parents[1]
SOURCE = Path('/workspace/scratch/984d5d85cc67/work/L66_blind_corpus')
ENV = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def run(kind, passage, ledger, driver):
    dest = ROOT/'evidence'/kind
    dest.mkdir(parents=True, exist_ok=True)
    prefix = dest/(passage+'_OpenAI_Codex')
    receipt = Path(str(prefix)+'.receipt.json')
    if receipt.exists():
        previous = json.loads(receipt.read_text())
        assert previous['ledger_sha256'] == digest(ledger), f'Ledger changed after run: {ledger}'
        return previous
    stdout = Path(str(prefix)+'.report.txt')
    stderr = Path(str(prefix)+'.stderr.txt')
    raw = Path(str(prefix)+'.raw.txt')
    for path in (stdout, stderr, raw):
        assert not path.exists(), f'Unreceipted evidence already exists: {path}'
    command = ['python3', str(driver), str(ledger), str(raw)]
    started = datetime.now(timezone.utc).isoformat()
    with stdout.open('wb') as out, stderr.open('wb') as err:
        result = subprocess.run(command, cwd=ledger.parent, stdout=out, stderr=err, env=ENV)
    row = {
        'author': 'OpenAI Codex',
        'raw_evidence_policy': 'Exact subprocess stdout/stderr and driver query log; authorship recorded here without modifying raw evidence.',
        'passage': passage, 'kind': kind, 'command': command,
        'cwd': str(ledger.parent), 'started_at': started,
        'finished_at': datetime.now(timezone.utc).isoformat(),
        'exit_code': result.returncode,
        'ledger_sha256': digest(ledger),
        'ledger_json_sha256': digest(ledger.with_suffix('.json')),
        'driver_sha256': digest(driver),
        'files': [{'path': str(p.relative_to(ROOT)), 'bytes': p.stat().st_size,
                   'sha256': digest(p)} for p in (stdout, stderr, raw) if p.exists()]
    }
    receipt.write_text(json.dumps(row, indent=2)+'\n')
    print(json.dumps({'passage':passage,'kind':kind,'exit_code':result.returncode,'receipt':str(receipt.relative_to(ROOT))}), flush=True)
    return row

def process(row):
    passage = row['passage']
    translation = ROOT/'translations'/(passage+'_OpenAI_Codex_translation.md')
    assert digest(translation)==row['translation_sha256'], f'Translation changed after close: {passage}'
    ledger = ROOT/'rigs/rig 1 - arguments'/('ledger_'+passage+'.pl')
    run('rig1',passage,ledger,SOURCE/'rigs/rig 1 - arguments/patched/run_check.py')
    run('consequences',passage,ledger,SOURCE/'tools/consequences.py')
    causal = ROOT/'rigs/rig 2 - causes'/('ledger_'+passage+'.pl')
    if causal.exists():
        run('rig2',passage,causal,SOURCE/'rigs/rig 2 - causes/patched/check2.py')

if __name__ == '__main__':
    order = [json.loads(line) for line in (ROOT/'evidence/translation_order.jsonl').read_text().splitlines() if line.strip()]
    with ThreadPoolExecutor(max_workers=3) as executor:
        list(executor.map(process,order))
