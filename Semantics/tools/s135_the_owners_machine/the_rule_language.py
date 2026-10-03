"""
What this file does, in plain words.

The rule language of the owner's machine (log S135): the class of rules about
amounts the machine can hold. Origin: HANDED IN by the builders (it names the
class of what can be built: the theory's naming trap, S118's grade 2).

A rule in this language says:
    after = c0 + cB x before + cA x added + cT x taken away + cK x tracked
where 'before', 'added', 'taken away' and 'tracked' are amounts the machine
holds for a scene (rule 4, with rule 3), 'after' is the amount it expects
when the screen lifts, each of cB, cA, cT, cK is -1, 0 or +1, and c0 is one of
-2, -1, 0, +1, +2. That is 405 rules. They are sums and differences of held
amounts; comparisons (equal, more, fewer) are used to check a rule against
what is counted.

The language contains the machine's first expectation ("after = tracked",
which is rules 3 and 4 in use, handed in), the relation to be built ("after =
before + added - taken away"), and many others. The machine is never told
which one is right.

This file also holds THE FIXED LIST used by the found way (the control): all
405 rules in one fixed order: fewest terms first, then the smaller constant
(0, +1, -1, +2, -2), then the amounts in the order tracked, before, added,
taken away, with +1 before -1.
"""

import itertools

ORIGIN = ('HANDED IN', 'The rule language (sums and differences of held amounts, 405 rules): written by the '
          'builders (Claude, for the owner, S135); it names the class of what the machine can build.')

AMOUNT_NAMES = ('before', 'added', 'taken away', 'tracked')
CONSTANT_RANGE = (-2, -1, 0, 1, 2)
COEFFICIENT_RANGE = (-1, 0, 1)


class AmountRule:
    """One rule: a constant and one coefficient per held amount, with its origin record."""

    def __init__(self, constant, coefficients, origin=None, name=None):
        self.constant = constant
        self.coefficients = dict(coefficients)
        for amount_name in AMOUNT_NAMES:
            self.coefficients.setdefault(amount_name, 0)
        self.origin = origin or {}
        self.name = name

    def key(self):
        return (self.constant,) + tuple(self.coefficients[n] for n in AMOUNT_NAMES)

    def expected_after(self, held_amounts):
        """The amount this rule expects when the screen lifts; None if an amount it needs is not held."""
        total = self.constant
        for amount_name in AMOUNT_NAMES:
            coefficient = self.coefficients[amount_name]
            if coefficient == 0:
                continue
            value = held_amounts.get(amount_name)
            if value is None:
                return None
            total += coefficient * value
        return total

    def number_of_terms(self):
        return sum(1 for n in AMOUNT_NAMES if self.coefficients[n] != 0) + (1 if self.constant != 0 else 0)

    def in_words(self, order=None):
        parts = []
        for amount_name in (order or AMOUNT_NAMES):
            coefficient = self.coefficients[amount_name]
            if coefficient == 1:
                parts.append(('+', amount_name))
            elif coefficient == -1:
                parts.append(('-', amount_name))
        if self.constant:
            parts.append(('+' if self.constant > 0 else '-', str(abs(self.constant))))
        if not parts:
            return 'after = 0'
        text = ('' if parts[0][0] == '+' else '- ') + parts[0][1]
        for sign, word in parts[1:]:
            text += ' %s %s' % (sign, word)
        return 'after = ' + text

    def __repr__(self):
        return self.in_words()


def rule_from_key(key, origin=None):
    return AmountRule(key[0], dict(zip(AMOUNT_NAMES, key[1:])), origin=origin)


def the_first_expectation():
    """'after = tracked': what rules 3 and 4 give the machine before anything is built."""
    return AmountRule(0, {'tracked': 1}, origin={'origin': 'HANDED IN',
                                                 'how': 'rules 3 and 4 in use: the amount when the screen lifts is the number of objects tracked behind it'},
                      name='the first expectation (tracking)')


def all_rules_in_the_language():
    return [rule_from_key((c0,) + coefficients) for c0 in CONSTANT_RANGE
            for coefficients in itertools.product(COEFFICIENT_RANGE, repeat=len(AMOUNT_NAMES))]


def the_fixed_list():
    """All 405 rules in the found way's fixed order."""
    constant_order = {0: 0, 1: 1, -1: 2, 2: 3, -2: 4}
    list_order_of_amounts = ('tracked', 'before', 'added', 'taken away')
    coefficient_order = {1: 0, -1: 1, 0: 2}

    def place(rule):
        return (rule.number_of_terms(), constant_order[rule.constant],
                tuple(coefficient_order[rule.coefficients[n]] for n in list_order_of_amounts))
    return sorted(all_rules_in_the_language(), key=place)


def fits_every_row(rule, rows):
    return all(rule.expected_after(row['held amounts']) == row['counted after'] for row in rows)
