% T27-B. Inclusive Only-ways constraint with both alternatives true.
line(n1). line(s1). line(f1).
denied(entry) :- line(n1), denied(open(side_gate)), denied(open(front_gate)).
holds(open(side_gate)) :- line(s1).
holds(open(front_gate)) :- line(f1).
