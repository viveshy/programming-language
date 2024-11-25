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

# Convert the input string to integer and calculate age
age = 2024 - int(birth_year)

print('Your age is:', age)

# float() conversion
# ________________
discount = 10

# Convert integer to float
print('Discount in float is:', float(discount))

# str() conversion
# ________________
visible_number = 31

# Convert integer to string
print('Integer to string is:', str(visible_number))

# bool() conversion
# ________________
is_monday = input('Is it Monday today? Enter True or False:\n')

# Convert input string to boolean
print('Today is Monday:', bool(is_monday))