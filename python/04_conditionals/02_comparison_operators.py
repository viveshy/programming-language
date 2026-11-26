"""
A comparison asks a question about two values and gives True or False.

    ┌──────────┬───────────────────────┐
    │ Operator │ Meaning               │
    ├──────────┼───────────────────────┤
    │ ==       │ equal                 │
    │ !=       │ not equal             │
    │ <        │ less than             │
    │ >        │ greater than          │
    │ <=       │ less than or equal    │
    │ >=       │ greater than or equal │
    └──────────┴───────────────────────┘

Why it matters: every if, every loop condition and every bounds check is a
comparison.

We will cover:
1. == and !=: equal and not equal
2. <, >, <= and >=: which is bigger
3. A comparison is a bool: use it in an if, or keep it
4. Chained comparisons: b < a <= c
"""


# ┌────────────────────────────────────────────────────────────┐
# │ 1. == AND !=: EQUAL AND NOT EQUAL                          │
# └────────────────────────────────────────────────────────────┘
# == asks "are these equal?". != asks "are these different?".

a = 15
b = 10
c = 15

assert (a == c) is True
assert (a == b) is False
assert (a != b) is True

# An integer and a float are compared by value.

assert (1 == 1.0) is True


# ┌────────────────────────────────────────────────────────────┐
# │ 2. <, >, <= AND >=: WHICH IS BIGGER                        │
# └────────────────────────────────────────────────────────────┘
# < means "less than" and > means "greater than".
# <= and >= also say True when the two are equal.

assert (b < a) is True
assert (a > c) is False  # equal is not greater
assert (a >= c) is True  # equal counts


# ┌────────────────────────────────────────────────────────────┐
# │ 3. A COMPARISON IS A BOOL: USE IT IN AN IF, OR KEEP IT     │
# └────────────────────────────────────────────────────────────┘
# A comparison gives True or False, so it can go straight into an if.

if a > b:
    bigger = a
else:
    bigger = b

assert bigger == 15  # max(a, b) does the same (06_collections)

# You can also keep the answer in a variable and use it later.

age = 18
is_adult = age >= 18
assert is_adult is True


# ┌────────────────────────────────────────────────────────────┐
# │ 4. CHAINED COMPARISONS: B < A <= C                         │
# └────────────────────────────────────────────────────────────┘
# b < a <= c means: b < a, and also a <= c. Both must be True.
# ("and" joins two tests that must both be True: 04_logical_operators.py.)
# The middle value takes part in both tests.

assert (b < a <= c) is True  # 10 < 15, and 15 <= 15
assert (1 <= a <= 10) is False  # 15 is past 10


print('All checks passed.')
