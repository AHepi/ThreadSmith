from pathlib import Path
import re
stamp=re.compile(rb'^# (?:Mon|Tue|Wed|Thu|Fri|Sat|Sun) (?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) [ \d]\d \d\d:\d\d:\d\d \d{4}\r?\n',re.M)
a=Path('run-stock/data'); b=Path('run-off/data')
expected={'population-400.spop','average.dat','count.dat','dominant.dat','resource.dat','tasks.dat','time.dat'}
assert {p.name for p in a.iterdir()} == {p.name for p in b.iterdir()} == expected
for p in sorted(a.iterdir()):
 if not p.is_file():continue
 s=p.read_bytes();t=(b/p.name).read_bytes()
 ns=stamp.sub(b'# TIMESTAMP\n',s);nt=stamp.sub(b'# TIMESTAMP\n',t)
 assert ns==nt,p.name
 print(p.name+': raw_equal='+str(s==t)+' timestamp_normalized_equal=True')
print('7/7 files match after replacing only timestamp header lines')
