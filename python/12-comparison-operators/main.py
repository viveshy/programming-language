"""
In this section, we will learn about the following comparison operators:
1. Equal to (==)
2. Not equal to (!=)
3. Greater than (>)
4. Less than (<)
5. Greater than or equal to (>=)
6. Less than or equal to (<=)
"""

# Define some sample variables
a = 15
b = 10
c = 15

# 1. Equal to (==)
# ___________________
print(f'Checking if {a} is equal to {b}:')
# Expected Output: Checking if 15 is equal to 10:
if a == b:
    print(f'{a} is equal to {b}')
else:
    print(f'{a} is not equal to {b}')
    # Expected Output: 15 is not equal to 10

# 2. Not equal to (!=)
# ______________________
print(f'\nChecking if {a} is not equal to {c}:')
# Expected Output: Checking if 15 is not equal to 15:
if a != c:
    print(f'{a} is not equal to {c}')
else:
    print(f'{a} is equal to {c}')
    # Expected Output: 15 is equal to 15

# 3. Greater than (>)
# ______________________
print(f'\nChecking if {a} is greater than {b}:')
# Expected Output: Checking if 15 is greater than 10:
if a > b:
    print(f'{a} is greater than {b}')
    # Expected Output: 15 is greater than 10
else:
    print(f'{a} is not greater than {b}')

# 4. Less than (<)
# ___________________
print(f'\nChecking if {b} is less than {a}:')
if b < a:
    print(f'{b} is less than {a}')
else:
    print(f'{b} is not less than {a}')

# 5. Greater than or equal to (>=)
# _________________________________
print(f'\nChecking if {a} is greater than or equal to {c}:')
if a >= c:
    print(f'{a} is greater than or equal to {c}')
else:
    print(f'{a} is less than {c}')

# 6. Less than or equal to (<=)
# _______________________________
print(f'\nChecking if {b} is less than or equal to {a}:')
if b <= a:
    print(f'{b} is less than or equal to {a}')
else:
    print(f'{b} is greater than {a}')
