# What does range do in Python?
# Range in python generates list of numbers
# For example: range(5) will generate [0,1,2,3,4]


# Syntax 1
print("Syntax 1...")
for n in range(5):
    print(n)

# Syntax 2
print("Syntax 2 ...")
for i in range(3,10):
    print(i)

# Syntax 3
print("Syntax 3...")
for j in range(2,20,2):
    print(j)

# Syntax 4
print("Syntax 4...")
burgers = ['chicken', 'veg', 'supreme', 'double']
for b in range(len(burgers)):
    print(b, burgers[b])