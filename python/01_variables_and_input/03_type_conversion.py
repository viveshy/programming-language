"""
Type conversion turns a value of one type into another.

    ┌──────────┬─────────────────────────────────────────────────────┐
    │ Function │ What it does                                        │
    ├──────────┼─────────────────────────────────────────────────────┤
    │ int()    │ to an integer: ..., -2, -1, 0, 1, 2, ...            │
    │ float()  │ to a float: a number with a decimal point, like 2.5 │
    │ str()    │ to a string (text)                                  │
    │ bool()   │ to True or False                                    │
    └──────────┴─────────────────────────────────────────────────────┘

Why it matters: input() always gives you a string, and so does a contest judge.
To do maths with it, convert it to a number first.

We will cover:
1. str -> int and float
2. float -> int: cutting off the decimal part
3. is_integer(): does a float have a fraction part?
4. Big numbers: where a float loses digits
5. Anything -> str
6. bool, and True and False as numbers
"""


# ┌────────────────────────────────────────────────────────────┐
# │ 1. STR -> INT AND FLOAT                                    │
# └────────────────────────────────────────────────────────────┘
# A string of digits is still text, so + joins it. int() turns it into a number.

birth_year = '1990'  # what input() gives when the user types 1990

assert birth_year + '10' == '199010'  # text: + joins
assert int(birth_year) + 10 == 2000  # number: + adds

# Integers can be negative (whole numbers are only 0, 1, 2, ...).
# Spaces and a newline around the digits are ignored.

assert int('-42') == -42
assert int(' 42\n') == 42

# float() reads a number with a decimal point.

assert float('2.5') == 2.5
assert float('3') == 3.0


# ┌────────────────────────────────────────────────────────────┐
# │ 2. FLOAT -> INT: CUTTING OFF THE DECIMAL PART              │
# └────────────────────────────────────────────────────────────┘
# int() cuts off the decimal part. It does NOT round.

assert int(3.99) == 3
assert int(-3.99) == -3  # cuts towards zero: -3, not -4

# To round to the nearest integer, use round() (more in 04_math_functions.py).

assert round(3.99) == 4

# The other way, int -> float, always works. Mixing the two gives a float.

assert float(10) == 10.0
assert 1 + 2.0 == 3.0


# ┌────────────────────────────────────────────────────────────┐
# │ 3. IS_INTEGER(): DOES A FLOAT HAVE A FRACTION PART?        │
# └────────────────────────────────────────────────────────────┘
# x.is_integer() asks: is the part after the decimal point zero?
# It is a method of a float: a function you call with a dot after the value.
# It only answers the question. It converts nothing.

exact = 10 / 5  # / always gives a float: 2.0
uneven = 10 / 4  # 2.5

assert exact.is_integer() is True
assert uneven.is_integer() is False

# Use it before int() when losing the fraction would be a bug:
# int(uneven) would quietly turn 2.5 into 2.


# ┌────────────────────────────────────────────────────────────┐
# │ 4. BIG NUMBERS: WHERE A FLOAT LOSES DIGITS                 │
# └────────────────────────────────────────────────────────────┘
# A float is stored in 64 bits (a bit is a binary digit: 0 or 1), in a standard
# format called IEEE 754:
# - 52 bits hold the digits, and 1 more leading digit comes free: 53 digits
# - 12 bits hold the sign and where the point goes
# 53 binary digits store every integer exactly up to 2**53 = 9007199254740992.

assert 2 ** 53 == 9007199254740992
assert int(float(2 ** 53)) == 2 ** 53  # still exact

# Past 2**53, some integers can't be stored, so the float rounds them.

assert int(float(2 ** 53 + 1)) == 2 ** 53  # ...993 came back as ...992
assert float(2 ** 53 + 1) == float(2 ** 53)  # two integers, one float

# So the largest "safe" integer is 2**53 - 1: up to it, every integer and the
# next one are different floats. 53 binary digits are about 16 decimal digits.

# Python's int has no limit. It keeps every digit.

assert 2 ** 100 + 1 - 2 ** 100 == 1


# ┌────────────────────────────────────────────────────────────┐
# │ 5. ANYTHING -> STR                                         │
# └────────────────────────────────────────────────────────────┘
# str() turns any value into text, so you can join it with other text.

score = 31

assert str(score) == '31'
assert str(score) + '!' == '31!'
assert str(True) == 'True'


# ┌────────────────────────────────────────────────────────────┐
# │ 6. BOOL, AND TRUE AND FALSE AS NUMBERS                     │
# └────────────────────────────────────────────────────────────┘
# bool() of a number: 0 is False, anything else is True (negatives too).

assert bool(0) is False
assert bool(-1) is True

# bool() of a string only checks whether it is empty.

assert bool('') is False
assert bool('hello') is True

# True and False count as 1 and 0.

assert True + True == 2
assert int(False) == 0


print('All checks passed.')
