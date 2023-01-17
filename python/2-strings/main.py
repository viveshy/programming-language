# What is string in python?
# A string in python is a sequence of character enclosed within single or double quotes. In Golang, strings are enclosed within double quotes only.

#1)_______Declaring stings in python
name = "Bruce Wayne"
city = 'Gotham'
dialogue = "I'm batman"

#2)__________ Escape character
joker_says = 'What doesn\'t kill you makes you strong.'


#3)_________Accessing characters of string (It's like accessing element of array)
greet = 'hello'

#Forward accessing, starts from 0
print(greet[0])

#Backward accessing, starts from -1
print(greet[-1])
print(greet[-5])


#4)___________Slicing strings
#Syntax: string_name[inclusive:exclusive]  
#Syntac: string_name[inclusie1:-inclusive2] -- inclusive2 starts from 1

print(greet[0:3])  # Output = hel
print(greet[2:-1])  # Output = le

#The original string does not change while slicing strings

#5)______________String concatenation
batman = 'Rober Pattinson'
catwoman = 'Zoe Kravitz'

# Add strings
print(batman + ' ' + catwoman)

# Multiply strings (repeat the string)
print(batman * 4)


#6)__________Methods on strings
#upper
print(batman.upper())

#lower
print(batman.lower())

#split
cheeses = "brie, chedder, stilton"
cheeses_array = cheeses.split(",")

print(cheeses_array)

#len     -- find the length of the string
print(len(batman))
