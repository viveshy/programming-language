# Conditionals: summary

Read this after the lessons, and again before a contest or an interview.
Each lesson has two parts:

- **Tips to remember:** the facts and the mistakes to avoid, with the reason.
- **What to expect in CP/DSA:** where the topic shows up in competitive
  programming (CP) and in the data structures and algorithms (DSA) problems of
  coding interviews.

Practice problems for this folder are in [problems.md](problems.md).

## 1. If statements

Lesson: [01_if_statements.py](01_if_statements.py)

### Tips to remember

- The `if` line ends with a colon (`:`), and only the indented lines under it
  belong to the if. A line you forget to indent runs every time, whatever the
  condition says.
- `else` has no condition. It runs when the if's condition is False, so
  exactly one of the two blocks runs.
- `number % 2 == 0` is True when the number is even, because `%` gives the
  remainder and an even number leaves 0. `7 % 2` is 1, so 7 is odd.
- `if` / `elif` / `else` tries the conditions from the top and runs only the
  first True branch. The rest are skipped, even if they are True too.
- So put the narrowest test (the one the fewest values pass) first. If
  `score >= 70` comes first, a score of 95 gets `'C'`, because `95 >= 70` is
  True and the `score >= 90` branch never runs.
- Separate ifs are not a chain. Each one is tried, so a later one can
  overwrite the answer: after `if score >= 80:` and `if score >= 70:`, 85 ends
  with `'C'`, not `'B'`. Use `elif` for the second test.
- A nested if (an if inside another if's block) is tried only when the outer
  condition is True. Each `else` belongs to the if that it lines up with.
- A nested if with no else can be one if: `if age >= 18 and has_permission:`
  (`and` is in 04_logical_operators.py).
- `a if condition else b` gives `a` when the condition is True, and `b`
  otherwise: `'YES' if ok else 'NO'`. It picks a value. It does not run
  blocks.

### What to expect in CP/DSA

- Keep the best answer so far: `if x > best: best = x` (in a loop, 05_loops).
- Handle an edge case, like `n == 1`, before the main idea.
- Two possible answers, like `YES` and `NO`, are the most common contest
  output. The usual way to print one is `print('YES' if ok else 'NO')`.
- Even or odd is one if-else on `n % 2`.
- Several answers need one if-elif-else chain, narrowest test first: test
  "divisible by 3 and by 5" before "divisible by 3", or the "divisible by 3"
  branch catches 15.
- Contest code rarely nests ifs deeper than two levels. It keeps them flat
  with `and` or `elif`.

## 2. Comparison operators

Lesson: [02_comparison_operators.py](02_comparison_operators.py)

### Tips to remember

- Equal is `==` and not equal is `!=`. A single `=` stores a value, so
  `if a = 15:` is a SyntaxError.
- An int and a float compare by value: `1 == 1.0` is True.
- A number never equals its text: `15 == '15'` is False. `input()` always
  gives text, so convert it with `int()` before you compare:
  `15 == int('15')` is True.
- `<=` and `>=` also say True when the two are equal, but `<` and `>` do not.
  With `a = 15` and `c = 15`, `a > c` is False and `a >= c` is True.
- `<` or `<=`? Read the statement word for word. "At least 18" is
  `age >= 18`, because `age > 18` misses exactly 18.
- A comparison gives True or False. Use it in an if, keep it in a variable
  (`is_adult = age >= 18`), or check it with an assert.
- A chain like `b < a <= c` means `b < a and a <= c`: both must be True. The
  middle value takes part in both tests.
- A chain compares only neighbours: `a != b != c` never compares `a` with `c`.
  So `1 != 2 != 1` is True, though the first and the last are equal.

### What to expect in CP/DSA

- `n % 2 == 0` asks whether n is even, and `a % b == 0` asks whether b
  divides a exactly.
- A wrong `<` or `<=` at the edge is the classic off-by-one bug: the test is
  wrong only for the value at the edge, like `age > 18` for an age of 18.
  Words like "met" or "at least" mean `>=`, not `>`.
- When a problem asks for true or false, return the comparison itself. Once
  you spot the pattern, the whole answer can be one comparison.
- Check an index before you use it: `0 <= i < n`. In a grid, a neighbour cell
  is inside only if `0 <= row < rows`, where `rows` is the number of rows, and
  the same for columns.
- Statements write limits the same way: `1 <= n <= 10**5`.
- `x == y == z` tests three values at once, like three characters of a string.

## 3. String comparison

Lesson: [03_string_comparison.py](03_string_comparison.py)

### Tips to remember

- Two strings are equal only when they have the same characters in the same
  order: `'abc' == 'acb'` is False.
- Case matters, because `'H'` and `'h'` are different characters:
  `'Hello' != 'hello'`. To ignore case, compare `.lower()` copies.
- Many judges compare your output exactly, so to them `'Yes'` and `'YES'` are
  different answers. Print it exactly as the statement shows.
- A space is a character, just like a letter, and so is the newline `'\n'`.
  `.strip()` removes them from both ends:
  `'  Hello, World!  '.strip() == 'Hello, World!'`.
- `input()` drops the `'\n'` at the end of a line, but `sys.stdin.readline()`,
  the faster way to read (python-for-cp, 02_input_output), keeps it:
  `'YES\n' != 'YES'`. Strip the line first.
- `<` and `>` compare the first characters, then the next ones, and so on. The
  first difference decides: `'apple' < 'apricot'`, because `'p' < 'r'`.
- If one string runs out first, it comes first: `'app' < 'apple'`.
- Comparing two characters compares their codes, which `ord()` gives:
  `'0'` to `'9'` are 48 to 57, `'A'` to `'Z'` are 65 to 90, and `'a'` to `'z'`
  are 97 to 122.
- So every uppercase letter comes before every lowercase one:
  `'Zebra' < 'apple'`, because `'Z'` is 90 and `'a'` is 97. Lowercase both
  sides to get dictionary order.
- Numbers kept as text compare character by character, not by value:
  `'10' < '9'`, because `'1' < '9'`. Convert with `int()` first. A number
  against a string, like `10 < '9'`, stops with a TypeError.

### What to expect in CP/DSA

- A palindrome reads the same both ways: compare a string with its reverse,
  `s[::-1]` (02_strings/01_strings.py).
- When upper and lower case count as the same letter, lowercase the text
  first.
- To check the case of a whole word, compare it with `word.upper()` and
  `word.lower()`.
- Strip a line of contest input before you compare it: it can end with `'\n'`
  or with spaces.
- Sorting words uses this order (06_collections/02_list_methods.py), and
  letters compare with `<` and `>` just like numbers.
- `ord(c) - ord('a')` turns `'a'` to `'z'` into 0 to 25: a slot for each
  letter, to count each letter in a list (06_collections/01_lists.py).

## 4. Logical operators

Lesson: [04_logical_operators.py](04_logical_operators.py)

### Tips to remember

- `and` is True only when both sides are True. `or` is True when at least one
  side is True, and False only when both are False.
- Each side must be a full test: `x > 0 and < 10` is a SyntaxError. Write
  `x > 0 and x < 10`, or the chain `0 < x < 10`.
- `not` flips the value. For "is not inside", write `x not in s`: it reads
  better than `not (x in s)`.
- The order: comparisons first, then `not`, then `and`, then `or`. Brackets go
  before everything, so add them when you are unsure.
- Python does not go left to right here: `True or False and False` means
  `True or (False and False)`, which is True. Left to right would give False.
- Short-circuiting: `and` stops at the first False and `or` at the first True,
  because the answer is known by then. The right side never runs, so
  `False and 1 / 0` does not crash.
- So the guard, the test that protects the other one, goes first:
  `i < len(s) and s[i] == x`. With `s = 'abc'` and `i = 3`, the other order,
  `s[i] == 'c' and i < len(s)`, runs `s[3]` first and crashes.
- `and` and `or` give back one of their two values, not always True or False:
  `(0 or 5) == 5`, `('' or 'default') == 'default'`, `(3 and 5) == 5`.
- `x == 1 or 2` does not mean "x is 1 or 2". `==` goes first, so it is
  `(x == 1) or 2`, which gives 2. 2 counts as True, so an if on it always
  runs. Write `x == 1 or x == 2`.
- `or` replaces every value that counts as False, 0 included: with
  `count = 0`, `count or 10` gives 10. That is wrong when 0 was a real count.

### What to expect in CP/DSA

- A grid cell `(r, c)` is inside only if `0 <= r < rows and 0 <= c < cols`.
  Check that before you ask what is in the cell, like "is it land?".
- Several cases with one answer: `if n == 0 or n == 1:` (edge cases first).
- `if x not in seen:` catches the first time you meet `x`. To find a repeat,
  check `x in seen` before you add `x` (sets: 06_collections/07_sets.py).
- Date problems need the leap-year test: February has 29 days in a leap year.
- When you mix `and` with `or`, add brackets anyway, so the reader doesn't
  need to know the order:
  `(year % 4 == 0 and year % 100 != 0) or year % 400 == 0`.
- Linked lists and trees are made of nodes. `node.val` is a node's value.
  Guard first: `if node and node.val == x`. At the end of a list there is no
  node, only `None` (05_falsy.py), and `None.val` would crash.
- Loops use the same guard: `while fast and fast.next:`
  (05_loops/01_while_loop.py).
- In DSA code, the value of `or` shows up when you merge two linked lists: at
  the end, `list1 or list2` gives the list that still has nodes.

## 5. Falsy

Lesson: [05_falsy.py](05_falsy.py)

### Tips to remember

- A falsy value counts as False in an if, in a while, or with `not`. The
  falsy values are `0`, `0.0`, `False`, `''`, `None`, and empty collections:
  `[]`, `()`, `{}`, `set()`, `range(0)`. Every other value is truthy.
- Every number but zero is truthy, negatives too: `bool(-1)` is True. So a
  number can go straight into an if: `if remainder:` runs when it is not 0.
- `None` is Python's value for "no value here", and it is falsy.
- `if items:` means "if items is not empty", and `if name:` means "if name is
  not `''`". `input()` gives `''` when the user just presses Enter.
- `{}` is an empty dict, so an empty set is written `set()`.
- `'0'`, `' '` and `[0]` are truthy, because each holds one thing.
- `input()` gives text, so a typed 0 is `'0'`, which is truthy. Convert it
  first: `int('0')` is 0, which is falsy.
- Test for None with `x is None` and `x is not None`. `is` asks whether two
  names point to the very same value, and there is only one None.
- `not x` is True for `0` and `''` as well as for `None`. When 0 is a real
  answer, like a match found at index 0, `not result` wrongly says "nothing
  found". Write `result is None`.

### What to expect in CP/DSA

- `while n:` repeats until `n` is 0, for example to take a number apart digit
  by digit (05_loops/01_while_loop.py).
- `if n % 2:` means "if n is odd". `n % 2 == 1` says the same, more clearly.
- Linked lists and trees use `None` for "no node here": the end of a list, or
  a missing child. `if not root:` is the usual first line of tree code (the
  root is the top node), and an empty tree (`None`) has depth 0.
- `while head:` walks a linked list from its first node, `head`, until it
  reaches `None`.
- `while stack:` keeps going until the stack, a list you add to and take from
  at the end, is empty (06_collections/08_deque.py). Some problems end by
  checking that the stack is empty.
- A row of zeros like `[0, 0, 0]` is truthy, because it has items. To ask "is
  every item 0?", test the items, not the list.
- Tree values can be 0. `if node:` tests the node, but `if node.val:` is a bug
  when the value is 0.
- A start value when every number may be negative: `best = None`, then
  `if best is None or x > best: best = x`.
