"""
String methods in Python are case sensitive and do not change the original string.
We will discuss the following string methods and functions:

Functions: 
    1) len() - Returns the length of the string.

Methods: 
    1) .upper() - Converts all characters in the string to uppercase.
    2) .lower() - Converts all characters in the string to lowercase.
    3) .find('string_to_look_up') - Returns the index of the first occurrence of the specified substring.
    4) .replace('old_string', 'new_string') - Replaces occurrences of the old substring with the new substring.
    5) 'string-sequence' in string_variable - Returns a boolean indicating whether the specified substring is present in the string.
"""

# Example string
movie = 'Mission Impossible'

# Get the length of the string
print('Length of the string:', len(movie))
# Expected Output: Length of the string: 17

# Convert the string to uppercase
print('Uppercase:', movie.upper())
# Expected Output: Uppercase: MISSION IMPOSSIBLE

# Convert the string to lowercase
print('Lowercase:', movie.lower())
# Expected Output: Lowercase: mission impossible

# Find the index of the substring 'ssion'
print('Index of "ssion":', movie.find('ssion'))
# Expected Output: Index of "ssion": 2

print('Index of "z":', movie.find('z'))
# Expected Output: Index of "z": -1

# Replace 'Imp' with 'IMP' in the string
print('Replace "Imp" with "IMP":', movie.replace('Imp', 'IMP'))
# Expected Output: Replace "Imp" with "IMP": Mission IMPossible

# Check if 'ssion' is present in the string
print('Is "ssion" in the movie title?', 'ssion' in movie)
# Expected Output: Is "ssion" in the movie title? True

print('Is "zz" in the movie title?', 'zz' in movie)
# Expected Output: Is "zz" in the movie title? False


# # Character Validation
test_string = "abc123"

print("Character checking methods:")
# Expected Output: Character checking methods:

print(f"  isdigit('123'): {'123'.isdigit()}")
# Expected Output:   isdigit('123'): True

print(f"  isnumeric('123'): {'123'.isnumeric()}")
# Expected Output:   isnumeric('123'): True

print(f"  isalpha('abc'): {'abc'.isalpha()}")
# Expected Output:   isalpha('abc'): True

print(f"  isalnum('{test_string}'): {test_string.isalnum()}")
# Expected Output:   isalnum('abc123'): True