import random

print("Welcome to Dragon Coaster Park")

rand_discount = float(random.randint(1, 5))
ticket_bought = input("Would you like to buy a ticket? (yes/no): ")
coupon_value = 5
free_ticket = False


if ticket_bought.upper() == "YES":
    guest_age = int(input("Enter guest age: "))
    coupon = input("Do you have a coupon? (yes/no): ")

    if coupon.upper() == "YES":
         discount_total = coupon_value + rand_discount
    else:
         discount_total = rand_discount

    match guest_age:
        case n if n < 5:
            free_ticket = True
            base_ticket = 0
        case n if n >= 5 and n <= 12:
            base_ticket = 12
        case n if n >= 13 and n <= 64:
              base_ticket = 25
        case n if n >= 65:
              base_ticket = 15

    ticket_total = base_ticket - discount_total

    if free_ticket == False:
         print(f"Mystery discount: ${rand_discount:.2f}")
         print(f"Your ticket costs: ${ticket_total:.2f}")
    else:
         print("Your ticket is free")

elif ticket_bought.upper() == "NO":
    print("Thanks, maybe next time")
else:
    print("Invalid input, Please try again")
