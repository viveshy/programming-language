"""
In this section, we will explore "falsy" values: values that count as False
when used in an if statement or with `not`.

Falsy values:
1. Zero of any number type (0, 0.0)
2. Boolean False
3. Empty String ("")
4. None
5. Any other empty collection: [], (), {}, set(), range(0)

Other built-in values are "truthy", including some that look empty but aren't.
"""

# 1. Zero (0)
assert bool(0) is False
assert bool(0.0) is False
assert (not 0) is True

# 2. Boolean False
assert (not False) is True

# 3. Empty String ("")
assert bool('') is False

# 4. None
assert bool(None) is False

# 5. Empty collections
assert bool([]) is False
assert bool(()) is False
assert bool({}) is False
assert bool(set()) is False
assert bool(range(0)) is False

# Truthy values that look empty but are not
assert bool('0') is True  # a string with one character, '0'
assert bool(' ') is True  # a string with one space
assert bool([0]) is True  # a list with one item in it

# This is why `if items:` is a common way to say "if the list is not empty"
items = []
if items:
    status = 'has items'
else:
    status = 'empty'

assert status == 'empty'

print('All checks passed.')
