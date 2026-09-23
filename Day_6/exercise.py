# 1. One acre of land is equal to 43,560 square feet. Write a program that asks the user to enter the number of acres and
# display the number of square feet.
# Output:
# Acre to Square foot converter. How many acres do you have? 25
# You have 25 acres which is equal to: 1089000 square feet

# CONVERSION_RATE = 43,560

# acres = int(input("Acre to Square foot converter. How many acres do you have? "))

# square_feet =  acres * CONVERSION_RATE

# print(f"You have {acres} acres witch is equal to: {square_feet} square feet")

# 2. Write a program that asks the user to enter three test scores. The program should display each test score, as well as
# the average test of the users' scores.
# Output:
# Enter the first test score: 10
# Enter the second test score: 20
# Enter the third test score: 30
# Test Score 1: 10.0
# Test Score 2: 20.0
# Test Score 3: 30.0
# Average Score: 20.0

# test1 = float(input("Enter your first test score: "))
# test2 = float(input("Enter your second test score: "))
# test3 = float(input("Enter your third test score: "))

# avg_score = (test1 + test2 + test3) / 3

# print(f"Test Score 1: {test1}")
# print(f"Test Score 2: {test2}")
# print(f"Test Score 3: {test3}")
# print(f"Average Score: {avg_score}")

# 3. A bag of cookies holds 40 cookies. The calorie information on the bag claims that there are 10 "servings" in the bag
# and that a serving equals 300 calories. Write a program that asks the user to input how many cookies they ate and
# then reports how many total calories were consumed.
# Output:
# How many cookies did you eat? 25
# You ate 25 cookies
# Which is equal to: 1875.0 calories

#4 cookie = 1 serving = 300 cal 300/4

# cookies = int(input("How many cookies did you eat: "))

# CAL_PER_COOKIE = 75

# cal = cookies * CAL_PER_COOKIE

# print(f"You ate {cookies} cookies")
# print(f"Which is equal to: {cal} calories")


# 4. Ask the user for
#  number of pizzas (int)
#  price per pizza (float, dollars)
#  tip percent (float; e.g., 15 for 15%)
#  number of people sharing (int)
# Calculate and print: subtotal, tip amount, total, and amount per person.
# Formatting currency to 2 decimals. Display appropriate inputs and outputs.



# 5. Ask the user for a currency amount and display the number of dollars, quarters, dimes, nickels, and pennies in that
# amount. Display appropriate inputs and outputs.

total = float(input("Enter currency amount: "))

total_processed = round(total * 100)

dollars = total_processed // 100
remaining = total_processed % 100
quarters = remaining // 25
remaining = remaining % 25
dimes = remaining // 10
remaining = remaining % 10
nickels = remaining // 5
remaining = remaining % 5
pennies = remaining // 1

print(dollars)
print(quarters)
print(dimes)
print(nickels)
print(pennies)