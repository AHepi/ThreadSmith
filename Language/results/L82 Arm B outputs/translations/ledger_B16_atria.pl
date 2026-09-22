% ledger_B16_atria.pl - built by translate_via_api_2.py from the model's JSON (atria). Standing and marks are in the JSON.
line(foreman).
kind(foreman, farm_foreman) :- line(foreman).
body(foreman, not_stated) :- line(foreman).
line(note).
kind(note, note) :- line(note).
body(note, not_stated) :- line(note).
line(kept).
holds(kept_notes(foreman)) :- line(kept).
line(rounds).
holds(made_rounds(foreman)) :- line(rounds).
line(wrote).
holds(wrote(foreman, note)) :- line(wrote).
line(finished).
holds(finished_rounds(foreman)) :- line(finished).
line(flock).
kind(flock, flock) :- line(flock).
body(flock, not_stated) :- line(flock).
line(gate).
kind(gate, gate) :- line(gate).
body(gate, not_stated) :- line(gate).
line(topfield).
kind(top_field, field) :- line(topfield).
body(top_field, not_stated) :- line(topfield).
line(gateopen).
holds(stood_open(gate)) :- line(gateopen).
line(flocktop).
holds(is_in(flock, top_field)) :- line(flocktop).
line(since1).
claim_since(since1, is_in(flock, top_field), stood_open(gate)) :- line(since1).
line(grass).
kind(grass, grass) :- line(grass).
body(grass, not_stated) :- line(grass).
line(lowerfield).
kind(lower_field, field) :- line(lowerfield).
body(lower_field, not_stated) :- line(lowerfield).
line(nograss).
denied(remained_in(grass, lower_field)) :- line(nograss).
