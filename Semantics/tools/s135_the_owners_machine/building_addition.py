"""
What this file does, in plain words.

How the owner's machine forms a rule over amounts from its own ledger (log
S135). Three ways, each a learner the machine can be given:

THE BUILT WAY (the machine's repair). It starts holding its first expectation,
"after = tracked" (rules 3 and 4 in use, handed in). When that expectation
fails on a scene (a recognized difficulty: its claimed aim, to predict the
amount when the screen lifts, has failed), it:
  1. holds the old expectation as the target of the repair, with every ledger
     row: those it got right (to be kept right) and those it got wrong (to be
     put right);
  2. computes the failure's content: on every row, the error of the old
     expectation, "counted after minus tracked";
  3. assembles a correction from it: solves exactly (fractions, Gaussian
     elimination) for the coefficients that make "correction = c0 + cB x before
     + cA x added + cT x taken away + cK x tracked" equal the error on EVERY row
     seen; the solution is a set (a fixed part and free directions the rows
     leave open); every member inside the language's bounds is a rival repair;
     the new rule is "after = tracked + correction";
  4. if one rule is left, holds it (origin BUILT, naming the failures that forced
     it); if several, holds them all as rivals, predicts where they agree and
     says "undetermined" where they disagree, and narrows them with each new
     row; if none, logs that no rule in the language fits and keeps the old one.
It never consults a list of rules: the set is computed from the rows.

THE FOUND WAY (the control). The 405 rules in a fixed order (the_rule_language.
the_fixed_list); at the first failure, and whenever its held rule fails again,
it takes the first rule in the list that fits every row (origin FOUND, with its
place in the list).

THE FILTER-ALL WAY (a second control). Keeps every one of the 405 rules that fits
every row, and commits when one is left. Its outputs equal the built way's by
construction of the mathematics; it is here to show that outputs alone cannot
tell building from an exhaustive filter (the theory's Argument 9): only the
trace can.

Origin of this file: HANDED IN by the builders (Claude, for the owner, S135).
"""

from fractions import Fraction
import itertools

import the_rule_language as language


def usable(row):
    return all(isinstance(row['held amounts'].get(n), int) for n in language.AMOUNT_NAMES) and \
        isinstance(row['counted after'], int)


def _reduced_row_echelon(matrix):
    """Exact Gaussian elimination on a list of rows of Fractions (the last column is the right-hand side).
    Returns (reduced rows, pivot columns)."""
    rows = [list(r) for r in matrix]
    number_of_unknowns = len(rows[0]) - 1 if rows else 0
    pivot_columns = []
    pivot_row = 0
    for column in range(number_of_unknowns):
        chosen = None
        for r in range(pivot_row, len(rows)):
            if rows[r][column] != 0:
                chosen = r
                break
        if chosen is None:
            continue
        rows[pivot_row], rows[chosen] = rows[chosen], rows[pivot_row]
        pivot_value = rows[pivot_row][column]
        rows[pivot_row] = [v / pivot_value for v in rows[pivot_row]]
        for r in range(len(rows)):
            if r != pivot_row and rows[r][column] != 0:
                factor = rows[r][column]
                rows[r] = [a - factor * b for a, b in zip(rows[r], rows[pivot_row])]
        pivot_columns.append(column)
        pivot_row += 1
        if pivot_row == len(rows):
            break
    return rows, pivot_columns


def solve_for_all_fitting_repairs(rows, old_rule, amount_order=None):
    """
    The built way's step 2 and 3: from the rows, the set of every rule in the language that equals
    'old rule + correction' and fits every row. `amount_order` only changes the order of the unknowns
    in the elimination (for the order-shuffle check). Returns (set of rule keys, a trace dictionary).
    """
    amount_order = list(amount_order or language.AMOUNT_NAMES)
    unknown_names = ['constant'] + amount_order
    old_coefficient = {'constant': old_rule.constant}
    old_coefficient.update(old_rule.coefficients)
    bounds = {'constant': language.CONSTANT_RANGE}
    for n in language.AMOUNT_NAMES:
        bounds[n] = language.COEFFICIENT_RANGE
    # correction bounds: the final rule must stay inside the language
    correction_bounds = {n: [v - old_coefficient[n] for v in bounds[n]] for n in unknown_names}

    matrix, errors = [], []
    for row in rows:
        held = row['held amounts']
        error = row['counted after'] - old_rule.expected_after(held)
        errors.append(error)
        matrix.append([Fraction(1)] + [Fraction(held[n]) for n in amount_order] + [Fraction(error)])
    trace = {'rows used': len(rows), 'errors of the old expectation': errors,
             'rows the old expectation got wrong': sum(1 for e in errors if e != 0)}
    if not matrix:
        return set(), dict(trace, outcome='no rows')
    reduced, pivots = _reduced_row_echelon(matrix)
    number_of_unknowns = len(unknown_names)
    for r in reduced:
        if all(v == 0 for v in r[:number_of_unknowns]) and r[number_of_unknowns] != 0:
            return set(), dict(trace, outcome='no relation in the language fits every row (the rows contradict one another)',
                               rank=len(pivots))
    free = [c for c in range(number_of_unknowns) if c not in pivots]
    trace['rank'] = len(pivots)
    trace['free directions left open by the rows'] = [unknown_names[c] for c in free]
    found = set()
    for free_values in itertools.product(*[correction_bounds[unknown_names[c]] for c in free]):
        solution = [None] * number_of_unknowns
        for c, v in zip(free, free_values):
            solution[c] = Fraction(v)
        good = True
        for pivot_index, pivot_column in enumerate(pivots):
            r = reduced[pivot_index]
            value = r[number_of_unknowns] - sum(r[c] * solution[c] for c in free)
            if value.denominator != 1 or int(value) not in correction_bounds[unknown_names[pivot_column]]:
                good = False
                break
            solution[pivot_column] = value
        if not good:
            continue
        final = {name: int(solution[i]) + old_coefficient[name] for i, name in enumerate(unknown_names)}
        found.add((final['constant'],) + tuple(final[n] for n in language.AMOUNT_NAMES))
    trace['outcome'] = 'one rule left' if len(found) == 1 else ('rivals left' if found else 'no rule inside the language bounds fits')
    trace['rules left'] = sorted(found)
    return found, trace


class BuiltWay:
    """The machine's repair: the old expectation held as the target, the correction computed from the failures."""

    name = 'built'

    def __init__(self, amount_order=None):
        self.first_expectation = language.the_first_expectation()
        self.held_rule = self.first_expectation
        self.rivals = None
        self.state = 'holding the first expectation'
        self.amount_order = amount_order
        self.failures = []
        self.log = []

    def predict(self, held_amounts):
        if self.rivals is not None:
            values = {language.rule_from_key(k).expected_after(held_amounts) for k in self.rivals}
            if len(values) == 1:
                return values.pop()
            return 'undetermined'
        return self.held_rule.expected_after(held_amounts) if self.held_rule is not None else None

    def _repair(self, rows, row_number, reason):
        rule_set, trace = solve_for_all_fitting_repairs(rows, self.first_expectation, self.amount_order)
        rivals_before = len(self.rivals) if self.rivals is not None else (1 if self.held_rule else 0)
        entry = {'row number': row_number, 'reason': reason, 'rivals before': rivals_before,
                 'rivals after': len(rule_set), 'trace': trace}
        if len(rule_set) == 1:
            key = next(iter(rule_set))
            first_time = self.state != 'holding a built rule'
            self.held_rule = language.rule_from_key(key, origin={
                'origin': 'BUILT',
                'how': 'assembled by the machine as a repair of its first expectation (after = tracked): the '
                       'correction computed by exact elimination from the errors of that expectation on every '
                       'ledger row, one rule left inside the declared language',
                'failures that drove it': list(self.failures),
                'formed at ledger row': row_number,
                'rows checked': len(rows),
                'the class it was built in': 'HANDED IN: sums and differences of held amounts (405 rules), by the builders',
            })
            self.held_rule.name = 'the built rule over amounts'
            self.rivals = None
            self.state = 'holding a built rule'
            entry['held now'] = self.held_rule.in_words()
            entry['first time one rule was left'] = first_time
        elif len(rule_set) > 1:
            self.rivals = set(rule_set)
            self.state = 'holding rivals'
            entry['held now'] = ['%s' % language.rule_from_key(k).in_words() for k in sorted(rule_set)]
        else:
            # no rule in the language fits every row: keep the old expectation and try again at the next failure
            if self.state == 'holding rivals':
                self.rivals = None
                self.held_rule = self.first_expectation
                self.state = 'holding the first expectation'
            entry['held now'] = 'no rule in the language fits; kept: ' + (self.held_rule.in_words() if self.held_rule else 'nothing')
        self.log.append(entry)

    def learn_from_row(self, row, usable_rows, row_number):
        if not usable(row):
            return
        if self.state == 'holding the first expectation':
            if self.first_expectation.expected_after(row['held amounts']) == row['counted after']:
                return
            self.failures.append(row_number)
            self._repair(usable_rows, row_number, 'recognized difficulty: the first expectation failed')
        elif self.state == 'holding rivals':
            if self.first_expectation.expected_after(row['held amounts']) != row['counted after']:
                self.failures.append(row_number)
            self._repair(usable_rows, row_number, 'a new row while holding rivals')
        elif self.state == 'holding a built rule':
            if self.held_rule.expected_after(row['held amounts']) != row['counted after']:
                self.failures.append(row_number)
                self._repair(usable_rows, row_number, 'the built rule failed')


class FoundWay:
    """The control: the first rule in a fixed list that fits every row."""

    name = 'found'

    def __init__(self, fixed_list=None):
        self.list = fixed_list if fixed_list is not None else language.the_fixed_list()
        self.held_rule = language.the_first_expectation()
        self.failures = []
        self.log = []
        self.state = 'holding the first expectation'

    def predict(self, held_amounts):
        return self.held_rule.expected_after(held_amounts) if self.held_rule is not None else None

    def learn_from_row(self, row, usable_rows, row_number):
        if not usable(row):
            return
        if self.held_rule.expected_after(row['held amounts']) == row['counted after']:
            return
        self.failures.append(row_number)
        for place, rule in enumerate(self.list):
            if language.fits_every_row(rule, usable_rows):
                self.held_rule = language.rule_from_key(rule.key(), origin={
                    'origin': 'FOUND',
                    'how': 'the first rule in the builders\' fixed list that fits every ledger row',
                    'place in the list': place + 1,
                    'failures that triggered the search': list(self.failures),
                    'formed at ledger row': row_number,
                })
                self.held_rule.name = 'the found rule over amounts'
                self.state = 'holding a found rule'
                self.log.append({'row number': row_number, 'held now': self.held_rule.in_words(), 'place in the list': place + 1,
                                 'rules in the list that fit every row': sum(1 for r in self.list if language.fits_every_row(r, usable_rows))})
                return
        self.log.append({'row number': row_number, 'held now': 'unchanged (nothing in the list fits)'})


class FilterAllWay:
    """The second control: keep every one of the 405 rules that fits every row; commit when one is left."""

    name = 'filter all'

    def __init__(self):
        self.held_rule = language.the_first_expectation()
        self.rivals = None
        self.failures = []
        self.log = []
        self.state = 'holding the first expectation'

    def predict(self, held_amounts):
        if self.rivals is not None:
            values = {language.rule_from_key(k).expected_after(held_amounts) for k in self.rivals}
            return values.pop() if len(values) == 1 else 'undetermined'
        return self.held_rule.expected_after(held_amounts)

    def learn_from_row(self, row, usable_rows, row_number):
        if not usable(row):
            return
        if self.state == 'holding the first expectation' and self.held_rule.expected_after(row['held amounts']) == row['counted after']:
            return
        if self.state == 'holding one rule' and self.held_rule.expected_after(row['held amounts']) == row['counted after']:
            return
        self.failures.append(row_number)
        keys = {r.key() for r in language.all_rules_in_the_language() if language.fits_every_row(r, usable_rows)}
        if len(keys) == 1:
            self.held_rule = language.rule_from_key(next(iter(keys)), origin={'origin': 'FOUND (filter all)'})
            self.rivals = None
            self.state = 'holding one rule'
        elif keys:
            self.rivals = keys
            self.state = 'holding rivals'
        self.log.append({'row number': row_number, 'rules left': len(keys)})
