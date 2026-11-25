r"""
Type conversion turns a value of one type into another. The built-in functions:
- int()    to a whole number
- float()  to a decimal number
- str()    to text
- bool()   to True or False

input() always gives you a string, so these conversions are how you turn what
the user typed into numbers. Below, plain strings stand in for what input()
would return.

What converts to what:

    from \ to   int()               float()          str()             bool()
    int         -                   3 -> 3.0         3 -> '3'          0 -> False, others True
    float       3.99 -> 3 (cuts)    -                2.5 -> '2.5'      0.0 -> False, others True
    str         '42' -> 42          '2.5' -> 2.5     -                 '' -> False, others True
    bool        True -> 1           True -> 1.0      True -> 'True'    -

What does NOT work (Python stops with a ValueError):
    int('2.5')    int() of a string needs a whole number: use int(float('2.5'))
    int('abc')    not a number at all
    int('')       an empty string is not a number either
    float('abc')  not a number

We will cover:
1. str -> int and float
2. int -> float, and float -> int
3. Anything -> str
4. bool, and bool as a number
"""

# 1. STR -> INT AND FLOAT
# ___________________
birth_year = '1990'  # what input() returns when the user types 1990

assert birth_year + '10' == '199010'  # still a string: + joins the text
assert int(birth_year) + 10 == 2000  # converted to int: + adds
assert type(int(birth_year)) is int

assert int('-42') == -42
assert int(' 42\n') == 42  # spaces and a newline around the number are ignored

assert float('2.5') == 2.5
assert float('3') == 3.0  # a whole number in text is fine for float()
assert float('1e3') == 1000.0  # 1e3 means 1 * 10**3

# int('2.5') fails (see the list at the top). Go through float() first:
assert int(float('2.5')) == 2

# 2. INT -> FLOAT, AND FLOAT -> INT
# ___________________
discount = 10

# int -> float: always works, and adds .0
assert float(discount) == 10.0
assert type(float(discount)) is float

# Mixing them in arithmetic converts the int to a float for you
assert 1 + 2.0 == 3.0
assert type(1 + 2.0) is float

# float -> int: int() cuts off the decimal part. It does NOT round.
assert int(3.99) == 3
assert int(-3.99) == -3  # it cuts towards zero, so -3.99 becomes -3, not -4
assert int(5.0) == 5

# To round to the nearest whole number, use round() instead
# (more in 03_numbers_and_operators/04_math_functions.py)
assert round(3.99) == 4

# Check that a float is a whole number before converting it
assert (5.0).is_integer() is True
assert (5.5).is_integer() is False

# Careful with very big numbers: a float keeps only about 16 significant digits,
# so int -> float -> int can come back different
assert int(float(9007199254740993)) == 9007199254740992  # the last digit changed

# 3. ANYTHING -> STR
# ___________________
visible_number = 31

assert str(visible_number) == '31'
assert str(visible_number) + '!' == '31!'
assert str(2.5) == '2.5'
assert str(3.0) == '3.0'  # a float keeps its .0
assert str(True) == 'True'

# Python never mixes text and numbers by itself: 31 + '!' is an error (TypeError).
# Convert one side first, as above.

# 4. BOOL, AND BOOL AS A NUMBER
# ___________________
# Numbers: zero is False, everything else is True (negative numbers too)
assert bool(0) is False
assert bool(0.0) is False
assert bool(5) is True
assert bool(-1) is True

# bool() of a string only checks whether the string is empty.
# Any non-empty string is True, even the string 'False', or a single space.
is_monday = 'False'  # what input() returns when the user types False

assert bool(is_monday) is True
assert bool(' ') is True
assert bool('') is False

# To read a True/False answer, compare the text instead:
assert (is_monday == 'True') is False

# The other way: True and False behave like the numbers 1 and 0
assert int(True) == 1
assert int(False) == 0
assert float(True) == 1.0
assert True + True == 2  # handy for counting how many conditions are true

print('All checks passed.')
