class VendingMachine:
    def __init__(self, initial_soda, initial_water, initial_coffee):
        self.soda_count = initial_soda
        self.water_count = initial_water
        self.coffee_count = initial_coffee

    def purchase(self, drink_type):
        if drink_type == 'soda':
            if self.soda_count > 0:
                print("Dispensing Soda. Enjoy!")
                self.soda_count -= 1
            else:
                print("Sorry, out of Soda.")
        elif drink_type == 'water':
            if self.water_count > 0:
                print("Dispensing Water. Enjoy!")
                self.water_count -= 1
            else:
                print("Sorry, out of Water.")
        elif drink_type == 'coffee':
            if self.coffee_count > 0:
                print("Dispensing Coffee. Enjoy!")
                self.coffee_count -= 1
            else:
                print("Sorry, out of Coffee.")
        else:
            print("Invalid drink type. Please choose from soda, water, or coffee.")

    def restock(self, drink_type, quantity):
        if drink_type == 'soda':
            self.soda_count += quantity
            print(f"Restocked {quantity} bottles of Soda.")
        elif drink_type == 'water':
            self.water_count += quantity
            print(f"Restocked {quantity} bottles of Water.")
        elif drink_type == 'coffee':
            self.coffee_count += quantity
            print(f"Restocked {quantity} bottles of Coffee.")
        else:
            print("Invalid drink type. Please choose from soda, water, or coffee.")

    def report_inventory(self):
        print(f"Current Inventory: Soda - {self.soda_count} bottles, Water - {self.water_count} bottles, Coffee - {self.coffee_count} bottles")


def main():
    vending_machine = VendingMachine(10, 20, 15)

    while True:
        command = input("Enter command (purchase, restock, report, quit/q): ").lower()

        if command in ['quit', 'q']:
            break
        elif command == 'purchase':
            drink_type = input("Enter drink type (soda, water, coffee): ").lower()
            vending_machine.purchase(drink_type)
        elif command == 'restock':
            drink_type = input("Enter drink type to restock (soda, water, coffee): ").lower()
            quantity = int(input("Enter quantity to restock: "))
            vending_machine.restock(drink_type, quantity)
        elif command == 'report':
            vending_machine.report_inventory()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
