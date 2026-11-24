"""
A comprehension builds a list, dict or set from a loop in a single line:

    [expression for item in iterable]
    [expression for item in iterable if condition]

We will cover:
1. List comprehensions
2. Comprehensions with a condition
3. Dict comprehensions
4. Set comprehensions
5. Generator expressions inside sum(), max() and friends
6. Building a grid (and the trap to avoid)
"""

# 1. LIST COMPREHENSIONS
# ________________________
squares = [x * x for x in range(5)]
assert squares == [0, 1, 4, 9, 16]

# It does the same as this loop
loop_squares = []
for x in range(5):
    loop_squares.append(x * x)

assert squares == loop_squares

# 2. WITH A CONDITION
# ________________________
# `if` at the END filters which items are kept
evens = [x for x in range(10) if x % 2 == 0]
assert evens == [0, 2, 4, 6, 8]

# `if ... else` in the EXPRESSION picks a value for every item
labels = ['even' if x % 2 == 0 else 'odd' for x in range(3)]
assert labels == ['even', 'odd', 'even']

# 3. DICT COMPREHENSIONS
# ________________________
assert {w: len(w) for w in ['hi', 'hey']} == {'hi': 2, 'hey': 3}

# 4. SET COMPREHENSIONS
# ________________________
assert {x % 3 for x in range(10)} == {0, 1, 2}

# 5. GENERATOR EXPRESSIONS
# ________________________
# Without brackets, inside a function call, the values are produced one at a
# time and never stored as a list
assert sum(x * x for x in range(4)) == 14  # 0 + 1 + 4 + 9
assert max(len(w) for w in ['a', 'abc', 'ab']) == 3

# 6. BUILDING A GRID
# ________________________
# n rows of m zeros. `_` is the usual name for a loop variable you don't use.
n, m = 2, 3

good = [[0] * m for _ in range(n)]  # a NEW inner list for every row
good[0][0] = 1
assert good == [[1, 0, 0], [0, 0, 0]]
assert good[1] == [0, 0, 0]

# The trap: * n repeats the SAME inner list n times (see 03_shallow_and_deep_copy.py)
bad = [[0] * m] * n
bad[0][0] = 1
assert bad == [[1, 0, 0], [1, 0, 0]]  # every row changed
assert bad[0] is bad[1]

print('All checks passed.')
