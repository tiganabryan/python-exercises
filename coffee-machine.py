import sys

resources = {
    "Water": 100,
    "Milk": 50,
    "Coffee": 76,
    "Money": 2.5,
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
        elif order == "stop":
            is_on = False


take_order()


# def take_order():
#     order = input("what would you like? (espresso/latte/cappuccino): ")

#     if order == "espresso" or "latte" or "cappucino":
#         print(f"1 {order} coming up!")

#     elif order == "stop":
#         sys.exit()

#     elif order == "report":
#         for field in resources:
#             print(f"{field}: {field.value}")


# take_order()
