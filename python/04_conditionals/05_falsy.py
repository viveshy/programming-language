"""
A falsy value counts as False in an if, in a while, or with not.
Every other value is truthy: it counts as True.

    ┌─────────────┬────────────────────────────────────────────────┐
    │ Falsy value │ What it is                                     │
    ├─────────────┼────────────────────────────────────────────────┤
    │ 0 and 0.0   │ zero, of any number type                       │
    │ False       │ the bool False itself                          │
    │ ''          │ the empty string                               │
    │ None        │ Python's value for "no value here"             │
    │ [] () {}    │ empty collections, and also set() and range(0) │
    └─────────────┴────────────────────────────────────────────────┘

Why it matters: `if items:` means "if items is not empty". DSA code tests for
empty and for None like this all the time.

We will cover:
1. Zero and False
2. The empty string and None
3. Empty collections
4. Truthy values that look empty
5. Testing for None: is None
"""


# ┌────────────────────────────────────────────────────────────┐
# │ 1. ZERO AND FALSE                                          │
# └────────────────────────────────────────────────────────────┘
# Zero of any number type is falsy. Every other number is truthy, negatives too.
# bool() shows how a value counts (03_type_conversion.py).

assert bool(0) is False
assert bool(0.0) is False
assert bool(-1) is True

assert (not 0) is True
assert (not False) is True

# So a number can go straight into an if.

remainder = 7 % 2

if remainder:
    parity = 'odd'  # remainder is 1, which counts as True
else:
    parity = 'even'

assert parity == 'odd'


# ┌────────────────────────────────────────────────────────────┐
# │ 2. THE EMPTY STRING AND NONE                               │
# └────────────────────────────────────────────────────────────┘
# '' has no characters, so it is falsy. A string with any character is truthy.
# None is Python's value for "no value here". It is falsy too.

assert bool('') is False
assert bool('a') is True
assert bool(None) is False

name = ''  # what input() gives when the user just presses Enter

if name:
    greeting = 'Hello, ' + name
else:
    greeting = 'Hello, stranger'

assert greeting == 'Hello, stranger'


# ┌────────────────────────────────────────────────────────────┐
# │ 3. EMPTY COLLECTIONS                                       │
# └────────────────────────────────────────────────────────────┘
# A collection holds many values. Lists, tuples, dicts and sets come in
# 06_collections, and range in 05_loops.
# An empty one is falsy. One with anything in it is truthy.

assert bool([]) is False  # list
assert bool(()) is False  # tuple
assert bool({}) is False  # dict

assert bool(set()) is False  # {} is a dict, so an empty set is written set()
assert bool(range(0)) is False
assert bool([1, 2]) is True

# This is why `if items:` is the usual way to say "if the list is not empty".

items = []

if items:
    status = 'has items'
else:
    status = 'empty'

assert status == 'empty'


# ┌────────────────────────────────────────────────────────────┐
# │ 4. TRUTHY VALUES THAT LOOK EMPTY                           │
# └────────────────────────────────────────────────────────────┘
# A value is falsy only when it is zero, False, None or empty.
# Each of these holds one thing, so it is truthy.

assert bool('0') is True  # a string with one character, '0'
assert bool(' ') is True  # a string with one space
assert bool([0]) is True  # a list with one item in it


# ┌────────────────────────────────────────────────────────────┐
# │ 5. TESTING FOR NONE: IS NONE                               │
# └────────────────────────────────────────────────────────────┘
# x is None asks: is x exactly None? x is not None asks the opposite.
# (`is` asks whether two names point to the very same value. There is only one
# None, so `is None` is the standard test. More in 06_collections.)

result = None  # nothing found yet
assert result is None

result = 0  # found, at index 0
assert result is not None


print('All checks passed.')
