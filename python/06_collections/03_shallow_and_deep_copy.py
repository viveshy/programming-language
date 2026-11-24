"""
In Python, when you assign a list to a variable, it creates a reference to the original list. This means that both the original and copied lists point to the same list in memory.

To create a true copy of a list, you can use:
1. Shallow Copy: Creates a new list with references to the same elements as the original list.
2. Deep Copy: Creates a new list with copies of the original elements, including nested lists.

`a is b` is True when a and b are the very same object, not just equal ones.
"""

import copy

# 1. ASSIGNMENT IS NOT A COPY
# _____________________________
original = [1, 2, 3, 4]
same_list = original  # both names now point to ONE list

assert same_list is original
same_list[0] = 99
assert original == [99, 2, 3, 4]  # changed through the other name

# 2. SHALLOW COPY OF A FLAT LIST
# _____________________________
original = [1, 2, 3, 4]
shallow = original.copy()  # a new list

assert shallow == original
assert shallow is not original

# Changing the copy does not touch the original...
shallow[0] = 8
assert shallow == [8, 2, 3, 4]
assert original == [1, 2, 3, 4]

# ...and changing the original does not touch the copy
original[2] = 100
assert original == [1, 2, 100, 4]
assert shallow == [8, 2, 3, 4]

# 3. SHALLOW COPY OF A NESTED LIST
# _____________________________
# A shallow copy is a new OUTER list, but the inner lists are shared
original = [[1, 2, 3, 4], ['x', 'y', 'z']]
shallow = original.copy()

assert shallow is not original
assert shallow[0] is original[0]  # the same inner list

# Changing an inner list through the copy shows up in the original
shallow[0][2] = 'a'
assert shallow == [[1, 2, 'a', 4], ['x', 'y', 'z']]
assert original == [[1, 2, 'a', 4], ['x', 'y', 'z']]

# Replacing a whole inner list in the copy does not affect the original
shallow[1] = ['new']
assert original == [[1, 2, 'a', 4], ['x', 'y', 'z']]

# 4. DEEP COPY OF A NESTED LIST
# _____________________________
# A deep copy copies the inner lists too, so nothing is shared
original = [[1, 2, 3, 4], ['x', 'y', 'z']]
deep = copy.deepcopy(original)

assert deep == original
assert deep[0] is not original[0]

deep[0][2] = 'a'
assert deep == [[1, 2, 'a', 4], ['x', 'y', 'z']]
assert original == [[1, 2, 3, 4], ['x', 'y', 'z']]  # unchanged

original[1][2] = 77
assert original == [[1, 2, 3, 4], ['x', 'y', 77]]
assert deep == [[1, 2, 'a', 4], ['x', 'y', 'z']]  # unchanged

print('All checks passed.')
