def print_delivery(customer, city, parcels):
    print(f"{customer} has {parcels} going to {city}")

# the order matters because the order of the arguments passed in are in the order that the tuple is

delivery = ("Maya", "Edmonton", 3)
print_delivery(*delivery)