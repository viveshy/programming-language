"""
The following arithmetic operations are covered here:
1. Addition: +
2. Subtraction: -
3. Multiplication: *
4. Division: /, //, and % 
   - / => quotient with remainder 
   - // => only quotient 
   - % => remainder
5. Power: **
"""

# Define integer and float variables
int_num1 = 10
int_num2 = 3
float_num1 = 10.33
float_num2 = 3.5

"""
1. ADDITION:
_________________
"""
print('\nAddition Results:')
# int + int = int
print(f'int {int_num1} + int {int_num2} = {int_num1 + int_num2}')
# Expected Output: int 10 + int 3 = 13

# float + float = float
print(f'float {float_num1} + float {float_num2} = {float_num1 + float_num2}')
# Expected Output: float 10.33 + float 3.5 = 13.83

# int + float = float
print(f'int {int_num1} + float {float_num1} = {int_num1 + float_num1}')
# Expected Output: int 10 + float 10.33 = 20.33


"""
2. SUBTRACTION:
_________________
"""
print('\nSubtraction Results:')
# int - int = int
print(f'int {int_num1} - int {int_num2} = {int_num1 - int_num2}')

# float - float = float
print(f'float {float_num1} - float {float_num2} = {float_num1 - float_num2}')

# int - float = float
print(f'int {int_num1} - float {float_num1} = {int_num1 - float_num1}')


"""
3. MULTIPLICATION:
_________________
"""
print('\nMultiplication Results:')
# int * int = int
print(f'int {int_num1} * int {int_num2} = {int_num1 * int_num2}')

# float * float = float
print(f'float {float_num1} * float {float_num2} = {float_num1 * float_num2}')

# int * float = float
print(f'int {int_num1} * float {float_num1} = {int_num1 * float_num1}')


"""
4. DIVISION:
_________________
"""
print('\nDivision using /:')
# int / int = float
print(f'int {int_num1} / int {int_num2} = {int_num1 / int_num2}')

# float / float = float
print(f'float {float_num1} / float {float_num2} = {float_num1 / float_num2}')

# int / float = float
print(f'int {int_num1} / float {float_num1} = {int_num1 / float_num1}')

print('\nDivision using //:')
# int // int = int
print(f'int {int_num1} // int {int_num2} = {int_num1 // int_num2}')

# float // float = float
print(f'float {float_num1} // float {float_num2} = {float_num1 // float_num2}')

# int // float = float
print(f'int {int_num1} // float {float_num1} = {int_num1 // float_num1}')


print('\nDivision using %:')
# int % int = int
print(f'int {int_num1} % int {int_num2} = {int_num1 % int_num2}')

# float % float = float
print(f'float {float_num1} % float {float_num2} = {float_num1 % float_num2}')

# int % float = float
print(f'int {int_num1} % float {float_num1} = {int_num1 % float_num1}')


"""
5. POWER OF:
_________________
"""
print('\nPower Results:')
# int ** int = int
print(f'int {int_num1} ** int {int_num2} = {int_num1 ** int_num2}')

# float ** float = float
print(f'float {float_num1} ** float {float_num2} = {float_num1 ** float_num2}')

# int ** float = float
print(f'int {int_num1} ** float {float_num1} = {int_num1 ** float_num1}')