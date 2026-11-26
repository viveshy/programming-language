# Conditionals: problems

Practice problems for the lessons in this folder, in lesson order.
Do a lesson first, then its problems. The tips for each lesson are in
[summary.md](summary.md).

24 problems: 24 Easy. All are free.

## 1. If statements

Lesson: [01_if_statements.py](01_if_statements.py)

| Problem | Level | Hint |
|---|---|---|
| [2413. Smallest Even Multiple](https://leetcode.com/problems/smallest-even-multiple/) | Easy | One if-else on `n % 2` |
| [412. Fizz Buzz](https://leetcode.com/problems/fizz-buzz/) | Easy | Test "divisible by 3 and by 5" first, or the "divisible by 3" branch catches 15 (with a loop, 05_loops) |
| [2525. Categorize Box According to Criteria](https://leetcode.com/problems/categorize-box-according-to-criteria/) | Easy | Four answers, one chain |

## 2. Comparison operators

Lesson: [02_comparison_operators.py](02_comparison_operators.py)

| Problem | Level | Hint |
|---|---|---|
| [2798. Number of Employees Who Met the Target](https://leetcode.com/problems/number-of-employees-who-met-the-target/) | Easy | "Met" means `>=`, not `>` (with a loop, 05_loops) |
| [292. Nim Game](https://leetcode.com/problems/nim-game/) | Easy | Once you spot the pattern, the answer is one comparison |
| [733. Flood Fill](https://leetcode.com/problems/flood-fill/) | Easy | A neighbour cell is inside the picture only if `0 <= r < rows` and `0 <= c < cols` |
| [2264. Largest 3-Same-Digit Number in String](https://leetcode.com/problems/largest-3-same-digit-number-in-string/) | Easy | `x == y == z` tests three characters at once |

## 3. String comparison

Lesson: [03_string_comparison.py](03_string_comparison.py)

| Problem | Level | Hint |
|---|---|---|
| [2108. Find First Palindromic String in the Array](https://leetcode.com/problems/find-first-palindromic-string-in-the-array/) | Easy | Compare each word with the word reversed |
| [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | Easy | Upper and lower case count as the same letter, so lowercase the text first |
| [520. Detect Capital](https://leetcode.com/problems/detect-capital/) | Easy | Compare the word with `word.upper()` and `word.lower()` |
| [58. Length of Last Word](https://leetcode.com/problems/length-of-last-word/) | Easy | The text can end with spaces |
| [744. Find Smallest Letter Greater Than Target](https://leetcode.com/problems/find-smallest-letter-greater-than-target/) | Easy | Letters compare with `>` |
| [387. First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string/) | Easy | Count each letter in its `ord(c) - ord('a')` slot (lists come in 06_collections) |

## 4. Logical operators

Lesson: [04_logical_operators.py](04_logical_operators.py)

| Problem | Level | Hint |
|---|---|---|
| [463. Island Perimeter](https://leetcode.com/problems/island-perimeter/) | Easy | Is the cell next door inside the grid, and is it land? |
| [2119. A Number After a Double Reversal](https://leetcode.com/problems/a-number-after-a-double-reversal/) | Easy | The answer joins two tests with `or` |
| [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | Easy | Before you add `x` to `seen`, check `x in seen` |
| [1154. Day of the Year](https://leetcode.com/problems/day-of-the-year/) | Easy | February has 29 days in a leap year |
| [925. Long Pressed Name](https://leetcode.com/problems/long-pressed-name/) | Easy | Check `i < len(name)` before you use `name[i]` |
| [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | Easy | `while fast and fast.next:` (05_loops) |
| [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) | Easy | At the end, `list1 or list2` gives the list that still has nodes |

## 5. Falsy

Lesson: [05_falsy.py](05_falsy.py)

| Problem | Level | Hint |
|---|---|---|
| [1342. Number of Steps to Reduce a Number to Zero](https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/) | Easy | `while num:` loops until `num` is 0 |
| [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | Easy | An empty tree (`None`) has depth 0 |
| [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | Easy | `while head:` walks the list until `None` |
| [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | Easy | At the end, the stack must be empty |
