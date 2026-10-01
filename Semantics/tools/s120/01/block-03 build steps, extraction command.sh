python3 - <<'PY'
from pathlib import Path
import re
report=Path('Avida_Anticipation_Report.md').read_text()
for name,body in re.findall(r'<!-- artifact: ([^\n]+) -->\n```[^\n]*\n(.*?)\n```',report,re.S):
    path=Path(name)
    assert not path.is_absolute() and '..' not in path.parts
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(body+'\n')
PY
