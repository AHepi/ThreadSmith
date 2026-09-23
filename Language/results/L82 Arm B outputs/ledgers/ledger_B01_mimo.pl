% ledger_B01_mimo.pl - built by translate_via_api_2.py from the model's JSON (mimo). Standing and marks are in the JSON.
line(foreman).
kind(foreman, farm_foreman) :- line(foreman).
body(foreman, not_stated) :- line(foreman).
line(note).
kind(note, note) :- line(note).
body(note, not_stated) :- line(note).
line(rounds).
kind(rounds, rounds) :- line(rounds).
body(rounds, not_stated) :- line(rounds).
line(kept_notes).
holds(kept(foreman, note)) :- line(kept_notes).
line(on_rounds).
holds(kept_on(note, rounds)) :- line(on_rounds).
holds(rounds_of(foreman, rounds)) :- line(on_rounds).
line(wrote_note).
holds(wrote(foreman, note)) :- line(wrote_note).
line(shepherd).
kind(shepherd, shepherd) :- line(shepherd).
body(shepherd, not_stated) :- line(shepherd).
line(flock).
kind(flock, flock) :- line(flock).
body(flock, not_stated) :- line(flock).
line(gate).
kind(gate, gate) :- line(gate).
body(gate, not_stated) :- line(gate).
line(top_field).
kind(top_field, field) :- line(top_field).
body(top_field, not_stated) :- line(top_field).
line(flock_top).
holds(in(flock, top_field)) :- line(flock_top).
line(gate_stood_open).
holds(gate_open(gate)) :- line(gate_stood_open).
line(gate_rule).
holds(driven_through(flock, gate)) :- line(gate_rule), holds(left_open_by(shepherd, gate)).
line(since1).
claim_since(since1, in(flock, top_field), gate_open(gate)) :- line(since1).
line(added_note).
holds(added_to(foreman, note)) :- line(added_note).
line(lower_field).
kind(lower_field, field) :- line(lower_field).
body(lower_field, not_stated) :- line(lower_field).
line(grass).
kind(grass, grass) :- line(grass).
body(grass, not_stated) :- line(grass).
line(field_empty).
holds(empty_of_grass(lower_field)) :- line(field_empty).
line(note_end).
holds(ended_with(note, rounds_finish_time)) :- line(note_end).
line(rounds_done).
holds(finished(rounds)) :- line(rounds_done).
