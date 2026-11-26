# Collections: problems

Practice problems for the lessons in this folder, in lesson order.
Do a lesson first, then its problems. The tips for each lesson are in
[summary.md](summary.md).

76 problems: 61 Easy, 14 Medium, 1 Hard. All are free.

## 1. Lists

Lesson: [01_lists.py](01_lists.py)

| Problem | Level | Hint |
|---|---|---|
| [1920. Build Array from Permutation](https://leetcode.com/problems/build-array-from-permutation/) | Easy | `ans[i]` is `nums[nums[i]]`, an index read from the list itself |
| [867. Transpose Matrix](https://leetcode.com/problems/transpose-matrix/) | Easy | The item at `grid[r][c]` moves to `[c][r]` |
| [1470. Shuffle the Array](https://leetcode.com/problems/shuffle-the-array/) | Easy | The two halves are `nums[:n]` and `nums[n:]` |
| [1480. Running Sum of 1d Array](https://leetcode.com/problems/running-sum-of-1d-array/) | Easy | `nums[i] += nums[i - 1]` for each `i` from 1 (with a loop, 05_loops) |
| [1748. Sum of Unique Elements](https://leetcode.com/problems/sum-of-unique-elements/) | Easy | The values are 1 to 100, so `[0] * 101` counts how often each one appears |
| [1929. Concatenation of Array](https://leetcode.com/problems/concatenation-of-array/) | Easy | The answer is `nums + nums` |

## 2. List methods

Lesson: [02_list_methods.py](02_list_methods.py)

| Problem | Level | Hint |
|---|---|---|
| [1672. Richest Customer Wealth](https://leetcode.com/problems/richest-customer-wealth/) | Easy | `sum()` of each row, then the largest |
| [1491. Average Salary Excluding the Minimum and Maximum Salary](https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/) | Easy | Take `min()` and `max()` out of `sum()`, then divide by `len()` minus 2 |
| [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | Easy | `append()` each opening bracket, and `pop()` it when its closing bracket comes |
| [682. Baseball Game](https://leetcode.com/problems/baseball-game/) | Easy | The scores so far live on a stack |
| [1389. Create Target Array in the Given Order](https://leetcode.com/problems/create-target-array-in-the-given-order/) | Easy | One `insert()` for each `i`. The lists have at most 100 items, so that is fast enough |
| [1346. Check If N and Its Double Exist](https://leetcode.com/problems/check-if-n-and-its-double-exist/) | Easy | A first answer asks whether `x * 2 in arr` for each `x` (watch out for 0: its double is itself) |
| [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | Easy | After sorting, equal items are neighbours |
| [1913. Maximum Product Difference Between Two Pairs](https://leetcode.com/problems/maximum-product-difference-between-two-pairs/) | Easy | After sorting, the two largest and two smallest are at the ends |
| [989. Add to Array-Form of Integer](https://leetcode.com/problems/add-to-array-form-of-integer/) | Easy | The digits of the answer come out last digit first. Collect them, then reverse |

## 3. Shallow and deep copy

Lesson: [03_shallow_and_deep_copy.py](03_shallow_and_deep_copy.py)

| Problem | Level | Hint |
|---|---|---|
| [78. Subsets](https://leetcode.com/problems/subsets/) | Medium | Each subset you save must be a copy of the current one |
| [289. Game of Life](https://leetcode.com/problems/game-of-life/) | Medium | Every cell changes at once, so a first answer reads from a copy. `board.copy()` shares the rows: copy each row |

## 4. Tuples

Lesson: [04_tuples.py](04_tuples.py)

| Problem | Level | Hint |
|---|---|---|
| [1496. Path Crossing](https://leetcode.com/problems/path-crossing/) | Easy | Keep every point `(x, y)` you have visited as a tuple in a set |
| [747. Largest Number At Least Twice of Others](https://leetcode.com/problems/largest-number-at-least-twice-of-others/) | Easy | When the largest number passes the test, the answer is its index |

## 5. Unpacking

Lesson: [05_unpacking.py](05_unpacking.py)

| Problem | Level | Hint |
|---|---|---|
| [344. Reverse String](https://leetcode.com/problems/reverse-string/) | Easy | Swap the two ends, then move both inwards |
| [905. Sort Array By Parity](https://leetcode.com/problems/sort-array-by-parity/) | Easy | Swap each even number to the front |

## 6. Dictionaries

Lesson: [06_dictionaries.py](06_dictionaries.py)

| Problem | Level | Hint |
|---|---|---|
| [13. Roman to Integer](https://leetcode.com/problems/roman-to-integer/) | Easy | `{'I': 1, 'V': 5, 'X': 10, ...}` gives the value of each letter |
| [763. Partition Labels](https://leetcode.com/problems/partition-labels/) | Medium | `last[ch]`, the last index of letter `ch`, tells how far that letter reaches |
| [1. Two Sum](https://leetcode.com/problems/two-sum/) | Easy | Store each number's index as you go. For each new `x`, ask: is `target - x` already a key? |
| [509. Fibonacci Number](https://leetcode.com/problems/fibonacci-number/) | Easy | The classic first memo problem |
| [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) | Easy | The same rule as Fibonacci, so the same memo |
| [904. Fruit Into Baskets](https://leetcode.com/problems/fruit-into-baskets/) | Medium | The window may hold at most 2 kinds of fruit, so `len(d)` must stay at most 2 |
| [169. Majority Element](https://leetcode.com/problems/majority-element/) | Easy | The key whose count is more than `n // 2` |
| [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/) | Easy | Count the letters of both strings, then compare the two dicts with `==` |
| [383. Ransom Note](https://leetcode.com/problems/ransom-note/) | Easy | Count the magazine's letters, then spend them on the note |
| [387. First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string/) | Easy | Count, then walk the string again and stop at the first letter whose count is 1 |
| [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/) | Medium | Anagrams share their sorted letters, so the key is `tuple(sorted(word))`: a list can't be a key |
| [1971. Find if Path Exists in Graph](https://leetcode.com/problems/find-if-path-exists-in-graph/) | Easy | Build the adjacency list from the edges first |

## 7. Sets

Lesson: [07_sets.py](07_sets.py)

| Problem | Level | Hint |
|---|---|---|
| [1832. Check if the Sentence Is Pangram](https://leetcode.com/problems/check-if-the-sentence-is-pangram/) | Easy | The sentence uses every letter when its set of characters has 26 items |
| [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | Medium | A set holds the letters of a sliding window, a stretch of the string that moves along it. Remove letters from its left end while a repeat is in it |
| [2351. First Letter to Appear Twice](https://leetcode.com/problems/first-letter-to-appear-twice/) | Easy | The answer is the first letter that is already in `seen` |
| [771. Jewels and Stones](https://leetcode.com/problems/jewels-and-stones/) | Easy | Put the jewels in a set, then check each stone |
| [202. Happy Number](https://leetcode.com/problems/happy-number/) | Easy | Keep the numbers seen so far in a set. Meeting one again means they go round in a loop forever |
| [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | Easy | There is a repeat when the set is smaller than the list |
| [349. Intersection of Two Arrays](https://leetcode.com/problems/intersection-of-two-arrays/) | Easy | The numbers in both, with `&` |
| [2215. Find the Difference of Two Arrays](https://leetcode.com/problems/find-the-difference-of-two-arrays/) | Easy | One set minus the other, both ways round |
| [1684. Count the Number of Consistent Strings](https://leetcode.com/problems/count-the-number-of-consistent-strings/) | Easy | Count the words whose letters are all allowed: `set(word) <= set(allowed)` |
| [500. Keyboard Row](https://leetcode.com/problems/keyboard-row/) | Easy | A word fits when its letters are a subset of one keyboard row |
| [733. Flood Fill](https://leetcode.com/problems/flood-fill/) | Easy | Spread from one cell; visited cells are skipped |
| [200. Number of Islands](https://leetcode.com/problems/number-of-islands/) | Medium | A visited set of `(row, col)` cells stops BFS or DFS from counting a cell twice |

## 8. Deque

Lesson: [08_deque.py](08_deque.py)

| Problem | Level | Hint |
|---|---|---|
| [994. Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) | Medium | The queue starts with every rotten orange at once: `deque(list_of_rotten_cells)` |
| [933. Number of Recent Calls](https://leetcode.com/problems/number-of-recent-calls/) | Easy | Append each new time, and `popleft()` the times more than 3000 ms old |
| [239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) | Hard | The deque keeps the candidates, and `dq[0]` is the current maximum (shown in python-for-cp, 03_collections/01_deque.py) |
| [1971. Find if Path Exists in Graph](https://leetcode.com/problems/find-if-path-exists-in-graph/) | Easy | BFS from `source`, then check whether `destination` was reached |
| [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) | Medium | BFS over a tree, one level at a time |
| [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | Easy | The classic stack problem (use a list) |
| [1823. Find the Winner of the Circular Game](https://leetcode.com/problems/find-the-winner-of-the-circular-game/) | Medium | Rotate the circle so the friend who leaves is at the left, then `popleft()` |
| [643. Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/) | Easy | A window of exactly `k` numbers, done with a running sum |

## 9. Split and join

Lesson: [09_split_and_join.py](09_split_and_join.py)

| Problem | Level | Hint |
|---|---|---|
| [58. Length of Last Word](https://leetcode.com/problems/length-of-last-word/) | Easy | `s.split()[-1]` is the last word, even when `s` ends with spaces |
| [2114. Maximum Number of Words Found in Sentences](https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/) | Easy | `len(s.split())` is the number of words |
| [151. Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/) | Medium | `split()` drops the extra spaces for you |
| [2788. Split Strings by Separator](https://leetcode.com/problems/split-strings-by-separator/) | Easy | Split each string, and drop the empty pieces |
| [71. Simplify Path](https://leetcode.com/problems/simplify-path/) | Medium | Split the path at `'/'`. The empty pieces and `'.'` mean "stay here" |
| [165. Compare Version Numbers](https://leetcode.com/problems/compare-version-numbers/) | Medium | `split('.')` and `map(int, ...)` turn `'1.01'` into the numbers 1 and 1 |
| [1816. Truncate Sentence](https://leetcode.com/problems/truncate-sentence/) | Easy | Join the first `k` words back with `' '` |
| [1108. Defanging an IP Address](https://leetcode.com/problems/defanging-an-ip-address/) | Easy | Split at `'.'`, then join with `'[.]'` |
| [557. Reverse Words in a String III](https://leetcode.com/problems/reverse-words-in-a-string-iii/) | Easy | Reverse each word, then join |
| [1528. Shuffle String](https://leetcode.com/problems/shuffle-string/) | Easy | Put each character at its new index in a list, then join the list |

## 10. Comprehensions

Lesson: [10_comprehensions.py](10_comprehensions.py)

| Problem | Level | Hint |
|---|---|---|
| [1431. Kids With the Greatest Number of Candies](https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/) | Easy | Compare every kid with `max(candies)`, worked out once |
| [1920. Build Array from Permutation](https://leetcode.com/problems/build-array-from-permutation/) | Easy | One comprehension over the indexes |
| [977. Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/) | Easy | A first answer squares every number, then sorts |
| [905. Sort Array By Parity](https://leetcode.com/problems/sort-array-by-parity/) | Easy | The even numbers, then the odd numbers, each list made with a filter |
| [2942. Find Words Containing Character](https://leetcode.com/problems/find-words-containing-character/) | Easy | Keep each index `i` whose word contains `x` (with `enumerate()`, 05_loops) |
| [599. Minimum Index Sum of Two Lists](https://leetcode.com/problems/minimum-index-sum-of-two-lists/) | Easy | Map each name in `list1` to its index |
| [1331. Rank Transform of an Array](https://leetcode.com/problems/rank-transform-of-an-array/) | Easy | Map each different value to its rank, going through `sorted(set(arr))` |
| [804. Unique Morse Code Words](https://leetcode.com/problems/unique-morse-code-words/) | Easy | A set of each word's code, then `len()` |
| [929. Unique Email Addresses](https://leetcode.com/problems/unique-email-addresses/) | Easy | A set of cleaned-up addresses (cut with `split('@')`, 09_split_and_join.py) |
| [1672. Richest Customer Wealth](https://leetcode.com/problems/richest-customer-wealth/) | Easy | `max()` over a generator of row sums |
| [1365. How Many Numbers Are Smaller Than the Current Number](https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/) | Easy | For each `x`, `sum(y < x for y in nums)` is a first answer |
| [62. Unique Paths](https://leetcode.com/problems/unique-paths/) | Medium | A DP grid with one count for each cell |
| [118. Pascal's Triangle](https://leetcode.com/problems/pascals-triangle/) | Easy | Row `i` is `[1] * (i + 1)`, one new list per row |
