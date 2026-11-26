# Python

Python fundamentals, one topic per file, studied in order. Once everything here
is covered and mastered, Python for competitive programming continues in a
separate repo, `python-for-cp`.

## How the lessons work

Every lesson is a plain Python file. Each fact in it is written as an `assert`:

```python
assert len('Mission Impossible') == 18
```

If a fact is false, Python stops with an `AssertionError` that shows the file
and line. When a lesson reaches its end, it prints `All checks passed.`

Each folder holds its lessons and two Markdown files:

- **The lessons** (`01_variables.py`, ...) teach. Each one opens with what the
  topic is (usually with a table of its main forms), why it matters, and a
  "We will cover" list. Then come numbered sections, each in a box, with the
  idea in plain words and the asserts that check it.
- **`summary.md`** is for revising. For each lesson it lists the tips to
  remember, with the mistakes to avoid, and what to expect when the topic comes
  up in competitive programming (CP) and in interview problems (DSA).
- **`problems.md`** lists problems to practise, lesson by lesson, with a link,
  the level and a hint for each. They are free LeetCode problems, plus two
  CSES problems for reading input.

Run one lesson (from this folder):

```bash
python3 01_variables_and_input/01_variables.py
```

Check every lesson at once:

```bash
python3 check_lessons.py
```

`02_receiving_input.py` waits for you to type something when you run it
yourself. The checker types `Ada` for it.

## How to revise

Read an assert, cover its right-hand side, and say what it should be. Then
change a value, run the file, and see which line stops it. Tick a lesson off
below once you can predict every assert in it. Then read its part of the
folder's `summary.md`, and solve its problems in `problems.md`. Before a
contest or interview, reread the `summary.md` files.

## Study order

### 01 Variables and input

[Summary](01_variables_and_input/summary.md) · [Problems](01_variables_and_input/problems.md)

- [ ] [Variables](01_variables_and_input/01_variables.py): int, float, str, bool, and how the lessons check themselves
- [ ] [Receiving input](01_variables_and_input/02_receiving_input.py): `input()` always gives back a string
- [ ] [Type conversion](01_variables_and_input/03_type_conversion.py): `int()`, `float()`, `str()`, `bool()`, `is_integer()`, where floats lose digits (2**53), `True` and `False` as numbers

### 02 Strings

[Summary](02_strings/summary.md) · [Problems](02_strings/problems.md)

- [ ] [Strings](02_strings/01_strings.py): quotes, multi-line strings, `+` and `*`, indexing, slicing, `s[::-1]`
- [ ] [Formatted strings](02_strings/02_formatted_strings.py): f-strings, decimal places (rounded), padding with zeros, binary
- [ ] [String methods](02_strings/03_string_methods.py): `len`, `upper`/`lower`, `in`, `find`, `count`, `replace`, `strip`, character checks

### 03 Numbers and operators

[Summary](03_numbers_and_operators/summary.md) · [Problems](03_numbers_and_operators/problems.md)

- [ ] [Arithmetic operators](03_numbers_and_operators/01_arithmetic_operators.py): `+ - * / // % **`, negative `//` and `%`, float precision, big ints
- [ ] [Augmented assignment](03_numbers_and_operators/02_augmented_assignment_operators.py): `+= -= *= **= /= //= %=`, and why Python has no `++`
- [ ] [Operator precedence](03_numbers_and_operators/03_operator_precedence.py): which operator goes first, left to right on the same level, `**` and the minus sign
- [ ] [Math functions](03_numbers_and_operators/04_math_functions.py): `round` (halves go to even), `abs`, `floor`, `ceil`, `isclose`

### 04 Conditionals

[Summary](04_conditionals/summary.md) · [Problems](04_conditionals/problems.md)

- [ ] [If statements](04_conditionals/01_if_statements.py): `if`, `elif`, `else`, nesting, the one-line if-else
- [ ] [Comparison operators](04_conditionals/02_comparison_operators.py): `== != < > <= >=` and chained comparisons
- [ ] [String comparison](04_conditionals/03_string_comparison.py): case, whitespace, alphabetical order
- [ ] [Logical operators](04_conditionals/04_logical_operators.py): `and`, `or`, `not`, their order, short-circuiting, the value they give back
- [ ] [Falsy values](04_conditionals/05_falsy.py): what counts as False, and testing with `is None`

### 05 Loops

[Summary](05_loops/summary.md) · [Problems](05_loops/problems.md)

- [ ] [While loop](05_loops/01_while_loop.py): `break`, `continue`, `while`/`else`, two pointers and binary search
- [ ] [Range](05_loops/02_range.py): counting up, down and in steps, empty ranges
- [ ] [For loops](05_loops/03_for_loops.py): `break` and `continue`, nesting, `for`/`else`, `enumerate`, `zip`

### 06 Collections

[Summary](06_collections/summary.md) · [Problems](06_collections/problems.md)

- [ ] [Lists](06_collections/01_lists.py): indexing, slicing, changing items, joining and repeating lists
- [ ] [List methods](06_collections/02_list_methods.py): `append`, `pop`, `pop(i)` and `insert` (slow at the front), `count`, `sort` vs `sorted`, `min`/`max`/`sum`
- [ ] [Shallow and deep copy](06_collections/03_shallow_and_deep_copy.py): when two names share one list, `+=` vs `+`, copying a grid
- [ ] [Tuples](06_collections/04_tuples.py): lists that can't change, and how to check that an error is raised
- [ ] [Unpacking](06_collections/05_unpacking.py): swapping, `_` and `*rest`
- [ ] [Dictionaries](06_collections/06_dictionaries.py): `get`, `in`, `pop`, looping, counting, grouping
- [ ] [Sets](06_collections/07_sets.py): no duplicates, fast `in`, union, intersection, difference
- [ ] [Deque](06_collections/08_deque.py): fast adding and removing at both ends, a queue for BFS
- [ ] [Split and join](06_collections/09_split_and_join.py): string ↔ list, reading numbers from a line
- [ ] [Comprehensions](06_collections/10_comprehensions.py): one-line lists, dicts and sets, building a grid

### 07 Functions

[Summary](07_functions/summary.md) · [Problems](07_functions/problems.md)

- [ ] [Functions](07_functions/01_functions.py): `return`, defaults, mutable defaults, `lambda`, `key=`, recursion
- [ ] [Scope of variables](07_functions/02_scope_of_variables.py): global, local, shadowing, `UnboundLocalError`, `global` and `nonlocal`
