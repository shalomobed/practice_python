speed_limit = int(input("Please enter the speed limit for the road: "))
driving_speed = int(input("Please enter the vehicle's recorded speed: "))
fine = 0
if driving_speed < speed_limit:
    if speed_limit - driving_speed < 10:
        print("There is no fine.")
    elif speed_limit - driving_speed >= 10:
        fine = 50
elif driving_speed > speed_limit:
    if driving_speed - speed_limit < 6:
        print("There is no fine.")
    elif driving_speed - speed_limit <= 20:
        fine = 75
    elif driving_speed - speed_limit <= 40:
        fine = 150
    else:
        fine = 300
else:
    print("There is no fine.")


if fine > 0:
    print(f"The speeding fine is ${fine}.")
