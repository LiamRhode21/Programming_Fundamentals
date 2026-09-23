import random

random_int = random.randint(0,1)
head_or_tails = "heads"
answer = "wrong"
guess = input("Guess the coin flip! Enter heads or tails (h/t)")

#head_or_tails = "heads" if random_int == 0 else "tails"

if random_int == 1:
    head_or_tails = "tails"

if guess.upper() == "T" and random_int == 1 or guess.upper() == "H" and random_int == 0:
    answer = "right"

print(f"The coin flip was: {head_or_tails}")
print(f"You guessed {answer}!")
