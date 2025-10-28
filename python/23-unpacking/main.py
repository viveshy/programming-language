# Tuple unpacking
coordinates = (1, 3, 8)

# Unpacking a tuple into individual variables
x, y, z = coordinates
print(f"Coordinates: x={x}, y={y}, z={z}")
# Expected Output: Coordinates: x=1, y=3, z=8

# Tuple unpacking can be used to swap values
a = 10
b = 20
print(f"Before swapping: a={a}, b={b}")
# Expected Output: Before swapping: a=10, b=20

a, b = b, a
print(f"After swapping: a={a}, b={b}")
# Expected Output: After swapping: a=20, b=10

# List unpacking
dimensions = [40, 50, 60]

# Unpacking a list into individual variables
length, breadth, height = dimensions
print(f"Dimensions: length={length}, breadth={breadth}, height={height}")
# Expected Output: Dimensions: length=40, breadth=50, height=60

# Demonstrating unpacking with excess values
more_dimensions = [40, 50, 60, 70]
length, breadth, height, _ = more_dimensions  # Using _ to ignore the last value
print(f"More Dimensions: length={length}, breadth={breadth}, height={height}")
# Expected Output: More Dimensions: length=40, breadth=50, height=60
