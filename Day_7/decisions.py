# decisions allow us to control the flow of the code

# age = 11

# if age >= 18:
#     print("You are an adult")
#     print("Have a groovy day!")


# print("This is fun!")# always executes

# comparison operators: ==, !=, <, >, <=, >=

# name = input("Enter your name: ")
# if name == "Liam":
#     print("Awesome name!")

# remember it is case sensitive
# safe comparison ignoring case
# name = input("Enter your name: ")
# if name.upper() == "LIAM": # compare upper case of user name
#     print("Awesome name!")

# Else
# name = input("Enter your name: ")
# if name.upper() == ("LIAM"):
#     print("Awesome name!")
# else:
#     print("Nobody's perfect....")

# grade = 70
# if grade >= 50:
#     print("pass")
# else:
#     print("fail")


grade = 0
# multiple conditions 
if grade >= 80:
    print("Honors!")
    print("You are smart!")
elif grade >= 50:
    print("pass")
elif grade == 0:
    print("Did you show up?")
else: # if none of the above conditions are true
    print("fail")
    print("Please try again")

print("Have a groovy day!")