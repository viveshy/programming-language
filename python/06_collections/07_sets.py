"""
A set is a collection with no duplicates and no order.
Checking whether something is in a set is very fast, which makes sets the tool
for "have I seen this before?" questions.

We will cover:
1. Creating a set
2. add, remove and discard
3. Fast membership with `in`
4. Removing duplicates from a list
5. Union, intersection, difference
6. Subsets
7. Which values can go in a set
8. No order
"""

# 1. CREATING A SET
# ___________________
assert type(set()) is set  # an empty set
assert type({}) is dict  # careful: {} is an empty DICT

assert {3, 1, 2} == {1, 2, 3}  # order does not matter
assert set([3, 1, 3, 2]) == {1, 2, 3}  # duplicates are dropped
assert set('banana') == {'b', 'a', 'n'}

# 2. ADD, REMOVE AND DISCARD
# ___________________
s = {1, 2}
s.add(3)
s.add(3)  # adding an item that is already there does nothing
assert s == {1, 2, 3}

s.remove(3)
assert s == {1, 2}

s.discard(99)  # discard quietly ignores a missing item...
assert s == {1, 2}

try:
    s.remove(99)  # ...but remove raises a KeyError
    raised = False
except KeyError:
    raised = True

assert raised is True

# 3. FAST MEMBERSHIP
# ___________________
# `x in some_list` checks the items one by one. `x in some_set` jumps
# straight to the answer. With a million items, that is slow versus instant.
seen = set()
duplicates = []
for name in ['ana', 'bo', 'ana', 'cy', 'bo']:
    if name in seen:
        duplicates.append(name)
    seen.add(name)

assert duplicates == ['ana', 'bo']

# 4. REMOVING DUPLICATES FROM A LIST
# ___________________
names = ['ana', 'bo', 'ana', 'cy', 'bo']
assert len(set(names)) == 3
assert sorted(set(names)) == ['ana', 'bo', 'cy']  # sorted(), because a set has no order

# 5. UNION, INTERSECTION, DIFFERENCE
# ___________________
a = {1, 2}
b = {2, 3}

assert a | b == {1, 2, 3}  # union: in either set
assert a & b == {2}  # intersection: in both sets
assert a - b == {1}  # difference: in a but not in b
assert a ^ b == {1, 3}  # symmetric difference: in exactly one of them

# 6. SUBSETS
# ___________________
assert {1, 2} <= {1, 2, 3}  # every item of the left set is in the right set
assert not ({1, 4} <= {1, 2, 3})

# 7. WHICH VALUES CAN GO IN A SET
# ___________________
# Like dict keys, set items must be values that cannot change ("hashable")
assert {(1, 2), (1, 2)} == {(1, 2)}  # tuples of hashable items are fine

try:
    bad = {[1, 2]}  # a list can change, so it cannot go in a set
    allowed = True
except TypeError:
    allowed = False

assert allowed is False

# 8. NO ORDER
# ___________________
# A set has no positions (s[0] is an error), and the order you see when you
# print or loop over it can change between runs. Use sorted() when order matters.
assert sorted({3, 1, 2}) == [1, 2, 3]

print('All checks passed.')
