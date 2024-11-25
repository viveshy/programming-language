"""
In this section, we will learn about string comparison in Python.
We will cover the following topics:
1. Equality Check (==)
2. Inequality Check (!=)
3. Case Sensitivity
4. Whitespace Considerations
"""

# Define some sample strings with descriptive names
greeting_message = "Hello, World!"
duplicate_greeting = "Hello, World!"
different_greeting = "Hello, Python!"
case_different_greeting = "hello, world!"  # Different case
trailing_whitespace_greeting = "Hello, World!   "  # String with trailing whitespace
leading_whitespace_greeting = "   Hello, World!"  # String with leading whitespace

# 1. Equality Check (==)
# ________________________
print(f'Checking equality:')
if greeting_message == duplicate_greeting:
    print(f'"{greeting_message}" is equal to "{duplicate_greeting}"')
else:
    print(f'"{greeting_message}" is not equal to "{duplicate_greeting}"')

# 2. Inequality Check (!=)
# __________________________
print(f'\nChecking inequality:')
if greeting_message != different_greeting:
    print(f'"{greeting_message}" is not equal to "{different_greeting}"')
else:
    print(f'"{greeting_message}" is equal to "{different_greeting}"')

# 3. Case Sensitivity
# _____________________
print(f'\nChecking case sensitivity:')
if greeting_message == case_different_greeting:
    print(f'"{greeting_message}" is equal to "{case_different_greeting}" (case insensitive)')
else:
    print(f'"{greeting_message}" is not equal to "{case_different_greeting}" (case sensitive)')

# 4. Whitespace Considerations
# ______________________________
print(f'\nChecking whitespace considerations:')
if greeting_message.strip() == trailing_whitespace_greeting.strip():
    print(f'"{greeting_message.strip()}" is equal to "{trailing_whitespace_greeting.strip()}" (ignoring trailing whitespace)')
else:
    print(f'"{greeting_message.strip()}" is not equal to "{trailing_whitespace_greeting.strip()}"')

if greeting_message.strip() == leading_whitespace_greeting.strip():
    print(f'"{greeting_message.strip()}" is equal to "{leading_whitespace_greeting.strip()}" (ignoring leading whitespace)')
else:
    print(f'"{greeting_message.strip()}" is not equal to "{leading_whitespace_greeting.strip()}"')