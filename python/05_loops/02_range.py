"""
range() gives a run of integers, one after another, for a loop to step through.

    ┌──────────────────────────┬────────────────────────────────────────────┐
    │ Call                     │ Gives                                      │
    ├──────────────────────────┼────────────────────────────────────────────┤
    │ range(stop)              │ 0, 1, 2, ..., stop - 1                     │
    │ range(start, stop)       │ start, start + 1, ..., stop - 1            │
    │ range(start, stop, step) │ start, start + step, start + 2 * step, ... │
    └──────────────────────────┴────────────────────────────────────────────┘

The stop is never included.

Why it matters: most contest loops run over range(n): the indexes 0 to n - 1
of a string or list with n items.

We will cover:
1. range(stop): counting from 0
2. range(start, stop)
3. range(start, stop, step)
4. Counting down with a negative step
5. Empty ranges
6. A range is not a list
7. range in a for loop
"""


# ┌────────────────────────────────────────────────────────────┐
# │ 1. RANGE(STOP): COUNTING FROM 0                            │
# └────────────────────────────────────────────────────────────┘
# range(5) gives 0, 1, 2, 3, 4: five numbers, starting at 0. The 5 is left out.
# list() turns a range into a list, so we can see and check the numbers
# (lists come in 06_collections).

assert list(range(5)) == [0, 1, 2, 3, 4]
assert list(range(1)) == [0]


# ┌────────────────────────────────────────────────────────────┐
# │ 2. RANGE(START, STOP)                                      │
# └────────────────────────────────────────────────────────────┘
# The start is included and the stop is not, so you get stop - start numbers.
# If you leave out the start, it is 0.

assert list(range(2, 6)) == [2, 3, 4, 5]  # 6 - 2 = 4 numbers
assert list(range(0, 5)) == list(range(5))


# ┌────────────────────────────────────────────────────────────┐
# │ 3. RANGE(START, STOP, STEP)                                │
# └────────────────────────────────────────────────────────────┘
# The step is the gap from one number to the next.
# If you leave it out, the step is 1. A step of 0 stops with a ValueError.

assert list(range(1, 10, 2)) == [1, 3, 5, 7, 9]
assert list(range(0, 10, 3)) == [0, 3, 6, 9]

# The stop is still left out, even when a step lands on it exactly.

assert list(range(0, 9, 3)) == [0, 3, 6]


# ┌────────────────────────────────────────────────────────────┐
# │ 4. COUNTING DOWN WITH A NEGATIVE STEP                      │
# └────────────────────────────────────────────────────────────┘
# A negative step counts down. The stop is still left out.

assert list(range(5, 0, -1)) == [5, 4, 3, 2, 1]  # no 0
assert list(range(10, 0, -3)) == [10, 7, 4, 1]


# ┌────────────────────────────────────────────────────────────┐
# │ 5. EMPTY RANGES                                            │
# └────────────────────────────────────────────────────────────┘
# A range can hold no numbers at all. When depends on the direction:
# - counting up (positive step): empty when start is not before stop
# - counting down (negative step): empty when start is not after stop

assert list(range(0)) == []  # start 0 is not before stop 0
assert list(range(5, 2)) == []  # counting up from 5 never reaches 2

assert list(range(0, 5, -1)) == []  # counting down from 0 never reaches 5
assert list(range(3, 3, -1)) == []

# A loop over an empty range runs 0 times. There is no error.


# ┌────────────────────────────────────────────────────────────┐
# │ 6. A RANGE IS NOT A LIST                                   │
# └────────────────────────────────────────────────────────────┘
# A range stores only start, stop and step. It makes each number when the loop
# asks for it, so even a huge range takes almost no memory.
# len() still knows how many numbers it has, without building a list.

assert len(range(1, 10, 2)) == 5
assert len(range(10 ** 9)) == 10 ** 9  # no list of a billion numbers is built


# ┌────────────────────────────────────────────────────────────┐
# │ 7. RANGE IN A FOR LOOP                                     │
# └────────────────────────────────────────────────────────────┘
# A for loop runs its block once for each number in the range, with i set to
# that number each time (for loops come in 03_for_loops).

total = 0
for i in range(1, 5):
    total += i

assert total == 1 + 2 + 3 + 4


print('All checks passed.')
