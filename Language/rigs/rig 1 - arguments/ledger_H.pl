% ledger_H.pl - the owner's Mondays paragraph
line(1). line(2). line(3). line(4). line(5). line(6). line(7). line(8). line(9). line(10). line(11). line(12). line(13). line(14).
line(15). line(16). line(17). line(18). line(19). line(20). line(21). line(22). line(23). line(24). line(25). line(26). line(27).
holds(arbitrary(X)) :- line(1), holds(is_beginning(X)).
holds(is_beginning(monday)) :- line(2).
holds(lacks_authority(X)) :- line(3), holds(arbitrary(X)).
holds(lacks_authority(monday)) :- line(4).
claim_since(5, lacks_authority(monday), is_beginning(monday)) :- line(5).
holds(no_duty_to_obey(X)) :- line(6), holds(lacks_authority(X)).
holds(issues_command(monday)) :- line(7).
holds(no_duty_to_obey(monday)) :- line(8).
claim_since(9, no_duty_to_obey(monday), lacks_authority(monday)) :- line(9).
holds(is_suggestion(C)) :- line(10), holds(is_command(C)), holds(unheeded(C)).
holds(is_command(mondays_command)) :- line(11).
holds(is_suggestion(monday)) :- line(12).
claim_since(13, is_suggestion(monday), no_duty_to_obey(monday)) :- line(13).
holds(optional(X)) :- line(14), holds(is_suggestion(X)).
holds(ceases_if_ignored(monday)) :- line(15).
claim_since(16, ceases_if_ignored(monday), optional(monday)) :- line(16).
denied(exists(monday)) :- line(17).
produced(becomes(tuesday, monday)) :- line(18), denied(exists(monday)).
holds(exists(D)) :- line(19), holds(becomes(X, D)).
holds(week_is_one_day) :- line(20).
claim_since(21, week_is_one_day, becomes(tuesday, monday)) :- line(21).
holds(unemployed(time)) :- line(22).
claim_since(23, unemployed(time), week_is_one_day) :- line(23).
holds(is_leisure(X)) :- line(24), holds(unemployed(X)).
holds(basis_of_culture(X)) :- line(25), holds(is_leisure(X)).
holds(saves_civilization(sleeping_in)) :- line(26).
claim_since(27, saves_civilization(sleeping_in), basis_of_culture(time)) :- line(27).
