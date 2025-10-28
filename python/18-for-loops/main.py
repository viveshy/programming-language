"""
In this section, we will learn about the following concepts related to for loops:
1. Basic for loop
2. For loop with range
3. Nested for loops
4. For loop with else clause
5. For loop with enumerate
"""

# 1. Basic for loop
# ______________________
fruits = ['apple', 'banana', 'cherry']

print('Iterating over a list of fruits:')
# Expected Output: Iterating over a list of fruits:
for fruit in fruits:
    print(fruit)
    # Expected Output: apple, banana, cherry (each on new line)

# 2. For loop with range
# ______________________
print('\nUsing range to iterate over numbers:')
# Expected Output: Using range to iterate over numbers:
for i in range(5):
    print(f'Current number: {i}')
    # Expected Output: Current number: 0, 1, 2, 3, 4 (each on new line)

# 3. Nested for loops
# _________________________
print('\nNested for loops to create a multiplication table:')
for i in range(1, 4):  # Outer loop for rows
    for j in range(1, 4):  # Inner loop for columns
        print(f'{i} x {j} = {i * j}')
    print('---')  # Separator for rows

# 4. For loop with else clause
# ___________________________
print('\nUsing a for loop with an else clause:')
for number in range(3):
    print(f'Number: {number}')
else:
    print('Loop completed without encountering a break statement.')

# 5. For loop with enumerate
# ___________________________
print('\nUsing a for loop with enumerate:')
# Expected Output: Using a for loop with enumerate:
for index, fruit in enumerate(fruits):
    print(f'Index {index}: {fruit}')
    # Expected Output: Index 0: apple, Index 1: banana, Index 2: cherry
