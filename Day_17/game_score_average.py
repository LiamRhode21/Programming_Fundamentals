game_score = 0
total = 0
count = 0
invalid_entry = 0

while game_score != -1:
    try:
        game_score = int(input("Enter game score: "))

        if game_score > 100 or game_score < -1:
            raise ValueError("Game score must be between 0 and 100")

    except ValueError as error:
        print(f"please only enter integers: {error}")
        invalid_entry += 1
        continue

    if game_score != -1:
        total += game_score
        count += 1

try:
    score_average = total / count

except ZeroDivisionError:
    print("No values entered")

else:
    print(f"The average score is {score_average:.2f}")
    print(f"you had {invalid_entry} invalid entries")