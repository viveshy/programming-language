"""
Operator precedence decides which operator goes first when a line has several.
From first to last:

    ┌───────┬──────────────────────┬───────────────────────────────────┐
    │ Order │ Operator             │ Meaning                           │
    ├───────┼──────────────────────┼───────────────────────────────────┤
    │ 1     │ ( )                  │ brackets                          │
    │ 2     │ **                   │ power                             │
    │ 3     │ -x                   │ a minus sign in front of a number │
    │ 4     │ *  /  //  %          │ multiply and divide               │
    │ 5     │ +  -                 │ add and subtract                  │
    │ 6     │ ==  !=  <  >  <=  >= │ comparisons                       │
    │ 7     │ not                  │ flips True and False              │
    │ 8     │ and                  │ both sides must be True           │
    │ 9     │ or                   │ one side is enough                │
    └───────┴──────────────────────┴───────────────────────────────────┘

Assignment (=, +=, ...) happens last, after the whole right side is worked out.

Why it matters: (a + b) % m and a + b % m give different answers, and Python
gives no error for the wrong one.

We will cover:
1. * / // % before + and -
2. Brackets go first
3. Same level: left to right
4. ** and the minus sign
5. Comparisons come after the maths
6. not, then and, then or
"""


# ┌────────────────────────────────────────────────────────────┐
# │ 1. * / // % BEFORE + AND -                                 │
# └────────────────────────────────────────────────────────────┘
# * / // % go before + and -, as in school maths.

assert 10 + 2 * 3 - 5 == 11  # 2 * 3 first: 10 + 6 - 5
assert 7 + 10 % 3 == 8  # 10 % 3 first: 7 + 1

# With more levels, follow the table: 2 ** 2 first, then 3 * 4 and 8 / 4,
# then + and -.

assert 5 + 3 * 2 ** 2 - 8 / 4 == 15.0


# ┌────────────────────────────────────────────────────────────┐
# │ 2. BRACKETS GO FIRST                                       │
# └────────────────────────────────────────────────────────────┘
# Whatever is inside ( ) is worked out first.

assert (10 + 2) * 3 == 36
assert 10 + 2 * 3 == 16


# ┌────────────────────────────────────────────────────────────┐
# │ 3. SAME LEVEL: LEFT TO RIGHT                               │
# └────────────────────────────────────────────────────────────┘
# Operators on the same level are worked out from left to right.

assert 10 - 4 - 3 == 3  # (10 - 4) - 3, not 10 - (4 - 3)
assert 100 // 10 % 10 == 0  # (100 // 10) % 10


# ┌────────────────────────────────────────────────────────────┐
# │ 4. ** AND THE MINUS SIGN                                   │
# └────────────────────────────────────────────────────────────┘
# ** goes before a minus sign in front, so -2 ** 2 is -(2 ** 2).

assert -2 ** 2 == -4

# ** is the one operator that goes right to left.

assert 2 ** 3 ** 2 == 512  # 2 ** (3 ** 2) = 2 ** 9
assert (2 ** 3) ** 2 == 64


# ┌────────────────────────────────────────────────────────────┐
# │ 5. COMPARISONS COME AFTER THE MATHS                        │
# └────────────────────────────────────────────────────────────┘
# Comparisons (04_conditionals/02_comparison_operators.py) go after all the
# maths, so both sides are worked out first.

assert 2 + 3 == 5  # (2 + 3) == 5
assert 2 * 3 > 5  # (2 * 3) > 5


# ┌────────────────────────────────────────────────────────────┐
# │ 6. NOT, THEN AND, THEN OR                                  │
# └────────────────────────────────────────────────────────────┘
# not, and and or (04_conditionals/04_logical_operators.py) come after the
# comparisons. Each has its own level: not first, then and, then or.

assert (not 1 == 2) is True  # not (1 == 2)
assert (not True and False) is False  # (not True) and False
assert (True or False and False) is True  # True or (False and False)


print('All checks passed.')
