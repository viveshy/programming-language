# Strings: problems

Practice problems for the lessons in this folder, in lesson order.
Do a lesson first, then its problems. The tips for each lesson are in
[summary.md](summary.md).

15 problems: 15 Easy. All are free.

## 1. Strings

Lesson: [01_strings.py](01_strings.py)

| Problem | Level | Hint |
|---|---|---|
| [1812. Determine Color of a Chessboard Square](https://leetcode.com/problems/determine-color-of-a-chessboard-square/) | Easy | `coordinates[0]` is the column letter and `coordinates[1]` is the row digit |
| [796. Rotate String](https://leetcode.com/problems/rotate-string/) | Easy | Try every rotation `s[i:] + s[:i]` (loops come in 05_loops) |
| [2108. Find First Palindromic String in the Array](https://leetcode.com/problems/find-first-palindromic-string-in-the-array/) | Easy | Compare each word with `word[::-1]` |
| [557. Reverse Words in a String III](https://leetcode.com/problems/reverse-words-in-a-string-iii/) | Easy | Reverse each word with `[::-1]` (`split()` and `join()` come in 06_collections/09_split_and_join.py) |

## 2. Formatted strings

Lesson: [02_formatted_strings.py](02_formatted_strings.py)

| Problem | Level | Hint |
|---|---|---|
| [228. Summary Ranges](https://leetcode.com/problems/summary-ranges/) | Easy | Write each range as `f'{a}->{b}'` |
| [401. Binary Watch](https://leetcode.com/problems/binary-watch/) | Easy | The minutes always have two digits |
| [868. Binary Gap](https://leetcode.com/problems/binary-gap/) | Easy | `f'{n:b}'` gives the bits of `n` as text |

## 3. String methods

Lesson: [03_string_methods.py](03_string_methods.py)

| Problem | Level | Hint |
|---|---|---|
| [520. Detect Capital](https://leetcode.com/problems/detect-capital/) | Easy | Compare the word with `word.upper()` and `word.lower()` |
| [771. Jewels and Stones](https://leetcode.com/problems/jewels-and-stones/) | Easy | Ask `stone in jewels` for each stone (loops come in 05_loops) |
| [2000. Reverse Prefix of Word](https://leetcode.com/problems/reverse-prefix-of-word/) | Easy | `find()` says where to cut, and `-1` means leave the word as it is |
| [657. Robot Return to Origin](https://leetcode.com/problems/robot-return-to-origin/) | Easy | `count()` each move letter |
| [1678. Goal Parser Interpretation](https://leetcode.com/problems/goal-parser-interpretation/) | Easy | `replace()` each command with what it stands for |
| [58. Length of Last Word](https://leetcode.com/problems/length-of-last-word/) | Easy | `rstrip()` first, so the spaces at the end don't count |
| [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | Easy | Keep only the `isalnum()` characters, in `lower()` |
| [2496. Maximum Value of a String in an Array](https://leetcode.com/problems/maximum-value-of-a-string-in-an-array/) | Easy | `isdigit()` decides if a string counts as its number or as its length |
