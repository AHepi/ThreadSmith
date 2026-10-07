"""
What this file does, in plain words.

Rule 4 of the owner's machine (log S135): AMOUNTS.
Origin: HANDED IN by the builders (Claude, for the owner, S135); written outside
the machine, run inside it.

The rule in plain words: the amount in a region, or in a set of objects picked
out at one moment, is the number of distinct tracked objects in it, including
those held behind the screen through rule 3. An amount is held as a number the
machine can compare with another (equal, more, fewer). It is general: it does
not depend on colour, size or place.

What this rule does NOT do: it does not add, subtract or relate amounts. It
counts sets and compares two numbers. Nothing handed in to the machine
combines amounts.
"""

ORIGIN = ('HANDED IN', 'Rule 4, amounts: written by the builders (Claude, for the owner, S135) outside the '
          'machine and run inside it; it counts sets and compares two numbers; it does not combine amounts; '
          'the machine did not form it.')
PLAIN_WORDS = ('The amount in a region or in a set picked out at one moment is the number of distinct objects '
               'in it (behind the screen too, through rule 3); amounts are compared as equal, more or fewer.')


def amount_of_a_set(things):
    """The number of distinct things in a set (whatever their colour, size or place)."""
    return len(set(id(t) for t in things))


def amount_in_a_region(tracks, held_hidden, region, permanence_on):
    """The number of distinct objects in a rectangle: tracks seen inside it, and held hidden ones (rule 3) if permanence is on."""
    top, bottom, left, right = region
    seen_inside = [t for t in tracks if top <= t.centre[0] <= bottom and left <= t.centre[1] <= right]
    hidden_inside = list(held_hidden) if permanence_on else []
    # one set, counted once: the objects seen inside and the ones held behind the screen together
    return amount_of_a_set(seen_inside + hidden_inside)


def compare(first, second):
    """Equal, more or fewer: the first amount against the second."""
    if first == second:
        return 'equal'
    return 'more' if first > second else 'fewer'
