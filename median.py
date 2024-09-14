first = int(input("Please enter the first number: "))
second = int(input("Please enter the second number: "))
third = int(input("Please enter the third number: "))

median = 0
if first > second and first > third:
    if second > third:
        median = second
    else:
        median = third
elif second > first and second > third:
    if first > third:
        median = first
    else:
        median = third
elif third > first and third > second:
    if first > second:
        median = first
    else:
        median = second
print("The median number is", median)
