print("Intro to Python")
# Comment - does not execute
# To comment multiple
# line, highlight and
# ctrl /

# Case sensitive.
# Extra spaces do not matter around commands, operators
# Spaces DO matter in indentaion (code blocks). Indentation creates a code block
# Strings can us "" or ''
# "" are more common due to lssues with apostropes in strings ('o'clock')
print("It's a groovy day")

# Escaple characters - provide ways insert values into strings and other behaviours
print("It's a \"groovy\" day")
print('It\'s a "groovy" day!')
print("Hello\nWorld") #New line
print("Name:\tShane") #Tab
print("\\n") #print an escape sequence

# Variables
# A named box that holds a value
# values can change
# variable names contain only letters, numbers and _
# Cannot start with a number
# are written in snake_case
# in Python we do not explcilty declare variables before use
# Cannot be python keywords/reserved


# examples of assigning values to variables
first_name = "Liam" # string - written in quotes
age = 24 # interger
price = 4.24 # float
is_valid = True # Boolean (True/False)

age = 53

# Use a value in a variable
print(first_name)
print(age)

# String concatenation
# + is a string concatenation operator
print("Hello " + "World")
print("Hello " + first_name)

# When using + all values must be strings. we can cast the age to a string
print("Hello " + first_name + "! I see you are " + str(age) + " years old")

# You can use a comma and mix strings and numbers
print("Hello", first_name, "! I see you are", str(age), "years old")

# Preferred way (f strings)
print(f"Hello {first_name}! I see you are {age} years old")

# Constants - like a variable but is not supposed to change values
# Used to give a meaningfull name to a value
# Consants use SCREAMING_SNAKECASE
GST = .05

total = 100 * .05
print(total)
# BETTER
total = 100 * GST
print(total)

# user input
# input returns a string
#name = input("Enter your name: ")
#age = input("Enter your age: ")

#print(f"Hello {name}! You are {age} years old")

# prompt for 2 integers
# add them together
# display the sum
# number1 + number2 = sum
# int(), str(), float()

# number1 = int(input("Enter your first number: "))
# number2 = int(input("Enter your second number: "))

# sum = number1 + number2

# print(f"{number1} + {number2} = {sum}")

# # preferred  first one
# # or 

# number1 = input("Enter your first number: ")
# number2 = input("Enter your second number: ")

# sum = int(number1) + int(number2)

# print(f"{number1} + {number2} = {sum}")

# Math Operators

print(4 + 2)
print(4 - 2)
print(4 * 2)
print(4 / 2)# 2.0 / returns a float
print(9//4)# 2 floor division (rounds down to the nearest whole number)
print(2 ** 3)# exponent 
print(9 % 4)# 1 - Modulus remainder

# formatting numbers

total = 100.1234567
print(round(total,2))
print(round(total,6))

print(f"{total:.2f}")
print(f"{total:.6f}")

price = 100
print(f"{price:.2f}")

# Math functions
# import imports the math module which contains math functions and constants
import math

test_value = 5.245124

print(math.ceil(test_value)) # ceiling rounds up to the next whole number
print(math.floor(test_value)) # floor down to whole number
print(math.pow(2,3)) # exponent
print(math.sqrt(9)) # square root
print(max(1,4,56,1004)) # maximum
print(min(1,4,56,1004)) # minimum

