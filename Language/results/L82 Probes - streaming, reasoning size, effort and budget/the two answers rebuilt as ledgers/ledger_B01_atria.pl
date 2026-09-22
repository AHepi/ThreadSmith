% ledger_B01_atria.pl - built by translate_via_api_2.py from the model's JSON (atria). Standing and marks are in the JSON.
line(a_foreman).
kind(foreman, person) :- line(a_foreman).
body(foreman, not_stated) :- line(a_foreman).
line(a_notes).
kind(notes, notes) :- line(a_notes).
body(notes, not_stated) :- line(a_notes).
line(a_rounds).
kind(rounds, rounds) :- line(a_rounds).
body(rounds, not_stated) :- line(a_rounds).
line(a_note).
kind(note, note) :- line(a_note).
body(note, not_stated) :- line(a_note).
line(a_kept).
holds(kept(foreman, notes)) :- line(a_kept).
line(a_onrounds).
holds(on_rounds(foreman, rounds)) :- line(a_onrounds).
line(a_wrote).
holds(wrote(foreman, note)) :- line(a_wrote).
line(n_gate).
kind(gate, gate) :- line(n_gate).
body(gate, not_stated) :- line(n_gate).
line(n_flock).
kind(flock, flock) :- line(n_flock).
body(flock, not_stated) :- line(n_flock).
line(n_shepherd).
kind(shepherd, person) :- line(n_shepherd).
body(shepherd, not_stated) :- line(n_shepherd).
line(n_top).
kind(top_field, field) :- line(n_top).
body(top_field, not_stated) :- line(n_top).
line(n_low).
kind(lower_field, field) :- line(n_low).
body(lower_field, not_stated) :- line(n_low).
line(n_rounds).
kind(rounds, rounds) :- line(n_rounds).
body(rounds, not_stated) :- line(n_rounds).
line(n_open).
holds(stood_open(gate)) :- line(n_open).
line(n_concl).
holds(in_field(flock, top_field)) :- line(n_concl).
line(n_grass).
denied(has_grass(lower_field)) :- line(n_grass).
line(n_done).
holds(finished(rounds)) :- line(n_done).
line(n_always).
holds(driven_through(flock, gate)) :- line(n_always), holds(stood_open(gate)).
line(n_link).
holds(in_field(flock, top_field)) :- line(n_link), holds(driven_through(flock, gate)).
line(n_since).
claim_since(n_since, in_field(flock, top_field), stood_open(gate)) :- line(n_since).
