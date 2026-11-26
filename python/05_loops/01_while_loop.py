"""
A while loop runs its block again and again, as long as its condition is True.

    while condition:
        block        # runs, then Python checks the condition again

    ┌──────────┬─────────────────────────────────────────────────────┐
    │ Keyword  │ What it does                                        │
    ├──────────┼─────────────────────────────────────────────────────┤
    │ break    │ leave the loop at once                              │
    │ continue │ skip the rest of the block and go to the next round │
    └──────────┴─────────────────────────────────────────────────────┘

Why it matters: use while when you don't know in advance how many rounds you
need. Binary search and two pointers are while loops.

We will cover:
1. The basic while loop
2. break: leave the loop early
3. continue: skip to the next round
4. while ... else
5. while lo < hi: two pointers and binary search
"""


# ┌────────────────────────────────────────────────────────────┐
# │ 1. THE BASIC WHILE LOOP                                    │
# └────────────────────────────────────────────────────────────┘
# Python checks the condition. If it is True, the block runs, then Python
# checks again. When the condition is False, the loop stops.
# seen collects the values, so an assert can check them. seen.append(x) adds x
# to the end of the list seen (lists come in 06_collections).

counter = 0
seen = []

while counter < 5:
    seen.append(counter)
    counter += 1  # without this, counter < 5 stays True forever

assert seen == [0, 1, 2, 3, 4]

# After the loop, counter is 5: the value that made counter < 5 False.

assert counter == 5


# ┌────────────────────────────────────────────────────────────┐
# │ 2. BREAK: LEAVE THE LOOP EARLY                             │
# └────────────────────────────────────────────────────────────┘
# break stops the loop at once, even if the condition is still True.
# Python goes on with the first line after the loop.

countdown = 5
seen = []

while countdown > 0:
    seen.append(countdown)
    countdown -= 1
    if countdown == 2:
        break

assert seen == [5, 4, 3]
assert countdown == 2  # still > 0, but break ended the loop

# while True: never stops by itself, so it needs a break. Use it when the stop
# test is easiest to write in the middle of the block.

power = 1

while True:
    power *= 2
    if power > 100:
        break

assert power == 128  # the first power of 2 above 100


# ┌────────────────────────────────────────────────────────────┐
# │ 3. CONTINUE: SKIP TO THE NEXT ROUND                        │
# └────────────────────────────────────────────────────────────┘
# continue skips the rest of the block. Python goes straight back to the
# condition and starts the next round. The loop does not stop.

n = 0
odds = []

while n < 9:
    n += 1
    if n % 2 == 0:
        continue  # even: the append below does not run
    odds.append(n)

assert odds == [1, 3, 5, 7, 9]


# ┌────────────────────────────────────────────────────────────┐
# │ 4. WHILE ... ELSE                                          │
# └────────────────────────────────────────────────────────────┘
# The else block runs when the loop ends because its condition became False.
# A break skips it.

attempts = 0
finished_normally = False

while attempts < 3:
    attempts += 1
else:
    finished_normally = True

assert finished_normally is True

attempts = 0
finished_normally = False

while attempts < 3:
    attempts += 1
    if attempts == 2:
        break
else:
    finished_normally = True

assert attempts == 2
assert finished_normally is False  # break skipped the else


# ┌────────────────────────────────────────────────────────────┐
# │ 5. WHILE LO < HI: TWO POINTERS AND BINARY SEARCH           │
# └────────────────────────────────────────────────────────────┘
# Two pointers: lo starts at the first index and hi at the last. Each round
# moves them towards each other, and the loop stops when they meet.
# Here they check a palindrome: a word that reads the same backwards.

word = 'racecar'
lo = 0
hi = len(word) - 1  # the last index
is_palindrome = True

while lo < hi:
    if word[lo] != word[hi]:
        is_palindrome = False
        break
    lo += 1
    hi -= 1

assert is_palindrome is True

# Binary search: each round halves the range lo..hi where the answer must be.
# Here: the smallest x with x * x >= 50. It must be in 0..50.

lo = 0
hi = 50

while lo < hi:
    mid = (lo + hi) // 2
    if mid * mid >= 50:
        hi = mid  # mid works: the answer is mid or smaller
    else:
        lo = mid + 1  # mid is too small: the answer is bigger

assert lo == 8  # 7 * 7 = 49 is too small, 8 * 8 = 64 works

# Halving is fast: even the range 0..10**18 takes only about 60 rounds.


print('All checks passed.')
