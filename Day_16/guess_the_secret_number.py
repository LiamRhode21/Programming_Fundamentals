import random

attempts = 0
secret_number = random.randint(1, 100)

while True:
    user_input = input("Guess the secret number: ")

    if user_input.lower() == "q":
        print(f"Lmao you suck you didn't even get it right after {attempts} attempts")
        break
    elif int(user_input) > secret_number:
        print("Too high!")
        attempts += 1
    elif int(user_input) < secret_number:
        print("Too low!")
        attempts += 1
    elif int(user_input) == secret_number:
        print(f"Correct! You guessed it in {attempts} attempts")
        break