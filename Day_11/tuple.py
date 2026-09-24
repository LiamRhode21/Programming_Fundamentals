# Same as a list but immutable (cannot change)
# defined with () insisted of []

# ask the user for a month name and print if it is a winter month
winter_months = ("December", "January", "February")
month = input("Enter a month: ")

if month in winter_months:
    print("Winter")
else:
    print("Not winter")

# OR
print(f"{"Winter" if month in winter_months else "Not Winter"}")

# unpacking a tuple
first_name, last_name = ("Liam", "Rhode")
print(f"Hello {first_name} {last_name}")

# list of tuples

characters = [("R2", "D3"), ("Han", "Solo"), ("Marty", "McFly")]
print(characters)
index = int(input("Enter a index to see a character: "))
print(f"The character is: {characters[index][0]} {characters[index][1]}")

