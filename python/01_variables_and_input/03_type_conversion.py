"""
The built-in functions used for explicit conversion are:
- int()
- float()
- bool()
- str()

input() always gives you a string, so these conversions are how you turn
what the user typed into numbers. Below, plain strings stand in for what
input() would return.
"""

# int() conversion
# ________________
birth_year = '1990'  # what input() returns when the user types 1990

assert birth_year + '10' == '199010'  # still a string: + joins the text
assert int(birth_year) + 10 == 2000  # converted to int: + adds
assert int('-42') == -42

# int() on a float cuts off the decimal part. It does not round.
assert int(3.99) == 3
assert int(-3.99) == -3

# float() conversion
# ________________
discount = 10

assert float(discount) == 10.0
assert float('2.5') == 2.5

# str() conversion
# ________________
visible_number = 31

assert str(visible_number) == '31'
assert str(visible_number) + '!' == '31!'

# bool() conversion
# ________________
# bool() of a string only checks whether the string is empty.
# Any non-empty string is True, even the string 'False'.
is_monday = 'False'  # what input() returns when the user types False

assert bool(is_monday) is True
assert bool('') is False

# To read a True/False answer, compare the text instead:
assert (is_monday == 'True') is False

print('All checks passed.')
