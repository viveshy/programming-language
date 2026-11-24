"""
Augmented assignment operators are a shorthand way to perform a binary operation and assign the result back to one of the operands.

For numbers, each one is shorthand for the longer form:
    - Addition (+=): x += y is the same as x = x + y
    - Subtraction (-=): x -= y is the same as x = x - y
    - Multiplication (*=): x *= y is the same as x = x * y
    - Division (/=): x /= y is the same as x = x / y
    - Floor division (//=): x //= y is the same as x = x // y
    - Modulus (%=): x %= y is the same as x = x % y

(For a list, += changes the list in place instead: see
06_collections/03_shallow_and_deep_copy.py.)
"""

x = 10

# Addition (+=)
x += 5  # equivalent to x = x + 5
assert x == 15

# Subtraction (-=)
x -= 3  # equivalent to x = x - 3
assert x == 12

# Multiplication (*=)
x *= 2  # equivalent to x = x * 2
assert x == 24

# Division (/=) turns x into a float, like / always does
x /= 4  # equivalent to x = x / 4
assert x == 6.0
assert type(x) is float

# Floor division (//=) keeps an int an int
n = 24
n //= 5  # equivalent to n = n // 5
assert n == 4
assert type(n) is int

# Modulus (%=)
y = 17
y %= 5  # equivalent to y = y % 5
assert y == 2

print('All checks passed.')
