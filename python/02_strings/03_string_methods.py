"""
String methods in Python are case sensitive and do not change the original string.
We will discuss the following string methods and functions:

Functions:
    1) len() - Returns the length of the string.

Methods:
    1) .upper() - Converts all characters in the string to uppercase.
    2) .lower() - Converts all characters in the string to lowercase.
    3) .find('string_to_look_up') - Returns the index of the first occurrence of the specified substring.
    4) .replace('old_string', 'new_string') - Replaces occurrences of the old substring with the new substring.
    5) 'string-sequence' in string_variable - Returns a boolean indicating whether the specified substring is present in the string.
    6) .strip(), .lstrip(), .rstrip() - Remove spaces and newlines from the ends of the string,
       or the characters you name, like .strip('-').
    7) .isdigit(), .isnumeric(), .isalpha(), .isalnum() - Check what kind of characters the string has.
"""

movie = 'Mission Impossible'

# 1. LENGTH
# _______________
# The space counts too: 7 letters + 1 space + 10 letters
assert len(movie) == 18

# 2. UPPER AND LOWER
# _______________
assert movie.upper() == 'MISSION IMPOSSIBLE'
assert movie.lower() == 'mission impossible'

# Methods return a new string; the original is unchanged
assert movie == 'Mission Impossible'

# 3. FIND
# _______________
assert movie.find('ssion') == 2
assert movie.find('z') == -1  # -1 means "not found"

# 4. REPLACE
# _______________
assert movie.replace('Imp', 'IMP') == 'Mission IMPossible'

# 5. IN
# _______________
assert ('ssion' in movie) is True
assert ('zz' in movie) is False
assert ('mission' in movie) is False  # case sensitive: 'M' is not 'm'

# 6. STRIP
# _______________
# Removes spaces, tabs and newlines from both ends (never from the middle).
# This is how stray spaces and the newline at the end of a line of input get removed.
assert '  hi there \n'.strip() == 'hi there'
assert '  hi '.lstrip() == 'hi '  # left end only
assert '  hi '.rstrip() == '  hi'  # right end only
assert '--hi--'.strip('-') == 'hi'  # name the characters to remove
assert 'xyhiyx'.strip('xy') == 'hi'  # each character in 'xy' is removed, in any order

# 7. CHARACTER CHECKS
# _______________
test_string = 'abc123'

assert '123'.isdigit() is True
assert '123'.isnumeric() is True
assert 'abc'.isalpha() is True
assert test_string.isalnum() is True  # letters and digits only
assert '-5'.isdigit() is False  # the minus sign is not a digit

print('All checks passed.')
