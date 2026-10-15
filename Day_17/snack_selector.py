snacks = ["Popcorn", "Pretzels", "Cookies", "Nachos"]

print("Available Snacks\n")

for index, snack in enumerate(snacks, start= 1):
    print(f"{index}. {snack}")

try:
    choice = int(input("Enter your choice(1-4): "))

except ValueError:
    print(f"Enter an integer")

else:
    try: 
        if choice < 1:
            raise ValueError("choice cannot be less than 1")
        choice_string = snacks[choice - 1]
    except ValueError as error_msg:
        print(f"Invalid Choice: {error_msg}")
    except IndexError:
        print("There is no snack with that number")
    else:
        print(f"\nSelected snack: {choice_string}")

