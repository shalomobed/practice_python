string = input("Please Enter Your String: ")
reversed = ''
while string!= "Quit" and string != "quit" and string != "q":
    for x in range(len(string)-1,-1,-1):
        reversed += string[x]
    print(f"Reversed: {reversed}")
    reversed=''
    string = input("Please Enter Your String: ")


