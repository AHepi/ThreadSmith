% F05 N17-B selected after source review and before execution.
% Ordinary production is BECAUSE; no narrow MAKES line is added.
line(a1). line(o1). line(c1).
holds(adjusted(handle)) :- line(a1).
holds(open(gate)) :- line(o1).
claim_because(c1, open(gate), adjusted(handle)) :- line(c1).
