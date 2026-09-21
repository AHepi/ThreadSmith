% T26-B. Only-ways compiled as an ALWAYS SHOWS negative constraint.
line(n1). line(e1).
denied(entry) :- line(n1), denied(open(side_gate)), denied(open(front_gate)).
holds(entry) :- line(e1).
