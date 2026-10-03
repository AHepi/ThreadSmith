# Plain note (log S120, written by Claude, Opus 5.5, 1 October 2026).
# What this does: compares the data files of two 400-update Avida runs, one by the stock binary
# and one by the binary patched with reply 01's anticipation code switched off, file by file,
# after replacing only the date line Avida writes at the top of each file (the same rule as the
# reply's own compare.py). Used for two settings the reply did not try: SPECULATIVE 1 (the stock
# default) and the 77-task environment. Usage: python3 this.py STOCK_DIR OFF_DIR
import re
import sys
from pathlib import Path

stamp = re.compile(rb'^# (?:Mon|Tue|Wed|Thu|Fri|Sat|Sun) (?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) '
                   rb'[ \d]\d \d\d:\d\d:\d\d \d{4}\r?\n', re.M)
a, b = Path(sys.argv[1]) / "data", Path(sys.argv[2]) / "data"
names_a = sorted(p.name for p in a.iterdir() if p.is_file())
names_b = sorted(p.name for p in b.iterdir() if p.is_file())
print("same file names:", names_a == names_b, len(names_a), "files")
same = 0
for name in names_a:
    x, y = (a / name).read_bytes(), (b / name).read_bytes()
    ok = stamp.sub(b"# DATE\n", x) == stamp.sub(b"# DATE\n", y)
    same += ok
    print("%s: raw_equal=%s equal_after_date_line=%s" % (name, x == y, ok))
print("%d of %d files equal after the date line" % (same, len(names_a)))
