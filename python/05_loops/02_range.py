"""
The range() function in Python is used to generate a sequence of numbers.
It is commonly used in combination with for loops to iterate over a specific range of numbers.

## Syntax
1. range(stop)
2. range(start, stop)
3. range(start, stop, step)

list(range(...)) turns the sequence into a list, which makes it easy to check.
"""

# 1. Using range() with a single argument: 0 up to, but not including, stop
assert list(range(5)) == [0, 1, 2, 3, 4]

# 2. Using range() with start and stop arguments
assert list(range(2, 6)) == [2, 3, 4, 5]

# 3. Using range() with start, stop, and step arguments
assert list(range(1, 10, 2)) == [1, 3, 5, 7, 9]

# 4. Using range() with a negative step to count down
assert list(range(5, 0, -1)) == [5, 4, 3, 2, 1]

# 5. Empty ranges: start is not before stop, so there is nothing to count
assert list(range(0)) == []
assert list(range(5, 2)) == []  # counting up from 5 never reaches 2

# 6. Using range() in a for loop
total = 0
for i in range(1, 5):
    total += i

assert total == 1 + 2 + 3 + 4

# A range knows its length without building the whole list
assert len(range(1, 10, 2)) == 5

"""
## Important Points
- The range() function returns an immutable sequence of numbers.
- The start value is included in the sequence, while the stop value is not.
- If the step value is not provided, it defaults to 1.
- If the start value is not provided, it defaults to 0.
- The range() function cannot accept floating-point numbers as arguments
  (range(0.5) raises a TypeError).
- The range() function is often used in combination with for loops to iterate over a specific range of numbers.
"""

print('All checks passed.')
