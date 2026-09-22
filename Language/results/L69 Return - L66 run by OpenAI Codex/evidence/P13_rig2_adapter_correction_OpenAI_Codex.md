# P13 rig-2 adapter correction

Written by OpenAI Codex under L66. Seen: the original `check2.py` run logged `removed: [] | swap: None` for P13's what-if; it ignores rig-1's `make_not_so` field. Its printed claim to have made a change therefore did not establish an executed change.

Worked out: use the existing supported `swap` field to replace the positive clause `holds(decline_from_course(atoms)) :- line(e).` with `denied(decline_from_course(atoms)) :- line(e).` in the temporary query program. This implements the same negative source condition without changing the saved ledger, checker, response classes or movement claim. New pair: `rigs/rig 2 - causes/ledger_P13_correction1.*`. The original semantic translation and rig-1 ledger are unchanged. A separate corrected run is required; no original log is altered.
