"""
What this file does, in plain words.

Runs every test of the owner's machine (log S135) and writes the raw output to
the scratchpad folder given on the command line (never into git), plus one
summary file. Sections, as written before building:
  (a) the four handed-in rules alone: recognising objects, displacement,
      object permanence, amounts;
  (b) the amounts tests of the infant studies' kind (one joins one behind the
      screen; two take away one; larger amounts, some never shown while
      building), on the machine with the four rules only, after building and
      after finding;
  (c) the building of addition: the ledger, what each failure changed, the rule
      formed and its origin; its use on unseen test scenes; the part-level
      what-if check; the controls (no difficulty; no permanence; the same
      ledger without the failures);
  (d) the knock-outs: permanence off; the built rule removed; sham; restore;
      displacement off;
  (e) the order-shuffle check;
  (f) the same-final-frame check.
Everything is deterministic from fixed seeds. Run it under timeout and nice.

Origin of this file: HANDED IN by the builders (Claude, for the owner, S135).
"""

import copy
import json
import os
import random
import sys
import time
from collections import Counter

import the_world
import the_machine
import the_rule_language as language
import building_addition

BUILDING_SEED = 1350
TEST_SEED = 2350


def build_machine(way, rule_3_on=True, schedule=None, amount_order=None, fixed_list=None):
    machine = the_machine.TheMachine(way, rule_3_on=rule_3_on, amount_order=amount_order, fixed_list=fixed_list)
    for scene in (schedule if schedule is not None else the_world.building_schedule(BUILDING_SEED)):
        machine.watch_scene(scene.frames, scene.label)
    machine.learning_on = False
    return machine


def triples_seen_while_building(schedule):
    return {(s.facts['before'], s.facts['added'], s.facts['taken away']) for s in schedule if s.facts.get('lift')}


# ---------------------------------------------------------------- (a) the four rules alone
def section_a():
    rng = random.Random(TEST_SEED)
    out = {}
    # recognising objects
    right_apart, total_apart, touching_frames, touching_counted_as_fewer = 0, 0, 0, 0
    for i in range(700):
        frame, true_count, touching = the_world.random_still_frame(rng, allow_same_colour_touching=(i >= 500))
        seen = len(the_machine.rule_1.recognise_objects(frame))
        if touching:
            touching_frames += 1
            touching_counted_as_fewer += seen < true_count
        else:
            total_apart += 1
            right_apart += seen == true_count
    out['recognise objects'] = {'frames with no two of one colour touching': total_apart, 'counted right': right_apart,
                                'frames with two of one colour touching': touching_frames,
                                'of those, counted as fewer (the declared limit)': touching_counted_as_fewer}

    # displacement: walk scenes with turns and jumps, test colours and shapes
    def displacement_scores(rule_2_on=True):
        rng_walk = random.Random(TEST_SEED + 1)
        straight, straight_flagged, changed, changed_flagged = 0, 0, 0, 0
        tracks_total, tracks_one_object = 0, 0
        jumps, jumps_flagged = 0, 0
        for n in range(60):
            scene = the_world.walk_scene(rng_walk, rng_walk.randint(1, 4), colours=the_world.BUILDING_COLOURS + the_world.TEST_ONLY_COLOURS,
                                         shapes=the_world.SHAPES_IN_TESTS, frames=30, chance_of_turn=0.08, chance_of_jump=0.03,
                                         label='test walk')
            machine = the_machine.TheMachine('none', rule_2_on=rule_2_on, learning_on=False)
            report = machine.watch_scene(scene.frames)
            jump_frames = {(t, d['true number']) for (t, kind, d) in scene.events if kind == 'jump'}
            flagged_frames = {t for (t, kind, d) in report['violations'] if kind in ('displacement: vanished in plain sight', 'displacement: appeared from nowhere')}
            for (t, number) in jump_frames:
                jumps += 1
                jumps_flagged += t in flagged_frames
            # per object, per frame
            positions = [{o[0]: (o[2], o[3]) for o in tf['objects']} for tf in scene.truth_per_frame]
            track_of_object = []
            for pf, tf in zip(report['per frame'], scene.truth_per_frame):
                owner = tf['owner_of_visible_cell']
                mapping = {}
                for (number, cells) in pf['tracks']:
                    owners = {owner.get(c) for c in cells} - {None}
                    if len(owners) == 1:
                        mapping[owners.pop()] = number
                track_of_object.append(mapping)
            for t in range(2, len(scene.frames)):
                for number in positions[t]:
                    if number not in positions[t - 1] or number not in positions[t - 2]:
                        continue
                    if (t, number) in jump_frames or (t - 1, number) in jump_frames:
                        continue
                    track = track_of_object[t].get(number)
                    if track is None or track != track_of_object[t - 1].get(number) or track != track_of_object[t - 2].get(number):
                        continue
                    move_now = (positions[t][number][0] - positions[t - 1][number][0], positions[t][number][1] - positions[t - 1][number][1])
                    move_before = (positions[t - 1][number][0] - positions[t - 2][number][0], positions[t - 1][number][1] - positions[t - 2][number][1])
                    flagged = any(v for (n, e, v) in report['per frame'][t]['predictions'] if n == track)
                    if move_now == move_before:
                        straight += 1
                        straight_flagged += flagged
                    else:
                        changed += 1
                        changed_flagged += flagged
            # identity: does each machine track stay with one true object?
            objects_of_track = {}
            for pf, tf in zip(report['per frame'], scene.truth_per_frame):
                owner = tf['owner_of_visible_cell']
                for (number, cells) in pf['tracks']:
                    owners = {owner.get(c) for c in cells} - {None}
                    objects_of_track.setdefault(number, set()).update(owners)
            for number, owners in objects_of_track.items():
                tracks_total += 1
                tracks_one_object += len(owners) == 1
        return {'straight steps': straight, 'straight steps flagged (false alarms)': straight_flagged,
                'changed steps (turn, bounce, blocked)': changed, 'changed steps flagged': changed_flagged,
                'jumps': jumps, 'jumps flagged (vanished and appeared)': jumps_flagged,
                'tracks': tracks_total, 'tracks that stayed with one object': tracks_one_object}
    out['displacement'] = displacement_scores()

    # object permanence: four variants
    permanence = {}
    expected = {'comes out': set(), 'stays behind': {'permanence: did not come out'},
                'vanishes': {'permanence: did not come out', 'permanence: was not there'},
                'different one': {'permanence: a different one came out'}}
    for rule_3_on in (True, False):
        for variant in expected:
            rng_pass = random.Random(TEST_SEED + 2)
            got, extra = 0, 0
            for n in range(40):
                scene = the_world.pass_behind_scene(rng_pass, variant, two=(n % 4 == 0),
                                                    colours=the_world.BUILDING_COLOURS + the_world.TEST_ONLY_COLOURS,
                                                    shapes=[(1, 1), (2, 2)] if n % 4 else [(1, 1)])
                machine = the_machine.TheMachine('none', rule_3_on=rule_3_on, learning_on=False)
                report = machine.watch_scene(scene.frames)
                kinds = {k for (_, k, _) in report['violations'] if k.startswith('permanence')}
                got += expected[variant] <= kinds
                extra += bool(kinds - expected[variant] - {'permanence: did not come out', 'permanence: was not there'}) if variant == 'different one' else bool(kinds - expected[variant])
            permanence[('permanence on' if rule_3_on else 'permanence off') + ', ' + variant] = {
                'scenes': 40, 'expected violations all logged': got, 'scenes with an unexpected permanence violation': extra}
    out['object permanence'] = permanence

    # amounts, frame by frame, behind the screen
    def amount_scores(rule_3_on=True, rule_2_on=True):
        rng_amount = random.Random(TEST_SEED + 3)
        result = Counter()
        for n in range(200):
            before = rng_amount.randint(0, 7)
            added = rng_amount.randint(1, 5)
            taken = rng_amount.randint(0, min(3, before + added))
            scene = the_world.amounts_scene(rng_amount, before, added, taken, colours=the_world.BUILDING_COLOURS + the_world.TEST_ONLY_COLOURS,
                                            shapes=the_world.SHAPES_IN_TESTS)
            if scene is None:
                continue
            machine = the_machine.TheMachine('none', rule_3_on=rule_3_on, rule_2_on=rule_2_on, learning_on=False)
            report = machine.watch_scene(scene.frames)
            group = 'scenes never more than three behind' if before + added <= 3 else 'scenes more than three behind at some time'
            for pf, tf in zip(report['per frame'], scene.truth_per_frame):
                true_amount = tf['true_amount_behind_screen']
                if true_amount is None or pf['amount in the screen region'] is None:
                    continue
                result[(group, 'frames')] += 1
                result[(group, 'right')] += pf['amount in the screen region'] == true_amount
        return {'%s: %s' % k: v for k, v in sorted(result.items())}
    out['amounts behind the screen, frame by frame'] = {'all four rules': amount_scores(),
                                                         'permanence off': amount_scores(rule_3_on=False),
                                                         'displacement off': amount_scores(rule_2_on=False)}
    return out


# ---------------------------------------------------------------- shared test scenes
def unseen_test_scenes(number=300, seed=TEST_SEED + 10):
    rng = random.Random(seed)
    scenes = []
    while len(scenes) < number:
        before = rng.randint(0, 9)
        added = rng.randint(1, 5)
        taken = rng.randint(0, min(4, before + added))
        impossible = rng.choice([None, None, 'one more', 'one fewer'])
        if impossible == 'one fewer' and before + added - taken == 0:
            impossible = 'one more'
        scene = the_world.amounts_scene(rng, before, added, taken, impossible=impossible,
                                        colours=the_world.TEST_ONLY_COLOURS + the_world.BUILDING_COLOURS,
                                        shapes=the_world.SHAPES_IN_TESTS, label='test amounts')
        if scene is not None:
            scenes.append(scene)
    return scenes


def score_on_test_scenes(machine, scenes, seen_triples):
    result = Counter()
    for scene in scenes:
        m = copy.deepcopy(machine)
        report = m.watch_scene(scene.frames, scene.label)
        lift = report['lift']
        f = scene.facts
        triple = (f['before'], f['added'], f['taken away'])
        most_behind = f['before'] + f['added']
        beyond = 'more than three behind at some time' if most_behind > 3 else 'never more than three behind'
        seen = 'triple seen while building' if triple in seen_triples else 'triple never seen while building'
        flagged = lift['verdict'] in ('more', 'fewer')
        right = lift['prediction'] == f['true after']
        if f['impossible'] is None:
            for group in ('all', beyond, seen, 'before is zero' if f['before'] == 0 else 'before is not zero'):
                result[('possible', group, 'scenes')] += 1
                result[('possible', group, 'expected right, no violation')] += (not flagged) and right
                result[('possible', group, 'violation logged (a false alarm)')] += flagged
        else:
            for group in ('all', beyond, seen):
                result[('impossible', group, 'scenes')] += 1
                result[('impossible', group, 'violation logged')] += flagged
        result[('undetermined', 'all', 'scenes')] += lift['prediction'] == 'undetermined'
    return {'%s | %s | %s' % k: v for k, v in sorted(result.items())}


# ---------------------------------------------------------------- (b) infant-style amounts tests
def section_b(machines, seen_triples):
    cases = [((1, 1, 0), 'one joins one'), ((2, 0, 1), 'two take away one'),
             ((2, 2, 0), None), ((3, 1, 1), None), ((1, 3, 0), None),
             ((4, 3, 0), None), ((5, 5, 0), None), ((7, 4, 0), None), ((6, 2, 3), None), ((9, 5, 4), None)]
    out = {}
    for (before, added, taken), name in cases:
        triple_name = name or '%d + %d - %d' % (before, added, taken)
        true_after = before + added - taken
        for outcome in ('possible', 'one fewer', 'one more'):
            shown = true_after + {'possible': 0, 'one fewer': -1, 'one more': 1}[outcome]
            key = '%s, the screen lifts on %d (%s)' % (triple_name, shown, 'expected' if outcome == 'possible' else 'impossible')
            out[key] = {'seen while building': (before, added, taken) in seen_triples}
            for machine_name, machine in machines.items():
                rng = random.Random(hash(key) % 100000 + TEST_SEED)
                violations, rights = 0, 0
                for repeat in range(10):
                    scene = the_world.amounts_scene(rng, before, added, taken,
                                                    impossible=None if outcome == 'possible' else outcome,
                                                    colours=the_world.TEST_ONLY_COLOURS + the_world.BUILDING_COLOURS,
                                                    shapes=the_world.SHAPES_IN_TESTS)
                    report = copy.deepcopy(machine).watch_scene(scene.frames)
                    lift = report['lift']
                    violations += lift['verdict'] in ('more', 'fewer')
                    rights += lift['prediction'] == true_after
                out[key][machine_name] = {'violations logged, of 10': violations, 'expected the true amount, of 10': rights}
    return out


# ---------------------------------------------------------------- (c) building, controls and use
def replay(learner, rows, shuffle_rows_inside=None):
    """Feeds ledger rows to a learner in the given order; returns the held rule after each row."""
    held_after = []
    so_far = []
    for i, row in enumerate(rows):
        if building_addition.usable(row):
            so_far.append(row)
        given = list(so_far)
        if shuffle_rows_inside is not None:
            shuffle_rows_inside.shuffle(given)
        learner.learn_from_row(row, given, i + 1)
        rivals = getattr(learner, 'rivals', None)
        if rivals:
            held_after.append('rivals: ' + '; '.join(language.rule_from_key(k).in_words() for k in sorted(rivals)))
        else:
            held_after.append(learner.held_rule.in_words())
    return held_after


def section_c(schedule, built, found, filter_all, none, test_scenes, seen_triples):
    out = {}
    # the ledger and the building log
    out['ledger rows'] = len(built.ledger)
    out['usable ledger rows'] = sum(building_addition.usable(r) for r in built.ledger)
    out['rows where the first expectation (tracking) failed'] = sum(
        1 for r in built.ledger if building_addition.usable(r) and language.the_first_expectation().expected_after(r['held amounts']) != r['counted after'])
    out['built way: what each failure and each new row changed'] = [
        {k: v for k, v in e.items() if k != 'trace'} | {'errors of the old expectation on the rows used': e['trace'].get('errors of the old expectation'),
                                                        'rank': e['trace'].get('rank'),
                                                        'free directions': e['trace'].get('free directions left open by the rows')}
        for e in built.learner.log]
    out['built way: the rule held at the end'] = built.current_rule_in_words()
    out['built way: its origin record'] = built.learner.held_rule.origin
    out['found way: log'] = found.learner.log
    out['found way: the rule held at the end'] = found.current_rule_in_words()
    out['found way: its origin record'] = found.learner.held_rule.origin
    out['filter-all way: log'] = filter_all.learner.log
    out['filter-all way: the rule held at the end'] = filter_all.current_rule_in_words()
    out['the first 12 ledger rows'] = [{'held amounts': r['held amounts'], 'counted after': r['counted after'],
                                        'prediction': r['prediction'], 'verdict': r['verdict'], 'held rule': r['held rule']}
                                       for r in built.ledger[:12]]

    # use on unseen test scenes
    out['use on 300 test scenes'] = {name: score_on_test_scenes(m, test_scenes, seen_triples)
                                     for name, m in (('four rules only', none), ('built', built), ('found', found), ('filter all', filter_all))}

    # the part-level what-if check
    rng = random.Random(TEST_SEED + 20)
    agree, total = 0, 0
    by_edit = Counter()
    for n in range(100):
        before = rng.randint(1, 8)
        added = rng.randint(1, 4)
        taken = rng.randint(0, 3)
        edit = rng.choice([('before', 1), ('before', -1), ('added', 1), ('added', -1), ('taken away', 1), ('taken away', -1)])
        values = {'before': before, 'added': added, 'taken away': taken}
        edited = dict(values)
        edited[edit[0]] += edit[1]
        if edited['added'] < 1 or edited['taken away'] < 0 or edited['taken away'] > edited['before'] + edited['added'] \
                or values['taken away'] > values['before'] + values['added'] or edited['before'] < 0:
            continue
        seed = rng.randint(0, 10 ** 6)
        answers, world = [], []
        for v in (values, edited):
            scene = the_world.amounts_scene(random.Random(seed), v['before'], v['added'], v['taken away'],
                                            colours=the_world.TEST_ONLY_COLOURS, shapes=the_world.SHAPES_IN_TESTS)
            if scene is None:
                break
            report = copy.deepcopy(built).watch_scene(scene.frames)
            answers.append(report['lift']['prediction'])
            world.append(scene.facts['true after'])
        if len(answers) < 2:
            continue
        total += 1
        ok = (answers[1] - answers[0]) == (world[1] - world[0]) and answers[1] == world[1]
        agree += ok
        by_edit['%s %+d' % edit] += ok
        by_edit['%s %+d (scenes)' % edit] += 1
    out['part-level what-if check'] = {'edited scenes': total, 'the rule\'s answer changed as the world\'s did': agree, 'by edit': dict(by_edit)}

    # controls
    control_schedule = the_world.building_schedule(BUILDING_SEED, largest_amount=3)
    control = build_machine('built', schedule=control_schedule)
    out['control: no difficulty (never more than three behind)'] = {
        'scenes': len(control_schedule), 'ledger rows': len(control.ledger),
        'rows where tracking failed': sum(1 for r in control.ledger if building_addition.usable(r) and r['verdict'] not in ('equal',)),
        'state at the end': control.learner.state, 'rule held': control.current_rule_in_words()}
    no_permanence = build_machine('built', rule_3_on=False, schedule=schedule)
    out['control: building with permanence off from the start'] = {
        'state at the end': no_permanence.learner.state, 'rule held': no_permanence.current_rule_in_words(),
        'log': [{k: v for k, v in e.items() if k != 'trace'} | {'outcome': e['trace'].get('outcome')} for e in no_permanence.learner.log][:6]}
    usable_rows = [r for r in built.ledger if building_addition.usable(r)]
    first = language.the_first_expectation()
    successes = [r for r in usable_rows if first.expected_after(r['held amounts']) == r['counted after']]
    failures = [r for r in usable_rows if first.expected_after(r['held amounts']) != r['counted after']]
    for name, rows in (('the same ledger without the failed rows', successes), ('the failed rows only', failures),
                       ('the whole ledger', usable_rows)):
        rule_set, trace = building_addition.solve_for_all_fitting_repairs(rows, first)
        out['control: ' + name] = {'rows': len(rows), 'rules left': [language.rule_from_key(k).in_words() for k in sorted(rule_set)],
                                   'rank': trace.get('rank'), 'free directions': trace.get('free directions left open by the rows')}
    return out


# ---------------------------------------------------------------- (d) knock-outs
def section_d(built, found, test_scenes, seen_triples, schedule):
    out = {}
    out['intact (built)'] = score_on_test_scenes(built, test_scenes, seen_triples)
    m = copy.deepcopy(built); m.rule_3_on = False
    out['permanence off (built)'] = score_on_test_scenes(m, test_scenes, seen_triples)
    m = copy.deepcopy(found); m.rule_3_on = False
    out['permanence off (found)'] = score_on_test_scenes(m, test_scenes, seen_triples)
    m = copy.deepcopy(built); m.remove_the_held_rule()
    out['built rule removed'] = score_on_test_scenes(m, test_scenes, seen_triples)
    sham = copy.deepcopy(built); sham.sham_removal()
    out['sham removal'] = score_on_test_scenes(sham, test_scenes, seen_triples)
    m.restore_the_held_rule()
    out['restored'] = score_on_test_scenes(m, test_scenes, seen_triples)
    m = copy.deepcopy(built); m.rule_2_on = False
    out['displacement off (built)'] = score_on_test_scenes(m, test_scenes, seen_triples)
    # identical predictions? (sham and restore against intact, scene by scene)
    def predictions(machine):
        return [copy.deepcopy(machine).watch_scene(s.frames)['lift']['prediction'] for s in test_scenes]
    intact = predictions(built)
    out['scenes where the sham changed the prediction'] = sum(a != b for a, b in zip(intact, predictions(sham)))
    out['scenes where the restored machine differs from the intact one'] = sum(a != b for a, b in zip(intact, predictions(_restored(built))))
    return out


def _restored(built):
    m = copy.deepcopy(built)
    m.remove_the_held_rule()
    m.restore_the_held_rule()
    return m


# ---------------------------------------------------------------- (e) order shuffle
def section_e(built):
    rows = list(built.ledger)
    out = {}
    base_list = language.the_fixed_list()

    def summarise(histories):
        finals = Counter(h[-1] for h in histories)
        distinct_per_step = [len(set(h[i] for h in histories)) for i in range(len(histories[0]))]
        return {'rule held at the end, by count of orders': dict(finals),
                'ledger rows at which the held rule differed between orders': sum(1 for d in distinct_per_step if d > 1),
                'most different rules held at one row': max(distinct_per_step)}
    reference_found = replay(building_addition.FoundWay(list(base_list)), rows)
    out['found way, the fixed list (reference)'] = {'held after each row (changes only)': _changes(reference_found)}
    histories = []
    for i in range(50):
        shuffled = list(base_list)
        random.Random(9000 + i).shuffle(shuffled)
        histories.append(replay(building_addition.FoundWay(shuffled), rows))
    out['found way, 50 random orders of the list'] = summarise(histories)
    out['found way, 50 random orders of the list: rules held at the end'] = sorted(set(h[-1] for h in histories))
    histories = []
    for i in range(50):
        r = random.Random(9500 + i)
        shuffled = sorted(base_list, key=lambda rule: (rule.number_of_terms(), r.random()))
        histories.append(replay(building_addition.FoundWay(shuffled), rows))
    out['found way, 50 orders keeping fewest terms first'] = summarise(histories)
    reference_built = replay(building_addition.BuiltWay(), rows)
    out['built way (reference)'] = {'held after each row (changes only)': _changes(reference_built)}
    histories = []
    for i in range(50):
        r = random.Random(9800 + i)
        order = list(language.AMOUNT_NAMES)
        r.shuffle(order)
        histories.append(replay(building_addition.BuiltWay(amount_order=order), rows, shuffle_rows_inside=r))
    out['built way, 50 orders of the rows and of the amounts'] = summarise(histories)
    histories = []
    for i in range(50):
        histories.append(replay(building_addition.FilterAllWay(), rows))
    out['filter-all way'] = summarise(histories)
    # arrival order of the history itself shuffled (secondary)
    arrival = {'built': Counter(), 'found': Counter()}
    for i in range(50):
        shuffled_rows = list(rows)
        random.Random(9900 + i).shuffle(shuffled_rows)
        arrival['built'][replay(building_addition.BuiltWay(), shuffled_rows)[-1]] += 1
        arrival['found'][replay(building_addition.FoundWay(list(base_list)), shuffled_rows)[-1]] += 1
    out['the history itself in 50 random orders: rule at the end'] = {k: dict(v) for k, v in arrival.items()}
    # agreement between the built way and the filter-all way, row by row
    filter_reference = replay(building_addition.FilterAllWay(), rows)
    out['rows where the built way and the filter-all way predict differently'] = sum(
        _held_set(a) != _held_set(b) for a, b in zip(reference_built, filter_reference))
    return out


def _held_set(text):
    return frozenset(text.replace('rivals: ', '').split('; '))


def _changes(history):
    changes = []
    previous = None
    for i, h in enumerate(history):
        if h != previous:
            changes.append({'after ledger row': i + 1, 'held': h})
            previous = h
    return changes


# ---------------------------------------------------------------- (f) same final frame
def section_f(built, none, schedule):
    rng = random.Random(TEST_SEED + 30)
    pairs = []
    while len(pairs) < 50:
        a = (rng.randint(0, 6), rng.randint(1, 5))
        b = (rng.randint(0, 6), rng.randint(1, 5))
        if sum(a) == sum(b):
            continue
        length = 20
        seed = rng.randint(0, 10 ** 6)
        sa = the_world.amounts_scene(random.Random(seed), a[0], a[1], 0, lift=False, total_frames=length,
                                     delay_before_group=rng.randint(1, 4), label='pair A')
        sb = the_world.amounts_scene(random.Random(seed + 1), b[0], b[1], 0, lift=False, total_frames=length,
                                     delay_before_group=rng.randint(1, 4), label='pair B')
        if sa is None or sb is None or sa.frames[-1] != sb.frames[-1] or len(sa.frames) != len(sb.frames):
            continue
        pairs.append((sa, sb))
    out = {'pairs': len(pairs), 'every pair the same length and the same final frame': True}
    for name, machine, wipe in (('built', built, False), ('four rules only', none, False), ('built, memory wiped at the last frame', built, True)):
        right, both = 0, 0
        for sa, sb in pairs:
            answers = []
            for s in (sa, sb):
                report = copy.deepcopy(machine).watch_scene(s.frames, answer_how_many_behind_at_the_end=True, wipe_memory_at_the_end=wipe)
                answers.append(report['answer: how many behind the screen'] == s.facts['true after'])
            right += sum(answers)
            both += all(answers)
        out[name] = {'answers right, of %d' % (2 * len(pairs)): right, 'pairs with both right': both}
    # a rival that reads only the frame count and the final frame gives both scenes of a pair one answer
    counted = Counter(r['counted after'] for r in built.ledger)
    constant_answer = counted.most_common(1)[0][0]
    right = sum((sa.facts['true after'] == constant_answer) + (sb.facts['true after'] == constant_answer) for sa, sb in pairs)
    out['clock-only rival (frame count and final frame), best possible'] = {
        'answers right at most, of %d (one answer per pair)' % (2 * len(pairs)): len(pairs),
        'answers right at most, of %d (every scene has the same length and final frame, so one answer for all)' % (2 * len(pairs)):
            Counter(s.facts['true after'] for pair in pairs for s in pair).most_common(1)[0][1]}
    out['clock-only rival, concrete: the most common amount in the ledger (%d)' % constant_answer] = {'answers right, of %d' % (2 * len(pairs)): right}
    return out


def main(output_folder):
    os.makedirs(output_folder, exist_ok=True)
    start = time.process_time()
    timings = {}
    schedule = the_world.building_schedule(BUILDING_SEED)
    seen_triples = triples_seen_while_building(schedule)

    t = time.process_time()
    a = section_a()
    timings['(a)'] = time.process_time() - t

    t = time.process_time()
    built = build_machine('built', schedule=schedule)
    found = build_machine('found', schedule=schedule)
    filter_all = build_machine('filter all', schedule=schedule)
    none = build_machine('none', schedule=schedule)
    timings['building'] = time.process_time() - t

    t = time.process_time()
    b = section_b({'four rules only': none, 'built': built, 'found': found}, seen_triples)
    timings['(b)'] = time.process_time() - t

    test_scenes = unseen_test_scenes()
    t = time.process_time()
    c = section_c(schedule, built, found, filter_all, none, test_scenes, seen_triples)
    timings['(c)'] = time.process_time() - t
    t = time.process_time()
    d = section_d(built, found, test_scenes, seen_triples, schedule)
    timings['(d)'] = time.process_time() - t
    t = time.process_time()
    e = section_e(built)
    timings['(e)'] = time.process_time() - t
    t = time.process_time()
    f = section_f(built, none, schedule)
    timings['(f)'] = time.process_time() - t
    timings['whole run, CPU seconds'] = time.process_time() - start

    summary = {'seeds': {'building': BUILDING_SEED, 'tests': TEST_SEED},
               'building schedule': {'scenes': len(schedule), 'kinds': dict(Counter(s.kind for s in schedule)),
                                     'amount triples seen while building': sorted(seen_triples)},
               'handed in': {k: v for k, v in built.handed_in.items()},
               '(a) the four rules alone': a, '(b) amounts tests of the infant studies\' kind': b,
               '(c) the building of addition': c, '(d) knock-outs': d, '(e) order shuffle': e,
               '(f) same final frame': f, 'CPU seconds': timings}
    with open(os.path.join(output_folder, 'summary.json'), 'w') as handle:
        json.dump(summary, handle, indent=1, default=str)
    with open(os.path.join(output_folder, 'raw ledger, built way.json'), 'w') as handle:
        json.dump(built.ledger, handle, indent=1, default=str)
    with open(os.path.join(output_folder, 'raw building log, built way.json'), 'w') as handle:
        json.dump(built.learner.log, handle, indent=1, default=str)
    print(json.dumps(timings, indent=1))


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else 'out')
