"""
What this file does, in plain words.

Self-tests of the owner's machine (log S135): small checks that each part does
what its plain words say, run before the full tests. Each check prints PASS or
FAIL; the file ends with the count. Run it under timeout and nice.

Origin of this file: HANDED IN by the builders (Claude, for the owner, S135).
"""

import random

import the_world
import the_machine
import rule_1_recognise_objects as rule_1
import rule_2_displacement as rule_2
import rule_3_object_permanence as rule_3
import rule_4_amounts as rule_4
import the_rule_language as language
import building_addition

results = []


def check(name, condition):
    results.append((name, bool(condition)))
    print(('PASS  ' if condition else 'FAIL  ') + name)


def frame_from_text(lines):
    return tuple(tuple(0 if ch == '.' else int(ch) for ch in line) for line in lines)


# rule 1
frame = frame_from_text(['11..2', '1...2', '..3..', '9999.', '..1.1'])
objects = rule_1.recognise_objects(frame)
check('rule 1: four connected regions of one colour each are four objects; the screen is not an object (and two separate colour-1 cells are two)',
      len(objects) == 5 and sorted(o.colour for o in objects) == [1, 1, 1, 2, 3])
check('rule 1: the screen is found as a rectangle', rule_1.find_the_screen(frame) == (3, 3, 0, 3))

# rule 2
a = rule_1.SeenObject(4, [(5, 5)])
track = rule_2.Track(1, a, 0)
rule_2.move_track(track, rule_1.SeenObject(4, [(5, 6)]))
move, error, violated = rule_2.move_track(track, rule_1.SeenObject(4, [(5, 7)]))
check('rule 2: a straight step is predicted, no violation', move == (0, 1) and not violated)
move, error, violated = rule_2.move_track(track, rule_1.SeenObject(4, [(6, 7)]))
check('rule 2: a turn is a violation of the prediction', violated and error == 1)
pairs, lost, new = rule_2.match_objects_to_tracks([track], [rule_1.SeenObject(4, [(12, 12)])])
check('rule 2: an object far beyond the bounded step is not matched', not pairs and lost and new)

# rule 3
held = []
dropped = None
for i in range(4):
    t = rule_2.Track(i, rule_1.SeenObject(1 + i, [(8, 5 + 2 * i)]), 0)
    dropped = rule_3.hide(held, t, 1, (6, 15, 3, 12))
check('rule 3: a fourth hidden object drops the oldest (capacity three)', len(held) == 3 and dropped is not None and dropped.colour == 1)
out = rule_3.come_out(held, rule_1.SeenObject(3, [(8, 2)]))
check('rule 3: an object coming out is matched by colour to a held one', out is not None and out.colour == 3 and len(held) == 2)
check('rule 3: a held object not revealed at the lift is a violation',
      rule_3.check_after_the_lift(held, [rule_1.SeenObject(2, [(9, 9)])]) == [('was not there', {'colour': 4})])

# rule 4
check('rule 4: the amount of a set counts distinct things whatever their colour or size',
      rule_4.amount_of_a_set([rule_1.SeenObject(1, [(0, 0)]), rule_1.SeenObject(8, [(3, 3), (3, 4), (4, 3), (4, 4)])]) == 2)
check('rule 4: compare', rule_4.compare(3, 2) == 'more' and rule_4.compare(1, 2) == 'fewer' and rule_4.compare(2, 2) == 'equal')

# the rule language
check('the rule language holds 405 rules, each once', len({r.key() for r in language.the_fixed_list()}) == 405)
check('the fixed list puts the first expectation before the relation to be built',
      [r.in_words() for r in language.the_fixed_list()].index('after = tracked') <
      [r.in_words() for r in language.the_fixed_list()].index('after = before + added - taken away'))

# the built way
rows = []
for b, ad, t in [(1, 1, 0), (2, 2, 1), (0, 2, 1), (3, 2, 0), (4, 1, 1), (2, 3, 1), (0, 1, 0), (4, 3, 2), (1, 2, 0)]:
    rows.append({'held amounts': {'before': b, 'added': ad, 'taken away': t, 'tracked': min(b + ad - t, 3)}, 'counted after': b + ad - t})
rule_set, trace = building_addition.solve_for_all_fitting_repairs(rows, language.the_first_expectation())
check('built way: a varied ledger leaves one rule, before + added - taken away',
      [language.rule_from_key(k).in_words() for k in rule_set] == ['after = before + added - taken away'])
rule_set, trace = building_addition.solve_for_all_fitting_repairs([r for r in rows if r['held amounts']['tracked'] == r['counted after']],
                                                                  language.the_first_expectation())
check('built way: without the failed rows two rivals stay (tracking, and the relation)', len(rule_set) == 2)
shuffled = list(rows)
random.Random(3).shuffle(shuffled)
check('built way: the order of the rows and of the amounts does not change the set',
      building_addition.solve_for_all_fitting_repairs(shuffled, language.the_first_expectation(), ['tracked', 'added', 'before', 'taken away'])[0]
      == building_addition.solve_for_all_fitting_repairs(rows, language.the_first_expectation())[0])
contradiction = rows + [{'held amounts': {'before': 1, 'added': 1, 'taken away': 0, 'tracked': 2}, 'counted after': 5}]
check('built way: contradicting rows leave no rule',
      building_addition.solve_for_all_fitting_repairs(contradiction, language.the_first_expectation())[0] == set())

# the found way
found = building_addition.FoundWay()
found.learn_from_row(rows[3], rows[:4], 4)
check('found way: takes the first rule in the list that fits the rows so far', found.held_rule.origin.get('origin') == 'FOUND')

# the world and the machine together
rng = random.Random(7)
agree = 0
for n in range(20):
    before, added = rng.randint(0, 5), rng.randint(1, 4)
    taken = rng.randint(0, min(2, before + added))
    scene = the_world.amounts_scene(rng, before, added, taken, shapes=the_world.SHAPES_IN_TESTS)
    report = the_machine.TheMachine('none', learning_on=False).watch_scene(scene.frames)
    held_amounts = report['lift']['held amounts']
    agree += (held_amounts['before'], held_amounts['added'], held_amounts['taken away'], report['lift']['counted after']) == \
        (before, added, taken, before + added - taken)
check('machine: the held amounts and the count at the lift agree with the world in 20 of 20 scenes', agree == 20)
machine = the_machine.TheMachine('built')
for scene in the_world.building_schedule(1350, number_of_scenes=60):
    machine.watch_scene(scene.frames, scene.label)
check('machine: after 60 building scenes the built way holds before + added - taken away, origin BUILT',
      machine.learner.held_rule.in_words() == 'after = before + added - taken away' and machine.learner.held_rule.origin['origin'] == 'BUILT')
scene = the_world.pass_behind_scene(random.Random(2), 'vanishes')
report = the_machine.TheMachine('none').watch_scene(scene.frames)
check('machine: an object that vanished behind the screen is a violation at the lift',
      any(k == 'permanence: was not there' for (_, k, _) in report['violations']))

passed = sum(ok for _, ok in results)
print('%d of %d self-tests passed' % (passed, len(results)))
raise SystemExit(0 if passed == len(results) else 1)
