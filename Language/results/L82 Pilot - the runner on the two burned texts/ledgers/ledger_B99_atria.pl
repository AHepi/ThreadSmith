% ledger_B99_atria.pl - built by translate_via_api.py from the model's JSON (atria). Standing and marks are in the JSON.
line(lamp).
kind(lamp, lamp) :- line(lamp).
body(lamp, not_stated) :- line(lamp).
line(burning).
holds(burning(lamp)) :- line(burning).
line(inspector).
kind(inspector, person) :- line(inspector).
body(inspector, not_stated) :- line(inspector).
line(iw_lamp).
kind(lamp, lamp) :- line(iw_lamp).
body(lamp, not_stated) :- line(iw_lamp).
line(iw_burning).
holds(burning(lamp)) :- line(iw_burning).
line(iw_visitor).
kind(visitor, visitor) :- line(iw_visitor).
body(visitor, not_stated) :- line(iw_visitor).
line(iw_returned).
holds(returned(visitor)) :- line(iw_returned).
line(iw_since).
claim_since(iw_since, returned(visitor), burning(lamp)) :- line(iw_since).
line(visitor).
kind(visitor, visitor) :- line(visitor).
body(visitor, not_stated) :- line(visitor).
line(returned).
holds(returned(visitor)) :- line(returned).
line(deny).
denied_because(deny, returned(visitor), burning(lamp)) :- line(deny).
