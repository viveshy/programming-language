"""
A simplified hierarchy of common operators, from highest to lowest precedence:
1. Parentheses ()
2. Exponentiation **
3. Unary minus: -x
4. Multiplication *, Division /, Floor Division //, Modulus %
5. Addition +, Subtraction -
6. Comparison Operators (>, <, >=, <=, ==, !=)
7. not
8. and
9. or
Assignment (=) is not an operator here: it happens last, after the right side is worked out.
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

# not, and, or each have their own level: not first, then and, then or
assert (True or False and False) is True  # and goes first: True or (False and False)
assert ((True or False) and False) is False  # brackets change the answer
assert (not True and False) is False  # not goes first: (not True) and False

print('All checks passed.')
