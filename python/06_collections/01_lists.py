"""
A list holds many values in order, inside square brackets: [1, 2, 3].

    ┌─────────────────┬───────────────────────────────────────────────────┐
    │ Code            │ Meaning                                           │
    ├─────────────────┼───────────────────────────────────────────────────┤
    │ numbers[0]      │ the first item (indexes start at 0)               │
    │ numbers[-1]     │ the last item                                     │
    │ numbers[1:3]    │ a slice: a new list of the items at index 1 and 2 │
    │ numbers[0] = 10 │ change an item in place                           │
    └─────────────────┴───────────────────────────────────────────────────┘

Why it matters: every array in a problem is a list in Python. You read into it,
index it and change it in almost every solution.

We will cover:
1. Creating a list
2. Indexing
3. Slicing
4. Changing an item
5. Joining and repeating lists
"""


# ┌────────────────────────────────────────────────────────────┐
# │ 1. CREATING A LIST                                         │
# └────────────────────────────────────────────────────────────┘
# Write the items inside [], with commas between them. len() counts the items.

numbers = [1, 2, 3, 4]

assert len(numbers) == 4
assert len([]) == 0  # an empty list

# One list can hold items of different types.

mixed = [1, 'apple', 3.14, True]
assert len(mixed) == 4


# ┌────────────────────────────────────────────────────────────┐
# │ 2. INDEXING                                                │
# └────────────────────────────────────────────────────────────┘
# Each item has an index. The first is 0, the second is 1, and so on.
# Negative indexes count from the end: -1 is the last item.

assert numbers[0] == 1
assert numbers[1] == 2

assert numbers[-1] == 4
assert numbers[-2] == 3


# ┌────────────────────────────────────────────────────────────┐
# │ 3. SLICING                                                 │
# └────────────────────────────────────────────────────────────┘
# A slice works like a string slice: the start index is included, the end is
# not. Leave out start to begin at 0, or end to go to the end.

assert numbers[1:3] == [2, 3]
assert numbers[:2] == [1, 2]
assert numbers[2:] == [3, 4]

# numbers[:] is a new list with every item: a copy
# (more in 03_shallow_and_deep_copy.py).

assert numbers[:] == [1, 2, 3, 4]


# ┌────────────────────────────────────────────────────────────┐
# │ 4. CHANGING AN ITEM                                        │
# └────────────────────────────────────────────────────────────┘
# Unlike a string, a list can be changed in place: assign to an index.

numbers[0] = 10
assert numbers == [10, 2, 3, 4]

numbers[-1] = 40
assert numbers == [10, 2, 3, 40]


# ┌────────────────────────────────────────────────────────────┐
# │ 5. JOINING AND REPEATING LISTS                             │
# └────────────────────────────────────────────────────────────┘
# + joins two lists into a new one. * repeats the items.

assert [1, 2] + [3] == [1, 2, 3]
assert [1, 2] * 2 == [1, 2, 1, 2]
assert [0] * 3 == [0, 0, 0]


print('All checks passed.')
