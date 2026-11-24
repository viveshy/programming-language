"""
In this section, we will learn about string comparison in Python.
We will cover the following topics:
1. Equality Check (==)
2. Inequality Check (!=)
3. Case Sensitivity
4. Whitespace Considerations
5. Alphabetical Order (<, >)
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
assert greeting_message == duplicate_greeting

# 2. Inequality Check (!=)
# __________________________
assert greeting_message != different_greeting

# 3. Case Sensitivity
# _____________________
# 'H' and 'h' are different characters
assert 'Hello' != 'hello'
assert greeting_message != case_different_greeting

# To ignore case, compare lowercase copies
assert greeting_message.lower() == case_different_greeting.lower()

# 4. Whitespace Considerations
# ______________________________
# Spaces count as characters, so these are not equal...
assert greeting_message != trailing_whitespace_greeting
assert greeting_message != leading_whitespace_greeting

# ...until strip() removes the spaces at the ends
assert trailing_whitespace_greeting.strip() == 'Hello, World!'
assert leading_whitespace_greeting.strip() == greeting_message

# 5. Alphabetical Order (<, >)
# ______________________________
# Strings compare letter by letter, like a dictionary
assert 'apple' < 'banana'
assert 'app' < 'apple'  # a shorter prefix comes first
assert 'Zebra' < 'apple'  # every uppercase letter comes before every lowercase letter

print('All checks passed.')
