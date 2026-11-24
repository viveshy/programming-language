"""
A dictionary (dict) stores key: value pairs. You look a value up by its key
instead of by its position. Keys are unique: setting a key again replaces
its value.

We will cover:
1. Creating a dictionary
2. Reading values: d[key] vs d.get(key, default)
3. Adding and updating
4. Checking keys with `in`
5. Removing: del and pop
6. Looping over keys(), values() and items()
7. Order
8. Which values can be keys
9. The counting pattern
"""

# 1. CREATING A DICTIONARY
# __________________________
menu = {'soup': 4.99, 'pie': 7.99, 'salad': 6.99}

assert len(menu) == 3
assert type({}) is dict  # {} is an empty dict, not an empty set
assert dict(a=1, b=2) == {'a': 1, 'b': 2}

# 2. READING VALUES
# __________________________
assert menu['soup'] == 4.99

# A missing key with [] raises a KeyError
try:
    menu['juice']
    found = True
except KeyError:
    found = False

assert found is False

# .get() returns a default instead of raising (None if you give no default)
assert menu.get('juice') is None
assert menu.get('juice', 0) == 0
assert menu.get('pie', 0) == 7.99

# 3. ADDING AND UPDATING
# __________________________
menu['soup'] = 8.99  # the key exists: its value is replaced
menu['juice'] = 3.5  # the key is new: it is added

assert menu == {'soup': 8.99, 'pie': 7.99, 'salad': 6.99, 'juice': 3.5}

# 4. CHECKING KEYS WITH in
# __________________________
assert ('pie' in menu) is True
assert (7.99 in menu) is False  # `in` looks at the keys, not the values
assert (7.99 in menu.values()) is True

# 5. REMOVING
# __________________________
del menu['juice']
assert ('juice' in menu) is False

price = menu.pop('salad')  # pop removes the key and gives back its value
assert price == 6.99
assert menu.pop('missing', None) is None  # with a default, a missing key is fine

# 6. LOOPING
# __________________________
assert list(menu.keys()) == ['soup', 'pie']
assert list(menu.values()) == [8.99, 7.99]
assert list(menu.items()) == [('soup', 8.99), ('pie', 7.99)]

lines = []
for item, cost in menu.items():  # each item is a (key, value) pair
    lines.append(f'{item}: {cost}')

assert lines == ['soup: 8.99', 'pie: 7.99']

# 7. ORDER
# __________________________
# A dict remembers the order its keys were added in (Python 3.7 and later)
fresh = {'soup': 1, 'pie': 2, 'salad': 3}
assert list(fresh) == ['soup', 'pie', 'salad']  # list(d) gives the keys

# 8. WHICH VALUES CAN BE KEYS
# __________________________
# Keys must be values that cannot change ("hashable"): str, int, float, tuple.
# A tuple key is handy for grid positions.
grid = {(0, 1): 'wall'}
assert grid[(0, 1)] == 'wall'

# A list can change, so it cannot be a key
try:
    bad = {[0, 1]: 'wall'}
    allowed = True
except TypeError:
    allowed = False

assert allowed is False

# 9. THE COUNTING PATTERN
# __________________________
# get(letter, 0) gives 0 the first time a letter is seen
counts = {}
for letter in 'banana':
    counts[letter] = counts.get(letter, 0) + 1

assert counts == {'b': 1, 'a': 3, 'n': 2}

print('All checks passed.')
