"""
Logical operators join or flip True and False.

    ┌──────────┬────────────────────────────────────────┐
    │ Operator │ What it gives                          │
    ├──────────┼────────────────────────────────────────┤
    │ and      │ True only when both sides are True     │
    │ or       │ True when at least one side is True    │
    │ not      │ flips True to False, and False to True │
    └──────────┴────────────────────────────────────────┘

Why it matters: conditions often have two parts, like "inside the string and
equal to x". In DSA code, and also stops a crash before it happens.

We will cover:
1. and: both sides must be True
2. or: at least one side must be True
3. not: flip True and False
4. The order: not, then and, then or
5. Short-circuiting: the right side may never run
6. The value that and / or give back
"""


# ┌────────────────────────────────────────────────────────────┐
# │ 1. AND: BOTH SIDES MUST BE TRUE                            │
# └────────────────────────────────────────────────────────────┘
# a and b is True only when a is True and b is True.

assert (True and True) is True
assert (True and False) is False
assert (False and False) is False

x = 5
y = 10

assert (x > 0 and y > 0) is True  # both are positive


# ┌────────────────────────────────────────────────────────────┐
# │ 2. OR: AT LEAST ONE SIDE MUST BE TRUE                      │
# └────────────────────────────────────────────────────────────┘
# a or b is True when a is True, or b is True, or both.
# It is False only when both sides are False.

assert (True or False) is True
assert (True or True) is True  # both True counts too
assert (False or False) is False

assert (x < 0 or y < 0) is False  # neither is negative


# ┌────────────────────────────────────────────────────────────┐
# │ 3. NOT: FLIP TRUE AND FALSE                                │
# └────────────────────────────────────────────────────────────┘
# not takes one value and flips it.

assert (not True) is False
assert (not False) is True
assert (not (x > 0)) is False  # x is positive, so "not positive" is False

# For "is not inside", write x not in s. It reads better than not (x in s).

assert ('z' not in 'apple') is True


# ┌────────────────────────────────────────────────────────────┐
# │ 4. THE ORDER: NOT, THEN AND, THEN OR                       │
# └────────────────────────────────────────────────────────────┘
# Comparisons like > and == go first. Then not, then and, then or.
# Brackets go before everything, so add them when in doubt.

assert (not True and False) is False  # (not True) and False
assert (True or False and False) is True  # True or (False and False)
assert ((True or False) and False) is False  # brackets: or first

# A leap year divides by 4 but not by 100, or it divides by 400.
# and goes first, so this needs no brackets:

year = 1900
is_leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
assert is_leap is False  # 1900 divides by 100, but not by 400


# ┌────────────────────────────────────────────────────────────┐
# │ 5. SHORT-CIRCUITING: THE RIGHT SIDE MAY NEVER RUN          │
# └────────────────────────────────────────────────────────────┘
# Python works out the left side first, and stops once it knows the answer:
# - and stops at the first False: False and anything is False
# - or stops at the first True: True or anything is True
# Then the right side never runs.

# 1 / 0 would stop the program with a ZeroDivisionError. Here it never runs:

assert (False and 1 / 0) is False
assert (True or 1 / 0) is True

# This makes a bounds check safe. s[3] is past the end of 'abc' (IndexError),
# but i < len(s) is False, so s[i] is never looked at.

s = 'abc'
i = 3

assert (i < len(s) and s[i] == 'c') is False


# ┌────────────────────────────────────────────────────────────┐
# │ 6. THE VALUE THAT AND / OR GIVE BACK                       │
# └────────────────────────────────────────────────────────────┘
# and and or give back one of their two values, not always True or False:
# - a or b    gives a if a counts as True, otherwise b
# - a and b   gives a if a counts as False, otherwise b
# 0 and '' count as False (03_type_conversion.py; more in 05_falsy.py).

assert (0 or 5) == 5
assert ('' or 'default') == 'default'
assert ('Ada' or 'default') == 'Ada'

assert (3 and 5) == 5
assert (0 and 5) == 0


print('All checks passed.')
