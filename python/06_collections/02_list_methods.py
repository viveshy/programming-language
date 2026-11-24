"""
We will discuss the following list methods and functions:

Functions:
    1) len(list) => Returns the length of the list
    2) sorted(list) => Returns a NEW sorted list (the original is unchanged)
    3) min(list), max(list), sum(list) => Smallest item, largest item, total

Methods:
    1) .append(elem) => Adds an element to the end of the list
    2) .pop() => Removes and returns the last element
    3) elem in list => Checks if an element is present in the list
    4) .count(elem) => Counts occurrences of an element
    5) .sort() => Sorts the list itself, in ascending order
    6) .reverse() => Reverses the list itself
"""

sample_list = [5, 3, 8, 1, 2]

# 1. len()
# _______________
assert len(sample_list) == 5

# 2. .append(elem)
# _______________
sample_list.append(6)
assert sample_list == [5, 3, 8, 1, 2, 6]

# 3. .pop()
# _______________
popped_element = sample_list.pop()
assert popped_element == 6
assert sample_list == [5, 3, 8, 1, 2]

# 4. elem in list
# _______________
assert (3 in sample_list) is True
assert (7 in sample_list) is False

# 5. .count(elem)
# _______________
assert sample_list.count(1) == 1
assert [1, 2, 1, 1].count(1) == 3

# 6. sorted() vs .sort()
# _______________
# sorted() gives back a new sorted list and leaves the original alone
assert sorted(sample_list) == [1, 2, 3, 5, 8]
assert sample_list == [5, 3, 8, 1, 2]

# reverse=True sorts from largest to smallest
assert sorted(sample_list, reverse=True) == [8, 5, 3, 2, 1]

# key=len sorts by each item's length instead of the item itself
words = ['banana', 'kiwi', 'apple']
assert sorted(words) == ['apple', 'banana', 'kiwi']  # alphabetical
assert sorted(words, key=len) == ['kiwi', 'apple', 'banana']  # shortest first

# .sort() changes the list itself and returns None
result = sample_list.sort()
assert result is None
assert sample_list == [1, 2, 3, 5, 8]

# 7. .reverse()
# _______________
sample_list.reverse()
assert sample_list == [8, 5, 3, 2, 1]

# 8. min(), max(), sum()
# _______________
assert min(sample_list) == 1
assert max(sample_list) == 8
assert sum(sample_list) == 19

print('All checks passed.')
