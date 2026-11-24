"""
In this section, we will learn about the following Math functions and methods:

Functions:
    - round(x)    : Rounds a number to the nearest integer.
    - abs(x)      : Returns the absolute value of a number.

Methods:
    - math.floor(x)   : Returns the largest integer less than or equal to x.
    - math.ceil(x)    : Returns the smallest integer greater than or equal to x.
    - math.isclose(a, b) : Checks whether two floats are equal apart from a tiny error.

Note: Math methods are imported from the module 'math'.
"""

import math

# Define positive and negative numbers
positive_num = 5.36
negative_num = -8.34

# 1. ROUND
# __________________
assert round(positive_num) == 5
assert round(negative_num) == -8

# A second argument keeps that many digits after the decimal point
assert round(5.367, 2) == 5.37

# Exact halves go to the EVEN neighbour, not always up
assert round(2.5) == 2
assert round(3.5) == 4
assert round(-2.5) == -2

# 2.675 is stored as 2.67499999..., so it rounds down
assert round(2.675, 2) == 2.67

# 2. ABS
# __________________
assert abs(positive_num) == 5.36
assert abs(negative_num) == 8.34

# 3. CEIL AND FLOOR
# __________________
# ceil goes up to the next whole number, floor goes down
assert math.ceil(positive_num) == 6
assert math.ceil(negative_num) == -8  # "up" from -8.34 is -8
assert math.floor(positive_num) == 5
assert math.floor(negative_num) == -9  # "down" from -8.34 is -9

# 4. ISCLOSE
# __________________
# The safe way to compare floats (see 01_arithmetic_operators.py, section 6)
assert math.isclose(0.1 + 0.2, 0.3)

print('All checks passed.')
