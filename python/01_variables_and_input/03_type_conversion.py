"""
The built-in functions used for explicit conversion are:
- int()
- float() 
- bool()
- str()
"""

# int() conversion
# ________________
birth_year = input('Enter your birth year:\n')
# User input example: 1990

# Convert the input string to integer and calculate age
age = 2024 - int(birth_year)

print('Your age is:', age)
# Expected Output: Your age is: 34

# float() conversion
# ________________
discount = 10

# Convert integer to float
print('Discount in float is:', float(discount))
# Expected Output: Discount in float is: 10.0

# str() conversion
# ________________
visible_number = 31

# Convert integer to string
print('Integer to string is:', str(visible_number))
# Expected Output: Integer to string is: 31

# bool() conversion
# ________________
is_monday = input('Is it Monday today? Enter True or False:\n')
# User input example: True

# Convert input string to boolean
print('Today is Monday:', bool(is_monday))
# Expected Output: Today is Monday: True (Note: Any non-empty string returns True)