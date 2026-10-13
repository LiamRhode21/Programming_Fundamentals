snacks = ["Popcorn", "Pretzels", "Cookies", "Nachos"]

print("Available Snacks\n")

for index, snack in enumerate(snacks, start= 1):
    print(f"{index}. {snack}")

try:
    choice = int(input("Enter your choice(1-4): "))

    if choice < 1:
        raise ValueError("choice cannot be less than 1")
    
    choice_string = snacks[choice - 1]

except ValueError as error:
    print(f"Please enter a valid input: {error}")

except IndexError as error:
    print(f"{error}")

else:
    print(f"\nSelected snack: {choice_string}")