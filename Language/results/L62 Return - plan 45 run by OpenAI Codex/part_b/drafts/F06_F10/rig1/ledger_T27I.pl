% T27-I. No dependent content is invented for the binned at-least-one clause.
line(s1). line(f1).
holds(open(side_gate)) :- line(s1).
holds(open(front_gate)) :- line(f1).
