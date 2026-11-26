# Numbers and operators: problems

Practice problems for the lessons in this folder, in lesson order.
Do a lesson first, then its problems. The tips for each lesson are in
[summary.md](summary.md).

22 problems: 17 Easy, 5 Medium. All are free.

## 1. Arithmetic operators

Lesson: [01_arithmetic_operators.py](01_arithmetic_operators.py)

| Problem | Level | Hint |
|---|---|---|
| [1491. Average Salary Excluding the Minimum and Maximum Salary](https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/) | Easy | The answer is a total divided by a count, so `/` is right there |
| [2520. Count the Digits That Divide a Number](https://leetcode.com/problems/count-the-digits-that-divide-a-number/) | Easy | `n % 10` (section 4) gives a digit, then `n // 10` drops it |
| [1523. Count Odd Numbers in an Interval Range](https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/) | Easy | `(high + 1) // 2` is how many odd numbers there are from 1 to `high` |
| [1688. Count of Matches in Tournament](https://leetcode.com/problems/count-of-matches-in-tournament/) | Easy | `n` teams play `n // 2` matches in a round |
| [412. Fizz Buzz](https://leetcode.com/problems/fizz-buzz/) | Easy | `i % 3 == 0` and `i % 5 == 0` decide what to print |
| [189. Rotate Array](https://leetcode.com/problems/rotate-array/) | Medium | The item at index `i` moves to `(i + k) % n` |
| [1175. Prime Arrangements](https://leetcode.com/problems/prime-arrangements/) | Easy | Multiply, taking `% MOD` at every step |
| [7. Reverse Integer](https://leetcode.com/problems/reverse-integer/) | Medium | Take the sign off first, since `-123 % 10` is 7 |
| [2550. Count Collisions of Monkeys on a Polygon](https://leetcode.com/problems/count-collisions-of-monkeys-on-a-polygon/) | Medium | `pow(2, n, MOD) - 2` can be below 0. One more `% MOD` makes it right (`pow()` is in summary.md) |
| [1922. Count Good Numbers](https://leetcode.com/problems/count-good-numbers/) | Medium | `n` goes up to `10**15`, so it needs `pow(5, ..., MOD)` |
| [2469. Convert the Temperature](https://leetcode.com/problems/convert-the-temperature/) | Easy | Answers within `10**-5` are accepted |

## 2. Augmented assignment operators

Lesson: [02_augmented_assignment_operators.py](02_augmented_assignment_operators.py)

| Problem | Level | Hint |
|---|---|---|
| [1480. Running Sum of 1d Array](https://leetcode.com/problems/running-sum-of-1d-array/) | Easy | `total += x`, one number at a time |
| [1342. Number of Steps to Reduce a Number to Zero](https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/) | Easy | `n //= 2` when `n` is even, `n -= 1` when it is odd |
| [326. Power of Three](https://leetcode.com/problems/power-of-three/) | Easy | `n //= 3` for as long as `n % 3 == 0` |
| [1018. Binary Prefix Divisible By 5](https://leetcode.com/problems/binary-prefix-divisible-by-5/) | Easy | Keep only the remainder mod 5, so the number never grows |
| [2011. Final Value of Variable After Performing Operations](https://leetcode.com/problems/final-value-of-variable-after-performing-operations/) | Easy | Turn `"++X"` and `"X++"` into `x += 1`, and `"--X"` and `"X--"` into `x -= 1` |

## 3. Operator precedence

Lesson: [03_operator_precedence.py](03_operator_precedence.py)

| Problem | Level | Hint |
|---|---|---|
| [268. Missing Number](https://leetcode.com/problems/missing-number/) | Easy | `n * (n + 1) // 2` minus the sum of the list |
| [704. Binary Search](https://leetcode.com/problems/binary-search/) | Easy | `mid = (lo + hi) // 2` on every step |

## 4. Math functions

Lesson: [04_math_functions.py](04_math_functions.py)

| Problem | Level | Hint |
|---|---|---|
| [1779. Find Nearest Point That Has the Same X or Y Coordinate](https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/) | Easy | Uses the Manhattan distance |
| [1266. Minimum Time Visiting All Points](https://leetcode.com/problems/minimum-time-visiting-all-points/) | Easy | Works with `abs()` of the x and y differences |
| [875. Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) | Medium | A pile of `p` bananas, eaten `k` per hour, takes `(p + k - 1) // k` hours |
| [1232. Check If It Is a Straight Line](https://leetcode.com/problems/check-if-it-is-a-straight-line/) | Easy | Compare slopes by multiplying across, not by dividing |
