% N23-A. One said premise and one explicitly described translator addition.
line(s1). line(f1).
holds(red(ribbon)) :- line(s1).
holds(open(gate)) :- line(f1), holds(red(ribbon)).
