# # 1. Ask the user for a temperature in Celsius and convert it to Fahrenheit.

# temp_c = float(input("What is your temperature in celsius: "))

# temp_f = (temp_c * 9 / 5) + 32

# print(f"{temp_c} degrees celsius is {temp_f:.2f} degrees fahrenheit")

# # 2. Ask the user for a name, an adjective, a verb (past tense) and a place.
# # Print a silly sentence using them.

# name = input("Give me a name: ")
# adjective = input("Give me an adjective: ")
# verb = input("Give me a verb (past tense): ")
# place = input("Give me place: ")

# print(f"{name} is {adjective} and {verb} to {place}")

# # 3. Ask the user for the width and height of a rectangle. There could be
# # decimals. Calculate and display the width, height, area, and perimeter.
# # Calculations print the results rounded to 3 decimal places.

# width = float(input("What is the width of your rectangle: "))
# height = float(input("What is the height of your rectangle: "))

# area = round(width * height,3)
# perimeter = round(2 * (width + height),3)

# print(f"Width: {width} \nHeight: {height} \nArea: {area} \nPerimeter: {perimeter}")

# 4. Ask for the price of an item and the quantity purchased. Display the
# amount of the total including GST.

# GST = .05
# price = float(input("What is the price of the item: "))
# quantity = int(input("What is the quantity purchased: "))

# total = round((price * quantity) * (GST + 1),2)

# print(f"Your total is ${total}")


# 5. Ask the user for a number of miles and print out how many kilometers
# it is. Display to 2 decimal places.
# The conversion rate is 1 mile = 1.609344 kilometers

# miles = float(input("Number of miles: "))
# KM_TO_M = 1.609344

# kilometers = round(miles * KM_TO_M,2)

# print(f"{miles} miles in kilometers is {kilometers}")

# 6. Ask the user for the distance they want to travel, the fuel consumption
# of their vehicle in l/100km and the price per litre. Display the cost for
# the trip!

# distance = int(input("How many Km are you traveling: "))
# fuel_consumption = float(input("How many liters does your car consume per 100Km: "))
# price = float(input("What is the price of gas per liters: "))

# cost = round(((fuel_consumption / 100) * distance) * price,2)

# print(f"Your total for the trip is {cost}")


# populate 2 variables with 2 numbers from the user print the variables
    # number 1
    # number 2
# swap the values that are in the variables print the variables


number1 = int(input("Enter Number 1: "))
number2 = int(input("Enter Number 2: "))

print(f"Number 1: {number1}")
print(f"Number 2: {number2}")

stored_number = number1
number1 = number2
number2 = stored_number

print(f"Number 1: {number1}")
print(f"Number 2: {number2}")