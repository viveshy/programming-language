"""
Lists in Python can be created using square brackets [] and can contain items of different data types.

CREATING A LIST:
To create a list, simply write a set of items within square brackets, separated by commas. For example:
- A list of integers: `numbers = [1, 2, 3, 4]`
- A heterogeneous list: `mixed = [1, 'apple', 3.14, True]`

ACCESSING LIST ELEMENTS:
Each item in a list has an assigned index value, starting from 0. You can access items using their index:
- Use positive indexing: `list_name[index]`
- Use negative indexing: `list_name[-index]` (counts from the end)
"""

# 1. CREATING LISTS
# ___________________
numbers = [1, 2, 3, 4]
mixed = [1, 'apple', 3.14, True]

assert len(numbers) == 4
assert len(mixed) == 4
assert len([]) == 0  # an empty list

# 2. INDEXING
# ___________________
assert numbers[0] == 1  # First element (index 0)
assert numbers[1] == 2  # Second element (index 1)
assert numbers[-1] == 4  # Last element
assert numbers[-2] == 3  # Second last element

# 3. SLICING
# ___________________
# Like strings: the start index is included, the end index is not
assert numbers[1:3] == [2, 3]
assert numbers[:2] == [1, 2]
assert numbers[2:] == [3, 4]
assert numbers[:] == [1, 2, 3, 4]  # a copy of the whole list

# 4. CHANGING AN ITEM
# ___________________
# Unlike strings, lists can be changed in place
numbers[0] = 10
assert numbers == [10, 2, 3, 4]

print('All checks passed.')
