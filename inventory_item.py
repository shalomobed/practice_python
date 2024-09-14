class InventoryItem:
    def __init__(self, name: str, quantity: int):
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return str(f"Item's Name: {self.name}; Current Stock: {self.quantity};")

    def add_stock(self, amount: int):
        if amount < 0:
            raise ValueError("Invalid amount")
        self.quantity += amount

    def remove_stock(self, amount: int):
        if amount > self.quantity or amount < 0:
            raise ValueError("Invalid operation")
        self.quantity -= amount


def main():
    try:
        print("- Cups")
        cups = InventoryItem("Cups", 30)
        cups.add_stock(4)
        print(cups)
        cups.remove_stock(15)
        print(cups)

        print("\n- Glasses")
        glasses = InventoryItem("Glasses", 50)
        glasses.add_stock(5)
        print(glasses)
        glasses.remove_stock(70)
        print(glasses)

    except ValueError as e:
        print("Error is:", e)


if __name__ == "__main__":
    main()
