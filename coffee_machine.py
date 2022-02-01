from coffee_maker import CoffeeMaker
from menu import Menu, MenuItem
from money_machine import MoneyMachine

coff_mach = CoffeeMaker()
coff_mach_menu = Menu()  # Already has all the drink information added.

bank = MoneyMachine()

continue_running = True

while continue_running:
    choice = input("What would you like to do? (items/espresso/latte/cappuccino/report/replenish/off): ")
    if choice == "off":
        continue_running = False
        print("Machine Shutdown")
    elif choice == "items":
        print(coff_mach_menu.get_items())
    elif choice == "report":
        coff_mach.report()
        bank.report()
    elif choice == "replenish":
        coff_mach.replenish()
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        for drink in coff_mach_menu.menu:
            if drink.name == choice:
                if coff_mach.is_resource_sufficient(drink):
                    if bank.make_payment(drink.cost):
                        coff_mach.make_coffee(drink)
