total = 0
counter = 0

while True:
    user_input = input("Enter an item price (q to quit): ")

    if user_input.lower() == "q":
        break
    else:
        total = total + float(user_input)
        counter += 1

print(f"Items purchased: {counter}")
print(f"Total cost: ${total:.2f}")