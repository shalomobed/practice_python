import math
import random
radius = int(input("Please enter the radius of the sphere: "))
volume = float(4/3 * math.pi * pow(radius,3))
print (f"The volume of a sphere with radius of {radius} is {volume:.2f}")


num = random.randint(1,10)
factorial = math.factorial(num)
print("The factorial of",num, "is", factorial)
