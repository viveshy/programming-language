"""
A dictionary (dict) stores key: value pairs. You look a value up by its key,
not by its position.

    ┌────────────────────┬───────────────────────────────────────────────┐
    │ Code               │ What it does                                  │
    ├────────────────────┼───────────────────────────────────────────────┤
    │ d = {'soup': 4.99} │ a dict with one pair: key 'soup', value 4.99  │
    │ d['soup']          │ read a value (KeyError if the key is missing) │
    │ d.get('soup', 0)   │ read a value, or get 0 if the key is missing  │
    │ d['pie'] = 7.99    │ add a pair, or replace the value              │
    │ 'pie' in d         │ is this key in the dict?                      │
    └────────────────────┴───────────────────────────────────────────────┘

Why it matters: a dict finds a key in O(1) time: the same short time however
big it is. Counting, grouping and memo tables are all dicts.

We will cover:
1. Creating a dictionary
2. Reading values: d[key] vs d.get(key, default)
3. Adding and updating
4. Checking keys with in
5. Removing: del and pop
6. Looping over keys(), values() and items()
7. Which values can be keys
8. Counting with d.get(x, 0) + 1
9. Grouping: a list for each key
"""


# ┌────────────────────────────────────────────────────────────┐
# │ 1. CREATING A DICTIONARY                                   │
# └────────────────────────────────────────────────────────────┘
# Write key: value pairs inside {}, with commas between them.

menu = {'soup': 4.99, 'pie': 7.99, 'salad': 6.99}

assert len(menu) == 3  # len() counts the pairs
assert menu['pie'] == 7.99

# dict() builds one too. Each name=value becomes a pair, with the name as a
# string key.

assert dict(a=1, b=2) == {'a': 1, 'b': 2}


# ┌────────────────────────────────────────────────────────────┐
# │ 2. READING VALUES: D[KEY] VS D.GET(KEY, DEFAULT)           │
# └────────────────────────────────────────────────────────────┘
# d[key] gives the value for a key.
# d.get(key, default) gives the default instead when the key is missing.

assert menu['soup'] == 4.99
assert menu.get('pie', 0) == 7.99  # the key is there: its value
assert menu.get('juice', 0) == 0  # the key is missing: the default

# With no default, get() gives None for a missing key.

assert menu.get('juice') is None


# ┌────────────────────────────────────────────────────────────┐
# │ 3. ADDING AND UPDATING                                     │
# └────────────────────────────────────────────────────────────┘
# d[key] = value adds the key if it is new, and replaces its value if it is not.
# A key appears only once in a dict.

menu['soup'] = 8.99  # 'soup' is there: its value is replaced
menu['juice'] = 3.5  # 'juice' is new: it is added

assert menu == {'soup': 8.99, 'pie': 7.99, 'salad': 6.99, 'juice': 3.5}

# Writing the same key twice in {} keeps only the last value.

assert {'a': 1, 'a': 2} == {'a': 2}


# ┌────────────────────────────────────────────────────────────┐
# │ 4. CHECKING KEYS WITH IN                                   │
# └────────────────────────────────────────────────────────────┘
# key in d asks: is this key in the dict? It takes O(1) time.
# x in a list checks the items one by one: O(n) time, where n is the number of
# items. So it gets slower as the list grows.

assert 'pie' in menu
assert 'cake' not in menu  # not in is the opposite of in


# ┌────────────────────────────────────────────────────────────┐
# │ 5. REMOVING: DEL AND POP                                   │
# └────────────────────────────────────────────────────────────┘
# del d[key] removes a pair. d.pop(key) removes it and gives back its value.

del menu['juice']
assert 'juice' not in menu

price = menu.pop('salad')
assert price == 6.99
assert menu == {'soup': 8.99, 'pie': 7.99}


# ┌────────────────────────────────────────────────────────────┐
# │ 6. LOOPING OVER KEYS(), VALUES() AND ITEMS()               │
# └────────────────────────────────────────────────────────────┘
# A dict remembers the order its keys were added in (Python 3.7 and later).
# Loops go in that order. A plain loop over a dict gives the keys.

assert list(menu) == ['soup', 'pie']  # list(d) gives the keys
assert list(menu.keys()) == ['soup', 'pie']
assert list(menu.values()) == [8.99, 7.99]
assert list(menu.items()) == [('soup', 8.99), ('pie', 7.99)]

# items() gives (key, value) pairs. Unpack each pair into two names.

lines = []
for item, cost in menu.items():
    lines.append(f'{item}: {cost}')
assert lines == ['soup: 8.99', 'pie: 7.99']

# Order doesn't matter to ==: two dicts are equal when they hold the same pairs.

assert {'a': 1, 'b': 2} == {'b': 2, 'a': 1}


# ┌────────────────────────────────────────────────────────────┐
# │ 7. WHICH VALUES CAN BE KEYS                                │
# └────────────────────────────────────────────────────────────┘
# A key must be "hashable": a value that can't change, like str, int, float, or
# a tuple of such values. Python turns the key into a number (its hash) to find
# it fast, so the key must never change.

grid = {(0, 1): 'wall'}  # a tuple key: a (row, col) position
assert grid[(0, 1)] == 'wall'


# ┌────────────────────────────────────────────────────────────┐
# │ 8. COUNTING WITH D.GET(X, 0) + 1                           │
# └────────────────────────────────────────────────────────────┘
# Start with an empty dict. For each item, add 1 to its count.
# get(x, 0) gives 0 the first time x is seen, so a new key starts at 1.

counts = {}
for letter in 'banana':
    counts[letter] = counts.get(letter, 0) + 1
assert counts == {'b': 1, 'a': 3, 'n': 2}


# ┌────────────────────────────────────────────────────────────┐
# │ 9. GROUPING: A LIST FOR EACH KEY                           │
# └────────────────────────────────────────────────────────────┘
# To group items, map each key to a list. Make the empty list the first time a
# key is seen, then append to it.

by_first = {}
for word in ['ant', 'bee', 'ape']:
    first = word[0]
    if first not in by_first:
        by_first[first] = []
    by_first[first].append(word)
assert by_first == {'a': ['ant', 'ape'], 'b': ['bee']}


print('All checks passed.')
