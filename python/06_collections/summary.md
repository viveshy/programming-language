# Collections: summary

Read this after the lessons, and again before a contest or an interview.
Each lesson has two parts:

- **Tips to remember:** the facts and the mistakes to avoid, with the reason.
- **What to expect in CP/DSA:** where the topic shows up in competitive
  programming (CP) and in the data structures and algorithms (DSA) problems of
  coding interviews.

Practice problems for this folder are in [problems.md](problems.md).

## 1. Lists

Lesson: [01_lists.py](01_lists.py)

### Tips to remember

- Indexes start at 0, so the last index is `len(a) - 1`, not `len(a)`. With
  `numbers = [1, 2, 3, 4]`, `numbers[4]` stops with an IndexError: list index
  out of range.
- Negative indexes count from the end: `numbers[-1]` is the last item, the same
  one as `numbers[len(numbers) - 1]`.
- A grid is a list of lists: `grid[r][c]` is row r, column c. With
  `grid = [[1, 2, 3], [4, 5, 6]]`, `grid[1][0] == 4`. `len(grid)` counts the
  rows (2) and `len(grid[0])` the columns (3).
- A slice takes its start index but not its end: `numbers[1:3] == [2, 3]`, the
  items at index 1 and 2. Leave out the start to begin at 0, or the end to go
  to the end.
- `a[:]` is a new list with every item: a copy (03_shallow_and_deep_copy.py).
- Indexing past the end stops with an IndexError, but slicing past the end does
  not. The slice quietly stops at the end, so it can come back short:
  `[1, 2, 3][1:10] == [2, 3]` and `[1, 2, 3][5:] == []`.
- Unlike a string, a list can be changed in place: `numbers[0] = 10`.
- A list can't grow that way: on a list of 4 items, `numbers[4] = 50` stops
  with an IndexError. To add at the end, use `.append()` (02_list_methods.py).
- `+` joins two lists into a new one: `[1, 2] + [3] == [1, 2, 3]`. `*` repeats
  the items: `[0] * 3 == [0, 0, 0]`.
- `[0] * n` is fine for numbers, but `[[0] * m] * n` repeats ONE inner list n
  times, so changing one row changes them all (03_shallow_and_deep_copy.py).
  For a grid, write `[[0] * m for _ in range(n)]` (10_comprehensions.py).

### What to expect in CP/DSA

- Every array in a problem (`nums`, `arr`, `a`) is a list. Mixed types are
  rare: a contest list almost always holds one type.
- `a[i]` and `a[i - 1]` compare an item with the one before it.
- An index can come from the list itself: `nums[nums[i]]`.
- The transpose of a grid swaps its rows and columns: the item at `grid[r][c]`
  moves to `[c][r]`.
- `a[:n]` and `a[n:]` split a list in two: the first n items and the rest.
- A slice copies every item it takes, so slicing a long list inside a loop is
  slow. Use indexes there instead.
- Update an array in place: `a[i] += a[i - 1]` for each i from 1 (with a loop,
  05_loops) gives running sums, each item the total so far: `[1, 2, 3, 4]`
  becomes `[1, 3, 6, 10]`.
- `[0] * n` makes n counters, one per possible value. When the values go from
  1 to 100, `cnt = [0] * 101` has indexes 0 to 100, and `cnt[x] += 1` counts
  each x.

## 2. List methods

Lesson: [02_list_methods.py](02_list_methods.py)

### Tips to remember

- `min([])` and `max([])` stop with a ValueError: an empty list has no smallest
  or largest item. `sum([])` is fine: 0.
- `.append(x)` adds x at the end, and `.pop()` removes the last item and gives
  it back. Both are fast however long the list is.
- `.pop()` on an empty list stops with an IndexError. Check first, because an
  empty list is False (04_conditionals/05_falsy.py): `if stack: stack.pop()`.
- A list keeps its items side by side in memory, so `pop(0)` and `insert(0, x)`
  shift every other item by one place: slow on a long list.
- Taking items from the front with `pop(0)`, one by one, shifts about
  `n * n / 2` items in total: billions for `n = 10**5`, so Time Limit Exceeded.
  Use a deque (fast at both ends) and its `popleft()` instead (08_deque.py).
- `in` is an operator, like `+` or `==`, not a method: `3 in nums` gives True
  or False. `.count(x)` is a method, and a missing x counts 0, not an error.
- `in` and `.count()` look at every item, one by one, so inside a loop over a
  long list they are slow. For many checks, put the items in a set first
  (07_sets.py), or count them all at once in a dictionary (06_dictionaries.py).
- `sorted(a)` gives back a NEW sorted list and leaves `a` alone. `a.sort()`
  sorts `a` itself and gives back None, so `nums = nums.sort()` sets `nums` to
  None and loses your list: just write `nums.sort()`.
- `reverse=True` sorts from largest to smallest, and `key=len` sorts by each
  item's length: `sorted(['banana', 'kiwi', 'apple'], key=len)` gives
  `['kiwi', 'apple', 'banana']`. `a.sort()` takes them too.
- `append()`, `insert()` and `reverse()` also give back None. `pop()` is the
  odd one: it gives back the item.

### What to expect in CP/DSA

- `sum(a)` for a total, `max(a) - min(a)` for the gap from the smallest to the
  largest. A grid's biggest row total: `sum()` each row, then take the largest.
- The average without the smallest and the largest item: take `min(a)` and
  `max(a)` out of `sum(a)`, then divide by `len(a) - 2`.
- A list is a stack: `append()` puts an item on top, `pop()` takes the newest
  item off, and `stack[-1]` looks at it. To check brackets, push each opening
  bracket, and pop it when its closing bracket comes.
- BFS (breadth-first search) takes items from the front of a queue: use
  `deque.popleft()`, never `list.pop(0)`.
- On short lists, `pop(i)` and `insert(i, x)` are fine: with at most 100 items,
  one `insert()` per item is fast enough.
- `in` and `count()` are fine for one check, or on a short list. To find an x
  whose double is also in `arr`, a first answer asks `x * 2 in arr` for each x.
  Watch out for 0: its double is itself.
- Sorting first makes many problems easier: equal items end up side by side,
  and the smallest and largest are at the two ends.
- `key=` sorts by any rule you write (with lambda, 07_functions).
- Build a list from the back with `append()`, then `reverse()` once at the
  end. This is cheaper than `insert(0, x)` for every item. When the digits of
  an answer come out last digit first, collect them, then reverse.

## 3. Shallow and deep copy

Lesson: [03_shallow_and_deep_copy.py](03_shallow_and_deep_copy.py)

### Tips to remember

- `b = a` does not copy: both names point to ONE list, so a change through one
  name shows up through the other.
- `is` asks "the very same object?" and `==` asks "equal values?". To compare
  items, use `==`: `is` only tells you whether two names share one list.
- Two lists with equal items are still two lists: after `first = [1, 2]` and
  `second = [1, 2]`, `first == second` is True and `first is second` is False.
- For numbers, `x += 1` and `x = x + 1` do the same thing. For lists they
  differ, and you see it as soon as two names share one list.
- `b += [2]` changes the list itself, so every name for it sees the change.
  `b = b + [3]` builds a NEW list and points only `b` at it.
- What each way shares (`copy.deepcopy` needs `import copy`):

| Code | What you get | Outer list | Inner lists |
|---|---|---|---|
| `b = a` | one list, two names | shared | shared |
| `b = a.copy()`, `a[:]` or `list(a)` | shallow copy | new | shared |
| `b = copy.deepcopy(a)` | deep copy | new | new |

- A shallow copy of a flat list (no lists inside) is safe: changing the copy
  does not touch the original, and the other way round.
- In a shallow copy of a nested list (a list of lists), changing an item inside
  an inner list shows up in the original. Replacing a whole inner list,
  `shallow[1] = ['new']`, changes only the copy.
- So `grid.copy()` or `grid[:]` shares every row: marking a cell in the "copy"
  marks it in the original grid too. Copy each row instead:
  `[row[:] for row in grid]` (10_comprehensions.py).

### What to expect in CP/DSA

- A function that gets a list gets the same list, not a copy, so a change it
  makes shows up outside (07_functions).
- To keep a list as it is now, save a copy before you change it again. When
  you list all subsets, each subset you save must be a copy of the current one.
- Backtracking (a search that adds items to one list, `path`, and takes them
  off again) must save `path[:]`, not `path`. Otherwise every saved answer is
  the same list, and it changes as the search goes on.
- BFS and DP (dynamic programming) that keep the old grid while they build the
  new one must copy it row by row, or the grid quietly breaks: Wrong Answer.
- When every cell of a board changes at once, a first answer reads from a copy
  of the board. `board.copy()` shares the rows: copy each one.
- `copy.deepcopy` is slow on a big grid. For a grid of numbers or letters,
  copying each row is enough and much faster.

## 4. Tuples

Lesson: [04_tuples.py](04_tuples.py)

### Tips to remember

- The comma makes the tuple, not the parentheses: `point = 3, 4` is the tuple
  `(3, 4)`. So `(5)` is just the number 5 in brackets: a tuple with one item
  needs a comma, `(5,)`.
- Indexing and slicing work just like lists, and a slice of a tuple is a tuple:
  `(1, 2, 3, 4, 5)[1:4] == (2, 3, 4)`.
- A tuple can't be changed after it is made (it is immutable): `t[0] = 10`
  raises TypeError. A list allows the same change.
- To check that a line raises an error, put it inside `try:`. If it raises the
  error named in `except`, Python jumps to the except block instead of
  stopping. Record what happened in a variable, then assert it.
- Because a tuple can't change, `(row, col)` can be a dictionary key or a set
  item. A list can't (06_dictionaries.py, 07_sets.py).
- A tuple has only two ordinary methods, `count(x)` and `index(x)`. It has no
  `append()` or `sort()`, because it can't change.
- `index(x)` gives the index of the FIRST x: `('a', 'b', 'a', 'c').index('a')`
  is 0.
- `index(x)` raises a ValueError when x is missing. It does not give -1 like a
  string's `.find()`, so check with `x in t` first.

### What to expect in CP/DSA

- A grid cell is a pair `(row, col)`, and a point on a plane is `(x, y)`.
- A function can give back several values as one tuple: `return a, b`
  (07_functions).
- `point[0]` and `point[1]` read the row and column, but more often you unpack
  the pair: `r, c = point` (05_unpacking.py).
- Keep the cells or points you have visited as tuples in a set:
  `visited = {(0, 0), (0, 1)}`, then ask `(0, 1) in visited`.
- You meet `.index(x)` more on lists, which have it too, with the same
  ValueError. `a.index(max(a))` gives the index of the largest item.

## 5. Unpacking

Lesson: [05_unpacking.py](05_unpacking.py)

### Tips to remember

- Unpacking needs as many names as there are items: `x, y, z = (1, 3, 8)`. A
  list unpacks the same way.
- The wrong number of names stops with a ValueError: too few names give "too
  many values to unpack", too many names give "not enough values to unpack".
- `a, b = b, a` swaps two values, because the right side is built first, as
  the tuple `(b, a)`, and then unpacked into `a` and `b`.
- The names on the left are filled from left to right. With `nums = [1, 2, 0]`,
  `nums[0], nums[nums[0]] = nums[nums[0]], nums[0]` should swap `nums[0]` and
  `nums[1]`, but `nums[0]` becomes 2 first, so `nums[2]` gets 1: `[2, 2, 1]`.
- So save the index first: after `j = nums[0]`,
  `nums[0], nums[j] = nums[j], nums[0]` gives `[2, 1, 0]`.
- `_` is an ordinary name. By habit, it means "I don't need this value", but
  it still holds the value: `length, breadth, height, _ = [40, 50, 60, 70]`
  sets `_` to 70.
- A name with `*` before it collects the items the other names don't take:
  `first, *rest = [1, 2, 3, 4]` gives `rest == [2, 3, 4]`. Only one name may
  have the `*`.
- The starred name always gets a list, even from a tuple, and even when no
  items are left for it: `head, *tail = (5,)` gives `tail == []`.

### What to expect in CP/DSA

- Read two numbers from one line: `n, m = map(int, input().split())` (`split`
  and `map` come in 09_split_and_join.py).
- Unpack in a for loop, `for i, x in enumerate(a)` (05_loops/03_for_loops.py),
  or unpack a grid cell, `r, c = cell`.
- Two pointers are two indexes, one at each end, that move towards each other
  (05_loops/01_while_loop.py). They swap with `a[i], a[j] = a[j], a[i]`. To
  reverse a list in place, swap the two ends, then move both inwards.
- To put the even numbers first, swap each even number to the front.
- `for _ in range(t)` repeats something without needing the counter: one turn
  for each of the t test cases.
- A line that starts with a count and then the numbers:
  `n, *nums = map(int, input().split())`. Otherwise `*` is rarely needed:
  `a[0]` and `a[1:]` do the same job.

## 6. Dictionaries

Lesson: [06_dictionaries.py](06_dictionaries.py)

### Tips to remember

- `{}` is an empty dict, not an empty set. An empty set is `set()` (07_sets.py).
- `d[key]` on a missing key stops with a KeyError. `d.get(key, 0)` gives the
  default, 0, instead, and `d.get(key)` with no default gives None.
- `d[key] = value` adds a new key, or silently replaces the old value. So a
  loop that stores each letter's index keeps the last one: over `'abca'`,
  `last['a']` ends as 3. To keep the first, store it only while the key is new.
- `key in d` takes O(1) time: the same short time however big the dict is. But
  it checks the keys, not the values: `7.99 in menu` is False, and
  `7.99 in menu.values()` checks the values one by one, like a list.
- `del d[key]` and `d.pop(key)` stop with a KeyError on a missing key.
  `d.pop(key, None)` gives None instead.
- Loops go in the order the keys were added (Python 3.7 and later). Adding or
  deleting keys while you loop over the same dict stops with a RuntimeError, so
  loop over a copy of the keys: `for k in list(d):`.
- A key must be hashable: a value that can't change, like str, int, float, or a
  tuple of such values. Python finds a key by a number made from it (its
  hash), so the key must never change.
- A list can change, so `{[0, 1]: 'wall'}` stops with a TypeError.
  `tuple(a_list)` makes a tuple with the same items, and that works.
- Count with `counts[x] = counts.get(x, 0) + 1`. `counts[x] += 1` stops with a
  KeyError the first time, because the key isn't there yet.
- Group with `if k not in groups: groups[k] = []`, then `groups[k].append(x)`.
  `d.get(k, []).append(x)` changes nothing: the new list is never stored.

### What to expect in CP/DSA

- Lookup tables are written once, at the top: `{'I': 1, 'V': 5, 'X': 10}`.
- Use `d[key]` when the key must be there: if it isn't, the KeyError shows the
  bug. Use `d.get(key, 0)` when a missing key just means "none yet".
- "Have I seen this before?" in O(1). For two numbers that add up to a target,
  store each number's index as you go. For each new x: is `target - x` a key?
- Memo tables: `memo` maps an input to its answer. Check it first, store each
  new answer, and nothing is worked out twice (needs recursion, 07_functions).
- Sliding window (a stretch of the list that moves along it): count the items
  inside in a dict, and delete a key when its count drops to 0. Then `len(d)`
  is the number of different items in the window.
- Counting is the most used dict pattern of all. Then loop over `items()` for
  the answer, compare two count dicts with `==`, or walk the string again and
  stop at the first letter whose count is 1.
- Problems rarely want insertion order: loop over `sorted(d)` for sorted keys.
- Grids use `(row, col)` tuples as keys: `dist[(r, c)] = steps`. Memo keys are
  often tuples too: `memo[(i, j)]` for a state with two numbers.
- Anagrams (the same letters in another order) share their sorted letters:
  group them under `tuple(sorted(word))`, since a list can't be a key.
- Graphs: `graph[u]`, the list of u's neighbours (an adjacency list), is built
  from the edges by grouping. BFS (breadth-first search) over it: 08_deque.py.
- `Counter` counts in one line, and `defaultdict(list)` makes the empty lists
  for you (python-for-cp, 03_collections/02_counter_and_defaultdict.py).

## 7. Sets

Lesson: [07_sets.py](07_sets.py)

### Tips to remember

- An empty set is `set()`. `{}` is an empty dict.
- `add(x)` twice keeps one x. `remove(x)` stops with a KeyError when x is
  missing, while `discard(x)` does nothing.
- `x in s` is O(1), but `x in a_list` checks the items one by one: O(n). Inside
  a loop over n items, that is about `n * n` steps, `10**10` for `n = 10**5`:
  Time Limit Exceeded. Make a set once, before the loop, and check against it.
- `len(set(a))` counts the different values. There is a repeat when
  `len(set(a)) < len(a)`.
- `list(set(names))` gives the names in no fixed order. To keep the order they
  first appeared in, use a loop and a `seen` set.
- Four operators combine two sets. With `a = {1, 2}` and `b = {2, 3}`:

| Code | Keeps the items | Gives |
|---|---|---|
| `a \| b` | in either set (union) | `{1, 2, 3}` |
| `a & b` | in both sets (intersection) | `{2}` |
| `a - b` | in a but not in b (difference) | `{1}` |
| `a ^ b` | in exactly one of them (symmetric difference) | `{1, 3}` |

- Difference has a direction: `b - a` is `{3}`, not `{1}`.
- `a <= b` asks whether every item of a is also in b (a is a "subset" of b).
- Items must be hashable, like dict keys: a tuple can go in, a list can't.
  `{[1, 2]}` stops with a TypeError.
- A set has no positions, so `s[0]` stops with a TypeError. Its order is not
  fixed, so printing a set straight away is a Wrong Answer when the judge wants
  increasing order. Use `sorted(s)`.

### What to expect in CP/DSA

- "Have I seen this before?" in O(1): check `x in seen`, then `seen.add(x)`.
  `remove()` takes a thing back out, as when letters leave a sliding window.
- Put the things to look for in a set once, then check each item against it.
- When a step is repeated on a number, keep the numbers seen so far in a set.
  Meeting one again means they go round in a loop forever.
- A string of the letters a to z uses every one when `len(set(s)) == 26`.
- `set(a) & set(b)` gives the values in both lists. `set(a) - set(b)` gives
  those only in a, and `set(b) - set(a)` those only in b.
- "Does this word use only these letters?" is `set(word) <= set(allowed)`.
- BFS and DFS are two ways to explore a grid or a graph step by step. Both keep
  a visited set of `(row, col)` cells, so no cell is visited or counted twice.
- "Print the different values in increasing order" is `sorted(set(a))`.

## 8. Deque

Lesson: [08_deque.py](08_deque.py)

### Tips to remember

- Start with `from collections import deque`. Each end has its own methods, and
  adding or removing one item takes O(1) time:

| End | Add one | Remove one | Add many |
|---|---|---|---|
| right | `append(x)` | `pop()` | `extend(items)` |
| left | `appendleft(x)` | `popleft()` | `extendleft(items)` |

- `deque(items)` takes the items out of what you give it. A start cell like
  `(0, 0)` is a tuple, so `deque(start)` holds two numbers, 0 and 0. Write
  `deque([start])` for one cell.
- `pop()` and `popleft()` on an empty deque stop with an IndexError. An empty
  deque is falsy, like an empty list, so loop with `while queue:`.
- Queue (first in, first out): `append()` and `popleft()`. Stack (last in,
  first out): `append()` and `pop()`, on a plain list.
- Never use `list.pop(0)` as a queue: it shifts every other item one place,
  O(n) for each pop, and over a whole BFS that is a Time Limit Exceeded.
- `rotate(2)` moves every item 2 places right, and the items that fall off the
  right end come back in at the left. `rotate(-2)` moves them left.
- `deque(maxlen=3)` keeps the newest 3 items: adding to a full deque drops an
  item from the other end.
- `extendleft(items)` adds the items one at a time at the left, so they end up
  reversed: `extendleft([0, -1])` puts -1 first.

### What to expect in CP/DSA

- BFS (breadth-first search) visits places in order of their distance from the
  start: the start, then everything 1 step away, then 2, and so on. A queue
  gives exactly that order: `while queue:`, take `node = queue.popleft()` and
  append each neighbour not yet in `dist`, with `dist[nxt] = dist[node] + 1`.
- BFS also tells whether one place can reach another, or goes over a tree one
  level at a time. A BFS from many cells at once starts with `deque(cells)`.
- `appendleft()` is rarer. In "0-1 BFS", where some moves cost nothing, those
  moves go to the front of the queue.
- In a sliding window, `popleft()` drops the items that left it, such as times
  that are too old.
- For the largest item of each window, a deque keeps the candidates, and `dq[0]`
  is the largest (python-for-cp, 03_collections/01_deque.py).
- Matching brackets is the classic stack problem: use a list.
- `rotate()` fits games where people stand in a circle: rotate the one who
  leaves to the left end, then `popleft()`.
- `maxlen` keeps the last k items with no extra code. For a window of k
  numbers, a running sum is usually simpler: add the number that comes in,
  subtract the one that leaves.
- In BFS each neighbour is checked before it goes in, so it is appended one at
  a time, not with `extend()`.

## 9. Split and join

Lesson: [09_split_and_join.py](09_split_and_join.py)

### Tips to remember

- `split()` with no argument cuts at any run of spaces, tabs or newlines, and
  ignores them at both ends: `'  3 1\t2\n'.split() == ['3', '1', '2']`.
- `split(sep)` counts every single separator, so two in a row leave an empty
  piece: `'a,,b'.split(',') == ['a', '', 'b']`.
- So `split(' ')` is not `split()`: `'a  b'.split(' ') == ['a', '', 'b']`, and
  `int('')` on the empty piece stops with a ValueError.
- `a = list(map(int, line.split()))` reads a line of numbers. When you know how
  many there are, unpack them: `a, b, c = map(int, line.split())`.
- `map()` is not a list. It gives the results one at a time, and only once:
  `lazy[0]` stops with a TypeError, and a second pass gives nothing. Wrap it in
  `list()` when you need a list.
- `sep.join(items)` is called on the separator: `' '.join(words)`. A list has
  no `join()`, so `words.join(' ')` stops with an AttributeError.
- `join()` accepts strings only: `'-'.join([1, 2, 3])` stops with a TypeError.
  Turn the numbers into strings first: `'-'.join(map(str, nums))`.
- `split(sep)` undoes `join(sep)` only when no item contains sep:
  `'-'.join(['a-b', 'c']).split('-')` gives 3 pieces, not 2.
- A string can't be changed. To change its characters, use `list(s)`, change
  the list, then glue it back with `''.join(...)`.

### What to expect in CP/DSA

- `split()` is safe on messy input: extra spaces, a space at the end, or the
  `'\n'` at the end of a line. `s.split()[-1]` is the last word even when s
  ends with spaces, and `len(s.split())` is the number of words.
- `split(':')` gives the hours and the minutes of a time like `'09:30'`. A path
  split at `'/'` has empty pieces and `'.'` pieces, which mean "stay here".
- Almost every contest solution reads its input this way: `n = int(input())`
  for a line with one number, `a = list(map(int, input().split()))` for a line
  of numbers.
- On big inputs, `input()` itself gets slow. Faster ways: python-for-cp,
  02_input_output/01_fast_input.py.
- `split('.')` and `map(int, ...)` turn a version like `'1.01'` into the
  numbers 1 and 1.
- Many string problems are split, change, join: cut the words with `split()`,
  change them or keep only some, then join them back with `' '.join(...)`.
- Printing answers: `print(' '.join(map(str, ans)))` puts them on one line with
  spaces, and `print('\n'.join(map(str, ans)))` puts one per line.
- Collect the answers in a list and print once at the end. Many `print()`
  calls, or `text += piece` in a loop, can be slow (python-for-cp,
  02_input_output/02_fast_output.py).
- To put each character at a new index, fill a list, then join it.

## 10. Comprehensions

Lesson: [10_comprehensions.py](10_comprehensions.py)

### Tips to remember

- `[x * x for x in a]` builds a new list, like a loop with `append()`.
- The expression runs once for every item, so a `max()` inside it walks the
  whole list each time: about `n * n` steps. Work it out once, before:
  `best = max(scores)`, then `[s == best for s in scores]`.
- An `if` at the end keeps only the items that pass: `[x for x in a if x > 0]`.
- An `if ... else` at the front picks a value for every item and drops none:
  `[x if x > 0 else 0 for x in [3, -1, 2]] == [3, 0, 2]`. An `if` at the end
  can't have an `else`: that is a SyntaxError.
- `{k: v for ...}` builds a dict. A key that comes twice keeps its last value:
  `{ch: i for i, ch in enumerate('abca')}['a'] == 3`.
- `{x for ...}`, with no colon, builds a set.
- Inside a call like `sum()`, a comprehension needs no brackets of its own: it
  is a generator expression, and no list is stored. `sum(x > 0 for x in a)`
  counts the items that pass, because True counts as 1.
- Round brackets make a generator you can store in a name. Like `map()`, it can
  be used only once: after `gen = (x * x for x in range(4))`, the first
  `sum(gen)` is 14 and the second is 0.
- A grid of n rows is `[[0] * m for _ in range(n)]`. Never write
  `[[0] * m] * n`: it repeats the same inner list n times, so changing one row
  changes every row (03_shallow_and_deep_copy.py shows why).

### What to expect in CP/DSA

- Change every item of a list: `[int(x) for x in line.split()]` gives the same
  list as `list(map(int, line.split()))`.
- One comprehension over the indexes builds a new array from an old one. A
  first answer often changes every item, then sorts.
- Filters build lists like "the even numbers, then the odd numbers". With
  `enumerate()`, a filter can keep the indexes instead:
  `[i for i, w in enumerate(words) if x in w]`.
- A dict comprehension makes a value-to-index map, for O(1) lookups:
  `{v: i for i, v in enumerate(a)}`. Going through `sorted(set(a))` maps each
  different value to its rank.
- A set comprehension, then `len()`, counts the different results of a change.
- A generator adds up, counts or finds the best with no extra list:
  `max(sum(row) for row in grid)`. For each x, `sum(y < x for y in nums)`
  counts the smaller numbers.
- DP (dynamic programming: answers built from smaller answers, kept in a
  table) needs a grid: `dp = [[0] * (m + 1) for _ in range(n + 1)]`.
- A grid BFS marks cells in `visited = [[False] * m for _ in range(n)]`.
- Read a grid of n lines with `grid = [input() for _ in range(n)]`.
