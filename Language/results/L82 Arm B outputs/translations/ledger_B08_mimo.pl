% ledger_B08_mimo.pl - built by translate_via_api_2.py from the model's JSON (mimo). Standing and marks are in the JSON.
line(foreman).
kind(foreman, farm_foreman) :- line(foreman).
body(foreman, not_stated) :- line(foreman).
line(note).
kind(note, note) :- line(note).
body(note, not_stated) :- line(note).
line(rounds).
kind(rounds, rounds) :- line(rounds).
body(rounds, not_stated) :- line(rounds).
line(p1).
holds(keeps(foreman, note)) :- line(p1).
line(note_topic).
holds(about(note, rounds)) :- line(note_topic).
line(p2).
holds(writes(foreman, note)) :- line(p2).
line(shepherd).
kind(shepherd, shepherd) :- line(shepherd).
body(shepherd, not_stated) :- line(shepherd).
line(flock).
kind(flock, flock) :- line(flock).
body(flock, not_stated) :- line(flock).
line(top_field).
kind(top_field, field) :- line(top_field).
body(top_field, not_stated) :- line(top_field).
line(gate).
kind(gate, gate) :- line(gate).
body(gate, not_stated) :- line(gate).
line(gate_open).
holds(open(gate)) :- line(gate_open).
line(flock_top).
holds(in_top_field(flock)) :- line(flock_top).
line(since1).
claim_since(since1, in_top_field(flock), open(gate)) :- line(since1).
line(p3).
holds(adds(foreman, note)) :- line(p3).
line(lower_field).
kind(lower_field, field) :- line(lower_field).
body(lower_field, not_stated) :- line(lower_field).
line(grass).
kind(grass, grass) :- line(grass).
body(grass, not_stated) :- line(grass).
line(lower_empty).
holds(empty_of(lower_field, grass)) :- line(lower_empty).
line(note_end).
holds(ended_with(note, finish_of(rounds))) :- line(note_end).
line(rounds_done).
holds(finished(rounds)) :- line(rounds_done).
