"""
A tuple holds values in order, like a list, but it can't be changed after it is
made (it is immutable).

    ┌───────┬───────────┬──────────────────┐
    │ Type  │ Example   │ After it is made │
    ├───────┼───────────┼──────────────────┤
    │ list  │ [1, 2, 3] │ can be changed   │
    │ tuple │ (1, 2, 3) │ can't be changed │
    └───────┴───────────┴──────────────────┘

Why it matters: a pair like (row, col) is a tuple. Because it can't change, it
can be a dictionary key or a set item, and a list can't.

We will cover:
1. Creating a tuple: the comma makes it
2. Indexing and slicing
3. Tuples can't be changed (and how to check for an error)
4. count() and index(): the only two methods
"""


# ┌────────────────────────────────────────────────────────────┐
# │ 1. CREATING A TUPLE: THE COMMA MAKES IT                    │
# └────────────────────────────────────────────────────────────┘
# Write the items inside (), with commas between them.

numbers_tuple = (1, 2, 3, 4, 5)
assert len(numbers_tuple) == 5

# The comma makes the tuple, not the parentheses. They can be left out.

point = 3, 4
assert type(point) is tuple
assert point == (3, 4)

# So a tuple with one item needs a comma too: (5,). Without the comma, (5) is
# just the number 5 in brackets.

assert type((5,)) is tuple
assert type((5)) is int


# ┌────────────────────────────────────────────────────────────┐
# │ 2. INDEXING AND SLICING                                    │
# └────────────────────────────────────────────────────────────┘
# Indexing and slicing work just like lists. A slice of a tuple is a tuple.

assert numbers_tuple[0] == 1
assert numbers_tuple[-1] == 5
assert numbers_tuple[1:4] == (2, 3, 4)


# ┌────────────────────────────────────────────────────────────┐
# │ 3. TUPLES CAN'T BE CHANGED (AND HOW TO CHECK FOR AN ERROR) │
# └────────────────────────────────────────────────────────────┘
# How to check that a line raises an error:
# - put the line that should fail inside try:
# - if it raises the error named in except, Python jumps to the except block
#   instead of stopping;
# - record what happened in a variable, and assert it afterwards.

try:
    numbers_tuple[0] = 10  # try to change the first item
    changed = True
except TypeError:
    changed = False  # 'tuple' object does not support item assignment

assert changed is False
assert numbers_tuple == (1, 2, 3, 4, 5)

# A list allows the same change.

numbers_list = [1, 2, 3, 4, 5]
numbers_list[0] = 10
assert numbers_list == [10, 2, 3, 4, 5]


# ┌────────────────────────────────────────────────────────────┐
# │ 4. COUNT() AND INDEX(): THE ONLY TWO METHODS               │
# └────────────────────────────────────────────────────────────┘
# A tuple has only two ordinary methods: count() and index().
# It has no append() or sort(), because it can't change.

letters = ('a', 'b', 'a', 'c')

assert letters.count('a') == 2  # how many times 'a' appears
assert letters.index('a') == 0  # the index of the FIRST 'a'
assert letters.index('c') == 3


print('All checks passed.')
