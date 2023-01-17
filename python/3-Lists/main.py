# What is list?
# In Python, list is array of a data type.

#1)____________Create list from strings
greeting = "Hello there dudes"
greeting_list = greeting.split(' ')

#2)_____________Create list of numbers
numbers = [1, 2, 3, 4]

#3)____________Accessing element of list
#Forward accessing
numbers[0]
numbers[2]

#Backward accessing
numbers[-3]

#4)__________Slicing list
#Syntax: list_name[inclusive:exclusive]
#Syntax: list_name[inclusive:-exclusive]  -- exclusive starts from 1
print(numbers[0:-1])

#5)___________Concatenate two list
odd = [1,3,5]
even = [2,4,6]
odd_even = odd + even
print(odd_even)

#6)____________Add elem to last position
odd.append(7)
print(odd)

#7)______________Remove last elem and return the removed elem
poped_number = odd.pop()
print(poped_number)
print(odd)

#8)__________Remove a particular element from the list (first occurrence)
odd.remove(3)
print(odd)

odd.append(89)
odd.append(89)

odd.remove(89)
print(odd)

#9)___________Delete an element based on index
print(odd)

del(odd[2])

print(odd)

#10)_____________List of list ; It's nothing but 2D list
# A list can comprise of list of heterogeneous data types
names = ['Hare', 'Krishna', 'Hare', 'Ram']
numbers = [108, 1008]

name_number = [names, numbers]
print(name_number)

# Accessing list of list ; follows same logic as that of 1D list
print(name_number[1][0])
name_number[1].append(74)

print(name_number)