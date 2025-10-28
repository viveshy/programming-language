"""
In this section, we will learn about the following types of while loops:
1. Basic while loop
2. While loop with break statement
3. While loop with else clause

The syntax for a while loop is:
    while condition:
        # body of the while loop
        
Ensure the while loop has a termination condition to prevent an infinite loop. Without a termination condition, the loop will continue executing indefinitely, leading to an unresponsive program.
"""

# 1. Basic while loop
# ______________________
# Initialize a counter
counter = 0

print('Counting from 0 to 4:')
# Expected Output: Counting from 0 to 4:
while counter < 5:
    print(counter)
    # Expected Output: 0, 1, 2, 3, 4 (each on new line)
    counter += 1  # Increment the counter


# 2. While loop with break statement
# ___________________________________
print('\nCounting until a break condition:')
# Expected Output: Counting until a break condition:
countdown = 5

while countdown > 0:
    print(countdown)
    # Expected Output: 5, 4, 3 (each on new line)
    countdown -= 1
    if countdown == 2:
        print('Countdown stopped at 2.')
        # Expected Output: Countdown stopped at 2.
        break  # Exit the loop when countdown reaches 2

# 3. While loop with else clause
# ________________________________
print('\nUsing a while loop with an else clause:')
# Expected Output: Using a while loop with an else clause:
attempts = 0

while attempts < 3:
    print(f'Attempt number: {attempts + 1}')
    # Expected Output: Attempt number: 1, Attempt number: 2, Attempt number: 3
    attempts += 1
else:
    print('All attempts completed successfully.')
    # Expected Output: All attempts completed successfully.