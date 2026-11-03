from .snack_shack.display import display_welcome, display_output
from .snack_shack.validation import get_non_empty_string, get_valid_integer
from .snack_shack.pricing import calculate_total

def main():
    print("School Movie Night - Snack Sales")
    display_welcome()
    snack = get_non_empty_string("What snack are we selling?")
    while True:
        quantity = get_valid_integer("Enter a quantity")
        if quantity > 0:
            break
        else:
            print("Must be a whole number and more than 0")

    total = calculate_total(quantity)
    display_output(snack, quantity, total)
    print("Thanks for supporting out school movie night!")

if __name__ == "__main__":
    main()