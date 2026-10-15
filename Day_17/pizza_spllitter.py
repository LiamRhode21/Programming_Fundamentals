try:
    total_pizza_cost = float(input("Enter the total pizza cost: "))
    numb_of_people = int(input("Enter the number of people splitting the pizza: "))
    cost_per_person = total_pizza_cost / numb_of_people

except ZeroDivisionError:
    print("Invalid input do not enter 0")
except ValueError:
    print("Invalid input please enter a number")
else:
    print(f"{total_pizza_cost:.2f} split between {numb_of_people} is {cost_per_person:.2f}")