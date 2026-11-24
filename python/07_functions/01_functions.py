"""
A function is a named block of code that you can run (call) as often as you like.

    def name(parameters):
        ...
        return result

We will cover:
1. Defining and calling a function
2. return
3. Returning several values
4. Default and keyword arguments
5. The mutable default argument trap
6. lambda
7. Functions as values (key= in sorted)
8. Recursion
"""

# 1. DEFINING AND CALLING
# _________________________
def greet(name):
    return f'Hello, {name}!'


assert greet('Ada') == 'Hello, Ada!'

# 2. RETURN
# _________________________
def add(a, b):
    return a + b


assert add(2, 3) == 5


# A function without a return statement gives back None
def say_nothing():
    message = 'nobody sees this'


assert say_nothing() is None


# return ends the function straight away, even inside a loop
def first_negative(numbers):
    for n in numbers:
        if n < 0:
            return n
    return None


assert first_negative([3, -1, -5]) == -1
assert first_negative([1, 2]) is None

# 3. RETURNING SEVERAL VALUES
# _________________________
# `return a, b` really returns one tuple, which you can unpack
def divmod_pair(a, b):
    return a // b, a % b


assert divmod_pair(7, 2) == (3, 1)

q, r = divmod_pair(7, 2)
assert q == 3 and r == 1

assert divmod(7, 2) == (3, 1)  # Python has this one built in

# 4. DEFAULT AND KEYWORD ARGUMENTS
# _________________________
def power(base, exponent=2):  # exponent is 2 unless you pass something else
    return base ** exponent


assert power(3) == 9
assert power(3, 3) == 27
assert power(exponent=3, base=2) == 8  # named (keyword) arguments can come in any order

# 5. THE MUTABLE DEFAULT ARGUMENT TRAP
# _________________________
# The default [] is created ONCE, when `def` runs, and then shared by every call
def add_item(x, items=[]):
    items.append(x)
    return items


assert add_item('a') == ['a']
assert add_item('a') == ['a', 'a']  # the same list again!


# The fix: default to None and make a new list inside the function
def add_item_fixed(x, items=None):
    if items is None:
        items = []
    items.append(x)
    return items


assert add_item_fixed('a') == ['a']
assert add_item_fixed('a') == ['a']

# 6. LAMBDA
# _________________________
# A lambda is a small function written in one expression: lambda parameters: result
square = lambda x: x * x
assert square(4) == 16

# 7. FUNCTIONS AS VALUES
# _________________________
# A function can be stored in a variable or passed to another function
def shout(text):
    return text.upper()


say = shout
assert say('hi') == 'HI'
assert list(map(shout, ['a', 'b'])) == ['A', 'B']

# sorted() calls the key function on each item and sorts by what it returns
assert sorted(['ccc', 'a', 'bb'], key=len) == ['a', 'bb', 'ccc']
assert sorted([(1, 'b'), (2, 'a')], key=lambda pair: pair[1]) == [(2, 'a'), (1, 'b')]

# To sort by several things, return a tuple: by age, then by name
people = [('bo', 30), ('ana', 25), ('cy', 25)]
assert sorted(people, key=lambda person: (person[1], person[0])) == [('ana', 25), ('cy', 25), ('bo', 30)]

# 8. RECURSION
# _________________________
# A recursive function calls itself on a smaller problem until it reaches
# a case it can answer directly (the base case)
def factorial(n):
    if n <= 1:  # base case
        return 1
    return n * factorial(n - 1)


assert factorial(5) == 120  # 5 * 4 * 3 * 2 * 1

# Python stops at about 1000 nested calls and raises a RecursionError.
# (Raising that limit, or avoiding deep recursion, comes later with Python for CP.)
try:
    factorial(5000)
    finished = True
except RecursionError:
    finished = False

assert finished is False

print('All checks passed.')
