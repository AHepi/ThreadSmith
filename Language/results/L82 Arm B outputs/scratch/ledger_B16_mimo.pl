% ledger_B16_mimo.pl - built by translate_via_api_2.py from the model's JSON (mimo). Standing and marks are in the JSON.
line(foreman).
kind(foreman, person) :- line(foreman).
body(foreman, not_stated) :- line(foreman).
line(notes).
kind(notes, record) :- line(notes).
body(notes, not_stated) :- line(notes).
line(rounds).
kind(evening_rounds, round) :- line(rounds).
body(evening_rounds, not_stated) :- line(rounds).
line(kept).
holds(kept(foreman, notes, evening_rounds)) :- line(kept).
line(shepherd).
kind(shepherd, person) :- line(shepherd).
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
line(in_top).
holds(in_field(flock, top_field)) :- line(in_top).
line(gate_open).
holds(stood_open(gate)) :- line(gate_open).
line(since1).
claim_since(since1, in_field(flock, top_field), stood_open(gate)) :- line(since1).
line(grass).
kind(grass, grass) :- line(grass).
body(grass, not_stated) :- line(grass).
line(lower_field).
kind(lower_field, field) :- line(lower_field).
body(lower_field, not_stated) :- line(lower_field).
line(no_grass).
denied(remained_in(grass, lower_field)) :- line(no_grass).
line(note).
kind(note, record) :- line(note).
body(note, not_stated) :- line(note).
line(notelink).
holds(one_of(note, notes)) :- line(notelink).
line(ended).
holds(ended_with(note, finish_time(evening_rounds))) :- line(ended).
line(rounds_done).
holds(finished(evening_rounds)) :- line(rounds_done).
