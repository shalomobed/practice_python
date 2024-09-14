password = input("Please enter your Password: ")
result=''
for position in password:
    if position == 'o':
        result += '0'
    elif position == 'i':
        result += '1'
    elif position == 'a':
        result += '@'
    elif position == 'e':
        result += '3'
    elif position == 'A':
        result += '4'
    elif position == 'B':
        result += '8'
    elif position == 's':
        result += '$'
    else:
        result += position

print(f"Your new strong password is: {result}!")


