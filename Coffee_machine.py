MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0
}

class CoffeeMachine:
    def __init__(self):
        """Initialize the coffee machine with default resources and menu."""
        self.resources = resources.copy()
        self.menu = MENU

    def report(self):
        """Print the current resource values."""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")
        print(f"Money: ${self.resources['money']}\n")

    def is_resource_sufficient(self, drink):
        """
        Check if there are enough resources to make the selected drink.
        
        Args:
            drink (str): The name of the drink selected.
        
        Returns:
            bool: True if resources are sufficient, False otherwise.
        """
        ingredients = self.menu[drink]['ingredients']
        for item in ingredients:
            if self.resources.get(item, 0) < ingredients[item]:
                print(f"Sorry there is not enough {item}.\n")
                return False
        return True

    def process_coins(self):
        """
        Process the coins inserted by the user.
        
        Returns:
            float: The total amount of money inserted.
        """
        print("Please insert coins.")
        try:
            quarters = int(input("How many quarters? "))  # $0.25
            dimes = int(input("How many dimes? "))        # $0.10
            nickles = int(input("How many nickles? "))    # $0.05
            pennies = int(input("How many pennies? "))    # $0.01
        except ValueError:
            print("Invalid input. Please insert coins again.\n")
            return 0.0

        total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
        return total

    def is_transaction_successful(self, money_received, drink_cost):
        """
        Check if the transaction is successful based on the money received.
        
        Args:
            money_received (float): The total money inserted by the user.
            drink_cost (float): The cost of the selected drink.
        
        Returns:
            bool: True if transaction is successful, False otherwise.
        """
        if money_received < drink_cost:
            print("Sorry that's not enough money. Money refunded.\n")
            return False
        elif money_received > drink_cost:
            change = round(money_received - drink_cost, 2)
            print(f"Here is ${change} dollars in change.\n")
        self.resources['money'] += drink_cost
        return True

    def make_coffee(self, drink):
        """
        Deduct the required resources and make the coffee.
        
        Args:
            drink (str): The name of the drink to be made.
        """
        ingredients = self.menu[drink]['ingredients']
        for item in ingredients:
            self.resources[item] -= ingredients[item]
        print(f"Here is your {drink} ☕️. Enjoy!\n")

    def run(self):
        """Run the coffee machine program."""
        machine_on = True
        while machine_on:
            choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
            if choice == 'off':
                machine_on = False
                print("Turning off the coffee machine. Goodbye!")
            elif choice == 'report':
                self.report()
            elif choice in self.menu:
                if self.is_resource_sufficient(choice):
                    payment = self.process_coins()
                    if self.is_transaction_successful(payment, self.menu[choice]['cost']):
                        self.make_coffee(choice)
            else:
                print("Invalid selection. Please choose espresso, latte, or cappuccino.\n")


if __name__ == "__main__":
    coffee_machine = CoffeeMachine()
    coffee_machine.run() 