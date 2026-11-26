"""
A copy is a new list with the same items. b = a is NOT a copy: it gives the
same list a second name.

    ┌──────────────────────┬──────────────────────────────────────────────────┐
    │ Code                 │ What you get                                     │
    ├──────────────────────┼──────────────────────────────────────────────────┤
    │ b = a                │ one list, two names                              │
    │ b = a.copy()         │ shallow copy: new outer list, shared inner lists │
    │ b = copy.deepcopy(a) │ deep copy: new lists all the way down            │
    └──────────────────────┴──────────────────────────────────────────────────┘

Why it matters: a change through a "copy" that is not one changes the original
too. In BFS and DP this quietly breaks a grid, and you get a Wrong Answer.

We will cover:
1. Assignment is not a copy
2. += changes the list, + makes a new one
3. Shallow copy of a flat list
4. Shallow copy of a nested list
5. Deep copy
"""

import copy  # copy.deepcopy (section 5) lives in the copy module


# ┌────────────────────────────────────────────────────────────┐
# │ 1. ASSIGNMENT IS NOT A COPY                                │
# └────────────────────────────────────────────────────────────┘
# b = a makes b a second name for the SAME list. A change through one name
# shows up through the other.

original = [1, 2, 3, 4]
same_list = original

same_list[0] = 99
assert original == [99, 2, 3, 4]  # changed through the other name

# a is b asks: are a and b the very same object? == only asks: equal values?

assert same_list is original


# ┌────────────────────────────────────────────────────────────┐
# │ 2. += CHANGES THE LIST, + MAKES A NEW ONE                  │
# └────────────────────────────────────────────────────────────┘
# On a list, b += [2] changes the list itself, so every name for it sees it.
# b = b + [3] builds a NEW list and points only b at it.

a = [1]
b = a
b += [2]
assert a == [1, 2]  # a sees the change

b = b + [3]
assert b == [1, 2, 3]
assert a == [1, 2]  # a still points to the old list


# ┌────────────────────────────────────────────────────────────┐
# │ 3. SHALLOW COPY OF A FLAT LIST                             │
# └────────────────────────────────────────────────────────────┘
# a.copy() makes a new list with the same items. a[:] and list(a) do the same.

original = [1, 2, 3, 4]
shallow = original.copy()

assert shallow == original
assert shallow is not original
assert original[:] is not original and list(original) is not original

# Changing the copy does not touch the original, and the other way round.

shallow[0] = 8
assert original == [1, 2, 3, 4]

original[2] = 100
assert shallow == [8, 2, 3, 4]


# ┌────────────────────────────────────────────────────────────┐
# │ 4. SHALLOW COPY OF A NESTED LIST                           │
# └────────────────────────────────────────────────────────────┘
# A shallow copy is a new OUTER list, but the inner lists inside are shared.

original = [[1, 2, 3, 4], ['x', 'y', 'z']]
shallow = original.copy()

assert shallow is not original
assert shallow[0] is original[0]  # the same inner list

# Changing an item inside an inner list shows up in the original.

shallow[0][2] = 'a'
assert original == [[1, 2, 'a', 4], ['x', 'y', 'z']]

# Replacing a whole inner list changes only the outer list of the copy.

shallow[1] = ['new']
assert original == [[1, 2, 'a', 4], ['x', 'y', 'z']]


# ┌────────────────────────────────────────────────────────────┐
# │ 5. DEEP COPY                                               │
# └────────────────────────────────────────────────────────────┘
# copy.deepcopy(a) copies the inner lists too, so nothing is shared.

original = [[1, 2, 3, 4], ['x', 'y', 'z']]
deep = copy.deepcopy(original)

assert deep == original
assert deep[0] is not original[0]

# A change on either side stays on that side.

deep[0][2] = 'a'
assert original == [[1, 2, 3, 4], ['x', 'y', 'z']]

original[1][2] = 77
assert deep == [[1, 2, 'a', 4], ['x', 'y', 'z']]


print('All checks passed.')
