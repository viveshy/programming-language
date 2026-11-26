"""
A string (str) is text: a sequence of characters inside quotes.

    ┌────────────┬────────────────────────────────────────┐
    │ Written as │ Quotes                                 │
    ├────────────┼────────────────────────────────────────┤
    │ 'jeans'    │ single quotes                          │
    │ "jeans"    │ double quotes                          │
    │ '''...'''  │ triple quotes: text over several lines │
    └────────────┴────────────────────────────────────────┘

Why it matters: names, words and every line of contest input are strings.
Many interview problems, like palindromes and anagrams, are about them.

We will cover:
1. Single and double quotes
2. Triple quotes: text over several lines
3. Joining with + and repeating with *
4. Indexing: one character
5. Slicing: a piece of the string
6. Slicing with a step: s[::-1]
"""


# ┌────────────────────────────────────────────────────────────┐
# │ 1. SINGLE AND DOUBLE QUOTES                                │
# └────────────────────────────────────────────────────────────┘
# Single and double quotes make exactly the same string.

assert 'jeans' == "jeans"

# To put one kind of quote inside, wrap the string in the other kind.

research_paper = "Google's Pipe Syntax in SQL"
medium_blog = 'Standard SQL will be empowered by "GoogleSQL"'

# Or put a backslash before the quote: \' and \" are quotes inside the string.

assert research_paper == 'Google\'s Pipe Syntax in SQL'
assert medium_blog == "Standard SQL will be empowered by \"GoogleSQL\""


# ┌────────────────────────────────────────────────────────────┐
# │ 2. TRIPLE QUOTES: TEXT OVER SEVERAL LINES                  │
# └────────────────────────────────────────────────────────────┘
# Triple quotes (''' or """) let a string run over several lines.

email = '''Hi Bruce,

Thank you for the invite.

Best regards,
John'''

# It is an ordinary string. Each line break is the newline character, \n.
# \n counts as one character (len() counts characters: 03_string_methods.py).

assert email == 'Hi Bruce,\n\nThank you for the invite.\n\nBest regards,\nJohn'
assert len('a\nb') == 3


# ┌────────────────────────────────────────────────────────────┐
# │ 3. JOINING WITH + AND REPEATING WITH *                     │
# └────────────────────────────────────────────────────────────┘
# + joins two strings into a new one. * repeats a string.

assert 'Mission' + ' Impossible' == 'Mission Impossible'
assert 'ab' * 3 == 'ababab'
assert '-' * 5 == '-----'


# ┌────────────────────────────────────────────────────────────┐
# │ 4. INDEXING: ONE CHARACTER                                 │
# └────────────────────────────────────────────────────────────┘
# Each character has an index: its position. Counting starts at 0.
# s[i] gives the character at index i.

title = 'What is pipe syntax in SQL?'

assert title[0] == 'W'
assert title[1] == 'h'

# Negative indexes count from the end: -1 is the last character.

assert title[-1] == '?'
assert title[-2] == 'L'


# ┌────────────────────────────────────────────────────────────┐
# │ 5. SLICING: A PIECE OF THE STRING                          │
# └────────────────────────────────────────────────────────────┘
# s[start:end] gives the characters from start up to end.
# start is included. end is NOT included.

assert title[0:4] == 'What'
assert title[1:-1] == 'hat is pipe syntax in SQL'

# Leave out start to begin at 0. Leave out end to go to the end.
# s[:] is all of it.

assert title[:4] == 'What'
assert title[8:] == 'pipe syntax in SQL?'
assert title[:] == 'What is pipe syntax in SQL?'

# A slice s[start:end] has end - start characters.

assert len(title[8:12]) == 4  # 'pipe'


# ┌────────────────────────────────────────────────────────────┐
# │ 6. SLICING WITH A STEP: S[::-1]                            │
# └────────────────────────────────────────────────────────────┘
# A third number is the step: s[start:end:step].
# s[::2] takes every 2nd character.

word = 'abcdef'

assert word[::2] == 'ace'
assert word[1::2] == 'bdf'

# A step of -1 walks backwards, so s[::-1] is the string reversed.

assert word[::-1] == 'fedcba'


print('All checks passed.')
