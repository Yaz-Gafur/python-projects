from data import MENU, resources

profit = 0

def is_recources_enough(order_ingredients):
    for i in order_ingredients:
        if order_ingredients[i] > resources[i]:
            print(f"Sorry, there is not enought {i}.")
            return False
    return True

def process_coins():
    print("Please, insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
    
def make_coffee(drink_name, order_ingredients):
    for i in order_ingredients:
        recources[i] -= order_ingredients[i]
    print(f"Here is your {drink_name}. Enjoy!")


is_on= True


while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}g")
        print(f"Water: {profit}")
    else:
        drink = MENU[choice]
        if is_recources_enough(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
