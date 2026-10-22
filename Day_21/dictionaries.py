# Dictionaries - store data in a key-value pairs
# Keys are unique. strings or numbers
# Values can be anything(strings, bool, int..., dictionaries)

# Example
student = {"name":"Homer", "age":44, "email":"Homer@gmail.com"}

# access values by the key
print (student["name"])# retrieve a value
student["age"] = 42# update a value
student["city"] = "Springfield"# create a new key/value

# key = input("Enter a new key: ")
# value = input("Enter a value for that key: ")
# student[key] = value

# remove a key/value
del student["email"]

print(student)

# using a key that does not exist is a KeyError
# del student["favorite_color_smartie"]

# check if key exists:
if "favorite_color_smartie" in student:
    del student["favorite_color_smartie"]

# Use get to retrieve value
# returns none if key does not exist
print(student.get("favorite_color_smartie"))
# OR return a different value
print(student.get("favorite_color_smartie","N/As"))

# Dictionaries as values
inventory = {
    "apples":{"stock_count": 5, "price": .30},
    "bananas":{"stock_count": 55, "price": .20},
    "oranges":{"stock_count": 40, "price": .25}
}

print(inventory["apples"]["price"])

# Loop through a dictionary
student = {"Homer":30, "Lisa":98, "Bart":45, "Marge":70}
# keys
for key in student: # by default keys are returned
    print(f"{key}: {student[key]}")

# Loop through the values:
# get average of all the grades
total = 0
for grade in student.values():
    total += grade
average = total / len(student)
print(f"Average grade: {average}")

# Retrieve both key and values 
for name, grade in student.items():
    print(f"{name}: {grade}")

# sort by the key
for name, grade in sorted(student.items()):
    print(f"{name}: {grade}")

# Reverse
for name, grade in sorted(student.items(), reverse=True):
    print(f"{name}: {grade}")

inventory = {"apples":0, "bananas":0, "oranges":0}
purchases = ["apples","bananas","apples","oranges","apples"]

# Add the boxes of purchases to the inventory.
# Result {"apples":3, "bananas":1, "oranges":1}

#print out
#apples: 3
#bananas: 1
#oranges: 1

# inventory["apples"] = purchases.count("apples")
# inventory["bananas"] = purchases.count("bananas")
# inventory["oranges"] = purchases.count("oranges")
for purchase in purchases:
    inventory[purchase] += 1

for item, amount in inventory.items():
    print(f"{item}: {amount}")

for item in inventory:
    amount = purchases.count(item)
    print(f"{item}: {amount}")