"""
What this file does, in plain words.

The owner's machine (log S135). It sees only the grid, frame by frame, and runs
on its own with nobody steering. It has four general rules handed in by the
builders (recognise objects, displacement, object permanence, amounts), each a
separate module that can be switched off, and one way of forming a rule over
amounts from its own ledger (built, found, filter all, or none).

For each scene it:
  - recognises the objects in each frame (rule 1);
  - follows them from frame to frame and predicts their next place (rule 2);
  - holds what goes behind the screen and expects it to come out (rule 3);
  - counts sets and regions, and holds amounts (rule 4): before (on the stage
    when the screen came down), added (the set that went behind in one frame),
    taken away (the set that came out in one frame), tracked (individual
    objects held behind the screen);
  - when the screen lifts, predicts the amount from its held rule over amounts,
    counts what is there, logs a violation if they differ, writes a ledger row,
    and, if learning is on, lets its learner repair or keep its rule.
Its short-term state is cleared at the start of each scene; its long-term store
(the rules and the ledger) carries on.

Origin of this file: HANDED IN by the builders (Claude, for the owner, S135).
"""

import rule_1_recognise_objects as rule_1
import rule_2_displacement as rule_2
import rule_3_object_permanence as rule_3
import rule_4_amounts as rule_4
import building_addition
import the_rule_language as language

GRID_SIZE = 16


def _near_the_screen(outline, screen, margin=1):
    top, bottom, left, right = outline
    s_top, s_bottom, s_left, s_right = screen
    return top <= s_bottom + margin and bottom >= s_top - margin and left <= s_right + margin and right >= s_left - margin


def _inside(outline, screen):
    top, bottom, left, right = outline
    s_top, s_bottom, s_left, s_right = screen
    return s_top <= top and bottom <= s_bottom and s_left <= left and right <= s_right


class TheMachine:
    def __init__(self, way='built', rule_2_on=True, rule_3_on=True, learning_on=True, amount_order=None,
                 fixed_list=None, capacity=rule_3.CAPACITY):
        self.rule_2_on = rule_2_on
        self.rule_3_on = rule_3_on
        self.learning_on = learning_on
        self.capacity = capacity
        self.handed_in = {
            'rule 1, recognise objects': {'origin': rule_1.ORIGIN, 'in plain words': rule_1.PLAIN_WORDS, 'switched on': True},
            'rule 2, displacement': {'origin': rule_2.ORIGIN, 'in plain words': rule_2.PLAIN_WORDS, 'switched on': rule_2_on},
            'rule 3, object permanence': {'origin': rule_3.ORIGIN, 'in plain words': rule_3.PLAIN_WORDS, 'switched on': rule_3_on,
                                          'capacity': capacity},
            'rule 4, amounts': {'origin': rule_4.ORIGIN, 'in plain words': rule_4.PLAIN_WORDS, 'switched on': True},
            'the rule language': {'origin': language.ORIGIN},
        }
        if way == 'built':
            self.learner = building_addition.BuiltWay(amount_order=amount_order)
        elif way == 'found':
            self.learner = building_addition.FoundWay(fixed_list=fixed_list)
        elif way == 'filter all':
            self.learner = building_addition.FilterAllWay()
        else:
            self.learner = building_addition.FoundWay(fixed_list=[])  # holds the first expectation for ever
            self.learner.name = 'none'
        self.way = way
        self.ledger = []
        self.removed_rule = None

    # ---- the knock-outs -------------------------------------------------------------
    def remove_the_held_rule(self):
        """Knock-out: the rule over amounts is taken away; predictions go back to the first expectation (tracking)."""
        self.removed_rule = (self.learner.held_rule, getattr(self.learner, 'rivals', None), self.learner.state)
        self.learner.held_rule = language.the_first_expectation()
        if hasattr(self.learner, 'rivals'):
            self.learner.rivals = None
        self.learner.state = 'holding the first expectation'

    def restore_the_held_rule(self):
        held_rule, rivals, state = self.removed_rule
        self.learner.held_rule = held_rule
        if hasattr(self.learner, 'rivals'):
            self.learner.rivals = rivals
        self.learner.state = state
        self.removed_rule = None

    def sham_removal(self):
        """Sham: the held rule rewritten with its terms in another order and another name (content unchanged), and the oldest ten ledger rows deleted."""
        rule = self.learner.held_rule
        rewritten = language.AmountRule(rule.constant, dict(reversed(list(rule.coefficients.items()))),
                                        origin=dict(rule.origin, sham='rewritten with its terms reversed and renamed'),
                                        name='renamed by the sham')
        self.learner.held_rule = rewritten
        del self.ledger[:10]

    # ---- watching one scene -----------------------------------------------------------
    def watch_scene(self, frames, label='', answer_how_many_behind_at_the_end=False, wipe_memory_at_the_end=False):
        tracks, held_hidden = [], []
        next_track = [1]
        violations, per_frame = [], []
        screen_before = None
        last_screen = None
        held = {'before': None, 'added': 0, 'taken away': 0}
        sets_in, sets_out = 0, 0
        lift_report = None

        def new_track(seen, frame_index, came_out=False):
            t = rule_2.Track(next_track[0], seen, frame_index)
            t.came_from_behind_the_screen = came_out
            next_track[0] += 1
            tracks.append(t)
            return t

        for frame_index, frame in enumerate(frames):
            seen = rule_1.recognise_objects(frame)
            screen_now = rule_1.find_the_screen(frame)
            if screen_now:
                last_screen = screen_now
            prediction_records = []
            if frame_index == 0:
                for o in seen:
                    new_track(o, frame_index)
                screen_before = screen_now
                per_frame.append({'tracks': [(t.number, t.cells) for t in tracks], 'predictions': [],
                                  'amount in the screen region': None})
                continue

            if self.rule_2_on:
                pairs, lost, new_objects = rule_2.match_objects_to_tracks(tracks, seen)
                for track, o in pairs:
                    move, error, violated = rule_2.move_track(track, o)
                    prediction_records.append((track.number, error, violated))
                    if violated:
                        violations.append((frame_index, 'displacement: not where predicted', {'colour': track.colour, 'error in cells': error}))
                tracks = [t for t in tracks if t not in lost]
            else:
                # without displacement nothing links one frame to the next: last frame's objects are gone, these are new
                lost, new_objects = list(tracks), list(seen)
                tracks = []

            # the screen comes down this frame: what it covers is behind it
            if screen_now and not screen_before:
                covered = [t for t in lost if _inside(t.outline, screen_now)]
                held['before'] = rule_4.amount_of_a_set(covered) if self.rule_3_on else 0
                if self.rule_3_on:
                    for t in covered:
                        dropped = rule_3.hide(held_hidden, t, frame_index, screen_now, self.capacity)
                        if dropped is not None:
                            violations.append((frame_index, 'note: one held object dropped (capacity)', {'colour': dropped.colour}))
                lost = [t for t in lost if t not in covered]
            # objects that went out of sight at the screen (the screen already down)
            if screen_now and screen_before and self.rule_2_on:
                went_behind = [t for t in lost if _near_the_screen(t.outline, screen_now)]
                if went_behind:
                    sets_in += 1
                    held['added'] = rule_4.amount_of_a_set(went_behind) if sets_in == 1 else 'more than one set'
                    if self.rule_3_on:
                        for t in went_behind:
                            t.outline = (t.outline[0] + t.last_move[0], t.outline[1] + t.last_move[0],
                                         t.outline[2] + t.last_move[1], t.outline[3] + t.last_move[1])
                            dropped = rule_3.hide(held_hidden, t, frame_index, screen_now, self.capacity)
                            if dropped is not None:
                                violations.append((frame_index, 'note: one held object dropped (capacity)', {'colour': dropped.colour}))
                lost = [t for t in lost if t not in went_behind]
            # the rest left the world at an edge, or vanished in plain sight
            if self.rule_2_on:
                for t in lost:
                    if not (rule_2.predicted_to_leave_the_world(t) or rule_2.at_an_edge_of_the_world(t.outline)):
                        violations.append((frame_index, 'displacement: vanished in plain sight', {'colour': t.colour}))

            # the screen lifts this frame: count what is revealed, check the prediction
            if screen_before and not screen_now:
                revealed = [o for o in new_objects if _inside((o.top, o.bottom, o.left, o.right), screen_before)]
                counted_after = rule_4.amount_of_a_set(revealed)
                held_amounts = dict(held)
                held_amounts['tracked'] = rule_4.amount_of_a_set(held_hidden) if self.rule_3_on else 0
                prediction = self.learner.predict(held_amounts)
                if self.rule_3_on:
                    for v in rule_3.check_after_the_lift(held_hidden, revealed):
                        violations.append((frame_index, 'permanence: ' + v[0], v[1]))
                if prediction == 'undetermined' or prediction is None:
                    verdict = 'no single prediction'
                else:
                    verdict = rule_4.compare(counted_after, prediction)
                    if verdict != 'equal':
                        violations.append((frame_index, 'amount: %s than expected' % verdict,
                                           {'expected': prediction, 'counted': counted_after}))
                row = {'scene': label, 'held amounts': held_amounts, 'counted after': counted_after,
                       'prediction': prediction, 'verdict': verdict, 'held rule': self.current_rule_in_words()}
                self.ledger.append(row)
                lift_report = row
                if self.learning_on:
                    usable_rows = [r for r in self.ledger if building_addition.usable(r)]
                    self.learner.learn_from_row(row, usable_rows, len(self.ledger))
                held_hidden = []
                for o in revealed:
                    new_track(o, frame_index)
                new_objects = [o for o in new_objects if o not in revealed]

            # objects that came out from behind the screen
            if screen_now and screen_before and self.rule_2_on:
                came_out = [o for o in new_objects if _near_the_screen((o.top, o.bottom, o.left, o.right), screen_now)]
                if came_out:
                    sets_out += 1
                    held['taken away'] = rule_4.amount_of_a_set(came_out) if sets_out == 1 else 'more than one set'
                    for o in came_out:
                        if self.rule_3_on:
                            had_any = bool(held_hidden)
                            match = rule_3.come_out(held_hidden, o)
                            if match is None:
                                violations.append((frame_index, 'permanence: a different one came out' if had_any else
                                                   'permanence: one came out that was not held', {'colour': o.colour}))
                        new_track(o, frame_index, came_out=True)
                new_objects = [o for o in new_objects if o not in came_out]
            for o in new_objects:
                if self.rule_2_on and not rule_2.at_an_edge_of_the_world((o.top, o.bottom, o.left, o.right)):
                    violations.append((frame_index, 'displacement: appeared from nowhere', {'colour': o.colour}))
                new_track(o, frame_index)

            if self.rule_3_on:
                for v in rule_3.step_hidden_objects(held_hidden, frame_index):
                    violations.append((frame_index, 'permanence: ' + v[0], v[1]))
            if screen_now:
                amount_in_region = rule_4.amount_in_a_region(tracks, held_hidden, screen_now, self.rule_3_on)
            else:
                amount_in_region = None
            per_frame.append({'tracks': [(t.number, t.cells) for t in tracks], 'predictions': prediction_records,
                              'amount in the screen region': amount_in_region})
            screen_before = screen_now

        report = {'label': label, 'violations': violations, 'per frame': per_frame, 'lift': lift_report}
        if answer_how_many_behind_at_the_end:
            held_amounts = dict(held)
            held_amounts['tracked'] = rule_4.amount_of_a_set(held_hidden) if self.rule_3_on else 0
            if wipe_memory_at_the_end:
                held_amounts = {'before': None, 'added': None, 'taken away': None, 'tracked': 0}
            report['answer: how many behind the screen'] = self.learner.predict(held_amounts)
            report['held amounts at the end'] = held_amounts
        return report

    def current_rule_in_words(self):
        rivals = getattr(self.learner, 'rivals', None)
        if rivals:
            return 'rivals: ' + '; '.join(language.rule_from_key(k).in_words() for k in sorted(rivals))
        return self.learner.held_rule.in_words() if self.learner.held_rule else 'nothing'
