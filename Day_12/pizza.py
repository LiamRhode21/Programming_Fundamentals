sold_out = ["mushrooms", "bacon"]
banned_toppings = ["pineapple"]

toppings = []
topping_number = 1
toppings_added = 0

while len(toppings) < 5:
    toppings.append(input(f"Enter topping {topping_number}: ").lower())
    topping_number += 1

print("Requested toppings:")
for index, topping in enumerate(toppings, start= 1):
    print(f"{index}. {topping}")

for topping in toppings:
    if topping in sold_out:
        print(f"Sorry, {topping} is sold out!")
    elif topping in banned_toppings:
        print(f"{topping} is banned!")
    else:
        print(f"Adding {topping}")
        toppings_added += 1

toppings_total = toppings_added * 2

print(f"{toppings_added} toppings added \nTopping cost: ${toppings_total:.2f}")