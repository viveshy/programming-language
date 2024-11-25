"""
The range() function in Python is used to generate a sequence of numbers.
It is commonly used in combination with for loops to iterate over a specific range of numbers.

## Syntax
1. range(stop)
2. range(start, stop)
3. range(start, stop, step)

## Examples
"""

# 1. Using range() with a single argument
print("Using range() with a single argument:")
for i in range(5):
    print(i)

print("\n")

# 2. Using range() with start and stop arguments
print("Using range() with start and stop arguments:")
for i in range(2, 6):
    print(i)

print("\n")

# 3. Using range() with start, stop, and step arguments
print("Using range() with start, stop, and step arguments:")
for i in range(1, 10, 2):
    print(i)

print("\n")

# 4. Using range() with negative values
print("Using range() with negative values:")
for i in range(5, 0, -1):
    print(i)

print("\n")

"""
## Important Points
- The range() function returns an immutable sequence of numbers.
- The start value is included in the sequence, while the stop value is not.
- If the step value is not provided, it defaults to 1.
- If the start value is not provided, it defaults to 0.
- The range() function cannot accept floating-point numbers as arguments.
- The range() function is often used in combination with for loops to iterate over a specific range of numbers.
"""
