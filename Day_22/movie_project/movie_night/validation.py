def get_valid_age():
    while True:
        try:
            age = int(input("Enter an age: "))
        except ValueError:
            print("Enter a positive whole number")
            continue
        if age >= 0:
            return age
        else:
            print("Enter a positive whole number")

def get_valid_quantity():
    while True:
        try:
            tickets = int(input("enter number of tickets: "))
        except ValueError:
            print("Enter number greater than 0")
            continue
        if tickets > 0:
            return tickets
        else:
            print("Enter number greater than 0")

