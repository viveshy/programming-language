"""
In this section, we will learn about the scope of variables in Python:
where a variable can be seen and changed.
We will cover the following topics:
1. Global Variables
2. Local Variables
3. Variable Shadowing
4. Modifying Global Variables
5. The UnboundLocalError trap

Each function returns what it saw, so an assert can check it.
"""

# 1. Global Variables
# ________________________
# A variable created outside every function is global: any function can read it
global_variable = 'I am a global variable'


def access_global_variable():
    return global_variable  # reading a global needs no special keyword


assert access_global_variable() == 'I am a global variable'

# 2. Local Variables
# ________________________
# A variable created inside a function only exists while that function runs
def local_variable_example():
    local_variable = 'I am a local variable'
    return local_variable


assert local_variable_example() == 'I am a local variable'

try:
    local_variable  # not defined out here
    visible_outside = True
except NameError:
    visible_outside = False

assert visible_outside is False

# 3. Variable Shadowing
# ________________________
# Assigning inside a function creates a NEW local variable, even if a global
# has the same name. The global is untouched.
def variable_shadowing_example():
    global_variable = 'I am a local variable with the same name'
    # globals() still lets us read the real global
    return global_variable, globals()['global_variable']


inside, real_global = variable_shadowing_example()
assert inside == 'I am a local variable with the same name'
assert real_global == 'I am a global variable'
assert global_variable == 'I am a global variable'  # unchanged

# 4. Modifying Global Variables
# _______________________________
# To assign to a global from inside a function, declare it with `global`
def modify_global_variable():
    global global_variable
    global_variable = 'I have been modified'


modify_global_variable()
assert global_variable == 'I have been modified'

# 5. The UnboundLocalError trap
# _______________________________
# Because the function assigns to counter, Python treats counter as local in
# the WHOLE function, so `counter + 1` reads a local that has no value yet.
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

print('All checks passed.')
