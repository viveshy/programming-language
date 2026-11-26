"""
Math functions round numbers, drop their sign and compare floats.

    ┌────────────────────┬────────────────────────────────────┬─────────────┐
    │ Function           │ What it gives                      │ Needs       │
    ├────────────────────┼────────────────────────────────────┼─────────────┤
    │ round(x)           │ the nearest integer                │ built in    │
    │ round(x, n)        │ x with n digits after the point    │ built in    │
    │ abs(x)             │ the distance from 0: drops a minus │ built in    │
    │ math.floor(x)      │ round down: largest integer <= x   │ import math │
    │ math.ceil(x)       │ round up: smallest integer >= x    │ import math │
    │ math.isclose(a, b) │ equal apart from a tiny error?     │ import math │
    └────────────────────┴────────────────────────────────────┴─────────────┘

Built-in functions are always there. The others live in the math module, a
file of extra functions. Load it once with import math, then call math.floor().

Why it matters: rounding up a division shows up in many counting problems,
and abs() in every distance.

We will cover:
1. round(): to the nearest integer
2. abs(): the distance from 0
3. math.floor() and math.ceil(): round down and up
4. math.isclose(): compare floats
"""

import math


# ┌────────────────────────────────────────────────────────────┐
# │ 1. ROUND(): TO THE NEAREST INTEGER                         │
# └────────────────────────────────────────────────────────────┘
# round(x) gives the nearest integer, as an int.

assert round(5.36) == 5
assert round(-8.34) == -8
assert type(round(5.36)) is int

# A second number keeps that many digits after the decimal point.

assert round(5.367, 2) == 5.37


# ┌────────────────────────────────────────────────────────────┐
# │ 2. ABS(): THE DISTANCE FROM 0                              │
# └────────────────────────────────────────────────────────────┘
# abs(x) drops the minus sign. An integer stays an integer.

assert abs(-8.34) == 8.34
assert abs(5.36) == 5.36
assert abs(-7) == 7


# ┌────────────────────────────────────────────────────────────┐
# │ 3. MATH.FLOOR() AND MATH.CEIL(): ROUND DOWN AND UP         │
# └────────────────────────────────────────────────────────────┘
# math.floor() rounds down, math.ceil() rounds up. Both give an integer.

assert math.floor(5.36) == 5
assert math.ceil(5.36) == 6
assert math.ceil(5.0) == 5  # no fraction part: it stays as it is

# With negative numbers, down is away from zero and up is towards it.

assert math.floor(-8.34) == -9  # int(-8.34) would give -8: it cuts towards 0
assert math.ceil(-8.34) == -8


# ┌────────────────────────────────────────────────────────────┐
# │ 4. MATH.ISCLOSE(): COMPARE FLOATS                          │
# └────────────────────────────────────────────────────────────┘
# Floats are often a tiny bit off (01_arithmetic_operators.py, section 7).
# math.isclose(a, b) is True when a and b differ by only a tiny amount.

assert math.isclose(0.1 + 0.2, 0.3)  # even though 0.1 + 0.2 != 0.3


print('All checks passed.')
