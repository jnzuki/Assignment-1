### Data ###
import data

recipes = data.recipes
class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input."""
        self.machine_resources = machine_resources  # Stores initial machine resources
        self.is_on = True  # Flag to keep the machine running

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for item in ingredients:
            if ingredients[item] > self.machine_resources[item]:
                print(f"Sorry, not enough {item}.")
                return False
        return True

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        print("Please insert coins.")
        total = int(input("how many quarters?: ")) * 0.25
        total += int(input("how many dimes?: ")) * 0.10
        total += int(input("how many nickels?: ")) * 0.05
        total += int(input("how many pennies?: ")) * 0.01
        return total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient."""
        if coins >= cost:
            change = round(coins - cost, 2)
            if change > 0:
                print(f"Here is ${change} in change.")
            print("Transaction successful!")
            return True
        else:
            print("Sorry, that's not enough money. Money refunded.")
            return False

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources."""
        for item in order_ingredients:
            self.machine_resources[item] -= order_ingredients[item]
        print(f"Making your {sandwich_size} sandwich. Enjoy!")

    def report(self):
        """Prints a report of all machine resources."""
        print("Current resources:")
        for item, quantity in self.machine_resources.items():
            print(f"{item}: {quantity}")

    def turn_off(self):
        """Turns off the machine."""
        self.is_on = False
        print("Turning off the machine...")


# Initialize the machine with available resources
machine_resources = {
    "bread": 12,  # slice
    "ham": 18,  # slice
    "cheese": 24,  # ounces
}

sandwich_machine = SandwichMachine(machine_resources)



# Main program loop
while sandwich_machine.is_on:
    choice = input(
        "What size sandwich would you like? (small/medium/large) or type 'report' to view resources or 'off' to turn off: ").lower()

    if choice == "off":
        sandwich_machine.turn_off()
    elif choice == "report":
        sandwich_machine.report()
    elif choice in recipes:
        sandwich = recipes[choice]
        if sandwich_machine.check_resources(sandwich["ingredients"]):
            payment = sandwich_machine.process_coins()
            if sandwich_machine.transaction_result(payment, sandwich["cost"]):
                sandwich_machine.make_sandwich(choice, sandwich["ingredients"])
    else:
        print("Invalid selection. Please choose again.")











