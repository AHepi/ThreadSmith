% F05 N17-A selected after source review and before execution.
% Assistance is HELPS; no LETS line and no tendency is added.
line(h1). line(s1).
social(n17a, helps, handle_adjustment, gate, open) :- line(h1).
holds(stayed_shut(gate)) :- line(s1).
