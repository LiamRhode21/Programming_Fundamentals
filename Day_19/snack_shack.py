# a function is block of code. you can define it once and call i as need.

def display_welcome():
    print("Welcome to the snack shack!")
    print("Most snack are $4.00 each.")

def calculate_total(quantity, unit_price = 4):
    total = quantity * unit_price
    return total

def display_output(item_name, quantity, total):
    print(f"Snack: {item_name}")
    print(f'Quantity: {quantity}')
    print(f"Total: ${total:.2f}")

def get_valid():
    while True:
        try:
            return int(input("How many? "))
        except ValueError:
            print("Please enter an integer.")



UNIT_PRICE = 2.99

display_welcome()
item_name = input("Snack name: ")
quantity = get_valid()
# total = calculate_total(quantity, UNIT_PRICE)
# total = calculate_total(quantity)
total = calculate_total(quantity = quantity, unit_price = UNIT_PRICE)
display_output(item_name, quantity,total)
