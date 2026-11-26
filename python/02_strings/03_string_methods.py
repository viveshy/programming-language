"""
A string method is a function you call with a dot after a string: s.upper().

    ┌──────────────────────┬────────────────────────────────────────────────┐
    │ Code                 │ What it gives                                  │
    ├──────────────────────┼────────────────────────────────────────────────┤
    │ len(s)               │ how many characters (a function, not a method) │
    │ s.upper(), s.lower() │ all capitals, all small letters                │
    │ x in s               │ is x somewhere in s? True or False             │
    │ s.find(x)            │ the index where x first starts, or -1          │
    │ s.count(x)           │ how many times x appears                       │
    │ s.replace(old, new)  │ every old swapped for new                      │
    │ s.strip()            │ s without spaces and newlines at the two ends  │
    │ s.isalpha(), ...     │ what kind of characters s has                  │
    └──────────────────────┴────────────────────────────────────────────────┘

Why it matters: most string problems clean, search or count text. These do it
in one call.

We will cover:
1. len(): counting characters
2. upper() and lower()
3. Searching: in, find() and count()
4. replace()
5. strip(): removing characters from the ends
6. Character checks: isalpha(), isalnum(), isdigit(), ...
"""


# ┌────────────────────────────────────────────────────────────┐
# │ 1. LEN(): COUNTING CHARACTERS                              │
# └────────────────────────────────────────────────────────────┘
# len(s) gives how many characters s has. Spaces count too.
# It is a function, so the string goes inside the brackets: len(movie).

movie = 'Mission Impossible'

assert len(movie) == 18  # 7 letters + 1 space + 10 letters
assert len('') == 0  # the empty string

# The last index is always len(s) - 1 (indexes: 01_strings.py).

assert movie[len(movie) - 1] == 'e'


# ┌────────────────────────────────────────────────────────────┐
# │ 2. UPPER() AND LOWER()                                     │
# └────────────────────────────────────────────────────────────┘
# upper() gives all capitals. lower() gives all small letters.
# Other characters, like spaces and digits, stay as they are.

assert movie.upper() == 'MISSION IMPOSSIBLE'
assert movie.lower() == 'mission impossible'
assert 'abc123'.upper() == 'ABC123'

# A string method never changes the string. It returns a new string.

assert movie == 'Mission Impossible'  # upper() and lower() left it as it was


# ┌────────────────────────────────────────────────────────────┐
# │ 3. SEARCHING: IN, FIND() AND COUNT()                       │
# └────────────────────────────────────────────────────────────┘
# x in s asks: does the text x appear in s? It gives True or False.

assert ('ssion' in movie) is True
assert ('zz' in movie) is False

# s.find(x) gives the index where x first starts.
# It gives -1 when x is missing. It does not raise an error.

assert movie.find('ssion') == 2
assert movie.find('z') == -1

# s.count(x) gives how many times x appears.

assert movie.count('s') == 4
assert movie.count('z') == 0


# ┌────────────────────────────────────────────────────────────┐
# │ 4. REPLACE()                                               │
# └────────────────────────────────────────────────────────────┘
# s.replace(old, new) swaps EVERY old for new and returns the new string.

assert movie.replace('Imp', 'IMP') == 'Mission IMPossible'
assert 'banana'.replace('a', 'o') == 'bonono'  # all of them, not just the first

# Replacing with '' deletes.

assert '1,000,000'.replace(',', '') == '1000000'


# ┌────────────────────────────────────────────────────────────┐
# │ 5. STRIP(): REMOVING CHARACTERS FROM THE ENDS              │
# └────────────────────────────────────────────────────────────┘
# strip() removes spaces, tabs and newlines from both ends, never the middle.
# lstrip() does only the left end. rstrip() does only the right end.

assert '  hi there \n'.strip() == 'hi there'
assert '  hi '.lstrip() == 'hi '
assert '  hi '.rstrip() == '  hi'

# Name the characters to remove inside the brackets.

assert '--hi--'.strip('-') == 'hi'


# ┌────────────────────────────────────────────────────────────┐
# │ 6. CHARACTER CHECKS: ISALPHA(), ISALNUM(), ISDIGIT(), ...  │
# └────────────────────────────────────────────────────────────┘
# These give True only if EVERY character in the string passes:
# - isalpha(): letters only
# - isalnum(): letters and digits only

assert 'abc'.isalpha() is True
assert 'abc123'.isalpha() is False
assert 'abc123'.isalnum() is True

# Three methods check for digits. For the plain digits 0-9 they all agree.

assert '123'.isdecimal() is True
assert '123'.isdigit() is True
assert '123'.isnumeric() is True

# They differ only on special characters.

assert '²'.isdecimal() is False  # superscript two
assert '²'.isdigit() is True
assert '²'.isnumeric() is True

assert '½'.isdecimal() is False
assert '½'.isdigit() is False
assert '½'.isnumeric() is True

assert '٣'.isdecimal() is True  # the Arabic-Indic digit three: a decimal digit


print('All checks passed.')
