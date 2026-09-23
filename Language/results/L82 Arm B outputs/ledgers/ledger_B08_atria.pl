% ledger_B08_atria.pl - built by translate_via_api_2.py from the model's JSON (atria). Standing and marks are in the JSON.
line(foreman).
kind(foreman, person) :- line(foreman).
body(foreman, heavy_and_standing) :- line(foreman).
line(rounds).
kind(rounds, rounds) :- line(rounds).
body(rounds, not_stated) :- line(rounds).
line(notes).
kind(notes, notes) :- line(notes).
body(notes, not_stated) :- line(notes).
line(s1fact).
holds(kept_notes_on(foreman, rounds)) :- line(s1fact).
line(flock).
kind(flock, flock) :- line(flock).
body(flock, not_stated) :- line(flock).
line(top_field).
kind(top_field, field) :- line(top_field).
body(top_field, not_stated) :- line(top_field).
line(gate).
kind(gate, gate) :- line(gate).
body(gate, not_stated) :- line(gate).
line(flock_in).
holds(in_top_field(flock)) :- line(flock_in).
line(gate_open).
holds(stood_open(gate)) :- line(gate_open).
line(since1).
claim_since(since1, in_top_field(flock), stood_open(gate)) :- line(since1).
line(lower_field).
kind(lower_field, field) :- line(lower_field).
body(lower_field, not_stated) :- line(lower_field).
line(grass).
kind(grass, grass) :- line(grass).
body(grass, not_stated) :- line(grass).
line(lower_empty).
holds(empty_of_grass(lower_field)) :- line(lower_empty).
line(s4fact).
holds(finished(rounds)) :- line(s4fact).
