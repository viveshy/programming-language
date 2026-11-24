"""
In this section, we will learn about the following concepts related to for loops:
1. Basic for loop
2. For loop with range
3. Nested for loops
4. For loop with else clause
5. For loop with enumerate
6. For loop with zip
"""

fruits = ['apple', 'banana', 'cherry']

# 1. Basic for loop
# ______________________
seen = []
for fruit in fruits:
    print(fruit)
    seen.append(fruit)

assert seen == ['apple', 'banana', 'cherry']

# 2. For loop with range
# ______________________
squares = []
for i in range(5):
    squares.append(i * i)

assert squares == [0, 1, 4, 9, 16]

# 3. Nested for loops
# _________________________
# The inner loop runs completely for every step of the outer loop
products = []
for i in range(1, 4):  # Outer loop for rows
    for j in range(1, 4):  # Inner loop for columns
        products.append(i * j)

assert products == [1, 2, 3, 2, 4, 6, 3, 6, 9]

# 4. For loop with else clause
# ___________________________
# Like while/else: the else block runs only if the loop did not hit a break.
# A common use is searching: break when found, else means "not found".
found = None
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

# 5. For loop with enumerate
# ___________________________
# enumerate gives (index, item) pairs. (index, item) is a tuple, and
# `for index, fruit in ...` unpacks it; both are covered in 06_collections.
pairs = []
for index, fruit in enumerate(fruits):
    pairs.append((index, fruit))

assert pairs == [(0, 'apple'), (1, 'banana'), (2, 'cherry')]

# start=1 makes the counting begin at 1
assert list(enumerate(fruits, start=1)) == [(1, 'apple'), (2, 'banana'), (3, 'cherry')]

# 6. For loop with zip
# ___________________________
# zip walks through two (or more) lists side by side
prices = [40, 20, 60]
menu = []
for fruit, price in zip(fruits, prices):
    menu.append(f'{fruit}: {price}')

assert menu == ['apple: 40', 'banana: 20', 'cherry: 60']
assert list(zip(['a', 'b'], [1, 2])) == [('a', 1), ('b', 2)]

# zip stops at the end of the SHORTER list
assert list(zip(['a', 'b', 'c'], [1, 2])) == [('a', 1), ('b', 2)]

print('All checks passed.')
