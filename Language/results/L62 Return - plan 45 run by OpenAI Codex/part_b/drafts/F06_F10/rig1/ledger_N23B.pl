% N23-B. Both object-level lines are explicitly described additions.
line(f1). line(f2).
holds(red(ribbon)) :- line(f1).
holds(open(gate)) :- line(f2), holds(red(ribbon)).
