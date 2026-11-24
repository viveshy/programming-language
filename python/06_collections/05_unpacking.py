"""
Unpacking puts the items of a tuple or list into separate variables in one line.
The number of variables on the left must match the number of items.
"""

# 1. TUPLE UNPACKING
# ____________________
coordinates = (1, 3, 8)

x, y, z = coordinates
assert (x, y, z) == (1, 3, 8)
assert x == 1 and y == 3 and z == 8

# 2. SWAPPING TWO VALUES
# ____________________
# The right side is built first as a tuple (b, a), then unpacked into a, b
a = 10
b = 20
a, b = b, a
assert (a, b) == (20, 10)

# 3. LIST UNPACKING
# ____________________
dimensions = [40, 50, 60]

length, breadth, height = dimensions
assert (length, breadth, height) == (40, 50, 60)

# 4. IGNORING VALUES WITH _
# ____________________
more_dimensions = [40, 50, 60, 70]
length, breadth, height, _ = more_dimensions  # Using _ to ignore the last value
assert height == 60

# 5. COLLECTING THE REST WITH *
# ____________________
first, *rest = [1, 2, 3, 4]
assert first == 1
assert rest == [2, 3, 4]  # the starred name always gets a list

*start, last = [1, 2, 3, 4]
assert start == [1, 2, 3]
assert last == 4

print('All checks passed.')
