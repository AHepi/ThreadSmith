# NOTE (S115, added by Claude): Astra's six hand-made test cases for the patched build.
# Copied unchanged from GPT 6 Astra's reply 06 (tests/S115 Returns from GPT 6 Astra/06 Return - independent review of the first reply.md); only these note lines were added.
from pathlib import Path
import shutil, subprocess, json, sys
# Usage: python smoke.py /path/to/avida-mini /path/to/run-root /path/to/smoke-root
binary, runs, tests = [Path(x).resolve() for x in sys.argv[1:]]
ancestor=(runs/'B2/default-heads.org').read_text()
header='#inst_set heads_default\n#hw_type 0\n'
body='\n'.join(x for x in ancestor.splitlines() if not x.startswith('#'))+'\n'
def program(prefix): return header+'\n'.join(prefix)+'\n'+body
fixtures={'echo':program(['IO']*4), 'zero':program(['IO']*3+['IO','nop-C']),
          'graph':program(['IO']*3+['inc','nop-C']*130+['IO','nop-C']),
          'path':program(['IO']*3+['inc','nop-C','IO','nop-C']+['IO']*4),
          'one':program(['IO']*3+['inc','nop-C','IO','nop-C']),
          'choose0':program(['IO']*6+['IO','nop-C']),
          'choose1':program(['IO']*6+['inc','nop-C','IO','nop-C'])}
scenarios={
 'B1':('B1',['u begin InjectRange zero.org 0 16','u 1 MiniB1','u 1 Exit']),
 'B2':('B2',['u begin InjectRange echo.org 0 24','u begin InjectRange zero.org 24 32','u 0 MiniB2','u 0 Exit']),
 'B3':('B3',['u begin InjectRange graph.org 0 16','u begin InjectRange path.org 16 24','u begin InjectRange one.org 24 32','u 0 MiniB3','u 0 Exit']),
 'C0':('C',['u begin InjectRange echo.org 0 17','u begin Inject zero.org 17','u begin InjectRange choose0.org 32 48','u 0 MiniC','u 0 Exit']),
 'C1':('C',['u begin InjectRange echo.org 0 17','u begin Inject zero.org 17','u begin InjectRange choose1.org 32 48','u 0 MiniC','u 0 Exit']),
 'emptyB2':('B2',['u begin InjectRange default-heads.org 0 32','u 0 MiniB2','u 0 Exit'])}
results={}
for name,(mode,events) in scenarios.items():
 d=tests/name; shutil.copytree(runs/mode,d,dirs_exist_ok=True)
 (d/'events.cfg').write_text('\n'.join(events)+'\n')
 for f,s in fixtures.items(): (d/(f+'.org')).write_text(s)
 p=subprocess.run([str(binary),'-c','avida.cfg'],cwd=d,capture_output=True,text=True)
 (d/'stdout.log').write_text(p.stdout); (d/'stderr.log').write_text(p.stderr)
 log=(d/('mini-b1.log' if name=='B1' else 'mini.log')).read_text() if p.returncode==0 else ''
 brief=[x for x in log.splitlines() if x.startswith(('INVALID','EMPTY','UNREACHABLE','GRAPH','MOVE','Q ','WINS','PAIR'))]
 if name=='B1': brief=log.splitlines()
 results[name]={'exit':p.returncode,'records':brief}
(tests/'results.json').write_text(json.dumps(results,indent=2))
print(json.dumps(results,indent=2))
