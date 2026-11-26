# Functions: summary

Read this after the lessons, and again before a contest or an interview.
Each lesson has two parts:

- **Tips to remember:** the facts and the mistakes to avoid, with the reason.
- **What to expect in CP/DSA:** where the topic shows up in competitive
  programming (CP) and in the data structures and algorithms (DSA) problems of
  coding interviews.

Practice problems for this folder are in [problems.md](problems.md).

## 1. Functions

Lesson: [01_functions.py](01_functions.py)

### Tips to remember

- `def` only defines a function, and `greet('Ada')` calls it. Python runs the
  file from top to bottom, so `def` must come before the first call: calling
  `greet()` above its `def` stops with a NameError.
- With no `return`, or a forgotten one, a call gives back `None`. Printing the
  answer inside the function is not returning it either.
- `return` ends the call at once, even in the middle of a loop.
- `return a, b` gives back one tuple that holds both values. Unpack it into two
  names: `q, r = divmod(7, 2)` gives `3` and `1`.
- Defaults fill in left-out arguments: with `def power(base, exponent=2)`,
  `power(3) == 9`. Keyword arguments name their parameter, so they go in any
  order: `power(exponent=3, base=2) == 8`.
- Parameters with a default must come after the ones without:
  `def power(exponent=2, base)` is a SyntaxError.
- Never use `[]` or `{}` as a default. A default is made once, when `def` runs,
  and every call shares it, so a list default keeps what earlier calls put into
  it. Default to `None` and make a new list inside the function.
- `sorted(items, key=f)` sorts by what `f(item)` returns: `key=len` sorts by
  length. A tuple key, like `(age, name)`, sorts by age, then by name.
- Pass the function, don't call it: `key=len()` stops with a TypeError,
  because `len()` runs at once, with nothing to measure.
- Recursion needs a base case, a case the function answers directly, like
  `n <= 1` in `factorial`. Python stops at about 1000 nested calls with a
  RecursionError, and a missing base case ends the same way.
- `fib` calls itself twice, so the number of calls doubles at each level:
  `fib(30)` makes about 2.7 million calls, working out the same values again
  and again. Memoization (remembering answers) fixes this.

### What to expect in CP/DSA

- LeetCode gives you the `def` line, and you write the block. It checks the
  value you return, so printing the answer instead is wrong.
- Return as soon as you know the answer: `return True` the moment you find
  what you look for, and `return False` after the loop.
- A helper can return two answers at once, e.g. `(smallest, largest)`.
  `n, last_digit = divmod(n, 10)` splits off the last digit in one step.
- Defaults show up mostly in built-ins, like `sorted(nums, reverse=True)`, and
  in recursive helpers that count from a default: `def dfs(node, depth=0)`.
- A mutable default is a real cause of Wrong Answers. LeetCode runs many test
  cases in one program, so a default like `seen=set()` or `memo={}` can keep
  data from an earlier test case. Make the set or dict inside the function.
- `lambda` is used almost only as `key=` in `sorted()`, `min()` and `max()`.
- A minus sign sorts a number largest first: with `(name, score)` pairs,
  `key=lambda s: (-s[1], s[0])` sorts by high score, then by name.
- DFS (depth-first search) on trees and graphs is usually a recursive helper
  (lesson 2 below shows its usual shape). Inputs `10**5` levels deep need a
  higher limit, or a loop instead (Python for CP, 05_recursion).
- A recursion like `fib` with n up to 45 is too slow as it is: add memoization
  (Python for CP, 04_tools/03_memoization.py).

## 2. Scope of variables

Lesson: [02_scope_of_variables.py](02_scope_of_variables.py)

### Tips to remember

- Any function can read a global variable (one made outside every function),
  with no special keyword. To assign to it, declare `global name` first.
- A local variable (one made inside a function) exists only during its call.
  Outside the function, its name raises a NameError.
- A local starts again at every call, so it can't count calls: a function that
  sets `calls = 0`, then does `calls += 1`, returns 1 every time.
- Assigning to a name inside a function makes a new local, even if a global
  has the same name. The local hides (shadows) the global, which stays
  untouched.
- Assigning to a name anywhere in a function makes it local in the whole
  function. So `counter = counter + 1` there reads a local that has no value
  yet, and stops with an UnboundLocalError. `counter += 1` fails the same way:
  write `global counter` first.
- Don't name variables `max`, `min`, `sum` or `list`, because that hides the
  built-in: after `max = 10`, `max([1, 2])` stops with a TypeError. Use names
  like `best`, `total` or `nums`.
- `append()` changes a list without assigning to its name, so it needs no
  `global`.
- `nonlocal name` assigns to the outer function's variable, when one function
  is defined inside another. `global` can't reach it: with `global steps`,
  `steps += 1` looks for a global named `steps`, finds none, and stops with a
  NameError. A plain `steps = 5` is worse: no error, but it makes a new global
  and leaves the outer `steps` unchanged.

### What to expect in CP/DSA

- Globals hold what every function needs: constants at the top of the file,
  like `MOD = 10**9 + 7`, and the input, read once at the top.
- Every recursive call gets its own locals. That is why `factorial(n - 1)`
  doesn't overwrite the `n` of the call above it (01_functions.py).
- A `solve()` function called once per test case starts every test case with
  fresh variables.
- In a contest script, a DFS (depth-first search) helper often updates a global
  counter or best answer with `global`.
- On LeetCode, your function sits inside `class Solution`, so the counter is
  usually a local of your function, not a global. Then use `nonlocal`.
- DFS visits a node, then calls itself on each child. Its usual shape on
  LeetCode: inside your function, set `total = 0` and define a helper
  `dfs(node)` that says `nonlocal total`, adds 1 and calls `dfs` on each
  child. Then call `dfs(root)` and return `total`.
- The helper can also return a value, like a depth, and update a `nonlocal`
  best on the way.
- Without `nonlocal`, have `dfs` return its answer, and add up the returns.
