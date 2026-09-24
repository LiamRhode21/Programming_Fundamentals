import random

number_list = [random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)]

guess = int(input("Guess a number that is in the list (1-10): "))

print(f"{"You Win!" if guess in number_list else "You Lose!"}")
print(f"The numbers were: {number_list}")