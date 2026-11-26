"""
An f-string is a string with f before the quotes. Values in {} are put into it.

    ┌────────────────┬─────────────────────────────────────────────────────┐
    │ Code           │ Gives                                               │
    ├────────────────┼─────────────────────────────────────────────────────┤
    │ f'{name}'      │ the value of name, as text                          │
    │ f'{2 + 3}'     │ the result, as text: '5'                            │
    │ f'{price:.2f}' │ price with exactly 2 digits after the decimal point │
    │ f'{m:02d}'     │ m with at least 2 digits, padded with zeros         │
    └────────────────┴─────────────────────────────────────────────────────┘

Why it matters: contest output must match the expected text exactly, often
with a fixed number of decimal places. f-strings build that text.

We will cover:
1. Values in curly braces
2. Expressions in curly braces
3. Decimal places, rounded
4. Padding with zeros, and binary
"""


# ┌────────────────────────────────────────────────────────────┐
# │ 1. VALUES IN CURLY BRACES                                  │
# └────────────────────────────────────────────────────────────┘
# Put f before the quotes. Each {name} is replaced by its value, as text.

first_name = 'John'
last_name = 'Smith'

message = f'{first_name} [{last_name}] is a coder.'
assert message == 'John [Smith] is a coder.'

# Numbers are turned into text for you. No str() needed.

age = 30
assert f'{first_name} is {age}' == 'John is 30'


# ┌────────────────────────────────────────────────────────────┐
# │ 2. EXPRESSIONS IN CURLY BRACES                             │
# └────────────────────────────────────────────────────────────┘
# Anything inside {} is worked out first, then turned into text.

assert f'{2 + 3}' == '5'
assert f'{first_name} has {len(first_name)} letters' == 'John has 4 letters'


# ┌────────────────────────────────────────────────────────────┐
# │ 3. DECIMAL PLACES, ROUNDED                                 │
# └────────────────────────────────────────────────────────────┘
# :.2f after a value means "show exactly 2 digits after the decimal point".

price = 3.14159

assert f'{price:.2f}' == '3.14'
assert f'{price:.4f}' == '3.1416'

# It ROUNDS to the nearest. It does not cut: 2.678 becomes 2.68, not 2.67.

assert f'{2.678:.2f}' == '2.68'

# It adds zeros when needed. An integer works too.

assert f'{7:.2f}' == '7.00'


# ┌────────────────────────────────────────────────────────────┐
# │ 4. PADDING WITH ZEROS, AND BINARY                          │
# └────────────────────────────────────────────────────────────┘
# :02d shows an integer with at least 2 digits, adding zeros in front.
# d means a decimal integer. A longer number is never cut.

assert f'{5:02d}' == '05'
assert f'{123:02d}' == '123'

# :b writes an integer in binary (base 2, digits 0 and 1): 5 = 4 + 1 = 101.
# :08b also pads it with zeros to 8 digits. bin() adds '0b' in front.

assert f'{5:b}' == '101'
assert f'{5:08b}' == '00000101'
assert bin(5) == '0b101'


print('All checks passed.')
