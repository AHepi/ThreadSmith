from pathlib import Path
import shlex,subprocess
s=Path('build-patched/avida-core/CMakeFiles/avida.dir/flags.make').read_text()
a=next(x.split('=',1)[1] for x in s.splitlines() if x.startswith('CXX_INCLUDES'))
cmd=['g++','-std=gnu++11','-O0','-DNDEBUG']+shlex.split(a)+['history/check.cc','-Wl,--start-group','build-patched/lib/libavida-core.a','build-patched/lib/libapto.a','build-patched/lib/libtcmalloc-1.4.a','-Wl,--end-group','-lpthread','-o','history/tests/check']
p=subprocess.run(cmd,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
Path('history/build.log').write_text(p.stdout);print('History harness compile exit',p.returncode)
if p.returncode:print(p.stdout[-3000:])
raise SystemExit(p.returncode)
