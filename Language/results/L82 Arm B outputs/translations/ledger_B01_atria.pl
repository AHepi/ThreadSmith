% ledger_B01_atria.pl - built by translate_via_api_2.py from the model's JSON (atria). Standing and marks are in the JSON.
line(f1).
kind(foreman, farm_foreman) :- line(f1).
body(foreman, not_stated) :- line(f1).
line(n1).
kind(note, note) :- line(n1).
body(note, not_stated) :- line(n1).
line(k1).
holds(kept(foreman, note)) :- line(k1).
line(e1).
holds(ended(note)) :- line(e1).
line(sh1).
kind(shepherd, shepherd) :- line(sh1).
body(shepherd, not_stated) :- line(sh1).
line(fl1).
kind(flock, flock) :- line(fl1).
body(flock, not_stated) :- line(fl1).
line(g1).
kind(gate, gate) :- line(g1).
body(gate, not_stated) :- line(g1).
line(tf1).
kind(top_field, field) :- line(tf1).
body(top_field, not_stated) :- line(tf1).
line(go1).
holds(open(gate)) :- line(go1).
line(fi1).
holds(in_field(flock, top_field)) :- line(fi1).
line(si1).
claim_since(si1, in_field(flock, top_field), open(gate)) :- line(si1).
line(al1).
holds(driven_through(flock, gate)) :- line(al1), holds(left_open(shepherd, gate)).
line(lo1).
holds(left_open(shepherd, gate)) :- line(lo1).
line(al2).
holds(in_field(flock, top_field)) :- line(al2), holds(driven_through(flock, gate)).
line(lf1).
kind(lower_field, field) :- line(lf1).
body(lower_field, not_stated) :- line(lf1).
line(eg1).
holds(empty_of_grass(lower_field)) :- line(eg1).
