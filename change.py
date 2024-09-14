cents = int(input("Please enter a number of cents: "))
quarters_num = cents//25
cents=cents%25
dimes_num = cents//10
cents = cents%10
nickels_num = cents//5
cents=cents%5
pennies_num = cents//1


print ("Coins: ", quarters_num, "quarters,", dimes_num, "dimes,", nickels_num, "nickels,", pennies_num, "pennies")