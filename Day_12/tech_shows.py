shows = ["Silicon Valley", "Halt and Catch Fire", "Blackberry", "The Billion Dollar Code", "Mr. Robot", "The IT Crowd", "WeCrashed",
                 "The Social Network", "Severance", "Pirates of Silicon Valley"]

print(f"The best show is: {shows[0]}")
print(f"The most classic show is: {shows[len(shows) - 1]}")

shows[6] = "The Dropout"
shows[7] = "Black Mirror"

print(f"The fourth to ninth shows on the list are: {shows[4:9]}")

print("The top five shows are:")
for index, show in enumerate(shows[:5], start = 1):
    print(f"Ranked {index} is: {show}")
