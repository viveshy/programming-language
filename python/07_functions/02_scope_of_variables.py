"""
In this section, we will learn about the scope of variables in Python.
We will cover the following topics:
1. Global Variables
2. Local Variables
3. Variable Shadowing
4. Modifying Global Variables
"""

# 1. Global Variables
# ________________________
global_variable = "I am a global variable"

def access_global_variable():
    print(f'Accessing global variable: {global_variable}')
    # Expected Output: Accessing global variable: I am a global variable

# 2. Local Variables
# ________________________
def local_variable_example():
    local_variable = "I am a local variable"
    print(f'Inside function: {local_variable}')
    # Expected Output: Inside function: I am a local variable

# 3. Variable Shadowing
# ________________________
def variable_shadowing_example():
    """
    This local variable has the same name as the global variable.
    """
    global_variable = "I am a local variable with the same name"
    print(f'Inside function (shadowed): {global_variable}')  # Refers to the local variable
    # Expected Output: Inside function (shadowed): I am a local variable with the same name
    
    """
    Using the globals() function to access the global variable.
    The global keyword is not needed when accessing global variables,
    it is only required when assigning values to global variables.
    """
    print(f'Accessing global variable inside function: {globals()["global_variable"]}')
    # Expected Output: Accessing global variable inside function: I have been modified

# Outside the function, we can access the global variable
print('Global Variable:')
# Expected Output: Global Variable:

access_global_variable()

# Attempting to access the local variable outside its function will raise an error
print('\nLocal Variable:')
# Expected Output: Local Variable:

try:
    print(local_variable)  # This will raise a NameError
except NameError:
    print("Error: local_variable is not defined outside its function.")
    # Expected Output: Error: local_variable is not defined outside its function.

# Call the function that defines a local variable
local_variable_example()

# 4. Modifying Global Variables
# _______________________________
def modify_global_variable():
    """
    Declare the variable as global using the global keyword
    when modifying a global variable inside a function.
    """
    global global_variable
    global_variable = "I have been modified"
    print(f'Inside function (modified): {global_variable}')
    # Expected Output: Inside function (modified): I have been modified

print('\nBefore modifying global variable:')
# Expected Output: Before modifying global variable:

print(global_variable)
# Expected Output: I am a global variable

modify_global_variable()

print('\nAfter modifying global variable:')
# Expected Output: After modifying global variable:

print(global_variable)
# Expected Output: I have been modified

# 5. Variable Shadowing Example
# _______________________________
print('\nVariable Shadowing Example:')
# Expected Output: Variable Shadowing Example:

variable_shadowing_example()
print(f'Global Variable after shadowing_example: {global_variable}')  # This will still access the original global variable
# Expected Output: Global Variable after shadowing_example: I have been modified