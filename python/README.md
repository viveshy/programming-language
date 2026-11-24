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
below once you can predict every assert in it.

## Study order

### 01 Variables and input
- [ ] [Variables](01_variables_and_input/01_variables.py): int, float, str, bool, and how the lessons check themselves
- [ ] [Receiving input](01_variables_and_input/02_receiving_input.py): `input()` always gives back a string
- [ ] [Type conversion](01_variables_and_input/03_type_conversion.py): `int()`, `float()`, `str()`, `bool()` and the `bool('False')` trap

### 02 Strings
- [ ] [Strings](02_strings/01_strings.py): quotes, multi-line strings, indexing and slicing
- [ ] [Formatted strings](02_strings/02_formatted_strings.py): f-strings and decimal places
- [ ] [String methods](02_strings/03_string_methods.py): `len`, `upper`/`lower`, `find`, `replace`, `in`, `strip`, character checks

### 03 Numbers and operators
- [ ] [Arithmetic operators](03_numbers_and_operators/01_arithmetic_operators.py): `+ - * / // % **`, negative `//` and `%`, float precision, big ints
- [ ] [Augmented assignment](03_numbers_and_operators/02_augmented_assignment_operators.py): `+= -= *= /= //= %=`
- [ ] [Operator precedence](03_numbers_and_operators/03_operator_precedence.py): which operator goes first, and two `**` surprises
- [ ] [Math functions](03_numbers_and_operators/04_math_functions.py): `round` (halves go to even), `abs`, `floor`, `ceil`, `isclose`

### 04 Conditionals
- [ ] [If statements](04_conditionals/01_if_statements.py): `if`, `elif`, `else`, nesting
- [ ] [Comparison operators](04_conditionals/02_comparison_operators.py): `== != < > <= >=` and chained comparisons
- [ ] [String comparison](04_conditionals/03_string_comparison.py): case, whitespace, alphabetical order
- [ ] [Logical operators](04_conditionals/04_logical_operators.py): `and`, `or`, `not`
- [ ] [Falsy values](04_conditionals/05_falsy.py): what counts as False

### 05 Loops
- [ ] [While loop](05_loops/01_while_loop.py): `break` and `while`/`else`
- [ ] [Range](05_loops/02_range.py): counting up, down and in steps
- [ ] [For loops](05_loops/03_for_loops.py): nesting, `for`/`else`, `enumerate`, `zip`

### 06 Collections
- [ ] [Lists](06_collections/01_lists.py): indexing, slicing, changing items
- [ ] [List methods](06_collections/02_list_methods.py): `append`, `pop`, `count`, `sort` vs `sorted`, `key=`, `min`/`max`/`sum`
- [ ] [Shallow and deep copy](06_collections/03_shallow_and_deep_copy.py): when two names share one list
- [ ] [Tuples](06_collections/04_tuples.py): lists that can't change, and how to check that an error is raised
- [ ] [Unpacking](06_collections/05_unpacking.py): swapping, `_` and `*rest`
- [ ] [Dictionaries](06_collections/06_dictionaries.py): `get`, `in`, `pop`, looping, counting
- [ ] [Sets](06_collections/07_sets.py): no duplicates, fast `in`, union, intersection, difference
- [ ] [Deque](06_collections/08_deque.py): fast adding and removing at both ends
- [ ] [Split and join](06_collections/09_split_and_join.py): string ↔ list, reading numbers from a line
- [ ] [Comprehensions](06_collections/10_comprehensions.py): one-line lists, dicts and sets, and the grid trap

### 07 Functions
- [ ] [Functions](07_functions/01_functions.py): `return`, defaults, the mutable default trap, `lambda`, `key=`, recursion
- [ ] [Scope of variables](07_functions/02_scope_of_variables.py): global, local, shadowing, `UnboundLocalError`
