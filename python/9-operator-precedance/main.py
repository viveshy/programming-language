"""
A simplified hierarchy of common operators, from highest to lowest precedence:
1.Parentheses ()
2.Exponentiation **
3.Multiplication *, Division /, Floor Division //, Modulus %
4.Addition +, Subtraction -
5.Comparison Operators (>, <, >=, <=, ==, !=)
6.Logical Operators: AND and, OR or
7.Assignment =
"""


# Example of Arithmetic Operations
result = 10 + 2 * 3 - 5
print('Result of 10 + 2 * 3 - 5 =', result)
# Expected Output: Result of 10 + 2 * 3 - 5 = 11


# Example with Parentheses
result_with_parentheses = (10 + 2) * 3
print('Result of (10 + 2) * 3 =', result_with_parentheses)
# Expected Output: Result of (10 + 2) * 3 = 36

# Example with Multiple Operators
complex_result = 5 + 3 * 2 ** 2 - 8 / 4
print('Result of 5 + 3 * 2 ** 2 - 8 / 4 =', complex_result)
# Expected Output: Result of 5 + 3 * 2 ** 2 - 8 / 4 = 15.0