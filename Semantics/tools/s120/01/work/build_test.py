from pathlib import Path
import shlex,subprocess
flags=Path('build-patched/avida-core/CMakeFiles/avida.dir/flags.make').read_text()
incs=next(x.split('=',1)[1] for x in flags.splitlines() if x.startswith('CXX_INCLUDES'))
cmd=['g++','-std=gnu++11','-O0','-DNDEBUG']+shlex.split(incs)+['tests/check.cc','-Wl,--start-group','build-patched/lib/libavida-core.a','build-patched/lib/libapto.a','build-patched/lib/libtcmalloc-1.4.a','-Wl,--end-group','-lpthread','-o','tests/check']
p=subprocess.run(cmd,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
Path('test-build.log').write_text(p.stdout)
print('test harness compile exit',p.returncode)
if p.returncode: print(p.stdout[-2400:])
raise SystemExit(p.returncode)
