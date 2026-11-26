# Functions: problems

Practice problems for the lessons in this folder, in lesson order.
Do a lesson first, then its problems. The tips for each lesson are in
[summary.md](summary.md).

7 problems: 6 Easy, 1 Medium. All are free.

## 1. Functions

Lesson: [01_functions.py](01_functions.py)

| Problem | Level | Hint |
|---|---|---|
| [1550. Three Consecutive Odds](https://leetcode.com/problems/three-consecutive-odds/) | Easy | Return `True` the moment you see three odd numbers in a row, and `False` after the loop |
| [1636. Sort Array by Increasing Frequency](https://leetcode.com/problems/sort-array-by-increasing-frequency/) | Easy | A tuple key, frequency first, then the value from largest |
| [2418. Sort the People](https://leetcode.com/problems/sort-the-people/) | Easy | Sort the names by their heights |
| [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/) | Medium | Sort the intervals by their start |
| [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) | Easy | The same recursion as `fib`, but `n` goes up to 45, so plain recursion is too slow: add memoization |

## 2. Scope of variables

Lesson: [02_scope_of_variables.py](02_scope_of_variables.py)

| Problem | Level | Hint |
|---|---|---|
| [543. Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/) | Easy | `dfs` returns a depth, and updates a `nonlocal` best on the way |
| [938. Range Sum of BST](https://leetcode.com/problems/range-sum-of-bst/) | Easy | `dfs` adds to a `nonlocal` total |
