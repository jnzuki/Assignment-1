# sandwich_maker.py

class SandwichMaker:
    def __init__(self, resources):
        """Initialize the sandwich maker with available resources."""
        self.resources = resources

    def check_resources(self, ingredients):
        """Returns True when the order can be made, False if ingredients are insufficient."""
        for item in ingredients:
            if ingredients[item] > self.resources[item]:
                print(f"Sorry, not enough {item}.")
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources."""
        for item in order_ingredients:
            self.resources[item] -= order_ingredients[item]
        print(f"Making your {sandwich_size} sandwich. Enjoy!")

    def report(self):
        """Prints a report of all machine resources."""
        print("Current resources:")
        for item, quantity in self.resources.items():
            print(f"{item}: {quantity}")
