import math

try:
    radius = float(input("Enter the radius of the circle: "))
except ValueError:
    print("Invalid input! Please enter a numeric value for the radius.")
else:
    area = math.pi * radius**2
    circumference = 2 * math.pi * radius

    print("The area of the circle is:", area)
    print("The circumference of the circle is:", circumference)
