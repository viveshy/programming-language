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

# String using double quotes
research_paper = "Google's Pipe Syntax in SQL"
print(research_paper)
# Expected Output: Google's Pipe Syntax in SQL

# String using single quotes 
medium_blog = 'Standard SQL will be empowered by "GoogleSQL"'
print(medium_blog)
# Expected Output: Standard SQL will be empowered by "GoogleSQL"

# String using triple quotes
email = '''
Hi Bruce,

Thank you for the invite. I look forward to meeting you at the event.

Best regards,
John
'''

print(email)
# Expected Output:
# Hi Bruce,
#
# Thank you for the invite. I look forward to meeting you at the event.
#
# Best regards,
# John


"""
Accessing strings: Strings are indexed like lists and can be accessed in a similar fashion.

It is noted that the start index is inclusive and the end index is exclusive.
"""
title = 'What is pipe syntax in SQL?'

# string_name[index]  => to get the character at the specified index
print('title[0]:', title[0])
# Expected Output: title[0]: W

# string_name[-index]  => to get the character at the specified index from the end
print('title[-1]:', title[-1])
# Expected Output: title[-1]: ?

# string_name[start_index:end_index]
print('title[0:10]:', title[0:10])
# Expected Output: title[0:10]: What is pi
print('title[1:-1]:', title[1:-1])
# Expected Output: title[1:-1]: hat is pipe syntax in SQL

# string_name[start_index:] => to return everything from the start_index through the end of the string
# here, end_index will be the length of the string
print('title[2:]:', title[2:])
# Expected Output: title[2:]: at is pipe syntax in SQL?

# string_name[:end_index] => to return everything from the 0th index through the end_index
# here, start_index will be 0
print('title[:6]:', title[:6])
# Expected Output: title[:6]: What i

# string_name[:] => to return all the characters
print('title[:]:', title[:])
# Expected Output: title[:]: What is pipe syntax in SQL?

