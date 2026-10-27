
#__name__ contains the name of the module being executed
#if you run the module directly __name__ will contain __main__
#if you run the module from an import __name__ will contain the name of the module you imported
# print(f"Module Name: {__name__}")

#import functions
from .display import display_welcome,display_output
# from display import *          * means all functions
from .pricing import calculate_total
from .validation import get_valid


def main():
    UNIT_PRICE = 2.99
    
    display_welcome()
    item_name = input("Snack name: ")
    quantity = get_valid()
    # total = calculate_total(quantity, UNIT_PRICE)
    # total = calculate_total(quantity)
    total = calculate_total(quantity = quantity, unit_price = UNIT_PRICE)
    display_output(item_name, quantity,total)

# this is called a main guard. Its purpose is to only run the mainline if this module (snack_shack.py) is run directly (not from import)
if __name__ == "__main__":
    main()