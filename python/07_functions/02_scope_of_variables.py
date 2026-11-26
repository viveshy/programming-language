"""
Scope is where a variable can be seen and changed.

    ┌─────────────────┬───────────────────────────────────────────────────────┐
    │ Kind            │ Meaning                                               │
    ├─────────────────┼───────────────────────────────────────────────────────┤
    │ global variable │ made outside every function: any function can read it │
    │ local variable  │ made inside a function: exists only during that call  │
    └─────────────────┴───────────────────────────────────────────────────────┘

Why it matters: a recursive helper, like a DFS (depth-first search), often
has to update a counter or a best answer that lives outside it. That needs
global or nonlocal.

We will cover:
1. Global variables
2. Local variables
3. Shadowing: the same name inside a function
4. global: assigning to a global variable
5. nonlocal: assigning to the outer function's variable
"""


# ┌────────────────────────────────────────────────────────────┐
# │ 1. GLOBAL VARIABLES                                        │
# └────────────────────────────────────────────────────────────┘
# A variable made outside every function is global. Any function can read it,
# with no special keyword.

global_variable = 'I am a global variable'

def access_global_variable():
    return global_variable

assert access_global_variable() == 'I am a global variable'


# ┌────────────────────────────────────────────────────────────┐
# │ 2. LOCAL VARIABLES                                         │
# └────────────────────────────────────────────────────────────┘
# A variable made inside a function is local. It exists only while that call
# runs. Outside the function, the name is unknown.

def local_variable_example():
    local_variable = 'I am a local variable'
    return local_variable

assert local_variable_example() == 'I am a local variable'

# Using the name outside raises a NameError. try runs a block; if that error
# happens, the except block runs instead of the program stopping.

try:
    local_variable
    visible_outside = True
except NameError:
    visible_outside = False

assert visible_outside is False


# ┌────────────────────────────────────────────────────────────┐
# │ 3. SHADOWING: THE SAME NAME INSIDE A FUNCTION              │
# └────────────────────────────────────────────────────────────┘
# Assigning to a name inside a function makes a NEW local variable, even if a
# global has the same name. The local hides (shadows) the global, and the
# global is untouched.

def variable_shadowing_example():
    global_variable = 'I am a local variable with the same name'
    # globals() is a dict of all global names, so it still reaches the real one
    return global_variable, globals()['global_variable']

inside, real_global = variable_shadowing_example()
assert inside == 'I am a local variable with the same name'
assert real_global == 'I am a global variable'
assert global_variable == 'I am a global variable'  # unchanged

# If a function assigns to a name ANYWHERE, that name is local in the
# WHOLE function. So counter = counter + 1 reads a local that has no value
# yet, and stops with an UnboundLocalError.

counter = 0

def broken_increment():
    counter = counter + 1

try:
    broken_increment()
    worked = True
except UnboundLocalError:
    worked = False

assert worked is False
assert counter == 0


# ┌────────────────────────────────────────────────────────────┐
# │ 4. GLOBAL: ASSIGNING TO A GLOBAL VARIABLE                  │
# └────────────────────────────────────────────────────────────┘
# To assign to a global from inside a function, declare it first with
# global name. Then name = ... changes the global, not a new local.

def modify_global_variable():
    global global_variable
    global_variable = 'I have been modified'

modify_global_variable()
assert global_variable == 'I have been modified'

# This fixes the counter from section 3.

def increment():
    global counter
    counter += 1

increment()
increment()
assert counter == 2

# Changing a list in place, e.g. with append, does not assign to the name,
# so it needs no global.

found = []

def remember(x):
    found.append(x)

remember(5)
assert found == [5]


# ┌────────────────────────────────────────────────────────────┐
# │ 5. NONLOCAL: ASSIGNING TO THE OUTER FUNCTION'S VARIABLE    │
# └────────────────────────────────────────────────────────────┘
# A function can be defined inside another function. The inner one can read
# the outer one's variables. To assign to one, declare it with nonlocal name.

def make_count():
    count = 0

    def add_one():
        nonlocal count  # count belongs to make_count
        count += 1

    add_one()
    add_one()
    return count

assert make_count() == 2


print('All checks passed.')
