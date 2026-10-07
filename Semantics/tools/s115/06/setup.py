# NOTE (S115, added by Claude): Astra's configuration generator for the four miniatures (seed 11501; change RANDOM_SEED for 11502, 11503).
# Copied unchanged from GPT 6 Astra's reply 06 (tests/S115 Returns from GPT 6 Astra/06 Return - independent review of the first reply.md); only these note lines were added.
#!/usr/bin/env python3
# Usage: python setup.py /path/to/avida-checkout /path/to/run-root
from pathlib import Path
import re, shutil, sys
source, destination = map(Path, sys.argv[1:])
config = source / 'avida-core/support/config'
base = (config / 'avida.cfg').read_text()
common = dict(RANDOM_SEED=11501, WORLD_X=16, WORLD_Y=2, WORLD_GEOMETRY=2,
              NUM_DEMES=2, BIRTH_METHOD=6, PREFER_EMPTY=1, SLICING_METHOD=1,
              BASE_MERIT_METHOD=0, BASE_CONST_MERIT=100, DEATH_METHOD=0,
              SPECULATIVE=0, COPY_MUT_PROB=0.0075, DIVIDE_INS_PROB=0.05,
              DIVIDE_DEL_PROB=0.05, MIGRATION_RATE=0, DEMES_MIGRATION_RATE=0,
              EVENT_FILE='events.cfg', ENVIRONMENT_FILE='environment.cfg')
for mode, demes in [('B1', 1), ('B2', 2), ('B3', 2), ('C', 3)]:
    run = destination / mode
    run.mkdir(parents=True, exist_ok=True)
    values = dict(common, NUM_DEMES=demes, WORLD_Y=demes)
    if mode == 'B1':
        values.update(BASE_MERIT_METHOD=4, DEATH_METHOD=2, BIRTH_METHOD=0)
    text = base
    for name, value in values.items():
        text, count = re.subn(r'^' + name + r'\s+.*$', f'{name} {value}', text, flags=re.M)
        if count == 0: text += f'\n{name} {value}\n'
        assert count <= 1, name
    (run / 'avida.cfg').write_text(text)
    for name in ['default-heads.org', 'instset-heads.cfg']:
        shutil.copyfile(config / name, run / name)
    environment = ('REACTION TARGET match_number:target=0,threshold=0,halflife=1 '
                   'process:value=1:type=pow:max=1 requisite:max_count=1\n') if mode == 'B1' else (
                   'REACTION OBS echo process:value=0:type=pow:max=1 requisite:max_count=1\n')
    (run / 'environment.cfg').write_text(environment)
    events = [f'u begin InjectRange default-heads.org 0 {16*demes}']
    events += ['u 100:100:5000 MiniB1'] if mode == 'B1' else [f'u 0:1:5000 Mini{mode}']
    events += ['u 0:100:5000 PrintAverageData', 'u 0:100:5000 PrintCountData',
               'u 0:100:5000 PrintTimeData',
               'u 0:100:5000 SavePopulation filename=detail:save_historic=0', 'u 5000 Exit']
    (run / 'events.cfg').write_text('\n'.join(events) + '\n')
