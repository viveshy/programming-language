"""
We will discuss the following list methods and functions:

Functions: 
    1) len() - Returns the length of the list.

Methods: 
    1) .append(elem) => Adds an element to the list
    2) .pop() => Removes the last element
    3) elem in list => Checks if an element is present in the list
    4) .count(elem) => Counts occurrences of an element
    5) .sort() => Sorts the list in ascending order
    6) .reverse() => Reverses the list
"""

# list_methods_demo.py

# Sample list for demonstration
sample_list = [5, 3, 8, 1, 2]

# Function: len()
print("Original list:", sample_list)
# Expected Output: Original list: [5, 3, 8, 1, 2]

print("Length of the list:", len(sample_list))
# Expected Output: Length of the list: 5

# Method: .append(elem)
print("\nDemonstrating .append()")
# Expected Output: Demonstrating .append()

sample_list.append(6)  
print("List after appending 6:", sample_list)
# Expected Output: List after appending 6: [5, 3, 8, 1, 2, 6]

# Method: .pop()
print("\nDemonstrating .pop()")
# Expected Output: Demonstrating .pop()

popped_element = sample_list.pop()  
print("Popped element:", popped_element)
# Expected Output: Popped element: 6

print("List after popping:", sample_list)
# Expected Output: List after popping: [5, 3, 8, 1, 2]

# Method: elem in list
print("\nDemonstrating 'elem in list'")
# Expected Output: Demonstrating 'elem in list'

element_to_check = 3
exists = element_to_check in sample_list
print(f"Is {element_to_check} in the list? {exists}")
# Expected Output: Is 3 in the list? True

# Method: .count(elem)
print("\nDemonstrating .count()")
# Expected Output: Demonstrating .count()

count_of_element = sample_list.count(1)  
print(f"Count of element 1 in the list: {count_of_element}")
# Expected Output: Count of element 1 in the list: 1

# Method: .sort()
print("\nDemonstrating .sort()")
# Expected Output: Demonstrating .sort()

sample_list.sort()  
print("List after sorting:", sample_list)
# Expected Output: List after sorting: [1, 2, 3, 5, 8]

# Method: .reverse()
print("\nDemonstrating .reverse()")
# Expected Output: Demonstrating .reverse()

sample_list.reverse()  
print("List after reversing:", sample_list)
# Expected Output: List after reversing: [8, 5, 3, 2, 1]