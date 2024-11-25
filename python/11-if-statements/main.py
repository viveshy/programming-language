"""
In this section, we will learn about the following concepts related to if statements:
1. Basic if statement
2. if-else statement
3. if-elif-else statement
4. Nested if statements
"""

# 1. Basic if statement
# ______________________
number = 10

print(f'Checking if {number} is positive:')
if number > 0:
    print(f'{number} is a positive number.')

# 2. if-else statement
# ______________________
print(f'\nChecking if {number} is even or odd:')
if number % 2 == 0:
    print(f'{number} is an even number.')
else:
    print(f'{number} is an odd number.')

# 3. if-elif-else statement
# ___________________________
print('\nGrading System:')
score = 85

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f'Score: {score}, Grade: {grade}')

# 4. Nested if statements
# _________________________
age = 20
has_permission = True

print('\nChecking access based on age and permission:')
if age >= 18:
    print('You are an adult.')
    if has_permission:
        print('You have permission to enter.')
    else:
        print('You do not have permission to enter.')
else:
    print('You are not an adult.')
    