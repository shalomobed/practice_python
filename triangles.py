import math
# my name is Shalom Obed and this is a code identifying the type of triangle

# user inputs the side lengths of the triangle
a = int(input("Please enter the length side A of the triangle (in metres): "))
b = int(input("Please enter the length side B of the triangle (in metres): "))
c = int(input("Please enter the length side C of the triangle (in metres): "))
# finding the perimeter
perimeter = (a+b+c)
print("The perimeter of the triangle is", perimeter, "m")
# finding the area using Hero's Formula
s = (0.5 * (a+b+c))
area = (math.sqrt(s*(s-a)*(s-b)*(s-c)))
print("The area of the triangle is", area, "m^2")
# identifying the type of triangle using 'if-else'
# checking for a right triangle
if a * a + b * b == c * c:
    print("It is a Right Triangle")
# checking for an acute triangle
elif a * a + b * b > c * c:
    if a < b < c:
        print("It is an Acute Triangle")
    else:
        print("Acute triangle ('A' ought to be the smallest number and 'C' the largest as the hypotenuse)")
# checking for an obtuse triangle
elif a * a + b * b < c * c:
    if a < b < c:
        print("It is an Obtuse Triangle")
    else:
        print("Obtuse triangle ('A' ought to be the smallest number and 'C' the largest as the hypotenuse)")
# if user's input doesn't identify with any type of triangle
else:
    print("It is neither an acute, obtuse or right triangle.")