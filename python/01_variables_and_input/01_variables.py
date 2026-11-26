"""
A variable is a name that stores a value. Every value has a type:

    ┌───────┬──────────────────────────────────────────┐
    │ Type  │ What it holds                            │
    ├───────┼──────────────────────────────────────────┤
    │ int   │ an integer: ..., -2, -1, 0, 1, 2, ...    │
    │ float │ a number with a decimal point, like 10.5 │
    │ str   │ a string (text), like 'jeans'            │
    │ bool  │ True or False                            │
    └───────┴──────────────────────────────────────────┘

Why it matters: every program keeps its data in variables, and the type
decides what you can do with a value.

We will cover:
1. assert: how these lessons check themselves
2. Variables: a name for a value
3. Numbers: int and float
4. Strings: str
5. Booleans: bool
"""


# ┌────────────────────────────────────────────────────────────┐
# │ 1. ASSERT: HOW THESE LESSONS CHECK THEMSELVES              │
# └────────────────────────────────────────────────────────────┘
# Each fact in these lessons is written as an assert line.
# - If the claim after assert is true, nothing happens and Python moves on.
# - If it is false, the program stops with an AssertionError showing that line.

assert 1 + 1 == 2  # == asks: are these two equal?
assert 10 - 3 == 7

# So when a lesson reaches its last line and prints 'All checks passed.',
# every fact in it is true.


# ┌────────────────────────────────────────────────────────────┐
# │ 2. VARIABLES: A NAME FOR A VALUE                           │
# └────────────────────────────────────────────────────────────┘
# = stores the value on the right under the name on the left.
# After that, the name gives back the value.

price = 100

assert price == 100
assert price + 5 == 105

# A new = replaces the old value. The variable keeps only the latest one.

price = 80
assert price == 80

# A name uses letters, digits and _, and can't start with a digit: item_name.
# Names are case sensitive: price and Price are two different variables.

Price = 5
assert Price == 5
assert price == 80  # unchanged


# ┌────────────────────────────────────────────────────────────┐
# │ 3. NUMBERS: INT AND FLOAT                                  │
# └────────────────────────────────────────────────────────────┘
# An int is an integer: no decimal point. It can be negative.
# A float is a number with a decimal point.
# type(x) gives the type of x. Read type(x) is int as "x is an int".

discount = 10.5  # a percentage

assert type(price) is int
assert type(-7) is int
assert type(discount) is float


# ┌────────────────────────────────────────────────────────────┐
# │ 4. STRINGS: STR                                            │
# └────────────────────────────────────────────────────────────┘
# A string is text inside quotes (more in 02_strings).

item_name = 'jeans'

assert type(item_name) is str
assert item_name == 'jeans'


# ┌────────────────────────────────────────────────────────────┐
# │ 5. BOOLEANS: BOOL                                          │
# └────────────────────────────────────────────────────────────┘
# A bool has only two values: True and False.
# It answers a yes/no question. == gives a bool.

is_discount_available = True

assert type(is_discount_available) is bool
assert is_discount_available is True
assert (price == 100) is False  # price is 80 now


print('All checks passed.')
