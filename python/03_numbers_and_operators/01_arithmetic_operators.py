"""
Arithmetic operators do maths on numbers.

    ┌──────────┬────────────────────┬──────────────┬────────────────────────┐
    │ Operator │ Name               │ Example      │ Note                   │
    ├──────────┼────────────────────┼──────────────┼────────────────────────┤
    │ +        │ add                │ 7 + 2 == 9   │                        │
    │ -        │ subtract           │ 7 - 2 == 5   │                        │
    │ *        │ multiply           │ 7 * 2 == 14  │                        │
    │ /        │ divide             │ 7 / 2 == 3.5 │ always a float         │
    │ //       │ floor division     │ 7 // 2 == 3  │ quotient, rounded down │
    │ %        │ remainder (modulo) │ 7 % 2 == 1   │ what is left over      │
    │ **       │ power              │ 7 ** 2 == 49 │                        │
    └──────────┴────────────────────┴──────────────┴────────────────────────┘

Why it matters: contest problems are mostly maths on integers, and // and %
are in almost every solution.

We will cover:
1. + - *: integers and floats
2. /: division always gives a float
3. //: floor division
4. %: the remainder
5. // and % with negative numbers
6. **: power
7. Floats are not exact: 0.1 + 0.2 != 0.3
"""


# ┌────────────────────────────────────────────────────────────┐
# │ 1. + - *: INTEGERS AND FLOATS                              │
# └────────────────────────────────────────────────────────────┘
# With two integers, + - * give an integer.

assert 10 + 3 == 13
assert 10 - 3 == 7
assert 10 * 3 == 30

# With a float on either side, the answer is a float.

assert 10 + 0.5 == 10.5
assert type(10 + 0.5) is float
assert 2.5 * 4 == 10.0


# ┌────────────────────────────────────────────────────────────┐
# │ 2. /: DIVISION ALWAYS GIVES A FLOAT                        │
# └────────────────────────────────────────────────────────────┘
# / gives the full answer, fraction included. It is always a float, even when
# the division is exact.

assert 7 / 2 == 3.5
assert 10 / 2 == 5.0
assert type(10 / 2) is float

# A float with no fraction part, like 5.0, is stored exactly, so == is safe.
# A fraction that never ends, like 3.333..., is cut short: use round().

assert round(10 / 3, 4) == 3.3333


# ┌────────────────────────────────────────────────────────────┐
# │ 3. //: FLOOR DIVISION                                      │
# └────────────────────────────────────────────────────────────┘
# a // b divides and rounds DOWN to an integer. This is the quotient: how many
# times b fits into a.

assert 7 // 2 == 3  # 3.5 rounded down
assert 10 // 3 == 3

# Two integers give an integer. With a float on either side, // still rounds
# down, but the answer is a float.

assert type(10 // 3) is int
assert 10.33 // 3.5 == 2.0
assert 10 // 10.33 == 0.0


# ┌────────────────────────────────────────────────────────────┐
# │ 4. %: THE REMAINDER                                        │
# └────────────────────────────────────────────────────────────┘
# a % b is what is left over after a // b. Say it "a mod b" (short for modulo).

assert 7 % 2 == 1  # 7 == 3 * 2 + 1
assert 6 % 3 == 0  # nothing left: 3 divides 6 exactly
assert 3 % 5 == 3  # 5 fits 0 times, so all of 3 is left over

# // and % always fit together: a == (a // b) * b + a % b.

a = 17
b = 5
assert (a // b) * b + a % b == a  # 3 * 5 + 2 == 17

# % works on floats too, but contests use it on integers.

assert round(10.33 % 3.5, 2) == 3.33


# ┌────────────────────────────────────────────────────────────┐
# │ 5. // AND % WITH NEGATIVE NUMBERS                          │
# └────────────────────────────────────────────────────────────┘
# // always rounds DOWN, towards minus infinity. For a negative answer, down
# means away from zero: -3.5 becomes -4, not -3.
# (A minus sign in front goes first: -7 // 2 is (-7) // 2. More in
# 03_operator_precedence.py.)

assert -7 // 2 == -4
assert 7 // -2 == -4

# % then keeps a == (a // b) * b + a % b true, so the remainder takes the sign
# of the right-hand number b.

assert -7 % 2 == 1  # (-4) * 2 + 1 == -7
assert 7 % -2 == -1  # (-4) * (-2) - 1 == 7


# ┌────────────────────────────────────────────────────────────┐
# │ 6. **: POWER                                               │
# └────────────────────────────────────────────────────────────┘
# a ** b multiplies b copies of a: 2 ** 3 == 2 * 2 * 2.

assert 2 ** 3 == 8
assert 10 ** 3 == 1000

# A float on either side gives a float. ** 0.5 is the square root.

assert 2.5 ** 2 == 6.25
assert 9 ** 0.5 == 3.0

# Integers have no limit in Python, so a big power keeps every digit.

assert 2 ** 100 == 1267650600228229401496703205376


# ┌────────────────────────────────────────────────────────────┐
# │ 7. FLOATS ARE NOT EXACT: 0.1 + 0.2 != 0.3                  │
# └────────────────────────────────────────────────────────────┘
# A float is stored in binary. In binary, 0.1 is a fraction that never ends, the
# way 1/3 = 0.333... never ends in decimal. A float keeps only 53 binary digits
# (01_variables_and_input/03_type_conversion.py, section 4), so it stores the
# nearest value it can, which is a tiny bit off.

assert 0.1 + 0.2 != 0.3
assert 0.1 + 0.2 == 0.30000000000000004

# Round before you compare.

assert round(0.1 + 0.2, 2) == 0.3


print('All checks passed.')
