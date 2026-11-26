# Variables and input: problems

Practice problems for the lessons in this folder, in lesson order.
Do a lesson first, then its problems. The tips for each lesson are in
[summary.md](summary.md).

8 problems: 8 Easy. All are free.

## 1. Variables

Lesson: [01_variables.py](01_variables.py)

| Problem | Level | Hint |
|---|---|---|
| [2469. Convert the Temperature](https://leetcode.com/problems/convert-the-temperature/) | Easy | The input and the answers are floats |
| [231. Power of Two](https://leetcode.com/problems/power-of-two/) | Easy | The answer is `True` or `False` |

## 2. Receiving input

Lesson: [02_receiving_input.py](02_receiving_input.py)

LeetCode calls your function with the input ready, so it never uses `input()`.
These two come from CSES, a free contest-style site where your program reads
the input itself.

| Problem | Level | Hint |
|---|---|---|
| [CSES 1068. Weird Algorithm](https://cses.fi/problemset/task/1068) | Easy | Read n with `int(input())`, then halve it when even, else make it `3 * n + 1`, until it is 1 (a while loop, 05_loops) |
| [CSES 1083. Missing Number](https://cses.fi/problemset/task/1083) | Easy | Read n, then the second line with `split()` (06_collections). The answer is `n * (n + 1) // 2 - sum(nums)` |

## 3. Type conversion

Lesson: [03_type_conversion.py](03_type_conversion.py)

| Problem | Level | Hint |
|---|---|---|
| [1295. Find Numbers with Even Number of Digits](https://leetcode.com/problems/find-numbers-with-even-number-of-digits/) | Easy | `len(str(x)) % 2 == 0` |
| [9. Palindrome Number](https://leetcode.com/problems/palindrome-number/) | Easy | Compare `str(x)` with `str(x)` reversed |
| [1281. Subtract the Product and Sum of Digits of an Integer](https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/) | Easy | Turn each character of `str(n)` back into a digit with `int()` |
| [1351. Count Negative Numbers in a Sorted Matrix](https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/) | Easy | A first answer adds `x < 0` for every number `x` (with a loop, 05_loops) |
