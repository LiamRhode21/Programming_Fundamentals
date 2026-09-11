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
