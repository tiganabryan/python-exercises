# work in progress:)

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
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# for resource, amount in resources.items():
#     print(f"{resource}: {amount}")


is_on = True


def take_order():
    global is_on

    while is_on:
        order = input("what would you like? (espresso/latte/cappuccino): ")

        if order == "espresso" or order == "latte" or order == "cappucino":
            for category in MENU[order].items():
                print(category["ingredients"])
            # print(f"1 {order} coming up!")

        elif order == "off":
            is_on = False

        elif order == "report":
            print(f"water: {resources['water']}ml")
            print(f"milk: {resources['milk']}ml")
            print(f"coffee: {resources['coffee']}g")
            print(f"money: ${resources['money']}")


take_order()
