"""
In this section, we will learn about the following types of while loops:
1. Basic while loop
2. While loop with break statement
3. While loop with else clause

The syntax for a while loop is:
    while condition:
        # body of the while loop

Ensure the while loop has a termination condition to prevent an infinite loop. Without a termination condition, the loop will continue executing indefinitely, leading to an unresponsive program.

Each loop below collects the values it visits in a list, so an assert can check them.
"""

# 1. Basic while loop
# ______________________
counter = 0
seen = []  # an empty list; seen.append(x) adds x to its end (lists are covered in 06_collections)

while counter < 5:
    print('counter is', counter)
    seen.append(counter)
    counter += 1  # Increment the counter, or the loop never ends

assert seen == [0, 1, 2, 3, 4]
assert counter == 5  # the condition counter < 5 became False, so the loop stopped

# 2. While loop with break statement
# ___________________________________
countdown = 5
seen = []

while countdown > 0:
    seen.append(countdown)
    countdown -= 1
    if countdown == 2:
        break  # Exit the loop immediately when countdown reaches 2

assert seen == [5, 4, 3]
assert countdown == 2

# 3. While loop with else clause
# ________________________________
# The else block runs only if the loop ended normally, without a break.
attempts = 0
finished_normally = False

while attempts < 3:
    attempts += 1
else:
    finished_normally = True

assert attempts == 3
assert finished_normally is True

# With a break, the else block is skipped
attempts = 0
finished_normally = False

while attempts < 3:
    attempts += 1
    if attempts == 2:
        break
else:
    finished_normally = True

assert attempts == 2
assert finished_normally is False

print('All checks passed.')
