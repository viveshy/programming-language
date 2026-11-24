"""
In this section, we will learn about the following comparison operators:
1. Equal to (==)
2. Not equal to (!=)
3. Greater than (>)
4. Less than (<)
5. Greater than or equal to (>=)
6. Less than or equal to (<=)

A comparison produces True or False, so it can go straight into an if
statement, or into an assert.
"""

# Define some sample variables
a = 15
b = 10
c = 15

# 1. Equal to (==)
# ___________________
assert (a == b) is False
assert (a == c) is True

# 2. Not equal to (!=)
# ______________________
assert (a != c) is False
assert (a != b) is True

# 3. Greater than (>)
# ______________________
assert (a > b) is True

# 4. Less than (<)
# ___________________
assert (b < a) is True

# 5. Greater than or equal to (>=)
# _________________________________
assert (a >= c) is True  # equal counts

# 6. Less than or equal to (<=)
# _______________________________
assert (b <= a) is True

# 7. Using a comparison in an if statement
# _______________________________
if a > b:
    bigger = a
else:
    bigger = b

assert bigger == 15

# 8. Chained comparisons
# _______________________________
# Python lets you chain comparisons: b < a <= c means (b < a) and (a <= c)
assert (b < a <= c) is True

print('All checks passed.')
