# Formula creation
import math

#Input always treats the variable as string. Remember to type cast
radius = int(input("Enter radius of circle: "))
pie = math.pi

area = pie * radius**2

print("The area of the circle is", area)