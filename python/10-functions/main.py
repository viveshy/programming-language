#1. Function without params
def greet():
    print("Hare Krishna!")

# Call greet function
greet()

#2. Function with params
def greet_with_timme(name, time):
    print(f'Good {time}, {name}!')

greet_with_timme('Krishna', 'morning')

#3. Default params
def greet_with_default_params(name = 'Ram', time = 'night'):
    print(f'Good {time}, {name}')

greet_with_default_params()

#4. Return 
def calculate_area_of_circle(radius):
    return 3.142 * radius **2

area = calculate_area_of_circle(2)
print(f'Area of circle is {area}')