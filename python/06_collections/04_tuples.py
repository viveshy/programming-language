"""
Tuples are similar to lists in Python. However, unlike lists, 
tuples are immutable, meaning we cannot modify them after creation.
"""

# LIST VS TUPLE
numbers_list = [1, 2, 3, 4, 5]  # A mutable list
numbers_tuple = (1, 2, 3, 4, 5)  # An immutable tuple

# Demonstrating tuple methods
# Two primarily used methods on tuples are: count and index

# count(x): Returns the number of occurrences of x in the tuple
count_of_3 = numbers_tuple.count(3)
print(f"The number 3 appears {count_of_3} times in the tuple.")
# Expected Output: The number 3 appears 1 times in the tuple.

# index(x): Returns the index of the first occurrence of x in the tuple
index_of_4 = numbers_tuple.index(4)
print(f"The index of the number 4 in the tuple is {index_of_4}.")
# Expected Output: The index of the number 4 in the tuple is 3.

# Accessing elements in a tuple is similar to accessing elements in a list
# Accessing the first and last elements
first_element = numbers_tuple[0]
last_element = numbers_tuple[-1]
print(f"First element: {first_element}, Last element: {last_element}")
# Expected Output: First element: 1, Last element: 5

# Slicing a tuple
slice_of_tuple = numbers_tuple[1:4]  # Slicing from index 1 to 3
print(f"Sliced tuple: {slice_of_tuple}")
# Expected Output: Sliced tuple: (2, 3, 4)

# Demonstrating that tuples are immutable
try:
    numbers_tuple[0] = 10  # Attempting to modify the first element
except TypeError as e:
    print(f"Error: {e}. Tuples cannot be modified.")
    # Expected Output: Error: 'tuple' object does not support item assignment. Tuples cannot be modified.

