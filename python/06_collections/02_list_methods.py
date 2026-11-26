"""
Functions and methods read a list or change it. A method is a function you
call with a dot after the value: a.append(4).

    ┌────────────────┬───────────────────────────────────────────────┐
    │ Code           │ What it does                                  │
    ├────────────────┼───────────────────────────────────────────────┤
    │ len(a)         │ how many items                                │
    │ min(a), max(a) │ the smallest and the largest item             │
    │ sum(a)         │ all the items added up                        │
    │ sorted(a)      │ a NEW sorted list (a is unchanged)            │
    │ a.append(x)    │ add x at the end                              │
    │ a.pop()        │ remove the last item and give it back         │
    │ a.pop(i)       │ remove the item at index i and give it back   │
    │ a.insert(i, x) │ put x at index i                              │
    │ a.count(x)     │ how many times x appears                      │
    │ a.sort()       │ sort the list itself                          │
    │ a.reverse()    │ reverse the list itself                       │
    │ x in a         │ True if x is in a (an operator, not a method) │
    └────────────────┴───────────────────────────────────────────────┘

Why it matters: almost every solution builds a list with append, sorts it or
adds it up. Some of them are slow on long lists, which can mean Time Limit
Exceeded.

We will cover:
1. len(), min(), max(), sum()
2. append() and pop(): the end of the list
3. pop(i) and insert(i, x): slow at the front
4. in and count(): is it there, and how often?
5. sorted() vs sort()
6. reverse()
"""


# ┌────────────────────────────────────────────────────────────┐
# │ 1. LEN(), MIN(), MAX(), SUM()                              │
# └────────────────────────────────────────────────────────────┘
# These functions read the list and give back one value. The list is unchanged.

nums = [5, 3, 8, 1, 2]

assert len(nums) == 5
assert min(nums) == 1
assert max(nums) == 8
assert sum(nums) == 19


# ┌────────────────────────────────────────────────────────────┐
# │ 2. APPEND() AND POP(): THE END OF THE LIST                 │
# └────────────────────────────────────────────────────────────┘
# .append(x) adds x at the end. .pop() removes the last item and gives it back.
# Both change the list itself, and both are fast however long the list is.

stack = [1, 2]
stack.append(3)
assert stack == [1, 2, 3]

top = stack.pop()
assert top == 3
assert stack == [1, 2]


# ┌────────────────────────────────────────────────────────────┐
# │ 3. POP(I) AND INSERT(I, X): SLOW AT THE FRONT              │
# └────────────────────────────────────────────────────────────┘
# .pop(i) removes the item at index i. .insert(i, x) puts x at index i.

letters = ['a', 'b', 'c', 'd']

assert letters.pop(1) == 'b'
assert letters == ['a', 'c', 'd']

letters.insert(0, 'z')
assert letters == ['z', 'a', 'c', 'd']

assert letters.pop(0) == 'z'  # pop(0) removes the first item
assert letters == ['a', 'c', 'd']

# A list keeps its items side by side in memory. Removing or inserting at
# index i shifts every item after i by one place:
# - pop() at the end shifts nothing: fast.
# - pop(0) and insert(0, x) shift every other item: slow on a long list.


# ┌────────────────────────────────────────────────────────────┐
# │ 4. IN AND COUNT(): IS IT THERE, AND HOW OFTEN?             │
# └────────────────────────────────────────────────────────────┘
# in is an operator, like + or ==. x in a gives True or False.
# .count(x) is a method: how many times x appears.

assert (3 in nums) is True
assert (7 in nums) is False

assert [1, 2, 1, 1].count(1) == 3
assert nums.count(7) == 0  # missing: 0, not an error


# ┌────────────────────────────────────────────────────────────┐
# │ 5. SORTED() VS SORT()                                      │
# └────────────────────────────────────────────────────────────┘
# sorted(a) gives back a NEW sorted list and leaves a alone.

assert sorted(nums) == [1, 2, 3, 5, 8]
assert nums == [5, 3, 8, 1, 2]  # unchanged

# reverse=True sorts from largest to smallest.
# key=len sorts by each item's length instead of the item itself.

assert sorted(nums, reverse=True) == [8, 5, 3, 2, 1]

words = ['banana', 'kiwi', 'apple']
assert sorted(words) == ['apple', 'banana', 'kiwi']  # alphabetical
assert sorted(words, key=len) == ['kiwi', 'apple', 'banana']  # shortest first

# a.sort() sorts the list itself. It takes the same reverse= and key=.

nums.sort()
assert nums == [1, 2, 3, 5, 8]

# a.sort() gives back None, not the sorted list.

assert nums.sort() is None


# ┌────────────────────────────────────────────────────────────┐
# │ 6. REVERSE()                                               │
# └────────────────────────────────────────────────────────────┘
# a.reverse() reverses the list itself. Like sort(), it gives back None.

nums.reverse()
assert nums == [8, 5, 3, 2, 1]


print('All checks passed.')
