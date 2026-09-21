% N25-B. Actual history plus source-supplied no_push commitments.
line(m1). line(h1). line(c1). line(c2). line(w1).
holds(moved(box)) :- line(m1).
holds(records(photograph, moved(box))) :- line(h1).
denied(pushed(box)) :- line(c1).
denied(moved(box)) :- line(c2).
