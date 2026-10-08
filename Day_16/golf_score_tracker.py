scores = []
rounds = 0

while True:
    score = input("Enter a score (q to quit): ")

    if score.lower() == "q":
        break
    else:
        scores.append(int(score))
        rounds += 1

print(f"Scores: {scores}")
print(f"Rounds played: {rounds}")
if len(scores) == 0:
    print("No rounds played yet!")
else:
    avg_score = sum(scores) / len(scores)
    print(f"Average score: {avg_score}")
    best_score = min(scores)
    print(f"Best Score: {best_score}")
