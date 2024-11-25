"""
Lists in Python can be created using square brackets [] and can contain items of different data types.

CREATING A LIST:
To create a list, simply write a set of items within square brackets, separated by commas. For example:
- A list of integers: `numbers = [1, 2, 3, 4]`
- A heterogeneous list: `mixed = [1, 'apple', 3.14, True]`

ACCESSING LIST ELEMENTS:
Each item in a list has an assigned index value, starting from 0. You can access items using their index:
- Use positive indexing: `list_name[index]`
- Use negative indexing: `list_name[-index]` (counts from the end)
"""

# Creating a list of integers
numbers = [1, 2, 3, 4]
print("\nList of numbers:", numbers)

# Creating a heterogeneous list
mixed = [1, 'apple', 3.14, True]
print("\nHeterogeneous list:", mixed)

# Accessing elements using positive indexing
print('\nFirst element (index 0):', numbers[0])  # Output: 1
print('Second element (index 1):', numbers[1])  # Output: 2

# Accessing elements using negative indexing
print('\nLast element (index -1):', numbers[-1])  # Output: 4
print('Second last element (index -2):', numbers[-2])  # Output: 3

# Slicing the list
print('\nSlice from index 1 to 3:', numbers[1:3])  # Output: [2, 3]
print('Slice from the beginning to index 2:', numbers[:2])  # Output: [1, 2]
print('Slice from index 2 to the end:', numbers[2:])  # Output: [3, 4]
print('Complete list:', numbers[:])  # Output: [1, 2, 3, 4]