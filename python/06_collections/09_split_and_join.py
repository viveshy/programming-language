"""
split() and join() convert between a string and a list of strings:
- text.split(separator)  : string -> list of strings
- separator.join(items)  : list of strings -> string

join() takes an iterable as an argument and returns a string that is the
concatenation of the strings in the iterable. The string whose method is
called is inserted in between each given string.

Key Points:
- The separator is the string that will be inserted between each element
- The iterable can be a list, tuple, or any sequence of strings
- All elements in the iterable must be strings (convert numbers first)
- join() is more efficient than concatenating strings with + in loops
"""

# 1. SPLIT
# __________
assert 'Python is awesome'.split() == ['Python', 'is', 'awesome']

# With no argument, split() cuts on any run of spaces, tabs or newlines,
# and ignores them at the ends
assert 'a  b'.split() == ['a', 'b']
assert '  3 1\t2\n'.split() == ['3', '1', '2']

# With a separator, every single separator counts, so empty pieces can appear
assert 'a,,b'.split(',') == ['a', '', 'b']
assert '2026-11-24'.split('-') == ['2026', '11', '24']

# 2. TURNING A LINE OF TEXT INTO NUMBERS
# __________
# A line typed as '3 1 2' arrives as ONE string. split() cuts it into pieces,
# and map(int, pieces) applies int() to every piece.
line = '3 1 2'
numbers = list(map(int, line.split()))
assert numbers == [3, 1, 2]

# map can also feed unpacking directly
a, b, c = map(int, line.split())
assert a + b + c == 6

# 3. JOIN
# __________
words = ['Python', 'is', 'awesome']

assert ' '.join(words) == 'Python is awesome'
assert ', '.join(words) == 'Python, is, awesome'
assert '-'.join(words) == 'Python-is-awesome'
assert ''.join(words) == 'Pythonisawesome'

# 4. JOINING NUMBERS
# __________
# join only accepts strings...
try:
    '-'.join([1, 2, 3])
    worked = True
except TypeError:
    worked = False

assert worked is False

# ...so turn each number into a string first with map(str, ...)
numbers = [1, 2, 3, 4, 5]
assert '-'.join(map(str, numbers)) == '1-2-3-4-5'

# The usual way to print a list of numbers on one line, separated by spaces
assert ' '.join(map(str, [3, 1, 2])) == '3 1 2'

# 5. MORE JOIN EXAMPLES
# __________
# Characters of a string
chars = list('hello')
assert chars == ['h', 'e', 'l', 'l', 'o']
assert ''.join(chars) == 'hello'

# Building file paths
path_parts = ['home', 'user', 'documents', 'file.txt']
assert '/'.join(path_parts) == 'home/user/documents/file.txt'

# Join with newlines for multi-line output
lines = ['First line', 'Second line', 'Third line']
multi_line = '\n'.join(lines)
print(multi_line)
assert multi_line == 'First line\nSecond line\nThird line'
assert multi_line.split('\n') == lines  # split undoes join

# Reversing a string
assert ''.join(reversed('python')) == 'nohtyp'

print('All checks passed.')
