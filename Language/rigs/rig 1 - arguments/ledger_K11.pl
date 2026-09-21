% ledger_K11.pl - F11 USUALLY habit feeding an ALWAYS SHOWS line (the other model's audit case, run to see what the rig really does)
line(1). line(2). line(3). line(4). line(5). line(6).
kind(today, inspection) :- line(1).
holds(raised(flag, O)) :- line(2), kind(O, inspection), not exception(2, O).
exception(2, O) :- denied(raised(flag, O)).
holds(shut(gate, O)) :- line(3), holds(raised(flag, O)).
holds(shut(gate, today)) :- line(4).
claim_since(5, shut(gate, today), kind(today, inspection)) :- line(5).
holds(kind(X,K)) :- line(6), kind(X,K).
