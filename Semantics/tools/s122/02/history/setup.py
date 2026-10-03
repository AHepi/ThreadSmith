from pathlib import Path
import shutil
p=Path('history/tests');p.mkdir(exist_ok=True)
for n in ['avida.cfg','instset-heads.cfg','default-heads.org']: shutil.copyfile(Path('tests')/n,p/n)
(p/'events.cfg').write_text('')
(p/'environment-cap.cfg').write_text('REACTION O hist_order process:value=1:type=pow requisite:max_count=1\nREACTION I hist_interval process:value=1:type=pow requisite:max_count=1\nREACTION S hist_sequence process:value=1:type=pow requisite:max_count=1\n')
(p/'environment.cfg').write_text('REACTION O hist_order process:value=1:type=add\nREACTION I hist_interval process:value=1:type=add\nREACTION S hist_sequence process:value=1:type=add\n')
programs={'order':'IO nop-A nand IO IO nop-A','interval':'IO IO nop-A IO IO IO nop-A','sequence':'IO nop-A nand IO IO IO nop-A','echo':'IO','always':'nand inc inc IO'}
for n,body in programs.items(): (p/(n+'.org')).write_text('#inst_set heads_default\n#hw_type 0\n'+'\n'.join(body.split())+'\n')
print('History fixtures written; W=2; stateful expected counts=7,6,6 at time_mod=10')
