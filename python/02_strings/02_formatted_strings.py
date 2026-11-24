"""
Formatted strings in Python start with the prefix 'f'.
Any value (a string, a number, or an expression) can be added within curly braces {}.
"""

# 1. VALUES IN CURLY BRACES
# ___________________________
first_name = 'John'
last_name = 'Smith'

# Create a formatted string using f-string syntax
message = f'{first_name} [{last_name}] is a coder.'

print('Formatted string example:', message)
assert message == 'John [Smith] is a coder.'

# 2. EXPRESSIONS IN CURLY BRACES
# ___________________________
# Anything inside {} is worked out first, then turned into text
assert f'{2 + 3}' == '5'
assert f'{first_name} has {len(first_name)} letters' == 'John has 4 letters'

# 3. DECIMAL PLACES
# ___________________________
# :.2f after the value means "show 2 digits after the decimal point"
price = 3.14159
assert f'{price:.2f}' == '3.14'

print('All checks passed.')
