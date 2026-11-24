"""
A simplified hierarchy of common operators, from highest to lowest precedence:
1.Parentheses ()
2.Exponentiation **
3.Multiplication *, Division /, Floor Division //, Modulus %
4.Addition +, Subtraction -
5.Comparison Operators (>, <, >=, <=, ==, !=)
6.Logical Operators: AND and, OR or
7.Assignment =
"""

# Multiplication happens before addition and subtraction: 10 + 6 - 5
assert 10 + 2 * 3 - 5 == 11

# Parentheses go first
assert (10 + 2) * 3 == 36

# Several levels at once: 2 ** 2 first, then 3 * 4 and 8 / 4, then + and -
assert 5 + 3 * 2 ** 2 - 8 / 4 == 15.0

# Two surprises with **
assert -2 ** 2 == -4  # ** happens before the minus sign: -(2 ** 2)
assert (-2) ** 2 == 4
assert 2 ** 3 ** 2 == 512  # ** goes right to left: 2 ** (3 ** 2) = 2 ** 9

print('All checks passed.')
