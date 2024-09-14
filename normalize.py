count = int(input("Please enter the number of floating-point values: "))

fp_list = []
for x in range(count):
    fp_values = float(input("Please enter a floating-point value: "))
    fp_list.append(fp_values)
largest_value = (max(fp_list))
print("")
print("Normalized Floating-Point Values:")
for x in fp_list:
    fp_norm = (x/largest_value)
    print(f"{fp_norm:.2f}")
