"""
We will learn about the following data types in this section:
1. Numbers
2. Strings
3. Boolean

HOW THESE LESSONS CHECK THEMSELVES
Each fact is written as an `assert` line, for example:
    assert price == 100
If the claim after `assert` is true, nothing happens and Python moves on.
If it is false, the program stops with an AssertionError showing that line.
So when a lesson reaches its last line and prints 'All checks passed.',
every fact in it is true.
"""

# 1. NUMBERS: int and float
# ___________________________
price = 100  # Price of the item (integer)
discount = 10.5  # Discount percentage (float)

assert type(price) is int
assert type(discount) is float
assert price == 100
assert discount == 10.5

# 2. STRINGS
# _______________
item_name = 'jeans'  # Name of the item (string)

assert type(item_name) is str
assert item_name == 'jeans'

# 3. BOOLEAN
# _______________
# NOTE: BOOLEAN can have only two values: True or False
is_discount_available = True  # Indicates if a discount is available (boolean)

assert type(is_discount_available) is bool
assert is_discount_available is True

print('All checks passed.')
