# Loops: summary

Read this after the lessons, and again before a contest or an interview.
Each lesson has two parts:

- **Tips to remember:** the facts and the mistakes to avoid, with the reason.
- **What to expect in CP/DSA:** where the topic shows up in competitive
  programming (CP) and in the data structures and algorithms (DSA) problems of
  coding interviews.

Practice problems for this folder are in [problems.md](problems.md).

## 1. While loop

Lesson: [01_while_loop.py](01_while_loop.py)

### Tips to remember

- `while` runs its block again and again, as long as its condition is True.
  After each round, Python checks the condition again.
- Something in the block must change the condition, or the loop never ends.
  That is an infinite loop: the program hangs. Stop it with Ctrl+C.
- After the loop, the variable holds the value that made the condition False:
  after `while counter < 5:`, `counter` is 5, not 4.
- Digits: `n % 10` is the last digit of `n`, and `n //= 10` drops it
  (03_numbers_and_operators/01_arithmetic_operators.py). A `while n > 0:` loop
  that does both visits every digit, last to first.
- `break` leaves the loop at once, even if the condition is still True.
- `while True:` never stops by itself, so it needs a `break`. Use it when the
  stop test is easiest to write in the middle of the block.
- `continue` skips the rest of the block and starts the next round.
- In a while loop, update before `continue`. If `n += 1` came after it, an
  even `n` would skip the update every time, and the loop would never end.
- The `else` of a loop runs only if the loop ended without `break`. It does
  not mean "the loop never ran": even after 0 rounds, the `else` runs.
- Binary search: `while lo < hi:`, `mid = (lo + hi) // 2`, then `hi = mid` if
  mid works, or `lo = mid + 1` if mid is too small.
- Write `lo = mid + 1`, not `lo = mid`. When `hi` is `lo + 1`, `mid` is `lo`
  again (`(7 + 8) // 2 == 7`), so `lo = mid` would not move `lo`, and the
  loop would never end.

### What to expect in CP/DSA

- Use `while` when you don't know in advance how many rounds you need: count
  the rounds of a `while n > 0:` loop, add up the digits of a number (1234
  gives 10), or build the reversed number digit by digit.
- Stop a search with `break` as soon as you find the answer: the rest is
  wasted work.
- `while True:` repeats a rule until you reach the state you are looking for.
  If a number can come back, keep the numbers seen in a set
  (06_collections/07_sets.py), and `break` when one comes back.
- `continue` skips the items you don't need, instead of putting the rest of
  the block inside an `if`. It is more common in for loops (03_for_loops.py).
- `while ... else` is rare. Most people use a flag (a True/False variable, like
  `found = True`) instead, or `return` from a function
  (07_functions/01_functions.py). `for ... else` is a little more common.
- Two pointers start at both ends and move towards each other while
  `lo < hi`. The lesson checks a palindrome this way: a word that reads the
  same backwards.
- When only letters and digits count, `continue` past the other characters:
  those where `isalnum()` is False (02_strings/03_string_methods.py).
- Binary search halves the range where the answer must be, each round, so
  even the range 0 to `10**18` takes only about 60 rounds. It works the same
  way on a sorted list (06_collections/01_lists.py).

## 2. Range

Lesson: [02_range.py](02_range.py)

### Tips to remember

- The start is included, the stop is not: `range(5)` is 0, 1, 2, 3, 4, five
  numbers starting at 0.
- `range()` takes only integers. `range(n / 2)` stops with a TypeError,
  because `/` always gives a float, even `3.0`. Write `range(n // 2)`.
- `range(start, stop)` gives `stop - start` numbers: `range(2, 6)` is
  2, 3, 4, 5. Leave out the start and it is 0.
- `range(1, n)` stops at `n - 1`. To count from 1 to n, write
  `range(1, n + 1)`.
- The step is the gap from one number to the next. Leave it out and it is 1.
  A step of 0 stops with a ValueError.
- The stop is left out even when a step lands on it exactly: `range(0, 9, 3)`
  is 0, 3, 6.
- A negative step counts down, and the stop is still left out. So to count
  down to 0, the stop must be -1: `range(4, -1, -1)` is 4, 3, 2, 1, 0.
- Counting up, a range is empty when `start >= stop`. Counting down, it is
  empty when `start <= stop`. A loop over it runs 0 times, with no error.
- So `range(5, 2)` is empty: you meant to count down but forgot the step, so
  it counted up and got nothing. Add the step: `range(5, 2, -1)` is 5, 4, 3.
- A range is not a list. It stores only start, stop and step, and makes each
  number when the loop asks for it. So even `range(10 ** 9)` takes almost no
  memory, and `len()` still counts its numbers without building a list.
- Printing a range does not show its numbers: `str(range(5))` is
  `'range(0, 5)'`. Use `list()` to see them.

### What to expect in CP/DSA

- Most contest loops are `for i in range(n)`: `i` takes the indexes 0 to
  `n - 1` of a string or list with n items.
- To do something t times, e.g. once per test case: `for _ in range(t)`. `_`
  is the usual name for a value you won't use (06_collections/05_unpacking.py).
- Problems often number things from 1 to n, and n itself must be included:
  `range(1, n + 1)`.
- Every second index: `range(0, n, 2)`. The multiples of k up to n:
  `range(k, n + 1, k)`. To jump through a string `2 * k` characters at a time:
  `range(0, len(s), 2 * k)`.
- To count primes, a sieve crosses out the multiples of each prime, using a
  step.
- The indexes from last to first: `range(n - 1, -1, -1)`, which gives 2, 1, 0
  for `'abc'`. Use it to walk back from the end of a string, or to add 1 at
  the last digit and carry to the left.
- Small cases often need no extra code: when n is 0 or 1, `range(1, n)` is
  empty, so the loop doesn't run. Still check your answer for that case.
- `for i in range(10 ** 6)` is fine: it never builds a list of a million
  items. When you do need a real list, e.g. to change its items, write
  `list(range(n))`.
- A loop works, but a formula is faster when there is one: 1 + 2 + ... + n is
  `n * (n + 1) // 2`, instant even for `n = 10**18`.

## 3. For loops

Lesson: [03_for_loops.py](03_for_loops.py)

### Tips to remember

- `for x in seq:` runs the block once per item: the items of a list, the
  characters of a string, the numbers of a range.
- A new value for the loop variable does not change the list, because the
  loop variable is only a name for the current item. Inside
  `for fruit in fruits:`, `fruit = fruit.upper()` leaves `fruits` unchanged.
- To change the items, loop over the indexes, `range(len(nums))`, and assign
  to `nums[i]`.
- With `s[i - 1]`, start at `i = 1`. At `i = 0`, `s[i - 1]` is `s[-1]`, the
  last item. Python gives no error, only a wrong answer: with
  `word = 'aabbbc'`, `word[0 - 1]` is `'c'`.
- `break` and `continue` work as in a while loop. In a for loop, `continue`
  can't loop forever, because the next item comes by itself.
- In nested loops (a loop inside a loop), `break` leaves only the loop it is
  in. The outer loop keeps going.
- The inner loop runs all the way through for every step of the outer loop.
  So nested loops over n items cost about `n * n` steps.
- `for ... else`: the `else` runs only if the loop did not break. Use it to
  search: break when you find it, and `else` means "not found".
- `enumerate(s)` gives pairs `(index, item)`, counting from 0. `start=1`
  changes only the counting. It does not skip the first item:
  `list(enumerate('ab', start=1))` is `[(1, 'a'), (2, 'b')]`.
- `zip(a, b)` pairs up the first items, then the second items, and so on. It
  stops at the end of the shorter one, without any error:
  `list(zip(['a', 'b', 'c'], [1, 2]))` is `[('a', 1), ('b', 2)]`, no `'c'`.

### What to expect in CP/DSA

- Most loops in contest code are for loops: `for ch in s` checks or counts the
  characters of a string, and `for x in nums` goes through a list of numbers
  from the input. `ch in other` tests a character against another string.
- Compare each item with the one before it, `s[i]` with `s[i - 1]`, starting
  at `i = 1`. A running total adds the total so far at `i - 1` the same way.
- `break` stops at the first item that answers the question. `continue` skips
  the items you don't need, e.g. characters that are not letters.
- Every pair `i < j`: start the inner loop at `i + 1`. For n = 4 that gives 6
  pairs, `n * (n - 1) // 2`. Three nested loops go through every triple.
- n items give about `n * n / 2` pairs. That is fine for n up to a few
  thousand, but `n = 10**5` gives `5 * 10**9` pairs: far too slow.
- `for ... else` can check for a prime: `break` at the first `d` in
  `range(2, n)` with `n % d == 0`, and let the `else` set `is_prime = True`.
  For n = 2, `range(2, 2)` is empty, so the `else` runs: 2 is prime. Correct.
- Many people use a flag or a function with `return` instead
  (07_functions/01_functions.py). For a big n, stop once `d * d > n`: a while
  loop fits that better.
- Use `enumerate` when you need both the index and the item. It is cleaner
  than `range(len(nums))` plus `nums[i]`.
- With `for i, x in enumerate(nums)`, you can look up `target - x` among the
  numbers seen so far (in a dict, 06_collections/06_dictionaries.py).
- `zip` compares two strings position by position: count where `x != y` in
  `for x, y in zip(a, b)`. `'abcd'` and `'abed'` differ in one place. If one
  is longer, add its rest yourself, because `zip` drops it.
