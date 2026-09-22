% laws.pl
% What this file does: the shape book, the response classes, the strength relations and the general laws.
% It is the same for every ledger. Developed on the owner's ball and coin paragraph only, then frozen.
#pred line(N) :: 'line @(N) is in the ledger'.

% ---- the shape book: a verb is a shape the checker sees, plus a name it does not ----
shape(throw, press_release). shape(toss, press_release). shape(hurl, press_release).
shape(push, press). shape(pull, press). shape(lean_on, press). shape(hit, press).
shape(drop, release). shape(open_fist_on, release). shape(let_go_of, release).
shape(close_fist_on, hold). shape(hold, hold).
has_press(press_release). has_press(press).
has_release(press_release). has_release(release).
has_hold(hold).
presses(E, I, T, D) :- did(E, I, V, T, D), shape(V, S), has_press(S).
releases(E, I, T) :- did(E, I, V, T, _), shape(V, S), has_release(S).
holds_back(E, I, T) :- did(E, I, V, T, _), shape(V, S), has_hold(S).

% ---- response classes: how a thing answers a press ----
resistance(T, small) :- body(T, light_loose).
resistance(T, large) :- body(T, heavy_loose).
resistance(T, large) :- body(T, heavy_standing).
resistance(T, unbeatable) :- body(T, fixed).
capacity(T, S) :- resistance(T, S).
tendency(T, down) :- body(T, light_loose).
tendency(T, down) :- body(T, heavy_loose).

% ---- strength: three levels, compared, never measured ----
lesser(small, small, small). lesser(small, large, small). lesser(small, unbeatable, small).
lesser(large, small, small). lesser(large, large, large). lesser(large, unbeatable, large).
lesser(unbeatable, small, small). lesser(unbeatable, large, large). lesser(unbeatable, unbeatable, unbeatable).
far_smaller(small, large). far_smaller(small, unbeatable). far_smaller(large, unbeatable).

% ---- directions ----
opposite(toward(X), away_from(X)). opposite(away_from(X), toward(X)). opposite(up, down). opposite(down, up).

% ---- physical laws ----
% you cannot press hard on something that gives way: a press is never bigger than what the pressed thing resists
press_size(E, Size) :- presses(E, I, T, _), capacity(I, C), resistance(T, R), lesser(C, R, Size).
press_on(T, D, Size, direct(E)) :- presses(E, _, T, D), press_size(E, Size).
% every press is pressed back equally, the other way
press_on(I, Opp, Size, pushback(E)) :- presses(E, I, _, D), opposite(D, Opp), press_size(E, Size).
% law of making and law of direction: a thing CAN move a given way only if a press that way is not far smaller than what it resists
can_move(T, D, pressed(Src)) :- press_on(T, D, Size, Src), resistance(T, R), not far_smaller(Size, R).
% law of letting: a release can only produce what the thing was already heading for
can_move(T, D, released(E)) :- releases(E, _, T), tendency(T, D).
% a link in a chain: could THIS earlier happening have produced that movement? (names the happening, so the laws never loop back on themselves)
result_possible(E, T, D) :- press_on(T, D, Size, direct(E)), resistance(T, R), not far_smaller(Size, R).
result_possible(E, T, D) :- press_on(T, D, Size, pushback(E)), resistance(T, R), not far_smaller(Size, R).
result_possible(E, T, D) :- releases(E, _, T), tendency(T, D).
% a thing MUST move if the press dwarfs what it resists, or if it is let go and heads somewhere
must_move(T, D, pressed(Src)) :- press_on(T, D, Size, Src), resistance(T, R), far_smaller(R, Size).
must_move(T, D, released(E)) :- releases(E, _, T), tendency(T, D).

% ---- people, groups and rules: only the word-and-slots laws ----
needs_tendency(lets). needs_tendency(helps). needs_tendency(stops).
needs_no_tendency(makes).
word_misfit(E, Word) :- social(E, Word, _, T, R), needs_tendency(Word), tends_not(T, R).
word_misfit(E, Word) :- social(E, Word, _, T, R), needs_no_tendency(Word), tends(T, R).
tendency_stated(E) :- social(E, _, _, T, R), tends(T, R).
tendency_stated(E) :- social(E, _, _, T, R), tends_not(T, R).

% ---- PATCH 1 (forced by case X1, the wind): an influence with no response class. The press is real but its size cannot be judged.
has_capacity(I) :- capacity(I, _).
press_unsized(E, I, T, D) :- presses(E, I, T, D), not has_capacity(I).
% ---- PATCH 2 (forced by case X2, kick): a verb that is not in the shape book. Counted, never silently dropped.
known_verb(V) :- shape(V, _).
no_shape(E, V, T) :- did(E, _, V, T, _), not known_verb(V).

% ---- PATCH 3 (pile 2, finding F01): the thing pressed has no stated response to a press. The press is real; whether it is enough cannot be judged.
has_resistance(T) :- resistance(T, _).
press_unresisted(E, I, T, D) :- presses(E, I, T, D), not has_resistance(T).
