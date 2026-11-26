"""
input() waits for the user to type a line, then gives it back as a string.

Why it matters: input() always gives a string, even when you type a number.
In a contest, every number you read starts as text.

We will cover:
1. input(): reading one line
2. The Enter key is removed
3. Numbers arrive as text

Run this file yourself and type something when it asks.
"""


# ┌────────────────────────────────────────────────────────────┐
# │ 1. INPUT(): READING ONE LINE                               │
# └────────────────────────────────────────────────────────────┘
# input() pauses the program until you type a line and press Enter.
# The text in the brackets is a prompt, printed first to say what to type.

name = input('Enter your name here:\n')  # say you type John

print('The entered name is: ' + name)

# Whatever you type, input() gives it back as a str.

assert type(name) is str


# ┌────────────────────────────────────────────────────────────┐
# │ 2. THE ENTER KEY IS REMOVED                                │
# └────────────────────────────────────────────────────────────┘
# Pressing Enter adds a newline character, '\n', at the end of the line.
# input() removes it, so name holds only what you typed.
# x not in s asks: is x missing from s? (in: 02_strings/03_string_methods.py)

assert '\n' not in name

# Only the newline is removed. Spaces you type before or after are kept.


# ┌────────────────────────────────────────────────────────────┐
# │ 3. NUMBERS ARRIVE AS TEXT                                  │
# └────────────────────────────────────────────────────────────┘
# Typing 1990 gives you the string '1990', not the number 1990.
# + on two strings joins them instead of adding.

assert '1990' + '1' == '19901'

# 03_type_conversion.py shows how to turn '1990' into the number 1990.


print('All checks passed.')
