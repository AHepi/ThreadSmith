#!/usr/bin/env python3
"""Repeat the authenticated native runtime smoke test. Not the whole of plan 45.

Only the SCASP executable location is relocated in memory. Source files and
checker rules remain unchanged. An exit code is never a semantic certificate.
"""
from __future__ import annotations
import argparse
import datetime
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[1]

def verify_sources() -> None:
    manifest=json.loads((ROOT/'evidence/authenticated_sources.json').read_text())
    for entry in manifest['files']:
        data=(ROOT/entry['path']).read_bytes()
        if hashlib.sha256(data).hexdigest()!=entry['sha256']:
            raise ValueError('Source changed: '+entry['path'])

def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--scasp',type=Path,default=Path('/home/claude/sCASP/scasp'))
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    verify_sources()
    stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    output=args.output or ROOT/'replays'/stamp
    output.mkdir(parents=True,exist_ok=False)
    record={'scope':'NATIVE_RUNTIME_SMOKE_ONLY','part_a_comparisons_completed':0,
            'part_b_forcing_runs_completed':0,'scasp':str(args.scasp),
            'semantic_pass':None,'source_modified':False}
    if not args.scasp.is_file() or not os.access(args.scasp,os.X_OK):
        record['status']='BLOCKED_MISSING_EXECUTABLE'
        (output/'result.json').write_text(json.dumps(record,indent=2)+'\n')
        print(json.dumps(record,indent=2))
        return 2
    # The source's hard-coded path is an environment location, not a rule.
    code='''import importlib.util,sys
sys.dont_write_bytecode=True
spec=importlib.util.spec_from_file_location("native_rig1",sys.argv[1])
m=importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
m.SCASP=sys.argv[2]
with open(sys.argv[4],"a",encoding="utf-8") as log:
    print(m.check(sys.argv[3],log))
'''
    command=[sys.executable,'-B','-c',code,
             str(ROOT/'sources/rig1_patched/run_check.py'),str(args.scasp.resolve()),
             str(ROOT/'sources/runtime_smoke/ledger_T05B.pl'),str(output/'raw_log.txt')]
    record['command']=command
    try:
        done=subprocess.run(command,capture_output=True,text=True,timeout=240)
        (output/'stdout.txt').write_text(done.stdout)
        (output/'stderr.txt').write_text(done.stderr)
        record['returncode']=done.returncode
        record['status']='DRIVER_RETURNED_REVIEW_RAW_OUTPUT' if done.returncode==0 else 'DRIVER_FAILED'
    except subprocess.TimeoutExpired as exc:
        record['status']='SMOKE_TIMED_OUT'
        record['error']=str(exc)
    verify_sources()
    (output/'result.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps(record,indent=2))
    return 0 if record['status']=='DRIVER_RETURNED_REVIEW_RAW_OUTPUT' else 2

if __name__=='__main__':
    try: raise SystemExit(main())
    except (OSError,ValueError,KeyError) as exc:
        print(str(exc),file=sys.stderr)
        raise SystemExit(2)
