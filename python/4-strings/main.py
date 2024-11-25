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

# String using single quotes 
medium_blog = 'Standard SQL will be empowered by "GoogleSQL"'
print(medium_blog)

# String using triple quotes
email = '''
Hi Bruce,

Thank you for the invite. I look forward to meeting you at the event.

Best regards,
John
'''

print(email)


"""
Accessing strings: Strings are indexed like lists and can be accessed in a similar fashion.

It is noted that the start index is inclusive and the end index is exclusive.
"""
title = 'What is pipe syntax in SQL?'

# string_name[index]  => to get the character at the specified index
print('title[0]:', title[0])

# string_name[-index]  => to get the character at the specified index from the end
print('title[-1]:', title[-1])

# string_name[start_index:end_index]
print('title[0:5]:', title[0:5])
print('title[1:-1]:', title[1:-1])

# string_name[start_index:] => to return everything from the start_index through the end of the string
# here, end_index will be the length of the string
print('title[2:]:', title[2:])

# string_name[:end_index] => to return everything from the 0th index through the end_index
# here, start_index will be 0
print('title[:6]:', title[:6])

# string_name[:] => to return all the characters
print('title[:]:', title[:])