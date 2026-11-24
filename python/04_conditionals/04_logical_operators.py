"""
In this section, we will learn about logical operators in Python.
We will cover the following operators:
1. Logical AND (and)
2. Logical OR (or)
3. Logical NOT (not)
"""

# 1. Logical AND (and)
# ________________________
print('Logical AND (and):')
# Expected Output: Logical AND (and):
a = True
b = False

# Example of AND operator
if a and b:
    print('Both a and b are True.')
else:
    print('At least one of a or b is False.')
    # Expected Output: At least one of a or b is False.

# Additional examples
x = 5
y = 10
if x > 0 and y > 0:
    print('Both x and y are positive numbers.')
    # Expected Output: Both x and y are positive numbers.

# 2. Logical OR (or)
# ________________________
print('\nLogical OR (or):')
# Expected Output: Logical OR (or):
c = True
d = False

# Example of OR operator
if c or d:
    print('At least one of c or d is True.')
    # Expected Output: At least one of c or d is True.
else:
    print('Both c and d are False.')

# Additional examples
if x < 0 or y < 0:
    print('At least one of x or y is negative.')
else:
    print('Both x and y are non-negative.')
    # Expected Output: Both x and y are non-negative.

# 3. Logical NOT (not)
# ________________________
print('\nLogical NOT (not):')
# Expected Output: Logical NOT (not):
e = True

# Example of NOT operator
if not e:
    print('e is False.')
else:
    print('e is True.')
    # Expected Output: e is True.

# Additional examples
if not (x > 0):
    print('x is not positive.')
else:
    print('x is positive.')
    # Expected Output: x is positive.

# 4. Combining Logical Operators
# ________________________________
print('\nCombining Logical Operators:')
# Expected Output: Combining Logical Operators:

if (x > 0 and y > 0) or (not d):
    print('Either both x and y are positive or d is False.')
    # Expected Output: Either both x and y are positive or d is False.

