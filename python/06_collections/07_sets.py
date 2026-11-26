"""
A set is a collection with no duplicates and no order.

    ┌───────────────┬────────────────────────────────────┐
    │ Code          │ What it does                       │
    ├───────────────┼────────────────────────────────────┤
    │ s = {1, 2, 3} │ a set with three items             │
    │ set()         │ an empty set ({} is an empty dict) │
    │ s.add(x)      │ put x in                           │
    │ x in s        │ is x in the set? O(1)              │
    └───────────────┴────────────────────────────────────┘

Why it matters: x in s takes O(1) time, like a dict key (06_dictionaries.py).
So sets answer "have I seen this before?" fast, and they drop duplicates.

We will cover:
1. Creating a set
2. add, remove and discard
3. Fast membership with in
4. Removing duplicates from a list
5. Union, intersection, difference
6. Subsets
7. Which values can go in a set
8. No order
"""


# ┌────────────────────────────────────────────────────────────┐
# │ 1. CREATING A SET                                          │
# └────────────────────────────────────────────────────────────┘
# Write the items inside {}, or pass a list or a string to set().
# Duplicates are dropped, and the order doesn't matter.

assert {3, 1, 2} == {1, 2, 3}
assert set([3, 1, 3, 2]) == {1, 2, 3}
assert set('banana') == {'b', 'a', 'n'}  # a string gives its characters


# ┌────────────────────────────────────────────────────────────┐
# │ 2. ADD, REMOVE AND DISCARD                                 │
# └────────────────────────────────────────────────────────────┘
# s.add(x) puts x in. Adding an item that is already there does nothing.

s = {1, 2}
s.add(3)
s.add(3)
assert s == {1, 2, 3}

# s.remove(x) and s.discard(x) both take x out.

s.remove(3)
s.discard(2)
assert s == {1}

# They differ when x is missing: remove(x) stops with a KeyError, but
# discard(x) does nothing.

s.discard(99)  # 99 is not in s: no error
assert s == {1}


# ┌────────────────────────────────────────────────────────────┐
# │ 3. FAST MEMBERSHIP WITH IN                                 │
# └────────────────────────────────────────────────────────────┘
# x in a list checks the items one by one: O(n) time.
# x in a set jumps straight to the answer: O(1) time.

seen = set()
repeats = []
for name in ['ana', 'bo', 'ana', 'cy', 'bo']:
    if name in seen:
        repeats.append(name)
    seen.add(name)
assert repeats == ['ana', 'bo']


# ┌────────────────────────────────────────────────────────────┐
# │ 4. REMOVING DUPLICATES FROM A LIST                         │
# └────────────────────────────────────────────────────────────┘
# set(items) keeps one of each item. len(set(items)) counts the different ones.

names = ['ana', 'bo', 'ana', 'cy', 'bo']

assert len(set(names)) == 3
assert sorted(set(names)) == ['ana', 'bo', 'cy']  # sorted() gives a list


# ┌────────────────────────────────────────────────────────────┐
# │ 5. UNION, INTERSECTION, DIFFERENCE                         │
# └────────────────────────────────────────────────────────────┘
# Four operators combine two sets into a new set.

a = {1, 2}
b = {2, 3}

assert a | b == {1, 2, 3}  # union: in either set
assert a & b == {2}  # intersection: in both sets
assert a - b == {1}  # difference: in a but not in b
assert a ^ b == {1, 3}  # symmetric difference: in exactly one of them

# Difference has a direction: b - a is not a - b.

assert b - a == {3}


# ┌────────────────────────────────────────────────────────────┐
# │ 6. SUBSETS                                                 │
# └────────────────────────────────────────────────────────────┘
# a <= b asks: is every item of a also in b? Then a is a "subset" of b.

assert {1, 2} <= {1, 2, 3}
assert not ({1, 4} <= {1, 2, 3})  # 4 is not in the right set


# ┌────────────────────────────────────────────────────────────┐
# │ 7. WHICH VALUES CAN GO IN A SET                            │
# └────────────────────────────────────────────────────────────┘
# Like dict keys, set items must be hashable: values that can't change, like
# str, int, float, or a tuple of such values (06_dictionaries.py).

visited = {(0, 0), (0, 1)}  # grid cells as (row, col) tuples
visited.add((0, 1))  # already there
assert len(visited) == 2


# ┌────────────────────────────────────────────────────────────┐
# │ 8. NO ORDER                                                │
# └────────────────────────────────────────────────────────────┘
# A set has no positions, so s[0] stops with a TypeError.
# The order you see when you print it or loop over it is not fixed. For
# strings, it can even change from one run to the next.
# Use sorted() when the order matters.

assert sorted({3, 1, 2}) == [1, 2, 3]


print('All checks passed.')
