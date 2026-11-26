"""
A for loop takes the items of a sequence one at a time, and runs its block once
for each item.

    for item in sequence:
        block        # item is the next item each time

    ┌──────────────┬───────────────────────────────┐
    │ Looping over │ Gives                         │
    ├──────────────┼───────────────────────────────┤
    │ a list       │ its items, in order           │
    │ a string     │ its characters, one at a time │
    │ a range      │ its numbers (02_range.py)     │
    └──────────────┴───────────────────────────────┘

Why it matters: most loops in contest code are for loops: over range(n), over
the characters of a string, or over a list of numbers.

We will cover:
1. Looping over a list or a string
2. Looping over indexes with range
3. break and continue in a for loop
4. Nested loops
5. for ... else
6. enumerate: index and item together
7. zip: two sequences side by side
"""


# ┌────────────────────────────────────────────────────────────┐
# │ 1. LOOPING OVER A LIST OR A STRING                         │
# └────────────────────────────────────────────────────────────┘
# The loop variable (fruit here) is set to each item in turn.
# fruits is a list: items in order, inside [ ] (lists come in 06_collections).
# seen.append(x) adds x to the end of the list seen.

fruits = ['apple', 'banana', 'cherry']
seen = []

for fruit in fruits:
    seen.append(fruit)

assert seen == ['apple', 'banana', 'cherry']

# A string gives one character at a time.

vowels = 0
for ch in 'banana':
    if ch in 'aeiou':  # is ch one of these letters? (in: 02_strings)
        vowels += 1

assert vowels == 3


# ┌────────────────────────────────────────────────────────────┐
# │ 2. LOOPING OVER INDEXES WITH RANGE                         │
# └────────────────────────────────────────────────────────────┘
# range(len(nums)) gives the indexes 0, 1, ..., len(nums) - 1 (02_range.py).
# Loop over indexes when you need the position, not just the item.
# To change the items of a list, assign to nums[i] (more in 06_collections).

nums = [1, 2, 3]
for i in range(len(nums)):
    nums[i] = nums[i] * 2

assert nums == [2, 4, 6]

# An index also lets you look at a neighbour: s[i - 1] is just before s[i].

word = 'aabbbc'
changes = 0
for i in range(1, len(word)):
    if word[i] != word[i - 1]:
        changes += 1

assert changes == 2  # a -> b and b -> c


# ┌────────────────────────────────────────────────────────────┐
# │ 3. BREAK AND CONTINUE IN A FOR LOOP                        │
# └────────────────────────────────────────────────────────────┘
# They work as in a while loop (01_while_loop.py):
# - break leaves the loop at once
# - continue skips the rest of the block and goes on to the next item
# In a for loop, continue can't loop forever: the next item comes by itself.

first_big = None  # None means "nothing found yet"
for x in [3, 8, 12, 20]:
    if x > 10:
        first_big = x
        break

assert first_big == 12  # 20 was never looked at

letters = ''
for ch in 'a-b c':
    if ch == '-' or ch == ' ':
        continue
    letters += ch

assert letters == 'abc'


# ┌────────────────────────────────────────────────────────────┐
# │ 4. NESTED LOOPS                                            │
# └────────────────────────────────────────────────────────────┘
# A loop inside a loop. The inner loop runs all the way through for every
# step of the outer loop.

products = []
for i in range(1, 4):  # outer loop: rows
    for j in range(1, 4):  # inner loop: columns
        products.append(i * j)

assert products == [1, 2, 3, 2, 4, 6, 3, 6, 9]  # 3 * 3 = 9 rounds


# ┌────────────────────────────────────────────────────────────┐
# │ 5. FOR ... ELSE                                            │
# └────────────────────────────────────────────────────────────┘
# Like while ... else: the else block runs only if the loop did not break.
# Use it to search: break when you find it, and else means "not found".

for number in [3, 8, 11]:
    if number % 2 == 0:
        found = number
        break
else:
    found = 'no even number'

assert found == 8

for number in [3, 5, 11]:
    if number % 2 == 0:
        found = number
        break
else:
    found = 'no even number'

assert found == 'no even number'


# ┌────────────────────────────────────────────────────────────┐
# │ 6. ENUMERATE: INDEX AND ITEM TOGETHER                      │
# └────────────────────────────────────────────────────────────┘
# enumerate(fruits) gives pairs (index, item), counting from 0.
# Each pair is a tuple, and for index, fruit in ... unpacks it into two names
# (tuples and unpacking come in 06_collections).

pairs = []
for index, fruit in enumerate(fruits):
    pairs.append((index, fruit))

assert pairs == [(0, 'apple'), (1, 'banana'), (2, 'cherry')]


# ┌────────────────────────────────────────────────────────────┐
# │ 7. ZIP: TWO SEQUENCES SIDE BY SIDE                         │
# └────────────────────────────────────────────────────────────┘
# zip(a, b) pairs up the first items of a and b, then the second items, and
# so on.

prices = [40, 20, 60]
menu = []
for fruit, price in zip(fruits, prices):
    menu.append(f'{fruit}: {price}')

assert menu == ['apple: 40', 'banana: 20', 'cherry: 60']
assert list(zip(['a', 'b'], [1, 2])) == [('a', 1), ('b', 2)]


print('All checks passed.')
