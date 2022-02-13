from menu import Menu
from cofee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True

while is_on:
    options = menu.get_items()
    options = options[:-1]
    choice = input(f"What would you like? ({options}): ")

    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "refill":
        coffee_maker.refill_ingredients()
    else:
        drink = menu.find_drink(choice)

        if drink is None:
            print()
        elif coffee_maker.is_resources_sufficient(drink) and money_machine.make_payments(drink.cost):
            coffee_maker.make_coffee(drink)
