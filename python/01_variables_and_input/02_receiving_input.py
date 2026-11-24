"""
The built-in function used for receiving input is 'input'.
Remember, input is always received as a string (str), even when you type a number.

Run this file yourself and type something when it asks.
"""

# Prompt the user to enter their name
name = input('Enter your name here:\n')
# User input example: John

# Display the entered name
print('The entered name is: ' + name)

# Whatever was typed, input() hands it back as a string
assert type(name) is str

# input() removes the Enter key (the newline) from the end of what you typed
assert '\n' not in name

# Typing 1990 gives you the string '1990', not the number 1990.
# Adding two strings joins them instead of doing arithmetic:
assert '1990' + '1' == '19901'
# (03_type_conversion.py shows how to turn '1990' into the number 1990)

print('All checks passed.')
