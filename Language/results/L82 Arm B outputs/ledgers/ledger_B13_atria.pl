% ledger_B13_atria.pl - built by translate_via_api_2.py from the model's JSON (atria). Standing and marks are in the JSON.
line(a).
kind(morning, morning) :- line(a).
body(morning, not_stated) :- line(a).
line(b).
kind(platform, platform) :- line(b).
body(platform, not_stated) :- line(b).
line(c).
holds(cold(morning)) :- line(c).
line(d).
holds(empty(platform)) :- line(d).
line(e).
kind(train, train) :- line(e).
body(train, not_stated) :- line(e).
line(f).
kind(station, station) :- line(f).
body(station, not_stated) :- line(f).
line(g).
kind(signal, signal) :- line(g).
body(signal, not_stated) :- line(g).
line(h).
kind(junction, junction) :- line(h).
body(junction, not_stated) :- line(h).
line(i).
holds(left(train, station)) :- line(i).
line(j).
holds(failed(signal)) :- line(j).
line(k).
claim_because(k, left(train, station), failed(signal)) :- line(k).
line(l).
kind(porters, porter) :- line(l).
body(porters, heavy_and_standing) :- line(l).
line(m).
kind(mailbags, mailbag) :- line(m).
body(mailbags, not_stated) :- line(m).
line(n).
holds(carried(porters, mailbags)) :- line(n).
line(o).
kind(lamps, lamp) :- line(o).
body(lamps, not_stated) :- line(o).
line(p).
holds(pulled_out(train)) :- line(p).
line(q).
holds(switched_off(lamps)) :- line(q).
