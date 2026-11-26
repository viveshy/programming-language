# Loops: problems

Practice problems for the lessons in this folder, in lesson order.
Do a lesson first, then its problems. The tips for each lesson are in
[summary.md](summary.md).

19 problems: 18 Easy, 1 Medium. All are free.

## 1. While loop

Lesson: [01_while_loop.py](01_while_loop.py)

| Problem | Level | Hint |
|---|---|---|
| [1342. Number of Steps to Reduce a Number to Zero](https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/) | Easy | Count the rounds of a `while n > 0` loop |
| [9. Palindrome Number](https://leetcode.com/problems/palindrome-number/) | Easy | Build the reversed number digit by digit |
| [202. Happy Number](https://leetcode.com/problems/happy-number/) | Easy | Repeat the digit rule in a `while True` loop, and `break` at 1 or when a number comes back (keep them in a set, 06_collections) |
| [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | Easy | Two pointers from both ends; `continue` past characters that are not `isalnum()` (02_strings) |
| [35. Search Insert Position](https://leetcode.com/problems/search-insert-position/) | Easy | The lesson's `while lo < hi` binary search, on a sorted list (lists come in 06_collections) |

## 2. Range

Lesson: [02_range.py](02_range.py)

| Problem | Level | Hint |
|---|---|---|
| [412. Fizz Buzz](https://leetcode.com/problems/fizz-buzz/) | Easy | Go through 1 to n, and n itself must be included: `range(1, n + 1)` |
| [2894. Divisible and Non-divisible Sums Difference](https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/) | Easy | Add up over 1 to n: `range(1, n + 1)` |
| [541. Reverse String II](https://leetcode.com/problems/reverse-string-ii/) | Easy | Jump through the string `2 * k` characters at a time with `range(0, len(s), 2 * k)` |
| [204. Count Primes](https://leetcode.com/problems/count-primes/) | Medium | A sieve crosses out the multiples of each prime, using a step |
| [58. Length of Last Word](https://leetcode.com/problems/length-of-last-word/) | Easy | Walk back from the end of the string: `range(len(s) - 1, -1, -1)` |
| [66. Plus One](https://leetcode.com/problems/plus-one/) | Easy | Add 1 at the last digit, and carry to the left |

## 3. For loops

Lesson: [03_for_loops.py](03_for_loops.py)

| Problem | Level | Hint |
|---|---|---|
| [771. Jewels and Stones](https://leetcode.com/problems/jewels-and-stones/) | Easy | Loop over `stones`, and test `ch in jewels` |
| [1480. Running Sum of 1d Array](https://leetcode.com/problems/running-sum-of-1d-array/) | Easy | From index 1 on, add the total so far at `i - 1` |
| [1446. Consecutive Characters](https://leetcode.com/problems/consecutive-characters/) | Easy | Compare `s[i]` with `s[i - 1]` |
| [1512. Number of Good Pairs](https://leetcode.com/problems/number-of-good-pairs/) | Easy | Check every pair `i < j` |
| [1534. Count Good Triplets](https://leetcode.com/problems/count-good-triplets/) | Easy | Three nested loops |
| [1. Two Sum](https://leetcode.com/problems/two-sum/) | Easy | `for i, x in enumerate(nums)`, look up `target - x` among the numbers seen so far (in a dict, 06_collections) |
| [1790. Check if One String Swap Can Make Strings Equal](https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/) | Easy | Loop over the two strings with `zip()`, and note where they differ |
| [1768. Merge Strings Alternately](https://leetcode.com/problems/merge-strings-alternately/) | Easy | Loop over the two words with `zip()`, then add the rest of the longer one (`zip()` drops it) |
