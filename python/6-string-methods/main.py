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

# Convert the string to uppercase
print('Uppercase:', movie.upper())

# Convert the string to lowercase
print('Lowercase:', movie.lower())

# Find the index of the substring 'ssion'
print('Index of "ssion":', movie.find('ssion'))
print('Index of "z":', movie.find('z'))

# Replace 'Imp' with 'IMP' in the string
print('Replace "Imp" with "IMP":', movie.replace('Imp', 'IMP'))

# Check if 'ssion' is present in the string
print('Is "ssion" in the movie title?', 'ssion' in movie)
print('Is "zz" in the movie title?', 'zz' in movie)