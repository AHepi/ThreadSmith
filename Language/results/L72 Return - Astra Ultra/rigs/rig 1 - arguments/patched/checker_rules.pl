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

% --- PATCH 3 (after first runs of B-E): direction. "What produced it" is kept apart from "how we know it".
% A ledger line that says what MAKES something happen is written with produced(...).
% A line that says what SHOWS something stays as holds(...). Whatever is produced also holds.
#pred produced(F) :: 'something in the ledger makes this happen: @(F)'.
#pred missing(F) :: 'a line nobody wrote would be needed: @(F)'.
holds(F) :- produced(F).

% --- PATCH 9 (pile 2, finding F14): an exception of the "did not apply" kind. The line is switched off for that thing; nothing is said about what happened instead.
#pred exempt(N,X) :: '@(X) is exempt from line @(N)'.
exception(N, X) :- exempt(N, X).

% --- PATCH 14 (pile 3, F08): wording for a denied BECAUSE
#pred denied_because(N,E,C) :: 'line @(N) denies that @(C) produced @(E)'.
