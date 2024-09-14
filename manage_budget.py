class Budget:
    def __init__(self):
        #Initial budget
        self.categories = {"rent": -1200, "sales": 3000, "marketing": -500}

    def add_category(self, category, amount):
        if category in self.categories:
            raise ValueError(f"Category '{category}' already exists.")
        self.categories[category] = amount

    def remove_category(self, category):
        if category not in self.categories:
            raise ValueError(f"Category '{category}' does not exist.")
        del self.categories[category]

    def update_category(self, category, amount):
        if category not in self.categories:
            raise ValueError(f"Category '{category}' does not exist.")
        self.categories[category] = amount

    def manage_budget(self,**kwargs):
        for operation, categories in kwargs.items():
            if operation == "add":
                for category, amount in categories.items():
                    self.add_category(category, amount)
            elif operation == "remove":
                for category in categories:
                    self.remove_category(category)
            elif operation == "update":
                for category, amount in categories.items():
                    self.update_category(category, amount)
            else:
                raise ValueError(f"Invalid operation '{operation}'.")
        return self.categories

#Calling initial budget
budget = Budget()

#Add categories
budget.manage_budget(add={"utilities": -300, "snacks": -100})

#Update categories
budget.manage_budget(update={"sales": 3200})

#Remove categories
budget.manage_budget(remove=["marketing"])

#Print updated budget
print(budget.categories)
