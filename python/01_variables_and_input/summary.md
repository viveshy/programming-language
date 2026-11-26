# Variables and input: summary

Read this after the lessons, and again before a contest or an interview.
Each lesson has two parts:

- **Tips to remember:** the facts and the mistakes to avoid, with the reason.
- **What to expect in CP/DSA:** where the topic shows up in competitive
  programming (CP) and in the data structures and algorithms (DSA) problems of
  coding interviews.

Practice problems for this folder are in [problems.md](problems.md).

## 1. Variables

Lesson: [01_variables.py](01_variables.py)

### Tips to remember

- `assert` checks a fact. If it is true, Python moves on. If it is false, the
  program stops with an `AssertionError` that shows the line.
- `=` stores a value and `==` compares two values. So `assert price = 80` is a
  SyntaxError: write `assert price == 80`.
- A new `=` replaces the old value. Names are case sensitive: `price` and
  `Price` are two different variables.
- `type(x)` gives the type of a value:

| Type | Examples | Remember |
|---|---|---|
| `int` | `100`, `-7` | an integer: no decimal point |
| `float` | `10.5`, `100.0` | a decimal point makes a float, even `.0` |
| `str` | `'jeans'`, `'7'` | text in quotes, even when it is digits |
| `bool` | `True`, `False` | a capital letter, and no quotes |

- `100 == 100.0` is True, but the types differ: `100.0` is a float.
- `'7'` is text, so `'7' == 7` is False.
- `true` with a small t is a NameError: Python looks for a variable called
  `true`. `'True'` in quotes is a str, not a bool.

### What to expect in CP/DSA

- Every solution keeps its input in variables: `n`, `k`, `s`. Short names are
  normal in contests. In interviews, use clear names.
- Most answers are integers. Use a float only when the problem has decimals:
  printing `100.0` when the judge expects `100` is a Wrong Answer.
- Many LeetCode functions return a bool. Contest judges usually want text
  instead, like `YES` or `NO`, and printing `True` there is a Wrong Answer.
- Test your code on small cases before you submit; `assert` is a quick way.
  On a judge, a failed assert stops your program: a Runtime Error.
- Many interview problems are about strings: palindromes, anagrams.

## 2. Receiving input

Lesson: [02_receiving_input.py](02_receiving_input.py)

### Tips to remember

- `input()` always gives back a str, even when you type a number.
- `input()` removes the Enter key (the newline `'\n'`) from the end. Spaces you
  type stay.
- `+` on two strings joins them: `'1990' + '1' == '19901'`.
- Text compares character by character, not by value: `'10' < '9'` is True,
  because `'1'` comes before `'9'`. Convert to int first.

### What to expect in CP/DSA

- In a contest, call `input()` with no prompt. The judge reads everything you
  print, so a prompt like `'Enter n:'` becomes part of your answer: Wrong
  Answer.
- Input is read one line at a time: `line = input()`. One integer is
  `n = int(input())`. Several numbers on one line need `split()` first
  (06_collections/09_split_and_join.py).
- For a word or a line of text, `input().strip()` also drops stray spaces.
- For very big inputs, `sys.stdin.readline()` is faster than `input()`, but it
  keeps the `'\n'` at the end. Strip it.
- LeetCode never uses `input()`. It calls your function with the values ready.

## 3. Type conversion

Lesson: [03_type_conversion.py](03_type_conversion.py)

### Tips to remember

What converts to what:

| from ↓ to → | `int()` | `float()` | `str()` | `bool()` |
|---|---|---|---|---|
| int | - | `3 -> 3.0` | `3 -> '3'` | `0 -> False`, else True |
| float | `3.99 -> 3` | - | `2.5 -> '2.5'` | `0.0 -> False`, else True |
| str | `'42' -> 42` | `'2.5' -> 2.5` | - | `'' -> False`, else True |
| bool | `True -> 1` | `True -> 1.0` | `True -> 'True'` | - |

- `int()` of a string accepts only an integer: `int('2.5')`, `int('abc')` and
  `int('')` raise ValueError. For `'2.5'`, use `int(float('2.5'))`.
- `int()` cuts towards zero, but `//` rounds down: `int(-7 / 2) == -3`, while
  `-7 // 2 == -4`. To round to the nearest integer, use `round()`
  (03_numbers_and_operators/04_math_functions.py).
- `x.is_integer()` asks whether a float has a fraction part. It converts
  nothing. On Python 3.10, which many judges run, only floats have it:
  `(10).is_integer()` crashes there.
- A float stores 53 binary digits (the IEEE 754 standard), so it holds every
  integer exactly only up to `2**53 = 9007199254740992`. Past that it rounds:
  `float(2**53 + 1) == float(2**53)`.
- So `/` loses digits on big numbers, and `//` is exact. With
  `big = 10**18 + 3`, `big // 2` is right and `int(big / 2)` is off by one.
- For the same reason `is_integer()` can be wrong on big numbers:
  `((2**53 + 1) / 2).is_integer()` is True, though `2**53 + 1` is odd.
- `1e9` means `1 * 10**9`, but it is a float.
- Python never mixes text and numbers: `31 + '!'` raises TypeError. Convert one
  side first.
- A float keeps its `.0` in text: `str(10 / 5)` is `'2.0'`, not `'2'`.
- `bool()` of a string only checks whether it is empty, so `bool('False')` is
  True. Compare the text instead: `answer == 'True'`.
- `True` and `False` count as 1 and 0: `True + True == 2`.

### What to expect in CP/DSA

- Every solution starts by reading numbers: `n = int(input())`. `int()` ignores
  the `'\n'` at the end of the judge's line.
- To divide integers, write `a // b`, never `int(a / b)`. The middle index in
  binary search is `mid = (lo + hi) // 2`.
- Numbers often go up to `10**18`, which fits C++'s 64-bit integers but is far
  past `2**53`. Keep them as int: use `//`, never `/` or `float()`.
- Write `MOD = 10**9 + 7`, not `1e9 + 7`, which is a float.
- Ask about divisibility with `%`, not `is_integer()`: `n % 2 == 0` (is n
  even?), `a % b == 0` (does b divide a exactly?).
- If the judge expects `2`, printing `2.0` is a Wrong Answer. Keep integer
  results as int.
- `str(n)` gives the digits of a number: `len(str(1234)) == 4`. The minus sign
  is a character too: `str(-42) == '-42'`.
- Adding up True values counts things: `count += x > 0` adds 1 only when x is
  positive.
