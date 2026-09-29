bands = ["Abva", "Linkin park", "Paramore", "Limp bizkit", "Three days grace", "Powerwolf", "Onlyne"]

# For loops allow us to look at each element in a list
# band is a variable holding the value each time through the loop
for band in bands:
    print(f"{band} is a great band!")

songs = ["Astrothunder", "Don't touch my clogs", "My Soft Spots My Robots"]

# loop through the list and return indexes and values
for index, song in enumerate(songs):
    print(f"{song} is at index {index}")

for index, song in enumerate(songs):
    print(f"#{index + 1}. {song}")

for index, song in enumerate(songs, start = 1):
    print(f"#{index}. {song}")

# from this list of characters, use the tuple to print out only the character that are not from the dark side

characters = ["Han Solo", "Yoda", "Darth Maul", "Ashoka", "Anakin Skywalker", "Grevous"]

dark_side = ("Darth Maul", "Darth Vader", "Grevous")

for character in characters:
    if character not in dark_side:
        print(f"{character} is on the light side.")

# Using continue
for character in characters:
    if character in dark_side:
        continue # will go to the next iteration of the loop
    print(f"{character} is on the light side.")

# take above code and add the characters to a new light_side list

light_side = []
for character in characters:
    if character not in dark_side:
        light_side.append(character)
# display
for character in light_side:
    print(character)
