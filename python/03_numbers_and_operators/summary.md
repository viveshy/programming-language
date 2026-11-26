# Numbers and operators: summary

Read this after the lessons, and again before a contest or an interview.
Each lesson has two parts:

- **Tips to remember:** the facts and the mistakes to avoid, with the reason.
- **What to expect in CP/DSA:** where the topic shows up in competitive
  programming (CP) and in the data structures and algorithms (DSA) problems of
  coding interviews.

Practice problems for this folder are in [problems.md](problems.md).

## 1. Arithmetic operators

Lesson: [01_arithmetic_operators.py](01_arithmetic_operators.py)

### Tips to remember

Dividing `7` and `-7` by `2`:

| `/` divide | `//` floor division | `%` remainder |
|---|---|---|
| `7 / 2 == 3.5` | `7 // 2 == 3` | `7 % 2 == 1` |
| `-7 / 2 == -3.5` | `-7 // 2 == -4` | `-7 % 2 == 1` |

- A float on either side makes a float: `2.5 * 4` is `10.0`, not `10`.
- `/` always gives a float, and a float loses digits past `2**53`
  (01_variables_and_input/03_type_conversion.py): `(10**18 + 1) / 1 == 10**18`.
- `//` throws the fraction away at once, so multiply first, then divide:
  `7 * 3 // 2 == 10`, but in `7 // 2 * 3 == 9` the `.5` was lost first.
- `a % 0`, `a // 0` and `a / 0` all stop with a ZeroDivisionError. Make sure
  the number you divide by can't be 0.
- `-7 // 2` is `-4`, not `-3`, because `//` rounds down, towards minus
  infinity. `a % b` then takes the sign of `b`, so that
  `a == (a // b) * b + a % b` always holds: `-7 == (-4) * 2 + 1`.
- So `n % 10` is the last digit only when `n >= 0`: `-123 % 10 == 7`, because
  `-123 // 10` is `-13`. Drop the sign first: `abs(-123) % 10 == 3`.
- C++ and Java cut towards zero instead: there `-7 / 2` is `-3` and `-7 % 2`
  is `-1`. So code copied from them can give different answers in Python.
- `^` is not power but XOR, an operator on bits (binary digits): `2 ^ 3 == 1`.
- `** 0.5` gives a float, so on big numbers the square root can be off by
  one: `int((10**16 - 1) ** 0.5)` is `10**8`, not `99999999`. `math.isqrt(n)`
  gives the exact integer square root (the math module: 04_math_functions.py).
- Floats are often a tiny bit off, because a float keeps only 53 binary
  digits and 0.1 never ends in binary: `0.1 + 0.2 == 0.30000000000000004`.
  So `==` can fail: round before you compare, or stay in integers.
- `int()` cuts off the fraction, so `int(0.57 * 100) == 56`: `0.57 * 100` is
  `56.99999999999999`, a tiny bit under 57. Use `round()` to get 57.

### What to expect in CP/DSA

- Contest numbers are integers, and integer maths is exact. Printing `10.0`
  when the judge expects `10` is a Wrong Answer.
- Use `/` only when the problem asks for a decimal answer, like an average (a
  total divided by a count). Such answers are judged with a tolerance, like
  "within `10**-6` of the right answer", so a tiny float error is fine there.
- `n % 10` is the last digit and `n // 10` drops it: `472 % 10 == 2` and
  `472 // 10 == 47`. Repeat until `n` is 0 to visit every digit (05_loops).
- `//` also counts: from 1 to `high` there are `(high + 1) // 2` odd numbers,
  and `n` teams make `n // 2` pairs.
- Even or odd: `n % 2 == 0` means even and `n % 2 == 1` means odd, also for a
  negative `n`. In C++, `-3 % 2` is `-1`, so that odd check fails there.
- Does `b` divide `a`? Check `a % b == 0`.
- Wrapping around a circle: with `n` seats numbered 0 to `n - 1`, the seat
  after seat `i` is `(i + 1) % n`, and `k` seats on is `(i + k) % n`. Going
  back, `(i - 1) % n` takes seat 0 to seat `n - 1`.
- Answers modulo `10**9 + 7`: when the answer is huge, the problem asks for
  its remainder after dividing by `MOD = 10**9 + 7`. Taking `% MOD` after
  every `+` and `*` gives the same final answer, and keeps the numbers small.
- A difference modulo `MOD` is never negative: `(3 - 5) % MOD == MOD - 2`. So
  when a result like `pow(2, n, MOD) - 2` can be below 0, take `% MOD` again.
- No overflow (a number too big to store): in C++ a 64-bit integer stops near
  `9.2 * 10**18`, but in Python `a * b` is exact at any size.
- `pow(a, b, m)` gives `a ** b % m` fast. `a ** b % m` first builds the whole
  of `a ** b`, which is very slow when `b` is big, like `10**15`.

## 2. Augmented assignment operators

Lesson: [02_augmented_assignment_operators.py](02_augmented_assignment_operators.py)

### Tips to remember

- `x += 5` is short for `x = x + 5`: work out `x + 5`, then store the answer
  back in `x`. `-=`, `*=`, `**=`, `/=`, `//=` and `%=` work the same way.
- The whole right side is worked out first, so `x *= 2 + 1` means
  `x = x * (2 + 1)`: it multiplies `x` by 3. With `x = 10` you get 30, not 21.
- The variable must exist first: `total += 5` with no `total = 0` before it
  stops with a NameError, because there is no old `total` to add 5 to.
- `/=` turns `x` into a float, because `/` always gives a float. `//=` keeps
  an integer an integer.
- So `/=` on a big integer loses digits: with `big = 10**18 + 2`, `big /= 2`
  gives `5 * 10**17`, not `5 * 10**17 + 1`. Use `//=` instead.
- `x %= m` keeps only the remainder, so `x` stays from 0 to `m - 1` (for
  `m > 0`). But `total += x % MOD` makes only `x` small, and `total` keeps
  growing. Take `%` of the sum: `total %= MOD` after adding, or
  `total = (total + x) % MOD`.
- Python has no `x++` or `x--`: write `x += 1` and `x -= 1`. `x++` is a
  SyntaxError, but `++x` is allowed and does nothing: it means `+(+x)`, two
  plus signs in front, so `x` stays the same. In the same way, `--x` is
  `-(-x)`, which is `x` again.

### What to expect in CP/DSA

- Counting: `count += 1` each time you find what you are looking for, and
  `i += 1` to step through a loop (05_loops).
- A running total: `total += x` for each number `x`.
- `n //= 10` drops the last digit and `n //= 2` halves `n`. Both stay exact.
  Avoid `/=` on integers: it turns them into floats.
- `//=` pairs with a `%` check: `n //= 2` when `n % 2 == 0`, or `n //= 3` for
  as long as `n % 3 == 0`.
- `ans %= MOD` after every step keeps an answer modulo `10**9 + 7` small. When
  you need only a remainder, keep only the remainder after each step, so the
  number never grows.
- `i = (i + 1) % n` moves to the next seat around a circle of `n` seats.

## 3. Operator precedence

Lesson: [03_operator_precedence.py](03_operator_precedence.py)

### Tips to remember

- The order, from first to last: `( )`, `**`, `-x`, `* / // %`, `+ -`,
  comparisons, `not`, `and`, `or`. Assignment (`=`, `+=`, ...) happens last,
  after the whole right side is worked out.
- `%` sits with `*` and `/`, not with `+` and `-`, so `a + b % m` is
  `a + (b % m)`: `5 + 9 % 7 == 7`, but `(5 + 9) % 7 == 0`. To take `%` of a
  sum, put brackets round the sum.
- `//` works the same way: with `lo = 4` and `hi = 10`, `(lo + hi) // 2` is 7,
  but `lo + hi // 2` is 9, because only `hi` was halved.
- The same level goes left to right: `8 / 2 * 4` is `(8 / 2) * 4 == 16.0`,
  not `8 / (2 * 4)`. Write the brackets if you meant `8 / (2 * 4) == 1.0`.
- `**` is the one operator that goes right to left: `2 ** 3 ** 2` is
  `2 ** 9 == 512`, not `(2 ** 3) ** 2 == 64`.
- `**` goes before a minus sign in front: `-2 ** 2 == -4`. So a sign that
  flips +1, -1, +1, ... is `(-1) ** k`, with brackets, because `-1 ** k` is
  `-(1 ** k)`, which is always -1.
- The maths goes before comparisons, so `n % 2 == 0` needs no brackets.
- `and` goes before `or`, so `a or b and c` is `a or (b and c)`:
  `True or False and False` is True, but `(True or False) and False` is
  False. When you mix `and` with `or`, add brackets.

### What to expect in CP/DSA

- A sum modulo `MOD` needs brackets, `(a + b) % MOD`, and so does the middle
  index in binary search, `mid = (lo + hi) // 2`, worked out on every step.
- The sum `1 + 2 + ... + n` is `n * (n + 1) // 2`. Without the brackets,
  `n * n + 1 // 2` is just `n * n`, because `1 // 2` goes before the `+`, and
  `1 // 2` is 0.
- If a list holds the numbers 1 to `n` with one missing, `n * (n + 1) // 2`
  minus the sum of the list gives the missing number.
- Left to right does what you want here: `a * b % MOD` is `(a * b) % MOD`,
  and `n // 10 % 10` is `(n // 10) % 10`, the second digit from the right:
  `472 // 10 % 10 == 7`.
- No brackets needed: `10**9 + 7` (`**` goes first, then `+ 7`),
  `a * d == c * b` (two products compared) and `x > 0 and y > 0` (the
  comparisons go first).
- When you are not sure of the order, add brackets. They cost nothing.

## 4. Math functions

Lesson: [04_math_functions.py](04_math_functions.py)

### Tips to remember

- `round()` and `abs()` are built in. `math.floor()`, `math.ceil()` and
  `math.isclose()` need `import math` first.
- `round()` sends an exact half to the even neighbour, not always up:
  `round(2.5) == 2`, `round(3.5) == 4`, `round(-2.5) == -2`.
- `round(2.675, 2)` is `2.67`, not `2.68`, because 2.675 is stored as
  2.67499999... (floats are not exact: 01_arithmetic_operators.py, section 7).
- `abs(a - b)` is the distance between `a` and `b`, either way round:
  `abs(3 - 10) == 7` and `abs(10 - 3) == 7`.
- `math.floor()` rounds down and `math.ceil()` rounds up. For a negative
  number, down is away from zero: `math.floor(-8.34) == -9`, while
  `math.ceil(-8.34) == -8`. `int(-8.34)` is `-8` too: it cuts towards 0.
- Round a division of integers up with `(a + b - 1) // b`, not
  `math.ceil(a / b)`, because `a / b` is a float, and a float loses digits
  past `2**53`. With `a = 3 * 10**17 + 1`, `math.ceil(a / 3)` gives `10**17`,
  but `(a + 3 - 1) // 3` gives the right answer, `10**17 + 1`.
- Compare floats with `math.isclose()`: `math.isclose(0.1 + 0.2, 0.3)` is
  True. It measures "tiny" against the size of the numbers, so next to 0
  nothing counts as close: `math.isclose(0.1 + 0.2 - 0.3, 0)` is False.
- To compare with 0, give `abs_tol` (the absolute tolerance: the gap you
  accept): `math.isclose(0.1 + 0.2 - 0.3, 0, abs_tol=1e-9)` is True. `1e-9`
  means `10**-9`. (Named arguments like `abs_tol=` come in 07_functions.)

### What to expect in CP/DSA

- Contest answers are mostly integers, so `round()` is rare. To print a float
  with 2 digits after the point, use `f'{x:.2f}'`
  (02_strings/02_formatted_strings.py).
- To turn a float that is a tiny bit off back into an integer, use `round()`,
  not `int()`: `int(0.57 * 100)` is 56, but `round(0.57 * 100)` is 57.
- The distance on a grid, moving only along rows and columns (the Manhattan
  distance), is `abs(x1 - x2) + abs(y1 - y2)`.
- Rounding up a division of integers is common: 10 items in boxes of 4 need
  `(10 + 4 - 1) // 4 == 3` boxes (`(a + b - 1) // b` needs `b > 0`). Or use
  `-(-a // b)`: `//` rounds `-a / b` down, and the minus flips it.
- Use `math.floor()` and `math.ceil()` only on values that are floats
  already. To round a division of integers down, `a // b` is enough.
- Avoid floats where you can. Is `a / b` equal to `c / d`? Compare `a * d`
  with `c * b` instead: exact integers. `2 * 9 == 3 * 6`, so `2 / 6` equals
  `3 / 9`. Compare slopes (how steep a line is) the same way.
- If floats can't be avoided, check `abs(x - y) < 1e-9`.
