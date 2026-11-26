"""
A function is a named block of code. You define it once with def, then run it
(call it) as often as you like.

    def name(parameters):    # parameters: names for the values passed in
        block
        return result        # the value the call gives back

Why it matters: on LeetCode, your answer is a function. Recursion (a function
calling itself) and sorted(key=...) show up in a great many problems.

We will cover:
1. Defining and calling a function
2. return
3. Returning several values
4. Default and keyword arguments
5. Mutable defaults: one list for every call
6. lambda: a function in one line
7. Functions as values: key= in sorted
8. Recursion
"""


# ┌────────────────────────────────────────────────────────────┐
# │ 1. DEFINING AND CALLING A FUNCTION                         │
# └────────────────────────────────────────────────────────────┘
# def only defines the function: nothing in its block runs yet.
# greet('Ada') calls it: the block runs with name set to 'Ada'.

def greet(name):
    return f'Hello, {name}!'

assert greet('Ada') == 'Hello, Ada!'
assert greet('Bo') == 'Hello, Bo!'


# ┌────────────────────────────────────────────────────────────┐
# │ 2. RETURN                                                  │
# └────────────────────────────────────────────────────────────┘
# return hands a value back to the caller. The call then stands for that value.

def add(a, b):
    return a + b

assert add(2, 3) == 5
assert add(add(1, 2), 3) == 6  # a call can go wherever a value can

# return ends the function at once, even in the middle of a loop.

def first_negative(numbers):
    for n in numbers:
        if n < 0:
            return n
    return None  # None means "no value" (04_conditionals)

assert first_negative([3, -1, -5]) == -1
assert first_negative([1, 2]) is None


# ┌────────────────────────────────────────────────────────────┐
# │ 3. RETURNING SEVERAL VALUES                                │
# └────────────────────────────────────────────────────────────┘
# return a, b gives back ONE tuple that holds both values. You can unpack it
# into two names (tuples and unpacking: 06_collections).

def divmod_pair(a, b):
    return a // b, a % b

assert divmod_pair(7, 2) == (3, 1)

q, r = divmod_pair(7, 2)
assert q == 3 and r == 1

# Python has this one built in: divmod(a, b).

assert divmod(7, 2) == (3, 1)


# ┌────────────────────────────────────────────────────────────┐
# │ 4. DEFAULT AND KEYWORD ARGUMENTS                           │
# └────────────────────────────────────────────────────────────┘
# A parameter written with = has a default value. The default is used when the
# call leaves that argument out.

def power(base, exponent=2):
    return base ** exponent

assert power(3) == 9  # exponent is 2
assert power(3, 3) == 27

# A keyword argument names its parameter, so the order doesn't matter.

assert power(exponent=3, base=2) == 8


# ┌────────────────────────────────────────────────────────────┐
# │ 5. MUTABLE DEFAULTS: ONE LIST FOR EVERY CALL               │
# └────────────────────────────────────────────────────────────┘
# A default value is made ONCE, when def runs. Every call that leaves the
# argument out gets that same object.
# A list, set or dict is mutable: it can be changed in place, e.g. by append.

# So a list default keeps what earlier calls put into it.

def add_item(x, items=[]):
    items.append(x)
    return items

assert add_item('a') == ['a']
assert add_item('b') == ['a', 'b']  # the 'a' from the first call is still there

# The fix: default to None, and make a new list inside the function.

def add_item_fixed(x, items=None):
    if items is None:
        items = []
    items.append(x)
    return items

assert add_item_fixed('a') == ['a']
assert add_item_fixed('b') == ['b']


# ┌────────────────────────────────────────────────────────────┐
# │ 6. LAMBDA: A FUNCTION IN ONE LINE                          │
# └────────────────────────────────────────────────────────────┘
# lambda parameters: expression   makes a small function without def.
# It gives back the value of the expression, with no return keyword.

square = lambda x: x * x
assert square(4) == 16

# Style: PEP 8, Python's style guide, says to use def when you give a function
# a name. A lambda is meant to be passed straight into another function.


# ┌────────────────────────────────────────────────────────────┐
# │ 7. FUNCTIONS AS VALUES: KEY= IN SORTED                     │
# └────────────────────────────────────────────────────────────┘
# A function is a value too: you can store it in a variable or pass it to
# another function. Without ( ) you refer to the function; with ( ) you call it.

def shout(text):
    return text.upper()

say = shout  # no ( ): say is now another name for shout
assert say('hi') == 'HI'

# map(f, items) calls f on every item. list() collects the results.

assert list(map(shout, ['a', 'b'])) == ['A', 'B']

# sorted(items, key=f) calls f on each item and sorts by what f returns.

assert sorted(['ccc', 'a', 'bb'], key=len) == ['a', 'bb', 'ccc']

pairs = [(1, 'b'), (2, 'a')]
assert sorted(pairs, key=lambda pair: pair[1]) == [(2, 'a'), (1, 'b')]

# To sort by several things, return a tuple: by age, then by name.

people = [('bo', 30), ('ana', 25), ('cy', 25)]
by_age = sorted(people, key=lambda person: (person[1], person[0]))
assert by_age == [('ana', 25), ('cy', 25), ('bo', 30)]

# min() and max() take key= too.

assert max(['ccc', 'a', 'bb'], key=len) == 'ccc'


# ┌────────────────────────────────────────────────────────────┐
# │ 8. RECURSION                                               │
# └────────────────────────────────────────────────────────────┘
# A recursive function calls itself on a smaller problem, until it reaches a
# case it can answer directly: the base case.

def factorial(n):
    if n <= 1:  # base case
        return 1
    return n * factorial(n - 1)

assert factorial(5) == 120  # 5 * 4 * 3 * 2 * 1

# Fibonacci: each number is the sum of the two before it: 0, 1, 1, 2, 3, 5, 8.

def fib(n):
    if n < 2:  # base cases: fib(0) = 0 and fib(1) = 1
        return n
    return fib(n - 1) + fib(n - 2)

assert fib(10) == 55


print('All checks passed.')
