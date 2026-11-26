"""
An augmented assignment does an operation on a variable and stores the answer
back in the same variable.

    ┌────────────┬────────────┬───────────────────┐
    │ Short form │ Same as    │ Note              │
    ├────────────┼────────────┼───────────────────┤
    │ x += 3     │ x = x + 3  │                   │
    │ x -= 3     │ x = x - 3  │                   │
    │ x *= 3     │ x = x * 3  │                   │
    │ x **= 3    │ x = x ** 3 │                   │
    │ x /= 3     │ x = x / 3  │ x becomes a float │
    │ x //= 3    │ x = x // 3 │                   │
    │ x %= 3     │ x = x % 3  │                   │
    └────────────┴────────────┴───────────────────┘

Why it matters: a solution keeps updating a few variables, like a count, a
running total or a number losing its digits. This is the short way to write it.

We will cover:
1. += -= *= **=: update a number
2. /= and //=: the division rules still apply
3. %=: keep a number small
4. No ++ or -- in Python
"""


# ┌────────────────────────────────────────────────────────────┐
# │ 1. += -= *= **=: UPDATE A NUMBER                           │
# └────────────────────────────────────────────────────────────┘
# x += 5 means: work out x + 5, then store the answer back in x.

x = 10
x += 5
assert x == 15

x -= 3
assert x == 12

x *= 2
assert x == 24

x **= 2
assert x == 576  # 24 ** 2

# For a list, += changes that same list instead of making a new one
# (06_collections/03_shallow_and_deep_copy.py).


# ┌────────────────────────────────────────────────────────────┐
# │ 2. /= AND //=: THE DIVISION RULES STILL APPLY              │
# └────────────────────────────────────────────────────────────┘
# /= turns x into a float, like / always does.

x = 24
x /= 4
assert x == 6.0
assert type(x) is float

# //= keeps an integer an integer.

n = 24
n //= 5
assert n == 4
assert type(n) is int


# ┌────────────────────────────────────────────────────────────┐
# │ 3. %=: KEEP A NUMBER SMALL                                 │
# └────────────────────────────────────────────────────────────┘
# x %= m keeps only the remainder, so x ends up from 0 to m - 1 (for m > 0).

y = 17
y %= 5
assert y == 2


# ┌────────────────────────────────────────────────────────────┐
# │ 4. NO ++ OR -- IN PYTHON                                   │
# └────────────────────────────────────────────────────────────┘
# C++ and Java add 1 with x++. Python has no ++: write x += 1.

count = 0
count += 1
assert count == 1

# Python has no -- either: write x -= 1 to take 1 away.

count -= 1
assert count == 0


print('All checks passed.')
