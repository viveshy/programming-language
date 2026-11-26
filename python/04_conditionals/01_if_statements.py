"""
An if statement runs a block of code only when its condition is True.

    ┌─────────┬───────────────────────────────────────────────────────────────┐
    │ Keyword │ What it does                                                  │
    ├─────────┼───────────────────────────────────────────────────────────────┤
    │ if      │ runs its block when the condition is True                     │
    │ elif    │ "else if": tried only when every condition above it was False │
    │ else    │ runs when every condition above it was False                  │
    └─────────┴───────────────────────────────────────────────────────────────┘

Why it matters: every problem has cases (even or odd, found or not found).
An if picks the code that runs for each case.

We will cover:
1. if: run a block only when a condition is True
2. if-else: one of two blocks
3. if-elif-else: the first True condition wins
4. Nested if: an if inside an if
5. The one-line if-else
"""


# ┌────────────────────────────────────────────────────────────┐
# │ 1. IF: RUN A BLOCK ONLY WHEN A CONDITION IS TRUE           │
# └────────────────────────────────────────────────────────────┘
# A condition is a question with a True or False answer, like number > 0.
# (Comparisons like > and == come in 02_comparison_operators.py.)
# The line ends with a colon (:). The block is the indented lines under it.

number = 10
sign = 'unknown'  # each example stores which branch ran, so an assert can check

if number > 0:
    sign = 'positive'

assert sign == 'positive'

if number < 0:
    sign = 'negative'  # skipped: 10 < 0 is False

assert sign == 'positive'


# ┌────────────────────────────────────────────────────────────┐
# │ 2. IF-ELSE: ONE OF TWO BLOCKS                              │
# └────────────────────────────────────────────────────────────┘
# else has no condition. Its block runs when the if's condition is False.
# So exactly one of the two blocks runs.

number = 7

if number % 2 == 0:  # remainder 0 means even
    parity = 'even'
else:
    parity = 'odd'  # 7 % 2 is 1, so the else block runs

assert parity == 'odd'


# ┌────────────────────────────────────────────────────────────┐
# │ 3. IF-ELIF-ELSE: THE FIRST TRUE CONDITION WINS             │
# └────────────────────────────────────────────────────────────┘
# Python tries the conditions from the top and runs only the FIRST True one.
# The rest are skipped, even if they are True too.
# else is optional. It runs when no condition was True.

score = 85

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
else:
    grade = 'F'

assert grade == 'B'  # 85 >= 70 is True too, but the 'B' branch came first


# ┌────────────────────────────────────────────────────────────┐
# │ 4. NESTED IF: AN IF INSIDE AN IF                           │
# └────────────────────────────────────────────────────────────┘
# An if can sit inside another if's block. The inner if is tried only when the
# outer condition is True.
# Each else belongs to the if that it lines up with.

age = 20
has_permission = True

if age >= 18:
    if has_permission:
        access = 'adult with permission: may enter'
    else:
        access = 'adult without permission: may not enter'
else:
    access = 'not an adult'  # lines up with the outer if: runs when age < 18

assert access == 'adult with permission: may enter'

# An if inside an if, with no else, can be one if:
# if age >= 18 and has_permission:   (and comes in 04_logical_operators.py)


# ┌────────────────────────────────────────────────────────────┐
# │ 5. THE ONE-LINE IF-ELSE                                    │
# └────────────────────────────────────────────────────────────┘
# a if condition else b gives a when the condition is True, and b otherwise.
# It picks a value. It does not run blocks.

parity = 'even' if number % 2 == 0 else 'odd'
assert parity == 'odd'  # number is 7

x = -4
size = x if x >= 0 else -x  # abs() does this (04_math_functions.py)
assert size == 4


print('All checks passed.')
