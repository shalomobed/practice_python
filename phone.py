phone_number = int(input("Please enter your phone number: "))
line = phone_number%10000
prefix = (phone_number%10000000)//10000
area_code = (phone_number%10000000000)//10000000
line, prefix, area_code = str(line), str(prefix), str(area_code)
output = ("("+area_code+") "+prefix +"-"+line)
print("Phone Number:", output )
