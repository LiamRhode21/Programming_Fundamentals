# List Methods

# Sorting
numbers = [42, 4, 45, 7, 200, 5]
numbers.sort() # sort ascending
print(numbers)

numbers.sort(reverse= True)
print(numbers)

# Add a value to a list 
colors = ["red", "green"]
colors.append("orange") # end of list
colors.insert(1, "blue")
print(colors)

# extend with another list 
new_list = ["brown", "purple"]
colors.extend(new_list)
print(colors)

# insert in the middle of a list with a slice
colors[4:4] = ["cyan", "yellow"]
print(colors)

# removing values
pets = ["cats", "dogs", "ferrets", "guinea pigs", "parrots"]
removed_pet = pets.pop(4)# remove at an index and returns the value in that index
print(removed_pet)
print(pets)

# remove by value
pets.remove("guinea pigs")
print(pets)

# remove the element 
del pets[0]
print(pets)

# removing a value that does not exist is an error
# pets.remove("guinea pigs")

# check if value is in list
cities = ["Edmonton", "Calgary", "Vancouver", "Red Deer"]
check = "Edmonton" in cities
print(check)
print(f"Edmonton is in the list? {"Edmonton" in cities}")

if "Edmonton" in cities:
    cities.remove("Edmonton")

# index of a value
print(f"The index for Calgary is: {cities.index("Calgary")}")

# count the occurrences of a value in a list
cities = ["Edmonton", "Calgary", "Vancouver", "Red Deer", "Edmonton"]
print(f"Edmonton is in the list {cities.count("Edmonton")} times")

# clear a list
cities.clear()
print(cities)

heights = []
height = input("Enter your height: ")
heights.append(height)
height = input("Enter your height: ")
heights.append(height)
height = input("Enter your height: ")
heights.append(height)
print(heights)

