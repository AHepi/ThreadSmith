% ledger_B13_mimo.pl - built by translate_via_api_2.py from the model's JSON (mimo). Standing and marks are in the JSON.
line(a).
kind(morning, morning) :- line(a).
body(morning, not_stated) :- line(a).
line(b).
kind(platform, platform) :- line(b).
body(platform, not_stated) :- line(b).
line(j).
holds(was_cold(morning)) :- line(j).
line(c).
kind(train, train) :- line(c).
body(train, not_stated) :- line(c).
line(d).
kind(station, station) :- line(d).
body(station, not_stated) :- line(d).
line(e).
kind(signal, signal) :- line(e).
body(signal, not_stated) :- line(e).
line(f).
kind(junction, junction) :- line(f).
body(junction, not_stated) :- line(f).
line(k).
holds(left_station_late(train, station)) :- line(k).
line(l).
holds(failed(signal)) :- line(l).
line(p).
claim_because(p, left_station_late(train, station), failed(signal)) :- line(p).
line(g).
kind(porters, porter) :- line(g).
body(porters, heavy_and_standing) :- line(g).
line(h).
kind(mailbags, mailbag) :- line(h).
body(mailbags, not_stated) :- line(h).
line(m).
holds(carried(porters, mailbags, toward(end_of_platform))) :- line(m).
line(n).
holds(moved(mailbags, toward(end_of_platform))) :- line(n).
line(i).
kind(lamps, lamp) :- line(i).
body(lamps, not_stated) :- line(i).
line(o).
holds(switched_off(lamps)) :- line(o).
