"""
Strings can be compared with the same operators as numbers.

    ┌─────────────────┬──────────────────────────────────────────────┐
    │ Operators       │ What they check                              │
    ├─────────────────┼──────────────────────────────────────────────┤
    │ == and !=       │ same text or not: every character must match │
    │ <, >, <= and >= │ which comes first, character by character    │
    └─────────────────┴──────────────────────────────────────────────┘

Why it matters: checking answers, palindromes and sorting words all compare
strings, and one extra space or capital letter breaks the match.

We will cover:
1. == and != on strings
2. Upper and lower case
3. Spaces count
4. Order: character by character
"""


# ┌────────────────────────────────────────────────────────────┐
# │ 1. == AND != ON STRINGS                                    │
# └────────────────────────────────────────────────────────────┘
# Two strings are equal only when they have the same characters, in the same
# order.

greeting = 'Hello, World!'

assert greeting == 'Hello, World!'
assert greeting != 'Hello, Python!'
assert ('abc' == 'acb') is False  # same letters, different order


# ┌────────────────────────────────────────────────────────────┐
# │ 2. UPPER AND LOWER CASE                                    │
# └────────────────────────────────────────────────────────────┘
# 'H' and 'h' are different characters, so case matters.
# To ignore case, compare lowercase copies made with .lower().

assert 'Hello' != 'hello'
assert 'Hello'.lower() == 'hello'.lower()


# ┌────────────────────────────────────────────────────────────┐
# │ 3. SPACES COUNT                                            │
# └────────────────────────────────────────────────────────────┘
# A space is a character, just like a letter. So is the newline '\n'.
# .strip() removes spaces and newlines from both ends.

padded = '  Hello, World!  '

assert padded != greeting
assert padded.strip() == greeting


# ┌────────────────────────────────────────────────────────────┐
# │ 4. ORDER: CHARACTER BY CHARACTER                           │
# └────────────────────────────────────────────────────────────┘
# < and > compare the first characters. If they are the same, they compare the
# next ones, and so on. The first difference decides.
# If one string runs out first, the shorter one comes first.

assert 'apple' < 'banana'  # 'a' < 'b'
assert 'apple' < 'apricot'  # 'a' and 'p' match, then 'p' < 'r'
assert 'app' < 'apple'  # 'app' ran out first

# Each character has a number, its code, and ord() gives it. Comparing two
# characters compares their codes:
# - '0' to '9' are 48 to 57
# - 'A' to 'Z' are 65 to 90
# - 'a' to 'z' are 97 to 122

assert ord('A') == 65
assert ord('a') == 97


print('All checks passed.')
