"""
Unpacking puts the items of a tuple or a list into separate names, in one line.

    ┌──────────────────────┬─────────────────────────────────────┐
    │ Code                 │ What it does                        │
    ├──────────────────────┼─────────────────────────────────────┤
    │ x, y, z = (1, 3, 8)  │ x is 1, y is 3, z is 8              │
    │ a, b = b, a          │ swap two values                     │
    │ first, *rest = items │ rest gets a list of the other items │
    └──────────────────────┴─────────────────────────────────────┘

Why it matters: reading two numbers from a line (n, m = ...) and swapping two
values come up in almost every solution.

We will cover:
1. Unpacking a tuple or a list
2. Swapping two values
3. Ignoring a value with _
4. Collecting the rest with *
"""


# ┌────────────────────────────────────────────────────────────┐
# │ 1. UNPACKING A TUPLE OR A LIST                             │
# └────────────────────────────────────────────────────────────┘
# Put as many names on the left as there are items on the right. The first
# name gets the first item, the second name the second, and so on.

coordinates = (1, 3, 8)

x, y, z = coordinates
assert x == 1 and y == 3 and z == 8

# A list unpacks the same way.

length, breadth, height = [40, 50, 60]
assert (length, breadth, height) == (40, 50, 60)


# ┌────────────────────────────────────────────────────────────┐
# │ 2. SWAPPING TWO VALUES                                     │
# └────────────────────────────────────────────────────────────┘
# a, b = b, a swaps two values. The right side is built first, as the tuple
# (b, a). Then it is unpacked into a and b.

a = 10
b = 20
a, b = b, a
assert (a, b) == (20, 10)

# It works on list items too.

nums = [1, 2, 3]
nums[0], nums[2] = nums[2], nums[0]
assert nums == [3, 2, 1]


# ┌────────────────────────────────────────────────────────────┐
# │ 3. IGNORING A VALUE WITH _                                 │
# └────────────────────────────────────────────────────────────┘
# _ is an ordinary name. By habit, it means "I don't need this value".

length, breadth, height, _ = [40, 50, 60, 70]
assert height == 60
assert _ == 70  # it still holds the value, like any other name


# ┌────────────────────────────────────────────────────────────┐
# │ 4. COLLECTING THE REST WITH *                              │
# └────────────────────────────────────────────────────────────┘
# A name with * before it collects all the items the other names don't take.
# Only one name may have the *.

first, *rest = [1, 2, 3, 4]
assert first == 1
assert rest == [2, 3, 4]

*start, last = [1, 2, 3, 4]
assert start == [1, 2, 3]
assert last == 4

# The starred name always gets a list, even from a tuple, and even when no
# items are left for it.

head, *tail = (5,)
assert head == 5
assert tail == []


print('All checks passed.')
