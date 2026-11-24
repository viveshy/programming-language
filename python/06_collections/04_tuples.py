"""
Tuples are similar to lists in Python. However, unlike lists,
tuples are immutable, meaning we cannot modify them after creation.
"""

# LIST VS TUPLE
numbers_list = [1, 2, 3, 4, 5]  # A mutable list
numbers_tuple = (1, 2, 3, 4, 5)  # An immutable tuple

# 1. TUPLE METHODS
# __________________
# Two primarily used methods on tuples are: count and index

# count(x): Returns the number of occurrences of x in the tuple
assert numbers_tuple.count(3) == 1

# index(x): Returns the index of the first occurrence of x in the tuple
assert numbers_tuple.index(4) == 3

# 2. ACCESSING AND SLICING
# __________________
# Works just like lists
assert numbers_tuple[0] == 1
assert numbers_tuple[-1] == 5
assert numbers_tuple[1:4] == (2, 3, 4)  # slicing a tuple gives a tuple

# 3. A TUPLE WITH ONE ITEM
# __________________
# The comma makes the tuple, not the parentheses
assert type((5,)) is tuple
assert type((5)) is int  # just the number 5 in brackets

# 4. TUPLES ARE IMMUTABLE
# __________________
# HOW TO CHECK THAT SOMETHING RAISES AN ERROR
# Put the line that should fail inside `try:`. If it raises the error named
# in `except`, Python jumps to the except block instead of stopping.
# We record what happened in a variable and assert it afterwards.
try:
    numbers_tuple[0] = 10  # Attempting to modify the first element
    changed = True
except TypeError:
    changed = False  # 'tuple' object does not support item assignment

assert changed is False
assert numbers_tuple == (1, 2, 3, 4, 5)

# A list allows the same change
numbers_list[0] = 10
assert numbers_list == [10, 2, 3, 4, 5]

print('All checks passed.')
