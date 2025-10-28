"""
Join in Python is a string method that combines elements of an iterable (like a list) into a single string.

The join() method takes an iterable as an argument and returns a string that is the concatenation 
of the strings in the iterable. The string whose method is called is inserted in between each given string.

Syntax: separator.join(iterable)

Key Points:
- The separator is the string that will be inserted between each element
- The iterable can be a list, tuple, or any sequence of strings
- All elements in the iterable must be strings (or convertible to strings)
- join() is more efficient than concatenating strings with + in loops
"""

# Example list of words
words = ['Python', 'is', 'awesome']

# Join with space separator
sentence = ' '.join(words)
print('Joined with space:', sentence)
# Expected Output: Joined with space: Python is awesome

# Join with different separators
print('Joined with comma:', ', '.join(words))
# Expected Output: Joined with comma: Python, is, awesome
print('Joined with hyphen:', '-'.join(words))
# Expected Output: Joined with hyphen: Python-is-awesome
print('Joined with no separator:', ''.join(words))
# Expected Output: Joined with no separator: Pythonisawesome

# Join numbers (need to convert to strings first)
numbers = [1, 2, 3, 4, 5]
number_string = '-'.join(map(str, numbers))
print('Numbers joined:', number_string)
# Expected Output: Numbers joined: 1-2-3-4-5

# Join characters of a string (reverse operation of split)
text = "hello"
chars = list(text)
print('Characters as list:', chars)
# Expected Output: Characters as list: ['h', 'e', 'l', 'l', 'o']
rejoined = ''.join(chars)
print('Rejoined string:', rejoined)
# Expected Output: Rejoined string: hello

# Practical example: Building file paths
path_parts = ['home', 'user', 'documents', 'file.txt']
file_path = '/'.join(path_parts)
print('File path:', file_path)
# Expected Output: File path: home/user/documents/file.txt

# Join with newlines for multi-line output
lines = ['First line', 'Second line', 'Third line']
multi_line = '\n'.join(lines)
print('Multi-line output:')
print(multi_line)
# Expected Output: 
# Multi-line output:
# First line
# Second line
# Third line

# Using join to reverse a string
original = "python"
reversed_string = ''.join(reversed(original))
print('Original:', original)
# Expected Output: Original: python
print('Reversed using join:', reversed_string)
# Expected Output: Reversed using join: nohtyp