% checker_rules.pl
% What this file does: the fixed rules every ledger is checked against.
% Developed on paragraph A only, then frozen. Anything added later is marked PATCH with a date and reason.

% --- read-back wording (fixed rules, no guessing) ---
#pred line(N) :: 'line @(N) is in the ledger'.
#pred kind(X,K) :: '@(X) is a @(K)'.
#pred contradiction(F) :: 'the ledger both gives and denies: @(F)'.
#pred holds(F) :: 'it follows or was said that: @(F)'.
#pred denied(F) :: 'you said this is not so: @(F)'.
#pred exception(N,X) :: '@(X) is a known exception to line @(N)'.
#pred achieves(A,F) :: 'doing @(A) changes something that @(F) depends on'.
#pred changes(A,X) :: 'doing @(A) changes @(X)'.
#pred depends_on(F,X) :: '@(F) depends, directly or through other things, on @(X)'.
#pred depends(F,X) :: '@(F) depends directly on @(X)'.

% --- check 1: contradiction ---
contradiction(F) :- holds(F), denied(F).

% --- check 3: does a plan touch what its goal depends on? ---
achieves(A, F) :- changes(A, X), depends_on(F, X).
depends_on(F, X) :- depends(F, X).
depends_on(F, X) :- depends(F, Y), depends_on(Y, X).
