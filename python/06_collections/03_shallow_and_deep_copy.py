"""
In Python, when you assign a list to a variable, it creates a reference to the original list. This means that both the original and copied lists point to the same list in memory.

To create a true copy of a list, you can use:
1. Shallow Copy: Creates a new list with references to the same elements as the original list.
2. Deep Copy: Creates a new list with copies of the original elements, including nested lists.

"""

import copy

# SHALLOW COPY
#_______________
print(f'Shallow copy in flat list:')
# Expected Output: Shallow copy in flat list:
shallow_original_list_flat = [1, 2, 3, 4]

shallow_copied_list_flat = shallow_original_list_flat.copy()

print(f'\nChange in original list {shallow_original_list_flat}: shallow_original_list_flat[0] = 8 ')
# Expected Output: Change in original list [1, 2, 3, 4]: shallow_original_list_flat[0] = 8

shallow_original_list_flat[0] = 8
print(f'Orginal list: ', shallow_original_list_flat)
# Expected Output: Orginal list:  [8, 2, 3, 4]

print(f'Copied list:', shallow_copied_list_flat)
# Expected Output: Copied list: [1, 2, 3, 4]

print(f'\nChange in copied list {shallow_copied_list_flat}: shallow_original_list_flat[2] = 100 ')
# Expected Output: Change in copied list [1, 2, 3, 4]: shallow_original_list_flat[2] = 100

shallow_original_list_flat[2] = 100
print(f'Orginal list: ', shallow_original_list_flat)
# Expected Output: Orginal list:  [8, 2, 100, 4]

print(f'Copied list:', shallow_copied_list_flat)
# Expected Output: Copied list: [1, 2, 3, 4]


print(f'\nShallow copy in nested list:')
# Expected Output: Shallow copy in nested list:
shallow_original_list_nested = [[1, 2, 3, 4], ['x','y','z']]

shallow_copied_list_nested = shallow_original_list_nested.copy()

print(f'\nChange in original list {shallow_original_list_nested}: shallow_original_list_nested[0][2] = "a"')
# Expected Output: Change in original list [[1, 2, 3, 4], ['x', 'y', 'z']]: shallow_original_list_nested[0][2] = "a"

shallow_original_list_nested[0][2] = 'a'
print(f'Orginal list: ', shallow_original_list_nested)
# Expected Output: Orginal list:  [[1, 2, 'a', 4], ['x', 'y', 'z']]

print(f'Copied list:', shallow_copied_list_nested)
# Expected Output: Copied list: [[1, 2, 'a', 4], ['x', 'y', 'z']]

print(f'\nChange in copied list {shallow_copied_list_nested}: shallow_original_list_nested[1][2] = 77')
# Expected Output: Change in copied list [[1, 2, 'a', 4], ['x', 'y', 'z']]: shallow_original_list_nested[1][2] = 77

shallow_original_list_nested[1][2] = 77
print(f'Orginal list: ', shallow_original_list_nested)
# Expected Output: Orginal list:  [[1, 2, 'a', 4], ['x', 'y', 77]]

print(f'Copied list:', shallow_copied_list_nested)
# Expected Output: Copied list: [[1, 2, 'a', 4], ['x', 'y', 77]]


# DEEP COPY
#_______________
print(f'Deep copy in flat list:')
# Expected Output: Deep copy in flat list:
deep_original_list_flat = [1, 2, 3, 4]

deep_copied_list_flat = copy.deepcopy(deep_original_list_flat)

print(f'\nChange in original list {deep_original_list_flat}: deep_original_list_flat[0] = 8 ')
# Expected Output: Change in original list [1, 2, 3, 4]: deep_original_list_flat[0] = 8

deep_original_list_flat[0] = 8
print(f'Orginal list: ', deep_original_list_flat)
# Expected Output: Orginal list:  [8, 2, 3, 4]

print(f'Copied list:', deep_copied_list_flat)
# Expected Output: Copied list: [1, 2, 3, 4]

print(f'\nChange in copied list {deep_copied_list_flat}: deep_original_list_flat[2] = 100 ')
# Expected Output: Change in copied list [1, 2, 3, 4]: deep_original_list_flat[2] = 100

deep_original_list_flat[2] = 100
print(f'Orginal list: ', deep_original_list_flat)
# Expected Output: Orginal list:  [8, 2, 100, 4]

print(f'Copied list:', deep_copied_list_flat)
# Expected Output: Copied list: [1, 2, 3, 4]


print(f'\nDeep copy in nested list:')
# Expected Output: Deep copy in nested list:
deep_original_list_nested = [[1, 2, 3, 4], ['x','y','z']]

deep_copied_list_nested = copy.deepcopy(deep_original_list_nested)

print(f'\nChange in original list {deep_original_list_nested}: deep_original_list_nested[0][2] = "a"')
# Expected Output: Change in original list [[1, 2, 3, 4], ['x', 'y', 'z']]: deep_original_list_nested[0][2] = "a"

deep_original_list_nested[0][2] = 'a'
print(f'Orginal list: ', deep_original_list_nested)
# Expected Output: Orginal list:  [[1, 2, 'a', 4], ['x', 'y', 'z']]

print(f'Copied list:', deep_copied_list_nested)
# Expected Output: Copied list: [[1, 2, 3, 4], ['x', 'y', 'z']]

print(f'\nChange in copied list {deep_copied_list_nested}: deep_original_list_nested[1][2] = 77')
# Expected Output: Change in copied list [[1, 2, 3, 4], ['x', 'y', 'z']]: deep_original_list_nested[1][2] = 77

deep_original_list_nested[1][2] = 77
print(f'Orginal list: ', deep_original_list_nested)
# Expected Output: Orginal list:  [[1, 2, 'a', 4], ['x', 'y', 77]]

print(f'Copied list:', deep_copied_list_nested)
# Expected Output: Copied list: [[1, 2, 3, 4], ['x', 'y', 'z']]