% ledger_B04_atria.pl - built by translate_via_api_2.py from the model's JSON (atria). Standing and marks are in the JSON.
line(a1).
kind(nurse, nurse) :- line(a1).
body(nurse, not_stated) :- line(a1).
line(a2).
kind(notes, handover_notes) :- line(a2).
body(notes, not_stated) :- line(a2).
line(a3).
kind(sister, night_nurse) :- line(a3).
body(sister, not_stated) :- line(a3).
line(a4).
holds(reads(nurse, notes)) :- line(a4).
line(a5).
holds(left_by(notes, sister)) :- line(a5).
line(t1).
kind(sister, night_nurse) :- line(t1).
body(sister, not_stated) :- line(t1).
line(t2).
kind(patient, patient) :- line(t2).
body(patient, not_stated) :- line(t2).
line(t3).
kind(bed, bed) :- line(t3).
body(bed, not_stated) :- line(t3).
line(t4).
kind(desk, desk) :- line(t4).
body(desk, not_stated) :- line(t4).
line(t5).
kind(night_staff, staff) :- line(t5).
body(night_staff, not_stated) :- line(t5).
line(t6).
kind(ward, ward) :- line(t6).
body(ward, not_stated) :- line(t6).
line(t7).
claim_plan(t7, move(patient, toward(desk)), easy_to_monitor(breathing(patient))) :- line(t7).
line(t8).
depends(easy_to_monitor(breathing(patient)), near(bed, desk)) :- line(t8).
line(t9).
holds(in_bed(patient, bed)) :- line(t9).
line(t10).
changes(move(patient, toward(desk)), near(bed, desk)) :- line(t10).
line(t11).
holds(lets(near(bed, desk), watch_chest_rise(night_staff, patient))) :- line(t11).
denied(walk_ward(night_staff)) :- line(t11).
line(t12).
claim_since(t12, easy_to_monitor(breathing(patient)), lets(near(bed, desk), watch_chest_rise(night_staff, patient))) :- line(t12).
line(t13).
holds(normal_temperature(patient)) :- line(t13).
