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
print(f'Round of {negative_num} is: {round(negative_num)}')


# abs()
print(f'\nAbsolute value of {positive_num} is: {abs(positive_num)}')
print(f'Absolute value of {negative_num} is: {abs(negative_num)}')


# Math methods
# ________________

# math.ceil()
print(f'\nCeiling of {positive_num} is: {math.ceil(positive_num)}')
print(f'Ceiling of {negative_num} is: {math.ceil(negative_num)}')

# math.floor()
print(f'\nFloor of {positive_num} is: {math.floor(positive_num)}')
print(f'Floor of {negative_num} is: {math.floor(negative_num)}')