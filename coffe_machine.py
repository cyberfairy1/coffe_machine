COFFEE_MENU = { 
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "price": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "price": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "price": 3.0,
    }
}

bank_balance = 0
supplies = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def enough_supplies(ingredients):
    """Check if we’ve got enough to make your drink. Returns True if we do, otherwise False."""
    for item in ingredients:
        if ingredients[item] > supplies[item]:
            print(f"Oh, looks like we’re short on {item}.")
            return False
    return True


def get_coins():
    """Ask the customer for coins and calculate the total inserted."""
    print("Insert your coins, please!")
    total = int(input("Quarters, how many?: ")) * 0.25
    total += int(input("Dimes, how many?: ")) * 0.10
    total += int(input("Nickels, how many?: ")) * 0.05
    total += int(input("Pennies, how many?: ")) * 0.01
    return total


def handle_transaction(payment, cost):
    """Handles the payment process, checks if enough money was given, and returns change if necessary."""
    if payment >= cost:
        change = round(payment - cost, 2)
        print(f"Here's ${change} back in change.")
        global bank_balance
        bank_balance += cost
        return True
    else:
        print("Not enough cash. Refunding your money.")
        return False


def brew_coffee(drink_name, ingredients):
    """Make the coffee and deduct ingredients from the supplies."""
    for item in ingredients:
        supplies[item] -= ingredients[item]
    print(f"Here's your {drink_name}. Enjoy!")


machine_running = True

while machine_running:
    order = input("What'll it be? (espresso/latte/cappuccino): ").lower()
    if order == "off":
        machine_running = False
        print("Powering down. See you next time!")
    elif order == "report":
        print(f"Water: {supplies['water']}ml")
        print(f"Milk: {supplies['milk']}ml")
        print(f"Coffee: {supplies['coffee']}g")
        print(f"Earnings: ${bank_balance}")
    elif order in COFFEE_MENU:
        drink = COFFEE_MENU[order]
        if enough_supplies(drink["ingredients"]):
            payment = get_coins()
            if handle_transaction(payment, drink["price"]):
                brew_coffee(order, drink["ingredients"])
    else:
        print(f"Sorry, we don't serve {order}. How about trying something from the menu?")
