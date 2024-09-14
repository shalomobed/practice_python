interstate_number = int(input("Please enter an interstate number: "))
type = ""
direction = ""
primary_number = 0
type_p = ""

if 100 <= interstate_number <= 999 and interstate_number%100 != 0:
        type = "auxiliary"
        primary_number = interstate_number % 100
        if 1 <= primary_number <= 99:
            type_p = "primary"
            if primary_number % 2 == 0:
                direction = "east/west"
            else:
                direction = "north/south"
        else:
            print(interstate_number, "is not a valid interstate highway number.")

elif 1 <= interstate_number <=99:
    primary_number = interstate_number%100
    type_p = "primary"
    if interstate_number % 2 == 0:
        direction = "east/west"
    else:
        direction = "north/south"

else:
    print(interstate_number, "is not a valid interstate highway number.")

if type:
    print(f"I-{interstate_number} is {type}, serving I-{primary_number}, going {direction}.")
if type_p:
    print(f"I-{primary_number} is {type_p}, going {direction}.")

