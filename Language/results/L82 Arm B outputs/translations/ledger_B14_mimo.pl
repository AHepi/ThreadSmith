% ledger_B14_mimo.pl - built by translate_via_api_2.py from the model's JSON (mimo). Standing and marks are in the JSON.
line(nurse).
kind(nurse, nurse) :- line(nurse).
line(notes).
kind(handover_notes, notes) :- line(notes).
body(handover_notes, not_stated) :- line(notes).
line(nsis).
kind(night_sister, sister) :- line(nsis).
line(read1).
holds(reads(nurse, handover_notes)) :- line(read1).
line(leave1).
holds(left_behind(night_sister, handover_notes)) :- line(leave1).
line(pat).
kind(patient, patient) :- line(pat).
line(desk).
kind(desk, desk) :- line(desk).
body(desk, not_stated) :- line(desk).
line(plan1).
claim_plan(plan1, move(patient, toward_desk), easier_to_monitor(breathing(patient))) :- line(plan1).
changes(move(patient, toward_desk), distance_from(patient, desk)) :- line(plan1).
line(temp1).
holds(temperature_was_normal_at_midnight(patient)) :- line(temp1).
line(lastline).
holds(has_last_line(handover_notes)) :- line(lastline).
