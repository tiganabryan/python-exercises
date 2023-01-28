import sys

resources = {
    "water": 100,
    "milk": 50,
    "coffee": 76,
    "money": 2.50,
}

# for resource, amount in resources.items():
#     print(f"{resource}: {amount}")


is_on = True


def take_order():
    global is_on

    while is_on:
        order = input("what would you like? (espresso/latte/cappuccino): ")

        if order == "espresso" or order == "latte" or order == "cappucino":
            print(is_on)
            print(f"1 {order} coming up!")

        elif order == "off":
            is_on = False

        elif order == "report":
            print(f"water: {resources['water']}ml")
            print(f"milk: {resources['milk']}ml")
            print(f"coffee: {resources['coffee']}g")
            print(f"money: ${resources['money']}")


take_order()
