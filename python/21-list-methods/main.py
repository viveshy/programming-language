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
print("Length of the list:", len(sample_list))

# Method: .append(elem)
print("\nDemonstrating .append()")
sample_list.append(6)  
print("List after appending 6:", sample_list)

# Method: .pop()
print("\nDemonstrating .pop()")
popped_element = sample_list.pop()  
print("Popped element:", popped_element)
print("List after popping:", sample_list)

# Method: elem in list
print("\nDemonstrating 'elem in list'")
element_to_check = 3
exists = element_to_check in sample_list
print(f"Is {element_to_check} in the list? {exists}")

# Method: .count(elem)
print("\nDemonstrating .count()")
count_of_element = sample_list.count(1)  
print(f"Count of element 1 in the list: {count_of_element}")

# Method: .sort()
print("\nDemonstrating .sort()")
sample_list.sort()  
print("List after sorting:", sample_list)

# Method: .reverse()
print("\nDemonstrating .reverse()")
sample_list.reverse()  
print("List after reversing:", sample_list)