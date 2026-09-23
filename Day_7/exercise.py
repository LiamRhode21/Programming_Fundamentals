# Simple Decision Exercise
# Use if/else in the following questions.

# 1. Prompt the user for two number and display a message indicating if they are equal or not.

# number1 = int(input("Enter your first number: "))
# number2 = int(input("Enter your second number: "))

# if number1 == number2:
#     print(f"{number1} and {number2} are equal")
# else:
#     print(f"{number1} and {number2} are not equal")

# 1 print

# number1 = int(input("Enter your first number: "))
# number2 = int(input("Enter your second number: "))

# result = " "

# if number1 != number2:
#     result = " not "
# print(f"The numbers are{result}equal")

# 2. Prompt the user for two numbers and display the highest value.

# number1 = int(input("Enter your first number: "))
# number2 = int(input("Enter your second number: "))

# if number1 > number2:
#     print(f"{number1} is higher then {number2}")
# elif number2 > number1:
#     print(f"{number2} is higher then {number1}")
# else:
#     print("they are equal")

# 3. Prompt the user for two numbers and display the highest value as well as display if it was the
# second or first number entered.

# number1 = int(input("Enter your first number: "))
# number2 = int(input("Enter your second number: "))

# if number1 > number2:
#     print(f"{number1} is higher then {number2} and it was the first number entered")
# elif number2 > number1:
#     print(f"{number2} is higher then {number1} and it was the second number entered")
# else:
#     print("they are equal")

# 4. Prompt the user for three numbers and display the highest value.

# number1 = int(input("Enter your first number: "))
# number2 = int(input("Enter your second number: "))
# number3 = int(input("Enter your third number: "))

# highest_number = number1
# if highest_number < number2:
#     highest_number = number2
# if highest_number < number3:
#     highest_number = number3

# print(f"out of {number1}, {number2}, {number3} the highest is {highest_number}")

# 5. Prompt the user for a number and display a message indicating if it is even or odd.

# number = int(input("Enter your number: "))

# if number % 2 == 0:
#     print(f"{number} is even")
# else:
#     print(f"{number} is odd")

# 6. Prompt the user for 2 numbers and a menu to allow them to choose to display the equation and
# answer for adding, subtracting, multiplying or dividing the numbers.

number1 = float(input("Enter number 1: "))
number2 = float(input("Enter number 2: "))
operation = input("Enter a operation to preform(+ - * /): ")
total = 0

if operation == "+":
    total = number1 + number2
elif operation == "-":
    total = number1 - number2
elif operation == "*":
    total = number1 * number2
elif operation == "/":
    total = number1 / number2
else:
    print("Invalid operator")

if operation in ["+", "-", "*", "/"]:
    print(f"{number1:g} {operation} {number2:g} = {total:g}")

# :g gets rid of unnecessary decimals 


# Challenge: If the user enters a invalid operation, display an error message