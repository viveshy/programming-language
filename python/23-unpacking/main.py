# Tuple unpacking
coordinates = (1, 3, 8)

# Unpacking a tuple into individual variables
x, y, z = coordinates
print(f"Coordinates: x={x}, y={y}, z={z}")

# Tuple unpacking can be used to swap values
a = 10
b = 20
print(f"Before swapping: a={a}, b={b}")
a, b = b, a
print(f"After swapping: a={a}, b={b}")

# List unpacking
dimensions = [40, 50, 60]

# Unpacking a list into individual variables
length, breadth, height = dimensions
print(f"Dimensions: length={length}, breadth={breadth}, height={height}")

# Demonstrating unpacking with excess values
more_dimensions = [40, 50, 60, 70]
length, breadth, height, _ = more_dimensions  # Using _ to ignore the last value
print(f"More Dimensions: length={length}, breadth={breadth}, height={height}")
