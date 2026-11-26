"""
split() and join() convert between a string and a list of strings.

    ┌──────────────────────┬────────────┬─────────────────────────────────┐
    │ Code                 │ Gives      │ What it does                    │
    ├──────────────────────┼────────────┼─────────────────────────────────┤
    │ 'a b'.split()        │ ['a', 'b'] │ cut at spaces                   │
    │ 'a,b'.split(',')     │ ['a', 'b'] │ cut at each ','                 │
    │ ' '.join(['a', 'b']) │ 'a b'      │ glue together, with ' ' between │
    └──────────────────────┴────────────┴─────────────────────────────────┘

Why it matters: contest input arrives as lines of text, and answers go out as
text. split() reads a line of numbers. join() prints a list on one line.

We will cover:
1. split() with no argument
2. split(sep) with a separator
3. A line of text -> numbers with map(int, ...)
4. join()
5. Joining numbers with map(str, ...)
6. More join examples
"""


# ┌────────────────────────────────────────────────────────────┐
# │ 1. SPLIT() WITH NO ARGUMENT                                │
# └────────────────────────────────────────────────────────────┘
# text.split() cuts a string into words. It gives back a list of strings.

assert 'Python is awesome'.split() == ['Python', 'is', 'awesome']

# With no argument, it cuts at any run of spaces, tabs (\t) or newlines (\n),
# and ignores them at both ends.

assert 'a   b'.split() == ['a', 'b']
assert '  3 1\t2\n'.split() == ['3', '1', '2']


# ┌────────────────────────────────────────────────────────────┐
# │ 2. SPLIT(SEP) WITH A SEPARATOR                             │
# └────────────────────────────────────────────────────────────┘
# text.split(sep) cuts at every sep. Each single sep counts, so two in a row
# leave an empty piece '' between them.

assert '2026-11-24'.split('-') == ['2026', '11', '24']
assert 'a,,b'.split(',') == ['a', '', 'b']


# ┌────────────────────────────────────────────────────────────┐
# │ 3. A LINE OF TEXT -> NUMBERS WITH MAP(INT, ...)            │
# └────────────────────────────────────────────────────────────┘
# A line typed as 3 1 2 arrives as ONE string. split() cuts it into pieces.
# map(int, pieces) applies int() to every piece. list() collects the results.

line = '3 1 2'  # what input() gives for the line 3 1 2
numbers = list(map(int, line.split()))
assert numbers == [3, 1, 2]

# When you know how many numbers the line holds, unpack them straight away.

a, b, c = map(int, line.split())
assert a + b + c == 6


# ┌────────────────────────────────────────────────────────────┐
# │ 4. JOIN()                                                  │
# └────────────────────────────────────────────────────────────┘
# sep.join(items) glues the strings in items together, with sep between each
# two. join is called on the separator, not on the list.

words = ['Python', 'is', 'awesome']

assert ' '.join(words) == 'Python is awesome'
assert ', '.join(words) == 'Python, is, awesome'
assert ''.join(words) == 'Pythonisawesome'  # nothing between

# items can be anything you can loop over that gives strings: a tuple, or a
# string (its characters).

assert '-'.join(('a', 'b')) == 'a-b'
assert '-'.join('abc') == 'a-b-c'


# ┌────────────────────────────────────────────────────────────┐
# │ 5. JOINING NUMBERS WITH MAP(STR, ...)                      │
# └────────────────────────────────────────────────────────────┘
# join() accepts strings only. map(str, numbers) turns each number into a
# string first.

numbers = [1, 2, 3]
assert '-'.join(map(str, numbers)) == '1-2-3'
assert ' '.join(map(str, numbers)) == '1 2 3'


# ┌────────────────────────────────────────────────────────────┐
# │ 6. MORE JOIN EXAMPLES                                      │
# └────────────────────────────────────────────────────────────┘
# list(text) splits a string into its characters. ''.join() glues them back.

chars = list('hello')
assert chars == ['h', 'e', 'l', 'l', 'o']
assert ''.join(chars) == 'hello'

# '/'.join() builds a path. '\n'.join() puts each item on its own line.

assert '/'.join(['home', 'user', 'file.txt']) == 'home/user/file.txt'

lines = ['First line', 'Second line']
text = '\n'.join(lines)
assert text == 'First line\nSecond line'
assert text.split('\n') == lines  # split undoes the join

# reversed(text) gives the characters from last to first. ''.join() makes them
# a string again.

assert ''.join(reversed('python')) == 'nohtyp'


print('All checks passed.')
