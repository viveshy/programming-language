number = [2,3,4,5,6,7]

# Find first occurrence of multiple of 5 using while loop
index = 0
while index < len(number):
    if number[index] % 5 == 0:
        print(f'First occurrence of multiple of 5 in list is {number[index]}')
        break
    index += 1

# Find odd numbers using while
mixed_numbers = [1,2,3,4,7,8]
ind = 0
while ind < len(mixed_numbers):
    if mixed_numbers[ind] % 2 == 0:
        print(f'Even number is {mixed_numbers[ind]}')
    
    ind +=1