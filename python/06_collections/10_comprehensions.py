"""
A comprehension builds a list, dict or set from a loop, in one line.

    ┌─────────────────────────────┬───────────────────────────────────┐
    │ Comprehension               │ Builds                            │
    ├─────────────────────────────┼───────────────────────────────────┤
    │ [x * x for x in items]      │ a list                            │
    │ [x for x in items if x > 0] │ a list that keeps only some items │
    │ {x: len(x) for x in items}  │ a dict                            │
    │ {x % 3 for x in items}      │ a set                             │
    └─────────────────────────────┴───────────────────────────────────┘

Why it matters: building, filtering and changing lists is part of almost every
problem. And [[0] * m for _ in range(n)] is the safe way to make a grid.

We will cover:
1. List comprehensions
2. Filtering with if, and choosing with if ... else
3. Dict comprehensions
4. Set comprehensions
5. Generator expressions inside sum(), max() and friends
6. Building a grid
"""


# ┌────────────────────────────────────────────────────────────┐
# │ 1. LIST COMPREHENSIONS                                     │
# └────────────────────────────────────────────────────────────┘
# [expression for item in items] works out the expression for every item and
# collects the results in a new list.

squares = [x * x for x in range(5)]
assert squares == [0, 1, 4, 9, 16]

# It does the same as this loop.

loop_squares = []
for x in range(5):
    loop_squares.append(x * x)
assert squares == loop_squares


# ┌────────────────────────────────────────────────────────────┐
# │ 2. FILTERING WITH IF, AND CHOOSING WITH IF ... ELSE        │
# └────────────────────────────────────────────────────────────┘
# An if at the END filters: only the items that pass are kept.

evens = [x for x in range(10) if x % 2 == 0]
assert evens == [0, 2, 4, 6, 8]

# An if ... else in the EXPRESSION picks a value for every item. Nothing is
# dropped.

labels = ['even' if x % 2 == 0 else 'odd' for x in range(3)]
assert labels == ['even', 'odd', 'even']


# ┌────────────────────────────────────────────────────────────┐
# │ 3. DICT COMPREHENSIONS                                     │
# └────────────────────────────────────────────────────────────┘
# {key: value for item in items} builds a dict.

assert {w: len(w) for w in ['hi', 'hey']} == {'hi': 2, 'hey': 3}

# With enumerate, it maps each item to its index.

index_of = {ch: i for i, ch in enumerate('abc')}
assert index_of == {'a': 0, 'b': 1, 'c': 2}


# ┌────────────────────────────────────────────────────────────┐
# │ 4. SET COMPREHENSIONS                                      │
# └────────────────────────────────────────────────────────────┘
# {expression for item in items}, with no colon, builds a set. Duplicates are
# dropped, as in any set.

assert {x % 3 for x in range(10)} == {0, 1, 2}


# ┌────────────────────────────────────────────────────────────┐
# │ 5. GENERATOR EXPRESSIONS INSIDE SUM(), MAX() AND FRIENDS   │
# └────────────────────────────────────────────────────────────┘
# With no brackets of its own, inside a call like sum(), it is a "generator
# expression". The values are made one at a time and never stored as a list.

assert sum(x * x for x in range(4)) == 14  # 0 + 1 + 4 + 9
assert max(len(w) for w in ['a', 'abc', 'ab']) == 3

# True counts as 1 (01_variables_and_input/03_type_conversion.py), so sum() of
# a condition counts the items that pass.

assert sum(x > 0 for x in [3, -1, 2]) == 2


# ┌────────────────────────────────────────────────────────────┐
# │ 6. BUILDING A GRID                                         │
# └────────────────────────────────────────────────────────────┘
# n rows of m zeros. _ is the usual name for a loop variable you don't use.
# [0] * m runs again for every row, so each row is a NEW list.

n, m = 2, 3

good = [[0] * m for _ in range(n)]
good[0][0] = 1
assert good == [[1, 0, 0], [0, 0, 0]]  # only row 0 changed

# Don't write [[0] * m] * n. It repeats the SAME inner list n times, so
# changing one row changes every row (03_shallow_and_deep_copy.py shows why).

bad = [[0] * m] * n
bad[0][0] = 1
assert bad == [[1, 0, 0], [1, 0, 0]]  # every row changed
assert bad[0] is bad[1]  # one list, in two places


print('All checks passed.')
