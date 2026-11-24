"""
Strings in Python can be written using:
- double quotes
- single quotes
- triple quotes

FOR DOUBLE AND SINGLE QUOTES:
If we use double quotes for strings, we can use single quotes in the middle of the string to be part of the string and vice-versa.

FOR TRIPLE QUOTES:
We use triple quotes to define multi-line strings. For example, an email is often written using triple quotes in Python.
"""

# 1. SINGLE AND DOUBLE QUOTES
# _____________________________
# Both kinds of quotes make exactly the same string
assert 'jeans' == "jeans"

# Double quotes let a single quote sit inside the string...
research_paper = "Google's Pipe Syntax in SQL"
# ...and single quotes let double quotes sit inside it
medium_blog = 'Standard SQL will be empowered by "GoogleSQL"'

# A backslash also lets you put the same quote inside
assert 'Google\'s' == "Google's"

# 2. TRIPLE QUOTES
# _____________________________
email = '''Hi Bruce,

Thank you for the invite. I look forward to meeting you at the event.

Best regards,
John'''

print(email)

# A triple-quoted string is an ordinary string with newline characters (\n) in it
assert email == 'Hi Bruce,\n\nThank you for the invite. I look forward to meeting you at the event.\n\nBest regards,\nJohn'

"""
Accessing strings: Strings are indexed like lists and can be accessed in a similar fashion.

It is noted that the start index is inclusive and the end index is exclusive.
"""

# 3. INDEXING AND SLICING
# _____________________________
title = 'What is pipe syntax in SQL?'

# string_name[index]  => the character at that index (counting starts at 0)
assert title[0] == 'W'

# string_name[-index]  => counts from the end
assert title[-1] == '?'

# string_name[start_index:end_index] => end_index itself is not included
assert title[0:10] == 'What is pi'
assert title[1:-1] == 'hat is pipe syntax in SQL'

# string_name[start_index:] => from start_index through the end of the string
assert title[2:] == 'at is pipe syntax in SQL?'

# string_name[:end_index] => from index 0 up to (not including) end_index
assert title[:6] == 'What i'

# string_name[:] => all the characters
assert title[:] == 'What is pipe syntax in SQL?'

print('All checks passed.')
