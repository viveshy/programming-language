"""
In this section, we will learn about the following concepts related to if statements:
1. Basic if statement
2. if-else statement
3. if-elif-else statement
4. Nested if statements

Each example stores which branch ran in a variable, so an assert can check it.
"""

# 1. Basic if statement
# ______________________
number = 10

sign = 'unknown'
if number > 0:
    sign = 'positive'

assert sign == 'positive'

# 2. if-else statement
# ______________________
if number % 2 == 0:
    parity = 'even'
else:
    parity = 'odd'

assert parity == 'even'

# 3. if-elif-else statement
# ___________________________
# Python checks the conditions from the top and runs only the FIRST one that is true
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

assert grade == 'B'  # 85 >= 70 is also true, but the 'B' branch came first

# 4. Nested if statements
# _________________________
age = 20
has_permission = True

if age >= 18:
    if has_permission:
        access = 'adult with permission: may enter'
    else:
        access = 'adult without permission: may not enter'
else:
    access = 'not an adult'

assert access == 'adult with permission: may enter'

print('All checks passed.')
