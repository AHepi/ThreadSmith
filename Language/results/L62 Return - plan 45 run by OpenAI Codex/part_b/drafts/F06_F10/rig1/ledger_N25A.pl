% N25-A. Actual record and proposed counterfactual answer remain distinguishable in JSON.
line(p1). line(m1). line(h1). line(w1).
holds(pushed(box)) :- line(p1).
holds(moved(box)) :- line(m1).
holds(records(photograph, moved(box))) :- line(h1).
