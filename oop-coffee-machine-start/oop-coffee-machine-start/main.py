from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_money_machine = MoneyMachine()
my_resource = CoffeeMaker()


"""Items available in the menu"""
menu = Menu()
machine_on = True
while machine_on:
    user_choice_of_drinks = menu.get_items()
    choice = input(f"what would you like {user_choice_of_drinks}:".lower())
    if choice == "off":
        machine_on = False
    elif choice == "report":
        print(my_resource.report())
        my_money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if my_resource.is_resource_sufficient(drink) and my_money_machine.make_payment(drink.cost):
            my_resource.make_coffee(drink)
        
