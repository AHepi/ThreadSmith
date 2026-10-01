python3 - <<'EXTRACT'
from pathlib import Path
import re
source=Path('Brief02_History_Selector_Execution_Report.md').read_text()
out=Path('selector-files')
out.mkdir(exist_ok=False)
for name,content in re.findall(r'^### File: ([A-Za-z0-9_.-]+)\n\n```[^\n]*\n(.*?)^```',source,re.M|re.S):
    (out/name).write_text(content)
print('Files extracted to',out)
EXTRACT
