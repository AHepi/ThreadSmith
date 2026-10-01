from pathlib import Path
import shutil
source=Path('av_src/avida-core/support/config')
tests=Path('tests');tests.mkdir(exist_ok=True)
for name in ['avida.cfg','instset-heads.cfg','default-heads.org']:
 shutil.copyfile(source/name,tests/name)
(tests/'events.cfg').write_text('')
(tests/'environment.cfg').write_text('REACTION ANT anticipate process:value=1:type=add\n')
(tests/'environment-cap.cfg').write_text('REACTION ANT anticipate process:value=1:type=pow requisite:max_count=1\n')
for name,body in [('echo','IO\n'),('inc','inc\nIO\n')]:
 (tests/(name+'.org')).write_text('#inst_set heads_default\n#hw_type 0\n'+body)
base=(source/'default-heads.org').read_text()
(tests/'copy-echo.org').write_text(base.replace('h-alloc','IO\nIO\nIO\nh-alloc',1))
(tests/'copy-inc.org').write_text(base.replace('h-alloc','inc\nIO\ninc\nIO\ninc\nIO\nh-alloc',1))
events='''u begin Inject default-heads.org
u 0:100:end PrintAverageData
u 0:100:end PrintDominantData
u 0:100:end PrintCountData
u 0:100:end PrintTasksData
u 0:100:end PrintTimeData
u 0:100:end PrintResourceData
u 400 SavePopulation filename=population
u 400 Exit
'''
for name in ['run-stock','run-off']:
 target=Path(name);target.mkdir(exist_ok=True)
 for file in ['avida.cfg','instset-heads.cfg','default-heads.org','environment.cfg']:
  shutil.copyfile(source/file,target/file)
 (target/'events.cfg').write_text(events)
print('Test fixtures written')
