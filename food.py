menu = {
    "Hot Dog": 1.50,
    "Slice of Pizza": 1.99,
    "Whole Pizza": 9.95,
    "Soft Drink": 0.59
}
hot_dogs = int(input("Please enter the number of Hot Dogs: "))
pizza_slices = int(input("Please enter the number of  Pizza Slices: "))
pizza_whole = int(input("Please enter the number of Whole Pizzas: "))
soft_drinks = int(input("Please enter the number of Soft Drinks: "))
total = ((menu["Hot Dog"]*hot_dogs)
            + (menu["Slice of Pizza"]*pizza_slices)
            + (menu["Whole Pizza"]*pizza_whole)
            + (menu["Soft Drink"]*soft_drinks))
total = f'{total:.2f}'
print (str("The total cost of the order is $"+ total))
