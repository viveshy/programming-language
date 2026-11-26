# Strings: summary

Read this after the lessons, and again before a contest or an interview.
Each lesson has two parts:

- **Tips to remember:** the facts and the mistakes to avoid, with the reason.
- **What to expect in CP/DSA:** where the topic shows up in competitive
  programming (CP) and in the data structures and algorithms (DSA) problems of
  coding interviews.

Practice problems for this folder are in [problems.md](problems.md).

## 1. Strings

Lesson: [01_strings.py](01_strings.py)

### Tips to remember

- `'jeans'` and `"jeans"` make the same string.
- `'Google's'` is a SyntaxError, because the string ends at the second quote.
  Wrap it in the other kind of quote, `"Google's"`, or put a backslash before
  the quote: `'Google\'s'`.
- Triple quotes (`'''` or `"""`) make a string over several lines, with the
  newline `\n` at each line break. It is one character: `len('a\nb') == 3`.
- `+` joins strings and `*` repeats them: `'ab' * 3 == 'ababab'`.
- `+` never mixes text and numbers: `'Room ' + 5` is a TypeError. Turn the
  number into text first: `'Room ' + str(5) == 'Room 5'`.
- Indexes start at 0, and `s[-1]` is the last character. An index past the end
  stops with an IndexError: `title = 'What is pipe syntax in SQL?'` has 27
  characters, so its last index is 26 and `title[27]` crashes.
- Strings never change: `title[0] = 'w'` is a TypeError. Build a new string
  instead: `'w' + title[1:]`.
- `s[start:end]` includes start but not end, so it has `end - start`
  characters. Leave out start to begin at 0, or end to go to the end.
- A slice past the end does not crash, unlike an index. It quietly gives fewer
  characters, or `''`, which can hide a bug: `title[20:100] == 'in SQL?'` and
  `title[50:] == ''`.
- `s[::-1]` is s reversed, because a step of -1 walks backwards.
- With a negative step, start must be the bigger index. With
  `word = 'abcdef'`, `word[4:1:-1] == 'edc'`, but `word[1:4:-1] == ''`,
  because walking backwards from 1 never reaches 4.

### What to expect in CP/DSA

- Python has no separate character type: a character is a string of length 1,
  like `'a'`, `'7'` or `' '`.
- The kind of quote rarely matters. Pick one and use it everywhere.
- `'-' * n` or `'.' * n` builds a row of n characters, for patterns and grids.
- To build a long answer, collect the pieces in a list and join them once,
  because many `+` on a string can be slow. `print('\n'.join(lines))` prints
  many lines at once (06_collections/09_split_and_join.py).
- When each position has a meaning, index it directly: in `'a1'`, `s[0]` is the
  letter and `s[1]` the digit. It is still text, so `int(s[1])` gives a number.
- To change characters, make the string a list (06_collections/01_lists.py).
- A slice copies its characters, so it is not free: `s[i:j]` takes about
  `j - i` steps. Slicing inside a loop can be slow.
- `s[i:] + s[:i]` moves the first i characters to the end: a rotation of s.
  Trying every i (a loop, 05_loops) gives every rotation.
- `s == s[::-1]` checks for a palindrome (the same both ways). To reverse each
  word of a sentence, split it into words first
  (06_collections/09_split_and_join.py), then use `[::-1]` on each.

## 2. Formatted strings

Lesson: [02_formatted_strings.py](02_formatted_strings.py)

### Tips to remember

- Put `f` before the quotes and values in `{}`: with `first_name = 'John'`,
  `f'Hi {first_name}' == 'Hi John'`. Numbers become text, with no `str()`.
- Without the `f`, nothing is replaced: `'Hi {first_name}'` keeps the braces as
  plain text.
- Anything in `{}` is worked out first, then becomes text: `f'{2 + 3}' == '5'`.
- On Python 3.10, which many judges run, `{}` can't use the same quote as the
  outside of the f-string: `f'{first_name + '!'}'` is a SyntaxError there.
  Python 3.12 allows it. Use the other kind: `f'{first_name + "!"}'`.
- `f'{lo=}'` gives the name and the value, like `'lo=3'`, for debugging.

A format code goes after a colon in `{}`:

| Code | Gives | Remember |
|---|---|---|
| `f'{2.678:.2f}'` | `'2.68'` | 2 digits after the decimal point, rounded to the nearest (not cut) |
| `f'{7:.2f}'` | `'7.00'` | it adds zeros, and an integer works too |
| `f'{5:02d}'` | `'05'` | an integer with at least 2 digits, zeros in front (`123` stays `'123'`) |
| `f'{5:b}'` | `'101'` | an integer in binary (base 2): 5 = 4 + 1 |
| `f'{5:08b}'` | `'00000101'` | binary, padded with zeros to 8 digits |
| `bin(5)` | `'0b101'` | the built-in adds `'0b'` in front |

- `round()` gives a number, and a number drops zeros at the end: if the judge
  expects `2.50`, `print(round(2.5, 2))` prints `2.5`, a Wrong Answer. For
  fixed decimals, write `f'{2.5:.2f}'`, which gives `'2.50'`.
- A float is often stored a tiny bit off: the float 2.675 is really about
  2.67499999..., so `f'{2.675:.2f}'` rounds down to `'2.67'`.
- `d` and `b` work only on integers. `f'{10 / 2:02d}'` stops with a ValueError,
  because `/` gives the float `5.0`. `f'{10 // 2:02d}'` works, because `//`
  keeps it an integer.

### What to expect in CP/DSA

- Output with labels: `print(f'Case #{t}: {answer}')`. An answer like the range
  `'0->2'` is `f'{a}->{b}'`.
- Remove debug prints like `print(f'{x=}')` before you submit: the judge reads
  all your output.
- "Print the answer with 6 digits after the decimal point" means
  `print(f'{ans:.6f}')`.
- Judges usually accept a small error, like `10**-6`, so print enough digits.
- LeetCode returns numbers, not text, so you rarely format decimals there.
- Times and dates: `f'{h}:{m:02d}'` gives `'7:05'`, not `'7:5'`.
- `f'{n:b}'` gives the bits of n as text.

## 3. String methods

Lesson: [03_string_methods.py](03_string_methods.py)

### Tips to remember

- A string method never changes the string: it returns a new one. So
  `movie.upper()` on its own line throws the result away. Store what it
  returns: `shout = movie.upper()`.
- Searching is case sensitive, because `'M'` is not `'m'`: with
  `movie = 'Mission Impossible'`, `'mission' in movie` is False. Search in
  `movie.lower()` instead.
- `find()` gives -1 when the text is missing, not an error. But -1 is also an
  index, the last character: `movie[movie.find('z')]` quietly gives `'e'`.
  Check for -1 before you use what `find()` gave you.
- `replace()` swaps every match, not just the first:
  `'banana'.replace('a', 'o') == 'bonono'`. `count()` counts the matches.
- `strip()` removes characters from the two ends only, never from the middle.
- `strip('ing')` does not remove the ending `'ing'`. It removes any mix of
  `'i'`, `'n'` and `'g'` from the ends: `'running'.strip('ing') == 'ru'`, not
  `'runn'`. `removesuffix('ing')` removes an exact ending.

The three digit checks:

| Method | What it accepts |
|---|---|
| `isdecimal()` | 0-9 and other decimal digit characters, like `'٣'` |
| `isdigit()` | decimal digits + special digits like `'²'` |
| `isnumeric()` | digits + fractions like `'½'` + other numeric characters |

- Every `isdecimal()` character is also `isdigit()` and `isnumeric()`. Every
  `isdigit()` character is also `isnumeric()`.
- None of them accepts a minus sign, a decimal point or an empty string, yet
  `int('-5')` works: `'-5'.isdigit()` is False. So `isdigit()` can't tell you
  if `int()` will work.

### What to expect in CP/DSA

- `len(s)` is the n in most string problems. It is instant, even on a huge
  string, because Python stores the length.
- To compare text without caring about capitals, `lower()` both sides first.
  Comparing a word with `word.upper()` tells you if it is all capitals.
- `in`, `find()` and `count()` read the whole string: about `len(s)` steps.
- Usual patterns: `ch in allowed` for each character, `find()` to know where
  to cut (-1: leave the text as it is), and `count()` for each letter.
- `replace()` deletes or swaps characters before you work on the text.
- `s = input().strip()` reads a word or a line without stray spaces.
  `sys.stdin.readline()` keeps the `'\n'` at the end, and `strip()` removes it.
- `rstrip()` first when the spaces at the end must not count.
- `isdigit()` is enough, because contest input uses only the plain digits 0-9,
  where all three checks agree.
- To clean text, keep only the `isalnum()` characters, in `lower()`.
  `isdigit()` tells a number like `'42'` apart from a word like `'abc'`.
