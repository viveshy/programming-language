"""
The following arithmetic operations are covered here:
1. Addition: +
2. Subtraction: -
3. Multiplication: *
4. Division: /, //, and %
   - / => quotient with remainder (always gives a float)
   - // => only quotient (rounded down)
   - % => remainder
5. Power: **

Floats are stored in binary and are often a tiny bit off (section 6), so float
results here are checked with round(value, digits) instead of an exact ==.
"""

# Define integer and float variables
int_num1 = 10
int_num2 = 3
float_num1 = 10.33
float_num2 = 3.5

# 1. ADDITION
# _________________
assert int_num1 + int_num2 == 13  # int + int = int
assert round(float_num1 + float_num2, 2) == 13.83  # float + float = float
assert round(int_num1 + float_num1, 2) == 20.33  # int + float = float
assert type(int_num1 + float_num1) is float

# 2. SUBTRACTION
# _________________
assert int_num1 - int_num2 == 7
assert round(float_num1 - float_num2, 2) == 6.83
assert round(int_num1 - float_num1, 2) == -0.33  # the raw result is -0.33000000000000007

# 3. MULTIPLICATION
# _________________
assert int_num1 * int_num2 == 30
assert round(float_num1 * float_num2, 3) == 36.155
assert round(int_num1 * float_num1, 1) == 103.3

# 4. DIVISION
# _________________
# / always gives a float, even when the division is exact
assert int_num1 / 2 == 5.0
assert type(int_num1 / 2) is float
assert round(int_num1 / int_num2, 4) == 3.3333
assert round(float_num1 / float_num2, 4) == 2.9514
assert round(int_num1 / float_num1, 4) == 0.9681

# // keeps only the quotient: int // int = int, anything with a float gives a float
assert int_num1 // int_num2 == 3
assert type(int_num1 // int_num2) is int
assert float_num1 // float_num2 == 2.0
assert int_num1 // float_num1 == 0.0

# % gives the remainder
assert int_num1 % int_num2 == 1
assert round(float_num1 % float_num2, 2) == 3.33
assert int_num1 % float_num1 == 10.0

# With negative numbers, // rounds DOWN (towards minus infinity), not towards zero,
# and % takes the sign of the right-hand number.
assert -7 // 2 == -4  # -3.5 rounded down is -4
assert -7 % 2 == 1  # because (-4 * 2) + 1 == -7
assert 7 // -2 == -4

# 5. POWER
# _________________
assert int_num1 ** int_num2 == 1000
assert round(float_num1 ** float_num2, 2) == 3542.84
assert round(int_num1 ** float_num1) == 21379620895

# Python ints never overflow: they grow as big as needed
assert 2 ** 100 == 1267650600228229401496703205376

# 6. FLOATS ARE NOT EXACT
# _________________
# 0.1 and 0.2 cannot be stored exactly in binary, so their sum is a tiny bit off
assert 0.1 + 0.2 != 0.3
assert round(0.1 + 0.2, 2) == 0.3

print('All checks passed.')
