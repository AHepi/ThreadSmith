% ledger_K19.pl - F19 a usual-case line that simply states the conclusion
line(1). line(2). line(3). line(4).
holds(raised(flag)) :- line(1).
holds(shut(gate)) :- line(2).
claim_since(3, shut(gate), raised(flag)) :- line(3).
holds(shut(gate)) :- line(4).
