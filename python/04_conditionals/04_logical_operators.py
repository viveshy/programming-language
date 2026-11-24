"""
In this section, we will learn about logical operators in Python.
We will cover the following operators:
1. Logical AND (and): True only when both sides are True
2. Logical OR (or): True when at least one side is True
3. Logical NOT (not): flips True to False and False to True
"""

x = 5
y = 10

# 1. Logical AND (and)
# ________________________
assert (True and True) is True
assert (True and False) is False
assert (False and False) is False

assert (x > 0 and y > 0) is True  # both x and y are positive

# 2. Logical OR (or)
# ________________________
assert (True or False) is True
assert (False or False) is False

assert (x < 0 or y < 0) is False  # neither is negative

# 3. Logical NOT (not)
# ________________________
assert (not True) is False
assert (not False) is True

assert (not (x > 0)) is False  # x is positive, so "not positive" is False

# 4. Combining Logical Operators
# ________________________________
d = False

if (x > 0 and y > 0) or (not d):
    result = 'both positive, or d is False'
else:
    result = 'neither'

assert result == 'both positive, or d is False'

print('All checks passed.')
