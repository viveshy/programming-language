"""
In this section, we will learn about the following Math functions and methods:

Functions:
    - round(x)    : Rounds a number to the nearest integer.
    - abs(x)      : Returns the absolute value of a number.

Methods: 
    - math.floor(x) : Returns the largest integer less than or equal to x.
    - math.ceil(x)  : Returns the smallest integer greater than or equal to x.

Note: Math methods are imported from the module 'math'.
"""

import math

# Define positive and negative numbers
positive_num = 5.36
negative_num = -8.34

# Math functions
# __________________
# round()
print(f'Round of {positive_num} is: {round(positive_num)}')
# Expected Output: Round of 5.36 is: 5

print(f'Round of {negative_num} is: {round(negative_num)}')
# Expected Output: Round of -8.34 is: -8


# abs()
print(f'\nAbsolute value of {positive_num} is: {abs(positive_num)}')
# Expected Output: Absolute value of 5.36 is: 5.36

print(f'Absolute value of {negative_num} is: {abs(negative_num)}')
# Expected Output: Absolute value of -8.34 is: 8.34


# Math methods
# ________________

# math.ceil()
print(f'\nCeiling of {positive_num} is: {math.ceil(positive_num)}')
# Expected Output: Ceiling of 5.36 is: 6

print(f'Ceiling of {negative_num} is: {math.ceil(negative_num)}')
# Expected Output: Ceiling of -8.34 is: -8

# math.floor()
print(f'\nFloor of {positive_num} is: {math.floor(positive_num)}')
# Expected Output: Floor of 5.36 is: 5

print(f'Floor of {negative_num} is: {math.floor(negative_num)}')
# Expected Output: Floor of -8.34 is: -9