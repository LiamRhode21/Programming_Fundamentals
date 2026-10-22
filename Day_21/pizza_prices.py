toppings = {
 "cheese" : True,
 "pepperoni" : True,
 "mushrooms" : False,
 "pineapple" : False,
 "anchovies" : True,
 "olives" : False,
 "sausage" : True
}

topping_price = {
 "cheese" : 0.5,
 "pepperoni" : 2.0,
 "mushrooms" : 1.0,
 "pineapple" : 0.5,
 "anchovies" : 1.5,
 "olives" : 1.25,
 "sausage" : 2.25
}
BASE_PRICE = 12
total = BASE_PRICE
for topping in toppings:
    if toppings[topping] == True:
        total += topping_price[topping]
        print(topping)
    else:
        print(f"No {topping}")

TIP = .18
total += total * TIP
print(f"Your total is: {total}")

