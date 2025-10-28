"""
Augmented assignment operators are a shorthand way to perform a binary operation and assign the result back to one of the operands.

Examples of augmented assignment operators in Python are:
    - Addition (+=): x += y is equivalent to x = x + y
    - Subtraction (-=): x -= y is equivalent to x = x - y
    - Multiplication (*=): x *= y is equivalent to x = x * y
    - Division (/=): x /= y is equivalent to x = x / y
    - Modulus (%=): x %= y is equivalent to x = x % y

"""

# Examples of augmented assignment operators in action
x = 10
print('Initial value of x:', x)
# Expected Output: Initial value of x: 10

# Addition (+=)
x += 5  # equivalent to x = x + 5
print('After x += 5:', x)
# Expected Output: After x += 5: 15

# Subtraction (-=)
x -= 3  # equivalent to x = x - 3
print('After x -= 3:', x)
# Expected Output: After x -= 3: 12

# Multiplication (*=)
x *= 2  # equivalent to x = x * 2
print('After x *= 2:', x)
# Expected Output: After x *= 2: 24

# Division (/=)
x /= 4  # equivalent to x = x / 4
print('After x /= 4:', x)
# Expected Output: After x /= 4: 6.0

# Modulus (%=)
y = 17
print('\nInitial value of y:', y)
# Expected Output: Initial value of y: 17

y %= 5  # equivalent to y = y % 5
print('After y %= 5:', y)
# Expected Output: After y %= 5: 2