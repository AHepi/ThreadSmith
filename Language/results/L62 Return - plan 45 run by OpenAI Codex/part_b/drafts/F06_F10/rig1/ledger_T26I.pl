% T26-I. Only-ways compiled as an ALWAYS SHOWS negative constraint.
line(e1). line(n1).
holds(entered(cart)) :- line(e1).
denied(entered(cart)) :- line(n1), denied(open(side_gate)), denied(open(front_gate)).
