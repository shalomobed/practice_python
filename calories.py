age = int(input ("Please enter your age: "))
weight = int(input ("Please enter your weight in pounds: "))
heart_rate = int(input("Please enter your heart rate in beats per minutes: "))
time = int(input("Please enter the length of your workout in minutes: "))

calories_burned = ((age * 0.2757 + weight * 0.03295 + heart_rate * 1.0781 - 75.4991) * time)/8.368
calories_burned = round(calories_burned,2)
#print ("Calories burned: ", calories_burned, "calories")
print(f"Calories burned: {calories_burned:.2f} calories")